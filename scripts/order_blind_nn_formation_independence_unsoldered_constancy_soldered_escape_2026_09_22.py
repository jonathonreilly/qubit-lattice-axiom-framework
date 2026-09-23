#!/usr/bin/env python3
"""Order-blind nearest-neighbour formation: independence beyond neighbours,
constancy under the unsoldered reading, and the soldered escape, exact.

Supplied conditional finite models; no physical formation law is inferred.  Exact rational arithmetic throughout; no floating point enters
any check.

Declared objects
  * Z^3 windows: the 3-site path x-y-z along e_z and the 7-site cross (a site
    with its six neighbours); the proper cubic group O (24 signed permutation
    matrices of determinant +1) acting on positions, and under the soldered
    reading on values too;
  * nearest-neighbour formation rules r(a | N), N a partial map from the six
    directions to formed neighbour values, used sequentially along a
    formation order (the formation reading of the Admissibility sentence);
  * finite soldered alphabets: the cube orbits of sizes 6, 8, 12, 24 and the
    48-point union of the two proper-rotation orbits of (1, 2, 3) (the chiral
    pair), with the uniform one-site law; the continuum Bloch sphere with
    Haar measure, whose push-forward to t = a.d is uniform on [-1, 1];
  * binary comparison laws from the record-dynamics and clock-and-rate
    blocks: the chain rule of the nearest-neighbour pair measure (order-blind,
    conditions beyond neighbours) and the local rule proportional to
    2^(formed neighbours agreeing) (nearest-neighbour, order-sensitive).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

AUDIT_TIMEOUT_SEC = 120
RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


# ---------------------------------------------------------------- geometry
def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def cubic_group():
    G = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            A = [[0] * 3 for _ in range(3)]
            for i in range(3):
                A[i][perm[i]] = signs[i]
            A = tuple(tuple(r) for r in A)
            if det3(A) == 1:
                G.append(A)
    return G


def mv(g, v):
    return tuple(sum(g[i][j] * v[j] for j in range(3)) for i in range(3))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def neg(v):
    return tuple(-x for x in v)


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


O = cubic_group()
EX, EY, EZ = (1, 0, 0), (0, 1, 0), (0, 0, 1)
DIRS = (EX, neg(EX), EY, neg(EY), EZ, neg(EZ))


def orbit(p):
    return sorted({mv(g, p) for g in O})


# ---------------------------------------------------------------- the 48-point soldered rule
A24P = orbit((1, 2, 3))
A48 = sorted(set(A24P) | set(orbit((1, 2, -3))))
CHI = {a: (1 if a in set(A24P) else -1) for a in A48}
XT = {(d, a): (CHI[a] if dot(a, d) == 3 else 0) for d in DIRS for a in A48}
KAPPA = Fr(1, 2)
R0_48 = Fr(1, 48)


def phi48(d, a, b):
    """Bond factor for a formed neighbour at direction d with value b."""
    return 1 + KAPPA * XT[(d, a)] * XT[(neg(d), b)]


def rule48(a, N):
    p = R0_48
    for d, b in N.items():
        p *= phi48(d, a, b)
    return p


def nbr_condition(site, formed):
    return {d: formed[vadd(site, d)] for d in DIRS if vadd(site, d) in formed}


def finished_law(sites, alphabet, rule, order):
    """Exact finished-record law of one formation order (dict: config tuple -> mass)."""
    law = {}
    for cfg in product(alphabet, repeat=len(sites)):
        val = dict(zip(sites, cfg))
        formed = {}
        p = Fr(1)
        for s in order:
            p *= rule(val[s], nbr_condition(s, formed))
            if p == 0:
                break
            formed[s] = val[s]
        if p:
            law[cfg] = p
    return law


print("== 1. Order-blind nearest-neighbour laws are independent beyond neighbours ==")
check("48-point alphabet: two proper-rotation orbits of 24 (the chiral pair); every point has one coordinate +-3",
      len(A24P) == 24 and len(A48) == 48 and all(sum(1 for c in a if abs(c) == 3) == 1 for a in A48))
PATH = ((0, 0, 0), (0, 0, 1), (0, 0, 2))
LAWS = {o: finished_law(PATH, A48, rule48, o) for o in permutations(PATH)}
BASE = LAWS[PATH]
check("soldered 48-point rule on the 3-site path: all 6 formation orders give one exact finished law",
      all(L == BASE for L in LAWS.values()) and sum(BASE.values()) == 1,
      f"{len(BASE)} atoms; order-blind by direct computation, not by assumption")
MARG_XZ = {}
for (ax, ay, az), m in BASE.items():
    MARG_XZ[(ax, az)] = MARG_XZ.get((ax, az), Fr(0)) + m
check("non-adjacent sites x, z are exactly independent with the one-site law: all 2304 pair masses = 1/48^2",
      len(MARG_XZ) == 2304 and set(MARG_XZ.values()) == {R0_48 * R0_48})
C_XY = sum(m * XT[(EZ, ax)] * XT[(neg(EZ), ay)] for (ax, ay, az), m in BASE.items())
C_YZ = sum(m * XT[(EZ, ay)] * XT[(neg(EZ), az)] for (ax, ay, az), m in BASE.items())
check("adjacent sites stay correlated: E[X_z(a_x) X_-z(a_y)] = kappa/36 = 1/72 on both bonds",
      C_XY == KAPPA / 36 == C_YZ == Fr(1, 72))

# binary comparison laws on the same path
B2 = (1, -1)
EDGES_P = ((PATH[0], PATH[1]), (PATH[1], PATH[2]))
MUW = {cfg: Fr(2) ** sum(1 for s, t in EDGES_P if dict(zip(PATH, cfg))[s] == dict(zip(PATH, cfg))[t])
       for cfg in product(B2, repeat=3)}
ZMU = sum(MUW.values())


def chain_rule(a, s, formed):
    """Chain rule of the nearest-neighbour pair measure: conditions on every formed site."""
    def w(assign):
        tot = Fr(0)
        for cfg, x in MUW.items():
            c = dict(zip(PATH, cfg))
            if all(c[k] == v for k, v in assign.items()):
                tot += x
        return tot
    base = w(formed)
    new = dict(formed)
    new[s] = a
    return w(new) / base


def law_general(rule_fn, order):
    law = {}
    for cfg in product(B2, repeat=3):
        val = dict(zip(PATH, cfg))
        formed, p = {}, Fr(1)
        for s in order:
            p *= rule_fn(val[s], s, formed)
            formed[s] = val[s]
        law[cfg] = p
    return law


def corr_xz(law):
    ex = sum(m * c[0] for c, m in law.items())
    ez = sum(m * c[2] for c, m in law.items())
    return sum(m * c[0] * c[2] for c, m in law.items()) - ex * ez


CHAIN_LAWS = [law_general(chain_rule, o) for o in permutations(PATH)]
check("comparison: the pair-measure chain rule is order-blind on the path, yet x and z correlate at 1/9",
      all(L == CHAIN_LAWS[0] for L in CHAIN_LAWS) and corr_xz(CHAIN_LAWS[0]) == Fr(1, 9),
      "consistent with independence beyond neighbours only because the chain rule is not nearest-neighbour")
check("the chain rule's conditional for z given x alone (y unformed) is 5/9 against 4/9: it reads a non-neighbour",
      chain_rule(1, PATH[2], {PATH[0]: 1}) == Fr(5, 9) and chain_rule(1, PATH[2], {PATH[0]: -1}) == Fr(4, 9))


def local_rule(a, s, formed):
    nb = [formed[vadd(s, d)] for d in DIRS if vadd(s, d) in formed]
    ka = sum(1 for v in nb if v == a)
    return Fr(2) ** ka / (Fr(2) ** ka + Fr(2) ** (len(nb) - ka))


L_CHAIN_ORDER = law_general(local_rule, PATH)
L_ENDS_FIRST = law_general(local_rule, (PATH[0], PATH[2], PATH[1]))
check("comparison: the local rule 2^(agreeing neighbours) gives c(x,z) = 1/9 chain-first but 0 ends-first",
      corr_xz(L_CHAIN_ORDER) == Fr(1, 9) and corr_xz(L_ENDS_FIRST) == 0,
      "nearest-neighbour but order-sensitive: exactly the case the independence theorem leaves open")

print()
print("== 2. The exact form of order-blind nearest-neighbour rules (48-point soldered rule) ==")
check("bond symmetry phi_d(a, b) = phi_-d(b, a) on all 6 directions and 48 x 48 value pairs",
      all(phi48(d, a, b) == phi48(neg(d), b, a) for d in DIRS for a in A48 for b in A48))
check("disjoint supports: every value lies in the support of exactly one direction's function X_d",
      all(sum(1 for d in DIRS if XT[(d, a)] != 0) == 1 for a in A48)
      and all(sum(XT[(d, a)] for a in A48) == 0 for d in DIRS),
      "each X_d has mean 0 under the uniform one-site law")
CLASS_VALS = (-1, 0, 1)


def class_product(a, dset, xs):
    """Product of bond factors when the neighbour at direction d has X_-d(value) = x."""
    p = Fr(1)
    for d, x in zip(dset, xs):
        p *= 1 + KAPPA * XT[(d, a)] * x
    return p


norm_ok = True
n_conditions = 0
for k in range(7):
    for dset in combinations(DIRS, k):
        for xs in product(CLASS_VALS, repeat=k):
            n_conditions += 1
            norm_ok = norm_ok and sum(R0_48 * class_product(a, dset, xs) for a in A48) == 1
check("normalisation for every neighbour condition: all 4^6 = 4096 value classes of partial maps sum to 1",
      norm_ok and n_conditions == 4096,
      "the rule depends on a neighbour value b only through X_-d(b) in {-1, 0, 1}")
check("soldered covariance: X_gd(g a) = X_d(a) for all 24 rotations, 6 directions, 48 values",
      all(XT[(mv(g, d), mv(g, a))] == XT[(d, a)] for g in O for d in DIRS for a in A48))
check("the rule varies with the nearest-neighbour conditions, as Admissibility requires",
      any(rule48(a, {EZ: b}) != R0_48 for a in A48 for b in A48)
      and max(rule48(a, {EZ: b}) for a in A48 for b in A48) == Fr(3, 96)
      and min(rule48(a, {EZ: b}) for a in A48 for b in A48) == Fr(1, 96))

print()
print("== 3. Unsoldered reading: direction-blind bond factors force a constant rule ==")
B_UP = next(b for b in A48 if XT[(neg(EZ), b)] == 1)
UNSOLD = sum(R0_48 * phi48(EZ, a, B_UP) ** 2 for a in A48)
check("direction-blind copy of the 48-point factor: two neighbours with one value give total mass 25/24",
      sum(R0_48 * phi48(EZ, a, B_UP) for a in A48) == 1 and UNSOLD == Fr(25, 24),
      "E[phi^2] = 1 + Var(phi): normalisation for two equal neighbours forces Var(phi) = 0")
SIX = orbit((0, 0, 1))


def potts_rule(kappa):
    def r(a, N):
        w = {x: Fr(1) for x in SIX}
        for b in N.values():
            for x in SIX:
                if x == b:
                    w[x] *= 1 + kappa
        return w[a] / sum(w.values())
    return r


def cross_exchange_gap(r, a, b, c):
    """Centre with a formed leaf value c at +x; exchange with the leaf at +z (its own condition)."""
    lhs = r(a, {EX: c}) * r(b, {neg(EZ): a})
    rhs = r(b, {}) * r(a, {EX: c, EZ: b})
    return lhs - rhs


gaps = {k: cross_exchange_gap(potts_rule(k), EX, EX, EX) for k in (Fr(-1, 2), Fr(1, 2), Fr(1), Fr(2))}
check("unsoldered Potts rules on the six-axis alphabet fail exchange on the 7-site cross for every sampled nonzero kappa",
      all(g != 0 for g in gaps.values()) and cross_exchange_gap(potts_rule(Fr(0)), EX, EX, EX) == 0
      and gaps[Fr(1)] == Fr(4, 49) - Fr(2, 27),
      "kappa = 1: 4/49 against 2/27; only kappa = 0 (constant, no variation) is order-blind")

print()
print("== 4. Soldered continuum: an order-blind rule that varies, via disjoint polar caps ==")


def pint(coeffs, lo, hi):
    """Exact integral of sum c_k t^k over [lo, hi]."""
    return sum(c * (Fr(hi) ** (k + 1) - Fr(lo) ** (k + 1)) / (k + 1) for k, c in enumerate(coeffs))


CAP = Fr(3, 4)
XPOLY = (Fr(-7, 8), Fr(1))                     # X(t) = t - 7/8 on the cap t > 3/4
X2POLY = (Fr(49, 64), Fr(-7, 4), Fr(1))        # X(t)^2
MEAN_X = pint(XPOLY, CAP, 1) / 2
MEAN_X2 = pint(X2POLY, CAP, 1) / 2
check("cap profile X(t) = (t - 7/8) 1[t > 3/4]: Haar mean exactly 0, second moment exactly 1/1536",
      MEAN_X == 0 and MEAN_X2 == Fr(1, 1536),
      "Haar push-forward of t = a.d is uniform on [-1, 1]: integrals are exact polynomial integrals")
check("the six caps {a.d > 3/4} are pairwise disjoint: opposite caps trivially, perpendicular since 2(3/4)^2 > 1",
      2 * CAP * CAP > 1 and all(dot(d, e) in (0, -1) for d, e in combinations(DIRS, 2)),
      "so a product of bond factors at distinct directions is 1 + a sum of single terms")
KAP_C = Fr(32)
check("with kappa = 32 every bond factor 1 + kappa X(a.d) X(-b.d) lies in [1/2, 3/2]: strictly positive",
      1 - KAP_C * Fr(1, 64) == Fr(1, 2) and 1 + KAP_C * Fr(1, 64) == Fr(3, 2))
check("nearest-neighbour record correlation E[X_d(a_x) X_-d(a_y)] = kappa/1536^2 = 1/73728, nothing beyond",
      KAP_C * MEAN_X2 * MEAN_X2 == Fr(1, 73728))
def cap_x(t):
    return Fr(t) - Fr(7, 8) if Fr(t) > CAP else Fr(0)


def cap_phi(d, a, b):
    """Bond factor on unit vectors a, b for a neighbour at direction d."""
    return 1 + KAP_C * cap_x(dot(a, d)) * cap_x(-dot(b, d))


check("soldered, not unsoldered: rotations preserve every a.d, but the factor depends on the bond direction",
      all(dot(mv(g, a), mv(g, d)) == dot(a, d) for g in O for a in ((1, 2, 3), (3, -1, 2)) for d in DIRS)
      and cap_phi(EZ, EZ, neg(EZ)) == Fr(3, 2) and cap_phi(EX, EZ, neg(EZ)) == 1
      and cap_phi(EZ, EZ, neg(EZ)) == cap_phi(neg(EZ), neg(EZ), EZ),
      "at a = e_z, b = -e_z: factor 3/2 across a z-bond, 1 across an x-bond; bond-symmetric")

print()
print("== 5. Soldered cube orbits: which alphabets admit an order-blind rule that varies ==")


def inv3(g):
    return tuple(tuple(g[j][i] for j in range(3)) for i in range(3))


def pull(g, A):
    """(g f)(a) = f(g^-1 a) as an index map on the alphabet A."""
    idx = {a: i for i, a in enumerate(A)}
    gi = inv3(g)
    return [idx[mv(gi, a)] for a in A]


def nullspace(rows, n):
    """Exact basis of {x in Q^n : rows . x = 0}."""
    M = [list(map(Fr, r)) for r in rows]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        M[r] = [x / M[r][c] for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fr(0)] * n
        v[fcol] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fcol]
        basis.append(v)
    return basis


RZ = next(g for g in O if mv(g, EX) == EY and mv(g, EZ) == EZ)
G_TO = {d: next(g for g in O if mv(g, EZ) == d) for d in DIRS}


def pair_forms(A, eps):
    """Eigenline basis of the quarter-turn about z (eigenvalue eps, mean zero) and the two
    pair-condition quadratic forms: w against its opposite-bond and perpendicular-bond copies."""
    n = len(A)
    PR = pull(RZ, A)
    rows = [[(1 if j == PR[i] else 0) - (eps if j == i else 0) for j in range(n)] for i in range(n)]
    rows.append([1] * n)
    B = nullspace(rows, n)

    def form(d):
        P = pull(G_TO[d], A)
        k = len(B)
        M = [[sum(B[i][a] * B[j][P[a]] for a in range(n)) for j in range(k)] for i in range(k)]
        return [[(M[i][j] + M[j][i]) / 2 for j in range(k)] for i in range(k)]
    return B, form(neg(EZ)), form(EX)


def rank1_semidefinite(M):
    k = len(M)
    return len(nullspace(M, k)) == k - 1


def only_zero_common_real_zero(M1, M2):
    """Exact: the real common zero set of the two quadratic forms is {0} (cases met here)."""
    k = len(M1)
    if k == 1:
        return M1[0][0] != 0 or M2[0][0] != 0
    for S, T in ((M1, M2), (M2, M1)):
        if all(x == 0 for r in S for x in r):
            continue
        if not rank1_semidefinite(S):
            continue
        K = nullspace(S, k)
        R_ = [[sum(K[p][i] * T[i][j] * K[q][j] for i in range(k) for j in range(k)) for q in range(len(K))]
              for p in range(len(K))]
        if len(K) == 1:
            return R_[0][0] != 0
        if len(K) == 2:
            return R_[0][0] * R_[1][1] - R_[0][1] * R_[1][0] > 0
    return False


obstr = {}
for name, A in (("6", orbit((0, 0, 1))), ("8", orbit((1, 1, 1))), ("12", orbit((1, 1, 0)))):
    n = len(A)
    dims, ok = [], True
    for eps in (1, -1):
        B, Mo, Mp = pair_forms(A, eps)
        dims.append(len(B))
        ok = ok and only_zero_common_real_zero(Mo, Mp)
    obstr[name] = ((n - 1) // 6, dims, ok)
check("6-, 8-, 12-point orbits: six orthogonal bond spaces in n-1 = 5, 7, 11 dims have dim <= 0, 1, 1",
      [v[0] for v in obstr.values()] == [0, 1, 1],
      "a nonzero bond space is a real eigenline of the quarter-turn about its own axis")
check("on those three orbits no real eigenline meets the two pair conditions: the rule is constant",
      all(v[2] for v in obstr.values())
      and [v[1] for v in obstr.values()] == [[2, 1], [1, 2], [2, 3]],
      "eigenline dims (+1, -1): " + "; ".join(f"{k}-point {v[1]}" for k, v in obstr.items()))
A24 = orbit((1, 2, 3))
check("controls: the decision procedure rejects forms (c0+c1)^2, c0^2-c1^2, which share the real zero c0 = -c1",
      only_zero_common_real_zero([[Fr(1), Fr(1)], [Fr(1), Fr(1)]], [[Fr(1), Fr(0)], [Fr(0), Fr(-1)]]) is False)


def transverse_sign(d, a):
    """sign of the product of the two coordinates of a transverse to d, on the cap a.d = 3."""
    if dot(a, d) != 3:
        return 0
    i, j = [k for k in range(3) if d[k] == 0]
    return 1 if a[i] * a[j] > 0 else -1


XS = {(d, a): transverse_sign(d, a) for d in DIRS for a in A24}
R0_24 = Fr(1, 24)


def phi24(d, a, b):
    return 1 + KAPPA * XS[(d, a)] * XS[(neg(d), b)]


def rule24(a, N):
    p = R0_24
    for d, b in N.items():
        p *= phi24(d, a, b)
    return p


check("single 24-point orbit: transverse-sign functions have disjoint supports and mean 0 per direction",
      all(sum(1 for d in DIRS if XS[(d, a)] != 0) == 1 for a in A24)
      and all(sum(XS[(d, a)] for a in A24) == 0 for d in DIRS)
      and all(XS[(EZ, mv(RZ, a))] == -XS[(EZ, a)] for a in A24),
      "each is a quarter-turn eigenfunction of eigenvalue -1 on its cap")
W24 = [XS[(EZ, a)] for a in A24]
P_OPP, P_PERP = pull(G_TO[neg(EZ)], A24), pull(G_TO[EX], A24)
check("controls: the 24-point transverse sign meets both pair conditions in the same machinery (0 and 0)",
      sum(W24[i] * W24[P_OPP[i]] for i in range(24)) == 0 and sum(W24[i] * W24[P_PERP[i]] for i in range(24)) == 0
      and any(W24))
check("its bond factors are soldered-covariant and bond-symmetric (all 24 x 6 x 24 x 24 cases)",
      all(phi24(mv(g, d), mv(g, a), mv(g, b)) == phi24(d, a, b) for g in O for d in DIRS for a in A24 for b in A24)
      and all(phi24(d, a, b) == phi24(neg(d), b, a) for d in DIRS for a in A24 for b in A24))
norm24 = all(sum(R0_24 * __import__("functools").reduce(lambda u, v: u * v,
                                                            [1 + KAPPA * XS[(d, a)] * x for d, x in zip(dset, xs)],
                                                            Fr(1)) for a in A24) == 1
             for k in range(7) for dset in combinations(DIRS, k) for xs in product(CLASS_VALS, repeat=k))
check("24-point rule: normalised for all 4096 value classes of neighbour conditions, and it varies",
      norm24 and any(rule24(a, {EZ: b}) != R0_24 for a in A24 for b in A24))
LAWS24 = {o: finished_law(PATH, A24, rule24, o) for o in permutations(PATH)}
L24 = LAWS24[PATH]
M24 = {}
for (ax, ay, az), m in L24.items():
    M24[(ax, az)] = M24.get((ax, az), Fr(0)) + m
check("24-point rule on the path: 6 orders, one law; ends independent; adjacent correlation kappa/36",
      all(L == L24 for L in LAWS24.values()) and sum(L24.values()) == 1
      and set(M24.values()) == {R0_24 * R0_24} and len(M24) == 576
      and sum(m * XS[(EZ, ax)] * XS[(neg(EZ), ay)] for (ax, ay, az), m in L24.items()) == KAPPA / 36)

print()
print("per_element: checked the finite configurations and arithmetic controls explicitly enumerated above")
print("per_site: checked the declared finite-window local rules under their supplied sampling conventions")
print("per_mode: checked and not executed — no infinite-volume Fourier or spectral mode computation is performed")
print("per_block: checked only the listed finite windows and orders; proofs beyond those runs are source arguments")
print("lattice_wide: checked and not executed — no infinite-lattice formation process or physical completion is simulated")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
