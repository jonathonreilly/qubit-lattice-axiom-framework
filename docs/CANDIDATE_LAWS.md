---
claim_id: candidate_laws
claim_type: meta
claim_scope: "Register of owner-adopted candidate laws CL-1 to CL-3; zero premise weight. Results that use a candidate law are conditional on it."
---

# Candidate laws

Claim type: meta.

Candidate laws are working clauses the owner has adopted to build on. They are not axioms. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), [policy section 6](audit/AXIOM_MINIMALITY_POLICY.md#6-explicit-owner-approval-for-axioms-and-primitives) and `docs/audit/data/axiom_premise_nodes.json` alone control premise admission, so this register has zero premise weight. Any result that uses a candidate law is conditional on it, and the models used to explore a law are supplied choices, not consequences of it.

## Terms

- **Burn.** A site is burnt when a record forms there. Its qubit leaves the flow (CL-2), and since a record is permanent and a site holds at most one, a burnt site never returns to the flow and never records again.
- **Relay.** A sequence of burns at successive nearest-neighbour sites that record the same value: the record at one site is followed by a record of that value at an unburnt neighbour.

## CL-1: lossless influence

> "Influence passes from site to site without loss."

Adopted by the owner on 2026-10-18. It does not fix the update rule or its coefficients. In the supplied scalar averaging model, a loss epsilon per step screens influence beyond a range proportional to epsilon^(-1/2).

## CL-2: a record's qubit leaves the flow

> "When a record forms, its qubit leaves the flow: the network is permanently short that site's share."

Adopted by the owner on 2026-10-18. It does not fix the size of the share, the field equations or the boundary conditions. The supplied models and their limits are in the [CL-2 evidence note](CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md).

## CL-3: a record can be read once

> "A record can be read once. A burn's one read is taken by the next site of its relay."

Adopted by the owner on 2026-10-19. The axioms say only records are readable but not how many times. CL-3 limits readability without changing permanence: the record stays locked, and only its single read is spent. A fact that many readers can learn needs many records of it. CL-3 does not say which records relay, when a relay steps, how the next site is chosen, or who takes the read of a record that does not relay. The supplied models behind it are in the [CL-3 evidence note](CANDIDATE_LAW_CL3_READ_ONCE_RECORDS_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-19.md).
