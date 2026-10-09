---
claim_id: zero_one_two_shifted_cap_factor_unique_nonzero_root_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Conditional on the formation reading and on partial neighbour conditions. On the proper cubic orbit of (0, 1, 2), the soldered bond factor phi(t) = 1 + (1 - 2 t) B^X + (t^2 - t + 1) B^Y, with B^X and B^Y the odd cap bond kernels, is not the constant factor 1 at t = 0. Partial normalisation holds at exactly one real value, t = 1/2. There phi = 1 + (3/4) B^Y, and the opposite bond values are 1/4, 1, and 7/4, all positive. The root is the root of the supplied linear polynomial. No physical rule is selected. The bond correlation matrix is not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/zero_one_two_shifted_cap_factor_unique_nonzero_root_2026_10_09.py
---

# One shifted cap factor has a unique nonzero normalisation value

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/zero_one_two_shifted_cap_factor_unique_nonzero_root_2026_10_09.py`](../scripts/zero_one_two_shifted_cap_factor_unique_nonzero_root_2026_10_09.py)

**Parent, not a lemma.** The quadratic pencil note on this branch classifies
factors that equal the constant `1` at `t = 0`. Its steelman left open a
factor whose value at the parameter origin is a non-constant soldered bond
factor. Nothing below uses that note's `625`-tuple census, its balance
witness, or its root counts. The two odd cap lines are rebuilt here. The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply proper cubic rotations.
Their open-gate list still places source/action outside the axioms, and the
2026-07-04 revision still leaves the formation rule — which admissible
possibility, at which site, with what weight, at what rate — as downstream
supplier content. This note does not supply a formation site, probability,
or rate.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact support, covariance, root, and partial-normalisation identities for one declared bond factor on two odd cap lines."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "This factor has a unique nonzero normalisation value, and that value is supplied by the polynomial 1 - 2 t. It is not a selected interaction. The odd cap alphabet stops. Do not queue another pencil. The following block's supplier is the formation rule, not a bond pencil. Formation site, probability, and rate stay unsupplied."
conditional_surface_status: "one shifted factor 1 + (1 - 2 t) X + (t^2 - t + 1) Y on the odd cap lines, partial neighbour conditions, orbit of (0, 1, 2)"
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
campaign does not appear. The polynomials below are supplied coefficients,
not a derived law.

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
distinct directions on one line is identically `0`. Both bond kernels

```text
B^X_d(a, b) = X_d(a) X_{-d}(b),    B^Y_d(a, b) = Y_d(a) Y_{-d}(b)
```

are invariant under every proper cubic rotation, and they are linearly
independent. The opposite bond products of each kernel are exactly
`{-1, 0, 1}`.

**Proof.** The group and the orbit each have 24 elements. The quarter
turn has six orbits of length 4, one at each of the heights `2` and `-2`.
The identities are equalities of those finitely many integers. The runner
evaluates them on every record and every direction, and it compares both
sides of each bond identity on every proper rotation and every pair of
records. Independence is one bond where `B^X` is nonzero and `B^Y` is
zero, and one bond with those roles reversed.

## Theorem 2 — normalisation of one affine combination

**Conclusion.** For any rational scalars `c1` and `c2`, the bond factor
`1 + c1 B^X + c2 B^Y` is normalised for every partial neighbour condition
if and only if `c1 = 0` or `c2 = 0`. If both are nonzero, one opposite-`z`
condition has sum `24 + 4 c1 c2`.

**Proof.** Suppose `c2 = 0`. Distinct directions of `X` have disjoint
supports, and the records partition into those six supports, four records
each. On a condition `T`, a record whose occupied direction lies outside
`T` contributes `1`. A record whose occupied direction `e` lies in `T`
contributes `1 + c1 m_e X_e(a)`. The sum of `X_e` on its support is `0`,
so those four records contribute `4`. The total is `4 * 6 = 24`. The same
count with `Y` covers `c1 = 0`. The value of the surviving scalar does
not enter.

A condition that uses only one direction cannot see both coefficients.
On one direction the two lines have disjoint supports, so each record
meets at most one of them, and the same cancellation applies to both
scalars at once. The obstruction uses two directions.

Suppose instead that both scalars are nonzero. The opposite-`z` mark
pairs of `(X, Y)` include `(1, 0)` and `(0, 1)`. Choose the `+z`
neighbour so that `(X_{-z}, Y_{-z}) = (1, 0)`, and the `-z` neighbour so
that `(X_z, Y_z) = (0, 1)`. The `+z` factor is `1 + c1 X_z`. The
direction-reversal identity turns the `-z` factor into `1 + c2 X_z`. The
product sum is

```text
sum_a (1 + c1 X_z(a)) (1 + c2 X_z(a)) = 24 + 4 c1 c2,
```

because the directional sum vanishes and the square sum is `4`. The same
polynomial identity holds for every rational pair, not only for integers:
it expands in the integer values of `X_z`. The excess sum is `4 c1 c2`,
which is zero only if `c1 c2 = 0`. The runner compares that monomial with
the expanded sum on every pair in `{-2, ..., 2}^2`, including `(1, 1)`,
`(-1, 1)`, and `(0, 1)`.

## Theorem 3 — one shifted factor has a unique nonzero root

**Conclusion.** Define

```text
phi(t) = 1 + (1 - 2 t) B^X + (t^2 - t + 1) B^Y.
```

Write `c1(t) = 1 - 2 t` and `c2(t) = t^2 - t + 1`. For every rational `t`,
`phi(t)` is a scalar combination of the two invariant kernels, with
scalars independent of the direction, so `phi(t)` is soldered-covariant.
The value `phi(0) = 1 + B^X + B^Y` is not the constant factor `1`. The
coefficient vectors at `t = 0` and at `t = 1` are `(1, 1)` and `(-1, 1)`.
Their determinant is `2`, so there is no function `H` independent of `t`
and no scalar `kappa(t)` with `phi(t) = 1 + kappa(t) H`.

Partial normalisation holds at a real number `t` if and only if `c1(t) = 0`
or `c2(t) = 0`. The first equation holds only at `t = 1/2`. The second
polynomial has no real root. Therefore `t = 1/2` is the unique real
normalisation value, and it is nonzero. At that value

```text
phi(1/2) = 1 + (3/4) B^Y.
```

The opposite bond values are `(4 + 3 u)/4` for `u` in `{-1, 0, 1}`, that
is `1/4`, `1`, and `7/4`, all strictly positive. The runner checks every
partial mark image at `t = 1/2`, at `t = 0`, and at `t = 1`.

**Proof.** Theorem 2 applies to the rational values `c1(t)` and `c2(t)`.
The equation `1 - 2 t = 0` has the single solution `t = 1/2`. In
particular it holds at the unreduced fraction `2/4` and fails at `0`,
`1`, and `3/2`. The quadratic `t^2 - t + 1` is monic with integer
coefficients and constant term `1`, so any rational root in lowest terms
has numerator dividing `1` and denominator dividing `1`, hence is `±1`.
The values there are `c2(1) = 1` and `c2(-1) = 3`, neither zero. Its
discriminant is `1 - 4 = -3`, so it has no real root. The only real
solution of `c1(t) = 0` or `c2(t) = 0` is `t = 1/2`.

Substitute that value: `c1(1/2) = 0` and
`c2(1/2) = 1/4 - 1/2 + 1 = 3/4`. Theorem 1 gives the opposite products of
`B^Y`. Each numerator `4 + 3 u` is `1`, `4`, or `7`. Since `B^X` is not
identically zero, `phi(0)` is not the constant function `1`. The two
coefficient vectors are not proportional because their determinant is `2`.
The partial-mark scans at `0` and at `1` fail, and the scan at `1/2`
passes, which matches the criterion at those three rationals. The root
analysis covers every other real number. No further parameter is scanned.

## What this does not do

- It does not select a value of `t`, of `kappa`, or of a physical
  nearest-neighbour law. The unique root is the root of the supplied
  polynomial `1 - 2 t`. The scale `3/4` is the supplied quadratic
  evaluated there. Covariance holds for every `t`, so it does not choose
  the root. Replacing the supplied linear factor by a different polynomial
  moves the root. That replacement is not performed here.
- It does not say that every bond factor with a non-constant value at
  `t = 0` has a unique nonzero root. The declared object is this one
  factor.
- It does not rerun the coefficient box `{-2, -1, 0, 1, 2}` or the shape
  `1 + t (a X + b Y) + t^2 (c X + d Y)`. Those pencils equal `1` at the
  origin and were already classified.
- It does not rerun the even and odd quarter-turn split of `1 + kappa F`.
  The value at the root is one pure line, already known to normalise at
  every scale. The new fact is that this pencil meets that line at exactly
  one parameter.
- It does not recompute a path correlation, a CHSH square, a readout
  weight, or a quadratic channel of a `3×3` correlation.
- It does not identify either cap line with a mass density, and it does
  not identify `phi` with a formation weight.
- It does not supply the formation site, probability, or rate, and it
  does not invent a hazard law.
- It does not queue another pencil. The odd cap alphabet of `(0, 1, 2)`
  stops in this campaign. The supplier for a following block is the
  formation rule left outside the axioms, not another bond factor.

## No-Go Discipline Gate

Scoped claim: the one factor `phi` above is soldered-covariant, is not the
constant `1` at `t = 0`, and is partially normalised at exactly one real
number, `t = 1/2`, where the bond values are strictly positive. That
number is not a selected physical law.

N1. Five attacks on that scoped claim:

1. Let `t = 0` be the normalisation value because the constant term is
   `1`. The kernel coefficients there are both `1`, and the opposite-`z`
   excess sum is `4`. `ATTEMPTED`.
2. Let strict positivity delete `t = 1/2`. The numerators are `1`, `4`,
   and `7`. `ATTEMPTED`.
3. Let `t^2 - t + 1` vanish at `t = 1` and supply a second rational root.
   The value is `1`, not `0`. `ATTEMPTED`.
4. Let the factor be the old shape `1 + kappa(t) H`. The coefficient
   vectors at `0` and at `1` have determinant `2`. `ATTEMPTED`.
5. Let the unique root be the constant rule `phi = 1`. At `t = 1/2` the
   `Y` coefficient is `3/4`, not `0`. `ATTEMPTED`.

N2. This factor, the two cap lines, the partial-neighbour reading, and the
orbit are one supplied model. No independent-wall count is asserted.
Dropping partial conditions is a different reading, not a second wall
inside this factor.

N3. The formation reading, the factor, and the uniform weight are written
as hypotheses. No phrase of a hidden dynamics clause is used in Theorems
1–3. The three approved primitives `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive` are not used.

N4. The quadratic box is not a witness that a shifted factor was already
classified. Dropping it leaves Theorems 1–3 intact: the cap lines, the
excess, and this factor are recomputed here.

N5. "This factor" means the two polynomials above and the bond kernels in
the span of `B^X` and `B^Y` on the proper orbit of `(0, 1, 2)`. The runner
resolves record values and directions. It does not resolve a multi-site
window, a block of sites, or an infinite lattice.

N6. This note does not say that a new axiom is required. Source/action
remains an open gate. The formation rule remains downstream supplier
content. Exhibiting a mathematical root does not fill that supplier.

N7. Steelman, outside this factor: allow a third bond kernel, or require
normalisation only for the full six-neighbour condition. Either can change
the root set. Neither is this factor. Neither is queued. The odd cap
alphabet stops.

N8. This note does not reopen the linear quarter-turn split, the
achiral-orbit path factor, the quadratic coefficient box, the chiral pair
of `(1, 2, 3)`, or the quadratic channels of a `3×3` correlation.

## Review record

This note does not narrow the quadratic pencil note. It uses the same
alphabet and answers the steelman that note left open, for one declared
factor: a non-constant value at `t = 0` can move the forced root off `0`,
and for this factor the resulting root is unique and nonzero. The root is
still a supplied number. The open-gate sentence of the axiom memo is still
the axiom text. It is not given a derivation.

Outstanding at landing: `t = 1/2` is not a selected interaction; the odd
cap alphabet stops; another pencil is not queued; the formation-rule
supplier stays unsupplied; independent audit has not reviewed this note.
No helper runner is declared.

The root formula and the excess `4 c1 c2` were written before the matching
runner lines. The author re-ran two load-bearing mutations on scratch
copies; each exited with `FAIL=1`, and the copies were not kept.

- Demanding that the factor fail normalisation at `t = 1/2` fails one check.
- Demanding that `t^2 - t + 1` vanish at `t = 1` fails one check.

## Runner

`scripts/zero_one_two_shifted_cap_factor_unique_nonzero_root_2026_10_09.py`
builds the proper cubic group, the two cap orbits, and the transported
alternating lines. It checks direction reversal, supports, soldered
invariance of both bond kernels, both opposite-product sets, the excess
monomial `4 c1 c2`, the coefficient values at `0`, `1/2`, `1`, and `-1`,
the discriminant `-3`, the determinant `2`, the positivity numerators, and
every partial mark image at `t = 1/2`, `t = 0`, and `t = 1`. It reads no
external scientific input.
