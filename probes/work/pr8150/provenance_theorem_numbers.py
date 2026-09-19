#!/usr/bin/env python3
"""J:provenance:PR8150 — theorem-statement numbers vs note / runner / exact count."""
from __future__ import annotations

import subprocess
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = None
BRANCH = "physics-loop/admissibility-induced-law-block16-static-law-not-a-mixture-of-formation-laws-20260915"
NOTE = (
    "docs/ADMISSIBILITY_RULE_STATIC_LAW_IS_NOT_A_MIXTURE_OF_FORMATION_LAWS_ON_ANY_"
    "WINDOW_WITH_A_CYCLE_FLIP_MONOTONICITY_BOUNDED_THEOREM_NOTE_2026-09-15.md"
)
RUNNER = "scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    r = git("rev-parse", f"origin/{BRANCH}")
    head = r.stdout.strip()
    if git("cat-file", "-e", head).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
        head = git("rev-parse", f"origin/{BRANCH}").stdout.strip()
    out = git("show", f"{head}:{path}")
    if out.returncode != 0:
        raise SystemExit(out.stderr[:400])
    return out.stdout


def n_qual(n, edges):
    nbr = {i: [] for i in range(n)}
    for a, b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    c = 0
    for perm in permutations(range(n)):
        pos = [0] * n
        for t, i in enumerate(perm):
            pos[i] = t
        if all(sum(1 for u in nbr[s] if pos[u] < pos[s]) < 2 for s in range(n)):
            c += 1
    return c


def main() -> None:
    note = show(NOTE)
    runner = show(RUNNER)
    items = [
        ("(3, 1, 2)", ["(3, 1, 2)", "(3,1,2)", "p = 3"]),
        ("2x3", ["2x3", "2×3", "2 x 3"]),
        ("plaquette", ["plaquette"]),
        ("cycle", ["containing a cycle", "a cycle"]),
        ("at least two", ["at least two", "size at least two"]),
    ]
    unsourced = []
    for token, alts in items:
        src = None
        for name, blob in (("NOTE", note), ("RUNNER", runner)):
            for alt in alts:
                for line in blob.splitlines():
                    if alt in line:
                        src = f"{name}: {line.strip()[:140]}"
                        break
                if src:
                    break
            if src:
                break
        if src:
            print(f"OK | {token} | {src}")
        else:
            print(f"UNSOURCED | {token}")
            unsourced.append(token)
    q4 = n_qual(4, [(i, (i + 1) % 4) for i in range(4)])
    q3 = n_qual(3, [(0, 1), (1, 2)])
    print(f"DERIVED | C4 qualifying={q4} (0); path3 qualifying={q3}/6")
    if q4 != 0:
        unsourced.append(f"C4 qualifying {q4}")
        print("HIT: C4 qualifying != 0")
    if unsourced:
        for u in unsourced:
            print("HIT:", u)
        print("SUMMARY: provenance FIRED; " + "; ".join(unsourced))
        return
    print(
        "SUMMARY: provenance OK — claim_scope (3,1,2), 2x3, plaquette/cycle "
        "and 'at least two' sourced in the note/runner; C4 qualifying 0 and "
        "path3 4/6 derived exactly"
    )


if __name__ == "__main__":
    main()
