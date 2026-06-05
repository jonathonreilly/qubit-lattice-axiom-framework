# Assumptions and Imports - Record Dynamics Classifier

## Load-bearing repo inputs

- **Record axiom, 2026-06-05 reset.** Given a supplied finite central-sector
  decomposition and fixed `K`/CPT conjugation, the record names the realized
  orbit and scalar readout `I` is finitely additive over disjoint records.
  Record supplies no probability, weighting, time metric, source/action,
  decoherence, or dynamics.
- **Two-sector generation readout.**
  `RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05` supplies the singlet
  sector of real dimension `1` and faithful doublet sector of real dimension
  `2`, conditional on the supplied readout context.
- **Koide/dial algebra.**
  `KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05` and
  `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05` supply
  `Q=1/3+(2/3)r` and `r(s)=2^(s-1)`.

## Supplied dynamics classes, not physical derivations

- Two-sector entropy ascent on the block simplex.
- Real-mode entropy ascent on the three resolved real modes.
- Lueders/record sharpening `r -> 2r^2`.
- Reverse/thermalizing branch `r -> sqrt(r/2)`.
- Supplied heat-kernel path `r(t)=tanh(t)^4`.

These are classified, not asserted as the physical charged-lepton arrow.

## Standard math

- Finite-dimensional calculus for entropy functions.
- Local one-dimensional stability for maps and flows.
- Exact symbolic algebra in `sympy`.

## Forbidden imports

- No PDG values, charged-lepton masses, fits, or empirical comparators.
- No Born-rule probability interpretation from Record alone.
- No hidden source/action, time metric, or decoherence dynamics.
- No claim that `Q=2/3` is uniquely forced by minimal axioms.
