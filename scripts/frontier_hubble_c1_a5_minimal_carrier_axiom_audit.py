#!/usr/bin/env python3
"""Archive-firewall runner for the stale Lane 5 A5 carrier-axiom packet.

This registered runner intentionally does not certify a minimal carrier axiom
or live support for (G1)/(C1).  The source note is archived, audited_failed,
and retracted.  A PASS here means only that the note carries the required
non-authority boundary and that this script no longer presents the failed
minimal-carrier wrapper as active science.
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "archive_unlanded"
    / "stale-frames-2026-04-30"
    / "HUBBLE_LANE5_C1_A5_MINIMAL_CARRIER_AXIOM_AUDIT_NOTE_2026-04-28.md"
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
    print("HUBBLE LANE 5 A5 CARRIER-AXIOM ARCHIVE-FIREWALL RUNNER")
    print("=" * 78)
    print("Scope: source-boundary witness only; no minimality theorem is certified.")
    print()

    check("archived source note exists", NOTE.exists(), str(NOTE))
    if not NOTE.exists():
        print(f"SUMMARY: HUBBLE A5 ARCHIVE FIREWALL PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
        return 1

    note = NOTE.read_text(encoding="utf-8")

    check(
        "title and status mark the packet retracted",
        contains_all(
            note,
            (
                "# Historical Lane 5 `(C1)` Gate A5 Carrier-Axiom Packet (Retracted)",
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
                "claim_id `hubble_lane5_c1_a5_minimal_carrier_axiom_audit_note_2026-04-28`",
                "`audit_status: audited_failed`",
                "`effective_status: retained_no_go`",
                "not as an active docs claim",
            ),
        ),
        "row identity and failed wrapper rationale present",
    )
    check(
        "archive firewall rejects active A5 authority",
        contains_all(
            note,
            (
                "not an active A5 audit",
                "not live support for `(G1)` or `(C1)` closure",
                "not authority for a minimal carrier-axiom narrative",
                "fresh proof surface rather than this failed wrapper frame",
            ),
        ),
        "minimal-carrier narrative remains retracted",
    )
    check(
        "registered-runner contract demotes this script to a firewall witness",
        contains_all(
            note,
            (
                "## 2026-06-18 registered-runner contract",
                "The registered runner for this archived row is a firewall witness only.",
                "It must not be used to re-prove the historical minimal-carrier theorem.",
                "A PASS does not certify a minimal carrier axiom",
            ),
        ),
        "runner contract present in note",
    )
    check(
        "archive boundary denies live support for G1/C1",
        contains_all(
            note,
            (
                "This is an archive-only recovery note, not an active audit.",
                "minimal-carrier framing is retracted as live support for `(G1)` or `(C1)`",
                "A future carrier-axiom analysis must be rebuilt from a fresh proof",
                "surface and current dependencies",
            ),
        ),
        "old A5 wrapper cannot be used as live support",
    )
    check(
        "no active retained/clean status line is present",
        no_active_status_line(note),
        "actual status remains archived_failed/retracted only",
    )

    print()
    print(f"SUMMARY: HUBBLE A5 ARCHIVE FIREWALL PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
