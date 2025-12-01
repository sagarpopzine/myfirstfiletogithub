# def my_function():
#     x = 10  # Local variable
#     print(x)

# my_function()
# print(x) 

y = 20  # Global variable

def another_function():
    print(y)  # This will access the global variable 'y'

another_function()
print(y)  # This will print 20