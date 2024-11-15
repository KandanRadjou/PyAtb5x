# write a program to take a user age and let him know if he can go to the club
#21

# Logic building formula
# step 1
#figure out user input - data type - int
#o/p- string - user if he can go or not
#----------------------------------------------

# Step 2  rough logic (brute force)
# age >21 - User can go to club
# age <21 - User cant go to club


#Step 3 write the logic
age=int(input("enter your age\n"))
age=int(age)
if age>=21:
    print("can go to club")
else:
    print("cant go with this age")

#Step 4 check for the edge cases
#we should consider edge cases such as
#negative age or extremely high values - Program will break
#non-numeric input - ex. A B C
#age which is valid >130

#Step 5 Optimize with the code
#handle all the edge cases




