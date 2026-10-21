---
claim_id: partition_link_leapfrog_matches_fermion_band_and_symmetric_source_fixes_shared_light_cone_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied massless fermion tick and supplied link discretisations: a leapfrog with E on even-partition links and B on the dual odd-partition links at Courant number 1/sqrt(3) has exactly the fermion band at every sampled K, with static Gauss modes and a zone-corner Jordan block; link placements on the individual site hops or in continuous time match only at leading order; and a source is symmetric in g = diag(-alpha,1,1,1) only if alpha = d(w^2)/d(K^2), which is 1/3 for both the fermion and the partition links, giving c_grav = c_fermion at leading order. Comparisons with ultra-high-energy cosmic-ray, photon-decay and GW170817 bounds are estimates. No link law, placement, value of alpha or interacting light cone is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/partition_link_leapfrog_matches_fermion_band_and_symmetric_source_fixes_shared_light_cone_2026_10_21.py
---

# A partition-link leapfrog matches the fermion band, and a symmetric source fixes a shared light cone

Claim type: bounded_theorem.
Primary runner: `scripts/partition_link_leapfrog_matches_fermion_band_and_symmetric_source_fixes_shared_light_cone_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its fermion tick has a light cone, but nothing in it fixes the speed of link quanta or of the geometry's waves. This note compares three link discretisations with the fermion band and asks what a symmetric stress tensor requires of the flat background. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the discretisations used. Units: K in blocks, w per tick.

## The fermion band

At mu = 0 the block hop W is Hermitian with W^2 = 1, and all 8 bands obey cos w = S(K) over 2000 K to 1.0e-15. The cone speed is 1/sqrt(3), with phase-velocity coefficient (3 A4 - 1)/24 along the axis, face and body directions (0.0833, 0.0208, 0.0000).

## Links on the two partitions

Put E on the links between even-block centres and B on the links between odd-block centres; the odd-block lattice is the dual of the even one. Each half-tick advances one field by C times the curl of the other, giving sin^2(w/2) = C^2 sum sin^2(K_i/2).

- At C = 1/sqrt(3) both transverse polarisations have exactly the fermion band at every K: maximum difference 1.2e-14 over 2000 K, polarisation splitting 9.3e-15.
- The longitudinal Gauss modes are static (eigenvalue 1 to 2.4e-15).
- C = 1/sqrt(3) is the stability edge: |eig| = 1 just below and 1.0935 just above.
- At K = pi(1,1,1) the transverse map is a Jordan block, so there is no link vacuum at that one point.
- At C = 0.5 or 0.55 the link speed is C, so the leading-order cone differs from the fermion's.

## Links on the site hops, and in continuous time

One leapfrog per tick on the site hops would need Courant number 2/sqrt(3), which is unstable (maximum |eig| = 13.72). One leapfrog per half-tick has c = 1/sqrt(3), but its O(K^2) coefficient is (3 A4 - 1)/96, a quarter of the fermion's, so these links are faster than fermions by (3 A4 - 1) w^2 / 32 (0 to 1/16). Continuous-time lattice links are slower than fermions by w^2/24 in every direction.

## Gauge-covariant W

With phases on W's hops and a random face flux, W'^2 is not 1 and cos(mu/2) W' + i sin(mu/2) is not unitary (deviation 0.498; pure gauge gives 5.9e-15). The polar part sign(W') is unitary, squares to 1, is gauge covariant and reduces to W at zero flux, but it is a supplied fix. Neither choice fixes the links' own kinetic term or Courant number.

## The symmetric-source condition

For a band, energy flux divided by momentum density is d(w^2)/d(K^2). A source is symmetric in g = diag(-alpha, 1, 1, 1) only if alpha equals that ratio. The fermion and the partition links both give 0.33333332 at long wavelength, and the two ratios agree at every K to 8.8e-12. A massive band has rest-frame ratio (1/3)(mu/2) cot(mu/2), checked at mu = 0.1 and 0.5, so its limiting speed lies below the cone by mu^2/24. The transverse-traceless wave cone is w = sqrt(alpha) K, so alpha = 1/3 gives c_grav/c_fermion = 1 at leading order; alpha = 0.6 gives 1.3416 and alpha = 1 gives 1.7321.

## Estimates against measurement

With w = E tau, tau = L_block/(sqrt(3) c) and a = sqrt(8 pi) l_P, at block = 2a:

- Continuous-time links make fermions faster by 9.4e-17 at 1e20 eV, 2.1e6 times the proton vacuum-Cherenkov threshold of 4.4e-23. This excludes them if protons carry the fermion's O(K^2) term. At block = a the ratio is 5.3e5.
- Half-tick site links make photons faster by at most 2.8e-26 at 1.4 PeV, below the photon-decay threshold of 2.7e-19 by 9.7e6. The cosmic-ray bound is one-sided: it applies only when fermions are faster.
- The massive offset mu^2/24 is 8.2e-39 for the proton.
- GW170817 (|c_g - c|/c below about 1e-15) allows alpha = 1/3, while alpha = 0.6 would miss by about 3e14.

## Checks

The runner prints `TOTAL: PASS=27 FAIL=0`. Its PASS lines cover the fermion band and its three directional coefficients, the partition-link band match, static Gauss modes, the zone-corner Jordan block, the stability edge, the two off-edge Courant controls, the unstable per-tick site leapfrog, the three half-tick site coefficients, the speed ordering, the gauge-phase unitarity failure and polar-part fix, the flux-to-momentum ratios, the massive offsets, the gravitational cone, and the cosmic-ray, photon-decay and GW170817 estimates.

## Supplied and boundary

Supplied: the discretisations and their placement, the tick as time step, the unit map, and the energy-flux reading of the source with canonical quasi-momentum. The symmetric-source condition fixes only the leading order; the all-order match comes from the supplied partition placement. Loop corrections in an interacting theory, the composite proton's O(K^2) term and the zone-corner Jordan block are not resolved. No link law, placement, value of alpha or interacting light cone is established.
