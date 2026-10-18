"""C4b-03: which elements of the framework group Z^3 x| O preserve the alternating 2x2x2
Margolus partitions P0 = {2m + {0,1}^3} and P1 = P0 + (1,1,1)?  (exhaustive, exact)

g = (R, t): x -> R x + t, R in O (about the site 0), t in Z^3.  Partitions are 2-periodic, so t
mod 2 suffices; we check by explicit point sets on a 6^3 window (blocks fully inside).
The two-step Margolus QCA U = V_{P1} V_{P0} (V an O_c-covariant block unitary) is covariant
under g iff g P0 = P0 and g P1 = P1 (as partitions); g P0 = P1 & g P1 = P0 gives covariance
only up to the half-step conjugation U -> V_{P0} U V_{P0}^{-1} (time glide).
"""
import itertools
import numpy as np
from c4b_common import check, total, O

W = range(-4, 6)


def partition(a):
    blocks = set()
    for m in itertools.product(range(-2, 3), repeat=3):
        base = np.array(a) + 2 * np.array(m)
        blocks.add(frozenset(tuple(int(v) for v in base + np.array(c)) for c in itertools.product((0, 1), repeat=3)))
    return blocks


def inside(block):
    return all(-2 <= v <= 3 for p in block for v in p)


P = {a: {b for b in partition(a) if inside(b)} for a in [(0, 0, 0), (1, 1, 1)]}
FULL = {a: partition(a) for a in [(0, 0, 0), (1, 1, 1)]}


def image(g, blocks):
    R, t = g
    return {frozenset(tuple(int(v) for v in R @ np.array(p) + t) for p in b) for b in blocks}


preserve, swap = [], []
for Ri, R in enumerate(O):
    for t in itertools.product((0, 1), repeat=3):
        t = np.array(t)
        im0 = image((R, t), P[(0, 0, 0)])
        im1 = image((R, t), P[(1, 1, 1)])
        if im0 <= FULL[(0, 0, 0)] and im1 <= FULL[(1, 1, 1)]:
            preserve.append((Ri, tuple(t)))
        if im0 <= FULL[(1, 1, 1)] and im1 <= FULL[(0, 0, 0)]:
            swap.append((Ri, tuple(t)))

print(f"elements (R, t mod 2) preserving (P0,P1): {len(preserve)}; swapping: {len(swap)}")
check("for every R in O exactly one translation class t mod 2 preserves both partitions "
      "(so the stabiliser is a full O about the cube centre, times 2Z^3)",
      len(preserve) == 24 and len({r for r, _ in preserve}) == 24)
site_rot = [r for r, t in preserve if t == (0, 0, 0)]
check("rotations about the lattice site 0 (t=0) preserving the partitions form a group of order 3 "
      "(C3 about (1,1,1)); O about a site is NOT a symmetry", len(site_rot) == 3)
trans = [t for r, t in preserve if np.array_equal(O[r], np.eye(3, dtype=int))]
check("pure translations preserving the partitions: only t = 0 mod 2 (i.e. 2Z^3); e_1 is not a symmetry",
      trans == [(0, 0, 0)])
trans_sw = [t for r, t in swap if np.array_equal(O[r], np.eye(3, dtype=int))]
check("translation by (1,1,1) swaps P0 <-> P1 (time-glide symmetry only)", trans_sw == [(1, 1, 1)])
# rotation about the cube centre c=(1/2,1/2,1/2): x -> R(x-c)+c, i.e. t = c - R c  (integer)
c = np.array([0.5, 0.5, 0.5])
ok = True
for r, t in preserve:
    tc = c - O[r] @ c
    ok &= np.allclose(np.mod(tc, 2), np.array(t))
check("the preserving element for each R is the rotation about the cube centre (t = c - Rc mod 2)", ok)
total()
