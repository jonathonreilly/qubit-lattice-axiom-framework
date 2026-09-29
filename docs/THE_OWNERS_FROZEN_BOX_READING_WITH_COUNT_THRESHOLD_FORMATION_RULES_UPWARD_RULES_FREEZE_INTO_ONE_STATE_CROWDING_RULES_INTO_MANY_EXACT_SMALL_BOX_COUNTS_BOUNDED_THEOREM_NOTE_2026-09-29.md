---
claim_id: the_owners_frozen_box_reading_with_count_threshold_formation_rules_upward_rules_freeze_into_one_state_crowding_rules_into_many_exact_small_box_counts_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "A supplied formalisation, not adopted, of the owner's reading (records form where the neighbourhood allows; a sealed box's record count rises until frozen; frozen = black hole). The axioms supply no formation rule: Admissibility governs which possibility a forming record locks, conditional on formation, not where or when records form. Sealed L^d boxes of Z^d (d = 2, 3); at most one record per site; records permanent; an empty site may form a record iff its number k of recorded nearest neighbours lies in an allowed set A; monotone growth; frozen when no empty site has k in A. (A) Upward-closed rules (A = {m, ..., 2d}): the frozen state from any start is the unique least closure; from the empty box it is the full box if 0 is in A, else the empty box. (B) Crowding rules (A = {0, ..., m}): a configuration is reachable iff its recorded set is m-degenerate, and frozen iff every empty site has more than m recorded neighbours; exact counts N of reachable frozen occupation sets on 2D boxes L = 2..5 and 3D boxes L = 2, 3 (all 28 pinned); for m = 0 these are the grid's maximal-independent-set counts. (C) Volume law for every crowding rule with m <= 2d - 1 (the Fable referee's sealed-block lemma): N_L >= N_b^(floor((L+1)/(b+1))^d), so ln N >= c L^d with explicit c > 0 (upper bound L^d ln 2). (D) For m >= d every configuration is reachable; for m = 2d - 1, N is the number of independent sets of the (L-2)^d interior. (E) Another count-threshold rule (2D, A = {0, 2, 3, 4}) has N = 1, 7, 13 on L = 2, 3, 4 with all empty sites within distance 1 of the boundary, so the class is not exhausted by the two families. No entropy identification or black-hole comparison is claimed; one conditional comparison is recorded (if the flat count were the entropy, the proved 3D m = 0 bound exceeds the area count 6L^2/4 for every L >= 19). Not shown: other formation rules in general, the exact asymptotic rates, record contents, outcome weights."
upstream_dependencies:
  - minimal_axioms
runner: scripts/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.py
---

# The owner's frozen-box reading with count-threshold formation rules: upward rules freeze into one state, crowding rules into many (exact small-box counts)

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** exact lemmas, a proved volume law for crowding rules, and
finite exact counts; unaudited. Revised after the first referee's FAILS
verdict, which withdrew the scaling and black-hole conclusions drawn from
finite counts. Revised again with the Fable referee's findings, which
supply a proof of the volume law and another rule in the class.
Independent checks are recorded below.

## In one paragraph

The owner's reading, recorded in this PR and not adopted:
- records form where their neighbourhood allows;
- a sealed box fills until nothing more can form;
- a box frozen that way is a black hole.

The axioms themselves do not say where or when records form, so this probe
supplies the simplest rules of that kind and counts the ways a sealed box
can end up frozen.
- **If more recorded neighbours never stop a record forming,** the box
  always ends in the same frozen state.
- **If crowding stops records forming,** it can end in many. The number
  of possible frozen boxes grows exponentially with the number of sites,
  for every crowding rule (proved here). For the strictest one, no two
  records side by side, it is the count of "maximal independent sets" of
  the grid.
- **Other rules exist.** One example: exactly one recorded neighbour blocks
  formation. On the small 2D boxes checked, the bulk always fills, and the
  only freedom lies within one site of the boundary.

Whether this says anything about black holes depends on which entropy the
reading means. It could be a count of possible frozen interiors, weighted
somehow, or something else, such as the entanglement across the surface
that main's area-law lane studies. The reading does not say, and this note
does not decide it.

## Pre-registration and outcome

- **Registered** (scratch, before any check): PASS if some tested rule gave
  ln N growing like the boundary; FAIL if every tested rule gave a unique
  frozen state or ln N growing like the volume.
- **Outcome:** FAIL for both registered families.
  - The upward-closed rules give a unique state (proved).
  - Every crowding rule gives ln N growing like the volume (proved in C).
- **Outside the registration:**
  - The Fable referee scanned all count-threshold rules. It found a 2D rule,
    A = {0, 2, 3, 4}, whose counts on small boxes look like the boundary
    kind (E).
  - Its 3D counts at L = 2, 3 are 11 and 10 (the referee's enumeration, not
    re-run here), so this is not an area law in 3D on the sizes seen.
  - The referee also constructed a 3D rule, A = {0, 3, 4, 5, 6}, with at
    least area growth from free tubes and a small volume rate (c ≈ 0.011).
    That is reported by the referee and not re-run here.
  - So the class of count-threshold rules contains one-state, boundary-like,
    area-like and volume behaviours.

## Prior art

On main (the review-history lane):
- Cycle 19's runner (scripts/nearest_neighbor_seed_compilation_cycle19_2026_07_14.py)
  shows random-sequential-adsorption order dependence, with different
  maximal independent sets from different schedules.
- The Cycle 26 note
  (docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md)
  records differing trajectory weights and jamming densities.
- Main's black-hole entropy lane (the area-law notes and the BH-entropy
  companion) studies entanglement across a boundary, a different quantity.

External, reference only:
- the maximal-independent-set counts of grid graphs (Oh, arXiv:1709.03678;
  OEIS A197054);
- jammed-state configurational entropy against random-sequential-adsorption
  outcome weights: a flat count is not the entropy of the process
  (Došlić et al., arXiv:2302.08791);
- bootstrap percolation, which is order-independent.

## Premises (supplied)

- **Box.** A sealed L^d box of Z^d, d = 2 or 3. Neighbours outside it count
  as unrecorded.
- **Records.** At most one per site, and permanent.
- **Formation rule.** An empty site may form a record iff its number k of
  recorded nearest neighbours lies in an allowed set A. This formalises the
  owner's reading. It is not the Admissibility axiom, which, read with
  Record, concerns which possibility a forming record locks, not the
  formation site or rate.
- **Frozen.** No empty site has k in A.
- **The count N.** The number of distinct frozen occupation sets reachable
  from the empty box. It is a flat count, not the outcome distribution of
  any process.

## A — upward-closed rules: one frozen state (check A)

- If A = {m, …, 2d}, growth is monotone and adding records never removes
  eligibility. So the frozen state is the least closed set containing the
  start, whatever the order of events.
- Checked for every m on 5² and 3³ boxes, from random starts and orders.
- From the empty box the result is the full box if 0 ∈ A, and the empty box
  otherwise.

## B — crowding rules: exact counts (check B)

With A = {0, …, m} (a record forms only if at most m neighbours are
recorded):
- **Reachable** iff the recorded set is m-degenerate: reverse an addition
  order.
- **Frozen** iff every empty site has more than m recorded neighbours.

All 28 counts are pinned in the runner:

| d | m | N for L = 2, 3, 4, 5 (2D) or L = 2, 3 (3D) |
| --- | --- | --- |
| 2 | 0 | 2, 10, 42, 358 (maximal independent sets) |
| 2 | 1 | 6, 57, 1699, 144205 |
| 2 | 2 | 1, 17, 305, 22398 |
| 2 | 3 | 1, 2, 7, 63 |
| 3 | 0 | 6, 496 |
| 3 | 1 | 40, 379531 |
| 3 | 2 | 34, 413615 |
| 3 | 3 | 1, 12274 |
| 3 | 4 | 1, 65 |
| 3 | 5 | 1, 2 |

## C — a volume law for every crowding rule (check C)

The Fable referee's sealed-block lemma:
- Let T be a b^d block. Let R_T ⊂ T be m-degenerate, with every empty
  site of T having more than m recorded neighbours inside T.
- Build R_T first. Adding records outside T never touches T: an empty site
  of T only gains recorded neighbours, so it stays ineligible.
- Place floor((L+1)/(b+1))^d such blocks at gap 1. Choose any sealed-box
  frozen state in each, then complete by any growth in the corridors.
- Distinct choices give distinct reachable frozen states. So
  N_L ≥ N_b^(floor((L+1)/(b+1))^d).

Consequences:
- ln N ≥ c L^d asymptotically, with c = ln N_b / (b+1)^d > 0 whenever
  N_b ≥ 2. Every crowding rule with m ≤ 2d − 1 has such a b in the table,
  and the upper bound is L^d ln 2.
- The best per-site lower bounds from the table:

  | d | m = 0 | m = 1 | m = 2 | m = 3 | m = 4 | m = 5 |
  | --- | --- | --- | --- | --- | --- | --- |
  | 2 | 0.163 | 0.330 | 0.278 | 0.115 | | |
  | 3 | 0.097 | 0.201 | 0.202 | 0.147 | 0.065 | 0.011 |

- The construction is checked on five box sizes. It is exhaustive where
  feasible: 16, 1296 and 10⁴ distinct states, exactly N_b^(blocks). The
  others are sampled.

## D — two exact facts (check D)

- **m ≥ d.** Every configuration is m-degenerate: the lexicographically
  least recorded site has at most d recorded neighbours. So every frozen
  set is reachable.
- **m = 2d − 1.** A frozen set has a full boundary, because a boundary site
  has fewer than 2d neighbours. Its empty interior sites form an independent
  set, and every independent set works. So N is the number of independent
  sets of the (L − 2)^d interior: 1, 2, 7, 63 in 2D and 1, 2 in 3D, as in
  the table.

## E — another rule (check E)

- 2D, A = {0, 2, 3, 4}: a record forms unless exactly one neighbour is
  recorded.
- N = 1, 7, 13 for L = 2, 3, 4. The referee's C enumeration gives 27 at
  L = 5.
- In every frozen state the empty sites lie within distance 1 of the
  boundary.
- Neither family covers this rule. It is recorded as a member of the class,
  not analysed further.

## What the reading would need

A black hole's entropy grows with its surface area. For "frozen box =
black hole" to hold at the level of entropy, the reading needs three
things:
- **an identified entropy.** A flat count of frozen interiors, the
  entropy of the formation process's outcome distribution, or the
  entanglement across the surface (main's lane) are different quantities.
- **a formation rule.** Upward-closed rules leave no freedom, so the flat
  count is 1. Crowding rules make it grow with the volume (C). E shows a
  rule whose freedom sits at the boundary on small 2D boxes.
- **only if the flat count were the entropy:** C's proved bound for 3D
  m = 0 exceeds the area count 6L²/4, in lattice-Planck units, for every
  L ≥ 19. This comparison is conditional and is not adopted.
- **a scale and a coefficient.** The scale primitive declares a⁻¹ = M_Pl as
  a units conversion with no dimensionless content. The black-hole
  coefficient, ¼ in S = A/4 (G in lattice units), is dimensionless content
  that main's BH-entropy lane treats as an open gate.

This probe supplies none of these. It only shows which formation rules
leave the frozen box free and which do not.

## No-Go Discipline Gate

The note makes no no-go claim. It records structural lemmas (A, B, C, D),
exact finite counts, and one rule outside the families (E).
- The volume law in C is a positive growth theorem for the crowding
  family.
- The earlier sentence "volume, not area", read as excluding a black-hole
  entropy, is not restored. E shows that the rule class is wider than the
  two families. The N5 certificate
lines are kept in the runner output.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: FAILS.** Its findings, and how
  this version answers each:
  1. "Volume, not area" is not established by finite counts. Withdrawn.
  2. The combinatorial core was verified independently (all counts, both
     lemmas).
  3. The formalisation was attributed to Admissibility. Corrected: it is
     the owner's reading.
  4. The black-hole comparison lacked a physical bridge. Withdrawn to "what
     the reading would need".
  5. The gate. The no-go is withdrawn, so none is claimed.
  6. The runner under-asserted. All 28 counts are now pinned.
  7. Prior art. The repo's Cycle 19 and 26 work, the maximal-independent-set
     literature, and the RSA-weights literature are added.
- **Fable check (same family; it reviewed the first version): FAILS as
  titled.** A, B and every count were reproduced by an exhaustive
  predecessor enumeration, with no error. Its findings, and how this
  version answers each:
  1. Prove the upward-closed uniqueness. Given in A's lemma (least
     closure).
  2. Add the m ≥ d and m = 2d − 1 facts. Added (D).
  3. The volume law is a theorem; supply it. Added (C), with the rigorous
     per-site bounds.
  4. The crossover size should be a rigorous bound. Stated conditionally:
     L ≥ 19 for every larger L, computed from C.
  5. Other rules break the dichotomy. Recorded (E, and the outcome
     section). The title already names only the two families.
  6. Overreach in the title and "a few lattice spacings". The first
     version's title and scaling claims were already withdrawn in the
     second version; nothing here restores them.
- **gpt-5.6-sol, second round:** pending.

## Reproduction

`python3 scripts/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in about 2 minutes. The canonical
cache is at
logs/runner-cache/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.txt.
