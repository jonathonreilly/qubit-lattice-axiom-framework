#!/usr/bin/env python3
"""A22 task 3 (supplied toy): many-body heating at the tick frequency vs change per beat.

Ring of L qubits, half filling.  Generator H0 = sum_b SWAP_b (even bonds weight 1, odd bonds weight 1-2m/pi)
                                             + Jz sum n_s n_{s+1} + J2 sum n_s n_{s+2}   (diagonal, non-integrable)
Step  U(theta) = exp(-i theta V) * L_odd(theta (1-2m/pi)) * L_even(theta),  L = prod exp(-i angle SWAP_b).
theta -> 0: Trotterised H0 (small change per beat).  theta = pi/2: even layer = full swap, odd = pi/2 - m:
A19's round plus diagonal interactions (time-doubler symmetry exact).
Start: ground state of H0 in the half-filled sector.  Heating fraction e(t) = (<H0>_t - E_gs)/(E_inf - E_gs),
E_inf = sector average of H0 (infinite temperature).

usage: heat.py L T theta1,theta2,...
"""
import sys, time, numpy as np
from scipy.sparse.linalg import eigsh, LinearOperator

L = int(sys.argv[1]); T = int(sys.argv[2]); thetas = [float(x) for x in sys.argv[3].split(",")]
m = 0.3; Jz = 0.5; J2 = 0.7
wo = 1 - 2 * m / np.pi
dim = 2 ** L
bits = (np.arange(dim)[:, None] >> (L - 1 - np.arange(L))[None, :]) & 1    # bits[i, s] = n_s (site s = axis s)
Nsec = bits.sum(1) == L // 2
Vdiag = (Jz * sum(bits[:, s] * bits[:, (s + 1) % L] for s in range(L)) +
         J2 * sum(bits[:, s] * bits[:, (s + 2) % L] for s in range(L))).astype(float)
bond_w = np.array([1.0 if s % 2 == 0 else wo for s in range(L)])          # bond (s, s+1)


def swap_apply(psi, s):
    t = psi.reshape([2] * L)
    return np.swapaxes(t, s, (s + 1) % L).reshape(dim)


def H0(psi):
    out = Vdiag * psi
    for s in range(L):
        out = out + bond_w[s] * swap_apply(psi, s)
    return out


def gate_layer(psi, angle, parity):
    # exp(-i a SWAP) = cos a - i sin a SWAP  on bonds (s, s+1), s = parity mod 2 (disjoint, commuting)
    c, sn = np.cos(angle), np.sin(angle)
    for s in range(parity, L, 2):
        psi = c * psi - 1j * sn * swap_apply(psi, s)
    return psi


# ground state of H0 in the half-filled sector
idx = np.nonzero(Nsec)[0]
def mv(x):
    full = np.zeros(dim, complex); full[idx] = x
    return H0(full)[idx]
op = LinearOperator((idx.size, idx.size), matvec=mv, dtype=complex)
rng = np.random.default_rng(0)
Egs, vgs = eigsh(op, k=1, which="SA", v0=rng.normal(size=idx.size) + 0j, tol=1e-10)
E_gs = Egs[0]
diagH = Vdiag.copy()                       # sector trace of H0: SWAP diagonal = 1 when n_s = n_{s+1}
for s in range(L):
    diagH += bond_w[s] * (bits[:, s] == bits[:, (s + 1) % L])
E_inf = diagH[Nsec].mean()
print(f"L={L} half filling dim={idx.size}; m={m} Jz={Jz} J2={J2}; E_gs={E_gs:.6f} E_inf={E_inf:.6f} (per site {E_gs/L:.4f}, {E_inf/L:.4f})")
psi0 = np.zeros(dim, complex); psi0[idx] = vgs[:, 0]
for th in thetas:
    t0 = time.time()
    psi = psi0.copy()
    phV = np.exp(-1j * th * Vdiag)
    ts, es = [], []
    for t in range(1, T + 1):
        psi = gate_layer(psi, th, 0)
        psi = gate_layer(psi, th * wo, 1)
        psi = phV * psi
        if t % 5 == 0 or t < 20:
            ts.append(t); es.append((np.vdot(psi, H0(psi)).real - E_gs) / (E_inf - E_gs))
    ts = np.array(ts); es = np.array(es)
    # window averages over [t/2, t] at log-spaced t
    wins = []
    tt = 20
    while tt <= T:
        sel = (ts > tt / 2) & (ts <= tt)
        wins.append((tt, es[sel].mean()))
        tt *= 2
    tstar = next((tt for tt, e in wins if e > 0.5), None)
    s = "  ".join(f"{tt}:{e:.3f}" for tt, e in wins)
    print(f"theta={th:.4f} (1/theta={1/th:.3f}): window-avg heating fraction [t/2,t]  {s}   | t*(>0.5) = {tstar}   [{time.time()-t0:.1f}s]")
    sys.stdout.flush()
