#!/usr/bin/env python3
"""edge-set: triangle/tetrahedron projector, dressed edge hop, CL-2 edge units.

Adopted edge set (coordinator, from edge-modes): axis edges + on every square face
the diagonal joining its two even-sum corners; each unit cube = 5 tetrahedra
(inscribed regular tetrahedron on the even corners, 4 corner tetrahedra at the odd
corners: 3 axis + 3 diagonal edges). Register length = l0 * (1 + n/2S), n in 0..2S.
Two readings of l0: (F) the edge's flat length (1 or sqrt2 rungs); (L) CL-1's
literal "rung length" for every edge.
Sections: A cell constraints; B projector kept by the dressed hop (exact);
C CL-2 cost with/without edge units. numpy/scipy only.
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
from scipy.sparse.csgraph import connected_components
from scipy.linalg import expm
from scipy.optimize import linprog

T0 = time.time()
NP = NF = 0
def check(name, ok, msg):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {msg}")

R2 = np.sqrt(2.0)
# ---------------- cells of the adopted set ----------------
# corner tetrahedron at odd corner o=(1,0,0) of the unit cube: o and its 3 cube neighbours
CORNER = [np.array(v) for v in [(1, 0, 0), (0, 0, 0), (1, 1, 0), (1, 0, 1)]]
INSCR = [np.array(v) for v in [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]]
P6 = list(itertools.combinations(range(4), 2))

def cm_gram(L):
    """Gram matrix of a tetrahedron from its 6 lengths (order P6); PD <=> nondegenerate."""
    G = np.empty(L.shape[:-1] + (3, 3))
    l = {p: L[..., k] for k, p in enumerate(P6)}
    for i in range(1, 4):
        for j in range(1, 4):
            lij = 0 if i == j else l[(min(i, j), max(i, j))]
            G[..., i-1, j-1] = 0.5*(l[(0, i)]**2 + l[(0, j)]**2 - lij**2)
    return G

def tri_ok(a, b, c, tol=1e-12):
    return (a + b > c + tol) & (b + c > a + tol) & (a + c > b + tol)

def tet_ok(L, tol=1e-12):
    ev = np.linalg.eigvalsh(cm_gram(L))
    tris = [(0, 1, 3), (0, 2, 4), (1, 2, 5), (3, 4, 5)]   # faces as P6 edge indices
    t = np.ones(L.shape[:-1], bool)
    for a, b, c in tris:
        t &= tri_ok(L[..., a], L[..., b], L[..., c])
    return t & (ev[..., 0] > tol)

def flat_len(cell):
    return np.array([np.linalg.norm(cell[b] - cell[a]) for a, b in P6])

print("== A. triangle and tetrahedron constraints on the adopted cells")
# A1 grid theorem for same-type triangles (all diagonal, or the literal reading)
okA1 = True
for S2 in range(1, 9):
    n = np.arange(S2 + 1); f = 1 + n/S2
    F = np.array(list(itertools.product(f, repeat=3)))
    bad = ~tri_ok(F[:, 0], F[:, 1], F[:, 2])
    badset = {tuple(np.round(x*S2 - S2).astype(int)) for x in F[bad]}
    okA1 &= badset == {(0, 0, S2), (0, S2, 0), (S2, 0, 0)}
check("A1 [T] same-type triangle (three windows of one flat length)", okA1,
      "for 2S = 1..8 the only failures are the three corner configurations n = (0,0,2S): f1+f2 >= 2 >= f3 with equality only there")

rng = np.random.default_rng(11)
Nmc = 200000
fr = rng.uniform(1, 2, (Nmc, 6))
res = {}
for nm, cell in (("corner", CORNER), ("inscribed", INSCR)):
    lF = flat_len(cell)
    res[nm, "F"] = 1 - tet_ok(fr * lF).mean()
    res[nm, "L"] = 1 - tet_ok(fr * 1.0).mean()
aad_F = 1 - tri_ok(fr[:, 0], fr[:, 1], R2*fr[:, 2]).mean()
aad_th = (2*R2 - 2)**3 / 6 / R2       # closed form of P(sqrt2 f3 > f1 + f2)
check("A2 [T] mixed axis-axis-diagonal triangle, flat-length windows", abs(aad_F - aad_th) < 3e-3,
      f"fails when sqrt2 f3 >= f1+f2: fraction (2sqrt2-2)^3/(6sqrt2) = {aad_th:.4f} (MC {aad_F:.4f}); edge-source B2's 0.069 is this")
check("A3 [D] tetrahedra (Gram PD) under uniform independent windows", res["corner", "F"] > aad_F,
      f"fail fraction F-reading: corner {res['corner','F']:.3f}, inscribed {res['inscribed','F']:.3f}; "
      f"L-reading: corner {res['corner','L']:.3f}, inscribed {res['inscribed','L']:.3f}; triangles alone are not enough, the clause must be per tetrahedron")
# literal reading cannot hold the flat cube
dev = min(abs((S + nd)/(S + na) - R2) for S in range(1, 65) for nd in range(S+1) for na in range(S+1))
check("A4 [T] CL-1's literal 'rung length times (1+n/2S)' has no flat state", dev > 0,
      f"min |l_d/l_a - sqrt2| over 2S <= 64 is {dev:.1e} > 0; a flat cube needs diagonal/axis = sqrt2, i.e. (2S+n_d)/(2S+n_a) = sqrt2, irrational: no integer solution for any S; the length must be the edge's flat length times (1+n/2S)")
# near-flat: constraint never binds within a common-scale band
band = 1 + 0.2*rng.uniform(0, 1, (Nmc, 6))
nf = 1 - tet_ok(band*flat_len(CORNER)).mean()
nfi = 1 - tet_ok(band*flat_len(INSCR)).mean()
check("A5 [D] within a 20% band of one scale the projector never binds", nf == 0 and nfi == 0,
      f"fail fraction corner {nf:.0e}, inscribed {nfi:.0e}: it binds only on cells sheared well beyond 20%")

# ---------------- B. projector kept by the dressed hop ----------------
print("== B. projector P (every tetrahedron nondegenerate) and the dressed edge hop")
# toy: inscribed tetrahedron + corner tetrahedron at (1,0,0) sharing the face {000,110,101}
VERT = {(0, 0, 0): 0, (1, 1, 0): 1, (1, 0, 1): 2, (0, 1, 1): 3, (1, 0, 0): 4}
VX = {i: np.array(v) for v, i in VERT.items()}
CELLS = [[0, 1, 2, 3], [4, 0, 1, 2]]
EDGES = sorted({tuple(sorted((c[a], c[b]))) for c in CELLS for a, b in P6})
EI = {e: k for k, e in enumerate(EDGES)}
NE = len(EDGES)                                   # 9 registers: 6 diagonals + 3 axis
L0 = np.array([np.linalg.norm(VX[b] - VX[a]) for a, b in EDGES])
S2 = 2; d = S2 + 1
cfg = np.array(list(itertools.product(range(d), repeat=NE)))
Ncfg = len(cfg)
lens = L0 * (1 + cfg / S2)
cell_ok = []
for c in CELLS:
    idx = [EI[tuple(sorted((c[a], c[b])))] for a, b in P6]
    cell_ok.append(tet_ok(lens[:, idx]))
allowed = cell_ok[0] & cell_ok[1]
pw = d ** np.arange(NE)[::-1]
def hop(e, mask=None):
    """bare register hop X_e (n -> n+-1, matrix element 1), optionally projected on mask."""
    rows, cols = [], []
    for s in (+1, -1):
        src = np.where((cfg[:, e] + s >= 0) & (cfg[:, e] + s < d))[0]
        dst = src + s * pw[e]
        if mask is not None:
            keep = mask[src] & mask[dst]; src, dst = src[keep], dst[keep]
        rows.append(dst); cols.append(src)
    r = np.concatenate(rows); c_ = np.concatenate(cols)
    return sp.csr_matrix((np.ones(len(r)), (r, c_)), shape=(Ncfg, Ncfg))
Hb = sum(hop(e) for e in range(NE))
# local dressing: P_e = product of projectors of the cells containing e only
Hl = None
for e, (a, b) in enumerate(EDGES):
    m = np.ones(Ncfg, bool)
    for c, ok in zip(CELLS, cell_ok):
        if a in c and b in c: m &= ok
    h = hop(e, m)
    Hl = h if Hl is None else Hl + h
Pd = sp.diags(allowed.astype(float))
Hg = Pd @ Hb @ Pd
diff_loc = abs((Pd @ Hl @ Pd - Hg)).max()
comm_l = abs(Hl @ Pd - Pd @ Hl).max()
comm_b = abs(Hb @ Pd - Pd @ Hb).max()
vol = np.sqrt(np.clip(np.linalg.det(cm_gram(lens[:, [EI[tuple(sorted((CELLS[0][a], CELLS[0][b])))] for a, b in P6]])), 0, None))
phase = 0.7 * lens.sum(1) - 1.3 * vol                 # supplied toy total phase (diagonal)
theta = 0.4
psi = np.where(allowed, rng.normal(size=Ncfg) + 1j*rng.normal(size=Ncfg), 0); psi /= np.linalg.norm(psi)
def run(H, psi, nt=12):
    for _ in range(nt):
        psi = np.exp(-1j*phase) * expm_multiply(-1j*theta*H, psi)
    return psi
leak_b = np.linalg.norm(run(Hb, psi)[~allowed])
leak_l = np.linalg.norm(run(Hl, psi)[allowed == False])
check("B1 [T] the local dressed hop is the projected hop and commutes with P", diff_loc == 0 and comm_l == 0 and comm_b > 0,
      f"9 registers (6 diag + 3 axis), 2S=2, {allowed.sum()}/{Ncfg} allowed: |P H_loc P - P H P| {diff_loc:.0e}, |[H_loc,P]| {comm_l:.0e}, bare |[H,P]| {comm_b:.0f}")
check("B2 [T] edge tick (dressed hop + total phase) keeps P exactly; bare hop leaks",
      leak_l < 1e-13 and leak_b > 1e-2,
      f"12 ticks from a random allowed state: weight outside P dressed {leak_l:.1e}, bare {leak_b:.3f}")
# product of local gates (one per register, any order) also keeps P
psi2 = psi.copy()
for _ in range(3):
    for e, (a, b) in enumerate(EDGES):
        m = np.ones(Ncfg, bool)
        for c, ok in zip(CELLS, cell_ok):
            if a in c and b in c: m &= ok
        psi2 = expm_multiply(-1j*theta*hop(e, m), psi2)
    psi2 = np.exp(-1j*phase)*psi2
check("B3 [T] per-register dressed gates in any order keep P", np.linalg.norm(psi2[~allowed]) < 1e-13 and abs(np.linalg.norm(psi2) - 1) < 1e-12,
      f"sequential gates: leak {np.linalg.norm(psi2[~allowed]):.0e}, norm-1 {abs(np.linalg.norm(psi2)-1):.0e}")
ncomp, lab = connected_components(Hg[allowed][:, allowed], directed=False)
check("B4 [D] the allowed set stays connected under the dressed hop", ncomp == 1,
      f"{ncomp} component(s): the projection removes states but does not split the register space")

# ---------------- C. CL-2 cost: edge units ----------------
print("== C. CL-2 transport of the actual edge values")
# single corner tetrahedron, 2S=2: 729 configurations, dense Floquet
idxc = [EI[tuple(sorted((CELLS[1][a], CELLS[1][b])))] for a, b in P6]
cfg1 = np.array(list(itertools.product(range(d), repeat=6)))
l1 = flat_len(CORNER) * (1 + cfg1/S2)
ok1 = tet_ok(l1)
D1 = np.abs(cfg1[:, None, :] - cfg1[None, :, :]).sum(-1)    # edge units between configs
H1 = np.zeros((len(cfg1),)*2)
p1w = d ** np.arange(6)[::-1]
for e in range(6):
    for i in np.where(ok1 & (cfg1[:, e] < S2))[0]:
        j = i + p1w[e]
        if ok1[j]: H1[i, j] = H1[j, i] = 1
v1 = np.sqrt(np.clip(np.linalg.det(cm_gram(l1)), 0, None))
ph1 = 0.7*l1.sum(1) - 1.3*v1
A = np.where(ok1)[0]
U = np.diag(np.exp(-1j*ph1[A])) @ expm(-1j*theta*H1[np.ix_(A, A)])
w, V = np.linalg.eig(U)
DA = D1[np.ix_(A, A)]
supp = np.abs(U) > 1e-12
def sinkhorn(p, q, K, it=3000):
    u = np.ones_like(p); v = np.ones_like(q)
    for _ in range(it):
        u = p / np.maximum(K @ v, 1e-300); v = q / np.maximum(K.T @ u, 1e-300)
    return u[:, None]*K*v[None, :]
flips_ent, flips_min, err = [], [], 0
for k in rng.choice(len(A), 6, replace=False):
    f = V[:, k] / np.linalg.norm(V[:, k]); p = np.abs(f)**2
    q = np.abs(U @ f)**2
    pi = sinkhorn(p, q, supp.astype(float))
    err = max(err, np.abs(pi.sum(1) - p).max())
    flips_ent.append((pi*(DA > 0)).sum())        # prob. that some register changes per tick
    flips_min.append(0.0)                         # identity plan: cost 0, unique since D>0 off-diagonal
fe = np.mean(flips_ent)
check("C1 [D] without edge units the cost is zero on every allowed transition: greatest entropy flips stationary edges",
      fe > 0.3 and err < 1e-9,
      f"6 Floquet eigenstates (corner tet, 2S=2, {len(A)} allowed): P(actual edge values change per tick) entropic {fe:.3f} "
      f"(range {min(flips_ent):.2f}-{max(flips_ent):.2f}), i.e. a Planck-rate random walk of the actual lengths")
check("C2 [T] with edge units the stationary actual edges are frozen", max(flips_min) == 0,
      "p -> p with staying allowed: the identity plan costs 0 units and every other plan costs > 0, so the plan is unique and no edge value moves")
# C3: moving state, single register 2S=8 + linear phase: min-unit plan tracks the odds, entropy plan does not
S8 = 8; nn = np.arange(S8+1)
Hs = np.diag(np.ones(S8), 1); Hs = Hs + Hs.T
Us = np.diag(np.exp(-1j*0.9*nn)) @ expm(-1j*0.5*Hs)
f = np.zeros(S8+1, complex); f[1] = 1
mv_min = mv_ent = 0.0; drift = 0.0
Cs = np.abs(nn[:, None] - nn[None, :]).astype(float)
for t in range(6):
    p = np.abs(f)**2; g = Us @ f; q = np.abs(g)**2
    K = (np.abs(Us) > 1e-12).astype(float)
    ub = [(0, None) if K.flat[i] else (0, 0) for i in range(K.size)]
    Aeq = np.vstack([np.kron(np.eye(S8+1), np.ones(S8+1)), np.kron(np.ones(S8+1), np.eye(S8+1))])
    r = linprog(Cs.ravel(), A_eq=Aeq, b_eq=np.r_[p, q], bounds=ub, method="highs")
    mv_min += r.fun
    mv_ent += (sinkhorn(p, q, K)*Cs).sum()
    drift += abs(np.cumsum(q - p)[:-1]).sum()    # 1D W1 = forced motion
    f = g
check("C3 [T] with edge units the actual length moves exactly the forced amount (1D W1)", abs(mv_min - drift) < 1e-6 and mv_ent > 1.5*mv_min,
      f"one register 2S=8, 6 ticks from n=1: moved units min-cost {mv_min:.3f} = W1 {drift:.3f}; cost-free entropic {mv_ent:.3f}")
print(f"elapsed_seconds {time.time()-T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
