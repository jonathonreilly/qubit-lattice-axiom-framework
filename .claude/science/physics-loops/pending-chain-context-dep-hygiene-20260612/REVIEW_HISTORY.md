# Review History

- 2026-06-12: In-memory citation graph check:
  - `lattice_3d_nyquist_diffraction_note` no longer depends on `start_here`.
  - `linear_response_second_order_kubo_note` no longer depends on
    `minimal_axioms_2026-05-03`.
  - `koide_r_half_not_symmetry_protected_dynamical_norm_balance_narrow_no_go_note_2026-06-04`
    no longer depends on `koide_bae_30_probe_campaign_note_2026-05-09`.
- 2026-06-12: `git diff --check` passed.
- 2026-06-12: `scripts/lattice_3d_nyquist_diffraction_probe.py` passed.
- 2026-06-12: `scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
  passed with `6 PASS, 0 FAIL`.
- 2026-06-12: `scripts/linear_response_second_order_kubo.py` was not rerun to
  completion in this branch; the live attempt timed out at 240s, and the
  existing runner cache records `exit_code: 0`, `elapsed_sec: 574.52` for the
  unchanged script.
