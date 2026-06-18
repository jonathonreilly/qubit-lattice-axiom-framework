# Route Portfolio

## Route A: Reconcile Summary Counts

Status: implemented.

Update the source note to use `SUMMARY: PASS=64 FAIL=0` for PR #2850 and
`SUMMARY: PASS=52 FAIL=0` for PR #2864.

## Route B: Make Mismatch Regressions Executable

Status: implemented.

Add runner assertions that every stack PR's cached summary string appears in
the note and in the corresponding cached log.
