# Route Portfolio

## R1: Record/log-det direct derivation

- Type: constructive theorem attempt.
- Target: derive `Phi_X=-log w_X` and the `w`-Hessian readout from Record/log-det surfaces.
- Result: no-go. Record supplies additivity after the scalar context is supplied; determinant/log selection requires an extra quotient.
- Dramatic-step score: 2.

## R2: Additive countermodel family

- Type: no-go / obstruction.
- Target: test whether channel additivity alone selects the pure log barrier.
- Result: `Phi_epsilon=sum_X[-log w_X+epsilon w_X^2]` preserves supplied-channel additivity, but changes the Hessian ratio to `11/6` at `epsilon=1`.
- Dramatic-step score: 3.

## R3: Coordinate gate

- Type: import retirement / obstruction.
- Target: test whether `-log w` alone fixes a readout coefficient.
- Result: Hessian is `1/w^2` in `w`, but zero in `u=log w`; a coordinate/readout bridge is load-bearing.
- Dramatic-step score: 2.

## R4: Future positive theorem route

- Type: constructive theorem.
- Target: derive a Route-2 channel determinant-sector context, determinant quotient, and Hessian-to-E-center bridge.
- Result: queued next; not supplied by current block.
- Dramatic-step score: 3, but higher theorem risk.

Selected block83 route: R2 plus R3, because it gives a falsifier for the Record/log-det-alone derivation and a precise future positive theorem target.
