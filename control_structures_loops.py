# If-Else Statements:
x = 10
if x > 0:
    print("Positive number")
else:
    print("Non-positive number")

# Elif
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade:", grade)

# For Loop
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

""""
When used in the "for" statement, "in" is used to iterate over elements 
in a sequence or collection.¸
It allows you to loop through each item in a sequence one by one, 
assigning the current item to a variable in each iteration.
"""

# While Loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Break and Continue Statements
for i in range(1, 10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

"""
break statement terminates the loop entirely.
continue statement skips the current iteration and moves to the next one.
"""

# Functions


def my_function():
    a = 5
    b = 10
    print(a + b)

my_function()