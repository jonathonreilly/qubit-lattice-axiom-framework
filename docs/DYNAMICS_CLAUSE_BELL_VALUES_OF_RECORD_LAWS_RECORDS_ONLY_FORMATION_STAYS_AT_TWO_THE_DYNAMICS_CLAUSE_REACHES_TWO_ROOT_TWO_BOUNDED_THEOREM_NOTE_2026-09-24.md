---
claim_id: dynamics_clause_bell_values_of_record_laws_records_only_formation_stays_at_two_the_dynamics_clause_reaches_two_root_two_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "CHSH values of record laws under four supplied readings, none adopted. (1) Formation reading, records-only conditioning: each record is a function of the records already formed at its neighbours and of fresh local randomness. If both setting records form with no parents and neither is an ancestor of the other wing's outcome, the joint odds are a mixture over the common ancestry of products of one-wing odds, so |CHSH| <= 2. Checked on 9000 random kernels over three windows, largest 1.94. (2) If a record carrying one wing's setting is an ancestor of the other wing's outcome, |CHSH| = 4 exactly. (3) Static reading conditioned on its end records: a five-site binary chain reaches the exact rational 2981272129803/1020712070201 > 2 sqrt 2. (4) The dynamics clause of the supplied companion construction with records as fields and the trace rule of the supplied companion construction: the antiferromagnetic Heisenberg bond of an isolated pair has the singlet as ground state, antipodal menus give E = -a.b and CHSH = 2 sqrt 2 exactly, and no state or antipodal menus exceed 2 sqrt 2. Sequential formation (A by the trace rule, then B by its isolated ground-state law in the field of A's record) reproduces the singlet odds. The dynamics clause, the trace rule, the menus and the setting mechanism are supplied, not derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_bell_records_only_formation_versus_dynamics_clause_2026_09_24.py
---

# Bell values of record laws: records-only formation stays at 2, the dynamics clause reaches 2 sqrt 2

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite results and one classical theorem applied to supplied readings; unaudited.

## Result and scope

the supplied constructions found that the odds at a site with an unrecorded neighbour
depend on that neighbour's state, not on records alone. This note asks
whether that matters for correlations. It does, sharply. The CHSH value of
two wings separates the readings:

| Reading (all supplied) | Largest CHSH |
|---|---|
| Formation, conditioning on records alone, settings formed independently | 2 |
| Formation, a record carries one wing's setting to the other wing | 4 |
| Static law, conditioned on its setting records | above `2 sqrt 2` |
| The dynamics clause with records as fields and the trace rule | `2 sqrt 2` exactly |

The first row is Bell's theorem, applied to the formation reading. A law
that conditions on neighbour records alone is a local causal model. With
independently formed settings, its correlations stay inside the classical
set.

The last row is the quantum value. The dynamics clause of the supplied companion construction
reaches it and does not go beyond it:
- The antiferromagnetic Heisenberg bond of an isolated pair has the
  singlet as its ground state.
- Read by the trace rule on antipodal menus, the singlet gives
  `E = -a.b`, hence `2 sqrt 2`.
- Records can also form one at a time. Once A's record exists, B is an
  isolated site in the field of A's record, and B's law is the
  isolated-site law of the supplied companion construction. The two orders give identical odds.

The middle rows show why the hypotheses matter. A record that carries a
setting across the wings gives the CHSH value 4 with no-signalling outcome marginals. A
static law conditioned on its own setting records post-selects and exceeds
the quantum value.

The fixed causal formation model with independent settings obeys its classical bound. The supplied quantum state, trace rule and menus attain the quantum value; this is not a derivation from the four axioms or an exhaustive classification of admissible dynamics.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`).
  - Admissibility: the distribution at a site "is determined by, and
    varies with, the nearest-neighbor conditions".
  - Record: "Records form ... records are permanent. Only records are
    readable."
  - The memo leaves "the formation site, probability, or rate" to
    downstream supplier content.
- **Formation reading** (supplied, as in the landed formation notes).
  - Records form in some order, each drawn from a kernel that depends on the
    contents of the already formed neighbour records, with fresh local
    randomness.
  - "Conditioning on records alone" means that no other state enters the
    kernel.
- **Wings.** Setting records `s_A`, `s_B` and outcome records `a`, `b`
  (two contents, read as `+1` and `-1`).
  - `E_st` is the expectation of `ab` given `s_A = s`, `s_B = t`.
  - CHSH is `|E00 + E01 + E10 - E11|`, maximised over which pair is
    negated.
- **Static reading** (supplied). A joint law on a finite window with pair
  weights. "Conditioning on the setting records" selects the sub-ensemble
  with the given end records.
- **Dynamics side** (supplied, not adopted).
  - The generator of the supplied companion construction with the Heisenberg coupling.
  - Records as fields and odds by the trace rule, as in the supplied companion construction.
  - Antipodal menus `{p, -p}`.

## Theorem 1 — records-only formation with independent settings: CHSH <= 2

*Statement.* In the formation reading with records-only conditioning,
suppose:
- the setting records have no parents;
- neither setting is an ancestor of the other wing's outcome.

Let `W` be the set of records that are ancestors of both outcomes. Then

`P(a, b | s_A, s_B) = sum_W P(W) P(a | s_A, W) P(b | s_B, W)`,

and `|CHSH| <= 2`.

*Proof.*
- **`W` is closed under ancestry.** An ancestor of a common ancestor is a
  common ancestor.
- **The exclusive ancestors split.** An ancestor of `a` that is not in `W`
  has no ancestor outside `W` that is also an ancestor of `b`. So the
  exclusive ancestors of `a` and of `b` are disjoint.
- **Their randomness is independent.** Their fresh randomness is
  independent of each other and of `W`.
- **Each outcome depends on its own wing.** Neither setting is an ancestor
  of the other wing or of `W`, so `a` is a function of `(s_A, W, a's
  exclusive noise)` and `b` of `(s_B, W, b's exclusive noise)`.
- **The bound follows.** Conditioning on `W` factorises the odds. Each
  factorised term is a mixture of the sixteen deterministic response
  pairs, and each of those has `|CHSH| <= 2`.

The runner checks this on three windows (a chain, a fork and a shared
source) with 9000 random kernels over binary and ternary contents:
- the joint odds, summed over every record by the formation chain rule,
  equal the mixture over the common ancestry alone, with each wing's
  exclusive ancestors integrated out, to `8e-16`;
- the largest CHSH found is `1.94`;
- the sixteen deterministic response pairs all have `|CHSH| = 2`. ∎

## Theorem 2 — two readings that leave the classical set

*Statement.*
- **(a) A path across the wings.** Let `a`'s record carry `(a, s_A)` in its
  content, and let `b = a xor (s_A and s_B)` be drawn after it. Then
  `CHSH = 4` exactly.
- **(b) Static conditioning.** The five-site binary chain
  `s_A - A - C - B - s_B`, with pair weights in `{1, 1/100}` given in the
  runner and conditioned on its end records, has CHSH exactly
  `2981272129803/1020712070201 = 2.9208`, which exceeds `2 sqrt 2`.

*Proof.* Both are exact enumerations in rational arithmetic.
- In (a) the expectations are `(1, 1, 1, -1)`.
- In (b) conditioning on both ends makes the distribution of the middle
  record depend on both settings. That is the measurement independence
  that Theorem 1 assumes. ∎

Without independence, a law can match or exceed any correlation. The Bell
bound of Theorem 1 is therefore a property of formation with
independently formed settings, not of every record law.

## Theorem 3 — the dynamics clause reaches 2 sqrt 2 and no further

*Statement.* Under the Heisenberg coupling with `J > 0`, take a pair
`A`, `B` whose other neighbours carry records with cancelling resultants,
so that by the supplied companion construction the pair is isolated with zero field.
- Its unique ground state is the singlet.
- The trace rule on antipodal menus `{+-a}`, `{+-b}` gives `E = -a.b`.
- The standard menus give `CHSH = 2 sqrt 2` exactly.
- No two-qubit state and no antipodal menus exceed `2 sqrt 2`.

*Proof.*
- `s.s = 2 SWAP - 1` has eigenvalue `-3` on the singlet and `+1` on the
  triplet.
- The correlation is the standard singlet expectation, checked
  symbolically.
- For unit menus, the Bell operator satisfies `B^2 = 4 - [A0, A1] (x) [B0, B1]`.
  Each commutator has norm at most 2, so `||B|| <= 2 sqrt 2` (Tsirelson).
- The runner checks the identity to `4e-15`, and finds a largest value of
  `2.63` over 20000 random states and menus. ∎

## Theorem 4 — sequential formation gives the same odds

*Statement.* In the setting of Theorem 3:
- let `A` record first, by the trace rule on the pair state;
- then `B` is isolated, in the field `J q_A` of `A`'s record;
- let `B` record by its ground-state law (the supplied companion construction).

The joint odds equal the singlet's joint odds for every pair of antipodal
menus.

*Proof.*
- After `A` records `+-p_A`, the trace rule leaves `B` in the state
  `-+p_A`.
- For `J > 0`, this is the ground state of `B` in the field `+-J p_A`, so
  `B`'s isolated law is exactly its conditional state.
- The runner checks 200 random menu pairs, to `8e-16`. ∎

The sequential construction uses the supplied selective projector update as well as the trace rule; neither is derived here. In the joint reading, `A`'s
odds come from the entangled pair state. That is exactly the case of open
PR 9041's scope limit: `A` has an unrecorded neighbour, so its "conditions"
include `B`'s state. After `A`'s record forms, `B` is an isolated site and
records by the isolated-site law.

## Checks

The runner prints nine checks in six families. All pass in about four
seconds:
- **A.** Deterministic response pairs.
- **B.** The mixture identity and the CHSH bound on 9000 random formation
  kernels.
- **C.** The exact value 4 for a path across the wings.
- **D.** The exact static-chain value above `2 sqrt 2`.
- **E.** The singlet ground state and `E = -a.b` (symbolic),
  `2 sqrt 2` at the standard menus, and the Tsirelson identity and bound
  over 20000 random draws.
- **F.** Sequential formation.

## What this does not do

- It does not derive the dynamics clause, the trace rule, the menus or
  how settings are chosen. The settings' independence is a hypothesis of
  Theorem 1.
- It does not treat formation orders in which a wing's setting is an
  ancestor of the other wing's outcome, except as the scope example of
  Theorem 2(a).
- It makes no claim about spacelike separation in any emergent geometry.
  "Wings" are sets of records in a formation order.
- No physical Bell experiment is modelled or compared.

## Consequence for the supplied model

Take a law that conditions on neighbour records alone and forms settings
independently. Whatever its kernels, it stays in the classical set. The
quantum value needs the conditions at a site to include an unrecorded
neighbour's state. That is what the dynamics clause supplies, as the scope
limit of the supplied companion construction already showed.

Decision points recorded: the dynamics clause (D-dyn), the trace rule
(D-tr), antipodal menus and independent settings. None is adopted.

## Causal and no-signalling qualifications

Theorem 1 uses a fixed directed acyclic formation graph, independent exogenous random variables including the setting sources, nonzero setting probabilities, and no outcome/setting postselection. An adaptive scheduler must be included among the causal variables before applying the theorem; record-only kernel syntax alone does not exclude hidden setting communication. In Theorem 2(a), the fair shared bit gives `P(a|s,t)=P(b|s,t)=1/2`: both observable marginals are no-signalling even though the construction sends setting information internally. The static chain is a supplied finite pair-weight model, not a proof of one homogeneous covariant law on the full qubit lattice.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [dynamics_clause_bell_records_only_formation_versus_dynamics_clause_2026_09_24.py](../scripts/dynamics_clause_bell_records_only_formation_versus_dynamics_clause_2026_09_24.py). Paired output: [current runner output](../logs/runner-cache/dynamics_clause_bell_records_only_formation_versus_dynamics_clause_2026_09_24.txt). All numerical historical figures above describe the declared finite setup; current tolerances and diagnostics are in this paired output.

## No-Go Discipline Gate

This section bounds the negative subclaims; it grants neither a retained grade nor an exhaustive search over physical alternatives.

### N1 — Alternative routes

- **ATTEMPTED — Local response polytope.** Exceed two with deterministic local response functions. All sixteen vertices have magnitude two, and convex mixtures preserve the bound.
- **ATTEMPTED — Causal common ancestry.** Exceed two with the stated fixed-DAG, independent-setting formation law. Conditioning on its exogenous common causes gives the local mixture.
- **ATTEMPTED — Cross-wing signalling path.** Drop causal separation while keeping operational no-signalling marginals. The explicit PR-box construction reaches four; this escapes the hypotheses and refutes the original signalling label.
- **ATTEMPTED — Static conditioning.** Replace adapted formation by end-conditioned positive chain weights. The exact rational value exceeds two root two; this is a different law class.
- **ATTEMPTED — Quantum observables.** Exceed two root two with dichotomic tensor-product observables. The squared CHSH operator gives the norm bound, attained by the supplied singlet.

These are the actual formulations tested in the argument and controls above. Successful escapes narrow the rejected broader claim; they are not counted as failed physical alternatives.

### N2 — Conditional structure

No count of independent physical walls is asserted. Dynamics, preparation and readout are supplied jointly; implication relations between possible derivations of them remain unresolved. The scoped results use their explicit hypotheses rather than an asserted wall-independence theorem.

### N3 — Hidden assumptions

The stated Hamiltonian, state preparation, record compression and readout are conditional mathematical inputs, not additions to the axioms. Numerical tolerances and finite graph sizes are diagnostics, not exact or thermodynamic proofs.

### N4 — Residual matching

No prior no-go is used to close an additional residual. Linked companion notes supply only their displayed covariance, projector or probability identities. The examples above do not certify other formation laws or physical models.

### N5 — Resolution

- `per_element:` Deterministic local binary responses and PR-box marginals are tested.
- `per_site:` Single-wing response kernels and conditioned record probabilities are tested.
- `per_mode:` checked and not executed — no propagating-mode Bell claim is made.
- `per_block:` Finite classical windows and the supplied two-qubit CHSH operator are tested.
- `lattice_wide:` checked and not executed — no unrestricted lattice formation theorem is certified.

### N6 — Partial closure

Choosing the stated supplied model yields the conditional theorem without adopting a new axiom. A convention cannot by itself select its state, dynamics or probability law. No claim that a new axiom is necessary is made.

### N7 — Strongest counter-route

An adaptive scheduler could carry a setting into the remote outcome even when a simplified record graph conceals that dependence. The exact PR-box example supplies the mechanism. A broader classical bound would have to incorporate the scheduler and prove causal separation and independent setting variables; the fixed-DAG theorem does not close that route.

### N8 — Related work

The linked companion sources are the relevant nearby arguments rechecked for this result. Their conditional boundaries are preserved here. Similar wording or a prior finite computation does not supply a universal obstruction.
