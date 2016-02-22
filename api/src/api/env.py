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


def init():
    config.ConfigMgr.init(os.path.join(define.root, "config/api.yaml"))
    with open(os.path.join(define.root, "config/api-logger.yaml"), 'r') as s:
        c = yaml.load(s)
        logs.LoggerMgr.init(define.root, c)
