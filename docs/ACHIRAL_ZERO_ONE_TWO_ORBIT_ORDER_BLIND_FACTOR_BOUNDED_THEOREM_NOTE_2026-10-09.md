---
claim_id: achiral_zero_one_two_orbit_order_blind_factor_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Conditional on the formation reading and the soldered product form already used for finite alphabets. The proper cubic orbit of (0, 1, 2) has 24 points and equals its full signed-permutation orbit, so it is not a chiral pair. The transverse-sign factor of (1, 2, 3) is identically 0 on it. The axis-role sign below defines a bond product that is normalised, bond-symmetric, soldered-covariant, and fixed by diag(1, 1, -1). At kappa = 1/2 the 3-site path is order-blind, the ends are independent, and the adjacent correlation is 1/72. No physical rule is selected. The bond correlation matrix is not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/achiral_zero_one_two_orbit_order_blind_factor_2026_10_09.py
---

# An achiral 24-point record alphabet still carries an order-blind factor

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/achiral_zero_one_two_orbit_order_blind_factor_2026_10_09.py`](../scripts/achiral_zero_one_two_orbit_order_blind_factor_2026_10_09.py)

**Parent sentence, not a lemma.** The order-blind note of 2026-09-22 exhibits
varying soldered rules on the proper orbit of `(1, 2, 3)`, on the chiral
union of that orbit with its mirror, and on the Haar sphere. Its boundary
sentence is:

> generic orbits beyond the exhibited rules, higher-rank bond spaces, and mixed alphabets are not classified.

The orbit of `(0, 1, 2)` is one such alphabet. Nothing below imports that
note's path masses, its transverse-sign identities, or its constancy proof
on the orbits of sizes 6, 8, and 12. The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply proper cubic rotations.
Their open-gate list still places source/action outside the axioms. This
note does not close that gate, and it does not supply a formation site,
probability, or rate.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact orbit count and an explicit bond product on one finite alphabet, checked by rational enumeration."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "This alphabet is achiral and the factor is mirror-fixed. Higher-rank spaces and the other 24-point orbits stay unclassified. Formation site, probability, and rate stay unsupplied."
conditional_surface_status: "soldered product rules on the proper cubic orbit of (0, 1, 2), with one supplied kappa"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

The formation reading says a nearest-neighbour rule assigns a distribution
to each partial map from the six axis directions to already formed
neighbour values. Soldered covariance rotates positions and values
together. A product factor has the shape

```text
phi_d(a, b) = 1 + kappa X_d(a) X_{-d}(b),
```

and the one-site law is uniform on a finite alphabet. These are supplied
mathematical hypotheses. They are not the admissibility distribution, and
`X` is not a mass density. The `3×3` bond correlation used in the earlier
notes of this campaign does not appear.

## Theorem 1 — the orbit is achiral, and the old cap sign is zero

**Conclusion.** Let `O` be the `24` signed permutation matrices of
determinant `+1`, and let `A` be the orbit of `(0, 1, 2)`. Then `|A| = 24`,
and `A` is already closed under the `24` improper signed permutations. No
coordinate of a point of `A` is `±3`. On every cap `a·d = 2`, the product
of the two transverse coordinates is `0`.

**Proof.** A vector with entries `0, ±1, ±2`, each absolute value once, is
determined by the axis of the zero (`3` choices), the axis of the unit
entry (`2` remaining choices), and the signs of the two nonzero entries
(`4` choices). These `24` vectors are distinct. Signing the zero axis does
not create another vector, so this set is the full signed-permutation
orbit.

The diagonal matrix `s = diag(-1, 1, 1)` is improper and fixes
`(0, 1, 2)`. If an improper `g` sends `(0, 1, 2)` to `v`, then `g s` is
proper and sends `(0, 1, 2)` to the same `v`. Thus the proper orbit is the
whole set. It is not the union of two proper orbits.

On a cap `a·d = 2`, the entry along `d` is `+2` and the transverse entries
are `0` and `±1`. Their product is `0`. The transverse-sign factor used on
`(1, 2, 3)`, which reads that product on the cap `a·d = 3`, therefore has
no support on `A`.

## Theorem 2 — an axis-role sign gives a mirror-fixed bond product

**Conclusion.** For `a ∈ A`, let `i0`, `i1`, and `i2` be the axes of the
zero, the absolute value `1`, and the absolute value `2`. Let
`sgn(i0, i1, i2)` be the sign of that permutation of `(0, 1, 2)`, and set

```text
epsilon(a) = sgn(i0, i1, i2) (-1)^{i2}.
```

Let `d(a)` be the signed axis of the absolute value `2`, and set
`X_d(a) = epsilon(a)` if `d = d(a)` and `0` otherwise. Then each point lies
on exactly one cap, each cap has four points and sums to `0`, and the
positive-`z` cap changes sign under the quarter turn about `z`. At
`kappa = 1/2` every bond factor lies in `{1/2, 1, 3/2}`. The product is
bond-symmetric and invariant under all `24` proper rotations. This
representative `X` is fixed by `diag(1, 1, -1)`. The same enumeration finds
`4` proper and `4` improper signed permutations that fix `X`.

**Proof.** The absolute value `2` occupies one axis, so exactly one of the
six signed axes equals `d(a)`. The four points with last coordinate `+2`
are `(0, 1, 2)`, `(0, -1, 2)`, `(1, 0, 2)`, and `(-1, 0, 2)`. The first two
have axis triple `(0, 1, 2)`, whose sign is `+1`, and `(-1)^{2} = 1`, so
`epsilon = +1`. The last two have axis triple `(1, 0, 2)`, whose sign is
`-1`, so `epsilon = -1`. The cap sum is `0`. The quarter turn
`(x, y, z) -> (-y, x, z)` cycles these four points and exchanges the two
axis triples, so the cap is an eigenfunction of eigenvalue `-1`.

The same count of signs on every cap is the statement that every
directional sum vanishes. It is the finite check that each of the six caps
has two pluses and two minuses.

Bond symmetry is immediate: `X_d(a) X_{-d}(b)` equals
`X_{-d}(b) X_d(a)`. For the reflection `s = diag(1, 1, -1)`, the axis
indices of `s a` equal those of `a`, and `epsilon` does not read entry
signs, so `epsilon(s a) = epsilon(a)`. The sign of the absolute-value-`2`
entry flips, so `d(s a) = s d(a)`. Therefore
`X_{s d}(s a) = X_d(a)`. Since `s = s^{-1}`, the representative is
invariant under the soldered action of `s`, and so is the product.

Flipping the sign of `epsilon` on both members of one opposite pair of
directions multiplies `X_d(a)` and `X_{-d}(b)` by the same minus and does
not change the product. The factor `(-1)^{i2}` chooses a representative with `4` proper and `4`
improper fixers. Dropping it leaves the bond product unchanged; both
representatives still satisfy the reflection identity because both signs
read only axis roles. Without that factor, the representative has `12`
proper and `12` improper fixers. The runner checks both stabilizers and
the unchanged bond products; no reflection breaking follows from this gauge.

Soldered invariance under the remaining proper rotations is the same
identity on the `24 × 6 × 24 × 24` tuples. The runner evaluates those
tuples. It is not inferred from the single reflection.

## Theorem 3 — the product normalises, and the path law is order-blind

**Conclusion.** For every assignment of marks `x_d ∈ {-1, 0, 1}`,

```text
(1/24) sum_a prod_d (1 + kappa x_d X_d(a)) = 1
```

whenever the caps sum to `0`, at the supplied `kappa = 1/2` and in fact for
every scalar `kappa`. The resulting rule is strictly positive at
`kappa = 1/2`. On the path of three sites along `e_z`, all six formation
orders give one finished law of mass `1`. The two ends are independent,
with every pair mass `1/24^2`. The adjacent correlation
`E[X_z(a) X_{-z}(b)]` equals `kappa/36 = 1/72`. The rule varies:
`phi_z((0, 1, 2), (0, 1, -2)) = 3/2`.

**Proof.** At each `a` only `d(a)` has a nonzero factor, and that factor is
`epsilon(a)`. The product over directions therefore collapses to
`1 + kappa x_{d(a)} epsilon(a)`. Summing over `a` and grouping by caps,
each inner sum of `epsilon` is `0`. The average is `1` for every mark
assignment and every `kappa`.

At `kappa = 1/2` the three possible products `X_d(a) X_{-d}(b)` give
`1/2`, `1`, and `3/2`. In particular
`X_z(0, 1, 2) = 1` and `X_{-z}(0, 1, -2) = 1`, so one bond factor is
`3/2`. The uniform one-site weight times this factor is not the uniform
weight. The rule depends on the neighbour value.

For one occupied bond in direction `d`, the finished pair weight is
`(1/24)^2 phi_d(a, b)`, because the first site forms with an empty
neighbourhood and the second forms against that one neighbour. Then

```text
E[X_d(a) X_{-d}(b)]
  = (1/24)^2 sum_{a,b} (1 + kappa X_d(a) X_{-d}(b)) X_d(a) X_{-d}(b).
```

The sum of `X_d` vanishes, so the disconnected term drops. The remainder
factors as `kappa (sum_a X_d(a)^2) (sum_b X_{-d}(b)^2) / 24^2`. Each
square sum equals `4`, and `16 kappa / 576 = kappa/36`. At `kappa = 1/2`
this is `1/72`.

Bond symmetry says the two orders of an adjacent pair multiply by the same
factor. The runner does not stop at that identity: it builds all `24^3`
configurations of the three-site path under each of the six orders and
compares the finished laws, then sums the end marginal and the adjacent
correlation. Those comparisons are the path statement.

## What this does not do

- It does not select a formation order, a value of `kappa`, or a physical
  nearest-neighbour law.
- It does not split this alphabet into a chiral pair. There is one proper
  orbit.
- It does not revive the transverse-sign factor of `(1, 2, 3)`. That
  factor is zero here.
- It does not classify `(1, 1, 2)`, `(1, 2, 2)`, any mixed alphabet, or a
  bond space of rank greater than one.
- It does not identify the bond product with a mass density or with the
  `3×3` correlation of the earlier notes.
- It does not supply the formation site, probability, or rate, and it does
  not invent a hazard law.

## No-Go Discipline Gate

Scoped claim: this orbit is not a chiral pair, the transverse-sign factor
has no support on it, and the axis-role product above is nevertheless a
normalised soldered factor fixed by one reflection. A claim that every
24-point orbit varies, or that none does, is not made.

N1. Five attacks on that scoped claim:

1. Let the proper orbit be smaller than the mirror orbit. The sign-flip
   `diag(-1, 1, 1)` fixes the seed and folds every improper image back
   into `O`. `ATTEMPTED`.
2. Let the transverse product vary a cap. Every transverse pair on
   `a·d = 2` contains a zero. `ATTEMPTED`.
3. Let the axis-role product miss normalisation. Disjoint caps with sum
   zero kill every mark assignment. `ATTEMPTED`.
4. Let `diag(1, 1, -1)` flip the representative. It preserves axis indices
   and flips only the cap direction, and `epsilon` does not read the
   flipped sign. `ATTEMPTED`.
5. Let two formation orders of the path disagree. The runner compares all
   six laws. `ATTEMPTED`.

N2. The alphabet, the uniform one-site weight, the product shape, and the
value `kappa = 1/2` are one supplied model. No independent-wall count is
asserted.

N3. The formation reading and soldered action are written as hypotheses.
No phrase of a hidden dynamics clause is used in Theorems 1–3.

N4. The constancy proofs on the orbits of sizes 6, 8, and 12, and the
transverse-sign rule on `(1, 2, 3)`, are not lemmas. Dropping those
citations leaves Theorems 1–3 intact.

N5. "This orbit" means the proper cubic orbit of `(0, 1, 2)`. "The factor"
means the product built from the displayed `epsilon`. The path is the
three sites `(0,0,0)`, `(0,0,1)`, and `(0,0,2)`. No larger window was
enumerated.

N6. This note does not say that a new axiom is required. The three
approved primitives in the premise registry are not used. Source/action
remains an open gate.

N7. Steelman, outside this domain: a bond space of rank greater than one,
or the orbit of `(1, 1, 2)`. Those escapes do not split the orbit of
`(0, 1, 2)` and do not give the transverse-sign factor a support it does
not have.

N8. The chiral pair in the order-blind note is the mirror union of
`(1, 2, 3)`. This note does not reopen that pair. The quadratic channels
of a `3×3` correlation are a different carrier.

## Review record

This note does not narrow the bond, square, readout, or quadratic-channel
notes. It uses a different alphabet. The open-gate sentence of the axiom
memo is still the axiom text. It is not given a derivation.

Outstanding at landing: the product stays a supplied example; `kappa` stays
unselected; `(1, 1, 2)`, `(1, 2, 2)`, mixed alphabets, and higher-rank bond
spaces stay unclassified; formation site, probability, and rate stay
unsupplied; independent audit has not reviewed this note. No helper runner
is declared.

The cap arithmetic and the correlation factorisation were written before
the matching runner lines. The author re-ran two load-bearing mutations on
scratch copies; each exited nonzero, and the copies were not kept.

- Replacing the opposite cap in the product by the same direction fails
  five checks.
- Demanding that the adjacent correlation equal `1/36` rather than `1/72`
  fails the correlation check.

## Runner

`scripts/achiral_zero_one_two_orbit_order_blind_factor_2026_10_09.py`
builds the signed permutations, compares the proper and full orbits,
evaluates the transverse product, checks the caps and the quarter turn,
enumerates bond symmetry and soldered covariance, counts the signed
permutations that fix the representative, averages all `729` mark classes,
and compares the six path laws. It reads no external scientific input.
The mirror fold and the cap-sum argument are the checks that do not share
the path enumeration.
