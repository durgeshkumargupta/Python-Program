while True:
    print("1.Check Value Error")
    print("2.Check File Not Found Error")
    print("3.Check Type Error")
    print("4.Check IOError")
    print("5.Check File Exist Error")
    print("0.Exit")
    n=int(input("Enter Choice:"))
    if n==1:
        try:
            f = open('abc.txt', 'r')
            print("Successfully")
        except ValueError:
            print("Value Error")
    elif n==2:
        try:
            f = open('abc2.txt', 'r')
            print("Successfully")
        except FileNotFoundError:
            print("File Not Found error")
    elif n==3:
        try:
            f = open('abc.txt', 'r', 'w')
            print("Successfully")
        except TypeError:
            print("Type Error")
    elif n==4:
        try:
            f = open('abc.txt', 'w+')
            f.write("Sample")
            f1 = open('ccc.txt', 'r')
            print("Successfully")
        except IOError:
            print("IO Error")
    elif n==5:
        try:
            f=open('abc2.txt','w')
            print("Successfully")
        except FileExistsError:
            print("File Exist Error")
    elif n==0:
        break
    else:
        print("Invalid input Please try again ")


