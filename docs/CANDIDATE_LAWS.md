---
claim_id: candidate_laws
claim_type: meta
claim_scope: "Register of the current working candidate laws CL-1 to CL-7 and their open dependencies; zero premise weight. Results that use a candidate law are conditional on it."
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

> "Each tick a relay forms its next record in the neighbouring block in its direction, at an unburnt site of that block chosen with equal probability. If that block is used up, the relay takes its direction afresh from its block's odds among directions whose block is not."

Relays therefore always move one block per tick. A block of n sites can take n visits.

## CL-5: a relay's energy

> "A relay's energy is the mean phase advanced in one tick by its block's direction amplitudes, weighted by their odds."

The phase advance of an amplitude is minus the argument of its value after the tick times the conjugate of its value before, at the same block. Energy is in radians per tick. For a mode of definite frequency it is that frequency.

## CL-6: relays follow the odds

> "Relays are distributed as the odds of block and direction. Each tick, with probability twice its energy, a relay takes its direction afresh from its block's odds; where the tick update has changed the odds, relays in directions over their odds then switch to directions under them, in proportion to the shortfalls."

The first sentence is what the second maintains: once relays start distributed as the odds, the switching keeps them so at every tick. Its domain is relays whose energy is at most one half radian per tick, and blocks that are not used up.

## CL-7: the record source

> "Each tick a relay deposits its energy on the spacetime step it takes, (1, d). Each turn from d to d' deposits -1/4 on the chord d' - d. The record source is the sum of the deposits, each entered as the outer product of its vector with itself."

A step of one block per tick is the unit spacetime step, so a relay moves at the top speed. The single source tensor carries energy, momentum and stress. Consider a mode of definite frequency, of a tick update that moves each direction amplitude one block along its direction. For it, CL-5 to CL-7 give energy times u u, with u = (1, v) and v the group velocity, shear included. For packets the momentum balance closes up to a residual that falls with packet width. Every symmetric source can be written as deposits on the edges of the D4 carrier. Evidence: `docs/SCALE_LADDER_GRAVITY_BURN_AND_TURN_SOURCE_TENSOR_BOUNDED_THEOREM_NOTE_2026-10-21.md`, `docs/RELAY_ENERGY_AS_LOCAL_ODDS_FREQUENCY_BOUNDED_THEOREM_NOTE_2026-10-21.md` and `docs/RECORD_SOURCE_AS_EDGE_DEPOSITS_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

## What follows without a further law

Suppose geometry is described by edge lengths and responds to the deposits linearly and without loss (CL-1). Its response is then a symmetric tensor field, since the deposits are outer products of edge vectors. Then the response operator is the linearised Einstein operator, the field is massless, and every species couples with the same strength. A static source then has equal time and space potentials, so light is deflected twice as much as by the time potential alone. These steps are rederived in `docs/RECORD_PROGRAM_THEOREMS_REDERIVED_BOUNDED_THEOREM_NOTE_2026-10-21.md`.

A relay carries its value unchanged and moves one block per tick, so its value current is conserved exactly on the lattice. Suppose the links respond to that current through a vector field, linearly and without loss. The response is then the Maxwell operator: gauge invariant, massless, Coulomb for a static charge, and coupled to the value rather than the species. Since record values are discrete outcomes, charges are discrete too (`docs/RELAY_VALUE_CURRENT_AND_THE_VECTOR_FIELD_IT_SOURCES_BOUNDED_THEOREM_NOTE_2026-10-21.md`).

Proper time needs no law either. A clock is itself a system of relays, and the phase it accumulates along its path advances at eps - k.v. For a relativistic dispersion that equals m^2/eps, which is m/gamma. Moving clocks therefore run slow as a consequence of the tick update, not as an added rule (`docs/SCALE_LADDER_GRAVITY_FRONT_CLOCKS_SPIN_HALF_WALK_BOUNDED_THEOREM_NOTE_2026-10-21.md`).

## Open dependencies

- **The tick update of the odds.** CL-5 to CL-7 use it, but no law here fixes it. That includes how a block's possibilities split into step directions, and each species' mass. One qubit per site is one fermion mode per site, so a field with internal components has to live on blocks. The current candidate puts four two-component fields on the eight sites of a 2^3 block and runs a three-substep walk. It adds a same-block chirality mass and a second, staggered-type mass that gaps the doublers. That candidate satisfies CL-5 to CL-7 for plane waves (`docs/BLOCK_OF_EIGHT_ONE_MODE_SITES_CARRIES_A_GAPPED_DIRAC_BAND_BOUNDED_THEOREM_NOTE_2026-10-21.md`). It is not adopted, because it is exactly covariant under only 4 of the 24 rotations and its light band comes in four sublattice copies.
- **Reading squared amplitudes as probabilities.** The axioms give a per-site distribution, but not this reading of block-direction amplitudes.
- **The responses.** The derivations above need inputs no law here supplies. Geometry must be edge lengths responding to deposits, the premise the geometry lane already uses. Links must carry a vector response to value currents. The coupling strengths are open too: G = c a^2 for lattice spacing a, with c undetermined, and the charge unit. The gauge group beyond one conserved value is also open.
- **Matter content.** In the block candidate, the light band's four sublattice copies sit at k = 0 and the three momenta pi(1,1,0) and its permutations. Rotations about a site fix the first copy and permute the other three, so the copies form a singlet and a triplet. Their partners, shifted by pi(1,1,1), sit at the remaining corners of the zone. Together the eight corners carry the 1 + 1 + 3 + 3 corner structure studied in the repo's generation notes. The copies do not mix under the candidate update. No law here identifies a triplet with generations, supplies colour or weak structure, or makes the light fermions chiral. Those remain the open bridges recorded in the generation, colour and chirality notes.
- **When records form.** Relays form a record every tick (CL-4), but no law here says when a new fact first forms from the odds, or at what rate. That is the measurement question, and it also bears on vacuum energy. A new record's realised weight minus its expected weight averages to zero, so record formation adds zero-mean noise to the source. If gravity is unimodular, that noise would make the cosmological constant wander with zero mean, by an amount that depends on the formation rate.

