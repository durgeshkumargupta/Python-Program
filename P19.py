# sum of first even number
def fun(args):
    add = 0
    while(args>=0):
        if (args % 2 == 0):
            add += args
        args-=1
    return add


limit = int(input("Enter limited data:"))
print("Sum of even number:", fun(limit))

#O/P
#Enter limited data:10
#Sum of even number: 30
