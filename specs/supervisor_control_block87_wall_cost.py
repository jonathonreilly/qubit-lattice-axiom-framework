#!/usr/bin/env python3
"""Supervisor control for block 87 (disjoint machinery: floating-point spectra and zone sums; evidence, not proof).

W1: the level rule on longer rings: the sea's energy of a wall pair on rings of 16, 64, 256 against (1 + delta) - sqrt(1 + delta^2).
W2: the three-dimensional wall tension sigma_sea(delta): the transverse average on grids of side 64, 256, 512, and its direct check as
    [E_sea(two walls across x) - E_sea(uniform)] / (2 L^2) on 8^3 and 16^3 tori; sigma_sea/delta^2 as delta -> 0; the exact value at delta = 1.
W3: block 59's law on the 8^3 torus with random rational couplings: the wall's energy per unit area against -2 alpha delta^2.
W4: the criterion alpha_c(delta) = sigma_sea/(2 delta^2), and, along block 84's balance delta*(kappa), the wall criterion at delta*.
"""
import sys
from itertools import product

import numpy as np


def h1d(L, delta, walls):
    T = np.roll(np.eye(L), -1, axis=1)
    s = np.array([1 if (not walls or x < L // 2) else -1 for x in range(L)])
    t = np.diag(1 + delta * s * (-1.0) ** np.arange(L))
    return (t @ T - T.T @ t) / 2j


def w1():
    print("W1: sea energy of a wall pair on a ring against (1 + delta) - sqrt(1 + delta^2)")
    for delta in (0.1, 0.3, 0.5, 0.9):
        row = []
        for L in (16, 64, 256):
            ew = np.linalg.eigvalsh(h1d(L, delta, True))
            eu = np.linalg.eigvalsh(h1d(L, delta, False))
            row.append(f"L={L}: {np.sum(ew[ew < 0]) - np.sum(eu[eu < 0]):.6f}")
        print(f"  delta={delta}: " + ", ".join(row) + f"; rule: {1 + delta - np.sqrt(1 + delta * delta):.6f}")


def sigma_grid(delta, L):
    k = 2 * np.pi * (np.arange(L) + 0.5) / L
    ky, kz = np.meshgrid(k, k, indexing="ij")
    e2 = np.sin(ky) ** 2 + delta ** 2 * np.cos(ky) ** 2 + np.sin(kz) ** 2 + delta ** 2 * np.cos(kz) ** 2
    return float(np.mean(np.sqrt(delta ** 2 + e2) + np.sqrt(1 + e2) - np.sqrt(e2) - np.sqrt(1 + delta ** 2 + e2)))


def sea_direct(L, delta, walls_x):
    ex = np.linalg.eigvalsh(h1d(L, delta, walls_x))
    ey = np.linalg.eigvalsh(h1d(L, delta, False))
    e2 = ex[:, None, None] ** 2 + ey[None, :, None] ** 2 + ey[None, None, :] ** 2
    return -float(np.sum(np.sqrt(e2)))


def w2():
    print("W2: wall tension sigma_sea(delta)")
    for delta in (0.01, 0.05, 0.1, 0.3, 0.5, 0.7, 1.0):
        grids = [sigma_grid(delta, L) for L in (64, 256, 512)]
        direct = [(sea_direct(L, delta, True) - sea_direct(L, delta, False)) / (2 * L * L) for L in (8, 16)]
        print(f"  delta={delta}: transverse average {grids[0]:.6f}, {grids[1]:.6f}, {grids[2]:.6f}; direct 8^3 {direct[0]:.6f}, 16^3 {direct[1]:.6f}; sigma/delta^2 = {grids[2] / delta ** 2:.4f}; alpha_c = sigma/(2 delta^2) = {grids[2] / (2 * delta ** 2):.4f}")
    print(f"  at delta = 1 exactly 2 sqrt3 - sqrt2 - 2 = {2 * np.sqrt(3) - np.sqrt(2) - 2:.6f}")


def bonds(L):
    return [(x, a) for x in product(range(L), repeat=3) for a in range(3)]


def step(x, a, d, L):
    y = list(x)
    y[a] = (y[a] + d) % L
    return tuple(y)


def law_energy(u, L, al, be, ga):
    c0 = -2 * al - 8 * be - 4 * ga
    tot = 0.0
    for (x, a) in bonds(L):
        coll = [u[(step(x, a, d, L), a)] for d in (1, -1)]
        par = [u[(step(x, l, d, L), a)] for l in range(3) if l != a for d in (1, -1)]
        perp = []
        for l in range(3):
            if l == a:
                continue
            for base in (x, step(x, a, 1, L)):
                perp.append(u[(base, l)])
                perp.append(u[(step(base, l, -1, L), l)])
        tot += u[(x, a)] * (c0 * u[(x, a)] + al * sum(coll) + be * sum(perp) + ga * sum(par))
    return -tot / 2


def pattern(L, delta, walls_x):
    return {(x, a): delta * (-1 if (a == 0 and walls_x and x[0] >= L // 2) else 1) * (-1.0) ** x[a] for (x, a) in bonds(L)}


def w3():
    print("W3: block 59's law on 8^3, random couplings: wall energy per unit area against -2 alpha delta^2")
    rng = np.random.default_rng(5)
    L = 8
    for trial in range(3):
        al, be, ga = rng.uniform(0.01, 0.3, 3)
        delta = rng.uniform(0.1, 0.9)
        d = (law_energy(pattern(L, delta, True), L, al, be, ga) - law_energy(pattern(L, delta, False), L, al, be, ga)) / (2 * L * L)
        print(f"  alpha={al:.4f} beta={be:.4f} gamma={ga:.4f} delta={delta:.3f}: per area {d:.6f} vs -2 alpha delta^2 = {-2 * al * delta ** 2:.6f}")


def w4():
    print("W4: along block 84's balance: delta*(kappa) and the wall criterion alpha_c(delta*) = sigma_sea/(2 delta*^2)")
    L = 64
    k = 2 * np.pi * (np.arange(L) + 0.5) / L
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    s2 = np.sin(kx) ** 2 + np.sin(ky) ** 2 + np.sin(kz) ** 2
    c2 = np.cos(kx) ** 2 + np.cos(ky) ** 2 + np.cos(kz) ** 2
    ds = np.linspace(0, 1, 2001)
    E = np.array([-np.mean(np.sqrt(s2 + d * d * c2)) for d in ds])
    for kap in (0.125, 0.12, 0.11, 0.10, 0.095, 0.09):
        i = int(np.argmin(E + 6 * kap * ds ** 2))
        dstar = ds[i]
        ac = sigma_grid(dstar, 256) / (2 * dstar ** 2) if dstar > 0 else float("nan")
        print(f"  kappa = alpha + 2 beta = {kap}: delta* = {dstar:.3f}; walls favoured iff alpha > {ac:.4f} (so iff beta < {(kap - ac) / 2:.4f} when kappa is held)")


def main():
    w1()
    w2()
    w3()
    w4()


if __name__ == "__main__":
    sys.exit(main())
