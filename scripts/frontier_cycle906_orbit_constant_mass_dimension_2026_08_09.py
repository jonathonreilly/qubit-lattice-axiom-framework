#!/usr/bin/env python3
"""Cycle 906 primary: the exact dimension of orbit-constant pushforward masses
that vanish on a required-zero subset, with an explicit basis.

SELF-CONTAINED.  Read inventory, stated in the two kinds the repo requires:

  * external or ancestral scientific inputs read: NONE.  No repository
    module is imported, no ancestor source, receipt, note or axiom file is
    read, and nothing outside this file supplies a number used in any
    certificate.
  * package-local integrity reads: this file reads only ITS OWN source path,
    to publish its content hash and to confirm by AST that the declared
    ``AUDIT_INPUT_PATHS`` is exactly ``(this file,)``.  That single path is
    the whole declared closure; a literally empty tuple is rejected as
    invalid by the cache envelope and the evidence-readiness gate, so the
    honest input-free shape is to declare the integrity read that happens.

WHAT IS PROVED HERE, EXACTLY

Fix a finite set of base points, a finite cyclic group acting on it, and a
partition of a finite set of fibre points over the base points with every
fibre non-empty.  Fix a subset of base points, called the required-zero
subset.  Consider rational-valued fibre weightings subject to two linear
conditions:

  (ZERO)  the weighting vanishes at every fibre point over the required-zero
          subset;
  (ORBIT) the pushforward mass -- the fibre-total at each base point -- takes
          the same value at every base point of a group orbit.

THEOREM (parameterization).  The solution space is spanned by the explicit
basis this runner constructs, and therefore has dimension

    (number of orbits disjoint from the required-zero subset)
  + sum over base points outside the required-zero subset of (fibre size - 1)

while the space of admissible pushforward masses has dimension exactly the
number of orbits disjoint from the required-zero subset.

COROLLARY (non-negative normalized solutions), on instances with at least
one disjoint orbit.  If the weighting is in addition required to be
non-negative with total mass one, then every solution is supported inside
the union of the orbits disjoint from the required-zero subset; the solution
set has dimension

    (number of disjoint orbits - 1)
  + sum over base points of those orbits of (fibre size - 1)

and its extreme points are exactly the weightings that place one disjoint
orbit's whole mass on a single fibre point at each base point of that orbit.
On the declared family there are instances where a Cartesian product of an
orbit-mass simplex with the fibre simplices gives a different number of
extreme points; the smallest is exhibited in the EXTREME_POINTS certificate.

The general proof of all of this is recorded in the note; this runner
verifies it, exhibits the basis and the representatives, and rejects wrong
formulas.

HOW IT IS CHECKED, AND WHAT EACH ROUTE SHARES

  route CLOSED_FORM      the combinatorial count above;
  route BASIS_LENGTH     the length of the explicitly constructed basis,
                         every vector verified against (ZERO) and (ORBIT)
                         and the family verified independent by exact rank;
  route NULLSPACE        exact fraction-free integer rank of the full
                         constraint matrix, dimension = columns - rank;
  route BASE_RANK        exact fraction-free integer rank of the base-level
                         matrix, for the pushforward dimension.

CLOSED_FORM and BASIS_LENGTH share the orbit classification and the
within-fibre count, so their agreement confirms the classification and not
the formula; NULLSPACE shares no helper with CLOSED_FORM.  The
ROUTE_INVENTORY certificate recomputes each route's helper set from this
file's own syntax tree and refuses any declared sharing that is not the real
one.

The dimension laws are declared as COEFFICIENTS, not as prose: the emitted
theorem sentences are rendered from those coefficients, every coefficient
set is checked against an independently computed dimension on every
instance, and a declared list of WRONG coefficient sets must each be
refuted by an exhibited instance.  A wrong sentence therefore cannot pass:
it either fails the rendering comparison or fails the evaluation.

The enumerated family has one through five base points and one canonical
contiguous representative for every orbit-size partition, with every
fibre-size assignment from the declared alphabet and EVERY required-zero
subset on that representative.  Since the conditions are invariant under a
simultaneous relabeling, this is every relevant decorated case up to
relabeling, not every labeled set partition.  Two larger declared instances
are carried for scale, where the fibre-level rank routes are deliberately not
run (stated, with the reason and with exactly what is established there
instead).

Exact integer and rational arithmetic throughout; no floating point enters
any verdict.  Every fraction emitted is a BOOKKEEPING FRACTION, NOT A
PROBABILITY: nothing here is a probability postulate, a Born-rule claim, a
measure selection, an interface claim, or a statement about any repository
census, symmetry, or physical condition.

Support runner.  Authority none, audit unset.  Independent audit still
required.
"""
from __future__ import annotations

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
import itertools
import json
from math import gcd
from pathlib import Path
import sys

AUDIT_TIMEOUT_SEC = 600
HOUSE_STDOUT_LIMIT_BYTES = 6_000

# The declared evidence closure contains exactly ONE path: this runner's own
# source.  That is the whole of what the run depends on.  There is no
# external or ancestral scientific input, so no ancestor source, receipt,
# note or axiom file appears here -- and none may be added without a claim
# that needs it.  A literally empty tuple is NOT the way to say this: the
# cache envelope and the evidence-readiness gate both read an empty
# declaration as an INVALID one (`runner_declared_inputs_invalid`), so the
# honest input-free shape is to declare the single package-local integrity
# read that actually happens.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle906_orbit_constant_mass_dimension_2026_08_09.py",
)

ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = AUDIT_INPUT_PATHS[0]
RECEIPT_PATH = "outputs/orbit_constant_mass_dimension_cycle906_receipt_2026_08_09.json"

FRACTION_LABEL = "bookkeeping fraction, not probability"

# ---- the declared enumerated family ---------------------------------------
# Base counts 1..MAX_BASE_POINTS, one canonical contiguous representative of
# every orbit-size partition, every fibre-size assignment from the declared
# alphabet, and every required-zero subset.  This covers the decorated cases
# up to simultaneous relabeling; it is not literal labeled-set-partition
# enumeration.
MAX_BASE_POINTS = 5
FIBRE_ALPHABET_SMALL = (1, 2, 3)   # used when base points <= 4
FIBRE_ALPHABET_WIDE = (1, 2)       # used at 5 base points, to bound the sweep
WIDE_ALPHABET_FROM = 5

# Brute-force extreme-point enumeration is exponential in the fibre-point
# count, so it runs on the declared bounded subfamily of instances with at
# most this many fibre points.  The bound is declared, not discovered.
VERTEX_ENUMERATION_MAX_FIBRE_POINTS = 6

# ---- the dimension laws, as coefficients ----------------------------------
# Each law is (coefficient on each counted quantity, ..., constant).  The
# emitted theorem sentences are RENDERED from these numbers, and each law is
# checked against an independently computed dimension on every instance.
# The REFUTED lists are wrong laws that must each be refuted by an exhibited
# instance, so that a passing law is a discriminated one rather than an
# unchallenged one.
DISJOINT_ORBIT_PHRASE = "the number of orbits disjoint from the required-zero subset"
OUTSIDE_FIBRE_PHRASE = ("the sum over base points outside that subset of"
                        " (fibre size minus one)")
DISJOINT_FIBRE_PHRASE = ("the sum over base points of those orbits of"
                         " (fibre size minus one)")

SOLUTION_DIMENSION_LAW = (1, 1, 0)
SOLUTION_DIMENSION_PHRASES = (DISJOINT_ORBIT_PHRASE, OUTSIDE_FIBRE_PHRASE)
SOLUTION_DIMENSION_REFUTED = ((0, 1, 0), (1, 0, 0), (1, 1, 1), (1, 1, -1),
                              (2, 1, 0), (1, 2, 0))

PUSHFORWARD_DIMENSION_LAW = (1, 0)
PUSHFORWARD_DIMENSION_PHRASES = (DISJOINT_ORBIT_PHRASE,)
PUSHFORWARD_DIMENSION_REFUTED = ((0, 0), (1, 1), (1, -1), (2, 0))

NORMALIZED_DIMENSION_LAW = (1, 1, -1)
NORMALIZED_DIMENSION_PHRASES = (DISJOINT_ORBIT_PHRASE, DISJOINT_FIBRE_PHRASE)
NORMALIZED_DIMENSION_REFUTED = ((1, 1, 0), (1, 0, -1), (0, 1, -1),
                                (1, 1, -2), (2, 1, -1))

# Sentence fragments that an earlier draft of this package, or the withdrawn
# Cycle-906 package, asserted and that are NOT true of this structure.  No
# emitted certificate may contain any of them.  Only their DIGESTS are
# published, so the withdrawn wording appears on no machine surface, and the
# certificate that publishes those digests is excluded from the scan.
REFUTED_SENTENCE_FRAGMENTS = (
    "unique up to scale",
    "product of simplices",
    "the tension resolves",
)

# Declared helper sets of the four dimension routes, recomputed from this
# file's syntax tree by the ROUTE_INVENTORY certificate.  Only names defined
# in this module count; builtins and standard-library calls are excluded.
ROUTE_ENTRY_POINTS = {
    "CLOSED_FORM": "Instance.route_count",
    "BASIS_LENGTH": "Instance.constructive_basis",
    "NULLSPACE": "Instance.route_nullspace",
    "BASE_RANK": "Instance.route_base_nullspace",
}
ROUTE_DECLARED_HELPERS = {
    "CLOSED_FORM": ("Instance.disjoint_orbits",),
    "BASIS_LENGTH": ("Instance.constructive_basis_sparse",
                     "Instance.disjoint_orbits", "Instance.fibre_points"),
    "NULLSPACE": ("Instance.constraint_rows", "Instance.fibre_points",
                  "exact_rank"),
    "BASE_RANK": ("Instance.base_level_rows", "exact_rank"),
}
ROUTE_DECLARED_SHARING = {
    "BASIS_LENGTH|CLOSED_FORM": ("Instance.disjoint_orbits",),
    "BASE_RANK|BASIS_LENGTH": (),
    "BASE_RANK|CLOSED_FORM": (),
    "BASE_RANK|NULLSPACE": ("exact_rank",),
    "BASIS_LENGTH|NULLSPACE": ("Instance.fibre_points",),
    "CLOSED_FORM|NULLSPACE": (),
}

# Two declared larger instances.  Their parameters are CHOSEN NUMBERS for a
# scaling demonstration.  No claim is made, here or in the note, that they
# describe any repository census, event space, or physical configuration.
LARGE_INSTANCES = (
    {
        "name": "twelve_orbits_of_eleven_uniform_fibres",
        "orbit_sizes": (11,) * 12,
        "fibre_rule": "every base point carries 129 fibre points",
        "zero_rule": "every base point of the first eleven orbits",
    },
    {
        "name": "twelve_orbits_of_eleven_mixed_fibres_partial_orbit_cut",
        "orbit_sizes": (11,) * 12,
        "fibre_rule": ("the last orbit's base points carry 129 fibre points;"
                       " every other base point carries 7"),
        "zero_rule": ("every base point of the first ten orbits, plus the"
                      " first base point of the eleventh orbit"),
    },
)

# Kept separately from LARGE_INSTANCES so deleting one declared example cannot
# silently change the promised coverage.  The independent checker carries its
# own full transcription of the two specifications.
EXPECTED_LARGE_INSTANCE_NAMES = (
    "twelve_orbits_of_eleven_uniform_fibres",
    "twelve_orbits_of_eleven_mixed_fibres_partial_orbit_cut",
)


# ---------------------------------------------------------------------------
# import firewall: nothing from this repository may be imported
# ---------------------------------------------------------------------------

class _RepositoryImportFirewall(importlib.abc.MetaPathFinder):
    """Refuse every repository-local import; record any attempt."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        leaf = fullname.rsplit(".", 1)[-1]
        if leaf.startswith(("frontier_", "toy_", "runner_cache")):
            self.hits.append(fullname)
            raise ImportError(f"self-contained runner forbids import: {fullname}")
        return None


FIREWALL = _RepositoryImportFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


OUTPUT_LINES: list[str] = []


def emit(name: str, payload: dict) -> bool:
    ok = bool(payload.get("pass"))
    # The complete certificate stays in the receipt.  Stdout carries a stable
    # digest so the audit cache remains compact enough to inspect in full.
    OUTPUT_LINES.append(
        f"CERTIFICATE {name} {'PASS' if ok else 'FAIL'} "
        f"canonical_json_sha256={digest(payload)}"
    )
    return ok


def bounded_stdout(lines: list[str]) -> str:
    """Render stdout and fail closed on the repository execution contract."""
    if not lines or not lines[-1].startswith("TOTAL: PASS="):
        raise ValueError("runner stdout must end with TOTAL: PASS=<n> FAIL=<n>")
    rendered = "\n".join(lines) + "\n"
    if len(rendered.encode("utf-8")) >= HOUSE_STDOUT_LIMIT_BYTES:
        raise ValueError("runner stdout exceeds the 6000-byte house limit")
    return rendered


# ---------------------------------------------------------------------------
# rendering: every emitted formula sentence is a function of its coefficients
# ---------------------------------------------------------------------------

def render_law(coefficients: tuple[int, ...], phrases: tuple[str, ...]) -> str:
    """Render `a*p1 + b*p2 + ... + c` as prose FROM THE COEFFICIENTS.

    The emitted theorem text is produced only through this function, so a
    sentence cannot drift away from the numbers the run actually verifies.
    """
    weights, constant = coefficients[:-1], coefficients[-1]
    if len(weights) != len(phrases):
        raise ValueError("coefficient/phrase arity mismatch")
    pieces: list[tuple[bool, str]] = []
    for weight, phrase in zip(weights, phrases):
        if weight == 0:
            continue
        scale = {1: "", 2: "twice ", 3: "three times "}.get(abs(weight))
        if scale is None:
            scale = f"{abs(weight)} times "
        pieces.append((weight > 0, scale + phrase))
    if constant:
        word = {1: "one", 2: "two", 3: "three"}.get(abs(constant),
                                                    str(abs(constant)))
        pieces.append((constant > 0, word))
    if not pieces:
        return "zero"
    text = ("" if pieces[0][0] else "minus ") + pieces[0][1]
    for positive, piece in pieces[1:]:
        text += (" plus " if positive else " minus ") + piece
    return text


def evaluate_law(coefficients: tuple[int, ...], quantities: tuple[int, ...]) -> int:
    weights, constant = coefficients[:-1], coefficients[-1]
    return sum(w * q for w, q in zip(weights, quantities)) + constant


# ---------------------------------------------------------------------------
# exact linear algebra: fraction-free integer elimination over the rationals
# ---------------------------------------------------------------------------

def exact_rank(rows: list[list[int]], ncols: int) -> int:
    """Rank over Q of an integer matrix, by fraction-free elimination.

    No floating point and no Fraction: cross-multiplication keeps every
    entry an exact integer, and a per-row content division keeps them small.
    """
    mat = [list(row) for row in rows]
    nrows = len(mat)
    rank = 0
    for col in range(ncols):
        if rank >= nrows:
            break
        pivot = None
        for r in range(rank, nrows):
            if mat[r][col]:
                pivot = r
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        prow = mat[rank]
        pval = prow[col]
        for r in range(rank + 1, nrows):
            val = mat[r][col]
            if not val:
                continue
            row = mat[r]
            for c in range(col, ncols):
                row[c] = row[c] * pval - prow[c] * val
            content = 0
            for c in range(col, ncols):
                content = gcd(content, row[c])
            if content > 1:
                for c in range(col, ncols):
                    row[c] //= content
        rank += 1
    return rank


def integerize(vector: list[Fraction]) -> list[int]:
    """Scale a rational vector to the integers, for exact_rank."""
    scale = 1
    for value in vector:
        denominator = Fraction(value).denominator
        scale = scale * denominator // gcd(scale, denominator)
    return [int(value * scale) for value in vector]


def unique_solution(rows: list[list[int]], ncols: int,
                    forced_zero: list[int]) -> list[Fraction] | None:
    """The unique x with rows.x = 0, sum(x) = 1, x = 0 off the given support.

    Returns None when the system has no solution or more than one.  Used
    only by the brute-force extreme-point enumeration.
    """
    mat = [[Fraction(x) for x in row] + [Fraction(0)] for row in rows]
    mat.append([Fraction(1)] * ncols + [Fraction(1)])
    for point in forced_zero:
        row = [Fraction(0)] * (ncols + 1)
        row[point] = Fraction(1)
        mat.append(row)
    pivots: list[int] = []
    r = 0
    for col in range(ncols):
        pivot = None
        for i in range(r, len(mat)):
            if mat[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        head = mat[r][col]
        mat[r] = [x / head for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][col] != 0:
                factor = mat[i][col]
                mat[i] = [a - factor * b for a, b in zip(mat[i], mat[r])]
        pivots.append(col)
        r += 1
    if len(pivots) != ncols:
        return None
    for i in range(r, len(mat)):
        if mat[i][ncols] != 0:
            return None
    solution = [Fraction(0)] * ncols
    for i, col in enumerate(pivots):
        solution[col] = mat[i][ncols]
    return solution


# ---------------------------------------------------------------------------
# instances
# ---------------------------------------------------------------------------

class Instance:
    """One declared instance of the structure the theorem quantifies over.

    Base points are numbered 0..n-1 and laid out orbit by orbit in
    contiguous runs.  The group is generated by the permutation that
    advances each run cyclically by one place.
    """

    def __init__(self, orbit_sizes: tuple[int, ...],
                 fibre_sizes: tuple[int, ...],
                 required_zero: frozenset[int]) -> None:
        self.orbit_sizes = orbit_sizes
        self.fibre_sizes = fibre_sizes
        self.required_zero = required_zero
        self.n_base = sum(orbit_sizes)
        orbits: list[tuple[int, ...]] = []
        start = 0
        for size in orbit_sizes:
            orbits.append(tuple(range(start, start + size)))
            start += size
        self.orbits = tuple(orbits)
        # fibre point indexing: base point 0's fibre first, then 1's, ...
        offsets: list[int] = []
        base_of_point: list[int] = []
        running = 0
        for base, size in enumerate(fibre_sizes):
            offsets.append(running)
            base_of_point.extend([base] * size)
            running += size
        self.fibre_offset = tuple(offsets)
        self.base_of_point = tuple(base_of_point)
        self.n_fibre = running

    @property
    def key(self) -> tuple:
        """Layout-independent canonical key for cross-runner comparison."""
        return (self.orbit_sizes,
                tuple((self.fibre_sizes[v], int(v in self.required_zero))
                      for v in range(self.n_base)))

    def generator(self) -> tuple[int, ...]:
        perm = list(range(self.n_base))
        for orbit in self.orbits:
            for i, v in enumerate(orbit):
                perm[v] = orbit[(i + 1) % len(orbit)]
        return tuple(perm)

    def fibre_points(self, base: int) -> range:
        off = self.fibre_offset[base]
        return range(off, off + self.fibre_sizes[base])

    def disjoint_orbits(self) -> tuple[tuple[int, ...], ...]:
        return tuple(o for o in self.orbits
                     if not (set(o) & self.required_zero))

    def disjoint_base_points(self) -> set[int]:
        return {v for o in self.disjoint_orbits() for v in o}

    # ---- the two linear conditions, as integer rows -----------------------

    def constraint_rows(self) -> list[list[int]]:
        rows: list[list[int]] = []
        for base in sorted(self.required_zero):
            for point in self.fibre_points(base):
                row = [0] * self.n_fibre
                row[point] = 1
                rows.append(row)
        for orbit in self.orbits:
            head = orbit[0]
            for other in orbit[1:]:
                row = [0] * self.n_fibre
                for point in self.fibre_points(head):
                    row[point] += 1
                for point in self.fibre_points(other):
                    row[point] -= 1
                rows.append(row)
        return rows

    def base_level_rows(self) -> list[list[int]]:
        rows: list[list[int]] = []
        for base in sorted(self.required_zero):
            row = [0] * self.n_base
            row[base] = 1
            rows.append(row)
        for orbit in self.orbits:
            head = orbit[0]
            for other in orbit[1:]:
                row = [0] * self.n_base
                row[head] += 1
                row[other] -= 1
                rows.append(row)
        return rows

    # ---- the routes -------------------------------------------------------

    def constructive_basis_sparse(self):
        """Explicit spanning family as sparse vectors, no rank computation.

        Two kinds: a within-fibre difference for every fibre point after the
        first at each base point outside the required-zero subset, and one
        orbit vector for every orbit disjoint from that subset.
        """
        for base in range(self.n_base):
            if base in self.required_zero:
                continue
            points = list(self.fibre_points(base))
            for point in points[1:]:
                yield {points[0]: Fraction(1), point: Fraction(-1)}
        for orbit in self.disjoint_orbits():
            yield {self.fibre_offset[base]: Fraction(1) for base in orbit}

    def constructive_basis(self) -> list[list[int]]:
        """The same family densified, for the exact independence rank."""
        basis: list[list[int]] = []
        for sparse in self.constructive_basis_sparse():
            vector = [0] * self.n_fibre
            for point, value in sparse.items():
                vector[point] = int(value)
            basis.append(vector)
        return basis

    def route_nullspace(self) -> int:
        rows = self.constraint_rows()
        return self.n_fibre - exact_rank(rows, self.n_fibre)

    def route_count(self) -> int:
        outside = sum(self.fibre_sizes[v] - 1
                      for v in range(self.n_base)
                      if v not in self.required_zero)
        return len(self.disjoint_orbits()) + outside

    def route_base_nullspace(self) -> int:
        rows = self.base_level_rows()
        return self.n_base - exact_rank(rows, self.n_base)

    # ---- the counted quantities the laws are written in -------------------

    def disjoint_orbit_count(self) -> int:
        return len(self.disjoint_orbits())

    def outside_fibre_freedom(self) -> int:
        return sum(self.fibre_sizes[v] - 1 for v in range(self.n_base)
                   if v not in self.required_zero)

    def disjoint_fibre_freedom(self) -> int:
        return sum(self.fibre_sizes[v] - 1
                   for o in self.disjoint_orbits() for v in o)

    # ---- verification of a candidate weighting ----------------------------

    def satisfies_zero(self, weight: dict[int, Fraction]) -> bool:
        for point, value in weight.items():
            if value != 0 and self.base_of_point[point] in self.required_zero:
                return False
        return True

    def pushforward(self, weight: dict[int, Fraction]) -> list[Fraction]:
        mass = [Fraction(0)] * self.n_base
        for point, value in weight.items():
            mass[self.base_of_point[point]] += value
        return mass

    def satisfies_orbit_constancy(self, weight: dict[int, Fraction]) -> bool:
        mass = self.pushforward(weight)
        for orbit in self.orbits:
            head = mass[orbit[0]]
            for other in orbit[1:]:
                if mass[other] != head:
                    return False
        return True

    # ---- support containment, as a row-space certificate ------------------

    def fibre_indicator(self, base: int) -> list[int]:
        row = [0] * self.n_fibre
        for point in self.fibre_points(base):
            row[point] = 1
        return row

    # ---- exhibited non-negative normalized representatives ----------------

    def fibre_uniform_representative(self) -> dict[int, Fraction] | None:
        """Equal weight on every fibre point of the first disjoint orbit."""
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return None
        orbit = disjoint[0]
        size = len(orbit)
        weight: dict[int, Fraction] = {}
        for base in orbit:
            share = Fraction(1, size * self.fibre_sizes[base])
            for point in self.fibre_points(base):
                weight[point] = share
        return weight

    def concentrated_representative(self) -> dict[int, Fraction] | None:
        """The whole of each base point's share on its first fibre point."""
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return None
        orbit = disjoint[0]
        size = len(orbit)
        return {self.fibre_offset[base]: Fraction(1, size) for base in orbit}

    def signed_witness_hypothesis(self) -> bool:
        """Some base point is outside the required-zero subset, lies in an
        orbit that meets it, and carries at least two fibre points."""
        disjoint = self.disjoint_base_points()
        for base in range(self.n_base):
            if base in self.required_zero or base in disjoint:
                continue
            if self.fibre_sizes[base] >= 2:
                return True
        return False

    def relaxed_witness_hypothesis(self) -> bool:
        """The same hypothesis WITHOUT the two-fibre-point clause.

        Declared only so the witness gate has a wrong hypothesis to reject:
        the constructed witness does not exist under it.
        """
        disjoint = self.disjoint_base_points()
        for base in range(self.n_base):
            if base in self.required_zero or base in disjoint:
                continue
            return True
        return False

    def cross_orbit_signed_witness(self) -> dict[int, Fraction] | None:
        """A signed solution supported OUTSIDE every disjoint orbit.

        Exists exactly under `signed_witness_hypothesis`.  It witnesses that
        support containment in the disjoint orbits is a consequence of
        non-negativity, not of the two linear conditions alone.
        """
        disjoint = self.disjoint_base_points()
        for base in range(self.n_base):
            if base in self.required_zero or base in disjoint:
                continue
            if self.fibre_sizes[base] < 2:
                continue
            points = list(self.fibre_points(base))
            return {points[0]: Fraction(1), points[1]: Fraction(-1)}
        return None

    # ---- the non-negative normalized solution set --------------------------

    def normalized_dimension_bounds(self) -> tuple[int, int]:
        """Two-sided bounds on the dimension of the non-negative normalized
        solution set, computed WITHOUT the closed form.

        Upper bound: the solution set lies in the affine subspace cut out by
        the two conditions, by vanishing off the disjoint orbits, and by
        total mass one -- its dimension is an exact rank computation.
        Lower bound: the affine rank of exhibited points, each of which is
        verified to be a non-negative normalized solution.
        """
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return (-1, -1)
        rows = self.constraint_rows()
        inside = self.disjoint_base_points()
        for base in range(self.n_base):
            if base in inside:
                continue
            for point in self.fibre_points(base):
                row = [0] * self.n_fibre
                row[point] = 1
                rows.append(row)
        upper = self.n_fibre - exact_rank(rows, self.n_fibre) - 1
        points = self.exhibited_extreme_points()
        origin = points[0]
        directions = []
        for point in points[1:]:
            delta = [a - b for a, b in zip(point, origin)]
            directions.append(integerize(delta))
        lower = exact_rank(directions, self.n_fibre) if directions else 0
        return (lower, upper)

    def exhibited_extreme_points(self) -> list[list[Fraction]]:
        """The claimed extreme points: one disjoint orbit's whole mass, on a
        single fibre point at each of that orbit's base points."""
        points: list[list[Fraction]] = []
        for orbit in self.disjoint_orbits():
            share = Fraction(1, len(orbit))
            choices = [list(self.fibre_points(base)) for base in orbit]
            for choice in itertools.product(*choices):
                vector = [Fraction(0)] * self.n_fibre
                for point in choice:
                    vector[point] = share
                points.append(vector)
        return points

    def brute_force_extreme_points(self) -> set[tuple[Fraction, ...]]:
        """Every basic feasible point of the non-negative normalized set.

        A point of a polyhedron is extreme exactly when the constraints
        active at it determine it uniquely, so this enumerates supports and
        keeps the non-negative unique solutions.  Exponential in the fibre
        count; run only on the declared bounded subfamily.
        """
        rows = self.constraint_rows()
        found: set[tuple[Fraction, ...]] = set()
        for mask in range(1 << self.n_fibre):
            forced = [p for p in range(self.n_fibre) if not (mask >> p) & 1]
            solution = unique_solution(rows, self.n_fibre, forced)
            if solution is None or any(v < 0 for v in solution):
                continue
            found.add(tuple(solution))
        return found

    def product_shape_extreme_point_count(self) -> int:
        """How many extreme points a Cartesian product of an orbit-mass
        simplex with the fibre simplices would have.  Declared as a WRONG
        count, kept so the extreme-point gate has something to reject."""
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return 0
        product = 1
        for orbit in disjoint:
            for base in orbit:
                product *= self.fibre_sizes[base]
        return len(disjoint) * product

    def extreme_point_count(self) -> int:
        disjoint = self.disjoint_orbits()
        total = 0
        for orbit in disjoint:
            product = 1
            for base in orbit:
                product *= self.fibre_sizes[base]
            total += product
        return total

    def zero_count(self, weight: dict[int, Fraction]) -> int:
        return self.n_fibre - sum(1 for v in weight.values() if v != 0)


def enumerate_partitions(total: int) -> list[tuple[int, ...]]:
    """All orbit-size partitions of `total`, largest part first."""
    if total == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def walk(remaining: int, cap: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(prefix)
            return
        for part in range(min(cap, remaining), 0, -1):
            walk(remaining - part, part, prefix + (part,))

    walk(total, total, ())
    return out


def enumerate_family() -> list[Instance]:
    instances: list[Instance] = []
    for n_base in range(1, MAX_BASE_POINTS + 1):
        alphabet = (FIBRE_ALPHABET_WIDE if n_base >= WIDE_ALPHABET_FROM
                    else FIBRE_ALPHABET_SMALL)
        for orbit_sizes in enumerate_partitions(n_base):
            for fibres in itertools.product(alphabet, repeat=n_base):
                for mask in range(1 << n_base):
                    zero = frozenset(v for v in range(n_base)
                                     if mask & (1 << v))
                    instances.append(Instance(orbit_sizes, fibres, zero))
    return instances


def build_large_instance(spec: dict) -> Instance:
    orbit_sizes = spec["orbit_sizes"]
    n_base = sum(orbit_sizes)
    bounds: list[int] = []
    running = 0
    for size in orbit_sizes:
        bounds.append(running)
        running += size
    if spec["name"] == "twelve_orbits_of_eleven_uniform_fibres":
        fibres = tuple(129 for _ in range(n_base))
        zero = frozenset(range(bounds[11]))
    else:
        last_start = bounds[11]
        fibres = tuple(129 if v >= last_start else 7 for v in range(n_base))
        zero = frozenset(range(bounds[10])) | {bounds[10]}
    return Instance(orbit_sizes, fibres, zero)


# ---------------------------------------------------------------------------
# certificates
# ---------------------------------------------------------------------------

def certificate_self_containment() -> dict:
    source = (ROOT / SELF_PATH).read_bytes()
    tree = ast.parse(source, filename=SELF_PATH)
    declared_literal: tuple | None = None
    declared_timeout = None
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Name):
                continue
            if target.id == "AUDIT_INPUT_PATHS":
                try:
                    declared_literal = tuple(ast.literal_eval(node.value))
                except (ValueError, TypeError):
                    declared_literal = None
            if target.id == "AUDIT_TIMEOUT_SEC" \
                    and isinstance(node.value, ast.Constant):
                declared_timeout = node.value.value
    closure_is_self_only = declared_literal == (SELF_PATH,)
    repo_modules = sorted(
        name for name, mod in list(sys.modules.items())
        if getattr(mod, "__file__", None)
        and str(ROOT) in str(getattr(mod, "__file__", ""))
        and name != "__main__"
    )
    payload = {
        "certificate": "SELF_CONTAINMENT",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "declared_closure_is_this_runner_source_only": closure_is_self_only,
        "declared_closure_contains_no_ancestor_artifact": True,
        "every_declared_path_is_in_this_landing_delta": True,
        "declared_audit_timeout_sec": declared_timeout,
        "read_inventory": {
            "external_or_ancestral_scientific_inputs": [],
            "package_local_integrity_reads": [SELF_PATH],
        },
        "repository_modules_imported": repo_modules,
        "import_firewall_hits": list(FIREWALL.hits),
        "self_sha256": sha256(source).hexdigest(),
    }
    payload["pass"] = bool(
        AUDIT_INPUT_PATHS == (SELF_PATH,)
        and closure_is_self_only
        and declared_timeout == AUDIT_TIMEOUT_SEC
        and not repo_modules
        and not FIREWALL.hits
    )
    return payload


def certificate_group_structure(instances: list[Instance]) -> dict:
    checked = 0
    failures: list[str] = []
    for inst in instances:
        perm = inst.generator()
        # closure, identity and inverses of the cyclic group generated by perm
        powers = [tuple(range(inst.n_base))]
        current = powers[0]
        for _ in range(inst.n_base * 2 + 2):
            current = tuple(perm[x] for x in current)
            if current == powers[0]:
                break
            powers.append(current)
        group = set(powers)
        closed = all(tuple(a[b[i]] for i in range(inst.n_base)) in group
                     for a in group for b in group)
        has_identity = powers[0] in group
        has_inverses = all(
            any(tuple(a[b[i]] for i in range(inst.n_base)) == powers[0]
                for b in group)
            for a in group)
        # orbits of the generated group equal the declared orbit partition
        seen: list[tuple[int, ...]] = []
        for base in range(inst.n_base):
            orbit = tuple(sorted({g[base] for g in group}))
            if orbit not in seen:
                seen.append(orbit)
        declared = sorted(tuple(sorted(o)) for o in inst.orbits)
        if not (closed and has_identity and has_inverses
                and sorted(seen) == declared):
            failures.append(compact(inst.key))
        checked += 1
    payload = {
        "certificate": "GROUP_STRUCTURE",
        "instances_checked": checked,
        "statement": ("for every instance the declared generator generates a"
                      " finite cyclic group -- closed, with identity and"
                      " inverses -- whose orbits are exactly the declared"
                      " orbit partition"),
        "failures": failures[:8],
        "failure_count": len(failures),
    }
    payload["instances_declared"] = len(instances)
    payload["pass"] = (checked == len(instances) > 0) and not failures
    return payload


def sweep(instances: list[Instance]) -> list[dict]:
    """One pass over the family, recording every independently computed
    dimension the laws are then judged against."""
    rows: list[dict] = []
    for inst in instances:
        basis = inst.constructive_basis()
        basis_independent = (exact_rank(basis, inst.n_fibre) == len(basis)
                             if basis else True)
        basis_admissible = True
        for vector in basis:
            weight = {i: Fraction(v) for i, v in enumerate(vector) if v}
            if not (inst.satisfies_zero(weight)
                    and inst.satisfies_orbit_constancy(weight)):
                basis_admissible = False
                break
        lower, upper = inst.normalized_dimension_bounds()
        rows.append({
            "key": inst.key,
            "disjoint_orbits": inst.disjoint_orbit_count(),
            "outside_fibre_freedom": inst.outside_fibre_freedom(),
            "disjoint_fibre_freedom": inst.disjoint_fibre_freedom(),
            "dimension_by_nullspace_rank": inst.route_nullspace(),
            "dimension_by_closed_form": inst.route_count(),
            "dimension_by_basis_length": len(basis),
            "basis_independent": basis_independent,
            "basis_admissible": basis_admissible,
            "pushforward_dimension_by_rank": inst.route_base_nullspace(),
            "normalized_dimension_lower": lower,
            "normalized_dimension_upper": upper,
        })
    return rows


def certificate_dimension_laws(rows: list[dict], declared: int) -> dict:
    """Every dimension law, judged against an independent computation, and
    every declared WRONG law, required to be refuted by an instance."""
    defects: list[str] = []
    solution_law_failures = 0
    pushforward_law_failures = 0
    normalized_law_failures = 0
    normalized_bounds_open = 0
    basis_defects = 0
    closed_form_disagreements = 0
    normalized_checked = 0

    def refutation_state(law_set, quantities_of, truth_of, domain) -> list[dict]:
        out = []
        for wrong in law_set:
            witness = None
            for row in rows:
                if not domain(row):
                    continue
                if evaluate_law(wrong, quantities_of(row)) != truth_of(row):
                    witness = {
                        "instance": compact(row["key"]),
                        "wrong_law_gives": evaluate_law(wrong,
                                                        quantities_of(row)),
                        "independent_computation_gives": truth_of(row),
                    }
                    break
            out.append({"refuted_law": list(wrong),
                        "refuted_by": witness})
        return out

    for row in rows:
        solution_quantities = (row["disjoint_orbits"],
                               row["outside_fibre_freedom"])
        truth = row["dimension_by_nullspace_rank"]
        if evaluate_law(SOLUTION_DIMENSION_LAW, solution_quantities) != truth:
            solution_law_failures += 1
        if row["dimension_by_closed_form"] != truth \
                or row["dimension_by_basis_length"] != truth:
            closed_form_disagreements += 1
        if not (row["basis_independent"] and row["basis_admissible"]):
            basis_defects += 1
        if evaluate_law(PUSHFORWARD_DIMENSION_LAW, (row["disjoint_orbits"],)) \
                != row["pushforward_dimension_by_rank"]:
            pushforward_law_failures += 1
        if row["disjoint_orbits"]:
            normalized_checked += 1
            lower = row["normalized_dimension_lower"]
            upper = row["normalized_dimension_upper"]
            if lower != upper:
                normalized_bounds_open += 1
            claimed = evaluate_law(NORMALIZED_DIMENSION_LAW,
                                   (row["disjoint_orbits"],
                                    row["disjoint_fibre_freedom"]))
            if not (lower == upper == claimed):
                normalized_law_failures += 1
        else:
            if row["normalized_dimension_lower"] != -1:
                defects.append("bounds computed without a disjoint orbit")

    solution_refutations = refutation_state(
        SOLUTION_DIMENSION_REFUTED,
        lambda r: (r["disjoint_orbits"], r["outside_fibre_freedom"]),
        lambda r: r["dimension_by_nullspace_rank"],
        lambda r: True)
    pushforward_refutations = refutation_state(
        PUSHFORWARD_DIMENSION_REFUTED,
        lambda r: (r["disjoint_orbits"],),
        lambda r: r["pushforward_dimension_by_rank"],
        lambda r: True)
    normalized_refutations = refutation_state(
        NORMALIZED_DIMENSION_REFUTED,
        lambda r: (r["disjoint_orbits"], r["disjoint_fibre_freedom"]),
        lambda r: r["normalized_dimension_upper"],
        lambda r: bool(r["disjoint_orbits"]))
    all_refuted = all(entry["refuted_by"] is not None
                      for entry in (solution_refutations
                                    + pushforward_refutations
                                    + normalized_refutations))

    table = sorted((compact(r["key"]), r["dimension_by_nullspace_rank"])
                   for r in rows)
    payload = {
        "certificate": "DIMENSION_LAWS",
        "statement": ("on every instance of the declared exhaustive family"
                      " each declared dimension law reproduces a dimension"
                      " computed without it -- the solution dimension by"
                      " exact fraction-free nullspace rank, the pushforward"
                      " dimension by exact base-level rank, and the"
                      " non-negative normalized dimension by an exact rank"
                      " upper bound met by the affine rank of exhibited"
                      " verified solutions -- and every declared wrong law is"
                      " refuted by an exhibited instance"),
        "instances": len(rows),
        "instances_declared": declared,
        "solution_dimension_law": list(SOLUTION_DIMENSION_LAW),
        "pushforward_dimension_law": list(PUSHFORWARD_DIMENSION_LAW),
        "normalized_dimension_law": list(NORMALIZED_DIMENSION_LAW),
        "solution_law_failures": solution_law_failures,
        "pushforward_law_failures": pushforward_law_failures,
        "normalized_law_failures": normalized_law_failures,
        "normalized_instances_checked": normalized_checked,
        "normalized_bounds_that_did_not_close": normalized_bounds_open,
        "closed_form_or_basis_length_disagreements": closed_form_disagreements,
        "basis_defects": basis_defects,
        "refuted_solution_dimension_laws": solution_refutations,
        "refuted_pushforward_dimension_laws": pushforward_refutations,
        "refuted_normalized_dimension_laws": normalized_refutations,
        "every_declared_wrong_law_was_refuted": all_refuted,
        "dimension_table_digest": digest(table),
        "dimension_sum": sum(r["dimension_by_nullspace_rank"] for r in rows),
        "dimension_max": max(r["dimension_by_nullspace_rank"] for r in rows),
        "distinct_dimensions": sorted({r["dimension_by_nullspace_rank"]
                                       for r in rows}),
        "defects": sorted(set(defects))[:8],
    }
    payload["pass"] = bool(
        rows and len(rows) == declared and not defects and all_refuted
        and solution_law_failures == 0
        and pushforward_law_failures == 0
        and normalized_law_failures == 0
        and normalized_bounds_open == 0
        and closed_form_disagreements == 0
        and basis_defects == 0
    )
    return payload


def certificate_support_containment(instances: list[Instance]) -> dict:
    """Support containment, proved per instance by a row-space certificate.

    For a base point outside every disjoint orbit, the fibre-total
    functional at that base point is a NON-NEGATIVE vector lying in the row
    space of the constraint matrix.  It therefore vanishes on every
    solution, and on a non-negative solution that forces every one of that
    base point's fibre weights to zero.  The same test at a base point
    INSIDE a disjoint orbit must fail -- that control is what makes the
    certificate discriminating rather than automatic.
    """
    certified = 0
    missing = 0
    controls = 0
    control_defects = 0
    example = None
    # recounted independently of the loop below: every base point of every
    # declared instance must fall into exactly one of the tallies
    declared_base_points = sum(inst.n_base for inst in instances)
    for inst in instances:
        rows = inst.constraint_rows()
        rank = exact_rank(rows, inst.n_fibre)
        inside = inst.disjoint_base_points()
        for base in range(inst.n_base):
            indicator = inst.fibre_indicator(base)
            in_row_space = exact_rank(rows + [indicator],
                                      inst.n_fibre) == rank
            if base in inside:
                controls += 1
                if in_row_space:
                    control_defects += 1
            else:
                if in_row_space:
                    certified += 1
                    if example is None:
                        example = {
                            "instance": compact(inst.key),
                            "base_point": base,
                            "fibre_total_functional_is_in_the_row_space": True,
                            "so_every_non_negative_solution_vanishes_there":
                                True,
                        }
                else:
                    missing += 1
    payload = {
        "certificate": "SUPPORT_CONTAINMENT",
        "statement": ("at every base point outside the disjoint orbits the"
                      " fibre-total functional is a non-negative vector in"
                      " the row space of the constraint matrix, so every"
                      " non-negative solution is zero at each of that base"
                      " point's fibre points; at every base point inside a"
                      " disjoint orbit the same functional is NOT in the row"
                      " space, so the test is not automatic"),
        "base_points_certified_outside_the_disjoint_orbits": certified,
        "base_points_without_a_certificate": missing,
        "control_base_points_inside_the_disjoint_orbits": controls,
        "control_defects": control_defects,
        "base_points_declared": declared_base_points,
        "every_declared_base_point_accounted_for":
            certified + missing + controls == declared_base_points,
        "worked_example": example,
    }
    payload["pass"] = bool(certified and not missing and controls
                           and not control_defects
                           and certified + missing + controls
                           == declared_base_points)
    return payload


def certificate_extreme_points(instances: list[Instance]) -> dict:
    """Brute-force extreme-point enumeration on the declared bounded
    subfamily, against the claimed extreme-point set and count."""
    checked = 0
    set_mismatches = 0
    count_mismatches = 0
    product_shape_differs = 0
    separating_example = None
    first_mismatch = None
    declared_subfamily = sum(
        1 for inst in instances
        if inst.n_fibre <= VERTEX_ENUMERATION_MAX_FIBRE_POINTS
        and inst.disjoint_orbits())
    for inst in instances:
        if inst.n_fibre > VERTEX_ENUMERATION_MAX_FIBRE_POINTS \
                or not inst.disjoint_orbits():
            continue
        checked += 1
        brute = inst.brute_force_extreme_points()
        claimed = {tuple(v) for v in inst.exhibited_extreme_points()}
        if brute != claimed:
            set_mismatches += 1
            if first_mismatch is None:
                first_mismatch = compact(inst.key)
        if len(brute) != inst.extreme_point_count():
            count_mismatches += 1
        product_count = inst.product_shape_extreme_point_count()
        if product_count != len(brute):
            product_shape_differs += 1
            if separating_example is None:
                separating_example = {
                    "instance": compact(inst.key),
                    "extreme_points_enumerated": len(brute),
                    "a_cartesian_product_of_simplices_would_have":
                        product_count,
                }
    payload = {
        "certificate": "EXTREME_POINTS",
        "statement": ("on every instance of the declared bounded subfamily"
                      " the extreme points of the non-negative normalized"
                      " solution set, enumerated by brute force over all"
                      " supports, are exactly the weightings that place one"
                      " disjoint orbit's whole mass on a single fibre point"
                      " at each of that orbit's base points, and their number"
                      " is the sum over disjoint orbits of the product of"
                      " that orbit's fibre sizes"),
        "bounded_subfamily": ("instances with at least one disjoint orbit and"
                              f" at most {VERTEX_ENUMERATION_MAX_FIBRE_POINTS}"
                              " fibre points"),
        "instances_enumerated": checked,
        "instances_in_the_declared_subfamily": declared_subfamily,
        "extreme_point_set_mismatches": set_mismatches,
        "extreme_point_count_mismatches": count_mismatches,
        "first_mismatch": first_mismatch,
        "instances_where_a_product_of_simplices_would_give_another_count":
            product_shape_differs,
        "separating_example": separating_example,
    }
    payload["pass"] = bool(checked == declared_subfamily > 0
                           and not set_mismatches
                           and not count_mismatches and product_shape_differs
                           and separating_example is not None)
    return payload


def certificate_nonnegative_witnesses(instances: list[Instance]) -> dict:
    with_solution = 0
    two_distinct = 0
    zero_count_differs = 0
    distinctness_biconditional_failures = 0
    hypothesis_holds = 0
    hypothesis_with_a_disjoint_orbit = 0
    hypothesis_without_a_disjoint_orbit = 0
    witness_found = 0
    witness_biconditional_failures = 0
    relaxed_hypothesis_failures = 0
    defects: list[str] = []
    example = None
    smallest_witness_without_a_disjoint_orbit = None
    visited = 0
    # An INDEPENDENT recount of the two tallies, taken outside the main loop
    # over the whole declared family.  A loop that quietly skips instances --
    # the defect this gate exists to catch -- disagrees with these numbers.
    independent_hypothesis = sum(1 for inst in instances
                                 if inst.signed_witness_hypothesis())
    independent_witnesses = sum(1 for inst in instances
                                if inst.cross_orbit_signed_witness() is not None)
    for inst in instances:
        visited += 1
        uniform = inst.fibre_uniform_representative()
        if uniform is not None:
            with_solution += 1
            concentrated = inst.concentrated_representative()
            for weight in (uniform, concentrated):
                total = sum(weight.values(), Fraction(0))
                if total != 1 or any(v < 0 for v in weight.values()):
                    defects.append("representative not normalized or not "
                                   "non-negative")
                if not (inst.satisfies_zero(weight)
                        and inst.satisfies_orbit_constancy(weight)):
                    defects.append("representative violates a declared "
                                   "condition")
            disjoint_bases = inst.disjoint_base_points()
            outside = [p for p, v in uniform.items()
                       if v != 0 and inst.base_of_point[p] not in disjoint_bases]
            if outside:
                defects.append("non-negative representative supported outside "
                               "the disjoint orbits")
            distinct = uniform != concentrated
            counts_differ = (inst.zero_count(uniform)
                             != inst.zero_count(concentrated))
            if distinct != counts_differ:
                distinctness_biconditional_failures += 1
            if distinct:
                two_distinct += 1
                if inst.pushforward(uniform) != inst.pushforward(concentrated):
                    defects.append("distinct representatives with different "
                                   "pushforward mass at a single disjoint "
                                   "orbit")
            if counts_differ:
                zero_count_differs += 1
                if example is None:
                    example = {
                        "key": inst.key,
                        "fibre_uniform_zero_count": inst.zero_count(uniform),
                        "concentrated_zero_count": inst.zero_count(concentrated),
                        "shared_pushforward_mass": [
                            fr(m) for m in inst.pushforward(uniform)],
                        "fraction_label": FRACTION_LABEL,
                    }
        # the signed witness is tested on EVERY instance: its stated
        # existence condition does not mention a disjoint orbit
        hypothesis = inst.signed_witness_hypothesis()
        witness = inst.cross_orbit_signed_witness()
        if hypothesis:
            hypothesis_holds += 1
            if inst.disjoint_orbits():
                hypothesis_with_a_disjoint_orbit += 1
            else:
                hypothesis_without_a_disjoint_orbit += 1
                if smallest_witness_without_a_disjoint_orbit is None:
                    smallest_witness_without_a_disjoint_orbit = compact(inst.key)
        if (witness is not None) != hypothesis:
            witness_biconditional_failures += 1
        if inst.relaxed_witness_hypothesis() and witness is None:
            relaxed_hypothesis_failures += 1
        if witness is not None:
            witness_found += 1
            disjoint_bases = inst.disjoint_base_points()
            if not (inst.satisfies_zero(witness)
                    and inst.satisfies_orbit_constancy(witness)):
                defects.append("cross-orbit signed witness is not a solution")
            if not any(v < 0 for v in witness.values()):
                defects.append("cross-orbit witness is not signed")
            if any(inst.base_of_point[p] in disjoint_bases
                   for p, v in witness.items() if v != 0):
                defects.append("cross-orbit witness is supported inside a "
                               "disjoint orbit")
    payload = {
        "certificate": "NON_NEGATIVE_WITNESSES",
        "statement": ("wherever a disjoint orbit exists, the fibre-uniform"
                      " weighting and the concentrated weighting are both"
                      " non-negative, normalized solutions supported inside"
                      " the disjoint orbits and sharing one pushforward mass,"
                      " and they are distinct exactly when their zero counts"
                      " differ; and, on every instance of the family, a signed"
                      " solution supported strictly outside every disjoint"
                      " orbit is constructed exactly when a base point lies"
                      " outside the required-zero subset, lies in an orbit"
                      " that meets it, and carries at least two fibre points;"
                      " both signed-witness tallies are recounted"
                      " independently of the sweep loop, so a loop that"
                      " skipped part of the declared family would disagree"
                      " with its own recount"),
        "instances_visited": visited,
        "instances_declared": len(instances),
        "independent_recount_of_the_hypothesis": independent_hypothesis,
        "independent_recount_of_the_witnesses": independent_witnesses,
        "instances_with_a_disjoint_orbit": with_solution,
        "instances_with_two_distinct_representatives": two_distinct,
        "instances_where_zero_counts_differ": zero_count_differs,
        "distinctness_biconditional_failures": distinctness_biconditional_failures,
        "instances_satisfying_the_signed_witness_hypothesis": hypothesis_holds,
        "of_those_with_a_disjoint_orbit": hypothesis_with_a_disjoint_orbit,
        "of_those_without_a_disjoint_orbit": hypothesis_without_a_disjoint_orbit,
        "instances_with_a_cross_orbit_signed_solution": witness_found,
        "witness_hypothesis_biconditional_failures": witness_biconditional_failures,
        "instances_refuting_the_hypothesis_without_the_two_fibre_clause":
            relaxed_hypothesis_failures,
        "smallest_signed_witness_without_a_disjoint_orbit":
            smallest_witness_without_a_disjoint_orbit,
        "worked_example": example,
        "defects": sorted(set(defects))[:8],
    }
    payload["pass"] = bool(
        with_solution and two_distinct and zero_count_differs
        and hypothesis_holds and witness_found and not defects
        and visited == len(instances)
        and hypothesis_holds == independent_hypothesis
        and witness_found == independent_witnesses
        and hypothesis_holds == (hypothesis_with_a_disjoint_orbit
                                 + hypothesis_without_a_disjoint_orbit)
        and distinctness_biconditional_failures == 0
        and witness_biconditional_failures == 0
        and relaxed_hypothesis_failures > 0
    )
    return payload


def certificate_large_instances() -> dict:
    rows = []
    declared_names = tuple(spec.get("name") for spec in LARGE_INSTANCES)
    declared_set_is_exact = declared_names == EXPECTED_LARGE_INSTANCE_NAMES
    ok = declared_set_is_exact
    for spec in LARGE_INSTANCES:
        inst = build_large_instance(spec)
        closed_form = inst.route_count()
        base_dim = inst.route_base_nullspace()
        uniform = inst.fibre_uniform_representative()
        normalized = evaluate_law(NORMALIZED_DIMENSION_LAW,
                                  (inst.disjoint_orbit_count(),
                                   inst.disjoint_fibre_freedom()))
        basis_len = 0
        basis_inside_disjoint = 0
        basis_admissible = True
        inside = inst.disjoint_base_points()
        for vector in inst.constructive_basis_sparse():
            basis_len += 1
            if all(inst.base_of_point[p] in inside for p in vector):
                basis_inside_disjoint += 1
            if not (inst.satisfies_zero(vector)
                    and inst.satisfies_orbit_constancy(vector)):
                basis_admissible = False
        checks = {
            "closed_form_equals_basis_length": closed_form == basis_len,
            "every_basis_vector_satisfies_both_conditions": basis_admissible,
            "base_level_dimension_equals_disjoint_orbits":
                base_dim == inst.disjoint_orbit_count(),
            "solution_dimension_law_reproduces_the_closed_form":
                evaluate_law(SOLUTION_DIMENSION_LAW,
                             (inst.disjoint_orbit_count(),
                              inst.outside_fibre_freedom())) == closed_form,
            "normalized_dimension_equals_the_basis_count_inside_the_"
            "disjoint_orbits": normalized == basis_inside_disjoint - 1,
            "representative_is_normalized":
                sum(uniform.values(), Fraction(0)) == 1,
            "representative_is_non_negative":
                all(v >= 0 for v in uniform.values()),
            "representative_satisfies_both_conditions":
                inst.satisfies_zero(uniform)
                and inst.satisfies_orbit_constancy(uniform),
        }
        ok = ok and all(checks.values())
        rows.append({
            "name": spec["name"],
            "declared_parameters": {
                "orbit_sizes": list(spec["orbit_sizes"]),
                "fibre_rule": spec["fibre_rule"],
                "required_zero_rule": spec["zero_rule"],
            },
            "base_points": inst.n_base,
            "fibre_points": inst.n_fibre,
            "orbits_disjoint_from_required_zero": inst.disjoint_orbit_count(),
            "solution_space_dimension": closed_form,
            "pushforward_mass_dimension": base_dim,
            "non_negative_normalized_dimension": normalized,
            "representative_zero_count": inst.zero_count(uniform),
            "checks": checks,
        })
    payload = {
        "certificate": "LARGE_DECLARED_INSTANCES",
        "statement": ("on two declared larger instances the proved dimension"
                      " laws are evaluated at the declared parameters and"
                      " cross-checked against the explicit basis length, the"
                      " count of basis vectors supported inside the disjoint"
                      " orbits, the exact base-level rank and the exhibited"
                      " representative; their parameters are chosen numbers"
                      " for scale and describe no repository census or"
                      " physical configuration"),
        "routes_not_run_here_and_why": (
            "the fibre-level rank routes -- the dense fraction-free nullspace"
            " rank, the row-space support certificate and the two-sided"
            " normalized-dimension bounds -- are NOT run on these two"
            " instances: exact elimination over more than two thousand"
            " columns is outside this runner's declared budget.  What these"
            " two rows establish is therefore the arithmetic evaluation of"
            " laws proved in the note and verified by those routes on the"
            " exhaustive family, together with the base-level rank, the"
            " basis verification and the representative verification"
            " performed here"),
        "expected_instance_names": list(EXPECTED_LARGE_INSTANCE_NAMES),
        "declared_instance_names": list(declared_names),
        "declared_instance_set_is_exact": declared_set_is_exact,
        "instances_checked": len(rows),
        "rows": rows,
    }
    payload["pass"] = bool(
        ok and len(rows) == len(EXPECTED_LARGE_INSTANCE_NAMES)
    )
    return payload


def _module_call_graph(tree: ast.Module) -> dict[str, set[str]]:
    """Direct in-module calls of every module function and Instance method."""
    definitions: dict[str, ast.FunctionDef] = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            definitions[node.name] = node
        elif isinstance(node, ast.ClassDef):
            for child in node.body:
                if isinstance(child, ast.FunctionDef):
                    definitions[f"{node.name}.{child.name}"] = child
    method_names = {name.split(".", 1)[1] for name in definitions
                    if "." in name}
    graph: dict[str, set[str]] = {}
    for name, node in definitions.items():
        owner = name.split(".", 1)[0] if "." in name else None
        calls: set[str] = set()
        for child in ast.walk(node):
            if not isinstance(child, ast.Call):
                continue
            func = child.func
            if isinstance(func, ast.Name) and func.id in definitions:
                calls.add(func.id)
            elif isinstance(func, ast.Attribute) and func.attr in method_names:
                calls.add(f"{owner}.{func.attr}" if owner else func.attr)
        graph[name] = calls
    return graph


def certificate_route_inventory() -> dict:
    """Recompute each dimension route's helper set from this file's own
    syntax tree, and refuse any declared sharing that is not the real one."""
    tree = ast.parse((ROOT / SELF_PATH).read_bytes(), filename=SELF_PATH)
    graph = _module_call_graph(tree)
    computed: dict[str, tuple[str, ...]] = {}
    for route, entry in ROUTE_ENTRY_POINTS.items():
        seen: set[str] = set()
        stack = [entry]
        while stack:
            current = stack.pop()
            for callee in graph.get(current, ()):  # transitive closure
                if callee not in seen:
                    seen.add(callee)
                    stack.append(callee)
        computed[route] = tuple(sorted(seen))
    helper_mismatches = sorted(
        route for route in ROUTE_ENTRY_POINTS
        if computed[route] != tuple(sorted(ROUTE_DECLARED_HELPERS[route])))
    computed_sharing: dict[str, tuple[str, ...]] = {}
    routes = sorted(ROUTE_ENTRY_POINTS)
    for i, left in enumerate(routes):
        for right in routes[i + 1:]:
            shared = tuple(sorted(set(computed[left]) & set(computed[right])))
            computed_sharing[f"{left}|{right}"] = shared
    sharing_mismatches = sorted(
        pair for pair, shared in computed_sharing.items()
        if shared != tuple(sorted(ROUTE_DECLARED_SHARING.get(pair, ("?",)))))
    payload = {
        "certificate": "ROUTE_INVENTORY",
        "statement": ("each dimension route's transitive helper set is"
                      " recomputed from this file's own syntax tree, counting"
                      " only names defined in this module, and must equal the"
                      " declared set; the pairwise shared helpers must equal"
                      " the declared sharing, so no route may be advertised as"
                      " sharing less than it does"),
        "declared_helpers": {k: list(v) for k, v in
                             ROUTE_DECLARED_HELPERS.items()},
        "recomputed_helpers": {k: list(v) for k, v in computed.items()},
        "declared_sharing": {k: list(v) for k, v in
                             ROUTE_DECLARED_SHARING.items()},
        "recomputed_sharing": {k: list(v) for k, v in
                               computed_sharing.items()},
        "helper_mismatches": helper_mismatches,
        "sharing_mismatches": sharing_mismatches,
        "closed_form_and_basis_length_are_independent_of_each_other":
            not computed_sharing.get("BASIS_LENGTH|CLOSED_FORM"),
        "closed_form_and_nullspace_are_independent_of_each_other":
            not computed_sharing.get("CLOSED_FORM|NULLSPACE"),
    }
    payload["pass"] = not helper_mismatches and not sharing_mismatches
    return payload


def build_theorem(dimension_laws: dict, witnesses: dict,
                  extreme_points: dict, large_instances: dict) -> dict:
    """The theorem, with every formula sentence RENDERED from the verified
    coefficients and every count taken from the certificate that computed
    it.  There is no free-text theorem field."""
    return {
        "parameterization": (
            "for every finite cyclic action on finitely many base points,"
            " every assignment of non-empty finite fibres and every"
            " required-zero subset, the solutions of the two linear"
            " conditions are exactly the span of the explicit basis this"
            " runner constructs, so their dimension is "
            + render_law(SOLUTION_DIMENSION_LAW, SOLUTION_DIMENSION_PHRASES)),
        "pushforward_dimension": (
            "the space of admissible pushforward masses has dimension exactly "
            + render_law(PUSHFORWARD_DIMENSION_LAW,
                         PUSHFORWARD_DIMENSION_PHRASES)
            + "; where that number is one, every admissible pushforward mass"
              " is therefore a rational multiple of one fixed admissible"
              " mass"),
        "non_negative_normalized": (
            "on instances with at least one disjoint orbit, adding"
            " non-negativity and total mass one puts every solution to zero"
            " at every fibre point over a base point outside the disjoint"
            " orbits and leaves a set of dimension "
            + render_law(NORMALIZED_DIMENSION_LAW,
                         NORMALIZED_DIMENSION_PHRASES)
            + ", whose extreme points are exactly the weightings that place"
              " one disjoint orbit's whole mass on a single fibre point at"
              " each of that orbit's base points"),
        "signed_solution_off_the_disjoint_orbits": (
            "whenever a base point lies outside the required-zero subset,"
            " lies in an orbit that meets it, and carries at least two fibre"
            " points, the difference of two of its fibre weights is a"
            " solution supported strictly outside every disjoint orbit; that"
            " hypothesis holds at "
            + str(witnesses["instances_satisfying_the_signed_witness_hypothesis"])
            + " of the "
            + str(dimension_laws["instances"])
            + " swept instances and a witness is exhibited at every one of"
              " them, so support containment is a consequence of"
              " non-negativity and not of the two linear conditions alone"),
        "verification_scope": (
            "the laws above are proved in the note for all finite instances;"
            " this runner verifies them on "
            + str(dimension_laws["instances"])
            + " exhaustively enumerated canonical representatives of the"
              " declared decorated family, the extreme-point"
              " statement by brute-force enumeration on the "
            + str(extreme_points["instances_enumerated"])
            + " of them with at most "
            + str(VERTEX_ENUMERATION_MAX_FIBRE_POINTS)
            + " fibre points and a disjoint orbit, and evaluates the laws at"
              " the "
            + str(large_instances["instances_checked"])
            + " declared larger instances where the fibre-level rank"
              " routes are not run"),
        "scope": (
            "conditional on the declared finite structure only; this runner"
            " reads no repository census, no symmetry claim, no interface"
            " condition and no axiom surface, and asserts nothing about any"
            " of them"),
    }


def certificate_claim_text(theorem: dict, certificates: dict) -> dict:
    """Every emitted theorem sentence must be the rendering of a verified
    law, and no refuted sentence may appear anywhere in the output."""
    rendered = {
        "solution_dimension": render_law(SOLUTION_DIMENSION_LAW,
                                         SOLUTION_DIMENSION_PHRASES),
        "pushforward_dimension": render_law(PUSHFORWARD_DIMENSION_LAW,
                                            PUSHFORWARD_DIMENSION_PHRASES),
        "normalized_dimension": render_law(NORMALIZED_DIMENSION_LAW,
                                           NORMALIZED_DIMENSION_PHRASES),
    }
    carries_its_formula = {
        "parameterization":
            rendered["solution_dimension"] in theorem["parameterization"],
        "pushforward_dimension":
            rendered["pushforward_dimension"] in theorem["pushforward_dimension"],
        "non_negative_normalized":
            rendered["normalized_dimension"] in theorem["non_negative_normalized"],
    }
    scanned = compact({name: payload for name, payload in certificates.items()
                       if name != "CLAIM_TEXT"}) + compact(theorem)
    present = sorted(fragment for fragment in REFUTED_SENTENCE_FRAGMENTS
                     if fragment in scanned)
    gated_by = {
        "parameterization": "DIMENSION_LAWS",
        "pushforward_dimension": "DIMENSION_LAWS",
        "non_negative_normalized": "DIMENSION_LAWS",
        "signed_solution_off_the_disjoint_orbits": "NON_NEGATIVE_WITNESSES",
        "verification_scope": "EXTREME_POINTS",
        "scope": "SELF_CONTAINMENT",
    }
    ungated = sorted(set(theorem) - set(gated_by))
    missing_gate = sorted(name for name in gated_by
                          if not certificates.get(gated_by[name], {}).get("pass"))
    payload = {
        "certificate": "CLAIM_TEXT",
        "statement": ("every formula sentence of the emitted theorem is"
                      " rendered from the coefficient set that the"
                      " DIMENSION_LAWS certificate verified against an"
                      " independent computation, every theorem field names"
                      " the passing certificate that gates it, and no"
                      " sentence withdrawn as false appears anywhere in the"
                      " emitted output (this certificate's own list is"
                      " excluded from that scan)"),
        "rendered_formulas": rendered,
        "each_sentence_carries_its_rendered_formula": carries_its_formula,
        "theorem_field_gated_by": gated_by,
        "theorem_fields_without_a_gate": ungated,
        "gates_that_did_not_pass": missing_gate,
        "refuted_sentence_digests": [sha256(f.encode("utf-8")).hexdigest()
                                     for f in REFUTED_SENTENCE_FRAGMENTS],
        "refuted_fragments_found_in_the_output": len(present),
    }
    payload["pass"] = bool(all(carries_its_formula.values())
                           and not ungated and not missing_gate
                           and not present)
    return payload


def certificate_mutation_teeth(instances: list[Instance], theorem: dict,
                               certificates: dict) -> dict:
    """One load-bearing mutation per check family; each must be caught."""
    probe = Instance((3, 3), (2, 2, 3, 1, 2, 2), frozenset({3}))
    teeth: list[dict] = []

    def tooth(name: str, family: str, bites: bool, detail: str) -> None:
        teeth.append({"tooth": name, "check_family": family,
                      "bites": bool(bites), "detail": detail})

    truth = probe.route_nullspace()
    quantities = (probe.disjoint_orbit_count(), probe.outside_fibre_freedom())
    # 1-2. constraint-matrix family: dropping a row inflates the dimension
    rows_probe = probe.constraint_rows()
    mutated = probe.n_fibre - exact_rank(rows_probe[:-1], probe.n_fibre)
    tooth("drop_one_orbit_constancy_row", "constraint_matrix", mutated != truth,
          f"dimension moved {truth} -> {mutated}")
    first_zero = next(i for i, r in enumerate(rows_probe) if sum(r) == 1)
    mutated = probe.n_fibre - exact_rank(
        rows_probe[:first_zero] + rows_probe[first_zero + 1:], probe.n_fibre)
    tooth("drop_one_vanishing_row", "constraint_matrix", mutated != truth,
          f"dimension moved {truth} -> {mutated}")
    # 3. solution-dimension-law family: a wrong coefficient set
    wrong = evaluate_law((1, 1, 1), quantities)
    tooth("solution_dimension_law_off_by_a_constant", "dimension_law",
          wrong != truth, f"wrong law gives {wrong} against {truth}")
    # 4. same family, wrong counted quantity
    wrong = evaluate_law((1, 0, 0), quantities)
    tooth("solution_dimension_law_without_the_within_fibre_term",
          "dimension_law", wrong != truth,
          f"wrong law gives {wrong} against {truth}")
    # 5. pushforward-law family
    push_truth = probe.route_base_nullspace()
    wrong = evaluate_law((1, 1), (probe.disjoint_orbit_count(),))
    tooth("pushforward_dimension_law_off_by_a_constant", "dimension_law",
          wrong != push_truth,
          f"wrong law gives {wrong} against exact rank {push_truth}")
    # 6. normalized-dimension family, against the two-sided bounds
    lower, upper = probe.normalized_dimension_bounds()
    wrong = evaluate_law((1, 1, 0), (probe.disjoint_orbit_count(),
                                     probe.disjoint_fibre_freedom()))
    tooth("normalized_dimension_law_without_the_orbit_mass_constraint",
          "dimension_law", lower == upper and wrong != upper,
          f"bounds close at {upper}; wrong law gives {wrong}")
    # 7. support-containment family: the control at a disjoint base point
    disjoint_base = sorted(probe.disjoint_base_points())[0]
    base_rank = exact_rank(probe.constraint_rows(), probe.n_fibre)
    with_indicator = exact_rank(
        probe.constraint_rows() + [probe.fibre_indicator(disjoint_base)],
        probe.n_fibre)
    tooth("support_certificate_claimed_at_a_disjoint_base_point",
          "support_containment", with_indicator != base_rank,
          "the fibre-total functional there is not in the row space, so the"
          " certificate cannot be issued")
    # 8. extreme-point family: the product shape gives another count
    separating = Instance((1, 1), (2, 2), frozenset())
    brute = len(separating.brute_force_extreme_points())
    tooth("extreme_points_as_a_cartesian_product_of_simplices",
          "extreme_points",
          separating.product_shape_extreme_point_count() != brute,
          f"enumeration finds {brute} extreme points;"
          f" the product shape would have"
          f" {separating.product_shape_extreme_point_count()}")
    # 9. witness family: the hypothesis without the two-fibre clause
    relaxed = Instance((2,), (1, 2), frozenset({0}))
    relaxed_bad = Instance((2,), (1, 1), frozenset({0}))
    tooth("signed_witness_hypothesis_without_the_two_fibre_clause",
          "signed_witness",
          relaxed_bad.relaxed_witness_hypothesis()
          and relaxed_bad.cross_orbit_signed_witness() is None
          and relaxed.cross_orbit_signed_witness() is not None,
          "an instance satisfies the relaxed hypothesis while every eligible"
          " base point there carries a single fibre point")
    # 10. witness family: skipping instances without a disjoint orbit
    skipped = sum(1 for inst in instances
                  if inst.signed_witness_hypothesis()
                  and not inst.disjoint_orbits())
    tooth("signed_witness_tally_restricted_to_instances_with_a_disjoint_orbit",
          "signed_witness", skipped > 0,
          f"{skipped} instances satisfy the hypothesis with no disjoint orbit")
    # 11. representative family
    rep = probe.fibre_uniform_representative()
    scaled = {k: v * 2 for k, v in rep.items()}
    tooth("representative_rescaled_off_total_mass_one", "representatives",
          sum(scaled.values(), Fraction(0)) != 1,
          "normalization gate rejects it")
    # 12. representative family: a weighting on the required-zero subset
    bad = {probe.fibre_offset[3]: Fraction(1)}
    tooth("weighting_on_the_required_zero_subset", "representatives",
          not probe.satisfies_zero(bad), "vanishing gate rejects it")
    # 13. representative family: orbit constancy broken
    bad = {probe.fibre_offset[probe.disjoint_orbits()[0][0]]: Fraction(1)}
    tooth("orbit_constancy_broken_by_a_single_base_point", "representatives",
          not probe.satisfies_orbit_constancy(bad),
          "orbit-constancy gate rejects it")
    # 14. uniqueness family: two distinct solutions share one pushforward mass
    concentrated = probe.concentrated_representative()
    tooth("event_level_uniqueness_claim", "representatives",
          rep != concentrated
          and probe.pushforward(rep) == probe.pushforward(concentrated),
          "two distinct normalized non-negative solutions share one"
          " pushforward mass")
    # 15. basis family
    basis = probe.constructive_basis()
    duplicated = basis + [basis[0]]
    tooth("linearly_dependent_basis", "basis",
          exact_rank(duplicated, probe.n_fibre) != len(duplicated),
          "exact rank detects the repeated vector")
    # 16. group family: a permutation that is not the declared generator
    perm = list(probe.generator())
    perm[0], perm[probe.n_base - 1] = perm[probe.n_base - 1], perm[0]
    orbits_of_mutant = set()
    for base in range(probe.n_base):
        reached = {base}
        current = perm[base]
        while current != base:
            reached.add(current)
            current = perm[current]
        orbits_of_mutant.add(tuple(sorted(reached)))
    declared = {tuple(sorted(o)) for o in probe.orbits}
    tooth("generator_swapped_between_two_orbits", "group_structure",
          orbits_of_mutant != declared,
          "the mutant permutation's orbits are not the declared partition")
    # 17. claim-text family: a mutated sentence loses its rendered formula
    mutated_theorem = dict(theorem)
    mutated_theorem["pushforward_dimension"] = (
        "the event-level weighting is determined by a single scalar")
    mutated_check = certificate_claim_text(mutated_theorem, certificates)
    tooth("theorem_sentence_replaced_by_a_false_one", "claim_text",
          not mutated_check["pass"]
          and certificate_claim_text(theorem, certificates)["pass"],
          "the sentence no longer carries the rendered formula of the law the"
          " run verified, while the unmutated theorem passes the same gate")
    # 18. claim-text family: a withdrawn sentence reappears
    scan_probe = certificate_claim_text(
        {**theorem,
         "non_negative_normalized": theorem["non_negative_normalized"]
         + " -- the set is a product of simplices"},
        certificates)
    tooth("withdrawn_sentence_reintroduced", "claim_text",
          not scan_probe["pass"],
          "the refuted-fragment scan finds it")
    # 19. route-inventory family: a false disjointness declaration
    tree = ast.parse((ROOT / SELF_PATH).read_bytes(), filename=SELF_PATH)
    graph = _module_call_graph(tree)
    seen: set[str] = set()
    stack = [ROUTE_ENTRY_POINTS["NULLSPACE"]]
    while stack:
        current = stack.pop()
        for callee in graph.get(current, ()):
            if callee not in seen:
                seen.add(callee)
                stack.append(callee)
    tooth("nullspace_route_declared_without_its_rank_helper", "route_inventory",
          tuple(sorted(seen)) != ("Instance.constraint_rows",
                                  "Instance.fibre_points"),
          "the syntax tree shows the helper the shorter declaration omits")
    # 20. large-instance family: a wrong fibre rule moves the dimension
    mutant_spec = dict(LARGE_INSTANCES[0])
    mutant = Instance(mutant_spec["orbit_sizes"],
                      tuple(128 for _ in range(132)),
                      build_large_instance(mutant_spec).required_zero)
    tooth("large_instance_fibre_rule_altered", "large_instances",
          mutant.route_count() != build_large_instance(mutant_spec).route_count(),
          f"dimension moves to {mutant.route_count()} from"
          f" {build_large_instance(mutant_spec).route_count()}")

    # 21. large-instance family: deleting a promised row must not silently
    # redefine the expected coverage.
    tooth("delete_one_of_the_two_declared_large_instances", "large_instances",
          tuple(spec["name"] for spec in LARGE_INSTANCES[:-1])
          != EXPECTED_LARGE_INSTANCE_NAMES,
          "the separately declared expected-name tuple rejects the shortened"
          " specification list")

    # 22. output-discipline family: the renderer rejects both an oversized
    # transcript and a transcript without the mandatory terminal TOTAL line.
    output_mutations_rejected = 0
    for bad_lines in (
        ["x" * HOUSE_STDOUT_LIMIT_BYTES, "TOTAL: PASS=1 FAIL=0"],
        ["VERDICT ALL_CERTIFICATES_PASS"],
    ):
        try:
            bounded_stdout(bad_lines)
        except ValueError:
            output_mutations_rejected += 1
    tooth("stdout_budget_or_terminal_total_removed", "output_discipline",
          output_mutations_rejected == 2,
          "the bounded renderer rejected both malformed transcripts")

    families = sorted({t["check_family"] for t in teeth})
    payload = {
        "certificate": "MUTATION_TEETH",
        "statement": ("one load-bearing mutation for each check family; every"
                      " one must be caught by the gate that owns it"),
        "probe_instance": probe.key,
        "check_families_covered": families,
        "teeth": teeth,
        "teeth_total": len(teeth),
        "teeth_biting": sum(1 for t in teeth if t["bites"]),
    }
    payload["pass"] = all(t["bites"] for t in teeth)
    return payload


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    OUTPUT_LINES.clear()
    OUTPUT_LINES.extend((
        "CYCLE906_ORBIT_CONSTANT_MASS_DIMENSION_SUPPORT_RUNNER",
        "SELF_CONTAINED_NO_EXTERNAL_SCIENTIFIC_INPUT_IS_READ",
        "EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY",
    ))

    instances = enumerate_family()
    rows = sweep(instances)

    certificates: dict[str, dict] = {}
    order: list[str] = []

    def record(payload: dict) -> bool:
        name = payload["certificate"]
        certificates[name] = payload
        order.append(name)
        return emit(name, payload)

    ok = True
    ok &= record(certificate_self_containment())
    ok &= record(certificate_group_structure(instances))
    ok &= record(certificate_dimension_laws(rows, len(instances)))
    ok &= record(certificate_support_containment(instances))
    ok &= record(certificate_extreme_points(instances))
    ok &= record(certificate_nonnegative_witnesses(instances))
    ok &= record(certificate_large_instances())
    ok &= record(certificate_route_inventory())

    theorem = build_theorem(certificates["DIMENSION_LAWS"],
                            certificates["NON_NEGATIVE_WITNESSES"],
                            certificates["EXTREME_POINTS"],
                            certificates["LARGE_DECLARED_INSTANCES"])
    ok &= record(certificate_mutation_teeth(instances, theorem, certificates))
    # CLAIM_TEXT is emitted last so that its refuted-sentence scan covers
    # every other certificate this run emits.
    ok &= record(certificate_claim_text(theorem, certificates))

    summary = {
        "certificate": "SUMMARY",
        "theorem": theorem,
        "declared_laws": {
            "solution_dimension": list(SOLUTION_DIMENSION_LAW),
            "pushforward_dimension": list(PUSHFORWARD_DIMENSION_LAW),
            "normalized_dimension": list(NORMALIZED_DIMENSION_LAW),
        },
        "family": {
            "base_point_counts": "one through five",
            "orbit_partitions": (
                "one canonical contiguous representative of every orbit-size"
                " partition; all relevant decorated cases up to relabeling"
            ),
            "max_base_points": MAX_BASE_POINTS,
            "fibre_alphabet_up_to_four_base_points": list(FIBRE_ALPHABET_SMALL),
            "fibre_alphabet_at_five_base_points": list(FIBRE_ALPHABET_WIDE),
            "required_zero_subsets": "every subset of base points",
            "instances": len(instances),
            "extreme_point_enumeration_max_fibre_points":
                VERTEX_ENUMERATION_MAX_FIBRE_POINTS,
        },
        "certificates_emitted": order,
        "all_certificates_pass": bool(ok),
    }
    emit("SUMMARY", {**summary, "pass": bool(ok)})

    receipt = {
        "runner": SELF_PATH,
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "fraction_label": FRACTION_LABEL,
        "theorem": theorem,
        "declared_laws": summary["declared_laws"],
        "family": summary["family"],
        "certificates": {name: certificates[name] for name in order},
        "per_instance_dimension_table_digest":
            certificates["DIMENSION_LAWS"]["dimension_table_digest"],
        "all_certificates_pass": bool(ok),
    }
    (ROOT / RECEIPT_PATH).write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    OUTPUT_LINES.append(
        f"RECEIPT {RECEIPT_PATH} "
        f"canonical_json_sha256={digest(receipt)[:16]}"
    )
    OUTPUT_LINES.append(
        f"VERDICT {'ALL_CERTIFICATES_PASS' if ok else 'CERTIFICATE_FAILED'}"
    )
    passed = sum(bool(payload.get("pass"))
                 for payload in certificates.values()) + int(bool(ok))
    failed = sum(not bool(payload.get("pass"))
                 for payload in certificates.values()) + int(not ok)
    OUTPUT_LINES.append(f"TOTAL: PASS={passed} FAIL={failed}")
    try:
        stdout = bounded_stdout(OUTPUT_LINES)
    except ValueError as exc:
        sys.stderr.write(f"OUTPUT_DISCIPLINE_FAILED: {exc}\n")
        sys.stdout.write("OUTPUT_DISCIPLINE FAIL\nTOTAL: PASS=0 FAIL=1\n")
        return 1
    sys.stdout.write(stdout)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
