# Handoff

This branch repairs the auditor's domain caveat for the quark Koide open-gate
note. The algebra statement now requires `sum x_k != 0`, equivalently nonzero
mean `a`, before using `Q` and `|b|^2/a^2`.

## Verification

- `python3 scripts/frontier_quark_mass_spectrum_koide_scheme_open_gate.py`
- `python3 -m py_compile scripts/frontier_quark_mass_spectrum_koide_scheme_open_gate.py`

## Reviewer Notes

- No `docs/audit/**` files should be present in this PR.
- No new axiom is introduced.
- The row remains an open-gate comparator, not a quark-mass theorem.
- Quark mass values remain scheme/scale observational comparators.

## PR

Pending.
