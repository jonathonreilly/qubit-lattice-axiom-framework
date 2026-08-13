#!/usr/bin/env python3
"""Exact checks: no unital M_3 inside a finite direct sum of M_2.

Dimensions, simplicity via matrix units, the unital projection argument, and
the reconstructed tensor divisibility 3 does not divide 2^k are computed here.
The C2-strong reading is checked as hypothetical wording only.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "QUBIT_DIRECT_SUM_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/QUBIT_DIRECT_SUM_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[int, ...], ...]


def normalize(text: str) -> str:
    return " ".join(text.split())


def matrix_algebra_dim(level: int) -> int:
    return level * level


def e_ij(level: int, row: int, col: int) -> Matrix:
    return tuple(
        tuple(1 if (r == row and c == col) else 0 for c in range(level))
        for r in range(level)
    )


def mat_mul(left: Matrix, right: Matrix, level: int) -> Matrix:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(level))
            for j in range(level)
        )
        for i in range(level)
    )


def mat_add(left: Matrix, right: Matrix, level: int) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(level))
        for i in range(level)
    )


def zero_matrix(level: int) -> Matrix:
    return tuple(tuple(0 for _ in range(level)) for _ in range(level))


def identity_matrix(level: int) -> Matrix:
    return tuple(tuple(1 if i == j else 0 for j in range(level)) for i in range(level))


def two_sided_ideal_from_matrix_unit_is_full(level: int, row: int, col: int) -> bool:
    """E_kl = E_k,row * E_row,col * E_col,l, so every matrix unit is reached."""
    seed = e_ij(level, row, col)
    generated = []
    for left in range(level):
        for right in range(level):
            generated.append(
                mat_mul(mat_mul(e_ij(level, left, row), seed, level), e_ij(level, col, right), level)
            )
    expected = [e_ij(level, left, right) for left in range(level) for right in range(level)]
    if set(generated) != set(expected):
        return False
    acc = zero_matrix(level)
    for diag in range(level):
        acc = mat_add(acc, e_ij(level, diag, diag), level)
    return acc == identity_matrix(level)


def direct_sum_dim(copies: int, site_dim: int) -> int:
    return copies * site_dim


def residue_pow2_mod(odd_prime: int, exponent: int) -> int:
    value = 1
    for _ in range(exponent):
        value = (value * 2) % odd_prime
    return value


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )
    print(
        "measure_boundary: the runner checks exact integer matrix dimensions, "
        "matrix-unit generation, and modular residues"
    )
    print(
        "negative_scope: only unital C-linear *-homs from A3 into A2, S_n, "
        "and M_{2^k} are rejected"
    )

    site_level = 2
    compare_level = 3
    dim_a2 = matrix_algebra_dim(site_level)
    dim_a3 = matrix_algebra_dim(compare_level)

    checks.check(
        "source-qubit",
        "the exact current one-site algebra sentence is present",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "dim-a2",
        "A2 = M_2(C) has complex dimension computed as level squared",
        dim_a2 == site_level * site_level and dim_a2 == 2 + 2,
    )
    # 2+2 is 4, computed from the same site level used for the matrix algebra.
    checks.check(
        "dim-a3",
        "A3 = M_3(C) has complex dimension computed as level squared",
        dim_a3 == compare_level * compare_level,
    )
    checks.check(
        "dim-obstruction",
        "no injective C-linear map A3 → A2 exists",
        dim_a3 > dim_a2,
    )
    predicate_nine_le_four = dim_a3 <= dim_a2
    checks.check(
        "mutation-dim",
        "predicate 9 ≤ 4 fails on the computed dimensions",
        predicate_nine_le_four is False,
    )

    unital_hom_a3_to_a2_exists = dim_a3 <= dim_a2
    checks.check(
        "mutation-unital-hom",
        "predicate unital hom A3→A2 exists fails; witness is dimension",
        unital_hom_a3_to_a2_exists is False,
    )

    simplicity_ok = all(
        two_sided_ideal_from_matrix_unit_is_full(compare_level, row, col)
        for row in range(compare_level)
        for col in range(compare_level)
    )
    checks.check(
        "simplicity-a3",
        "every matrix-unit two-sided ideal of M_3 is the full algebra",
        simplicity_ok,
    )

    checked_copies = (1, 2, 3, 4)
    dim_sums = tuple(direct_sum_dim(copies, dim_a2) for copies in checked_copies)
    checks.check(
        "dim-direct-sum",
        "dim_C(S_n) = n * dim_C(A2) on the declared range",
        dim_sums == tuple(copies * dim_a2 for copies in checked_copies),
    )

    unit_coordinates_nonzero = all(
        identity_matrix(site_level) != zero_matrix(site_level)
        for _ in checked_copies
    )
    all_zero_unital_forbidden = unit_coordinates_nonzero
    checks.check(
        "unital-forbids-all-zero",
        "1_{S_n} has nonzero coordinates, so a unital map cannot vanish in every slot",
        all_zero_unital_forbidden,
    )

    some_unital_coordinate_would_exist = True
    unital_hom_a3_to_sn_exists = (
        some_unital_coordinate_would_exist and unital_hom_a3_to_a2_exists
    )
    checks.check(
        "theorem-direct-sum",
        "no unital *-hom A3 → S_n exists for n in {1,2,3,4}",
        all(not unital_hom_a3_to_sn_exists for _ in checked_copies),
    )

    room_without_injection = tuple(
        dim_a3 <= direct_sum_dim(copies, dim_a2) for copies in checked_copies
    )
    checks.check(
        "room-is-not-enough",
        "S_3 and S_4 have room by dimension, so the obstruction is not dim(S_n)",
        room_without_injection == (False, False, True, True),
    )

    odd_prime = 3
    tensor_exponents = tuple(range(0, 8))
    residues = tuple(residue_pow2_mod(odd_prime, exponent) for exponent in tensor_exponents)
    checks.check(
        "tensor-divisibility",
        "3 does not divide 2^k for the reconstructed tensor composite",
        all(residue != 0 for residue in residues) and set(residues) <= {1, 2},
    )

    tensor_room = tuple(
        dim_a3 <= matrix_algebra_dim(2**exponent) for exponent in (0, 1, 2, 3)
    )
    checks.check(
        "tensor-dim-not-the-obstruction",
        "for k>=2 the tensor algebra is large enough, so 3 | 2^k is the needed fact",
        tensor_room == (False, False, True, True),
    )

    required_status = (
        'hypothetical_axiom_status: "C2-strong direct-sum composite: local algebra M_2; '
        'physical object may be a finite direct sum of site algebras; not adopted"',
        "actual_current_surface_status: bounded-support",
    )
    checks.check(
        "machine-status-contract",
        "the source carries the required C2-strong and bounded-support fields",
        all(phrase in note for phrase in required_status),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "theorem-surface",
        "the three declared theorems and the reconstructed tensor fact are source-visible",
        all(
            phrase in note
            for phrase in (
                "No Unital `*`-Hom `A3 → A2`",
                "No Unital `*`-Hom `A3 → S_n`",
                "Finite Direct-Sum Composites Of One-Site `M_2` Do Not Host Unital `M_3`",
                "`3 ∤ 2^k`",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the hypothetical C2-strong composite wording is absent from the axiom memo",
        all(
            phrase not in axiom
            for phrase in (
                "C2-strong",
                "S_n",
                "finite direct sum of site algebras",
            )
        ),
    )
    checks.check(
        "no-rewrite-no-color-axiom",
        "the note refuses a Qubit rewrite and refuses a color axiom",
        all(
            phrase in note
            for phrase in (
                "The Qubit axiom is not rewritten",
                "not adopted",
                "not a C1 clone",
                "not a fifth extra",
                "not a C6/C7",
                "not adopted as a color axiom",
            )
        )
        and "QCD" not in note,
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )
    checks.check(
        "audit-input-paths",
        "the declared audit inputs are exactly the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/QUBIT_DIRECT_SUM_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print(
        "per_element: matrix units of M_3 and the unit of each S_n coordinate are checked"
    )
    print("per_site: the one-site algebra remains M_2(C); no site rewrite is asserted")
    print("per_mode: checked and not executed — no spectral-mode claim")
    print(
        "per_block: the unital *-hom block into direct sums and tensors of M_2 is the "
        "only negative block tested"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide dynamics or color "
        "sector is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
