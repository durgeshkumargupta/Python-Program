try:
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    c2=n1/n2

except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero Divisible Error")
except NameError:
    print("Name Error")
except KeyboardInterrupt:
    print("Keyboard Interrupted Error")
except TypeError:
    print("Type Error")
except Exception:
    print("Other type of Exception")
else:
    print("Successful")

