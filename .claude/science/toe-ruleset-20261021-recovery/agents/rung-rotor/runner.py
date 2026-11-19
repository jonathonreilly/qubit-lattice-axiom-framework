#!/usr/bin/env python3
"""rung-rotor: can the rung column above a site (a semi-infinite fermion chain with a filled sea) be the TPF rotor?
 A one column: the Hilbert-hotel shift is a depth-2 fermionic-swap circuit (product sea) or its quasi-local dressing (gapped
   hopping sea); Shale-Stinespring implementable, index 1, the whole charge distribution moves by one unit (exact U(1) turn)
 B the register's ladder: neighbouring columns share every cell above their merging rung (difference charge bounded); a range-r
   update moves at most O(r 2^-dJ) charge per fine site across rung J (no positive density of hotels); CL-1's lapse truncates
   the column at rung log2 T after T ticks
 C anomaly: with SUPPLIED full-density columns (a half-plane) and a Chern bulk, 2 pi flux pumps one charge into the bottom edge
   and one out at the far end (inflow); two opposite layers pump N_R - N_L = 2, the Dirac-chain value of rotor-rishon B3
Labels: [T] theorem / exact computation. Supplied model, finite diagnostic; no physical identification.
Cited, not rederived: Shale-Stinespring implementability, Carey-Ruijsenaars charge sectors, Avron-Seiler-Simon index of pairs,
Qi-Wu-Zhang model, Callan-Harvey inflow, Kaplan domain-wall fermions, TPF arXiv:2601.04304."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 90

import math, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm, sqrtm, eigh
from scipy.optimize import linear_sum_assignment

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max()) if np.size(X) else 0.0
rng = np.random.default_rng(20261022)

def conveyor(L):                         # one-body u0: e_2k -> e_2k+2, e_1 -> e_0, e_2k+3 -> e_2k+1 (layer B after layer A)
    def layer(pairs):
        U = np.eye(L)
        for i, j in pairs: U[[i, j]] = U[[j, i]]
        return U
    A = layer([(i, i + 1) for i in range(0, L - 1, 2)]); B = layer([(i, i + 1) for i in range(1, L - 1, 2)])
    return B @ A
def fermion_ops(n):
    cs = []
    for j in range(n):
        c = np.zeros((2 ** n, 2 ** n))
        for s in range(2 ** n):
            if (s >> j) & 1: c[s ^ (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
        cs.append(c)
    return cs

# ======================================= A. one column =======================================
print('== A. one column: modes j = 0,1,2,... (rung j), sea = even rungs filled (staggered column mass)')
okA1 = True; det = []
for L in (8, 16, 64, 256):
    u = conveyor(L); P0 = np.diag((np.arange(L) % 2 == 0).astype(float)); D = P0 - u @ P0 @ u.T
    Rw = L // 2; bot = np.trace(D[:Rw, :Rw]); top = np.trace(D[Rw:, Rw:])
    cm = u @ P0 - P0 @ u; hs = np.sum(cm[:Rw, :] ** 2)
    okA1 &= abs(bot - 1) < 1e-14 and abs(top + 1) < 1e-14 and abs(hs - 1) < 1e-14 and nrm(u @ u.T - np.eye(L)) == 0
    det.append(f'L={L}: bottom {bot:+.0f}, far end {top:+.0f}')
n = 8; cs = fermion_ops(n); G = np.eye(2 ** n)
for k in (0, 1):                         # second quantisation: f-swap gates exp(-i pi/2 (c_i^+ c_j + h.c. - n_i - n_j)), A then B
    for i in range(k, n - 1, 2):
        h = cs[i].T @ cs[i + 1]; G = expm(-0.5j * np.pi * (h + h.T - cs[i].T @ cs[i] - cs[i + 1].T @ cs[i + 1])) @ G
u = conveyor(n); cov = max(nrm(G @ cs[j].T @ G.conj().T - sum(u[i, j] * cs[i].T for i in range(n))) for j in range(n))
sea = np.zeros(2 ** n); sea[sum(1 << j for j in range(0, n, 2))] = 1
Qw = lambda R: sum(cs[j].T @ cs[j] for j in range(R))
mb = [(float(sea @ Qw(R) @ sea), float(np.real((G @ sea).conj() @ Qw(R) @ (G @ sea))), float(np.real((G.conj().T @ sea).conj() @ Qw(R) @ (G.conj().T @ sea)))) for R in (2, 4, 6)]
okA1 &= cov < 1e-12 and all(abs(b - a + 1) < 1e-12 and abs(c - a - 1) < 1e-12 for a, b, c in mb)
check('A1 [T] the Hilbert-hotel shift is a depth-2 f-swap circuit on the column (the translation of the column folded at its '
      'bottom); P - uPu^dag = |e0><e0| exactly (the far-end defect sits at the truncation), ||[u,P]||_HS = 1: implementable, '
      'index 1; dense Fock (8 modes): G c_j^+ G^dag = sum u_ij c_i^+, G lowers / G^dag raises every bottom window by exactly 1',
      okA1, '; '.join(det) + f'; covariance {cov:.0e}')

def dressed(L, m, t):                    # gapped hopping sea P_t, Kato-type V with P_t = V P0 V^dag, u_t = V u0 V^dag
    H = np.diag(-m * (-1.0) ** np.arange(L)) - t * (np.eye(L, k=1) + np.eye(L, k=-1))
    w, v = eigh(H); Pt = v[:, w < 0] @ v[:, w < 0].T
    P0 = np.diag((np.arange(L) % 2 == 0).astype(float)); X = Pt @ P0 + (np.eye(L) - Pt) @ (np.eye(L) - P0)
    V = X @ np.real(np.linalg.inv(sqrtm(X.T @ X))); return Pt, V @ conveyor(L) @ V.T, V
okA2 = True; det = []
for t in (0.3, 0.6):
    errs = []
    for L in (40, 80, 160):
        Pt, ut, V = dressed(L, 1.0, t); R = L // 2; Dt = Pt - ut @ Pt @ ut.T
        ind = np.trace(Dt[:R, :R]); far = np.trace(Dt[R:, R:]); errs.append(abs(ind - 1))
        P0_ = np.diag((np.arange(L) % 2 == 0).astype(float)); okA2 &= nrm(V @ P0_ @ V.T - Pt) < 1e-10
        okA2 &= nrm(ut @ ut.T - np.eye(L)) < 1e-10 and abs(far + 1) < 1e-8
        dist = np.abs(np.subtract.outer(np.arange(L), np.arange(L))); tail = float(np.abs(ut[dist > 24]).max())
        bulk = nrm((ut @ Pt - Pt @ ut)[8:L - 8, 8:L - 8])
    okA2 &= max(errs) < 1e-9 and tail < 1e-6 and bulk < 1e-6
    det.append(f't/m={t}: |index-1| {max(errs):.0e}, tail {tail:.0e}, bulk [u,P] {bulk:.0e}')
check('A2 [T] gapped hopping column sea: the dressed shift u_t = V u0 V^dag is unitary, quasi-local (matrix elements beyond 24 '
      'rungs < 1e-6), commutes with the sea away from both ends, and its bottom index is 1 for every truncation (far end -1)',
      okA2, '; '.join(det))
L = 80; Pt, ut, _ = dressed(L, 1.0, 0.6); R = 40; C0 = Pt[:R, :R]; C1 = (ut.T @ Pt @ ut)[:R, :R]   # state G^dag|sea>
gen = lambda C, a: np.linalg.det(np.eye(R) + (np.exp(1j * a) - 1) * C)
alist = [0.7, 1.9, math.pi - 0.1, 2 * math.pi * (math.sqrt(5) - 1) / 2]
rat = [gen(C1, a) / gen(C0, a) / np.exp(1j * a) for a in alist]
check('A3 [T] the full bottom-window charge distribution of G^dag|sea> is that of the sea moved by one unit: '
      '<e^{i a Q_R}> ratio = e^{i a} for every angle a (not only Z_d, cf. rotor-rishon A2), so (Q_rel, G) is an exact rotor pair: '
      'integer turn charge unbounded both ways, unitary raising, compact angle. G has index 1, so it is fermion-odd; a bosonic '
      'rotor is the even sector with L = Q_rel/2 and raising G^2', max(abs(r - 1) for r in rat) < 1e-9,
      f'max |ratio - 1| {max(abs(r - 1) for r in rat):.0e} at a = {", ".join(f"{a:.2f}" for a in alist)}')

# ======================================= B. the register's ladder =======================================
print('== B. ladder: rung-j cells hold one mode per 2^(dj) fine sites; the column of x = cells containing x')
okB1 = True; det = []
for D in (8, 12, 16):
    N = 2 ** D; xs = np.arange(N - 1)
    merge = np.array([next(j for j in range(D + 1) if (x >> j) == ((x + 1) >> j)) for x in xs])
    priv = 2 * merge                         # private cells of x and x+1: rungs 0..merge-1, one each
    v2 = np.array([(int(x + 1) & -int(x + 1)).bit_length() - 1 for x in xs])
    okB1 &= np.array_equal(merge, v2 + 1) and abs(np.mean(merge) - 2) < 0.05 and priv.max() == 2 * D
    frac = [float(np.mean(merge >= k)) for k in (2, 4, 6)]
    okB1 &= all(abs(f - 2.0 ** (1 - k)) < 1e-3 + 2.0 ** (-D + 2) for f, k in zip(frac, (2, 4, 6)))
    det.append(f'D={D}: width(L_x) {D + 1}, width(L_x - L_x+1) mean {np.mean(priv):.2f} max {priv.max()} (one seam pair)')
check('B1 [T] neighbouring columns share every cell above their merging rung v2(x+1)+1, so L_x - L_{x+1} lives on 2(v2+1) private '
      'cells: bounded, fraction 2^(1-k) of pairs reach k; a unitary R with R D R^dag = D - 2 needs D unbounded (spec D = spec D - 2), '
      'so no exact inter-column hop e^{i(phi_x+1 - phi_x)} exists at any pair at finite depth', okB1, '; '.join(det))

def ladder(N, J):                        # 1D dyadic ladder: vertices (j, i), lateral and vertical edges
    idx = {}; vs = []
    for j in range(J + 1):
        for i in range(N >> j): idx[(j, i)] = len(vs); vs.append((j, i))
    E = [(idx[(j, i)], idx[(j, i + 1)]) for (j, i) in vs if (j, i + 1) in idx] + [(idx[(j, i)], idx[(j + 1, i >> 1)]) for (j, i) in vs if j < J]
    return vs, E
N, Jm, r = 128, 6, 2; vs, E = ladder(N, Jm); nv = len(vs); rung = np.array([v[0] for v in vs])
adj = [[] for _ in range(nv)]
for a, b in E: adj[a].append(b); adj[b].append(a)
okB2 = True; worst = {}
for J in range(0, Jm):
    A = rung <= J; cut = [(a, b) for a, b in E if A[a] != A[b]]
    dist = np.full(nv, 99); fr = [x for e in cut for x in e]; dist[fr] = 0; q = list(fr)
    while q:
        x = q.pop(0)
        for y in adj[x]:
            if dist[y] > dist[x] + 1: dist[y] = dist[x] + 1; q.append(y)
    collar = int(np.sum(dist <= r - 1)); worst[J] = 0.0
    for trial in range(12):
        U = np.eye(nv, dtype=complex)
        for layer in range(r):
            used = set(); perm = rng.permutation(len(E))
            for e in perm:
                a, b = E[e]
                if a in used or b in used: continue
                used |= {a, b}; g = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0]
                Ug = np.eye(nv, dtype=complex); Ug[np.ix_([a, b], [a, b])] = g; U = Ug @ U
        P = np.diag(rng.integers(0, 2, nv).astype(float)); dq = abs(np.trace((U @ P @ U.conj().T - P)[np.ix_(A, A)]).real)
        okB2 &= dq <= collar + 1e-9; worst[J] = max(worst[J], dq / N)
    sat = sum(1 for (j, i) in vs if j == J + 1)  # swap every vertical cut edge with sea below / empty above: flux = cells at J+1
    okB2 &= sat <= collar and abs(sat / N - 2.0 ** -(J + 1)) < 1e-12
check('B2 [T] cut theorem: for a range-r one-body update, |tr Pi_A(uPu^dag - P)| <= #modes within r of the cut; across rung J this '
      'is O(r 2^(-dJ)) per fine site (saturated by vertical swaps, 2^-(J+1) in d = 1): a density rho of hotels whose defects leave '
      'every finite rung needs rho <= C r 2^(-dJ) for all J, so rho = 0. Total ladder storage per fine site sum_j 2^(-dj): 1 (d=1), '
      '1/7 (d=3)', okB2, 'max random flux per fine site by J: ' + ', '.join(f'{J}:{w:.3f}' for J, w in worst.items()))

okB3 = True; det = []
for Lc in (8, 12, 16, 24):
    u = conveyor(Lc); occ = (np.arange(Lc) % 2 == 0).astype(int); sea0 = occ.copy(); Kmax = None
    for k in range(1, Lc + 1):
        occ = (u.T @ occ).round().astype(int)        # G^dag: raise; occupation of e_i after = occupation of u e_i before
        Wn = Lc // 2; q = int(occ[:Wn].sum() - sea0[:Wn].sum())
        if q != k and Kmax is None: Kmax = k - 1
    okB3 &= Kmax == Lc // 4
    det.append(f'{Lc} rungs: {Kmax} exact raises')
Tage = 2 ** 203
check('B3 [T] CL-1 lapse: rung j ticks once per 2^j fine ticks, so after T ticks only rungs <= log2 T have acted and the column is '
      'a finite carrier: charge K fills 2K rungs and the far-end hole walks down 2 rungs per raise, so a bottom window is raised exactly only '
      '(rungs)/4 times: |L| <= (1/4) log2 T (about 50 for 2^203 ~ 1e61 ticks); an exact raise is never completed in finite time',
      okB3, '; '.join(det) + f'; T = 2^203 -> {int(math.log2(Tage)) // 4} units')

# ======================================= C. anomaly with supplied full-density columns =======================================
print('== C. supplied half-plane: fine ring (Nx) x M rungs, two modes per cell, Qi-Wu-Zhang update in the (fine, rung) plane')
def strip(kx, M, mu, s):
    T = np.eye(M, k=-1); sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.])
    return np.kron(np.eye(M), s * math.sin(kx) * sx + (mu + math.cos(kx)) * sz) + np.kron((T - T.T) / 2j, sy) + np.kron((T + T.T) / 2, sz)
def pump(Nx, M, mu, s, steps=120):
    Pb = np.kron(np.diag((np.arange(M) < M // 2).astype(float)), np.eye(2)); db = 0.0; dt = 0.0; tot = 0.0
    for kx in 2 * np.pi * np.arange(Nx) / Nx:
        w, v = eigh(strip(kx, M, mu, s)); track = v[:, w < 0]
        b0 = np.real(np.einsum('in,ij,jn->', track.conj(), Pb, track))
        for st in range(1, steps + 1):
            w, v = eigh(strip(kx + 2 * np.pi / Nx * st / steps, M, mu, s)); ov = np.abs(track.conj().T @ v)
            _, col = linear_sum_assignment(-ov); ph = np.diag(v[:, col].conj().T @ track); track = v[:, col] * (ph / np.abs(ph))
        b1 = np.real(np.einsum('in,ij,jn->', track.conj(), Pb, track)); db += b1 - b0
    return db
Nx, M = 10, 14
d1 = pump(Nx, M, -1.0, +1); d2 = pump(Nx, M, -1.0, -1)
check('C1 [T] a 2 pi flux through the fine ring pumps exactly one charge into the bottom (fine) edge and one out at the far end: '
      'the chiral edge is anomalous and the columns absorb the inflow (Callan-Harvey; the defect is the Hilbert-hotel one); the '
      'opposite layer pumps -1, so N_R - N_L at the fine edge changes by 2, the one-mode Dirac-chain value (rotor-rishon B3: rishon '
      'carrier 0). Needs one cell per fine site at every rung, a 2D lattice, not the register ladder (B2)',
      abs(abs(d1) - 1) < 1e-3 and abs(d1 + d2) < 1e-3, f'layer +: {d1:+.4f}, layer -: {d2:+.4f}, N_R - N_L {d1 - d2:+.4f}')

print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('Supplied: the staggered column sea, t/m, the f-swap order, random ladder circuits, the half-plane and QWZ mass -1. '
      'Dense Fock <= 2^8; Gaussian otherwise.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
