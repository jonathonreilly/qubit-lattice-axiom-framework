#!/usr/bin/env python3
"""T61 D1: independent reproduction of P6's free-sea numbers (own code, not P6's runner).

Free walker on Z^3, H(k) = sum_a sigma_a (e s(k))_a, s = (sin k1, sin k2, sin k3); filled lower band.
E(e) = -< |e s| >_BZ per cell.  Shear e = expm(t*eps/2), tr eps^2 = 1.  c = d^2E/dt^2 at 0.
"""
import numpy as np
from scipy.linalg import expm

def grid(N):
    k = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    s = np.sin(k)
    S = np.stack(np.meshgrid(s, s, s, indexing="ij"), 0).reshape(3, -1)
    return S

def E(e, S):
    w = e @ S
    return -np.sqrt((w * w).sum(0)).mean()

def curvature(eps, S, h):
    e = lambda t: expm(t * eps / 2)
    return (E(e(h), S) + E(e(-h), S) - 2 * E(e(0.0), S)) / h**2

def rich(eps, S, h=0.1):
    c1 = curvature(eps, S, h)
    c2 = curvature(eps, S, h / 2)
    return (4 * c2 - c1) / 3, c1, c2

if __name__ == "__main__":
    axis = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)
    face = np.zeros((3, 3)); face[0, 1] = face[1, 0] = 1 / np.sqrt(2)
    # second axis-type shear (cubic-equivalent check): diag(1,1,-2)/sqrt6
    axis2 = np.diag([1.0, 1.0, -2.0]) / np.sqrt(6)
    for N in (64, 96, 128):
        S = grid(N)
        E0 = E(np.eye(3), S)
        cE, a1, a2 = rich(axis, S)
        cE2, _, _ = rich(axis2, S)
        cT, b1, b2 = rich(face, S)
        print(f"N={N:4d}  E0={E0:+.6f}  c_E(axis diag(1,-1,0))={cE:+.6f} (h=.1:{a1:+.6f} h=.05:{a2:+.6f})  "
              f"c_E(diag(1,1,-2))={cE2:+.6f}  c_T(face,natural)={cT:+.6f}")
    print("P6 quoted: E0=-1.19380  c_E=-0.17793  c_T(natural)=-0.14667")
    # dependence on a nonlinear-vs-affine parametrisation (diamagnetic part): affine path e=1+t*eps/2
    S = grid(96)
    def curv_aff(eps, h=0.05):
        f = lambda t: E(np.eye(3) + t * eps / 2, S)
        return (f(h) + f(-h) - 2 * f(0)) / h**2
    print("affine path curvature: axis %+.6f face %+.6f" % (curv_aff(axis), curv_aff(face)))
    # gradient at flat: G = dE/de_{aj}; expect G = -tau*delta
    tau = np.mean(S[0] ** 2 / np.sqrt((S * S).sum(0)))
    print("tau = <sin^2 k1/|s|> = %.6f ;  tau/4 = %.6f" % (tau, tau / 4))
