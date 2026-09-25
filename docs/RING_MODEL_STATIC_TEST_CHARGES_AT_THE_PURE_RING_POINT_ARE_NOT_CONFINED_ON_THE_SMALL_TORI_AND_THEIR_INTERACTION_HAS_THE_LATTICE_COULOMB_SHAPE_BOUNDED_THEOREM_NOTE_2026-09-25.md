---
claim_id: ring_model_static_test_charges_at_the_pure_ring_point_are_not_confined_on_the_small_tori_and_their_interaction_has_the_lattice_coulomb_shape_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit ice model with the vertex Gauss law exact except at two static test charges (divergence +-2 for charge 1, +-4 for charge 2) and the clause -g (U + U^dag) + V N_flip, g = 1, on L^3 tori; pairs made by reversing directed strings in the canonical zero-winding state; the compiled projector of open PR 9236 (1920 walkers, projection 50, two to four seeds). Exact: plaquette flips conserve every vertex divergence, so the charges are static; at the RK point every flip component has ground energy zero, so the pair energy does not depend on the separation there; checked on the 2^3 torus (6000 charged configurations, a 508-state flip component, RK ground energy 1.6e-15, projector energy identically zero; pure-ring ground energy -7.85688 against the projector's -7.8576 +- 0.0037). Finite estimates at the pure-ring point: on 8^3 the pair energy above separation 1 is +0.269 +- 0.076, +0.367 +- 0.062, +0.262 +- 0.082 at separations 2, 3, 4, fitted by the torus lattice Coulomb shape 4U[G(1) - G(d)] with U = 1.48 +- 0.20 (chi^2 1.6 for 2 degrees of freedom) and poorly by a linear string (chi^2 8.6); relative to separation 2 the data give U = 0.9 +- 1.0, and the excess of the separation-1 fit over 1/chi = 0.85-0.94 (open PR 9236) is carried by the adjacent pair; the separation energy E(L/2) - E(1) is 0.312 +- 0.011, 0.279 +- 0.028, 0.262 +- 0.082 on 4^3, 6^3, 8^3 (12^3: 0.48 +- 0.57, unresolved), so a string tension above about 0.05 per link is inconsistent with these tori; a charge-2 pair gives 0.742 +- 0.070 at separation 4 (2.8 +- 0.9 times charge 1; linear response 4); at V/g = 0.5 the charge-1 separation energy is 0.69 +- 0.23 of its V = 0 value (1/chi ratio 0.49). No confinement, deconfinement, Coulomb law or limit is claimed beyond these finite tori."
upstream_dependencies:
  - minimal_axioms
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
  - ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_static_test_charges_separation_energy_against_the_lattice_coulomb_law_2026_09_25.py
---

# Static test charges at the pure-ring point are not confined on the small tori, and their interaction has the lattice Coulomb shape

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model with finite projector estimates; unaudited.

## Result

Open PR 9236 bounded the pure-ring photon with energies alone and found the
transverse susceptibility `χ̄ ≈ 1.1`. In the Gaussian comparator the same
coupling `U = 1/χ̄` sets the static interaction of charges, and a
deconfined phase keeps that interaction bounded as the charges separate,
where a confined one grows linearly. This block measures the ground energy
of static test-charge pairs, again from energies alone.
- **Exact (Theorem 1).** Plaquette flips conserve every vertex charge, so a
  pair at separation `d` has its own flip component and ground energy
  `E(d)`. At the RK point every component has ground energy zero, so there
  the pair has no energetic interaction at all.
- **Not confined on these tori.** The energy to pull a charge-1 pair from
  neighbours to the far side of the torus is `0.312 ± 0.011`,
  `0.279 ± 0.028`, `0.262 ± 0.082` on 4³, 6³, 8³: level, not growing. A string
  tension above about `0.05` per link is inconsistent with these tori.
- **The shape is Coulomb.** On 8³ the torus lattice Coulomb shape
  `4U[G(1) − G(d)]` fits `E(d) − E(1)` with `χ² = 1.6` for two degrees of
  freedom; a linear string gives `χ² = 8.6`.
- **The strength agrees with `1/χ̄` only beyond the core.** The fit gives
  `U = 1.48 ± 0.20`, 2.7 standard errors above `1/χ̄ = 0.85–0.94`; the excess
  is carried by the adjacent pair, bound more strongly than the comparator
  gives. Measured from separation 2, the data give `U = 0.9 ± 1.0`:
  consistent, but uninformative.
- **Charge 2 and the RK potential point the same way, loosely.** A charge-2
  pair costs `0.742 ± 0.070` to separate, `2.8 ± 0.9` times the charge-1
  value where linear response gives 4, and its effective `U = 0.79` sits
  near `1/χ̄`. At `V/g = 0.5` the charge-1 separation energy falls to
  `0.69 ± 0.23` of its pure-ring value, against the `0.49` that the
  susceptibilities of open PR 9239 predict.

Supplied model, finite estimates: no confinement, deconfinement, Coulomb
law or limit is claimed beyond these tori. What they show is that the
static charges behave as the photon bounds of open PR 9236 lead one to
expect in a Coulomb phase, with a core that the Gaussian comparator does
not describe.

## Setting and decision points

- **D-gauss with two test charges, D-roles, D-ring (landed).** The exact
  vertex Gauss law holds at every vertex except two: one with four arrows
  out and two in (divergence `+2`, charge `+1`) and one with two out and four
  in (charge `−1`); for charge 2, five and one. The clause is
  `−g (U + U†) + V N_flip`, `g = 1`, on `L³` tori.
- **The configurations (method).** In the canonical zero-winding ice state
  of the landed winding-sector note, one directed string of arrows from
  `A = (0,0,0)` to `B = (d,0,0)` is reversed (two strings for charge 2,
  each found by a breadth-first search of the arrow graph). Each
  separation has its own flip component; walkers start from that
  configuration and relax under the projector.
- **The projector (method).** The compiled projector of open PR 9236,
  guide `exp(0.2 (1 − V/g) N_flip)`, fixed populations of 1920 walkers,
  projection 50; the mixed energy estimator is exact for any guide.

None is adopted.

## Theorem 1 — static charges, and the RK point

1. **The charges are static.** A plaquette flip reverses four links around
   one plaquette; at each of its corners one link turns in and one turns
   out, so every vertex keeps its divergence. The flip component of a
   configuration therefore has fixed charges, and the ground energy `E(d)`
   of a pair at separation `d` is well defined.
2. **No energetic interaction at the RK point.** At `V = g` the clause is a
   sum of projectors and the uniform superposition over any flip component
   is annihilated by every term. So `E(d) = 0` for every separation and
   every charge: whatever interaction the pair has at the RK point is
   entropic, not energetic.
3. **The Gaussian comparator's law.** In the lattice Maxwell comparator of
   the landed note
   `GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
   a static pair of divergence `±2Q` costs `4Q² U [G(0) − G(d)]` above
   separated charges, where `G` is the lattice Green function of the torus
   without its zero mode and `U` is the coupling whose inverse is the
   transverse susceptibility, `χ̄ = 1/U`. So the comparator predicts
   `E(d) − E(1) = 4Q² U [G(1) − G(d)]`, bounded as `d` grows, with the same
   `U` open PR 9236 measured through the transverse response.

The runner checks the first two statements exactly on the 2³ torus. ∎

## Diagnostic 1 — exact control

On the 2³ torus with charges `−1` at `(0,0,0)` and `+1` at `(1,0,0)`: 6000
configurations carry these charges; the flip component of the constructed
one has 508 states, all with the same charges. The RK clause's lowest
eigenvalue on that component is `1.6·10⁻¹⁵` and the projector's local
energy vanishes on every block; at the pure-ring point the exact ground
energy `−7.85688` against the projector's `−7.8576 ± 0.0037`.

## Diagnostic 2 — the pair on 8³

Four seeds per separation; errors are the larger of the seed scatter and
the mean bin error over the square root of the seed count.

| separation `d` | `E(d) − E(1)` | Coulomb shape `4[G(1) − G(d)]` | `U = 0.9` prediction |
|---|---|---|---|
| 2 | +0.269 ± 0.076 | 0.1684 | 0.152 |
| 3 | +0.367 ± 0.062 | 0.2210 | 0.199 |
| 4 | +0.262 ± 0.082 | 0.2340 | 0.211 |

The torus Green function without its zero mode has `G(0) = 0.2246` and
`G(d,0,0) = 0.0583, 0.0162, 0.0030, −0.0002` for `d = 1 … 4`. The Coulomb fit
through separation 1 gives `U = 1.48 ± 0.20` (`χ² = 1.6`); a linear string
`σ (d − 1)` gives `σ = 0.139` with `χ² = 8.6`. Differences from separation 2,
`E(3) − E(2) = 0.10 ± 0.08` and `E(4) − E(2) = −0.01 ± 0.09` (arithmetic on the
printed values, bin errors combined without their correlation), give
`U = 0.9 ± 1.0` against the Coulomb shape.

## Diagnostic 3 — the separation energy against the torus

| torus | `E(L/2) − E(1)` | seeds | Coulomb with `U = 1.48` |
|---|---|---|---|
| 4³ | +0.312 ± 0.011 | 4 | 0.175 |
| 6³ | +0.279 ± 0.028 | 4 | 0.289 |
| 8³ | +0.262 ± 0.082 | 4 | 0.346 |
| 12³ | +0.475 ± 0.572 | 2 | 0.401 |

A string tension `σ` would add `σ (L/2 − 1)`: from 4³ to 8³ that is `2σ`. The
measured change is `−0.05 ± 0.08`, so `σ` above about `0.05` per link is
inconsistent with these tori. The 12³ pair energies scatter by about 0.8
between two seeds at 1920 walkers and resolve nothing.

## Diagnostic 4 — charge 2, and the RK potential halfway

- **Charge 2 on 8³.** `E(4) − E(1) = 0.742 ± 0.070` for a pair of divergence
  `±4`, three seeds; `2.8 ± 0.9` times the charge-1 value, where the
  Gaussian comparator gives 4; its effective `U = 0.742/(16 · 0.0585) = 0.79`.
  A vertex of charge 2 has five of its six arrows pointing the same way, so
  the field at the core is saturated and the comparator's unbounded field
  overstates its cost.
- **`V/g = 0.5` on 8³.** The charge-1 separation energy `0.181 ± 0.023`, three
  seeds, is `0.69 ± 0.23` of the `V = 0` value; the susceptibilities of open
  PR 9239 give `1.077/2.220 = 0.49` if `U = 1/χ̄` at both points. ∎

## What this means for the lanes

- **Photon and charge lane.** On these tori the pure-ring point shows the
  two faces of a Coulomb phase from energies alone: a transverse mode
  whose energy is bounded linearly in the momentum (open PR 9236) and
  static charges whose separation energy stays bounded with the Coulomb
  shape. The strength of the charge interaction beyond the core is
  consistent with the transverse susceptibility but not yet measured to
  better than its own size; the core binds the adjacent pair more strongly
  than the Gaussian comparator.
- **What the framework supplied.** The Gauss law with test charges, the
  ring and the RK potential are decision points; the strings, the
  projector and the comparator are methods.

## What stays open

- The charge interaction beyond the core at a precision that tests
  `U = 1/χ̄` (separations 2–6 on 12³ with many more seeds or walkers).
- The 12³ and larger separation energies, where the population effect on
  single energies is large.
- The adjacent-pair core, and charge 2, against a non-Gaussian account.

## Evidence limits

- **Domain:** the listed tori, separations along one axis, the flip
  components of the constructed configurations, the estimator settings.
- **Exact versus estimated:** Theorem 1 and the 2³ numbers are exact; all
  larger-torus numbers are projector estimates whose errors have no proved
  coverage, and the 12³ ones are dominated by seed scatter.
- **Fits:** the Coulomb and linear fits are one-parameter forms, the
  comparator's shape and a string; neither is a law of the model.

## Prior art

Rokhsar and Kivelson 1988; Hermele, Fisher and Balents 2004; Castelnovo,
Moessner and Sondhi 2008 (emergent charges in ice); Shannon, Sikora,
Pollmann, Penc and Fulde 2012; Kogut 1979 (confinement and string tension
on lattices). All cited as prior art, not as premises.

## Checks

The runner has 4 checks and all pass in about 50 minutes, single-threaded.

| Check | Result |
|---|---|
| Exact 2³ control | Charges conserved on a 508-state component; RK energy zero; pure-ring energy within errors. |
| Pair on 8³ | Reported: the table, the Coulomb and linear fits. |
| Size | Reported: the separation energy on 4³–12³. |
| Charge 2 and `V/g = 0.5` | Reported. |

## Independent check

None yet. The runner was run once through the cache tool; seeded Monte
Carlo reproduces its numbers.

## What this does not do

- It adopts no clause, Gauss law, source or method.
- It claims no confinement, deconfinement, Coulomb law, coupling or limit
  beyond these finite tori.
