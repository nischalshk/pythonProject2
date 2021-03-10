""" 14. Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys."""

def read_csv(filename):
    file = open("test/testing.txt")
    people = []
    all_lines = file.readlines()
    headers = all_lines[:1][0].replace("\n","").split(",")
    all_values = all_lines[1:]

    for line in all_values:
        values = line.replace("\n","").split(",")
        person = {}
        for i, header in enumerate(headers):
            person[header] = values[i]

        people.append(person)

    return people


print(read_csv("test/testing.txt"))