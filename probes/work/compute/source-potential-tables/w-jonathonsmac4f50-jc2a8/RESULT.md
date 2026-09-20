source-potential-tables, independent run 1 of 2
worker w-jonathonsmac4f50-jc2a8 (claude-opus-5), unit C-source-potential-tables-a1

Result: not computed; too few points are logged.

The task says: if fewer than half the points are logged, list what is missing and stop.
When the unit was run (ai/probes at 393ad9d6):

X:source-potential: 2 of the 48 grid points are logged, plus 2 off-grid short runs (L = 16, T = 600).

What the four logs contain, for the record (no fit, no seed scatter, single seeds):

  grid point, dim 3s (light-cone), beta = 1, L = 32, T = 2000, h = 0.5, seed 1, n = 7
    measured/linear by r: 1: 0.945, 2: 0.959, 3: 0.962, 4: 0.988, 6: 0.939, 8: 0.950, 12: 0.352, 16: 1.909
    r * measured: 1: +0.037348, 2: +0.034390, 3: +0.029649, 4: +0.026320, 6: +0.018312, 8: +0.012496, 12: +0.001020, 16: -0.003504
    continuum h/(4 pi beta) = 0.039789
    (the last two r are past L/4 and are dominated by the periodic image; the ratio is not a constant there)

  grid point, dim 3 (backward), beta = 6, L = 48, T = 2000, h = 0.5, seed 1, n = 4
    measured/linear by r: 1: 0.970, 2: 0.969, 3: 0.967, 4: 0.967, 6: 0.944, 8: 0.958, 12: 0.922, 16: 0.969
    r * measured: 1: +0.009151, 2: +0.006314, 3: +0.003456, 4: +0.001912, 6: +0.000912, 8: +0.000728, 12: +0.000288, 16: -0.000432
    continuum h/(4 pi beta) = 0.006631
    forward minus backward along the body diagonal: 1: +0.005985, 2: +0.003301, 3: +0.002246, 4: +0.001708, 6: +0.001133, 8: +0.000807

  off-grid, dim 3s, beta = 6, L = 16, T = 600, h = 0.5, seed 1: measured/linear 0.990, 0.989, 0.990, 0.987 at r = 1..4
  off-grid, dim 3,  beta = 6, L = 16, T = 600, h = 0.5, seed 1: measured/linear 0.962, 0.966, 0.963, 0.930 at r = 1..4

MISSING (46 of 48; run.py prints each as an `extra` string)
  dim 3s and dim 3, beta = 1, 2, 3, 6, 12, L = 32 and 48, T = 2000, T0 = 800, h = 0.5, seeds 1 and 2
    (all 40 except '3s 1 32 2000 800 0.5 1' and '3 6 48 2000 800 0.5 1')
  the h scan: 3s, beta = 3, L = 32, h = 0.1, 0.25, 1, 2, seed 1
  the 2+1 comparison: '2s 6 128 3000 1200 0.5 1' and '2 6 128 3000 1200 0.5 1'
  the larger planes: '3s 6 64 1500 600 0.5 1' and '3s 3 64 1500 600 0.5 1'

Items (1) to (4) of the task all need the missing points:
  (1) c_R(beta) needs both seeds at every beta;
  (2) the plateau and its bending need L = 48 and 64;
  (3) linearity in h needs the four h values;
  (4) the asymmetry needs the backward lattice at more than one coupling.
No HIT: nothing here contradicts the task's expectations, which are not testable with two points.
