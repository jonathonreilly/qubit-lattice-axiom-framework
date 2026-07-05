#!/usr/bin/env python3
"""Guard the architecture-portability post-audit evidence firewall.

This runner is source-hygiene support only. It does not re-audit the
portability theorem and does not set an audit verdict. It checks that the
archived failed packet remains retired as evidence and that historical summary
surfaces point to the live runner-backed sweep note instead.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ARCHIVE = ROOT / "archive_unlanded" / "work-history-unverifiable-portability-2026-04-30" / "ARCHITECTURE_PORTABILITY_AUDIT_2026-04-11.md"
SWEEP = ROOT / "docs" / "ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md"
LANE_BOARD = ROOT / "docs" / "work_history" / "repo" / "LANE_STATUS_BOARD.md"
DISCOVERY_LOG = ROOT / "docs" / "work_history" / "POTENTIAL_PUBLICATION_DISCOVERIES_LOG.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    require(path.exists(), f"missing expected file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    archive = read(ARCHIVE)
    sweep = read(SWEEP)
    lane_board = read(LANE_BOARD)
    discovery_log = read(DISCOVERY_LOG)

    require("**Status:** RETRACTED 2026-04-30" in archive, "archive retraction status is missing")
    require("historical / diagnostic and retired as evidence" in archive, "archive is not explicitly retired as evidence")
    require("must not be\nlisted as an evidence note" in archive, "archive evidence firewall sentence is missing")
    require("Historical Original Text Below Is Retracted" in archive, "historical text is not visibly retracted")
    require("## Verdict" not in archive, "archive still exposes the old live Verdict heading")
    require("## Exact Retained Wording" not in archive, "archive still exposes the old live retained wording heading")
    require("Retainable to `main`" not in archive, "archive still carries the old retainable assertion")

    require("scripts/frontier_architecture_portability_sweep.py" in sweep, "live sweep note lost its primary runner")
    require("This is a portability companion, not a standalone Newton closure." in sweep, "live sweep boundary is missing")

    stale_link = "ARCHITECTURE_PORTABILITY_AUDIT_2026-04-11.md`](../../../archive_unlanded"
    require(stale_link not in lane_board, "lane board still lists the archived audit packet as a start-here evidence note")
    require("ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md" in lane_board, "lane board lost the live sweep note")
    require("retired as evidence" in lane_board, "lane board does not flag the archived packet as evidence-retired")

    stale_discovery_link = "ARCHITECTURE_PORTABILITY_AUDIT_2026-04-11.md`](../../archive_unlanded"
    require(stale_discovery_link not in discovery_log, "discovery log still lists the archived audit packet as evidence")
    require("ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md" in discovery_log, "discovery log lost the live sweep note")
    require("not part of this D-item evidence chain" in discovery_log, "discovery log does not exclude the archived packet")

    print("PASS: architecture portability archived-audit evidence firewall holds")


if __name__ == "__main__":
    main()
