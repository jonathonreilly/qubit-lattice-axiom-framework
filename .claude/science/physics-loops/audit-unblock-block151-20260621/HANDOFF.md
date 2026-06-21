# Handoff

Block 151 repairs and registers the Koide April 22 support-batch aggregate runner.

## What Changed

- Repaired `scripts/frontier_charged_lepton_yukawa_bz_quadrature_explicit.py` so the current large BZ coefficient is treated as a negative boundary, not a small-correction support claim.
- Updated `scripts/frontier_koide_lane_regression.py` expected count to the current `398/398`.
- Added `Claim type`, `Status authority`, and `Runner` metadata to `docs/KOIDE_AXIOM_NATIVE_SUPPORT_BATCH_NOTE_2026-04-22.md`.
- Added cache transcripts for the aggregate and repaired BZ runner.
- Regenerated audit ledger, queue, citation graph, and runner classification.

## Boundary

The target remains:

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`

The aggregate result is `TOTAL: 398/398`. The row classifier is dominant `D`, expected because the support packet contains comparator/readout material. This PR does not promote charged-lepton Koide closure.

## Reviewer Notes

The reviewer lane can cherry-pick or refresh this PR against fast-moving `main`; this branch intentionally does not chase main after PR creation.
