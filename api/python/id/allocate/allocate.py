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
        self.__redis_inst = None
        self.__logger = LoggerMgr.getLogger()

    def get_redis_inst(self):
        """
        get a redis instance
        :return:
        """
        config.ConfigMgr.init(os.path.join(define.root, "config/id.yaml"))
        redis_conf = config.ConfigMgr.get("redis", {})
        redis_host = redis_conf.get("host", "localhost")
        redis_port = redis_conf.get("port", 6379)

        pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=0)
        self.__redis_inst = redis.Redis(connection_pool=pool)

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
            start = int(value) if value else 1
            stop = start + count
            id_list = [x for x in xrange(start, stop)]
            self.__redis_inst.set(type, stop)
        except Exception, e:
            self.__logger.error("allocate id failed %s" % e)

        return id_list

