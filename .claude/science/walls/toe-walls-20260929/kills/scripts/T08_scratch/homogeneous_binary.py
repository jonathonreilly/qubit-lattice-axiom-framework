"""Kill check 3 (premise the attack omits): the axioms give ONE fixed nearest-neighbour rule, the same at every site and bond,
on ONE site domain.  The ladder uses role-dependent bond tables and 4-state wing sites.  Test the homogeneous analogue:
every site binary, every bond (settings included) the same symmetric positive table W = [[w0,w1],[w1,w2]].
Ladder K=1 (plaquette) and K=2.  Maximise CHSH over W (and over the labelling of the settings) under
(i) no locality constraint, (ii) PI (a indep of t, b indep of s), (iii) ML (also rails indep of s,t)."""
import numpy as np
from itertools import product
from scipy.optimize import minimize
def law(W, K, s, t):
    # sites: s | A | rail1_1..rail1_K , rail2_1..rail2_K | B | t ; cycle A-r1_1-..-r1_K-B-r2_K-..-r2_1-A
    L = {}
    for A in (0,1):
        for R in product((0,1),repeat=2*K):
            r1,r2 = R[:K],R[K:]
            for B in (0,1):
                w = W[s][A]*W[B][t]
                chain1 = (A,)+r1+(B,); chain2 = (A,)+r2+(B,)
                for c in (chain1,chain2):
                    for i in range(len(c)-1): w *= W[c[i]][c[i+1]]
                L[(A,R,B)] = w
    Z = sum(L.values()); return {k:v/Z for k,v in L.items()}, Z
def stats(x, K):
    W = np.exp(np.array([[x[0],x[1]],[x[1],x[2]]]))
    E = {}; marg = {}
    for s in (0,1):
        for t in (0,1):
            l,Z = law(W,K,s,t)
            E[s,t] = sum(p*(1-2*k[0])*(1-2*k[2]) for k,p in l.items())
            marg[s,t] = ( sum(p for k,p in l.items() if k[0]==0), sum(p for k,p in l.items() if k[2]==0),
                          [sum(p for k,p in l.items() if k[1][i]==0) for i in range(2*K)] )
    S = max(abs(E[0,0]+E[0,1]+E[1,0]-E[1,1]), abs(-E[0,0]+E[0,1]+E[1,0]+E[1,1]),
            abs(E[0,0]-E[0,1]+E[1,0]+E[1,1]), abs(E[0,0]+E[0,1]-E[1,0]+E[1,1]))
    # fixed sign pattern for optimisation
    S0 = E[0,0]+E[0,1]+E[1,0]-E[1,1]
    pi = [marg[s,0][0]-marg[s,1][0] for s in (0,1)] + [marg[0,t][1]-marg[1,t][1] for t in (0,1)]
    ml = [ marg[s,t][2][i]-marg[0,0][2][i] for s in (0,1) for t in (0,1) for i in range(2*K)]
    return S, S0, np.array(pi), np.array(ml)
rng = np.random.default_rng(0)
for K in (1,2):
    for mode in ("none","PI","ML"):
        best = 0
        for trial in range(150):
            x0 = rng.normal(0,2,size=3)
            def f(x): 
                S,S0,pi,ml = stats(x,K); return -S0
            cons = []
            if mode in ("PI","ML"): cons.append({"type":"eq","fun":lambda x: stats(x,K)[2]})
            if mode=="ML": cons.append({"type":"eq","fun":lambda x: stats(x,K)[3]})
            out = minimize(f,x0,method="SLSQP",constraints=cons,bounds=[(-8,8)]*3,options={"maxiter":200,"ftol":1e-12})
            S,S0,pi,ml = stats(out.x,K)
            ok = (mode=="none") or (np.abs(pi).max()<1e-7 and (mode=="PI" or np.abs(ml).max()<1e-7))
            if ok: best = max(best, S)
        print(f"K={K} homogeneous binary symmetric rule, constraint={mode}: best |CHSH| = {best:.6f}")
