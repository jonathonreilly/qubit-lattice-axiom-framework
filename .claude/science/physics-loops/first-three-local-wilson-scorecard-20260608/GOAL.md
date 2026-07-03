# Goal

Repair the scorecard mismatch blocking `GAUGE_VACUUM_PLAQUETTE_FIRST_THREE_SAMPLE_LOCAL_WILSON_PARTIAL_EVALUATION_NOTE_2026-04-17.md`.

The audit repair target was:

```text
runner_artifact_issue: repair the stale expected summary or add the missing
theorem check, then re-audit the same local-only scope.
```

This branch chooses the stronger repair: add the missing theorem check for the Bessel-determinant one-plaquette normalization, preserving the note's expected `THEOREM PASS=6 SUPPORT=4 FAIL=0` scorecard.
