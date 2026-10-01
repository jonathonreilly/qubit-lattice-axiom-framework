---
claim_id: composite_site_network_flux_free_the_cubic_flip_points_have_explicit_degree_one_neighbourhoods_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), J_x = J_y = 1, J_z = J, at the line-family node where the charge flips: (i) J = 1, kappa^2 = 3/20, e^{i x0} = (-2 + i sqrt 5)/3; (ii) J = 5/2, kappa^2 = 45/44, e^{i x0} = (7 + 5i sqrt 11)/18; theta = (x0 + x)(1, -1, 0) + y(1, 1, 0) + z(0, 0, 1). Exact arithmetic in K = Q(i, sqrt p, sqrt q) ((3, 5) resp. (5, 11)) with the node as expansion point; magnitudes bounded by outward-rounded rational square roots; inequalities as exact rational comparisons. With x' = x + m z^2 and weights (3, 3, 1), the E = 0 Schur numerator is Num = N_lead + G with N_lead = n_x x' + n_y y + n_b z^3, n_x, n_y, n_b mutually orthogonal (Gram entries equal the landed closed forms), G of weight >= 4, N_0 of weight >= 5, and the weight-6 part of det H equals the leading form (independent 4x4 determinant route). On the ball N^6 = x'^2 + y^2 + z^6 <= rho^6 with rho = 29/500 (i), 69/1000 (ii): detC < 0, |N_lead + tG| >= (s - K_G rho) N^3 > 0 for t in [0, 1] (s = 0.1750, K_G rho = 0.169 (i); s = 5.444, K_G rho = 5.42 (ii)), and N_0 < |N|; hence the node is the unique zero of Num in the ball, det H > 0 with signature (2, 2) elsewhere in it, and the Pauli map has degree +1 at +x0 and -1 at -x0 on every weighted sphere inside. Unfolding kappa = kappa_node + eps: the weight-3 normal form is n_x X + n_y Y + n_b (z^3 - mu eps z), mu = (J + 2)/kappa^3 > 0; for 0 < |eps| <= eps0 (eps0 = 1/62500 (i), 1/2250000 (ii)) the Pauli map has exactly one zero in a shifted box for eps < 0 and exactly three for eps > 0, with indices (+1) and (-1, +1, +1) at +x0 (reversed at -x0). The radii and ranges are explicit and not optimal; the inequalities fail at slightly larger radii and ranges (checked). Floating point: the Pauli-map zeros coincide with the landed exact line and plane families (so they are touchings), solid-angle degrees are +-1, and the triple product has the matching sign. Not covered: optimal radii, other couplings, anisotropic flips, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_cubic_flip_points_have_explicit_degree_one_neighbourhoods_2026_10_01.py
---

# The cubic flip points have explicit degree-one neighbourhoods

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact arithmetic in a multiquadratic field with explicit remainder bounds, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
at `J_x = J_y = 1`, `J_z = J`. The two flip points are the line-family nodes
where the charge changes:

| Case | `J` | `κ²` | `e^{ix₀}` | Regime |
|---|---|---|---|---|
| (i) | 1 | `3/20` | `(−2 + i√5)/3` | triangle |
| (ii) | `5/2` | `45/44` | `(7 + 5i√11)/18` | `J_z > J_x + J_y` |

Coordinates: `θ = (x₀ + x)(1, −1, 0) + y(1, 1, 0) + z(0, 0, 1)`.

All arithmetic is exact in `K = Q(i, √p, √q)`, with `(p, q) = (3, 5)` for (i) and
`(5, 11)` for (ii), and the node itself as the expansion point. Magnitudes are
bounded with outward-rounded rational square roots. Every inequality is an exact
rational comparison.

## Local form

Set `x′ = x + m z²` and use weights `(3, 3, 1)`.
- The `E = 0` Schur numerator is `Num = N_lead + G`, with
  `N_lead = n_x x′ + n_y y + n_b z³`.
- `n_x`, `n_y` and `n_b` are mutually orthogonal. Their Gram entries equal the landed
  closed forms.
- `G` has weight `≥ 4` and `N₀` has weight `≥ 5`.
- An independent 4×4 determinant computation gives the weight-6 part of `det H`
  as the leading form.

## Explicit neighbourhoods

The balls are `N⁶ = x′² + y² + z⁶ ≤ ρ⁶`.

| Case | `ρ` | `s` | `K_G ρ` |
|---|---|---|---|
| (i) | `29/500` | `0.1750` | `0.169` |
| (ii) | `69/1000` | `5.444` | `5.42` |

On each ball:
- `det C < 0`;
- `|N_lead + tG| ≥ (s − K_G ρ) N³ > 0` for `t ∈ [0, 1]`;
- `N₀ < |N|`.

So, inside the ball:
- the node is the unique zero of `Num`;
- `det H > 0` with signature `(2, 2)` everywhere else;
- the Pauli map has degree `+1` at `+x₀` and `−1` at `−x₀` on every weighted sphere.

The same inequalities fail at `ρ = 3/50` (i) and `7/100` (ii). So the radii are
explicit but nearly tight for this method, and not optimal.

## Unfolding in κ

Let `κ = κ_node + ε`.
- The weight-3 normal form is `n_x X + n_y Y + n_b(z³ − μεz)`, with `μ = (J + 2)/κ³ > 0`.
- For `0 < |ε| ≤ ε₀`, the Pauli map has exactly one zero in a shifted box for
  `ε < 0`, and exactly three for `ε > 0`.
  - The range is `ε₀ = 1/62500` for (i) and `1/2250000` for (ii).
  - The indices at `+x₀` are `(+1)`, and `(−1, +1, +1)` respectively. They are
    reversed at `−x₀`.
- The conditions fail at larger ranges, as checked.

## Floating-point consistency

- The Laurent objects agree with a direct Schur complement.
- The Pauli-map zeros coincide with the landed exact line and plane families,
  to `4·10⁻⁸`. So they are band touchings.
- Solid-angle degrees are `±1`.
- The triple product has the matching sign along the axis.

## What this settles and what it does not

- **Settled.** At both flip points (triangle regime and `J_z > J_x + J_y`):
  - the cubic node has an explicit neighbourhood with degree `±1`;
  - the one-to-three splitting holds for an explicit κ-range on each side.
- **Not settled here.**
  - Optimal radii.
  - Other couplings and anisotropic flips.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at two flip points.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator, families and charge convention are used as stated there.
- **N5:** exact field arithmetic and explicit remainder bounds; floating-point checks are labelled.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_cubic_flip_points_have_explicit_degree_one_neighbourhoods_2026_10_01.py
```

Nineteen checks; prints `TOTAL: PASS=19 FAIL=0` in about 20 seconds.
