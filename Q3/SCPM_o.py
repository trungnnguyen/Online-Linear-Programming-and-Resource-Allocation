import numpy as np
from cvxpy import *
from random import random, randrange,uniform,normalvariate
from math import sqrt


k=10
m=1
n=4
x = Variable(k,1)
s = Variable(m,1)
#z = Variable(1)

a = np.random.randint(0, 2, (k, m))
p = np.random.uniform(0, 1, (m,1))
q = np.random.randint(10, 21, (k,1))
pi = a.dot(p) + np.sqrt(0.2) * np.random.randn(k, 1)
w=1e-3
b=np.ones((10,1))*1000.0
obj1 = Maximize(pi.transpose()*x  + w*sum(log(s))/m)
obj2 = Maximize(pi.transpose()*x  + w*sum(1-exp(-s))/m)
#part 1
constraints = [x[n:] == 0,a.transpose()*x  - b + s == 0, x <= q, x >= 0, s >= 0]
# Form objective.

# Form and solve problem.
prob1 = Problem(obj1, constraints)
prob1.solve(solver=CVXOPT)  # Returns the optimal value.
print "status:", prob1.status
print "optimal value", prob1.value
print "optimal var", x.value


#part 2

c = x[0:n]
constraints = [x[0:n] - c == 0,a.transpose()*x  - b + s == 0, x <= q, x >= 0, s >= 0]
# Form and solve problem.
prob2 = Problem(obj1, constraints)
prob2.solve(solver=CVXOPT,abstol=1e-25)  # Returns the optimal value.

print "status:", prob2.status
print "optimal value", prob2.value
print "optimal var", x.value
