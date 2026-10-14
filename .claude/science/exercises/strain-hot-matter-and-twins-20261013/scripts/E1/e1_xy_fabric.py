#!/usr/bin/env python3
"""E1 (C') and (D, graphene part).
(C') 3D classical XY, H = -sum_{x,j} J_j cos(theta_x - theta_{x+j}), J = (1+t, 1-t, 1), low T.
  Harmonic: <(Delta_j theta)^2> = T W_j, W_j = < e_j / sum_k J_k e_k >, e_j = 2(1 - cos q_j); sum rule sum_j J_j W_j = 1.
  Self-consistent harmonic stiffness rho_j = J_j exp(-T W_j(rho)/2) (one loop: J_j (1 - T W_j/2)).
  The spin-wave quadratic form sum_j rho_j e_j(q) vanishes at q = 0 for every rho (U(1) shift symmetry).
(D) half-filled honeycomb band energy per cell (2 spins): E(u) = -2 <|f|>, bond strain (1+2u, 1-u, 1-u);
  <|f|> via the elliptic-E inner average; d^2E/du^2 at u = 0 by central differences.
"""
import numpy as np
from scipy.special import ellipe
from scipy.integrate import quad

def W(J, N=96):
    q = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    e = 2 * (1 - np.cos(q))
    acc = np.zeros(3)
    for i in range(N):
        E = J[0] * e[i] + J[1] * e[:, None] + J[2] * e[None, :]
        acc += [(e[i] / E).sum(), (e[:, None] / E).sum(), (e[None, :] / E).sum()]
    return acc / N**3

def scha(J, T, N=96, it=60):
    rho = np.array(J, float)
    for _ in range(it):
        rho = np.array(J) * np.exp(-0.5 * T * W(rho, N))
    return rho

def mean_absf(t):
    t1, t2, t3 = t
    def inner(th1):
        w = abs(t1 + t2 * np.exp(-1j * th1))
        S = (w + t3) ** 2; m = 4 * w * t3 / S
        return (2 / np.pi) * np.sqrt(S) * ellipe(m)
    return quad(inner, 0, 2 * np.pi, limit=1000, epsabs=1e-14, epsrel=1e-13)[0] / (2 * np.pi)

if __name__ == "__main__":
    print("(C') 3D XY: harmonic W_j and stiffness under stretch J = (1+t, 1-t, 1); grids N = 64, 96")
    for t in (0.0, 0.05, 0.1, 0.2):
        J = np.array([1 + t, 1 - t, 1.0])
        w64 = W(J, 64); w96 = W(J, 96)
        print(f"  t={t:.2f}: W(N96) = {w96[0]:.6f} {w96[1]:.6f} {w96[2]:.6f}  (N64 {w64[0]:.6f} {w64[1]:.6f});  sum_j J_j W_j = {(J*w96).sum():.12f}")
    T = 0.5
    print(f"  self-consistent harmonic stiffness at T = {T} (isotropic 3D XY T_c ~ 2.2, RECALLED):")
    for t in (0.0, 0.05, 0.1, 0.2):
        J = np.array([1 + t, 1 - t, 1.0])
        rho = scha(J, T)
        lr = np.log(rho[0] / rho[1]); lJ = np.log(J[0] / J[1])
        print(f"  t={t:.2f}: rho = {rho[0]:.6f} {rho[1]:.6f} {rho[2]:.6f};  ln(rho_x/rho_y) = {lr:+.6f} vs ln(J_x/J_y) = {lJ:+.6f};  quadratic form at q=0: {np.dot(rho, [0,0,0]):.1f} (identically 0)")
    print("  metric seen by this Goldstone under coupling stretch (1+t,1-t): ln(v_x/v_y) = (1/2) ln(rho_x/rho_y) ~ t at T->0")
    Kc = 0.5 * np.arcsinh(1.0)
    print(f"  compare 2D Ising at Kc, same coupling stretch K(1+t),K(1-t): ln(xi_x/xi_y) ~ 2Kc coth(2Kc) t = {2*Kc/np.tanh(2*Kc):.6f} t")
    print("\n(D) honeycomb band energy E(u) = -2<|f|> per cell, d2E/du2 at u=0 (bond strain (1+2u,1-u,1-u))")
    E0 = -2 * mean_absf(np.array([1.0, 1.0, 1.0]))
    print(f"  E(0) = {E0:.12f}  (comparator: -2 x 1.5746 = -3.1492 per cell, RECALLED)")
    for h in (0.02, 0.01, 0.005):
        Ep = -2 * mean_absf(np.array([1 + 2 * h, 1 - h, 1 - h])); Em = -2 * mean_absf(np.array([1 - 2 * h, 1 + h, 1 + h]))
        print(f"  h={h}: d2E/du2 = {(Ep + Em - 2 * E0) / h**2:+.6f}   (E(+h)-E(-h))/2h = {(Ep-Em)/(2*h):+.3e}")
