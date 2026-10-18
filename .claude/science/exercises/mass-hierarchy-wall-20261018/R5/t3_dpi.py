#!/usr/bin/env python3
"""R5 T3: what data processing does and does not forbid for iterated lossy rungs (finite-dim illustration)."""
import numpy as np
from scipy.linalg import logm, expm

def D(r, s):
    return float(np.real(np.trace(r @ (logm(r) - logm(s))))) / np.log(2)

def apply(K, r):
    return sum(k @ r @ k.conj().T for k in K)

def tm(K, d):
    """transfer matrix on vec(rho)"""
    return sum(np.kron(k, k.conj()) for k in K)

# (i) amplitude damping after z-rotation: attracting spiral
g, phi = 0.05, 0.7
Rz = np.diag([np.exp(-1j*phi/2), np.exp(1j*phi/2)])
K = [np.array([[1, 0], [0, np.sqrt(1-g)]]) @ Rz, np.array([[0, np.sqrt(g)], [0, 0]]) @ Rz]
ev = np.linalg.eigvals(tm(K, 2))
sig = np.diag([1.0 - 1e-12, 1e-12]).astype(complex)  # fixed point |0><0| (regularised)
sig = np.array([[1, 0], [0, 0]], complex)
# use full-rank reference: fixed point of K composed with weak depolarising to keep logs finite
p = 1e-3
def Phi(r):
    r2 = apply(K, r)
    return (1-p)*r2 + p*np.eye(2)/2
# fixed point by iteration
s = np.eye(2)/2
for _ in range(20000): s = Phi(s)
r = 0.98*np.array([[0.5, 0.5], [0.5, 0.5]], complex) + 0.01*np.eye(2)
Ds, bloch = [], []
for n in range(60):
    Ds.append(D(r, s)); bloch.append((2*r[0, 1].real, 2*r[0, 1].imag))
    r = Phi(r)
mono = all(Ds[i+1] <= Ds[i] + 1e-12 for i in range(len(Ds)-1))
ang = np.unwrap(np.angle([complex(*b) for b in bloch]))
print(f'(i) eigenvalues of transfer matrix: {np.round(ev, 4)}; complex pair |lam| = {abs(ev[np.argmax(abs(ev.imag))]):.4f}')
print(f'    D(Phi^n rho || sigma) monotone non-increasing: {mono}; first/last D = {Ds[0]:.3f}/{Ds[-1]:.2e}; '
      f'coherence winds {abs(ang[-1]-ang[0])/(2*np.pi):.1f} turns while shrinking (attracting spiral)')

# (ii) protected qubit rotated by 2pi/5, other qubit depolarised: peripheral eigenvalues, a period-5 state cycle
th = 2*np.pi/5
U = np.diag([1, np.exp(1j*th)])
def Phi2(r):
    r4 = r.reshape(2, 2, 2, 2)
    rA = np.einsum('ajbj->ab', r4)  # trace out B
    rA = U @ rA @ U.conj().T
    return np.kron(rA, np.eye(2)/2)
# transfer matrix numerically
B = np.eye(16)
T = np.stack([Phi2(B[:, k].reshape(4, 4)).reshape(16) for k in range(16)], 1)
evs = np.linalg.eigvals(T)
per = evs[np.isclose(np.abs(evs), 1, atol=1e-10)]
r0 = np.kron(np.array([[0.5, 0.5], [0.5, 0.5]]), np.eye(2)/2).astype(complex)
r0 = 0.9*r0 + 0.1*np.eye(4)/4
sref = np.eye(4)/4
orb = [r0]
for _ in range(10): orb.append(Phi2(orb[-1]))
cyc = np.linalg.norm(orb[5] - orb[0]) < 1e-12 and np.linalg.norm(orb[1] - orb[0]) > 1e-3
Dc = [D(o, sref) for o in orb]
print(f'(ii) peripheral eigenvalues: {np.round(np.sort_complex(per), 4)}')
print(f'     period-5 cycle of states: {cyc}; D along cycle = {np.round(Dc[:6], 6)} (DPI equality on the protected qubit)')

# (iii) random channels with full Kraus rank (4 Kraus ops on a qutrit): spectral gap below 1
rng = np.random.default_rng(1)
gaps = []
for _ in range(200):
    G = rng.normal(size=(12, 3)) + 1j*rng.normal(size=(12, 3))
    Q, _ = np.linalg.qr(G)  # isometry 3 -> 12
    Ks = [Q[3*j:3*j+3, :] for j in range(4)]
    e = np.sort(np.abs(np.linalg.eigvals(tm(Ks, 3))))[::-1]
    gaps.append(e[1])
print(f'(iii) 200 random rank-4 qutrit channels: largest non-unit |eigenvalue| max = {max(gaps):.3f} (no peripheral cycles)')
