"""Refuting pass, block 23 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the full shift bound of P1 on a 4x4 window with free boundary (16 sites, 24 bonds) at beta = 1/2 and 2: the truth <s_0^1 s_x^1 + s_0^2 s_x^2>
     for x = (3, 3) by Monte Carlo with the heat-bath sampler (exact one-site conditionals e^{beta s.h}), against exp(a_x - a_0 + beta sum_b (cosh(Delta a) - 1))
     with the shift function of P2 (gamma = 1/2 and the optimized gamma) — the bound must dominate the estimate well beyond its statistical error;
(R2) the shift function's Lipschitz bound on the torus (Z/2LZ)^2 with the torus distance, L = 12, R = d_T(0, x) up to 16 (wrapping), every bond;
(R3) the harmonic bound H_R <= 1 + log R by the integral test for R <= 10^6, and the bond-sum bound 2 gamma^2 cosh(gamma)(1 + 8 H_R) against the exact
     sum over bonds of (cosh(Delta a) - 1) on Z^2 for R <= 40 (the true sum is far below the bound);
(R4) the optimization by a grid: max over gamma in (0, 1] of gamma - (128/5) beta gamma^2 at beta = 1/10, 1, 10 against 5/(512 beta) (or the boundary value);
(R5) the torus consequence: M_N^2 bound skeleton at kappa' = 1/2, 1 against direct shell sums for L <= 200."""
import math
import random

import numpy as np

random.seed(23); np.random.seed(23)


def heat_bath_window(beta, L, sweeps, burn):
    sites = [(i, j) for i in range(L) for j in range(L)]
    S = np.random.normal(size=(L, L, 3)); S /= np.linalg.norm(S, axis=2, keepdims=True)
    acc = 0.0; cnt = 0
    for sweep in range(sweeps):
        for (i, j) in sites:
            h = np.zeros(3)
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < L and 0 <= jj < L:
                    h += S[ii, jj]
            hn = np.linalg.norm(h)
            if hn < 1e-12:
                v = np.random.normal(size=3); v /= np.linalg.norm(v); S[i, j] = v; continue
            x = beta * hn
            u = random.random()
            # sample t = cos(angle to h) with density e^{x t} on [-1,1]
            t = math.log(math.exp(-x) + u * (math.exp(x) - math.exp(-x))) / x
            t = max(-1.0, min(1.0, t))
            e1 = h / hn
            tmp = np.array([1.0, 0, 0]) if abs(e1[0]) < 0.9 else np.array([0, 1.0, 0])
            e2 = np.cross(e1, tmp); e2 /= np.linalg.norm(e2); e3 = np.cross(e1, e2)
            ph = 2 * math.pi * random.random(); r = math.sqrt(max(0.0, 1 - t * t))
            S[i, j] = t * e1 + r * (math.cos(ph) * e2 + math.sin(ph) * e3)
        if sweep >= burn:
            acc += S[0, 0, 0] * S[L - 1, L - 1, 0] + S[0, 0, 1] * S[L - 1, L - 1, 1]; cnt += 1
    return acc / cnt


L = 4
x = (3, 3); R = math.hypot(*x)
for beta in (0.5, 2.0):
    est = heat_bath_window(beta, L, 6000, 500)
    for gamma in (0.5, min(1.0, 5 / (256 * beta))):
        a = {(i, j): gamma * max(0.0, math.log((1 + R) / (1 + math.hypot(i, j)))) for i in range(L) for j in range(L)}
        bonds = [((i, j), (i + 1, j)) for i in range(L - 1) for j in range(L)] + [((i, j), (i, j + 1)) for i in range(L) for j in range(L - 1)]
        bsum = sum(math.cosh(a[y] - a[z]) - 1 for y, z in bonds)
        bound = math.exp(a[x] - a[(0, 0)] + beta * bsum)
        print(f"R1 4x4 window beta={beta} gamma={gamma:.4f}: MC estimate of <s^1s^1+s^2s^2>(0,(3,3)) = {est:.4f}; P1 bound = {bound:.4f}; dominates: {abs(est) <= bound}")
Lt = 12
def dT(y):
    d1 = min(abs(y[0]) % (2 * Lt), 2 * Lt - abs(y[0]) % (2 * Lt)); d2 = min(abs(y[1]) % (2 * Lt), 2 * Lt - abs(y[1]) % (2 * Lt))
    return math.hypot(d1, d2)
ok2 = True
gamma = 0.8
for Rv in (3.0, 8.0, 12.0, 16.0):
    a = lambda y: gamma * max(0.0, math.log((1 + Rv) / (1 + dT(y))))
    for i in range(2 * Lt):
        for j in range(2 * Lt):
            for d in ((1, 0), (0, 1)):
                y = (i, j); z = ((i + d[0]) % (2 * Lt), (j + d[1]) % (2 * Lt))
                ok2 = ok2 and abs(a(y) - a(z)) <= gamma / (1 + min(dT(y), dT(z))) + 1e-12
print(f"R2 torus L=12: the shift function's Lipschitz bound holds on every bond for R = 3, 8, 12, 16 (wrapping): {ok2}")
H = 0.0; ok3 = True
for n in range(1, 10 ** 6 + 1):
    H += 1 / n
    if n in (10, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6):
        ok3 = ok3 and H <= 1 + math.log(n)
print(f"R3 H_R <= 1 + log R at R = 10^k, k <= 6: {ok3}")
ok3b = True; worst = 0.0
for Rv in range(1, 41):
    gamma = 0.7
    a = lambda y: gamma * max(0.0, math.log((1 + Rv) / (1 + math.hypot(*y))))
    tot = 0.0
    rng = range(-Rv - 2, Rv + 3)
    for i in rng:
        for j in rng:
            for d in ((1, 0), (0, 1)):
                tot += math.cosh(a((i, j)) - a((i + d[0], j + d[1]))) - 1
    bound = 2 * gamma ** 2 * math.cosh(gamma) * (1 + 8 * sum(1 / k for k in range(1, Rv + 1)))
    ok3b = ok3b and tot <= bound; worst = max(worst, tot / bound)
print(f"R3 exact bond sums on Z^2 (R <= 40, gamma = 0.7) are below 2 gamma^2 cosh(gamma)(1 + 8 H_R): {ok3b}; largest ratio {worst:.3f}")
for beta in (0.1, 1.0, 10.0):
    grid = np.linspace(1e-4, 1, 100001)
    vals = grid - (128 / 5) * beta * grid ** 2
    best = vals.max()
    ref = 5 / (512 * beta) if beta >= 5 / 256 else 1 - 128 * beta / 5
    print(f"R4 beta={beta}: grid max of gamma - (128/5) beta gamma^2 on (0,1] = {best:.6f} vs the note's {ref:.6f}")
ok5 = True
for Lv in range(1, 201):
    for kap in (0.5, 1.0):
        ssum = sum(8 * j * (1 + j) ** (-kap) for j in range(1, Lv + 1))
        ok5 = ok5 and ssum <= 8 * Lv * (1 + Lv) ** (1 - kap) + 1e-9
print(f"R5 torus shell sums <= 8 L (1+L)^(1-kappa') for L <= 200 at kappa' = 1/2, 1: {ok5}")
