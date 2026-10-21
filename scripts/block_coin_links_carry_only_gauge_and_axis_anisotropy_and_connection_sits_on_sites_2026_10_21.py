#!/usr/bin/env python3
"""What a link of the lattice can carry under the CL-2 tick. Supplied models, finite checks, no physical identification.

 A  The link inside the coin. With every cube edge open, an edge-only block coin is unitary only if every face of
    the block carries flux pi and the edge moduli depend only on the axis, with sum m_a^2 = 1. Field strength
    inside a block breaks unitarity; restoring it (polar part) needs U-turn (body-diagonal) amplitudes.
 B  Metric content of link moduli: bands cos w = sum_a c_a c'_a cos K_a, so the moduli carry only the E part of a
    diagonal metric (2 of 6 components): no trace, no shear.
 C  The connection lives on sites. Link phases compatible with unitary coins are a site phase chi between the even
    and odd half-tick; the gauge group is block phases; field strength sits on mixed plaquettes. CL-2's hop is the
    coarse incidence operator d + d^T (pi flux = boundary of a boundary is zero).
 D  A supplied quadratic law for chi: one isotropic massless pair, gapped extras, no doublers.
 E  Admissibility form: edge factors are nearest-neighbour Markov; a four-site ring is not.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/BLOCK_COIN_LINKS_CARRY_ONLY_GAUGE_AND_AXIS_ANISOTROPY_AND_CONNECTION_SITS_ON_SITES_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import os, sys, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*a):
    raise TimeoutError('120-second cap exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from collections import deque
from scipy.optimize import least_squares

T0 = time.time(); PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- the CL-2 coin ----------------
C = np.array(list(itertools.product((0, 1), repeat=3)))           # corner / residue, index 4x+2y+z
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5)
def coh(n):
    n = n / np.linalg.norm(n); w, v = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); return v[:, -1]
XI = [coh(2 * C[i] - 1.0) for i in range(8)]
EDGES = [(a, b) for a in range(8) for b in range(a + 1, 8) if np.abs(C[a] - C[b]).sum() == 1]
AX = [int(np.argmax(np.abs(C[a] - C[b]))) for a, b in EDGES]
PH0 = [-(XI[a].conj() @ XI[b]) / abs(XI[a].conj() @ XI[b]) for a, b in EDGES]
def coin(mod=None, ph=None):
    W = np.zeros((8, 8), complex)
    for i, (a, b) in enumerate(EDGES):
        m = 1 / np.sqrt(3) if mod is None else mod[i]; p = 0.0 if ph is None else ph[i]
        W[a, b] = m * PH0[i] * np.exp(1j * p); W[b, a] = np.conj(W[a, b])
    return W
W0 = coin(); I8 = np.eye(8)
FACES = []
for ax in range(3):
    o = [k for k in range(3) if k != ax]
    for v in (0, 1):
        def at(p, q):
            t = [0, 0, 0]; t[ax] = v; t[o[0]] = p; t[o[1]] = q; return t[0] * 4 + t[1] * 2 + t[2]
        FACES.append([at(0, 0), at(1, 0), at(1, 1), at(0, 1)])
def hol(W, cyc): return np.prod([W[cyc[(i + 1) % 4], cyc[i]] for i in range(4)])
def tickK(K, X, W):
    D = np.exp(1j * (C @ K)); return (D.conj()[:, None] * X * D[None, :]) @ W

print('== A. the link inside the coin')
check('A1 CL-2 coin (spin-3/2 overlap phases on the 12 edges) is a Hermitian involution with flux pi on all six faces',
      np.abs(W0 - W0.conj().T).max() < 1e-14 and np.abs(W0 @ W0 - I8).max() < 1e-14 and all(abs(hol(W0, f) / abs(hol(W0, f)) + 1) < 1e-12 for f in FACES))
def res_h(x):
    R = coin(x[:12], x[12:]) @ coin(x[:12], x[12:]) - I8; return np.concatenate([R.real.ravel(), R.imag.ravel()])
x0 = np.concatenate([np.full(12, 1 / np.sqrt(3)), np.zeros(12)])
Jac = np.array([(res_h(x0 + 1e-6 * e) - res_h(x0 - 1e-6 * e)) / 2e-6 for e in np.eye(24)]).T
sv = np.linalg.svd(Jac, compute_uv=False); rank = int(np.sum(sv > 1e-6 * sv[0]))
check('A2 the unitary edge-coin family has tangent dimension 9 at CL-2 = 7 site rephasings + 2 axis anisotropies',
      24 - rank == 9, f'Jacobian rank {rank} of 24')
lo = np.concatenate([np.zeros(12), np.full(12, -np.inf)]); hi = np.concatenate([np.full(12, 2.0), np.full(12, np.inf)])
st = []; closed = 0
for t in range(40):
    r = least_squares(res_h, np.concatenate([rng.uniform(0.2, 0.9, 12), rng.uniform(-np.pi, np.pi, 12)]), bounds=(lo, hi),
                      xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
    if np.abs(res_h(r.x)).max() > 1e-9: continue
    m = r.x[:12]
    if m.min() < 1e-3: closed += 1; continue
    W = coin(m, r.x[12:]); ma = [m[[i for i in range(12) if AX[i] == a]] for a in range(3)]
    st.append((max(np.ptp(v) for v in ma), abs(sum(v.mean() ** 2 for v in ma) - 1), max(abs(abs(np.angle(hol(W, f))) - np.pi) for f in FACES)))
st = np.array(st)
check('A3 only if: every solution of W^2 = 1 found from random starts with all edges open has per-axis moduli, '
      'sum m_a^2 = 1 and flux pi on every face', len(st) >= 20 and st.max() < 1e-9,
      f'{len(st)} open solutions (+{closed} with a closed edge); max spread {st[:, 0].max():.0e}, |sum-1| {st[:, 1].max():.0e}, |flux-pi| {st[:, 2].max():.0e}')
ok = 0
for t in range(20):
    c = np.abs(rng.normal(size=3)); c /= np.linalg.norm(c); ph = rng.uniform(-np.pi, np.pi, 8)
    W = coin([c[AX[i]] for i in range(12)], [ph[b] - ph[a] for a, b in EDGES]); ok += np.abs(W @ W - I8).max() < 1e-13
check('A4 if: any per-axis moduli on the unit sphere with any site rephasing give W^2 = 1', ok == 20, f'{ok}/20')
dv = [np.abs(coin(None, [d] + [0] * 11) @ coin(None, [d] + [0] * 11) - I8).max() / d for d in (1e-3, 1e-2, 1e-1)]
def coin_g(z):
    W = np.zeros((8, 8), complex)
    for i, (p, q) in enumerate(EDGES): W[q, p] = z[i] + 1j * z[12 + i]; W[p, q] = z[24 + i] + 1j * z[36 + i]
    return W
def res_u(z): R = coin_g(z).conj().T @ coin_g(z) - I8; return np.concatenate([R.real.ravel(), R.imag.ravel()])
gens = []
for t in range(30):
    r = least_squares(res_u, rng.normal(size=48) * 0.4, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=6000)
    W = coin_g(r.x)
    if np.abs(res_u(r.x)).max() < 1e-9 and np.abs(W[np.abs(W) > 0]).min() > 1e-3 and np.count_nonzero(np.abs(W) > 1e-3) == 24: gens.append(W)
brk = []; keep = 0
for W in gens:
    A = rng.uniform(-0.3, 0.3, 12); WA = W.copy(); g = np.exp(1j * rng.uniform(-np.pi, np.pi, 8))
    for i, (p, q) in enumerate(EDGES): WA[q, p] *= np.exp(1j * A[i]); WA[p, q] *= np.exp(-1j * A[i])
    brk.append(np.abs(WA.conj().T @ WA - I8).max()); WG = np.diag(g) @ W @ np.diag(g.conj()); keep = max(keep, np.abs(WG.conj().T @ WG - I8).max())
check('A5 field strength inside a block breaks unitarity: one link phase d gives ||W^2-1|| = d/3; for general (non-Hermitian) '
      'unitary edge coins a random U(1) dressing breaks W^dag W = 1 while pure gauge keeps it',
      np.allclose(dv, 1 / 3, atol=1e-3) and len(gens) >= 5 and min(brk) > 1e-2 and keep < 1e-12,
      f'd/3 ratios {np.round(dv, 4).tolist()}; {len(gens)} non-Hermitian coins, min break {min(brk):.3f}')
def polar(H): w, V = np.linalg.eigh(H); return (V * np.sign(w)) @ V.conj().T
dist = np.abs(C[:, None, :] - C[None, :, :]).sum(2)
rows = []
for d in (0.0, 0.2, 0.6):
    H = coin(None, rng.uniform(-1, 1, 12) * d); P = polar(H); G = np.diag(np.exp(1j * rng.uniform(-np.pi, np.pi, 8)))
    rows.append((np.abs(P @ P - I8).max() + np.abs(P - P.conj().T).max(), np.abs(polar(G @ H @ G.conj().T) - G @ P @ G.conj().T).max(),
                 np.linalg.norm(P[dist == 2]), np.linalg.norm(P[dist == 3])))
rows = np.array(rows)
check('A6 polar part of a dressed edge hop is a gauge-covariant Hermitian involution; its extra weight is all on U-turns '
      '(body diagonals), none on face diagonals, and vanishes at flux pi', rows[:, :3].max() < 1e-12 and rows[0, 3] < 1e-12 and rows[1:, 3].min() > 1e-2,
      f'U-turn weight at dressing 0, 0.2, 0.6: {np.round(rows[:, 3], 4).tolist()}')

print('== B. metric content of the link moduli')
Wa = [np.zeros((8, 8), complex) for _ in range(3)]
for i, (a, b) in enumerate(EDGES): Wa[AX[i]][a, b] = W0[a, b]; Wa[AX[i]][b, a] = W0[b, a]
eb = 0; ug = 0
for t in range(6):
    c = np.abs(rng.normal(size=3)); c /= np.linalg.norm(c); cp = np.abs(rng.normal(size=3)); cp /= np.linalg.norm(cp)
    We = np.sqrt(3) * sum(c[a] * Wa[a] for a in range(3)); Wo = np.sqrt(3) * sum(cp[a] * Wa[a] for a in range(3))
    for K in rng.uniform(-np.pi, np.pi, size=(60, 3)):
        eb = max(eb, np.abs(np.cos(np.angle(np.linalg.eigvals(tickK(K, Wo, We)))) - (c * cp) @ np.cos(K)).max())
    ug = max(ug, np.abs(We @ We - I8).max())
c2 = np.array([0.8, 0.5, 0.2]); W2 = np.sqrt(3) * sum(c2[a] * Wa[a] for a in range(3))
check('B1 per-axis moduli c (even) and c\' (odd): exactly cos w = sum_a c_a c\'_a cos K_a, and W(c)^2 = 1 iff |c| = 1. '
      'The massless quadratic form is diag(c_a c\'_a): no shear terms, trace fixed by unitarity, c != c\' opens a gap',
      eb < 1e-12 and ug < 1e-13 and abs(np.abs(W2 @ W2 - I8).max() - abs(c2 @ c2 - 1)) < 1e-12, f'band error {eb:.0e}; |c|^2 = 0.93 gives ||W^2-1|| = {np.abs(W2 @ W2 - I8).max():.2f}')
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3)); [R.__setitem__((i, perm[i]), sg[i]) for i in range(3)]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def cls(R):
    t = round(np.trace(R)); return {3: 0, 0: 1, 1: 3}.get(t, 2 if np.allclose(R, np.diag(np.diag(R))) else 4)
CH = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'E': [2, -1, 2, 0, 0], 'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, -1, -1, 1]}
def mult(chars): return {k: round(sum(np.array(v)[cls(R)] * x for R, x in zip(rots, chars)) / 24) for k, v in CH.items()}
sym_idx = [(i, j) for i in range(3) for j in range(i, 3)]
def sym2(R):
    M = np.zeros((6, 6))
    for b, (k, l) in enumerate(sym_idx):
        E = np.zeros((3, 3)); E[k, l] = E[l, k] = 1; F = R @ E @ R.T
        for a, (i, j) in enumerate(sym_idx): M[a, b] = F[i, j]
    return M
mod_rep = mult([np.trace(np.abs(R)) for R in rots]); met_rep = mult([np.trace(sym2(R)) for R in rots])
check('B2 under the 24 rotations the three axis moduli span A1+E, the six metric components A1+E+T2; unitarity removes A1, so '
      'link moduli carry E only (2 of 6): neither the trace (the light-bending part) nor the T2 shear',
      mod_rep == {'A1': 1, 'A2': 0, 'E': 1, 'T1': 0, 'T2': 0} and met_rep == {'A1': 1, 'A2': 0, 'E': 1, 'T1': 0, 'T2': 1})

print('== C. the connection lives on sites')
class Torus:
    def __init__(s, N):
        s.N = N; s.sites = np.array(list(itertools.product(range(N), repeat=3))); s.n = len(s.sites)
        s.idx = {tuple(x): i for i, x in enumerate(s.sites)}; s.even = []; s.odd = []
        for o in itertools.product(range(0, N, 2), repeat=3):
            o = np.array(o); s.even.append([s.idx[tuple((o + C[r]) % N)] for r in range(8)])
            s.odd.append([s.idx[tuple((o + 2 - C[r]) % N)] for r in range(8)])
        s.be = np.zeros(s.n, int); s.bo = np.zeros(s.n, int)
        for b, ss in enumerate(s.even): s.be[ss] = b
        for b, ss in enumerate(s.odd): s.bo[ss] = b
    def half(s, Wb, blocks):
        M = np.zeros((s.n, s.n), complex)
        for ss in blocks: M[np.ix_(ss, ss)] += Wb
        return M
    def plaqs(s):
        out = []
        for x in s.sites:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                p = [x.copy() for _ in range(4)]; p[1][a] += 1; p[2][a] += 1; p[2][b] += 1; p[3][b] += 1
                out.append([s.idx[tuple(q % s.N)] for q in p])
        return out
T = Torus(4); We_ = T.half(W0, T.even); Wo_ = T.half(W0, T.odd); U = Wo_ @ We_; H = We_ + Wo_
Ks = [np.pi * np.array(k) for k in itertools.product(range(2), repeat=3)]
pred = np.sort(np.repeat([np.cos(K).sum() / 3 for K in Ks], 8)); got = np.sort(np.cos(np.angle(np.linalg.eigvals(U))))
check('C1 the tick is a product of two reflections: U + U^dag = H^2 - 2 with H = W_even + W_odd, and the 4^3 torus has the CL-2 bands',
      np.abs(U + U.conj().T - H @ H + 2 * np.eye(T.n)).max() < 1e-13 and np.abs(pred - got).max() < 1e-12)
fl = {'intra': set(), 'mixed': set()}; cnt = {'intra': 0, 'mixed': 0}
for pq in T.plaqs():
    k = 'intra' if len(set(T.be[pq])) == 1 or len(set(T.bo[pq])) == 1 else 'mixed'
    fl[k].add(round(abs(np.angle(np.prod([H[pq[(i + 1) % 4], pq[i]] for i in range(4)]))) / np.pi, 9)); cnt[k] += 1
check('C2 every plaquette of Z^3 carries flux pi in CL-2: the faces of blocks and the mixed plaquettes whose edges lie in four blocks',
      fl == {'intra': {1.0}, 'mixed': {1.0}} and cnt == {'intra': 96, 'mixed': 96}, f'{cnt}')
T8 = Torus(8); H8 = T8.half(W0, T8.even) + T8.half(W0, T8.odd)
S = [[a for a in range(3) if x[a] % 2] for x in T8.sites]; Bd = np.zeros((T8.n, T8.n))
for i, x in enumerate(T8.sites):
    for a in S[i]:
        sg = (-1) ** sum(1 for b in S[i] if b < a)
        for pm in (1, -1):
            t = x.copy(); t[a] = (t[a] + pm) % T8.N; Bd[T8.idx[tuple(t)], i] += pm * sg
D = Bd + Bd.T; g = np.zeros(T8.n, complex); g[0] = 1; seen = {0}; dq = deque([0])
while dq:
    x = dq.popleft()
    for y in np.nonzero(np.abs(H8[:, x]) > 1e-12)[0]:
        if y not in seen: g[y] = np.sqrt(3) * D[y, x] * H8[y, x] * g[x]; seen.add(y); dq.append(y)
Hg = np.sqrt(3) * (g.conj()[:, None] * H8 * g[None, :]); mask = np.abs(H8) > 1e-12
check('C3 CL-2\'s hop is the incidence operator d + d^T of the coarse cell complex (sites with 0,1,2,3 odd coordinates = '
      'vertices, edges, faces, cubes), up to site phases on the 8^3 torus; d^2 = 0 is what puts pi through every plaquette',
      np.abs(Bd @ Bd).max() == 0 and np.abs(Hg[mask] - D[mask]).max() < 1e-12, f'max deviation {np.abs(Hg[mask] - D[mask]).max():.0e} on {int(mask.sum())} entries')
pe = rng.uniform(-np.pi, np.pi, T.n); po = rng.uniform(-np.pi, np.pi, T.n); Ge = np.diag(np.exp(1j * pe)); Go = np.diag(np.exp(1j * po))
WeA = np.zeros_like(We_); WoA = np.zeros_like(Wo_)
for ss in T.even: WeA[np.ix_(ss, ss)] = (Ge @ We_ @ Ge.conj().T)[np.ix_(ss, ss)]
for ss in T.odd: WoA[np.ix_(ss, ss)] = (Go @ Wo_ @ Go.conj().T)[np.ix_(ss, ss)]
Th = np.diag(np.exp(1j * (pe - po))); HA = WeA + WoA; dmix = dint = 0
for pq in T.plaqs():
    r = np.prod([HA[pq[(i + 1) % 4], pq[i]] for i in range(4)]) / np.prod([H[pq[(i + 1) % 4], pq[i]] for i in range(4)])
    if len(set(T.be[pq])) == 1 or len(set(T.bo[pq])) == 1: dint = max(dint, abs(np.angle(r)))
    else:
        ch = (pe - po)[pq]; al = ch[0] - ch[1] + ch[2] - ch[3]; dmix = max(dmix, min(abs(np.angle(r * np.exp(-1j * al))), abs(np.angle(r * np.exp(1j * al)))))
check('C4 link phases that keep every block coin unitary (pure gauge inside each block) are a site phase chi = phi_e - phi_o '
      'applied between the half-ticks; they leave block faces at pi and change mixed fluxes by the alternating sum of chi',
      np.abs(Ge.conj().T @ (WoA @ WeA) @ Ge - Th.conj() @ Wo_ @ Th @ We_).max() < 1e-12 and dint < 1e-12 and dmix < 1e-12)
chi = rng.uniform(-np.pi, np.pi, T.n); Tc = np.diag(np.exp(1j * chi)); Uc = Tc.conj() @ Wo_ @ Tc @ We_
le = rng.uniform(-np.pi, np.pi, len(T.even)); lo_ = rng.uniform(-np.pi, np.pi, len(T.odd)); Le = np.diag(np.exp(1j * le[T.be]))
Tc2 = np.diag(np.exp(1j * (chi + lo_[T.bo] - le[T.be])))
bare = np.abs(Le @ U @ Le.conj().T - U).max()
check('C5 U(chi) = Theta^dag W_odd Theta W_even is unitary and covariant under independent phases on every even and odd block; '
      'without chi the bare tick has no such local symmetry (only the global phase)',
      np.abs(Uc @ Uc.conj().T - np.eye(T.n)).max() < 1e-12 and np.abs(Tc2.conj() @ Wo_ @ Tc2 @ We_ - Le @ Uc @ Le.conj().T).max() < 1e-12 and bare > 0.1,
      f'bare tick changed by block phases: {bare:.2f}')
Pb = [np.diag(np.isin(np.arange(T.n), ss).astype(float)) for ss in T.even[:4]]; Pbo = [np.diag(np.isin(np.arange(T.n), ss).astype(float)) for ss in T.odd[:4]]
check('C6 each half-tick keeps every block\'s odds inside the block, so all transport between blocks passes through sites: '
      'a site is the link of the block lattice joining its even and odd block',
      max(np.abs(P @ We_ - We_ @ P).max() for P in Pb) < 1e-14 and max(np.abs(P @ Wo_ - Wo_ @ P).max() for P in Pbo) < 1e-14)

print('== D. a supplied quadratic law for chi on the block lattice (electric sum E^2/2, magnetic sum over mixed plaquettes)')
mixed = []
for r in C:
    for a, b in ((0, 1), (1, 2), (0, 2)):
        cs = [r.copy() for _ in range(4)]; cs[1][a] += 1; cs[2][a] += 1; cs[2][b] += 1; cs[3][b] += 1
        pq = [T.idx[tuple(q % 4)] for q in cs]
        if not (len(set(T.be[pq])) == 1 or len(set(T.bo[pq])) == 1): mixed.append(cs)
def Mk(k):
    Cm = np.zeros((len(mixed), 8), complex)
    for i, cs in enumerate(mixed):
        for j, q in enumerate(cs): rr = q % 2; Cm[i, int(rr @ [4, 2, 1])] += (-1) ** j * np.exp(1j * k @ ((q - rr) // 2))
    return Cm.conj().T @ Cm
e0 = np.linalg.eigvalsh(Mk(np.zeros(3))); zr = [int(np.sum(np.linalg.eigvalsh(Mk(rng.uniform(-np.pi, np.pi, 3))) < 1e-9)) for _ in range(300)]
check('D1 12 mixed plaquettes per 2x2x2 cell; block phases are exact zero modes and the only ones away from k = 0; at k = 0 four zeros '
      '(gauge + uniform connection) and gapped 8, 8, 8, 24', len(mixed) == 12 and set(zr) == {2} and np.allclose(e0, [0, 0, 0, 0, 8, 8, 8, 24], atol=1e-9))
rat = []
for d in ([1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 2, 3]):
    d = np.array(d, float) / np.linalg.norm(d); rat += list(np.linalg.eigvalsh(Mk(0.05 * d))[2:4] / 0.05 ** 2)
kr = rng.uniform(-np.pi, np.pi, size=(2000, 3)); lowest = min(np.linalg.eigvalsh(Mk(k))[2] / (2 * np.sum(1 - np.cos(k))) for k in kr)
hs = [np.linalg.eigvalsh(Mk(np.pi * np.array(v)))[2] for v in ([1, 0, 0], [1, 1, 0], [1, 1, 1])]
check('D2 one isotropic massless pair, omega^2 = k^2/2 (cell units, unit couplings) in four directions; no second massless point '
      '(third eigenvalue / 2 sum(1 - cos k) stays bounded below over the zone; zone corners gapped)', np.ptp(rat) < 2e-4 and abs(np.mean(rat) - 0.5) < 2e-4 and lowest > 0.05 and min(hs) > 0.5,
      f'omega^2/k^2 in [{min(rat):.5f}, {max(rat):.5f}], min ratio over zone {lowest:.3f}, corners {np.round(hs, 2).tolist()}')
wf = np.abs(np.angle(np.linalg.eigvals(tickK(np.array([0.01, 0.0, 0.0]), W0, W0)))).min()
print(f'   speed: the coin gives c = {wf / 0.01:.4f} = 1/sqrt3 cell per tick; chi with per-tick angles tau*g_E, tau*g_B gives c = tau sqrt(g_E g_B / 2):'
      ' equal only if tau^2 g_E g_B = 2/3, a supplied tuning')

print('== E. Admissibility form on the triangle-free block graph (8 binary sites)')
cfg = np.array(list(itertools.product((0, 1), repeat=8))); spin = 2 * cfg - 1.0
nbr = {a: [b for b in range(8) if dist[a, b] == 1] for a in range(8)}
def law(J, K):
    E = sum(J[i] * spin[:, a] * spin[:, b] for i, (a, b) in enumerate(EDGES)) + 0.3 * spin.sum(1)
    if K: E = E + K * spin[:, FACES[0]].prod(1)
    p = np.exp(E); return p / p.sum()
def markov_dev(p):
    dev = 0.0; P = p.reshape([2] * 8)
    for a in range(8):
        cond = np.moveaxis(P, a, 0); cond = cond[1] / (cond[0] + cond[1])                 # P(s_a = 1 | rest)
        for b in range(8):
            if b == a or b in nbr[a]: continue
            ax = b if b < a else b - 1; dev = max(dev, np.abs(np.take(cond, 0, ax) - np.take(cond, 1, ax)).max())
    return dev
J = rng.normal(size=12)
check('E1 a positive law with site and edge factors is nearest-neighbour Markov (each site\'s conditional ignores non-neighbours); '
      'adding one four-site face ring makes a corner\'s conditional depend on its face-diagonal partner', markov_dev(law(J, 0)) < 1e-12 and markov_dev(law(J, 0.7)) > 1e-2,
      f'dependence on non-neighbours: {markov_dev(law(J, 0)):.0e} without ring, {markov_dev(law(J, 0.7)):.3f} with ring')

print('== measured-reality arithmetic')
a = np.sqrt(8 * np.pi) * 1.616255e-35; Ea = 1.973270e-7 / a
print(f'   lattice energy hbar c / a = {Ea:.2e} eV for a = sqrt(8 pi) l_P; photon mass < 1e-18 eV (PDG) is {1e-18 / Ea:.0e} of it: an unprotected composite needs that tuning')
print('   speed ties: |c_e - c_gamma| < ~1e-11 (LEP/Tevatron, Hohensee et al. 2009), 1e-16..1e-21 (Crab, model-dependent); '
      'GW170817 (c_g - c_gamma)/c in [-3e-15, +7e-16]; so tau^2 g_E g_B must equal 2/3 to ~2e-11 or better')
print('   Cassini: gamma - 1 = (2.1 +- 2.3)e-5; the trace of the spatial metric cannot ride on link moduli (B1, B2)')
print('supplied: CL-2 coin and partitions; all edges open; minimal coupling as hop or site phases; the quadratic chi law and its couplings;'
      ' positivity and a joint law in E. Not derived: a carrier for chi, photon speed, Coulomb phase, any physical identification.')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
