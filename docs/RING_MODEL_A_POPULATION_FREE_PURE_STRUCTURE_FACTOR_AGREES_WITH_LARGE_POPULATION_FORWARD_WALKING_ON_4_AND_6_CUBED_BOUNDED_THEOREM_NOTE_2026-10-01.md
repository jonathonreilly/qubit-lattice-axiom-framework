---
claim_id: ring_model_a_population_free_pure_structure_factor_agrees_with_large_population_forward_walking_on_4_and_6_cubed_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component (link fields sigma = +-1, exact Gauss law, H = -sum_p (U_p + U_p^dag) at the pure ring point) with the landed cyclic transverse modes. Population-free estimate of the pure transverse structure factor S = <|O_a|^2> from the configuration at the MIDDLE of a reptation path (guide exp(0.2 N_flip)), with the path ends giving the mixed estimate, in independent chains; checked against a forward-walking estimate from the fixed-population projector at 3840 walkers. Exact 2^3 control at k = pi: middle S = 1.0119 +- 0.0015 against the exact 1.01215 and ends S = 0.9907 +- 0.0009 against the exact mixed 0.98972. 4^3 at k = pi/2: reptation 0.6196 +- 0.0188 (10 chains) against forward walking 0.6374 +- 0.0080 (lag 4), 0.9 combined standard errors. 6^3 at k = pi/3: reptation 0.5037 +- 0.0165 (8 chains, canonical and loop starts) against forward walking 0.4964 +- 0.0088, 0.4 combined standard errors; every chain's path shifted by at least 1.5 path lengths in production. Both values lie below the landed 120-walker forward-walking values (0.688 on 4^3, about 0.56 on 6^3) and within the landed moment ceilings s sqrt(u chi) (0.721 and 0.556). So without any walker population the pure S agrees with large-population forward walking on 4^3 and 6^3, and the landed small-population values are high. Exact 2^3 references are computed in the runner. No 8^3 or larger population-free value, certified structure factor, single-mode statement, limit or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_on_8_cubed_the_forward_walking_structure_factor_falls_with_the_population_to_within_the_moment_bound_bounded_theorem_note_2026-09-28
runner: scripts/ring_model_population_free_pure_structure_factor_by_reptation_on_small_tori_2026_10_01.py
---

# A population-free pure structure factor agrees with large-population forward walking on 4³ and 6³

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** finite diagnostics with an exact control; unaudited.

## Supplied setting

Use the supplied ring component and the cyclic transverse modes `O_a` of the
landed note
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`.
The landed note
`RING_MODEL_ON_8_CUBED_THE_FORWARD_WALKING_STRUCTURE_FACTOR_FALLS_WITH_THE_POPULATION_TO_WITHIN_THE_MOMENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-28.md`
found that the forward-walking structure factor `S` falls as the walker
population grows. It follows that the earlier small-population values were
too high. That conclusion rests on the same estimator family.

**This block's estimator.** It estimates the pure `S` with no walker
population at all.
- A reptation path of imaginary time is sampled with the guide
  `exp(0.2 N_flip)`.
- For a long path, the configuration at its middle is distributed as the
  ground state squared, so `|O_a|²` measured there is a pure estimate.
- The two ends give the mixed estimate.
- The middle configuration is advanced incrementally, and at every
  measurement it is checked against a replay from the path's tail.

## Result

1. **Exact 2³ control at `k = π`.** The 864-state component's exact
   references are computed in the runner. Over twelve chains:
   - middle `S = 1.0119 ± 0.0015`, against the exact `1.01215`;
   - ends `S = 0.9907 ± 0.0009`, against the exact mixed value `0.98972`.
2. **4³ at `k = π/2`.**
   - Reptation, 10 chains: `0.6196 ± 0.0188`.
   - Forward walking at 3840 walkers: `0.6374 ± 0.0080` at lag 4, which is
     0.9 combined standard errors away.
   - Every chain's path shifted by 2.2 to 3.5 path lengths during
     production.
3. **6³ at `k = π/3`.**
   - Reptation, 8 chains from canonical and loop starts: `0.5037 ± 0.0165`.
   - Forward walking at 3840 walkers: `0.4964 ± 0.0088`, which is 0.4
     combined standard errors away.
   - Every chain's path shifted by 1.66 to 2.10 path lengths during
     production.
4. **Mixed values agree too.** The reptation ends and the forward-walking
   lag-0 values agree: `0.844` against `0.852` on 4³, and `0.685` against
   `0.686` on 6³.

| torus | reptation (pure) | forward walking, 3840 walkers | landed 120-walker value | landed moment ceiling |
|---|---|---|---|---|
| 4³ | `0.620 ± 0.019` | `0.637 ± 0.008` | `0.688` | `0.721` |
| 6³ | `0.504 ± 0.017` | `0.496 ± 0.009` | `≈ 0.56` | `0.556` |

## What follows

- **Population-free confirmation.** Without any walker population, the pure
  structure factor agrees with large-population forward walking on 4³ and
  6³.
- **The landed small-population values were high.** Those 120-walker values
  lie above the population-free ones.
- **Within the moment bound.** The population-free values lie within the
  landed moment ceilings `s√(uχ)`.

## Estimator and reproduction boundary

- **Errors.** Errors are the chain-to-chain scatter. Path motion is slow,
  so each production run is required to shift the path by at least 1.5
  path lengths.
- **8³ not covered.** On 8³ the path moves too slowly for this estimator at
  these lengths, so no population-free value is given there.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³, 4³ and 6³.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimators remain supplied.
- **N4:** the landed moment identities and forward-walking note govern their scopes.
- **N5:** finite estimates with an exact control.
- **N6:** a population-free value on 8³ and larger tori remains open.
- **N7:** other estimators and guides remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_population_free_pure_structure_factor_by_reptation_on_small_tori_2026_10_01.py
```

Nine checks; prints `TOTAL: PASS=9 FAIL=0` in about ten minutes of computation.
