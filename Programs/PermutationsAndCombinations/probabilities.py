#consider non-symmetric dice for which probability to get kk points is proportional to k,
# k=1,2,3,4,5,6k=1,2,3,4,5,6. (I.e. probability to get 2 is twice as large as probability to get 1.)
# What is the probability to get 1 point on this dice? Enter proper fraction

#Let x be the probability to get one point.
# Then the probability to get kkpoints is kx.
# Sum of all probabilities should be equal to 1,
# therefore, we have an equation: x + 2x + 3x + 4x + 5x + 6x = 1x+2x+3x+4x+5x+6x=1
# which is equivalent to 21x=121x=1.
# Therefore,
x = 1/21

#consider non-symmetric dice for which probability to get k points is proportional to k, k=1,2,3,4,5,6k=1,2,3,4,5,6.
# (I.e. probability to get 2 is twice as large as probability to get 1.)
# What is the probability to get less then 3 points? Enter proper fraction.

#According to previous question, probability to get 1 point is 1/21 and 2 points is 2/21.
# The probability to get less then 3 points is a sum of probabilities to get 1 point and to get 2 points.
print(1/21 + 2/21)