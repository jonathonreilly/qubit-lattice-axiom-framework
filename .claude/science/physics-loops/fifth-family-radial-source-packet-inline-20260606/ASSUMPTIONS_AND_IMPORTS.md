# Assumptions And Imports

Allowed repo-native inputs:

- `scripts/FIFTH_FAMILY_RADIAL_BASIN.py`
- `scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py`
- `scripts/FIFTH_FAMILY_RADIAL_SWEEP.py`
- `scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py`
- `scripts/CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py`
- `scripts/gate_b_no_restore_farfield.py`
- paired cached runner outputs under `logs/runner-cache/`

No new axiom, observed target value, fitted selector, external comparator, or
textbook import is introduced. The branch exposes and verifies existing repo
sources and caches.

Open dependency classes:

- independent audit verdict;
- any family-wide radial-shell theorem;
- any continuum/asymptotic closure;
- any physical mass-observable derivation.
