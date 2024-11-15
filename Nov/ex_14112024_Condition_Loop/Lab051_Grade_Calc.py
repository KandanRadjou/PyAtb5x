# A:90 - 100
# B:80 - 89
# C:70 - 79
# D:60 - 69
# F:0  - 59

# Logic building formula

# 1 --> user i/P ----- Score or marks ---> int
# 2 --> User o/P ----- A or B

score = int(input("enter your score\n"))

# Score >=90  and <=100 --"A"
# score >=80  and <=89 --"B"
# score >=70  and <=79 --"c"
# score >=60  and <=69 --"D"
# score >=0  and <=59 --"F"

if score >= 90 and score <= 100:
    print("your grade is", "A")
elif score >= 80 and score <= 89:
    print("your grade is", "B")
elif score >= 70 and score <= 79:
    print("your grade is", "C")
elif score >= 60 and score <= 69:
    print("your grade is", "D")
elif score >= 100:
    print("your are a Master")
else:
    print("your grade is", "F")
