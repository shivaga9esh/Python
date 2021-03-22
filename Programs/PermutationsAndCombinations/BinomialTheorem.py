

#####################################################################

#import math
#print(math.factorial(120)/ (math.factorial(120 - 75) * math.factorial(75)))
#print(math.factorial(120)/ (math.factorial(120 - 76) * math.factorial(76)))
#####################################################################

#import scipy.special
#scipy.special.binom(10, 5, exact=True)

#Find the coefficients of the expansion of (3a-b)^3 . That is, represent  (3a-b)^3 as x^3  + y a^2 b^1 + z  ..... Try to compute these coefficients using the binomial theorem
#Enter the values of x , y, z

import scipy.special
a = 1
b = 1

P_temp = scipy.special.binom(3, 0)
q_temp = pow(3*a, 3-0)
r_temp = pow(-b,0)

#or
#Use Binomial expander online - https://www.mathway.com/Algebra