# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''

from userhandlers import SelfHandler, LoginHandler

entries = [
    # account
    (r"/login$", LoginHandler),
    (r"^/self$", SelfHandler),
]
