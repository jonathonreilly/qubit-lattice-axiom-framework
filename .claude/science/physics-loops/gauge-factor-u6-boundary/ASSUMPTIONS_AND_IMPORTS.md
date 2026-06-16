# Assumptions And Imports

## Zero-Input Structural Checks

- `su(2)` closure on the qubit fiber.
- `su(3)` generator independence and no faithful `su(3)` carrier below
  dimension 3.
- `[su(3) x I, I x su(2)] = 0`.
- Full `u(6)` dimension on the unrestricted six-dimensional carrier.
- `su(3) x su(2)` cross-factor complement dimension 24.
- Irreducible-action commutants for `su(2)` on `C^2` and `su(3)` on `C^3`.

## Supplied Premises

- The `C^3(base) x C^2(fiber)` carrier factorization.
- The factor-locality / `MR_color` premise that selects the factor-preserving
  algebra over unrestricted `u(6)`.
- Gauging selection, physical-color meaning, and chiral `su(2)_L` selection.

## Imports Not Used

- No PDG, observed, fitted, cosmological, or literature value is used.
- No new framework axiom is introduced.
- Textbook Lie-algebra facts used by the prose are checked directly in the
  runner rather than imported as load-bearing proof.
