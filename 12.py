""" 12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed."""

def palindrome(data):
    revered_str = data[::-1].lower()

    if revered_str == data.lower():
        return True
    else:
        return False

print(palindrome("Madam"))

print(palindrome("Nischal"))
