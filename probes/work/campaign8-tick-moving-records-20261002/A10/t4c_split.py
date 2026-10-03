"""t4c: second-order branch split of the signed Strang cone; n-dependence; palindromic cycle;
threshold where the pi gap closes (quasienergy bandwidth reaches pi)."""
import numpy as np
from scipy.optimize import brentq
from vcyc import layers_U, strang9

pi = np.pi
Ks = np.array([pi, pi, pi])
rng = np.random.default_rng(5)

def blk(a, phi):
    return [(a, 0, phi / 2), (a, 1, phi), (a, 0, phi / 2)]

def pal18(phi):
    return blk(0, phi) + blk(1, phi) + blk(2, phi) + blk(2, phi) + blk(1, phi) + blk(0, phi)

def coeffs(lay, n, d1=0.002, d2=0.004, d3=0.006):
    U0 = layers_U(Ks[None], lay, True)[0]
    ref = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
    ph = []
    for d in (d1, d2, d3):
        ph.append(np.sort(np.angle(np.linalg.eigvals(layers_U((Ks + d * n)[None], lay, True)[0]) * np.conj(ref))))
    ph = np.array(ph)
    ds = np.array([d1, d2, d3])
    V = np.vstack([ds, ds ** 2, ds ** 3]).T          # fit w = v d + a d^2 + b d^3 per band
    sol = np.linalg.lstsq(V, ph, rcond=None)[0]
    return sol[0], sol[1]

for th in [0.1, 0.2, 0.4, pi / 4]:
    rat = []
    for t in range(40):
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        v, a = coeffs(strang9(th), n)
        up = np.sort(a[4:])                      # the four upper bands, q^2 coefficients
        rat.append((up[-1] - up[0]) / 2 / abs(n[0] * n[1] * n[2]))
    v, a = coeffs(strang9(th), np.ones(3) / np.sqrt(3))
    print(f"Strang-9 th={th:.4f}: speed {np.round(v[4:], 6)}; diag q^2 coeff (upper) {np.round(np.sort(a[4:]), 5)};"
          f" half-split/|nx ny nz| over 40 random n: mean {np.mean(rat):.5f} sd {np.std(rat):.1e}")

for phi in [0.1, 0.2, pi / 8]:
    v, a = coeffs(pal18(phi), np.ones(3) / np.sqrt(3))
    v2, a2 = coeffs(pal18(phi), np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81]))
    print(f"palindrome-18 phi={phi:.4f}: speed {np.round(v[4:], 6)} (2 sin phi = {2*np.sin(phi):.6f}); "
          f"diag q^2 coeffs {np.round(np.sort(a[4:]), 6)}; generic-n q^2 {np.round(np.sort(a2[4:]), 6)}")

# pi-gap threshold for Strang-9 signed: max quasienergy at K=0 reaches pi
def maxqe(th):
    U = layers_U(np.zeros((1, 3)), strang9(th), True)[0]
    U0 = layers_U(Ks[None], strang9(th), True)[0]
    ref = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
    return np.abs(np.angle(np.linalg.eigvals(U) * np.conj(ref))).max()
ths = np.linspace(0.05, 1.0, 96)
vals = [maxqe(t) for t in ths]
for t, v in zip(ths[::8], vals[::8]):
    print(f"   th={t:.3f}: max|qe| at K=0 = {v:.4f}")
k = next(i for i, v in enumerate(vals) if v > pi - 1e-3)
print("first theta on grid with max|qe(K=0)| ~ pi:", round(ths[k], 4), " neighbours:", np.round(vals[k-2:k+1], 4))
U = layers_U(np.zeros((1, 3)), strang9(0.3), True)[0]
U0 = layers_U(Ks[None], strang9(0.3), True)[0]
ref = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
print("K=0 relative eigenphases at th=0.3:", np.round(np.sort(np.angle(np.linalg.eigvals(U) * np.conj(ref))), 5),
      " 2 sqrt3 th=", round(2 * np.sqrt(3) * 0.3, 5))
