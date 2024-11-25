#create a program to sum of three number from the user input
#if user doesn't enter any number, use default as 100,200,300
# Logic Building Formula

num1=int(input("enter the number one\n"))
num2=int(input("enter the number two\n"))
num3=int(input("enter the number three\n"))

def sum_of_three_number(num1=100,num2=200,num3=300):
    return num1+num2+num3
result=sum_of_three_number(num1,num2,num3)
print(result)
