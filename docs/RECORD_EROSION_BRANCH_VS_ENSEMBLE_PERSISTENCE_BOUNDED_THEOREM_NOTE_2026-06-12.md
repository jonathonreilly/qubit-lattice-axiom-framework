# Under Continued Pointer Measurement the Branch-Relational Record Functional Erodes (Oscillating, Decaying Envelope) While the Born-Weighted Ensemble Z-Summary Mutual Information Persists Exactly (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_record_erosion_ensemble_persistence_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_record_erosion_ensemble_persistence_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=12 FAIL=0` — exact trees to depth 10.

## Inputs and dependency boundary

This packet extends the finite branch-budget model from
[`BRANCHING_RECORD_BUDGET_INEQUALITY_BOUNDED_THEOREM_NOTE_2026-06-12.md`](BRANCHING_RECORD_BUDGET_INEQUALITY_BOUNDED_THEOREM_NOTE_2026-06-12.md)
and its slack-rate follow-on
[`BRANCHING_SLACK_RATE_PROJECTIVE_LIMIT_BOUNDED_THEOREM_NOTE_2026-06-12.md`](BRANCHING_SLACK_RATE_PROJECTIVE_LIMIT_BOUNDED_THEOREM_NOTE_2026-06-12.md).
The eroding object here is the branch-state connected-correlator record functional,
not the Record axiom's durable registration of a realized outcome. No claim is made
that durable records unform, re-register, or change.

## Findings

Two record measures tracked exactly through a broadcast phase then a measurement-only phase:

- **The branch-relational record functional erodes, non-monotonically**: under continued weak pointer
  measurement the Born-weighted connected-correlator count decays with **rebounds**
  (`ε = 0.3/0.6`: oscillating decay, gated); at `ε = 0.9` the trajectory **oscillates with a
  decaying envelope** — even steps exactly zero, odd-step rebounds falling geometrically
  (`0.041 → 0.0064 → 0.0011 → 0.00018`, ratio ≈ 0.16; gated to this pattern, which refuted
  the draft's monotone-zero guess).
- **The Born-weighted ensemble Z-summary persists exactly**: during the broadcast phase
  the per-fragment mutual information rises as `[1,0,0] → [1,1,0] → [1,1,1]` bits, and
  through the entire measurement-only phase it stays `[1,1,1]` (`10⁻¹²`) at every step
  and every `ε`. Controls: `ε = 0` changes nothing; one projective step kills all
  connected correlators; the `|0⟩`-pointer registers nothing in either measure.

**The measured statement**: the branch-state connected-correlator record functional is fragile under
continued readout; the Born-weighted ensemble Z-summary mutual information is exactly
conserved. Stated as a measured model fact only — no interpretive framing is introduced.

## Scope

The broadcast + weak-measurement model, exact, depth 10; the branch-functional-vs-ensemble
split is the datum. Born derived-chain cap inherited through the linked finite branch-budget
packets. Not claimed: other dynamics, asymptotics, durable-record unforming, or any
interpretation beyond the measured split. No new axiom/primitive/measure/weight; `r`
untouched. The audit lane grades.
