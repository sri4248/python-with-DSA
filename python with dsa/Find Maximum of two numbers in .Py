#Find Maximum of two numbers in Python
a,b=list(map(int,input().split()))
print(max(a,b))
#using ternary operator
a=7
b=3
print(a if a>b else b)
#using if else statement
if a>b:
    print(a)
else:
    print(b)
