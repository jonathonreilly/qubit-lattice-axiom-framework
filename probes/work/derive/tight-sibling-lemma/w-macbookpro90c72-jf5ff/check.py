#!/usr/bin/env python3
"""J:derive:tight-sibling-lemma:a3 (worker w-macbookpro90c72-jf5ff, grok-4.6).

Exact enumeration of the isolated depth-2 predecessor cone (route i).
"""
from __future__ import annotations

import os
import sys
from collections import Counter
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "lib"))
from family import brute_min, cone, kinds, run_automaton

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def enumerate_cone2():
    z = (2, 2, 2)
    c2 = cone(z, 2)
    sites = cone(z, 3)
    ok("E.1 depth-2 cone has 10 sites", len(c2) == 10, str(len(c2)))
    ok("E.2 depth-3 cone has 20 sites", len(sites) == 20, str(len(sites)))
    n_proc_sib = 0
    n_proc_z = 0
    vals = []
    vz_when_sib = []
    n_tight_pred = 0
    for mask in range(1 << len(c2)):
        zeta = {c2[i]: 1 for i in range(len(c2)) if mask >> i & 1}
        eta = run_automaton(sites, zeta)
        ones, npred, kind = kinds(eta)
        if kind.get(z) != "proc":
            continue
        n_proc_z += 1
        pw = [u for u in npred[z] if kind.get(u) == "proc"]
        if len(pw) < 2:
            continue
        n_proc_sib += 1
        for u in pw:
            vu = brute_min(eta, u, 1)
            vals.append(vu)
            if vu == 0:
                n_tight_pred += 1
        vz_when_sib.append(brute_min(eta, z, 1))
    ctr = Counter(vals)
    ok("E.3 processed z with >=2 processed 1-preds: 512 of 1024 mark patterns", n_proc_sib == 512, str(n_proc_sib))
    ok("E.4 n processed z (any preds)", n_proc_z > 0, str(n_proc_z))
    ok("E.5 every such predecessor has brute_min v defined", None not in vals and len(vals) == 1248, f"n={len(vals)}")
    ok("E.6 none of those predecessors is tight (v=0)", n_tight_pred == 0, str(n_tight_pred))
    ok("E.7 all predecessor v are in {-5,-6,-8,-9,-11,-14}", set(vals) <= {F(-5), F(-6), F(-8), F(-9), F(-11), F(-14)}, str(ctr))
    ok("E.8 max predecessor v is -5 < 0", max(vals) == F(-5), str(max(vals)))
    ok("E.9 min predecessor v is -14", min(vals) == F(-14), str(min(vals)))
    ok("E.10 1248 = 512 patterns x (2 or 3 processed preds)", len(vals) == 1248)
    # successor v on those patterns
    ok("E.11 successor v always defined", None not in vz_when_sib)
    ok("E.12 successor v never positive on the isolated cone", max(vz_when_sib) <= 0, str(Counter(vz_when_sib)))
    return ctr, Counter(vz_when_sib)


def main():
    ctr, ctz = enumerate_cone2()
    print("pred v counts:", dict(ctr))
    print("succ v counts:", dict(ctz))
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL isolated depth-2 predecessor cone (10 mark sites, 1024 patterns): 512 patterns have a "
        "processed z with at least two processed 1-predecessors; in all 1248 predecessor instances the exact "
        "brute-min rooted value is in {-5,-6,-8,-9,-11,-14}, never 0. Route (i) holds on the isolated cone: two "
        "processed siblings that share a processed successor are never tight. Global tightness can use nodes "
        "outside the cone; that is the first step the local enumeration does not cover."
    )
    print(
        "HIT: on the isolated depth-2 cone of a site z, every mark pattern that makes z processed with two or more "
        "processed 1-predecessors has brute_min v(u) in {-5,-6,-8,-9,-11,-14} for each such predecessor u, never "
        "v(u)=0 (512/1024 patterns, 1248 predecessor instances). Tight processed siblings sharing a processed "
        "successor do not occur in the isolated cone."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
