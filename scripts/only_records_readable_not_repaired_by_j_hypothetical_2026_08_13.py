#!/usr/bin/env python3
"""Honesty checks: C1 J does not repair 'Only records are readable'.

Reconstructs the two-site C1 field, evaluates I and J on the empty and unit
configurations, and confirms that the empty history remains a defined readout.
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import Any


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ONLY_RECORDS_READABLE_NOT_REPAIRED_BY_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ONLY_RECORDS_READABLE_NOT_REPAIRED_BY_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BLANK = 0
A = "A"
B = "B"
WINDOW = ("x", "y")
MENU = frozenset({A, B})
CODOMAIN = frozenset({BLANK}) | MENU

UNDEFINED = object()


@dataclass(frozen=True)
class Config:
    name: str
    field: tuple[Any, ...]


def J_of(config: Config) -> tuple[Any, ...]:
    if len(config.field) != len(WINDOW):
        raise ValueError("J must be indexed by the declared window")
    if any(value not in CODOMAIN for value in config.field):
        raise ValueError("J must land in {0} union M")
    return config.field


def o_from_J(config: Config) -> tuple[int, ...]:
    return tuple(0 if value == BLANK else 1 for value in J_of(config))


def I_of(config: Config) -> int:
    return sum(o_from_J(config))


def has_lock(config: Config) -> bool:
    return I_of(config) != 0


def is_undefined(value: object) -> bool:
    return value is UNDEFINED


def r_strict_readout(config: Config) -> object:
    if not has_lock(config):
        return UNDEFINED
    return I_of(config)


def identity_gates(e: Config, u: Config) -> dict[str, object]:
    return {
        "I_of(e)": I_of(e),
        "J_of(e)": J_of(e),
        "o_from_J(e)": o_from_J(e),
        "I_of(u)": I_of(u),
        "J_of(u)": J_of(u),
    }


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

    print("external_scientific_inputs: current Record wording is source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: C1 is displayed only; no Record rewrite, pairing on J, L_phys, or r=1/2 is adopted")

    e = Config("e", (BLANK, BLANK))
    u = Config("u", (A, BLANK))
    gates = identity_gates(e, u)
    gate_source = inspect.getsource(identity_gates)

    checks.check(
        "identity-gate-calls",
        "identity gates call I_of(e), J_of(e), o_from_J(e), I_of(u), and J_of(u)",
        all(
            needle in gate_source
            for needle in ("I_of(e)", "J_of(e)", "o_from_J(e)", "I_of(u)", "J_of(u)")
        ),
    )
    checks.check(
        "empty-I-defined",
        "predicate I(e) is undefined fails because I_of(e) equals 0",
        not is_undefined(gates["I_of(e)"]) and gates["I_of(e)"] == 0,
    )
    checks.check(
        "empty-J-defined",
        "predicate J(e) is undefined fails because J_of(e) equals (0, 0)",
        not is_undefined(gates["J_of(e)"]) and gates["J_of(e)"] == (0, 0),
    )
    checks.check(
        "empty-has-no-lock",
        "predicate e has a lock fails because o_from_J(e) equals (0, 0)",
        not has_lock(e) and gates["o_from_J(e)"] == (0, 0),
    )
    checks.check(
        "unit-I-convention",
        "I_of(u) equals the unit-count convention 1",
        gates["I_of(u)"] == 1,
    )
    checks.check(
        "unit-J-field",
        "J_of(u) is the one-lock field (A, 0)",
        gates["J_of(u)"] == (A, 0),
    )
    checks.check(
        "strict-readout-contrast",
        "R_strict leaves e without a readout while current I still reads 0",
        is_undefined(r_strict_readout(e))
        and r_strict_readout(u) == 1
        and I_of(e) == 0,
    )
    checks.check(
        "c1-type",
        "both displayed fields are values of J:W to {0} union M and 0 is not a menu label",
        BLANK not in MENU
        and set(J_of(e)) <= CODOMAIN
        and set(J_of(u)) <= CODOMAIN,
    )
    checks.check(
        "source-record-clause",
        "the axiom memo still carries the leftover clause and the empty identity",
        "Only records are readable." in axiom
        and "I(empty)=0" in axiom.replace(" ", ""),
    )
    checks.check(
        "note-leftover-display",
        "the note displays the leftover clause and the including-empty owner reading",
        "Only records are readable" in note
        and "only record-configurations (including empty) have a readout" in note
        and "not c1zero" in note
        and "not c1addI" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required C1 follow-on hypothetical status and bounded-support surface",
        'hypothetical_axiom_status: "C1 follow-on: only-records-readable is not repaired by J; empty still has a readout; not adopted"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "no-adoption",
        "the note refuses a Record rewrite, pairing on J, L_phys, and r=1/2",
        "Does not adopt C1" in note
        and "Do not put a pairing on `J`" in note
        and "Do not adopt `L_phys`" in note
        and "Do not force `r = 1/2`" in note
        and "cheapest change" not in note,
    )
    checks.check(
        "unit-count-is-convention",
        "the note does not claim Record additivity forces I(u)=1",
        "does not by itself force the unit to be `1`" in note
        and "Does not claim Record additivity forces the unit-count" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the canonical axiom file is not rewritten with C1 field notation",
        all(phrase not in axiom for phrase in ("J_of", "o_from_J", "R_strict", "C1 follow-on")),
    )

    print("per_element: empty and unit C1 fields are the only configurations evaluated")
    print("per_site: occupancy is the sitewise blank-versus-lock bit; no lattice-wide dynamics is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
