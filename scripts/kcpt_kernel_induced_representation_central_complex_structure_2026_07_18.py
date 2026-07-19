#!/usr/bin/env python3
"""KCPT kernel induced representation: central complex structure (bounded theorem).

Integer / rational-exact verification runner. Every gated quantity is recomputed
from the construction (D2 from the eta phases, V8 from the corner subsets, the
dressed classes from their definitions); expected values appear only on the
comparison side of each gate. The raw complex-structure representative J64 is
FOUND by the runner (central raw element squaring to -64 I, canonical orientation),
normalized as j = J64/64, and then gated against its closed-form Pauli word -- it
is never hard-coded.

Group elements are 64 times an orthogonal matrix and 80 of the 96 carry half-unit
(+-32) entries, so a scalar floor-divide by 64 would corrupt them. Commutant,
orbit-rank and orbit gates therefore run on the RAW integer matrices (all such
tests are scale-invariant). The product A@B of two group elements is always
divisible by 64, so mul(A,B) = (A@B)//64 stays exact.

Paired note: docs/KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md
Cache: logs/runner-cache/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.txt
"""

import os
import re
import sys
import json
import subprocess
import itertools
import numpy as np
from sympy import Matrix, eye, symbols, factor, simplify, I as sy_I

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASS = 0
FAIL = 0


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    print(f"[{tag}] {'PASS' if ok else 'FAIL'} {desc}")
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


# ------------------------------------------------------------------ construction
L = 4
N = 64


def idx(x1, x2, x3):
    return (x1 * L + x2) * L + x3


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
HW = [0, 1, 1, 1, 2, 2, 2, 3]
sub_index = {s: k for k, s in enumerate(SUBSETS)}


def sub_xor(sa, sb):
    return tuple(sorted(set(sa).symmetric_difference(set(sb))))


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
I8 = 64 * np.eye(8, dtype=np.int64)


def induced(U):
    return V8.T @ U @ V8


def mul(A, B):
    P = A @ B
    assert np.all(P % 64 == 0), "mul divisibility failure"
    return P // 64


def Zt(t):
    z = np.array([(-1) ** int(sum(t[k] for k in S)) for S in SUBSETS], dtype=np.int64)
    return np.diag(z)


def subperm(sigma):
    P = np.zeros((8, 8), dtype=np.int64)
    for c, S in enumerate(SUBSETS):
        newS = tuple(sorted(sigma(k) for k in S))
        P[sub_index[newS], c] = 1
    return P


def X_T(T):
    P = np.zeros((8, 8), dtype=np.int64)
    for c, S in enumerate(SUBSETS):
        P[sub_index[sub_xor(S, T)], c] = 1
    return P


def Ms_from_shat(shat):
    Ms = np.zeros((8, 8), dtype=np.int64)
    for r, R in enumerate(SUBSETS):
        for c, S in enumerate(SUBSETS):
            Ms[sub_index[sub_xor(R, S)], c] += shat[r]
    return Ms


# ------------------------------------------------------- scan the dressed classes
scan = {}
for name, base in BASES.items():
    cand = 0
    preserve = 0
    commuting = []
    for bits in ALLBITS:
        diagd = np.diag(SF[bits])
        for t in itertools.product(range(L), repeat=3):
            U = diagd @ base @ TR[t]
            cand += 1
            UV = U @ V8
            K8 = V8.T @ UV
            if np.array_equal(64 * UV, V8 @ K8):
                preserve += 1
            if np.array_equal(U @ D2, D2 @ U):
                commuting.append((bits, t, K8.copy()))
    scan[name] = dict(cand=cand, preserve=preserve, commuting=commuting)


def eqm(a, b):
    return np.array_equal(a, b)


# ============================================================================ B1
print("== B1 surface and whole-class kernel preservation ==")
gate("B1.1", eqm(D2.T, -D2) and set(np.unique(D2).tolist()).issubset({-1, 0, 1}),
     "D2 integer antisymmetric, entries in {-1,0,1}")
rankD2 = Matrix(D2.tolist()).rank()
gate("B1.2", rankD2 == 56, f"rank(D2)==56 so dim ker==8 (got {rankD2})")
gate("B1.3",
     eqm(D2 @ V8, np.zeros((N, 8), dtype=np.int64))
     and eqm(V8.T @ V8, 64 * np.eye(8, dtype=np.int64))
     and sorted([HW.count(h) for h in (0, 1, 2, 3)]) == [1, 1, 3, 3],
     "D2@V8==0, V8.T@V8==64I, HW grading 1+3+3+1")

for name in BASES:
    s = scan[name]
    gate(f"B1.4-{name}", s["cand"] == 4096 and s["preserve"] == 4096,
         f"{name}: 4096 candidates, all preserve corner kernel (residual identity)")
for name in BASES:
    gate(f"B1.5-{name}", len(scan[name]["commuting"]) == 64,
         f"{name}: exactly 64 members commute with D2")
for name in BASES:
    ok = all(eqm(K.T @ K, 4096 * np.eye(8, dtype=np.int64))
             for _, _, K in scan[name]["commuting"])
    gate(f"B1.6-{name}", ok, f"{name}: every commuting K8 has K8.T@K8==4096 I")

# B1.7 dictionary
texmp = (1, 2, 3)
gate("B1.7a", eqm(induced(TR[texmp]), 64 * Zt(texmp)),
     "induced(trans(1,2,3))==64*Z(t) parity diagonal")
P_swap01 = subperm(lambda k: {0: 1, 1: 0, 2: 2}[k])
P_sigma = subperm(lambda k: {0: 1, 1: 2, 2: 0}[k])
gate("B1.7b", eqm(induced(U2), 64 * P_swap01),
     "induced(undressed U2)==64*P_swap01 (swap subset axes 0,1)")
gate("B1.7c", eqm(induced(UR), 64 * P_sigma),
     "induced(undressed UR)==64*P_sigma (0->1->2->0 on subsets)")

# B1.8
d_lin = SF[(0, 1, 1, 0, 0, 0)]
gate("B1.8", eqm(induced(np.diag(d_lin)), 64 * X_T((1, 2))),
     "induced(diag chi_{(1,2)})==64*X_{(1,2)} symmetric-difference perm")

# B1.9 factorization exemplar
bex = (0, 1, 0, 1, 0, 0)
tex = (1, 0, 0)
dex = SF[bex]
Uex = np.diag(dex) @ U2 @ TR[tex]
gate("B1.9a", eqm(Uex @ D2, D2 @ Uex), "exemplar bits=(0,1,0,1,0,0),t=(1,0,0) commutes with D2")
K8ex = induced(Uex)
shat = V8.T @ dex
gate("B1.9b", eqm(K8ex, Ms_from_shat(shat) @ P_swap01 @ Zt(tex)),
     "exemplar K8 == Ms(shat) @ P_swap01 @ Z(t)")
supp = {SUBSETS[r]: int(shat[r]) for r in range(8) if shat[r] != 0}
gate("B1.9c", supp == {(): 32, (0,): -32, (1,): 32, (0, 1): 32},
     "exemplar shat support == {():32,(0,):-32,(1,):32,(0,1):32}")

# B1.10
gate("B1.10", any(b == bex and t == tex for b, t, _ in scan["U2"]["commuting"]),
     "exemplar (bits,t) present in the U2 commuting solution set")

# ============================================================================ B2
print("== B2 per-class census and the linear/quadratic dichotomy ==")
gate("B2.1-stab", all((b[3], b[4], b[5]) == (0, 0, 0) for b, _, _ in scan["stab"]["commuting"]),
     "stab: all commuting members purely linear (b==0,0,0)")
gate("B2.1-U2", all((b[3], b[4], b[5]) != (0, 0, 0) for b, _, _ in scan["U2"]["commuting"]),
     "U2: no purely-linear commuting member")
gate("B2.1-UR", all((b[3], b[4], b[5]) != (0, 0, 0) for b, _, _ in scan["UR"]["commuting"]),
     "UR: no purely-linear commuting member")
gate("B2.2-U2", all((b[3], b[4], b[5]) == (1, 0, 0) for b, _, _ in scan["U2"]["commuting"]),
     "U2: forced quadratic signature (b12,b13,b23)==(1,0,0)")
gate("B2.2-UR", all((b[3], b[4], b[5]) == (1, 1, 0) for b, _, _ in scan["UR"]["commuting"]),
     "UR: forced quadratic signature (b12,b13,b23)==(1,1,0)")


def law_ok(name, law):
    for b, t, _ in scan[name]["commuting"]:
        exp = tuple(v % 2 for v in law(t))
        if (b[0], b[1], b[2]) != exp:
            return False
    return True


gate("B2.3-stab", law_ok("stab", lambda t: (0, t[0], t[0] + t[1])),
     "stab compensator law (a1,a2,a3)==(0,t1,t1+t2)")
gate("B2.3-U2", law_ok("U2", lambda t: (1 + t[0], 1, 1 + t[0] + t[1])),
     "U2 compensator law (a1,a2,a3)==(1+t1,1,1+t1+t2)")
gate("B2.3-UR", law_ok("UR", lambda t: (t[0] + t[1], 0, t[0])),
     "UR compensator law (a1,a2,a3)==(t1+t2,0,t1)")

for name in BASES:
    byb = {}
    for b, t, _ in scan[name]["commuting"]:
        byb.setdefault(b, []).append(t)
    ok = len(byb) == 4 and all(len(v) == 16 for v in byb.values())
    gate(f"B2.4-{name}", ok, f"{name}: commuting set == 4 sign-fields x 16 translations")


def block_diag(K):
    for i in range(8):
        for j in range(8):
            if HW[i] != HW[j] and K[i, j] != 0:
                return False
    return True


def triplet_pres(K):
    for c in (1, 2, 3):
        for r in range(8):
            if r not in (1, 2, 3) and K[r, c] != 0:
                return False
    return True


gcount = {name: sum(1 for _, _, K in scan[name]["commuting"] if block_diag(K)) for name in BASES}
tcount = {name: sum(1 for _, _, K in scan[name]["commuting"] if triplet_pres(K)) for name in BASES}
gate("B2.5a", (gcount["stab"], gcount["U2"], gcount["UR"]) == (16, 0, 0),
     "grading-preserving counts per class == 16/0/0")
gate("B2.5b", (tcount["stab"], tcount["U2"], tcount["UR"]) == (16, 0, 0),
     "triplet-preserving counts per class == 16/0/0")
gp_stab = [(b, t, K) for b, t, K in scan["stab"]["commuting"] if block_diag(K)]
gate("B2.5c",
     len(gp_stab) == 16
     and all((b[0], b[1], b[2]) == (0, 0, 0) for b, _, _ in gp_stab)
     and all(eqm(K, np.diag(np.diag(K))) for _, _, K in gp_stab),
     "the 16 stab grading-preservers are exactly a==(0,0,0), each a pure Z-diagonal")

dK = {name: {K.tobytes() for _, _, K in scan[name]["commuting"]} for name in BASES}
dvac = {name: {tuple(K[:, 0].tolist()) for _, _, K in scan[name]["commuting"]} for name in BASES}
gate("B2.6a", all(len(dK[name]) == 8 for name in BASES),
     "distinct induced K8 per class == 8")
gate("B2.6b", all(len(dvac[name]) == 4 for name in BASES),
     "distinct vacuum images (K8 column 0) per class == 4")

census = {}
for _, _, K in scan["stab"]["commuting"]:
    key = frozenset((HW[i], HW[j]) for i in range(8) for j in range(8) if K[i, j] != 0)
    census[key] = census.get(key, 0) + 1
exp_census = {
    frozenset({(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2)}): 32,
    frozenset({(0, 0), (1, 1), (2, 2), (3, 3)}): 16,
    frozenset({(0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1)}): 16,
}
gate("B2.7", census == exp_census,
     "stab hw-block-support census == 32/16/16 with the named supports")

# ============================================================================ B3
print("== B3 the induced group G ==")
gens_by_class = {name: [K for _, _, K in scan[name]["commuting"]] for name in BASES}
gens_all = {}
for name in BASES:
    for K in gens_by_class[name]:
        gens_all[K.tobytes()] = K
GEN = list(gens_all.values())


def closure(gs):
    gs = [g.copy() for g in gs]
    elts = {g.tobytes(): g for g in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for x in frontier:
            for g in gs:
                p = mul(x, g)
                k = p.tobytes()
                if k not in elts:
                    elts[k] = p
                    nf.append(p)
        frontier = nf
    return list(elts.values())


G = closure(GEN)
gate("B3.1", len(GEN) == 24 and len(G) == 96,
     f"G = closure of 24 distinct induced K8; |G|==96 (got {len(G)})")


def clo_size(names):
    gs = []
    for nm in names:
        gs += gens_by_class[nm]
    return len(closure(gs))


gate("B3.2a", (clo_size(["stab"]), clo_size(["U2"]), clo_size(["UR"])) == (16, 32, 48),
     "single-class closures <stab>/<U2>/<UR> == 16/32/48")
gate("B3.2b",
     (clo_size(["stab", "U2"]), clo_size(["stab", "UR"]), clo_size(["U2", "UR"])) == (32, 48, 96),
     "pair closures 32/48/96; only U2+UR generate all of G")

gate("B3.3a", any(eqm(g, -I8) for g in G), "-64 I is in G")
center = [g for g in G if all(eqm(mul(g, h), mul(h, g)) for h in G)]
gate("B3.3b", len(center) == 4, f"center Z(G) has order 4 (got {len(center)})")
central_sq = [g for g in center if eqm(mul(g, g), -I8)]
gate("B3.3c", len(central_sq) == 2, "exactly 2 central elements square to -I")


def order(g):
    p = g.copy()
    k = 1
    while not eqm(p, I8):
        p = mul(p, g)
        k += 1
    return k


import math
orders = [order(g) for g in G]
expo = 1
for o in orders:
    expo = expo * o // math.gcd(expo, o)
gate("B3.4a", expo == 24, f"exponent(G)==24 (got {expo})")

inv = {}
for g in G:
    for h in G:
        if eqm(mul(g, h), I8):
            inv[g.tobytes()] = h
            break
bykey = {g.tobytes(): i for i, g in enumerate(G)}
remaining = set(range(len(G)))
sizes = []
while remaining:
    i = next(iter(remaining))
    g = G[i]
    cls = set()
    for h in G:
        cls.add(mul(mul(h, g), inv[h.tobytes()]).tobytes())
    ids = {bykey[k] for k in cls}
    sizes.append(len(ids))
    remaining -= ids
gate("B3.4b",
     len(sizes) == 16
     and sorted(sizes) == [1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 12, 12],
     "16 conjugacy classes, sizes [1,1,1,1,6x6,8x4,12x2]")

comms = []
for g in G:
    for h in G:
        comms.append(mul(mul(mul(g, h), inv[g.tobytes()]), inv[h.tobytes()]))
Gp = closure(comms)
gate("B3.4c", len(Gp) == 24 and (len(G) // len(Gp)) == 4,
     "commutator subgroup order 24; abelianization order 4")

gG = [g for g in G if block_diag(g)]
tG = [g for g in G if triplet_pres(g)]
gate("B3.5a", len(gG) == 4 and len(tG) == 4,
     "grading-preserving members of G == 4 == triplet-preserving")
restr = set()
lock = True
for g in gG:
    R = g[np.ix_([1, 2, 3], [1, 2, 3])]
    assert np.all(R % 64 == 0)
    Rd = (R // 64)
    restr.add(tuple(np.diag(Rd).tolist()))
    if Rd[0, 0] != Rd[1, 1]:
        lock = False
gate("B3.5b", restr == {(1, 1, 1), (1, 1, -1), (-1, -1, 1), (-1, -1, -1)},
     "triplet restrictions == {I, diag(1,1,-1), diag(-1,-1,1), -I}")
gate("B3.5c", lock, "every graded restriction has R[0,0]==R[1,1] (x1,x2 sign-locked)")

gate("B3.6", eqm(sum(G), np.zeros((8, 8), dtype=np.int64)),
     "sum over G of K8 == 0 (no fixed vector)")

# ============================================================================ B4
print("== B4 complex-type irreducibility and the commutant ==")
sum_tr2 = sum(int(np.trace(g)) ** 2 for g in G)
gate("B4.1", sum_tr2 == 786432 == 2 * 96 * 4096,
     f"sum tr(K8)^2 == 786432 == 2*96*4096 so <chi,chi>==2 (got {sum_tr2})")
fs = sum(int(np.trace(mul(g, g))) for g in G)
gate("B4.2", fs == 0, f"Frobenius-Schur sum over G of tr(mul(K,K))==0 (got {fs})")

# small generating subset (verify closure 96) then commutant over Q on RAW matrices
genpair = None
for i in range(len(GEN)):
    for j in range(i + 1, len(GEN)):
        if len(closure([GEN[i], GEN[j]])) == 96:
            genpair = [GEN[i], GEN[j]]
            break
    if genpair:
        break
gate("B4.3a", genpair is not None and len(closure(genpair)) == 96,
     "a 2-element generating subset closes to all 96")
blocks = []
for K in genpair:
    Ki = K.astype(object)
    M = np.kron(Ki, np.eye(8, dtype=object)) - np.kron(np.eye(8, dtype=object), Ki.T)
    blocks.append(Matrix(M.tolist()))
commutant_dim = len(Matrix.vstack(*blocks).nullspace())
gate("B4.3b", commutant_dim == 2,
     f"exact commutant over Q (raw kron equations) has dimension 2 (got {commutant_dim})")

# Find raw J64: central, scaled-square -64 I, orientation
# J64[index(()),index((1,))] > 0. Then normalize exactly as j = J64/64.
i_vac = sub_index[()]
i_x2 = sub_index[(1,)]
cand_J64 = [g for g in central_sq if g[i_vac, i_x2] > 0]
gate("B4.4a", len(cand_J64) == 1,
     "unique raw central root with J64 chi_{x2}=+64 chi_{}")
J64 = cand_J64[0]
otherJ64 = [g for g in central_sq if not eqm(g, J64)][0]
gate("B4.4b", eqm(otherJ64, -J64), "the other raw central root == -J64")

assert np.all(J64 % 64 == 0)
nz = int(np.count_nonzero(J64))
formula_ok = True
for c, S in enumerate(SUBSETS):
    r = sub_index[sub_xor(S, (1,))]
    val = 64 * ((-1) ** len(set(S) & {0, 2})) * (1 if 1 in S else -1)
    if int(J64[r, c]) != val:
        formula_ok = False
gate("B4.5a", nz == 8 and formula_ok,
     "J64 has 8 nonzeros; J64[index(S^{1}),index(S)]==64*(-1)^{|S&{0,2}|}*(+1 iff 1 in S)")
gate("B4.5b",
     int(np.trace(J64)) == 0 and eqm(J64.T, -J64) and eqm(mul(J64, J64), -I8),
     "trace(J64)==0, J64.T==-J64, mul(J64,J64)==-64 I; hence j^2==-I")
gate("B4.5c", all(eqm(J64 @ g, g @ J64) for g in GEN),
     "J64 (equivalently j) commutes with every generator")
Jsupp = {(HW[i], HW[j]) for i in range(8) for j in range(8) if J64[i, j] != 0}
gate("B4.5d", Jsupp == {(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2)},
     "hw-block support of J64 == {(0,1),(1,0),(1,2),(2,1),(2,3),(3,2)}")
col0 = J64[:, i_vac].copy()
expcol = np.zeros(8, dtype=np.int64)
expcol[i_x2] = -64
gate("B4.5e", eqm(col0, expcol),
     "J64 column 0 == -64 * e_{(1,)} (j maps vacuum -> minus chi_{x2})")

lam = symbols('lambda')
j = Matrix((J64 // 64).tolist())
cp = j.charpoly(lam).as_expr()
gate("B4.6a", simplify(cp - (lam ** 2 + 1) ** 4) == 0,
     "charpoly(j) == (lambda^2 + 1)^4")
rp = (j - sy_I * eye(8)).rank()
rm = (j + sy_I * eye(8)).rank()
gate("B4.6b", rp == 4 and rm == 4,
     "rank(j - iI)==4 and rank(j + iI)==4 (W and Wbar both 4-dim)")

sa, sb = symbols('a b')
detexpr = (sa * eye(8) + sb * j).det()
gate("B4.7", simplify(detexpr - (sa ** 2 + sb ** 2) ** 4) == 0,
     "det(aI + bj) == (a^2 + b^2)^4; Q[j] is a field, and Maschke gives rational irreducibility")

e1 = np.zeros(8, dtype=np.int64)
e1[1] = 1
orbit = [g @ e1 for g in G]  # RAW integer vectors; rank is scale-invariant
rank_orbit = Matrix([v.tolist() for v in orbit]).rank()
gate("B4.8a", rank_orbit == 8,
     f"rank of 96x8 orbit {{K@e_1}} == 8 (single hw=1 carrier spans kernel) (got {rank_orbit})")
cur = [np.eye(8, dtype=np.int64)[i] for i in (1, 2, 3)]
r_cur = Matrix([v.tolist() for v in cur]).rank()
grew = True
while grew:
    grew = False
    newset = list(cur)
    for g in G:
        for v in cur:
            newset.append(g @ np.array(v))
    M = Matrix([v.tolist() for v in newset])
    nr = M.rank()
    if nr > r_cur:
        _, piv = M.T.rref()
        cur = [np.array(newset[p]) for p in piv]
        r_cur = nr
        grew = True
gate("B4.8b", r_cur == 8,
     "iterative rref from span{e1,e2,e3} stabilizes at dimension 8")

gate("B4.9", len(gG) == 4 and all(eqm(g, np.diag(np.diag(g))) for g in gG),
     "the 4 graded members of G are DIAGONAL (reducible-contrast discriminator)")

# ============================================================================ B5
print("== B5 FLAG registration and neutrality ==")
gate("B5.1a", all(g.dtype == np.int64 for g in G) and all(np.isreal(g).all() for g in G),
     "entrywise conjugation fixes G (normalized elements real rational; raw representatives integer)")
basis_plus = (j - sy_I * eye(8)).nullspace()
Aminus = j + sy_I * eye(8)
swap_ok = len(basis_plus) == 4 and all((Aminus * v.conjugate()).is_zero_matrix for v in basis_plus)
gate("B5.1b", swap_ok,
     "conjugation carries ker(j - iI) into ker(j + iI): swaps W <-> Wbar")

e0 = np.zeros(8, dtype=np.int64)
e0[0] = 1
vac_orbit = {tuple((g @ e0).tolist()) for g in G}  # RAW vectors
gate("B5.2a", len(vac_orbit) == 48, f"vacuum orbit under G has size 48 (got {len(vac_orbit)})")
supps = {tuple(sorted({HW[i] for i in range(8) if v[i] != 0})) for v in vac_orbit}
exp_supps = {(0,), (0, 1, 2), (0, 1, 2, 3), (0, 2), (1,), (1, 2), (1, 2, 3), (1, 3), (2,)}
gate("B5.2b", supps == exp_supps,
     "vacuum-orbit hw-support set matches the mixed-grade spec set")

w1, w2, w3 = symbols('w1 w2 w3')
W = Matrix.diag(w1, w2, w3)
neutral = True
for g in gG:
    R = Matrix((g[np.ix_([1, 2, 3], [1, 2, 3])] // 64).tolist())
    if not (R * W - W * R).is_zero_matrix:
        neutral = False
gate("B5.3", neutral,
     "each triplet restriction commutes with diag(w1,w2,w3): no per-slot weight relation (r-neutral)")

# ============================================================================ B6
print("== B6 negative controls / rejectors ==")
gate("B6.1a", not eqm(U2 @ D2, D2 @ U2), "undressed U2 does not commute with D2")
gate("B6.1b", not eqm(UR @ D2, D2 @ UR), "undressed UR does not commute with D2")
brej = (0, 1, 0, 1, 1, 0)
Urej = np.diag(SF[brej]) @ U2 @ TR[tex]
gate("B6.2", not eqm(Urej @ D2, D2 @ Urej),
     "one-bit rejector: exemplar with b13 flipped does not commute with D2")


def axis_word(axis, inter, present_axis):
    Jp = np.zeros((8, 8), dtype=np.int64)
    for c, S in enumerate(SUBSETS):
        r = sub_index[sub_xor(S, (axis,))]
        Jp[r, c] = 64 * ((-1) ** len(set(S) & inter)) * (1 if present_axis in S else -1)
    return Jp


Jx1 = axis_word(0, {1, 2}, 0)
Jx3 = axis_word(2, {0, 1}, 2)
gate("B6.3a", any(not eqm(Jx1 @ g, g @ Jx1) for g in G),
     "wrong-axis word J' (complex axis x1) fails to commute with some g in G")
gate("B6.3b", any(not eqm(Jx3 @ g, g @ Jx3) for g in G),
     "wrong-axis word J'' (complex axis x3) fails to commute with some g in G")
Ulaw = np.diag(SF[(0, 0, 0, 0, 0, 0)]) @ STAB @ TR[(1, 0, 0)]
gate("B6.4", not eqm(Ulaw @ D2, D2 @ Ulaw),
     "law rejector: stab bits all-zero, t=(1,0,0) violates the stab law and does not commute")

# ============================================================================ B7
print("== B7 verbatim quote gates ==")
NOTE_PATH = os.path.join(
    ROOT, "docs",
    "KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md")
MECH_PATH = os.path.join(
    ROOT, "docs",
    "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md")
CARR_PATH = os.path.join(
    ROOT, "docs",
    "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md")
AX_PATH = os.path.join(ROOT, "docs", "MINIMAL_AXIOMS_2026-06-29.md")


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def normalize(text):
    lines = [re.sub(r'^\s*>\s?', '', ln) for ln in text.split('\n')]
    return re.sub(r'\s+', ' ', ' '.join(lines)).strip()


note_raw = read_text(NOTE_PATH)
note_norm = normalize(note_raw) if note_raw is not None else ""

FRAGMENTS = [
    ("B7.1", MECH_PATH,
     "**FLAG — two-model mechanism:** the entrywise-conjugate presentations in L-K2 satisfy the same named clauses and exchange every K-odd seed."),
    ("B7.2", MECH_PATH,
     "The memo's live Qualification leaves the unfixed choice conditional/open."),
    ("B7.3", CARR_PATH, "graded by Hamming weight as `1 + 3 + 3 + 1`"),
    ("B7.4", CARR_PATH,
     "`eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`"),
    ("B7.5", CARR_PATH, "its exact rank is `56`"),
    ("B7.6", AX_PATH, "standard translations, and proper cubic rotations"),
]
for tag, path, frag in FRAGMENTS:
    src = read_text(path)
    src_norm = normalize(src) if src is not None else ""
    frag_norm = normalize(frag)
    in_src = frag_norm in src_norm
    in_note = frag_norm in note_norm
    if not in_src:
        j = src_norm.find(frag_norm[:24])
        near = src_norm[j:j + len(frag_norm) + 12] if j >= 0 else "(anchor not found)"
        print(f"    [{tag}] source fragment missing; nearest actual text: {near!r}")
    gate(tag, in_src and in_note,
         f"verbatim fragment present in source AND in the new note")

# ============================================================================ B8
print("== B8 sharded-ledger existence ==")
LEDGERS = [
    ("B8.1", "docs/audit/data/ledger/kc/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_bounded_theorem_note_2026-07-17.json"),
    ("B8.2", "docs/audit/data/ledger/kc/kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_bounded_theorem_note_2026-07-16.json"),
    ("B8.3", "docs/audit/data/ledger/mi/minimal_axioms.json"),
]
for tag, rel in LEDGERS:
    p = os.path.join(ROOT, rel)
    ok = False
    if os.path.exists(p):
        try:
            with open(p, "r", encoding="utf-8") as fh:
                json.load(fh)
            ok = True
        except (OSError, json.JSONDecodeError):
            ok = False
    gate(tag, ok, f"ledger shard exists and json-parses: {os.path.basename(rel)}")

# ============================================================================ B9
print("== B9 note hygiene ==")
if note_raw is None:
    for tag in ("B9.1", "B9.2", "B9.3a", "B9.3b", "B9.4"):
        gate(tag, False, "note file not found")
else:
    forbidden = ["only route", "last route", "exhaust", "closes the route",
                 "closes this route", "no other route", "final route",
                 "retained", "unaudited", "effective_status", "audit grade"]
    present_forbidden = [s for s in forbidden if s in note_raw]
    gate("B9.1", not present_forbidden,
         f"forbidden route/status strings absent (found: {present_forbidden})")
    dec = re.search(r'[0-9]\.[0-9]', note_raw)
    gate("B9.2", dec is None,
         f"no bare-decimal literal [0-9].[0-9] in note (match: {dec.group(0) if dec else None})")
    links = re.findall(r'\]\(([^)]+)\)', note_raw)
    dependency_links = {
        "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
    }
    artifact_links = {
        "../scripts/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.py",
        "../logs/runner-cache/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.txt",
    }
    expected_links = dependency_links | artifact_links
    note_dir = os.path.dirname(NOTE_PATH)
    resolved = [os.path.normpath(os.path.join(note_dir, u.split("#", 1)[0])) for u in links]
    tracked = []
    for path in resolved:
        rel = os.path.relpath(path, ROOT)
        proc = subprocess.run(
            ["git", "-C", ROOT, "ls-files", "--error-unmatch", "--", rel],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        tracked.append(proc.returncode == 0)
    link_ok = (
        len(links) == len(expected_links)
        and set(links) == expected_links
        and all(os.path.isfile(path) for path in resolved)
        and all(tracked)
    )
    gate("B9.3a", link_ok,
         "exactly 3 authorities and 2 paired artifacts; every target resolves and is tracked")
    handle = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03"
    backticked = ("`" + handle + "`") in note_raw
    not_linked = not any(handle in u for u in links)
    gate("B9.3b", backticked and not_linked,
         "STAGGERED_DIRAC handle appears backticked and NOT as a link")
    runner_rel = "scripts/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.py"
    cache_rel = "logs/runner-cache/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.txt"
    required = ["**Type:** bounded_theorem", "bounded theorem", "does NOT select",
                "Boundary", runner_rel, cache_rel]
    missing = [s for s in required if s not in note_raw]
    gate("B9.4", not missing, f"required strings present (missing: {missing})")
    verbatim_math = ["Z (x) iY (x) Z", "(a^2 + b^2)^4", "(lambda^2 + 1)^4"]
    missing_math = [s for s in verbatim_math if s not in note_raw]
    gate("B9.5", not missing_math,
         f"PRESERVE-VERBATIM math strings present (missing: {missing_math})")

# ================================================================= final tally
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
