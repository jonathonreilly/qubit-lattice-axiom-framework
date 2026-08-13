#!/usr/bin/env python3
"""Exact checks: a declared two-site L-table is extra, not forced.

Displayed tables L0 and L1 jointly list (μ, o, K) on W={x,y}. They are
well-defined and disagree at μ and K. Current Admissibility does not name
either table. No table is adopted.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "DECLARED_TWO_SITE_L_TABLE_IS_EXTRA_NOT_FORCED_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/DECLARED_TWO_SITE_L_TABLE_IS_EXTRA_NOT_FORCED_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

WINDOW = ("x", "y")
MENU = ("A", "B")
P_Z = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))


def normalize(text: str) -> str:
    return " ".join(text.split())


def mat_mul(left: tuple, right: tuple) -> tuple:
    return tuple(
        tuple(
            left[row][0] * right[0][col] + left[row][1] * right[1][col]
            for col in range(2)
        )
        for row in range(2)
    )


def mat_adj(matrix: tuple) -> tuple:
    return tuple(tuple(matrix[col][row] for col in range(2)) for row in range(2))


def mat_trace(matrix: tuple) -> Fraction:
    return matrix[0][0] + matrix[1][1]


@dataclass(frozen=True)
class LTable:
    name: str
    occupancy: tuple[int, int]
    mu_x_A: Fraction
    mu_x_B: Fraction
    k_pz: Fraction

    def well_defined(self) -> bool:
        o_ok = self.occupancy == (1, 0) and set(self.occupancy) <= {0, 1}
        mu_ok = (
            self.mu_x_A >= 0
            and self.mu_x_B >= 0
            and self.mu_x_A + self.mu_x_B == 1
        )
        k_ok = Fraction(0) <= self.k_pz <= Fraction(1)
        return o_ok and mu_ok and k_ok


L0 = LTable(
    name="L0",
    occupancy=(1, 0),
    mu_x_A=Fraction(1, 3),
    mu_x_B=Fraction(2, 3),
    k_pz=Fraction(1, 3),
)
L1 = LTable(
    name="L1",
    occupancy=(1, 0),
    mu_x_A=Fraction(3, 5),
    mu_x_B=Fraction(2, 5),
    k_pz=Fraction(3, 5),
)


def L0_muA() -> Fraction:
    return L0.mu_x_A


def L1_muA() -> Fraction:
    return L1.mu_x_A


def predicate_L0_equals_L1() -> bool:
    return (
        L0.occupancy == L1.occupancy
        and L0_muA() == L1_muA()
        and L0.mu_x_B == L1.mu_x_B
        and L0.k_pz == L1.k_pz
    )


def predicate_axiom_memo_names_L0(axiom: str) -> bool:
    return "L0" in axiom


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

    print("external_scientific_inputs: current axiom wording is source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: displayed L0 and L1 are not adopted; L_phys, r=1/2, and Born derivation are refused")

    checks.check(
        "table-L0-well-defined",
        "L0 is a finite occupancy-probability-grade table on W={x,y}",
        L0.well_defined() and WINDOW == ("x", "y") and MENU == ("A", "B"),
    )
    checks.check(
        "table-L1-well-defined",
        "L1 is a finite occupancy-probability-grade table on the same window",
        L1.well_defined() and L1.occupancy == L0.occupancy,
    )
    checks.check(
        "projector-Pz",
        "P_z is the declared rank-one projector diag(1,0)",
        P_Z == ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
        and mat_mul(P_Z, P_Z) == P_Z
        and mat_adj(P_Z) == P_Z
        and mat_trace(P_Z) == 1,
    )
    checks.check(
        "identity-L0-muA",
        "identity gate L0_muA() returns the declared L0 menu mass at A",
        L0_muA() == L0.mu_x_A and L0.k_pz == L0_muA(),
    )
    checks.check(
        "identity-L1-muA",
        "identity gate L1_muA() returns the declared L1 menu mass at A",
        L1_muA() == L1.mu_x_A and L1.k_pz == L1_muA(),
    )
    checks.check(
        "tables-disagree",
        "L0 and L1 disagree at μ and K (1/3 ≠ 3/5)",
        L0_muA() != L1_muA() and L0.k_pz != L1.k_pz,
    )
    checks.check(
        "mutation-L0-equals-L1",
        "predicate L0=L1 fails",
        predicate_L0_equals_L1() is False,
    )
    checks.check(
        "source-admissibility-one-rule",
        "Admissibility names one fixed nearest-neighbor rule",
        "There is one fixed nearest-neighbor admissibility rule" in axiom,
    )
    checks.check(
        "source-form-values-unspecified",
        "the memo leaves the distribution form and values unspecified",
        "the distribution's extensional form and values are not specified by this memo"
        in normalized_axiom
        and "the remaining formation rules (the distribution's form and"
        in normalized_axiom,
    )
    checks.check(
        "axiom-does-not-name-L0",
        "predicate axiom memo names L0 fails",
        predicate_axiom_memo_names_L0(axiom) is False and "L1" not in axiom,
    )
    checks.check(
        "granting-L-does-not-select",
        "the note records that granting there is an L does not select the table",
        "Granting “there is an `L`” does not select the table." in normalized_note
        or 'Granting "there is an `L`" does not select the table.' in normalized_note,
    )
    checks.check(
        "c3-not-cheaper-without-selection",
        "C3 without a selected table is not cheaper than H_extra",
        "Candidate C3 without a selected table is not cheaper than `H_extra`."
        in normalized_note,
    )
    checks.check(
        "machine-status-contract",
        "the source carries the required hypothetical and bounded-support fields",
        'hypothetical_axiom_status: "C3 counterfactual: Admissibility references one declared executable L-table; table not adopted"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "theorem-four-non-adoption",
        "the note adopts neither table nor L_phys, does not force r=1/2, and does not claim Born is derived",
        all(
            phrase in normalized_note
            for phrase in (
                "This note does not adopt `L0` or `L1`.",
                "It does not adopt `L_phys`.",
                "It does not force `r=1/2`.",
                "It does not claim Born is derived.",
            )
        )
        and "0.5934" not in note
        and "github.com" not in note,
    )
    checks.check(
        "parents-axiom-memo-only",
        "AUDIT_INPUT_PATHS are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/DECLARED_TWO_SITE_L_TABLE_IS_EXTRA_NOT_FORCED_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
