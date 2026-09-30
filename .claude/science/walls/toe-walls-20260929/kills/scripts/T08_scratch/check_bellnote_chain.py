"""Kill check: does the attacker's reduced relaxation contain the landed Bell-note static chain (CHSH 2.9208), and does
its optimiser find it?  Also: does that landed chain satisfy PI / ML?"""
import numpy as np, itertools, sys
sys.path.insert(0, '../../attacks/T08_scratch')
from fractions import Fraction as Fr
eps = 0.01
bits = (0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0)
Wt = [[[(1.0 if bits[4*kk+2*i+j] else eps) for j in range(2)] for i in range(2)] for kk in range(4)]
# reduced form F[s,a,c] = W0[s][a] W1[a][c]; G[t,b,c] = W2[c][b] W3[b][t]
F = np.zeros((2,2,2)); G = np.zeros((2,2,2))
for s in range(2):
    for a in range(2):
        for c in range(2):
            F[s,a,c] = Wt[0][s][a]*Wt[1][a][c]
for t in range(2):
    for b in range(2):
        for c in range(2):
            G[t,b,c] = Wt[2][c][b]*Wt[3][b][t]
N = np.einsum("sal,tbl->stabl", F, G); Z = N.sum(axis=(2,3,4)); P = N/Z[:,:,None,None,None]
sgn = np.array([1.,-1.])
E = np.einsum("stab,a,b->st", P.sum(axis=4), sgn, sgn)
print("E =", E.round(4).tolist())
S = E[0,0]+E[0,1]+E[1,0]-E[1,1]
print("S (this sign pattern) =", S, "  all 4 patterns:", [abs(E[0,0]+E[0,1]+E[1,0]-E[1,1]), abs(-E[0,0]+E[0,1]+E[1,0]+E[1,1]), abs(E[0,0]-E[0,1]+E[1,0]+E[1,1]), abs(E[0,0]+E[0,1]-E[1,0]+E[1,1])])
Pa = P.sum(axis=(3,4))[...,0]; Pb = P.sum(axis=(2,4))[...,0]
print("P(a=+|s,t):", Pa.round(4).tolist()); print("P(b=+|s,t):", Pb.round(4).tolist())
print("Z(s,t):", Z.round(5).tolist())
Pl = P.sum(axis=(2,3)); print("P(c|s,t):", Pl.round(4).tolist())
