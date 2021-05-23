""" 
What's up homie? This module is about math and liam and their gang. 
I just learned about style tips and best practices. Welcome to my world!
Style tips are hard. This is called kayla_math.py btw. 

"""

from math import sqrt, factorial


def square(x: float)->float: 
    return x*x

def hypotenuse (a:float,b:float)->float: 
    
   c:float = sqrt(square(a) + square(b))
   return c
   

def exp(x:float,n:int)->float:
    sum = 0.0
    for i in range (0, n+1):
        sum = (x**i)/float(factorial(i)) + sum 
        print (i,sum)
    return sum 
    
    
print (exp(1,100))









