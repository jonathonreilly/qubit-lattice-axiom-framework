"""Native rung MPO and variational state checks; not a scalar-mode certificate."""
from pathlib import Path
import numpy as np,json,time,sys,pickle
import quimb as qu
import quimb.tensor as qtn
P=Path(__file__).resolve().parent
I=np.eye(2);X=np.array([[0.,1],[1,0]]);Z=np.diag([1.,-1])
def kron(*args):
 a=np.array([[1.]])
 for b in args:a=np.kron(a,b)
 return a
xs=[kron(*[X if i==a else I for i in range(3)]) for a in range(3)]
zs=[kron(*[Z if i==a else I for i in range(3)]) for a in range(3)]
h=-xs[0]@xs[2]-xs[1]+xs[0]@xs[1]@zs[0]@zs[1]+xs[2]@zs[0]@zs[1]
Ds=zs+[zs[0]@zs[1]@zs[2]]
def mpo(L):
 W=np.zeros((6,6,8,8));W[0,0]=np.eye(8);W[5,5]=np.eye(8);W[0,5]=h
 for a,d in enumerate(Ds):W[0,a+1]=-d;W[a+1,5]=d
 return qtn.MatrixProductOperator([W[0] if i==0 else W[:,5] if i==L-1 else W.copy() for i in range(L)],shape='lrud')
