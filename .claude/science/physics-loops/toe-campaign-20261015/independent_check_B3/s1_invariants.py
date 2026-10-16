# Invariant / equivariant spaces on the 27-point cell, by Reynolds averaging over O
import numpy as np, itertools
R=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3));
        for i in range(3): M[i,p[i]]=s[i]
        if round(np.linalg.det(M))==1: R.append(M)
assert len(R)==24
N=list(itertools.product([-1,0,1],repeat=3)); idx={n:i for i,n in enumerate(N)}
# scalar functions: coefficient vector c_n (complex), f(Rk)=f(k) <=> c_{Rn}=c_n
P=np.zeros((27,27))
for M in R:
    for n in N:
        P[idx[tuple((M@np.array(n)).astype(int))],idx[n]]+=1/24
print("dim invariant scalars (complex) =",round(np.trace(P)))
# vector functions: g(k)=sum G_n e^{ikn}, G_n in C^3; equivariance g(Rk)=R g(k) <=> G_{Rn}=R G_n
P3=np.zeros((81,81))
for M in R:
    for n in N:
        m=idx[tuple((M@np.array(n)).astype(int))]
        P3[3*m:3*m+3,3*idx[n]:3*idx[n]+3]+=M/24
print("dim equivariant vectors (complex) =",round(np.trace(P3)))
# list orbit sums of invariant scalars
orbits=set()
for n in N:
    orbits.add(tuple(sorted(tuple((M@np.array(n)).astype(int)) for M in R)))
print("orbits:",len(orbits))
# show equivariant basis: real/imag structure
w,v=np.linalg.eigh((P3+P3.T)/2); B=v[:,w>0.5]
for j in range(B.shape[1]):
    G=B[:,j].reshape(27,3); nz=[(N[i],np.round(G[i],3)) for i in range(27) if np.abs(G[i]).max()>1e-9]
    print(j,nz[:4],'...')
