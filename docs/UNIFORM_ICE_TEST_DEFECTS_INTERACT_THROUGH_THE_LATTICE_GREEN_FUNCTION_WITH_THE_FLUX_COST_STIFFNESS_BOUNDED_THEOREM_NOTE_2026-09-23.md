---
claim_id: uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "In uniform ice three of the six links at every vertex are occupied, so the staggered link field E = (-1)^(x+y+z) (2v - 1) is divergence-free. A test defect is one vertex with four (delta = +1) or two (delta = -1) occupied links; it carries charge 2 delta (-1)^(x+y+z). Two opposite test defects probe the layer measure, and nothing is admitted into the rule. Their free energy V = -ln(Z_pair / Z_0) in the infinite prism A x Z is computed by layer transfer, on the square 4 x 4 and the strip 2 x 8. It is compared with the Gaussian divergence-free field, V(r) - V(r') = K Q^2 (G_A(r') - G_A(r)), where G_A is the Green's function of the Z^3 graph Laplacian on the prism, Q = 2, and K = 2 c(2) comes from the flux cost, so nothing is fitted. On 4 x 4 the pair free energy depends only on the distance in the cross-section graph, which is the four-cube (V = 0.46195, 0.53561, 0.56358, 0.57797 at distances 1 to 4). Swapping the defect types leaves V unchanged on both shapes. The pair attracts. Relative to the nearest in-layer pair, the ratio of measured to predicted differences is 0.9614, 0.9738 and 0.9781 in the layer of the square (within 4%, and within 1% beyond distance 2), 0.967 to 0.995 along the prism of the square for z = 1 to 9, 0.981 to 0.993 along the strip's length and 0.973 to 0.995 along its prism (within 3%), and 0.9252 and 1.0563 across the strip's width of 2 (within 8%). At z = 8 the step V(z+1) - V(z) agrees with the Gaussian's within 0.1% on both shapes and with the flux cost ln(lam_0 / lam_2) within 1%. No limit beyond the computed cross-sections is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_2026_09_23.py
---

# Uniform ice: test defects interact through the lattice Green's function with the flux-cost stiffness

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8869 found that the
zero-flux layer chain of uniform ice carries the branch of a massless
nearest-neighbour lattice field. Open PR 8871 found that one stiffness,
fixed by the unit field on every link, sets both the flux cost and the
correlations. A field of this kind should have sources. This block puts two
test sources into the layer measure and measures how they interact.

## Result up front

1. **Test defects are charges.** Uniform ice occupies three of the six
   links at every vertex, so the staggered field
   E = (−1)^(x+y+z) (2v − 1) is divergence-free. A test defect is one
   vertex with four occupied links (δ = +1) or two (δ = −1). Its
   divergence is 2δ(−1)^(x+y+z), so it carries charge ±2. Two opposite
   defects form a probe of the layer measure. Nothing is admitted into the
   rule, which stays three of six everywhere else.

2. **Free energy by layer transfer.** The pair's free energy in the
   infinite prism A × Z is V = −ln(Z_pair/Z_0). With both defects in one
   layer, Z_pair/Z_0 = ⟨ψ_0|T_D|ψ_0⟩/λ_0, where T_D uses the changed vertex
   count at the defects. With the defects z layers apart, the flux between
   them is |S| = 2, and the transfer runs through that sector. T is the
   layer transfer of the landed layer-unit note (PR 8740), applied by the
   row transfer of open PR 8859.

3. **The Gaussian prediction has no free constant.** A Gaussian
   divergence-free field with stiffness K gives
   V(r) − V(r′) = K Q² (G_A(r′) − G_A(r)) for charges ±Q, where G_A is the
   Green's function of the Z^3 graph Laplacian on the prism:

   G_A(r, z) − G_A(0, 0) = (1/A) [ −|z|/2 + Σ_{q≠0} (cos(q·r) e^(−D|z|) − 1)/(2 sinh D) ],

   with cosh D = 1 + Σ_i (1 − cos q_i). The runner takes Q = 2 and
   K = 2 c(2) from the flux cost c(2) = (A/4) ln(λ_0/λ_2), as in open PR
   8871.

4. **Symmetry.** The cross-section 4 × 4 is the four-cube as a graph, so
   the pair free energy on it depends only on graph distance:
   V = 0.46195, 0.53561, 0.56358, 0.57797 at distances 1 to 4. Both ice
   and the Gaussian respect this. Swapping the defect types, which is the
   complement, leaves V unchanged on both shapes.

5. **The measured interaction.** Ratios of the measured difference
   V(r) − V(0,1) to the Gaussian's, with nothing fitted:

   | shape | pairs | ratios | agreement |
   |---|---|---|---|
   | 4 × 4 | in the layer, distances 2, 3, 4 | 0.9614, 0.9738, 0.9781 | within 4% |
   | 4 × 4 | in the layer, from distance 2 | 1.0080, 1.0085 | within 1% |
   | 4 × 4 | along the prism, z = 1 to 9 | 0.967 to 0.995 | within 4% |
   | 2 × 8 | along the length | 0.981 to 0.993 | within 3% |
   | 2 × 8 | along the prism, z = 1 to 9 | 0.973 to 0.995 | within 3% |
   | 2 × 8 | across the width of 2 | 0.9252, 1.0563 | within 8% |

   The pair attracts: V rises with distance.

6. **The string.** On a finite cross-section the field lines between
   defects far apart along the prism cannot spread, so V grows linearly.
   At z = 8 the step V(z+1) − V(z) is 0.08176 on 4 × 4 and 0.07869 on
   2 × 8. It agrees with the Gaussian's step within 0.1%, and with the flux
   cost ln(λ_0/λ_2) (0.08176 and 0.07844) within 1%. The tension is the
   flux cost, K Q²/(2A), which falls as the cross-section grows.

7. **What this means.** The static field of uniform ice has sources, and
   they interact as the field's own Green's function says, with the
   stiffness already fixed by the flux cost. On the square cross-section
   the pair free energy follows the lattice Green's function within 4% at
   every separation, and within 1% beyond distance 2. That is the static
   Coulomb interaction of the Coulomb phase, read from layer units, with
   charge 2 and no free coupling. The width-2 direction of the strip shows
   the lattice scale again, as in open PR 8871. On large cross-sections the
   Gaussian reading gives the potential −K Q²/(4πr) with K = 2/3, so
   −2/(3πr). That is a reading, not a computed limit. No constant is
   compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_2026_09_23.py`
- **Result:** `TOTAL: PASS=7 FAIL=0`, about 24 s, stdout 1209 characters,
  peak about 500 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_2026_09_23.txt`
- **Arithmetic:** exact integer row tensors, including the defect rows;
  the vacuum and flux-sector tops by Lanczos iteration (tolerance 1e-12);
  the Green's function in closed form over the finite set of transverse
  wavenumbers.

## Premises and declared objects

- **Layer units and the transfer matrix:** the landed note
  `UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md`
  (PR 8740).
- **Flux sectors:** the landed note
  `UNIFORM_ICE_LAYER_TRANSFER_FLUX_SECTORS_CARRY_A_GAUSSIAN_STIFFNESS_INVERSE_IN_THE_CROSS_SECTION_BOUNDED_THEOREM_NOTE_2026-09-23.md`
  (PR 8746). T maps the flux S of one layer to −S, so a sector is
  |S| = s.
- **Row transfer:** open PR 8859.
- **Test defect:** one vertex with four or two occupied links, a probe
  only.
- **Comparison field:** the Gaussian divergence-free field, with the Z^3
  graph Laplacian of the landed note
  `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`.

## Prior art and what is new

- The landed notes of PRs 8740 and 8746: layer units and flux sectors.
- Open PRs 8859, 8864, 8869 and 8871: the row transfer, the gapless
  chain, the massless branch and the one stiffness.
- New here: test defects as charges 2; their pair free energy by layer
  transfer; its agreement with the prism's lattice Green's function at the
  flux-cost stiffness; the four-cube symmetry of the 4 × 4 section; the
  string tension as the flux cost.

## Theorem — Test defects on the computed cross-sections

On the cross-sections 4 × 4 and 2 × 8, the pair free energies of two
opposite test defects satisfy the stated symmetries and stand in the stated
ratios to the Gaussian prediction with Q = 2 and K = 2 c(2). No limit is
claimed beyond the computed cross-sections.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger squares are the direct extension and
  are beyond this machine.
- **N2 wall independence.** K comes from the flux sector's top level. V
  comes from the vacuum vector and the defect layers, so they are separate
  computations.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance;
  every checked relation holds with margin.
- **N4 residual matching.** Nothing is fitted; the ratios are genuine
  residuals.
- **N5 rhetoric audit.** "Interact through the lattice Green's function"
  means the stated ratios on the computed shapes. The 1/r form is the
  Gaussian reading on large cross-sections, not a computed limit.
- **N6 partial-closure paths.** Larger squares; defects of charge 4; the
  core free energy of one defect.
- **N7 steelman.** Against the reading: the nearest pairs deviate by up to
  4% on the square and 8% across the strip's width. For it: nothing is
  fitted, and beyond distance 2 the square agrees within 1%. Both are
  recorded.
- **N8 cross-cycle echo.** The landed notes of PRs 8740 and 8746 and open
  PRs 8859, 8864, 8869 and 8871 are cited.

## Falsifiers

- A pair on the square whose ratio departs from 1 by more than 4%.
- A step at z = 8 that departs from the flux cost by more than 1%.
- A failure of the four-cube or complement symmetry.

## Boundaries and non-claims

- The cross-sections 4 × 4 and 2 × 8, and separations up to 9 layers.
- Test defects are a probe; no defect is admitted into the rule.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, the landed notes of PRs 8740 and 8746, and open PRs
8859, 8864, 8869 and 8871 are cited; the comparison field is built from
the framework's Z^3 graph Laplacian. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the flux-sector top level for K; the vacuum
  and defect layers for V; the closed-form Green's function.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| defect vertex count ignored | defects removed | caught (5 FAILs) |
| defects of equal charge | pair not neutral | caught (7 FAILs) |
| charge 1 in place of 2 | charge changed | caught (5 FAILs) |
| stiffness read as c in place of 2c | factor 2 dropped | caught (5 FAILs) |
| Green's function without the zero mode | string dropped | caught (3 FAILs) |
| continuum rate in place of the lattice rate | rate changed | caught (4 FAILs) |
| Green's function missing the factor 1/2 | normalisation changed | caught (5 FAILs) |
| flux without the staggered sign | sectors changed | caught (5 FAILs) |
| charge sign not staggered along the prism | pair not neutral at odd z | caught (3 FAILs) |
| wrap links not identified | wrap dropped | caught (6 FAILs) |
| one extra layer between the defects | transfer count changed | caught (3 FAILs) |
| two occupied links per vertex | rule changed | caught (6 FAILs) |

  12 of 12 are caught.

- **Vacuity guard:** the free energies, every ratio, the steps and K are
  printed.
- **Budget:** 7 checks, stdout 1209 characters (ceiling 6000), about 24 s
  (ceiling 900 s), peak about 500 MB.

## Verification

```bash
python3 scripts/uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_2026_09_23.txt`.
