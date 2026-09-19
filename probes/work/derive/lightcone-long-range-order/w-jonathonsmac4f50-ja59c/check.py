#!/usr/bin/env python3
"""lightcone-long-range-order, attempt a5: exact checks for ATTEMPT.md.

Gamma_L: vertices (x, a), x in (Z/L)^3 (L even), a in {0, 1}; edges (x,0)-(y,1) with y - x in N7 = {0, +-e1, +-e2, +-e3}.
The light-cone formation law's stationary law pi (GIVEN) is the layer-0 marginal of the sphere (n = 3) Heisenberg ferromagnet
on Gamma with coupling beta on every edge.  A = {(x,0): |x| even} u {(x,1): |x| odd}, B = the rest.

Sections (step numbers of ATTEMPT.md in brackets):
 G  graph facts, exhaustively on L = 4 and 6 [S1-S4]: every bond-plane reflection composed with the layer swap (theta_P) is an
    involutive automorphism whose crossing edges are exactly {u, theta_P u} and which maps A onto A; the pure layer swap sigma is an
    involutive automorphism swapping A and B, and with halves (A, B) its crossing edges are exactly the vertical edges
    {u, sigma u}; every edge crosses some reflection of the family; Gamma is the bilayer Z^3 x K_2 under (x,a) -> (x, a + |x| mod 2);
 P  positivity of the crossing kernel e^{beta s.s'} on the sphere (Legendre coefficients) [S2];
 N  numerical (labelled) Gaussian domination on the Ising analogue (n = 1) of Gamma in one dimension, L = 4, 6, including the
    staggered twist t 1_A that the round-1 argument could not reach [S5];
 S  the spectrum {E, 14 - E} symbolically [S6];
 T  the threshold [S8-S9]: I_0 = (1/6) sum_m p_2m and I_2 = (1/8) sum_m (9/16)^m p_2m from the exact cubic-lattice return counts
    (the recurrence checked against the closed form), with rigorous tails; beta_0 = (3/2)(I_0 + I_2) bracketed; the finite-volume
    remainders; the executed |m| = 0.76 at beta = 1 against the bound.
"""
import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


N7 = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def gamma(L, d=3, stencil=None):
    st = stencil or ([(0,) * d] + [tuple((1 if i == j else 0) * s for i in range(d)) for j in range(d) for s in (1, -1)])
    V = [(x, a) for x in itertools.product(range(L), repeat=d) for a in (0, 1)]
    E = set()
    for x in itertools.product(range(L), repeat=d):
        for n in st:
            y = tuple((x[i] + n[i]) % L for i in range(d))
            E.add(frozenset({(x, 0), (y, 1)}))
    return V, E


def par(x):
    return sum(x) % 2


# ============================================================================================ G
def section_G():
    print("=" * 100)
    print("G  reflections of Gamma_L (exhaustive, L = 4, 6)")
    ok_all = True
    stats = []
    for L in (4, 6):
        V, E = gamma(L)
        A = {v for v in V if (v[1] + par(v[0])) % 2 == 0}
        B = set(V) - A
        refl = []
        for j in range(3):
            for c in range(L // 2):          # bond planes between c, c+1 (and c + L/2, c + L/2 + 1 on the torus)
                def th(v, j=j, c=c):
                    x, a = v
                    y = list(x)
                    y[j] = (2 * c + 1 - x[j]) % L
                    return (tuple(y), 1 - a)
                plus = {v for v in V if (v[0][j] - c - 1) % L >= L // 2}      # x_j in {c-L/2+1..c}: one side
                refl.append((f"theta(dir{j},c={c})", th, plus))
        sig = lambda v: (v[0], 1 - v[1])
        refl.append(("sigma", sig, A))
        crossed = set()
        for name, th, plus in refl:
            minus = set(V) - plus
            invol = all(th(th(v)) == v for v in V)
            auto = all(frozenset({th(u) for u in e}) in E for e in E)
            swap = {th(v) for v in plus} == minus
            cross = [e for e in E if len(e & plus) == 1]
            pairs = all(th(next(iter(e & plus))) == next(iter(e & minus)) for e in cross)
            ok = invol and auto and swap and pairs
            if name != "sigma":
                ok &= {th(v) for v in A} == A
            else:
                ok &= {th(v) for v in A} == B and all(next(iter(e))[0] == next(iter(e - {next(iter(e))}))[0] for e in cross)
            ok_all &= ok
            crossed |= set(cross)
        every = crossed == E
        # the bilayer isomorphism (x, a) -> (x, a + |x| mod 2): edges -> intra-layer nearest-neighbour edges and rungs
        phi = lambda v: (v[0], (v[1] + par(v[0])) % 2)
        img = {frozenset(phi(u) for u in e) for e in E}
        bil = set()
        for x in itertools.product(range(L), repeat=3):
            bil.add(frozenset({(x, 0), (x, 1)}))
            for j in range(3):
                y = list(x)
                y[j] = (y[j] + 1) % L
                for l in (0, 1):
                    bil.add(frozenset({(x, l), (tuple(y), l)}))
        iso = img == bil and len(img) == len(E)
        ok_all &= every and iso
        stats.append(f"L={L}: {len(V)} vertices, {len(E)} edges, {len(refl)} reflections")
    check("G1", ok_all, "every theta_P (bond plane x layer swap, all planes and directions) and sigma (layer swap, halves A|B) is an involutive "
          "automorphism swapping its halves with crossing edges exactly {u, theta u}; the theta_P map A onto A (the round-1 obstruction) while "
          "sigma maps A onto B and its crossing edges are exactly the vertical edges; every edge crosses some reflection; Gamma_L is the "
          "bilayer (Z/L)^3 x K_2 under (x,a) -> (x, a + |x| mod 2): " + "; ".join(stats))


# ============================================================================================ P
def section_P():
    print("=" * 100)
    print("P  the crossing kernel e^{beta s.s'} on the sphere is positive definite")
    t = sp.Symbol("t")
    ok = True
    for l in range(0, 9):
        Pl = sp.legendre(l, t)
        for j in range(0, 25):
            v = sp.integrate(t ** j * Pl, (t, -1, 1))
            ok &= v >= 0 and (v > 0) == (j >= l and (j - l) % 2 == 0)
    check("P1", ok, "int_{-1}^{1} t^j P_l(t) dt >= 0 for l <= 8, j <= 24 (> 0 iff j >= l, j - l even): e^{beta t} = sum_j beta^j t^j / j! has "
          "positive Legendre coefficients, so by Funk-Hecke the kernel e^{beta s.s'} is a positive-definite kernel on S^2 x S^2 "
          "(the step the reflection positivity of both families uses)")


# ============================================================================================ N
def section_N():
    print("=" * 100)
    print("N  numerical (labelled): Gaussian domination on the Ising analogue of Gamma in one dimension")
    import mpmath as mp
    mp.mp.dps = 40
    worst = mp.mpf(0)
    worst_twist = mp.mpf(0)
    rng = np.random.default_rng(5)
    for L in (4, 6):
        V, E = gamma(L, d=1, stencil=[(0,), (1,), (-1,)])
        idx = {v: i for i, v in enumerate(V)}
        edges = [tuple(idx[u] for u in e) for e in E]
        A = [idx[v] for v in V if (v[1] + v[0][0]) % 2 == 0]
        configs = np.array(list(itertools.product((-1, 1), repeat=len(V))), dtype=float)
        for beta in (mp.mpf("0.3"), mp.mpf(1), mp.mpf(2)):
            def Z(h):
                tot = mp.mpf(0)
                ev = np.array(edges)
                for s in configs:
                    e = sum(float((s[i] - s[j] - (h[i] - h[j])) ** 2) for i, j in edges)
                    tot += mp.e ** (-beta * e / 2)
                return tot
            Z0 = Z([0.0] * len(V))
            for tt in (0.25, 0.5, 1.0, 2.0):
                h = [tt if i in A else 0.0 for i in range(len(V))]
                r = Z(h) / Z0
                worst_twist = max(worst_twist, r)
            for _ in range(3 if L == 6 else 6):
                h = list(rng.normal(size=len(V)))
                worst = max(worst, Z(h) / Z0)
    check("N1", worst <= 1 and worst_twist <= 1,
          f"Ising analogue (n = 1) on the 1D doubled graph, L = 4, 6, beta = 0.3, 1, 2, 40 digits: max Z(h)/Z(0) over random fields = "
          f"{mp.nstr(worst, 8)}; over the staggered twists t 1_A (t = 1/4..2) = {mp.nstr(worst_twist, 8)} (both <= 1, as S5 proves)")


# ============================================================================================ S
def section_S():
    print("=" * 100)
    print("S  the spectrum of Gamma's Laplacian")
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    Ak = 1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))
    Lk = sp.Matrix([[7, -Ak], [-Ak, 7]])
    Ek = 6 - 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))
    ev = Lk.eigenvals()
    ok = set(sp.simplify(e - Ek) for e in ev) == {0, sp.simplify(14 - 2 * Ek)} or set(sp.simplify(e) for e in ev) == {sp.simplify(Ek), sp.simplify(14 - Ek)}
    vplus = sp.Matrix([1, 1]) / sp.sqrt(2)
    vminus = sp.Matrix([1, -1]) / sp.sqrt(2)
    ok &= sp.simplify(Lk * vplus - Ek * vplus) == sp.zeros(2, 1) and sp.simplify(Lk * vminus - (14 - Ek) * vminus) == sp.zeros(2, 1)
    shift = sp.simplify((14 - Ek) - (Ek.subs({k1: k1 + sp.pi, k2: k2 + sp.pi, k3: k3 + sp.pi}) + 2)) == 0
    check("S1", ok and shift, "L(k) = [[7, -A], [-A, 7]], A = 1 + 2 sum cos k_j: eigenvectors (1, +-1)/sqrt2 with eigenvalues E(k) = 6 - 2 sum cos k_j "
          "and 14 - E(k) = E(k + (pi,pi,pi)) + 2 (the bilayer's E + 2 band, momentum-shifted)")


# ============================================================================================ T
def return_counts(M):
    """b_m = number of closed 2m-step walks on Z^3 (A002896), by the recurrence; the first 31 checked against the closed form"""
    b = [1, 6]
    for n in range(2, M + 1):
        num = 2 * (2 * n - 1) * (10 * n * n - 10 * n + 3) * b[n - 1] - 36 * (n - 1) * (2 * n - 1) * (2 * n - 3) * b[n - 2]
        assert num % (n ** 3) == 0
        b.append(num // n ** 3)
    closed = [math.comb(2 * n, n) * sum(math.comb(n, k) ** 2 * math.comb(2 * k, k) for k in range(n + 1)) for n in range(31)]
    return b, b[:31] == closed


def section_T():
    print("=" * 100)
    print("T  the threshold beta_0 = (3/2)(I_0 + I_2) and the finite-volume remainders")
    M = 2000
    b, rec_ok = return_counts(M)
    p = [Fr(b[m], 36 ** m) for m in range(M + 1)]            # p_{2m} = return probability of the 3D walk
    S0 = sum(p, Fr(0))
    S2 = sum((Fr(9, 16) ** m * p[m] for m in range(M + 1)), Fr(0))
    # rigorous tail of sum_{m > M} p_{2m}: <= 6 int_{A0}^inf [e^{-A} I_0(A)]^3 dA, e^{-A} I_0(A) <= (2 pi A)^{-1/2}(1 + (sqrt2 - 1)/(2A)) + e^{-A}/2
    A0 = Fr(2 * M + 2, 3)
    # for A >= A0: e^{-A}/2 <= 10^{-100} (2 pi A)^{-1/2}; so the bracket is <= (2 pi A)^{-1/2} (1 + eta), eta = (sqrt2 - 1)/(2 A0) + 10^{-100}
    eta = (math.sqrt(2) - 1) / (2 * float(A0)) + 1e-100
    tail_p = 6 * (1 + eta) ** 3 * (2 * math.pi) ** (-1.5) * 2 / math.sqrt(float(A0))
    tail_p_up = Fr(tail_p).limit_denominator(10 ** 12) + Fr(1, 10 ** 11)
    I0_lo, I0_hi = S0 / 6, (S0 + tail_p_up) / 6
    tail2 = Fr(1, 8) * Fr(9, 16) ** (M + 1) / Fr(7, 16)
    I2_lo, I2_hi = S2 / 8, S2 / 8 + tail2
    b0_lo, b0_hi = Fr(3, 2) * (I0_lo + I2_lo), Fr(3, 2) * (I0_hi + I2_hi)
    # the Bessel bound, checked at a few points against mpmath (numerical, labelled)
    import mpmath as mp
    mp.mp.dps = 30
    bes_ok = all(mp.e ** (-z) * mp.besseli(0, z) <= (2 * mp.pi * z) ** (-0.5) * (1 + (mp.sqrt(2) - 1) / (2 * z)) + mp.e ** (-z) / 2
                 for z in (mp.mpf(1), mp.mpf(10), mp.mpf(100), mp.mpf(1334)))
    check("T1", rec_ok and bes_ok and b0_hi - b0_lo < Fr(1, 100),
          f"return counts b_m (m <= {M}) by the recurrence, the first 31 equal to C(2m,m) sum_k C(m,k)^2 C(2k,k); "
          f"I_0 in [{float(I0_lo):.6f}, {float(I0_hi):.6f}], I_2 in [{float(I2_lo):.8f}, {float(I2_hi):.8f}]; "
          f"beta_0 = (3/2)(I_0 + I_2) in [{float(b0_lo):.5f}, {float(b0_hi):.5f}]")
    # finite volume: G_L <= I_0 + (3/(4L)) S2(L/2) + pi^2/(16 L), H_L <= I_2 + (1/2)(3/4)^L
    def eps(L):
        K = L // 2
        s2 = sum(Fr(1, m1 * m1 + m2 * m2) for m1 in range(1, K + 1) for m2 in range(1, K + 1))
        return float(Fr(3, 4 * L) * s2) + math.pi ** 2 / (16 * L) + 0.5 * 0.75 ** L
    rows = []
    for L in (12, 24, 48, 100):
        bound = 1 - 1.5 * (float(I0_hi + I2_hi) + eps(L))            # at beta = 1
        rows.append(f"L={L}: eps_L={eps(L):.4f}, <|m_0|^2> >= {bound:.4f} at beta=1")
    # numerical (labelled): the exact torus sums at L = 24, 48
    num = []
    for L in (24, 48):
        g = 2 * np.pi * np.arange(L) / L
        c = np.cos(g)
        C = c[:, None, None] + c[None, :, None] + c[None, None, :]
        Ek = 6 - 2 * C
        mask = Ek > 1e-12
        GL = (1 / Ek[mask]).sum() / L ** 3
        HL = (1 / (14 - Ek)).sum() / L ** 3
        num.append(f"L={L}: G_L={GL:.5f}, H_L={HL:.5f}, (3/2)(G_L+H_L)={1.5 * (GL + HL):.5f}")
    ok_exec = 1 - 1.5 * (float(I0_hi + I2_hi) + eps(24)) <= 0.76 ** 2
    check("T2", ok_exec, "finite volume (every even L): <|m_0|^2>_pi >= 1 - (3/(2 beta))(G_L + H_L), G_L <= I_0 + (3/(4L)) S2(L/2) + pi^2/(16L), "
          "H_L <= I_2 + (3/4)^L/2: " + "; ".join(rows) + "; consistent with the executed |m| = 0.76 at beta = 1 (0.76^2 = 0.5776); numerical torus sums: "
          + "; ".join(num))
    return b0_lo, b0_hi


def main():
    section_G()
    section_P()
    section_N()
    section_S()
    b0_lo, b0_hi = section_T()
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = (f"long-range order of pi (sphere menu) for beta > beta_0 = (3/2)(I_0 + I_2) in [{float(b0_lo):.4f}, {float(b0_hi):.4f}]: the layer swap "
            "with halves A|B (the two parity classes) is a reflection of Gamma whose crossing edges are exactly the vertical edges, which closes "
            "the round-1 gap (the staggered twist Z(t 1_A) <= Z(0) follows from one Cauchy-Schwarz step); with the bond-plane x layer-swap "
            "reflections every edge crosses a reflection, so Gaussian domination holds for all fields, the infrared bound holds on both "
            "bands {E, 14 - E}, and <|m_0|^2>_pi >= 1 - (3/(2 beta))(G_L + H_L) on every even torus")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S9, finite facts CHECKED here) " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
