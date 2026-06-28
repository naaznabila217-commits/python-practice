#swapping using third variable
'''n = int(input("Enter first number to swap:"))
m = int(input("Enter second number to swap:"))
print("before swapping the numbers are:",n,m)
o = n
n = m
m = o
print("after swapping the numbers are:",n,m)'''







#swapping without using any third variable
n = int(input("Enter first number to swap:"))
m = int(input("Enter second number to swap:"))
n = n+m
m = n-m
n = n-m
print("after swapping the numbers are:",n,m)

