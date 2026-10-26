import numpy as np, itertools, time
from lib import *
L=4; n=16
n,bonds=torus_bonds((4,4))
# original one-body
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex)
def orig_h(dims, sig):
    n=int(np.prod(dims)); h=np.zeros((2*n,2*n),complex)
    d=len(dims)
    for c in itertools.product(*[range(L) for L in dims][::-1]):
        c=c[::-1]
        i=sum(c[k]*int(np.prod(dims[:k])) for k in range(d))
        for j in range(d):
            c2=list(c); c2[j]=(c2[j]+1)%dims[j]
            i2=sum(c2[k]*int(np.prod(dims[:k])) for k in range(d))
            blk=-0.5j*sig[j]
            h[2*i:2*i+2,2*i2:2*i2+2]+=blk
            h[2*i2:2*i2+2,2*i:2*i+2]+=blk.conj().T
    return h
h=orig_h((4,4),[sx,sy])
# gauge
def g(c):
    M=np.eye(2,dtype=complex)
    for k,s in enumerate([sx,sy,sz][:len(c)]):
        M=M@np.linalg.matrix_power(s,c[k])
    return M
V=np.zeros((32,32),complex)
for y in range(4):
  for x in range(4):
    i=x+4*y
    V[2*i:2*i+2,2*i:2*i+2]=g((x,y))*(1j)**(x+y)
hh=V.conj().T@h@V
# expected real hop
hexp=np.zeros((32,32))
for (a,b,j,t,c) in bonds:
    for s in range(2):
        hexp[2*a+s,2*b+s]+=t; hexp[2*b+s,2*a+s]+=t
print(np.abs(hh-hexp).max())
