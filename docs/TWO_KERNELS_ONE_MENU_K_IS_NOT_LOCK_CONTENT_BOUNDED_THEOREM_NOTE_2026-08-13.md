---
claim_id: two_kernels_one_menu_k_is_not_lock_content_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On one binary menu and one density, the trace kernel and the half-threshold step kernel disagree at the formed lock of content A. Live Record names the lock label A from record content alone, not a kernel number. Neither kernel is named by live Record. A Born number requires a supplied kernel. Both kernels are displayed; neither is adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_kernels_one_menu_k_is_not_lock_content_2026_08_13.py
---

# Two Kernels On One Menu: K Is Not Lock Content

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** one binary menu, one density, two displayed kernels, one formed lock.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_kernels_one_menu_k_is_not_lock_content_2026_08_13.py`](../scripts/two_kernels_one_menu_k_is_not_lock_content_2026_08_13.py)
**Parent:** axiom memo only
([`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)).

## Result Up Front

The same formed lock and the same menu do not pick a kernel. Live Record:

> A readout value is determined by record content alone.

That readout is the lock label `A`, not `3/5` and not `1`. Named `I` is not
axiom content; this note does not write `I(A)=1` as an axiom step. The lock is
`A`.

Two exact kernels on the same pair `ρ`, `P_A` disagree. A Born number
therefore requires a supplied kernel. Both kernels are displayed. Neither is
adopted.

This block is independent of the occupancy-menu-kernel triple (drop `o`,
menu, or kernel one at a time) and of the C1 occupancy-retract ledger. The
hole here is two kernels on one already-formed lock.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Fraction algebra on one menu and one density: two kernels disagree at the lock of content A, and live Record names the label A rather than either kernel value. No axiom edit, no named I, no adopted Born kernel."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "whether a formed lock of content A on a displayed menu already is a Born number"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the declared menu, density, two kernels, and formed lock of content A; no kernel is selected as physical law"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The menu is `{A, B}` with projectors

`P_A = diag(1, 0)`, `P_B = I − P_A`.

The density is

`ρ = diag(3/5, 2/5)`.

The trace kernel is

`K_tr(ρ, P) = Tr(ρ P)`.

So `K_tr(ρ, P_A) = 3/5` and `K_tr(ρ, P_B) = 2/5`.

The step kernel is

`K_step(ρ, P) = 1` if `Tr(ρ P) ≥ 1/2`, else `0`.

So `K_step(ρ, P_A) = 1` and `K_step(ρ, P_B) = 0`.

A formed lock of content `A` is the Record datum. The readout is determined
by record content alone. That value is the label `A`.

## Theorem 1

`K_tr(ρ, P_A) = 3/5 ≠ 1 = K_step(ρ, P_A)`.

Same menu, same `ρ`, same lock label `A`. The two kernels disagree at the
formed lock. Kernel equality is false.

## Theorem 2

Neither kernel is named by live Record. `I` is not axiom content, so this
note does not write `I(A)=1` as an axiom step. The lock is `A`.

The governing Record section of
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
says that records form, lock one admissible possibility, are unique and
permanent, are the only readable objects, and that a readout value is
determined by record content alone. It does not name `Tr(ρ P)`, `K_tr`, or
`K_step`.

## Theorem 3

A Born number requires a supplied kernel. Display both kernels. Do not adopt
either. Do not adopt Born. Do not import Gleason.

## Mutation Predicates

The following predicates fail:

1. `K_tr(ρ, P_A) == K_step(ρ, P_A)`
2. “live memo names `Tr(ρ P)`” as governing Record content

The live Record section of
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
is the text from `### Record / Fixed Reality` through `## Qualification`.
That section contains the content-alone sentence and does not contain
`Tr(ρ P)`.

## What This Does Not Claim

- No axiom is edited.
- Named `I` is not restored as axiom content.
- Neither `K_tr` nor `K_step` is adopted as physical law.
- Born is not adopted and is not claimed false.
- Gleason is not imported.
- Occupancy, a second menu, and a C1 retract of `J` are out of scope.
- The result is a type split between lock content and a supplied kernel, not
  a uniqueness theorem among kernels.
