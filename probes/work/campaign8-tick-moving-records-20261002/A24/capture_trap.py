#!/usr/bin/env python3
"""A24 S4 (supplied toy): a SETTLED one-site record.  A probe excitation on chain B can be captured at a trap site t
(next to junction site j0), the capture releasing its excess energy as an emitted excitation ('photon') on chain C.
States: |B_x> (probe on B, no photon) and |C_z> (probe held in the trap AND photon at z).  The trap is ONE site; its
occupation projector P_t = sum_z |C_z><C_z| labels the whole captured branch.  Continuous time, energy conserved:
   H = -J_B sum(B hops) - J_C sum(C hops) - V sum_z |C_z><C_z| + g (|C_0><B_j0| + h.c.)
The only energy term that flips the trap is the capture term, so the one-site trap lock costs exactly
   dE_trap(t) = -2 Re[ g conj(psi_C0) psi_Bj0 ]     (L2 applied to the trap)
which vanishes once the probe has left j0 AND the photon has left C_0: the possibility at the trap is then settled.
Compared at the same times with sharp records of the probe on B and of the photon on C (single excitations).
Part 2: A9's per-tick formation instrument with weight F = f P (Kraus sqrt(f) P and sqrt(1 - f P)), f per tick,
placed (i) on the trap, (ii) on a B site on the probe's path, (iii) on a C site on the photon's path:
   energy injected per record, vs f.
"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm

LB, LC = 300, 400
JB, JC, V, g = 1.0, 1.0, 1.0, 1.0
j0 = 200
N = LB + LC
H = np.zeros((N, N))
for x in range(LB - 1):
    H[x, x + 1] = H[x + 1, x] = -JB
for z in range(LC - 1):
    H[LB + z, LB + z + 1] = H[LB + z + 1, LB + z] = -JC
for z in range(LC):
    H[LB + z, LB + z] = -V
H[LB, j0] = H[j0, LB] = g
Hs = sp.csr_matrix(H)

q, wq, x_s = 0.3, 12.0, 130
x = np.arange(LB)
psi0 = np.zeros(N, complex)
psi0[:LB] = np.exp(-(x - x_s) ** 2 / (4 * wq ** 2) + 1j * q * x)
psi0 /= np.linalg.norm(psi0)
E0 = np.vdot(psi0, H @ psi0).real
kph = np.arccos(-(E0 + V) / (2 * JC))
print(f"probe q={q} (v={2*JB*np.sin(q):.3f}), <H>={E0:+.5f} (band centre 0); capture releases V={V}: photon k~{kph:.3f} "
      f"(v={2*JC*np.sin(kph):.3f}); junction j0={j0}, start x={x_s}, coupling g={g}")

Pt = np.zeros(N); Pt[LB:] = 1.0          # trap occupied (diagonal projector)


def dE_diag_partition(psi, blocks):
    """sum_k <P_k H P_k> - <H> for diagonal projectors given as index arrays."""
    tot = -np.vdot(psi, Hs @ psi).real
    for idx in blocks:
        v = np.zeros_like(psi); v[idx] = psi[idx]
        tot += np.vdot(v, Hs @ v).real
    return tot


trap_blocks = [np.arange(LB, N), np.arange(LB)]
B_sharp = [np.array([i]) for i in range(LB)] + [np.arange(LB, N)]
C_sharp = [np.array([LB + z]) for z in range(LC)] + [np.arange(LB)]
U1 = expm(-1j * H * 1.0)
psi = psi0.copy()
print("  t   P(trap)  |psi_Bj0|  |psi_C0|   dE_trap(direct)  -2Re(g c0* bj0)   dE(sharp probe record on B)  dE(sharp photon record on C)")
for t in range(0, 241):
    if t % 10 == 0:
        dT = dE_diag_partition(psi, trap_blocks)
        form = -2 * np.real(g * np.conj(psi[LB]) * psi[j0])
        dB = dE_diag_partition(psi, B_sharp)
        dC = dE_diag_partition(psi, C_sharp)
        print(f"{t:4d}  {np.sum(np.abs(psi[LB:])**2):.4f}  {abs(psi[j0]):.2e}  {abs(psi[LB]):.2e}   {dT:+.3e}       {form:+.3e}"
              f"          {dB:+.4f}                    {dC:+.4f}")
    psi = U1 @ psi
pcap = np.sum(np.abs(psi[LB:]) ** 2)
EB_hop = np.vdot(psi[:LB], (H[:LB, :LB] @ psi[:LB])).real
print(f"final: P(captured) {pcap:.4f}; norm {np.linalg.norm(psi):.12f}; energy {np.vdot(psi, H @ psi).real:+.8f} (start {E0:+.8f})")


# ---------------------------------------------------------------- part 2: per-tick formation instrument
def run_rate(f, where, T=360):
    if where == "trap":
        P = Pt.copy()
    elif where == "B":
        P = np.zeros(N); P[170] = 1.0          # a B site on the probe's path, before the junction
    else:
        P = np.zeros(N); P[LB + 40] = 1.0      # a C site on the photon's path
    c = 1 - np.sqrt(1 - f)
    Kn = 1 - c * P                           # sqrt(1 - f P) for a diagonal projector P
    psi = psi0.copy(); inj = 0.0; rec = 0.0
    for t in range(T):
        psi = U1 @ psi
        e_before = np.vdot(psi, Hs @ psi).real
        vf = np.sqrt(f) * P * psi; vn = Kn * psi
        inj += np.vdot(vf, Hs @ vf).real + np.vdot(vn, Hs @ vn).real - e_before
        rec += np.vdot(vf, vf).real
        psi = vn
    left = np.sum(P * np.abs(psi) ** 2)       # weight still on P in the no-record branch (forms later, at no cost if settled)
    return inj, rec, left


print("\nper-tick formation instrument F = f P: total injected energy / expected records")
print("   f       trap: inj/rec (records)          B site on path: inj/rec (records)      C site: inj/rec (records)")
for f in (1.0, 0.3, 0.1, 0.03, 0.01, 0.003):
    row = []
    for where in ("trap", "B", "C"):
        inj, rec, left = run_rate(f, where)
        tot = rec + (left if where == "trap" else 0.0)
        row.append(f"{inj/tot:+.4e} ({tot:.4f})")
    print(f"   {f:<6}  " + "     ".join(row))
print("   reference depths below band centre: probe on B 2J_B cos q = %.4f; photon on C (relative to its band centre -V): %.4f"
      % (2 * JB * np.cos(q), 2 * JC * np.cos(kph)))
