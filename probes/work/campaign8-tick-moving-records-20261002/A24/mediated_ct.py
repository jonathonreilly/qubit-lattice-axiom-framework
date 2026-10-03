#!/usr/bin/env python3
"""A24 S2 (supplied toy): energy budget of a MEDIATED registration in continuous time (energy exactly conserved
by the unitary part).  Ladder: mover chain A (hopping J_A, heavy: m_A = 1/(2 J_A)), probe chain B (hopping J_B = 1),
contact energy U n_A(x) n_B(x) on rungs.  Two-excitation wavefunction psi[x_A, x_B], open chains of L sites.

Stage 1 (unitary): the probe packet (momentum q < 0, coming from the right) hits the slow mover and splits into a
reflected and a transmitted part.  Stage 2 (lock): a sharp one-site record of the probe (record wherever it is, or a
reflected-probe record).  Bookkeeping (L1):
   dE_lock = sum_y <P_y H P_y> - <H>;  P_y commutes with H_A and with the contact term, so
   dE_lock = -<H_B>  (the probe's depth below its band centre), and the mover's mean energy is unchanged by the lock.
Compared with direct locks on the mover: sharp (-<H_A>) and Gaussian of width sigma (J_A cos K /(4 sigma^2)).
usage: mediated_ct.py q1,q2,...   (probe momenta, negative)
"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

L = 260
JA, KA, wA, xA0 = 0.05, 0.5, 8.0, 110
JB, wB, xB0 = 1.0, 12.0, 155
U = 1.5


def hop(L, J):
    d = -J * np.ones(L - 1)
    return sp.diags([d, d], [-1, 1], format="csr")


HA1 = hop(L, JA); HB1 = hop(L, JB)
I = sp.identity(L, format="csr")
HA = sp.kron(HA1, I, format="csr"); HB = sp.kron(I, HB1, format="csr")
eq = (np.arange(L)[:, None] == np.arange(L)[None, :]).astype(float).ravel()
HU = sp.diags(U * eq, format="csr")
H = (HA + HB + HU).tocsr()


def pk(x0, k, w):
    x = np.arange(L)
    p = np.exp(-(x - x0) ** 2 / (4 * w ** 2) + 1j * k * x)
    return p / np.linalg.norm(p)


def ev(op, v):
    return np.vdot(v, op @ v).real


def kstats(amp2d):
    """mover momentum distribution of a (L, nB) block: circular mean and sd (radians per site)."""
    F = np.fft.fft(amp2d, n=2048, axis=0)
    n = np.sum(np.abs(F) ** 2, axis=1); n /= n.sum()
    K = 2 * np.pi * np.arange(2048) / 2048
    z = np.sum(n * np.exp(1j * K)); Km = np.angle(z)
    d = (K - Km + np.pi) % (2 * np.pi) - np.pi
    return Km, np.sqrt(np.sum(n * d ** 2))


qs = [float(v) for v in sys.argv[1].split(",")] if len(sys.argv) > 1 else [-0.3]
psiA = pk(xA0, KA, wA)
EA0 = np.vdot(psiA, HA1 @ psiA).real
KA0, sKA0 = kstats(psiA[:, None])
print(f"mover: J_A={JA} (m_A={1/(2*JA):.0f}), K_A={KA}, v_A={2*JA*np.sin(KA):.4f}, w_A={wA}; <H_A>={EA0:+.6f}; "
      f"K sd {sKA0:.4f}.  contact U={U}, L={L}")
print(f"direct locks on the mover instead: sharp dE = -<H_A> = {-EA0:+.5f} (mover half-bandwidth 2J_A = {2*JA}); "
      f"Gaussian sigma = w_B = {wB}: J_A cos K_A/(4 sigma^2) = {JA*np.cos(KA)/(4*wB**2):.3e}")
for q in qs:
    vB = 2 * JB * np.sin(abs(q))
    vA = 2 * JA * np.sin(KA)
    T = (xB0 - xA0) / (vB + vA) + (4 * wB + 4 * wA + 10) / vB
    psiB = pk(xB0, q, wB)
    psi = np.outer(psiA, psiB).ravel()
    E = [ev(HA, psi), ev(HB, psi), ev(HU, psi)]
    psi = expm_multiply(-1j * H * T, psi, traceA=0.0)
    E1 = [ev(HA, psi), ev(HB, psi), ev(HU, psi)]
    P2 = psi.reshape(L, L)
    pA = np.sum(np.abs(P2) ** 2, axis=1); xAc = np.dot(pA, np.arange(L))
    pB = np.sum(np.abs(P2) ** 2, axis=0)
    xs = np.arange(L)
    R = xs > xAc + 4 * wA; Tm = xs < xAc - 4 * wA
    pR, pT = pB[R].sum(), pB[Tm].sum()
    # energies conditional on the probe branch
    def cond(sel):
        blk = P2[:, sel]; nrm = np.sum(np.abs(blk) ** 2)
        ea = np.vdot(blk, HA1 @ blk).real / nrm
        eb = np.vdot(blk.T, HB1[np.ix_(sel, sel)] @ blk.T).real / nrm
        Km, sK = kstats(blk)
        return ea, eb, Km, sK
    eaR, ebR, KmR, sKR = cond(R)
    eaT, ebT, KmT, sKT = cond(Tm)
    # full sharp probe lock, outcome-averaged: sum_y <P_y H P_y> - <H>
    dE_lock = -E1[0] - E1[1] - E1[2]
    for y in range(L):
        v = np.zeros((L, L), complex); v[:, y] = P2[:, y]; v = v.ravel()
        dE_lock += ev(H, v)
    print(f"\nq={q:+.3f} (v_B={vB:.3f}), T={T:.0f}: norm {np.linalg.norm(psi):.12f}; total energy "
          f"{sum(E):+.8f} -> {sum(E1):+.8f}")
    print(f"   collision: <H_A> {E[0]:+.6f} -> {E1[0]:+.6f}, <H_B> {E[1]:+.6f} -> {E1[1]:+.6f}, contact {E[2]:.1e} -> {E1[2]:.1e};"
          f" P(reflected) {pR:.4f}, P(transmitted) {pT:.4f}")
    print(f"   given reflected probe: mover <H_A> {eaR:+.6f} (change {eaR-EA0:+.3e}), mover K {KmR:+.4f} "
          f"(shift {KmR-KA0:+.4f}; -2|q| = {-2*abs(q):+.3f}), mover K sd {sKR:.4f}; probe <H_B> {ebR:+.5f}")
    print(f"   given transmitted:     mover <H_A> {eaT:+.6f} (change {eaT-EA0:+.3e}), mover K shift {KmT-KA0:+.4f}, K sd {sKT:.4f}")
    print(f"   SHARP PROBE LOCK (record wherever the probe is): dE = {dE_lock:+.6f}; -<H_B> = {-E1[1]:+.6f} "
          f"(2 J_B cos q = {2*JB*np.cos(q):+.4f}); per reflected-probe record: {-ebR:+.5f}; "
          f"mover share of dE: exactly 0")
    sys.stdout.flush()
