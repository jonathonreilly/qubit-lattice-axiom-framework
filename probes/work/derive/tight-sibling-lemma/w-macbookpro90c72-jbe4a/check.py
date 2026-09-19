#!/usr/bin/env python3
"""Exact local census for J:derive:tight-sibling-lemma:a5 (worker w-macbookpro90c72-jbe4a).

Route (i): 2x2x2 cube below a processed site, all 256 noise patterns.
Route (iv): block 31 witnesses W1,W2,W3 are not tight-sibling counterexamples.
"""
from __future__ import annotations

import os
import sys
from collections import Counter
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "lib"))
from family import (  # noqa: E402
    W1,
    W2,
    W3,
    brute_min,
    kinds,
    preds,
    run_automaton,
    single_seed_min,
)


def cube_sites():
    return [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]


def main() -> int:
    failures = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        extra = f" {detail}" if detail else ""
        print(f"CHECK {name}: {'PASS' if cond else 'FAIL'}{extra}")
        if not cond:
            failures.append(name)

    sites = cube_sites()
    root = (1, 1, 1)
    pred_root = preds(root)
    check("E0", len(sites) == 8 and len(pred_root) == 3)

    n_eta1 = 0
    n_proc = 0
    n_two_proc_preds = 0
    n_tight_pair = 0
    vmin = Counter()
    for bits in product((0, 1), repeat=8):
        zeta = {sites[i]: bits[i] for i in range(8) if bits[i]}
        eta = run_automaton(sites, zeta)
        if eta.get(root, 0) != 1:
            continue
        n_eta1 += 1
        ones, npred, kind = kinds(eta)
        if kind.get(root) != "proc":
            continue
        n_proc += 1
        pw = [u for u in npred[root] if kind.get(u) == "proc"]
        if len(pw) < 2:
            continue
        n_two_proc_preds += 1
        vals = []
        for w in pw:
            bm = brute_min(eta, w, 1)
            if bm is None:
                continue
            vals.append(bm)
            vmin[bm] += 1
            if bm == 0:
                n_tight_pair += 1
        if any(v == 0 for v in vals) and len(vals) >= 2 and min(vals) == 0:
            print("TIGHT PAIR", zeta, pw, vals)
    print(
        f"CUBE census: eta(root)=1 in {n_eta1}/256; processed root {n_proc}; "
        f"two-proc-preds {n_two_proc_preds}; tight-pair hits {n_tight_pair}; "
        f"brute_min values {sorted(vmin.items())}"
    )
    check("E1a", n_tight_pair == 0, f"tight hits {n_tight_pair}")
    check("E1b", n_two_proc_preds > 0, f"n_two={n_two_proc_preds}")
    check("E1c", 0 not in vmin, f"values {dict(vmin)}")

    # Route (iv): block 31 witnesses, rooted at their declared roots
    for name, W in (("W1", W1), ("W2", W2), ("W3", W3)):
        root_w, box, marks = W
        A, B, L = box
        sites_w = [(a, b, c) for a in range(A) for b in range(B) for c in range(L)]
        zeta = {tuple(m): 1 for m in marks}
        eta = run_automaton(sites_w, zeta)
        ones, npred, kind = kinds(eta)
        check(f"{name}root1", eta.get(root_w, 0) == 1, f"eta[root]={eta.get(root_w)}")
        if kind.get(root_w) == "proc":
            pw = [u for u in npred[root_w] if kind.get(u) == "proc"]
            tight = 0
            for w in pw:
                smin, seeds, _ = single_seed_min(eta, w, 1)
                bm = brute_min(eta, w, 1) if len(ones) <= 14 else smin
                print(f"  {name} pred {w} kind={kind.get(w)} single_seed={smin} brute={bm} nseeds={None if seeds is None else len(seeds)}")
                if bm == 0 or smin == 0:
                    tight += 1
            check(f"{name}notight", tight == 0, f"tight preds {tight} of {len(pw)}")
        else:
            print(f"  {name} root kind={kind.get(root_w)}")
            check(f"{name}notight", True, "root not processed")

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: on the isolated 2x2x2 cube, every noise pattern (256) in which the "
        "top site is processed with at least two processed 1-predecessors has "
        f"brute_min(c=1) in {sorted(vmin)} at those predecessors, never 0 "
        f"(n_two_proc_preds={n_two_proc_preds}). Block 31 witnesses W1,W2,W3 are "
        "not tight-sibling counterexamples. Local route (i) holds on this cone; "
        "the lemma is not proved on the infinite lattice."
    )
    print(
        "SUMMARY: PARTIAL exhaustive 2x2x2 cube: no tight processed sibling pair "
        f"sharing a processed successor (n_two={n_two_proc_preds}, values {sorted(vmin)}); "
        "W1-W3 of block 31 are not counterexamples; the tight-sibling lemma remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
