from noraise import noraise

@noraise(print_exc=True, return_exception=True, ignored_error_types=[ZeroDivisionError])
def f2():
    return 1/0

res = f2()
print(type(res), res)

# This will not catch the crash, and print
# 
# 
# < ------------------------------------- Caught with @noraise ------------------------------------ >
#
# Traceback (most recent call last):
#   File "/Users/kristofk/github/py_noraise/noraise/noraise.py", line 32, in wrapper
#     return function(*args, **kwargs)
#   File "demo.py", line 5, in f2
#     return 1/0
# ZeroDivisionError: division by zero
# 
# < ----------------------------------------------------------------------------------------------- >
# 
# 
# <class 'ZeroDivisionError'> division by zero