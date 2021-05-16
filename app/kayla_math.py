""" 
What's up homie? This module is about math and liam and their gang. 
I just learned about style tips and best practices. Welcome to my world!
Style tips are hard. This is called kayla_math.py btw. 

"""

from math import sqrt, e, factorial
import decimal

def square(x): 
    return x*x

def hypotenuse (a,b): 
    
   c = sqrt(square(a) + square(b))
   return c
   

def exp(x,n):
    sum = 0.0
    for i in range (0, n+1):
        sum = (x**i)/float(factorial(i)) + sum 
        print (i,sum)
    return sum 
    
    
print (exp(1,100))









