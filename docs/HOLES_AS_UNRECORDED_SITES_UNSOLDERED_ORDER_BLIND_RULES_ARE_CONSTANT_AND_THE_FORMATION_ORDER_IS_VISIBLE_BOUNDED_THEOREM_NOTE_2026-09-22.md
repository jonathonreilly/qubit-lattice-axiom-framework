---
claim_id: holes_as_unrecorded_sites_unsoldered_order_blind_rules_are_constant_and_the_formation_order_is_visible_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading with the Record and Qualification text's semantics for holes: a site whose neighbour condition lies outside the rule's domain carries no record, cannot be read, and formation continues; a finished state is a configuration of records. Under the unsoldered reading, on every alphabet, an order-blind nearest-neighbour rule normalised on its domain has every occurring condition in its domain and is constant there; in the sub-probability model with deficits as unrecorded sites, order-blindness forces a constant hole rate and constant values. Hence every admissible unsoldered rule makes the formation order visible in finished states. Exact exhibits on two sites, the bent path, the 4-site star and the 7-site cross, including the contrast with the drop convention. No rule, reading or order law is selected."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - formation_order_covariance_and_isotropic_binary_order_blind_classification_bounded_theorem_note_2026-09-13
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
runner: scripts/holes_as_unrecorded_sites_unsoldered_order_blind_rules_constant_2026_09_22.py
---

# Holes as unrecorded sites: unsoldered order-blind rules are constant, and the formation order is visible

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The two previous blocks of this
continuation (open PRs 8663 and 8664) showed that under the unsoldered
reading only rules with holes can be order-blind and vary, and only
when failed histories are dropped. This block asks what the axiom text
says a hole is.

## Result up front

1. **The text reads a hole as an unrecorded site.** Record: "When
   present, a record locks exactly one admissible local possibility …
   A site with no record cannot be read." Qualification: "A state is a
   configuration of records", and a law "gives exactly one answer" where
   its supplied condition holds. A site whose neighbour condition has no
   admissible possibility therefore carries no record, its neighbours
   cannot read it, and formation continues. Nothing in the text discards
   the history. The drop convention used for completion masses
   (support-rule, clock-and-rate, formation-unit, and the previous block)
   is a conditioning the text does not supply.

2. **Under that semantics, unsoldered order-blind rules are constant.**
   Take a rule normalised on its domain (reading note 3: the distribution
   is a probability measure). On two adjacent sites, the later site
   of either order may land outside the domain while the earlier never
   does, so order-blindness puts every one-neighbour condition that
   occurs inside the domain. The star extends this to every occurring
   condition. The rule then never fails where it acts, and the previous
   block's variance theorem makes it constant. The sub-probability model,
   with deficits as unrecorded sites, gives the same conclusion: the two
   orders of a pair differ by r0(a)(delta(a) - delta0), so the hole rate
   is constant, and the rule normalised on the no-hole event is constant.
   Only constant values with a constant erasure rate survive.

3. **Every admissible unsoldered rule makes the formation order
   visible.** With the variation sentence, the formation order enters
   the finished state for every admissible rule under the unsoldered
   reading, on every alphabet, with or without holes. The clock
   decision's candidate "order-blind physical rule" is excluded outright.
   What remains is which order law holds.

4. **Hole locations carry the order.** For deficit rejection on a pair,
   the unrecorded site is always the later-formed one (probability 1/2),
   while under the drop convention the two orders agree. On the 7-site
   cross with the centre formed k-th (k = 1..7), the deficit rejection and
   soft pair rules of the previous block give 7 distinct finished-state
   laws, against 1 under the drop convention. Binary exclusion normalised
   on its domain gives 6. Constant erasure (hole rate 1/3, fair values) is
   order-blind on all 24 orders of the 4-site star, and it does not vary.

5. **Combined with the previous blocks.** Under the text's semantics,
   order-blind admissible formation exists only under the soldered
   reading, on alphabets such as the generic 24-point orbit and the
   sphere, and with nearest-neighbour reach only. So every admissible
   formation law whose records correlate beyond nearest neighbours makes
   the formation order visible, in both readings of covariance. The
   completion masses of the clock-and-rate and formation-unit blocks are
   the probabilities of no unrecorded site under this semantics, so they
   stand unchanged.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the order-blind escape of the previous block uses the drop convention for holes; determine the text's semantics of a hole and whether the escape survives it"
source_of_blocker_text: open_pr_8664_n7_and_boundaries
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry into the re-assembly: under the text's hole semantics the formation order is visible for every admissible unsoldered rule and for every admissible rule with reach beyond nearest neighbours; the clock decision reduces to the choice of order law"
conditional_surface_status: "formation reading; the Record and Qualification sentences read as fixing the semantics of a site with no admissible possibility; one formation attempt per site; no rule, reading or order law selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the theorems are short proofs on the two-site and star windows valid for every alphabet; every exhibit is an exact rational computation over declared orders"
```

## Premises and declared objects

The Record, Qualification and Admissibility sentences quoted above;
reading note 2 (the distribution does not supply the formation site,
probability or rate) and reading note 3 (the distribution is a
probability measure; admissible means its support). A domain rule gives a
normalised distribution at every condition of its domain and has no
admissible possibility outside it. A deficit rule is the previous block's
sub-probability model, kept for comparison because its deficit is a
formation probability that reading note 2 does not supply. Each site
has one formation attempt, at its place in the order; a site with no
admissible possibility stays unrecorded and is read as absent by its
neighbours. Unsoldered reading: the rule is unchanged when formed
neighbours' positions are rotated with their values fixed, so a single
formed neighbour's conditional does not depend on its direction, the
property the proofs use; the example rules are direction-blind. Windows and example rules as declared in the runner.

## Prior art and what is new

- Open PRs 8663 and 8664 (this continuation): never-failing unsoldered
  order-blind rules are constant (with and without positivity); under the
  drop convention, order-blind hole rules have pair form and a clock-blind
  hole mass. New here: the text's semantics of a hole removes that escape
  and makes the formation order visible for every admissible unsoldered
  rule.
- Landed support-rule note and open clock-and-rate and formation-unit PRs
  (8641, 8643): completion masses under the drop convention. New here:
  those masses are the no-unrecorded-site probabilities under the text's
  semantics, so they stand; what the drop convention hid is the
  hole location, which carries the order.

## Theorem 1 — Domain rules: order-blind means no holes and a constant rule

Let an unsoldered nearest-neighbour rule, normalised on its domain D, be
order-blind on the 7-site cross, with holes read as unrecorded sites.
The empty condition lies in D, or no site ever records. On two adjacent
sites x, y: with x first, P(x = a, y unrecorded) = r0(a) 1[{a} not in D];
with y first, y records at the empty condition, so this probability is 0.
Hence {a} lies in D for every a with r0(a) > 0. On the star, leaves first
gives P(leaves b_i, centre unrecorded) = prod r0(b_i) 1[N not in D];
centre first gives 0. So every occurring condition lies in D. The rule
never fails where it acts, and the previous block's Theorem 1 makes it
constant there.

## Theorem 2 — Deficit rules: order-blind means constant erasure and constant values

Let an unsoldered sub-probability rule, with deficits read as unrecorded
sites, be order-blind on the 7-site cross. With delta(N) the deficit at
N: the pair gives r0(a) delta({a}) = delta0 r0(a), and the star gives
prod r0(b_i) delta(N) = delta0 prod r0(b_i), so delta(N) = delta0 on every
occurring condition. The event that no site is unrecorded then has
probability (1 - delta0)^n in every order. On that event the finished law
is the product of r(. | N) / (1 - delta0) along the order, a never-failing
order-blind rule, so it is constant. Only constant values with a
constant erasure rate survive, and they do not vary.

## Theorem 3 — Exhibits

Exact exhibits on declared windows: deficit rejection on a pair leaves
the later site unrecorded with probability 1/2 in either order, so the
two orders differ, while the drop convention makes them agree (mass
1/2). Hole rates delta(a) = 1/2 (rejection) and 1/4 (soft pair) against
delta0 = 0. Binary exclusion normalised on its domain never leaves the
domain on a pair, but on the bent path it leaves the centre unrecorded
with probability 1/2 (leaves first) or 0 (centre first). On the 7-site
cross, with the centre formed k-th, there are 7, 7 and 6 distinct
finished-state laws for deficit rejection, soft pair and domain
exclusion, and 1, 1 and 6 under the drop convention. Six-axis exclusion
on the 4-site star never leaves its domain and is order-sensitive
through its values. Constant erasure is order-blind on all 24 star
orders.

## No-Go Discipline Gate

The negative content is scoped: under the text's hole semantics and the
unsoldered reading, no admissible nearest-neighbour rule is order-blind.

- **N1 alternative routes.** Retrying formation at an unrecorded site,
  formation probabilities supplied beyond the Admissibility sentence,
  and the soldered reading (order-blind rules with nearest-neighbour
  reach, previous blocks) are outside Theorem 1.
- **N2 wall independence.** Exchange-type comparisons on the pair and
  star; no dynamics or clock input.
- **N3 hidden walls.** The semantics of a hole is read from the Record
  and Qualification sentences; one formation attempt per site is a stated
  premise. The exhibits use declared orders (centre formed k-th), not all
  orders.
- **N4 residual matching.** The clock decision's residual is the choice
  of order law; its order-blind candidate is excluded under the unsoldered
  reading and confined to nearest-neighbour reach under the soldered one.
- **N5 rhetoric audit.** "Excluded" and "visible" are used only under
  the stated semantics and reading.
- **N6 partial-closure paths.** Retry semantics and soldered hole rules
  are open continuations.
- **N7 steelman.** Against item 1: one could read a failed formation as
  a history that never happened. The text gives no such rule, and reading
  note 2 withholds formation probabilities from the law. The drop
  convention is kept as a named comparison, not discarded.
- **N8 cross-cycle echo.** The previous blocks' theorems are used, and
  their drop-convention results are restated as conditional on that
  convention.

## Falsifiers

- An unsoldered domain rule, order-blind on the 7-site cross under
  unrecorded-site semantics, with an occurring condition outside its
  domain or varying on occurring conditions, falsifies Theorem 1.
- A deficit rule order-blind under the same semantics with a
  non-constant hole rate on occurring conditions falsifies Theorem 2.
- Any listed exact value or law count failing its recomputation
  falsifies Theorem 3.

## Boundaries and non-claims

No rule, reading, order law or clock is selected. One formation attempt
per site is assumed; a retry semantics is not analysed. The soldered
reading's order-blind rules (nearest-neighbour reach) are the previous
blocks'. No physical identification is made. Nothing here grades,
unlocks or audits any other claim.

## Imports

The axiom sentences quoted; supplied windows and example rules; the
previous blocks' theorems. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) finished-state laws computed by exact
  dynamic programmes over partial states with unrecorded marks, under
  both conventions from one routine with a flag, so the difference
  isolates the convention; (ii) hole rates read directly from the rules
  and compared with the two-site order difference; (iii) the erasure
  rule's order-blindness checked on all 24 orders of the star.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| unrecorded sites read as formed | hole mark treated as a value | caught (crash, nonzero exit) |
| deficit not recorded as a hole | hole branch removed | caught (4 FAILs) |
| drop flag ignored | holes kept under the drop convention | caught (1 FAIL) |
| rejection allows clashes | exclusion removed | caught (4 FAILs) |
| domain rule not normalised | 1/len(allowed) to 1/len(alphabet) | caught (3 FAILs) |
| erasure rate depends on neighbours | delta0 to delta0 x count | caught (1 FAIL) |
| states not re-indexed by site | order indexing kept | caught (2 FAILs) |
| soft weight value part dropped | K to the constant 3/4 | caught after strengthening (1 FAIL; the soft rule's values are now pinned) |

  Eight of eight mutants are caught, one after the strengthening.
- **Vacuity guard:** every law count compares separately computed laws;
  the drop and unrecorded conventions run through one routine, so any
  difference is the convention's.
- **Budget:** 10 checks, stdout 1810 characters (ceiling 6000), 0.15 s
  (ceiling 900 s), exact Fractions; no dense state space.

## Verification

```bash
python3 scripts/holes_as_unrecorded_sites_unsoldered_order_blind_rules_constant_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=10 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/holes_as_unrecorded_sites_unsoldered_order_blind_rules_constant_2026_09_22.txt`.
