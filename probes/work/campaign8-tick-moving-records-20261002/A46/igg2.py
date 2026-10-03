"""A46 igg2: gauge-group check for the covariant same-sublattice hops (Q2), as in A44 igg.py.
NN bonds gauge-factor i (|y| = |x| + 1); face-diagonal (1,1,0): |y|-|x| = 2 -> factor -1; (1,-1,0): 0 -> 1;
axis pair (2,0,0): 2 -> -1.  eta-SU(2) invariance of a bond needs M eps + eps M^* = 0."""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 2)[0] + "/A44")
from a44lib import SIG
eps = np.array([[0, 1], [-1, 0]], complex)
def defect(M): return np.abs(M @ eps + eps @ M.conj()).max()
for lab, d in (("fd(1,1,0)", (1, 1, 0)), ("fd(1,-1,0)", (1, -1, 0)), ("axis(2,0,0)", (2, 0, 0))):
    dh = np.array(d, float) / np.linalg.norm(d); fac = 1j ** (sum(d))
    for nm, M in (("t2", np.eye(2)), ("i lam2 s.d", 1j * sum(dh[c] * SIG[c] for c in range(3)))):
        print(f"{lab:11s} {nm:11s}: gauged |M eps + eps M*| = {defect(fac * M):.2f}  ({'breaks eta-SU(2) -> U(1)' if defect(fac * M) > 1e-12 else 'SU(2)-invariant'})")
