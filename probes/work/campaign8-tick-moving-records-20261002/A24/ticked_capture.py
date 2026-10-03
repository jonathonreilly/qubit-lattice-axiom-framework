#!/usr/bin/env python3
"""A24 S8 (supplied toy): the capture-trap record on the TICKED Dirac round (A19 core), with the conserved lifted energy
E = arccos(-(U + U^dag)/2) of the whole network's tick U (a function of U, so exactly conserved; quasi-local).
Network: probe ring B (A19 round, mass m_B) and photon ring C (mass m_C); C-states = 'probe held in the trap AND photon
at z'.  Each tick: U = G_cap(theta_c) (U_B + U_C), G_cap a partial swap between site j0 of B and site 0 of C.
The trap record is one site: P_t = projector on all C-states.  Reported vs tick: P(trap); energy injected by a trap
lock; by a sharp probe record on B; by a sharp photon record on C.  Part 2: per-tick formation F = f P_t, energy per record.
usage: ticked_capture.py m_C [theta_c]
"""
import sys
import numpy as np
sys.path.insert(0, "/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/"
                   "34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A19")
from core1d import step, packet, vgroup, PI

mB, q, w, c0 = 0.3, 0.3, 10.0, 150
mC = float(sys.argv[1]) if len(sys.argv) > 1 else 0.05
thc = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
MB, MC = 300, 400
NB, NC = 2 * MB, 2 * MC
N = NB + NC
j0 = 2 * 250                                   # junction: even site of cell 250 on B


def tick_matrix():
    U = np.zeros((N, N), complex)
    for i in range(NB):                        # columns = images of basis vectors
        a = np.zeros(MB, complex); b = np.zeros(MB, complex)
        (a if i % 2 == 0 else b)[i // 2] = 1.0
        a2, b2 = step(a, b, mB)
        U[0:NB:2, i] = a2; U[1:NB:2, i] = b2
    for i in range(NC):
        a = np.zeros(MC, complex); b = np.zeros(MC, complex)
        (a if i % 2 == 0 else b)[i // 2] = 1.0
        a2, b2 = step(a, b, mC)
        U[NB + 0:N:2, NB + i] = a2; U[NB + 1:N:2, NB + i] = b2
    G = np.eye(N, dtype=complex)
    G[j0, j0] = G[NB, NB] = np.cos(thc)
    G[j0, NB] = G[NB, j0] = -1j * np.sin(thc)
    return G @ U


U = tick_matrix()
print(f"unitarity |U^dag U - 1| = {np.abs(U.conj().T @ U - np.eye(N)).max():.1e}")
A = (U + U.conj().T) / 2
lam, Vv = np.linalg.eigh(A)
E = (Vv * np.arccos(np.clip(-lam, -1, 1))) @ Vv.conj().T          # lifted energy, Hermitian, commutes with U
del A
print(f"[E, U] = {np.abs(E @ U - U @ E).max():.1e}; spectrum of E in [{np.arccos(np.clip(-lam,-1,1)).min():.4f}, "
      f"{np.arccos(np.clip(-lam,-1,1)).max():.4f}]; m_B={mB}, m_C={mC}, theta_c={thc}")
a, b = packet(MB, mB, q, w, c0)
psi0 = np.zeros(N, complex); psi0[0:NB:2] = a; psi0[1:NB:2] = b
E0 = np.vdot(psi0, E @ psi0).real
WB = np.arccos(np.cos(mB) * np.cos(q))
kC = np.arccos(np.clip(np.cos(WB) / np.cos(mC), -1, 1))
print(f"probe q={q} v={vgroup(q, mB):.3f} cells/tick, <E>={E0:.5f} (W_B(q)={WB:.5f}); matched photon k={kC:.4f} "
      f"(v={vgroup(kC, mC):.3f}); band centre pi/2")
Ptrap = np.zeros(N); Ptrap[NB:] = 1.0


def dE_diag(psi, blocks):
    tot = -np.vdot(psi, E @ psi).real
    for idx in blocks:
        v = np.zeros_like(psi); v[idx] = psi[idx]
        tot += np.vdot(v, E @ v).real
    return tot


def dE_sharp(psi, lo, hi):
    """sharp record of the excitation on sites lo..hi-1 (one outcome per site) + the rest as one outcome."""
    Ed = np.real(np.diag(E))
    p = np.abs(psi) ** 2
    rest = np.ones(N, bool); rest[lo:hi] = False
    v = np.where(rest, psi, 0)
    return np.sum(p[lo:hi] * Ed[lo:hi]) + np.vdot(v, E @ v).real - np.vdot(psi, E @ psi).real


trap_blocks = [np.arange(NB, N), np.arange(NB)]
psi = psi0.copy()
print("  t   P(trap)   dE_trap lock   dE sharp probe(B)   dE sharp photon(C)")
for t in range(0, 401):
    if t % 25 == 0:
        print(f"{t:4d}  {np.sum(np.abs(psi[NB:])**2):.4f}   {dE_diag(psi, trap_blocks):+.3e}     {dE_sharp(psi, 0, NB):+.4f}"
              f"            {dE_sharp(psi, NB, N):+.4f}")
    psi = U @ psi
print(f"final: norm {np.linalg.norm(psi):.12f}; <E> {np.vdot(psi, E @ psi).real:.8f} (start {E0:.8f})")

print("per-tick formation F = f P_trap: energy per record")
for f in (0.03, 0.01, 0.003):
    c = 1 - np.sqrt(1 - f); Kn = 1 - c * Ptrap
    psi = psi0.copy(); inj = 0.0; rec = 0.0
    for t in range(400):
        psi = U @ psi
        vf = np.sqrt(f) * Ptrap * psi; vn = Kn * psi
        inj += np.vdot(vf, E @ vf).real + np.vdot(vn, E @ vn).real - np.vdot(psi, E @ psi).real
        rec += np.vdot(vf, vf).real
        psi = vn
    tot = rec + np.sum(Ptrap * np.abs(psi) ** 2)
    print(f"   f={f}: injected/record = {inj/tot:+.4e}  (/f = {inj/tot/f:+.4f}); expected records {tot:.4f}")
