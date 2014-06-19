import sys
from distutils.core import setup

if sys.version_info < (3, 0, 0):
    print('White Rabbit requires Python 3')

version = '1.0.3.0= 'white-rabbit'

setup(
    name='White Rabbit',
    description='Console-based time management program',
    author='PariahVi (http://pariahvi.com)',
    author_email='vi@pariahvi.com',
    license='BSD',
    version=version,
    url='https://github.com/PariahVi/white-rabbit',
    scripts=[mainscript]
    )
