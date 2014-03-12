import sys
from distutils.core import setup

if sys.version_info < (3, 0, 0):
    print('White Rabbit requires Python 3')

version = '2.0.0'
mainscript = 'white-rabbit'

setup(
    name='White Rabbit',
    description='Console-based time management program',
    author='Violet (PariahVi)',
    author_email='violet@pariahvi.com',
    license='BSD',
    version=version,
    url='https://bitbucket.org/PariahVi/white-rabbit',
    scripts=[mainscript]
    )
