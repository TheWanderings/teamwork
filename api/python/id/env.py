#!/usr/bin/env python
#coding:utf-8
"""
__title__ = ""
__author__ = "adw"
__mtime__ = "2016/3/19"
__purpose__ = 
"""
import os
import define
import config
import logs
import yaml
import cache


def init():
    config.ConfigMgr.init(os.path.join(define.root, "config/id.yaml"))
    with open(os.path.join(define.root, "config/id-logger.yaml"), 'r') as s:
        c = yaml.load(s)
        logs.LoggerMgr.init(define.root, c)
    logger = logs.LoggerMgr.getLogger()



def finish():
    logger = logs.LoggerMgr.getLogger()
    logger.info("finish now")