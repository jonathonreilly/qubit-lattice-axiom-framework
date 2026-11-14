#!/usr/bin/env python3
"""T8 of CRITERIA.md: one-dimensional lift kernels T0, T1 and their constants."""
import numpy as np


def cubic_bspline(u):
    u = abs(u)
    if u < 1:
        return 2 / 3 - u**2 + u**3 / 2
    if u < 2:
        return (2 - u) ** 3 / 6
    return 0.0


def build(L, Nc=30):
    """Periodic: fine n = L Nc, coarse sites y = L j. Returns matrix T0[x, j]."""
    n = L * Nc
    r = (L - 1) // 2
    xs = np.arange(n)

    def d(x, y):
        return ((x - y + n / 2) % n) - n / 2

    Xi = np.array([[cubic_bspline(d(x, L * j) / L) for j in range(Nc)] for x in xs])
    beta_raw = np.array([(1 - (2 * s / (L + 1)) ** 2) ** 2 for s in range(-r, r + 1)])
    beta_raw *= L / beta_raw.sum()
    Beta = np.zeros((n, Nc))
    for j in range(Nc):
        for k, s in enumerate(range(-r, r + 1)):
            Beta[(L * j + s) % n, j] = beta_raw[k]
    R0 = np.zeros((Nc, n))
    for j in range(Nc):
        for s in range(-r, r + 1):
            R0[j, (L * j + s) % n] = 1 / L
    T0 = Xi + Beta @ (np.eye(Nc) - R0 @ Xi)
    return n, Nc, T0, R0


def main():
    prev = None
    for L in (3, 5, 7, 9, 21):
        n, Nc, T0, R0 = build(L)
        err_id = np.abs(R0 @ T0 - np.eye(Nc)).max()
        err_const = np.abs(T0.sum(1) - 1).max()
        # affine reproduction away from the periodic seam
        y = np.arange(Nc) * L - n / 2
        x = np.arange(n) - n / 2
        lin = T0 @ y
        mask = (x > -n / 2 + 4 * L) & (x < n / 2 - 4 * L)
        err_lin = np.abs(lin - x)[mask].max()
        # eta_c(x), c = (y_j, y_j + L): from dT0 omega = T1 d omega, open sum from the right of j, centred in the middle
        dz = np.roll(T0, -1, axis=0) - T0  # [x, j]
        mid = Nc // 2
        eta = np.zeros((n, Nc))
        for j in range(Nc):
            # sum over j'' = j + 1 ... j + Nc//2 cyclically, restricted to x near j
            for s in range(1, Nc // 2):
                eta[:, j] += dz[:, (j + s) % Nc]
        # kernel restricted near the bond: zero it far away
        for j in range(Nc):
            for xx in range(n):
                dist = ((xx - L * j - L / 2 + n / 2) % n) - n / 2
                if abs(dist) > 6.5 * L:
                    eta[xx, j] = 0
        err_sum = np.abs(eta.sum(1) - 1 / L).max()
        # R1 T1 = id
        R1 = np.zeros((Nc, n))
        r = (L - 1) // 2
        for j in range(Nc):
            for a in range(-r, r + 1):
                for s in range(L):
                    R1[j, (L * j + a + s) % n] += 1 / L
        err_R1 = np.abs(R1 @ eta - np.eye(Nc)).max()
        c_z = L * np.abs(dz).max()
        de = np.roll(eta, -1, axis=0) - eta
        c_e = L**2 * np.abs(de).max()
        c_e0 = L * np.abs(eta).max()
        print(f"L {L}: R0T0 {err_id:.1e} const {err_const:.1e} lin {err_lin:.1e} sum eta {err_sum:.1e} R1T1 {err_R1:.1e} | L|grad zeta| {c_z:.3f} L|eta| {c_e0:.3f} L^2|grad eta| {c_e:.3f} sup|zeta| {np.abs(T0).max():.3f} l1 row zeta {np.abs(T0).sum(1).max():.3f} l1 row eta*L {L*np.abs(eta).sum(1).max():.3f}", flush=True)


if __name__ == "__main__":
    main()
