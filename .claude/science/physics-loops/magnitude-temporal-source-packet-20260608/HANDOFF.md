# Handoff

This PR repairs the source-side blocker for `MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06`.

Main changes:

- Adds a source-packet section with one-hop retained/bounded authorities and caches.
- Tightens the clock-rate no-go reading: count-only rows may cite counts; rate rows must name a denominator; no physical rate/metric is derived.
- Adds runner checks for dependency docs, runners, caches, ledger statuses, and retained no-go wording.
- Refreshes the runner cache.

Verification:

- `PYTHONPATH=scripts python3 scripts/magnitude_temporal_factor_is_count_not_rate_2026_06_06.py` -> `TOTAL: PASS=52 FAIL=0`
- Cache refresh succeeded for the one changed runner.
- No `docs/audit/**` edits are intended.

Residuals:

- Does not derive the full magnitude.
- Does not close per-record/UV minimal-block readout selection.
