n=int(input("enter 1st number:"))
m=int(input("enter 2nd number:"))
o=int(input("enter 3rd number:"))
if n > m and n > o:
    print(n,"is greater than among all")
elif m > n and m > o:
    print(m,"is greater than among all")
else:
    print(o,"is greater than among all")