#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from functools import wraps

from .logger import logger


def log(*largs, **lkwargs):

    # Inject logger object to function as the last parameter.
    if len(largs) == 1 and callable(largs[0]) and len(lkwargs.items()) == 0:
        return logger(largs[0])

    lkwargs.get('')

    
