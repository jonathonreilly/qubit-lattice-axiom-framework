#!/usr/bin/env python3
"""J:attack-e:PR8152 — pattern (e) SAMPLED EVIDENCE.

Not the known frame-third-column HIT (unnormalized q1×q2).

M1: a non-polar point has infinite SO(2)_q orbit (executed: 12 distinct
positions under the 3/5,4/5 rotation). Adversarial extra rational rotations
instead of more samples of the same one. HIT if a non-polar unit point
returns in finitely many steps (a finite invariant set outside {q,-q}).
"""
from __future__ import annotations

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def rot_z(c, s):
    return sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def main() -> int:
    pole = sp.Matrix([0, 0, 1])
    pairs = [
        (sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(5, 13), sp.Rational(12, 13)),
        (sp.Rational(8, 17), sp.Rational(15, 17)),
        (sp.Rational(7, 25), sp.Rational(24, 25)),
    ]
    pt = sp.Matrix([sp.Rational(3, 5), 0, sp.Rational(4, 5)])
    for c, s_ in pairs:
        Rz = rot_z(c, s_)
        if sp.simplify(c**2 + s_**2 - 1) != 0:
            hit(f"({c},{s_}) not on the circle")
            continue
        if Rz * pole != pole:
            hit(f"rotation {c} does not fix the pole")
        seen = []
        cur = pt
        cycled = False
        for step in range(1, 25):
            cur = sp.simplify(Rz * cur)
            t = tuple(cur)
            if t in seen:
                hit(f"non-polar point returned at step {step} under c={c}")
                cycled = True
                break
            seen.append(t)
        print(f"c={c}: {len(seen)} distinct images in 24 steps; cycle={cycled}")
        if (cur - pt).norm() == 0 and not cycled:
            # 24-step return would have been caught
            pass

    if HITS:
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - adversarial extra "
        "rational rotations about z (5/13, 8/17, 7/25 plus the executed 3/5) "
        "keep 24 distinct images of a non-polar unit point; M1's infinite-orbit "
        "claim is not a sampled never; not the known frame-normalization HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
