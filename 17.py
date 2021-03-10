""" 17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors."""

first_num = int(input("Enter First Number:  "))
second_num = int(input("Enter Second Number:  "))
op = input("Enter Operator:  ")
value = 0

if op == '/':
    if first_num == 0 or second_num == 0:
        print("0 Value error")
    else:
        print(first_num/second_num)
elif op == '+':
    print(first_num + second_num)
elif op == '-':
    print(first_num - second_num)
elif op == '*':
    print(first_num * second_num)
else:
    print("Invalid Operator")
