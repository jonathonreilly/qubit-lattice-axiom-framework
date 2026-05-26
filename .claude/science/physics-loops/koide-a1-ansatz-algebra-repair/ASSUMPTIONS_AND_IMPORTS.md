# Assumptions And Imports

## Declared Inputs

- Formal variables `a > 0` and `r >= 0`.
- Formal trace declarations `tr(Phi) = 3a` and
  `tr(Phi^2) = 3a^2 + 6r^2`.
- The quartic ansatz
  `V(Phi) := [2 tr(Phi)^2 - 3 tr(Phi^2)]^2`.
- The Brannen parameter convention `c := 2r/a` and the formal expression
  `Q := 1/3 + c^2/6`.

## Not Imported

- No observed lepton masses.
- No fitted phase selector.
- No Standard Model Yukawa theorem.
- No derivation of the quartic ansatz from Axiom 1 / Axiom 2.
- No new axiom and no audit verdict.

## Open Import

The ansatz itself remains an admitted premise. Any downstream use must keep
that premise visible until a separate theorem derives or replaces it.
