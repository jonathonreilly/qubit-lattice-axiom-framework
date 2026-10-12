---
claim_id: zero_one_two_soldered_bond_kappa_not_forced_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Conditional on the formation reading and on bond factors of the shape 1 + kappa F_d with F independent of kappa. Partial neighbour conditions are required. On the proper cubic orbit of (0, 1, 2), soldered covariance of a rank-1 product does not constrain kappa. Normalisation at one nonzero kappa holds if and only if it holds for every kappa. Nonzero even quarter-turn families normalise only at kappa = 0. Each odd pure quarter-turn orbit line normalises for every kappa. Strict positivity on the unit line is the interval |kappa| < 1, not a point. No physical rule is selected. The bond correlation matrix is not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/zero_one_two_soldered_bond_kappa_not_forced_2026_10_09.py
---

# Soldered covariance on the orbit of (0, 1, 2) does not force kappa

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/zero_one_two_soldered_bond_kappa_not_forced_2026_10_09.py`](../scripts/zero_one_two_soldered_bond_kappa_not_forced_2026_10_09.py)

**Parent, not a lemma.** The order-blind note of 2026-09-22 fixes the
product shape and the partial-neighbour moment identity. The achiral-orbit
note on this branch exhibits one axis-role product on the proper orbit of
`(0, 1, 2)` and evaluates it at a supplied `kappa = 1/2`. Nothing below
uses that note's path masses, its correlation `1/72`, or its constancy
argument. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply proper
cubic rotations. Their open-gate list still places source/action outside
the axioms. This note does not supply a formation site, probability, or
rate.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact cocycle and moment identities for the rank-1 products on one 24-point alphabet, plus the homogeneous expansion in kappa."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Kappa stays unselected. A factor nonlinear in kappa, and normalisation of the full neighbourhood alone, stay open. Formation site, probability, and rate stay unsupplied."
conditional_surface_status: "bond factors 1 + kappa F on the proper cubic orbit of (0, 1, 2), with partial neighbour conditions"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

The formation reading says a nearest-neighbour rule assigns a distribution
to each partial map from the six axis directions to already formed
neighbour values. Soldered covariance rotates positions and values
together. The bond factor in this note has the shape

```text
phi_d(a, b) = 1 + kappa F_d(a, b),
```

with `F` independent of `kappa`. The rank-1 case is
`F_d(a, b) = X_d(a) X_{-d}(b)`. The one-site law is uniform on the proper
orbit of `(0, 1, 2)`. These are supplied mathematical hypotheses. They are
not the admissibility distribution, and `F` is not a mass density. The
`3×3` bond correlation used in the earlier notes of this campaign does not
appear.

## Theorem 1 — covariance does not see kappa

**Conclusion.** Let `kappa` be nonzero. Soldered covariance of `phi` is
equivalent to

```text
F_{g d}(g a, g b) = F_d(a, b)
```

for every proper cubic `g`, and this identity does not contain `kappa`.

**Proof.** Substitute the shape. The summand `1` matches, and the
remaining equality is multiplied by the same nonzero `kappa` on both
sides.

## Theorem 2 — partial normalisation isolates powers of kappa

**Conclusion.** Fix `F` independent of `kappa`, on any finite alphabet.
For a neighbour condition of cardinality `k`, the excess of the uniform
average is a polynomial of degree at most `k` with no constant term. If
the product is normalised at even one nonzero `kappa`, for every partial
neighbour condition, then every coefficient of every such polynomial
vanishes, and the product is normalised for every scalar `kappa`. If any
coefficient does not vanish, the product is normalised only at
`kappa = 0`. No product of this shape is normalised exactly on a nonempty
finite set of nonzero values.

**Proof.** Expand `prod (1 + kappa F_d(a, b_d))`. A condition `N` of
cardinality `k` has excess

```text
sum_{T ⊆ N, T nonempty} kappa^{|T|} Avg_a prod_{d in T} F_d(a, b_d).
```

Proceed by induction on `k`. At cardinality 1 the excess is `kappa` times
one average. It vanishes at a nonzero `kappa` only if that average is
identically zero as a function of the neighbour, so the excess polynomial
is the zero polynomial. At cardinality `k`, the coefficient of each
`kappa^j` with `j < k` is an average of a product over a proper subset
`T`. That average is the leading coefficient of the condition `T` with
the same neighbour values, and the inductive hypothesis says it is zero.
The excess therefore reduces to `kappa^k` times one average. Vanishing at
a nonzero `kappa` forces that average to vanish. Every coefficient is
zero, so every scalar `kappa` normalises the condition. If instead some
coefficient is nonzero, the smallest cardinality that carries it fails
for every nonzero `kappa`. The constant rule `kappa = 0` normalises for
every `F`, and it is not a selected interaction.

Each occupied direction contributes one factor of `kappa`, whether or not
`F_d` is an outer product. A sum of several rank-1 channels inside one
`F` does not change the degree count.

## Theorem 3 — both branches occur on this orbit

**Conclusion.** Let `A` be the proper cubic orbit of `(0, 1, 2)`, and let
`Q` be the quarter turn about `e_z`. The `Q`-orbits are six 4-point sets:
the caps `z = ±2`, the heights `z = ±1`, and two orbits in the plane
`z = 0`. A nonzero rank-1 product that is soldered-covariant has `X_z`
and `X_{-z}` in one common eigenspace of `Q`, with eigenvalue `±1`.
Transport by

```text
X_d(a) = f(σ_d^{-1} a),
```

Use matched opposite sections `σ_{-d}=σ_d H` for positive coordinate
axes, where `H=diag(1,-1,-1)`, and `σ_z=I`. Specifically, in row notation,
`σ_x=[[0,0,1],[1,0,0],[0,1,0]]` and
`σ_y=[[1,0,0],[0,0,1],[0,-1,0]]`. These are the runner's sections;
they send `e_z` to the indicated directions. Transport with this choice
preserves a linear cocycle

```text
X_{g d}(g a) = χ(g, d) X_d(a),    χ(g, d) χ(g, -d) = 1.
```

Inside the even sector the six orbit lines share one character, and inside
the odd sector they share one character, so both 6-dimensional spans are
covariant. A sum of the two eigenvalues on the positive cap is not.

On the even span, label coefficients by the six orbits and let `(s, t, u)`
be the three partner sums: positive cap with negative cap, height `+1`
with height `-1`, and the two zero-height orbits with each other. Let `P`
be the sum of the three partner products. The enumerated moments are

```text
sum_a X_z(a) = 4(s + t + u),
sum_a X_z(a) X_{-z}(a) = 8 P,
sum_a X_z(a) X_x(a) = 2(st + su + tu).
```

These three vanish together only at the zero coefficient vector. Every
nonzero even family is therefore normalised only at `kappa = 0`. The
positive-cap indicator has directional sum `4`, and its one-bond excess
equals `kappa` times that sum.

On the odd span every directional sum vanishes. Each pure orbit line has
disjoint directional supports, one direction occupied at each point, and
every subset moment zero, so every `kappa` normalises. The unit
positive-cap line has opposite bond products exactly `{-1, 0, 1}`. Strict
positivity of every bond factor is the interval `|kappa| < 1`, not a
point. Replacing the coefficient `c` by `2c` multiplies those products by
`4`, so the bond factor depends on the product `kappa c^2` and not on a
preferred pair `(kappa, c)`. The same line reproduces the axis-role bond
product of the achiral-orbit note. The odd family with both caps occupied,
and the odd family with the positive cap and the height `+1` both
occupied, each have a nonzero pair moment, so each is normalised only at
`kappa = 0`.

**Proof.** The quarter-turn count is the division of 24 points into orbits
of a fixed-point-free order-4 rotation. The identity section gives
`X_z = f`. Covariance under `Q`, which fixes both `e_z` and `-e_z`, reads
`u(Qa) v(Qb) = u(a) v(b)`. If the product is not identically zero, the
supports are `Q`-invariant and the common ratio is a fourth root of unity;
for real functions it is `±1`, the same eigenvalue on `u` and on `v`. The
two eigenspaces meet only at zero, so a mixed function makes the cross
term `u_+ ⊗ v_- + u_- ⊗ v_+` vanish only by killing the product. The
runner's mixed cap is that failure.

For `h=σ_{gd}^{-1}gσ_d`, one has `h∈<Q>`. The matched sections give
`σ_{-gd}^{-1}gσ_{-d}=HhH=h^{-1}`, since `HQH=Q^{-1}`. The real
characters `Q↦±1` agree on `h` and `h^{-1}`, proving the opposite-character
product is one. Independently chosen sections do not suffice: replacing
only `σ_x` by `σ_x Q` flips only `X_x` in the odd sector and breaks bond
covariance between the x and z directions. The runner checks this control.

The cocycle identity is linear. It holds on each of the six even lines
with one common character, and on each of the six odd lines with one
common character, so it holds on both spans. The character identity
`χ(d) χ(-d) = 1` is the product form of soldered covariance. One raw
product check under `Q`, not routed through the character table, agrees
on one even line and one odd line. The half turn about `x` is proper,
squares to the identity, and sends `e_z` to `-e_z`; on each odd line,
`X_{-z}` is a constant sign times `X_z` composed with that half turn, so
the opposite factor is not a second function.

A quadratic form on `Q^6` is determined by its values on `e_i` and on
`e_i + e_j`. The runner compares the three even moment formulae with the
enumerated sums on that determining set. The polynomial

```text
(s + t + u)^2 - 2(st + su + tu) - (s^2 + t^2 + u^2)
```

has every coefficient zero, so `s + t + u = 0` and `st + su + tu = 0`
imply `s^2 + t^2 + u^2 = 0`. Three rational squares sum to zero only when
each is zero: clear a common denominator, and use that an integer square
is nonnegative and that a sum of nonnegative integers vanishes only when
each summand does. Each partner sum then vanishes, so each partner pair
is antisymmetric. On that subspace a polynomial of degree at most 2 is
determined by its values on `{0, 1, 2}^3`. The opposite moment there
equals `-8(p^2 + q^2 + r^2)`, and the mean and the perpendicular moment
equal zero. Thus `-8(p^2 + q^2 + r^2) = 0` forces the remaining
amplitudes to vanish.

An odd function alternates on every 4-point orbit, so each directional
sum is zero. On a pure line the six transported copies meet each point
once, because each point's six pulls meet each orbit once; every product
of two or more directions is identically zero. The unit positive-cap
products are the runner's set `{-1, 0, 1}`. The factors `1 ± kappa` are
positive together exactly for `|kappa| < 1`. The comparison with the
axis-role sign is equality of all `6 × 24 × 24` bond products, not a path
enumeration. The two-cap odd family has opposite moment `8`. The
cap-plus-equator family has nonzero perpendicular moment, and one explicit
two-bond excess equals `kappa^2` times that moment times two nonzero
marks: the value at `kappa = 2` is four times the value at `kappa = 1`,
and the value at `kappa = 1` is not zero.

## What this does not do

- It does not select a value of `kappa`, a formation order, or a physical
  nearest-neighbour law. The constant rule at `kappa = 0` is not a
  selected interaction.
- It does not recompute a path correlation. The axis-role product is
  identified only by its bond factors.
- It does not list every odd coefficient vector whose moments vanish. Any
  further vector with all moments zero is normalised for every `kappa`, by
  Theorem 2. The six pure lines are enough to show that the free branch
  is nonempty.
- It does not treat a factor `1 + kappa F + kappa^2 G` with `G` independent
  of `F`. Inside one cardinality those two powers can balance.
- It does not drop partial neighbour conditions. A rule required to
  normalise only when all six neighbours are present can mix degrees.
- It does not classify another alphabet, and it does not exhibit a
  higher-rank flat family. Theorem 2 already says that a higher-rank
  channel still inside `1 + kappa F` cannot pin a nonzero `kappa`.
- It does not identify the bond product with a mass density or with the
  `3×3` correlation of the earlier notes.
- It does not supply the formation site, probability, or rate, and it does
  not invent a hazard law.

## No-Go Discipline Gate

Scoped claim: no normalised soldered-covariant product of the shape
`1 + kappa F` on this orbit, with partial neighbour conditions and `F`
independent of `kappa`, has its `kappa` fixed at a nonzero value. Even
quarter-turn families normalise only at `0`. Odd pure lines normalise for
every `kappa`.

N1. Five attacks on that scoped claim:

1. Let the even sector hide a discrete nonzero `kappa`. Its mean or a pair
   moment is a nonzero pure power unless the coefficient vector is zero.
   `ATTEMPTED`.
2. Let two odd orbits cancel different powers at one `kappa`. A condition
   of one cardinality is a single power. `ATTEMPTED`.
3. Let a mixed eigenvalue produce a covariant product that pins `kappa`.
   The quarter-turn identity kills the mixed product, and one explicit sum
   fails the cocycle. `ATTEMPTED`.
4. Let strict positivity on the axis-role line select `kappa = 1/2`. The
   unit products are `{-1, 0, 1}`, so positivity is `|kappa| < 1`.
   `ATTEMPTED`.
5. Let the scale `c` of a pure line be fixed and thereby fix `kappa`. The
   bond factor depends on `kappa c^2`, and `c = 2` multiplies the products
   by `4`. `ATTEMPTED`.

N2. The shape `1 + kappa F`, the partial-neighbour reading, and the orbit
are one supplied model. No independent-wall count is asserted. Dropping
partial conditions is the same escape as allowing two powers in one
cardinality, not a second wall.

N3. The formation reading, the product shape, and the uniform weight are
written as hypotheses. No phrase of a hidden dynamics clause is used in
Theorems 1–3. The three approved primitives in the premise registry are
not used.

N4. The achiral-orbit note is not a witness that `kappa` was already
forced or already freed for every covariant product. It evaluates one
product at one supplied value. The order-blind note's transverse-sign rule
is a different alphabet. Dropping both citations leaves Theorems 1–3
intact.

N5. "This orbit" means the proper cubic orbit of `(0, 1, 2)`. "The factor"
means `1 + kappa F` as displayed. The runner resolves record values and
directions. It does not resolve a multi-site window, a block of sites, or
an infinite lattice.

N6. This note does not say that a new axiom is required. Source/action
remains an open gate. A nonlinear dependence on `kappa` would be a
different supplied shape, not a new axiom of this note.

N7. Steelman, outside this domain: allow `phi = 1 + kappa F + kappa^2 G`
with `F` and `G` soldered-covariant and not proportional, or require
normalisation only for the full six-neighbour condition. Either escape can
balance two powers. Neither split is a normalised linear product on this
orbit, and neither gives the even sector a nonzero `kappa`.

N8. The axis-role product in the achiral-orbit note is the odd
positive-cap line of Theorem 3. This note does not reopen that path
calculation, the chiral pair of `(1, 2, 3)`, or the quadratic channels of
a `3×3` correlation.

## Review record

This note does not narrow the achiral-orbit note. It uses the same
alphabet and answers a question that note left open: whether every
normalised covariant product leaves `kappa` free. The open-gate sentence
of the axiom memo is still the axiom text. It is not given a derivation.

Outstanding at landing: `kappa` stays unselected; the odd moment-flat
locus may be larger than the six pure lines, and any such extension is
still free for every `kappa`; a factor nonlinear in `kappa` stays
unclassified; formation site, probability, and rate stay unsupplied;
independent audit has not reviewed this note. No helper runner is
declared.

The expansion and the partner-sum reduction were written before the
matching runner lines. The author re-ran two load-bearing mutations on
scratch copies; each exited with `FAIL=1`, and the copies were not kept.

- Demanding that the even positive-cap indicator stay normalised at
  `kappa = 1` fails one check.
- Demanding that an odd pure line have a nonzero subset moment fails one
  check.

## Runner

`scripts/zero_one_two_soldered_bond_kappa_not_forced_2026_10_09.py`
builds the signed permutations and the six quarter-turn orbits, compares
cocycle characters inside each sector, checks one raw product under the
quarter turn, compares the even moment polynomials with their closed forms
on the determining set `e_i` and `e_i + e_j`, expands the square identity,
checks the antisymmetric grid `{0, 1, 2}^3`, enumerates all subset moments
of the six odd lines, and compares the axis-role bond products. It reads
no external scientific input. The character table and the raw quarter-turn
product are the two covariance checks. The one-bond and two-bond excesses
are the homogeneity checks that do not share that table.
