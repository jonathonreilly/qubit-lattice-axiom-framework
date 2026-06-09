---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Grown Transfer Basin Note

**Date:** 2026-06-08 live replacement for the archived stale-runner note
**Status:** bounded current-source basin packet; no audit-status movement is
claimed here.
**Primary runners:**
[`scripts/GROWN_TRANSFER_BASIN_SWEEP.py`](../scripts/GROWN_TRANSFER_BASIN_SWEEP.py),
[`scripts/GROWN_TRANSFER_BASIN_TARGETED.py`](../scripts/GROWN_TRANSFER_BASIN_TARGETED.py)
**Runner caches:**
[`logs/runner-cache/GROWN_TRANSFER_BASIN_SWEEP.txt`](../logs/runner-cache/GROWN_TRANSFER_BASIN_SWEEP.txt),
[`logs/runner-cache/GROWN_TRANSFER_BASIN_TARGETED.txt`](../logs/runner-cache/GROWN_TRANSFER_BASIN_TARGETED.txt)
**Assertion wrapper:**
[`scripts/grown_transfer_basin_live_packet.py`](../scripts/grown_transfer_basin_live_packet.py)
**Repair note:**
[`docs/GROWN_TRANSFER_BASIN_TARGETED_REPAIR_NOTE_2026-06-04.md`](GROWN_TRANSFER_BASIN_TARGETED_REPAIR_NOTE_2026-06-04.md)

## Purpose

The archived `grown_transfer_basin_note` failed because the targeted checker
used the wrong complex-action survival predicate. It required
`abs(action_gamma0) < 1e-12`, while the source claim was about same-row survival
of the signed-source package and the complex-action `TOWARD -> AWAY`
carryover with near-unit weak-field response.

The current runners share the repaired predicate functions and the current
wrapper asserts that the targeted and full sweep caches agree.

## Current Safe Claim

On the finite current grid:

- targeted rows `(0.15, 0.60)`, `(0.20, 0.60)`, `(0.20, 0.70)`, and
  `(0.25, 0.80)` survive both observables: `4/4`;
- the full `3 x 3` drift/restore sweep reports signed-source survivors `9/9`,
  complex-action survivors `9/9`, and same-row survivors `9/9`;
- row values are recomputed by `_score_row(drift, restore)`, which builds the
  grown geometry through `scripts/gate_b_grown_joint_package.py` and applies
  the shared row predicates.

## Boundary

This is finite bounded support for a narrow nearby basin. It does not prove a
family-wide graph-ladder transfer theorem, a physical geometry-generic claim,
or any effective audit status. The remaining source question is whether this
finite row grid and grown-geometry helper dependency are acceptable to
independent audit.

## Verification

```bash
python3 scripts/cached_runner_output.py --check-only scripts/GROWN_TRANSFER_BASIN_TARGETED.py
python3 scripts/cached_runner_output.py --check-only scripts/GROWN_TRANSFER_BASIN_SWEEP.py
python3 scripts/cached_runner_output.py --refresh scripts/grown_transfer_basin_live_packet.py
```
