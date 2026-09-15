---
claim_id: admissibility_rule_formation_unit_clause_witness_sequential_formation_reproduces_the_joint_law_iff_no_site_records_an_inside_neighbour_with_a_second_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On finite units U of Z^3 with outside neighbours carrying fixed records (possibly none), the six-axis menu and the covariant positive product rule (p, q, r), executed at (3, 1, 2), under the records-only reading: (U1) a positive law on a finite set is determined by its one-site conditionals, so the joint law of a unit — the law whose one-site conditionals given all neighbours are the rule — is the Gibbs conditional and is unique (proved; executed); (U2) sequential formation of the unit along an order equals its joint law iff no site records an inside neighbour together with a second recorded neighbour, inside or outside (proved for every non-constant rule; executed on every order of a path, a domino, the plaquette and the star's classes, isolated and in environments); (U3) in isolation the star's sequential law equals its joint law iff at most one leaf precedes the center, so the star does not separate joint from sequential formation, while the isolated plaquette does under every order (executed); (U4) in a recorded environment every connected unit with at least two sites differs from its joint law under every order, since the last site records all its neighbours (proved; executed); (U5) the clause candidates are recorded and not adopted. No order, unit, rule or coupling is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
runner: scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py
---

# The formation-unit clause witness: sequential formation of a unit reproduces its joint law exactly when no site records an inside neighbour together with a second one — the isolated star does not separate the two readings, a recorded environment always does

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

The Admissibility axiom says "for each site". The derivation campaign asks
what changes if the unit that forms is not a site but a covariant set of
sites — a site and its six neighbours, say — and expected that the set's
joint law would differ from every one-at-a-time law. We define joint
formation for a classical rule in the only way the sentence allows: the
set's records are drawn from the one law under which every site's odds,
given all its neighbours, are the rule's. That law is unique. Then the
comparison has a clean answer. Forming the set one site at a time gives
exactly the joint law when, and only when, no site ever records an inside
neighbour together with any other neighbour. For an isolated star that
happens whenever the center forms first or second: the campaign's expected
witness fails there. For a square it never happens. And once the set sits
inside a field of records — which is the only situation a unit ever sees
after the first one — it never happens for any connected set of two or more
sites, because the last site to form sees all its neighbours. So "for each
site" and "for each set" are the same physics only for isolated tree-shaped
sets, and the whole-window set is the static reading.

Exactly: the criterion of U2; on the isolated star the total variations
between the sequential and joint laws are `0, 0, 1/72, 5/144, 505/10368,
575/10368, 103375/1492992` for `k = 0..6` leaves before the center; on the
isolated plaquette `455/31176` (path orders) and `37/1299` (diagonal-first);
the normalizer lemma
`K_k(b,…,b) − K_k(−b,b,…,b) = ((p−q)/Z_1)[(p/Z_1)^{k−1} − (q/Z_1)^{k−1}]`.
Executed with exact arithmetic: 18 checks, 12 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's formation-unit block (#8093, verdict table row 'Formation unit': to compute) — single-site formation against joint formation on a covariant set, with the clause candidates 'for each site' against 'for each admissible set of sites'"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the witness is exhibited exactly and the criterion for agreement is proved; the star does not separate the readings in isolation but every multi-site unit does in an environment; the clause decision is the owner's. Consumers: #8093's verdict table and assembly; block 14 (PR #8148, the rate clause) as the companion witness; the campaign's queue"
conditional_surface_status: "U1, U2, U4 proved for every non-constant rule; U3 and the environment executions at (3,1,2); conditional on the records-only reading, the six-axis menu, the product rule and the definition of joint formation as the rule-consistent law"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a telescoping ratio argument (U1); a one-site-conditional comparison with an exact normalizer lemma (U2); exhaustive enumeration of orders on small units (U3); a last-site argument (U4); every number an exact rational"
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable."

**Readings carried, named, nothing new adopted.** The records-only reading
and the sequential formation law of block 01
([`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)):
`r(a | ∅) = 1/M`, `r(a | A) = Π_{y∈A} K(v_y, a)/K_{|A|}(v_A)`, `K(b,a) = φ(a,b)/Z_1`,
`K_k(v_A) = Σ_s Π_{y∈A} K(v_y, s)`, `K_1 ≡ 1`; the census note's multiset key
([`ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`](ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md),
Lemma L). The six-axis menu, positivity, the product rule `(p, q, r)`,
`Z_1 = p + q + 4r`.

**Units and environments.** A unit is a finite `U ⊂ Z³`; `O = N(U) \ U` its
outside neighbours, carrying fixed records `v_O` (the *environment*); `v_O`
empty is the *isolated* unit. **Joint formation** of `U` given `v_O`: the
records of `U` are drawn from the law `μ_U^{joint}(· | v_O)` on `M^U` whose
one-site conditional at every `x ∈ U`, given all of `x`'s neighbours (inside
and outside), is the rule; by U1 it is
`Π_{edges inside U} φ · Π_{edges U–O} φ / Z_U(v_O)`. **Sequential formation**
along an order `σ` of `U`: `μ_σ(v_U | v_O) = Π_x r(v_x | v_{A_x})`,
`A_x = (N(x) ∩ O) ∪ {inside neighbours recorded before x}`.

**Units executed.** The star (a site and its six neighbours); the plaquette;
a domino; a path of three; a single site. Environments: none; all `+x`; a
fixed mixed configuration (seeded pseudo-random, printed by the runner).

## Prior art and what is new

Block 01 (on `main`) proved Theorem B (sequential equals static when every
record forms with at most one recorded neighbour) and the disagreement on
windows with a cycle, both for isolated windows; the census note named joint
formation on covariant sets as an owner decision; the unitary-tick notes of
2026-09-03/04 treat joint recording of commuting projectors, where sequential
and simultaneous recording agree by the projector chain rule. The uniqueness
of a positive law given its one-site conditionals is the Brook–Besag ratio
argument, re-proved here. Nothing on `main` (search recorded in
`ROUTE_PORTFOLIO.md`) defines joint formation for a classical rule or gives
the criterion.

New here: the definition and its uniqueness (U1); the iff criterion in an
environment (U2) with the exact normalizer lemma; the corrected star
witness (U3); the environment theorem (U4); the clause reading (U5).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| U1 uniqueness of a positive law given its conditionals; the joint law | proved; executed by reconstructing a random positive law on three sites (B1) |
| U2 the criterion, both directions | proved for every non-constant rule; the lemma executed symbolically and numerically; the criterion checked on every order of the path, the domino, the plaquette and the star's classes, isolated and in environments (B2, C1–C3) |
| U3 the star corrected; the plaquette | executed (D1–D2) |
| U4 environments: every connected multi-site unit differs under every order | proved; executed (E1–E2) |
| U5 the clause reading | recorded (the table) |
| covariant random units; units larger than executed; other menus | open; not this note |

## Theorem U1 — the joint law is well defined

**Statement.** A strictly positive probability law on `M^U` (`U` finite) is
determined by its one-site conditionals `μ(v_x | v_{U∖x})`, `x ∈ U`. Hence
there is exactly one positive law on `U` whose one-site conditionals given
all neighbours are the rule: `μ_U^{joint}(v | v_O) = Π_{edges inside U} φ(v_e) Π_{edges U–O} φ(v_e)/Z_U(v_O)`.

*Proof.* Fix a reference pattern `v*` and, for any `v`, change sites one at a
time from `v*` to `v` along `x_1, …, x_n`; `μ(v)/μ(v*) = Π_i μ(w^{(i)})/μ(w^{(i−1)})`
with `w^{(i)}` differing from `w^{(i−1)}` at `x_i` only, and each factor is a
ratio of one-site conditionals at `x_i`. So the conditionals fix all ratios,
and normalization fixes `μ`. The displayed law has the rule as its one-site
conditionals (the factors not containing `v_x` cancel), so it is that law. ∎
Executed: a pseudo-random positive law on three sites reconstructed exactly
from its conditionals (B1).

## Theorem U2 — the criterion

**Statement.** For every non-constant rule, every unit `U`, every environment
`v_O` and every order `σ`: `μ_σ(· | v_O) = μ_U^{joint}(· | v_O)` if and only if
no site `x ∈ U` records an inside neighbour together with a second recorded
neighbour, i.e. for every `x` with `A_x ∩ U ≠ ∅`, `|A_x| = 1`.

**Lemma (the normalizer depends on each recorded value).** For `k ≥ 2`,
`K_k(b, b, …, b) − K_k(−b, b, …, b) = ((p − q)/Z_1) [(p/Z_1)^{k−1} − (q/Z_1)^{k−1}]`,
nonzero iff `p ≠ q`; and for `c ⊥ b`,
`K_k(b, …, b) − K_k(c, b, …, b) = [(p − r)(p^{k−1} − r^{k−1}) + (q − r)(q^{k−1} − r^{k−1})]/Z_1^k`,
nonzero unless `p = q = r`. *Proof.* `K_k(a, b, …, b) = Σ_s K(a,s) K(b,s)^{k−1}`;
`K(b,s) − K(−b,s)` is `(p−q)/Z_1` at `s = b`, `(q−p)/Z_1` at `s = −b` and `0`
elsewhere; `K(b,s) − K(c,s)` is `(p−r)/Z_1, (q−r)/Z_1, (r−p)/Z_1, (r−q)/Z_1, 0, 0`
at `s = b, −b, c, −c, ±(b×c)`. ∎

*Proof of U2.* (⇐) Multiply the factors: every edge of `U` and every `U–O`
edge contributes one `K`, at the later endpoint; the normalizers
`K_{|A_x|}(v_{A_x})` are `K_1 = 1` when `|A_x| = 1` and functions of `v_O`
alone when `A_x ⊂ O`. So `μ_σ = Π_edges K · c(v_O)`, which is the joint law by
normalization. (⇒) Suppose some `w` has `y ∈ A_w ∩ U` and `|A_w| ≥ 2`. The
sequential law's one-site conditional at `y` is proportional to
`Π_{z∈N(y)} K(v_z, v_y) · Π_{w' : y ∈ A_{w'}} 1/K_{|A_{w'}|}(v_{A_{w'}})`
(the factors of `μ_σ` containing `v_y`), while the joint law's is
proportional to the first product alone. Take the pattern in which every
value in every `A_{w'}` with `y ∈ A_{w'}` equals `b`, and compare `v_y = b`
with `v_y = −b` (or `c ⊥ b` when `p = q`): by the Lemma each normalizer
`K_{|A_{w'}|}(v_y, b, …, b)` is strictly larger at `v_y = b` (the differences
above are positive for `p ≠ q` — both factors have the sign of `p − q` — and
in the orthogonal case unless `p = q = r`), so the ratio of the two
conditionals at `v_y = b` and `v_y = −b` differs from the joint law's ratio,
and by U1 the laws differ. ∎ Executed: the Lemma symbolically in `(p, q, r)`
and numerically at `(3,1,2)` for `k = 2..6` (B2); the criterion against exact
equality on every order of the isolated path and domino, the plaquette, the
star's seven classes (C1), and on every order of the domino and the path in
an environment and three orders of the star in two environments (C2–C3).

## Theorem U3 — the star does not separate the readings in isolation; the plaquette does

**Statement.** For the isolated star, `μ_σ = μ^{joint}` iff at most one leaf
precedes the center (the center then records at most one neighbour and every
later leaf records only the center); the seven classes by the number `k` of
leaves before the center give total variations
`0, 0, 1/72, 5/144, 505/10368, 575/10368, 103375/1492992` at `(3,1,2)`. For the
isolated plaquette every order differs from the joint (static) law:
`455/31176` for the sixteen path orders and `37/1299` for the eight
diagonal-first orders; and no convex combination of the order laws equals it
(the class ratios to `Π K` are strictly increasing in the diagonal
normalizer, as in the plaquette argument of PR #8148, re-executed here).

*Proof.* U2 with the star's recorded sets (`A_center` = the leaves before it;
`A_leaf` = `{center}` or `∅`); the plaquette's last site records both its
neighbours in every order. ∎ (D1–D2.)

## Theorem U4 — in a recorded environment every multi-site unit separates the readings

**Statement.** Let `U` be connected with `|U| ≥ 2` and let every outside
neighbour of `U` be recorded. Then for every order, `μ_σ ≠ μ^{joint}`.

*Proof.* The last site `x` of the order has all six neighbours recorded
(`A_x = N(x)`), and at least one of them lies in `U` since `U` is connected
with two or more sites; so `x` records an inside neighbour together with five
others, and U2 applies. ∎ Executed: the star (center-first, leaves-first and
one-leaf-first in the all-`+x` and the mixed environment), the domino and the
path (every order) in the mixed environment — all differ, all violate the
criterion; a single site agrees (E1–E2).

*Reading.* Inside a growing field of records, a unit larger than a site never
forms "as if one at a time": the last of its sites sees the whole
neighbourhood, and the rule applied to that site alone cannot reproduce the
joint odds. The isolated tree is the only place where the two readings
coincide — the same place where the formation law meets the static law
(block 01, Theorem B; the seeded rate law of PR #8148).

## The clause candidates (recorded, not adopted)

| candidate | what this note says about it |
|---|---|
| keep "for each site" (the site is the unit) | the sequential reading: block 01's formation laws, mixed over orders by whatever fixes the order (PR #8148) |
| "for each admissible set of sites" (a covariant set is the unit) | joint formation of the set; agrees with the sequential reading only on isolated tree-shaped sets with at most one recorded neighbour per site (U2, U3); in an environment never (U4); with the whole window as the set it is the static reading |

The decision is the owner's. This note selects none.

## No-Go Discipline Gate

The negative sentences are U2's "only if" and U4. Both are proved for every
non-constant rule.

### N1 — Routes by which a sequential law could still equal the joint law

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a cancellation among normalizers | several `K` factors compensating | the comparison at one site with all other recorded values equal to `b` isolates each factor's monotone dependence (the Lemma); no compensation | RULED OUT AT SCOPE |
| 2 the constant rule | `p = q = r` | every law is uniform | trivial |
| 3 a random covariant unit | units drawn at random | mixtures of sequential laws; on the plaquette outside the hull (U3); in an environment every member differs (U4) | narrowed |
| 4 clocks or orders chosen by the environment | any order | U4 holds for every order | RULED OUT AT SCOPE |
| 5 other menus | a menu on which some normalizer is constant in one argument | outside the six-axis menu; obligation named | not attempted |

### N2 — Wall-independence audit
Walls: the records-only reading, the product rule, positivity, the definition of joint formation as the rule-consistent law. Independent; each defines the object.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: none in the theorems.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 01 (main): Theorem B and the cycle disagreement | isolated windows | U2's isolated case; U3 | yes |
| the census note (main): Lemma L; joint formation named as an owner decision | the multiset key; the decision | the star's classes; the clause table | yes |
| PR #8148 (open; not an input) | the rate clause; the plaquette hull | the re-executed class ratios; the companion witness | context only |
| the unitary-tick notes (main) | commuting projectors | the contrast in Prior art | context only |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "sequential equals joint iff the criterion"; "in an environment never" | executed: the Lemma for `k = 2..6`; the reconstruction on three sites | executed: every pattern of each unit (`6^7` for the star) | executed: every order of the path, the domino, the plaquette; the star's seven classes; three star orders in two environments | executed: five units, three environments | proved for every non-constant rule (U2, U4); random units and other menus not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no unit; the definition of joint formation is the supplied object and is not adopted. No primitive is a wall.

### N7 — Steelman
Hostile reviewer: "You defined joint formation to be the static conditional, so of course sequential formation misses it." Reply: the definition is forced by the axiom sentence applied to every site of the set at once, and U1 shows it is the only such law; the content is the exact criterion, the corrected star, and the environment theorem, none of which is a definition. Conceded: covariant random units are not classified.

### N8 — Cross-cycle echo
Block 01's Theorem B, PR #8148's tree result and U2's "if" direction are one fact: the two readings meet exactly where every record sees one neighbour. No structurally similar wall was retired.

## Falsifiers
- A positive three-site law not recovered from its conditionals (B1); a `k ≤ 6` at which the Lemma's closed form fails (B2).
- An order on any executed unit where exact equality and the criterion disagree (C1–C3).
- A star class with `k ≤ 1` differing from the joint law or with `k ≥ 2` equal to it; a plaquette order equal to the static law; a class ratio not increasing in the diagonal normalizer (D1–D2).
- A connected multi-site unit in a full environment with an order reproducing the joint law, or a single site that does not (E1–E2).

## Boundaries and non-claims
This note defines joint formation for a classical rule, proves when sequential formation reproduces it, and exhibits the formation-unit witness; it does not classify covariant random units, does not treat menus other than the six-axis one, does not select an order, unit, rule or coupling as physical, and adopts no clause. No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 and the census note (both on `main`): proposed, unaudited; the parts used (Theorem B; Lemma L) are restated. PR #8148 (open) is referenced for context only.
- Re-proved at scope: U1 (the Brook–Besag ratio argument), U2, U4, the normalizer lemma.
- Reference only (named, not used): the projector chain rule of the unitary-tick notes.

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane and take it; no subagents). The control (`specs/supervisor_control_block15_formation_unit.py`) computed the star classes, the plaquette, the environments and the lemma before the contract; the lens pass is in `GOAL_block15.md`; the primary seat wrote U1–U5 and the runner; the refuting pass (`CHECKER_block15_findings.md`) recomputed the criterion by a second implementation that tracks recorded neighbours per site directly, the star's joint law by the tree factorization instead of the normalized product, and the environment star laws by an order-by-order recursion. Facts settled while executing: the campaign's expected star witness holds only with an environment (U3, U4) — the isolated star's center-first and one-leaf-first orders reproduce the joint law exactly, as Theorem B predicts; the star's environment executions were limited to three orders per environment to keep the runner near one minute (each star law is `6^7` patterns); the lemma's orthogonal form is needed only when `p = q`.

## Verification

```bash
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py --exact
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py --mutation star_separates_in_isolation_claimed
```

Families: A authority and inputs; B the uniqueness lemma and the normalizer lemma; C the criterion against exact equality on every executed order; D the star and the plaquette; E the environment theorem; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 12 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=18 FAIL=0`.
