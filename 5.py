""" 5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age."""

print("Question 5")


my_tup = ('Nischal', 'Shakya', 22)

fren_tup1 = ('Raja', 'Dhakal', 20)

fren_tup2 = ('Samrat', 'Shrestha', 29)


people = []


#appending tuples to people list
people.append(my_tup)
people.append(fren_tup1)
people.append(fren_tup2)

#sorted with firstname
print(sorted(people))

#sorting according to age
print(sorted(people, key=lambda x:x[-1]))

#sorting according to lastname
print(sorted(people, key=lambda x:x[1]))
