# Arithmetic Operators:
x = 10
y = 3

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y 
modulus = x % y 
exponentiation = x ** y
floor_division = x // y


# Comparison Operators:
x = 10
y = 3

equal_to = x == y 
not_equal_to = x != y 
less_than = x < y 
greater_than = x > y 
less_than_or_equal_to = x <= y 
greater_than_or_equal_to = x >= y 

# Assignment Operators
x = 10

x += 5  # x = 15
x -= 3  # x = 12
x *= 2  # x = 24
x /= 6  # x = 4.0
print(x)

# there is no x++ or ++x

# Logical Operators
x = 10
y = 3

logical_and = x > 5 and y < 2
logical_or = x > 5 or y < 2
logical_not = not (x > 5)

# Membership Operators
fruits = ["apple", "banana", "orange"]

in_operator = "apple" in fruits 
not_in_operator = "grape" not in fruits

# Identity Operators
m = 10
n = 10
z = [1, 2, 3] # is this equal to w?  What about in JavaScript?
w = [1, 2, 3]

"""
'==' compares by value
'is' compares lists by reference, like JavaScript
"""

is_operator = m is n 
is_not_operator = z is not w 
