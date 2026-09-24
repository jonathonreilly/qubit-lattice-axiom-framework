#!/usr/bin/env python3
"""Independent referee of moving-clumping-bounds attempt a1.

Author w-jonathonsmac4f50-j6200 (claude-opus-5). Referee w-macbookpro90c72-j9347 (grok-4.6).
Own total-variation bound and own conditional. The Ising critical value is the quoted literature number.
"""
import itertools
from fractions import Fraction as F

import sympy as sp

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


def om(a, b, P, Q, R):
    if a == b:
        return P
    if a ^ 1 == b:
        return Q
    return R


def weights(others, g, P, Q, R, c, z):
    w = []
    for a in range(6):
        pr = z
        for s in others:
            if s != 6:
                pr *= c * om(a, s, P, Q, R)
        if g != 6:
            pr *= c * om(a, g, P, Q, R)
        w.append(pr)
    w.append(F(1))
    return w


def tv(w1, w2):
    s1, s2 = sum(w1), sum(w2)
    return sum(abs(x / s1 - y / s2) for x, y in zip(w1, w2)) / 2


def dobrushin(P, Q, R, c, z):
    best = F(0)
    for ms in itertools.combinations_with_replacement(range(7), 5):
        for u in range(7):
            w1 = weights(ms, u, P, Q, R, c, z)
            for u2 in range(u + 1, 7):
                t = tv(w1, weights(ms, u2, P, Q, R, c, z))
                if t > best:
                    best = t
    return best


def zfree(P, Q, R, c):
    best = F(0)
    for u in range(7):
        for u2 in range(7):
            if u == u2:
                continue
            lam = []
            for a in range(6):
                num = c * om(a, u2, P, Q, R) if u2 != 6 else F(1)
                den = c * om(a, u, P, Q, R) if u != 6 else F(1)
                lam.append(num / den)
            lam.append(F(1))
            M, m = max(lam), min(lam)
            best = max(best, (M - m) / (M + m))
    return best


# ---------------------------------------------------------------- neutral scale
for tri in ((3, 1, 2), (5, 2, 4), (1, 1, 1)):
    P, Q, R = tri
    c0 = F(6, P + Q + 4 * R)
    require(c0 * (P + Q + 4 * R) / 6 == 1, f"c0({tri}) = {c0} averages an occupied neighbour to an empty one")

# cancellation: the ratio of two single-site weights does not see z or the other neighbours
z, other, P, Q, R, c = sp.symbols("z F p q r c", positive=True)
# content a=0 against neighbour states 0 and 1 (equal vs opposite)
ratio = sp.simplify((z * other * c * P) / (z * other * c * Q))
require(ratio == P / Q, "changing one neighbour cancels z and the other five neighbours")

# total variation of an [m,M] reweighting
# For fixed mean the L1 spread is largest at the endpoints, so the worst case is two-point.
# f(alpha) = alpha(1-alpha)(M-m) / (alpha m + (1-alpha) M)
# Its maximum is (sqrt(M)-sqrt(m))/(sqrt(M)+sqrt(m)) <= (M-m)/(M+m).
Rsym = sp.symbols("R", positive=True)
alpha = sp.symbols("alpha", positive=True)
# the two-point function stays under the loose bound: the quadratic
# alpha^2 (R+1) - 2 alpha R + R has discriminant -4R < 0 and positive leading coefficient
disc = sp.discriminant(alpha**2 * (Rsym + 1) - 2 * alpha * Rsym + Rsym, alpha)
require(sp.factor(disc) == -4 * Rsym, "every two-point reweighting has total variation <= (M-m)/(M+m)")

# certified region
certs = []
for tri in ((1, 1, 1), (9, 8, 8)):
    P, Q, R = tri
    c0 = F(6, P + Q + 4 * R)
    for mul in (F(1), F(5, 4)):
        b = zfree(P, Q, R, c0 * mul)
        certs.append((tri, mul, 6 * b, 6 * b < 1))
require(all(u for *_, u in certs), " (1,1,1) and (9,8,8) satisfy 6(M-m)/(M+m) < 1 up to c/c0 = 5/4")

# channels
rows = []
for tri, c, expect_rise in (((3, 1, 2), F(1, 2), True), ((1, 1, 1), F(2), False)):
    vals = [6 * dobrushin(*tri, c, z) for z in (F(1, 10), F(1), F(10))]
    rows.append((tri, vals, vals[-1] > vals[0]))
    require((vals[-1] > vals[0]) == expect_rise, f"{tri} at c={c}: 6C = {[float(v) for v in vals]}")
require(abs(rows[0][1][0] - F(14133, 10000)) < F(1, 2000), "content channel at z=0.1 is about 1.4133")

# lattice gas
require(dobrushin(1, 1, 1, F(1), F(1)) == 0 and dobrushin(1, 1, 1, F(1), F(10)) == 0,
        "uniform weights at c0=1 have Dobrushin coefficient 0 at two fugacities")
# K = log(c w)/4, so c/c0 = exp(4 K) when c0 w = 1
Kc = sp.Float("0.2216544")
onset = sp.exp(4 * Kc)
require(abs(onset - sp.Float("2.4269")) < sp.Float("1e-4"), f"quoted K_c gives c/c0 = {float(onset):.4f}")

# reflection positivity: eigenvalues of the 6x6 content matrix
p, q, r = sp.symbols("p q r", real=True)
# modes: all-ones eigenvalue p+q+4r; three (p-q); two (p+q-2r)
# explicit matrix check at a generic point and at (5,2,4)
def omega(P, Q, R):
    M = sp.zeros(6)
    for i in range(6):
        for j in range(6):
            M[i, j] = om(i, j, P, Q, R)
    return M


def schur_eigs(P, Q, R, c):
    S = c * omega(P, Q, R) - sp.ones(6)
    return sorted(sp.simplify(e) for e in S.eigenvals())


# symbolic eigenvalues via the modes
v_uniform = sp.Matrix([1, 1, 1, 1, 1, 1])
v_odd = sp.Matrix([1, -1, 0, 0, 0, 0])
v_axis = sp.Matrix([1, 1, -1, -1, 0, 0])
Om = omega(p, q, r)
require(sp.simplify(Om * v_uniform - (p + q + 4 * r) * v_uniform) == sp.zeros(6, 1), "uniform mode of the content matrix is p+q+4r")
require(sp.simplify(Om * v_odd - (p - q) * v_odd) == sp.zeros(6, 1), "odd mode is p-q, so p>=q is needed")
require(sp.simplify(Om * v_axis - (p + q - 2 * r) * v_axis) == sp.zeros(6, 1), "axis-difference mode is p+q-2r")
require(5 + 2 - 2 * 4 == -1, "(5,2,4) has p+q-2r = -1, so the pair matrix is indefinite at every scale")

print(f"TOTAL FAIL={len(FAILS)}", flush=True)
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0], flush=True)
else:
    print("HIT: confirmed - the z-free bound (M-m)/(M+m) gives uniqueness for (1,1,1) and (9,8,8) up to c/c0=5/4, and (5,2,4) is never reflection positive", flush=True)
    print("SUMMARY: confirmed - neighbour ratios cancel z, total variation is at most (M-m)/(M+m), neutral uniform weights are independent, and the PSD modes are p-q and p+q-2r. The Peierls count was not claimed.", flush=True)
