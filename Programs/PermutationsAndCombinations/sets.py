A = {1, 3, 2, 0, 1, 3}
print(A)


A={1,3,4,7,10,11}
#B={1,7,11}
#B={1,3,4,7,10,11}
#B={1,3,4,8}
B={1,3,4,5,7,10,11}


print(B.issubset(A))

A={1,2,4,5,6}
B={1,2,3,5,7}

print(A.intersection(B))
print(A.union(B))

#A coin tossed 3 times. Let A be event First tossing yields head and
# B be event Exactly one tail occurred. How many outcomes belongs to event A∩B?
coin = {'H','T'}
count = 3

from itertools import product
for c in product("HT", repeat=3):
  print("".join(c))

#A pair of fair dice rolled. What is the probability of event Sum of points is greater than 10?
# Enter proper irreducible fraction
coin = {'1','2', '3', '4', '5', '6'}
count = 2

from itertools import product
for c in product("123456", repeat=2):
  print("".join(c))