# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''
import base64
import json
import re
import time
import uuid

import tornado.web

import define
from api.basehandler import BaseHandler, CustomHTTPError
from user.account.accountmgr import AccountMgr, CustomMgrError


class CookieAuthHandler(BaseHandler):
    """
    验证cookie
    """
    def get(self):
        info = {"cookie": self.get_argument("cookie"),}
        try:
            user_mgr = AccountMgr()
            response = user_mgr.cookie_auth(**info)
            if not response:
                raise CustomHTTPError(401, error=define.C_EC_auth, cause=define.C_CAUSE_cookieMissing)
        except CustomMgrError, e:
            raise CustomHTTPError(401, error=define.C_EC_auth, cause=e.message)

        self.write(response)


class UserBaseHandler(BaseHandler):
    def get_current_user(self):
        cookie = self.get_secure_cookie(self.C_COOKIE)
        info = {"cookie": cookie}
        try:
            user_mgr = AccountMgr()
            response = user_mgr.cookie_auth(**info)
            if not response:
                raise CustomHTTPError(401, error=define.C_EC_auth, cause=define.C_CAUSE_cookieMissing)
        except CustomMgrError, e:
            raise CustomHTTPError(401, error=define.C_EC_auth, cause=e.message)

        return response


class RegisterHandler(UserBaseHandler):
    # 应该用post，为了方便测试暂时用get
    def post(self, *args, **kwargs):

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
            user_mgr = AccountMgr(db_session=self.db_session)
            user_mgr.register(**info)
        except CustomMgrError, e:
            raise CustomHTTPError(409, e.message)  # 不确定该用哪个code，502比较符合规则，但是前端接受不到原因


class LoginHandler(UserBaseHandler):
    def post(self):
        email = self.get_argument("user_name")
        password = self.get_argument("password")
        info = {
            "user_name": email,
            "password": password,
            "timestamp": time.time(),
        }
        try:
            user_mgr = AccountMgr(db_session=self.db_session)
            if not user_mgr.login(**info):
                raise CustomHTTPError(401, error=define.C_EC_auth, cause=define.C_CAUSE_wrongPassword)
        except CustomMgrError, e:
            raise CustomHTTPError(401, error=define.C_EC_auth, cause=define.C_CAUSE_accountNotExisted)

        rand_str = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
        self.set_secure_cookie(self.C_COOKIE, rand_str)
        info["cookie"] = rand_str  # self.get_secure_cookie(self.C_COOKIE)
        try:
            info.pop("password")
            user_mgr.cookie_cache(**info)
        except CustomMgrError, e:
            raise CustomHTTPError(401, error=define.C_EC_cacheError, cause=e.message)

class LogoutHandler(UserBaseHandler):
    """
    user logout
    """
    @tornado.web.authenticated
    def post(self):
        cookie = self.get_secure_cookie(self.C_COOKIE)
        try:
            user_mgr = AccountMgr()
            user_mgr.cookie_delete(cookie)
        except CustomMgrError, e:
            raise CustomHTTPError(401, error=define.C_EC_cacheError, cause=define.C_CAUSE_delKeyError)


class UserInfoHandler(UserBaseHandler):
    """
    获取用户信息
    """

    @tornado.web.authenticated
    def get(self):
        print "okkkke"
        # user_name = self.get_argument("user_name")
        pass
        self.write({
            "cause": "very good"
        })
