# Goal

Repair the post-audit runner artifact issue on `action_normalization_note`
without applying audit verdicts.

The latest audit rationale says to reconcile
`docs/ACTION_NORMALIZATION_NOTE.md` with
`scripts/frontier_action_normalization.py` by adding a real PASS/FAIL
certificate or changing the expected verification summary. This PR takes the
stronger path: the runner now emits and enforces the expected certificate.
