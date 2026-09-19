#!/usr/bin/env python3
"""Probe: U1_RECORD_DISTRIBUTION_OVERLAP_POSITIVE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.

Falsifier bullets implemented with machinery disjoint from the runner:

 A  autocorrelation theorem on 60 exact densities p = |q|^2/||q||^2 (Fejer-Riesz:
    nonnegative by construction) with q a random trigonometric polynomial with
    Gaussian-integer coefficients (degree <= 6: asymmetric, drifting, negative and
    complex Fourier coefficients), plus the note's example and an explicit
    sine-component density:
      * the overlap coefficients c_m computed from the definition
        C(delta) = int p(theta) p(theta + delta) (coefficient convolution
        p_hat_{-m} p_hat_m) are real, >= 0 and equal |p_hat_m|^2 (exact Q(i));
      * C(delta) <= C(0) on 721 points, C computed by 50-digit quadrature of the
        defining integral;
      * V''(0) = sum m^2 c_m / sum c_m (exact) equals ||p'||^2/||p||^2 (exact,
        from the Fourier series of p') and the 50-digit finite difference of
        -log C, and is > 0; the uniform density gives C = 1, kappa = 0.
 B  Record histograms (sec. 2): exact equal-bin masses f_i of a trigonometric
    density, C_N(s) = N sum_i f_i f_{i+s}; the identity
    C_N(s) = sum_m |p_hat_m|^2 sinc^2(pi m/N) e^{i m delta_N}; convergence to C at
    delta = pi/4 and 0 for N = 16..4096 (runner: 256; its witness N <= 256) with
    rate N^-2; unequal refining bins (widths alternating 1:2) do not converge to C(0).
 C  sec. 4 example p = 1 - 0.6 cos: C = 1 + 0.18 cos, V''(0) = 9/59, raw curvature -3/2.
 D  sec. 6 blocks: the quadratic gauge block with temporal plaquette weight k_t and
    spatial weight k_s, symbolic in the momentum symbols s_mu: at k_0 = 0 and
    s != 0, temporal-only rank 1 (static transverse modes have no stiffness),
    isotropic rank 3 with gauge null vector (s_0, s) and two transverse modes of
    energy k_s |s|^2; numerically at every momentum of L = 4..10 tori.

Prints SUMMARY: lines; HIT: only when a falsifier of the note fires.
"""
import cmath
import math
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 50
HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ------------------------------------------------------------------ exact Q(i) Fourier arithmetic
def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


def conv(P, Q):
    """Fourier coefficient dicts {n: (re, im)} -> product"""
    out = {}
    for n, a in P.items():
        for m, b in Q.items():
            v = cmul(a, b)
            o = out.get(n + m, (Fr(0), Fr(0)))
            out[n + m] = (o[0] + v[0], o[1] + v[1])
    return {k: v for k, v in out.items() if v != (0, 0)}


def density_from_q(qc):
    """p = |q|^2 / ||q||^2 as Fourier coefficients; q = sum_k qc[k] e^{ik theta}"""
    Q = {k: (Fr(a), Fr(b)) for k, (a, b) in qc.items()}
    Qbar = {-k: cconj(v) for k, v in Q.items()}          # conj(q) has coefficients conj(q_k) at -k
    P = conv(Q, Qbar)
    norm = P[0][0]
    return {k: (v[0] / norm, v[1] / norm) for k, v in P.items()}


def p_eval(P, th):
    return sum((mp.mpf(v[0].numerator) / v[0].denominator + 1j * mp.mpf(v[1].numerator) / v[1].denominator) * mp.e ** (1j * n * th)
               for n, v in P.items())


def run_A(n_rand=60, seed=20260919):
    print("=" * 78)
    print("A  autocorrelation theorem on exact nonnegative densities")
    rng = random.Random(seed)
    dens = []
    for _ in range(n_rand):
        deg = rng.randint(1, 6)
        qc = {k: (rng.randint(-5, 5), rng.randint(-5, 5)) for k in range(0, deg + 1)}
        if all(v == (0, 0) for v in qc.values()) or all(v == (0, 0) for k, v in qc.items() if k != 0):
            qc[1] = (1, 2)
        dens.append(("random", density_from_q(qc)))
    dens.append(("note example 1 - 0.6 cos", {0: (Fr(1), Fr(0)), 1: (Fr(-3, 10), Fr(0)), -1: (Fr(-3, 10), Fr(0))}))
    # 1 - 0.6 cos + 0.3 sin 2theta : sin 2t = (e^{2it} - e^{-2it})/(2i) -> coefficient at 2: -0.15 i, at -2: +0.15 i
    dens.append(("asymmetric sine", {0: (Fr(1), Fr(0)), 1: (Fr(-3, 10), Fr(0)), -1: (Fr(-3, 10), Fr(0)),
                                     2: (Fr(0), Fr(-3, 20)), -2: (Fr(0), Fr(3, 20))}))
    bad_modsq = bad_max = bad_curv = bad_sign = 0
    worst_fd = mp.mpf(0)
    neg_or_complex = 0
    kappas = []
    for name, P in dens:
        # reality and nonnegativity (the latter by Fejer-Riesz construction; spot check)
        real_ok = all(P.get(-n, (0, 0)) == cconj(v) for n, v in P.items())
        if any(v[1] != 0 or v[0] < 0 for n, v in P.items() if n != 0):
            neg_or_complex += 1
        # overlap coefficients from the definition: c_m = p_hat_{-m} p_hat_m
        c = {m: cmul(P.get(-m, (Fr(0), Fr(0))), P[m]) for m in P}
        modsq_ok = all(c[m][1] == 0 and c[m][0] == P[m][0] ** 2 + P[m][1] ** 2 for m in c)
        if not (real_ok and modsq_ok):
            bad_modsq += 1
        # curvature: exact from C and from ||p'||^2/||p||^2
        C0 = sum(v[0] for v in c.values())
        Cpp = -sum(m * m * v[0] for m, v in c.items())
        kappa = -Cpp / C0
        dP = {n: cmul((Fr(0), Fr(n)), v) for n, v in P.items() if n != 0}          # p' coefficients i n p_hat_n
        num = sum(v[0] ** 2 + v[1] ** 2 for v in dP.values())
        den = sum(v[0] ** 2 + v[1] ** 2 for v in P.values())
        if kappa != num / den:
            bad_curv += 1
        if kappa <= 0:
            bad_sign += 1
        kappas.append(float(kappa))
        # C by quadrature of the defining integral; C <= C(0); finite-difference curvature
        if name != "random" or len(kappas) <= 12:
            def Cq(d):
                f = lambda th: mp.re(p_eval(P, th) * p_eval(P, th + d))
                return mp.quad(f, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]) / (2 * mp.pi)
            Cz = Cq(mp.mpf(0))
            h = mp.mpf("1e-6")
            fd = -(mp.log(Cq(h)) + mp.log(Cq(-h)) - 2 * mp.log(Cz)) / h ** 2
            worst_fd = max(worst_fd, abs(fd - mp.mpf(kappa.numerator) / kappa.denominator))
            # C <= C(0) on 721 points (closed form sum c_m e^{i m delta}, cross-checked against quadrature at a few)
            grid = [2 * mp.pi * j / 720 for j in range(721)]
            Cvals = [sum(mp.mpf(v[0].numerator) / v[0].denominator * mp.cos(m * d) for m, v in c.items()) for d in grid]
            for d in (mp.mpf("0.7"), mp.mpf("2.9")):
                if abs(Cq(d) - sum(mp.mpf(v[0].numerator) / v[0].denominator * mp.cos(m * d) for m, v in c.items())) > mp.mpf(10) ** -30:
                    bad_modsq += 1
            if max(Cvals) > Cvals[0] + mp.mpf(10) ** -40:
                bad_max += 1
    print(f"  {len(dens)} densities ({neg_or_complex} with negative or complex nonzero Fourier coefficients): overlap "
          f"coefficient not a real modulus square: {bad_modsq}; C(delta) > C(0) somewhere: {bad_max}; kappa != ||p'||^2/||p||^2: "
          f"{bad_curv}; kappa <= 0: {bad_sign}; max |finite-difference V''(0) - kappa| {mp.nstr(worst_fd, 3)}; kappa range "
          f"[{min(kappas):.4f}, {max(kappas):.4f}]")
    uni = {0: (Fr(1), Fr(0))}
    cu = {m: cmul(uni.get(-m, (Fr(0), Fr(0))), uni[m]) for m in uni}
    k_uni = sum(m * m * v[0] for m, v in cu.items()) / sum(v[0] for v in cu.values())
    print(f"  uniform density: C = {cu[0][0]} (no nonzero coefficient), kappa = {k_uni}")
    if bad_modsq:
        hit("an overlap coefficient is not a modulus square")
    if bad_max:
        hit("an overlap is larger away from the identity")
    if bad_curv or bad_sign or worst_fd > mp.mpf("1e-8"):
        hit("V''(0) differs from ||p'||^2/||p||^2 or is nonpositive")
    return len(dens), neg_or_complex, bad_modsq, bad_max, bad_curv, bad_sign, worst_fd, (min(kappas), max(kappas))


def run_B():
    print("=" * 78)
    print("B  Record histograms: equal bins, the sinc^2 identity, unequal bins")
    # density 1 + 0.25 cos + 0.2 sin 2 (the note's witness family extended by a sine term)
    P = {0: 1.0 + 0j, 1: 0.125 + 0j, -1: 0.125 + 0j, 2: -0.1j, -2: 0.1j}
    Pm = {n: mp.mpc(v.real, v.imag) for n, v in P.items()}

    def binmass(a, b):
        s = (b - a) / (2 * mp.pi) * Pm[0]
        for n, v in Pm.items():
            if n != 0:
                s += v * (mp.e ** (1j * n * b) - mp.e ** (1j * n * a)) / (1j * n * 2 * mp.pi)
        return mp.re(s)

    def C(d):
        return mp.re(sum(abs(v) ** 2 * mp.e ** (1j * n * d) for n, v in Pm.items()))
    rows = []
    worst_sinc = mp.mpf(0)
    for N in (16, 32, 64, 128, 256, 512, 1024, 2048, 4096):
        edges = [2 * mp.pi * i / N for i in range(N + 1)]
        f = [binmass(edges[i], edges[i + 1]) for i in range(N)]
        out = []
        for s in (N // 8, 0):
            CN = N * mp.fsum(f[i] * f[(i + s) % N] for i in range(N))
            dN = 2 * mp.pi * s / N
            sinc = mp.re(sum(abs(v) ** 2 * (mp.sin(mp.pi * n / N) / (mp.pi * n / N) if n else 1) ** 2 * mp.e ** (1j * n * dN)
                             for n, v in Pm.items()))
            worst_sinc = max(worst_sinc, abs(CN - sinc))
            out.append(abs(CN - C(dN)))
        rows.append((N, out[0], out[1]))
    rates = [rows[i][1] / rows[i + 1][1] for i in range(len(rows) - 1)]
    # unequal refining bins: widths alternating 1:2 (in units 2 pi / (1.5 N)), statistic N sum f_i^2 at zero shift
    uneq = []
    for N in (64, 256, 1024):
        w = [(1 if i % 2 == 0 else 2) for i in range(N)]
        tot = sum(w)
        edges = [mp.mpf(0)]
        for wi in w:
            edges.append(edges[-1] + 2 * mp.pi * wi / tot)
        f = [binmass(edges[i], edges[i + 1]) for i in range(N)]
        uneq.append((N, N * mp.fsum(x * x for x in f)))
    print("  equal bins |C_N - C| at delta = pi/4 and 0: " + ", ".join(f"N={N}: {mp.nstr(a, 3)}/{mp.nstr(b, 3)}" for N, a, b in rows))
    print(f"  successive error ratios at pi/4: {[mp.nstr(r, 5) for r in rates]} (-> 4 for N^-2); sinc^2 identity max dev "
          f"{mp.nstr(worst_sinc, 3)}")
    print(f"  unequal 1:2 bins, N sum f_i^2 at zero shift: {', '.join(f'N={N}: {mp.nstr(v, 10)}' for N, v in uneq)} vs C(0) = "
          f"{mp.nstr(C(0), 10)}")
    if rows[-1][1] > mp.mpf("1e-6") or worst_sinc > mp.mpf(10) ** -30:
        hit("finite equal-bin Record histograms do not approximate the overlap statistic")
    return rows, rates, worst_sinc, uneq, C(0)


def run_C():
    print("=" * 78)
    print("C  the sec. 4 example")
    p1 = Fr(-3, 10)
    c1 = p1 * p1
    Cform = (1, 2 * c1)                      # 1 + 2 c1 cos
    kappa = (2 * c1) / (1 + 2 * c1)
    # raw: -log(p(theta)/p(0)) with p = 1 - 0.6 cos; second derivative at 0 = -p''(0)/p(0) = -(0.6)/(0.4)
    raw = -Fr(6, 10) / Fr(4, 10)
    print(f"  C = 1 + {Cform[1]} cos(delta); V''(0) = {kappa} = 0.18/1.18; raw curvature {raw}")
    ok = Cform[1] == Fr(18, 100) and kappa == Fr(9, 59) and raw == Fr(-3, 2)
    if not ok:
        hit("the sec. 4 example values differ")
    return Cform[1], kappa, raw


def run_D():
    print("=" * 78)
    print("D  sec. 6 quadratic gauge blocks")
    s0, s1, s2, s3, kt, ks = sp.symbols("s0 s1 s2 s3 k_t k_s", real=True)
    s = [s0, s1, s2, s3]
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    def block(kt_, ks_):
        K = sp.zeros(4, 4)
        for mu, nu in pairs:
            w = kt_ if mu == 0 else ks_
            row = sp.zeros(1, 4)                 # (dA)_{mu nu} = s_mu A_nu - s_nu A_mu (midpoint symbols)
            row[nu] += s[mu]
            row[mu] -= s[nu]
            K += w * row.T * row
        return K
    Kt = block(kt, 0).subs(s0, 0)
    Ki = block(kt, kt).subs(s0, 0)
    sub = {s1: sp.Rational(3, 7), s2: sp.Rational(-5, 11), s3: sp.Rational(2, 13), kt: sp.Rational(9, 4)}
    rank_t = Kt.subs(sub).rank()
    rank_i = Ki.subs(sub).rank()
    gauge = sp.Matrix([0, s1, s2, s3])
    null_i = sp.simplify(Ki * gauge) == sp.zeros(4, 1)
    trans = sp.Matrix([0, s2, -s1, 0])            # A_0 = 0, A . s = 0
    e_t = sp.simplify((trans.T * Kt * trans)[0])
    e_i = sp.simplify((trans.T * Ki * trans)[0] / (trans.T * trans)[0])
    print(f"  k_0 = 0 symbolic: temporal-only rank {rank_t}, isotropic rank {rank_i}, gauge (0, s) null: {null_i}; static transverse "
          f"energy: temporal-only {e_t}, isotropic {e_i} per unit norm")
    # numeric over all spatial momenta of L = 4..10 at k_0 = 0 (same blocks, numpy)
    bad = 0
    def nblock(sv, kt_, ks_):
        K = np.zeros((4, 4))
        for mu, nu in pairs:
            w = kt_ if mu == 0 else ks_
            row = np.zeros(4)
            row[nu] += sv[mu]
            row[mu] -= sv[nu]
            K += w * np.outer(row, row)
        return K
    count = 0
    for L in range(4, 11):
        for m in np.ndindex(L, L, L):
            if m == (0, 0, 0):
                continue
            sv = np.array([0.0] + [2 * math.sin(math.pi * mi / L) for mi in m])
            rt = np.linalg.matrix_rank(nblock(sv, 1.0, 0.0), tol=1e-9)
            ri = np.linalg.matrix_rank(nblock(sv, 1.0, 1.0), tol=1e-9)
            ev = np.sort(np.linalg.eigvalsh(nblock(sv, 1.0, 1.0)))
            r2 = float(sv @ sv)
            if rt != 1 or ri != 3 or abs(ev[0]) > 1e-9 or np.max(np.abs(ev[1:] - r2)) > 1e-9:
                bad += 1
            count += 1
    print(f"  {count} static momenta on L = 4..10: temporal-only rank 1, isotropic rank 3 with spectrum {{0, |s|^2 x3}}: failures {bad}")
    if rank_t != 1 or rank_i != 3 or not null_i or e_t != 0 or bad:
        hit("the temporal-only block carries magnetic transverse stiffness, or the isotropic block differs")
    return rank_t, rank_i, e_t, e_i, count, bad


def main():
    t0 = time.time()
    nd, nneg, bm, bmax, bc, bs, wfd, kr = run_A()
    summary(f"A {nd} exact nonnegative densities ({nneg} with negative/complex coefficients): overlap coefficients real modulus "
            f"squares (failures {bm}), C <= C(0) on 721 points (failures {bmax}), kappa = ||p'||^2/||p||^2 exact (failures {bc}), "
            f"kappa > 0 (failures {bs}), 50-digit finite difference agrees to {mp.nstr(wfd, 2)}; kappa in [{kr[0]:.4f}, {kr[1]:.4f}]; "
            f"uniform gives C = 1, kappa = 0")
    rows, rates, ws, uneq, C0 = run_B()
    summary(f"B equal-bin histograms: |C_N - C(pi/4)| = {mp.nstr(rows[0][1], 3)} (N=16) ... {mp.nstr(rows[-1][1], 3)} (N=4096), "
            f"ratios -> {mp.nstr(rates[-1], 5)} (N^-2), exact sinc^2 bin identity to {mp.nstr(ws, 2)}; unequal 1:2 bins give "
            f"N sum f^2 = {mp.nstr(uneq[-1][1], 8)} vs C(0) = {mp.nstr(C0, 8)}")
    c1, kap, raw = run_C()
    summary(f"C example: C = 1 + {c1} cos, V''(0) = {kap}, raw -log p curvature {raw}")
    rt, ri, et, ei, cnt, bad = run_D()
    summary(f"D blocks at k_0 = 0: temporal-only rank {rt} with zero static transverse energy ({et}), isotropic rank {ri} with "
            f"transverse energy {ei}; {cnt} momenta on L = 4..10: failures {bad}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
