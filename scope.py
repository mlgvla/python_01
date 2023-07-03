global_var = 10  # Global variable

def modify_global():
    global global_var  # Declare the variable as global within the function
    global_var = 20    # Modify the global variable within the function

def print_global():
    print(global_var)  # Access the global variable from within another function

print_global()      
modify_global()
print_global()      

global_var = 10

def a_function():
    print(global_var)  # Accessing the global variable

a_function()

# Scope

# Global vs Local Scope
global_var = 10

def my_function():
    global_var = 5
    print(global_var)  # Is this "global_var" global or local?

my_function() 
print(global_var)



# Local Scope
def my_new_function():
    local_var = 5
    print(local_var)  # Accessing the local variable

my_new_function() 

# Enclosing Scope
def outer_function():
    outer_var = "Hello"

    def inner_function():
        return outer_var  # Accessing the variable from the outer scope

    return inner_function

my_very_new_function = outer_function()
print(my_very_new_function()) 


