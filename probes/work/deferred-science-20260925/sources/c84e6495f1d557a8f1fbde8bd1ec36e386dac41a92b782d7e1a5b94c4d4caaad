---
claim_id: ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_continuously_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic ice) and the plaquette clause H = -g sum_p (U_p + U_p^dag) + V sum_p n_p, g = 1, V/g from 1 (Rokhsar-Kivelson) to 0 (pure ring) (open PRs 9066, 9072, 9146); the guided continuous-time projector Monte Carlo of open PR 9148 with guiding exponent alpha = 0.2 (1 - V/g), the forward-walking weight map of open PR 9163 at lag 2, walkers in the zero-winding sector of open PR 9153. Exact: at V = g the uniform superposition over a flip component is a zero-energy ground state and with alpha = 0 the local energy vanishes identically, so the projector is the symmetric continuous-time flip walk whose stationary law is uniform; the runner finds max |E(tau)| = 0 exactly and the sum rule of open PR 9163 exact per block. Finite diagnostics (120 walkers; 4^3 projection 40, 6^3 projection 32; ten-bin errors): at V = g the axis star T/2 is 1.521 +- 0.012 (4^3) and 1.527 +- 0.012 (6^3) and the corner star 3.07 +- 0.03 and 3.02 +- 0.03, against zero-winding-sector uniform samples 1.60 (4^3, 2.3 standard errors) and 1.52 (6^3) and 3.01, 3.00; along V = 1, 0.75, 0.5, 0.25, 0 on 4^3 the axis weight per polarisation falls 1.521, 1.185, 0.984, 0.857, 0.726 (+- 0.006-0.018) and the corner weight rises 3.07, 3.53, 3.85, 4.97, 7.59 (+- 0.03-0.60), monotone within errors and resolved between the end points at 37 and 7.5 standard errors; the ring expectation per plaquette u_0 rises 0.266, 0.278, 0.286, 0.291, 0.292 and the pure flippable density 0.266, 0.280, 0.292, 0.305, 0.321; on 6^3 at V = 1, 0.5, 0 the axis weight is 1.527, 0.720, 0.610 (+- 0.012-0.022) and the corner 3.02, 4.00, 6.55 (+- 0.03-0.74), the V = 0 axis value 1.7 standard errors above open PR 9161's 0.557 +- 0.022. No phase, no transition point and no thermodynamic limit is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_2026_09_24.py
---

# From the RK point to the pure-ring point the transverse weight moves to the zone corner continuously

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** an exact anchor with finite numerical diagnostics under supplied decision points; unaudited.

## Result

Open PR 9163 found that the pure-ring ground state (`V = 0`) carries a
third of the uniform-ice transverse weight at the smallest momentum and
twice it at the zone corner `(π,π,π)`, while the uniform-ice (RK) state is
flat. This note follows the weight map along `V/g` from the RK point to the
pure-ring point.
- **The RK point anchors the sweep exactly (Theorem 1).** At `V = g` the
  clause is a sum of projectors with the uniform superposition as an exact
  zero-energy ground state; with the guiding exponent at zero the local
  energy of every configuration is identically zero, so the projector is
  the symmetric flip walk and samples the uniform ensemble of the flip
  component. The runner finds `max |E(τ)| = 0` exactly, the sum rule exact
  per block, and every star back at the uniform value: axis `1.521 ± 0.012`
  and `1.527 ± 0.012`, corner `3.07 ± 0.03` and `3.02 ± 0.03` on 4³ and 6³
  (the 4³ axis sits 2.3 standard errors below the loop-sampled sector
  value 1.60; the 6³ values agree).
- **The weight moves continuously and monotonically.** On 4³ along
  `V = 1, 0.75, 0.5, 0.25, 0` the axis weight per polarisation falls
  `1.521, 1.185, 0.984, 0.857, 0.726` and the corner weight rises
  `3.07, 3.53, 3.85, 4.97, 7.59`, each step in the same direction within
  errors and the end points 37 and 7.5 standard errors apart. On 6³ at
  `V = 1, 0.5, 0`: axis `1.527, 0.720, 0.610`, corner `3.02, 4.00, 6.55`.
  The corner's rise accelerates toward `V = 0`; the axis's fall is fastest
  near the RK point.
- **The ring expectation barely moves while the map reorganises.**
  `u_0 = ⟨U + U†⟩` per plaquette rises only from 0.266 to 0.292 and the
  flippable density from 0.266 to 0.321 across the sweep, while the axis
  weight halves and the corner weight more than doubles: the redistribution
  is a correlation effect of the ring dynamics, not a change in how many
  plaquettes resonate.

Supplied model, finite diagnostics: no phase, no transition point and no
thermodynamic limit is claimed. What the sweep shows is that the two ends
of the zone are connected smoothly by the ring dynamics, with the RK point
as an exact check of the whole estimator chain.

## Setting and decision points

- **D-gauss, D-roles, D-ring, D-RK (open PRs 9066, 9072, 9146).** Link qubits at
  link sites of the doubled lattice; the exact vertex Gauss law; the
  plaquette clause `H = −g Σ_p (U_p + U_p†) + V Σ_p n_p`, with `n_p` the
  flippable indicator, `g = 1`. `V/g` runs from 1 (the Rokhsar–Kivelson
  point) to 0 (the pure-ring point of open PRs 9146–9163).
- **The projector and the pure estimator (methods).** The guided
  continuous-time Green's function Monte Carlo of open PR 9148 with guiding
  function `exp(α N_flip)`, `α = 0.2 (1 − V/g)`, walkers in the zero-winding
  sector of open PR 9153, the lineage estimator of open PR 9161 at forward
  lag 2 carrying the full weight map of open PR 9163 and the flippable count.
- **The observables (method).** The transverse weight `T(k) = Σ_a |O_a(k)|²`
  by star of the cubic group (open PR 9163): the smallest axis star
  `(1,0,0)` (per polarisation, `T/2`) and the zone corner `(π,π,π)`; the
  ring expectation per plaquette `u_0 = ⟨U + U†⟩ = −(e_0 − V n_f)` from the
  mixed energy per plaquette `e_0` and the pure flippable density `n_f`.

None is adopted.

## Theorem 1 — the RK point is exact for the projector

At `V = g` the clause is `Σ_p (n_p − U_p − U_p†)`, a sum of projectors onto
the antisymmetric combination of each flippable plaquette's two
orientations, so `H ≥ 0`, and on any flip component the uniform
superposition of its configurations is annihilated by every term: it is an
exact zero-energy ground state (Rokhsar and Kivelson 1988). With `α = 0` the
guiding function is uniform and the local energy of every configuration is
`V N_flip − Σ_{p flippable} 1 = 0` identically, so the walkers carry unit
weights, branch nowhere, and perform the continuous-time random walk that
flips a uniformly chosen flippable plaquette at rate one per flippable
plaquette. That walk's stationary distribution on a flip component is
uniform (the flip graph is regular in the sense that each directed flip has
its reverse at the same rate), so the forward-walking estimator at any lag
is an estimator of the uniform ice ensemble of the component: every star of
the weight map must return to the uniform value, the energy is exactly
zero, and the sum rule of open PR 9163 holds per block. The runner checks
the energy to 10⁻⁹ and the stars within statistical errors against a
winding-preserving loop sample of the same sector. ∎

The RK point therefore anchors the sweep at a value every estimator must
reproduce; deviations at `V < g` are the ring dynamics, not the method.

## Diagnostic — the sweep on 4³ and 6³

Walkers (120) start in the zero-winding sector from the canonical ice state
of open PR 9153 after winding-preserving loop equilibration with the
guiding function `exp(α N_flip)`, `α = 0.2 (1 − V)`; projection `τ = 40`
(4³) and 32 (6³) in blocks of 0.05, the first 8 discarded; the weight map
and the flippable count ride along the lineages and are read at forward
lag 2. The sector-uniform reference is a winding-preserving loop sample of
the same sector at `V = g` (its 4³ axis value 1.60 exceeds the
unconstrained 1.51 of open PR 9163 because the winding weight of the
`(0,0,0)` star is redistributed by the sum rule). `T/2` is per polarisation
on the axis star; `T` is the corner star `(π,π,π)`.

| `V/g` | torus | `e_0` per plaquette | `u_0` | `n_f` (pure) | axis `T/2` | corner `T` |
|---|---|---|---|---|---|---|
| 1 | 4³ | 0 (exact) | 0.266 | 0.266 | 1.521 ± 0.012 | 3.07 ± 0.03 |
| 0.75 | 4³ | −0.0683 | 0.278 | 0.280 | 1.185 ± 0.015 | 3.53 ± 0.06 |
| 0.5 | 4³ | −0.1398 | 0.286 | 0.292 | 0.984 ± 0.006 | 3.85 ± 0.07 |
| 0.25 | 4³ | −0.2145 | 0.291 | 0.305 | 0.857 ± 0.013 | 4.97 ± 0.12 |
| 0 | 4³ | −0.2920 | 0.292 | 0.321 | 0.726 ± 0.018 | 7.59 ± 0.60 |
| 1 | 6³ | 0 (exact) | 0.261 | 0.261 | 1.527 ± 0.012 | 3.02 ± 0.03 |
| 0.5 | 6³ | −0.1385 | 0.283 | 0.289 | 0.720 ± 0.018 | 4.00 ± 0.17 |
| 0 | 6³ | −0.2887 | 0.289 | 0.312 | 0.610 ± 0.022 | 6.55 ± 0.74 |

- **Anchor.** At `V = g` the energy is zero to the last digit on every
  block (no branching, unit weights), the sum rule holds to `10⁻¹⁵`, and
  the flippable density matches the sector-uniform sample. The 4³ axis
  value sits 2.3 standard errors below the loop sample; on 6³ the two
  agree. With the flip walk provably uniform on its component, a
  persistent 4³ offset would mean the loop sample and the walkers weight
  the sector's flip components differently; at this precision it is a
  fluctuation to be rechecked with another seed.
- **Monotone.** Every consecutive pair of axis values falls and every
  consecutive pair of corner values rises within two combined standard
  errors; the end points differ by 37 (axis) and 7.5 (corner) standard
  errors on 4³.
- **Two ends, one motion.** The axis weight loses most near the RK point
  (1.52 → 1.19 in the first quarter of the sweep) and the corner gains most
  near the pure-ring point (4.97 → 7.59 in the last quarter): the
  long-wavelength suppression switches on as soon as the ring term
  outweighs the RK potential, and the short-range `(π,π,π)` correlation
  builds up as the potential vanishes.
- **Consistency with the earlier blocks.** The `V = 0` axis values
  `0.726 ± 0.018` (4³) and `0.610 ± 0.022` (6³) are 1.5 and 1.7 standard
  errors above open PR 9161's `0.692 ± 0.013` and `0.557 ± 0.022`; the
  corner values `7.59 ± 0.60` and `6.55 ± 0.74` are 2.1 and 0.5 standard
  errors above open PR 9163's `6.13 ± 0.36` and `6.12 ± 0.53`. The corner
  is the slowest observable to converge (its error at `V = 0` is ten times
  the RK one); the ten-bin errors of a 32–40 projection may understate it.
  The 6³ energies at `V = 0` (−0.2887) and `V = 0.5` sit within the spread
  of open PRs 9148–9163. ∎

## What this means for the lanes

- **Photon lane.** The RK point is now an exact anchor for the whole
  estimator chain (projector, forward walking, weight map, sum rule): the
  method reproduces the known state to the last digit in energy and within
  errors in the map. The redistribution found at `V = 0` in open PRs 9161
  and 9163 switches on continuously from the RK point, fastest at the two
  ends of the sweep; nothing in the map jumps between `V = g` and `V = 0`
  on these tori, which is what a single liquid regime connected to the RK
  point would show and what a transition between them would not
  (finite diagnostic, no phase claim).
- **What the framework supplied.** The Gauss law, the ring, the RK
  potential and the sweep in `V/g` are decision points; the estimators are
  methods.

## What stays open

- The 4³ RK axis offset (2.3 standard errors) with another seed and a
  longer projection.
- The corner's convergence and its growth with `L` at fixed `V`, where
  open PR 9163 found none between 4³ and 6³ at `V = 0`.
- The sweep beyond the RK point (`V > g`, toward frozen states) and below
  `V = 0` (`V < 0`, where the ring term is aided).

## Prior art

Rokhsar and Kivelson 1988 (the sum-of-projectors point and its uniform
ground state); Trivedi and Ceperley 1990 (Green's function Monte Carlo and
forward walking); Hermele, Fisher and Balents 2004. All cited as prior art,
not as premises.

## Checks

The runner has 3 checks and all pass in about 3.5 minutes, single-threaded.

| Check | Result |
|---|---|
| The RK point | `max |E(τ)| = 0`; axis, corner and flippable density within 3 standard errors of the sector-uniform sample; sum rule exact per block. |
| 4³ sweep | Axis falls and corner rises monotonically within errors; end points 37 and 7.5 standard errors apart; the table. |
| 6³ sweep | The same ordering; the `V = 0` axis value within 3 standard errors of open PR 9161. |

## Independent check

None yet. The runner was rerun from a clean shell to write the cache;
seeded Monte Carlo reproduces the numbers. The `V = 0` rows are a further
seed of open PRs 9161 and 9163.

## What this does not do

- It adopts no clause, Gauss law, potential or method.
- It claims no phase, no transition and no thermodynamic limit; the sweep
  is a finite-torus diagnostic of a supplied model with ten-bin standard
  errors at one forward lag.
