---
claim_id: dynamics_clause_a_closed_lattice_whose_only_irreversible_events_are_records_evolves_unitarily_between_records_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Open PR 9084 showed that locality of marginals makes the evolution between records a channel: linear and completely positive. Take two readings, recorded and not adopted. The lattice is closed, with nothing outside it (D-closed). Records are its only irreversible events, so evolution between records neither mixes a pure global state nor lowers the distinguishability of two states (D-onlyrec). (i) A channel that sends every pure state to a pure state has Kraus operators with parallel outputs on every input, so they are proportional, or it is a rank-one replacement channel. Proportional Kraus operators give a unitary conjugation (deviation 3e-16). (ii) The replacement channel keeps purity but sends orthogonal states to one output, losing distinguishability. (iii) Random non-unitary channels send some pure state to a mixed one (output purity as low as 0.38) and lower some pure pair's trace distance (by up to 0.86); unitaries do neither. So under D-closed and D-onlyrec, the evolution between records is unitary: the reversibility part of D-rev follows. Continuous time and nearest-neighbour range stay supplied. No derivation of D-closed, D-onlyrec, the time structure or the coupling values is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_closed_lattice_evolves_unitarily_between_records_2026_09_24.py
---

# A closed lattice whose only irreversible events are records evolves unitarily between them

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** conditional derivation with finite certificates; unaudited.

## Result

Open PR 9084 derived that the evolution between records is linear and
completely positive (a channel) from locality of marginals. It left
reversibility supplied (D-rev). This note derives reversibility from two
readings of the axioms:
- **D-closed.** The lattice is the whole system; the axioms name nothing
  outside it.
- **D-onlyrec.** Records are the only irreversible events. So between
  records a pure global state stays pure and distinguishable states stay
  distinguishable.

Under these, the evolution between records is unitary:
- a channel that keeps every pure state pure is a unitary conjugation or a
  replacement channel;
- the replacement channel erases distinguishability.

## Setting and decision points

- **D-loc**, giving channels (open PR 9084).
- **D-closed and D-onlyrec (new).** As above: two readings of the axioms,
  recorded and not adopted.
  - The Record axiom makes records the permanent facts. D-onlyrec reads
    that as saying nothing else is irreversible.

## Theorem — purity and distinguishability give unitarity

Let `Φ(ρ) = Σ_i K_i ρ K_i†` be a channel on a finite-dimensional system.

- **Purity forces proportional Kraus operators.** If `Φ(|ψ⟩⟨ψ|)` is pure for
  every `ψ`, then the vectors `K_i ψ` are parallel for every `ψ`.
  - Two linear maps whose outputs are parallel on every input are
    proportional, unless one has rank one.
  - So either `K_i = c_i V` for all `i`, or `Φ` replaces every state by one
    pure state.
- **Proportional Kraus operators give a unitary.** Trace preservation makes
  `V` unitary (an isometry, in finite dimension), and then
  `Φ(ρ) = V ρ V†`.
- **Distinguishability rules out replacement.** The replacement channel
  sends orthogonal states to the same output, so it lowers their
  distinguishability from 1 to 0. ∎

Under D-closed, the global state has nothing to entangle with, so its
purity is a fact about the lattice. D-onlyrec forbids losing purity or
distinguishability without a record. So the evolution between records is
unitary.

## Checks

The runner has 4 checks and all pass in under 1 s.

| Check | Result |
|---|---|
| Purity | Random non-unitary qubit and qutrit channels reach output purity 0.383. Unitaries keep purity to 3e-15. |
| Replacement channel | Output purity 1, but orthogonal inputs map to the same output (trace distance 1 → 0). |
| Mechanism | Proportional Kraus operators equal `U ρ U†` to 3e-16. A generic channel's Kraus outputs have non-parallelism up to 0.889. |
| Distinguishability | Random non-unitary channels lower a pure pair's trace distance by up to 0.864. Unitaries change none (1e-15). |

## What this means for the lanes

- **Dynamics.** With open PRs 9083, 9084 and 9085, the campaign's quantum
  rules and dynamics now rest on these readings:
  - D-loc;
  - the lock;
  - two-possibility menus;
  - D-closed and D-onlyrec;
  - continuous time and nearest-neighbour range;
  - covariance.

  Everything else follows: the Born law, the collapse, antipodal menus,
  linear, completely positive and unitary evolution, and the clause's form.
  The coupling values stay open.
- **What stays open.** Continuous time and the range, which the Lattice
  axiom's nearest-neighbour structure suggests but does not fix. Also the
  coupling values `J`, `K`, `D`.

## What this does not do

- It adopts no reading. D-closed and D-onlyrec are recorded, not derived
  from the axiom text.
- It treats finite-dimensional channels. The infinite lattice is reached
  as a limit and is not treated.
- It does not derive continuous time, the range or the couplings.
