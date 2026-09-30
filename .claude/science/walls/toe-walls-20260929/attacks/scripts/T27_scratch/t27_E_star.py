#!/usr/bin/env python3
"""T27 test E1: a 4-link STAR (centre valence 4) in the wall's own SU(2) one-rishon model.

Purpose: the 4-cycle used in tests A-D never has a vertex with more than 3 doublets, so its atoms
(n_v, o_e) are always rank <= 1 and resolve the Gauss sector by themselves.  A star with centre
valence 4 has atoms of Gauss rank 2 (four doublets have two singlets).  Question: is the extra
label a LOCAL colour-blind invariant (pair Casimir of two electric fields at the centre), and does
the hop stay local in the enlarged label set?

Model = same conventions as the note (see t27_ABCD.py): links e=(i=centre 0, j=leaf e+1), 5 vertices,
10 JW matter modes, link = orientation x colour, dim = 2^10 x 4^4 = 262144.
"""
import itertools, sys, time, json
from collections import defaultdict
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg
from scipy.sparse.csgraph import connected_components

T0 = time.time()
OUT = {}
def log(*a):
    print(*a); sys.stdout.flush()
def check(name, cond, detail=""):
    OUT[name] = bool(cond)
    log(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))

NV, NE = 5, 4
LINKS = [(0, 1), (0, 2), (0, 3), (0, 4)]      # (i = centre, j = leaf)
NMODE = 2 * NV
DM = 2 ** NMODE
DL = 4
DLL = DL ** NE
DIM = DM * DLL
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TAU = [SX, SY, SZ]
def kron_list(mats):
    out = sp.identity(1, format="csr", dtype=complex)
    for m in mats:
        out = sp.kron(out, sp.csr_matrix(m), format="csr")
    return out
def jw_annihilate(m):
    mats = []
    for k in range(NMODE):
        if k < m: mats.append(SZ)
        elif k == m: mats.append(np.array([[0, 1], [0, 0]], dtype=complex))
        else: mats.append(I2)
    return kron_list(mats)
CM = [jw_annihilate(m) for m in range(NMODE)]
PI4 = np.diag([1., 1., 0., 0.]).astype(complex)
PJ4 = np.diag([0., 0., 1., 1.]).astype(complex)
TA4 = [np.kron(I2, t / 2.0).astype(complex) for t in TAU]
U4 = [[np.zeros((4, 4), dtype=complex) for _ in range(2)] for _ in range(2)]
for a in range(2):
    for b in range(2):
        U4[a][b][2 + b, a] = -1.0
def link_only(e, op):
    return kron_list([op if k == e else np.eye(DL) for k in range(NE)])
def emb_matter(op):
    return sp.kron(op, sp.identity(DLL, format="csr", dtype=complex), format="csr")
def emb_link(e, op):
    return sp.kron(sp.identity(DM, format="csr", dtype=complex), link_only(e, op), format="csr")
PSI = {(v, a): emb_matter(CM[2 * v + a]) for v in range(NV) for a in range(2)}
RHO = {}
for v in range(NV):
    for a in range(3):
        acc = sp.csr_matrix((DIM, DIM), dtype=complex)
        for p in range(2):
            for q in range(2):
                c = TAU[a][p, q] / 2.0
                if c != 0:
                    acc = acc + c * (PSI[(v, p)].getH() @ PSI[(v, q)])
        RHO[(v, a)] = acc.tocsr()
EF = {}
for e in range(NE):
    for a in range(3):
        EF[(e, 'i', a)] = emb_link(e, PI4 @ TA4[a])
        EF[(e, 'j', a)] = emb_link(e, PJ4 @ TA4[a])
def ends_at(v):
    out = []
    for e, (i, j) in enumerate(LINKS):
        if i == v: out.append((e, 'i'))
        if j == v: out.append((e, 'j'))
    return out
G = {}
for v in range(NV):
    for a in range(3):
        acc = RHO[(v, a)]
        for (e, s) in ends_at(v):
            acc = acc + EF[(e, s, a)]
        G[(v, a)] = acc.tocsr()
ETA = [1.0] * NE     # star has no cycle; the sign is a gauge choice on a tree
H = sp.csr_matrix((DIM, DIM), dtype=complex)
for e, (i, j) in enumerate(LINKS):
    term = sp.csr_matrix((DIM, DIM), dtype=complex)
    for a in range(2):
        for b in range(2):
            term = term + (PSI[(i, a)].getH() @ PSI[(j, b)]) @ emb_link(e, U4[a][b])
    term = term + term.getH()
    H = H - ETA[e] * term
H = H.tocsr()
log("built star G,H in %.1fs (dim %d)" % (time.time() - T0, DIM))
def nnz0(M):
    M = sp.csr_matrix(M).copy(); M.eliminate_zeros(); return int(M.nnz)
def comm(A, B):
    return (A @ B - B @ A).tocsr()
check("S0 [G_v^a, H_hop] = 0 exactly on the star", all(nnz0(comm(G[(v, a)], H)) == 0 for v in range(NV) for a in range(3)))

idx = np.arange(DIM)
mat = idx // DLL
lk = idx % DLL
def matter_bit(m): return (mat >> (NMODE - 1 - m)) & 1
NOCC = np.stack([matter_bit(2 * v) + matter_bit(2 * v + 1) for v in range(NV)], axis=1)
dig = np.stack([(lk // (DL ** (NE - 1 - e))) % DL for e in range(NE)], axis=1)
ORI = dig // 2
key = NOCC.dot(3 ** np.arange(NV)) * 16 + ORI.dot(2 ** np.arange(NE))
_, comp2 = np.unique(key, return_inverse=True)

g3 = np.stack([G[(v, 2)].diagonal().real for v in range(NV)], axis=1)
cut = np.where(np.all(np.abs(g3) < 1e-12, axis=1))[0]
log("Cartan cut size", len(cut))
Gplus = {v: (G[(v, 0)] + 1j * G[(v, 1)]).tocsc() for v in range(NV)}

# pair Casimir of the electric fields at the centre for links (a,b): (E_a + E_b)^2 with E_l = P_i^l tau/2 at centre end
def pair_casimir(a, b):
    tot = sp.csr_matrix((DIM, DIM), dtype=complex)
    for k in range(3):
        Ek = EF[(a, 'i', k)] + EF[(b, 'i', k)]
        tot = tot + Ek @ Ek
    return tot.tocsr()
C_pair = {(a, b): pair_casimir(a, b) for a in range(NE) for b in range(a + 1, NE)}
log("pair Casimirs built %.1fs" % (time.time() - T0))

cut_atoms = defaultdict(list)
for r in cut:
    cut_atoms[comp2[r]].append(r)
def label_of(at):
    r = np.where(comp2 == at)[0][0]
    return tuple(int(x) for x in NOCC[r]), tuple(int(x) for x in ORI[r])
ranks = {}
Kvecs, Klabs = [], []     # kernel vectors and their (atom, iota) labels
n_rank2 = 0
unresolved = 0
for at, cols in cut_atoms.items():
    cols = np.array(cols)
    Gram = np.zeros((len(cols), len(cols)), dtype=complex)
    for v in range(NV):
        Mv = Gplus[v][:, cols]
        Gram += (Mv.getH() @ Mv).toarray()
    ev, evec = np.linalg.eigh((Gram + Gram.conj().T) / 2)
    null = evec[:, ev < 1e-9]
    k = null.shape[1]
    lab = label_of(at)
    ranks[lab] = k
    if k == 0: continue
    # embed as sparse columns (rows = the atom's Cartan-cut patterns)
    def spcol(vec_small):
        return sp.csr_matrix((vec_small, (cols, np.zeros(len(cols), dtype=int))), shape=(DIM, 1))
    if k == 1:
        Kvecs.append(spcol(null[:, 0])); Klabs.append((lab, 0))
        continue
    n_rank2 += 1
    n, o = lab
    at_c = [e for e in range(NE) if o[e] == 0]
    if len(at_c) < 2:
        unresolved += 1
        for t in range(k): Kvecs.append(spcol(null[:, t])); Klabs.append((lab, t))
        continue
    pair = (at_c[0], at_c[1])
    Bsp = sp.hstack([spcol(null[:, t]) for t in range(k)]).tocsr()
    Cb = (Bsp.getH() @ (C_pair[pair] @ Bsp)).toarray()
    Cb = (Cb + Cb.conj().T) / 2
    cv, cvec = np.linalg.eigh(Cb)
    if np.min(np.diff(cv)) < 1e-6:
        unresolved += 1
    for t in range(k):
        Kvecs.append(spcol(null @ cvec[:, t])); Klabs.append((lab, round(float(cv[t]), 6)))
K = sp.hstack(Kvecs).tocsr()
dimK = K.shape[1]
exp = 0
c = [2, 1, 2, 2, 4]
for o in itertools.product(range(2), repeat=NE):
    p = [sum(1 for e in range(NE) if o[e] == 0)] + [1 if o[e] == 1 else 0 for e in range(NE)]
    val = 1
    for pv in p: val *= c[pv]
    exp += val
check("E1a Gauss kernel dimension equals sum_o prod_v c(p_v) = %d (c=[2,1,2,2,4])" % exp, dimK == exp, "computed=%d" % dimK)
maxrank = max(ranks.values())
check("E1b the star has atoms of Gauss rank 2 (colour-blind atoms alone do NOT resolve it)", maxrank == 2,
      "max atom rank=%d, rank-2 atoms=%d" % (maxrank, n_rank2))
check("E1c every rank-2 atom is resolved by the pair Casimir (E_a+E_b)^2 of two rishon fields at the centre (distinct eigenvalues)", unresolved == 0,
      "unresolved=%d" % unresolved)
gr = (K.getH() @ K).toarray()
check("E1d the enlarged label vectors are orthonormal", np.allclose(gr, np.eye(dimK), atol=1e-9))
res = max(abs(G[(v, a)] @ K).max() for v in range(NV) for a in range(3))
check("E1e label vectors are annihilated by all Gauss generators (residual %.1e)" % res, res < 1e-10)
Z2 = lambda n, o: (sum(1 for e in range(NE) if o[e] == 0) + (n[0] == 1)) % 2 == 0 and all(((1 if o[e] == 1 else 0) + (n[e + 1] == 1)) % 2 == 0 for e in range(NE))
nz_atoms = set(l for l, k in ranks.items() if k > 0)
rule = set((n, o) for n in itertools.product(range(3), repeat=NV) for o in itertools.product(range(2), repeat=NE) if Z2(n, o))
check("E1f the atoms with a singlet are exactly those obeying the local Z2 rule (parity of doublets at every vertex even)", nz_atoms == rule, "%d vs %d" % (len(nz_atoms), len(rule)))
# rank pattern: rank equals M(count of doublets) * ... check rank(atom) = M(doublets at centre) where M = Catalan-type
M = {0: 1, 1: 0, 2: 1, 3: 0, 4: 2, 5: 0, 6: 5}
badrank = 0
for (n, o), k in ranks.items():
    pc = sum(1 for e in range(NE) if o[e] == 0) + (n[0] == 1)
    pred = M[pc] if all((((1 if o[e] == 1 else 0) + (n[e + 1] == 1)) % 2 == 0) for e in range(NE)) else 0
    if k != pred: badrank += 1
check("E1g atom rank = M(number of doublets at the centre) (M(0..4)=1,0,1,0,2) on the star", badrank == 0, "mismatches=%d" % badrank)

# Hop in the enlarged label basis
HK = (K.getH() @ H @ K).toarray()
HK = (HK + HK.conj().T) / 2
w = np.linalg.eigvalsh(HK)
log("   star spectrum: min %.6f max %.6f" % (w.min(), w.max()))
# H maps kernel into kernel?
resid = sp.linalg.norm(H @ K - K @ (K.getH() @ (H @ K)))
check("E1h H_hop maps the label span into itself (residual %.1e)" % resid, resid < 1e-9)
nzp = [(a, b) for a in range(dimK) for b in range(dimK) if abs(HK[a, b]) > 1e-10]
def is_hop(la, lb):
    (n1, o1), (n2, o2) = la, lb
    d = [e for e in range(NE) if o1[e] != o2[e]]
    if len(d) != 1: return False
    e = d[0]; i, j = LINKS[e]
    dn = [n2[v] - n1[v] for v in range(NV)]
    if any(dn[v] != 0 for v in range(NV) if v not in (i, j)): return False
    return (dn[i], dn[j]) in ((1, -1), (-1, 1))
okloc = all(is_hop(Klabs[a][0], Klabs[b][0]) for a, b in nzp)
check("E1i every nonzero hop element (enlarged labels) is a single-link hop: atom labels change on ONE link and its two ends only", okloc,
      "nonzero entries=%d of %d^2" % (len(nzp), dimK))
# far-label independence: leaves other than the hopping leaf
grp = defaultdict(list)
for a, b in nzp:
    (n1, o1), i1 = Klabs[a]; (n2, o2), i2 = Klabs[b]
    if not any(o1[e] == 0 and o2[e] == 1 for e in range(NE)): continue
    e = [k for k in range(NE) if o1[k] != o2[k]][0]
    if o1[e] != 0: continue
    leaf = e + 1
    far = tuple(n1[v] for v in range(1, NV) if v != leaf)
    localkey = (e, n1[0], n1[leaf], tuple(o1[k] for k in range(NE) if k != e), i1, i2)
    grp[localkey].append((abs(HK[a, b]), far))
spread = 0.0; multi = 0
for lk_, lst in grp.items():
    if len(set(f for m, f in lst)) > 1:
        multi += 1
        spread = max(spread, max(m for m, f in lst) - min(m for m, f in lst))
check("E1j hop magnitude is independent of the labels of the other leaves (max spread %.1e over %d local classes with several far-label values)" % (spread, multi), spread < 1e-9 and multi > 0)
OUT["elapsed_s"] = time.time() - T0
json.dump(OUT, open("t27_E_star_result.json", "w"), indent=1)
log("DONE %.1fs" % (time.time() - T0))
