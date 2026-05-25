#!/usr/bin/env python3
"""Does the framework's retained parity/chiral violation reach the generation triplet?

Test of the "cancel the flip, don't prevent it" idea. The framework already
RETAINS parity violation (cpt_exact_note: C and P individually send H -> -H,
"lattice origin of parity violation"). Question: does that violation act on the
hw=1 generation triplet to lift its S_3 mass degeneracy -- i.e., is the
generation C_3-breaking a CONSEQUENCE of the framework's existing parity
violation, or a SEPARATE flavor input?

Decisive, robust computation in momentum space on the 8 Brillouin-zone corners
{0,pi}^3 (encode pi as 1), grouped by Hamming weight 1 + 3 + 3 + 1:

  hw0: (0,0,0)
  hw1: (1,0,0),(0,1,0),(0,0,1)   <- the three generations (weight-1 triplet)
  hw2: (1,1,0),(1,0,1),(0,1,1)   <- the weight-2 (3-bar) triplet
  hw3: (1,1,1)

Three operations:
  (A) chiral/epsilon  eps(n)=(-1)^{sum n}  =>  momentum shift by (pi,pi,pi)
      = flip every coordinate. This is the operation behind H -> -H.
  (B) spatial inversion p -> -p (mod 2pi).
  (C) axis permutation S_3 (swap/cycle coordinates) -- the group that FORCES
      the generation mass degeneracy (s3_mass_matrix_no_go).

We ask: do (A) or (B) act WITHIN the hw=1 triplet (so they could lift its
degeneracy), or do they act elsewhere?

Pure finite combinatorics on 8 corners. No PDG / fitted / scale / mass input.
Asserts no audit status.
"""

from __future__ import annotations

import itertools

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


CORNERS = list(itertools.product((0, 1), repeat=3))


def weight(c):
    return sum(c)


def by_weight(w):
    return [c for c in CORNERS if weight(c) == w]


def eps_flip(c):
    # momentum shift by (pi,pi,pi): flip each coordinate 0<->1
    return tuple(1 - x for x in c)


def inversion(c):
    # p -> -p mod 2pi: 0->0, pi->pi  (since -pi == pi)
    return c  # every corner is fixed


def axis_perm(c, sigma):
    return tuple(c[sigma[i]] for i in range(3))


def main() -> int:
    print("=" * 76)
    print("RETAINED PARITY/CHIRAL VIOLATION vs THE GENERATION TRIPLET")
    print("=" * 76)

    hw1 = set(by_weight(1))
    hw2 = set(by_weight(2))
    print(f"\n  hw=1 triplet (generations): {sorted(hw1)}")
    print(f"  hw=2 triplet (3-bar):       {sorted(hw2)}")

    # (A) chiral / epsilon: maps hw=1 -> hw=2 (out of the generation sector)
    print("\n" + "-" * 76)
    print("(A) chiral eps (H -> -H operation): momentum flip by (pi,pi,pi)")
    print("-" * 76)
    img = {eps_flip(c) for c in hw1}
    check("eps maps the hw=1 triplet ENTIRELY into the hw=2 triplet", img == hw2,
          detail=f"image = {sorted(img)}")
    check("eps does NOT act within the hw=1 triplet (image disjoint from hw1)",
          img.isdisjoint(hw1))
    print("        -> eps relates generations (3) to anti-generations (3-bar),")
    print("           NOT one generation to another. It cannot lift the hw=1")
    print("           degeneracy (it is not an operator on the triplet).")

    # (B) spatial inversion: fixes every corner -> identity on the triplet
    print("\n" + "-" * 76)
    print("(B) spatial inversion p -> -p (mod 2pi)")
    print("-" * 76)
    fixed = all(inversion(c) == c for c in hw1)
    check("inversion fixes every hw=1 corner (acts as identity on the triplet)", fixed)
    print("        -> identity on the triplet; commutes with every mass matrix;")
    print("           cannot lift the degeneracy.")

    # (C) axis permutation S_3: permutes the hw=1 triplet within itself
    print("\n" + "-" * 76)
    print("(C) axis permutation S_3 (the degeneracy-forcing group)")
    print("-" * 76)
    within = all({axis_perm(c, s) for c in hw1} == hw1
                 for s in itertools.permutations(range(3)))
    check("every axis permutation maps the hw=1 triplet onto itself (acts within)",
          within)
    # a transposition genuinely swaps two generations
    swap = (1, 0, 2)
    swapped = {axis_perm(c, swap) for c in hw1}
    moved = sum(1 for c in hw1 if axis_perm(c, swap) != c)
    check("an axis transposition genuinely swaps two generations (moves 2, fixes 1)",
          swapped == hw1 and moved == 2, detail=f"moved {moved} corners")

    # the three operations are distinct
    print("\n" + "-" * 76)
    print("The three operations are distinct")
    print("-" * 76)
    check("eps (hw1->hw2) != axis permutation (hw1->hw1)", img != hw1)
    check("inversion (identity) != axis transposition (nontrivial on hw1)", moved > 0)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  THE RETAINED PARITY/CHIRAL VIOLATION DOES NOT REACH THE GENERATION\n"
            "  TRIPLET.\n"
            "  * The chiral eps operation (the one behind H -> -H) maps the hw=1\n"
            "    triplet ENTIRELY onto the hw=2 (3-bar) triplet: it relates\n"
            "    generations to anti-generations, not one generation to another.\n"
            "    It is not even an operator on the triplet, so it cannot lift the\n"
            "    hw=1 S_3 mass degeneracy.\n"
            "  * Spatial inversion fixes every hw=1 corner -> identity on the\n"
            "    triplet -> cannot lift the degeneracy.\n"
            "  * The group that DOES act within the triplet, and whose breaking\n"
            "    lifts the degeneracy, is the axis-permutation S_3 -- a DISTINCT\n"
            "    operation from the framework's chiral/parity violation.\n\n"
            "  Honest consequence: the 'cancel the flip using the framework's\n"
            "  existing parity violation' route does NOT reach the generations.\n"
            "  The chiral/parity violation lives on the 3 <-> 3-bar\n"
            "  (particle/antiparticle-like) axis; the generation S_3 -> C_3\n"
            "  breaking is a SEPARATE input, in the flavor sector (the unaudited\n"
            "  a3_route1 / yt_class_6,7 C_3-breaking cluster), not supplied by the\n"
            "  retained CPT parity violation.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
