---
claim_id: floquet_sea_vacuum_source_is_zero_planckian_or_mass_dominated_not_measured_lambda_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied block tick and supplied half-filled sea: det U(K) = 1 so the 8 quasi-energies sum to 0; at mu = 0 the sea phase is exactly -2 pi per block per tick, which is 0 mod 2 pi but -pi/4 per site under the generator reading; mass leaves a residual -I0 mu^2 per block, a supplied Hartree condensate rule leaves -(a/16) mu^4 ln(1/mu) per site, a supplied one-block model's vacuum is undressed, a supplied counter-rotating variant shifts it by -(g^2/2) cot(Delta/2) with a balanced-channel sum rule, and the sea's pressure depends on the zone cut. Unit-mapped values and record-noise wander are compared with measured rho_Lambda as estimates. No vacuum, log branch, unimodular reading or value of Lambda is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/floquet_sea_vacuum_source_is_zero_planckian_or_mass_dominated_not_measured_lambda_2026_10_21.py
---

# The Floquet-sea vacuum source is zero, Planckian or mass-dominated, not the measured Lambda

Claim type: bounded_theorem.
Primary runner: `scripts/floquet_sea_vacuum_source_is_zero_planckian_or_mass_dominated_not_measured_lambda_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its geometry law sources curvature by the generator i log U of the tick. This note computes what a supplied half-filled sea sources under that law and its alternatives, and compares the results with the measured vacuum density. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used, and main chooses no vacuum, so the sea is supplied.

## Sum rules and the sea phase

Write the block hop as W(mu) = e^{i mu/2} exp(i(pi - mu) P_-) with rank P_- = 4. Then det U(K) = 1 at every K, so the 8 quasi-energies sum to 0. This cancels only the all-empty and all-full fillings. The spectrum is symmetric under w -> -w with 4 bands of each sign at every K (checked at mu = 0.37).

At mu = 0 the shift K -> K + pi(1,1,1) maps |w| to pi - |w|, so the filled bands of each such pair sum to -4 pi (maximum deviation 5.3e-15). The sea phase is -2 pi per block per tick (runner value -6.283185307180). Read mod 2 pi it is 0, and the vacuum odds return each tick. Read through the generator it is -pi/4 per site per tick. The register does not choose between these readings.

## Mass, condensate and dressing

- Floquet Hellmann-Feynman: dE_sea/dmu = -<B> per block per tick, to 2.2e-9. The residual is E_sea(mu) + 2 pi = -I0 mu^2 (1 + O(mu^2 ln mu)) with I0 = 1.1567154153; at mu = 0.05, 0.1 and 0.2 the residuals are -2.8865e-3, -1.1517e-2 and -4.5680e-2 against -I0 mu^2 = -2.8918e-3, -1.1567e-2 and -4.6269e-2.
- Supplied Hartree condensate rule: at the gap root the mu^2 term cancels and leaves -(a/16) mu^4 ln(1/mu) + O(mu^4) per site, with a = 3 sqrt(3)/(2 pi^2). The integration-by-parts check gives -2.500315e-4.
- Supplied one-block model with coupling a+ b+ c + h.c.: it conserves a number, so the empty state is an exact Floquet eigenstate with phase 0. The dressed vacuum is the bare vacuum and its Born-mean source is exactly 0.
- Supplied counter-rotating variant a+ b+ c+ + h.c.: the dressed vacuum's quasi-energy is -(g^2/2) cot(Delta/2) + O(g^4), with Delta the quasi-energy of the state it couples to. With the rotating coupling off the formula matches to 2.5e-4. It vanishes at Delta = pi and flips sign above.
- Floquet sum rule: channels at Delta and 2 pi - Delta cancel the shift. In the balanced toy the shift is -2.2e-16 at g = 0.02 and -1.4e-16 at g = 0.3, against -2.9227e-4 for one channel.

## The vacuum equation of state is not fixed

At mu = 0 the sea's kinetic stress depends on where the momentum zone is cut. The zones [-pi, pi) and [0, 2 pi) give p = -1.4936 and +1.4936 per block with rho = -6.2832, so w = p/rho = +0.2377 or -0.2377. Neither gives w = -1.

## Estimates against measured Lambda

With a = sqrt(8 pi) l_P and tau = 2a/(sqrt(3) c), the measured value (Planck 2018, Omega_L = 0.6847 +- 0.0073, H0 = 67.4 +- 0.5) is rho_L = 5.251e-10 J/m^3 = 1.133e-123 rho_P, nonzero at more than 90 sigma.

| source | rho / rho_P | ratio to measured |
|---|---|---|
| massless sea, generator reading | 1.08e-3 | 9.5e119 |
| massless sea, phase mod 2 pi | 0 | excluded |
| relays counted relative to the sea | 0 | excluded |
| fixed mass, electron | 1.16e-47 | 1.0e76 |
| fixed mass, top | 1.33e-36 | 1.2e87 |
| condensate, electron | 3.87e-90 | 3.4e33 |
| condensate, top | 3.76e-68 | 3.3e55 |
| condensate, 50 meV neutrino | 4.70e-118 | 4.1e5 |

If gravity is unimodular and each relay forms one record per half-tick with independent zero-mean jumps, the rms wander over the Hubble volume after 13.8 Gyr (2.8e60 half-ticks) is 1.6e-139, 4.2e-137 and 8.2e-134 rho_P for relic neutrinos, electrons and baryons. Only Planck-size jumps reach the measured scale, and they overshoot at 2.1e-110. A Sorkin-type scaling rho_P/sqrt(N) over the Hubble 4-volume, which is not in the register, gives 1.9e-121 rho_P counted in cells and 6.9e-123 counted in Planck 4-volumes. It needs cell-count fluctuations that a regular lattice lacks.

## Checks

The runner prints `TOTAL: PASS=15 FAIL=0`. Its PASS lines cover det U = 1, the w -> -w symmetry, the pair sum at mu = 0, the sea phase, Hellmann-Feynman, the fixed-mass residual, the zone-dependent pressure, the undressed vacuum, the counter-rotating shift, the balanced sum rule, the condensate consistency and its mu^4 ln residual, the measured significance, the absence of any rule-level source within three orders of measured, and the record-noise wander.

## Supplied and boundary

Supplied: the block hop and mass parameter, the sea filling, the log branch, the one-block couplings (the counter-rotating term is a variant), the condensate rule and Hartree approximation, the unit map, the unimodular reading, the jump sizes and the particle densities. Counting relays relative to the sea sets the vacuum to zero by construction. Measured comparisons are estimates. No vacuum, log branch, unimodular reading or value of Lambda is established.
