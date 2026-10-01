---
claim_id: composite_site_network_flux_free_line_nodes_outside_the_coupling_triangle_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), general couplings J_x, J_y, J_z, kappa > 0; s = J_x + J_y, P = J_x J_y, S = J_x^2 + J_y^2 - J_z^2, u = kappa^2, c = cos 2 pi x on the line f = (x, 1-x, 0). Exact (symbolic): on the line det H = 16 q(c)^2 with q = 4u c^2 - 2Pc - S - 4u; at a root of q the kernel is two-dimensional with levels 0, 0, +-4 J_z, the triple product is T = -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/J_z^3 with F_c(c) = P(s + J_z)c^2 + s(s^2 + J_z s - 2P)c + (J_x + J_z)(J_y + J_z)(s - J_z), and det Hess_theta(det H) = 2^17 kappa^2 q'^2 F_c^2 (1 - c^2), so a simple root with F_c != 0 is an isolated touching of charge -sign(q' F_c) (x < 1/2). (a) J_z < |J_x - J_y|: q = -4u(1 - c^2) - 2P(1 + c) + J_z^2 - (J_x - J_y)^2 < 0 on (-1, 1), no line touching for any kappa; J_z = |J_x - J_y|: q = -2(1 + c)(2u(1 - c) + P), the line's zero is the zone corner (1/2, 1/2, 0) for every kappa. (b) J_z > J_x + J_y: q = -4(1 - c^2)(u - u(c)) with u(c) U-shaped on (-1, 1); line touchings exist iff u >= u_* = (-S + sqrt(S^2 - 4P^2))/8, a double root c_b = P/(4u_*) at u_* and two simple roots c_1 < c_b < c_2 above; F_c has a zero c_F in (0, 1) iff J_z < phi s (phi the golden ratio); Res_c(F_c, F_b) = -J_z^2 P (J_z + s) G with G a quintic in J_z, increasing for J_z >= s with a unique zero J_0 in (s, phi s), and F_c(c_b) > 0 iff J_z < J_0; the x < 1/2 pair is born with charges (+1, -1) on (c_1, c_2) for s < J_z < J_0 and (-1, +1) for J_z > J_0; for J_z < phi s one of the two flips to -1 at u = u_+, the larger root of the irreducible factor R2 of Res_c(q, F_c) (the same closed form as in the triangle regime), and for J_z >= phi s neither flips; isotropic G = J_z^2 (J_z^3 - 4 J_z - 4). (c) J_z = J_x + J_y: q = (c - 1)(4u(c + 1) - 2P); the zone centre is a zero for every kappa, a second root c_2 = P/(2u) - 1 enters (-1, 1) iff u > P/4, with charge +1 for P/4 < u < P/2 and -1 for u > P/2. Leading-order weighted Schur expansions (no remainder radius): the zone centre (J_z = s, including u = P/4) and the zone corner (J_z = |J_x - J_y|) are semi-Dirac with leading Pauli maps of Jacobian odd in x, local degree 0. Floating-point checks: root counts, triple products and Fukui fluxes at random couplings. Not covered: off-line touchings (the line charge changes imply they exist but are not analysed), the three-dimensional form of the line merger away from the zone points, remainder radii at the zone points, interval certification, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_line_nodes_outside_the_coupling_triangle_2026_10_01.py
---

# Line nodes outside the coupling triangle

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact symbolic algebra, with labelled floating-point checks, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
with general couplings `(J_x, J_y, J_z)` and odd term `κ`.

Notation: `s = J_x + J_y`, `P = J_xJ_y`, `S = J_x² + J_y² − J_z²` and `u = κ²`. On
the line `f = (x, 1 − x, 0)`, `c = cos 2πx`.

The coupling triangle `|J_x − J_y| < J_z < J_x + J_y` is where the line nodes were
previously analysed. This note treats all couplings outside it.

## Exact facts on the line, for every coupling

1. `det H = 16 q(c)²`, with `q = 4uc² − 2Pc − S − 4u`.
2. At a root of `q`:
   - the kernel is two-dimensional, with levels `0, 0, ±4J_z`;
   - the kernel-projector triple product is
     `T = −32π³κ q′(c) F_c(c) sin(2πx)/J_z³`;
   - `det Hess_θ(det H) = 2¹⁷κ² q′² F_c² (1 − c²)`.

   Here `F_c(c) = P(s + J_z)c² + s(s² + J_zs − 2P)c + (J_x + J_z)(J_y + J_z)(s − J_z)`.
3. So a simple root with `F_c ≠ 0` is an isolated touching. Its charge is
   `−sign(q′F_c)` for the node with `x < 1/2`. The partner at `(1 − x, x, 0)` has
   the opposite charge.

## (a) `J_z ≤ |J_x − J_y|`

- `q = −4u(1 − c²) − 2P(1 + c) + J_z² − (J_x − J_y)²` is negative on `(−1, 1)`. So
  there is no line touching for any `κ`.
- On the boundary `J_z = |J_x − J_y|`, `q = −2(1 + c)(2u(1 − c) + P)`. The line's
  zero is the zone corner `(1/2, 1/2, 0)`, for every `κ`.

## (b) `J_z > J_x + J_y`

1. **Existence.** `q = −4(1 − c²)(u − u(c))`, with `u(c)` U-shaped on `(−1, 1)`.
   - Line touchings exist iff `u ≥ u_* = (−S + √(S² − 4P²))/8`.
   - At `u_*` there is a double root, `c_b = P/(4u_*)`: a pair creation on the line.
   - Above `u_*` there are two simple roots, `c₁ < c_b < c₂`.
2. **Zeros of `F_c`.** `F_c` has a zero in `(0, 1)` iff `J_z < φs`, where `φ` is the
   golden ratio.
3. **Birth charges.**
   - Exactly, `Res_c(F_c, F_b) = −J_z²P(J_z + s)G`, where `F_b` is the polynomial
     whose root is `c_b`. `G` is a quintic in `J_z`. It is increasing for
     `J_z ≥ s`, with a unique zero `J₀` in `(s, φs)`.
   - `F_c(c_b) > 0` iff `J_z < J₀`.
   - The `x < 1/2` pair is born with charges `(+1, −1)` on `(c₁, c₂)` for
     `s < J_z < J₀`, and `(−1, +1)` for `J_z > J₀`.
4. **Flip.**
   - For `J_z < φs`, one node of the pair flips to `−1` at `u = u₊`. This is the
     larger root of the irreducible factor `R₂` of `Res_c(q, F_c)`, the same
     closed form as in the triangle regime.
   - For `J_z ≥ φs`, neither node flips.
5. **Isotropic case.** `G = J_z²(J_z³ − 4J_z − 4)`, so `J₀ ≈ 2.3830`.
6. **Exact samples.** At `J_x = J_y = 1` and `J_z = 13/6, 5/2, 29/10, 10/3`, the
   runner checks `u_*`, the birth charges and `u₊` exactly.

## (c) `J_z = J_x + J_y`

- `q = (c − 1)(4u(c + 1) − 2P)`. The zone centre is a zero for every `κ`.
- A second root, `c₂ = P/(2u) − 1`, enters `(−1, 1)` iff `u > P/4`.
- Its charge is `+1` for `P/4 < u < P/2` and `−1` for `u > P/2`.

## Zone points (leading order)

Weighted Schur expansions to leading order give semi-Dirac Pauli maps. Their
Jacobian is odd in `x`, so the local degree is 0. This applies to:
- the zone centre for `J_z = s`, including `u = P/4`, where the soft direction is quartic;
- the zone corner for `J_z = |J_x − J_y|`.

No remainder radius is computed here.

## Floating-point consistency

All of the following agree with the exact statements:
- root counts and triple products at random couplings, with the closed form for
  `T` holding to `3·10⁻¹³`;
- the birth and flip patterns across `J₀` and `u₊`;
- Fukui fluxes around the line merger and around the zone points.

## What this settles and what it does not

- **Settled.** Combined with the triangle-regime result, the line touchings are
  exact for all positive couplings: where they exist, where they are born, their
  charges, and where those flip.
- **Not settled here.**
  - Off-line touchings. The line charge changes imply they exist, but they are
    not analysed.
  - The three-dimensional form of the line merger away from the zone points.
  - Remainder radii at the zone points.
  - Interval certification.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator; all positive couplings outside the triangle.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator is used as stated there.
- **N5:** exact symbolic algebra and leading-order expansions; floating-point checks are labelled.
- **N6:** the items listed above remain open.
- **N7:** other sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_line_nodes_outside_the_coupling_triangle_2026_10_01.py
```

Twenty-two checks; prints `TOTAL: PASS=22 FAIL=0` in under a minute.
