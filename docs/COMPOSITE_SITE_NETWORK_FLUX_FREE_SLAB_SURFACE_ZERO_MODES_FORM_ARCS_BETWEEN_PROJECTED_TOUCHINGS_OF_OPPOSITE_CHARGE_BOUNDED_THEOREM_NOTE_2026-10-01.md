---
claim_id: composite_site_network_flux_free_slab_surface_zero_modes_form_arcs_between_projected_touchings_of_opposite_charge_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J_x = J_y = J_z = 1, odd term kappa = 0.3 and 0.6, four-site Bloch matrix H(f) = i M(f). Finite-slab floating-point diagnostics: slabs open along the primitive translation a3 (N = 40 layers, the cell cut and one shifted cut), periodic along a1, a2, on an 80 x 80 surface grid. The slab construction reproduces the bulk (periodic closure to 1e-14). The floating FHS values on the sampled slices f1 = const agree within each sampled interval and their observed changes equal -chi, chi the landed chirality computed at the exact family positions (kappa 0.3: C = 1, 0; kappa 0.6: 1, 0, -1, 0, -1, 0). On the top surface the zero contour of the slab (a jump of the negative-energy weight on the top half) consists of open arcs whose closest approach to the projected touchings is 0.005 to 0.014 and which join touchings of opposite charge (one arc at kappa 0.3, three at kappa 0.6), plus a straight line u = 1/2 for the cell cut; the net spectral flow of the contour across a surface circle equals the slice Chern number on 78 to 80 of 80 circles, the exceptions lying within 0.001 of a touching coordinate. Which touchings an arc joins depends on the termination: at kappa 0.6 the cell cut pairs (0,5), (1,2), (3,4) and a shifted cut pairs (0,3), (1,4), (2,5). No certified statement, arc endpoint at a touching, intrinsic pairing, other couplings, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_slab_surface_zero_mode_arcs_2026_10_01.py
---

# Slab surface zero modes of the flux-free comparator form arcs between projected touchings of opposite charge

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** finite-slab floating-point diagnostics; unaudited.

## Supplied setting

Use the supplied comparator and the exact touching families of the landed note
[current mathematical parent](COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md)
at `J = (1, 1, 1)`:
- `κ = 0.3`, with two line touchings of opposite charge;
- `κ = 0.6`, with two line touchings and four plane-(iii) touchings.

The charge is the landed chirality `sign Im Tr(P∂₁H P∂₂H P∂₃H)`, computed
here at the exact family positions.

**The slab.**
- **Geometry.** Keep `f₁`, `f₂` as momenta (periodic along `a₁`, `a₂`), and
  stack `N` copies of the four-site cell along `a₃` with open ends. This is
  the cell cut; a shifted cut relabels the sites' layers.
- **Surface signal.** For each `(f₁, f₂)`, take the weight of the slab's
  negative-energy subspace on the top half of the layers. A jump of that
  weight by more than one half across a grid edge marks a top-surface zero
  crossing.
- **Arcs and their ends.** The crossing edges form the zero contour. Its
  connected pieces that do not wrap the surface zone are the arcs. An arc's
  end distance is the closest approach of the arc to the projected touching
  nearest its end.

## Result

1. **Construction.**
   - The reconstructed bulk equals the landed Bloch matrix to `1e-15`.
   - The slabs are Hermitian.
   - Periodic closure reproduces the bulk spectrum, including a
     three-layer supercell, to `1e-14`.
2. **Numerical slice Chern values.** On the sampled tori `f₁ = const`, the
   rounded floating FHS values agree between the touchings' `f₁` values,
   and their observed changes equal `−χ`:
   - `κ = 0.3`: `C = 1` outside and `0` between the touchings at
     `f₁ = 0.355` (`+`) and `0.645` (`−`);
   - `κ = 0.6`: `C = 1, 0, −1, 0, −1, 0` across the six touchings.
3. **Arcs, cell cut, top surface, N = 40.**
   - `κ = 0.3`: one arc joins the `+` and `−` touchings, with end distances
     `0.005` and `0.005`.
   - `κ = 0.6`: three arcs, each joining a `+` and a `−` touching, with the
     pairing `(0,5)`, `(1,2)`, `(3,4)` and end distances `0.005` to `0.014`.
   - Both couplings also show a straight line `u = 1/2` that wraps the
     surface zone.
4. **Flow equals the slice Chern number.** The net spectral flow of the zero
   contour across a surface circle equals the slice Chern number:
   - on 80 of 80 circles at `κ = 0.3`;
   - on 78 of 80 at `κ = 0.6`, where the two exceptions lie within `0.001`
     of a touching coordinate.

   This holds on both surfaces, for both coordinates.
5. **Termination.** At `κ = 0.6` a shifted cut keeps three arcs of opposite
   charge but pairs them `(0,3)`, `(1,4)`, `(2,5)`, and the line `u = 1/2`
   is absent.

## What follows

- **Arcs connect opposite charges.** On these slabs the surface zero modes
  form arcs that run between the projections of touchings of opposite
  charge. The slice Chern numbers they carry change by the touchings'
  charges.
- **The pairing is not intrinsic.** Which touchings an arc joins depends on
  the termination, so this block asserts arcs of opposite charge and not a
  pairing.

## Boundary

- Everything is floating point on finite slabs.
- An arc's approach to a touching is resolved to the grid and the slab
  thickness; that it ends exactly at a touching is not shown.
- Other couplings, other surfaces and anisotropies are not covered.
- The straight line `u = 1/2` is a property of the cell cut. A 2 × 2
  transfer-matrix argument for it is not part of this block.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at `J = (1,1,1)`, `κ = 0.3, 0.6`; slabs of 40 layers.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs, the `u = +1` sector and the slab terminations remain supplied.
- **N4:** the landed families and chirality convention are used as stated there.
- **N5:** floating-point finite-slab diagnostics.
- **N6:** exact or certified arcs, endpoints and other couplings remain open.
- **N7:** other surfaces, terminations and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_slab_surface_zero_mode_arcs_2026_10_01.py
```

Ten checks; prints `TOTAL: PASS=10 FAIL=0` in about ninety seconds.

The contour connectivity, endpoint assignments and wrap classification use finite grid thresholds and nearest-node distances. They are diagnostics of the recorded arrays, not an all-slice Chern theorem or an exact arc endpoint/connectivity certificate.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) sets the premise boundary. The supplied comparator is not a framework-law or physical-species selection. Original source and execution history remain recoverable at [PR #9420](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9420); this is provenance, not audit authority.

Network definition: [current supplied network](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
