#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from logging import Logger
import logging.config

from oh_my_logging.builders import LoggerBuilderFactory
from oh_my_logging.decorators import log_error


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


def test_logger_on_function():
    @log_error(ignore_errors=(Exception,))
    def func():
        raise Exception('123')
    
    func()

    assert 1 == 1
