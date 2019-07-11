#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from logging import Logger
import logging.config

from oh_my_logging.builders import LoggerBuilderFactory
from oh_my_logging.decorators import log


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
    LoggerBuilderFactory(dictConfig)


def test_log_on_function1():
    @log
    def func(logger):
        assert isinstance(logger, Logger)
        logger.info('hello world')
        assert logger.root.handlers[0].message == 'hello world'

    func()


def test_log_on_function2():
    @log(log.STAT, log.ARGS, log.RETURNING)
    def func(a, b):
        return a + b

    func(1,2)
    assert 1 == 1

def test_log_onfunction3():
    @log(log.STAT, log.ARGS, log.RETURNING, {'target': log.ERROR, 'ignore_errors': (Exception,)})
    def func(a, b):
        raise Exception('123')
        return a + b

    func(1,2)
    assert 1 != 1

