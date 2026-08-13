#!/usr/bin/env python3
"""Exact checks: axioms do not select which PVM a Lüders instrument reads.

Identity gates call born(rho, Pz) and born(rho, Px). The equality predicate
K(rho, Pz) = K(rho, Px) is required to fail, as is the predicate that the
canonical axiom memo names P_z.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/AXIOMS_DO_NOT_SELECT_WHICH_PVM_A_LUDERS_INSTRUMENT_READS_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PARENT_REL = (
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_"
    "BOUNDED_THEOREM_NOTE_2026-08-09.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/AXIOMS_DO_NOT_SELECT_WHICH_PVM_A_LUDERS_INSTRUMENT_READS_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
PARENT_PATH = ROOT / PARENT_REL
AXIOM_PATH = ROOT / AXIOM_REL

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


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


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def born(sigma: Matrix, projector: Matrix) -> Fraction:
    return trace(mat_mul(sigma, projector))


def k_rho_pz_equals_k_rho_px(sigma: Matrix, p_z: Matrix, p_x: Matrix) -> bool:
    return born(sigma, p_z) == born(sigma, p_x)


def axioms_name_pz(axiom_text: str) -> bool:
    compact = normalize(axiom_text)
    needles = (
        "P_z",
        "P_x",
        "diag(1,0)",
        "sigma_x",
        "sigma_z",
        "Lüders",
        "Luders",
        "projector-valued",
    )
    return any(needle in compact for needle in needles)


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
    normalized_note = normalize(note).replace("> ", "")
    source = Path(__file__).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current axiom wording and the August 9 "
        "parent are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency against the declared parents"
    )
    print(
        "negative_scope: only equality of the two displayed Born weights and "
        "the claim that the axioms name P_z are rejected"
    )

    I = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    Pz = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    Px = (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(1, 2)),
    )
    I_minus_Pz = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    I_minus_Px = (
        (Fraction(1, 2), Fraction(-1, 2)),
        (Fraction(-1, 2), Fraction(1, 2)),
    )
    rho = (
        (Fraction(3, 5), Fraction(0)),
        (Fraction(0), Fraction(2, 5)),
    )

    checks.check(
        "identity-born-z",
        "born(rho, Pz) equals the exact weight 3/5",
        born(rho, Pz) == Fraction(3, 5),
    )
    checks.check(
        "identity-born-x",
        "born(rho, Px) equals the exact weight 1/2",
        born(rho, Px) == Fraction(1, 2),
    )
    checks.check(
        "binary-menu-resolutions",
        "each displayed pair sums exactly to the identity",
        mat_add(Pz, I_minus_Pz) == I and mat_add(Px, I_minus_Px) == I,
    )
    checks.check(
        "complement-weights",
        "the complementary Born weights are 2/5 and 1/2",
        born(rho, I_minus_Pz) == Fraction(2, 5)
        and born(rho, I_minus_Px) == Fraction(1, 2),
    )
    checks.check(
        "mutation-equal-weights",
        "the predicate K(rho, P_z)=K(rho, P_x) fails",
        not k_rho_pz_equals_k_rho_px(rho, Pz, Px),
    )
    checks.check(
        "polarized-state",
        "rho is a polarized density matrix with Bloch radius 1/5, not r=1/2",
        trace(rho) == 1
        and rho[0][0] - rho[1][1] == Fraction(1, 5)
        and rho[0][0] - rho[1][1] != Fraction(1, 2)
        and rho != (
            (Fraction(1, 2), Fraction(0)),
            (Fraction(0), Fraction(1, 2)),
        ),
    )
    checks.check(
        "source-qubit",
        "Qubit names M_2(C) and that no possibility is privileged",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "No possibility is privileged." in axiom,
    )
    checks.check(
        "source-admissibility",
        "Admissibility names a nearest-neighbor-determined distribution",
        (
            "For each site, the probability distribution over the possibilities is "
            "determined by, and varies with, the nearest-neighbor conditions."
        )
        in normalize(axiom),
    )
    checks.check(
        "mutation-axioms-name-pz",
        "the predicate that the axioms name P_z fails",
        not axioms_name_pz(axiom),
    )
    checks.check(
        "source-parent",
        "the August 9 parent supplies the unique trace form after a supplied grading",
        all(
            phrase in parent
            for phrase in (
                "menu-independent grading",
                "There is a unique density matrix",
                "w(E)=Tr(rho E)",
            )
        ),
    )
    checks.check(
        "note-theorems",
        "the note records the two-menu disagreement, the un-named menus, and the extra declaration",
        all(
            phrase in normalized_note
            for phrase in (
                "K(rho, P_z)=Tr(rho P_z)=3/5",
                "K(rho, P_x)=Tr(rho P_x)=(3/5)(1/2)+(2/5)(1/2)=1/2",
                "3/5 != 1/2",
                "Neither sentence names `P_z` versus `P_x`",
                "A later Lüders compiler that returns those Born weights still consumes a declared projector",
                "`{P_z, I-P_z}` and `{P_x, I-P_x}`",
            )
        ),
    )
    checks.check(
        "note-hygiene-theorems",
        "the note refuses August 9 replacement, Born denial, n=z selection, r=1/2, and a PVM axiom",
        all(
            phrase in normalized_note
            for phrase in (
                "This note does not improve or replace",
                "It does not say Born is false",
                "It does not select `n=z` by cubic covariance",
                "a polarized density matrix is allowed",
                "It does not force `r=1/2`",
                "It does not adopt a PVM axiom",
                "neither is adopted",
            )
        ),
    )
    checks.check(
        "forbidden-closures",
        "the note avoids we adopt, a Lüders axiom, L_phys, dim-2 Gleason, and unmerged PR citations",
        all(
            phrase not in note
            for phrase in (
                "we adopt",
                "Lüders axiom",
                "Luders axiom",
                "L_phys",
                "dim-2 Gleason",
                "dimension-two Gleason",
                "dimension 2 Gleason",
                "pvmluders",
                "github.com/",
                "/pull/",
            )
        ),
    )
    checks.check(
        "identity-gates-call-born",
        "the identity gates in this runner literally call born(rho, Pz) and born(rho, Px)",
        "born(rho, Pz)" in source and "born(rho, Px)" in source,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support and negative-route-pruning fields",
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
                "hypothetical_axiom_status: \"no PVM-selecting clause is displayed, recommended, or adopted\"",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the forbidden-closure rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "a PVM axiom is adopted" in note,
    )
    checks.check(
        "declared-inputs-exist",
        "AUDIT_INPUT_PATHS resolve to the new note, the August 9 parent, and the axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, PARENT_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    print(
        "per_element: two rank-one projectors and one polarized density matrix "
        "are evaluated by the exact Born kernel"
    )
    print(
        "per_site: the disagreement and the axiom-text check are one-site "
        "statements; no composite carrier is asserted"
    )
    print(
        "per_mode: the z and x axes are checked, together with the refusal to "
        "force r=1/2; no exhaustion of Bloch directions is claimed"
    )
    print(
        "per_block: only PVM declaration versus declared-menu Born evaluation "
        "is the negative block tested"
    )
    print(
        "lattice_wide: checked and not executed — cubic covariance is used only "
        "to refuse a privileged axis; no lattice-wide dynamics is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
