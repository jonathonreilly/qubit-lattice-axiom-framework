# Claim Status Certificate

## Actual Status

`bounded-support`

The branch is a dependency-reroute and runner-staleness repair. It does not
claim retained status for gravity-clean or G_Newton self-consistency.

## Imports Retired Or Exposed

- Retired as load-bearing language: the gravity Green premise framed as an
  external/textbook theorem in consumer notes and runners.
- Exposed as current dependency: Born-source support rows now exist and must be
  composed explicitly instead of ignored or silently promoted.

## Remaining Gates

- Propagator-skeleton selection for `L^{-1}=G_0`.
- Weak-field-action derivation for `S=L(1-phi)`.
- Parent-chain composition through the Born-source dependency.

## Verification

```text
python3 scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py
TOTAL: PASS=32, FAIL=0

python3 scripts/frontier_gravity_clean_derivation.py
PASS=13 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py
python3 -m py_compile scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py scripts/frontier_gravity_clean_derivation.py
git diff --check
git diff --name-only -- docs/audit
```
