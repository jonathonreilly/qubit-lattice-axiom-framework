---
claim_id: m3_does_not_embed_in_one_site_m2_color_algebra_is_extra_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The trial color algebra A3 = M_3(C) is nine-dimensional over C. The one-site axiom algebra A2 = M_2(C) is four-dimensional over C. There is therefore no injective C-linear map A3 → A2, and in particular no injective *-homomorphism. Qubit names M_2(C) and does not name M_3(C) or SU(3). A color algebra is an extra displayed object of dimension at least 9, not an axiom and not QCD. The result does not retire June 10, does not identify N_p with ln Z_L, does not import 0.5934, does not force r=1/2, and does not claim a later multi-site tensor obstruction."
upstream_dependencies:
  - minimal_axioms
runner: scripts/m3_does_not_embed_in_one_site_m2_color_algebra_is_extra_2026_08_13.py
---

# `M_3(C)` Does Not Embed In One-Site `M_2(C)`; A Color Algebra Is Extra

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact complex dimensions of the one-site axiom algebra and a
displayed trial color algebra. No QCD import. No axiom edit.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/m3_does_not_embed_in_one_site_m2_color_algebra_is_extra_2026_08_13.py`](../scripts/m3_does_not_embed_in_one_site_m2_color_algebra_is_extra_2026_08_13.py)
**Parents:** the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write

```text
A2 = M_2(C)     dim_C(A2) = 4
A3 = M_3(C)     dim_C(A3) = 9
```

for the full one-site possibility algebra named by Qubit, and for a displayed
trial color algebra. The integer comparison `9 > 4` is exact. There is no
injective `C`-linear map `A3 → A2`, hence no injective unital `*`-homomorphism.
Qubit names `M_2(C)` and does not name `M_3(C)` or `SU(3)`. A color algebra is
therefore extra: at least a nine-dimensional unital `*`-algebra, equivalently
displayable as operators on a `C^3` Hilbert space. This note displays `A3`. It
does not adopt a color axiom and does not identify `A3` with QCD.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer dimensions of M_2(C) and M_3(C) give a one-site linear-injection obstruction. Multi-site tensors, later color constructions, June 10 objects, and QCD identification remain outside the claim."
trace_class: negative_route_pruning
target_claim_id: one_site_m2_does_not_host_m3_color_algebra
target_blocker_text: "decide whether a color algebra injects into the one-site Qubit algebra"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for one-site C-linear and *-algebra injection; multi-site tensors remain open"
hypothetical_axiom_status: "A3 is displayed only; no color axiom is adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `M_n(C)` be the unital `*`-algebra of `n × n` complex matrices, with the
standard adjoint. As a complex vector space it has the matrix-unit basis

```text
{ E_{ij} : 1 <= i,j <= n }
```

so the exact integer dimension is

```text
dim_C(M_n(C)) = n^2.
```

The one-site algebra is the Qubit presentation

```text
A2 := M_2(C),    dim_C(A2) = 2^2 = 4.
```

The displayed trial color algebra is

```text
A3 := M_3(C),    dim_C(A3) = 3^2 = 9.
```

Equivalently, `A3 ≅ B(C^3)` as a unital `*`-algebra, so the same extra object
may be displayed as a three-dimensional complex Hilbert space. Neither display
is an axiom.

The Qubit sentence used below is the current axiom-memo wording, quoted
verbatim:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

That sentence does not name `M_3(C)` and does not name `SU(3)`.

## Theorem 1 — No One-Site Linear Injection

There is no injective `C`-linear map `A3 → A2`.

**Proof.** Any injective linear map of finite-dimensional vector spaces
satisfies `dim(domain) ≤ dim(codomain)`. The dimensions are the exact integers
`9` and `4`. The comparison `9 ≤ 4` is false, so no such injection exists.

In particular there is no injective unital `*`-homomorphism `A3 → A2`: every
unital `*`-homomorphism of these matrix algebras is `C`-linear.

The same comparison is the required mutation predicate. The statement
`dim_C(M_3(C)) ≤ dim_C(M_2(C))` is the false integer predicate `9 ≰ 4`.

## Theorem 2 — Qubit Names `M_2(C)` Only

The current Qubit axiom states that the full one-site possibility domain has
algebraic presentation `M_2(C)`. It does not name `M_3(C)` and does not name
`SU(3)`. The one-site algebra available as axiom content is therefore `A2`,
not `A3`.

This is a quotation of the axiom memo, not an axiom edit.

## Theorem 3 — A Color Algebra Is Extra

Any algebra isomorphic to `A3` is extra relative to one-site Qubit content.
The extra object is at least a nine-dimensional unital `*`-algebra, or a
`C^3` Hilbert space on which that algebra acts. This note displays `A3`.

The note does not adopt a color axiom. It does not identify `A3` with QCD,
does not import a QCD Lagrangian, gauge coupling, or confinement statement,
and does not treat `SU(3)` as axiom content.

## Theorem 4 — June 10 Is Not Retired

This dimension comparison does not retire June 10. The objects `N_p` and
`ln Z_L` are different: `N_p` is a plaquette count, while `ln Z_L` is a
finite-volume log partition function. They are not identified here.

The number `0.5934` is not used, not imported, and not derived.

## Theorem 5 — No Forced `r = 1/2` And No Multi-Site Claim

This note does not force `r = 1/2`.

The obstruction is one-site. For a multi-site tensor `A2^{⊗k}` one has the
exact integer dimension `4^k`, which already exceeds `9` at `k ≥ 2`. Dimension
counting on one site therefore does not claim that a color algebra is
impossible later on a multi-site tensor.

## Explicit Non-Claims

- No axiom is edited, added, or proposed.
- No color axiom is adopted.
- `A3` is displayed, not identified with QCD.
- Unmerged work, including independent carrier and composition lanes, is not
  cited and is not a parent.
- June 10 is not retired. `N_p` is not `ln Z_L`. The value `0.5934` is not
  imported.
- `r = 1/2` is not selected.
- A later multi-site or composite construction is not ruled out.

## Runner Contract

The companion runner checks exact integer dimensions through the identity
gates `dim_m2()` and `dim_m3()`, rejects the mutation predicate
`dim M_3 ≤ dim M_2`, quotes the Qubit sentence, and records the non-claims
above. Declared audit inputs are this note and the axiom memo only.
