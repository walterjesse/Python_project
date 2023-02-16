x=1
marks=50
grades=58
#if statement
if x>0:
    print("The number is positive")
    print(4+10)
#if.. else statement
if marks>=60:
    print("You passed")
else:
    print("You failed")

#if...elif...else
if grades<=29 and grades>=0:
    print("You failed")
elif grades<=49 and grades>=30:
    print("Fair")
elif grades<=79 and grades>=50:
    print("you have credid")
elif grades<=100 and grades>=80:
    print("you have Passed")
else:
    print("wrong entry")

