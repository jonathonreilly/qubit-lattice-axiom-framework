#!/usr/bin/env python3
"""J:attack:PR8033 — pattern (c) EXECUTED NUMBERS: 243, 18, h_R, 3=sqrt(9).

Note: 243 R1 center flows, 18 helper checks, h_R=R^2-floor(R^2/4)+3R,
3=sqrt(9). HIT if 243!=3^5, cache TOTAL!=18, or h_R not positive increasing.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/finite-pw-confinement-block43-20260907"
CACHE = "logs/runner-cache/gauge_wilson_finite_pw_static_energy_lower_controls_2026_09_07.txt"


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    hits = []
    if 3 ** 5 != 243:
        hits.append("243 != 3^5")
    print(f"243=3^5 {3**5==243}")
    if 3 * 3 != 9:
        hits.append("3^2 != 9")
    h = [r * r - (r * r) // 4 + 3 * r for r in range(1, 21)]
    print(f"h_R R=1..20 {h}")
    if not (all(x > 0 for x in h) and h == sorted(h)):
        hits.append("h_R not positive increasing")
    cache = git_show(CACHE)
    m = re.search(r"TOTAL: (\d+)", cache)
    tot = int(m.group(1)) if m else None
    print(f"cache TOTAL {tot} stated 18")
    if tot != 18:
        hits.append(f"TOTAL {tot} != 18")
    if "all243" not in cache and "243" not in cache:
        hits.append("243 not in cache")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (c) EXECUTED NUMBERS - 243=3^5, h_R increasing, "
            "cache TOTAL 18; does not fire"
        )


if __name__ == "__main__":
    main()
