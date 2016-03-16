# coding: utf-8
'''
Created on 2015年12月11日

@author: AilenZou
'''
from .cache import Cache
import pickle
import redis


class RedisCache(Cache):
    def __init__(self, logger, timeout=10, **configs):
        self.__timeout = timeout
        self.__configs = configs
        self.__redisClient = None
        self.logger = logger

    def __reconnect(self):
        self.__redisClient = redis.StrictRedis(**self.__configs)
        
    def _do_get_from_cache(self, key):
        try:
            v = self.__redisClient.get(key)
        except AttributeError:
            self.__reconnect()
            v = self.__redisClient.get(key)
        if v is None:
            return None
        return pickle.loads(v)
        
    def _do_save_cache(self, key, value, timeoutSecond=None):
        v = pickle.dumps(value)
        timeout = self.__timeout if timeoutSecond is None else timeoutSecond
        def do(key, timeout, v):
            self.logger.debug("timeout: %s", timeout)
            if timeout is not None:
                self.__redisClient.setex(key, 
                                         timeout, 
                                         v
                                         )
            else:
                self.__redisClient.set(key,
                                       v)
        try:
            do(key, timeout, v)
        except AttributeError:
            self.__reconnect()
            do(key, timeout, v)
        
    def _do_delete_cache(self, key):
        try:
            self.__redisClient.delete(key)
        except AttributeError:
            self.__reconnect()
            self.__redisClient.delete(key)
