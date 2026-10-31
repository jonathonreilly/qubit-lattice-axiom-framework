#!/usr/bin/env python3
"""r55a_1 -- S4' contour degeneracy at d=4, L=3. Criteria: checks/r55a_1_criteria.md (written first).
Integers and fractions.Fraction only; no floats. Reviewer: claude-opus-5-5 (REVIEW55_ARS.md)."""
from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter
from math import comb, factorial
import random

d, L, MU = 4, 3, 0
HALF = (L - 1) // 2
sites = list(product(range(-HALF, HALF + 1), repeat=d))
orders = list(permutations(range(d)))

def axial(y, sigma):
    """complete-axial path c_X -> c_X+y in order sigma, as unit steps (axis, sign)."""
    steps = []
    for a in sigma:
        s = 1 if y[a] > 0 else -1
        steps += [(a, s)] * abs(y[a])
    return tuple(steps)

def full_word(y, sigma, far_sigma=None):
    p = axial(y, sigma)
    q = axial(y, far_sigma if far_sigma is not None else sigma)   # far-end path c_Y -> y+L e_mu (translate)
    return p + ((MU, 1),) * L + tuple((a, -s) for (a, s) in reversed(q))

def reduce_word(w):
    st = []
    for a, s in w:
        if st and st[-1] == (a, -s):
            st.pop()
        else:
            st.append((a, s))
    return tuple(st)

out = []
P = out.append
P("r55a_1  S4' degeneracy, d=4, L=3, mu=axis 0  (criteria: r55a_1_criteria.md)")

# E1
n_idx = len(sites) * len(orders)
P(f"E1 index pairs = {n_idx}  -> {'PASS' if n_idx == 1944 else 'FAIL'}")

# E2 labels (y, axial path)
labels = Counter((y, axial(y, s)) for y in sites for s in orders)
hist_lab = dict(sorted(Counter(labels.values()).items()))
E2 = (len(labels) == 633 and hist_lab == {1: 384, 4: 192, 12: 48, 24: 9})
P(f"E2 labels = {len(labels)}, multiplicity histogram {hist_lab}  -> "
  f"{'LABELS-633-CONFIRMED' if E2 else 'LABELS-DISAGREE'}")

# E3 reduced full paths
red = Counter(reduce_word(full_word(y, s)) for y in sites for s in orders)
hist_red = dict(sorted(Counter(red.values()).items()))
E3 = (len(red) == 475 and hist_red == {1: 288, 4: 96, 6: 48, 12: 12, 20: 24, 48: 6, 72: 1})
P(f"E3 freely reduced full paths = {len(red)}, histogram {hist_red}  -> "
  f"{'REDUCED-475-CONFIRMED' if E3 else 'REDUCED-DISAGREE'}")
straight = ((MU, 1),) * L
P(f"   multiplicity of the straight path S_c = {red[straight]}  (weight {F(red[straight], n_idx)})")
P(f"   max label multiplicity = {max(labels.values())} (weight {F(max(labels.values()), n_idx)})")

# E5 closed form
cf = sum(comb(3, k) * 2**k * factorial(k) * (1 + 2*k) for k in range(4))
P(f"E5 closed form sum_k C(3,k)2^k k!(1+2k) = {cf}  -> {'AGREES' if cf == len(red) else 'DISAGREES'}")

# E6 convexity of both partitions
w_lab = [F(m, n_idx) for m in labels.values()]
w_red = [F(m, n_idx) for m in red.values()]
E6 = all(x > 0 for x in w_lab + w_red) and sum(w_lab) == 1 and sum(w_red) == 1
P(f"E6 label weights {sorted(set(w_lab))}")
P(f"   reduced weights {sorted(set(w_red))}")
P(f"   all > 0 and both sum to 1 exactly -> {'CONVEX-PRESERVED' if E6 else 'FAIL'}")

# C1 control: no reduction
raw = Counter(full_word(y, s) for y in sites for s in orders)
C1 = (len(raw) == 633 and len(raw) != len(red))
P(f"C1 control (no free reduction): distinct raw words = {len(raw)}  -> {'FIRES' if C1 else 'DOES-NOT-FIRE'}")

# E7 exact SU(2) holonomies (unit quaternions with rational entries)
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)
def qconj(p):
    return (p[0], -p[1], -p[2], -p[3])
ONE = (F(1), F(0), F(0), F(0))

def rand_unit_quat(rng):
    a, b, c = (F(rng.randint(-40, 40), rng.randint(1, 13)) for _ in range(3))
    n = a*a + b*b + c*c
    q = ((n - 1) / (n + 1), 2*a / (n + 1), 2*b / (n + 1), 2*c / (n + 1))
    assert q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2 == 1
    return q

def make_field(seed):
    rng = random.Random(seed)
    U = {}
    rngs = [range(-2, 6) if a == MU else range(-2, 3) for a in range(d)]
    for x in product(*rngs):
        for a in range(d):
            U[(x, a)] = rand_unit_quat(rng) if seed is not None else ONE
    return U

def holonomy(U, word):
    x = [0] * d
    h = ONE
    for a, s in word:
        if s == 1:
            h = qmul(h, U[(tuple(x), a)]); x[a] += 1
        else:
            x[a] -= 1; h = qmul(h, qconj(U[(tuple(x), a)]))
    return h

def e7(U, far_reversed=False):
    vals = {}
    cls_ok = True
    cls_val = {}
    for y in sites:
        for s in orders:
            w = full_word(y, s, tuple(reversed(s)) if far_reversed else None)
            h = holonomy(U, w)
            vals[h] = vals.get(h, 0) + 1
            if not far_reversed:
                r = reduce_word(w)
                if r in cls_val and cls_val[r] != h:
                    cls_ok = False
                cls_val.setdefault(r, h)
    return len(vals), cls_ok

res = {}
for seed in (1, 2):
    U = make_field(seed)
    nv, ok = e7(U)
    nv_unp, _ = e7(U, far_reversed=True)
    res[seed] = (nv, ok, nv_unp)
    P(f"E7 field seed={seed}: distinct holonomy values (paired S4') = {nv}; same value within every reduced class: {ok}")
    P(f"   C2 control, unpaired far end (reversed order): distinct values = {nv_unp}")
U0 = make_field(None)
nv0, ok0 = e7(U0)
P(f"C3 control, identity field: distinct holonomy values = {nv0}  -> {'FIRES' if nv0 == 1 else 'DOES-NOT-FIRE'}")

ok_all = all(res[s][1] for s in res)
counts = [res[s][0] for s in res]
if not ok_all:
    E7 = "FAIL"
elif all(c == len(red) for c in counts):
    E7 = "PASS"
elif any(c == len(red) for c in counts):
    E7 = "COINCIDENCE-ON-ONE-FIELD"
else:
    E7 = "FAIL"
P(f"E7 verdict: {E7}")
C2 = all(res[s][2] != res[s][0] for s in res)
P(f"C2 verdict: {'FIRES' if C2 else 'DOES-NOT-FIRE'}")

if len(red) != 633 and E7 == "PASS":
    E4 = "REFUTED"
elif len(red) == 633 and E7 == "PASS":
    E4 = "CONFIRMED"
else:
    E4 = "NOT-SETTLED"
P(f"E4 KN_ADOPT's '633 distinct transporters': {E4}  (distinct transporters = {len(red)})")
print("\n".join(out))
