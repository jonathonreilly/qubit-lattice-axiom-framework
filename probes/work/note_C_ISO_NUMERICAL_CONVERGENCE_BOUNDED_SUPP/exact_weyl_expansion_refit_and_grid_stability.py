#!/usr/bin/env python3
"""Probe: C_ISO_NUMERICAL_CONVERGENCE_BOUNDED_SUPPORT_NOTE_2026-05-10_numconv.

Machinery disjoint from the runner (windowed midpoint Weyl quadrature with
ngauss, numpy lstsq-free weighted fit):

 E  the SU(3) Wilson single-plaquette expansion EXACTLY: with
    Z(beta) = E_Haar[exp((beta/3) Re Tr U)] and P_W = 1 - d log Z / d beta,
    the Weyl-torus integral expanded in 1/beta by Gaussian moments (sympy):
    beta^4 e^-beta Z = C (1 + a_1/beta + a_2/beta^2 + ...), hence
    P_W = 4/beta + c_2/beta^2 + c_3/beta^3 with c_2 = a_1 and c_3 = 2 a_2 - a_1^2;
    the note's "c_2 = -1" and the machinery's fitted c_3 = -4.328 +- 0.05.
 Q  the falsifier "the SU(3) Weyl quadrature fails to stabilize under grid
    refinement at the beta values used": P_W by a full-torus periodic trapezoid
    (spectrally convergent) at beta_W = 24, 48, 96 (xi = 4, 8, 16) and the
    self-test betas 12..3000, refined N = 256..4096; the runner's windowed
    midpoint scheme (window min(pi, 10 sigma), 4 ngauss points) re-implemented
    and refined over ngauss = 50..800 against it; (P_W beta - 4) beta at 3000.
 F  the weighted volume refit P(L) = P_inf + a/L^2 + b/L^4 over L = 3,4,6,8,10
    with weights 1/sigma^2, solved exactly (Fractions): P_inf and its error
    (note 0.44044 +- 0.00026); the corrected value P_inf P_HK/P_W at xi = 4
    (note 0.41092 +- 0.00026) with the propagated error; the xi = 4, 8, 16
    corrected spread (note about 35%).

Prints SUMMARY: lines; HIT: only when a falsifier of the note fires.
"""
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ------------------------------------------------------------------------------------------ E
def run_E():
    print("=" * 78)
    print("E  exact 1/beta expansion of the Wilson single plaquette")
    w1, w2, e = sp.symbols("w1 w2 epsilon", real=True)
    # u = A w with u1^2 + u1 u2 + u2^2 = w1^2 + w2^2 ; |det A| = 2/sqrt3
    u1 = w1 - w2 / sp.sqrt(3)
    u2 = 2 * w2 / sp.sqrt(3)
    u3 = -u1 - u2
    us = [u1, u2, u3]
    # theta = u sqrt(eps); expansions to eps^2 beyond the Gaussian
    #   4 sin^2(x/2) = x^2 (1 - x^2/12 + x^4/360 - ...)
    #   (beta/3)(cos theta - 1) = -u^2/6 + eps u^4/72 - eps^2 u^6/2160 + ...
    V = 1
    for j in range(3):
        for k in range(j + 1, 3):
            d = us[j] - us[k]
            V *= d ** 2 * (1 - e * d ** 2 / 12 + e ** 2 * d ** 4 / 360)
    Xp = sum(e * u ** 4 / 72 - e ** 2 * u ** 6 / 2160 for u in us)
    corr = sp.expand(sp.series(sp.exp(Xp), e, 0, 3).removeO())
    integrand = sp.expand(sp.expand(V) * corr)
    # keep orders e^0..e^2
    poly = sp.Poly(integrand, e)
    coeffs = {k[0]: c for k, c in zip(poly.monoms(), poly.coeffs()) if k[0] <= 2}

    def gauss(expr):
        """int int expr(w) exp(-(w1^2 + w2^2)/3) dw1 dw2 for a polynomial expr"""
        P = sp.Poly(sp.expand(expr), w1, w2)
        tot = 0
        for (a, b), c in zip(P.monoms(), P.coeffs()):
            if a % 2 or b % 2:
                continue
            # int x^(2n) exp(-x^2/3) dx = Gamma(n + 1/2) 3^(n + 1/2)
            ma = sp.gamma(sp.Rational(a + 1, 2)) * sp.Integer(3) ** sp.Rational(a + 1, 2)
            mb = sp.gamma(sp.Rational(b + 1, 2)) * sp.Integer(3) ** sp.Rational(b + 1, 2)
            tot += c * ma * mb
        return sp.simplify(tot)
    G0 = gauss(coeffs[0])
    C = sp.simplify(G0 * 2 / sp.sqrt(3) / (24 * sp.pi ** 2))
    a1 = sp.simplify(gauss(coeffs[1]) / G0)
    a2 = sp.simplify(gauss(coeffs[2]) / G0)
    c2 = a1
    c3 = sp.simplify(2 * a2 - a1 ** 2)
    print(f"  C = {C} = {float(C):.10f}; a_1 = {a1}; a_2 = {a2}; c_2 = a_1 = {c2}; c_3 = 2 a_2 - a_1^2 = {c3} = {float(c3):.6f}")
    print(f"  machinery's fitted c_3 = -4.328 +- 0.05: exact value inside the band: {abs(float(c3) + 4.328) <= 0.05}")
    if c2 != -1:
        hit(f"the exact NLO coefficient c_2 = {c2} is not -1")
    return C, a1, a2, c2, c3


# ------------------------------------------------------------------------------------------ Q
def torus_PW(beta, N, chunk=256):
    """P_W = 1 - <Re Tr U>/3 by the full-torus periodic trapezoid rule"""
    t = 2 * np.pi * np.arange(N) / N
    num = den = 0.0
    for s0 in range(0, N, chunk):
        t1 = t[s0:s0 + chunk][:, None]
        t2 = t[None, :]
        t3 = -(t1 + t2)
        vd = (4 * np.sin((t1 - t2) / 2) ** 2) * (4 * np.sin((t1 - t3) / 2) ** 2) * (4 * np.sin((t2 - t3) / 2) ** 2)
        f = np.cos(t1) + np.cos(t2) + np.cos(t3)
        wgt = vd * np.exp(beta / 3 * (f - 3))
        num += float(np.sum(wgt * f))
        den += float(np.sum(wgt))
    return 1 - num / den / 3


def window_PW(beta, ngauss):
    """the runner's scheme re-implemented: midpoints on [-rmax, rmax]^2, rmax = min(pi, 10 sigma), n = 4 ngauss"""
    sigma = math.sqrt(3.0 / beta)
    rmax = min(math.pi, 10.0 * sigma)
    n = 4 * ngauss
    g = np.linspace(-rmax, rmax, n, endpoint=False) + rmax / n
    T1, T2 = np.meshgrid(g, g, indexing="ij")
    T3 = -T1 - T2
    vd = 64 * np.sin((T1 - T2) / 2) ** 2 * np.sin((T2 - T3) / 2) ** 2 * np.sin((T3 - T1) / 2) ** 2
    f = np.cos(T1) + np.cos(T2) + np.cos(T3)
    wgt = vd * np.exp(beta / 3 * (f - 3))
    return 1 - float((wgt * f).sum() / wgt.sum()) / 3


def run_Q(c3_exact):
    print("=" * 78)
    print("Q  grid refinement of the Weyl quadrature")
    rows = {}
    worst_torus = 0.0
    worst_window = 0.0
    for beta in (12, 24, 48, 96, 192, 384, 768, 1500, 3000):
        vals = [torus_PW(beta, N) for N in (256, 512, 1024, 2048, 4096)]
        conv = abs(vals[-1] - vals[-2]) / vals[-1]
        wins = [window_PW(beta, ng) for ng in (50, 100, 200, 400, 800)]
        wdev = max(abs(w - vals[-1]) / vals[-1] for w in wins[1:])
        worst_torus = max(worst_torus, conv)
        worst_window = max(worst_window, wdev)
        rows[beta] = (vals[-1], conv, wins, wdev)
    for beta, (pw, conv, wins, wdev) in rows.items():
        print(f"  beta_W={beta:5d}: full torus P_W {pw:.12f} (last refinement change {conv:.1e}); runner-scheme ngauss 100..800 "
              f"max rel dev from it {wdev:.1e}; (P_W beta - 4) beta = {(pw * beta - 4) * beta:+.6f}")
    b = 3000
    nlo = (rows[b][0] * b - 4) * b
    pred = -1 + float(c3_exact) / b
    print(f"  at beta = 3000: (P_W beta - 4) beta = {nlo:+.6f}; exact c_2 + c_3/beta = {pred:+.6f}; relative distance of the "
          f"quadrature value from c_2 = -1: {abs(nlo + 1):.2%}")
    if worst_torus > 1e-10 or worst_window > 1e-9:
        hit(f"the Weyl quadrature does not stabilize under refinement (torus {worst_torus:.1e}, runner scheme {worst_window:.1e})")
    return rows, nlo, pred, worst_torus, worst_window


# ------------------------------------------------------------------------------------------ F
def run_F(rows):
    print("=" * 78)
    print("F  the weighted volume refit and the corrected xi = 4 value")
    data = [(3, Fr("0.44545"), Fr("0.00034")), (4, Fr("0.44329"), Fr("0.00016")), (6, Fr("0.44207"), Fr("0.00022")),
            (8, Fr("0.44099"), Fr("0.00026")), (10, Fr("0.44090"), Fr("0.00023"))]
    # normal equations X^T W X beta = X^T W y, exact
    X = [[Fr(1), Fr(1, L * L), Fr(1, L ** 4)] for L, _, _ in data]
    Wt = [1 / s ** 2 for _, _, s in data]
    y = [v for _, v, _ in data]
    A = [[sum(Wt[i] * X[i][r] * X[i][c] for i in range(5)) for c in range(3)] for r in range(3)]
    bvec = [sum(Wt[i] * X[i][r] * y[i] for i in range(5)) for r in range(3)]
    # invert A exactly
    M = [row[:] + [Fr(int(r == c)) for c in range(3)] for r, row in enumerate(A)]
    for c in range(3):
        p = next(r for r in range(c, 3) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        piv = M[c][c]
        M[c] = [v / piv for v in M[c]]
        for r in range(3):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    Ainv = [row[3:] for row in M]
    coef = [sum(Ainv[r][c] * bvec[c] for c in range(3)) for r in range(3)]
    Pinf = coef[0]
    err = math.sqrt(float(Ainv[0][0]))
    chi2 = sum(Wt[i] * (y[i] - sum(X[i][c] * coef[c] for c in range(3))) ** 2 for i in range(5))
    xi = 4
    st = 1 / (2 * xi)
    PHK = 1 - math.exp(-(4 / 3) * st)
    PW = rows[6 * xi][0]
    fac = PHK / PW
    Pc = float(Pinf) * fac
    print(f"  P_inf = {float(Pinf):.6f} +- {err:.6f} (note 0.44044 +- 0.00026); a = {float(coef[1]):+.5f}, b = {float(coef[2]):+.5f}; "
          f"chi^2 = {float(chi2):.3f} for 2 dof")
    print(f"  xi = 4: s_t = 1/8, beta_W = 24, P_HK = {PHK:.10f}, P_W = {PW:.10f}, factor {fac:.8f}; corrected {Pc:.6f} "
          f"(note 0.41092); propagated error {err * fac:.6f} (note +-0.00026)")
    lat = {4: 0.44329, 8: 0.40949, 16: 0.28350}
    corr = {}
    for x, P in lat.items():
        s = 1 / (2 * x)
        corr[x] = P * (1 - math.exp(-(4 / 3) * s)) / rows[6 * x][0]
    spread = (max(corr.values()) - min(corr.values())) / max(corr.values())
    print(f"  corrected 4^3 x 16 values: " + ", ".join(f"xi={x}: {v:.5f}" for x, v in corr.items()) +
          f"; spread (max - min)/max = {spread:.1%} (note about 35%)")
    ok = abs(float(Pinf) - 0.44044) <= 5e-6 and abs(err - 0.00026) <= 5e-6 and abs(Pc - 0.41092) <= 5e-6
    if not ok:
        hit(f"the refit or the corrected value differs from the note (P_inf {float(Pinf):.6f} +- {err:.6f}, corrected {Pc:.6f})")
    return float(Pinf), err, float(chi2), fac, Pc, corr, spread


def main():
    t0 = time.time()
    C, a1, a2, c2, c3 = run_E()
    summary(f"E exact: beta^4 e^-beta Z = C (1 + a_1/beta + a_2/beta^2), C = {C}, a_1 = {a1}, a_2 = {a2}; P_W = 4/beta + c_2/beta^2 "
            f"+ c_3/beta^3 with c_2 = {c2} (the note's -1 exactly) and c_3 = {c3} = {float(c3):.6f} (the machinery's fitted "
            f"-4.328 +- 0.05)")
    rows, nlo, pred, wt, ww = run_Q(c3)
    summary(f"Q the full-torus trapezoid stabilizes to {wt:.0e} relative and the runner's windowed scheme agrees with it to "
            f"{ww:.0e} at every beta used (12..3000, incl. 24/48/96); (P_W beta - 4) beta = {nlo:+.5f} at 3000 = c_2 + c_3/beta "
            f"({pred:+.5f}), i.e. {abs(nlo + 1):.2%} from -1")
    Pinf, err, chi2, fac, Pc, corr, spread = run_F(rows)
    summary(f"F exact weighted refit P_inf = {Pinf:.6f} +- {err:.6f} (chi^2 {chi2:.2f}/2); corrected xi = 4 value {Pc:.6f} with "
            f"propagated error {err * fac:.6f} (factor {fac:.5f}; the note quotes the unscaled +-0.00026); corrected xi = 4, 8, 16 "
            f"values {', '.join(f'{v:.5f}' for v in corr.values())}, spread {spread:.1%}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
