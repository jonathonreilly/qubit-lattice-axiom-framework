---
claim_id: relay_value_current_and_the_vector_field_it_sources_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Exact lattice continuity of a relay value current on a supplied walk, and symbolic rederivation that a local covariant second-order vector operator compatible with a conserved current is the Maxwell operator; no gauge group beyond one conserved value, charge values, lattice field dynamics or empirical identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/relay_value_current_and_the_vector_field_it_sources_2026_10_21.py
---

# The relay value current and the vector field it sources

Claim type: bounded_theorem.
Primary runner: `scripts/relay_value_current_and_the_vector_field_it_sources_2026_10_21.py`.

Two clauses in the [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, are used here. Under the read-once clause a relay passes on its value without copying or destroying it. Under the stepping clause it moves one block per tick. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) make record outcomes discrete.

## The value current

Let every relay of a species carry value q. Define the density as q times the expected number of relays at a block. Define the current on a link as q times the expected number crossing it per tick. No relay is created or destroyed, and each moves exactly one block per tick. The density change at a block therefore equals inflow minus outflow, exactly. On a six-direction walk packet with relays following the odds, the runner finds the violation below 1e-17 over six ticks on 24^3 sites. Unlike the record source of CL-7, which balances only up to a residual that falls with packet width, this current is conserved exactly on the lattice. Since record values are discrete outcomes, the charges a relay can carry form a discrete set.

## The vector field

**Ansatz.** The general local, Lorentz-covariant, second-order operator on a vector field is O(A)_n = a k^2 A_n + b k_n (k.A).

**Divergence condition.** A conserved current imposes no extra condition on A exactly when k.O(A) vanishes for every A. That forces b = -a, which is the Maxwell operator. It annihilates pure-gauge fields k xi, and a mass term spoils the identity.

**Static charge.** In Coulomb gauge a static charge gives A_0 = -q/|k|^2, the Coulomb potential, with A_i = 0.

**Coupling.** Suppose two species couple with strengths e1 and e2 and exchange value at rate J. The source's divergence is then (e1 - e2) J, so the field must couple to the value carried, not to the species.

## Scope

The walk, the packet, the value assignment and the vector-field ansatz are supplied. A vector response on links is assumed here, just as the geometry lane assumes edge lengths. No gauge group beyond one conserved value, charge values, lattice field dynamics or empirical identification is established.
