#!/usr/bin/env python3
"""A24 S5 (supplied toy): full mediated + SETTLED registration chain in continuous time (energy exactly conserved).
Mover chain A (heavy, J_A = 0.05) under the probe chain B (J_B = 1), contact energy U on rungs; the probe reflected
by the mover travels on to a trap at junction j0 (as in S4), where capture emits a photon on chain C.
The record is ONE site: the trap.  Questions:
  (1) energy injected by the trap record vs time (formula -2 Re g sum_a conj(psi[a,C0]) psi[a,Bj0]);
  (2) the same instant: sharp record of the probe on B (single excitation) for comparison;
  (3) what the trap record does to the mover: recoil (momentum shift ~ -2|q|), spread, energy change.
"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

LB, LC = 400, 300
JB, JC, V, g, U = 1.0, 1.0, 1.0, 1.0, 1.5
j0 = 305
JA, KA, wA, xA0 = 0.05, 0.5, 8.0, 200      # mover position in B coordinates
LA, off = 100, 160                         # mover chain window: A site a <-> B site a + off
q, wB, xB0 = -0.3, 12.0, 250
NN = LB + LC

Hn = sp.lil_matrix((NN, NN))
for x in range(LB - 1):
    Hn[x, x + 1] = Hn[x + 1, x] = -JB
for z in range(LC - 1):
    Hn[LB + z, LB + z + 1] = Hn[LB + z + 1, LB + z] = -JC
for z in range(LC):
    Hn[LB + z, LB + z] = -V
Hn[LB, j0] = Hn[j0, LB] = g
Hn = Hn.tocsr()
HA1 = sp.diags([-JA * np.ones(LA - 1), -JA * np.ones(LA - 1)], [-1, 1], format="csr")
contact = np.zeros((LA, NN))
for a in range(LA):
    contact[a, a + off] = U
HA = sp.kron(HA1, sp.identity(NN), format="csr")
HN = sp.kron(sp.identity(LA), Hn, format="csr")
HU = sp.diags(contact.ravel(), format="csr")
H = (HA + HN + HU).tocsr()


def ev(op, v):
    return np.vdot(v, op @ v).real


a = np.arange(LA)
psiA = np.exp(-(a + off - xA0) ** 2 / (4 * wA ** 2) + 1j * KA * a); psiA /= np.linalg.norm(psiA)
x = np.arange(LB)
psiN = np.zeros(NN, complex); psiN[:LB] = np.exp(-(x - xB0) ** 2 / (4 * wB ** 2) + 1j * q * x); psiN /= np.linalg.norm(psiN)
psi0 = np.outer(psiA, psiN).ravel()
E0 = ev(H, psi0); EA0 = ev(HA, psi0)


def kstats(blk):
    F = np.fft.fft(blk, n=2048, axis=0)
    n = np.sum(np.abs(F) ** 2, axis=1); n /= n.sum()
    K = 2 * np.pi * np.arange(2048) / 2048
    Km = np.angle(np.sum(n * np.exp(1j * K)))
    d = (K - Km + np.pi) % (2 * np.pi) - np.pi
    return Km, np.sqrt(np.sum(n * d ** 2))


KmA0, sKA0 = kstats(psiA[:, None])
print(f"mover J_A={JA} K_A={KA} at {xA0}; probe q={q} at {xB0}; junction j0={j0}; U={U} V={V} g={g}; dim {LA*NN}")
print(f"start: energy {E0:+.8f}, <H_A> {EA0:+.6f}, mover K {KmA0:+.4f} sd {sKA0:.4f}")
ts = np.arange(0, 381, 20)
snaps = expm_multiply(-1j * H, psi0, start=0, stop=380, num=len(ts), endpoint=True, traceA=0.0)
trapidx = np.arange(LB, NN)
print("  t    P(trap)  dE_trap(direct)  formula      dE(sharp probe record on B)   P(probe within 4 sites of j0)")
for t, psi in zip(ts, snaps):
    P2 = psi.reshape(LA, NN)
    # trap lock: two outcomes, captured (C block) or not (B block)
    vC = np.zeros_like(P2); vC[:, LB:] = P2[:, LB:]
    vB = np.zeros_like(P2); vB[:, :LB] = P2[:, :LB]
    dT = ev(H, vC.ravel()) + ev(H, vB.ravel()) - ev(H, psi)
    form = -2 * np.real(g * np.sum(np.conj(P2[:, LB]) * P2[:, j0]))
    # sharp probe record on B: one outcome per B site, plus 'captured'
    dS = ev(H, vC.ravel()) - ev(H, psi)
    for y in range(LB):
        v = np.zeros_like(P2); v[:, y] = P2[:, y]
        dS += ev(H, v.ravel())
    pnear = np.sum(np.abs(P2[:, j0 - 4:j0 + 5]) ** 2)
    print(f"{t:4d}  {np.sum(np.abs(P2[:, LB:])**2):.4f}  {dT:+.3e}       {form:+.3e}      {dS:+.4f}                       {pnear:.2e}")
psi = snaps[-1]; P2 = psi.reshape(LA, NN)
print(f"final: norm {np.linalg.norm(psi):.12f}, energy {ev(H, psi):+.8f} (start {E0:+.8f})")
pB = np.sum(np.abs(P2[:, :LB]) ** 2, axis=0); pA = np.sum(np.abs(P2) ** 2, axis=1)
xAc = np.dot(pA, a + off)
for name, sel in (("captured (trap record)", np.arange(LB, NN)),
                  ("free probe right of mover, not captured", np.arange(int(xAc + 30), LB)),
                  ("transmitted (left of mover)", np.arange(0, int(xAc - 30)))):
    blk = P2[:, sel]; w = np.sum(np.abs(blk) ** 2)
    eA = np.vdot(blk, HA1 @ blk).real / w
    Km, sK = kstats(blk)
    pa = np.sum(np.abs(blk) ** 2, axis=1); pa /= pa.sum()
    mu = np.dot(pa, a); sdx = np.sqrt(np.dot(pa, (a - mu) ** 2))
    print(f"  given {name}: weight {w:.4f}; mover <H_A> change {eA-EA0:+.3e}; K shift {Km-KmA0:+.4f} (-2|q| = {-2*abs(q):+.2f}); "
          f"K sd {sK:.4f} (start {sKA0:.4f}); position sd {sdx:.2f}")
