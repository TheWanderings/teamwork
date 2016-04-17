# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''
import tornado.web
import define
from api.basehandler import BaseHandler, CustomHTTPError
import re

from user.account.accountmgr import AccountMgr, CustomMgrError


class SelfHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pass


class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):

        email = self.get_argument("email")
        p = re.compile(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
        if not p.match(email):
            raise CustomHTTPError(400, "invalid email")

        password = self.get_argument("password")
        p = re.compile(r"^[a-zA-Z]\w{5,17}$")
        if not p.match(password):
            raise CustomHTTPError(400, "invalid password")

        account = self.get_argument("account")
        image = self.get_argument("image", None)

        info = {
            "email": email,
            "password": password,
            "account": account,
            "image": image,
        }
        try:
            user_mgr = AccountMgr(session=self.db_session)
            user_mgr.register(**info)
        except CustomMgrError, e:
            raise CustomHTTPError(409, e.message)  # 不确定该用哪个code，502比较符合规则，但是前端接受不到原因





class LoginHandler(BaseHandler):
    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        # raise CustomHTTPError(401,
        #                       define.C_EC_wrongPassword,
        #                       cause=define.C_CAUSE_userMissing
        #                       )
