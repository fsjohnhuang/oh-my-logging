#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from logging import Logger
import logging.config

from oh_my_logging.builders import LoggerBuilderFactory
from oh_my_logging.decorators import logger


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


def test_logger_on_function():
    @logger
    def func(logger):
        assert isinstance(logger, Logger)
        logger.info('hello world')
        assert logger.root.handlers[0].message == 'hello world'

    func()
