from noraise import noraise

@noraise(print_exc=True)
def f2():
    return 1/0

res = f2()
print(type(res), res)