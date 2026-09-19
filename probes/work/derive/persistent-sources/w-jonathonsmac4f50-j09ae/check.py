#!/usr/bin/env python3
"""persistent-sources, attempt a5: exact checks for ATTEMPT.md.

Linear light-cone formation (GIVEN): theta_{t+1} = P theta_t + xi_{t+1} on (Z/L)^3 or Z^3, P = average over the 7-stencil
N7 = {0, +-e_j} (symbol phi = 1 - E/7, E(k) = 6 - 2 sum cos k_j), xi i.i.d. N(0, sigma^2); G = (I - P)^{-1} (symbol 7/E; on the torus
the pseudo-inverse on mean-zero functions).  I - P = L3/7 with L3 the lattice Laplacian 6 - sum of the six neighbours.

Sections (step numbers of ATTEMPT.md in brackets):
 A  (a) pins: the rate of the free process holding theta(y1) = a, theta(y2) = b at every level is Delta R = (a - b)^2 / (4 sigma^2 D(r)),
    D(r) = G2(0) - G2(r), G2 = G^2 [S1-S5].  Exact torus values of G and G2 on L = 6..16 by symmetry-reduced rational solves (checked
    against FFT sums); the minimal-action configuration and its action exactly; the constant-path rate against the exact Toeplitz forms
    of the difference process (numerical, labelled); the continuum constant int_0^inf (q - sin q)/q^3 dq = pi/4, so D(r)/r -> 49/(8 pi);
 B  (b) field sources: the stationary mean G h (superposition), the path relative-entropy rate |h|^2/(2 sigma^2) (no interaction), and the
    reversible law's free energy F(h) = -(1/(2 sigma^2)) h^T (I + P) G h (interaction -(2/sigma^2) h1 h2 G(r) off the diagonal); exact on
    tori for the dipole h1 = -h2 (the only stationary two-field case on a torus) [S6-S8];
 C  (c) superposition: exact for field sources; false for pins (the two-pin mean is not the sum of one-pin means) [S9].
"""
import itertools
import math
import sys
import time
from fractions import Fraction as F

import numpy as np
import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


# ------------------------------------------------------------------------------------ symmetry-reduced exact torus solves
def orbit_data(L):
    H = L // 2
    reps = [x for x in itertools.product(range(H + 1), repeat=3) if x[0] >= x[1] >= x[2]]
    index = {x: i for i, x in enumerate(reps)}
    def fold(y):
        z = sorted((min(v % L, (-v) % L) for v in y), reverse=True)
        return tuple(z)
    def osize(x):
        s = 1
        for v in x:
            s *= 1 if v in (0, H) else 2
        perms = len(set(itertools.permutations(x)))
        return s * perms
    sizes = [osize(x) for x in reps]
    assert sum(sizes) == L ** 3
    nbr = []
    for x in reps:
        row = []
        for j in range(3):
            for sgn in (1, -1):
                y = list(x)
                y[j] += sgn
                row.append(index[fold(y)])
        nbr.append(row)
    return reps, index, sizes, nbr, fold


def solve_laplace(L, rhs_orbit, od):
    """solve L3 g = rhs on symmetric functions, with sum_x g(x) = 0 (rhs must have zero total); exact Fractions"""
    reps, index, sizes, nbr, fold = od
    n = len(reps)
    A = [[F(0)] * n + [F(0)] for _ in range(n)]
    for i in range(n):
        A[i][i] += 6
        for j in nbr[i]:
            A[i][j] -= 1
        A[i][n] = F(rhs_orbit[i])
    A[n - 1] = [F(s) for s in sizes] + [F(0)]          # replace the last equation by the mean-zero gauge
    # Gaussian elimination
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        inv = 1 / A[c][c]
        rowc = [v * inv for v in A[c]]
        A[c] = rowc
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], rowc)]
    return [A[i][n] for i in range(n)]


def torus_G_G2(L):
    od = orbit_data(L)
    reps, index, sizes, nbr, fold = od
    N = L ** 3
    rhs = [F(7) * ((1 if x == (0, 0, 0) else 0) - F(1, N)) for x in reps]
    g = solve_laplace(L, rhs, od)                     # (I - P) g = delta - 1/N, i.e. L3 g = 7(delta - 1/N); g = G (mean zero)
    h = solve_laplace(L, [7 * v for v in g], od)      # (I - P) h = g, i.e. h = G^2 delta (mean zero)
    return od, g, h


# ============================================================================================ A
def section_A():
    print("=" * 100)
    print("A  (a) two pins held at every level")
    rows = []
    ok_fft = True
    exact = {}
    for L in (6, 8, 10, 12, 14, 16):
        t = time.time()
        od, g, h = torus_G_G2(L)
        reps, index, sizes, nbr, fold = od
        D = {j: h[index[(0, 0, 0)]] - h[index[fold((j, 0, 0))]] for j in range(1, L // 2 + 1)}
        exact[L] = (od, g, h, D)
        # FFT cross-check (floats)
        kk = 2 * np.pi * np.arange(L) / L
        c = np.cos(kk)
        E = 6 - 2 * (c[:, None, None] + c[None, :, None] + c[None, None, :])
        with np.errstate(divide="ignore"):
            G2hat = np.where(E > 1e-12, 49 / E ** 2, 0.0)
            Ghat = np.where(E > 1e-12, 7 / E, 0.0)
        G2 = np.fft.ifftn(G2hat).real
        Gf = np.fft.ifftn(Ghat).real
        ok_fft &= all(abs(float(D[j]) - (G2[0, 0, 0] - G2[j, 0, 0])) < 1e-9 for j in D)
        ok_fft &= abs(float(g[index[(0, 0, 0)]]) - Gf[0, 0, 0]) < 1e-9 and abs(float(g[index[(1, 0, 0)]]) - Gf[1, 0, 0]) < 1e-9
        ok_fft &= all(D[j] < D[j + 1] for j in range(1, L // 2))          # D_L(r e1) increases with r (exact comparison)
        rows.append(f"L={L}: D(e1)={D[1]} ({float(D[1]):.5f}), D({L // 2}e1)={float(D[L // 2]):.5f} [{time.time() - t:.1f}s]")
    check("A1", ok_fft, "exact torus G and G2 = G^2 (mean zero) by symmetry-reduced rational solves of L3 g = 7(delta - 1/N), L3 h = 7g, equal to "
          "the FFT sums, and D_L(r e1) increasing in r on every torus; D_L(r e1) = G2(0) - G2(r e1): " + "; ".join(rows))
    # A2: the minimal action exactly (L = 8): theta* = mu G2 (delta_y1 - delta_y2) holds the difference at delta with action delta^2/(2 D)
    L = 8
    od, g, h, D = exact[L]
    reps, index, sizes, nbr, fold = od
    N = L ** 3
    y1, y2, r = (0, 0, 0), (3, 0, 0), 3
    def G2at(x):
        return h[index[fold(x)]]
    delta = F(1)
    mu = delta / (2 * (G2at((0, 0, 0)) - G2at((r, 0, 0))))
    theta = {x: mu * (G2at(tuple(x[i] - y1[i] for i in range(3))) - G2at(tuple(x[i] - y2[i] for i in range(3))))
             for x in itertools.product(range(L), repeat=3)}
    held = theta[y1] - theta[y2] == delta
    # (I - P) theta = mu G (delta_y1 - delta_y2): compare, and the action |(I - P) theta|^2 = mu^2 (2 G2(0) - 2 G2(r))
    def Gat(x):
        return g[index[fold(x)]]
    def IminusP(f, x):
        s = f[x]
        for n in ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            s -= f[tuple((x[i] + n[i]) % L for i in range(3))] / 7
        return s
    res_ok = all(IminusP(theta, x) == mu * (Gat(tuple(x[i] - y1[i] for i in range(3))) - Gat(tuple(x[i] - y2[i] for i in range(3))))
                 for x in list(theta)[:120])
    action = sum(IminusP(theta, x) ** 2 for x in theta)
    act_ok = action == delta ** 2 / (2 * (G2at((0, 0, 0)) - G2at((r, 0, 0))))
    # a common shift is free: (I - P) 1 = 0
    free_ok = all(IminusP({x: F(1) for x in theta}, x) == 0 for x in list(theta)[:50])
    check("A2", held and res_ok and act_ok and free_ok,
          f"L = 8, pins at distance 3: theta* = mu G2(. - y1) - mu G2(. - y2) holds theta(y1) - theta(y2) = 1 with (I - P) theta* = mu G(. - y1) - mu G(. - y2) "
          f"and action |(I - P) theta*|^2 = 1/(2 D) = {action} exactly; a common shift costs nothing ((I - P) 1 = 0): the rate is (a - b)^2/(4 sigma^2 D)")
    # A3: the constant-path rate of the stationary difference process against its Toeplitz forms (numerical, labelled)
    L = 6
    od, g, h, D = exact[L]
    kk = 2 * np.pi * np.arange(L) / L
    c = np.cos(kk)
    E = 6 - 2 * (c[:, None, None] + c[None, :, None] + c[None, None, :])
    phi = 1 - E / 7
    r = 2
    num = 2 - 2 * np.cos(kk * r)[:, None, None] * np.ones_like(E)
    mask = E > 1e-12
    def gam(tau):
        return float((num[mask] * phi[mask] ** abs(tau) / (1 - phi[mask] ** 2)).sum() / L ** 3)
    target = 1 / (2 * 2 * float(D[r]))                 # (1/2) 1^T Gamma^{-1} 1 / T -> 1/(2 * long-run variance), long-run variance = 2 D
    vals = []
    for T in (50, 100, 200, 400):
        Gm = np.array([[gam(i - j) for j in range(T)] for i in range(T)])
        x = np.linalg.solve(Gm, np.ones(T))
        vals.append(0.5 * x.sum() / T)
    conv = abs(vals[-1] - target) < abs(vals[0] - target) and abs(vals[-1] - target) / target < 0.02
    check("A3", conv, f"numerical (L = 6, r = 2 e1, sigma = 1): the constant-path cost per level (1/(2T)) 1^T Gamma_T^(-1) 1 of the difference process = "
          + ", ".join(f"{v:.5f}" for v in vals) + f" at T = 50, 100, 200, 400 -> 1/(4 D) = {target:.5f}")
    # A4: the continuum constant and the 1/r coefficient
    q = sp.Symbol("q", positive=True)
    I = sp.integrate((q - sp.sin(q)) / q ** 3, (q, 0, sp.oo))
    c_ok = sp.simplify(I - sp.pi / 4) == 0
    coeff = sp.Rational(49, 1) * (1 / (2 * sp.pi ** 2)) * I       # D(r)/r -> 49 (1/(2 pi^2)) int (q - sin q)/q^3
    coeff_ok = sp.simplify(coeff - sp.Rational(49, 8) / sp.pi) == 0
    # numerical (labelled): infinite-volume D(r e1) = 49 int_0^inf t e^{-6t} I_0(2t)^2 (I_0(2t) - I_r(2t)) dt (1/E^2 = int t e^{-tE} dt)
    import mpmath as mp
    mp.mp.dps = 30
    def Dinf(rr):
        f = lambda t: t * (mp.besseli(0, 2 * t) * mp.e ** (-2 * t)) ** 2 * (mp.besseli(0, 2 * t) - mp.besseli(rr, 2 * t)) * mp.e ** (-2 * t)
        return 49 * mp.quad(f, [0, 1, 10, 100, 1000, 10000, mp.inf])
    lim = 49 / (8 * mp.pi)
    trend = [(rr, Dinf(rr)) for rr in (4, 16, 64, 128)]
    gaps = [abs(d / rr - lim) for rr, d in trend]
    offs = [d - lim * rr for rr, d in trend]
    mono = all(gaps[i + 1] < gaps[i] for i in range(len(gaps) - 1)) and abs(offs[-1] - offs[-2]) < abs(offs[1] - offs[0])
    check("A4", c_ok and coeff_ok and mono, f"int_0^inf (q - sin q)/q^3 dq = {I}, so D(r)/r -> 49/(8 pi) = {float(lim):.5f} and Delta R -> "
          f"2 pi (a - b)^2 / (49 sigma^2 r); numerical infinite-volume values (Bessel integral, 30 digits): "
          + ", ".join(f"D/r = {float(d / rr):.5f} at r = {rr}" for rr, d in trend)
          + f"; D - 49 r/(8 pi) = " + ", ".join(f"{float(o):.4f}" for o in offs) + " (a constant offset near 0.59)")
    return exact


# ============================================================================================ B
def section_B(exact):
    print("=" * 100)
    print("B  (b) two field sources")
    # B1: dipole on the torus: m = h (G(. - y1) - G(. - y2)) solves m = P m + h exactly; a nonzero total field makes the mean drift
    L = 8
    od, g, h2, D = exact[L]
    reps, index, sizes, nbr, fold = od
    def Gat(x):
        return g[index[fold(x)]]
    y1, y2 = (0, 0, 0), (3, 0, 0)
    hval = F(1)
    m = {x: hval * (Gat(tuple(x[i] - y1[i] for i in range(3))) - Gat(tuple(x[i] - y2[i] for i in range(3)))) for x in itertools.product(range(L), repeat=3)}
    def Pf(f, x):
        return sum(f[tuple((x[i] + n[i]) % L for i in range(3))] for n in ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))) / 7
    src = lambda x: hval if x == y1 else (-hval if x == y2 else 0)
    stat = all(m[x] == Pf(m, x) + src(x) for x in m)
    check("B1", stat, "L = 8, dipole h at y1, -h at y2 (distance 3): the stationary mean m = h G(. - y1) - h G(. - y2) satisfies m = P m + h exactly "
          "(superposition of the one-source means); with h1 + h2 != 0 the spatial mean grows by h1 + h2 per level, so no stationary law on a torus")
    # B2: the path relative-entropy rate
    x, hs, s2 = sp.symbols("x h sigma2", positive=True)
    xi = sp.Symbol("xi", real=True)
    llr = ((hs + xi) ** 2 - xi ** 2) / (2 * s2)
    kl = sp.integrate(llr * sp.exp(-xi ** 2 / (2 * s2)) / sp.sqrt(2 * sp.pi * s2), (xi, -sp.oo, sp.oo))
    check("B2", sp.simplify(kl - hs ** 2 / (2 * s2)) == 0,
          "the relative entropy per level and per source site of the sourced chain against the free one is h^2/(2 sigma^2): the path rate is "
          "(h1^2 + h2^2)/(2 sigma^2), with no term depending on the distance")
    # B3: the reversible law's free energy: C^{-1} G = (I + P)/sigma^2; F = -(1/(2 sigma^2)) h^T (I + P) G h; dipole value on the torus
    def IpPG(x):
        return 2 * Gat(x) - ((1 if x == (0, 0, 0) else 0) - F(1, L ** 3))
    Fdip = -(hval ** 2) * (IpPG((0, 0, 0)) - IpPG((3, 0, 0)))            # sigma^2 = 1
    alt = -(hval ** 2) * (2 * (Gat((0, 0, 0)) - Gat((3, 0, 0))) - 1)
    # the matrix identity C^{-1} G = (I + P)/sigma^2 on every mode: (1 - phi^2)(1/(1 - phi)) = 1 + phi
    ph = sp.Symbol("phi")
    ident = sp.simplify((1 - ph ** 2) / (1 - ph) - (1 + ph)) == 0
    check("B3", Fdip == alt and ident, f"the reversible linear law with a field: pi_h = N(G h, C), C = sigma^2 (I - P^2)^-1, so -log pi_h couples to theta through "
          f"C^-1 G h = (I + P) h / sigma^2 and the free energy is F(h) = -(1/(2 sigma^2)) h^T (I + P) G h; for two sources its cross term is "
          f"-(1/sigma^2) h1 h2 ((I + P) G)(r) = -(2/sigma^2) h1 h2 G(r) for r != 0, i.e. -7 h1 h2/(2 pi sigma^2 r) at large r; L = 8 dipole value "
          f"F = {Fdip} (sigma = 1)")


# ============================================================================================ C
def section_C():
    print("=" * 100)
    print("C  (c) superposition")
    G0, Gr, a, b = sp.symbols("G0 Gr a b", real=True)
    c1, c2 = sp.symbols("c1 c2")
    sol = sp.solve([G0 * c1 + Gr * c2 - a, Gr * c1 + G0 * c2 - b], [c1, c2])
    at_y1 = sp.simplify(G0 * sol[c1] + Gr * sol[c2])
    naive = a + b * Gr / G0
    diff = sp.simplify(naive - at_y1)
    ok = at_y1 == a and sp.simplify(diff - b * Gr / G0) == 0
    check("C1", ok, "two pins on Z^3: the pinned mean is c1 G(. - y1) + c2 G(. - y2) with [[G(0), G(r)], [G(r), G(0)]] c = (a, b); the sum of the two "
          "one-pin means alpha G(. - y)/G(0) exceeds the pin at y1 by b G(r)/G(0): pins do not superpose, field sources do (B1)")


def main():
    exact = section_A()
    section_B(exact)
    section_C()
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("two sites held at a and b at every level cost the free linear light-cone process the rate (a - b)^2/(4 sigma^2 D(r)) per level, "
            "D = G^2(0) - G^2(r): zero for like pins at every distance, positive and decreasing for unlike pins, with D(r)/r -> 49/(8 pi) so "
            "Delta R = 2 pi (a - b)^2/(49 sigma^2 r) + o(1/r); two field sources: the stationary mean superposes, the path relative-entropy "
            "rate (h1^2 + h2^2)/(2 sigma^2) has no distance dependence, while the reversible law's free energy has the cross term "
            "-(2/sigma^2) h1 h2 G(r) ~ -7 h1 h2/(2 pi sigma^2 r); pins do not superpose; exact torus values L = 6..16")
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
