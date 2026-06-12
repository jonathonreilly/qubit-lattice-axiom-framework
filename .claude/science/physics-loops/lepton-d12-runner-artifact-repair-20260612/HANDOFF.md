# Handoff

## Summary

This branch repairs the lepton D12-prime open-gate runner/cache. The source
split changed since the older cache: YUKAWA now owns only color-channel
fraction algebra, while the YT Ward note owns the `H_unit` scalar-singlet
surface. The runner now checks that split and still confirms no lepton scalar
bridge is present.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_lepton_block_d12_prime_matching.py
python3 scripts/precompute_audit_runners.py --check-only --pr-diff origin/main --allow-non-main --push-mode none
git diff --check
```

Observed result: runner PASS=13 / FAIL=0, relevant caches fresh, whitespace
check clean.

## Remaining Work

Independent review/audit should re-check the same narrow open gate. Building a
lepton-composite scalar bridge is separate frontier work.
