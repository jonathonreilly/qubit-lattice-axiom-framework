---
claim_id: ring_model_ice_transverse_weight_sum_rule_the_ring_term_moves_the_weight_from_the_smallest_momenta_to_the_zone_corner_without_a_growing_peak_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (open PRs 9066, 9072); the guided continuous-time projector Monte Carlo of open PR 9148 with the forward-walking estimator of open PR 9161. Exact: for O_a(k) = N^{-1/2} sum_v e^{-ik.v} sigma_a(v), Parseval gives (1/N) sum_k sum_a |O_a(k)|^2 = 3 for every link configuration and the Gauss law makes sum_a (1 - e^{-ik_a}) O_a(k) vanish for every ice configuration, so the zone average of the transverse weight T(k) = sum_a |O_a(k)|^2 is exactly 3 (3/2 per polarisation) in every state supported on ice; checked to 1e-15 on samples and 1e-15 on every projector block. Finite diagnostics (120 walkers, projection 40, forward lag 2, ten-bin errors, stars of the cubic group labelled by sorted reduced integers): uniform ice has T within 0.18 of 3 on every non-zero star of 4^3 and 6^3; the pure-ring ground state has T/2 = 0.711 +- 0.014 (4^3) and 0.530 +- 0.022 (6^3) on the axis star (1,0,0), agreeing with open PR 9161 within one standard error, and the ratio pure/uniform runs monotonically from 0.48 and 0.36 at (1,0,0) to 2.18 and 2.06 at the zone corner (pi,pi,pi), whose weight is 6.13 +- 0.36 on 4^3 and 6.12 +- 0.53 on 6^3 against the uniform-ice 2.82 and 2.98; the stars above the uniform value at two standard errors are (2,2,2), (2,2,1), (2,2,0), (2,1,1) on 4^3 and the nine stars with two or three components at or beyond 2pi/3 on 6^3. No order, no phase and no thermodynamic limit is claimed; the corner peak does not grow between the two tori."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_transverse_weight_sum_rule_and_where_the_ring_term_moves_the_weight_2026_09_24.py
---

# The transverse weight of ice is fixed by a sum rule; at the pure-ring point the ring term moves it from the smallest momenta to the zone corner, without a growing peak

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** an exact identity with finite numerical diagnostics under supplied decision points; unaudited.

## Result

Open PR 9161 found the pure-ring ground state's transverse field
fluctuations at the smallest momentum at about a third of the uniform-ice
value. This note shows that the loss is a redistribution, says where the
weight goes, and measures it.
- **The transverse weight is fixed (Theorem 1).** Because every link
  variable squares to one, Parseval fixes the zone average of
  `Σ_a |O_a(k)|²` at 3 for every configuration; because the Gauss law
  holds exactly, the longitudinal combination `Σ_a (1 − e^{−ik_a}) O_a(k)`
  vanishes at every `k`, so the two transverse polarisations carry all of
  it: the zone average of the transverse weight is exactly 3, that is 3/2
  per polarisation, in every ice state and every state supported on ice.
  Uniform ice sits at this average on every star of the cubic group (within
  0.18 on 4³ and 6³); open PR 9161's "1.5" is the zone average itself.
- **The pure-ring ground state moves the weight to the zone corner.** With
  the full weight map carried along walker lineages (forward lag 2), the
  ratio pure/uniform runs monotonically from `0.48` (4³) and `0.36` (6³) at
  the smallest axis star to `2.18` and `2.06` at `(π, π, π)`: the corner
  carries `6.13 ± 0.36` on 4³ and `6.12 ± 0.53` on 6³ against the
  uniform-ice `2.82` and `2.98`. Between the two lie the face and edge
  stars in order of `|k|`. The axis stars reproduce open PR 9161's
  smallest-momentum values within one standard error (`0.711 ± 0.014` vs
  `0.692 ± 0.013`; `0.530 ± 0.022` vs `0.557 ± 0.022`).
- **No growing peak.** The corner weight is the same on 4³ and 6³ within
  errors; a Bragg peak of an ordered state would grow with the volume. The
  alternating circulation the ring term favours on every plaquette
  correlates the link fields in the `(π, π, π)` pattern at short range, and
  on these tori that is all it does.

Supplied model, finite diagnostics: no order, no phase and no
thermodynamic limit is claimed. The sum rule is bookkeeping of the supplied
model; its content here is that the small-`k` suppression of open PR 9161
and the corner enhancement are one fact seen from two ends of the zone.

## Setting and decision points

- **D-gauss, D-roles, D-ring (open PRs 9066, 9072).** Link qubits at link
  sites of the doubled lattice; the exact vertex Gauss law, three in and
  three out; the covariant plaquette clause `−g (U + U†)`; `V = 0`; `g = 1`.
- **The projector and the pure estimator (methods).** The guided
  continuous-time Green's function Monte Carlo of open PR 9148, walkers in
  the zero-winding sector of open PR 9153, the lineage (forward-walking)
  estimator of open PR 9161 at forward lag 2, here carrying the full weight
  map of every walker.
- **The observable (method).** `O_a(k) = N^{−1/2} Σ_v e^{−ik·v} σ_a(v)`,
  with `σ_a(v) = ±1` the arrow on the link leaving `v` along `+a`,
  `k = 2π m/L`, and the weight map `T(k) = Σ_a |O_a(k)|²`, averaged over the
  stars of the cubic group (labelled by the sorted reduced integers
  `(m₁, m₂, m₃)`). On an axis star `T = 2 S_T`, twice open PR 9161's
  per-polarisation structure factor.

None is adopted.

## Theorem 1 — the transverse weight of ice is fixed

For every configuration `σ` of the link field, Parseval's identity gives
`(1/N) Σ_k Σ_a |O_a(k)|² = (1/N) Σ_v Σ_a σ_a(v)² = 3`.
For an ice configuration the Gauss law at every vertex,
`Σ_a [σ_a(v) − σ_a(v − â)] = 0`, reads in Fourier space
`Σ_a (1 − e^{−ik_a}) O_a(k) = 0`: the longitudinal combination vanishes at
every `k`, so at each momentum the two transverse polarisations carry the
whole of `T(k)`. Hence in every ice state, and in every state supported on
ice configurations (the pure-ring ground state, the uniform-ice state, any
guided or projected state), the zone average of the transverse weight is
exactly 3, that is 3/2 per polarisation: the number open PR 9161 measured
for uniform ice at the smallest axis momentum is the zone average itself,
and a state that carries a third of it at small `k` must carry the
difference elsewhere in the zone. Both identities hold configuration by
configuration, so they hold for every Monte Carlo estimate exactly, not in
the mean: the runner checks them to 10⁻¹⁰ on samples and to 10⁻⁹ on every
projector block. ∎

The sum rule is a bookkeeping identity of the supplied model, not a
physical law; its use here is to say where the ring dynamics puts the
transverse weight it removes from long wavelengths.

## Diagnostic — the map by star on 4³ and 6³

Walkers (120 per size) start in the zero-winding sector from the canonical
ice state of open PR 9153 after winding-preserving loop equilibration with
the guiding function `exp(0.2 N_flip)`, and are projected for `τ = 40` in
blocks of 0.05 with the first 8 discarded; each walker carries the weight
map of its lineage and the estimate at forward lag 2 is averaged over the
weighted population, then over the members of each star, then over blocks
(ten-bin errors). Uniform ice is sampled by loop updates. `T` sums the two
transverse polarisations; 3 is the zone average; the `(0,0,0)` star is the
winding weight (4.5 and 4.4 for unconstrained uniform ice, 0 in the
zero-winding sector) and is excluded from the ratios.

| star (units of `2π/L`) | 4³ uniform | 4³ pure ring | ratio | 6³ uniform | 6³ pure ring | ratio |
|---|---|---|---|---|---|---|
| `(1,0,0)` smallest axis | 2.98 | 1.42 ± 0.03 | 0.48 | 2.94 | 1.06 ± 0.04 | 0.36 |
| `(1,1,0)` | 2.99 | 2.15 | 0.72 | 3.04 | 1.55 | 0.51 |
| `(1,1,1)` | 2.88 | 2.94 | 1.02 | 2.90 | 2.03 | 0.70 |
| `(2,0,0)` | 3.04 | 2.34 | 0.77 | 3.04 | 1.98 | 0.65 |
| `(2,1,0)` | 3.00 | 2.97 | 0.99 | 3.08 | 2.28 | 0.74 |
| `(2,1,1)` | 3.01 | 3.64 | 1.21 | 2.96 | 2.52 | 0.85 |
| `(2,2,0)` | 2.98 | 4.20 | 1.41 | 3.00 | 2.97 | 0.99 |
| `(2,2,1)` | 2.95 | 4.84 | 1.64 | 2.98 | 3.28 | 1.10 |
| `(2,2,2)` corner on 4³ | 2.82 | 6.13 ± 0.36 | 2.18 | 2.95 | 3.92 | 1.33 |
| `(3,0,0)` | — | — | — | 2.82 | 2.54 | 0.90 |
| `(3,1,0)` | — | — | — | 2.90 | 2.73 | 0.94 |
| `(3,1,1)` | — | — | — | 3.01 | 3.04 | 1.01 |
| `(3,2,0)` | — | — | — | 2.99 | 3.59 | 1.20 |
| `(3,2,1)` | — | — | — | 2.99 | 3.65 | 1.22 |
| `(3,2,2)` | — | — | — | 3.03 | 4.58 | 1.51 |
| `(3,3,0)` | — | — | — | 2.97 | 3.80 | 1.28 |
| `(3,3,1)` | — | — | — | 3.07 | 4.08 | 1.33 |
| `(3,3,2)` | — | — | — | 3.02 | 4.92 | 1.63 |
| `(3,3,3)` corner on 6³ | — | — | — | 2.98 | 6.12 ± 0.53 | 2.06 |

Pure-ring values other than the axis and corner stars are quoted from the
ratios the runner prints times the uniform values, to two decimals; their
errors are of the order of the corner's relative error.

- **Monotone in `|k|`.** On both tori the ratio increases with the number
  and size of the reduced components: the small-`|k|` stars lose weight,
  the stars with two or three components at or beyond `2π/3` gain it, and
  the gain is largest at the corner. On 6³ the stars above the uniform
  value at two standard errors are `(3,3,3)`, `(3,3,2)`, `(3,3,1)`,
  `(3,3,0)`, `(3,2,2)`, `(3,2,1)`, `(3,2,0)`, `(2,2,2)`, `(2,2,1)`; on 4³
  they are `(2,2,2)`, `(2,2,1)`, `(2,2,0)`, `(2,1,1)`.
- **The guiding function is not the story.** The variational state
  `exp(0.2 N_flip)` puts `1.075` and `1.030` per polarisation on the axis
  star; the projection takes it to `0.711` and `0.530`. The redistribution
  is the ring dynamics, not the Jastrow weight.
- **The corner does not grow.** `6.13 ± 0.36` on 4³ and `6.12 ± 0.53` on
  6³; a Bragg peak would scale as the volume (a factor 3.4 between these
  tori). This is the field-correlation counterpart of the flippability
  diagnostics of open PRs 9146 and 9148, which found no plaquette order to
  8³.
- **Energies.** `e_0 = −0.29276 ± 0.00035` (4³) and `−0.28914 ± 0.00016`
  (6³) per plaquette, within the spread of open PRs 9148, 9153 and 9161. ∎

## What this means for the lanes

- **Photon lane.** The sum rule turns open PR 9161's "a third of the
  uniform-ice constant at the smallest momentum" into a redistribution
  statement: the ring dynamics at `V = 0` moves transverse weight from the
  long-wavelength axis stars to the zone corner `(π, π, π)` and the stars around it. The map by star is the
  finite-torus shape of the pure-ring state's field correlations, with
  uniform ice (flat at the zone average) as the comparison; the receiving
  star is where the ring term's alternating circulation correlates the
  links of a plaquette.
- **What the framework supplied.** The Gauss law, the ring and `V = 0` are
  decision points; the mode, the projector and the forward walking are
  methods; the sum rule is an identity of the supplied model.

## What stays open

- The receiving star's weight as `L` grows (a growing peak would be the
  first sign of an ordering tendency; a saturating one would not), and the
  small-`k` side, which open PR 9161 leaves undecided between a photon and
  a residual constant.
- The same map as `V/g` moves toward the RK point, where every star must
  return to the uniform-ice value.
- Independent checks of every number here.

## Prior art

Parseval's identity and the lattice Gauss law are standard; the
pinch-point form of the classical ice correlator is Youngblood and Axe 1981
and Henley 2005, cited as prior art, not as premises.

## Checks

The runner has 4 checks and all pass in about 1.5 minutes, single-threaded.

| Check | Result |
|---|---|
| Identities | Zone average 3 and longitudinal amplitude 0 on uniform and guided samples of 4³ and 6³, to 10⁻¹⁰. |
| Uniform ice | Axis star at 3/2 per polarisation within 0.12 on both tori; the map by star. |
| Pure ring, 4³ | Sum rule exact per block; axis star within 3 standard errors of open PR 9161; the receiving star. |
| Pure ring, 6³ | The same on 6³. |

## Independent check

None yet. The runner was rerun from a clean shell to write the cache;
seeded Monte Carlo reproduces the numbers. The axis stars are a second
seed of open PR 9161's smallest-momentum values.

## What this does not do

- It adopts no clause, Gauss law or method.
- It claims no order, no phase and no thermodynamic limit; the map is a
  finite-torus diagnostic of a supplied model, and its errors are ten-bin
  standard errors of correlated projector blocks at one forward lag.
