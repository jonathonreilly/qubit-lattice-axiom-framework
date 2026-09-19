#!/usr/bin/env python3
"""J:note falsifier for U1_RECORD_FACE_LIKELIHOOD_SPATIAL_GAUGE_AND_PHOTON_GERM (on main).

Falsifier implemented (the note's Falsifiers section): "the orientation-complete positive spatial Hessian lacks exactly two positive transverse
directions at nonzero momentum" (and, with it, the rotor frequencies sqrt(alpha kappa P) on both transverse directions).

The note's runner checks the Fourier formula K_ij = kappa (P delta_ij - q_i q_j) at every nonzero momentum on L = 3, 4, 5, 7. Here, beyond
those sizes and with disjoint machinery, the Hessian of S = sum_f V(Phi_f) at the flat connection is built in REAL SPACE from the face-link
incidence on the L^3 torus, Phi_f = l_mu(X) + l_nu(X + e_mu) - l_mu(X + e_nu) - l_nu(X) for every face (X, mu < nu): Hess = kappa B^T B.
  1. L = 6 and L = 8: the full spectrum of B^T B (3L^3 x 3L^3, dense) against the multiset {0 x (L^3 + 2)} u {E(k) x 2 : k != 0},
     E(k) = sum_j 2(1 - cos k_j);
  2. L = 6: B^T B projected onto the plane waves of each momentum k (a 3x3 block computed from the real-space matrix): exactly two positive
     eigenvalues, both equal to E(k), and the null vector along q_j = e^{ik_j} - 1, at every nonzero k;
  3. controls: dropping one face orientation (the (0,1) faces) leaves momenta with ONE positive direction; weighting it 2 splits the two.
"""
from __future__ import annotations

import itertools

import numpy as np


def incidence(L, weights=(1.0, 1.0, 1.0)):
    N = L ** 3
    idx = lambda x: ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
    link = lambda x, mu: 3 * idx(x) + mu
    pairs = [(0, 1), (0, 2), (1, 2)]
    rows = []
    for X in itertools.product(range(L), repeat=3):
        for w, (mu, nu) in zip(weights, pairs):
            if w == 0:
                continue
            e_mu = tuple(1 if i == mu else 0 for i in range(3))
            e_nu = tuple(1 if i == nu else 0 for i in range(3))
            r = np.zeros(3 * N)
            s = np.sqrt(w)
            r[link(X, mu)] += s
            r[link(tuple(a + b for a, b in zip(X, e_mu)), nu)] += s
            r[link(tuple(a + b for a, b in zip(X, e_nu)), mu)] -= s
            r[link(X, nu)] -= s
            rows.append(r)
    return np.array(rows)


def spectrum_check(L):
    B = incidence(L)
    H = B.T @ B
    ev = np.sort(np.linalg.eigvalsh(H))
    ks = [2 * np.pi * np.array(n) / L for n in itertools.product(range(L), repeat=3)]
    pred = [0.0] * 3                                  # k = 0: three constant link modes
    for k in ks:
        if np.allclose(k, 0):
            continue
        E = float(np.sum(2 * (1 - np.cos(k))))
        pred += [0.0, E, E]                             # one gauge zero mode, two transverse
    pred = np.sort(np.array(pred))
    return np.max(np.abs(ev - pred)), int(np.sum(np.abs(ev) < 1e-9)), L ** 3 + 2


def block(H, L, n):
    N = L ** 3
    k = 2 * np.pi * np.array(n) / L
    xs = np.array(list(itertools.product(range(L), repeat=3)))
    ph = np.exp(1j * xs @ k) / np.sqrt(N)
    V = np.zeros((3 * N, 3), dtype=complex)
    for mu in range(3):
        V[mu::3, mu] = ph
    M = V.conj().T @ (H @ V)
    return k, (M + M.conj().T) / 2


def block_check(L, weights=(1.0, 1.0, 1.0)):
    B = incidence(L, weights)
    H = B.T @ B
    two_pos = one_pos = 0
    worst_E = 0.0
    worst_null = 0.0
    split = 0
    for n in itertools.product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        k, M = block(H, L, n)
        ev = np.linalg.eigvalsh(M)
        pos = int(np.sum(ev > 1e-9))
        E = float(np.sum(2 * (1 - np.cos(k))))
        if pos == 2:
            two_pos += 1
        elif pos == 1:
            one_pos += 1
        if weights == (1.0, 1.0, 1.0):
            worst_E = max(worst_E, float(np.max(np.abs(np.sort(ev)[1:] - E))))
            q = np.exp(1j * k) - 1
            # a pure gauge l_mu(x) = lam(x + e_mu) - lam(x) with lam = e^{ik.x} has plane-wave coefficients q_mu: the block's null vector
            worst_null = max(worst_null, float(np.linalg.norm(M @ q) / np.linalg.norm(q)))
        else:
            srt = np.sort(ev)
            if pos == 2 and abs(srt[2] - srt[1]) > 1e-9:
                split += 1
    return two_pos, one_pos, worst_E, worst_null, split


def main():
    ok_spec = True
    for L in (6, 8):
        dev, zeros, zpred = spectrum_check(L)
        ok_spec &= dev < 1e-8 and zeros == zpred
        print(f"1. L={L}: real-space B^T B ({3 * L ** 3} links) spectrum vs {{0 x (L^3+2)}} u {{E(k) x 2}}: max deviation {dev:.2e}; zero "
              f"eigenvalues {zeros} (predicted {zpred})")
    two, one, wE, wn, _ = block_check(6)
    print(f"2. L=6 momentum blocks from the real-space matrix: {two} of {6 ** 3 - 1} nonzero momenta have exactly two positive directions "
          f"({one} have one); max |transverse eigenvalue - E(k)| = {wE:.2e}; max |block * q|/|q| (gauge null vector) = {wn:.2e}")
    two_m, one_m, _, _, _ = block_check(6, (0.0, 1.0, 1.0))
    two_u, one_u, _, _, split = block_check(6, (2.0, 1.0, 1.0))
    print(f"3. controls on L=6: (0,1) faces dropped -> {one_m} momenta with one positive direction, {two_m} with two; (0,1) faces weighted 2 -> "
          f"{split} momenta with split transverse eigenvalues")
    ok = ok_spec and two == 6 ** 3 - 1 and one == 0 and wE < 1e-9 and wn < 1e-9 and one_m > 0 and split > 0
    if ok:
        print("SUMMARY: falsifier 'the orientation-complete Hessian lacks exactly two positive transverse directions at nonzero momentum' does "
              "not fire beyond the note's sizes: on L = 6 and 8 the real-space face-incidence Hessian B^T B has spectrum {0 x (L^3+2)} u "
              "{E(k) x 2} exactly (to 1e-8), and on L = 6 every one of the 215 nonzero momentum blocks has exactly two positive eigenvalues, "
              "both E(k) (so rotor frequencies sqrt(alpha kappa E(k)) on both), with the gauge null vector; dropping or reweighting one "
              "orientation breaks this as the note's controls say")
    else:
        print(f"HIT: the transverse-Hessian falsifier fires: spectrum {ok_spec}, two-positive {two}/{6 ** 3 - 1}, one-positive {one}, "
              f"E deviation {wE}, null {wn}, controls {one_m}/{split}")
        print("SUMMARY: falsifier fired; see the lines above")


if __name__ == "__main__":
    main()
