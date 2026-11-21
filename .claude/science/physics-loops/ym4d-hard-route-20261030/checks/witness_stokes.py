#!/usr/bin/env python3
"""The rectangle test: a Gaussian potential reads the far flux, the Wilson weight does not.

Geometry (parts/witness.md, Text 3). Plaquettes l(y) in the (1,2) plane at (0,0,y3,y4), y at the
corners of a D x D square in the (3,4) plane. Far loop: the (3,4) plaquette at (R, 0, c3, c4),
centred on the square for odd D. For each edge k of the square, y_k -> y_{k+1}, three lassos at
base y_k: Gamma_1 = l(y_k), Gamma_2 = sigma_k l(y_{k+1}) sigma_k^-1, Gamma_3 = tau_k l_3 tau_k^-1.

 Stk_X = sum_k K_X^(k) / P_k,  P_k = (d G d^T)(l(y_k), l(y_{k+1})), X = comp, total.

PRE-REGISTERED CRITERIA (written before the first run).
 S1 IDENTITY: Stk_comp = -24 Flux to relative 1e-9, Flux = sum over the plaquettes of the square
    of (d E_3). This is the claim K_comp^(k) = -24 E_3(sigma_k) P_k in Feynman gauge, since
    directions decouple and P(l, l_3) = 0.
 S2 WARD: |Stk_total / Stk_comp| decreases with R and is below 0.5 at R >= 8, by the Ward
    identity and the reflection in x_4. FAIL means K_total does read the far flux, and the test
    does not separate.
 S3 TAIL: K_total^(k) does not change when tau_k is replaced by another tail (relative 1e-9).
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_tree_coeff import K_comp, K_vert, Lat, check_rss, current, curl, field_E, path_links, plaq  # noqa: E402


def steps_between(a, b):
    out = []
    for mu in range(len(a)):
        n = b[mu] - a[mu]
        out += [(mu + 1) if n > 0 else -(mu + 1)] * abs(n)
    return out


def lasso_steps(tail, loop):
    return list(tail) + list(loop) + [-s for s in reversed(tail)]


def run(T, D, R):
    lat = Lat(4, T)
    c = (D - 1) // 2  # far plaquette corner, centred on the square for odd D
    far = (R, 0, c, c)
    corners = [(0, 0, 0, 0), (0, 0, D, 0), (0, 0, D, D), (0, 0, 0, D)]
    l3 = plaq(3, 4)
    E3 = field_E(lat, current(lat, path_links(lat, far, l3)))
    Es = {}
    for y in corners:
        Es[y] = field_E(lat, current(lat, path_links(lat, y, plaq(1, 2))))
    total_c, total_t, total_alt = 0.0, 0.0, 0.0
    rows = []
    for k, y in enumerate(corners):
        z = corners[(k + 1) % 4]
        sigma = steps_between(y, z)
        s1 = plaq(1, 2)
        s2 = lasso_steps(sigma, plaq(1, 2))
        tail = steps_between(y, far)
        s3 = lasso_steps(tail, l3)
        L1, L2, L3 = path_links(lat, y, s1), path_links(lat, y, s2), path_links(lat, y, s3)
        E1, E2 = Es[y], Es[z]
        kc = K_comp(lat, L1, L2, L3, E1, E2, E3)
        kv = K_vert(lat, E1, E2, E3)
        Pk = float(np.sum(current(lat, L2) * E1))
        # another tail, for S3: go along x_1 first, then transverse
        tail2 = steps_between(y, (R, 0, y[2], y[3])) + steps_between((R, 0, y[2], y[3]), far)
        L3b = path_links(lat, y, lasso_steps(tail2, l3))
        kc_b = K_comp(lat, L1, L2, L3b, E1, E2, E3)
        rows.append((k, kc, kv, kc + kv, Pk, kc_b + kv))
        total_c += kc / Pk
        total_t += (kc + kv) / Pk
        total_alt += (kc_b + kv) / Pk
    P3 = curl(lat, E3, 2, 3)
    flux = float(np.sum(P3[0, 0, 0:D, 0:D]))
    return rows, total_c, total_t, total_alt, flux


def main():
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    for D in (3, 5):
        for R in (6, 8, 12, 16):
            rows, sc, st, salt, flux = run(T, D, R)
            s1 = abs(sc + 24 * flux) / abs(24 * flux)
            s3 = abs(st - salt) / max(abs(st), 1e-30)
            print(f"D={D} R={R}: Stk_comp={sc:.6e} -24Flux={-24*flux:.6e} S1rel={s1:.1e} Stk_total={st:.6e} ratio={abs(st/sc):.4f} S3rel={s3:.1e} rss={check_rss():.2f}GB", flush=True)
            if R == 8:
                for r in rows:
                    print(f"   k={r[0]} K_comp={r[1]:.4e} K_vert={r[2]:.4e} K_total={r[3]:.4e} P={r[4]:.5e}")


if __name__ == "__main__":
    main()
