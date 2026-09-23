---
claim_id: order_blind_formation_with_zeros_and_holes_never_failing_unsoldered_rules_are_constant_and_hole_rules_have_pair_form_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading, unsoldered reading, every alphabet. A nearest-neighbour rule that never fails (zeros allowed) and is order-blind is constant on every neighbour condition that occurs, by a variance identity on the 3-site bent path. A sub-probability rule that is strictly order-blind (every order gives the same finished sub-law, holes included) has the exact pair form r(a|N) = r0(a) prod K(a,b) with symmetric K, and conversely; its finished sub-law is the nearest-neighbour pair weight on the window, so its completion mass and completed-record law are order-independent, and a varying one must have holes. Exact exhibits on the bent path, 4-site star, 7-site cross (all 5040 orders) and 8-site path: copy-when-unanimous is order-sensitive; binary rejection exclusion is strictly order-blind with completion 1/64 on the cross and staggered completed records; forcing exclusion has order-dependent completion 1 to 1/32; the soft pair rule (3/4)(1 + ab/3) is strictly order-blind and its completed-record law is exactly the static pair measure 2^(agreeing bonds), with correlations 3^-d. No rule, reading, order law or hole semantics is selected."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - formation_order_covariance_and_isotropic_binary_order_blind_classification_bounded_theorem_note_2026-09-13
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/order_blind_formation_zeros_and_holes_unsoldered_pair_form_2026_09_22.py
---

# Order-blind formation with zeros and holes: never-failing unsoldered rules are constant, and hole rules have pair form

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The previous block of this continuation
(open PR 8663) proved that under the unsoldered reading a strictly
positive order-blind nearest-neighbour rule is constant. It left open
rules with zero conditionals and rules that can fail. This block covers
both, for every alphabet.

## Result up front

1. **Zeros do not help: a never-failing unsoldered order-blind rule is
   constant on every condition that occurs.** Exchange on two adjacent
   sites makes the adjacent-pair law J(a, b) = r0(a) rho(b | a)
   symmetric. Order-blindness on the 3-site bent path, with both leaves
   holding one value b, gives E_r0[rho(b | .)^2] = r0(b)^2 =
   E_r0[rho(b | .)]^2. The variance vanishes, rho(b | a) = r0(b), and the
   star window extends constancy to every condition that occurs. No
   positivity enters. Admissibility requires variation with the
   nearest-neighbor conditions, so every never-failing admissible rule
   under the unsoldered reading is order-sensitive. Exhibit: the rule
   that copies unanimous formed neighbours has zeros, never fails and
   varies; its variance gap is exactly 1/4, and the two leaves of the
   bent path differ with probability 1/2 leaves-first and never
   centre-first.

2. **Rules that can fail: strict order-blindness has an exact pair
   form.** If every formation order gives the same finished sub-law
   (holes included), then r(a | N) = r0(a) prod K(a, b) over the formed
   neighbours, with K(a, b) = K(b, a) and E_r0[prod K] <= 1 on every
   neighbour condition. Conversely every such rule is strictly
   order-blind on every window, with finished sub-law
   prod r0(a_x) prod over bonds K(a_x, a_y). By item 1 a varying one must
   have holes. Its completion mass and its completed-record law are both
   independent of the formation order, so the clock cannot be read
   from records of any kind.

3. **Forcing and rejection separate on the clock.** On the 7-site cross
   the binary rejection rule (draw a fair coin, fail if a formed
   neighbour holds the same value) gives one sub-law for all 5040 orders:
   two staggered configurations, 1/128 each, completion 1/64. The forcing
   rule (take the opposite of unanimous formed neighbours, fail if they
   disagree) has the same completed law but order-dependent completion:
   6 distinct masses, from 1 (centre first) to 1/32 (all leaves first).
   The hole mass that read the clock in the clock-and-rate block belongs
   to forcing rules; rejection rules' hole mass is clock-blind.

4. **The static pair law returns as a completed-record law.** The soft
   pair rule K(a, b) = (3/4)(1 + ab/3) is a sub-probability rule on every
   neighbour condition (worst case 65/128), strictly order-blind on the
   cross (all 5040 orders), and it varies. On the 8-site path its
   completion mass is (3/4)^7 = 2187/16384 for every order. Conditional
   on completion, its record law is exactly the static nearest-neighbour
   pair measure 2^(agreeing bonds), with correlations 3^-d at every
   distance. So the static reading's pair laws are the completed-record
   laws of strictly order-blind formation with holes. The two readings
   of the sentence agree on what completed records say, and differ by a
   hole mass. Binary rejection gives exact staggered order at every
   distance (completion 1/128 on the path). Six-axis rejection gives
   agreement 1/5 at distance 2 and 4/25 at distance 3 (completion
   (5/6)^3).

5. **The unsoldered admissible formation laws split exactly in two.**
   Those that never fail are order-sensitive: the formation order
   enters finished records. Those that are order-blind carry holes, have
   pair form, and have an order-independent hole mass; their completed
   records carry any nearest-neighbour pair law allowed by
   sub-normalisation, including long-range geometric decay and
   staggered order. The price of order-blind reach is a hole mass that
   grows with the window: (3/4)^|bonds| on trees for the soft rule.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the previous block left open unsoldered order-blind rules with zero conditionals and rules that can fail; classify both on every alphabet and state what their completed records carry"
source_of_blocker_text: open_pr_8663_next_trace_action
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the exact split (never-failing implies order-sensitive; order-blind implies pair-form holes with clock-blind hole mass) into the re-assembly; specify what a hole does downstream; test value clocks on forcing rules, where the order is visible"
conditional_surface_status: "formation reading; unsoldered reading; sub-probability rules with holes dropped from the finished law (conditioning on completion, as in the support-rule and clock-and-rate blocks); no hole semantics beyond that is selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorems 1 and 2 are short proofs on the bent path and star windows, valid for every alphabet; every exhibit is an exact rational computation over complete order sets or declared order samples"
```

## Premises and declared objects

Formation reading of the Admissibility sentence, as in the previous
block: a nearest-neighbour rule r(. | N) applied sequentially along a
formation order, N the formed neighbours and their values. Here the
rule may be a sub-probability: the masses at a condition sum to at most
1, and the deficit is the probability that the forming site has no
admissible possibility (a hole). The finished sub-law of an order keeps
the completed histories, as in the support-rule and clock-and-rate
blocks. A rule never fails when every sum is 1. It is strictly
order-blind on a window when every order gives the same finished
sub-law, total mass included. Unsoldered reading: the rule is unchanged
when the formed neighbours' positions are rotated about the site with
their values fixed. The rotations act transitively on the six
directions, so a site with a single formed neighbour has a conditional
that does not depend on that neighbour's direction; the rule may still
see the relative geometry of several formed neighbours. The proofs use
only the single-neighbour property and bent-path and star comparisons
at a fixed geometry. The example rules are direction-blind (they see the
multiset of formed values). On Z^3 two neighbours of a site are never adjacent, so the
bent path (a site with two neighbours) and the star (a site with k
neighbours) are windows whose leaves can form first with no formed
neighbour. Example rules are supplied; no axiom sentence is re-derived.

## Prior art and what is new

- Open PR 8663 (previous block): order-blind never-failing rules have no
  correlation beyond nearest neighbours; strictly positive order-blind
  rules have product form; under the unsoldered reading they are
  constant. New here: constancy without positivity (zeros allowed),
  and the exact pair form of strictly order-blind rules that can fail.
- Landed binary classification note (2026-09-13): interior isotropic
  binary rules. New here: every alphabet, non-interior rules, and rules
  with holes.
- Landed support-rule note and open clock-and-rate PR 8641: hole masses
  of a forcing rule on the parity plane read the formation order. New
  here: rejection rules with the same support have clock-blind hole
  masses, so which kind of hole a rule has decides whether the clock
  is visible.
- Open record-dynamics PR 8646 (corrected): the static pair measure is an
  admissible static law whose chain rule reads non-neighbours. New here:
  the same measure is the completed-record law of a strictly order-blind
  nearest-neighbour formation rule with holes.

## Exact target and obligation graph

Target: the unsoldered order-blind rules that the previous block left
open (zeros, holes), on every alphabet. Obligations: (i) never-failing
rules with zeros (Theorem 1); (ii) strictly order-blind rules with holes
(Theorem 2); (iii) exhibits separating rejection from forcing and
showing what completed records carry (Theorem 3); (iv) the consequence
for the clock decision and the readings, without adoption.

## Theorem 1 — Never-failing unsoldered order-blind rules are constant where they act

Let a nearest-neighbour rule never fail and be order-blind on the 7-site
cross, under the unsoldered reading. Write r0 = r(. | empty) and
rho(b | a) for the conditional at a site whose only formed neighbour
holds a (the same for every direction). Two adjacent sites: the two
orders give J(a, b) = r0(a) rho(b | a) = r0(b) rho(a | b). Bent path with
leaves y1, y2 and centre x: leaves first gives
r0(b1) r0(b2) r(a | {b1, b2}); centre first gives
r0(a) rho(b1 | a) rho(b2 | a). Put b1 = b2 = b and sum over a: the left
side is r0(b)^2 because the rule never fails, the right side is
E_r0[rho(b | .)^2]; and E_r0[rho(b | .)] = sum_a J(a, b) = r0(b). So
Var_r0(rho(b | .)) = 0 and rho(b | a) = r0(b) for every a in the support
of r0. The star with k leaves, leaves first against centre first, then
gives r(a | N) = r0(a) for every condition N whose values all have
positive r0-mass, which are exactly the conditions that occur. So the
rule is constant wherever it acts; any variation sits on conditions that
never occur, and no finished record shows it.

## Theorem 2 — Strict order-blindness with holes is pair form

Let a sub-probability nearest-neighbour rule be strictly order-blind on
the 7-site cross, under the unsoldered reading. The two-site and star
comparisons above hold verbatim for sub-laws, so
r(a | N) = r0(a) prod_i K(a, b_i) on every condition that occurs, with
K(a, b) = rho(b | a) / r0(b) = K(b, a), and each such mass vector sums to
at most 1. Conversely, if r has this form with symmetric K and
E_r0[prod_i K(., b_i)] <= 1 for every neighbour condition, then in any
window and any order each bond contributes K exactly once, at its later
endpoint, so every order gives the finished sub-law
prod_x r0(a_x) prod_bonds K(a_x, a_y). A varying such rule must fail
somewhere, by Theorem 1. Its completion mass and its completed-record
law (the normalised pair weight) do not depend on the order.

## Theorem 3 — Exhibits: rejection, forcing, and the static pair law

On the 7-site cross, all 5040 orders: binary rejection exclusion
(K = 1[a != b]) gives one sub-law, two staggered configurations of 1/128
each (completion 1/64); forcing exclusion gives the same two completed
configurations with equal mass but completion 1, 1/2, ..., 1/32
depending on how many leaves form before the centre (6 distinct
values); the soft pair rule K = (3/4)(1 + ab/3) gives one sub-law with
completion (3/4)^6. The forcing rule is not of pair form: its
one-neighbour K = 2 1[a != b] would give mass 2 to two equal
neighbours. On the 8-site path (four declared orders), the soft rule's
completion is (3/4)^7 and its completed law equals the static pair
measure 2^(agreeing bonds) atom by atom, with c(0, d) = 3^-d for
d = 1, ..., 7; binary rejection has completion 1/128 and completed
records the two staggered patterns (end-to-end correlation -1). Six-axis
rejection (proper colourings) is strictly order-blind on the bent path
(6 orders) and the 4-site star (24 orders), with completion (5/6)^3 and
distance-2 agreement 1/5; on a 4-site path the agreement is
(1/6)(1 + 5(-1/5)^d): 1/5 at d = 2 and 4/25 at d = 3.

## Consequences for the recorded decisions

- **Clock.** Under the unsoldered reading every never-failing admissible
  rule is order-sensitive, now without positivity. The candidate
  "order-blind physical rule" survives only as a pair-form rule with
  holes, whose hole mass and completed law are clock-blind. Forcing rules
  with holes keep a clock-sensitive hole mass.
- **Readings.** The static reading's nearest-neighbour pair laws are the
  completed-record laws of strictly order-blind formation with holes.
  The readings then differ only by a hole mass. The previous block's
  reading decision point is sharpened to exactly that.
- **Reach.** Completed records of order-blind unsoldered rules can carry
  long-range correlation (geometric decay, staggered order), always
  paid for by a hole mass that grows with the window.

## No-Go Discipline Gate

The negative content is scoped: under the unsoldered reading, no
never-failing nearest-neighbour rule that varies on conditions that occur
is order-blind; no strictly order-blind rule escapes pair form.

- **N1 alternative routes.** The soldered reading (the previous block),
  rules that are order-blind only conditional on completion (forcing
  rules), and hole semantics in which formation continues around a hole
  are outside these theorems.
- **N2 wall independence.** Exchange on the two-site, bent-path and star
  windows; no dynamics, clock or spectral input.
- **N3 hidden walls.** Holes are dropped from the finished law, the
  convention of the support-rule and clock-and-rate blocks; the soft
  rule's order check on the 8-site path uses four declared orders, while
  its strict order-blindness is proved by Theorem 2's converse and
  checked on all 5040 orders of the cross.
- **N4 residual matching.** The residual on the clock decision is now:
  order law (never-failing rules), or pair-form holes (order-blind
  rules), or forcing holes (clock in the hole mass), matching the
  recorded candidates with the order-blind one sharpened.
- **N5 rhetoric audit.** "Constant", "pair form" and "clock-blind" are
  exact statements under stated hypotheses; no closure language.
- **N6 partial-closure paths.** Hole semantics downstream of a hole and
  the soldered reading with holes are open continuations.
- **N7 steelman.** Against item 5: dropping failed histories may
  misdescribe a hole. If a hole left its site unrecorded while
  formation continued, the finished law would include unrecorded sites,
  and the pair form would describe only the recorded part. The theorems
  are stated under the drop convention, and the alternative is named.
- **N8 cross-cycle echo.** The binary interior classification and the
  previous block's strictly positive case are special cases, cited.

## Falsifiers

- A never-failing unsoldered order-blind rule whose one-neighbour
  conditional differs from r0 at a value of positive r0-mass falsifies
  Theorem 1.
- A strictly order-blind unsoldered sub-probability rule not of the
  stated pair form, or a symmetric sub-normalised pair rule with two
  orders giving different sub-laws, falsifies Theorem 2.
- Any listed exact value (completions 1/64, 1/32, (3/4)^6, (3/4)^7,
  1/128, (5/6)^3; agreements 1/5, 4/25; correlations 3^-d) failing its
  recomputation falsifies Theorem 3.

## Boundaries and non-claims

No rule, reading, order law or hole semantics is selected. The theorems
use the unsoldered reading; the soldered never-failing case is the
previous block's. Holes are dropped from the finished law; a semantics
in which a hole is an unrecorded site with formation continuing is not
analysed. Completion masses decay with the window, so order-blind reach
through holes is paid for by growing hole mass. No physical
identification is made. Nothing here grades, unlocks or audits any other
claim.

## Imports

Supplied windows, alphabets and example rules; the landed exchange
characterization; standard finite probability. No audit grade, no new
axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) strict order-blindness checked by direct
  sub-law computation over all 5040 orders of the cross for three rules,
  not inferred from the pair form; (ii) the pair form checked on all 127
  value lists against the closed forms of K; (iii) the soft rule's
  completed law compared atom by atom with the static pair measure built
  independently from its weights 2^(agreeing bonds); (iv) the six-axis
  agreements compared with the closed form (1/6)(1 + 5(-1/5)^d) of the
  uniform proper-colouring chain; (v) the variance gap of the copy rule
  compared with its direct order-sensitivity on the bent path.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| copy rule copies the opposite | unanimous value negated | caught (1 FAIL) |
| sub-law keeps the order's own indexing | configurations not re-indexed by site | caught (5 FAILs) |
| rejection allows equal values | exclusion removed | caught (5 FAILs) |
| forcing takes the same value | opposite to same | caught (1 FAIL) |
| soft weight asymmetric in a | K(a, b) to (1 + (ab + a)/3) | caught (4 FAILs) |
| soft lambda 3/4 to 1 | sub-normalisation lost | caught (2 FAILs) |
| neighbour lookup ignores formed sites | condition emptied | caught (8 FAILs) |
| pair measure base 2 to 3 | comparison measure changed | caught (1 FAIL) |
| correlation drops the mean product | means not subtracted | missed; masked non-defect (every mean is 0 by flip symmetry, now pinned by an explicit check) |

  Eight of eight defect mutants are caught; the ninth is a masked
  non-defect.
- **Vacuity guard:** every equality compares independently computed
  laws, closed forms or stated exact rationals; the forcing and rejection
  rules share a support, so their difference isolates the rule type.
- **Budget:** 14 checks, stdout 2477 characters (ceiling 6000),
  about 10 s (ceiling 900 s), exact Fractions; largest computation the
  5040-order sweeps of the cross; no dense state space.

## Verification

```bash
python3 scripts/order_blind_formation_zeros_and_holes_unsoldered_pair_form_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=14 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/order_blind_formation_zeros_and_holes_unsoldered_pair_form_2026_09_22.txt`.
