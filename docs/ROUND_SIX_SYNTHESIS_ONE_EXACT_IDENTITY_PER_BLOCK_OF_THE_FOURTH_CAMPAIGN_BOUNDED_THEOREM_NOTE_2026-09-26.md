---
claim_id: round_six_synthesis_one_exact_identity_per_block_of_the_fourth_campaign_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Recomputes one exact or reference identity per block of the fourth campaign on its supplied models: the four-site Bloch reduction of the u = +1 quadratic Majorana comparator against the 32-site torus levels; the rational-momentum characteristic polynomial at f = (1/4, 3/4, 1/2); on the line f = (x, 1 - x, 0) the determinant identity D = 16 N^2, the identity C = (w d/dw)^2 D at w = 1 = -64 [(1 + c)(J + 2) - J^2]^2 / (1 + c) on N = 0, and their joint solution kappa^2 = J (J + 2) / (4 (4 + 2J - J^2)); the zero-determinant root at J = 1; the projected-comparator energies of the 32-site flux-free and exception candidates at kappa = 0.3 and the exception repeated onto 64 sites; the numerical Lanczos Ritz reference of the full 2^3 charged torus at t = 0.35. No new result; each block's own note governs its scope."
upstream_dependencies:
  - minimal_axioms
  - composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
  - composite_site_network_the_half_fluxed_sectors_that_undercut_the_flux_free_one_on_32_and_64_sites_lose_when_repeated_onto_larger_clusters_bounded_theorem_note_2026-09-26
  - ring_model_single_link_charge_hopping_the_projector_misses_the_exact_2_cubed_energy_with_a_mismatched_guide_and_its_6_cubed_energy_spans_two_percent_across_guides_bounded_theorem_note_2026-09-26
runner: scripts/round_six_synthesis_one_exact_identity_per_block_of_the_fourth_campaign_2026_09_26.py
---

# Round-six synthesis: one exact identity per block of the fourth campaign

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** recomputation of exact algebra and numerical references from the campaign's notes; unaudited.

## The blocks, in their reviewed scope

- **The composite-site comparator's bands.** The landed note
  `COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md`
  retains an exact four-band reduction, a rational-momentum polynomial,
  exact identities on one momentum line and the analytic Lipschitz
  inequality. Its adaptive searches give numerical groups (two below the
  split, six above), not certified node counts.
- **The slice fluxes (open PR 9300).** On the same line the zero-determinant
  root has a closed form. Discrete slice fluxes averaged along each axis
  come close to the value that root gives.
- **Flux candidates (landed).**
  `COMPOSITE_SITE_NETWORK_THE_HALF_FLUXED_SECTORS_THAT_UNDERCUT_THE_FLUX_FREE_ONE_ON_32_AND_64_SITES_LOSE_WHEN_REPEATED_ONTO_LARGER_CLUSTERS_BOUNDED_THEOREM_NOTE_2026-09-26.md`:
  the tested half-fluxed candidates that undercut the flux-free one on 32
  and 64 sites lie above it when repeated onto larger clusters. These are
  finite candidate comparisons.
- **Moving charges (landed).**
  `RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_THE_PROJECTOR_MISSES_THE_EXACT_2_CUBED_ENERGY_WITH_A_MISMATCHED_GUIDE_AND_ITS_6_CUBED_ENERGY_SPANS_TWO_PERCENT_ACROSS_GUIDES_BOUNDED_THEOREM_NOTE_2026-09-26.md`:
  the finite-population projector's energy depends on the guide. Open PR
  9306 finds that even the energy-minimising penalty leaves a 6³ energy
  that falls when the population doubles.
- **The photon (open PR 9298).** A finite curvature estimate on 24³ at
  `k = π/12` gives an estimated upper bound on the selected component and
  leaves open whether the susceptibility falls at the smallest momenta.

## The identities recomputed

1. **Bloch reduction.** The four-site Bloch matrix of the `u = +1`
   comparator at `κ = 0.3` reproduces the 32 levels of the 32-site torus to
   `10⁻¹²`.
2. **Rational momentum.** At `f = (1/4, 3/4, 1/2)`, `J = 1`, the
   characteristic polynomial is exactly
   `(λ² − 48(1/2 − κ)²)(λ² − 48(1/2 + κ)²)`.
3. **The line identities.** On `f = (x, 1 − x, f₃)` with `J_x = J_y = 1`,
   `J_z = J`, `c = cos 2πx` and `w = e^{2πif₃}`: at `w = 1`, `D = det H = 16 N²`
   with `N = J² + 4c²κ² − 2c − 4κ² − 2`. On `N = 0`,
   `C = (w ∂_w)² D |_{w=1} = −64 [(1 + c)(J + 2) − J²]² / (1 + c)`.
   Solving `C = 0` with `N = 0` gives `κ² = J(J + 2)/[4(4 + 2J − J²)]`, which is
   `3/20` at `J = 1`. `C` is minus `(2π)⁻²` times the second derivative of `D`
   in `f₃`.
4. **The zero-determinant root.** At `J = 1` the root of `N = 0` in `(−1, 1)`
   is `c = −(1 + 4κ²)/(1 + √(1 + 4κ² + 16κ⁴))`.
5. **The 32-site candidates.** At `κ = 0.3` the flux-free and exception
   candidates have projected-comparator energies `−84.81708` and
   `−85.64104` (16 of 32 ten-loops at `−1`); repeated onto 64 sites the
   exception lies above the flux-free energy there.
6. **The charged torus.** On the full `2³` torus (all 24 links carry
   `−t σ^x`, 2²⁴ states), `t = 0.35`, `M = 2`, the Lanczos Ritz reference
   is `−9.631658548`.

## What stays open

- **Moving charges:** a controlled `⟨σ^x⟩(t)` on `6³` and larger tori.
- **The comparator bands:** certified node counts and continuum Chern
  numbers, and which sector is the ground sector of the spin model.
- **The photon:** whether the susceptibility stays flat at the smallest
  momenta; more seeds and one guide for all probe fields.

## Boundary

This note recomputes identities and adds no new result. Supplied models;
no phase, limit or physical identification.

## Reproduction

```bash
python3 scripts/round_six_synthesis_one_exact_identity_per_block_of_the_fourth_campaign_2026_09_26.py
```

Six checks; prints `TOTAL: PASS=6 FAIL=0` in about 50 s.
