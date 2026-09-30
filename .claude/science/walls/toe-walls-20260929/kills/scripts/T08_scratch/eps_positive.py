"""Kill check 2: the ladder uses hard-zero (0/1) weights.  A local specification with a *distribution at every site for every
neighbour condition* needs positive weights.  Replace 0 by eps in every bond; compute exact CHSH, Z(s,t), and the largest
single-site-marginal dependence on (s,t)."""
import numpy as np
from itertools import product
def run(K, eps):
    res = {}
    for s in (0,1):
        for t in (0,1):
            law = {}
            for A in product((0,1),repeat=2):
                for R in product((0,1),repeat=2*K):
                    g1,g2 = R[:K],R[K:]
                    for B in product((0,1),repeat=2):
                        w = 1.0
                        def bond(ok): return 1.0 if ok else eps
                        w *= bond(A[0]==s); w *= bond(B[0]==t)
                        w *= bond(g1[0]==A[1]); w *= bond(g2[0]==(A[1]^1^A[0]))
                        for k in range(K-1):
                            w *= bond(g1[k+1]==g1[k]); w *= bond(g2[k+1]==g2[k])
                        w *= bond(B[0]==1 or B[1]==g1[-1]); w *= bond(B[0]==0 or B[1]==(g2[-1]^1))
                        law[(A,R,B)] = w
            Z = sum(law.values()); res[(s,t)] = ({k:v/Z for k,v in law.items()}, Z)
    E = {}
    for st,(law,Z) in res.items():
        E[st] = sum(p*(1-2*k[0][1])*(1-2*k[2][1]) for k,p in law.items())
    S = E[0,0]+E[0,1]+E[1,0]-E[1,1]
    def marg(f):
        return {st:{v: sum(p for k,p in law.items() if f(k)==v) for v in {f(k) for k in law}} for st,(law,Z) in res.items()}
    maxdev = 0.0
    sites = {"a": lambda k:k[0][1], "b": lambda k:k[2][1]}
    for i in range(2*K): sites[f"r{i}"] = (lambda i: lambda k:k[1][i])(i)
    for name,f in sites.items():
        m = marg(f)
        for v in (0,1):
            vals = {st:m[st].get(v,0) for st in m}
            if name=="a":   # outcome a: must not depend on t (PI) nor s (no-signalling of A's outcome from own setting is not required)
                dev = max(abs(vals[(s,0)]-vals[(s,1)]) for s in (0,1))
            elif name=="b":
                dev = max(abs(vals[(0,t)]-vals[(1,t)]) for t in (0,1))
            else:
                dev = max(vals.values())-min(vals.values())
            maxdev = max(maxdev,dev)
    return S, maxdev, [round(res[st][1],6) for st in sorted(res)]
for K in (1,2):
    print("K=%d"%K)
    for eps in (1.0, 0.3, 0.1, 0.01, 0.001, 0.0):
        S,dev,Z = run(K,eps)
        print(f"  eps={eps:<6} CHSH={S:.6f}  max single-site marginal dependence (outcome a on t, b on s, rails on s,t)={dev:.2e}  Z(s,t)={Z}")
