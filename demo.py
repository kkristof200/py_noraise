# from noraise import noraise

# @noraise(print_exc=True)
# def f2():
#     return 1/0

# res = f2()
# print(type(res), res)


def decorator(function):
    def wrapper(*args, **kwargs):
        print('wrapper over \'{}\''.format(function.__name__))
        return function(*args, **kwargs)

    return wrapper

@decorator
def f1(a: int):
    print(a)

f1(1)




def decorator_with_param(param: int):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print('wrapper with param \'{}\' over \'{}\''.format(param, function.__name__))
            return function(*args, **kwargs)

        return wrapper
    return real_decorator

@decorator_with_param(param=5)
def f2(a: int):
    print(a)

f2(1)