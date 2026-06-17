# Handoff

Branch: `codex/staggered-density-readout-bridge-20260617`

This PR repairs a source-side blocker for
`axiom_first_lattice_noether_onsite_internal_narrow_theorem_note_2026-06-05`.

What changed:

- Added a finite-CAR theorem proving `rho_x = chibar_x chi_x` is the local
  number projection `a_x^dag a_x` and normalized onsite U(1) generator.
- Added a runner proving the one-site, uniqueness, finite-lattice, and
  matrix-unit density commutator checks.
- Updated the Noether note to cite this bridge and keep the KS matrix as an
  explicit finite exhibit rather than a broad realization-gate dependency.

Checks run:

- `python3 scripts/staggered_dirac_local_density_readout_bridge_2026_06_17.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/staggered_dirac_local_density_readout_bridge_2026_06_17.py`

Not done:

- No audit-loop run.
- No audit ledger, queue, publication, or front-door edits.
- No review-loop run; reviewer owns that step.
