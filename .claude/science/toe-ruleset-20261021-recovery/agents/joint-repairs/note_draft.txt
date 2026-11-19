---
claim_id: joint_relay_energy_and_switching_repairs_on_two_relay_walks_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite diagnostics on supplied lossless 1D two-relay walks and few-qubit pointer couplings of proposed joint repairs to the relay energy (a conditional energy) and to switching (joint switching plus fresh sequential redraws); records where the literal proposals fail, where the repairs hold, and the remaining failures of the record source for entangled and standing-wave states and of finite block capacity; no physical identification, field equation or adoption of the repairs is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/joint_relay_energy_and_switching_repairs_on_two_relay_walks_2026_10_21.py
---

# Joint repairs of relay energy and switching on two-relay walks

Claim type: bounded_theorem.
Primary runner: `scripts/joint_relay_energy_and_switching_repairs_on_two_relay_walks_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its relay energy and switching law are stated for one relay. This note tests two joint versions on supplied two-relay walks: a conditional energy given the other relays' blocks and directions, and joint switching with fresh redraws from the conditional odds. Several checks below confirm failures; they are reported as such. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## The conditional energy

Taken literally, the conditional energy of relay 1 in a product state counts relay 2's phase: w1 + w2 = 0.6383 instead of w1 = 0.2000. Restricting to relay 1's own part of the tick gives 0.200000 exactly. Three further failures remain. From a one-site start, the same-block amplitude before the tick is zero at every tick, so the phase is undefined (the generator reading H = i log U is defined there and gives 0 to 1.7e-16). An upper-band packet has negative same-block energy in its tails (weight 0.0035, minimum -0.228). In an entangled state the repaired energy exceeds 1/2 on some configurations (range 0.1414 to 0.5105, weight 0.0173), outside the switching law's domain.

## Redraws and readings

Sequential redraws, each from the conditional odds, keep the joint occupation equal to the joint odds for 20 ticks to 2.1e-16, and sampled pairs match with chi2/dof 0.919 over 978 bins. Simultaneous redraws miss by 7.92e-2 and own-block-marginal redraws, as the switching law is written, by 1.00e-1. With two coined pointers reading one spin, sequential redraws stay exact (6.5e-16) and reader disagreement matches that of the odds (0.0965 against 0.1012); marginal redraws do not (0.0677). For a singlet with coined pointers, relay readings give CHSH 2.577 against 2.5710 for the odds.

## The record source

For product states the repaired rules give relay 1 the source eps u u exactly, with components (0.27935, 0.19371, 0.13433). For the entangled state (0,2k)+(2k,0) the energy component is the mean energy (0.31916 in the generator reading, 0.31889 in the own-part reading), but the flux and stress components (0.160, 0.051) are not the branch-mixture values (0.194, 0.171). Relay 1's switching turns depend on walker 2's coin (0.0563 against 0.1265) while its own odds do not, to 6.9e-18. For a standing wave of the same modes and energy, burns plus turns give stress -0.0563 against eps v^2 = 0.1822 for the plane wave. The linear reading T_xx = <H> - theta <sigma_x> gives the standing wave the plane-wave value and a six-mode packet 0.1860 against a mode-weighted 0.1848.

## Finite block capacity

With burns and a block capacity n on a ring of 16 blocks, the current follows the odds until a block is used up and then every relay is stuck, since no stated law covers a full block. The first hit comes at a median of 50, 223 and 951 ticks for n = 4, 16 and 64. A drifting packet over 150 ticks breaks for most relays at n = 1 and shows no hits at n >= 8 at this scale.

## Scope

Supplied: the walks, coins, packets, pointer couplings, update orders, block capacities and the linear stress reading. No physical identification, field equation or adoption of the repairs is established.
