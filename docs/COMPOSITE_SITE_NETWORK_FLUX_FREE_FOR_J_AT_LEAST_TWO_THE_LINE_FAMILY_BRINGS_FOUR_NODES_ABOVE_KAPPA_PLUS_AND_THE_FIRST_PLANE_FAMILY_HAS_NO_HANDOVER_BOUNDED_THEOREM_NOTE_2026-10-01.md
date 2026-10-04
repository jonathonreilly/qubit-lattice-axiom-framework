---
claim_id: composite_site_network_flux_free_for_j_at_least_two_the_line_family_brings_four_nodes_above_kappa_plus_and_the_first_plane_family_has_no_handover_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J_x = J_y = 1, J_z = J, odd term kappa, four-site Bloch matrix H(f) = i M(f); the three exact touching families of the landed certificate note (det H, its gradient and the two lowest characteristic-polynomial coefficients vanish on them identically, re-checked here), now read for J >= 2 (and J < 0). Exact, with K = kappa^2: (i) for J > 2 both line roots lie in (-1, 1) iff K >= K_+(J) = [(J^2-2) + J sqrt(J^2-4)]/8 and none below (two distinct points at K_+, four distinct line nodes strictly above K_+); at J = 2 the zone centre Gamma is a line node for every kappa and the second root 1/(2K) - 1 enters (-1, 1) for K > 1/4; (ii) on the present J >= 2 domain the first plane family is real iff 2 <= J < 1 + sqrt5 and K >= kappa_c^2 = J(J+2)/[4(4+2J-J^2)], with no upper limit for J >= 2, born from one line root (the smaller for J < J0, the larger for J > J0, J0 the root of J^3 - 4J - 4 where kappa_c^2 = K_+); (iii) the second plane family is never real for J >= 2, so there is no handover; every real family point (J != 0) is an exact double zero level with outer levels at least 2|J|; at J = 2 and kappa > 0, Gamma has a rank-two Hessian, rank one at kappa = 0; along (1,-1,0), det H has fourth order for K != 1/4 and eighth order at K = 1/4; for J < 0 only the line family (that of |J|) appears. The closed forms agree with exact real-root counts at 7680 rational couplings. Interval certificates (outward rounding, the landed method): gapped everywhere at (5/2, 99/100) and (4, 1); exactly the family nodes, conical with chirality strings -++- (4, 2), -+-+++-- (5/2, 3/2) and six conical nodes plus an unresolved cluster containing the exact Gamma double zero at (2,1); -+0++-- records six conical signs and a zero placeholder, not Gamma's local degree. Not covered: completeness between the certified couplings, the boundary couplings K_+, kappa_c^2, J0, J = 0, Gamma's local degree, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_touching_families_for_j_at_least_two_2026_10_01.py
---

# For J ≥ 2 the line family brings four nodes above κ₊, and the first plane family has no handover

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra with interval certificates at sampled couplings; unaudited.

## Supplied setting

Use the supplied comparator and the three exact touching families of the landed note
[current mathematical parent](COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md),
with `J_x = J_y = 1` and `J_z = J`:
- (i) the line `(x, 1−x, 0)`;
- (ii) the plane `f₁ + f₂ = 1`;
- (iii) the plane `f₁ + f₂ = 2f₃`.

That note states the families' real ranges for `0 < J < 2`. It certifies one
coupling beyond, `J = 5/2`, `κ = 3/10`, where the middle gap is open. This
block determines exactly where each family is real for `J ≥ 2`, and for
`J < 0`.

## Result

Write `K = κ²`.

1. **The families are exact for all couplings.** `det H`, its gradient and
   the two lowest characteristic-polynomial coefficients vanish identically
   on all three families, modulo their defining polynomials.
2. **Line (i), J > 2.** Both roots of
   `4Kc² − 2c + J² − 4K − 2 = 0` lie in `(−1, 1)` iff `K ≥ K₊(J)`, where
   `K₊(J) = [(J² − 2) + J√(J² − 4)]/8`. Below that there are none.
   - At `K = K₊`, the two cosine roots coincide, giving two distinct
     points, not four. There are four line nodes only for `K > K₊`.
   - `K₊(2) = 1/4`, `K₊(5/2) = 1`, `K₊(3) = (7 + 3√5)/8` and
     `K₊(4) = 7/4 + √3`.
3. **J = 2.** The zone centre Γ is a line node for every κ. The second root
   `1/(2K) − 1` enters `(−1, 1)` for `K > 1/4`. At Γ the Hessian of `det H`
   has rank two for `κ > 0`, and rank one at `κ = 0`. Along `(1,−1,0)`,
   `det H = 16(c−1)²[4K(c+1)−2]²`: fourth order for `K ≠ 1/4`,
   eighth order at `K = 1/4`. Thus Γ is not conical.
4. **First plane family (ii).** On the present `J ≥ 2` domain it is real iff
   `2 ≤ J < 1 + √5` and
   `K ≥ κ_c² = J(J+2)/[4(4+2J−J²)]`. For `J ≥ 2` there is no upper limit in
   `K`. For `0 < J < 2`, the earlier family note also requires
   `K ≤ κ_h²`; this note does not remove that upper bound.
   - It is born from one line root: the smaller one for `J < J₀`, the larger
     for `J > J₀`.
   - `J₀ = 2.3830…` is the root of `J³ − 4J − 4`, where `κ_c² = K₊`;
     otherwise `κ_c² > K₊`.
5. **Second plane family (iii).** It is never real for `J ≥ 2`, for either
   sign of the square root. The handover at `κ_h` is a `J < 2` phenomenon.
6. **Double level.** Every real family point with `J ≠ 0` is an exact double
   zero level, with outer levels at least `2|J|` (exactly `4|J|` on the
   line).
7. **J < 0.** The line family is that of `|J|`. Plane (ii) is never real, and
   plane (iii) is real at `J = −2` and there it is the point Γ. `J → −J` is not a symmetry
   of `det H`.
8. **Cross-check.** The closed-form real regions agree with exact real-root
   counts at 7680 rational couplings (`J = n/8` in `[−6, 6]`,
   `κ = n/20` in `(0, 4]`), with no mismatch.
9. **Interval certificates** (outward rounding, the landed method):

   | (J, κ) | state | certificate |
   |---|---|---|
   | (5/2, 99/100) | `K < K₊ = 1` | middle gap open everywhere (9 levels) |
   | (4, 1) | `K < K₊ = 3.48` | middle gap open everywhere |
   | (4, 2) | four line nodes | exactly the family nodes, conical, chirality `−++−`, sum 0 |
   | (5/2, 3/2) | four line and four plane-(ii) nodes | exactly the family nodes, conical, chirality `−+−+++−−`, sum 0 |
   | (2, 1) | Γ, two line and four plane-(ii) nodes | six unique conical nodes; a seventh cluster contains Γ, with uniqueness inside that cluster unproved; `0` is a placeholder, not a Γ charge |

## What follows

For `J ≥ 2` the touchings are organised as follows:
- **Below `K₊`:** the comparator is gapped (certified at two couplings).
- **At `K₊` for `J > 2`:** two distinct line points appear; they split into four above it.
- **Above `κ_c²`:** the first plane family adds four more for every larger κ,
  while `J < 1 + √5`.
- **No handover:** the second plane family never appears.
- **At `J = 2`:** Γ is a non-conical touching present at every κ.

## Boundary

- Completeness of the families, meaning no other touchings, is certified at
  four non-Γ sampled couplings and not between them. At `(J,κ)=(2,1)`
  it clears the complement of seven clusters and proves uniqueness only
  in the six conical boxes. It does not exclude additional zeros inside
  the Γ cluster.
- The boundary couplings `K₊`, `κ_c²`, `J₀` and `J = 0` are not covered.
- Γ's local degree at `J = 2` is not determined.
- Spin-model equivalence and any physical reading are outside this block.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator with `J_x = J_y = 1`, `J ≥ 2` (and `J < 0`); certificates at five couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed certificate note's families and method are used as stated there.
- **N5:** exact real-range algebra; interval certificates at samples.
- **N6:** completeness between samples and the boundary couplings remain open.
- **N7:** other sectors and anisotropies remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_touching_families_for_j_at_least_two_2026_10_01.py
```

Fifteen checks; prints `TOTAL: PASS=15 FAIL=0` in about a hundred seconds.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) sets the premise boundary. The supplied comparator is not a framework-law or physical-species selection. Original source and execution history remain recoverable at [PR #9422](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9422); this is provenance, not audit authority.

Network definition: [current supplied network](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
