---
claim_id: the_owners_frozen_box_reading_with_count_threshold_formation_rules_upward_rules_freeze_into_one_state_crowding_rules_into_many_exact_small_box_counts_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "A supplied formalisation, not adopted, of the owner's reading (records form where the neighbourhood allows; a sealed box's record count rises until frozen; frozen = black hole). The axioms supply no formation rule: Admissibility governs which possibility a forming record locks, conditional on formation, not where or when records form. Sealed L^d boxes of Z^d (d = 2, 3); at most one record per site; records permanent; an empty site may form a record iff its number k of recorded nearest neighbours lies in an allowed set A; monotone growth; frozen when no empty site has k in A. (A) Upward-closed rules (A = {m, ..., 2d}): the frozen state from any start is the unique least closure; from the empty box it is the full box if 0 is in A, else the empty box. (B) Crowding rules (A = {0, ..., m}): a configuration is reachable iff its recorded set is m-degenerate, and frozen iff every empty site has more than m recorded neighbours; exact counts N of reachable frozen occupation sets on 2D boxes L = 2..5 and 3D boxes L = 2, 3 (all 28 pinned); for m = 0 these are the grid's maximal-independent-set counts. No asymptotic scaling, entropy identification or black-hole comparison is claimed from these finite counts; the note records what the reading would need. Not shown: other formation rules, record contents, outcome weights, larger sizes."
upstream_dependencies:
  - minimal_axioms
runner: scripts/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.py
---

# The owner's frozen-box reading with count-threshold formation rules: upward rules freeze into one state, crowding rules into many (exact small-box counts)

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** two exact lemmas and finite exact counts; unaudited. Revised
after the first referee's FAILS verdict, which withdrew the scaling and
black-hole conclusions. Independent checks are recorded below.

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
- **If crowding stops records forming,** it can end in many. For the
  strictest crowding rule, no two records side by side, the number is the
  count of "maximal independent sets" of the grid. That count is known to
  grow with the number of sites.

Whether this says anything about black holes depends on which entropy the
reading means. It could be a count of possible frozen interiors, weighted
somehow, or something else, such as the entanglement across the surface
that main's area-law lane studies. The reading does not say, and this note
does not decide it.

## Pre-registration and outcome

- **Registered** (scratch, before any check): PASS if some tested rule gave
  ln N growing like the boundary; FAIL if every tested rule gave a unique
  frozen state or ln N growing like the volume.
- **Outcome:**
  - The upward-closed rules give a unique state (proved).
  - For the exclusion rule (m = 0), volume growth is known from the
    literature, not from these counts.
  - For m ≥ 1 the finite counts cannot decide the scaling.

  So the registered test is decided (FAIL) only for the upward-closed and
  exclusion rules.

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

## What the reading would need

A black hole's entropy grows with its surface area. For "frozen box =
black hole" to hold at the level of entropy, the reading needs three
things:
- **an identified entropy.** A flat count of frozen interiors, the
  entropy of the formation process's outcome distribution, or the
  entanglement across the surface (main's lane) are different quantities.
- **a formation rule.** Upward-closed rules leave no freedom, so the flat
  count is 1. Under the exclusion rule the flat count grows with the number
  of sites (literature).
- **a scale and a coefficient.** The scale primitive declares a⁻¹ = M_Pl as
  a units conversion with no dimensionless content. The black-hole
  coefficient, ¼ in S = A/4 (G in lattice units), is dimensionless content
  that main's BH-entropy lane treats as an open gate.

This probe supplies none of these. It only shows which formation rules
leave the frozen box free and which do not.

## No-Go Discipline Gate

The note makes no no-go claim. It records two structural lemmas (A, B)
and exact finite counts. The earlier no-go ("volume, not area") is
withdrawn, and no residual sentence functions as one. The N5 certificate
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
- **Fable check:** pending (it is reviewing the first version).

## Reproduction

`python3 scripts/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.py`
prints 2 checks, the N5 lines and TOTAL, in about 2 minutes. The canonical
cache is at
logs/runner-cache/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.txt.
