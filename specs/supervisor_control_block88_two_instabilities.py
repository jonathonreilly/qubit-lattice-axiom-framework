#!/usr/bin/env python3
"""Supervisor control for block 88 (disjoint machinery: floating-point spectra and zone sums; evidence, not proof).

W1: the sea's second-order response per unit modulation power to a single-axis modulation t_x = 1 + eps cos(q x) at every q = 2 pi m / L
    on rings of 48 and 96 (separable in the transverse directions): chi~(q) from chi_a/9 (q = 0, one axis) to chi/3 (q = pi), continuity at pi.
W2: the anisotropy coefficient chi_a = 9 <s_x^2 (s_y^2 + s_z^2)/|s|^3> and chi = <sum cos^2/|s|> on midpoint grids to 256^3; the thresholds
    chi/12 and chi_a/72; a direct check of the anisotropy's second-order energy on a 32^3 grid.
W3: the single-axis balance f(q) = chi~(q)/2 - alpha(1 - cos q) - 4 beta over alpha in [0, 0.3]: the maximiser is always an endpoint; the
    boundary alpha where f(pi) = f(0).
W4: the map in (alpha, beta): alternation unstable iff alpha + 2 beta < chi/12; anisotropy unstable iff beta < chi_a/72; the four regions.
"""
import sys

import numpy as np


def response_curve(L, eps=0.01):
    T = np.roll(np.eye(L), -1, axis=1)
    k = 2 * np.pi * np.arange(L) / L
    s2 = np.sin(k)[:, None] ** 2 + np.sin(k)[None, :] ** 2

    def energy(e, q):
        t = np.diag(1 + e * np.cos(q * np.arange(L)))
        ex = np.linalg.eigvalsh((t @ T - T.T @ t) / 2j)
        return -np.sum(np.sqrt(ex[:, None, None] ** 2 + s2[None, :, :])) / L ** 3

    E0 = energy(0.0, 0.0)
    qs = np.array([2 * np.pi * m / L for m in range(L // 2 + 1)])
    chi = []
    for q in qs:
        c = -(energy(eps, q) + energy(-eps, q) - 2 * E0) / eps ** 2
        power = 1.0 if (q < 1e-12 or abs(q - np.pi) < 1e-12) else 0.5
        chi.append(c / power)
    return qs, np.array(chi)


def w1():
    print("W1: response per unit power chi~(q) to a single-axis modulation")
    out = {}
    for L in (48, 96):
        qs, chi = response_curve(L)
        out[L] = (qs, chi)
        print(f"  L={L}: " + ", ".join(f"{q:.2f}: {c:.4f}" for q, c in zip(qs[:: max(1, L // 12)], chi[:: max(1, L // 12)])) + f"; at pi - 2pi/L: {chi[-2]:.4f}; at pi: {chi[-1]:.4f}")
    return out


def w2():
    print("W2: chi and chi_a on midpoint grids; thresholds; direct anisotropy check")
    for L in (64, 128, 256):
        k = 2 * np.pi * (np.arange(L) + 0.5) / L
        kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
        a, b, c = np.sin(kx) ** 2, np.sin(ky) ** 2, np.sin(kz) ** 2
        s = np.sqrt(a + b + c)
        chi = float(np.mean((np.cos(kx) ** 2 + np.cos(ky) ** 2 + np.cos(kz) ** 2) / s))
        chi_a = float(9 * np.mean(a * (b + c) / s ** 3))
        print(f"  L={L}: chi = {chi:.5f} (chi/12 = {chi / 12:.5f}); chi_a = {chi_a:.5f} (chi_a/72 = {chi_a / 72:.5f})")
    L = 32
    k = 2 * np.pi * (np.arange(L) + 0.5) / L
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    a, b, c = np.sin(kx) ** 2, np.sin(ky) ** 2, np.sin(kz) ** 2

    def E(e):
        return -float(np.mean(np.sqrt((1 + 2 * e) ** 2 * a + (1 - e) ** 2 * (b + c))))

    e = 0.01
    print(f"  direct second difference of the anisotropy's sea energy on 32^3: -(E(e) + E(-e) - 2E(0))/e^2 = {-(E(e) + E(-e) - 2 * E(0)) / e ** 2:.5f}; first difference (E(e) - E(-e))/(2e) = {(E(e) - E(-e)) / (2 * e):.2e}")


def w3(curves):
    print("W3: the single-axis balance over alpha: the maximiser of f(q) is always an endpoint")
    qs, chi = curves[96]
    interior = 0
    for alpha in np.linspace(0, 0.3, 301):
        f = chi / 2 - alpha * (1 - np.cos(qs))
        i = int(np.argmax(f))
        if 0 < i < len(qs) - 1 and f[i] > max(f[0], f[-1]) + 1e-12:
            interior += 1
    print(f"  interior maxima found: {interior} of 301 alphas; boundary alpha where f(pi) = f(0): {(chi[-1] - chi[0]) / 4:.4f}")


def w4():
    print("W4: the map in (alpha, beta) (chi = 1.5381, chi_a = 1.8827)")
    chi, chi_a = 1.5381, 1.8827
    for alpha, beta in ((0.05, 0.0), (0.05, 0.02), (0.05, 0.04), (0.10, 0.0), (0.10, 0.02), (0.15, 0.01), (0.15, 0.03)):
        alt = alpha + 2 * beta < chi / 12
        ani = beta < chi_a / 72
        print(f"  alpha={alpha:.2f} beta={beta:.2f}: alternation {'unstable' if alt else 'stable'} (alpha + 2 beta = {alpha + 2 * beta:.3f} vs {chi / 12:.3f}); anisotropy {'unstable' if ani else 'stable'} (beta vs {chi_a / 72:.4f})")


def main():
    curves = w1()
    w2()
    w3(curves)
    w4()


if __name__ == "__main__":
    sys.exit(main())
