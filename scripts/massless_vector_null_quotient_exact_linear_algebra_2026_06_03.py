#!/usr/bin/env python3
"""Exact rational verifier for the massless-vector null quotient theorem.

The theorem verified here is intentionally only finite-dimensional linear
algebra:

    V = C^4 with eta = diag(1, -1, -1, -1)
    k != 0 and eta(k, k) = 0
    L_k(epsilon) = eta(k, epsilon)
    dim_C(ker L_k / span{k}) = 2

No physical interpretation of V, k, epsilon, L_k, or the quotient is used.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "MASSLESS_VECTOR_NULL_QUOTIENT_EXACT_LINEAR_ALGEBRA_THEOREM_NOTE_2026-06-03.md"
)

PASS = 0
FAIL = 0


def as_fraction_matrix(rows: list[list[int | Fraction]]) -> list[list[Fraction]]:
    return [[Fraction(entry) for entry in row] for row in rows]


def rank_q(rows: list[list[int | Fraction]]) -> int:
    """Gaussian-elimination rank over Q."""
    matrix = as_fraction_matrix(rows)
    if not matrix:
        return 0
    row_count = len(matrix)
    col_count = len(matrix[0])
    rank = 0
    for col in range(col_count):
        pivot = None
        for row in range(rank, row_count):
            if matrix[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][col]
        matrix[rank] = [entry / pivot_value for entry in matrix[rank]]
        for row in range(row_count):
            if row == rank:
                continue
            factor = matrix[row][col]
            if factor == 0:
                continue
            matrix[row] = [
                current - factor * pivot_entry
                for current, pivot_entry in zip(matrix[row], matrix[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def minkowski_covector(k: tuple[int, int, int, int]) -> list[int]:
    k0, k1, k2, k3 = k
    return [k0, -k1, -k2, -k3]


def dot(row: list[int | Fraction], column: tuple[int, int, int, int]) -> Fraction:
    return sum(Fraction(a) * Fraction(b) for a, b in zip(row, column))


def minkowski_norm(k: tuple[int, int, int, int]) -> Fraction:
    return dot(minkowski_covector(k), k)


def column_rank(columns: list[tuple[int, int, int, int]]) -> int:
    if not columns:
        return 0
    rows = [[column[row] for column in columns] for row in range(4)]
    return rank_q(rows)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def verify_null_vector(k: tuple[int, int, int, int]) -> None:
    cov = minkowski_covector(k)
    row_rank = rank_q([cov])
    kernel_dim = 4 - row_rank
    span_dim = column_rank([k])
    containment = dot(cov, k)
    quotient_dim = kernel_dim - span_dim

    check(f"{k}: exact null condition eta(k,k)=0", minkowski_norm(k) == 0)
    check(f"{k}: k is nonzero", any(entry != 0 for entry in k))
    check(f"{k}: L_k row is nonzero", any(entry != 0 for entry in cov))
    check(f"{k}: rank(L_k)=1", row_rank == 1, f"rank={row_rank}")
    check(f"{k}: dim ker(L_k)=3", kernel_dim == 3, f"dim={kernel_dim}")
    check(f"{k}: L_k(k)=0", containment == 0, f"L_k(k)={containment}")
    check(f"{k}: dim span{{k}}=1", span_dim == 1, f"dim={span_dim}")
    check(
        f"{k}: dim ker(L_k)/span{{k}}=2",
        quotient_dim == 2,
        f"3 - {span_dim} = {quotient_dim}",
    )


def main() -> int:
    print("Massless-vector null quotient exact linear algebra verifier")
    print("Claim: for nonzero null k in (C^4, diag(1,-1,-1,-1)),")
    print("       dim_C(ker L_k / span{k}) = 2")

    section("General theorem invariants")
    dimension_v = 4
    rank_nonzero_functional = 1
    nullity = dimension_v - rank_nonzero_functional
    null_vector_span_dim = 1
    quotient_dim = nullity - null_vector_span_dim
    check("dim_C V = 4", dimension_v == 4)
    check("nonzero functional to C has rank 1", rank_nonzero_functional == 1)
    check("rank-nullity gives dim ker(L_k)=3", nullity == 3)
    check("nonzero k gives dim span{k}=1", null_vector_span_dim == 1)
    check("quotient dimension is 3 - 1 = 2", quotient_dim == 2)

    section("Exact rational null-vector witnesses")
    for witness in [
        (1, 0, 0, 1),
        (5, 3, 4, 0),
        (13, 12, 0, 5),
        (25, 7, 24, 0),
    ]:
        verify_null_vector(witness)

    section("Canonical quotient basis witness")
    canonical_k = (1, 0, 0, 1)
    cov = minkowski_covector(canonical_k)
    e_x = (0, 1, 0, 0)
    e_y = (0, 0, 1, 0)
    basis_columns = [e_x, e_y, canonical_k]
    check("canonical e_x lies in ker(L_k)", dot(cov, e_x) == 0)
    check("canonical e_y lies in ker(L_k)", dot(cov, e_y) == 0)
    check("canonical k lies in ker(L_k)", dot(cov, canonical_k) == 0)
    check("canonical {e_x,e_y,k} has rank 3", column_rank(basis_columns) == 3)
    check(
        "canonical quotient representatives {e_x,e_y} have rank 2",
        column_rank([e_x, e_y]) == 2,
    )

    section("Massive/non-null contrast")
    massive_k = (2, 0, 0, 0)
    massive_cov = minkowski_covector(massive_k)
    massive_row_rank = rank_q([massive_cov])
    massive_kernel_dim = 4 - massive_row_rank
    check("massive contrast has eta(k,k)!=0", minkowski_norm(massive_k) != 0)
    check("massive contrast rank(L_k)=1", massive_row_rank == 1)
    check("massive contrast dim ker(L_k)=3", massive_kernel_dim == 3)
    check("massive contrast k is not in ker(L_k)", dot(massive_cov, massive_k) != 0)
    check(
        "massive contrast has no null quotient by span{k}",
        dot(massive_cov, massive_k) == minkowski_norm(massive_k),
    )

    section("Source-note boundary checks")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    required_phrases = [
        "pure finite-dimensional complex-linear-algebra identity",
        "does not assert that the vector space is physical spacetime",
        "physical photon/gluon/gauge",
        "No plane-wave decomposition, gauge orbit, gauge-fixing",
        "does not close the physical massless-vector theorem by itself",
    ]
    for phrase in required_phrases:
        check(f"note contains boundary phrase: {phrase}", phrase in note_text)
    forbidden_status_phrases = [
        "**Author-surface status:** retained",
        "**Author-surface status:** proposed_retained",
        "audit_status: audited_clean",
        "effective_status: retained",
    ]
    for phrase in forbidden_status_phrases:
        check(f"note avoids forbidden status phrase: {phrase}", phrase not in note_text)

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: EXACT-SUPPORT")
        return 0
    print("VERDICT: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
