---
claim_id: ring_model_the_zero_winding_gauss_sector_has_frozen_flip_components_on_every_even_torus_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied ring model: link fields sigma = +-1 on the periodic cubic torus with the exact vertex Gauss law (3 in, 3 out), plaquette flips of circulating plaquettes, canonical zero-winding state sigma_x = (-1)^y, sigma_y = sigma_z = (-1)^x. Exact: (1) for even L the axis-constant states sigma_x = s(z), sigma_y = g(x), sigma_z = h(y), and the anticyclic version, with s, g, h balanced +-1 sequences, satisfy the Gauss law, have zero winding and no circulating plaquette, so each is a one-state flip component distinct from the canonical one: 2 C(L, L/2)^3 states (16, 432, 16000, 686000 for L = 2, 4, 6, 8; all checked for L <= 6, a fixed sample of 300 for L = 8); (2) exhaustive enumeration: on 2x2x2, 880 zero-winding Gauss states = the 864-state canonical component plus 16 frozen states; on 2x2x4, 1 552 024 = 1 551 976 + 48 frozen; in both cases the frozen states are exactly the family of (1); (3) the kernel of the plaquette circulation matrix has dimension n_v + 2 for L = 2, 4, so the linear flip invariants on Gauss states are the three windings; (4) for odd L every Gauss state has odd winding in each direction, so the zero-winding sector is empty; (5) replayed flip certificates place the 48 non-frozen staggered images of the canonical state (L = 4, 8) and fixed-seed loop-sampled starts (twenty on 4^3, five on 8^3) in the canonical component. Not shown: that every non-frozen zero-winding state lies in the canonical component for L >= 4, or that the family lists every frozen state for L >= 4; no energy is computed; no physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_zero_winding_gauss_sector_has_frozen_flip_components_on_every_even_torus_2026_10_01.py
---

# The zero-winding Gauss sector has frozen flip components on every even torus

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact integer computations and exhaustive enumeration, for a supplied model; unaudited.

## Supplied setting

The landed ring-model notes work in the connected flip component of the canonical
zero-winding state on the cubic `L³` torus. This note shows that the restriction
is not empty of content. The zero-winding Gauss sector is not flip-connected.

## Results

1. **Frozen family (exact, every even L).** Take balanced `±1` sequences `s, g, h`
   of length `L`, and set `σ_x = s(z)`, `σ_y = g(x)`, `σ_z = h(y)`, or the anticyclic
   version `σ_x = f(y)`, `σ_y = g(z)`, `σ_z = h(x)`.
   - These states satisfy the Gauss law, have zero winding, and have no
     circulating plaquette.
   - So each is a one-state flip component, distinct from the canonical one,
     which has circulating plaquettes.
   - There are `2·C(L, L/2)³` of them: 16, 432, 16000 and 686000 for `L = 2, 4, 6, 8`.
   - The runner checks every member for `L ≤ 6` and a fixed sample of 300 for `L = 8`.
2. **Exhaustive enumeration.** Every frozen state found is a member of the family.

   | Torus | All Gauss states | Zero winding | Canonical component | Frozen |
   |---|---|---|---|---|
   | 2×2×2 | 9600 | 880 | 864 | 16 |
   | 2×2×4 | 23 063 296 | 1 552 024 | 1 551 976 | 48 |

3. **Linear invariants.** For `L = 2, 4`, the kernel of the plaquette circulation
   matrix has dimension `n_v + 2`. So the linear flip invariants on Gauss states
   are exactly the three windings.
4. **Odd L.** Every Gauss state has odd winding in each direction, so the
   zero-winding sector is empty.
5. **Certificates.** An independent function replays explicit flip lists that end
   at the canonical state. They place in the canonical component:
   - the 48 non-frozen staggered images of the canonical state, at `L = 4` and `L = 8`;
   - fixed-seed loop-sampled starts (`|exp(0.2 N_flip)|²` in the zero-winding
     sector): twenty on 4³ and five on 8³.

## Reading for the landed numerics

- The restriction to the canonical component in the landed notes is necessary:
  frozen states exist on every even torus.
- The tested loop-sampled starts do lie in the canonical component. So the
  start-state dependence seen in an unlanded 8³ reptation probe is not explained
  by a component split among those starts. Incomplete equilibration remains the
  untested alternative.

## What this does not show

- That every non-frozen zero-winding state lies in the canonical component, for `L ≥ 4`.
- That the family lists every frozen state, for `L ≥ 4`.
- Any energy.
- Any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied ring model; tori as listed.
- **N2:** no phase or no-go wall is imported.
- **N3:** the model and the canonical state remain supplied.
- **N4:** the landed sector convention is used as stated there.
- **N5:** exact integer computations, exhaustive enumeration and replayed certificates.
- **N6:** the items listed above remain open.
- **N7:** other sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_zero_winding_gauss_sector_has_frozen_flip_components_on_every_even_torus_2026_10_01.py
```

Nineteen checks; prints `TOTAL: PASS=19 FAIL=0` in under half a minute.
