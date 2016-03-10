'''
Created on 2016年3月10日

@author: AilenZou
'''

from .rediscache import RedisCache
from cache.exces import UnsupportedError

class CacheMgr(object):
    '''
    Manager for caches.
    '''
    __cache = None

    @classmethod
    def init(cls, type, **configs):
        '''
            Init the cache mgr.
            @param type: 缓存类型，目前支持有"redis"
            @param configs: 针对此类型对应的配置
        '''
        if type == "redis":
            __cache = RedisCache(**configs)
        else:
            raise UnsupportedError()
    
    @classmethod
    def getCache(cls):
        return cls.__cache