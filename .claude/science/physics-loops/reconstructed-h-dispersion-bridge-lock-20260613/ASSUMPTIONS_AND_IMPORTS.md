# Assumptions And Imports

No new axiom is introduced.

Source-side one-hop bridge:

- `FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`
  derives the d-dimensional free staggered two-step dispersion on the
  `U=1` surface.
- `scripts/free_staggered_two_step_dispersion_d_dimensional_2026_06_12.py`
  passes with `TOTAL: PASS=7, FAIL=0`, and the reconstructed-H runner checks
  that this cache is SHA-fresh.

Remaining boundaries:

- one-particle/free-bilinear transfer channel only;
- no claim about full many-body Fock transfer spectrum beyond the standard
  free-bilinear second-quantized construction;
- no gauged/interacting log-transfer locality theorem;
- no exact quasilocal Lieb-Robinson tail-composition closure.
