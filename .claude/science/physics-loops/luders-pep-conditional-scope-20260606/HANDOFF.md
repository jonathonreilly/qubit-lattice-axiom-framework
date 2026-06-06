# Handoff

## What Changed

This branch narrows the Lüders sequential-effect source note to conditional
finite-matrix support. The note now assumes the Lüders update and trace/effect
pairing as supplied measurement-side premises, then proves/checks that
`M_{P,E} = P E P` is the exact two-step effect and a valid effect.

## Why

The previous source wording presented the measurement bridge as stronger than
the actual support surface. This repair preserves the useful algebra while
making the remaining measurement/probability inputs explicit.

## Verification

- `python3 -m py_compile scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py`
- `python3 scripts/cached_runner_output.py scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py --refresh --timeout-sec 120`

## Remaining Open Work

The framework still needs a separate measurement/probability bridge if the
parent Lüders/Born lane is to move beyond conditional support.

## Audit Discipline

No audit-ledger files are edited in this branch, and the branch does not set an
audit outcome.
