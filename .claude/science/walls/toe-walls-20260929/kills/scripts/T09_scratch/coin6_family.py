"""Exact coin-6 family: U(k) = D(k) C, C = e^{ia}PA + e^{ib}PE + e^{ig}PT (commutes with all 24 rotations).
 (1) alpha = gamma: isotropic linear cone speed 1/sqrt3 (measured); (2) alpha != gamma: curved massive branch with isotropic k^2 coefficient."""
import numpy as np
from common import *
exec(open('test3_stochastic_vs_unitary.py').read().split("rng = np.random.default_rng(11)")[0].split("print('eigenvalues")[0])   # builds I6, Rev, Side
# re-create projectors (same as in test3)
Pa = np.ones((6, 6)) / 6
odd = np.zeros((6, 3)); even = np.zeros((6, 3))
for i in range(3):
    odd[2 * i, i] = 1 / np.sqrt(2); odd[2 * i + 1, i] = -1 / np.sqrt(2)
    even[2 * i, i] = 1 / np.sqrt(2); even[2 * i + 1, i] = 1 / np.sqrt(2)
Pt = odd @ odd.T; Pe = even @ even.T - Pa
def Dk(k): return np.diag([np.exp(1j * (k @ v)) for v in DIRS])
def spec(al, be, ga, k):
    C = np.exp(1j * al) * Pa + np.exp(1j * be) * Pe + np.exp(1j * ga) * Pt
    return np.linalg.eigvals(Dk(k) @ C), C
dirs = {'100': np.array([1, 0, 0.]), '110': np.array([1, 1, 0.]) / np.sqrt(2), '111': np.array([1, 1, 1.]) / np.sqrt(3), '123': np.array([1, 2, 3.]) / np.sqrt(14)}
print('(1) alpha=gamma=0, beta=pi/2: max eigenphase shift / |k| (cone speed), |k|=1e-4; 1/sqrt3 =', round(1 / np.sqrt(3), 5))
for n, d in dirs.items():
    lam, _ = spec(0, np.pi / 2, 0, 1e-4 * d)
    ph = np.angle(lam)
    print('   dir', n, 'speed', round(np.max(np.abs(np.where(np.abs(ph) < 1, ph, 0))) / 1e-4, 5))
print('(2) alpha=0, gamma=0.6, beta=pi/2: A-band eigenphase shift / |k|^2 ; theory -g^2/Delta with g^2=1/3, Delta=0.6 approx (via 2-level):')
for n, d in dirs.items():
    k = 1e-2 * d
    lam, _ = spec(0, np.pi / 2, 0.6, k)
    ph = np.angle(lam)
    a_band = ph[np.argmin(np.abs(ph))]
    print('   dir', n, 'delta_phi/k^2 =', round(a_band / 1e-4, 4))
# stochastic vs unitary: only permutation matrices are in both classes
print('(3) coins that are BOTH row-stochastic (nonnegative entries) and unitary: enumerating eigenphases on grid (a,b,g) with entries >= 0')
cnt = 0; hits = []
for al in np.linspace(0, 2 * np.pi, 25):
    for be in np.linspace(0, 2 * np.pi, 25):
        for ga in np.linspace(0, 2 * np.pi, 25):
            C = np.exp(1j * al) * Pa + np.exp(1j * be) * Pe + np.exp(1j * ga) * Pt
            if np.max(np.abs(C.imag)) < 1e-9 and np.min(C.real) > -1e-9:
                hits.append((round(al, 3), round(be, 3), round(ga, 3), np.round(C.real[0], 3)))
uniq = {}
for h in hits: uniq[tuple(h[3])] = h
for v in uniq.values(): print('   ', v)
