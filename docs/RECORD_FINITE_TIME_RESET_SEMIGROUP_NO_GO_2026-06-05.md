---
claim_id: record_finite_time_reset_semigroup_no_go_2026-06-05
claim_type_author_hint: exact_negative_boundary
---

# Record Finite-Time Reset Semigroup No-Go

**Date:** 2026-06-05
**Claim type:** exact negative boundary for finite-time reset dynamics.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_finite_time_reset_semigroup_no_go_2026_06_05.py`](../scripts/frontier_record_finite_time_reset_semigroup_no_go_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_finite_time_reset_semigroup_no_go_2026_06_05.txt`](../logs/runner-cache/frontier_record_finite_time_reset_semigroup_no_go_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_OPEN_SYSTEM_RESET_CHANNEL_INTERFACE_2026-06-05.md`](RECORD_OPEN_SYSTEM_RESET_CHANNEL_INTERFACE_2026-06-05.md)
- [`RECORD_BLANK_SINK_PREPARATION_REGRESS_NO_GO_2026-06-05.md`](RECORD_BLANK_SINK_PREPARATION_REGRESS_NO_GO_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)

## Question

Can the exact reset channel from the open-system interface be treated as the
finite-time output of an ordinary bounded-generator semigroup, thereby deriving
a finite physical reset rate?

No. The exact reset channel is singular as a linear map on operators, while a
finite-time exponential of a finite bounded generator is invertible.

## Result

For a `d`-dimensional sink register, the exact reset channel is

```text
R(A) = |0><0| Tr(A).
```

As a linear superoperator on the `d^2`-dimensional operator space, `R` has
one-dimensional range and rank `1`. For `d > 1`, it is singular.

For any finite matrix generator `L`, the finite-time map

```text
Phi_t = exp(t L)
```

is invertible with inverse `exp(-t L)`. Therefore `R` cannot equal `Phi_t` for
finite `t` and finite `L`.

This is the precise rate boundary:

```text
exact reset channel = allowed open-system interface
finite-time bounded-generator semigroup = cannot produce that exact endpoint
```

Amplitude damping illustrates the boundary. With `p(t) = 1 - exp(-gamma t)`,
finite `gamma t` gives `p < 1`, so the superoperator remains invertible and the
excited state is not exactly blank. The reset endpoint appears at `p = 1`,
which is an endpoint/admitted discrete channel or asymptotic limit, not a
finite-rate derivation.

## Negative Route Pruning

| route | verdict | reason |
|---|---|---|
| exact reset channel gives finite-time rate | pruned | reset superoperator is singular |
| bounded-generator semigroup reaches exact reset at finite time | pruned | finite matrix exponentials are invertible |
| amplitude damping with finite `gamma t` exactly blanks | pruned | `p(t) < 1` at finite `gamma t` |
| semigroup no-go blocks open reset channel interface | pruned | discrete/asymptotic/singular/open-boundary routes remain open |
| rate boundary fixes a dial | pruned | no selector is supplied |

## What This Unlocks

- Dynamics proposals can use the reset channel as an interface without
  pretending it also derives a finite physical rate.
- A future physical implementation must choose one of the honest routes:
  asymptotic relaxation, a discrete intervention, a singular/limit process, or
  a richer non-Markovian/open-boundary construction.
- Audit rows can separate "CPTP reset exists" from "finite-time generator
  derived."

## Boundaries

- Does not derive a Hamiltonian, bath, temperature, thermodynamic cost,
  finite-time rate, clock, low-record boundary, probabilities, or a dial
  setting.
- Does not block asymptotic damping, discrete reset channels, singular limits,
  or non-Markovian/open-boundary dynamics.
- Does not apply audit verdicts.

## Runner Summary

The runner builds reset superoperators for `d = 2, 4, 8`, verifies rank-one
singularity and trace preservation, checks amplitude-damping superoperators at
finite `p < 1` versus the endpoint `p = 1`, and records the finite-exponential
invertibility marker.

Expected result:

```text
SCORECARD PASS=43 FAIL=0
```

```yaml
claim_id: record_finite_time_reset_semigroup_no_go_2026-06-05
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "exact no-go for finite-time bounded-generator semigroup realization of exact reset"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
