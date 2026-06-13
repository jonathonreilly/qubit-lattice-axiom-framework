# Handoff

This branch repairs the fractional-instanton dilute-gas open-gate packet by
adding a downstream source-boundary firewall and runner test.

Changed artifacts:

- `docs/FRACTIONAL_INSTANTON_DILUTE_GAS_CONDENSATE_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`
- `scripts/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.py`
- `logs/runner-cache/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.txt`

Reviewer focus:

- Confirm the firewall matches the audit caveat: no positive hierarchy bridge,
  determinant/measure/coupling-scale prescription, condensate closure, or
  framework substrate/observable identification can be imported from this
  external packet.
- Confirm the note remains open-gate/external and does not promote the
  fractional-instanton packet to retained.

Known caveat:

- Strict audit lint on current main reports unrelated retained hash drift in
  `cl3_taste_generation_theorem` and
  `free_dirac_car_positive_energy_equal_time_anticommutator_support_bounded_note_2026-06-08`.
