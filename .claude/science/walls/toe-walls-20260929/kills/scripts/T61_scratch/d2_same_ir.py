#!/usr/bin/env python3
"""T61 D2: same infrared, different shear stiffness (own code).

Natural coupling: symbol w = e s(k).   Designed coupling (P6 T6): w = s(phi(k)), phi = time-1 flow of a
divergence-free trigonometric field v that vanishes at the 8 nodes, with node Jacobian = the shear.
Both are given the SAME node metric G_K = J_K^T J_K at all 8 nodes (axis shear).  Compare (a) node metrics,
(b) sea energy shift.  Also: taste-universal face coupling check (-0.1088).
"""
import numpy as np, itertools
from scipy.linalg import expm

def sgrid(N):
    k = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    K = np.stack(np.meshgrid(k, k, k, indexing="ij"), 0).reshape(3, -1)
    return K

def v_axis(K, lam):
    k1, k2 = K[0], K[1]
    return np.stack([0.5 * lam * np.sin(2 * k1) * np.cos(2 * k2),
                     -0.5 * lam * np.cos(2 * k1) * np.sin(2 * k2),
                     np.zeros_like(k1)], 0)

def v_face(K, lam):
    k1, k2 = K[0], K[1]
    return np.stack([0.5 * lam * np.sin(2 * k2), 0.5 * lam * np.sin(2 * k1), np.zeros_like(k1)], 0)

def flow(K, v, lam, steps=24):
    x = K.copy(); dt = 1.0 / steps
    for _ in range(steps):
        k1 = v(x, lam); k2 = v(x + 0.5 * dt * k1, lam); k3 = v(x + 0.5 * dt * k2, lam); k4 = v(x + dt * k3, lam)
        x = x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x

def energy_designed(N, v, lam):
    K = sgrid(N)
    P = flow(K, v, lam)
    w = np.sin(P)
    return -np.sqrt((w * w).sum(0)).mean()

def energy_natural(N, e):
    K = sgrid(N)
    w = e @ np.sin(K)
    return -np.sqrt((w * w).sum(0)).mean()

def node_metrics_designed(v, lam, h=1e-5):
    out = {}
    for Kn in itertools.product([0.0, np.pi], repeat=3):
        Kn = np.array(Kn)
        J = np.zeros((3, 3))
        for j in range(3):
            d = np.zeros(3); d[j] = h
            P = flow(np.stack([Kn + d, Kn - d], 1), v, lam)
            J[:, j] = (np.sin(P[:, 0]) - np.sin(P[:, 1])) / (2 * h)
        out[tuple(int(x / np.pi) for x in Kn)] = J.T @ J
    return out

def node_metrics_natural(e):
    out = {}
    for Kn in itertools.product([0.0, np.pi], repeat=3):
        eta = np.cos(np.array(Kn))
        J = e @ np.diag(eta)
        out[tuple(int(x / np.pi) for x in Kn)] = J.T @ J
    return out

def spread(M):
    ms = list(M.values())
    return max(np.abs(m - ms[0]).max() for m in ms)

if __name__ == "__main__":
    lam = 0.1
    N = 96
    E0 = energy_natural(N, np.eye(3))
    # axis shear: natural e = diag(exp(lam), exp(-lam), 1) has node metric diag(e^{2lam}, e^{-2lam}, 1)
    e_ax = np.diag([np.exp(lam), np.exp(-lam), 1.0])
    Gn = node_metrics_natural(e_ax); Gd = node_metrics_designed(v_axis, lam)
    ref = np.diag([np.exp(2 * lam), np.exp(-2 * lam), 1.0])
    print("AXIS shear lam=0.1")
    print("  natural: node-metric spread over 8 nodes = %.2e ; max|G-ref| = %.2e" % (spread(Gn), max(np.abs(m - ref).max() for m in Gn.values())))
    print("  designed: node-metric spread over 8 nodes = %.2e ; max|G-ref| = %.2e" % (spread(Gd), max(np.abs(m - ref).max() for m in Gd.values())))
    Eth = energy_natural(N, e_ax); Edes = energy_designed(N, v_axis, lam)
    print("  E0 = %.9f ; E_natural - E0 = %+.6e ; E_designed - E0 = %+.6e" % (E0, Eth - E0, Edes - E0))
    print("  predicted natural shift c_E*(t^2/2) with t = 2*sqrt(2)*lam*... (info only)")
    # FACE shear
    e_fc = expm(lam * np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0.0]]))
    ref_f = e_fc @ e_fc.T
    Gn = node_metrics_natural(e_fc); Gd = node_metrics_designed(v_face, lam)
    print("FACE shear lam=0.1 (target off-diagonal sinh(2 lam)=%.4f)" % np.sinh(2 * lam))
    print("  natural: node-metric spread = %.3f (mirrored shear at 4 nodes)" % spread(Gn))
    print("  designed: node-metric spread = %.2e ; max|G-ref| = %.2e" % (spread(Gd), max(np.abs(m - ref_f).max() for m in Gd.values())))
    Efn = energy_natural(N, e_fc); Efd = energy_designed(N, v_face, lam)
    print("  E_natural - E0 = %+.6e ; E_designed - E0 = %+.6e" % (Efn - E0, Efd - E0))
    # taste-universal face coupling: w_a = e_aa sin k_a + sum_{j!=a} e_a^j cos k_a sin k_j cos k_j
    def E_tu(e, N=96):
        K = sgrid(N); s = np.sin(K); c = np.cos(K)
        w = np.zeros_like(s)
        for a in range(3):
            w[a] = e[a, a] * s[a]
            for j in range(3):
                if j != a:
                    w[a] += e[a, j] * c[a] * s[j] * c[j]
        return -np.sqrt((w * w).sum(0)).mean()
    face = np.zeros((3, 3)); face[0, 1] = face[1, 0] = 1 / np.sqrt(2)
    h = 0.05
    f = lambda t: E_tu(expm(t * face / 2))
    cT_tu = (f(h) + f(-h) - 2 * f(0.0)) / h**2
    print("taste-universal face coefficient c_T = %+.5f (P6/L16: -0.10882)" % cT_tu)
