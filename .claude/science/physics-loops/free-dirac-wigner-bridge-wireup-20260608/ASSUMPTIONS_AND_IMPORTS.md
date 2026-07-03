# Assumptions And Imports

## Allowed Current Inputs

- The parent packet `docs/FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md`.
- The companion representation packet `docs/FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`.
- The companion runner/cache pair `scripts/free_dirac_poincare_representation_2026-05-30.py` and `logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt`.
- The Wigner bridge packet `docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md`.
- The Wigner bridge runner/cache pair `scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py` and `logs/runner-cache/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt`.

## Imports Not Retired

- The continuum free one-particle mass-shell carrier is an allowed restricted-packet surface here; it is not derived from baseline lattice axioms.
- The block does not derive spin-statistics, interacting locality, or full lattice Lorentz symmetry.
- No observational target values, fitted selectors, or admitted unit conventions are used.

## Import Movement

The block retires one hidden dependency edge in the parent packet by making the Wigner strong-continuity bridge explicit and machine-checked from the parent runner. It does not remove the restricted-carrier boundary.
