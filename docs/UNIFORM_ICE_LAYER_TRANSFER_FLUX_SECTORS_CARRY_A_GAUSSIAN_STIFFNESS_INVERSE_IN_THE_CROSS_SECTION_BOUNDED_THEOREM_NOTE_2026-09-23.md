---
claim_id: uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The layer transfer matrix of the uniform ice measure (3 of each vertex's 6 links occupied) on prisms of cross-section 2 x 2, 2 x 4 and 2 x 6 (areas A = 4, 8, 12), as in open PR 8740, built from exact integer counts of in-plane configurations with prescribed degrees. The counts are checked: trace T^2 = 9600 on 2 x 2 (the landed torus), and the tori 2 x 2 x 4 and 2 x 2 x 6 (70121226240 ice states) agree with transfers along another axis. Every cross-section conserves the size of the staggered vertical flux S, and zero flux carries the largest eigenvalue. With lambda_S the largest eigenvalue modulus in the sector |S| and f(S) = -ln(lambda_S / lambda_0) the free energy of flux S per layer, f(S) A / S^2 lies between 0.28 and 0.41 over every flux sector of the three cross-sections; at the smallest flux, |S| = 2, it is 0.2808, 0.3073 and 0.3121 at A = 4, 8, 12, with shrinking steps, and at each A it rises with the flux. So the flux sectors cost close to c S^2 / A per layer with one c near 0.31, with corrections that grow with the flux density: a Gaussian flux stiffness, as in a Coulomb phase. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
runner: scripts/uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_2026_09_23.py
---

# Uniform ice seen by layer units: the flux sectors carry a Gaussian stiffness inverse in the cross-section

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8740 formed the uniform ice measure
on infinite prisms layer by layer. The layer transfer matrix conserves the
staggered vertical flux, and long prisms select zero flux. This block
compares the flux sectors across three cross-sections, to see how the
free energy of a flux depends on its size and on the area it spreads
over.

## Result up front

1. **The counts are checked.** On 2 × 2, trace T² = 9600, the landed
   torus. The tori 2 × 2 × 4 and 2 × 2 × 6 (70121226240 ice states) agree
   with transfers along another axis.

2. **Every cross-section conserves the flux, and zero flux leads.** On
   2 × 2, 2 × 4 and 2 × 6, the size of the staggered vertical flux is
   conserved from layer to layer. Zero flux carries the largest
   eigenvalue.

3. **The flux costs close to c S²/A per layer.** Write the free energy of
   flux S per layer as f(S) = −ln(λ_S / λ_0). Then:
   - f(S) A / S² lies between 0.28 and 0.41 over every flux sector of
     the three cross-sections;
   - at the smallest flux, |S| = 2, it takes the values 0.2808, 0.3073
     and 0.3121 at A = 4, 8 and 12, with shrinking steps;
   - at each A it rises slowly with the flux, so the corrections grow
     with the flux density.

4. **What this means.** The flux sectors seen by layer units carry one
   Gaussian stiffness, near 0.31 per unit of S²/A per layer. That is the
   free-energy cost of a uniform field in a Coulomb phase. The landed
   cubic-ice note computes the Coulomb correlations of the same measure.
   This block sees the same phase through the transfer matrix of the
   formation units of open PR 8740. No constant is compared with an
   outside value.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "how the flux sectors of the layer transfer matrix of open PR 8740 depend on the flux and on the cross-section"
source_of_blocker_text: open_pr_8740
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the photon branch: layer units see a Gaussian flux stiffness near 0.31 per S^2 / A per layer"
conditional_surface_status: "uniform ice measure on 2 x b transverse tori (b = 2, 4, 6) times Z; layer transfer matrices"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact integer transfer matrices and traces; sector eigenvalues in floating point"
```

## Premises and declared objects

- **Measure and units.** The uniform ice measure, and the layer units and
  transfer matrix of open PR 8740.
- **Cross-sections.** The tori 2 × 2, 2 × 4 and 2 × 6, with areas 4, 8
  and 12.
- **Counts.** In-plane configurations are counted by their degree
  vectors, exactly, in chunks.
- **Flux.** S(v) = Σ (−1)^(x+y) (2v − 1) over the cross-section.

## Prior art and what is new

- Open PR 8740: the layer transfer matrix, flux conservation and
  zero-flux selection on 2 × 2 and 2 × 4.
- The landed cubic-ice note: Coulomb correlations of the uniform measure.
- New here:
  - the 2 × 6 cross-section;
  - the free energies of all flux sectors;
  - their approach to a common c S²/A.

## Theorem — Flux free energies

The runner computes λ_S for every sector of the three cross-sections,
and reports f(S) A / S² for each. The two bounds and the monotone
approach at the smallest flux are the checked statements. The Gaussian
reading, f(S) ≈ c S²/A, is the pattern they show.

## No-Go Discipline Gate

There is no negative content. The claim is scoped to the declared
cross-sections.

- **N1 alternative routes.** Wider cross-sections in both directions are
  not computed; one side stays 2.
- **N2 wall independence.** Exact counts with a cross-axis check.
- **N3 hidden walls.** None.
- **N4 residual matching.** The residual is the square cross-sections
  (4 × 4 and larger).
- **N5 rhetoric audit.** "Gaussian stiffness" names the pattern
  f(S) ≈ c S²/A within the stated bounds.
- **N6 partial-closure paths.** Square cross-sections.
- **N7 steelman.** For a stiffness: one coefficient across three areas.
  Against: every cross-section has width 2. Both are recorded.
- **N8 cross-cycle echo.** Open PR 8740 and the landed cubic-ice note are
  cited.

## Falsifiers

Any of the following falsifies the theorem:
- a count that differs from the cross-axis count;
- a sector transition that changes |S|;
- a coefficient outside the stated bounds.

## Boundaries and non-claims

- The declared cross-sections.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PR 8740 and the landed cubic-ice note are cited. No audit grade, no
new axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the landed 9600 count;
  - two cross-axis counts;
  - exact integer traces.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| two occupied links per vertex | 3 to 2 | caught (2 FAILs) |
| flux without the staggered sign | sign dropped | caught (2 FAILs) |
| area taken as a + b | product to sum | caught (1 FAIL) |
| sector eigenvalue of smallest modulus | max to min | caught (2 FAILs) |
| degree vectors counted once each | multiplicity dropped | caught (2 FAILs) |
| second direction without wrap-around | periodic to open | caught (3 FAILs) |
| 2 x 2 x 6 cross-check read from the 2 x 4 matrix | matrix swapped | caught (1 FAIL) |

  All 7 are caught. One further mutant is equivalent: dropping the last
  configuration of each chunk removes only configurations with a
  degree-4 vertex, which the ice rule never uses.

- **Vacuity guard:** counts, sector maxima and coefficients are printed.
- **Budget:** 3 checks, stdout 827 characters (ceiling 6000), about
  9 s and 0.57 GB (ceiling 900 s).

## Verification

```bash
python3 scripts/uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=3 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_2026_09_23.txt`.
