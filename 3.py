""" 3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text."""

print("Question 3")

string1 = input("Enter First String:  ")
string2 = input("Enter Second String:  ")

sort_string1 = sorted(string1.lower())
sort_string2 = sorted(string2.lower())

if sort_string1 == sort_string2:
    print("Anagram")
else:
    print("Not Anagram")

