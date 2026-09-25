---
claim_id: dynamics_clause_records_as_the_only_irreversible_events_restate_reversibility_a_channel_that_keeps_pure_states_pure_and_distinguishable_is_unitary_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Open PR 9084 leaves reversibility between records supplied (D-rev). Take two things, recorded and not adopted. First, the evolution of a finite region between records is a channel (D-chan; open PR 9084 treats one site with a decoupled partner, so the whole-region statement is a premise). Second, records are the only irreversible events (D-onlyrec): between records no pure state becomes mixed and no two pure states become less distinguishable. (i) A channel that sends every pure state to a pure state has Kraus operators with parallel outputs on every input. Two linear maps with that property are proportional, or both have rank at most one with a common range. So the Kraus operators are proportional, giving a unitary conjugation (deviation 3e-16), or the channel replaces every state by one pure state. (ii) The replacement channel keeps purity but sends orthogonal states to one output, losing distinguishability. (iii) Random non-unitary channels send some pure state to a mixed one (output purity as low as 0.38) and lower some pure pair's trace distance (by up to 0.86); unitaries do neither. So for channels on a finite system, D-onlyrec is Wigner's condition: it restates reversibility in record language rather than deriving it, and the theorem supplies the unitary form. The Record axiom makes records permanent; it does not say nothing else is irreversible, so D-onlyrec is an added reading. Closure of the lattice (nothing outside it) motivates reading purity as a fact about the lattice but does no mathematical work. The infinite lattice, continuous time, the range and the coupling values are not treated."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_as_the_only_irreversible_events_restate_reversibility_2026_09_24.py
---

# Records as the only irreversible events restate reversibility

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** an equivalence with finite certificates; unaudited.

## Result

Open PR 9084 shows a site's evolution between records must be linear and
completely positive, and leaves reversibility supplied (D-rev). This note
asks what reversibility looks like in record language.
- **D-onlyrec.** Records are the only irreversible events. So between
  records a pure state stays pure and distinguishable states stay
  distinguishable.
- **For a channel, that is unitarity.** A channel that keeps every pure
  state pure is a unitary conjugation or a replacement channel. The
  replacement channel erases distinguishability.

So D-onlyrec and reversibility are the same condition for channels on a
finite system (Wigner's condition). The note restates D-rev in record
language and supplies the unitary form. It does not derive reversibility
from anything weaker.

## Setting and decision points

- **D-chan.** The evolution of a finite region between records is a
  channel. Open PR 9084 treats one site with a decoupled partner. A closed
  region has no decoupled partner, so the whole-region statement is a
  premise here.
- **D-onlyrec.** As above. The Record axiom makes records permanent. It
  does not say that nothing else is irreversible, so D-onlyrec is an added
  reading, recorded and not adopted.
- **D-closed.** The lattice is the whole system. This motivates reading a
  global state's purity as a fact about the lattice, but the theorem does
  not use it.

## Theorem — purity and distinguishability give unitarity

Let `Φ(ρ) = Σ_i K_i ρ K_i†` be a channel on a finite-dimensional system.

- **Purity gives parallel outputs.** If `Φ(|ψ⟩⟨ψ|)` is pure for every `ψ`,
  then the vectors `K_i ψ` are parallel for every `ψ`.
- **The lemma.** Two linear maps whose outputs are parallel on every input
  are proportional, or both have rank at most one with a common range.
  - A rank-two map and a rank-one map have fully non-parallel outputs on
    some input.
  - Two rank-one maps `|w⟩⟨u|` and `|w⟩⟨v|` are parallel everywhere but
    not proportional.
- **So there are two cases.**
  - Either `K_i = c_i V` for all `i`. Then trace preservation makes `V`
    unitary, in finite dimension, and `Φ(ρ) = V ρ V†`.
  - Or every `K_i = |w⟩⟨u_i|`. Then `Φ` replaces every state by `|w⟩⟨w|`.
- **Distinguishability rules out replacement.** The replacement channel
  sends orthogonal states to the same output, so it lowers their
  distinguishability from 1 to 0. ∎

Conversely, a unitary conjugation keeps purity and distinguishability. So
for channels, D-onlyrec holds exactly when the evolution is unitary.

## Checks

The runner has 5 checks and all pass in under 1 s.

| Check | Result |
|---|---|
| Purity | Random non-unitary qubit and qutrit channels reach output purity 0.383. Unitaries keep purity to 3e-15. |
| Replacement channel | Output purity 1, but orthogonal inputs map to the same output (trace distance 1 → 0). |
| Mechanism | Proportional Kraus operators equal `U ρ U†` to 3e-16. A generic channel's Kraus outputs have non-parallelism up to 0.889. |
| Distinguishability | Random non-unitary channels lower a pure pair's trace distance by up to 0.864. Unitaries change none (1e-15). |
| The lemma | Two rank-one maps with a common range: non-parallelism 4e-16, not proportional. A rank-two and a rank-one map: non-parallelism up to 0.993. |

## What this means for the lanes

- **Dynamics.** Reversibility between records now has a record-language
  form, D-onlyrec. It is supplied either way. With open PRs 9083 to 9085,
  the campaign's quantum rules and dynamics rest on:
  - the kinematics the clause brings;
  - D-perm, with the lock, the support condition and the distant update;
  - D-tr;
  - D-loc at equal time;
  - two-possibility menus;
  - D-chan and D-onlyrec, which is reversibility;
  - continuous, time-homogeneous evolution;
  - the range on the generator;
  - covariance.

  From these, the trace rule, the Born orientation, antipodal menus, and
  linear, completely positive, unitary evolution follow. The uniqueness of
  the distant update also follows, and the generator is Hermitian. Its
  two-site form restates the range. The coupling values stay open.
- **Prior art.** Maps that keep pure states pure and distinguishable are
  the subject of Wigner's theorem. This note uses the Kraus form for
  channels, and cites Wigner as prior art, not as a premise.

## Independent checks

A separate checker wrote its own code without reading this runner. A later
adversarial review of the whole chain ran its own checks.
- **Confirmed.** The replacement channel's purity and its trace distance
  1 → 0. That proportional Kraus operators give a unitary (d = 2, 3, 5).
  That all 40 random non-unitary channels mix some pure state and lower
  some pair's trace distance, while unitaries change neither.
- **Flagged, now addressed.**
  - D-onlyrec *is* reversibility for channels, so the first version's
    "reversibility follows" overstated it. The note now says it restates
    it.
  - D-closed does no mathematical work.
  - Open PR 9084's channel covers one site with a decoupled partner; the
    whole region needs D-chan.
  - The lemma was stated too weakly. It now says: proportional, or both
    rank at most one with a common range.

## What this does not do

- It adopts no reading. D-chan, D-onlyrec and D-closed are recorded, not
  derived from the axiom text.
- It treats finite-dimensional channels. The infinite lattice is not
  treated.
- It does not derive continuous time, the range or the couplings.
