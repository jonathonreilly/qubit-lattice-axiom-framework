---
claim_id: round_four_synthesis_the_pure_ring_photon_from_energies_alone_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "A synthesis of four open blocks (open PRs 9236, 9239, 9244, 9247) on the supplied link-qubit ice model with the ring clause, all finite estimates of exact inequalities and none adopted. The runner recomputes one exact identity per block with its own code: on the exact 2^3 component the cyclic-triple f-sum average equals 2 u s^2 (3.008907) and the moment chain reads 2.5173 <= 2.7754 <= 2.8724 <= 2.9728; dE_0/dV equals the ground-state flippable count at V/g = 0.5 (9.006137) and the RK ground energy vanishes; the 508-state component of a charge pair carries fixed charges and has zero RK ground energy; on a 3646-state region bounded by records the Hellmann-Feynman first moment equals the double commutator (1.424504). The finite estimates it quotes (transverse susceptibility 1.04-1.21 from pi/8 to pi/2 on 6^3-16^3; energy bound on the lowest transverse excitation about 1.04 s(k) at the smallest momenta; its softening toward the RK point roughly as (1 - V/g)^(1/2); static charges whose separation energy stays level from 4^3 to 8^3 with the lattice Coulomb shape; a region bounded by records reproducing the torus bound within about 1 %) are those of the blocks with their stated errors. No photon law, phase, limit or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
  - ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
runner: scripts/round_four_synthesis_the_pure_ring_photon_from_energies_alone_2026_09_25.py
---

# Round-four synthesis: the pure-ring photon from energies alone

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** a synthesis of open blocks, exact identities recomputed, finite estimates quoted; unaudited.

## Result

The landed notes on the pure-ring point measured the photon with a
fixed-population projector and forward walking. The landed two-regulator
note then found the walker population, not the torus, steering those
numbers on the larger tori, with forward-walking ancestry collapsing. Four
blocks rebuilt the photon lane on quantities that need only ground-state
energies, whose mixed estimator is exact for any guide. This note collects
what they found and recomputes one exact identity from each.

**The method (open PR 9236).** A compiled projector whose events cost the
same on every torus (70–360 times faster on 8³–16³), and the transverse
susceptibility `χ̄_T(k)` read from energies in a weak probe field on a
cyclic mode triple that meets each plaquette orientation once. With the
exact averaged f-sum rule `f̄ = 2us²`, log-convexity of the spectral moments
bounds the lowest transverse excitation by `2 s(k)(u/χ̄)^{1/2}` and the
structure factor by `s(k)(uχ̄)^{1/2}`.

**What the four blocks found (finite estimates, stated errors in each).**
- **The photon bound (9236).** `χ̄_T = 1.04–1.21` from `π/8` to `π/2` on
  6³–16³, not growing at small momentum; hence the lowest transverse
  excitation is bounded by about `1.04 s(k)` and the structure factor by
  about `0.54 s(k)` at the smallest momenta. A residual constant in the
  structure factor and a quadratic mode are inconsistent with these
  estimates; the earlier forward-walking values on 12³ and 16³ lie 3–10
  standard errors above the bound, while on 4³ and 6³ they sit at it.
- **Toward the RK point (9239).** Along `V/g` on 8³ the susceptibility rises
  from `1.08` to `14.5`, the velocity bound falls roughly as
  `(1 − V/g)^{1/2}`, the `k`-dependence of a quadratic mode appears only at
  the RK point, and there the projector reproduces uniform ice, its
  susceptibility on the exact floor set by directly sampled uniform ice.
- **Static charges (9244).** Test charges are static under the ring and
  have zero energy at the RK point for every separation. At the pure-ring
  point the energy to separate a pair stays level from 4³ to 8³, so a
  string tension above about `0.05` per link is inconsistent with these
  tori, and on 8³ the pair energy has the lattice Coulomb shape; its fitted
  strength exceeds `1/χ̄` through the adjacent-pair core.
- **The region regulator (9247).** Inside a region bounded by records the
  same energy-only bound matches the torus within about 1 % at the
  smallest standing wave for two record frames and two sizes; the records
  reduce only the response amplitude near the boundary.

**One picture, on these tori.** The pure-ring point has a gapless
transverse mode bounded linearly in the momentum with slope near one, a
structure factor that vanishes at least linearly, charges that are not
confined, a velocity that softens toward the RK point, and an energy scale
that does not depend on the regulator. That is the finite-torus shape of
the Coulomb phase of the supplied model; no limit or phase is claimed.

## Recomputed identities (the runner)

| Block | Identity recomputed | Result |
|---|---|---|
| 9236 | cyclic-triple f-sum average `= 2us²`; moment chain on the exact 2³ component | 3.008907 both sides; 2.5173 ≤ 2.7754 ≤ 2.8724 ≤ 2.9728 |
| 9239 | `∂E_0/∂V = ⟨N_flip⟩` at `V/g = 0.5`; zero RK ground energy | 9.006137 both sides; −2.3·10⁻¹⁵ |
| 9244 | a charge pair's component keeps its charges; zero RK ground energy | 508 states, charges `−2, 0, 2`; 1.6·10⁻¹⁵ |
| 9247 | Hellmann–Feynman first moment `=` double commutator in a region bounded by records | 3646 states; 1.424504 both |
| — | the register | nine entries |

## Lessons

- **Energies before lineages.** When forward walking's ancestry collapses,
  quantities built from ground-state energies — susceptibilities through
  probe fields, first moments through Hellmann–Feynman derivatives,
  charge interactions — avoid it, and moment inequalities turn them into
  bounds.
- **Cover the orientations.** A single mode's f-sum needs its own
  plaquette orientation; a mode set that meets each orientation once
  makes the averaged identity exact without symmetry.
- **Check the arithmetic on exact cases.** This runner's first version
  miscounted flippable plaquettes by a misplaced parenthesis and overflowed
  64-bit codes on the region; the exact identities caught both.

## What stays open

- Tori beyond 16³, which need smaller reconfiguration steps or a better
  guide; the charge interaction beyond the core at a precision that tests
  `U = 1/χ̄`; larger regions bounded by records.
- Independent checks of every block.

## Prior art

As in the blocks: Feynman 1954; Pitaevskii and Stringari 2003; Hellmann
1937 and Feynman 1939; Trivedi and Ceperley 1990; Calandra Buonaura and
Sorella 1998; Rokhsar and Kivelson 1988; Moessner and Sondhi 2003; Hermele,
Fisher and Balents 2004; Castelnovo, Moessner and Sondhi 2008; Shannon et
al. 2012; Benton, Sikora and Shannon 2012. All cited as prior art, not as
premises.

## Checks

The runner has 5 checks and all pass in about one second; the table above
lists them.

## Independent check

None yet. The identities are recomputed with code independent of the
blocks' runners; the finite numbers are quoted from the blocks' caches.

## What this does not do

- It adopts no clause, Gauss law, record frame, method or comparison.
- It claims no photon law, phase, limit or physical identification.
