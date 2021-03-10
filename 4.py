""" 4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?"""

print("Question 4")

my_list = []
#print list id before appending
print(id(my_list))

#appending items into the list
my_list.append('Nischal')
my_list.append('Code')
my_list.append('Shakya')
#printing list and id of list after appending
print(my_list)
print(id(my_list))

#sorting the list
print(sorted(my_list))

