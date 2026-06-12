# DM Minimum-Information Source-Law Firewall

Branch: `physics-loop/dm-mininfo-source-law-firewall-20260612`
Base: `origin/main` at `31b5d454`

## Purpose

Repair the `audited_numerical_match` surface for:

- `dm_leptogenesis_pmns_minimum_information_source_law_note_2026-04-16`

The audit blocker was precise: the row imposed `eta_i*/eta_obs = 1`, verified one numerical optimizer output, and did not prove global uniqueness, stationarity classification, or a retained selector law.

## Changes

- Added a current-surface source certificate naming the actual status as `conditional-support / numerical-match`.
- Removed binding "unique stationary point" / "retained claim" framing.
- Reframed the checked result as a runner-found calibrated constrained-optimization diagnostic under an adopted selector.
- Added runner checks enforcing the new source boundary.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py
# PASS=21 FAIL=0
```

Remaining blockers:

- derive `I_seed` or a replacement selector from retained framework inputs;
- derive the favored-column identification in the restricted packet;
- prove KKT/global-minimality classification independent of the observed `eta_obs` calibration;
- retire the imposed `eta_i*/eta_obs = 1` comparator constraint.
