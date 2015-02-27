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
    platforms='No particular restrictions',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
        'Topic :: Other/Nonlisted Topic'
    ]
)
