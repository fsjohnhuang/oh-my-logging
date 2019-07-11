#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from logging import Logger
import logging.config

from oh_my_logging.builders import LoggerBuilderFactory
from oh_my_logging.decorators import log_stat


def setup_module(module):
    global dictConfig
    dictConfig = {
        'version': 1,
        'root': {
            'level': 'ERROR',
            'handlers': ['memory'],
        },
        'handlers': {
            'memory': {
                'class': 'oh_my_logging.handlers.MemoryHandler',
                'formatter': 'default',
            },
        },
        'formatters': {
            'default': {
                'format': '%(message)s',
            },
        },
    }
    LoggerBuilderFactory.unsafe_clear()
    LoggerBuilderFactory(dictConfig)


def test_log_stat_on_function():
    @log_stat
    def func(name, num):
        return '{}.{}'.format(name, num)

    ret = func('oh_my_logging', 123)

    assert func.__log_stat == 0
