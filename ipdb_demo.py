# import ipdb

def divide(a, b):
    result = a / b
    return result

def multiply(a, b):
    result = a + b
    return result

def complex_calculation(a, b):
    result1 = divide(a, b)
    result2 = multiply(a, result1)
    return result2

def main():
    # ipdb.set_trace() # Set a breakpoint
    print("In main")
    a = 10
    b = 2
    result = complex_calculation(a, b)
    print("Result:", result)

if __name__ == '__main__':
    main()
