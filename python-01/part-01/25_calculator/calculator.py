'''
Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

Some examples of expected behaviour:

Sample output
Number 1: 10
Number 2: 17
Operation: add

10 + 17 = 27

Sample output
Number 1: 4
Number 2: 6
Operation: multiply

4 * 6 = 24

Sample output
Number 1: 4
Number 2: 6
Operation: subtract

4 - 6 = -2
'''

num_1 = int(input("Number 1:"))
num_2 = int(input("Number 2:"))
operation = input("Operation:")

if operation == "add":
    print(num_1, "+", num_2, "=", num_1 + num_2)
if operation == "subtract":
    print(num_1, "-", num_2, "=", num_1 - num_2)
if operation == "multiply":
    print(num_1, "*", num_2, "=", num_1 * num_2)
