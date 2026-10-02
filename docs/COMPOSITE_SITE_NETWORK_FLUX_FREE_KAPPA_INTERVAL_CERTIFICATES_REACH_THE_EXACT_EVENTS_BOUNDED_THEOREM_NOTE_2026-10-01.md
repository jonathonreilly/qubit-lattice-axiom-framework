---
claim_id: composite_site_network_flux_free_kappa_interval_certificates_reach_the_exact_events_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), J_x = J_y = 1, J_z = 1 (and one anisotropic coupling (1, 4/5, 1)). Exact (sympy): on the line, plane-(ii) and plane-(iii) families det H, its gradient and the constant and linear characteristic coefficients vanish identically for symbolic kappa; the characteristic polynomial is invariant under f -> -f and f1 <-> f2; kappa_c^2 = 3/20 (line node at cos 2 pi x = -2/3, c3 = 1) and kappa_h^2 = 1/4 (merged plane-(ii) point (1/4, 3/4, 1/2)), where D and grad D vanish and the Hessian of D in theta has rank 2 (kernel f3, block [[608/15, -1312/45], [-1312/45, 608/15]]) at kappa_c and rank 1 (192[[1, -1], [-1, 1]]) at kappa_h; at kappa = 0, D = 16|(1 + z1)(1 + z2) - w|^2, a nodal curve through the kappa -> 0 line-node limit (1/3, 2/3, 0); at (1, 4/5, 1) the flip coupling is kappa_c^2 = (-6134 + 354 sqrt 5441)/169175. Interval (outward-rounded congruence inertia, exact symmetry transport of node certificates with verified image inclusion, f-Taylor clearing with a rigorous remainder bound): for every kappa in each of the seven cells [19/50, 191/500], [87/200, 89/200], [97/200, 49/100], [13/25, 53/100], [3/5, 31/50], [1/25, 1/20] at J = 1 and [3/10, 8/25] at (1, 4/5, 1), the middle bands touch at exactly the family nodes: 2 line nodes (+-) below kappa_c, 6 nodes (-+++--) between kappa_c and kappa_h, 6 nodes (-+-+-+) above kappa_h, 2 line nodes (+-) at the anisotropic coupling below its flip. Cells containing kappa_c or kappa_h are refused by the certifier. Reported (logged development certificates of the same code, not re-run by this runner): 55 cells cover kappa in [0.008, 0.385], [0.400, 0.496], [0.505, 1.1] at J = 1 and [0.03, 0.34] at (1, 4/5, 1). Not covered: the gaps around kappa_c, kappa_h and kappa -> 0, other couplings, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_kappa_interval_certificates_extended_to_the_exact_event_gaps_2026_10_01.py
---

# κ-interval certificates reach the exact events

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra plus outward-rounded interval certificates on κ-cells, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
at `J_x = J_y = J_z = 1`. One anisotropic coupling, `(1, 4/5, 1)`, is also treated.

## Exact events

| Coupling | κ | What holds there |
|---|---|---|
| birth | `κ_c² = 3/20` | Line node at `cos 2πx = −2/3`, `c₃ = 1`. The Hessian of `D` has rank 2, with kernel `f₃` and block `[[608/15, −1312/45], [−1312/45, 608/15]]`. |
| handover | `κ_h² = 1/4` | Merged plane-(ii) point `(1/4, 3/4, 1/2)`. The Hessian has rank 1, `192[[1, −1], [−1, 1]]`. |
| limit | `κ = 0` | `D = 16\|(1+z₁)(1+z₂) − w\|²`, a nodal curve through the κ → 0 line-node limit `(1/3, 2/3, 0)`. |
| anisotropic flip | `(1, 4/5, 1)` | `κ_c² = (−6134 + 354√5441)/169175`. |

Further exact facts:
- On the line, plane-(ii) and plane-(iii) families, `det H`, its gradient and the constant and linear characteristic coefficients vanish identically for symbolic κ.
- The characteristic polynomial is invariant under `f → −f` and `f₁ ↔ f₂`.

## Certified cells

The method extends the landed κ-interval certificate in three ways:
- exact-symmetry transport of node certificates, with verified inclusion of each image;
- first-order f-Taylor clearing with a rigorous remainder bound;
- anisotropic couplings.

For every κ in each cell below, the middle bands touch at exactly the family nodes.

| Cell | Coupling | Nodes (charges) |
|---|---|---|
| `[19/50, 191/500]`, 0.0073 below κ_c | J = 1 | 2 line nodes (+, −) |
| `[87/200, 89/200]` | J = 1 | 6 nodes (−, +, +, +, −, −) |
| `[97/200, 49/100]`, 0.01 below κ_h | J = 1 | 6 nodes (−, +, +, +, −, −) |
| `[13/25, 53/100]`, 0.02 above κ_h | J = 1 | 6 nodes (−, +, −, +, −, +) |
| `[3/5, 31/50]` | J = 1 | 6 nodes (−, +, −, +, −, +) |
| `[1/25, 1/20]` | J = 1 | 2 line nodes (+, −) |
| `[3/10, 8/25]` | (1, 4/5, 1) | 2 line nodes (+, −) |

The certifier refuses cells that contain κ_c or κ_h. Controls fail as they should:
- the Hessian test at the κ_c point;
- wrong-map inclusion and a tiling gap;
- a removed node tube.

## Reported coverage (development logs)

These certificates come from the same code and are not re-run by this runner.

- **J = 1:** 55 cells cover κ ∈ `[0.008, 0.385]`, `[0.400, 0.496]` and `[0.505, 1.1]`.
- **(1, 4/5, 1):** the cells cover κ ∈ `[0.03, 0.34]`.

The three J = 1 gaps contain the birth at κ_c, the handover at κ_h and the κ → 0
limit. Inside the gaps the certificates say nothing.

## What this settles and what it does not

- **Settled.** The node count, with charges, on the seven re-certified cells, and
  the exact events that bound the regimes.
- **Not settled here.**
  - The gaps themselves.
  - Other couplings.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at J = 1 and (1, 4/5, 1).
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator and certificate are used as stated there.
- **N5:** exact algebra and outward-rounded interval certificates.
- **N6:** the gaps remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_kappa_interval_certificates_extended_to_the_exact_event_gaps_2026_10_01.py
```

Twenty-three checks; prints `TOTAL: PASS=23 FAIL=0` in about 4.5 minutes.
