# No-Go Ledger

## Do Not Use Stem-Only Missing Checks For Cleanup

Observation: runner-cache filenames contain only the runner stem. For nested
runners, `logs/runner-cache/foo.txt` does not distinguish
`scripts/foo.py` from `scripts/corrections/foo.py`.

Result: a cleanup guard based only on `scripts/<stem>.py` can produce false
orphan positives.

Status: blocked by this PR's header-aware preservation rule.

## Do Not Delete Candidate Orphans In This Block

The block target is safety before cleanup, not cleanup itself. Deletion of the
remaining candidates is left for a later focused review/PR.
