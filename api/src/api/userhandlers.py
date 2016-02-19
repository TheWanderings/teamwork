# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''
import tornado.web
from .basehandler import BaseHandler


class SelfHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pass
