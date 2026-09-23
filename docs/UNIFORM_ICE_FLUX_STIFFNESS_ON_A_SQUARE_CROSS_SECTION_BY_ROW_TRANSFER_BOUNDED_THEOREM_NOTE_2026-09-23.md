---
claim_id: uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The layer transfer matrix of uniform ice on an a x b transverse torus (open PRs 8740, 8746) is applied row by row: a row of a vertices, its a horizontal links summed out, maps (the row's w bits, the links in from the previous row) to (the row's v bits, the links out to the next row), with a frontier of 2a link bits, so the matrix is never formed. This reproduces open PR 8746 (trace T^2 = 9600 on 2 x 2; the zero-flux and |S| = 2 top eigenvalues on 2 x 2, 2 x 4 and 2 x 6), and the transfer is symmetric. On the square 4 x 4 cross-section (area A = 16), the top eigenvalue falls with the staggered flux across |S| = 0, 2, 4, 6, 8 (3244639.0, 2989915.0, 2332665.4, 1526346.9, 822834.3). The coefficient c(S) = (A / S^2) ln(lam_0 / lam_S) is 0.3270, 0.3300, 0.3352 and 0.3430, within 3% of its value at |S| = 2 up to |S| = 6: a Gaussian flux stiffness on a square cross-section. At equal area the strip 2 x 8 has c = 0.3137 at |S| = 2, about 4% below the square. The strips 2 x b, b = 2 to 10, give c = 0.2808, 0.3073, 0.3121, 0.3137 and 0.3145, rising and levelling. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.py
---

# Uniform ice flux stiffness on a square cross-section, by row transfer

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8740 formed uniform ice
by layer units on infinite prisms in the zero-flux sector. Open PR 8746
found that the flux sectors of the layer transfer matrix carry a Gaussian
stiffness on cross-sections of width 2, and left square cross-sections
open. This block reaches the square 4 × 4 cross-section.

## Result up front

1. **Row transfer.** The layer transfer matrix T maps the vertical links
   below a layer (v) to those above it (w). On an a × b transverse torus it
   is applied one row at a time. A row of a vertices, with its a
   horizontal links summed out, maps the row's w bits and the links coming
   in from the previous row to the row's v bits and the links going out to
   the next row. The frontier is 2a link bits, so on 4 × 4 the matrix, with
   2^16 rows, is never formed. The method reproduces open PR 8746 on
   2 × 2, 2 × 4 and 2 × 6, including trace T² = 9600, and the transfer is
   symmetric.

2. **A square cross-section.** On 4 × 4 (area 16) the top eigenvalue falls
   with the staggered flux |S| = 0, 2, 4, 6, 8. The free energy of flux S
   per layer, f(S) = ln(λ_0 / λ_S), gives:

   | \|S\| | c(S) = f(S) A / S² |
   |---|---|
   | 2 | 0.3270 |
   | 4 | 0.3300 |
   | 6 | 0.3352 |
   | 8 | 0.3430 |

   So f(S) ≈ c S² / A with c near 0.33, within 3% up to |S| = 6: the
   Gaussian flux stiffness holds on a square cross-section as it does on
   strips.

3. **Shape at equal area.** The strip 2 × 8 has c = 0.3137 at |S| = 2,
   about 4% below the square's 0.3270 at the same area.

4. **Strips level off.** For the strips 2 × b, c at |S| = 2 is 0.2808,
   0.3073, 0.3121, 0.3137 and 0.3145 for b = 2 to 10: rising, with the last
   step under 0.002.

5. **What this means.** The flux sectors seen by layer units carry one
   Gaussian stiffness on both cross-section shapes, with a coefficient of
   about 0.31 to 0.33 per layer at these sizes. That is the free-energy cost
   of a uniform field in a Coulomb phase. The square sits a few percent
   above the strip at equal area; which value large cross-sections
   approach is not decided here. No constant is compared with an outside
   value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.py`
- **Result:** `TOTAL: PASS=5 FAIL=0`, about 48 s, stdout 816 characters,
  peak about 570 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.txt`
- **Arithmetic:** the row tensor is an exact integer count. Sector top
  eigenvalues come from dense diagonalisation for sectors of at most 400
  states and from Lanczos iteration (tolerance 1e-12) above that.

## Premises and declared objects

- **Layer units and the transfer matrix** (open PR 8740): uniform ice in
  occupation form, three occupied links at every vertex.
- **Staggered flux** S = Σ (−1)^(x+y) (2v − 1), conserved in magnitude by
  the transfer (open PR 8740).
- **Stiffness coefficient** c(S) (open PR 8746).

## Prior art and what is new

- Open PR 8740: the transfer matrix and the zero-flux sector.
- Open PR 8746: the Gaussian stiffness on cross-sections of width 2.
- New here: the row transfer; the square 4 × 4 cross-section; the strip
  2 × 8 at equal area; the strip 2 × 10.

## Theorem — Row transfer

On a layer, a vertex has four in-plane links and two vertical ones, and the
ice rule asks for three occupied links. Order the vertices by rows. The
in-plane links split into horizontal links inside a row and links between
consecutive rows. For fixed links between rows, the horizontal links of
different rows are independent, so the count factorises into one row
tensor per row. It is summed over the between-row links, with the last row
wrapping to the first. The runner's contraction follows exactly this
factorisation, and the checks against open PR 8746 confirm it.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger squares are beyond this frontier.
- **N2 wall independence.** The row transfer is checked against the
  degree-count transfer of open PR 8746.
- **N3 hidden walls.** Floating-point eigenvalues; the tolerance is
  stated, and all checked relations hold with wide margins.
- **N4 residual matching.** The residual is shape dependence at a few
  percent.
- **N5 rhetoric audit.** "Gaussian" means c(S) nearly constant over the
  listed sectors.
- **N6 partial-closure paths.** Squares of side 6 and more; the approach
  to large cross-sections.
- **N7 steelman.** For shape independence: both shapes are Gaussian with
  close coefficients. Against: 4% apart at area 16. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8740 and 8746 are cited.

## Falsifiers

- A disagreement with open PR 8746 on the width-2 cross-sections.
- A square-sector top eigenvalue that rises with |S|.

## Boundaries and non-claims

- Cross-sections 2 × 2 to 2 × 10 and 4 × 4.
- No limit of large cross-sections is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms and open PRs 8740 and 8746 are cited. No audit grade, no
new axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the row transfer against the degree count of
  open PR 8746; trace T² against the landed torus count; symmetry.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| two occupied links per vertex | ice rule changed | caught (4 FAILs) |
| horizontal degree without the left link | link dropped | caught (5 FAILs) |
| torus not closed across the rows | trace replaced | caught (5 FAILs) |
| flux without the staggered sign | sign dropped | caught (5 FAILs) |
| small sectors read at the bottom | smallest eigenvalue | caught (2 FAILs) |
| large sectors read at the bottom | smallest eigenvalue | caught (5 FAILs) |
| area taken as a + b | area changed | caught (3 FAILs) |
| wrap links not identified | wrap dropped | caught (5 FAILs) |

  8 of 8 are caught.

- **Vacuity guard:** eigenvalues and coefficients are printed.
- **Budget:** 5 checks, stdout 816 characters (ceiling 6000), about 48 s
  (ceiling 900 s), peak about 570 MB.

## Verification

```bash
python3 scripts/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=5 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.txt`.
