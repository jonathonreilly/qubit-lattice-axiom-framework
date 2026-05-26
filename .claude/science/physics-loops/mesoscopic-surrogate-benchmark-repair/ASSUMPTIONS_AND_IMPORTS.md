# Assumptions And Imports

- The fixed 3D ordered-lattice setup is part of the runner configuration for
  this finite sweep; this block does not certify it as a general
  source-control authority.
- The benchmark gates are branch-local audit targets, not new axioms:
  `support2 >= 25`, `capture1 >= 0.95`, `capture2 >= 0.95`,
  `score >= 0.999`, and `|width_ratio - 1| <= 0.05`.
- Helper sources remain visible through the registered helper paths
  `scripts/quasi_persistent_relaunch_probe.py` and
  `scripts/two_body_momentum_harness.py`.
- The only positive claim is finite-table: under the declared benchmark,
  broad top-N rows pass and square/Gaussian rows do not.
