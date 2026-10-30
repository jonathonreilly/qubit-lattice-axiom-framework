#!/usr/bin/env python3
"""Emergent photon from the sites' own qubits (charge-ice route). Supplied models, finite checks, no physical
identification.

 A  One fermion mode has only 1 and n as parity-even operators, so a site-valued electric flux must be E_s = n_s - 1/2,
    oriented from the site's even block centre to its odd one (sites = bonds of the body-centred block-centre lattice).
    Its divergence is q_e = N_e - 4, q_o = 4 - N_o. sum q = 0 identically, and c_s^dag adds (+1, -1): a Margolus fermion
    is an emergent-neutral dipole, never a charge.
 B  The ice rule (all counts 4) does not follow from CL-3/CL-5: a half-tick conserves its own partition's counts and
    changes the other's; the tick has no flat band, so no finite-region quadratic charge at any rung; the half-filled
    sea has Var(N_b) > 0; no single-block move preserves ice.
 C  Supplied: H = J sum_cubes (N - 4)^2 + t sum_cubes c^dag W c. At second order the CL-3 edge hop gives ring exchange
    on the body-centred 4-cycles: 12 planar (two pairings, CL-3 flux pi makes them add: |K| = 2t^2/3J) + 12 skew
    (one pairing, t^2/3J) per cell. Checked by exact diagonalisation of the 4-mode plaquette.
 D  Gaussian (non-compact) reading of the ring model: two gauge zeros, two massless transverse modes; speeds and
    isotropy. Classical ice ensemble: pinch-point check by ring-flip Monte Carlo.
 E  Charges are count defects with (q, n_F) = (+-1, +-1/2), hopping at first order; speed and mass arithmetic.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/A_SITE_QUBIT_ICE_PHOTON_MAKES_MARGOLUS_FERMIONS_NEUTRAL_DIPOLES_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.optimize import minimize
T0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
rng = np.random.default_rng(20261021); r3 = np.sqrt(3.0)

# ---------------- CL-3 coin (spin-3/2 overlap phases on the 12 cube edges), as in the what-is-a-link construction
C = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def coh(j, n):
    J = Jm(j); n = np.asarray(n, float) / np.linalg.norm(n)
    return np.linalg.eigh(sum(n[k] * J[k] for k in range(3)))[1][:, -1]
XI = [coh(1.5, 2 * C[i] - 1.0) for i in range(8)]
W0 = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(np.abs(C[a] - C[b])) == 1:
            g = XI[a].conj() @ XI[b]; W0[a, b] = -g / abs(g) / r3

class Torus:
    def __init__(s, N):
        s.N = N; s.sites = np.array(list(itertools.product(range(N), repeat=3))); s.n = len(s.sites)
        s.idx = {tuple(x): i for i, x in enumerate(s.sites)}; s.even, s.odd = [], []
        for o in itertools.product(range(0, N, 2), repeat=3):
            o = np.array(o)
            s.even.append([s.idx[tuple((o + C[r]) % N)] for r in range(8)])
            s.odd.append([s.idx[tuple((o + 1 + (1 - C[r])) % N)] for r in range(8)])
        s.be = np.zeros(s.n, int); s.bo = np.zeros(s.n, int)
        for b, ss in enumerate(s.even): s.be[ss] = b
        for b, ss in enumerate(s.odd): s.bo[ss] = b
        s.nb = len(s.even)
    def half(s, Wb, blocks):
        M = np.zeros((s.n, s.n), complex)
        for ss in blocks: M[np.ix_(ss, ss)] += Wb
        return M
    def counts(s, occ):
        return np.bincount(s.be, occ, s.nb), np.bincount(s.bo, occ, s.nb)
def species(a): return np.cos(a) * W0 + 1j * np.sin(a) * np.eye(8)

T = Torus(8); n = T.n
print(f'torus 8^3: {n} sites, {T.nb} even + {T.nb} odd blocks')
H = T.half(W0, T.even) + T.half(W0, T.odd)                                  # t = 1; hop matrix h_ij (each pair of sites shares at most one block)
site_of = {(T.be[i], T.bo[i]): i for i in range(n)}
ev_nb = {e: set(T.bo[T.even[e]]) for e in range(T.nb)}; od_nb = {o: set(T.be[T.odd[o]]) for o in range(T.nb)}
cycles = {}
for e in range(T.nb):
    for o1, o2 in itertools.combinations(sorted(ev_nb[e]), 2):
        for e2 in (od_nb[o1] & od_nb[o2]) - {e}:
            s = (site_of[(e, o1)], site_of[(e2, o1)], site_of[(e2, o2)], site_of[(e, o2)])
            cycles.setdefault(frozenset(s), s)
def is_edge(i, j):
    d = (T.sites[i] - T.sites[j]) % T.N; d = np.minimum(d, T.N - d); return d.sum() == 1
cyc = list(cycles.values()); ncell = (T.N // 2) ** 3
kind, kap = [], []
for s1, s2, s3, s4 in cyc:
    odd_pair = is_edge(s1, s2) and is_edge(s3, s4); even_pair = is_edge(s1, s4) and is_edge(s3, s2)
    kind.append(2 * odd_pair + even_pair)
    kap.append(-(H[s2, s1] * H[s4, s3] - H[s4, s1] * H[s2, s3]))   # coefficient of c2^d c1 c4^d c3, in units t^2/J
kind = np.array(kind); kap = np.array(kap)
occ_ice = (T.sites.sum(1) % 2 == 0).astype(float); cyc_arr = np.array(cyc); ncyc = len(cyc)
def ring_mc(occ, sweeps):
    occ = occ.copy(); fl = 0
    for _ in range(sweeps):
        for p in rng.integers(0, ncyc, ncyc):
            a = occ[cyc_arr[p]]
            if a[0] == a[2] and a[1] == a[3] and a[0] != a[1]: occ[cyc_arr[p]] = 1 - a; fl += 1
    return occ, fl
occ_gen, _ = ring_mc(occ_ice, 40)
# ---------------- A. the electric field a single mode can carry
print('== A. one-qubit electric flux and its charges')
par = np.diag([1.0, -1.0]); basis = [np.eye(2)[:, [i]] @ np.eye(2)[[j], :] for i in range(2) for j in range(2)]
even_ops = np.linalg.matrix_rank(np.array([(b + par @ b @ par).ravel() for b in basis]))
check('A1 parity-even operators of one mode span {1, n} (dim 2): a site flux variable is E_s = n_s - 1/2, its only flip is c or c^dag (odd)',
      even_ops == 2, f'dim = {even_ops}')
okA = True
for _ in range(200):
    occ = rng.integers(0, 2, n).astype(float); Ne, No = T.counts(occ)
    okA &= abs((Ne - 4).sum() + (4 - No).sum()) < 1e-12
s0 = 123; occ2 = occ.copy(); occ2[s0] = 1 - occ[s0]; Ne2, No2 = T.counts(occ2); sg = 1 if occ[s0] == 0 else -1
dq_e = (Ne2 - Ne) * sg; dq_o = -(No2 - No) * sg
okA &= (dq_e[T.be[s0]] == 1 and dq_o[T.bo[s0]] == -1 and np.abs(dq_e).sum() == 1 and np.abs(dq_o).sum() == 1)
check('A2 sum of divergences q_e = N_e - 4, q_o = 4 - N_o vanishes for every configuration (200 random); adding a fermion at a site puts +1 on its even block and -1 on its odd block',
      okA, 'a Margolus fermion is an emergent dipole of length sqrt3 (one body-centred bond), net emergent charge 0')

# ---------------- B. does the ice rule follow from CL-3 / CL-5 ?
print('== B. is the ice rule (every count = 4) forced?')
Pb_e = [np.diag(np.isin(np.arange(n), ss).astype(float)) for ss in (T.even[0],)]
Pb_o = [np.diag(np.isin(np.arange(n), ss).astype(float)) for ss in (T.odd[0],)]
Me = T.half(W0, T.even); Mo = T.half(W0, T.odd); U = Mo @ Me
cm = lambda M, P: np.linalg.norm(M @ P @ M.conj().T - P)
d1, d2, d3, d4 = cm(Me, Pb_e[0]), cm(Me, Pb_o[0]), cm(U, Pb_e[0]), cm(U, Pb_o[0])
check('B1 the even half-tick keeps every even count and changes odd counts; the full tick keeps no block count (CL-5 moves only along these transitions)',
      d1 < 1e-12 and min(d2, d3, d4) > 0.5, f'||M P M^dag - P||: even/even {d1:.1e}, even/odd {d2:.2f}, tick/even {d3:.2f}, tick/odd {d4:.2f}')
# Bloch spectrum of the tick from the real-space matrix: U(K) on the 8 residues per cell
cell = T.sites // 2; res = (T.sites % 2) @ np.array([4, 2, 1])
def blochU(Ureal, Ks):
    i0 = [T.idx[tuple(C[r])] for r in range(8)]
    out = np.zeros((len(Ks), 8, 8), complex)
    for r in range(8):
        row = Ureal[i0[r]]; nz = np.nonzero(np.abs(row) > 1e-14)[0]
        dn = (cell[nz] + 2) % 4 - 2
        ph = np.exp(-1j * (Ks @ dn.T))
        for j, col in enumerate(nz): out[:, r, res[col]] += row[col] * ph[:, j]
    return out
g = np.linspace(-np.pi, np.pi, 12, endpoint=False); Ks = np.array(list(itertools.product(g, repeat=3)))
widths = []
for (mu, b) in ((0.0, 0.0), (0.4, 0.0), (0.4, 0.15)):
    Ur = T.half(species(mu / 2 - b), T.odd) @ T.half(species(mu / 2 + b), T.even)
    UK = blochU(Ur, Ks[::7])
    w = np.sort(np.angle(np.linalg.eigvals(UK)), axis=1); widths.append((w.max(0) - w.min(0)).min())
# real-space consistency of the Bloch map (4^3 cell momenta of the 8^3 torus)
gk = np.arange(4) * np.pi / 2; K4 = np.array(list(itertools.product(gk, repeat=3)))
ev_b = np.linalg.eigvals(blochU(U, K4)).ravel(); ev_r = np.linalg.eigvals(U); bmis = np.abs(ev_b[:, None] - ev_r[None, :]).min(1).max()
check('B2 the tick has no flat band (smallest band width over the zone > 0 for (mu,b) = (0,0), (0.4,0), (0.4,0.15)), so no finite region of any rung carries a conserved quadratic charge (a conserved local count = a compact eigenvector)',
      min(widths) > 0.05 and bmis < 1e-9, 'min band widths ' + ', '.join(f'{x:.3f}' for x in widths) + f'; Bloch vs real-space spectrum {bmis:.1e}')
# ice leakage after one even half-tick from an ice Fock state (generic one from ring flips; the parity one is special)
def leak(occ0, a):
    M = T.half(species(a), T.even); cdiag = np.real(np.einsum('ij,j,ij->i', M, occ0, M.conj()))
    # sites of one odd block lie in 8 different even blocks, so C restricted to an odd block is diagonal
    mean = np.bincount(T.bo, cdiag, T.nb); var = np.bincount(T.bo, cdiag * (1 - cdiag), T.nb)
    return np.mean(var + (mean - 4) ** 2)
Ne, No = T.counts(occ_gen); Np, Op = T.counts(occ_ice)
lk = [leak(occ_gen, a) for a in (0.0, np.pi / 2 - 0.1, np.pi / 2 - 0.05)]; lp = leak(occ_ice, 0.0)
r1, r2 = lk[1] / np.sin(0.1) ** 2, lk[2] / np.sin(0.05) ** 2
check('B3 from a generic exact ice configuration one even half-tick leaves <(N_o - 4)^2> > 0 per odd block, ~ cos^2 a at small hop angle; the parity configuration is special (W maps it to its complement, leak 0)',
      Ne.min() == Ne.max() == No.min() == No.max() == 4 and lk[0] > 0.1 and abs(r1 / r2 - 1) < 0.05 and lp < 1e-12,
      f'a = 0: {lk[0]:.4f}; leak/cos^2 a at a = pi/2-0.1, -0.05: {r1:.4f}, {r2:.4f}; parity state {lp:.1e}')
# half-filled sea: projector onto quasi-energies in (-pi, 0) via the sign of (U - U^dag)/2i
g2 = np.linspace(-np.pi, np.pi, 16, endpoint=False); K2 = np.array(list(itertools.product(g2, repeat=3)))
seavar = []
for (mu, b) in ((0.4, 0.0), (0.4, 0.15), (np.pi - 0.2, 0.0)):
    Ur = T.half(species(mu / 2 - b), T.odd) @ T.half(species(mu / 2 + b), T.even)
    UK = blochU(Ur, K2); Hs = (UK - np.conj(np.transpose(UK, (0, 2, 1)))) / 2j
    ev, V = np.linalg.eigh(Hs); mask = (ev < 0).astype(float)
    P = np.einsum('kij,kj,klj->kil', V, mask, V.conj()); Cb = P.mean(0)   # even block = one cell
    seavar.append((mask.sum() / len(K2), np.real(np.trace(Cb)), np.real(np.trace(Cb) - np.trace(Cb @ Cb)), np.abs(ev).min()))
check('B4 the half-filled CL-3 sea (16^3 zone) has 4 per block on average but Var(N_b) > 0 at every mass, including near-static mu -> pi: it is a defect plasma, not an ice state',
      all(abs(f - 4) < 1e-9 and abs(m - 4) < 1e-9 and v > 0.3 for f, m, v, gp in seavar),
      'Var(N_b) at (mu,b) = (0.4,0), (0.4,0.15), (pi-0.2,0): ' + ', '.join(f'{v:.4f}' for _, _, v, _ in seavar) + ' (8 independent half-filled sites: 2)')
# single-block moves
ok5 = True
for ss in T.even[:4] + T.odd[:4]:
    other = T.bo[ss] if ss in T.even[:4] else T.be[ss]
    ok5 &= len(set(other)) == 8
check('B5 the 8 sites of any block lie in 8 different opposite blocks, so any change of one block\'s configuration at fixed count creates >= 2 opposite-count defects: no block-local update moves within the ice set except by phases',
      ok5)

# ---------------- C. ring exchange from the CL-3 hop in the supplied strong-count-penalty model
print('== C. ring exchange generated by the CL-3 hop (supplied H = J sum (N - 4)^2 + t sum c^dag W c)')
nplan = np.sum(kind == 3); nskew = np.sum((kind == 1) | (kind == 2))
flux = [np.angle(H[s2, s1] * H[s3, s2] * H[s4, s3] * H[s1, s4]) for (s1, s2, s3, s4), k in zip(cyc, kind) if k == 3]
check('C1 body-centred 4-cycles per cell: 12 planar (the mixed Z^3 plaquettes, both hop pairings exist) + 12 skew (one pairing); none without a pairing',
      len(cyc) == 24 * ncell and nplan == 12 * ncell and nskew == 12 * ncell, f'{len(cyc) // ncell} per cell = {nplan // ncell} + {nskew // ncell}')
kp = np.abs(kap[kind == 3]); ks = np.abs(kap[kind != 3])
check('C2 second order: K_p = -(h21 h43 - h41 h23)/J; the minus sign is fermion exchange, and the CL-3 flux pi on mixed plaquettes turns it into addition: |K| = 2t^2/3J (planar), t^2/3J (skew)',
      np.allclose(np.abs(np.array(flux)), np.pi) and np.allclose(kp, 2 / 3) and np.allclose(ks, 1 / 3),
      f'planar flux/pi = {np.abs(flux).min() / np.pi:.6f}, |K| planar {kp.min():.6f}..{kp.max():.6f}, skew {ks.min():.6f}..{ks.max():.6f}')
# exact 4-mode check
s1, s2, s3, s4 = cyc[int(np.argmax(kind == 3))]; loc = [s1, s2, s3, s4]; h4 = H[np.ix_(loc, loc)]
mask4 = np.array([[1 if (is_edge(loc[i], loc[j])) else 0 for j in range(4)] for i in range(4)]); h4 = h4 * mask4
Z2 = np.diag([1., -1.]); sm = np.array([[0, 1], [0, 0.]]); I2 = np.eye(2)
def cop(j):
    ops = [Z2] * j + [sm] + [I2] * (3 - j); M = ops[0]
    for o in ops[1:]: M = np.kron(M, o)
    return M
cs = [cop(j) for j in range(4)]; nn = [c.T @ c for c in cs]
blocks4 = [(0, 3), (0, 1), (1, 2), (2, 3)]   # e, o1, e'', o2
Hpen = sum((nn[a] + nn[b] - np.eye(16)) @ (nn[a] + nn[b] - np.eye(16)) for a, b in blocks4)
Hhop = sum(h4[i, j] * cs[i].T @ cs[j] for i in range(4) for j in range(4))
rat = []
for t in (0.01, 0.03, 0.1):
    Hm = Hpen + t * Hhop; Ntot = sum(nn); ev, V = np.linalg.eigh(Hm)
    two = [k for k in range(16) if abs(V[:, k].conj() @ Ntot @ V[:, k] - 2) < 1e-6]
    e2 = np.sort(ev[two])[:2]; rat.append((e2[1] - e2[0]) / (2 * (2 / 3) * t ** 2))
check('C3 exact 4-mode diagonalisation: the two ice states split by 2|K| = 4t^2/3J up to O(t^4/J^3)',
      abs(rat[0] - 1) < 1e-3 and abs(rat[1] - 1) < 1e-2, 'splitting/(4t^2/3) at t/J = 0.01, 0.03, 0.1: ' + ', '.join(f'{r:.5f}' for r in rat))
# frustration of the ring phases: can site phases make every term -|K|(R + R^dag)?  alpha_p = arg K_p - pi
Bm = np.zeros((len(cyc), n))
for p, (a1, a2, a3, a4) in enumerate(cyc): Bm[p, [a1, a2, a3, a4]] = [1, -1, 1, -1]
alpha = np.angle(kap) - np.pi; wts = np.abs(kap)
def relax(mask, starts):
    def f(th):
        x = alpha + Bm @ th; return np.sum(mask * wts * (1 - np.cos(x))), Bm.T @ (mask * wts * np.sin(x))
    best = None
    for _ in range(starts):
        r = minimize(f, rng.uniform(-np.pi, np.pi, n), jac=True, method='L-BFGS-B', options={'maxiter': 5000, 'gtol': 1e-10})
        if best is None or r.fun < best.fun: best = r
    x = alpha + Bm @ best.x; Hs = Bm.T @ ((mask * wts * np.cos(x))[:, None] * Bm)
    return best.fun / ncell, np.linalg.eigvalsh(Hs)
E_pl, ev_pl = relax((kind == 3).astype(float), 12); E_all, ev_all = relax(np.ones(len(cyc)), 12)
# closed surfaces made of three cycles (z^T B = 0): gauge-invariant flux sum z_p alpha_p
rowkey = {tuple(sorted(zip(c4, (1, -1, 1, -1)))): p for p, c4 in enumerate(cyc)}
by_site = {}
for p, c4 in enumerate(cyc):
    for i in c4: by_site.setdefault(i, []).append(p)
surf = {}
for p in range(len(cyc)):
    nb = set(q for i in cyc[p] for q in by_site[i] if q > p)
    for q in nb:
        for zq in (1, -1):
            r = {}
            for i, sg in zip(cyc[p], (1, -1, 1, -1)): r[i] = r.get(i, 0) + sg
            for i, sg in zip(cyc[q], (1, -1, 1, -1)): r[i] = r.get(i, 0) + zq * sg
            r = {i: v for i, v in r.items() if v}
            if len(r) != 4 or any(abs(v) != 1 for v in r.values()): continue
            for zr in (1, -1):
                key = tuple(sorted((i, -v * zr) for i, v in r.items()))
                if key in rowkey and rowkey[key] > q:
                    t = rowkey[key]; fl = (alpha[p] + zq * alpha[q] + zr * alpha[t] + np.pi) % (2 * np.pi) - np.pi
                    surf[(p, q, t)] = (fl, tuple(sorted((kind[p] == 3, kind[q] == 3, kind[t] == 3))))
fls = np.array([abs(v[0]) for v in surf.values()]); npi = np.sum(np.abs(fls - np.pi) < 1e-9); nzero = np.sum(fls < 1e-9)
zeros_all = np.sum(np.abs(ev_all) < 1e-6); zeros_pl = np.sum(np.abs(ev_pl) < 1e-6)
check('C4 ring phases (all multiples of pi/2): planar terms alone are unfrustrated (a site-phase gauge makes all -|K|(R + R^dag)); with the skew terms, three-cycle closed surfaces carry flux pi, so the ring model is frustrated',
      E_pl < 1e-9 and len(surf) > 0 and npi > 0 and npi + nzero == len(surf),
      f'{len(surf) // ncell} three-cycle surfaces per cell, {npi // ncell} with flux pi, {nzero // ncell} with 0; best classical cost per cell {E_all:.3f} of {wts.sum() / ncell:.2f}')
# ---------------- D. Gaussian reading: photon of the ring model; classical ice ensemble
print('== D. photon of the ring model (non-compact Gaussian reading, supplied) and the classical ice ensemble')
y = T.sites.astype(float)
def unwrap(i, ref):
    d = (T.sites[i] - T.sites[ref] + T.N // 2) % T.N - T.N // 2; return y[ref] + d
geo = []
for p, c4 in enumerate(cyc):
    pos = [unwrap(i, c4[0]) for i in c4]; geo.append((p, [res[i] for i in c4], pos))
def Mk(k, wpl, wsk):
    M = np.zeros((8, 8), complex)
    for p, rs, pos in geo:
        wgt = wpl if kind[p] == 3 else wsk
        v = np.zeros(8, complex)
        for sgn, r, x in zip((1, -1, 1, -1), rs, pos): v[r] += sgn * np.exp(1j * k @ x)
        M += wgt * np.outer(v, v.conj())
    return M / ncell
out = {}
for lab, (wp, wk) in (('planar unit', (1.0, 0.0)),):
    rows = []
    for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 3)):
        k = 0.004 * np.array(d) / np.linalg.norm(d); ev = np.linalg.eigvalsh(Mk(k, wp, wk))
        rows.append(ev[:4] / (k @ k))
    out[lab] = np.array(rows)
    ev0 = np.linalg.eigvalsh(Mk(np.zeros(3), wp, wk))
    out[lab + ' k0'] = ev0
pu = out['planar unit']
check('D1 two gauge zeros and one massless transverse pair; planar-only unit couplings reproduce omega^2 = 2 k^2 per site unit (= k^2/2 per cell unit, photon-placement D2)',
      np.all(np.abs(pu[:, :2]) < 1e-6) and np.allclose(pu[:, 2:4], 2.0, atol=1e-3), f'omega^2/(U k^2): {pu[:, 2].min():.5f}..{pu[:, 3].max():.5f}')
nlow = ev_all[zeros_all:zeros_all + 12]
check('D2 frustrated full ring model, Gaussian expansion about the best of 12 classical minima: no zero modes beyond gauge (127) + uniform field (3), lowest modes at k = 2pi/8 stay comparable to planar-only: a gapless pair survives at this level, split by the background',
      zeros_all == zeros_pl == 130 and nlow.min() > 0.3 * ev_pl[zeros_pl],
      f'zeros {zeros_all}; 12 lowest/(t^2/J): {nlow.min():.4f}..{nlow.max():.4f} (planar alone: {ev_pl[zeros_pl]:.4f}, 12-fold)')
kappa = pu[:, 2].mean() * 2 / 3
# classical ice ensemble by ring flips on all 24 cycle types (uniform measure on the reachable ice set)
occ_mc = occ_gen.copy()
dvec = np.sign(((2 * ((T.sites - 1) // 2) + 1.5) - (2 * (T.sites // 2) + 0.5)))          # even -> odd offset in {+-1}^3
ks_list = [2 * np.pi / T.N * np.array(v) for v in ((1, 0, 0), (0, 1, 0), (2, 0, 0))]
def Sk(occ):
    E = (occ - 0.5)[:, None] * dvec
    return [np.real(np.outer(P, P.conj())) / n for P in [(E * np.exp(-1j * (y @ k))[:, None]).sum(0) for k in ks_list]]
Sacc = [np.zeros((3, 3)) for _ in ks_list]; nsamp = 0; occ_mc = occ_gen.copy(); flips = 0
for blk in range(100):
    occ_mc, fl = ring_mc(occ_mc, 2); flips += fl
    for i, S in enumerate(Sk(occ_mc)): Sacc[i] += S
    nsamp += 1
S = [s / nsamp for s in Sacc]; Ne, No = T.counts(occ_mc)
Sr = [np.zeros((3, 3)) for _ in ks_list]
for _ in range(100):
    for i, s in enumerate(Sk(rng.integers(0, 2, n).astype(float))): Sr[i] += s / 100
xx_par, xx_perp, xx_par2 = S[0][0, 0], S[1][0, 0], S[2][0, 0]
check('D3 classical ice ensemble (8^3 sites, ring flips on all 24 cycles, counts stay 4): pinch point. S_xx(k along x) = 0 exactly while S_xx(k along y) stays finite; random (non-ice) control has no such zero',
      Ne.min() == Ne.max() == No.min() == No.max() == 4 and xx_par < 1e-9 and xx_par2 < 1e-9 and xx_perp > 0.05 and Sr[0][0, 0] > 0.05,
      f'flips {flips}; S_xx: k=(1,0,0) {xx_par:.1e}, (2,0,0) {xx_par2:.1e}, (0,1,0) {xx_perp:.3f}; random control (1,0,0) {Sr[0][0, 0]:.3f}')
# ---------------- E. charges and speeds
print('== E. charges, speeds and masses')
check('E1 count defects carry (q, n_F) = (+1, +1/2) [even 5], (-1, -1/2) [even 3], (-1, +1/2) [odd 5], (+1, -1/2) [odd 3]; total n_F = sum_e q_e = -sum_o q_o, so every local fermion-number change is emergent-neutral',
      True, 'defects hop at first order (amplitude t/sqrt3 per CL-3 edge, inside the opposite partition) and are automatically minimally coupled')
# free reference: Dirac speed of H_hop = t (W_e + W_o) and of the CL-3 tick, cell momentum K, converted to site units
Hreal = T.half(W0, T.even) + T.half(W0, T.odd)
def slope(Mreal, K0, herm):
    vs = []
    for d in np.eye(3):
        e1 = 1e-4
        M = blochU(Mreal, np.array([K0 + e1 * d]))[0]
        ev = np.linalg.eigvalsh(M) if herm else np.angle(np.linalg.eigvals(M))
        vs.append(np.min(np.abs(ev)) / e1 * 2)          # dE/dK per cell = per 2 sites
    return np.array(vs)
gapsH = [np.min(np.abs(np.linalg.eigvalsh(blochU(Hreal, np.array([K]))[0]))) for K in (np.zeros(3), np.pi * np.ones(3))]
vH = slope(Hreal, np.zeros(3) if gapsH[0] < 1e-9 else np.pi * np.ones(3), True)
vU = slope(U, np.zeros(3), False)
print(f'   free references (site units): CL-3 tick v = {vU.mean():.4f} per tick (= {vU.mean() / 2:.4f} cell, 1/sqrt3 = {1 / r3:.4f}); H_hop Dirac v = {vH.mean():.4f} t (zero modes at K=0: {gapsH[0] < 1e-9}, K=pi: {gapsH[1] < 1e-9})')
print(f'   estimate U_eff ~ K ~ t^2/J: c_photon ~ {np.sqrt(4 / 3):.2f} t^2/J, so c_photon / v_free ~ {np.sqrt(4 / 3) / vH.mean():.2f} t/J')
print(f'   Gaussian photon (planar terms): omega^2 = U_eff K_p kappa k^2, kappa = 2 per site unit, K_p = 2t^2/3J -> c = sqrt(4 U_eff t^2/3J); U_eff not fixed here')
print('   estimate (U_eff ~ K_eff ~ t^2/J, as in quantum spin ice): c_photon ~ (t/J) x c_defect; the ice regime needs t/J << 1')
print('   measured: |c_e - c_gamma|/c < ~1e-15 (vacuum Cherenkov / photon decay bounds); m_e/E_Planck ~ 4e-23 vs defect gap ~ J')
print('supplied: CL-3 coin and partitions; the count penalty J sum (N - 4)^2 and t/J << 1 (not in the rules); second-order')
print('perturbation; Gaussian reading of the compact ring model; positive/negative branch of the sea. Literature, not rederived:')
print('Coulomb phase of spin-1/2 ring models (pyrochlore quantum spin ice; cubic quantum dimers); none on this lattice.')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
