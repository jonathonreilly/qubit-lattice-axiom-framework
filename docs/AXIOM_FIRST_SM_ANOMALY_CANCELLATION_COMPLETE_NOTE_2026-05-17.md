# `AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Claim type:** meta
**Parent under repair:** [`AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md)
**Wave:** downstream surgical-fix wave (graph-listed direct dependent of `anomaly_forces_time_theorem`, but see §2 dep clarification).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only. This note does not set or predict the parent's audit outcome.

## 1. Source character

`AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md`
is a **synthesis-aggregator positive_theorem** that records, on the
retained Cl(3)/Z³ left-handed-frame SM matter content, the simultaneous
cancellation of:

- `(A0)` SU(2)^3 cubic (group-theoretic, content-independent);
- `(A1)` SU(3)^3 cubic;
- `(A2)` SU(2)^2 U(1)_Y mixed;
- `(A3)` grav² U(1)_Y ≡ Tr[Y];
- `(A4)` U(1)_Y^3 cubic;
- `(A5)` SU(2) Witten Z_2 nonperturbative parity.

All five are exact `Fraction` or integer-parity equalities verified by
the cited runner. The synthesis is correctly described as an
"aggregator" that does **not** itself derive matter content or
hypercharges; it cites those as upstream inputs.

The hostile-audit-grade issues fixed here are about (i) the **tier
qualifier** on those upstream inputs, and (ii) a **spurious citation-
graph edge** to `ANOMALY_FORCES_TIME_THEOREM`. The arithmetic of
`(A0)-(A5)` is unchanged.

## 2. Findings

### F-A — Stale "retained-grade upstreams" tier descriptor

**Symptom:** the §6 `conditional_surface_status` field originally read:

> "conditional on retained-grade upstreams (NATIVE_GAUGE_CLOSURE,
> GRAPH_FIRST_SU3_INTEGRATION, three-generation structure,
> LEFT_HANDED_CHARGE_MATCHING, HYPERCHARGE_IDENTIFICATION,
> ONE_GENERATION_MATTER_CLOSURE, SM hypercharge uniqueness) and on the
> three component anomaly theorems (already audit-pending under their
> own status fields)"

**Reality (per 2026-05-17 ledger snapshot):**

| Upstream | `audit_status` | `effective_status` | Retained-grade? |
|---|---|---|---|
| `NATIVE_GAUGE_CLOSURE_NOTE` | `audited_clean` | `retained_bounded` | yes |
| `GRAPH_FIRST_SU3_INTEGRATION_NOTE` | `audited_clean` | `retained_bounded` | yes |
| `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE` | `unaudited` | `unaudited` | **no** |
| `THREE_GENERATION_STRUCTURE_NOTE` | `unaudited` | `unaudited` | **no** |
| `LEFT_HANDED_CHARGE_MATCHING_NOTE` | `audited_clean` | `retained_bounded` | yes |
| `HYPERCHARGE_IDENTIFICATION_NOTE` | `audited_conditional` | `audited_conditional` | **no** |
| `ONE_GENERATION_MATTER_CLOSURE_NOTE` | `unaudited` | `unaudited` | **no** |
| `STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24` | `unaudited` | `unaudited` | **no** |

| Component | `audit_status` | `effective_status` |
|---|---|---|
| `SU3_CUBIC_ANOMALY_CANCELLATION_THEOREM_NOTE_2026-04-24` | `audited_conditional` | `audited_conditional` |
| `LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25` | `unaudited` | `unaudited` |
| `SU2_WITTEN_Z2_ANOMALY_THEOREM_NOTE_2026-04-24` | `unaudited` | `unaudited` |
| `RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES_NOTE_2026-05-02` | `unaudited` | `unaudited` |

**Net:** 4 of 7 named upstreams in the original wording (THREE_GENERATION_STRUCTURE / OBSERVABLE, HYPERCHARGE_IDENTIFICATION, ONE_GENERATION_MATTER_CLOSURE, SM hypercharge uniqueness) are **not** at `retained_bounded`. Calling the upstream composite "retained-grade" is an over-statement of the input-tier qualifier.

**Fix:** the `conditional_surface_status` and `proposal_allowed_reason`
fields now describe the upstream as a "tier-mixed matter-content
surface"; a new §7 "Upstream-tier accounting (2026-05-17)" provides the
two tables above and states explicitly that the synthesis's effective
tier is bounded above by the weakest upstream tier. The arithmetic of
`(A0)-(A5)` itself is unchanged.

### F-aux — Spurious citation-graph dep clarification

**Symptom:** the citation graph (per `docs/audit/data/citation_graph.json`)
records this note as a direct dependent of
`anomaly_forces_time_theorem`. Inspection of the source note shows the
only link to `ANOMALY_FORCES_TIME_THEOREM.md` is in §5 (Cross-references)
under the descriptor "parent framework using these anomaly identities
upstream" — an **informational pointer**, not a load-bearing input.

The note's `(A0)-(A5)` proofs do **not** import `d_t = 1`, the `(3, 1)`
spacetime signature conclusion, or any other content of
`ANOMALY_FORCES_TIME_THEOREM` as a proof step.

**Fix:** the new §7 includes a "Cross-reference dep clarification"
subsection that records the edge as an apparent (graph-artifact) dep
rather than a content-citation flow. This lets downstream audit tooling
disambiguate when computing cycle-membership and break-target lists.

(No edit is made to the citation-graph data; the disambiguation is
recorded in the source note as a documentation-level signal, consistent
with the source-only review-loop policy.)

## 3. What this fix does NOT do

- Change `(A0)-(A5)` proofs.
- Change the synthesis statement or the matter-content table in §0.
- Change the arithmetic equalities in §2 (still exact `Fraction` /
  integer-parity).
- Change the runner expectation (`PASS=N FAIL=0`).
- Change the list of "What This Synthesis Does Not Claim" in §3.
- Promote any upstream theorem or alter any retained-tier claim.
- Modify pipeline code or citation_graph data.
- Set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (synthesis aggregator retained; effective tier
inherits the weakest of the upstream composite tiers per §7). The
corrected note brings the input-tier qualifier into line with the
ledger and disambiguates the apparent vs load-bearing citation-graph
edges. The synthesis's own arithmetic is unaffected.

Once the currently `unaudited` upstreams (three-generation structure,
ONE_GENERATION_MATTER_CLOSURE, SM hypercharge uniqueness, LH anomaly
trace catalog, SU2 Witten Z2, RH sector identities) audit through, the
synthesis's effective tier rises automatically without further surgical
edits.

## 5. Verification

Paired runner:
`scripts/frontier_axiom_first_sm_anomaly_cancellation_complete_downstream_fix.py`

Programmatically verifies:

- **F-A:** stale "retained-grade upstreams" wording retired; "tier-mixed"
  wording present; §7 "Upstream-tier accounting" header present; the
  three-generation, HYPERCHARGE_IDENTIFICATION, ONE_GENERATION_MATTER_CLOSURE,
  and SM-hypercharge-uniqueness upstreams are correctly labelled with
  their actual ledger tiers; retained upstreams (NATIVE_GAUGE_CLOSURE,
  GRAPH_FIRST_SU3_INTEGRATION, LEFT_HANDED_CHARGE_MATCHING) are still
  labelled `audited_clean` / `retained_bounded`.
- **F-aux:** the apparent-dep / cross-reference clarification subsection
  is present and identifies the `ANOMALY_FORCES_TIME_THEOREM` link as
  informational.
- **Structural invariants:** §0 synthesis statement preserved;
  matter-content table preserved; `(A0)-(A5)` arithmetic preserved;
  runner expectation preserved; §3 "What This Synthesis Does Not Claim"
  preserved.

Cached output: `logs/runner-cache/frontier_axiom_first_sm_anomaly_cancellation_complete_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — clarified as informational cross-reference (not load-bearing)
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — sibling downstream fix (`s3_anomaly_spacetime_lift_note`)
- [PR #1509](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1509) — sibling downstream fix (`dt1_time_dimension_proof_walk`)
- [PR #1510](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1510) — sibling downstream fix (`s3_time_spacetime_tensor_primitive`)
