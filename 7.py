""" 7. Create a list of tuples of first name, last name, and age for your friends
and colleagues. If you don't know the age, put in None. Calculate the
average age, skipping over any None values. Print out each name,
followed by old or young if they are above or below the average age."""

print("Question 7")

age_list = []

my_list = [('Nischal', 'Shakya', None), ('Samrat', 'Shrestha', 24), ('Rama', 'Gopal', 25)]

sum=0

count=0

for first_name, last_name, age in my_list:
    age_list.append(age)

for i in age_list:
    if type(i) == int:

        sum = sum + i

        count = count + 1

aveg = sum/count

print(aveg)

for first_name, last_name, age in my_list:
    if age == None:
        continue
    elif age > aveg :
        print(first_name, last_name + ' older than average')
    else:
        print(first_name, last_name + ' younger than average')
