# Z3 Character-Isomorphism Weyl Axis-Cycle Orientation Open Gate

**Date:** 2026-05-30
**Claim type:** open_gate
**Status:** source note; downstream status is decided by independent review.
**Primary runner:** [`scripts/frontier_z3_character_isomorphism_weyl_axis_cycle_orientation_open_gate.py`](../scripts/frontier_z3_character_isomorphism_weyl_axis_cycle_orientation_open_gate.py)

## Result

The parent
[`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md`](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md)
showed that the `SU(3)_c` center action has the wrong character for a regular
three-label bridge.  The surviving tempting route is the order-three cubic
axis cycle, represented on the three coordinate axes by

```text
P = [[0, 0, 1],
     [1, 0, 0],
     [0, 1, 0]].
```

The runner verifies the useful positive fact: this axis-cycle representation
has regular `Z3` character `(3, 0, 0)`.  It also verifies the unresolved
orientation fact: among permutation alignments, exactly the three cyclic powers
`{I, P, P^2}` commute with the axis cycle.  They are related by cyclic
relabeling, so the finite character calculation supplies no distinguished
first element of that orbit.

Thus the axis-cycle route remains an open gate.  It can match the regular
character, but the finite algebra checked here does not canonically choose a
within-sector species ordering.

## Verified Local Facts

1. `P^3 = I`, `det(P) = 1`, and the character of the axis-cycle
   representation is `(3, 0, 0)`.
2. The center action on the color fundamental has character
   `(3, 3 omega, 3 omega^2)`, so it is not the regular representation.
3. Every `W = a0 I + a1 P + a2 P^2` commutes with `P`, and the span
   `{I, P, P^2}` is three-dimensional.
4. Among the six permutation matrices on three labels, exactly the three
   cyclic powers `{I, P, P^2}` commute with `P`; the three transpositions do
   not.
5. Cyclic relabeling maps a diagonal carrier operator to an isospectral operator
   with permuted order.  Diagonality alone therefore does not select one cyclic
   alignment as first.

## Boundary

This note is not a formal no-go over all possible color/generation bridges.  It
does not derive a charged-lepton, Koide, or Yukawa closure, and it does not
approve a new axiom, primitive, or Tier-A admission.

The exact boundary is narrower:

```text
axis-cycle regular character: verified;
canonical within-sector orientation from that finite character calculation: open.
```

A future source could close this gate by deriving a non-stipulated ordering of
the three cyclic alignments from accepted framework content.  This note only
shows that the regular character and simultaneous diagonal form, by themselves,
do not provide that ordering.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_z3_character_isomorphism_weyl_axis_cycle_orientation_open_gate.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: Weyl axis-cycle character/orientation open-gate checks pass.
```
