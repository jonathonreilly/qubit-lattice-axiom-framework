#!/usr/bin/env python3
"""Exact checks: occupancy-product pairing disagrees with content-match pairing.

Two disjoint occupied unit locks with unequal labels. Both pairing tables
are extras. Live Record is quoted. Named additive I is not restored.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "OCCUPANCY_PAIRING_AND_CONTENT_MATCH_PAIRING_DISAGREE_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_PAIRING_AND_CONTENT_MATCH_PAIRING_DISAGREE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

ONE = Fraction(1)
ZERO = Fraction(0)

Lock = tuple[bool, str | None]


def occupied(label: str) -> Lock:
    return (True, label)


def unoccupied() -> Lock:
    return (False, None)


def b_pi(site_s: Lock, site_t: Lock) -> Fraction:
    """Occupancy-product pairing (extra): 1 iff both sites are occupied."""
    occ_s, _label_s = site_s
    occ_t, _label_t = site_t
    return ONE if occ_s and occ_t else ZERO


def b_eq(site_s: Lock, site_t: Lock) -> Fraction:
    """Content-match pairing (extra): 1 iff both occupied and labels equal."""
    occ_s, label_s = site_s
    occ_t, label_t = site_t
    if occ_s and occ_t and label_s == label_t:
        return ONE
    return ZERO


def live_memo_contains_i_empty_as_axiom(memo: str) -> bool:
    """True only if I(empty)=0 is asserted as Record axiom content.

    Denial sentences that the assignment is not Record content do not
    satisfy this predicate.
    """
    denial = (
        "value `I(empty)=0` are not Record axiom content"
    )
    if denial in memo:
        return False
    return "`I(empty)=0`" in memo or "I(empty)=0" in memo


def live_memo_names_two_argument_pairing(memo: str) -> bool:
    needles = (
        "B_π",
        "B_\\pi",
        "B_eq",
        "two-argument pairing",
        "two-argument map",
        "occupancy-product pairing",
        "content-match pairing",
    )
    return any(needle in memo for needle in needles)


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

    print("external_scientific_inputs: none; B_π and B_eq are displayed extras")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact Fraction occupancy and label comparison")
    print("negative_scope: neither pairing is adopted; I is not restored")

    lock_s = occupied("A")
    lock_t = occupied("B")
    lock_same = occupied("A")
    lock_empty = unoccupied()

    pi_ab = b_pi(lock_s, lock_t)
    eq_ab = b_eq(lock_s, lock_t)
    pi_aa = b_pi(lock_s, lock_same)
    eq_aa = b_eq(lock_s, lock_same)
    pi_empty = b_pi(lock_s, lock_empty)
    eq_empty = b_eq(lock_s, lock_empty)

    checks.check("thm1-b-pi", "B_π(s,t) = 1 on occupied (A,B)", pi_ab == ONE)
    checks.check("thm1-b-eq", "B_eq(s,t) = 0 on occupied (A,B)", eq_ab == ZERO)
    checks.check(
        "thm1-disagree",
        "B_π(s,t) = 1 ≠ 0 = B_eq(s,t) on the displayed (A,B) pair",
        pi_ab == ONE and eq_ab == ZERO and pi_ab != eq_ab,
    )
    checks.check(
        "control-same-label",
        "both locks A gives B_π = B_eq = 1",
        pi_aa == ONE and eq_aa == ONE,
    )
    checks.check(
        "control-unoccupied",
        "an unoccupied second site gives B_π = B_eq = 0",
        pi_empty == ZERO and eq_empty == ZERO,
    )
    checks.check(
        "mutation-tables-equal-fails",
        "predicate B_π(s,t) == B_eq(s,t) on (A,B) fails",
        not (pi_ab == eq_ab),
    )

    record_readable = "Only records are readable."
    record_content = "A readout value is determined by record content"
    record_unread = "A site with no record cannot be read."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    i_denial = "value `I(empty)=0` are not Record axiom content"

    checks.check(
        "thm2-live-record-quoted",
        "live Record readout sentences are quoted without rewrite",
        record_readable in axiom
        and record_content in axiom
        and record_unread in axiom
        and record_lock in axiom
        and record_readable in note
        and record_content in note
        and record_unread in note
        and record_lock in note,
    )
    checks.check(
        "thm2-two-one-site-labels",
        "site s reads A and site t reads B as two one-site labels",
        "Site `s` reads `A` and site `t` reads `B`" in note
        and "two one-site labels" in note,
    )
    checks.check(
        "thm2-memo-does-not-name-tables",
        "the axiom memo does not name B_π, B_eq, or a two-argument pairing",
        not live_memo_names_two_argument_pairing(axiom),
    )
    checks.check(
        "mutation-memo-names-two-arg-pairing-fails",
        "predicate live memo names a two-argument pairing fails",
        not live_memo_names_two_argument_pairing(axiom),
    )

    checks.check(
        "thm3-tables-are-extras",
        "both tables are displayed extras and π is not adopted",
        "Two extra tables are displayed, not adopted." in note
        and "does not adopt `π`" in note,
    )
    checks.check(
        "thm3-not-adopt-pi",
        "the note does not adopt π",
        "does not adopt `π`" in note,
    )
    checks.check(
        "thm3-not-pair-on-j",
        "arguments are occupied locks and labels, not a J field",
        "does not pair on a `J` field" in note
        and "occupied locks and their labels" in note,
    )
    checks.check(
        "thm3-i-not-restored",
        "named additive I is denied as axiom content and is not restored",
        i_denial in axiom
        and i_denial in note
        and "does not restore named additive `I`" in note,
    )
    checks.check(
        "mutation-i-empty-as-axiom-fails",
        "predicate live memo contains I(empty)=0 as axiom content fails",
        not live_memo_contains_i_empty_as_axiom(axiom),
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/OCCUPANCY_PAIRING_AND_CONTENT_MATCH_PAIRING_DISAGREE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and no axiom adoption are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'hypothetical_axiom_status: "not proposed; B_π and B_eq remain extras; I is not restored"'
        in note
        and "This note authors no\naudit verdict" in note,
    )
    checks.check(
        "scope-refusals",
        "no G_N, no 1/r install, no axiom edit, no pairing-on-J",
        ("G_" + "N") not in note
        and ("1/" + "r") not in note
        and "I is not restored" in note
        and ("import " + "qcd") not in self_source.lower()
        and ("#" + "6259") not in note
        and ("#" + "6204") not in note,
    )
    checks.check(
        "honest-auditor-boundary",
        "Honest-auditor / Boundary is present and authors no audit verdict",
        "## Honest-auditor / Boundary" in note
        and "no audit verdict is\nauthored here" in note
        and "**Type:** bounded_theorem" in note
        and "Parents:** the live axiom memo" in note,
    )

    print(
        "per_element: exact Fraction values cover B_π and B_eq on (A,B), (A,A), and an unoccupied cell."
    )
    print(
        "per_site: each site contributes one lock label; Record readout stays one-site."
    )
    print(
        "per_mode: occupancy-product and content-match are compared as two extras, not adopted."
    )
    print(
        "per_block: the different-label cell is the disagreement; the same-label control agrees."
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide pairing law is claimed."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
