# Assumptions and Imports

## Load-bearing inputs

- Finite `3 x 3` matrix arithmetic over `C`.
- Displayed matrices `E_12`, `E_23`, `E_31`, `C`, `I_3`, and `P_23`.
- Displayed maps:
  - `A_fwd(c) = c_1 E_12 + c_2 E_23 + c_3 E_31`;
  - `A -> C A C^dagger`;
  - `A -> P_23 A^dagger P_23`.

## Removed imports

- No carrier or native observable/value-law authority is imported.
- No physical claim that the specified identity input is the sole-axiom
  free-point block is imported.
- No physical claim that graph-first induces the prescribed
  swap-conjugation map is imported.
- No PMNS angle, value-selection, PDG, or fitted numerical data is used.

## Audit boundary

The source row is reset to `unaudited` and must be audited independently
before any retained-grade interpretation is allowed.
