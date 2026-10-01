---
claim_id: composite_site_network_flux_free_the_cell_cut_slab_has_an_exact_surface_zero_line_at_f1_one_half_for_equal_in_plane_couplings_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, Bloch matrix H(f) = i M(f), on the half-infinite slab open along the primitive translation a3 with the cell cut (layers 0, 1, 2, ..., top surface at layer 0), periodic along a1, a2 with momenta (f1, f2) = (u, v). Exact, symbolic in (J_x, J_y, J_z, kappa): the layer blocks A (intra) and B (to the next layer) have B nonzero at three entries independent of J_x, J_y, and at f1 = 1/2 the 2x2 block of A on sites {0,1} is -2(J_x - J_y) sigma_y. For J_x = J_y, kappa != 0, J_z != 0 and every v in [0, 1): the zero-energy l^2 kernel of the half-infinite slab at (1/2, v) is exactly one-dimensional, spanned by psi_L = lambda^L (1, r, 0, 0) with lambda = rho e^{i pi (v - 1/2)}, r = -J_z rho/(2 kappa (sigma - rho)) real, sigma = sin pi v, rho = (|tau| - sqrt(tau^2 - 4))/2, |tau| = sigma + (4 kappa^2 + J_z^2)/(4 kappa^2 sigma), since tau^2 - 4 = (sigma - b/sigma)^2 + 4 delta > 0 (delta = J_z^2/(4 kappa^2), b = 1 + delta) puts exactly one eigenvalue of the 2x2 transfer matrix inside the unit disc and the boundary condition is empty; rho is largest at v = 1/2, rho_max = ((sqrt(J_z^2 + 16 kappa^2) - J_z)/(4 kappa))^2. The bottom surface carries the mirror statement on the line v = 1/2 (sites {2,3}). On the bulk plane f1 = 1/2 there is no zero energy, so the line lies in the projected gap. Floating-point cross-checks: rho(0.2) = 0.14557417 (kappa 0.3) and 0.31711487 (kappa 0.6) match finite-slab decay and |eig T|, the finite-N splitting decays as rho^{2N}, and for J_x != J_y the zero crossing moves off u = 1/2. Not covered: other cuts and open directions, the arcs, J_x != J_y exactly, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_exact_surface_zero_line_of_the_cell_cut_slab_2026_10_01.py
---

# The cell-cut slab has an exact surface zero line at f₁ = 1/2 for equal in-plane couplings

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra for a supplied comparator's slab; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
on a half-infinite slab:
- open along the primitive translation `a₃`, stacking copies of the four-site
  cell with the cell cut;
- layers `0, 1, 2, …`, with the top surface at layer 0;
- periodic along `a₁`, `a₂`, with momenta `(f₁, f₂) = (u, v)`.

Write `z₁ = e^{2πiu}`, `z₂ = e^{2πiv}` and `σ = sin πv`. Sites `{0, 1}` are
called p and sites `{2, 3}` are called q.

## Result

All statements are exact and symbolic in `(J_x, J_y, J_z, κ)` unless marked.

1. **Layer blocks.** The block `B` to the next layer has exactly three
   nonzero entries, none involving `J_x` or `J_y`:
   - `B[2,0] = −2iκ(z₂−1)/z₂`;
   - `B[3,0] = −2iJ_z`;
   - `B[3,1] = 2iκ(z₁−1)/z₁`.

   In the intra-layer block, `A[3,0] = 0`, and at `f₁ = 1/2` the p-block of
   `A` equals `−2(J_x − J_y)σ_y`. That block vanishes exactly when
   `J_x = J_y`.
2. **Transfer matrix.** For `J_x = J_y`, a p-supported vector is a zero mode
   of the half-infinite slab iff `x_{L+1} = T x_L` for all `L ≥ 0`. Here
   `T = −B_s⁻¹A_s`, with `det T = −z₂`, and the boundary condition is empty.
3. **Top theorem.** Take `J_x = J_y`, `κ ≠ 0`, `J_z ≠ 0`, and any
   `v ∈ [0, 1)`.
   - The zero-energy ℓ² kernel at `(1/2, v)` is exactly one-dimensional.
   - It is spanned by `ψ_L = λ^L (1, r, 0, 0)`, with
     `λ = ρ e^{iπ(v − 1/2)}` and `r = −J_zρ/(2κ(σ − ρ))`, which is real.
   - The decay rate is `ρ = (|τ| − √(τ² − 4))/2`, with
     `|τ| = σ + (4κ² + J_z²)/(4κ²σ)`.

   The key inequality is `τ² − 4 = (σ − b/σ)² + 4δ > 0`, with
   `δ = J_z²/(4κ²)` and `b = 1 + δ`. It puts exactly one eigenvalue of `T`
   inside the unit disc. The q-part vanishes by `det A_pq ≠ 0`, and at
   `v = 0` by a separate 2 × 2 argument. The rate is largest at `v = 1/2`,
   where `ρ_max = ((√(J_z² + 16κ²) − J_z)/(4κ))²`.
4. **Bottom theorem.** The bottom surface carries the mirror statement on
   the line `v = 1/2`, on sites `{2, 3}`. Its transfer matrix has the
   reciprocal eigenvalues, with `v` replaced by `u`.
5. **Projected gap.** On the bulk plane `f₁ = 1/2`,
   `det H = |det(A_qp + λB_qp)|²` has no zero, since `|τ| > 2`. So the
   line lies in the projected bulk gap.
6. **Floating-point cross-checks.**
   - The exact `ρ(0.2)` is `0.14557417` at `κ = 0.3` and `0.31711487` at
     `κ = 0.6`. It matches the float `|eig T|` and the layer ratio of a
     40-layer slab, where the exact mode leaves `|Hψ| ≤ 2e-15`.
   - In 50-digit finite slabs the top–bottom splitting decays as `ρ^{2N}`.
   - For `J_x ≠ J_y`, for example `J = (1, 0.8, 1)`, the zero crossing moves
     off `u = 1/2` (`u* = 0.5035, 0.5055, 0.4945` at `v = 0.1, 0.25, 0.75`).
     This is a negative control, reported and not asserted.

## What this settles and what it does not

- **Settled.** For equal in-plane couplings, the cell-cut `a₃` surface hosts
  an exact straight zero line, one-dimensional and with an explicit decay
  rate, inside the projected bulk gap. The bottom surface hosts the mirror
  line. This makes exact the straight lines seen in the floating-point slab
  study of the same surfaces.
- **Not settled here.**
  - Other cuts and open directions.
  - The arcs between projected touchings.
  - An exact statement for `J_x ≠ J_y`.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator on the cell-cut `a₃` half-infinite slab, `J_x = J_y`.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs, the `u = +1` sector and the termination remain supplied.
- **N4:** the landed comparator's Bloch matrix is used as stated there.
- **N5:** exact algebra; float and 50-digit cross-checks.
- **N6:** other terminations and `J_x ≠ J_y` remain open.
- **N7:** other surfaces and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_exact_surface_zero_line_of_the_cell_cut_slab_2026_10_01.py
```

Ten checks; prints `TOTAL: PASS=10 FAIL=0` in a few seconds.
