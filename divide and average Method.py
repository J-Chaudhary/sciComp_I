from math import *

def average(a, b):
    return (a + b) / 2.0

def improve(guess, x):
    return average(guess, x/guess)

def good_enough(guess, x):
    d = abs(guess*guess - x)
    return (d < 0.001)

def square_root(guess, x):
    while(not good_enough(guess, x)):
        guess = improve(guess, x)
        print (guess)
    return guess

def my_sqrt(x):
    r = square_root(1, x)
    return r


my_sqrt(25)
