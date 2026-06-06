# Assumptions And Imports

## Allowed Inputs

- PR #2804 K-Z external-lift gate pack.
- The active blocker quoted in that pack: do not use `W_lift = 0.05` as a
  load-bearing bracket until it is extracted from an explicit finite
  `SU(3), beta=6` primary-source bracket.
- Guo, Li, Yang, and Zhu, "Bootstrapping SU(3) lattice Yang-Mills theory,"
  JHEP 12 (2025) 033, arXiv:2502.14421.
- Source-bundle vector coordinates from `figures/4Dsu3plotcd.eps`, used only
  as an image-derived convention diagnostic.

## Derived Inside This Block

- The paper action coefficient and standard Wilson coefficient imply
  `lambda = N^2 / beta`.
- For `N = 3`, Wilson `beta = 6` maps to plotted `lambda = 1.5`.
- The source-bundle vector extraction gives width `0.245195` at `lambda=1.5`
  and width `0.048725` at `lambda=3.0`.

## Open Imports

- Table/source-data extraction for the finite `SU(3)`, Wilson `beta=6`
  bracket.
- Repo-owned finite `SU(3)`, Wilson `beta=6` SDP reproduction.
- Any convention bridge that identifies the framework beta target with the
  paper's plotted `lambda=3.0` coordinate rather than Wilson `beta=6`.

## Forbidden Inputs

- Treating image/vector extraction as a theorem-grade numeric table.
- Treating old `W_lift ~= 0.05` as a finite `SU(3)`, Wilson `beta=6` bracket
  without a convention bridge.
- Observed plaquette values or Monte Carlo target matching as proof inputs.
- Fitted `beta_eff`.
