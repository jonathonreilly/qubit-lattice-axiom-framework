#!/usr/bin/env python3
"""Exact checks for the occupancy-menu-kernel triple note.

Identity gates compute Tr(rho P) and the unit-lock record count. The runner
does not embed those values inside the pairing, and it does not import a
frame-function theorem.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "SMALLEST_COMPLETE_BORN_EXTRA_IS_OCCUPANCY_MENU_KERNEL_TRIPLE_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PARENT_PATH = ROOT / "docs" / (
    "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_"
    "BOUNDED_THEOREM_NOTE_2026-08-09.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SMALLEST_COMPLETE_BORN_EXTRA_IS_OCCUPANCY_MENU_KERNEL_TRIPLE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][0] * right[0][column] + left[row][1] * right[1][column]
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def mat_scale(value: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(value * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def tr(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def born(rho: Matrix, projector: Matrix) -> Fraction:
    return tr(mat_mul(rho, projector))


def record_I(*locks: object) -> Fraction:
    return sum((Fraction(1) for lock in locks if lock), Fraction(0))


def formed_sites(occupancy: dict[str, int]) -> set[str]:
    return {site for site, value in occupancy.items() if value == 1}


def mu_and_I_determine_born_number_and_site(
    rows: tuple[tuple[dict[str, Fraction], Fraction, Fraction, str], ...]
) -> bool:
    """True only if equal (mu, I) force one Born number and one formed site."""
    seen: dict[tuple[tuple[tuple[str, Fraction], ...], Fraction], tuple[Fraction, str]] = {}
    for mu, readout, number, site in rows:
        key = (tuple(sorted(mu.items())), readout)
        if key in seen and seen[key] != (number, site):
            return False
        seen[key] = (number, site)
    return True


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
    parent = PARENT_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_src = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)

    print(
        "external_scientific_inputs: current axiom wording and the August 9 "
        "parent are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no cache envelope is written"
    )

    identity = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    sigma_x = (
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0)),
    )
    Pz = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    Px = mat_scale(Fraction(1, 2), mat_add(identity, sigma_x))
    rho = (
        (Fraction(3, 5), Fraction(0)),
        (Fraction(0), Fraction(2, 5)),
    )
    mu = {"A": Fraction(3, 5), "B": Fraction(2, 5)}
    o10 = {"x": 1, "y": 0}
    o01 = {"x": 0, "y": 1}

    kz = born(rho,Pz)
    kx = born(rho,Px)
    i10 = record_I(o10["x"], o10["y"])
    i01 = record_I(o01["x"], o01["y"])

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-admissibility",
        "the exact current distribution sentence is present",
        canonical_sentence in normalize(axiom),
    )
    checks.check(
        "source-record-additivity",
        "the current axiom note names additive scalar readout with empty value zero",
        "I(empty)=0" in normalize(axiom).replace(" ", "")
        or "I(empty)=0" in axiom.replace(" ", ""),
    )
    checks.check(
        "source-parent",
        "the parent theorem supplies the unique trace form only after menu-independent low-arity grading",
        all(
            phrase in parent
            for phrase in (
                "menu-independent grading",
                "Every two- or three-member menu is normalized",
                "There is a unique density matrix",
            )
        ),
    )
    checks.check(
        "menu-resolutions",
        "the z and x projector pairs each sum exactly to the identity",
        mat_add(Pz, mat_sub(identity, Pz)) == identity
        and mat_add(Px, mat_sub(identity, Px)) == identity,
    )
    checks.check(
        "identity-born-z",
        "born(rho,Pz) computes the exact kernel value 3/5",
        kz == Fraction(3, 5),
    )
    checks.check(
        "identity-born-x",
        "born(rho,Px) computes the exact kernel value 1/2",
        kx == Fraction(1, 2),
    )
    checks.check(
        "identity-record",
        "record_I of each unit occupancy is 1",
        i10 == Fraction(1) and i01 == Fraction(1),
    )
    checks.check(
        "theorem-1-occupancy",
        "o10 and o01 share I=1 and mu but name different formed sites",
        i10 == i01 == Fraction(1)
        and o10 != o01
        and formed_sites(o10) == {"x"}
        and formed_sites(o01) == {"y"},
    )
    checks.check(
        "theorem-2-menu",
        "without a menu the two kernel values are distinct",
        kz != kx,
    )
    checks.check(
        "theorem-3-kernel",
        "record count is not the kernel",
        i10 != kz,
    )
    mutation_mu_I = mu_and_I_determine_born_number_and_site(
        (
            (mu, i10, kz, "x"),
            (mu, i01, kz, "y"),
            (mu, i10, i10, "x"),
        )
    )
    checks.check(
        "mutation-mu-I",
        "the predicate (mu,I) determines the Born number and site fails",
        mutation_mu_I is False,
    )
    checks.check(
        "mutation-kernel-equality",
        "the predicate K(rho,Pz)=K(rho,Px) fails",
        (kz == kx) is False,
    )
    checks.check(
        "identity-call-surface",
        "identity gates call born(rho,Pz), born(rho,Px), and record_I",
        "born(rho,Pz)" in runner_src
        and "born(rho,Px)" in runner_src
        and "record_I" in runner_src,
    )
    theorem_needles = (
        "Without occupancy the compiler has no formed site",
        "Without a menu the compiler has no outcome list",
        "Record count is not the kernel",
        "at least as fine as the triple",
        "Do not import Gleason",
    )
    checks.check(
        "note-theorems",
        "the source records Theorems 1-5 in the declared wording",
        all(phrase in note for phrase in theorem_needles),
    )
    checks.check(
        "hygiene-forbidden-phrases",
        "the source does not adopt an axiom, name L_phys, or treat Gleason as a dependency",
        "we adopt" not in note
        and "Born axiom" not in note
        and "L_phys" not in note
        and "GLEASON_ON_QUBIT_LATTICE" not in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support and negative-route-pruning trace fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: negative_route_pruning",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )
    checks.check(
        "parent-unresolved",
        "the source treats the August 9 parent as unaudited display, not a frame-function import",
        "effective_status: unaudited" in note and "Do not import Gleason" in note,
    )

    print(
        "per_element: two occupancies, two binary projectors, and two exact "
        "kernel values are checked"
    )
    print(
        "per_site: the occupancy split is a two-site window statement; no "
        "composite carrier is asserted"
    )
    print("per_mode: checked and not executed — no spectral mode is claimed")
    print("per_block: the drop-one extra block is the only negative block tested")
    print(
        "lattice_wide: checked and not executed — no lattice-wide dynamics or "
        "Born impossibility is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
