"""C1 checker model: the eight-node step S.R_L.U_H.U_L rebuilt on the independent B7-checker core (chk_core.py, a copy of
B7_check/chk_core.py: own GF(2) gauge, own brute-force PSG).  No import of the repo model, chk_model.py or c1lib.py.

Conventions (chk_core): G_g |v,c> = (-1)^(lam.v + tau(c)) |M v, M c>,  O = sum_{v,d} |v+d><v| (x) h_d,  O(k) = sum_d h_d e^{-ik.d},
Bloch vectors e^{ik.v};  symmetric O  <=>  U_g O(k) U_g^T = O(M k + pi M lam).
Step factors (definitions from the scale-ladder note item 6 / chk_model.py, re-implemented in this gauge):
  H_on  = on-site corner hopping, amplitude -(-1)^u;   R_L = link hopping, amplitude -(-1)^u / sqrt2;
  Lam   = on-site triangle term i(-1)^u around each octant triangle, oriented by det;
  U_H   = P0 - P1 - i P2 (spectral projectors of H_on, ascending);  U_L = P0 + i P1 + i P2 + P3 (of Lam, ascending);
  S     = diagonal shift {d,e}@v -> {d,e}@v+d+e, signs from symmetrising one hop over the 24 proper lifts.
A gauge change relative to the repo can move momenta by pi*Z^3 and flip the overall sign of S; nodes are therefore
located from the spectrum, not assumed."""
import itertools
import numpy as np
from chk_core import (CORN, CI, ETYPES, ELIST, u, OH, LAM, TAU, UF, Z, edge_key, neg, vadd, dot)

PROPER = list(range(24))
def wrap(x): return (np.asarray(x) + np.pi) % (2 * np.pi) - np.pi
def same_k(a, b, tol=1e-8): return np.allclose(wrap(np.asarray(a, float) - np.asarray(b, float)), 0, atol=tol)

# ---- blocks ----
def add(bl, d, M):
    d = tuple(int(x) for x in d)
    bl.setdefault(d, np.zeros((12, 12), complex)); bl[d] += M
Hon = np.zeros((12, 12)); blL = {}
for (i1, i2, s) in ELIST:
    a = -(-1.0) ** int(u[ETYPES[(i1, i2, s)]])
    if tuple(s) == Z:
        Hon[i2, i1] += a; Hon[i1, i2] += a
    else:
        M1 = np.zeros((12, 12)); M1[i2, i1] = a / np.sqrt(2); add(blL, s, M1)
        M2 = np.zeros((12, 12)); M2[i1, i2] = a / np.sqrt(2); add(blL, neg(s), M2)
Lam = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, zz = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
    cy = [frozenset((x, y)), frozenset((y, zz)), frozenset((zz, x))]
    if round(np.linalg.det(np.array([x, y, zz]))) < 0: cy = cy[::-1]
    for a_ in range(3):
        q, r = cy[a_], cy[(a_ + 1) % 3]
        amp = 1j * (-1.0) ** int(u[ETYPES[edge_key(q, r, Z)]])
        Lam[CI[r], CI[q]] += amp; Lam[CI[q], CI[r]] += np.conj(amp)
def eproj(M):
    w, V = np.linalg.eigh(M); ls = sorted(set(np.round(w, 6)))
    return ls, [V[:, np.abs(w - l) < 1e-6] @ V[:, np.abs(w - l) < 1e-6].conj().T for l in ls]
EV_H, PH = eproj(Hon); EV_L, PL = eproj(Lam)
assert len(PH) == 3 and len(PL) == 4, (EV_H, EV_L)
UH = PH[0] - PH[1] - 1j * PH[2]
UL = PL[0] + 1j * PL[1] + 1j * PL[2] + PL[3]

def rot_blocks(bl, g):
    """blocks of G_g O G_g^T: h'_{M d} = (-1)^{lam.d} U h_d U^T."""
    out = {}
    for d, h in bl.items():
        add(out, OH[g] @ np.array(d), (-1.0) ** int(LAM[g] @ np.array(d)) * UF[g] @ h @ UF[g].T)
    return out
def sym_blocks(bl, idx=PROPER, chi=None):
    out = {}
    for g in idx:
        c = 1.0 if chi is None else np.conj(chi[g])
        for d, h in rot_blocks(bl, g).items(): add(out, d, c * h / len(idx))
    return {d: h for d, h in out.items() if np.abs(h).max() > 1e-13}
cxy = frozenset(((1, 0, 0), (0, 1, 0)))
seed = {}; M0 = np.zeros((12, 12)); M0[CI[cxy], CI[cxy]] = 1.0; add(seed, (1, 1, 0), M0)
blS = sym_blocks(seed)
mx = max(np.abs(h).max() for h in blS.values()); blS = {d: h / mx for d, h in blS.items()}

def bloch(bl, ks):
    ks = np.atleast_2d(np.asarray(ks, float)); out = np.zeros((len(ks), 12, 12), complex)
    for d, h in bl.items(): out += np.exp(-1j * ks @ np.array(d, float))[:, None, None] * h[None]
    return out
def dbloch(bl, ks, j):
    ks = np.atleast_2d(np.asarray(ks, float)); out = np.zeros((len(ks), 12, 12), complex)
    for d, h in bl.items(): out += (-1j * d[j]) * np.exp(-1j * ks @ np.array(d, float))[:, None, None] * h[None]
    return out
UU = UH @ UL
def Wb(ks): return bloch(blS, ks) @ bloch(blL, ks) @ UU
def W(k): return Wb(k)[0]
def dW(k, j): return (dbloch(blS, k, j)[0] @ bloch(blL, k)[0] + bloch(blS, k)[0] @ dbloch(blL, k, j)[0]) @ UU

# ---- affine action of the lifts ----
def gk(g, k): return OH[g] @ np.asarray(k, float) + np.pi * (OH[g] @ LAM[g])
def stab(k, idx=PROPER): return [g for g in idx if same_k(gk(g, k), k)]
def find_el(M): return [g for g in range(48) if (OH[g] == np.array(M)).all()][0]

# class labels (proper rotations) and the A2 character of O
def cls(M):
    t = int(round(np.trace(M)))
    if t == 3: return 'E'
    if t == 0: return 'C3'
    if t == 1: return 'C4'
    return 'C2' if all(abs(M[i, i]) == 1 for i in range(3)) else "C2'"
A2 = {g: {'E': 1, 'C3': 1, 'C2': 1, 'C4': -1, "C2'": -1}[cls(OH[g])] for g in PROPER}
A1 = {g: 1 for g in PROPER}

# ---- levels ----
def levels(k, Wfun=W, tol=1e-7):
    """list of (eigenphase, orthonormal basis) of the unitary Wfun(k), grouped by degeneracy."""
    Wk = Wfun(k); e, V = np.linalg.eig(Wk); ph = np.angle(e); used = np.zeros(len(e), bool); out = []
    for i in np.argsort(ph):
        if used[i]: continue
        grp = np.where((~used) & (np.abs(wrap(ph - ph[i])) < tol))[0]; used[grp] = True
        Qm, _ = np.linalg.qr(V[:, grp]); out.append((ph[i], Qm))
    return out
def level_at(k, E, Wfun=W):
    for e, Qm in levels(k, Wfun):
        if abs(wrap(e - E)) < 1e-6: return Qm
    return None
PAU = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def weyl_B(k, Qm):
    """first-order degenerate PT of the eigenphase on a 2-fold level: d(phase) = -i <W^dag dW>."""
    Wk = W(k); A = [-1j * Qm.conj().T @ Wk.conj().T @ dW(k, j) @ Qm for j in range(3)]
    a = np.array([np.trace(x).real / 2 for x in A])
    B = np.array([[np.trace(A[j] @ PAU[b]).real / 2 for b in range(3)] for j in range(3)])
    return a, B
CUBE = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
