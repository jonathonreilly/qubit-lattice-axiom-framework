---
claim_id: composite_site_network_flux_free_certified_touching_census_at_boundary_couplings_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), D = det M >= 0, charge = sign of T = Im Tr(P d1H P d2H P d3H), at seven boundary couplings (J_x, J_y, J_z; kappa) with J_x != J_y: J_z = J_x + J_y: G1 (6/5, 4/5, 2; 2/5), G2 (6/5, 4/5, 2; 3/5), G3 (6/5, 4/5, 2; 4/5), G4 (3/2, 1/2, 2; 3/4); J_z = J_x - J_y: M1 (6/5, 4/5, 2/5; 3/10), M2 (6/5, 4/5, 2/5; 3/5), M3 (3/2, 1/2, 1; 3/2). At each, the degenerate touching (the zone centre for J_z = J_x + J_y, the corner (1/2, 1/2, 0) for J_z = J_x - J_y) has an explicit quasi-ball N^4 = x^4 + y^2 + z^2 <= rho^4 (rho 0.175 to 0.350) on which exact Laurent polynomials over Q(i), a degree-12 Taylor expansion and the Lagrange remainder give detC < 0, a zero-free homotopy to the leading semi-Dirac map and det H > 0 away from the point, so it is the unique zero there with Pauli-map degree 0; every other touching is verified exactly (rank 2 in the ring of its algebraic coordinates; off-plane orbits have cos 2 pi f_3 a root of an irreducible integer cubic at G3, G4 and an irreducible quintic at M2, M3), charged by interval-signed T and isolated by a Hessian-positive-definite box; an adaptive outward-rounded Taylor clearing shows D > 0 outside the boxes and the ball (cube inclusion in the ball by rigorous upward-rounded bounds). Census besides the degenerate point: G1 none; G2 two line touchings (+, -); G3, G4 four off-plane (+, -, -, +) and two line (-, +); M1 none; M2, M3 four off-plane (+, -, -, +); total charge 0 at each. Not covered: u = P/4 exactly, J_x = J_y on the boundary, couplings in between, the identification of the Pauli-map degree with a band Chern number beyond floating-point fluxes, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_certified_touching_census_at_boundary_couplings_2026_10_01.py
---

# Certified touching census at boundary couplings

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra, explicit remainder bounds and outward-rounded interval certificates, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
at couplings on the two boundaries of the coupling triangle, with `J_x ≠ J_y`.
- On `J_z = J_x + J_y` the zone centre Γ is a degenerate, semi-Dirac touching for every `κ`.
- On `J_z = J_x − J_y` the corner `(1/2, 1/2, 0)` is.

At these points the Hessian of `det M` is singular, so they need explicit
neighbourhoods rather than convexity boxes.

## Census

`P = J_xJ_y` and `u = κ²`. The table lists touchings besides the degenerate point.

| Label | `(J_x, J_y, J_z; κ)` | Degenerate point | Off-plane (charges) | Line (charges) | Total |
|---|---|---|---|---|---|
| G1 | `(6/5, 4/5, 2; 2/5)` | Γ, `u < P/4` | none | none | 0 |
| G2 | `(6/5, 4/5, 2; 3/5)` | Γ, `P/4 < u < P/2` | none | `+, −` | 0 |
| G3 | `(6/5, 4/5, 2; 4/5)` | Γ, `u > P/2` | `+, −, −, +` (cubic) | `−, +` | 0 |
| G4 | `(3/2, 1/2, 2; 3/4)` | Γ, `u > P/2` | `+, −, −, +` (cubic) | `−, +` | 0 |
| M1 | `(6/5, 4/5, 2/5; 3/10)` | corner | none | none | 0 |
| M2 | `(6/5, 4/5, 2/5; 3/5)` | corner | `+, −, −, +` (quintic) | none | 0 |
| M3 | `(3/2, 1/2, 1; 3/2)` | corner | `+, −, −, +` (quintic) | none | 0 |

- "cubic" and "quintic" give the degree of the irreducible integer polynomial
  satisfied by `cos 2πf₃` on the off-plane orbit.
- On `J_z = J_x + J_y` at these couplings it is a cubic. On `J_z = J_x − J_y` it is a quintic.

## How each entry is established

1. **The degenerate point.** On an explicit quasi-ball `N⁴ = x⁴ + y² + z² ≤ ρ⁴`
   (`ρ` from 0.175 to 0.350), the following hold:
   - The method is exact Laurent polynomials over `Q(i)`, a degree-12 Taylor
     expansion and the Lagrange remainder.
   - `det C < 0`.
   - The homotopy from the full Schur numerator to the leading semi-Dirac map has no zero.
   - `det H > 0` away from the point.

   So the point is the unique zero in its ball, and its Pauli map has degree 0.
2. **Other touchings.** Each is checked exactly: rank 2 in the ring of its
   algebraic coordinates. Each is charged by interval-signed `T` and isolated by a
   Hessian-positive-definite box.
3. **Completeness.** An adaptive outward-rounded Taylor clearing shows
   `det M > 0` outside the boxes and the ball. Whether a cube lies inside the ball
   is decided by rigorous upward-rounded bounds.

## Controls

Each of the following fails as it should:
- removing a box or the ball leaves uncleared cubes outside;
- perturbed data give a nonzero determinant;
- a wrong centre leaves a node unmatched;
- a moved centre or an oversized box breaks the box test;
- an oversized ball or a perturbed leading coefficient breaks the ball conditions.

Floating-point checks: the Fukui fluxes are `∓1` around the G2 line nodes and
`0` through the ball spheres. The ball-inclusion and Taylor bounds were also
checked against sampled values.

## What this settles and what it does not

- **Settled.** At these seven boundary couplings, the complete touching set with
  charges, including the degenerate point (degree 0). Total charge 0 at each.
- **Not settled here.**
  - `u = P/4` exactly.
  - `J_x = J_y` on the boundary.
  - Couplings in between.
  - The identification of the Pauli-map degree with a band Chern number beyond
    floating-point fluxes.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at seven boundary couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator and charge convention are used as stated there.
- **N5:** exact algebra, remainder bounds and outward-rounded certificates; floating-point checks are labelled.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_certified_touching_census_at_boundary_couplings_2026_10_01.py
```

Thirty-two checks; prints `TOTAL: PASS=32 FAIL=0` in under a minute.
