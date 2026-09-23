---
claim_id: order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading of the Admissibility sentence (a nearest-neighbour rule applied sequentially along a formation order). For every finite alphabet: an order-blind hole-free nearest-neighbour rule makes every set of pairwise non-adjacent sites independent with the one-site law, so non-adjacent individual sites have independent marginals; an order-blind strictly positive translation-covariant rule has the exact product form r(a|N) = r0(a) prod phi_d(a,b) with bond-symmetric factors normalised on every neighbour condition, already forced on the 7-site cross. Under the unsoldered reading such rules are constant, so with the variation sentence every strictly positive admissible rule is order-sensitive on the 7-site cross. Under the soldered reading: exact non-existence of varying order-blind rules on the 6-, 8- and 12-point cube orbits; explicit varying order-blind rules on a single 24-point orbit, on the 48-point chiral pair and on the Haar sphere, each exhibited with exact checks. No rule, reading, order law or clock is selected; nothing is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/order_blind_nn_formation_independence_unsoldered_constancy_soldered_escape_2026_09_22.py
---

# Order-blind nearest-neighbour formation: independence beyond neighbours, unsoldered constancy, and the soldered cube-orbit escape

**Date:** 2026-09-22
**Type:** bounded_theorem
The results below concern explicitly supplied finite formation models.
Their parameters, alphabets, orders and sampling laws are conditions of the
calculation, not additional framework premises.

## Result up front

1. **Order-blind nearest-neighbour formation carries no correlation
   beyond nearest neighbours, on every finite alphabet.** If a nearest-neighbour
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

3. **On positive finite support, unsoldered variation implies order sensitivity.** Values are not rotated with positions, so the factor is
   the same for every direction. Two neighbours holding one value then
   give E_r0[phi^2] = 1 = E_r0[phi]^2, so phi = 1 and the rule is
   constant. Admissibility requires the distribution to vary with the
   nearest-neighbor conditions, so no strictly positive admissible rule
   is order-blind under this reading: some two formation orders of the
   7-site cross give different finished-record laws. This extends the
   landed binary classification to every finite alphabet, on the positive-mass finite support. This is a theorem within the stated sequential model, not a choice of
   physical interpretation.

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
   finished law for all six orders of the path. By item 1 their non-adjacent individual-site marginals are independent.

5. **The implication stays within the model.** Non-adjacent correlations
   contradict order-blindness for normalized sequential nearest-neighbour
   draws. The explicit directional examples establish conditional mathematical
   possibilities, not physical realizations or an axiom interpretation.

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
conditional_surface_status: "formation reading of the Admissibility sentence; strict positivity where stated; supplied alphabets and example rules; no rule, reading, order law or clock is selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorems 1-3 are short proofs valid for every finite alphabet under stated hypotheses; Theorem 4 is exact finite algebra on declared cube orbits plus exact polynomial integrals on the Haar sphere; every exhibit is an exact rational computation"
```

## Premises and declared objects

The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the
sampling process studied here. Sequential draws use the declared conditional
law given the previously formed configuration, with fresh randomness at each
step; a chosen order is external to those draws. Correlated joint draws and
adaptive orders are separate models. Skipping a failed attempt and continuing,
or dropping its whole history, are supplied alternatives. Neither convention
follows from unreadability alone.


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
carries the marginal to every order. In particular every two-site
correlation between non-adjacent sites vanishes. No
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
on every window. Proof: by comparing the two adjacent orders and marginalizing subsequent normalized draws,
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
N: the rule is constant. The argument holds on every finite alphabet, finite with positive one-site mass, and already on the 7-site cross.
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

By Theorem 1 all three have independent marginals on sets of pairwise non-adjacent
individual sites; this does not assert independence of separated multi-site blocks. The high-symmetry orbits 6, 8, 12 are the soldered menus of the
possibility-covariance and menus-and-Born blocks; the exhibited
soldered order-blind variation lives on a generic orbit, the chiral pair
and the continuum. Other generic orbits and higher-rank bond spaces are
not classified.

## Consequences and limits

The finite constructions distinguish the stated sampling laws and orders.
They do not choose a physical formation law, exclude alternatives outside the
stated support, or settle gravity, clock, locality or alphabet decisions.

## No-Go Discipline Gate

The negative scope is only the explicitly stated finite-model implication or
independent-clock bound. No general physical formation exclusion is claimed.

**N1 — Five distinct challenges.** Each is ATTEMPTED by the local argument
or the named finite computation, with its outcome kept explicit:

- **Nonlocal conditionals (ATTEMPTED):** the exact pair-measure chain rule keeps distance-two correlation; it escapes by reading a non-neighbour.
- **Order-sensitive local draws (ATTEMPTED):** the local binary rule gives different endpoint correlations for chain-first and ends-first orders.
- **Finite unsoldered variation (ATTEMPTED):** the two-neighbour variance identity forces zero variance under normalized order-blind sampling.
- **Small directional alphabets (ATTEMPTED):** the six-, eight- and twelve-point orbit quadratic forms exclude the stated nonzero bond lines.
- **Generic directional alphabets (ATTEMPTED):** the 24/48-point and disjoint-cap constructions are explicit positive escapes from unsoldered constancy, not excluded by the general reach theorem.

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
t = a.d; the adjacent-order product comparison proved here; standard finite linear
algebra over the rationals. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Author check record (original proposal)

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

## Landing review correction

Serial source review in one Codex session under the owner's no-subagent
instruction narrowed physical interpretations to supplied model conditions.
Original author check reports above are historical; they do not certify these
corrections. Current source-bound executions and independent controls are
recorded in the combined landing evidence. No independent audit is claimed.

## Verification

```bash
python3 scripts/order_blind_nn_formation_independence_unsoldered_constancy_soldered_escape_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=27 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/order_blind_nn_formation_independence_unsoldered_constancy_soldered_escape_2026_09_22.txt`.
