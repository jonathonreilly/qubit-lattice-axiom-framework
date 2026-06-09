#!/usr/bin/env python3
"""Finite Hamming-complementation support for the AC_phi_lambda discussion.

This runner checks only finite algebraic facts:

* complementation maps hw=1 corners to hw=2 corners;
* complementation commutes with the C3[111] rotation;
* both triplets are free C3 orbits;
* the fixed-locus density arithmetic is the same;
* the three-slot circulant mass multiset is invariant under slot relabeling.

It does not read or write the Tier-A registry, apply audit status, retire an
admission, or derive the physical species bridge.
"""
from __future__ import annotations

import itertools

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("AC_PHI_LAMBDA HW-COMPLEMENTATION EQUIVARIANCE SUPPORT")
    print("=" * 88)

    corners = list(itertools.product([0, 1], repeat=3))
    hw1 = [c for c in corners if sum(c) == 1]
    hw2 = [c for c in corners if sum(c) == 2]

    def complement(c):
        return tuple(1 - x for x in c)

    def rotate(c):
        return (c[2], c[0], c[1])

    section("Hamming complementation")
    check(
        "b -> 1-b maps hw=1 bijectively to hw=2",
        sorted(complement(c) for c in hw1) == sorted(hw2),
        detail=f"hw1={hw1}, hw2={hw2}",
    )
    check(
        "complementation is involutive",
        all(complement(complement(c)) == c for c in corners),
    )
    check(
        "complementation commutes with the C3[111] rotation on every corner",
        all(complement(rotate(c)) == rotate(complement(c)) for c in corners),
    )

    section("C3 orbit structure")

    def is_free_three_cycle(triplet):
        return sorted(rotate(c) for c in triplet) == sorted(triplet) and all(
            rotate(c) != c for c in triplet
        )

    check("C3 acts as a free three-cycle on hw=1", is_free_three_cycle(hw1))
    check("C3 acts as a free three-cycle on hw=2", is_free_three_cycle(hw2))

    section("Fixed-locus density and circulant symmetric readout")
    omega = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    density = sp.simplify(
        sp.Rational(1, 3)
        * sum(1 / ((1 - omega**j) * (1 - omega ** (2 * j))) for j in (1, 2))
    )
    check("L_3(1,2) fixed-locus density reduces exactly to 2/9", density == sp.Rational(2, 9))

    a, B, delta = sp.symbols("a B delta", positive=True, real=True)
    slots = [a + 2 * B * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    e1 = sp.simplify(sum(slots))
    e2 = sp.simplify(sum(slots[i] * slots[j] for i in range(3) for j in range(i + 1, 3)))
    e3 = sp.simplify(sp.expand_trig(sp.expand(slots[0] * slots[1] * slots[2])))
    target_e3 = sp.expand_trig(a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta))
    check(
        "circulant determinant identity e3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta) is exact",
        sp.simplify(e3 - target_e3) == 0,
    )
    permuted = [slots[1], slots[2], slots[0]]
    pe1 = sp.simplify(sum(permuted))
    pe2 = sp.simplify(
        sum(permuted[i] * permuted[j] for i in range(3) for j in range(i + 1, 3))
    )
    pe3 = sp.simplify(sp.expand_trig(sp.expand(permuted[0] * permuted[1] * permuted[2])))
    check(
        "elementary symmetric polynomials are invariant under cyclic slot relabeling",
        sp.simplify(e1 - pe1) == 0
        and sp.simplify(e2 - pe2) == 0
        and sp.simplify(e3 - pe3) == 0,
    )

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
