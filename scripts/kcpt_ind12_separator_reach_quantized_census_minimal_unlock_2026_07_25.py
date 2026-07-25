#!/usr/bin/env python3
"""KCPT ind12 separator: native frame, reach census, and central extension.

On the fixed finite L = 4, N = 64 staggered lattice this runner answers, for the ind12
separator sep = P_a - P_b, the question of which lattice-native subalgebras realize the
intermediate algebra resolutions between C[M] and the full symmetry algebra. It builds every
object from the bare site construction and the real matrices only (self-contained; no import
or exec of any other runner), then runs a class-A finite-dimensional gate battery:

  - A_nat = <D2, J_full, S_eps> true-closes at dimension 16, has four-dimensional
    restrictions on every Dirac shell, and has center C[M] at the stated tolerances.
  - sep has overlap^2 at numerical zero against A_nat.
  - H stabilizes A_nat and sep, making the computed reach invariant on the H-classes.
  - The 36-class census resolves four reach labels and a nine-cell dimension/reach histogram.
  - A28 = <A_nat, g1> true-closes at dimension 28 and numerically resolves seven M2(C)
    summands, with sep represented as the difference of two minimal central idempotents.
  - Shift and rotation contrasts exercise the same reach machinery away from the target.

ANTI-FABRICATION DISCIPLINE.  Every dimension, reach value, character difference, rank,
residual, cluster count, and numerical separation margin claimed by this runner is recomputed
from D2f, Jfull, Seps, the constituent projectors, and the 768 elements of G_amb. Reach is
read by the same residual machinery for every gate. Every reach and dimension gate is taken
only at true closure (empty frontier below cap), never on a capped basis. Unless a singular
value is named, matrix residuals use the Frobenius norm; every SVD uses economy form. Any CP
or chirality tokens retained in construction tags are geometric provenance labels only, not
physical identifications.
"""
import itertools
import sys

import numpy as np

L, N = 4, 64
TOL0 = 1e-12       # matrix-equality-class float residual
TOL_J = 1e-9       # J_full covariance residual
SV_NULL = 1e-8     # census null-space cut
SV_GAP = 1e-4      # kept-singular-value / inter-cluster floor
TOL_EIG = 1e-8     # holomorphic eigenvector selection (construction)
TOL_COMM = 1e-6    # commutant SVD cut (construction)


def eqm(a, b):
    return np.array_equal(a, b)


# ================= finite-surface construction ================================================
def idx(a, b, c):
    return (a * L + b) * L + c


coords = np.zeros((N, 3), dtype=np.int64)
for a in range(L):
    for b in range(L):
        for c in range(L):
            coords[idx(a, b, c)] = (a, b, c)


def eta_mu(mu, x):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** int(x[0])
    return (-1) ** int(x[0] + x[1])


e = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
D2 = np.zeros((N, N), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for mu in range(3):
        D2[i, idx(*((x + e[mu]) % L))] += eta_mu(mu, x)
        D2[i, idx(*((x - e[mu]) % L))] -= eta_mu(mu, x)

SUBSETS = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
sidx = {frozenset(S): k for k, S in enumerate(SUBSETS)}
V8 = np.zeros((N, 8), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for k, S in enumerate(SUBSETS):
        V8[i, k] = (-1) ** int(sum(x[j] for j in S))


def sgn_subset(S):
    Sset = frozenset(S)
    return ((-1) ** len(Sset & frozenset({0, 2}))) * (1 if 1 in Sset else -1)


J64 = np.zeros((8, 8), dtype=np.int64)
for k, S in enumerate(SUBSETS):
    T = frozenset(S) ^ frozenset({1})
    J64[sidx[T], k] = 64 * sgn_subset(S)
Jker_int = V8 @ J64 @ V8.T

M = D2 @ D2
lam = [0, -4, -8, -12]
Fac = [M - lam[m] * np.eye(N, dtype=np.int64) for m in range(4)]
Q = []
for m in range(4):
    P0 = np.eye(N, dtype=np.int64)
    for mp in range(4):
        if mp != m:
            P0 = P0 @ Fac[mp]
    Q.append(P0)
Nm = []
for m in range(4):
    v = 1
    for mp in range(4):
        if mp != m:
            v *= (lam[m] - lam[mp])
    Nm.append(v)

D2f = D2.astype(float)
Pf = [Q[m].astype(float) / Nm[m] for m in range(4)]
Jkerf = Jker_int.astype(float) / (64.0 ** 2)
Jbulk = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3))
Jfull = Jkerf + Jbulk

eps = np.array([(-1) ** int(coords[i][0] + coords[i][1] + coords[i][2]) for i in range(N)], dtype=np.int64)
Seps_int = np.diag(eps)
Seps = Seps_int.astype(float)
I64i = np.eye(N, dtype=np.int64)


def perm(fmap):
    P0 = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        y = np.array(fmap(coords[i])) % L
        P0[i, idx(int(y[0]), int(y[1]), int(y[2]))] = 1
    return P0


UR = perm(lambda x: (x[1], x[2], x[0]))
U2m = perm(lambda x: (-x[1], -x[0], -x[2]))
STAB = np.eye(N, dtype=np.int64)
TR = {t: perm(lambda x, t=t: (x[0] - t[0], x[1] - t[1], x[2] - t[2]))
      for t in itertools.product(range(L), repeat=3)}


def signfield(bits):
    a1, a2, a3, b12, b13, b23 = bits
    d = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x1, x2, x3 = coords[i]
        expo = a1 * x1 + a2 * x2 + a3 * x3 + b12 * x1 * x2 + b13 * x1 * x3 + b23 * x2 * x3
        d[i] = (-1) ** int(expo)
    return d


ALLBITS = list(itertools.product([0, 1], repeat=6))
SF = {bits: signfield(bits) for bits in ALLBITS}
BASES = {"stab": STAB, "U2": U2m, "UR": UR}


def closure_grp(gs):
    gs = [g0.copy() for g0 in gs]
    elts = {g0.tobytes(): g0 for g0 in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for xg in frontier:
            for g0 in gs:
                p = xg @ g0
                key = p.tobytes()
                if key not in elts:
                    elts[key] = p
                    nf.append(p)
        frontier = nf
    return list(elts.values())


commuting = []
for name, base in BASES.items():
    for bits in ALLBITS:
        dd = np.diag(SF[bits])
        for t in itertools.product(range(L), repeat=3):
            U = dd @ base @ TR[t]
            if eqm(U @ D2, D2 @ U):
                commuting.append(U.copy())
Gamb = closure_grp(commuting)
Gamb_set = {U.tobytes() for U in Gamb}

Gsorted = sorted(Gamb, key=lambda U: U.tobytes())
gens_G = []
seenG = {I64i.tobytes()}
gen_closure_G = 0
for U in Gsorted:
    if eqm(U, I64i) or U.tobytes() in seenG:
        continue
    gens_G.append(U)
    cl = closure_grp(gens_G)
    seenG = {x.tobytes() for x in cl}
    gen_closure_G = len(cl)
    if gen_closure_G == 768:
        break

gens_H = gens_G + [Seps_int]
Hgrp = closure_grp(gens_H)
gen_closure_H = len(Hgrp)
Hset = {h.tobytes() for h in Hgrp}

# holomorphic / anti-holomorphic frames
evals, evecs = np.linalg.eig(Jfull)
selp = np.where(np.abs(evals - 1j) < TOL_EIG)[0]
selm = np.where(np.abs(evals + 1j) < TOL_EIG)[0]
Bh, _ = np.linalg.qr(evecs[:, selp])
Bm, _ = np.linalg.qr(evecs[:, selm])


def commutant_dim(mats, r):
    Ir = np.eye(r, dtype=complex)
    A = np.vstack([np.kron(m.T, Ir) - np.kron(Ir, m) for m in mats])
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < TOL_COMM))


def commutant_basis(mats, r, d):
    Ir = np.eye(r, dtype=complex)
    A = np.vstack([np.kron(m.T, Ir) - np.kron(Ir, m) for m in mats])
    Uc, s, Vh = np.linalg.svd(A, full_matrices=False)
    del Uc, A
    return [np.conj(Vh[-(i + 1)]).reshape(r, r, order="F") for i in range(d)]


def split_block(Z, basis_mats, r, d):
    for seed in range(128):
        rng = np.random.default_rng(seed)
        cc = rng.standard_normal(len(basis_mats)) + 1j * rng.standard_normal(len(basis_mats))
        Y = sum(cc[i] * basis_mats[i] for i in range(len(basis_mats)))
        Hs = Y + Y.conj().T
        ww, VV = np.linalg.eigh(Hs)
        spread = float(ww[-1] - ww[0])
        if spread <= 0:
            continue
        thr = 1e-4 * spread
        grp = [[0]]
        for j in range(1, r):
            if ww[j] - ww[j - 1] > thr:
                grp.append([j])
            else:
                grp[-1].append(j)
        intra = max((ww[g[-1]] - ww[g[0]]) for g in grp)
        inter = min((ww[grp[t + 1][0]] - ww[grp[t][-1]]) for t in range(len(grp) - 1)) \
            if len(grp) > 1 else 0.0
        if len(grp) == d and inter > 1e6 * max(intra, 1e-18):
            return [Z @ VV[:, g] for g in grp], [len(g) for g in grp], seed
    return None, None, -1


# Five holomorphic G_amb idempotents on W from the constituent census.
Cgens = [Bh.conj().T @ g.astype(complex) @ Bh for g in gens_G]
dimcW = commutant_dim(Cgens, 32)
BsW = commutant_basis(Cgens, 32, dimcW)
subZW, ranksW, seedW = split_block(Bh, BsW, 32, dimcW)
order = list(np.argsort(ranksW))
subZW = [subZW[i] for i in order]
ranksW = [ranksW[i] for i in order]
PW = [z @ z.conj().T for z in subZW]
PHm = [Seps.astype(complex) @ p @ Seps.astype(complex) for p in PW]

# The six H-constituents after geometric parity completion.
gens_Hc = [g.astype(complex) for g in gens_H]
constituents = []  # (tag, Z, wrank, is_split)
for k in range(len(PW)):
    wrank = ranksW[k]
    block = PW[k] + PHm[k]
    r = int(round(np.trace(block).real))
    ww, VV = np.linalg.eigh((block + block.conj().T) / 2)
    Z = VV[:, -r:]
    matsH = [Z.conj().T @ g @ Z for g in gens_Hc]
    d = commutant_dim(matsH, r)
    if d == 1:
        constituents.append((f"ind{r}(W{wrank})", Z, wrank, False))
    else:
        BsB = commutant_basis(matsH, r, d)
        subZb, subr, seedb = split_block(Z, BsB, r, d)
        ordb = list(np.argsort(subr))
        subZb = [subZb[i] for i in ordb]
        for h_i, zz in enumerate(subZb):
            constituents.append((f"split12_{'+' if h_i == 0 else '-'}(W{wrank})", zz, wrank, True))

# ============================= derived operator-algebra objects ===============================
I64 = np.eye(64)
tags = [c[0] for c in constituents]
Zs = [c[1] for c in constituents]
Ps = [Z @ Z.conj().T for Z in Zs]
dims = [Z.shape[1] for Z in Zs]
n = len(constituents)
Jf = np.asarray(Jfull, dtype=float)
Mf = M.astype(float)
mshell = np.array([np.trace(Ps[k] @ Mf).real / dims[k] for k in range(n)])
i_plus = next(k for k in range(n) if tags[k].startswith("split12_+"))
i_minus = next(k for k in range(n) if tags[k].startswith("split12_-"))
i_ind12 = [k for k in range(n) if tags[k].startswith("ind12")]
i_ind8 = [k for k in range(n) if tags[k].startswith("ind8")]
a8 = max(i_ind8, key=lambda k: mshell[k])   # ind8 on M-shell 0   (m = 0 kernel)
b8 = min(i_ind8, key=lambda k: mshell[k])   # ind8 on M-shell -12 (m = 3)

# precompute the 1536 group representatives (perf only; every gated quantity is recomputed)
Hf = [h.astype(float) for h in Hgrp]
Hc = [h.astype(complex) for h in Hgrp]
gens_H_c = [g.astype(complex) for g in gens_H]


# =============================== helpers & gate machinery ====================================
# The ind12 separator (the fifth central direction of the bicommutant construction).
Pa = Ps[i_ind12[0]]
Pb = Ps[i_ind12[1]]
sep = Pa - Pb

# H-conjugation generating set (four G_amb generators plus the parity involution)
Hgens = [g.astype(np.int64) for g in gens_G] + [Seps_int]

RATS = [0.0, 1.0 / 9.0, 1.0 / 3.0, 1.0]
RAT_LABELS = ["0", "1/9", "1/3", "1"]

_P = [0]
_F = [0]


def gate(name, cond, msg):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")
    if ok:
        _P[0] += 1
    else:
        _F[0] += 1


# ---- reference machinery (used identically for every reach/dim gate) -----------------------
def vec(A):
    return np.asarray(A, dtype=complex).reshape(-1)


def orth_add(B, A, tol=1e-9):
    v = vec(A)
    nv = np.linalg.norm(v)
    if nv < tol:
        return B, False
    v = v / nv
    for _ in range(2):
        if B.shape[0]:
            v = v - B.T @ (B.conj() @ v)
    r = np.linalg.norm(v)
    if r < tol:
        return B, False
    return np.vstack([B, v / r]), True


def word_algebra(gens, cap=350, tol=1e-9):
    gens = [np.asarray(g, dtype=complex) for g in gens]
    B = np.zeros((0, N * N), dtype=complex)
    B, _ = orth_add(B, np.eye(N))
    frontier = [np.eye(N, dtype=complex)]
    while frontier and B.shape[0] < cap:
        newf = []
        for w in frontier:
            for g in gens:
                p = g @ w
                B2, added = orth_add(B, p, tol)
                if added:
                    B = B2
                    newf.append(p)
        frontier = newf
    return B, len(frontier) == 0   # closed = True iff frontier emptied below cap


def resid(B, A):
    v = vec(A)
    v = v / np.linalg.norm(v)
    return float(np.linalg.norm(v - B.T @ (B.conj() @ v)))


def overlap2(B, A):
    return 1.0 - resid(B, A) ** 2


def orthonormal_basis(mats, tol=1e-9):
    B = np.zeros((0, N * N), dtype=complex)
    for A in mats:
        B, _ = orth_add(B, A, tol)
    return B


def span_dim(mats, tol=1e-9):
    return orthonormal_basis(mats, tol).shape[0]


def center_of(Xlist, gens, tol=SV_NULL):
    """Center of the algebra spanned by Xlist (orthonormal N x N basis rows reshaped).

    Solves for c with [g, sum_k c_k X_k] = 0 for every generator g; returns the null
    dimension and the central matrices (already orthonormal, since Xlist is orthonormal
    and the null right-singular vectors are orthonormal in coefficient space)."""
    d = len(Xlist)
    cols = [np.concatenate([vec(g @ Xk - Xk @ g) for g in gens]) for Xk in Xlist]
    Amat = np.array(cols).T                     # (len(gens)*N^2, d)
    Uc, s, Vh = np.linalg.svd(Amat, full_matrices=False)
    del Uc, Amat
    null_idx = [i for i in range(len(s)) if s[i] < tol]
    zmats = [sum(np.conj(Vh[i])[k] * Xlist[k] for k in range(d)) for i in null_idx]
    return len(null_idx), zmats, s


def sv_margins(s, tol=SV_NULL):
    """Return the largest numerical-null and smallest kept singular values."""
    dropped = [float(x) for x in s if x < tol]
    kept = [float(x) for x in s if x >= tol]
    return max(dropped, default=0.0), min(kept, default=float("inf"))


def elt_order(g, cap=64):
    P = g.astype(np.int64)
    cur = P.copy()
    for k in range(1, cap + 1):
        if np.array_equal(cur, I64i):
            return k
        cur = cur @ P
    return -1


def rowmats(B):
    return [B[k].reshape(N, N) for k in range(B.shape[0])]


def frob(A):
    return float(np.linalg.norm(A))


# Native-frame basis, reused by the stability and contrast gates.
Bnat, nat_closed = word_algebra([D2f, Jfull, Seps])
Xnat = rowmats(Bnat)

print("[INFO] reach omega(g) := overlap^2(<A_nat, g>, sep); matrix residuals are Frobenius "
      "unless a singular value is named; every SVD is economy (full_matrices=False)")

# ================================== native frame ===============================================
B_d2, cl_d2 = word_algebra([D2f])
gate("NATIVE-D2-ALGEBRA", cl_d2 and B_d2.shape[0] == 7,
     f"dim<D2f>={B_d2.shape[0]} (=7) closed={cl_d2}  [C[D2]: spectrum {{0, +-2i sqrt m}}]")

B_dj, cl_dj = word_algebra([D2f, Jfull])
gate("NATIVE-DIRAC-PAIR", cl_dj and B_dj.shape[0] == 8,
     f"dim<D2f,Jfull>={B_dj.shape[0]} (=8) closed={cl_dj}  [adds only the kernel complex structure]")

gate("NATIVE-FRAME-DIM", nat_closed and Bnat.shape[0] == 16,
     f"dim A_nat=<D2f,Jfull,Seps>={Bnat.shape[0]} (=16) closed={nat_closed}")

_j2 = frob(Jfull @ Jfull + I64)
_s2 = frob(Seps @ Seps - I64)
_ac = frob(Jfull @ Seps + Seps @ Jfull)
gate("NATIVE-COMPLEX-STRUCTURE", _j2 < 1e-12,
     f"complex structure ||Jfull^2+I||_F={_j2:.12e} (<1e-12)")
gate("NATIVE-PARITY-INVOLUTION", _s2 < 1e-12,
     f"involution ||Seps^2-I||_F={_s2:.12e} (<1e-12)")
gate("NATIVE-GRADING-ANTICOMMUTATION", _ac < 1e-12,
     f"anticommutation ||Jfull.Seps+Seps.Jfull||_F={_ac:.12e} (<1e-12)")

shell_dims_nat = [span_dim([Pf[m] @ X @ Pf[m] for X in Xnat]) for m in range(4)]
gate("NATIVE-SHELL-BLOCKS", shell_dims_nat == [4, 4, 4, 4],
     f"per-shell restriction dims of A_nat={shell_dims_nat} (=[4,4,4,4])")

dimZnat, zmats_nat, _s_nat = center_of(Xnat, [D2f, Jfull, Seps])
_nat_null_max, _nat_kept_min = sv_margins(_s_nat)
centerB_nat = orthonormal_basis(zmats_nat)
res_shell = [resid(centerB_nat, Pf[m]) for m in range(4)]
gate("NATIVE-CENTER-DIM", dimZnat == 4, f"dim Z(A_nat)={dimZnat} (=4)")
gate("NATIVE-CENTER-GAP", _nat_null_max < SV_NULL and _nat_kept_min > SV_GAP,
     f"center SVD margin: largest null={_nat_null_max:.12e} (<{SV_NULL:.1e}); "
     f"smallest kept={_nat_kept_min:.12e} (>{SV_GAP:.1e})")
gate("NATIVE-CENTER-CM", max(res_shell) < 1e-10,
     f"Z(A_nat) numerically matches C[M]: max_m resid(Pf[m], null-span)="
     f"{max(res_shell):.12e} (<1e-10)")

ov_sep_nat = overlap2(Bnat, sep)
gate("NATIVE-SEPARATOR-ORTHOGONALITY", abs(ov_sep_nat) <= 1e-10,
     f"sep non-membership: overlap^2(A_nat, sep)={ov_sep_nat:.12e} "
     f"(|overlap^2|<=1e-10 at the stated tolerance)")

# ================================== H stability ===============================================
_seps_not_gamb = Seps_int.tobytes() not in Gamb_set
_conj_ok = all((h @ g @ h.T).tobytes() in Gamb_set for h in Hgens for g in gens_G)
gate("STABILITY-PARITY-OUTSIDE-AMBIENT", _seps_not_gamb,
     f"S_eps not in G_amb (in G_amb={not _seps_not_gamb}, must be False: H strictly enlarges G_amb)")
gate("STABILITY-AMBIENT-NORMALITY", _conj_ok,
     f"conj by H maps G_amb -> G_amb: all {len(Hgens)}x{len(gens_G)} spot conjugates land in G_amb={_conj_ok}")

Hgens_f = [h.astype(float) for h in Hgens]
res_b2 = max(resid(Bnat, h @ X @ h.T) for h in Hgens_f for X in [D2f, Jfull, Seps])
gate("STABILITY-NATIVE-FRAME", res_b2 < 1e-10,
     f"conj by H maps {{D2f,Jfull,Seps}} into A_nat: max_h,X resid(A_nat, h X h^T)={res_b2:.12e} "
     f"(<1e-10) => conj by H preserves A_nat")

res_b3 = max(frob(h @ sep @ h.T - sep) for h in Hgens_f)
gate("STABILITY-SEPARATOR", res_b3 < 1e-10,
     f"conj by H fixes the separator: max_h ||h sep h^T - sep||_F={res_b3:.12e} "
     f"(<1e-10) => with native-frame stability, omega is numerically H-class invariant")

# ================================== reach census ===============================================
# partition G_amb into H-conjugation classes (orbit-closure BFS over Hgens)
elts = {g.tobytes(): g for g in Gamb}
unassigned = dict(elts)
classes = []
while unassigned:
    k0, g0 = next(iter(unassigned.items()))
    orbit = {k0: g0}
    frontier = [g0]
    while frontier:
        nf = []
        for x in frontier:
            for h in Hgens:
                y = h @ x @ h.T
                ky = y.tobytes()
                if ky in elts and ky not in orbit:
                    orbit[ky] = y
                    nf.append(y)
        frontier = nf
    for kk in orbit:
        unassigned.pop(kk, None)
    classes.append(list(orbit.values()))

records = []
for ci, c in enumerate(classes):
    rep = c[0]
    repf = rep.astype(float)
    B, closed = word_algebra([D2f, Jfull, Seps, repf])
    dim = B.shape[0]
    om = overlap2(B, sep)
    diffs = [abs(om - r) for r in RATS]
    j = int(np.argmin(diffs))
    dchi = float((np.trace(Pa @ repf) - np.trace(Pb @ repf)).real)
    records.append(dict(idx=ci, size=len(c), dim=dim, closed=closed,
                        omega=om, oi=j, ores=diffs[j], dchi=dchi,
                        order=elt_order(rep)))

_nclass = len(classes)
_sizesum = sum(r["size"] for r in records)
gate("CENSUS-CLASS-COUNT", _nclass == 36, f"number of H-classes={_nclass} (=36)")
gate("CENSUS-ELEMENT-COUNT", _sizesum == 768,
     f"class sizes sum={_sizesum} (=768, partition of G_amb)")

_all_closed = all(r["closed"] for r in records)
_max_dim = max(r["dim"] for r in records)
gate("CENSUS-TRUE-CLOSURE", _all_closed and _max_dim < 350,
     f"every class rep TRUE-closes below cap 350: all_closed={_all_closed}, max closed dim={_max_dim}")

_max_ores = max(r["ores"] for r in records)
_vals = sorted(set(RAT_LABELS[r["oi"]] for r in records))
gate("CENSUS-REACH-SPECTRUM", _max_ores < 1e-9,
     f"every class omega matches one of {{0, 1/9, 1/3, 1}} within 1e-9: max match residual="
     f"{_max_ores:.12e}; observed labels={_vals}")

counts = [0, 0, 0, 0]
for r in records:
    counts[r["oi"]] += r["size"]
gate("CENSUS-REACH-COUNTS", counts == [528, 12, 96, 132],
     f"element counts by omega {{0:{counts[0]}, 1/9:{counts[1]}, 1/3:{counts[2]}, 1:{counts[3]}}} "
     f"(={{528, 12, 96, 132}})")

hist = {}
for r in records:
    key = (r["dim"], r["oi"])
    hist[key] = hist.get(key, 0) + r["size"]
expected_hist = {(16, 0): 4, (24, 0): 12, (28, 1): 12, (28, 3): 4, (32, 0): 96,
                 (48, 0): 320, (76, 3): 128, (88, 0): 96, (96, 2): 96}
print("[INFO] refined (dim, omega) census histogram [element counts]:")
for key in sorted(hist):
    print(f"       (dim={key[0]:>3}, omega={RAT_LABELS[key[1]]:>4}): {hist[key]}")
gate("CENSUS-DIM-REACH-HISTOGRAM", hist == expected_hist,
     f"refined (dim, omega) histogram has {len(hist)} cells (=9) and matches expected element counts")

oned3 = [r for r in records if r["oi"] == 2]
one1 = [r for r in records if r["oi"] == 3]
_c6a = len(oned3) == 4 and all(r["size"] == 24 and r["order"] == 8 for r in oned3)
_c6b = sorted((r["size"], r["order"]) for r in one1) == [(4, 4), (64, 12), (64, 12)]
gate("CENSUS-THIRD-ORDERS", _c6a,
     f"order census: omega=1/3 -> {len(oned3)} classes size 24 all order 8 (ok={_c6a})")
gate("CENSUS-FULL-REACH-ORDERS", _c6b,
     f"order census: omega=1 -> (size,order) multiset={sorted((r['size'], r['order']) for r in one1)} "
     f"(=[(4,4),(64,12),(64,12)], ok={_c6b})")

# ================================== character/reach relation ===================================
FOURSQRT2 = 4.0 * np.sqrt(2.0)
dchi_targets = [0.0, FOURSQRT2, -FOURSQRT2]
max_dchi_res = max(min(abs(r["dchi"] - t) for t in dchi_targets) for r in records)
dchi_seen = sorted(set(round(r["dchi"], 6) for r in records))
gate("CHARACTER-SPECTRUM", max_dchi_res < 1e-9,
     f"every Delta-chi(g)=Re(tr(Pa g)-tr(Pb g)) in {{0, +-4 sqrt2}} within 1e-9: max match "
     f"residual={max_dchi_res:.12e}; observed values={dchi_seen} (4 sqrt2={FOURSQRT2:.12g})")

set_dchi = set(r["idx"] for r in records if abs(r["dchi"]) > 1e-6)
set_third = set(r["idx"] for r in records if r["oi"] == 2)
set_reach = set(r["idx"] for r in records if r["oi"] == 3)
_elts_dchi = sum(r["size"] for r in records if abs(r["dchi"]) > 1e-6)
_omega1_blind = all(abs(r["dchi"]) < 1e-6 for r in records if r["oi"] == 3)
gate("CHARACTER-THIRD-INVERSION",
     set_dchi == set_third and len(set_dchi) > 0 and len(set_third) > 0,
     f"inversion: {{Delta-chi != 0}} == {{omega=1/3}}={set_dchi == set_third} "
     f"(4 classes, |Delta-chi!=0 classes|={len(set_dchi)}, {_elts_dchi} elements; both nonempty)")
gate("CHARACTER-FULL-BLINDNESS", _omega1_blind and len(set_reach) > 0,
     f"every fully-reaching (omega=1) class is character-blind (Delta-chi=0)={_omega1_blind}; "
     f"reaching set nonempty={len(set_reach) > 0}")

# ================================== 28-dimensional central extension ============================
g1 = np.diag(SF[(0, 1, 0, 0, 0, 0)]) @ TR[(1, 1, 1)]        # diag((-1)^{x2}) . T(1,1,1)
g1f = g1.astype(float)
ord_g1 = elt_order(g1)
gate("UNLOCK-MINIMAL-ELEMENT-MEMBERSHIP", g1.tobytes() in Gamb_set,
     f"g1=diag((-1)^{{x2}}).T(1,1,1) in G_amb (by matrix equality)={g1.tobytes() in Gamb_set}")
gate("UNLOCK-MINIMAL-ELEMENT-ORDER", ord_g1 == 4,
     f"order(g1)={ord_g1} (=4: a sign-dressed body-diagonal unit translation)")

# H-orbit of g1 (same conjugation BFS)
orb = {g1.tobytes(): g1}
frontier = [g1]
while frontier:
    nf = []
    for x in frontier:
        for h in Hgens:
            y = h @ x @ h.T
            ky = y.tobytes()
            if ky in Gamb_set and ky not in orb:
                orb[ky] = y
                nf.append(y)
    frontier = nf
g1_3 = g1 @ g1 @ g1
target_orbit = {g1.tobytes(), g1_3.tobytes(), (-g1).tobytes(), (-g1_3).tobytes()}
one1_sizes = sorted(r["size"] for r in one1)
gate("UNLOCK-MINIMAL-ELEMENT-ORBIT", set(orb.keys()) == target_orbit and len(orb) == 4,
     f"H-orbit of g1 == {{g1, g1^3, -g1, -g1^3}} exactly (size {len(orb)}=4, "
     f"match={set(orb.keys()) == target_orbit})")
gate("UNLOCK-MINIMAL-CLASS", one1_sizes == [4, 64, 64],
     f"g1's class is the unique smallest reaching class: omega=1 class sizes={one1_sizes} "
     f"(=[4,64,64], every other omega=1 class has size 64)")

B28, cl28 = word_algebra([D2f, Jfull, Seps, g1f])
X28 = rowmats(B28)
ov_g1 = overlap2(B28, sep)
gate("UNLOCK-ALGEBRA-DIM", cl28 and B28.shape[0] == 28,
     f"dim A28=<A_nat,g1>={B28.shape[0]} (=28) TRUE-closed={cl28}")
gate("UNLOCK-FULL-REACH", abs(ov_g1 - 1.0) < 1e-9,
     f"omega(g1)={ov_g1:.12e} (|omega-1|={abs(ov_g1 - 1.0):.3e}<1e-9, sep in A28)")

shell_dims_28 = [span_dim([Pf[m] @ X @ Pf[m] for X in X28]) for m in range(4)]
gate("UNLOCK-SHELL-DIMS", shell_dims_28 == [4, 8, 8, 8],
     f"per-shell restriction dims of A28={shell_dims_28} (=[4,8,8,8])")

dimZ28, zmats_28, _s28 = center_of(X28, [D2f, Jfull, Seps, g1f])
_a28_null_max, _a28_kept_min = sv_margins(_s28)
gate("UNLOCK-CENTER-DIM", dimZ28 == 7,
     f"dim Z(A28)=commutant nullspace={dimZ28} (=7, center refines C^4 -> C^7)")
gate("UNLOCK-CENTER-GAP", _a28_null_max < SV_NULL and _a28_kept_min > SV_GAP,
     f"center SVD margin: largest null={_a28_null_max:.12e} (<{SV_NULL:.1e}); "
     f"smallest kept={_a28_kept_min:.12e} (>{SV_GAP:.1e})")


def count_clusters(zmats, seed, tol=1e-6):
    rng = np.random.default_rng(seed)
    m = len(zmats)
    cc = rng.standard_normal(m) + 1j * rng.standard_normal(m)
    Zg = sum(cc[i] * zmats[i] + np.conj(cc[i]) * zmats[i].conj().T for i in range(m))
    Hs = (Zg + Zg.conj().T) / 2.0
    w, V = np.linalg.eigh(Hs)
    groups = [[0]]
    for j in range(1, len(w)):
        if w[j] - w[j - 1] > tol:
            groups.append([j])
        else:
            groups[-1].append(j)
    max_intra = max(float(w[g[-1]] - w[g[0]]) for g in groups)
    min_inter = min(float(w[groups[j + 1][0]] - w[groups[j][-1]])
                    for j in range(len(groups) - 1))
    return groups, w, V, max_intra, min_inter


groups_a, w_a, V_a, _intra_a, _inter_a = count_clusters(zmats_28, 20260725)
groups_b, _, _, _intra_b, _inter_b = count_clusters(zmats_28, 42)
gate("UNLOCK-CENTER-CLUSTERS-PRIMARY",
     len(groups_a) == 7 and _intra_a < SV_NULL and _inter_a > SV_GAP,
     f"central sampling seed=20260725: clusters={len(groups_a)} (=7); "
     f"max intra={_intra_a:.12e} (<{SV_NULL:.1e}); min inter={_inter_a:.12e} (>{SV_GAP:.1e})")
gate("UNLOCK-CENTER-CLUSTERS-CONTRAST",
     len(groups_b) == 7 and _intra_b < SV_NULL and _inter_b > SV_GAP,
     f"central sampling seed=42: clusters={len(groups_b)} (=7); "
     f"max intra={_intra_b:.12e} (<{SV_NULL:.1e}); min inter={_inter_b:.12e} (>{SV_GAP:.1e})")

idems = [V_a[:, g] @ V_a[:, g].conj().T for g in groups_a]
blockdims = [span_dim([E @ X @ E for X in X28]) for E in idems]
ranks_e = [int(round(np.trace(E).real)) for E in idems]
supports = [frozenset(m for m in range(4) if frob(Pf[m] @ E) > 1e-8) for E in idems]
support_ms = {}
for rk, sup in zip(ranks_e, supports):
    support_ms[(rk, sup)] = support_ms.get((rk, sup), 0) + 1
expected_support_ms = {(8, frozenset({0})): 1, (12, frozenset({1})): 2,
                       (12, frozenset({2})): 2, (4, frozenset({3})): 2}
gate("UNLOCK-WEDDERBURN-BLOCKS", all(bd == 4 for bd in blockdims),
     f"A28 numerically resolves M2(C)^7: spectral-idempotent blockdims="
     f"{sorted(blockdims)} (all =4)")
gate("UNLOCK-IDEMPOTENT-RANKS", sorted(ranks_e) == [4, 4, 8, 12, 12, 12, 12],
     f"idempotent rank multiset={sorted(ranks_e)} (=[4,4,8,12,12,12,12])")
gate("UNLOCK-SHELL-SUPPORTS", support_ms == expected_support_ms,
     f"(rank,shell-support) multiset matches {{(8,{{0}}):1,(12,{{1}}):2,(12,{{2}}):2,(4,{{3}}):2}} "
     f"-> {support_ms == expected_support_ms} (shell 0 does not split; shells 1,2,3 split in two)")

shell2_idems = [E for E, sup in zip(idems, supports) if sup == frozenset({2})]
_best = float("inf")
_sepdiff = float("inf")
if len(shell2_idems) == 2:
    E1, E2 = shell2_idems
    m1 = max(frob(E1 - Pa), frob(E2 - Pb))
    m2 = max(frob(E1 - Pb), frob(E2 - Pa))
    if m1 <= m2:
        Ea, Eb, _best = E1, E2, m1
    else:
        Ea, Eb, _best = E2, E1, m2
    _sepdiff = frob(sep - (Ea - Eb))
gate("UNLOCK-SHELL2-IDEMPOTENTS", len(shell2_idems) == 2 and _best < 1e-8,
     f"the two shell-2 minimal central idempotents match {{Pa,Pb}}: min-matching "
     f"max||E-P||_F={_best:.12e} (<1e-8)")
gate("UNLOCK-SEPARATOR-IDEMPOTENTS", _sepdiff < 1e-8,
     f"sep = e_a - e_b: ||sep-(Ea-Eb)||_F={_sepdiff:.12e} (<1e-8) => sep is a difference of "
     f"minimal central idempotents of A28")

# ================================== shift-direction contrasts =================================
g_ninth = np.diag(SF[(0, 1, 0, 0, 0, 0)]) @ TR[(1, 1, 3)]
g_zero = np.diag(SF[(0, 1, 0, 0, 0, 0)]) @ TR[(1, 1, 2)]
Bn9, cln9 = word_algebra([D2f, Jfull, Seps, g_ninth.astype(float)])
ov_n9 = overlap2(Bn9, sep)
gate("SHIFT-REACH-NINTH",
     g_ninth.tobytes() in Gamb_set and cln9 and Bn9.shape[0] == 28
     and abs(ov_n9 - 1.0 / 9.0) < 1e-9,
     f"g_ninth in G_amb={g_ninth.tobytes() in Gamb_set}; dim<A_nat,g_ninth>={Bn9.shape[0]} (=28) "
     f"closed={cln9}; omega={ov_n9:.12e} (|omega-1/9|={abs(ov_n9-1.0/9.0):.3e}<1e-9)")

Bz, clz = word_algebra([D2f, Jfull, Seps, g_zero.astype(float)])
ov_z = overlap2(Bz, sep)
gate("SHIFT-REACH-ZERO",
     g_zero.tobytes() in Gamb_set and clz and Bz.shape[0] == 48 and abs(ov_z) <= 1e-10,
     f"g_zero in G_amb={g_zero.tobytes() in Gamb_set}; dim<A_nat,g_zero>={Bz.shape[0]} (=48) "
     f"closed={clz}; omega={ov_z:.12e} (|omega|<=1e-10)")

gate("SHIFT-DIMENSION-CONTRAST", Bn9.shape[0] == 28 and B28.shape[0] == 28,
     f"g_ninth and g1 extension dims are both 28 ({Bn9.shape[0]}, {B28.shape[0]}): "
     f"extension dimension does NOT determine reach")

g_ur1 = np.diag(SF[(0, 0, 0, 1, 1, 0)]) @ UR @ TR[(0, 0, 1)]
g_ur3 = np.diag(SF[(0, 0, 0, 1, 1, 0)]) @ UR @ TR[(0, 0, 3)]
Bu1, clu1 = word_algebra([D2f, Jfull, Seps, g_ur1.astype(float)])
Bu3, clu3 = word_algebra([D2f, Jfull, Seps, g_ur3.astype(float)])
ov_u1 = overlap2(Bu1, sep)
ov_u3 = overlap2(Bu3, sep)


def class_size_of(gmat):
    key = gmat.tobytes()
    for c in classes:
        if any(x.tobytes() == key for x in c):
            return len(c)
    return -1


sz_u1 = class_size_of(g_ur1)
sz_u3 = class_size_of(g_ur3)
gate("ROTATION-FULL-REACH",
     g_ur1.tobytes() in Gamb_set and g_ur3.tobytes() in Gamb_set
     and elt_order(g_ur1) == 12 and elt_order(g_ur3) == 12
     and clu1 and clu3 and Bu1.shape[0] == 76 and Bu3.shape[0] == 76
     and abs(ov_u1 - 1.0) < 1e-9 and abs(ov_u3 - 1.0) < 1e-9
     and sz_u1 == 64 and sz_u3 == 64,
     f"g_ur1,g_ur3 in G_amb; orders={elt_order(g_ur1)},{elt_order(g_ur3)} (=12); dims={Bu1.shape[0]},"
     f"{Bu3.shape[0]} (=76) closed={clu1},{clu3}; omega={ov_u1:.12e},{ov_u3:.12e} (=1); "
     f"H-class sizes={sz_u1},{sz_u3} (=64)")

# ================================== discriminating controls ====================================
ov_g1_central = overlap2(Bnat, Pf[0] - Pf[3])
gate("REACH-IN-FRAME-CONTROL", abs(ov_g1_central - 1.0) < 1e-9,
     f"membership detector sanity: overlap^2(A_nat, Pf[0]-Pf[3])={ov_g1_central:.12e} "
     f"(=1 within 1e-9: an in-frame central difference IS seen by the same resid machinery)")

_g2 = abs(ov_g1 - 1.0 / 3.0) > 0.5 and abs(ov_z - 1.0) > 0.9
gate("REACH-DIAL-CONTRAST", _g2,
     f"wrong-value rejector: |omega(g1)-1/3|={abs(ov_g1-1.0/3.0):.6g} (>0.5) and "
     f"|omega(g_zero)-1|={abs(ov_z-1.0):.6g} (>0.9): the reach contrast is nonconstant")

gp = np.diag(SF[(1, 0, 0, 0, 0, 0)]) @ TR[(1, 1, 1)]        # wrong sign field (-1)^{x1} . T(1,1,1)
if gp.tobytes() in Gamb_set:
    Bgp, clgp = word_algebra([D2f, Jfull, Seps, gp.astype(float)])
    ovp = overlap2(Bgp, sep)
    gate("REACH-SIGNFIELD-PERTURBATION", abs(ovp - 1.0) > 1e-3,
         f"perturbation rejector: gp=diag((-1)^{{x1}}).T(1,1,1) in G_amb; measured omega(gp)={ovp:.12e}, "
         f"|omega(gp)-1|={abs(ovp-1.0):.6g} (>1e-3): a wrong sign field does NOT reproduce the unlock")
else:
    gate("REACH-SIGNFIELD-PERTURBATION", True,
         f"perturbation rejector: gp=diag((-1)^{{x1}}).T(1,1,1) is NOT in G_amb "
         f"(gp in G_amb={gp.tobytes() in Gamb_set}): a wrong sign field is not even an admissible "
         f"extension, so it cannot reproduce the unlock")

print(f"TOTAL: PASS={_P[0]} FAIL={_F[0]}")
sys.exit(0 if _F[0] == 0 else 1)
