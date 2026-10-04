---
claim_id: composite_site_network_flux_free_slice_chern_numbers_match_the_certified_census_charges_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), at B = (J_x, J_y, J_z; kappa) = (6/5, 4/5, 1; 3/10) and H1 = (6/5, 4/5, 1; 1/5), with the touching lists and charges (charge = sign T, T = Im Tr(P d1H P d2H P d3H)) of the certified censuses (B: four off-plane touchings +1, -1, -1, +1 and two line touchings -1, +1; H1: two line touchings +1, -1), re-found here by Newton from embedded positions with sign det V = charge. Chern numbers C of the two lowest bands on two-dimensional slices of constant f_3, f_1 and f_1 - f_2 (oriented by the +n normal): on every slice used, the middle gap is bounded below by outward-rounded interval inertia on an adaptive quadtree (g >= 0.062 at B, >= 0.40 at H1), and the plaquette phases of the lattice (Fukui) Chern number are bounded below pi by certified derivative constants (bounds <= 0.94), so the exact-arithmetic lattice integer equals the slice Chern number under the linked admissibility lemma; the reported integer is evaluated in floating point and is not interval-authenticated and agrees at two meshes and, at one slice, with a 30-digit recomputation. Values: B, f_3 = 5/256, 1/16, 1/2, 15/16, 251/256: C = 0 throughout; B, f_1 = 0, 5/16, 25/64, 1/2, 39/64, 11/16: C = +1, 0, +1, 0, +1, 0; B, f_1 - f_2 = 0, 5/16, 1/2, 11/16: C = +1, 0, +2, 0; H1, f_3 = 1/4, 1/2: C = 0, 0; H1, f_1 = 0, 1/2: C = +1, 0; H1, f_1 - f_2 = 0, 1/2: C = +1, +2. Every one of the 21 slice-to-slice jumps equals minus the sum of the census charges between the slices (14 nonzero, of size 1 or 2), so the convention C_jump = -charge is checked against both signs. Not covered: other couplings, a proof of the lattice integer by interval arithmetic, completeness of the touching list beyond the cited censuses, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_slice_chern_numbers_match_the_certified_census_charges_2026_10_01.py
---

# Slice Chern numbers match the certified census charges

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** interval-certified gaps and admissibility bounds, floating-point lattice integers, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
at two couplings `(J_x, J_y, J_z; κ)`:

| Label | Coupling | Touchings (charges) |
|---|---|---|
| B | `(6/5, 4/5, 1; 3/10)` | four off-plane (`+1, −1, −1, +1`) and two line (`−1, +1`) |
| H1 | `(6/5, 4/5, 1; 1/5)` | two line (`+1, −1`) |

The charges are `sign T`, with `T = Im Tr(P∂₁H P∂₂H P∂₃H)`. They come from the
certified censuses. The runner re-finds every touching by Newton from embedded
positions and checks `sign det V = charge`.

## Slice Chern numbers

`C` is the Chern number of the two lowest bands on two-dimensional slices of
constant `f₃`, `f₁` or `f₁ − f₂`, each oriented by the `+n` normal.

| Coupling | Slice family | Constants | `C` |
|---|---|---|---|
| B | `f₃` | `5/256, 1/16, 1/2, 15/16, 251/256` | `0, 0, 0, 0, 0` |
| B | `f₁` | `0, 5/16, 25/64, 1/2, 39/64, 11/16` | `+1, 0, +1, 0, +1, 0` |
| B | `f₁ − f₂` | `0, 5/16, 1/2, 11/16` | `+1, 0, +2, 0` |
| H1 | `f₃` | `1/4, 1/2` | `0, 0` |
| H1 | `f₁` | `0, 1/2` | `+1, 0` |
| H1 | `f₁ − f₂` | `0, 1/2` | `+1, +2` |

How each value is established:
- **Gap (interval).** On every slice used, the middle gap is bounded below by
  outward-rounded interval inertia on an adaptive quadtree. The bound is
  `g ≥ 0.062` at B and `g ≥ 0.40` at H1.
- **Admissibility (interval).** Certified derivative constants bound the
  plaquette phases of the lattice (Fukui) Chern number below `π`, at most `0.94`.
  Under the linked admissibility lemma, the exact-arithmetic lattice integer
  equals the slice Chern number. The floating integer still requires
  interval authentication of the links, phases and total before this
  equality certifies its reported numerical value.
- **The integer (floating point).** The lattice integer agrees at two meshes.
  At one slice it also agrees with a 30-digit recomputation of all 4096 plaquette
  phases.

## Jumps against the census

Each of the 21 slice-to-slice jumps equals minus the sum of the census charges
lying between the two slices. Fourteen of the jumps are nonzero, of size 1 or 2.
So the convention "jump = −charge" is checked, and the opposite sign would
contradict all 14.
- The `f₁` slabs at B contain one touching each, so they check the census charges
  one by one.
- Each `f₃` layer at B carries a pair of opposite charges, so `C(f₃)` stays 0.

## What this settles and what it does not

- **Settled.** At B and H1:
  - the stated interval gap/admissibility bounds on the listed slices and
    numerically consistent lattice integers for three slice families;
  - the reported numerical jumps reproduce the census charges under the stated convention.
- **Not settled here.**
  - Other couplings.
  - An interval proof of the lattice integer itself.
  - Completeness of the touching list beyond the cited censuses.
  - Equality with the spin model, and any physical reading.


## Reviewed source connections

- [COMPOSITE_SITE_NETWORK_FLUX_FREE_ANISOTROPIC_TOUCHINGS_EXIST_WITH_UNIT_CHARGE_BY_INTERVAL_GAP_CERTIFICATES_AND_LATTICE_CHERN_NUMBERS_BOUNDED_THEOREM_NOTE_2026-10-01.md](COMPOSITE_SITE_NETWORK_FLUX_FREE_ANISOTROPIC_TOUCHINGS_EXIST_WITH_UNIT_CHARGE_BY_INTERVAL_GAP_CERTIFICATES_AND_LATTICE_CHERN_NUMBERS_BOUNDED_THEOREM_NOTE_2026-10-01.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_WITH_CHARGES_AT_FIVE_ANISOTROPIC_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md](COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_WITH_CHARGES_AT_FIVE_ANISOTROPIC_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_ACROSS_COUPLING_REGIMES_BOUNDED_THEOREM_NOTE_2026-10-01.md](COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_ACROSS_COUPLING_REGIMES_BOUNDED_THEOREM_NOTE_2026-10-01.md)

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at two couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator and charge convention are used as stated there.
- **N5:** interval gap and admissibility bounds; floating-point lattice integers are labelled.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_slice_chern_numbers_match_the_certified_census_charges_2026_10_01.py
```

Thirteen checks; prints `TOTAL: PASS=13 FAIL=0` in about 30 seconds.
