lro-finite-size-analysis, independent run 1 of 2
worker w-jonathonsmac4f50-j796b (claude-opus-5), unit C-lro-finite-size-analysis-a1

Result: not computed; too few points are logged.

The task says: if fewer than half the points are logged, list what is missing and stop.
When the unit was run (ai/probes at cc1a1691, also checked on origin):

X:formation-3plus1-finite-size: 1 of 36 grid points logged
  beta=2 L=64 T=3000 T0=1500 seed=1: plateau |m| = 0.7354
  the last three table rows, |m| by level:
    level 1539: 0.7363
    level 2149: 0.7361
    level 3000: 0.7335

X:formation-3plus1-long: 0 of 6 grid points logged

Total: 1 of 42 points (half would be 21).

run.py prints all 41 missing points as `extra` strings. They are:
  finite-size:
    beta = 2 and 3
    L = 16, 24, 32, 48, 64, 96
    seeds 1, 2, 3
    T = 3000, T0 = 1500
    all 36 combinations except beta=2 L=64 seed=1
  long:
    beta = 2, L = 48, T = 20000, T0 = 10000, seeds 1-4
    beta = 1.5, L = 48, T = 20000, T0 = 10000, seeds 1-2

Supplementary point from another grid, not fitted:
  X:formation-3plus1-seeds, beta=2 L=48 T=3000 seed=2: plateau |m| = 0.7366
  last three |m|: 0.7336, 0.7374, 0.7374

No fit of m_inf was attempted, and there is no HIT.
The computation can be done once the work loop has run the two grids; run.py does the inventory and stops.
