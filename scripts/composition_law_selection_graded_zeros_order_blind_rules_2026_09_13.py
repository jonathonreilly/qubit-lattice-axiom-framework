#!/usr/bin/env python3
"""Composition and law selection: graded zeros against order-blind covariant rules.

Exact finite check (rationals in Q(sqrt 2) and integer characters only) on the
grid2x3, 2x2x2 cube and grid3x3 windows of whether a translation- and
rotation-covariant order-blind record rule reproduces the zero set of the graded
(Jordan-Wigner) composition's ground occupation law at zero interaction, sector by
sector and across sectors.  Families: signed-automorphism characters, static
recorded-neighbour classes, bond-type rules, star-local rules, the positive
bond-product comparator, and sequential recorded-neighbour support rules under two
exterior conventions of the open window (exterior never records; exterior is a
wall of permanent empty records) plus the boundary-state cluster-graph family.

Prints TOTAL: PASS=N FAIL=0 on success.  Runtime about 80 s.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from typing import Dict, FrozenSet, List, Sequence, Tuple

Pattern = FrozenSet[int]
PASS = 0
FAIL = 0
LINES: List[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        LINES.append(f"PASS {name} {detail}".rstrip())
    else:
        FAIL += 1
        LINES.append(f"FAIL {name} {detail}".rstrip())


# ---------------------------------------------------------------- clusters
def grid_cluster(rows: int, cols: int):
    """Sites r*cols+c, bonds = horizontal and vertical nearest neighbours."""
    sites = list(range(rows * cols))
    bonds = []
    for r in range(rows):
        for c in range(cols):
            i = r * cols + c
            if c + 1 < cols:
                bonds.append((i, i + 1))
            if r + 1 < rows:
                bonds.append((i, i + cols))
    coords = {r * cols + c: (r, c) for r in range(rows) for c in range(cols)}
    return sites, sorted(bonds), coords


def cube_cluster():
    """Sites 4x+2y+z on {0,1}^3, 12 edges of the cube."""
    sites = list(range(8))
    coords = {4 * x + 2 * y + z: (x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)}
    bonds = []
    for i in sites:
        for j in sites:
            if i < j:
                d = sum(abs(a - b) for a, b in zip(coords[i], coords[j]))
                if d == 1:
                    bonds.append((i, j))
    return sites, sorted(bonds), coords


def automorphisms(sites: Sequence[int], bonds: Sequence[Tuple[int, int]]):
    """Bond-preserving site permutations (as tuples perm[i] = image of i)."""
    bondset = {frozenset(b) for b in bonds}
    out = []
    for perm in itertools.permutations(sites):
        if all(frozenset((perm[i], perm[j])) in bondset for i, j in bonds):
            out.append(perm)
    return out


def sector(sites: Sequence[int], n: int) -> List[Pattern]:
    return [frozenset(c) for c in itertools.combinations(sites, n)]


# ---------------------------------------------------------- graded hopping
def jw_sign(pattern: Pattern, i: int, j: int) -> int:
    """(-1)^(occupied sites strictly between i and j in site order)."""
    lo, hi = min(i, j), max(i, j)
    return -1 if sum(1 for s in pattern if lo < s < hi) % 2 else 1


def hopping_matrix(patterns: List[Pattern], bonds, graded: bool) -> List[List[int]]:
    """Matrix of -sum_bonds (x_i^dag x_j + h.c.) in the occupation basis (t = 1)."""
    index = {p: k for k, p in enumerate(patterns)}
    dim = len(patterns)
    H = [[0] * dim for _ in range(dim)]
    for p in patterns:
        for i, j in bonds:
            for a, b in ((i, j), (j, i)):
                if a in p and b not in p:
                    q = (p - {a}) | {b}
                    # x_b^dag x_a |p>: graded sign from the ladder strings.
                    # Removing a then adding b: sign (-1)^{#occ < a} * (-1)^{#occ' < b}
                    # which equals (-1)^{#occ strictly between a and b} for a NN pair.
                    s = jw_sign(p, a, b) if graded else 1
                    H[index[q]][index[p]] += -s
    return H


def perm_sign(pattern: Pattern, perm) -> int:
    """sgn_S(sigma): sign of the permutation the automorphism induces on the
    ordered occupied sites (sorted S -> sorted sigma(S))."""
    src = sorted(pattern)
    img = [perm[s] for s in src]
    # sign of the permutation sorting img
    order = sorted(range(len(img)), key=lambda k: img[k])
    visited = [False] * len(order)
    sign = 1
    for k in range(len(order)):
        if not visited[k]:
            length = 0
            m = k
            while not visited[m]:
                visited[m] = True
                m = order[m]
                length += 1
            if length % 2 == 0:
                sign = -sign
    return sign


# ------------------------------------------------ exact number field Q(sqrt2)
class QS2:
    """a + b*sqrt(2) with rational a, b (exact)."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, o):
        o = o if isinstance(o, QS2) else QS2(o)
        return QS2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, QS2) else QS2(o)
        return QS2(self.a - o.a, self.b - o.b)

    def __neg__(self):
        return QS2(-self.a, -self.b)

    def __mul__(self, o):
        o = o if isinstance(o, QS2) else QS2(o)
        return QS2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 2 * self.b * self.b
        return QS2(self.a / n, -self.b / n)

    def __truediv__(self, o):
        o = o if isinstance(o, QS2) else QS2(o)
        return self * o.inv()

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def __eq__(self, o):
        o = o if isinstance(o, QS2) else QS2(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def sign(self) -> int:
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if (a > 0) == (b > 0):
            return 1 if a > 0 else -1
        big = a * a > 2 * b * b
        return (1 if a > 0 else -1) if big else (1 if b > 0 else -1)

    def __repr__(self):
        return f"{self.a}+{self.b}r2" if self.b else f"{self.a}"


def nullspace(M: List[List[QS2]]) -> List[List[QS2]]:
    """Exact nullspace basis of a square matrix over Q(sqrt2)."""
    n = len(M)
    A = [row[:] for row in M]
    pivots = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, n) if not A[i][c].is_zero()), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = A[r][c].inv()
        A[r] = [x * inv for x in A[r]]
        for i in range(n):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for fc in free:
        v = [QS2() for _ in range(n)]
        v[fc] = QS2(1)
        for k, pc in enumerate(pivots):
            v[pc] = -A[k][fc]
        basis.append(v)
    return basis


def negative_inertia(M: List[List[QS2]]) -> int:
    """Number of negative eigenvalues of a nonsingular symmetric matrix over
    Q(sqrt2), by exact symmetric elimination (Sylvester's law of inertia)."""
    n = len(M)
    A = {i: {j: M[i][j] for j in range(n) if not M[i][j].is_zero()} for i in range(n)}
    alive = set(range(n))
    neg = 0
    while alive:
        p = next((i for i in alive if i in A[i]), None)
        if p is not None:
            d = A[p][p]
            neg += d.sign() < 0
            col = {i: A[i][p] for i in alive if i != p and p in A[i]}
            for i, ai in col.items():
                fi = ai / d
                for j, pj in A[p].items():
                    if j in alive and j != p:
                        val = A[i].get(j, QS2()) - fi * pj
                        if val.is_zero():
                            A[i].pop(j, None)
                        else:
                            A[i][j] = val
            alive.discard(p)
            continue
        # all remaining diagonals vanish: take a 2x2 off-diagonal pivot
        p = next((i for i in alive if any(j in alive for j in A[i])), None)
        if p is None:
            raise ValueError("singular matrix in inertia count")
        q = next(j for j in A[p] if j in alive)
        b = A[p][q]
        neg += 1  # block [[0,b],[b,0]] has inertia (1 positive, 1 negative)
        rest = [i for i in alive if i not in (p, q)]
        for i in rest:
            aip = A[i].get(p, QS2())
            aiq = A[i].get(q, QS2())
            if aip.is_zero() and aiq.is_zero():
                continue
            for j in rest:
                apj = A[p].get(j, QS2())
                aqj = A[q].get(j, QS2())
                val = A[i].get(j, QS2()) - (aip * aqj + aiq * apj) / b
                if val.is_zero():
                    A[i].pop(j, None)
                else:
                    A[i][j] = val
        alive.discard(p)
        alive.discard(q)
    return neg


# ------------------------------------------------------- ground-state analysis
def graded_ground(patterns, bonds, energy: QS2):
    """Exact ground vector of the graded hopping term at the given energy.
    Returns (vector, zero patterns, kernel dimension, count of eigenvalues
    below energy + 1/4)."""
    H = hopping_matrix(patterns, bonds, graded=True)
    n = len(patterns)
    M = [[QS2(H[i][j]) - (energy if i == j else QS2()) for j in range(n)] for i in range(n)]
    basis = nullspace(M)
    shift = energy + QS2(Fraction(1, 4))
    M2 = [[QS2(H[i][j]) - (shift if i == j else QS2()) for j in range(n)] for i in range(n)]
    below = negative_inertia(M2)
    v = basis[0] if basis else None
    zeros = [] if v is None else [p for p, x in zip(patterns, v) if x.is_zero()]
    return v, zeros, len(basis), below


def ungraded_connected(patterns, bonds) -> bool:
    """Configuration graph of the ungraded hopping term is connected (so its
    ground vector is simple and strictly positive by Perron-Frobenius)."""
    H = hopping_matrix(patterns, bonds, graded=False)
    n = len(patterns)
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in range(n):
            if H[i][j] != 0 and j not in seen:
                seen.add(j)
                stack.append(j)
    return len(seen) == n and all(H[i][j] <= 0 for i in range(n) for j in range(n))


def characters(patterns, v, auts, graded: bool):
    """chi(sigma) with U_sigma v = chi(sigma) v, or None if v is not an
    eigenvector of the (signed) automorphism action."""
    index = {p: k for k, p in enumerate(patterns)}
    chis = {}
    for perm in auts:
        chi = None
        for p, x in zip(patterns, v):
            img = frozenset(perm[s] for s in p)
            s = perm_sign(p, perm) if graded else 1
            y = v[index[img]]
            # (U v)[img] = s * x  must equal chi * y
            if x.is_zero() and y.is_zero():
                continue
            if x.is_zero() != y.is_zero():
                return None
            ratio = (x * QS2(s)) / y
            if chi is None:
                chi = ratio
            elif not (chi == ratio):
                return None
        chis[perm] = chi
    return chis


def character_zero_prediction(patterns, auts, chis) -> List[Pattern]:
    """Patterns fixed by some automorphism with chi(sigma) sgn_S(sigma) = -1."""
    out = []
    for p in patterns:
        for perm in auts:
            if frozenset(perm[s] for s in p) == p:
                if (chis[perm] * QS2(perm_sign(p, perm))) == QS2(-1):
                    out.append(p)
                    break
    return out


# --------------------------------------------- classical covariant support rules
def bond_type(p: Pattern, i: int, j: int) -> str:
    return "".join(sorted(str(int(i in p)) + str(int(j in p))))


def bond_rule_zero_set(patterns, bonds, forbidden: FrozenSet[str]) -> FrozenSet[Pattern]:
    return frozenset(p for p in patterns if any(bond_type(p, i, j) in forbidden for i, j in bonds))


def neighbours(sites, bonds) -> Dict[int, List[int]]:
    nb = {s: [] for s in sites}
    for i, j in bonds:
        nb[i].append(j)
        nb[j].append(i)
    return nb


def star_class(p: Pattern, i: int, nb) -> Tuple[int, int, int]:
    """(value, degree, occupied neighbours): the covariant local class of site i."""
    return (int(i in p), len(nb[i]), sum(1 for j in nb[i] if j in p))


def maximal_star_rule(patterns, zeros, sites, nb):
    """Largest forbidden class set compatible with every nonzero pattern, and
    the zero patterns it kills.  A star-local support rule reproduces the zero
    set iff this maximal set kills every zero pattern."""
    zeroset = set(zeros)
    used_by_nonzero = set()
    for p in patterns:
        if p not in zeroset:
            used_by_nonzero.update(star_class(p, i, nb) for i in sites)
    all_classes = {star_class(p, i, nb) for p in patterns for i in sites}
    fmax = all_classes - used_by_nonzero
    killed = [p for p in zeros if any(star_class(p, i, nb) in fmax for i in sites)]
    return fmax, killed


def step_class(p: Pattern, i: int, formed: FrozenSet[int], nb, conv: str = "unrec") -> tuple:
    """Covariant order-blind class of site i at its formation step.
    conv="unrec": the open cluster's exterior never records, so the Z^3 rule sees
    (value, recorded neighbours, occupied recorded neighbours).
    conv="empty": the exterior is a wall of permanent empty records, so it sees
    (value, unrecorded neighbours, occupied recorded neighbours).
    conv="wall": the exterior is a distinguishable third neighbour state (a rule on
    the cluster graph, not a Z^3 rule): (value, unrecorded, recorded empty, occupied)."""
    rec = [j for j in nb[i] if j in formed]
    n1 = sum(1 for j in rec if j in p)
    n0 = len(rec) - n1
    nu = len(nb[i]) - len(rec)
    v = int(i in p)
    if conv == "unrec":
        return (v, n0 + n1, n1)
    if conv == "empty":
        return (v, nu, n1)
    return (v, nu, n0, n1)


CLASS_INDEX: dict = {}
CLASSES: list = []


def class_bit(c) -> int:
    """Bit index of a class tuple, registered on first use (never reassigned)."""
    if c not in CLASS_INDEX:
        CLASS_INDEX[c] = len(CLASSES)
        CLASSES.append(c)
    return CLASS_INDEX[c]


def order_class_sets(p: Pattern, sites, nb, conv: str = "unrec") -> List[int]:
    """Minimal class-set bitmasks over all formation orders (subset DP)."""
    n = len(sites)
    full = (1 << n) - 1
    reach = {0: {0}}
    for size in range(n):
        for T in [t for t in reach if bin(t).count("1") == size]:
            formed = frozenset(s for s in sites if T >> s & 1)
            for i in sites:
                if not (T >> i & 1):
                    bit = 1 << class_bit(step_class(p, i, formed, nb, conv))
                    reach.setdefault(T | 1 << i, set()).update(m | bit for m in reach[T])
    masks = reach[full]
    return [m for m in masks if not any(o != m and (o & m) == o for o in masks)]


# ---------------------------------------------------------------------------
# Chunk 4a: exact sector census (four occupation sectors on three clusters).
# ---------------------------------------------------------------------------

# (label, cluster, occupation number N, exact lowest graded energy in Q(sqrt2))
SECTORS = [
    ("grid2x3", (2, 3), 2, QS2(Fraction(-2), Fraction(-1))),   # -(2+sqrt2)
    ("grid2x3", (2, 3), 3, QS2(Fraction(-1), Fraction(-2))),   # -(1+2sqrt2)
    ("cube", None, 4, QS2(Fraction(-6), Fraction(0))),         # -6
    ("grid3x3", (3, 3), 3, QS2(Fraction(0), Fraction(-4))),    # -4sqrt2
]
EXPECT_ZEROS = {("grid2x3", 2): 3, ("grid2x3", 3): 2, ("cube", 4): 12, ("grid3x3", 3): 8}
EXPECT_CHAR = {("grid2x3", 2): 3, ("grid2x3", 3): 0, ("cube", 4): 12, ("grid3x3", 3): 4}
EXPECT_SIGNS = {("grid2x3", 2): (9, 3, 3), ("cube", 4): (29, 29, 12)}


def build_cluster(spec):
    return grid_cluster(*spec) if spec is not None else cube_cluster()


def exact_sector_census():
    """Exact ground vectors, zero sets, gap certificates and sign characters."""
    results = {}
    for label, spec, n_occ, energy in SECTORS:
        sites, bonds, _coords = build_cluster(spec)
        nb = neighbours(sites, bonds)
        pats = sector(sites, n_occ)
        auts = automorphisms(sites, bonds)
        vec, zeros, kdim, below = graded_ground(pats, bonds, energy)
        key = (label, n_occ)
        check(f"{label} N={n_occ}: exact graded kernel of H-E is one-dimensional",
              kdim == 1, f"kernel dim {kdim}")
        check(f"{label} N={n_occ}: E is the simple lowest eigenvalue, gap >= 1/4",
              below == 1, f"negative inertia of H-(E+1/4) = {below}")
        check(f"{label} N={n_occ}: zero set of the graded ground vector has "
              f"{EXPECT_ZEROS[key]} patterns", len(zeros) == EXPECT_ZEROS[key],
              f"|Z| = {len(zeros)} of {len(pats)}")
        chis = characters(pats, vec, auts, True)
        chi_ok = all(c is not None and c in (QS2(Fraction(1)), QS2(Fraction(-1)))
                     for c in chis.values())
        check(f"{label} N={n_occ}: ground vector is a signed-automorphism eigenvector, "
              f"character +-1 (|Aut| = {len(auts)})", chi_ok,
              f"characters {sorted(str(c) for c in set(chis.values()))}")
        pred = character_zero_prediction(pats, auts, chis)
        check(f"{label} N={n_occ}: chi(sigma) sgn_S(sigma) = -1 predicts {EXPECT_CHAR[key]} of "
              f"{EXPECT_ZEROS[key]} zeros, all genuine",
              set(pred) <= set(zeros) and len(pred) == EXPECT_CHAR[key],
              f"predicted {len(pred)}, actual {len(zeros)}")
        pos = sum(1 for x in vec if x.sign() > 0)
        neg = sum(1 for x in vec if x.sign() < 0)
        if key in EXPECT_SIGNS:
            check(f"{label} N={n_occ}: signed components (+,-,0) = {EXPECT_SIGNS[key]}",
                  (pos, neg, len(zeros)) == EXPECT_SIGNS[key], f"got {(pos, neg, len(zeros))}")
        conn = ungraded_connected(pats, bonds)
        check(f"{label} N={n_occ}: ungraded graph connected, off-diagonal <= 0 "
              f"(Perron: positive ground vector, no zeros)", conn, str(conn))
        results[key] = (sites, bonds, nb, pats, list(zeros), vec, auts)
    return results


# ---------------------------------------------------------------------------
# Chunk 4b: sequential recorded-neighbour support rules.
# A rule is a forbidden set F of step classes (value, recorded neighbours,
# occupied recorded neighbours); a pattern is supported when some formation
# order has every step outside F ("exists-order" semantics).  The rule is
# order blind: it names no order, and covariant: classes are Aut-invariant.
# ---------------------------------------------------------------------------

def support_constraints(sites, nb, pats, zeros, conv: str = "unrec"):
    """(zero class-sets, nonzero class-set lists, used-class mask, U)."""
    zset = set(zeros)
    U = {p: order_class_sets(p, sites, nb, conv) for p in pats}
    zm = [c for S in zeros for c in U[S]]
    nz = [U[S] for S in pats if S not in zset]
    used = 0
    for p in pats:
        for c in U[p]:
            used |= c
    return zm, nz, used, U


def count_support_rules(zm, nz, used, cap=200000):
    """All forbidden sets F over the used classes that kill every zero pattern
    (every class-set of every zero pattern meets F) and keep every nonzero
    pattern (some class-set avoids F).  Exact enumeration with suffix pruning."""
    bits = [i for i in range(len(CLASSES)) if used >> i & 1]
    suffix = [0] * (len(bits) + 1)
    for i in range(len(bits) - 1, -1, -1):
        suffix[i] = suffix[i + 1] | (1 << bits[i])
    sols: List[int] = []

    def rec(idx, F):
        if any((c & (F | suffix[idx])) == 0 for c in zm):
            return
        if any(all(c & F for c in lst) for lst in nz):
            return
        if idx == len(bits):
            sols.append(F)
            return
        if len(sols) >= cap:
            return
        rec(idx + 1, F | (1 << bits[idx]))
        rec(idx + 1, F)

    rec(0, 0)
    return sols


def forced_and_never(sols, used):
    inter = (1 << len(CLASSES)) - 1
    uni = 0
    for F in sols:
        inter &= F
        uni |= F
    forced = sorted(CLASSES[i] for i in range(len(CLASSES)) if inter >> i & 1 and used >> i & 1)
    never = sorted(CLASSES[i] for i in range(len(CLASSES)) if not (uni >> i & 1) and used >> i & 1)
    return forced, never


def fmt_classes(cs) -> str:
    return " ".join("".join(map(str, c)) for c in cs) or "-"


def static_order_census(sites, nb, pats, zeros, auts):
    """Number of formation orders (one representative per Aut orbit) for which
    some forbidden class set F, applied along that single fixed order,
    reproduces the zero set exactly."""
    zset = set(zeros)
    reps = set()
    for order in itertools.permutations(sites):
        reps.add(min(tuple(a[s] for s in order) for a in auts))
    valid = 0
    for order in reps:
        masks = {}
        for p in pats:
            formed: FrozenSet[int] = frozenset()
            mk = 0
            for i in order:
                mk |= 1 << class_bit(step_class(p, i, formed, nb))
                formed = formed | {i}
            masks[p] = mk
        allowed = (1 << len(CLASSES)) - 1
        for p in pats:
            if p not in zset:
                allowed &= ~masks[p]
        if all(masks[p] & allowed for p in zeros):
            valid += 1
    return len(reps), valid


EXPECT_RULES = {("grid2x3", 2): 476, ("grid2x3", 3): 201, ("cube", 4): 8750, ("grid3x3", 3): 421}
JOINT_TRIPLE = (("grid2x3", 2), ("cube", 4), ("grid3x3", 3))
EXPECT_TRIPLE = 160
EXPECT_TRIPLE_FORCED = [(0, 2, 0), (0, 2, 1), (0, 3, 1), (0, 3, 2), (1, 0, 0), (1, 1, 0),
                        (1, 3, 1), (1, 4, 0), (1, 4, 2)]
EXPECT_TRIPLE_NEVER = [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 2, 2), (0, 3, 0), (1, 2, 0),
                       (1, 2, 1), (1, 3, 0), (1, 3, 2), (1, 4, 1)]


# Exterior convention "empty": the open cluster's boundary is a wall of permanent
# empty records, so the Z^3 rule sees (value, unrecorded neighbours, occupied).
EXPECT_RULES_EMPTY = {("grid2x3", 2): 782, ("grid2x3", 3): 2607, ("cube", 4): 8750,
                      ("grid3x3", 3): 1116}
EXPECT_EMPTY_PAIR = 39
EXPECT_EMPTY_PAIR_FORCED = [(0, 1, 0), (0, 2, 0), (1, 1, 1), (1, 1, 2), (1, 3, 0)]
EXPECT_EMPTY_PAIR_NEVER = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (0, 2, 1),
                           (1, 0, 1), (1, 2, 0), (1, 2, 1)]


def support_rule_families(results):
    """Per-sector, pairwise, and joint counts of sequential support rules;
    static-order census; bond-type, star-local and positive-comparator checks."""
    cons = {}
    for key, (sites, bonds, nb, pats, zeros, vec, auts) in results.items():
        zm, nz, used, _U = support_constraints(sites, nb, pats, zeros)
        cons[key] = (zm, nz, used)
        sols = count_support_rules(zm, nz, used)
        forced, never = forced_and_never(sols, used)
        exp = EXPECT_RULES[key]
        ok = len(sols) == exp if exp is not None else len(sols) > 0
        check(f"{key[0]} N={key[1]} exterior-unrecorded: {len(sols)} rules "
              f"({bin(used).count('1')} classes)", ok,
              f"forced {fmt_classes(forced)}; never {fmt_classes(never)}")
        if key[0] == "grid2x3" and key[1] == 3:
            LINES.append(f"  grid2x3 N=3 forced forbidden: {fmt_classes(forced)}")
            LINES.append(f"  grid2x3 N=3 never forbidden: {fmt_classes(never)}")

    def joint(keys, table=None, cap=200000):
        table = cons if table is None else table
        zm = sum((table[k][0] for k in keys), [])
        nz = sum((table[k][1] for k in keys), [])
        used = 0
        for k in keys:
            used |= table[k][2]
        sols = count_support_rules(zm, nz, used, cap)
        return sols, used

    sols, used = joint(JOINT_TRIPLE)
    forced, never = forced_and_never(sols, used)
    check(f"joint over the three discriminator sectors (2x3 N=2, cube N=4, 3x3 N=3): "
          f"{len(sols)} rules", len(sols) == EXPECT_TRIPLE)
    check("joint triple: forced forbidden classes " + fmt_classes(forced),
          forced == EXPECT_TRIPLE_FORCED)
    check("joint triple: never forbidden classes " + fmt_classes(never),
          never == EXPECT_TRIPLE_NEVER)
    example = sorted(CLASSES[i] for i in range(len(CLASSES)) if sols[0] >> i & 1) if sols else []
    LINES.append("  joint triple example rule F = " + fmt_classes(example))
    for pair, exp in [((("grid2x3", 2), ("cube", 4)), 1021),
                      ((("grid2x3", 2), ("grid3x3", 3)), 384),
                      ((("cube", 4), ("grid3x3", 3)), 189)]:
        sols, used = joint(pair)
        check(f"pair {pair[0][0]} N={pair[0][1]} + {pair[1][0]} N={pair[1][1]}: {len(sols)} rules",
              len(sols) == exp)
    sols, used = joint((("grid2x3", 2), ("grid2x3", 3)))
    check("grid2x3 N=2 and N=3 jointly: no N-blind sequential support rule "
          f"({len(sols)} rules)", len(sols) == 0)
    sols, used = joint(tuple(results.keys()))
    check(f"all four sectors jointly: {len(sols)} rules", len(sols) == 0)

    cons_e = {}
    for key, (sites, bonds, nb, pats, zeros, vec, auts) in results.items():
        zm, nz, used, _U = support_constraints(sites, nb, pats, zeros, "empty")
        cons_e[key] = (zm, nz, used)
        sols = count_support_rules(zm, nz, used)
        forced, never = forced_and_never(sols, used)
        tag = " (= exterior-unrecorded count; degree-regular)" if key[0] == "cube" else ""
        check(f"{key[0]} N={key[1]} exterior-empty: {len(sols)} rules "
              f"({bin(used).count('1')} classes){tag}", len(sols) == EXPECT_RULES_EMPTY[key],
              f"forced {fmt_classes(forced)}; never {fmt_classes(never)}")
    sols, used = joint((("grid2x3", 2), ("grid2x3", 3)), cons_e)
    forced, never = forced_and_never(sols, used)
    check(f"exterior-empty: grid2x3 N=2 and N=3 jointly: {len(sols)} N-blind rules",
          len(sols) == EXPECT_EMPTY_PAIR)
    check("exterior-empty pair: forced " + fmt_classes(forced), forced == EXPECT_EMPTY_PAIR_FORCED)
    check("exterior-empty pair: never " + fmt_classes(never), never == EXPECT_EMPTY_PAIR_NEVER)
    example = sorted(CLASSES[i] for i in range(len(CLASSES)) if sols[0] >> i & 1) if sols else []
    LINES.append("  exterior-empty pair example rule F = " + fmt_classes(example))
    sols, used = joint(JOINT_TRIPLE, cons_e)
    check(f"exterior-empty: joint discriminator triple: {len(sols)} rules", len(sols) == 0)
    sols, used = joint(tuple(results.keys()), cons_e)
    check(f"exterior-empty: all four sectors jointly: {len(sols)} rules", len(sols) == 0)
    cons_w = {}
    for key, (sites, bonds, nb, pats, zeros, vec, auts) in results.items():
        if key[0] == "grid2x3":
            zm, nz, used, _U = support_constraints(sites, nb, pats, zeros, "wall")
            cons_w[key] = (zm, nz, used)
    sols, used = joint((("grid2x3", 2), ("grid2x3", 3)), cons_w, cap=1)
    check("boundary-state cluster-graph rules: grid2x3 N=2 and N=3 jointly admit a rule "
          f"(existence, {len(sols)} found at cap 1)", len(sols) == 1)

    for key, exp_reps, exp_valid in [(("grid2x3", 2), 180, 0), (("grid2x3", 3), 180, 20),
                                     (("cube", 4), 840, 0)]:
        sites, bonds, nb, pats, zeros, vec, auts = results[key]
        reps, valid = static_order_census(sites, nb, pats, zeros, auts)
        check(f"{key[0]} N={key[1]}: one fixed order + forbidden classes: "
              f"{valid} of {reps} order classes reproduce the zeros",
              reps == exp_reps and valid == exp_valid)

    # Static order-blind families.
    types = ["00", "01", "11"]
    for key in results:
        sites, bonds, nb, pats, zeros, vec, auts = results[key]
        zset = frozenset(zeros)
        sizes = []
        hit = False
        for r in range(1, 4):
            for forb in itertools.combinations(types, r):
                zs = bond_rule_zero_set(pats, bonds, frozenset(forb))
                sizes.append(len(zs))
                hit = hit or zs == zset
        check(f"{key[0]} N={key[1]}: bond-type forbidding rules give zero-set sizes "
              f"{','.join(map(str, sizes))}, never the graded set", not hit)
        fmax, killed = maximal_star_rule(pats, zeros, sites, nb)
        check(f"{key[0]} N={key[1]}: star-local rule: maximal forbidden class set has "
              f"{len(fmax)} classes and kills {len(killed)} of {len(zeros)} zeros",
              len(fmax) == 0 and len(killed) == 0)
        w = {"00": Fraction(1), "01": Fraction(1, 2), "11": Fraction(1, 3)}
        weights = []
        for p in zeros:
            prod = Fraction(1)
            for i, j in bonds:
                prod *= w[bond_type(p, i, j)]
            weights.append(prod)
        check(f"{key[0]} N={key[1]}: positive bond-product comparator weight on every "
              f"graded zero (min {min(weights)})", min(weights) > 0)


# ---------------------------------------------------------------------------
# Chunk 4c: driver.
# ---------------------------------------------------------------------------

def main() -> int:
    results = exact_sector_census()
    support_rule_families(results)
    print("\n".join(LINES))
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
