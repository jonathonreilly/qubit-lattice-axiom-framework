#!/usr/bin/env python3
"""J:provenance:PR8144 — theorem-statement numbers vs runner cache / derivation.

Statement text = claim_scope + Parts I–IV identities (1)–(5). Each numeric
token is CACHE, DERIVED, DEFINITION, or EXCLUDED. HIT if UNCOVERED.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/physics-loop/static-charge-transfer-sector-20260915"
CACHE = "logs/runner-cache/finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_2026_09_15.txt"

# (token, role, bucket)  bucket in {cache, derived, definition, excluded}
ITEMS = [
    ("N>=1", "model domain", "definition"),
    ("beta>0", "model domain", "definition"),
    ("(1)", "c_k Poisson identity label", "excluded"),
    ("(2)", "K(j) product-of-maxima label", "excluded"),
    ("(3)", "inverse-moment bound label", "excluded"),
    ("(4)", "free-state inverse-moment label", "excluded"),
    ("(5)", "Hamiltonian moment bound label", "excluded"),
    ("8140", "upstream PR", "excluded"),
    ("8133", "upstream PR", "excluded"),
    ("8a71d7fa", "PR8140 pin", "excluded"),
    ("K(j)", "definition (2)", "definition"),
    ("kappa_q", "max_k c_k/c_{k+q}", "definition"),
    ("PASS=4", "runner TOTAL", "cache"),
    ("FAIL=0", "runner TOTAL", "cache"),
    ("24", "path-Green grid_side", "cache"),
    ("40", "path-Green grid_side", "cache"),
    ("64", "path-Green grid_side", "cache"),
    ("N=2", "inverse-moment case", "cache"),
    ("N=3", "inverse-moment case", "cache"),
    ("N=4", "inverse-moment case", "cache"),
    ("1", "K(j=0) or identity factor", "derived"),  # K(0)=1
]


def git_show(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{BRANCH}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        subprocess.run(
            ["git", "fetch", "origin", "physics-loop/static-charge-transfer-sector-20260915"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        r = subprocess.run(
            ["git", "show", f"{BRANCH}:{path}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    if r.returncode != 0:
        raise SystemExit((r.stderr or r.stdout)[:400])
    return r.stdout


def main() -> int:
    cache = git_show(CACHE)
    uncovered = []
    n_cache = n_der = n_def = n_exc = 0
    for token, role, bucket in ITEMS:
        if bucket == "cache":
            ok = token in cache or token.replace("=", " = ") in cache
            # PASS=4 appears as TOTAL: PASS=4 FAIL=0
            if token == "PASS=4":
                ok = "PASS=4" in cache
            if token == "FAIL=0":
                ok = "FAIL=0" in cache
            if token.startswith("N="):
                ok = f'"N": {token.split("=")[1]}' in cache or token in cache
            print(f"{token:12} CACHE    {role}: {'ok' if ok else 'MISSING'}")
            n_cache += 1
            if not ok:
                uncovered.append(token)
        elif bucket == "derived":
            # K(j=0)=1: each max c_k/c_k = 1
            print(f"{token:12} DERIVED  {role}: K(j=0)=prod 1 = 1")
            n_der += 1
        elif bucket == "definition":
            print(f"{token:12} DEFINITION {role}")
            n_def += 1
        else:
            print(f"{token:12} EXCLUDED {role}")
            n_exc += 1
    if uncovered:
        print("HIT: unsourced " + ", ".join(uncovered))
        print("SUMMARY: provenance (PR #8144): UNCOVERED " + ", ".join(uncovered))
        return 0
    print(
        f"SUMMARY: provenance (PR #8144): all {len(ITEMS)} listed statement "
        f"tokens sourced (cache {n_cache}, derived {n_der}, definition {n_def}, "
        f"excluded {n_exc}); K(j=0)=1 derived; TOTAL PASS=4 in cache; no UNCOVERED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
