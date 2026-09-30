"""Test G (post-hoc, exploratory; motivated by the plateau D8 ~ 0.049 seen in Test B for three different starts):
is the residual the KL of the branch weights (A side, B side) at t = 8?  Branch mass is conserved once the branches
have disjoint support.  Setting (theta_A, theta_B) = (0, pi/4)."""
import os, numpy as np
import testB_protocol as B
from common import kl
for m in B.models.values(): m.cap = 1e5
s = B.SETS[0]; m = B.models[s]
side = B.side > 0
def branches(r):
    w = np.array([[r[np.ix_(sa, sb)].sum() for sb in (side, ~side)] for sa in (side, ~side)])
    return w.ravel()
def klv(a, b):
    mk = a > 1e-300
    return float((a[mk] * np.log(a[mk] / b[mk])).sum())
te = np.arange(0, 9.0)
Peq = m.P(8.0); wP = branches(Peq)
print('Born branch weights (++,+-,-+,--) at t=8:', np.round(wP, 4))
for nm in ['1 width x2 (prob width 2.1)', '2 width x0.4', '5 point mass at (12,12)', '3 shifted by 2', '6 correlated 1+0.5 sA sB']:
    r8 = m.evolve(B.starts[nm], te)[-1]
    wr = branches(r8)
    print(f"{nm:30s} D8={kl(r8, Peq):.4f}  KL(branch weights)={klv(wr, wP):.4f}   record branch weights={np.round(wr, 4)}")
    # also branch weights at t=0 from the initial ensemble for reference
