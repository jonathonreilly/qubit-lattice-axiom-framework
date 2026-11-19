---
claim_id: fine_rate_octree_ladder_charged_coarse_sea_magnetic_response_doubles_per_rung_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "On the supplied octree ladder ticked at the fine rate and gauged by a U(1) that commutes with the ladder, coarse modes carry the fine charge, a rung-j plaquette carries 4^j times the fine flux, and the B^2 response per volume scales as 2^j per rung (E^2 as 2^-j); finite gapped tori give a positive bulk rung coefficient; estimated against measurement, the resulting magnetic running is excluded, so the gauged fine-rate octree route fails; no escape route is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/fine_rate_octree_ladder_charged_coarse_sea_magnetic_response_doubles_per_rung_2026_10_21.py
---

# On the fine-rate octree ladder the charged coarse sea's magnetic response doubles per rung

Claim type: bounded_theorem.
Primary runner: `scripts/fine_rate_octree_ladder_charged_coarse_sea_magnetic_response_doubles_per_rung_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. One of its routes to chirality hides the mirror by ticking every rung of an octree ladder at the fine rate. This note gauges that ladder and asks what the coarse rungs do to the photon. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the ladder nor its rate.

## Statement

On the supplied octree ladder ticked at the fine rate:

1. A rung-j plaquette carries 4^j times the fine plaquette flux, gauge invariantly.
2. The ladder graph is connected, so a U(1) that commutes with it gives every coarse mode the fine charge.
3. Per unit volume the rung-j response to B^2 scales as 2^j, to E^2 as 2^-j and to B^4 as 32^j. So d(1/mu)_j = 8 pi alpha q^2 (c_b/v) 2^j while the electric correction converges, and the magnetic and electric photon coefficients run differently.

Negative result: on finite gapped tori the bulk rung coefficient c_b is positive, so the vacuum's magnetic stiffness grows linearly with wavelength. Estimated against measurement, this is excluded by more than 30 orders of magnitude.

## Derivation

A coarse plaquette encloses 4^j fine plaquettes, and by Stokes any local covariant transport gives the enclosed flux up to O(dF) corrections. The ladder is one connected component, so a U(1) commuting with the ladder Hamiltonian is constant on it; neutral coarse modes would let the light-sector charge leak through the ladder couplings. A rung-j cell has volume 8^j and, at the fine rate, a mode on it moves at 2^j times the light speed. Counting the energy per rung-j cell in ticks gives the powers 2^j, 2^-j and 32^j.

The field also induces compensating modes. Flux F gives exactly |F| rung-0 lowest-Landau-level branches and |F| branches of opposite slope one rung up, moving at <2^j> times the light speed. Every anomaly-free charge has zero net inflow (sum q^3 = 0), but the branches are not neutral: the conductance along B adds as sum |q|^3 per channel, which never cancels.

## Checks

The runner ends with `TOTAL: PASS=10 FAIL=0`. Its lines:

- `[PASS] A1 THEOREM coarse holonomy = enclosed flux: rung-j plaquette phase = 4^j x fine plaquette flux, gauge invariant ... max error 4e-15`.
- `[PASS] A2 THEOREM the ladder graph is connected, so a U(1) commuting with it gives coarse modes the fine charge ... components 1 of 288 modes`.
- `[PASS] A3 THEOREM power counting at the fine rate ... B^2 per volume x 2^j, E^2 x 2^-j, B^4 x 32^j ... exact for j = 0..5`.
- `[PASS] B1 R = 1, 16x16x4: flux F gives |F| rung-0 lowest-Landau-level branches and |F| compensating branches of opposite slope on rung 1`, with velocity ratios 1.86, 1.86, 1.82 against <2^j> = 1.98, 1.98, 1.93.
- `[PASS] B2 R = 2: the compensating branch moves at <2^j> times the light speed ... (8, 8, 8): 2.20 vs 2.23; (16, 8, 8): 2.77 vs 2.92`.
- `[PASS] B3 DIAGNOSTIC hybridisation of rung-0 and compensating branches ... gap F=1,2,3: 4.0e-04, 6.9e-04, 7.6e-04 rad/tick (bulk gap 1.6e-2)`.
- `[PASS] C1 DIAGNOSTIC 32x32x8-equivalent tori (Bloch twists): gapped ..., quadratic in flux ..., field costs energy (diamagnetic) on every rung | ... c(2)/c(1) 0.996, 0.956`.
- `[PASS] C2 DIAGNOSTIC per-site coefficients ... c0 5.99e-04; c1 2.15e-03 = 7.18e-04 (rung 0) + 1.44e-03 (rung 1)`, giving c_b = 8.4e-4 in rung units.
- `[PASS] C3 DIAGNOSTIC rung locality of the self-similar recursion ... A(R=1) -9.6894e-03, A(R=2) -9.6396e-03`: the coefficient doubles per rung.
- `[PASS] D1 estimates: bulk stiffness exceeds the light-speed bound by > 1e30, the static/atomic ratio by > 1e10, PVLAS by > 1e40`.

The ladder was gapped with a species mass mu = s t on every rung, only so that the field energy is analytic. An exploration run outside the runner gave c_b = 8.2e-4, 1.3e-3 and 1.75e-3 at mu = s t, 0.5 s t and 0; it is positive in every case tried.

## Estimates against measurement

These are estimates from the finite coefficients above, not theorems. Summed over one family, K = 8 pi alpha (16/3) c_b/v = 0.018, so d(1/mu) is about 1.7e20 at the electron Compton length, 3.5e26 at 1 micron and 2.3e31 at 0.1 m.

- Photon against matter speed at 1 micron: a predicted ratio of order 1e13, against the bound |dc/c| < 3e-19.
- Lab-scale against atomic-scale 1/mu: a predicted factor 1.4e11, against current balances that agree with alpha to about 1e-6.
- PVLAS at 2.5 T: a predicted bulk anisotropy of order 1e24, against Delta n = (12 +- 17)e-23. The compensating modes alone give about 4e-19 in an assumed geometry.
- Magnetars at 1e10 T: the observed X-ray polarisation matches QED vacuum physics, against a predicted anisotropy of order 1e19.
- Penning-trap g-2: loop photons at k ~ m_e would see d(1/mu) ~ 2e20, an O(1) change, against agreement with QED to about 1e-10.

The compensating modes themselves are nearly sterile. With a = sqrt(8 pi) l_P and a landing threshold of pi/4 plaquette flux they land on rung j* = 87 at 1 T, as gapless chiral branches moving at about 1.5e26 c, with an extrapolated amplitude overlap of about 1e-2303 with rung 0 and a density of states suppressed by c/v = 6e-27.

## Boundary

Supplied: the octree sites, the fine rate, the ladder couplings and masses, mu, the tori and twists, axis-ordered transport, the filled sea as vacuum, a = sqrt(8 pi) l_P, the pi/4 landing threshold and the PVLAS geometry. Cited: the earlier octree-ladder overlap law and the measured values. The filled sea is not optional here: measured light-by-light scattering and the running of alpha require it, and the photon couples to the conserved total current. The register's dressed-coupling clause fixes one wavelength only and cannot remove a running that grows with wavelength. A per-rung counterterm -c_b would have to be tuned (c_b depends on mu) and would have to cancel every order, which amounts to a new supplied clause. Ticking coarse rungs at the zoom rate keeps the mirror light and adds charged states at every mass scale. The result is consistent with the main notes showing that lattice orbital responses are generically nonzero. No escape route is established.
