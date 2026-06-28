m = int(input("enter year:"))
n = int(input("enter month number(1 or 2 or 3 etc) to know number of days in it:"))
if m % 400 == 0 or m % 4 == 0 and m % 100 != 0:
    isleap = True
    print(m,"is a leap year")
else:
    isleap = False
    print(m,"is not a leap year")
    print("feb-28 days")
if n == 1:
    print("jan-31 days")
elif n == 2:
    if isleap:
        print("feb-29 days")
    else:
        print("feb-28 days")
elif n == 3:
    print("mar-31 days")
elif n == 4:
    print("apr-30 days")
elif n == 5:
    print("may-31 days")
elif n == 6:
    print("june-30 days")
elif n == 7:
    print("july-31 days")
elif n == 8:
    print("aug-31 days")
elif n == 9:
    print("sep-30 days")
elif n == 10:
    print("oct-31 days")
elif n == 11:
    print("nov-30 days")
else:
    print("dec-31 days")




