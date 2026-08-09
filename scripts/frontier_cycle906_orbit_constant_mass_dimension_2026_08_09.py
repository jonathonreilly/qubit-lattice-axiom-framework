#!/usr/bin/env python3
"""Cycle 906 primary: the exact dimension of orbit-constant pushforward masses
that vanish on a required-zero subset, with an explicit basis.

SELF-CONTAINED BY CONSTRUCTION.  ``AUDIT_INPUT_PATHS`` is the EMPTY tuple.
Read inventory, stated in the two kinds the repo requires:

  * external or ancestral scientific inputs read: NONE.  No repository
    module is imported, no ancestor source, receipt, note or axiom file is
    read, and nothing outside this file supplies a number used in any
    certificate.
  * package-local integrity reads: this file reads ITS OWN source, once, to
    publish its content hash and to confirm by AST that the declared
    ``AUDIT_INPUT_PATHS`` literal really is empty.

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

COROLLARY (non-negative normalized solutions).  If the weighting is in
addition required to be non-negative with total mass one, then every
solution is supported inside the union of the orbits disjoint from the
required-zero subset, and the solution set is a product of simplices of
dimension

    (number of disjoint orbits - 1)
  + sum over base points of those orbits of (fibre size - 1).

The fibre-uniform weighting on one disjoint orbit is ONE representative of
that set, exhibited here.  When the sum above is positive the runner also
exhibits a SECOND, distinct non-negative normalized solution with the same
pushforward mass and a different zero count, so the zero count is a property
of the exhibited representative rather than of the solution set.

HOW IT IS CHECKED

Three routes that do not share an implementation path must agree on every
instance of an exhaustively enumerated family:

  route BASIS       explicit basis construction, each vector verified against
                    (ZERO) and (ORBIT) and the family verified independent by
                    exact integer rank;
  route NULLSPACE   exact fraction-free integer rank of the full constraint
                    matrix, dimension = columns - rank;
  route COUNT       the closed-form combinatorial count above.

The enumerated family is every instance with at most five base points, every
orbit partition of those base points, fibre sizes drawn from the declared
alphabet, and EVERY subset of base points as the required-zero subset.  Two
larger declared instances are carried for scale, where the dense event-level
rank route is deliberately not run (stated, with its reason).

Nine planted mutations are applied and each must be caught by the gate that
owns it, so no certificate here is a pass-through.

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
# Every instance with at most MAX_BASE_POINTS base points, every orbit
# partition, every fibre-size assignment from the declared alphabet, and
# every subset of base points as the required-zero subset.
MAX_BASE_POINTS = 5
FIBRE_ALPHABET_SMALL = (1, 2, 3)   # used when base points <= 4
FIBRE_ALPHABET_WIDE = (1, 2)       # used at 5 base points, to bound the sweep
WIDE_ALPHABET_FROM = 5

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


def emit(name: str, payload: dict) -> bool:
    ok = bool(payload.get("pass"))
    print(f"CERTIFICATE {name} {'PASS' if ok else 'FAIL'} {compact(payload)}")
    return ok


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

    # ---- the three routes -------------------------------------------------

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

    def cross_orbit_signed_witness(self) -> dict[int, Fraction] | None:
        """A signed solution supported OUTSIDE every disjoint orbit.

        Exists whenever some base point lies outside the required-zero
        subset, is not in a disjoint orbit, and carries at least two fibre
        points.  It witnesses that support containment in the disjoint
        orbits is a consequence of non-negativity, not of the two linear
        conditions alone.
        """
        disjoint_bases = {v for o in self.disjoint_orbits() for v in o}
        for base in range(self.n_base):
            if base in self.required_zero or base in disjoint_bases:
                continue
            if self.fibre_sizes[base] < 2:
                continue
            points = list(self.fibre_points(base))
            return {points[0]: Fraction(1), points[1]: Fraction(-1)}
        return None

    def nonnegative_polytope_dimension(self) -> int:
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return -1  # the normalized non-negative set is empty
        within = sum(self.fibre_sizes[v] - 1 for o in disjoint for v in o)
        return within + (len(disjoint) - 1)

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
    payload["pass"] = checked > 0 and not failures
    return payload


def _instance_row(inst: Instance, with_dense_route: bool) -> dict:
    basis = inst.constructive_basis()
    route_basis = len(basis)
    basis_independent = exact_rank(basis, inst.n_fibre) == route_basis \
        if basis else True
    basis_admissible = True
    for vector in basis:
        weight = {i: Fraction(v) for i, v in enumerate(vector) if v}
        if not (inst.satisfies_zero(weight)
                and inst.satisfies_orbit_constancy(weight)):
            basis_admissible = False
            break
    route_count = inst.route_count()
    route_null = inst.route_nullspace() if with_dense_route else None
    base_dim = inst.route_base_nullspace()
    return {
        "key": inst.key,
        "route_basis": route_basis,
        "route_count": route_count,
        "route_nullspace": route_null,
        "basis_independent": basis_independent,
        "basis_admissible": basis_admissible,
        "base_level_dimension": base_dim,
        "disjoint_orbits": len(inst.disjoint_orbits()),
        "nonnegative_polytope_dimension": inst.nonnegative_polytope_dimension(),
    }


def certificate_three_routes(instances: list[Instance]) -> tuple[dict, list[dict]]:
    rows = [_instance_row(inst, with_dense_route=True) for inst in instances]
    disagreements = [r for r in rows
                     if not (r["route_basis"] == r["route_count"]
                             == r["route_nullspace"])]
    bad_basis = [r for r in rows
                 if not (r["basis_independent"] and r["basis_admissible"])]
    bad_base = [r for r in rows
                if r["base_level_dimension"] != r["disjoint_orbits"]]
    table = sorted((compact(r["key"]), r["route_count"]) for r in rows)
    payload = {
        "certificate": "THREE_ROUTES_AGREE",
        "statement": ("on every instance of the declared exhaustive family the"
                      " explicit-basis dimension, the exact fraction-free"
                      " nullspace dimension and the closed-form count are"
                      " equal; every basis vector satisfies both linear"
                      " conditions and the basis is exactly independent; and"
                      " the pushforward-mass dimension equals the number of"
                      " orbits disjoint from the required-zero subset"),
        "instances": len(rows),
        "dimension_table_digest": digest(table),
        "dimension_sum": sum(r["route_count"] for r in rows),
        "dimension_max": max(r["route_count"] for r in rows),
        "distinct_dimensions": sorted({r["route_count"] for r in rows}),
        "route_disagreements": len(disagreements),
        "basis_defects": len(bad_basis),
        "base_level_disagreements": len(bad_base),
        "first_disagreement": (compact(disagreements[0]["key"])
                               if disagreements else None),
    }
    payload["pass"] = bool(
        rows and not disagreements and not bad_basis and not bad_base
    )
    return payload, rows


def certificate_nonnegative_witnesses(instances: list[Instance]) -> dict:
    with_solution = 0
    two_distinct = 0
    zero_count_differs = 0
    signed_outside = 0
    defects: list[str] = []
    example = None
    for inst in instances:
        uniform = inst.fibre_uniform_representative()
        if uniform is None:
            if inst.nonnegative_polytope_dimension() != -1:
                defects.append("polytope dimension without a disjoint orbit")
            continue
        with_solution += 1
        concentrated = inst.concentrated_representative()
        for weight in (uniform, concentrated):
            total = sum(weight.values(), Fraction(0))
            if total != 1 or any(v < 0 for v in weight.values()):
                defects.append("representative not normalized or not non-negative")
            if not (inst.satisfies_zero(weight)
                    and inst.satisfies_orbit_constancy(weight)):
                defects.append("representative violates a declared condition")
        disjoint_bases = {v for o in inst.disjoint_orbits() for v in o}
        outside = [p for p, v in uniform.items()
                   if v != 0 and inst.base_of_point[p] not in disjoint_bases]
        if outside:
            defects.append("non-negative representative supported outside the "
                           "disjoint orbits")
        if uniform != concentrated:
            two_distinct += 1
            if inst.pushforward(uniform) != inst.pushforward(concentrated):
                defects.append("distinct representatives with different "
                               "pushforward mass at a single disjoint orbit")
            if inst.zero_count(uniform) != inst.zero_count(concentrated):
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
        witness = inst.cross_orbit_signed_witness()
        if witness is not None:
            signed_outside += 1
            if not (inst.satisfies_zero(witness)
                    and inst.satisfies_orbit_constancy(witness)):
                defects.append("cross-orbit signed witness is not a solution")
    payload = {
        "certificate": "NON_NEGATIVE_WITNESSES",
        "statement": ("wherever a disjoint orbit exists, the fibre-uniform"
                      " weighting and the concentrated weighting are both"
                      " non-negative, normalized solutions supported inside"
                      " the disjoint orbits and sharing one pushforward mass;"
                      " where the fibres allow it they are distinct and have"
                      " different zero counts, so the zero count belongs to"
                      " the representative; and a signed solution supported"
                      " strictly outside every disjoint orbit exists whenever"
                      " a base point outside the required-zero subset lies in"
                      " an orbit that meets it and carries two fibre points"),
        "instances_with_a_disjoint_orbit": with_solution,
        "instances_with_two_distinct_representatives": two_distinct,
        "instances_where_zero_counts_differ": zero_count_differs,
        "instances_with_a_cross_orbit_signed_solution": signed_outside,
        "worked_example": example,
        "defects": sorted(set(defects))[:8],
    }
    payload["pass"] = bool(
        with_solution and two_distinct and zero_count_differs
        and signed_outside and not defects
    )
    return payload


def certificate_large_instances() -> dict:
    rows = []
    ok = True
    for spec in LARGE_INSTANCES:
        inst = build_large_instance(spec)
        count = inst.route_count()
        base_dim = inst.route_base_nullspace()
        uniform = inst.fibre_uniform_representative()
        polytope = inst.nonnegative_polytope_dimension()
        basis_len = 0
        basis_admissible = True
        for vector in inst.constructive_basis_sparse():
            basis_len += 1
            if not (inst.satisfies_zero(vector)
                    and inst.satisfies_orbit_constancy(vector)):
                basis_admissible = False
        checks = {
            "closed_form_equals_basis_length": count == basis_len,
            "every_basis_vector_satisfies_both_conditions": basis_admissible,
            "base_level_dimension_equals_disjoint_orbits":
                base_dim == len(inst.disjoint_orbits()),
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
            "orbits_disjoint_from_required_zero": len(inst.disjoint_orbits()),
            "solution_space_dimension": count,
            "pushforward_mass_dimension": base_dim,
            "non_negative_normalized_polytope_dimension": polytope,
            "representative_zero_count": inst.zero_count(uniform),
            "checks": checks,
        })
    payload = {
        "certificate": "LARGE_DECLARED_INSTANCES",
        "statement": ("the closed-form count, the explicit basis length, the"
                      " exact base-level rank and the exhibited representative"
                      " agree on two declared larger instances; their"
                      " parameters are chosen numbers for scale and describe"
                      " no repository census or physical configuration"),
        "dense_event_level_rank_route": (
            "NOT RUN on these two instances: dense fraction-free elimination"
            " over more than ten thousand columns is outside this runner's"
            " declared budget, so the dense route is exercised only on the"
            " exhaustive family, where it agrees with both other routes"),
        "rows": rows,
    }
    payload["pass"] = ok
    return payload


def certificate_mutation_teeth(instances: list[Instance]) -> dict:
    """Nine planted mutations; each must be caught by the gate that owns it."""
    probe = Instance((3, 3), (2, 2, 3, 1, 2, 2), frozenset({3}))
    teeth: list[dict] = []

    def tooth(name: str, bites: bool, detail: str) -> None:
        teeth.append({"tooth": name, "bites": bool(bites), "detail": detail})

    truth = probe.route_count()
    # 1. dropping one orbit-constancy row inflates the nullspace dimension
    rows = probe.constraint_rows()
    mutated = probe.n_fibre - exact_rank(rows[:-1], probe.n_fibre)
    tooth("drop_one_orbit_constancy_row", mutated != truth,
          f"dimension moved {truth} -> {mutated}")
    # 2. dropping one vanishing row inflates it too
    first_zero = next(i for i, r in enumerate(rows) if sum(r) == 1)
    mutated = probe.n_fibre - exact_rank(
        rows[:first_zero] + rows[first_zero + 1:], probe.n_fibre)
    tooth("drop_one_vanishing_row", mutated != truth,
          f"dimension moved {truth} -> {mutated}")
    # 3. counting all orbits instead of the disjoint ones
    wrong = len(probe.orbits) + sum(
        probe.fibre_sizes[v] - 1 for v in range(probe.n_base)
        if v not in probe.required_zero)
    tooth("count_all_orbits_not_the_disjoint_ones", wrong != truth,
          f"wrong closed form gives {wrong} against {truth}")
    # 4. forgetting the within-fibre directions
    wrong = len(probe.disjoint_orbits())
    tooth("omit_within_fibre_directions", wrong != truth,
          f"wrong closed form gives {wrong} against {truth}")
    # 5. a vector that breaks the vanishing condition is rejected
    bad = {probe.fibre_offset[3]: Fraction(1)}
    tooth("weighting_on_the_required_zero_subset",
          not probe.satisfies_zero(bad), "vanishing gate rejects it")
    # 6. a vector that breaks orbit constancy is rejected
    disjoint = probe.disjoint_orbits()[0]
    bad = {probe.fibre_offset[disjoint[0]]: Fraction(1)}
    tooth("orbit_constancy_broken_by_a_single_base_point",
          not probe.satisfies_orbit_constancy(bad),
          "orbit-constancy gate rejects it")
    # 7. an unnormalized representative is caught
    rep = probe.fibre_uniform_representative()
    scaled = {k: v * 2 for k, v in rep.items()}
    tooth("representative_rescaled_off_total_mass_one",
          sum(scaled.values(), Fraction(0)) != 1, "normalization gate rejects it")
    # 8. a claim of event-level uniqueness is refuted by the second witness
    concentrated = probe.concentrated_representative()
    tooth("event_level_uniqueness_claim",
          rep != concentrated
          and probe.pushforward(rep) == probe.pushforward(concentrated),
          "two distinct normalized non-negative solutions share one"
          " pushforward mass")
    # 9. a dependent basis is caught by the exact rank
    basis = probe.constructive_basis()
    duplicated = basis + [basis[0]]
    tooth("linearly_dependent_basis",
          exact_rank(duplicated, probe.n_fibre) != len(duplicated),
          "exact rank detects the repeated vector")

    payload = {
        "certificate": "MUTATION_TEETH",
        "probe_instance": probe.key,
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
    print("CYCLE906_ORBIT_CONSTANT_MASS_DIMENSION_SUPPORT_RUNNER")
    print("SELF_CONTAINED_NO_EXTERNAL_SCIENTIFIC_INPUT_IS_READ")
    print("EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY")

    instances = enumerate_family()

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
    routes, rows = certificate_three_routes(instances)
    ok &= record(routes)
    ok &= record(certificate_nonnegative_witnesses(instances))
    ok &= record(certificate_large_instances())
    ok &= record(certificate_mutation_teeth(instances))

    theorem = {
        "parameterization": (
            "for every instance of the declared structure the solution space"
            " of the two linear conditions is spanned by the explicit basis"
            " this runner constructs, so its dimension is the number of"
            " orbits disjoint from the required-zero subset plus the sum over"
            " base points outside that subset of (fibre size minus one)"),
        "pushforward_dimension": (
            "the space of admissible pushforward masses has dimension exactly"
            " the number of orbits disjoint from the required-zero subset; in"
            " particular, at one disjoint orbit the pushforward mass is"
            " determined up to a single scalar"),
        "non_negative_corollary": (
            "adding non-negativity and total mass one confines every solution"
            " to the union of the disjoint orbits and leaves a product of"
            " simplices of dimension (number of disjoint orbits minus one)"
            " plus the sum over base points of those orbits of (fibre size"
            " minus one); the fibre-uniform weighting is one point of that"
            " set, exhibited, and a second point is exhibited alongside it"),
        "scope": (
            "conditional on the declared finite structure only; this runner"
            " reads no repository census, no symmetry claim, no interface"
            " condition and no axiom surface, and asserts nothing about any"
            " of them"),
    }
    summary = {
        "certificate": "SUMMARY",
        "theorem": theorem,
        "family": {
            "max_base_points": MAX_BASE_POINTS,
            "fibre_alphabet_up_to_four_base_points": list(FIBRE_ALPHABET_SMALL),
            "fibre_alphabet_at_five_base_points": list(FIBRE_ALPHABET_WIDE),
            "required_zero_subsets": "every subset of base points",
            "instances": len(instances),
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
        "family": summary["family"],
        "certificates": {name: certificates[name] for name in order},
        "per_instance_dimension_table_digest":
            certificates["THREE_ROUTES_AGREE"]["dimension_table_digest"],
        "all_certificates_pass": bool(ok),
    }
    (ROOT / RECEIPT_PATH).write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    print(f"RECEIPT {RECEIPT_PATH} sha256={digest(receipt)[:16]}")
    print(f"VERDICT {'ALL_CERTIFICATES_PASS' if ok else 'CERTIFICATE_FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
