---
claim_id: the_owners_frozen_box_reading_with_count_threshold_formation_rules_upward_rules_freeze_into_one_state_crowding_rules_into_many_exact_small_box_counts_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "A supplied formalisation, not adopted, of the owner's reading (records form where the neighbourhood allows; a sealed box's record count rises until frozen; frozen = black hole). The axioms supply no formation rule: Admissibility governs which possibility a forming record locks, conditional on formation, not where or when records form. Sealed L^d boxes of Z^d (d = 2, 3); at most one record per site; records permanent; an empty site may form a record iff its number k of recorded nearest neighbours lies in an allowed set A; monotone growth; frozen when no empty site has k in A. (A) Upward-closed rules (A = {m, ..., 2d}): the frozen state from any start is the unique least closure; from the empty box it is the full box if 0 is in A, else the empty box. (B) Crowding rules (A = {0, ..., m}): a configuration is reachable iff its recorded set is m-degenerate, and frozen iff every empty site has more than m recorded neighbours; exact counts N of reachable frozen occupation sets on 2D boxes L = 2..5 and 3D boxes L = 2, 3 (all 28 pinned); for m = 0 these are the grid's maximal-independent-set counts. (C) Volume law for every crowding rule (m <= 2d - 1; m = 2d blocks nothing and fills the box) (the Fable referee's sealed-block lemma): N_L >= N_b^(floor((L+1)/(b+1))^d), so liminf ln N_L / L^d >= c with explicit c > 0 (upper bound L^d ln 2). (D) For m >= d every configuration is reachable; for m = 2d - 1, N is the number of independent sets of the (L-2)^d interior. (E) Another count-threshold rule (2D, A = {0, 2, 3, 4}) has N = 1, 7, 13 on L = 2, 3, 4 (27 at L = 5 by two referees' independent enumerations), growing far more slowly than any crowding rule on these sizes; its empty sites form strips, which need not touch the boundary; so the class is not exhausted by the two families. No entropy identification or black-hole comparison is claimed; one conditional comparison is recorded (if the flat count were the entropy, the lattice spacing the Planck length, the box's surface a horizon and the quarter coefficient imported, the proved 3D m = 0 bound would exceed the area count 6L^2/4 for every L >= 19). Not shown: other formation rules in general, the exact asymptotic rates, record contents, outcome weights."
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
  formation. On the small 2D boxes checked, the number of frozen boxes
  grows far more slowly than for crowding. Its empty sites form narrow
  strips, which need not touch the boundary.

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
    A crowding rule is one with m ≤ 2d − 1; m = 2d blocks nothing and
    fills the box.
- **Outside the registration:**
  - The Fable referee scanned all count-threshold rules. It found a 2D rule,
    A = {0, 2, 3, 4}, whose counts on small boxes grow slowly: 1, 7, 13, 27
    (E).
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

With A = {0, …, m}, where m ≤ 2d − 1 (a record forms only if at most m
neighbours are recorded; m = 2d would block nothing):
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
- liminf ln N_L / L^d ≥ c, with c = ln N_b / (b+1)^d > 0 whenever N_b ≥ 2.
  The floor in the bound means this holds in the limit, not pointwise for
  every L. Every crowding rule with m ≤ 2d − 1 has such a b in the table,
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
- N = 1, 7, 13 for L = 2, 3, 4. Two referees' independent enumerations
  give 27 at L = 5.
- The empty sites form strips of width at most 2. They need not touch the
  boundary. The second-round referee's example at L = 5 records columns 0,
  3 and 4 and leaves columns 1 and 2 empty; it is frozen and reachable
  (checked in E).
- The counts grow far more slowly than any crowding rule's on these sizes
  (ln N / L ≈ 0.65 for L = 3–5). Neither family covers this rule. It is
  recorded as a member of the class, not analysed further.

## What the reading would need

A black hole's entropy grows with its surface area. For "frozen box =
black hole" to hold at the level of entropy, the reading needs three
things:
- **an identified entropy.** A flat count of frozen interiors, the
  entropy of the formation process's outcome distribution, or the
  entanglement across the surface (main's lane) are different quantities.
- **a formation rule.** Upward-closed rules leave no freedom, so the flat
  count is 1. Crowding rules make it grow with the volume (C). E shows a
  rule with much slower growth on small 2D boxes.
- **A conditional comparison.** Assume all of the following:
  - the flat count is the entropy;
  - the lattice spacing is the Planck length (the scale primitive declares
    a unit and does not derive this);
  - the box's surface is a horizon;
  - the ¼ coefficient is imported.

  Then C's proved bound for 3D m = 0 exceeds the area count 6L²/4 for
  every L ≥ 19. The comparison is not adopted.
- **a scale and a coefficient.** The scale primitive declares a⁻¹ = M_Pl as
  a units conversion with no dimensionless content. The black-hole
  coefficient, ¼ in S = A/4 (G in lattice units), is dimensionless content
  that main's BH-entropy lane treats as an open gate.

This probe supplies none of these. It only shows which formation rules
leave the frozen box free and which do not.

## No-Go Discipline Gate

The registered outcome is negative, so the gate applies. The bounded
negative claim: for the two registered families of supplied count-threshold
rules in sealed boxes, the flat count of reachable frozen states does not
grow like the boundary. It is 1 for upward-closed rules, and grows like the
volume for crowding rules (m ≤ 2d − 1). No claim is made about black holes,
other rules or weighted counts.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *Order dependence reduces the count.* ATTEMPTED (A: the least closure
     is order-independent; B: reachable iff m-degenerate). Fails.
  2. *The sealed boundary pins the interior.* ATTEMPTED (C: interior blocks
     at gap 1 are unaffected by any completion; D: at m = 2d − 1 the
     boundary is forced full but the interior stays free). Fails.
  3. *Few reachable states for large m.* ATTEMPTED (D: for m ≥ d every
     frozen set is reachable; the table's N_b ≥ 2 for every m ≤ 2d − 1).
     Fails.
  4. *The finite sizes mislead about the limit.* ATTEMPTED (C: a proved
     liminf bound; upper bound L^d ln 2). Fails.
  5. *The count is dominated by boundary-attached states.* ATTEMPTED (C's
     blocks are interior; their number grows like L^d). Fails.
  6. *A rule outside the families.* ATTEMPTED for one rule (E): much slower
     growth. Not classified, so it is a domain escape, not a failed attack.

  **Domain escapes** (outside the premises, not claimed):
  - other formation rules;
  - process weights instead of flat counts (random sequential adsorption
    weights differ; Došlić et al.);
  - recorded (non-empty) outer boundaries;
  - record contents;
  - any identification of entropy.
- **N2 — pairwise table, with directions.**
  - W1: count-threshold formation rules of the two families (supplied).
  - W2: one permanent record per site.
  - W3: a sealed box whose outside counts as unrecorded.
  - W4: the flat count (no weights).
  - W5: reachability from the empty box.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: a rule says when a site may form, not how many records it may hold | no: permanence and uniqueness fix no threshold | independent |
  | W1, W3 | no: rules are local and say nothing of the box's edge | no: an edge convention fixes no rule | independent |
  | W1, W4 | no: a rule defines dynamics, not how outcomes are weighted | no: a counting convention fixes no rule | independent |
  | W1, W5 | no: the rule does not fix the start | no: the start fixes no rule | independent |
  | W2, W3 | no | no | independent: site occupancy versus the edge convention |
  | W2, W4 | no: permanence does not fix weights | no | independent |
  | W2, W5 | no: permanence allows any start | no: a start does not force permanence | independent |
  | W3, W4 | no | no | independent: the edge convention versus the counting convention |
  | W3, W5 | no | no | independent: the edge convention versus the start |
  | W4, W5 | no: flat counting allows any start | no: the start fixes no weights | independent |

  The claim uses all five. Dropping W4 (weights) or W1 (other rules) are
  the recorded escapes.
- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "sealed": explicit (W3);
  - "flat": explicit (W4);
  - "nearest-neighbour": part of W1;
  - "permanent": explicit (W2);
  - "box": the finite sizes are resolved by C's limit;
  - "registered": stated, with the Fable rule E outside it.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | docs/MINIMAL_AXIOMS_2026-06-29.md:68 | Admissibility supplies no formation site, probability or rate | the rule is supplied, not derived | yes |
  | scripts/nearest_neighbor_seed_compilation_cycle19_2026_07_14.py:10 | random-sequential-adsorption order dependence | counted as distinct reachable states (B) | yes |

  Both are context, not load-bearing proofs.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "one state" (upward-closed) | each start's closure | the rule at every site | not applicable | 5² and 3³ boxes | proved (least closure) for every box |
  | "grows like the volume" (crowding) | each constructed state checked frozen and reachable | the rule at every site | not applicable | five box sizes | proved as a liminf for every m ≤ 2d − 1 (C) |

- **N6 — primitive scan.** No primitive is invoked, and the formation rule
  is marked supplied. The scale primitive appears only in the conditional
  comparison, where it is noted that it does not derive a = l_P.
- **N7 — steelman, in a hostile reviewer's voice.** "The owner's reading
  need not be a count-threshold rule. Records may form by a weighted
  process, and a black hole's entropy counts microstates compatible with a
  macrostate, not frozen outcomes of one process. The area law may be
  entanglement across the surface (main's area-law lane), not a count of
  interiors. E already shows that the class contains slower-growing rules;
  the terminal obligation is a classification of formation rules and an
  identified entropy." Convincing against any broad claim. So none is made,
  and the note is limited to the two families' flat counts.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism | Applies here? |
  | --- | --- | --- | --- |
  | Cycle 19/26 order dependence of adsorption | no | distinct schedules give distinct maximal independent sets | yes: it is why the count is large |
  | probe 7: under a unitary wave the record count never rises | no | reversibility | outside: formation here is supplied and irreversible |

- **Outcome.** PASS as scoped. The registered outcome is FAIL for both
  families.

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
- **gpt-5.6-sol, second round: FAILS.**
  - Resolved: findings 1–3, 6 and 7. The referee closed C's proof
    independently: reverse peeling builds each block, gap-one blocks share
    no edges, holes stay ineligible under every completion, and restrictions
    distinguish the choices. It also checked the L ≥ 19 bound interval by
    interval, and confirmed D.
  - Its findings, and how this version answers each:
    - The conditional comparison imported more than the flat count. All
      four assumptions are now listed.
    - "Outcome: FAIL" is a negative trigger that needs the full gate. N1–N8
      are now written.
    - E's boundary claim is false at L = 5: its example leaves an interior
      column empty. The claim is withdrawn, and the example is checked in E.
    - Write C as a liminf, and bound crowding rules by m ≤ 2d − 1. Both
      applied.
- **gpt-5.6-sol, third round:** pending.

## Reproduction

`python3 scripts/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in about 2 minutes. The canonical
cache is at
logs/runner-cache/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.txt.
