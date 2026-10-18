"""B18 checker model: the supplied corner model, built by copying the construction code of
scripts/scale_ladder_corner_fermion_cross_rung_invariants_2026_10_18.py (gauge, PSG lifts,
H0, Bloch blocks, diagonal shift S, Lambda, on-site Clifford-phase factors).
Independent of b18lib.py / walklib.py.  Import with  `from chk_model import *`."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ.setdefault(_v, "2")
import itertools, sys
import numpy as np
REPO = '/home/user/qubit-lattice-axiom-framework'
sys.path.insert(0, REPO + '/scripts')
import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
C = _model._run_reviewed_program(definitions_only=True)

L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']
F = dict(square=1, triangle=0, plaquette=1, tube=1)
def dmod(x): return ((x + 1) % L) - 1
DIRS = C['DIRS']
def neg(d): return tuple(-x for x in d)
def perp(d, e): return sum(a*b for a, b in zip(d, e)) == 0 and d != e
etypes = []; ekey = {}
def addt(c1, c2, sh):
    if (c1, c2, sh) in ekey or (c2, c1, neg(sh)) in ekey: return
    ekey[(c1, c2, sh)] = ekey[(c2, c1, neg(sh))] = len(etypes); etypes.append((c1, c2, sh))
Z0 = (0, 0, 0)
for c in CORN:
    d, e = tuple(c)
    for a, b in ((d, e), (e, d)):
        for f in DIRS:
            if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                addt(c, frozenset((a, f)), Z0)
        addt(c, frozenset((neg(a), b)), a)
nT = len(etypes)
def cyc(seq):
    return [ekey[(c1, c2, tuple(y - x for x, y in zip(p1, p2)))] for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
cell = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
for d in DIRS:
    a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
    b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
    cell['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
    for i in range(4):
        p, q = ring[i], ring[(i+1) % 4]
        cell['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    cell['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
    cell['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
rows = []; rhs = []
for k_, cs in cell.items():
    for c in cs: rows.append(c); rhs.append(F[k_])
ucell = C['gf2_solve'](rows, rhs, nT)
u = np.zeros(C['nE'], np.uint8)
for key, i in C['EID'].items():
    a, b = tuple(key); (v, c), (w, c2) = VERTS[a], VERTS[b]
    u[i] = ucell[ekey[(c, c2, tuple(dmod(y - x) for x, y in zip(v, w)))]]
assert all({int(sum(u[j] for j in c) % 2) for c in cs} == {F[k_]} for k_, cs in C['cycles'].items())

INVM = -np.eye(3, dtype=int)
psg = lambda f: C['psg_sign'](f, u)
rots = [psg(lambda q, M=R: C['rot_vert'](M, q)) for R in ROTS]
invs = [psg(lambda q, M=R @ INVM: C['rot_vert'](M, q)) for R in ROTS]
TV = list(itertools.product(range(L), repeat=3))
trans = [psg(lambda q, t=t: C['trans_vert'](t, q)) for t in TV]
def conj(Xm, P, s):
    sg = (-1.0) ** s; Y = np.zeros_like(Xm); Y[np.ix_(P, P)] = Xm * np.outer(sg, sg); return Y
def opmat_from(P, s):
    M = np.zeros((nV, nV)); M[P, np.arange(nV)] = (-1.0) ** s; return M
loc0 = [C['VID'][((0, 0, 0), c)] for c in CORN]; CI = {c: i for i, c in enumerate(CORN)}
def H0(t1, t2):
    H = np.zeros((nV, nV))
    for key in C['EDGES']:
        i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
        H[i, j] = H[j, i] = -t * (-1.0) ** u[C['EID'][key]]
    return H
def blocks_from(Hr):
    bl = {}
    for a, v in enumerate(VERTS):
        sh = tuple(dmod(x) for x in v[0])
        for bi, j in enumerate(loc0):
            if abs(Hr[a, j]) > 1e-12: bl.setdefault(sh, np.zeros((12, 12), complex))[CI[v[1]], bi] += Hr[a, j]
    return bl
def Hk(bl, k):
    H = np.zeros((12, 12), complex)
    for sh, M in bl.items(): H += M * np.exp(1j * np.dot(k, sh))
    return H
kst = np.array([1, -1, 1]) * np.pi / 2
def Bloch(k):
    B = np.zeros((nV, 12), complex)
    for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(L ** 3)
    return B
def wrap(x): return np.angle(np.exp(1j * x))

# Part 6 ingredients (copied)
RLr = H0(0.0, 1.0) / np.sqrt(2)
blL = blocks_from(RLr)
HonR = H0(1.0, 0.0)
c_xy = [c for c in CORN if set(c) == {(1, 0, 0), (0, 1, 0)}][0]
i0 = C['VID'][((0, 0, 0), c_xy)]; j0 = C['VID'][((1, 1, 0), c_xy)]
Sr = np.zeros((nV, nV))
for Pr, sr in rots:
    for Pt, st in trans:
        P = Pt[Pr]; s_ = sr ^ st[Pr]; Sr[P[j0], P[i0]] += (-1.0) ** (int(s_[i0]) + int(s_[j0]))
Sr /= np.abs(Sr).max()
assert np.allclose(Sr @ Sr.T, np.eye(nV)) and all(np.allclose(conj(Sr, P, s_), Sr) for P, s_ in rots + trans[:5])
Lam = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    for a_ in range(3):
        q_, r_ = cy[a_], cy[(a_ + 1) % 3]; ii, jj = C['VID'][((0, 0, 0), q_)], C['VID'][((0, 0, 0), r_)]
        amp = 1j * (-1.0) ** u[C['EID'][frozenset((ii, jj))]]; Lam[CI[r_], CI[q_]] += amp; Lam[CI[q_], CI[r_]] += np.conj(amp)
def eproj(M):
    w_, V_ = np.linalg.eigh(M); ls = sorted(set(np.round(w_, 6)))
    return [V_[:, np.abs(w_ - l) < 1e-6] @ V_[:, np.abs(w_ - l) < 1e-6].conj().T for l in ls]
Hon0 = (Bloch(np.zeros(3)).conj().T @ HonR @ Bloch(np.zeros(3)))
PH, PLm = eproj(Hon0), eproj(Lam)
PHASE = [1, 1j, -1, -1j]
def UHc(a, b): return PH[0] + PHASE[a] * PH[1] + PHASE[b] * PH[2]
def ULc(a, b, c): return PLm[0] + PHASE[a] * PLm[1] + PHASE[b] * PLm[2] + PHASE[c] * PLm[3]
UH = PH[0] - PH[1] - 1j * PH[2]; UL = PLm[0] + 1j * PLm[1] + 1j * PLm[2] + PLm[3]
assert np.allclose(UH, UHc(2, 3)) and np.allclose(UL, ULc(1, 1, 0))
blS = blocks_from(Sr)
SKc = lambda k: Hk(blS, k)
RLk = lambda k: Hk(blL, k)
Ws = lambda k: SKc(k) @ RLk(k) @ UH @ UL
Rm = [opmat_from(P, s) for P, s in rots]
CUBE = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
FACE = {c: tuple(int(x) for x in np.add(*[np.array(d) for d in c])) for c in CORN}
