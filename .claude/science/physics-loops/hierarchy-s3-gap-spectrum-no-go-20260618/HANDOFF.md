# Handoff

This PR adds a narrow S3 route-pruning theorem for the DELTA0 hierarchy gate.
It does not audit, retag, or land anything.

Main artifact:
- `docs/HIERARCHY_DELTA0_S3_FIXED_GAP_SPECTRUM_NO_GO_NOTE_2026-06-18.md`
- `scripts/frontier_hierarchy_delta0_s3_fixed_gap_spectrum_no_go_2026_06_18.py`

Claim movement:
- Prunes the fixed-G lattice-gauge-only NJL S3 gap-spectrum arm.
- Does not close DELTA0 and does not eliminate threshold-dependent, EW-driven,
  or non-NJL S3 mechanisms.

Verification:
- `PYTHONPATH=scripts python3 scripts/frontier_hierarchy_delta0_s3_fixed_gap_spectrum_no_go_2026_06_18.py`
- `PYTHONPATH=scripts python3 scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py`
- `python3 -m py_compile scripts/frontier_hierarchy_delta0_s3_fixed_gap_spectrum_no_go_2026_06_18.py`
- `git diff --check`

Next science action:
- Try an outside-K1-K8 attachment observable or a derived threshold-dependent
  `G_n` route if the reviewer finds this pruning useful.
