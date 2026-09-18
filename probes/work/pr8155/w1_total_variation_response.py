#!/usr/bin/env python3
"""J:falsifier:PR8155 - block 21 (PR #8155), a stated theorem's finite check: W1, TV(P_h, P_h') <= (beta/(2 sqrt3)) |h - h'| for all
h, h' in R^3, where P_h(ds) is proportional to exp(beta s.h) dsigma(s) on the sphere; with W2's exact antipodal value
TV(P_e, P_-e) = tanh(beta/2).  The runner executes W1's ingredients (the covariance eigenvalues L'(x), L(x)/x <= 1/3 by coefficient ratios
for n <= 12, the derivative identity on a finite weighted space); here the total variation itself is computed, for finite (not
infinitesimal) changes of the field, by quadrature on the sphere, at 2400 random pairs (h, h') with |h|, |h'| up to 12 and beta*|h| up
to 12, at structured pairs (antipodal, orthogonal, parallel), and the coefficient ratios of W1(ii) are extended to n <= 400 exactly.
Machinery.  P_h has density (x/(4 pi sinh x)) e^{beta s.h} with x = beta|h| (uniform at h = 0); TV = (1/2) int |p - q| dsigma by a
Gauss-Legendre rule in cos(theta) (400 nodes) times a uniform rule in phi (800 nodes) in the frame of h + h' (the integrand is smooth
except on the curve p = q, where the rule converges as its mesh; the quadrature error is estimated by halving both resolutions).
HIT if TV exceeds the bound by more than 50 times the estimated quadrature error, if the antipodal value differs from tanh(beta/2) beyond
50 times its own error estimate, or if a coefficient ratio differs from 6/(n(2n-1)) or 3/(2n+1) (or exceeds 1) for some n <= 400.
"""
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np

rng = np.random.default_rng(8155)


def grid(nt, nph):
    t, wt = np.polynomial.legendre.leggauss(nt)          # t = cos(theta) in [-1, 1]
    ph = 2 * np.pi * (np.arange(nph) + 0.5) / nph
    T, PH = np.meshgrid(t, ph, indexing="ij")
    st = np.sqrt(1 - T * T)
    S = np.stack([st * np.cos(PH), st * np.sin(PH), T], -1)
    W = (wt[:, None] * np.ones_like(PH)) * (2 * np.pi / nph)
    return S, W


G_FINE, G_COARSE = grid(400, 800), grid(200, 400)


def log_density(S, v):
    x = np.linalg.norm(v)
    if x < 1e-14:
        return np.full(S.shape[:-1], -math.log(4 * math.pi))
    # log(x/(4 pi sinh x)) stably: sinh x = e^x (1 - e^{-2x})/2
    return math.log(x) - math.log(2 * math.pi) - x - math.log1p(-math.exp(-2 * x)) + S @ v


def tv(beta, h1, h2, g):
    S, W = g
    # rotate so that e3 is along h1 + h2 (the grid is densest near the poles in theta)
    m = np.asarray(h1) + np.asarray(h2)
    if np.linalg.norm(m) > 1e-12:
        e3 = m / np.linalg.norm(m)
        a = np.array([1.0, 0, 0]) if abs(e3[0]) < 0.9 else np.array([0, 1.0, 0])
        e1 = a - (a @ e3) * e3
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(e3, e1)
        R = np.stack([e1, e2, e3], 1)                     # columns: the new frame in old coordinates
        S = S @ R.T
    p = np.exp(log_density(S, beta * np.asarray(h1)))
    q = np.exp(log_density(S, beta * np.asarray(h2)))
    return 0.5 * float(np.sum(W * np.abs(p - q)))


def main():
    t0 = time.time()
    c = 1 / (2 * math.sqrt(3))
    worst = (0.0, None)
    fails = []
    n = 0
    maxerr = 0.0
    pairs = []
    for _ in range(2400):
        beta = float(rng.choice([0.05, 0.1, 0.2, 0.2886, 0.5, 1.0, 2.0]))
        r1, r2 = rng.uniform(0, 12 / beta if beta > 1 else 12), rng.uniform(0, 12 / beta if beta > 1 else 12)
        r1, r2 = min(r1, 12 / beta), min(r2, 12 / beta)
        u1, u2 = rng.normal(size=3), rng.normal(size=3)
        pairs.append((beta, u1 / np.linalg.norm(u1) * r1, u2 / np.linalg.norm(u2) * r2))
    for beta in (0.1, 0.2886, 1.0, 3.0):
        e = np.array([0.0, 0.0, 1.0])
        for r in (0.1, 1.0, 3.0, 6.0):
            pairs.append((beta, e * r, -e * r))
            pairs.append((beta, e * r, np.array([r, 0.0, 0.0])))
            pairs.append((beta, e * r, e * (r + 0.5)))
            pairs.append((beta, e * r, e * r * 1.01))
    for beta, h1, h2 in pairs:
        d = float(np.linalg.norm(h1 - h2))
        if d < 1e-12:
            continue
        v_f = tv(beta, h1, h2, G_FINE)
        v_c = tv(beta, h1, h2, G_COARSE)
        err = abs(v_f - v_c) + 1e-12
        maxerr = max(maxerr, err)
        bound = beta * c * d
        ratio = v_f / (beta * d)
        n += 1
        if ratio > worst[0]:
            worst = (ratio, (beta, np.round(h1, 3).tolist(), np.round(h2, 3).tolist(), v_f, bound, err))
        if v_f > bound + 50 * err:
            fails.append((beta, h1, h2, v_f, bound))
    print(f"[W1] {n} pairs: TV/(beta |h - h'|) at most {worst[0]:.6f} (bound 1/(2 sqrt3) = {c:.6f}), attained at beta = {worst[1][0]}, "
          f"h = {worst[1][1]}, h' = {worst[1][2]} (TV {worst[1][3]:.6e}); largest quadrature-error estimate {maxerr:.1e}; violations {len(fails)}")
    # W2: antipodal value tanh(beta/2) at h = e, h' = -e (unit field)
    anti = []
    for beta in (0.05, 0.2886, 1.0, 2.0, 5.0):
        e = np.array([0.0, 0.0, 1.0])
        v = tv(beta, e, -e, G_FINE)
        vc = tv(beta, e, -e, G_COARSE)
        anti.append((beta, v, math.tanh(beta / 2), abs(v - math.tanh(beta / 2)), abs(v - vc)))
    anti_bad = [a for a in anti if a[3] > 50 * a[4] + 1e-9]          # the |p - q| kink sits on the equator: use the rule's own error
    print("[W2] TV(P_e, P_-e) vs tanh(beta/2): " + "; ".join(f"beta={b}: {v:.10f} vs {t:.10f} (quadrature error estimate {e_:.1e})" for b, v, t, _, e_ in anti))
    # W1(ii): coefficient ratios, exactly, n <= 400
    bad_ratio = []
    for m in range(2, 401):
        lhs = Fr(3, 2) * Fr(2 ** (2 * m), math.factorial(2 * m))          # 3 sinh^2 x - 3x^2 coefficient of x^{2m}
        rhs = Fr(1, 2) * Fr(2 ** (2 * m - 2), math.factorial(2 * m - 2))  # x^2 sinh^2 x coefficient
        if lhs / rhs != Fr(6, m * (2 * m - 1)) or lhs > rhs:
            bad_ratio.append(("L'", m))
    for m in range(1, 401):
        lhs = Fr(2 * m, math.factorial(2 * m + 1))
        rhs = Fr(1, 3 * math.factorial(2 * m - 1))
        if lhs / rhs != Fr(3, 2 * m + 1) or lhs > rhs:
            bad_ratio.append(("L/x", m))
    print(f"[W1ii] coefficient ratios 6/(n(2n-1)) (n = 2..400) and 3/(2n+1) (n = 1..400) exact and at most 1: {not bad_ratio} ({len(bad_ratio)} exceptions)")
    print(f"[time] {time.time() - t0:.0f}s")
    if fails:
        print(f"HIT: W1 violated at {len(fails)} pairs, e.g. beta = {fails[0][0]}, TV {fails[0][3]:.6e} > bound {fails[0][4]:.6e}")
    if anti_bad:
        print(f"HIT: W2 antipodal value differs from tanh(beta/2): {anti_bad}")
    if bad_ratio:
        print(f"HIT: W1(ii) coefficient ratio exceptions: {bad_ratio[:5]}")
    print(f"SUMMARY: W1 at {n} pairs (finite field changes, beta |h| up to 12): max TV/(beta|h - h'|) = {worst[0]:.4f} <= 1/(2 sqrt3) = {c:.4f}, "
          f"{len(fails)} violations; W2's tanh(beta/2) reproduced at 5 couplings (max deviation {max(a[3] for a in anti):.1e}); W1(ii) ratios exact to n = 400; "
          f"falsifier {'FIRES' if (fails or anti_bad or bad_ratio) else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
