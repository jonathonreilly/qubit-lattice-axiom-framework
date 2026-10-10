---
claim_id: plaquette_corner_symbol_pair_covariance_only_zero_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On one unit square, each corner takes a value in {0, 1, blank}. Color 0 contributes 0, color 1 contributes an integer u, and blank contributes an integer v, the same pair at every corner. That weighted sum is covariant for the boundary-sign character if and only if (u, v) = (0, 0). The solution module is {0} and its basis is empty. The zero pair is not a flux. No site and no rate are supplied. The corner-weight family stops."
upstream_dependencies:
  - minimal_axioms
  - plaquette_corner_circulation_not_forced_bounded_theorem_note_2026-10-10
  - plaquette_corner_weight_covariance_only_zero_bounded_theorem_note_2026-10-10
runner: scripts/plaquette_corner_symbol_pair_covariance_only_zero_2026_10_10.py
---

# One shared symbol weight meets the boundary sign only at zero

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/plaquette_corner_symbol_pair_covariance_only_zero_2026_10_10.py`](../scripts/plaquette_corner_symbol_pair_covariance_only_zero_2026_10_10.py)

**Carrier.** The object is the same unit square as the
[circulation census](PLAQUETTE_CORNER_CIRCULATION_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-10.md),
with corners

```text
(0,0,0), (1,0,0), (1,1,0), (0,1,0)
```

in boundary order and with each corner in `{0, 1, blank}`. That census
defines the circulation character and does not weigh colors. The
[per-corner weight note](PLAQUETTE_CORNER_WEIGHT_COVARIANCE_ONLY_ZERO_BOUNDED_THEOREM_NOTE_2026-10-10.md)
classifies weights that depend on the corner, with blank contributing `0`.
This note does not use that relation lattice. It asks a different question:
one integer for the color `1`, and one integer for blank, the same pair at
every corner. Color `0` contributes `0`. It does not rerun the orbit table,
and it does not divide the pivot `2`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply translations and
proper cubic rotations. They do not say how a rotation moves a
possibility. This note moves the record with the corner. A blank is a
color. It is not a fourth symbol, and the square is not given a fifth
corner. The note does not choose a formation site, and it does not define
a rate.

Reading note (2) of the minimal axioms still says the distribution does
not supply the formation site, probability, or rate. The open-gate list
still names "source/action and physical-observable identification." This
classification does not close either sentence.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The integer kernel of one shared color weight and one shared blank weight is the zero module for the boundary-sign character."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The only shared pair (u, v) covariant for the character already defined is (0, 0). The zero pair is not adopted as a flux. The corner-weight family stops."
conditional_surface_status: "alphabet {0, 1, blank} on four corners; color 0 contributes 0; color 1 contributes u; blank contributes v; the same pair at every corner; character is the boundary sign already defined"
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
This note recomputes those eight maps. It does not import the orbit count
or the even-sum lattice.

For `(u, v)` in `Z^2`, the weighted sum is

```text
φ(c) = u N_1(c) + v N_b(c)
```

where `N_1` is the number of corners colored `1` and `N_b` is the number
colored blank. Equivalently, color `0` contributes `0`, color `1`
contributes `u`, and blank contributes `v`, added once at each corner.
The pair does not depend on the corner. It is covariant when
`φ(g·c) = χ(g) φ(c)` for every one of the eight isometries and every
coloring. The color moves with the corner. If `π` sends corner `i` to
corner `π(i)`, the color at `i` arrives at `π(i)`. No edge variable is
defined. `φ` is not called a flux.

## Theorem 1 — the sum is a count

**Conclusion.** Every corner-preserving isometry permutes the four
corners. The induced map is a bijection of `{0,1,2,3}`. Therefore it
preserves the multiset of colors, and

```text
N_1(g·c) = N_1(c),    N_b(g·c) = N_b(c)
```

for every coloring. The same pair at every corner then gives
`φ(g·c) = φ(c)` for every `(u, v)`.

Moving a single `1` from one corner to another does not change the sum.
Moving a single blank does not change it either. On `1000`, `0100`,
`0010`, and `0001` the value of `(u, v) = (1, 0)` is `1`. On `b000`,
`0b00`, `00b0`, and `000b` the value of `(0, 1)` is `1`.

The character identity therefore has residual

```text
φ(g·c) - χ(g) φ(c) = (1 - χ(g)) φ(c).
```

Both sides are linear in `(u, v)`. It is enough to check the identity on
the pairs `(1, 0)` and `(0, 1)`; it then holds for every integer
combination. The runner checks those two pairs on all `81` colorings and
all eight permutations.

When `χ(g) = +1`, the residual is `0` for every coloring and every pair.
An orientation-preserving isometry contributes only the zero equation in
`Z^2`.

## Theorem 2 — the only solution is zero

**Conclusion.** The solution module is `{0}`. A `Z`-basis is the empty
family. The relation lattice, meaning the lattice generated by the
covariance rows in `Z^2`, is all of `Z^2`. It has index `1` and
determinant `1`.

The other diagonal half turn is `x ↦ Rx + (1,1,0)` with

```text
R = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]
```

Its corner permutation is `(2,1,0,3)` and its character is `-1`. It fixes
`(1,0,0)` and `(0,1,0)` and swaps `(0,0,0)` with `(1,1,0)`. For this
isometry the residual is `2 φ(c)`. Covariance forces `φ(c) = 0` for every
coloring, because `Z` has no element of order `2`.

The coloring `1000` has `N_1 = 1` and `N_b = 0`, so `φ = u`. The coloring
`b000` has `N_1 = 0` and `N_b = 1`, so `φ = v`. The two equations are

```text
(1, 0)
(0, 1)
```

Their determinant is `1`. Exact division of each pivot `1` against
right-hand side `0` returns the quotient `0`. The only integer solution
is `(u, v) = (0, 0)`.

Every count row is the combination `(N_1, N_b) = N_1 (1, 0) + N_b (0, 1)`.
The four reversing isometries therefore contribute only rows inside this
lattice, and the four preserving isometries contribute the zero row. The
two unit rows generate every covariance equation. The index is `1`, not
a second integer solution.

The four-blank coloring has row `(0, 4) = 4 (0, 1)`. The pivot `4` divides
`0`, and the quotient is `0`. It does not divide `1`, so that row is not
a separate congruence class. It does not leave a nonzero `v`.

The zero pair satisfies every character identity, because both sides are
`0`. A `Z`-basis of `{0}` is empty. The zero pair is not adopted as a
flux.

Two nonzero pairs are recorded so the obstruction is visible, and neither
is used as a search. The pair `(1, 0)` on `1000` has value `1`. The other
diagonal sends `1000` to `0010`, where the value is also `1`. The
character requires `-1`. The pair `(0, 1)` on `b000` has value `1` and
sends that coloring to `00b0`, where the value is also `1` rather than
`-1`. The pair `(1, -1)` vanishes on `1b00`, where one color `1` cancels
one blank, and still fails on `1000`. A cancellation on one mixed
coloring is not a solution.

No corner entry is identified with a mass density. No coefficient of any
larger module is selected. This is the last pair in the corner-weight
family. A third color, a fifth corner, a weight that depends on the
corner again, and a menu that deletes blank corners are not opened.

## What this does not say

- It does not adopt `(0, 0)` as a circulation, a flux, or a mass density.
- It does not say that every integer function of the four colors fails
  the character. A weight that depends on the corner is a different
  family, already classified only when blank contributes `0`. The rank-3
  module is not recomputed and not adopted.
- It does not use the even-sum sublattice, the determinant `-2`, or the
  four named rows of that family.
- It does not add a third color, and it does not add a fifth corner.
- It does not delete blank corners before the sum.
- It does not form an edge variable. The sum is a function of the four
  corner records only.
- It does not rerun the 21-orbit census, the alternating-sum witness, a
  six-neighbor shell census, a bond factor, a cap pencil, or a CHSH
  square.
- It does not choose the square, and it does not define a formation rate.
- The corner-weight family stops after this pair.

## No-Go Discipline Gate

Scoped claim: the weighted sum with color `0` contributing `0`, color `1`
contributing `u`, and blank contributing `v`, the same pair at every
corner, is covariant for the boundary-sign character exactly at
`(u, v) = (0, 0)`. The solution module is `{0}`. Its basis is empty. The
zero pair is not a flux. The corner-weight family stops.

N1. Five attacks on that scoped claim:

1. Let a nonzero pair survive because every corner permutation preserves
   the counts. The other diagonal half turn has character `-1` and sends
   the value of `(1, 0)` on `1000` from `1` to `1`. `ATTEMPTED`.
2. Let the four-blank row `(0, 4)` leave a nonzero blank weight. The
   pivot `4` divides `0`, and the only quotient is `0`. `ATTEMPTED`.
3. Let `(1, -1)` survive because it vanishes on `1b00`. The same pair has
   value `1` on `1000`, and the reversal requires `-1`. `ATTEMPTED`.
4. Let an orientation-preserving isometry cut the kernel further, or let
   a reversing isometry add a row outside the unit lattice. Preserving
   elements contribute the zero row. Every reversing row is an integer
   combination of `(1, 0)` and `(0, 1)`. `ATTEMPTED`.
5. Let the zero pair be a selected flux because it is the only solution.
   The theorem does not adopt it. `ATTEMPTED`.

N2. Only this two-integer family and the character already defined are
used. No second output action is stated.

N3. The alphabet `{0, 1, blank}`, the shared contributions of color `0`,
color `1`, and blank, and the character `χ` are written as hypotheses. No
dynamics clause is used. The three approved primitives
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive` are not inputs.

N4. The per-corner weight note, the rank-3 census, and the alternating-sum
witness are different carriers. Dropping their counts leaves Theorems 1
and 2 intact: the eight isometries, the count invariance, the determinant
`1`, and the quotient `0` are recomputed here. No count in those notes is
used as a mass or as a flux. The even-sum lattice is not an input.

N5. The negative sentence is about one square and one two-integer family.
The runner evaluates the eight permutations, the `81` colorings, the two
unit rows, and the division. It does not resolve a second square as an
independent variable.

N6. This note does not say that a new axiom is required. It does not
select a coefficient. Source/action remains an open gate. The formation
rule remains downstream supplier content.

N7. Steelman, outside this menu: give the two weights different values at
different corners, add a third color, add a fifth corner, or delete blank
corners before the sum, or call the zero pair an edge flux. None of those
is executed. The corner-weight family stops. The odd cap alphabet stays
stopped. The shell censuses are not reopened.

N8. This note does not reopen the per-corner four-weight elimination, the
81-coloring orbit table, the alternating value on one coloring, the
729-shell census, the one-blank census, the binary-shell census, the
CHSH squares, the quadratic channels, the achiral-orbit factor, the
linear factor `1 + kappa F`, the quadratic pencil, or the shifted cap
factor.

## Review record

The open question was which pairs `(u, v)` make the shared symbol sum
covariant for the character already defined. The only solution is
`(0, 0)`. A basis of the solution module is empty. The relation lattice
is all of `Z^2`, of index `1` and determinant `1`. The zero pair is not a
flux. The miss on `origin/main` is real: the hits that mention a blank
corner or color `1` are other carriers. The corner-weight family stops
after this pair.

Outstanding at landing: no edge variable is formed; a menu that deletes
blanks is outside and is not queued; a third color and a fifth corner are
not opened; the site and the rate stay unsupplied; independent audit has
not reviewed this note. No helper runner is declared.

The two unit rows, the determinant `1`, and the quotient `0` were fixed
by the elimination above before the runner's expected comparisons. The
author re-ran two load-bearing mutations on scratch copies; each printed
`FAIL=1`, and the copies were not kept.

- Demanding that the determinant be `2` fails one check.
- Demanding that `(1, 0)` on the image of `1000` meet the required value
  `-1` fails one check.

## Runner

`scripts/plaquette_corner_symbol_pair_covariance_only_zero_2026_10_10.py`
builds the 24 proper rotations and the isometries `Rx + b` that preserve
the four corners. It checks the boundary-sign homomorphism, the count
invariance of the shared pair, the residual `(1 - χ) φ`, the two unit
rows and their determinant `1`, the generation of every covariance
equation, the quotient `0` of the unit pivots and of the dependent pivot
`4`, the zero pair on all `81` colorings, the failures of `(1, 0)` and
`(0, 1)` on the named reversal, and the failure of `(1, -1)` on `1000`
after it vanishes on `1b00`. It emits no flux. It reads no external
scientific input. The cached result is `TOTAL: PASS=6 FAIL=0`.
