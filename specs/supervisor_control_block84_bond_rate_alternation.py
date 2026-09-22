#!/usr/bin/env python3
"""Supervisor control for block 84 (disjoint machinery: floating-point zone sums and grids; evidence, not proof).

W1: the sea's second-order coefficient chi = <sum_j cos^2 k_j / sqrt(sum_j sin^2 k_j)> over the zone on midpoint grids of side 16 to 128,
    and the single-axis coefficient chi_1 (expected chi/3); the threshold kappa_c = chi/12.
W2: the sea's energy per site E(delta) = -<sqrt(sum sin^2 + delta^2 sum cos^2)> (T1's closed form) against delta, and the balance
    E(delta) + 6 kappa delta^2 minimised over delta for kappa across the window: delta*, the rest energy sqrt(3) delta*, the gain;
    the runaway value kappa_run below which delta* = 1.
W3: with the axioms' scalar hop timed by the same bond rates (block 82's 16 x 16 blocks): the least |E| over the zone against delta for
    a in {1/20, 1/10, 1/4}, against the corner crossing delta = 2a.
"""
import sys

import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
SIG = [SX, SY, SZ]


def zone(L):
    k = 2 * np.pi * (np.arange(L) + 0.5) / L
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    s2 = np.sin(kx) ** 2 + np.sin(ky) ** 2 + np.sin(kz) ** 2
    c2 = np.cos(kx) ** 2 + np.cos(ky) ** 2 + np.cos(kz) ** 2
    return s2, c2, np.cos(kx) ** 2


def w1():
    print("W1: chi and chi_1 on midpoint grids; threshold kappa_c = chi/12")
    last = None
    for L in (16, 32, 64, 96, 128):
        s2, c2, cx2 = zone(L)
        chi = float(np.mean(c2 / np.sqrt(s2)))
        chi1 = float(np.mean(cx2 / np.sqrt(s2)))
        print(f"  L={L}: chi = {chi:.5f}, chi_1 = {chi1:.5f} (chi/3 = {chi / 3:.5f}); kappa_c = chi/12 = {chi / 12:.5f}")
        last = chi
    return last


def w2(chi):
    print("W2: E(delta) per site and the balance E(delta) + 6 kappa delta^2 (kappa = alpha + 2 beta)")
    s2, c2, _ = zone(64)
    ds = np.linspace(0, 1, 4001)
    E = np.array([-np.mean(np.sqrt(s2 + d * d * c2)) for d in ds])
    print("  E(delta): " + ", ".join(f"{d:g}: {E[int(d * 4000)]:.5f}" for d in (0, 0.1, 0.2, 0.4, 0.7, 1.0)))
    print(f"  second-difference estimate of -E''(0): {-(E[40] - 2 * E[0] + E[0]) / (0.01 ** 2) * 1:.4f} (chi = {chi:.4f}); E(1) - E(0) = {E[-1] - E[0]:.5f}")
    kappa_run = -(E[-1] - E[0]) / 6
    print(f"  runaway: delta* = 1 whenever 6 kappa < -(E(1) - E(0)), i.e. kappa < {kappa_run:.5f}")
    for kap in (0.20, 0.13, 0.128, 0.125, 0.12, 0.11, 0.10, 0.095, 0.09, 0.085, 0.06, 0.0):
        tot = E + 6 * kap * ds ** 2
        i = int(np.argmin(tot))
        print(f"  kappa = {kap:.3f}: delta* = {ds[i]:.4f}, rest energy sqrt3 delta* = {np.sqrt(3) * ds[i]:.4f}, gain per site {tot[i] - tot[0]:.5f}")


def place(mat, j):
    fs = [I2, I2, I2]
    fs[j] = mat
    return np.kron(I2, np.kron(fs[0], np.kron(fs[1], fs[2])))


def coin(mat):
    return np.kron(mat, np.eye(8, dtype=complex))


def block16(k, delta, a):
    H = np.zeros((16, 16), dtype=complex)
    for j in range(3):
        s, c = np.sin(k[j]), np.cos(k[j])
        H += coin(SIG[j]) @ place(-s * SZ + delta * c * SY, j)
        H += place(2 * a * (c * SZ + delta * s * SY), j)
    return H


def w3():
    print("W3: least |E| over the zone (grid 20^3) with the scalar hop timed by the same bond rates; corner crossing at delta = 2a")
    grid = np.linspace(0, np.pi, 20)
    for a in (0.05, 0.1, 0.25):
        row = []
        for delta in (0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7):
            least = 9.0
            for kx in grid:
                for ky in grid:
                    for kz in grid:
                        ev = np.linalg.eigvalsh(block16((kx, ky, kz), delta, a))
                        least = min(least, float(np.min(np.abs(ev))))
            row.append(f"delta={delta:g}: {least:.4f}")
        print(f"  a={a:g} (2a = {2 * a:g}): " + "; ".join(row))


def main():
    chi = w1()
    w2(chi)
    w3()


if __name__ == "__main__":
    sys.exit(main())
