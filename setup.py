# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)
setup(
    name='sloth',
    version='1.0.0',
    description="just pratice distributed program",
    author="hzhouzhe",
    setup_requires='setuptools',
    entry_points={
        'console_scripts': ['sloth=sloth.bootstrap.sloth:main']
    },
    install_requires=[
        'oslo.config>=1.2.0,<2.0.0'
    ],
    packages=find_packages()
)
