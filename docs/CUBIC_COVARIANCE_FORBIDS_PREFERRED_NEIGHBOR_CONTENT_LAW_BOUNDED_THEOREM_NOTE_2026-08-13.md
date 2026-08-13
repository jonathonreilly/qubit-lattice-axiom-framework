---
claim_id: cubic_covariance_forbids_preferred_neighbor_content_law_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "A nearest-neighbor content law that reads only the +e3 neighbor is not covariant under a proper cubic rotation, so it is not an Admissibility-shaped law. The result excludes preferred-axis neighbor dependence only. It does not select a unique covariant rule, does not force mu=1/2, does not adopt a law, and does not claim that no later selector exists."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cubic_covariance_forbids_preferred_neighbor_content_law_2026_08_13.py
---

# Cubic Covariance Forbids a Preferred-Neighbor Content Law

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite algebra on six-neighbor content 6-tuples and one
hostile preferred-axis law; no dynamics, no unique-rule selection, and no
axiom edit.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cubic_covariance_forbids_preferred_neighbor_content_law_2026_08_13.py`](../scripts/cubic_covariance_forbids_preferred_neighbor_content_law_2026_08_13.py)

## Result Up Front

Admissibility requires one fixed nearest-neighbor rule that is covariant
under proper cubic rotations. A law that looks only at the `+e3` neighbor is
not that kind of rule.

Fix a site at the origin and a two-letter menu `{A,B}`. A 6-tuple is a map

`n : {±e1, ±e2, ±e3} → {A,B}`

recording the neighbor content in each of the six cubic directions. The
hostile preferred-axis law is

`μ_z(A | n) = 1` if `n(+e3)=A`, else `1/3`.

Those two values are exact `Fraction` assignments of the hostile example.
This note does not force `μ = 1/2`.

The standard 90° rotation about the `x`-axis is the coordinate map

`(x,y,z) ↦ (x, −z, y)`.

It is a proper cubic rotation. Acting on 6-tuples by
`(R·n)(d) = n(R^{-1} d)` moves the `+e3` slot onto a different cubic
direction. There exist 6-tuples `n` and `R·n` with

`μ_z(A|n)=1` and `μ_z(A|R·n)=1/3`.

So `μ_z` is not invariant under `R`. Quoting Admissibility, the rule is
covariant under proper cubic rotations. Therefore `μ_z` is not an
Admissibility-shaped law.

This is a positive constraint: preferred-axis neighbor dependence is
excluded. The note does not adopt a law. It does not select the unique
covariant rule. Many maps that still depend on the full 6-tuple can remain
covariant. The result does not claim that no later selector exists.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The hostile preferred-axis law is exhibited as non-invariant under one proper cubic rotation, using only the current Admissibility covariance sentence. Unique covariant-rule selection, a numerical law, and later selectors remain open."
trace_class: negative_route_pruning
target_claim_id: preferred_neighbor_content_law_forbidden
target_blocker_text: "preferred-axis neighbor dependence is not Admissibility-shaped"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for the displayed hostile law and the displayed rotation; unique-rule selection remains open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e1=(1,0,0)`, `e2=(0,1,0)`, `e3=(0,0,1)` for the standard cubic
generators. The six nearest-neighbor directions at the origin are
`{±e1, ±e2, ±e3}`.

A **content 6-tuple** is a function `n` from that six-element set into the
menu `{A,B}`. No physical identification of `A` or `B` is used. They are
labels.

The **hostile law** `μ_z` assigns, for each 6-tuple `n`,

`μ_z(A | n) = 1` if `n(+e3) = A`, and `μ_z(A | n) = 1/3` otherwise.

Equivalently, `μ_z(B | n) = 0` if `n(+e3)=A`, and `2/3` otherwise. Both
values are exact rationals. The law depends on `n` only through the single
slot `n(+e3)`.

Let `R` be the linear map

`R(x,y,z) = (x, −z, y)`,

with matrix (rows)

```
[[ 1,  0,  0],
 [ 0,  0, -1],
 [ 0,  1,  0]].
```

This is the standard 90° rotation about the positive `x`-axis (right-hand
sense: `e2 ↦ e3` and `e3 ↦ −e2`). The signed image of `+e3` is `−e2`, which
is a neighbor direction on the `e2` axis, not the original `+e3` slot.

The induced action on 6-tuples is

`(R·n)(d) = n(R^{-1} d)`

for each cubic direction `d`. Because `R` is orthogonal, `R^{-1}=R^{T}`.

A law `μ` is **invariant under `R`** when `μ(A | n) = μ(A | R·n)` for every
6-tuple `n`. Admissibility-shaped laws are required to be covariant under
every proper cubic rotation, hence in particular under this `R`.

## Theorem 1 — The Displayed Map Is A Proper Cubic Rotation

`R` satisfies `R^{T} R = I` and `det R = 1`. Explicitly,

`R^{T} = [[1,0,0],[0,0,1],[0,-1,0]]`,

so

`R^{T} R = I`,

and the determinant expansion along the first row is

`det R = det([[0,-1],[1,0]]) = 1`.

`R` permutes the six nearest-neighbor directions:

`R(+e1)=+e1`, `R(−e1)=−e1`, `R(+e2)=+e3`, `R(−e2)=−e3`,
`R(+e3)=−e2`, `R(−e3)=+e2`.

It therefore maps the cubic nearest-neighbor shell to itself and is a
proper cubic rotation about the origin, in the sense of the Lattice axiom
(standard translations and proper cubic rotations about each site).

## Theorem 2 — The Hostile Law Is Not Invariant Under `R`

Let `n` be the 6-tuple with `n(+e3)=A` and `n(d)=B` for every other
direction `d`. Then `μ_z(A | n) = 1` by definition.

The inverse image of the `+e3` slot is

`R^{-1}(+e3) = R^{T}(+e3) = −e2`.

Hence

`(R·n)(+e3) = n(−e2) = B`,

and `μ_z(A | R·n) = 1/3`.

The two values `1` and `1/3` are unequal, so `μ_z` is not invariant under
`R`. The same mismatch is the failure of the predicate “`μ_z` is
cubic-covariant” on this pair `(n, R·n)`.

The constant 6-tuple with every slot equal to `A` is invariant, as is the
constant-`B` 6-tuple. Invariance on a proper subset of 6-tuples is not
covariance of the law.

## Theorem 3 — `μ_z` Is Not An Admissibility-Shaped Law

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

> There is one fixed nearest-neighbor admissibility rule, covariant under
> lattice translations and proper cubic rotations.

The same memo continues that, for each site, the probability distribution
over the possibilities is determined by, and varies with, the
nearest-neighbor conditions.

`μ_z` is a nearest-neighbor content rule on the six-direction shell, but
Theorem 2 shows it fails covariance under the proper cubic rotation `R` of
Theorem 1. Therefore `μ_z` is not an Admissibility-shaped law.

The conclusion uses only the named covariance requirement and the explicit
hostile dependence on the single `+e3` slot. It does not use any unmerged
work, any numerical fit, or any axiom edit.

## Theorem 4 — Preferred-Axis Dependence Is Killed; A Unique Rule Is Not Selected

The argument excludes laws whose value depends on a preferred cubic
direction in the way `μ_z` depends on `+e3`. Any rule that assigns
different probabilities to a 6-tuple and to a proper-cubic rotate of that
6-tuple fails the same test.

The argument does not select a unique covariant rule. Covariance is a
constraint, not a uniqueness theorem. Many maps that still depend on the
full 6-tuple — rather than on one preferred neighbor — can be invariant
under every proper cubic rotation. This note does not enumerate them, rank
them, or adopt one of them.

In particular, this note does not force `μ = 1/2`. The values `1` and
`1/3` belong only to the hostile example. Equal-probability `1/2` is one
covariant candidate on a two-letter menu, not a consequence of killing
`μ_z`. The note does not adopt a law.

## Theorem 5 — A Later Selector Is Not Ruled Out

Nothing here claims that no later selector exists. A subsequent derivation
may still impose further Admissibility-compatible constraints and select a
specific covariant rule, or prove that several covariant rules remain.
Those are later questions. The present theorem only removes
preferred-neighbor content laws from the Admissibility-shaped class.

## What This Does Not Claim

- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not register a primitive and does not import a numerical value.
- It does not identify `{A,B}` with a physical species, Bloch state, or
  record-lock value beyond being a two-letter menu of local possibilities.
- It does not force `μ = 1/2` and does not adopt a law.
- It does not claim uniqueness of the covariant rule.
- It does not claim that no later selector exists.
- It does not cite, depend on, or close any unmerged work.

## Parents

The only parent on `origin/main` is the current axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Runner

[`scripts/cubic_covariance_forbids_preferred_neighbor_content_law_2026_08_13.py`](../scripts/cubic_covariance_forbids_preferred_neighbor_content_law_2026_08_13.py)
checks the exact `Fraction` identities for `R^{T} R = I` and `det R = 1`,
constructs the witness 6-tuple, and evaluates `μ_z` only by calling
`mu_z(n)` and `rotate_x90_tuple(n)`. The mutation predicate “`μ_z` is
cubic-covariant” fails on that witness. All probabilities are exact
`Fraction` values. The runner does not force `μ = 1/2`.
