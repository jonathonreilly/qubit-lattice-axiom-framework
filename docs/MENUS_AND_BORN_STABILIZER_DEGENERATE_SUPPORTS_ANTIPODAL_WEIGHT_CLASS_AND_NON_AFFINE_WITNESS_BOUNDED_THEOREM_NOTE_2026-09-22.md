---
claim_id: menus_and_born_stabilizer_degenerate_supports_antipodal_weight_class_and_non_affine_witness_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Exact finite census of covariant supports for zero, one, two and three supplied neighbours on real unit Bloch vectors, using exact rational witnesses and normalized integer direction alphabets under the soldered (diagonal proper-cubic) and unsoldered (independent lattice and internal rotation) actions, including the stabiliser-degenerate antiparallel and parallel pairs; six-axis free-parameter counts by two independent methods (one neighbour 9; opposite pairs 24 over 9 orbits; adjacent pairs 87 over 21 orbits); the antipodal weight class f(p.q) with the affine reduction, the repeat-certainty selection of c = 1, two explicit non-affine witnesses and exact separating moments; soldered menu t-sets and the fourth-moment invariant. No all-axiom model, no physical Born derivation, no axiom selection; the affinity and menu-supplier clauses are recorded as decision points."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - covariant_effect_map_nonselection_and_repeat_certainty_collapse_bounded_theorem_note_2026-07-11
  - admissibility_six_neighbor_affine_cq_channel_solder_support_boundary_bounded_theorem_note_2026-08-14
  - admissibility_sharp_qubit_record_writer_orientation_axiom_decision_bounded_theorem_note_2026-09-01
  - born_price_wordings_homogeneity_collinear_menus_four_outcome_fair_coin_2026_09_05
  - composition_law_selection_graded_zeros_order_blind_rules_bounded_theorem_note_2026-09-13
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
runner: scripts/menus_and_born_stabilizer_degenerate_supports_and_antipodal_weight_class_2026_09_22.py
---

# Menus and Born: stabiliser-degenerate supports, the antipodal weight class, and two non-affine witnesses

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign block:** menus-and-Born, wave B of the TOE derivation campaign by
underdetermination witnesses (design note 2026-09-13). The block asks which
antipodal-menu weight laws survive covariance and a precisely formulated
exchange condition, with every selecting condition named explicitly, and it
carries the support census into the stabiliser-degenerate configurations that
the open menus work left aside.

## Result up front

1. **The antiparallel pair forces the fair coin unsoldered, and splits the
   two readings.** The configuration with recorded value q at position +z and
   -q at position -z is fixed, under the unsoldered action, by the pair
   (lattice 180-degree turn about x, internal 180-degree turn about any u
   orthogonal to q), and this fixer sends q to -q. Covariance alone therefore
   forces w(q) = w(-q) = 1/2 for every rational unit q, with no slot-symmetry
   assumption; the perpendicular partner is constructed rationally as
   u = rot180(e_z + q) e_x for q distinct from -e_z. Under the soldered
   action the same configuration forces the fair coin exactly on the family
   q_x q_y (q_x^2 - q_y^2) = 0 (q orthogonal to one of the four horizontal
   two-fold axes x, y, (1,1,0), (1,-1,0)); off that family the soldered
   stabiliser is the identity alone. The two readings of the covariance
   sentence therefore agree on the fair coin on a thin family and disagree
   off it: a sharpening of the soldering fork on a two-point menu.

2. **Covariance compresses every antipodal weight law to one function, and
   affinity is the clause that selects the linear class.** SO(3)
   transitivity identifies every pair at equal p.q, so a covariant weight is
   a function f(t), t = p.q. Affinity in the neighbour state, plus
   covariance, leaves f(t) = (1 + c t)/2 with one constant c; same-label
   repeat certainty f(1) = 1 then buys c = 1, the Born form, inside that
   class. The anti-Born flip c = -1 passes normalisation and positivity and
   is removed by same-label repeat certainty alone. Two explicit non-affine
   laws, (1 + t^3)/2 and (1 + t)/2 + t(1 - t^2)/8, pass every other stated
   condition (normalisation as a polynomial identity, positivity by exact
   monotonicity, both endpoint conditions); affinity fails at the midpoint
   (9/16 and 51/64 against the affine 3/4). The class is convex.

3. **The first record moment separates what the second cannot see.**
   E[s.q] under Haar-uniform relative orientation is 1/3 (Born), 1/5
   (cubic), 11/30 (monotone witness), 4/15 (midpoint mixture), c/3 on the
   affine family, and 1/2 for the step law; E[(s.q)^2] = 1/3 for every
   normalised f, and E[(s.q)^3] separates again (1/5, 1/7, 3/14). Born is
   neither extremal in the full normalised class nor singled out by these
   statistics; within the affine family it is the c = 1 endpoint.

4. **Soldered alphabets quantise the menu and are separated from the
   continuum by the fourth-moment invariant.** The six-axis, 8-point and
   12-point cube-orbit menus restrict t to {0, +-1}, {+-1/3, +-1} and
   {0, +-1/2, +-1}; the invariant p_x^4 + p_y^4 + p_z^4 takes the values 1,
   1/3, 1/2 against the Haar mean 3/5, and 24-point orbits carry a modulus
   (1/2 for (1,2,3), 13/21 for (1,2,4)).

5. **Census with two independent counts.** Under the soldered action on the
   six-axis alphabet: one neighbour leaves 9 free weight parameters (orbits
   6 + 6 + 24, contributions 2 + 2 + 5); opposite-position pairs leave 24
   over 9 configuration orbits, with the antiparallel aligned pair at
   stabiliser D4 (order 8, one free parameter, coin forced) and the parallel
   aligned pair at C4 (two free parameters, no forced coin); adjacent pairs
   leave 87 over 21 orbits. An orbit-stabiliser count and an independent
   count of orbits on (configuration, value) pairs agree on all three.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "test whether covariance and a precisely formulated exchange condition restrict normalized antipodal-menu weights f(p.q); affinity alone leaves a coefficient in f(t) = (1 + c t)/2 and does not select the Born value; any endpoint, repeat-certainty, additivity, menu, or readout condition used to select a value must be explicit"
source_of_blocker_text: design_note_2026-09-13
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "feed the antiparallel-pair soldering split and the recorded affinity decision point to the clock-and-rate block; extend the census to mixed and larger alphabets and to menus supplied by a second neighbour"
conditional_surface_status: "all supports, actions, alphabets and weight families are supplied finite model content; no axiom selection follows; the affinity clause and the menu-supplier clause (own value, second neighbour, or lattice axis) are recorded as separating decision points, not adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every statement is an exact finite computation (rational rotation matrices, complete enumerations over the 24-element proper cubic group, exact polynomial identities and integrals in Fractions) on declared configurations, alphabets and weight families; nothing is asserted beyond them"
```

## Premises and declared objects

Rotations are exact rational 3x3 matrices: the proper cubic group O (the 24
signed permutation matrices of determinant +1) and rational SO(3) elements
outside O built from Pythagorean data (the 3-4-5 rotation about z, the
Rodrigues rotation R_q about a rational unit q with cosine 3/5, and
180-degree turns 2 n n^T / (n.n) - I about arbitrary nonzero rational n).
The analytic domain is the full real unit sphere, with full SO(3) internal action. The runner uses rational unit witnesses; the 8-, 12- and 24-point alphabets are normalized integer directions, whose coordinates need not be rational. Their dot products and quartic invariants are evaluated without square roots using common squared norms. Haar measure refers to the full sphere, not to its countable rational subset. A neighbour configuration
is a map from lattice positions to recorded values; the soldered action
moves positions and values with one rotation, the unsoldered action moves
positions with a lattice rotation and values with an independent internal
rotation. Antipodal-menu weight laws are exact polynomials f(t) in t = p.q
with Fraction coefficients: Born (1 + t)/2, the cubic witness (1 + t^3)/2,
the monotone witness (1 + t)/2 + t(1 - t^2)/8. Haar-uniform relative
orientation is t uniform on [-1, 1] with density dt/2, integrated exactly.
Finite soldered alphabets are the cube orbits of sizes 6, 8, 12, 24. All of
these are supplied model content; the axioms enter through the design
note's brief, and no axiom sentence is re-derived here.

## Prior art and what is new

- `docs/ADMISSIBILITY_RULE_MENUS_NEIGHBOUR_GENERATED_SUPPORTS_UNSOLDERED_AND_CUBE_ORBIT_MENUS_SOLDERED_BOUNDED_THEOREM_NOTE_2026-09-15.md`
  (open PR 8152, branch
  `physics-loop/admissibility-induced-law-block18-menus-neighbour-generated-supports-cube-orbits-20260915`):
  finite SO(2)_q-invariant sets inside {q, -q} (M1), the two-neighbour
  reduction with trivial stabiliser for non-collinear pairs (M2), cube-orbit
  menus and stabilisers (M3), alphabet and copy-probability findings
  (M4, M5). That note leaves the collinear and antiparallel pairs, triples,
  and any f beyond the Born form open; this note is that census.
- `docs/ADMISSIBILITY_RULE_FRAME_ATTACHED_FOUR_POINT_MENU_COVARIANT_WEIGHTS_GIBBS_LINEAR_FAMILY_AND_SEQUENTIAL_SUPPORT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-09-16.md`
  (open PR 8169): the four-point menu is covariant while distinct (T1), the
  bisector exchange leaves copy and flip masses free at t = 0 (T2), the
  four-point overlap fails the variation sentence (T4). New here: the
  rotational slot-exchange census on positions, the position-blindness of
  unsoldered weights under that exchange, and the value-attached antipodal
  menu's breakage exhibited against the surviving four-point menu.
- `docs/POSSIBILITY_SYMMETRIC_SEQUENTIAL_FORMATION_THAT_VARIES_HAS_ORDER_DEPENDENT_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-15.md`
  (open PR 8137): order dependence of sequential formation, independent of
  soldering; context for what this note does not touch.
- Landed repeat-certainty note (2026-07-11): repeat certainty selects the
  coefficient inside a covariant effect class and is not derived from Record
  permanence. Replayed here on the antipodal weight class, isolating the
  anti-Born flip as the configuration removed by the same-label wording.
- Landed Born-price note (2026-09-05): the four-outcome menu forces
  homogeneity and then the Born form with the sign left open. New here: on
  the two-point menu the sign is bought by same-label repeat certainty and
  by nothing else among the stated conditions.
- Landed composition note (2026-09-13): graded zeros for order-blind product
  rules. New here: the product rule on the antipodal menu is a graded zero
  at both menu points for every endpoint law, while the symmetrised sum
  rule returns the fair coin.
- B1 possibility-covariance note (2026-09-14): the soldering fork and the
  fourth-moment invariant. New here: that invariant separates each finite
  soldered menu from the continuum and carries a modulus across 24-point
  orbits. A5 support-rules note (2026-09-14): census method and layout.

What is new in one line: the stabiliser-degenerate two- and three-neighbour
census with the soldered/unsoldered split on the antiparallel pair, the
affine reduction with its selection accounting, two non-affine witnesses
passing every other stated condition, the separating and blind moments, and
the double-counted six-axis free-parameter census.

## Exact target and obligation graph

The design note's brief for this block, quoted: "Study covariant supports
for one, two, and three supplied neighbours under a specified action,
including stabilizer-degenerate cases." and "Test whether covariance and a
precisely formulated exchange condition restrict normalized antipodal-menu
weights f(p.q). Affinity alone leaves a coefficient in f(t) = (1 + c t)/2
and does not select the Born value. Any endpoint, repeat-certainty,
additivity, menu, or readout condition used to select a value must be
explicit. A non-affine example or an unresolved classification is a valid
scoped outcome; a new axiom is not automatically necessary."

Obligations discharged: the support census including the degenerate
antiparallel and parallel pairs and triples (Theorems 1, 2); the weight
restriction with every selecting condition named (Theorem 3); explicit
non-affine examples with the separating statistics (Theorem 4); the
soldered-alphabet comparison (Theorem 5). The affinity clause and the
menu-supplier clause are recorded as decision points below; neither is
adopted, and no new axiom is proposed.

## Theorem 1 — Stabiliser-degenerate covariant supports

On the declared configurations, under both actions, with every claim
exhibited by an exact stabiliser element or an exact obstruction:

- (a) With no recorded neighbour, the unsoldered reading admits no finite
  nonempty covariant menu: SO(3) acts transitively on the sphere, so any invariant set containing one point contains them all. The runner supplies finite witnesses moving four cube-orbit menus; these examples are not the general proof. The
  soldered reading admits the cube-orbit menus of sizes 6, 8, 12, 24 with
  stabilisers of orders 4, 3, 2, 1.
- (b) With one recorded neighbour q, the latitude circles at
  t_n = (n^2 - 1)/(n^2 + 1) are pairwise disjoint invariant sets with
  strictly decreasing positive transverse radius 2n/(n^2+1), tending to zero as n tends to infinity. Thus the infinite family has no least positive radius; the finite sample n=1,...,8 does have a minimum. Disjoint circles are not ordered by inclusion. Every point outside {q,-q} has an entire nontrivial circle as its SO(2)_q orbit, so a finite invariant menu lies inside {q,-q}. The 25 computed orbit points are only a finite control.
- (c) The antiparallel ordered pair {+z: q, -z: -q}: unsoldered, the fixer
  (RX180, rot180(u)) with u orthogonal to q flips q, forcing
  w(q) = w(-q) = 1/2 for every rational unit q (perpendicular partner
  constructed as u = rot180(e_z + q) e_x for q distinct from -e_z, and
  u = e_x for q = -e_z); the pair (I, R_q) also fixes the configuration, so
  the stabiliser exceeds the flip Z2. Soldered, exactly four cubic
  rotations invert e_z (the 180-degree turns about x, y, (1,1,0),
  (1,-1,0)), and the fair coin is forced precisely when q is orthogonal to
  one of those axes, that is on q_x q_y (q_x^2 - q_y^2) = 0; on the sampled
  family Q_XZ and Q_DIAG are forced, Q_XY and Q_GEN have the identity
  stabiliser alone. The product composition rule places mass
  f(1) f(-1) = 0 at both menu points for every endpoint law (a graded zero,
  matching the composition note), while the symmetrised sum rule returns
  the fair coin.
- (d) The parallel pair {+z: q, -z: q} is fixed by (RX180, I) and (I, R_q)
  and by no value-flipping pair among the exhibited candidates: nothing
  beyond the one-neighbour constraint is forced.
- (e) Triples: the cross product is equivariant under all sampled
  rotations; two non-collinear values fixed pointwise force the identity: their cross product supplies a third independent fixed vector. This argument alone does not classify configuration stabilisers that may permute the recorded values. The antiparallel pair with an orthogonal third neighbour
  keeps the flip fixer, so the fair coin on {q, -q} survives; with the
  non-orthogonal third P35 = (3/5) q + (4/5) u the lattice part is forced
  to RX180 and the internal part would need r u = (3/2) q + u of squared
  norm 13/4, so no q-flipping fixer exists. A fixer preserving the uniquely located third value and the two z slots pointwise fixes two non-collinear values internally and two position axes, hence is the identity. The
  soldered own-axis triple {x: x, y: y, z: z} has stabiliser C3 and one
  free parameter on the six-axis alphabet.

The rotation with cosine 3/5 has infinite order: if its nontrivial eigenvalue z were a root of unity, z+z^-1=6/5 would be a rational algebraic integer, hence an integer, a contradiction. The finite power check does not prove this by itself.

## Theorem 2 — Six-axis free-parameter census, twice

Under the soldered action on the six-axis alphabet, with free parameters
counted per configuration orbit as (number of stabiliser orbits on the
alphabet) - 1: one neighbour gives 9 (orbits of sizes 6, 6, 24 with
contributions 2, 2, 5); opposite-position pairs give 24 over 9 orbits, the
antiparallel aligned pair contributing 1 at stabiliser order 8 with the
coin forced, the parallel aligned pair 2 at stabiliser order 4 with no
forced coin; adjacent pairs give 87 over 21 orbits. An independent count,
the number of orbits on (configuration, value) pairs minus the number of
configuration orbits, agrees on all three totals.

## Theorem 3 — The antipodal weight class and its selections

Covariance identifies every ordered pair at equal p.q under an explicit
real rotation (with a rational witness at t = 3/5), so a covariant antipodal weight law is a single function
f(t). Slot exchange between neighbour positions is realised inside the
proper cubic group for every ordered pair of distinct positions (four
swappers for opposite pairs, one for adjacent pairs); unsoldered, the
bisector swap makes weights position-blind and breaks the value-attached
antipodal menu while the four-point menu survives; soldered, the swap
rotates values, so exchange is a separate condition rather than a
consequence. Affinity in the neighbour state plus covariance leaves
f(t) = (1 + c t)/2 with one constant (the kernel of R_q - I is the line
through q); normalisation and positivity bound the coefficient to
[-1, 1]; same-label repeat certainty f(1) = 1 selects c = 1 alone, and the
anti-Born flip c = -1 is certain for the flipped label. Which f-values are
ever probed is decided by the menu supplier: one unsoldered neighbour
supplies {q, -q} and probes f at the endpoints alone; a second neighbour
supplies the four-point menu; soldering supplies lattice-axis menus. The
affinity clause and this menu-supplier clause are the recorded decision
points of the block.

## Theorem 4 — Two non-affine witnesses and the moment ledger

The cubic law (1 + t^3)/2 and the monotone law (1 + t)/2 + t(1 - t^2)/8
satisfy normalisation as a polynomial identity, positivity by exact
monotonicity (derivatives 3 t^2 / 2 and (5 - 3 t^2)/8, the latter with
minimum 1/4 on the interval), and both endpoint conditions f(-1) = 0,
f(1) = 1; affinity fails at the midpoint of t = 1 and t = 0 (values 9/16
and 51/64 against the affine 3/4). The class of admissible laws is convex.
Under Haar-uniform relative orientation the first record moment E[s.q]
takes 1/3, 1/5, 11/30 on Born, cubic, monotone, 4/15 on the midpoint
mixture, c/3 on the affine family, and 1/2 on the step law; the second
moment is 1/3 for every normalised f; the third moment takes 1/5, 1/7,
3/14. The candidate laws pass every stated condition except affinity and
are separated by odd moments that a second-moment protocol cannot see.

## Theorem 5 — Soldered alphabets against the continuum

The six-axis, 8-point and 12-point menus restrict t = p.q to {0, +-1},
{+-1/3, +-1} and {0, +-1/2, +-1}. The invariant p_x^4 + p_y^4 + p_z^4
takes the constant values 1, 1/3, 1/2 on those orbits against the Haar
mean 3/5, separating each finite soldered menu from the continuum, and
distinguishes 24-point orbits from one another (1/2 on the orbit of
(1,2,3), 13/21 on the orbit of (1,2,4)), so the 24-point family carries a
modulus.

## No-Go Discipline Gate

The negative content is scoped: the soldered antiparallel pair does not
force the fair coin off the family q_x q_y (q_x^2 - q_y^2) = 0, and the
stated conditions short of affinity do not restrict f to the affine class.

- **N1 alternative routes.** Additivity across richer menus, readout and
  scale-reading constructions, frame-function conditions of Gleason type,
  composition with more neighbours, and differently formulated exchange
  sentences are unclassified and may select more.
- **N2 wall independence.** Everything here is finite group theory and
  exact polynomial algebra; no dynamics, clock, spectral or formation-order
  input enters.
- **N3 hidden walls.** All supports, actions, alphabets and weight families
  are supplied. The soldered forcing criterion is verified on a five-point
  rational sample plus the complete four-element inverter census inside O;
  the unsoldered every-q statement is constructive, not sampled.
- **N4 residual matching.** The residual toward the Born value is exactly
  the affinity clause plus same-label repeat certainty, matching the
  Born-price note's account (form bought, sign left) with the sign here
  bought by the same-label wording on the two-point menu.
- **N5 rhetoric audit.** "Forces" is used where an exhibited stabiliser
  element does the forcing; "splits" names an exact membership disagreement
  between the two readings; no closure language is used.
- **N6 partial-closure paths.** Absent repeat certainty the affine family
  remains a one-parameter class; the non-affine class is nonempty and
  convex. Promotion routes stay open.
- **N7 steelman.** Against the split: the worry that slot symmetry was
  smuggled in is answered by the unsoldered fixer being a genuine
  configuration stabiliser with no exchange input. For Born: within the
  affine family Born maximises E[s.q] at c = 1, but in the full normalised
  class the step law reaches 1/2, so the maximiser reading fails there and
  the statistic does not single Born out.
- **N8 cross-cycle echo.** No earlier cycle claimed the antiparallel-pair
  forcing or its soldered split; the repeat-certainty and Born-price
  selections echoed here are cited, not re-derived.

## Falsifiers

- A rational pair (lattice, internal) fixing the parallel configuration
  {+z: q, -z: q} while sending q to -q, for a sampled q, falsifies
  Theorem 1(d).
- A proper cubic rotation inverting e_z outside the four listed turns, or a
  soldered fixer flipping Q_XY or Q_GEN in the antiparallel configuration,
  falsifies Theorem 1(c).
- A normalised positive affine law with f(1) = 1 and c distinct from 1
  falsifies the selection accounting of Theorem 3.
- An exact evaluation with E[(s.q)^2] depending on the normalised law, or
  disagreeing with 1/3, falsifies Theorem 4.
- A recomputation of any listed t-set or fourth-moment value, or a
  disagreement between the two census methods on any family, falsifies
  Theorems 2 and 5.

## Boundaries and non-claims

No axiom is selected, changed or proposed; no physical Born rule is
derived; no all-axiom model is built. The affinity clause and the
menu-supplier clause are recorded as separating decision points for the
campaign ledger, not adopted. Every-q statements quantify over rational
unit vectors, with the constructive perpendicular partner for q distinct
from -e_z and the direct partner e_x at q = -e_z. The census covers the
six-axis alphabet under the soldered action; mixed and larger alphabets
and menus supplied by a second neighbour are future census families.
Formation order is out of scope here and lives in the order-dependence
note. Nothing here grades, unlocks or audits any other claim.

## Imports

Supplied representations (rational rotations, configurations, alphabets,
weight polynomials, the Haar density) and standard finite group and
polynomial machinery. The cited open notes are read as prior art with the
limited roles stated above; the cited landed notes carry their own scopes.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Original author review record (historical)

- **Seat:** one Fable 5.1 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) the free-parameter census computed by the
  orbit-stabiliser count and, independently, by counting orbits on
  (configuration, value) pairs, agreeing on all three families; (ii) the
  soldered forcing criterion computed by membership scan over O per sampled
  q against the polynomial criterion q_x q_y (q_x^2 - q_y^2) = 0, agreeing
  in both directions on the sample; (iii) hand-checked rationals against
  the runner's Fractions: 9/16 and 51/64 at the midpoint, 11/30 = 1/3 +
  4 eps / 15 at eps = 1/8, 4/15 for the midpoint mixture, 3/14 for the
  monotone third moment, 13/21 = 273/441 for the (1,2,4) orbit; (iv) the
  stabiliser orders 8, 4, 3 for the aligned pairs and own-axis triple
  cross-checked against the orbit-size products 3 x 8 = 6 x 4 = 24 and the
  cube-orbit table of the open menus note.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| improper rotations enter O | determinant filter `== 1` to `in (1, -1)` | caught (12 FAILs) |
| rot180 sign flipped | `- (1 if i == j else 0)` to `+ (...)` | caught (7 FAILs) |
| rodrigues cosine and sine swapped | `c=Fr(3,5), s=Fr(4,5)` to `c=Fr(4,5), s=Fr(3,5)` | missed; diagnosed non-defect |
| forces_fair_coin accepts identity | `mv(g, q) == neg(q)` to `mv(g, q) == q` | caught (2 FAILs) |
| census drops the normalisation -1 | `total += n - 1` to `total += n` | caught (3 FAILs) |
| pair count keeps orbit subtraction out | `npairs - len(...)` to `npairs` | caught (3 FAILs) |
| haar denominator off by one | `c / (k + 1)` to `c / (k + 2)` | caught (5 FAILs) |
| pneg_arg parity inverted | `k % 2 == 0` to `k % 2 == 1` | caught (3 FAILs) |
| Born linear coefficient halved | `1: Fr(1, 2)` to `1: Fr(1, 4)` | caught (5 FAILs) |
| cross product component negated | first component sign swapped | caught (2 FAILs) |
| quartic invariant degraded to squares | `** 4 ... ** 2` to `** 2 ... ** 1` | caught (2 FAILs) |

  The missed mutant is a genuine non-defect: any exact rational cosine and
  sine pair on the unit circle with cosine outside {0, +-1/2, +-1} yields a
  rotation about q of infinite order (Niven), and no check depends on the
  particular 3-4-5 choice. Ten of ten defect mutants are caught.
- **Vacuity guard:** every check compares computed exact values against
  stated targets; the two census methods use different algorithms and are
  compared both to each other and to stated totals; the blind-moment check
  verifies the value 1/3 rather than comparing witnesses to one another;
  the forcing criterion is checked in both directions across the sample.
- **Budget:** 42 checks, stdout 5972 characters (ceiling 6000), 0.4 s
  elapsed (ceiling 900 s), exact Fractions throughout, largest enumeration
  the 432-image adjacent-pair orbit scan; no dense state space enters.

## Verification

```bash
python3 scripts/menus_and_born_stabilizer_degenerate_supports_and_antipodal_weight_class_2026_09_22.py
```

Original runner summary before review fixes: `TOTAL: PASS=42 FAIL=0`; the runner exits nonzero if
any check fails. Cached output:
`logs/runner-cache/menus_and_born_stabilizer_degenerate_supports_and_antipodal_weight_class_2026_09_22.txt`.
