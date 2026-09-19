#!/usr/bin/env python3
"""J:derive:tight-sibling-lemma:a1 (worker w-macbookpro90c72-j133a).

Independent of a3 (isolated depth-2 1024) and a5 (2x2x2 256): exhaustive 3x2x2
box (4096 noise patterns) for processed successors of two processed 1-predecessors.
Integers throughout (brute_min at c=1).
"""
from __future__ import annotations

import os
import sys
from collections import Counter
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "lib"))
from family import brute_min, is_fork, kinds, preds, run_automaton  # noqa: E402

FAILS: list[str] = []
OKS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def sites_3x2x2():
    return [(x, y, z) for x in range(3) for y in range(2) for z in range(2)]


def main():
    sites = sites_3x2x2()
    check("E0.n12", len(sites) == 12)
    vmin = Counter()
    n_two_proc = 0
    n_tight = 0
    n_patterns = 0
    for bits in product((0, 1), repeat=12):
        n_patterns += 1
        zeta = {sites[i]: bits[i] for i in range(12)}
        eta = run_automaton(sites, zeta)
        ones, npred, kind = kinds(eta)
        for z in ones:
            if kind[z] != "proc":
                continue
            pps = [p for p in npred[z] if p in kind and kind[p] == "proc"]
            if len(pps) < 2:
                continue
            # sibling pair among processed 1-predecessors
            for i in range(len(pps)):
                for j in range(i + 1, len(pps)):
                    u, v = pps[i], pps[j]
                    if not is_fork(u, v):
                        continue
                    n_two_proc += 1
                    val = brute_min(eta, z, 1)
                    if val is None:
                        continue
                    vmin[val] += 1
                    if val == 0:
                        n_tight += 1
    check("E1.4096", n_patterns == 4096)
    print("E2.two-proc-sibling-successor cases", n_two_proc)
    print("E2.brute_min histogram", dict(sorted(vmin.items())))
    check("E2.no-tight", n_tight == 0, f"n_tight={n_tight} hist={dict(vmin)}")
    check("E2.never-positive", all(v <= 0 for v in vmin), f"{list(vmin)}")
    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: exhaustive 3x2x2 (4096 noise patterns): every processed site "
        f"whose 1-predecessors include a fork-related processed pair has brute_min "
        f"in {sorted(vmin)} at c*=1, never 0 ({n_two_proc} such successor cases). "
        "No local tight-sibling counterexample in this box; lemma still open on Z^3. "
        "Independent of a3/a5 windows."
    )
    print(
        "SUMMARY: PARTIAL no tight processed-sibling successor on the 3x2x2 box "
        f"(brute_min in {sorted(vmin)}, never 0); lemma open on the infinite lattice"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
