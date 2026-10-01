# Campaign 7 (2026-10-01): probable work and negatives, deferred to the backlog

Owner rule (2026-09-26): only validated science that moves the program forward goes into a PR; probable work goes here.

## 1. A Gaussian long-wavelength guide does not cure lineage collapse (8^3, float, clean negative)
`gguide_lib.py` implements psi_T = exp(alpha N_flip - sum_q beta_q |O_q|^2) for the ring projector (class-sum scheme, O(K) per hop;
E_L validated to 3e-15 against brute force, hop law by chi-square, exact 2^3 at beta = 0). On 8^3 (960 walkers, 4 seeds) beta in
{0, .25, .5, 1, 1.5} leaves the ESS fraction (0.990), the walker log-weight spread (0.096-0.098) and the distinct-ancestor fraction at
lag 1 (0.086-0.092) and lag 2 (0.024-0.027) unchanged; a calibrated four-triple guide gives -17% in sd(log mean weight) only.
Why (measured): walker E_L has sd 6.6; the 12 lowest modes carry about 2% of Var(E_L); the count of ADJACENT FLIPPABLE PLAQUETTE PAIRS
explains 45% (R^2 0.012 -> 0.466, `elreg.py`); E_L stays correlated for about one time unit (C(0.1) = 0.50, C(1) = 0.07, `elcorr.py`),
so the accumulated log weight has sd 3.8 per unit time and lineages coalesce. alpha scan (beta 0): alpha = 0.2 is near-optimal; at
alpha = 0 (1.4% distinct ancestors at lag 1) u(Lc=0) = 0.2859, i.e. the energy bias tracks lineage collapse on 8^3 itself -- supports the
effective-population explanation of the large-torus energy offset (campaign 6 item 1). Next: a pair-plaquette Jastrow guide
(exp(alpha N_flip + gamma N_pair), cf. Sikora et al. PRB 84 115129) -- in progress at the end of campaign 7 (see its outcome below if added).

## 2. Reptation renewal-rate formula overstates renewals by 12-60x
The campaign-5 reptation notes (probes/work/campaign5-probable-20260926/reptation/RESULTS.md, rq_L.py printout) estimate renewals as
moves / (M^2 (1 - acceptance)). A renewal needs the path's signed shift to span one path length (only then is the interior replaced).
Measured: 8^3, 1600 x 0.0125, acceptance 0.954, 4e6 moves: formula 34 renewals, actual shift range 0.56-1.24 path lengths (6 chains);
6^3 same settings, 4e6 moves: formula 52, actual 0.94-2.22; 4^3, 192 x 0.1, 4e5 moves: formula 87, actual 1.9-7.5. Path motion is
sub-diffusive (8^3 D_eff = <shift^2>/lag: 0.55, 0.32, 0.17, 0.08, 0.03 segments^2/move at lags 1e4, 3e4, 1e5, 3e5, 1e6). Mixed END
energies need only end-local equilibration, so the landed 8^3 reptation curvature values are not shown wrong; printing the shift range
in that runner would settle it.

## 3. Population-free pure S on 8^3 (open)
The middle-of-path reptation estimator is validated on 2^3 (exact), 4^3 and 6^3 (agrees with forward walking at 3840 walkers; a PR
runner was prepared). On 8^3 the path is too slow: `rept8_S.py` (4 canonical-start chains, path 20, burn-in to 2.5 path lengths) needs
about 1 hour for +-0.02. Population-free MIXED S on 8^3 = 0.5715 +- 0.0028 (13 chains), u_ends = 0.28869 +- 0.00003.

`LIT_SUMMARY.md`: the campaign-7 literature lens (population-control bias N_w^-k, Nemec N_eff, genealogy theory, quantum-ice guides).
