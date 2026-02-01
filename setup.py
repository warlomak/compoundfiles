#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# compoundfiles – Python library for reading/writing OLE Compound Files (CFB)
#
# Copyright (c) 2026 warlomak <warlomak@gmail.com>
#
# This code is licensed under the MIT License.
# You may use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of this software under the terms of the MIT License.
#
# Original project (forked from): https://github.com/waveform-computing/compoundfiles
# Original author: Dave Hughes <dave@waveform.org.uk>
#
# This file contains setup configuration for compound files.

"Library for parsing, reading, writing, and editing OLE Compound Documents (fork with writing and editing support, available via git)"

from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division,
    )
str = type('')

import os
import sys
from setuptools import setup, find_packages

if sys.version_info[0] == 2:
    if not sys.version_info >= (2, 7):
        raise ValueError('This package requires Python 2.7 or above')
elif sys.version_info[0] == 3:
    if not sys.version_info >= (3, 2):
        raise ValueError('This package requires Python 3.2 or above')
else:
    raise ValueError('Unrecognized major version of Python')

HERE = os.path.abspath(os.path.dirname(__file__))

# Workaround <http://bugs.python.org/issue10945>
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

# Workaround <http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html>
try:
    import multiprocessing
except ImportError:
    pass

__project__      = 'compoundfiles'
__version__      = '0.3'
__author__       = 'warlomak'
__author_email__ = 'warlomak@gmail.com'
__url__          = 'https://github.com/warlomak/compoundfiles'
__platforms__    = 'ALL'

__classifiers__  = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    ]

__keywords__ = [
    'microsoft',
    'ole',
    'compound',
    'document',
    ]

__requires__ = [
    ]

__extra_requires__ = {
    'doc': ['sphinx'],
    'test': ['pytest', 'coverage', 'mock'],
    }

__entry_points__ = {
    }

if sys.version_info[:2] == (3, 2):
    # The version of ipaddr on PyPI is incompatible with Python 3.2; use a
    # private fork of it instead
    __requires__.append('setuptools==18.4')
    __requires__.append('pip==7.0.0')
    __extra_requires__['doc'].extend([
        'Jinja2<2.7',
        'MarkupSafe<0.16',
        ])
    __extra_requires__['test'].remove('pytest')
    __extra_requires__['test'].append('pytest==2.9.2')
    __extra_requires__['test'].remove('coverage')
    __extra_requires__['test'].append('coverage<4.0dev')
    __extra_requires__['test'].append('attrs==16.2.0')
elif sys.version_info[:2] == (3, 3):
    __requires__.append('setuptools==30.1')


def main():
    import io
    with io.open(os.path.join(HERE, 'README.rst'), 'r') as readme:
        setup(
            name                 = __project__,
            version              = __version__,
            description          = __doc__,
            long_description     = readme.read(),
            classifiers          = __classifiers__,
            author               = __author__,
            author_email         = __author_email__,
            url                  = __url__,
            license              = [
                c.rsplit('::', 1)[1].strip()
                for c in __classifiers__
                if c.startswith('License ::')
                ][0],
            keywords             = __keywords__,
            packages             = find_packages(),
            package_data         = {},
            include_package_data = True,
            platforms            = __platforms__,
            install_requires     = __requires__,
            extras_require       = __extra_requires__,
            tests_require        = __extra_requires__.get('test', []),
            entry_points         = __entry_points__,
            )

if __name__ == '__main__':
    main()
