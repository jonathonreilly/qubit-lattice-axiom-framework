# Native collisions change the finite neutral-feature problem

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_finite_feature_collision.py](../scripts/native_finite_feature_collision.py)

The native bound-end mechanism does not by itself give a stable finite particle.
For a long square feature, the two endpoints reproduce the derived collective
bands locally. But at short length, the same one-qubit Hamiltonian reconnects
that feature to mobile singleton defects. The resulting escape continuum
contains the paired-end band edge itself.

The exact separated-end dispersion gives relative kinetic coefficient
2Jz lambda/sqrt3. Combined with the previously derived bulk cost Jz lambda4/16,
it suggests a length scale proportional to lambda^-1 and an energy scale
proportional to Jz lambda3. These are conditional balances, not an Airy spectrum:
collision scattering, earlier K2 energy shifts and the full channel dynamics
must be retained.

There is also a constructive result for coupling. The original uniform
longitudinal distance-two readout obeys exactly

    C_excess = -4 N + 4 A,

where N counts broken longitudinal bonds and A counts adjacent pairs of those
bonds. It is constant on separated endpoint configurations but changes at native
collisions. A checked first-order move has Delta C=8. Thus the existing readout
resolves contact dynamics without adding a scalar interaction or coupling
constant. A particular spectral line or physical detector coupling is not yet
established.

The complete proof and failed route (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9773/FINITE_FEATURE_COLLISION_PROOF.md`)
distinguish the layer-neutral infinite-volume continuum from neutral quasimodes
on large even tori. Connectivity does not prove radiation: interference could
protect an embedded state. Native collision scattering is the next unresolved
calculation. No full-H particle, fermion, gravitational scalar, cosmological
identification or empirical validation is claimed.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.
