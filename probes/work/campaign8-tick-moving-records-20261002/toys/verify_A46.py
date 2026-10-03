"""Coordinator check of A46's ring identity on a 4-spin face 1-2-3-4:
P + P^-1 = 1/4[(12)(34) + (14)(23) - (13)(24)] + 1/4 sum_{i<j} (ij) + 1/4, with (ij) = sigma_i . sigma_j; spectrum -2 (x4), 0 (x6), +2 (x6)."""
import numpy as np, itertools
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.diag([1,-1]).astype(complex)]
def op(i,a):
    m=[np.eye(2)]*4; m=list(m); m[i]=s[a]; out=m[0]
    for k in range(1,4): out=np.kron(out,m[k])
    return out
def dot(i,j): return sum(op(i,a)@op(j,a) for a in range(3))
# cyclic permutation P: spin at site k moves to site k+1 (mod 4)
P=np.zeros((16,16))
for b in range(16):
    bits=[(b>>(3-k))&1 for k in range(4)]
    nb=[bits[(k-1)%4] for k in range(4)]
    P[int(''.join(map(str,nb)),2),b]=1
lhs=P+P.T
d=lambda i,j: dot(i-1,j-1)
rhs=0.25*(d(1,2)@d(3,4)+d(1,4)@d(2,3)-d(1,3)@d(2,4))+0.25*sum(d(i,j) for i,j in itertools.combinations([1,2,3,4],2))+0.25*np.eye(16)
print("identity holds:", np.allclose(lhs,rhs))
ev=np.round(np.linalg.eigvalsh(lhs),8); vals,counts=np.unique(ev,return_counts=True); print("spectrum:", dict(zip(vals,counts)))
