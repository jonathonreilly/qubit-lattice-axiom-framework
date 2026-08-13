#!/usr/bin/env python3
"""Exact checks: uniqueness-per-site is J's type, not a theorem of I.

Displayed C1 type J:W→{0}∪M. Legal unit lock L is a value. Double mark D
is not. Scalar I is defined on L only; occupancy-count of D is 1.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "UNIQUENESS_PER_SITE_IS_J_TYPE_NOT_A_THEOREM_OF_I_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/UNIQUENESS_PER_SITE_IS_J_TYPE_NOT_A_THEOREM_OF_I_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

W = ("x", "y")
M = frozenset({"A", "B"})
J_CODOMAIN = frozenset({0}) | M
UNIT_I = 1  # convention; Record additivity does not force the unit

# Legal unit lock L: J=(A,0), o=(1,0), I=1.
L = {
    "name": "L",
    "J": {"x": "A", "y": 0},
    "o": {"x": 1, "y": 0},
}

# Counterfactual double mark D: J*(x)={A,B}, J*(y)=∅.
D = {
    "name": "D",
    "marks": {"x": frozenset({"A", "B"}), "y": frozenset()},
}


def normalize(text: str) -> str:
    return " ".join(text.split())


def J_of(history: dict) -> tuple:
    """Displayed C1 value as the ordered pair (J(x), J(y))."""
    return (history["J"]["x"], history["J"]["y"])


def _site_values(obj: dict) -> tuple:
    if "J" in obj:
        return tuple(obj["J"][site] for site in W)
    if "marks" in obj:
        return tuple(obj["marks"][site] for site in W)
    raise TypeError("object supplies neither a C1 map nor a mark-map")


def is_J_value(obj: dict) -> bool:
    """True iff obj is a value of J:W→{0}∪M."""
    try:
        return all(value in J_CODOMAIN for value in _site_values(obj))
    except TypeError:
        return False


def is_legal_occupancy(history: dict) -> bool:
    if "o" not in history or "J" not in history:
        return False
    occupancy = history["o"]
    lock = history["J"]
    if any(occupancy[site] not in (0, 1) for site in W):
        return False
    if not is_J_value(history):
        return False
    for site in W:
        formed = occupancy[site] == 1
        locked = lock[site] != 0
        if formed != locked:
            return False
    return True


def I_of(history: dict) -> int:
    """Scalar I on legal occupancies / unit locks. Unit-count convention."""
    if not is_legal_occupancy(history):
        raise TypeError("current scalar I is not defined on this object")
    occupied = sum(1 for site in W if history["o"][site] == 1)
    return occupied * UNIT_I


def occ_count(mark_map: dict) -> int:
    """Number of sites with a nonempty mark. Defined on D without typing D as J."""
    return sum(1 for site in W if mark_map["marks"][site])


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

    print("external_scientific_inputs: current axiom wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: uniqueness-per-site is not an I-equation on the displayed window; C1 is not adopted")

    checks.check(
        "source-record-lock-one",
        "the axiom memo states that a record locks exactly one admissible local possibility",
        "locks exactly one admissible local possibility" in normalized_axiom,
    )
    checks.check(
        "source-record-one-per-site",
        "the axiom memo states that a site never carries more than one record",
        "A site never carries more than one record" in normalized_axiom,
    )
    checks.check(
        "honest-menu-excludes-zero",
        "honest M={A,B} has 0 notin M, so the rejector is not a zero token",
        0 not in M and J_CODOMAIN == frozenset({0, "A", "B"}),
    )

    # Identity gates required by the spec.
    j_L = J_of(L)
    d_is_j = is_J_value(D)
    i_L = I_of(L)
    c_D = occ_count(D)

    checks.check(
        "identity-J-of-L",
        "J_of(L) is the legal unit lock (A, 0)",
        j_L == ("A", 0) and is_J_value(L),
    )
    checks.check(
        "mutation-D-not-J-value",
        "predicate 'D is a value of J:W→{0}∪M' fails",
        d_is_j is False,
    )
    checks.check(
        "mutation-I-of-L-is-one",
        "predicate 'I(L)≠1' fails by the unit-count convention",
        i_L == 1,
    )
    checks.check(
        "mutation-occ-count-D-is-one",
        "predicate 'occ_count(D)≠1' fails",
        c_D == 1,
    )

    i_undefined_on_D = False
    try:
        I_of(D)
    except TypeError:
        i_undefined_on_D = True
    checks.check(
        "I-domain-excludes-D",
        "current scalar I is not defined on the double mark, so no I-equation fails on D",
        i_undefined_on_D,
    )
    checks.check(
        "double-mark-contents",
        "D marks {A,B} at x and empty at y, and {A,B} is not in {0}∪M",
        D["marks"]["x"] == frozenset({"A", "B"})
        and D["marks"]["y"] == frozenset()
        and frozenset({"A", "B"}) not in J_CODOMAIN,
    )
    checks.check(
        "note-type-not-I-theorem",
        "the note states uniqueness is J's type, not a theorem of I, and does not adopt C1",
        all(
            phrase in normalized_note
            for phrase in (
                "not a theorem of I",
                "Those sentences are the type of J",
                "C1 is not adopted",
                "not enlarged to power-set valued maps",
            )
        ),
    )
    checks.check(
        "note-not-c1zero",
        "the note displays the type gap and separates it from a zero-token menu",
        all(
            phrase in normalized_note
            for phrase in (
                "This Is Not A Zero-Token Menu Gap",
                "{A, B} ∉ {0} ∪ M",
                "not a zero token",
            )
        ),
    )
    checks.check(
        "note-non-claims",
        "the note refuses r=1/2, L_phys, pairing on J, and additivity-forced I=1",
        all(
            phrase in normalized_note
            for phrase in (
                "does not force a formation rate `r = 1/2`",
                "does not adopt a physical lattice carrier `L_phys`",
                "does not put a pairing",
                "does not claim Record additivity forces `I = 1`",
            )
        )
        and "cheapest change" not in normalized_note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required hypothetical and bounded-support status strings",
        all(
            phrase in note
            for phrase in (
                'hypothetical_axiom_status: "C1 follow-on: at most one lock per site is J\'s type, not a property of I; not adopted"',
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo is not rewritten with C1 maps or double-mark notation",
        all(
            phrase not in axiom
            for phrase in (
                "J : W → {0} ∪ M",
                "J*(x) = {A, B}",
                "double mark",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "N1-N8 and the do-not-ship list are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )

    print("per_element: legal unit lock L and double mark D are the only displayed histories")
    print("per_site: both objects occupy only x; y is unformed / unmarked")
    print("per_mode: occupancy-count and C1 typing are the only compared readouts")
    print("lattice_wide: checked and not executed — the window is two named sites")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
