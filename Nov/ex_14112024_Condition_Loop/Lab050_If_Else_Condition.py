# program find the Max number between three numbers

# Logic building
# user i/p- num1,num2,num3 -- int
# o/p-int or string with max number


num1 = int(input("enter the num1\n"))
num2 = int(input("enter the num2\n"))
num3 = int(input("enter the num3\n"))

# syntax
# logic - if else - 1 condition
# if condition 1:
#          print("do 1")
# elif condition 2:
#          print("do 2")
# elif condition 3:
#          print("do 3")
# else:
#          print("do for else")

# 5>3,5>2----->5
# num1>num2 and num1>num3--->num1

# 12>10 and 12>11 ----->12
# num2>num1 and num2>num3---->num2

# num3

if num1 > num2 and num1 > num3:
    print("max num is", num1)
elif num2 > num1 and num2 > num3:
    print("max num is", num2)
else:
    print("max num is", num3)
