#!/usr/bin/env python3
"""Independent NT-1 modulus-kernel rebuild.

This deliberately imports none of the worker's Python modules.  It uses the
polar form D_ov = 1 + X (X^dagger X)^(-1/2), rather than sign(H_W), and the
factorization |rho_11112| = |det D_1|^2 |det D_2|^(1/2).
"""

import sys
import time
import numpy as np


S1 = np.array([[0.0, 1.0], [1.0, 0.0]], complex)
S2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], complex)
I2 = np.eye(2, dtype=complex)


def wrap(x):
    return (x + np.pi) % (2.0 * np.pi) - np.pi


def site(x, t, T):
    return (t + T - 1) * 2 + (x % 2)


def joined_angles(uxa, uta, uxb, utb, crossing, T):
    """Return explicit directed-link angles keyed by (direction,x,t)."""
    ax, at = {}, {}
    for t in range(1, T + 1):
        for x in range(2):
            ax[(x, t)] = uxa[t - 1, x]
            ax[(x, 1 - t)] = uxb[t - 1, x]
    for t in range(1, T):
        for x in range(2):
            at[(x, t)] = uta[t - 1, x]
            at[(x, -t)] = -utb[t - 1, x]
    at[(0, 0)], at[(1, 0)] = crossing
    return ax, at


def wilson_batch(uxa, uta, uxb, utb, crossings, T, charge):
    """Massless Wilson operator, r=1, antiperiodic x, open time."""
    count = len(crossings)
    n = 8 * T
    out = np.repeat((2.0 * np.eye(n, dtype=complex))[None, :, :], count, axis=0)
    for p, crossing in enumerate(crossings):
        ax, at = joined_angles(uxa, uta, uxb, utb, crossing, T)
        for (x, t), angle in ax.items():
            a, b = 2 * site(x, t, T), 2 * site(x + 1, t, T)
            bc = -1.0 if x == 1 else 1.0
            u = bc * np.exp(1.0j * charge * angle)
            out[p, a:a+2, b:b+2] += -0.5 * (I2 - S1) * u
            out[p, b:b+2, a:a+2] += -0.5 * (I2 + S1) * np.conj(u)
        for (x, t), angle in at.items():
            a, b = 2 * site(x, t, T), 2 * site(x, t + 1, T)
            u = np.exp(1.0j * charge * angle)
            out[p, a:a+2, b:b+2] += -0.5 * (I2 - S2) * u
            out[p, b:b+2, a:a+2] += -0.5 * (I2 + S2) * np.conj(u)
    return out


def overlap_logabs_and_gap(dw):
    """Polar overlap determinant and singular gap of X=D_W-1."""
    n = dw.shape[-1]
    eye = np.eye(n, dtype=complex)
    x = dw - eye[None, :, :]
    xdx = np.conj(np.swapaxes(x, 1, 2)) @ x
    ew, ev = np.linalg.eigh(xdx)
    if np.min(ew) <= 0.0:
        raise RuntimeError("non-positive X^dagger X eigenvalue")
    invroot = (ev * (1.0 / np.sqrt(ew))[:, None, :]) @ np.conj(np.swapaxes(ev, 1, 2))
    dov = eye[None, :, :] + x @ invroot
    _, logabs = np.linalg.slogdet(dov)
    return logabs, np.sqrt(ew.min(axis=1))


def entry(uxa, uta, uxb, utb, T, order, delta=0.6):
    offset = uxb[0] - uxa[0]
    phi_total = wrap(offset.sum())
    lo, hi = max(-delta, phi_total - delta), min(delta, phi_total + delta)
    if hi <= lo:
        return 0.0, np.inf
    xg, wg = np.polynomial.legendre.leggauss(order)
    d0 = 0.5 * (hi - lo) * xg + 0.5 * (hi + lo)
    weights = 0.5 * (hi - lo) * wg
    crossings = np.column_stack([np.zeros(order), d0 - offset[0]])
    ld1, g1 = overlap_logabs_and_gap(wilson_batch(uxa, uta, uxb, utb, crossings, T, 1))
    ld2, g2 = overlap_logabs_and_gap(wilson_batch(uxa, uta, uxb, utb, crossings, T, 2))
    exponent = 2.0 * ld1 + 0.5 * ld2
    shift = exponent.max()
    value = np.exp(shift) * np.sum(weights * np.exp(exponent - shift))
    return value, min(g1.min(), g2.min())


def main():
    pool_path = sys.argv[1]
    saved_path = sys.argv[2]
    order = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    data = np.load(pool_path)
    ux, ut = data["ux"], data["ut"]
    count, T = len(ux), ux.shape[1]
    start = time.time()

    wmatch = np.max(np.abs(wrap(ux[:, 0, :].sum(axis=1))))
    max_plaq = 0.0
    for a in range(count):
        for t in range(T - 1):
            for x in range(2):
                p = ux[a, t, x] + ut[a, t, (x + 1) % 2] - ux[a, t + 1, x] - ut[a, t, x]
                max_plaq = max(max_plaq, abs(wrap(p)))
    print(f"pool={pool_path} k={count} Lt={2*T} n={order} Wmatch={wmatch:.3e} max_bulk={max_plaq:.6f}", flush=True)

    raw = np.zeros((count, count), float)
    min_gap = np.inf
    for a in range(count):
        for b in range(count):
            raw[a, b], gap = entry(ux[a], ut[a], ux[b], ut[b], T, order)
            min_gap = min(min_gap, gap)
        print(f"row {a+1}/{count} elapsed={time.time()-start:.1f}s", flush=True)
    norm = raw / np.sqrt(np.outer(np.diag(raw), np.diag(raw)))
    asym = np.max(np.abs(norm - norm.T))
    herm = 0.5 * (norm + norm.T)
    eig = np.linalg.eigvalsh(herm)
    saved = np.load(saved_path)
    saved_h = 0.5 * (saved + saved.conj().T)
    saved_eig = np.linalg.eigvalsh(saved_h)
    print(f"min_gap={min_gap:.12e} asym={asym:.3e}")
    print(f"independent_lmin={eig[0]:+.12e} lmax={eig[-1]:.12e} relative={eig[0]/eig[-1]:+.12e}")
    print(f"saved_lmin={saved_eig[0]:+.12e} lmax={saved_eig[-1]:.12e} relative={saved_eig[0]/saved_eig[-1]:+.12e}")
    print(f"max_abs_matrix_diff_vs_saved_real={np.max(np.abs(herm-saved_h.real)):.3e}")
    print("lowest_independent=" + np.array2string(eig[:5], precision=12))
    print(f"elapsed={time.time()-start:.1f}s")


if __name__ == "__main__":
    main()
