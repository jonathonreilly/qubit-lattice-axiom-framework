#!/usr/bin/env python3
"""T2f: the coupling matters -- relabelling coupling of an RP hypercubic kernel (bears on the open lemma's scope).

Take ANY flat kernel D_1(q0, k) in Lemma N's class (here: family A single pole, sigma_N = 4).  Define
  D_G(q0, k) := D_1(q0, Phi_eps(k)),   Phi_eps = time-eps flow of v(k) = curl Psi(k),  Psi = -(1/3) s(k) x (B s(k)),
  s(k) = (sin k_i),  B = -X/2.  v is analytic, periodic, divergence-free, v(k) = B k + O(k^3), so Phi_eps is an analytic
  volume-preserving diffeomorphism of T^3 with D Phi_eps(0) = exp(-eps X/2):  D_G ~ q0^2 + k^T g^-1 k in the IR.
EXACT: (1/2)<log D_G> = (1/2)<log D_1> (change of variables, unit Jacobian) for every eps -> kappa = 0 in both channels;
  at fixed k the time dependence is that of D_1 at the momentum Phi(k), so the time-RP of D_1 is inherited for every g.
This is R4's free relabelling counterexample (agents/R4_misframing.md:34-36), here with time-RP and a 4D RP kernel.
Checks: kappa by finite differences; IR covariance; position-space decay of D_G's couplings; Hankel test at sheared g.
"""
import numpy as np
from t2_core import CHANNELS, V_matrix, midgrid

M2 = 0.09
R_POLE = (16 - 1 / 3) / 4


def vfield(k, B):
    s = np.sin(k); c = np.cos(k)            # k: (3, ...)
    Bs = np.einsum("ij,j...->i...", B, s)
    trBc = sum(B[i, i] * c[i] for i in range(3))
    sumc = c.sum(0)
    BsC = np.einsum("ij,j...->i...", B, s * c)
    return -(1 / 3) * (c * Bs + s * trBc - Bs * sumc - BsC)


def flow(k, B, eps, nsteps=60):
    h = eps / nsteps
    for _ in range(nsteps):
        a1 = vfield(k, B); a2 = vfield(k + h / 2 * a1, B); a3 = vfield(k + h / 2 * a2, B); a4 = vfield(k + h * a3, B)
        k = k + h / 6 * (a1 + 2 * a2 + 2 * a3 + a4)
    return k


def D1(q0, k):
    V = V_matrix(k[0], k[1], k[2])
    S = 2 - 2 * np.cos(q0) + V[0][0] + V[1][1] + V[2][2]
    return M2 + S / (1 + R_POLE * S)


def E_of(eps, X, L):
    kk = np.array(np.meshgrid(*(midgrid(L),) * 3, indexing="ij"))
    phi = flow(kk, -X / 2, eps) if eps != 0 else kk
    acc = 0.0
    for q0 in midgrid(L):
        acc += np.sum(np.log(D1(q0, phi)))
    return 0.5 * acc / L ** 4, phi


def DA(eps, X, L):
    """family-A coupling of the same flat kernel (for contrast): S with g^-1 = exp(-eps X)."""
    from scipy.linalg import expm
    gi = expm(-eps * X)
    k = np.meshgrid(*(midgrid(L),) * 3, indexing="ij")
    V = V_matrix(*k)
    Ssp = sum(gi[i, j] * V[i][j] for i in range(3) for j in range(3))
    acc = 0.0
    for q0 in midgrid(L):
        S = 2 - 2 * np.cos(q0) + Ssp
        acc += np.sum(np.log(M2 + S / (1 + R_POLE * S)))
    return 0.5 * acc / L ** 4


if __name__ == "__main__":
    print(f"== T2f: relabelling coupling of family-A single pole (sigma_N = 4), m^2 = {M2} ==")
    h = 0.05
    for L in (24, 32):
        for ch, X in CHANNELS.items():
            E = [E_of(t * h, X, L)[0] for t in (-2, -1, 0, 1, 2)]
            kap = (-E[0] + 16 * E[1] - 30 * E[2] + 16 * E[3] - E[4]) / (12 * h * h)
            EA = [DA(t * h, X, L) for t in (-2, -1, 0, 1, 2)]
            kapA = (-EA[0] + 16 * EA[1] - 30 * EA[2] + 16 * EA[3] - EA[4]) / (12 * h * h)
            print(f" L={L} {ch:5s}: relabelled kappa = {kap:+.2e}   (E(0.1)-E(0) = {E[4]-E[2]:+.1e});  same kernel, family-A coupling kappa = {kapA:+.4e}")
    # volume preservation of the discrete flow: Jacobian determinant at random points
    from numpy.random import default_rng
    rng = default_rng(1)
    X = CHANNELS["T_2g"]; eps = 0.3
    pts = rng.uniform(-np.pi, np.pi, (3, 200))
    d = 1e-5
    jac = np.zeros((200, 3, 3))
    for j in range(3):
        e = np.zeros((3, 1)); e[j] = d
        jac[:, :, j] = ((flow(pts + e, -X / 2, eps) - flow(pts - e, -X / 2, eps)) / (2 * d)).T
    print(f" Jacobian det of Phi (T_2g, eps=0.3) over 200 random points: min {np.linalg.det(jac).min():.10f} max {np.linalg.det(jac).max():.10f}")
    # IR covariance: D_G(0, k) / (k^T g^-1 k) for small k
    from scipy.linalg import expm
    for ch, X in CHANNELS.items():
        gi = expm(-eps * X)
        rat = []
        for _ in range(20):
            u = rng.normal(size=3); u /= np.linalg.norm(u); k = 1e-3 * u
            phi = flow(k[:, None], -X / 2, eps)[:, 0]
            kin = (D1(0.0, phi[:, None]) - M2)[0]
            rat.append(kin / (k @ gi @ k))
        print(f" IR covariance {ch} eps=0.3: D_G/(k^T g^-1 k) at |k|=1e-3 over 20 directions: {min(rat):.6f} .. {max(rat):.6f}")
    # locality: Fourier coefficients of D_G on a standard 32^4 grid (eps = 0.3, T_2g), max |w(n)| by shell
    L = 32
    kk = 2 * np.pi * np.arange(L) / L
    K = np.array(np.meshgrid(kk, kk, kk, indexing="ij"))
    phi = flow(K, -CHANNELS["T_2g"] / 2, eps)
    Dg = np.array([D1(q, phi) for q in kk])
    w = np.fft.fftn(Dg).real / L ** 4
    n = np.fft.fftfreq(L, 1 / L).astype(int)
    N = np.array(np.meshgrid(n, n, n, n, indexing="ij"))
    shell = np.abs(N).max(0)
    print(" locality (T_2g, eps=0.3): max |coupling| on shell |n|_inf = R:")
    print("   " + "  ".join(f"R={R}:{np.abs(w[shell == R]).max():.1e}" for R in range(1, 13)))
    # time-RP at sheared g: Hankel at 6 random spatial momenta
    NT = 512; T = 10
    q0 = 2 * np.pi * (np.arange(NT) + 0.5) / NT - np.pi
    idx = np.add.outer(np.arange(T + 1), np.arange(T + 1))
    worst = np.inf
    for _ in range(6):
        k = rng.uniform(-np.pi, np.pi, (3, 1))
        phi = flow(k, -CHANNELS["T_2g"] / 2, eps)
        Sq = 1 / np.array([D1(q, phi)[0] for q in q0])
        G = np.array([np.mean(Sq * np.cos(q0 * nn)) for nn in range(2 * T + 2)])
        for H in (G[idx], G[idx + 1], G[idx] - G[idx + 1]):
            ev = np.linalg.eigvalsh(H); worst = min(worst, ev.min() / ev.max())
    print(f" time-RP of relabelled kernel (T_2g, eps=0.3), 6 random k, site/link/Hausdorff worst ratio: {worst:+.1e}")
