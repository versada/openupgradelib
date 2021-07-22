#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import openupgradelib

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


dirname = os.path.dirname(__file__)

test_requirements = [
    'coverage',
    'flake8',
    'pep8-naming',
    'mock',
]

setup(
    name='openupgradelib',
    version=openupgradelib.__version__,
    description=openupgradelib.__doc__,
    long_description='',
    author=openupgradelib.__author__,
    author_email=openupgradelib.__email__,
    url='https://github.com/OCA/openupgradelib',
    packages=['openupgradelib'],
    package_dir={'openupgradelib': 'openupgradelib'},
    include_package_data=True,
    install_requires=["lxml", "cssselect"],
    license=openupgradelib.__license__,
    zip_safe=False,
    keywords='openupgradelib',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
