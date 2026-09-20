#!/usr/bin/env python3
"""Block 42 control (floating point; not the runner): the full nonlinear self-consistent odds around one held record.

Part 1  six outcomes: the lean v_z(r) along an axis against the screened lattice Green function, at screened triples and on the massless surface.
Part 2  seven outcomes ('no record' among the possibilities): the density excess around a held record at the neutral scale (g = 1) and with glue (g > 1).
Part 3  bodies of agreeing records: the far lean of cubes of 1, 8, 27, 64 records and of 8 records spaced 4 apart, against one record.
"""
import itertools
import numpy as np


def green(L, m2):
    k = 2 * np.pi * np.arange(L) / L
    E = 6 - 2 * (np.cos(k)[:, None, None] + np.cos(k)[None, :, None] + np.cos(k)[None, None, :])
    D = E + m2
    if m2 == 0:
        D[0, 0, 0] = np.inf
    return np.real(np.fft.ifftn(1.0 / D))


def solve6(p, q, r, L, iters=60000, tol=1e-13, body=((0, 0, 0),)):
    om = np.array([[p if a == b else q if a == (b ^ 1) else r for b in range(6)] for a in range(6)], float)
    pi = np.full((L, L, L, 6), 1 / 6.0)
    rec = np.zeros(6)
    rec[0] = 1.0
    mask = np.zeros((L, L, L), bool)
    for site in body:
        mask[tuple(site)] = True
    for it in range(iters):
        pi[mask] = rec
        logp = np.zeros_like(pi)
        for d in range(3):
            for sgn in (1, -1):
                logp += np.log(np.roll(pi, sgn, axis=d) @ om.T)
        new = np.exp(logp - logp.max(axis=-1, keepdims=True))
        new /= new.sum(axis=-1, keepdims=True)
        new[mask] = rec
        err = np.abs(new - pi).max()
        pi = new
        if err < tol:
            break
    pi[mask] = rec
    return pi[..., 0] - pi[..., 1], it + 1


def solve7(p, q, r, g, rho, L, iters=20000, tol=1e-13):
    om = np.array([[p if a == b else q if a == (b ^ 1) else r for b in range(6)] for a in range(6)], float)
    c = g * 6.0 / (p + q + 4 * r)
    z = rho / (6 * (1 - rho) * (1 + rho * (g - 1)) ** 6)
    pi = np.zeros((L, L, L, 7))
    pi[..., :6] = rho / 6
    pi[..., 6] = 1 - rho
    rec = np.zeros(7)
    rec[0] = 1.0
    for it in range(iters):
        pi[0, 0, 0] = rec
        logp = np.zeros_like(pi)
        logp[..., :6] = np.log(z)
        for d in range(3):
            for sgn in (1, -1):
                nb = np.roll(pi, sgn, axis=d)
                logp[..., :6] += np.log(nb[..., 6:7] + c * (nb[..., :6] @ om.T))
        new = np.exp(logp - logp.max(axis=-1, keepdims=True))
        new /= new.sum(axis=-1, keepdims=True)
        new[0, 0, 0] = rec
        err = np.abs(new - pi).max()
        pi = new
        if err < tol:
            break
    pi[0, 0, 0] = rec
    return 1 - pi[..., 6] - rho, pi[..., 0] - pi[..., 1], it + 1


if __name__ == "__main__":
    print("PART 1: six outcomes, one record (+z) at the origin; lean ratio v_z(r)/v_z(1) against G_m(r)/G_m(1)")
    for (p, q, r, L) in ((2.5, 1, 2, 15), (5, 2, 4, 15), (2.9, 1, 2, 21)):
        l1 = (p - q) / (p + q + 4 * r)
        m2 = (1 - 6 * l1) / l1
        vz, its = solve6(p, q, r, L)
        G = green(L, m2)
        print(f"  ({p},{q},{r}) side {L}: 6 l1 = {6 * l1:.3f}, m^2 = {m2:.3f}, range {m2 ** -0.5:.2f}, iterations {its}: " + "  ".join(f"r={k}: {vz[k, 0, 0] / vz[1, 0, 0]:.4f}|{G[k, 0, 0] / G[1, 0, 0]:.4f}" for k in (2, 3, 4, 5, 6)))
    print("  on the massless surface, (3,1,2): r * v_z(r) along an axis (a pure one-over-distance field would give a constant)")
    for L in (15, 21, 27):
        vz, its = solve6(3, 1, 2, L)
        print(f"  side {L}, iterations {its}: " + "  ".join(f"r={k}: {k * vz[k, 0, 0]:.4f}" for k in (1, 2, 3, 4, 5, 6, 7)))
    print("PART 2: seven outcomes, background density 0.3, (5,2,4): density excess around a held record, and the vector lean")
    for g in (1.0, 1.5, 2.0):
        rho = 0.3
        l1 = 3 / 23
        lam_s = rho * (1 - rho) * (g - 1) / (1 + rho * (g - 1))
        lam_v = rho * g * l1 / (1 + rho * (g - 1))
        dr, vz, its = solve7(5, 2, 4, g, rho, 15)
        msg = f"  g = {g}: scalar strength {lam_s:.4f} (6x = {6 * lam_s:.3f}), vector strength {lam_v:.4f}; density excess at r = 1..4: " + " ".join(f"{dr[k, 0, 0]:+.2e}" for k in (1, 2, 3, 4))
        if lam_s > 0:
            G = green(15, (1 - 6 * lam_s) / lam_s)
            msg += "; ratio to r=1 against the screened Green function: " + " ".join(f"{dr[k, 0, 0] / dr[1, 0, 0]:.4f}|{G[k, 0, 0] / G[1, 0, 0]:.4f}" for k in (2, 3, 4))
        print(msg)
    print("PART 3: bodies of agreeing records (+z), side 25: lean at 5, 7, 9 steps beyond the face, as a multiple of one record's")
    for (p, q, r) in ((2.95, 1, 2), (2.5, 1, 2)):
        l1 = (p - q) / (p + q + 4 * r)
        base = None
        for side in (1, 2, 3, 4):
            body = list(itertools.product(range(side), repeat=3))
            vz, its = solve6(p, q, r, 25, tol=1e-12, body=body)
            far = [vz[side - 1 + d, 0, 0] for d in (5, 7, 9)]
            base = base or far
            print(f"  ({p},{q},{r}) range {((1 - 6 * l1) / l1) ** -0.5:.2f}: cube of {side ** 3:2d} records: " + " ".join(f"{v / b:.2f}" for v, b in zip(far, base)))
        body = [tuple(4 * k for k in cc) for cc in itertools.product(range(2), repeat=3)]
        vz, its = solve6(p, q, r, 25, tol=1e-12, body=body)
        far = [vz[4 + d, 0, 0] for d in (5, 7, 9)]
        print(f"  ({p},{q},{r}): 8 records spaced 4 apart: " + " ".join(f"{v / b:.2f}" for v, b in zip(far, base)))
