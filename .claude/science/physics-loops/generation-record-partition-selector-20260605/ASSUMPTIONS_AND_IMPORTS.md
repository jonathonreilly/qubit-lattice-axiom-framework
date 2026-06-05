# Assumptions and Imports - Generation Record Partition Selector

## Load-bearing repo inputs

- **Record axiom, 2026-06-05.** Given a supplied finite central-sector
  decomposition and fixed `K`/CPT conjugation, Record names the realized
  `K`/CPT orbit and scalar readout is finitely additive. Record does not
  supply the context, weights, probability, source/action, or dynamics.
- **Generation readout context.** The hw=1 generation carrier is supplied as
  the regular representation of `C3`.
- **Fixed K/CPT conjugation.** Complex conjugation on the complexified carrier
  is part of the supplied readout context.
- **Prior two-sector row.**
  `RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05` proves the orbit count:
  one singlet plus one faithful doublet.

## Standard math

- Finite-dimensional representation theory of `C3`.
- Central idempotents in the group algebra.
- Exact symbolic matrix algebra.

## Forbidden imports

- No PDG values or fitted charged-lepton masses.
- No Born probability.
- No source/action or time-arrow assumption.
- No value selection for `r`, `s`, or `Q`.
- No claim that the block-counting measure is selected.
