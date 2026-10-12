---
claim_id: plaquette_corner_weight_covariance_only_zero_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On one unit square, each corner takes a value in {0, 1, blank}. For an integer weight vector (w0, w1, w2, w3), the weighted corner sum, with blank counted as 0, is covariant for the boundary-sign character if and only if the weight is 0. The solution module is {0} and its basis is empty. The zero weight is not a flux. No site and no rate are supplied."
upstream_dependencies:
  - minimal_axioms
  - plaquette_corner_circulation_not_forced_bounded_theorem_note_2026-10-10
  - plaquette_corner_alternating_sum_not_covariant_bounded_theorem_note_2026-10-10
runner: scripts/plaquette_corner_weight_covariance_only_zero_2026_10_10.py
---

# Integer corner weights meet the boundary sign only at zero

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/plaquette_corner_weight_covariance_only_zero_2026_10_10.py`](../scripts/plaquette_corner_weight_covariance_only_zero_2026_10_10.py)

**Carrier.** The object is the same unit square as the
[circulation census](PLAQUETTE_CORNER_CIRCULATION_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-10.md),
with corners

```text
(0,0,0), (1,0,0), (1,1,0), (0,1,0)
```

in boundary order and with each corner in `{0, 1, blank}`. That census
defines the circulation character and does not weigh the corners. The
[alternating-sum note](PLAQUETTE_CORNER_ALTERNATING_SUM_NOT_COVARIANT_BOUNDED_THEOREM_NOTE_2026-10-10.md)
rejects one weight and does not classify the others. This note classifies
every integer weight. It does not rerun the orbit table, and it does not
use the value of that one rejected sum.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply translations and
proper cubic rotations. They do not say how a rotation moves a
possibility. This note moves the record with the corner. A blank is a
color. Inside this family of sums, blank contributes the integer `0`.
That numeric map does not add a fourth color. The note does not choose a
formation site, and it does not define a rate.

Reading note (2) of the minimal axioms still says the distribution does
not supply the formation site, probability, or rate. The open-gate list
still names "source/action and physical-observable identification." This
classification does not close either sentence.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The integer kernel of the weighted corner sums is the zero module for the boundary-sign character."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Every integer corner weight that is covariant for the character already defined is the zero weight. The zero weight is not adopted as a flux."
conditional_surface_status: "alphabet {0, 1, blank} on four corners; blank contributes 0 only inside the weighted sum; character is the boundary sign already defined"
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

For `w = (w0, w1, w2, w3)` in `Z^4`, the weighted corner sum is

```text
φ_w(c) = w0 n(c0) + w1 n(c1) + w2 n(c2) + w3 n(c3)
```

where `n(0) = 0`, `n(1) = 1`, and `n(b) = 0`. It is covariant when
`φ_w(g·c) = χ(g) φ_w(c)` for every one of the eight isometries and every
coloring. The color moves with the corner. If `π` sends corner `i` to
corner `π(i)`, the color at `i` arrives at `π(i)`. No edge variable is
defined. `φ_w` is not called a flux.

The numeric patterns `(n(c0), n(c1), n(c2), n(c3))` are exactly the
16 tuples in `{0,1}^4`. Blank and `0` contribute the same integer, so
blank does not add a pattern. Both sides of the character identity are
linear in that pattern. Evaluating on the four colorings with a single
`1` shows that covariance is equivalent to the 32 equations

```text
w_{π(i)} = χ(π) w_i
```

one for each of the eight permutations and each corner `i`. In row form,
the equation for `(π, i)` is the vector `e_{π(i)} - χ(π) e_i`.

## Theorem 1 — the relation lattice

**Conclusion.** Let `E` be the set of vectors in `Z^4` whose four
coordinates sum to an even integer. It is the kernel of the sum modulo
`2`, so it has index `2`.

Every covariance row has coordinate sum `1 - χ(π)`. That sum is `0` when
`χ(π) = 1` and `2` when `χ(π) = -1`. Every row therefore lies in `E`.

Four of the rows are these:

- the quarter turn `π = (1,2,3,0)`, `χ = +1`, at corner `0`, gives
  `R1 = (-1, 1, 0, 0)`
- the half turn `π = (2,3,0,1)`, `χ = +1`, at corner `0`, gives
  `R2 = (-1, 0, 1, 0)`
- the three-quarter turn `π = (3,0,1,2)`, `χ = +1`, at corner `0`, gives
  `R3 = (-1, 0, 0, 1)`
- the half turn about the other diagonal, `π = (2,1,0,3)`, `χ = -1`, at
  corner `3`, gives `R4 = (0, 0, 0, 2)`

The quarter turn is `x ↦ Rx + (1,0,0)` with

```text
R = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
```

The half turn is `x ↦ Rx + (1,1,0)` with `R = diag(-1,-1,1)`. The
three-quarter turn is `x ↦ Rx + (0,1,0)` with

```text
R = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
```

The other diagonal half turn is `x ↦ Rx + (1,1,0)` with

```text
R = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]
```

It fixes `(1,0,0)` and `(0,1,0)` and swaps `(0,0,0)` with `(1,1,0)`. Its
linear part has determinant `1`, and the affine map has order `2`.

Replace `R2` by `R2 - R1` and `R3` by `R3 - R1`, then replace the new
`R3` by that vector minus the new `R2`. The four rows become

```text
(-1, 1, 0, 0)
( 0,-1, 1, 0)
( 0, 0,-1, 1)
( 0, 0, 0, 2)
```

Adding one row to another does not change the determinant, and there is
no row swap. The determinant is `(-1)(-1)(-1)(2) = -2`.

The same four rows generate `E`. If `(a,b,c,d)` has even coordinate sum,
the integers

```text
x1 = b
x2 = c
x3 = -a - b - c
x4 = (a + b + c + d) / 2
```

satisfy `x1 R1 + x2 R2 + x3 R3 + x4 R4 = (a,b,c,d)`. Thus every
covariance row, already known to lie in `E`, is an integer combination of
`R1` through `R4`. The odd vector `(1,0,0,0)` is not in `E`, and the
same formula does not divide it by `2`. No covariance equation cuts `E`
down further. The relation lattice is exactly `E`, a sublattice of index
`2`, not a rank-3 lattice and not all of `Z^4`.

## Theorem 2 — the only solution is zero

**Conclusion.** The original four rows and the triangular rows have the
same integer solutions, because each row operation is reversed by adding
the row back. The triangular system is

```text
-w0 + w1 = 0
-w1 + w2 = 0
-w2 + w3 = 0
2 w3 = 0
```

The last equation says `2 w3 = 0`. For every integer `n`, the quotient
`(2n)/2` is `n`, so `w3 = (2 w3)/2 = 0`. Then `w2 = w3 = 0`, `w1 = w2 = 0`,
and `w0 = w1 = 0`. The only integer solution of the four rows is
`(0,0,0,0)`. Every other covariance equation is an integer combination of
those rows, so it gives the same solution set. The zero weight satisfies
every character identity, because both sides are `0`.

A `Z`-basis of the solution module is the empty family. The index `2` of
`E` is the missing odd-sum equations. It is not a second integer weight.
`Z` has no element of order `2`.

One nonzero vector is recorded so the sign obstruction is visible, and it
is not used as a search. The constant weight `(1,1,1,1)` counts the
corners whose color is `1`. On the coloring `1000` the count is `1`. The
other diagonal half turn sends `1000` to `0010`, where the count is also
`1`. The character is `-1`, so covariance would require `-1`. The constant
weight is not a solution. The same conclusion already follows from
Theorem 2, since the vector is not zero.

The zero weight is not adopted as a flux. No corner entry is identified
with a mass density. No coefficient of any larger module is selected.

## What this does not say

- It does not adopt the zero weight as a circulation, a flux, or a mass
  density.
- It does not say that every integer function of the four colors fails
  the character. A function that separates blank from `0` is outside this
  family. The rank-3 module is not recomputed and not adopted.
- It does not assign a separate integer to blank. Blank contributes `0`
  only inside this family.
- It does not enlarge the alphabet, and it does not delete blank corners
  before the sum.
- It does not form an edge variable. The sum is a function of the four
  corner records only.
- It does not rerun the 21-orbit census, the alternating-sum witness, a
  six-neighbor shell census, a bond factor, a cap pencil, or a CHSH
  square.
- It does not choose the square, and it does not define a formation rate.

## No-Go Discipline Gate

Scoped claim: the weighted corner sum with blank counted as `0` is
covariant for the boundary-sign character exactly at the zero weight. The
solution module is `{0}`. Its basis is empty. The zero weight is not a
flux.

N1. Five attacks on that scoped claim:

1. Let a constant weight survive because every corner permutation
   preserves the count of ones. The other diagonal half turn has
   character `-1` and sends the count on `1000` from `1` to `1`.
   `ATTEMPTED`.
2. Let the index-`2` relation lattice leave a nonzero integer solution.
   The triangular pivot `2` divides `0`, and the only quotient is `0`.
   `ATTEMPTED`.
3. Let blank, rather than `0`, create another numeric pattern and another
   solution. Both contribute `0`, and the 16 patterns are exactly
   `{0,1}^4`. `ATTEMPTED`.
4. Let some other covariance row cut the kernel below what the four rows
   allow. Every covariance row is an integer combination of those four.
   `ATTEMPTED`.
5. Let the zero weight be a selected flux because it is the only
   solution. The theorem does not adopt it. `ATTEMPTED`.

N2. Only this four-integer family and the character already defined are
used. No second output action is stated.

N3. The alphabet `{0, 1, blank}`, the numeric map that sends blank to `0`,
and the character `χ` are written as hypotheses. No dynamics clause is
used. The three approved primitives `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive` are not
inputs.

N4. The rank-3 census and the alternating-sum witness are different
carriers. Dropping their counts leaves Theorems 1 and 2 intact: the eight
isometries, the determinant `-2`, and the quotient `0` are recomputed
here. No count in those notes is used as a mass or as a flux.

N5. The negative sentence is about one square and one four-integer
family. The runner evaluates the 32 equations, the determinant, and the
division. It does not resolve a second square as an independent variable.

N6. This note does not say that a new axiom is required. It does not
select a coefficient. Source/action remains an open gate. The formation
rule remains downstream supplier content.

N7. Steelman, outside this menu: give blank an integer other than `0`,
or delete blank corners before the sum, or call the zero weight an edge
flux. None of those is executed. The odd cap alphabet stays stopped. The
shell censuses are not reopened.

N8. This note does not reopen the 81-coloring orbit table, the free-orbit
names as a module basis, the alternating value on one coloring, the
729-shell census, the one-blank census, the binary-shell census, the
CHSH squares, the quadratic channels, the achiral-orbit factor, the
linear factor `1 + kappa F`, the quadratic pencil, or the shifted cap
factor.

## Review record

The open question was which integer vectors `(w0,w1,w2,w3)` make the
weighted corner sum covariant for the character already defined. The only
solution is `0`. A basis of the solution module is empty. The relation
lattice is the even-sum sublattice, of index `2` and determinant `-2`.
The zero weight is not a flux. The miss on `origin/main` is real: the
corner-weight hits there are other carriers.

Outstanding at landing: a numeric map that sends blank to an integer
other than `0` is not classified; no edge variable is formed; a menu
that deletes blanks is outside; the site and the rate stay unsupplied;
independent audit has not reviewed this note. No helper runner is
declared.

The four rows, the determinant `-2`, and the quotient `0` were fixed by
the elimination above before the runner's expected comparisons. The
author re-ran two load-bearing mutations on scratch copies; each printed
`FAIL=1`, and the copies were not kept.

- Demanding that the determinant be `1` fails one check.
- Demanding that the constant weight meet the required value `-1` fails
  one check.

## Runner

`scripts/plaquette_corner_weight_covariance_only_zero_2026_10_10.py`
builds the 24 proper rotations and the isometries `Rx + b` that preserve
the four corners. It checks the four named permutations and the
boundary-sign homomorphism, the 32 even-sum equations, the generation of
those equations by the four rows, the determinant `-2`, the reversible
triangular elimination, the quotient `0`, the zero weight on all 81
colorings, the constant weight on `1000`, and the blank-to-zero map. It
emits no flux. It reads no external scientific input. The cached result
is `TOTAL: PASS=6 FAIL=0`.
