# No-Go Ledger

## Do Not Delete Before Guarded Dry Run

The cleanup candidate set changed from 11 to 9 to 8 as safety guards landed.
Manual deletion before those guards would have removed valid nested-runner or
repo-referenced cache evidence.

Status: avoided.

## Do Not Treat Cleanup As Audit

Deleting orphan cache files does not validate or invalidate any scientific
claim. It is repository hygiene only.
