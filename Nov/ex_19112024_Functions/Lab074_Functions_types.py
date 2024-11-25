# they cant return ->non Return
# no return type and no parameter/argument----NRNP

#1.# they cant return ->non Return
def greet():
        print("hello")
greet()

#2.No return type and with argument/parameter

def greet_by_name(name):
    print("hello",name)
greet_by_name("kandan")

#3.No return type and with default argument(Positional argument)
def say_hello_default_arg(name="kandan"):
    print("hello",name.upper())

say_hello_default_arg("Mr.")
say_hello_default_arg()

def multiple_args(name1="a",name2="b"):
    print("MUL->",name1,name2)
multiple_args()
multiple_args(name1="kandan")
multiple_args(name1="Mr",name2="Kandan")

#math.pow()

#4.Arguement + return Type

def sum_of_two(a,b):
    return a+b
result= sum_of_two(a=4,b=60)
print(result)

def sum_of_two_number_with_default(num1=100,num2=300):
    return(num1+num2)
result=sum_of_two_number_with_default(num1=2000,num2=9000)
print(result)