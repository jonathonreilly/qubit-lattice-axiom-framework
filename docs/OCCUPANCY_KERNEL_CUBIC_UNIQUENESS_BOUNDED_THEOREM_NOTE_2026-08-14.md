---
claim_id: occupancy_kernel_cubic_uniqueness_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Linear maps from 6-NN occupancy bits to R^3 that intertwine proper cube rotations with the standard 3 are exactly the scalar multiples of n_μ = c_{+μ} − c_{-μ}. The even combination s_μ = c_{+μ} + c_{-μ} is not the standard 3. This is uniqueness of the displayed L0 kernel, not a new extra, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/occupancy_kernel_cubic_uniqueness_2026_08_14.py
---

# Unique Cubic-Equivariant Occupancy Kernel

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact linear-algebra uniqueness over `Q` for maps
`{0,1}^6 → Q^3`. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/occupancy_kernel_cubic_uniqueness_2026_08_14.py`](../scripts/occupancy_kernel_cubic_uniqueness_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Six occupancy bits `c_{+x}, c_{-x}, c_{+y}, c_{-y}, c_{+z}, c_{-z}`.
A linear map `A: Q^6 → Q^3` is proper-cubic-equivariant when
`A(g·c) = R(g) A(c)` for proper cube rotations `R(g)`.

The solution space is one-dimensional: `n_μ = α (c_{+μ} − c_{-μ})`.
The even combination `s_μ = c_{+μ} + c_{-μ}` fails the standard
`3`. The displayed `L0` kernel is that unique line.

This is still a comparator fact, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Q uniqueness of the cubic-equivariant linear occupancy kernel."
trace_class: frontier_discovery
target_claim_id: occupancy_kernel_cubic_uniqueness
target_blocker_text: "L0 kernel is one of many linear maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for linear maps on six occupancy bits"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name `n_μ`.

## Theorem 1 — `n` is equivariant

`n_μ = c_{+μ} − c_{-μ}` satisfies `n(g·c) = R(g) n(c)` for `90°`
about `z` and about `x`, on all `64` occupancy tuples.

## Theorem 2 — `s` is not the standard `3`

`s_μ = c_{+μ} + c_{-μ}` fails `s(g·c) = R(g) s(c)` for `90°`
about `z`.

## Theorem 3 — Hom is one-dimensional

The `18` coefficients of a linear map `Q^6 → Q^3`, subjected to
the two generators, have a `1`-dimensional solution space spanned
by `n`.

## Theorem 4 — not a TOE

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “`s` is equivariant” must fail.
2. Predicate “solution space has dimension `2`” must fail.
3. Predicate “note adopts the kernel as axiom text” must fail.

Identity gates: `n0(c)`, `rotate_z(c)`, `equivariant_dimension()`.

## Honest-auditor / Boundary

Finite linear algebra over `Q` on six bits. This note authors no
audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No dynamics.
- Qubit remains `M_2(C)`.
