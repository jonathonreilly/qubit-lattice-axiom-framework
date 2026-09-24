---
claim_id: uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Uniform ice on L x L x L cubic tori is sampled by a worm on the divergence-free arrows: it starts at a uniformly random vertex, reverses one of the three outgoing arrows (never the one just reversed) at every step, and stops on returning to the start. Every step has probability 1/3 both ways, so it samples the uniform measure on all ice configurations, winding sectors included. By cubic symmetry the sum-rule stiffness is K_L = 2/3 + 1/(3N) exactly. Control: all 2^24 arrow patterns of the L = 2 torus give 9600 ice configurations, 880 at zero flux, in 125 winding sectors, with <W^2> = 76/25 per direction; the worm reproduces <W^2> (3.0367 +- 0.0094) and the zero-flux fraction (0.09155 +- 0.00065 against 0.09167) and visits every sector. A Gaussian divergence-free field gives the winding the weight exp(-K W^2/(2L)) and the equal-time correlation S_zz(k) = P_zz(k)/K; the sum rule <E_z^2> = 1 fixes K_L = (1/N)(sum_{k != 0} P_zz(k) + 1), which tends to 2/3. The winding stiffness c_W = K_W/2, inverted from <W^2>, is 0.3329, 0.3350, 0.3356 and 0.3350 on L = 8, 12, 16 and 24 (standard errors 0.0011 to 0.0024), within 1% of K_L/2; combined over L = 12, 16 and 24 it is 0.3352 +- 0.0008, 0.56% above 1/3. On L = 8 with 10^6 worms, K_L S_zz/P_zz agrees with 1 within 1% in all 70 symmetry classes with P_zz > 0.05; the deviations are systematic: the smallest wavevectors lie below 1 (0.9966 +- 0.0004), the zone corner above (+0.70% +- 0.27%). The stiffness the smallest wavevectors imply, 0.3348 +- 0.0001, agrees with the winding value within 2 standard errors. S_zz vanishes on the longitudinal axis, and no vertex carries divergence after sampling. No limit beyond the sampled sizes is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_2026_09_23.py
---

# Uniform ice on cubic tori: the winding stiffness and the correlations carry the sum-rule stiffness

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8871 found on infinite
prisms of small cross-section that one stiffness sets both the flux cost
and the correlations of uniform ice. The unit field on every link fixes
that stiffness through the sum rule, and the Gaussian reading's value on
large sections is K = 2/3, c = 1/3. Transfer matrices stop at
cross-sections of 16 sites. This block tests the value on tori with up to
13824 sites.

## Result up front

1. **The sampler.** A worm moves on the divergence-free arrows. It starts
   at a uniformly random vertex, and at every step it reverses one of the
   three outgoing arrows of its head, never the one it just reversed. It
   stops when it returns to the start. Every step has probability 1/3,
   forwards and backwards, so the worm samples the uniform measure on all
   ice configurations of the torus, winding sectors included.

2. **The exact control.** On the L = 2 torus all 2^24 arrow patterns give:
   - 9600 ice configurations, 880 of them at zero flux, as in the landed
     RK note;
   - 125 winding sectors;
   - ⟨W²⟩ = 76/25 per direction.

   The worm reproduces ⟨W²⟩ (3.0367 ± 0.0094) and the zero-flux fraction
   (0.09155 ± 0.00065 against 0.09167), and it visits every sector.

3. **What the Gaussian predicts.** A Gaussian divergence-free field with
   stiffness K on the torus gives:
   - the winding W through a plane the weight exp(−K W²/(2L)) on W ∈ 2Z;
   - the equal-time correlation S_zz(k) = P_zz(k)/K at k ≠ 0, with
     P_zz = 1 − s_z²/(s_x² + s_y² + s_z²) and s_i² = 2 − 2 cos k_i.

   The sum rule ⟨E_z²⟩ = 1 fixes K_L = (1/N)(Σ_{k≠0} P_zz(k) + 1). The
   projector's trace is 2 at every k ≠ 0, and cubic symmetry shares it
   equally among the three directions, so K_L = 2/3 + 1/(3N) exactly.

4. **The winding stiffness.** Inverting ⟨W²⟩ through the discrete Gaussian
   gives c_W = K_W/2:

   | L | c_W | K_L/2 |
   |---|---|---|
   | 8 | 0.3329 ± 0.0013 | 0.3337 |
   | 12 | 0.3350 ± 0.0011 | 0.3334 |
   | 16 | 0.3356 ± 0.0013 | 0.3334 |
   | 24 | 0.3350 ± 0.0024 | 0.3333 |

   Every value is within 1% of the sum-rule value. Combined over L = 12,
   16 and 24 it is 0.3352 ± 0.0008, 0.56% above 1/3.

5. **The correlations.** On L = 8 with 10^6 worms, grouped into the 70
   symmetry classes with P_zz > 0.05, K_L S_zz/P_zz agrees with 1 within 1%
   in every class. At this precision the deviations are systematic, not
   noise:
   - the smallest wavevectors lie below 1: 0.9966 ± 0.0004;
   - the zone corner (π, π, π) lies above: +0.70% ± 0.27%.

   The stiffness the smallest wavevectors imply, K_L/(2r) = 0.3348 ±
   0.0001, agrees with the winding value within 2 standard errors.

6. **The longitudinal null.** S_zz vanishes at k = (0, 0, k_z ≠ 0), and no
   vertex carries divergence after sampling.

7. **What this means.** On tori far beyond the transfer matrices, the
   static field of uniform ice keeps the stiffness that the sum rule
   fixes, to half a percent. Two independent measurements agree on the
   long-wavelength value: the winding fluctuations on L = 12 to 24 give
   0.3352 ± 0.0008, and the smallest correlation wavevectors on L = 8 give
   0.3348 ± 0.0001. That is about 0.5% above the Gaussian reading's 1/3.
   The residual has a source: the unit field puts slightly more weight at
   the zone boundary than a Gaussian with the same sum rule, so slightly
   less remains at long wavelengths. The static photon's coupling is
   therefore fixed by uniform ice itself, with no free constant. The sum
   rule gives it to 0.5%; the measured long-wavelength value is c ≈ 0.335.
   No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_2026_09_23.py`
- **Result:** `TOTAL: PASS=8 FAIL=0`, about 115 s, stdout 1583 characters,
  peak about 390 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_2026_09_23.txt`
- **Arithmetic:** exact integer enumeration on L = 2 with the exact
  fraction 76/25; seeded sampling (numba's generator, fixed seeds) with
  standard errors from 20 or 40 bins; the Gaussian quantities in closed
  form; K_W by bisection on the discrete Gaussian.

## Premises and declared objects

- **Uniform ice:** three of six links occupied at every vertex; equivalently
  divergence-free arrows E = ±1.
- **Worm sampler:** as stated, with fixed seeds.
- **Winding:** W_i, the arrow sum over the links crossing a plane normal to
  i; it is the same for every such plane.
- **Comparison field:** the Gaussian divergence-free field on the torus,
  built from the Z^3 graph Laplacian of the landed note
  `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`.

## Prior art and what is new

- Open PR 8871: on small prisms the unit link field fixes one stiffness for
  the flux cost and the correlations.
- The landed note
  `SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`
  counted the L = 2 configurations (9600, and 880 at zero flux) and
  sampled zero-flux tori of side 6 to 12 by plaquette moves. It found the
  longitudinal null and finite transverse weights, but no amplitude. Its
  moves cannot change the winding.
- New here: a sampler that reaches every winding sector, validated
  exactly on L = 2; the exact sum-rule stiffness 2/3 + 1/(3N); the
  winding stiffness on L up to 24; the correlation
  amplitude against the sum rule in every symmetry class; and the finding
  that the long-wavelength stiffness lies 0.5% above the sum-rule value,
  measured two independent ways.

## Theorem — The sampled tori

On L = 2 the enumeration is exact. On L = 8, 12, 16 and 24, the sampled
winding stiffness and correlations stand in the stated relations to the
sum-rule stiffness, with the stated standard errors. No limit is claimed
beyond the sampled sizes.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger tori and longer runs are the direct
  extension.
- **N2 wall independence.** The winding and the correlations are
  separate observables; the L = 2 enumeration checks the sampler.
- **N3 hidden walls.** Sampling error is estimated by binning. The worm's
  detailed balance is argued above and checked against the exact L = 2
  measure.
- **N4 residual matching.** Nothing is fitted. The 0.5% residual is
  reported, not absorbed.
- **N5 rhetoric audit.** "Carry the sum-rule stiffness" means within 1%
  on every size, with the systematic 0.5% offset stated.
- **N6 partial-closure paths.** The same test for the prism flux cost at
  larger cross-sections; the zone-boundary excess on larger tori.
- **N7 steelman.** For exact equality with 1/3: every size is within 1%.
  Against: the combined winding value is 2.3 standard errors above 1/3,
  and the small wavevectors agree with it. Both are recorded, and the
  note concludes the offset is real at the 0.5% level.
- **N8 cross-cycle echo.** Open PR 8871 and the landed RK note are cited.

## Falsifiers

- A sampled size on which c_W departs from K_L/2 by more than 1%.
- A symmetry class on L = 8 whose ratio departs from 1 by more than 1%.
- A worm estimate on L = 2 more than 4 standard errors from the exact
  values.

## Boundaries and non-claims

- Tori of side 2 (exact) and 8 to 24 (sampled).
- No limit beyond the sampled sizes is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, open PR 8871, and the landed RK and lattice-Green notes
are cited; the comparison field is built from the framework's Z^3 graph
Laplacian. No audit grade, no new axiom, no new primitive, no new
comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the exact L = 2 enumeration; the winding and
  the correlations as separate observables; the closed-form Gaussian.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| exclusion dropped for forward links only | worm made asymmetric | caught (5 FAILs) |
| biased step choice | worm made non-uniform | caught (4 FAILs) |
| winding read on the wrong plane | winding changed | caught (4 FAILs) |
| winding weight without the factor 2 | Gaussian changed | caught (3 FAILs) |
| projector for the x component | projector changed | caught (2 FAILs) |
| sum rule without the zero mode | K_L shifted by 1/N | caught (1 FAIL) |
| initial state not divergence-free | start changed | caught (nonzero exit) |
| structure factor of E_x | component changed | caught (3 FAILs) |
| enumeration misses one in-link | control changed | caught (1 FAIL) |
| worm stops one step early | defects left behind | caught (nonzero exit) |
| smallest classes read above 1 | direction reversed | caught (1 FAIL) |

  11 of 11 are caught. The zero-mode mutant shifts K_L by 1/N, below the
  1% tolerance, and was missed until the exact check K_L = 2/3 + 1/(3N)
  was added.

- **Vacuity guard:** every stiffness with its error, the class extremes
  and the control values are printed.
- **Budget:** 8 checks, stdout 1583 characters (ceiling 6000), about 115 s
  (ceiling 900 s), peak about 390 MB.

## Verification

```bash
python3 scripts/uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=8 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_2026_09_23.txt`.
