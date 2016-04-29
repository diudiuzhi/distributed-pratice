# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)
setup(
    name='distributed-pratice',
    version='1.0.0',
    description="just pratice",
    author="hzhouzhe",
    setup_requires='setuptools',
    entry_points={
        'console_scripts': ['distributed-pratice=distributed_pratice.node:main']
    },
    packages=find_packages()
)
