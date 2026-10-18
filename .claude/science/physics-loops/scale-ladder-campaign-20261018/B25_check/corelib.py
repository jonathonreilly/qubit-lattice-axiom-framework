"""B25_check independent model library.
Built ONLY on B7_check/chk_core.py (own GF(2) gauge solve, own brute-force PSG) -- does not import chk_model, chklib,
b2Xlib or any B25 code.  Letters in the chk_core gauge and chk_core Bloch convention H(k) = sum_d h_d e^{-i k.d}:
  S       : PSG symmetrisation of the single hop |(1,1,0), c_xy><0, c_xy|  (diagonal, displacement +f_c)
  R       : link hopping  -(-1)^u / sqrt2  on link edges   (same overall sign convention as the repo model: H0 = -t(-1)^u)
  Hon     : on-site hopping -(-1)^u on on-site edges; PH = its eigenprojectors (ascending eigenvalue)
  Lam     : oriented triangle hopping i(-1)^u (orientation by det of the octant frame); PLm = eigenprojectors (ascending)
  H_ab = PH0 + i^a PH1 + i^b PH2;  L_abc = PLm0 + i^a PLm1 + i^b PLm2 + i^c PLm3;  PP = PLm0 + PLm2;  PL(phi) = PP + e^{i phi}(1-PP)
  Y = diag((-1)^{(f_x+f_y+f_z)/2})."""
import os, sys, itertools
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ.setdefault(_v, "1")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B7_check'))
import chk_core as cc
import numpy as np

CORN = cc.CORN; CI = cc.CI; Z0 = (0, 0, 0)
FC = np.array([np.add(*[np.array(d) for d in c]) for c in CORN])          # f_c, integer vectors
# ---- S
cxy = frozenset(((1, 0, 0), (0, 1, 0)))
_hS = {}
for g in cc.PROPER:
    R = cc.OH[g]; c2 = cc.rcorn(R, cxy); d = tuple(int(x) for x in R @ np.array([1, 1, 0]))
    s = (-1.0) ** int(cc.LAM[g] @ np.array([1, 1, 0]))
    _hS.setdefault(d, np.zeros((12, 12)))[CI[c2], CI[c2]] += s
_hS = {d: M for d, M in _hS.items() if np.abs(M).max() > 1e-12}
_n = max(np.abs(M).max() for M in _hS.values()); _hS = {d: M / _n for d, M in _hS.items()}
SIG = np.zeros(12)
for d, M in _hS.items():
    for c in range(12):
        if abs(M[c, c]) > 0: SIG[c] = M[c, c]; assert np.array_equal(np.array(d), FC[c])
assert np.all(np.abs(SIG) == 1)
# ---- R_L
_hL = {}
for (i1, i2, s), e in cc.ETYPES.items():
    if s == Z0: continue
    amp = -(-1.0) ** int(cc.u[e]) / np.sqrt(2)
    _hL.setdefault(tuple(s), np.zeros((12, 12)))[i2, i1] += amp
    _hL.setdefault(tuple(-x for x in s), np.zeros((12, 12)))[i1, i2] += amp
LSH = np.array(list(_hL.keys()), float); LM = np.array([_hL[s] for s in _hL])
# ---- on-site
Hon = np.zeros((12, 12))
for (i1, i2, s), e in cc.ETYPES.items():
    if s != Z0: continue
    Hon[i1, i2] += -(-1.0) ** int(cc.u[e]); Hon[i2, i1] += -(-1.0) ** int(cc.u[e])
Lam = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    for a_ in range(3):
        q, r = cy[a_], cy[(a_ + 1) % 3]
        e = cc.ETYPES[cc.edge_key(q, r, Z0)]
        amp = 1j * (-1.0) ** int(cc.u[e]); Lam[CI[r], CI[q]] += amp; Lam[CI[q], CI[r]] += np.conj(amp)
def eproj(M):
    w_, V_ = np.linalg.eigh(M); ls = sorted(set(np.round(w_, 6)))
    return [V_[:, np.abs(w_ - l) < 1e-6] @ V_[:, np.abs(w_ - l) < 1e-6].conj().T for l in ls], ls
PH, HLEV = eproj(Hon); PLm, LLEV = eproj(Lam)
I4 = [1, 1j, -1, -1j]
def Hab(a, b): return PH[0] + I4[a % 4] * PH[1] + I4[b % 4] * PH[2]
def Labc(a, b, c): return PLm[0] + I4[a % 4] * PLm[1] + I4[b % 4] * PLm[2] + I4[c % 4] * PLm[3]
def H6(a, b): return PH[0] + np.exp(1j * np.pi * a / 6) * PH[1] + np.exp(1j * np.pi * b / 6) * PH[2]
def L6(a, b, c): return PLm[0] + np.exp(1j * np.pi * a / 6) * PLm[1] + np.exp(1j * np.pi * b / 6) * PLm[2] + np.exp(1j * np.pi * c / 6) * PLm[3]
PP = PLm[0] + PLm[2]
def PL(phi): return PP + np.exp(1j * phi) * (np.eye(12) - PP)
Ymat = np.diag((-1.0) ** (FC.sum(1) // 2))
def letter_const(name):
    """name as in the B-series palettes: Hab, Labc, Ha.b, La.b.c, Pm (PL(m pi/6)), L101/L202/L303 are ordinary L letters."""
    if name[0] == 'P': return PL(np.pi * int(name[1:]) / 6)
    if '.' in name:
        xs = [int(t) for t in name[1:].split('.')]
        return H6(*xs) if name[0] == 'H' else L6(*xs)
    xs = [int(t) for t in name[1:]]
    return Hab(*xs) if name[0] == 'H' else Labc(*xs)
POW = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2, 'S4': 4, 'S4i': -4}
def Wc(w, ks):
    """batched word in the chk_core convention; w: list of 'S*'/'R' strings and 12x12 matrices; product left to right."""
    ks = np.atleast_2d(np.asarray(ks, float)); N = len(ks); W = np.broadcast_to(np.eye(12, dtype=complex), (N, 12, 12)).copy()
    for L in w:
        if isinstance(L, str):
            if L == 'R': W = W @ np.einsum('nt,tij->nij', np.exp(-1j * ks @ LSH.T), LM)
            else:
                p = POW[L]; W = W * ((SIG ** abs(p)) * np.exp(-1j * p * ks @ FC.T))[:, None, :]
        else: W = W @ L
    return W
def build(sk, names):
    it = iter(names); return [letter_const(next(it)) if L in ('o', 'p', 'q') else L for L in sk]
def nSw(w): return sum(POW[L] for L in w if isinstance(L, str) and L != 'R')
def wrap(x): return np.angle(np.exp(1j * np.asarray(x)))
# PSG (proper rotations): W(R k + pi R lam) = U W(k) U^T, U = UF[g]  (constant!)
ROTG = cc.PROPER
def fib(g, k): return cc.fibre_image(g, k)
