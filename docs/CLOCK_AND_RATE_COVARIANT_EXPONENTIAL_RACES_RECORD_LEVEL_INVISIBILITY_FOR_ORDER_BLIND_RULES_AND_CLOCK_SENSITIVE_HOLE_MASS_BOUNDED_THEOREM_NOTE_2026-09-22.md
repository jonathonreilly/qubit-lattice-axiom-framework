---
claim_id: clock_and_rate_covariant_exponential_races_record_level_invisibility_for_order_blind_rules_and_clock_sensitive_hole_mass_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Exact finite comparison of four covariant exponential-clock rate laws (uniform, neighbour count 1+k, (1+k)^2, 1/(1+k)) and one value law on the 2x3 window and the 3x3 parity-role plane: induced race order laws and their covariance; record-level invisibility of every listed clock for the chain rule of a positive pair measure; record-level separation of the clocks by the nearest-neighbour rule with exact statistics; the plane hard-support completion mass E[2^-d] under each clock, by two independent dynamic programmes and a direct 9! enumeration, with the completion-conditioned record law uniform on the Gauss set for value-blind clocks. No axiom selection, no physical time, no rate clause adopted; no partial-hole location law."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/clock_and_rate_covariant_race_order_laws_record_visibility_and_hole_mass_2026_09_22.py
---

# Clock and rate: covariant races, record-level invisibility, and the clock-sensitive hole mass

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign block:** clock-and-rate, wave C of the TOE derivation campaign by
underdetermination witnesses (design note 2026-09-13). The block supplies
concrete covariant rate laws for independent exponential clocks, binds the
induced order laws and the finished-record laws separately, and exhibits
where records can and cannot see the clock.

## Result up front

1. **Clocks always reshape the order law and need not reach the records.**
   Under the uniform rate every one of the 720 orders of the 2x3 window has
   mass 1/720; the neighbour-count law 1 + k moves order masses across
   [1/3360, 1/252] while staying normalised and covariant under the window
   rotation. The design note's warning is realised exactly: different order
   laws need not yield different record statistics.

2. **Invisibility theorem for order-blind rules.** For the chain rule of the
   positive pair measure mu proportional to 2^(agreeing edges) — a rule that
   conditions on every formed site and is order-blind — the finished-record
   law equals mu exactly under the count, squared-count, inverse-count and
   value clocks, on all 64 atoms. The mechanism is that the race factors
   telescope: for every fixed full value pattern the race masses sum to one,
   so clocks spend no probability on values. A covariant clock leaves no
   record trace when the conditional rule is order-blind and the support has
   no holes.

3. **Visibility for order-sensitive rules.** The local nearest-neighbour
   rule (r(a) proportional to 2^(formed neighbours with value a)) fails the
   exchange identity of the formation-order block, and the three clocks
   produce three different finished laws: the edge-agreement expectation is
   16780559/3645000 (uniform), 4956001733/1071630000 (count),
   126083753/27337500 (value), against 2696/561 for the static measure —
   four distinct exact rationals, with positive total-variation separations.
   On these windows the exhibited order-blind rule conditions on every
   formed site while the local rule is clock-sensitive: the locality against
   order-blindness tension is recorded, consistent with the sister
   formation-order finding that order-blind binary nearest-neighbour rules
   are constant.

4. **The hole mass reads the clock even though the rule is order-blind.**
   On the parity-role plane of the support-rule note (V = 4, L = 4, P = 1),
   the hard-support rule's completion mass E[2^-d] is 5/8 under the uniform
   clock (matching that note, recomputed by an independent subset dynamic
   programme and by direct enumeration of all 9! orders), and
   145882686915239/206615469060000 (about 0.706) under the count clock,
   99873182931058298117591/125349298909891262306100 (about 0.797) under the
   squared-count clock, 304695555559113623750221/524938138301974597200000
   (about 0.580) under the inverse-count clock. All four are distinct, and
   they order with clock eagerness: cluster-eager clocks complete checks
   before links can close them (E[d] falls from 4/5), frontier-averse clocks
   do the opposite. Conditional on completion, the record law is uniform on
   the Gauss set for every value-blind clock (per-order uniformity exhibited
   over all 512 coins on explicit d = 0, 1, 2 orders; a mixture of identical
   uniforms is uniform).

5. **Decision points recorded, nothing adopted.** (a) a uniform-clock
   clause; (b) an eagerness (neighbour-count) clause; (c) a value-clock
   clause; (d) order-blindness of the physical rule, which erases the clock
   from records except through hole masses; (e) time as record count, under
   which no rate law exists and the order is registered data as in the
   formation-order block. The realized-state primitive supplies no
   comparison measure, and none is imported.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "supply and compare concrete covariant rate laws on specified finite windows; bind the induced order laws and finished-record laws separately; different rate or order laws need not yield different record statistics even when some orders do; exhibit the proposed difference rather than infer it"
source_of_blocker_text: design_note_2026-09-13
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "feed the clock-sensitive hole mass and the eagerness ordering to the formation-unit block and the record-dynamics reframing; test value clocks on constrained windows where the race couples to the coins; carry the completion-conditioned uniformity to assembly"
conditional_surface_status: "all rate laws, rules, measures and windows are supplied finite model content; no rate clause, time metric or order measure is selected; the five clause candidates are recorded as decision points, not adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every statement is an exact finite computation (rational race products, subset and partial-assignment dynamic programmes, complete enumerations over 720 and 9! orders and 512 coin vectors) on declared windows, rules and rate laws; nothing is asserted beyond them"
```

## Premises and declared objects

Windows: the 2x3 rectangle (6 sites, 7 edges) and the 3x3 plane with the
parity roles of the landed support-rule note (roles by coordinate parity,
V = 4, L = 4, P = 1; checks[v] = v plus its in-window L neighbours; each L
in exactly two checks; the Gauss set has 32 = 2^(9-4) patterns). Clocks:
independent exponential clocks, one per unformed site, with a covariant
rate law; by memorylessness the induced order law is the sequential race
P(next = s) = lambda(s)/sum over unformed sites, restarted after every
formation. Rate laws: uniform 1; neighbour-count laws 1 + k, (1 + k)^2,
1/(1 + k) with k the number of formed in-window nearest neighbours; the
value law 1 + (agreeing pairs among formed neighbour values), covariant
under window rotations and the internal flip. Conditional rules on the
binary alphabet: the chain rule of mu proportional to 2^(agreeing edges),
conditioning on every formed site; the nearest-neighbour rule with
r(a) proportional to 2^(formed neighbours with value a). The plane
hard-support rule of the support-rule note: L and P free, a V site forms
only after its in-window L neighbours with the parity they force;
d(order) counts the L sites that form last within the union of their two
checks, and P(fully recorded | order) = 2^(-d). All of these are supplied
model content; no axiom sentence is re-derived.

## Prior art and what is new

- Landed formation-order note (2026-09-13, wave A): order laws compared as
  supplied measures, the exchange identity characterising order-blind
  rules, and the sister classification that order-blind binary
  nearest-neighbour rules are constant. New here: clocks that induce the
  order law, and the exact split between order-law visibility and
  record-law visibility.
- Landed support-rule note (2026-09-14, wave A): the plane roles, the
  hard-support rule, d, the uniform-order d-histogram (108864, 217728,
  36288) and E[2^-d] = 5/8. New here: the completion mass as a function of
  the clock, by two independent dynamic programmes agreeing with each
  other and, at the uniform point, with that note and with a from-scratch
  9! enumeration; the eagerness ordering; the completion-conditioned
  uniformity under every value-blind clock.
- Landed possibility-covariance note (2026-09-14, wave B): the covariance
  context for rate laws on the value side; the value clock here is
  flip-covariant in that sense.
- Open physics-loop blocks ail53 (PR 8568, branch
  `physics-loop/admissibility-induced-law-block53-no-master-clock-forces-the-lattice-laplace-equation-20260921`)
  and ail54 (PR 8570): those supply a neighbour-determined, scale-covariant
  tick-rate field and study its averaging equation and phase consequences.
  This block is orthogonal: it supplies no tick field and instead asks
  whether finished records can distinguish rate laws at all. Cited as an
  open lane, read from its branch, not duplicated.
- Landed clock-construction notes (2026-09-13/15, native half-line clock
  completion, growing formation current, finite-clock family): supplied
  clock constructions inside models. This block quantifies over rate laws
  instead of building one.

What is new in one line: the exact three-way split — clocks always move
the order law, never the records of an order-blind rule on a hole-free
window, and always the hole mass of the hard-support rule — with every
number an exact rational and every route recomputed independently.

## Exact target and obligation graph

The design note's brief, quoted: "Supply and compare concrete covariant
rate laws, for example independent exponential clocks with constant or
neighbour-dependent rates, on specified finite windows. Bind the induced
order laws and finished-record laws separately. Different rate or order
laws need not yield different record statistics even when some orders do.
Exhibit the proposed difference rather than infer it. Order-independent
statistics do not settle every physical time or rate target. Any candidate
rate clause remains a possible owner decision after a scoped witness; the
realized-state primitive supplies no comparison measure."

Obligations discharged: concrete covariant rate laws supplied (five);
order laws and record laws bound separately (Theorems 1 against 2, 3, 4);
the proposed differences exhibited, not inferred (exact separations in
Theorems 3 and 4; exact equalities in Theorem 2); clause candidates
recorded as decision points with no adoption.

## Theorem 1 — Induced order laws and their covariance

The race law of the uniform clock is the uniform order law (all 720
orders at 1/720, total mass one). The count clock's order law is
normalised, covariant under the 180-degree window rotation on sampled
orders, and not exchangeable: order masses range over [1/3360, 1/252].
Driven by any fixed full value pattern, the value clock's race masses sum
to one over all 720 orders: the race factors telescope, so clocks spend
no probability on values.

## Theorem 2 — Record-level invisibility for the chain rule

The chain rule of mu is order-blind (the finished law equals mu for three
explicit orders, all 64 atoms, and the exchange identity holds on sampled
pairs). Under the count, squared-count, inverse-count and value clocks the
finished-record law of the race process equals mu exactly. Consequence:
for this rule class no covariant rate law is visible in finished records;
an order-blind conditional rule erases the clock on a hole-free window.

## Theorem 3 — Record-level visibility for the nearest-neighbour rule

The nearest-neighbour rule fails the exchange identity on an exhibited
sampled pair. Its finished laws under the uniform, count and value clocks
are three distinct exact distributions (pairwise total variation
29995127/3429216000, 201911/43740000, 29140541/6429780000), all
normalised and flip-covariant. The edge-agreement expectation separates
the three clocks and the static measure pairwise: 16780559/3645000,
4956001733/1071630000, 126083753/27337500, 2696/561.

## Theorem 4 — The clock-sensitive hole mass

On the plane, the uniform clock reproduces the support-rule note's
d-histogram (3/10, 3/5, 1/10) and completion mass E[2^-d] = 5/8, by a
subset dynamic programme over 512 x 3 states and, independently, by
direct enumeration of all 9! orders (counts 108864, 217728, 36288). The
count, squared-count and inverse-count clocks give completion masses
145882686915239/206615469060000, 99873182931058298117591/125349298909891262306100
and 304695555559113623750221/524938138301974597200000; the histogram
programme and an independent absorbed-coin programme agree on every one.
All four masses are distinct and order with clock eagerness, and E[d]
moves oppositely (4/5 at uniform, lower for eager clocks, higher for the
frontier-averse clock). On explicit orders of d = 0, 1, 2, over all 512
coin vectors, the completion fraction is 2^-d and the completed patterns
are exactly the Gauss set with uniform multiplicity; a rate-weighted
mixture of identical uniform conditional laws is uniform, so the
completion-conditioned record law is clock-blind for every value-blind
clock while the completion mass is clock-sensitive.

## No-Go Discipline Gate

The negative content is scoped: on the exhibited windows, the listed
clocks are invisible in the finished records of the chain-rule class, and
no listed statistic of the completion-conditioned plane law sees the
clock.

- **N1 alternative routes.** Correlated clocks, non-exponential waiting
  laws, clocks reading records beyond nearest neighbours, value clocks on
  constrained windows, and rules between the local and full-conditioning
  extremes are unclassified.
- **N2 wall independence.** Everything is finite combinatorics and exact
  dynamic programming; no Hamiltonian, spectral input or continuum limit
  enters.
- **N3 hidden walls.** All rate laws, rules and measures are supplied; the
  covariance checks are sampled, not complete; the telescoping identity is
  checked by complete 720-order sums at two value patterns.
- **N4 residual matching.** The residual toward a physical time is exactly
  the clause family recorded (uniform, eagerness, value, order-blindness,
  record-count), matching the design note's expectation that a rate clause
  remains an owner decision after a scoped witness.
- **N5 rhetoric audit.** "Invisible" and "reads the clock" name exact
  equalities and inequalities of finished-record quantities; no closure
  language is used; a failed search is not claimed anywhere.
- **N6 partial-closure paths.** The locality against order-blindness
  tension is exhibited, not proved in generality; a local order-blind
  nonconstant rule on some window would reopen the invisibility route at
  full locality. Promotion routes stay open.
- **N7 steelman.** Against the witness: the objection that the hole mass
  is process bookkeeping rather than record content is answered by the
  completion fraction being a statistic of which windows carry full
  records; the objection that the chain rule smuggles order-blindness in
  by nonlocality is conceded and recorded as the tension, consistent with
  the sister classification that local order-blind binary rules are
  constant. For the clocks: the strongest case that clocks are physical is
  precisely the hole channel, and the strongest case that they are not is
  the chain-rule class; both are exhibited.
- **N8 cross-cycle echo.** The d-histogram and 5/8 are the support-rule
  note's results, cited and independently recomputed, not re-derived as
  new; the exchange identity is the formation-order block's, applied.

## Falsifiers

- A listed clock under which the chain-rule finished law differs from mu
  on any atom falsifies Theorem 2.
- Equality of any two of the four plane completion masses, or a
  disagreement between the histogram and absorbed-coin programmes, or a
  uniform-clock histogram differing from (3/10, 3/5, 1/10), falsifies
  Theorem 4.
- An order among the exhibited three whose completed patterns are not
  uniform on the Gauss set falsifies the conditional-uniformity claim.
- Coincidence of the three nearest-neighbour finished laws, or of the
  four edge-agreement expectations, falsifies Theorem 3.
- An exchange-identity violation for the chain rule on the sampled pairs
  falsifies the order-blindness exhibit.

## Boundaries and non-claims

No rate clause, time metric, order measure or comparison measure is
selected, adopted or imported; the realized-state primitive is respected
(alternatives are never averaged inside any model; every mixture shown is
a property of a supplied clock's induced law, labelled as such). The
invisibility theorem is exhibited for the chain rule of one positive pair
measure on one window under four clocks; its generality is argued in
prose (telescoping) and bounded by the checks. Value clocks are tested on
the hole-free window; on constrained windows the race couples to
the coins and is left as a boundary. No partial-record or hole-location
law is constructed (the support-rule note's boundary is respected). The
record-count reading of time is a recorded decision point; its
distributional consequences with holes are not computed here beyond E[d].
Nothing here grades, unlocks or audits any other claim.

## Imports

Supplied rate laws, rules, measures and windows; standard finite
probability and dynamic programming. The cited landed notes carry their
own scopes; the open ail lane is cited as prior art with no status
import. No audit grade, no new axiom, no new primitive, no new comparator
and no new framing is imported.

## Review record

- **Seat:** one Fable 5.1 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) the plane completion mass computed by the
  (subset, d) histogram programme and by the absorbed-coin subset
  programme, agreeing for all four clocks; (ii) the uniform-clock
  histogram recomputed by direct enumeration of all 9! orders, agreeing
  with the dynamic programme and with the support-rule note's counts;
  (iii) the uniform-clock nearest-neighbour law computed by the race
  programme and by the uniform mixture of all 720 fixed-order laws,
  agreeing on all 64 atoms; (iv) the telescoping identity verified by
  complete 720-order race sums at two value patterns; (v) hand values
  1/720, 4/5, 5/8 and the d-count integers against the programmes.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| race not normalised | drop `/ tot` in the race product | caught (3 FAILs) |
| count law loses its floor | `1 + k` to `k` | caught (division by zero, nonzero exit) |
| value law counts disagreeing pairs | `==` to `!=` in the pair test | missed; diagnosed non-defect |
| chain rule degraded to iid | conditional replaced by 1/2 | caught (3 FAILs) |
| NN rule base 2 to 1 | `2^k` to `1^k` | caught (3 FAILs) |
| histogram DP never increments d | closure increment removed | caught (4 FAILs) |
| absorbed DP drops the compatibility coin | `w /= 2` to `w /= 1` | caught (2 FAILs) |
| hole sim parity sign flipped | required parity offset by one | caught (1 FAIL) |
| checks drop the V site itself | `[v] +` removed from checks | caught (6 FAILs) |
| pair measure base 2 to 1 | mu degraded to uniform | missed; diagnosed non-defect |

  Both missed mutants are genuine non-defects: the disagreement-counting
  value law is another covariant value law, and the base-1 measure is the
  uniform pair measure — in each case the theorems quantify over supplied
  examples and remain true, and every check correctly passes. Eight of
  eight defect mutants are caught.
- **Vacuity guard:** every equality compares two independently computed
  routes or a stated exact rational; the covariance checks compare
  transformed against untransformed inputs; the exchange check exhibits
  an equality and an inequality side by side; the separation checks
  assert distinctness of printed exact values, not mere non-identity of
  objects.
- **Budget:** 22 checks, stdout 3815 characters (ceiling 6000), 1.4 s
  elapsed (ceiling 900 s), exact Fractions throughout; largest structures
  the 729 partial assignments of the 2x3 window and the 512 x 3 subset
  states of the plane; no dense space at or above 2^11.

## Verification

```bash
python3 scripts/clock_and_rate_covariant_race_order_laws_record_visibility_and_hole_mass_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=22 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/clock_and_rate_covariant_race_order_laws_record_visibility_and_hole_mass_2026_09_22.txt`.
