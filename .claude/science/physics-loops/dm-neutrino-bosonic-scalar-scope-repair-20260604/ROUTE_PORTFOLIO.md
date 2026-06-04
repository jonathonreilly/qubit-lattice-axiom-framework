# Route Portfolio

## Route A: Prove Real-D Determinant Response

Status: not attempted in this branch.

This would require proving that the scalar-baseline response
`det(mI+jΓ_1)/det(mI)` transfers to the real-D block response
`det(D+jΓ_1)/det(D)`. The auditor listed this as one possible repair, but it is
larger and riskier than the available narrowing route.

## Route B: Narrow To Scalar Diagnostics

Status: executed.

This route leaves the scalar determinant identities as diagnostics and makes
the finite Frobenius ratio the theorem conclusion. It directly matches the
auditor-provided alternative repair action.

## Route C: Drop Determinant Diagnostics Entirely

Status: unnecessary.

The determinant identities are exact and useful for inspection as long as they
are not claimed as real-D source responses.
