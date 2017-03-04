import numpy
from cvxpy import *

# Create two scalar optimization variables.
X = Variable(5);
z = Variable();

A = numpy.array([[1,0,1,1,0],[1,0,0,1,1],[1,0,1,1,0],[0,1,0,1,1],[0,0,1,0,0]]);

pi = numpy.array([0.75, 0.35, 0.4, 0.95, 0.75]);
#randomVector = numpy.random.rand(1, 5);
#scaledRandomVector = numpy.multiply(randomVector, 0.2);
#pi = numpy.add(numpy.array([0.75, 0.35, 0.4, 0.95, 0.75]), scaledRandomVector);

q = numpy.array([10, 5, 10, 10, 5]);

constraints = [];

for i in range(A.shape[1]):
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

############################################################################################

# Dual of the Linear Problem to Solve Shadow Prices

P = Variable(5);
s = Variable(5);

obj2 = Minimize(q.T*s);

#for i in range(A.shape[1]):
#    constraints2.append( A[i,:].T*P + s[i] >= pi[i] );
    # constraints2.append(P[i] >= 0);
    # constraints2.append(s[i] >= 0);

constraints2 = [A.T*P + s >= pi, numpy.ones(5)*P == 1, P >= 0, s >= 0];

# Form and solve problem.
prob2 = Problem(obj2, constraints2)
prob2.solve()  # Returns the optimal value.
print "Optimal Shadow Prices:"
print P.value
