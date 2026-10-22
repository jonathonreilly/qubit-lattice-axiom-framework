#!/usr/bin/env python3
"""One light Dirac copy on 4^3 cells (onecopy-verify).

 1  copy count on 2^3 cubes: content of every spinorial site action, tensor facts, star sizes;
 2  E1/2g multiplicity of L^3 cells is even (L = 2, 4, 6);
 3  CL-2's spin-3/2 reflection W on the 2^3 cubes nested in a 4^3 block: covariance, odd under one inversion action;
 4  the CL-2-type opposite-step glide on 4^3 cells cannot hold one copy;
 5  the W-glide (odd half-tick = (2,2,2)-translate of W V W) makes the light pair massless for every block unitary V;
 6  doubling: that protection and a w -> -w symmetry cannot coexist with one copy;
 7  a protected tick P: massless without tuning, particle-hole asymmetric (c != 0), not gapped; c tuned to 0 is not gapped either;
 8  a particle-hole-symmetric tick S: real-space covariance, exact w -> -w, one Dirac copy, certified light count over the zone;
 9  the other-cells tuned tick: one copy certified over the zone, but no w -> -w symmetry and c != 0;
10  estimates of the resulting particle-antiparticle dispersion splitting against measured bounds.
Supplied model, finite diagnostic; no physical identification.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/ONE_LIGHT_DIRAC_COPY_ON_FOUR_CUBED_BLOCKS_AND_THE_PROTECTION_PARTICLE_HOLE_TRADE_OFF_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
from math import comb
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1'); os.environ.setdefault('OMP_NUM_THREADS', '1')
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm

T_START = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ============================================================ double groups O' and O_h' (inversion central, I^2 = 1)
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([w1*w2 - x1*x2 - y1*y2 - z1*z2, w1*x2 + x1*w2 + y1*z2 - z1*y2, w1*y2 - x1*z2 + y1*w2 + z1*x2, w1*z2 + x1*y2 - y1*x2 + z1*w2])
def qkey(q): return tuple(np.round(q, 8) + 0.0)
def binary_octahedral():
    r2 = np.sqrt(0.5); gens = [np.array([r2, 0, 0, r2]), np.array([0.5, 0.5, 0.5, 0.5])]
    els = {qkey(np.array([1., 0, 0, 0])): np.array([1., 0, 0, 0])}; fr = list(els.values())
    while fr:
        new = []
        for a in fr:
            for g in gens:
                c = qmul(a, g)
                if qkey(c) not in els: els[qkey(c)] = c; new.append(c)
        fr = new
    return list(els.values())
def q_su2(q): w, x, y, z = q; return np.array([[w - 1j*z, -1j*x - y], [-1j*x + y, w + 1j*z]])
def q_so3(q):
    w, x, y, z = q
    return np.array([[1 - 2*(y*y + z*z), 2*(x*y - z*w), 2*(x*z + y*w)], [2*(x*y + z*w), 1 - 2*(x*x + z*z), 2*(y*z - x*w)], [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x*x + y*y)]])
class DG:
    def __init__(self, with_inv):
        Q = binary_octahedral(); self.el = [(q, e) for e in ((0, 1) if with_inv else (0,)) for q in Q]; self.n = len(self.el)
        self.U = [q_su2(q) for q, e in self.el]; self.Rp = [np.round(q_so3(q)) for q, e in self.el]
        self.R = [Rp * (-1) ** e for Rp, (q, e) in zip(self.Rp, self.el)]; self.par = np.array([e for q, e in self.el])
        ix = {(qkey(q), e): i for i, (q, e) in enumerate(self.el)}
        self.mul = np.array([[ix[(qkey(qmul(a[0], b[0])), (a[1] + b[1]) % 2)] for b in self.el] for a in self.el])
        self.e = ix[(qkey(np.array([1., 0, 0, 0])), 0)]; self.m1 = ix[(qkey(np.array([-1., 0, 0, 0])), 0)]
        self.inv = np.array([int(np.where(self.mul[i] == self.e)[0][0]) for i in range(self.n)])
        t = np.array([np.trace(u).real for u in self.U]); a2 = np.array([round(np.linalg.det(np.abs(R))) for R in self.Rp])
        trR = np.array([np.trace(R) for R in self.Rp]); trR2 = np.array([np.trace(R @ R) for R in self.Rp])
        base = {'E1/2': t + 0j, 'E5/2': t * a2 + 0j, 'G3/2': t ** 3 - 2 * t + 0j}
        self.irr = {}
        for k, v in base.items():
            if with_inv: self.irr[k + 'g'] = v.copy(); self.irr[k + 'u'] = v * (-1.0) ** self.par
            else: self.irr[k] = v
        self.gen = {'A1': np.ones(self.n), 'T1': trR, 'E': (trR ** 2 + trR2) / 2 - 1 - trR * a2}
        self.dim = {k: int(round(v[self.e].real)) for k, v in self.irr.items()}
    def mult(self, ch, ref): return np.vdot(ref, ch) / self.n
    def decompose(self, ch): return {k: int(round(self.mult(ch, v).real)) for k, v in self.irr.items() if abs(self.mult(ch, v)) > 1e-7}
    def chars1(self, H):
        """all spinorial 1-dim characters (chi(-1) = -1) of the subgroup H."""
        H = list(H); Hs = set(H); order = {}
        for h in H:
            k, a = 1, h
            while a != self.e: a = self.mul[a, h]; k += 1
            order[h] = k
        gens, span = [], {self.e}
        for h in sorted(H, key=lambda h: -order[h]):
            if h in span: continue
            gens.append(h); span = {self.e}; fr = [self.e]
            while fr:
                nf = []
                for a in fr:
                    for g in gens:
                        b = self.mul[a, g]
                        if b not in span: span.add(b); nf.append(b)
                fr = nf
        out = []
        for ks in itertools.product(*[range(order[g]) for g in gens]):
            val = {self.e: 1.0 + 0j}; fr = [self.e]; ok = True; gv = [np.exp(2j * np.pi * k / order[g]) for k, g in zip(ks, gens)]
            while fr and ok:
                nf = []
                for a in fr:
                    for g, v in zip(gens, gv):
                        b = self.mul[a, g]; c = val[a] * v
                        if b in val:
                            if abs(val[b] - c) > 1e-9: ok = False; break
                        else: val[b] = c; nf.append(b)
                    if not ok: break
                fr = nf
            if ok and abs(val[self.m1] + 1) < 1e-9: out.append(val)
        return out
class Cell:
    """L^3 cell of Z^3 (cosets mod L Z^3), point group about the block centre p = ((L-1)/2)(1,1,1); monomial site actions."""
    def __init__(self, G, L):
        self.G, self.L = G, L; self.p = np.full(3, (L - 1) / 2.0)
        self.pos = np.array(list(itertools.product(range(L), repeat=3)), dtype=float); self.N = len(self.pos)
        idx = {tuple(int(v) for v in x): i for i, x in enumerate(self.pos)}; self.img = np.zeros((G.n, self.N), int)
        for g in range(G.n):
            y = np.round((G.R[g] @ (self.pos - self.p).T).T + self.p).astype(int) % L; self.img[g] = [idx[tuple(v)] for v in y]
        seen, self.orbits = set(), []
        for i in range(self.N):
            if i in seen: continue
            orb = sorted(set(self.img[:, i])); seen |= set(orb); H = [g for g in range(G.n) if self.img[g, i] == i]
            self.orbits.append(dict(rep=i, sites=orb, H=H, chis=G.chars1(H)))
    def site_action(self, choice):
        G = self.G; phi = np.zeros((G.n, self.N), complex)
        for o, c in zip(self.orbits, choice):
            chi = o['chis'][c]; r = o['rep']; trep = {}
            for g in range(G.n): trep.setdefault(self.img[g, r], g)
            for g in range(G.n):
                for s in o['sites']: phi[g, s] = chi[G.mul[G.inv[trep[self.img[g, s]]], G.mul[g, trep[s]]]]
        return phi
    def char(self, phi, K):
        G = self.G; ch = np.zeros(G.n, complex)
        for g in range(G.n):
            fx = np.where(self.img[g] == np.arange(self.N))[0]; Gv = G.R[g] @ K - K
            ch[g] = np.sum(phi[g, fx] * np.exp(1j * (self.pos[fx] - self.p) @ Gv))
        return ch
    def rep_err(self, phi):
        G = self.G
        return max(np.abs(phi[G.mul[g, h]] - phi[g, self.img[h]] * phi[h]).max() for g in range(0, G.n, 3) for h in range(G.n))

# ============================================================ 1. copy count on 2^3 cubes
print('== 1. 2^3 cubes: every spinorial site action')
cont = {}
for wi in (False, True):
    G = DG(wi); C = Cell(G, 2); res = set()
    for ch in itertools.product(*[range(len(o['chis'])) for o in C.orbits]):
        phi = C.site_action(list(ch)); assert C.rep_err(phi) < 1e-12
        res.add(tuple(tuple(sorted(G.decompose(C.char(phi, K)).items())) for K in (np.zeros(3), np.full(3, np.pi / 2))))
    cont[wi] = res
GO, GH = DG(False), DG(True)
okH = cont[True] == {((('G3/2g', 1), ('G3/2u', 1)), (('G3/2g', 1), ('G3/2u', 1)))}
okO = cont[False] == {((('G3/2', 2),), (('G3/2', 2),)), ((('E1/2', 1), ('E5/2', 1), ('G3/2', 1)), (('E1/2', 1), ('E5/2', 1), ('G3/2', 1)))}
check("with inversion, every site action gives G3/2g+G3/2u at both invariant momenta (no E1/2, no E5/2)", okH)
check("rotations only: spin-3/2 corner gives 2 G3/2; the m=+-1/2 corners give E1/2+E5/2+G3/2 (one E1/2 only)", okO)
mA1 = lambda a, b: GO.mult(GO.irr[a] * np.conj(GO.irr[b]), GO.gen['A1']).real
mT1 = lambda a, b: GO.mult(GO.irr[a] * np.conj(GO.irr[b]), GO.gen['T1']).real
check("tensor facts: E1/2 x E1/2 holds A1 and T1 (mass, k-linear term); E1/2 x E5/2 holds neither; G3/2 = E1/2 x E",
      np.isclose(mA1('E1/2', 'E1/2'), 1) and np.isclose(mT1('E1/2', 'E1/2'), 1) and abs(mA1('E1/2', 'E5/2')) < 1e-9 and abs(mT1('E1/2', 'E5/2')) < 1e-9
      and np.allclose(GO.irr['G3/2'], GO.irr['E1/2'] * GO.gen['E']))
Kg = np.array(list(itertools.product(range(8), repeat=3))) * np.pi / 8   # 2Z^3 zone: K mod pi
sizes = []
for K in Kg:
    st = {tuple(np.round((R @ K) / np.pi * 8).astype(int) % 8) for R in GO.R}; sizes.append(len(st))
sizes = np.array(sizes)
check("2Z^3 zone: every non-invariant momentum has a star of at least 3 points (only Gamma and R are fixed)",
      sizes[sizes > 1].min() == 3 and np.sum(sizes == 1) == 2, f'star sizes {sorted(set(sizes.tolist()))}')
print('   => on 2^3 cubes a light Dirac needs two copies (Gamma/R) or a star of >= 3, for every covariant block unitary')

# ============================================================ 2. E1/2g multiplicity of L^3 cells
print('== 2. E1/2g multiplicity (inversion included)')
m_e12 = {}
for L in (2, 4, 6):
    C = Cell(GH, L); chs = [[0] * len(C.orbits)] if L == 6 else list(itertools.product(*[range(len(o['chis'])) for o in C.orbits]))
    m_e12[L] = sorted({GH.decompose(C.char(C.site_action(list(c)), np.zeros(3))).get('E1/2g', 0) for c in chs})
check("E1/2g multiplicity at Gamma = m(m-1) + 2 C(m,3) for L = 2m: 0, 2, 8 (always even)",
      m_e12 == {2: [0], 4: [2], 6: [8]} and all(m * (m - 1) + 2 * comb(m, 3) == {1: 0, 2: 2, 3: 8}[m] for m in (1, 2, 3)), str(m_e12))

# ============================================================ 3. spin-3/2 gauge on the 4^3 cell; CL-2's W
print("== 3. 4^3 cell in CL-2's spin-3/2 gauge")
CORN = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J32 = Jm(1.5); SIG = Jm(0.5)
XI = []
for c in CORN:
    n = (2 * c - 1.0) / np.sqrt(3); w, v = np.linalg.eigh(sum(n[k] * J32[k] for k in range(3))); XI.append(v[:, -1])
W8 = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.abs(CORN[a] - CORN[b]).sum() == 1: g = XI[a].conj() @ XI[b]; W8[a, b] = -g / abs(g) / np.sqrt(3)
L4, N = 4, 64
SITES = np.array(list(itertools.product(range(L4), repeat=3))); IDX = {tuple(x): i for i, x in enumerate(SITES)}
RES = (SITES % 2) @ [4, 2, 1]; P0 = np.full(3, 1.5); Id = np.eye(N)
WA = np.zeros((N, N), complex)
for b0 in itertools.product((0, 2), repeat=3):
    ids = [IDX[tuple(np.array(b0) + c)] for c in CORN]; WA[np.ix_(ids, ids)] = W8[np.ix_(RES[ids], RES[ids])]
ROT = [R for R in GO.Rp[:48]]
LIFT = []
for q in binary_octahedral():
    R = np.round(q_so3(q)); w0, x, y, z = q; ang = 2 * np.arccos(np.clip(w0, -1, 1)); sn = np.sqrt(max(1 - w0 * w0, 0))
    nvec = np.array([x, y, z]) / sn if sn > 1e-12 else np.array([0, 0, 1.0])
    LIFT.append((R, q_su2(q), expm(-1j * ang * sum(nvec[k] * J32[k] for k in range(3)))))
def site_rot(R, D, L=L4, sites=SITES, idx=IDX, cen=P0):
    n = len(sites); Gm = np.zeros((n, n), complex)
    for i, x in enumerate(sites):
        y = np.rint(R @ (x - cen) + cen).astype(int) % L
        Gm[idx[tuple(y)], i] = XI[int((y % 2) @ [4, 2, 1])].conj() @ D @ XI[int((x % 2) @ [4, 2, 1])]
    return Gm
GROT = [site_rot(R, D) for R, U, D in LIFT]
T0 = np.zeros((N, N))
for i, x in enumerate(SITES): T0[IDX[tuple((x + 2) % 4)], i] = 1
ORB = {}
for i, x in enumerate(SITES): ORB.setdefault(tuple(np.sort(np.abs(x - P0))), []).append(i)
PERM_I = [IDX[tuple(3 - x)] for x in SITES]; PI_ = np.zeros((N, N)); PI_[PERM_I, np.arange(N)] = 1
def inversion_actions():
    """central inversions x -> 3-x with I^2 = 1: phases solved orbit by orbit (monomial propagation)."""
    out = []
    keys = list(ORB)
    base = {}
    for kk in keys:
        o = ORB[kk]; r = o[0]; d = {r: 1.0 + 0j}; fr = [r]
        while fr:
            nf = []
            for s_ in fr:
                for Gm in GROT:
                    t = int(np.argmax(np.abs(Gm[:, s_]))); ph = Gm[t, s_]
                    # I G = G I  =>  d[t] = G[I t, I s] d[s] / G[t, s]
                    tI, sI = PERM_I[t], PERM_I[s_]; val = Gm[tI, sI] * d[s_] / ph
                    if t not in d: d[t] = val; nf.append(t)
            fr = nf
        v = np.zeros(N, complex)
        for k_, x_ in d.items(): v[k_] = x_
        c = v[r] * v[PERM_I[r]]; base[kk] = v / np.sqrt(c)
    for sg in itertools.product((1, -1), repeat=len(keys)):
        I = PI_ @ np.diag(sum(s_ * base[k_] for s_, k_ in zip(sg, keys)))
        if np.abs(I @ I - Id).max() < 1e-9 and max(np.abs(I @ Gm - Gm @ I).max() for Gm in GROT) < 1e-9: out.append((sg, I))
    return out
INV = inversion_actions()
odd = [I for sg, I in INV if np.abs(I @ WA + WA @ I).max() < 1e-9 and sg[0] == 1]
even = [I for sg, I in INV if np.abs(I @ WA - WA @ I).max() < 1e-9 and sg[0] == 1]
IP = odd[0]
GALL = GROT + [Gm @ IP for Gm in GROT]
e12 = np.array([np.trace(U) for R, U, D in LIFT]); g32 = np.array([np.trace(D) for R, U, D in LIFT])
e52 = np.array([np.trace(U) * round(np.linalg.det(np.abs(R))) for R, U, D in LIFT])
CHI = {}
for nm, ch in (('E1/2', e12), ('E5/2', e52), ('G3/2', g32)): CHI[nm + 'g'] = np.concatenate([ch, ch]); CHI[nm + 'u'] = np.concatenate([ch, -ch])
def proj(nm): return int(round(CHI[nm][0].real)) / len(GALL) * sum(np.conj(c) * Gm for c, Gm in zip(CHI[nm], GALL))
PR = {nm: proj(nm) for nm in CHI}
def covariant(X): return sum(Gm @ X @ Gm.conj().T for Gm in GALL) / len(GALL)
clos = max(min(np.abs(GALL[a] @ GALL[b] - Gc).max() for Gc in GALL) for a in range(0, 96, 13) for b in range(0, 96, 11))
check("CL-2's W is a reflection; spin-3/2 site phases give the 48 rotation lifts about the 4^3 block centre, which with a"
      " central inversion close into O_h' on 64 sites", np.abs(W8 @ W8 - np.eye(8)).max() < 1e-13 and clos < 1e-12, f'closure {clos:.1e}')
check("W on the cubes of the nested 2^3 tiling commutes with the rotations and the (2,2,2) translation; it is odd under"
      " exactly one central inversion action and even under exactly one (up to sign)",
      max(np.abs(Gm @ WA - WA @ Gm).max() for Gm in GROT) < 1e-13 and np.abs(T0 @ WA - WA @ T0).max() < 1e-15 and len(odd) == 1 and len(even) == 1,
      f'{len(INV)} central involutions')
E_EDGE = np.zeros((N, N)); E_FACE = np.zeros((N, N))
for k_, o in ORB.items():
    if k_ == (0.5, 1.5, 1.5): E_EDGE[o, o] = 1
    if k_ == (0.5, 0.5, 1.5): E_FACE[o, o] = 1
P_EDGE = E_EDGE @ PR['E1/2g']
check("4^3 content: E1/2g and E1/2u twice each (one copy on the edge-centre orbit, one on the face-centre orbit)",
      all(np.isclose(np.trace(PR[nm]).real, d) for nm, d in (('E1/2g', 4), ('E1/2u', 4), ('E5/2g', 4), ('E5/2u', 4), ('G3/2g', 24), ('G3/2u', 24)))
      and np.isclose(np.trace(P_EDGE).real, 2) and np.isclose(np.trace(E_FACE @ PR['E1/2g']).real, 2))
YPOS = np.array([[v if v >= 2 else v + 4 for v in x] for x in SITES]); LAM = (YPOS - SITES).astype(float)
def bloch_odd(Ao, K): ph = np.exp(-1j * (LAM @ K)); return (ph[:, None] * Ao) * ph.conj()[None, :]
def Tk(K):
    Tm = np.zeros((N, N), complex)
    for s_, x in enumerate(SITES):
        src = x - 2; sp = IDX[tuple(src % 4)]; Tm[s_, sp] = np.exp(1j * K @ (src - src % 4))
    return Tm
def levels(U0, P):
    """quasi-energies of U0 restricted to the range of the projector P (P commutes with U0)."""
    w, V = np.linalg.eigh((P + P.conj().T) / 2); B = V[:, w > 0.5]
    return np.sort(-np.angle(np.linalg.eigvals(B.conj().T @ U0 @ B)))
def negclosed(lv):
    """max over levels w of the circular distance from -w to the nearest level (0 iff the set is closed under w -> -w)."""
    lv = np.asarray(lv); return max(min(arcd(-x, y) for y in lv) for x in lv)
def arcd(a, b): return np.abs(np.angle(np.exp(1j * (np.asarray(a) - b))))
rng = np.random.default_rng(20261021)
def rand_cov():
    X = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); H = covariant(X + X.conj().T); return H / np.linalg.norm(H, 2)

def certify(Ufun, Lip, kap, d0, wa, dpi, maxboxes=60000):
    """adaptive boxes over the wedge 0 <= K3 <= K2 <= K1 <= pi/4 (a fundamental domain of O_h on the zone); kappa on a box edge.
    accept a box (centre c, half-width r) if, with rho = sum_i Lip_i r >= ||U(K) - U(c)||:
      dist(-1, spec U(c)) - rho > 2 sin(dpi/2)                          (no state within dpi of pi);
      K1 >= kappa: dist(1, spec U(c)) - rho > 2 sin(d0/2)               (no state within d0 of 0);
      K1 <= kappa: dist(exp(-+i wa), spec U(c)) - rho > 0                (no state crosses |w| = wa)."""
    h0 = np.pi / 4 / 8; s0, spi = 2 * np.sin(d0 / 2), 2 * np.sin(dpi / 2); za, zb = np.exp(-1j * wa), np.exp(1j * wa)
    todo = [(np.array([i, j, l]) * h0 + h0 / 2, h0 / 2) for i in range(8) for j in range(8) for l in range(8)]
    todo = [(c, r) for c, r in todo if (c[0] + r >= c[1] - r) and (c[1] + r >= c[2] - r)]
    nbox = 0; mins = [9.0, 9.0, 9.0]
    while todo:
        c, r = todo.pop(); lam = np.linalg.eigvals(Ufun(c)); rho = Lip.sum() * r; nbox += 1
        mp = np.abs(lam + 1).min() - rho - spi; ok = mp > 0; lo1, hi1 = c[0] - r, c[0] + r
        if lo1 >= kap - 1e-12: m0_ = np.abs(lam - 1).min() - rho - s0; ok = ok and m0_ > 0
        elif hi1 <= kap + 1e-12: m0_ = min(np.abs(lam - za).min(), np.abs(lam - zb).min()) - rho; ok = ok and m0_ > 0
        else: ok = False
        if ok:
            mins[0] = min(mins[0], mp); mins[1 if lo1 >= kap - 1e-12 else 2] = min(mins[1 if lo1 >= kap - 1e-12 else 2], m0_); continue
        if r < 2e-4 or nbox > maxboxes: return False, nbox, mins
        for dd in itertools.product((-0.5, 0.5), repeat=3):
            cc = c + np.array(dd) * r
            if (cc[0] + r / 2 >= cc[1] - r / 2) and (cc[1] + r / 2 >= cc[2] - r / 2): todo.append((cc, r / 2))
    return True, nbox, mins
# ============================================================ 4. the CL-2-type opposite-step glide
print('== 4. opposite-step glide on 4^3 cells (odd half-tick = image of the inverse even one)')
IC = T0 @ IP
trmax = max(abs(np.trace(Gm @ M)) for Gm in GALL for M in (T0, IC))
comm = max(np.abs(Gm @ M - M @ Gm).max() for Gm in GALL for M in (T0, IC))
check("both tiling-exchanging maps (translation by (2,2,2), inversion through (2.5,2.5,2.5)) commute with O_h' at K=0 and"
      " fix no site mod 4, so every trace tr(g M) vanishes", trmax < 1e-12 and comm < 1e-12, f'max|tr| {trmax:.1e}')
symm = 0
for _ in range(3):
    Ve = expm(-0.9j * rand_cov())
    for M in (T0, IC):
        symm = max(symm, negclosed(levels(M @ Ve.conj().T @ M.conj().T @ Ve, PR['E1/2g'])))
check("random covariant blocks: the two E1/2g levels at Gamma are always {w, -w}, so one light copy brings a second light"
      " copy or a copy at pi", symm < 1e-9, f'max asym {symm:.1e}')

# ============================================================ 5. W-glide protection
print('== 5. W-glide: odd half-tick = (2,2,2)-translate of W V W')
TW = T0 @ WA; err_c = err_s = deg = 0
for _ in range(3):
    Ve = expm(-1j * rand_cov() * rng.uniform(0.5, 2)); Ao = TW @ Ve @ TW.conj().T
    for K in rng.uniform(-1, 1, (3, 3)):
        Uk = bloch_odd(Ao, K) @ Ve; Sk = Tk(K) @ WA @ Ve
        err_c = max(err_c, np.abs(Sk @ Uk - Uk @ Sk).max()); err_s = max(err_s, np.abs(Sk @ Sk - np.exp(-4j * K.sum()) * Uk).max())
    U0 = Ao @ Ve
    for nm in ('E1/2', 'E5/2', 'G3/2'): deg = max(deg, np.abs(levels(U0, PR[nm + 'g']) - levels(U0, PR[nm + 'u'])).max())
check("for every covariant block unitary V: Sigma = T_(2,2,2) W V commutes with U(K) and Sigma^2 = exp(-4iK.(1,1,1)) U(K)",
      err_c < 1e-12 and err_s < 1e-12, f'{err_c:.1e}, {err_s:.1e}')
check("Sigma(0) anticommutes with the inversion, so every Gamma level is a g/u pair: E1/2g and E1/2u levels coincide (no tuning)",
      deg < 1e-10 and np.abs((WA @ IP + IP @ WA)).max() < 1e-12, f'max |w_g - w_u| {deg:.1e} over 3 random blocks')
def tickP(Pa, e, f, mu=0.0):
    Pb = TW @ Pa @ TW.conj().T; Q = Id - Pa - Pb
    Ve = np.exp(-1j * (e - mu / 2)) * Pa + np.exp(1j * (e - mu / 2)) * Pb + np.exp(-1j * f) * Q
    Vp = np.exp(-1j * (e + mu / 2)) * Pa + np.exp(1j * (e + mu / 2)) * Pb + np.exp(-1j * f) * Q
    return Ve, TW @ Vp @ TW.conj().T
eP, fP = 7 * np.pi / 12, np.pi / 12
Ve, Ao = tickP(P_EDGE, eP, fP, mu=0.05); lm = np.sort(levels(Ao @ Ve, PR['E1/2g'] + PR['E1/2u']))
pert = 0
for _ in range(2):
    Ve2, Ao2 = tickP(P_EDGE, eP, fP); Ve2 = Ve2 @ expm(-0.1j * rand_cov()); Ao2 = TW @ Ve2 @ TW.conj().T
    pert = max(pert, np.abs(levels(Ao2 @ Ve2, PR['E1/2g']) - levels(Ao2 @ Ve2, PR['E1/2u'])).max())
check("mass from the step asymmetry e -+ mu/2 (breaks Sigma): light levels +-mu; covariant perturbations that keep the glide"
      " keep the light pair degenerate", np.allclose(lm[np.abs(lm) < 0.3], [-0.05, -0.05, 0.05, 0.05], atol=1e-12) and pert < 1e-10, f'{pert:.1e}')

# ============================================================ 6. doubling: protection versus w -> -w
print('== 6. doubling: protection and a w -> -w symmetry')
sym6 = 0
for _ in range(3):
    X = rand_cov(); H = (X - WA @ X @ WA) / 2; Ve = expm(-1j * H / np.linalg.norm(H, 2)); Ao = TW @ Ve @ TW.conj().T
    lg = levels(Ao @ Ve, PR['E1/2g']); lu = levels(Ao @ Ve, PR['E1/2u'])
    sym6 = max(sym6, negclosed(lg), np.abs(lg - lu).max())
check("glide + W-odd generator (both symmetries): the E1/2 Dirac points at Gamma sit at {w, -w}; a single light copy is impossible",
      sym6 < 1e-9, f'{sym6:.1e}')
print('   theorem: Sigma gives {w_g} = {w_u}, a w -> -w map gives {w_g} = -{w_u} or -{w_g}; with even E1/2g multiplicity'
      ' (section 2) a second E1/2 pair sits at 0 or pi')

# ============================================================ 7. protected tick P
print('== 7. protected tick P: V = e^-ie P + e^ie (TW)P(TW)^-1 + e^-i phi Q (edge copy, e = 7pi/12, phi = pi/12)')
gq = np.linspace(0, np.pi / 4, 6); KW = np.array([k for k in itertools.product(gq, gq, gq) if k[0] >= k[1] >= k[2]])
KWo = KW[np.linalg.norm(KW, axis=1) > 0.3]
dirs = np.array([[1, 2, 3.], [3, -1, 2], [-2, 1, 1.5]]); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
def cone(Lm, Ao, Rm, k=2e-3):
    vs, cs = [], []
    for d in dirs:
        q = -np.angle(np.linalg.eigvals(Lm @ bloch_odd(Ao, k * d) @ Rm)); l = np.sort(q[np.argsort(np.abs(q))[:4]])
        vs.append((l[3] - l[0]) / (2 * k)); cs.append(l.sum() / 2 / (2 * k * k))
    return np.mean(vs), np.ptp(vs), np.mean(cs)
def grid_gap(Lm, Ao, Rm):
    a = np.abs(-np.angle(np.linalg.eigvals(np.array([Lm @ bloch_odd(Ao, K) @ Rm for K in KWo])))); return a.min(), (np.pi - a).min()
Ve, Ao = tickP(P_EDGE, eP, fP); vP, spP, cP = cone(Id, Ao, Ve); gP0, gPpi = grid_gap(Id, Ao, Ve)
q0 = -np.angle(np.linalg.eigvals(Ao @ Ve))
check("P: 4 light states at Gamma (massless with no tuning), 60 at 2 phi; isotropic Dirac cone",
      int(np.sum(np.abs(q0) < 1e-9)) == 4 and int(np.sum(arcd(q0, 2 * fP) < 1e-9)) == 60 and spP < 1e-5, f'v {vP:.3f}')
check("P: no w -> -w symmetry (Gamma spectrum {0, 2phi}); the cone is particle-hole asymmetric, w+ + w- = 2 c k^2 with c != 0",
      abs(cP) > 1, f'c = {cP:+.2f} (lattice units)')

from scipy.optimize import minimize_scalar
dP = np.array([1, 1, 0.]) / np.sqrt(2)
zb = minimize_scalar(lambda x: np.abs(-np.angle(np.linalg.eigvals(bloch_odd(Ao, x * dP) @ Ve))).min(), bounds=(0.08, 0.3), method='bounded', options=dict(xatol=1e-10))
check("P is not gapped: the strongly bent cone returns to w = 0 near |K| = v/|c| (zero found along (1,1,0))",
      zb.fun < 1e-6, f'|w| = {zb.fun:.1e} at |K| = {zb.x:.4f}; v/|c| = {vP / abs(cP):.4f}')
from scipy.optimize import brentq, minimize
ve_ = np.linalg.eigh(P_EDGE)[1][:, -1]; a_p = (ve_ + T0 @ ve_) / np.sqrt(2); a_m = (ve_ - T0 @ ve_) / np.sqrt(2)
def copyT(th, ph):
    v = np.cos(th) * a_p + np.exp(1j * ph) * np.sin(th) * a_m; S_ = np.array([Gm @ v for Gm in GALL]).T; u_, sv_, _ = np.linalg.svd(S_); return u_[:, :2] @ u_[:, :2].conj().T
PG = PR['G3/2g'] + PR['G3/2u']; Pa0 = copyT(1.0, 2.0)
def tickP2(f1, e=2.0, f2=-np.pi / 6):
    Pb = TW @ Pa0 @ TW.conj().T; Q = Id - Pa0 - Pb
    V_ = np.exp(-1j * e) * Pa0 + np.exp(1j * e) * Pb + np.exp(-1j * f1) * (Q - PG) + np.exp(-1j * f2) * PG; return V_, TW @ V_ @ TW.conj().T
def c_of(f1):
    V_, A_ = tickP2(f1); k_ = 3e-3; q = -np.angle(np.linalg.eigvals(bloch_odd(A_, k_ * dirs[0]) @ V_)); l = np.sort(q[np.argsort(np.abs(q))[:4]]); return l.sum() / 2 / (2 * k_ * k_)
fr = np.linspace(0.02, 1.5, 40); cv = [c_of(x) for x in fr]
f1c = brentq(c_of, *[(fr[i], fr[i + 1]) for i in range(39) if np.sign(cv[i]) != np.sign(cv[i + 1]) and max(abs(cv[i]), abs(cv[i + 1])) < 50][0], xtol=1e-12)
V2, A2_ = tickP2(f1c)
fz = lambda K: np.abs(-np.angle(np.linalg.eigvals(bloch_odd(A2_, K) @ V2))).min() / max(np.linalg.norm(K), 1e-3) if np.linalg.norm(K) > 0.01 else 9
gz = np.linspace(0.02, np.pi / 4, 9); KK = np.array([k_ for k_ in itertools.product(gz, gz, gz) if k_[0] >= k_[1] >= k_[2]])
vz = np.array([fz(K) for K in KK])
rz = min((minimize(fz, KK[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=900)) for i in np.argsort(vz)[:3]), key=lambda r: r.fun)
wz = np.abs(-np.angle(np.linalg.eigvals(bloch_odd(A2_, rz.x) @ V2))).min()
check("tuning c to 0 inside the glide class (second heavy phase on G3/2) opens light-level states elsewhere: an exact zero off Gamma",
      wz < 1e-8 and np.linalg.norm(rz.x) > 0.2, f'c = {c_of(f1c):+.0e} at f1 = {f1c:.4f}; |w| = {wz:.0e} at K = {np.round(rz.x, 3).tolist()}')
# ============================================================ 8. particle-hole tick S
print('== 8. particle-hole tick S: every block applies exp(-i[s e B + phi_s I Q]), light step sign s alternating')
RT = (Id + 1j * T0) / np.sqrt(2); P_CIRC = RT @ P_EDGE @ RT.conj().T
eS, feS, foS = np.pi / 3, np.pi / 2, np.pi / 6
def tickS(Pa, e=eS, fe=feS, fo=foS, mu=0.0, extra=None):
    Pb = WA @ Pa @ WA; Q = Id - Pa - Pb; B = Pa - Pb
    He = (e - mu / 2) * B + fe * IP @ Q + (0 if extra is None else extra); Ho = -(e + mu / 2) * B + fo * IP @ Q
    return expm(-0.5j * He), expm(-1j * Ho)
Vh, Ao = tickS(P_CIRC)
q0 = -np.angle(np.linalg.eigvals(Vh @ Ao @ Vh))
lev = levels(Vh @ Ao @ Vh, PR['E1/2g'] + PR['E1/2u'])
check("S: light copy P = (1+iT)/sqrt2 on the edge copy, B = P - WPW; Gamma: 4 light states (E1/2g + E1/2u), 30 at +2pi/3,"
      " 30 at -2pi/3", int(np.sum(np.abs(q0) < 1e-9)) == 4 and int(np.sum(arcd(q0, 2 * np.pi / 3) < 1e-9)) == 30
      and int(np.sum(arcd(q0, -2 * np.pi / 3) < 1e-9)) == 30 and np.sum(np.abs(lev) < 1e-9) == 4)
sw = max(np.abs(WA @ (Vh @ bloch_odd(Ao, K) @ Vh) @ WA - (Vh @ bloch_odd(Ao, K) @ Vh).conj().T).max() for K in rng.uniform(-1, 1, (4, 3)))
check("S: W is an exact Floquet chiral symmetry, W U(K) W = U(K)^-1 (spectrum symmetric under w -> -w at every K)", sw < 1e-12, f'{sw:.1e}')
# real space: 8^3 torus
L8 = 8; S8 = np.array(list(itertools.product(range(L8), repeat=3))); I8 = {tuple(x): i for i, x in enumerate(S8)}; N8 = 512
def embed(B64, origin):
    M = np.zeros((N8, N8), complex); ids = [I8[tuple((x + origin) % L8)] for x in SITES]
    cs = [IDX[tuple((x + origin) % 4)] for x in SITES]; M[np.ix_(ids, ids)] = B64[np.ix_(cs, cs)]; return M
def layer(B64, off): return sum(embed(B64, np.array(o) + off) for o in itertools.product((0, 4), repeat=3))
Ur = layer(Vh, 0) @ layer(Ao, 2) @ layer(Vh, 0)
gensR = [(R, D) for R, U, D in LIFT if (np.allclose(R, [[0, -1, 0], [1, 0, 0], [0, 0, 1]]) or np.allclose(R, [[0, 0, 1], [1, 0, 0], [0, 1, 0]]))]
Gr = [site_rot(R, D, L=L8, sites=S8, idx=I8) for R, D in gensR]
Ir = np.zeros((N8, N8), complex); dI = np.array([IP[PERM_I[i], i] for i in range(N)])
for i, x in enumerate(S8): Ir[I8[tuple((3 - x) % L8)], i] = dI[IDX[tuple(x % 4)]]
T4 = np.zeros((N8, N8))
for i, x in enumerate(S8): T4[I8[((x[0] + 4) % 8, x[1], x[2])], i] = 1
WAr = layer(WA, 0)
cv = max(np.abs(M @ Ur - Ur @ M).max() for M in Gr + [Ir, T4])
wb = np.sort(np.concatenate([-np.angle(np.linalg.eigvals(Vh @ bloch_odd(Ao, np.pi / 4 * np.array(c, float)) @ Vh)) for c in itertools.product((0, 1), repeat=3)]))
wr = np.sort(-np.angle(np.linalg.eigvals(Ur)))
check("S on the 8^3 torus: unitary, commutes with the C4 and C3 lifts, the inversion and the translation by 4; W U W = U^-1;"
      " Bloch gives all 512 quasi-energies",
      np.abs(Ur @ Ur.conj().T - np.eye(N8)).max() < 1e-12 and cv < 1e-12 and np.abs(WAr @ Ur @ WAr - Ur.conj().T).max() < 1e-12 and np.abs(wr - wb).max() < 1e-9,
      f'cov {cv:.1e}, spec {np.abs(wr - wb).max():.1e}')
vS, spS, cS = cone(Vh, Ao, Vh); k = 0.02
om = np.array([np.sort(np.abs(-np.angle(np.linalg.eigvals(Vh @ bloch_odd(Ao, k * d) @ Vh))))[:4] for d in dirs])
Vm, Aom = tickS(P_CIRC, mu=0.04); qm = levels(Vm @ Aom @ Vm, PR['E1/2g'] + PR['E1/2u'])
check("S: isotropic Dirac cone, each sign twofold, c = 0 exactly; mass from the light-step asymmetry: Gamma levels +-mu",
      spS < 1e-6 and abs(cS) < 1e-6 and np.ptp(om) / om.mean() < 1e-3 and np.allclose(np.sort(qm[np.abs(qm) < 0.3]), [-.04, -.04, .04, .04], atol=1e-12),
      f'v {vS:.4f} sites/tick, c {cS:+.1e}')
rat = []
for e_, fe_, fo_ in ((np.pi / 4, np.pi / 2, np.pi / 6), (1.2, np.pi / 2, np.pi / 6), (np.pi / 3, np.pi / 2, 0.0), (np.pi / 3, 2 * np.pi / 3, np.pi / 6)):
    Vh_, Ao_ = tickS(P_CIRC, e=e_, fe=fe_, fo=fo_); rat.append(cone(Vh_, Ao_, Vh_)[0] / (4 * np.sin(e_) / np.sqrt(3)))
check("S cone speed = sin(eps)/sqrt3 blocks per tick (CL-2's formula with the 4^3 block), independent of the heavy phases",
      np.abs(np.array(rat) - 1).max() < 1e-4, f'ratios {np.round(rat, 6).tolist()}')
Xp = rand_cov(); Vp_, Ap_ = tickS(P_CIRC, extra=0.05 * (Xp - WA @ Xp @ WA) / 2)
pertS = np.abs(levels(Vp_ @ Ap_ @ Vp_, PR['E1/2g'])).min()
swp = np.abs(WA @ (Vp_ @ Ap_ @ Vp_) @ WA - (Vp_ @ Ap_ @ Vp_).conj().T).max()
check("S is not protected: a small covariant W-odd term in the even generator keeps W U W = U^-1 but moves the light pair off 0"
      " (its zero is exact only in this form)", pertS > 1e-4 and swp < 1e-12, f'shift {pertS:.1e}')
# ---- certified light count: Lipschitz bound ||dU/dK_i|| = ||[Lambda_i, A_o]|| (K independent)
Lip = np.array([np.linalg.norm(np.diag(LAM[:, i]) @ Ao - Ao @ np.diag(LAM[:, i]), 2) for i in range(3)]) * (1 + 1e-9)
okc, nb, mns = certify(lambda K: Vh @ bloch_odd(Ao, K) @ Vh, Lip, np.pi / 32, 0.12, 0.5, 0.35)
cnt0 = int(np.sum(np.abs(-np.angle(np.linalg.eigvals(Vh @ Ao @ Vh))) < 0.5))
def hausd(a, b): return max(np.abs(a[:, None] - b[None, :]).min(1).max(), np.abs(b[:, None] - a[None, :]).min(1).max())
covK = max(hausd(np.linalg.eigvals(Vh @ bloch_odd(Ao, R @ Kt) @ Vh), np.linalg.eigvals(Vh @ bloch_odd(Ao, Kt) @ Vh))
           for R in GH.R[::5] for Kt in rng.uniform(-0.7, 0.7, (2, 3)))
check("S certified over the zone (Lipschitz boxes on the O_h wedge): nothing within 0.35 of pi; for |K|_inf >= pi/32 nothing"
      " within 0.12 of 0; for |K|_inf <= pi/32 exactly 4 states with |w| < 0.5",
      okc and cnt0 == 4 and covK < 1e-10, f'{okc}: {nb} boxes, ||dU/dK_i|| <= {Lip[0]:.3f}, margins {min(mns):.3f}, O_h spectra {covK:.0e}')

# ============================================================ 9. the other-cells tuned tick
print('== 9. the other-cells tuned tick (induced site action, edge-orbit E1/2 pair, (1,0,2) imaginary odd hop, t = 0.4)')
C4 = Cell(GH, 4); phi4 = C4.site_action([0] * len(C4.orbits)); MG = []
for g in range(GH.n):
    M_ = np.zeros((N, N), complex); M_[C4.img[g], np.arange(N)] = phi4[g]; MG.append(M_)
pos4 = C4.pos.astype(int); idx4 = {tuple(x): i for i, x in enumerate(pos4)}
proj4 = lambda nm: GH.dim[nm] / GH.n * sum(np.conj(GH.irr[nm][g]) * MG[g] for g in range(GH.n))
E4 = np.diag([1.0 if tuple(sorted(np.abs(x - 1.5))) == (0.5, 1.5, 1.5) else 0.0 for x in pos4])
Pg4, Pu4 = E4 @ proj4('E1/2g') @ E4, E4 @ proj4('E1/2u') @ E4; Pl4 = Pg4 + Pu4
LAM4 = np.array([[4 if v < 2 else 0 for v in x] for x in pos4], float)
M0 = np.zeros((N, N), complex); ia, ib = idx4[(2, 3, 3)], idx4[(3, 3, 1)]; M0[ia, ib] = 1j; M0[ib, ia] = -1j
h4 = sum(M_ @ M0 @ M_.conj().T for M_ in MG) / GH.n; h4 /= np.abs(np.linalg.eigvalsh(h4)).max()
B4 = expm(-0.4j * h4)
def bo4(K): ph = np.exp(-1j * (LAM4 @ K)); return (ph[:, None] * B4) * ph.conj()[None, :]
def A4(c0, m0): return expm(-0.5j * ((np.pi / 2) * (Id - Pl4) + c0 * Pl4 + m0 * (Pg4 - Pu4)))
def gu(c0, m0):
    A = A4(c0, m0); w, V = np.linalg.eig(A @ B4 @ A); n = np.real(np.einsum('ij,ij->j', V.conj(), V)); q = -np.angle(w)
    return q[np.argmax(np.real(np.einsum('ji,jk,ki->i', V.conj(), Pg4, V)) / n)], q[np.argmax(np.real(np.einsum('ji,jk,ki->i', V.conj(), Pu4, V)) / n)]
c0 = m0 = 0.0
for _ in range(50):
    a_, b_ = gu(c0, m0); c0 -= (a_ + b_) / 2; m0 -= (a_ - b_) / 2
A = A4(c0, m0); q0 = -np.angle(np.linalg.eigvals(A @ B4 @ A))
vO, spO, cO = cone(A, B4, A) if False else (None, None, None)
vs_, cs_ = [], []
for d in dirs:
    for kk in (2e-3,):
        q = -np.angle(np.linalg.eigvals(A @ bo4(kk * d) @ A)); l = np.sort(q[np.argsort(np.abs(q))[:4]]); vs_.append((l[3] - l[0]) / (2 * kk)); cs_.append(l.sum() / 2 / (2 * kk * kk))
vO, cO = np.mean(vs_), np.mean(cs_)
check("massless at the critical m0 = %.5f (Gamma: 4 states at 0, all other levels in [1.17, 1.98], none at negative w), so no w -> -w"
      " symmetry; the cone has c != 0" % m0, int(np.sum(np.abs(q0) < 1e-9)) == 4 and np.min(q0[np.abs(q0) > 1e-9]) > 1.1 and abs(cO) > 0.05,
      f'v {vO:.4f}, c {cO:+.4f}')
LipO = np.array([np.linalg.norm(np.diag(LAM4[:, i]) @ B4 - B4 @ np.diag(LAM4[:, i]), 2) for i in range(3)]) * (1 + 1e-9)
TO = time.time(); okO, nbO, mO = certify(lambda K: A @ bo4(K) @ A, LipO, np.pi / 16, 0.08, 0.5, 0.6)
check("other-cells tick certified over the zone: nothing within 0.6 of pi; for |K|_inf >= pi/16 nothing within 0.08 of 0;"
      " for |K|_inf <= pi/16 exactly 4 states with |w| < 0.5 (one light Dirac copy, confirmed)",
      okO and int(np.sum(np.abs(q0) < 0.5)) == 4, f'{okO}: {nbO} boxes, ||dU/dK_i|| <= {LipO[0]:.3f}, margins {min(mO):.3f}, {time.time() - TO:.1f} s')

# ============================================================ 10. estimates
print('== 10. estimates (supplied lattice spacing a = 5 Planck lengths)')
print('   E(particle, antiparticle) = v|k| +- c k^2  ->  eta = 2 (c/v)(a/l_P); measured (Crab synchrotron, vacuum Cherenkov): |eta| < ~1e-7')
for nm, c_, v_ in (('P (protected)', cP, vP), ('other-cells tick', cO, vO)):
    print(f'   {nm:17s}: c/v = {c_ / v_:+.3e} -> eta = {2 * c_ / v_ * 5:+.1e}')
print(f'   S (particle-hole) : c = 0 by the exact W symmetry (numerical {cS:+.0e})')
print(f'   runtime {time.time() - T_START:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
