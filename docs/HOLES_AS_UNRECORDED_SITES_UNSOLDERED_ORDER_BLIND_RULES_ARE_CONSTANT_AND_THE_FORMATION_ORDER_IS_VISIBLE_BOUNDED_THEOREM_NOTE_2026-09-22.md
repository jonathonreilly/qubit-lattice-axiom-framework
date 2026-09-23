---
claim_id: holes_as_unrecorded_sites_unsoldered_order_blind_rules_are_constant_and_the_formation_order_is_visible_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading with the supplied one-attempt unrecorded-site convention: a site whose neighbour condition lies outside the rule's domain carries no record, cannot be read, and formation continues; a finished state is a configuration of records. Under the unsoldered reading, on every finite alphabet, an order-blind nearest-neighbour rule normalised on its domain has every occurring condition in its domain and is constant there; in the sub-probability model with deficits as unrecorded sites, order-blindness forces a constant hole rate and constant values. Hence every unsoldered rule varying on occurring conditions makes the formation order visible in finished states. Exact exhibits on two sites, the bent path, the 4-site star and the 7-site cross, including the contrast with the drop convention. No rule, reading or order law is selected."

upstream_dependencies:
  - minimal_axioms
runner: scripts/holes_as_unrecorded_sites_unsoldered_order_blind_rules_constant_2026_09_22.py
---

# Holes as unrecorded sites: unsoldered order-blind rules are constant, and the formation order is visible

**Date:** 2026-09-22
**Type:** bounded_theorem
The results below concern explicitly supplied finite formation models.
Their parameters, alphabets, orders and sampling laws are conditions of the
calculation, not additional framework premises.

## Result up front

1. **The calculation supplies an unrecorded-site convention.** A site with
   no allowed value is left unrecorded after one attempt and formation
   continues. Record's unreadability clause is consistent with this model,
   but does not determine retry, stopping, or history-conditioning rules.
   Those alternatives remain open.

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

3. **Observable variation implies order sensitivity in the stated model.**
   The finite constancy theorem concerns occurring conditions. Variation on
   unreachable conditions need not change a finished law. Thus no universal
   exclusion follows from the framework's variation sentence alone.

4. **Hole locations carry the order.** For deficit rejection on a pair,
   the unrecorded site is always the later-formed one (probability 1/2),
   while under the drop convention the two orders agree. On the 7-site
   cross with the centre formed k-th (k = 1..7), the deficit rejection and
   soft pair rules of the previous block give 7 distinct finished-state
   laws, against 1 under the drop convention. Binary exclusion normalised
   on its domain gives 6. Constant erasure (hole rate 1/3, fair values) is
   order-blind on all 24 orders of the 4-site star, and it does not vary.

5. **No universal formation exclusion follows.** The finite constancy
   result concerns occurring conditions. An initial support on which a law is
   constant can coexist with variation outside that support. No physical
   order law or hole convention is selected here.

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
conditional_surface_status: "formation reading; a supplied convention for a site with no allowed possibility; one formation attempt per site; no rule, reading or order law selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the theorems are short proofs on the two-site and star windows valid for every finite alphabet; every exhibit is an exact rational computation over declared orders"
```

## Premises and declared objects

The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the
sampling process studied here. Sequential draws use the declared conditional
law given the previously formed configuration, with fresh randomness at each
step; a chosen order is external to those draws. Correlated joint draws and
adaptive orders are separate models. Skipping a failed attempt and continuing,
or dropping its whole history, are supplied alternatives. Neither convention
follows from unreadability alone.


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

## Theorem 1 — Finite domain rules: constancy on occurring conditions

Let an unsoldered nearest-neighbour rule, normalised on its domain D, be
order-blind on the 7-site cross, with holes read as unrecorded sites.
The empty condition lies in D, or no site ever records. On two adjacent
sites x, y: with x first, P(x = a, y unrecorded) = r0(a) 1[{a} not in D];
with y first, y records at the empty condition, so this probability is 0.
Hence {a} lies in D for every a with r0(a) > 0. On the star, leaves first
gives P(leaves b_i, centre unrecorded) = prod r0(b_i) 1[N not in D];
centre first gives 0. So every occurring condition lies in D. The rule
never fails where it acts, and constancy follows from the finite variance argument:
write rho(b|a) for the one-neighbour conditional. Pair order equality gives
r0(a)rho(b|a)=r0(b)rho(a|b). Comparing centre-first and leaves-first on
a two-leaf star gives E_r0[rho(b|.)^2]=r0(b)^2 and E_r0[rho(b|.)]=r0(b),
so the variance is zero. The full star comparison then gives r(a|N)=r0(a)
on positive-probability conditions.

## Theorem 2 — Deficit rules: order-blind means constant erasure and constant values

Let an unsoldered sub-probability rule, with deficits read as unrecorded
sites, be order-blind on the 7-site cross. Assume delta0<1, since delta0=1 produces no records and supplies no constraint
on unreachable conditions. With delta(N) the deficit at
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

The negative scope is only the explicitly stated finite-model implication or
independent-clock bound. No general physical formation exclusion is claimed.

**N1 — Five distinct challenges.** Each is ATTEMPTED by the local argument
or the named finite computation, with its outcome kept explicit:

- **Dropped histories (ATTEMPTED):** the pair rejection sub-law is order-blind, showing that the conclusion depends on keeping hole positions.
- **Continued failed attempts (ATTEMPTED):** the pair rejection process with holes retained changes which site is unrecorded.
- **Normalized domain exclusion (ATTEMPTED):** the bent-path control distinguishes centre-first and leaves-first holes.
- **Constant erasure (ATTEMPTED):** the erasure control is order-blind over all star orders and has no variation on its reachable support.
- **Unreachable-condition variation (ATTEMPTED):** a law that always draws 0 when all seen values are 0, but changes on a neighbour value 1, has a constant reachable law; this defeats the original unqualified variation-clause exclusion.

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
the finite variance proof given here. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Author check record (original proposal)

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

## Landing review correction

Serial source review in one Codex session under the owner's no-subagent
instruction narrowed physical interpretations to supplied model conditions.
Original author check reports above are historical; they do not certify these
corrections. Current source-bound executions and independent controls are
recorded in the combined landing evidence. No independent audit is claimed.

## Verification

```bash
python3 scripts/holes_as_unrecorded_sites_unsoldered_order_blind_rules_constant_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=10 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/holes_as_unrecorded_sites_unsoldered_order_blind_rules_constant_2026_09_22.txt`.
