---
claim_id: composite_site_network_flux_free_the_cell_cut_surface_arc_at_kappa_three_tenths_is_an_interval_certified_algebraic_curve_ending_at_the_line_node_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J_x = J_y = J_z = 1, kappa = 3/10, on the half-infinite slab open along a3 with the cell cut (top surface at layer 0), surface momenta (u, v). Exact (sympy): the layer blocks; the bulk characteristic quartic in lambda reduces, with lambda = e^{i pi (u+v)} mu, to a real quadratic in x = mu + 1/mu; eliminating the decaying solutions against the layer-0 condition gives the eliminant Y = c S_u^2 S_v^3 H G' (S = sin pi., C = cos pi.), with the irreducible integer form 625 G' = S_u a0 + C_u C_v S_v b0, a0 = 625 + 300Y + 27Y^2 - (750 + 108Y)X + 81X^2, b0 = 2500 - 300Y - (600 + 108Y)X - 540X^2 (X = S_u^2, Y = S_v^2); in trigonometric coordinates the condition s_u a0 + (1/2)(1 + c_u) s_v b0 = 2 C_u 625 G' contains the straight line u = 1/2 as the factor C_u; a root-counting quantity Xi has a closed form and equals F_tau(1)F_tau(-1) on G' = 0. On the antidiagonal u + v = 1, 625 G' = 625 S_u (1 - 2KX)(4KX^2 + 4(1-K)X - 3), K = 4 kappa^2, the second factor being the landed line-family polynomial; at the line node cos 2 pi u0 = (25 - 7 sqrt19)/9 the decaying root reaches |lambda| = 1 (n(-1) = g(-1) = 0, Xi = 0). Interval-certified (mpmath intervals, outward rounding): for u in [1e-5, 0.34] the set G' = 0 is the graph of a unique continuous v = f(u) with Xi > 0 and no bulk root on the unit circle (584 boxes); over [0.34, 0.37] the graph continues with dXi/du < 0 and contains the node; branch and bound over u in [0.001, 0.499], v in [0, 1] leaves no other point with G' = 0 and Xi >= 0. Floating point: the N = 40 finite-slab top contour equals the set of grid edges where G' changes sign with Xi > 0 and the direct 4 x 4 null-vector criterion (80 of 80 edges). With the argued (not machine-checked) step that G' = 0 and Xi > 0 give a top-surface zero mode, the top-surface arc at kappa = 3/10 is this curve and ends at the projection of the line node. Not covered: the root-pair step, the loci u = 0, v = 0, H = 0, the discriminant crossing at u = 0.305, the strips u < 1e-5 and (0.499, 0.501), the node neighbourhood beyond the certified graph, other kappa, J, terminations, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_exact_surface_arc_of_the_cell_cut_slab_at_kappa_three_tenths_2026_10_01.py
---

# The cell-cut surface arc at κ = 3/10 is an interval-certified algebraic curve ending at the line node

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra with an interval certificate and one argued step; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
at `J = (1, 1, 1)`, `κ = 3/10`. At this coupling there are two line
touchings, at `(u₀, 1 − u₀, 0)` and its mirror, with
`cos 2πu₀ = (25 − 7√19)/9`.

The slab is half-infinite: open along `a₃` with the cell cut, layers
`0, 1, 2, …` with the top surface at layer 0, and surface momenta `(u, v)`.
Floating-point slab studies of this surface show a zero-energy arc running
between the projections of the two touchings. This block describes that arc
exactly.

Write `S_u = sin πu`, `C_u = cos πu` (similarly for `v`), `X = S_u²`,
`Y = S_v²` and `K = 4κ² = 9/25`.

## Result

1. **Bulk roots.** The bulk recursion's characteristic quartic in `λ`
   becomes, with `λ = e^{iπ(u+v)} μ`, a real quadratic in `x = μ + 1/μ`.
   This is exact.
2. **Zero-mode condition.** Eliminating the decaying solutions against the
   layer-0 condition gives the eliminant
   `Y = c S_u² S_v³ H G′`, where `H` is a spurious common-root factor. The
   factor `G′` has the irreducible integer form
   `625 G′ = S_u a₀ + C_u C_v S_v b₀`, with
   - `a₀ = 625 + 300Y + 27Y² − (750 + 108Y)X + 81X²`;
   - `b₀ = 2500 − 300Y − (600 + 108Y)X − 540X²`.

   In trigonometric coordinates the condition carries the factor `C_u`,
   which gives the straight line `u = 1/2`. That line's exact statement is a
   separate surface-line block.
3. **Selecting the arc.** A root-counting quantity `Ξ` has a closed form,
   and on `G′ = 0` it equals `F_τ(1)F_τ(−1)`. `Ξ > 0` means the two decaying
   roots form a matching pair.
4. **Endpoint (exact).** On the antidiagonal `u + v = 1`:
   - `625 G′ = 625 S_u (1 − 2KX)(4KX² + 4(1 − K)X − 3)`, and the second
     factor is the landed line-family polynomial;
   - at the line node, `n(−1) = g(−1) = 0`, so a decaying root reaches
     `|λ| = 1`, and `Ξ = 0`.
5. **Interval certificate** (mpmath intervals, outward rounding):
   - **Corridor.** For `u ∈ [1e-5, 0.34]` the set `G′ = 0` is the graph of a
     unique continuous `v = f(u)`, with `Ξ > 0` and no bulk root on the unit
     circle. This uses 584 boxes; the smallest certified lower bound of `Ξ`
     is `0.114`.
   - **Node window.** Over `[0.34, 0.37]` the graph continues, `dΞ/du < 0`
     along it, and it contains the node.
   - **Exclusion.** A branch-and-bound over `u ∈ [0.001, 0.499]`,
     `v ∈ [0, 1]` leaves no other point with `G′ = 0` and `Ξ ≥ 0`
     (0 undecided boxes).
6. **Floating-point cross-check.** On an 80 × 80 grid, three edge sets are
   equal, all 80 of 80 edges:
   - the top-surface contour of a 40-layer slab;
   - the grid edges where `G′` changes sign with `Ξ > 0`;
   - the edges passing a direct 4 × 4 null-vector criterion.

## What follows

Take the argued step that `G′ = 0` with `Ξ > 0` gives a top-surface zero
mode: since `τ` and `−K/τ` give reciprocal pairs, exactly one of them gives
the decaying pair. Then the top-surface arc at `κ = 3/10` is the
interval-certified branch of the algebraic curve `G′ = 0`, and it ends at the
projection of the line touching.

## Boundary

- **Argued, not machine-checked.** The root-pair step is argued, and checked
  numerically on the grid.
- **Not certified.**
  - The loci `u = 0`, `v = 0` and `H = 0`.
  - The discriminant crossing at `u = 0.305`, which rests on continuity.
  - The strips `u < 1e-5` and `(0.499, 0.501)`.
  - The node neighbourhood beyond the certified graph.
  - The mirror half, which follows from the exact `(u, v) → (1 − u, 1 − v)`
    invariance.
- **Not covered.** Other `κ`, `J` and terminations; equality with the spin
  model; any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at `J = (1,1,1)`, `κ = 3/10`; the cell-cut `a₃` half-infinite slab.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs, the `u = +1` sector and the termination remain supplied.
- **N4:** the landed family and its node are used as stated there.
- **N5:** exact algebra, interval certificate, one argued step, float cross-check.
- **N6:** the listed loci, other couplings and terminations remain open.
- **N7:** other surfaces and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_exact_surface_arc_of_the_cell_cut_slab_at_kappa_three_tenths_2026_10_01.py
```

Ten checks; prints `TOTAL: PASS=10 FAIL=0` in about eighty seconds.
