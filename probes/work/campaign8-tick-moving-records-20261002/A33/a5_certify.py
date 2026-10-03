"""A33 a5: exact impurity certificates for period-2 candidates.
usage: python3 a5_certify.py r2 i1,i2,...|ALLMOB [L=8] [side=3]

A certificate is a pair of Paulis P, Q supported in a box B, each commuting with every generator
on Z^3, with P Q = -Q P. Then the generators leave a local qubit free: the stabilizer group is not
maximal, so the 'state' is not pure (EXACT). The torus is only used to list the generators that
touch B; with L > side + 2*r_inf no generator wraps onto B twice, so commuting with the torus
generators touching B is the same as commuting with the Z^3 generators touching B.
Independently re-verified on Z^3 with the pattern algebra (no torus).
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns, role_of, shape_at
from p2lib import Torus, Elim, pcomm, BITS2L, pat_str
from p2_tests import box

r2 = int(sys.argv[1])
L = int(sys.argv[3]) if len(sys.argv) > 3 else 8
side = int(sys.argv[4]) if len(sys.argv) > 4 else 3
t0 = time.time()
D = pickle.load(open(f"p2a_sols_r{r2}.pkl", "rb"))
S = Space(r2)
if sys.argv[2] == "ALLMOB":
    idx = []
    for line in open(f"p2a_screen_r{r2}.txt"):
        if "mobL4={'V': 0, 'C': 0, 'E': 0, 'F': 0}" not in line:
            idx.append(int(line.split()[0]))
else:
    idx = [int(t) for t in sys.argv[2].split(",")]
assert L > side + 2 * S.rinf


def nullspace_paulis(sh, B):
    """basis of Paulis on box B (as patterns) commuting with all Z^3 generators touching B."""
    Bset = set(B)
    pos = {y: k for k, y in enumerate(B)}
    rows = []
    rad = S.rinf
    xs = set()
    for y in B:
        for d in itertools.product(range(-rad, rad + 1), repeat=3):
            xs.add(tuple(a + b for a, b in zip(y, d)))
    gens = []
    for x in xs:
        role, axis = role_of(x)
        _, p = shape_at(sh[role], role, axis, x)
        if any(z in Bset for z in p):
            gens.append(p)
    E = Elim()
    for p in gens:
        row = 0
        for z, l in p.items():
            if z in pos:
                k = pos[z]
                bx, bz = {1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
                if bz:
                    row |= 1 << (2 * k)
                if bx:
                    row |= 1 << (2 * k + 1)
        E.add(row)
    n = 2 * len(B)
    # nullspace of the row space: solve via reduced echelon
    piv = sorted(E.rows.items())
    # convert to RREF dict pivot->row
    R = {}
    for h, (v, _) in sorted(E.rows.items(), reverse=True):
        R[h] = v
    hs = sorted(R, reverse=True)
    for h in hs:
        for h2 in hs:
            if h2 != h and (R[h2] >> h) & 1:
                R[h2] ^= R[h]
    free = [j for j in range(n) if j not in R]
    basis = []
    for f in free:
        v = 1 << f
        for h, row in R.items():
            if (row >> f) & 1:
                v |= 1 << h
        basis.append(v)
    pats = []
    for v in basis:
        p = {}
        for k, y in enumerate(B):
            x, z = (v >> (2 * k)) & 1, (v >> (2 * k + 1)) & 1
            if x or z:
                p[y] = BITS2L[(x, z)]
        pats.append(p)
    return pats, gens


ncert = 0
for n in idx:
    sol, _ = D["sols"][n]
    sh = shapes_of(S, sol)
    B = box((2, 2, 2), side)
    pats, gens = nullspace_paulis(sh, B)
    pair = None
    for i in range(len(pats)):
        for j in range(i + 1, len(pats)):
            if pcomm(pats[i], pats[j]):
                pair = (pats[i], pats[j])
                break
        if pair:
            break
    if pair:
        # re-verify on Z^3: both commute with every generator touching the box
        okP = all(pcomm(pair[0], g) == 0 for g in gens)
        okQ = all(pcomm(pair[1], g) == 0 for g in gens)
        ncert += okP and okQ
        print(f"#{n}: local logical qubit in a {side}^3 box (dim C_B={len(pats)}); certificate verified on Z^3: {okP and okQ}")
        print(f"     P = {pat_str(pair[0])}\n     Q = {pat_str(pair[1])}")
    else:
        print(f"#{n}: no anticommuting pair in the {side}^3 box (dim C_B={len(pats)})")
print(f"certified impure: {ncert} of {len(idx)}   ({time.time()-t0:.1f}s)")
