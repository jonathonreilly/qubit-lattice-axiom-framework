"""A51 vbs_check: the columnar VBS (dimers (x, x+e1), x1 even) and the closed-form rule from the dimer condition
J11 + J22 = J12 + J21 (EXACT algebra: H_inter^{AB}|ss> = (Delta_AB/4) D_A.D_B |ss>, Delta = sum eta_i eta_j J_ij):
   J = j for (001),(011),(111);  j/2 for (002),(012),(112);  j/4 for (022),(122);  j/8 for (222);  0 beyond.
VMC sees exactly 1/3 of each dimer-pair excitation (the T0 T0 part is in the support, T+T- is not), so for two-spin rules
VMC variance = (1/3) true variance and lam = 0 is exact.  Usage: vbs_check.py L"""
import sys, signal, numpy as np
signal.alarm(100)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from anal51 import *
L = int(sys.argv[1]); ks, m, F4, G, Gm = metrics(L); nc = len(ks); N = L ** 3
rule = {(0, 0, 1): 1, (0, 1, 1): 1, (1, 1, 1): 1, (0, 0, 2): .5, (0, 1, 2): .5, (1, 1, 2): .5, (0, 2, 2): .25, (1, 2, 2): .25, (2, 2, 2): .125}
v = np.zeros(nc + 10)
for k, x in rule.items(): v[ks.index(k)] = x
for sp in ("vbs", "lp:0"):
    S, nf = load(L, sp)
    if S is None: continue
    C = covm(S, N); e = (S @ v).real / N
    print(f"L={L} {sp}: closed-form VBS rule: lam(VMC, mod metric) = {(v @ C @ v) / (v @ Gm @ v):.3e}; <H>/site {e.mean():+.5f}; per-sample spread {e.std():.2e}")
S, nf = load(L, "vbs"); sub = subsets(ks, nc, 12)["B"]; o = lam_jk(S, N, sub, Gm)
w = np.zeros(nc + 10); w[sub] = o["vec"]; w /= w[0]
print("bilinear |d|^2<=12 VBS minimizer (J_NN=1): " + " ".join(f"{ks[c]}:{w[c]:+.3f}" for c in sub))
