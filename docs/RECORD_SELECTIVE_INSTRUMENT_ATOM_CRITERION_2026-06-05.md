---
claim_id: record_selective_instrument_atom_criterion_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Selective Instrument Atom Criterion

**Date:** 2026-06-05
**Claim type:** bounded_theorem — bounded support map and finite criterion.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_selective_instrument_atom_criterion_2026_06_05.py`](../scripts/frontier_record_selective_instrument_atom_criterion_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_selective_instrument_atom_criterion_2026_06_05.txt`](../logs/runner-cache/frontier_record_selective_instrument_atom_criterion_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md`](RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md)
- [`RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md`](RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)

## Purpose

The dephasing/broadcast interface leaves a nonselective ensemble state. This
note gives the finite criterion for when a post-record atom is present:

```text
selective instrument outcome + normalized branch + repeat-stable readout
```

Only after that gate does the record-history append/count grammar apply.

## Criterion

For projectors `P_i = |i><i|`, define selective CP maps

```text
M_i(rho) = P_i rho P_i
p_i = Tr M_i(rho)
rho_i = M_i(rho) / p_i  when p_i > 0.
```

A branch supplies a post-record atom `i` when:

1. `p_i > 0`;
2. `rho_i` is normalized;
3. re-reading the same projector is stable: `P_i rho_i P_i = rho_i`;
4. an outcome token `i` is supplied to the history append operation.

The nonselective state `sum_i M_i(rho)` is not a single atom.

## Result

The criterion supplies bounded support for the post-record gate:

- probabilities remain pre-record/ensemble weights until a selective outcome is
  supplied;
- a selected branch gives a one-hot atom and repeat-stable readout;
- record history appends that atom, not the nonselective density matrix.

## Negative Route Pruning

| route | verdict | reason |
|---|---|---|
| nonselective instrument output is an atom | pruned | it is a sum over outcomes |
| probability weight is a realized record | pruned | outcome token is separate |
| branch normalization selects the outcome | pruned | normalization is conditional on supplied branch |
| repeat stability derives Born frequencies | pruned | frequencies are not derived here |
| selective atom fixes clock/rate/dial | pruned | no time normalization or selector is supplied |

## What This Unlocks

- Audit lanes can require the selective atom gate before post-record history is
  invoked.
- Dephasing/broadcast and history append now have a finite bridge without
  collapsing probability, outcome selection, and record information into one
  step.

## Boundaries

- Does not derive outcome selection, Born frequencies, physical collapse,
  Hamiltonian, clock/rate, reset cost, probabilities, or a dial setting.
- Does not apply audit verdicts or edit repo-wide authority surfaces.

## Runner Summary

The runner verifies branch probabilities, normalized selective states,
repeat-stable readout, nonselective/ selective separation, and history append.

Expected result:

```text
SCORECARD PASS=33 FAIL=0
```

```yaml
claim_id: record_selective_instrument_atom_criterion_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "selective atom criterion; outcome selection and Born frequencies remain open"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
