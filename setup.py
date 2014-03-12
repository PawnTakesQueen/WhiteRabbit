#!/usr/bin/env python3

'''
    py2app/py2exe build script for White Rabbit.

    Will automatically ensure that all build prerequisites are available
    via ez_setup

    Usage (Linux):
        python2 setup.py install

    Usage (Mac OS X):
        python2 setup.py py2app
'''

import sys
from distutils.core import setup

if sys.version_info < (3, 0, 0):
    print('White Rabbit requires Python 3')

VERSION = '2.0.0'
mainscript = 'white-rabbit'

if sys.platform == 'darwin':
    extra_options = dict(
        setup_requires=['py2app'],
        app=[mainscript],
        # Cross-platform applications generally expect sys.argv to
        # be used for opening files.
        options=dict(py2app=dict(argv_emulation=True)),
    )
else:
    extra_options = dict(
        # Normally unix-like platforms will use "setup.py install"
        # and install the main script as such
        scripts=[mainscript],
        )

setup(
    name='White-Rabbit',
    description='Console-based time management program',
    author='Violet (PariahVi)',
    author_email='violet@pariahvi.com',
    license='BSD',
    version=VERSION,
    url='https://bitbucket.org/PariahVi/white-rabbit',
    **extra_options
    )
