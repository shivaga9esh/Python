# Suppose we want to analyse texts in Latin alphabet (26 possible letters). For this we want to compute the frequencies of all possible 3-letter combinations in a text.
# For this we will need to store a number for each possible 3-letter combination. How many number we will have to store for a text?

x = pow(26, 3) #all possible - fully unordered - 26 * 26 * 26
print(x)

#How many 5-digit numbers are there that have digits 1, 2, 3, 4 and 5 (each of them exactly once)? # fully ordered
print(5 * 4 * 3 * 2 * 1)

#How many integer numbers between 0 and 9999 are there that have exactly one digit 7 and exactly one digit 2? # half ordered and hald un-ordered
print(4 * 3 * 8 * 8)

#Binomial Distribution is a Discrete Distribution. It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
#Given 10 trials for coin toss generate 10 data points:
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)
