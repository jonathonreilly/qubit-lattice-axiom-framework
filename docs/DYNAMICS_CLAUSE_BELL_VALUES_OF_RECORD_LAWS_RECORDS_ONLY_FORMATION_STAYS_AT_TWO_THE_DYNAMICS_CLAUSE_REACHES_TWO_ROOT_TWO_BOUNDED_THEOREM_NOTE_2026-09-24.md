---
claim_id: dynamics_clause_bell_values_of_record_laws_records_only_formation_stays_at_two_the_dynamics_clause_reaches_two_root_two_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "CHSH values of record laws under four supplied readings, none adopted. (1) Formation reading, records-only conditioning: each record is a function of the records already formed at its neighbours and of fresh local randomness. If both setting records form with no parents and neither is an ancestor of the other wing's outcome, the joint odds are a mixture over the common ancestry of products of one-wing odds, so |CHSH| <= 2. Checked on 9000 random kernels over three windows, largest 1.94. (2) If a record carrying one wing's setting is an ancestor of the other wing's outcome, |CHSH| = 4 exactly. (3) Static reading conditioned on its end records: a five-site binary chain reaches the exact rational 2981272129803/1020712070201 > 2 sqrt 2. (4) The dynamics clause of open PR 9040 with records as fields and the trace rule of open PR 9041: the antiferromagnetic Heisenberg bond of an isolated pair has the singlet as ground state, antipodal menus give E = -a.b and CHSH = 2 sqrt 2 exactly, and no state or antipodal menus exceed 2 sqrt 2. Sequential formation (A by the trace rule, then B by its isolated ground-state law in the field of A's record) reproduces the singlet odds. The dynamics clause, the trace rule, the menus and the setting mechanism are supplied, not derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_bell_records_only_formation_versus_dynamics_clause_2026_09_24.py
---

# Bell values of record laws: records-only formation stays at 2, the dynamics clause reaches 2 sqrt 2

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite results and one classical theorem applied to supplied readings; unaudited.

## Result and scope

Open PR 9041 found that the odds at a site with an unrecorded neighbour
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

The last row is the quantum value. The dynamics clause of open PR 9040
reaches it and does not go beyond it:
- The antiferromagnetic Heisenberg bond of an isolated pair has the
  singlet as its ground state.
- Read by the trace rule on antipodal menus, the singlet gives
  `E = -a.b`, hence `2 sqrt 2`.
- Records can also form one at a time. Once A's record exists, B is an
  isolated site in the field of A's record, and B's law is the
  isolated-site law of open PR 9041. The two orders give identical odds.

The middle rows show why the hypotheses matter. A record that carries a
setting across the wings gives the no-signalling-violating value 4. A
static law conditioned on its own setting records post-selects and exceeds
the quantum value.

So the four axioms read with formation and records-only conditioning
cannot give the quantum correlations. The dynamics clause gives exactly
the quantum value.

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
  - The generator of open PR 9040 with the Heisenberg coupling.
  - Records as fields and odds by the trace rule, as in open PR 9041.
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
so that by open PR 9041 the pair is isolated with zero field.
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
- let `B` record by its ground-state law (open PR 9041).

The joint odds equal the singlet's joint odds for every pair of antipodal
menus.

*Proof.*
- After `A` records `+-p_A`, the trace rule leaves `B` in the state
  `-+p_A`.
- For `J > 0`, this is the ground state of `B` in the field `+-J p_A`, so
  `B`'s isolated law is exactly its conditional state.
- The runner checks 200 random menu pairs, to `8e-16`. ∎

The quantum correlation needs no extra rule. In the joint reading, `A`'s
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

## Consequence for the campaign

Take a law that conditions on neighbour records alone and forms settings
independently. Whatever its kernels, it stays in the classical set. The
quantum value needs the conditions at a site to include an unrecorded
neighbour's state. That is what the dynamics clause supplies, as the scope
limit of open PR 9041 already showed.

Decision points recorded: the dynamics clause (D-dyn), the trace rule
(D-tr), antipodal menus and independent settings. None is adopted.
