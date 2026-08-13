#!/usr/bin/env python3
"""Exact two-site checks: J's 0 is absence, not a menu element.

Identity gates call o_from_J on the honest histories u, v and on the
displayed ambiguous_J0. Occupancy-of-locks is well-defined only when
0 is outside the honest menu.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "J_ZERO_IS_ABSENCE_NOT_A_MENU_ELEMENT_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/J_ZERO_IS_ABSENCE_NOT_A_MENU_ELEMENT_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


# Exact integer tokens. 0 is the displayed absence symbol, not a lock label
# on the honest menu.
ABSENCE = 0
A = "A"
B = "B"

W = ("x", "y")
M = frozenset({A, B})
M0 = frozenset({ABSENCE, A})

# Honest histories as J:W → {0}∪M, written in the order (x, y).
u = (ABSENCE, A)
v = (A, ABSENCE)

# Same cell of symbols on the counterfactual menu that contains 0.
ambiguous_J0 = (ABSENCE, A)


def o_from_J(j_map: tuple[object, ...]) -> tuple[int, int]:
    """Definitional retract: 0 iff J(z)=0, else 1. Exact integers."""
    return tuple(0 if value == ABSENCE else 1 for value in j_map)  # type: ignore[return-value]


def occupancy_of_locks_well_defined(menu: frozenset[object]) -> bool:
    """Occupancy-of-locks is a function of J only when 0 is not a lock label."""
    return ABSENCE not in menu


def classifies_lock0_versus_unformed(j_map: tuple[object, ...], menu: frozenset[object]) -> bool:
    """False when J(z)=0 and 0 is a declared menu element."""
    if ABSENCE in menu and any(value == ABSENCE for value in j_map):
        return False
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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print("external_scientific_inputs: current axiom wording is source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")

    # Mutation: 0 is an element of honest M must fail.
    zero_in_honest_m = ABSENCE in M
    checks.check(
        "mutation-zero-notin-honest-M",
        "predicate '0 is an element of honest M' fails",
        zero_in_honest_m is False and occupancy_of_locks_well_defined(M) is True,
    )

    # Identity gates: must call o_from_J on u and v.
    o_u = o_from_J(u)
    o_v = o_from_J(v)
    checks.check(
        "identity-o_from_J-u",
        "o_from_J(u) equals occupancy (0,1)",
        o_u == (0, 1) and u == (0, A),
    )
    checks.check(
        "identity-o_from_J-v",
        "o_from_J(v) equals occupancy (1,0)",
        o_v == (1, 0) and v == (A, 0),
    )

    honest_codomain = frozenset({ABSENCE}) | M
    checks.check(
        "theorem1-disjoint-union",
        "honest {0}∪M is a three-point disjoint union",
        honest_codomain == frozenset({ABSENCE, A, B}) and len(honest_codomain) == 3,
    )
    checks.check(
        "theorem1-zero-means-unformed",
        "on honest M, J(z)=0 means unformed not lock 0",
        o_u[0] == 0 and u[0] == ABSENCE and A in M and ABSENCE not in M,
    )

    # Counterfactual M0 contains the token 0; the union is not disjoint.
    checks.check(
        "theorem2-M0-contains-zero",
        "counterfactual M0 contains the token 0",
        ABSENCE in M0 and M0 == frozenset({ABSENCE, A}),
    )
    collapsed_codomain = frozenset({ABSENCE}) | M0
    checks.check(
        "theorem2-union-not-disjoint",
        "{0}∪M0 equals M0 so the union is not disjoint",
        collapsed_codomain == M0 and len(collapsed_codomain) == 2,
    )

    # Identity gate on displayed ambiguous_J0.
    o_ambiguous = o_from_J(ambiguous_J0)
    lock0_occupancy_if_zero_were_a_lock = (1, 1)
    checks.check(
        "identity-o_from_J-ambiguous_J0",
        "o_from_J(ambiguous_J0) returns (0,1) and so counts a possible lock-0 as unformed",
        ambiguous_J0 == (0, A)
        and o_ambiguous == (0, 1)
        and o_ambiguous != lock0_occupancy_if_zero_were_a_lock,
    )
    checks.check(
        "mutation-M0-does-not-classify",
        "predicate 'J0 on M0 classifies lock-0 versus unformed' fails",
        classifies_lock0_versus_unformed(ambiguous_J0, M0) is False
        and occupancy_of_locks_well_defined(M0) is False,
    )
    checks.check(
        "theorem2-retract-not-occupancy-on-M0",
        "o_from_J does not recover a well-defined occupancy-of-locks on M0",
        occupancy_of_locks_well_defined(M0) is False
        and o_ambiguous == (0, 1),
    )

    record_needles = (
        "Records form.",
        "locks exactly one admissible local possibility",
        "A readout value is determined by record content alone",
        "I(empty)=0",
    )
    checks.check(
        "source-record-axiom",
        "the axiom memo still names formation, one locked possibility, content-only readout, and I(empty)=0",
        all(phrase in axiom or phrase in normalized_axiom for phrase in record_needles),
    )
    checks.check(
        "theorem3-unformed-not-a-lock",
        "the note keeps unformed outside the locked-possibility type",
        "unformed is not a locked possibility" in normalized_note
        and "tagged sum" in normalized_note
        and "0 notin M" in note,
    )

    status_needles = (
        'hypothetical_axiom_status: "C1 follow-on: J zero is absence not a lock label; 0 notin M required; not adopted"',
        "actual_current_surface_status: bounded-support",
    )
    checks.check(
        "machine-status-contract",
        "required hypothetical and surface-status strings are source-visible",
        all(phrase in note for phrase in status_needles),
    )
    checks.check(
        "theorem4-nonadoption",
        "the note does not pick {A,B}, adopt C1, or install a vacuum possibility",
        all(
            phrase in normalized_note
            for phrase in (
                "does not pick the menu `{A,B}`",
                "does not adopt C1",
                "does not install a vacuum possibility",
            )
        ),
    )
    checks.check(
        "theorem5-no-extras",
        "the note refuses r=1/2, L_phys, and a pairing on J",
        all(
            phrase in note
            for phrase in (
                "Do not force `r=1/2`",
                "Do not adopt `L_phys`",
                "Do not put a pairing on `J`",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo is not edited with C1, J, or a zero lock token",
        all(
            phrase not in normalized_axiom
            for phrase in (
                "o_from_J",
                "ambiguous_J0",
                "0 notin M",
                "site-indexed J",
            )
        )
        and "Records form." in axiom,
    )
    checks.check(
        "identity-gate-surface",
        "the note names the three identity-gate calls",
        "o_from_J(u)" in note
        and "o_from_J(v)" in note
        and "ambiguous_J0" in note
        and "o_from_J(ambiguous_J0)" in note,
    )

    print("per_element: two honest J-cells and one ambiguous M0 cell are checked with exact integer retracts")
    print("per_site: both window sites are read; classification fails at the site that writes 0 on M0")
    print("per_mode: not executed — no spectral or rate object is claimed")
    print("per_block: the only negative block is 0-as-lock-label versus 0-as-absence")
    print("lattice_wide: checked and not executed — the window is two sites; no lattice-wide adoption is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
