# coding: utf-8
'''
Created on 2016年2月16日

@author: AilenZou
'''

from .standard import StandardLogger
from .exceptions import UnknownKeyError


class LoggerFactory(object):
  
    '''
    classdocs
    '''
    __loggers = []

    @classmethod
    def init(cls, rootDir, configs):
        defalutLevel = configs.get("level", "info")
        for cfg in configs.get("loggers", []):
            if "level" not in cfg:
                cfg["level"] = defalutLevel
            if cfg["type"] == "standard":
                StandardLogger.init(rootDir, cfg)
                cls.__loggers.append(StandardLogger._logger)
            else:
                raise UnknownKeyError("unknown type: %s" % cfg["type"])

    @classmethod
    def getLogger(cls, filters=None):
        if filters is None:
            return cls.__loggers[0]