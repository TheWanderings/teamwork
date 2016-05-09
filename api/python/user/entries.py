# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''

from user.handlers import LoginHandler, RegisterHandler, CookieAuthHandler, UserInfoHandler, LogoutHandler

entries = [
    # account
    (r"/register$", RegisterHandler),
    (r"/login$", LoginHandler),
    (r"/cookie_auth$", CookieAuthHandler),
    (r"/logout$", LogoutHandler),
    (r"/user_info$", UserInfoHandler),

]
