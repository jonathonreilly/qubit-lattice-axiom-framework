---
claim_id: order_blind_formation_with_zeros_and_holes_never_failing_unsoldered_rules_are_constant_and_hole_rules_have_pair_form_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading, unsoldered reading, every finite alphabet. A nearest-neighbour rule that never fails (zeros allowed) and is order-blind is constant on every neighbour condition that occurs, by a variance identity on the 3-site bent path. A finite-alphabet sub-probability rule with positive empty-condition masses that is strictly order-blind on pairs and substars (every order gives the same completed-state sub-law and completion mass) has the exact pair form r(a|N) = r0(a) prod K(a,b) with symmetric K, and conversely; its finished sub-law is the nearest-neighbour pair weight on the window, so its completion mass and completed-record law are order-independent, and variation on occurring conditions requires failure somewhere. Exact exhibits on the bent path, 4-site star, 7-site cross (all 5040 orders) and 8-site path: copy-when-unanimous is order-sensitive; binary rejection exclusion is strictly order-blind with completion 1/64 on the cross and staggered completed records; forcing exclusion has order-dependent completion 1 to 1/32; the soft pair rule (3/4)(1 + ab/3) is strictly order-blind and its completed-record law is exactly the static pair measure 2^(agreeing bonds), with correlations 3^-d. No rule, reading, order law or hole semantics is selected."

upstream_dependencies:
  - minimal_axioms
runner: scripts/order_blind_formation_zeros_and_holes_unsoldered_pair_form_2026_09_22.py
---

# Order-blind formation with zeros and holes: never-failing unsoldered rules are constant on reached conditions, and positive-base hole rules have pair form

**Date:** 2026-09-22
**Type:** bounded_theorem
The results below concern explicitly supplied finite formation models.
Their parameters, alphabets, orders and sampling laws are conditions of the
calculation, not additional framework premises.

## Result up front

1. **Zeros do not help: a never-failing unsoldered order-blind rule is
   constant on every condition that occurs.** Exchange on two adjacent
   sites makes the adjacent-pair law J(a, b) = r0(a) rho(b | a)
   symmetric. Order-blindness on the 3-site bent path, with both leaves
   holding one value b, gives E_r0[rho(b | .)^2] = r0(b)^2 =
   E_r0[rho(b | .)]^2. The variance vanishes, rho(b | a) = r0(b), and the
   star window extends constancy to every condition that occurs. No
   positivity enters. Admissibility requires variation with the
   nearest-neighbor conditions, so every never-failing rule varying on occurring conditions
   under the unsoldered reading is order-sensitive. Exhibit: the rule
   that copies unanimous formed neighbours has zeros, never fails and
   varies; its variance gap is exactly 1/4, and the two leaves of the
   bent path differ with probability 1/2 leaves-first and never
   centre-first.

2. **Positive-base finite rules that can fail have pair form under strict
   order-blindness on pairs and substars.** If every formation order gives the same finished sub-law
   (completion mass included; failed histories omitted), then r(a | N) = r0(a) prod K(a, b) over the formed
   neighbours, with K(a, b) = K(b, a) and E_r0[prod K] <= 1 on every
   neighbour condition. Conversely every such rule is strictly
   order-blind on every window, with finished sub-law
   prod r0(a_x) prod over bonds K(a_x, a_y). By item 1, variation on occurring conditions requires failure
   somewhere in this model. Its completion mass and its completed-record law are both
   independent of the formation order, so the completed-state sub-law and its total mass do not distinguish
   the order; partial failed histories are not compared.

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
   neighbour condition (mass 65/128 on six equal neighbours; maximum 1 at the empty condition), strictly order-blind on the
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

5. **The unsoldered classified rule families separate as follows.**
   Those that never fail are order-sensitive: the formation order
   enters finished records. Those with positive base masses that are strictly order-blind on
   pairs and substars and vary on reached conditions carry holes, have pair form, and have an order-independent hole mass; their completed
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
target_blocker_text: "determine the stated conditional finite-model results without selecting a physical formation law"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "test extensions outside the declared finite models; a physical downstream consumer is not yet established"
conditional_surface_status: "formation reading; unsoldered reading; sub-probability rules with holes dropped from the finished law (conditioning on completion, as in the support-rule and clock-and-rate blocks); no hole semantics beyond that is selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorems 1 and 2 are short proofs on the bent path and star windows, valid for every finite alphabet; every exhibit is an exact rational computation over complete order sets or declared order samples"
```

## Premises and declared objects

The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the
sampling process studied here. Sequential draws use the declared conditional
law given the previously formed configuration, with fresh randomness at each
step; a chosen order is external to those draws. Correlated joint draws and
adaptive orders are separate models. Skipping a failed attempt and continuing,
or dropping its whole history, are supplied alternatives. Neither convention
follows from unreadability alone.


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


Scope of the constancy statements: finite alphabets, conditions with positive
probability under the supplied initial law, and order-blindness on all relevant
pair, bent-path and star windows. Constancy on reached conditions does not
exclude a rule that varies only on unreachable conditions. The point-mass
proof is not a pointwise theorem for an atomless alphabet; the explicit Haar
construction, where present, is checked separately. No variation clause is
silently strengthened to require observable variation on this initial support.

## Relation to earlier work

This packet states its supplied models and finite calculations directly.
Earlier campaign comparisons are historical motivation, not imported proof,
physical authority, or an adopted formation law.

## Exact target and obligation graph

Target: the unsoldered order-blind rules that the previous block left
open (zeros, holes), on every finite alphabet. Obligations: (i) never-failing
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

Let a finite-alphabet sub-probability nearest-neighbour rule have r0(a)>0
for every retained alphabet symbol and be strictly order-blind on the pair
and every substar of the 7-site cross, under the unsoldered reading. The two-site and star
comparisons above hold verbatim for sub-laws, so
r(a | N) = r0(a) prod_i K(a, b_i) on every condition that occurs, with
K(a, b) = rho(b | a) / r0(b) = K(b, a), and each such mass vector sums to
at most 1. Conversely, if r has this form with symmetric K and
E_r0[prod_i K(., b_i)] <= 1 for every neighbour condition, then in any
window and any order each bond contributes K exactly once, at its later
endpoint, so every order gives the finished sub-law
prod_x r0(a_x) prod_bonds K(a_x, a_y). A rule varying on occurring conditions must fail
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

## Consequences and limits

The finite constructions distinguish the stated sampling laws and orders.
They do not choose a physical formation law, exclude alternatives outside the
stated support, or settle gravity, clock, locality or alphabet decisions.

## No-Go Discipline Gate

The negative scope is only the explicitly stated finite-model implication or
independent-clock bound. No general physical formation exclusion is claimed.

**N1 — Five distinct challenges.** Each is ATTEMPTED by the local argument
or the named finite computation, with its outcome kept explicit:

- **Zeros without failure (ATTEMPTED):** the copy-unanimous example is order-sensitive; the finite variance proof covers zero entries on reachable support.
- **History rejection (ATTEMPTED):** binary rejection has symmetric pair form and completion 1/64 on the cross, an explicit escape from never-failing hypotheses.
- **Forced compatible value (ATTEMPTED):** binary forcing has order-dependent completion and is not the same sub-law as rejection.
- **Soft pair weights (ATTEMPTED):** exact sub-normalized weights reproduce the finite static pair law after completion conditioning.
- **Larger finite alphabets (ATTEMPTED):** the six-colour rejection chain has the stated distance-two and distance-three agreements; binary-only conclusions are not imposed on it.

**N2 — Conditions.** The stated alphabet, sampling law and domain jointly
specify this model; no theorem counting independent physical walls is asserted.
Changing one condition does not automatically supply the other conditions.
Relations between alternative physical choices remain unclassified.

**N3 — Hidden-condition scan.** Fresh sequential randomness, finite supported
alphabets where used, declared orders, and the particular failure convention
are supplied conditions. No framework grant for them is claimed. Physical
encodings of abstract role labels remain separate from the finite calculations.

**N4 — Residual matching.** All negative implications used here are proved in
this note on the named domain. Historical comparisons are not invoked as
negative witnesses; no external residual is declared closed by analogy.

**N5 — Resolution.** The runner checks the finite elements/sites/windows
listed in its output. Universal implications are the source proofs; infinite
lattice formation, spectral modes and untested block correlations are not
executed or inferred from a finite sample.

**N6 — Partial routes.** Other alphabets, joint or correlated draws, adaptive
orders, retry conventions and other failure handling are not ruled out. No
new axiom is declared necessary. Scale and kinetic-form primitives have no
role in this finite calculation; they are not classified as missing inputs.

**N7 — Steelman.** A different process can evade a product-law bound by shared
randomness, evade an order comparison by conditioning on completion, or evade
a finite-support constancy statement by varying only off the reached support.
These are concrete reasons not to promote this packet to a physical no-go.
The result is restricted to the model whose hypotheses the proof actually uses.

**N8 — Cross-packet check.** The related formation packets distinguish dropped
histories, holes retained as absent sites, directional alphabets and joint
units. Those distinctions are preserved here. Neither a historical campaign
label nor a previous bounded conclusion grants a general exclusion.

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

## Author check record (original proposal)

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

## Landing review correction

Serial source review in one Codex session under the owner's no-subagent
instruction narrowed physical interpretations to supplied model conditions.
Original author check reports above are historical; they do not certify these
corrections. Current source-bound executions and independent controls are
recorded in the combined landing evidence. No independent audit is claimed.

## Verification

```bash
python3 scripts/order_blind_formation_zeros_and_holes_unsoldered_pair_form_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=14 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/order_blind_formation_zeros_and_holes_unsoldered_pair_form_2026_09_22.txt`.
