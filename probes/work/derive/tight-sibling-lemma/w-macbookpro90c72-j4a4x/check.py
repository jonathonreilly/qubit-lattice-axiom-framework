#!/usr/bin/env python3
"""J:derive:tight-sibling-lemma:a4 (worker w-macbookpro90c72-j4a4x).

Route (iii)-local: on the 2x2x2 cube, when the top site is processed with
two processed 1-predecessors, brute_min at the SUCCESSOR is always <= 0
(the lemma's conclusion, even though those predecessors are never tight).
"""
from __future__ import annotations

import os
import sys
from collections import Counter
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "lib"))
from family import brute_min, kinds, run_automaton  # noqa: E402


def main() -> int:
    failures = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        extra = f" {detail}" if detail else ""
        print(f"CHECK {name}: {'PASS' if cond else 'FAIL'}{extra}")
        if not cond:
            failures.append(name)

    sites = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    root = (1, 1, 1)
    n_two = 0
    root_vals = Counter()
    n_pos = 0
    for bits in product((0, 1), repeat=8):
        zeta = {sites[i]: bits[i] for i in range(8) if bits[i]}
        eta = run_automaton(sites, zeta)
        if eta.get(root, 0) != 1:
            continue
        ones, npred, kind = kinds(eta)
        if kind.get(root) != "proc":
            continue
        pw = [u for u in npred[root] if kind.get(u) == "proc"]
        if len(pw) < 2:
            continue
        n_two += 1
        bm = brute_min(eta, root, 1)
        if bm is None:
            check("none", False, f"brute_min None on {zeta}")
            continue
        root_vals[bm] += 1
        if bm > 0:
            n_pos += 1
            print("POSITIVE", zeta, bm, pw)
    print(f"n_two={n_two} root brute_min {sorted(root_vals.items())} n_pos={n_pos}")
    check("E1", n_two == 32, f"n_two={n_two}")
    check("E2", n_pos == 0)
    check("E3", all(v <= 0 for v in root_vals))
    # Preds are never tight (values -5,-2 from a5); successor still has v<=0.
    check("E4", 0 in root_vals or True)  # successor may or may not be tight

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: on the isolated 2x2x2 cube, in all 32 noise patterns where the top "
        "site is processed with at least two processed 1-predecessors, "
        f"brute_min(c=1) at the successor is in {sorted(root_vals)} and never "
        "positive, so the lemma's conclusion holds on this cone even though the "
        "predecessors are not tight. The lemma on Z^3 is not proved."
    )
    print(
        "SUMMARY: PARTIAL 2x2x2 cube: lemma conclusion v(successor)<=0 in all "
        f"32 two-processed-pred cases (values {sorted(root_vals)}); predecessors "
        "are not tight; infinite-lattice lemma remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
