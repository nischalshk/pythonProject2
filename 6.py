""" 6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it."""

print("Question 6")

my_list = ['NIschal', 'Samrat', 'Anish', 'Sanil', 'John']
flag = 0

for items in my_list:
    if items.lower() == 'john':
        print('Found')
        flag = 1
        break

if flag == 0:
    print("Not Found")


