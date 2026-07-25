#!/usr/bin/env python3
"""Cycle 693: the exact additive consequence of the Record readout clauses.

The accepted Record wording supplies content determinacy, finite additivity on
pairwise-disjoint record collections, and the empty value.  It follows that
each such readout is uniquely determined by its singleton content weights.

The stronger complex function-algebra carrier used by the post-record
semigroup theorem does not follow without further structure:

* the framework does not force a finite record-content alphabet;
* Record does not name C as the scalar codomain or operationally supply every
  mathematical content-weight rule;
* the additive reduct does not select a physical algebra product.

The parent theorem already names pointwise multiplication.  This runner does
not call that standard construction an unnamed input; it only checks that the
Record additive reduct alone cannot distinguish it from another unital
commutative product on the same finite-dimensional vector space.

All scored computations use exact integer or Fraction arithmetic.  The runner
imports no repository content.
"""

from __future__ import annotations

import itertools
import json
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


# Three record identities.  Records 0 and 1 share content "a"; record 2 has
# content "b".  A configuration is a bit mask, so all collections are finite
# and records are pairwise distinct even when their contents agree.
CONFIGS = tuple(range(8))
CONTENT = ("a", "a", "b")


def content_counts(mask: int) -> dict[str, int]:
    counts = {"a": 0, "b": 0}
    for record_id, content in enumerate(CONTENT):
        if mask & (1 << record_id):
            counts[content] += 1
    return counts


def compatible(values: tuple[F, ...]) -> bool:
    """The finite fixture's exact (D)+(A)+(Z) constraint predicate."""
    if values[0] != 0:
        return False
    if values[1] != values[2]:  # singleton records with the same content
        return False
    for left in CONFIGS:
        for right in CONFIGS:
            if left & right:
                continue
            if values[left | right] != values[left] + values[right]:
                return False
    return True


def factorized_values(weight_a: F, weight_b: F) -> tuple[F, ...]:
    result = []
    for mask in CONFIGS:
        counts = content_counts(mask)
        result.append(counts["a"] * weight_a + counts["b"] * weight_b)
    return tuple(result)


def constraint_rows() -> list[list[F]]:
    """Linear equations for arbitrary I(S), without constructing I from f."""
    rows: list[list[F]] = []
    empty = [F(0) for _ in CONFIGS]
    empty[0] = F(1)
    rows.append(empty)
    same_content = [F(0) for _ in CONFIGS]
    same_content[1] = F(1)
    same_content[2] = F(-1)
    rows.append(same_content)
    for left in CONFIGS:
        for right in CONFIGS:
            if left & right:
                continue
            row = [F(0) for _ in CONFIGS]
            row[left | right] += 1
            row[left] -= 1
            row[right] -= 1
            rows.append(row)
    return rows


def rational_rank(rows: list[list[F]]) -> int:
    matrix = [list(map(F, row)) for row in rows]
    if not matrix:
        return 0
    nrows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next(
            (row for row in range(pivot_row, nrows) if matrix[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(nrows):
            if row == pivot_row or matrix[row][col] == 0:
                continue
            multiple = matrix[row][col]
            matrix[row] = [
                entry - multiple * pivot_entry
                for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def satisfies(rows: list[list[F]], vector: tuple[F, ...]) -> bool:
    return all(
        sum((coefficient * value for coefficient, value in zip(row, vector)), F(0))
        == 0
        for row in rows
    )


Matrix = tuple[F, F, F, F]
Vector = tuple[F, F, F]


def is_scalar_matrix(matrix: Matrix) -> bool:
    a, b, c, d = matrix
    return b == 0 and c == 0 and a == d


def available(matrix: Matrix, occupied_neighbors: tuple[int, ...]) -> bool:
    """A fixed covariant varying rule: full M2 for even count, center for odd."""
    if sum(occupied_neighbors) % 2 == 0:
        return True
    return is_scalar_matrix(matrix)


@dataclass(frozen=True)
class Record:
    site: tuple[int, int, int]
    content: Matrix


def matrix_trace(matrix: Matrix) -> F:
    return matrix[0] + matrix[3]


def record_readout(records: tuple[Record, ...]) -> F:
    return sum((matrix_trace(record.content) for record in records), F(0))


def add(u: Vector, v: Vector) -> Vector:
    return tuple(a + b for a, b in zip(u, v))  # type: ignore[return-value]


def pointwise(u: Vector, v: Vector) -> Vector:
    return (u[0] * v[0], u[1] * v[1], u[2] * v[2])


def truncated(u: Vector, v: Vector) -> Vector:
    """C[x]/(x^3), in the basis (1,x,x^2)."""
    return (
        u[0] * v[0],
        u[0] * v[1] + u[1] * v[0],
        u[0] * v[2] + u[1] * v[1] + u[2] * v[0],
    )


def algebra_laws(multiply, unit: Vector, grid: tuple[Vector, ...]) -> bool:
    if not grid:
        return False
    for u in grid:
        if multiply(unit, u) != u or multiply(u, unit) != u:
            return False
    for u in grid:
        for v in grid:
            if multiply(u, v) != multiply(v, u):
                return False
            for w in grid:
                if multiply(multiply(u, v), w) != multiply(u, multiply(v, w)):
                    return False
                if multiply(u, add(v, w)) != add(multiply(u, v), multiply(u, w)):
                    return False
    return True


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 693,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    # R1: start from every arbitrary candidate map on the fixture, filter by
    # the clauses, and check the converse factorization.  This is deliberately
    # not a list of maps first constructed from content weights.
    value_grid = tuple(F(v) for v in range(-1, 2))
    candidates = itertools.product(value_grid, repeat=len(CONFIGS))
    compatible_maps = [values for values in candidates if compatible(values)]
    factorization_failures = []
    for values in compatible_maps:
        expected = factorized_values(values[1], values[4])
        if values != expected:
            factorization_failures.append((values, expected))
    check(
        "arbitrary-map exhaustive converse is non-vacuous and every compatible "
        "fixture readout factors uniquely through singleton content weights",
        bool(compatible_maps) and not factorization_failures,
        {
            "candidate_maps": len(value_grid) ** len(CONFIGS),
            "compatible_maps": len(compatible_maps),
            "factorization_failures": len(factorization_failures),
        },
    )

    # R2: negative controls ensure the compatibility filter is live.
    good = factorized_values(F(1), F(-1))
    nonadditive = list(good)
    nonadditive[3] += 1
    content_mismatch = list(good)
    content_mismatch[2] += 1
    check(
        "compatibility predicate accepts the exact factorized rule and rejects "
        "independent additivity and content-determinacy corruptions",
        compatible(good)
        and not compatible(tuple(nonadditive))
        and not compatible(tuple(content_mismatch)),
        {
            "good_accepted": compatible(good),
            "nonadditive_rejected": not compatible(tuple(nonadditive)),
            "content_mismatch_rejected": not compatible(tuple(content_mismatch)),
        },
    )

    # R3: an independent exact linear-system route proves that the full solution
    # space on the fixture is two-dimensional and is spanned by the two content
    # count functions.
    equations = constraint_rows()
    equation_rank = rational_rank(equations)
    solution_dimension = len(CONFIGS) - equation_rank
    basis_a = factorized_values(F(1), F(0))
    basis_b = factorized_values(F(0), F(1))
    factor_basis_rank = rational_rank([list(basis_a), list(basis_b)])
    check(
        "exact linear constraint system has precisely the singleton-content "
        "factorization space as its solution space",
        solution_dimension == 2
        and factor_basis_rank == 2
        and satisfies(equations, basis_a)
        and satisfies(equations, basis_b),
        {
            "equations": len(equations),
            "rank": equation_rank,
            "solution_dimension": solution_dimension,
            "factor_basis_rank": factor_basis_rank,
        },
    )
    summary["additive_factorization"] = (
        "derived for each supplied additive scalar codomain and realized content set"
    )

    # R4: finite fixture for the full-model counterexample in the note.  The
    # written proof supplies the infinite family and full M2(C) domain; here we
    # exhaust all six-neighbor occupancy patterns/permutations and test a
    # nonempty exact content family.
    neighbor_patterns = tuple(itertools.product((0, 1), repeat=6))
    neighbor_permutations = tuple(itertools.permutations(range(6)))
    noncentral: Matrix = (F(1), F(0), F(0), F(0))
    covariant = all(
        available(noncentral, pattern)
        == available(noncentral, tuple(pattern[index] for index in permutation))
        for pattern in neighbor_patterns
        for permutation in neighbor_permutations
    )
    varying = available(noncentral, (0, 0, 0, 0, 0, 0)) and not available(
        noncentral, (1, 0, 0, 0, 0, 0)
    )
    integers = tuple(range(-10, 11))
    records = tuple(
        Record(
            site=(3 * index, 0, 0),
            content=(F(value), F(0), F(0), F(0)),
        )
        for index, value in enumerate(integers)
    )
    distinct_contents = len({record.content for record in records}) == len(records)
    distinct_nonadjacent_sites = all(
        left.site != right.site
        and sum(abs(a - b) for a, b in zip(left.site, right.site)) != 1
        for index, left in enumerate(records)
        for right in records[index + 1 :]
    )
    all_available_empty = all(
        available(record.content, (0, 0, 0, 0, 0, 0)) for record in records
    )
    split = 9
    additive = record_readout(records) == (
        record_readout(records[:split]) + record_readout(records[split:])
    )
    duplicate_left = Record(site=(0, 3, 0), content=records[4].content)
    duplicate_right = Record(site=(0, 6, 0), content=records[4].content)
    determinate = record_readout((duplicate_left,)) == record_readout(
        (duplicate_right,)
    )
    check(
        "full-framework infinite-content countermodel construction has a "
        "covariant varying admissibility rule and content-only finite-additive "
        "readout on a nonempty exact fixture",
        covariant
        and varying
        and bool(records)
        and distinct_contents
        and distinct_nonadjacent_sites
        and all_available_empty
        and record_readout(()) == 0
        and additive
        and determinate,
        {
            "neighbor_patterns": len(neighbor_patterns),
            "neighbor_permutations": len(neighbor_permutations),
            "distinct_contents_tested": len(records),
            "covariant": covariant,
            "varying": varying,
            "additive": additive,
            "determinate": determinate,
        },
    )
    summary["finite_alphabet"] = (
        "not entailed; full-framework infinite-content countermodel exhibited"
    )

    # R5: both products satisfy the algebra laws on a declared nonempty exact
    # grid.  Their formulas make bilinearity/associativity universal; this grid
    # is an executable cross-check rather than the proof by itself.
    coefficient_grid = tuple(F(v) for v in range(-1, 2))
    vectors = tuple(itertools.product(coefficient_grid, repeat=3))
    pointwise_laws = algebra_laws(pointwise, (F(1), F(1), F(1)), vectors)
    truncated_laws = algebra_laws(truncated, (F(1), F(0), F(0)), vectors)
    check(
        "pointwise C^3 and truncated C[x]/(x^3) are both commutative "
        "associative unital distributive products on the same additive fixture",
        bool(vectors) and pointwise_laws and truncated_laws,
        {
            "vectors": len(vectors),
            "pointwise_laws": pointwise_laws,
            "truncated_laws": truncated_laws,
        },
    )

    # R6: exact nilpotent witness.  In pointwise C^3, coordinatewise w^n=0
    # implies each complex coordinate is zero; the finite grid below is only a
    # check of the implementation against that field-theoretic proof.
    zero: Vector = (F(0), F(0), F(0))
    x: Vector = (F(0), F(1), F(0))
    x2 = truncated(x, x)
    x3 = truncated(x2, x)
    pointwise_nilpotents = [
        vector
        for vector in vectors
        if vector != zero and pointwise(pointwise(vector, vector), vector) == zero
    ]
    check(
        "non-isomorphic product witness: x is nonzero with x^2 nonzero and "
        "x^3=0 in C[x]/(x^3), while the pointwise fixture has no nonzero "
        "nilpotent",
        x != zero and x2 != zero and x3 == zero and not pointwise_nilpotents,
        {
            "x": str(x),
            "x_squared": str(x2),
            "x_cubed": str(x3),
            "pointwise_grid_nilpotents": len(pointwise_nilpotents),
        },
    )
    summary["complex_scalar_carrier"] = (
        "not derived by Record; scalar codomain and operational closure remain inputs"
    )
    summary["algebra_product"] = (
        "not selected by the additive Record reduct; parent already names pointwise multiplication"
    )

    summary["conclusion"] = (
        "Record derives singleton-content factorization for each supplied "
        "additive scalar codomain. It does not by itself supply a finite "
        "content alphabet, a complex operational carrier, or a physical "
        "event-algebra product identification."
    )
    summary["firewalls"] = {
        "dynamics_probability_or_measurement_claimed": False,
        "physical_carrier_identified": False,
        "new_axiom_or_primitive_proposed": False,
        "pointwise_product_called_unnamed_input": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_record_readout_carrier_three_way_split_cycle693_receipt_2026_07_25.json"
    )
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(
            json.dumps(summary, indent=1, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT RECORD_ADDITIVE_FACTOR_BOUNDARY_FAILED")
        return 1
    print("RESULT RECORD_FIXES_ADDITIVE_FORM_NOT_FINITE_COMPLEX_EVENT_ALGEBRA")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
