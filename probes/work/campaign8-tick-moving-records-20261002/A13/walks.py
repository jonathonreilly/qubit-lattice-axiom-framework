#!/usr/bin/env python3
"""A13 check 2: the two kinds of things in the assembled model (supplied toy).

(a) A readable record (option A: each step re-forms with the cut) on the cycled pairing moves with the classical
    kernel |G|^2: within its current pair, stay 1-s, move s (s = sin^2 theta).  Derived here (EXACT):
    move -> next partner lies in the same direction; stay -> next partner lies in the opposite direction, so
    E[x_T^2] = T s + 2 sum_{k=1}^{T-1} (T-k) s^2 (2s-1)^{k-1}  ->  T s/(1-s);  zero drift at long times.
    Compared against exact propagation of the probability vector (1D brickwork) and of the 3D six-layer cycle.
(b) An unrecorded excitation on the same layers (coherent): <x^2> grows like t^2 (ballistic, interferes).
"""
import numpy as np


def formula_x2(T, s):
    k = np.arange(1, T)
    return T * s + 2 * np.sum((T - k) * s * s * (2 * s - 1) ** (k - 1))


def classical_1d(L, x0, T, s):
    p = np.zeros(L); p[x0] = 1.0
    xs = np.arange(L) - x0
    out = {}
    for t in range(1, T + 1):
        start = (x0 % 2) if t % 2 == 1 else 1 - (x0 % 2)      # tick 1 pairs the start site with its right neighbour
        i = np.arange(start, L - 1, 2)
        j = i + 1
        pi, pj = p[i].copy(), p[j].copy()
        p[i] = (1 - s) * pi + s * pj
        p[j] = (1 - s) * pj + s * pi
        out[t] = (np.dot(p, xs), np.dot(p, xs ** 2))
    return out


def coherent_1d(L, x0, T, theta):
    psi = np.zeros(L, complex); psi[x0] = 1.0
    xs = np.arange(L) - x0
    c, sn = np.cos(theta), np.sin(theta)
    out = {}
    for t in range(1, T + 1):
        start = (x0 % 2) if t % 2 == 1 else 1 - (x0 % 2)
        i = np.arange(start, L - 1, 2)
        j = i + 1
        a, b = psi[i].copy(), psi[j].copy()
        # one-excitation block of exp(-i theta SWAP): cos - i sin sigma_x  (relative to the empty pair)
        psi[i] = c * a - 1j * sn * b
        psi[j] = c * b - 1j * sn * a
        pr = np.abs(psi) ** 2
        out[t] = (np.dot(pr, xs), np.dot(pr, xs ** 2))
    return out


def classical_3d(C, s):
    """Six-layer cycle x-even, x-odd, y-even, y-odd, z-even, z-odd; record starts at the origin (even site)."""
    R = 2 * C + 2
    L = 2 * R + 2                 # even size, origin at index R (R even keeps parities aligned)
    p = np.zeros((L, L, L)); p[R, R, R] = 1.0
    coords = np.arange(L) - R
    for cyc in range(C):
        for axis in range(3):
            for par in (0, 1):
                q = np.moveaxis(p, axis, 0)
                i = np.arange(0, L - 1)
                i = i[(coords[i] % 2) == par]
                j = i + 1
                qi, qj = q[i].copy(), q[j].copy()
                q[i] = (1 - s) * qi + s * qj
                q[j] = (1 - s) * qj + s * qi
                p = np.moveaxis(q, 0, axis)
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing='ij')
    r2 = np.sum(p * (X ** 2 + Y ** 2 + Z ** 2))
    return r2, p.sum()


def main():
    for theta in (0.3, 0.6, np.pi / 4, 1.2):
        s = np.sin(theta) ** 2
        L, x0, T = 1201, 600, 400
        cl = classical_1d(L, x0, T, s)
        co = coherent_1d(L, x0, T, theta)
        err = max(abs(cl[t][1] - formula_x2(t, s)) for t in (1, 2, 3, 10, 57, 400))
        print(f"theta={theta:.4f} s={s:.4f}: record E[x^2]: formula vs exact chain max |diff| = {err:.1e}; "
              f"E[x^2]/T at T=400: {cl[400][1]/400:.4f} (s/(1-s) = {s/(1-s):.4f}); mean drift at T=400: {cl[400][0]:.4f} "
              f"(limit s/(2(1-s)) = {s/(2*(1-s)):.4f})")
        print(f"      unrecorded excitation <x^2>/t^2 at t=100,200,400: "
              f"{co[100][1]/1e4:.4f}, {co[200][1]/4e4:.4f}, {co[400][1]/16e4:.4f};  record <x^2>/t: "
              f"{cl[100][1]/100:.4f}, {cl[200][1]/200:.4f}, {cl[400][1]/400:.4f}")
    # 3D: the six-layer cycle factorizes into three 1D walks (2 axis ticks per cycle)
    for theta in (0.6, np.pi / 4):
        s = np.sin(theta) ** 2
        C = 20
        r2, tot = classical_3d(C, s)
        pred = 3 * formula_x2(2 * C, s)
        print(f"3D cycle theta={theta:.4f}: E[r^2] after {C} cycles = {r2:.6f}, 3 x 1D formula(2C) = {pred:.6f}, "
              f"|diff| = {abs(r2-pred):.1e}, prob conserved to {abs(tot-1):.1e}; per tick -> {r2/(6*C):.4f} "
              f"(asymptote per tick s/(1-s) = {s/(1-s):.4f})")


if __name__ == '__main__':
    main()
