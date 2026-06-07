# Physics Loop Handoff

## Status

`exact-support`; audit still required before any repo-wide retained status.

## Claim moved

`higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02`

## Blocker addressed

The conditional blocker asks for a retained one-hop bridge deriving the
`d=4/Z^4` APBC taste count `N_taste = 16` and the mean-field determinant `W(J)`
form used in the curvature calculation.

## What this PR does

- Adds a bridge-packet section to the parent Higgs ratio note.
- Adds parent-runner checks for bridge artifact paths, source markers, source
  size, cache runner names, runner SHA freshness, clean exits, and expected
  output markers.
- Refreshes the parent runner cache.
- Refreshes the determinant/APBC bridge runner cache.
- Leaves `docs/audit/**` untouched.

## Verification

```bash
python3 -m py_compile scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py scripts/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.py scripts/audit_companion_higgs_mean_field_determinant_apbc_taste_bridge_2026_06_06.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_higgs_mean_field_determinant_apbc_taste_bridge_2026_06_06.py
git diff --check
git diff --name-only -- docs/audit
```

## Loop packet

`.claude/science/physics-loops/higgs-ratio-bridge-packet-inline-20260606/`
