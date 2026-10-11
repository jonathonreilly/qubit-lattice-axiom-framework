# Nonlinear fluid evidence

This directory preserves the selective independent review and its raw evidence.
The source note and primary runner are in `docs/` and `scripts/`; the canonical
primary stdout cache is in `logs/runner-cache/`. Their final hashes are recorded
in NONLINEAR_SOURCE_IDENTITIES.json one directory above.

The review was written from an external task artifact directory. Its references
to `resume_20261011/<name>` identify the original location; files with those
basenames are copied here without changing their bytes. The raw unified
packaging diff is stored as `nonlinear_stability_packaging_diff.txt.gz`;
decompression recovers the original bytes, including diff context spaces. References to
`worktree/docs/` and `worktree/scripts/` identify the corresponding repository
paths. The root draft is historical proof-development evidence; the final
source note is the theorem offered for review. Author replay and independently
implemented finite checks are distinguished in the review. Neither applies an
audit verdict or proves the analytic theorem by numerical sampling.
