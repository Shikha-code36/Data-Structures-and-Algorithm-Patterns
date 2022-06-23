'''                             
                                FIBONACCI
  A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.                              
                                '''

def Fibonacci(n):
  if n<0:
    return -1
  elif n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    fibo = Fibonacci(n-1) + Fibonacci(n-2)
    return fibo

print(Fibonacci(8)) #21
print(Fibonacci(0)) #0
print(Fibonacci(-1)) #-1

'''Leetcode Fibonacci Question
problem link - https://leetcode.com/problems/fibonacci-number/'''


  

