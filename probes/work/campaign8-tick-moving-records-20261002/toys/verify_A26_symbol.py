#!/usr/bin/env python3
"""Coordinator's independent check of A26 (written from the report's statements; own index convention o = sx + 2*sy).

2D one-excitation staggered cycle, 2x2 cell, KS signs eta_x = 1, eta_y = (-1)^x; time-symmetric blocks
X = Ex(a/2) Ox(a) Ex(a/2), Y likewise; one-site mass phase exp(-i (mu/2) N eps), eps = (-1)^{x+y}; U = M X Y M.
Field coupling: bond angle a = th * N * e_axis; shear: X -> R X R^dag, R = S P(beta) S^dag,
S = exp(-i pi/4 [unsigned in-cell y-hops]), P = exp(-i beta [in-cell x-hops with sign (-1)^y]), sin(2 beta) = h_xy.
Claims checked:
 (1) cone at K* = (pi, pi); flat cone isotropic;
 (2) D6: rest frequency at K* = mu*N exactly (any dose);
 (3) D2: massless slopes see g^{ij} = E^T E: 45 deg -> sqrt(1-h), 135 deg -> sqrt(1+h), all four bands (taste-blind);
 (4) D2 massive: omega^2 - (N mu)^2 has the same metric;
 (5) R = exp(+-i beta X_x Y_y) (sandwich identity);
 (6) D10: staggered Peierls phases split the tastes with opposite shears;
 (7) D7: two-site (staggered-angle) rest frequency OS = 2 delta N e, ST = 2 delta N.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.linalg import expm

def o(sx, sy):
    return sx + 2 * sy

def gen(K, axis, parity, amp):
    """amp(sx, sy) -> complex amplitude of the bond starting at in-cell site (sx, sy) (lower end along axis)."""
    G = np.zeros((4, 4), complex)
    if axis == 0:
        for sy in (0, 1):
            if parity == 0:   # in-cell bond (0,sy)-(1,sy)
                t = amp(0, sy); G[o(1, sy), o(0, sy)] += t; G[o(0, sy), o(1, sy)] += np.conj(t)
            else:             # cross-cell bond (1,sy)-(0,sy)+x
                t = amp(1, sy) * np.exp(-1j * K[0]); G[o(0, sy), o(1, sy)] += t; G[o(1, sy), o(0, sy)] += np.conj(t)
    else:
        for sx in (0, 1):
            if parity == 0:
                t = amp(sx, 0); G[o(sx, 1), o(sx, 0)] += t; G[o(sx, 0), o(sx, 1)] += np.conj(t)
            else:
                t = amp(sx, 1) * np.exp(-1j * K[1]); G[o(sx, 0), o(sx, 1)] += t; G[o(sx, 1), o(sx, 0)] += np.conj(t)
    return G

EPS = np.diag([(-1.0) ** (sx + sy) for sy in (0, 1) for sx in (0, 1)]).astype(complex)  # index o = sx + 2 sy

def cycle(K, th, mu=0.0, N=1.0, ex=1.0, ey=1.0, beta=0.0, phi=0.0, delta=0.0, mode="ST"):
    ax = th * N * ex; ay = th * N * ey
    # x amplitudes: KS eta_x = 1; optional Peierls phase pattern (-1)^{x+y} * phi on x-bonds
    def ampx_even(sx, sy):
        return np.exp(1j * phi * (-1) ** (sx + sy))
    def ampx_odd(sx, sy):
        return np.exp(1j * phi * (-1) ** (sx + sy))
    def ampy_even(sx, sy):
        return (-1) ** sx * np.exp(-1j * phi * (-1) ** sy)
    def ampy_odd(sx, sy):
        return (-1) ** sx * np.exp(-1j * phi * (-1) ** sy)
    # two-site mass: split angles th0 +- delta on even/odd bonds (OS: (th0 +- d) N e ; ST: N (th0 e +- d))
    if mode == "OS":
        axe, axo = (th + delta) * N * ex, (th - delta) * N * ex
        aye, ayo = (th + delta) * N * ey, (th - delta) * N * ey
    else:
        axe, axo = N * (th * ex + delta), N * (th * ex - delta)
        aye, ayo = N * (th * ey + delta), N * (th * ey - delta)
    Ex = expm(-1j * (axe / 2) * gen(K, 0, 0, ampx_even)); Ox = expm(-1j * axo * gen(K, 0, 1, ampx_odd))
    Ey = expm(-1j * (aye / 2) * gen(K, 1, 0, ampy_even)); Oy = expm(-1j * ayo * gen(K, 1, 1, ampy_odd))
    Xb = Ex @ Ox @ Ex; Yb = Ey @ Oy @ Ey
    if beta != 0.0:
        Gs = gen(K, 1, 0, lambda sx, sy: 1.0)                 # unsigned in-cell y-hops (K-independent)
        Gp = gen(K, 0, 0, lambda sx, sy: (-1.0) ** sy)        # in-cell x-hops with sign (-1)^y
        S = expm(-1j * np.pi / 4 * Gs); P = expm(-1j * beta * Gp)
        R = S @ P @ S.conj().T
        Xb = R @ Xb @ R.conj().T
    M = expm(-1j * (mu / 2) * N * EPS)
    return M @ Xb @ Yb @ M

def qe(U):
    return np.sort(np.angle(np.linalg.eigvals(U)))

Ks = np.array([np.pi, np.pi])
print("(1) cone at K*: ", np.abs(qe(cycle(Ks, 0.3))).max())
th = 0.05; t = 1e-4
def slopes(**kw):
    out = {}
    for ang in (0, 30, 45, 60, 90, 135):
        n = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        w = qe(cycle(Ks + t * n, th, **kw))
        out[ang] = np.sort(np.abs(w)) / t
    return out
flat = slopes()
print("    flat slopes (all 4 bands) / sin(th):")
for a, v in flat.items():
    print("      %3d deg: %s" % (a, np.round(v / np.sin(th), 6)))
# (2) rest frequency
for thd in (0.05, 0.6, 1.2):
    for (mu, N) in ((0.05, 1.0), (0.05, 0.9), (0.16, 0.8)):
        w = qe(cycle(Ks, thd, mu=mu, N=N, ex=0.93, ey=1.04, beta=0.07))
        assert np.allclose(np.abs(w), mu * N, atol=1e-12), (thd, mu, N, w)
print("(2) rest frequency at K* = mu*N exactly (doses 0.05/0.6/1.2, with frame + shear): OK")
# (3) shear slopes
h = 0.05; beta = 0.5 * np.arcsin(h)
sh = slopes(beta=beta)
print("(3) shear h_xy = %.2f, slope ratio to flat, all 4 bands:" % h)
for a in (0, 45, 90, 135):
    print("      %3d deg: %s   metric sqrt(q.g.q) = %.6f" % (a, np.round(sh[a] / flat[a], 6),
          np.sqrt(1 - h * np.sin(2 * np.radians(a)))))
# diagonal frame + lapse
ld = slopes(N=0.9, ex=0.95, ey=0.97)
print("    lapse 0.9, e=(0.95,0.97): ratios 0/45/90 deg:",
      [np.round((ld[a] / flat[a])[0], 6) for a in (0, 45, 90)],
      " expected", [0.9 * 0.95, round(0.9 * np.sqrt((0.95 ** 2 + 0.97 ** 2) / 2), 6), 0.9 * 0.97])
# (4) massive: omega^2 - (N mu)^2 vs q
mu, N = 0.02, 0.95
for a in (45, 135):
    n = np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]); q = 2e-3
    w = np.abs(qe(cycle(Ks + q * n, th, mu=mu, N=N, beta=beta)))
    w0 = np.abs(qe(cycle(Ks + q * n, th, mu=mu, N=N)))
    print("(4) massive %3d deg: (w^2-(N mu)^2) ratio sheared/unsheared = %s ; metric %.6f" %
          (a, np.round((w ** 2 - (N * mu) ** 2) / (w0 ** 2 - (N * mu) ** 2), 5), 1 - h * np.sin(2 * np.radians(a))))
# (5) sandwich identity in the 2-bit cell space: X_x = sigma_x on sx, Y_y = sigma_y on sy (o = sx + 2 sy -> kron(sy, sx))
X = np.array([[0, 1], [1, 0]], complex); Yp = np.array([[0, -1j], [1j, 0]], complex)
XxYy = np.kron(Yp, X)
Gs = gen(Ks, 1, 0, lambda sx, sy: 1.0); Gp = gen(Ks, 0, 0, lambda sx, sy: (-1.0) ** sy)
S = expm(-1j * np.pi / 4 * Gs); P = expm(-1j * 0.37 * Gp); R = S @ P @ S.conj().T
print("(5) |R - exp(+i b XxYy)| = %.2e ; |R - exp(-i b XxYy)| = %.2e" %
      (np.abs(R - expm(1j * 0.37 * XxYy)).max(), np.abs(R - expm(-1j * 0.37 * XxYy)).max()))
# (6) staggered Peierls phases
p2 = slopes(phi=0.02)
print("(6) Peierls phi=0.02: 45 deg ratios %s ; 135 deg %s" % (np.round(p2[45] / flat[45], 6), np.round(p2[135] / flat[135], 6)))
# (7) two-site rest frequencies
for mode in ("OS", "ST"):
    d, Nn, e = 0.01, 0.9, 0.95
    w = np.abs(qe(cycle(Ks, 0.3, N=Nn, ex=e, ey=e, delta=d, mode=mode)))
    print("(7) %s two-site rest |w| = %s ; 2 d N e = %.6f ; 2 d N = %.6f" % (mode, np.round(w, 6), 2 * d * Nn * e, 2 * d * Nn))
