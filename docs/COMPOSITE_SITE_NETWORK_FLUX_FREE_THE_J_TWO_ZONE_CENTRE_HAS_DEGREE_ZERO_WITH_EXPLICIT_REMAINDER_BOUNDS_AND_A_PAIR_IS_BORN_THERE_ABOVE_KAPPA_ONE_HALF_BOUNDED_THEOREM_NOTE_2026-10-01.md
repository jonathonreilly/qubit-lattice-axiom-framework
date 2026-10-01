---
claim_id: composite_site_network_flux_free_the_j_two_zone_centre_has_degree_zero_with_explicit_remainder_bounds_and_a_pair_is_born_there_above_kappa_one_half_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), at J_x = J_y = 1, J_z = 2 (the boundary J_z = J_x + J_y), odd term kappa > 0; theta = 2 pi f = x(1,-1,0) + y(1,1,0) + z(0,0,1). Exact rational arithmetic: H(0) has spectrum {0, 0, +-8}; with C the 2x2 block on the complement of ker H(0), detC = det C and Num = detC (A - B C^-1 B^dag) = Pauli components (N_x, N_y, N_z, N_0) as Laurent polynomials in e^{ix}, e^{iy}, e^{iz} over Q(i)[kappa], det(Num) = detC det H; N_x, N_z, N_0 are odd and N_y, detC, det H even under theta -> -theta. With weights x: 1, (y, z): 2 and kappa != 1/2, Num = -64 d_lead + G with d_lead = (2(y - z), (1 - 4 kappa^2) x^2/2, -8 kappa y), G of weight >= 4, N_0 of weight >= 5, and det H = 64 |d_lead|^2 + R with R of weight >= 6; at kappa = 1/2 with weights (1; 4, 4), d_lead = (2(y - z), x^4/8, -4y), G of weight >= 6, N_0 >= 9, R >= 10. Exact Taylor polynomials of total degree <= 12 plus the Lagrange remainder bound give explicit quasi-balls (N^4 = x^4 + y^2 + z^2, resp. N^8 = x^8 + y^2 + z^2) on which detC < 0, the homotopy -64 d_lead + t G (0 <= t <= 1) has no zero except Gamma, N_0 < |N| (det H > 0, two negative and two positive levels), and |R| < 64 |d_lead|^2: at kappa = 1/4, 1, 2 (radii 0.37, 0.38, 0.26), uniformly on kappa in [1/10, 2/5] (0.23) and [3/5, 3] (0.062), and at kappa = 1/2 (0.2). On every quasi-sphere inside these balls Gamma is an isolated zero and the normalised Pauli map D = N/detC has degree 0 (d_lead omits a point of the sphere since d_y has a fixed sign); independently, the exact parity D(-theta) = (-D_x, D_y, -D_z)(theta) gives degree 0 on every zero-free inversion-symmetric sphere about Gamma, for every kappa. On the axis theta = x(1,-1,0), exactly N_x = N_z = N_0 = 0, detC = -4(cos x + 3)^2, D_y = 4(cos x - 1)(2 kappa^2 (cos x + 1) - 1)/(cos x + 3); for kappa > 1/2 a pair of touchings sits at cos x0 = 1/(2 kappa^2) - 1, i.e. tan(x0/2) = sqrt(4 kappa^2 - 1), where Num vanishes and ker H is two-dimensional; the Pauli map's Jacobian determinant there is 256 kappa (4 kappa^2 - 1)^(3/2) (1 - 2 kappa^2)/(4 kappa^2 + 1)^2 at +x0 and its negative at -x0, so the pair has degrees +1 and -1 at +x0 and -x0 for 1/2 < kappa < 1/sqrt 2 and the opposite beyond; x0 = 4 sqrt(kappa - 1/2) - (10/3)(kappa - 1/2)^(3/2) + O((kappa - 1/2)^(5/2)). Floating-point checks: Laurent objects against a direct Schur complement; solid-angle degrees on the proved spheres; the triple-product sign at the pair agrees with the Jacobian sign at five kappa. Not covered: a statement for a sphere enclosing Gamma and the pair together, completeness of the touching set, other couplings, the band Chern number beyond the Pauli-map degree, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_j_two_zone_centre_degree_zero_with_remainder_bounds_and_the_pair_born_there_2026_10_01.py
---

# The J = 2 zone centre has degree zero with explicit remainder bounds, and a pair is born there above κ = 1/2

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact rational algebra with explicit Taylor–Lagrange remainder bounds, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
taken at `J_x = J_y = 1`, `J_z = 2`. This is the boundary `J_z = J_x + J_y` of the
coupling triangle. The zone centre Γ is a touching for every `κ`.

The coordinates are `θ = 2πf = x(1,−1,0) + y(1,1,0) + z(0,0,1)`.

## Exact structure

1. `H(0)` has spectrum `{0, 0, ±8}`.
2. Let `C` be the 2×2 block on the complement of `ker H(0)`. Set
   `Num = det C · (A − B C⁻¹ B†)`, the Schur complement at `E = 0` times `det C`.
   - `Num` has Pauli components `(N_x, N_y, N_z, N_0)`.
   - These are exact Laurent polynomials over `Q(i)[κ]`.
   - `det(Num) = det C · det H`.
3. Under `θ → −θ`, `N_x`, `N_z` and `N_0` are odd, while `N_y`, `det C` and `det H`
   are even.
4. **Generic `κ ≠ 1/2`** (weights `x: 1`, `(y, z): 2`):
   - `Num = −64 d_lead + G`, with `d_lead = (2(y − z), (1 − 4κ²)x²/2, −8κy)` and `G` of weight `≥ 4`;
   - `N_0` has weight `≥ 5`;
   - `det H = 64|d_lead|² + R`, with `R` of weight `≥ 6`.
5. **`κ = 1/2`** (weights `(1; 4, 4)`):
   - `d_lead = (2(y − z), x⁴/8, −4y)`;
   - `G` has weight `≥ 6`, `N_0` has weight `≥ 9`, and `R` has weight `≥ 10`.

## Explicit neighbourhoods

The quasi-norm is `N⁴ = x⁴ + y² + z²` for generic `κ`, and `N⁸ = x⁸ + y² + z²` at
`κ = 1/2`. Each function is a finite Fourier sum. The runner bounds it by its
exact Taylor polynomial of total degree 12, plus the Lagrange remainder
`|e^{iφ} − T₁₂(φ)| ≤ |φ|¹³/13!` summed over modes. This gives explicit balls `N ≤ ρ`
on which:
- (A) `det C < 0`;
- (B) the homotopy `−64 d_lead + tG` with `0 ≤ t ≤ 1` vanishes at Γ and nowhere else;
- (C) `N_0 < |N|`, so `det H > 0` with two negative and two positive levels;
- (D) `|R| < 64|d_lead|²`.

The radii are:

| `κ` | radius |
|---|---|
| `1/4` | 0.37 |
| `1` | 0.38 |
| `2` | 0.26 |
| uniformly on `[1/10, 2/5]` | 0.23 |
| uniformly on `[3/5, 3]` | 0.062 |
| `1/2` | 0.2 |

## Degree zero

- **Leading-map argument.** On every quasi-sphere inside these balls, Γ is an
  isolated zero. `d_y` of `d_lead` has a fixed sign, so `d_lead` omits a point of
  the sphere and has degree 0. The homotopy (B) carries this to the full
  normalised Pauli map `D = N/det C`.
- **Parity argument.** This holds for every `κ` and needs no remainder bound.
  The exact parity `D(−θ) = (−D_x, D_y, −D_z)(θ)` is a rotation (determinant +1)
  composed with the antipodal map (degree −1). So the degree is 0 on every
  zero-free inversion-symmetric sphere about Γ.

## The pair born at Γ

On the axis `θ = x(1, −1, 0)` the following hold exactly:
- `N_x = N_z = N_0 = 0` and `det C = −4(cos x + 3)²`;
- `D_y = 4(cos x − 1)(2κ²(cos x + 1) − 1)/(cos x + 3)`.

For `κ > 1/2` this gives a pair of touchings at `cos x₀ = 1/(2κ²) − 1`, that is,
`tan(x₀/2) = √(4κ² − 1)`. There `Num = 0` and `ker H` is two-dimensional.

The exact Jacobian determinant of the Pauli map at `+x₀` is
`256κ(4κ² − 1)^{3/2}(1 − 2κ²)/(4κ² + 1)²`. At `−x₀` it is the negative.
- For `1/2 < κ < 1/√2`, the degrees are `+1` at `+x₀` and `−1` at `−x₀`.
- Beyond `1/√2`, they are opposite.

As `κ → 1/2⁺`, `x₀ = 4√(κ − 1/2) − (10/3)(κ − 1/2)^{3/2} + …`.

This axis is the line `(x, 1 − x, 0)` of the landed families. The sign change at
`κ = 1/√2` agrees with the isotropic flip coupling `κ_c² = J(J+2)/(4(4+2J−J²)) = 1/2`
at `J = 2`.

## Floating-point consistency

- The exact Laurent objects agree with a direct numerical Schur complement at
  800 random points.
- Solid-angle degrees on the proved spheres are 0.
- At the pair, the sign of the kernel-projector triple product agrees with the
  Jacobian sign at five `κ`.

## What this settles and what it does not

- **Settled.** At `J = 2`:
  - Γ is an isolated touching whose Pauli map has degree 0, with explicit
    neighbourhoods at the stated `κ`, and degree 0 by parity for every `κ`;
  - the pair born at Γ for `κ > 1/2` is exact, with its degrees and their
    exchange at `κ = 1/√2`.
- **Not settled here.**
  - A statement for a sphere enclosing Γ and the pair together (the proved
    balls lie inside the pair).
  - Completeness of the touching set.
  - Other couplings.
  - The band Chern number beyond the Pauli-map degree.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at `J = (1, 1, 2)`.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator is used as stated there.
- **N5:** exact algebra and explicit remainder bounds; floating-point checks are labelled.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_j_two_zone_centre_degree_zero_with_remainder_bounds_and_the_pair_born_there_2026_10_01.py
```

Thirty checks; prints `TOTAL: PASS=30 FAIL=0` in a few seconds.
