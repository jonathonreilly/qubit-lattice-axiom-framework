# Handoff

## Summary

This block repairs the sign-portability derivation row by narrowing it to a
bounded cached gate certificate.

The cache reports:

- derivation block: `PASS`;
- five core families: `G1G2G3G4 = PPPP`;
- one holdout family: `G1G2G3G4 = PPPP`;
- overall: `PASS`.

The note now excludes unconditional unit-slope and cross-family theorem claims.

## Pipeline Result

```yaml
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
ready: true
criticality: medium
transitive_descendants: 78
load_bearing_score: 6.804
deps: []
helper_runner_paths: []
open_dependency_paths: []
```

## Runner Output

```bash
PYTHONPATH=scripts python3 scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py
```

Result:

```text
Sign portability cached gate certificate: PASS
PASS=42 FAIL=0
```

## Remaining Science

The row-wise detector-intensity and first-order plus-response lower-bound
theorem remains open.
