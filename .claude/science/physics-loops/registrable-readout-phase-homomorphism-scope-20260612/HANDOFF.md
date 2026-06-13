# Handoff

## What Changed

This branch repairs
`registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10`
by replacing the overbroad Record-alone claim with a theorem restricted to
`H_char`, the determinant-character / group-homomorphic phase-readout subclass.

The primary note and runner now explicitly keep the counterexample
`I(S)=sum_j cos(theta_j)`, which is Record-additive over disjoint records,
K-even, and phase-dependent.

## Verification

Run:

```bash
python3 scripts/frontier_registrable_readout_additive_even_phase_free_2026_06_10.py
python3 scripts/frontier_registrable_readout_phase_homomorphism_scope_guard_2026_06_12.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_registrable_readout_additive_even_phase_free_2026_06_10.py,scripts/frontier_registrable_readout_phase_homomorphism_scope_guard_2026_06_12.py --check-only --push-mode=none
```

Expected:

- Primary runner: `PASS=32, FAIL=0`
- Scope guard: `PASS=8, FAIL=0`
- Runner cache check: both caches fresh

## Remaining Blocker

This branch does not prove that the relevant physical readout must lie in
`H_char`. If a downstream chain needs absence of all non-homomorphic K-even
phase readouts, it still needs a separate science bridge.
