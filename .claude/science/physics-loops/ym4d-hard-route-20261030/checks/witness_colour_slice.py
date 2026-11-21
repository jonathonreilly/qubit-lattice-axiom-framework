#!/usr/bin/env python3
"""Algebra behind the colour-general form of Theorem 3.7 of parts/witness.md.

In tilde coordinates at momenta k1 + k2 + k3 = 0, with half angles, khat = 2 sin(k / 2), D_l = diag cos(k_l / 2),
form(a1, a2, a3) = (a1, D3 a2)(Y12 . a3) + (a2, D1 a3)(Y23 . a1) + (a3, D2 a1)(Y31 . a2).
Fields: a_i^(c f) = delta^(c f) v_i / khat_i^2 + khat_i h_i^(c f), v_i . khat_i = 0, h_i a 3 x 3 matrix.
Formula (*) claimed for the contraction eps_abc eps_fgh form(a_1^(a f), a_2^(b g), a_3^(c h)):

  6 form(u1, u2, u3) + 2 sum_cyc t_l (v_i, D_l v_j) (1 / khat_i^2 - 1 / khat_j^2)
      - sum_cyc a(h_j, h_l) lam_i,   (i, j, l) = (1, 2, 3) and cyclic,

 where u_i = v_i / khat_i^2, t_l = tr h_l, a(M, N) = tr M tr N - tr(M N), lam_1 = (v1, D3 khat2), lam_2 = (v2, D1 khat3),
 lam_3 = (v3, D2 khat1). Also claimed: Y23 = D3 khat2 - D2 khat3, so (v1, Y23) = 2 lam_1, and cyclically.

PRE-REGISTERED CRITERIA (written before the first run).
 Z1 FORMULA: agreement to relative 1e-10 over 200 random samples. FAIL means the proof written from (*) is wrong.
 Z2 IDENTITY: the Y identity holds to 1e-12.
 Z3 FORM ON GRADIENTS: form(khat1, khat2, khat3) = 0 to 1e-12.
"""
from __future__ import annotations

import itertools
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np

EPS = np.zeros((3, 3, 3))
for a, b, c in itertools.permutations(range(3)):
    EPS[a, b, c] = np.linalg.det(np.eye(3)[[a, b, c]])


def form(k, a1, a2, a3):
    D = [np.cos(k[i] / 2) for i in range(3)]
    Y = lambda i, j: 2 * np.sin((k[i] - k[j]) / 2)
    return (
        np.sum(a1 * D[2] * a2) * np.sum(Y(0, 1) * a3)
        + np.sum(a2 * D[0] * a3) * np.sum(Y(1, 2) * a1)
        + np.sum(a3 * D[1] * a1) * np.sum(Y(2, 0) * a2)
    )


def main():
    rng = np.random.default_rng(11)
    d = 4
    worst_z1, worst_z2, worst_z3 = 0.0, 0.0, 0.0
    for _ in range(200):
        k = np.zeros((3, d))
        k[0] = rng.uniform(-1.5, 1.5, d)
        k[1] = rng.uniform(-1.5, 1.5, d)
        k[2] = -k[0] - k[1]
        khat = 2 * np.sin(k / 2)
        D = np.cos(k / 2)
        kh2 = np.sum(khat * khat, axis=1)
        v = []
        for i in range(3):
            w = rng.normal(size=d) + 1j * rng.normal(size=d)
            v.append(w - khat[i] * (khat[i] @ w) / kh2[i])
        h = [rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)) for _ in range(3)]
        u = [v[i] / kh2[i] for i in range(3)]

        def field(i, c, f):
            return (1.0 if c == f else 0.0) * u[i] + khat[i] * h[i][c, f]

        lhs = 0.0j
        for a, b, c in itertools.permutations(range(3)):
            for f, g, s in itertools.permutations(range(3)):
                lhs += EPS[a, b, c] * EPS[f, g, s] * form(k, field(0, a, f), field(1, b, g), field(2, c, s))

        t = [np.trace(h[i]) for i in range(3)]
        amat = lambda M, N: np.trace(M) * np.trace(N) - np.trace(M @ N)
        lam = [np.sum(v[0] * D[2] * khat[1]), np.sum(v[1] * D[0] * khat[2]), np.sum(v[2] * D[1] * khat[0])]
        rhs = 6 * form(k, u[0], u[1], u[2])
        for (i, j, l) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            rhs += 2 * t[l] * np.sum(v[i] * D[l] * v[j]) * (1 / kh2[i] - 1 / kh2[j])
            rhs -= amat(h[j], h[l]) * lam[i]
        worst_z1 = max(worst_z1, abs(lhs - rhs) / max(abs(lhs), 1e-30))

        Y23 = 2 * np.sin((k[1] - k[2]) / 2)
        worst_z2 = max(worst_z2, np.max(np.abs(Y23 - (D[2] * khat[1] - D[1] * khat[2]))))
        worst_z2 = max(worst_z2, abs(np.sum(v[0] * Y23) - 2 * lam[0]))
        worst_z3 = max(worst_z3, abs(form(k, khat[0], khat[1], khat[2])))
    print(f"Z1 {'PASS' if worst_z1 < 1e-10 else 'FAIL'}: worst relative difference {worst_z1:.2e}")
    print(f"Z2 {'PASS' if worst_z2 < 1e-12 else 'FAIL'}: worst {worst_z2:.2e}")
    print(f"Z3 {'PASS' if worst_z3 < 1e-12 else 'FAIL'}: worst {worst_z3:.2e}")


if __name__ == "__main__":
    main()
