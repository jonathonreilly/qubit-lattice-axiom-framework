---
claim_id: composite_site_network_flux_free_the_line_node_flip_coupling_is_an_exact_resultant_root_and_the_j_two_zone_centre_has_degree_zero_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f). (A) General couplings J_x, J_y, J_z, kappa > 0, s = J_x + J_y, P = J_x J_y, u = kappa^2: on the line (x, 1-x, 0), det H = 16 q(c)^2 with q(c) = 4u c^2 - 2P c + J_z^2 - J_x^2 - J_y^2 - 4u (checked symbolically), and the line node's charge is sign F_c(c_-) with the stated cubic-coefficient polynomial F_c; exactly, Res_c(q, F_c) = -(s + J_z) R2(u) with R2 = A2 u^2 + B2 u + C2 irreducible (A2 = 16(s^2 + J_z s - J_z^2)(J_z^3 - 4Ps + s^3), B2 = 4(s^2 - 2P - J_z^2)(2J_z^3 P - 4J_z P s^2 + J_z s^4 - 4P s^3 + s^5), C2 = P^2 (s + J_z)(s^4 - 4P s^2 - J_z^4)), disc_u R2 = 16 N1^2 Delta_F, and the closed form u_+ = (N0 + N1 sqrt(Delta_F))/Den is an exact root with shared root c_F^+ of q and F_c; with u(c) a strictly decreasing bijection, F_c(-1) < 0 < F_c(1), F_c(c0) = (s + J_z)(J_z^4 - (J_x^2 - J_y^2)^2)/(4P) and u_- < 0, in the triangle regime |J_x - J_y| < J_z < J_x + J_y the x < 1/2 line node's charge flips once, from +1 to -1, at kappa^2 = u_+ iff |J_x^2 - J_y^2| < J_z^2, and is -1 for all kappa otherwise; isotropic limit J(J+2)/(4(4+2J-J^2)). (B) J_x = J_y = 1, J_z = 2, the zone centre Gamma: a double zero for every kappa; the E = 0 Schur-complement Pauli vector in weights (x: 1; y, z: 2) is d = (2(y - z), (1 - 4kappa^2) x^2/2, -8 kappa y) through weight 4 and the weight-4 part of det H is 64 |d|^2 (at kappa = 1/2 the x^2 term vanishes and with weights (1; 4, 4) d = (2(y - z), x^4/8, -4y), det H weight 8 = 64 |d|^2); the leading map's Jacobian is odd in x, so Gamma is an isolated semi-Dirac touching of local degree 0 for every kappa > 0, with a pair of nodes born at Gamma for kappa > 1/2. Floating-point checks: the charge sign straddles kappa_c at six couplings; sphere and ellipsoid fluxes give 0 at Gamma and +-1 at the line nodes. Not covered: couplings outside the triangle regime, remainder bounds at Gamma, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_line_node_flip_coupling_exact_and_j_two_zone_centre_degree_zero_2026_10_01.py
---

# The line-node flip coupling is an exact resultant root, and the J = 2 zone centre has degree zero

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact symbolic algebra for a supplied comparator; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`.
Two exact completions are proved here.

## (A) The flip coupling for general couplings

On the line `(x, 1 − x, 0)` the runner checks symbolically that
`det H = 16 q(c)²`, with
`q(c) = 4u c² − 2P c + J_z² − J_x² − J_y² − 4u`. Here `s = J_x + J_y`,
`P = J_xJ_y` and `u = κ²`. The charge of the `x < 1/2` line node is the sign
of `F_c(c₋)`, where
`F_c(c) = P(s+J_z)c² + s(J_x²+J_y²+J_z s)c + (J_x+J_z)(J_y+J_z)(s−J_z)`.

1. **Resultant.** `Res_c(q, F_c) = −(s + J_z) R₂(u)`. Here `R₂` is quadratic
   in `u` and irreducible, with coefficients:
   - `A₂ = 16(s²+J_zs−J_z²)(J_z³−4Ps+s³)`;
   - `B₂ = 4(s²−2P−J_z²)(2J_z³P−4J_zPs²+J_zs⁴−4Ps³+s⁵)`;
   - `C₂ = P²(s+J_z)(s⁴−4Ps²−J_z⁴)`.
2. **Roots.** `disc_u R₂ = 16 N₁² Δ_F`. Both roots `u_± = (N₀ ± N₁√Δ_F)/Den`
   are exact roots of `R₂`. `u₊` and `q` share the root `c_F⁺` of `F_c`.
3. **Branch.** The following hold exactly:
   - `u(c) = −(2Pc + S)/(4(1 − c²))`, with `S = J_x² + J_y² − J_z²`, is a
     strictly decreasing bijection from `(−1, 1)` onto the reals;
   - `F_c(−1) < 0 < F_c(1)`;
   - `F_c(c₀) = (s+J_z)(J_z⁴ − (J_x² − J_y²)²)/(4P)` at `c₀ = −S/(2P)`;
   - `u₋ < 0`.

   So, in the triangle regime `|J_x − J_y| < J_z < J_x + J_y`, the `x < 1/2`
   line node's charge flips once, from `+1` to `−1`, at `κ² = u₊` iff
   `|J_x² − J_y²| < J_z²`. Otherwise it is `−1` for every `κ`. A grid of 400
   couplings agrees with the criterion (247 flip, 153 do not). The isotropic limit is `J(J+2)/(4(4+2J−J²))`.
4. **Samples** (exact algebraic numbers; decimals printed):
   - at `(1, 4/5, 1)`, `κ_c² = 0.11809…`;
   - at `(6/5, 4/5, 1)`, `κ_c² = 0.04633…`;
   - at `(2, 1, 5/2)`, `κ_c² = 0.56593…`.
5. **Consistency (floating point).** The charge sign changes across `κ_c`
   (`κ_c(1 ± 10⁻³)`) at six couplings and stays `−1` at two no-flip
   couplings.

## (B) The zone centre at J = 2

At `J_x = J_y = 1`, `J_z = 2`, the zone centre Γ is a touching for every `κ`.

1. **Effective Hamiltonian.** Write `θ = 2πf = x(1,−1,0) + y(1,1,0) + z(0,0,1)`
   with weights `x: 1` and `y, z: 2`.
   - The E = 0 Schur-complement Pauli vector is
     `d = (2(y − z), (1 − 4κ²)x²/2, −8κy)` through weight 4.
   - The weight-4 part of `det H` is `64|d|²`, so Γ is an isolated zero.
2. **κ = 1/2.** The `x²` term vanishes. With weights `(1; 4, 4)`:
   - `d = (2(y − z), x⁴/8, −4y)`;
   - the weight-8 part of `det H` is `64|d|²`;
   - the dispersion along `(1, −1, 0)` is quartic.
3. **Degree zero.** The leading map's Jacobian is odd in `x`, so preimages
   pair up with opposite signs. The local degree is `0` for every `κ > 0`:
   Γ is a semi-Dirac touching of charge zero.
   - For `κ > 1/2` a pair of nodes is born at Γ.
   - The symmetry `H(−f) = −conj H(f)` agrees, giving
     `d(−θ) = (−d_x, d_y, −d_z)`.
4. **Consistency (floating point).** The lowest two bands' fluxes are `0` on
   off-centre ellipsoids around Γ at `κ = 0.5` and `1`, and `±1` at the line
   nodes.

## What this settles and what it does not

- **Settled.**
  - The flip coupling of the line nodes, which earlier work reported as
    numerically verified, is an exact resultant root, with an exact flip
    criterion within the triangle regime.
  - The `J = 2` zone centre is a degree-zero semi-Dirac touching for every
    `κ`.
- **Not settled here.**
  - Couplings outside the triangle regime.
  - Explicit remainder bounds at Γ.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator; (A) general positive couplings, (B) `J = 2`.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed families are used as stated there.
- **N5:** exact algebra; floating-point consistency checks.
- **N6:** the regimes listed above remain open.
- **N7:** other sectors and couplings remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_line_node_flip_coupling_exact_and_j_two_zone_centre_degree_zero_2026_10_01.py
```

Ten checks; prints `TOTAL: PASS=10 FAIL=0` in a few seconds.
