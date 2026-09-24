---
claim_id: candidate_assembly_source_linked_graph_eleven_targets_minimal_decision_sets_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Eighteenth edition of the campaign's source-linked graph: 118 nodes (2 sources, 75 landed results cited by note path and verified on disk, 4 open results of the campaign's pull requests marked open, 12 decision groups with 40 recorded candidate clauses, 6 route choices, 8 routes, and the design note's 11 preserved targets), evaluated with AND semantics for results, routes and targets and OR semantics for choices. Verified: well-formedness, acyclicity with a negative control, source linking, the exact minimal decision sets of every target. Downstream gravity has exactly four minimal decision sets: {alphabet, order law}, {alphabet, reading}, {soldering, reading, roles}, {soldering, joint units, order law, roles}; every formation set holds the order law and every static set the reading. Every one contains a frame source, soldering or the coordinate-letter alphabet: the formation routes need one (PR 8676) and so does the static route (PR 8679), which also rests on a supplied Hamiltonian, an open edge. Single-site formation reaches the uniform ice measure beyond one top cell only with plan letters (PRs 8715, 8719; plans, PR 8686), which removes {soldering, order law, roles}; beyond rows exact joint formation needs units unbounded along an axis formed as a chain, so the joint-unit route needs an order law too (PR 8720). Without the layer order the sets return to the seventh edition's, without the plan letters as well to the sixth edition's five, and without the static frame source as well to the third edition's. With relational letters only, as under possibility covariance (fixed letters unavailable, no relational first formation, roles not registered), letters in alternating pairs record the role pattern under the static reading away from the side-4 torus (PR 8750) and four-angle cycles record it on the landed ice torus (PR 8752), which needs the static reading since under the sweep reading they record none (PR 8756), so gravity's sets are {alphabet, reading}, {soldering, reading, roles}, {soldering, joint units, order law, roles} and {alphabet, order law, roles, soldering}, and the one unsoldered set is {alphabet, reading}; with single-angle relational letters only (PR 8743) it is {alphabet, reading, roles}. That route needs no supplied octant: under the rotation-covariant rule that the Admissibility text asks for, cycle letters record their octant on the landed torus (PR 8854), strong cycle letters record the frame and the roles on every window (PR 8856), and strong letters are generic (PR 8857). The formed photon route reaches the uniform ice measure only through a coordinator (PR 8686; otherwise formed ice is directed, PR 8687), and the letters may be fixed or relational (PR 8691); a positive static rule selects the equal-time Coulomb law, so the supplied Hamiltonian is needed only for dynamics (PR 8698), and formed flux moves as a persistent walk (PR 8701); relational spirals are linearly rigid on the lattice and under the static reading but amplified by the sweep (PR 8717), and locally rigid under the static reading in the full nonlinear relations (PR 8724); the landed torus ice measure has no local formation order (PR 8727), linear ice sweep rules move flux by a linear transfer, damped when strictly positive and rigid for permutations, with mixed cases beyond both (PR 8726), seven relational letters carry the frame (PR 8729), no planar window of two to five squares admits a single-site order (PR 8735), nor any induced window of six squares (open PR 8993), under local formation multi-qubit units leave relational first formations a fair coin (PR 8731), under the static reading with its fixed octant relational frames with Sidon angles are globally rigid, carrying the frame but no role pattern (PR 8743), that rigidity needs a global octant, since site and line orientations leave the letters flexible (PR 8744), and layer units form uniform ice on infinite prisms in the zero-flux sector (PR 8740), whose flux sectors carry a Gaussian stiffness (PR 8746); these leave the minimal sets unchanged. Landed pull requests are cited as PR N. The ice-model lane joins record dynamics: results on the supplied ice model, landed as finite diagnostics and exact conditional identities (PRs 8859 and 8864, and the fourteen PRs 8869 to 8954 in narrowed form), and two open ones, an exact weighted identity for the cubic covariance with finite L = 16 diagnostics 0.29% above the continuous calibration (open PR 8968) the same diagnostics on L = 12 and L = 24 (open PR 8984), and their planar counterpart on square-ice tori, 4.3% to 4.7% above as on the strips (open PR 8985); one-vertex scalar invariants for one neutral statistic feed gravity (PR 8918). Uniform ice and the Gaussian comparisons are supplied models, and no Gaussian law, limiting stiffness or physical field is established. These leave the minimal sets unchanged. The first edition's locality group is withdrawn (Admissibility text) and the order-law group lists no order-blind rule. No completion percentage, no identification, no clause adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
  - formation_order_covariance_and_isotropic_binary_order_blind_classification_bounded_theorem_note_2026-09-13
  - admissibility_handed_rule_pseudoscalar_invariant_census_and_parity_odd_record_correlators_bounded_theorem_note_2026-09-13
  - admissibility_readability_continuum_alphabet_fisher_rank_and_formation_order_second_order_bounded_theorem_note_2026-09-13
  - composition_law_selection_graded_zeros_order_blind_rules_bounded_theorem_note_2026-09-13
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
  - covariant_effect_map_nonselection_and_repeat_certainty_collapse_bounded_theorem_note_2026-07-11
  - born_price_wordings_homogeneity_collinear_menus_four_outcome_fair_coin_2026_09_05
  - a_hierarchy_of_neighbourhood_conditions_glued_breakable_and_free_record_groups_under_shifting_ticks_bounded_theorem_note_2026-09-03
runner: scripts/candidate_assembly_source_linked_graph_minimal_decision_sets_2026_09_22.py
---

# Candidate assembly, eighteenth edition: the source-linked graph and its minimal decision sets

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** wave E (assembly) of the TOE derivation campaign by
underdetermination witnesses, re-assembled after the next-steps
continuation. The first edition of this pull request built a conjunctive
graph and reported gravity behind four decisions: clock, locality, roles,
soldering. The continuation found that locality is Admissibility text,
that the text excludes an order-blind rule under the unsoldered reading,
and that roles and the photon route each have more than one way to be
met. The second edition encoded those alternatives and computed minimal
decision sets exactly. The third edition added registered frames (open
PR 8676). Coordinate letters with an order law put the lattice frame in
the record, which gives soldering an alternative in both formation
routes. The fourth edition added the static route's frame source (open
PR 8679). Read statically, the landed uniform ice measure satisfies the
nearest-neighbour sentence only with vertex records that name
directions: soldered records, or coordinate letters. The fifth and sixth
editions record further results, which leave the minimal sets unchanged:
- the formed photon route reaches the uniform measure only through a
  coordinator (PR 8686);
- formed ice is otherwise directed (PR 8687);
- the letters may be fixed, or relational under possibility covariance
  (PR 8691);
- a positive static rule selects the equal-time Coulomb law, so the
  supplied Hamiltonian is needed only for dynamics (PR 8698);
- formed flux moves as a persistent walk, ballistic then diffusive (open
  PR 8701).

The seventh edition records two further results. Single-site formation
reaches the uniform ice measure beyond one top cell only with plan
letters (PRs 8715, 8719; plans, PR 8686). That removes
{soldering, order law, roles} from gravity's minimal sets. It also
records that relational spirals are linearly rigid on the lattice and
under the static reading but amplified by the sweep (PR 8717), and
that finite joint cell units reach rows but not blocks, in the plane and
in three dimensions (PR 8720).

The eighth edition draws the consequence of the unit result. Beyond rows,
exact joint formation needs units unbounded along an axis, formed as a
chain. That is a layer order, so the joint-unit route needs the order law
too. Every formation set of gravity then holds the order law, and every
static set the reading. It also records that the static spiral is
locally rigid in the full nonlinear relations (PR 8724).

The ninth edition records three more results without new decisions:
- the landed torus ice measure has no local formation order (open
  PR 8727);
- every linear ice sweep rule moves flux as a damped or rigid Markov walk
  (PR 8726);
- seven relational letters carry the frame (PR 8729).

The tenth edition records six more, again without new decisions:
- no planar window of two to five squares admits a single-site order,
  and every search stops at one square minus its shared corners (open
  PR 8735);
- under possibility covariance and local formation, multi-qubit units
  leave relational first formations a fair coin at every single-face
  attachment (PR 8731);
- under the static reading with its fixed octant, relational frames
  whose angles form a Sidon set are globally rigid: every static record
  is a spiral on its core (PR 8743);
- that rigidity needs a global octant: orienting each site or each lattice
  line leaves the letters flexible (PR 8744);
- layer units form the uniform ice measure exactly on infinite prisms of
  cross-section 2 x 2, in the zero-flux sector that long prisms select
  (PR 8740);
- the flux sectors of the layer transfer matrix cost close to c S^2 / A per
  layer on three cross-sections, with c between 0.28 and 0.41 over every
  flux sector and near 0.31 at the smallest flux on the two larger ones: a
  Gaussian flux stiffness (PR 8746).

The eleventh edition records three more, two of which change the
relational control:
- relational letters in alternating pairs record the role pattern under
  the static reading, with each site a function of its neighbours, on open
  boxes and on tori whose side the pair sums allow. On the side-4 torus
  the pair sums are forced to 180 degrees, and a site is fixed by its
  neighbours only up to its antipode (PR 8750);
- relational letters in four-angle cycles record it on the landed ice
  torus of side 4 as well, with each site a function of its neighbours
  (PR 8752);
- under the sweep reading, which reads back neighbours only, the cycle
  letters admit records that are not spirals and read no role pattern, so
  the route needs the static reading (PR 8756).

The twelfth edition records three more, which remove the supplied octant
from that route:
- under the rotation-covariant rule that the Admissibility text asks for,
  each site reads each line in either orientation, and the cycle letters
  record their own octant on the landed ice torus (PR 8854);
- strong cycle letters record the frame and the roles on every window
  under that rule; the orientation is recorded only where phase walks
  cannot turn (PR 8856);
- strong letters are generic: every obstruction is a nontrivial relation
  among the angles (PR 8857).

The thirteenth edition records what has landed and adds the ice-model
lane. Thirty-five of the cited pull requests have landed, so thirty-eight
nodes now link to their landed notes and thirteen stay open; landed pull
requests are cited as PR N. One landed note is sharper than its open
version: linear ice sweep rules move flux by a linear transfer, damped
when strictly positive and rigid for permutations, with mixed cases beyond
both (PR 8726). The ice-model lane joins record dynamics: row-transfer flux
costs on the square cross-section (PR 8859), the zero-flux layer chain's
gap (PR 8864), transfer spectra (PR 8869), Gaussian variance calibration
(PR 8871) and neutral defect insertions on prisms (PR 8875).

The fourteenth edition records ten more landings, among them the
first-edition inputs (PRs 8637, 8641 and 8646) and PRs 8859 and 8864, so ten
more nodes link to their landed notes and five stay open. It adds winding
samples on cubic tori (PR 8881) and tensor constraints with transverse
spectra (PR 8890) to the lane.

The fifteenth edition adds Gaussian layer-functional fits (PR 8896), a
flip-graph variational quotient for the supplied Hamiltonian (PR 8905) and
backtracking-worm balance (PR 8913) to the lane, and one-vertex scalar
invariants (PR 8918) to gravity. It updates the layer-unit,
photon-dynamics and record-statistic edges.

The sixteenth edition adds saturated layers (PR 8928), planar and cubic
calibration comparisons (PR 8930), flux-sector rates (PR 8949) and
charge-two and charge-four defect comparisons (PR 8951) to the lane, and
updates the continuum-bridge edge.

The seventeenth edition records that those fourteen results have landed in
narrowed form, together with the square-ice weighted identity (PR 8954).
In their landed form uniform ice and the Gaussian comparisons are supplied
models, and every numerical result is a finite diagnostic; no Gaussian
law, limiting stiffness or physical field is established. Each of the
fourteen nodes now links to its landed note under a name taken from its
landed title, the three open edges that cited them follow the landed
scopes, and the editions above describe the results by their landed
titles. Three open results join the lane:
- an exact weighted identity for the unit-arrow covariance on cubic tori,
  with finite L = 16 diagnostics: the smallest wavevectors imply a
  stiffness 0.29% above the continuous calibration, at 6.0 binned standard
  errors (open PR 8968);
- the same diagnostics on L = 12 and L = 24, at 0.44% and 0.31% (open PR
  8984);
- their planar counterpart: on square-ice tori of side 32 to 128 the
  smallest wavevectors sit 4.3% to 4.7% above the planar calibration, in
  the range the strips of PR 8930 record (open PR 8985).

The eighteenth edition adds that no induced window of six squares admits a
fixed single-site order (open PR 8993). The result joins the single-site
route, and that open edge narrows to planar windows beyond six squares.

In every edition the minimal sets are unchanged.

## Result up front

1. **The graph.** 118 nodes, each edge a cited result, a recorded
   decision, or a route choice:
   - 2 sources (the axioms, the primitives);
   - 75 landed results, cited by note path and verified on disk at this
     revision;
   - 4 open results of the campaign's pull requests, marked open;
   - 12 decision groups carrying 40 recorded candidate clauses. The
     soldering group lists the four actions of PR 8671; the
     alphabet group lists fixed and relational coordinate letters and
     plan letters; the unit group lists units unbounded along an axis;
   - 6 route choices and 8 routes. They include the two frame-source
     choices (formed and static), the letter-scheme choice (fixed or
     relational), the routes that read roles from static coordinate
     letters or from relational pair or cycle letters, single-site
     formation with an order law, and joint
     formation units;
   - the design note's 11 preserved targets, verbatim.

   Results, routes and targets need all of their inputs; a choice needs
   any one.

2. **Two first-edition entries are withdrawn.** The locality group goes:
   Admissibility reads "one fixed nearest-neighbor admissibility rule"
   (record-dynamics PR 8646, corrected). The order-law group, which
   replaces the clock group, no longer lists an order-blind physical
   rule; the text excludes one under the unsoldered reading (open PRs
   8663, 8664, 8666).

3. **Downstream gravity has exactly four minimal decision sets.**
   - {alphabet, order law}: the registered-frame route under formation
     (PR 8676). Coordinate letters in a sweep put the lattice frame
     in the record, and the ice support and role letters are read from
     the labels.
   - {alphabet, reading}: the same letters under the static reading (open
     PR 8679). The static frame rule is rigid, and it makes the uniform
     ice measure nearest-neighbour admissible with roles read from labels.
   - {soldering, reading, roles}: the static route with soldered vertex
     records and supplied roles.
   - {soldering, joint units, order law, roles}: formation by joint
     units. Finite cell units reach rows but not blocks, in the plane and
     in three dimensions (PR 8720). The units must be unbounded along
     an axis and formed as a chain, which is a layer order.

   The sixth edition's {soldering, order law, roles} is gone. With single
   sites, the uniform ice measure beyond one top cell needs plan letters
   (PRs 8715, 8719, 8735). With the alphabet group, that set is covered by
   {alphabet, order law}.

   So every formation set holds the order law, and every static set holds
   the reading. Every set also contains a frame source: soldering, or the coordinate-letter
   alphabet. Read statically, the landed ice measure in occupation form
   breaks the nearest-neighbour sentence, so the static route needs a
   frame source too. It still rests on the landed ice note's supplied
   quantum Hamiltonian for dynamics, which is an open edge; its equal-time
   law is selected by a positive static rule in the ice limit (open
   PR 8698). Controls recover the earlier editions:
   - removing the layer order restores the seventh edition's four sets;
   - removing the plan-letter requirement as well restores the sixth
     edition's five;
   - removing the static frame source as well restores the third
     edition's four;
   - removing the registered-frame route too restores the second
     edition's.

   A control keeps relational letters only, as under possibility
   covariance:
   - fixed letters are unavailable, and relational letters have no first
     formation (PRs 8691, 8731), so the letter scheme is empty;
   - registered roles need fixed parity letters. A single-angle static
     relational record carries no role pattern (PR 8743), but letters
     in alternating pairs record it away from the side-4 torus (open
     PR 8750), and four-angle cycles record it on that torus (open
     PR 8752).

   Gravity's sets then become {alphabet, reading},
   {soldering, reading, roles}, {soldering, joint units, order law, roles}
   and {alphabet, order law, roles, soldering}. The last of these keeps
   plan letters for single-site formation; the control does not remove
   them. The one unsoldered set is {alphabet, reading}: the static reading
   with its octant and relational pair or cycle letters, which carry both
   the frame and the roles. It is the set fixed letters need, and it does not depend
   on plan letters. With single-angle relational letters only (open
   PR 8743), the unsoldered set is the tenth edition's
   {alphabet, reading, roles}. The static reading here needs no supplied
   octant: under the rotation-covariant rule the cycle letters record
   their octant on the landed torus (PR 8854), strong cycle letters
   record the frame and the roles on every window (PR 8856), and
   strong letters are generic (PR 8857).

   The formed routes deliver the ice support. The landed uniform measure
   behind the Coulomb correlations also needs a coordinator (open
   PR 8686). Beyond one top cell, single-site formation needs plan letters
   (PRs 8715, 8719, 8735). Without them, formed ice is directed and its
   correlations are causal (PR 8687). Under possibility covariance
   the letters are relational spirals, available exactly in the sweep and
   under the static reading (PR 8691); under local formation,
   multi-qubit units leave their first formations a fair coin at every
   single-face attachment (PR 8731). They are linearly rigid on the
   lattice and under the static reading, but a sweep amplifies consistent
   boundary errors (PR 8717). Under the static reading they are
   locally rigid in the full nonlinear relations (PR 8724). With
   Sidon angles, such as the seven letters, and the reading's fixed
   octant, they are globally rigid: every static record is a spiral on its
   core. If each site, or each lattice line, may pick its own orientation,
   they are not (PRs 8743, 8744). A static
   spiral looks the same from every site, so it carries the frame but no
   role pattern. Roles read from static letters therefore use fixed
   coordinate letters; with relational letters alone, roles are supplied.
   The alphabet group still covers {alphabet, reading} through its
   fixed-letter candidate, so the minimal sets are unchanged.

4. **The other targets.**
   - Record dynamics: {reading, soldering}, {reading, alphabet},
     {soldering, joint units, order law}, or {alphabet, order law}.
   - Gauge: {roles}, {alphabet, order law}, or {alphabet, reading}.
   - Formation law: {rule, order law}; clock/rate: {order law}.
   - Menus, handedness, Born, readability, formation unit and matter keep
     their first-edition sets.

   No target is decision-free, and every decision group appears in some
   target's minimal sets.

5. **Declared open edges (7).**
   - Gravity: the record-statistic bridge to a curvature response, and a
     continuum bridge.
   - Record dynamics: photon dynamics on the landed supplied Hamiltonian
     (the equal-time law needs only a positive static rule, PR 8698),
     the defect densities of front-like order laws, and first-formation
     orders beyond corner growth, broadcast and the designed order (not
     classified; PR 8676), and exact formation of the uniform ice
     measure by layer units with an infinite cross-section, or by single
     sites on planar windows beyond six squares or three-dimensional
     windows beyond two cubes. Neither is searched. Finite cell units fail
     around blocks, and chains of units work (PR 8720). On prisms of
     cross-section 2 x 2, layer units are exact in the zero-flux sector
     (PR 8740). No planar window of
     two to five squares and no pair of adjacent cubes admits a
     single-site order (PRs 8715, 8719, 8735), nor does any induced
     window of six squares (open PR 8993). The static reading's
     nearest-neighbour admissibility of the ice measure is settled by open
     PR 8679.
   - Matter: the record/role bridge to physical fermions.

   No completion percentage is attached, and no physical identification
   follows from any label.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "build a source-linked graph from reviewed results with their exact premises and remaining obligations; preserve the original targets; an unproved bridge remains an open edge; do not attach a completion percentage or infer identification from a label"
source_of_blocker_text: design_note_2026-09-13
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "when the open pull requests land, flip their nodes to landed provenance and re-run; compute the frame-disagreement density under independent clocks and the defect densities of front-like order laws; search joint-unit formation of the uniform ice measure"
conditional_surface_status: "the graph is supplied structure assembled from cited results; AND/OR semantics is a stated modelling choice; decision groups are menus of recorded candidates, none adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every verified property is an exact finite computation (file existence, ledgers, a topological sort with a negative control, minimal-set closure under AND/OR) on the declared graph"
```

## Premises and declared objects

The graph is declared in full in the runner: node kinds (source, landed,
open, decision, choice, route, target) with provenance; directed edges;
candidate menus per decision group; open edges per target; the design
note's target list. Landed provenance is a docs/ path checked on disk;
open provenance names one of the campaign's open pull requests (8968,
8984, 8985 and 8993). Semantics: a decision
group's minimal set is itself; a choice takes the union of its inputs'
minimal families; every other node takes all pairwise unions of its
inputs' families. Families are kept minimal by removing supersets. Every
edge is a cited dependency; an edge that no cited result supports is not
drawn.

## Prior art and what is new

Every landed node is prior art, cited by path, including the binary
classification, the static roles note and the spin-half cubic-ice
Coulomb note. The open nodes are this campaign's results, cited by pull
request. New here: the graph with route choices, the frame-source
choice, and the exact minimal decision sets. The first edition's four-group account is
superseded, and the withdrawn entries are recorded with their sources.

## Theorem 1 — Well-formedness and source linking

The ledger is 2 + 75 + 4 + 12 + 6 + 8 + 11 = 118 nodes. Every edge
endpoint is declared. No edge enters a source or a decision group, and
edges leaving targets go to targets. Every landed path exists on disk.
Every open provenance names a campaign pull request, and the locality
group is absent. The 12 groups carry 40 candidates, at least 2 each, and
the order-law group lists no order-blind rule. The target list equals the
design note's.

## Theorem 2 — Acyclicity and minimal decision sets

A depth-first topological order covers all 118 nodes, and the same sorter
rejects a two-node cycle. The minimal decision sets are as stated in
items 3 and 4. They are computed by closure over the declared edges and
compared with independently written expected families. Every minimal set
of gravity contains soldering or the alphabet, and exactly one of the
order law and the reading. With the layer order removed, the closure
returns the seventh edition's sets; with the plan letters removed as
well, the sixth edition's five; with the static frame source removed as
well, the third edition's four.

## No-Go Discipline Gate

The negative content is scoped: under the declared graph and semantics,
no preserved target has an empty decision set.

- **N1 alternative routes.** Other first-formation orders, other units
  and other alphabets could add routes. The graph records the campaign's
  current account and lists the unclassified orders as an open edge.
- **N2 wall independence.** File existence, ledgers, sorts and closures.
- **N3 hidden walls.** AND/OR semantics is stated; route nodes are
  explicit. Supplied structure in the landed ice route is an open edge.
- **N4 residual matching.** Each target's residual is its minimal sets
  plus its open edges.
- **N5 rhetoric audit.** "Established route" names a route whose every
  edge is a cited result; no necessity of soldering is claimed.
- **N6 partial-closure paths.** Landing flips open nodes; owner decisions
  shrink the sets; the open edges are the named continuations.
- **N7 steelman.** For soldering: it registers the roles with 8 letters
  and completes in every connected order (PR 8669). Against it as a
  requirement: coordinate letters avoid it, under formation (open PR
  8676) and under the static reading (PR 8679), at the price of a
  320-letter alphabet. No recorded route avoids both. Both options are
  recorded.
- **N8 cross-cycle echo.** The first edition is superseded in place; its
  withdrawn entries and this edition's own correction are listed below.

## Falsifiers

- A missing landed path, a cycle, or a closure differing from the stated
  families under the declared graph falsifies Theorems 1-2.

## Boundaries and non-claims

The graph adds no status to any cited result and adopts no clause. Open
nodes carry open provenance until their pull requests land. AND/OR
semantics is a modelling choice, stated and implemented. Nothing here
grades, unlocks or audits any other claim.

## Imports

The cited notes with their own scopes; the design note's target list;
standard graph algorithms. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** first edition by one Fable 5.1 seat; second to eighteenth
  editions by one Opus 5.5 seat; no subagents.
- **Corrections before landing (2026-09-22).** (1) The first edition
  carried a locality decision group and a conjunctive four-group account
  of gravity. Locality is Admissibility text, and the order-blind
  candidate is excluded by the text under the unsoldered reading. This
  edition withdraws the group and adds route choices. (2) An earlier
  push of this edition kept a direct soldering edge into gravity, taken
  over from the first edition with no cited result behind it. That
  edition reported soldering in every minimal set of gravity. The edge
  is removed, and the static route {reading, roles} became visible as
  a set without soldering. (3) The third edition adds the registered-frame
  route of PR 8676. Gravity gains {alphabet, order law}, which
  replaces {soldering, order law, alphabet}. (4) The fourth edition adds
  the static route's frame source (PR 8679). {reading, roles} becomes
  {soldering, reading, roles}, and {alphabet, reading} appears. (5) The
  fifth edition records PRs 8686, 8687 and 8691 as result nodes and
  a letter-scheme choice; the minimal sets are unchanged. (6) The sixth
  edition records PRs 8698 and 8701, and narrows the supplied
  Hamiltonian's open edge to dynamics. (7) The seventh edition records
  PRs 8715, 8717, 8719 and 8720. Single-site formation needs plan
  letters for the uniform ice measure beyond one top cell, which removes
  {soldering, order law, roles} from gravity's sets. Spiral rigidity
  joins the relational letters, and joint cell units join the joint-unit
  route. (8) The eighth edition draws the consequence of PR 8720.
  Beyond rows, exact joint formation needs units unbounded along an axis,
  formed as a chain by an order law. {soldering, joint units, roles}
  becomes {soldering, joint units, order law, roles}. It also records
  PR 8724. (9) The ninth edition records PRs 8726, 8727 and
  8729; the minimal sets are unchanged. (10) The tenth edition records
  PRs 8731, 8735, 8743, 8744, 8740 and 8746. It narrows the single-site open
  edge to planar windows beyond five squares and three-dimensional windows
  beyond two cubes, and the layer-unit edge to infinite cross-sections;
  the minimal sets are unchanged. It adds a control with relational
  letters only, whose one unsoldered set is {alphabet, reading, roles}.
  (11) The eleventh edition records PRs 8750, 8752 and 8756: letters in
  alternating pairs record the role pattern away from the side-4 torus,
  and four-angle cycles record it on that torus, under the static reading
  only (the sweep reading records none). The relational control's
  unsoldered set becomes {alphabet, reading}, and a control with
  single-angle letters keeps {alphabet, reading, roles}. The main minimal
  sets are unchanged. (12) The twelfth edition records PRs 8854, 8856
  and 8857: the relational route needs no supplied octant, and strong
  letters are generic. The minimal sets are unchanged. (13) The thirteenth
  edition links the thirty-eight nodes whose pull requests have landed to
  their landed notes, restates the linear-transport result as the landed
  note has it, and adds the ice-model lane (PRs 8859 and 8864, since
  landed, and PRs 8869, 8871 and 8875, then open) as results feeding
  record dynamics. The minimal sets are unchanged. (14) The fourteenth
  edition links ten more landed nodes and adds PRs 8881 and 8890, then
  open, to the lane. The minimal sets are
  unchanged. (15) The fifteenth edition adds PRs 8896, 8905 and 8913, then
  open, to record dynamics and PR 8918 to gravity, and it updates the
  photon-dynamics, layer-unit and record-statistic edges. It also corrects
  the layer-unit edge, which still cited PRs 8715, 8719, 8720, 8735 and
  8740 as open after they had landed. The minimal sets are unchanged.
  (16) The sixteenth edition adds PRs 8928, 8930, 8949 and 8951, then
  open, to record dynamics and updates the continuum-bridge edge. The
  minimal sets are unchanged. (17) The seventeenth edition records the
  landing of those fourteen results in narrowed form, with PR 8954. It
  links each of their nodes to its landed note under a name taken from its
  landed title, restates the record-statistic, photon-dynamics, layer-unit
  and continuum-bridge edges and the edition texts in the landed wording,
  and renames the lane the ice-model lane. It adds open PRs 8968, 8984
  and 8985 to the lane. The minimal sets are unchanged. (18) The
  eighteenth edition adds open PR 8993, no order on any induced window of
  six squares, to the single-site route and narrows that open edge to
  windows beyond six squares. The minimal sets are unchanged.
- **Independence sources:** (i) landed provenance checked against the
  files at this revision; (ii) minimal sets computed by closure and
  compared with separately written expected families; (iii) the sorter
  exercised on the graph and on a cyclic control.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| OR choices evaluated as AND | choice branch disabled | caught |
| minimise keeps supersets | minimisation removed | caught |
| static route drops the reading | edge deleted | caught |
| registered roles lose the alphabet | edge deleted | caught |
| landed path corrupted | one-letter typo | caught |
| locality group restored | withdrawn group re-added | caught |
| order-blind candidate restored | excluded candidate re-added | caught |
| direct soldering edge into gravity restored | unsupported edge re-added | caught |
| cycle guard removed | seen test deleted | missed; diagnosed non-defect (the recursion fallback still rejects cycles) |
| registered-frame route loses the order law | edge deleted | caught |
| frame source loses soldering | edge deleted | caught |
| frame source read as AND | choice declared a route | caught |
| static frame source loses soldering | edge deleted | caught |
| roles from static letters lose the reading | edge deleted | caught |
| static route drops its frame source | edge deleted | caught |
| letter scheme read as AND | choice declared a route | caught |
| coordinator edge dropped | result edge deleted | caught |
| plan-letter edge dropped | decision edge deleted | caught |
| single-site route read as a choice | route declared a choice | caught |
| two-cube result edge dropped | result edge deleted | caught |
| spiral rigidity edge dropped | result edge deleted | caught |
| joint-unit result edge dropped | result edge deleted | caught |
| joint-unit route loses the unit decision | decision edge deleted | caught |
| layer-order edge dropped | decision edge deleted | caught |
| static spiral rigidity edge dropped | result edge deleted | caught |
| finite-letters edge dropped | result edge deleted | caught |
| torus edge dropped | result edge deleted | caught |
| linear-transport edge dropped | result edge deleted | caught |
| polyomino-window edge dropped | result edge deleted | caught |
| multi-qubit unit edge dropped | result edge deleted | caught |
| static global rigidity edge dropped | result edge deleted | caught |
| layer-unit edge dropped | result edge deleted | caught |
| control keeps the letter scheme | control edit removed | caught |
| control keeps roles read from letters | control edit weakened | caught |
| global-octant edge dropped | result edge deleted | caught |
| flux-stiffness edge dropped | result edge deleted | caught |
| pair-letter result edge dropped | result edge deleted | caught |
| cycle-letter result edge dropped | result edge deleted | caught |
| sweep result edge dropped | result edge deleted | caught |
| octant result edge dropped | result edge deleted | caught |
| folded-roles result edge dropped | result edge deleted | caught |
| generic-letters result edge dropped | result edge deleted | caught |
| pair-letter route without the reading | decision edge deleted | caught |
| single-angle control keeps the pair route | control edit removed | caught |
| third-edition control keeps the pair route | control edit weakened | caught |
| ice-model result edge dropped | result edge deleted | caught |
| ice-model result attached to the photon-route choice | result edge moved into a choice | caught |
| newly landed node left open | provenance kind reverted | caught |
| later ice-model result edge dropped | result edge deleted | caught |
| fifteenth-edition ice-model result edge dropped | result edge deleted | caught |
| seam result moved from gravity to record dynamics | result edge moved | caught |
| seam result attached to the photon-route choice | result edge moved into a choice | caught |
| sixteenth-edition ice-model result edge dropped | result edge deleted | caught |
| seventeenth-edition result edge dropped | result edge deleted | caught |
| landed ice-model node left open | provenance kind reverted | caught |
| open result attached to the photon-route choice | result edge moved into a choice | caught |
| planar torus result edge dropped | result edge deleted | caught |
| six-square window result edge dropped | result edge deleted | caught |

  Fifty-seven of fifty-seven defect mutants are caught; the cycle-guard mutant is the diagnosed non-defect.
- **Vacuity guard:** every family is compared with an independently
  written expected family; provenance is checked on disk.
- **Budget:** 22 checks, stdout 4143 characters (ceiling 6000; declared audit timeout 120 s),
  under a second; a 118-node graph.

## Verification

```bash
python3 scripts/candidate_assembly_source_linked_graph_minimal_decision_sets_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=22 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/candidate_assembly_source_linked_graph_minimal_decision_sets_2026_09_22.txt`.
