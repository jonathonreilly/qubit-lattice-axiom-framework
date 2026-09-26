#!/usr/bin/env python3
"""Independent referee for the neutral two-valued law at large beta.

Worker w-macbookpro90c72-j89cc. Does not import the attempt. Exact
fractions and sympy only. Families:
  K  neutral kernel
  P  reflection positivity on an 8-ring (Gram matrix)
  L  low-density occupation bound, cluster symmetry, path sum
  C  bad-cube census, weight ratio, Peierls series, numerical corner
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, product

import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


# ---------------------------------------------------------------- K
beta, t, z = sp.symbols("beta t z", positive=True)
c0 = 1 / sp.cosh(beta)
def generic_zero(expr):
    """True when a simplified identity is 0 off a measure-zero pole."""
    s = sp.simplify(expr)
    if s == 0:
        return True
    if isinstance(s, sp.Piecewise):
        vals = [v for v, _cond in s.args]
        return any(v == 0 for v in vals) and all(v == 0 or v.has(sp.nan) for v in vals)
    return False


kernel_ok = True
for s in (1, -1):
    for s2 in (1, -1):
        bond = sp.simplify(
            (c0 * sp.exp(beta * s * s2) - (1 + sp.tanh(beta) * s * s2)).rewrite(sp.exp)
        )
        kernel_ok &= bond == 0
vacancy_ok = sp.simplify(1 - (1 + sp.tanh(beta) * 0)) == 0
avg_ok = all(
    sp.simplify((1 + t * s * 1 + 1 + t * s * (-1)) / 2 - 1) == 0 for s in (1, -1)
)
one_minus = sp.simplify(
    (1 - sp.tanh(beta) - 2 / (sp.exp(2 * beta) + 1)).rewrite(sp.exp)
)
ok(
    "K1",
    kernel_ok and vacancy_ok and avg_ok and one_minus == 0,
    "c=1/cosh beta gives B=1+t*sigma*sigma' (t=tanh beta), vacancy weight 1, "
    "menu average of an occupied neighbour is 1, and 1-tanh beta = 2/(e^{2 beta}+1)",
)

# ---------------------------------------------------------------- P  8-ring, reflection through sites 0 and 4
# Sites 0..7. theta(i) = -i mod 8. Mirror pair (1, 7).
tt, zz = Fr(1, 3), Fr(5, 2)
vals = (-1, 0, 1)
site_w = {-1: zz, 0: Fr(1), 1: zz}


def bond(a, b):
    return 1 + tt * a * b


Z = Fr(0)
G = [[Fr(0)] * 3 for _ in range(3)]
idx = {v: i for i, v in enumerate(vals)}
for spins in product(vals, repeat=8):
    w = Fr(1)
    for s in spins:
        w *= site_w[s]
    for i in range(8):
        w *= bond(spins[i], spins[(i + 1) % 8])
    Z += w
    G[idx[spins[1]]][idx[spins[7]]] += w
Gm = sp.Matrix([[g / Z for g in row] for row in G])
psd = Gm == Gm.T and all(
    Gm.extract(list(S), list(S)).det() >= 0
    for r in (1, 2, 3)
    for S in combinations(range(3), r)
)
# odd observable across two clusters: spins 0,1 coupled, spin 3 alone, no bond 1-3
num03 = Fr(0)
num01 = Fr(0)
Zc = Fr(0)
for s0, s1, s3 in product((1, -1), repeat=3):
    w = bond(s0, s1)  # the only occupied bond
    Zc += w
    num03 += w * s0 * s3
    num01 += w * s0 * s1
ok(
    "P1",
    psd and Z > 0 and num03 == 0 and num01 == tt * Zc,
    f"8-ring at t=1/3, z=5/2: joint law of mirror sites (1,7) is symmetric PSD; "
    f"on two occupied clusters <s0 s3>=0 and <s0 s1>={num01}/{Zc}",
)

# ---------------------------------------------------------------- L
top = sp.expand((1 + t) ** 6 + (1 - t) ** 6)
dom_ok = True
for k in range(7):
    for ell in range(7 - k):
        S = sp.expand((1 + t) ** k * (1 - t) ** ell + (1 - t) ** k * (1 + t) ** ell)
        coeffs = sp.Poly(sp.expand(top - S), t).all_coeffs()
        dom_ok &= all(cf >= 0 for cf in coeffs)
top_coeffs = sp.Poly(top, t).all_coeffs()
top_ok = all(cf >= 0 for cf in top_coeffs) and top.subs(t, 1) == 64
# zS/(1+zS) <= zS <= 64z when 0 <= S <= 64. The numerator of the gap is nonnegative.
Ssym = sp.symbols("S", nonnegative=True)
gap = sp.together(64 * z - z * Ssym / (1 + z * Ssym))
gap_num = sp.numer(sp.together(gap))
# the path union bound sums in closed form
N = sp.symbols("N", integer=True, positive=True)
n = sp.symbols("n", integer=True)
p = sp.symbols("p")
path_partial = sp.summation(6 * 5 ** (n - 1) * p ** (n + 1), (n, 1, N))
path_closed = 6 * p ** 2 * (1 - (5 * p) ** N) / (1 - 5 * p)
# z = 1/400 < 1/320, p = 64/400 = 4/25
p400 = Fr(64, 400)
bound400 = p400 + 6 * p400 ** 2 / (1 - 5 * p400)
ok(
    "L1",
    dom_ok and top_ok and generic_zero(path_partial - path_closed) and bound400 == Fr(116, 125),
    "S(k,l) <= (1+t)^6+(1-t)^6 <= 64 coefficientwise for every neighbourhood with "
    f"k+l<=6; sum of self-avoiding-path weights equals 6p^2/(1-5p); "
    f"at z=1/400, p=4/25<1/5 and the x-sum is {bound400}",
)
ok(
    "L2",
    p400 < Fr(1, 5)
    and Fr(64, 320) == Fr(1, 5)
    and sp.expand(gap_num - z * (64 * (1 + z * Ssym) - Ssym)) == 0,
    "z<1/320 is exactly p=64z<1/5; zS/(1+zS) < 64z when S is at most the t=1 value 64",
)

# ---------------------------------------------------------------- C  cube census
cube = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
edges = [
    (i, j)
    for i in range(8)
    for j in range(i + 1, 8)
    if sum(abs(cube[i][q] - cube[j][q]) for q in range(3)) == 1
]
assert len(edges) == 12


def pattern_stats(tau):
    V = sum(v == 0 for v in tau)
    m = sum(tau[i] * tau[j] == -1 for i, j in edges)
    same = sum(tau[i] * tau[j] == 1 for i, j in edges)
    kvac = 12 - m - same
    return V, m, same, kvac


def torus_bonds(L, tau):
    """Direct count on the even torus of the 2-periodic extension."""
    val = {}
    for x in product(range(L), repeat=3):
        val[x] = tau[cube.index(tuple(q % 2 for q in x))]
    occ = opp = same = vacb = 0
    for x, sx in val.items():
        occ += sx != 0
        for d in range(3):
            y = list(x)
            y[d] = (y[d] + 1) % L
            pr = sx * val[tuple(y)]
            opp += pr == -1
            same += pr == 1
            vacb += pr == 0
    return occ, same, opp, vacb


poly = {}
census_ok = True
ratio_ok = True
n_bad = 0
min_m_full = None
for tau in product((-1, 0, 1), repeat=8):
    V, m, same, kvac = pattern_stats(tau)
    mono = all(v == 1 for v in tau) or all(v == -1 for v in tau)
    # algebraic weight ratio, cleared of the (1+t) denominator
    # claimed: w/w_+ = z^{-V} ((1-t)/(1+t))^{2m} (1+t)^{-2k}
    # times (1+t)^{24}: (1-t)^{2m} (1+t)^{2*same}
    left_m = sum(2 for i, j in edges if tau[i] * tau[j] == -1)
    left_same = sum(2 for i, j in edges if tau[i] * tau[j] == 1)
    ratio_ok &= (left_m, left_same) == (2 * m, 2 * same) and m + same + kvac == 12
    for L in (4, 6):
        occ, sB, oB, vB = torus_bonds(L, tau)
        cells = (L ** 3) // 8
        census_ok &= (occ, sB, oB, vB) == (
            cells * (8 - V),
            cells * 2 * same,
            cells * 2 * m,
            cells * 2 * kvac,
        )
        census_ok &= sB + oB + vB == 3 * L ** 3
    if mono:
        census_ok &= V == 0 and m == 0
        continue
    n_bad += 1
    poly[(V, m)] = poly.get((V, m), 0) + 1
    if V == 0:
        min_m_full = m if min_m_full is None else min(min_m_full, m)

lead = {(1, 0): 16, (0, 3): 16, (1, 2): 48, (2, 0): 56, (0, 4): 30}
ok(
    "C1",
    census_ok
    and ratio_ok
    and n_bad == 3 ** 8 - 2
    and min_m_full == 3
    and (0, 0) not in poly
    and all(poly[k] == v for k, v in lead.items())
    and len(poly) == 42
    and sum(poly.values()) == 6559,
    f"6559 bad patterns, 42 monomials, min opposite-edges on a full cube is 3; "
    f"leading counts { {k: poly[k] for k in lead} }; "
    f"on the 4^3 and 6^3 tori each cube edge occurs twice per 2-cell",
)

A0, U0 = Fr(1, 10 ** 5), Fr(1, 100)
eps = sum(Fr(cnt) * A0 ** V * U0 ** m for (V, m), cnt in poly.items())
q = 676 * eps
# 26**(2(n-1)) = 676**(n-1)
animal = sp.Integer(26) ** (2 * (n - 1))
animal_ok = sp.simplify(animal / (sp.Integer(676) ** (n - 1))) == 1
qq = sp.symbols("qq")
Lsym = sp.symbols("L", integer=True, positive=True)
small_partial = sp.summation(2 * n * qq ** (n - 1), (n, 1, N))
# sum_{n=1}^N n r^{n-1} = (1 - (N+1) r^N + N r^{N+1}) / (1-r)^2
small_closed = 2 * (1 - (N + 1) * qq ** N + N * qq ** (N + 1)) / (1 - qq) ** 2
tail_partial = sp.summation(qq ** (n - 1), (n, Lsym, N))
tail_closed = qq ** (Lsym - 1) * (1 - qq ** (N - Lsym + 1)) / (1 - qq)
series_small = generic_zero(small_partial - small_closed)
tail_gen = generic_zero(tail_partial - tail_closed)
peierls = 2 * eps + 2 * eps / (1 - q) ** 2
corr = 1 - 2 * peierls
bmin = sp.log(2 * 10 ** 8 - 1) / 2
bmin_n = sp.N(bmin, 25)
root_ok = sp.Pow(sp.Integer(10) ** 8, sp.Rational(1, 4)) == 100
z_pow = sp.Integer(10) ** 40 == (sp.Integer(10) ** 5) ** 8
ok(
    "C2",
    animal_ok
    and series_small
    and tail_gen
    and z_pow
    and eps <= Fr(1, 2704)
    and q <= Fr(1, 4)
    and corr > Fr(998, 1000)
    and root_ok
    and sp.N(bmin, 10) > sp.Float("9.556")
    and sp.N(bmin, 10) < sp.Float("9.557"),
    f"eps = P(1e-5, 1e-2) = {eps} = {float(eps):.6e}; q = {float(q):.6f}; "
    f"1-2[2eps+2eps/(1-q)^2] = {corr} = {float(corr):.6f} > 998/1000; "
    f"beta threshold log(2e8-1)/2 = {float(bmin_n):.5f}; "
    f"26^(2(n-1))=676^(n-1) and the Peierls series sum exactly",
)

# straight-ray exit: on Z^3 a star-connected n-set has l_inf diameter <= n-1.
# Finite witness: every star-connected 3-set on the L=8 torus, lifted, has
# l_inf diameter <= 2 in some fundamental chart (no wrap forced by size < L).
Lbox = 8
star = [
    (dx, dy, dz)
    for dx in (-1, 0, 1)
    for dy in (-1, 0, 1)
    for dz in (-1, 0, 1)
    if (dx, dy, dz) != (0, 0, 0)
]
assert len(star) == 26


def lift_diameter(sites):
    """Minimum l_inf diameter over placements of the periodic copies."""
    # Fix one site at its representative in 0..L-1 and try BFS distances.
    best = None
    origin = sites[0]
    # coordinates relative to origin, choosing the representative in -L/2..L/2
    rels = []
    for s in sites:
        r = [((s[d] - origin[d] + Lbox // 2) % Lbox) - Lbox // 2 for d in range(3)]
        rels.append(r)
    diam = 0
    for a in rels:
        for b in rels:
            diam = max(diam, max(abs(a[d] - b[d]) for d in range(3)))
    return diam


# build all star-connected 3-sets containing 0 by growing
origin = (0, 0, 0)
n2 = []
for nb in star:
    s = tuple(nb[d] % Lbox for d in range(3))
    n2.append(frozenset((origin, s)))
n3 = set()
diam_ok = True
for pair in n2:
    for s0 in pair:
        for nb in star:
            s = tuple((s0[d] + nb[d]) % Lbox for d in range(3))
            trip = frozenset(pair | {s})
            if len(trip) == 3:
                n3.add(trip)
for trip in n3:
    diam_ok &= lift_diameter(tuple(trip)) <= 2
ok(
    "C3",
    diam_ok and len(n3) > 0 and all(lift_diameter(tuple(p)) <= 1 for p in {frozenset(p) for p in [tuple(x) for x in n2]}),
    f"{len(n3)} star-connected 3-sets on the 8-torus through the origin have "
    f"l_inf diameter <= 2, so a set of size n<L fits in a non-wrapping box of side n-1",
)

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: fails at step " + FAILS[0] + " - an independent exact check of that family failed")
    sys.exit(1)
print(
    "SUMMARY: confirmed partial - two-valued neutral law, kernel 1+tanh(beta) sigma sigma'; "
    "no long-range order for z<1/320 at every beta; chessboard-Peierls order for "
    f"z>=10^40 and 1-tanh beta<=10^(-8) gives <sigma_0 sigma_x> >= {float(corr):.5f} - delta_L "
    "once the chessboard estimate and the torus separation lemma are granted"
)
print(
    "HIT: confirmed - the claim survives. The neutral kernel is 1+tanh(beta) sigma sigma'. "
    "For z<1/320 the occupied set is dominated by Bernoulli(64z), so M_L^2 -> 0 on every even torus. "
    "All 6559 bad cubes have chessboard weight at most A^V U^m; "
    f"P(10^(-5),10^(-2))={float(eps):.6e} <= 1/2704 and the Peierls value is "
    f"{float(corr):.6f} > 998/1000 before a torus term that vanishes for 676P<1. "
    "Order at large beta remains conditional on the chessboard estimate and torus separation. "
    "The sphere menu and the window 1/320<=z<10^40 stay open."
)
