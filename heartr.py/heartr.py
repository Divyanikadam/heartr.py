import math
from turtle import *

def heart(k):
    return 15 * math.sin(k)**3

def heart1(k, n):
    return 12 * math.cos(n) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(1000)
bgcolor('black')

n = 0  # Define the value of n outside the loop
for i in range(6000):
    goto(heart(i) * 20, heart1(i, n) * 20)  # Provide the value of n to heart1
    for j in range(6):
        color('white')

done()
