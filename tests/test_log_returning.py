#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from logging import Logger
import logging.config

from oh_my_logging.builders import LoggerBuilderFactory
from oh_my_logging.decorators import log_returning


def setup_module(module):
    global dictConfig
    dictConfig = {
        'version': 1,
        'root': {
            'level': 'DEBUG',
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


def test_log_returning_on_function():
    @log_returning
    def func(name, num):
        return '{}.{}'.format(name, num)

    ret = func('oh_my_logging', 123)

    logger = LoggerBuilderFactory().builder(func).build()
    assert logger.root.handlers[0].message == (log_returning.__TEMPLATE % repr(ret))
