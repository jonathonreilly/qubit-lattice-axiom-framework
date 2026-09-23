---
claim_id: star_constraints_under_nearest_neighbour_formation_unsoldered_broadcast_bounds_and_soldered_registration_of_the_parity_role_skeleton_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading with the text's hole semantics. Pair constraints are enforced in every order (the later site checks); star constraints (joint constraints on one site's neighbours) are not: under the unsoldered reading a site's neighbours formed after it with no other formed neighbour are identically distributed given its record, giving bounds 16/243 (role-letter link profile), 1/2 (Gauss parity with an odd vertex first), 5/16 (ice). Scalar role letters keep pair constraints yet complete non-skeleton states with no unrecorded site (share up to 7/8 on sampled cube orders; V-L-P on a path). Soldered axis-labelled role letters on the 2x2x2 cube: over all 40320 orders, completion is exactly (1/8)^(k-1) for k independent nucleations (histogram 8640/24480/5760/1440), conditional states are the 8 skeleton phases uniformly, connected growth always completes, and the uniform order law completes with probability 599/2048. No rule, reading, alphabet or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/star_constraints_under_nn_formation_broadcast_bounds_and_soldered_role_registration_2026_09_22.py
---

# Star constraints under nearest-neighbour formation: unsoldered broadcast bounds, and soldered registration of the parity-role skeleton

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The assembly graph (open PR 8648) left
downstream gravity behind the roles decision: the superlattice
roles are supplied next-nearest data, a window extension, or a sector
clause. The landed roles note (2026-09-04, T2) shows statically that a
nearest-neighbour table over role letters pins the parity skeleton up to
its 8 translates. This block asks what formation needs in order to
register that skeleton as record content.

## Result up front

1. **Formation enforces pair constraints, not star constraints.** When a
   site forms it checks compatibility with each formed neighbour, so
   every pair constraint holds in every order, at the price of unrecorded
   sites. A star constraint (the six neighbours of one site jointly
   constrained) is different. If the centre forms first and each
   neighbour forms with the centre as its only formed neighbour, no site
   ever sees the whole star.

2. **Unsoldered broadcast bounds.** Under the unsoldered reading those
   neighbours get the same conditional whatever their direction, so they
   are independent and identically distributed given the centre's
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

5. **What moves in the decision structure.** Registering the roles by
   formation needs soldered, axis-labelled letters (the unsoldered bound
   16/243 and item 3 rule out scalar letters). It also needs an order law
   that nucleates once, or pays 7/8 per extra nucleus. The roles decision
   thus reduces to soldering, the order law, and an eight-letter
   alphabet. With locality being text (open PR 8646) and the clock
   reduced to the order law (open PRs 8663, 8664, 8666), the first
   assembly's account of gravity (clock, locality, roles, soldering)
   becomes, on the registered-roles route, soldering, the order law and
   the alphabet. The second-edition assembly (open PR 8648) computes
   gravity's minimal decision sets exactly. These bounds hold in the
   broadcast order; unsoldered orders that register a frame are not
   classified here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the assembly graph leaves gravity behind the roles decision; determine what nearest-neighbour formation needs to register the parity-role skeleton as record content"
source_of_blocker_text: assembly_graph_open_pr_8648
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "re-assemble with the roles decision reduced to soldering, the order law and the alphabet (done in open PR 8648); compute nucleation statistics of covariant order laws on larger windows"
conditional_surface_status: "formation reading; text hole semantics; supplied role letters (scalar and axis-labelled), windows and orders; no alphabet, reading or order law selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the broadcast bounds are short proofs with exact grid maxima; the cube results are exact computations over all 40320 orders (nucleation counts) and a sample covering every nucleation count (laws)"
```

## Premises and declared objects

Formation reading and hole semantics as in open PR 8666. The parity-role
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

## Prior art and what is new

- Landed roles note (2026-09-04): T2, a nearest-neighbour table over role
  letters pins the parity skeleton statically up to 8 translates; T3-T4,
  the pin field and the binary record alphabet need more. New here: the
  formation question. Static tables enforce every star constraint at
  once. Formation enforces only pair constraints unless the centre forms
  last or broadcasts, which under the unsoldered reading it cannot.
- Landed support-rule note: Gauss parity realised with the vertex formed
  after its links. New here: that is the checker-last case of a general
  statement, with the unsoldered bound 1/2 when the vertex forms first.
- Open ice-support PR 8667: the ice count's 5/16. New here: the general
  broadcast bound, and the same structure for the role skeleton.
- Open PRs 8663, 8664, 8666: order-blind formation and hole semantics.
  New here: registered content (the phase) and its nucleation price.

## Theorem 1 — Pair constraints versus star constraints

A domain rule that admits only values compatible with every formed
neighbour enforces every pair constraint in every order: the later site
of each adjacent pair checks it, and is unrecorded when no value fits.
For a star constraint at a site c, take an order that forms c first and
then each neighbour of c while c is its only formed neighbour. Under the
unsoldered reading the neighbours' conditionals do not depend on
direction, so the neighbours are independent and identically distributed
given c's record. A star constraint that singles out some directions (an
anisotropic one) then holds with probability at most the largest mass
that a product distribution puts on it: 3 q^2 (1-q)^4 <= 16/243 for the
link profile, (1 - (1-2p)^6)/2 <= 1/2 for odd parity, and
20 p^3 (1-p)^3 <= 5/16 for the ice count. Each maximum is checked exactly
on a 13-point grid.

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

The negative content is scoped: under the unsoldered reading, no
nearest-neighbour rule holds an anisotropic star constraint above the
stated bounds in the centre-first order, and scalar letters do not
register the skeleton.

- **N1 alternative routes.** Other order laws, larger windows, other
  alphabets (for example the pin field of the landed roles note) and the
  static reading are outside these theorems.
- **N2 wall independence.** Exact counting and exact grid maxima; no
  dynamics.
- **N3 hidden walls.** Role letters and their rules are supplied; the
  cube laws are verified on a sample covering every nucleation count, with
  the formula applied to the full histogram.
- **N4 residual matching.** The roles decision's residual is soldering,
  the order law and the eight-letter alphabet, matching recorded groups.
- **N5 rhetoric audit.** "Registers" names an exact conditional law with
  the phase fixed by the nucleus; bounds are exact.
- **N6 partial-closure paths.** Nucleation statistics of covariant order
  laws on large windows are open.
- **N7 steelman.** For scalar letters: the static reading pins the
  skeleton with them (landed T2). Against formation with them: item 3
  exhibits completed wrong skeletons with no hole. Both are recorded, and
  the separation is exact.
- **N8 cross-cycle echo.** The landed static roles results and the ice
  bound are cited, not re-derived.

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

## Review record

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

## Verification

```bash
python3 scripts/star_constraints_under_nn_formation_broadcast_bounds_and_soldered_role_registration_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=11 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/star_constraints_under_nn_formation_broadcast_bounds_and_soldered_role_registration_2026_09_22.txt`.
