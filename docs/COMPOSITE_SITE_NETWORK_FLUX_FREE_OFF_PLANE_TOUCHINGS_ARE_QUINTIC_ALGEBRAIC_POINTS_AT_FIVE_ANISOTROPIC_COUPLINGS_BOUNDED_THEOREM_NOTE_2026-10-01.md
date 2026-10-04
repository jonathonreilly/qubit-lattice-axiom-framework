---
claim_id: composite_site_network_flux_free_off_plane_touchings_are_quintic_algebraic_points_at_five_anisotropic_couplings_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f) with z_j = exp(2 pi i f_j). (1) For positive J_x, J_y, J_z, kappa, with polynomial identities symbolic in those parameters: M + M(1/z)^T = 0; det(mu - M) = mu^4 + a2 mu^2 + D (so D >= 0 on the torus); in the site ordering (0,1 | 2,3), H = [[h_x, iW],[-iW^dag, h_y]] with h_x = d(theta_1).sigma, h_y = d(theta_2).sigma, d(theta) = (b sin theta, -a - b cos theta, -2k sin theta), (a, b, c, k) = 2(J_x, J_y, J_z, kappa), W = [[w, c v],[-c, v conj w]], w = k(conj z_1 - 1) + k(1 - z_2) v, v = 1/z_3; W W^dag = lambda^2 1 with lambda^2 = |w|^2 + c^2; det M = lambda^4 + |d_x|^2 |d_y|^2 - 2 d_y.e with e the Pauli vector of W^dag h_x W and |e| = lambda^2 |d_x|; |d_x|^2 det M = s_1^2 + s_2^2 + s_3^2 with s = |d_x|^2 d_y - e; |d_x|^2 >= (2J_x - 2J_y)^2. For J_x != J_y the zeros of D are the common zeros of the three real trigonometric polynomials s_i. (2) At (J_x, J_y, J_z; kappa) = (6/5, 4/5, 1; 3/10), (1, 4/5, 1; 9/20), (1, 4/5, 1; 4/5), (2, 1, 5/2; 9/10), (3/2, 1/2, 4/5; 3/2): an integer quintic Q5, irreducible over Q with one root alpha_0 in [-1, 1], and rational polynomials of degree 4 in alpha_0 for c_1 + c_2, c_1 c_2, s_1 s_2 and s_3 (s_1 + s_2) (c_j = cos 2 pi f_j, s_j = sin 2 pi f_j, c_3 = alpha_0) define points of the torus at which, exactly in Q[alpha, t, d, i]/(Q5, t^2 - (1 - alpha^2), d^2 - (sigma^2 - 4 pi), i^2 + 1), every 3x3 minor of M vanishes, det M = tr M = 0 and the mu^2 coefficient a2 is a nonzero element; the identities hold for each of the four sign choices of (t, d). (3) For one of these points at each coupling, outward-rounded interval arithmetic (mpmath.iv, 300 bits) with exact rational LDL shows: 1 - alpha_0^2 > 0 and sigma^2 - 4 pi > 0; on the box |theta_j - theta0_j| <= 10^-6 about an 8-digit centre the Hessian of D is positive definite (D strictly convex), a2 > 0, and the algebraic point lies in the box; hence it is the unique zero of D in the box and a touching of the two middle bands at E = 0 (levels -l1, 0, 0, l1). So cos 2 pi f_3 at that touching is algebraic of degree exactly 5; at the first coupling c_1 and c_2 are roots of an irreducible degree-10 integer polynomial (exact resultant), and at the second the exact degree-10 polynomial equals an earlier independently found one up to scale. The coefficients were found by integer-relation search and are proved by the exact checks. Not covered: completeness of the touching set at these couplings, a closed form in the couplings, other couplings, the touchings' charges, spin-model equivalence, physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_off_plane_touchings_are_quintic_algebraic_points_at_five_anisotropic_couplings_2026_10_01.py
---

# Off-plane touchings of the anisotropic comparator are quintic algebraic points

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra plus an outward-rounded interval box certificate, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
with general couplings `(J_x, J_y, J_z)` and odd term `κ`. The runner tabulates
that note's network terms. Throughout, `z_j = e^{2πi f_j}`,
`c_j = cos 2πf_j` and `s_j = sin 2πf_j`.

When `J_x ≠ J_y`, numerical searches find middle-band touchings off the
coordinate planes. Their coordinates had not been identified exactly. This
note identifies them at five couplings.

## (1) Structure for positive couplings, with symbolic identities

1. `M` is anti-Hermitian on the torus.
2. `det(μ − M) = μ⁴ + a₂μ² + D`. So the spectrum of `H` is `{±l₁, ±l₂}` with
   `D = l₁²l₂² ≥ 0`.
3. Take the site ordering `(0, 1 | 2, 3)` and set `(a, b, c, k) = 2(J_x, J_y, J_z, κ)`.
   Then `H = [[h_x, iW], [−iW†, h_y]]`, where:
   - `h_x = d(θ₁)·σ` and `h_y = d(θ₂)·σ`;
   - `d(θ) = (b sin θ, −a − b cos θ, −2k sin θ)`;
   - `W = [[w, cv], [−c, v w̄]]`, with `w = k(z̄₁ − 1) + k(1 − z₂)v` and `v = 1/z₃`.
4. `W W† = λ²·1`, with `λ² = |w|² + c²`.
5. `det M = λ⁴ + |d_x|²|d_y|² − 2 d_y·e`. Here `e` is the Pauli vector of
   `W† h_x W`, with `|e| = λ²|d_x|`.
6. `|d_x|² det M = s₁² + s₂² + s₃²`, with `s = |d_x|² d_y − e`.
7. `|d_x|² = (2J_x − 2J_y)² + 2ab(1 + cos θ₁) + 4k² sin²θ₁ ≥ (2J_x − 2J_y)²`.

So for `J_x ≠ J_y` the touchings are exactly the common zeros of three real
trigonometric polynomials. Equivalently, `λ² = |d_x||d_y|` and the rotation
by `W` carries `d̂_x` to `d̂_y`.

## (2) Exact zeros at five couplings

The five couplings `(J_x, J_y, J_z; κ)` are:

| Label | Coupling |
|---|---|
| B | `(6/5, 4/5, 1; 3/10)` |
| A | `(1, 4/5, 1; 9/20)` |
| C | `(1, 4/5, 1; 4/5)` |
| F | `(2, 1, 5/2; 9/10)` |
| G | `(3/2, 1/2, 4/5; 3/2)` |

G lies in `J_z < |J_x − J_y|`.

The runner embeds the following for each coupling:
- an integer quintic `Q5`, irreducible over `Q`, with exactly one root `α₀` in `[−1, 1]`;
- rational polynomials of degree 4 in `α₀` for `σ = c₁ + c₂`, `π = c₁c₂`,
  `r₁₂ = s₁s₂` and `w = s₃(s₁ + s₂)`.

At B, `Q5 = 864x⁵ + 816x⁴ − 166396x³ + 837889x² + 205720x − 829767`.

The point is built as follows:
- `c₃ = α₀` and `s₃ = t`, with `t² = 1 − α₀²`;
- `c₁,₂ = (σ ± d)/2`, with `d² = σ² − 4π`;
- `s₁ + s₂ = w t/(1 − α₀²)` and `s₁ − s₂ = −σ d t/w`.

In the ring `Q[α, t, d, i]/(Q5, t² − (1 − α²), d² − (σ² − 4π), i² + 1)` the
runner checks exactly:
- the four defining relations;
- `c_j² + s_j² = 1` for `j = 1, 2, 3`;
- all sixteen 3×3 minors of `M`, with `det M = tr M = 0`;
- `a₂` is a nonzero element.

The identities hold for all four sign choices of `(t, d)`. Each choice gives
an exact zero of `D`.

The coefficients were found by an integer-relation search. The exact checks
are what establish them. Three negative controls at B each make all sixteen
minors nonzero: a constant shift of `σ` by `10⁻⁹`, a flipped sign of `s₂`, and
`Q5`'s constant term plus 1.

## (3) One certified isolated touching per coupling

For one sign choice per coupling, outward-rounded interval arithmetic (300
bits) with exact rational `LDLᵀ` shows the following:
- `1 − α₀² > 0` and `σ² − 4π > 0`, so the point is real.
- On the box `|θ_j − θ0_j| ≤ 10⁻⁶` about an 8-digit centre, the Hessian of `D`
  is positive definite. The smallest pivot ranges from 8.86 (A) to 551 (G).
- `a₂` is bounded below on the box: at least 21.0 (B), 34.8 (A), 52.3 (C),
  125 (F) and 90.8 (G).
- The algebraic point lies in the box, between `8.2·10⁻⁹` (B) and
  `4.2·10⁻⁸` (G) from the centre.

Since `D ≥ 0`, and since it is strictly convex on the box, it has at most one
zero there. That zero is the algebraic point. Its levels are `−l₁, 0, 0, l₁`
with `l₁ > 0`: a touching of the two middle bands at `E = 0`.

Approximate values are below. The `f` values are midpoints of their enclosures.

| Coupling | `α₀ = cos 2πf₃` | `f` |
|---|---|---|
| B | 0.964327310302 | (0.255056929267, 0.589947050396, 0.0426385691717) |
| A | −0.00151009728722 | (0.222999042437, 0.686437050565, 0.250240339539) |
| C | −0.538415727922 | (0.0352628499302, 0.68747587819, 0.340488487697) |
| F | 0.761130116069 | (0.211021781856, 0.7012748566, 0.112322422314) |
| G | 0.00790675591878 | (0.0558665224745, 0.36728320423, 0.751258412401) |

So `cos 2πf₃` at the touching is algebraic of degree exactly 5.

At B, `c₁` and `c₂` are roots of `N10 = Res_α(Q5, x² − σx + π)`. This
polynomial is irreducible of degree 10, with an exact ring check. At A, the
exact `N10` equals, up to scale, a degree-10 polynomial found earlier by an
independent integer-relation search on `cos 2πf₁`.

## What this settles and what it does not

- **Settled.**
  - For `J_x ≠ J_y`, the touchings are the common zeros of three explicit real
    trigonometric polynomials.
  - At five couplings, the numerically located off-plane touchings are exact
    algebraic points, with `cos 2πf₃` of degree 5.
- **Not settled here.**
  - Completeness of the touching set at these couplings.
  - A closed form in the couplings.
  - Other couplings.
  - The touchings' charges.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator; five rational couplings, plus the symbolic structure identities.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator is used as stated there.
- **N5:** exact algebra, plus an outward-rounded interval box certificate.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_off_plane_touchings_are_quintic_algebraic_points_at_five_anisotropic_couplings_2026_10_01.py
```

Fourteen checks; prints `TOTAL: PASS=14 FAIL=0` in a few seconds.

## Current source references

- [COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26](COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
