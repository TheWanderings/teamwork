#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ""
__author__ = "adw"
__mtime__ = "2016/3/19"
__purpose__ = 
"""
import tornado.web
import define
import allocate.allocate

from api.basehandler import BaseHandler, CustomHTTPError
from allocate.allocate import IdMng


class AllocateHandler(BaseHandler):

    def get(self):
        """
        get database table primary key id
        :return: list
        """
        type = self.get_argument("type", None)
        count = self.get_argument("count", 10)
        id_mng = IdMng()
        id_list = id_mng.allocate_id(type=type, count=count)
        if id_list:
            self.write(id_list)
