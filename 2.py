""" 2. Write an if statement to determine whether a variable holding a year is
a leap year."""

print("Question 2")

year = int(input("Enter a year:  "))

if year % 4 == 0:
    #checking whether the year is a century year or not
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap Year")
    else:
        print("Not Leap Year")
else:
    print("Not Leap Year")