# write a python program to calculate the area of circle given its radius using the

#logic building formula

# step1 figure out the inputs and outputs
#input - r - data type -> float
#pi=3.14
#power - pow or ** -> any either we can use
# o/p  -> float-area,print area

#Step 2
# rough logic = area=3.14 * pow(r,2)

#Step 3

radius=float(input("enter the radius of the circle\n"))
print(radius)
area=3.14 * (radius**2)
print("area of the circle is->",area)
print(f"area of the circle is :{area}")