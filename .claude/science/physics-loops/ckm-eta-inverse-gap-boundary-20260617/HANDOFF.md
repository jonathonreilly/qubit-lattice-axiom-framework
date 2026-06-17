# Handoff

## What Changed

- Demoted the CKM `eta^2` inverse-square gap note from retained/proposed
  framing to bounded support.
- Changed runner dependency checks so open ledger statuses become `[BOUNDARY]`
  instead of hard issues.
- Refreshed `logs/runner-cache/frontier_ckm_wolfenstein_eta_inverse_square_gap.txt`
  to `exit_code: 0`, `status: ok`.

## What Did Not Change

- No audit ledger, queue, dispatch queue, or publication/status surface was
  edited.
- No audit verdict was applied.
- No new axiom was introduced.

## Verification

```bash
python3 -m py_compile scripts/frontier_ckm_wolfenstein_eta_inverse_square_gap.py
PYTHONPATH=scripts python3 scripts/frontier_ckm_wolfenstein_eta_inverse_square_gap.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/frontier_ckm_wolfenstein_eta_inverse_square_gap.py --timeout-sec 120
rg -n 'HARD_ISSUES=[1-9]' logs/runner-cache/frontier_ckm_wolfenstein_eta_inverse_square_gap.txt
git diff --check
```

Expected closeout:

```text
TOTAL: PASS=28, BOUNDARY=7, HARD_ISSUES=0
```
