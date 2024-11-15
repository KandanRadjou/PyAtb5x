s1=float(input("enter the side s1\n"))
s2=float(input("enter the side s2\n"))
s3=float(input("enter the side s3\n"))
if s1==s2==s3:
    print("It is a equilateral triangle")
elif s1==s2:
    print("It is a isosceles")
else:
    print("It is a Scalene")
