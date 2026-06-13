# Handoff

This branch repairs the Koide first-order selector audited conditional by adding
a bridge-scope firewall and runner token checks.

Reviewer focus:

- Confirm `M(b) tensor sigma_+` remains an algebraic localization only.
- Confirm no retained `AC_phi_lambda` bridge or physical `r` weighting is claimed.
- Confirm the false converse is excluded.

Known caveat:

- Strict audit lint on current main reports unrelated retained hash drift in
  `cl3_taste_generation_theorem` and
  `free_dirac_car_positive_energy_equal_time_anticommutator_support_bounded_note_2026-06-08`.
