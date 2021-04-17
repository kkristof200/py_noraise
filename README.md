# noraise

![PyPI - package version](https://img.shields.io/pypi/v/noraise?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/noraise?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/noraise?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/noraise?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/py_noraise?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/py_noraise?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/py_noraise?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/py_noraise?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/py_noraise?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/py_noraise?label=repo%20license&style=flat-square)

## Description

Lightweight utility package, that provides a function decorator to easily catch and print exceptions

## Install

~~~~bash
pip install noraise
# or
pip3 install noraise
~~~~

## Usage

~~~~python
from noraise import noraise

@noraise(print_exc=True, return_exception=True)
def f2():
    return 1/0

res = f2()
print(type(res), res)

# This will not catch the crash, and print
# 
# 
# < ----------------------------------------------- Caught with @noraise ---------------------------------------------- >
# 
# Traceback (most recent call last):
#   File "/Users/kristofk/github/py_noraise/noraise/noraise.py", line 32, in wrapper
#     return function(*args, **kwargs)
#   File "demo.py", line 5, in f2
#     return 1/0
# ZeroDivisionError: division by zero
# 
# < -------------------------------------------------------------------------------------------------------------------- >
# 
# 
# <class 'ZeroDivisionError'> division by zero
~~~~

## Dependencies