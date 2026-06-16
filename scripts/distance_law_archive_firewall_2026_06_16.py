#!/usr/bin/env python3
"""Guard the archived distance-law stale-runner firewall.

This is source-hygiene support only. It does not run the audit loop and does
not set audit status. It checks that the old contradictory distance-law packet
is clearly retired as evidence and that branch-retainability context points to
current bounded replay notes instead.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded" / "gravity-distance-law-stale-runners-2026-04-30" / "DISTANCE_LAW_NOTE.md"
BRANCH_NOTE = ROOT / "docs" / "CLAUDE_BRANCH_RETAINABILITY_NOTE.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    require(path.exists(), f"missing expected file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    archive = read(ARCHIVE)
    branch_note = read(BRANCH_NOTE)

    require("**Status:** RETRACTED 2026-04-30" in archive, "archive retraction status is missing")
    require("historical / diagnostic and retired as evidence" in archive, "archive is not explicitly retired as evidence")
    require("must not be listed as live distance-law evidence" in archive, "archive live-evidence firewall missing")
    require("Historical artifact chain (retracted)" in archive, "archive artifact chain is not marked historical")
    require("Historical results (retracted)" in archive, "archive results are not marked historical")
    require("Historical conclusion (retracted)" in archive, "archive conclusion is not marked historical")
    require("## Artifact chain" not in archive, "archive still exposes a live Artifact chain heading")
    require("## Results" not in archive, "archive still exposes a live Results heading")
    require("## Honest conclusion" not in archive, "archive still exposes a live conclusion heading")

    require("docs/WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md" in branch_note, "branch note lost current wide-lattice replay pointer")
    require("retired as evidence and must not be used as a live distance-law" in branch_note, "branch note does not retire the old archive")

    print("PASS: distance-law archived evidence firewall holds")


if __name__ == "__main__":
    main()
