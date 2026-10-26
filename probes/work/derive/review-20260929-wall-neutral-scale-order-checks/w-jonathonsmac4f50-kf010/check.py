#!/usr/bin/env python3
"""J:derive:review-20260929-wall-neutral-scale-order-checks:a1

Contentless record gas on an even cubic torus (T21's "0.412").  What is exact,
what is imported, what is numerical.

Machinery (disjoint from the sources' C/Metropolis codes): Fractions and Python
integers for every finite identity; mpmath for constants; numpy only for
enumeration bookkeeping, FFT-free lattice sums and a small heat-bath run.

Families
  A  gas == antiferromagnetic Ising, exactly (T1(b) of the landed 2026-09-24 note)
  B  reflection positivity: fails for the gas variables, holds after the
     sublattice complement (exact 2x2 and 256x256 reflection forms)
  C  infrared (Gaussian-domination) instances: exact structure factors
  D  constants: Watson integral, finite-torus sums, g_IR, bracket
  E  Simon-Lieb instance (disorder side of the bracket)
  F  small independent Monte Carlo: the 0.41 crossing is numerical
Exit code 0 unless a check fails.
"""
import itertools
import math
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np

mp.mp.dps = 40
T0 = time.time()
RESULTS = []


def rep(ok, msg):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + msg, flush=True)


# ---------------------------------------------------------------- graph tools
def torus(dims):
    """Sites and the dV edges (multigraph when some side is 2): (x, x+e_i)."""
    sites = list(itertools.product(*[range(n) for n in dims]))
    pos = {x: i for i, x in enumerate(sites)}
    edges = []
    for x in sites:
        for i in range(len(dims)):
            y = list(x)
            y[i] = (y[i] + 1) % dims[i]
            edges.append((pos[x], pos[tuple(y)]))
    return sites, pos, edges


def all_configs(V):
    N = 1 << V
    return ((np.arange(N, dtype=np.int64)[:, None] >> np.arange(V)) & 1).astype(np.int8)


# ------------------------------------------------------------------ family A
def family_A():
    g = Fraction(1, 4)          # sqrt(g) = 1/2 rational
    half = Fraction(1, 2)
    for dims in [(4, 4), (4, 2, 2)]:
        d = len(dims)
        sites, pos, edges = torus(dims)
        V = len(sites)
        n = all_configs(V)
        B = np.zeros(len(n), dtype=np.int64)       # recorded bonds (both ends occupied)
        like = np.zeros(len(n), dtype=np.int64)    # bonds with equal occupancy
        for u, v in edges:
            B += (n[:, u] & n[:, v])
            like += (n[:, u] == n[:, v])
        N = n.sum(axis=1, dtype=np.int64)
        # zeta = g^(-d) (d = 3 is g^-3 of the landed note); T1(b): B - dN = (like - dV)/2
        ok = True
        for Bi, li, Ni in zip(B.tolist(), like.tolist(), N.tolist()):
            wg = (g ** (-d)) ** Ni * g ** Bi
            wi = half ** li
            if wg / wi != Fraction(2) ** (d * V):
                ok = False
                break
        rep(ok, "A1 exact gas weight zeta^N g^B = 2^(dV) * (1/2)^(#like) on every one of "
                "%d configurations of the %s torus (g=1/4, zeta=g^-%d)" % (len(n), dims, d))
    # 3D simple graph 4x4x4, random sample
    rng = np.random.default_rng(20260929)
    sites, pos, edges = torus((4, 4, 4))
    V = len(sites)
    ok = True
    for _ in range(300):
        occ = rng.integers(0, 2, V)
        Bi = sum(int(occ[u] & occ[v]) for u, v in edges)
        li = sum(int(occ[u] == occ[v]) for u, v in edges)
        Ni = int(occ.sum())
        wg = (g ** (-3)) ** Ni * g ** Bi
        ok &= (wg / Fraction(1, 2) ** li == Fraction(2) ** (3 * V))
    rep(ok, "A2 same identity on 300 random configurations of the simple 4x4x4 torus (exact Fractions)")
    # complement symmetry n -> 1-n on the even torus without contents (T1(b))
    ok = True
    for _ in range(300):
        occ = rng.integers(0, 2, V)
        w1 = (g ** (-3)) ** int(occ.sum()) * g ** sum(int(occ[u] & occ[v]) for u, v in edges)
        c = 1 - occ
        w2 = (g ** (-3)) ** int(c.sum()) * g ** sum(int(c[u] & c[v]) for u, v in edges)
        ok &= (w1 == w2)
    rep(ok, "A3 complement n->1-n leaves the weight unchanged at zeta=g^-3 (half filling in expectation)")
    # g = e^{-4K}: aligned/anti-aligned = e^{-2K} = sqrt(g)
    K = -mp.log(mp.mpf(1) / 4) / 4
    rep(abs(mp.exp(-2 * K) - mp.mpf(1) / 2) < mp.mpf(10) ** -35,
        "A4 g = exp(-4K): Ising coupling K = ln(2)/2 for g=1/4, e^{-2K} = 1/2")


# ------------------------------------------------------------------ family B
def reflection_forms(dims, a, b):
    """A (plain reflection) and A' (reflection with spin flip) for the AFM Ising
    weight (a/b)^{#like}, reflection x0 -> 1-x0 (mod L0) on the first axis."""
    sites, pos, edges = torus(dims)
    V = len(sites)
    L0 = dims[0]
    s = all_configs(V).astype(np.int64) * 2 - 1
    like = np.zeros(len(s), dtype=np.int64)
    for u, v in edges:
        like += (s[:, u] == s[:, v])
    E = len(edges)
    table = [a ** l * b ** (E - l) for l in range(E + 1)]
    w = [table[l] for l in like.tolist()]
    refl = {}
    for x in sites:
        y = list(x)
        y[0] = (1 - x[0]) % L0
        refl[pos[x]] = pos[tuple(y)]
    plus = [pos[x] for x in sites if x[0] in (1, 2)]       # columns 1,2 (L0 = 4)
    idx_plus = {p: i for i, p in enumerate(plus)}
    P = len(plus)
    # code of the + half configuration
    pw = (1 << np.arange(P)).astype(np.int64)
    code_a = ((s[:, plus] + 1) // 2 * pw).sum(axis=1)
    # Theta applied to the - half, read on the + sites: sigma(refl(y)), y in +
    mirror = [refl[y] for y in plus]
    code_c = ((s[:, mirror] + 1) // 2 * pw).sum(axis=1)
    code_cf = ((-s[:, mirror] + 1) // 2 * pw).sum(axis=1)
    A = [[0] * (1 << P) for _ in range(1 << P)]
    Af = [[0] * (1 << P) for _ in range(1 << P)]
    for wi, ca, cc, ccf in zip(w, code_a.tolist(), code_c.tolist(), code_cf.tolist()):
        A[ca][cc] += wi
        Af[ca][ccf] += wi
    return A, Af


def family_B():
    a, b = 1, 2   # sqrt(g) = 1/2 -> g = 1/4
    # exact 2x2 cross-bond forms
    M_afm = np.array([[a, b], [b, a]], dtype=object)       # (s, s') -> a if like else b
    det_afm = a * a - b * b
    rep(det_afm < 0, "B1 cross-bond form in the gas/AFM variables [[a,b],[b,a]], a/b=1/2: det = %d < 0, "
                     "not positive semidefinite (exact)" % det_afm)
    det_fer = b * b - a * a
    rep(det_fer > 0 and b > 0, "B2 cross-bond form after the sublattice complement [[b,a],[a,b]]: "
                               "trace %d, det %d: positive definite (exact)" % (2 * b, det_fer))
    for dims in [(4, 4), (4, 2, 2)]:
        A, Af = reflection_forms(dims, a, b)
        An = np.array([[float(x) for x in row] for row in A])
        Afn = np.array([[float(x) for x in row] for row in Af])
        An /= An.max()
        Afn /= Afn.max()
        assert np.allclose(An, An.T) and np.allclose(Afn, Afn.T)
        ev = np.linalg.eigvalsh(An)
        evf = np.linalg.eigvalsh(Afn)
        rep(ev[0] < -1e-6,
            "B3 %s torus, plain reflection through bond planes of the AFM weight: smallest eigenvalue "
            "%.3e < 0, not reflection positive" % (dims, ev[0]))
        # exact certificate: rationalise the eigenvector, evaluate f A f with integers
        w_, U = np.linalg.eigh(An)
        f = np.rint(U[:, 0] / np.abs(U[:, 0]).max() * 1000).astype(np.int64).tolist()
        fAf = sum(f[i] * A[i][j] * f[j] for i in range(len(f)) for j in range(len(f)) if f[i] and f[j])
        rep(fAf < 0, "B4 %s: exact integer certificate f.A.f < 0 for a rationalised vector" % (dims,))
        rep(evf[0] > -1e-12,
            "B5 %s torus, reflection composed with a global spin flip (= plain reflection of the sublattice-"
            "complemented ferromagnet): smallest eigenvalue %.3e >= 0 (float, normalised)" % (dims, evf[0]))


# ------------------------------------------------------------------ family C
COS4 = [1, 0, -1, 0]
SIN4 = [0, 1, 0, -1]


def structure(dims, a, b):
    """Exact staggered structure factors S(k) and m^2 of the AFM weight (a/b)^{#like}."""
    sites, pos, edges = torus(dims)
    V = len(sites)
    d = len(dims)
    s = all_configs(V).astype(np.int64) * 2 - 1
    like = np.zeros(len(s), dtype=np.int64)
    for u, v in edges:
        like += (s[:, u] == s[:, v])
    E = len(edges)
    table = [a ** l * b ** (E - l) for l in range(E + 1)]
    w = [table[l] for l in like.tolist()]
    Z = sum(w)
    stag = np.array([(-1) ** sum(x) for x in sites], dtype=np.int64)
    st = s * stag[None, :]
    out = {}
    for kk in itertools.product(*[range(n) for n in dims]):
        e = [(kk[j] * x[j] * (4 // dims[j])) % 4 for x in sites for j in range(d)]
        e = np.array(e).reshape(V, d).sum(axis=1) % 4
        cr = np.array([COS4[t] for t in e], dtype=np.int64)
        ci = np.array([SIN4[t] for t in e], dtype=np.int64)
        re = (st * cr[None, :]).sum(axis=1)
        im = (st * ci[None, :]).sum(axis=1)
        m2 = (re * re + im * im).tolist()
        Sk = Fraction(sum(wi * mi for wi, mi in zip(w, m2)), Z * V)
        Ek = sum(1 - Fraction(COS4[(kk[j] * (4 // dims[j])) % 4]) for j in range(d))
        out[kk] = (Sk, Ek)
    return out, V


def family_C():
    for dims in [(4, 4), (4, 2, 2)]:
        for (a, b) in [(1, 2), (1, 3)]:
            out, V = structure(dims, a, b)
            K = mp.log(mp.mpf(b) / a) / 2
            worst = mp.mpf(0)
            for kk, (Sk, Ek) in out.items():
                if all(k == 0 for k in kk):
                    continue
                ratio = mp.mpf(Sk.numerator) / Sk.denominator * mp.mpf(Ek.numerator) / Ek.denominator * 2 * K
                worst = max(worst, ratio)
            rep(worst < 1,
                "C1 %s torus, a/b=%d/%d (exact S(k)): staggered S(k) <= 1/(2K E(k)) for all k != 0; "
                "worst ratio %s" % (dims, a, b, mp.nstr(worst, 6)))
            # the consequence for the staggered magnetisation
            S0, _ = out[tuple(0 for _ in dims)]
            m2 = mp.mpf(S0.numerator) / S0.denominator / V
            GL = sum(1 / (mp.mpf(Ek.numerator) / Ek.denominator)
                     for kk, (Sk, Ek) in out.items() if any(kk)) / V
            bound = 1 - GL / (2 * K)
            rep(m2 >= bound, "C2 %s torus, a/b=%d/%d: <m_stag^2> = %s >= 1 - G_L/(2K) = %s"
                % (dims, a, b, mp.nstr(m2, 8), mp.nstr(bound, 8)))
            # sum rule (1/V) sum_k S(k) = 1, exact
            tot = sum(Sk for Sk, _ in out.values()) / V
            rep(tot == 1, "C3 %s torus, a/b=%d/%d: exact sum rule (1/V) sum_k S(k) = 1" % (dims, a, b))


# ------------------------------------------------------------------ family D
def GL_torus(L):
    k = 2 * np.pi * np.arange(L) / L
    e = 1 - np.cos(k)
    E = e[:, None, None] + e[None, :, None] + e[None, None, :]
    E[0, 0, 0] = np.inf
    return (1.0 / E).sum() / L ** 3


def family_D():
    # Watson constant two independent ways
    f = lambda s: mp.exp(-3 * s) * mp.besseli(0, s) ** 3
    G_bessel = mp.quad(f, [0, 1, 5, 20, 100, 1000, 10 ** 4, 10 ** 5, mp.inf])
    G_gamma = (mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24)
               * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)) / 3
    rep(abs(G_bessel - G_gamma) < mp.mpf(10) ** -12,
        "D1 G_inf = int d^3k/(2pi)^3 1/(3 - sum cos k) = %s: Bessel-integral quadrature equals the Gamma-product "
        "closed form / 3 to 1e-12 (|diff| = %s)" % (mp.nstr(G_gamma, 12), mp.nstr(abs(G_bessel - G_gamma), 3)))
    G = G_gamma
    # finite torus sums
    prev = 0.0
    mono = True
    below = True
    vals = {}
    for L in (4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128):
        gl = GL_torus(L)
        vals[L] = gl
        mono &= gl > prev
        below &= gl < float(G)
        prev = gl
    rep(mono and below, "D2 G_L = (1/V) sum_{k!=0} 1/E(k) increases with L and stays below G_inf for even L = 4..128 "
                        "(G_4 = %.6f, G_128 = %.6f, G_inf = %.6f)" % (vals[4], vals[128], float(G)))
    # extrapolation to the Watson constant: independent confirmation of the limit
    Ls = np.array([32, 48, 64, 96, 128], dtype=float)
    Y = np.array([vals[int(L)] for L in Ls])
    X = np.vstack([np.ones_like(Ls), 1 / Ls, 1 / Ls ** 2, 1 / Ls ** 3]).T
    coef = np.linalg.lstsq(X, Y, rcond=None)[0]
    rep(abs(coef[0] - float(G)) < 2e-5, "D3 fit G_L = G + c1/L + c2/L^2 + c3/L^3 on L=32..128 gives G = %.7f "
                                         "(closed form %.7f): G_L -> G_inf" % (coef[0], float(G)))
    # thresholds
    K_ir = G / 2
    g_ir = mp.exp(-4 * K_ir)
    rep(mp.mpf("0.2527") < K_ir < mp.mpf("0.2528"), "D4 K_IR = G_inf/2 = %s" % mp.nstr(K_ir, 10))
    rep(mp.mpf("0.3638") < g_ir < mp.mpf("0.3640"),
        "D5 g_IR = exp(-4 K_IR) = exp(-2 G_inf) = %s" % mp.nstr(g_ir, 10))
    old = mp.mpf(9) / 62500
    rep(g_ir > old, "D6 g_IR / (9/62500) = %s: the infrared threshold exceeds the landed contentless Peierls "
                    "threshold by a factor %.0f" % (mp.nstr(g_ir / old, 6), float(g_ir / old)))
    # rigorous lower bound on <m_stag^2> at g = 1/4 and at the scan points, all even L (D2 monotone) and L -> inf
    for gg in (mp.mpf(1) / 4, mp.mpf("0.30"), mp.mpf("0.35")):
        Kg = -mp.log(gg) / 4
        bnd = 1 - G / (2 * Kg)
        rep(bnd > 0, "D7 g = %s: <m_stag^2> >= 1 - G/(2K) = %s  (L -> inf; G_L < G for the listed L)"
            % (mp.nstr(gg, 4), mp.nstr(bnd, 6)))
    # disorder side: Simon-Lieb one-site gives tanh K < 1/6, i.e. g > ((1-t)/(1+t))^2 = 25/49
    t = Fraction(1, 6)
    g_sl = ((1 - t) / (1 + t)) ** 2
    rep(g_sl == Fraction(25, 49), "D8 disorder side: tanh K < 1/(2d) = 1/6 <=> g > ((1-t)/(1+t))^2 = %s = %.5f"
        % (g_sl, float(g_sl)))
    # literature value (reference only) lies strictly inside the bracket
    K_lit = mp.mpf("0.2216546")
    g_lit = mp.exp(-4 * K_lit)
    rep(g_ir < g_lit < mp.mpf(25) / 49,
        "D9 bracket: g_IR = %s < exp(-4 K_c^{lit}) = %s < 25/49 = %s  (K_c^{lit} = 0.2216546 is a numerical "
        "literature value, not derived here)" % (mp.nstr(g_ir, 6), mp.nstr(g_lit, 6), mp.nstr(mp.mpf(25) / 49, 6)))
    # no closed form: the proved bracket has width
    rep(mp.mpf(25) / 49 - g_ir > mp.mpf("0.14"),
        "D10 proved bracket for the transition value of g has width %s (nothing here fixes it to 0.412)"
        % mp.nstr(mp.mpf(25) / 49 - g_ir, 4))


# ------------------------------------------------------------------ family E
def family_E():
    for dims in [(4, 4), (4, 2, 2)]:
        a, b = 1, 2
        sites, pos, edges = torus(dims)
        V = len(sites)
        s = all_configs(V).astype(np.int64) * 2 - 1
        unlike = np.zeros(len(s), dtype=np.int64)
        for u, v in edges:
            unlike += (s[:, u] != s[:, v])
        E = len(edges)
        table = [a ** l * b ** (E - l) for l in range(E + 1)]       # ferro weight (a/b)^{#unlike}
        w = [table[l] for l in unlike.tolist()]
        Z = sum(w)
        t = Fraction(b - a, b + a)           # tanh K with e^{-2K} = a/b
        nb = {}
        for u, v in edges:
            nb.setdefault(u, []).append(v)
            nb.setdefault(v, []).append(u)

        def corr(x, y):
            return Fraction(sum(wi * int(p) for wi, p in zip(w, (s[:, x] * s[:, y]).tolist())), Z)
        ok = True
        worst = None
        for x in range(1, V):
            lhs = corr(0, x)
            rhs = t * sum(corr(y, x) for y in nb[0])
            ok &= lhs <= rhs
            slack = rhs - lhs
            worst = slack if worst is None or slack < worst else worst
        rep(ok, "E1 %s torus, ferro e^{-2K}=1/2 (tanh K = 1/3): Simon-Lieb one-site instance "
                "<s_0 s_x> <= tanh K sum_{y~0} <s_y s_x> for every x != 0 (exact; min slack %s)" % (dims, worst))


# ------------------------------------------------------------------ family F
def heat_bath(L, K, sweeps, burn, rng):
    s = np.where(rng.random((L, L, L)) < 0.5, 1, -1).astype(np.int8)
    ii, jj, kk = np.indices((L, L, L))
    masks = [((ii + jj + kk) % 2 == 0), ((ii + jj + kk) % 2 == 1)]
    m2 = 0.0
    m4 = 0.0
    cnt = 0
    for it in range(sweeps + burn):
        for mk in masks:
            h = (np.roll(s, 1, 0) + np.roll(s, -1, 0) + np.roll(s, 1, 1) + np.roll(s, -1, 1)
                 + np.roll(s, 1, 2) + np.roll(s, -1, 2)).astype(np.float64)
            p = 1.0 / (1.0 + np.exp(-2 * K * h))
            new = np.where(rng.random((L, L, L)) < p, 1, -1).astype(np.int8)
            s = np.where(mk, new, s)
        if it >= burn:
            m = float(s.sum()) / L ** 3
            m2 += m * m
            m4 += m ** 4
            cnt += 1
    m2 /= cnt
    m4 /= cnt
    return 1 - m4 / (3 * m2 * m2)


def family_F():
    # ferro variables == AFM gas on an even torus (family A); g = exp(-4K)
    rng = np.random.default_rng(1234567)
    gs = [0.34, 0.38, 0.40, 0.41, 0.42, 0.44, 0.48]
    Ls = (6, 10, 14)
    sweeps = {6: 60000, 10: 40000, 14: 30000}
    U = {L: [] for L in Ls}
    for L in Ls:
        for g in gs:
            K = -math.log(g) / 4
            U[L].append(heat_bath(L, K, sweeps[L], 2000, rng))
    diff = [U[14][i] - U[6][i] for i in range(len(gs))]
    for i, g in enumerate(gs):
        print("     g=%.2f  U4(L=6)=%.4f  U4(L=10)=%.4f  U4(L=14)=%.4f  diff(14-6)=%+.4f"
              % (g, U[6][i], U[10][i], U[14][i], diff[i]), flush=True)
    rep(diff[0] > 0 and diff[-1] < 0,
        "F1 Binder cumulant of the staggered magnetisation: L=14 above L=6 at g=0.34 (ordered side) and below at "
        "g=0.48 (disordered side)")
    cross = None
    for i in range(len(gs) - 1):
        if diff[i] > 0 >= diff[i + 1]:
            cross = gs[i] + (gs[i + 1] - gs[i]) * diff[i] / (diff[i] - diff[i + 1])
            break
    rep(cross is not None and 0.37 <= cross <= 0.45,
        "F2 crossing of the L=6 and L=14 Binder curves at g ~ %s (statistical, small sizes; numerical scope of "
        "the 0.41 figure; not a proof)" % ("%.3f" % cross if cross is not None else "none"))
    gir = math.exp(-2 * 0.5054620197173)
    rep(diff[0] > 0 and gs[0] < gir,
        "F3 the rigorous ordered range g <= %.4f (D5) is consistent with the run (g=0.34 ordered)" % gir)


def main():
    family_A()
    family_B()
    family_C()
    family_D()
    family_E()
    family_F()
    n_pass = sum(RESULTS)
    n_fail = len(RESULTS) - n_pass
    print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
    if n_fail == 0:
        print("HIT: for the contentless record gas on even tori (exactly the 3D antiferromagnetic Ising model, "
              "g = exp(-4K), zeta = g^-3), the infrared bound gives staggered order for every g <= exp(-2 G_inf) "
              "= 0.36388, about 2500 times the landed Peierls threshold 9/62500, and the exact reflection form "
              "shows that, for the contentless gas on even tori, the 'reflection-positivity floor' g >= 1 belongs to the gas variables only; "
              "0.412 stays a numerical value inside the proved bracket (0.36388, 25/49).")
    print("SUMMARY: the contentless gas is exactly the 3D AFM Ising model, whose proved ordered range (infrared "
          "bound, imported theorem, instances verified exactly) reaches g=0.36388 and whose disordered range "
          "starts at 25/49, so 0.412 is a numerical value inside a proved bracket, and (contentless, even tori) reflection "
          "positivity holds after a sublattice complement for every g<1; runtime %.0f s." % (time.time() - T0))
    sys.exit(0 if n_fail == 0 else 1)


if __name__ == "__main__":
    main()
