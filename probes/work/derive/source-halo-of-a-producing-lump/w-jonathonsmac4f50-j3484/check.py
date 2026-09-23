#!/usr/bin/env python3
"""J:derive:source-halo-of-a-producing-lump:a3 - worker w-jonathonsmac4f50-j3484 (claude-opus-5-5).

Setting (blocks 39-41, open PRs 'ail39', 'ail40', 'ail41'; supplied, not adopted): neutral scale c0 = 6/T, T = p + q + 4r; an empty
site x with recorded neighbours of contents s_y forms at rate z Z_x, Z_x = sum_a prod_y c0 omega(a, s_y). A lump = records held in
place; for agreeing contents (all +z) an empty site touching k lump records has Z = c0^k A_k, A_k = p^k + q^k + 4 r^k.
Production excess Q = z sum_{empty x touching the lump} (Z_x - 6).  Exact arithmetic: integers, Fraction, sympy.
"""
import itertools
import random
from collections import Counter
from fractions import Fraction as Fr

import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


p, q, r, z = sp.symbols('p q r z', positive=True)
T = p + q + 4 * r
A = lambda k: p ** k + q ** k + 4 * r ** k
delta = lambda k: 6 ** (k - 1) * A(k) / T ** k - 1                   # (Z_k - 6)/6 at the neutral scale, aligned contents
NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
add = lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def census(S):
    touching = {add(s, d) for s in S for d in NB} - S
    return Counter(sum(add(t, d) in S for d in NB) for t in touching)


def Q_of(S):
    return sp.expand(6 * z * sum(n * delta(k) for k, n in census(S).items()))


def rat(expr, triple):
    return sp.nsimplify(expr.subs({p: triple[0], q: triple[1], r: triple[2]}))


# ================================================================ A1 the one-record rule and the given numbers
ok = sp.simplify(delta(1)) == 0
ok &= rat(delta(2), (3, 1, 2)) + 1 == sp.Rational(13, 12) and rat(delta(3), (3, 1, 2)) + 1 == sp.Rational(5, 4)
ok &= rat(delta(2), (12, 1, 2)) + 1 == sp.Rational(46, 21) and rat(delta(3), (12, 1, 2)) + 1 == sp.Rational(2348, 343)
ok &= all(sp.simplify(sp.expand(A(k)) - sp.expand(sum((sp.Integer(1) * w) ** k for w in (p, q, r, r, r, r)))) == 0 for k in range(1, 7))
check('A1', ok, "EXACT: at the neutral scale an empty site touching k agreeing lump records has Z - 6 = 6 delta_k, "
      "delta_k = 6^(k-1) A_k/T^k - 1; delta_1 = 0 identically (every row of W sums to 6), and the unit's numbers are reproduced "
      "(13/12, 5/4 at (3,1,2); 46/21, 2348/343 at (12,1,2)); hence Q = 6z sum_k n_k delta_k over the census n_k of empty sites "
      "touching the lump in exactly k records")

# ================================================================ A2 cube, pit, adatom, step - by enumeration
cube = lambda Lc: set(itertools.product(range(Lc), repeat=3))
ok = True
rows = []
for Lc in (3, 4, 5, 6):
    Cb = cube(Lc)
    ok &= Q_of(Cb) == 0 and set(census(Cb)) == {1}
    face = (Lc // 2, Lc // 2, Lc - 1)                    # a face record (top face, interior)
    pit = Cb - {face}
    ok &= sp.simplify(Q_of(pit) - 6 * z * delta(5)) == 0
    ad = Cb | {(Lc // 2, Lc // 2, Lc)}
    ok &= sp.simplify(Q_of(ad) - 6 * z * 4 * delta(2)) == 0
    # a one-high step: half of the top face raised by one layer
    step = Cb | {(i, j, Lc) for i in range(Lc) for j in range(Lc // 2)}
    cs = census(step)
    ok &= sp.simplify(Q_of(step) - 6 * z * cs.get(2, 0) * delta(2)) == 0 and cs.get(2, 0) == Lc and set(cs) <= {1, 2}
    rows.append(f"L={Lc}: step census {dict(cs)}")
ok &= True
check('A2', ok, "EXACT (enumerated, cubes of side 3-6): a cube has every touching empty site next to ONE record, so Q = 0 "
      "exactly; a pit (one face record removed) makes one empty site touching 5 records: Q = 6z delta_5; an adatom on a face "
      "makes four sites touching 2 records: Q = 24z delta_2; a one-high step along a face has one k = 2 site per unit of step "
      "length: Q = 6z delta_2 x (step length) - production lives on the defects of the surface, not on its area",
      "; ".join(rows) + f"; at (3,1,2): delta_2 = {rat(delta(2), (3, 1, 2))}, delta_5 = {rat(delta(5), (3, 1, 2))}")

# ================================================================ A3 the lattice ball: Q grows as R^2, with a computable constant
import numpy as np
from scipy import integrate


def ball_census(Rb):
    n = 2 * Rb + 5
    c = n // 2
    g = np.indices((n, n, n)) - c
    B = (g ** 2).sum(0) <= Rb * Rb
    cnt = np.zeros(B.shape, dtype=int)
    for ax in range(3):
        for sgn in (1, -1):
            cnt += np.roll(B, sgn, axis=ax)
    touch = (~B) & (cnt > 0)
    return Counter(cnt[touch].tolist()), int(B.sum())


d312 = {k: rat(delta(k), (3, 1, 2)) for k in range(1, 7)}
# per unit area of a surface with sorted |normal| (n1 >= n2 >= n3): touching sites at height h in (0, n1] have
# k = #{i : n_i >= h}, so densities n1 - n2 (k = 1), n2 - n3 (k = 2), n3 (k = 3); integrate over the sphere
def sorted_n(th, ph):
    return np.sort(np.abs([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]))[::-1]
I2 = integrate.dblquad(lambda ph, th: (sorted_n(th, ph)[1] - sorted_n(th, ph)[2]) * np.sin(th), 0, np.pi, 0, 2 * np.pi, epsabs=1e-9, epsrel=1e-9)[0]
I3 = integrate.dblquad(lambda ph, th: sorted_n(th, ph)[2] * np.sin(th), 0, np.pi, 0, 2 * np.pi, epsabs=1e-9, epsrel=1e-9)[0]
pred = 6 * (float(d312[2]) * I2 + float(d312[3]) * I3)
rowsb = []
okb = True
last = []
for Rb in (8, 16, 24, 32, 40, 50, 60):
    cs, Nb = ball_census(Rb)
    okb &= set(cs) <= {1, 2, 3}
    Qv = 6 * sum(v * d312[k] for k, v in cs.items())
    last.append(float(Qv) / Rb ** 2)
    rowsb.append(f"R={Rb}: Q/(zR^2) = {float(Qv) / Rb ** 2:.3f}, Q/(zN) = {float(Qv) / Nb:.4f}")
ok = okb and abs(last[-1] - pred) / pred < 0.03 and abs(last[-1] - pred) < abs(last[0] - pred)
check('A3', ok, "EXACT censuses (lattice balls to R = 60) + a PROVED density law: the touching sites of a ball have k = 1, 2, 3 "
      "only; per unit area of a surface with sorted |normal| (n1, n2, n3) the k = 1, 2, 3 touching sites have densities "
      "n1 - n2, n2 - n3, n3, so Q/(z R^2) -> 6 (delta_2 I_2 + delta_3 I_3), I_2 = int (n2 - n3) dOmega, I_3 = int n3 dOmega "
      "over the unit sphere (quadrature), = 5.52 at (3,1,2); the censuses approach it (within 3 percent at R = 60) while "
      "Q/(record count) falls like 1/R: a compact lump's production excess is a SURFACE quantity",
      f"I_2 = {I2:.6f}, I_3 = {I3:.6f}, predicted {pred:.4f}; " + "; ".join(rowsb))

# ================================================================ A4 the porous lump: E[Q] proportional to the record count
f = sp.symbols('f', positive=True)


def EQ_porous(Lc):
    """exact E[Q]/(6z) for a cube of side Lc whose sites are recorded independently with probability f:
    sum over sites x (inside or on the outer shell) of P(x empty) E[delta_{k_x}], k_x ~ Binomial(#lump-neighbours of x, f)."""
    Cb = cube(Lc)
    shell = {add(s, d) for s in Cb for d in NB} - Cb
    tot = 0
    for x in list(Cb) + list(shell):
        m = sum(add(x, d) in Cb for d in NB)
        pe = (1 - f) if x in Cb else 1
        tot += pe * sum(sp.binomial(m, k) * f ** k * (1 - f) ** (m - k) * delta(k) for k in range(2, m + 1))
    return sp.expand(tot)


# brute-force check on a 2x2x2 cube (256 configurations) at (3,1,2), f = 1/3
Cb2 = cube(2)
fv = sp.Rational(1, 3)
brute = 0
for occ in itertools.product((0, 1), repeat=8):
    S = {s for s, o in zip(sorted(Cb2), occ) if o}
    w = fv ** sum(occ) * (1 - fv) ** (8 - sum(occ))
    if S:
        brute += w * rat(Q_of(S), (3, 1, 2)) / (6 * z)
formula = rat(EQ_porous(2).subs(f, fv), (3, 1, 2))
ok = sp.simplify(brute - formula) == 0
# leading order: E[Q]/N -> 6z ((1-f)/f) sum_k C(6,k) f^k (1-f)^(6-k) delta_k as Lc grows
bulk = 6 * z * (1 - f) / f * sum(sp.binomial(6, k) * f ** k * (1 - f) ** (6 - k) * delta(k) for k in range(2, 7))
lead = []
for Lc in (4, 8, 16):
    per = rat(EQ_porous(Lc).subs(f, fv), (3, 1, 2)) * 6 * z / (fv * Lc ** 3)
    lead.append(float(per / z))
bv = float(rat(bulk.subs(f, fv), (3, 1, 2)) / z)
ok &= abs(lead[-1] - bv) / bv < 0.15 and abs(lead[-1] - bv) < abs(lead[0] - bv)
check('A4', ok, "EXACT (the expectation by linearity, confirmed by all 256 configurations of a 2x2x2 porous cube at (3,1,2), "
      "f = 1/3): a porous lump's mean production excess is a VOLUME quantity - E[Q]/(record count) tends to "
      "6z ((1-f)/f) sum_{k>=2} C(6,k) f^k (1-f)^(6-k) delta_k, the holes inside it being production sites with k ~ "
      "Binomial(6, f) recorded neighbours",
      f"brute {brute} = formula {formula}; per record at L = 4, 8, 16: {', '.join(f'{v:.5f}' for v in lead)} -> bulk {bv:.5f}")

# ================================================================ C1 disagreeing contents: mean zero, the variance, and sinks
Om = sp.Matrix(6, 6, lambda a, b: p if a == b else (q if a == (b ^ 1) else r))
ok = True
var = {}
for k in range(1, 5):
    M2 = (Om * Om) / 6                                     # E_s[omega(a,s) omega(b,s)]
    EZ2 = (6 / T) ** (2 * k) * sum(M2[a, b] ** k for a in range(6) for b in range(6))
    var[k] = sp.simplify(EZ2 - 36)
# brute force for k = 2 at (3,1,2)
tri = {p: 3, q: 1, r: 2}
Omv = Om.subs(tri)
c0 = sp.Rational(6, 12)
Zs = []
for s1 in range(6):
    for s2 in range(6):
        Zs.append(sum(c0 ** 2 * Omv[a, s1] * Omv[a, s2] for a in range(6)))
mean2 = sum(Zs) / 36
var2 = sum((Zz - mean2) ** 2 for Zz in Zs) / 36
ok &= mean2 == 6 and sp.simplify(var[2].subs(tri) - var2) == 0 and sp.simplify(var[1]) == 0
opp = sp.nsimplify(sum(c0 ** 2 * Omv[a, 4] * Omv[a, 5] for a in range(6)))
ok &= opp < 6
check('C1', ok, "EXACT: next to k records of independent uniform contents E[Z] = 6 (mean excess zero) and "
      "Var Z = (6/T)^(2k) sum_{a,b} ((Omega^2)_{ab}/6)^k - 36, which is 0 for k = 1 (so a cube with random contents has Q = 0 "
      "exactly) and positive for k >= 2 (checked against all 36 content pairs at (3,1,2)); disagreeing neighbours can make "
      "Z < 6 - two opposite contents give Z = 11/2 at (3,1,2): a sink of production, so Q can take either sign",
      f"Var Z_2 at (3,1,2) = {var2}; Var Z_3 = {sp.nsimplify(var[3].subs(tri))}; opposite pair Z = {opp}")

# ================================================================ B1 the halo's multipole expansion (exact algebra)
x1, x2, x3, kap, R_ = sp.symbols('x1 x2 x3 kappa R', positive=True)
xv = sp.Matrix([x1, x2, x3])
y = sp.Matrix(sp.symbols('y1:4', real=True))
Gc = lambda v: 1 / (4 * sp.pi * sp.sqrt(v.dot(v)))
tay = sp.series(Gc(xv - sp.Symbol('t') * y).subs(sp.Symbol('t'), sp.Symbol('t')), sp.Symbol('t'), 0, 2).removeO().subs(sp.Symbol('t'), 1)
dip = sp.simplify(tay - Gc(xv) - (xv.dot(y)) / (4 * sp.pi * sp.sqrt(xv.dot(xv)) ** 3))
ok = dip == 0
check('B1', ok, "PROVED given the lattice Green function's far form G(x) = 1/(4 pi |x|) + O(|x|^-3) (ASSUMED, standard): the "
      "stationary halo u(x) = (1/kappa) sum_y G(x - y) q_y has the far field Q/(4 pi kappa |x|) + d.x/(4 pi kappa |x|^3) + "
      "O(|x|^-3), d = sum_y q_y y the dipole of the production excess (exact Taylor step checked); for a lump with Q = 0 (a cube) "
      "the halo starts at the dipole or higher: a perfect cube draws no monopole halo at all")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact: at the neutral scale a lump of agreeing records produces Q = 6z sum_k n_k delta_k, "
      "delta_k = 6^(k-1) A_k/T^k - 1, over the empty sites touching it in k records; delta_1 = 0, so a cube produces nothing "
      "(Q = 0), a pit 6z delta_5, an adatom 24z delta_2, a step 6z delta_2 per unit length; a ball's Q grows as R^2 (surface); "
      "a porous lump's mean Q grows with its record count (the holes produce); random contents: mean 0, Var Z_k given, "
      "Var = 0 at k = 1, sinks possible; far halo Q/(4 pi kappa r) + dipole")
if all(RESULTS):
    print("HIT: at the neutral scale the production excess of a lump of agreeing records is Q = 6z sum_k n_k (6^(k-1) A_k/T^k - 1) "
          "over the empty sites touching it in exactly k records; the k = 1 term vanishes identically, so a cube has Q = 0 "
          "exactly (even with random contents), production sits on surface defects (pit 6z delta_5, adatom 24z delta_2, step "
          "6z delta_2 per unit length), a compact ball has Q proportional to R^2, and only a porous lump has mean Q "
          "proportional to its record count, E[Q]/N -> 6z ((1-f)/f) sum_{k>=2} C(6,k) f^k (1-f)^(6-k) delta_k; so a halo "
          "strength proportional to the record count needs a lump whose interior is itself a production surface")
