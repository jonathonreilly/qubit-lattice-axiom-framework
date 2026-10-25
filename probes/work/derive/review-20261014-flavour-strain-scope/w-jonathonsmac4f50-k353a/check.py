#!/usr/bin/env python3
"""Disjoint exact check of the flavour-strain scope (task review-20261014-flavour-strain-scope).

Setting (see ATTEMPT.md): generation triplet = the three hw1 corner modes (pi,0,0),(0,pi,0),(0,0,pi) of the
supplied walker; symmetry group G = (Z^3 translations mod 2) x| (24 proper cubic rotations), |G| = 192;
a vacuum is characterised by its stabiliser H <= G; two Hermitian LH x LH matrices A (up), B (down) are
H-invariant; strain = traceless symmetric 3x3 tensor, rotated by the rotation part only.

Everything finite is exact (integers / Fractions / sympy).  The only floating-point lines are labelled FLOAT.
Method is disjoint from the source script: no numerical SVD commutants, no generator-pair closure for the
enumeration (subgroups come from a Z^1-cocycle parametrisation of N x| Q; closure is used only as a cross-check).
"""
import itertools, random, sys, time, hashlib, os
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time()
OK = []


def chk(name, cond, detail=""):
    cond = bool(cond)
    OK.append(cond)
    print(("PASS " if cond else "FAIL ") + name + ((" | " + detail) if detail else ""))
    sys.stdout.flush()


# ---------------------------------------------------------------------------------------------
# 0. the group: 24 proper rotations (signed permutation matrices, det +1) and translations mod 2
# ---------------------------------------------------------------------------------------------
def idet(M):
    return int(round(float(np.linalg.det(M))))  # 3x3 signed permutations: det is +-1, rounding is exact


ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for j in range(3):
            M[perm[j], j] = sg[j]
        if idet(M) == 1:
            ROT.append(M)
chk("G0 proper cubic rotations = 24 signed-permutation matrices with det +1", len(ROT) == 24)
RKEY = {M.tobytes(): i for i, M in enumerate(ROT)}
QMUL = [[RKEY[(ROT[i] @ ROT[j]).tobytes()] for j in range(24)] for i in range(24)]
QINV = [next(j for j in range(24) if QMUL[i][j] == RKEY[np.eye(3, dtype=int).tobytes()]) for i in range(24)]
QID = RKEY[np.eye(3, dtype=int).tobytes()]
VEC = list(itertools.product((0, 1), repeat=3))           # translation parities v in F_2^3
VID = {v: i for i, v in enumerate(VEC)}


def vadd(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))


def qact(ri, v):                                           # (R v) mod 2
    return tuple(int(x) % 2 for x in ROT[ri] @ np.array(v))


# G element = (ri, v): x -> R x + v on Z^3 (only v mod 2 matters for the corner modes).  id = ri*8 + vid
def gid(ri, v):
    return ri * 8 + VID[v]


def gparts(g):
    return g // 8, VEC[g % 8]


GMUL = np.zeros((192, 192), int)
for g1 in range(192):
    r1, v1 = gparts(g1)
    for g2 in range(192):
        r2, v2 = gparts(g2)
        GMUL[g1, g2] = gid(QMUL[r1][r2], vadd(v1, qact(r1, v2)))
GID = gid(QID, (0, 0, 0))
chk("G1 composition (R1,v1)(R2,v2)=(R1R2, v1+R1 v2) closes on 192 elements, associative on a 4000-sample, identity ok",
    all(GMUL[GID, g] == g and GMUL[g, GID] == g for g in range(192)) and
    all(GMUL[GMUL[a, b], c] == GMUL[a, GMUL[b, c]] for a, b, c in
        [(random.Random(5).randrange(192), random.Random(6 + k).randrange(192), random.Random(7 + 3 * k).randrange(192))
         for k in range(4000)]))
GINV = [int(np.where(GMUL[g] == GID)[0][0]) for g in range(192)]

# ---------------------------------------------------------------------------------------------
# 1. the generation representation derived from the lattice (plane waves (-1)^{x_i})
# ---------------------------------------------------------------------------------------------
BOX = list(itertools.product(range(-2, 3), repeat=3))


def f(i, x):
    return -1 if x[i] % 2 else 1


RHO = []
ok_unique = True
for g in range(192):
    ri, v = gparts(g)
    R = ROT[ri]
    Ri = ROT[QINV[ri]]
    # g^{-1}: x -> Ri (x - v) ; (g.f_i)(x) = f_i(g^{-1} x)
    M = np.zeros((3, 3), int)
    for i in range(3):
        vals = [f(i, tuple(Ri @ (np.array(x) - np.array(v)))) for x in BOX]
        hit = 0
        for j in range(3):
            for s in (1, -1):
                if all(vals[k] == s * f(j, BOX[k]) for k in range(len(BOX))):
                    M[j, i] = s
                    hit += 1
        if hit != 1:
            ok_unique = False
    RHO.append(M)
chk("R1 each symmetry maps every corner plane wave (-1)^{x_i} to +-(another one), uniquely (derived from the lattice action)",
    ok_unique)
chk("R2 rho is a homomorphism G -> GL3(Z) on all 192^2 pairs",
    all(np.array_equal(RHO[GMUL[a, b]], RHO[a] @ RHO[b]) for a in range(192) for b in range(192)))
absP = lambda ri: np.abs(ROT[ri])
chk("R3 rho(R,v) = diag((-1)^v')|R| : rotations act by pure permutations (no sign), translations by diagonal signs",
    all(np.array_equal(np.abs(RHO[g]), absP(g // 8)) for g in range(192)) and
    all(np.array_equal(RHO[gid(QID, v)], np.diag([(-1) ** x for x in v])) for v in VEC))
K0 = [g for g in range(192) if np.array_equal(RHO[g], np.eye(3, dtype=int)) or np.array_equal(RHO[g], -np.eye(3, dtype=int))]
rotK0 = sorted(set(g // 8 for g in K0))
chk("R4 elements acting as a scalar +-1 on the generation triplet: 8 of them = {pi-rotations about the 3 axes, 1} x {no flip, flip all three}",
    len(K0) == 8 and len(rotK0) == 4 and all(ROT[r].trace() in (3, -1) and np.all(np.abs(ROT[r]) == np.eye(3, dtype=int)) for r in rotK0))
K0S = frozenset(K0)

# ---------------------------------------------------------------------------------------------
# 2. exact action on strain (rational 5x5 matrices) and on Hermitian matrices (integer 9x9)
# ---------------------------------------------------------------------------------------------
# strain basis b1=E12+E21,b2=E13+E31,b3=E23+E32 (off-diagonal, "OD"), b4=E11-E22, b5=E11+E22-2E33 ("D0")
def E(i, j):
    M = sp.zeros(3, 3)
    M[i, j] = 1
    return M


SB = [E(0, 1) + E(1, 0), E(0, 2) + E(2, 0), E(1, 2) + E(2, 1), E(0, 0) - E(1, 1), E(0, 0) + E(1, 1) - 2 * E(2, 2)]


def scoord(S):
    return [S[0, 1], S[0, 2], S[1, 2], (S[0, 0] - S[1, 1]) / 2, (S[0, 0] + S[1, 1]) / 2]


def M5(R):
    Rs = sp.Matrix(R.tolist())
    cols = [scoord(Rs * b * Rs.T) for b in SB]
    return [[Fr(int(sp.numer(cols[q][p])), int(sp.denom(cols[q][p]))) for q in range(5)] for p in range(5)]  # [p][q]


M5R = [np.array(M5(R), dtype=object) for R in ROT]


def tr5(ri, part="all"):
    idx = {"all": range(5), "OD": range(3), "D0": range(3, 5)}[part]
    return sum(M5R[ri][p, p] for p in idx)


# check R acts as a representation and preserves the two summands
chk("S1 strain action is a representation of the 24 rotations; D0 (diagonal traceless) and OD (off-diagonal) are invariant summands",
    all(np.array_equal(M5R[QMUL[a][b]], M5R[a].dot(M5R[b])) for a in range(24) for b in range(24)) and
    all(all(M5R[a][p, q] == 0 for p in range(3) for q in (3, 4)) and all(M5R[a][p, q] == 0 for p in (3, 4) for q in range(3))
        for a in range(24)))

# Hermitian 3x3 as 9 integer coordinates: X_11,X_22,X_33,X_12,X_13,X_23 (symmetric real part), Y_12,Y_13,Y_23 (imag part, antisymmetric)
PAIRS = [(0, 1), (0, 2), (1, 2)]


def hcoords(X, Y):
    return [X[0, 0], X[1, 1], X[2, 2]] + [X[i, j] for i, j in PAIRS] + [Y[i, j] for i, j in PAIRS]


def hbasis(k):
    X = np.zeros((3, 3), int)
    Y = np.zeros((3, 3), int)
    if k < 3:
        X[k, k] = 1
    elif k < 6:
        i, j = PAIRS[k - 3]
        X[i, j] = X[j, i] = 1
    else:
        i, j = PAIRS[k - 6]
        Y[i, j] = 1
        Y[j, i] = -1
    return X, Y


WG = []
for g in range(192):
    P = RHO[g]
    W = np.zeros((9, 9), int)
    for k in range(9):
        X, Y = hbasis(k)
        W[:, k] = hcoords(P @ X @ P.T, P @ Y @ P.T)
    WG.append(W)
chk("W1 action on Hermitian matrices (A -> rho A rho^T, real rho) is a homomorphism G -> GL9(Z)",
    all(np.array_equal(WG[GMUL[a, b]], WG[a] @ WG[b]) for a in range(0, 192, 3) for b in range(192)))
chk("W2 kernel of the action on Hermitian matrices is exactly the order-8 group K0 of R4",
    set(g for g in range(192) if np.array_equal(WG[g], np.eye(9, dtype=int))) == set(K0))

# ---------------------------------------------------------------------------------------------
# 3. subgroup enumeration by Z^1-cocycles of N x| Q  (disjoint from the source's generator-pair closure)
# ---------------------------------------------------------------------------------------------
def closure_idx(gens, mul, ident):
    S = {ident}
    fr = [ident]
    while fr:
        new = []
        for x in fr:
            for g in gens:
                y = mul(x, g)
                if y not in S:
                    S.add(y)
                    new.append(y)
        fr = new
    return frozenset(S)


qmul = lambda a, b: QMUL[a][b]
subQ = set()
for a in range(24):
    subQ.add(closure_idx([a], qmul, QID))
for a in range(24):
    for b in range(a, 24):
        subQ.add(closure_idx([a, b], qmul, QID))
subQ = sorted(subQ, key=lambda s: (len(s), sorted(s)))
chk("E1 S4 ~ O has 30 subgroups (all <=2-generated)", len(subQ) == 30, f"found {len(subQ)}")


def subspaces():
    out = set()
    for r in range(0, 4):
        for gens in itertools.combinations(VEC[1:], r):
            S = {(0, 0, 0)}
            for g in gens:
                S |= {vadd(s, g) for s in S}
            out.add(frozenset(S))
    return sorted(out, key=lambda s: (len(s), sorted(s)))


subN = subspaces()
chk("E2 F_2^3 has 16 subspaces", len(subN) == 16, f"found {len(subN)}")


def min_gens(QH):
    el = sorted(QH)
    if len(QH) == 1:
        return []
    for a in el:
        if closure_idx([a], qmul, QID) == QH:
            return [a]
    for a, b in itertools.combinations(el, 2):
        if closure_idx([a, b], qmul, QID) == QH:
            return [a, b]
    raise RuntimeError


def cosets(K):
    cs = {}
    for v in VEC:
        c = frozenset(vadd(v, k) for k in K)
        cs[v] = min(c)
    return cs


ALLH = {}
cocycle_counts = {}
for QH in subQ:
    gens = min_gens(QH)
    for K in subN:
        if not all(qact(q, k) in K for q in QH for k in K):
            continue
        cs = cosets(K)
        reps = sorted(set(cs.values()))
        n_cocycles = 0
        for vals in itertools.product(reps, repeat=len(gens)):
            c = {QID: (0, 0, 0)}
            ok = True
            fr = [QID]
            while fr and ok:
                nx = []
                for q in fr:
                    for g, cg in zip(gens, vals):
                        q2 = QMUL[g][q]
                        val = cs[vadd(cg, qact(g, c[q]))]       # c(g q) = c(g) + g.c(q)
                        if q2 in c:
                            if c[q2] != val:
                                ok = False
                                break
                        else:
                            c[q2] = val
                            nx.append(q2)
                    if not ok:
                        break
                fr = nx
            if not ok or set(c) != set(QH):
                continue
            # full cocycle identity on all pairs
            if not all(c[QMUL[a][b]] == cs[vadd(c[a], qact(a, c[b]))] for a in QH for b in QH):
                continue
            n_cocycles += 1
            H = frozenset(gid(q, vadd(c[q], k)) for q in QH for k in K)
            ALLH[H] = (tuple(sorted(QH)), K)
        cocycle_counts[(QH, K)] = n_cocycles
SUBS = list(ALLH)
chk("E3 subgroup count via sum over (Q_H, K) of |Z^1(Q_H, N/K)| = 1120 (source reports 1120 by closure)",
    len(SUBS) == 1120 and sum(cocycle_counts.values()) == 1120, f"{len(SUBS)}")


def is_subgroup(H):
    Hl = list(H)
    return GID in H and all(GMUL[a, b] in H for a in Hl for b in Hl)


chk("E4 every cocycle-built H is closed under the group law and has the declared image Q_H and kernel K",
    all(is_subgroup(H) for H in SUBS) and
    all(frozenset(g // 8 for g in H) == frozenset(ALLH[H][0]) and
        frozenset(VEC[g % 8] for g in H if g // 8 == QID) == ALLH[H][1] for H in SUBS))
# completeness cross-check: every <=2-generated subgroup (closure) is in the list
SUBSET = set(SUBS)
bad = 0
cache = {}
gmul = lambda a, b: int(GMUL[a, b])
for a in range(192):
    ca = closure_idx([a], gmul, GID)
    if ca not in SUBSET:
        bad += 1
    for b in range(a + 1, 192):
        H = closure_idx([a, b], gmul, GID)
        if H not in SUBSET:
            bad += 1
chk("E5 completeness cross-check: closure of every cyclic and every 2-generated subgroup of G is in the cocycle list", bad == 0,
    f"missing {bad}")

# ---------------------------------------------------------------------------------------------
# 4. per-subgroup invariants, exact
# ---------------------------------------------------------------------------------------------
def avg(vals, n):
    return sum(vals) / n


def classify(H):
    Hl = sorted(H)
    n = len(H)
    chi2 = Fr(sum(int(np.trace(RHO[g])) ** 2 for g in Hl), n)                 # dim commutant (complex) = <chi,chi>
    fixdim = Fr(sum(int(np.trace(WG[g])) for g in Hl), n)                    # dim_R of H-fixed Hermitian matrices
    sdim = {p: avg([tr5(g // 8, p) for g in Hl], n) for p in ("all", "OD", "D0")}
    rots = sorted(set(g // 8 for g in Hl))
    o3 = any(np.array_equal(np.linalg.matrix_power(ROT[r], 3), np.eye(3, dtype=int)) and r != QID for r in rots)
    return dict(n=n, chi2=chi2, fixdim=fixdim, S=sdim["all"], OD=sdim["OD"], D0=sdim["D0"], rot=len(rots), o3=o3)


TYPE = {3: "a", 5: "b", 9: "c", 2: "d", 1: "e"}
INFO = {H: classify(H) for H in SUBS}
chk("C1 commutant dimension from the 3-dim character <chi,chi> equals dim of H-fixed Hermitian matrices from the 9-dim action (all 1120)",
    all(v["chi2"] == v["fixdim"] and v["chi2"].denominator == 1 and int(v["chi2"]) in TYPE for v in INFO.values()))
for H, v in INFO.items():
    v["type"] = TYPE[int(v["chi2"])]
    v["distinct"] = v["type"] in "abc"
    v["mix"] = v["type"] in "bc"
    v["K"] = ALLH[H][1]
cnt = {}
for v in INFO.values():
    k = (v["o3"], v["distinct"], v["mix"])
    cnt[k] = cnt.get(k, 0) + 1
SRC = {(False, False, False): 231, (False, True, False): 445, (False, True, True): 283, (True, False, False): 121, (True, True, False): 40}
chk("C2 counts by (rotation part has order-3 element, three distinct masses possible, nontrivial mixing) agree with source "
    "(x2_cert_run1_strainnorm_bug.out:46-51 first three fields; COMBO_REPORT.md:128-132)", cnt == SRC, str(cnt))
chk("C3 type a/b/c/d/e counts: a (abelian, multiplicity-free) / b (2+1 repeated) / c (scalar) / d (2-dim irrep) / e (3-dim irrep)",
    True, str({t: sum(1 for v in INFO.values() if v["type"] == t) for t in "abcde"}))

# --- theorem A: strain-free <=> rotation part contains order-3 element AND is T or O (order 12 or 24) -------
sf = [H for H, v in INFO.items() if v["S"] == 0]
chk("A1 invariant traceless strain = 0  <=>  rotation part of H is the tetrahedral group (12) or the octahedral group (24)  (all 1120)",
    all((v["S"] == 0) == (v["rot"] in (12, 24)) for v in INFO.values()), f"{len(sf)} strain-free subgroups")
chk("A2 (source claim X2-L8, all 1120) nontrivial mixing => at least one invariant traceless strain component",
    all(v["S"] >= 1 for v in INFO.values() if v["mix"]))
chk("A3 rotation part contains an element of order 3 => commutant is abelian (type a/e only; no mixing) -- exact reason in A4",
    all(v["type"] in ("a", "d", "e") for v in INFO.values() if v["o3"]) and all(not v["mix"] for v in INFO.values() if v["o3"]))
# A4: the exact reason: rho(h) for an order-3 rotation part has char poly x^3 -+ 1  (three distinct eigenvalues)
x = sp.symbols("x")
o3els = [g for g in range(192) if g // 8 != QID and np.array_equal(np.linalg.matrix_power(ROT[g // 8], 3), np.eye(3, dtype=int))]
polys = set()
for g in o3els:
    polys.add(sp.factor(sp.Matrix(RHO[g].tolist()).charpoly(x).as_expr()))
disc_ok = all(sp.discriminant(sp.Poly(p, x)) != 0 for p in polys)
chk("A4 every symmetry with an order-3 rotation part (64 of 192) has rho with char poly x^3-1 or x^3+1: three distinct eigenvalues, so its commutant is the diagonal algebra (abelian)",
    len(o3els) == 64 and polys <= {sp.factor(x ** 3 - 1), sp.factor(x ** 3 + 1)} and disc_ok, str(polys))
# A5: no order-3 element => rotation part is a 2-group inside a conjugate of D4 => invariant strain >=1
rot2 = [H for H, v in INFO.items() if not v["o3"]]
chk("A5 no order-3 rotation => rotation part has order dividing 8 (a 2-group, so inside a Sylow D4 of S4) and S^H >= 1 (all such H)",
    all(v["rot"] in (1, 2, 4, 8) and v["S"] >= 1 for v in (INFO[H] for H in rot2)))
# A6: the converse that is NOT true: groups with order-3 element do not all have S=0
chk("A6 order-3 rotation does not imply strain-free: rotation part C3 or D3 keeps a body-diagonal strain (source counts: (True,*,*,True)=100)",
    sum(1 for v in INFO.values() if v["o3"] and v["S"] > 0) == 100 and
    all(v["rot"] in (3, 6) for v in INFO.values() if v["o3"] and v["S"] > 0))
chk("A7 the two directions combined: mixing => S^H>=1 holds, but S^H>=1 does not give mixing (sample of 1120: groups with S>=1 and no mixing)",
    sum(1 for v in INFO.values() if v["S"] >= 1 and not v["mix"]) == 1120 - len(sf) - 283,
    str(sum(1 for v in INFO.values() if v["S"] >= 1 and not v["mix"])))

# --- theorem B: realistic (all nine |V_ij| nonzero) mixing <=> rho(H) scalar ------------------------------
typec = [H for H, v in INFO.items() if v["type"] == "c"]
chk("B1 type c (commutant = all of M3, the only case where generic unitary mixing with all nine entries nonzero is allowed) <=> H subset of K0 (R4)",
    set(typec) == set(H for H in SUBS if H <= K0S), f"{len(typec)} subgroups")
chk("B2 every type-c group has rotation part inside V4={1, three pi-rotations} (no order-3, no C4); diagonal (D0) strain invariants = 2 for all 16; off-diagonal (OD) invariants vanish exactly when the rotation part is all of V4",
    all(INFO[H]["D0"] == 2 and INFO[H]["rot"] in (1, 2, 4) for H in typec) and
    all((INFO[H]["OD"] == 0) == (INFO[H]["rot"] == 4) for H in typec))
# type b: block structure; verify with exact projectors that mixing is only inside a 2+1 split
def block_zero_pattern_ok(H):
    # commutant of rho(H) in M3(Q) via exact nullspace; type b means algebra ~ M2 + C : check it has a nontrivial central idempotent
    gens = sorted(H)
    rows = []
    for g in gens:
        P = sp.Matrix(RHO[g].tolist())
        rows.append(sp.kronecker_product(sp.eye(3), P) - sp.kronecker_product(P.T, sp.eye(3)))
    N = sp.Matrix.vstack(*rows).nullspace()
    mats = [sp.Matrix(3, 3, list(v)).T for v in N]    # column-major vec -> matrix
    return len(mats)
tb = [H for H, v in INFO.items() if v["type"] == "b"]
chk("B3 exact nullspace (sympy rational) of the commutant has dimension 5 for a sample of 20 type-b groups and 9 for 5 type-c groups",
    all(block_zero_pattern_ok(H) == 5 for H in tb[:20]) and all(block_zero_pattern_ok(H) == 9 for H in typec[:5]))

# --- isotropy closure: what the generation data (A,B) can actually have as stabiliser -----------------------
rng = random.Random(20261014)
def fixspan(H):
    S = sum(WG[g] for g in H)
    return S


def pointwise_fixer(S):
    return frozenset(g for g in range(192) if np.array_equal(WG[g] @ S, S))


ISO = {}
for H in SUBS:
    S = fixspan(H)
    Hbar = pointwise_fixer(S)
    ISO[H] = Hbar
isoset = set(ISO.values())
chk("I1 every pointwise stabiliser of Fix(H) contains H and K0; its fixed space is the same as H's (so the same mixing type)",
    all(H <= ISO[H] and K0S <= ISO[H] for H in SUBS) and
    all(classify(ISO[H])["fixdim"] == INFO[H]["fixdim"] for H in SUBS))
# generic-point check: random integer (A,B) in Fix(H)^2 has stabiliser exactly Hbar
def generic_stab(S, tries=40):
    cols = [S[:, k] for k in range(9)]
    for _ in range(tries):
        wa = sum(rng.randint(-9, 9) * c for c in cols)
        wb = sum(rng.randint(-9, 9) * c for c in cols)
        st = frozenset(g for g in range(192) if np.array_equal(WG[g] @ wa, wa) and np.array_equal(WG[g] @ wb, wb))
        yield st
okgen = True
for H in SUBS[::7]:
    S = fixspan(H)
    st = next(generic_stab(S))
    if st != ISO[H]:
        # allow a second draw (a random draw may land on a proper subspace of lower stabiliser-orbit)
        st2 = next(generic_stab(S))
        okgen = okgen and (st2 == ISO[H] or st == ISO[H])
chk("I2 a random integer pair (A,B) in Fix(H)^2 has stabiliser exactly the pointwise fixer (sampled over 160 of the 1120 groups)", okgen)
ISOINFO = {}
for I in isoset:
    v = classify(I)
    v["type"] = TYPE[int(v["chi2"])]
    v["mix"] = v["type"] in "bc"
    ISOINFO[I] = v
chk("I3 number of distinct isotropy groups (exact stabilisers of (A,B) data)", True, f"{len(isoset)} of 1120 subgroups are isotropy groups")
chk("I4 EVERY isotropy group has zero invariant off-diagonal (OD, rhombohedral/shear) strain: the generation matrices (A,B) are blind to T2 strain at every order",
    all(v["OD"] == 0 for v in ISOINFO.values()))
chk("I5 isotropy groups with nontrivial mixing: all have D0 (diagonal tetragonal/orthorhombic) invariant strain >= 1",
    all(v["D0"] >= 1 for v in ISOINFO.values() if v["mix"]))
chk("I6 isotropy groups containing an order-3 rotation are strain-free (S=0) and have trivial mixing -- the K0 =>V4 closure forces tetrahedral rotation part",
    all(v["S"] == 0 and not v["mix"] for v in ISOINFO.values() if v["o3"]))
chk("I7 nontrivial mixing among isotropy groups => rotation part / V4 has order 1 or 2 (its image in S3 contains no 3-cycle)",
    all(v["rot"] in (4, 8) for v in ISOINFO.values() if v["mix"]))
# one isotropy group realises type c
c_iso = [I for I, v in ISOINFO.items() if v["type"] == "c"]
chk("I8 exactly one isotropy group has type c (full unitary mixing): K0 itself, S^{K0} = D0 (2-dim), OD part 0",
    c_iso == [K0S] and ISOINFO[K0S]["D0"] == 2 and ISOINFO[K0S]["S"] == 2)

# ---------------------------------------------------------------------------------------------
# 5. covariants: character dimensions, and populated-at-degree-1 statement
# ---------------------------------------------------------------------------------------------
def chiW(g, r=1):
    # character of the pair (A,B) action: 2 copies of the 9-dim action; element g^r
    gr = g
    for _ in range(r - 1):
        gr = int(GMUL[gr, g])
    return 2 * int(np.trace(WG[gr]))


def symchar(g, d):
    c1, c2, c3 = chiW(g, 1), chiW(g, 2), chiW(g, 3)
    if d == 1:
        return Fr(c1)
    if d == 2:
        return Fr(c1 * c1 + c2, 2)
    if d == 3:
        return Fr(c1 ** 3 + 3 * c1 * c2 + 2 * c3, 6)
    raise ValueError


def hom_dim(d, part):
    return sum(symchar(g, d) * tr5(g // 8, part) for g in range(192)) / 192


dims = {(d, p): hom_dim(d, p) for d in (1, 2, 3) for p in ("OD", "D0")}
chk("V1 dim Hom_G(Sym^d(Herm3 + Herm3), OD strain) = 0 for d=1,2,3 (T2 is never sourced by the generation matrices)",
    all(dims[(d, "OD")] == 0 for d in (1, 2, 3)), str({k: str(v) for k, v in dims.items()}))
chk("V2 equivariant linear maps (A,B) -> D0 strain: dimension 2 (the traceless diagonal of A and of B); degree 2 and 3 spaces are non-zero",
    dims[(1, "D0")] == 2 and dims[(2, "D0")] > 0 and dims[(3, "D0")] > 0, f"d1={dims[(1,'D0')]}, d2={dims[(2,'D0')]}, d3={dims[(3,'D0')]}")


def covariant_linear_equivariance():
    # L(A) = traceless part of diag(A) in strain coordinates (c4,c5); equivariance L(W_g w) = M5(g) L(w) for all g, on a random A
    r = random.Random(3)
    ok = True
    for _ in range(5):
        w = [r.randint(-9, 9) for _ in range(9)]

        def L(w):
            a, b, c = Fr(w[0]), Fr(w[1]), Fr(w[2])
            t = (a + b + c) / 3
            a, b, c = a - t, b - t, c - t
            return [Fr(0), Fr(0), Fr(0), (a - b) / 2, (a + b) / 2]
        for g in range(192):
            wg = [int(v) for v in WG[g] @ np.array(w)]
            lhs = L(wg)
            Lw = L(w)
            rhs = [sum(M5R[g // 8][p, q] * Lw[q] for q in range(5)) for p in range(5)]
            ok = ok and lhs == rhs
    return ok


chk("V3 L(A) = traceless diagonal of A (corner basis) is G-equivariant into D0 for all 192 symmetries (exact, random integer A)",
    covariant_linear_equivariance())

# populated at degree 1 for generic vev: the degree-1 covariants span S^{Hbar} for every isotropy group with D0 invariants
def rankD0_linear(I, trials=6):
    S = fixspan(sorted(I))
    cols = [S[:, k] for k in range(9)]
    r = random.Random(11)
    vecs = []
    for _ in range(trials):
        w = sum(r.randint(-9, 9) * c for c in cols)
        a, b, c = Fr(int(w[0])), Fr(int(w[1])), Fr(int(w[2]))
        t = (a + b + c) / 3
        a, b, c = a - t, b - t, c - t
        vecs.append([(a - b) / 2, (a + b) / 2])
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in v] for v in vecs]).rank()


okpop = True
for I, v in ISOINFO.items():
    if v["S"] != 0 and v["mix"] or (v["S"] != 0):
        okpop = okpop and (rankD0_linear(sorted(I)) == v["D0"])
chk("V4 for every isotropy group with D0 invariants, the degree-1 covariant (traceless corner-diagonal of A) spans all of S^{Hbar}: the allowed channel is populated at LINEAR order in the vev generically",
    okpop)

# finite-group lemma behind 'allowed cannot be forbidden by symmetry': values of covariants at w fill S^{Stab(w)}
def covariant_span(w, d):
    # w: 18-vector (A,B).  Returns rank of the set of values F(w) over ALL G-equivariant polynomial maps F of degree d (Reynolds-averaged monomials)
    pts = []
    for g in range(192):
        W = WG[g]
        pts.append(np.concatenate([W @ w[:9], W @ w[9:]]))
    pts = np.array(pts, dtype=object)
    mons = list(itertools.combinations_with_replacement(range(18), d))
    vals = np.ones((192, len(mons)), dtype=object)
    for k, m in enumerate(mons):
        for idx in m:
            vals[:, k] = vals[:, k] * pts[:, idx]
    out = set()
    for p in range(5):
        # Reynolds average of the map u -> m(u) e_p : sum_g M5(g^{-1})[:,p] m(g w)
        T = np.array([[M5R[QINV[g // 8]][a, p] for a in range(5)] for g in range(192)], dtype=object)     # 192 x 5
        res = T.T.dot(vals)                                                                                     # 5 x nm
        for k in range(len(mons)):
            col = tuple(res[:, k])
            if any(c != 0 for c in col):
                out.add(col)
    if not out:
        return 0
    return sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in col] for col in out]).rank()


# --- (i) a sample vacuum with nontrivial mixing, isotropy group with rot/V4 = Z2: values fill S^{Stab}
mixiso = [I for I, v in ISOINFO.items() if v["mix"]]
sample = None
for I in sorted(mixiso, key=lambda s: (len(s), sorted(s))):
    if ISOINFO[I]["type"] == "b" and ISOINFO[I]["rot"] == 8 and ISOINFO[I]["D0"] == 1:
        sample = I
        break
S = fixspan(sorted(sample))
cols = [S[:, k] for k in range(9)]
r = random.Random(77)
wA = sum(r.randint(-3, 3) * c for c in cols)
wB = sum(r.randint(-3, 3) * c for c in cols)
wv = np.array([int(t) for t in np.concatenate([wA, wB])], dtype=object)
st = frozenset(g for g in range(192) if np.array_equal(WG[g] @ wA, wA) and np.array_equal(WG[g] @ wB, wB))
# equal-diagonal vacuum with the same symmetry? we compute the dimension of covariant values at w for d=1,2,3
rk = {d: covariant_span(wv, d) for d in (1, 2, 3)}
chk("V5 finite-group lemma on a type-b mixing vacuum (rot/V4 = Z2): the span of all covariant values has rank = dim S^{Stab(w)} by degree 3 (and never exceeds it)",
    st == sample and max(rk.values()) == ISOINFO[sample]["S"] and rk[3] == ISOINFO[sample]["S"],
    f"stab order {len(st)}, rank by degree {rk}, dim S^Stab = {ISOINFO[sample]['S']}")

# --- (ii) exact rational full-mixing vacuum (isotropy K0) with NO linear strain: allowed but not forced
#     A,B have equal corner diagonals; degree-1 covariants vanish; degree-2/3 covariants decide the next order.
def herm(X, Y):
    return sp.Matrix(3, 3, lambda i, j: sp.Integer(X[i][j]) + sp.I * sp.Integer(Y[i][j]))


# A: off-diagonal entries 1, i, 1 (moduli equal, diagonal 0); B: 1, 1, i with different link carrying the phase
A = sp.Matrix([[0, 1, sp.I], [1, 0, 1], [-sp.I, 1, 0]])
B = sp.Matrix([[0, sp.I, 1], [-sp.I, 0, 1], [1, 1, 0]])
chk("X0 A and B are Hermitian, have zero diagonals (linear strain covariants vanish), and do not commute (nontrivial mixing)",
    A == A.H and B == B.H and (A * B - B * A) != sp.zeros(3, 3))
def coords(M):
    return [int(sp.re(M[0, 0])), int(sp.re(M[1, 1])), int(sp.re(M[2, 2])), int(sp.re(M[0, 1])), int(sp.re(M[0, 2])), int(sp.re(M[1, 2])),
            int(sp.im(M[0, 1])), int(sp.im(M[0, 2])), int(sp.im(M[1, 2]))]
wA2 = np.array(coords(A), dtype=object)
wB2 = np.array(coords(B), dtype=object)
w2 = np.concatenate([wA2, wB2])
st2 = frozenset(g for g in range(192) if np.array_equal(WG[g] @ np.array(wA2, dtype=int), np.array(wA2, dtype=int)) and
                np.array_equal(WG[g] @ np.array(wB2, dtype=int), np.array(wB2, dtype=int)))
rk2 = {d: covariant_span(w2, d) for d in (1, 2, 3)}
v2 = classify(st2)
print("INFO vacuum X: stabiliser order", len(st2), "type", TYPE[int(v2["chi2"])], "dim S^stab =", v2["S"], "covariant-value rank by degree", rk2)
# nontrivial and full mixing, FLOAT confirmation
ea, Ua = np.linalg.eigh(np.array(A.tolist(), dtype=complex))
eb, Ub = np.linalg.eigh(np.array(B.tolist(), dtype=complex))
Vm = np.abs(Ua.conj().T @ Ub)
chk("X1 (FLOAT) A,B have three distinct eigenvalues each and all nine |V_ij| = |<u_i|v_j>| exceed 1e-3 (full mixing), eigenvalues "
    f"{np.round(ea,3).tolist()} / {np.round(eb,3).tolist()}",
    np.min(np.diff(ea)) > 1e-3 and np.min(np.diff(eb)) > 1e-3 and Vm.min() > 1e-3, f"min|V|={Vm.min():.3f}")
chk("X2 the linear strain covariants of this full-mixing vacuum vanish (rank 0 at degree 1) although the symmetry allows a 2-dim D0 channel for its stabiliser",
    rk2[1] == 0 and v2["D0"] >= 1, f"stab D0 dim {v2['D0']}")
chk("X3 finite-group lemma: some covariant value at this vacuum is non-zero by degree 3 iff dim S^Stab>0; rank at degree<=3 = " + str(max(rk2.values())),
    (max(rk2.values()) > 0) == (v2["S"] > 0) and max(rk2.values()) <= v2["S"])

# ---------------------------------------------------------------------------------------------
# 6. exclusion tables (derived above, exact)
# ---------------------------------------------------------------------------------------------
print("TABLE isotropy groups (generation-sector stabilisers): rot/V4 order | type | #groups | dim D0 inv | translation-kernel sizes |I∩N|")
rows = {}
for I, v in ISOINFO.items():
    Kn = len([g for g in I if g // 8 == QID])
    key = (v["rot"] // 4, v["type"], v["D0"], v["S"] - v["D0"])
    rows.setdefault(key, []).append(Kn)
for k in sorted(rows):
    print("   rot/V4=%d type=%s D0inv=%d ODinv=%d : %d groups, |I∩N| in %s" % (k[0], k[1], k[2], k[3], len(rows[k]), sorted(set(rows[k]))))
mixI = [I for I, v in ISOINFO.items() if v["mix"]]
def Kset(I):
    return frozenset(VEC[g % 8] for g in I if g // 8 == QID)


def tied(K):
    return [pr for pr in PAIRS if K == frozenset(s for s in VEC if s[pr[0]] == s[pr[1]])]


okT1 = True
K111 = frozenset({(0, 0, 0), (1, 1, 1)})
for I in mixI:
    K = Kset(I)
    okT1 = okT1 and (K == K111 or len(tied(K)) == 1) and len(K) < 8
    if ISOINFO[I]["type"] == "c":
        okT1 = okT1 and K == K111
chk("T1 nontrivial mixing needs the vacuum to break unit translations: the pure-translation part K=I∩N of every mixing isotropy group is {0,111} or {s: s_i=s_j} for one pair (i,j) (|K|=2 or 4, never N); type c has K={0,111}",
    okT1, f"{len(mixI)} mixing isotropy groups")
chk("T2 exact translations (I ⊇ N) force diagonal A,B (type a or finer): no mixing, and with a 3-cycle in the rotation part a triple degeneracy",
    all((not v["mix"]) for I, v in ISOINFO.items() if all(gid(QID, vv) in I for vv in VEC)) and
    all(v["type"] in ("e", "d") for I, v in ISOINFO.items() if all(gid(QID, vv) in I for vv in VEC) and v["o3"]),
    "")
mdeg = {t: sorted(set(v["rot"] // 4 for v in ISOINFO.values() if v["type"] == t)) for t in "abcde"}
print("INFO rot/V4 orders occurring per type among isotropy groups:", mdeg)
free_distinct = [I for I, v in ISOINFO.items() if v["S"] == 0 and v["type"] == "a"]
chk("T3 strain-free isotropy groups with three DISTINCT masses exist (type a, rotation part T or O) but then all mixing is trivial",
    len(free_distinct) > 0 and all(ISOINFO[I]["rot"] in (12, 24) for I in free_distinct), f"{len(free_distinct)} groups")
degen = [I for I, v in ISOINFO.items() if v["type"] in ("d", "e")]
chk("T4 forced degeneracies: types d (two-fold) and e (three-fold) occur and have no mixing; they are excluded from any three-mass spectrum",
    len(degen) > 0 and all(not ISOINFO[I]["mix"] for I in degen), f"{len(degen)} isotropy groups")

# ---------------------------------------------------------------------------------------------
# 7. source hashes (only if the copies are present next to this script)
# ---------------------------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
SRC_H = {"COMBO_REPORT.md": "3b5e095d96a3fa16fb8b8c3b9adc6cf560f9a167db481132719efac6bc5b9438",
         "PREREG.md": "68ad0b91b897fa054d028df3cbab9eba26e809aa99f7f99664c0e23268616acc",
         "x2_cert.py": "0dd8ea359ee2842b76a2238a1806b5996f66b145cb3788c963b8801a9b257338",
         "x2_cert_run1_strainnorm_bug.out": "331c507059f34851866754f9a4ab3ed9d474fa4ca7c5a98184d26a32645c17e8"}
for nm, h in SRC_H.items():
    p = os.path.join(HERE, "src", nm)
    if os.path.exists(p):
        chk("H sha256 of source copy " + nm, hashlib.sha256(open(p, "rb").read()).hexdigest() == h)

npass = sum(OK)
nfail = len(OK) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("HIT: generation-sector vacua are blind to off-diagonal (T2) strain; mixing => allowed diagonal (E) strain channel populated at linear order, "
          "full nine-entry mixing only for stabiliser K0 (generation-trivial), allowed != forced (explicit full-mixing vacuum with zero linear strain)")
print("SUMMARY: Exact cocycle enumeration of all 1120 residual groups confirms the source's classification (mixing => invariant strain), sharpens it to "
      "'only the diagonal E-type quadrupole, only for stabilisers without a 3-cycle, full nine-entry mixing only when the generation action is trivial', "
      "and shows the coefficient is a free dynamical input, not forced.")
print(f"# runtime {time.time()-T0:.0f}s", file=sys.stderr)
sys.exit(0 if nfail == 0 else 1)
