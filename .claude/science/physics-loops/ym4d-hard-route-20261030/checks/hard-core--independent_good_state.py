#!/usr/bin/env python3
"""(GOOD) of Text 4.7 in one variable: a cut in xi_eff against a cut in the real noise, at a complex centre.

mu(s)   := int_{|x| <= p2} rho(x - s) Phi(x) dx,    the state of the true integrand, a cut in xi_eff, real x, complex density.
muA(s)  := int_{|xi| <= p} rho(xi) Phi(xi + s) dxi,  state A, a cut in the real noise, a real density.
G(s)    := mu(s) - muA(s).

PRE-STATED CRITERIA, written before the first run. Phi(x) = exp(0.01 i x - 0.002 x^2), analytic with no growth in the range used; (p, p2) = (6, 40), (12, 80), (40, 160).
s = a + i y with a in (0, 1, p / 4), y in (0, p / 16, p / 8).
PASS-GOOD if |G(s)| <= 2 exp(-p^2 / 3) sup |Phi| + 1e-11 for all of these, and |muA(s)| <= sup over the real line of |Phi(xi + s)|, which is the bound with no density. FAIL-GOOD otherwise.
The modulus bound for mu, exp(y^2 / 2), is printed for comparison: the point of gate D2 is that it is large at large p, while |mu| is not. One variable, one analytic Phi: this tests the formula and nothing else.
RESULT OF THE FIRST RUN, as registered: FAIL-GOOD on three cases, all at p = 40, y = 5, with |G| about 1e-10 against the floor 1e-11; all others ok. There |mu| is about 1 from an integrand of size exp(y^2 / 2) = 2.7e5,
so double precision can leave about 1e-10, and my floor did not allow for that. That is a suspicion, not a result. ADDED BEFORE THE SECOND RUN: the same cases in 60 digits with mpmath. PASS-GOOD2 if |G| <= 2 exp(-p^2 / 3) sup |Phi|, with no floor, on all nine cases at p = 40. FAIL-GOOD2 otherwise, and then (GOOD) is wrong.
RESULT OF THE SECOND RUN, as registered: FAIL-GOOD2, but void as a test of the formula: the bound there is 5e-232, and |G| was 1e-58, at the rounding level of 60 digits, as 1e-10 was at 16. So |G| tracks the working precision, and the criterion could not be met at any size of G above it.
ADDED BEFORE THE THIRD RUN: closed forms by erf, at 500 digits, same nine cases. PASS-GOOD3 if |G| <= 2 exp(-p^2 / 3) sup |Phi| on all of them. FAIL-GOOD3 otherwise, and then (GOOD) is wrong.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import numpy as np

rho = lambda z: np.exp(-z * z / 2) / np.sqrt(2 * np.pi)
Phi = lambda z: np.exp(0.01j * z - 0.002 * z * z)


NODES = np.polynomial.legendre.leggauss(1500)  # computed once: the first version recomputed them per integral, and was stopped with nothing read


def integ(f, a, b):
    x, w = NODES
    t = 0.5 * (b - a) * x + 0.5 * (b + a)
    return 0.5 * (b - a) * np.sum(w * f(t))


ok = True
for p, p2 in ((6.0, 40.0), (12.0, 80.0), (40.0, 160.0)):
    for a in (0.0, 1.0, p / 4):
        for y in (0.0, p / 16, p / 8):
            s = a + 1j * y
            mu = integ(lambda x: rho(x - s) * Phi(x), -p2, p2)
            muA = integ(lambda xi: rho(xi) * Phi(xi + s), -p, p)
            G = mu - muA
            supPhi = np.exp(0.002 * y * y) * np.exp(0.01 * y)
            bound = 2 * np.exp(-p * p / 3) * supPhi + 1e-11
            good = abs(G) <= bound and abs(muA) <= supPhi * (1 + 1e-9)
            ok = ok and good
            print(f"p={p:4.0f} a={a:5.1f} y={y:5.2f}  |mu|={abs(mu):.6f} modulus bound {np.exp(y * y / 2):.2e}  |muA|={abs(muA):.6f}  |G|={abs(G):.2e} bound {bound:.2e} {'ok' if good else 'NO'}")
print("PASS-GOOD" if ok else "FAIL-GOOD")

import mpmath as mp
mp.mp.dps = 60
ok2 = True
for p, p2 in ((40, 160),):
    for a in (0, 1, mp.mpf(p) / 4):
        for y in (0, mp.mpf(p) / 16, mp.mpf(p) / 8):
            s_ = mp.mpc(a, y)
            r = lambda z: mp.exp(-z * z / 2) / mp.sqrt(2 * mp.pi)
            P = lambda z: mp.exp(mp.mpc(0, 0.01) * z - mp.mpf("0.002") * z * z)
            pts_mu = [-p2, a - 30, a, a + 30, p2]
            pts_mu = sorted(set(max(-p2, min(p2, t)) for t in pts_mu))
            mu = mp.quad(lambda x: r(x - s_) * P(x), pts_mu)
            muA = mp.quad(lambda xi: r(xi) * P(xi + s_), [-p, -10, 0, 10, p])
            G = mu - muA
            supPhi = mp.exp(mp.mpf("0.002") * y * y) * mp.exp(mp.mpf("0.01") * y)
            bound = 2 * mp.exp(-mp.mpf(p) ** 2 / 3) * supPhi
            good = abs(G) <= bound
            ok2 = ok2 and good
            print(f"p={p} a={float(a):5.1f} y={float(y):5.2f}  |G|={mp.nstr(abs(G), 4)} bound {mp.nstr(bound, 4)} {'ok' if good else 'NO'}")
print("PASS-GOOD2" if ok2 else "FAIL-GOOD2")

mp.mp.dps = 500
ok3 = True
c, d = mp.mpf("0.01"), mp.mpf("0.002")
A = mp.mpf(1) / 2 + d
pref = 1 / mp.sqrt(2 * mp.pi) * mp.sqrt(mp.pi) / (2 * mp.sqrt(A))


def gauss_int(B, C, lo, hi):
    # int_lo^hi exp(-A x^2 + B x - C) dx / sqrt(2 pi)
    return pref * mp.exp(B * B / (4 * A) - C) * (mp.erf(mp.sqrt(A) * (hi - B / (2 * A))) - mp.erf(mp.sqrt(A) * (lo - B / (2 * A))))


p, p2 = mp.mpf(40), mp.mpf(160)
for a in (mp.mpf(0), mp.mpf(1), p / 4):
    for y in (mp.mpf(0), p / 16, p / 8):
        s_ = mp.mpc(a, y)
        mu = gauss_int(s_ + mp.mpc(0, c), s_ * s_ / 2, -p2, p2)
        muA = gauss_int(mp.mpc(0, c) - 2 * d * s_, -(mp.mpc(0, c) * s_ - d * s_ * s_), -p, p)
        G = mu - muA
        supPhi = mp.exp(d * y * y) * mp.exp(c * y)
        bound = 2 * mp.exp(-p * p / 3) * supPhi
        good = abs(G) <= bound
        ok3 = ok3 and good
        print(f"p=40 a={float(a):5.1f} y={float(y):5.2f}  |mu|={mp.nstr(abs(mu), 6)} |G|={mp.nstr(abs(G), 4)} bound {mp.nstr(bound, 4)} exp(-p^2/2)={mp.nstr(mp.exp(-p * p / 2), 3)} {'ok' if good else 'NO'}")
print("PASS-GOOD3" if ok3 else "FAIL-GOOD3")
