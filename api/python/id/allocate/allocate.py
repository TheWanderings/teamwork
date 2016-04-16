#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ""
__author__ = "adw"
__mtime__ = "2016/3/19"
__purpose__ = 
"""
import os

import config
import define
from logs import LoggerMgr
import redis


class IdManage(object):
    """
    manage all database primary key id
    """

    def __init__(self):
        self.__logger = LoggerMgr.getLogger()
        self.__redis_inst = self.get_redis_inst()

    def get_redis_inst(self):
        """
        get a redis instance
        :return:
        """
        config.ConfigMgr.init(os.path.join(define.root, "config/id.yaml"))
        redis_conf = config.ConfigMgr.get("redis", {})
        redis_host = redis_conf.get("host", "localhost")
        redis_port = redis_conf.get("port", 6379)

        return redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    def allocate_id(self, type, count):
        """
        get a id list by type
        :param count:
        :param type:
        :return:
        """
        id_list = None
        try:
            value = self.__redis_inst.get(type)
        except redis.ConnectionError, e:
            self.__logger.error("redis get failed %s" % e)
            return None
        start = int(value) if value else 1
        stop = start + count
        id_list = [x for x in xrange(start, stop)]

        try:
            self.__redis_inst.set(type, stop)
            self.__logger.info("{0} get {1} ids: {2}-{3}".format(type, count, id_list[0], id_list[-1]))
        except redis.ConnectionError, e:
            self.__logger.error("redis set failed %s" % e)
            return None

        return id_list


