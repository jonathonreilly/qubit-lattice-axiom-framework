---
claim_id: composite_site_network_flux_free_the_touching_count_is_certified_on_whole_kappa_intervals_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J_x = J_y = 1, J_z = J = 1, odd term kappa, four-site Bloch matrix H(f) = i M(f). Computer-assisted certificate valid for EVERY kappa in a rational interval (outward-rounded interval arithmetic, exact rational tiling, exact family algebra): for every kappa in [1/10, 3/25] the middle-band touchings are exactly the 2 line nodes; for every kappa in [21/50, 17/40] exactly the 6 nodes of the line and first plane family; for every kappa in [3/5, 31/50] and in [1, 11/10] exactly the 6 nodes of the line and second plane family. In each case every node is a double zero level with nonzero outer levels, conical with a positive interval cone constant, of constant chirality (strings +-, -+++--, -+-+-+, -+-+-+, each summing to zero), and H has two negative and two positive levels everywhere else. Method: boxes in (f, kappa) are cleared by interval inertia applied to the affine-in-kappa family through a float eigenbasis congruence (validated by an interval diagonal-dominance check; Sylvester's law); uncleared boxes form one blob per exact node tube; a moving frame following each node certifies per kappa sub-cell, with the kappa derivatives of H carried exactly and a third-order remainder in the Weyl radius; an interval Hessian of det H positive definite on each cluster hull gives uniqueness. The exact families are re-verified symbolically with kappa symbolic. Cells containing kappa_c or kappa_h are refused by construction. Not covered: kappa between the certified intervals, the transition couplings, other J, anisotropy, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_touching_count_certified_on_whole_kappa_intervals_2026_10_01.py
---

# The flux-free comparator's touching count is certified on whole κ intervals

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** computer-assisted certificate on four κ intervals; unaudited.

## Supplied setting

Use the supplied comparator and the exact touching families of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
with `J_x = J_y = J_z = 1`. That note certifies the exact touching count at
sampled couplings; between the samples the count is not certified.
This block certifies the count for every `κ` in rational intervals.

## Certificate

1. **Exact families.** The three families (the line, the first plane and the
   second plane) are re-verified symbolically with `κ` left symbolic. On
   them, `det H`, its gradient and the two lowest characteristic-polynomial
   coefficients vanish identically.
2. **Clearing in `(f, κ)`.**
   - `H` is exactly affine in `κ`. So the family `H(c, κ_m) + δH₁(c)`,
     `|δ| ≤ ρ`, over a box can be tested through a congruence by a float
     eigenbasis `Q`.
   - That congruence is validated by an interval check that `QᴴQ` is
     diagonally dominant. By Sylvester's law, interval `LDLᵀ` inertia at `∓r`
     then bounds the whole family.
   - The variation in `f` enters as a Weyl radius.
   - Uncleared boxes form one blob per exact node tube. The tubes come from
     interval evaluation of the exact cosine formulas.
3. **Moving frame.** For each blob and each `κ` sub-cell, the frame follows
   the node. The first and second `κ` derivatives of `H` along the path are
   carried exactly, and a third-order remainder enters the Weyl radius. The
   sub-cells tile each certified cell exactly, in rational arithmetic.
4. **Uniqueness and node properties.**
   - An interval Hessian of `det H` is positive definite on each cluster's
     sheared hull. So there is at most one zero there, and the exact node is
     it.
   - Each node is checked to be a double zero with nonzero outer levels
     (`e₂ < 0`), and conical with a positive interval cone constant. Its
     chirality is certified with a constant sign.
   - Away from the clusters, `H` has two negative and two positive levels.
5. **Exclusion.** Cells containing `κ_c` or `κ_h`, where nodes merge and the
   Hessian degenerates, are refused by construction.

## Result

| κ interval (J = 1) | nodes | sub-cell/node pairs | min cone constant | chirality |
|---|---|---|---|---|
| `[1/10, 3/25]` | 2 (line) | 2 | `0.0104` | `+−` |
| `[21/50, 17/40]` | 6 (line + first plane) | 24 | `0.00216` | `−+++−−` |
| `[3/5, 31/50]` | 6 (line + second plane) | 24 | `0.0204` | `−+−+−+` |
| `[1, 11/10]` | 6 (line + second plane) | 24 | `0.000733` | `−+−+−+` |

For every `κ` in each interval, the middle-band touchings are exactly the
listed family nodes. Each is conical with the stated chirality, and the
chiralities sum to zero.

The chirality strings agree with the exact charge map of the families on
these ranges. Below `κ_c` the line pair carries `(+, −)`. Between `κ_c` and
`κ_h` the line node on the `x < 1/2` side carries `−1`, and the first-plane
nodes beside it carry `+1` each.

## What this settles and what it does not

- **Settled.** On four whole `κ` intervals at `J = 1`, the touching count and
  charges are certified, not just at points. The same method certified
  further intervals in development runs (`[0.05, 0.30]`, `[0.35, 0.37]`,
  `[0.52, 0.53]`, and `[0.10, 0.11]` at `J = 1/2`); this runner reproduces
  the four listed above.
- **Not settled here.**
  - The κ ranges between the certified intervals.
  - The neighbourhoods of `κ_c` and `κ_h`, which are refused by
     construction.
  - Other `J`, and anisotropy.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at `J = 1` on four κ intervals.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed families and certificate method are extended as stated.
- **N5:** interval-certified with outward rounding; float eigenbasis and frame velocities carry no claim.
- **N6:** other κ ranges, J and anisotropy remain open.
- **N7:** other sectors and couplings remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_touching_count_certified_on_whole_kappa_intervals_2026_10_01.py
```

Seven checks; prints `TOTAL: PASS=7 FAIL=0` in about six minutes.
