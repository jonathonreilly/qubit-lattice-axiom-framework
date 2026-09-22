---
claim_id: order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading of the Admissibility sentence (a nearest-neighbour rule applied sequentially along a formation order). For every alphabet: an order-blind hole-free nearest-neighbour rule makes every set of pairwise non-adjacent sites independent with the one-site law, so no record correlation survives beyond nearest neighbours; an order-blind strictly positive translation-covariant rule has the exact product form r(a|N) = r0(a) prod phi_d(a,b) with bond-symmetric factors normalised on every neighbour condition, already forced on the 7-site cross. Under the unsoldered reading such rules are constant, so with the variation sentence every strictly positive admissible rule is order-sensitive on the 7-site cross. Under the soldered reading: exact non-existence of varying order-blind rules on the 6-, 8- and 12-point cube orbits; explicit varying order-blind rules on a single 24-point orbit, on the 48-point chiral pair and on the Haar sphere, each exhibited with exact checks. No rule, reading, order law or clock is selected; nothing is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - formation_order_covariance_and_isotropic_binary_order_blind_classification_bounded_theorem_note_2026-09-13
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/order_blind_nn_formation_independence_unsoldered_constancy_soldered_escape_2026_09_22.py
---

# Order-blind nearest-neighbour formation: independence beyond neighbours, unsoldered constancy, and the soldered cube-orbit escape

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses (design note 2026-09-13; assembly graph,
open PR 8648). The assembly left downstream gravity behind four recorded
decisions: clock, locality, roles, soldering. This block asks what the
Admissibility text itself says when the clock decision's candidate
"order-blind physical rule" meets the text's own nearest-neighbour and
variation sentences.

## Result up front

1. **Order-blind nearest-neighbour formation carries no correlation
   beyond nearest neighbours, on every alphabet.** If a nearest-neighbour
   rule that never fails is order-blind on a window, every set of
   pairwise non-adjacent sites is independent with the one-site law: form
   those sites first, and none of them has a formed neighbour. Every
   record correlation at graph distance two or more vanishes exactly. On
   the 3-site path the order-blind soldered rules below give ends that are
   exactly independent, while adjacent sites correlate at exactly 1/72.

2. **Order-blind strictly positive rules have one exact form, forced
   already on the 7-site cross.** Exchange between the centre and one leaf
   of the site-plus-six-neighbours window gives
   r(a | N) = r0(a) prod over formed neighbours of phi_d(a, b), with
   bond-symmetric factors phi_d(a, b) = phi_-d(b, a) and
   E_r0[prod phi_d(., b_d)] = 1 for every neighbour condition; conversely
   every such family is order-blind on every window.

3. **Under the unsoldered reading the text forces order-sensitive
   formation.** Values are not rotated with positions, so the factor is
   the same for every direction. Two neighbours holding one value then
   give E_r0[phi^2] = 1 = E_r0[phi]^2, so phi = 1 and the rule is
   constant. Admissibility requires the distribution to vary with the
   nearest-neighbor conditions, so no strictly positive admissible rule
   is order-blind under this reading: some two formation orders of the
   7-site cross give different finished-record laws. This extends the
   landed binary classification to every alphabet, including the
   continuum Bloch sphere. The clock decision's candidate "order-blind
   physical rule" is excluded here; the order is recorded in the records.

4. **Under the soldered reading order-blind rules that vary exist on
   the generic 24-point orbit and the sphere, and not on the
   high-symmetry orbits.** On the 6-, 8- and 12-point cube orbits the six bond spaces
   must be mutually orthogonal eigenlines, and exact algebra shows no
   real eigenline meets the two pair conditions, so every order-blind
   positive rule is constant. On a single 24-point orbit, the sign of the
   two coordinates transverse to d on the cap a.d = 3 gives a varying
   order-blind rule. So does chirality on the same caps of the 48-point
   chiral pair, and a centred profile on disjoint polar caps
   {a.d > 3/4} of the Haar sphere. Each is checked exactly: covariance,
   bond symmetry, normalisation on every neighbour condition, and one
   finished law for all six orders of the path. By item 1 all of them are
   correlated at nearest neighbours only.

5. **What moves in the decision structure.** The clock decision loses
   "order-blind physical rule" under the unsoldered reading with positive
   rules. Under the soldered reading it survives on the exhibited
   generic alphabets (not on the 6-, 8-, 12-point orbits) and only with
   nearest-neighbour reach. In every reading, a
   record correlation at distance two or more from an admissible rule
   that never fails certifies order-sensitive formation or a support with
   holes. Locality is Admissibility text, not a decision; the static
   reading of the same sentence (conditionals given all other sites)
   admits the geometric correlations of the nearest-neighbour pair
   measure, so the two readings separate exactly on reach.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the assembly graph leaves downstream gravity behind the recorded decisions clock, locality, roles and soldering; test whether the Admissibility text constrains the clock decision's order-blind candidate through its nearest-neighbour and variation sentences"
source_of_blocker_text: assembly_graph_open_pr_8648
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the forced order-sensitivity into the assembly graph (clock decision without its order-blind candidate under the unsoldered reading; locality as axiom text); test integer glued supports and value clocks for record reach beyond nearest neighbours; classify higher-rank soldered rules on generic orbits"
conditional_surface_status: "formation reading of the Admissibility sentence; strict positivity where stated; supplied alphabets and example rules; no rule, reading, order law or clock is selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorems 1-3 are short proofs valid for every alphabet under stated hypotheses; Theorem 4 is exact finite algebra on declared cube orbits plus exact polynomial integrals on the Haar sphere; every exhibit is an exact rational computation"
```

## Premises and declared objects

The Admissibility text: "There is one fixed nearest-neighbor admissibility
rule, covariant under lattice translations and proper cubic rotations. For
each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions." Read
with Record in the formation reading (reading note 2), a rule assigns to
each neighbour condition N — the partial map from the six directions to
the values of the formed in-window neighbours — a distribution r(. | N),
used sequentially along a formation order sigma of a window; the finished
law of sigma is the product of the conditionals along sigma. The rule
never fails when every r(. | N) is a probability distribution; it is
strictly positive when every r(a | N) > 0 (on the continuum, a density
positive almost everywhere against the Haar reference). It is order-blind
on a window when every formation order gives the same finished law.
Translation covariance: one rule at every site. Rotation covariance,
unsoldered: r(a | N o g^-1) = r(a | N), values untouched; soldered:
r(g a | g N) = r(a | N), values rotated with positions. Alphabets: the
cube orbits of sizes 6, 8, 12, 24 (the orbit of (1, 2, 3)), the 48-point
union of the two proper-rotation orbits of (1, 2, 3), and the Bloch
sphere with Haar measure, whose push-forward to t = a.d is uniform on
[-1, 1]. Windows: the 3-site path and the 7-site cross (a site with its
six neighbours). All exhibited rules are supplied examples; no axiom
sentence is re-derived.

## Prior art and what is new

- Landed binary classification note (2026-09-13): no invariant total
  order on Z^3; order-blindness of a nearest-neighbour rule is equivalent
  to exchange on positive prefixes for adjacent pairs (its Theorem 2, used
  here); interior isotropic binary order-blind rules are constant. New
  here: Theorem 1 for every alphabet with no positivity; the exact product
  form and its converse (Theorem 2); constancy for every alphabet under
  the unsoldered reading, by a variance argument on the 7-site cross
  (Theorem 3); and the soldered classification with explicit varying
  order-blind rules (Theorem 4).
- Landed formation-order and possibility-covariance notes (2026-09-13,
  2026-09-14): order laws, and the two readings of covariance. New here:
  the readings separate on whether order-blind formation can vary at all.
- Open campaign PRs 8641 (clock-and-rate), 8643 (formation-unit), 8646
  (record-dynamics) and 8648 (assembly): the clock decision's candidate
  "order-blind physical rule", the invisibility of clocks for order-blind
  chain rules that condition beyond neighbours, and the nearest-neighbour
  sentence's exclusion of long-range pair structure. New here: within the
  text's own nearest-neighbour rules, order-blindness is either impossible
  with variation (unsoldered) or confined to nearest-neighbour reach
  (soldered). Cited as an open lane, not as landed status.

What is new in one line: the text's nearest-neighbour and variation
sentences, read in the formation reading, force order-sensitive formation
under the unsoldered reading for every strictly positive rule, and bound
every order-blind rule to nearest-neighbour correlations in every reading.

## Exact target and obligation graph

Target: the status of the clock decision's candidate "order-blind physical
rule" against the Admissibility text, and the reach of order-blind
formation. Obligations: (i) the reach of order-blind rules, on every
alphabet (Theorem 1); (ii) the exact form of order-blind strictly positive
rules (Theorem 2); (iii) the unsoldered reading against the variation
sentence (Theorem 3); (iv) the soldered reading on the declared alphabets,
with non-existence proved where it holds and explicit rules where it
fails (Theorem 4); (v) the consequences for the recorded decisions,
stated without adopting any.

## Theorem 1 — Order-blind nearest-neighbour formation is independent beyond neighbours

Let a nearest-neighbour rule that never fails be order-blind on a window
W, and let I be a set of pairwise non-adjacent sites of W. Then the
finished law restricted to I is the product of the one-site laws
r(. | empty). Proof: choose an order that forms I first; each site of I
then forms with no formed neighbour, so its conditional is r(. | empty),
and the sites formed later do not change the marginal of I. Order-blindness
carries the marginal to every order. In particular every record
correlation between sites at graph distance two or more vanishes. No
positivity, covariance or alphabet assumption enters; the never-fails
hypothesis is needed, since a support with holes conditions on completion
(the glued-support rigidity of the record-dynamics block is of that kind).
Exhibits: the 48-point and 24-point rules below give exactly independent
ends on the path (every pair mass 1/48^2, respectively 1/24^2) while
adjacent sites correlate at kappa/36; the pair-measure chain rule, which is
order-blind but reads a non-neighbour (5/9 against 4/9), correlates the
ends at 1/9; the local rule 2^(agreeing neighbours), which is
nearest-neighbour but order-sensitive, correlates the ends at 1/9
chain-first and at 0 ends-first.

## Theorem 2 — The exact form of order-blind strictly positive rules

Let a strictly positive translation-covariant nearest-neighbour rule be
order-blind on the 7-site cross. Then for every neighbour condition N,

r(a | N) = r0(a) prod_{(d, b) in N} phi_d(a, b),
phi_d(a, b) = r(b | {-d: a}) / r0(b),

with phi_d(a, b) = phi_-d(b, a) and E_r0[prod_{(d, b) in N} phi_d(., b)] = 1
for every N. Conversely every family with these properties is order-blind
on every window. Proof: by the landed exchange characterization,
order-blindness on the cross is exchange for each centre-leaf pair on
every positive prefix. With the leaf at direction d, its own condition
empty and the other leaves formed as N, exchange reads
r(a | N) r(b | {-d: a}) = r(b | empty) r(a | N + {d: b}), which is the
factor rule; iterating over the formed leaves gives the product form. The
leaf's one-neighbour conditional is the rule itself at a site whose only
formed neighbour lies at -d, so r(b | {-d: a}) = r0(b) phi_-d(b, a), which
is bond symmetry. Normalisation of r(. | N) is the moment identity.
Conversely, for adjacent sites in any window with any backgrounds the two
sides of exchange differ only by phi_d(a, b) against phi_-d(b, a), and
non-adjacent pairs exchange trivially. The exhibits verify bond symmetry
on all 6 x 48 x 48 and 6 x 24 x 24 cases and normalisation on all 4^6 =
4096 value classes of neighbour conditions for both finite rules.

## Theorem 3 — Unsoldered reading: order-blind strictly positive rules are constant

Under the unsoldered reading the one-neighbour conditional r(b | {-d: a})
is invariant under the rotations about the site, which act transitively
on the six directions with values untouched; hence phi_d = phi for every
d. Take two formed neighbours holding one value b: E_r0[phi(., b)^2] = 1,
and a single one gives E_r0[phi(., b)] = 1, so
E_r0[(phi(., b) - 1)^2] = 0 and phi(., b) = 1 on the support of r0, which
is the whole alphabet by strict positivity. So r(a | N) = r0(a) for every
N: the rule is constant. The argument holds on every alphabet, finite or
the Haar sphere (almost everywhere), and already on the 7-site cross.
Because Admissibility requires the distribution to vary with the
nearest-neighbor conditions, a strictly positive admissible rule under
the unsoldered reading is never order-blind: some two formation orders of
the 7-site cross give different finished-record laws. Exhibits: the
direction-blind copy of the 48-point factor gives total mass 25/24 for two
equal neighbours, so it is not even a rule; the unsoldered Potts family on
the six-axis alphabet fails exchange on the cross for every sampled
kappa != 0 (kappa = 1: 4/49 against 2/27) and passes only at kappa = 0.

## Theorem 4 — Soldered reading: where order-blind rules can vary

Under the soldered reading phi_{gd}(g a, g b) = phi_d(a, b) and r0 is
invariant. The bond spaces W_d = span_b {phi_d(., b) - 1} are subspaces
of the mean-zero functions with W_{gd} = g W_d, W_{e_z} invariant under
the quarter-turn about e_z, and normalisation on two distinct directions
makes them mutually orthogonal.

(a) On a single cube orbit of n points (uniform r0), six orthogonal copies
fit in dimension n - 1 only if dim W_d <= floor((n - 1)/6): 0, 1, 1 for
n = 6, 8, 12. A nonzero invariant line is a real eigenline of the
quarter-turn (eigenvalue +1 or -1). Every pair of distinct directions is
rotation-equivalent to an opposite or a perpendicular pair, so a line
must meet two quadratic conditions; on all six eigenspaces of the three
orbits the two conditions share only the zero real solution (on
one-dimensional spaces a nonzero coefficient; otherwise one condition is
a rank-one square whose kernel carries a definite restriction of the
other), so only w = 0 remains. Every order-blind strictly
positive soldered rule on these orbits is constant.

(b) On the single 24-point orbit of (1, 2, 3), let X_d(a) be the sign of
the product of the two coordinates of a transverse to d when a.d = 3, and
0 otherwise. Every point has exactly one coordinate of modulus 3, so the
six supports are disjoint; the quarter-turn alternates the sign around
each cap, so each X_d has mean 0; and the sign change of X_d and X_-d
under a rotation is the same (one transverse plane), so
phi_d(a, b) = 1 + kappa X_d(a) X_-d(b), |kappa| < 1, is covariant and
bond-symmetric. At any value at most one factor differs from 1, so every
product of factors has mean exactly 1. By Theorem 2 the rule is order-blind
on every window, and it varies.

(c) On the 48-point chiral pair, chirality (+1 on one proper-rotation
orbit, -1 on the other) on the same caps gives a second varying
order-blind rule; on the Haar sphere, X(t) = (t - 7/8) 1[t > 3/4] on the
pairwise disjoint caps {a.d > 3/4} (disjoint because 2 (3/4)^2 > 1), with
mean 0 and second moment 1/1536, gives a third, with kappa = 32 keeping
every factor in [1/2, 3/2] and nearest-neighbour correlation exactly
1/73728.

By Theorem 1 all three have record correlations at nearest neighbours
only. The high-symmetry orbits 6, 8, 12 are the soldered menus of the
possibility-covariance and menus-and-Born blocks; the exhibited
soldered order-blind variation lives on a generic orbit, the chiral pair
and the continuum. Other generic orbits and higher-rank bond spaces are
not classified.

## Consequences for the recorded decisions

- **Locality** is Admissibility text ("one fixed nearest-neighbor
  admissibility rule"), not a decision; the assembly graph's locality
  group is withdrawn (the record-dynamics PR was corrected before
  landing; the assembly PR is to be corrected in place).
- **Clock.** Under the unsoldered reading with strictly positive rules,
  the candidate "order-blind physical rule" is excluded by the text
  (Theorem 3): formation order enters the finished records, and which
  order law holds is the remaining decision. Under the soldered reading
  the candidate survives on the 24-point orbit, the 48-point pair and
  the sphere, fails on the 6-, 8-, 12-point orbits (Theorem 4), and
  carries nearest-neighbour reach only (Theorem 1).
- **Reach.** In every reading, an admissible rule that never fails and
  produces a record correlation at distance two or more is order-sensitive
  (contrapositive of Theorem 1), or the correlation comes from a support
  with holes. Long-range record statistics of the kind the gravity and
  record-dynamics targets need therefore run through order-sensitive
  formation or through supports.
- **Reading of the sentence.** The static reading (conditionals given all
  other sites) admits the nearest-neighbour pair measure with geometric
  correlations at every distance; the formation reading with
  order-blindness admits nearest-neighbour correlations only. The reading
  notes are interpretive; the two readings are recorded side by side as a
  decision point, with this exact separation attached.

## No-Go Discipline Gate

The negative content is scoped: under the formation reading, no strictly
positive unsoldered-covariant rule that varies is order-blind; no
order-blind rule that never fails correlates non-adjacent sites; no
strictly positive soldered order-blind rule varies on the 6-, 8- or
12-point orbits.

- **N1 alternative routes.** Rules with zeros but no failures under the
  unsoldered reading, higher-rank soldered rules on generic orbits,
  mixed-orbit alphabets, and the static reading are not classified here.
- **N2 wall independence.** The proofs use only the exchange identity,
  positivity and covariance; no dynamics, clock, spectral input or limit.
- **N3 hidden walls.** The formation reading and strict positivity are
  stated hypotheses. The finite exhibits are complete where stated
  (all orders of the path, all value classes, all rotations); the sampled
  kappa values in the Potts exhibit illustrate Theorem 3, whose proof is
  general.
- **N4 residual matching.** The residual on the clock decision is the
  choice of order law (unsoldered) or of a generic alphabet with
  nearest-neighbour reach (soldered), matching the recorded candidates
  minus the one excluded.
- **N5 rhetoric audit.** "Forces" and "excluded" are used only where a
  proof covers every rule under the stated hypotheses; "exists" only
  with an explicit rule exhibited exactly.
- **N6 partial-closure paths.** The unsoldered statement with zeros, the
  static reading, and higher-rank soldered rules are open continuations.
  Promotion routes stay open.
- **N7 steelman.** Against Theorem 3: a rule with zeros could vary and be
  order-blind under the unsoldered reading without failing; the
  hypothesis is stated and that case is left open. Against the reach
  statement: supports with holes do produce long-range order (the
  record-dynamics rigidity), and the statement names them as the other
  route. For the soldered escape: it is real but confined to
  nearest-neighbour reach, so it cannot carry long-range statistics.
- **N8 cross-cycle echo.** The binary classification is the special case
  of Theorem 3 on the binary alphabet and is cited, with a different
  proof here; the exchange characterization is the landed theorem, used.

## Falsifiers

- An order-blind rule that never fails with a nonzero correlation between
  non-adjacent sites falsifies Theorem 1.
- A strictly positive order-blind rule on the 7-site cross violating the
  product form, bond symmetry or the moment identity falsifies Theorem 2.
- A strictly positive unsoldered-covariant rule that varies and is
  order-blind on the 7-site cross falsifies Theorem 3.
- A varying order-blind strictly positive soldered rule on the 6-, 8- or
  12-point orbit, or a failure of any listed check for the 24-point,
  48-point or Haar rules, falsifies Theorem 4.

## Boundaries and non-claims

No rule, reading, order law or clock is selected; nothing is adopted.
Theorem 3 assumes strict positivity; rules with zeros that never fail are
not classified under the unsoldered reading. Theorem 4's non-existence
covers the three single orbits; generic orbits beyond the exhibited rules,
higher-rank bond spaces, and mixed alphabets are not classified. The
static reading is compared, not adopted or refuted. Supports with holes
are outside Theorem 1 and are the named route to long-range order. No
physical identification (photon, gravity, time) is made. Nothing here
grades, unlocks or audits any other claim.

## Imports

Supplied alphabets, windows, example rules and the Haar push-forward to
t = a.d; the landed exchange characterization; standard finite linear
algebra over the rationals. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) order-blindness of the 48- and 24-point
  rules on the path computed directly over all six formation orders, not
  inferred from Theorem 2's converse; (ii) normalisation checked by direct
  sums over all 4096 value classes of neighbour conditions, independent of
  the disjoint-support argument; (iii) the non-existence on the 6-, 8-,
  12-point orbits decided by exact quadratic-form algebra in the runner,
  cross-checked during development by an independent symbolic solve (on
  the 12-point orbit's eigenvalue -1 space the only common zeros are
  complex, c0 = -+ i sqrt(2) c2 / 2) and by a floating-point scan whose
  residual minima stayed clearly positive; (iv) the 24-point rule was
  found by that scan (residual 8.7e-23 on the eigenvalue -1 space) and
  then verified exactly; (v) two controls give the decision procedure
  teeth: it rejects a pair of forms with a shared real zero, and the
  24-point transverse sign meets both pair conditions in the same
  machinery.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| coupling set to zero | kappa = 1/2 to 0 (constant rule) | caught (4 FAILs) |
| chirality lost | both orbits +1 | caught (7 FAILs) |
| bond factor reads the wrong neighbour cap | X_-d(b) to X_d(b) | caught (5 FAILs) |
| formation ignores formed neighbours | neighbour condition emptied | caught (2 FAILs) |
| chain rule unnormalised | drop the denominator | caught (2 FAILs) |
| local rule loses its coupling | base 2 to 1 | caught (1 FAIL) |
| Potts coupling ignored | factor 1 + kappa to 1 | caught (1 FAIL) |
| cap threshold 3/4 to 1/2 | caps overlap | caught (3 FAILs) |
| transverse axes fixed to (x, y) | direction ignored | caught (1 FAIL) |
| decision procedure always accepts | rank-one branch returns True | caught (1 FAIL, control) |
| eigen-rows sign flipped | computes the other eigenvalue's space | caught after strengthening (1 FAIL; the verdict itself was unchanged because both eigenspaces are analysed, so the eigenspace dimensions (2,1), (1,2), (2,3) are now asserted) |

  Eleven of eleven mutants are caught, one after the dimension assertion was added.

- **Vacuity guard:** every equality compares independently computed
  objects or stated exact rationals; the order-blindness exhibits compare
  six separately computed laws; the non-existence verdicts are paired
  with a positive control on which the same machinery finds a solution.
- **Budget:** 27 checks, stdout 4291 characters (ceiling 6000), about 16 s
  (ceiling 900 s), exact Fractions throughout; largest enumeration the
  48^3 = 110592 path configurations per order; no dense state space.

## Verification

```bash
python3 scripts/order_blind_nn_formation_independence_unsoldered_constancy_soldered_escape_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=27 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/order_blind_nn_formation_independence_unsoldered_constancy_soldered_escape_2026_09_22.txt`.
