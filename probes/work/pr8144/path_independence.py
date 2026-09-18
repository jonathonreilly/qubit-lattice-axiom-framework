#!/usr/bin/env python3
"""J:attack:PR8144 — pattern (c) EXECUTED NUMBERS: path-independence of reduced energy.

claim_scope: the transfer Hamiltonian has an insertion-path-independent spectral
bottom. The runner-cache EVIDENCE_JSON general_path_green table lists two path
indices on grids 24, 40, 64 at T=1,2,5,12. HIT if any (T, grid) pair has
path_index 0 and 1 disagreeing beyond 1e-12, or if inverse_moment disagrees
with spectral_inverse_moment.
"""
from __future__ import annotations

import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/physics-loop/static-charge-transfer-sector-20260915"
CACHE = "logs/runner-cache/finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_2026_09_15.txt"


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    txt = git_show(CACHE)
    m = re.search(r"EVIDENCE_JSON: (\{.*\})\nper_element:", txt, re.S)
    if not m:
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - could not parse EVIDENCE_JSON")
        return
    data = json.loads(m.group(1))
    rows = data["general_path_green"]
    by = defaultdict(dict)
    for row in rows:
        by[(row["T"], row["grid_side"])][row["path_index"]] = row["reduced_energy"]
    hits = []
    for key, paths in sorted(by.items()):
        vals = list(paths.values())
        print(f"T={key[0]} L={key[1]} paths {paths}")
        if len(vals) < 2:
            hits.append(f"missing path at {key}")
        elif abs(vals[0] - vals[1]) > 1e-12:
            hits.append(f"path-dependent energy at {key}: {vals}")
    for case in data["inverse_moments"]["cases"]:
        a, b = case["inverse_moment"], case["spectral_inverse_moment"]
        if abs(a - b) > 1e-10:
            hits.append(f"inverse moment {a} vs spectral {b} N={case['N']} j={case['j']}")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print(
            f"SUMMARY: attack pattern (c) EXECUTED NUMBERS - {len(by)} (T,grid) pairs "
            "path-independent; inverse moments match spectra; does not fire"
        )


if __name__ == "__main__":
    main()
