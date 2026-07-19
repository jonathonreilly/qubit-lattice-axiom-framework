#!/usr/bin/env python3
"""KCPT bulk-block eigenvalue stratification: Hamming shells, the ker-pi carrier,
and adjacency-native complex structures.

Class-A finite check on the fixed 4^3 staggered surface. The staggered adjacency
D2, the corner-wave kernel frame V8, and the ambient D2-commuting dressed closure
G_amb of order 768 are rebuilt from the construction (machinery copied from the
landed ambient runner). The eigenvalue strata of M = D2 @ D2 are resolved by exact
integer projectors, the per-shell commutant dimensions e_m, cross terms h_{m,m'},
and Frobenius-Schur indicators nu_m are recomputed as exact character sums (Fraction)
over the regenerated 768 members acting on the stratum projectors -- never hardcoded
-- and the adjacency-native antisymmetric operators D2 Q_m are exhibited and their
invariant span tested with an explicit non-invariant rejector. Every load-bearing
gate uses exact integer numpy (int64, with Python-int / Fraction arithmetic for the
character sums and sesquilinear values) or exact sympy rank; no floating point enters
any gate. Each gate prints one line; the script prints a final TOTAL line and exits
nonzero on any failure.
"""
import os
import re
import sys
import itertools
from fractions import Fraction
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------
# Bookkeeping
# ----------------------------------------------------------------------------
PASS = 0
FAIL = 0


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {'PASS' if ok else 'FAIL'} - {desc}")
    return ok


def eqm(a, b):
    return np.array_equal(a, b)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")

# ----------------------------------------------------------------------------
# Construction (transcribed verbatim from the landed surface / ambient runner)
# ----------------------------------------------------------------------------
L = 4
N = 64


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
HW = [len(S) for S in SUBSETS]
V8 = np.zeros((N, 8), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for k, S in enumerate(SUBSETS):
        V8[i, k] = (-1) ** int(sum(x[j] for j in S))


def perm(fmap):
    P = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        y = np.array(fmap(coords[i])) % L
        P[i, idx(int(y[0]), int(y[1]), int(y[2]))] = 1
    return P


UR = perm(lambda x: (x[1], x[2], x[0]))
U2 = perm(lambda x: (-x[1], -x[0], -x[2]))
STAB = np.eye(N, dtype=np.int64)
TR = {t: perm(lambda x, t=t: (x[0] - t[0], x[1] - t[1], x[2] - t[2]))
      for t in itertools.product(range(L), repeat=3)}

I64 = np.eye(N, dtype=np.int64)
ZERO = np.zeros((N, N), dtype=np.int64)
eye8 = np.eye(8, dtype=np.int64)


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
BASES = {"stab": STAB, "U2": U2, "UR": UR}


def closure_amb(gs):
    gs = [g.copy() for g in gs]
    elts = {g.tobytes(): g for g in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for xg in frontier:
            for g in gs:
                p = xg @ g
                key = p.tobytes()
                if key not in elts:
                    elts[key] = p
                    nf.append(p)
        frontier = nf
    return list(elts.values())


def perm_sign(U):
    cols = np.argmax(np.abs(U), axis=1)
    signs = U[np.arange(N), cols]
    return cols, signs


def conj_sp(cols, signs, A):
    # (U A U^T)[a,b] = signs[a] signs[b] A[cols[a], cols[b]] for signed-perm U
    return A[np.ix_(cols, cols)] * np.outer(signs, signs)


def trUQ(U, Q):
    # tr(U @ Q) == sum_{i,j} U[i,j] Q[j,i] == sum(U * Q.T); entries are small integers
    return int(np.multiply(U, Q.T).sum())


def proportional(A, B):
    # exact: True iff A and B are linearly dependent (A == r B for rational r, or A == 0)
    A = A.astype(object)
    B = B.astype(object)
    nz = np.argwhere(B != 0)
    if len(nz) == 0:
        return bool(np.all(A == 0))
    i0, j0 = nz[0]
    num = A[i0, j0]
    den = B[i0, j0]
    return bool(np.all(A * den == num * B))


# ============================================================================
# B1 - construction anchored to the landed surface
# ============================================================================
gate("B1.1", eqm(D2, -D2.T) and set(np.unique(D2)).issubset({-1, 0, 1}),
     "D2 integer, antisymmetric (D2 == -D2.T), entries in {-1,0,1}")
gate("B1.2", sp.Matrix(D2.tolist()).rank() == 56,
     "exact rank(D2) == 56 via sympy (kernel dimension 8)")
gate("B1.3", eqm(D2 @ V8, np.zeros((N, 8), dtype=np.int64)),
     "D2 @ V8 == 0 exactly")
gate("B1.4", eqm(V8.T @ V8, 64 * eye8),
     "V8.T @ V8 == 64 * I8 exactly")
gate("B1.5", HW == [0, 1, 1, 1, 2, 2, 2, 3]
     and [HW.count(w) for w in (0, 1, 2, 3)] == [1, 3, 3, 1],
     "Hamming-weight grading of the kernel frame == 1 + 3 + 3 + 1")

# ============================================================================
# B2 - the ker-pi carrier identity (result 1)
# ============================================================================
M = D2 @ D2
carrier = 2 * (TR[(2, 0, 0)] + TR[(0, 2, 0)] + TR[(0, 0, 2)]) - 6 * I64
gate("B2.1", eqm(M, M.T),
     "M = D2 @ D2 is symmetric (D2 antisymmetric)")
gate("B2.2", eqm(M, carrier),
     "carrier identity: M == 2*(T_200 + T_020 + T_002) - 6*I exactly")
gate("B2.3", not eqm(M, 2 * (TR[(2, 0, 0)] + TR[(0, 2, 0)] + TR[(0, 0, 2)]) - 5 * I64)
     and not eqm(M, 2 * (TR[(1, 0, 0)] + TR[(0, 2, 0)] + TR[(0, 0, 2)]) - 6 * I64),
     "rejectors: the -6 diagonal and the even-shift T_200 are both pinned")
even_tr = [TR[t] for t in itertools.product([0, 2], repeat=3)]
gate("B2.4", all(eqm(M @ T, T @ M) for T in even_tr),
     "M commutes with every even translation (the (Z/2)^3 ker-pi carrier)")

# ============================================================================
# B3 - minimal polynomial, strata, projectors (result 2)
# ============================================================================
lam = [0, -4, -8, -12]
Fac = [M - lam[m] * I64 for m in range(4)]
minpoly = Fac[0] @ Fac[1] @ Fac[2] @ Fac[3]
gate("B3.1", eqm(minpoly, ZERO),
     "minimal polynomial M(M+4I)(M+8I)(M+12I) == 0 exactly")

Q = []
for m in range(4):
    P = I64.copy()
    for mp in range(4):
        if mp != m:
            P = P @ Fac[mp]
    Q.append(P)
drop_nonzero = all(not eqm(Q[m], ZERO) for m in range(4))
gate("B3.2", drop_nonzero,
     "every drop-one product Q_m = prod_{m'!=m}(M - lambda_m' I) is nonzero")

Nm = []
for m in range(4):
    v = 1
    for mp in range(4):
        if mp != m:
            v *= (lam[m] - lam[mp])
    Nm.append(v)
gate("B3.3", Nm == [384, -128, 128, -384],
     f"normalizers N_m = prod(lambda_m - lambda_m') == {Nm}")
gate("B3.4", all(eqm(M @ Q[m], lam[m] * Q[m]) for m in range(4)),
     "eigen-projector action: M Q_m == lambda_m Q_m for all m")
gate("B3.5", all(eqm(Q[m] @ Q[m], Nm[m] * Q[m]) for m in range(4)),
     "idempotence up to scale: Q_m^2 == N_m Q_m for all m")
gate("B3.6", all(eqm(Q[m] @ Q[mp], ZERO) for m in range(4) for mp in range(4) if m != mp),
     "orthogonality: Q_m Q_m' == 0 for m != m'")
gate("B3.7", eqm(Q[0] - 3 * Q[1] + 3 * Q[2] - Q[3], 384 * I64)
     and not eqm(Q[0] - 3 * Q[1] + 3 * Q[2] - Q[3], 383 * I64),
     "partition of unity: Q_0 - 3Q_1 + 3Q_2 - Q_3 == 384 I (coefficient pinned)")
gate("B3.8", all(eqm(Q[m], Q[m].T) for m in range(4)),
     "each Q_m is real symmetric")
# stratum dims are COMPUTED from tr Q_m / N_m, then checked (not hardcoded first)
dm = []
tr_ok = True
for m in range(4):
    tq = int(np.trace(Q[m]))
    if tq % Nm[m] != 0:
        tr_ok = False
        dm.append(None)
    else:
        dm.append(tq // Nm[m])
gate("B3.9", tr_ok and dm == [8, 24, 24, 8],
     f"stratum dims from tr Q_m / N_m == {dm} (expected 8,24,24,8)")
gate("B3.10", eqm(Q[0], 6 * (V8 @ V8.T)),
     "kernel projector matches corner frame: Q_0 == 6 * V8 @ V8.T")
bulk_rank = (sp.Matrix(Q[1].tolist()).rank()
             + sp.Matrix(Q[2].tolist()).rank()
             + sp.Matrix(Q[3].tolist()).rank())
gate("B3.11", bulk_rank == 56 and (dm[1] + dm[2] + dm[3]) == 56,
     f"bulk rank rank(Q_1)+rank(Q_2)+rank(Q_3) == {bulk_rank} == 24+24+8 == rank D2")

print(f"[info] stratum dims d_m = {dm}")

# ============================================================================
# B4 - momentum diagonalization and the K-geometry (result 3)
# ============================================================================
I_RE = [1, 0, -1, 0]
I_IM = [0, 1, 0, -1]


def wave(k):
    re = np.zeros(N, dtype=np.int64)
    im = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x = coords[i]
        r = int((k[0] * x[0] + k[1] * x[1] + k[2] * x[2]) % 4)
        re[i] = I_RE[r]
        im[i] = I_IM[r]
    return re, im


def mval(k):
    return int((k[0] % 2) + (k[1] % 2) + (k[2] % 2))


allk = list(itertools.product(range(4), repeat=3))
eig_ok = True
wave_norm_ok = True
for k in allk:
    wr, wi = wave(k)
    lm = -4 * mval(k)
    if not eqm(M @ wr, lm * wr) or not eqm(M @ wi, lm * wi):
        eig_ok = False
    if int(wr @ wr + wi @ wi) != N:
        wave_norm_ok = False
gate("B4.1", eig_ok and wave_norm_ok,
     "every nonzero unit-modulus momentum wave phi_k is an M-eigenvector at lambda = -4 m(k) (re and im parts)")
re10, im10 = wave((1, 0, 0))
gate("B4.2", eqm(M @ re10, -4 * re10) and not eqm(M @ re10, ZERO[:, 0])
     and not eqm(M @ re10, -8 * re10) and np.any(re10 != 0),
     "wrong-eigenvalue rejector: M phi_(1,0,0) == -4 phi, not 0 and not -8 phi")
counts = [sum(1 for k in allk if mval(k) == m) for m in range(4)]
gate("B4.3", counts == [8, 24, 24, 8],
     f"per-stratum momentum counts == {counts} (== stratum dims d_m)")
gate("B4.4", all(mval(tuple((-ki) % 4 for ki in k)) == mval(k) for k in allk),
     "K: k -> -k (mod 4) preserves every stratum, m(-k) == m(k)")
fixedK = [k for k in allk if tuple((-ki) % 4 for ki in k) == k]
gate("B4.5", len(fixedK) == 8 and all(mval(k) == 0 for k in fixedK),
     "K fixes exactly the 8 kernel (m=0) momenta")
bulk = [k for k in allk if mval(k) >= 1]
bulk_fpf = all(tuple((-ki) % 4 for ki in k) != k for k in bulk)
pairs = set()
for k in bulk:
    kk = tuple((-ki) % 4 for ki in k)
    pairs.add(frozenset((k, kk)))
gate("B4.6", len(bulk) == 56 and bulk_fpf and len(pairs) == 28,
     "K is fixed-point-free on the 56 bulk momenta (28 conjugate pairs)")

# ============================================================================
# B5 - ker-pi isotypic blocks (result 4)
# ============================================================================
EPS = list(itertools.product([0, 1], repeat=3))
R8 = {}
for eps in EPS:
    S = np.zeros((N, N), dtype=np.int64)
    for b in itertools.product([0, 1], repeat=3):
        t = (2 * b[0], 2 * b[1], 2 * b[2])
        sgn = (-1) ** int(eps[0] * b[0] + eps[1] * b[1] + eps[2] * b[2])
        S = S + sgn * TR[t]
    R8[eps] = S
block_ok = True
for m in range(4):
    rhs = np.zeros((N, N), dtype=np.int64)
    for eps in EPS:
        if sum(eps) == m:
            rhs = rhs + R8[eps]
    if not eqm(8 * Q[m], Nm[m] * rhs):
        block_ok = False
gate("B5.1", block_ok,
     "block resolution: 8 Q_m == N_m * sum_{wt(eps)=m} R8_eps for all m")
rhs_wrong = np.zeros((N, N), dtype=np.int64)
for eps in EPS:
    if sum(eps) == 2:
        rhs_wrong = rhs_wrong + R8[eps]
gate("B5.2", not eqm(8 * Q[1], Nm[1] * rhs_wrong),
     "wrong-weight rejector: 8 Q_1 != N_1 * sum_{wt(eps)=2} R8_eps")

# ============================================================================
# B6 - regenerate the ambient group G_amb (order 768) (result setup)
# ============================================================================
commuting = {}
for name, base in BASES.items():
    lst = []
    for bits in ALLBITS:
        dd = np.diag(SF[bits])
        for t in itertools.product(range(L), repeat=3):
            U = dd @ base @ TR[t]
            if eqm(U @ D2, D2 @ U):
                lst.append(U.copy())
    commuting[name] = lst
per_class = {n: len(commuting[n]) for n in BASES}
amb_scan = [U for n in BASES for U in commuting[n]]
gate("B6.1", sum(per_class.values()) == 192 and all(v == 64 for v in per_class.values()),
     f"scan keeps 192 D2-commuting members, 64 per class ({per_class})")
Gamb = closure_amb(amb_scan)
gate("B6.2", len(Gamb) == 768 and len(set(U.tobytes() for U in Gamb)) == 768,
     "BFS closure of the 192 has order exactly 768, all distinct")
gate("B6.3", all(eqm(U @ D2, D2 @ U) for U in Gamb),
     "every one of the 768 commutes with D2 exactly")
gate("B6.4", all(eqm(U @ U.T, I64) for U in Gamb),
     "orthogonality: U U^T == I64 for all 768 (signed permutations)")
COLS = []
SIGNS = []
for U in Gamb:
    c, s = perm_sign(U)
    COLS.append(c)
    SIGNS.append(s)
sp_ok = True
for u in range(0, 768, 97):
    if not eqm(conj_sp(COLS[u], SIGNS[u], M), Gamb[u] @ M @ Gamb[u].T):
        sp_ok = False
gate("B6.5", sp_ok,
     "signed-perm representation self-check: conj_sp == dense U M U^T (sampled)")

# every ambient member commutes with M (hence with each Q_m, a polynomial in M)
gate("B6.6", all(eqm(U @ M, M @ U) for U in Gamb)
     and all(eqm(U @ Q[m], Q[m] @ U) for U in Gamb for m in range(4)),
     "every ambient member commutes with M and with every Q_m")

# ker-pi blocks are permuted by axis permutation, weight-preserving; orbits {1,3,3,1}
key_to_eps = {R8[eps].tobytes(): eps for eps in EPS}
perm_ok = True
weight_ok = True
edges = {eps: set() for eps in EPS}
for u in range(768):
    for eps in EPS:
        img = conj_sp(COLS[u], SIGNS[u], R8[eps])
        kk = img.tobytes()
        if kk not in key_to_eps:
            perm_ok = False
            continue
        eps2 = key_to_eps[kk]
        edges[eps].add(eps2)
        if sum(eps2) != sum(eps):
            weight_ok = False
gate("B6.7", perm_ok and weight_ok,
     "G_amb conjugation permutes the 8 ker-pi blocks, preserving Hamming weight")
# orbits from the collected edges
seen = set()
orbit_sizes = []
for eps in EPS:
    if eps in seen:
        continue
    stack = [eps]
    comp = set()
    while stack:
        y = stack.pop()
        if y in comp:
            continue
        comp.add(y)
        for z in edges[y]:
            if z not in comp:
                stack.append(z)
    seen |= comp
    orbit_sizes.append(len(comp))
gate("B6.8", sorted(orbit_sizes) == [1, 1, 3, 3],
     f"block orbits are exactly the weight classes, sizes {sorted(orbit_sizes)} == 1,3,3,1")

# ============================================================================
# B7 - bulk commutant resolution by exact character sums (result 5, headline)
# ============================================================================
G = 768
tr_all = [[trUQ(U, Q[m]) for U in Gamb] for m in range(4)]
U2_list = [U @ U for U in Gamb]
tr2_all = [[trUQ(U2, Q[m]) for U2 in U2_list] for m in range(4)]

e_val = []
for m in range(4):
    S = sum(t * t for t in tr_all[m])
    fr = Fraction(S, G * Nm[m] ** 2)
    e_val.append(fr)
gate("B7.1", all(fr.denominator == 1 for fr in e_val),
     "commutant character sums e_m are exact integers (768 N_m^2 divides the sum)")
e_int = [int(fr) for fr in e_val]
gate("B7.2", e_int == [2, 4, 4, 2],
     f"per-stratum commutant dims e_m == {e_int} (computed by character sum)")

h_val = {}
h_zero = True
for m in range(4):
    for mp in range(m + 1, 4):
        S = sum(tr_all[m][i] * tr_all[mp][i] for i in range(G))
        fr = Fraction(S, G * Nm[m] * Nm[mp])
        h_val[(m, mp)] = fr
        if fr != 0:
            h_zero = False
gate("B7.3", h_zero,
     "all cross terms h_{m,m'} == 0 (strata share no equivariant maps)")
gate("B7.4", e_int[1] + e_int[2] + e_int[3] == 10 and (e_int[1], e_int[2], e_int[3]) == (4, 4, 2),
     "the parent's ten on the image block resolves as 10 = 4 + 4 + 2")
gate("B7.5", e_int[0] == 2,
     "the kernel shell keeps e_0 == 2 (matching span{I, j})")
total = sum(e_int) + 2 * sum(int(v) for v in h_val.values())
gate("B7.6", total == 12,
     f"reconciliation: sum_m e_m + 2 sum_{{m<m'}} h == {total} == parent total 12")
# subgroup rejector: restricting the group to the 8 ker-pi translations changes e_1
kerpi_mats = even_tr
S_sub = sum(trUQ(T, Q[1]) ** 2 for T in kerpi_mats)
e1_sub = Fraction(S_sub, len(kerpi_mats) * Nm[1] ** 2)
gate("B7.7", e1_sub == 192 and e1_sub != e_val[1],
     f"group-is-load-bearing rejector: e_1 over the 8 ker-pi translations == {e1_sub} != 4")

print(f"[info] commutant dims e_m = {e_int}")
print(f"[info] cross terms h_(m,m') = {{ {', '.join(f'{k}: {int(v)}' for k, v in h_val.items())} }}")

# ============================================================================
# B8 - Frobenius-Schur classification (result 6)
# ============================================================================
nu_val = []
for m in range(4):
    S = sum(tr2_all[m])
    fr = Fraction(S, G * Nm[m])
    nu_val.append(fr)
gate("B8.1", all(fr.denominator == 1 for fr in nu_val),
     "Frobenius-Schur sums nu_m are exact integers (768 N_m divides the sum)")
nu_int = [int(fr) for fr in nu_val]
gate("B8.2", nu_int == [0, 2, 0, 0],
     f"Frobenius-Schur indicators nu_m == {nu_int} (computed by character sum)")
a_m = [(e_int[m] - nu_int[m]) for m in range(4)]
s_m = [(e_int[m] + nu_int[m]) for m in range(4)]
half_ok = all(a % 2 == 0 for a in a_m) and all(s % 2 == 0 for s in s_m)
a_m = [a // 2 for a in a_m]
s_m = [s // 2 for s in s_m]
gate("B8.3", half_ok and a_m == [1, 1, 2, 1],
     f"invariant antisymmetric dims a_m = (e_m - nu_m)/2 == {a_m}")
gate("B8.4", half_ok and s_m == [1, 3, 2, 1],
     f"invariant symmetric dims s_m = (e_m + nu_m)/2 == {s_m}")
gate("B8.5", all(a_m[m] + s_m[m] == e_int[m] and s_m[m] - a_m[m] == nu_int[m] for m in range(4))
     and all(a_m[m] >= 0 and s_m[m] >= 0 for m in range(4)),
     "consistency: a_m + s_m == e_m, s_m - a_m == nu_m, all nonnegative")

print(f"[info] Frobenius-Schur nu_m = {nu_int}")
print(f"[info] invariant antisymmetric dims a_m = {a_m}")
print(f"[info] invariant symmetric dims s_m = {s_m}")

# ============================================================================
# B9 - adjacency-native complex structures (result 7)
# ============================================================================
DQ = [D2 @ Q[m] for m in range(4)]
gate("B9.1", all(eqm(D2 @ Q[m], Q[m] @ D2) for m in range(4)),
     "D2 commutes with every Q_m (it is a polynomial in M = D2^2)")
gate("B9.2", eqm(DQ[0], ZERO),
     "D2 Q_0 == 0: the adjacency vanishes on the kernel stratum")
gate("B9.3", all((not eqm(DQ[m], ZERO)) and eqm(DQ[m].T, -DQ[m]) for m in (1, 2, 3)),
     "each D2 Q_m (m >= 1) is a nonzero real antisymmetric operator")


def invariant(A):
    return all(eqm(conj_sp(COLS[u], SIGNS[u], A), A) for u in range(768))


gate("B9.4", all(invariant(DQ[m]) for m in (1, 2, 3)),
     "each D2 Q_m (m >= 1) commutes with all 768 ambient members")
gate("B9.5", all(eqm(DQ[m] @ DQ[m], -4 * m * Nm[m] * Q[m]) for m in range(4)),
     "square identity: (D2 Q_m)^2 == -4 m N_m Q_m for all m")

# span-membership discriminator on shell 1 (a_1 == 1, so the invariant
# antisymmetric axis is exactly span(D2 Q_1)).
u0 = np.zeros(N, dtype=np.int64); u0[0] = 1
u1 = np.zeros(N, dtype=np.int64); u1[1] = 1
K0 = np.outer(u0, u1) - np.outer(u1, u0)


def avg_of(A):
    acc = np.zeros((N, N), dtype=np.int64)
    for u in range(768):
        acc = acc + conj_sp(COLS[u], SIGNS[u], A)
    return acc


Seed1 = Q[1] @ K0 @ Q[1]
Zpert = DQ[1] + Seed1
gate("B9.6", a_m[1] == 1 and invariant(DQ[1]) and not eqm(DQ[1], ZERO),
     "shell 1 is adjacency-pinned: a_1 == 1 and D2 Q_1 is a nonzero invariant axis")
gate("B9.7", (not eqm(Seed1, ZERO)) and eqm(Zpert.T, -Zpert)
     and (not invariant(Seed1)) and (not proportional(Zpert, DQ[1])),
     "rejector: the perturbed non-invariant antisymmetric Zpert fails span(D2 Q_1)")
AvgZpert = avg_of(Zpert)
gate("B9.8", (not eqm(AvgZpert, ZERO)) and proportional(AvgZpert, DQ[1]),
     "group-average of Zpert lands back in span(D2 Q_1) (invariant axis restored)")
gate("B9.9", a_m[3] == 1 and invariant(DQ[3]) and not eqm(DQ[3], ZERO),
     "shell 3 is adjacency-pinned: a_3 == 1 and D2 Q_3 is a nonzero invariant axis")

# shell 2 is not adjacency-rigid (a_2 == 2): exhibit a second invariant
# antisymmetric operator on stratum 2 that is independent of D2 Q_2. A single
# rank-two adjacency seed (sites 0,1) averages back onto span(D2 Q_2); a
# structurally different seed (sites 0,21) reaches the other invariant axis.
u21 = np.zeros(N, dtype=np.int64); u21[21] = 1
K0b = np.outer(u0, u21) - np.outer(u21, u0)
Adj2 = Q[2] @ avg_of(K0) @ Q[2]
Alt2 = Q[2] @ avg_of(K0b) @ Q[2]
gate("B9.10", a_m[2] == 2 and (not eqm(Adj2, ZERO))
     and (not eqm(Alt2, ZERO)) and invariant(Alt2)
     and eqm(Alt2.T, -Alt2) and (not proportional(Alt2, DQ[2]))
     and proportional(Adj2, DQ[2]),
     "shell 2 not adjacency-rigid: a_2 == 2, a second invariant antisym axis off span(D2 Q_2)")

# B9.11 - complex-structure SIGN. B9.5 gates the square identity
# (D2 Q_m)^2 == -4 m N_m Q_m, but that coefficient against the unnormalized Q_m
# is NOT uniformly signed: -4 m N_m = (0, 512, -1024, 4608). The complex-structure
# property lives in the idempotent normalization P_m = Q_m / N_m, against which the
# square is -4 m N_m^2 P_m with -4 m N_m^2 < 0 on every bulk shell. This gate pins
# the sign story (raw coefficient not uniformly negative; idempotent coefficient
# negative everywhere) and ties it to the actual matrices.
raw_coeff = [-4 * m * Nm[m] for m in range(4)]
idem_coeff = [-4 * m * Nm[m] ** 2 for m in range(4)]
gate("B9.11",
     raw_coeff == [0, 512, -1024, 4608]
     and any(raw_coeff[m] > 0 for m in (1, 2, 3))
     and all(idem_coeff[m] < 0 for m in (1, 2, 3))
     and all(eqm(Nm[m] * (DQ[m] @ DQ[m]), idem_coeff[m] * Q[m]) for m in (1, 2, 3)),
     "complex-structure sign: (D2 Q_m)^2 == -4 m N_m^2 P_m is a negative multiple of the idempotent P_m = Q_m/N_m on every bulk shell, though raw -4 m N_m = (0,512,-1024,4608) is not uniformly negative")

# ============================================================================
# B10 - the m=1 value tables and K-real registration (result 8)
# ============================================================================
v = Q[1][:, 0].astype(object)
gate("B10.1", eqm(M @ Q[1][:, 0], -4 * Q[1][:, 0]) and np.any(Q[1][:, 0] != 0),
     "v = Q_1[:,0] is a nonzero stratum-1 vector: M v == -4 v")
A0 = 2 * Q[1][:, 0]
B0 = -(D2 @ Q[1][:, 0])
gate("B10.2", eqm(D2 @ A0, -2 * B0) and eqm(D2 @ B0, 2 * A0),
     "doublet: D2 A == -2 B and D2 B == 2 A (so J_1 = D2/2 gives J_1 w == i w)")
vv = int(v @ v)
normw = int(A0.astype(object) @ A0.astype(object)) + int(B0.astype(object) @ B0.astype(object))
gate("B10.3", normw == 8 * vv,
     f"doublet norm |w|^2 == A.A + B.B == 8 |v|^2 (|v|^2 = {vv}, |w|^2 = {normw})")


def sesq(Mre, Mim, wr, wi):
    Mre = Mre.astype(object)
    Mim = Mim.astype(object)
    wr = wr.astype(object)
    wi = wi.astype(object)
    return int(wr @ Mre @ wr + wi @ Mre @ wi + 2 * (wi @ Mim @ wr))


# w = A + iB -> (wr, wi) = (A0, B0); conj w -> (A0, -B0)
Ksep = DQ[1]  # i (D2 Q_1) as Hermitian imaginary part
sep_w = sesq(ZERO, Ksep, A0, B0)
sep_cw = sesq(ZERO, Ksep, A0, -B0)
gate("B10.4", sep_w == -sep_cw and sep_w != 0,
     f"K-odd separator i(D2 Q_1): opposite nonzero values ({sep_w}, {sep_cw})")
# raw projector pair 2 Q_1 -+ i(D2 Q_1): Hermitian real part 2 Q_1, imag part -+ D2 Q_1
Pa_w = sesq(2 * Q[1], -DQ[1], A0, B0)
Pa_cw = sesq(2 * Q[1], -DQ[1], A0, -B0)
Pb_w = sesq(2 * Q[1], DQ[1], A0, B0)
Pb_cw = sesq(2 * Q[1], DQ[1], A0, -B0)
gate("B10.5", (Pa_w == 0) != (Pa_cw == 0) and (Pb_w == 0) != (Pb_cw == 0)
     and Pa_w == Pb_cw and Pa_cw == Pb_w,
     f"projector pair one-zero with K swap: 2Q_1-i(D2Q_1)->({Pa_w},{Pa_cw}), "
     f"2Q_1+i(D2Q_1)->({Pb_w},{Pb_cw})")
qf_w = sesq(Q[1], ZERO, A0, B0)
qf_cw = sesq(Q[1], ZERO, A0, -B0)
gate("B10.6", qf_w == qf_cw and qf_w != 0,
     f"K-real symmetric face Q_1: SAME value on the conjugate pair ({qf_w}, {qf_cw})")

print(f"[info] m=1 value tables: |v|^2={vv}, |w|^2={normw}, "
      f"i(D2Q1) on (w, conj w)=({sep_w}, {sep_cw}), "
      f"projector 2Q1-i(D2Q1) on (w, conj w)=({Pa_w}, {Pa_cw}), Q1 face=({qf_w}, {qf_cw})")

# ============================================================================
# B11 - note hygiene (the only gate that reads a target file back)
# ============================================================================
NOTE_NAME = "KCPT_BULK_BLOCK_EIGENVALUE_STRATIFICATION_ADJACENCY_NATIVE_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md"
note_path = os.path.join(DOCS, NOTE_NAME)
with open(note_path, encoding="utf-8") as fh:
    note_raw = fh.read()
note_low = note_raw.lower()

FORBIDDEN = ["the spec", "spectrum", "spectral", "retained", "audited",
             "conditional", "open_gate", "pass with", "effective_status",
             "exhausts", "exhausted", "only route", "last route",
             "closes the", "final route"]
present_forbidden = [s for s in FORBIDDEN if s in note_low]
gate("B11.1", present_forbidden == [],
     f"forbidden substrings absent from the note ({present_forbidden or 'none'})")

REQUIRED = ["bounded_theorem", "10 = 4 + 4 + 2", "ten on the image block",
            "M = 2 (T_200 + T_020 + T_002) - 6 I", "(D2 Q_m)^2 = -4 m N_m Q_m"]
missing_req = [s for s in REQUIRED if s not in note_raw]
gate("B11.2", missing_req == [],
     f"required verbatim strings present ({missing_req or 'all present'})")

DEP_LINKS = [
    "MINIMAL_AXIOMS_2026-06-29.md",
    "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md",
    "KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md",
    "KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md",
]
link_targets = set(re.findall(r"\]\(([^)]+)\)", note_raw))
links_present = set(DEP_LINKS).issubset(link_targets)
deps_exist = all(os.path.isfile(os.path.join(DOCS, d)) for d in DEP_LINKS)
gate("B11.3", links_present and deps_exist,
     "all five dependency links present as markdown links and the deps exist")
gate("B11.4", "**Type:** bounded_theorem" in note_raw and "## Boundary" in note_raw
     and "**Claim boundary:**" in note_raw,
     "note carries the bounded_theorem front matter, claim boundary, and Boundary section")

# ----------------------------------------------------------------------------
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
