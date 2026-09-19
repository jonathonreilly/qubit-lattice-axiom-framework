#!/usr/bin/env python3
"""J:derive:tight-sibling-lemma:a6 (worker w-macbookpro90c72-jf526, grok-4.6).

Route (iv): block 31 witnesses W1 and controls Z_A, Z_B against the hard inductive case.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "lib"))
from family import W1, Z_A, Z_B, kinds, run_automaton, single_seed_min

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def load(data):
    root, (A, B, L), marks = data[0], data[1], data[2]
    sites = [(a, b, c) for a in range(A) for b in range(B) for c in range(L)]
    zeta = {tuple(z): 1 for z in marks}
    eta = run_automaton(sites, zeta)
    return root, eta, kinds(eta)


def v_of(eta, z):
    val, _, _ = single_seed_min(eta, z, 1)
    return val


def e_w1():
    root, eta, (ones, npred, kind) = load(W1)
    ok("W1.1 root is processed", kind.get(root) == "proc")
    vr = v_of(eta, root)
    ok("W1.2 single-seed v(root)=-2", vr == F(-2), str(vr))
    hard = 0
    n_allproc = 0
    min_pred = None
    for z in ones:
        if kind[z] != "proc":
            continue
        pw = [u for u in npred[z] if kind.get(u) == "proc"]
        if len(pw) != len(npred[z]) or len(pw) < 2:
            continue
        n_allproc += 1
        vs = [v_of(eta, u) for u in pw]
        if None in vs:
            continue
        m = max(vs)
        min_pred = m if min_pred is None else max(min_pred, m)
        if all(v == 0 for v in vs):
            hard += 1
    ok("W1.3 no hard case (all 1-preds tight processed)", hard == 0, f"allproc={n_allproc}")
    ok("W1.4 max v among those processed 1-preds is negative", min_pred is not None and min_pred < 0, str(min_pred))


def e_za():
    root, eta, (ones, npred, kind) = load(Z_A)
    vr = v_of(eta, root)
    ok("ZA.1 single-seed v(root)=0 (tight processed root)", vr == F(0), str(vr))
    pw = [u for u in npred[root] if kind.get(u) == "proc"]
    ok("ZA.2 root has three processed 1-preds", len(pw) == 3 == len(npred[root]), str(npred[root]))
    vs = [v_of(eta, u) for u in pw]
    ok("ZA.3 those preds have v=-1,-1,-1", vs == [F(-1), F(-1), F(-1)], str(vs))
    ok("ZA.4 not a hard case (preds are not tight)", not all(v == 0 for v in vs))
    hard = 0
    for z in ones:
        if kind[z] != "proc":
            continue
        preds = npred[z]
        if not preds or any(kind.get(u) != "proc" for u in preds):
            continue
        vs = [v_of(eta, u) for u in preds]
        if vs and all(v == 0 for v in vs):
            hard += 1
    ok("ZA.5 no hard case anywhere in Z_A", hard == 0)


def e_zb():
    root, eta, (ones, npred, kind) = load(Z_B)
    vr = v_of(eta, root)
    ok("ZB.1 single-seed v(root)=0", vr == F(0), str(vr))
    pw = list(npred[root])
    ok("ZB.2 root has three 1-preds, all processed", len(pw) == 3 and all(kind.get(u) == "proc" for u in pw), str(pw))
    vs = sorted(v_of(eta, u) for u in pw)
    ok("ZB.3 pred values are {-1,-1,0}", vs == [F(-1), F(-1), F(0)], str(vs))
    ok("ZB.4 exactly one tight processed pred, not all three: not a hard case", vs.count(F(0)) == 1)
    hard = 0
    for z in ones:
        if kind[z] != "proc":
            continue
        preds = npred[z]
        if not preds or any(kind.get(u) != "proc" for u in preds):
            continue
        vals = [v_of(eta, u) for u in preds]
        if None in vals:
            continue
        if all(v == 0 for v in vals):
            hard += 1
    ok("ZB.5 no hard case anywhere in Z_B among single-seed-defined v", hard == 0)


def main():
    e_w1()
    e_za()
    e_zb()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: ROUTE FAILS AT step (iv) named witnesses: W1, Z_A, Z_B contain processed sites with all-processed "
        "1-predecessors, but those predecessors are never all tight. Z_A's root is tight with three preds at v=-1; "
        "Z_B's root is tight with pred values {-1,-1,0}; W1's root has v=-2. No counterexample to the lemma among "
        "these configurations. (W2/W3 have multiple seeds, so single-seed DP does not apply.)"
    )
    print(
        "HIT: block 31 W1 and controls Z_A, Z_B are not counterexamples to the tight-sibling lemma: exact single-seed "
        "DP gives v(W1 root)=-2; v(Z_A root)=0 with three processed preds each v=-1; v(Z_B root)=0 with pred values "
        "{-1,-1,0}. The hard case (every 1-pred tight processed) does not occur on these mark sets."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
