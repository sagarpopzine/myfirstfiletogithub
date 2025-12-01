def factorial(n):
 if n == 0 or n == 1:
    return 1
    return n * factorial(n-1)
num=int(input("enter a num: "))
print("the factorial of",num,"is",factorial(num))