---
claim_id: uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The uniform ice measure (3 of each vertex's 6 links occupied) on prisms whose cross-section is an n x n torus, infinite along the axis, formed by layer units: a unit is the slab between heights z and z + 1, its in-plane links and the vertical links above it. The ice rule at the layer's vertices couples a unit only to the vertical links below it, so the transfer matrix T[v, w] (in-plane configurations completing ice between vertical links v below and w above) counts the ice states of the n x n x H torus as trace T^H. For n = 2: trace T^2 = 9600, the landed count of the 2 x 2 x 2 torus, and trace T^4 = 23063296 agrees with a transfer along another axis. The staggered vertical flux S(v) = sum of (-1)^(x+y) (2 v - 1) flips sign at every layer, so |S| is conserved: sectors |S| = 0, 2, 4 with 6, 8 and 2 layer states. The zero-flux block is entrywise positive with characteristic polynomial (x - 6)(x + 10)(x + 14)^2 (x^2 - 64 x + 188) and simple top eigenvalue 32 + 2 sqrt 209 = 60.91; the flux sectors have eigenvalues +46, -46 and +18, -18. Long tori select zero flux: the share of ice states with flux falls as 2 (46 / 60.91)^H for even H and vanishes for odd H. In the zero-flux sector the law of a layer given the layer below and the far end of a long torus tends to the kernel P(w | v) = T[v, w] phi(w) / (lambda phi(v)), independent of the far end (deviation 8.7e-10 at H = 16), so forming the prism layer by layer with this kernel from a zero-flux layer reproduces the long-prism limit, each layer's law depending only on the vertical links below it. For n = 3 the top eigenvalues come as a pair +lambda, -lambda: the vertical parity alternates, and odd tori have no ice states. A second cross-section, 2 x 4 (256 layer states), behaves the same way: flux sectors 0 to 8, a zero-flux block (70 states) with positive square and top eigenvalue 2401.33 above every flux sector's, and a layer kernel that forgets the far end. The infinite cross-section is not reached. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
runner: scripts/uniform_ice_layer_units_on_infinite_prisms_zero_flux_transfer_chain_2026_09_23.py
---

# Uniform ice by layer units on infinite prisms is exact in the zero-flux sector that long prisms select

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The assembly (open PR 8648) lists as an open
edge exact formation of the uniform ice measure "by layer units on the
infinite lattice". Open PR 8720 showed that finite cell units fail around
blocks, and that chains of units work on finite windows. This block runs
the chain along an infinite axis.

## Result up front

1. **Layers carry the measure through a transfer matrix.** Take a prism
   whose cross-section is an n × n torus, infinite along its axis. A layer
   unit is the slab between heights z and z + 1: its in-plane links and
   the vertical links above it. The ice rule at the layer's vertices
   couples a unit only to the vertical links below it. So the transfer
   matrix T[v, w] counts in-plane configurations that complete ice between
   vertical links v below and w above. The n × n × H torus then has
   trace T^H ice states.
   - For n = 2, trace T² = 9600, the landed count of the 2 × 2 × 2 torus.
   - trace T⁴ = 23063296 agrees with a transfer along another axis.

2. **The flux through the cross-section is conserved.** The staggered
   vertical flux S(v) = Σ (−1)^(x+y) (2v − 1) flips sign at every layer,
   so |S| is conserved. For n = 2 the sectors are:

   | sector | layer states | eigenvalues |
   |---|---|---|
   | \|S\| = 0 | 6 | simple top eigenvalue 32 + 2√209 ≈ 60.91 |
   | \|S\| = 2 | 8 | +46 and −46 |
   | \|S\| = 4 | 2 | +18 and −18 |

   The zero-flux block is entrywise positive. Its characteristic
   polynomial is (x − 6)(x + 10)(x + 14)²(x² − 64x + 188). This is fixed
   exactly by the integer traces of its first six powers (Newton's
   identities), and the polynomial annihilates the block.

3. **Long prisms select zero flux.** The share of torus ice states that
   carry flux falls as 2(46/60.91)^H for even H and vanishes for odd H.

4. **Layer units form the zero-flux measure exactly.** In the zero-flux
   sector, take the law of a layer given the layer below and the far end
   of a long torus. It tends to the kernel
   P(w | v) = T[v, w] φ(w) / (λ φ(v)) and does not depend on the far end:
   the deviation is 8.7 × 10⁻¹⁰ at H = 16.
   - Forming the prism layer by layer with this kernel reproduces the
     long-prism limit. The first layer is drawn from the zero-flux sector
     with weight φ(v)², the stationary law. T is symmetric, so the chain
     runs the same way down as up.
   - Each layer's law depends only on the vertical links below it, which
     are its formed neighbours.

   Because the flux is conserved, a chain started in another sector stays
   there.

5. **Odd cross-sections alternate.** For n = 3 the top eigenvalues come
   as a pair +λ, −λ, so the parity of the vertical links alternates.
   Odd tori have no ice states, since 3V/2 occupied links must be an
   integer.

6. **A second cross-section agrees.** On the 2 × 4 cross-section (256
   layer states) the flux is again conserved, with sectors |S| = 0 to 8.
   The zero-flux block (70 states) has an entrywise positive square and a
   top eigenvalue 2401.33, above every flux sector's (at most 2059.36).
   The layer kernel again forgets the far end.

7. **What this means for the open edge.** Chains of layer units form the
   uniform ice measure exactly along an infinite axis, on both cross-sections
   checked. They must start in
   the zero-flux sector, which long prisms select. The infinite
   cross-section, the full infinite lattice, is not reached here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "exact formation of the uniform ice measure by layer units on the infinite lattice (assembly open edge, open PR 8648)"
source_of_blocker_text: open_pr_8648
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record in the assembly: layer units form the uniform ice measure exactly on infinite prisms of cross-section 2 x 2, in the zero-flux sector; the infinite cross-section remains open"
conditional_surface_status: "uniform ice measure on n x n transverse tori times Z; layer units; zero-flux sector"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact integer transfer matrices, an exact characteristic polynomial, and convergence checked at stated tolerances"
```

## Premises and declared objects

- **Measure.** The uniform ice measure: 3 of each vertex's 6 links are
  occupied. Prisms are the n × n transverse torus times the integers.
- **Layer unit.** The in-plane links of one layer and the vertical links
  above it. Vertex, plaquette and cube records are functions of links, so
  they add nothing to the conditionals.
- **Criterion.** The unit form of the local formation criterion (open PRs
  8715 and 8720): a unit's law given everything formed depends only on its
  formed neighbours.
- **Arithmetic.** Exact integer transfer matrices, traces and
  annihilating polynomial. Eigenvectors and convergence are in floating
  point at stated tolerances.

## Prior art and what is new

- Open PR 8720: joint cell units, and chains of units on finite windows.
- Open PR 8727 and the landed cubic-ice note: the 2 × 2 × 2 torus with
  9600 ice states.
- New here:
  - the infinite axis;
  - the conserved flux and its sectors;
  - zero-flux selection by long prisms;
  - the exact zero-flux kernel;
  - the odd-cross-section alternation.

## Theorem 1 — Transfer and flux

The ice rule at a layer's vertices involves only the in-plane links of that
layer and the vertical links just below and just above it. Summing over
the in-plane links gives T[v, w], and the ice states of the n × n × H
torus number trace T^H.

In-plane degrees sum to 3n² − |v| − |w|, and that sum is twice the number
of in-plane links, so it is even. With the staggered sign, conservation
sharpens to S(w) = −S(v) whenever T[v, w] > 0. The runner checks this for
all 256 pairs at n = 2.

## Theorem 2 — The zero-flux chain

The zero-flux block is positive, so its top eigenvalue is simple with a
positive eigenvector φ (Perron). The torus conditional of a layer given
the layer below (v) and the far end (a) is
T[v, w] (T^(H−2))[w, a] / (T^(H−1))[v, a]. It converges to
T[v, w] φ(w) / (λ φ(v)) at the rate of the second eigenvalue, 14/60.91 per
layer. The chain with this kernel is a nearest-neighbour chain of layer
units, and it reproduces the limit measure.

## No-Go Discipline Gate

The negative content is small: odd tori have no ice states, and flux
sectors lose weight on long prisms. Both are scoped to the declared prisms.

- **N1 alternative routes.** Infinite cross-sections are outside this
  block.
- **N2 wall independence.** Exact counts, a cross-axis check, an exact
  polynomial.
- **N3 hidden walls.** The zero-flux start is the sector that long prisms
  select, not a new choice.
- **N4 residual matching.** The residual is the infinite cross-section.
- **N5 rhetoric audit.** "Exact" refers to the declared prisms and the
  zero-flux sector.
- **N6 partial-closure paths.** Larger even cross-sections, which need a
  transfer within the layer.
- **N7 steelman.** For layer units: they form the measure exactly along
  an infinite axis. Against: the unit is a whole layer, and the
  cross-section is finite here.
- **N8 cross-cycle echo.** Open PRs 8648, 8715, 8720 and 8727 are cited.

## Falsifiers

Any of the following falsifies the theorems:
- a transfer count that differs from 9600 or from the cross-axis count;
- a transition between different |S|;
- a far-end dependence that does not vanish;
- an ice state on an odd torus.

## Boundaries and non-claims

- The declared prisms, units and sectors.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8648, 8715, 8720 and 8727 and the landed cubic-ice note are cited.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the landed 9600 count;
  - a transfer along another axis;
  - the exact characteristic polynomial, from traces of powers;
  - the direct far-end dependence.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| two occupied links per vertex | 3 to 2 | caught (4 FAILs) |
| cross-section without the x links | x links dropped | caught (5 FAILs) |
| flux without the staggered sign | sign dropped | caught (3 FAILs) |
| kernel from the lowest eigenvector | argmax to argmin | caught (1 FAIL) |
| share counted over zero flux | complement | caught (1 FAIL) |
| conditional with swapped powers | H - 1 and H - 2 swapped | caught (1 FAIL) |
| quadratic factor off by one | 188 to 187 | caught (1 FAIL) |
| odd cross-section parity test inverted | even to odd | caught (1 FAIL) |
| cross-check along the same axis | 2 x 4 to 2 x 2 | caught (1 FAIL) |
| eigenvalue -14 taken once | multiplicity 2 to 1 | caught (1 FAIL) |
| 2 x 4 flux without the staggered sign | sign dropped | caught (1 FAIL) |
| 2 x 4 kernel from the lowest eigenvector | argmax to argmin | caught (1 FAIL) |
| 2 x 4 kernel without its normalisation | phi factors dropped | caught (1 FAIL) |

  All 13 are caught. One further mutant is equivalent: shifting one
  matrix power in the 2 x 4 conditional by one leaves the large-H limit
  unchanged, since both powers project onto the top eigenvector.

- **Vacuity guard:** counts, sector sizes, spectra, shares and deviations
  are printed.
- **Budget:** 6 checks, stdout 2222 characters (ceiling 6000), about 2 s
  (ceiling 900 s).

## Verification

```bash
python3 scripts/uniform_ice_layer_units_on_infinite_prisms_zero_flux_transfer_chain_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_layer_units_on_infinite_prisms_zero_flux_transfer_chain_2026_09_23.txt`.
