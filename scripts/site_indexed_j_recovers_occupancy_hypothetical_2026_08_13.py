#!/usr/bin/env python3
"""Exact checks: site-indexed J recovers occupancy under displayed C1.

Window W={x,y}. Menu M={A,B}. Current readout I is scalar cardinality.
Displayed C1 readout J is site-indexed. Identity gates call I_of(o10),
J_of(o10), and o_from_J. The predicate that I splits o10 from o01 must
fail. The predicate that J(o10)=J(o01) must fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "SITE_INDEXED_J_RECOVERS_OCCUPANCY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SITE_INDEXED_J_RECOVERS_OCCUPANCY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

WINDOW = ("x", "y")
MENU = ("A", "B")


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class History:
    occupancy: tuple[int, int]
    locks: tuple[object, object]

    def occ_at(self, site: str) -> int:
        return self.occupancy[WINDOW.index(site)]

    def lock_at(self, site: str) -> object:
        return self.locks[WINDOW.index(site)]


def make_history(occ_x: int, occ_y: int, lock_x: object = 0, lock_y: object = 0) -> History:
    if occ_x not in (0, 1) or occ_y not in (0, 1):
        raise ValueError("occupancy bits must be 0 or 1")
    if occ_x == 0 and lock_x != 0:
        raise ValueError("unoccupied x cannot lock")
    if occ_y == 0 and lock_y != 0:
        raise ValueError("unoccupied y cannot lock")
    if occ_x == 1 and lock_x not in MENU:
        raise ValueError("occupied x must lock a menu entry")
    if occ_y == 1 and lock_y not in MENU:
        raise ValueError("occupied y must lock a menu entry")
    return History((occ_x, occ_y), (lock_x, lock_y))


o00 = make_history(0, 0)
o10 = make_history(1, 0, lock_x="A")
o01 = make_history(0, 1, lock_y="A")
o11 = make_history(1, 1, lock_x="A", lock_y="A")


def I_of(history: History) -> int:
    return sum(history.occupancy)


def J_of(history: History) -> tuple[object, object]:
    values = []
    for site in WINDOW:
        if history.occ_at(site) == 0:
            values.append(0)
        else:
            values.append(history.lock_at(site))
    return (values[0], values[1])


def o_from_J(site_indexed: tuple[object, object]) -> tuple[int, int]:
    return tuple(0 if label == 0 else 1 for label in site_indexed)


def I_from_J(site_indexed: tuple[object, object]) -> int:
    return sum(1 for label in site_indexed if label != 0)


def site_blind_mu() -> tuple[str, str]:
    """Same one-site law token at both sites."""
    return ("same-law-on-M", "same-law-on-M")


def i_table() -> tuple[int, int, int, int]:
    return (I_of(o00), I_of(o10), I_of(o01), I_of(o11))


def pi_table() -> tuple[int, int, int, int]:
    ox = (o00.occupancy[0], o10.occupancy[0], o01.occupancy[0], o11.occupancy[0])
    oy = (o00.occupancy[1], o10.occupancy[1], o01.occupancy[1], o11.occupancy[1])
    return (ox[0] * oy[0], ox[1] * oy[1], ox[2] * oy[2], ox[3] * oy[3])


def i_splits_o10_from_o01() -> bool:
    return I_of(o10) != I_of(o01)


def j_of_o10_equals_j_of_o01() -> bool:
    return J_of(o10) == J_of(o01)


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
        "occupancy bits and both 2x2 tables are reconstructed here"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read "
        "for claim-surface consistency"
    )
    print(
        "negative_scope: only scalar I as a splitter of o10/o01 and silent "
        "adoption of C1 or of a pairing through I are rejected"
    )

    checks.check(
        "source-records-form",
        "the axiom states that records form",
        "Records form." in axiom,
    )
    checks.check(
        "source-content-only",
        "the axiom makes readout content-only",
        "Only records are readable." in axiom
        and "A readout value is determined by record content alone." in normalized_axiom,
    )
    checks.check(
        "source-record-I",
        "the axiom supplies additive I with I(empty)=0",
        "I(empty)=0" in axiom,
    )
    checks.check(
        "source-formation-site-unsupplied",
        "the Admissibility reading note does not supply formation site",
        "does not supply the formation site, probability, or rate" in normalized_axiom,
    )
    checks.check(
        "source-does-not-name-J",
        "the axiom memo does not name the displayed site-indexed J",
        "J(z)" not in axiom and "site-indexed J" not in axiom,
    )

    identity_I = I_of(o10)
    identity_J = J_of(o10)
    identity_o = o_from_J(identity_J)

    checks.check(
        "theorem1-I-does-not-split",
        "I(o10)=I(o01)=1 and site-blind mu is the same",
        identity_I == 1
        and I_of(o01) == 1
        and site_blind_mu()[0] == site_blind_mu()[1],
    )
    checks.check(
        "theorem1-J-splits",
        "J(o10)=(A,0) differs from J(o01)=(0,A)",
        identity_J == ("A", 0) and J_of(o01) == (0, "A") and identity_J != J_of(o01),
    )
    checks.check(
        "theorem2-retract",
        "o_from_J recovers occupancy on every {0,1}-occupancy of W",
        identity_o == o10.occupancy
        and o_from_J(J_of(o00)) == o00.occupancy
        and o_from_J(J_of(o01)) == o01.occupancy
        and o_from_J(J_of(o11)) == o11.occupancy,
    )
    checks.check(
        "theorem3-I-J-equals-I",
        "I_J equals current I on the four occupancies",
        all(I_from_J(J_of(history)) == I_of(history) for history in (o00, o10, o01, o11))
        and I_of(o00) == 0
        and I_of(o11) == 2,
    )
    checks.check(
        "theorem3-i-table",
        "the reconstructed I-table is (0,1,1,2)",
        i_table() == (0, 1, 1, 2),
    )
    checks.check(
        "theorem3-pi-table",
        "the reconstructed product table is (0,0,0,1)",
        pi_table() == (0, 0, 0, 1) and i_table() != pi_table(),
    )
    checks.check(
        "mutation-I-splits",
        "the predicate that I splits o10 from o01 fails",
        i_splits_o10_from_o01() is False,
    )
    checks.check(
        "mutation-J-equal",
        "the predicate that J(o10)=J(o01) fails",
        j_of_o10_equals_j_of_o01() is False,
    )
    checks.check(
        "source-note-display",
        "the note displays J, refuses C1, and keeps the pairing extra",
        all(
            phrase in normalized_note
            for phrase in (
                "J(o10)=(A,0)",
                "J(o01)=(0,A)",
                "I(o10)=1=I(o01)",
                "(0,1,1,2)",
                "(0,0,0,1)",
                "does not adopt C1",
                "does not force `r=1/2`",
                "does not adopt `L_phys`",
                "does not by itself dissolve that pairing",
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
        "the source uses the required C1 and bounded-support fields",
        all(
            phrase in note
            for phrase in (
                'hypothetical_axiom_status: "C1 counterfactual: Record readout is site-indexed J, not scalar I; not adopted"',
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
        "the displayed C1 map is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("o10", "o_from_J", "L_phys", "C1 counterfactual")
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "no later compiler exists" in note,
    )

    print(
        "per_element: each site of W is assigned 0 or a locked menu entry in J"
    )
    print(
        "per_site: two named sites with unit locks; I(o10) and I(o01) are both 1"
    )
    print(
        "per_mode: checked and not executed — no spectral or harmonic mode is used"
    )
    print(
        "per_block: only the scalar-I versus site-indexed-J readout block is tested"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide formation rate is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
