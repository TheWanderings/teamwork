#coding: utf-8
'''
Created on 2015年12月15日

@author: AilenZou
'''

from .exceptions import *

class Logger(object):
  C_LEVEL_DEBUG = "debug"
  C_LEVEL_INFO = "info"
  C_LEVEL_WARNING = "warning"
  C_LEVEL_ERROR = "error"
  
  @classmethod
  def init(cls, configs):
    raise UnimplementedError()
  
  @classmethod
  def setLevel(cls, level):
    raise UnimplementedError()
  
  @classmethod
  def log(cls, level, message, *args, **kwargs):
    raise UnimplementedError()

  @classmethod
  def debug(cls, message, *args, **kwargs):
    cls.log(Logger.C_LEVEL_DEBUG, message, *args, **kwargs)

  @classmethod
  def info(cls, message, *args, **kwargs):
    cls.log(Logger.C_LEVEL_INFO, message, *args, **kwargs)

  @classmethod
  def warning(cls, message, *args, **kwargs):
    cls.log(Logger.C_LEVEL_WARNING, message, *args, **kwargs)

  @classmethod
  def error(cls, message, *args, **kwargs):
    cls.log(Logger.C_LEVEL_ERROR, message, *args, **kwargs)

  @classmethod
  def exception(cls, message, *args, **kwargs):
    cls.log(Logger.C_LEVEL_ERROR, message, *args, **kwargs)
