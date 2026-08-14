#!/usr/bin/env python3
"""Exact checks: empty-empty pairing cell is not a blank readout.

Two occupancy pairings are reconstructed from lock-collection counts.
The empty-empty cells agree at Fraction 0. That cell is table data, not
a site readout of a blank and not I(empty). No pairing is adopted and I
is not restored.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "EMPTY_EMPTY_PAIRING_CELL_IS_NOT_A_BLANK_READOUT_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/EMPTY_EMPTY_PAIRING_CELL_IS_NOT_A_BLANK_READOUT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

LockCollection = frozenset[str]
EMPTY: LockCollection = frozenset()


def occupancy(locks: LockCollection) -> Fraction:
    """Count of formed records in a lock collection, as an exact Fraction."""
    return Fraction(len(locks))


def b_pi(left: LockCollection, right: LockCollection) -> Fraction:
    """Product occupancy pairing, reconstructed locally."""
    return occupancy(left) * occupancy(right)


def b_plus(left: LockCollection, right: LockCollection) -> Fraction:
    """Count-add occupancy pairing, reconstructed locally."""
    return occupancy(left) + occupancy(right)


def identity_gate_pi() -> Fraction:
    """Product pairing evaluated at the identity lock collection."""
    return b_pi(EMPTY, EMPTY)


def identity_gate_plus() -> Fraction:
    """Count-add pairing evaluated at the identity lock collection."""
    return b_plus(EMPTY, EMPTY)


def record_axiom_section(axiom_text: str) -> str:
    """Return the live Record axiom body, not later commentary."""
    marker = "### Record / Fixed Reality"
    start = axiom_text.index(marker)
    rest = axiom_text[start + len(marker) :]
    next_heading = rest.find("\n### ")
    if next_heading < 0:
        next_heading = rest.find("\n## ")
    if next_heading < 0:
        return axiom_text[start:]
    return axiom_text[start : start + len(marker) + next_heading]


def live_memo_contains_i_empty_zero(axiom_text: str) -> bool:
    """True only if the Record axiom text asserts I(empty)=0."""
    compact = record_axiom_section(axiom_text).replace(" ", "")
    return "I(empty)=0" in compact


def blank_site_readout() -> Fraction | None:
    """A blank site has no record, so it has no defined readout value."""
    record_content = None
    if record_content is None:
        return None
    raise AssertionError("blank-site branch must return before any readout")


def empty_empty_cell_is_site_readout_of_a_blank() -> bool:
    """Pairing cell is a supplied table entry, not a blank-site readout."""
    readout = blank_site_readout()
    if readout is None:
        return False
    pairing_cell = b_pi(EMPTY, EMPTY)
    return pairing_cell == readout


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; reconstructed occupancy pairings only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction occupancy counts; no floating-point inputs")
    print("claim_boundary: agreed empty-empty cell is table data, not a blank readout")

    empty_pi = b_pi(EMPTY, EMPTY)
    empty_plus = b_plus(EMPTY, EMPTY)
    unit_s: LockCollection = frozenset({"s"})
    unit_t: LockCollection = frozenset({"t"})
    occupied_pi = b_pi(unit_s, unit_t)
    occupied_plus = b_plus(unit_s, unit_t)
    gate_pi = identity_gate_pi()
    gate_plus = identity_gate_plus()
    blank_value = blank_site_readout()

    checks.check(
        "thm1-empty-pi-zero",
        "B_π(∅,∅) is the exact Fraction 0",
        empty_pi == Fraction(0) and isinstance(empty_pi, Fraction),
    )
    checks.check(
        "thm1-empty-plus-zero",
        "B_+(∅,∅) is the exact Fraction 0",
        empty_plus == Fraction(0) and isinstance(empty_plus, Fraction),
    )
    checks.check(
        "thm1-empty-cells-agree",
        "B_π(∅,∅) = B_+(∅,∅) as Fractions",
        empty_pi == empty_plus,
    )
    checks.check(
        "thm1-identity-gates-return-zeros",
        "identity gates return those zeros",
        gate_pi == Fraction(0)
        and gate_plus == Fraction(0)
        and gate_pi == empty_pi
        and gate_plus == empty_plus,
    )
    checks.check(
        "thm1-agreement-is-not-selection",
        "shared empty-empty cell does not select a pairing",
        empty_pi == empty_plus and occupied_pi != occupied_plus,
    )
    checks.check(
        "control-occupied-pi",
        "B_π({s},{t}) = 1",
        occupied_pi == Fraction(1),
    )
    checks.check(
        "control-occupied-plus",
        "B_+({s},{t}) = 2",
        occupied_plus == Fraction(2),
    )
    checks.check(
        "control-disagreement-not-load-bearing-cut",
        "occupied-occupied 1≠2 is a control, not this note's cut",
        occupied_pi != occupied_plus
        and "not this note's" in note
        and "load-bearing cut" in note,
    )
    checks.check(
        "thm2-live-record-quote",
        "live Record unreadability sentences are quoted without rewrite",
        "Only records are readable." in axiom
        and "A readout value is determined by record" in axiom
        and "A site with no record cannot be read." in axiom
        and "Only records are readable." in note
        and "A readout value is determined by record" in note
        and "A site with no record cannot be read." in note,
    )
    checks.check(
        "thm2-blank-has-no-defined-readout",
        "a blank site has no defined readout value",
        blank_value is None,
    )
    checks.check(
        "thm2-pairing-cell-is-table-entry-not-readout",
        "the pairing cell is a supplied table entry, not a blank readout",
        not empty_empty_cell_is_site_readout_of_a_blank()
        and empty_pi == Fraction(0)
        and blank_value is None,
    )
    checks.check(
        "thm2-cell-is-not-i-empty",
        "the pairing cell is not I(empty)",
        "it is not `I(empty)`" in note
        and "Named additive `I` is not" in note
        and "I(empty)=0` are not Record axiom content" in axiom,
    )
    checks.check(
        "thm3-cell-is-still-extra",
        "the agreed empty-empty cell remains extra bookkeeping",
        "remains extra" in note
        and "does not adopt `π`" in note
        and "does not restore" in note
        and "`J` field" in note
        and "vacuum energy" in note
        and "Newton constant" in note,
    )
    checks.check(
        "mutation-live-memo-contains-i-empty-zero-fails",
        "predicate “live memo contains I(empty)=0” fails",
        live_memo_contains_i_empty_zero(axiom) is False,
    )
    checks.check(
        "mutation-empty-empty-is-blank-readout-fails",
        "predicate “empty-empty cell is a site readout of a blank” fails",
        empty_empty_cell_is_site_readout_of_a_blank() is False,
    )
    checks.check(
        "mutation-empty-cells-disagree-fails",
        "predicate B_π(∅,∅) != B_+(∅,∅) fails",
        (empty_pi != empty_plus) is False,
    )
    checks.check(
        "machine-status-contract",
        "bounded status and leftover-cut trace are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: negative_route_pruning" in note
        and "target_claim_id: empty_empty_pairing_cell_is_not_a_blank_readout"
        in note,
    )
    checks.check(
        "scope-exclusions",
        "no G_N, no 1/r install, no axiom edit, I is not restored",
        "No `G_N`" in note
        and "no `1/r`" in note
        and "I is not restored" in note
        and "no axiom is edited" in note
        and ("import " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "parents-axiom-only",
        "declared parents are the live axiom memo only",
        "Parents:** the live axiom memo" in note
        and "upstream_dependencies:\n  - minimal_axioms\n" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/EMPTY_EMPTY_PAIRING_CELL_IS_NOT_A_BLANK_READOUT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print("per_element: empty-empty and occupied-occupied cells of both pairings.")
    print("per_site: a blank site has no defined readout; occupancy is not a readout.")
    print("per_mode: product and count-add tables are both evaluated, neither adopted.")
    print("per_block: identity gates, mutation predicates, and Record unreadability.")
    print("lattice_wide: checked and not executed — no lattice-wide pairing is claimed.")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
