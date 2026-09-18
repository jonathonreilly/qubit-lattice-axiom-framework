#!/usr/bin/env python3
"""J:attack:PR8028 — pattern (c) EXECUTED NUMBERS: helper TOTAL 32 and 42.

Note: sector helper performs 32 controls; Dirichlet helper performs 42.
HIT if runner-cache TOTAL lines disagree.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/static-uniform-block38-20260907"
SEC = "logs/runner-cache/gauge_wilson_static_source_sector_controls_2026_09_07.txt"
DIRI = "logs/runner-cache/gauge_wilson_static_source_dirichlet_controls_2026_09_07.txt"


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def total(path: str) -> int | None:
    m = re.search(r"TOTAL: (\d+)", git_show(path))
    return int(m.group(1)) if m else None


def main() -> None:
    s, d = total(SEC), total(DIRI)
    print(f"sector TOTAL {s} stated 32; Dirichlet TOTAL {d} stated 42")
    hits = []
    if s != 32:
        hits.append(f"sector TOTAL {s} != 32")
    if d != 42:
        hits.append(f"Dirichlet TOTAL {d} != 42")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - sector 32 and Dirichlet 42 match cache; does not fire")


if __name__ == "__main__":
    main()
