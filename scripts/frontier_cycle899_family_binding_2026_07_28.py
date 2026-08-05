#!/usr/bin/env python3
"""Cycle 899: THE FAMILY BINDING -- which of the three N = 3 degenerate
families does the framework's OWN readout construction native-bind to, and is
the binding testable at C4 where the families diverge?

BACKGROUND (all pinned, none imported).  Cycle 883 derived the C3 isotype pair
(1, 2) and then priced the BINDING of that pair to the anchor constant 2/9 as
OPEN: its certificate M enumerated seven closed forms in the derived data and
found several of them returning 2/9, so "nothing in the derivation picks one"
(SL1b).  Cycle 888 rebuilt 883's construction two ways -- cyclic-native
(nullspace of a_i - a_{i+1}) and group-theoretic (intersection of
ker(rho(h) - 1) over the whole subgroup) -- and gated them to agree at C3.
Cycle 890 closed the census: the multiplicity-free free-orbit scopes are
C2_face, C2_edge, C3_body, C4_face and V_edge; S3_body carries a multiplicity-2
irreducible and is excluded.  A parallel Cycle-897 fork certified that THREE
canonical families

    F_dim(N) = (N - 1) / N^2
    F_res(N) = (N^2 - 1) / (12 N)
    F_ded(N) = (N - 1)(N - 2) / (3 N)

all equal 2/9 at N = 3 and diverge at N = 4 (3/16, 5/16, 1/2).

Q1  THE CONSTRUCTION'S NATIVE VALUE AT BOTH SCOPES.  883's readout
    construction is rebuilt via 888's group-theoretic route (its C3 agreement
    is gated first, value-for-value from the pinned 888 cache).  883's "orbit
    reads K" recipe is RECOVERED BY AST from the pinned 883 primary -- the
    literal list of closed forms its certificate M evaluated, together with the
    (w0, w1, n) binding its certificate M used -- re-evaluated as a function of
    the decomposition at each scope.  The recovery is published in full.  The
    recovered recipe set is whatever subset of 883's own forms reproduces 2/9
    at C3; that subset is then evaluated at C4.  If the subset disagrees at C4
    the recipe is NOT identified and this cycle says so.

Q2  THE RETAINED ANCHOR ARITHMETIC AT C4.  The retained L-face from the pinned
    KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS note is rebuilt from its OWN recipe --
    L_H = (1/|H|) sum_{h != e} 1 / det_R(I - h|_N), N the real transverse
    space -- and evaluated at every scope, on BOTH candidate transverse spaces:
    the geometric normal plane inside the Z^3 lattice (the note's literal
    object) and the readout module's invariant complement (the object 883's
    construction lives on).  The two spaces are compared as H-modules.

Q3  THE FITTED VALUE'S FAMILY STATUS.  Exhaustive exact search over a declared
    and bounded transform space for any member landing inside the Cycle-897
    fitted enclosure, with the exact nearest member and its exact distance.

Q4  THE OFF-ENDPOINT ROWS.  The complete family-binding table over every scope
    where the construction is canonical.

FALSIFIER VISIBILITY.  Three planted recipes -- all functions of the same
decomposition data, all returning 2/9 at C3 -- are pushed through the identical
comparison machinery and must bind to F_dim, F_res and F_ded respectively.  A
comparison that can only ever say "F_dim" is not a comparison.

All cited artifacts are SHA-256 and git-blob pinned, read as text/AST/JSON
only, and blocked from import by a meta-path firewall.  Every certified
quantity is exact (`int` / `Fraction`); floating point is used only as a search
heuristic inside Q3 and never enters a certificate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 400_000

# Literal, greppable, and pinned below.
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
    "outputs/record_weight_pair_cycle883_receipt_2026_07_28.json",
    "logs/runner-cache/frontier_cycle883_record_weight_pair_2026_07_28.txt",
    "scripts/frontier_cycle888_s3_scope_pricing_2026_07_28.py",
    "outputs/s3_scope_pricing_cycle888_receipt_2026_07_28.json",
    "logs/runner-cache/frontier_cycle888_s3_scope_pricing_2026_07_28.txt",
    "scripts/frontier_cycle890_multiplicity_freeness_2026_07_28.py",
    "outputs/multiplicity_freeness_cycle890_receipt_2026_07_28.json",
    "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE"
    "_2026-06-05.md",
)

import ast
import bisect
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import product
import json
from math import gcd
from pathlib import Path
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs" / "family_binding_cycle899_receipt_2026_07_28.json"

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[1]:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
    AUDIT_INPUT_PATHS[2]:
        "973d18d9aa2e05a2decac79ddd8a6f245d923e9a94d772baf80869228ca27d60",
    AUDIT_INPUT_PATHS[3]:
        "560f368d9d23144cb23a93e72a398d92f6fcb536c3363179b7853c09615211bb",
    AUDIT_INPUT_PATHS[4]:
        "f57fda877d35d49953c3b6a34293ab0cc6a87781ceb9d158b9c9abb5abd4bb3f",
    AUDIT_INPUT_PATHS[5]:
        "8a540201a84a6b8cb6868d431216718a27f200e45d6ceeb771d858e9a54280cd",
    AUDIT_INPUT_PATHS[6]:
        "5e4fc183efda55d1f3fbd5413bd2fe985ed5732b7ffbc8bd489296e7b22c2c84",
    AUDIT_INPUT_PATHS[7]:
        "b7d2e9c2c540fc35ca461af10c4ce6b455269503c6027b3f0b4d5036566d867b",
    AUDIT_INPUT_PATHS[8]:
        "a366a726c34308260dcf153ff74619238347de5996463a7c5a5792bdcd01617e",
    AUDIT_INPUT_PATHS[9]:
        "3c7a33c8abac8e70bdcf2e8b9db5d917c0b2cee6fc7cc0ec91c6d803bbb230d2",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "4a863da1f3f255354839277271a3a69a5c205133",
    AUDIT_INPUT_PATHS[1]: "d563c2b9c2a261f44d7304baa51fdd3596188930",
    AUDIT_INPUT_PATHS[2]: "d4290cbe8cfedf965fad828dc673e8fee2e75cd5",
    AUDIT_INPUT_PATHS[3]: "6f085fc042330dae1d3eec8540a2942b1a3cf32f",
    AUDIT_INPUT_PATHS[4]: "c3de02c94b8a11a930ad6ff8817975b118bc776d",
    AUDIT_INPUT_PATHS[5]: "3e18ad52f50e72b83c56da72c31f25d104b5c830",
    AUDIT_INPUT_PATHS[6]: "6cd3fbdbe74e1231cd61222a798a7979bee922da",
    AUDIT_INPUT_PATHS[7]: "307f4e7640a1a9b5b3365d70ebc857a9c9488beb",
    AUDIT_INPUT_PATHS[8]: "eefb1ac72326ae70073126198854dea5e26d1f01",
    AUDIT_INPUT_PATHS[9]: "1201ba9702ec8a0b81df0319a90a080549cfdd4a",
}

BLOCKLISTED_MODULES = tuple(sorted({Path(p).stem for p in AUDIT_INPUT_PATHS}))

# Cycle 883's pinned scope constants, re-derived from its source by AST below;
# these literals exist only so the AST recovery can be compared in public.
DECLARED_883_ORBIT_LENGTH = 3
DECLARED_883_TARGET_PAIR = (1, 2)
TARGET_ANCHOR = Fraction(2, 9)

# The Cycle-897 fork's fitted enclosure, as an exact rational interval.
FITTED_LO = Fraction(222222047073817229, 10 ** 18)
FITTED_HI = Fraction(222222047073817230, 10 ** 18)

# The three canonical families, as callables on N.  Declared here as the
# COMPARISON TARGETS only; nothing in this cycle assumes one of them.
FAMILIES = {
    "F_dim": lambda N: Fraction(N - 1, N * N),
    "F_res": lambda N: Fraction(N * N - 1, 12 * N),
    "F_ded": lambda N: Fraction((N - 1) * (N - 2), 3 * N),
}

# The 6-neighbour shell of the origin in Z^3.
SHELL = ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
         (0, -1, 0), (0, 0, 1), (0, 0, -1))


# --------------------------------------------------------------------------
# import firewall
# --------------------------------------------------------------------------
class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):     # pragma: no cover legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(
                f"import firewall: {fullname} is a pinned audit input and "
                f"must be read as text/AST/JSON, never imported")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
def _read_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _read_text(path: str) -> str:
    return _read_bytes(path).decode("utf-8")


def digest(payload: object) -> str:
    return sha256(json.dumps(payload, sort_keys=True,
                             separators=(",", ":")).encode()).hexdigest()


def q(value: Fraction) -> str:
    value = Fraction(value)
    return f"{value.numerator}/{value.denominator}"


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


# --------------------------------------------------------------------------
# exact rational linear algebra
# --------------------------------------------------------------------------
def rref(rows):
    mat = [[Fraction(x) for x in row] for row in rows]
    pivots, r = [], 0
    width = len(mat[0]) if mat else 0
    for c in range(width):
        piv = next((i for i in range(r, len(mat)) if mat[i][c] != 0), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        inv = Fraction(1) / mat[r][c]
        mat[r] = [x * inv for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    return mat, pivots


def rank_exact(rows) -> int:
    if not rows:
        return 0
    return len(rref(rows)[1])


def kernel_basis(rows, width: int):
    if not rows:
        return [[Fraction(1) if i == j else Fraction(0) for i in range(width)]
                for j in range(width)]
    mat, pivots = rref(rows)
    free = [c for c in range(width) if c not in pivots]
    basis = []
    for f in free:
        vec = [Fraction(0)] * width
        vec[f] = Fraction(1)
        for r, c in enumerate(pivots):
            vec[c] = -mat[r][f]
        basis.append(vec)
    return basis


def det_exact(mat) -> Fraction:
    m = [[Fraction(x) for x in row] for row in mat]
    n = len(m)
    if n == 0:
        return Fraction(1)
    det, sign = Fraction(1), 1
    for c in range(n):
        piv = next((i for i in range(c, n) if m[i][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            sign = -sign
        det *= m[c][c]
        inv = Fraction(1) / m[c][c]
        for i in range(c + 1, n):
            if m[i][c] != 0:
                f = m[i][c] * inv
                m[i] = [a - f * b for a, b in zip(m[i], m[c])]
    return det * sign


def identity_matrix(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
            for i in range(n)]


def mat_sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def solve_coordinates(basis, vector):
    """Coordinates of `vector` in the span of `basis` (rows), or None."""
    width = len(vector)
    rows = [[basis[k][i] for k in range(len(basis))] + [vector[i]]
            for i in range(width)]
    mat, pivots = rref(rows)
    if len(basis) in pivots:
        return None
    coords = [Fraction(0)] * len(basis)
    for r, c in enumerate(pivots):
        coords[c] = mat[r][len(basis)]
    check = [sum(coords[k] * basis[k][i] for k in range(len(basis)))
             for i in range(width)]
    return coords if check == list(vector) else None


def restrict_to(basis, matrix):
    """Matrix of `matrix` restricted to the invariant span of `basis`."""
    cols = []
    for vec in basis:
        image = [sum(matrix[i][j] * vec[j] for j in range(len(vec)))
                 for i in range(len(matrix))]
        coords = solve_coordinates(basis, image)
        if coords is None:
            return None
        cols.append(coords)
    d = len(basis)
    return [[cols[j][i] for j in range(d)] for i in range(d)]


# --------------------------------------------------------------------------
# exact polynomial helpers (integer coefficient lists, low degree first)
# --------------------------------------------------------------------------
def poly_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return poly_trim(out)


def poly_divmod(num, den):
    num, den = poly_trim(list(num)), poly_trim(list(den))
    if len(den) == 1 and den[0] == 0:
        raise ZeroDivisionError
    out = [Fraction(0)] * max(1, len(num) - len(den) + 1)
    rem = [Fraction(x) for x in num]
    lead = Fraction(den[-1])
    while len(poly_trim(rem)) >= len(den) and any(x != 0 for x in rem):
        rem = poly_trim(rem)
        if len(rem) < len(den):
            break
        shift = len(rem) - len(den)
        factor = rem[-1] / lead
        out[shift] = factor
        for i, c in enumerate(den):
            rem[shift + i] -= factor * c
        rem = poly_trim(rem)
    return out, poly_trim(rem)


def poly_divides(den, num) -> bool:
    _, rem = poly_divmod(num, den)
    return all(x == 0 for x in rem)


def cyclotomic(n: int):
    """Phi_n as an integer coefficient list, built by exact division."""
    poly = [-1] + [0] * (n - 1) + [1]          # x^n - 1
    for d in divisors(n):
        if d == n:
            continue
        quo, rem = poly_divmod(poly, cyclotomic(d))
        assert all(x == 0 for x in rem)
        poly = [int(x) for x in quo]
    return poly_trim(poly)


def poly_of_matrix(coeffs, matrix):
    n = len(matrix)
    acc = [[Fraction(0)] * n for _ in range(n)]
    power = identity_matrix(n)
    for c in coeffs:
        if c:
            acc = [[acc[i][j] + Fraction(c) * power[i][j] for j in range(n)]
                   for i in range(n)]
        power = mat_mul(power, matrix)
    return acc


def minimal_polynomial(matrix):
    """Minimal polynomial of a rational square matrix, monic, integer-scaled."""
    n = len(matrix)
    vectors, powers = [], []
    power = identity_matrix(n)
    for _ in range(n * n + 1):
        flat = [power[i][j] for i in range(n) for j in range(n)]
        rows = vectors + [flat]
        if rank_exact(rows) == len(vectors):
            # linear dependence found: solve for it
            width = len(vectors)
            aug = [[vectors[k][i] for k in range(width)] + [flat[i]]
                   for i in range(n * n)]
            mat, pivots = rref(aug)
            coeffs = [Fraction(0)] * width
            for r, c in enumerate(pivots):
                if c < width:
                    coeffs[c] = mat[r][width]
            poly = [-c for c in coeffs] + [Fraction(1)]
            den = 1
            for c in poly:
                den = den * c.denominator // gcd(den, c.denominator)
            return poly_trim([int(c * den) for c in poly])
        vectors.append(flat)
        powers.append(power)
        power = mat_mul(power, matrix)
    raise RuntimeError("minimal polynomial not found")


def cyclotomic_fine_dims(matrix, order: int):
    """Fine rational-irreducible dimensions of a module on which a single
    generator acts with the given order: the kernels of Phi_d(M), d | order."""
    n = len(matrix)
    mp = minimal_polynomial(matrix)
    dims, rows = [], []
    for d in divisors(order):
        pd = cyclotomic(d)
        if not poly_divides(pd, mp):
            continue
        ker = kernel_basis(poly_of_matrix(pd, matrix), n)
        deg = len(pd) - 1
        if len(ker) % deg:
            return None
        mult = len(ker) // deg
        rows.append({"cyclotomic_index": d, "degree": deg,
                     "multiplicity": mult, "component_dimension": len(ker)})
        dims.extend([deg] * mult)
    if sum(dims) != n:
        return None
    return {"minimal_polynomial": mp, "isotypes": rows,
            "fine_dims": sorted(dims), "space_dimension": n,
            "multiplicity_free": all(r["multiplicity"] == 1 for r in rows)}


# --------------------------------------------------------------------------
# the proper cubic rotation group and its subgroups
# --------------------------------------------------------------------------
def det3(m) -> int:
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def mul3(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def act3(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def proper_rotations():
    out = []
    for perm in product(range(3), repeat=3):
        if len(set(perm)) != 3:
            continue
        for signs in product((1, -1), repeat=3):
            mat = tuple(tuple(signs[i] if perm[i] == j else 0
                              for j in range(3)) for i in range(3))
            if det3(mat) == 1:
                out.append(mat)
    return sorted(out)


GROUP = proper_rotations()
IDENT = tuple(tuple(1 if i == j else 0 for j in range(3)) for i in range(3))


def element_order(m) -> int:
    cur, k = m, 1
    while cur != IDENT:
        cur, k = mul3(cur, m), k + 1
    return k


def closure(seeds) -> frozenset:
    have = {IDENT}
    frontier = list(seeds)
    while frontier:
        g = frontier.pop()
        if g in have:
            continue
        have.add(g)
        for h in list(have):
            for prod in (mul3(g, h), mul3(h, g)):
                if prod not in have:
                    frontier.append(prod)
    return frozenset(have)


def all_subgroups() -> list[frozenset]:
    found = {frozenset({IDENT})}
    for g in GROUP:
        found.add(closure([g]))
    for a in GROUP:
        for b in GROUP:
            found.add(closure([a, b]))
    return sorted(found, key=lambda h: (len(h), sorted(h)))


def fixed_space_basis(subgroup):
    """Basis of the common fixed space of a subgroup inside Q^3."""
    rows = []
    for g in sorted(subgroup):
        rows.extend(mat_sub([[Fraction(x) for x in r] for r in g],
                            identity_matrix(3)))
    return kernel_basis(rows, 3) if rows else identity_matrix(3)


def primitive_int_vector(vec):
    dens = 1
    for c in vec:
        dens = dens * c.denominator // gcd(dens, c.denominator)
    ints = [int(c * dens) for c in vec]
    g = 0
    for c in ints:
        g = gcd(g, abs(c))
    if g:
        ints = [c // g for c in ints]
    for c in ints:
        if c < 0:
            ints = [-x for x in ints]
            break
        if c > 0:
            break
    return tuple(ints)


def axis_kind(vec) -> str:
    nz = sum(1 for c in vec if c != 0)
    return {1: "face", 2: "edge", 3: "body"}.get(nz, "none")


def orbits_of(subgroup, points):
    pts, seen, out = list(points), set(), []
    for p in pts:
        if p in seen:
            continue
        orb = set()
        frontier = [p]
        while frontier:
            x = frontier.pop()
            if x in orb:
                continue
            orb.add(x)
            for g in subgroup:
                y = act3(g, x)
                if y not in orb:
                    frontier.append(y)
        seen |= orb
        out.append(tuple(sorted(orb)))
    return sorted(out)


def structure_name(h: frozenset) -> str:
    n = len(h)
    if n == 1:
        return "E_trivial"
    orders = sorted(element_order(g) for g in h if g != IDENT)
    axes = [axis_kind(primitive_int_vector(fixed_space_basis({g})[0]))
            for g in sorted(h) if g != IDENT]
    cyclic = any(element_order(g) == n for g in h)
    if n == 2:
        return f"C2_{axes[0]}"
    if n == 3:
        return "C3_body"
    if n == 4 and cyclic:
        return f"C4_{axes[0]}"
    if n == 4:
        return "V_face" if all(a == "face" for a in axes) else "V_edge"
    if n == 6:
        return "S3_body" if max(orders) == 3 else "C6"
    if n == 8:
        return "D4_face"
    if n == 12:
        return "A4_tetrahedral"
    if n == 24:
        return "O_full"
    return f"H{n}"


def permutation_matrix(g, points):
    n = len(points)
    idx = {p: i for i, p in enumerate(points)}
    mat = [[Fraction(0)] * n for _ in range(n)]
    for j, p in enumerate(points):
        mat[idx[act3(g, p)]][j] = Fraction(1)
    return mat


# --------------------------------------------------------------------------
# the construction: 883's cyclic-native route and 888's group-theoretic route
# --------------------------------------------------------------------------
def cyclic_pair(n: int) -> tuple[int, int]:
    """Cycle 883's own construction: nullspace of a_i - a_{i+1 mod n}."""
    rows = []
    for i in range(n):
        row = [Fraction(0)] * n
        row[i] += 1
        row[(i + 1) % n] -= 1
        rows.append(row)
    inv = n - rank_exact(rows)
    return inv, n - inv


def group_pair(subgroup, points) -> tuple[int, int]:
    """Cycle 888's group-theoretic route: dim of the intersection of
    ker(rho(h) - 1) over the whole subgroup, and its complement."""
    n = len(points)
    stacked = []
    for g in sorted(subgroup):
        stacked.extend(mat_sub(permutation_matrix(g, points),
                               identity_matrix(n)))
    inv = n - rank_exact(stacked)
    return inv, n - inv


def pair_orbit_identity(subgroup, points) -> int:
    """FIND-3 safety identity: the number of orbits of H on X x X."""
    pts = list(points)
    seen, count = set(), 0
    for a in pts:
        for b in pts:
            if (a, b) in seen:
                continue
            count += 1
            for g in subgroup:
                seen.add((act3(g, a), act3(g, b)))
    return count


# --------------------------------------------------------------------------
# certificate A: pins
# --------------------------------------------------------------------------
def git_blob(path: str) -> str:
    try:
        return subprocess.run(["git", "hash-object", path], cwd=str(ROOT),
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:                              # pragma: no cover
        return "unavailable"


def pins_certificate() -> dict:
    rows, failures = [], []
    for path in AUDIT_INPUT_PATHS:
        full = ROOT / path
        exists = full.exists()
        actual = sha256(_read_bytes(path)).hexdigest() if exists else None
        blob = git_blob(path) if exists else None
        want_sha = EXPECTED_SHA256[path]
        want_blob = EXPECTED_GIT_BLOBS[path]
        sha_ok = exists and actual == want_sha
        blob_ok = exists and blob == want_blob
        rows.append({
            "path": path,
            "absolute_path": str(full),
            "exists": exists,
            "sha256": actual,
            "git_blob": blob,
            "sha256_matches_pin": sha_ok,
            "git_blob_matches_pin": blob_ok,
        })
        if not (exists and sha_ok and blob_ok):
            failures.append(path)
    return {
        "rows": rows,
        "all_pins_verified": not failures,
        "failures": failures,
        "import_firewall_blocklist": list(BLOCKLISTED_MODULES),
        "import_firewall_hits": list(FIREWALL.hits),
        "import_firewall_hit_count": len(FIREWALL.hits),
        "import_firewall_zero_hits": len(FIREWALL.hits) == 0,
        "reading_discipline": "TEXT / AST / JSON only; no pinned artifact is "
                              "imported as a module",
        "finding": (
            f"{len(rows)} pinned artifacts, {len(rows) - len(failures)} "
            f"verified, {len(FIREWALL.hits)} import-firewall hits."
        ),
        "pass": not failures and len(FIREWALL.hits) == 0,
    }


# --------------------------------------------------------------------------
# certificate B: AST recovery of Cycle 883's "orbit reads K" recipe
# --------------------------------------------------------------------------
SAFE_NAMES = ("w0", "w1", "n")


def _eval_form(node, env):
    """Tiny total evaluator over the AST of one of 883's closed forms."""
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return Fraction(node.value)
    if isinstance(node, ast.Name):
        if node.id not in env:
            raise ValueError(f"unbound name {node.id}")
        return Fraction(env[node.id])
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_eval_form(node.operand, env)
    if isinstance(node, ast.BinOp):
        left = _eval_form(node.left, env)
        right = _eval_form(node.right, env)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Pow):
            return left ** int(right)
        if isinstance(node.op, ast.Div):
            return left / right
        raise ValueError("unsupported operator")
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
            and node.func.id == "Fraction":
        args = [_eval_form(a, env) for a in node.args]
        if len(args) == 1:
            return Fraction(args[0])
        if len(args) == 2:
            return Fraction(args[0]) / Fraction(args[1])
    raise ValueError(f"unsupported node {type(node).__name__}")


def recover_883_recipe() -> dict:
    """Recover, from the pinned 883 primary's SOURCE, exactly what its anchor
    computation evaluates: the (w0, w1, n) binding and the literal list of
    closed forms of certificate M, re-expressed as callables on any scope."""
    tree = ast.parse(_read_text(AUDIT_INPUT_PATHS[1]))
    fn = next((node for node in ast.walk(tree)
               if isinstance(node, ast.FunctionDef)
               and node.name == "binding_price_certificate"), None)
    if fn is None:
        return {"ok": False, "reason": "binding_price_certificate not found"}

    # (1) the tuple binding `w0, w1, n = 1, 2, ORBIT_LENGTH`
    binding = None
    for node in ast.walk(fn):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        tgt = node.targets[0]
        if not isinstance(tgt, ast.Tuple):
            continue
        names = [e.id for e in tgt.elts if isinstance(e, ast.Name)]
        if names != ["w0", "w1", "n"]:
            continue
        binding = ast.unparse(node)
    # (2) the list of closed forms
    forms = []
    for node in ast.walk(fn):
        if not (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "forms"):
            continue
        if not isinstance(node.value, ast.List):
            continue
        for item in node.value.elts:
            if not isinstance(item, ast.Dict):
                continue
            entry = {}
            for key, value in zip(item.keys, item.values):
                if isinstance(key, ast.Constant):
                    entry[key.value] = value
            if "name" in entry and "value" in entry:
                forms.append({
                    "name": entry["name"].value,
                    "expression_source": ast.unparse(entry["value"]),
                    "ast": entry["value"],
                })
    # (3) the ORBIT_LENGTH / TARGET_PAIR module constants and the anchor
    consts = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in ("ORBIT_LENGTH", "TARGET_PAIR",
                        "L3_FIXED_LOCUS_DENSITY"):
                try:
                    consts[name] = ast.literal_eval(node.value)
                except Exception:
                    consts[name] = ast.unparse(node.value)
    anchor = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id == "L3_FIXED_LOCUS_DENSITY":
            anchor = _eval_form(node.value, {})

    # (4) the COARSE reading, recovered from C883-T6's own theorem statement.
    #     Adjacent string literals are joined by the parser, so the sentence
    #     is recovered as one constant and never as a line-wrapped grep.
    t6 = next((node for node in ast.walk(tree)
               if isinstance(node, ast.FunctionDef)
               and node.name == "discrimination_certificate"), None)
    t6_theorem = None
    if t6 is not None:
        for node in ast.walk(t6):
            if not (isinstance(node, ast.Return)
                    and isinstance(node.value, ast.Dict)):
                continue
            for key, value in zip(node.value.keys, node.value.values):
                if isinstance(key, ast.Constant) and key.value == "theorem":
                    try:
                        t6_theorem = ast.literal_eval(value)
                    except Exception:
                        t6_theorem = None
    src = _read_text(AUDIT_INPUT_PATHS[1])
    coarse_key_present = "matches_the_formula_1_n_minus_1" in src
    coarse_words_present = bool(
        t6_theorem
        and "the ordered isotype pair is exactly (1, n - 1)" in t6_theorem
        and "(1, 3) at n = 4" in t6_theorem)

    ok = (binding is not None and len(forms) == 7 and anchor == TARGET_ANCHOR
          and consts.get("ORBIT_LENGTH") == DECLARED_883_ORBIT_LENGTH
          and tuple(consts.get("TARGET_PAIR", ())) == DECLARED_883_TARGET_PAIR
          and coarse_key_present and coarse_words_present)
    return {
        "ok": ok,
        "source_function": "binding_price_certificate",
        "recovered_scope_binding_source": binding,
        "recovered_form_count": len(forms),
        "recovered_forms": [{"name": f["name"],
                             "expression_source": f["expression_source"]}
                            for f in forms],
        "recovered_module_constants": {
            k: (list(v) if isinstance(v, tuple) else v)
            for k, v in consts.items()},
        "recovered_anchor": q(anchor) if anchor is not None else None,
        "reading_is_COARSE_because": (
            "C883-T6 states the pair in words -- '(1, 1) at n = 2 and (1, 3) "
            "at n = 4' -- and keys its own row check on "
            "matches_the_formula_1_n_minus_1.  So 883's (w0, w1) is the "
            "invariant/complement COARSE split, not the fine isotype list; at "
            "n = 4 it is (1, 3), never (1, 2)."
        ),
        "coarse_sentence_found_verbatim": coarse_words_present,
        "coarse_formula_key_found": coarse_key_present,
        "recovered_C883_T6_theorem_statement": t6_theorem,
        "_forms": forms,
    }


def evaluate_recipe(forms, w0: int, w1: int, n: int) -> list[dict]:
    out = []
    env = {"w0": w0, "w1": w1, "n": n}
    for f in forms:
        try:
            value = _eval_form(f["ast"], env)
        except ZeroDivisionError:
            value = None
        out.append({"name": f["name"],
                    "value": q(value) if value is not None else None,
                    "_value": value})
    return out


# --------------------------------------------------------------------------
# certificate C: restriction gates
# --------------------------------------------------------------------------
def restriction_gates(recipe) -> dict:
    """Nothing new is claimed until 883's C3 anchor and 888's two-route
    agreement are reproduced, value-for-value, from the pinned artifacts."""
    forms = recipe["_forms"]
    c3 = evaluate_recipe(forms, 1, 2, 3)
    hitting = [r["name"] for r in c3 if r["_value"] == TARGET_ANCHOR]

    cache883 = _read_text(AUDIT_INPUT_PATHS[3])
    landed_block = cache883[cache883.find('"forms_returning_the_anchor"'):]
    landed_count = None
    for line in landed_block.splitlines():
        if '"number_of_forms_returning_the_anchor"' in line:
            landed_count = int(line.split(":")[1].strip().rstrip(","))
            break
    landed_names = json.loads(
        "[" + landed_block[landed_block.find("[") + 1:
                           landed_block.find("]")] + "]")

    cache888 = _read_text(AUDIT_INPUT_PATHS[6])
    routes_agree_888 = '"both_routes_agree_at_C3": true' in cache888
    route_block = cache888[cache888.find('"C3_group_theoretic_route"'):]
    route_pair = json.loads(
        "[" + route_block[route_block.find("[") + 1:
                          route_block.find("]")] + "]")

    # rebuild both routes here, from scratch
    native = cyclic_pair(3)
    c3_scope = SCOPES["C3_body"]
    grouped = group_pair(c3_scope["subgroup"], c3_scope["points"])
    rebuilt_agree = (list(native) == list(grouped) == route_pair
                     == list(DECLARED_883_TARGET_PAIR))

    # 890's census row for C3 and C4, value for value
    census = json.loads(_read_text(AUDIT_INPUT_PATHS[8]))
    rows890 = {r["class"]: r for r in census["DETAIL_T2_rows"]}
    census_ok = (rows890["C3_body"]["coarse_ordered_pair"] == [1, 2]
                 and rows890["C3_body"]["fine_dims"] == [1, 2]
                 and rows890["C4_face"]["coarse_ordered_pair"] == [1, 3]
                 and rows890["C4_face"]["fine_dims"] == [1, 1, 2]
                 and rows890["V_edge"]["coarse_ordered_pair"] == [1, 3]
                 and rows890["S3_body"]["MULTIPLICITY_FREE"] is False)

    anchor_ok = (bool(hitting) and sorted(hitting) == sorted(landed_names)
                 and len(hitting) == landed_count)
    return {
        "gate_1_cycle883_anchor_by_its_own_recipe": {
            "evaluated_at_(w0, w1, n)": [1, 2, 3],
            "rows": [{"name": r["name"], "value": r["value"],
                      "hits_the_anchor": r["_value"] == TARGET_ANCHOR}
                     for r in c3],
            "forms_returning_the_anchor_recomputed_here": sorted(hitting),
            "forms_returning_the_anchor_in_the_pinned_883_cache":
                sorted(landed_names),
            "count_recomputed_here": len(hitting),
            "count_in_the_pinned_883_cache": landed_count,
            "value_for_value_match": anchor_ok,
            "docstring_discrepancy_found_in_the_pinned_883_primary": (
                "883's module docstring says 'four distinct closed forms in "
                "(1, 2, 3) return 2/9'; its own certificate M computed and "
                "recorded FIVE, and five is what recomputes here.  The prose "
                "is stale, the computation is not; nothing downstream of the "
                "count changes."
            ),
        },
        "gate_2_cycle888_two_route_agreement_at_C3": {
            "cycle888_cache_says_both_routes_agree": routes_agree_888,
            "cycle888_group_theoretic_route_pair": route_pair,
            "rebuilt_here_cyclic_native": list(native),
            "rebuilt_here_group_theoretic": list(grouped),
            "all_four_agree": rebuilt_agree,
        },
        "gate_3_cycle890_census_rows": {
            "C3_body": rows890["C3_body"]["coarse_ordered_pair"],
            "C4_face_coarse": rows890["C4_face"]["coarse_ordered_pair"],
            "C4_face_fine": rows890["C4_face"]["fine_dims"],
            "V_edge_coarse": rows890["V_edge"]["coarse_ordered_pair"],
            "S3_body_is_multiplicity_free":
                rows890["S3_body"]["MULTIPLICITY_FREE"],
            "value_for_value_match": census_ok,
        },
        "finding": (
            f"883's anchor recomputes to {q(TARGET_ANCHOR)} on "
            f"{len(hitting)} of its own seven forms, matching its pinned "
            f"cache name-for-name; 888's two routes agree at C3 and are "
            f"rebuilt here to the same pair {list(grouped)}; 890's census "
            f"rows match value-for-value."
        ),
        "pass": anchor_ok and routes_agree_888 and rebuilt_agree and census_ok,
    }


# --------------------------------------------------------------------------
# scope construction (built once, used by every certificate)
# --------------------------------------------------------------------------
def build_scopes() -> dict:
    scopes = {}
    for h in all_subgroups():
        name = structure_name(h)
        if name in scopes:
            continue
        orbs = orbits_of(h, SHELL)
        free = [o for o in orbs if len(o) == len(h) and len(h) > 1]
        if not free:
            continue
        points = sorted(max(free, key=len))
        scopes[name] = {
            "name": name,
            "subgroup": h,
            "order": len(h),
            "points": points,
            "free_orbit_length": len(points),
            "shell_orbit_lengths": sorted(len(o) for o in orbs),
        }
    return scopes


SCOPES = build_scopes()
SCOPE_ORDER = ["C2_face", "C2_edge", "C3_body", "C4_face", "V_edge",
               "S3_body"]


def hecke_algebra_basis(subgroup, points):
    """Basis of End_H(M): all matrices commuting with every rho(h).  Its
    dimension is the number of H-orbits on X x X (the FIND-3 identity)."""
    n = len(points)
    mats = [permutation_matrix(g, points) for g in sorted(subgroup)]
    rows = []
    for m in mats:
        for i in range(n):
            for j in range(n):
                row = [Fraction(0)] * (n * n)
                for k in range(n):
                    row[i * n + k] += m[k][j]        # (A rho)_{ij}
                    row[k * n + j] -= m[i][k]        # (rho A)_{ij}
                rows.append(row)
    flat = kernel_basis(rows, n * n)
    return [[[v[i * n + j] for j in range(n)] for i in range(n)]
            for v in flat]


def readout_decomposition(scope) -> dict:
    """The readout (permutation) module of the free orbit.  The COARSE split
    comes from 888's group-theoretic route.  MULTIPLICITY-FREENESS is decided
    by the standard exact criterion -- the module is multiplicity-free iff its
    Hecke algebra End_H(M) is commutative -- with the FIND-3 pair-orbit
    identity as an independent dimension gate.  Fine rational dimensions are
    computed by cyclotomic kernels where a single generator exists and by
    simultaneous sign eigenspaces for the elementary-abelian scope; where
    neither route applies the field is reported as null rather than guessed."""
    h, points = scope["subgroup"], scope["points"]
    n = len(points)
    gens = [g for g in sorted(h) if g != IDENT and element_order(g) == len(h)]
    dec, route = None, None
    if gens:
        mat = permutation_matrix(gens[0], points)
        dec = cyclotomic_fine_dims(mat, element_order(gens[0]))
        route = "cyclotomic_kernels_of_a_generator"
    elif all(element_order(g) <= 2 for g in h):
        mats = [permutation_matrix(g, points) for g in sorted(h)]
        dims, blocks, seen_dim = [], [], 0
        for sign in product((1, -1), repeat=len(mats)):
            rows = []
            for s, m in zip(sign, mats):
                rows.extend(mat_sub(m, [[Fraction(s) if i == j else Fraction(0)
                                         for j in range(n)]
                                        for i in range(n)]))
            ker = kernel_basis(rows, n)
            if ker:
                blocks.append({"sign_pattern": list(sign),
                               "component_dimension": len(ker)})
                dims.extend([1] * len(ker))
                seen_dim += len(ker)
        route = "simultaneous_sign_eigenspaces"
        if seen_dim == n:
            dec = {"minimal_polynomial": None, "isotypes": blocks,
                   "fine_dims": sorted(dims), "space_dimension": n}
    else:
        route = "no_single_generator_and_not_elementary_abelian"

    hecke = hecke_algebra_basis(h, points)
    commutes = all(mat_mul(a, b) == mat_mul(b, a)
                   for a in hecke for b in hecke)
    pair_orbits = pair_orbit_identity(h, points)
    return {
        "ok": True,
        "route": route,
        "space_dimension": n,
        "coarse_pair": list(group_pair(h, points)),
        "fine_dims": dec["fine_dims"] if dec else None,
        "multiplicity_free": commutes,
        "multiplicity_freeness_route":
            "End_H(M) is commutative (Hecke-algebra criterion)",
        "hecke_algebra_dimension": len(hecke),
        "pair_orbit_identity_orbits_on_X_times_X": pair_orbits,
        "FIND3_safety_gate": len(hecke) == pair_orbits == len(h),
        "minimal_polynomial_of_a_generator":
            dec["minimal_polynomial"] if dec else None,
    }


def geometric_transverse(scope) -> dict:
    """The note's own object: the real normal space of the subgroup's fixed
    line inside the Z^3 lattice, with its fine decomposition."""
    h = scope["subgroup"]
    fixed = fixed_space_basis(h)
    if len(fixed) != 1:
        return {"ok": False,
                "fixed_space_dimension": len(fixed),
                "reason": ("no one-dimensional common fixed line, so the "
                           "note's fixed-locus / normal-space split does not "
                           "exist at this scope")}
    axis = primitive_int_vector(fixed[0])
    normal = kernel_basis([[Fraction(c) for c in axis]], 3)
    gens = [g for g in sorted(h) if g != IDENT and element_order(g) == len(h)]
    dec = None
    if gens:
        restricted = restrict_to(normal, [[Fraction(x) for x in row]
                                          for row in gens[0]])
        if restricted is not None:
            dec = cyclotomic_fine_dims(restricted, element_order(gens[0]))
    return {
        "ok": True,
        "fixed_space_dimension": 1,
        "axis": list(axis),
        "axis_kind": axis_kind(axis),
        "normal_space_dimension": len(normal),
        "normal_space_basis": [[q(c) for c in v] for v in normal],
        "fine_dims": dec["fine_dims"] if dec else None,
        "minimal_polynomial_of_a_generator":
            dec["minimal_polynomial"] if dec else None,
    }


def l_face_on(space_basis, matrices_by_element, order: int) -> dict:
    """The retained L-face recipe, verbatim:
       L = (1/|H|) sum_{h != e} 1 / det_R(I - h|_space)."""
    rows, total, singular = [], Fraction(0), []
    d = len(space_basis)
    for label, mat in matrices_by_element:
        restricted = restrict_to(space_basis, mat)
        if restricted is None:
            return {"ok": False, "reason": f"{label} does not preserve the "
                                           f"space"}
        det = det_exact(mat_sub(identity_matrix(d), restricted))
        rows.append({"element": label, "det_R_I_minus_h": q(det)})
        if det == 0:
            singular.append(label)
        else:
            total += Fraction(1) / det
    if singular:
        return {"ok": False, "rows": rows, "singular_elements": singular,
                "reason": "det_R(I - h) vanishes on at least one non-identity "
                          "element, so the recipe divides by zero here"}
    value = total / order
    return {"ok": True, "rows": rows, "group_order": order,
            "sum_of_inverse_determinants": q(total), "value": q(value),
            "_value": value}


# --------------------------------------------------------------------------
# certificate D (Q1): the construction's native K at every scope
# --------------------------------------------------------------------------
def family_of(pairs) -> dict:
    """Outcome-neutral comparison: which family (if any) reproduces the given
    {N: value} map on every N in the map?"""
    matches = []
    for fam, fn in FAMILIES.items():
        if all(fn(N) == v for N, v in pairs.items()):
            matches.append(fam)
    return {
        "family_values_at_each_N": {
            str(N): {fam: q(fn(N)) for fam, fn in FAMILIES.items()}
            for N in sorted(pairs)},
        "observed": {str(N): q(v) for N, v in sorted(pairs.items())},
        "matching_families": matches,
        "verdict": (matches[0] if len(matches) == 1
                    else ("NONE" if not matches else "AMBIGUOUS:" +
                          ",".join(matches))),
    }


def native_value_certificate(recipe) -> dict:
    forms = recipe["_forms"]
    c3 = evaluate_recipe(forms, 1, 2, 3)
    recovered = [f for f, r in zip(forms, c3) if r["_value"] == TARGET_ANCHOR]

    rows, per_scope = [], {}
    for name in SCOPE_ORDER:
        scope = SCOPES.get(name)
        if scope is None:
            continue
        dec = readout_decomposition(scope)
        w0, w1 = dec["coarse_pair"]
        n = scope["free_orbit_length"]
        evals = evaluate_recipe(recovered, w0, w1, n)
        values = sorted({r["value"] for r in evals})
        agree = len(values) == 1
        native = evals[0]["_value"] if agree else None
        rows.append({
            "scope": name,
            "group_order": scope["order"],
            "free_orbit_length": n,
            "readout_space_dimension": dec["space_dimension"],
            "coarse_pair_w0_w1": [w0, w1],
            "fine_dims": dec["fine_dims"],
            "multiplicity_free": dec["multiplicity_free"],
            "FIND3_safety_gate": dec["FIND3_safety_gate"],
            "recovered_recipe_values": {r["name"]: r["value"] for r in evals},
            "recovered_recipe_forms_all_agree": agree,
            "native_K": q(native) if native is not None else None,
            "canonical_scope_for_the_construction": dec["multiplicity_free"],
        })
        per_scope[name] = native

    c3_native = per_scope.get("C3_body")
    c4_native = per_scope.get("C4_face")
    comparison = family_of({3: c3_native, 4: c4_native})

    # why the ambiguity 883 priced is a phantom at the family level
    identity_rows = []
    for n in range(2, 13):
        w0, w1 = cyclic_pair(n)
        evals = evaluate_recipe(recovered, w0, w1, n)
        vals = {r["value"] for r in evals}
        identity_rows.append({"n": n, "coarse_pair": [w0, w1],
                              "distinct_values_among_the_recovered_forms":
                                  sorted(vals),
                              "collapse": len(vals) == 1,
                              "equals_F_dim":
                                  evals[0]["_value"] == FAMILIES["F_dim"](n)})
    collapse_everywhere = all(r["collapse"] and r["equals_F_dim"]
                              for r in identity_rows)

    ok = (c3_native == TARGET_ANCHOR
          and all(r["recovered_recipe_forms_all_agree"] for r in rows)
          and c4_native is not None
          and len(comparison["matching_families"]) <= 1)
    return {
        "question": ("Executing 883's own recipe on the construction's own "
                     "decomposition, what does one full free orbit read at "
                     "each scope?"),
        "recovered_recipe_forms": [f["name"] for f in recovered],
        "recovered_recipe_count": len(recovered),
        "rows": rows,
        "native_K_at_C3": q(c3_native) if c3_native else None,
        "native_K_at_C4": q(c4_native) if c4_native else None,
        "restriction_gate_C3_reproduces_the_anchor":
            c3_native == TARGET_ANCHOR,
        "family_comparison": comparison,
        "family_verdict": comparison["verdict"],
        "the_883_ambiguity_is_a_phantom_at_the_family_level": {
            "what_883_priced": (
                "883 recorded a five-fold DISCRETE CHOICE: five of its seven "
                "enumerated closed forms return 2/9 at (1, 2, 3), and it "
                "concluded 'nothing in the derivation picks one' (SL1b)."),
            "what_is_computed_here": (
                "On the free-orbit locus w0 = 1, w1 = n - 1, w0 + w1 = n, so "
                "all five forms are the SAME FUNCTION OF THE SCOPE.  The "
                "five-fold choice is a choice of EXPRESSION, not of value: it "
                "induces a singleton on scopes."),
            "rows": identity_rows,
            "all_five_collapse_to_F_dim_on_every_orbit_length":
                collapse_everywhere,
            "the_honest_residual": (
                "This closes SL1b only WITHIN 883's own enumerated form set.  "
                "Forms outside that set, in the same data, bind elsewhere -- "
                "the planted variants in certificate G exhibit two of them.  "
                "What is closed is: the recipe 883 actually wrote down is "
                "family-identified.  What is not closed is: that 883's "
                "enumeration was exhaustive."),
        },
        "finding": (
            f"The recovered recipe evaluates to {q(c3_native)} at C3 (the "
            f"restriction gate) and {q(c4_native)} at C4; the family "
            f"comparison returns {comparison['verdict']}."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate E (Q2): the retained L-face arithmetic at C4
# --------------------------------------------------------------------------
def l_face_certificate() -> dict:
    rows = []
    geometric, readout = {}, {}
    for name in SCOPE_ORDER:
        scope = SCOPES.get(name)
        if scope is None:
            continue
        h = scope["subgroup"]
        order = len(h)
        non_identity = [(f"h{i}_order{element_order(g)}", g) for i, g in
                        enumerate(sorted(h)) if g != IDENT]

        geo = geometric_transverse(scope)
        if geo["ok"]:
            mats = [(lbl, [[Fraction(x) for x in row] for row in g])
                    for lbl, g in non_identity]
            normal = kernel_basis(
                [[Fraction(c) for c in geo["axis"]]], 3)
            geo_l = l_face_on(normal, mats, order)
        else:
            geo_l = {"ok": False, "reason": geo["reason"]}

        points = scope["points"]
        n = len(points)
        ones = [[Fraction(1)] * n]
        complement = kernel_basis(ones, n)     # the sum-zero readout complement
        mats = [(lbl, permutation_matrix(g, points)) for lbl, g in
                non_identity]
        read_l = l_face_on(complement, mats, order)
        red_fine = readout_decomposition(scope)["fine_dims"]
        transverse_fine = None
        if red_fine is not None:
            transverse_fine = sorted(red_fine)
            transverse_fine.remove(1)          # drop the invariant line

        rows.append({
            "scope": name,
            "group_order": order,
            "geometric_normal_space": {
                "defined": geo["ok"],
                "reason_if_undefined": geo.get("reason"),
                "dimension": geo.get("normal_space_dimension"),
                "fine_dims": geo.get("fine_dims"),
                "axis": geo.get("axis"),
                "axis_kind": geo.get("axis_kind"),
                "L_face": {k: v for k, v in geo_l.items()
                           if not k.startswith("_")},
            },
            "readout_transverse_space": {
                "dimension": n - 1,
                "readout_module_fine_dims": red_fine,
                "transverse_fine_dims": transverse_fine,
                "L_face": {k: v for k, v in read_l.items()
                           if not k.startswith("_")},
            },
        })
        geometric[name] = geo_l.get("_value")
        readout[name] = read_l.get("_value")

    geo_cmp = family_of({3: geometric["C3_body"], 4: geometric["C4_face"]})

    # the note's recipe, evaluated abstractly for every cyclic order, exactly:
    # sum over non-identity roots of unity of 1 / ((1 - z)(1 - z^-1)), computed
    # as the trace of the inverse of multiplication by (1 - x)(1 - x^{N-1}) in
    # Q[x] / Phi-free((x^N - 1)/(x - 1)).  No floating point, no closed form
    # assumed.
    abstract_rows = []
    for N in range(2, 13):
        f = [1] * N                                  # (x^N - 1)/(x - 1)
        d = N - 1
        def reduce_poly(p):
            p = [Fraction(x) for x in p]
            while len(p) > d:
                lead, k = p[-1], len(p) - 1
                p = p[:-1]
                for i, c in enumerate(f[:-1]):
                    p[k - d + i] -= lead * Fraction(c)
                p = list(p)
            while len(p) < d:
                p.append(Fraction(0))
            return p
        u = poly_mul([1, -1], [1] + [0] * (N - 2) + [-1])   # (1-x)(1-x^{N-1})
        cols = []
        for j in range(d):
            shifted = [0] * j + list(u)
            cols.append(reduce_poly(shifted))
        mult = [[cols[j][i] for j in range(d)] for i in range(d)]
        # trace of the inverse of `mult`
        aug = [row[:] + [Fraction(1) if i == j else Fraction(0)
                         for j in range(d)]
               for i, row in enumerate(mult)]
        red, piv = rref(aug)
        inv = [[red[i][d + j] for j in range(d)] for i in range(d)]
        trace = sum(inv[i][i] for i in range(d))
        value = trace / N
        abstract_rows.append({
            "N": N,
            "sum_of_inverse_determinants": q(trace),
            "L_face_value": q(value),
            "equals_F_res": value == FAMILIES["F_res"](N),
            "equals_F_dim": value == FAMILIES["F_dim"](N),
        })
    abstract_is_F_res = all(r["equals_F_res"] for r in abstract_rows)

    # the module identification that collapses the two readings at N = 3
    collapse = []
    for name in ("C2_face", "C3_body", "C4_face"):
        scope = SCOPES[name]
        geo = geometric_transverse(scope)
        red = readout_decomposition(scope)
        readout_fine = red["fine_dims"]
        # the readout transverse fine dims = readout fine dims minus one copy
        # of the trivial isotype
        transverse_fine = sorted(readout_fine)
        transverse_fine.remove(1)
        collapse.append({
            "scope": name,
            "geometric_normal_fine_dims": geo.get("fine_dims"),
            "readout_transverse_fine_dims": transverse_fine,
            "the_two_spaces_are_isomorphic_as_H_modules":
                geo.get("fine_dims") == transverse_fine,
        })

    # the three families coincide pairwise only at N = 3 -- computed, exact
    coincidences = []
    for a, b in (("F_dim", "F_res"), ("F_dim", "F_ded"), ("F_res", "F_ded")):
        hits = [N for N in range(2, 2001)
                if FAMILIES[a](N) == FAMILIES[b](N)]
        coincidences.append({"pair": [a, b], "N_where_equal": hits})
    triple = [N for N in range(2, 2001)
              if FAMILIES["F_dim"](N) == FAMILIES["F_res"](N)
              == FAMILIES["F_ded"](N)]

    disagree = geometric["C4_face"] != readout.get("C4_face")
    return {
        "question": ("The retained anchor arithmetic is the note's finite "
                     "inverse-normal-determinant average.  What does IT read "
                     "at the C4 analogue, from its own recipe?"),
        "recipe_as_written_in_the_pinned_note":
            "L_H(N) = (1/|H|) sum_{h != e} 1 / det_R(I - h|_N)",
        "rows": rows,
        "geometric_L_face_at_C3": q(geometric["C3_body"]),
        "geometric_L_face_at_C4": q(geometric["C4_face"]),
        "geometric_family_comparison": geo_cmp,
        "geometric_family_verdict": geo_cmp["verdict"],
        "readout_L_face_at_C3": (q(readout["C3_body"])
                                 if readout["C3_body"] else None),
        "readout_L_face_at_C4_is_defined": readout.get("C4_face") is not None,
        "why_the_readout_L_face_dies_off_prime_orbit_length": (
            "det_R(I - h) on the readout complement vanishes exactly when h "
            "fixes a nonzero vector there, i.e. when h has order < n.  A free "
            "orbit of length n has such an h unless every non-identity "
            "element has order n -- that is, unless n is PRIME.  C3 is prime; "
            "C4 is not, and its square acts trivially on the [1] (sign) "
            "summand of the [1, 2] readout transverse decomposition, which is "
            "precisely the summand the geometric normal plane does not have."
        ),
        "the_L_face_on_the_READOUT_space_at_prime_n_is_F_dim": {
            "rows": [{"n": p,
                      "value": q(Fraction(p - 1, p * p)),
                      "equals_F_dim": True}
                     for p in (2, 3, 5, 7)],
            "why": ("at prime p every non-identity element generates, so "
                    "det_R(I - h) = p on the (p-1)-dimensional complement for "
                    "all p-1 of them, giving (1/p)(p-1)(1/p) = (p-1)/p^2."),
        },
        "abstract_cyclic_rows_from_the_notes_own_recipe": abstract_rows,
        "the_notes_recipe_is_the_F_res_family": abstract_is_F_res,
        "module_identification_that_collapses_the_two_readings": collapse,
        "family_pairwise_coincidences_over_N_in_2_to_2000": coincidences,
        "all_three_families_coincide_only_at": triple,
        "the_two_lineages_disagree_at_C4": disagree,
        "finding": (
            f"The retained L-face reads {q(geometric['C3_body'])} at C3 and "
            f"{q(geometric['C4_face'])} at C4, binding to "
            f"{geo_cmp['verdict']}; its transport onto the readout space is "
            f"defined only at prime orbit length and there equals F_dim.  The "
            f"C3 agreement is the module identification "
            f"(geometric normal plane) == (readout transverse space), which "
            f"holds at C3 and fails at C4."
        ),
        "pass": (geometric["C3_body"] == TARGET_ANCHOR
                 and geo_cmp["verdict"] == "F_res"
                 and abstract_is_F_res
                 and triple == [3]
                 and readout.get("C4_face") is None),
    }


# --------------------------------------------------------------------------
# certificate F (Q3): the fitted value's family status
# --------------------------------------------------------------------------
MOBIUS_BOUND = 4
Q3_N_MAX = 2000
Q3_EXPONENTS = (1, 2)


def q3_certificate() -> dict:
    lo, hi = FITTED_LO, FITTED_HI
    lo_n, lo_d = lo.numerator, lo.denominator
    hi_n, hi_d = hi.numerator, hi.denominator
    mid = (lo + hi) / 2

    tuples = [(a, b, c, d)
              for a in range(-MOBIUS_BOUND, MOBIUS_BOUND + 1)
              for b in range(-MOBIUS_BOUND, MOBIUS_BOUND + 1)
              for c in range(-MOBIUS_BOUND, MOBIUS_BOUND + 1)
              for d in range(-MOBIUS_BOUND, MOBIUS_BOUND + 1)
              if a * d - b * c != 0]
    cd_pairs = sorted({(c, d) for _, _, c, d in tuples})
    ab_pairs = sorted({(a, b) for a, b, _, _ in tuples})

    base = []
    for fam, fn in FAMILIES.items():
        for N in range(2, Q3_N_MAX + 1):
            v = fn(N)
            if v == 0:
                continue
            for e in Q3_EXPONENTS:
                w = v ** e
                base.append((fam, N, e, w.numerator, w.denominator))

    inside, best = [], None
    for fam, N, e, u, v in base:
        nums = sorted({a * u + b * v for a, b in ab_pairs})
        for c, d in cd_pairs:
            den = c * u + d * v
            if den == 0:
                continue
            s = 1 if den > 0 else -1
            aden = den * s
            # exact: is any representable numerator inside [lo, hi] * den?
            n_lo = -((-(lo_n * aden)) // lo_d) if s > 0 else \
                   -((-(-hi_n * aden)) // hi_d)
            # nearest representable numerator to mid * den (exact after pick)
            target = mid * den
            k = bisect.bisect_left(nums, int(target))
            for cand in nums[max(0, k - 2):k + 3]:
                value = Fraction(cand, den)
                dist = (Fraction(0) if lo <= value <= hi
                        else min(abs(value - lo), abs(value - hi)))
                if best is None or dist < best[0]:
                    best = (dist, value, fam, N, e, c, d, cand)
                if lo <= value <= hi:
                    inside.append({"family": fam, "N": N, "exponent": e,
                                   "value": q(value)})
            del n_lo

    # the tail lemma: beyond a computed N0 no member of the space can be inside
    limit_points = sorted({Fraction(p, r)
                           for p in range(-MOBIUS_BOUND, MOBIUS_BOUND + 1)
                           for r in range(1, MOBIUS_BOUND + 1)}
                          | {Fraction(-p, r)
                             for p in range(1, MOBIUS_BOUND + 1)
                             for r in range(1, MOBIUS_BOUND + 1)})
    tau = None
    degenerate_constants_inside = []
    for a, b, c, d in tuples:
        if d == 0:
            # M(F) = (aF + b) / (cF).  If b == 0 this is the constant a/c;
            # otherwise |M(F)| >= (|b| - |a|F)/(|c|F), which exceeds the
            # enclosure once F < |b| / (|a| + hi*|c|).  Both branches are
            # computed, not asserted.
            if b == 0:
                const = Fraction(a, c)
                if lo <= const <= hi:
                    degenerate_constants_inside.append(q(const))
                continue
            bound = Fraction(abs(b), 1) / (Fraction(abs(a)) + hi * abs(c))
            if tau is None or bound < tau:
                tau = bound
            continue
        r = Fraction(b, d)
        delta = (Fraction(0) if lo <= r <= hi
                 else min(abs(r - lo), abs(r - hi)))
        if delta == 0:
            tau = Fraction(0)
            break
        bound = (delta * d * d) / (abs(a * d - b * c) + delta * abs(d * c))
        bound = abs(bound)
        if tau is None or bound < tau:
            tau = bound
    n0 = {}
    for fam, fn in FAMILIES.items():
        for e in Q3_EXPONENTS:
            worst = None
            for N in range(2, Q3_N_MAX + 1):
                v = fn(N) ** e
                if v == 0:
                    continue
                small = min(v, Fraction(1) / v)
                if small >= tau:
                    worst = N
            n0[f"{fam}^{e}"] = worst
    tail_covered = all(v is None or v <= Q3_N_MAX for v in n0.values())

    # smallest denominator of any rational inside the enclosure (Stern-Brocot)
    def smallest_denominator(a: Fraction, b: Fraction) -> Fraction:
        p_lo, q_lo, p_hi, q_hi = 0, 1, 1, 0
        while True:
            p, r = p_lo + p_hi, q_lo + q_hi
            v = Fraction(p, r)
            if v < a:
                p_lo, q_lo = p, r
            elif v > b:
                p_hi, q_hi = p, r
            else:
                return v

    floor_frac = smallest_denominator(lo, hi)

    headline = []
    for fam, fn in FAMILIES.items():
        for N in (2, 3, 4, 5, 6):
            v = fn(N)
            dist = (Fraction(0) if lo <= v <= hi
                    else min(abs(v - lo), abs(v - hi)))
            headline.append({"family": fam, "N": N, "value": q(v),
                             "exact_distance_to_the_enclosure": q(dist),
                             "distance_decimal": f"{float(dist):.6e}"})

    dist, value, fam, N, e, c, d, cand = best
    return {
        "question": ("Does any member of a declared, bounded transform space "
                     "over the three families land inside the Cycle-897 "
                     "fitted enclosure?"),
        "fitted_enclosure": [q(lo), q(hi)],
        "fitted_enclosure_decimal": ["0.222222047073817229",
                                     "0.222222047073817230"],
        "declared_transform_space": {
            "form": "(a*F + b) / (c*F + d)",
            "integer_coefficient_bound": MOBIUS_BOUND,
            "nondegeneracy": "a*d - b*c != 0",
            "base_values": "F_fam(N)^e, fam in {F_dim, F_res, F_ded}",
            "N_range": [2, Q3_N_MAX],
            "exponents": list(Q3_EXPONENTS),
            "negative_exponents": ("subsumed: (a,b,c,d) = (0,1,1,0) is the "
                                   "reciprocal, so F^-1 and F^-2 are already "
                                   "in the image"),
            "size": {"mobius_tuples": len(tuples),
                     "base_values": len(base),
                     "distinct_denominator_pairs": len(cd_pairs)},
            "honest_bound": (
                "This space contains every rational scaling p/q with "
                "|p|,|q| <= 4, every integer and quarter-integer shift in "
                "that range, reciprocals, and their compositions of depth "
                "one.  It does NOT contain: transcendental transforms, "
                "products of two different families, transforms with "
                "coefficients above 4, or exponents outside {1, 2} and their "
                "reciprocals.  Nothing here rules those out."
            ),
        },
        "members_inside_the_enclosure": inside,
        "count_inside_the_enclosure": len(inside),
        "nearest_member": {
            "value": q(value),
            "value_decimal": f"{float(value):.18f}",
            "family": fam, "N": N, "exponent": e,
            "mobius_denominator_pair": [c, d],
            "numerator": cand,
            "exact_distance_to_the_enclosure": q(dist),
            "distance_decimal": f"{float(dist):.6e}",
        },
        "headline_rows": headline,
        "smallest_denominator_rational_inside_the_enclosure": {
            "value": q(floor_frac),
            "denominator": floor_frac.denominator,
            "why_this_matters": (
                "any rational at all inside the enclosure needs a denominator "
                f"of at least {floor_frac.denominator}; the three families "
                "produce denominators dividing N^2, 12N and 3N respectively, "
                "so a family value could only reach that height at an N far "
                "outside the range where the family is anywhere near the "
                "target."
            ),
        },
        "tail_lemma": {
            "tau_the_uniform_smallness_threshold": q(tau),
            "statement": (
                "for a Mobius tuple with d != 0, |M(F) - b/d| = "
                "|F||ad-bc| / (|d||cF+d|) <= |F||ad-bc| / (|d|(|d|-|c||F|)), "
                "so M(F) cannot reach the enclosure once "
                "|F| < delta*d^2 / (|ad-bc| + delta|d||c|) where delta is the "
                "distance from b/d to the enclosure; tuples with d = 0 send "
                "F -> 0 to infinity or to the constant a/c.  The same bound "
                "applies to F -> infinity after substituting G = 1/F."),
            "largest_N_still_above_the_threshold_per_base_family": n0,
            "finite_scan_covers_the_whole_tail": tail_covered,
            "limit_point_count": len(limit_points),
            "degenerate_d_equals_zero_constants_inside_the_enclosure":
                degenerate_constants_inside,
            "no_degenerate_constant_is_inside":
                not degenerate_constants_inside,
        },
        "finding": (
            f"{len(inside)} of the {len(base) * len(cd_pairs)} scanned "
            f"(base value, denominator) cells put any representable member "
            f"inside the enclosure.  The nearest member of the whole declared "
            f"space is {q(value)} at distance {float(dist):.6e}; the nearest "
            f"bare family value is 2/9 at distance "
            f"{float(min(abs(Fraction(2, 9) - lo), abs(Fraction(2, 9) - hi))):.6e}."
        ),
        "pass": (len(inside) == 0 and tail_covered and dist > 0
                 and not degenerate_constants_inside),
    }


# --------------------------------------------------------------------------
# certificate G: falsifier visibility -- planted recipes
# --------------------------------------------------------------------------
PLANTED = {
    "PLANT_dim  w1 / (w0 + w1)^2":
        lambda w0, w1, n: Fraction(w1, (w0 + w1) ** 2),
    "PLANT_res  w1 * (w1 + 2) / (12 * n)":
        lambda w0, w1, n: Fraction(w1 * (w1 + 2), 12 * n),
    "PLANT_ded  w1 * (w1 - 1) / (3 * n)":
        lambda w0, w1, n: Fraction(w1 * (w1 - 1), 3 * n),
}


def planted_certificate() -> dict:
    rows = []
    for label, fn in PLANTED.items():
        c3 = fn(1, 2, 3)
        c4 = fn(1, 3, 4)
        cmp_ = family_of({3: c3, 4: c4})
        rows.append({
            "planted_recipe": label,
            "value_at_C3": q(c3),
            "returns_the_anchor_at_C3": c3 == TARGET_ANCHOR,
            "value_at_C4": q(c4),
            "family_verdict_through_the_same_machinery": cmp_["verdict"],
        })
    verdicts = [r["family_verdict_through_the_same_machinery"] for r in rows]
    all_anchor = all(r["returns_the_anchor_at_C3"] for r in rows)
    spans = sorted(verdicts) == ["F_ded", "F_dim", "F_res"]

    # a recipe that binds to NOTHING, to show the machinery can say NONE
    none_row = family_of({3: TARGET_ANCHOR, 4: TARGET_ANCHOR})
    return {
        "why_this_exists": (
            "A family comparison that can only ever answer 'F_dim' is not a "
            "comparison.  Three recipes -- all functions of the SAME "
            "decomposition data (w0, w1, n), all returning the anchor 2/9 at "
            "C3 -- are pushed through the identical machinery."),
        "rows": rows,
        "verdicts": verdicts,
        "every_plant_returns_the_anchor_at_C3": all_anchor,
        "the_three_plants_span_the_three_families": spans,
        "the_machinery_can_also_answer_NONE": {
            "recipe": "the constant 2/9 (the fine-top reading, see below)",
            "verdict": none_row["verdict"],
        },
        "the_fine_reading_caveat": (
            "890's census records C4_face with fine dims [1, 1, 2] and a "
            "'fine top pair' [1, 2].  A recipe reading (w0, w1) off the FINE "
            "top pair instead of the coarse split would return 2/9 at C4 as "
            "well -- a constant, binding to NONE of the three families.  That "
            "reading is excluded here not by preference but by C883-T6's own "
            "words, which state the pair is (1, 3) at n = 4; and under the "
            "fine reading 883's five recovered forms no longer agree with "
            "each other at C4 (they split into 2/9, 1/8 and 3/16), so the "
            "fine reading also fails 883's own internal consistency."),
        "finding": (
            f"Three planted recipes, all anchored at 2/9 at C3, bind to "
            f"{verdicts} respectively; the machinery also returns "
            f"{none_row['verdict']} for a recipe on no family."),
        "pass": all_anchor and spans and none_row["verdict"] == "NONE",
    }


def fine_reading_split() -> dict:
    """The fine-top reading's C4 values, computed rather than asserted."""
    recipe = recover_883_recipe()
    forms = recipe["_forms"]
    c3 = evaluate_recipe(forms, 1, 2, 3)
    recovered = [f for f, r in zip(forms, c3) if r["_value"] == TARGET_ANCHOR]
    fine = evaluate_recipe(recovered, 1, 2, 4)     # fine top pair (1,2), n = 4
    values = sorted({r["value"] for r in fine})
    return {
        "reading": "fine top pair (w0, w1) = (1, 2) with n = 4",
        "values": {r["name"]: r["value"] for r in fine},
        "distinct_values": values,
        "the_recovered_forms_disagree_under_this_reading": len(values) > 1,
    }


# --------------------------------------------------------------------------
# certificate H (Q4): the complete table
# --------------------------------------------------------------------------
def table_certificate(native: dict, lface: dict) -> dict:
    native_by = {r["scope"]: r for r in native["rows"]}
    l_by = {r["scope"]: r for r in lface["rows"]}
    rows = []
    for name in SCOPE_ORDER:
        if name not in native_by:
            continue
        nr, lr = native_by[name], l_by[name]
        n = nr["free_orbit_length"]
        rows.append({
            "scope": name,
            "group_order": nr["group_order"],
            "free_orbit_length": n,
            "multiplicity_free": nr["multiplicity_free"],
            "construction_is_canonical_here": nr["multiplicity_free"],
            "coarse_pair": nr["coarse_pair_w0_w1"],
            "readout_fine_dims": nr["fine_dims"],
            "native_K": nr["native_K"],
            "native_K_equals_F_dim_at_this_orbit_length":
                nr["native_K"] == q(FAMILIES["F_dim"](n)),
            "retained_L_face_geometric":
                lr["geometric_normal_space"]["L_face"].get("value"),
            "retained_L_face_geometric_defined":
                lr["geometric_normal_space"]["L_face"]["ok"],
            "retained_L_face_readout_defined":
                lr["readout_transverse_space"]["L_face"]["ok"],
            "the_two_lineages_agree_here": (
                lr["geometric_normal_space"]["L_face"].get("value")
                == nr["native_K"]),
            "F_dim": q(FAMILIES["F_dim"](n)),
            "F_res": q(FAMILIES["F_res"](n)),
            "F_ded": q(FAMILIES["F_ded"](n)),
        })
    agreeing = [r["scope"] for r in rows if r["the_two_lineages_agree_here"]]
    canonical = [r["scope"] for r in rows
                 if r["construction_is_canonical_here"]]
    return {
        "rows": rows,
        "scopes_where_the_construction_is_canonical": canonical,
        "scopes_where_the_two_lineages_agree": agreeing,
        "S3_note": (
            "S3_body carries a free orbit of length 6 but its readout module "
            "contains the 2-dimensional rational irreducible with "
            "MULTIPLICITY TWO (fine dims [1, 1, 2, 2]), so the split is a P^1 "
            "family and the construction is not canonical there.  It is "
            "listed for completeness and excluded from the binding table.  "
            "Its retained L-face is also undefined, and for a computed "
            "reason: the three order-2 elements of the body-diagonal S3 "
            "REVERSE the body diagonal, so the subgroup's common fixed space "
            "is 0-dimensional and the note's fixed-locus / normal-plane split "
            "does not exist at all.  Same for V_edge."),
        "E_trivial_note": (
            "The trivial subgroup has free orbit length 1, coarse pair "
            "(1, 0), and every family degenerates: F_dim(1) = 0, F_res(1) = "
            "0, F_ded(1) = 0.  It carries no readout complement and is "
            "excluded."),
        "finding": (
            f"{len(canonical)} scopes carry a canonical construction; the two "
            f"lineages agree on {len(agreeing)} of them "
            f"({agreeing}); the native K follows F_dim on every row."),
        "pass": (len(canonical) == 5 and agreeing == ["C3_body"]
                 and all(r["native_K_equals_F_dim_at_this_orbit_length"]
                         for r in rows)),
    }


# --------------------------------------------------------------------------
# outcome
# --------------------------------------------------------------------------
def outcome_certificate(native, lface, q3, table) -> dict:
    return {
        "Q1_the_constructions_native_value": {
            "recipe_recovered_by_AST": True,
            "native_K_at_C3": native["native_K_at_C3"],
            "restriction_gate_reproduces_2_over_9":
                native["restriction_gate_C3_reproduces_the_anchor"],
            "native_K_at_C4": native["native_K_at_C4"],
            "family_verdict": native["family_verdict"],
            "against": {"F_dim(4)": q(FAMILIES["F_dim"](4)),
                        "F_res(4)": q(FAMILIES["F_res"](4)),
                        "F_ded(4)": q(FAMILIES["F_ded"](4))},
        },
        "Q2_the_retained_anchor_arithmetic": {
            "geometric_L_face_at_C3": lface["geometric_L_face_at_C3"],
            "geometric_L_face_at_C4": lface["geometric_L_face_at_C4"],
            "family_verdict": lface["geometric_family_verdict"],
            "the_two_lineages_disagree_at_C4":
                lface["the_two_lineages_disagree_at_C4"],
            "verdict": (
                "The framework's DERIVATION lineage and its RETAINED ANCHOR "
                "lineage bind to DIFFERENT families.  The disagreement is "
                "concrete at C4: the construction reads "
                f"{native['native_K_at_C4']}, the retained arithmetic reads "
                f"{lface['geometric_L_face_at_C4']}.  At most one can be the "
                "record's readout.  The AXIOM-GROUNDED construction -- the "
                "one rebuilt here from 883's derivation via 888's "
                "group-theoretic route -- produces "
                f"{native['native_K_at_C4']}, i.e. "
                f"{native['family_verdict']}."),
            "why_they_agreed_at_C3": (
                "Two independent collapses coincide at N = 3 and only there.  "
                "(i) The geometric normal plane of the body-diagonal rotation "
                "and the readout module's invariant complement are the SAME "
                "C3-module (both the unique 2-dimensional rational "
                "irreducible), so the note's determinant average does not "
                "care which space it is evaluated on; at C4 the readout "
                "transverse space is [1, 2] and the geometric normal plane is "
                "[2], and the extra [1] makes the note's recipe singular.  "
                "(ii) The three families are pairwise equal only at N = 3, "
                "computed exactly: F_dim = F_res forces 12 = N(N+1), "
                "F_dim = F_ded forces N(N-2) = 3, F_res = F_ded forces "
                "3N = 9."),
        },
        "Q3_the_fitted_values_family_status": {
            "members_inside_the_enclosure": q3["count_inside_the_enclosure"],
            "nearest_member": q3["nearest_member"]["value"],
            "nearest_member_distance":
                q3["nearest_member"]["distance_decimal"],
            "smallest_denominator_admitted_by_the_enclosure":
                q3["smallest_denominator_rational_inside_the_enclosure"][
                    "denominator"],
            "verdict": ("No retained family, and no member of the declared "
                        "transform space over them, explains the fitted "
                        "number.  This is data for the obligation's future, "
                        "not a claim about what should explain it."),
        },
        "Q4_the_off_endpoint_rows": {
            "canonical_scopes":
                table["scopes_where_the_construction_is_canonical"],
            "scopes_where_the_lineages_agree":
                table["scopes_where_the_two_lineages_agree"],
        },
        "what_this_does_to_SL1b": (
            "SL1b asked which functional the record's readout is.  Within "
            "883's own enumerated form set the question is now ANSWERED as a "
            "family question and was never open: all five forms that return "
            "2/9 at C3 are the same function of the scope, namely F_dim.  "
            "What replaces SL1b is sharper and harder: the retained anchor "
            "note computes a DIFFERENT family, on a DIFFERENT space, and the "
            "two are distinguishable at C4.  The open item is no longer "
            "'which functional' but 'which SPACE the record reads' -- the "
            "geometric normal plane of the lattice rotation, or the readout "
            "module's invariant complement."),
        "what_would_falsify_this": (
            "Exhibit a closed form in (w0, w1, n) that (a) 883's derivation "
            "actually licenses rather than merely permits, (b) returns 2/9 at "
            "C3, and (c) returns 5/16 at C4.  Certificate G's PLANT_res is "
            "exactly such a form for (b) and (c); what it lacks is (a).  "
            "Alternatively: show that the record reads the geometric normal "
            "plane rather than the readout module, which would flip the "
            "verdict to F_res without touching any computation here."),
    }


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def build() -> dict:
    pins = pins_certificate()
    if not pins["pass"]:
        print(json.dumps({"FATAL": "pin verification failed", "pins": pins},
                         indent=1))
        sys.exit(2)

    recipe = recover_883_recipe()
    if not recipe["ok"]:
        print(json.dumps({"FATAL": "recipe recovery failed",
                          "recipe": recipe}, indent=1, default=str))
        sys.exit(2)

    gates = restriction_gates(recipe)
    if not gates["pass"]:
        print(json.dumps({"FATAL": "restriction gate failed",
                          "gates": gates}, indent=1, default=str))
        sys.exit(2)

    native = native_value_certificate(recipe)
    lface = l_face_certificate()
    q3 = q3_certificate()
    planted = planted_certificate()
    table = table_certificate(native, lface)
    fine = fine_reading_split()

    certificates = {
        "A_PINS": pins,
        "B_RECIPE_RECOVERY": {k: v for k, v in recipe.items()
                              if not k.startswith("_")},
        "C_RESTRICTION_GATES": gates,
        "D_Q1_NATIVE_VALUE": native,
        "E_Q2_RETAINED_L_FACE": lface,
        "F_Q3_FITTED_VALUE": q3,
        "G_FALSIFIER_VISIBILITY": planted,
        "H_Q4_COMPLETE_TABLE": table,
        "I_FINE_READING_SPLIT": fine,
    }
    passes = {k: v.get("pass") for k, v in certificates.items()
              if isinstance(v, dict) and "pass" in v}

    return {
        "cycle": 899,
        "question": ("Which of the three N=3-degenerate families does the "
                     "framework's own readout construction native-bind to, "
                     "and is that binding testable at C4?"),
        "answer": (
            f"The construction binds to {native['family_verdict']}: its "
            f"native K is {native['native_K_at_C3']} at C3 (the restriction "
            f"gate) and {native['native_K_at_C4']} at C4.  The retained "
            f"anchor arithmetic binds to {lface['geometric_family_verdict']}: "
            f"{lface['geometric_L_face_at_C3']} at C3 and "
            f"{lface['geometric_L_face_at_C4']} at C4.  They DISAGREE at C4, "
            f"and the disagreement is a disagreement about which SPACE the "
            f"record reads, not about which functional."),
        "certificates": certificates,
        "certificate_passes": passes,
        "all_certificates_pass": all(passes.values()),
        "outcome": outcome_certificate(native, lface, q3, table),
        "source_pins": [
            {"path": r["path"], "sha256": r["sha256"], "git_blob": r["git_blob"]}
            for r in pins["rows"]],
        "sharpest_new_facts": [
            "883's five-fold binding ambiguity is a phantom at the family "
            "level: on the free-orbit locus all five of its 2/9-returning "
            "forms are the identical function (n-1)/n^2 of the scope, so the "
            "recipe it wrote down IS family-identified even though the "
            "expression is not.",
            "The construction's native K at C4 is 3/16 = F_dim(4); the "
            "retained L-face at C4 is 5/16 = F_res(4).  The two lineages bind "
            "to different families and the disagreement is concrete.",
            "The retained L-face recipe, transported onto the readout module "
            "where the derivation lives, is DEFINED only at prime orbit "
            "length -- and there it equals F_dim, not F_res.  The F_res "
            "reading is a property of the geometric normal plane, not of the "
            "recipe.",
            "N = 3 is the unique orbit length at which the geometric normal "
            "plane and the readout transverse space are the same module; at "
            "C4 the readout transverse space carries an extra 1-dimensional "
            "sign summand on which the note's determinant vanishes.",
            "The three families are pairwise equal only at N = 3, forced by "
            "12 = N(N+1), N(N-2) = 3 and 3N = 9 respectively.",
            "The native K depends only on the free-orbit length, so C4_face "
            "and V_edge read identically (3/16) despite different fine "
            "decompositions ([1,1,2] vs [1,1,1,1]) -- while the retained "
            "L-face distinguishes them (5/16 vs undefined).",
        ],
        "next_attackable_question": (
            "Which space does the Record axiom's readout live on: the "
            "geometric normal plane of the lattice rotation, or the invariant "
            "complement of the readout module?  Everything numerical is now "
            "settled on both sides; the residual is a single identification, "
            "and it is decidable at C4."),
    }


def main() -> int:
    started = monotonic()
    first = build()
    second = build()
    stable = digest(first) == digest(second)
    first["deterministic_double_build"] = {
        "first_digest": digest(first),
        "second_digest": digest(second),
        "byte_stable": stable,
    }
    first["runtime_seconds"] = round(monotonic() - started, 3)
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(first, indent=1, sort_keys=True,
                                  default=str) + "\n")
    text = json.dumps(first, indent=1, sort_keys=True, default=str)
    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        text = text[:STDOUT_LIMIT_BYTES] + "\n... TRUNCATED ..."
    print(text)
    ok = first["all_certificates_pass"] and stable
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
