#!/usr/bin/env python3
"""B24_check part 4 (claim 5 scoping, exact): pinning (degeneracy forcing) needs OPERATOR-level symmetry, isotropy (L4) only
needs SPECTRAL invariance.  If the operator taste lattice Lam_op is smaller than the spectral one Lam_sp (as found for
S2.L101.S2.H13, chk3b: the (pi/4)(1,1,1) spectral taste has no constant intertwiner), the relevant geometric question is
whether C2pair(mod Lam_op) is contained in Tfix(mod Lam_sp).  Exhaustive over the 10 O-invariant lattices
2piZ^3 <= Lam_op <= Lam_sp <= (pi/4)Z^3, linear action around k* (exact integers, points on (pi/16)Z^3)."""
import itertools, numpy as np
from fractions import Fraction as Fr
ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
tr = [int(np.trace(R)) for R in ROT]
isT = np.array([t in (3, 0) or (t == -1 and np.all(np.abs(np.diag(R)) == 1)) for R, t in zip(ROT, tr)])
C2 = [i for i, t in enumerate(tr) if t == -1]
C2P = [(i, j) for i in C2 for j in C2 if i < j and np.array_equal(ROT[i] @ ROT[j], ROT[j] @ ROT[i])]
# lattices in units pi/16 (mod 32): sc_a, fcc_a, bcc_a with a in pi/16 units
def lat(kind, a):
    S = set()
    for n in itertools.product(range(-64, 65, 1), repeat=1): pass
    for v in itertools.product(range(32), repeat=3):
        x = [Fr(c, a) for c in v]
        if kind == 'sc': ok = all(t.denominator == 1 for t in x)
        elif kind == 'fcc': ok = all(t.denominator == 1 for t in x) and sum(x) % 2 == 0
        else: ok = all(t.denominator == 1 for t in x) or all((t - Fr(1, 2)).denominator == 1 for t in x)
        if ok: S.add(v)
    return S
LATS = {f"sc({a})": lat('sc', a) for a in (32, 16, 8, 4)}
LATS.update({f"fcc({a})": lat('fcc', a) for a in (16, 8, 4)})
LATS.update({f"bcc({a})": lat('bcc', a) for a in (32, 16, 8)})
assert all(all(tuple(x % 32 for x in (32 * np.eye(3, dtype=int)[i])) in L for i in range(3)) for L in LATS.values())
grid = np.array(list(itertools.product(range(32), repeat=3)))
def fixmat(L):
    memb = np.zeros((32,) * 3, bool)
    for v in L: memb[v] = True
    return np.array([memb[tuple(((grid @ R.T - grid) % 32).T)] for R in ROT])
FX = {n: fixmat(L) for n, L in LATS.items()}
def c2pair(F):
    p = np.zeros(len(grid), bool)
    for i, j in C2P: p |= F[i] & F[j]
    return p
def tfix(F): return np.all(F[isT], axis=0)
print("unit pi/16 (scale a in parentheses)")
good = []
for no, Lo in LATS.items():
    for ns, Ls in LATS.items():
        if not Lo <= Ls: continue
        bad = c2pair(FX[no]) & ~tfix(FX[ns]); nb = int(bad.sum())
        if nb == 0: good.append((no, ns))
        print(f"  Lam_op={no:8s} Lam_sp={ns:8s}  #grid points C2pair(op) & not Tfix(sp) = {nb}")
print("\npairs with C2pair(mod Lam_op) contained in Tfix(mod Lam_sp):", good)
print("same-lattice cases among them:", [g for g in good if g[0] == g[1]])
