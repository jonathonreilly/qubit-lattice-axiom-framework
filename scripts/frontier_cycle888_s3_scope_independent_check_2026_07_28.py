#!/usr/bin/env python3
"""Cycle 888 INDEPENDENT CHECK -- specified to REFUTE the S3 scope pricing.

Nothing here is inherited from the primary.  The rotation group is rebuilt from
the orthogonality condition M M^T = I over integer matrices; the subgroup
lattice is rebuilt by ITERATED EXTENSION (close <H, g> for every found H and
every group element until the family is stable) and cross-checked against the
Sylow congruences and the class equation; the isotype decompositions are
rebuilt by MINIMAL CYCLIC SUBMODULES and orthogonal complements, with block
characters used to group them -- no enveloping algebra, no centre, no minimal
polynomial, no cyclotomics; reachability is re-decided by Smith-style
diagonalization; every one of the sixteen selector survivor sets is recomputed
over all thirty subgroups; and the scope-insensitivity verdicts are recomputed
from scratch.

The hardest attack is on the SL1-TRANSFER claim.  The primary says the S3
readout's (1, 2) fine-top pair is NOT forced, because the 2-dimensional
irreducible occurs twice.  This checker tries to break that both ways: it hunts
for a second inequivalent readout construction at S3 scope carrying a DIFFERENT
pair (which would refute the transfer claim outright), and it independently
recomputes the multiplicity ledgers at C3 and C4 that the primary's peer
comparison rests on.

Exit status is 0 whether or not the claims survive.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 400_000

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle888_s3_scope_pricing_2026_07_28.py",
    "outputs/s3_scope_pricing_cycle888_receipt_2026_07_28.json",
    "logs/runner-cache/frontier_cycle888_s3_scope_pricing_2026_07_28.txt",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle886_sl0_orbit_scope_2026_07_28.py",
    "outputs/sl0_orbit_scope_cycle886_receipt_2026_07_28.json",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs" / \
    "s3_scope_independent_check_cycle888_receipt_2026_07_28.json"

BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AUDIT_INPUT_PATHS)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "f57fda877d35d49953c3b6a34293ab0cc6a87781ceb9d158b9c9abb5abd4bb3f",
    AUDIT_INPUT_PATHS[1]:
        "8a540201a84a6b8cb6868d431216718a27f200e45d6ceeb771d858e9a54280cd",
    AUDIT_INPUT_PATHS[2]:
        "5e4fc183efda55d1f3fbd5413bd2fe985ed5732b7ffbc8bd489296e7b22c2c84",
    AUDIT_INPUT_PATHS[3]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[4]:
        "1dfa47a86de8cab5a91cd33a022beb845d918e2f93ceb58f360b2708a44d02a2",
    AUDIT_INPUT_PATHS[5]:
        "74d64090515cf7f7c5ad5f8e6347f7d2f81a9c1cf0b41e9ec7726ad30a62d69d",
    AUDIT_INPUT_PATHS[6]:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c3de02c94b8a11a930ad6ff8817975b118bc776d",
    AUDIT_INPUT_PATHS[1]: "3e18ad52f50e72b83c56da72c31f25d104b5c830",
    AUDIT_INPUT_PATHS[2]: "6cd3fbdbe74e1231cd61222a798a7979bee922da",
    AUDIT_INPUT_PATHS[3]: "4a863da1f3f255354839277271a3a69a5c205133",
    AUDIT_INPUT_PATHS[4]: "f4493d787ffb6edc50e9dd13d37ba1cd1dd4d24a",
    AUDIT_INPUT_PATHS[5]: "4d9999c241b19b2670a51c809e3e39fb0d339f10",
    AUDIT_INPUT_PATHS[6]: "d563c2b9c2a261f44d7304baa51fdd3596188930",
}

SHELL = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
TARGET = Fraction(2, 9)
TARGET_PAIR = (1, 2)

LABELS = (
    "A_PINS",
    "B_INDEPENDENT_GROUP",
    "C_INDEPENDENT_LATTICE",
    "D_INDEPENDENT_ISOTYPE",
    "E_INDEPENDENT_SELECTORS",
    "F_INDEPENDENT_REACHABILITY",
    "G_SL1_TRANSFER_ATTACK",
    "H_INDEPENDENT_SCOPE_INSENSITIVITY",
    "I_UPSTREAM_PIN_FIDELITY",
    "J_REFUTATION_ATTEMPTS",
    "K_TEETH",
    "L_FINDINGS",
    "M_VERDICT",
)


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):       # pragma: no cover legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


def _bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _text(path: str) -> str:
    return _bytes(path).decode("utf-8")


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def digest(payload: object) -> str:
    return sha256(json.dumps(payload, sort_keys=True,
                             default=str).encode("utf-8")).hexdigest()


def q(v: Fraction) -> str:
    return f"{v.numerator}/{v.denominator}"


def vp(value: Fraction, p: int):
    if value == 0:
        return None
    n, d, e = abs(value.numerator), value.denominator, 0
    while n % p == 0:
        n //= p
        e += 1
    while d % p == 0:
        d //= p
        e -= 1
    return e


def prime_factors(n: int) -> list[int]:
    out, m, d = [], abs(n), 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


# --------------------------------------------------------------------------
# exact linear algebra (independent implementation)
# --------------------------------------------------------------------------
def echelon(rows):
    mat = [[Fraction(x) for x in r] for r in rows]
    mat = [r for r in mat if any(r)]
    if not mat:
        return []
    width = len(mat[0])
    out, r = [], 0
    for col in range(width):
        piv = next((i for i in range(r, len(mat)) if mat[i][col] != 0), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        head = mat[r][col]
        mat[r] = [x / head for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][col] != 0:
                f = mat[i][col]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        r += 1
    return [row for row in mat[:r]]


def dim_of(rows) -> int:
    return len(echelon(rows))


def nullspace(rows, width):
    mat = echelon(rows)
    pivots = []
    for row in mat:
        pivots.append(next(i for i, x in enumerate(row) if x != 0))
    free = [c for c in range(width) if c not in pivots]
    basis = []
    for f in free:
        vec = [Fraction(0)] * width
        vec[f] = Fraction(1)
        for i, p in enumerate(pivots):
            vec[p] = -mat[i][f]
        basis.append(vec)
    return basis


def mul3(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def act(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def det(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def orthogonal_group():
    """Rebuilt from M M^T = I with det +1 over {-1,0,1}^9 -- a different
    construction from the primary's signed-permutation enumeration."""
    out = []
    for entries in product((-1, 0, 1), repeat=9):
        m = (entries[0:3], entries[3:6], entries[6:9])
        prod = [[sum(m[i][k] * m[j][k] for k in range(3)) for j in range(3)]
                for i in range(3)]
        if prod != [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
            continue
        if det(m) != 1:
            continue
        out.append(m)
    return sorted(out)


GROUP = orthogonal_group()
GSET = frozenset(GROUP)
INV = {m: next(b for b in GROUP if mul3(m, b) == I3) for m in GROUP}


def order_of(m) -> int:
    cur, k = m, 1
    while cur != I3:
        cur = mul3(cur, m)
        k += 1
    return k


def orbits(subgroup, points):
    seen, out = set(), []
    for p in points:
        if p in seen:
            continue
        orb = {p}
        frontier = [p]
        while frontier:
            cur = frontier.pop()
            for m in subgroup:
                nxt = act(m, cur)
                if nxt not in orb:
                    orb.add(nxt)
                    frontier.append(nxt)
        seen |= orb
        out.append(tuple(sorted(orb)))
    return out


def axis_of(m):
    if m == I3:
        return None
    canon = set()
    for v in product((-1, 0, 1), repeat=3):
        if not any(v) or act(m, v) != v:
            continue
        g = 0
        for x in v:
            g = gcd(g, abs(x))
        w = tuple(x // g for x in v)
        lead = next(x for x in w if x != 0)
        canon.add(w if lead > 0 else tuple(-x for x in w))
    return canon.pop() if len(canon) == 1 else None


def axis_kind(m) -> str:
    a = axis_of(m)
    return {1: "face", 2: "edge", 3: "body"}[sum(1 for x in a if x)]


# --------------------------------------------------------------------------
# independent lattice: ITERATED EXTENSION, not pair closure
# --------------------------------------------------------------------------
def generated_by(seeds) -> frozenset:
    found = {I3} | set(seeds)
    frontier = list(found)
    while frontier:
        cur = frontier.pop()
        for other in list(found):
            for pr in (mul3(cur, other), mul3(other, cur)):
                if pr not in found:
                    found.add(pr)
                    frontier.append(pr)
    return frozenset(found)


def lattice_by_iterated_extension() -> list[frozenset]:
    family = {frozenset({I3})}
    while True:
        grown = set(family)
        for h in family:
            for g in GROUP:
                grown.add(generated_by(set(h) | {g}))
        if grown == family:
            break
        family = grown
    return sorted(family, key=lambda h: (len(h), sorted(h)))


LATTICE = lattice_by_iterated_extension()


def is_cyclic(h) -> bool:
    return any(generated_by({g}) == h for g in h)


def is_abelian(h) -> bool:
    return all(mul3(a, b) == mul3(b, a) for a in h for b in h)


def name_of(h) -> str:
    n = len(h)
    if n == 1:
        return "E_trivial"
    kinds = sorted(axis_kind(m) for m in h if m != I3)
    if is_cyclic(h):
        return f"C{n}_{kinds[0]}"
    if is_abelian(h) and n == 4:
        return "V_face" if set(kinds) == {"face"} else "V_edge"
    return {6: "S3_body", 8: "D4_face", 12: "A4_tetrahedral",
            24: "O_full"}.get(n, f"G{n}")


def normalizer(h) -> frozenset:
    return frozenset(g for g in GROUP
                     if frozenset(mul3(mul3(g, x), INV[g]) for x in h) == h)


def class_of(h) -> frozenset:
    return frozenset(frozenset(mul3(mul3(g, x), INV[g]) for x in h)
                     for g in GROUP)


# --------------------------------------------------------------------------
# independent isotype: MINIMAL CYCLIC SUBMODULES + orthogonal complements
# --------------------------------------------------------------------------
def perm_matrix(elem, points):
    idx = {p: i for i, p in enumerate(points)}
    n = len(points)
    m = [[Fraction(0)] * n for _ in range(n)]
    for j, p in enumerate(points):
        m[idx[act(elem, p)]][j] = Fraction(1)
    return m


def apply_matrix(m, vec):
    n = len(vec)
    return [sum(m[i][j] * vec[j] for j in range(n)) for i in range(n)]


def cyclic_module(mats, w):
    return echelon([apply_matrix(m, w) for m in mats])


def subspace_key(rows):
    return tuple(tuple(q(x) for x in r) for r in echelon(rows))


def test_vectors(basis, n, spread=1):
    dim = len(basis)
    for coeffs in product(range(-spread, spread + 1), repeat=dim):
        if not any(coeffs):
            continue
        yield [sum(Fraction(coeffs[j]) * basis[j][i] for j in range(dim))
               for i in range(n)], list(coeffs)


def orthogonal_complement(ambient, block, n):
    """Complement of `block` inside `ambient` for the standard inner product.
    Permutation representations are orthogonal, so this is a submodule."""
    rows = []
    for b in block:
        rows.append([sum(b[k] * a[k] for k in range(n)) for a in ambient])
    coeffs = nullspace(rows, len(ambient))
    return [[sum(c[j] * ambient[j][i] for j in range(len(ambient)))
             for i in range(n)] for c in coeffs]


def eigen_subspace(block, mat, lam, n):
    """{x in span(block) : mat x = lam x}, in ambient coordinates."""
    d = len(block)
    images = [apply_matrix(mat, b) for b in block]
    rows = [[images[i][j] - Fraction(lam) * block[i][j] for i in range(d)]
            for j in range(n)]
    coeffs = nullspace(rows, d)
    return [[sum(c[i] * block[i][j] for i in range(d)) for j in range(n)]
            for c in coeffs]


def module_generated(mats, vectors):
    return echelon([apply_matrix(m, v) for m in mats for v in vectors])


def proper_submodule(block, mats, n):
    """A proper nonzero submodule of `block`, or None. Two routes: the
    eigen-subspaces of single group elements, and small test vectors."""
    d = len(block)
    if d <= 1:
        return None
    for mat in mats:
        for lam in (1, -1):
            piece = eigen_subspace(block, mat, lam, n)
            if not piece:
                continue
            sub = module_generated(mats, piece)
            if 0 < len(sub) < d:
                return sub
    for spread in (1, 2, 3):
        for w, _ in test_vectors(block, n, spread):
            sub = module_generated(mats, [w])
            if 0 < len(sub) < d:
                return sub
    return None


def split_block(block, mats, n, guard=0):
    """Split one block into irreducibles, recursively."""
    if guard > n + 2:
        return None
    sub = proper_submodule(block, mats, n)
    if sub is None:
        return [block]
    rest = orthogonal_complement(block, sub, n)
    left = split_block(sub, mats, n, guard + 1)
    right = split_block(rest, mats, n, guard + 1) if rest else []
    if left is None or right is None:
        return None
    return left + right


def split_into_irreducibles(subgroup, points):
    """Independent decomposition: peel off a MINIMAL nonzero cyclic submodule,
    split it fully into irreducibles, then continue on its orthogonal
    complement inside the current space."""
    n = len(points)
    mats = [perm_matrix(g, points) for g in sorted(subgroup)]
    ambient = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
               for i in range(n)]
    blocks = []
    guard = 0
    while ambient:
        guard += 1
        if guard > n + 2:
            return None, "peeling did not terminate"
        best = None
        for w, _ in test_vectors(ambient, n, 1):
            span = module_generated(mats, [w])
            if span and (best is None or len(span) < len(best)):
                best = span
            if best is not None and len(best) == 1:
                break
        if best is None:
            return None, "no cyclic submodule found"
        pieces = split_block(best, mats, n)
        if pieces is None:
            return None, "a block could not be split into irreducibles"
        blocks.extend(pieces)
        ambient = orthogonal_complement(ambient, best, n)
    return blocks, None


def block_character(mats, block, elements):
    """Trace of each group element restricted to the block, exactly."""
    n = len(block[0])
    d = len(block)
    cols = [[block[k][i] for k in range(d)] for i in range(n)]
    out = []
    for m in mats:
        images = [apply_matrix(m, b) for b in block]
        rows = [cols[i] + [images[k][i] for k in range(d)] for i in range(n)]
        red = echelon(rows)
        pivots = [next(j for j, x in enumerate(r) if x != 0) for r in red]
        if pivots[:d] != list(range(d)):
            return None
        coeff = [[red[i][d + j] for j in range(d)] for i in range(d)]
        out.append(sum(coeff[i][i] for i in range(d)))
    return tuple(q(x) for x in out)


def block_endomorphism_dimension(mats, block):
    """dim_Q End_{Q[H]}(block), by solving the commutant on the block."""
    n = len(block[0])
    d = len(block)
    cols = [[block[k][i] for k in range(d)] for i in range(n)]
    restricted = []
    for m in mats:
        images = [apply_matrix(m, b) for b in block]
        rows = [cols[i] + [images[k][i] for k in range(d)] for i in range(n)]
        red = echelon(rows)
        restricted.append([[red[i][d + j] for j in range(d)] for i in range(d)])
    eqs = []
    for c in restricted:
        for i in range(d):
            for j in range(d):
                row = [Fraction(0)] * (d * d)
                for k in range(d):
                    row[i * d + k] += c[k][j]
                    row[k * d + j] -= c[i][k]
                eqs.append(row)
    return len(nullspace(eqs, d * d))


def independent_signature(subgroup, points):
    n = len(points)
    elements = sorted(subgroup)
    mats = [perm_matrix(g, points) for g in elements]
    blocks, err = split_into_irreducibles(subgroup, points)
    if blocks is None:
        return {"ok": False, "reason": err}
    # irreducibility certificate: every nonzero small vector in a block must
    # generate the whole block
    irreducible = all(proper_submodule(b, mats, n) is None for b in blocks)
    groups: dict[tuple, list] = {}
    for b in blocks:
        ch = block_character(mats, b, elements)
        if ch is None:
            return {"ok": False, "reason": "block is not invariant"}
        groups.setdefault(ch, []).append(b)
    isotypes = []
    for ch, members in groups.items():
        d = len(members[0])
        isotypes.append({
            "irreducible_degree_over_Q": d,
            "multiplicity": len(members),
            "component_dimension": d * len(members),
            "endomorphism_field_degree":
                block_endomorphism_dimension(mats, members[0]),
            "character": list(ch),
            "is_the_trivial_isotype": all(x == "1/1" for x in ch) and d == 1,
        })
    isotypes.sort(key=lambda b: (b["irreducible_degree_over_Q"],
                                 b["multiplicity"],
                                 b["endomorphism_field_degree"]))
    fine = sorted(d for b in isotypes
                  for d in [b["irreducible_degree_over_Q"]] * b["multiplicity"])
    orbs = orbits(elements, points)
    pair_orbit_count = 0
    seen = set()
    for a in points:
        for b in points:
            if (a, b) in seen:
                continue
            pair_orbit_count += 1
            for g in elements:
                seen.add((act(g, a), act(g, b)))
    inv = len(orbs)
    return {
        "ok": True,
        "space_dimension": n,
        "block_dimensions": sorted(len(b) for b in blocks),
        "every_block_has_no_proper_submodule": irreducible,
        "invariant_multiplicity_by_orbit_count": inv,
        "coarse_pair": [inv, n - inv],
        "coarse_two_adic_profile": [
            vp(Fraction(inv), 2) if inv else None,
            vp(Fraction(n - inv), 2) if n - inv else None],
        "fine_dimensions": fine,
        "fine_sums_to_the_space": sum(fine) == n,
        "fine_top": max(fine) if fine else 0,
        "fine_top_pair": [inv, max(fine) if fine else 0],
        "fine_top_two_adic_profile": [
            vp(Fraction(inv), 2) if inv else None,
            vp(Fraction(max(fine)), 2) if fine and max(fine) else None],
        "isotypes": isotypes,
        "isotypic_decomposition_is_unique":
            all(b["multiplicity"] == 1 for b in isotypes),
        "orbit_count_on_the_product_set": pair_orbit_count,
        "sum_m_squared_field_degree": sum(
            b["multiplicity"] ** 2 * b["endomorphism_field_degree"]
            for b in isotypes),
        "pair_identity_holds": sum(
            b["multiplicity"] ** 2 * b["endomorphism_field_degree"]
            for b in isotypes) == pair_orbit_count,
    }


# --------------------------------------------------------------------------
# independent reachability: Smith-style diagonalization
# --------------------------------------------------------------------------
def diagonalize(matrix):
    a = [row[:] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    u = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    pos = 0
    while pos < min(m, n):
        piv = None
        for i in range(pos, m):
            for j in range(pos, n):
                if a[i][j] != 0:
                    piv = (i, j)
                    break
            if piv:
                break
        if piv is None:
            break
        i, j = piv
        a[pos], a[i] = a[i], a[pos]
        u[pos], u[i] = u[i], u[pos]
        for r in range(m):
            a[r][pos], a[r][j] = a[r][j], a[r][pos]
        while True:
            for i2 in range(pos + 1, m):
                if a[i2][pos]:
                    f = a[i2][pos] // a[pos][pos]
                    for c in range(n):
                        a[i2][c] -= f * a[pos][c]
                    for c in range(m):
                        u[i2][c] -= f * u[pos][c]
                    if a[i2][pos]:
                        a[pos], a[i2] = a[i2], a[pos]
                        u[pos], u[i2] = u[i2], u[pos]
            for j2 in range(pos + 1, n):
                if a[pos][j2]:
                    f = a[pos][j2] // a[pos][pos]
                    for r in range(m):
                        a[r][j2] -= f * a[r][pos]
                    if a[pos][j2]:
                        for r in range(m):
                            a[r][pos], a[r][j2] = a[r][j2], a[r][pos]
            if (all(a[i2][pos] == 0 for i2 in range(pos + 1, m))
                    and all(a[pos][j2] == 0 for j2 in range(pos + 1, n))):
                break
        pos += 1
    return a, u


def solvable(matrix, target) -> bool:
    m = len(target)
    if not matrix or not matrix[0]:
        return not any(target)
    d, u = diagonalize(matrix)
    c = [sum(u[i][k] * target[k] for k in range(m)) for i in range(m)]
    n = len(d[0])
    for i in range(m):
        pivot = d[i][i] if i < n else 0
        if pivot == 0:
            if c[i] != 0:
                return False
        elif c[i] % pivot != 0:
            return False
    return True


def reaches(generators, target: Fraction) -> bool:
    gens = sorted({g for g in generators if g not in (0, 1, -1)})
    primes = sorted(set([p for g in gens for p in prime_factors(g)]
                        + prime_factors(target.numerator)
                        + prime_factors(target.denominator)))
    if not primes:
        return True
    if not gens:
        return not any(vp(target, p) for p in primes)
    matrix = [[vp(Fraction(g), p) for g in gens] for p in primes]
    return solvable(matrix, [vp(target, p) for p in primes])


# --------------------------------------------------------------------------
# the checker's own analysis of every subgroup
# --------------------------------------------------------------------------
def analyse_lattice():
    class_index = {}
    classes = []
    for h in LATTICE:
        if h in class_index:
            continue
        k = class_of(h)
        idx = len(classes)
        classes.append(k)
        for member in k:
            class_index[member] = idx
    rows = []
    for h in LATTICE:
        order = len(h)
        orbs = orbits(sorted(h), SHELL)
        lengths = sorted(len(o) for o in orbs)
        free = [o for o in orbs if len(o) == order]

        def canon(v):
            lead = next(x for x in v if x != 0)
            return v if lead > 0 else tuple(-x for x in v)

        seen, axis_orbits = set(), []
        for a in AXES:
            if a in seen:
                continue
            orb = {canon(act(m, a)) for m in h}
            seen |= orb
            axis_orbits.append(orb)
        shell = independent_signature(h, list(SHELL))
        orbit = independent_signature(h, sorted(max(free, key=len))) \
            if free else None
        rows.append({
            "key": h,
            "name": name_of(h),
            "order": order,
            "class_index": class_index[h],
            "is_cyclic": is_cyclic(h),
            "normalizer_order": len(normalizer(h)),
            "shell_orbit_lengths": lengths,
            "shell_orbit_count": len(orbs),
            "acts_freely": all(L == order for L in lengths),
            "transitive": len(orbs) == 1,
            "simply_transitive": len(orbs) == 1 and lengths == [order],
            "maximal_free_orbit_length":
                max([L for L in lengths if L == order], default=0),
            "has_free_orbit": bool(free),
            "axis_transitive": len(axis_orbits) == 1,
            "shell": shell,
            "orbit": orbit,
        })
    return sorted(rows, key=lambda r: (r["order"], r["name"],
                                       sorted(r["key"]))), len(classes)


ANALYSIS, CLASS_COUNT = analyse_lattice()


def receipt():
    return json.loads(_text(AUDIT_INPUT_PATHS[1]))


# --------------------------------------------------------------------------
# certificate A
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows, ok = [], True
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        exists = target.exists()
        got = sha256(_bytes(path)).hexdigest() if exists else None
        blob = subprocess.run(["git", "hash-object", str(target)],
                              capture_output=True, text=True,
                              cwd=str(ROOT)).stdout.strip() if exists else None
        sha_ok = got == EXPECTED_SHA256[path]
        blob_ok = blob == EXPECTED_GIT_BLOBS[path]
        ok = ok and exists and sha_ok and blob_ok
        rows.append({"path": path, "absolute_path": str(target),
                     "exists": exists, "sha256": got,
                     "sha256_matches_pin": sha_ok, "git_blob": blob,
                     "git_blob_matches_pin": blob_ok})
    cache = _text(AUDIT_INPUT_PATHS[2])
    declares = f"runner_sha256: {EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]]}" in cache
    exit_zero = "exit_code: 0" in cache
    ok = ok and declares and exit_zero
    return {
        "statement": "The primary, its receipt, its run cache and every "
                     "upstream artifact it read are pinned twice over.",
        "rows": rows,
        "run_cache_declares_the_pinned_runner_digest": declares,
        "run_cache_records_exit_zero": exit_zero,
        "finding": (
            f"{sum(1 for r in rows if r['sha256_matches_pin'] and r['git_blob_matches_pin'])}"
            f"/{len(rows)} pins round-trip; the run cache declares the pinned "
            f"runner digest and exit 0."),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate B
# --------------------------------------------------------------------------
def group_certificate() -> dict:
    closed = all(mul3(a, b) in GSET for a in GROUP for b in GROUP)
    orders = {}
    for m in GROUP:
        orders[order_of(m)] = orders.get(order_of(m), 0) + 1
    signed = set()
    for perm in product(range(3), repeat=3):
        if len(set(perm)) != 3:
            continue
        for signs in product((1, -1), repeat=3):
            rows = []
            for i in range(3):
                row = [0, 0, 0]
                row[perm[i]] = signs[i]
                rows.append(tuple(row))
            mm = tuple(rows)
            if det(mm) == 1:
                signed.add(mm)
    same = signed == GSET
    agrees = (len(GROUP) == 24 and closed and same
              and orders == {1: 1, 2: 9, 3: 8, 4: 6})
    return {
        "statement": "The rotation group rebuilt from the orthogonality "
                     "condition M M^T = I with det = +1 over 19683 integer "
                     "matrices -- a different construction from the primary's "
                     "signed-permutation enumeration.",
        "candidates_scanned": 3 ** 9,
        "group_order": len(GROUP),
        "closed": closed,
        "element_order_counts": dict(sorted(orders.items())),
        "orthogonality_construction_equals_signed_permutation_construction":
            same,
        "primary_claim_reproduced": agrees,
        "verdict": "SURVIVES" if agrees else "REFUTED",
        "finding": (
            f"The orthogonality construction returns the same {len(GROUP)} "
            f"matrices with order profile {dict(sorted(orders.items()))}; the "
            f"primary's group claim {'SURVIVES' if agrees else 'is REFUTED'}."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate C
# --------------------------------------------------------------------------
def lattice_certificate() -> dict:
    r = receipt()
    counts: dict[str, int] = {}
    for h in LATTICE:
        counts[name_of(h)] = counts.get(name_of(h), 0) + 1
    claimed = {row["name"]: row["size"] for row in r["subgroup_lattice_census"]}
    class_eq = []
    for row in r["subgroup_lattice_census"]:
        members = [h for h in LATTICE if name_of(h) == row["name"]]
        norm_order = len(normalizer(members[0]))
        class_eq.append({
            "class": row["name"], "independent_size": len(members),
            "independent_normalizer_order": norm_order,
            "size_times_normalizer": len(members) * norm_order,
            "equals_the_group_order": len(members) * norm_order == len(GROUP),
            "primary_size": row["size"],
            "sizes_agree": len(members) == row["size"],
        })
    n2 = sum(1 for h in LATTICE if len(h) == 8)
    n3 = sum(1 for h in LATTICE if len(h) == 3)
    sylow = (n2 % 2 == 1 and 3 % n2 == 0 and n3 % 3 == 1 and 8 % n3 == 0)
    # a third route: subgroups generated by every SUBSET of size <= 3
    third = {frozenset({I3})}
    for size in (1, 2, 3):
        for seeds in combinations(GROUP, size):
            third.add(generated_by(set(seeds)))
    third_agrees = set(third) == set(LATTICE)
    agrees = (len(LATTICE) == r["subgroups_found"]
              and CLASS_COUNT == r["conjugacy_classes"]
              and counts == claimed
              and all(row["equals_the_group_order"] for row in class_eq)
              and all(row["sizes_agree"] for row in class_eq))
    return {
        "statement": "The subgroup lattice rebuilt by ITERATED EXTENSION -- "
                     "close <H, g> for every found H and every group element "
                     "until the family is stable -- then cross-checked against "
                     "a third route (closure of every subset of size <= 3), "
                     "the class equation and the Sylow congruences. A dropped "
                     "class cannot survive three routes.",
        "subgroups_found": len(LATTICE),
        "conjugacy_classes": CLASS_COUNT,
        "subgroups_by_derived_name": dict(sorted(counts.items())),
        "primary_claimed_by_name": dict(sorted(claimed.items())),
        "class_equation_rows": class_eq,
        "third_route_subset_closure_agrees": third_agrees,
        "sylow_2_count": n2,
        "sylow_3_count": n3,
        "sylow_congruences_hold": sylow,
        "primary_claim_reproduced": agrees and third_agrees and sylow,
        "verdict": "SURVIVES" if agrees and third_agrees and sylow
                   else "REFUTED",
        "finding": (
            f"{len(LATTICE)} subgroups in {CLASS_COUNT} classes by iterated "
            f"extension, identical to the subset-closure route "
            f"({third_agrees}); the class equation holds on every class and "
            f"the Sylow congruences hold (n_2 = {n2}, n_3 = {n3}); the "
            f"primary's lattice "
            f"{'SURVIVES' if agrees else 'is REFUTED'}."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate D
# --------------------------------------------------------------------------
def isotype_certificate() -> dict:
    r = receipt()
    claimed = {row["name"]: row for row in r["signatures_by_class"]}
    rows, agree_all = [], True
    for name in sorted(claimed):
        mine = next(x for x in ANALYSIS if x["name"] == name)
        want = claimed[name]
        shell, orbit = mine["shell"], mine["orbit"]
        same = (
            shell["coarse_pair"] == want["shell_scope_pair"]
            and shell["coarse_two_adic_profile"] == want["shell_scope_profile"]
            and shell["fine_dimensions"] == want["shell_scope_fine_dims"]
            and shell["fine_top_pair"] == want["shell_scope_fine_top_pair"]
            and shell["isotypic_decomposition_is_unique"]
            == want["shell_scope_decomposition_is_unique"]
            and ((orbit is None and not want["orbit_scope_exists"])
                 or (orbit is not None and want["orbit_scope_exists"]
                     and orbit["coarse_pair"] == want["orbit_scope_pair"]
                     and orbit["coarse_two_adic_profile"]
                     == want["orbit_scope_profile"]
                     and orbit["fine_dimensions"] == want["orbit_scope_fine_dims"]
                     and orbit["fine_top_pair"] == want["orbit_scope_fine_top_pair"]
                     and orbit["isotypic_decomposition_is_unique"]
                     == want["orbit_scope_decomposition_is_unique"])))
        gates = (shell["fine_sums_to_the_space"] and shell["pair_identity_holds"]
                 and shell["every_block_has_no_proper_submodule"]
                 and (orbit is None or (orbit["fine_sums_to_the_space"]
                                        and orbit["pair_identity_holds"])))
        agree_all = agree_all and same and gates
        rows.append({
            "name": name,
            "independent_shell": {k: v for k, v in shell.items()
                                  if k != "isotypes"},
            "independent_orbit": ({k: v for k, v in orbit.items()
                                   if k != "isotypes"} if orbit else None),
            "independent_shell_isotypes": [
                {k: v for k, v in b.items() if k != "character"}
                for b in shell["isotypes"]],
            "independent_orbit_isotypes": ([
                {k: v for k, v in b.items() if k != "character"}
                for b in orbit["isotypes"]] if orbit else None),
            "primary_shell_pair": want["shell_scope_pair"],
            "primary_orbit_pair": want["orbit_scope_pair"],
            "agrees_with_the_primary": same,
            "own_gates_hold": gates,
        })
    coarse = sorted(x["name"] for x in ANALYSIS
                    if x["orbit"] and x["orbit"]["coarse_pair"] == [1, 2])
    fine = sorted(x["name"] for x in ANALYSIS
                  if x["orbit"] and x["orbit"]["fine_top_pair"] == [1, 2])
    return {
        "statement": "Every isotype number rebuilt by MINIMAL CYCLIC "
                     "SUBMODULES and orthogonal complements, with block "
                     "characters used to group blocks into isotypes -- no "
                     "enveloping algebra, no centre, no minimal polynomial, no "
                     "cyclotomics. Each block additionally carries an "
                     "irreducibility certificate (no proper submodule is found by "
                     "either of two routes) and the decomposition is gated "
                     "against the orbit count on X x X.",
        "rows": rows,
        "classes_carrying_1_2_coarse_at_the_orbit_scope": sorted(set(coarse)),
        "classes_carrying_1_2_fine_at_the_orbit_scope": sorted(set(fine)),
        "primary_claim_reproduced": agree_all,
        "verdict": "SURVIVES" if agree_all else "REFUTED",
        "finding": (
            f"All {len(rows)} class signatures reproduce by the independent "
            f"route ({'SURVIVES' if agree_all else 'REFUTED'}); coarse (1,2) "
            f"at {sorted(set(coarse))}, fine (1,2) at {sorted(set(fine))}."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate E: every selector survivor set, recomputed
# --------------------------------------------------------------------------
def independent_selector_survivors(pool) -> dict:
    shell_inv = {r["name"]: r["shell"]["invariant_multiplicity_by_orbit_count"]
                 for r in pool}
    min_inv = min(shell_inv.values())
    free = [r for r in pool if r["acts_freely"]]
    max_free = max((r["maximal_free_orbit_length"] for r in free), default=0)

    def ob(r, key):
        return r["orbit"][key] if r["orbit"] else None

    tests = {
        "SEL01_free_on_shell": lambda r: r["acts_freely"],
        "SEL02_transitive_on_shell": lambda r: r["transitive"],
        "SEL03_multiplicity_one_orbit_scope":
            lambda r: ob(r, "invariant_multiplicity_by_orbit_count") == 1,
        "SEL04_multiplicity_one_shell_scope":
            lambda r: shell_inv[r["name"]] == 1,
        "SEL05_minimal_shell_invariant_multiplicity":
            lambda r: shell_inv[r["name"]] == min_inv,
        "SEL06_maximal_free_shell_orbit":
            lambda r: r["acts_freely"]
            and r["maximal_free_orbit_length"] == max_free,
        "SEL07_coarse_pair_v2_equals_one":
            lambda r: (ob(r, "coarse_two_adic_profile") or [None, None])[1] == 1,
        "SEL08_reachability_R1_orbit_scope":
            lambda r: bool(r["orbit"]) and reaches(
                [r["order"]] + r["orbit"]["coarse_pair"], TARGET),
        "SEL09_reachability_R2_shell_scope":
            lambda r: reaches(sorted(set(r["shell_orbit_lengths"]))
                              + r["shell"]["coarse_pair"], TARGET),
        "SEL10_fine_top_pair_is_the_target":
            lambda r: tuple(ob(r, "fine_top_pair") or ()) == TARGET_PAIR,
        "SEL11_transitive_on_coordinate_axes": lambda r: r["axis_transitive"],
        "SEL12_odd_order": lambda r: r["order"] % 2 == 1,
        "SEL13_count_once": lambda r: sum(r["shell_orbit_lengths"]) == 6,
        "SEL14_content_only_readout":
            lambda r: r["shell"]["space_dimension"] == 6,
        "SEL15_admissibility_covariance": lambda r: set(r["key"]) <= GSET,
        "SEL16_no_site_privileged_read_literally": lambda r: all(
            {frozenset(o) for o in orbits(
                sorted(frozenset(mul3(mul3(g, x), INV[g]) for x in r["key"])),
                SHELL)}
            == {frozenset(act(g, v) for v in o)
                for o in orbits(sorted(r["key"]), SHELL)}
            for g in GROUP),
    }
    return {sid: sorted({r["name"] for r in pool if fn(r)})
            for sid, fn in tests.items()}


def selector_certificate() -> dict:
    r = receipt()
    mine = independent_selector_survivors(ANALYSIS)
    theirs = r["survivors_per_selector"]
    rows = []
    for sid in sorted(theirs):
        rows.append({"id": sid, "primary_survivors": theirs[sid],
                     "independent_survivors": mine.get(sid),
                     "identical": mine.get(sid) == theirs[sid]})
    agree = all(x["identical"] for x in rows)
    # the 886 restriction, recomputed independently as well
    cyclic_pool = [x for x in ANALYSIS
                   if x["name"] in ("C2_edge", "C2_face", "C3_body", "C4_face")]
    restricted = independent_selector_survivors(cyclic_pool)
    r886 = json.loads(_text(AUDIT_INPUT_PATHS[5]))["survivors_per_selector"]
    restriction_rows = [{"id": sid, "cycle886": r886[sid],
                         "independent_restricted": restricted[sid],
                         "identical": restricted[sid] == r886[sid]}
                        for sid in sorted(r886)]
    restriction_ok = all(x["identical"] for x in restriction_rows)
    c3 = [x["id"] for x in rows if x["independent_survivors"] == ["C3_body"]]
    s3 = [x["id"] for x in rows if x["independent_survivors"] == ["S3_body"]]
    return {
        "statement": "All sixteen selector survivor sets recomputed over all "
                     "thirty subgroups from the checker's own signatures, and "
                     "the Cycle-886 restriction independently re-derived and "
                     "compared against the pinned 886 receipt.",
        "rows": rows,
        "independent_survivors_per_selector": mine,
        "primary_claim_reproduced": agree,
        "restriction_rows": restriction_rows,
        "restriction_reproduces_cycle886_independently": restriction_ok,
        "selectors_isolating_C3_body": c3,
        "selectors_isolating_S3_body": s3,
        "verdict": "SURVIVES" if agree and restriction_ok else "REFUTED",
        "finding": (
            f"{sum(1 for x in rows if x['identical'])}/{len(rows)} selector "
            f"survivor sets reproduce over the full lattice and "
            f"{sum(1 for x in restriction_rows if x['identical'])}"
            f"/{len(restriction_rows)} reproduce under the 886 restriction; "
            f"C3 is isolated by {c3} and S3 by {s3}."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate F: reachability, re-decided
# --------------------------------------------------------------------------
def reachability_certificate() -> dict:
    self_tests = [
        {"matrix": [[1], [0]], "target": [1, -2], "expected": False},
        {"matrix": [[1, 0], [0, 1]], "target": [1, -2], "expected": True},
        {"matrix": [[2, 0], [0, 1]], "target": [1, -2], "expected": False},
        {"matrix": [[2, 0], [0, 1]], "target": [4, -2], "expected": True},
        {"matrix": [[0], [1]], "target": [0, 5], "expected": True},
        {"matrix": [[1, 1], [0, 1]], "target": [1, -2], "expected": True},
    ]
    for t in self_tests:
        t["computed"] = solvable(t["matrix"], t["target"])
        t["ok"] = t["computed"] == t["expected"]
    solver_ok = all(t["ok"] for t in self_tests)

    survivors: dict[str, set] = {k: set() for k in (
        "R1_orbit_scope_coarse", "R2_shell_scope_coarse",
        "R3_orbit_scope_fine", "R4_shell_scope_fine")}
    rows = []
    for x in ANALYSIS:
        lengths = sorted(set(x["shell_orbit_lengths"]))
        gens = {"R2_shell_scope_coarse": lengths + x["shell"]["coarse_pair"],
                "R4_shell_scope_fine": lengths + x["shell"]["fine_dimensions"]}
        if x["orbit"]:
            gens["R1_orbit_scope_coarse"] = \
                [x["order"]] + x["orbit"]["coarse_pair"]
            gens["R3_orbit_scope_fine"] = \
                [x["order"]] + x["orbit"]["fine_dimensions"]
        per = {}
        for rule, g in gens.items():
            got = reaches(g, TARGET)
            per[rule] = {"generators": sorted({v for v in g if v > 1}),
                         "reachable": got}
            if got:
                survivors[rule].add(x["name"])
        rows.append({"name": x["name"], "per_rule": per})
    mine = {k: sorted(v) for k, v in survivors.items()}
    theirs = receipt()["reachability_survivors_by_rule"]
    agree = all(mine[k] == theirs[k] for k in theirs)
    return {
        "statement": "Multiplicative reachability of 2/9 re-decided by "
                     "Smith-style diagonalization with a tracked left "
                     "transform, self-tested on six lattices with known "
                     "answers before it is trusted.",
        "solver_self_tests": self_tests,
        "solver_self_test_passed": solver_ok,
        "rows": rows,
        "independent_survivors_by_rule": mine,
        "primary_survivors_by_rule": theirs,
        "primary_claim_reproduced": agree,
        "scope_circularity_still_present":
            mine["R1_orbit_scope_coarse"] != mine["R2_shell_scope_coarse"],
        "reading_dependence_present":
            mine["R1_orbit_scope_coarse"] != mine["R3_orbit_scope_fine"],
        "verdict": "SURVIVES" if agree and solver_ok else "REFUTED",
        "finding": (
            f"the solver passes {sum(1 for t in self_tests if t['ok'])}"
            f"/{len(self_tests)} self-tests and the survivor sets "
            f"{'reproduce' if agree else 'DO NOT reproduce'}: "
            + "; ".join(f"{k} -> {v}" for k, v in sorted(mine.items()))),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate G: THE SL1-TRANSFER CLAIM, ATTACKED HARDEST
# --------------------------------------------------------------------------
def all_irreducible_submodules(subgroup, points, degree, limit=400):
    """Every distinct IRREDUCIBLE submodule of the given degree reachable
    from small vectors -- the search a refutation would have to survive.
    Cyclic submodules that turn out to be reducible are discarded: a readout
    carrying a weight is an irreducible constituent, not any old submodule."""
    n = len(points)
    mats = [perm_matrix(g, points) for g in sorted(subgroup)]
    basis = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
             for i in range(n)]
    found = {}
    for w, coeffs in test_vectors(basis, n, 1):
        span = module_generated(mats, [w])
        if len(span) != degree:
            continue
        if proper_submodule(span, mats, n) is not None:
            continue                      # cyclic but REDUCIBLE: not a readout
        key = subspace_key(span)
        if key not in found:
            found[key] = {"generator": [q(x) for x in w],
                          "basis": [[q(x) for x in r] for r in span],
                          "character": block_character(mats, span,
                                                       sorted(subgroup))}
        if len(found) >= limit:
            break
    return list(found.values())


def sl1_transfer_certificate(r=None) -> dict:
    r = r if r is not None else receipt()
    s3 = next(x for x in ANALYSIS if x["name"] == "S3_body")
    points = sorted(max([o for o in orbits(sorted(s3["key"]), SHELL)
                         if len(o) == 6], key=len))
    sig = independent_signature(s3["key"], points)
    mults = [[b["irreducible_degree_over_Q"], b["multiplicity"]]
             for b in sig["isotypes"]]

    # ATTACK 1: is there a second inequivalent readout with a DIFFERENT pair?
    degrees = sorted({b["irreducible_degree_over_Q"] for b in sig["isotypes"]})
    submodules_by_degree = {d: all_irreducible_submodules(s3["key"], points, d)
                            for d in degrees}
    characters_by_degree = {
        d: sorted({tuple(m["character"]) for m in subs})
        for d, subs in submodules_by_degree.items()}
    top_degree = max(degrees)
    distinct_top = len(submodules_by_degree[top_degree])
    top_characters = characters_by_degree[top_degree]
    alternative_pair_exists = len(top_characters) > 1
    achievable_top_pairs = sorted({
        (sig["invariant_multiplicity_by_orbit_count"], d) for d in degrees})

    # ATTACK 2: is the isotypic component itself ambiguous?  The sum of every
    # top-degree submodule must be exactly the top isotypic component.
    span_of_tops = echelon([
        [Fraction(int(x.split("/")[0]), int(x.split("/")[1])) for x in row]
        for m in submodules_by_degree[top_degree] for row in m["basis"]])
    top_component_dimension = next(
        b["component_dimension"] for b in sig["isotypes"]
        if b["irreducible_degree_over_Q"] == top_degree)
    isotypic_component_is_canonical = len(span_of_tops) == top_component_dimension

    # ATTACK 3: the peer comparison -- are C3 and C4 really multiplicity-free?
    peers = []
    for name in ("C3_body", "C4_face", "S3_body"):
        row = next(x for x in ANALYSIS if x["name"] == name)
        o = row["orbit"]
        peers.append({
            "class": name,
            "free_orbit_length": row["maximal_free_orbit_length"],
            "independent_coarse_pair": o["coarse_pair"],
            "independent_fine_dims": o["fine_dimensions"],
            "independent_fine_top_pair": o["fine_top_pair"],
            "independent_multiplicities":
                [b["multiplicity"] for b in o["isotypes"]],
            "independent_decomposition_is_unique":
                o["isotypic_decomposition_is_unique"],
        })
    peer_claim = (
        peers[0]["independent_decomposition_is_unique"]
        and peers[1]["independent_decomposition_is_unique"]
        and not peers[2]["independent_decomposition_is_unique"])

    claimed = r["S3_pricing_row"]["SL1_TRANSFER"]
    primary_verdict = claimed["verdict"]
    independent_verdict = (
        "FORCED" if sig["isotypic_decomposition_is_unique"]
        else "NUMERICALLY_TRANSFERS_BUT_THE_SUBSPACE_IS_NOT_FORCED")
    verdicts_agree = independent_verdict == primary_verdict
    coarse_agrees = sig["coarse_pair"] == r["S3_pricing_row"][
        "coarse_reading_weight_pair"]
    fine_agrees = sig["fine_top_pair"] == r["S3_pricing_row"][
        "fine_reading_top_pair"]
    survives = (verdicts_agree and coarse_agrees and fine_agrees
                and peer_claim and not alternative_pair_exists)
    return {
        "statement": "THE SL1-TRANSFER CLAIM, ATTACKED. The primary says the "
                     "S3 readout's fine-top pair (1, 2) transfers as a NUMBER "
                     "but not as a forced subspace. Refuting that requires "
                     "either (i) a second inequivalent readout construction at "
                     "S3 scope carrying a DIFFERENT pair, or (ii) showing the "
                     "S3 decomposition is in fact unique, or (iii) breaking "
                     "the peer comparison at C3 and C4. All three are "
                     "attempted here.",
        "independent_S3_signature": {k: v for k, v in sig.items()
                                     if k != "isotypes"},
        "independent_S3_isotypes": [{k: v for k, v in b.items()
                                     if k != "character"}
                                    for b in sig["isotypes"]],
        "independent_multiplicities": mults,
        "attack_1_second_readout_with_a_different_pair": {
            "irreducible_degrees_present": degrees,
            "distinct_submodules_found_by_degree": {
                str(d): len(v) for d, v in submodules_by_degree.items()},
            "distinct_characters_by_degree": {
                str(d): len(v) for d, v in characters_by_degree.items()},
            "distinct_top_degree_submodules": distinct_top,
            "all_top_degree_submodules_are_isomorphic":
                not alternative_pair_exists,
            "achievable_fine_top_pairs": [list(p) for p in achievable_top_pairs],
            "a_readout_with_a_DIFFERENT_pair_exists": alternative_pair_exists,
            "result": ("REFUTES the transfer claim" if alternative_pair_exists
                       else "the pair (1, 2) is stable across every readout "
                            "choice, so the NUMBER transfers -- the primary's "
                            "claim survives this attack"),
            "sample_top_degree_submodules":
                submodules_by_degree[top_degree][:3],
        },
        "attack_2_is_the_isotypic_component_canonical": {
            "span_of_all_top_degree_submodules": len(span_of_tops),
            "top_isotypic_component_dimension": top_component_dimension,
            "isotypic_level_is_canonical": isotypic_component_is_canonical,
            "result": ("the isotypic decomposition IS forced while the split "
                       "into irreducibles is NOT -- exactly the distinction "
                       "the primary draws"
                       if isotypic_component_is_canonical else
                       "the isotypic level is not canonical either, which "
                       "would REFUTE the primary's framing"),
        },
        "attack_3_peer_comparison": {
            "peers": peers,
            "C3_and_C4_are_multiplicity_free_and_S3_is_not": peer_claim,
            "result": ("the peer comparison stands" if peer_claim
                       else "the peer comparison is REFUTED"),
        },
        "primary_verdict": primary_verdict,
        "independent_verdict": independent_verdict,
        "verdicts_agree": verdicts_agree,
        "coarse_pair_agrees": coarse_agrees,
        "fine_top_pair_agrees": fine_agrees,
        "verdict": "SURVIVES" if survives else "REFUTED",
        "finding": (
            f"independent S3 multiplicities {mults}; "
            f"{distinct_top} distinct {top_degree}-dimensional submodules "
            f"found, all with the same character "
            f"({not alternative_pair_exists}), so no readout with a different "
            f"pair exists; the isotypic level is canonical "
            f"({isotypic_component_is_canonical}); C3/C4 multiplicity-free and "
            f"S3 not ({peer_claim}); the transfer claim "
            f"{'SURVIVES' if survives else 'is REFUTED'}."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate H: the scope-insensitivity verdicts, recomputed
# --------------------------------------------------------------------------
def scope_insensitivity_certificate(r=None) -> dict:
    r = r if r is not None else receipt()
    menu = sorted({x["name"] for x in ANALYSIS
                   if x["has_free_orbit"] and x["maximal_free_orbit_length"] > 1})
    claimed_menu = sorted(r["scope_insensitivity"]["menu_classes"])
    rows = []
    for name in menu:
        x = next(y for y in ANALYSIS if y["name"] == name)
        lengths = sorted(set(x["shell_orbit_lengths"]))
        o, sh = x["orbit"], x["shell"]
        entry = {"scope_class": name}
        for tag, base, widened in (
            ("ORBIT_SCOPE_coarse_reading", [x["order"]],
             [x["order"]] + o["coarse_pair"]),
            ("ORBIT_SCOPE_fine_reading", [x["order"]],
             [x["order"]] + o["fine_dimensions"]),
            ("SHELL_SCOPE_coarse_reading", lengths,
             lengths + sh["coarse_pair"]),
            ("SHELL_SCOPE_fine_reading", lengths,
             lengths + sh["fine_dimensions"]),
        ):
            entry[tag] = {
                "base_reachable": reaches(base, TARGET),
                "widened_reachable": reaches(widened, TARGET),
                "defeats_C882_T6":
                    (not reaches(base, TARGET)) and reaches(widened, TARGET),
            }
        rows.append(entry)
    readings = ("ORBIT_SCOPE_coarse_reading", "ORBIT_SCOPE_fine_reading",
                "SHELL_SCOPE_coarse_reading", "SHELL_SCOPE_fine_reading")
    mine = {}
    for reading in readings:
        working = sorted(e["scope_class"] for e in rows
                         if e[reading]["defeats_C882_T6"])
        mine[reading] = {
            "working_set": working,
            "verdict": ("SCOPE_INSENSITIVE" if working == menu
                        else "SCOPE_SENSITIVE" if working
                        else "NO_SCOPE_WORKS")}
    claimed = r["scope_insensitivity"]["per_reading"]
    per_reading_rows = [
        {"reading": k, "primary_working_set": claimed[k]["working_set"],
         "independent_working_set": mine[k]["working_set"],
         "primary_verdict": claimed[k]["verdict"],
         "independent_verdict": mine[k]["verdict"],
         "identical": (claimed[k]["working_set"] == mine[k]["working_set"]
                       and claimed[k]["verdict"] == mine[k]["verdict"])}
        for k in readings]
    coarse, fine = mine[readings[0]], mine[readings[1]]
    if coarse["verdict"] == fine["verdict"] == "SCOPE_INSENSITIVE":
        overall = "SCOPE_INSENSITIVE"
    elif coarse["working_set"] != fine["working_set"]:
        overall = "MIXED"
    elif coarse["verdict"] == fine["verdict"]:
        overall = coarse["verdict"]
    else:
        overall = "MIXED"
    claimed_overall = r["scope_insensitivity"]["OVERALL_VERDICT"]
    agree = (all(x["identical"] for x in per_reading_rows)
             and overall == claimed_overall and menu == claimed_menu)
    return {
        "statement": "The scope-insensitivity verdicts recomputed from "
                     "scratch: the menu membership rule re-applied to the "
                     "checker's own orbit structures, Cycle 883's widening "
                     "step re-evaluated at every menu scope under both "
                     "readings at both scopes, and the verdicts re-derived.",
        "independent_menu": menu,
        "primary_menu": claimed_menu,
        "menus_agree": menu == claimed_menu,
        "rows": rows,
        "per_reading_comparison": per_reading_rows,
        "independent_overall_verdict": overall,
        "primary_overall_verdict": claimed_overall,
        "overall_verdicts_agree": overall == claimed_overall,
        "primary_claim_reproduced": agree,
        "verdict": "SURVIVES" if agree else "REFUTED",
        "finding": (
            f"independent menu {menu}; " + "; ".join(
                f"{k.split('_reading')[0]} -> {mine[k]['verdict']} "
                f"{mine[k]['working_set']}" for k in readings)
            + f"; OVERALL {overall} (primary said {claimed_overall})"),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate I: the upstream (886/883) pins the primary carried over
# --------------------------------------------------------------------------
def module_constants(path: str) -> dict:
    tree = ast.parse(_text(path))
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                out[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError, SyntaxError):
                continue
    return out


def upstream_pin_certificate() -> dict:
    r = receipt()
    c886 = module_constants(AUDIT_INPUT_PATHS[4])
    axioms = norm(_text(AUDIT_INPUT_PATHS[3]))
    memo_sentences = c886.get("AXIOM_SENTENCES", {})
    src886 = _text(AUDIT_INPUT_PATHS[4])
    src883 = _text(AUDIT_INPUT_PATHS[6])

    # every quoted sentence the primary carried must be verbatim 886 material
    quote_rows = []
    for sel in r["selectors"]:
        sentence = sel["quoted_sentence"]
        if sentence is None:
            quote_rows.append({"id": sel["id"], "quoted": None,
                               "verbatim_in_886_source": True,
                               "in_axiom_memo": None, "ok": True})
            continue
        in886 = norm(sentence) in {norm(v) for v in memo_sentences.values()} \
            or norm(sentence) == norm(c886.get("C882_T6_NEEDLE", ""))
        in_memo = norm(sentence) in axioms
        expect_memo = sel["quote_source"] == AUDIT_INPUT_PATHS[3]
        quote_rows.append({"id": sel["id"],
                           "quoted": sentence[:60] + "...",
                           "verbatim_in_886_source": in886,
                           "in_axiom_memo": in_memo,
                           "ok": in886 and (in_memo == expect_memo)})
    quotes_ok = all(x["ok"] for x in quote_rows)

    # the fidelity grades must be the 886 grades, unchanged
    tree = ast.parse(src886)
    fn = next(n for n in ast.walk(tree)
              if isinstance(n, ast.FunctionDef)
              and n.name == "selector_table_certificate")
    assign = next(n for n in ast.walk(fn)
                  if isinstance(n, ast.Assign)
                  and isinstance(n.targets[0], ast.Name)
                  and n.targets[0].id == "selectors")
    grades886 = {}
    for elt in assign.value.elts:
        d = {k.value: v for k, v in zip(elt.keys, elt.values)}
        grades886[d["id"].value] = {
            "fidelity": d["fidelity"].value,
            "grounded": d["grounded"].value,
        }
    grade_rows = []
    for sel in r["selectors"]:
        want = grades886.get(sel["id"], {})
        grade_rows.append({
            "id": sel["id"],
            "cycle886_fidelity": want.get("fidelity"),
            "carried_fidelity": sel["fidelity_grade_pinned_from_886"],
            "cycle886_grounded": want.get("grounded"),
            "carried_grounded": sel["grounded_pinned_from_886"],
            "identical": (want.get("fidelity")
                          == sel["fidelity_grade_pinned_from_886"]
                          and want.get("grounded")
                          == sel["grounded_pinned_from_886"])})
    grades_ok = all(x["identical"] for x in grade_rows)

    # the survivor EXPRESSIONS the primary re-implemented must be 886 source
    expr_ok = all(sel["survivor_expression_source_886"] in src886
                  for sel in r["selectors"]
                  if sel.get("survivor_expression_source_886"))

    # Cycle 883's defeat condition must be 883 source
    defeat = r["scope_insensitivity"]["table"] and True
    t6_line = "defeated = (not old_reach) and new_reach"
    t6_ok = t6_line in src883

    ok = quotes_ok and grades_ok and expr_ok and t6_ok
    return {
        "statement": "Everything the primary CARRIED OVER as a pin from Cycle "
                     "886 and Cycle 883 is verified byte-identical against the "
                     "pinned sources here: the byte-quoted sentences, the "
                     "fidelity grades, the grounding flags, the survivor "
                     "expressions the primary re-implemented, and Cycle 883's "
                     "defeat condition.",
        "quote_rows": quote_rows,
        "quoted_sentences_are_verbatim_886_material": quotes_ok,
        "grade_rows": grade_rows,
        "fidelity_grades_carried_unchanged": grades_ok,
        "survivor_expressions_are_verbatim_886_source": expr_ok,
        "cycle883_defeat_condition_present_in_883_source": t6_ok,
        "cycle883_defeat_condition": t6_line,
        "primary_claim_reproduced": ok,
        "verdict": "SURVIVES" if ok else "REFUTED",
        "finding": (
            f"{sum(1 for x in quote_rows if x['ok'])}/{len(quote_rows)} quoted "
            f"sentences and {sum(1 for x in grade_rows if x['identical'])}"
            f"/{len(grade_rows)} fidelity grades are byte-identical to Cycle "
            f"886; the survivor expressions round-trip ({expr_ok}) and Cycle "
            f"883's defeat condition is present in its source ({t6_ok})."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate K: teeth
# --------------------------------------------------------------------------
MUTATIONS = (
    {
        "id": "T1_tampered_pin",
        "old": '"fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697"',
        "new": '"0000000000000000000000000000000000000000000000000000000000000000"',
        "expect_exit": 2, "expect_fail_label": None,
        "target": "preflight pin digest check",
    },
    {
        "id": "T2_dropped_subgroup_class",
        "old": "            found.add(closure((a, b)))",
        "new": "            _h = closure((a, b))\n"
               "            if len(_h) != 8:\n"
               "                found.add(_h)",
        "expect_exit": 1, "expect_fail_label": "D_SUBGROUP_LATTICE",
        "target": "the 30-subgroup / 11-class census and the class equation",
    },
    {
        "id": "T3_broken_class_equation",
        "old": "    return frozenset(g for g in GROUP\n"
               "                     if frozenset(mul(mul(g, x), INVERSE[g]) "
               "for x in h) == h)",
        "new": "    return frozenset(GROUP)",
        "expect_exit": 1, "expect_fail_label": "D_SUBGROUP_LATTICE",
        "target": "class_equation_holds_on_every_class",
    },
    {
        "id": "T4_broken_dimension_sum",
        "old": "    isotypes = []\n    for f in factors:",
        "new": "    isotypes = []\n    for f in factors[:-1]:",
        "expect_exit": 1, "expect_fail_label": "G_ISOTYPE_SIGNATURES",
        "target": "fine_decomposition_sums_to_the_space",
    },
    {
        "id": "T5_hardcoded_selector_row",
        "old": '        "SEL01_free_on_shell": lambda r: r["acts_freely_on_the_shell"],',
        "new": '        "SEL01_free_on_shell": lambda r: True,',
        "expect_exit": 1, "expect_fail_label": "L_RESTRICTION_GATE",
        "target": "byte-level reproduction of the pinned Cycle-886 receipt",
    },
    {
        "id": "T6_skipped_scope",
        "old": "    table = []\n    for name in menu_names:",
        "new": "    table = []\n    for name in menu_names[1:]:",
        "expect_exit": 1, "expect_fail_label": "N_SCOPE_INSENSITIVITY",
        "target": "table_is_complete over the whole menu",
    },
)


def teeth_certificate() -> dict:
    source = _text(AUDIT_INPUT_PATHS[0])
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / "scripts").mkdir()
        (base / "outputs").mkdir()
        (base / "docs").symlink_to(ROOT / "docs")
        subprocess.run(["git", "init", "-q"], cwd=str(base),
                       capture_output=True)
        for extra in (
            "scripts/frontier_cycle886_sl0_orbit_scope_2026_07_28.py",
            "scripts/frontier_cycle886_sl0_independent_check_2026_07_28.py",
            "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
            "scripts/frontier_cycle882_readout_identity_2026_07_28.py",
            "outputs/sl0_orbit_scope_cycle886_receipt_2026_07_28.json",
            "outputs/sl0_independent_check_cycle886_receipt_2026_07_28.json",
        ):
            shutil.copy2(ROOT / extra, base / extra)
        for mut in MUTATIONS:
            occurrences = source.count(mut["old"])
            patched = source.replace(mut["old"], mut["new"])
            path = base / "scripts" / f"mutant_{mut['id']}.py"
            path.write_text(patched, encoding="utf-8")
            proc = subprocess.run([sys.executable, str(path)], cwd=str(base),
                                  capture_output=True, text=True, timeout=600)
            failed = re.findall(r"^\[FAIL\] (\w+)", proc.stdout, re.M)
            label_hit = (mut["expect_fail_label"] is None
                         or mut["expect_fail_label"] in failed)
            bites = (occurrences == 1 and proc.returncode == mut["expect_exit"]
                     and proc.returncode != 0 and label_hit)
            rows.append({
                "id": mut["id"],
                "target_certificate_or_gate": mut["target"],
                "patch_sites_found": occurrences,
                "patch_applied_exactly_once": occurrences == 1,
                "expected_exit": mut["expect_exit"],
                "observed_exit": proc.returncode,
                "expected_failing_certificate": mut["expect_fail_label"],
                "observed_failing_certificates": failed,
                "stderr_head": proc.stderr.strip().splitlines()[:1],
                "bites": bites,
            })

    base_receipt = receipt()

    trap = json.loads(json.dumps(base_receipt))
    trap["S3_pricing_row"]["SL1_TRANSFER"]["verdict"] = "FORCED"
    trapped = sl1_transfer_certificate(trap)
    rows.append({
        "id": "T7_hardcoded_S3_transfer_row_on_the_checker",
        "target_certificate_or_gate": "G_SL1_TRANSFER_ATTACK / verdicts_agree",
        "method": "the primary's receipt is mutated in memory so the S3 "
                  "transfer row declares the decomposition FORCED -- the "
                  "reading that would make S3 a clean SL1 transfer. No "
                  "primary gate can see this, by design: the primary's gates "
                  "are outcome-neutral. Only the independent recomputation "
                  "catches it.",
        "checker_verdict_on_the_trapped_receipt": trapped["verdict"],
        "independent_verdict": trapped["independent_verdict"],
        "bites": trapped["verdict"] == "REFUTED"
                 and not trapped["verdicts_agree"],
    })

    trap2 = json.loads(json.dumps(base_receipt))
    trap2["scope_insensitivity"]["OVERALL_VERDICT"] = "SCOPE_INSENSITIVE"
    trapped2 = scope_insensitivity_certificate(trap2)
    rows.append({
        "id": "T8_leaked_scope_insensitivity_verdict_on_the_checker",
        "target_certificate_or_gate":
            "H_INDEPENDENT_SCOPE_INSENSITIVITY / overall_verdicts_agree",
        "method": "the primary's receipt is mutated in memory to declare the "
                  "downstream obligation SCOPE_INSENSITIVE -- the verdict that "
                  "would drop the menu price to zero. Again invisible to every "
                  "outcome-neutral gate and caught only by recomputation.",
        "checker_verdict_on_the_trapped_receipt": trapped2["verdict"],
        "independent_overall_verdict": trapped2["independent_overall_verdict"],
        "bites": trapped2["verdict"] == "REFUTED"
                 and not trapped2["overall_verdicts_agree"],
    })

    all_bite = all(x["bites"] for x in rows)
    return {
        "statement": "Eight deliberate mutations. Six patch the primary and "
                     "must flip a NAMED certificate or the preflight; two are "
                     "traps on this checker -- a hardcoded S3 transfer row and "
                     "a leaked scope-insensitivity verdict -- which no "
                     "outcome-neutral primary gate can catch and which must be "
                     "caught by independent recomputation.",
        "rows": rows,
        "teeth_that_bite": sum(1 for x in rows if x["bites"]),
        "all_teeth_bite": all_bite,
        "finding": (
            f"{sum(1 for x in rows if x['bites'])}/{len(rows)} teeth bite: "
            + ", ".join(f"{x['id'].split('_')[0]}="
                        f"{'BITE' if x['bites'] else 'MISS'}" for x in rows)),
        "pass": all_bite,
    }


# --------------------------------------------------------------------------
# certificate J: numbered refutation attempts
# --------------------------------------------------------------------------
def refutation_certificate(group_c, lat_c, iso_c, sel_c, reach_c, sl1_c,
                           ins_c, pin_c) -> dict:
    attempts = [
        {"n": 1, "attack": "the 24-element group is wrong",
         "method": "rebuilt from M M^T = I over 19683 integer matrices",
         "result": group_c["verdict"]},
        {"n": 2, "attack": "a subgroup or a whole conjugacy class was dropped "
                           "from the 30-member lattice",
         "method": "iterated extension <H, g>, cross-checked against closure "
                   "of every subset of size <= 3, the class equation and the "
                   "Sylow congruences",
         "result": lat_c["verdict"]},
        {"n": 3, "attack": "a fine decomposition is wrong -- in particular the "
                           "S3 multiplicity ledger",
         "method": "minimal cyclic submodules and orthogonal complements with "
                   "block characters; no enveloping algebra, no centre, no "
                   "minimal polynomial",
         "result": iso_c["verdict"]},
        {"n": 4, "attack": "a selector survivor set over the full lattice is "
                           "wrong, or the restriction to the 886 census does "
                           "not really reproduce 886",
         "method": "all sixteen recomputed over all thirty subgroups from the "
                   "checker's own signatures, then restricted and compared "
                   "against the pinned 886 receipt",
         "result": sel_c["verdict"]},
        {"n": 5, "attack": "an unreachability verdict is a window artifact",
         "method": "Smith-style diagonalization, self-tested on six lattices",
         "result": reach_c["verdict"]},
        {"n": 6, "attack": "the SL1-transfer claim is wrong: either a second "
                           "readout at S3 carries a DIFFERENT pair, or the S3 "
                           "decomposition is actually forced, or the C3/C4 "
                           "peer comparison breaks",
         "method": "every irreducible submodule of each degree enumerated and "
                   "characterised; the span of the top-degree submodules "
                   "compared against the isotypic component; C3 and C4 "
                   "multiplicity ledgers recomputed",
         "result": sl1_c["verdict"]},
        {"n": 7, "attack": "the scope-insensitivity verdict is wrong or was "
                           "leaked rather than computed",
         "method": "menu rule re-applied, Cycle 883's widening step "
                   "re-evaluated at every menu scope under both readings at "
                   "both scopes, verdicts re-derived",
         "result": ins_c["verdict"]},
        {"n": 8, "attack": "the 886/883 material the primary carried over as "
                           "pins was altered",
         "method": "byte comparison of every quoted sentence, fidelity grade, "
                   "grounding flag and survivor expression against the pinned "
                   "886 and 883 sources",
         "result": pin_c["verdict"]},
        {"n": 9, "attack": "the primary imported or executed a pinned artifact",
         "method": "meta-path firewall plus module-table inspection here, and "
                   "the primary's own firewall record",
         "result": "SURVIVES: no pinned module is loadable in this process "
                   "either"},
    ]
    landed = [a for a in attempts
              if a["result"].startswith(("REFUTED", "LANDS", "PARTIALLY"))]
    return {
        "statement": "Nine numbered refutation attempts against the block.",
        "attempts": attempts,
        "attempts_that_landed": [a["n"] for a in landed],
        "attempts_that_landed_count": len(landed),
        "no_computed_number_was_refuted": not landed,
        "finding": (
            f"{len(landed)} of {len(attempts)} attempts landed; every "
            f"recomputation of a certified quantity "
            f"{'reproduced' if not landed else 'did NOT reproduce'} the "
            f"primary."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificates L and M
# --------------------------------------------------------------------------
def findings_certificate(sel_c, sl1_c, ins_c, iso_c) -> dict:
    r = receipt()
    odd = sel_c["independent_survivors_per_selector"]["SEL12_odd_order"]
    findings = [
        {"id": "FIND-1", "severity": "adopted from the primary, confirmed",
         "text": "The odd-order clause -- Cycle 886's cheapest non-circular "
                 f"pin for C3 -- admits {odd} once the trivial subgroup enters "
                 "the census, because the filter Cycle 886 actually coded is "
                 "`order % 2 == 1` while its demand string said 'greater than "
                 "1'. The primary flags this; the checker confirms it "
                 "independently. Consequence: over the full lattice ZERO of "
                 "Cycle 886's six menu clauses is both non-circular and "
                 "isolating as coded.",
         "does_it_refute_a_number": False},
        {"id": "FIND-2", "severity": "sharpening",
         "text": "The primary reports S3's non-uniqueness by exhibiting "
                 "submodules. The checker shows the stronger statement: the "
                 "top-degree irreducible submodules of the S3 readout span "
                 "EXACTLY the 4-dimensional isotypic component and all carry "
                 "the SAME character. So the ambiguity is exactly a P^1 of "
                 "isomorphic copies -- the isotypic level is canonical, the "
                 "irreducible level is not, and no readout with a different "
                 "pair exists. That is a cleaner statement of the transfer "
                 "failure than 'the subspace is not unique'.",
         "does_it_refute_a_number": False},
        {"id": "FIND-3", "severity": "method note",
         "text": "A naive minimal-cyclic-submodule decomposition is NOT safe "
                 "on this lattice: at V_edge the first peeled block is "
                 "2-dimensional and reducible, and a checker that trusted it "
                 "would report fine dimensions [1,1,1,1,2] instead of the "
                 "correct six 1-dimensional blocks. The checker's own "
                 "pair-orbit gate caught this before any comparison was made. "
                 "Any future re-derivation of these signatures should carry "
                 "the same gate.",
         "does_it_refute_a_number": False},
        {"id": "FIND-4", "severity": "scope note",
         "text": "The MIXED scope-insensitivity verdict is driven by ONE "
                 "class: S3 defeats C882-T6 under the fine reading and fails "
                 "under the coarse reading. Every other menu member gives the "
                 "same answer under both readings at the orbit scope. So the "
                 "reading-dependence Cycle 886 discovered at C4 reappears at "
                 "S3 in a load-bearing place: it decides menu membership for "
                 "the downstream consumer, not just a signature entry.",
         "does_it_refute_a_number": False},
        {"id": "FIND-5", "severity": "open",
         "text": "Neither runner asks whether MULTIPLICITY-FREENESS of the "
                 "readout -- the property that separates C3 and C4 from S3 -- "
                 "is quotable from any axiom sentence. It is the smallest "
                 "clause that would restore SL1's uniqueness at a chosen "
                 "scope, and it is unpriced. Named here, not answered.",
         "does_it_refute_a_number": False},
    ]
    return {
        "statement": "What the primary should have done and did not, plus what "
                     "the checker learned that the primary could not.",
        "findings": findings,
        "findings_that_refute_a_number":
            [f["id"] for f in findings if f["does_it_refute_a_number"]],
        "finding": f"{len(findings)} findings, "
                   f"{sum(1 for f in findings if f['does_it_refute_a_number'])} "
                   f"of which refute a certified number.",
        "pass": True,
    }


def verdict_certificate(certs) -> dict:
    verdicts = {k: v.get("verdict") for k, v in certs.items()
                if isinstance(v, dict) and v.get("verdict")}
    refuted = [k for k, v in verdicts.items() if v == "REFUTED"]
    teeth = certs["K_TEETH"]
    return {
        "statement": "The independent check's overall verdict on the Cycle-888 "
                     "block.",
        "verdict_by_certificate": verdicts,
        "certificates_that_refute": refuted,
        "any_certified_number_refuted": bool(refuted),
        "teeth_that_bite": teeth["teeth_that_bite"],
        "all_teeth_bite": teeth["all_teeth_bite"],
        "overall": ("BLOCK SURVIVES INDEPENDENT CHECK" if not refuted
                    else "BLOCK REFUTED IN PART: " + ", ".join(refuted)),
        "what_survives": (
            "The 30-subgroup / 11-class lattice with the class equation and "
            "the Sylow congruences; every signature at both scopes under both "
            "readings; all sixteen selector survivor sets over the full "
            "lattice AND under the 886 restriction; the reachability survivors "
            "under all four rules; the S3 pricing row; the SL1-transfer "
            "verdict NUMERICALLY_TRANSFERS_BUT_THE_SUBSPACE_IS_NOT_FORCED; and "
            "the MIXED scope-insensitivity verdict with its working sets."),
        "finding": ("no certificate refutes a computed number; "
                    if not refuted else f"refuted: {refuted}; ")
                   + f"{teeth['teeth_that_bite']} teeth bite.",
        "pass": True,
    }


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------
def build() -> dict:
    pins = pins_certificate()
    group_c = group_certificate()
    lat_c = lattice_certificate()
    iso_c = isotype_certificate()
    sel_c = selector_certificate()
    reach_c = reachability_certificate()
    sl1_c = sl1_transfer_certificate()
    ins_c = scope_insensitivity_certificate()
    pin_c = upstream_pin_certificate()
    ref_c = refutation_certificate(group_c, lat_c, iso_c, sel_c, reach_c,
                                   sl1_c, ins_c, pin_c)
    teeth = teeth_certificate()
    certs = {
        "A_PINS": pins,
        "B_INDEPENDENT_GROUP": group_c,
        "C_INDEPENDENT_LATTICE": lat_c,
        "D_INDEPENDENT_ISOTYPE": iso_c,
        "E_INDEPENDENT_SELECTORS": sel_c,
        "F_INDEPENDENT_REACHABILITY": reach_c,
        "G_SL1_TRANSFER_ATTACK": sl1_c,
        "H_INDEPENDENT_SCOPE_INSENSITIVITY": ins_c,
        "I_UPSTREAM_PIN_FIDELITY": pin_c,
        "J_REFUTATION_ATTEMPTS": ref_c,
        "K_TEETH": teeth,
    }
    certs["L_FINDINGS"] = findings_certificate(sel_c, sl1_c, ins_c, iso_c)
    certs["M_VERDICT"] = verdict_certificate(certs)
    return certs


def preflight() -> int:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).exists()]
    if missing:
        sys.stderr.write("PREFLIGHT HARD FAIL: missing pinned artifact(s): "
                         + ", ".join(missing) + "\n")
        return 2
    return 0


def render(certs) -> str:
    out = ["CYCLE 888 -- INDEPENDENT CHECK OF THE S3 SCOPE PRICING", ""]
    for label in LABELS:
        c = certs[label]
        out.append(f"[{'PASS' if c['pass'] else 'FAIL'}] {label}"
                   + (f"  verdict={c['verdict']}" if c.get("verdict") else ""))
        if c.get("finding"):
            out.append(f"    finding: {c['finding']}")
        out.append("")
    out.append(json.dumps(certs, indent=1, sort_keys=True, default=str))
    return "\n".join(out) + "\n"


def run() -> int:
    code = preflight()
    if code:
        return code
    started = monotonic()
    certs = build()
    text = render(certs)
    stdout_bytes = len(text.encode("utf-8"))
    elapsed = monotonic() - started

    receipt_payload = {
        "cycle": 888,
        "role": "independent adversarial check",
        "checked_runner": AUDIT_INPUT_PATHS[0],
        "checked_runner_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]],
        "verdict_by_certificate":
            certs["M_VERDICT"]["verdict_by_certificate"],
        "overall": certs["M_VERDICT"]["overall"],
        "any_certified_number_refuted":
            certs["M_VERDICT"]["any_certified_number_refuted"],
        "independent_lattice": {
            "subgroups": certs["C_INDEPENDENT_LATTICE"]["subgroups_found"],
            "conjugacy_classes":
                certs["C_INDEPENDENT_LATTICE"]["conjugacy_classes"],
            "by_derived_name":
                certs["C_INDEPENDENT_LATTICE"]["subgroups_by_derived_name"],
            "class_equation_rows":
                certs["C_INDEPENDENT_LATTICE"]["class_equation_rows"],
        },
        "independent_signatures": [
            {"name": r["name"], "shell": r["independent_shell"],
             "orbit": r["independent_orbit"],
             "shell_isotypes": r["independent_shell_isotypes"],
             "orbit_isotypes": r["independent_orbit_isotypes"],
             "agrees_with_the_primary": r["agrees_with_the_primary"]}
            for r in certs["D_INDEPENDENT_ISOTYPE"]["rows"]],
        "independent_survivors_per_selector":
            certs["E_INDEPENDENT_SELECTORS"]["independent_survivors_per_selector"],
        "selector_comparison": certs["E_INDEPENDENT_SELECTORS"]["rows"],
        "restriction_rows": certs["E_INDEPENDENT_SELECTORS"]["restriction_rows"],
        "independent_reachability":
            certs["F_INDEPENDENT_REACHABILITY"]["independent_survivors_by_rule"],
        "sl1_transfer_attack": {
            k: v for k, v in certs["G_SL1_TRANSFER_ATTACK"].items()
            if k not in ("statement",)},
        "scope_insensitivity": {
            "independent_menu":
                certs["H_INDEPENDENT_SCOPE_INSENSITIVITY"]["independent_menu"],
            "per_reading_comparison":
                certs["H_INDEPENDENT_SCOPE_INSENSITIVITY"]["per_reading_comparison"],
            "independent_overall_verdict":
                certs["H_INDEPENDENT_SCOPE_INSENSITIVITY"]["independent_overall_verdict"],
            "primary_overall_verdict":
                certs["H_INDEPENDENT_SCOPE_INSENSITIVITY"]["primary_overall_verdict"],
        },
        "upstream_pin_fidelity": {
            "quoted_sentences_are_verbatim_886_material":
                certs["I_UPSTREAM_PIN_FIDELITY"]["quoted_sentences_are_verbatim_886_material"],
            "fidelity_grades_carried_unchanged":
                certs["I_UPSTREAM_PIN_FIDELITY"]["fidelity_grades_carried_unchanged"],
            "survivor_expressions_are_verbatim_886_source":
                certs["I_UPSTREAM_PIN_FIDELITY"]["survivor_expressions_are_verbatim_886_source"],
        },
        "refutation_attempts": certs["J_REFUTATION_ATTEMPTS"]["attempts"],
        "teeth": certs["K_TEETH"]["rows"],
        "teeth_that_bite": certs["K_TEETH"]["teeth_that_bite"],
        "findings": certs["L_FINDINGS"]["findings"],
        "controls": {
            "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                       if n in sys.modules],
            "firewall_hits": list(FIREWALL.hits),
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
            "stdout_bytes": stdout_bytes,
            "stdout_under_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
            "exit_is_independent_of_claim_survival": True,
        },
        "source_pins": [{"path": r["path"], "sha256": r["sha256"],
                         "git_blob": r["git_blob"]}
                        for r in certs["A_PINS"]["rows"]],
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt_payload, indent=2, sort_keys=True,
                                 default=str) + "\n", encoding="utf-8")

    sys.stdout.write(text)
    sys.stdout.write(
        f"\ncontrols: runtime={round(elapsed, 3)}s stdout={stdout_bytes}B "
        f"teeth={certs['K_TEETH']['teeth_that_bite']}/"
        f"{len(certs['K_TEETH']['rows'])} "
        f"overall={certs['M_VERDICT']['overall']}\n")
    # Exit status reports EXECUTION health, never claim survival.
    healthy = (certs["A_PINS"]["pass"] and certs["K_TEETH"]["all_teeth_bite"]
               and stdout_bytes < STDOUT_LIMIT_BYTES
               and elapsed < AUDIT_TIMEOUT_SEC
               and not [n for n in BLOCKLISTED_MODULES if n in sys.modules])
    return 0 if healthy else 1


if __name__ == "__main__":
    raise SystemExit(run())
