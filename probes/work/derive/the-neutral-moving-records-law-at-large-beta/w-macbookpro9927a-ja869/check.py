#!/usr/bin/env python3
"""The neutral moving-records law at large beta -- worker w-macbookpro9927a-ja869.

Two-valued menu at block 40's neutral scale c = c0(beta) = 1/cosh(beta).
Families (see ATTEMPT.md):
  N  the neutral kernel is exactly 1 + t sigma sigma', t = tanh(beta), sigma = n s.
  R  reflection positivity through a plane of sites: an exact Gram check.
  L  low density: no long-range order for z < 1/320 at every beta
     (conditional occupation bound, domination, self-avoiding paths).
  C  high density and large beta: chessboard ratios of all 6559 bad 2x2x2
     patterns, the pattern polynomial, and the Peierls sum; the chessboard
     estimate (A1) and the torus separation lemma (A2) are ASSUMED.
Everything is exact (fractions, integers, sympy).
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


# ---------------------------------------------------------------- family N
b_ = sp.symbols('beta', positive=True)
t = sp.symbols('t', nonnegative=True)
c0 = 1 / sp.cosh(b_)
neutral = all(sp.simplify((c0 * sp.exp(b_ * s * s2)).rewrite(sp.exp)
                          - (1 + sp.tanh(b_).rewrite(sp.exp) * s * s2)) == 0
              for s in (1, -1) for s2 in (1, -1))
avg1 = all(sp.simplify(sum((1 + t * s * s2) for s2 in (1, -1)) / 2 - 1) == 0 for s in (1, -1))
ok("N1", neutral and avg1,
   "c0(beta) e^{beta s s'} = 1 + t s s' (t = tanh beta), so B(u,u') = 1 + t sigma sigma' "
   "with sigma = n s in {-1,0,1}; an occupied neighbour averages to the empty weight 1")

# ---------------------------------------------------------------- family R
tq, zq = Fr(1, 2), Fr(3)
wsite = {-1: zq, 0: Fr(1), 1: zq}
G = [[Fr(0)] * 3 for _ in range(3)]
vals = (-1, 0, 1)
for i, a in enumerate(vals):
    for j, b in enumerate(vals):
        for s0 in vals:
            for s2 in vals:
                G[i][j] += (wsite[s0] * wsite[a] * wsite[s2] * wsite[b] * (1 + tq * s0 * a)
                            * (1 + tq * a * s2) * (1 + tq * s2 * b) * (1 + tq * b * s0))
Gm = sp.Matrix(G)
minors_ok = all(Gm.extract(list(S), list(S)).det() >= 0
                for r in (1, 2, 3) for S in combinations(range(3), r))
ok("R1", minors_ok and Gm == Gm.T,
   "4-ring, reflection through sites {0,2}: the matrix E[1{s1=a}1{s3=b}] is symmetric PSD "
   "(all principal minors >= 0) at t=1/2, z=3")

# ---------------------------------------------------------------- family L
dom_ok = True
top = sp.expand((1 + t)**6 + (1 - t)**6)
for k in range(7):
    for l in range(7 - k):
        e = sp.expand((1 + t)**k * (1 - t)**l + (1 - t)**k * (1 + t)**l)
        d = sp.Poly(top - e, t)
        dom_ok &= all(cf >= 0 for cf in d.all_coeffs())
top_ok = all(cf >= 0 for cf in sp.Poly(top, t).all_coeffs()) and top.subs(t, 1) == 64
ok("L1", dom_ok and top_ok,
   "sum_{s=+-1} prod_{y~x}(1 + t s sigma_y) <= (1+t)^6 + (1-t)^6 <= 64 coefficientwise on "
   "t in [0,1], for all 3^6 neighbourhoods: P(x occupied | rest) <= 64z")
# spins correlate only inside occupied clusters: path 0-1-2-3 with O = {0,1,3}
tt = sp.symbols('tt', positive=True)
O = [0, 1, 3]
num = {}
Zc = 0
for sv in product((1, -1), repeat=3):
    s = dict(zip(O, sv))
    w = 1 + tt * s[0] * s[1]          # the only occupied bond inside O
    Zc += w
    num[(0, 3)] = num.get((0, 3), 0) + w * s[0] * s[3]
    num[(0, 1)] = num.get((0, 1), 0) + w * s[0] * s[1]
ok("L2", sp.simplify(num[(0, 3)] / Zc) == 0 and sp.simplify(num[(0, 1)] / Zc - tt) == 0,
   "given the occupied set, <s0 s3> = 0 across two occupied clusters and <s0 s1> = t inside one")
p = sp.symbols('p', positive=True)
nsum = p + sum(6 * 5**(n - 1) * p**(n + 1) for n in range(1, 40))
closed = p + 6 * p**2 / (1 - 5 * p)
pz = Fr(64, 400)          # z = 1/400
ser_ok = sp.simplify(sp.series(closed - nsum, p, 0, 40).removeO()) == 0
bound400 = pz + 6 * pz**2 / (1 - 5 * pz)
ok("L3", ser_ok and pz < Fr(1, 5) and bound400 == Fr(116, 125),
   f"sum_x P(0<->x) <= p + 6p^2/(1-5p) for p < 1/5 (n-step self-avoiding paths <= 6*5^(n-1)); "
   f"z = 1/400: p <= 4/25, sum <= {bound400}, so M_L^2 <= {bound400}/N -> 0")

# ---------------------------------------------------------------- family C
cube = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
edges = [(i, j) for i in range(8) for j in range(i + 1, 8)
         if sum(abs(cube[i][q] - cube[j][q]) for q in range(3)) == 1]
L4 = 4
tor_sites = list(product(range(L4), repeat=3))
poly = {}
diss_ok = True
count_bad = 0
for tau in product((-1, 0, 1), repeat=8):
    mono = all(v == 1 for v in tau) or all(v == -1 for v in tau)
    V = sum(1 for v in tau if v == 0)
    m = sum(1 for i, j in edges if tau[i] * tau[j] == -1)
    same = sum(1 for i, j in edges if tau[i] * tau[j] == 1)
    kvac = 12 - m - same
    # dissemination on the 4^3 torus: sigma(x) = tau(x mod 2); count factors directly
    occ = sames = opps = vacb = 0
    val = {x: tau[cube.index(tuple(q % 2 for q in x))] for x in tor_sites}
    for x in tor_sites:
        occ += val[x] != 0
        for d in range(3):
            y = list(x); y[d] = (y[d] + 1) % L4
            pr = val[x] * val[tuple(y)]
            sames += pr == 1; opps += pr == -1; vacb += pr == 0
    diss_ok &= (occ, sames, opps, vacb) == (8 * (8 - V), 16 * same, 16 * m, 16 * kvac)
    if not mono:
        count_bad += 1
        poly[(V, m)] = poly.get((V, m), 0) + 1
ok("C1", diss_ok and count_bad == 3**8 - 2 and min(m for (V, m) in poly if V == 0) == 3,
   "all 3^8 patterns: the 2-periodic extension on the 4^3 torus has (occupied sites, same, "
   "opposite, vacant bonds) = 8(8-V, 2same, 2m, 2k); so w_tau/w_+ = z^-V ((1-t)/(1+t))^{2m} "
   "(1+t)^{-2k} and z(tau) <= A^V U^m, A = z^(-1/8), U = ((1-t)/(1+t))^(1/4); 6559 bad, "
   "min m = 3 without vacancies")
A, U = sp.symbols('A U', positive=True)
Ppoly = sum(cnt * A**V * U**m for (V, m), cnt in poly.items())
lead = {(1, 0): 16, (0, 3): 16, (1, 2): 48, (2, 0): 56, (0, 4): 30}
ok("C2", all(poly[k] == v for k, v in lead.items()) and len(poly) == 42,
   f"pattern polynomial P(A,U) = 16A + 16U^3 + 48AU^2 + 56A^2 + 30U^4 + ... ({len(poly)} terms, "
   f"{sum(poly.values())} patterns)")
A0, U0 = Fr(1, 10**5), Fr(1, 100)
eps = sum(Fr(cnt) * A0**V * U0**m for (V, m), cnt in poly.items())
q = 676 * eps
peierls = 2 * eps + 2 * eps / (1 - q)**2
corr = 1 - 2 * peierls
ok("C3", eps <= Fr(1, 2704) and q <= Fr(1, 4) and corr > Fr(99, 100),
   f"at A <= 1e-5 (z >= 1e40), U <= 1e-2 (1 - tanh beta <= 1e-8): eps = P <= "
   f"{float(eps):.3e} <= 1/2704, q = 676 eps = {float(q):.3f}; "
   f"<sigma_0 sigma_x> >= 1 - 2[2eps + 2eps/(1-q)^2] - o(1) = {float(corr):.5f} - o(1)")
qq = sp.symbols('q', positive=True)
geo_ok = sp.expand(sp.series(2 / (1 - qq)**2, qq, 0, 30).removeO()
                   - sum(2 * n * qq**(n - 1) for n in range(1, 31))) == 0
ok("C4", geo_ok,
   "sum_{n>=1} 2n 676^(n-1) eps^n = 2eps/(1-q)^2 (surrounding sets meet a ray within n steps; "
   "connected sets of n cubes through a given one <= 26^(2(n-1)))")
# the parameter region: z >= 10^40 and 1 - tanh(beta) <= 1e-8
bmin = sp.log(2 * 10**8 - 1) / 2
ok("C5", sp.N(bmin, 8) > 9.55 and sp.N(bmin, 8) < 9.56,
   f"1 - tanh(beta) <= 1e-8 iff beta >= log(2e8 - 1)/2 = {float(sp.N(bmin, 8)):.4f}; "
   "the density is >= 1 - eps there")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PARTIAL two-valued menu at the neutral scale: the kernel is 1 + tanh(beta) "
      "sigma sigma'; no long-range order for z < 1/320 at every beta (exact); long-range order "
      "for z >= 10^40, 1 - tanh(beta) <= 1e-8 by reflection positivity in site planes and a "
      "chessboard Peierls bound (A1, A2 ASSUMED); the sphere menu is not reached")
print("HIT: At block 40's neutral scale c = 1/cosh(beta), the two-valued law with vacancies "
      "has kernel B = 1 + t sigma_x sigma_y exactly (t = tanh beta, sigma = n s in {-1,0,1}). "
      "(i) For every beta and z < 1/320, sum_x <sigma_0 sigma_x> <= p + 6p^2/(1-5p), p = 64z, "
      "on every even torus: spins correlate only inside occupied clusters and the occupied "
      "set is dominated by site percolation at 64z, so no long-range order. (ii) The law is "
      "reflection positive through planes of sites; a bad 2x2x2 pattern tau has chessboard "
      "weight <= A^V U^m (A = z^-1/8, U = ((1-t)/(1+t))^1/4, V vacancies, m opposite "
      "edges), P(A,U) = 16A + 16U^3 + ...; with the chessboard estimate and the torus "
      "separation lemma (both ASSUMED), P <= 1/2704 gives <sigma_0 sigma_x> >= 1 - 2[2P + "
      "2P/(1-676P)^2] - o(1) for all x, e.g. >= 0.996 for z >= 10^40 and 1 - tanh beta <= "
      "1e-8. So the neutral two-valued law orders at large beta and high density, and does "
      "not at low density.")
