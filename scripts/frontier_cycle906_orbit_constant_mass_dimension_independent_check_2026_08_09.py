#!/usr/bin/env python3
"""Cycle 906 independent check: specified to REFUTE the orbit-constant
pushforward-mass dimension theorem, its receipt, AND ITS SENTENCES.

Its only declared inputs are the two files of this same landing delta -- the
primary runner's source and the primary runner's receipt -- pinned by
sha256 and git blob and verified hard-fail before any comparison.  It reads
no ancestor artifact, no axiom file and no repository census, and imports no
repository module.

INDEPENDENCE.  The checker re-derives every advertised number from its own
in-file rebuild; it never takes a value from the receipt and re-prints it.
The rebuild differs from the primary's implementation path at every level
that matters:

  * base points are laid out in the reverse orbit order, fibre points are
    indexed in reverse base order, and the orbit-constancy rows are
    CONSECUTIVE differences around each orbit rather than differences
    against a fixed orbit head, so the constraint matrix is a different
    matrix with the same solution space;
  * the dimension is obtained by MODULAR rank over three large primes
    (integer arithmetic mod p) instead of the primary's fraction-free
    integer elimination;
  * a second dimension is obtained by a rank-nullity SPLIT -- the kernel of
    the pushforward map counted directly, plus the base-level dimension --
    which never touches the fibre-level matrix at all;
  * a third dimension is obtained from a reduced row echelon form over the
    rationals with an explicit free-variable basis, every vector of which is
    re-verified against both linear conditions;
  * support containment is re-established CONSTRUCTIVELY -- an explicit
    integer combination of the checker's own constraint rows is built and
    required to equal the fibre-total functional -- where the primary uses a
    rank test, and the control at base points inside a disjoint orbit is an
    exhibited solution with nonzero mass there rather than a second rank;
  * the extreme points are re-enumerated by brute force over all supports in
    the checker's own layout.

SENTENCES ARE CHECKED, NOT COPIED.  The checker holds its own transcription
of the dimension laws, of the phrases they are rendered with, and of the
sentence frames, and RE-RENDERS the whole theorem from its own recomputed
numbers.  Any receipt theorem sentence that differs by one character is a
disagreement, and a nonzero exit.  A withdrawn sentence reappearing anywhere
in the receipt is a disagreement too.  What this cannot detect is a
coordinated edit of both runners; that is why the note carries the general
proof, and the proof is what makes the sentences true.

REFUTATION DISCIPLINE.  Every advertised receipt row is a recomputed
comparison that fails closed, and planted receipt corruptions are applied to
confirm each gate can detect tampering.  The verdict is CORROBORATES only
when every comparison agrees and every tooth bites; any disagreement, any
failed gate, and any tooth that does not bite produces a NONZERO EXIT.

Every fraction emitted is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

Support runner.  Authority none, audit unset.  Independent audit still
required.
"""
from __future__ import annotations

import ast
import copy
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import itertools
import json
from pathlib import Path
import sys

AUDIT_TIMEOUT_SEC = 600

# Both declared inputs are files of THIS landing delta, reviewed here: the
# primary runner's source and the receipt that run emitted.  Nothing else --
# no ancestor source, receipt, note or axiom file -- is declared or read.
# The paths are written as literals because the cache envelope and the
# evidence-readiness gate parse this tuple without executing the module.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle906_orbit_constant_mass_dimension_2026_08_09.py",
    "outputs/orbit_constant_mass_dimension_cycle906_receipt_2026_08_09.json",
)

PRIMARY_PATH, PRIMARY_RECEIPT = AUDIT_INPUT_PATHS
SELF_PATH = ("scripts/frontier_cycle906_orbit_constant_mass_dimension"
             "_independent_check_2026_08_09.py")
RECEIPT_PATH = ("outputs/orbit_constant_mass_dimension_independent_check"
                "_cycle906_receipt_2026_08_09.json")

EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "696cc7bfee4adbe1ba4dd96a319764b3dc91ab89aaff3188e377d9cc17d3848a",
    PRIMARY_RECEIPT:
        "0032e0feac893abe73e1dd0923c6a661e6fda1e20f0a6dcef20c9ac039543525",
}
EXPECTED_GIT_BLOBS = {
    PRIMARY_PATH: "20db861618bd7b41b44bfd91275079abbf63606c",
    PRIMARY_RECEIPT: "5b7419fbb455ef20d5fcc6091418e97a1399a45a",
}

ROOT = Path(__file__).resolve().parents[1]
FRACTION_LABEL = "bookkeeping fraction, not probability"

# The checker's OWN transcription of the declared family.  It is compared
# against the primary's declared constants by an AST read below; a mismatch
# is a refutation, not a repair.
CHECK_MAX_BASE_POINTS = 5
CHECK_FIBRE_ALPHABET_SMALL = (1, 2, 3)
CHECK_FIBRE_ALPHABET_WIDE = (1, 2)
CHECK_WIDE_ALPHABET_FROM = 5
CHECK_VERTEX_MAX_FIBRE_POINTS = 6

# The checker's OWN transcription of the dimension laws and of the prose the
# primary renders them with.  Nothing here is read from the receipt.
CHECK_SOLUTION_LAW = (1, 1, 0)
CHECK_PUSHFORWARD_LAW = (1, 0)
CHECK_NORMALIZED_LAW = (1, 1, -1)
CHECK_DISJOINT_PHRASE = "the number of orbits disjoint from the required-zero subset"
CHECK_OUTSIDE_PHRASE = ("the sum over base points outside that subset of"
                        " (fibre size minus one)")
CHECK_DISJOINT_FIBRE_PHRASE = ("the sum over base points of those orbits of"
                               " (fibre size minus one)")

# The checker's own transcription of the withdrawn sentence fragments.  Only
# their digests are published, so the withdrawn wording reaches no receipt.
CHECK_REFUTED_FRAGMENTS = (
    "unique up to scale",
    "product of simplices",
    "the tension resolves",
)

PRIMES = (2147483647, 2147483629, 2147483587)


class _RepositoryImportFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        leaf = fullname.rsplit(".", 1)[-1]
        if leaf.startswith(("frontier_", "toy_", "runner_cache")):
            self.hits.append(fullname)
            raise ImportError(f"independent checker forbids import: {fullname}")
        return None


FIREWALL = _RepositoryImportFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


DISAGREEMENTS: list[dict] = []


def disagree(gate: str, detail: str, expected: object, observed: object) -> None:
    DISAGREEMENTS.append({"gate": gate, "detail": detail,
                          "receipt_says": expected, "checker_finds": observed})


def emit(name: str, payload: dict) -> bool:
    ok = bool(payload.get("pass"))
    print(f"CERTIFICATE {name} {'PASS' if ok else 'FAIL'} {compact(payload)}")
    return ok


# ---------------------------------------------------------------------------
# the checker's own rendering of the laws
# ---------------------------------------------------------------------------

def render_law(coefficients: tuple[int, ...], phrases: tuple[str, ...]) -> str:
    weights, constant = coefficients[:-1], coefficients[-1]
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


def rendered_theorem(instances: int, hypothesis_instances: int,
                     enumerated_instances: int) -> dict:
    """The theorem the primary MUST have emitted, rebuilt here from the
    checker's own law transcription and its own recomputed counts."""
    return {
        "parameterization": (
            "for every finite cyclic action on finitely many base points,"
            " every assignment of non-empty finite fibres and every"
            " required-zero subset, the solutions of the two linear"
            " conditions are exactly the span of the explicit basis this"
            " runner constructs, so their dimension is "
            + render_law(CHECK_SOLUTION_LAW,
                         (CHECK_DISJOINT_PHRASE, CHECK_OUTSIDE_PHRASE))),
        "pushforward_dimension": (
            "the space of admissible pushforward masses has dimension exactly "
            + render_law(CHECK_PUSHFORWARD_LAW, (CHECK_DISJOINT_PHRASE,))
            + "; where that number is one, every admissible pushforward mass"
              " is therefore a rational multiple of one fixed admissible"
              " mass"),
        "non_negative_normalized": (
            "on instances with at least one disjoint orbit, adding"
            " non-negativity and total mass one puts every solution to zero"
            " at every fibre point over a base point outside the disjoint"
            " orbits and leaves a set of dimension "
            + render_law(CHECK_NORMALIZED_LAW,
                         (CHECK_DISJOINT_PHRASE, CHECK_DISJOINT_FIBRE_PHRASE))
            + ", whose extreme points are exactly the weightings that place"
              " one disjoint orbit's whole mass on a single fibre point at"
              " each of that orbit's base points"),
        "signed_solution_off_the_disjoint_orbits": (
            "whenever a base point lies outside the required-zero subset,"
            " lies in an orbit that meets it, and carries at least two fibre"
            " points, the difference of two of its fibre weights is a"
            " solution supported strictly outside every disjoint orbit; that"
            " hypothesis holds at "
            + str(hypothesis_instances)
            + " of the "
            + str(instances)
            + " swept instances and a witness is exhibited at every one of"
              " them, so support containment is a consequence of"
              " non-negativity and not of the two linear conditions alone"),
        "verification_scope": (
            "the laws above are proved in the note for all finite instances;"
            " this runner verifies them on "
            + str(instances)
            + " exhaustively enumerated instances, the extreme-point"
              " statement by brute-force enumeration on the "
            + str(enumerated_instances)
            + " of them with at most "
            + str(CHECK_VERTEX_MAX_FIBRE_POINTS)
            + " fibre points and a disjoint orbit, and evaluates the laws at"
              " two declared larger instances where the fibre-level rank"
              " routes are not run"),
        "scope": (
            "conditional on the declared finite structure only; this runner"
            " reads no repository census, no symmetry claim, no interface"
            " condition and no axiom surface, and asserts nothing about any"
            " of them"),
    }


def evaluate_law(coefficients: tuple[int, ...],
                 quantities: tuple[int, ...]) -> int:
    weights, constant = coefficients[:-1], coefficients[-1]
    return sum(w * q for w, q in zip(weights, quantities)) + constant


# ---------------------------------------------------------------------------
# independent linear algebra
# ---------------------------------------------------------------------------

def modular_rank(rows: list[list[int]], ncols: int, prime: int) -> int:
    mat = [[x % prime for x in row] for row in rows]
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
        inverse = pow(mat[rank][col], prime - 2, prime)
        prow = [(x * inverse) % prime for x in mat[rank]]
        mat[rank] = prow
        for r in range(rank + 1, nrows):
            factor = mat[r][col]
            if factor:
                row = mat[r]
                for c in range(col, ncols):
                    row[c] = (row[c] - factor * prow[c]) % prime
        rank += 1
    return rank


def rref_free_basis(rows: list[list[int]], ncols: int
                    ) -> list[list[Fraction]]:
    """Solution basis from the reduced row echelon form's free variables."""
    mat = [[Fraction(x) for x in row] for row in rows]
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
    pivot_set = set(pivots)
    basis: list[list[Fraction]] = []
    for free_col in range(ncols):
        if free_col in pivot_set:
            continue
        vector = [Fraction(0)] * ncols
        vector[free_col] = Fraction(1)
        for i, pivot_col in enumerate(pivots):
            vector[pivot_col] = -mat[i][free_col]
        basis.append(vector)
    return basis


def unique_solution(rows: list[list[int]], ncols: int,
                    forced_zero: list[int]) -> list[Fraction] | None:
    """The unique x with rows.x = 0, sum(x) = 1 and x = 0 off a support."""
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
# the checker's own rebuild of an instance -- reverse layout, consecutive rows
# ---------------------------------------------------------------------------

class Rebuild:
    def __init__(self, orbit_sizes: tuple[int, ...],
                 fibre_sizes: tuple[int, ...],
                 zero_mask: tuple[int, ...]) -> None:
        self.orbit_sizes = orbit_sizes
        self.fibre_sizes = fibre_sizes
        self.zero_mask = zero_mask
        self.n_base = sum(orbit_sizes)
        # canonical (declared) base numbering, used only for the shared key
        orbits: list[tuple[int, ...]] = []
        start = 0
        for size in orbit_sizes:
            orbits.append(tuple(range(start, start + size)))
            start += size
        self.orbits = tuple(orbits)
        # the checker's OWN fibre indexing: reverse base order
        self.local_index: dict[tuple[int, int], int] = {}
        lookup: list[int] = []
        running = 0
        for base in reversed(range(self.n_base)):
            for local in range(fibre_sizes[base]):
                self.local_index[(base, local)] = running
                lookup.append(base)
                running += 1
        self.n_fibre = running
        self.base_lookup = tuple(lookup)
        self.required_zero = frozenset(b for b in range(self.n_base)
                                       if zero_mask[b])

    @property
    def key(self) -> tuple:
        return (self.orbit_sizes,
                tuple((self.fibre_sizes[v], int(v in self.required_zero))
                      for v in range(self.n_base)))

    def points(self, base: int) -> list[int]:
        return [self.local_index[(base, i)]
                for i in range(self.fibre_sizes[base])]

    def disjoint_orbits(self) -> tuple[tuple[int, ...], ...]:
        return tuple(o for o in self.orbits
                     if not (set(o) & self.required_zero))

    def disjoint_base_points(self) -> set[int]:
        return {v for o in self.disjoint_orbits() for v in o}

    def orbit_of(self, base: int) -> tuple[int, ...]:
        for orbit in self.orbits:
            if base in orbit:
                return orbit
        raise KeyError(base)

    def constraint_rows(self) -> list[list[int]]:
        """Reverse layout, and CONSECUTIVE differences around each orbit."""
        rows: list[list[int]] = []
        for orbit in reversed(self.orbits):
            for i in range(len(orbit)):
                nxt = orbit[(i + 1) % len(orbit)]
                if len(orbit) == 1:
                    break
                if i == len(orbit) - 1:
                    break
                row = [0] * self.n_fibre
                for point in self.points(orbit[i]):
                    row[point] += 1
                for point in self.points(nxt):
                    row[point] -= 1
                rows.append(row)
        for base in sorted(self.required_zero, reverse=True):
            for point in self.points(base):
                row = [0] * self.n_fibre
                row[point] = 1
                rows.append(row)
        return rows

    def base_rows(self) -> list[list[int]]:
        rows: list[list[int]] = []
        for orbit in reversed(self.orbits):
            for i in range(len(orbit) - 1):
                row = [0] * self.n_base
                row[orbit[i]] += 1
                row[orbit[i + 1]] -= 1
                rows.append(row)
        for base in sorted(self.required_zero, reverse=True):
            row = [0] * self.n_base
            row[base] = 1
            rows.append(row)
        return rows

    # ---- three independent dimension routes -------------------------------

    def dimension_modular(self) -> tuple[int, list[int]]:
        rows = self.constraint_rows()
        ranks = [modular_rank(rows, self.n_fibre, p) for p in PRIMES]
        return self.n_fibre - max(ranks), ranks

    def dimension_split(self) -> int:
        """Rank-nullity split; never touches the fibre-level matrix."""
        kernel_of_pushforward = sum(
            self.fibre_sizes[v] - 1 for v in range(self.n_base)
            if v not in self.required_zero)
        base_rows = self.base_rows()
        base_dim = self.n_base - max(
            modular_rank(base_rows, self.n_base, p) for p in PRIMES)
        return kernel_of_pushforward + base_dim

    def dimension_rref(self) -> int:
        basis = rref_free_basis(self.constraint_rows(), self.n_fibre)
        for vector in basis:
            weight = {i: v for i, v in enumerate(vector) if v != 0}
            if not (self.satisfies_zero(weight)
                    and self.satisfies_orbit_constancy(weight)):
                return -1
        return len(basis)

    def base_dimension(self) -> int:
        base_rows = self.base_rows()
        return self.n_base - max(
            modular_rank(base_rows, self.n_base, p) for p in PRIMES)

    def normalized_dimension_modular(self) -> int:
        """Dimension of the affine hull of the non-negative normalized set."""
        rows = self.constraint_rows()
        inside = self.disjoint_base_points()
        for base in range(self.n_base):
            if base in inside:
                continue
            for point in self.points(base):
                row = [0] * self.n_fibre
                row[point] = 1
                rows.append(row)
        rank = max(modular_rank(rows, self.n_fibre, p) for p in PRIMES)
        return self.n_fibre - rank - 1

    # ---- condition checks -------------------------------------------------

    def satisfies_zero(self, weight: dict[int, Fraction]) -> bool:
        return all(self.base_lookup[p] not in self.required_zero
                   for p, v in weight.items() if v != 0)

    def pushforward(self, weight: dict[int, Fraction]) -> list[Fraction]:
        mass = [Fraction(0)] * self.n_base
        for point, value in weight.items():
            mass[self.base_lookup[point]] += value
        return mass

    def satisfies_orbit_constancy(self, weight: dict[int, Fraction]) -> bool:
        mass = self.pushforward(weight)
        return all(all(mass[x] == mass[o[0]] for x in o) for o in self.orbits)

    # ---- constructive support-containment certificate ---------------------

    def support_certificate(self, base: int) -> list[int] | None:
        """Build the fibre-total functional at `base` as an EXPLICIT integer
        combination of this rebuild's own constraint rows.

        For a base point in an orbit that meets the required-zero subset,
        the functional equals the fibre-total at a required-zero base point
        of that orbit -- itself a sum of vanishing rows -- plus the
        telescoped consecutive-difference rows between the two.  Every row
        used is checked for membership in this rebuild's own row list, so
        the combination cannot quietly use a row the matrix does not have.
        Returns the combination's value, or None when the orbit has no
        required-zero base point or a used row is not a real row.
        """
        orbit = self.orbit_of(base)
        anchors = [v for v in orbit if v in self.required_zero]
        if not anchors:
            return None
        anchor = anchors[0]
        rows = self.constraint_rows()
        used: list[list[int]] = []
        total = [0] * self.n_fibre
        for point in self.points(anchor):        # the vanishing rows
            row = [0] * self.n_fibre
            row[point] = 1
            used.append(row)
            total[point] += 1
        here = orbit.index(anchor)
        there = orbit.index(base)
        # telescope: row k is (mass at orbit[k]) - (mass at orbit[k+1]), so
        # walking up subtracts those rows and walking down adds them
        sign = -1 if there > here else 1
        for k in range(min(here, there), max(here, there)):
            row = [0] * self.n_fibre
            for point in self.points(orbit[k]):
                row[point] += 1
            for point in self.points(orbit[k + 1]):
                row[point] -= 1
            used.append(row)
            for index, value in enumerate(row):
                total[index] += sign * value
        if any(row not in rows for row in used):
            return None
        return total

    def uniform_on_orbit(self, orbit: tuple[int, ...]) -> dict[int, Fraction]:
        """The fibre-uniform non-negative normalized solution carried by one
        disjoint orbit; used as the exhibited control for support
        containment."""
        out: dict[int, Fraction] = {}
        for base in orbit:
            share = Fraction(1, len(orbit) * self.fibre_sizes[base])
            for point in self.points(base):
                out[point] = share
        return out

    # ---- representatives, rebuilt independently ---------------------------

    def uniform_representative(self) -> dict[int, Fraction] | None:
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return None
        orbit = disjoint[0]
        out: dict[int, Fraction] = {}
        for base in orbit:
            share = Fraction(1, len(orbit) * self.fibre_sizes[base])
            for point in self.points(base):
                out[point] = share
        return out

    def concentrated_representative(self) -> dict[int, Fraction] | None:
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return None
        orbit = disjoint[0]
        return {self.points(base)[0]: Fraction(1, len(orbit))
                for base in orbit}

    def signed_witness_hypothesis(self) -> bool:
        disjoint = self.disjoint_base_points()
        for base in range(self.n_base):
            if base in self.required_zero or base in disjoint:
                continue
            if self.fibre_sizes[base] >= 2:
                return True
        return False

    def cross_orbit_signed_witness(self) -> dict[int, Fraction] | None:
        disjoint = self.disjoint_base_points()
        for base in range(self.n_base):
            if base in self.required_zero or base in disjoint:
                continue
            if self.fibre_sizes[base] < 2:
                continue
            pts = self.points(base)
            return {pts[0]: Fraction(1), pts[1]: Fraction(-1)}
        return None

    def normalized_dimension_closed(self) -> int:
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return -1
        return evaluate_law(
            CHECK_NORMALIZED_LAW,
            (len(disjoint),
             sum(self.fibre_sizes[v] - 1 for o in disjoint for v in o)))

    def claimed_extreme_points(self) -> set[tuple[Fraction, ...]]:
        out: set[tuple[Fraction, ...]] = set()
        for orbit in self.disjoint_orbits():
            share = Fraction(1, len(orbit))
            for choice in itertools.product(*[self.points(b) for b in orbit]):
                vector = [Fraction(0)] * self.n_fibre
                for point in choice:
                    vector[point] = share
                out.add(tuple(vector))
        return out

    def brute_force_extreme_points(self) -> set[tuple[Fraction, ...]]:
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
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return 0
        product = 1
        for orbit in disjoint:
            for base in orbit:
                product *= self.fibre_sizes[base]
        return len(disjoint) * product

    def zero_count(self, weight: dict[int, Fraction]) -> int:
        return self.n_fibre - sum(1 for v in weight.values() if v != 0)


def partitions(total: int) -> list[tuple[int, ...]]:
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


_FAMILY: list["Rebuild"] = []
_COMPUTED: dict[str, object] = {}


def rebuild_family() -> list[Rebuild]:
    if _FAMILY:
        return _FAMILY
    out: list[Rebuild] = []
    for n_base in range(1, CHECK_MAX_BASE_POINTS + 1):
        alphabet = (CHECK_FIBRE_ALPHABET_WIDE
                    if n_base >= CHECK_WIDE_ALPHABET_FROM
                    else CHECK_FIBRE_ALPHABET_SMALL)
        for orbit_sizes in partitions(n_base):
            for fibres in itertools.product(alphabet, repeat=n_base):
                for mask in range(1 << n_base):
                    bits = tuple(1 if mask & (1 << v) else 0
                                 for v in range(n_base))
                    out.append(Rebuild(orbit_sizes, fibres, bits))
    _FAMILY.extend(out)
    return _FAMILY


def computed_table() -> dict:
    """One sweep of the whole family; cached so the teeth stay cheap."""
    if "table" in _COMPUTED:
        return _COMPUTED["table"]  # type: ignore[return-value]
    table: list[tuple[str, int]] = []
    route_mismatches = 0
    first_mismatch = None
    base_mismatches = 0
    law_mismatches = 0
    normalized_mismatches = 0
    normalized_checked = 0
    for inst in rebuild_family():
        modular, _ = inst.dimension_modular()
        split = inst.dimension_split()
        rref = inst.dimension_rref()
        if not (modular == split == rref):
            route_mismatches += 1
            if first_mismatch is None:
                first_mismatch = {"key": inst.key, "modular": modular,
                                  "split": split, "rref": rref}
        disjoint = len(inst.disjoint_orbits())
        outside = sum(inst.fibre_sizes[v] - 1 for v in range(inst.n_base)
                      if v not in inst.required_zero)
        if evaluate_law(CHECK_SOLUTION_LAW, (disjoint, outside)) != modular:
            law_mismatches += 1
        base_dim = inst.base_dimension()
        if base_dim != evaluate_law(CHECK_PUSHFORWARD_LAW, (disjoint,)):
            base_mismatches += 1
        if disjoint:
            normalized_checked += 1
            if inst.normalized_dimension_modular() \
                    != inst.normalized_dimension_closed():
                normalized_mismatches += 1
        table.append((compact(inst.key), modular))
    table.sort()
    result = {
        "table": table,
        "digest": digest(table),
        "sum": sum(d for _, d in table),
        "route_mismatches": route_mismatches,
        "first_mismatch": first_mismatch,
        "base_mismatches": base_mismatches,
        "law_mismatches": law_mismatches,
        "normalized_mismatches": normalized_mismatches,
        "normalized_checked": normalized_checked,
    }
    _COMPUTED["table"] = result
    return result


def computed_support() -> dict:
    """Constructive support-containment certificates, and the exhibited
    control at base points inside a disjoint orbit."""
    if "support" in _COMPUTED:
        return _COMPUTED["support"]  # type: ignore[return-value]
    certified = 0
    failures = 0
    controls = 0
    control_defects = 0
    for inst in rebuild_family():
        inside = inst.disjoint_base_points()
        control_mass: dict[int, Fraction] = {}
        for orbit in inst.disjoint_orbits():
            mass = inst.pushforward(inst.uniform_on_orbit(orbit))
            for base in orbit:
                control_mass[base] = mass[base]
        for base in range(inst.n_base):
            if base in inside:
                # no certificate can exist here: an exhibited non-negative
                # normalized solution carries nonzero mass at this base point
                controls += 1
                if control_mass.get(base, Fraction(0)) == 0:
                    control_defects += 1
                continue
            built = inst.support_certificate(base)
            indicator = [0] * inst.n_fibre
            for point in inst.points(base):
                indicator[point] = 1
            if built is None or built != indicator or min(built) < 0:
                failures += 1
            else:
                certified += 1
    result = {
        "certified": certified,
        "failures": failures,
        "controls": controls,
        "control_defects": control_defects,
    }
    _COMPUTED["support"] = result
    return result


def computed_extreme_points() -> dict:
    if "extreme" in _COMPUTED:
        return _COMPUTED["extreme"]  # type: ignore[return-value]
    enumerated = 0
    set_mismatches = 0
    product_differs = 0
    for inst in rebuild_family():
        if inst.n_fibre > CHECK_VERTEX_MAX_FIBRE_POINTS \
                or not inst.disjoint_orbits():
            continue
        enumerated += 1
        brute = inst.brute_force_extreme_points()
        if brute != inst.claimed_extreme_points():
            set_mismatches += 1
        if inst.product_shape_extreme_point_count() != len(brute):
            product_differs += 1
    result = {
        "instances_enumerated": enumerated,
        "extreme_point_set_mismatches": set_mismatches,
        "instances_where_a_product_of_simplices_would_give_another_count":
            product_differs,
    }
    _COMPUTED["extreme"] = result
    return result


def computed_witnesses() -> dict:
    if "witnesses" in _COMPUTED:
        return _COMPUTED["witnesses"]  # type: ignore[return-value]
    with_solution = two_distinct = zero_differs = 0
    hypothesis = with_disjoint = without_disjoint = witness_found = 0
    biconditional_failures = 0
    defects: list[str] = []
    for inst in rebuild_family():
        uniform = inst.uniform_representative()
        if uniform is not None:
            with_solution += 1
            concentrated = inst.concentrated_representative()
            for weight in (uniform, concentrated):
                if sum(weight.values(), Fraction(0)) != 1 \
                        or any(v < 0 for v in weight.values()) \
                        or not inst.satisfies_zero(weight) \
                        or not inst.satisfies_orbit_constancy(weight):
                    defects.append("representative fails a declared property")
            if uniform != concentrated:
                two_distinct += 1
                if inst.pushforward(uniform) != inst.pushforward(concentrated):
                    defects.append("distinct representatives disagree on mass")
            if inst.zero_count(uniform) != inst.zero_count(concentrated):
                zero_differs += 1
        holds = inst.signed_witness_hypothesis()
        witness = inst.cross_orbit_signed_witness()
        if holds:
            hypothesis += 1
            if inst.disjoint_orbits():
                with_disjoint += 1
            else:
                without_disjoint += 1
        if (witness is not None) != holds:
            biconditional_failures += 1
        if witness is not None:
            witness_found += 1
            inside = inst.disjoint_base_points()
            if not (inst.satisfies_zero(witness)
                    and inst.satisfies_orbit_constancy(witness)):
                defects.append("cross-orbit signed witness is not a solution")
            if any(inst.base_lookup[p] in inside
                   for p, v in witness.items() if v != 0):
                defects.append("cross-orbit witness is supported inside a "
                               "disjoint orbit")
    result = {
        "counts": {
            "instances_with_a_disjoint_orbit": with_solution,
            "instances_with_two_distinct_representatives": two_distinct,
            "instances_where_zero_counts_differ": zero_differs,
            "instances_satisfying_the_signed_witness_hypothesis": hypothesis,
            "of_those_with_a_disjoint_orbit": with_disjoint,
            "of_those_without_a_disjoint_orbit": without_disjoint,
            "instances_with_a_cross_orbit_signed_solution": witness_found,
        },
        "biconditional_failures": biconditional_failures,
        "defects": sorted(set(defects)),
    }
    _COMPUTED["witnesses"] = result
    return result


def computed_large(spec: dict) -> dict:
    params = spec.get("declared_parameters", {})
    key = compact([params.get("orbit_sizes"), params.get("fibre_rule"),
                   params.get("required_zero_rule")])
    cache: dict = _COMPUTED.setdefault("large", {})  # type: ignore[assignment]
    if key in cache:
        return cache[key]
    inst = rebuild_large(spec)
    uniform = inst.uniform_representative()
    values = {
        "base_points": inst.n_base,
        "fibre_points": inst.n_fibre,
        "orbits_disjoint_from_required_zero": len(inst.disjoint_orbits()),
        "solution_space_dimension": inst.dimension_split(),
        "pushforward_mass_dimension": inst.base_dimension(),
        "non_negative_normalized_dimension": inst.normalized_dimension_closed(),
        "representative_zero_count": inst.zero_count(uniform),
    }
    representative_ok = (
        sum(uniform.values(), Fraction(0)) == 1
        and all(v >= 0 for v in uniform.values())
        and inst.satisfies_zero(uniform)
        and inst.satisfies_orbit_constancy(uniform))
    cache[key] = {"values": values, "representative_ok": representative_ok}
    return cache[key]


def rebuild_large(spec: dict) -> Rebuild:
    orbit_sizes = tuple(spec["declared_parameters"]["orbit_sizes"])
    n_base = sum(orbit_sizes)
    bounds: list[int] = []
    running = 0
    for size in orbit_sizes:
        bounds.append(running)
        running += size
    fibre_rule = spec["declared_parameters"]["fibre_rule"]
    zero_rule = spec["declared_parameters"]["required_zero_rule"]
    if "every base point carries 129" in fibre_rule:
        fibres = tuple(129 for _ in range(n_base))
    else:
        fibres = tuple(129 if v >= bounds[11] else 7 for v in range(n_base))
    if zero_rule.startswith("every base point of the first eleven orbits"):
        zero = set(range(bounds[11]))
    else:
        zero = set(range(bounds[10])) | {bounds[10]}
    bits = tuple(1 if v in zero else 0 for v in range(n_base))
    return Rebuild(orbit_sizes, fibres, bits)


# ---------------------------------------------------------------------------
# gates
# ---------------------------------------------------------------------------

def gate_pins() -> tuple[dict, dict]:
    payloads = {}
    for path in AUDIT_INPUT_PATHS:
        payloads[path] = (ROOT / path).read_bytes()
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    sha_ok = sha_rows == EXPECTED_SHA256
    blob_ok = blob_rows == EXPECTED_GIT_BLOBS
    receipt = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    # independent AST read of the primary's declared closure, family and laws
    tree = ast.parse(payloads[PRIMARY_PATH].decode("utf-8"),
                     filename=PRIMARY_PATH)
    declared: dict[str, object] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            try:
                declared[name] = ast.literal_eval(node.value)
            except (ValueError, TypeError, SyntaxError):
                continue
    primary_closure = tuple(declared.get("AUDIT_INPUT_PATHS") or ())
    closure_is_self_only = primary_closure == (PRIMARY_PATH,)
    family_matches = (
        declared.get("MAX_BASE_POINTS") == CHECK_MAX_BASE_POINTS
        and tuple(declared.get("FIBRE_ALPHABET_SMALL") or ())
        == CHECK_FIBRE_ALPHABET_SMALL
        and tuple(declared.get("FIBRE_ALPHABET_WIDE") or ())
        == CHECK_FIBRE_ALPHABET_WIDE
        and declared.get("WIDE_ALPHABET_FROM") == CHECK_WIDE_ALPHABET_FROM
        and declared.get("VERTEX_ENUMERATION_MAX_FIBRE_POINTS")
        == CHECK_VERTEX_MAX_FIBRE_POINTS
    )
    laws_match = (
        tuple(declared.get("SOLUTION_DIMENSION_LAW") or ()) == CHECK_SOLUTION_LAW
        and tuple(declared.get("PUSHFORWARD_DIMENSION_LAW") or ())
        == CHECK_PUSHFORWARD_LAW
        and tuple(declared.get("NORMALIZED_DIMENSION_LAW") or ())
        == CHECK_NORMALIZED_LAW
        and declared.get("DISJOINT_ORBIT_PHRASE") == CHECK_DISJOINT_PHRASE
        and declared.get("OUTSIDE_FIBRE_PHRASE") == CHECK_OUTSIDE_PHRASE
        and declared.get("DISJOINT_FIBRE_PHRASE") == CHECK_DISJOINT_FIBRE_PHRASE
    )
    if not sha_ok:
        disagree("pins", "declared input sha256 drift",
                 EXPECTED_SHA256, sha_rows)
    if not blob_ok:
        disagree("pins", "declared input git blob drift",
                 EXPECTED_GIT_BLOBS, blob_rows)
    if not closure_is_self_only:
        disagree("pins",
                 "the primary's declared closure is not exactly its own source",
                 (PRIMARY_PATH,), primary_closure)
    if not family_matches:
        disagree("pins", "the primary's declared family differs from the "
                         "checker's independent transcription",
                 {"MAX_BASE_POINTS": CHECK_MAX_BASE_POINTS},
                 {k: declared.get(k) for k in
                  ("MAX_BASE_POINTS", "FIBRE_ALPHABET_SMALL",
                   "FIBRE_ALPHABET_WIDE", "WIDE_ALPHABET_FROM",
                   "VERTEX_ENUMERATION_MAX_FIBRE_POINTS")})
    if not laws_match:
        disagree("pins", "the primary's declared dimension laws or their"
                         " rendering phrases differ from the checker's"
                         " independent transcription",
                 {"solution": list(CHECK_SOLUTION_LAW),
                  "pushforward": list(CHECK_PUSHFORWARD_LAW),
                  "normalized": list(CHECK_NORMALIZED_LAW)},
                 {k: declared.get(k) for k in
                  ("SOLUTION_DIMENSION_LAW", "PUSHFORWARD_DIMENSION_LAW",
                   "NORMALIZED_DIMENSION_LAW")})
    payload = {
        "certificate": "PINS",
        "declared_inputs": list(AUDIT_INPUT_PATHS),
        "both_declared_inputs_are_files_of_this_landing_delta": True,
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_all_match": sha_ok,
        "git_blobs_all_match": blob_ok,
        "primary_declared_closure": list(primary_closure),
        "primary_closure_is_its_own_source_only": closure_is_self_only,
        "primary_closure_contains_no_ancestor_artifact": True,
        "primary_family_matches_independent_transcription": family_matches,
        "primary_laws_match_independent_transcription": laws_match,
        "import_firewall_hits": list(FIREWALL.hits),
    }
    payload["pass"] = bool(sha_ok and blob_ok and closure_is_self_only
                           and family_matches and laws_match
                           and not FIREWALL.hits)
    return payload, receipt


def gate_dimension_table(receipt: dict) -> dict:
    family = rebuild_family()
    computed = computed_table()
    claimed = (receipt.get("certificates", {}).get("DIMENSION_LAWS", {}))
    own_digest = computed["digest"]
    own_sum = computed["sum"]
    claimed_digest = claimed.get("dimension_table_digest")
    claimed_count = claimed.get("instances")
    claimed_sum = claimed.get("dimension_sum")
    if own_digest != claimed_digest:
        disagree("dimension_table", "per-instance dimension table digest",
                 claimed_digest, own_digest)
    if claimed_count != len(family):
        disagree("dimension_table", "instance count",
                 claimed_count, len(family))
    if claimed_sum != own_sum:
        disagree("dimension_table", "dimension sum", claimed_sum, own_sum)
    if claimed.get("normalized_instances_checked") \
            != computed["normalized_checked"]:
        disagree("dimension_table", "instances with a disjoint orbit",
                 claimed.get("normalized_instances_checked"),
                 computed["normalized_checked"])
    if claimed.get("instances_declared") != len(family):
        disagree("dimension_table", "declared family size",
                 claimed.get("instances_declared"), len(family))
    if not claimed.get("every_declared_wrong_law_was_refuted"):
        disagree("dimension_table",
                 "the primary did not refute every declared wrong law",
                 True, claimed.get("every_declared_wrong_law_was_refuted"))
    payload = {
        "certificate": "DIMENSION_TABLE_REBUILT",
        "instances_rebuilt": len(family),
        "primes_used": list(PRIMES),
        "routes": ["modular rank", "rank-nullity split",
                   "rational reduced row echelon free-variable basis",
                   "modular rank of the support-restricted system"],
        "internal_route_mismatches": computed["route_mismatches"],
        "first_internal_mismatch": computed["first_mismatch"],
        "solution_law_mismatches": computed["law_mismatches"],
        "normalized_law_mismatches": computed["normalized_mismatches"],
        "normalized_instances_checked": computed["normalized_checked"],
        "checker_dimension_table_digest": own_digest,
        "receipt_dimension_table_digest": claimed_digest,
        "digest_agrees": own_digest == claimed_digest,
        "checker_dimension_sum": own_sum,
        "receipt_dimension_sum": claimed_sum,
        "instance_count_agrees": claimed_count == len(family),
    }
    payload["pass"] = bool(computed["route_mismatches"] == 0
                           and claimed.get("instances_declared") == len(family)
                           and computed["law_mismatches"] == 0
                           and computed["normalized_mismatches"] == 0
                           and own_digest == claimed_digest
                           and claimed_count == len(family)
                           and claimed_sum == own_sum
                           and claimed.get("every_declared_wrong_law_was_refuted"))
    return payload


def gate_base_level(receipt: dict) -> dict:
    family = rebuild_family()
    mismatches = computed_table()["base_mismatches"]
    claimed = (receipt.get("certificates", {})
               .get("DIMENSION_LAWS", {}).get("pushforward_law_failures"))
    if mismatches:
        disagree("base_level", "pushforward-mass dimension does not equal the "
                               "number of disjoint orbits", 0, mismatches)
    if claimed != 0:
        disagree("base_level", "receipt admits pushforward-law failures",
                 0, claimed)
    payload = {
        "certificate": "PUSHFORWARD_DIMENSION_REBUILT",
        "statement": ("on every rebuilt instance the pushforward-mass"
                      " dimension, computed by modular rank on the checker's"
                      " own base-level matrix, equals the number of orbits"
                      " disjoint from the required-zero subset"),
        "instances_rebuilt": len(family),
        "checker_mismatches": mismatches,
        "receipt_pushforward_law_failures": claimed,
    }
    payload["pass"] = bool(mismatches == 0 and claimed == 0)
    return payload


def gate_support_containment(receipt: dict) -> dict:
    computed = computed_support()
    claimed = (receipt.get("certificates", {}).get("SUPPORT_CONTAINMENT", {}))
    pairs = {
        "base_points_certified_outside_the_disjoint_orbits":
            computed["certified"],
        "control_base_points_inside_the_disjoint_orbits": computed["controls"],
        "base_points_declared": sum(inst.n_base for inst in rebuild_family()),
    }
    for name, value in pairs.items():
        if claimed.get(name) != value:
            disagree("support_containment", name, claimed.get(name), value)
    if computed["failures"]:
        disagree("support_containment",
                 "a base point outside the disjoint orbits has no constructive"
                 " certificate", 0, computed["failures"])
    if computed["control_defects"]:
        disagree("support_containment",
                 "an exhibited solution has zero mass at a base point of the"
                 " first disjoint orbit", 0, computed["control_defects"])
    payload = {
        "certificate": "SUPPORT_CONTAINMENT_REBUILT",
        "statement": ("for every base point outside the disjoint orbits the"
                      " checker BUILDS the fibre-total functional as an"
                      " explicit integer combination of its own constraint"
                      " rows and requires the result to equal the indicator,"
                      " so every non-negative solution vanishes there; at"
                      " base points of the first disjoint orbit an exhibited"
                      " solution carries nonzero mass, which is what makes"
                      " the test discriminating"),
        "checker_certified": computed["certified"],
        "checker_certificate_failures": computed["failures"],
        "checker_controls": computed["controls"],
        "checker_control_defects": computed["control_defects"],
        "receipt_counts": {k: claimed.get(k) for k in pairs},
        "counts_agree": all(claimed.get(k) == v for k, v in pairs.items()),
    }
    payload["pass"] = bool(not computed["failures"]
                           and not computed["control_defects"]
                           and all(claimed.get(k) == v
                                   for k, v in pairs.items()))
    return payload


def gate_extreme_points(receipt: dict) -> dict:
    computed = computed_extreme_points()
    claimed = (receipt.get("certificates", {}).get("EXTREME_POINTS", {}))
    pairs = {
        "instances_enumerated": computed["instances_enumerated"],
        "instances_in_the_declared_subfamily":
            computed["instances_enumerated"],
        "instances_where_a_product_of_simplices_would_give_another_count":
            computed[
                "instances_where_a_product_of_simplices_would_give_another_count"],
    }
    for name, value in pairs.items():
        if claimed.get(name) != value:
            disagree("extreme_points", name, claimed.get(name), value)
    if computed["extreme_point_set_mismatches"]:
        disagree("extreme_points",
                 "the enumerated extreme points are not the claimed ones",
                 0, computed["extreme_point_set_mismatches"])
    if claimed.get("extreme_point_set_mismatches") != 0:
        disagree("extreme_points", "receipt admits extreme-point mismatches",
                 0, claimed.get("extreme_point_set_mismatches"))
    payload = {
        "certificate": "EXTREME_POINTS_REBUILT",
        "statement": ("the checker re-enumerates every extreme point by brute"
                      " force over all supports in its own reversed layout and"
                      " compares the set with the weightings that place one"
                      " disjoint orbit's whole mass on a single fibre point at"
                      " each of that orbit's base points"),
        "checker_counts": computed,
        "receipt_counts": {k: claimed.get(k) for k in pairs},
        "counts_agree": all(claimed.get(k) == v for k, v in pairs.items()),
    }
    payload["pass"] = bool(not computed["extreme_point_set_mismatches"]
                           and claimed.get("extreme_point_set_mismatches") == 0
                           and all(claimed.get(k) == v
                                   for k, v in pairs.items()))
    return payload


def gate_witnesses(receipt: dict) -> dict:
    computed = computed_witnesses()
    rows: dict = computed["counts"]
    defects: list[str] = list(computed["defects"])
    claimed = (receipt.get("certificates", {})
               .get("NON_NEGATIVE_WITNESSES", {}))
    for name, value in rows.items():
        if claimed.get(name) != value:
            disagree("witnesses", name, claimed.get(name), value)
    if computed["biconditional_failures"]:
        disagree("witnesses",
                 "a witness exists exactly when the hypothesis holds",
                 0, computed["biconditional_failures"])
    swept_whole_family = (claimed.get("instances_visited")
                          == claimed.get("instances_declared")
                          == len(rebuild_family()))
    recounts_agree = (
        claimed.get("independent_recount_of_the_hypothesis")
        == rows["instances_satisfying_the_signed_witness_hypothesis"]
        and claimed.get("independent_recount_of_the_witnesses")
        == rows["instances_with_a_cross_orbit_signed_solution"])
    if not swept_whole_family:
        disagree("witnesses", "the primary's witness sweep did not visit the"
                              " whole declared family",
                 claimed.get("instances_visited"), len(rebuild_family()))
    if not recounts_agree:
        disagree("witnesses", "the primary's independent recounts",
                 {k: claimed.get(k) for k in
                  ("independent_recount_of_the_hypothesis",
                   "independent_recount_of_the_witnesses")},
                 {"hypothesis":
                  rows["instances_satisfying_the_signed_witness_hypothesis"],
                  "witnesses":
                  rows["instances_with_a_cross_orbit_signed_solution"]})
    payload = {
        "certificate": "WITNESSES_REBUILT",
        "statement": ("the checker rebuilds both non-negative normalized"
                      " representatives and the cross-orbit signed witness"
                      " from its own layout, recounts every advertised tally,"
                      " and tests the witness on EVERY instance -- its"
                      " existence condition does not mention a disjoint orbit"),
        "checker_counts": rows,
        "receipt_counts": {k: claimed.get(k) for k in rows},
        "checker_biconditional_failures": computed["biconditional_failures"],
        "primary_swept_the_whole_declared_family": swept_whole_family,
        "primary_independent_recounts_agree": recounts_agree,
        "defects": sorted(set(defects))[:8],
        "counts_agree": all(claimed.get(k) == v for k, v in rows.items()),
    }
    payload["pass"] = bool(not defects
                           and not computed["biconditional_failures"]
                           and swept_whole_family and recounts_agree
                           and all(claimed.get(k) == v for k, v in rows.items())
                           and rows["instances_with_a_disjoint_orbit"]
                           and rows["instances_with_a_cross_orbit_signed_solution"])
    return payload


def gate_large_instances(receipt: dict) -> dict:
    claimed_rows = (receipt.get("certificates", {})
                    .get("LARGE_DECLARED_INSTANCES", {}).get("rows", []))
    rows = []
    ok = bool(claimed_rows)
    for spec in claimed_rows:
        computed = computed_large(spec)
        own = computed["values"]
        representative_ok = computed["representative_ok"]
        agree = {k: (spec.get(k) == v) for k, v in own.items()}
        for k, matched in agree.items():
            if not matched:
                disagree("large_instances", f"{spec.get('name')}:{k}",
                         spec.get(k), own[k])
        if not representative_ok:
            disagree("large_instances",
                     f"{spec.get('name')}:representative", True, False)
        ok = ok and all(agree.values()) and representative_ok
        rows.append({"name": spec.get("name"), "checker_values": own,
                     "agrees": agree,
                     "representative_verified": representative_ok})
    payload = {
        "certificate": "LARGE_INSTANCES_REBUILT",
        "statement": ("each declared larger instance is rebuilt from the"
                      " receipt's declared parameters alone and every"
                      " advertised number is recomputed by the checker's"
                      " rank-nullity split, its own base-level modular rank"
                      " and its own representative"),
        "rows": rows,
    }
    payload["pass"] = bool(ok)
    return payload


def gate_theorem_text(receipt: dict) -> dict:
    """The sentences themselves, re-rendered from the checker's own law
    transcription and its own recomputed counts."""
    computed = computed_table()
    witnesses = computed_witnesses()["counts"]
    extreme = computed_extreme_points()
    expected = rendered_theorem(
        len(rebuild_family()),
        witnesses["instances_satisfying_the_signed_witness_hypothesis"],
        extreme["instances_enumerated"])
    claimed = receipt.get("theorem", {})
    differing = sorted(name for name in expected
                       if claimed.get(name) != expected[name])
    extra = sorted(set(claimed) - set(expected))
    for name in differing:
        disagree("theorem_text", f"theorem sentence {name}",
                 claimed.get(name), expected[name])
    if extra:
        disagree("theorem_text", "theorem field the checker does not render",
                 extra, [])
    declared_laws = receipt.get("declared_laws", {})
    laws_agree = (
        declared_laws.get("solution_dimension") == list(CHECK_SOLUTION_LAW)
        and declared_laws.get("pushforward_dimension")
        == list(CHECK_PUSHFORWARD_LAW)
        and declared_laws.get("normalized_dimension")
        == list(CHECK_NORMALIZED_LAW))
    if not laws_agree:
        disagree("theorem_text", "receipt's declared laws",
                 declared_laws,
                 {"solution_dimension": list(CHECK_SOLUTION_LAW),
                  "pushforward_dimension": list(CHECK_PUSHFORWARD_LAW),
                  "normalized_dimension": list(CHECK_NORMALIZED_LAW)})
    # a withdrawn sentence must not reappear anywhere in the receipt; the
    # primary's own published list of them is excluded from the scan
    scanned = copy.deepcopy(receipt)
    scanned.get("certificates", {}).pop("CLAIM_TEXT", None)
    text = compact(scanned)
    found = [sha256(fragment.encode("utf-8")).hexdigest()
             for fragment in CHECK_REFUTED_FRAGMENTS if fragment in text]
    if found:
        disagree("theorem_text", "withdrawn sentence found in the receipt",
                 [], found)
    payload = {
        "certificate": "THEOREM_TEXT_REBUILT",
        "statement": ("every theorem sentence in the receipt is re-rendered"
                      " here from the checker's own transcription of the"
                      " dimension laws and its own recomputed counts, and"
                      " compared character by character; the receipt is also"
                      " scanned for sentences withdrawn as false"),
        "sentences_compared": sorted(expected),
        "sentences_that_differ": differing,
        "receipt_fields_the_checker_does_not_render": extra,
        "declared_laws_agree": laws_agree,
        "withdrawn_sentence_digests_found": found,
        "withdrawn_sentence_digests_checked":
            [sha256(f.encode("utf-8")).hexdigest()
             for f in CHECK_REFUTED_FRAGMENTS],
    }
    payload["pass"] = bool(not differing and not extra and laws_agree
                           and not found)
    return payload


def gate_receipt_consistency(receipt: dict) -> dict:
    certificates = receipt.get("certificates", {})
    every_certificate_passes = all(bool(c.get("pass"))
                                   for c in certificates.values())
    claimed_all = bool(receipt.get("all_certificates_pass"))
    closure_self_only = receipt.get("AUDIT_INPUT_PATHS") == [PRIMARY_PATH]
    timeout = receipt.get("AUDIT_TIMEOUT_SEC")
    teeth = certificates.get("MUTATION_TEETH", {})
    teeth_all_bite = (teeth.get("teeth_total") == teeth.get("teeth_biting")
                      and (teeth.get("teeth_total") or 0) >= 18)
    families = teeth.get("check_families_covered") or []
    families_covered = len(families) >= 8
    self_containment = certificates.get("SELF_CONTAINMENT", {})
    no_external_reads = (
        self_containment.get("read_inventory", {})
        .get("external_or_ancestral_scientific_inputs") == []
        and not self_containment.get("repository_modules_imported"))
    if claimed_all and not every_certificate_passes:
        disagree("receipt_consistency",
                 "receipt claims all certificates pass while one does not",
                 True, False)
    if not closure_self_only:
        disagree("receipt_consistency",
                 "receipt evidence closure is not the primary's own source only",
                 [PRIMARY_PATH], receipt.get("AUDIT_INPUT_PATHS"))
    if not teeth_all_bite:
        disagree("receipt_consistency", "planted mutations do not all bite",
                 teeth.get("teeth_total"), teeth.get("teeth_biting"))
    if not families_covered:
        disagree("receipt_consistency",
                 "planted mutations do not cover every check family",
                 8, len(families))
    if not no_external_reads:
        disagree("receipt_consistency",
                 "the primary reports an external scientific read", [], "some")
    payload = {
        "certificate": "RECEIPT_CONSISTENCY",
        "every_certificate_in_the_receipt_passes": every_certificate_passes,
        "receipt_claims_all_pass": claimed_all,
        "evidence_closure_is_the_primary_source_only": closure_self_only,
        "declared_audit_timeout_sec": timeout,
        "planted_mutations_all_bite": teeth_all_bite,
        "check_families_the_mutations_cover": families,
        "primary_reports_no_external_scientific_read": no_external_reads,
    }
    payload["pass"] = bool(every_certificate_passes == claimed_all
                           and claimed_all and closure_self_only
                           and teeth_all_bite and families_covered
                           and no_external_reads
                           and timeout == AUDIT_TIMEOUT_SEC)
    return payload


# ---------------------------------------------------------------------------
# teeth: planted receipt corruptions, each must be refused
# ---------------------------------------------------------------------------

def run_teeth(receipt: dict) -> dict:
    teeth: list[dict] = []

    def bite(name: str, family: str, mutate, gate) -> None:
        spoiled = copy.deepcopy(receipt)
        mutate(spoiled)
        before = len(DISAGREEMENTS)
        payload = gate(spoiled)
        caught = (not payload.get("pass")) or len(DISAGREEMENTS) > before
        del DISAGREEMENTS[before:]
        teeth.append({"tooth": name, "check_family": family,
                      "bites": bool(caught)})

    bite("corrupt_dimension_table_digest", "dimension_table",
         lambda r: r["certificates"]["DIMENSION_LAWS"].__setitem__(
             "dimension_table_digest", "0" * 64),
         gate_dimension_table)
    bite("corrupt_instance_count", "dimension_table",
         lambda r: r["certificates"]["DIMENSION_LAWS"].__setitem__(
             "instances", 1),
         gate_dimension_table)
    bite("corrupt_dimension_sum", "dimension_table",
         lambda r: r["certificates"]["DIMENSION_LAWS"].__setitem__(
             "dimension_sum", 0),
         gate_dimension_table)
    bite("claim_a_wrong_law_was_not_refuted", "dimension_table",
         lambda r: r["certificates"]["DIMENSION_LAWS"].__setitem__(
             "every_declared_wrong_law_was_refuted", False),
         gate_dimension_table)
    bite("corrupt_pushforward_law_failures", "base_level",
         lambda r: r["certificates"]["DIMENSION_LAWS"].__setitem__(
             "pushforward_law_failures", 3),
         gate_base_level)
    bite("corrupt_support_containment_tally", "support_containment",
         lambda r: r["certificates"]["SUPPORT_CONTAINMENT"].__setitem__(
             "base_points_certified_outside_the_disjoint_orbits", 1),
         gate_support_containment)
    bite("corrupt_extreme_point_enumeration_tally", "extreme_points",
         lambda r: r["certificates"]["EXTREME_POINTS"].__setitem__(
             "instances_enumerated", 1),
         gate_extreme_points)
    bite("claim_the_product_shape_never_differs", "extreme_points",
         lambda r: r["certificates"]["EXTREME_POINTS"].__setitem__(
             "instances_where_a_product_of_simplices_would_give_another_count",
             0),
         gate_extreme_points)
    bite("corrupt_zero_count_witness_tally", "witnesses",
         lambda r: r["certificates"]["NON_NEGATIVE_WITNESSES"].__setitem__(
             "instances_where_zero_counts_differ", 0),
         gate_witnesses)
    bite("restrict_the_signed_witness_tally_to_disjoint_orbit_instances",
         "witnesses",
         lambda r: r["certificates"]["NON_NEGATIVE_WITNESSES"].__setitem__(
             "instances_with_a_cross_orbit_signed_solution", 2298),
         gate_witnesses)
    bite("corrupt_large_instance_solution_dimension", "large_instances",
         lambda r: r["certificates"]["LARGE_DECLARED_INSTANCES"]["rows"][0]
         .__setitem__("solution_space_dimension", 1),
         gate_large_instances)
    bite("corrupt_large_instance_normalized_dimension", "large_instances",
         lambda r: r["certificates"]["LARGE_DECLARED_INSTANCES"]["rows"][0]
         .__setitem__("non_negative_normalized_dimension", 0),
         gate_large_instances)
    bite("replace_a_theorem_sentence_with_a_false_one", "theorem_text",
         lambda r: r["theorem"].__setitem__(
             "pushforward_dimension",
             "the event-level weighting is unique up to scale"),
         gate_theorem_text)
    bite("shift_a_declared_law_coefficient", "theorem_text",
         lambda r: r["declared_laws"].__setitem__("solution_dimension",
                                                  [1, 1, 1]),
         gate_theorem_text)
    own_hypothesis = str(computed_witnesses()["counts"]
                         ["instances_satisfying_the_signed_witness_hypothesis"])
    bite("restate_a_theorem_count_that_the_run_did_not_produce", "theorem_text",
         lambda r: r["theorem"].__setitem__(
             "signed_solution_off_the_disjoint_orbits",
             r["theorem"]["signed_solution_off_the_disjoint_orbits"]
             .replace(own_hypothesis, str(int(own_hypothesis) + 1))),
         gate_theorem_text)
    bite("corrupt_evidence_closure_to_an_ancestor_pin", "receipt_consistency",
         lambda r: r.__setitem__(
             "AUDIT_INPUT_PATHS",
             [PRIMARY_PATH, "outputs/some_rejected_ancestor_receipt.json"]),
         gate_receipt_consistency)
    bite("launder_a_failed_certificate_into_all_pass", "receipt_consistency",
         lambda r: r["certificates"]["MUTATION_TEETH"].__setitem__("pass", False),
         gate_receipt_consistency)
    bite("drop_the_primary_mutation_families", "receipt_consistency",
         lambda r: r["certificates"]["MUTATION_TEETH"].__setitem__(
             "check_families_covered", ["basis"]),
         gate_receipt_consistency)

    payload = {
        "certificate": "TEETH",
        "statement": ("planted receipt corruptions, at least one per gate,"
                      " each applied to a deep copy and pushed through the"
                      " gate that owns it; every one must be refused"),
        "teeth": teeth,
        "teeth_total": len(teeth),
        "teeth_biting": sum(1 for t in teeth if t["bites"]),
        "check_families_covered": sorted({t["check_family"] for t in teeth}),
    }
    payload["pass"] = all(t["bites"] for t in teeth)
    return payload


def main() -> int:
    print("CYCLE906_INDEPENDENT_CHECK_SPECIFIED_TO_REFUTE")
    print("EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY")

    pins, receipt = gate_pins()
    ok = emit("PINS", pins)
    if not ok:
        print("VERDICT DISAGREES (declared inputs did not verify)")
        return 1

    order: list[str] = []
    certificates: dict[str, dict] = {}

    def record(payload: dict) -> bool:
        certificates[payload["certificate"]] = payload
        order.append(payload["certificate"])
        return emit(payload["certificate"], payload)

    certificates["PINS"] = pins
    order.append("PINS")
    ok &= record(gate_dimension_table(receipt))
    ok &= record(gate_base_level(receipt))
    ok &= record(gate_support_containment(receipt))
    ok &= record(gate_extreme_points(receipt))
    ok &= record(gate_witnesses(receipt))
    ok &= record(gate_large_instances(receipt))
    ok &= record(gate_theorem_text(receipt))
    ok &= record(gate_receipt_consistency(receipt))
    ok &= record(run_teeth(receipt))

    verdict = "CORROBORATES" if (ok and not DISAGREEMENTS) else "DISAGREES"
    summary = {
        "certificate": "VERDICT",
        "verdict": verdict,
        "disagreements": DISAGREEMENTS[:8],
        "disagreement_count": len(DISAGREEMENTS),
        "gates_run": order,
        "all_gates_pass": bool(ok),
        "pass": bool(ok and not DISAGREEMENTS),
    }
    emit("VERDICT", summary)

    out = {
        "runner": SELF_PATH,
        "checks": PRIMARY_PATH,
        "authority": "none",
        "audit": "unset",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "fraction_label": FRACTION_LABEL,
        "checker_verdict": verdict,
        "disagreements": DISAGREEMENTS,
        "certificates": {name: certificates[name] for name in order},
        "all_certificates_pass": bool(ok and not DISAGREEMENTS),
    }
    (ROOT / RECEIPT_PATH).write_text(
        json.dumps(out, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    print(f"RECEIPT {RECEIPT_PATH} sha256={digest(out)[:16]}")
    print(f"VERDICT {verdict}")
    return 0 if (ok and not DISAGREEMENTS) else 1


if __name__ == "__main__":
    sys.exit(main())
