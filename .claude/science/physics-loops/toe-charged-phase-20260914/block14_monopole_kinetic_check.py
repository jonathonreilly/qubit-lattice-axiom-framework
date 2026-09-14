"""Finite physical-flux challenges for an explicitly deformed Z3 generator."""
import itertools
import numpy as np
from scipy.linalg import expm, eigvalsh

F=np.array([[1,0,-1,0,-1,1,0],[0,1,0,-1,0,-1,1]])
bs=np.array(list(itertools.product(range(3),repeat=2)))
index={tuple(b):i for i,b in enumerate(bs)}
def principal(a):return (a+1)%3-1
pb=principal(bs)
etas=np.array(list(itertools.product(range(3),repeat=7)))
flux=(F@etas.T).T%3
lift=(F@principal(etas).T).T
number=np.count_nonzero(etas,axis=1)


def kernel(step,t,mu):
    K=np.zeros((9,9));weight=(step*t)**number
    for i,b in enumerate(bs):
        for j,bp in enumerate(bs):
            keep=np.all(flux==(bp-b)%3,axis=1)
            monop=(pb[j]-pb[i]-lift[keep])/3
            assert np.max(abs(monop-np.rint(monop)))<1e-12
            K[j,i]=sum(weight[keep]*np.exp(-mu*np.sum(monop**2,axis=1)))
    return K


def generator(t,mu,magnetic):
    A=np.zeros((9,9))
    for i,b in enumerate(bs):
        for link in range(7):
            for sig in (-1,1):
                bp=(b+sig*F[:,link])%3;j=index[tuple(bp)]
                m=(pb[j]-pb[i]-sig*F[:,link])/3
                assert np.max(abs(m-np.rint(m)))<1e-12
                A[j,i]+=t*np.exp(-mu*sum(m*m))
    assert np.max(abs(A-A.T))<1e-12
    V=magnetic*(2-np.cos(2*np.pi*bs/3).sum(axis=1))
    H=14*t*np.eye(9)-A+np.diag(V)
    assert eigvalsh(H)[0]>=-1e-12
    return H,V


for mu in (0.,.4,1.,3.):
    t=.7;H,V=generator(t,mu,.6)
    errors=[]
    for step in (.02,.01,.005,.0025):
        M=np.diag(np.exp(-step*V/2));K=kernel(step,t,mu)
        assert np.max(abs(K-K.T))<1e-12
        assert eigvalsh(K)[0]>0
        T=np.exp(-14*t*step)*M@K@M
        error=np.linalg.norm(T-expm(-step*H),2);errors.append(error)
        # Finite-time convergence, separately using repeated physical transfer.
        steps=round(.2/step)
        finite=np.linalg.matrix_power(T,steps)
        assert np.linalg.norm(finite-expm(-steps*step*H),2)<80*step
    ratios=np.array(errors[:-1])/errors[1:]
    assert ratios.min()>3.5 and ratios.max()<4.5
    print('mu_t',mu,'one_step_errors',errors,'ratios',ratios.tolist())
# Mu=0 must exactly recover the standard physical-strip generator.
H,_=generator(.7,0.,.6)
I=np.eye(9)
def shift(v):
    S=np.zeros((9,9))
    for i,b in enumerate(bs):S[index[tuple((b+v)%3)],i]=1
    return S
S1=shift(np.array([1,0]));S2=shift(np.array([0,1]));S12=shift(np.array([1,-1]))
expected=.7*(3*(2*I-S1-S1.T)+3*(2*I-S2-S2.T)+(2*I-S12-S12.T))
expected+=np.diag(.6*(2-np.cos(2*np.pi*bs/3).sum(axis=1)))
assert np.linalg.norm(H-expected)<1e-12
print('Direct rates, reversed moves, complete 2187-difference kernel, quadratic one-step errors, finite-time comparison, and undeformed limit checked. No phase result.')

# Separate three-dimensional cell-complex check: full periodic 5^3 cubic carrier.
L=5
sites=list(itertools.product(range(L),repeat=3));si={p:i for i,p in enumerate(sites)}
edges=[(p,d) for p in sites for d in range(3)];ei={e:i for i,e in enumerate(edges)}
faces=[(p,i,j) for p in sites for i,j in ((0,1),(0,2),(1,2))];fi={f:i for i,f in enumerate(faces)}
def advance(p,d):
    q=list(p);q[d]=(q[d]+1)%L;return tuple(q)
G=np.zeros((len(edges),len(sites)),int);C=np.zeros((len(faces),len(edges)),int)
for row,(p,d) in enumerate(edges):G[row,si[advance(p,d)]]=1;G[row,si[p]]=-1
for row,(p,i,j) in enumerate(faces):
    for edge,sign in (((p,i),1),((advance(p,i),j),1),((advance(p,j),i),-1),((p,j),-1)):C[row,ei[edge]]+=sign
D=np.zeros((len(sites),len(faces)),int)
for row,p in enumerate(sites):
    for face,sign in (((advance(p,0),1,2),1),((p,1,2),-1),((advance(p,1),0,2),-1),((p,0,2),1),((advance(p,2),0,1),1),((p,0,1),-1)):D[row,fi[face]]+=sign
assert np.max(abs(C@G))==0 and np.max(abs(D@C))==0
v=np.zeros(len(edges),int)
for y,z in itertools.product((1,2),repeat=2):v[ei[((2,y,z),0)]]=1
boundary=np.flatnonzero(C@v);assert len(boundary)==8
near=np.any(C[boundary]!=0,axis=0)
rng=np.random.default_rng(774)
for _ in range(6):
    a=rng.integers(3,size=len(edges));chi=rng.integers(3,size=len(sites));b=principal(C@a);bv=principal(C@(a+v))
    assert np.max(abs(principal(C@(a+G@chi))-b))==0
    assert np.max(abs((D@b)%3))==0
    for link in range(len(edges)):
        for sig in (-1,1):
            bp=principal(b+sig*C[:,link]);m=(bp-b-sig*C[:,link])/3
            reverse=(b-bp+sig*C[:,link])/3
            assert np.max(abs(m-np.rint(m)))==0 and np.max(abs(m+reverse))==0
            assert np.count_nonzero(m)<=4 and np.max(abs(m))<=1
            if not near[link]:
                bvp=principal(bv+sig*C[:,link]);mv=(bvp-bv-sig*C[:,link])/3
                assert np.max(abs(m-mv))==0
print('Three-dimensional 5^3 carrier: both incidence identities, Gauss invariance, integer cube charge, reversible bounded rates, and remote membrane support checked.')
