# program to find the max between two

# Logic building formula
# Step 1
# User i/p - two integers
# User o/p - int 1 which ever is greater max number it will return.
# 31.54 or 55.36  - float

num1=float(input("enter the num 1\n"))
num2=float(input("enter the num 2\n"))
if num1 >= num2:
    print("max num is",num1)
else:
    print("max num is",num2)
#edge cases- num1==num2
# string - A B C, Ten -> try and except - we will learn in future
#-ve value - we will learn this in future.