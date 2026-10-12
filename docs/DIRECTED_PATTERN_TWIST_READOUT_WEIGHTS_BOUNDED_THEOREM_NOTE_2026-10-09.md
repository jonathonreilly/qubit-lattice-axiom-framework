---
claim_id: directed_pattern_twist_readout_weights_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Conditional on one pair being a density on C^2 tensor C^2 whose real Pauli coefficients lie in the declared directed pattern: local Bloch numbers p and q, longitudinal correlation v, transverse correlation u, and twist t. The wing-1 reduction is (I+q Z)/2 and the wing-2 reduction is (I+p Z)/2. Every local projective Born weight is (1 ± q n_z)/2 or (1 ± p n_z)/2 and does not depend on u, t, or v. A joint coordinate weight matrix W contracts to u(W_xx+W_yy)+v W_zz+t(W_yx-W_xy). It is independent of t exactly when W_xy=W_yx, and the antisymmetric choice W_yx=1, W_xy=-1 equals 2t. The improper reflection diag(1,-1,1) has determinant -1 and sends the pattern to the pattern with t replaced by -t. The two positive pure twists t=±1, u=0, v=-1, p=q=0 are separated by that readout, with values +2 and -2, and are not separated by the local weights. The axioms do not supply the density, the projective instrument, or a choice of t. No CHSH square is recomputed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/directed_pattern_twist_readout_weights_2026_10_09.py
---

# Directed-pattern readout weights miss the twist unless the joint weight is antisymmetric

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/directed_pattern_twist_readout_weights_2026_10_09.py`](../scripts/directed_pattern_twist_readout_weights_2026_10_09.py)

**Parents:** the pattern and the matrix `T` are the ones in
[`DIRECTED_STABILIZER_SIX_PARAMETER_CHSH_MAXIMUM_BOUNDED_THEOREM_NOTE_2026-10-09.md`](DIRECTED_STABILIZER_SIX_PARAMETER_CHSH_MAXIMUM_BOUNDED_THEOREM_NOTE_2026-10-09.md).
That note states that a one-site reduction is not tested. This note tests
the reductions and the coordinate weights. It does not recompute a CHSH
square. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply proper
cubic rotations, the one-site algebra `M_2(C)`, and content-determined
readout. They do not supply this density or a choice of readout weights.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact partial traces, a nine-entry weight contraction, and one improper conjugation, all on a declared coefficient pattern."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "It does not derive the dynamics clause, the trace rule, the menus or how settings are chosen."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The sign of t stays unselected. Formation site, probability, and rate stay unsupplied. Do not invent a hazard law."
conditional_surface_status: "two-qubit density of the directed pattern, plus a supplied projective or coordinate-weight readout"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

Admissibility requires covariance under proper cubic rotations and says the
distribution over possibilities is determined by the nearest-neighbor
conditions. Reading note (2) in
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) still says that distribution
does not supply the formation site, probability, or rate. The open-gate
list still names Born weight values and measurement-basis selection as
outside the axioms. This note does not fill either gap, and it does not
invent a transition or hazard law.

The calculation starts only after two declared hypotheses. The pair is a
density of the parent pattern, and a readout is either a local projective
instrument `n·σ` or a real `3×3` weight matrix on the coordinate correlators.
Neither hypothesis is an axiom.

Searches of `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
did not find this split. The September handed-rule census evaluates a
six-letter menu, not this density. The Moriya note evaluates a supplied
dynamics-clause ground state, not these coefficients. The parent CHSH note
on this branch absorbs `t` into `r^2` for the square and does not reduce
the state.

## Definitions

Let `H = 4ρ` be

```text
I⊗I + q Z⊗I + p I⊗Z + u X⊗X + u Y⊗Y + t Y⊗X - t X⊗Y + v Z⊗Z.
```

The correlation matrix of the parent note is

```text
T = [[ u, -t, 0],
     [ t,  u, 0],
     [ 0,  0, v]].
```

A coordinate weight matrix `W = (W_ab)` defines the joint statistic
`Σ_{a,b} W_ab ⟨(e_a·σ) ⊗ (e_b·σ)⟩`. A same-direction weight is the special
case `W = a a^T` for some `a in R^3`. Let

```text
P = diag(1, -1, 1).
```

## Theorem 1 — local projective weights miss the twist

**Conclusion.** The wing-1 reduction is `(I + q Z)/2`. The wing-2 reduction
is `(I + p Z)/2`. For a unit vector `n`, the Born weight of eigenvalue `+1`
is `(1 + q n_z)/2` on wing 1 and `(1 + p n_z)/2` on wing 2. Both weights
are independent of `u`, `t`, and `v`. In particular they take the same
value at `t` and at `-t`.

**Proof.** `Tr_2(A⊗B) = A Tr(B)` and `Tr_1(A⊗B) = Tr(A) B`. Here
`Tr(I) = 2` and `Tr(X) = Tr(Y) = Tr(Z) = 0`, so every two-body term has
partial trace zero. The remaining terms are

```text
Tr_2(H) = 2 I + 2 q Z,    Tr_1(H) = 2 I + 2 p Z.
```

Dividing by `4` gives the two reductions. The Bloch vectors are `(0,0,q)`
and `(0,0,p)`, so `⟨n·σ⟩` is `q n_z` or `p n_z`. The eigenvalue-`+1`
weight of a projective instrument is `(1 + ⟨n·σ⟩)/2`. Replacing `t` by
any other value does not change `H`'s one-body part, so the reductions
are unchanged. Positivity of `ρ` is not used.

## Theorem 2 — which joint weights see the twist

**Conclusion.** The nine coordinate correlators are the entries of `T`.
For every real weight matrix,

```text
Σ W_ab E(e_a, e_b) = u (W_xx + W_yy) + v W_zz + t (W_yx - W_xy).
```

The statistic is independent of `t` exactly when `W_xy = W_yx`. The choice
`W_yx = 1`, `W_xy = -1`, and all other entries zero, equals `2t`. For every
`a in R^3`,

```text
a^T T a = u (a_x^2 + a_y^2) + v a_z^2,
```

which does not contain `t`.

**Proof.** The operator definition gives
`⟨X⊗X⟩ = ⟨Y⊗Y⟩ = u`, `⟨Z⊗Z⟩ = v`, `⟨X⊗Y⟩ = -t`, `⟨Y⊗X⟩ = t`, and the four
correlators that use one `z` and one transverse axis are zero. Those nine
numbers are the entries of `T`, so the contraction is the displayed linear
form. The coefficient of `t` vanishes exactly when `W_xy = W_yx`. The
named antisymmetric choice has coefficient `1 - (-1) = 2`.

Write `T = S + t J` with `S` symmetric and

```text
J = [[0, -1, 0],
     [1,  0, 0],
     [0,  0, 0]].
```

Then `a^T J a = 0` because `J^T = -J`, and `a^T S a` is the quadratic
polynomial above.

## Theorem 3 — one improper reflection flips only the twist

**Conclusion.** `det P = -1` and `P^2 = I`. The bond-invariants note's
group `G` is the set of determinant-`+1` signed permutations, so `P` is
not in `G`.
Conjugation replaces the pattern `(u, t, v)` by `(u, -t, v)`. At the two
points `(u, t, v) = (0, ±1, -1)`, with `p = q = 0`, `H` has spectrum
`0,0,0,4`, and the antisymmetric readout of Theorem 2 equals `+2` and
`-2` respectively. The local weights of Theorem 1 equal `1/2` at both
points.

**Proof.** `P` is diagonal, so `(P T P)_ij = P_ii T_ij P_jj`. The
transverse off-diagonal entries change sign and the diagonal entries do
not, which is the substitution `t ↦ -t`. The determinant computation is
the product of the diagonal entries. Theorem 1 of
[`PROPER_CUBIC_TWO_QUBIT_BOND_INVARIANTS_BOUNDED_THEOREM_NOTE_2026-10-09.md`](PROPER_CUBIC_TWO_QUBIT_BOND_INVARIANTS_BOUNDED_THEOREM_NOTE_2026-10-09.md)
identifies `G` with the determinant-`+1` signed permutations. This note
uses that identification and does not recompute the order of `G`. The
conjugation identity does not use it.

At either pure twist, `r^2 = 1` and `v = -1`. The computational
eigenvalues of `H` are `1 + v = 0` twice. The transverse block has
eigenvalues `1 - v ± 2 = 2 ± 2`, hence `4` and `0`. All four are
nonnegative. Theorem 2 then gives the readouts `2t = ±2`. Theorem 1 gives
the local weights `1/2` because `p = q = 0`.

## What this does not do

- It does not derive a formation site, probability, rate, or clock.
- It does not show that the admissibility distribution is this density.
- It does not select `t`, or any other coefficient.
- It does not derive Born weights. The projective instrument is supplied,
  and even then its weights do not see `t`.
- It does not derive a transition weight or a hazard law.
- It does not recompute a CHSH square or the parent's nullspace.
- It does not evaluate a POVM, a readout of a larger window, or an
  instrument whose value depends on both records except through `W`.
- It does not say that the framework's rule is handed. Both signs of `t`
  remain inside the pattern.

## No-Go Discipline Gate

Scoped claim: on this pattern, no local projective Born weight depends on
`t`, and no symmetric coordinate weight separates `t` from `-t`. The
antisymmetric coordinate weight does separate them, by `2t`. A claim that
every conceivable readout misses `t`, or that the physical rule is chiral,
is not made.

N1. Five attacks on the scoped blindness:

1. Let a two-body term change a one-site reduction. Theorem 1 uses
   `Tr(X) = Tr(Y) = Tr(Z) = 0`. `ATTEMPTED`.
2. Let the pattern hide an `x` or `y` Bloch component. Its one-body terms
   are only `q Z⊗I` and `p I⊗Z`. `ATTEMPTED`.
3. Let a same-direction weight `a a^T` see `t`. Theorem 2 uses
   `a^T J a = 0`. `ATTEMPTED`.
4. Let `W_xy = W_yx` still produce a nonzero coefficient of `t`. That
   coefficient is the difference of those two entries. `ATTEMPTED`.
5. Let `P` preserve `t`. Theorem 3 replaces `t` by `-t`, and the two
   patterns differ by `2t` in the antisymmetric readout. `ATTEMPTED`.

N2. The density and the coefficient pattern are one hypothesis. The
projective instrument and the weight matrix are readout conventions on
that hypothesis, not a second wall under the partial-trace identity.
Symmetric and antisymmetric weights are the two sides of one linear
coefficient. No independent-wall count is asserted.

N3. Theorems 1–3 were checked against the hidden-condition list in the
discipline note. No phrase on that list occurs in those proofs. The
density, the pattern, and the readout convention are written as hypotheses.

N4. The parent CHSH note's residual is that a one-site reduction was not
tested. That is the residual filled here, and its CHSH theorems are not
lemmas. The handed-rule census and the Moriya note name other objects.
Dropping both citations leaves Theorems 1–3 intact. The only external
identification used inside a proof is the bond-invariants description of
`G` in Theorem 3, and the conjugation identity does not need it.

N5. "Local projective weights do not depend on `t`" means both wings of
one bond and the three axes `x, y, z`. "Symmetric coordinate weights do
not separate `t` from `-t`" means one `3×3` weight matrix on that same
bond. Neither sentence was tested on a larger neighborhood or on an
infinite lattice. The runner prints those five resolutions.

N6. This note does not say that a new axiom is required. The three
approved primitives in the premise registry are not used. Born weight
values remain an open gate in the axiom memo; calculating them inside a
supplied instrument does not close that gate.

N7. Steelman, outside this domain: drop the projective restriction and
read the pair with a joint instrument. Theorem 2 says the antisymmetric
weight then sees `t`, so the blindness claim would be false if it were
stated for every readout. Drop the density and the calculation does not
apply. Those escapes do not put `t` into a local projective weight of
this pattern. The sign of `t` stays unselected.

N8. The parent's square depends on `t` only through `u^2 + t^2`. That
Gram fact is not the partial-trace argument, and this note does not reopen
the square. The September census already has scalar-blind witnesses on a
different alphabet; its proof is not a mechanism that retires the
coefficient calculation here.

## Review record

This note does not narrow the parent CHSH note. It fills the one-site
reduction that the parent left untested, and it classifies coordinate
weights. The formation sentence quoted above is recorded as still present.
It is not given a new derivation.

Outstanding at landing: the density hypothesis stays open; the projective
instrument stays supplied; `t` stays unselected; formation site,
probability, and rate stay unsupplied; independent audit has not reviewed
this note. No helper runner is declared.

## Runner

`scripts/directed_pattern_twist_readout_weights_2026_10_09.py` rebuilds
`H` from Pauli products, reduces both wings, compares the nine operator
correlators with `T`, evaluates symmetric and antisymmetric weights, and
conjugates `T` by `P`. The pure twists are checked by the four-eigenvalue
list, not by a CHSH square. The author re-ran two load-bearing mutations
on scratch copies; each exited nonzero. Those copies were not kept.

- Subtract `⟨Y⊗X⟩` from `⟨X⊗Y⟩` instead of the reverse: the `2t` check fails.
- Demand that the wing-1 Bloch number equal `p` rather than `q`: the
  reduction check fails.
