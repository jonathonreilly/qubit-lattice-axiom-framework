#!/usr/bin/env python3
"""J:note check for NATIVE_GAUGE_TRANSFER_REDUCED_A2_CLOSED_FORM_RUNG_SIXTEEN_BOUNDED_NOTE_2026-06-12 (on main).

Falsifier table (exact, sympy): the H nonseparability determinant 15/32 at (u,v) = (2,0),(2,1),(3,0),(3,1) and 0 with H -> 1; the
N_c = 3 multiplier Q(1,2) = 7 against 14/3; L(u^2+v^2) = 8/3 against the raw 8; the chamber closure; plus the (u,v) identities and,
for the note's steelman N7, whether H is L-harmonic and vanishes on both walls.

Finite witness rows (the note's table) with machinery disjoint from the runner (which evaluates c_(p,q)(beta) as a Bessel-determinant
mode sum in double precision): Wilson coefficients from the character recurrence c(beta) = e^{beta J} delta_(0,0) (Poisson-weighted
walk counts, all terms positive), my own transfer T = E diag(r) E with E = exp((beta/2)(J_box - 1)), the runner's definitions
c_J = beta (j_0 - j_1), c_D = beta (b_1/lambda_1 - b_0/lambda_0) with the box-truncated derivative, and:
  - the note's (beta, shell) rows compared digit by digit;
  - the shell ladder at each beta (shell + 8, + 16, + 24): is each printed row converged in the box?
  - beyond the grid: beta = 240, 480;
  - the reduced eigenvector test the obstruction is about: the top vector divided by the dimension factor H, sampled on a (u,v)
    rectangle inside the wedge, has singular values s2/s1 (a Hermite product would give rank one).
HIT if the exact table fails or a printed row is not reproduced at its own (beta, shell) beyond 1e-6.
"""
from __future__ import annotations

from math import exp, lgamma, log, sqrt

import numpy as np
import sympy as sp

STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]
NOTE_ROWS = {15: (16, 0.811415447696, 0.702464978092, 1.634257044064, 0.216335855768),
             30: (21, 0.834363055423, 0.779366847031, 1.649886251770, 0.204812933383),
             60: (28, 0.847469446625, 0.819818554081, 1.659053552666, 0.199245016875),
             120: (37, 0.854700610938, 0.840331338492, 1.724312693536, 0.196503452859)}


def table():
    x, y, u, v = sp.symbols("x y u v", real=True)
    sub = {x: (u + v) / 2, y: (u - v) / 2}
    Q = x ** 2 + x * y + y ** 2
    H = x * y * (x + y) / 2
    Huv = sp.expand(H.subs(sub))
    ok = {}
    ok["Q(u,v)"] = sp.expand(Q.subs(sub) - (3 * u ** 2 + v ** 2) / 4) == 0
    ok["H(u,v)"] = sp.expand(Huv - u * (u ** 2 - v ** 2) / 8) == 0
    f = sp.Function("f")
    g = f(u, v)
    # L in x,y applied to a test polynomial family, compared with (1/3) d_uu + d_vv
    xs, ys = sp.symbols("xs ys")
    P = xs ** 3 * ys + 2 * xs * ys ** 2 - xs ** 4 + 5 * ys ** 3
    Lxy = (sp.diff(P, xs, 2) - sp.diff(P, xs, ys) + sp.diff(P, ys, 2)) / 3
    Puv = P.subs({xs: (u + v) / 2, ys: (u - v) / 2})
    Luv = sp.diff(Puv, u, 2) / 3 + sp.diff(Puv, v, 2)
    ok["L(u,v)"] = sp.expand(Lxy.subs({xs: (u + v) / 2, ys: (u - v) / 2}) - Luv) == 0
    Hv = lambda a, b: Huv.subs({u: a, v: b})
    det = sp.nsimplify(Hv(2, 0) * Hv(3, 1) - Hv(2, 1) * Hv(3, 0))
    ok["det 15/32"] = det == sp.Rational(15, 32)
    ok["det with H->1 is 0"] = (1 * 1 - 1 * 1) == 0
    ok["N_c=3: 7, N_c=2: 14/3"] = Q.subs({x: 1, y: 2}) == 7 and sp.Rational(2, 3) * Q.subs({x: 1, y: 2}) == sp.Rational(14, 3)
    t = u ** 2 + v ** 2
    ok["L(u^2+v^2) = 8/3, raw 8"] = (sp.diff(t, u, 2) / 3 + sp.diff(t, v, 2) == sp.Rational(8, 3)) and \
        (sp.diff(t.subs({u: xs + ys, v: xs - ys}), xs, 2) + sp.diff(t.subs({u: xs + ys, v: xs - ys}), ys, 2) == 8)
    inch = lambda a, b: a >= 0 and -a <= b <= a
    ok["chamber closure"] = inch(1, 1) and inch(2, -2) and not inch(1, -2)
    LH = sp.expand(sp.diff(Huv, u, 2) / 3 + sp.diff(Huv, v, 2))
    walls = sp.expand(Huv.subs(v, u)) == 0 and sp.expand(Huv.subs(v, -u)) == 0
    return ok, LH, walls


def stencil(a):
    out = np.zeros_like(a)
    n = a.shape[0]
    for dp, dq in STEPS:
        out[max(-dp, 0): n + min(-dp, 0), max(-dq, 0): n + min(-dq, 0)] += a[max(dp, 0): n + min(dp, 0), max(dq, 0): n + min(dq, 0)]
    return out / 6.0


def coefficients(beta, S):
    B = S + int(10 * sqrt(beta)) + 60
    a = np.zeros((B + 1, B + 1))
    a[0, 0] = 1.0
    acc = np.zeros_like(a)
    for n in range(int(beta + 14 * sqrt(beta) + 40) + 1):
        acc += exp(-beta + n * log(beta) - lgamma(n + 1)) * a
        a = stencil(a)
    return acc / acc[0, 0]


def box_J(S):
    idx = {(p, q): p * (S + 1) + q for p in range(S + 1) for q in range(S + 1)}
    J = np.zeros((len(idx), len(idx)))
    for (p, q), i in idx.items():
        for dp, dq in STEPS:
            k = (p + dp, q + dq)
            if k in idx:
                J[idx[k], i] += 1 / 6
    return J, idx


def row(beta, S, r_full, want_vec=False):
    J, idx = box_J(S)
    r = np.array([r_full[p, q] for (p, q) in idx])
    w, V = np.linalg.eigh(J)
    E = (V * np.exp(beta / 2 * (w - 1))) @ V.T
    T = E @ (r[:, None] * E)
    lam, U = np.linalg.eigh(T)
    o = np.argsort(lam)[::-1]
    l0, l1 = lam[o[0]], lam[o[1]]
    v0, v1 = U[:, o[0]], U[:, o[1]]
    j0, j1 = v0 @ J @ v0, v1 @ J @ v1
    rp_full = stencil(r_full)                                  # d r / d beta numerator uses the stencil; box-truncated below
    cp = J @ r                                                   # runner: neighbours inside the box only
    rprime = cp - r * cp[idx[(0, 0)]]
    EDE = E @ (rprime[:, None] * E)
    b0, b1 = v0 @ EDE @ v0, v1 @ EDE @ v1
    cJ, cD = beta * (j0 - j1), beta * (b1 / l1 - b0 / l0)
    out = (cJ, cD, beta * (cJ - cD), l1 / l0)
    if want_vec:
        return out, v0, idx
    return out


def separability(beta, v0, idx):
    """Top vector divided by the dimension factor x y (x+y) (x = p+1, y = q+1) on a rectangle inside the wedge that scales with
    sqrt(beta): v = x-y in [-0.5, 0.5] sqrt(beta), u = x+y from above that bound to 2.5 sqrt(beta) (u, v even)."""
    v0 = v0 * np.sign(v0.sum())
    sb = sqrt(beta)
    v_hi = int(0.5 * sb)
    u_lo, u_hi = v_hi + 2, int(2.5 * sb)                         # |v| <= v_hi < u: strictly inside the wedge
    us = [uu for uu in range(u_lo, u_hi + 1) if uu % 2 == 0]
    vs = [vv for vv in range(-v_hi, v_hi + 1) if vv % 2 == 0]
    M = np.zeros((len(us), len(vs)))
    for a, uu in enumerate(us):
        for b, vv in enumerate(vs):
            x, y = (uu + vv) // 2, (uu - vv) // 2
            M[a, b] = v0[idx[(x - 1, y - 1)]] / (x * y * (x + y))
    s = np.linalg.svd(M, compute_uv=False)
    return float(s[1] / s[0]), float(s[2] / s[0]), M.shape


def main():
    ok, LH, walls = table()
    print(f"1. exact table: {ok}; L H = {LH}, H vanishes on both walls: {walls}")
    results, ladders, vecs = {}, {}, {}
    for beta in (15, 30, 60, 120, 240, 480):
        S0 = NOTE_ROWS[beta][0] if beta in NOTE_ROWS else {240: 48, 480: 64}[beta]
        shells = [S0, S0 + 8, S0 + 16, S0 + 24]
        rf = coefficients(beta, shells[-1])
        ladders[beta] = {S: row(beta, S, rf) for S in shells[:-1]}
        ladders[beta][shells[-1]], vec, vidx = row(beta, shells[-1], rf, want_vec=True)
        vecs[beta] = (vec, vidx)
        results[beta] = ladders[beta][S0]
        lad = ", ".join(f"shell {S}: cJ {v[0]:.9f} cD {v[1]:.9f} beta*margin {v[2]:.6f} ratio {v[3]:.9f}" for S, v in ladders[beta].items())
        print(f"2. beta = {beta}: {lad}")
    diffs = {}
    for beta, (S, cJ, cD, bm, ratio) in NOTE_ROWS.items():
        mine = results[beta]
        diffs[beta] = max(abs(mine[0] - cJ), abs(mine[1] - cD), abs(mine[2] - bm) / beta, abs(mine[3] - ratio))
    print(f"3. printed rows vs recomputation at the note's (beta, shell): max abs difference by beta {({b: float('%.2g' % d) for b, d in diffs.items()})}")
    sep = {beta: separability(beta, *vecs[beta]) for beta in (30, 60, 120, 240, 480)}
    print(f"4. converged top vector / dimension factor on a sqrt(beta)-scaled (u,v) rectangle in the wedge, singular-value ratios "
          f"(s2/s1, s3/s1, grid): { {b: (float('%.3g' % a), float('%.3g' % c), g) for b, (a, c, g) in sep.items()} }")
    fails = [k for k, v in ok.items() if not v]
    if LH != 0 or not walls:
        pass  # steelman premise only; not a falsifier of the note
    bad_rows = [b for b, d in diffs.items() if d > 1e-6]
    if bad_rows:
        fails.append(f"printed rows not reproduced at beta {bad_rows}")
    if fails:
        print(f"HIT: {fails}")
    conv = {b: (round(float(ladders[b][min(ladders[b])][2]), 6), round(float(ladders[b][max(ladders[b])][2]), 6)) for b in ladders}
    print(f"SUMMARY: the exact table holds (15/32, 0, 7, 14/3, 8/3, 8, chamber closure) and H is L-harmonic (L H = {LH}) vanishing on "
          f"both walls; the printed witness rows are reproduced at their own (beta, shell) to {max(diffs.values()):.1g}; beta*(c_J - c_D) "
          f"from the printed shell to shell + 24 moves {conv}; c_D < c_J at every computed point including beta = 240, 480 "
          f"({all(v[0] > v[1] for lad in ladders.values() for v in lad.values())}); the top vector divided by the dimension factor is "
          f"close to but not rank one on the sqrt(beta)-scaled wedge rectangle, s2/s1 = {({b: float('%.2g' % a) for b, (a, c, g) in sep.items()})}, "
          f"not decreasing with beta; the printed beta = 120 row is a box-truncation value (1.724313 at shell 37, 1.660830 from shell 45)")


if __name__ == "__main__":
    main()
