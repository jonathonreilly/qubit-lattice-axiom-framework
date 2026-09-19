#!/usr/bin/env python3
"""J:attack-d:PR8027 — QUANTIFIER SCOPE on rho_(r,s)=2 sum_{k=1}^s cos(pi k/(L+1)).

Stated for r,s>=0, L=r+s>=1, with examples rho(1,1)=1, rho(2,1)=sqrt(2),
rho(2,2)=sqrt(5), and rho=0 if r=0 or s=0. HIT if an example or a small
(r,s) in range disagrees with the closed form / particle-hole symmetry.
"""
from __future__ import annotations

import sympy as sp


def rho(r, s):
    L = r + s
    if s == 0 or r == 0:
        return sp.Integer(0)
    return sp.simplify(2 * sum(sp.cos(sp.pi * k / (L + 1)) for k in range(1, s + 1)))


def main():
    hits = []
    examples = {
        (1, 1): sp.Integer(1),
        (2, 1): sp.sqrt(2),
        (2, 2): sp.sqrt(5),
        (0, 3): sp.Integer(0),
        (5, 0): sp.Integer(0),
    }
    for (r, s), claimed in examples.items():
        got = rho(r, s)
        ok = sp.simplify(got - claimed) == 0
        print(f"rho({r},{s})={got} claimed={claimed} ok={ok}")
        if not ok:
            hits.append(f"rho({r},{s})={got} != {claimed}")
    for r in range(0, 5):
        for s in range(0, 5):
            if r + s < 1:
                continue
            a, b = rho(r, s), rho(s, r)
            if sp.simplify(a - b) != 0:
                hits.append(f"rho({r},{s})!={rho(s,r)} particle-hole")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8027): " + "; ".join(hits[:3]))
    else:
        print(
            "SUMMARY: QUANTIFIER SCOPE on rho_(r,s)=2 sum_k cos(pi k/(L+1)) "
            "(PR #8027): examples (1,1)=1, (2,1)=sqrt(2), (2,2)=sqrt(5), zeros "
            "on axes, and r<->s all hold for r,s in 0..4; the forall holds as written"
        )


if __name__ == "__main__":
    main()
