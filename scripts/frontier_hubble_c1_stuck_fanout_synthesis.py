#!/usr/bin/env python3
"""Archive-firewall runner for the stale Lane 5 stuck-fan-out packet.

This registered runner intentionally does not certify global exhaustion or
hidden-route closure for (C1).  The source note is archived, audited_failed,
and retracted.  A PASS here means only that the note carries the required
non-authority boundary and that this script no longer presents the failed
wrapper as an active no-hidden-route proof.
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "archive_unlanded"
    / "stale-frames-2026-04-30"
    / "HUBBLE_LANE5_C1_STUCK_FANOUT_SYNTHESIS_NOTE_2026-04-28.md"
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
    print("HUBBLE LANE 5 STUCK-FAN-OUT ARCHIVE-FIREWALL RUNNER")
    print("=" * 78)
    print("Scope: source-boundary witness only; no global exhaustion is certified.")
    print()

    check("archived source note exists", NOTE.exists(), str(NOTE))
    if not NOTE.exists():
        print(
            f"SUMMARY: HUBBLE STUCK FANOUT ARCHIVE FIREWALL PASS={PASS_COUNT} "
            f"FAIL={FAIL_COUNT}"
        )
        return 1

    note = NOTE.read_text(encoding="utf-8")

    check(
        "title and status mark the packet retracted",
        contains_all(
            note,
            (
                "# Historical Lane 5 `(C1)` Gate Stuck Fan-Out Packet (Retracted)",
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
                "claim_id `hubble_lane5_c1_stuck_fanout_synthesis_note_2026-04-28`",
                "`audit_status: audited_failed`",
                "`effective_status: retained_no_go`",
                "do not cite this wrapper as exhaustion or Axiom* minimality support",
            ),
        ),
        "row identity and failed wrapper rationale present",
    )
    check(
        "archive firewall rejects global-exhaustion authority",
        contains_all(
            note,
            (
                "not an active global exhaustion proof",
                "not Axiom* minimality support",
                "not authority that no hidden `(C1)` route remains",
                "use the separately audited/narrow route-no-go cluster",
            ),
        ),
        "failed wrapper remains archive-only",
    )
    check(
        "registered-runner contract demotes this script to a firewall witness",
        contains_all(
            note,
            (
                "## 2026-06-18 registered-runner contract",
                "The registered runner for this archived row is a firewall witness only.",
                "It must not be used to re-prove the historical global-exhaustion wrapper.",
                "A PASS does not certify global exhaustion",
            ),
        ),
        "runner contract present in note",
    )
    check(
        "archive boundary denies live G1/G2/C1 closure",
        contains_all(
            note,
            (
                "This is an archive-only recovery note, not an active audit-grade exhaustion",
                "It does not retain `(G1)`, `(G2)`, or `(C1)`",
                "does not extend `A_min`",
                "Route-local boundaries",
                "must come from the separately audited narrow route-no-go cluster",
            ),
        ),
        "old fan-out wrapper cannot be used as global no-go support",
    )
    check(
        "no active retained/clean status line is present",
        no_active_status_line(note),
        "actual status remains archived_failed/retracted only",
    )

    print()
    print(
        f"SUMMARY: HUBBLE STUCK FANOUT ARCHIVE FIREWALL PASS={PASS_COUNT} "
        f"FAIL={FAIL_COUNT}"
    )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
