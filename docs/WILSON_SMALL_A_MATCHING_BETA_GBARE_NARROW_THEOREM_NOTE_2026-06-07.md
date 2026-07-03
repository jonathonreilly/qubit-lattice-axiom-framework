# Wilson Small-a Matching for beta and g_bare

**Date:** 2026-06-07
**Claim type:** bounded_theorem
**Type:** exact-support source theorem under the supplied standard Wilson
plaquette action surface
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py`](../scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py)
**Cached log:**
[`logs/runner-cache/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.txt`](../logs/runner-cache/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.txt)

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
target_claim_id: beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08
target_blocker_text: "derive or register retained-grade authority for the Wilson action-surface matching premise WM"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
conditional_surface_status: "WM is exact inside the supplied standard Wilson plaquette action with canonical trace normalization; selection of that action surface remains outside this note."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true_for_exact_support_only
proposal_allowed_reason: "This note derives only the coefficient matching inside a supplied Wilson action form; it does not derive action-surface selection or g_bare=1."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Purpose

The row
`BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md`
was audited conditional because its arithmetic assumed the Wilson
action-surface matching premise

```text
WM: beta = 2 N_c / g_bare^2.
```

This note supplies the missing coefficient-matching theorem. It proves `WM`
from the supplied standard Wilson plaquette action form and canonical
`su(N_c)` trace normalization. It does not derive that the framework must
select the Wilson action surface, and it does not derive a physical value of
`g_bare`.

## Claim

Let `T_a` be Hermitian `su(N_c)` generators with

```text
Tr(T_a T_b) = delta_ab / 2.
```

Let the plaquette be represented in the standard small-lattice-spacing form

```text
U_P = exp(i a^2 g_bare F^a_{mu nu} T_a + O(a^3)).
```

Use the standard Wilson plaquette action

```text
S_W = beta sum_{x, mu<nu} (1 - (1/N_c) Re Tr U_{mu nu}(x)).
```

Then its leading small-`a` continuum term is

```text
S_W = [beta g_bare^2 / (4 N_c)]
      sum_{x, mu<nu} a^4 F^a_{mu nu}(x) F^a_{mu nu}(x) + higher order.
```

The continuum Yang-Mills kinetic term is

```text
S_YM = (1/4) int d^4x F^a_{mu nu} F^a_{mu nu}
     = (1/2) int d^4x sum_{mu<nu} F^a_{mu nu} F^a_{mu nu}.
```

Matching the coefficient of each unordered plaquette plane gives

```text
beta g_bare^2 / (4 N_c) = 1/2,
```

hence

```text
beta = 2 N_c / g_bare^2
```

and equivalently

```text
beta * g_bare^2 = 2 N_c.
```

For `N_c = 3` and `g_bare^2 = 1`, this gives `beta = 6`.

## Proof

Set

```text
X = a^2 g_bare F^a_{mu nu} T_a.
```

Since the generators are traceless, `Tr X = 0`. The second-order expansion is

```text
Re Tr exp(iX) = N_c - (1/2) Tr(X^2) + O(X^3).
```

The trace normalization gives

```text
Tr(X^2)
  = a^4 g_bare^2 F^a F^b Tr(T_a T_b)
  = (a^4 g_bare^2 / 2) F^a F^a.
```

Therefore

```text
1 - (1/N_c) Re Tr U_P
  = a^4 g_bare^2 F^a F^a / (4 N_c) + higher order.
```

Multiplying by `beta` and summing over unordered plaquette planes gives the
coefficient `beta g_bare^2/(4N_c)` in front of
`sum_{mu<nu} F^a_{mu nu}F^a_{mu nu}`. The continuum action
`(1/4) F^a_{mu nu}F^a_{mu nu}` counts both `(mu,nu)` and `(nu,mu)`, so over
unordered planes the coefficient is `1/2`. Equating the coefficients gives
`beta = 2N_c/g_bare^2`.

## Boundary

This note does not claim:

- Wilson plaquette action-surface selection from the three framework axioms;
- exclusion of Symanzik, heat-kernel, Manton, tadpole-improved, or other
  action surfaces;
- a physical value for `g_bare`;
- `g_bare = 1`;
- `beta = 6` unless the additional supplied specialization
  `N_c = 3`, `g_bare^2 = 1` is also supplied;
- a continuum-limit existence theorem beyond this coefficient matching;
- an audit verdict or direct status promotion for any row.

The theorem is exactly the small-`a` coefficient matching inside the supplied
standard Wilson plaquette action with canonical generator trace normalization.

## Downstream Use

If independently retained, this row supplies a one-hop source authority for
the `WM` premise in
`BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md`.
That downstream row's rescaling product identity remains ordinary algebra.
Any broader physical claim still needs its own action-surface and
normalization authorities.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py
```

Expected:

```text
TOTAL: PASS=57 FAIL=0
```
