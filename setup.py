#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import io

from setuptools import setup, find_packages

NAME = 'oh-my-logging'
DESCRIPTION = 'Enhancement for logging.'
URL = ''
EMAIL = 'fsjohnhuang@hotmail.com'
AUTHOR = 'fsjohnhuang'
PYTHON_REQUIRES = '>=2.7'
VERSION = '0.1.0'

REQUIRED = [
    'pyyaml',
]

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace('-', '_').replace(' ', '_')
    with io.open(os.path.join(here, project_slug, '__version__.py'), encoding='utf-8') as f:
        exec(f.read(), about)
else:
    about['version'] = VERSION

setup(
    name=NAME,
    version=about['version'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    url=URL,
    python_requires=PYTHON_REQUIRES,
    #packages=find_packages(where='./src/oh_my_logging', include=['*']),
    package_dir={'':'src'},
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
)
