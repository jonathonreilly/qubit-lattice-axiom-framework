# Assumptions And Imports

## Retained

- The explicit `beta = 6` `spatial_pair` witness family used by the existing
  dense-grid runner.
- The explicit target triple
  `Z^min = (0.135165279562..., 0.374012880009..., 0.543843858544...)`.
- The runner's finite enumeration of the stated `6 x 6 x 5 x 8 = 1440`
  sampled grid.
- The optimal scalar fit routine used by `gap_at`.

## Removed From The Binding Claim

- Empirical finite-difference Lipschitz constants.
- Adaptive continuous-box subdivision under those empirical constants.
- Any assertion that the sampled-grid argmin is the true continuous global
  minimum.

## Still Open

To restore a continuous-box no-go, a later block must provide analytic
operator-norm/subspace Lipschitz bounds, interval arithmetic over `gap_at`, a
proof-level global optimizer, or an analytic monotonicity theorem.
