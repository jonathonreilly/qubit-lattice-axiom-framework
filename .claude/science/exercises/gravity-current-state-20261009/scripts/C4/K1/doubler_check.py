"""K1: doubler symmetry of the naive fermion with the vielbein coupling.
psi -> (-1)^{x_mu} gamma_mu gamma_5 psi maps S_f[psi, h] to S_f[psi, R_mu h R_mu] at FIXED positions (internal reflection of h).
Hence Gamma_f(H; q) = Gamma_f(R H R; q) without reflecting q; with W(B4) this makes Gamma_f even in each q_mu separately,
so the cross-term forms F2, F3, A4 are absent from the fermion sector (to all orders in its own couplings).
Check: B(q) = rho(R)^T B(q) rho(R) for each axis reflection, at a generic on-grid q.   Usage: python doubler_check.py
"""
import numpy as np
import loop_fermion as lf
from ward_checks import rho
L, m = 16, 0.4
q = 2 * np.pi / L * np.array([2., 1, 0, 3])
B, _ = lf.bilinear(q, L, m)
for mu in range(4):
    R = np.eye(4); R[mu, mu] = -1
    r = rho(R)
    print(f"axis {mu}: internal reflection, max |rho^T B(q) rho - B(q)| / |B| = {np.abs(r.T @ B @ r - B).max() / np.abs(B).max():.1e}")
import loop_photon as lp
Bp = lp.bilinear(q, 12 if False else 16)[0]
R = np.eye(4); R[0, 0] = -1; r = rho(R)
print(f"photon (no such symmetry): internal reflection axis 0, max rel dev = {np.abs(r.T @ Bp @ r - Bp).max() / np.abs(Bp).max():.1e}")
