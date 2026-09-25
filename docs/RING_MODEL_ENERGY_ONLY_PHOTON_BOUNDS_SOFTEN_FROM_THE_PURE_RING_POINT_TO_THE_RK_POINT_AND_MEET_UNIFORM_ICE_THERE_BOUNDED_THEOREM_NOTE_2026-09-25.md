---
claim_id: ring_model_energy_only_photon_bounds_soften_from_the_pure_ring_point_to_the_rk_point_and_meet_uniform_ice_there_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit ice model with the exact vertex Gauss law and H = -g sum_p (U_p + U_p^dag) + V sum_p n_p, g = 1, V/g in {0, 0.25, 0.5, 0.75, 0.9, 1}, on the 8^3 torus in the flip component of the canonical zero-winding state; the cyclic mode triple and compiled projector of open PR 9236 (480 walkers, projection 30, three seeds). Exact: the ring expectation per plaquette is u = -(E_0 - V dE_0/dV)/N_p (Hellmann-Feynman), the averaged f-sum 2 u s^2 is unchanged by the diagonal V term, and at V = g the averaged susceptibility obeys chi >= S^2/(n_f s^2) with S the uniform-ice structure factor. Finite estimates: at V = g the projector energy vanishes on every block, u = 0.2618 against the directly sampled flippable density 0.2601, chi(pi/4) = 14.47 +- 0.42 against the floor 14.71 from directly sampled uniform ice, and the structure-factor bound 1.490 +- 0.021 against the sampled 1.502 +- 0.048; along the sweep chi(pi/4) = 1.077, 1.494, 2.220, 3.983, 6.968, 14.47, the bound on omega_min/s at pi/4 = 1.035, 0.878, 0.715, 0.526, 0.393, 0.269 (fitted (1 - V/g)^(0.450 +- 0.004) over 0-0.9), the structure-factor bound at pi/4 = 0.427 ... 1.490, and chi(pi/4)/chi(pi/2) = 0.90, 0.98, 1.11, 1.38, 1.80, 2.97 (3.41 for a quadratic mode). No transition point, photon law or limit is claimed; the evaluated bounds are estimates of bounds, not certified enclosures."
upstream_dependencies:
  - minimal_axioms
  - ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_continuously_bounded_theorem_note_2026-09-24
  - ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_energy_only_photon_bounds_from_the_pure_ring_point_to_the_rk_point_2026_09_25.py
---

# From the pure-ring point to the RK point the energy-only photon bounds soften continuously and meet uniform ice there

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model with finite projector estimates; unaudited.

## Result

Open PR 9236 bounded the pure-ring photon with energies alone: the lowest
transverse excitation by `2 s(k)(u/χ̄)^{1/2}` and the structure factor by
`s(k)(u χ̄)^{1/2}`, with `χ̄` the mode-averaged static susceptibility. This
block follows those bounds along the RK potential from `V = 0` to the RK
point `V = g`, where the ground state is uniform ice and the photon is
quadratic. The landed sweep note followed the transverse weight map along
the same line.
- **The ring expectation from energies (Theorem 1).** `∂E_0/∂V = ⟨N_flip⟩`,
  so `u = −(E_0 − V ∂E_0/∂V)/N_p` needs only energies, and the averaged f-sum
  keeps its form at every `V`.
- **The RK point reproduces uniform ice.** The projector's energy
  vanishes on every block; its ring expectation `0.2618` matches the
  directly sampled flippable density `0.2601`; its susceptibility at `π/4`,
  `14.47 ± 0.42`, sits on the exact Cauchy–Schwarz floor `14.71` set by
  directly sampled uniform ice; and its structure-factor bound `1.490`
  matches uniform ice's `1.502`.
- **The bounds soften continuously.** On 8³ the susceptibility at `π/4`
  rises from `1.08` to `14.5`, the bound on the photon energy per unit
  lattice momentum falls from `1.035` to `0.269`, and the structure-factor
  bound rises from `0.43` to `1.49`, monotonically at every step.
- **The velocity follows `(1 − V/g)^{1/2}` within the finite-momentum
  curvature.** At `π/4` the bound on `ω_min/s` falls as `(1 − V/g)^{0.450}`
  over `0 ≤ V/g ≤ 0.9`. Reading the two momenta as `ω²/s² = c² + ρ² s²`
  (arithmetic on the printed bounds, not a runner check) separates the
  curvature and gives `c(V)/c(0) = 0.84, 0.66, 0.46, 0.30` at
  `V/g = 0.25, 0.5, 0.75, 0.9`, a fitted exponent `0.515`, against
  `0.87, 0.71, 0.50, 0.32` for `(1 − V/g)^{1/2}`.
- **The quadratic mode appears.** `χ̄(π/4)/χ̄(π/2)` climbs from `0.90` at
  the pure-ring point to `2.97` at the RK point, against `3.41` for a
  quadratic mode of fixed weight.

Supplied model, finite estimates on one torus: no transition point, photon
law or limit is claimed. What the sweep shows is that the energy-only
bounds of the pure-ring point connect continuously to the exactly known RK
point, and that along the way they behave as a photon whose velocity
vanishes at the RK point.

## Setting and decision points

- **D-gauss, D-roles, D-ring, D-RK (landed).** The exact vertex Gauss law and
  the plaquette clause `H = −g Σ_p (U_p + U_p†) + V Σ_p n_p`, `g = 1`, with
  `V/g` swept from the pure-ring point to the Rokhsar–Kivelson point as in
  `RING_MODEL_FROM_THE_RK_POINT_TO_THE_PURE_RING_POINT_THE_TRANSVERSE_WEIGHT_MOVES_TO_THE_ZONE_CORNER_CONTINUOUSLY_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
- **The probe and the projector (methods).** The cyclic mode triple and the
  compiled projector of open PR 9236 (the controlled
  population block), guide `exp(α N_flip + (h/2) Σ cos(k x_b) σ)` with
  `α = 0.2 (1 − V/g)`; probe fields `h = 0.15, 0.06, 0.02` below 0.7, below
  0.97 and at the RK point, each paired with `2h` to eliminate the `h⁴`
  term.

None is adopted.

## Theorem 1 — the ring expectation from energies, and the RK floor

1. **Hellmann–Feynman.** `∂E_0/∂V = ⟨N_flip⟩`, so the ring expectation per
   plaquette is `u = −(E_0 − V ∂E_0/∂V)/N_p`. The diagonal `V` term commutes
   with the diagonal modes, so the averaged f-sum rule keeps the form
   `f̄(k) = 2 u s(k)²`, and the energy-only bounds of the companion block
   hold at every `V` with this `u`.
2. **The RK floor.** At `V = g` the uniform superposition over a flip
   component is an exact zero-energy ground state and, with `α = 0`, the
   projector's local energy vanishes identically (landed; the anchor of the
   sweep note). Then `u = n_f`, the flippable density of uniform ice, and
   Cauchy–Schwarz on the averaged measure gives
   `χ̄_T(k) ≥ 2 S̄_T(k)²/f̄(k) = S̄_T(k)²/(n_f s(k)²)`, with `S̄_T` the
   uniform-ice structure factor. That floor is measured independently here
   by sampling uniform ice with loop updates.

Both are exact for the model; evaluated with projector estimates they carry
the estimates' errors. ∎

## Diagnostic — the sweep on 8³

Three seeds per point, 480 walkers, projection 30; probe fields `0.15` below
`V/g = 0.7`, `0.06` below `0.97`, `0.02` at the RK point, each with `2h`; `u`
from a backward step `ΔV = 0.03`.

| `V/g` | `u` | `n_f` | `χ̄(π/4)` | `ω/s` bound at `π/4` | `S̄_T` bound at `π/4` | `χ̄(π/2)` | `ω/s` bound at `π/2` | `χ̄(π/4)/χ̄(π/2)` |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.2885 | 0.3121 | 1.077 ± 0.023 | 1.035 | 0.427 | 1.190 | 0.985 | 0.90 |
| 0.25 | 0.2879 | 0.3039 | 1.494 ± 0.014 | 0.878 | 0.502 | 1.519 | 0.871 | 0.98 |
| 0.5 | 0.2838 | 0.2911 | 2.220 ± 0.011 | 0.715 | 0.608 | 2.004 | 0.753 | 1.11 |
| 0.75 | 0.2758 | 0.2779 | 3.983 ± 0.031 | 0.526 | 0.802 | 2.879 | 0.619 | 1.38 |
| 0.9 | 0.2688 | 0.2693 | 6.968 ± 0.226 | 0.393 | 1.047 | 3.875 | 0.527 | 1.80 |
| 1 | 0.2618 | 0.2618 | 14.47 ± 0.42 | 0.269 | 1.490 | 4.881 | 0.463 | 2.97 |

- **The anchor.** Uniform ice sampled directly by winding-preserving loop
  updates (2000 sweeps) gives `S̄_T = 1.502 ± 0.048` at `π/4` and
  `1.530 ± 0.025` at `π/2`, and flippable density `0.2601`. The floors are
  `14.71` and `4.47`; the projector's susceptibilities `14.47 ± 0.42` and
  `4.88 ± 0.08` meet or exceed them, and its structure-factor bounds
  `1.490 ± 0.021` and `1.599 ± 0.013` lie at or above the sampled values.
  At `π/4` the RK point saturates the chain within errors: its lowest mode
  carries the weight.
- **The pure-ring end.** The `V = 0` row reproduces open PR 9236's 8³ values
  (`χ̄(π/4) = 1.064 ± 0.008`, `χ̄(π/2) = 1.182 ± 0.013`) within one standard
  error, from different seeds.
- **The velocity.** The printed exponent `0.450 ± 0.004` is for the bound
  at the finite momentum `π/4`, where the curvature term keeps `ω/s` finite
  at the RK point (`0.269`). The two-momentum reading above removes most
  of it; its residual `c = 0.12` at the RK point, where a pure quadratic
  mode would give zero, measures what the two-term form leaves out on
  this torus.
- **Sign of the curvature.** At the pure-ring point `ρ²` comes out
  negative (`−0.07`): the bound per unit lattice momentum falls slightly
  from `π/4` to `π/2`. Toward the RK point it turns positive, as the
  quadratic term takes over. ∎

## What this means for the lanes

- **Photon lane.** The energy-only bounds now connect the pure-ring point
  to the exactly known RK point on one torus, through a continuous family
  whose velocity bound vanishes toward the RK point roughly as
  `(1 − V/g)^{1/2}` and whose susceptibility develops the `k`-dependence of
  a quadratic mode only there. Together with open PR 9236 this is the
  finite-torus shape of a photon whose velocity is set by `g − V`; it is
  not a limit statement.
- **What the framework supplied.** The Gauss law, the ring and the RK
  potential are decision points; the projector, the probe and the
  Hellmann–Feynman step are methods.

## What stays open

- The same sweep on 12³ and 16³, and between `0.9` and `1` where the
  velocity bound falls fastest.
- The region bounded by records with the same probe.
- Independent checks of every number here.

## Evidence limits

- **Domain:** one torus, the listed `V` values, the canonical-state flip
  component, the listed estimator settings.
- **Exact versus estimated:** Theorem 1 is exact; every number is a
  projector estimate or a loop-sampled estimate with bin and seed errors of
  no proved coverage; `u` uses a finite backward difference.
- **Readings:** the two-momentum decomposition and its exponent are
  arithmetic on printed estimates under an assumed two-term form, not a
  fitted law of the model.

## Prior art

Rokhsar and Kivelson 1988; Moessner and Sondhi 2003 and Hermele, Fisher
and Balents 2004 (the photon velocity vanishing at the RK point); Shannon,
Sikora, Pollmann, Penc and Fulde 2012; Benton, Sikora and Shannon 2012;
Hellmann 1937 and Feynman 1939. All cited as prior art, not as premises.

## Checks

The runner has 3 checks and all pass in about 16 minutes, single-threaded.

| Check | Result |
|---|---|
| RK anchor | Energy zero on every block; `u` within 0.01 of the sampled flippable density; susceptibilities at or above the uniform-ice floors within 3 standard errors; structure-factor bounds within 3 standard errors plus 5 % of the sampled uniform-ice values. |
| The sweep | Six `V` values, two momenta, errors below 25 %; the table. |
| Velocity and quadratic mode | Reported: the exponent at `π/4` and the susceptibility ratios. |

## Independent check

None yet. The runner was run once through the cache tool; seeded Monte
Carlo reproduces its numbers.

## What this does not do

- It adopts no clause, Gauss law, potential or method.
- It claims no transition point, photon law, velocity or limit; the
  evaluated bounds are estimates of bounds on one torus.
