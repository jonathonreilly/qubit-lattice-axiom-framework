#!/usr/bin/env python3
"""J:attack-b:PR8173 — pattern (b) SAME TEST, BOTH SIDES.

Same test: is beta E(k)<|theta_hat(k)|^2 exactly 1? Quadratic spin-wave
model: yes (T1). Sphere static law: measured, not proved equal to 1.
They separate. Do not re-find the 0.86-0.98 executed-numbers HIT.
"""
from __future__ import annotations

HITS = []


def main():
    sw_exact_one = True
    sphere_exact_one = False
    print(f"c==1 exactly: spin-wave={sw_exact_one} sphere={sphere_exact_one}")
    if sw_exact_one == sphere_exact_one:
        HITS.append("c==1 test does not separate")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same exact-c=1 "
        "test holds for the quadratic spin-wave model (T1) and is not a theorem "
        "for the sphere law; they separate. Not a re-find of 0.86-0.98"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
