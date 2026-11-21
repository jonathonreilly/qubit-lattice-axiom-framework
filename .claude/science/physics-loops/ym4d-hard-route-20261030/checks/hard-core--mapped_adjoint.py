#!/usr/bin/env python3
"""The residual contour current of Q^o at a background. Consumer: Text 5.5, "the composite adjoint", and through it (R3), (SB) at order 1, Theorem F's hypothesis at the actual lift.

Written before running. Text 5.5 counts: || Q^{o*}(U) lambda - (positive path part with unitary transports) ||_{L^2} is at most C L^2 ||F||_{L^4} |lambda|, geometric in the level, with the top level dominating, so that T_2 = C a_*/L^2 absorbs L^2 exactly. And a check at a smooth field gave order lambda a L at the top level. This is a count. Here it is measured.

Field. d = 2, charged components, constant flux, level-1 adjoint flux a' = 2 pi m/nc^2. Q^o := Q - D' Phi as in `hard-core--mapped_sharp.py`. Path part: P_U (y, mu) := avg over x in B(y) of the sum along the line from x, with the transport of path_x as coefficient and the overall factor e^{i A} of the parent's reference, that is, the legs of the line only in eps_x, with the coefficient they have in the first-order expansion at zero relative phase. Residual: Res := Q^o - P_U. At a' = 0 it vanishes exactly.

Norm. In d = 2 the operator norm from L^2 with density normalisation to l^2 of coarse bonds is the plain ||Res||_{2 -> 2} on fine bonds in potential normalisation, since eta^{1 - d/2} = 1.

PRE-STATED criteria.
 P0. ||Res|| <= 1e-12 at a' = 0, L = 3, 5, 7, 9, 11.
 P1. For fixed m, nc = 6: op(L, a') / (L^2 a') at L = 5, 7, 9, 11 is at most 1.5 times its value at L = 3. This is the count that is consumed: failure means L^2 T_2 does not absorb the residual, and a_* would have to fall further in L, which would be allowed only if the coefficient stays polynomial, and I would report the power.
 P2. Linearity: op(L, 2 a')/op(L, a') in [1.5, 2.5], at a' = 0.1745 and L = 3, 5, 7.
 P3. Reported, no criterion: the exponent p in op ~ L^p a', a least-squares fit over L = 3 .. 11. The smooth-field estimate predicts p = 1.
 P4. Two levels, L = 3, fine torus 36: with Res2 := Qo1 Qo0 - P1 P0, op(Res2) is at most 2 op(Res1 at level 1), where Res1 := Qo1 - P1 on the level-1 lattice at the same level-2 flux a'. This is the count that the top level dominates. a' = 0.3927 m, m = 1, 2.
FAIL if P0, P1, P2 or P4 fails.

Limits. Constant flux only, so ||F||_{L^4} = a' and a pointwise bound holds, and the concentration near nested block centres for a field with only L^4 control is not tested. One or two levels. RSS guard 2 GB.
"""
import importlib.util
import os
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sharp_lam", os.path.join(HERE, "hard-core--mapped_sharp_lam.py"))
lam = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lam)
sh = lam.sh
tp = sh.tp
RealBg = tp.Bg


def path_part(g, Dc):
    """P_U: the line legs of path_x, with their coefficients, averaged over x, and the factor e^{i A} e^{-i (v_x)} removing the relative phase of the path."""
    N, L, nc, h = g.N, g.L, g.nc, g.h
    nb = 2 * N * N
    P = np.zeros((2 * nc * nc, nb), dtype=complex)
    for i in range(nc):
        for j in range(nc):
            y0 = (h + L * i, h + L * j)
            for mu in range(2):
                c = i * nc + j + mu * nc * nc
                data = {}
                for r0 in range(-h, h + 1):
                    for r1 in range(-h, h + 1):
                        x = (y0[0] + r0, y0[1] + r1)
                        data[(r0, r1)] = lam.legs(g, y0, x, mu)
                om0 = data[(0, 0)][1]
                vs = {k: np.angle(v[1] / om0) for k, v in data.items()}
                A = float(np.mean(list(vs.values())))
                row = np.zeros(nb, dtype=complex)
                for (r0, r1), (lg, om) in data.items():
                    x = (y0[0] + r0, y0[1] + r1)
                    # The legs of path_x: contour y -> x, line, contour back. The line's legs are identified by position in the list.
                    nc1 = abs(r0) + abs(r1)
                    line = lg[nc1 : nc1 + L]
                    # A unitary factor so that the parent's fluctuation is measured in the parent's frame.
                    fac = np.exp(1j * A) * np.exp(-1j * vs[(r0, r1)])
                    for b, co in line:
                        row[b] += fac * co / L**2
                P[c] = row
    return P


def residual(L, nc, m):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = sh.build_sharp(L, nc, m)
    P = path_part(g, Dc)
    Res = Qo - P
    guard()
    return np.linalg.norm(Res, 2), np.linalg.norm(Qo, 2), g, Qo, P, Dc


def two_levels(m):
    op0, qn, g0, Qo0, P0, Dc0 = residual(3, 12, m)
    g1 = RealBg(3, 4, 0)
    u1 = np.ones((2, 12, 12), dtype=complex)
    for i in range(12):
        for j in range(12):
            ci = i * 12 + j
            for mu in range(2):
                ni, nj = (i + (mu == 0)) % 12, (j + (mu == 1)) % 12
                u1[mu, i, j] = Dc0[ci + mu * 144, ni * 12 + nj]
    g1.u = u1
    tp.Bg = lambda L_, nc_, m_: g1
    try:
        _, D1, d1, Q1, Qo1, Dc1, ev1, r1, Phi1, Pr1, c1 = sh.build_sharp(3, 4, 0)
    finally:
        tp.Bg = RealBg
    P1 = path_part(g1, Dc1)
    res1 = np.linalg.norm(Qo1 - P1, 2)
    res2 = np.linalg.norm(Qo1 @ Qo0 - P1 @ P0, 2)
    guard()
    return op0, res1, res2


def main():
    ok = True
    print("P0, P1", flush=True)
    Ls = (3, 5, 7, 9, 11)
    nc = 6
    for L in Ls:
        op, qn, *_ = residual(L, nc, 0)
        good = op <= 1e-12
        ok = ok and good
        print(f" P0 L={L}: ||Res||={op:.1e} ||Q^o||={qn:.3f}: {good} rss={rss_gb():.2f}GB", flush=True)
    for m in (1, 2):
        ap = 2 * np.pi * m / nc**2
        vals = []
        for L in Ls:
            op, qn, *_ = residual(L, nc, m)
            vals.append(op)
            print(f" L={L} a'={ap:.4f}: ||Res||={op:.5f} ||Res||/(L^2 a')={op / (L**2 * ap):.5f} ||Res||/(L a')={op / (L * ap):.5f} ||Res||/a'={op / ap:.5f} rss={rss_gb():.2f}GB", flush=True)
        base = vals[0] / (Ls[0] ** 2 * ap)
        for L, v in zip(Ls, vals):
            good = v / (L**2 * ap) <= 1.5 * base
            ok = ok and good
            if not good:
                print(f"  P1 fails at L={L}", flush=True)
        p = np.polyfit(np.log(Ls), np.log(vals), 1)[0]
        print(f" P3 m={m}: exponent p = {p:.3f}", flush=True)
    print("P2", flush=True)
    for L in (3, 5, 7):
        a1 = residual(L, nc, 1)[0]
        a2 = residual(L, nc, 2)[0]
        good = 1.5 <= a2 / a1 <= 2.5
        ok = ok and good
        print(f" P2 L={L}: ratio {a2 / a1:.3f}: {good}", flush=True)
    print("P4", flush=True)
    for m in (1, 2):
        op0, res1, res2 = two_levels(m)
        good = res2 <= 2 * res1
        ok = ok and good
        print(f" P4 m={m} a'={0.3927 * m:.3f}: level 0 residual {op0:.5f}, level 1 residual {res1:.5f}, composite {res2:.5f}: {good} rss={rss_gb():.2f}GB", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
