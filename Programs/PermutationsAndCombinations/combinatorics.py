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
