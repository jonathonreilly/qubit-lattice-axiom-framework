"""Test F2: what a nearest-neighbour formation law can and cannot make (chain x1 - x2 - x3, formed in the order 1,2,3).
Sequential local formation gives P(x1) P(x2|x1) P(x3|x2): a first-order Markov chain (Gibbs note T1/T2).
(a) even-parity law on 3 bits is not in that class: distance to the class = I(x1;x3|x2) = ln 2.
(b) brute-force minimisation of D(P||mu) over all Markov chains mu confirms it.
(c) a product law and a pure GHZ-type law are in the class (distance 0)."""
import numpy as np
from scipy.optimize import minimize
import itertools
def cmi(P):
    # I(x1;x3|x2)
    s=0.0
    for a,b,c in itertools.product(range(2),repeat=3):
        if P[a,b,c]>0:
            p_b=P[:,b,:].sum(); p_ab=P[a,b,:].sum(); p_bc=P[:,b,c].sum()
            s+=P[a,b,c]*np.log(P[a,b,c]*p_b/(p_ab*p_bc))
    return s
def markov(theta):
    # theta: p1 (1), t12 (2), t23 (2) via sigmoid
    s=lambda z:1/(1+np.exp(-z))
    p1=np.array([s(theta[0]),1-s(theta[0])])
    A=np.array([[s(theta[1]),1-s(theta[1])],[s(theta[2]),1-s(theta[2])]])
    B=np.array([[s(theta[3]),1-s(theta[3])],[s(theta[4]),1-s(theta[4])]])
    return np.einsum('a,ab,bc->abc',p1,A,B)
def dist(P):
    best=1e9
    rng=np.random.default_rng(0)
    for _ in range(40):
        th=rng.normal(size=5)*2
        f=lambda th:(lambda mu:sum(P[i]*np.log(P[i]/max(mu[i],1e-300)) for i in np.ndindex(*P.shape) if P[i]>0))(markov(th))
        r=minimize(f,th,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-13,maxiter=4000))
        best=min(best,r.fun)
    return best
even=np.zeros((2,2,2))
for a,b,c in itertools.product(range(2),repeat=3):
    if (a+b+c)%2==0: even[a,b,c]=0.25
ghz=np.zeros((2,2,2)); ghz[0,0,0]=ghz[1,1,1]=0.5
prod=np.full((2,2,2),1/8)
for nm,P in [('even parity',even),('GHZ-type',ghz),('product',prod)]:
    print(f"{nm:12s} I(x1;x3|x2) = {cmi(P):.6f}   min_Markov D(P||mu) = {dist(P):.6f}   (ln2 = {np.log(2):.6f})")
