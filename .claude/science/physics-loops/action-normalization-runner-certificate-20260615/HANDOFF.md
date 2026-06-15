# Handoff

Reviewer focus:

- Confirm that the added checks are substantive and tied to the narrowed no-go
  premises.
- Confirm that the runner exits nonzero on failure or certificate-count drift.
- Confirm that the note and runner now agree on `TOTAL: PASS=42 FAIL=0`.
- Confirm that no audit verdict files are included.

Validation run:

```text
PYTHONPATH=scripts python3 scripts/frontier_action_normalization.py
TOTAL: PASS=42 FAIL=0
```

This PR is intended to make the existing narrowed no-go re-auditable by fixing
the runner artifact issue; it does not ask the reviewer to merge any audit
result.
