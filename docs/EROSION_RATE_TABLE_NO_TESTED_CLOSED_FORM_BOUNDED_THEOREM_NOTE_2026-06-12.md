# The Erosion-Rate Envelope Is Geometric at Moderate ε (0.5–0.8, 5% Gate) and Non-Geometric Near the Projective Endpoint (0.9–0.99); No Tested Closed Form Matches; the Threshold Time Is Censored-Nonincreasing; the Ensemble Record Persists (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_erosion_rate_table_no_closed_form_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_erosion_rate_table_no_closed_form_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=16 FAIL=0` — exact trees, seven ε values.

## Dependency

This is the rate-law follow-on of
[`RECORD_EROSION_BRANCH_VS_ENSEMBLE_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md`](RECORD_EROSION_BRANCH_VS_ENSEMBLE_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md);
the broadcast/readout model and Born cap are inherited from that note.

## Findings

The odd-step rebound envelope of the branch-relational record is **geometric at
moderate ε** (the 5% step-independence gate passes for ε = 0.5–0.8) and **measurably
non-geometric near the projective endpoint** (relative spreads 5.7–7.6% at
ε = 0.9/0.95/0.99 — gated as the observed split). **None of the four tested algebraic
candidates** (`(1−ε²)/4`, `(1−ε²)²/4`, `(1−ε²)/2`, `(1−ε²)²`) matches the measured
`r(ε)` table at `10⁻⁶` — candidates checked by evaluation, nothing fitted; the
**measured table is the datum** (deviations printed per candidate). The threshold time
`t*(ε)` is **censored-nonincreasing** in ε (finite horizon; gated); the Born-weighted ensemble Z-summary MI
stays `[1,1,1]` at every probed ε (`10⁻¹²`); ε = 0 and projective controls reproduce
the record-erosion predecessor.

## Scope

The broadcast + weak-measurement model, exact; candidate-form testing without fitting;
the closed form of `r(ε)`, if any, is the named open object. Born cap inherited. No new
axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
