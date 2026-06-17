#!/usr/bin/env python3
"""Finite Hamming-complementation support for the AC_phi_lambda discussion.

This runner checks only finite algebraic facts:

* complementation maps hw=1 corners to hw=2 corners;
* complementation commutes with the C3[111] rotation;
* both triplets are free C3 orbits;
* the fixed-locus density arithmetic is the same;
* the three-slot circulant mass multiset is invariant under slot relabeling.

Rigidity addendum (the classification is exhaustive on this finite surface):

* R-A: all 48 coordinate-permutation/bit-flip relabelings of the corner cube
  (S3 semidirect Z2^3, x_i -> x_{pi(i)} xor f_i) classify exactly as
  3 frame rotations,
  3 orientation transpositions, 6 triplet swaps (complementation composed
  with the former), or 36 grading-breaking maps that do not preserve the
  hw in {1,2} surface at all;
* R-B: by the Noether degree bound (|C3| = 3) the C3-invariant readout
  ring is generated in degree <= 3; the degree-by-degree decomposition is
  symmetric span + one orientation-odd line spanned by u - v, and
  (u - v)(slots) = -6 sqrt(3) B^3 sin(3 delta) exactly - the
  orientation-odd readout is the sin(3 delta) class stripped with the
  orientation convention, while symmetric readouts see only cos(3 delta);
  non-C3-invariant components are frame-dependent;
* R-C: the listed per-triplet invariant profiles (cardinality, free-cycle
  structure, pairwise Hamming distances) are equal elementwise. None of those
  profiles supplies an unequal triplet weight; a relative triplet weight
  would be a new dimensionless import, not a surface move.

It does not read or write the Tier-A registry, apply audit status, retire an
admission, or derive the physical species bridge.
"""
from __future__ import annotations

import itertools
from pathlib import Path

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

    section("Rigidity R-A: classification of all 48 coordinate-permutation/bit-flip relabelings")
    perms = list(itertools.permutations(range(3)))
    cyclic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    counts = {
        "frame": 0,
        "orientation": 0,
        "swap": 0,
        "swap_orientation": 0,
        "nonexistent": 0,
    }
    for pi in perms:
        for f in corners:
            def g(x, pi=pi, f=f):
                return tuple(x[pi[i]] ^ f[i] for i in range(3))

            i1, i2 = sorted(g(c) for c in hw1), sorted(g(c) for c in hw2)
            is_cyclic = pi in cyclic
            if i1 == sorted(hw1) and i2 == sorted(hw2):
                counts["frame" if is_cyclic else "orientation"] += 1
            elif i1 == sorted(hw2) and i2 == sorted(hw1):
                counts["swap" if is_cyclic else "swap_orientation"] += 1
            else:
                counts["nonexistent"] += 1
    check(
        "48 coordinate-permutation/bit-flip cube relabelings classify as 3+3+3+3 grading-preserving + 36 grading-breaking",
        counts
        == {
            "frame": 3,
            "orientation": 3,
            "swap": 3,
            "swap_orientation": 3,
            "nonexistent": 36,
        },
        detail=str(counts),
    )
    note_text = Path("docs/ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md").read_text(
        encoding="utf-8"
    )
    note_flat = " ".join(note_text.split())
    check(
        "source note scopes R-A to the order-48 coordinate-permutation/bit-flip universe",
        "coordinate-permutation/bit-flip cube automorphism group" in note_flat
        and "`x_i -> x_{pi(i)} xor f_i`" in note_flat
        and "not the larger affine group `AGL(3,2)`" in note_flat,
    )
    check(
        "every grading-preserving relabeling is frame, orientation, or complementation-composed",
        counts["frame"] + counts["orientation"] + counts["swap"] + counts["swap_orientation"] == 12,
        detail="the compensated classes exhaust the grading-preserving subgroup (order 12)",
    )
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    xs = [x1, x2, x3]
    e_polys = [
        x1 + x2 + x3,
        x1 * x2 + x1 * x3 + x2 * x3,
        x1 * x2 * x3,
    ]
    full_s3_invariant = all(
        sp.expand(
            p.subs({x1: xs[q[0]], x2: xs[q[1]], x3: xs[q[2]]}, simultaneous=True) - p
        )
        == 0
        for p in e_polys
        for q in perms
    )
    check(
        "elementary symmetric readouts are invariant under the full S3 (orientation included)",
        full_s3_invariant,
    )

    section("Rigidity R-B: readout decomposition is exhaustive (Noether degree bound)")
    u = x1**2 * x2 + x2**2 * x3 + x3**2 * x1
    v = x1 * x2**2 + x2 * x3**2 + x3 * x1**2
    rot_sub = {x1: x2, x2: x3, x3: x1}
    swp_sub = {x1: x2, x2: x1}
    check(
        "u and v are C3-invariant and exchanged by a transposition (orientation-odd pair)",
        sp.expand(u.subs(rot_sub, simultaneous=True) - u) == 0
        and sp.expand(v.subs(rot_sub, simultaneous=True) - v) == 0
        and sp.expand(u.subs(swp_sub, simultaneous=True) - v) == 0,
    )

    def c3_invariant_dim(d):
        monos = [m for m in itertools.product(range(d + 1), repeat=3) if sum(m) == d]
        fixed = sum(1 for m in monos if (m[1], m[2], m[0]) == m)
        return sp.Rational(len(monos) + 2 * fixed, 3)

    def s3_invariant_dim(d):
        monos = {
            tuple(sorted(m, reverse=True))
            for m in itertools.product(range(d + 1), repeat=3)
            if sum(m) == d
        }
        return len(monos)

    dims = [(d, c3_invariant_dim(d), s3_invariant_dim(d)) for d in (1, 2, 3)]
    check(
        "degree 1-3 C3-invariant dimensions are 1, 2, 4 vs symmetric 1, 2, 3 (one odd line, degree 3)",
        [(d, int(c), s) for d, c, s in dims] == [(1, 1, 1), (2, 2, 2), (3, 4, 3)],
        detail=f"dims (deg, C3, S3) = {[(d, int(c), s) for d, c, s in dims]}; "
        "Noether bound |C3| = 3 => the invariant ring is generated in degree <= 3",
    )
    a2, B2, delta2 = sp.symbols("a2 B2 delta2", positive=True, real=True)
    slots2 = [a2 + 2 * B2 * sp.cos(delta2 + 2 * sp.pi * k / 3) for k in range(3)]
    uv_slots = sp.simplify(
        sp.expand_trig(
            sp.expand(
                (u - v).subs(
                    {x1: slots2[0], x2: slots2[1], x3: slots2[2]}, simultaneous=True
                )
            )
        )
    )
    check(
        "(u - v)(slots) = -6 sqrt(3) B^3 sin(3 delta) exactly (orientation-odd = sin class)",
        sp.simplify(uv_slots + 6 * sp.sqrt(3) * B2**3 * sp.sin(3 * delta2)) == 0,
        detail=f"(u - v)(slots) = {uv_slots}",
    )
    w = u - v
    w_squared_s3 = all(
        sp.expand(
            (w**2).subs({x1: xs[q[0]], x2: xs[q[1]], x3: xs[q[2]]}, simultaneous=True)
            - w**2
        )
        == 0
        for q in perms
    )
    check("the square of the orientation-odd generator is S3-symmetric", w_squared_s3)

    section("Rigidity R-C: per-triplet invariant profiles are equal elementwise")

    def profile(triplet):
        free = is_free_three_cycle(triplet)
        pair_dists = sorted(
            sum(p ^ q for p, q in zip(c1, c2))
            for c1, c2 in itertools.combinations(triplet, 2)
        )
        return (len(triplet), free, pair_dists)

    check(
        "cardinality, free-cycle structure, and pairwise Hamming distances coincide",
        profile(hw1) == profile(hw2),
        detail=f"profile = {profile(hw1)} for both triplets",
    )
    check(
        "the hw label is the only distinguishing datum in this check and is exchanged by complementation",
        sorted(complement(c) for c in hw1) == sorted(hw2)
        and profile(hw1) == profile(hw2),
        detail="a relative triplet weight is not derivable from equal profiles; "
        "it would be a new dimensionless import",
    )

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
