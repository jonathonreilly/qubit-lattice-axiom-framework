---
claim_id: s4_faithful_so3_conjugacy_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Let G be the 24 signed-permutation 3x3 matrices of det=+1. The space-diagonal map phi: G -> S_4 is an isomorphism. A 90-degree rotation about x is an odd 4-cycle, so 3' = 3 tensor sgn does not land in SO(3). Every inner automorphism of this S_4 is conjugation by a unique element of G. No classification of all order-24 subgroups of SO(3) is used, and no Aut(M_2) action is adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/s4_faithful_so3_conjugacy_2026_08_14.py
---

# Faithful `S_4` Images In This `SO(3)` Frame Are `G`-Conjugate

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact identities for the 24-element group `G` of `3 × 3`
signed permutation matrices with `det = +1`, its space-diagonal
isomorphism to `S_4`, the exclusion of `3'`, and conjugacy of the
inner automorphisms inside `G`. No physical force law and no axiom
edit are asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/s4_faithful_so3_conjugacy_2026_08_14.py`](../scripts/s4_faithful_so3_conjugacy_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `G` for the `3 × 3` signed permutation matrices of determinant
`+1`. This is the proper cube rotation group on this coordinate frame.
The four space diagonals give an isomorphism `φ: G → S_4`.

A 90° rotation about the `x`-axis is an odd 4-cycle on those
diagonals. The other 3-dimensional irrep `3' = 3 ⊗ sgn` would send
that rotation to `−R`, which has determinant `−1` and is therefore
not in `SO(3)`. Every injective homomorphism of this `S_4` into
`SO(3)` that lands in the signed-permutation frame therefore uses
the standard `3`, not `3'`.

For every `σ ∈ S_4` there is a unique `g ∈ G` — namely
`g = φ^{-1}(σ)` — such that

```text
φ(g x g^{-1}) = σ φ(x) σ^{-1}
```

for all `x ∈ G`. So every inner automorphism of this `S_4` is
conjugation by an element of `G`. Two diagonal-label identifications
of `S_4` with `G` therefore differ by an inner automorphism of `G`.

This does not classify all finite subgroups of `SO(3)`. It does not
force a faithful action on `M_2`. It does not pick an Aut element of
the SWAP corner.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact enumeration of G and of the inner automorphisms realized by conjugation in G."
trace_class: frontier_discovery
target_claim_id: s4_faithful_so3_conjugacy
target_blocker_text: "conjugacy of faithful cube actions imported a false SO(3) subgroup sentence"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed signed-permutation frame"
hypothetical_axiom_status: "not proposed"
admitted_observation_status: null
next_trace_action: "independent audit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Those sentences name proper cubic rotations and the one-site algebra.
They do not name `S_4`, `3'`, or a conjugacy class of actions on `M_2`.

## Theorem 1 — `G` is the signed-permutation frame

There are exactly 24 signed permutation matrices of determinant `+1`.
They form a group under multiplication.

## Theorem 2 — space-diagonal map is an isomorphism

`φ` sends `R` to the permutation of the four space diagonals
`±(1,1,1)`, `±(1,1,−1)`, `±(1,−1,1)`, `±(1,−1,−1)`. It is a
homomorphism, its kernel is `{I}`, and it is therefore bijective.

## Theorem 3 — `3'` does not land in `SO(3)`

The 90° rotation `R(x,y,z)=(x,−z,y)` lies in `G`. Its diagonal
permutation is a 4-cycle, hence odd. `3'(R) = −R` has determinant
`−1`.

## Theorem 4 — inner autos are conjugations in `G`

For each `σ` in the image of `φ`, conjugation by `φ^{-1}(σ)`
realizes `Ad_σ` on the labels, and no other element of `G` does.

## Honest-auditor / Boundary

The signed-permutation frame is the theorem domain. This note
authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- A faithful action is not forced.
- No Aut-selection of the SWAP corner.
- No classification of all order-24 subgroups of `SO(3)`.
