# Handoff

## What Changed

- `docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`
  now proves KS phase uniqueness as a local Z2 gauge class via the
  Clifford `-1` plaquette cocycle.
- The note points the load-bearing single-mode Grassmann premise at
  the current substep-1 narrow theorem.
- `scripts/probe_kawamoto_smit_phase_forcing.py` now checks:
  construction, central pseudoscalar, cocycle, gauge transform,
  gauge recovery, transformed scalarization, and invalid all-plus
  rejection.
- The runner cache was refreshed.

## Verification

- `python3 -m py_compile scripts/probe_kawamoto_smit_phase_forcing.py`
- `python3 scripts/probe_kawamoto_smit_phase_forcing.py`
- `python3 scripts/cached_runner_output.py scripts/probe_kawamoto_smit_phase_forcing.py --refresh --timeout-sec 120`
- `python3 scripts/cached_runner_output.py scripts/probe_kawamoto_smit_phase_forcing.py --check-only`
- `git diff -- docs/audit --exit-code`
- `git diff --check`

## Boundaries

This PR does not close `AC_phi_lambda`, finite-boundary holonomy
selection, or direct Noether retagging.

## Next Action

Open a ready review PR, then continue the current audit-unblock scan.
