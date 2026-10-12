"""R16-10 evaluator: F_s(m, lam) by the IR-excised split (proved identity, report section 3):
  F = sum_BZ f_lat (1 - chi(|q|)) / N^3  +  int_{R^3} f_cont chi(|q|)        (chi = 1 on |q|<=r0, 0 beyond r1 < box)
and F_s(0+) = K_s + lim_{m,lam->0} sum_BZ f_lat (1 - chi)/N^3, K_0 = -1/3, K_1/2 = +2/3.
"""
import numpy as np, time
from r1610_core import *
K = {0: -1/3, 0.5: 2/3}

def bz_pts(N, chunk_axis=None):
    q1 = bz_grid(N)
    QX, QY, QZ = np.meshgrid(q1, q1, q1, indexing='ij')
    return QX.ravel(), QY.ravel(), QZ.ravel()

def lattice_part(spin, N, m, lam, matter, d, r0, r1, h=0.02, chunk=None):
    q1 = bz_grid(N)
    QY, QZ = np.meshgrid(q1, q1, indexing='ij')
    vals = {}
    tot = {p: 0.0 for p in (0.0, h, 2*h)}; part = {p: 0.0 for p in (0.0, h, 2*h)}; Ep = {}
    for ix in range(N):
        qx = np.full_like(QY, q1[ix]); r = np.sqrt(qx**2 + QY**2 + QZ**2)
        wt = (1 - chi(r, r0, r1))/N**3
        for p in (0.0, h, 2*h):
            if spin == 0:
                a, sea, ex, E = scalar_pt(qx, QY, QZ, p, m, lam, matter, d)
            else:
                a, acc, sea, E = dirac_pt(qx, QY, QZ, p, m, lam, matter[0], matter[1], d)
            tot[p] += np.sum(wt*a); part[p] += np.sum(wt*sea); Ep[p] = E
    if spin == 0:
        F = tot; T = part
    else:
        F = {p: 2*Ep[p]*tot[p] for p in tot}; T = {p: 2*Ep[p]*part[p] for p in part}
    return rich(F[0.0], F[h], F[2*h], h)/2*U, rich(T[0.0], T[h], T[2*h], h)/2*U

def cont_part(spin, m, lam, r0, r1, h=0.02, nr=12, nmu=32):
    pts, wts, rr = sph_points(4*r1, nr, nmu)
    w = wts*chi(rr, r0, r1)
    u = lambda k: np.asarray(k, float)**2; d = lambda q: np.asarray(q, float)
    if spin == 0:
        return speed_scalar(pts, w, m, lam, u, d, h)[0]
    S = lambda k: np.asarray(k, float); Wz = lambda k: 0.0*np.asarray(k, float)
    return speed_dirac(pts, w, m, lam, S, Wz, d, h)[0]
