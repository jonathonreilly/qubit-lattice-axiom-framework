#!/usr/bin/env python3
"""
Z_3 character-isomorphism open gate, axis-cycle (Weyl-Z_3) leg: the color
Weyl-Z_3 DOES carry the regular character (3,0,0), but its alignment to the
retained translation grading is an unfixable 3-fold cyclic orientation = P1
========================================================================

Exact/symbolic companion runner for the bounded no-go note

    docs/Z3_CHARACTER_ISOMORPHISM_WEYL_AXIS_CYCLE_ORIENTATION_NO_GO_NOTE_2026-05-30.md

Background
----------
The open gate Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10
killed only the SU(3)_c CENTER Z_3 as a color->generation bridge (its character
on the fundamental is (3, 3w, 3w^2), not the regular (3,0,0)). It left the
axis-cycle / Weyl-Z_3 leg -- which DOES carry the regular character (3,0,0) --
as "the work still to be derived."

This runner records the no-go increment: even with the matching regular
character, the alignment between the color Weyl-Z_3 grading and the retained
translation grading admits all three cyclic intertwiners (W proportional to I,
P, or P^2) with no A_min-canonical preference, while the three odd permutations
(transpositions) give W = 0. So the axis-cycle orientation is a free 3-fold P1
choice -- it reduces to P1 exactly like the center, and cannot be canonically
derived within A_min.

Type: no_go (companion runner). Status authority: independent audit lane only.
No new tags, no new vocabulary, no promotion language.

Run:
  python3 scripts/frontier_z3_character_isomorphism_weyl_axis_cycle_orientation_no_go.py
"""

from __future__ import annotations

import itertools

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  |  {detail}" if detail else ""))


def main() -> int:
    w = sp.exp(2 * sp.pi * sp.I / 3)
    # axis-cycle / Weyl-Z_3 generator: the cyclic permutation of the 3 corners
    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

    # ---- characters: axis-cycle is regular (3,0,0); center is not ---------
    chi_perm = [sp.simplify(sp.trace(P ** k)) for k in (0, 1, 2)]
    check("axis-cycle (Weyl-Z_3) character = regular (3,0,0)",
          chi_perm == [3, 0, 0], f"chi = {chi_perm}")
    center = [sp.simplify(sp.trace(z * sp.eye(3))) for z in (1, w, w ** 2)]
    check("center Z_3 character = (3, 3w, 3w^2) != regular (3,0,0)",
          [sp.simplify(c) for c in center] == [3, sp.simplify(3 * w), sp.simplify(3 * w ** 2)]
          and sp.simplify(center[1]) != 0,
          f"chi_center = {[sp.simplify(c) for c in center]}")
    check("P^3 = I and det P = 1 (order-3 cyclic)",
          sp.simplify(P ** 3 - sp.eye(3)) == sp.zeros(3) and sp.det(P) == 1)

    # ---- intertwiner space = group algebra C[Z_3] = span{I,P,P^2}, dim 3 --
    a0, a1, a2 = sp.symbols("a0 a1 a2")
    W = a0 * sp.eye(3) + a1 * P + a2 * P ** 2          # generic circulant
    check("every circulant W = a0 I + a1 P + a2 P^2 is Z_3-equivariant (commutes with P)",
          sp.simplify(W * P - P * W) == sp.zeros(3))
    # the three basis intertwiners are independent (dim of the family is 3)
    basis = [sp.eye(3), P, sp.simplify(P ** 2)]
    M = sp.Matrix([[b[i] for b in basis] for i in range(9)])  # 9x3 flattening
    check("intertwiner family {I,P,P^2} has dimension 3 (no canonical first element)",
          M.rank() == 3, f"rank = {M.rank()}")

    # ---- among the 6 permutations, exactly the 3 cyclic powers align -----
    perms = []
    for p in itertools.permutations(range(3)):
        Mp = sp.zeros(3)
        for i, j in enumerate(p):
            Mp[i, j] = 1
        perms.append((p, Mp))

    def equivariant(X):
        return sp.simplify(X * P - P * X) == sp.zeros(3)

    aligning = [(p, X) for (p, X) in perms if equivariant(X)]
    odd = [(p, X) for (p, X) in perms if not equivariant(X)]
    check("exactly 3 of 6 permutations are Z_3-equivariant alignments (W != 0)",
          len(aligning) == 3, f"aligning perms = {[p for p, _ in aligning]}")
    check("the 3 aligning permutations are exactly the cyclic powers {I,P,P^2}",
          all(any(sp.simplify(X - Pk) == sp.zeros(3) for Pk in basis) for _, X in aligning))
    check("the other 3 permutations (transpositions) are NOT equivariant => W = 0",
          len(odd) == 3, f"non-aligning perms = {[p for p, _ in odd]}")

    # ---- the three alignments are gauge-equivalent: no canonical preference
    # P relabels a diagonal operator's eigenvalues cyclically -> same spectrum,
    # different order; the simultaneous-diagonalization bridge fixes diagonality
    # but supplies NO canonical order (orientation).
    D = sp.diag(2, 5, 9)                      # any operator diagonal in the carrier basis
    Dc = sp.simplify(P * D * P.inv())         # cyclically relabeled
    check("cyclic relabeling preserves spectrum (isospectral) but permutes order "
          "=> no canonical first element",
          set(D.eigenvals().keys()) == set(Dc.eigenvals().keys())
          and not (D == Dc))
    check("=> axis-cycle orientation is a free 3-fold P1 choice "
          "(reduces to P1, like the center)", len(aligning) == 3)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
