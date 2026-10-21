---
claim_id: record_source_as_edge_deposits_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Plane-wave check that step and chord deposits sum to the spacetime dust tensor on a supplied six-direction walk, and the linear-algebra fact that D4-carrier edge outer products span symmetric 4x4 tensors; no field equation, edge-length dynamics, coupling value or physical identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/record_source_as_edge_deposits_2026_10_21.py
---

# The record source as deposits on edges

Claim type: bounded_theorem.
Primary runner: `scripts/record_source_as_edge_deposits_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, builds a record source from relay steps and turns. This note recasts it as deposits on edges, which is the variable a geometry carrier responds to. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the constructions below.

## Steps and chords

In one tick a relay moves one block along d. Take that as the spacetime vector s = (1, d). Each tick the relay deposits its energy eps on s, and each turn from d to d' deposits -1/4 on the spatial chord c = d' - d. The outer products of these vectors are then summed. For a reversal, c = -2d and the chord term is -d d.

For plane waves of the six-direction walk at three momenta, the sum equals eps u u with u = (1, v) to rounding. That one tensor contains the energy eps, the momentum eps v and the stress eps v v of moving matter; the step deposits alone miss. The source therefore needs no separate energy, momentum and stress rules, only deposits on two kinds of vector.

## Carrier edges

The D4 carrier's 24 edge vectors place (+-1, +-1) on two of the four spacetime axes. Their outer products span all ten components of a symmetric 4x4 tensor. Any record source can therefore be written as a set of deposits on carrier edges. A geometry described by edge lengths then couples to the source through those deposits. A symmetric tensor response is what such a geometry gives; it is not a separate assumption.

## Scope

The walk, the coin, the band selection and the identification of a tick step with (1, d) are supplied. No field equation, edge-length dynamics, coupling value or physical identification is established.
