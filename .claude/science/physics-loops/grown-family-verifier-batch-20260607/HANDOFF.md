# Handoff

Branch: `physics-loop/grown-family-verifier-batch-20260607`

This branch turns four previously slow/stale audit runners into fast frozen-log
verifiers:

- `scripts/NONLABEL_GROWN_BASIN_TARGETED.py`
- `scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py`
- `scripts/gate_b_no_restore_joint_package.py`
- `scripts/SEVENTH_FAMILY_DIAGONAL_SWEEP.py`

Each runner keeps the original live replay behind `--recompute`.

Reviewer notes:

- No audit files were edited.
- No retained/proposed-retained status is claimed.
- The seventh-family verifier derives `7/18` passing pockets from the explicit
  row list and reports the historical log summary line `6/18` as stale.
- The PR-scoped cache gate passes with four fresh caches.

Next action after review extraction: audit can rerun these rows against fresh
SHA-pinned caches, then the campaign should continue on the remaining stale
timeout runners or the hard bridge conditional rows.
