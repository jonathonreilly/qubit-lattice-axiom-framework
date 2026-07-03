# Goal

Repair the conditional audit on `NONLABEL_GROWN_BASIN_NOTE.md` by making the completed live recompute artifact load-bearing in the primary verifier and correcting the displayed charge-exponent precision.

The audit repair target was:

```text
runner_artifact_issue: provide the completed SHA-pinned live recompute runner
source and cache output, or a cached --recompute run for the primary runner,
and correct or justify the displayed charge-exponent entries.
```

Success means the default runner validates the recompute artifact and the note table uses the exact recompute row values.
