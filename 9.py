""" 9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found."""

print("Question 9")

position = 0
list = [2,4,5,8,10,15,18,25,28,35,48,50]


def binary_search(list, n):

    lower_bound = 0
    upper_bound = len(list) - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if list[mid] == n:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < n:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1

    return False


if binary_search(list,50):
    print("Found at: ", position)
else:
    print("Not Found")
