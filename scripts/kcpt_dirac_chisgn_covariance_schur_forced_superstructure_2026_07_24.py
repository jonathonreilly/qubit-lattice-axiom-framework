#!/usr/bin/env python3
"""KCPT Dirac-native grading character and the Schur-forced fused-block superstructure.

On the fixed finite L = 4, N = 64 staggered lattice this runner proves the superstructure
behind the Unit-20 measurements, from the bare site construction and the real matrices only:

  T1  The Dirac operator itself defines the grading character.  Conjugating the integer
      antisymmetric adjacency D2 by every one of the 1536 elements h of H yields EXACTLY
      +D2 or -D2 (integer equality); the resulting per-element sign s(h) is a homomorphism
      H -> {+-1} with kernel exactly G_amb, i.e. s = chi_sgn.
  T2  Re-certification (no novelty) of the J_full covariance h J_full h^T = chi_sgn(h) J_full
      in conjugation form, driven by the SAME sign function s.
  T3  A gated twisted-endomorphism census: the twisted diagonal dims are [1,1,1,1,0,0] over
      the six constituents and the twisted cross Hom(12+,12-) = Hom(12-,12+) = 1, while the
      untwisted diagonal dims are [1,1,1,1,1,1] (sum 6 = End_H) and untwisted cross = 0.
  T4  Schur-forced oddness on the fused 24-block: P+ X P+ = P- X P- = 0 for the chi_sgn-
      covariant operators D2 and J_full; {Gam, D24} = {Gam, J24} = 0; rho(H)|24 entirely
      even; even-part span-rank 288 = 12^2 + 12^2 (the Unit-20 288-stall).
  T5  Derivation of the Unit-20 commutator pins: [D2, P+] = -Gam @ D24 exactly, D24^2 = -4 Q24
      forces every one of the 24 nonzero singular values of [D2, P+] to equal 2, hence the
      Unit-20 operator-norm pin ||[D2, P_12+]||_2 = 2; the max-entry anchor 1/(2 sqrt 2) is
      a re-pinned measured lattice-frame value.
  T6  M-block scalars lambda*I with m := -lambda/4 DERIVED from the eigenvalue (multiset
      {0,3,2,2,1,1}); D2 vanishes on the kernel shell; and the Dirac / complex-structure
      block on each chi_sgn-self constituent lies in the 1-dimensional twisted-intertwiner
      line computed independently by the census solver.

ANTI-FABRICATION DISCIPLINE.  Every sign, rank, singular value and commutator norm below is
recomputed from the real integer/float matrices D2, M, J_full, S_eps, the constituent frames
Z and the actual 1536 elements of rho(H) -- never from a comparison target.  Each identity /
completeness gate carries a discriminating rejector or contrast (the S_eps sign rejector at
2*max|D2|; the chi-blind untwisted census that CANNOT reproduce the twisted table; the ind12
central contrast against the non-central fused block).  The block-scalar proportionality
D2 = 2 sqrt(m) * J_bulk shell by shell holds BY CONSTRUCTION of J_bulk and is deliberately NOT
gated as a finding.  Unless a singular value or another norm is named explicitly, every matrix
norm printed below is the entrywise maximum norm ||X||_max = max_ij |X_ij|.  "CP" and "chiral"
are geometric labels for S_eps and the two chi_sgn-graded halves of the real-12 only, never a
statement about Standard-Model CP or chirality.
"""
import itertools
import sys

import numpy as np

L, N = 4, 64
TOL0 = 1e-12       # exact-class float residual
TOL_J = 1e-9       # J_full covariance residual
SV_NULL = 1e-8     # census null-space cut
SV_GAP = 1e-4      # census kept-singular-value floor
TOL_EIG = 1e-8     # holomorphic eigenvector selection (construction)
TOL_COMM = 1e-6    # commutant SVD cut (construction)


def eqm(a, b):
    return np.array_equal(a, b)


# ================= construction (object-identical to the Unit-20 runner) =====================
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


# 5 holomorphic G_amb-idempotents on W (Unit-12 census)
Cgens = [Bh.conj().T @ g.astype(complex) @ Bh for g in gens_G]
dimcW = commutant_dim(Cgens, 32)
BsW = commutant_basis(Cgens, 32, dimcW)
subZW, ranksW, seedW = split_block(Bh, BsW, 32, dimcW)
order = list(np.argsort(ranksW))
subZW = [subZW[i] for i in order]
ranksW = [ranksW[i] for i in order]
PW = [z @ z.conj().T for z in subZW]
PHm = [Seps.astype(complex) @ p @ Seps.astype(complex) for p in PW]

# the SIX CP-completed H-constituents (Unit 14)
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

# ============================= derived objects (Unit-20 conventions) =========================
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
def nrm(A):
    return float(np.max(np.abs(A)))


def bnd(x, tol=TOL0):
    x = abs(float(x))
    return f"<= {tol:.1e}" if x <= tol else f"{x:.6g}"


_P = [0]
_F = [0]


def gate(name, cond, msg):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")
    if ok:
        _P[0] += 1
    else:
        _F[0] += 1


print("[INFO] matrix norm convention: ||X|| means ||X||_max = max_ij |X_ij| unless ||.||_2/SV is named")

# --------- the sign character s from conjugating D2 (integer arithmetic, computed once) -------
s_list = []
viol_sign = 0
for h in Hgrp:
    C = h @ D2 @ h.T
    if eqm(C, D2):
        s_list.append(1)
    elif eqm(C, -D2):
        s_list.append(-1)
    else:
        s_list.append(0)
        viol_sign += 1
s_dict = {h.tobytes(): s_list[k] for k, h in enumerate(Hgrp)}
s_gens = [s_dict[g.tobytes()] for g in gens_H]

# ================================== G01 -- construction sanity ===============================
_g01a = (len(Gamb) == gen_closure_G == 768 and len(Hgrp) == gen_closure_H == 1536)
gate("G01a", _g01a, f"|G_amb|={len(Gamb)} (=768)  |H|={len(Hgrp)} (=1536)")

_maxdev_orth = max(int(np.max(np.abs(h @ h.T - I64i))) for h in Hgrp)
_all_int = all(h.dtype == np.int64 for h in Hgrp)
gate("G01b", _all_int and _maxdev_orth == 0,
     f"all 1536 integer={_all_int}  max_h ||h@h.T - I||_int={_maxdev_orth} (=0, exact orthogonal)")

_seps_in_H = Seps_int.tobytes() in Hset
_seps_not_gamb = Seps_int.tobytes() not in Gamb_set
gate("G01c", _seps_in_H and _seps_not_gamb,
     f"S_eps in H={_seps_in_H}  S_eps in G_amb={not _seps_not_gamb} (must be False)")

_d2_int = (D2.dtype == np.int64)
_d2_anti = eqm(D2.T, -D2)
_evM = np.linalg.eigvalsh(Mf)
_mults = [int(np.sum(np.abs(_evM - v) < 1e-8)) for v in (0.0, -4.0, -8.0, -12.0)]
gate("G01d", _d2_int and _d2_anti and _mults == [8, 24, 24, 8],
     f"D2 integer={_d2_int}  D2^T=-D2 ={_d2_anti}  M-eigs {{0,-4,-8,-12}} mults={_mults} (=[8,24,24,8])")

_j2 = nrm(Jf @ Jf + I64)
gate("G01e", _j2 <= TOL0, f"||J_full^2 + I|| {bnd(_j2)}")

_herm06 = max(nrm(P - P.conj().T) for P in Ps)
_idem06 = max(nrm(P @ P - P) for P in Ps)
_orth06 = max(nrm(Ps[i] @ Ps[j]) for i in range(n) for j in range(n) if i != j)
_sum06 = nrm(sum(Ps) - I64)
_ranks06 = sorted(int(round(np.trace(P).real)) for P in Ps)
_hinv06 = max(nrm(g @ P - P @ g) for g in gens_H_c for P in Ps)
_unit06 = max(
    nrm(
        (Z.conj().T @ g @ Z).conj().T @ (Z.conj().T @ g @ Z)
        - np.eye(Z.shape[1])
    )
    for g in gens_H_c for Z in Zs
)
gate("G01f", _herm06 <= TOL0 and _idem06 <= TOL0 and _orth06 <= TOL0 and _sum06 <= TOL0
     and _ranks06 == [8, 8, 12, 12, 12, 12] and _hinv06 <= TOL0 and _unit06 <= TOL0,
     f"max||P-P^dag|| {bnd(_herm06)}  max||P^2-P|| {bnd(_idem06)}  max||PiPj|| {bnd(_orth06)}  "
     f"||sumP-I|| {bnd(_sum06)}  ranks={_ranks06}  max_gen||[g,P]|| {bnd(_hinv06)}  "
     f"max restricted-unitarity defect {bnd(_unit06)}")

# ============ G02 -- T1: the Dirac operator defines the grading character =====================
gate("G02a", viol_sign == 0,
     f"h@D2@h.T is EXACTLY +-D2 for all 1536 h (integer equality); violations={viol_sign}/1536")

_plus_set = {h.tobytes() for k, h in enumerate(Hgrp) if s_list[k] == 1}
_cplus = len(_plus_set)
_cminus = len(Hgrp) - _cplus
gate("G02b", _plus_set == Gamb_set and _cplus == 768 and _cminus == 768,
     f"s(h)=+1 <=> h in G_amb : {_plus_set == Gamb_set}   counts +1:{_cplus}  -1:{_cminus}")

_s_seps = s_dict[Seps_int.tobytes()]
_dev_seps = nrm((Seps_int @ D2 @ Seps_int.T - D2).astype(float))
gate("G02c", _s_seps == -1 and not eqm(Seps_int @ D2 @ Seps_int.T, D2) and abs(_dev_seps - 2.0) <= TOL0,
     f"rejector: s(S_eps)={_s_seps} (=-1); S_eps@D2@S_eps != +D2, max entry deviation={_dev_seps:.6g} (=2*max|D2|)")

_maxD2 = nrm(D2.astype(float))
gate("G02d", _maxD2 > 0, f"nondegeneracy: max|D2|={_maxD2:.6g} (>0, so the sign is meaningful)")

# ============================= G03 -- multiplicativity of s ==================================
fails03 = 0
count03 = 0
for g in gens_H:
    sg = s_dict[g.tobytes()]
    for h in Hgrp:
        gh = g @ h
        count03 += 1
        if s_dict[gh.tobytes()] != sg * s_dict[h.tobytes()]:
            fails03 += 1
gate("G03a", fails03 == 0,
     f"s(g@h)==s(g)*s(h) over gens_H x H ({len(gens_H)} x {len(Hgrp)} = {count03} products); failures={fails03}")

_kernel = {h.tobytes() for k, h in enumerate(Hgrp) if s_list[k] == 1}
gate("G03b", _kernel == Gamb_set and len(_kernel) == 768,
     f"homomorphism H -> {{+-1}} with kernel exactly G_amb (|ker|={len(_kernel)}=768, ker==G_amb "
     f"{_kernel == Gamb_set}) => s = chi_sgn")

# ==================== G04 -- T2 re-certification: J_full covariance ==========================
_maxres04 = 0.0
viol04 = 0
mism04 = 0
for k, hf in enumerate(Hf):
    conj = hf @ Jf @ hf.T
    res = nrm(conj - s_list[k] * Jf)
    if res > _maxres04:
        _maxres04 = res
    if res > TOL_J:
        viol04 += 1
    sJ = 1 if nrm(conj - Jf) < nrm(conj + Jf) else -1
    if sJ != s_list[k]:
        mism04 += 1
gate("G04a", viol04 == 0 and _maxres04 <= TOL_J,
     f"max_h ||h@J_full@h.T - s(h)*J_full||={_maxres04:.3e} ({bnd(_maxres04, TOL_J)}); violations={viol04}/1536")

gate("G04b", mism04 == 0,
     f"the SAME sign function s from G02 works for J_full: sign mismatches D2-vs-J_full={mism04}/1536")

_dev_j_seps = nrm(Seps @ Jf @ Seps - Jf)
gate("G04c", _dev_j_seps > 0.1,
     f"contrast rejector: for h=S_eps, ||S@J_full@S - J_full||={_dev_j_seps:.6g} (>0.1, the wrong +sign fails loudly)")


# ==================== G05 -- T3: twisted-endomorphism census ================================
def census(i_idx, j_idx, twist):
    """dim {X : R_j(g) X = chi(g) X R_i(g) for all generators g}, with SV-gap certificate.

    Reduces (R_i(g) unitary on the H-invariant constituent) to the eigen-equation
    kron(conj(R_i(g)), R_j(g)) vec(X) = chi(g) vec(X).  chi = s(g) if twist else +1.
    Returns (null_dim, gap_ok, smallest_kept_sv, largest_null_sv, [null X matrices])."""
    Zi, Zj = Zs[i_idx], Zs[j_idx]
    di, dj = Zi.shape[1], Zj.shape[1]
    blocks = []
    for gi, g in enumerate(gens_H_c):
        Ri = Zi.conj().T @ g @ Zi
        Rj = Zj.conj().T @ g @ Zj
        chi = float(s_gens[gi]) if twist else 1.0
        blocks.append(np.kron(np.conj(Ri), Rj) - chi * np.eye(di * dj))
    A = np.vstack(blocks)
    _u, sv, Vh = np.linalg.svd(A, full_matrices=False)
    tot = sv.size
    null_dim = int(np.sum(sv < SV_NULL))
    kept = tot - null_dim
    largest_null = float(sv[kept]) if null_dim > 0 else 0.0
    smallest_ret = float(sv[kept - 1]) if kept > 0 else float("inf")
    gap_ok = (largest_null < SV_NULL) and (smallest_ret > SV_GAP)
    nulls = [np.conj(Vh[kept + t]).reshape(dj, di, order="F") for t in range(null_dim)]
    return null_dim, gap_ok, smallest_ret, largest_null, nulls


census_order = [a8, b8, i_ind12[0], i_ind12[1], i_plus, i_minus]
X0_self = {}
tw_diag = []
tw_gap = True
tw_smallret = []
for idxc in census_order:
    nd, gok, sret, lnull, nulls = census(idxc, idxc, twist=True)
    tw_diag.append(nd)
    tw_gap = tw_gap and gok
    tw_smallret.append(sret)
    if nd == 1:
        X0_self[idxc] = nulls[0]
gate("G05a", tw_diag == [1, 1, 1, 1, 0, 0] and tw_gap,
     f"twisted diagonal dims (ind8,ind8,ind12,ind12,12+,12-)={tw_diag} (=[1,1,1,1,0,0]); "
     f"SV-gap ok={tw_gap} (min kept sv over the four dim-1 blocks="
     f"{min(tw_smallret[i] for i in range(4)):.3g}, SV_NULL={SV_NULL:.0e})")

nd_pm, gok_pm, sret_pm, lnull_pm, _ = census(i_plus, i_minus, twist=True)
gate("G05b", nd_pm == 1 and gok_pm,
     f"twisted Hom(12+,12-)={nd_pm} (=1); largest null sv={lnull_pm:.3g}, smallest kept={sret_pm:.3g}")

nd_mp, gok_mp, sret_mp, lnull_mp, _ = census(i_minus, i_plus, twist=True)
gate("G05c", nd_mp == 1 and gok_mp,
     f"twisted Hom(12-,12+)={nd_mp} (=1); largest null sv={lnull_mp:.3g}, smallest kept={sret_mp:.3g}")

ut_diag = []
ut_gap = True
for idxc in census_order:
    nd, gok, sret, lnull, _ = census(idxc, idxc, twist=False)
    ut_diag.append(nd)
    ut_gap = ut_gap and gok
gate("G05d", ut_diag == [1, 1, 1, 1, 1, 1] and sum(ut_diag) == 6 and ut_gap,
     f"untwisted diagonal dims={ut_diag} (=[1,1,1,1,1,1]), sum={sum(ut_diag)} (=End_H=6); SV-gap ok={ut_gap}")

nd_ut_pm, gok_ut_pm, sret_ut_pm, lnull_ut_pm, _ = census(i_plus, i_minus, twist=False)
gate("G05e", nd_ut_pm == 0 and gok_ut_pm,
     f"untwisted Hom(12+,12-)={nd_ut_pm} (=0); smallest sv={sret_ut_pm:.3g} (>SV_GAP={SV_GAP:.0e})")

_disc = (tw_diag != ut_diag) and (nd_pm == 1 and nd_ut_pm == 0)
gate("G05f", _disc,
     f"discriminator: twisted diag {tw_diag} != untwisted diag {ut_diag}, and twisted cross "
     f"{nd_pm} != untwisted cross {nd_ut_pm} -> the census genuinely depends on chi (a chi-blind "
     f"solver cannot produce both tables)")

# ==================== G06 -- T4: Schur-forced oddness on the fused 24-block ===================
Pp = Ps[i_plus]
Pm = Ps[i_minus]
Q24 = Pp + Pm
Gam = Pp - Pm
D24 = Q24 @ D2f @ Q24
J24 = Q24 @ Jf @ Q24

_off = max(nrm(Pp @ D2f @ Pp), nrm(Pm @ D2f @ Pm), nrm(Pp @ Jf @ Pp), nrm(Pm @ Jf @ Pm))
gate("G06a", _off <= TOL0,
     f"Schur-forced P+/- X P+/- = 0 for X in {{D2,J_full}}: max(||P+D2P+||,||P-D2P-||,||P+JP+||,"
     f"||P-JP-||)={_off:.3e} ({bnd(_off)})")

_ac_d = nrm(Gam @ D24 + D24 @ Gam)
gate("G06b", _ac_d <= TOL0, f"anticommutator ||{{Gam, D24}}||={_ac_d:.3e} ({bnd(_ac_d)})")

_ac_j = nrm(Gam @ J24 + J24 @ Gam)
gate("G06c", _ac_j <= TOL0, f"anticommutator ||{{Gam, J24}}||={_ac_j:.3e} ({bnd(_ac_j)})")

_d24sq = nrm(D24 @ D24 + 4 * Q24)
_j24sq = nrm(J24 @ J24 + Q24)
gate("G06d", _d24sq <= TOL0 and _j24sq <= TOL0,
     f"||D24^2 + 4 Q24||={_d24sq:.3e} ({bnd(_d24sq)})  ||J24^2 + Q24||={_j24sq:.3e} ({bnd(_j24sq)})")

_even = max(nrm(hf @ Gam - Gam @ hf) for hf in Hf)
gate("G06e", _even <= TOL0,
     f"rho(H)|24 entirely EVEN: max_h ||h@Gam - Gam@h||={_even:.3e} ({bnd(_even)})")

Z24 = np.hstack([Zs[i_plus], Zs[i_minus]])   # 64 x 24 orthonormal
rows24 = np.array([(Z24.conj().T @ (hc @ Z24)).ravel() for hc in Hc])   # 1536 x 576
_sv24 = np.linalg.svd(rows24, compute_uv=False)
_smax24 = float(_sv24[0])
r288 = int(np.sum(_sv24 > 1e-8 * _smax24))
_sk288 = float(_sv24[r288 - 1])
_sd288 = float(_sv24[r288]) if r288 < _sv24.size else 0.0
gate("G06f", r288 == 288 and _sk288 > 1e-4 * _smax24 and _sd288 <= 1e-8 * _smax24,
     f"even-part span-rank(rho(H)|24)={r288} (=12^2+12^2=288 < 576); smallest kept sv={_sk288:.3g}, "
     f"largest dropped sv={_sd288:.3g} (SV-gap certified)")

# ==================== G07 -- T5: derivation of the Unit-20 commutator pins ====================
K = D2f @ Pp - Pp @ D2f
_id_k = nrm(K + Gam @ D24)
gate("G07a", _id_k <= TOL0,
     f"exact identity [D2, P_12+] = -Gam @ D24: ||K + Gam@D24||={_id_k:.3e} ({bnd(_id_k)})")

_gram_k = nrm(K.conj().T @ K - 4 * Q24)
svK = np.linalg.svd(K, compute_uv=False)   # 64 singular values
n_near2 = int(np.sum(np.abs(svK - 2.0) <= 1e-9))
n_near0 = int(np.sum(svK <= 1e-9))
sv1 = float(svK[0])
sv24 = float(svK[23])
sv25 = float(svK[24])
gate("G07b", _gram_k <= TOL0 and n_near2 == 24 and n_near0 == 40 and n_near2 + n_near0 == 64,
     f"||K^dag K - 4Q24||={_gram_k:.3e} ({bnd(_gram_k)}); singular values of K: "
     f"{n_near2} within 1e-9 of 2, {n_near0} <= 1e-9 (sv1={sv1:.16g}, "
     f"sv24={sv24:.16g}, sv25={sv25:.3e})")

_maxsv = float(svK[0])
gate("G07c", abs(_maxsv - 2.0) <= TOL0,
     f"external anchor 1 (DERIVED): ||[D2,P_12+]||_2 = max sv(K)={_maxsv:.16g}, |max sv - 2.0|="
     f"{abs(_maxsv - 2.0):.3e} ({bnd(abs(_maxsv - 2.0))})")

_nrmK = nrm(K)
_tgt = 1.0 / (2.0 * np.sqrt(2.0))
gate("G07d", abs(_nrmK - _tgt) <= TOL0,
     f"external anchor 2 (measured lattice-frame, re-pinned): ||[D2,P_12+]||_max={_nrmK:.17g} vs "
     f"1/(2 sqrt 2)={_tgt:.17g}, diff={abs(_nrmK - _tgt):.3e} ({bnd(abs(_nrmK - _tgt))})")

_Pc = Ps[i_ind12[0]]
_comm_ind12 = nrm(D2f @ _Pc - _Pc @ D2f)
gate("G07e", _comm_ind12 <= TOL0,
     f"contrast rejector: an UNFUSED (central) ind12 projector commutes with D2: "
     f"||[D2, P_ind12]||={_comm_ind12:.3e} ({bnd(_comm_ind12)}) -- sharp central-vs-noncentral contrast")

# ==================== G08 -- T6: M-block scalars and twisted-line spanning ====================
lambdas = []
mvals = []
res_scalar = []
res_full_eig = []
for k in range(n):
    Mblk = Zs[k].conj().T @ Mf @ Zs[k]
    d = Zs[k].shape[1]
    lam_k = float(np.trace(Mblk).real / d)
    res_scalar.append(nrm(Mblk - lam_k * np.eye(d)))
    res_full_eig.append(nrm((Mf - lam_k * I64) @ Zs[k]))
    lambdas.append(lam_k)
    mvals.append(-lam_k / 4.0)
_max_res_scalar = max(res_scalar)
_max_res_full_eig = max(res_full_eig)
gate("G08a", _max_res_scalar <= TOL0 and _max_res_full_eig <= TOL0,
     f"each of six M-blocks Z^dag M Z is scalar lambda*I: max residual={_max_res_scalar:.3e} "
     f"({bnd(_max_res_scalar)}); full eigenspace max||(M-lambda I)Z||={_max_res_full_eig:.3e} "
     f"({bnd(_max_res_full_eig)}); lambdas={[round(v, 6) for v in lambdas]}")

m_round = [int(round(v)) for v in mvals]
_m_derived_ok = all(abs(mvals[k] - m_round[k]) <= 1e-9 for k in range(n))
m_multiset_ok = sorted(m_round) == [0, 1, 1, 2, 2, 3]
_ident_ok = (m_round[a8] == 0 and m_round[b8] == 3
             and m_round[i_ind12[0]] == 2 and m_round[i_ind12[1]] == 2
             and m_round[i_plus] == 1 and m_round[i_minus] == 1)
gate("G08b", _m_derived_ok and m_multiset_ok and _ident_ok,
     f"m := -lambda/4 DERIVED: multiset sorted={sorted(m_round)} (=[0,1,1,2,2,3]); "
     f"ind8s->{{{m_round[a8]},{m_round[b8]}}}=(0,3)  ind12s->{{{m_round[i_ind12[0]]},"
     f"{m_round[i_ind12[1]]}}}=(2,2)  12+/-->{{{m_round[i_plus]},{m_round[i_minus]}}}=(1,1)")

_d2_ker = nrm(D2f @ Zs[a8])
gate("G08c", _d2_ker <= TOL0,
     f"m=0 ind8 (kernel shell): ||D2 Z||={_d2_ker:.3e} ({bnd(_d2_ker)}) -- D2 vanishes "
     f"(D2^2=0 there and D2 normal => D2=0)")


def line_fit(blk, X0):
    c = np.vdot(X0, blk) / np.vdot(X0, X0)
    return c, nrm(blk - c * X0)


Jblk_a8 = Zs[a8].conj().T @ Jf @ Zs[a8]
c_a8, resJ_a8 = line_fit(Jblk_a8, X0_self[a8])
gate("G08d", resJ_a8 <= TOL0 and abs(c_a8) > SV_GAP,
     f"m=0 ind8: J_full block spans the twisted line, J_blk = c*X0: residual={resJ_a8:.3e} "
     f"({bnd(resJ_a8)}), |c|={abs(c_a8):.6g} (>SV_GAP={SV_GAP:.0e})")

D2blk_b8 = Zs[b8].conj().T @ D2f @ Zs[b8]
c_b8, resD_b8 = line_fit(D2blk_b8, X0_self[b8])
gate("G08e", resD_b8 <= TOL0 and abs(c_b8) > SV_GAP,
     f"m=3 ind8: D2 block spans the twisted line, D2_blk = c*X0: residual={resD_b8:.3e} "
     f"({bnd(resD_b8)}), |c|={abs(c_b8):.6g} (>SV_GAP={SV_GAP:.0e})")

res_ind12 = []
c_ind12 = []
for k in i_ind12:
    D2blk = Zs[k].conj().T @ D2f @ Zs[k]
    ck, rk = line_fit(D2blk, X0_self[k])
    res_ind12.append(rk)
    c_ind12.append(abs(ck))
gate("G08f", max(res_ind12) <= TOL0 and min(c_ind12) > SV_GAP,
     f"both m=2 ind12s: D2 block spans the twisted line, D2_blk = c*X0: max residual="
     f"{max(res_ind12):.3e} ({bnd(max(res_ind12))}), min|c|={min(c_ind12):.6g} "
     f"(>SV_GAP={SV_GAP:.0e})")

print(f"TOTAL: PASS={_P[0]} FAIL={_F[0]}")
sys.exit(0 if _F[0] == 0 else 1)
