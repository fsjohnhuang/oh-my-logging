#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from functools import wraps

from .logger import logger


def log(*largs, **lkwargs):
    """
    Examples:
        1. Attach to function without arguments.
    >>> @log
        def func(logger):
            pass

        2. Log arguments passed to function, returning value, count the execution time and exceptions.
    >>> @log(log.ARGS, log.RETURNING, log.STAT, log.ERROR)
        def func():
            pass
        
        3. Log specific exceptions then ignore it.
    >>> @log({'target': log.ERROR, 'errors': (FileNotFoundException,), 'raise_again': False})
        def func():
            pass
    """

    # Inject logger object to function as the last parameter.
    if len(largs) == 1 and callable(largs[0]) and len(lkwargs.items()) == 0:
        return logger(largs[0])
