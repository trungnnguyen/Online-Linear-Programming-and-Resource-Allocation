import numpy as np
from cvxpy import *

############################################################################################

# Initial Offline Problem, where we have access to 'n' bidders, while 'K-n' bidders are unknown.

# Create two scalar optimization variables.
m = 10
K = 10000
n = 1000

A = np.random.randint(0, 2, (m, K))

X = Variable(K)
z = Variable()

q = np.random.randint(10, 21, (K,1))
p = np.random.uniform(0, 1, (m,1))
pi = p.T.dot(A) + np.sqrt(0.2) * np.random.randn(1, K)

A = np.random.randint(0, 2, (m, K))

constraints = [];

for i in range(A.shape[0]):
    constraints.append( A[i,:]*X - z <= 0 );

    
for j in range(A.shape[1]):
    constraints.append(X[j] >= 0);
    constraints.append(X[j] <= q[j]);

constraints.append(X[n:] == 0);

# Form objective.
obj = Maximize( pi*X - z );

# Form and solve problem.
prob = Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print "status:", prob.status
print "optimal value", prob.value
print "optimal var:"
print X.value

############################################################################################

# Dual of the Linear Problem to Solve Shadow Prices

P = Variable(m);
s = Variable(K);

obj2 = Minimize(q.T*s);

#for i in range(A.shape[1]):
#    constraints2.append( A[i,:].T*P + s[i] >= pi[i] );
# constraints2.append(P[i] >= 0);
# constraints2.append(s[i] >= 0);

constraints2 = [A.T*P + s >= pi.T];
constraints2.append(np.ones(m)*P == 1);
constraints2.append(P >= 0)
constraints2.append(s >= 0);

# Form and solve problem.
prob2 = Problem(obj2, constraints2)
prob2.solve()  # Returns the optimal value.
print "Optimal Shadow Prices:"
print P.value

############################################################################################

# Perform the optimation on additional bidders

b = X.value;

constraints = [];

for i in range(A.shape[0]):
    constraints.append( A[i,:]*X - z <= 0 );

for j in range(A.shape[1]):
    constraints.append(X[j] >= 0);
    constraints.append(X[j] <= q[j]);

# Form objective.
obj = Maximize( pi*X - z );

# Form and solve problem.
prob = Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print "Optimal Order Fill:"
print X.value

