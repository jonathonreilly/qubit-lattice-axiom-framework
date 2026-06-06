Verification commands run:

```text
python3 -m py_compile scripts/signed_gravity_aps_locked_source_action_proposal.py
python3 scripts/signed_gravity_aps_locked_source_action_proposal.py
python3 scripts/precompute_audit_runners.py --runners scripts/signed_gravity_aps_locked_source_action_proposal.py --check-only --allow-non-main --push-mode none
```

Observed result:

- runner summary: `PASS=11 FAIL=0`
- cache reported fresh
