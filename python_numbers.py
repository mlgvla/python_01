# Integer
x = 10
print(type(x))

# Float
y = 3.14
print(type(y))

# Complex
z = 2 + 3j
print(type(z))

# Arithmetic operations
x = 10
y = 3
print(x + y)  
print(x - y) 
print(x * y) 
print(x / y) 
print(x ** y) 
print(x % y) 
print(x // y) # floor division

# abs()
number = -10
absolute_value = abs(number)
print(absolute_value)

# round()
number = 3.14159
rounded_number = round(number, 2)
print(rounded_number) 

# max() and min()
numbers = [5, 2, 8, 1, 9]
maximum_value = max(numbers)
minimum_value = min(numbers)
print(maximum_value) 
print(minimum_value)

print(max(5, 1, 8, 1, 9))
print(min(5, 1, 8, 1, 9))

# pow()
base = 2
exponent = 3
result = pow(base, exponent)
print(result)

# int()
number = 3.14
integer_value = int(number)
print(integer_value)

# float()
number = "3.14"
float_value = float(number)
print(float_value)

# complex()
real_part = 2
imaginary_part = 3
complex_number = complex(real_part, imaginary_part)
print(complex_number)

# Using the math module
import math

# sqrt()
number = 16
square_root = math.sqrt(number)
print(square_root) 

# Trigonometric functions
angle = math.pi / 4
sine_value = math.sin(angle)
cosine_value = math.cos(angle)
print(sine_value) 
print(cosine_value)

# Random numbers - use the random module
import random

random_integer = random.randint(1, 10)
random_float = random.uniform(0, 1)
print(random_integer)
print(random_float)

# format()
number = 3.14159
formatted_number = format(number, ".2f")
print(formatted_number)

# f-string formatting
number = 3.14159
formatted_number = f"{number:.2f}"
print(formatted_number)

# % operator
number = 3.14159
formatted_number = "%.2f" % number
print(formatted_number)

# Using round() and str()
number = 3.14159
formatted_number = str(round(number, 2))
print(formatted_number) 
print(type(formatted_number))