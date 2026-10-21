---
claim_id: scale_ladder_gravity_removed_sites_repel_and_blueshift_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite diagnostics of a supplied 2D lattice Klein-Gordon wave with sites removed from the flow inside a disk: packet shifts and the lowest confined mode; no gravity field, long-range response, physical identification or derivation of the record-removal clause."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/scale_ladder_gravity_removed_sites_repel_and_blueshift_2026_10_21.py
---

# Removed sites repel packets and raise confined frequencies

Claim type: bounded_theorem.
Primary runner: `scripts/scale_ladder_gravity_removed_sites_repel_and_blueshift_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, records the clause "When a record forms, its qubit leaves the flow: the network is permanently short that site's share." This note examines one supplied reading of that clause in isolation. In that reading a removed site holds zero amplitude, and the links to it are deleted. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose this reading or the wave equation below.

## Model and results

The wave is second-order lattice Klein-Gordon on a 360 by 200 grid, d2u/dt2 = Lap u - m^2 u on live sites. Inside a disk of radius 20, a fraction 0.5, 1 or 2 percent of sites is removed with a fixed seed. A packet passes at impact parameter 26. The runner compares its sideways position after passing with the run without removals.

- **Massless packet** (group speed .97): moved away from the disk by +4.0, +10.0 and +14.5 sites at the three fractions.
- **Packet of mass .5** (group speed .78): moved away by +3.9, +5.6 and +9.0 sites.
- **Confined mode:** the lowest mode of a radius-28 region containing the disk rises in frequency by 5.9, 23 and 50 percent.

A removed site acts as a hard obstacle, so a dilute set of them behaves as a repulsive medium. Both packets are pushed away, and a body held among the removals oscillates faster. Under a gravitational reading the expected signs are attraction for both packets and a slower clock. In this model all three signs are the opposite.

## Consequence for the gravity reading

In this supplied model, the local exclusion effect of removed sites is not an attractive gravitational response. A gravitational reading of record removal therefore needs a separate long-range response sourced by the records, such as a deficit field that propagates without loss. The runner does not supply such a field. The fractions here are far above any density implied by ordinary matter, so the local effect itself would be extremely small.

## Scope

The discretization, the removal rule, the masses, the momenta and the geometry are supplied. So are the seeds and the detection window. No gravity field, long-range response, physical identification or derivation of the clause is established.
