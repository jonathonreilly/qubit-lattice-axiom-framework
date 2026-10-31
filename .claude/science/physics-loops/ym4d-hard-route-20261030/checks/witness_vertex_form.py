#!/usr/bin/env python3
"""Closed form of the lattice cubic form on plane waves, used in parts/witness.md, Theorem 3.6.

Plane waves E_i(x, mu) = a^i_mu exp(i k^i . x), sum_i k^i = 0 mod 2 pi, a^i_mu = atil^i_mu exp(i k^i_mu / 2).
V := sum over the plaquettes at one site, for mu < nu, of V_p(E_1, E_2, E_3), as defined in Text 2.1.

Claim: V = C_0 sum_cyc(i, j, l) [ sum_mu atil^i_mu atil^j_mu cos(k^l_mu / 2) ] [ sum_nu 2 sin((k^i_nu - k^j_nu) / 2) atil^l_nu ],
with one constant C_0, the same for all k and a.

PRE-REGISTERED CRITERIA (written before the first run).
 X1 FORM: over 200 random (k, a, d = 4) the ratio V / (form) is one constant to relative 1e-10. If it
    is not, the proof of Theorem 3.6 does not stand as written.
 X2 PROOF STEP: for random k with all |k^i_mu| < pi, random hyperplane normals n^1, n^2, n^3 and
    the subspaces L_1, L_2 of the proof, the contradiction quantity
    sum_nu Y_nu^2 cos(k^3_nu / 2) / (cos(k^1_nu / 2) cos(k^2_nu / 2)) is positive. Only a sanity print.
 X3 SINGLE TRIPLE: with n^3 = Y_12, n^1 = Y_23, n^2 = Y_31 the form vanishes on the product of the
    three hyperplanes, which is why one triple is not enough and the proof varies k.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np


def V_site(k, a, d=4):
    """k[i][mu], a[i][mu]; sum over plaquettes at one site with x = 0 (the total phase is 1)."""
    tot = 0.0j
    for mu in range(d):
        for nu in range(mu + 1, d):
            inc = []
            P = []
            for i in range(3):
                w_m = np.exp(1j * k[i][mu])
                w_n = np.exp(1j * k[i][nu])
                e = [a[i][mu], a[i][nu] * w_m, -a[i][mu] * w_n, -a[i][nu]]
                inc.append(e)
                P.append(sum(e))
            for s in range(4):
                for t in range(s + 1, 4):
                    M = np.array([[P[j], inc[j][s], inc[j][t]] for j in range(3)])
                    tot += np.linalg.det(M)
    return tot


def form(k, atil, d=4):
    tot = 0.0j
    for (i, j, l) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        pair = sum(atil[i][m] * atil[j][m] * np.cos(k[l][m] / 2) for m in range(d))
        vec = sum(2 * np.sin((k[i][n] - k[j][n]) / 2) * atil[l][n] for n in range(d))
        tot += pair * vec
    return tot


def main():
    rng = np.random.default_rng(5)
    d = 4
    ratios = []
    for _ in range(200):
        k = np.zeros((3, d))
        k[0] = rng.uniform(-np.pi, np.pi, d)
        k[1] = rng.uniform(-np.pi, np.pi, d)
        k[2] = -k[0] - k[1]
        atil = rng.normal(size=(3, d)) + 1j * rng.normal(size=(3, d))
        a = atil * np.exp(1j * k / 2)
        ratios.append(V_site(k, a, d) / form(k, atil, d))
    ratios = np.array(ratios)
    c0 = ratios[0]
    spread = np.max(np.abs(ratios - c0)) / abs(c0)
    print(f"X1 {'PASS' if spread < 1e-10 else 'FAIL'}: C_0 = {c0:.10f}, spread = {spread:.2e}")

    # X2, X3 on small momenta
    k = np.zeros((3, d))
    k[0] = rng.uniform(-1, 1, d)
    k[1] = rng.uniform(-1, 1, d)
    k[2] = -k[0] - k[1]
    Y = 2 * np.sin((k[0] - k[1]) / 2)
    q = np.sum(Y**2 * np.cos(k[2] / 2) / (np.cos(k[0] / 2) * np.cos(k[1] / 2)))
    print(f"X2 quantity = {q:.6f} (positive)")
    Ys = {
        (0, 1): 2 * np.sin((k[0] - k[1]) / 2),
        (1, 2): 2 * np.sin((k[1] - k[2]) / 2),
        (2, 0): 2 * np.sin((k[2] - k[0]) / 2),
    }
    worst = 0.0
    for _ in range(200):
        at = []
        for (n, j) in ((Ys[(1, 2)], 0), (Ys[(2, 0)], 1), (Ys[(0, 1)], 2)):
            v = rng.normal(size=d) + 1j * rng.normal(size=d)
            v = v - n * (n @ v) / (n @ n)
            at.append(v)
        worst = max(worst, abs(form(k, np.array(at), d)))
    print(f"X3 {'PASS' if worst < 1e-12 else 'FAIL'}: max |form| on the special hyperplanes = {worst:.2e}")


if __name__ == "__main__":
    main()
