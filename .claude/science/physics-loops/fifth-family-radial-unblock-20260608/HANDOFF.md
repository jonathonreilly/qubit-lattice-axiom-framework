# Fifth-Family Radial Unblock Handoff

## Repair

Added `scripts/fifth_family_radial_symmetry_orientation_certificate_2026_06_08.py`.
It avoids the old `_measure_family` replay path and instead:

- derives zero and neutral exactness from source-field linearity;
- differentiates the zero-field propagation recurrence;
- verifies the first-order positive-source response is negative on the
  `drift=0.20, seed=0` radial row.

## Verification

- `python3 scripts/fifth_family_radial_symmetry_orientation_certificate_2026_06_08.py`
- `python3 scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/fifth_family_radial_symmetry_orientation_certificate_2026_06_08.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/fifth_family_radial_symmetry_orientation_certificate_2026_06_08.py`
- `git diff --check`
- `git diff -- docs/audit`

## Remaining Science

This does not prove a wider radial basin or a corrected positive-orientation
variant. It is a row-level bounded certificate for the audit blocker.
