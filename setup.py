import sys
from distutils.core import setup

if sys.version_info < (3, 0, 0):
    print('White Rabbit requires Python 3')

version = '1.0.3.1
mainscript = 'white-rabbit'

setup(
    name='White Rabbit',
    description='Console-based time management program',
    author='Vi Grey (http://pariahvi.com)',
    author_email='development@pariahvi.com',
    license='BSD',
    version=version,
    url='https://github.com/PariahVi/WhiteRabbit',
    scripts=[mainscript]
    )
