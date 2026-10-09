"""C4: does moving the matter's cutoff far below the lattice scale remove the lattice's TT imprint?

Toy: dilute Bose gas on Z^3 (Bogoliubov, bare on-site U, density n per site), probe strain in the
E channel as volume-preserving hopping anisotropy t = (e^eps, e^-eps, 1)  (prod t_i = 1).
Its low-energy modes live at |k| < 1/xi ~ sqrt(U n) << pi: a medium whose own cutoff is far below
the lattice scale (sound speed c ~ sqrt(2Un)). Translation-invariant vacuum.

E0/N = U n^2/2 + 1/2 int_BZ (E_k - e_k - U n),  E_k = sqrt(e_k^2 + 2 U n e_k).
Prediction (expansion for U n << e_k): d2E0/deps2 -> -(U n)^2 W''(0)/4, W(eps) = int_BZ 1/e_k,
so R(n) = [d2E0/deps2] / [U n^2/2] -> -U W''(0)/2, a nonzero constant as n -> 0 (FAIL of the escape)
unless W''(0) = 0.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import integrate, special

def W(eps):
    f = lambda s: special.i0e(2*np.exp(eps)*s) * special.i0e(2*np.exp(-eps)*s) * special.i0e(2*s)
    v1, _ = integrate.quad(f, 0, 50, limit=400, epsabs=1e-14, epsrel=1e-13)
    v2, _ = integrate.quad(f, 50, np.inf, limit=400, epsabs=1e-14, epsrel=1e-13)
    return v1 + v2

h = 1e-3
W0 = W(0.0)
Wpp = (W(h) - 2*W0 + W(-h)) / h**2
Wpp2 = (W(2*h) - 2*W0 + W(-2*h)) / (2*h)**2
print(f"Watson-type integral W(0) = {W0:.10f} (known 3D cubic value 0.2527310...)")
print(f"W''(0) (h=1e-3) = {Wpp:.8f}; (h=2e-3) = {Wpp2:.8f}")

def stretched_axis(n, p=3):
    u, w = leggauss(n)
    u = (u + 1) / 2; w = w / 2                 # u in [0,1]
    k = np.pi * u**p; wk = w * np.pi * p * u**(p-1)
    return k, wk

def d2E0(U, n, N=96):
    k, wk = stretched_axis(N)
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    Wt = wk[:, None, None] * wk[None, :, None] * wk[None, None, :] * 8 / (2*np.pi)**3
    sx, sy, sz = 4*np.sin(KX/2)**2, 4*np.sin(KY/2)**2, 4*np.sin(KZ/2)**2   # = 2(1-cos k), no cancellation
    ek = sx + sy + sz
    A = sx - sy          # d e_k / d eps at 0
    B = sx + sy          # d2 e_k / d eps2 at 0
    Un = U*n
    Ek = np.sqrt(ek**2 + 2*Un*ek)
    d2E = (A**2 + (ek+Un)*B)/Ek - (ek+Un)**2 * A**2 / Ek**3
    return 0.5*np.sum(Wt*(d2E - B))

U = 1.0
print(f"\nU = {U}:  predicted n->0 limit of R = -U W''/2 = {-U*Wpp/2:+.6f}")
for n in (0.1, 0.03, 0.01, 0.003, 0.001):
    vals = [d2E0(U, n, N) for N in (64, 96)]
    R = vals[-1] / (U*n**2/2)
    print(f"  n = {n:<6} xi^-1~sqrt(2Un)={np.sqrt(2*U*n):.3f}  d2E0/deps2 = {vals[-1]:+.3e} "
          f"(N=64: {vals[0]:+.3e})  R = {R:+.5f}")
