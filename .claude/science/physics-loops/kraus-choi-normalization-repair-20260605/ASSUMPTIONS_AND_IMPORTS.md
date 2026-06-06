# Assumptions And Imports

## Allowed Inputs

- Existing qubit-lattice finite-region algebra statement
  `A_Lambda ~= M_d(C)`.
- Standard finite-dimensional Kraus and Choi theorem context already named in
  the note.
- Finite matrix arithmetic checked by the new runner.

## Repair Boundary

The source convention is now the unnormalized Choi convention:
`|Omega> = sum_i |i>|i>`. Under this convention,
`Phi(X) = Tr_1[(X^T tensor I) C_Phi]` has no extra factor. The note also
states that the normalized convention would require the compensating factor
`d`.

## Forbidden Inputs

- No new axiom.
- No arbitrary infinite-volume channel theorem.
- No audit verdict edit.
