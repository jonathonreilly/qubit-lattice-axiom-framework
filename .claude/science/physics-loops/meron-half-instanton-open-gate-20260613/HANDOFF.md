# Handoff

This branch repairs the meron half-instanton open-gate packet by adding a
downstream source-boundary firewall to the note and a matching runner test.

Changed artifacts:

- `docs/MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`
- `scripts/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.py`
- `logs/runner-cache/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.txt`

Reviewer focus:

- Confirm the firewall language is strong enough for the audit row's boundary:
  later framework use must separately prove the regulator/twist/patching sector
  and the substrate/observable bridge.
- Confirm the note still stays open-gate/external and does not promote the
  meron packet to retained.

Known caveat:

- Strict audit lint on current main reports unrelated retained hash drift in
  `cl3_taste_generation_theorem` and
  `free_dirac_car_positive_energy_equal_time_anticommutator_support_bounded_note_2026-06-08`.
