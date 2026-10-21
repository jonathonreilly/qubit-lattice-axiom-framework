---
claim_id: one_qubit_split_step_walk_relay_source_and_doublers_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Plane-wave checks of the burn-and-turn source on a supplied one-qubit-per-site split-step walk on Z^3, and a finite Brillouin-zone scan of its gapless points; no physical matter content, derivation of the update or exact cubic covariance."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_qubit_split_step_walk_relay_source_and_doublers_2026_10_21.py
---

# One-qubit split-step walk: relay source and doublers

Claim type: bounded_theorem.
Primary runner: `scripts/one_qubit_split_step_walk_relay_source_and_doublers_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and leaves the tick update of the odds open. This note examines one supplied candidate that uses exactly one qubit per site, matching the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). In each tick the site qubit takes three nearest-neighbour substeps, along x, then y, then z. In substep i its sigma_i = +1 part moves one site toward +i and its sigma_i = -1 part toward -i. A relay's step direction along axis i is then the qubit's sigma_i outcome at substep i, so step directions are not an extra structure.

## Plane waves

For eigenmodes at five momenta, the Born weights of sigma_i at substep i are computed. The mean step per axis equals the group velocity to 1e-8 or better, as the eigenphase derivative of the product of substeps implies. Take the axis signs as independent with those weights, the redraw probability as twice the energy, and the turn stress as -(d'-d)(d'-d)/4. Burns plus turns then equal energy times v v, shear included, to rounding. Energy over |k| lies within 3 percent of one on the sampled directions at |k| up to .2.

## Doublers

A 48^3 scan of the Brillouin zone finds eight zero-quasi-energy cones, four of each chirality, so the chiralities cancel. The supplied update therefore describes doubled, not chiral, massless fermions at low energy. That agrees with doubling theorems for local lattice dynamics. There are further gapless points at quasi-energy pi.

## Further limits

The fixed substep order breaks exact cubic covariance at the lattice scale. A Dirac mass needs opposite-chirality components to mix. In this one-qubit update the opposite-chirality cones sit at different momenta, so a mass term must couple across momentum, as in staggered constructions. Each tick displaces every component by (+-1, +-1, +-1), which preserves the parities of x-y and y-z. The update therefore splits into four non-interacting sublattice copies at tick boundaries.

## Scope

The walk, substep order, momenta, scan grid and chirality evaluation are supplied. No physical matter content, derivation of the update or exact cubic covariance is established.
