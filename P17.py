# sum of multiple argument
def fun(args):
    add = 0
    for i in args:
        add += int(i)
    return add


list1 = list(input("Enter Data:").split(" "))
sum2 = fun(list1)
print("Sum of multiple argument:",sum2)


# O/P
#Enter Data:22 33 44 55
#Sum of multiple argument: 154