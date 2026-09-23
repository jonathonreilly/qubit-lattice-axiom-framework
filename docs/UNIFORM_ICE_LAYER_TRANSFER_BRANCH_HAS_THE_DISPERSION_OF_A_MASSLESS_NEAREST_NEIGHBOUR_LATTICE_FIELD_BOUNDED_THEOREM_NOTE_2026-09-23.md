---
claim_id: uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "In the zero-flux sector of uniform ice on the cross-sections 2 x 8 and 4 x 4, the layer transfer T of open PR 8740 commutes with the transverse translations and with the complement v -> 1 - v, so its spectrum splits by transverse wavenumber and complement parity. With the row transfer of open PR 8859, the top level in each wavenumber sector gives D(k) = ln(lam_0 / |lam_top(k)|). On the strip 2 x 8 at physical wavenumber q = pi/4, pi/2 and 3 pi/4, D = 0.7429, 1.3165 and 1.6581; the nearest-neighbour lattice field on Z^3, whose transfer rate satisfies cosh D = 1 + sum_i (1 - cos q_i), gives 0.7478, 1.3170 and 1.6530, so every point is within 1%. On the square 4 x 4 at q = (pi/2, 0), (pi/2, pi/2) and (pi/2, pi), D = 1.2963, 1.7419 and 2.0469 against 1.3170, 1.7627 and 2.0634, within 2%, and the diagonal-to-axis ratio 1.3438 agrees with the field's 1.3385 within 1%. The field has no free constant: no velocity, stiffness or mass is fitted. The vacuum is even under the complement with a positive level; all 10 branch states computed are odd with negative levels, as single quanta of the staggered field (-1)^(x+y) (2v - 1) are. Opposite wavenumbers, and (pi/2, 0) with (0, pi/2), are degenerate. The wavenumber-0 top equals the top of the full zero-flux sector, and the lowest branch points reproduce the gaps of open PR 8864 (8 D(pi/4) = 5.9434 on 2 x 8, D(pi/2, 0) = 1.29627 on 4 x 4). No limit beyond the computed cross-sections is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_2026_09_23.py
---

# Uniform ice: the layer transfer's zero-flux branch has the dispersion of a massless nearest-neighbour lattice field

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8864 found that the
zero-flux layer chain of uniform ice has a gap falling like 1/b on the
strips 2 × b and following the smallest transverse wavenumber. This block
resolves the chain's spectrum by wavenumber and asks what the whole branch
looks like.

## Result up front

1. **Two symmetries split the spectrum.** The layer transfer T commutes
   with the transverse translations, so its zero-flux spectrum splits by
   transverse wavenumber. T also commutes with the complement v → 1 − v,
   which flips every link occupation, because the rule "three of six links
   occupied" is self-complementary. The runner computes the top level of T
   in each wavenumber sector with the row transfer of open PR 8859, and
   sets D(k) = ln(λ_0 / |λ_top(k)|).

2. **Occupation and field wavenumbers.** The field on a link is
   (−1)^(x+y) (2v − 1): the occupation with the staggered sign. A single
   field quantum at physical wavenumber q therefore sits at occupation
   wavenumber q + (π, π), and it is odd under the complement.

3. **The branch matches a massless lattice field.** The nearest-neighbour
   lattice field on Z^3, the graph Laplacian of the landed note
   `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`,
   has symbol Σ_i 2(1 − cos k_i). At transverse wavenumber q its pole
   along the transfer direction sits at k_z = iD with

   cosh D = 1 + Σ_i (1 − cos q_i).

   It has no mass and no free constant. The measured branch:

   | cross-section | q | D (ice) | D (field) | deviation |
   |---|---|---|---|---|
   | 2 × 8 | π/4 | 0.7429 | 0.7478 | −0.7% |
   | 2 × 8 | π/2 | 1.3165 | 1.3170 | −0.04% |
   | 2 × 8 | 3π/4 | 1.6581 | 1.6530 | +0.3% |
   | 4 × 4 | (π/2, 0) | 1.2963 | 1.3170 | −1.6% |
   | 4 × 4 | (π/2, π/2) | 1.7419 | 1.7627 | −1.2% |
   | 4 × 4 | (π/2, π) | 2.0469 | 2.0634 | −0.8% |

   The diagonal-to-axis ratio on the square, 1.3438, agrees with the
   field's 1.3385 within 1%.

4. **The branch is made of single field quanta.** The vacuum is even
   under the complement and has a positive level. All 10 branch states
   computed are odd under the complement and have negative levels. The
   odd parity is that of one quantum of the field (−1)^(x+y) (2v − 1). The
   negative level is the same staggered sign along the transfer direction
   that open PR 8864 found for the next level.

5. **Symmetry pairs and cross-checks.** Opposite wavenumbers are
   degenerate on the strip, and (π/2, 0) is degenerate with (0, π/2) on
   the square. The wavenumber-0 top equals the top of the full zero-flux
   sector, λ_0 = 4727353.1633 on 2 × 8. The lowest branch points are the
   gaps of open PR 8864: 8 D(π/4) = 5.9434 on 2 × 8 and
   D(π/2, 0) = 1.29627 on 4 × 4. The next level found there is the bottom
   of this branch.

6. **What this means.** The zero-flux layer chain carries one branch of
   odd, single-quantum states whose rate D(q) follows the massless
   nearest-neighbour lattice field within 2% on both computed shapes, with
   nothing fitted. The slope at small q is fixed by the cubic symmetry,
   which makes the transfer direction equivalent to the transverse ones;
   the agreement across the whole branch up to q = π is measured, not
   derived. With the Gaussian flux stiffness of open PRs 8746 and 8859
   and the gapless chain of open PR 8864, the flux seen by formation units
   behaves on the computed cross-sections as one massless lattice field:
   the static photon of the Coulomb phase, read from layer units. No
   constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_2026_09_23.py`
- **Result:** `TOTAL: PASS=8 FAIL=0`, about 52 s, stdout 1331 characters,
  peak about 520 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_2026_09_23.txt`
- **Arithmetic:** exact integer row tensors; wavenumber sectors by the
  projector (1/ab) Σ_j e^(−i k·j) t^j; top levels by Lanczos iteration
  (tolerance 1e-10) on the projected operator. The field's rate is
  computed in closed form.

## Premises and declared objects

- **Layer units and the transfer matrix** (open PR 8740), zero-flux
  sector.
- **Row transfer** (open PR 8859).
- **Branch rate** D(k) = ln(λ_0 / |λ_top(k)|), with λ_0 the top level of
  the wavenumber-0 sector.
- **Comparison field:** the Z^3 graph Laplacian, a framework object, with
  the transfer rate stated above.

## Prior art and what is new

- Open PR 8740: the layer chain is exact on prisms.
- Open PRs 8746 and 8859: the Gaussian flux stiffness.
- Open PR 8864: the gap falls like 1/b and follows the smallest
  transverse wavenumber.
- New here: the complement symmetry of T; the resolution by wavenumber;
  the whole branch against the massless lattice field; the odd parity and
  negative levels of the branch states.

## Theorem — The branch on the computed cross-sections

On the cross-sections 2 × 8 and 4 × 4, in the zero-flux sector: T
commutes with the transverse translations and with the complement; the
branch rates are as tabulated and lie within the stated tolerances of the
massless nearest-neighbour lattice field; the vacuum is even with a
positive level; the computed branch states are odd with negative levels;
the stated degeneracies hold. No limit is claimed beyond the computed
cross-sections.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger cross-sections, such as 2 × 10 or
  6 × 6, are the direct extension; the square of side 6 is beyond this
  machine.
- **N2 wall independence.** The wavenumber-0 top is checked against the
  top of the full zero-flux sector, computed without the projector, and
  the lowest branch points against the gaps of open PR 8864.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance;
  every checked relation holds with margin.
- **N4 residual matching.** Nothing is fitted: the field's rate has no
  free constant, so every deviation in the table is a genuine residual.
- **N5 rhetoric audit.** "Has the dispersion of" means agreement within
  the stated percentages on the computed points, not identity.
- **N6 partial-closure paths.** Larger cross-sections; the branch in the
  nonzero flux sectors; the two-quantum continuum above the branch.
- **N7 steelman.** Against the reading: the square deviates by up to
  1.6%, and 2 × 8 is narrow. For it: nothing is fitted, the small-q slope
  is fixed by cubic symmetry, and the parity identifies the states.
  Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8740, 8746, 8859 and 8864 are cited.

## Falsifiers

- A computed branch point outside the stated tolerance of the field.
- A lowest branch point that differs from the gap of open PR 8864.
- A branch state even under the complement, or with a positive level.
- A failure of either commutation.

## Boundaries and non-claims

- The zero-flux sector of the cross-sections 2 × 8 and 4 × 4.
- No limit of large cross-sections is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms and open PRs 8740, 8746, 8859 and 8864 are cited; the
comparison field is the framework's Z^3 graph Laplacian. No audit grade,
no new axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the full-sector value of λ_0 on 2 × 8; the
  gaps of open PR 8864; the closed-form field rate; the parity read from
  the eigenvectors.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| two occupied links per vertex | ice rule changed | caught (5 FAILs) |
| horizontal degree without the left link | link dropped | caught (6 FAILs) |
| row swap in place of the row translation | translation broken | caught (7 FAILs) |
| strip read at occupation kx = 0 | wavenumber offset dropped | caught (3 FAILs) |
| field with half the stiffness | field changed | caught (3 FAILs) |
| projector phase conjugated | sectors read at −k | not caught (equivalent) |
| sector without the staggered sign | sign dropped | caught (4 FAILs) |
| parity read without the complement | parity changed | caught (1 FAIL) |
| row translation by two sites | projector broken | caught (6 FAILs) |
| wrap links not identified | wrap dropped | caught (5 FAILs) |
| torus not closed across the rows | trace replaced | caught (5 FAILs) |
| anisotropic field | field changed | caught (2 FAILs) |

  11 of 12 are caught. The conjugated projector reads each sector at −k.
  Reflection maps k to −k and commutes with T, so D(−k) = D(k) and the
  parities agree; the degeneracy checks confirm this directly. The mutant
  is therefore equivalent.

- **Vacuity guard:** every rate, its field value, the ratio and the
  parity range are printed.
- **Budget:** 8 checks, stdout 1331 characters (ceiling 6000), about 52 s
  (ceiling 900 s), peak about 520 MB.

## Verification

```bash
python3 scripts/uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=8 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_2026_09_23.txt`.
