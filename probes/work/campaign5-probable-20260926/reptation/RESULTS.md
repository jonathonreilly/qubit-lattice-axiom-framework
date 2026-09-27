# Reptation results (Campaign 5, 2026-09-26)

Library `rq2_lib.py`: one continuous-time importance-sampled path (ring buffer of segments), moves accepted with min(1, exp(W_new - W_old)), bounce on rejection; mixed energy at the ends, pure link/plaquette event densities in a middle window, optional diagonal probe field and guide field, and window integrals of chosen link modes. `rq_lib.py` is the earlier version used by `rq_test.py`.

Validated (and landed in open PRs 9352 via its runner): rate tables exact against brute force on 3^3/4^3 with charges; exact 2^3 control of mixed energies and the three-point curvature; 8^3 curvature 1.088 / 1.041 in two guide schemes.

Charged ring clause (H = -g sum(U + U^dag) - t sum sigma^x + M sum Q^2, g = 1, M = 2), 6^3, t = 0.25, guide exp(0.2 N_flip - gam sum Q^2):

| path | gam | <sigma^x> (middle) | E(ends) |
|---|---|---|---|
| 20 | 1.2 | 0.1142 +- 0.0037 | -195.036 +- 0.063 |
| 20 | 1.7 | 0.0989 +- 0.0036 | -195.718 +- 0.048 |
| 40 | 1.2 | 0.1107 +- 0.0025 | -195.868 +- 0.048 |
| 40 | 1.7 | 0.0931 +- 0.0011 | -195.793 +- 0.071 |

At path 40 the end energies agree; the pure link expectation differs by 6.5 sigma and its profile along the path is flat at a guide-dependent level in both runs.

Pure ring at t = 0: end energy per plaquette approaches its value slowly (still rising after 8-20 renewals at path 20: 8^3 .2865 -> .2882, 12^3 .2842 -> .2867, 16^3 .2835 -> .2853); the approach slows sharply with the torus, so 16^3 estimates from this guide are unreliable (a 16^3 run with 1.3 renewals gave u = .2841 and chi = 1.59, discarded).

Window fluctuations (`rq_chi_test.py`, `rq_L.py`): on exact 2^3 the mode-averaged a_m = 2.917 against 2.9175. On 8^3 (path 40, window 10): k = pi/4 single-exponential fit Delta = 0.550 +- 0.053, chi = 1.41 +- 0.14; k = pi/2 Delta = 1.18 +- 0.08, chi = 1.50 +- 0.07; the three-point energy estimate at pi/4 is 1.12.
