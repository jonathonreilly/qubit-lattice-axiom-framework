---
claim_id: uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "A Gaussian divergence-free field with weight exp(-(K/2) sum E^2) on the links of the prism A x Z has flux cost c = K/2 per layer and equal-layer vertical correlation S_zz(q) = sqrt(Q/(Q+4)) / K, with Q = sum_i 2 (1 - cos q_i). Every link carries E = (-1)^(x+y) (2v - 1) = +-1, so <E_z^2> = 1 fixes K to K_A = (1/A) sum_q sqrt(Q/(Q+4)), with no free constant. For uniform ice on the cross-sections 2 x 2, 2 x 4, 2 x 6, 2 x 8, 2 x 10 and 4 x 4, computed with the row transfer of open PR 8859: the measured flux cost c(2) reproduces open PR 8859 and lies within 1% of K_A/2 on every shape (+0.71% on 2 x 2, -0.37% to -0.40% on the strips 2 x 4 to 2 x 10, -0.02% on the square 4 x 4). With K = 2 c(2) taken from the flux cost, the measured equal-layer correlation of the zero-flux vacuum satisfies K S_zz(q) = sqrt(Q/(Q+4)) within 0.64% at every nonzero wavenumber on the square, within 5% on the strips 2 x 4 to 2 x 10 (largest at q = (pi, 0), across the width of 2), and within 10% on 2 x 2. The transverse projector of a divergence-free field on Z^3 has trace 2 at every nonzero wavevector, so by cubic symmetry the zone average of sqrt(Q/(Q+4)) is 2/3; on large cross-sections the Gaussian reading therefore gives K = 2/3 and c = 1/3. Every measured cost lies below 1/3, and the square's is within 2% of it. No limit beyond the computed cross-sections is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_2026_09_23.py
---

# Uniform ice: the unit field on every link fixes one stiffness for the flux cost and the field's correlations

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PRs 8746 and 8859 measured
the cost of a flux sector per layer of uniform ice and found it nearly
Gaussian. Open PR 8864 found the zero-flux layer chain gapless, and open
PR 8869 found its branch to be that of the massless nearest-neighbour
lattice field. The dispersion does not depend on the field's stiffness.
This block asks what sets the stiffness.

## Result up front

1. **What a Gaussian field predicts.** Take a divergence-free field with
   weight exp(−(K/2) Σ E²) on the links of the prism A × Z, where A is the
   periodic cross-section.
   - **Flux cost.** A flux S through every layer splits off as a uniform
     part, so it costs K S²/(2A) per layer: c = K/2.
   - **Correlations.** The equal-layer correlation of the vertical field
     at transverse wavenumber q is S_zz(q) = √(Q/(Q + 4)) / K, with
     Q = Σ_i 2(1 − cos q_i). This comes from the transverse projector
     1 − |s_z|²/|s|² integrated over k_z.

2. **The unit link field fixes the stiffness.** Every link is occupied or
   empty, so the field E = (−1)^(x+y) (2v − 1) is ±1 on every link and
   ⟨E_z²⟩ = 1 exactly. The rule "three of six links occupied" makes the
   field divergence-free, which gives the projector above. For the Gaussian
   field this is the sum rule (1/A) Σ_q S_zz(q) = 1. It fixes

   K_A = (1/A) Σ_q √(Q/(Q + 4)),

   with no free constant.

3. **The flux cost is that stiffness.** The measured flux cost c(2)
   reproduces open PR 8859 and lies within 1% of K_A/2 on every
   cross-section:

   | cross-section | c(2) measured | K_A/2 | deviation |
   |---|---|---|---|
   | 2 × 2 | 0.28082 | 0.27884 | +0.71% |
   | 2 × 4 | 0.30726 | 0.30841 | −0.37% |
   | 2 × 6 | 0.31210 | 0.31336 | −0.40% |
   | 2 × 8 | 0.31374 | 0.31501 | −0.40% |
   | 2 × 10 | 0.31451 | 0.31576 | −0.40% |
   | 4 × 4 | 0.32704 | 0.32709 | −0.02% |

   The prediction follows the shape dependence, from the smallest strip to
   the square.

4. **The same stiffness sets the correlations.** With K = 2 c(2) taken
   from the flux cost, the measured equal-layer correlation of the
   zero-flux vacuum satisfies K S_zz(q) = √(Q/(Q + 4)):
   - within 0.64% at every nonzero wavenumber on the square 4 × 4;
   - within 5% on the strips 2 × 4 to 2 × 10 (4.1% to 4.7%). The largest
     deviation sits at q = (π, 0), the wavenumber that alternates across
     the width of 2.
   - within 10% on 2 × 2 (9.0%).

   The flux cost comes from the top level of the |S| = 2 sector. The
   correlations come from the zero-flux vacuum vector. They are two
   separate observables of the layer measure, and they carry the same
   constant.

5. **The large-section value.** The transverse projector of a
   divergence-free field on Z^3 has trace 2 at every nonzero wavevector.
   Cubic symmetry shares it equally among the three directions, so the
   zone average of √(Q/(Q + 4)) is exactly 2/3. On large cross-sections
   the Gaussian reading therefore gives K = 2/3 and c = 1/3. Every
   measured cost lies below 1/3, and the square's, 0.32704, is within 2%
   of it.

6. **What this means.** The static photon of uniform ice has no free
   coupling. The field is ±1 on every link, and the three-of-six rule makes
   it divergence-free; together they fix the stiffness through the sum
   rule. That one
   constant then sets both the cost of flux and the equal-layer
   correlations: on the square within 0.02% and 0.64%. With the massless
   dispersion of open PR 8869, the flux seen by formation units behaves
   on the square cross-section as one Gaussian lattice field whose shape
   and normalisation both come from uniform ice itself. The width-2 strips show the
   lattice scale: there the correlation across the width deviates by up to
   4.7%. No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_2026_09_23.py`
- **Result:** `TOTAL: PASS=7 FAIL=0`, about 28 s, stdout 1285 characters,
  peak about 840 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_2026_09_23.txt`
- **Arithmetic:** exact integer row tensors; top levels by dense
  diagonalisation up to 4096 states and by Lanczos iteration (tolerance
  1e-11) above that; the Gaussian quantities in closed form. The k_z
  integral and the zone average are checked numerically.

## Premises and declared objects

- **Layer units and the transfer matrix** (open PR 8740).
- **Row transfer** (open PR 8859). T maps the flux S between consecutive
  layers to −S, so flux sectors are |S| = s.
- **Flux cost** c(2) = (A/4) ln(λ_0/λ_2), as in open PRs 8746 and 8859.
- **Equal-layer correlation** S_zz(q) = (1/A) ⟨|Σ_r e^(−iq·r) E_r|²⟩ in
  the zero-flux vacuum, whose layer law is ψ_0² for the top vector ψ_0 of
  the symmetric T.
- **Comparison field:** the Gaussian divergence-free field on Z^3, whose
  projector is built from the graph Laplacian of the landed note
  `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`.

## Prior art and what is new

- Open PRs 8746 and 8859: the flux cost and its near-Gaussian form.
- Open PRs 8864 and 8869: the gapless chain and its massless branch.
- New here: the sum-rule stiffness K_A; the flux cost as K_A/2 on every
  computed shape; the correlations with the same constant; the value
  K = 2/3 from the projector trace.

## Theorem — One stiffness on the computed cross-sections

On the cross-sections 2 × 2, 2 × 4, 2 × 6, 2 × 8, 2 × 10 and 4 × 4, the
measured flux costs and equal-layer correlations stand in the stated
relations to the Gaussian field whose stiffness is fixed by ⟨E_z²⟩ = 1.
The projector trace and the zone average 2/3 are exact. No limit is
claimed beyond the computed cross-sections.

## No-Go Discipline Gate

- **N1 alternative routes.** Squares of side 6 are the direct extension
  and are beyond this machine.
- **N2 wall independence.** The flux costs reproduce open PR 8859. The
  flux cost and the correlations are separate observables.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance;
  every checked relation holds with margin.
- **N4 residual matching.** Nothing is fitted: K_A comes from the sum
  rule, and the correlation test uses K from the flux cost.
- **N5 rhetoric audit.** "Fixes one stiffness" means the stated
  agreements on the computed shapes, not an identity. The value 1/3 is
  the Gaussian reading's large-section value, not a measured limit.
- **N6 partial-closure paths.** Larger squares; the cost at larger |S|,
  where open PR 8859 found departures from the Gaussian of up to 5%.
- **N7 steelman.** Against the reading: the strips deviate by up to 4.7%
  and 2 × 2 by 9%. For it: the square agrees within 0.64% at every
  wavenumber, and the flux cost follows K_A/2 across all six shapes.
  Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8740, 8746, 8859, 8864 and 8869 are
  cited.

## Falsifiers

- A cross-section on which c(2) departs from K_A/2 by more than 1%.
- A wavenumber on the square at which K S_zz(q) departs from √(Q/(Q + 4))
  by more than 1%.

## Boundaries and non-claims

- The computed cross-sections; the flux cost at |S| = 2.
- No limit of large cross-sections is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms and open PRs 8740, 8746, 8859, 8864 and 8869 are
cited; the comparison field is built from the framework's Z^3 graph
Laplacian. No audit grade, no new axiom, no new primitive, no new
comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the flux costs of open PR 8859; the flux cost
  and the correlations as separate observables; the closed-form Gaussian
  quantities.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| two occupied links per vertex | ice rule changed | caught (5 FAILs) |
| field without the staggered sign | sign dropped | caught (5 FAILs) |
| flux sector S = s in place of \|S\| = s | sector changed | caught (nonzero exit) |
| Gaussian weight without the k_z integral | weight changed | caught (3 FAILs) |
| flux cost read as the full stiffness | factor 2 dropped | caught (2 FAILs) |
| vacuum measure ψ in place of ψ² | layer law changed | caught (2 FAILs) |
| wavenumber grid shifted by half a step | grid changed | caught (4 FAILs) |
| projector trace over two directions | trace changed | caught (1 FAIL) |
| cost read from the \|S\| = 4 sector | sector changed | caught (5 FAILs) |
| wrap links not identified | wrap dropped | caught (5 FAILs) |

  10 of 10 are caught.

- **Vacuity guard:** every cost, its prediction, the largest correlation
  deviations with their wavenumbers, and the zone average are printed.
- **Budget:** 7 checks, stdout 1285 characters (ceiling 6000), about 28 s
  (ceiling 900 s), peak about 840 MB.

## Verification

```bash
python3 scripts/uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_2026_09_23.txt`.
