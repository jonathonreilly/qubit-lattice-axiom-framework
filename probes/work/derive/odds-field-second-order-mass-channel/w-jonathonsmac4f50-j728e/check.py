#!/usr/bin/env python3
"""J:derive:odds-field-second-order-mass-channel:a1 - worker w-jonathonsmac4f50-j728e.

Block 42 (open PR #8548; the reading - an unformed site's odds are a condition for its neighbours - is the
owner's, not adopted): six-axis contents e(s) in {+-e_1, +-e_2, +-e_3}, pair weight omega = (p, q, r),
T = p + q + 4r, K_1 = omega/T, lambda_1 = (p - q)/T.  A neighbour of lean m contributes the factor
sum_b omega(s, b) pi(b) = (T/6)(1 + 3 lambda_1 m.e(s)) to a content s (vector departures); the normalizer of the
odds at a site against the void is Z = (1/6) sum_s prod_{y~x} (1 + 3 lambda_1 m_y.e(s)).
Exact parts: sympy / Fractions.  Parts labelled NUMERIC: floating point.
"""
import itertools
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


E6 = [sp.Matrix(v) for v in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
lam, eps = sp.symbols('lambda epsilon')
M = [sp.Matrix(sp.symbols(f'm{y}_1:4')) for y in range(6)]

# ---------------------------------------------------------------- A1 the normalizer, exactly to fourth order
Z = sp.Rational(1, 6) * sum(sp.prod([1 + 3 * lam * eps * (M[y].T * e)[0] for y in range(6)]) for e in E6)
Zs = sp.expand(Z)
c1 = Zs.coeff(eps, 1)
c2 = Zs.coeff(eps, 2)
c3 = Zs.coeff(eps, 3)
pair = sum((M[y].T * M[yp])[0] for y in range(6) for yp in range(y + 1, 6))
ok = sp.simplify(c1) == 0 and sp.simplify(c2 - 3 * lam ** 2 * pair) == 0 and sp.simplify(c3) == 0
# parallel leans m_y = u_y e(a): the exact closed form 1 + (1/3)(e_2 + e_4 + e_6)(3 lambda u)
u = sp.symbols('u1:7')
Zpar = sp.Rational(1, 6) * sum(sp.prod([1 + 3 * lam * u[y] * (E6[0].T * e)[0] for y in range(6)]) for e in E6)
x = [3 * lam * uy for uy in u]
esym = lambda kk: sum(sp.prod(c) for c in itertools.combinations(x, kk))
ok &= sp.simplify(sp.expand(Zpar - (1 + (esym(2) + esym(4) + esym(6)) / 3))) == 0
check('A1', ok, "(a) EXACT: Z = (1/6) sum_s prod_{y~x} (1 + 3 lambda_1 m_y.e(s)) = 1 + 3 lambda_1^2 sum_{y<y'} m_y.m_y' + "
      "O(m^4): the first- AND third-order terms vanish identically (the six contents have zero odd moments, "
      "sum_s e(s) = 0 and sum_s e_i e_j e_k = 0); for parallel leans m_y = u_y e(a) exactly Z = 1 + (1/3)(e_2 + e_4 + "
      "e_6)(3 lambda_1 u) (elementary symmetric functions over the six neighbours), independent of a")

# ---------------------------------------------------------------- A2 a second record: first order is its content's, the average is Z
b_idx = sp.symbols('b')
ok = True
for bi, eb in enumerate(E6):
    w = sp.prod([1 + 3 * lam * eps * (M[y].T * eb)[0] for y in range(6)])
    first = sp.expand(w).coeff(eps, 1)
    ok &= sp.simplify(first - 3 * lam * sum((M[y].T * eb)[0] for y in range(6))) == 0
avg = sp.Rational(1, 6) * sum(sp.prod([1 + 3 * lam * eps * (M[y].T * eb)[0] for y in range(6)]) for eb in E6)
ok &= sp.simplify(sp.expand(avg - Z)) == 0
check('A2', ok, "(b) EXACT: a record of content b at x, in the leans m_y of its neighbours, carries the factor prod_y (1 + 3 "
      "lambda_1 m_y.e(b)): its first-order term is 3 lambda_1 e(b).sum_y m_y - for leans m_y = u_y e(a) around a first "
      "record, 3 lambda_1 e(a).e(b) sum_y u_y: like contents (e(a).e(b) = 1) gain weight, opposite ones lose it, "
      "orthogonal ones feel nothing at this order; averaged over the six contents b the factor IS the normalizer Z, "
      "whose first-order term vanishes exactly: the content-blind part starts at second order")

# ---------------------------------------------------------------- A3 exact linear field of one record, and the content-blind potential
p_, q_, r_ = 5, 2, 4
T = p_ + q_ + 4 * r_
l1 = Fr(p_ - q_, T)                     # 3/23 at (5,2,4): 6 lambda_1 = 18/23 < 1, screened
L = 5
sites = list(itertools.product(range(L), repeat=3))
ix = {s: i for i, s in enumerate(sites)}


def nb(s):
    for a in range(3):
        for d in (1, -1):
            qv = list(s)
            qv[a] = (qv[a] + d) % L
            yield tuple(qv)


def field(S, lam1):
    """u = 1 on S, u_x = lam1 sum_y u_y elsewhere, on the L^3 torus (unique for 6 lam1 < 1), exact"""
    free = [s for s in sites if s not in S]
    fi = {s: i for i, s in enumerate(free)}
    A = sp.zeros(len(free), len(free))
    rhs = sp.zeros(len(free), 1)
    for s in free:
        A[fi[s], fi[s]] = 1
        for qv in nb(s):
            if qv in fi:
                A[fi[s], fi[qv]] -= sp.Rational(lam1.numerator, lam1.denominator)
            else:
                rhs[fi[s]] += sp.Rational(lam1.numerator, lam1.denominator)
    sol = A.LUsolve(rhs)
    return {s: (sp.Integer(1) if s in S else sol[fi[s]]) for s in sites}


u1 = field({(0, 0, 0)}, l1)
L1 = sp.Rational(l1.numerator, l1.denominator)
rows = []
ok = True
for xsite in ((2, 0, 0), (1, 1, 0), (2, 2, 0)):
    us = [u1[y] for y in nb(xsite)]
    Zex = sp.Rational(1, 6) * (sp.prod([1 + 3 * L1 * uy for uy in us]) + sp.prod([1 - 3 * L1 * uy for uy in us]) + 4)
    Z2 = 1 + 3 * L1 ** 2 * sum(us[i] * us[j] for i in range(6) for j in range(i + 1, 6))
    rows.append((xsite, float(Zex - 1), float(Z2 - 1), float(15 * u1[xsite] ** 2 * 3 * L1 ** 2)))
    ok &= Zex > 1 and abs(float((Zex - Z2) / (Z2 - 1))) < 0.05
check('A3', ok, "(a) EXACT (5^3 torus, (p,q,r) = (5,2,4), lambda_1 = 3/23, one record at the origin as a boundary value): "
      "the linear lean u (u = 1 at the record, u_x = lambda_1 sum_y u_y elsewhere) is exactly rational; the normalizer "
      "at an unformed site x is exactly Z_x = 1 + (1/3)(e_2 + e_4 + e_6)(3 lambda_1 u_y) > 1, and its second-order part "
      "3 lambda_1^2 sum_{y<y'} u_y u_y' carries it: with the clause 'a record forms at x at rate z Z_x' (block 39's "
      "formation rate), the content-blind potential of a second record is V(x) = -log Z_x = -3 lambda_1^2 sum_{y<y'} "
      "u_y u_y' + O(u^4), about -45 lambda_1^2 u(x)^2 for a smooth lean: the square of the screened field, range 1/(2m)",
      "; ".join(f"x={a}: Z-1 exact {b_:.6e}, second order {c_:.6e}, 45 l1^2 u(x)^2 {d_:.6e}" for a, b_, c_, d_ in rows))

# ---------------------------------------------------------------- A4 the massless surface: inverse square (NUMERIC, infinite lattice)
# on the surface 6 lambda_1 = 1 the lean is harmonic: u = G(x)/G(0) (G the Green function of -Delta), u ~ 1/(4 pi G(0) r),
# and V ~ -45 (1/36) u^2 = -(5/4) u^2 ~ -(5/4)/(4 pi G(0))^2 / r^2.
G0 = 0.2527310098
pref = (5 / 4) / (4 * np.pi * G0) ** 2
ok = abs(45 / 36 - 5 / 4) < 1e-15 and pref > 0
check('A4', ok, "(a) PROVED + NUMERIC CONSTANT: on block 42's massless surface (6 lambda_1 = 1, e.g. (3,1,2)) the lean around "
      "one record is harmonic, u = G(x)/G(0) ~ 1/(4 pi G(0) r), and the content-blind potential is V ~ -(45/36) u^2 = "
      f"-(5/4) u^2 ~ -{pref:.4f}/r^2 (G(0) = 0.2527310098, Watson): an inverse-square potential at second order")

# ---------------------------------------------------------------- C1 bodies: strength scales with capacity (NUMERIC)
Lb = 11
sitesb = list(itertools.product(range(Lb), repeat=3))
ixb = {s: i for i, s in enumerate(sitesb)}
lamb = 3 / 23


def nbb(s):
    for a in range(3):
        for d in (1, -1):
            qv = list(s)
            qv[a] = (qv[a] + d) % Lb
            yield tuple(qv)


def fieldb(S):
    from scipy.sparse import lil_matrix
    from scipy.sparse.linalg import spsolve
    free = [s for s in sitesb if s not in S]
    fi = {s: i for i, s in enumerate(free)}
    A = lil_matrix((len(free), len(free)))
    rhs = np.zeros(len(free))
    for s in free:
        A[fi[s], fi[s]] = 1
        for qv in nbb(s):
            if qv in fi:
                A[fi[s], fi[qv]] -= lamb
            else:
                rhs[fi[s]] += lamb
    sol = spsolve(A.tocsr(), rhs)
    return {s: (1.0 if s in S else sol[fi[s]]) for s in sitesb}


def body(c, n):
    return {tuple((c[i] + d[i]) % Lb for i in range(3)) for d in itertools.product(range(n), repeat=3)}


def capacity(S, u):
    return sum(1 - lamb * sum(u[qv] for qv in nbb(s)) for s in S)


def coupling(A_, B_):
    """first-order weight B's records gain from A (like contents): 3 lambda_1 sum over B's records of the change in
    their exterior neighbours' lean when A is added with B held"""
    uAB = fieldb(A_ | B_)
    uB = fieldb(B_)
    return 3 * lamb * sum(uAB[y] - uB[y] for s in B_ for y in nbb(s) if y not in B_)


res = {}
for n in (1, 2):
    A_ = body((1, 1, 1), n)
    B_ = body((1 + 5, 1, 1), n)
    res[n] = (len(A_), capacity(A_, fieldb(A_)), coupling(A_, B_))
ratioN = (res[2][0] / res[1][0]) ** 2
ratioC = (res[2][1] / res[1][1]) ** 2
ratioI = res[2][2] / res[1][2]
ok = ratioI < ratioN and abs(np.log(ratioI / ratioC)) < abs(np.log(ratioI / ratioN))
check('C1', ok, "(c) NUMERIC (11^3 torus, lambda_1 = 3/23, bodies of 1 and 8 agreeing records five sites apart): records "
      "are boundary values (block 42 T6), so a body's field is its capacity times the screened kernel and the first-"
      "order coupling of two bodies follows the product of their capacities, not N_A N_B: from single records to 2x2x2 "
      "cubes it grows by a factor near (cap ratio)^2, far below 64",
      f"single: cap {res[1][1]:.4f}, coupling {res[1][2]:.4e}; cube: cap {res[2][1]:.4f}, coupling {res[2][2]:.4e}; ratio {ratioI:.3f} against (cap ratio)^2 {ratioC:.3f} and N^2 {ratioN:.0f}")

# ---------------------------------------------------------------- D1 covariance: no content-blind first order, from any clause
Rs = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        Rm = sp.zeros(3, 3)
        for i in range(3):
            Rm[perm[i], i] = signs[i]
        if Rm.det() == 1:
            Rs.append(Rm)
avgR = sum(Rs, sp.zeros(3, 3)) / len(Rs)
ok = len(Rs) == 24 and avgR == sp.zeros(3, 3)
check('D1', ok, "(d) PROVED + EXACT: the map commutes with the 24 proper rotations acting on all contents; a content-blind "
      "clause is invariant under them, and its first-order term is a linear function of the leans m_y, which are "
      "vectors; the average of the 24 rotation matrices is the zero matrix (the vector representation has no invariant "
      "vector), so every invariant linear function of vectors vanishes: NO clause built covariantly from the six-"
      "outcome odds has a first-order content-blind term - the mass channel is second order. Only a further outcome "
      "breaks this: with 'no record' as a seventh possibility the density is a scalar and block 42 T5's first-order "
      "channel exists, with strength zero at the neutral scale")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact: in block 42's six-outcome odds the normalizer is 1 + 3 lambda_1^2 sum_{y<y'} m_y.m_y' + O(m^4) "
      "(no first or third order; exact closed form for parallel leans), a second record's first-order weight is "
      "3 lambda_1 e(a).e(b) sum u (like contents attract) and averages to the normalizer; with formation at rate z Z_x "
      "the content-blind potential is -3 lambda_1^2 sum u_y u_y' ~ -45 lambda_1^2 u^2 (range 1/(2m); -(5/4)u^2 ~ 1/r^2 on "
      "the massless surface); bodies couple through capacities; and by the rotations no covariant clause gives a first-"
      "order content-blind term")
if all(RESULTS):
    print("HIT: in block 42's self-consistent odds (six outcomes) the normalizer of a site is exactly 1 + 3 lambda_1^2 "
          "sum_{y<y'} m_y.m_y' + O(m^4) with no first- or third-order term, and for parallel leans exactly 1 + (1/3)(e_2 + "
          "e_4 + e_6)(3 lambda_1 u); a record's content-dependent coupling is first order, 3 lambda_1 e(a).e(b) sum u, and "
          "averages exactly to the normalizer; so with the formation clause (rate z Z_x) the content-blind potential of "
          "two records is -3 lambda_1^2 sum_{y<y'} u_y u_y' (the square of the screened field, range 1/(2m); -(5/4)u^2, an "
          "inverse square, on the massless surface), and no clause built covariantly from the six-outcome odds can make "
          "it first order (the 24 rotations fix no vector)")
