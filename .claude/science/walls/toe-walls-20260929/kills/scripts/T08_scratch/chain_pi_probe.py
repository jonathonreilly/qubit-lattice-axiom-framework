"""Kill check on pre-registered P2 (machinery sanity): can the one-site-cut chain (G1) exceed 2 under PI (outcome
marginals no-signalling)?  Attacker's reduced run reports 2.0000 => P2 'FAIL' reading.  Use a stronger optimiser
(many random starts of the *parametrised chain* F=w0*w1, G=w2*w3, plus SLSQP on full F,G from the landed chain)."""
import numpy as np, itertools
from scipy.optimize import minimize
sgn = np.array([1.,-1.])
def Sfun(F,G):
    N = np.einsum("sal,tbl->stabl", F, G); Z = N.sum(axis=(2,3,4)); P = N/Z[:,:,None,None,None]
    E = np.einsum("stab,a,b->st", P.sum(axis=4), sgn, sgn)
    return E[0,0]+E[0,1]+E[1,0]-E[1,1], P, Z
def chain_FG(x, nc=2):
    # pairwise chain s-A-C-B-t with alphabet 2 for A,B and nc for C ; x holds 4 weight tables (exp-param)
    w = np.exp(x)
    i=0
    W0 = w[i:i+4].reshape(2,2); i+=4      # s,a
    W1 = w[i:i+2*nc].reshape(2,nc); i+=2*nc  # a,c
    W2 = w[i:i+2*nc].reshape(nc,2); i+=2*nc  # c,b
    W3 = w[i:i+4].reshape(2,2)            # b,t
    F = np.einsum("sa,ac->sac", W0, W1); G = np.einsum("cb,bt->tbc", W2, W3)
    return F,G
def pi_res(P):
    Pa = P.sum(axis=(3,4))[...,0]; Pb = P.sum(axis=(2,4))[...,0]
    return np.array([Pa[0,0]-Pa[0,1], Pa[1,0]-Pa[1,1], Pb[0,0]-Pb[1,0], Pb[0,1]-Pb[1,1]])
best=0; rng=np.random.default_rng(1)
nc=2
n = 4+2*nc+2*nc+4
for trial in range(400):
    x0 = rng.normal(0,2.5,size=n)
    def obj(x): F,G=chain_FG(x,nc); return -Sfun(F,G)[0]
    def cons(x): F,G=chain_FG(x,nc); S,P,Z=Sfun(F,G); return pi_res(P)
    out = minimize(obj,x0,method="SLSQP",constraints=[{"type":"eq","fun":cons}],bounds=[(-12,12)]*n,options={"maxiter":400,"ftol":1e-13})
    F,G=chain_FG(out.x,nc); S,P,Z=Sfun(F,G); r=np.abs(pi_res(P)).max()
    if r<1e-7 and S>best: best=S
print("pairwise chain, alphabet (2,2,2), PI-feasible best S over 400 starts:", round(best,6))
# unconstrained control: does this optimiser find the landed 2.92?
b2=0
for trial in range(400):
    x0 = rng.normal(0,2.5,size=n)
    out = minimize(lambda x: -Sfun(*chain_FG(x,nc))[0],x0,method="L-BFGS-B",bounds=[(-12,12)]*n)
    b2=max(b2,-out.fun)
print("unconstrained control (landed value 2.9208 is reachable):", round(b2,6))
