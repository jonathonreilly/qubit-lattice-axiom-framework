---
claim_id: composite_site_network_flux_free_node_count_versus_kappa_at_an_anisotropic_coupling_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), at (J_x, J_y, J_z) = (6/5, 4/5, 1), odd term kappa > 0. Exact: M anti-Hermitian on the torus with det(mu - M) = mu^4 + a2 mu^2 + D; |d_x|^2 det M = s_1^2 + s_2^2 + s_3^2 with |d_x|^2 >= 16/25, so the touchings are the zeros of the vector field s on the torus; on the line (x, 1 - x, 0) det M = 16 q^2 and det(ds/df) = -8192 pi^3 kappa sin(2 pi x) q'(c) F_c(c) modulo q, Res_c(q, F_c) proportional to 34375u^2 + 5400u - 324 (u = kappa^2, irreducible), so the line-node index changes sign once, at kappa_c^2 = (18 sqrt 91 - 108)/1375 (+1 below, -1 above for x < 1/2); on the plane f_2 = 0 a complete elimination gives exactly two real zeros of s, both at kappa^2 = 99/100 (cos 2 pi f_1 = -17/33, cos 2 pi f_3 = -1/3); crossings of the planes f_1 - f_2 = 1/2, f_1 - f_3 = 1/2, f_2 = f_3 by an off-plane zero occur at kappa^2 = (151 + sqrt 301)/625, (14 sqrt 31 - 53)/165, (233608 + 9874 sqrt 394)/2016125 (exact algebraic solution identities, plus independent outward-rounded Krawczyk existence boxes nearby; identification of an exact algebraic point with the boxed point is not proved by the floating proximity test). Interval (outward-rounded double arithmetic with mpmath.iv phase tables; parametric Krawczyk boxes with existence and uniqueness for every kappa in a cell, and hierarchical clearing of the rest of the torus over the cell): s has exactly 2 zeros for every kappa in [1/10, 3/25] and exactly 6 for every kappa in [99/100, 1], [6/5, 61/50], [103/200, 21/40], [77/200, 79/200] and [913/2000, 933/2000], all simple, with a2 > 0. Floating point: a Newton sweep over kappa = j/30 (j = 1..60) finds 2 zeros for kappa <= 0.2 and 6 from 0.233 on, and the off-plane pair emerges from the line node near kappa_c with f_3^2 linear in kappa - kappa_c. Not covered: certification near kappa_c and between the listed intervals, kappa < 1/10, other couplings, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_node_count_versus_kappa_at_an_anisotropic_coupling_2026_10_01.py
---

# Node count versus κ at an anisotropic coupling

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra plus outward-rounded interval certificates on κ-intervals, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
at `(J_x, J_y, J_z) = (6/5, 4/5, 1)`, with odd term `κ > 0`.

Since `|d_x|² det M = s₁² + s₂² + s₃²` and `|d_x|² ≥ 16/25`, the middle-band touchings
are exactly the zeros of the vector field `s` on the torus.

## Exact events

**E1 — the exact line-node index flip.** On the line `(x, 1 − x, 0)`:
- `det M = 16q²`;
- `det(ds/df) = −8192π³κ sin(2πx) q′(c) F_c(c)` modulo `q`;
- `Res_c(q, F_c)` is proportional to the irreducible polynomial `34375u² + 5400u − 324`,
  with `u = κ²`.

So the index of the `x < 1/2` line node changes sign exactly once, from `+1` to `−1`,
at `κ_c² = (18√91 − 108)/1375`, that is `κ_c ≈ 0.21525`. In floating point, an
off-plane pair emerges from the line node there, with `f₃²` linear in `κ − κ_c`.

**Events with no count change.** The off-plane orbit crosses symmetry and
coincidence planes:

| Event | Plane | `κ²` | Method |
|---|---|---|---|
| E2 | `f₂ = 0` (and `f₁ = 0`) | `99/100` | complete elimination on the plane: exactly two real zeros, at `cos 2πf₁ = −17/33`, `cos 2πf₃ = −1/3` |
| E3 | `f₁ − f₂ = 1/2` | `(151 + √301)/625` | exact algebraic solution identities; independent Krawczyk existence box nearby |
| E4 | `f₁ − f₃ = 1/2` | `(14√31 − 53)/165` | as E3 |
| E5 | `f₂ = f₃` | `(233608 + 9874√394)/2016125` | as E3 |

## Certified counts on κ-intervals

Each κ-interval is split into cells.
- **Node cubes.** A parametric Krawczyk test shows each node cube contains exactly
  one zero of `s` for every κ in the cell.
- **Rest of the torus.** A hierarchical clearing over the cell shows `s ≠ 0`
  everywhere outside the node cubes. It uses mean-value enclosures in `f` and `κ`,
  outward-rounded double arithmetic and iv phase tables.

| κ-interval | zeros of `s` for every κ |
|---|---|
| `[1/10, 3/25]` | exactly 2 |
| `[99/100, 1]` (contains E2) | exactly 6 |
| `[6/5, 61/50]` | exactly 6 |
| `[103/200, 21/40]` (contains E3) | exactly 6 |
| `[77/200, 79/200]` (contains E4) | exactly 6 |
| `[913/2000, 933/2000]` (contains E5) | exactly 6 |

All zeros are simple, and `a₂ > 0` on the node cubes.

Two controls fail as they should: leaving out a node cube, and the Krawczyk
test with the identity preconditioner.

## Floating-point consistency

- A Newton sweep at `κ = j/30` (`j = 1, …, 60`) finds 2 zeros for `κ ≤ 0.2` and 6
  from `0.233` on.
- At every node found, the sign of `det(ds/df)` equals the chirality sign.

## What this settles and what it does not

- **Settled.** At `(6/5, 4/5, 1)`:
  - the line-node index flips at the exact coupling `κ_c`; a full count
    transition there is observed numerically and remains uncertified;
  - the listed planes admit exact algebraic solution identities at the stated
    couplings, alongside certified nearby plane-system existence boxes;
  - the count is certified on six κ-intervals, four of which straddle those crossings.
- **Not settled here.**
  - Certification near `κ_c` and between the listed intervals.
  - `κ < 1/10`.
  - Other couplings.
  - Equality with the spin model, and any physical reading.

## Event and arithmetic limits

The six interval counts do not certify a full count transition at `κ_c`.
The plane-system Krawczyk boxes have radius `10⁻⁹`, whereas the algebraic
coordinate comparison accepts floating proximity `10⁻⁸`. That comparison
does not prove the exact algebraic point lies in the same box. The exact
polynomial identities and the interval existence/uniqueness statements
are retained separately; exact point-to-box identification, and uniqueness
of the events over all κ, remain open.

In the parametric census, spatial cube centres are dyadic: `cs` has at most
20 fractional bits, `ρ=2⁻ᵖ`, and the subgrid uses `mf=16`. The clearing grid
is dyadic through level 15. Their displayed additions, subtractions and
integer periodic shifts are exactly representable in binary64 on these
bounded fixtures. Phase arithmetic encloses those exact centres. The
small inflation factors dominate the bounded positive sums used for
Lipschitz radii; they do not grant an arbitrary-input interval theorem.

## Reviewed source connections

- [COMPOSITE_SITE_NETWORK_FLUX_FREE_OFF_PLANE_TOUCHINGS_ARE_QUINTIC_ALGEBRAIC_POINTS_AT_FIVE_ANISOTROPIC_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md](COMPOSITE_SITE_NETWORK_FLUX_FREE_OFF_PLANE_TOUCHINGS_ARE_QUINTIC_ALGEBRAIC_POINTS_AT_FIVE_ANISOTROPIC_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_ACROSS_COUPLING_REGIMES_BOUNDED_THEOREM_NOTE_2026-10-01.md](COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_ACROSS_COUPLING_REGIMES_BOUNDED_THEOREM_NOTE_2026-10-01.md)

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at one anisotropic coupling; κ-intervals as listed.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator is used as stated there.
- **N5:** exact algebra and outward-rounded interval certificates; floating-point checks are labelled.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_node_count_versus_kappa_at_an_anisotropic_coupling_2026_10_01.py
```

Seventeen checks; prints `TOTAL: PASS=17 FAIL=0` in about a minute.
