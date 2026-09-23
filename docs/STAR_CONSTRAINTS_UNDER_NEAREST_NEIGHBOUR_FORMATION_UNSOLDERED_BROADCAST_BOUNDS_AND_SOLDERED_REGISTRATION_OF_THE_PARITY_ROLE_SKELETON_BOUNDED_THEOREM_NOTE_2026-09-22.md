---
claim_id: star_constraints_under_nearest_neighbour_formation_unsoldered_broadcast_bounds_and_soldered_registration_of_the_parity_role_skeleton_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading with the supplied unrecorded-site convention. Pair constraints are enforced in every order (the later site checks); star constraints (joint constraints on one site's neighbours) are not: under the unsoldered reading a site's neighbours formed after it with no other formed neighbour are identically distributed given its record, giving bounds 16/243 (role-letter link profile), 1/2 (Gauss parity with an odd vertex first), 5/16 (ice). Scalar role letters keep pair constraints yet complete non-skeleton states with no unrecorded site (share up to 7/8 on sampled cube orders; V-L-P on a path). Soldered axis-labelled role letters on the 2x2x2 cube: over all 40320 orders, completion is exactly (1/8)^(k-1) for k independent nucleations (histogram 8640/24480/5760/1440), conditional states are the 8 skeleton phases uniformly, connected growth always completes, and the uniform order law completes with probability 599/2048. No rule, reading, alphabet or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/star_constraints_under_nn_formation_broadcast_bounds_and_soldered_role_registration_2026_09_22.py
---

# Star constraints under nearest-neighbour formation: unsoldered broadcast bounds, and soldered registration of the parity-role skeleton

**Date:** 2026-09-22
**Type:** bounded_theorem
The results below concern explicitly supplied finite formation models.
Their parameters, alphabets, orders and sampling laws are conditions of the
calculation, not additional framework premises.

## Result up front

1. **Formation enforces pair constraints, not star constraints.** When a
   site forms it checks compatibility with each formed neighbour, so
   every pair constraint holds in every order, at the price of unrecorded
   sites. A star constraint (the six neighbours of one site jointly
   constrained) is different. If the centre forms first and each
   neighbour forms with the centre as its only formed neighbour, no site
   ever sees the whole star.

2. **Unsoldered broadcast bounds.** Under the unsoldered reading those
   neighbours get the same conditional whatever their direction, and the separate fresh-draw premise makes them
   independent and identically distributed given the centre's
   record. The parity skeleton's link profile (the two vertex letters on
   the link's axis, four plaquette letters across it) then holds with
   probability at most 16/243. Gauss parity with an odd vertex formed
   first holds with probability at most 1/2, and the ice count at most
   5/16. Isotropic stars, such as a vertex whose neighbours are all links,
   can always hold. Gauss parity is absorbed when the vertex forms last,
   and a soldered vertex can dictate one of the 32 consistent link sets.

3. **Scalar role letters form wrong skeletons without leaving a hole.**
   With unsoldered role letters V, L, P, C and pair constraints alone,
   formation completes states outside every skeleton phase with no
   unrecorded site: up to 7/8 of the completed mass on sampled cube
   orders. On a straight 3-site path with the ends formed first, the
   middle is recorded with probability 1/2, and half of those states are
   V-L-P along one axis, which no skeleton contains.

4. **Soldered role letters register the skeleton, and the order sets
   the defect price.** Give each site an axis-labelled letter (its parity
   vector: V, L_x, L_y, L_z, P_yz, P_xz, P_xy, C), rotating with
   positions, so that a site's letter fixes each neighbour's letter. On
   the 2x2x2 cube, over all 40320 orders:
   - the completion probability is exactly (1/8)^(k-1), where k is the
     number of independent nucleations (histogram 8640, 24480, 5760, 1440
     for k = 1..4);
   - conditional on completion, the state is one of the 8 skeleton
     phases, each with mass 1/8;
   - connected-growth orders always complete, and the phase is registered
     by the first site;
   - under the uniform order law the skeleton completes with probability
     599/2048.

   With the ends of a straight path formed first, the middle is recorded
   with probability 1/8.

5. **The construction is conditional.** The bounds concern independent
   broadcast draws. The eight parity labels and their directional update are
   an abstract alphabet, not a proved equivariant one-qubit encoding. The
   finite construction neither classifies other orders nor reduces the
   framework's physical decisions to these model choices.

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
conditional_surface_status: "formation reading; supplied unrecorded-site convention; supplied role letters (scalar and axis-labelled), windows and orders; no alphabet, reading or order law selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the broadcast bounds are short proofs with exact grid maxima; the cube results are exact computations over all 40320 orders (nucleation counts) and a sample covering every nucleation count (laws)"
```

## Premises and declared objects

The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the
sampling process studied here. Sequential draws use the declared conditional
law given the previously formed configuration, with fresh randomness at each
step; a chosen order is external to those draws. Correlated joint draws and
adaptive orders are separate models. Skipping a failed attempt and continuing,
or dropping its whole history, are supplied alternatives. Neither convention
follows from unreadability alone.


Use the supplied skip-and-continue convention described above. The parity-role
skeleton: the letter of site s in phase phi is the parity vector
(s + phi) mod 2, so eight phases; its weight is the scalar role (V = 0,
L = 1, P = 2, C = 3). Soldered letters are parity vectors that rotate
with positions; the soldered rule gives a nucleating site (no formed
neighbour) a uniform letter, and a site with formed neighbours the letter
each implies across its bond (flip the parity along the bond axis),
unrecorded if they disagree. Scalar letters are the weights with the pair
rule (adjacent weights differ by one), uniform over compatible weights.
Windows: the 2x2x2 cube with all 40320 orders, the 3-site path, and the
6-leaf star.

## Relation to earlier work

This packet states its supplied models and finite calculations directly.
Earlier campaign comparisons are historical motivation, not imported proof,
physical authority, or an adopted formation law.

## Theorem 1 — Pair constraints versus star constraints

A domain rule that admits only values compatible with every formed
neighbour enforces every pair constraint in every order: the later site
of each adjacent pair checks it, and is unrecorded when no value fits.
For a star constraint at a site c, take an order that forms c first and
then each neighbour of c while c is its only formed neighbour. Under the
unsoldered reading the neighbours' conditionals do not depend on
direction, and the stipulated fresh draws make the neighbours independent and identically distributed
given c's record. A star constraint that singles out some directions (an
anisotropic one) then holds with probability at most the largest mass
that a product distribution puts on it: 3 q^2 (1-q)^4 <= 16/243 for the
link profile, (1 - (1-2p)^6)/2 <= 1/2 for odd parity, and
20 p^3 (1-p)^3 <= 5/16 for the ice count. For the profile bound, differentiating 3q^2(1-q)^4 gives
6q(1-q)^3(1-3q), with maximum 16/243 at q=1/3. For odd parity,
(1-2p)^6 is nonnegative; for ice use p(1-p)<=1/4. These continuous
proofs cover [0,1]; the 13-point grid is only a finite control.

## Theorem 2 — Scalar letters and soldered letters on the cube

Scalar letters: pair constraints hold, and completed states outside
every skeleton phase occur with no unrecorded site; the largest
non-skeleton share on the sampled orders is 7/8. Soldered letters: a
nucleus's letter fixes its cluster's phase, and clusters meeting at a
site conflict unless their phases agree. So the completion probability
of an order with k nucleations is (1/8)^(k-1), and a completed state is
the common phase's skeleton, each phase with mass 1/8. This is verified
exactly on orders covering k = 1, 2, 3, 4, together with the full
nucleation histogram over all 40320 orders, which gives the uniform-law
completion 599/2048.

## Theorem 3 — The path: the phase price and the scalar failure

With the ends of a straight 3-site path formed first, soldered letters
leave the middle recorded exactly when the ends agree, with probability
1/8. With scalar letters (uniform weights) the middle is recorded with
probability 1/2, and in half of those cases the ends differ (V-L-P),
outside every skeleton.

## No-Go Discipline Gate

The negative scope is only the explicitly stated finite-model implication or
independent-clock bound. No general physical formation exclusion is claimed.

**N1 — Five distinct challenges.** Each is ATTEMPTED by the local argument
or the named finite computation, with its outcome kept explicit:

- **Identical independent broadcasts (ATTEMPTED):** the profile derivative, parity identity and p(1-p) bound prove the three continuous upper bounds.
- **Scalar pair checking (ATTEMPTED):** the sampled cube and path laws have completed non-skeleton states, so pair checks alone do not certify a skeleton.
- **Directional parity propagation (ATTEMPTED):** the supplied alphabet propagates one phase and gives the positive construction.
- **Multiple independent nuclei (ATTEMPTED):** agreement of k independent uniform phases gives 8^(1-k) on a connected finite graph.
- **Connected finite growth (ATTEMPTED):** one nucleus yields completion one; this is an explicit permitted route, not a general impossibility claim.

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

- A nearest-neighbour rule under the unsoldered reading exceeding a
  stated broadcast bound in the centre-first order falsifies Theorem 1.
- A sampled cube order whose soldered completion differs from
  (1/8)^(k-1), or whose completed states are not the uniform skeleton
  phases, falsifies Theorem 2.
- Any listed exact value (599/2048, 7/8, 1/8, 1/2, 1/4, histogram)
  failing its recomputation falsifies Theorems 2-3.

## Boundaries and non-claims

No rule, reading, alphabet or order law is adopted. The soldered letters
are an eight-letter alphabet; their admissibility as possibilities is the
recorded alphabet decision. The static reading's pinning (landed T2) is
not contested. No physical identification is made. Nothing here grades,
unlocks or audits any other claim.

## Imports

The landed roles and support-rule notes cited; supplied letters, rules,
windows and orders. No audit grade, no new axiom, no new primitive, no
new comparator and no new framing is imported.

## Author check record (original proposal)

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) the completion formula compared with
  exact finished-state computations on orders covering every nucleation
  count; (ii) the skeleton phases built independently from the parity
  definition and compared as a set; (iii) the Gauss star by complete
  enumeration of the 64 link patterns; (iv) the path results by complete
  enumeration of end letters.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| broadcast does not flip the bond axis | neighbour gets the same letter | caught (2 FAILs) |
| conflicting broadcasts accepted | disagreement not a hole | caught (2 FAILs) |
| nucleation letter law not uniform | skewed letter law | caught (2 FAILs) |
| nucleation count ignores formed neighbours | every site a nucleus | caught (crash) |
| scalar rule allows equal weights | pair rule loosened | caught after strengthening (1 FAIL; the 7/8 share is now pinned) |
| link profile exponent | q^2 (1-q)^3 | caught (1 FAIL) |
| skeleton phases built without the phase | phases collapse | caught (1 FAIL) |
| scalar middle ignores one end | one pair constraint dropped | caught (1 FAIL) |

  Eight of eight mutants are caught, one after the strengthening.
- **Vacuity guard:** every law comparison is between independently built
  objects; each bound is an exact grid maximum, with the maximiser named.
- **Budget:** 11 checks, stdout 2100 characters (ceiling 6000), 0.3 s
  (ceiling 900 s), exact Fractions.

## Landing review correction

Serial source review in one Codex session under the owner's no-subagent
instruction narrowed physical interpretations to supplied model conditions.
Original author check reports above are historical; they do not certify these
corrections. Current source-bound executions and independent controls are
recorded in the combined landing evidence. No independent audit is claimed.

## Verification

```bash
python3 scripts/star_constraints_under_nn_formation_broadcast_bounds_and_soldered_role_registration_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=11 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/star_constraints_under_nn_formation_broadcast_bounds_and_soldered_role_registration_2026_09_22.txt`.
