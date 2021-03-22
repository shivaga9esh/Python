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