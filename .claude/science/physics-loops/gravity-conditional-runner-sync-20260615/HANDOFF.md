# Handoff

This PR synchronizes the gravity full-self-consistency runner with the narrowed
conditional source note and registers it for audit.

## Changed

- Added `Runner:` and `Runner cache:` links to
  `docs/GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`.
- Reworded `scripts/frontier_gravity_full_self_consistency.py` so its stdout
  states the conditional A2 boundary and does not claim A2 is derived.
- Added `logs/runner-cache/frontier_gravity_full_self_consistency.txt`.

## Verified

- Runner compiles and passes.
- Cache check is fresh.
- Citation graph attaches the runner to `gravity_full_self_consistency_note`.
- Full pipeline passes with no lint errors.
- Generated audit/publication outputs are not committed.

## Reviewer Notes

The pipeline invalidates the edited audited row and six downstream rows for
re-audit. That is expected and intentional: after landing, those rows should be
re-audited with the honest conditional runner packet.
