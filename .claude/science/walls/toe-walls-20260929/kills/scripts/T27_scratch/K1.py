#!/usr/bin/env python3
"""T27 tests A-D on the wall's own model (SU(2) one-rishon 4-cycle, 65536 dims).

Conventions copied from the note's runner (read, not imported, not edited):
scripts/non_abelian_gauss_law_no_record_pattern_solutions_check_2026_09_03.py
Pre-registration: PREREG.md in this folder (written before this script was run).
"""
import itertools, sys, time, json
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

T0 = time.time()
OUT = {}
def log(*a):
    print(*a); sys.stdout.flush()
def check(name, cond, detail=""):
    OUT[name] = bool(cond)
    log(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))

NV, NE = 4, 4
LINKS = [(0, 1), (1, 2), (2, 3), (3, 0)]
NMODE = 2 * NV
DM = 2 ** NMODE
DL = 4
DLL = DL ** NE
DIM = DM * DLL
ETA = [1.0, 1.0, -1.0, -1.0]
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
def build_hop(t=1.0):
    H = sp.csr_matrix((DIM, DIM), dtype=complex)
    for e, (i, j) in enumerate(LINKS):
        term = sp.csr_matrix((DIM, DIM), dtype=complex)
        for a in range(2):
            for b in range(2):
                term = term + (PSI[(i, a)].getH() @ PSI[(j, b)]) @ emb_link(e, U4[a][b])
        term = term + term.getH()
        H = H - t * ETA[e] * term
    return H.tocsr()
H = build_hop(1.0)
log("built G,H in %.1fs" % (time.time() - T0))

def nnz0(M):
    M = sp.csr_matrix(M).copy(); M.eliminate_zeros(); return int(M.nnz)
def comm(A, B):
    return (A @ B - B @ A).tocsr()

# ---------------------------------------------------------------- pattern labels
idx = np.arange(DIM)
mat = idx // DLL
lk = idx % DLL
def matter_bit(m):
    return (mat >> (NMODE - 1 - m)) & 1
NOCC = np.stack([matter_bit(2 * v) + matter_bit(2 * v + 1) for v in range(NV)], axis=1)   # n_v
dig = np.stack([(lk // (DL ** (NE - 1 - e))) % DL for e in range(NE)], axis=1)
ORI = dig // 2      # 0 = rishon at i end, 1 = rishon at j end
COL = dig % 2
def rishons_at(ori):
    """p_v for an orientation tuple"""
    p = [0] * NV
    for e, (i, j) in enumerate(LINKS):
        p[i if ori[e] == 0 else j] += 1
    return p

# ================================================================ TEST A
log("\n=== TEST A: baseline ===")
ok = all(nnz0(comm(G[(v, a)], H)) == 0 for v in range(NV) for a in range(3))
check("A1 [G_v^a, H_hop] = 0 exactly (12 pairs)", ok)
# no computational-basis pattern in the Gauss kernel: sum_{v,a} ||G e_r||^2 >0 for all r
cas = np.zeros(DIM)
for v in range(NV):
    for a in range(3):
        Gm = G[(v, a)]
        cas += np.asarray(Gm.multiply(Gm.conj()).sum(axis=0)).ravel().real   # ||G e_r||^2 per column
check("A2 zero of 65536 computational-basis patterns in the Gauss kernel (min sum ||G e_r||^2 = %.3f >= 2)" % cas.min(),
      cas.min() >= 2 - 1e-12)
# atoms = connected components of the graph of nonzero entries of G^1, G^2 (transverse)
adj = sp.csr_matrix((DIM, DIM), dtype=float)
for v in range(NV):
    for a in (0, 1):
        M = G[(v, a)].copy(); M.data = (np.abs(M.data) > 0).astype(float)
        adj = adj + M
ncomp, comp = connected_components(adj, directed=False)
check("A3 dim(R cap I) = number of atoms = 1296", ncomp == 1296, "components=%d" % ncomp)
# atoms = level sets of (n_v, o_e)?
key = (NOCC * 1).dot(3 ** np.arange(NV)) * 16 + ORI.dot(2 ** np.arange(NE))
_, comp2 = np.unique(key, return_inverse=True)
# compare partitions
pair = np.unique(np.stack([comp, comp2], axis=1), axis=0)
check("A4 components are exactly the level sets of (n_v, o_e)", pair.shape[0] == 1296 and len(np.unique(comp)) == 1296 and len(np.unique(comp2)) == 1296)

# Cartan cut: all G^3_v diagonal entries zero
g3 = np.stack([G[(v, 2)].diagonal().real for v in range(NV)], axis=1)
cut = np.where(np.all(np.abs(g3) < 1e-12, axis=1))[0]
check("A5 Cartan cut has 544 patterns", len(cut) == 544, "cut=%d" % len(cut))
Gplus = {v: (G[(v, 0)] + 1j * G[(v, 1)]).tocsr() for v in range(NV)}

# per-atom kernel: null space of stacked G^+ on the cut columns of the atom
K_cols = []      # kernel vectors as (indices, values)
atom_rank = {}
Kvecs = []
Kinfo = []
cut_atoms = {}
for r in cut:
    cut_atoms.setdefault(comp2[r], []).append(r)
for at, cols in cut_atoms.items():
    cols = np.array(cols)
    if len(cols) == 0: continue
    Gram = np.zeros((len(cols), len(cols)), dtype=complex)
    for v in range(NV):
        Mv = Gplus[v][:, cols]
        Gram += (Mv.getH() @ Mv).toarray()
    ev, evec = np.linalg.eigh((Gram + Gram.conj().T) / 2)
    null = evec[:, ev < 1e-9]      # columns span the null space of stacked G^+ on the cut atom
    atom_rank[at] = null.shape[1]
    for k in range(null.shape[1]):
        vec = np.zeros(DIM, dtype=complex); vec[cols] = null[:, k]
        Kvecs.append(vec); Kinfo.append(at)
tot = sum(atom_rank.values())
check("A6 Gauss kernel rank = 82", tot == 82, "rank=%d" % tot)

# verify these vectors are annihilated by every G_v^a (full check, all three components)
Kmat = np.stack(Kvecs, axis=1) if Kvecs else np.zeros((DIM, 0))
res = 0.0
for v in range(NV):
    for a in range(3):
        res = max(res, np.abs(G[(v, a)] @ Kmat).max())
check("A7 kernel vectors are annihilated by all 12 generators (max residual %.2e)" % res, res < 1e-10)
Ksp = sp.csr_matrix(Kmat)
HK = (Ksp.getH() @ H @ Ksp).toarray()
w = np.linalg.eigvalsh((HK + HK.conj().T) / 2)
check("A8 ground energy of H_hop on the Gauss kernel = -sqrt(34)", abs(w[0] + np.sqrt(34)) < 1e-9, "E0=%.12f, -sqrt34=%.12f" % (w[0], -np.sqrt(34)))
check("A9 40-fold numerical zero and reflected spectrum", (np.abs(w) < 1e-9).sum() == 40 and np.allclose(np.sort(w), np.sort(-w), atol=1e-9),
      "zeros=%d" % (np.abs(w) < 1e-9).sum())
# invariance: H K in span K
resid = np.linalg.norm(H @ Kmat - Kmat @ (Kmat.conj().T @ (H @ Kmat)))
check("A10 H_hop maps the Gauss kernel into itself (residual %.2e)" % resid, resid < 1e-10)

# ================================================================ TEST B
log("\n=== TEST B: colour-blind labels resolve the Gauss sector; support rule ===")
def atom_label(at):
    r = np.where(comp2 == at)[0][0]
    return tuple(int(x) for x in NOCC[r]), tuple(int(x) for x in ORI[r])
ranks = {}
for at, k in atom_rank.items():
    ranks[atom_label(at)] = k
nz = {lab: k for lab, k in ranks.items() if k > 0}
check("B1 every atom's Gauss rank is 0 or 1; exactly 82 atoms have rank 1",
      all(k in (0, 1) for k in ranks.values()) and len(nz) == 82 and sum(nz.values()) == 82,
      "atoms meeting the cut=%d, rank-1 atoms=%d, max rank=%d" % (len(ranks), len(nz), max(ranks.values())))
# also: atoms outside the Cartan cut have zero Gauss kernel by construction (G^3 nonzero) -- verify via counting all atoms
# Z2 rule
def z2_ok(n, o):
    p = rishons_at(o)
    return all((p[v] + (1 if n[v] == 1 else 0)) % 2 == 0 for v in range(NV))
rule_set = set((n, o) for n in itertools.product(range(3), repeat=NV) for o in itertools.product(range(2), repeat=NE) if z2_ok(n, o))
check("B2 the rank-1 atoms are exactly the atoms obeying the local Z2 rule (rishons at v + [n_v=1] even at every vertex)",
      set(nz.keys()) == rule_set, "rule set size=%d, rank-1 set size=%d" % (len(rule_set), len(nz)))
Kn = Kmat
gram = Kn.conj().T @ Kn
check("B3 the 82 label vectors are orthonormal and span the kernel", np.allclose(gram, np.eye(82), atol=1e-9))
# Label ordering
labels = [atom_label(at) for at in Kinfo]

# ================================================================ TEST C
log("\n=== TEST C: locality of the hop in label space ===")
A = HK
nzpairs = [(a, b) for a in range(82) for b in range(82) if abs(A[a, b]) > 1e-10]
def is_hop(la, lb):
    (n1, o1), (n2, o2) = la, lb
    dif_o = [e for e in range(NE) if o1[e] != o2[e]]
    if len(dif_o) != 1: return False
    e = dif_o[0]; i, j = LINKS[e]
    dn = [n2[v] - n1[v] for v in range(NV)]
    if any(dn[v] != 0 for v in range(NV) if v not in (i, j)): return False
    return (dn[i], dn[j]) in ((1, -1), (-1, 1))
loc_ok = all(is_hop(labels[a], labels[b]) for a, b in nzpairs)
check("C1 every nonzero H_hop matrix element in the label basis connects labels differing by ONE link hop",
      loc_ok, "nonzero entries=%d among 82x82" % len(nzpairs))
# link/direction consistency: (o flips 0->1 with matter moving j->i) is the H term; check
cnt = {}
for a, b in nzpairs:
    (n1, o1), (n2, o2) = labels[a], labels[b]
    e = [k for k in range(NE) if o1[k] != o2[k]][0]
    cnt[e] = cnt.get(e, 0) + 1
log("   nonzero entries per link:", cnt)
# C3: magnitude depends only on local labels
from collections import defaultdict
groups = defaultdict(list)
for a, b in nzpairs:
    (n1, o1), (n2, o2) = labels[a], labels[b]
    if not (o1[[k for k in range(NE) if o1[k] != o2[k]][0]] == 0):   # take only direction o:0->1 (a -> b)
        continue
    e = [k for k in range(NE) if o1[k] != o2[k]][0]
    i, j = LINKS[e]
    adj_links = [k for k in range(NE) if k != e and (i in LINKS[k] or j in LINKS[k])]
    opp = [k for k in range(NE) if k != e and k not in adj_links]
    far_v = [v for v in range(NV) if v not in (i, j)]
    local = (e, n1[i], n1[j], tuple(o1[k] for k in adj_links))
    far = (tuple(n1[v] for v in far_v), tuple(o1[k] for k in opp))
    groups[local].append((abs(A[a, b]), far))
spread = 0.0; ngrp_multi = 0
for local, lst in groups.items():
    mags = [m for m, f in lst]
    if len(set(f for m, f in lst)) > 1:
        ngrp_multi += 1
        spread = max(spread, max(mags) - min(mags))
check("C3 hop magnitude depends only on the labels of the two end vertices and adjacent links (max spread across far labels %.2e over %d local classes with >1 far label)" % (spread, ngrp_multi),
      spread < 1e-9 and ngrp_multi > 0)
mags_all = sorted(set(round(float(abs(A[a, b])), 9) for a, b in nzpairs))
log("   distinct hop magnitudes:", mags_all)


# ================================================================ KILL TEST K1: is the hop a LOCAL SIGNED RULE on labels?
log("\n=== KILL K1: rebuild H from a local |amplitude| table and test whether signs are gaugeable/local ===")
from collections import defaultdict
tab = {}
for a, b in nzpairs:
    (n1, o1), (n2, o2) = labels[a], labels[b]
    e = [k for k in range(NE) if o1[k] != o2[k]][0]
    i, j = LINKS[e]
    adj_links = [k for k in range(NE) if k != e and (i in LINKS[k] or j in LINKS[k])]
    key = (e, o1[e], n1[i], n1[j], n2[i], n2[j], tuple(o1[k] for k in adj_links))
    m = round(float(abs(A[a, b])), 9)
    tab.setdefault(key, set()).add(m)
log("local keys:", len(tab), " keys with >1 magnitude:", sum(1 for v in tab.values() if len(v) > 1))
# Build H with positive local magnitude and sign -eta_e (the bare bond sign), zero elsewhere
H0 = np.zeros((82, 82))
for a, b in nzpairs:
    (n1, o1), (n2, o2) = labels[a], labels[b]
    e = [k for k in range(NE) if o1[k] != o2[k]][0]
    H0[a, b] = -ETA[e] * float(abs(A[a, b]))
w_true = np.sort(np.linalg.eigvalsh(A.real if np.allclose(A.imag, 0, atol=1e-10) else (A + A.conj().T) / 2))
w0 = np.sort(np.linalg.eigvalsh((H0 + H0.T) / 2))
log("A is real in this phase convention? ", np.allclose(A.imag, 0, atol=1e-10))
log("true spectrum min/max:", w_true[0], w_true[-1], " magnitude-only (eta-signed) min/max:", w0[0], w0[-1])
log("spectra equal?", np.allclose(w_true, w0, atol=1e-8))
# Positive-only (no sign at all) spectrum
Hp = np.zeros((82, 82))
for a, b in nzpairs:
    Hp[a, b] = -float(abs(A[a, b]))
wp = np.sort(np.linalg.eigvalsh((Hp + Hp.T) / 2))
log("all-positive-amplitude spectrum min/max:", wp[0], wp[-1], " equals true?", np.allclose(wp, w_true, atol=1e-8))
# gauge-invariant test: for each closed cycle of length 4/6 in the label graph, compare sign product of true H with sign product of H0
import networkx as nx
Gr = nx.Graph()
for a, b in nzpairs:
    if a < b: Gr.add_edge(a, b)
cyc = nx.cycle_basis(Gr)
bad = 0; tot = 0
for c in cyc:
    prod_true = 1.0 + 0j; prod_0 = 1.0
    for k in range(len(c)):
        u, v = c[k], c[(k + 1) % len(c)]
        prod_true *= A[u, v]; prod_0 *= H0[u, v]
    tot += 1
    if abs(np.angle(prod_true / prod_0 if abs(prod_0) > 1e-12 else 1) ) > 1e-6:
        bad += 1
log("fundamental cycles in label graph: %d, with holonomy differing from the eta-only local rule: %d" % (tot, bad))
OUT["K1_spectra_equal"] = bool(np.allclose(w_true, w0, atol=1e-8))
OUT["K1_bad_cycles"] = bad
json.dump({k: v for k, v in OUT.items()}, open("K1_result.json", "w"), indent=1)
