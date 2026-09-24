---
claim_id: uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "On the square prism 4 x 4 of uniform ice, with the layer transfer of the landed layer-unit note (PR 8740) applied by the row transfer of the landed note of PR 8859, a test defect with five or one of its six links occupied (delta = +-2) carries charge +-4 of the staggered field, twice that of open PR 8875's defects. The charge-4 pair free energy depends only on the four-cube distance of the cross-section and is unchanged by the complement. Relative to the nearest pair, the charge-4 free-energy differences are 3.449, 3.577 and 3.623 times the charge-2 ones at distances 2, 3 and 4, rising toward the Gaussian factor 4. Along the prism, beyond the contact pair, the ratio of differences measured from z = 2 is 3.960 at z = 4 and 4.007 at z = 8. At z = 8 the charge-4 step equals the flux cost ln(lam_0 / lam_4) within 1%, and its ratio to the charge-2 step is 4.0361 against 4 c(4)/c(2) = 4.0362: the string ratio. Against the Gaussian K Q^2 Delta G with K = 2 c(2), the in-layer ratios are 0.9614, 0.9738, 0.9781 for charge 2 and 0.8290, 0.8708, 0.8860 for charge 4: the core correction grows with the charge. No limit beyond the computed cross-section is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_2026_09_24.py
---

# Uniform ice: test-defect pairs follow the charge-squared law, with a core correction that grows with the charge

**Date:** 2026-09-24
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8875 found that two test
defects of charge ±2 interact through the prism's lattice Green function at
the flux-cost stiffness, within 4% on the square 4 × 4. A Coulomb law also
fixes how the interaction scales with the charge: as Q². Its N6 path named
defects of charge 4. This block tests them.

## Result up front

1. **Charge-4 defects.** A vertex with five occupied links (δ = +2) or one
   (δ = −2) has divergence 2δ = ±4 in the staggered field: twice the charge
   of open PR 8875's defects. As before, the defects are probes, and nothing
   is admitted into the rule.

2. **Symmetry.** On 4 × 4 the charge-4 pair free energy depends only on
   the four-cube distance of the cross-section, and the complement leaves
   it unchanged.

3. **The charge-squared law in the layer.** Relative to the nearest pair,
   the charge-4 free-energy differences are 3.449, 3.577 and 3.623 times the
   charge-2 ones at distances 2, 3 and 4. They rise toward the Gaussian
   factor 4 as the pair separates.

4. **Along the prism.** Beyond the contact pair z = 1, whose charge-4 core
   is anomalous, the ratio of differences measured from z = 2 is 3.960 at
   z = 4 and 4.007 at z = 8. At z = 8 the charge-4 step V(z+1) − V(z)
   equals the flux cost ln(λ_0/λ_4) within 1%. Its ratio to the charge-2
   step is 4.0361, against 4 c(4)/c(2) = 4.0362. Far along the prism the
   pair is joined by a flux string, and the string's tension carries the
   non-Gaussian flux cost of open PR 8928. The ratio there is 4.04, not
   exactly 4.

5. **The core correction grows with the charge.** Against the Gaussian
   K Q² ΔG with K = 2c(2), the in-layer ratios are 0.9614, 0.9738 and
   0.9781 for charge 2, and 0.8290, 0.8708 and 0.8860 for charge 4.

6. **What this means.** The static Coulomb law of uniform ice scales with
   the square of the charge, as a Gaussian field requires. It does so
   exactly in the string along the prism, up to the flux cost's own
   stiffening, and approximately in the layer. There a charge-4 defect,
   which fills five of six links, has a stiffer core that takes 11% to 17%
   off the short-range differences, against 2% to 4% for charge 2. No
   constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_2026_09_24.py`
- **Result:** `TOTAL: PASS=4 FAIL=0`, about 30 s, stdout 978 characters,
  peak about 480 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_2026_09_24.txt`
- **Arithmetic:** exact integer row tensors including the defect rows; the
  vacuum and flux-sector tops by Lanczos iteration (tolerance 1e-12); the
  Green function in closed form.

## Premises and declared objects

- **Layer units and the transfer matrix:** the landed note of PR 8740;
  row transfer: the landed note of PR 8859.
- **Test defects:** vertices with δ = ±1 (charge ±2, open PR 8875) or
  δ = ±2 (charge ±4), probes only.
- **Comparison field:** the Gaussian divergence-free field with the Z^3
  graph Laplacian, as in open PR 8875.

## Prior art and what is new

- Open PR 8875: charge-2 pairs on prisms.
- Open PR 8928: the flux cost's stiffening, which sets the string ratio.
- New here: charge-4 pairs; the Q² law in the layer and along the prism;
  the string ratio 4 c(4)/c(2); the core correction's growth with charge.

## Theorem — Charge-4 pairs on the square prism

On the prism 4 × 4 the charge-4 and charge-2 pair free energies stand in
the stated ratios, and the string steps as stated. No limit is claimed
beyond the computed cross-section.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger cross-sections; charge 6, the
  largest at one vertex (all six links occupied, or none), is not computed
  here.
- **N2 wall independence.** The string step is checked against the
  flux-sector top, a separate computation.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance.
- **N4 residual matching.** Nothing is fitted.
- **N5 rhetoric audit.** "Follows the charge-squared law" means the stated
  ratios, exact for the string up to the flux cost and within 14% in the
  layer.
- **N6 partial-closure paths.** Mixed pairs, charge 2 against charge 4;
  the core free energy of one defect.
- **N7 steelman.** Against: the in-layer ratios fall short of 4 by 9% to
  14%. For: they rise with distance toward 4, and the string ratio is
  exact. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8875 and 8928 and the landed notes are
  cited.

## Falsifiers

- An in-layer ratio outside 3.4 to 3.7 at distances 2 to 4.
- A string step ratio departing from 4 c(4)/c(2) by more than 1%.

## Boundaries and non-claims

- The square prism 4 × 4.
- Test defects are probes; none is admitted into the rule.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, the landed notes of PRs 8740 and 8859, and open PRs
8875 and 8928 are cited. No audit grade, no new axiom, no new primitive, no
new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the flux-sector top for the string; the
  charge-2 pairs of open PR 8875.
- **Correction before landing.** A first version measured the prism ratio
  from the contact pair z = 1, whose charge-4 core is anomalous; the check
  now measures from z = 2.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| defect count clipped to one | charge 4 made charge 2 | caught (3 FAILs) |
| prediction linear in the charge | Q in place of Q² | caught (1 FAIL) |
| flux cost read at \|S\| = 2 | sector changed | caught (1 FAIL) |
| charge-4 cost normalised as charge 2 | normalisation changed | caught (1 FAIL) |
| charge sign not staggered | pair not neutral | caught (4 FAILs) |
| wrap links not identified | wrap dropped | caught (4 FAILs) |

  6 of 6 are caught.

- **Vacuity guard:** every ratio, step and cost is printed.
- **Budget:** 4 checks, stdout 978 characters (ceiling 6000), about 30 s
  (ceiling 900 s), peak about 480 MB.

## Verification

```bash
python3 scripts/uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_2026_09_24.txt`.
