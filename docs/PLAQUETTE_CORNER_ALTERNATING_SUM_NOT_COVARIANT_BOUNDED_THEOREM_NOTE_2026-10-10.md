---
claim_id: plaquette_corner_alternating_sum_not_covariant_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On one unit square, each corner takes a value in {0, 1, blank}. The alternating sum of the four values in boundary order, with blank counted as 0, is not covariant for the boundary-sign character of the eight corner-preserving proper isometries. The reversal x -> (y, x, -z) fixes the coloring 0101 and has character -1, while the sum there is -2 rather than +2. No coefficients on 001b, 011b, and 01bb are assigned. The sum is not a flux. No site and no rate are supplied."
upstream_dependencies:
  - minimal_axioms
  - plaquette_corner_circulation_not_forced_bounded_theorem_note_2026-10-10
runner: scripts/plaquette_corner_alternating_sum_not_covariant_2026_10_10.py
---

# The alternating corner sum is not a covariant circulation

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/plaquette_corner_alternating_sum_not_covariant_2026_10_10.py`](../scripts/plaquette_corner_alternating_sum_not_covariant_2026_10_10.py)

**Carrier.** The object is the same unit square as the
[circulation census](PLAQUETTE_CORNER_CIRCULATION_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-10.md),
with corners

```text
(0,0,0), (1,0,0), (1,1,0), (0,1,0)
```

in boundary order and with each corner in `{0, 1, blank}`. That census
defines the circulation character. It does not evaluate this sum. This
note evaluates one assignment and does not rerun the orbit table.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply translations and
proper cubic rotations. They do not say how a rotation moves a
possibility. This note moves the record with the corner. A blank is a
color. Inside this one sum, blank contributes the integer `0`. That
numeric map does not add a fourth color. The note does not choose a
formation site, and it does not define a rate.

Reading note (2) of the minimal axioms still says the distribution does
not supply the formation site, probability, or rate. The open-gate list
still names "source/action and physical-observable identification." This
evaluation does not close either sentence.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One alternating sum of the four corner values fails the boundary-sign identity on a named isometry and a named coloring."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The alternating corner sum is not covariant for the character already defined. No coefficients are assigned. The sum is not adopted as a flux."
conditional_surface_status: "alphabet {0, 1, blank} on four corners; blank contributes 0 only inside this sum; character is the boundary sign already defined"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

A coloring is a 4-tuple in boundary order. Write blank as `b`. The proper
cubic group is the 24 signed permutation matrices of determinant `1`. An
isometry is `x ↦ Rx + b` with `R` in that group and `b` in `Z^3`. Exactly
eight preserve the corner set. Their corner permutations are the four
cyclic shifts of `(0,1,2,3)` and the four cyclic shifts of `(0,3,2,1)`.
The circulation character `χ` is `+1` on the first four and `-1` on the
second four. It is the same homomorphism as in the circulation census.
This note recomputes those eight maps. It does not import the orbit count.

The assignment is

```text
φ(c) = n(c0) - n(c1) + n(c2) - n(c3)
```

where `n(0) = 0`, `n(1) = 1`, and `n(b) = 0`. It is covariant when
`φ(g·c) = χ(g) φ(c)` for every one of the eight isometries and every
coloring. The color moves with the corner. No edge variable is defined.
`φ` is not called a flux.

## Theorem 1 — one reversal and one coloring

**Conclusion.** The isometry `x ↦ Rx` with

```text
R = [[0, 1, 0], [1, 0, 0], [0, 0, -1]]
```

and shift `0` is one of the eight. It is the proper rotation
`(x, y, z) ↦ (y, x, -z)`, a half-turn about the diagonal through
`(0,0,0)` and `(1,1,0)`, not an improper reflection. It fixes those two
corners and swaps `(1,0,0)` with `(0,1,0)`. The induced permutation is
`(0, 3, 2, 1)`, and `χ = -1`.

This isometry fixes the coloring `0101`. That coloring has no blank. Its
alternating sum is `0 - 1 + 0 - 1 = -2`. The character identity requires
`+2`. Therefore `φ` is not covariant.

The same isometry fixes 27 colorings. The alternating sum is `0` on 9 of
them and nonzero on the other 18. Each of those 18 fails the character
identity. `0101` is the named witness among them.

The sign of this corner permutation is also `-1`, because the permutation
is the transposition of the two swapped corners. On `0101` the alternating
sum is unchanged, so replacing `χ` by that permutation sign does not
repair the witness. That sign is not adopted as a second character.

## Theorem 2 — no coefficients, and the sum is not a flux

**Conclusion.** An integer coefficient triple on `001b`, `011b`, and
`01bb` is defined for a covariant assignment, by evaluating it on those
representatives. This `φ` is not covariant. No such triple is assigned,
and the three values of `φ` on those representatives are not reported as
coefficients.

The identity isometry preserves `φ` on all 81 colorings. Across the eight
isometries, the character identity fails on 192 pairs. The named pair is
one of them. A second pair is recorded and is not the named witness: the
quarter turn

```text
R = [[0, -1, 0], [1, 0, 0], [0, 0, 1]],    b = (1, 0, 0)
```

has permutation `(1, 2, 3, 0)` and `χ = +1`. It sends `1000` to a coloring
whose alternating sum is `-1`, not `+1`.

The value `0` occurs, and so does a nonzero value, so `φ` is neither the
zero assignment nor an empty function. No coefficient is selected.
Calling `φ` a flux is not part of the theorem. No corner entry is
identified with a mass density.

## What this does not say

- It does not assign the integers by which `φ` meets `001b`, `011b`, or
  `01bb`, and it does not adopt any element of the rank-3 module.
- It does not classify every integer weight vector on the four corners.
  One alternating pattern is not a census of those weights.
- It does not adopt the sign of the corner permutation as the circulation
  character. The named witness fails that sign as well.
- It does not form an edge variable. The sum is a function of the four
  corner records only.
- It does not enlarge the alphabet. Blank remains a color and contributes
  `0` only inside this sum.
- It does not delete blank corners before the action. The witness `0101`
  has no blank, so the failure is not an artifact of that count.
- It does not rerun the 21-orbit census, a six-neighbor shell census, a
  bond factor, a cap pencil, or a CHSH square.
- It does not choose the square, and it does not define a formation rate.

## No-Go Discipline Gate

Scoped claim: the alternating sum of the four corner values in boundary
order, with blank counted as `0`, is not covariant for the boundary-sign
character. No coefficient triple is assigned. The sum is not a flux.

N1. Five attacks on that scoped claim:

1. Let boundary order make the alternating sum covariant. The named
   reversal has `χ = -1` and fixes `0101`, where the sum is `-2`, not
   `+2`. `ATTEMPTED`.
2. Let the blank-to-zero convention be the only cause. The coloring
   `0101` uses no blank, and the sum there is still `-2`. `ATTEMPTED`.
3. Let the sum vanish on every coloring fixed by this reversal. It is
   nonzero on 18 of the 27 fixed colorings. `ATTEMPTED`.
4. Let the sign of the corner permutation repair the witness. That sign
   is `-1` on this reversal, and the sum is unchanged. `ATTEMPTED`.
5. Let the quarter turn preserve the sum because its character is `+1`.
   It sends the sum of `1000` from `1` to `-1`. `ATTEMPTED`.

N2. Only this integer assignment and the character already defined are
used. No second output action is stated.

N3. The alphabet `{0, 1, blank}`, the numeric map that sends blank to `0`,
and the character `χ` are written as hypotheses. No dynamics clause is
used. The three approved primitives `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive` are not
inputs.

N4. The rank-3 census, the ring-model plaquette-circulation matrix, and
the shell censuses are different carriers. Dropping their counts leaves
Theorems 1 and 2 intact: the eight isometries and the value `-2` are
recomputed here. No count in those notes is used as a mass or as a flux.

N5. The negative sentence is about one square and one assignment. The
runner evaluates that assignment on the 81 colorings and the eight
isometries. It does not resolve a second square as an independent
variable.

N6. This note does not say that a new axiom is required. It does not
select a coefficient. Source/action remains an open gate. The formation
rule remains downstream supplier content.

N7. Steelman, outside this menu: delete blank corners before reading the
sum, or call the sum an edge flux, or treat another weight vector as
already decided. None of those is executed. The odd cap alphabet stays
stopped. The shell censuses are not reopened. Other weight vectors stay
unclassified.

N8. This note does not reopen the 81-coloring orbit table, the free-orbit
names as a module basis, the 729-shell census, the one-blank census, the
binary-shell census, the CHSH squares, the quadratic channels, the
achiral-orbit factor, the linear factor `1 + kappa F`, the quadratic
pencil, or the shifted cap factor.

## Review record

The open question was whether this one alternating sum is covariant for
the character already defined, and, if so, what its three integer
coefficients are. It is not covariant. The witness is the half-turn
`(x, y, z) ↦ (y, x, -z)` and the coloring `0101`. No coefficients are
assigned. The sum is not a flux. The miss is real.

Outstanding at landing: other integer weight vectors on the four corners
are not classified; no edge variable is formed; a menu that deletes
blanks is outside; the site and the rate stay unsupplied; independent
audit has not reviewed this note. No helper runner is declared.

The witness value `-2` and the fixed counts `27` and `18` were fixed by
hand before the runner's expected comparisons. The scan total `192` was
read from a first execution of this same comparison and then locked; it
is not a second counting method. The author re-ran two load-bearing
mutations on scratch copies; each printed `FAIL=1`, and the copies were
not kept.

- Demanding that the image value on `0101` equal the required value `+2`
  fails one check.
- Demanding that the number of failing pairs be `0` fails one check.

## Runner

`scripts/plaquette_corner_alternating_sum_not_covariant_2026_10_10.py`
builds the 24 proper rotations and the isometries `Rx + b` that preserve
the four corners. It checks the named reversal and the named quarter
turn, the boundary-sign homomorphism, the value `-2` on `0101`, the `27`
fixed colorings and the `18` nonzero values, the corner-permutation sign
of the reversal, the quarter-turn image of `1000`, the blank-to-zero map,
and the `192` failing pairs. It emits no coefficient triple. It reads no
external scientific input. The cached result is `TOTAL: PASS=8 FAIL=0`.
