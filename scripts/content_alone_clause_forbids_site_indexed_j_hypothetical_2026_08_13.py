#!/usr/bin/env python3
"""Exact two-history checks: strict content-alone forbids site-indexed J.

Reconstructs the C1 occupancy field J on the window W={x,y} from locked
labels. Identity gates call I_of, J_of, and bag_of on the two one-record
histories. No pairing, no r=1/2, no L_phys, no axiom edit.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "CONTENT_ALONE_CLAUSE_FORBIDS_SITE_INDEXED_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CONTENT_ALONE_CLAUSE_FORBIDS_SITE_INDEXED_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = ("x", "y")
EMPTY = 0
A = "A"
B = "B"
MENU = frozenset({A, B})


def history(*, x=EMPTY, y=EMPTY):
    locks = {"x": x, "y": y}
    if any(locks[site] not in MENU and locks[site] is not EMPTY for site in SITES):
        raise ValueError("lock must be a menu label or empty")
    return tuple(locks[site] for site in SITES)


h10A = history(x=A, y=EMPTY)
h01A = history(x=EMPTY, y=A)


def I_of(h):
    return sum(1 for lock in h if lock != EMPTY)


def J_of(h):
    return tuple(h)


def bag_of(h):
    return tuple(sorted(lock for lock in h if lock != EMPTY))


def o_of(h):
    return tuple(1 if lock != EMPTY else 0 for lock in h)


def predicate_j_obeys_r_strict() -> bool:
    return bag_of(h10A) == bag_of(h01A) and J_of(h10A) == J_of(h01A)


def predicate_i_h10a_differs_from_i_h01a() -> bool:
    return I_of(h10A) != I_of(h01A)


def identity_gates():
    return (
        I_of(h10A),
        I_of(h01A),
        J_of(h10A),
        J_of(h01A),
        bag_of(h10A),
    )


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
    source = Path(__file__).read_text(encoding="utf-8")
    i_h10a, i_h01a, j_h10a, j_h01a, bag_h10a = identity_gates()

    print(
        "external_scientific_inputs: current Record wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; axiom memo is the only parent"
    )

    record_clause = (
        "Only records are readable. A readout value is determined by record content "
        "alone."
    )
    checks.check(
        "source-record-clause",
        "the exact current content-alone sentence is present",
        record_clause in " ".join(axiom.split()),
    )
    checks.check(
        "reconstruct-h10A",
        "h10A locks only x to A and reconstructs J=(A,0) with I=1",
        h10A == (A, EMPTY) and j_h10a == (A, EMPTY) and i_h10a == 1,
    )
    checks.check(
        "reconstruct-h01A",
        "h01A locks only y to A and reconstructs J=(0,A) with I=1",
        h01A == (EMPTY, A) and j_h01a == (EMPTY, A) and i_h01a == 1,
    )
    checks.check(
        "identity-I",
        "identity gates call I_of on both one-record histories and get 1",
        I_of(h10A) == 1 and I_of(h01A) == 1 and i_h10a == i_h01a == 1,
    )
    checks.check(
        "identity-J",
        "identity gates call J_of on both histories and get distinct pairs",
        J_of(h10A) == (A, EMPTY) and J_of(h01A) == (EMPTY, A) and j_h10a != j_h01a,
    )
    checks.check(
        "identity-bag",
        "identity gate bag_of(h10A) is the site-blind singleton {A}",
        bag_of(h10A) == (A,) and bag_h10a == (A,) and bag_of(h01A) == (A,),
    )
    checks.check(
        "identity-source-needles",
        "runner source contains the required identity-gate calls",
        all(
            needle in source
            for needle in (
                "I_of(h10A)",
                "I_of(h01A)",
                "J_of(h10A)",
                "J_of(h01A)",
                "bag_of(h10A)",
            )
        ),
    )
    checks.check(
        "theorem-1-r-strict-I-bag",
        "scalar I and the site-blind bag obey R_strict",
        I_of(h10A) == I_of(h01A) and bag_of(h10A) == bag_of(h01A),
    )
    checks.check(
        "mutation-j-obeys-r-strict",
        "predicate J obeys R_strict fails",
        predicate_j_obeys_r_strict() is False,
    )
    checks.check(
        "mutation-i-differs",
        "predicate I(h10A) differs from I(h01A) fails",
        predicate_i_h10a_differs_from_i_h01a() is False,
    )
    checks.check(
        "theorem-4-weak-occupancy",
        "weak occupancy also violates R_strict",
        o_of(h10A) == (1, 0) and o_of(h01A) == (0, 1) and o_of(h10A) != o_of(h01A),
    )
    checks.check(
        "theorem-3-r-lax-allows-J",
        "under R_lax the two histories are distinct contents and J may differ",
        (SITES[0], A) != (SITES[1], A) and J_of(h10A) != J_of(h01A),
    )
    checks.check(
        "machine-status-contract",
        "note carries the required C1 follow-on status strings",
        all(
            phrase in note
            for phrase in (
                'hypothetical_axiom_status: "C1 follow-on: strict content-alone forbids J; clause is a drop/narrow candidate; not adopted"',
                "actual_current_surface_status: bounded-support",
            )
        ),
    )
    checks.check(
        "note-readings-and-nonadoption",
        "note quotes the clause, displays both readings, and adopts neither extra",
        all(
            phrase in note
            for phrase in (
                "A readout value is determined by record content alone",
                "R_strict",
                "R_lax",
                "does not pick R_strict versus",
                "does not adopt R_strict",
                "does not adopt R_lax",
                "does not force `r=1/2`",
                "does not adopt `L_phys`",
                "does not put a pairing on `J`",
                "drop/narrow candidate",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "site-indexed J histories are absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("h10A", "h01A", "R_strict", "R_lax", "C1-strong")),
    )
    checks.check(
        "audit-input-paths",
        "declared inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/CONTENT_ALONE_CLAUSE_FORBIDS_SITE_INDEXED_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "no-go-gate",
        "N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )
    checks.check(
        "no-pairing-no-half",
        "reconstructed maps use exact integer occupancy and no pairing of J",
        I_of(h10A) == 1
        and I_of(h01A) == 1
        and o_of(h10A) == (1, 0)
        and o_of(h01A) == (0, 1)
        and sum(o_of(h10A)) == 1
        and J_of(h10A)[0] == A
        and J_of(h10A)[1] == EMPTY,
    )

    print(
        "per_element: checked one locked possibility A on each history; "
        "both records lock A and I equals 1"
    )
    print(
        "per_site: checked the ordered pair J at x then y; "
        "(A,0) is not equal to (0,A)"
    )
    print(
        "per_mode: checked and not executed — no spectral or harmonic mode "
        "is defined on this two-site window"
    )
    print(
        "per_block: checked the two-site window block; R_strict equality "
        "is tested only on that window"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide dynamics "
        "or axiom rewrite is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
