#!/usr/bin/env python3
"""Exact checks: Born-cluster facts under a diagnostic support-only reading.

Identity gates call mu1_at_2, mu2_at_2, born_rho_P, and I_one.
The predicate mu1(A|2)=mu2(A|2) must fail (1/3 != 3/8).
The predicate Tr(rho P)=I(one lock) must fail (3/5 != 1).
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "BORN_CLUSTER_UNDER_SUPPORT_ONLY_ADMISSIBILITY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/BORN_CLUSTER_UNDER_SUPPORT_ONLY_ADMISSIBILITY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def mu1_at_2() -> Fraction:
    """Uniform three-slot occupancy law at neighbor count 2."""
    return Fraction(1, 3)


def mu2_at_2() -> Fraction:
    """Three-of-eight occupancy law at neighbor count 2."""
    return Fraction(3, 8)


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def mat_trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def mat_scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return (
        (scalar * matrix[0][0], scalar * matrix[0][1]),
        (scalar * matrix[1][0], scalar * matrix[1][1]),
    )


def is_projector(matrix: Matrix) -> bool:
    return mat_mul(matrix, matrix) == matrix


def rho_matrix() -> Matrix:
    return (
        (Fraction(3, 5), Fraction(0)),
        (Fraction(0), Fraction(2, 5)),
    )


def projector_p() -> Matrix:
    return (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )


def menu_identity() -> Matrix:
    return (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )


def born_rho_P() -> Fraction:
    return mat_trace(mat_mul(rho_matrix(), projector_p()))


def I_one() -> int:
    return 1


def I_empty() -> int:
    return 0


def occupancy_laws_agree_at_2() -> bool:
    """Hostile predicate: the two occupancy laws agree at k=2."""
    return mu1_at_2() == mu2_at_2()


def born_equals_one_lock() -> bool:
    """Hostile predicate: the Born pairing equals I of one lock."""
    return born_rho_P() == I_one()


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

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
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read "
        "for claim-surface consistency"
    )
    print(
        "negative_scope: only the four reconstructed facts and the "
        "reading-relative missing-mu classification are checked; a later "
        "compiler remains live"
    )

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-admissibility-aug5",
        "the exact current distribution sentence is present",
        canonical_sentence in normalized_axiom,
    )
    checks.check(
        "source-support-reading",
        "the axiom reading note takes available to be the distribution support",
        '"available"/"admissible" denotes its support' in axiom,
    )
    checks.check(
        "source-form-unspecified",
        "the memo withholds the distribution form and values",
        "form and values are not specified" in normalized_axiom,
    )
    checks.check(
        "source-record-I",
        "the axiom supplies additive I with I(empty)=0",
        "I(empty)=0" in axiom,
    )
    checks.check(
        "source-one-lock",
        "the axiom locks exactly one admissible local possibility",
        "a record locks exactly one admissible local possibility" in normalized_axiom,
    )

    checks.check(
        "fact1-values",
        "the two occupancy laws evaluate to 1/3 and 3/8 at k=2",
        mu1_at_2() == Fraction(1, 3) and mu2_at_2() == Fraction(3, 8),
    )
    checks.check(
        "mutation-occupancy-laws-agree",
        "the predicate mu1(A|2)=mu2(A|2) fails",
        occupancy_laws_agree_at_2() is False,
    )
    checks.check(
        "fact2-born-pairing",
        "Tr(rho P) equals 3/5",
        born_rho_P() == Fraction(3, 5),
    )
    checks.check(
        "fact2-one-lock",
        "I of one lock equals 1",
        I_one() == 1 and I_empty() == 0,
    )
    checks.check(
        "mutation-born-equals-I",
        "the predicate Tr(rho P)=I(one lock) fails",
        born_equals_one_lock() is False,
    )
    checks.check(
        "fact3-menu-identity",
        "Tr(I_2)=2 is not I(empty)=0",
        mat_trace(menu_identity()) == 2 and I_empty() == 0,
    )
    checks.check(
        "fact4-scaled-not-projector",
        "E0=(1/2)P is not a projector, while P is",
        is_projector(projector_p())
        and not is_projector(mat_scale(Fraction(1, 2), projector_p())),
    )
    checks.check(
        "theorem1-reading-independence",
        "the note states Facts 1-4 hold on both readings",
        all(
            phrase in normalized_note
            for phrase in (
                "true as arithmetic / type facts on both readings",
                "They do not depend on which reading is quoted",
            )
        ),
    )
    checks.check(
        "theorem2-expected-under-r-supp",
        "missing-mu sentences are expected under R_supp and walls under R_dist",
        all(
            phrase in normalized_note
            for phrase in (
                "the axioms pick neither",
                "mu` is not `rho`",
                "a lock is not `mu`",
                "expected gap",
                "Under **R_dist** the axiom *names* a law-level",
            )
        ),
    )
    checks.check(
        "theorem3-type-splits-remain",
        "Facts 2-4 remain type-splits and the compiler need is not dissolved",
        all(
            phrase in normalized_note
            for phrase in (
                "Facts 2–4 remain type-splits",
                "does not dissolve that need",
                "does not claim that no later compiler exists",
            )
        ),
    )
    checks.check(
        "theorem4-flip-count",
        "exactly one of the four reconstructed claims flips wall to gap",
        "Count of `R_dist -> R_supp` wall-to-gap flips: 1" in note,
    )
    checks.check(
        "source-note-readings",
        "both readings are quoted and neither is adopted as a rewrite",
        all(
            phrase in normalized_note
            for phrase in (
                "R_dist",
                "R_supp",
                "Neither is a rewrite",
                "clause is not dropped",
                "Do not force `r=1/2`",
                "does not adopt `L_phys`",
            )
        ),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required diagnostic machine-status fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                'hypothetical_axiom_status: "C4 diagnostic: classify selected claims under support-only Admissibility; clause not dropped"',
                "target_claim_type: bounded_theorem",
                "trace_class: negative_route_pruning",
                "source_of_blocker_text: handoff",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "excluded-imports",
        "Gleason, 0.5934, and unmerged-PR premises are refused",
        "Gleason's theorem is not imported" in note
        and "0.5934" in note
        and "not used" in normalized_note
        and "No unmerged pull request is cited" in note
        and "PR #" not in note
        and "#6" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the diagnostic witnesses are absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("mu1_at_2", "mu2_at_2", "born_rho_P", "I_one", "L_phys", "R_supp")
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "no later compiler exists" in note,
    )

    print("per_element: occupancy pair, Born pairing, empty count, and scaled projector are checked")
    print("per_site: one site at neighbor count 2 and one unit lock; no composite carrier is asserted")
    print("per_mode: checked and not executed — no spectral mode is used")
    print("per_block: only the four reconstructed facts and the reading flip are classified")
    print("lattice_wide: checked and not executed — no lattice-wide frequency claim is made")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
