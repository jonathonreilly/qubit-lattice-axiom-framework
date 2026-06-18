## Summary

Adds the fifth distinct N1 route requested by the latest conditional audit row
for the Koide `r=1/2` narrow no-go.

The added route proves that a `C3`-compatible coefficient rephasing /
doublet-basis calibration preserves `|b|^2/a^2`, so a hidden phase or basis
choice cannot force arbitrary `r` to `1/2`.

## Trace gate

- Target claim:
  `koide_r_half_not_symmetry_protected_dynamical_norm_balance_narrow_no_go_note_2026-06-04`
- Blocker quoted from audit ledger:
  `scope_too_broad: add a fifth distinct N1 route or rescope the row as a bounded algebraic support identity for the four explicitly checked C3/S3 unitary routes.`
- Trace class: `direct_blocker_closure`
- Audit/review status: source-side PR only; independent review/audit still owns
  effective status.

## Artifacts

- `docs/KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`
- `scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
- `logs/runner-cache/audit_companion_koide_r_half_not_symmetry_protected_exact.txt`
- `.claude/science/physics-loops/koide-rhalf-fifth-route-20260618/HANDOFF.md`
- `.claude/science/physics-loops/koide-rhalf-fifth-route-20260618/TRACE_GATE.md`
- `.claude/science/physics-loops/koide-rhalf-fifth-route-20260618/CLAIM_STATUS_CERTIFICATE.md`

## Checks

- `python3 scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
- `python3 -m py_compile scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
- `git diff --check`
