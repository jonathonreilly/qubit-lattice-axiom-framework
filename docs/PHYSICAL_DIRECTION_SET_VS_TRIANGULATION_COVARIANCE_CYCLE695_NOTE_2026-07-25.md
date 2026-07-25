# Direction-set covariance and triangulation covariance are different invariants — Cycle 695

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_direction_set_vs_triangulation_covariance_cycle695_2026_07_25.py`
(6 PASS / 0 FAIL, exit 0, exact integer arithmetic).

## Why this exists

[Proper-cubic covariance ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md)
bounds **triangulation** invariance: no eight-vertex unit-cube triangulation is
invariant under all 24 proper cubic rotations, the maximum is exactly 12
(five-tetrahedron), and the Kuhn/Freudenthal complex attains 6.

A real-space Regge construction does not always mediate its covariance through
the triangulation. It may mediate it through the **edge direction set** — asking
which frames carry every spatial direction class back into the set, up to a
global sign. That is a **different invariant**, and this cycle shows the two come
apart.

## Result

| object | invariant | value |
|---|---|---|
| 0/1 direction set (Kuhn edges) | oriented stabilizer | 3 |
| 0/1 direction set (Kuhn edges) | signed scope | **6** |
| Kuhn six-tetrahedron complex | cube-centred stabilizer | **6** |
| five-tetrahedron edge directions | signed scope | **24** |
| five-tetrahedron complex | cube-centred stabilizer | **12** |

**For the Kuhn complex the two invariants coincide at 6.** That coincidence is a
property of that complex, not an entailment — and it is exactly why a
construction reporting "6 of 24" can appear to be quoting the triangulation
ceiling when it is really quoting its direction set.

**For the five-tetrahedron complex they diverge by a factor of two.** Its
edge-direction set is closed under all 24 rotations while the triangulation it
belongs to is invariant under only 12.

**Neither invariant bounds the other.** The five-tetrahedron case exhibits a
direction-set scope (24) strictly greater than the Cycle-690 triangulation
ceiling (12).

## Consequence

Cycle 690's ceiling of 12 bounds **triangulation invariance**. It does **not**
bound a construction whose covariance is mediated by the edge direction set.

Two specific misreadings are blocked:

1. Reading the 12 as a universal ceiling for real-space Regge covariance. It is
   not; a direction-set-mediated construction is not bounded by it.
2. Citing Cycle 690 as the *licence* for a measured direction-set scope of 6.
   For the Kuhn complex those numbers coincide, so the citation looks right and
   is not — the theorem's stabilizer computation is about a different object.

This does not assert that any construction achieves 24. It asserts only that the
12-ceiling does not forbid it, and that the two invariants must be quoted
separately.

## Firewalls

- No physics is added: this compares two group-theoretic invariants of declared
  finite fixtures.
- No gravity, metric, dynamics, or observable claim is made.
- No axiom or primitive is proposed or adopted.

## Scope for independent review

Two declared complexes on the eight cube vertices, exact integer arithmetic,
full 24-frame enumeration with 576-product closure verified. Other complexes,
larger cells, improper rotations, and lattice-site (as opposed to cube-centred)
rotation centres are outside scope and untested. The N1–N8 verdict remains
reviewer-owned.

## Dependency citations

Self-contained; imports nothing from the repository. It cites
[Proper-cubic covariance ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md)
for the triangulation ceiling it reproduces and delimits.
