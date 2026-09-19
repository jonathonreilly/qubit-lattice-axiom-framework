#!/usr/bin/env python3
"""J:derive:tight-sibling-lemma:a2 (worker w-macbookpro90c72-j7021).

Route (ii)-local: on the isolated 2x2x2 cube, brute_min(c=1) at every 1-site
is <= 0 (a potential-style bound: v never positive on this cone).
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
    vals = Counter()
    n_ones = 0
    n_pos = 0
    n_none = 0
    for bits in product((0, 1), repeat=8):
        zeta = {sites[i]: bits[i] for i in range(8) if bits[i]}
        eta = run_automaton(sites, zeta)
        ones, npred, kind = kinds(eta)
        for z in ones:
            n_ones += 1
            bm = brute_min(eta, z, 1)
            if bm is None:
                n_none += 1
                continue
            vals[bm] += 1
            if bm > 0:
                n_pos += 1
                print("POSITIVE", z, bm, kind[z], zeta)
    print(f"n_ones={n_ones} n_none={n_none} n_pos={n_pos} values={sorted(vals.items())}")
    check("E1", n_pos == 0, f"n_pos={n_pos}")
    check("E2", n_ones > 0)
    check("E3", all(v <= 0 for v in vals))

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        f"HIT: on the isolated 2x2x2 cube, brute_min(c=1) at every 1-site over all "
        f"256 noise patterns is in {sorted(vals)} (n_ones={n_ones}, n_none={n_none}), "
        "never positive. So v<=0 holds for every site on this cone (a local "
        "potential bound), not only at successors of processed pairs. The lemma "
        "on Z^3 is not proved."
    )
    print(
        "SUMMARY: PARTIAL 2x2x2 cube potential-style bound: v<=0 at every 1-site "
        f"in all 256 patterns (values {sorted(vals)}); infinite-lattice lemma open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
