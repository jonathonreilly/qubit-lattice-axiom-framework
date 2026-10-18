#!/usr/bin/env python3
"""B24 part 1b: scale-free form of the lattice obstruction (exact rational arithmetic).
k* is fixed by all 24 PSG rotations mod 2piZ^3 (B20_check chk3), so around k* the affine action is linear:
k* + q -> k* + R q (mod 2piZ^3).  Every rotation-invariant lattice is cubic: sc_a = aZ^3, fcc_a = a{n: sum n even},
bcc_a = aZ^3 u aZ^3 + (a/2)(1,1,1).  For each type the witness q_w
     sc: (a/2) e_x        fcc: (a/2)(0,1,1)        bcc: (a/2) e_z
is fixed mod Lambda by a commuting C2 pair and not by T (exact, any a: the check is done in units of a with Fractions),
and the affine action itself is cross-checked on (pi/16)Z^3 against the operator-derived c_R.  Prints PASS/FAIL, TOTAL."""
import sys, os, itertools
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from b24lib import ACT, IST, C2PAIRS, kst
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
ks16 = np.round(kst / (np.pi / 16)).astype(int)
check("k* is fixed by all 24 rotations mod 2piZ^3 under the operator-derived affine action", all(np.all((R @ ks16 + c - ks16) % 32 == 0) for R, c in ACT))
def member(kind, x):           # x in units of a (Fractions)
    if kind == 'sc': return all(v.denominator == 1 for v in x)
    if kind == 'fcc': return all(v.denominator == 1 for v in x) and sum(x) % 2 == 0
    if kind == 'bcc': return all(v.denominator == 1 for v in x) or all((v - Fr(1, 2)).denominator == 1 for v in x)
W = {'sc': (Fr(1, 2), 0, 0), 'fcc': (0, Fr(1, 2), Fr(1, 2)), 'bcc': (0, 0, Fr(1, 2))}
res = {}
for kind, q in W.items():
    q = [Fr(v) for v in q]
    fix = [i for i, (R, c) in enumerate(ACT) if member(kind, [sum(int(R[r, s]) * q[s] for s in range(3)) - q[r] for r in range(3)])]
    hasT = all(i in fix for i in range(24) if IST[i]); pair = [p for p in C2PAIRS if p[0] in fix and p[1] in fix]
    res[kind] = (len(fix), hasT, len(pair))
check("witness q_w is fixed by a commuting C2 pair and not by T, for sc, fcc and bcc (scale-free: units of a)",
      all(not v[1] and v[2] > 0 for v in res.values()), f"(little-group order, T?, #C2 pairs) = {res}")
# cross-check with the affine action on (pi/16)Z^3 for the dyadic scales a = 2pi/n, n = 1,2,4,8 (point k*+q mod Lambda)
ok = True
for kind in W:
    for n in (1, 2, 4, 8):
        a16 = 32 // n
        def mem16(v):
            x = [Fr(int(t), a16) for t in v]; return member(kind, x)
        if kind == 'fcc' and n % 2: continue          # fcc_a contains 2piZ^3 only for even 2pi/a
        q16 = np.array([int(Fr(v) * a16) for v in W[kind]]); k = ks16 + q16
        fix = [i for i, (R, c) in enumerate(ACT) if mem16(R @ k + c - k)]
        ok &= (not all(i in fix for i in range(24) if IST[i])) and any(p[0] in fix and p[1] in fix for p in C2PAIRS)
check("same verdict from the full affine action at k* + q_w on (pi/16)Z^3, a = 2pi, pi, pi/2, pi/4 (fcc: a = pi, pi/2, pi/4, the ones containing 2piZ^3)", ok)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
