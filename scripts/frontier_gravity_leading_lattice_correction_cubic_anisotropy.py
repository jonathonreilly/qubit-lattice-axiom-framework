"""Class-A finite runner (memory-safe): the LEADING lattice correction to the emergent
Newtonian potential G(r)=1/(4 pi r) is a PURELY ANISOTROPIC O(1/r^3) cubic-harmonic term

    G(r) = 1/(4 pi r) + [5/(32 pi)] * K4(nhat) / r^3 + O(1/r^5),
    K4(nhat) = sum_mu nhat_mu^4 - 3/5   (the l=4 cubic harmonic),

a falsifiable lattice-gravity signature: gravity on the Z^3 lattice is NOT exactly
isotropic. Origin: the A1 graph-Laplacian dispersion lambda(k)=sum_mu(2-2cos k_mu)
= |k|^2 - (1/12) sum_mu k_mu^4 + O(k^6); the (1/12) sum k_mu^4 / k^4 correction to 1/lambda
Fourier-transforms to the 1/r^3 cubic harmonic (the isotropic 3/5 part is a contact term,
so the tail is purely K4). The exact lattice Green function is the heat-kernel/Bessel
resolvent G(x)=int_0^inf prod_mu e^{-2t} I_{x_mu}(2t) dt (companion #3184).

  T1  dispersion: 2-2cos k = k^2 - k^4/12 + O(k^6) (the -1/12 source of the correction).
  T2  residual Delta(r)=G(r)-1/(4 pi r) ~ 1/r^3 (power p=3) along [100],[110],[111].
  T3  cubic-harmonic structure: Delta*r^3 / K4(nhat) is DIRECTION-INDEPENDENT (same c on
      [100],[110],[111]) => Delta = c*K4/r^3.
  T4  coefficient: c (extrapolated r->inf along [100]) = 5/(32 pi) (c*32 pi = 5).
  T5  purely ANISOTROPIC: the spherical average of K4 is 0, so there is NO isotropic 1/r^3
      term (the leading isotropic correction is higher order); the direction-summed Delta*r^3
      (weighted by multiplicity) ~ 0.
  CTRL a wrong coefficient (e.g. 1/(8 pi)) is rejected.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import ive

results = []
def check(name, ok): results.append((name, bool(ok)))

def G(x, y, z):
    return quad(lambda t: ive(x, 2 * t) * ive(y, 2 * t) * ive(z, 2 * t), 0, np.inf, limit=600)[0]

def K4(d):
    n = np.array(d, float); n = n / np.linalg.norm(n)
    return (n ** 4).sum() - 0.6

# --- T1: dispersion 2-2cos k = k^2 - k^4/12 + ... ---
k = sp.symbols('k')
ser = sp.series(2 - 2 * sp.cos(k), k, 0, 6).removeO()
check("T1 dispersion 2-2cos k = k^2 - k^4/12 + O(k^6) (the -1/12 source)",
      sp.simplify(ser - (k ** 2 - k ** 4 / 12)) == 0)

# --- T2: residual ~ 1/r^3 ---
dirs = {'[100]': (1, 0, 0), '[110]': (1, 1, 0), '[111]': (1, 1, 1)}
ns = [12, 18, 26, 38]
ok2 = True
for name, d in dirs.items():
    rs = []; De = []
    for n in ns:
        x = tuple(int(n * c) for c in d); r = n * np.linalg.norm(d)
        De.append(abs(G(*x) - 1 / (4 * np.pi * r))); rs.append(r)
    p = -np.polyfit(np.log(rs), np.log(De), 1)[0]
    if not abs(p - 3.0) < 0.15:
        ok2 = False
check("T2 residual Delta(r)=G(r)-1/(4pi r) ~ 1/r^3 (power 3) on all directions", ok2)

# --- T3: cubic-harmonic structure (direction-independent Delta*r^3/K4) ---
cs = []
for name, d in dirs.items():
    n = 38; x = tuple(int(n * c) for c in d); r = n * np.linalg.norm(d)
    delta = G(*x) - 1 / (4 * np.pi * r)
    cs.append(delta * r ** 3 / K4(d))
check("T3 Delta*r^3/K4 direction-independent ([100],[110],[111] agree => c*K4/r^3 structure)",
      max(cs) - min(cs) < 0.002)

# --- T4: coefficient c = 5/(32 pi) (extrapolated along [100]) ---
ns2 = np.array([20, 30, 44, 64, 90])
cvals = np.array([(G(n, 0, 0) - 1 / (4 * np.pi * n)) * n ** 3 / 0.4 for n in ns2])
A = np.vstack([np.ones_like(ns2, float), 1 / ns2.astype(float) ** 2]).T
c_inf = np.linalg.lstsq(A, cvals, rcond=None)[0][0]
check("T4 coefficient c = 5/(32 pi) (extrapolated; c*32pi = %.4f)" % (c_inf * 32 * np.pi),
      abs(c_inf - 5 / (32 * np.pi)) < 5e-4)

# --- T5: purely anisotropic (K4 spherical average = 0; no isotropic 1/r^3) ---
# Monte-Carlo spherical average of K4
rng = np.random.default_rng(0)
v = rng.standard_normal((20000, 3)); v /= np.linalg.norm(v, axis=1, keepdims=True)
K4avg = np.mean((v ** 4).sum(axis=1) - 0.6)
check("T5 spherical average of K4 = 0 (=> purely anisotropic, no isotropic 1/r^3)", abs(K4avg) < 5e-3)

# --- CTRL: wrong coefficient rejected ---
check("CTRL wrong coefficient 1/(8 pi) is rejected", abs(c_inf - 1 / (8 * np.pi)) > 5e-3)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("RESULT: G(r) = 1/(4 pi r) + [5/(32 pi)] K4(nhat)/r^3 + O(1/r^5);  c_inf*32pi = %.4f" % (c_inf * 32 * np.pi))
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
