"""A44 gaps: mean-field gap at half filling vs theta (t=cos th, lam=sin th), APBC, L=4 and 6;
distinct occupied sets (the projected state only changes where the occupied set changes)."""
import sys, signal, numpy as np
signal.alarm(120)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a44lib import *
for L in (4, 6):
    cl = cube(L); prev = None
    print(f"L={L} APBC:")
    for thd in np.arange(0, 90.01, 2.5):
        th = np.radians(thd)
        Phi, gap, lev = mf_orbitals(cl, np.cos(th), np.sin(th))
        P = Phi @ Phi.conj().T          # projector on the occupied set
        ch = "" if prev is None else f" |dP| {np.abs(P - prev).max():.2f}"
        prev = P
        print(f"  th={thd:5.1f}: gap {gap:.4f}{ch}")
    Phi, gap, lev = mf_orbitals(cl, 1.0, 0.0, kind="pi")
    print(f"  KS pi-flux: gap {gap:.4f}")
