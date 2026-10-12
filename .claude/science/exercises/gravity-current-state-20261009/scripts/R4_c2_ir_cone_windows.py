"""C2: free IR cone, which part of the TT response comes from window FIXEDNESS and which from window SHAPE.

Weyl sea energy E(h) = - int_W d^3k/(2pi)^3 |e^{-h/2} k|, h = eps*P, P unit-Frobenius traceless.
Per-point second derivative: f'' = (k P^2 k)/(2|k|) - (k P k)^2/(4|k|^3).
 - ball window fixed in index space: isotropic, -K^4/(60 pi^2)  (refereed value, TEST_LOG.md:514)
 - cube window [-pi,pi]^3 fixed in index space: E and T2 differ (cubic anisotropy from shape)
 - window that follows the strain (W_h = e^{h/2} W_0): exactly 0 (change of variables, det = 1)
A real scalar's zero-point (+1/2 |k|) gives -1/2 times the Weyl-sea value: opposite sign.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

PE = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]]) / np.sqrt(2)
PT = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / np.sqrt(2)

def fpp(k, P):
    r = np.linalg.norm(k, axis=-1)
    kP = k @ P
    kPk = np.einsum('...i,...i->...', kP, k)
    kP2k = np.einsum('...i,...i->...', kP, kP)
    return kP2k / (2 * r) - kPk ** 2 / (4 * r ** 3)

def cube_integral(fun, n=48):
    # integrate over [-pi,pi]^3 as 8 octants, Gauss-Legendre in each (cusp only at origin corner)
    x, w = leggauss(n)
    x = (x + 1) / 2 * np.pi; w = w / 2 * np.pi          # [0, pi]
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    W = w[:, None, None] * w[None, :, None] * w[None, None, :]
    tot = 0.0
    for sx in (1, -1):
        for sy in (1, -1):
            for sz in (1, -1):
                k = np.stack([sx * X, sy * Y, sz * Z], axis=-1)
                tot += np.sum(W * fun(k))
    return tot / (2 * np.pi) ** 3

def ball_integral(fun, K=1.0, nr=40, nang=60):
    r, wr = leggauss(nr); r = (r + 1) / 2 * K; wr = wr / 2 * K
    ct, wt = leggauss(nang)
    ph = np.linspace(0, 2 * np.pi, 2 * nang, endpoint=False); wp = 2 * np.pi / len(ph)
    R, C, PH = np.meshgrid(r, ct, ph, indexing='ij')
    S = np.sqrt(1 - C ** 2)
    k = np.stack([R * S * np.cos(PH), R * S * np.sin(PH), R * C], axis=-1)
    W = (wr[:, None, None] * R ** 2) * wt[None, :, None] * wp
    return np.sum(W * fun(k)) / (2 * np.pi) ** 3

print("Weyl sea, d2E/deps2 (E = -sum |k|_h):")
for name, P in [("E ", PE), ("T2", PT)]:
    b = -ball_integral(lambda k: fpp(k, P))
    print(f"  ball K=1, {name}: {b:+.8f}   -1/(60 pi^2) = {-1/(60*np.pi**2):+.8f}")
cube = {}
for n in (32, 48, 64):
    cube[n] = {nm: -cube_integral(lambda k: fpp(k, P), n) for nm, P in [("E", PE), ("T2", PT)]}
    print(f"  cube [-pi,pi]^3 (GL n={n}): E {cube[n]['E']:+.6f}  T2 {cube[n]['T2']:+.6f}  "
          f"ratio T2/E {cube[n]['T2']/cube[n]['E']:.4f}")
Kc = (6 * np.pi ** 2) ** (1 / 3) * (np.pi / np.pi)  # ball with the cube's volume: (4/3)pi K^3 = (2pi)^3
Kc = (3 * (2 * np.pi) ** 3 / (4 * np.pi)) ** (1 / 3)
print(f"  equal-volume ball (K={Kc:.4f}): {-Kc**4/(60*np.pi**2):+.6f} (both channels)")
cE, cT = cube[64]['E'], cube[64]['T2']
iso = (2 * cE + 3 * cT) / 5
print(f"  cube: isotropic part (2E+3T2)/5 = {iso:+.6f}; anisotropy E-T2 = {cE-cT:+.6f}")
print("Window following the strain: E(h) = -int_{e^{h/2}W0} |e^{-h/2}k| = -int_{W0} |p| d^3p (det e^{h/2}=1): "
      "independent of h exactly => 0 in both channels.")
print("Real scalar zero point (+1/2|k|): each number times -1/2 (opposite sign).")
