# Wilson Generator-Rescaling Beta Transformation

**Date:** 2026-06-16
**Claim type:** bounded_theorem
**Type:** exact-support bridge inside the supplied standard Wilson plaquette
action surface.
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py`](../scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py)

```yaml
actual_current_surface_status: exact-support
trace_class: support_component_for_prior_blocker
target_claim_id: g_bare_rescaling_freedom_removal_theorem_note_2026-05-03
target_blocker_text: "add a Wilson-action normalization/transformation theorem deriving beta_new/beta_old under T_a -> c T_a"
source_of_blocker_text: audit_ledger
reachability_to_target: supplies_component_only
artifact_role: support_theorem
conditional_surface_status: "The transformation is exact inside the supplied standard Wilson action and canonical trace-normalization surface; Wilson action-surface selection remains outside this note."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true_for_exact_support_only
proposal_allowed_reason: "This note proves only the coefficient transformation under a supplied Wilson action and compensating generator/coupling rescaling; it does not reclassify, close, or promote the older g_bare consumer row."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Purpose

The `g_bare` rescaling audit history named a missing local theorem for the
Wilson-action normalization transformation under a generator rescaling. This
note supplies that component theorem using the already source-proved small-`a`
Wilson matching:
[`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).

It does not derive Wilson action-surface selection, does not derive beta=6,
does not derive g_bare=1, and does not by itself reclassify, close, or promote
any older `g_bare` consumer row.

## Claim

Assume the supplied standard Wilson plaquette action surface and canonical
trace normalization used in
[`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
That theorem gives

```text
beta = 2 N_c / g^2
```

and equivalently

```text
beta g^2 = 2 N_c.
```

Under a scalar generator rescaling

```text
T'_a = c T_a
```

the compensating coupling readout preserving the matrix-valued link exponent
is

```text
g' T'_a = g T_a,
```

so

```text
g'^2 = g^2 / c^2.
```

Applying the same Wilson small-`a` matching theorem to the primed surface gives

```text
beta' = 2 N_c / g'^2 = 2 N_c / (g^2/c^2) = c^2 beta.
```

Therefore

```text
beta' / beta = c^2
```

and

```text
beta' g'^2 = beta g^2 = 2 N_c.
```

This is the requested Wilson-action normalization transformation. It is
ordinary exact algebra once the Wilson small-`a` matching theorem and the
compensating generator/coupling rescaling are fixed.

## Fixed-Beta Consequence

On a fixed canonical Wilson beta surface, a nontrivial generator rescaling is
not invisible. For `c^2 != 1`,

```text
Tr(T'_a T'_b) = c^2 delta_ab / 2
```

and the Wilson-matched coefficient changes by

```text
beta' = c^2 beta.
```

Thus a nontrivial `T_a -> c T_a` does not preserve the same
canonical-normalization plus fixed-beta surface.

## Boundaries

This note does not claim:

- Wilson action-surface selection from the framework axioms;
- exclusion of Symanzik, heat-kernel, Manton, tadpole-improved, or other
  action surfaces;
- beta=6 as a framework-selected value;
- g_bare=1 as a framework-selected value;
- that a noncanonical generator scale is forbidden by this note alone;
- a continuum-limit existence theorem;
- an audit verdict or status promotion for any `g_bare` row.

The theorem is exactly the Wilson coefficient transformation under a supplied
standard Wilson action and a compensating generator/coupling rescaling.

## Downstream Use

This note is an available source authority for a beta-scaling step in any
future beta-routing consumer update, including a possible later repair of
`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`.
The current consumer row remains a Gram-scaling lemma and intentionally does
not consume this note. Canonical trace normalization is supplied by the CL3
color authority, and physical Wilson action-surface selection remains outside
this note.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py
```

Expected:

```text
TOTAL: PASS=83 FAIL=0
```
