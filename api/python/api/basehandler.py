# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''
import tornado.web
import define


class CustomHTTPError(tornado.web.HTTPError):
    def __init__(self, status_code, error, cause=None, log_message=None, *args, **kwargs):
        self.error = error
        self.cause = cause
        super(CustomHTTPError, self).__init__(status_code, log_message, *args, **kwargs)


class BaseHandler(tornado.web.RequestHandler):
    C_COOKIE = "cookie"
    
    def get_current_user(self):
        cookie = self.get_secure_cookie(self.C_COOKIE)
        if not cookie:
            raise CustomHTTPError(401, define.C_EC_auth, cause=define.C_CAUSE_cookieMissing)
        # TODO
    
    def write_error(self, status_code, **kwargs):
        if status_code >= 500:
            tornado.web.RequestHandler.write_error(self, status_code, **kwargs)
        elif "exc_info" in kwargs:
            _, err, _ = kwargs['exc_info']
            if isinstance(err, CustomHTTPError):
                self.write({
                            "error": err.error,
                            "cause": err.cause,
                            })
            else:
                tornado.web.RequestHandler.write_error(self, status_code, **kwargs)
        else:
            tornado.web.RequestHandler.write_error(self, status_code, **kwargs)
