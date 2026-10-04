"""A51 control51: positive controls in the long-range class basis (plain metric, all classes).
pol: soldered-uniform polarized product state = dual four-sublattice pattern; pairs parallel iff all components of d have
     equal parity -> those classes are exact null directions (EXACT), all others are not.
cs:  compass-staggered product state; pairs parallel iff |d|_1 even -> those classes null.
Also the parton's Casimir: plain-metric full-reach minimum = sum_c O_c with lam = 0 (exact singlet).  Usage: control51.py L"""
import sys, signal, numpy as np
signal.alarm(200)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from anal51 import *
L = int(sys.argv[1]); ks, m, F4, G, Gm = metrics(L); nc = len(ks); N = L ** 3; K = np.array(ks)
pred = {"pol": [c for c in range(nc) if len(set(K[c] % 2)) == 1], "cs": [c for c in range(nc) if K[c].sum() % 2 == 0]}
for sp in ("pol", "cs"):
    S, nf = load(L, sp)
    if S is None: continue
    C = covm(S[:, :nc], N); lam, V = releig(C, G[:nc, :nc]); npred = len(pred[sp])
    off = max(np.abs(C[np.ix_(pred[sp], range(nc))]).max(), 0)
    print(f"{sp} L={L} ({len(S)} samples): predicted null classes {npred}: {[tuple(K[c]) for c in pred[sp]]}")
    print(f"  lowest eigenvalues: {np.array2string(lam[:npred + 2], precision=2)}; max |C| on predicted-null rows {off:.1e}")
S, nf = load(L, "lp:0")
if S is not None:
    lam, V = releig(covm(S[:, :nc], N), G[:nc, :nc]); v = V[:, 0] / V[0, 0]
    print(f"parton L={L}: plain-metric full-reach B minimum lam = {lam[0]:.2e} (next {lam[1]:.3g}); vector spread max|v_c - 1| = {np.abs(v - 1).max():.1e} (Casimir = all ones)")
