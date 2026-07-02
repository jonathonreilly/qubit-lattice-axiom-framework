# S3 / Route-2 Readout Endpoint Physics Loop

## Objective

Attack the S3/Route-2 readout endpoint triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4)
```

from first principles, with the immediate target of deriving or sharply
constraining the remaining `rho_E = beta_E / alpha_E = 21/4` entry that blocks
the unique exact `Theta_R -> Lambda_R` coupling theorem.

## Operating Constraints

- Do not run audit tooling or apply audit verdicts.
- Do not push science to `main`.
- Do not refresh existing PR branches onto `main`.
- Do not check or report PR conflicts or mergeability.
- Open one review PR per coherent science block.
- Use branch-local loop-pack artifacts for state, trace, and handoff.

## Current Science Block

Block10 tests whether finite-frame source/readout dual normalization can supply
the two reciprocal local projector-weight factors needed for

```text
lambda = q_E / q_T = 9/4.
```

The block result is conditional-support: two independent local Riesz-dual
source/readout legs produce the endpoint algebra exactly, while current
Route-2 tensor/readout notes do not yet license those two independent legs.
