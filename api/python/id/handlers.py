#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ""
__author__ = "adw"
__mtime__ = "2016/3/19"
__purpose__ = 
"""
import tornado.web

from allocate.allocate import IdManage
from api.basehandler import BaseHandler, CustomHTTPError


class AllocateHandler(BaseHandler):

    def get(self):
        """
        get database table primary key id
        :return: list
        """
        try:
            type = self.get_argument("type")
            count = self.get_argument("count")
        except Exception, e:
            raise CustomHTTPError(400, "invalid argument: %s" % e)
        id_mng = IdManage()
        id_list = id_mng.allocate_id(type=type, count=count)
        if id_list:
            response = {
                "data": id_list
            }
            self.write(response)
