# Assumptions And Imports

## Supplied Packet

- P1: `eta = C * m_DM^2`
- P2: `m_DM = N_sites * v = 16 * v`
- P3: `Omega_b h^2 = 3.6515e-3 * eta_10`
- P4: `x_F in [22, 28]`
- P5: `g_* = 106.75`
- P6: `K = 1.07e9 GeV^-1`
- P7: `S_vis/S_dark in [1.4, 1.7]` and `alpha_X = alpha_LM`

## Framework Inputs

- `R_base = 31/9`
- ETA 188 structural decomposition as a cross-check, not as a numerical input

## Remaining Open Imports

P1 and P2 are the load-bearing physics gates. This branch does not derive the
freeze-out-bypass identity or the `N_sites * v` dark-mass route.

