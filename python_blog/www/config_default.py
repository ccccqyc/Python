#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charles'

'''
Default configurations.
默认的配置文件完全符合本地开发环境，无需任何设置，可以立刻启动服务器.
'''

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}
