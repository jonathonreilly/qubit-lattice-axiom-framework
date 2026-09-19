#!/usr/bin/env python3
"""Probe: NATIVE_GAUGE_TRANSFER_C00_LOWER_BOUND_RUNG_TWELVE_BOUNDED_NOTE_2026-06-12.

Machinery disjoint from the runner (Bessel-determinant machinery plus a Haar
Monte-Carlo at beta = 6, 9):

 I  the identity c_(0,0)(beta) = E_Haar[exp((beta/3) Re Tr U)] tested as EXACT:
    the right side by the Weyl integration formula on the maximal torus,
    (1/(3! (2 pi)^2)) int |Delta|^2 exp((beta/3)(cos t1 + cos t2 + cos(t1+t2))),
    evaluated by the periodic trapezoid rule (spectrally accurate for this
    analytic periodic integrand; grid refined until stable); the left side by
    the note's own definition c_(0,0) = sum_n det[I_{n+i-j}(beta/3)] implemented
    independently in mpmath at 40 digits; at beta = 6, 9, 24, 48, 96, 192, 384.
 T  the table beta^4 e^-beta c_(0,0) at 48, 96, 192, 384 (note 14.564, 14.728,
    14.808, 14.847) and beyond (768, 1536, 3072); the limit C EXACTLY from the
    Gaussian limit of the Weyl integral (sympy): C = 27 sqrt3/pi = 14.8859,
    against the note's approximate witness ~14.85 (reported, not a falsifier);
    the slope of beta^(3/2) e^-beta c_(0,0) (note -2.49 ~ -5/2); the wrong-power
    falsifier (beta^3 scaling drifts).
 B  the small-ball constant c_8 = lim P(eps)/eps^4 EXACTLY (sympy, polar
    integral of the torus Vandermonde over the Gaussian ellipse), C_lower =
    (c_8/2) e^-4 12^4; P(12/beta)/(c_8 (12/beta)^4) on the torus grid, i.e. where
    the note's 1/2 safety factor holds (its beta_0, left unspecified in the note);
    c_(0,0) >= C_lower e^beta beta^-4 and the grid witness c_(0,0) >= 8 e^beta beta^-4;
    the strict nondegenerate maximum of Re Tr U at U = I on the torus.

Prints SUMMARY: lines; HIT: only when a stated fact of the note fails.
"""
import math
import sys
import time

import numpy as np
import mpmath as mp
import sympy as sp

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


def weyl_scaled(beta, N, chunk=256):
    """e^-beta E_Haar[exp((beta/3) Re Tr U)] by the periodic trapezoid rule on an N x N torus grid (row chunks)"""
    t = 2 * np.pi * np.arange(N) / N
    total = 0.0
    for s0 in range(0, N, chunk):
        t1 = t[s0:s0 + chunk][:, None]
        t2 = t[None, :]
        t3 = -(t1 + t2)
        # |e^{ia} - e^{ib}|^2 = 4 sin^2((a - b)/2)
        vd = (4 * np.sin((t1 - t2) / 2) ** 2) * (4 * np.sin((t1 - t3) / 2) ** 2) * (4 * np.sin((t2 - t3) / 2) ** 2)
        ex = np.exp(beta / 3 * (np.cos(t1) + np.cos(t2) + np.cos(t3)) - beta)
        total += float(np.sum(vd * ex))
    return total / (N * N) / 6.0


def weyl_converged(beta):
    N = 256
    prev = weyl_scaled(beta, N)
    while True:
        N *= 2
        cur = weyl_scaled(beta, N)
        if (abs(cur - prev) <= 1e-14 * abs(cur) and N >= 1024) or N >= 4096:
            return cur, N
        prev = cur


def bessel_c00_scaled(beta):
    """e^-beta sum_n det[I_{n+i-j}(beta/3)]_{i,j=1..3}, 40 digits"""
    with mp.workdps(40):
        x = mp.mpf(beta) / 3
        total = mp.mpf(0)
        n = 0
        while True:
            terms = []
            for nn in ((n,) if n == 0 else (n, -n)):
                M = mp.matrix(3, 3)
                for i in range(3):
                    for j in range(3):
                        M[i, j] = mp.besseli(nn + i - j, x)
                terms.append(mp.det(M))
            s = mp.fsum(terms)
            total += s
            if n > 5 and abs(s) < mp.mpf(10) ** -35 * abs(total):
                break
            n += 1
        return total * mp.e ** (-mp.mpf(beta))


def run_I():
    print("=" * 78)
    print("I  exactness of c_(0,0) = E_Haar[exp((beta/3) Re Tr U)]")
    rows = []
    worst = 0.0
    for beta in (6, 9, 24, 48, 96, 192, 384):
        w, N = weyl_converged(beta)
        b = float(bessel_c00_scaled(beta))
        rel = abs(w - b) / b
        worst = max(worst, rel)
        rows.append((beta, w, b, rel, N))
        print(f"  beta={beta:3d}: Weyl/torus {w:.15e} (N={N}), Bessel determinant {b:.15e}, rel diff {rel:.1e}")
    if worst > 1e-10:
        hit(f"the Bessel-determinant c_(0,0) differs from the Haar average (rel {worst:.1e})")
    return rows, worst


def gaussian_constants():
    u1, u2, r, th = sp.symbols("u1 u2 r theta", real=True)
    u3 = -u1 - u2
    V = (u1 - u2) ** 2 * (u1 - u3) ** 2 * (u2 - u3) ** 2
    # C = lim beta^4 e^-beta c00 = (1/(24 pi^2)) int int V exp(-S/6) du1 du2, S = sum u_j^2 = 2(u1^2 + u1 u2 + u2^2);
    # evaluated below in the same polar coordinates of the quadratic form as c_8
    # c_8 = lim P(eps)/eps^4, P(eps) = (1/(24 pi^2)) area-integral of V over {S/2 <= eps}  (Re Tr U ~ 3 - S/2)
    # S/2 = u1^2 + u1 u2 + u2^2 <= eps: substitute to polar coordinates of the quadratic form
    # u = A w with w in the unit disc scaled by sqrt(eps): A = [[1, -1/sqrt3],[0, 2/sqrt3]] maps w1^2 + w2^2 -> u1^2+u1u2+u2^2
    w1, w2 = r * sp.cos(th), r * sp.sin(th)
    U1 = w1 - w2 / sp.sqrt(3)
    U2 = 2 * w2 / sp.sqrt(3)
    jac = sp.Rational(2, 1) / sp.sqrt(3)
    check_form = sp.simplify(U1 ** 2 + U1 * U2 + U2 ** 2 - r ** 2)
    Vp = sp.simplify(V.subs({u1: U1, u2: U2}))
    ang = sp.integrate(sp.expand(sp.simplify(Vp / r ** 6)), (th, 0, 2 * sp.pi))      # V(A w) = r^6 g(theta)
    area = ang * jac * sp.integrate(r ** 7, (r, 0, 1))                                  # eps = 1: {q <= 1}
    c8 = sp.simplify(area / (24 * sp.pi ** 2))
    gauss = ang * jac * sp.integrate(r ** 7 * sp.exp(-r ** 2 / 3), (r, 0, sp.oo))     # S/6 = q/3 = r^2/3
    C = sp.simplify(gauss / (24 * sp.pi ** 2))
    return C, c8, check_form


def run_T(C_exact):
    print("=" * 78)
    print("T  the scaled table, the limit constant and the power")
    table = {48: 14.564, 96: 14.728, 192: 14.808, 384: 14.847}
    vals = {}
    for beta in (48, 96, 192, 384, 768, 1536, 3072):
        w, N = weyl_converged(beta)
        vals[beta] = w * beta ** 4
    bad = [b for b, t in table.items() if abs(vals[b] - t) > 5e-4]
    Cf = float(C_exact)
    rich = [2 * vals[b2] - vals[b1] for b1, b2 in ((768, 1536), (1536, 3072))]
    betas = sorted(vals)
    slope = [(math.log(vals[b2] / b2 ** 2.5) - math.log(vals[b1] / b1 ** 2.5)) / (math.log(b2) - math.log(b1))
             for b1, b2 in zip(betas, betas[1:])]
    drift3 = [vals[b] / b for b in betas]              # beta^3 e^-beta c00 = (beta^4 e^-beta c00)/beta
    print("  beta^4 e^-beta c00: " + ", ".join(f"{b}: {vals[b]:.6f}" for b in betas))
    print(f"  exact Gaussian limit C = {C_exact} = {Cf:.10f}; Richardson (768,1536) {rich[0]:.6f}, (1536,3072) {rich[1]:.6f}")
    print(f"  local slopes of log(beta^(3/2) e^-beta c00) vs log beta: {', '.join(f'{s:.4f}' for s in slope)} (note -2.49 ~ -5/2)")
    print(f"  wrong power: beta^3 e^-beta c00 = {', '.join(f'{d:.4f}' for d in drift3)} (drifts to 0)")
    if bad:
        hit(f"table entries differ at beta = {bad}")
    mono = all(vals[b2] > vals[b1] for b1, b2 in zip(betas, betas[1:]))
    # the note's claims: monotone upward convergence to a finite positive C, power -4 (the "~14.85" is an approximate
    # witness, reported as a number below, not a falsifier)
    if not (mono and all(v < Cf for v in vals.values()) and abs(rich[1] - Cf) < 2e-3 and abs(slope[-1] + 2.5) < 0.01):
        hit(f"the scaled c00 does not rise monotonically to a finite limit with power -4 (C = {Cf:.6f})")
    print(f"  monotone upward: {mono}; the note's '~14.85' equals its beta = 384 value {vals[384]:.4f}; the limit is "
          f"{Cf:.5f} (difference {Cf - 14.85:+.4f})")
    return vals, Cf, rich, slope, drift3


def run_B(c8_exact, vals):
    print("=" * 78)
    print("B  the small-ball constant, C_lower and the safety factor")
    c8 = float(c8_exact)
    Clow = c8 / 2 * math.exp(-4) * 12 ** 4
    # P(eps) on a fine torus grid for eps = 12/beta
    rows = []
    for beta in (12, 24, 48, 96, 192, 384, 768):
        eps = 12.0 / beta
        N = 4096 if beta <= 96 else 8192
        # restrict to a window around 0 containing the region (radius ~ sqrt(2 eps) with margin)
        rad = min(math.pi, 3 * math.sqrt(2 * eps) + 0.05)
        n = int(N * rad / math.pi) // 2 * 2
        t = np.linspace(-rad, rad, n, endpoint=False) + rad / n
        t1, t2 = np.meshgrid(t, t, indexing="ij")
        t3 = -(t1 + t2)
        f = np.cos(t1) + np.cos(t2) + np.cos(t3)
        z1, z2, z3 = np.exp(1j * t1), np.exp(1j * t2), np.exp(1j * t3)
        vd = np.abs(z1 - z2) ** 2 * np.abs(z1 - z3) ** 2 * np.abs(z2 - z3) ** 2
        dA = (2 * rad / n) ** 2
        P = float(np.sum(vd * (f >= 3 - eps)) * dA / (6 * 4 * math.pi ** 2))
        rows.append((beta, eps, P, P / (c8 * eps ** 4)))
    ok_rows = [(b, r) for b, e, P, r in rows]
    print(f"  c_8 = {c8_exact} = {c8:.8f}; C_lower = (c_8/2) e^-4 12^4 = {Clow:.6f}")
    print("  P(12/beta) / (c_8 (12/beta)^4): " + ", ".join(f"beta={b}: {r:.4f}" for b, r in ok_rows))
    beta0 = next((b for b, r in ok_rows if r >= 0.5 and all(rr >= 0.5 for bb, rr in ok_rows if bb >= b)), None)
    holds = [(b, vals[b] >= Clow) for b in vals]
    witness8 = all(vals[b] >= 8 for b in vals)
    # strict nondegenerate maximum at U = I on the torus
    t = np.linspace(-np.pi, np.pi, 2001)
    t1, t2 = np.meshgrid(t, t, indexing="ij")
    f = np.cos(t1) + np.cos(t2) + np.cos(t1 + t2)
    near = np.hypot(t1, t2) > 0.05
    max_away = float(f[near].max())
    hess = np.array([[-2.0, -1.0], [-1.0, -2.0]])
    hev = np.linalg.eigvalsh(hess)
    print(f"  safety factor 1/2 holds from beta = {beta0} on this grid; c00 >= C_lower e^beta beta^-4 at "
          f"{sum(1 for _, h in holds if h)}/{len(holds)} tabulated beta; c00 >= 8 e^beta beta^-4 on the tabulated grid: {witness8}")
    print(f"  Re Tr U on the torus: max away from 0 (|t| > 0.05) {max_away:.6f} < 3; Hessian at I eigenvalues {hev} (negative "
          f"definite)")
    if Clow <= 0 or not all(h for _, h in holds) or not witness8 or max_away >= 3 or not np.all(hev < 0):
        hit("the lower bound, the grid witness or the strict maximum at U = I fails")
    return c8, Clow, rows, beta0, witness8


def main():
    t0 = time.time()
    rows, worst = run_I()
    summary(f"I c_(0,0) = E_Haar[exp((beta/3) Re Tr U)]: 40-digit Bessel determinant vs Weyl-torus trapezoid agree to "
            f"{worst:.1e} relative at beta = 6, 9, 24, 48, 96, 192, 384 (the identity is exact)")
    C, c8, chk = gaussian_constants()
    vals, Cf, rich, slope, drift3 = run_T(C)
    summary(f"T beta^4 e^-beta c00 = {', '.join(f'{vals[b]:.4f}' for b in sorted(vals))} at beta = {', '.join(str(b) for b in sorted(vals))}; "
            f"exact limit C = {C} = {Cf:.8f} (the note's '~14.85' is its beta = 384 value; the sequence keeps rising to "
            f"{Cf:.4f}); Richardson {rich[1]:.6f}; slopes -> {slope[-1]:.4f} (-5/2); beta^3 scaling "
            f"drifts {drift3[0]:.3f} -> {drift3[-1]:.4f}")
    c8f, Clow, brows, beta0, w8 = run_B(c8, vals)
    summary(f"B c_8 = {c8} = {c8f:.6f}, C_lower = {Clow:.4f} (> 0, far below C = {Cf:.3f}); P(12/beta)/(c_8 (12/beta)^4) = "
            f"{', '.join(f'{r[3]:.3f}' for r in brows)} at beta = {', '.join(str(r[0]) for r in brows)}, so the 1/2 safety factor "
            f"holds from beta = {beta0} on this grid; grid witness 8: {w8}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
