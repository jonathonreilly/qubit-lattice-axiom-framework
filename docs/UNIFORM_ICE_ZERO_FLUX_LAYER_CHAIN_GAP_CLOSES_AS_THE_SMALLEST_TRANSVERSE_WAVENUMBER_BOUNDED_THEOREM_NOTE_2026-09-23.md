---
claim_id: uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "In the zero-flux sector the layer units of open PR 8740 form uniform ice as a Markov chain of layers whose transfer matrix is the layer transfer T. Its gap is D = ln(lam_0 / |lam_1|), with lam_1 the next eigenvalue in modulus within the sector. Computed with the row transfer of open PR 8859: on 2 x 2 the top eigenvalue is 32 + 2 sqrt(209) and the next modulus 14, and on 2 x 4 the next modulus is 668.3638, as in open PR 8740. On every cross-section the next level is negative (the staggered sign of the occupation form) and degenerate: twice on the strips 2 x b and four times on the square 4 x 4. On the strips, D b = 2.9408, 5.1158, 5.7060, 5.9434 and 6.0608 for b = 2 to 10, rising and staying below 2 pi = 6.2832, so on the computed strips the gap closes like 1/b and the chain's memory grows with the cross-section. The square 4 x 4 has the gap of the strip 2 x 4 within 2% (1.29627 against 1.27895): the gap follows the smallest transverse wavenumber 2 pi / 4, not the area. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.py
---

# Uniform ice: the zero-flux layer chain's gap closes as the smallest transverse wavenumber

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8740 formed uniform ice by
layer units on infinite prisms: in the zero-flux sector the law of a layer
depends only on the layer below. Open PRs 8746 and 8859 measured what the
flux sectors cost. This block asks how fast the layer chain forgets, and
how that changes with the cross-section.

## Result up front

1. **The chain's gap.** In the zero-flux sector the layers form a Markov
   chain whose transfer matrix is the layer transfer T. Its gap
   D = ln(λ_0 / |λ_1|) sets how fast a layer forgets the layers far below
   it. Here λ_1 is the next eigenvalue in modulus within the sector. The
   row transfer of open PR 8859 gives it without forming T. It reproduces
   open PR 8740:
   - on 2 × 2 the top eigenvalue is 32 + 2√209 and the next modulus is 14;
   - on 2 × 4 the next modulus is 668.3638.

2. **The next level.** On every cross-section the next level is negative
   and degenerate:
   - twice on the strips 2 × b;
   - four times on the square 4 × 4.

   The negative sign is the staggered sign of the occupation form, so the
   occupations' correlations alternate from layer to layer. The degeneracy
   pairs opposite transverse wavenumbers; on the square both transverse
   directions contribute.

3. **The gap closes like 1/b.** On the strips 2 × b:

   | b | D b |
   |---|---|
   | 2 | 2.9408 |
   | 4 | 5.1158 |
   | 6 | 5.7060 |
   | 8 | 5.9434 |
   | 10 | 6.0608 |

   D b rises and stays below 2π = 6.2832, so on the computed strips D
   closes like 1/b, and the chain's memory grows with the cross-section.

4. **The gap follows the smallest wavenumber.** The square 4 × 4 has the
   gap of the strip 2 × 4 within 2% (1.29627 against 1.27895). Both have
   smallest transverse wavenumber 2π/4, while their areas differ by a
   factor of two.

5. **What this means.** On the computed cross-sections the layer measure
   of uniform ice shows no gap that stays open: D falls like 1/b. The
   decay rate along the prism is set by the
   smallest transverse wavenumber, and D b approaches 2π from below: the
   decay rate approaches the wavenumber itself. With the flux stiffness of
   open PRs 8746 and 8859, the flux seen by layer units behaves like a
   gapless Gaussian field. This is the static side of the Coulomb phase,
   read from formation units. It bears on the open edge for layer units
   with an infinite cross-section: for every finite cross-section the
   chain is exact, but its memory is not bounded as the cross-section
   grows. No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.py`
- **Result:** `TOTAL: PASS=4 FAIL=0`, about 62 s, stdout 711 characters,
  peak about 600 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.txt`
- **Arithmetic:** exact integer row tensors; eigenvalues by dense
  diagonalisation for sectors of at most 400 states and by Lanczos
  iteration (tolerance 1e-11) above that.

## Premises and declared objects

- **Layer units and the transfer matrix** (open PR 8740), zero-flux
  sector.
- **Row transfer** (open PR 8859).
- **Gap** D = ln(λ_0 / |λ_1|) within the zero-flux sector.

## Prior art and what is new

- Open PR 8740: the chain is exact on prisms; on 2 × 2 and 2 × 4 its next
  modulus.
- Open PRs 8746 and 8859: the flux stiffness.
- New here: the gap on strips up to 2 × 10 and on the square; its 1/b
  closing; its dependence on the smallest transverse wavenumber; the
  degeneracies.

## Theorem — The gap on the computed cross-sections

For the cross-sections 2 × b (b = 2, 4, 6, 8, 10) and 4 × 4, the zero-flux
top eigenvalues, next levels and gaps are as stated. The degeneracies are
read from the computed spectra. The 1/b closing is the statement that D b
rises and stays below 2π on the computed strips. No limit is claimed beyond
the computed cross-sections.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger squares are beyond this frontier.
- **N2 wall independence.** The row transfer reproduces open PR 8740's
  exact values.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance;
  the checked relations hold with margin.
- **N4 residual matching.** The sign of the next level is the occupation
  form's staggered sign.
- **N5 rhetoric audit.** "Closes like 1/b" means D b is bounded and rising
  on the computed strips, so D falls like 1/b there.
- **N6 partial-closure paths.** Squares of side 6; the gap in the other
  flux sectors.
- **N7 steelman.** For a surviving gap: only b up to 10 is computed.
  Against: D b rises monotonically toward 2π. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8740, 8746 and 8859 are cited.

## Falsifiers

- A disagreement with open PR 8740's values on 2 × 2 or 2 × 4.
- A strip on which D b falls with b, or exceeds 2π.

## Boundaries and non-claims

- The zero-flux sector of the cross-sections computed.
- No limit of large cross-sections is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms and open PRs 8740, 8746 and 8859 are cited. No audit
grade, no new axiom, no new primitive, no new comparator and no new framing
is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the exact 2 × 2 spectrum of open PR 8740; the
  2 × 4 next modulus; the square against the strip.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| two occupied links per vertex | ice rule changed | caught (1 FAIL) |
| horizontal degree without the left link | link dropped | caught (4 FAILs) |
| torus not closed across the rows | trace replaced | caught (3 FAILs) |
| sector without the staggered sign | sign dropped | caught (4 FAILs) |
| levels ordered by value, not modulus | ordering changed | caught (4 FAILs) |
| large sectors read at the top values only | negative levels missed | caught (3 FAILs) |
| wrap links not identified | wrap dropped | caught (3 FAILs) |

  7 of 7 are caught.

- **Vacuity guard:** eigenvalues, degeneracies and gaps are printed.
- **Budget:** 4 checks, stdout 711 characters (ceiling 6000), about 62 s
  (ceiling 900 s), peak about 600 MB.

## Verification

```bash
python3 scripts/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.txt`.
