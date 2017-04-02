#!/usr/bin/env python

from distutils.core import setup
from hannakageul import __version__

setup(
    name='hannakageul',
    version=__version__,
    description='Hangeul - Kana encoding converter',
    author='Mirai Kim',
    author_email='nachtbeere@outlook.com',
    url='https://github.com/noxowl/hannakageul',
    packages=['hannakageul', 'hannakageul.convert'])