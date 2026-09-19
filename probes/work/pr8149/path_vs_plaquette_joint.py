#!/usr/bin/env python3
"""J:attack-b:PR8149 — SAME TEST, BOTH SIDES: sequential vs joint.

U3: isolated star/path with max |A|<=1 agrees with the joint (static) law;
the plaquette (last site records two) disagrees. Identical test: TV(seq, joint).
Not the known 216-env HIT.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

P, Q, R = 3, 1, 2
VALS = ("+x", "-x", "+y", "-y", "+z", "-z")
OPP = {"+x": "-x", "-x": "+x", "+y": "-y", "-y": "+y", "+z": "-z", "-z": "+z"}
M = 6
Z1 = P + Q + 4 * R


def phi(s, t):
    if s == t:
        return P
    if OPP[s] == t:
        return Q
    return R


def K(a, s):
    return F(phi(s, a), Z1)


def Kk(rec):
    tot = F(0)
    for s in VALS:
        pr = F(1)
        for ai in rec:
            pr *= K(ai, s)
        tot += pr
    return tot


def cond(s, rec):
    if not rec:
        return F(1, M)
    num = F(1)
    for ai in rec:
        num *= K(ai, s)
    return num / Kk(rec)


def tv_seq_joint(verts, edges, order):
    pos = {x: i for i, x in enumerate(order)}
    A = {x: tuple(y for y in verts if {x, y} in edges and pos[y] < pos[x]) for x in verts}
    # sequential
    seq = {}
    joint_un = {}
    for vals in product(VALS, repeat=len(verts)):
        cfg = dict(zip(verts, vals))
        wseq = F(1)
        for x in order:
            wseq *= cond(cfg[x], tuple(cfg[y] for y in A[x]))
        wj = F(1)
        for a, b in edges:
            wj *= K(cfg[a], cfg[b])  # normalized one-site factors; joint ∝ Pi phi
        # actually static joint ∝ Pi_edges phi = Pi_edges Z1 K = const * Pi K
        seq[vals] = wseq
        joint_un[vals] = wj
    z = sum(joint_un.values())
    joint = {k: v / z for k, v in joint_un.items()}
    return sum(abs(seq[k] - joint[k]) for k in seq) / 2


def main():
    # path of 3: max |A|<=1
    path_v = ("L", "M", "R")
    path_e = {frozenset(p) for p in (("L", "M"), ("M", "R"))}
    tv_path = tv_seq_joint(path_v, path_e, ("L", "M", "R"))
    # plaquette C4
    pla_v = ("a", "b", "c", "d")
    pla_e = {frozenset(p) for p in (("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"))}
    tv_pla = tv_seq_joint(pla_v, pla_e, ("a", "b", "c", "d"))
    print(f"path L-M-R TV(seq,joint)={tv_path}")
    print(f"plaquette abcd TV(seq,joint)={tv_pla}")
    if tv_path == 0 and tv_pla > 0:
        print(
            "SUMMARY: SAME TEST BOTH SIDES on TV(sequential, joint) (PR #8149): "
            "the 3-path (max |A|<=1) has TV=0 and the plaquette (last site records two) "
            f"has TV={tv_pla}; the isolation-vs-cycle separation holds as written"
        )
    elif tv_path > 0 and tv_pla > 0:
        print(f"HIT: path also has TV={tv_path}>0, so TV(seq,joint)>0 does not separate path from plaquette")
        print("SUMMARY: SAME TEST BOTH SIDES (PR #8149): both path and plaquette have positive TV(seq,joint)")
    elif tv_path == 0 and tv_pla == 0:
        print("HIT: plaquette TV=0, sequential equals joint; U3's disagreement fails")
        print("SUMMARY: SAME TEST BOTH SIDES (PR #8149): plaquette sequential equals joint")
    else:
        print(f"HIT: unexpected TV path={tv_path} pla={tv_pla}")
        print("SUMMARY: SAME TEST BOTH SIDES (PR #8149): unexpected TV pair")


if __name__ == "__main__":
    main()
