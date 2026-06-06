# Assumptions And Imports

## Inputs

- PR #2966 updates the selector/dial subdivision to the current ledger
  snapshot.
- The generation/Koide index imports
  `scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py`
  and
  `scripts/frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06.py`.
- The current snapshot has 103 Koide/generation selector rows and 3
  generation/Koide stable-feature rows.

## Imports Retired

- Stale 105 selector-row count.
- Stale 108 combined-row count.
- Stale selector class split.

## Imports Still Open

- Stable-location support still does not select a dial.
- No physical selector, stable rule, measure/prior, physical arrow, or Koide
  closure is derived by this branch.
