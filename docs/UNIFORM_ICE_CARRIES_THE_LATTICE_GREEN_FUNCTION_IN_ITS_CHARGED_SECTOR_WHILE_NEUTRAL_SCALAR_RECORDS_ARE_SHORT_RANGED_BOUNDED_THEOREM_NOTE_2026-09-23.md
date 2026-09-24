---
claim_id: uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The design note's record-dynamics seam (#8093) asks whether a Laplacian or transverse kernel appears in finished record statistics, and names the gravity node's input: a scalar record statistic whose two-point function equals the lattice Green function. For uniform ice: the six outward arrows at a vertex are permuted by the 48 signed axis permutations and by the 24 proper rotations, and the group average on them has rank 1, spanned by their sum, which is the divergence and vanishes in ice, so no neutral scalar is linear in the arrows at one vertex. The straight-through count f(r) = sum_i E_i(r) E_i(r - e_i), a neutral quadratic scalar, has <f> = 39/25 exactly on the L = 2 torus, reproduced by the worm sampler of open PR 8881. The lattice Green function on a 128^3 torus (zero mode removed; G(0) - G(e) = (1 - 1/N)/6 within 1e-12) has G(r)/G(1) = 0.491, 0.310, 0.224, 0.175, 0.143, 0.120, 0.103 for r = 2 to 8 along an axis. On L = 16 with 5 x 10^5 worms, the connected correlation of f is resolved at r = 1 (0.52% of its variance) and r = 2, with C(2)/C(1) = 0.072, below a third of G(2)/G(1); for r = 3 to 8 it is zero within 4 standard errors, and its 3-standard-error upper bound on C(r)/C(1) lies between 0.022 and 0.034, below G(r)/G(1) at every r. With open PRs 8875 and 8913, which find the Green function in the free energy of test defects of charge +-2, and open PRs 8881 and 8890, which find the transverse kernel in the arrow correlations: uniform ice carries the lattice Green function in its charged sector, not in the neutral scalar record measured here. No limit beyond the sampled sizes is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_2026_09_23.py
---

# Uniform ice carries the lattice Green function in its charged sector, while neutral scalar records are short-ranged

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. The derivation campaign's design
note (#8093) poses a record-dynamics seam: does a Laplacian or transverse
kernel appear in the finished record statistics of a formation law? Its
counterexample branch is that record-side correlators are short-ranged.
It names the gravity node's input: a scalar record statistic whose
two-point function equals the lattice Green function. This block answers
the seam for the uniform ice measure, whose photon the campaign has now
characterized.

## Result up front

1. **The transverse kernel appears.** The arrow correlations of uniform
   ice are the transverse projector over the sum-rule stiffness, with two
   degenerate polarizations, within 1% at every wavevector (open PRs 8881
   and 8890). That is the vector sector.

2. **The Green function appears in the charged sector.** Test defects,
   vertices of divergence ±2, have a pair free energy that follows
   K Q² (G(r′) − G(r)): on prisms within 4% (open PR 8875), and on tori out
   to r = 8 within about 3% (open PR 8913). Their two-point function is
   exp(K Q² G(r)) up to a constant, so its connected part tends to
   K Q² G(r) ∝ 1/r. These are charged insertions: a pair of like charges
   repels as a pair of opposite charges attracts.

3. **No neutral scalar is linear in the arrows at a vertex.** The six
   outward arrows at a vertex are permuted by the 48 signed axis
   permutations and by the 24 proper rotations. The group average on them
   has rank 1, spanned by their sum. That sum is the divergence, which is
   zero in ice. A neutral scalar built from the records at one vertex is
   therefore at least quadratic in the arrows.

4. **A neutral quadratic scalar is short-ranged.** The straight-through
   count f(r) = Σ_i E_i(r) E_i(r − e_i) records how many axes the arrows
   cross a vertex straight through. As a sampler control, ⟨f⟩ = 39/25
   exactly on the L = 2 torus, and the worm reproduces it. On L = 16 with
   5 × 10^5 worms, its connected correlation is:
   - 0.52% of its variance at r = 1, and resolved at r = 2, where
     C(2)/C(1) = 0.072;
   - zero within 4 standard errors for r = 3 to 8. The 3-standard-error
     upper bound on C(r)/C(1) lies between 0.022 and 0.034.

   The lattice Green function on a 128³ torus keeps
   G(r)/G(1) = 0.491, 0.310, 0.224, 0.175, 0.143, 0.120 and 0.103 for
   r = 2 to 8. At r = 2 the scalar has fallen seven times further, and
   beyond it lies below the Green function at every distance.

5. **What this means for the seam.** In the uniform ice measure the
   transverse kernel appears in the vector records, and the Laplacian's
   Green function appears in the charged sector: for test defects, which
   carry sign. The neutral scalar record measured here is short-ranged,
   which is the seam's counterexample branch for neutral scalars. In the
   Gaussian reading this holds generally: a neutral scalar at one vertex is
   at least quadratic in the arrows, so its correlation decays at least as
   the square of the dipolar one, and a linear scalar spread over
   neighbouring vertices needs at least three derivatives. So the gravity
   node's input is not supplied by the photon's neutral records, and a
   sign-definite 1/r statistic must come from elsewhere. This narrows where
   gravity's input can come from. It does not say that gravity has no
   route. No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_2026_09_23.py`
- **Result:** `TOTAL: PASS=4 FAIL=0`, about 128 s, stdout 984 characters,
  peak about 240 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_2026_09_23.txt`
- **Arithmetic:** exact group averages; exact enumeration and fractions on
  L = 2; the Green function by FFT; seeded sampling (numba's generator,
  fixed seeds) with standard errors from 20 bins.

## Premises and declared objects

- **The seam:** the design note's record-dynamics seam (#8093), as quoted
  in the landed note
  `ADMISSIBILITY_RULE_DIRECTED_GAUSSIAN_PROPAGATOR_OVERLAP_COVARIANCE_GAIN_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md`.
- **Uniform ice** as divergence-free arrows; the worm sampler of open PR
  8881.
- **Neutral scalar:** a record statistic invariant under the cubic group
  that carries no charge; f is the example measured.
- **Lattice Green function:** of the Z^3 graph Laplacian, as in the landed
  note
  `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`.

## Prior art and what is new

- Open PRs 8881 and 8890: the transverse kernel.
- Open PRs 8875 and 8913: the Green function for test defects.
- New here: the invariant lemma for the arrows at one vertex; the measured
  short range of a neutral scalar record; and the seam's answer for
  uniform ice, which places the Green function in the charged sector.

## Theorem — The seam for uniform ice

The group averages are exact. On L = 2 the control is exact. On L = 16 the
sampled correlation of f stands in the stated relation to the lattice
Green function. No limit is claimed beyond the sampled sizes. The general
statement for neutral scalars is the Gaussian reading's and is stated as
such.

## No-Go Discipline Gate

- **N1 alternative routes.** Other neutral scalars and larger tori; scalar
  statistics of other measures or of the formation process itself.
- **N2 wall independence.** The lemma is exact; the measurement and the
  Green function are separate computations.
- **N3 hidden walls.** Sampling error from binning; the correlation beyond
  r = 2 is below the noise, so only bounds are stated there.
- **N4 residual matching.** Nothing is fitted.
- **N5 rhetoric audit.** "Short-ranged" means the stated measurement for f
  and the Gaussian reading's decay for neutral scalars. The claim is about
  uniform ice's records, not about gravity's routes.
- **N6 partial-closure paths.** A sign-definite scalar with a 1/r
  two-point function in another sector; the formation law's own
  statistics.
- **N7 steelman.** Against: one neutral scalar is measured. For: the
  lemma removes all linear scalars at a vertex, and the Gaussian reading
  covers the rest. Both are recorded.
- **N8 cross-cycle echo.** The design note's seam, open PRs 8875, 8881,
  8890 and 8913, and the landed notes are cited.

## Falsifiers

- A neutral scalar record of uniform ice whose connected correlation
  follows the lattice Green function.
- An exact group average of rank above 1 on the six outward arrows.

## Boundaries and non-claims

- The uniform ice measure; the neutral scalar f; tori of side 2 (exact) and
  16 (sampled).
- It is not claimed that gravity has no route, only that this measure's
  neutral scalars do not carry the Green function.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, the design note's seam, open PRs 8875, 8881, 8890 and
8913, and the landed notes are cited. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the exact group averages; the exact L = 2
  control; the Green function computed separately.
- **Correction before landing.** A first version stated "no neutral scalar
  is linear in the records". The lemma covers the arrows at one vertex; a
  linear scalar spread over neighbouring vertices exists with three
  derivatives, and it is even shorter-ranged. The wording now says so.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| group average over the unsigned permutations only | group shrunk | caught (1 FAIL) |
| outward signs ignored | action changed | caught (1 FAIL) |
| massive kernel in place of the Green function | reference changed | caught (2 FAILs) |
| correlation without the mean removed | statistic changed | caught (1 FAIL) |
| vector component in place of the scalar | record changed | caught (1 FAIL) |
| biased step choice | worm made non-uniform | caught (2 FAILs) |

  6 of 6 are caught. The vector mutant replaces f by the arrow E_z, whose
  correlation is dipolar and does not pass the neutral-scalar check.
- **Vacuity guard:** the ranks, the exact mean, the Green ratios and every
  correlation bound are printed.
- **Budget:** 4 checks, stdout 984 characters (ceiling 6000), about 128 s
  (ceiling 900 s), peak about 240 MB.

## Verification

```bash
python3 scripts/uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_2026_09_23.txt`.
