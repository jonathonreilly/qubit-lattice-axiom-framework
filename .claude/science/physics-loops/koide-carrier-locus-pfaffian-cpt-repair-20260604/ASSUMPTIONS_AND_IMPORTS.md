# Assumptions And Imports

## Load-Bearing Inputs

- Oriented two-state real antisymmetric doublet block `D_beta = [[0,beta],[-beta,0]]`.
- Existing carrier-locus finite algebra checks.
- Existing CPT C1/C2 algebraic invariance surface.

## Retired Import / Sign Drift

- The Pfaffian sign is now checked directly: `Pf(D_beta)=beta`, so `sign(Pf(D_beta))=sign(beta)`.
- The orientation/Hodge flip is now checked directly: it sends `D_beta -> -D_beta` and flips the Pfaffian sign.
- CPT R2 is corrected to the anti-linear statement `T v` carries `lambda^*`, not `-lambda^*`.
- Carrier-locus no longer imports CPT as a sign selector.

## New Axioms

None.

## Remaining Open Bridge

The records-pointer mechanism that would select which orientation sign Nature uses remains open.
