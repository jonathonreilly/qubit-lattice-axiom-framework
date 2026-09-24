---
claim_id: record_dynamics_finished_record_correlators_against_propagation_kernels_nearest_neighbour_sentence_excludes_long_range_pairs_and_glued_support_rigidity_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Exact finished-record correlators on the 8-site path and the 3x3 parity-role plane, with no tick, clock, Hamiltonian or evolution law anywhere: the nearest-neighbour pair measure's chain rule has connected correlator exactly 3^-(distance) against the exactly linear Dirichlet Green function of the path Laplacian (no scaling matches beyond one distance); a supplied all-pairs measure is covariant and order-blind with a distance-blind correlator 835/867, and is excluded by the Admissibility nearest-neighbour sentence under both the static reading (its site-0 conditional moves with the far site: 128/129 against 32/33) and the formation reading, while the nearest-neighbour measure is an admissible static law whose chain rule conditions beyond neighbours as a formation rule (5/9 against 4/9); a single supplied long bond moves the far correlator to 1095/3281 while the mid correlator stays under twice its geometric value; the uniform Gauss-set law has every one- and two-point parity exactly 0 and every dual-code parity exactly 1 at full window span. No photon or gravity identification, no dynamics selected, no clause adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
  - a_hierarchy_of_neighbourhood_conditions_glued_breakable_and_free_record_groups_under_shifting_ticks_bounded_theorem_note_2026-09-03
runner: scripts/record_dynamics_correlator_kernels_nearest_neighbour_sentence_and_glued_support_rigidity_2026_09_22.py
---

# Record dynamics: finished-record correlators against propagation kernels

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign block:** record-dynamics reframing, wave D of the TOE derivation
campaign by underdetermination witnesses (design note 2026-09-13). The
hypothesis under investigation — unrecorded sites carry no law-level state —
is a hypothesis, not an adopted reading; the block computes what
finished-record statistics alone can and cannot supply, with no tick
anywhere.

## Result up front

1. **A record correlator with no tick, and it is not a Laplacian kernel.**
   The nearest-neighbour pair measure — a law satisfying the stated static nearest-neighbour conditional test: every
   single-site conditional given all other sites depends on the
   neighbours alone, checked on all 256 configurations — has connected
   record correlator exactly 3^-(j-i) on every pair of the 8-site path.
   Its chain rule is order-blind, but as a formation rule it conditions
   beyond neighbours (item 2). The
   Dirichlet Green function of the path Laplacian is exactly
   (i+1)(8-j)/9: linear, with non-constant successive ratios, against the
   correlator's constant ratio 1/3. A scaling matched at distance one
   already fails at distance two. Geometric against linear is an exact
   type mismatch, not a fit residual.

2. **The supplied all-pairs law fails the nearest-neighbour conditional test.** The supplied all-pairs measure is flip-invariant,
   reflection-covariant, and its chain rule is order-blind, with a
   record correlator distance-blind at exactly 835/867 on every pair
   (against 1/2187 at full span for the nearest-neighbour law). It is
   not an admissible law. Admissibility reads "one fixed
   nearest-neighbor admissibility rule", with the distribution
   "determined by, and varies with, the nearest-neighbor conditions";
   under the static reading the all-pairs law's site-0 conditional moves
   when the far site 7 flips (128/129 against 32/33), and under the
   unrestricted-order chain-rule formation reading its conditionals depend on formed non-neighbours. The
   axiom text itself does the separating. **Correction:** the first
   version of this note called nearest-neighbour locality an unrecorded
   separating clause and recorded it as a decision point; it is
   Admissibility text, and that decision point is withdrawn. Under the
   formation reading the nearest-neighbour measure's own chain rule also
   conditions beyond neighbours (site 2 given site 0 alone: 5/9 against
   4/9), while the left-to-right chain rule on this path uses only the previous nearest neighbour. Thus the counterexample concerns unrestricted orders; which order-blind laws are admissible formation rules is a
   sharper question, left to the next campaign block. One supplied long
   bond changes both direct and indirect correlations (far correlator
   1095/3281, mid correlator below twice its geometric value by one part
   in 6562): correlator reach follows pair structure, and this computation excludes the supplied nonlocal conditional, not every possible law with long-range correlations.

3. **Glued supports give exact long-range order that no two-point probe
   sees.** Under the uniform Gauss-set law of the parity-role plane — the
   completed-record law of the hard-support rule for every value-blind
   process, per the clock-and-rate and formation-unit blocks — every
   one-point and every two-point parity expectation is exactly 0, while
   every check parity and every dual-code sum is exactly 1 at full window
   span, and a non-dual triple is exactly 0. Under fair coins all of
   these vanish. This is a third correlation type: code rigidity from
   support alone, matching neither the geometric class nor the Laplacian
   kernel, present with no tick and no dynamics.

4. **What follows for the reframing.** On the exhibited windows, which
   dynamical structure appears in finished records is decided by supplied
   content — pair structure (nearest-neighbour by the axiom text) decides
   correlator reach, support structure decides rigidity, and by the wave C blocks the clock and unit decide
   hole masses without touching completed records. Nothing here derives
   an evolution law for unrecorded sites, and nothing excludes one; the
   transverse vector kernel is a named boundary. A matching correlator
   alone identifies no photon, and none is claimed.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "for an explicitly supplied admissible state, formation law and observable, compare finite or asymptotically controlled record correlators with transverse or lattice-Laplacian kernels; a supplied staggered sea, clock, Hamiltonian or comparison kernel remains an input; finite short-range examples cannot exclude all long-range laws"
source_of_blocker_text: design_note_2026-09-13
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the correlation types (geometric from nearest-neighbour pair structure, linear kernels unmatched, code rigidity from supports) and the nearest-neighbour exclusion into the assembly wave; classify which order-blind laws are admissible formation rules; construct a vector observable for the transverse kernel comparison within budget; test rigidity on the 20-site Gauss cube by citation"
conditional_surface_status: "all measures, windows, kernels and observables are supplied finite model content; nearest-neighbour determination is Admissibility text and is checked under two readings, not recorded as a decision; the no-law-level-state hypothesis stays a hypothesis"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every statement is an exact finite computation (complete 2^8 and 2^9 enumerations, exact Gaussian elimination over the rationals, chain-rule dynamic programmes) on declared measures, windows and observables; nothing is asserted beyond them"
```

## Premises and declared objects

The 8-site path with nearest-neighbour edges; the 3x3 parity-role plane
with checks and Gauss set as in the support-rule note. Pair measures on
the binary alphabet: mu_NN proportional to 2^(agreeing nearest-neighbour
pairs), mu_LR proportional to 2^(agreeing pairs over all pairs), mu_END
with the nearest-neighbour bonds plus the single long bond (0, 7). Their
chain rules condition on every formed site and are order-blind formation
laws (exhibited). Connected correlators c(i, j) = E[v_i v_j] -
E[v_i] E[v_j], exact. The comparison kernel is the Dirichlet Green
function of the path Laplacian, computed by exact rational elimination;
the transverse vector kernel is a named boundary. The uniform Gauss-set
law and parity observables (-1)^(x_i) with parities of site sets. All
supplied model content; no tick, clock, rate, Hamiltonian or evolution
law enters any computation; no axiom sentence is re-derived.

## Prior art and what is new

- Landed support-rule note (2026-09-14, wave A): the plane roles, checks,
  Gauss set, and the U(1) adjudication context that the axioms select no
  dynamics class. New here: the Gauss set's exact parity ledger — blind
  two-points, dual-code rigidity at full span — read as a correlation
  type that no propagation kernel matches.
- Landed glued/breakable/free hierarchy note (2026-09-03): glued groups.
  New here: rigidity exhibited as the record-side face of gluing, with
  the free-alphabet contrast exact.
- Landed formation-order note (2026-09-13) and the wave C campaign PRs
  8641 and 8643 (open lane, cited without status import): order-blind
  chain rules and the result that clocks and units reach only hole
  masses. New here: the correlator side of the same coin — what finished
  records show with no process choice at all.
- The design note's dynamics section (2026-09-13): the brief followed
  here sentence by sentence; the no-law-level-state proposal remains a
  hypothesis and is neither adopted nor refuted.

What is new in one line: with no tick supplied anywhere, finished
records already carry three exactly distinguishable correlation types —
geometric (nearest-neighbour pair structure), distance-blind
(supplied long bonds, excluded by the nearest-neighbour sentence), and
dual-code rigidity (supplied support) — and none of them is a
lattice-Laplacian kernel.

## Exact target and obligation graph

The design note's brief, quoted: "The original proposal's claim that
unrecorded sites carry no law-level state is a hypothesis for
investigation, not an adopted reading or a theorem. Ask which dynamical
conclusions follow under the actual axiom text and which require a
separately specified law or bridge. Do not infer that all propagating
modes must be finished-record statistics. For an explicitly supplied
admissible state, formation law and observable, compare finite or
asymptotically controlled record correlators with transverse or
lattice-Laplacian kernels. A supplied staggered sea, clock, Hamiltonian
or comparison kernel remains an input. Finite short-range examples
cannot exclude all long-range laws; a matching correlator alone does not
identify a physical photon or gravitational field."

Obligations discharged: explicitly supplied laws and observables with
exact record correlators (Theorem 1); the comparison with the
lattice-Laplacian kernel carried out and failing exactly (Theorem 2);
the impossibility of excluding long-range laws exhibited constructively
rather than asserted (Theorem 3); the support channel computed as a
third type (Theorem 4); no photon or field identified, no dynamics
inferred, the hypothesis left standing as a hypothesis.

## Theorem 1 — The geometric record correlator

mu_NN is normalised, flip-invariant and reflection-covariant with every
one-point mean exactly 0; every single-site conditional given all other
sites depends on the neighbours alone (all 256 configurations, all 8
sites), so it passes that static conditional test; no all-axiom model is certified; its chain rule reproduces it
on two explicit formation orders, and its connected record correlator is exactly
3^-(j-i) on all 28 pairs of the path. A tick-free finished-record
statistic with exact geometric decay.

## Theorem 2 — The Laplacian kernel is exactly unmatched

The Dirichlet Green function of the path Laplacian is exactly
G(i, j) = (min+1)(8-max)/9, linear along each row with non-constant
successive ratios, while the record correlator's ratio is the constant
1/3; a scaling matched at distance one fails at distance two. On this
window the exhibited law's record correlator is not a Laplacian Green
kernel, as an exact statement about decay type.

## Theorem 3 — The supplied all-pairs conditional violates nearest-neighbour dependence

mu_LR satisfies the same normalisation, flip, reflection and
order-blindness exhibits as mu_NN, and its connected correlator takes
the single exact value 835/867 on every pair — distance-blind at full
window span, against 1/2187 for the nearest-neighbour law. It violates
the Admissibility nearest-neighbour sentence under both readings: its
site-0 conditional given all other sites is 128/129 with every site up
and 32/33 after flipping only the far site 7 (static reading), and its
chain rule conditions on formed non-neighbours (formation reading). The
pair (mu_NN, mu_LR) is therefore not a pair of axiom-satisfying models:
the text itself separates them. The nearest-neighbour measure passes
the static reading exactly, and as a formation rule its chain rule
conditions on a formed non-neighbour (5/9 against 4/9 at distance two
with the middle site unformed). mu_END exhibits
the mechanism site by site: its far correlator is 1095/3281 while its
mid correlator stays below twice the geometric value, by one part in
6562 — the extra bond changes other correlations as well as its endpoints.

## Theorem 4 — Glued-support rigidity

Under the uniform Gauss-set law every one-point and two-point parity
expectation is exactly 0 (36 pairs), every check parity is exactly 1,
the check sums give exact 4-point order across the window (two
four-site dual words at full span), a non-dual triple is exactly 0, and
under fair coins every listed parity vanishes (with the empty-set parity
1 guarding the normaliser). The rigidity sits exactly on the dual code:
long-range multi-point order from support alone, invisible to every
two-point probe, with no tick and no dynamics.

For a uniform binary linear code C, the character average of (-1)^(a.x) is one when a is orthogonal to C. Otherwise choose y in C with a.y=1; pairing x with x+y cancels the sum. Here the four independent checks span the 16-word dual, and the runner now verifies the identity for all 512 characters.

## No-Go Discipline Gate

The negative content is scoped: on the 8-site path the exhibited local
law's correlator is not a Laplacian kernel, and on the plane no
two-point parity sees the Gauss rigidity.

- **N1 alternative routes.** Vector observables and the transverse
  kernel, massive or long-range comparison kernels, larger windows,
  asymptotic controls, and correlators of order-sensitive laws are
  unclassified here.
- **N2 wall independence.** Complete enumerations and exact elimination;
  no spectral input, no continuum limit, no tick.
- **N3 hidden walls.** All measures, kernels and observables are
  supplied; order-blindness is exhibited on two orders per law, not
  proved for all orders inside the runner (the chain-rule algebra is the
  general argument, stated in prose).
- **N4 residual matching.** The residual toward a photon-as-record
  claim is a vector observable of nearest-neighbour rules or supports
  plus an identification bridge; the supplied all-pairs conditional fails the stated nearest-neighbour test. No classification of alternative local, hidden-variable or order-restricted realizations is proved. Each named, none built.
- **N5 rhetoric audit.** "Not a Laplacian kernel" is an exact
  decay-type statement on the window; "distance-blind" and "rigidity"
  name exact values; the exclusion of the all-pairs law is an exact
  statement about the nearest-neighbour sentence, and long-range record
  order from supports (Theorem 4) is not excluded.
- **N6 partial-closure paths.** The transverse comparison and the
  20-site Gauss cube rigidity are open continuations; promotion routes
  stay open.
- **N7 steelman.** For the reframing: the strongest case is Theorem 4 —
  genuine long-range record order with no tick, from support alone.
  Against it: Theorem 3 rejects one supplied nonlocal conditional and does not classify all mechanisms for long reach. Neither finite comparison identifies a photon kernel. The objection
  that the path is too small for decay types is answered by exactness:
  the mismatch is algebraic (constant against non-constant ratios), not
  asymptotic.
- **N8 cross-cycle echo.** The Gauss set and its uniform completed law
  are the support-rule and wave C results, cited and recomputed where
  used; the U(1) adjudication's no-dynamics-selected stands untouched.

## Falsifiers

- Any pair of the path with c(i, j) unequal to 3^-(j-i), or a Green
  entry off the closed form, falsifies Theorems 1 and 2.
- A scaling matching the correlator to the Green kernel on three
  distances falsifies Theorem 2.
- A second exact correlator value among the all-pairs law's 28 pairs,
  an all-pairs site-0 conditional unmoved by the far site, or a
  nearest-neighbour-measure conditional that moves with a non-neighbour
  flip, falsifies Theorem 3.
- A nonzero one- or two-point Gauss parity, a check parity below 1, or
  a nonzero non-dual triple falsifies Theorem 4.

## Boundaries and non-claims

No evolution law for unrecorded sites is derived, adopted or excluded;
the no-law-level-state proposal remains a hypothesis. No photon,
gravitational field or physical identification is made or approached;
the transverse vector kernel is a named boundary, not computed. The
Laplacian statement is a decay-type mismatch on the exhibited window,
not an all-window or all-law exclusion. The all-pairs law is exhibited
as excluded by the nearest-neighbour sentence. Nearest-neighbour
determination is axiom text, not a decision point; the first version's
decision point is withdrawn. Nothing here grades, unlocks or audits any
other claim.

## Imports

Supplied measures, kernels, windows and observables; standard finite
probability and exact linear algebra. Cited landed notes carry their own
scopes; the open wave C PRs are cited as an open lane. No audit grade,
no new axiom, no new primitive, no new comparator and no new framing is
imported.

## Original author review record (historical)

- **Seat:** one Fable 5.1 seat for the first version; the correction
  below by one Opus 5.5 seat; no subagents.
- **Correction before landing (2026-09-22):** the first version recorded
  nearest-neighbour locality as an unrecorded separating clause and
  called (mu_NN, mu_LR) a witness pair agreeing on every stated
  sentence. Admissibility already states a nearest-neighbour rule whose
  distribution is determined by the nearest-neighbor conditions; the
  all-pairs law violates that sentence under both readings. The runner
  now checks both readings exactly (four added checks), the decision
  point is withdrawn, and the files are renamed accordingly.
- **Independence sources:** (i) the geometric correlator checked against
  the closed form 3^-(j-i) on all 28 pairs, itself the standard
  open-boundary transfer argument recomputed by complete enumeration;
  (ii) the Green function checked against the closed form
  (min+1)(8-max)/9 site by site, the elimination against the formula;
  (iii) order-blindness checked by two explicit orders per law against
  the directly computed measure; (iv) the Gauss parities checked against
  the dual-code account (zero exactly off the dual span, one exactly on
  it) with the free-alphabet and empty-set contrasts guarding the
  normaliser.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| corr drops the mean subtraction | second term removed | missed; masked non-defect (means identically 0, guarded by the zero-mean checks) |
| pair-measure base 2 to 3 | correlation strength changed | caught (2 FAILs) |
| Laplacian loses a diagonal unit at the ends | Dirichlet degraded | caught (crash, nonzero exit) |
| elimination forward-only | back-substitution removed | caught (crash) |
| chain rule unnormalised | drop `/ base` | caught (2 FAILs) |
| checks drop the V site itself | `[v] +` removed | caught (crash) |
| parity average hard-codes 32 | `/ len(sample)` to `/ 32` | caught after strengthening (1 FAIL) |
| check sum uses union not symmetric difference | `!=` to `or` | caught (1 FAIL) |
| all-pairs list skips adjacent pairs | `i + 1` to `i + 2` | caught (1 FAIL) |
| static test treats next-nearest sites as neighbours | neighbour set widened to distance two | caught after strengthening (1 FAIL, next-nearest control) |

  The parity-normaliser mutant was missed before the empty-set-parity
  guard was added and is caught after it, in the support-rule note's
  tradition of recording the strengthening. The mean-subtraction mutant
  is a masked non-defect: every mean is identically zero on these
  flip-invariant laws, and the explicit zero-mean checks pin that down.
  The widened-neighbour mutant was missed until the next-nearest-bond
  control was added and is caught after it. Nine of nine defect mutants
  are caught.
- **Vacuity guard:** every computed object is compared against an
  independent closed form or a structurally different account (transfer
  form, Green formula, dual code); the contrast checks assert exact
  zeros and exact ones side by side; the empty-set parity guards the
  normalisation of the parity average.
- **Budget:** 18 checks, stdout 2834 characters (ceiling 6000), 0.14 s
  elapsed (ceiling 900 s), exact Fractions; largest enumerations 2^8
  and 2^9; no dense numeric space at or above 2^11.

## Verification

```bash
python3 scripts/record_dynamics_correlator_kernels_nearest_neighbour_sentence_and_glued_support_rigidity_2026_09_22.py
```

Original runner summary before review fixes: `TOTAL: PASS=18 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/record_dynamics_correlator_kernels_nearest_neighbour_sentence_and_glued_support_rigidity_2026_09_22.txt`.
