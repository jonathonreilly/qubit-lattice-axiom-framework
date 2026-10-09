"""C5: a free translation-invariant law whose sea window follows the strain exactly; what it costs.

phi_a = psi2 o psi1 on T^3, psi1: k1 += a sin k2, psi2: k2 += a sin k1  (each a measure-preserving
skew shift, so phi_a is a volume-preserving diffeomorphism of the Brillouin torus).
D phi_a^{-1}(0) = [[1+a^2, -a], [-a, 1]] (+) 1: symmetric, det 1 -> an IR metric strain (T2 + O(a^2) E).

Law A ("relabelled"):  H_a(k) = sigma . s(phi_a^{-1}(k)),  s = (sin k1, sin k2, sin k3).
Law B ("natural NN"):   H_a(k) = sigma . (M_a s(k)),     M_a = D phi_a^{-1}(0): same IR strain, NN hops.
Checks: (1) Weyl-sea energy vs a for A and B; (2) IR dispersions agree; (3) phi_a is not additive
(so an interaction vertex's lattice momentum conservation is not carried along); (4) hopping range of A.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

def phi_inv(k, a):
    k1, k2, k3 = k[..., 0], k[..., 1], k[..., 2]
    k2n = k2 - a * np.sin(k1)              # psi2^{-1}
    k1n = k1 - a * np.sin(k2n)             # psi1^{-1}
    return np.stack([k1n, k2n, k3], axis=-1)

def phi(k, a):
    k1, k2, k3 = k[..., 0], k[..., 1], k[..., 2]
    k1n = k1 + a * np.sin(k2)
    k2n = k2 + a * np.sin(k1n)
    return np.stack([k1n, k2n, k3], axis=-1)

def M(a):
    return np.array([[1 + a * a, -a, 0], [-a, 1, 0], [0, 0, 1.0]])

n = 72
x, w = leggauss(n); x = x * np.pi; w = w * np.pi       # [-pi, pi], smooth periodic integrand away from nodes
K = np.stack(np.meshgrid(x, x, x, indexing='ij'), axis=-1)
Wt = w[:, None, None] * w[None, :, None] * w[None, None, :] / (2 * np.pi) ** 3

def sea_A(a):
    s = np.sin(phi_inv(K, a))
    return -np.sum(Wt * np.linalg.norm(s, axis=-1))

def sea_B(a):
    s = np.sin(K) @ M(a).T
    return -np.sum(Wt * np.linalg.norm(s, axis=-1))

print("(1) Weyl-sea energy per cell (naive 2-component, GL n=72):")
for a in (0.0, 0.05, 0.1, 0.2):
    print(f"   a={a:<5} law A (relabelled) {sea_A(a):+.10f}   law B (natural NN) {sea_B(a):+.10f}")
h = 0.02
for lab, f in (("A", sea_A), ("B", sea_B)):
    d2 = (f(h) - 2 * f(0) + f(-h)) / h ** 2
    print(f"   d2E/da2 at 0, law {lab}: {d2:+.6e}")

print("(2) IR dispersion: |s(phi^-1(k))| vs |M s(k)| at small k (a=0.2):")
rng = np.random.default_rng(0)
for r in (1e-2, 1e-3):
    kk = rng.normal(size=(5, 3)); kk = r * kk / np.linalg.norm(kk, axis=1, keepdims=True)
    A_ = np.linalg.norm(np.sin(phi_inv(kk, 0.2)), axis=1); B_ = np.linalg.norm(np.sin(kk) @ M(0.2).T, axis=1)
    print(f"   |k|={r:g}: max relative difference {np.max(np.abs(A_ - B_) / B_):.2e}")

print("(3) additivity of phi (a=0.2): max |phi(k+k') - phi(k) - phi(k')| (mod 2pi) over 2000 random pairs:")
k1 = rng.uniform(-np.pi, np.pi, size=(2000, 3)); k2 = rng.uniform(-np.pi, np.pi, size=(2000, 3))
d = phi(k1 + k2, 0.2) - phi(k1, 0.2) - phi(k2, 0.2)
d = (d + np.pi) % (2 * np.pi) - np.pi
print(f"   {np.max(np.abs(d)):.3f}  (0 would mean a group automorphism of T^3)")

print("(4) hopping range of law A (a=0.2): |Fourier coefficient| of s1(phi^-1(k)) along k2 at range r:")
L = 64
g = 2 * np.pi * np.arange(L) / L
K1, K2 = np.meshgrid(g, g, indexing='ij')
kk = np.stack([K1, K2, np.zeros_like(K1)], axis=-1)
s1 = np.sin(phi_inv(kk, 0.2))[..., 0]
F = np.abs(np.fft.fft2(s1)) / L ** 2
for r in (1, 2, 3, 4, 6):
    print(f"   range {r}: {np.max(F[:, r]):.2e}")
