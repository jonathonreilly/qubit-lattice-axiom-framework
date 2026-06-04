# Handoff

## What Changed

- Corrected CPT R2 to the anti-linear spectrum statement: `T v` carries `lambda^*`, not `-lambda^*`.
- Added an exact CPT companion runner check for that R2 correction.
- Added carrier-locus checks proving `sign(Pfaffian(D_beta))=sign(beta)` and orientation/Hodge flip `D_beta -> -D_beta`.
- Reworded carrier-locus so CPT C1/C2 is not treated as a sign selector.
- Refreshed both runner caches.

## Checks

- `PYTHONPATH=scripts python3 scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py`
- `PYTHONPATH=scripts python3 scripts/frontier_koide_carrier_locus_decomposition.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_koide_carrier_locus_decomposition.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_carrier_locus_decomposition.py`
- `python3 -m py_compile scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py scripts/frontier_koide_carrier_locus_decomposition.py`
- `git diff --check`

## Remaining Bridge

The records-pointer mechanism that would select the orientation sign remains open and should be treated as the next science target, not as closed by this PR.
