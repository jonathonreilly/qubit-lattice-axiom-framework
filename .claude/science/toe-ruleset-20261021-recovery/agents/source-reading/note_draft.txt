---
claim_id: record_source_turn_deposits_are_not_fixed_by_a_relays_own_odds_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "In supplied two-direction relay models under the formation law that records never condition the odds, no relay rule that keeps the joint configuration Born at every tick makes a relay's one-tick turn statistics depend only on its own reduced odds; coarse-graining does not remove this, a burns-only source is traceless, and finite size estimates use a supplied coupling; no physical identification, field equation or adoption of a source reading is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/record_source_turn_deposits_are_not_fixed_by_a_relays_own_odds_2026_10_21.py
---

# Record-source turn deposits are not fixed by a relay's own odds

Claim type: bounded_theorem.
Primary runner: `scripts/record_source_turn_deposits_are_not_fixed_by_a_relays_own_odds_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its record source deposits a burn on each step and a turn when a relay changes direction. This note asks whether the turn part can be read from a relay's own odds when the odds are never conditioned on a record. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## No turn law local to one relay

Take two entangled two-direction relays A and B. A joint rule that stays Born at every tick bounds B's one-tick turn probability J01 differently for the two bases A can be measured in, while B's reduced odds are the same in both. For a maximally entangled direction pair at phi = pi/4, one basis forces J01 >= sin(phi)/2 = 0.3536 and the other caps J01 <= sin^2(phi/2) = 0.1464. The intervals are disjoint by (sin phi + cos phi - 1)/2 = 0.2071, which is positive on all of (0, pi/2). Brute-force steering ensembles never beat these bounds. Every tested partial entanglement (Schmidt weights 0.6 to 0.99) also has an infeasible orientation, with gaps 0.2000 down to 0.0098. For a massive-walk coin theta = 0.1 the forced gap is 0.0948 per tick, against a rest turn rate of 0.1. Bell-local deterministic kernels obey CHSH <= 2, as rederived.

Coarse-graining does not help. With B alternating R(+pi/4) and R(-pi/4) and A choosing a basis once, the minimal joint rule gives 0.7080 turns per relay per tick in one basis and 0 in the other. For any rule the shift is at least 0.4142 N T turns while the spread is at most (T/2) sqrt N, so the separation is at least 0.83 sqrt N standard deviations, about 83 at N = 1e4.

## Burns alone and a sustained channel

Every burn deposit is null, so a burns-only source is traceless, while eps u u has trace -m^2/eps. For 1D plane waves, burns plus turns give T11 = eps v^2 and burns alone overshoot by eps(1 - v^2). For a 3D relay at rest, burns alone give twice the dust strength in h00 and gamma = 1/3, against 1 and 1 for dust. For a momentum-entangled relay steered into plane or standing waves, the turn rate differs by at least eps v^2, for example 0.0988 against 0.1111 per tick at k = 0.016.

In a two-branch torque toy with one classical ball of weight 1/2, actual deposits give torque 1, branch-averaged deposits 0, and actual burns with reduced turns 2.

## Size, with a supplied coupling

Taking G = a^2/(8 pi) with hbar = c = 1 as a supplied conversion, the setting-dependent part for a rubidium atom at 1 cm/s is about 3e-46 kg mass equivalent per atom from the sustained channel, and about 8e-36 kg from switching. The smallest gravitating source measured to date is about 9e-5 kg.

## Scope

Supplied: the two-direction models, coins, angles, protocols, steering ensembles and the coupling conversion. No physical identification, field equation or adopted source reading is established.
