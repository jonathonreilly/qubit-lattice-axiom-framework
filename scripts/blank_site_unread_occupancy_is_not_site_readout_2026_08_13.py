#!/usr/bin/env python3
"""Exact checks: blank-site occupancy is not a site readout.

Window algebra on two lock configurations. Live Record is quoted from the
governing Record section of the axiom memo. Occupancy and the old formation
count are computed from the supplied sets; they are not axiom readout.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "BLANK_SITE_UNREAD_OCCUPANCY_IS_NOT_SITE_READOUT_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/BLANK_SITE_UNREAD_OCCUPANCY_IS_NOT_SITE_READOUT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BLANK_UNREAD = "A site with no record cannot be read."
ONLY_RECORDS = "Only records are readable."
CONTENT_ALONE = "A readout value is determined by record content alone."


def normalize(text: str) -> str:
    return " ".join(text.split())


def governing_record_section(note: str) -> str:
    """Live Record axiom only; exclude historical discussion."""
    try:
        section = note.split("### Record / Fixed Reality", 1)[1]
        section = section.split("## Qualification", 1)[0]
    except IndexError:
        return ""
    return normalize(section)


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


def site_readout(sigma: dict[str, str], site: str) -> str | None:
    return sigma[site] if site in sigma else None


def site_readout_domain(sigma: dict[str, str], window: frozenset[str]) -> frozenset[str]:
    return frozenset(site for site in window if site in sigma)


def occupancy(sigma: dict[str, str], site: str) -> int:
    return 1 if site in sigma else 0


def supplied_formation_count(sigma: dict[str, str], window: frozenset[str]) -> int:
    return sum(1 for site in window if site in sigma)


def site_readout_of_sigma_occ_defined_at_y(sigma_occ: dict[str, str]) -> bool:
    return "y" in sigma_occ and site_readout(sigma_occ, "y") is not None


def live_memo_contains_I_empty_as_governing_content(record_section: str) -> bool:
    return "I(empty)=0" in record_section


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    record_section = governing_record_section(axiom)
    normalized_note = normalize(note)

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )

    window = frozenset({"x", "y"})
    sigma_occ: dict[str, str] = {"x": "A"}
    sigma_full: dict[str, str] = {"x": "A", "y": "B"}

    occ_domain = site_readout_domain(sigma_occ, window)
    full_domain = site_readout_domain(sigma_full, window)
    occ_count = supplied_formation_count(sigma_occ, window)
    full_count = supplied_formation_count(sigma_full, window)
    occ_occupancy = {site: occupancy(sigma_occ, site) for site in window}

    checks.check(
        "source-blank-unread",
        "live Record quotes the blank-unread sentence",
        BLANK_UNREAD in record_section,
    )
    checks.check(
        "source-only-records",
        "live Record says only records are readable",
        ONLY_RECORDS in record_section,
    )
    checks.check(
        "source-content-alone",
        "live Record determines readout value by record content alone",
        CONTENT_ALONE in record_section,
    )
    checks.check(
        "mutation-live-memo-I-empty",
        "predicate live memo contains I(empty)=0 fails on governing Record",
        live_memo_contains_I_empty_as_governing_content(record_section) is False,
    )
    checks.check(
        "source-I-excluded",
        "memo states named I and I(empty)=0 are not Record axiom content",
        "named scalar collection functional `I`" in axiom
        and "I(empty)=0` are not Record axiom content" in axiom,
    )
    checks.check(
        "t1-domain-occ",
        "site readout domain of sigma_occ is {x}",
        occ_domain == frozenset({"x"}),
    )
    checks.check(
        "t1-domain-not-W",
        "site readout domain of sigma_occ is not W",
        occ_domain != window,
    )
    checks.check(
        "t1-value-x",
        "site readout of sigma_occ at x is A",
        site_readout(sigma_occ, "x") == "A",
    )
    checks.check(
        "mutation-readout-defined-at-y",
        "predicate site readout of sigma_occ is defined at y fails",
        site_readout_of_sigma_occ_defined_at_y(sigma_occ) is False
        and site_readout(sigma_occ, "y") is None,
    )
    checks.check(
        "t2-occupancy-at-y",
        "occupancy is defined at blank y on sigma_occ with value 0",
        occ_occupancy["y"] == 0 and "y" in occ_occupancy,
    )
    checks.check(
        "t2-occupancy-total",
        "occupancy is a total function on W for sigma_occ",
        occ_occupancy == {"x": 1, "y": 0} and set(occ_occupancy) == set(window),
    )
    checks.check(
        "t2-o-not-site-readout",
        "occupancy domain W is not the site-readout domain {x}",
        set(occ_occupancy) == set(window) and occ_domain == frozenset({"x"}),
    )
    checks.check(
        "t3-count-occ",
        "supplied-set formation count on sigma_occ is 1",
        occ_count == 1,
    )
    checks.check(
        "t3-count-full",
        "supplied-set formation count on sigma_full is 2",
        full_count == 2,
    )
    checks.check(
        "t3-count-is-cardinality",
        "formation count equals cardinality of occupied sites in W",
        occ_count == len(occ_domain) and full_count == len(full_domain),
    )
    checks.check(
        "t3-full-readout-domain",
        "site readout of sigma_full is defined on all of W",
        full_domain == window and site_readout(sigma_full, "y") == "B",
    )
    checks.check(
        "t4-no-J",
        "note does not adopt J",
        "does not adopt `J`" in normalized_note or "does not adopt J" in note,
    )
    checks.check(
        "t4-no-restore-I",
        "note does not restore I",
        "does not restore `I`" in normalized_note or "does not restore I" in note,
    )
    checks.check(
        "t4-no-formation-rate",
        "note does not pick a formation rate",
        "does not pick a formation rate" in normalized_note,
    )
    checks.check(
        "note-quotes-blank-unread",
        "note quotes the live blank-unread sentence",
        BLANK_UNREAD in note,
    )
    checks.check(
        "note-status",
        "note machine status is bounded-support",
        "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the declared note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/BLANK_SITE_UNREAD_OCCUPANCY_IS_NOT_SITE_READOUT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
