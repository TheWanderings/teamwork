# coding=utf-8
"""
user manager
@david
"""
import hashlib
import json
import os

# from _mysql_exceptions import InterfaceError, IntegrityError
import re

import requests

import config
import define
from logs import LoggerMgr
from user.db.dbclass import User
from sqlalchemy.exc import IntegrityError


class CustomMgrError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return repr(self.message)


class AccountMgr(object):
    """
    account manage
    """
    __ids = {}

    def __init__(self, session=None):
        self.__seesion = session
        self.__logger = LoggerMgr.getLogger()

    def register(self, **kwargs):
        """
        user register
        :param kwargs:
        :return:
        """
        id = self.__get_id(User.__tablename__)
        if not id:
            return None
        kwargs["uid"] = id
        # 加密
        m = hashlib.md5()
        m.update(kwargs["password"])
        kwargs["password"] = m.hexdigest()
        user = User(**kwargs)
        try:
            self.__seesion.add(user)
            self.__seesion.commit()
            self.__logger.info("add a user: {account}".format(**kwargs))
        except IntegrityError, e:
            msg = e.message
            # 从异常里找出是账号冲突还是邮箱冲突
            if msg.find("account") > 0:
                conflict = "account has existed"
            elif msg.find("email") > 0:
                conflict = "email has existed"
            else:
                conflict = msg
            raise CustomMgrError(conflict)

    def __get_id(self, db_name):
        """
        get primary id for db table
        :param db_name:
        :return:
        """
        ids = AccountMgr.__ids.get(db_name, None)
        if not ids:
            config.ConfigMgr.init(os.path.join(define.root, "config/user.yaml"))
            conf = config.ConfigMgr.get("id_server", {})
            # host = conf.get("host", "localhost")
            # port = conf.get("port", "10000")
            payload = {"type": db_name, "count": int(conf.get("{0}_req_num".format(db_name), 5)),}
            url = "http://{host}:{port}/allocate".format(**conf)
            response = requests.get(url=url, params=payload)
            if response.status_code == 200:
                result = json.loads(response.text)
                if result.get("data", None):
                    result["data"].reverse()
                    AccountMgr.__ids[db_name] = ids = result["data"]

        return ids.pop() if ids else None

    def login(self, **kwargs):
        """
        user login
        :param kwargs:
        :return:
        """
        result = self.__seesion.query(User.password).filter(User.email == kwargs["email"]).first()
        if result is None:
            raise CustomMgrError(define.C_CAUSE_accountNotExisted)
        m = hashlib.md5()
        m.update(kwargs["password"])
        encryopted_password = m.hexdigest()
        if result.password == encryopted_password:
            return True
        else:
            return False
