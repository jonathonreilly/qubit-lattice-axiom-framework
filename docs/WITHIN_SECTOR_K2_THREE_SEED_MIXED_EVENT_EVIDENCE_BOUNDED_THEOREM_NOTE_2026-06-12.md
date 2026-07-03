# Mixed-Event Within-Sector Evidence Across the Three Seeds: k=2 Adequate on the Landed Events of 4242/99; the Landed Seed-7 Event Untestable at Any Prefix; a Post-Hoc-Selected Seed-7 Probe Row (Disclosed) Also Shows Record Below Null (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (finite ESS-adequacy follow-on; cross-referenced source proposal, not graded here)
**Claim type:** bounded_theorem
**Related sources:** [`WITHIN_SECTOR_ESS_ADEQUACY_CONCLUSION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-06-12.md`](WITHIN_SECTOR_ESS_ADEQUACY_CONCLUSION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-06-12.md); [`WITHIN_SECTOR_MOMENT_RELATION_WRAPPED_GAUSSIAN_CONSISTENT_BOUNDED_THEOREM_NOTE_2026-06-12.md`](WITHIN_SECTOR_MOMENT_RELATION_WRAPPED_GAUSSIAN_CONSISTENT_BOUNDED_THEOREM_NOTE_2026-06-12.md)
**Primary runner:** [`scripts/frontier_within_sector_k2_mixed_event_evidence_2026_06_12.py`](../scripts/frontier_within_sector_k2_mixed_event_evidence_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_within_sector_k2_mixed_event_evidence_2026_06_12.txt`](../logs/runner-cache/frontier_within_sector_k2_mixed_event_evidence_2026_06_12.txt)
**Status:** source proposal; the audit lane grades. Runner `PASS=13 FAIL=0`.

## Findings

- **k=2 adequacy**: seeds 4242 and 99 are fully adequate (`AAAA`); the landed seed-7
  depth-4 event is **proven untestable at any nontrivial prefix** (`ESS ≈ 3.97 < 8`
  in all four sectors at `B = 16` — the weight-concentration datum, gated).
- **A seed-7 probe row** (depth 11, `B = 2048`; the second-smallest global coherence
  among rows with ≥ 64 branches — a **post-hoc selector, defined in this note, not
  pre-specified by the landed protocol**; its rule is gated so it is reproducible):
  adequate at `k = 2, 3`. This is **probe evidence on a different event** than the
  landed seed-7 event, stated as such — not a completion of the landed protocol.
- **Record below null on every testable comparison**: weighted `|δ|` vs permutation
  null p95 — `0.205 < 0.291` (4242, landed event), `0.100 < 0.246` (99, landed
  event), `0.177 < 0.251` (seed-7 **probe row**). The consistency picture is
  **mixed-event**: landed events on two seeds, a disclosed post-hoc probe on the
  third; untestability of the landed seed-7 event is itself gated.

## Scope

One moment relation, `k = 2` (and `k = 3` on the probe row), finite power.
Branch weights are the explicit Kraus/Born weights of this finite model; no new
axiom, primitive, or extra measure is introduced. `r` untouched. The audit lane
grades.
