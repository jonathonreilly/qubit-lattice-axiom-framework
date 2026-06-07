# D3 Lower-Bound Source-Packet Gate

**Date:** 2026-06-06
**Claim type:** meta
**Runner:** [`scripts/frontier_d3_lower_bound_source_packet_gate_2026_06_06.py`](../scripts/frontier_d3_lower_bound_source_packet_gate_2026_06_06.py)
**Cached output:** [`logs/runner-cache/frontier_d3_lower_bound_source_packet_gate_2026_06_06.txt`](../logs/runner-cache/frontier_d3_lower_bound_source_packet_gate_2026_06_06.txt)
(`SCORECARD: PASS=58 FAIL=0`)

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch certifies an audit packet/source-exposure gate. It does not retag the audit ledger, prove full D=3 dimension selection, or authorize a framework-baseline rewrite."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Scope

The active review queue still carries
`2026-05-20-d3-lower-bound-bridge-sign`, whose original finding was that the
submitted analytic lower-bound bridge did not match the existing runner's
phase-coupling observable around the two-dimensional logarithmic case.

Current `main` has moved since that queue item:

- `dimension_selection_finite_k_centroid_sign_bridge_note_2026-05-25` is
  `audited_clean` with effective status `retained_bounded`.
- `dimension_selection_lower_bound_bridge_v2_2026-05-20` is `audited_clean`
  with effective status `retained_bounded`.
- The parent `dimension_selection_note` remains `audited_conditional`, but its
  current blocker is now a runner-artifact/source-packet issue, not the old
  sign-bridge inconsistency.

This note certifies that the source-packet issue is inspectable from current
files. It does not update the audit ledger.

## Exact Gate

The parent row's current re-audit note asks for:

```text
include the finite-k bridge runner source, original dimension runner
source/cache, and source-packet verifier output so the displayed beta, I_3,
and sign computations can be independently inspected.
```

The runner checks that all of those artifacts are present and linked from
`DIMENSION_SELECTION_NOTE.md`:

- `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`
- `logs/runner-cache/frontier_dimension_selection_lower_bound_parent_repair.txt`
- `scripts/frontier_dimension_selection.py`
- `logs/runner-cache/frontier_dimension_selection.txt`
- `docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`
- `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`
- `logs/runner-cache/frontier_dimension_selection_finite_k_centroid_sign_bridge.txt`
- `outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json`
- `scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py`
- `logs/runner-cache/dimension_selection_parent_source_packet_manifest_2026_06_05.txt`

It also checks the source-packet verifier cache:

- belongs to `scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py`;
- has a SHA matching the current verifier source;
- exits with `exit_code=0` and `status=ok`;
- reports `SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS=57 FAIL=0`;
- includes SHA freshness checks for the original runner cache;
- includes the original `I_3/P = <1e-10` table evidence;
- includes the finite-k bridge cache summary `SUMMARY: PASS=56 FAIL=0`.

## Claim-State Movement

This branch separates three layers that were previously easy to conflate:

1. The old active-queue sign inconsistency has already been repaired on
   current `main` by the finite-k centroid-sign bridge and V2 lower-bound row.
2. The parent `DIMENSION_SELECTION_NOTE.md` row still needs audit action, but
   its listed source-packet artifacts are now present, linked, and SHA-fresh.
3. Full D=3 dimension selection remains open. The parent row still does not
   derive the all-d potential family, a framework-internal upper bound, uniform
   parameter control, or any baseline rewrite.

The intended downstream use is a re-audit target: reviewers can inspect the
parent row as a finite-runner lower-bound packet without re-opening the already
repaired sign-bridge issue.

## Non-Claims

This branch does not claim:

- a unique-dimension theorem;
- a derivation of `Z^3` from a dimension-free baseline;
- a repo-wide framework-baseline rewrite;
- a full D=3 spatial-dimension closure;
- an audit-lane verdict change.
