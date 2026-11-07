#!/usr/bin/env python3
"""Abelian lift form q_n against the level-lattice curvature energy (hard-core--independent, Text 7.1, 9.4).

Exact reduction used. With Q_str diagonal in the direction index and Feynman fine form ||grad A||^2, the coarse Feynman
covariance is diagonal: G_mu(P) = sum over aliases m in Z_n^4 of |Qhat_mu(p_m)|^2 / phat(p_m)^2 / n^4, p_m = (P + 2 pi m) / n, with
Qhat_mu(p) = n prod_i D_n(p_i) D_n(p_mu), D_n(p) = sin(n p / 2) / (n sin(p / 2)). As n -> infinity,
G_mu(P) = sum_{m in Z^4} prod_i sinc^2(k_i / 2) sinc^2(k_mu / 2) / k^2, k = P + 2 pi m.
Landau differs from Feynman on the coarse level only by a coarse gradient, so q_n(B) = min_lambda (B + chat lambda)^* G^{-1} (B + chat lambda), with chat_mu = exp(i P_mu) - 1.
D(B) = ||d_j B||^2 = sum_{mu < nu} |chat_mu B_nu - chat_nu B_mu|^2. Both forms vanish on B = chat, so compare them on its complement.

PRE-STATED CRITERIA (written before the first run).
  R(P) = eigenvalues of q_n relative to D on the complement of chat, at each P != 0.
  PASS-LOWER (Lemma 7.1): min R >= 1 - 1e-9 at n = 1, 3, 9 and for the n = infinity sum, up to its truncation error, which is bounded by
              comparing cutoffs: allow 1 - 1e-3 at n = infinity. FAIL-LOWER: below that. That would falsify Lemma 7.1.
  PASS-UPPER: C_I(n) = max R is finite and stable: C_I(infinity) from cutoffs 8 and 12 agree within 1 percent, the maximum over a grid of
              spacing 2 pi / 17 and over 4000 random P agree within 5 percent, and C_I(n) is monotone or stable from n = 3 to 9 to infinity.
  FAIL-UPPER: C_I grows on grid refinement near some P. That would falsify the upper bound consumed by 9.4 and 9.5.
  REPORT: C_I(n), and the limit of R as P -> 0, which must tend to 1 since (R4) reproduces constant curvature exactly.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1", MKL_NUM_THREADS="1")
import resource, sys
import numpy as np

RSS_LIMIT_GB = 2.0


def check_rss():
    gb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3
    if gb > RSS_LIMIT_GB:
        sys.exit(f"RSS {gb:.2f} GB above limit")


def Dn(p, n):
    # D_n(p) = sin(n p / 2) / (n sin(p / 2)), with D_n -> 1 at p = 0 mod 2 pi, up to sign handled by squares
    s = np.sin(p / 2)
    out = np.ones_like(p)
    mask = np.abs(s) > 1e-14
    out[mask] = np.sin(n * p[mask] / 2) / (n * s[mask])
    return out


def G_finite(P, n):
    grids = [(P[i] + 2 * np.pi * np.arange(n)) / n for i in range(4)]
    d2 = [Dn(g, n) ** 2 for g in grids]
    ph2 = [2 - 2 * np.cos(g) for g in grids]
    D = d2[0][:, None, None, None] * d2[1][None, :, None, None] * d2[2][None, None, :, None] * d2[3][None, None, None, :]
    den = ph2[0][:, None, None, None] + ph2[1][None, :, None, None] + ph2[2][None, None, :, None] + ph2[3][None, None, None, :]
    den = np.where(den < 1e-300, np.inf, den)
    base = D / den
    out = np.zeros(4)
    for mu in range(4):
        shape = [1, 1, 1, 1]
        shape[mu] = n
        # G_mu = n^-4 sum_m |Qhat_mu|^2 / phat^2 and |Qhat_mu|^2 = n^2 prod D^2 D_mu^2, so the prefactor is n^-2
        out[mu] = np.sum(base * d2[mu].reshape(shape)) / n ** 2
    return out


def G_infinite(P, cutoff):
    ms = 2 * np.pi * np.arange(-cutoff, cutoff + 1)
    k = [P[i] + ms for i in range(4)]
    s2 = [np.sinc(ki / (2 * np.pi)) ** 2 for ki in k]  # np.sinc(x) = sin(pi x) / (pi x)
    D = s2[0][:, None, None, None] * s2[1][None, :, None, None] * s2[2][None, None, :, None] * s2[3][None, None, None, :]
    den = (k[0] ** 2)[:, None, None, None] + (k[1] ** 2)[None, :, None, None] + (k[2] ** 2)[None, None, :, None] + (k[3] ** 2)[None, None, None, :]
    base = D / den
    out = np.zeros(4)
    for mu in range(4):
        shape = [1, 1, 1, 1]
        shape[mu] = 2 * cutoff + 1
        out[mu] = np.sum(base * s2[mu].reshape(shape))
    return out


def ratios(P, G):
    chat = np.exp(1j * P) - 1
    nc = np.linalg.norm(chat)
    if nc < 1e-9:
        return None
    # orthonormal basis of the complement of chat
    q, _ = np.linalg.qr(np.column_stack([chat, np.eye(4, dtype=complex)]))
    B = q[:, 1:4]
    Ginv = np.diag(1.0 / G)
    # q_n: Schur complement of the G^{-1} form over the coarse gauge direction
    Sch = Ginv - (Ginv @ chat[:, None]) @ (chat.conj()[None, :] @ Ginv) / (chat.conj() @ Ginv @ chat)
    A = B.conj().T @ Sch @ B
    Dform = nc ** 2 * np.eye(4, dtype=complex) - np.outer(chat, chat.conj())
    Dm = B.conj().T @ Dform @ B
    L = np.linalg.cholesky(Dm)
    Li = np.linalg.inv(L)
    ev = np.linalg.eigvalsh(Li @ A @ Li.conj().T)
    return ev


def scan(Gfun, Ps):
    lo, hi, Plo, Phi = np.inf, -np.inf, None, None
    for i, P in enumerate(Ps):
        ev = ratios(P, Gfun(P))
        if ev is None:
            continue
        if ev[0] < lo:
            lo, Plo = ev[0], P
        if ev[-1] > hi:
            hi, Phi = ev[-1], P
        if i % 500 == 0:
            check_rss()
    return lo, hi, Plo, Phi


def main():
    rng = np.random.default_rng(20261030)
    axis = (np.arange(1, 9) * 2 * np.pi / 17)  # one octant; G depends on |P_mu| and is permutation covariant
    grid = np.array(np.meshgrid(axis, axis, axis, axis, indexing="ij")).reshape(4, -1).T
    grid = grid[np.all(np.diff(grid, axis=1) >= 0, axis=1)]  # sorted representatives
    rand = rng.uniform(-np.pi, np.pi, size=(4000, 4))
    edge = np.array([[np.pi, 1e-3, 1e-3, 1e-3], [np.pi, np.pi, 1e-3, 1e-3], [np.pi, np.pi, np.pi, 1e-3], [np.pi, np.pi, np.pi, np.pi], [1e-3, 1e-3, 1e-3, 1e-3], [0.05, 0.0, 0.0, 0.0], [0.05, 0.05, 0.0, 0.0]])
    print(f"grid points {len(grid)}, random 4000, edge {len(edge)}", flush=True)
    for n in (1, 3, 9):
        f = lambda P, n=n: G_finite(P, n)
        lo, hi, Plo, Phi = scan(f, np.vstack([grid, edge]))
        print(f"n={n}: grid min R={lo:.9f} max R={hi:.6f} at P={np.round(Phi, 3)}", flush=True)
        lo2, hi2, _, _ = scan(f, rand[:800] if n == 9 else rand)
        print(f"n={n}: random min R={lo2:.9f} max R={hi2:.6f}", flush=True)
    for cutoff in (8, 12):
        f = lambda P, c=cutoff: G_infinite(P, c)
        lo, hi, Plo, Phi = scan(f, np.vstack([grid, edge]))
        print(f"n=inf cutoff={cutoff}: grid min R={lo:.9f} at P={np.round(Plo, 3)} max R={hi:.6f} at P={np.round(Phi, 3)}", flush=True)
    f = lambda P: G_infinite(P, 8)
    lo, hi, _, _ = scan(f, rand)
    print(f"n=inf cutoff=8: random min R={lo:.9f} max R={hi:.6f}", flush=True)
    for P in ([1e-3, 0, 0, 0], [1e-2, 1e-2, 0, 0], [1e-2, 2e-2, 3e-2, 4e-2], [1e-1, 2e-1, 3e-1, 4e-1]):
        ev = ratios(np.array(P), G_infinite(np.array(P), 8))
        print(f"small P {P}: R = {np.round(ev, 6)}", flush=True)


if __name__ == "__main__":
    main()
