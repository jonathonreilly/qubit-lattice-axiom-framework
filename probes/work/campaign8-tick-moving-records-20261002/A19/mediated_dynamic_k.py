"""A19: joint momentum analysis of the dynamic mediated toy (why the right-moving probe branch is sharp).
Joint cell-momentum distribution P(K_A, K_B) after the collision, split by the probe's band velocity sign."""
import sys, numpy as np
from core1d import step, packet, vgroup, plus_band, PI
S = 1024; Mc = S // 2
mA, KA, wA, cA = 1.2, 0.8, 10.0, 150
mp, q, wp, cp = 0.1, -0.05, 30.0, 300
phi = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
T = 400
aA, bA = packet(Mc, mA, KA, wA, cA); aB, bB = packet(Mc, mp, q, wp, cp)
psiA = np.empty(S, complex); psiA[0::2] = aA; psiA[1::2] = bA
psiB = np.empty(S, complex); psiB[0::2] = aB; psiB[1::2] = bB
psi = np.outer(psiA, psiB); dg = np.arange(S); eph = np.exp(1j * phi)
for t in range(T):
    pt = psi.T.copy(); a, b = step(pt[:, 0::2], pt[:, 1::2], mA); pt[:, 0::2] = a; pt[:, 1::2] = b; psi = pt.T.copy()
    a, b = step(psi[:, 0::2], psi[:, 1::2], mp); out = np.empty_like(psi); out[:, 0::2] = a; out[:, 1::2] = b; psi = out
    psi[dg, dg] *= eph
K = 2 * PI * np.arange(Mc) / Mc
# Bloch components: F[cA, cB][KA_idx, KB_idx]
F = {(ca, cb): np.fft.fft2(psi[ca::2, cb::2]) / Mc for ca in (0, 1) for cb in (0, 1)}
uAp = np.array(plus_band(K, mA)); uBp = np.array(plus_band(K, mp))           # (2, Mc) + band vectors
uAm = np.array([-np.conj(uAp[1]), np.conj(uAp[0])]); uBm = np.array([-np.conj(uBp[1]), np.conj(uBp[0])])
def proj(uA, uB):
    amp = sum(np.conj(uA[ca])[:, None] * np.conj(uB[cb])[None, :] * F[(ca, cb)] for ca in (0, 1) for cb in (0, 1))
    return np.abs(amp) ** 2
P = {(sa, sb): proj(uA, uB) for sa, uA in (("+", uAp), ("-", uAm)) for sb, uB in (("+", uBp), ("-", uBm))}
tot = sum(p.sum() for p in P.values())
vB = vgroup(K, mp)
def wrap(x): return (x + PI) % (2 * PI) - PI
print(f"phi={phi}: total weight {tot:.10f}")
for key, p in P.items():
    print(f"  mover band {key[0]}, probe band {key[1]}: weight {p.sum():.4f}")
# probe right-moving = (+ band & vB>0) or (- band & vB<0)
right = P[("+", "+")] * (vB[None, :] > 0) + P[("-", "+")] * (vB[None, :] > 0) + P[("+", "-")] * (vB[None, :] < 0) + P[("-", "-")] * (vB[None, :] < 0)
wr = right.sum()
print(f"  probe right-moving weight {wr:.4f}")
pKA = right.sum(1) / wr
gentle = np.abs(wrap(K - (KA + 2 * q))) < 0.15     # mover recoil -2|q| channel: K_A' ~ K_A - 0.1
near = np.abs(wrap(K - KA)) < 0.15
print(f"  in the right-moving-probe branch: P(K_A' within 0.15 of K_A + 2q = {KA+2*q:.2f}) = {pKA[gentle].sum():.4f}; "
      f"within 0.15 of K_A = {pKA[near].sum():.4f}; elsewhere (hard, lattice-scale transfers) = {1 - pKA[gentle | near].sum():.4f}")
pKB = right.sum(0) / wr
print(f"  right-moving probe K_B': fraction within 0.15 of -q = {(pKB[np.abs(wrap(K + q)) < 0.15]).sum():.4f}")
# mover-band flip weight overall
print(f"  mover left its band (- band weight): {P[('-', '+')].sum() + P[('-', '-')].sum():.4f}")
