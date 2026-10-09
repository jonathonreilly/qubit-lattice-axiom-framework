---
claim_id: directed_bond_quadratic_action_channels_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Conditional on a real 3x3 correlation matrix transforming by T -> R T R^T under signed permutations. The proper cubic group has order 24 and the full signed-permutation group has order 48. The quadratic polynomials invariant under either group are the same 4-dimensional space, with basis the trace square, the traceless-diagonal square, the symmetric-off-diagonal square, and the antisymmetric square. A rational 3-4-5 rotation leaves only the ratio 9/2 of the two middle squares constant on one tested pair. On the directed pattern the symmetric-off-diagonal square is identically 0, the antisymmetric square is 4 t^2, and every invariant quadratic is even in t. The four channel ratios stay unselected. No CHSH square and no readout weight is recomputed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/directed_bond_quadratic_action_channels_2026_10_09.py
---

# Proper-cubic quadratic scalars of a bond correlation leave four channel ratios free

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/directed_bond_quadratic_action_channels_2026_10_09.py`](../scripts/directed_bond_quadratic_action_channels_2026_10_09.py)

**Parents:** the proper cubic generators are the same two matrices written in
[`PROPER_CUBIC_TWO_QUBIT_BOND_INVARIANTS_BOUNDED_THEOREM_NOTE_2026-10-09.md`](PROPER_CUBIC_TWO_QUBIT_BOND_INVARIANTS_BOUNDED_THEOREM_NOTE_2026-10-09.md).
The directed pattern is the coefficient pattern named there and used by the
later readout note. Neither note's square, partial trace, or nullspace is a
lemma below. The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply proper cubic rotations.
Their open-gate list still places source/action and physical-observable
identification outside the axioms. This note does not close that gate.

The 2026-06-17 cubic-anisotropy note counts quadratic weights on the
traceless symmetric block only. It is a different carrier. Nothing below
uses its count, its floating-point split, or its lattice harmonic.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-group row reduction of degree-2 polynomials on a declared 3x3 matrix, plus one rational rotation and one directed substitution."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The four quadratic ratios stay unselected. The sign of t stays unselected. Formation site, probability, and rate stay unsupplied. Do not invent a hazard law."
conditional_surface_status: "a real 3x3 matrix with the signed-permutation action, and the directed coefficient pattern for the restriction"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

Admissibility requires covariance under proper cubic rotations. It does not
name a gravitational source or an action. The calculation starts only after
the matrix and the action are declared. Let `T` be a real `3×3` matrix. A
signed permutation `R`, with row `i` carrying sign `s_i` in column `σ(i)`,
acts by

```text
(R·T)_ij = s_i s_j T_σ(i)σ(j).
```

That is the Bloch-frame rule `T -> R T R^T` for this class of matrices. The
directed pattern, used only in Theorem 3, is

```text
T_xx = T_yy = u,  T_zz = v,  T_xy = -t,  T_yx = t,
```

with every other off-diagonal entry `0`. Declaring that pattern does not
identify it with the admissibility distribution.

Searches of `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
did not find this four-channel count. The queries are recorded in the loop
portfolio. The cubic-anisotropy note stays on the traceless symmetric block.
A dilute-thermodynamics note uses different pair amplitudes in a different
Hamiltonian.

## Definitions

Let `G` be the determinant-`+1` signed permutations, and let `H` be all
`48` signed permutations. The generators used for the closure are

```text
R_z = [[ 0, -1, 0],
       [ 1,  0, 0],
       [ 0,  0, 1]],
R_x = [[ 1,  0,  0],
       [ 0,  0, -1],
       [ 0,  1,  0]].
```

Write `tr = T_xx + T_yy + T_zz` and

```text
Q_trace = tr^2,
Q_diag  = (3 T_xx - tr)^2 + (3 T_yy - tr)^2 + (3 T_zz - tr)^2,
Q_sym   = (T_xy + T_yx)^2 + (T_xz + T_zx)^2 + (T_yz + T_zy)^2,
Q_anti  = (T_xy - T_yx)^2 + (T_xz - T_zx)^2 + (T_yz - T_zy)^2.
```

`Q_diag` is `9` times the sum of squares of the traceless diagonal entries.
On a symmetric matrix, `Q_sym` is `4` times the sum of squares of the three
upper off-diagonal entries.

## Theorem 1 — four quadratic channels, and no fifth

**Conclusion.** `G` has order `24` and equals the closure of `{R_z, R_x}`.
`H` has order `48`. The quadratic polynomials invariant under `G` are the
same `4`-dimensional space as those invariant under `H`. A basis is
`Q_trace`, `Q_diag`, `Q_sym`, `Q_anti`.

**Proof.** Both generators lie in `G`. Comparing the closure with the
`3! 2^3 = 48` signed permutations, split by determinant, gives the two
orders. The reflection `P = diag(1,-1,1)` has determinant `-1`, so it lies
in `H` and not in `G`.

Each of the four polynomials is invariant under every element of `H`. A
signed permutation permutes the diagonal entries, because
`(R·T)_ii = T_σ(i)σ(i)`. It therefore preserves `tr` and `Q_diag`. The same
formula multiplies both `T_ij + T_ji` and `T_ij - T_ji` by `s_i s_j` and
permutes the three unordered pairs, so it preserves `Q_sym` and `Q_anti`.

The four polynomials are linearly independent. On `I` the values are
`9, 0, 0, 0`. On `diag(1,-1,0)` they are `0, 18, 0, 0`. On the matrix with
`T_xy = T_yx = 1` and the other entries `0` they are `0, 0, 4, 0`. On the
matrix with `T_xy = 1`, `T_yx = -1`, and the other entries `0` they are
`0, 0, 0, 4`.

For the matching upper bound, the `45` monomials `T_ab T_cd` with the pair
of entries ordered are the coordinate space. Invariance under `G`, and
separately under `H`, is a homogeneous linear system on those coordinates.
Exact row reduction over the rationals gives a nullspace of dimension `4`
in both cases. An invariant space of dimension `4` that contains four
independent invariants has those invariants as a basis. In particular,
invariance under `G` does not leave an extra polynomial that changes under
`P`.

The square of the single entry `T_xx` is not invariant: `R_z` swaps it
with `T_yy`. The product of the `xy` symmetric sum and the `xy`
antisymmetric difference is not invariant either. `R_z` sends
`T_xy + T_yx` to its negative and fixes `T_xy - T_yx`, so that product
changes sign. The dimension count says no other cross term replaces it.

The same row reduction on linear forms, kept as a check and not used as a
lemma, gives a `1`-dimensional invariant space spanned by the trace. That
agrees with the correlation block of the bond-invariants nullspace. It is
not a new selection of a source coefficient.

## Theorem 2 — one rational rotation fixes the middle ratio

**Conclusion.** Let `S = diag(1,-1,0)` and let

```text
R = [[ 3/5, -4/5, 0],
     [ 4/5,  3/5, 0],
     [ 0,    0,   1]].
```

Then `R` is a rotation and not a signed permutation. `Q_diag(S) = 18` and
`Q_sym(S) = 0`, while `Q_diag(R S R^T) = 882/625` and
`Q_sym(R S R^T) = 2304/625`. The nonzero pairs `(α, β)` for which
`α Q_diag + β Q_sym` takes the same value on `S` and on `R S R^T` are
exactly those with `β/α = 9/2`. That ratio is the combination
`Q_diag/9 + Q_sym/2`, and both matrices give it the value `2`.

**Proof.** `det R = (9+16)/25 = 1` and `R R^T = I`. The entry `-4/5` is not
in `{-1, 0, 1}`, so `R` is not in `H`.

`R^T` is the transpose displayed by swapping the off-diagonal pair. Then
`S R^T` has rows `(3/5, 4/5, 0)`, `(4/5, -3/5, 0)`, and `0`. Multiplying by
`R` gives

```text
row 0 = (3/5)(3/5, 4/5, 0) + (-4/5)(4/5, -3/5, 0)
      = (-7/25, 24/25, 0),
row 1 = (4/5)(3/5, 4/5, 0) + (3/5)(4/5, -3/5, 0)
      = (24/25, 7/25, 0),
row 2 = 0.
```

With trace `0`, `Q_diag` on that image is
`2 (21/25)^2 = 882/625`. `Q_sym` is `(48/25)^2 = 2304/625`. Equality of
`α Q_diag + β Q_sym` on the two matrices is

```text
18 α = α (882/625) + β (2304/625).
```

Hence `α (10368/625) = β (2304/625)`. If `α = 0`, then `β = 0`.
Otherwise `β/α = 10368/2304 = 9/2`.
The combination `Q_diag/9 + Q_sym/2` has that ratio. On a symmetric
traceless matrix it equals the sum of squares of all entries, counting
each off-diagonal pair twice, which is `2` for `S` and for its image.

Proper-cubic invariance alone does not force this ratio. Theorem 1 keeps
`Q_diag` and `Q_sym` as independent invariants of `G`.

## Theorem 3 — the directed pattern sees three channels, and not the sign

**Conclusion.** On the directed pattern,

```text
Q_trace = (2u + v)^2,
Q_diag  = 6 (u - v)^2,
Q_sym   = 0,
Q_anti  = 4 t^2.
```

Every `G`-invariant quadratic therefore restricts to
`α (2u+v)^2 + 6 β (u-v)^2 + 4 δ t^2`. The coefficient of `Q_sym` does not
appear. Replacing `t` by `-t` changes none of the four basis polynomials.
At the two pure twists `u = 0`, `v = -1`, `t = ±1`, the four values are
`1`, `6`, `0`, and `4` for both signs.

**Proof.** Substitute the pattern. `tr = 2u+v`. Then
`3u - tr = u-v` and `3v - tr = -2(u-v)`, so
`Q_diag = 2(u-v)^2 + 4(u-v)^2 = 6(u-v)^2`. The symmetric `xy` sum is
`-t + t = 0` and the other symmetric sums are `0`, so `Q_sym = 0`. The
antisymmetric `xy` difference is `-t - t = -2t`, so `Q_anti = 4 t^2`.
These are even polynomials in `t`. Theorem 1 says every invariant
quadratic is a linear combination of the four, and the combination
restricts as stated. The pure-twist values are the same substitution at
those three numbers.

`Q_sym` is not the zero polynomial. On the matrix with `T_xy = T_yx = 1`
it equals `4`. The directed family simply does not meet that matrix.

## What this does not do

- It does not derive a formation site, probability, rate, or clock.
- It does not show that the admissibility distribution is this matrix.
- It does not select the four channel coefficients.
- It does not identify the trace, or any channel, with a mass density or
  with a gravitational field equation.
- It does not supply the derivative-dependent action left open by the
  cubic-anisotropy note.
- It does not recompute a CHSH square, a partial trace, or a readout
  weight. An antisymmetric coordinate weight can see the sign of `t`.
  These scalars do not.
- It does not evaluate a polynomial of degree above `2`, a functional of
  several bonds, or a matrix that is not `3×3`.

## No-Go Discipline Gate

Scoped claim: every quadratic polynomial invariant under `G` is a
combination of the four channels; on the directed pattern that combination
is even in `t` and independent of the symmetric-off-diagonal coefficient.
A claim that every functional misses the sign, or that covariance selects
a physical action, is not made.

N1. Five attacks on that scoped claim:

1. Let a cross term between the symmetric and antisymmetric off-diagonal
   sums see the sign of `t`. Theorem 1 records that `R_z` changes the sign
   of their `xy` product, and that the invariant dimension is `4`.
   `ATTEMPTED`.
2. Let `Q_sym` be nonzero on the directed pattern. Theorem 3 substitutes
   and gets `0`. `ATTEMPTED`.
3. Let the `3-4-5` rotation lie in `G`, so that it would not remove a
   cubic ratio. Its entries are not signs or zero. `ATTEMPTED`.
4. Let `P` preserve a quadratic that distinguishes `t` from `-t`. Every
   basis polynomial is invariant under all `48` signed permutations.
   `ATTEMPTED`.
5. Let the three polynomials other than `Q_anti` already span the
   invariants. The matrix with `T_xy = 1` and `T_yx = -1` separates
   `Q_anti`. `ATTEMPTED`.

N2. The matrix and the signed-permutation action are one hypothesis. The
directed pattern is that hypothesis on a coordinate subspace, not a second
wall. The four channels are one linear space. No independent-wall count is
asserted.

N3. Theorems 1–3 were checked against the hidden-condition list in the
discipline note. No phrase on that list occurs in those proofs. The matrix,
the pattern, and the group action are written as hypotheses.

N4. The bond-invariants nullspace, the readout identities, and the
cubic-anisotropy count are not lemmas. Dropping those citations leaves
Theorems 1–3 intact. The generators are written in this note.

N5. "Quadratic invariant" means a degree-`2` polynomial in the nine entries
of one matrix. The directed sentence means the three coefficients `u`, `t`,
and `v` of the pattern above. Neither sentence was tested on a larger
window. The runner prints the dimension, the four directed identities, and
the rotation ratio.

N6. This note does not say that a new axiom is required. The three approved
primitives in the premise registry are not used. Source/action remains an
open gate in the axiom memo. Naming the invariant polynomials inside a
declared matrix does not close that gate.

N7. Steelman, outside this domain: use a functional that is not a
degree-`2` polynomial, or a readout that is not required to be a cubic
scalar. The readout note shows that one antisymmetric weight equals `2t`,
so a universal blindness claim would be false. Those escapes do not put the
sign of `t` into a quadratic invariant of `G`. If the object is not this
matrix, Theorems 1–3 do not apply.

N8. The cubic-anisotropy note's floating-point count on a traceless
symmetric block is not this nine-entry row reduction, and this note does
not reopen that count. The bond note's linear nullspace is the trace check
recorded above, not the quadratic argument.

## Review record

This note does not narrow the bond, square, or readout notes. It counts
degree-`2` scalars of the correlation matrix those notes left uncounted.
The open-gate sentence quoted above is still the axiom text. It is not
given a derivation.

Outstanding at landing: the matrix stays declared; the four ratios stay
unselected; the sign of `t` stays unselected; formation site, probability,
and rate stay unsupplied; the derivative-dependent action stays unproved;
independent audit has not reviewed this note. No helper runner is declared.

The hand multiplication and the directed substitution were written before
the matching runner lines. The author re-ran two load-bearing mutations on
scratch copies; each exited nonzero, and the copies were not kept.

- Replacing the antisymmetric difference by a sum fails four checks.
- Demanding that the directed antisymmetric channel equal `t^2` rather
  than `4 t^2` fails the identity check.

## Runner

`scripts/directed_bond_quadratic_action_channels_2026_10_09.py` rebuilds
the closure, compares it with the signed permutations, row-reduces the
quadratic invariance systems, evaluates the four polynomials on the four
sample matrices and on the rotated pair, and substitutes the directed
pattern symbolically. It reads no external scientific input. The linear
trace check is printed and is not a step in Theorems 1–3.
