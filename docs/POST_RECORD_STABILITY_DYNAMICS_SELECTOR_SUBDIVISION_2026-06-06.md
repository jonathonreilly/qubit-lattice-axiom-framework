# Post-Record Stability/Dynamics Selector Subdivision

**Date:** 2026-06-06
**Type:** meta
**Claim type:** meta
**Status:** exact-support source-side for read-only stability/dynamics selector
subdivision; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py`](../scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.txt)
**Bounded row export:**
[`outputs/post_record_stability_dynamics_selector_slice_2026_06_07.json`](../outputs/post_record_stability_dynamics_selector_slice_2026_06_07.json)
**Load-bearing upstream helper:**
[`scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py`](../scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py)
with cache
[`logs/runner-cache/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.txt)

## Result

This block subdivides the `stability_or_dynamics_selector` sub-bucket from the
selector/dial subdivision.

It is read-only. It does not edit audit data, does not apply verdicts, and does
not select or force a generation/Koide dial location.

On the current ledger snapshot:

| Stability/dynamics sub-bucket | Rows |
|---|---:|
| `flow_or_thermal_stability` | 106 |
| `arrow_or_dynamics_bridge` | 63 |

Total: `169` stability/dynamics selector rows.

## Meaning

The stability/dynamics selector bucket splits into two tasks:

1. **Flow/thermal stability rows** can be reviewed for a supplied flow, map,
   fixed point, attractor, separatrix, thermal branch, or entropy principle.
   These rows may support a stable setting, but stable setting is not selected
   dial.
2. **Arrow/dynamics bridge rows** need a physical arrow, Hamiltonian, transfer,
   kernel, instrument, decoherence, or measurement bridge before any selector
   claim can be calibrated.

This is the exact queue for the user's dial constraint: we can preserve stable
locations as stable locations, while keeping physical selection and forced
values out of scope.

stable setting is not selected dial.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "stability/dynamics selector rows are subdivided for triage; stable settings are not selected dials"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch subdivides a read-only row bucket and does not edit audit data."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundaries

- Does not edit `docs/audit/data`.
- Does not apply or predict audit verdicts.
- Does not promote any row.
- Does not select or force a generation/Koide dial location.
- Does not turn stable settings into selected dials.
- Does not derive a physical arrow, kernel, Hamiltonian, instrument, clock, or
  rate from Record.

## Runner certificate

The runner verifies:

- source anchors in the selector/dial subdivision and evidence-ladder notes;
- the selector/dial helper source used to obtain the bucket is included in the
  packet;
- bounded ledger-row export exists for the selected stability/dynamics rows;
- current stability/dynamics selector row count is `169`;
- sub-bucket counts sum to `169`;
- expected sub-bucket counts match the current snapshot;
- representative rows are present in each sub-bucket;
- audit ledger hash is unchanged after the scan;
- no audit verdict, audit-data write, retained/promoted claim, stable-setting
  to selected-dial flag, or generation/Koide dial-selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py
```
