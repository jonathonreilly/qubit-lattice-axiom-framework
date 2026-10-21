---
claim_id: candidate_laws
claim_type: meta
claim_scope: "Register of the current working candidate laws CL-1 to CL-8 and their open dependencies; zero premise weight. Results that use a candidate law are conditional on it."
---

# Candidate laws

Claim type: meta.

Candidate laws are the current working rules adopted to build on. They are not axioms. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), [policy section 6](audit/AXIOM_MINIMALITY_POLICY.md#6-explicit-owner-approval-for-axioms-and-primitives) and `docs/audit/data/axiom_premise_nodes.json` alone control premise admission, so this register has zero premise weight. Any result that uses a candidate law is conditional on it. The models used to explore a law are supplied choices, not consequences of it.

## Terms

- **Tick.** One update of the odds under lossless influence (CL-1).
- **Odds.** The amplitudes the tick update acts on, one per block and step direction. Their squared magnitudes are read as probabilities, and their phases advance from tick to tick.
- **Block.** A cube of sites at the rung of the scale ladder on which the odds are written. Neighbouring blocks share a face.
- **Burn.** A site is burnt when a record forms there. Its qubit leaves the flow (CL-2), and since a record is permanent and a site holds at most one, a burnt site never returns to the flow and never records again.
- **Relay.** A sequence of records of the same value formed in successive neighbouring blocks. Its direction is the block step it is currently making.

## CL-1: lossless influence

> "Influence passes from site to site without loss."

It does not fix the update rule or its coefficients. In the supplied scalar averaging model, a loss epsilon per step screens influence beyond a range proportional to epsilon^(-1/2).

## CL-2: a record's qubit leaves the flow

> "When a record forms, its qubit leaves the flow: the network is permanently short that site's share."

It does not fix the size of the share, the field equations or the boundary conditions. Locally a removed site only excludes: in a supplied wave model, removed sites push packets away and raise confined frequencies (`docs/SCALE_LADDER_GRAVITY_REMOVED_SITES_REPEL_AND_BLUESHIFT_BOUNDED_THEOREM_NOTE_2026-10-21.md`). A gravitational role for the clause therefore needs a long-range response sourced by records. The supplied models are in the [CL-2 evidence note](CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md).

## CL-3: a record can be read once

> "A record can be read once. A burn's one read is taken by the next site of its relay."

The axioms say only records are readable but not how many times. CL-3 limits readability without changing permanence. A fact that many readers can learn needs many records of it. The supplied models are in the [CL-3 evidence note](CANDIDATE_LAW_CL3_READ_ONCE_RECORDS_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-19.md).

## CL-4: a relay steps every tick

> "Each tick a relay forms its next record in a neighbouring block, in its direction, at an unburnt site of that block chosen with equal probability. If that block has no unburnt site, the relay takes its direction afresh from its block's odds, restricted to directions whose neighbouring block has one."

Relays therefore always move one block per tick. A block of n sites can take n visits, so a relay may return to a block until the block is used up.

## CL-5: relays follow the odds

> "The probability that a relay is in a given block travelling in a given direction equals the odds of that block and direction."

This ties where relays are, and which way they go, to the amplitudes, so a relay's step statistics follow the squared amplitudes at every tick. Its domain is blocks with an unburnt site, since CL-4 keeps relays out of used-up blocks.

## CL-6: a relay's energy

> "A relay's energy is the mean phase advanced in one tick by its block's direction amplitudes, weighted by their odds."

The phase advance of an amplitude is minus the argument of its value after the tick times the conjugate of its value before, at the same block. Energy is measured in radians per tick. For a mode of definite frequency it is that frequency.

## CL-7: turning

> "Each tick, with probability twice its energy, a relay takes its direction afresh from its block's odds. Then, if the tick update has changed the odds, a relay in a direction now holding more than its odds switches, with probability equal to that direction's excess fraction, to a direction holding less, chosen in proportion to the shortfalls."

Its domain is relays whose energy is at most one half radian per tick. For a mode of definite frequency the odds do not change, so only the first sentence acts, and it keeps CL-5.

## CL-8: the record source

> "Each step of a relay in direction d adds its energy times d d to the record source. Each turn from d to d' adds -(d'-d)(d'-d)/4."

For a mode of definite frequency of a tick update that moves each direction amplitude one block along its direction, CL-5 to CL-8 give a source equal to energy times v v, shear included, where v is the group velocity. For packets the momentum balance closes up to a residual that falls with packet width. Evidence: `docs/SCALE_LADDER_GRAVITY_BURN_AND_TURN_SOURCE_TENSOR_BOUNDED_THEOREM_NOTE_2026-10-21.md` and `docs/RELAY_ENERGY_AS_LOCAL_ODDS_FREQUENCY_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

## Open dependencies

- **The tick update of the odds.** CL-5 to CL-8 use it, but no law here fixes it. This includes how a block's possibilities split into step directions, and each species' mixing strength (its mass).
- **Reading squared amplitudes as probabilities.** The Terms take the squared magnitudes of the odds as probabilities; the axioms give a per-site distribution but not this identification for block-direction amplitudes.
- **The field equation.** Nothing here says how geometry responds to the record source, or fixes its coupling.
- **Proper time.** On cubic walks in 3D the turn count is not a relativistic clock. Flips set by the chirality coherence converge to one in a supplied spin-1/2 walk, but they need signed ticks where packets interfere, so no clock law is listed.
