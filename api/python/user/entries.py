# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''

from user.handlers import SelfHandler, LoginHandler, RegisterHandler

entries = [
    # account
    (r"/register$", RegisterHandler),
    (r"/login$", LoginHandler),
    (r"^/self$", SelfHandler),
]
