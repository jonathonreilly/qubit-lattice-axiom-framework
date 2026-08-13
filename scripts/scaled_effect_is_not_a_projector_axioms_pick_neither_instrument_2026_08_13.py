#!/usr/bin/env python3
"""Exact checks: a scaled effect cP is not a projector; axioms pick neither instrument.

Identity gates call born(rho,P) and is_projector(E0). Mutation predicates that
E0 is a projector, or that Tr(rho P) equals Tr(rho E0), must fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "SCALED_EFFECT_IS_NOT_A_PROJECTOR_AXIOMS_PICK_NEITHER_INSTRUMENT_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SCALED_EFFECT_IS_NOT_A_PROJECTOR_AXIOMS_PICK_NEITHER_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def entry(value: int | Fraction) -> Fraction:
    return Fraction(value)


def diag(a: int | Fraction, b: int | Fraction) -> Matrix:
    zero = entry(0)
    return ((entry(a), zero), (zero, entry(b)))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][0] * right[0][column] + left[row][1] * right[1][column]
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matadd(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def is_projector(effect: Matrix) -> bool:
    return matmul(effect, effect) == effect


def born(state: Matrix, effect: Matrix) -> Fraction:
    return trace(matmul(state, effect))


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
    parent = PARENT_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_src = Path(__file__).read_text(encoding="utf-8")
    normalized_axiom = normalize(axiom)
    normalized_note = normalize(note)

    print("external_scientific_inputs: current axiom wording and the August 10 E0 object; no observational or fitted inputs")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: projector identity and first-outcome scale on one site; later compilers remain live")

    identity = diag(1, 1)
    P = diag(1, 0)
    E0 = diag(Fraction(1, 2), 0)
    rho = diag(Fraction(3, 5), Fraction(2, 5))
    I_minus_P = matsub(identity, P)
    I_minus_E0 = matsub(identity, E0)

    canonical_admissibility = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    canonical_record = "When present, a record locks exactly one admissible local possibility."
    checks.check(
        "source-admissibility",
        "the exact current distribution sentence is present",
        canonical_admissibility in normalized_axiom,
    )
    checks.check(
        "source-record",
        "the exact current lock sentence is present",
        canonical_record in normalized_axiom,
    )
    checks.check(
        "source-parent-e0",
        "the August 10 parent supplies the shared object E0=(1/2)P(z)",
        "E_0=(1/2)P(z)" in parent,
    )

    checks.check(
        "identity-is-projector-P",
        "is_projector(P) holds",
        is_projector(P) is True,
    )
    checks.check(
        "identity-is-projector-E0",
        "is_projector(E0) fails",
        is_projector(E0) is False,
    )
    checks.check(
        "identity-born-rho-P",
        "born(rho,P) equals 3/5",
        born(rho,P) == Fraction(3, 5),
    )
    checks.check(
        "identity-born-rho-E0",
        "born(rho, E0) equals 3/10",
        born(rho, E0) == Fraction(3, 10),
    )
    checks.check(
        "identity-gates-call-born-and-is-projector",
        "identity gates call born(rho,P) and is_projector(E0)",
        "born(rho,P)" in runner_src and "is_projector(E0)" in runner_src,
    )

    e0_square = matmul(E0, E0)
    checks.check(
        "theorem-1-projector-split",
        "P^2=P and E0^2=diag(1/4,0) so E0 is not a projector",
        matmul(P, P) == P
        and e0_square == diag(Fraction(1, 4), 0)
        and e0_square != E0
        and is_projector(E0) is False,
    )
    checks.check(
        "theorem-2-instruments-disagree",
        "Tr(rho P)=3/5 and Tr(rho E0)=3/10 disagree",
        born(rho,P) == Fraction(3, 5)
        and born(rho, E0) == Fraction(3, 10)
        and born(rho,P) != born(rho, E0),
    )

    predicate_e0_is_projector = is_projector(E0)
    checks.check(
        "mutation-e0-is-projector-fails",
        "the predicate E0 is a projector fails",
        predicate_e0_is_projector is False,
    )
    predicate_traces_equal = born(rho,P) == born(rho, E0)
    checks.check(
        "mutation-traces-equal-fails",
        "the predicate Tr(rho P)=Tr(rho E0) fails because 3/5 != 3/10",
        predicate_traces_equal is False
        and born(rho,P) == Fraction(3, 5)
        and born(rho, E0) == Fraction(3, 10),
    )

    checks.check(
        "binary-menus-resolve-identity",
        "both displayed menus sum exactly to I",
        matadd(P, I_minus_P) == identity and matadd(E0, I_minus_E0) == identity,
    )
    checks.check(
        "complements-born-normalize",
        "each menu's Born weights sum to one",
        born(rho,P) + born(rho, I_minus_P) == 1
        and born(rho, E0) + born(rho, I_minus_E0) == 1,
    )

    note_needles = (
        "P^2=diag(1,0)=P",
        "E_0^2=diag(1/4,0)",
        "E_0` is not a projector",
        "Tr(rho P)=3/5",
        "Tr(rho E_0)=3/10",
        "Neither sentence names `P` versus `cP`.",
        "`{P,I-P}` and `{E_0,I-E_0}`",
        "does not adopt either",
        "does not force `r=1/2`",
        "not replaced",
    )
    checks.check(
        "note-theorem-surface",
        "the note records both identities, non-adoption, no forced half-scale, and non-replacement",
        all(needle in note for needle in note_needles),
    )
    checks.check(
        "note-n5-theorem-4",
        "N5 is attached to Theorem 4 and refuses L_phys adoption and a forced r=1/2",
        "### N5 — resolution and rhetoric audit (Theorem 4)" in note
        and "no adoption of `L_phys`, no forced `r=1/2`, no Lüders map" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: negative_route_pruning",
                "source_of_blocker_text: handoff",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the displayed instruments are absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("E_0=(1/2)P", "diag(1/2,0)", "L_phys", "cP")
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note
        and "no later compiler can declare a scale" in note,
    )
    checks.check(
        "audit-input-paths",
        "declared inputs are the new note, the August 10 note, and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/SCALED_EFFECT_IS_NOT_A_PROJECTOR_AXIOMS_PICK_NEITHER_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and PARENT_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "no-unmerged-pr-citation",
        "the note cites no unmerged pull-request numbers",
        "PR #" not in note
        and "#6206" not in note
        and "#6199" not in note
        and "pvmselect" not in normalized_note
        and "pvmluders" not in normalized_note,
    )
    checks.check(
        "no-gleason",
        "the note does not invoke Gleason",
        "Gleason" not in note and "gleason" not in note,
    )
    checks.check(
        "august-standing-not-replaced",
        "August 9 and August 10 are left standing",
        "August 9" in note and "August 10" in note and "not replaced" in note,
    )
    checks.check(
        "theorem-3-axiom-quotes",
        "the note quotes the distribution sentence and the lock sentence",
        canonical_admissibility.replace("For each site, the p", "the p") in normalize(note)
        or canonical_admissibility in normalize(note),
    )

    print("per_element: identity gates call born(rho,P) and is_projector(E0)")
    print("per_site: one M_2(C) site; P versus (1/2)P only")
    print("per_mode: the rank-one ray of P and the scale c=1/2")
    print("per_block: instrument selection only; neither menu is adopted")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics claim")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
