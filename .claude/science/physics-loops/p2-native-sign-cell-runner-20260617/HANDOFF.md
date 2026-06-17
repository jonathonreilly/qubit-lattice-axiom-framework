# Handoff

## Target

`p2_wick_rotation_sign_epsilon_closure_narrow_theorem_note_2026-05-27`

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4258

## What changed

- The P2 runner now checks current C-Sc transfer language instead of stale
  source text.
- The P2 runner directly constructs the `Cl(4,0)` Euclidean sign cell and the
  `Cl(3,1)` Lorentzian sign cell.
- Both sign cells are checked by anticommutation, square-sign, and rank-16
  Clifford-monomial tests.
- The note now treats OS/Wightman/Lawson/Cartan-Bott material as parallel
  context only, not as a load-bearing proof import.

## Status boundary

This is bounded-support source repair. Parent C-Sc/C-RP/C-Aft/C-Ext boundaries
remain in force, and independent audit owns any effective status.

## Verification

Expected local verification commands:

```bash
python3 scripts/p2_wick_rotation_sign_epsilon_closure_runner_2026_05_27.py
python3 scripts/cached_runner_output.py --refresh scripts/p2_wick_rotation_sign_epsilon_closure_runner_2026_05_27.py
python3 scripts/cached_runner_output.py --check-only scripts/p2_wick_rotation_sign_epsilon_closure_runner_2026_05_27.py
python3 -m py_compile scripts/p2_wick_rotation_sign_epsilon_closure_runner_2026_05_27.py
git diff --check
```

## Reviewer notes

Please extract the science if useful. This PR intentionally does not update
main, ledger rows, audit outputs, active review queues, lane registries, or
publication matrices.
