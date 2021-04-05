# comparison on unordered pairs of elements or people - Hint: Make sure you only compare once and not twice
#comparision here is made only between 2 (say a,b in ab, ba ways)
n = 10
print(n * (n-1) / 2)

#or
import scipy.special
print(scipy.special.binom(10, 2))

#Suppose you are planning a road trip and you have five friends, but you can fit only three of them in your car.
#How many ways do you have to do it?

# _ _ _ => 5 * 4 * 3 possibilities - ordered and exactly once - comparision here is made only between 3. that will be 3 * 2 unordered possibilities
print((5 * 4 * 3)/ (3 * 2))

#or
import scipy.special
print(scipy.special.binom(5, 3))

#Assignment - no subset
n=8
count = 0

#Formula: ((8* 7 * 6)/ (3 * 2))
#print((8* 7 * 6)/ (3 * 2))

for i in range(n):
    for j in range(n):
        for k in range(n):
           if i < j and j < k:
                count += 1

print(count)


#Question 1 - with subset(k!)
#Suppose we have a dataset of size 12 and we want to construct a subset of data of size 6. How many ways do we have to do it?
#Formuala:
#n!/(n−k)!k!
import math
print(math.factorial(12)/ (math.factorial(12 - 6) * math.factorial(6)))

# or
# Better version of Code
#Formuala: (n-1 choose k-1) + (n-1 choose k)
C = dict() # C[n,k] is equal to n choose k

for n in range(13):
    C[n, 0] = 1
    C[n, n] = 1
    for k in range(1, n):
        C[n, k] = C[n - 1, k - 1] + C[n - 1, k]

print(C[12, 6])

#or
import scipy.special
print(scipy.special.binom(12, 6))


#Let's enumerate the rows of Pascal's triangle starting with 0. What is the sum of all the elements in the fifth row of Pascal's triangle
C = dict() # C[n,k] is equal to n choose k
for n in range(6):
    C[n, 0] = 1
    C[n, n] = 1
    for k in range(1, n):
        C[n, k] = C[n - 1, k - 1] + C[n - 1, k]

print(C[5, 0]+ C[5, 1]+ C[5, 2]+ C[5, 3]+ C[5, 4]+ C[5, 5])

# or
print(pow(2, 5))

# or
import scipy.special
print(scipy.special.binom(5, 0)+ scipy.special.binom(5, 1)+ scipy.special.binom(5, 2)  # scipy.special.binom(n, k) is equal to n choose k
      + scipy.special.binom(5, 3)+ scipy.special.binom(5, 4)+ scipy.special.binom(5, 5))



#What is the sum of all the elements from the first six rows of Pascal's triangle (all of the rows are depicted below)?
#print(pow(2, 0)+ pow(2, 1)+ pow(2, 2)+ pow(2, 3)+ pow(2, 4)+ pow(2, 5))


#Suppose we have a dataset of size 12 and we want to split it into two subsets of data of size 6
# (and it does not matter, which of the subsets is the first and which is the second). How many ways do we have to do it?
#print(math.factorial(12)/ (math.factorial(12 - 6) * math.factorial(6) * math.factorial(2)))


# what is the number of 5-card hands dealt off a standard 52-card deck ?
import scipy.special
print(scipy.special.binom(52, 5))

# what is the number of 5-card hands with 2 hearts and 3 spades ? hint: total of 13 hearts and 13 spades in standard pack
# 13 choose 2 hearts * 13 choose 3 spades
print(scipy.special.binom(13, 2) * scipy.special.binom(13, 3))

# 13 choose 4 hearts * 13 choose 1 spades
print("--> {0}".format(scipy.special.binom(13, 4) * scipy.special.binom(13, 1)))

###count of 4 ____ digit numbers containing 7 - considering atleast one 7 is must

#Straight forward approach
#print( 10 * 10 * 10 * 10)  - but how can we know atleast one 7 is present in the combinations ?
total = pow(10, 4)

#backward approach
# first - compute for the ones that does not have digit 7  _ _ _ _ 9 * 9 * 9 * 9
no_seven_digit = pow(9, 4)

#answer
print(total - no_seven_digit)


#### How many 4 digit numbers _ _ _ _ are there such that their digits are decreasing. Three digit numbers are also four-digit, they just start with 0
#solution : We have combinations of size 4 from 10 options
print(scipy.special.binom(10, 4))

##What is the number of bit-strings (that is, strings consisting of 0's and 1's) of length 8 where the number of 0's is equal to the number of 1's?

#In a bit string of length 8 you have 8 'places' to place a 0 or 1. When you have an equal number of 0's and 1's, you have 4 0's and 4 1's.
# When you have chosen were to place the 0's in the bit string the indices of the 1's are automatically determined.
#You have 8 choose 4
print(scipy.special.binom(8, 4))


#############################################################################################################################################################
print("-------------------------------------")
#Tuples - ordered with repetitions
from itertools import product
for c in product("abc", repeat=2):
  print("".join(c))

print("-------------------------------------")

#Permutations - ordered without repetitions
from itertools import permutations
for c in permutations("abc", 2):
  print("".join(c))

print("-------------------------------------")
#Combinations - unordered without repetitions

from itertools import combinations
for c in combinations("abc", 2):
  print("".join(c))

print("-------------------------------------")
#Combinations with repetitions - unordered with repetitions
from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBLE", 7):
  print("".join(c))

#or
k = 15
n = 4
print(scipy.special.binom(k+(n-1), n-1))

print("-------------------------------------")
print("-------------------------------------")

#Suppose there are 4 people and 9 different assignments. Each person should receive one assignment.
# Assignments for different people should be different. How many ways are there to do it?
#Total count of Possibilities
print(math.factorial(9)/ (math.factorial(9 - 4)))

#There are 4 people and 9 different assignments. We need to distribute all assignments among people. No assignment should be assigned to two people.
#Every person can be given arbitrary number of assignments from 0 to 9. How many ways are there to do it?
print(pow(4,9))

#There are 15 identical candies. How many ways are there to distribute them among 7 kids? - combinations with repetitions
k = 15
n = 7
print(scipy.special.binom(k+(n-1), n-1))

#There are 15 identical candies. How many ways are there to distribute them among 7 kids in such a way that each kid receives at least 1 candy?

# if received one candy each = 15 - 7 = 8candies left should be still distributed to 7 kids - combinations with repetitions
k = 8
n = 7
print(scipy.special.binom(k+(n-1), n-1))

#How many non-negative integer numbers are there below 10000 such that their sum of digits is equal to 9? - combinations with repetitions
k = 9 # total 1 - 9 possible numbers
n = 4 # below 10000 means just 4 positions in a number _ _ _ _
print(scipy.special.binom(k+(n-1), n-1))

# How many non-negative integer numbers are there below 10000 such that their sum of digits is equal to 10?
# We can start similarly to the previous problem. There are four digits in the number and we split the weight 10 among them.
# We can start with all digits being equal to 0 and then add 1 to one of them ten times in a row. So, each time we have to pick one of four digits.
# These choices are unordered and the repetitions are allowed. So we are dealing with combinations of size 10 out of 4 options with repetitions and we have the formula for that.
# This gives 286. But note that we have also counted cases where we place weight 10 into one digit and these cases do not correspond to 4-digit numbers.
# There are four such cases and subtracting them from our intermediate result we obtain the answer to the problem.
k = 10
n = 4
temp = scipy.special.binom(k+(n-1), n-1)
print(temp - 4) # here in each of the 4 positions. number 10 is not allowed anywhere

#How many four-digit numbers are there such that their digits are non-increasing, that is each next digit is not greater than the previous one?
# Three-digit numbers are also four-digit, they just start with 0.
#To fix such a number it is sufficient and enough to pick unordered subset of four numbers from 0 to 9.
# Then they can be ordered into a non-increasing order in a unique way. Since there might be equal digits in our number, repetitions are allowed.
# Thus we are dealing with combinations of size 4 out of 10 options with repetitions.
k = 4
n = 10
print(scipy.special.binom(k+(n-1), n-1))

#There are 12 students in the class. How many ways are there to split them into working groups of size 2 to work on the same assignment?
# we have to divide the extra count we done in the end of solution. we counted each splitting 6! times for each permutation of 6 groups
temp = scipy.special.binom(12, 2) * scipy.special.binom(10, 2) * scipy.special.binom(8, 2) * scipy.special.binom(6, 2) * scipy.special.binom(4, 2)  * scipy.special.binom(2, 2)
print(temp / math.factorial(6))

#Question 1
#We have a dataset of size 8 and we want to separate a subset of size 3 from it. How many ways do we have to do it?
k = 8
n = 3
print(scipy.special.binom(k, n))

#We have two disjoint datasets, of size 8 and 5 respectively.
#We would like to move three objects from the first dataset to the second and simultaneously move two objects from the second dataset to the first one. How many ways do we have to do it?
print(scipy.special.binom(8, 3) * scipy.special.binom(5, 2))

#In a 6 number lottery one is trying to guess an unordered subset of 6 numbers among 44 numbers without repetitions.
# For this one picks 6 numbers out of 44 himself. How many ways are there to do this? You can use wolfram alpha to compute the exact number.
k = 44
n = 6
print(scipy.special.binom(k, n))

#In a 6 number lottery one is trying to guess an unordered subset of 6 numbers among 44 numbers without repetitions.
# After the lottery the organisers decided to count how many possible ways are there to guess correctly exactly four numbers.
#What is the answer to this question? You can use wolfram alpha to compute the exact number.

#Answer: Something is wrong. Note that the lottery has already happened, so the set of winning numbers is fixed.
# So to guess exactly four winning numbers one has to pick four numbers among 6 winning numbers and pick two other numbers among remaining 44-6=38 numbers.
# Both of these are combinations and we know how to compute them. Then by the product rule we have to multiply the results to obtain the resulting number of possibilities.
print(scipy.special.binom(6, 4) * scipy.special.binom(38, 2))

print(math.factorial(5)/ (math.factorial(5 - 2)))

