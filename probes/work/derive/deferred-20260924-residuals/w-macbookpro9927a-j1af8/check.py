#!/usr/bin/env python3
"""Rotor-tail residual (#8957/#8958): the dark phases of the fibre generator -- worker w-macbookpro9927a-j1af8.

The construction (charge words, dark/bright split, the bright-from-dark Laurent block) is copied from the landed
exact control scripts/mobile_rotor_exact_tail_control_20260924.py (main, sha256 53170069...), unchanged in content.
Families (see ATTEMPT.md):
  S  the source's invariants: grade sizes 36/96/36, 24 dark and 72 bright words, flat-phase rank 23, uniform kernel.
  H  all 32 half-period phases z in {+-1}^5: exactly 8 are dark (kernel dims 1,1,2,1,1,2,4,2); at each the pencil
     [B | dB_1 K | ... | dB_5 K] has full column rank r + 5 dim K (non-degenerate); the three actual inputs overlap each
     dark kernel with 1/12, 1/12, 1/6 per kernel dimension.
  G  global reduction: 20 unit pivots (monomials, units on (C*)^5) leave a 52x4 residual; a dark phase needs either
     a rank-deficient 4x3 block, whose factored minor is -(z2^3 - z4^3 z5)(z2^3 z5 - z4^3)(z1 z3 + 1), or all 48
     column-21 entries zero, which forces z = (-1,-1,1,1,-1), a half-period dark point.
Everything is exact (integers, rationals, sympy Laurent polynomials).
"""
import sys
from collections import defaultdict
from itertools import combinations, product

import sympy as s

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


# ------------------------------------------------------------------ source construction (landed control, verbatim logic)
A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
edges = tuple((a, b) for a in A for b in B if a ^ b in (1, 2, 4))
tree = (1, 2, 3, 4, 6, 9, 11)
chords = (0, 5, 7, 8, 10)
words = []
for occupied in combinations(range(8), 6):
    for minus in occupied:
        words.append(tuple((-1 if i == minus else 1) if i in occupied else 0 for i in range(8)))
grade = lambda q: sum(q[a] == 0 for a in A)
low = [q for q in words if grade(q) == 0]
middle = [q for q in words if grade(q) == 1]
upper = [q for q in words if grade(q) == 2]
dark = [q for q in middle if not any(q[a] == q[b] == 0 for a, b in edges)]
bright = [q for q in middle if q not in dark]


def step(q, inward=False):
    result = []
    for ei, (a, b) in enumerate(edges):
        legal = q[a] == 0 and q[b] != 0 if inward else q[a] != 0 and q[b] == 0
        if not legal:
            continue
        charge = q[b] if inward else q[a]
        qq = list(q)
        qq[a], qq[b] = (charge, 0) if inward else (0, charge)
        shift = [0] * 5
        if ei in chords:
            shift[chords.index(ei)] = (charge if inward else -charge)
        result.append((tuple(qq), tuple(shift)))
    return result


def commutator_column(q):
    result = defaultdict(int)
    for first_inward, sign in [(True, 1), (False, -1)]:
        for q1, e1 in step(q, first_inward):
            for q2, e2 in step(q1, not first_inward):
                result[(q2, tuple(x + y for x, y in zip(e1, e2)))] += sign
    return {k: v for k, v in result.items() if v}


columns = [commutator_column(q) for q in dark]
ENT = []                                   # (bright row, dark column, exponent, coefficient)
for j, col in enumerate(columns):
    for (q, e), val in col.items():
        ENT.append((bright.index(q), j, e, val))


def parity(signs, e):
    return (-1) ** sum(ee % 2 for sg, ee in zip(signs, e) if sg == -1)


def B_at(signs):
    M = s.zeros(72, 24)
    for i, j, e, val in ENT:
        M[i, j] += val * parity(signs, e)
    return M


def D_at(signs, k):                        # dB/dtheta_k at a half-period point, divided by i (integer matrix)
    M = s.zeros(72, 24)
    for i, j, e, val in ENT:
        M[i, j] += e[k] * val * parity(signs, e)
    return M


# ------------------------------------------------------------------ family S
Bflat = B_at((1,) * 5)
ok("S1", [len(low), len(middle), len(upper), len(dark), len(bright)] == [36, 96, 36, 24, 72]
   and all(q not in dark for col in columns for q, _ in col) and Bflat.rank() == 23
   and Bflat * s.ones(24, 1) == s.zeros(72, 1),
   "source invariants: grades 36/96/36, 24 dark and 72 bright words, commutator columns land in bright words, "
   "flat-phase rank 23 with the uniform dark vector in the kernel")

# ------------------------------------------------------------------ inputs (source's actual first-mark vectors)
inc = s.zeros(8, 12)
for i, (a, b) in enumerate(edges):
    inc[a, i] = 1
    inc[b, i] = -1
T = inc.extract(range(7), tree)
background = s.Matrix([int(i in A) for i in range(8)])
refs = {}
for q in words:
    rhs = s.Matrix(q) - background
    v = T.inv() * rhs[:7, 0]
    E = s.zeros(12, 1)
    for k, ti in enumerate(tree):
        E[ti] = v[k]
    refs[q] = E


def physical_F(vec, center=None):
    out = defaultdict(int)
    for (q, E), amp in vec.items():
        for ei, (a, b) in enumerate(edges):
            if center is not None and a != center:
                continue
            if not q[a] or q[b]:
                continue
            qq, ee = list(q), list(E)
            qq[a], qq[b] = 0, q[a]
            ee[ei] -= q[a]
            out[(tuple(qq), tuple(ee))] += amp
    return dict(out)


def birth(vec, sign):
    out = defaultdict(int)
    for (q, E), amp in vec.items():
        if q[0] or q[1]:
            continue
        for sigma in ([sign] if sign else [-1, 1]):
            qq, ee = list(q), list(E)
            qq[0], qq[1] = sigma, -sigma
            ee[0] += sigma
            out[(tuple(qq), tuple(ee))] += amp
    return dict(out)


omega = {(tuple(int(i in A) for i in range(8)), (0,) * 12): 1}
INPUTS = []
for sign in (1, -1, 0):
    bv = birth(physical_F(omega), sign)
    rv = {x: -v for x, v in physical_F(bv, 0).items()}
    b = sum(v * v for v in bv.values())
    items = []
    for (q, E), amp in rv.items():
        w = tuple(int((s.Matrix(E) - refs[q])[c]) for c in chords)
        items.append((dark.index(q), w, amp))
    INPUTS.append((sign, b, items))

# ------------------------------------------------------------------ family H
dark_pts = []
for signs in product((1, -1), repeat=5):
    Bm = B_at(signs)
    r = Bm.rank()
    if r == 24:
        continue
    K = s.Matrix.hstack(*Bm.nullspace())
    d = K.shape[1]
    pencil = Bm.row_join(s.Matrix.hstack(*[D_at(signs, k) * K for k in range(5)]))
    nondeg = pencil.rank() == r + 5 * d
    PK = K * (K.T * K).inv() * K.T
    ovs = []
    for sign, b, items in INPUTS:
        vv = s.zeros(24, 1)
        for jj, w, amp in items:
            vv[jj] += amp * parity(signs, w)
        ovs.append(sp_ov := s.nsimplify((vv.T * PK * vv)[0] / b))
    dark_pts.append((signs, r, d, nondeg, ovs))
want = {(1, 1, 1, 1, 1): 1, (1, 1, 1, -1, -1): 1, (1, -1, -1, 1, -1): 2, (1, -1, -1, -1, 1): 1,
        (-1, 1, -1, 1, 1): 1, (-1, 1, -1, -1, -1): 2, (-1, -1, 1, 1, -1): 4, (-1, -1, 1, -1, 1): 2}
h_ok = {p[0]: p[2] for p in dark_pts} == want and all(p[1] == 24 - p[2] for p in dark_pts)
ok("H1", h_ok, f"exactly 8 of the 32 half-period phases are dark, kernel dims {[want[k] for k in want]} (total 14); "
   "the flat phase is one of them")
ok("H2", all(p[3] for p in dark_pts),
   "at every dark half-period phase the pencil [B | dB_1 K | ... | dB_5 K] has full column rank r + 5 dim K: "
   "no kernel vector stays dark to second order along any direction (non-degenerate)")
per_dim = all(p[4] == [s.Rational(p[2], 12), s.Rational(p[2], 12), s.Rational(p[2], 6)] for p in dark_pts)
ok("H3", per_dim, "the three actual first-mark inputs overlap each dark kernel with 1/12, 1/12, 1/6 per kernel "
   "dimension (flat phase: the source's 1/12, 1/12, 1/6)")

# ------------------------------------------------------------------ family G
z = s.symbols('z1:6')
rows = defaultdict(dict)
for i, j, e, val in ENT:
    rows[i][j] = s.expand(rows[i].get(j, 0) + val * s.Mul(*[zz**ee for zz, ee in zip(z, e)]))


def is_unit(x):
    t = s.Add.make_args(s.expand(x))
    if len(t) != 1 or t[0] == 0:
        return False
    return abs(s.Poly(s.expand(t[0] * s.Mul(*[zz**8 for zz in z])), *z).coeffs()[0]) == 1


R = {i: dict(r) for i, r in rows.items()}
left = set(range(24))
piv = 0
while True:
    best = None
    for i, r in R.items():
        for j, x in r.items():
            if j in left and is_unit(x):
                cand = (sum(1 for rr in R.values() if j in rr), i, j)
                best = cand if best is None or cand < best else best
    if best is None:
        break
    _, pi_, pj = best
    prow = R.pop(pi_)
    pv = prow[pj]
    for i, r in list(R.items()):
        if pj in r:
            f = s.expand(r[pj] / pv)
            for j, x in prow.items():
                nv = s.expand(r.get(j, 0) - f * x)
                if nv == 0:
                    r.pop(j, None)
                else:
                    r[j] = nv
            r.pop(pj, None)
            if not r:
                R.pop(i)
    left.discard(pj)
    piv += 1
cols_left = sorted(left)
resid = {i: {j: x for j, x in r.items() if j in left} for i, r in R.items()}
resid = {i: r for i, r in resid.items() if r}
four = [i for i, r in resid.items() if cols_left[-1] not in r]
blk = s.Matrix([[resid[i].get(j, 0) for j in cols_left[:3]] for i in four])
minors = [s.expand(s.fraction(s.together(blk.extract(list(rr), [0, 1, 2]).det(method='berkowitz')))[0])
          for rr in combinations(range(4), 3)]
target = -(z[1]**3 - z[3]**3 * z[4]) * (z[1]**3 * z[4] - z[3]**3) * (z[0] * z[2] + 1)
g_ok = piv == 20 and len(cols_left) == 4 and len(resid) == 52 and len(four) == 4 and any(s.expand(m - target) == 0 or s.expand(m + target) == 0 for m in minors)
ok("G1", g_ok, "20 unit pivots leave a 52x4 residual (dim ker B(z) = dim ker residual on (C*)^5); 4 residual rows "
   "avoid the last column, and one 3x3 minor of that 4x3 block is -(z2^3 - z4^3 z5)(z2^3 z5 - z4^3)(z1 z3 + 1)")
c21 = [resid[i][cols_left[-1]] for i in resid if cols_left[-1] in resid[i]]
simple = [s.factor(s.fraction(s.together(x))[0]) for x in c21]
has = lambda expr: any(s.expand(f - expr) == 0 or s.expand(f + expr) == 0 for f in simple)
sub = {z[4]: -1, z[3]: 1, z[2]: 1, z[1]: -1}
gg = None
for x in c21:
    p = s.expand(s.fraction(s.together(x))[0].subs(sub))
    if p != 0:
        gg = p if gg is None else s.gcd(gg, p)
branch_ok = (has(z[4] + 1) and has(z[1] + z[3]) and has(z[2] + z[3] * z[4]) and has(z[2] + z[4])
             and s.expand(gg - (z[0] + 1)) == 0)
ok("G2", branch_ok, "if all 48 last-column entries vanish then z5 = -1, z2 = -z4, z3 = -z4 z5, z3 = -z5, so "
   "(z2,z3,z4,z5) = (-1,1,1,-1), and the rest force z1 = -1: the half-period dark point (-1,-1,1,1,-1)")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PARTIAL rotor-tail fibre generator: the dark phases on the half-period lattice are exactly 8 "
      "(kernel dims 1,1,2,1,1,2,4,2), all non-degenerate, all overlapped by the actual inputs; if no dark phase "
      "lies off {0,pi}^5 the actual-birth fast energy decays exactly as tau^(-5/2); the off-lattice exclusion is "
      "reduced to three explicit sub-cases (first unresolved step)")
print("HIT: For #8957/#8958's rotor cube (N = 6, charge 4, W = 1), the fibre generator L(theta) = -i delta G(theta) - "
      "kappa P_bright has a purely imaginary eigenvalue exactly where the 72x24 bright-from-dark block B(theta) loses "
      "rank. Among the 32 half-period phases this happens at exactly 8, not only the flat one: kernel dims 1,1,2,1,1,"
      "2,4,2. At each, the pencil [B | dB_k K] has full column rank r + 5 dim K, so Re L is negative definite to "
      "second order along every direction on the dark kernel (non-degenerate). The three actual first-mark inputs "
      "overlap every dark kernel with 1/12, 1/12, 1/6 per dimension. Hence, if no dark phase lies off {0,pi}^5, "
      "c(1+tau)^(-5/2) <= f_i(tau) <= C(1+tau)^(-5/2): the exponent 5/2 of #8958 is exact. Off the lattice, 20 "
      "unit pivots reduce the question to a 52x4 residual; its last-column branch gives only (-1,-1,1,1,-1).")
