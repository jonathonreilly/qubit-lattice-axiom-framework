#!/usr/bin/env python3
"""KCPT total complex structure: ambient-invariant kernel-plus-bulk assembly.

Class-A finite check on the fixed 4^3 staggered surface. The staggered adjacency
D2, the corner-wave kernel frame V8, the bulk operator M = D2 @ D2 with its
drop-one projectors Q_m, and the ambient D2-commuting dressed closure G_amb of
order 768 are rebuilt from the site construction (machinery copied from the
landed bulk-stratification runner). The kernel monomial J64 is reconstructed from
the explicit subset rule in the linked kernel note and its required properties are
checked here; imported commutant-dimension facts are source-pinned, not rederived.

The kernel-supported complex structure J_ker = V8 @ J64 @ V8.T / 64**2 and the
summed bulk complex structure J_bulk = sum_{m=1,2,3} D2 @ P_m / (2 sqrt m) are
assembled into J_full = J_ker + J_bulk on the whole space C^64. The headline
identity J_full^2 = -I_64 is established PURELY RATIONALLY: writing B_m = D2 @ P_m,
the square reduces to (-P_ker) + sum_m (1/4m) (B_m @ B_m) with every 1/(2 sqrt m)
normalizer cancelling exactly against B_m @ B_m = -4 m P_m, so no sqrt survives any
load-bearing gate. Rational arithmetic is exact (integer numerator object arrays
over a positive integer denominator, gcd-reduced); the 768 ambient-commutation
gates are exact int64 matmuls. Floating point appears ONLY in gates tagged
[FLOAT SANITY - non-load-bearing]; every fact they confirm also has an exact gate.
Each gate prints one line; the script prints a final TOTAL line and exits nonzero
on any failure.
"""
import os
import re
import sys
import math
import itertools
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
# Exact rational matrices: (numerator object-int array, positive int denominator)
# gcd-reduced.  No floating point ever enters these.
# ----------------------------------------------------------------------------


def robj(a):
    return np.array(a, dtype=object)


def _reduce(num, den):
    den = int(den)
    if den < 0:
        num = -num
        den = -den
    g = den
    for v in num.flat:
        vi = int(v)
        if vi:
            g = math.gcd(g, -vi if vi < 0 else vi)
            if g == 1:
                break
    if g > 1:
        num = num // g          # exact: g divides every entry and den
        den //= g
    return (num, den)


def rat(num, den=1):
    return _reduce(robj(num), den)


def rmm(a, b):
    return _reduce(a[0] @ b[0], a[1] * b[1])


def radd(a, b):
    return _reduce(a[0] * b[1] + b[0] * a[1], a[1] * b[1])


def rscal(a, p, q=1):
    return _reduce(a[0] * int(p), a[1] * int(q))


def rneg(a):
    return (-a[0], a[1])


def req(a, b):
    return bool(np.array_equal(a[0] * b[1], b[0] * a[1]))


def riszero(a):
    return bool(np.all(a[0] == 0))


def rtrace_num(a):
    # exact integer numerator of the trace (trace == this / a[1])
    return int(sum(int(a[0][i, i]) for i in range(a[0].shape[0])))


# ----------------------------------------------------------------------------
# Construction (transcribed from the landed surface / bulk runner)
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
sidx = {frozenset(S): k for k, S in enumerate(SUBSETS)}
V8 = np.zeros((N, 8), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for k, S in enumerate(SUBSETS):
        V8[i, k] = (-1) ** int(sum(x[j] for j in S))

# J64: 8x8 integer monomial.  J64[sidx(S xor {1}), sidx(S)] = 64 (-1)^{|S & {0,2}|}(+1 if 1 in S else -1)
J64 = np.zeros((8, 8), dtype=np.int64)
for k, S in enumerate(SUBSETS):
    Sset = frozenset(S)
    T = Sset ^ frozenset({1})
    sign = ((-1) ** len(Sset & frozenset({0, 2}))) * (1 if 1 in Sset else -1)
    J64[sidx[T], k] = 64 * sign


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
Z8 = np.zeros((N, 8), dtype=np.int64)
eye8 = np.eye(8, dtype=np.int64)

I64o = rat(I64)
negI = rneg(I64o)


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


# ----------------------------------------------------------------------------
# Bulk operator, strata, projectors (integer), then the rational operators
# ----------------------------------------------------------------------------
M = D2 @ D2
lam = [0, -4, -8, -12]
Fac = [M - lam[m] * I64 for m in range(4)]
Q = []
for m in range(4):
    P = I64.copy()
    for mp in range(4):
        if mp != m:
            P = P @ Fac[mp]
    Q.append(P)
Nm = []
for m in range(4):
    v = 1
    for mp in range(4):
        if mp != m:
            v *= (lam[m] - lam[mp])
    Nm.append(v)

A = [D2 @ Q[m] for m in range(4)]                 # integer adjacency carriers A_m = D2 Q_m
Pker = rat(V8 @ V8.T, 64)                          # P_ker = V8 V8^T / 64
Jker_int = V8 @ J64 @ V8.T                         # integer kernel lift
Jker = rat(Jker_int, 64 ** 2)                      # J_ker = V8 J64 V8^T / 64^2
Prat = [rat(Q[m], Nm[m]) for m in range(4)]        # P_m = Q_m / N_m
Bm = {m: rat(A[m], Nm[m]) for m in (1, 2, 3)}      # B_m = D2 P_m (rational)
Pbulk = radd(radd(Prat[1], Prat[2]), Prat[3])      # P_bulk = P_1 + P_2 + P_3

# ============================================================================
# B0 - verbatim source-quote greps (pattern-6 defense)
# ============================================================================
DEP = {
    "delivery": "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "kernel": "KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md",
    "ambient": "KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md",
    "bulk": "KCPT_BULK_BLOCK_EIGENVALUE_STRATIFICATION_ADJACENCY_NATIVE_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md",
    "axioms": "MINIMAL_AXIOMS_2026-06-29.md",
}
_dep_txt = {k: open(os.path.join(DOCS, v), encoding="utf-8").read() for k, v in DEP.items()}
gate("B0.1", "its exact rank is `56`" in _dep_txt["delivery"],
     "v1 delivery: 'its exact rank is `56`' present")
gate("B0.2", "two-dimensional, `span{I, j}`" in _dep_txt["kernel"],
     "v2 kernel: 'two-dimensional, `span{I, j}`' present")
gate("B0.3", "the ambient group `G_amb` of order `768`" in _dep_txt["ambient"],
     "v3 ambient: 'the ambient group `G_amb` of order `768`' present")
gate("B0.4", "12 = 2 + 2*0 + 10" in _dep_txt["ambient"],
     "v4 ambient: '12 = 2 + 2*0 + 10' present")
gate("B0.5", "J_m = D2 P_m / (2 sqrt(m))" in _dep_txt["bulk"],
     "v5 bulk: 'J_m = D2 P_m / (2 sqrt(m))' present")

# ============================================================================
# B1 - surface (integer)
# ============================================================================
gate("B1.1", eqm(D2, -D2.T) and set(np.unique(D2)).issubset({-1, 0, 1}),
     "D2 == -D2.T (antisymmetric), entries in {-1,0,1}")
gate("B1.2", sp.Matrix(D2.tolist()).rank() == 56,
     "exact rank(D2) == 56 (kernel dimension 8)")
gate("B1.3", eqm(D2 @ V8, Z8),
     "D2 @ V8 == 0 exactly (V8 spans the kernel)")
gate("B1.4", eqm(V8.T @ V8, 64 * eye8),
     "V8.T @ V8 == 64 I_8 exactly")
gate("B1.5", bool(np.all(np.diag(D2) == 0)) and not bool(np.all(D2 == 0)),
     "rejector: D2 diagonal is all zeros (no self-loops), D2 nonzero")

# ============================================================================
# B2 - bulk operator & strata (integer)
# ============================================================================
carrier = 2 * (TR[(2, 0, 0)] + TR[(0, 2, 0)] + TR[(0, 0, 2)]) - 6 * I64
gate("B2.1", eqm(M, D2 @ D2) and eqm(M, M.T),
     "M == D2 @ D2 and M == M.T")
gate("B2.2", eqm(M, carrier),
     "carrier identity: M == 2*(T200 + T020 + T002) - 6 I")
gate("B2.3", bool(np.all(np.diag(M) == -6))
     and not eqm(M, 2 * (TR[(2, 0, 0)] + TR[(0, 2, 0)] + TR[(0, 0, 2)]) - 5 * I64),
     "rejector: diagonal coefficient is -6 not -5")
minpoly = Fac[0] @ Fac[1] @ Fac[2] @ Fac[3]
gate("B2.4", eqm(minpoly, ZERO),
     "minimal polynomial M(M+4I)(M+8I)(M+12I) == 0")
gate("B2.5", Nm == [384, -128, 128, -384] and Nm[0] == 384 and Nm[0] != 128,
     f"normalizers N_m = prod(lambda_m - lambda_m') == {Nm}; N_0 == 384 not 128")
gate("B2.6", all(eqm(M @ Q[m], lam[m] * Q[m]) for m in range(4)),
     "eigen-projector action M Q_m == lambda_m Q_m for all m")
gate("B2.7", all(eqm(Q[m] @ Q[m], Nm[m] * Q[m]) for m in range(4)),
     "idempotence up to scale Q_m^2 == N_m Q_m for all m")
gate("B2.8", all(eqm(Q[m] @ Q[mp], ZERO) for m in range(4) for mp in range(4) if m != mp),
     "orthogonality Q_m Q_m' == 0 for m != m'")
gate("B2.9", eqm(Q[0] - 3 * Q[1] + 3 * Q[2] - Q[3], 384 * I64)
     and not eqm(Q[0] - 3 * Q[1] + 3 * Q[2] - Q[3], 383 * I64),
     "partition of unity Q_0 - 3Q_1 + 3Q_2 - Q_3 == 384 I (coefficient pinned)")
dm = []
tr_ok = True
for m in range(4):
    tq = int(np.trace(Q[m]))
    if tq % Nm[m] != 0:
        tr_ok = False
        dm.append(None)
    else:
        dm.append(tq // Nm[m])
gate("B2.10", tr_ok and dm == [8, 24, 24, 8],
     f"stratum dims from tr Q_m / N_m == {dm} (expected 8,24,24,8)")
print(f"[info] stratum dims d_m = {dm}")

# ============================================================================
# B3 - kernel structure (rational)
# ============================================================================
gate("B3.1", eqm(J64 @ J64, -(64 ** 2) * eye8),
     "j = J64/64 squares to -I_8 (J64 @ J64 == -64^2 I_8)")
gate("B3.2", eqm(J64.T, -J64),
     "j.T == -j (J64 antisymmetric)")
gate("B3.3", int(np.trace(J64)) == 0,
     "tr(j) == 0")
gate("B3.4", not eqm(J64 @ J64, (64 ** 2) * eye8),
     "rejector: j @ j != +I_8")
gate("B3.5", req(rmm(Jker, Jker), rneg(Pker)),
     "J_ker @ J_ker == -P_ker (rational)")
gate("B3.6", eqm(Jker_int.T, -Jker_int),
     "J_ker.T == -J_ker (integer lift antisymmetric)")
gate("B3.7", rscal(Jker, 64 ** 2)[1] == 1 and req(rscal(Jker, 64 ** 2), rat(Jker_int)),
     "J_ker rational; 64^2 J_ker integer and equals V8 J64 V8.T")
gate("B3.8", req(rmm(Pker, Pker), Pker),
     "P_ker @ P_ker == P_ker (idempotent)")
gate("B3.9", rtrace_num(Pker) == 8 * Pker[1],
     "tr(P_ker) == 8")

# ============================================================================
# B4 - the P_0 = P_ker bridge and adjacency carriers (rational/integer)
# ============================================================================
gate("B4.1", req(Prat[0], Pker) and eqm(Q[0], 6 * (V8 @ V8.T)),
     "P_0 == P_ker: Q_0 == 6 V8 V8.T and Q_0/384 == V8 V8.T/64")
gate("B4.2", eqm(A[0], ZERO),
     "A_0 = D2 Q_0 == 0 (adjacency vanishes on the kernel shell)")
gate("B4.3", all(np.array_equal((A[m].astype(object) @ A[m].astype(object)),
                                (-4 * m * Nm[m]) * Q[m].astype(object)) for m in (1, 2, 3)),
     "A_m @ A_m == -4 m N_m Q_m (integer) for m=1,2,3")
gate("B4.4", all(req(rmm(Bm[m], Bm[m]), rscal(Prat[m], -4 * m)) for m in (1, 2, 3)),
     "B_m @ B_m == -4 m P_m (rational) for m=1,2,3")
gate("B4.5", all(req(Bm[m], rmm(rat(D2), Prat[m])) for m in (1, 2, 3)),
     "B_m == D2 @ P_m (rational construction cross-check)")
gate("B4.6", not req(rmm(Bm[1], Bm[1]), rscal(Prat[1], -8)),
     "rejector: B_1 @ B_1 != -8 P_1 (not the m=2 value)")

# ============================================================================
# B5 - THE RATIONAL ASSEMBLY (headline, all rational)
#
# Six rational facts compose the result:
#   (1) B_m @ B_m   == -4 m P_m          (m = 1,2,3)
#   (2) B_m @ B_m'  == 0                  (m != m')
#   (3) J_ker @ B_m == 0
#   (4) B_m @ J_ker == 0
#   (5) J_ker @ J_ker == -P_ker
#   (6) P_ker + P_1 + P_2 + P_3 == I
# Expanding J_full^2 = J_ker^2 + (J_ker B_bulk + B_bulk J_ker) + J_bulk^2, the
# middle vanishes by (3),(4); the bulk-bulk cross terms vanish by (2); and each
# diagonal 1/(4m)(B_m@B_m) reduces to -P_m by (1).  So J_full^2 equals the RATIONAL
# combination (-P_ker) + sum_m (1/4m)(B_m@B_m) == -I_64 with every 1/(2 sqrt m)
# normalizer cancelling.  No sqrt is formed in any load-bearing gate here.
# ============================================================================
# fact (1)
gate("B5.1", all(req(rmm(Bm[m], Bm[m]), rscal(Prat[m], -4 * m)) for m in (1, 2, 3)),
     "fact 1: B_m @ B_m == -4 m P_m for m=1,2,3")
# fact (2)
gate("B5.2", all(riszero(rmm(Bm[m], Bm[mp]))
                 for m in (1, 2, 3) for mp in (1, 2, 3) if m != mp),
     "fact 2: B_m @ B_m' == 0 for every m != m' in {1,2,3}")
# facts (3),(4)
gate("B5.3", all(riszero(rmm(Jker, Bm[m])) for m in (1, 2, 3)),
     "fact 3: J_ker @ B_m == 0 for m=1,2,3 (support orthogonality)")
gate("B5.4", all(riszero(rmm(Bm[m], Jker)) for m in (1, 2, 3)),
     "fact 4: B_m @ J_ker == 0 for m=1,2,3 (support orthogonality)")
# fact (5)
gate("B5.5", req(rmm(Jker, Jker), rneg(Pker)),
     "fact 5: J_ker @ J_ker == -P_ker")
# fact (6) plus P_bulk
gate("B5.6", req(radd(Pker, Pbulk), I64o) and riszero(rmm(Pker, Pbulk)),
     "fact 6: P_ker + P_bulk == I_64 and P_ker @ P_bulk == 0 (P_bulk = P_1+P_2+P_3)")
# each 1/(4m) term is exactly -P_m
gate("B5.7", all(req(rscal(rmm(Bm[m], Bm[m]), 1, 4 * m), rneg(Prat[m])) for m in (1, 2, 3)),
     "Rational(1,4m) (B_m @ B_m) == -P_m for m=1,2,3")

# THE headline: assemble the rational square and gate == -I_64
combo = rneg(Pker)
for m in (1, 2, 3):
    combo = radd(combo, rscal(rmm(Bm[m], Bm[m]), 1, 4 * m))
gate("B5.8", req(combo, negI),
     "J_full^2 == (-P_ker) + sum_m Rational(1,4m)(B_m @ B_m) == -I_64 (purely rational)")
# discriminating rejectors: dropping a shell, or mis-scaling a term, breaks it
combo_drop = rneg(Pker)
for m in (1, 2):
    combo_drop = radd(combo_drop, rscal(rmm(Bm[m], Bm[m]), 1, 4 * m))
combo_wrong = rneg(Pker)
for m in (1, 2, 3):
    combo_wrong = radd(combo_wrong, rscal(rmm(Bm[m], Bm[m]), 1, 4 * m + 1))
gate("B5.9", (not req(combo_drop, negI)) and (not req(combo_wrong, negI)),
     "rejectors: dropping shell 3, or 1/(4m+1) mis-normalization, does NOT give -I_64")

# [FLOAT SANITY - non-load-bearing] float assembly confirms the exact result
D2f = D2.astype(float)
Pf = [Q[m].astype(float) / Nm[m] for m in range(4)]
Jkerf = Jker_int.astype(float) / (64.0 ** 2)
Jbulkf = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3))
Jfullf = Jkerf + Jbulkf
resid_f = Jfullf @ Jfullf + np.eye(N)
gate("B5.10", float(np.max(np.abs(resid_f))) < 1e-10,
     "[FLOAT SANITY - non-load-bearing] float J_full @ J_full == -I_64 (atol 1e-10)")
Jbulk_wrong = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m + 1)) for m in (1, 2, 3))
Jfull_wrong = Jkerf + Jbulk_wrong
resid_w = Jfull_wrong @ Jfull_wrong + np.eye(N)
gate("B5.11", float(np.linalg.norm(resid_w)) > 0.5,
     "[FLOAT SANITY - non-load-bearing] wrong 2 sqrt(m+1) normalizer does NOT give -I (residual > 0.5)")

# ============================================================================
# B6 - ambient invariance (integer + flagged float)
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
amb_scan = [U for n in BASES for U in commuting[n]]
Gamb = closure_amb(amb_scan)
gate("B6.1", [len(commuting[name]) for name in BASES] == [64, 64, 64]
     and len(amb_scan) == 192
     and len(Gamb) == 768 and len(set(U.tobytes() for U in Gamb)) == 768,
     "scan has 64 commuting members per base, 192 total; regenerated ambient "
     "group |G_amb| == 768, all distinct")
commute_Jker = all(eqm(U @ Jker_int, Jker_int @ U) for U in Gamb)
gate("B6.2", commute_Jker,
     "U @ J_ker_int == J_ker_int @ U for all 768 (integer lift, exact)")
commute_A = all(eqm(U @ A[m], A[m] @ U) for U in Gamb for m in (1, 2, 3))
gate("B6.3", commute_A,
     "U @ A_m == A_m @ U for all 768 and m=1,2,3 (so J_full commutes: scalars 1/(2 sqrt m) are central)")
# a rational-level confirmation on a sampled member (still exact)
Usamp = Gamb[137]
gate("B6.4", req(rmm(rat(Usamp), Jker), rmm(Jker, rat(Usamp)))
     and all(req(rmm(rat(Usamp), Bm[m]), rmm(Bm[m], rat(Usamp))) for m in (1, 2, 3)),
     "sampled U commutes with the rational J_ker and every B_m (exact)")
T100 = TR[(1, 0, 0)]
gamb_keys = set(U.tobytes() for U in Gamb)
gate("B6.5",
     (not eqm(T100 @ A[1], A[1] @ T100))
     and (not eqm(T100 @ D2, D2 @ T100))
     and (T100.tobytes() not in gamb_keys)
     and eqm(T100 @ M, M @ T100),
     "rejector: odd translation T100 is NOT in G_amb (fails to commute with D2 and with A_1) though it commutes with the translation-invariant M")
few = [Gamb[i] for i in (0, 1, 5, 23, 191, 400, 767)]
comm_f = max(float(np.max(np.abs(U.astype(float) @ Jfullf - Jfullf @ U.astype(float)))) for U in few)
gate("B6.6", comm_f < 1e-10,
     "[FLOAT SANITY - non-load-bearing] float J_full commutes with a handful of U (atol 1e-10)")
commute_all = commute_Jker and commute_A

# ============================================================================
# B7 - commutant home (rational): block placement inside Unit 5's 12-dim commutant
# ============================================================================
gate("B7.1", req(rmm(rmm(Pker, Jker), Pker), Jker),
     "P_ker @ J_ker @ P_ker == J_ker (J_ker in the kernel block)")
gate("B7.2", riszero(rmm(Pbulk, Jker)) and riszero(rmm(Jker, Pbulk)),
     "P_bulk @ J_ker == 0 and J_ker @ P_bulk == 0")
gate("B7.3", all(req(rmm(rmm(Pbulk, Bm[m]), Pbulk), Bm[m]) for m in (1, 2, 3)),
     "P_bulk @ B_m @ P_bulk == B_m for m=1,2,3 (each carrier in the image block)")
gate("B7.4", all(riszero(rmm(Pker, Bm[m])) for m in (1, 2, 3)),
     "P_ker @ B_m == 0 for m=1,2,3")

# ============================================================================
# B8 - global entrywise-conjugation pairing (integer dims; flagged float for eigvecs)
# ============================================================================
constituents_real = (np.issubdtype(Jker_int.dtype, np.integer)
                     and all(np.issubdtype(A[m].dtype, np.integer) for m in (1, 2, 3))
                     and np.issubdtype(D2.dtype, np.integer))
gate("B8.1", constituents_real and all(int(v) == v for v in Pker[0].flat),
     "J_full is real: integer lift J_ker_int and every A_m are integer, P_m/J_ker rational")
holo = sum(dm[m] // 2 for m in range(4))
per_shell = tuple(dm[m] // 2 for m in range(4))
gate("B8.2", all(dm[m] % 2 == 0 for m in range(4)) and per_shell == (4, 12, 12, 4) and holo == 32,
     f"holomorphic dim = sum tr(P_m)//2 == {per_shell} == 4+12+12+4 == {holo}")
gate("B8.3", (dm[1] + dm[2] + dm[3]) // 2 == 28 and dm[0] // 2 == 4,
     "bulk contributes 28 conjugate pairs, kernel contributes 4 (Unit 2 dim W = 4); 28 + 4 = 32")
wf, vf = np.linalg.eig(Jfullf)
n_plus = int(np.sum(np.abs(wf - 1j) < 1e-8))
n_minus = int(np.sum(np.abs(wf + 1j) < 1e-8))
ipos = int(np.argmax(np.abs(wf - 1j) < 1e-8))
vp = vf[:, ipos]
cv = np.conj(vp)
resid_conj = float(np.linalg.norm(Jfullf @ cv + 1j * cv))     # J_full cv == -i cv  <=>  J cv + i cv == 0
gate("B8.4", n_plus == 32 and n_minus == 32 and resid_conj < 1e-8,
     "[FLOAT SANITY - non-load-bearing] eig(J_full): 32 at +i, 32 at -i, conj(v_+) in the -i eigenspace")

# ============================================================================
# B9 - boundary: independent bulk-shell sign family (rational + integer)
# ============================================================================
# J_alt = J_ker - J_bulk.  Its square uses J_ker - B_m pieces; the middle terms
# still vanish (facts 3,4) and each diagonal (-B_m)@(-B_m) == B_m@B_m, so the
# rational square is sign-independent and equals -I_64.
combo_alt = rneg(Pker)
for m in (1, 2, 3):
    nb = rneg(Bm[m])
    combo_alt = radd(combo_alt, rscal(rmm(nb, nb), 1, 4 * m))
gate("B9.1", req(combo_alt, negI) and req(combo_alt, combo),
     "J_alt @ J_alt == -I_64 via the same rational facts (sign-independent square)")
gate("B9.2", all(req(rmm(rneg(Bm[m]), rneg(Bm[m])), rmm(Bm[m], Bm[m])) for m in (1, 2, 3)),
     "sign-blindness: (-B_m)@(-B_m) == B_m@B_m for m=1,2,3")
gate("B9.3", commute_all,
     "J_alt commutes with all 768 (built from the same U @ J_ker_int, U @ A_m facts)")
gate("B9.4", not riszero(Bm[1]),
     "J_alt != J_full: J_full - J_alt = 2 J_bulk != 0 (B_1 is nonzero)")
Jaltf = Jkerf - Jbulkf
resid_alt = Jaltf @ Jaltf + np.eye(N)
differ = float(np.max(np.abs(Jfullf - Jaltf)))
gate("B9.5", float(np.max(np.abs(resid_alt))) < 1e-10 and differ > 0.5,
     "[FLOAT SANITY - non-load-bearing] float J_alt @ J_alt == -I and J_alt differs from J_full")

# ============================================================================
# B10 - note hygiene (the only gate that reads the target note back)
# ============================================================================
NOTE_NAME = "KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md"
note_path = os.path.join(DOCS, NOTE_NAME)
with open(note_path, encoding="utf-8") as fh:
    note_raw = fh.read()
note_low = note_raw.lower()

REQUIRED = ["J_full = J_ker + J_bulk", "P_ker + P_bulk = I", "J_full^2 = -I_64",
            "12 = 2 + 2*0 + 10", "J_m = D2 P_m / (2 sqrt(m))", "G_amb", "order `768`", "28",
            "**Type:** bounded_theorem", "**Claim boundary:**",
            "## Setting", "## What the runner checks", "## Honest auditor read"]
missing_req = [s for s in REQUIRED if s not in note_raw]
gate("B10.1", missing_req == [],
     f"required verbatim strings present ({missing_req or 'all present'})")

# spec MUST-BE-ABSENT set (line-for-line), lowercased
FORBIDDEN = ["retained", "audited_conditional", "open_gate", "r = 1/2",
             "unit 7", "bulk holomorphic split"]
present_forbidden = [s for s in FORBIDDEN if s in note_low]
gate("B10.2", present_forbidden == [],
     f"forbidden substrings absent from the note ({present_forbidden or 'none'})")

DEP_LINKS = sorted(DEP.values())
md_links = sorted(t for t in re.findall(r"\]\(([^)]+)\)", note_raw) if t.endswith(".md"))
deps_exist = all(os.path.isfile(os.path.join(DOCS, d)) for d in DEP_LINKS)
gate("B10.3", md_links == DEP_LINKS and deps_exist,
     f"exactly the five dependency notes are markdown-linked, once each ({len(md_links)} links)")
gate("B10.4", "**Type:** bounded_theorem" in note_raw and "**Claim boundary:**" in note_raw
     and "## Setting" in note_raw and "## Honest auditor read" in note_raw
     and "## What the runner checks" in note_raw,
     "note carries bounded_theorem front matter, Claim boundary, Setting, and the two named sections")

# ----------------------------------------------------------------------------
print("[note] all [FLOAT SANITY - non-load-bearing] gates are confirmations; "
      "every load-bearing gate above uses exact integer/rational arithmetic.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
