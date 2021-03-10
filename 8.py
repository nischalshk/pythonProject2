""" 8. Write a function, is_prime, that takes an integer and returns True if the number is
 prime and False if the number is not prime."""

print("Question 8")


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
    

print(test_prime(9))
