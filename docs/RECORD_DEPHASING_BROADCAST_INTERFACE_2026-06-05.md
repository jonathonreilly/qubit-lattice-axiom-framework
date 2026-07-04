---
claim_id: record_dephasing_broadcast_interface_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Dephasing Broadcast Interface

**Date:** 2026-06-05
**Claim type:** bounded_theorem — bounded support map and dynamics interface.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_dephasing_broadcast_interface_2026_06_05.py`](../scripts/frontier_record_dephasing_broadcast_interface_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_dephasing_broadcast_interface_2026_06_05.txt`](../logs/runner-cache/frontier_record_dephasing_broadcast_interface_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md`](RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md)
- [`RECORD_LOCAL_OBSERVABILITY_DECODER_CRITERION_2026-06-05.md`](RECORD_LOCAL_OBSERVABILITY_DECODER_CRITERION_2026-06-05.md)
- [`RECORD_DYNAMICS_AUDIT_GATE_LADDER_2026-06-05.md`](RECORD_DYNAMICS_AUDIT_GATE_LADDER_2026-06-05.md)

## Purpose

This note isolates the user's pre-record/post-record distinction in the
dynamics stack:

```text
pre-record qubit state -> dephasing/broadcast interface -> possible records
selective realized outcome -> post-record atom/history information
```

The nonselective dephased state is still an ensemble object. It is not yet a
single realized record atom.

## Interface

For a pointer qubit and blank fragments, use the broadcast isometry

```text
|0>|000> -> |0>|000>
|1>|000> -> |1>|111>.
```

For a pre-record state `sqrt(p0)|0> + sqrt(p1)|1>`, the global output is

```text
sqrt(p0)|0>|000> + sqrt(p1)|1>|111>.
```

Tracing out fragments dephases the pointer system:

```text
rho_S = diag(p0, p1).
```

The probabilities remain as weights in a nonselective state. A selective
instrument event is the additional step that yields a post-record atom, either
`0` with probability `p0` or `1` with probability `p1`, after which the history
append/count grammar applies.

## Result

The interface supplies three exact distinctions:

1. **Pre-record probability:** `p0, p1` are weights in the qubit state and in
   the nonselective reduced density matrices.
2. **Broadcast support:** each fragment has a local marginal carrying the same
   classical weights on the pointer basis, and selective branches have clean
   local broadcast words.
3. **Post-record information:** a realized branch supplies one atom and can be
   appended to record history; the nonselective density state alone is not that
   atom.

## Negative Route Pruning

| route | verdict | reason |
|---|---|---|
| nonselective dephasing is a produced record | pruned | it is still an ensemble density state |
| broadcast correlations select one outcome | pruned | selection is a separate instrument event |
| local marginals imply a history atom | pruned | history needs a realized atom |
| dephasing derives Born frequencies | pruned | probabilities are supplied by the pre-record state |
| dephasing fixes a clock/rate/dial | pruned | no time normalization or selector is supplied |

## What This Unlocks

- The framework can use qubit probabilities before realization without calling
  them post-record information.
- It can use post-record information after a selective event without pretending
  the nonselective state already contained a single atom.
- Audit lanes can ask whether a claim uses a pre-record probability, a
  nonselective dephased state, or a post-record atom/history.

## Boundaries

- Does not derive outcome selection, Born frequencies, physical collapse,
  Hamiltonian, clock/rate, reset cost, or a dial setting.
- Does not apply audit verdicts or edit repo-wide authority surfaces.

## Runner Summary

The runner verifies dephasing of the reduced pointer state, preservation of
global coherence before selection, local fragment marginals, selective branch
broadcast words, and the nonselective/selective gate split.

Expected result:

```text
SCORECARD PASS=33 FAIL=0
```

```yaml
claim_id: record_dephasing_broadcast_interface_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "dephasing/broadcast interface; selective post-record atom remains a separate gate"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
