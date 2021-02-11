# sum of multiple argrument
def fun(*args):
    add = 0
    for i in args:
        add += i
    return add


add2 = fun(22, 33, 11, 44)
print("Sum:", add2)

# O/P
#Sum: 110