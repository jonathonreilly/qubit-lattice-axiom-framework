#!/usr/bin/env python3
"""Archive-firewall runner for the stale Cl_4(C) consequence map.

This registered runner intentionally does not re-run the historical Axiom*
consequence cascade.  The source note is archived, audited_failed, and
retracted as live framework support.  A PASS here means only that the archived
note still carries the required non-authority boundary and that the runner
itself is a firewall witness rather than a closure witness.
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "archive_unlanded"
    / "stale-frames-2026-04-30"
    / "CL4C_CARRIER_AXIOM_CONSEQUENCE_MAP_NOTE_2026-04-28.md"
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, passed: bool, detail: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}: {detail}")
    return passed


def normalize(text: str) -> str:
    return " ".join(text.split())


def contains_all(text: str, needles: tuple[str, ...]) -> bool:
    normalized_text = normalize(text)
    return all(normalize(needle) in normalized_text for needle in needles)


def no_active_status_line(text: str) -> bool:
    forbidden_prefixes = (
        "**Actual current-surface status:** retained",
        "**Actual current-surface status:** retained_bounded",
        "**Actual current-surface status:** audited_clean",
        "**Actual current-surface status:** audited_conditional",
    )
    return not any(
        line.strip().startswith(forbidden_prefixes) for line in text.splitlines()
    )


def main() -> int:
    print("=" * 78)
    print("CL_4(C) CONSEQUENCE MAP ARCHIVE-FIREWALL RUNNER")
    print("=" * 78)
    print("Scope: source-boundary witness only; no Axiom* cascade is evaluated.")
    print()

    check("archived source note exists", NOTE.exists(), str(NOTE))
    if not NOTE.exists():
        print(f"SUMMARY: CL4C ARCHIVE FIREWALL PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
        return 1

    note = NOTE.read_text(encoding="utf-8")

    check(
        "title and status mark the packet retracted",
        contains_all(
            note,
            (
                "# Historical Cl_4(C) Carrier-Axiom Consequence Map (Retracted)",
                "**Status:** RETRACTED 2026-04-30",
            ),
        ),
        "historical/retracted title and status present",
    )
    check(
        "current-surface certificate is archived failed/retracted",
        contains_all(
            note,
            (
                "## Current-surface certificate (2026-06-12 source firewall)",
                "**Actual current-surface status:** archived `audited_failed` / retracted",
                "It may not be cited as retained, bounded, conditional,",
                "supporting, or methodological authority for any live framework chain.",
            ),
        ),
        "certificate blocks live authority use",
    )
    check(
        "audit verdict and no-go boundary are quoted in the source note",
        contains_all(
            note,
            (
                "claim_id `cl4c_carrier_axiom_consequence_map_note_2026-04-28`",
                "`audit_status: audited_failed`",
                "`effective_status: retained_no_go`",
                "archive-only recovery material, not an active claim note",
            ),
        ),
        "row identity and archived no-go rationale present",
    )
    check(
        "archive firewall rejects active consequence-map authority",
        contains_all(
            note,
            (
                "not an active Axiom* consequence map",
                "not support for a carrier-axiom closure",
                "not authority for downstream Hubble, Planck, gravity, or neutrino",
                "rebuilt from current dependencies",
            ),
        ),
        "Axiom* cascade remains archive-only",
    )
    check(
        "registered-runner contract demotes this script to a firewall witness",
        contains_all(
            note,
            (
                "## 2026-06-18 registered-runner contract",
                "The registered runner for this archived row is a firewall witness only.",
                "It must not be used to re-prove the historical closure cascade.",
                "A PASS does not adopt Axiom*",
            ),
        ),
        "runner contract present in note",
    )
    check(
        "archive boundary denies adoption and current-surface upgrades",
        contains_all(
            note,
            (
                "This is an archive-only recovery map.",
                "It does not adopt Axiom*",
                "does not retain any cosmology variable",
                "does not upgrade any conditional theorem on the current",
                "does not serve as active guidance for an extension decision",
            ),
        ),
        "closure language is explicitly retracted",
    )
    check(
        "no active retained/clean status line is present",
        no_active_status_line(note),
        "actual status remains archived_failed/retracted only",
    )

    print()
    print(f"SUMMARY: CL4C ARCHIVE FIREWALL PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
