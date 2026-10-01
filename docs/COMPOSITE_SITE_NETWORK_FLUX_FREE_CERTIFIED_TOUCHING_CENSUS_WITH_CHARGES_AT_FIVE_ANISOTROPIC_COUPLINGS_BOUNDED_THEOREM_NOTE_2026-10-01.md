---
claim_id: composite_site_network_flux_free_certified_touching_census_with_charges_at_five_anisotropic_couplings_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), D = det M >= 0, at (J_x, J_y, J_z; kappa) = B (6/5, 4/5, 1; 3/10), A (1, 4/5, 1; 9/20), C (1, 4/5, 1; 4/5), F (2, 1, 5/2; 9/10), G (3/2, 1/2, 4/5; 3/2). Charge of a touching := sign of T = Im Tr(P d1H P d2H P d3H) (P the kernel projector), as in the landed notes. (1) Exact: at each coupling the off-plane algebraic point (cos 2 pi f_3 the root in [-1, 1] of an irreducible integer quintic, the other coordinates from degree-4 rational polynomials) gives four touchings, one per sign choice of (t, d) = (sin 2 pi f_3, cos 2 pi f_1 - cos 2 pi f_2), with rank M = 2 in the ring Q[alpha, t, d, i]/(...); there T = c(alpha) t d exactly; at B, A, C, F the line (x, 1 - x, 0) has one root of q in [-1, 1] (at B, cos 2 pi x = -2/3) giving two line touchings, at G none. (2) Interval (outward-rounded mpmath.iv): sign T at the four off-plane touchings is +1, -1, -1, +1 for (t, d) = (+,+), (+,-), (-,+), (-,-), and the line touchings at x < 1/2 and x > 1/2 have -1 and +1. (3) Interval: around each touching a box of half-width 5e-5 in f on which the Hessian of D is positive definite and the touching lies, so it is the unique zero in the box; a2 > 0 on each box (levels -l1, 0, 0, l1). (4) Interval: adaptive dyadic clearing of the whole torus with a second-order Taylor lower bound of D (iv-enclosed phases, nextafter-outward double sums, third-order remainder) shows D > 0 on every cube not contained in one of the boxes. Hence at B, A, C and F the middle bands touch at exactly six points (four off-plane, two on the line) with charges +1, -1, -1, +1, -1, +1, and at G at exactly four off-plane points with charges +1, -1, -1, +1; the total charge is 0 at each. Not covered: other couplings, J_z > J_x + J_y, a closed form in the couplings, Chern numbers on surfaces beyond the local charges, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_certified_touching_census_with_charges_at_five_anisotropic_couplings_2026_10_01.py
---

# Certified touching census with charges at five anisotropic couplings

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra plus outward-rounded interval certificates, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
with general couplings, at five rational couplings `(J_x, J_y, J_z; κ)`:

| Label | Coupling |
|---|---|
| B | `(6/5, 4/5, 1; 3/10)` |
| A | `(1, 4/5, 1; 9/20)` |
| C | `(1, 4/5, 1; 4/5)` |
| F | `(2, 1, 5/2; 9/10)` |
| G | `(3/2, 1/2, 4/5; 3/2)` |

`D = det M ≥ 0`. A touching's charge is the sign of
`T = Im Tr(P∂₁H P∂₂H P∂₃H)`, where `P` is the kernel projector. This is the
landed convention.

## Census

| Coupling | Off-plane touchings (charges) | Line touchings (charges) | Total |
|---|---|---|---|
| B | 4 (+1, −1, −1, +1), `\|T\| = 143.86` | 2 (−1, +1), `\|T\| = 106.49` | 0 |
| A | 4 (+1, −1, −1, +1), `\|T\| = 206.72` | 2 (−1, +1), `\|T\| = 248.49` | 0 |
| C | 4 (+1, −1, −1, +1), `\|T\| = 2274.4` | 2 (−1, +1), `\|T\| = 1900.5` | 0 |
| F | 4 (+1, −1, −1, +1), `\|T\| = 2163.1` | 2 (−1, +1), `\|T\| = 1638.8` | 0 |
| G | 4 (+1, −1, −1, +1), `\|T\| = 14150` | none | 0 |

How to read the table:
- The off-plane charges are listed for `(t, d) = (+,+), (+,−), (−,+), (−,−)`, where
  `t = sin 2πf₃` and `d = cos 2πf₁ − cos 2πf₂`.
- The line charges are for `x < 1/2` and `x > 1/2` on `(x, 1 − x, 0)`.
- At B the line touchings sit at `cos 2πx = −2/3`.

## How each entry is established

1. **Exact points.** The off-plane point has `cos 2πf₃` equal to the root in
   `[−1, 1]` of an irreducible integer quintic. The other coordinates are given by
   degree-4 rational polynomials.
   - All four sign images are handled at once in the ring
     `Q[α, t, d, i]/(…)`, where `rank M = 2` exactly.
   - There `T = c(α)·t·d` exactly.
   - The line touchings are the roots of the line quadratic `q` in `[−1, 1]`.
2. **Charges.** The sign of `T` comes from the exact ring element, with `α` and
   the square roots enclosed by `mpmath.iv`. The sign pattern follows from
   `T = c(α)·t·d` and `T ∝ t` on the line.
3. **Isolation.** Around each touching there is a box of half-width `5·10⁻⁵` in
   `f`. On it the Hessian of `D` is positive definite (interval midpoint plus a
   Frobenius bound), and the touching lies inside. So it is the unique zero in
   the box. Also `a₂ > 0` there, so the levels are `−l₁, 0, 0, l₁`.
4. **Completeness.** The whole torus is cleared on adaptive dyadic cubes.
   - On each cube `D` is bounded below by its second-order Taylor form at the
     centre, using iv-enclosed phases and a third-order remainder.
   - The sums use `nextafter`-outward double arithmetic.
   - `D > 0` on every cube not contained in a box. The deepest level is 16 to 18,
     and 43k to 100k cubes are processed per coupling.

## Controls

Each of the following fails as it should:
- removing one box leaves uncleared cubes outside the others;
- a perturbed quintic, or a flipped sign, gives a nonzero determinant;
- a moved box centre puts the touching outside its box.

The phase-table enclosures contain 50-digit values. The Taylor bound lies below
sampled `D` on 450 random cubes. This last comparison is floating point.

## What this settles and what it does not

- **Settled.** At these five anisotropic couplings, the complete set of
  middle-band touchings with their charges.
  - Six touchings at B, A, C and F; four at G.
  - Total charge 0 at each.
- **Not settled here.**
  - Other couplings, and `J_z > J_x + J_y`.
  - A closed form in the couplings.
  - Chern numbers on surfaces beyond the local charges.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at five rational couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator and charge convention are used as stated there.
- **N5:** exact algebra and outward-rounded interval certificates.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_certified_touching_census_with_charges_at_five_anisotropic_couplings_2026_10_01.py
```

Twenty-nine checks; prints `TOTAL: PASS=29 FAIL=0` in about half a minute.
