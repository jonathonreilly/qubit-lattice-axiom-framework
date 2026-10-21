"""Exact positive-parity four-physical-site rung coordinates; no added degrees of freedom."""
import numpy as np
I=np.eye(2);X=np.array([[0.,1],[1,0]]);Z=np.diag([1.,-1])
def kron(*args):
 a=np.array([[1.]])
 for b in args:a=np.kron(a,b)
 return a
xs=[kron(*[X if i==a else I for i in range(3)]) for a in range(3)]
zs=[kron(*[Z if i==a else I for i in range(3)]) for a in range(3)]
h=-xs[0]@xs[2]-xs[1]+xs[0]@xs[1]@zs[0]@zs[1]+xs[2]@zs[0]@zs[1]
Ds=zs+[zs[0]@zs[1]@zs[2]]
