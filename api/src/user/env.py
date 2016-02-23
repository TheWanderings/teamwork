# coding: utf-8
'''
Created on 2016年2月18日

@author: AilenZou
'''

import os
import define
import config
import logs
import yaml
import cache


def init():
    config.ConfigMgr.init(os.path.join(define.root, "config/user.yaml"))
    with open(os.path.join(define.root, "config/user-logger.yaml"), 'r') as s:
        c = yaml.load(s)
        logs.LoggerMgr.init(define.root, c)
    redisConfig = config.ConfigMgr.get("redis", 
                                       {
                                            "host": "localhost",
                                            "port": 6379,
                                        })
    cacheMgr = cache.RedisCacheMgr(**redisConfig)
    
