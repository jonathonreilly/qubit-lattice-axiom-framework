---
claim_id: zero_one_two_partner_cap_quadratic_pencil_no_unique_nonzero_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Conditional on the formation reading and on partial neighbour conditions. On the proper cubic orbit of (0, 1, 2), bond factors 1 + t (a X + b Y) + t^2 (c X + d Y), with X and Y the odd cap lines and with coefficients in {-2,-1,0,1,2}, are not of the shape 1 + kappa F when a d - b c is nonzero. Normalisation always holds at t = 0. A nonzero rational is never the unique normalised value. In that independent box, 32 pencils normalise only at 0, 256 at two rationals, and 208 at three. Strict positivity does not choose between 0 and 1/2 on the named balance pencil. No physical rule is selected. The bond correlation matrix is not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/zero_one_two_partner_cap_quadratic_pencil_2026_10_09.py
---

# A quadratic partner-cap pencil does not isolate a nonzero parameter

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/zero_one_two_partner_cap_quadratic_pencil_2026_10_09.py`](../scripts/zero_one_two_partner_cap_quadratic_pencil_2026_10_09.py)

**Parent, not a lemma.** The linear note on this branch classifies bond
factors `1 + kappa F` with `F` independent of `kappa`. Its steelman was a
second power. Nothing below uses that note's even-sector moment
polynomials, its quarter-turn character table, or its path correlation.
The two odd cap lines are rebuilt here. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
supply proper cubic rotations. Their open-gate list still places
source/action outside the axioms. This note does not supply a formation
site, probability, or rate.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact support, moment, and root-set identities for one finite box of quadratic pencils on two odd cap lines."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "No unique nonzero parameter is selected in this box. A factor that is not 1 at t = 0, a cubic term, and normalisation of the full neighbourhood alone stay open. Formation site, probability, and rate stay unsupplied."
conditional_surface_status: "quadratic pencils in the odd partner-cap span, coefficients in {-2,-1,0,1,2}, partial neighbour conditions, orbit of (0, 1, 2)"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

The formation reading says a nearest-neighbour rule assigns a distribution
to each partial map from the six axis directions to already formed
neighbour values. Soldered covariance rotates positions and values
together. The one-site carrier is the proper cubic orbit of `(0, 1, 2)`,
with the uniform weight. These are supplied mathematical hypotheses. They
are not the admissibility distribution. Neither cap line is a mass
density. The `3×3` bond correlation used in the earlier notes of this
campaign does not appear.

## Theorem 1 — two odd cap lines

**Conclusion.** Let `A` be the proper cubic orbit of `(0, 1, 2)`, and let
`Q` be the quarter turn about `e_z`. Write `H` for the half turn about
`e_x`. The sections used below send `e_z` to a direction, the section at
`e_z` is the identity, and the section at `-e_z` is `H`. Let `f+` be the
alternating function, values `±1`, on the unique `Q`-orbit of height `2`,
and let `f-` be the same construction on the unique orbit of height `-2`.
Transport them by the sections:

```text
X_d(a) = f+(σ_d^{-1} a),    Y_d(a) = f-(σ_d^{-1} a).
```

Then `Y_{-d} = X_d` and `X_{-d} = Y_d`. On each direction the two supports
are disjoint. Each record meets exactly one direction of `X` and the
opposite direction of `Y`, and the two nonzero values there are equal.
Each directional sum is `0` and each square sum is `4`. A product of two
distinct directions on one line is identically `0`. Every nonempty subset
moment of each line is `0`. The opposite bond products of `X` are exactly
`{-1, 0, 1}`. Both bond kernels

```text
B^X_d(a, b) = X_d(a) X_{-d}(b),    B^Y_d(a, b) = Y_d(a) Y_{-d}(b)
```

are invariant under every proper cubic rotation, and they are linearly
independent.

**Proof.** The group and the orbit each have 24 elements. The quarter
turn has six orbits of length 4, one at each of the heights `2` and `-2`.
The identities are equalities of those finitely many integers. The runner
evaluates them on every record and every direction, and it compares both
sides of each bond identity on every proper rotation and every pair of
records. Independence is one bond where `B^X` is nonzero and `B^Y` is
zero, and one bond with those roles reversed.

## Theorem 2 — one linear combination is normalised only on a coordinate axis

**Conclusion.** For any rational scalars `c1` and `c2`, the bond factor
`1 + c1 B^X + c2 B^Y` is normalised for every partial neighbour condition
if and only if `c1 = 0` or `c2 = 0`. If both are nonzero, one opposite-`z`
condition has excess sum `4 c1 c2`.

**Proof.** Suppose `c1 = 0`. The supports of the six functions `Y_d`
partition the 24 records, four records to each direction. On a condition
`T`, a record whose occupied direction lies outside `T` contributes the
product `1`. A record whose occupied direction `e` lies in `T` contributes
`1 + c2 m_e Y_e(a)`, and the sum of `Y_e` on its four-point support is
`0`, so those four records contribute `4`. The total is
`4 (6 - |T|) + 4 |T| = 24`. The same count with `X` covers `c2 = 0`.
Every mark cancels with the directional sum, so the value of `c1` or of
`c2` does not enter.

Suppose instead that both scalars are nonzero. The opposite-`z` mark
pairs of `(X, Y)` include `(1, 0)` and `(0, 1)`. Choose the `+z`
neighbour so that `(X_{-z}, Y_{-z}) = (1, 0)`, and the `-z` neighbour so
that `(X_z, Y_z) = (0, 1)`. The direction-reversal identity turns the
second factor into `c2 X_z`. The product sum is

```text
sum_a (1 + c1 X_z(a)) (1 + c2 X_z(a)) = 24 + 4 c1 c2,
```

because the directional sum vanishes and the square sum is `4`. The
excess sum is `4 c1 c2`, which the runner compares with that monomial on
every pair in `{-2, ..., 2}^2`. It is zero only if `c1 c2 = 0`.

## Theorem 3 — a quadratic pencil always keeps the constant rule

**Conclusion.** For integers `a, b, c, d`, define

```text
phi(t) = 1 + t (a B^X + b B^Y) + t^2 (c B^X + d B^Y).
```

Then

```text
phi(t) = 1 + c1(t) B^X + c2(t) B^Y,
c1(t) = t (a + c t),    c2(t) = t (b + d t).
```

Partial normalisation holds exactly when `c1(t) = 0` or `c2(t) = 0`. The
value `t = 0` is always a solution, and `phi(0)` is the constant factor
`1`. If `a d - b c ≠ 0`, neither linear factor is the zero polynomial, the
coefficient vectors `(a, b)` and `(c, d)` are linearly independent, and
there is no function `H` independent of `t` and no scalar `kappa(t)` with
`phi(t) = 1 + kappa(t) H`. A nonzero rational is then never the unique
normalised value.

**Proof.** Substitute the two powers. Theorem 2 applies to the rational
values `c1(t)` and `c2(t)`. Both have the factor `t`, so `t = 0` is a
root, and the bond factor there is `1`. The polynomial `a + c t` is
identically zero only if `a = c = 0`, and `b + d t` is identically zero
only if `b = d = 0`. Either case forces the determinant `a d - b c` to
vanish. For a nonzero determinant the extra roots, when they are rational
and present, are `t = -a/c` if `c ≠ 0` and `t = -b/d` if `d ≠ 0`, and
`0` remains among them.

If `phi(t) - 1` lay on a single line `kappa(t) H` with `H` independent of
`t`, the coefficient vectors of `t` and of `t^2` would be parallel. They
are `(a, b)` and `(c, d)`. The balance witness below has vectors `(1, 1)`
and `(0, -2)`. Its bond functions at `t = 1` and at `t = 2` are the
combinations with coefficients `(1, -1)` and `(2, -6)`. Those two integer
vectors have determinant `-4`, and the runner finds that the corresponding
opposite-`z` bond tables are not proportional.

## Theorem 4 — the finite box

**Conclusion.** Let the coefficients range over `{-2, -1, 0, 1, 2}`. Of
the `625` tuples, `129` have determinant `0` and are excluded: they are
the shape `1 + kappa H` after the reparametrisation `kappa = t + lambda t^2`,
or a degenerate case of it. The one-parameter family `1 + (t + 2 t^2) B^X`
is such a tuple, and it is normalised at `t = 1` and at `t = 3` because
every scale of `B^X` is normalised. The remaining `496` tuples are
linearly independent as bond coefficients. Exactly `32` of them are
normalised only at `0`, exactly `256` at two rationals, and exactly `208`
at three. No independent tuple has a unique nonzero normalised value.

Three tuples show the three cardinalities:

- `(a, b, c, d) = (1, 0, 0, 1)`, so `F = B^X` and `G = B^Y`, is normalised
  only at `0`. At `t = 1` a partial condition fails.
- `(1, 1, 0, -2)`, so `F = B^X + B^Y` and `G = -2 B^Y`, is normalised
  exactly at `0` and at `1/2`. At `t = 1/2` one has `c1 = 1/2` and
  `c2 = 0`, so `phi = 1 + (1/2) B^X`. The bond values are `1/2`, `1`, and
  `3/2`, all positive. At `t = 0` the factor is `1`, also positive. At
  `t = 1` a partial condition fails.
- `(1, 1, -1, -2)` is normalised exactly at `0`, `1/2`, and `1`, and not
  at `2`.

The runner checks every partial mark image for these three pencils at
those rationals, not only the opposite-`z` excess.

**Proof.** The root set is the set in Theorem 3. The runner enumerates
the box, rejects determinant `0`, and counts the distinct reduced roots.
It also checks that no independent tuple has `a = c = 0` or `b = d = 0`,
so neither factor vanishes as a polynomial and the root description does
not hide an identically flat axis. Strict positivity on the balance
pencil keeps both `0` and `1/2`: the constant factor is positive, and
`2 + u > 0` for every opposite product `u` in `{-1, 0, 1}`.

## What this does not do

- It does not select a value of `t`, of `kappa`, or of a physical
  nearest-neighbour law. The constant rule `phi = 1` is not a selected
  interaction. The value `1/2` is a second root of one supplied pencil,
  and the same pencil is also normalised at `0`.
- It does not say that every nonlinear bond factor fails to isolate a
  parameter. The declared family is this coefficient box in the span of
  `B^X` and `B^Y`. A factor that is not `1` at the parameter origin, a
  third power, and a rule required to normalise only when all six
  neighbours are present are outside the family.
- It does not rerun the even and odd quarter-turn split of the linear
  ansatz `1 + kappa F`. The dependent pure line is one excluded control,
  not that classification.
- It does not recompute a path correlation, a CHSH square, a readout
  weight, or a quadratic channel of a `3×3` correlation.
- It does not identify either cap line with a mass density.
- It does not supply the formation site, probability, or rate, and it
  does not invent a hazard law.

## No-Go Discipline Gate

Scoped claim: no normalised soldered-covariant pencil in this coefficient
box, with `a d - b c ≠ 0` and with partial neighbour conditions, has a
unique nonzero parameter. The constant value `0` remains normalised for
every such pencil. On `(1, 1, 0, -2)`, strict positivity keeps both `0`
and `1/2`.

N1. Five attacks on that scoped claim:

1. Let the root `t = 0` be removed by not evaluating the constant factor.
   `phi(0) = 1`, and the empty power of `t` in `c1` and in `c2` is zero.
   `ATTEMPTED`.
2. Let strict positivity delete `t = 0` and keep `1/2`. Both factors are
   positive on the balance pencil. `ATTEMPTED`.
3. Let a dependent tuple produce a unique nonzero `kappa` inside the box.
   Determinant `0` is excluded. The control `1 + (t + 2 t^2) B^X` is
   normalised at more than one nonzero `t`. `ATTEMPTED`.
4. Let the three cardinalities collapse to a nonzero singleton under the
   box bounds. The counts are `32`, `256`, and `208`, and every set
   contains `0`. `ATTEMPTED`.
5. Let a cancellation hide a third scalar with `c1` and `c2` both
   nonzero. The opposite-`z` excess sum is `4 c1 c2`. `ATTEMPTED`.

N2. The coefficient box, the two cap lines, the partial-neighbour reading,
and the orbit are one supplied model. No independent-wall count is
asserted. Dropping partial conditions is a different reading, not a
second wall inside this box.

N3. The formation reading, the pencil, and the uniform weight are written
as hypotheses. No phrase of a hidden dynamics clause is used in Theorems
1–4. The three approved primitives `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive` are not used.

N4. The linear note is not a witness that a second power was already
classified. Dropping it leaves Theorems 1–4 intact: the cap lines, the
excess, and the box are recomputed here.

N5. "This box" means coefficients in `{-2, -1, 0, 1, 2}` and bond kernels
in the span of `B^X` and `B^Y` on the proper orbit of `(0, 1, 2)`. The
runner resolves record values and directions. It does not resolve a
multi-site window, a block of sites, or an infinite lattice.

N6. This note does not say that a new axiom is required. Source/action
remains an open gate. A factor that is not `1` at `t = 0` would be a
different supplied shape, not a new axiom of this note.

N7. Steelman, outside this domain: allow a summand `t^3 H` with `H`
independent of `B^X` and `B^Y`, or allow `phi(0)` to be a non-constant
soldered factor, or require normalisation only for the full six-neighbour
condition. Any of those can move the forced root at `0`. None is an
independent pencil in this box, and none selects a formation rate.

N8. This note does not reopen the linear quarter-turn split, the
achiral-orbit path factor, the chiral pair of `(1, 2, 3)`, or the
quadratic channels of a `3×3` correlation.

## Review record

This note does not narrow the linear note. It uses the same alphabet and
answers the steelman that note left open, inside one declared box: a
second power can add a nonzero normalised rational, and it cannot make
that rational the only one. The open-gate sentence of the axiom memo is
still the axiom text. It is not given a derivation.

Outstanding at landing: `t` and `kappa` stay unselected; the odd moment-flat
locus may be larger than these two lines; a factor that is not `1` at the
parameter origin stays unclassified; formation site, probability, and rate
stay unsupplied; independent audit has not reviewed this note. No helper
runner is declared.

The root formula and the excess `4 c1 c2` were written before the matching
runner lines. The author re-ran two load-bearing mutations on scratch
copies; each exited with `FAIL=1`, and the copies were not kept.

- Demanding that the balance pencil normalise only at `0` fails one check.
- Demanding that the opposite-`z` excess sum vanish for every `c1, c2`
  fails one check.

## Runner

`scripts/zero_one_two_partner_cap_quadratic_pencil_2026_10_09.py`
builds the proper cubic group, the two cap orbits, and the transported
alternating lines. It checks direction reversal, supports, subset moments,
soldered invariance of both bond kernels, the excess monomial `4 c1 c2`,
the `625`-tuple census, the three named root sets, positivity numerators
at `t = 1/2`, non-proportionality of the balance pencil at `t = 1` and
`t = 2`, and every partial mark image of those pencils at the claimed
roots and at one failing rational. The dependent control is checked at
`t = 1` and at `t = 3`. It reads no external scientific input.
