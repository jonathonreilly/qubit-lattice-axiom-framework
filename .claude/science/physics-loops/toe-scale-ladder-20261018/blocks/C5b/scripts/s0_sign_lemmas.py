#!/usr/bin/env python3
"""s0: sign/normalisation lemmas used by Theorem L (NOTE.md section 2).

(a) Calibrate the FHS lattice Chern routine against a direct finite-difference integral of
    Ch(P) = (i/2pi) int tr(P dP^dP) on the outward box surface (two different methods).
(b) Lemma S (hand-derived in NOTE): for H = dk.v.sigma, the lower band has Ch = sign det v
    on an outward surface around 0.  Checked for random v of both signs.
(c) Lemma T (hand-derived): (1/24 pi^2) int_{Sigma x [0,1]} tr(theta^3), g = exp(-2 pi i t P),
    orientation (Sigma, t), equals Ch(P).  Checked by direct quadrature.
"""
import numpy as np
import lib5b as L

C = L.Checker()
rng = np.random.default_rng(1)


def P_lower(v):
    def P(K):
        d = K @ v
        n = d / np.linalg.norm(d, axis=-1, keepdims=True)
        H = sum(n[..., j, None, None] * L.PAULI[j] for j in range(3))
        return 0.5 * (np.eye(2) - H)
    return P


def direct_chern(P, lo, hi, M=120):
    faces = L.box_surface_points(lo, hi, M)
    tot = 0.0
    for G in faces:
        Pg = P(G)
        du = (Pg[2:, 1:-1] - Pg[:-2, 1:-1]) / 2
        dv = (Pg[1:-1, 2:] - Pg[1:-1, :-2]) / 2
        Pc = Pg[1:-1, 1:-1]
        t = np.trace(Pc @ (du @ dv - dv @ du), axis1=-2, axis2=-1)
        tot += (1j / (2 * np.pi) * t.sum()).real
    return tot  # grid-step factors cancel (du,dv in index units)


def fhs_raw(P, lo, hi, M=30):
    faces = L.box_surface_points(lo, hi, M)
    tot = 0.0
    for G in faces:
        Pg = P(G)
        w, V = np.linalg.eigh(Pg)
        Q = V[..., :, -1]  # eigenvector of eigenvalue 1
        def lk(a, b):
            return np.sum(a.conj() * b, axis=-1)
        p = lk(Q[:-1, :-1], Q[1:, :-1]) * lk(Q[1:, :-1], Q[1:, 1:]) * lk(Q[1:, 1:], Q[:-1, 1:]) * lk(Q[:-1, 1:], Q[:-1, :-1])
        tot += np.angle(p).sum()
    return tot / (2 * np.pi)


lo, hi = np.array([-1.0, -0.8, -1.2]), np.array([0.9, 1.1, 1.0])
signs = []
for trial in range(6):
    v = rng.normal(size=(3, 3))
    P = P_lower(v)
    dc = direct_chern(P, lo, hi)
    raw = fhs_raw(P, lo, hi)
    sd = np.sign(np.linalg.det(v))
    print(f'  v det sign {sd:+.0f}: direct Ch = {dc:+.4f}, raw FHS sum = {raw:+.6f}')
    C.check(f'Lemma S: Ch(lower band) = sign det v (direct integral, trial {trial})', abs(dc - sd) < 0.05)
    signs.append(np.sign(raw) * np.sign(dc))
    C.check(f'raw FHS is integer (trial {trial})', abs(raw - round(raw)) < 1e-9)
C.check('FHS-to-analytic sign is the same in all trials', len(set(signs)) == 1)
C.check(f'lib5b.CH_SIGN ({L.CH_SIGN}) equals calibrated sign ({signs[0]})', L.CH_SIGN == signs[0])

# (c) Lemma T
for trial in range(3):
    v = rng.normal(size=(3, 3))
    P = P_lower(v)
    M, Nt = 60, 40
    tot = 0.0
    for G in L.box_surface_points(lo, hi, M):
        Pg = P(G)  # (M+1,M+1,2,2)
        du = (Pg[2:, 1:-1] - Pg[:-2, 1:-1]) / 2
        dv = (Pg[1:-1, 2:] - Pg[1:-1, :-2]) / 2
        Pc = Pg[1:-1, 1:-1]
        for t in (np.arange(Nt) + 0.5) / Nt:
            z = np.exp(-2j * np.pi * t)
            g = np.eye(2) + (z - 1) * Pc
            gi = np.eye(2) + (1 / z - 1) * Pc
            Au = gi @ ((z - 1) * du); Av = gi @ ((z - 1) * dv)
            At = gi @ (-2j * np.pi * z * Pc)
            # sum over permutations of (u,v,t): 3[tr(AuAvAt) - tr(AuAtAv)]
            tr = 3 * (np.trace(Au @ Av @ At - Au @ At @ Av, axis1=-2, axis2=-1))
            tot += tr.sum() / Nt
    val = tot / (24 * np.pi ** 2)
    ch = direct_chern(P, lo, hi, M=M)
    print(f'  Lemma T trial {trial}: (1/24pi^2) int tr theta^3 = {val.real:+.4f}{val.imag:+.1e}i, Ch = {ch:+.4f}')
    C.check(f'Lemma T: S^1 x Sigma winding of exp(-2 pi i t P) equals Ch(P) (trial {trial})', abs(val - ch) < 0.05)
C.total()
