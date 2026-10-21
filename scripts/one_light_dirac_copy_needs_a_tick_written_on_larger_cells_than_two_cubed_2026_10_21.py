#!/usr/bin/env python3
"""Cell geometry and the number of light Dirac copies for covariant partitioned ticks, one fermion mode per site of Z^3.

Sections:
 1  partition geometry: two-partition L^3 Margolus ticks are cubic covariant only for offset (L/2)(1,1,1); 3^3 never;
 2  site actions: which site stabilisers admit a spinorial character (2 pi rotation = -1); parity forces the
    corner (C3v) character to the j = 3/2 type;
 3  K-point counting for every O-invariant sublattice of index <= 64: which geometries can host ONE Dirac at an
    invariant momentum (rotations only: an E1/2 or E5/2 of multiplicity >= 2; with parity: E1/2g + E1/2u);
 4  integer-spin site actions force an even number of light copies;
 5  zoom: reading the supplied 2^3 spin-3/2 tick on 4^3 cells leaves 8 light states (two copies);
 6  a 4^3 Margolus tick (blocks of 2^3 blocks) with exactly one light Dirac fermion: unitarity, exact O_h
    covariance, light content, Dirac form, isotropy.
Supplied model, finite diagnostic; no physical identification; not derived from the axioms.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/ONE_LIGHT_DIRAC_COPY_NEEDS_A_TICK_WRITTEN_ON_LARGER_CELLS_THAN_TWO_CUBED_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys
from math import comb
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------------------------------------------------------- groups O' and O_h' (inversion central, I^2 = 1)
s0 = np.eye(2, dtype=complex); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
def so3(U): return np.array([[0.5 * np.trace(a @ U @ b @ U.conj().T).real for b in (sx, sy, sz)] for a in (sx, sy, sz)])
def su2(ax, ang):
    ax = np.array(ax, float); ax /= np.linalg.norm(ax); return np.cos(ang / 2) * s0 - 1j * np.sin(ang / 2) * (ax[0] * sx + ax[1] * sy + ax[2] * sz)
Op = [s0]
while True:
    new = [g @ h for g in Op for h in (su2([0, 0, 1], np.pi / 2), su2([1, 1, 1], 2 * np.pi / 3))]
    add = [n for n in new if not any(np.allclose(n, m) for m in Op)]
    if not add: break
    for n in add:
        if not any(np.allclose(n, m) for m in Op): Op.append(n)
def jmat(j):
    m = j - np.arange(int(round(2 * j)) + 1); Jp = np.diag(np.sqrt(j * (j + 1) - m[1:] * (m[1:] + 1)), 1).astype(complex)
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def spin_j(U, j):
    c = np.clip(np.trace(U).real / 2, -1, 1); th = 2 * np.arccos(c)
    if abs(np.sin(th / 2)) < 1e-12: return np.eye(int(2 * j + 1)) * (1 if c > 0 else (-1) ** int(round(2 * j)))
    v = np.array([np.trace(1j * U @ a).real / 2 for a in (sx, sy, sz)]) / np.sin(th / 2)
    w, V = np.linalg.eigh(sum(v[k] * jmat(j)[k] for k in range(3))); return V @ np.diag(np.exp(-1j * th * w)) @ V.conj().T

class Group:
    def __init__(self, with_inv):
        self.el = [(U, e) for e in ((0, 1) if with_inv else (0,)) for U in Op]; self.n = len(self.el)
        self.R = [so3(U) * (-1) ** e for U, e in self.el]
        kk = lambda U, e: (e,) + tuple(np.round(np.concatenate([U.real.ravel(), U.imag.ravel()]), 6) + 0.0)
        tab = {kk(U, e): k for k, (U, e) in enumerate(self.el)}
        self.mul = np.array([[tab[kk(a[0] @ b[0], (a[1] + b[1]) % 2)] for b in self.el] for a in self.el])
        self.inv = np.array([int(np.where(self.mul[i] == 0)[0][0]) for i in range(self.n)])
        self.minus1 = tab[kk(-s0, 0)]
        A2 = lambda R: round(np.linalg.det(np.abs(np.round(R))))
        self.irr = {}
        for par in ((0, 1) if with_inv else (0,)):
            sf = ('g', 'u')[par] if with_inv else ''
            self.irr['E1/2' + sf] = np.array([np.trace(U) * (-1) ** (e * par) for U, e in self.el])
            self.irr['E5/2' + sf] = np.array([np.trace(U) * A2(so3(U)) * (-1) ** (e * par) for U, e in self.el])
            self.irr['G3/2' + sf] = np.array([np.trace(spin_j(U, 1.5)) * (-1) ** (e * par) for U, e in self.el])
        for k, ch in self.irr.items(): assert abs(np.vdot(ch, ch).real / self.n - 1) < 1e-9, k
    def close(self, gs):
        S = {0}; fr = [0]
        while fr:
            nf = []
            for a in fr:
                for g in gs:
                    b = self.mul[a, g]
                    if b not in S: S.add(b); nf.append(b)
            fr = nf
        return S
    def order(self, g):
        k, a = 1, g
        while a != 0: a = self.mul[a, g]; k += 1
        return k
    def chars_1d(self, H):
        """all 1-dim characters of the subgroup H with chi(-1) = -1 (spinorial), by consistent extension from generators."""
        Hs = set(H); gens, span = [], {0}
        for h in H:
            if h not in span: gens.append(h); span = self.close(gens)
        out = []
        for vals in itertools.product(*[range(self.order(g)) for g in gens]):
            gv = [np.exp(2j * np.pi * v / self.order(g)) for v, g in zip(vals, gens)]
            chi = {0: 1.0 + 0j}; fr = [0]; ok = True
            while fr and ok:
                nf = []
                for a in fr:
                    for g, v in zip(gens, gv):
                        b = self.mul[a, g]; val = chi[a] * v
                        if b in chi:
                            if abs(chi[b] - val) > 1e-8: ok = False; break
                        else: chi[b] = val; nf.append(b)
                    if not ok: break
                fr = nf
            if ok and set(chi) == Hs and abs(chi[self.minus1] + 1) < 1e-8: out.append(chi)
        return out
GO, GH = Group(False), Group(True)

def lattice(kind, a):
    return a * {'sc': np.eye(3), 'fcc': np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]]).T, 'bcc': np.array([[2, 0, 0], [0, 2, 0], [1, 1, 1]]).T}[kind].astype(float)

def survey(G, B, p):
    Binv = np.linalg.inv(B); N = int(round(abs(np.linalg.det(B))))
    def key(x): f = Binv @ x; f = np.round(f - np.floor(f + 1e-7), 5) % 1.0; return tuple(np.round(f, 5) + 0.0)
    reps = {}
    for x in itertools.product(range(int(np.max(np.abs(B))) * 2 + 2), repeat=3):
        k = key(np.array(x, float)); reps.setdefault(k, np.array(x, float))
    keys = list(reps); idx = {k: i for i, k in enumerate(keys)}; pos = np.array([reps[k] for k in keys])
    act = np.zeros((G.n, N), int)
    for g in range(G.n):
        for i in range(N):
            y = G.R[g] @ (pos[i] - p) + p; assert np.allclose(y, np.round(y)); act[g, i] = idx[key(y)]
    seen, orbs = set(), []
    for i in range(N):
        if i in seen: continue
        o = sorted(set(act[:, i])); seen |= set(o); H = [g for g in range(G.n) if act[g, o[0]] == o[0]]
        orbs.append(dict(orb=o, size=len(o), H=H, chis=G.chars_1d(H)))
    return dict(N=N, pos=pos, act=act, orbits=orbs, B=B, p=p, key=key, idx=idx)

def induced_char(G, S, oi, chi, K=np.zeros(3)):
    o = S['orbits'][oi]; i0 = o['orb'][0]; act, pos, p = S['act'], S['pos'], S['p']; gs = {}
    for g in range(G.n): gs.setdefault(act[g, i0], g)
    ch = np.zeros(G.n, complex)
    for g in range(G.n):
        for s in o['orb']:
            if act[g, s] == s:
                h = G.mul[G.inv[gs[s]], G.mul[g, gs[s]]]; R = G.R[g]
                ch[g] += chi[h] * np.exp(1j * (R @ K - K) @ (R @ (pos[s] - p)))
    return ch
def decomp(G, ch): return {k: int(round((np.vdot(v, ch) / G.n).real)) for k, v in G.irr.items() if abs(np.vdot(v, ch)) / G.n > 1e-6}
def invariant_K(G, B):
    Bst = 2 * np.pi * np.linalg.inv(B).T; out = []
    for c in itertools.product(range(4), repeat=3):
        K = Bst @ (np.array(c) / 4)
        if all(np.allclose(np.linalg.solve(Bst, G.R[g] @ K - K), np.round(np.linalg.solve(Bst, G.R[g] @ K - K)), atol=1e-8) for g in range(G.n)): out.append(K)
    return out

# ================================================================ 1
print('== 1. partition geometry')
def covariant_offsets(L):
    """offsets t (mod L) of the second L^3 partition for which a common point p is a rotation centre of both partitions.
    d = (block centre - p) must satisfy R d - d in L Z^3 for all 24 R; t is allowed iff d and d + t are both such."""
    cands = [np.array(v) / 2 for v in itertools.product(range(2 * L), repeat=3)]
    good = [d for d in cands if all(np.allclose((R @ d - d) / L, np.round((R @ d - d) / L)) for R in GO.R)]
    ok = []
    for t in itertools.product(range(L), repeat=3):
        if any(all(np.allclose((R @ (d + t) - d - t) / L, np.round((R @ (d + t) - d - t) / L)) for R in GO.R) for d in good): ok.append(tuple(t))
    return ok
offs = {L: covariant_offsets(L) for L in (2, 3, 4, 5)}
check('L^3 blocks, two partitions: cubic covariance about a common centre holds only for offset 0 or (L/2)(1,1,1); none for odd L',
      all(offs[L] == ([(0, 0, 0)] if L % 2 else [(0, 0, 0), (L // 2,) * 3]) for L in offs), str(offs))

# ================================================================ 2
print('== 2. site actions (one mode per site; spinorial = 2 pi rotation acts as -1)')
def stab_label(G, H):
    rot = [g for g in H if G.el[g][1] == 0]; n = len(rot) // 2; imp = len(H) > len(rot)
    orders = [G.order(g) for g in rot]   # SU(2) orders: a C_n axis lifts to order 2n
    cyc = max(orders) == 2 * n if n > 1 else True
    lab = {1: 'C1'}.get(n) if n == 1 else (f'C{n}' if cyc else {2: 'D1', 4: 'D2', 6: 'D3', 8: 'D4', 12: 'T', 24: 'O'}[n])
    return lab + ('+imp' if imp else '')
def stab_types(G):
    out = {}
    for kind, a in [('sc', 2), ('bcc', 1), ('bcc', 2), ('sc', 4), ('fcc', 2), ('sc', 3)]:
        for p in (np.zeros(3), np.full(3, .5)):
            S = survey(G, lattice(kind, a), p)
            for o in S['orbits']: out.setdefault(stab_label(G, o['H']), set()).add(len(o['chis']) > 0)
    return out
so, sh = stab_types(GO), stab_types(GH)
check('rotations only: a spinorial site character exists exactly for stabilisers C1, C2, C3, C4, D3; never for D2, D4, T, O',
      all(so.get(k) == {True} for k in ('C1', 'C2', 'C3', 'C4', 'D3')) and all(so.get(k) == {False} for k in ('D2', 'D4', 'T', 'O')),
      str({k: sorted(v) for k, v in so.items()}))
S8 = survey(GH, lattice('sc', 2), np.full(3, .5)); o = S8['orbits'][0]
c3 = [g for g in o['H'] if abs(np.trace(GH.el[g][0]).real - 1) < 1e-9 and GH.el[g][1] == 0]  # C3 lift with trace +1
check('with parity, the 2^3 corner (stabiliser C3v): every spinorial character has chi(C3) = -1 (the j = 3/2 type); K=0 space = G3/2g + G3/2u',
      all(abs(chi[g] + 1) < 1e-9 for chi in o['chis'] for g in c3) and all(decomp(GH, induced_char(GH, S8, 0, chi)) == {'G3/2g': 1, 'G3/2u': 1} for chi in o['chis']),
      f"{len(o['chis'])} characters")
live_h = sorted(k for k, v in sh.items() if v == {True}); dead_h = sorted(k for k, v in sh.items() if v == {False})
check('with parity: live site stabilisers are C1(+imp, i.e. Cs), C3+imp (C3v) and D3+imp (D3d); C2v-, C4v-type and larger are dead',
      set(live_h) == {'C1+imp', 'C3+imp', 'D3+imp'}, f'live {live_h}; dead {dead_h}')

# ================================================================ 3
print('== 3. capacity for ONE Dirac at an invariant momentum')
def capacity(G, S, Ks):
    """best over live character choices and invariant K: rotations: max multiplicity of E1/2 or E5/2; parity: min(E1/2g,E1/2u) or (E5/2g,E5/2u)."""
    live = [o for o in S['orbits'] if o['chis']]; dead = sum(o['size'] for o in S['orbits'] if not o['chis']); best = 0
    choices = [range(len(o['chis'])) for o in live]
    for cs in itertools.product(*choices):
        for K in Ks:
            tot = {}
            for o, c in zip(live, cs):
                d = decomp(G, induced_char(G, S, S['orbits'].index(o), o['chis'][c], K))
                for k, v in d.items(): tot[k] = tot.get(k, 0) + v
            if G is GO: val = max(tot.get('E1/2', 0), tot.get('E5/2', 0))
            else: val = max(min(tot.get('E1/2g', 0), tot.get('E1/2u', 0)), min(tot.get('E5/2g', 0), tot.get('E5/2u', 0)))
            best = max(best, val)
    return best, dead
rows = []
for kind, a in [('sc', 2), ('fcc', 1), ('bcc', 1), ('fcc', 2), ('sc', 3), ('bcc', 2), ('sc', 4)]:
    B = lattice(kind, a)
    for pn, p in (('site', np.zeros(3)), ('body', np.full(3, .5))):
        cO, dO = capacity(GO, survey(GO, B, p), invariant_K(GO, B)); cH, dH = capacity(GH, survey(GH, B, p), invariant_K(GH, B))
        rows.append((f'{kind}{a}', pn, int(round(abs(np.linalg.det(B)))), cO, dO, cH, dH))
for r in rows: print(f"   {r[0]:5s} centre={r[1]:4s} N={r[2]:2d}  O: E-mult {r[3]} (dead sites {r[4]:2d})   O_h: Dirac pairs {r[5]} (dead {r[6]:2d})")
cap = {(r[0], r[1]): r for r in rows}
check('2^3 rung (Lambda = 2Z^3, body centre): no site action gives an E1/2/E5/2 of multiplicity 2 at any invariant K (rotations), none at all with parity',
      cap[('sc2', 'body')][3] == 1 and cap[('sc2', 'body')][5] == 0)
liveO = [r for r in rows if r[3] >= 2 and r[4] == 0]; liveH = [r for r in rows if r[5] >= 1 and r[6] == 0]
check('rotations only: the smallest dead-free geometry with single-Dirac capacity has 16 sites per cell (2 x FCC, two j=1/2 corner orbits)',
      min(r[2] for r in liveO) == 16 and ('fcc2', 'body') in [(r[0], r[1]) for r in liveO], str([(r[0], r[1], r[2]) for r in liveO]))
check('with parity: smallest dead-free geometry with an E1/2g + E1/2u pair has 32 sites per cell (2 x BCC); the uniform 4^3 cell (64) has two pairs',
      min(r[2] for r in liveH) == 32 and cap[('sc4', 'body')][5] == 2, str([(r[0], r[1], r[2]) for r in liveH]))

# ================================================================ 4
print('== 4. integer-spin site actions')
dims = {k: round(v[0].real) for k, v in GO.irr.items()}
E12 = GO.irr['E1/2']; prods = [E12 * GO.irr[k] for k in GO.irr]
check('spinorial irreps of O\' have dimensions 2, 2, 4 (all even); E1/2 x (spinorial) is a genuine rep (2 pi -> +1)',
      sorted(dims.values()) == [2, 2, 4] and all(abs(ch[GO.minus1] - ch[0]) < 1e-9 for ch in prods), str(dims))
print('   => if every site is integer-spin, a light spin-1/2 sector carries rotations as E1/2 x tau with tau spinorial:'
      ' the copy space has even dimension >= 2')

# ================================================================ 5
print('== 5. zoom: the supplied 2^3 spin-3/2 Wilson-type tick read on 4^3 cells')
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float)
def coherent(j, n):
    n = n / np.linalg.norm(n); th, ph, d = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])
XI = [coherent(1.5, v) for v in NV]; W32 = np.zeros((8, 8), complex)
for s, t in itertools.product(range(8), repeat=2):
    if abs(CORN[s] - CORN[t]).sum() == 1: g = XI[s].conj() @ XI[t]; W32[s, t] = -g / abs(g) / np.sqrt(3)
Va = lambda a: np.cos(a) * W32 + 1j * np.sin(a) * np.eye(8)
def fine_tick(K, ve, vo):
    D = np.exp(1j * (CORN @ K)); return (D[:, None] * vo * D.conj()[None, :]) @ ve
mu, bb = 0.05, 0.6
qe = np.concatenate([-np.angle(np.linalg.eigvals(fine_tick(np.pi * np.array(c, float), Va(mu / 2 + bb), Va(mu / 2 - bb)))) for c in itertools.product((0, 1), repeat=3)])
nl = int(np.sum(np.abs(qe) < 0.3))
check('coarse K = 0 of the 4^3 cell = fine block momenta {0, pi}^3: exactly 8 light states (|w| < 0.3), two copies, rest levels fourfold',
      nl == 8 and np.allclose(np.sort(np.abs(qe[np.abs(qe) < 0.3])), mu, atol=1e-9), f'light |w| = {np.round(np.sort(qe[np.abs(qe) < 0.3]), 4)}')
print('   (coarse-graining relabels Bloch states: it folds doublers onto K = 0 and never removes a light state)')

# ================================================================ 6
print('== 6. a 4^3 Margolus tick with one light Dirac fermion (one mode per site)')
G = GH; L = 4; p = np.full(3, 1.5); q = p + 2
S = survey(G, lattice('sc', 4), p); act = S['act']
loc = {tuple(int(v) % L for v in x): i for i, x in enumerate(S['pos'])}
def coset(x): return loc[tuple(int(round(v)) % L for v in x)]
orb_of = np.zeros(64, int); gs = {}; chis = []
for oi, o in enumerate(S['orbits']):
    for s in o['orb']: orb_of[s] = oi
    chis.append(o['chis'][0])
    for g in range(G.n): gs.setdefault(act[g, o['orb'][0]], g)
def phase(g, s): return chis[orb_of[s]][G.mul[G.inv[gs[act[g, s]]], G.mul[g, gs[s]]]]
def site_rep(g, sites, centre):
    idx = {tuple(x): i for i, x in enumerate(sites)}; M = np.zeros((len(sites), len(sites)), complex)
    for i, x in enumerate(sites):
        y = G.R[g] @ (np.array(x, float) - centre) + centre; M[idx[tuple(int(round(v)) for v in y)], i] = phase(g, coset(x))
    return M
even = [tuple(x) for x in itertools.product(range(4), repeat=3)]; odd = [tuple(np.array(x) + 2) for x in even]
Rp = [site_rep(g, even, p) for g in range(G.n)]; Rq = [site_rep(g, odd, q) for g in range(G.n)]
herr = max(np.abs(Rp[G.mul[a, b]] - Rp[a] @ Rp[b]).max() + np.abs(Rq[G.mul[a, b]] - Rq[a] @ Rq[b]).max() for a in range(G.n) for b in range(0, G.n, 11))
check('induced site action is a representation of O_h\' on even and odd 4^3 blocks', herr < 1e-12, f'{herr:.1e}')
proj = lambda Rs, nm: round(G.irr[nm][0].real) / G.n * sum(np.conj(G.irr[nm][g]) * Rs[g] for g in range(G.n))
edge = np.diag([1.0 if tuple(sorted(np.abs(np.array(x) - 1.5))) == (0.5, 1.5, 1.5) else 0 for x in even])
Pg, Pu = edge @ proj(Rp, 'E1/2g') @ edge, edge @ proj(Rp, 'E1/2u') @ edge
cs_e = [coset(x) for x in even]; cs_o = [coset(x) for x in odd]
def to_cos(M):
    out = np.zeros_like(M); out[np.ix_(cs_e, cs_e)] = M; return out
Pg, Pu = to_cos(Pg), to_cos(Pu); P = Pg + Pu; Q = np.eye(64) - P
check('molecular multiplet on the 24 edge-centre sites of a block: E1/2g and E1/2u projectors of rank 2 each',
      np.isclose(np.trace(Pg).real, 2) and np.isclose(np.trace(Pu).real, 2) and np.abs(Pg @ Pu).max() < 1e-12)
# odd-block hop: (1,0,2)-type hop between edge-centre sites of different even blocks, imaginary amplitude, O_h' averaged
ia, ib = odd.index((2, 3, 3)), odd.index((3, 3, 5)); M0 = np.zeros((64, 64), complex); M0[ia, ib] = 1j; M0[ib, ia] = -1j
h = sum(R @ M0 @ R.conj().T for R in Rq) / G.n; h /= np.abs(np.linalg.eigvalsh(h)).max()
nb = len({(min(a, b), max(a, b)) for a, b in np.argwhere(np.abs(h) > 1e-12)})
Xo = 4.0 * np.floor(np.array(odd, float) / 4)   # cell vector of each odd-block site (Bloch phases relative to the cell)
def HB(K):
    ph = np.exp(1j * Xo @ K); Hk = np.zeros((64, 64), complex); Hk[np.ix_(cs_o, cs_o)] = h * (ph.conj()[:, None] * ph[None, :]); return Hk
Eb, t, muL = np.pi / 2, 0.4, 0.01
def HA(c0, m0): return Eb * Q + c0 * P + m0 * (Pg - Pu)
def tick(K, c0, m0):
    A = expm(-0.5j * HA(c0, m0)); return A @ expm(-1j * t * HB(K)) @ A
def gamma_levels(c0, m0):
    w, V = np.linalg.eig(tick(np.zeros(3), c0, m0)); qv = -np.angle(w); n = np.real(np.einsum('ij,ij->j', V.conj(), V))
    fg = np.real(np.einsum('ji,jk,ki->i', V.conj(), Pg, V)) / n; fu = np.real(np.einsum('ji,jk,ki->i', V.conj(), Pu, V)) / n
    return qv[np.argmax(fg)], qv[np.argmax(fu)]
c0 = m0 = 0.0
for _ in range(40):
    a_, b_ = gamma_levels(c0, m0); c0 -= (a_ + b_) / 2; m0 -= (a_ - b_) / 2 - muL
print(f'   block rule: H_A = (pi/2) Q + c0 P + m0 (P_g - P_u) on even blocks, t h on odd blocks ({nb} bonds), tick = e^(-iH_A/2) e^(-i t h) e^(-iH_A/2)')
print(f'   tuned c0 = {c0:.2e}, m0 = {m0:.5f} (mass tuning: Gamma levels at +-{muL})')
U0 = tick(np.array([0.1, 0.2, 0.3]), c0, m0)
check('tick is unitary', np.abs(U0 @ U0.conj().T - np.eye(64)).max() < 1e-12)
# real-space check on an 8^3 torus: commutes with O_h' generators about p and with Lambda translations
L8 = 8; sites = list(itertools.product(range(L8), repeat=3)); sidx = {s: i for i, s in enumerate(sites)}
def embed(blockM, sites_blk, origin):
    out = np.zeros((512, 512), complex); ii = [sidx[tuple((np.array(x) + origin) % L8)] for x in sites_blk]; out[np.ix_(ii, ii)] = blockM; return out
HAe = np.zeros((64, 64), complex); HAe[:, :] = HA(c0, m0)[np.ix_(cs_e, cs_e)]
Ae = sum(embed(expm(-0.5j * HAe), even, np.array(o)) for o in itertools.product((0, 4), repeat=3))
Bo = sum(embed(expm(-1j * t * h), odd, np.array(o)) for o in itertools.product((0, 4), repeat=3))
Ureal = Ae @ Bo @ Ae
def global_rep(g):
    M = np.zeros((512, 512), complex)
    for i, x in enumerate(sites):
        y = G.R[g] @ (np.array(x, float) - p) + p; M[sidx[tuple(int(round(v)) % L8 for v in y)], i] = phase(g, coset(x))
    return M
gens = [g for g in range(G.n) if np.allclose(G.R[g], [[0, -1, 0], [1, 0, 0], [0, 0, 1]]) or np.allclose(G.R[g], [[0, 0, 1], [1, 0, 0], [0, 1, 0]]) or np.allclose(G.R[g], -np.eye(3))]
cerr = max(np.abs(Rg @ Ureal @ Rg.conj().T - Ureal).max() for Rg in (global_rep(g) for g in gens))
T4 = np.zeros((512, 512));
for i, x in enumerate(sites): T4[sidx[((x[0] + 4) % 8, x[1], x[2])], i] = 1
check('8^3 torus: tick commutes with the O_h\' generators (C4, C3, inversion and their lifts) about p and with translation by 4',
      cerr < 1e-12 and np.abs(T4 @ Ureal @ T4.T - Ureal).max() < 1e-12, f'{cerr:.1e} over {len(gens)} lifts')
wr = np.sort(-np.angle(np.linalg.eigvals(Ureal)))
wb = np.sort(np.concatenate([-np.angle(np.linalg.eigvals(tick(np.pi / 4 * np.array(c, float), c0, m0))) for c in itertools.product((0, 1), repeat=3)]))
check('Bloch tick reproduces the 512 real-space quasi-energies', np.abs(wr - wb).max() < 1e-9, f'{np.abs(wr - wb).max():.1e}')
# Gamma content
w0, V0 = np.linalg.eig(tick(np.zeros(3), c0, m0)); q0 = -np.angle(w0); light = np.abs(q0) < 0.3
Vl = V0[:, light]; ql = q0[light]
def irr_of(vecs):
    Pl = vecs @ np.linalg.pinv(vecs); ch = np.array([np.trace(Pl @ to_cos(Rp[g])) for g in range(G.n)]); return decomp(G, ch)
up, dn = Vl[:, ql > 0], Vl[:, ql < 0]
check('K = 0: exactly 4 light states: E1/2g at +mu and E1/2u at -mu (one particle and one antiparticle doublet of opposite parity)',
      light.sum() == 4 and irr_of(up) == {'E1/2g': 1} and irr_of(dn) == {'E1/2u': 1} and np.allclose(np.sort(ql), [-muL, -muL, muL, muL], atol=1e-9),
      f'light w = {np.round(np.sort(ql), 5)}')
g1 = np.linspace(-np.pi / 4, np.pi / 4, 13); Ks = np.array(list(itertools.product(g1, repeat=3)))
Wz = np.array([np.sort(np.abs(-np.angle(np.linalg.eigvals(tick(K, c0, m0))))) for K in Ks])
far = np.linalg.norm(Ks, axis=1) > 0.3
check('whole zone (13^3 grid): 4 light bands below 0.7; the other 60 stay >= 1.0 from both w = 0 and w = pi; light bands >= 0.1 from 0 for |K| > 0.3',
      Wz[:, 4].min() > 1.0 and (np.pi - Wz[:, -1]).min() > 1.0 and Wz[far, 0].min() > 0.1 and Wz[:, 3].max() < 0.7,
      f'heavy min |w| {Wz[:, 4].min():.3f}, min(pi-|w|) {(np.pi - Wz[:, -1]).min():.3f}, light far min {Wz[far, 0].min():.3f}, light max {Wz[:, 3].max():.3f}')
rng = np.random.default_rng(1); Kr = rng.uniform(-np.pi / 4, np.pi / 4, (600, 3))
Wr = np.array([np.sort(np.abs(-np.angle(np.linalg.eigvals(tick(K, c0, m0))))) for K in Kr])
farr = np.linalg.norm(Kr, axis=1) > 0.3
check('600 random zone points: same light content (4 bands below 0.7, the rest >= 1.0 from 0 and pi, light >= 0.1 from 0 for |K| > 0.3)',
      Wr[:, 3].max() < 0.7 and Wr[:, 4].min() > 1.0 and (np.pi - Wr[:, -1]).min() > 1.0 and Wr[farr, 0].min() > 0.1)
# Dirac form and isotropy
dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
def light_w(K):
    w = -np.angle(np.linalg.eigvals(tick(K, c0, m0))); return np.sort(w[np.abs(w) < 0.5])
def light_w(K):
    w = -np.angle(np.linalg.eigvals(tick(K, c0, m0))); return np.sort(w[np.abs(w) < 0.7])
ks = (0.004, 0.008, 0.016); vals = {k: np.array([light_w(k * d) for d in dirs]) for k in ks}
# fit w_+ = e2 k^2 + sqrt(mu^2 + v^2 k^2), w_- = e2 k^2 - sqrt(...): e2 from the sum, v from the difference
e2 = np.mean([(vals[k][:, 3] + vals[k][:, 0]) / 2 / k ** 2 for k in ks])
v2 = np.mean(((vals[ks[0]][:, 3] - vals[ks[0]][:, 0]) / 2) ** 2 - muL ** 2) / ks[0] ** 2; v = np.sqrt(v2)
dev = max(np.abs((vals[k][:, 3] - vals[k][:, 0]) / 2 - np.sqrt(muL ** 2 + v2 * k ** 2)).max() / np.sqrt(muL ** 2 + v2 * k ** 2) for k in ks)
spread = max(np.ptp(vals[k][:, 3]) / vals[k][:, 3].mean() for k in ks)
split = max(np.abs(vals[k][:, 3] - vals[k][:, 2]).max() + np.abs(vals[k][:, 1] - vals[k][:, 0]).max() for k in ks)
check('Dirac band: w = e2 k^2 +- sqrt(mu^2 + v^2 k^2) within 0.2% for |k| <= 0.016, each sign twofold, direction spread < 0.2%',
      dev < 2e-3 and spread < 2e-3 and split < 1e-10, f'v = {v:.4f} sites per tick, e2 = {e2:.3f}; dev {dev:.1e}, spread {spread:.1e}, spin split {split:.1e}')
check('the k^2 offset is non-relativistically negligible: 2 mu e2 / v^2 << 1 (it vanishes as mu -> 0)', abs(2 * muL * e2 / v2) < 0.05, f'{2 * muL * e2 / v2:.3f}')
# massless limit closes only at Gamma
c1, m1 = c0, m0 - muL
Wm = np.array([np.sort(np.abs(-np.angle(np.linalg.eigvals(tick(K, c1, m1))))) for K in Ks])
check('mu -> 0 (shift m0 by -mu): gap closes at K = 0 only (4 states at w = 0); away from K = 0 the light bands stay >= 0.1 from 0',
      Wm[np.argmin(np.linalg.norm(Ks, axis=1)), 3] < 1e-6 and Wm[far, 0].min() > 0.1, f'K=0 max light |w| {Wm[np.argmin(np.linalg.norm(Ks, axis=1)), 3]:.1e}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
