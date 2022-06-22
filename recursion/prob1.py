'''
                        FACTORIAL
The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1.
'''

def factorial(n):
    if n==1:
        return n
    elif n<0:
        return -1
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(-5)) #-1
print(factorial(5)) #120
print(factorial(0)) #1
