#!/usr/bin/env python3
"""rotor-rishon: can the Thorngren-Preskill-Fidkowski rotor matter be built from role-assigned one-mode fermion sites?
 A finite carriers: an exact integer turn charge has no unitary raising (no angle); an angle grid keeps only Z_d of the turn
 B the occupation-diagonal lock: turn = cluster fermion number, winding = link rishon number -> every set is on-site,
   anomalous sets pass, V-flux pumps no A-charge for EVERY interacting update; the one-mode Dirac chain pumps 2
 C quasi-energy: a bounded carrier removes one-cell folding but not k-cell folding (k ~ 2 pi / (eps U S^2))
Labels: [T] theorem / exact computation. Supplied model, finite diagnostic; no physical identification.
Cited, not rederived: Thorngren-Preskill-Fidkowski arXiv:2601.04304 (rotor TPF circuit), Chatterjee-Pace-Shao (Onsager axial
charge), 't Hooft anomaly matching for on-site symmetries, Weyl equidistribution."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 60

import itertools, math, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm, null_space

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max()) if np.size(X) else 0.0
rng = np.random.default_rng(20261022)
SETS = {'3450': [(8, -1), (4, 2)], 'Dirac(2,0)': [(2, 1)], '3452': [(8, -1), (6, 1)]}   # (qV, qA) per flavour

def fermion_ops(n):                     # Jordan-Wigner annihilators on n modes (dense, n <= 8)
    cs = []
    for j in range(n):
        c = np.zeros((2 ** n, 2 ** n))
        for s in range(2 ** n):
            if (s >> j) & 1: c[s ^ (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
        cs.append(c)
    return cs

# ============================== A. finite carriers: turn charge versus angle ==============================
print('== A. a finite carrier cannot hold both an exact integer turn charge and an angle')
okA1 = True; det1 = []
for k in (2, 3, 4):                     # k fermion modes, turn charge N = total mode number (the cluster's exact U(1))
    cs = fermion_ops(k); D = 2 ** k; N = sum(c.T @ c for c in cs)
    M = np.kron(np.eye(D), N) - np.kron(N.T, np.eye(D)) - np.eye(D * D)   # vec([N,X] - X) = 0, column-major
    B = null_space(M); X = (B @ rng.normal(size=B.shape[1])).reshape(D, D, order='F')
    top = np.diag(N) == k; sv = np.linalg.svd(X, compute_uv=False)
    okA1 &= nrm(N @ X - X @ N - X) < 1e-10 and nrm(np.linalg.matrix_power(X, k + 1)) < 1e-8 and nrm(X[:, top]) < 1e-12 and sv[-1] < 1e-10
    det1.append(f'k={k}: dim {B.shape[1]}, X^{k + 1}=0')
check('A1 [T] on k fermion modes every X with [N, X] = X (a raising of the exact cluster number) is nilpotent and kills the full '
      'cluster, so no unitary e^{i phi} exists: an exact integer turn charge comes with no angle and no winding density', okA1, '; '.join(det1))
okA2 = True; det2 = []
for d in (3, 5, 7):
    Nd = np.diag(np.arange(d)); V = np.roll(np.eye(d), 1, axis=0)          # clock shift, the unitary nearest to raising
    F = np.exp(-2j * np.pi * np.outer(np.arange(d), np.arange(d)) / d) / np.sqrt(d)   # columns: Pegg-Barnett angle states
    good = []
    for j in range(7 * d):
        be = j / (7 * d); Tb = np.diag(np.exp(2j * np.pi * be * np.arange(d)))
        cov = nrm(Tb @ V @ Tb.conj().T - np.exp(2j * np.pi * be) * V) < 1e-12
        perm = abs(np.abs(F.conj().T @ Tb @ F).max() - 1) < 1e-12 and np.allclose(np.abs(F.conj().T @ Tb @ F).sum(0), 1)
        okA2 &= (cov == perm); good += [j] if cov else []
    okA2 &= good == [7 * m for m in range(d)]; det2.append(f'd={d}: {len(good)} of {7 * d} turns')
check('A2 [T] with an angle grid (d Pegg-Barnett angles, clock shift V) a turn e^{2 pi i b N} keeps V covariant and maps angle '
      'states to angle states iff b is in Z/d: TPF\'s controlled turns by qV theta_j and its winding phase (read in the angle '
      'basis) survive only on Z_d, as for Z_N clocks', okA2, ', '.join(det2))

# ============================== B. occupation-diagonal lock ==============================
print('== B. carrier: turn = fermion number of a 2-mode cluster per cell, winding = rishon number of a 2-mode cluster per link')
# one flavour on a ring of 2 cells: modes 0,1 turn cluster of cell 0; 2,3 of cell 1; 4,5 link 0-1; 6,7 link 1-0 (8 modes, 256)
cs = fermion_ops(8); n = [c.T @ c for c in cs]
Nt = [n[0] + n[1], n[2] + n[3]]; El = [n[4] + n[5], n[6] + n[7]]; QV = Nt[0] + Nt[1]; QA = El[0] + El[1]
dens = Nt + El
okB1 = all(nrm(a @ b - b @ a) < 1e-14 for a in dens for b in dens) and all(np.allclose(np.diag(a), np.round(np.diag(a))) and nrm(a - np.diag(np.diag(a))) == 0 for a in dens)
endp = {}
for nm, qs in SETS.items():              # flavours are disjoint copies, so commutators factor flavour by flavour
    rho_V, rho_A = Nt[0], El[0]          # restriction to the interval {cell 0, link 0}
    sch = max(nrm((qV * rho_V + qA * rho_A) @ (qV * Nt[1] + qA * El[1]) - (qV * Nt[1] + qA * El[1]) @ (qV * rho_V + qA * rho_A)) for qV, qA in qs)
    cutA = nrm(expm(2j * np.pi * rho_A) - np.eye(256)); endp[nm] = (nrm(QV @ rho_A - rho_A @ QV), sch, cutA)
okB1 &= all(max(v) < 1e-10 for v in endp.values())
check('B1 [T] all densities (cluster numbers, link rishon numbers) are diagonal in one occupation basis: Q_V, Q_A are commuting '
      'exact integers, every combination is on-site (the TPF disentangler is W = 1), the 2 pi axial turn cut to an interval is 1 '
      '(no endpoint charge) and the Schwinger term is 0 for every set: 3450 AND the anomalous Dirac(2,0) and 3452 can all be linked '
      'with an exact Gauss law. The carrier is anomaly-blind, unlike the rotor (tpf-circuit B3, B4, D3)', okB1,
      ', '.join(f'{k}: [Q_V,Q_A^I] {v[0]:.0e}, Schwinger {v[1]:.0e}' for k, v in endp.items()))

def herm(X): return X + X.conj().T
def H_alpha(al, cf):                     # random interacting update generator conserving Q_V and Q_A; V-flux al on the turn bond
    t = [cs[i].T @ cs[j] for i in range(4) for j in range(4) if i // 2 != j // 2]           # turn hops between cells
    ph = [np.exp(1j * al * (1 if (i // 2, j // 2) == (1, 0) else -1)) for i in range(4) for j in range(4) if i // 2 != j // 2]
    w = [cs[i].T @ cs[j] for i in range(4, 8) for j in range(4, 8) if i != j]                # winding moves between links
    H = sum(cf[0][m] * ph[m] * t[m] for m in range(len(t))) + sum(cf[1][m] * w[m] for m in range(len(w)))
    H = H + sum(cf[2][m] * ph[m] * t[m] @ w[(3 * m) % len(w)] for m in range(len(t)))      # four-fermion correlated moves
    H = herm(H) / 2 + sum(cf[3][i] * n[i] for i in range(8)) + sum(cf[4][i] * n[i] @ n[(i + 3) % 8] for i in range(8))
    return H
cf = [rng.normal(size=8) + 1j * rng.normal(size=8), rng.normal(size=12) + 1j * rng.normal(size=12), 0.7 * (rng.normal(size=8) + 1j * rng.normal(size=8)),
      rng.normal(size=8), rng.normal(size=8)]
sec = (np.round(np.diag(QV)).astype(int), np.round(np.diag(QA)).astype(int))
lab = sorted(set(zip(*sec))); okB2 = True; drift = 0.0; ints = 0
U0 = None
for al in np.linspace(0, 2 * np.pi, 9):
    H = H_alpha(al, cf); okB2 &= nrm(H @ QV - QV @ H) < 1e-12 and nrm(H @ QA - QA @ H) < 1e-12
    U = expm(-1j * 0.3 * H_alpha(al, [c[::-1] for c in cf])) @ expm(-1j * 0.3 * H)         # a two-layer interacting update
    okB2 &= nrm(U @ QA - QA @ U) < 1e-12
    if U0 is None: U0 = U
for (v, a) in lab:                       # spectral flow sector by sector: the update at flux 2 pi is the update at 0 up to a gauge
    idx = np.where((sec[0] == v) & (sec[1] == a))[0]
    e0 = np.sort(np.angle(np.linalg.eigvals(U0[np.ix_(idx, idx)]))); e2 = np.sort(np.angle(np.linalg.eigvals(U[np.ix_(idx, idx)])))
    drift = max(drift, float(np.abs(e0 - e2).max()))
okB2 &= drift < 1e-9
check('B2 [T] V-flux insertion on an interacting rishon update (one-body turn and winding hops, density-density and four-fermion '
      'correlated moves; flux on the turn bond): Q_A commutes with the update at every flux, so threading 2 pi pumps exactly 0 '
      'axial charge and each (Q_V, Q_A) sector returns to itself', okB2, f'{len(lab)} sectors, quasi-energy return {drift:.1e}')
L = 10; ks = 2 * np.pi * np.arange(-L // 2, L // 2) / L; occ0 = set(np.where(-2 * np.cos(ks) < 0)[0])
shift = {i: (i + 1) % L for i in range(L)}; occ1 = {shift[i] for i in occ0}                        # 2 pi flux: k -> k + 2 pi / L
vel = 2 * np.sin(ks); chi = lambda S: sum(1 if vel[i] > 0 else -1 for i in S)
pump = chi(occ1) - chi(occ0)
check('B3 [T] contrast, the one-mode Dirac chain (hop -2 cos k, half filled, 10 sites): the same 2 pi V-flux moves one state from the '
      'left to the right Fermi point, N_R - N_L changes by 2 = the mixed anomaly the rotor carries; the rishon carrier gives 0',
      pump == 2 and occ1 != occ0, f'pump {pump:+d} (rishon carrier 0)')

# ============================== C. quasi-energy of a bounded carrier ==============================
print('== C. finite step: kinetic phase eps U L^2 per cell (rotor: L in Z; truncated: |L| <= S)')
dist = lambda x: abs((x + np.pi) % (2 * np.pi) - np.pi)
eU = 2 * np.pi * (math.sqrt(5) - 1) / 2 / 13
rot = min(dist(eU * Lr * Lr) for Lr in range(1, 4001)); trunc = {S: min(dist(eU * Lr * Lr) for Lr in range(1, S + 1)) for S in (1, 2, 3)}
check('C1 [T] one cell: the rotor\'s phases eps U L^2 come within any delta of 0 (Weyl); a truncated carrier with eps U S^2 < pi '
      'has single-cell gap exactly eps U', rot < 2e-3 and all(abs(v - eU) < 1e-12 for v in trunc.values()) and eU * 9 < np.pi,
      f'rotor min (L <= 4000) {rot:.1e}; truncated S=1..3 gap {eU:.3f}')
def kmin(S, m=16, kmax=40):              # fewest excited cells with sum L_i^2 = 0 mod m (eps U = 2 pi / m), 1 <= |L_i| <= S
    reach = {0}
    for k in range(1, kmax + 1):
        reach = {(r + l * l) % m for r in reach for l in range(1, S + 1)}
        if 0 in reach: return k
    return None
km = {S: kmin(S) for S in (1, 2, 3, 4)}
check('C2 [T] many cells (eps U = 2 pi/16): the fewest cells whose kinetic phases fold to 0 is 16, 4, 4 for S = 1, 2, 3 and 1 '
      'for S >= 4 (the rotor): a bounded carrier turns the one-cell resonance into a k-cell one, k >= 2 pi/(eps U S^2), so the '
      'gap is prethermal (order-k processes), not strict; imitating the rotor (large S) needs eps ~ 1/S^2',
      km == {1: 16, 2: 4, 3: 4, 4: 1} and all(km[S] >= math.ceil(16 / S ** 2) for S in km), str(km))

print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('Supplied: cluster sizes, the random update, flux placement, eps U. Cited: TPF 2601.04304, Chatterjee-Pace-Shao, anomaly '
      'matching, Weyl. Dense Fock spaces <= 2^8.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
