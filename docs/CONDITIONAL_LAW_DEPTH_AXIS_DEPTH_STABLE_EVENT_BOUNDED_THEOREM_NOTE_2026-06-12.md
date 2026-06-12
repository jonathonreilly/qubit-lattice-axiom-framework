# The Conditional Law's Selected Most-Spread Event Is Depth-Stable: the Argmin Freezes by Early Depth (Proven Against Deeper Rows), Its Null-Cleared Structure Is Unchanged Through Cap 14, and the Tested Period+Depth Axes Show No Strengthening (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the gauge-dynamics lane's named fork: the depth direction)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_conditional_law_depth_axis_saturation_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_conditional_law_depth_axis_saturation_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=35 FAIL=0` — exact
Born trees, no MC; the landed conventions **pinned and reproduced** (the seed-4242
depth-9 anchor: prefix-3 `0.5570` vs the landed `0.557`; null p95 `0.4694` vs
`0.469`).

## The question

After the period axis was closed
([`RECORD_CONDITIONAL_LAW_THREE_POINT_PERIOD_SERIES_BOUNDED_THEOREM_NOTE_2026-06-11.md`](RECORD_CONDITIONAL_LAW_THREE_POINT_PERIOD_SERIES_BOUNDED_THEOREM_NOTE_2026-06-11.md):
three-point series, no systematic strengthening), the named fork was the
**depth axis at fixed period**: does the
fixed-prefix-`k` conditional structure strengthen as the record tree deepens
(depths 9 → 14, branches to 16,384), at `L = 3` with the adversarial seed set?

## The findings (runner `PASS=35`)

**(D1) The most-spread event freezes early.** For every seed, the most-spread-row
selector returns the **same row** at every depth cap from its first appearance
through 14 (seed 4242: row 9; seed 99: row 7; seed 7: row 10): deeper trees produce
no more-spread events — the global coherence minimum is an **early-time, event-local
object**.

**(D2) The frozen events' conditional structure is depth-stable and null-cleared.**
All `18/18` (seed × depth-cap) gated events clear their label-permutation nulls
(explicit gate; finite seeded null sampling — 300 draws, rng 7777, disclosed), with
gaps frozen at their event values (seed 99: `+0.19` at `k=3` at every cap; seed 7:
`+0.33` from cap 10). And the freeze is **proven to be the argmin's content, not an
eligibility artifact**: the full per-row coherence ledger is printed, and every row
deeper than the frozen one has strictly larger `g1` at every seed (the new `W3f`
gates). No growth, no decay — a **depth-stable selected event**.

**(D3) The tested axes show no strengthening — the object remains open.** Combined
with the period-axis verdict (no systematic strengthening at `L = 3 -> 4 -> 5`),
the conditional law's record structure has now been scanned along both tested
finite axes with the same outcome: no strengthening with period (to `L = 5`) and
a depth-stable selected event (to cap 14). **The analytics/new-observable
redirect is double-supported on the tested axes**; the object itself — the
conditional law and its within-sector remainder — remains open. The centered-law
parent is
[`CENTERED_U1_FLUCTUATION_LAW_RECORD_MIXTURE_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](CENTERED_U1_FLUCTUATION_LAW_RECORD_MIXTURE_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-06-11.md).

## Scope

Fixed period `L = 3`, depths 9–14, three adversarial seeds, `K_occ = 5`, the landed
machinery exactly (selector semantics: argmin of global coherence over rows `n ≥ 5`
up to each cap — stated, so row-freezing is read correctly as "no deeper row
displaces the early minimum"). Trends are data; no asymptotic claim. The Born
derived-chain cap and named instruments (`ε = 0.6`, `τ = 0.35`) are inherited;
trajectories are realized-state data. **Not claimed**: behavior beyond depth 14 or
`L = 3`, any CLT premise, the within-sector remainder's structure (still the open
object). Cross-references: the linked period series and centered-law notes.

No new axiom, primitive, measure, or weight; `r` untouched; discrete throughout.
The audit lane grades.
