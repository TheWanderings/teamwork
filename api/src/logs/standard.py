# coding: utf-8
'''
Created on 2016年2月16日

@author: AilenZou
'''
from .logger import Logger

import logging
import os


class StandardLogger(Logger):
    _logger = None

    '''
    classdocs
    '''
    levelMap = {
        Logger.C_LEVEL_DEBUG: logging.DEBUG,
        Logger.C_LEVEL_INFO: logging.INFO,
        Logger.C_LEVEL_WARNING: logging.WARNING,
        Logger.C_LEVEL_ERROR: logging.ERROR,
    }
  
    @classmethod
    def init(cls, root, cfgs):
        cls._logger = logging.getLogger()
        fmtStr = "%(levelname)s-%(asctime)s-%(filename)s-%(lineno)d-%(funcName)s-%(threadName)s(%(thread)d): %(message)s"
        fmt = logging.Formatter(fmtStr)
        filePath = cfgs["path"]
        if not filePath.startswith("/"):
            filePath = os.path.join(root, filePath)
        hdl = logging.FileHandler(filePath)
        hdl.setFormatter(fmt)
        cls._logger.addHandler(hdl)
        lvl = cfgs.get("level", "info")
        cls.setLevel(lvl)
    
    @classmethod
    def setLevel(cls, level):
        cls._logger.setLevel(cls.levelMap[level])
