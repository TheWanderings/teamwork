# coding: utf-8
'''
Created on 2015年12月11日

@author: AilenZou
'''
from .cachemgr import CacheMgr
import pickle
import redis


class RedisCacheMgr(CacheMgr):
    def __init__(self, timeoutSecond=0, **configs):
        self.__timeout = timeoutSecond
        self.__redisClient = redis.StrictRedis(**configs)
        
    def _do_get_from_cache(self, key):
        v = self.__redisClient.get(key)
        if v is None:
            return None
        return pickle.loads(v)
        
    def _do_save_cache(self, key, value, timeoutSecond=None):
        v = pickle.dumps(value)
        self.__redisClient.setex(key, 
                                 self.__timeout if timeoutSecond is None else timeoutSecond, 
                                 v
                                 )
        
    def _do_delete_cache(self, key):
        self.__redisClient.delete(key)
