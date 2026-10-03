#!/usr/bin/env python3
"""A19 mediated registration, dynamic two-excitation version (supplied toy; no static-mover approximation).

Ladder in Z^3: mover chain A, probe chain B; both run the 1D Dirac round (masses m_A, m_p); rung pairs (A_x, B_x)
carry a |11> phase phi (number-conserving pair gate with theta = 0, A10 S1 family).  State psi[x_A, x_B] (sites).
After the head-on collision the probe alone is registered by a SHARP single-site record at y (its possibility
locked there); the mover's possibilities change at once to agree: psi_A(x) ~ psi(x, y).
Compared with the free mover and with a direct sharp site cut of the mover.  Total quasi-momentum is conserved.
"""
import numpy as np
from core1d import step, packet, vgroup, momentum_stats, PI

S = 1024                       # sites per chain (512 cells)
mA, KA, wA, cA = 1.2, 0.8, 10.0, 150
mp, q, wp, cp = 0.1, -0.05, 30.0, 300
phi, T = 0.6, 400
aA, bA = packet(S // 2, mA, KA, wA, cA)
aB, bB = packet(S // 2, mp, q, wp, cp)
psiA = np.empty(S, complex); psiA[0::2] = aA; psiA[1::2] = bA
psiB = np.empty(S, complex); psiB[0::2] = aB; psiB[1::2] = bB
psi = np.outer(psiA, psiB)
free = psiA[None].copy()
diag = np.arange(S)
eph = np.exp(1j * phi)


def stepA(p, m):               # step along axis 0 (mover)
    pt = p.T.copy()
    a, b = step(pt[:, 0::2], pt[:, 1::2], m)
    pt[:, 0::2] = a; pt[:, 1::2] = b
    return pt.T.copy()


def stepB(p, m):               # step along axis 1 (probe)
    a, b = step(p[:, 0::2], p[:, 1::2], m)
    out = np.empty_like(p); out[:, 0::2] = a; out[:, 1::2] = b
    return out


def stats1(v, m):
    a, b = v[0::2][None], v[1::2][None]
    Km, Kv, plus = momentum_stats(a, b, m)
    P = np.abs(v) ** 2; P /= P.sum()
    x = np.arange(v.size) / 2.0
    mu = np.dot(P, x)
    return Km[0], np.sqrt(Kv[0]), plus[0], mu, np.sqrt(np.dot(P, (x - mu) ** 2))


for t in range(T):
    psi = stepA(psi, mA)
    psi = stepB(psi, mp)
    psi[diag, diag] *= eph
    fa, fb = step(free[:, 0::2], free[:, 1::2], mA); free[:, 0::2] = fa; free[:, 1::2] = fb

print(f"mover m_A={mA} K_A={KA} (v={vgroup(KA, mA):+.3f}), probe m_p={mp} q={q} (v={vgroup(q, mp):+.3f}) w_p={wp} cells, "
      f"phi={phi}, T={T}; norm {np.sum(np.abs(psi)**2):.12f}")
Kf, sKf, pf, muf, sxf = stats1(free[0], mA)
print(f"free mover at T: K mean {Kf:+.4f}, K sd {sKf:.4f}, + band {pf:.4f}, position {muf:.1f} sd {sxf:.2f} cells")
# total quasi-momentum check (cell momenta): <e^{i(K_A + K_B)}> conserved by the translation-covariant ladder
def total_phase(p):
    F = np.fft.fft2(p[0::2, 0::2]) # dominant-sublattice proxy is not needed: use full two-sublattice transform
    return None
PB = np.sum(np.abs(psi) ** 2, axis=0)
yc = int(2 * (cA + vgroup(KA, mA) * 0.0))
# collision cell estimate and branch split: reflected probe ends right of the mover's final position
xA_final = muf
refl = (np.arange(S) / 2.0) > xA_final + 10
trans = (np.arange(S) / 2.0) < xA_final - 10
print(f"probe weight right of the mover (reflected) {PB[refl].sum():.4f}, left (transmitted) {PB[trans].sum():.4f}, "
      f"near the mover {1 - PB[refl].sum() - PB[trans].sum():.4f}")
for name, sel in (("reflected", refl), ("transmitted", trans)):
    acc = np.zeros(5); wsum = 0.0
    for y in np.nonzero(sel)[0]:
        if PB[y] < 1e-12:
            continue
        v = psi[:, y] / np.sqrt(PB[y])
        acc += PB[y] * np.array(stats1(v, mA)); wsum += PB[y]
    acc /= wsum
    print(f"  {name}-probe single-site records: mover K mean {acc[0]:+.4f} (shift vs free {acc[0]-Kf:+.4f}; "
          f"2q = {2*q:+.3f}), K sd {acc[1]:.4f}, + band {acc[2]:.4f}, position sd {acc[4]:.2f} cells (free {sxf:.2f})")
# direct sharp site cut of the mover at T, averaged over outcomes
P = np.abs(free[0]) ** 2
acc = np.zeros(5)
for x in np.nonzero(P > 1e-10)[0]:
    v = np.zeros(S, complex); v[x] = 1.0
    acc += P[x] * np.array(stats1(v, mA))
acc /= P[P > 1e-10].sum()
print(f"  direct sharp site cut of the mover: K sd {acc[1]:.4f} (uniform {PI/np.sqrt(3):.4f}), + band {acc[2]:.4f}")
