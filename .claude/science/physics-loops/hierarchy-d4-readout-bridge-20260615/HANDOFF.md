# Handoff

## What changed

- Added
  `docs/HIERARCHY_D4_EFFECTIVE_POTENTIAL_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-15.md`.
- Added
  `scripts/hierarchy_d4_effective_potential_readout_bridge_2026_06_15.py`.
- Updated `HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md` to point to the bounded
  bridge candidate. The retained endpoint note is intentionally untouched.
- Fixed the sign typo in the endpoint runner docstring:
  `(A_2/A_inf)^(1/4)`, not `(A_2/A_inf)^(-1/4)`.

## Verification

```bash
python3 scripts/hierarchy_d4_effective_potential_readout_bridge_2026_06_15.py
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
python3 scripts/frontier_hierarchy_effective_potential_endpoint.py
python3 -m py_compile scripts/hierarchy_d4_effective_potential_readout_bridge_2026_06_15.py scripts/frontier_hierarchy_effective_potential_endpoint.py scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
python3 scripts/precompute_audit_runners.py --runners scripts/hierarchy_d4_effective_potential_readout_bridge_2026_06_15.py,scripts/frontier_hierarchy_effective_potential_endpoint.py --check-only --allow-non-main
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

## Remaining blockers

- Audit/review must decide whether the bounded bridge premise closes the
  physical electroweak insertion map.
- Endpoint selection remains open.
- Full hierarchy closure remains open.
