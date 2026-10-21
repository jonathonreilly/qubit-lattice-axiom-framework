---
claim_id: regge_action_per_cell_and_the_conditional_gravity_coupling_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite deterministic diagnostics on the supplied Kuhn cubic and coned D4 Regge carriers: the long-wavelength ratio of the Regge second variation to the Einstein-Hilbert second variation per unit cell, the static response to a point deposit, and the conditional coupling G = a^2/(8 pi kappa) for an action kappa sum A delta; the value of kappa, the rung on which areas are counted, any induced coupling and any physical Newton constant or Planck identification are not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/regge_action_per_cell_and_the_conditional_gravity_coupling_2026_10_21.py
---

# The Regge action per cell and the conditional gravity coupling

Claim type: bounded_theorem.
Primary runner: `scripts/regge_action_per_cell_and_the_conditional_gravity_coupling_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its record source and a lossless edge-length response give the linearised Einstein operator, but not its strength. This note computes what a Regge action kappa sum_t A_t delta_t, with areas in units of the cell and deficits in radians, gives per cell. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the carriers nor kappa.

## Units

The relay energy is measured in radians of phase per tick and the record source deposits it on unit steps at the top speed. In those units hbar = 1, the top speed is 1 and the block spacing a is 1, so the coupling is a pure number, and the only free coefficient left in a Regge geometry phase is kappa.

## Regge against Einstein-Hilbert per cell

Let Q(k) be the Bloch Hessian of sum A delta over edge lengths; by Schlaefli it is sum_t dA_t (x) d delta_t at the flat background. The line-integrated metric reading turns Q into a 10x10 form K(k). The continuum comparison is the second-order part of sqrt(g) R, -1/4 (d h)^2 + 1/2 (div h)^2 - 1/2 div h . d tr h + 1/4 (d tr h)^2 up to divergences. For h = Re(H e^{ikx}) the cell sum of sum A delta at second order is H^dag K H / 4 and the cell integral of sqrt(g) R is H^dag F H / 2. At long wavelength H^dag K H / H^dag F H tends to 1 on both carriers: within 4e-4 for random H and 3e-5 for the transverse traceless wave on the Kuhn cubic (15 edges, 50 hinges per cell), within 3e-7 with the analytic-derivative Hessian of the repo Regge code, and within 2e-5 on the coned D4 (72 edges, 208 hinges). So sum A delta is (1/2) int sqrt(g) R per unit cell, and kappa sum A delta is the Einstein-Hilbert action with G = a^2/(8 pi kappa).

## A point deposit

At zero tick-momentum h_tt is gauge invariant, and stationarity with source term (1/2) h T gives h_tt = -(E/2 kappa)[K^+]_tt. In momentum space k^2 h_tt tends to E/kappa on both carriers within 4e-5, the lattice form of 8 pi G E / k^2. On a 24^3 torus with kappa = 1, fitting h_tt = 8 pi c E G_lat(r) + const over 4 <= r <= 9 gives c = 0.03965 with residual 1.9% on the coned D4, against 1/(8 pi) = 0.03979, and 0.03976 after 2^3-block averaging. The raw Kuhn cubic fit gives 0.0392 with residual 78%, dominated by soft zone-boundary modes near (pi,pi,pi), the orthoscheme soft-mode defect already recorded for this carrier. After averaging over 2^3 blocks it gives 0.03981 with residual 1.3%.

## Candidate normalisations

Reading one radian of deficit per radian of phase gives kappa = 1 and c = 1/(8 pi); a full-turn unit gives kappa = 1/(2 pi) and c = 1/4. Fixing one quantum per deposit per tick does not determine kappa, since the on-shell dressing of a static deposit per tick is X E^2/kappa with one lattice constant (X = -0.05258 on the coned D4, 24^3 torus), and fixing it to one quantum would make kappa depend on E and so single out a state. The record-removal clause does not fix the size of the share, so no coupling follows from it.

## Scope

Supplied: the carriers, flat Euclidean lengths, the metric reading, the action sign, the tick index, the equation of a deficit radian with a phase radian, the rung on which areas are counted (for 2^3 blocks, c per site is 1/(2 pi)), the torus, the fit window and the pseudo-inverse cutoff. Carrier independence is shown for two carriers at long wavelength only, and any coupling induced by the odds is not included. No physical Newton constant or Planck identification is established.
