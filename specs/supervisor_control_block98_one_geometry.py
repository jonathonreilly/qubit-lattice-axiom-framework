#!/usr/bin/env python3
"""Supervisor control for block 98 (floating point; evidence, not proof).

One record at the centre of the box slows the clocks around it by block 53's law, u = log w = 6 log(kappa) G(r) (block 95's field of one
record). The same u gives the pair energy of a second record, U(b) = 6 log(kappa) G(b) (block 95, a = 1), and times the phase of a walk
(block 54: H_w = sqrt(w) H sqrt(w), H = sum_j sigma_j (i/2)(T_j - T_j^dagger)).
W1: the transverse kick along a straight line at impact parameter b, -sum_x d_y u = -6 log(kappa) d_y G2(b) (G2 the line sum of G = the
    plane kernel), against 2|U(b)|: their ratio at b = 2 ... 24 on a 128-torus with the torus backgrounds removed (continuum value 2).
W2: walk packets (positive branch, wave vector k0 along x, width sigma) passing the record at impact parameter b: the change of the mean
    transverse wave vector, against a cloud of rays of E = w|sin k| with the packet's spreads in the same lattice field (block 54's ray law);
    for one ray on the straight line, tan(k0) x (line kick of u), and its velocity deflection angle against 2|U(b)|/cos^2(k0).
"""
import math
import sys
import time

import numpy as np
from scipy.ndimage import map_coordinates
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
WATSON_G0 = 0.2527310098     # lattice kernel at the origin on Z^3 (literature value, used only to align torus constants)


def zero_mean(L, dim):
    k = 2 * np.pi * np.fft.fftfreq(L)
    grids = np.meshgrid(*([k] * dim), indexing="ij")
    E = 2 * dim - 2 * sum(np.cos(g) for g in grids)
    E[(0,) * dim] = 1.0
    inv = 1.0 / E
    inv[(0,) * dim] = 0.0
    return np.real(np.fft.ifftn(inv))


def w1():
    L = 128
    G3 = zero_mean(L, 3)
    G2 = zero_mean(L, 2)
    V = L ** 3
    A = L ** 2
    print("W1: straight-line kick against twice the pair energy (per unit |6 log kappa|), 128-torus, backgrounds removed")
    c3 = WATSON_G0 - G3[0, 0, 0]
    for b in (2, 4, 8, 12, 16, 24):
        g3 = G3[b, 0, 0] - b * b / (6 * V) + c3                       # infinite-lattice value, torus background and constant removed
        kick = -(G2[b + 1, 0] - G2[b - 1, 0]) / 2 + b / (2 * A)       # plane background r^2/(4A) removed from the gradient
        print("  b = %2d: kick %.5f (1/(2 pi b) = %.5f); G(b) %.5f (1/(4 pi b) = %.5f); kick / G(b) = %.4f" % (b, kick, 1 / (2 * math.pi * b), g3, 1 / (4 * math.pi * b), kick / g3))


def walk_run(L, lam6, k0, b, sig, T):
    idx = np.arange(L ** 3).reshape((L, L, L))
    pos = np.stack(np.meshgrid(*[np.arange(L, dtype=float)] * 3, indexing="ij"))
    c = L // 2
    G = zero_mean(L, 3)
    G = np.roll(np.roll(np.roll(G, c, 0), c, 1), c, 2)                  # kernel centred on the record at (c, c, c)
    u = lam6 * G
    u = u - u[0, c, c]                                                   # unit of rate: the clock far along the path's start
    sw = np.exp(0.5 * u)
    rows, cols, vals = [], [], []
    for j in range(3):
        sl_a = [slice(None)] * 3
        sl_b = [slice(None)] * 3
        sl_a[j] = slice(0, L - 1)
        sl_b[j] = slice(1, L)
        xa, xb = idx[tuple(sl_a)].ravel(), idx[tuple(sl_b)].ravel()
        amp = (sw[tuple(sl_a)] * sw[tuple(sl_b)]).ravel()
        for s1 in range(2):
            for s2 in range(2):
                cc = SIG[j][s1, s2]
                if cc == 0:
                    continue
                rows += [2 * xb + s1, 2 * xa + s1]
                cols += [2 * xa + s2, 2 * xb + s2]
                vals += [(0.5j) * amp * cc, (-0.5j) * amp * cc]
    n = 2 * idx.size
    H = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
    start = np.array([10.0, c + b, c])
    kvec = np.array([k0, 0.0, 0.0])
    hk = sum(np.sin(kvec[j]) * SIG[j] for j in range(3))
    _, vecs = np.linalg.eigh(hk)
    spinor = vecs[:, 1]
    d = pos - start[:, None, None, None]
    env = np.exp(-(d ** 2).sum(axis=0) / (4 * sig ** 2)) * np.exp(1j * (d[0] * kvec[0]))
    comp = [np.fft.fftn(env * spinor[0]), np.fft.fftn(env * spinor[1])]
    kk = 2 * np.pi * np.fft.fftfreq(L)
    KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
    sx, sy, sz = np.sin(KX), np.sin(KY), np.sin(KZ)
    e = np.sqrt(sx * sx + sy * sy + sz * sz)
    e[e == 0] = 1.0
    nx, ny, nz = sx / e, sy / e, sz / e
    up = 0.5 * ((1 + nz) * comp[0] + (nx - 1j * ny) * comp[1])
    dn = 0.5 * ((nx + 1j * ny) * comp[0] + (1 - nz) * comp[1])
    psi = np.zeros(n, complex)
    psi[0::2] = np.fft.ifftn(up).ravel()
    psi[1::2] = np.fft.ifftn(dn).ravel()
    psi /= np.linalg.norm(psi)

    def mean_ky(p):
        a0 = np.fft.fftn(p[0::2].reshape((L, L, L)))
        a1 = np.fft.fftn(p[1::2].reshape((L, L, L)))
        wgt = np.abs(a0) ** 2 + np.abs(a1) ** 2
        return (wgt * np.sin(KY)).sum() / wgt.sum(), (wgt * np.sin(KX)).sum() / wgt.sum()
    ky0, kx0 = mean_ky(psi)
    psi_t = expm_multiply(-1j * H * T, psi)
    ky1, kx1 = mean_ky(psi_t)
    prob = (np.abs(psi_t[0::2]) ** 2 + np.abs(psi_t[1::2]) ** 2).reshape((L, L, L))
    xend = (prob * pos[0]).sum() / prob.sum()
    # ray value along the straight line y = c + b, z = c: line integral of d_y u by central differences
    line = -(u[:, c + b + 1, c] - u[:, c + b - 1, c]) / 2
    kick_u = line.sum()
    return ky1 - ky0, kx0, kick_u, xend, u, start


def ray_cloud(u, start, k0, sig, T, n=4000, steps=500, seed=98):
    """Rays of E = w(x) |sin k| in the lattice field u (linear interpolation), started from the packet's position and wave-vector spreads."""
    rng = np.random.default_rng(seed)
    x = start[None, :] + sig * rng.standard_normal((n, 3))
    k = np.array([k0, 0.0, 0.0])[None, :] + rng.standard_normal((n, 3)) / (2 * sig)
    gu = np.gradient(u)

    def field(x):
        coords = [x[:, 0], x[:, 1], x[:, 2]]
        uu = map_coordinates(u, coords, order=1, mode="nearest")
        g = np.stack([map_coordinates(gu[j], coords, order=1, mode="nearest") for j in range(3)], axis=1)
        return np.exp(uu), g

    def f(x, k):
        w, g = field(x)
        s, c = np.sin(k), np.cos(k)
        e = np.sqrt((s * s).sum(axis=1))
        return (w / e)[:, None] * s * c, -(e * w)[:, None] * g
    h = T / steps
    sy0 = np.sin(k[:, 1]).mean()
    for _ in range(steps):
        a1, b1 = f(x, k)
        a2, b2 = f(x + 0.5 * h * a1, k + 0.5 * h * b1)
        a3, b3 = f(x + 0.5 * h * a2, k + 0.5 * h * b2)
        a4, b4 = f(x + h * a3, k + h * b3)
        x = x + h * (a1 + 2 * a2 + 2 * a3 + a4) / 6
        k = k + h * (b1 + 2 * b2 + 2 * b3 + b4) / 6
    return np.sin(k[:, 1]).mean() - sy0


def w2():
    L = 80
    lam6 = -3.0
    G2 = zero_mean(128, 2)
    G3 = zero_mean(128, 3)
    V = 128 ** 3
    A = 128 ** 2
    c3 = WATSON_G0 - G3[0, 0, 0]
    print("W2: walk packets past one record, 6 log(kappa) = %.1f, box %d^3, width 4, travel time 50" % (lam6, L))
    for k0, b in ((0.8, 12), (0.8, 18), (0.5, 18)):
        if True:
            t0 = time.time()
            dky, kx0, kick_u, xend, u, start = walk_run(L, lam6, k0, b, 4.0, 50.0)
            ray_dky = math.tan(k0) * kick_u
            cloud_dky = ray_cloud(u, start, k0, 4.0, 50.0)
            twoU = 2 * abs(lam6) * (G3[b, 0, 0] - b * b / (6 * V) + c3)
            print("  k0 = %.2f, b = %2d: change of mean sin(k_y): walk %+.5f, cloud of rays with the packet's spreads %+.5f (ratio %.3f); one ray on the straight line %+.5f, its velocity angle %.4f against 2|U(b)|/cos^2(k0) = %.4f (2|U(b)| = %.4f); packet end x = %.1f; %.0f s"
                  % (k0, b, dky, cloud_dky, dky / cloud_dky, ray_dky, abs(ray_dky) / (math.sin(k0) * math.cos(k0)), twoU / math.cos(k0) ** 2, twoU, xend, time.time() - t0))
            sys.stdout.flush()


if __name__ == "__main__":
    w1()
    w2()
