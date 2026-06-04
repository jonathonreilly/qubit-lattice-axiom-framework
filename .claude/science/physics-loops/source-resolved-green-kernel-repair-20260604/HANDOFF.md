# Handoff

## Summary

This branch repairs a paired runner-artifact issue for the source-resolved exact
and propagating Green pocket notes.

The executable convention is now named consistently everywhere:

```text
rho_eps = sqrt(dx^2+dy^2+dz^2) + eps
kernel = exp(-mu rho_eps) / rho_eps
```

The finite packet values are unchanged. The caches are refreshed because the
runner print strings and script hashes changed.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/source_resolved_exact_green_pocket.py
PYTHONPATH=scripts python3 scripts/source_resolved_propagating_green_pocket.py
python3 scripts/cached_runner_output.py --refresh scripts/source_resolved_exact_green_pocket.py
python3 scripts/cached_runner_output.py --refresh scripts/source_resolved_propagating_green_pocket.py
python3 scripts/cached_runner_output.py --check-only scripts/source_resolved_exact_green_pocket.py
python3 scripts/cached_runner_output.py --check-only scripts/source_resolved_propagating_green_pocket.py
python3 -m py_compile scripts/source_resolved_exact_green_pocket.py scripts/source_resolved_propagating_green_pocket.py
git diff --check
```

Expected summaries:

```text
exact Green: PASS=5 FAIL=0
propagating Green: ASSERTIONS: PASS
```

## Remaining Open Gates

- Derive the Green-kernel form and parameters from retained framework dynamics.
- Prove any desired continuum or size-transfer theorem separately.
- Re-audit independently before any status change.
