"""Test D: mean-field (Hartree) CDW gap equation for a one-mode-per-site staggered sea with NN repulsion V."""
import numpy as np
from scipy.optimize import brentq
# H0 = staggered (Kogut-Susskind) hopping, spectrum +-sqrt(sum sin^2 k); half filled; per-site energies (see PREREGISTER)
n = 96
k = (np.arange(n) + 0.5) * 2 * np.pi / n - np.pi
kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
s2 = np.sin(kx) ** 2 + np.sin(ky) ** 2 + np.sin(kz) ** 2
inv = lambda D: np.mean(1.0 / np.sqrt(s2 + D * D))
# normalisation check: e0(D)->-D/2 for large D, and delta(D)=D/2*<1/sqrt>
for n2 in (48, 96):
    kk = (np.arange(n2) + 0.5) * 2 * np.pi / n2 - np.pi
    a, b, c_ = np.meshgrid(kk, kk, kk, indexing="ij")
    s = np.sin(a) ** 2 + np.sin(b) ** 2 + np.sin(c_) ** 2
    print(f"grid {n2}^3: <1/|s|> = {np.mean(1/np.sqrt(np.maximum(s,1e-12))):.5f}")
Vc = 1.0 / (3.0 * np.mean(1.0 / np.sqrt(s2)))
print(f"mean-field V_c = 1/(3<1/|s|>) = {Vc:.4f}   (hopping scale: Dirac velocity 1, bandwidth of |s| up to sqrt3)")
print("   V/Vc    Delta      Delta/sqrt(V/Vc-1)")
for r in (1.001, 1.01, 1.1, 1.5, 2, 3, 5, 10):
    V = r * Vc
    f = lambda D: 3 * V * inv(D) - 1.0
    D = brentq(f, 1e-6, 50.0)
    print(f"  {r:6.3f}  {D:8.4f}   {D/np.sqrt(r-1):8.4f}")
