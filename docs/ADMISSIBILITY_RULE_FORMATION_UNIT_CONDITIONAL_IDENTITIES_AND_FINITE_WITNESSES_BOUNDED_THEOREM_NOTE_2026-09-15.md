---
claim_id: admissibility_rule_formation_unit_conditional_identities_and_finite_witnesses_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Positive-law uniqueness; exact repeated-value normalizer identities; sufficient sequential/joint agreement for arbitrary fixed exterior records when each site with an inside recorded neighbour has exactly one recorded neighbour; exact finite star, plaquette, domino and path witnesses at (3,1,2). Arbitrary fixed-environment necessity and universal exclusions are deferred."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
runner: scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py
---

# Formation-unit conditional identities, a sufficient agreement condition, and finite witnesses

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Joint formation is a supplied model convention: use the positive law whose one-site conditionals, given all neighbours, equal the product rule. The ratio argument below establishes uniqueness and the displayed edge product establishes existence. This convention is not forced by the axiom sentence.

For any fixed exterior records, sequential formation agrees with this joint law under the sufficient condition stated below. The original necessity proof changed exterior records while claiming to hold them fixed; it does not establish the arbitrary-environment converse. The inherited universal multi-site environment exclusion is therefore deferred.

The primary's isolated-star classes are `k = 0,1,2,3,6`, with exact total variations `0,0,1/72,5/144,103375/1492992`. The historical control also evaluated `k=4,5`, with values `505/10368,575/10368`; those are historical evidence, not additional current-primary domains. The plaquette's 24 orders give `455/31176` for 16 path orders and `37/1299` for 8 diagonal-first orders.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain the named identities and finite witnesses; broad negative certification remains deferred."
conditional_surface_status: "Conditional on the declared six-axis menu, positive product rule and records-only reading."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
The original complete arguments and execution histories are preserved in
[the recovery manifest](work_history/review_loop/pr8150/original-manifest.json).
This source repair does not claim a completed independent audit.

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

The linked finite-window classification supplies the sufficient at-most-one-neighbour condition and the census supplies the multiset key. The uniqueness proof is the Brook–Besag ratio argument, restated completely below. The added content is the arbitrary-fixed-boundary sufficient condition, the repeated-value normalizer formulas and the finite unit comparisons. The joint-law convention remains a modelling choice.

## Exact target and obligation graph

Positive-law uniqueness; exact repeated-value normalizer identities; sufficient sequential/joint agreement for arbitrary fixed exterior records when each site with an inside recorded neighbour has exactly one recorded neighbour; exact finite star, plaquette, domino and path witnesses at (3,1,2). Arbitrary fixed-environment necessity and universal exclusions are deferred.

Universal negative conclusions from the original version remain deferred; they are not consequences promoted by this landing surface.

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

## Theorem U2 — sufficient agreement and normalizer identities

**Sufficient condition.** For any fixed exterior configuration `v_O`, if every `x` with `A_x ∩ U ≠ ∅` has `|A_x|=1`, then `μ_σ(·|v_O)=μ_U^{joint}(·|v_O)`.

*Proof.* Multiply the sequential factors. Every inside edge and every edge from the unit to its exterior contributes one `K`. A normalizer with an inside recorded value is `K_1=1`; every other normalizer depends on `v_O` alone (including the empty-set constant). The product is therefore the joint edge product times a factor independent of `v_U`. Normalization proves equality. ∎

**Lemma (the normalizer depends on each recorded value).** For `k ≥ 2`,
`K_k(b, b, …, b) − K_k(−b, b, …, b) = ((p − q)/Z_1) [(p/Z_1)^{k−1} − (q/Z_1)^{k−1}]`,
nonzero iff `p ≠ q`; and for `c ⊥ b`,
`K_k(b, …, b) − K_k(c, b, …, b) = [(p − r)(p^{k−1} − r^{k−1}) + (q − r)(q^{k−1} − r^{k−1})]/Z_1^k`,
nonzero unless `p = q = r`. *Proof.* `K_k(a, b, …, b) = Σ_s K(a,s) K(b,s)^{k−1}`;
`K(b,s) − K(−b,s)` is `(p−q)/Z_1` at `s = b`, `(q−p)/Z_1` at `s = −b` and `0`
elsewhere; `K(b,s) − K(c,s)` is `(p−r)/Z_1, (q−r)/Z_1, (r−p)/Z_1, (r−q)/Z_1, 0, 0`
at `s = b, −b, c, −c, ±(b×c)`. ∎


The lemma compares repeated-value configurations. Its strict comparisons are available in isolation or when all fixed exterior values are the same `b`; they do not permit replacing an arbitrary fixed exterior configuration by `b`. The original necessity argument and its universal fixed-environment conclusion are deferred. The primary checks agreement with the sufficient-condition predicate on its listed finite examples; those examples are not a proof of necessity for arbitrary environments.

## Theorem U3 — finite star and plaquette witnesses

**Finite witnesses at `(3,1,2)`.** The primary evaluates isolated-star classes `k=0,1,2,3,6`, giving `0,0,1/72,5/144,103375/1492992` respectively. The sufficient condition proves agreement for `k=0,1`. Exact enumeration gives the other three distances. The isolated plaquette's 24 orders give the two positive distances stated above. The class ratios at the three diagonal types are also computed exactly. No universal convex-mixture exclusion is promoted here.

## Theorem U4 — finite environment witnesses

**Finite environment comparisons.** The primary evaluates two star orders (`k=0,6`) in the all-`+x` environment and three (`k=0,1,6`) in its fixed mixed environment. It evaluates all two domino orders and all six path orders in the fixed mixed environment. Each listed multi-site comparison has positive exact total variation. The single-site comparison agrees.

For any fixed exterior configuration, a one-site unit has the same sequential and joint law directly from their definitions. The original claim about every connected multi-site unit in every fixed environment relied on the unsupported converse and remains deferred. No claim that every unit after a first unit necessarily has a full recorded environment is made.

## The clause candidates (recorded, not adopted)

A supplied single-site sequential law and a supplied joint law on a specified unit are two mathematical constructions. The sufficient condition and finite comparisons describe their relation at the stated scope. Neither construction is selected by this note.

## No-Go Discipline Gate

### N1 — Deferred negative certification
The original route table mixes changes of scope and non-attempts with actual arguments; it does not establish five independent exact-target attack families. Broad negative certification is withheld. The original full proofs remain byte-exact in the recovery manifest, and the original branches remain recovery handles.

### N2 — Supplied model conditions
The finite menu, positive product rule, records-only reading and any stated clock or joint-law convention are supplied mathematical conditions. The original wall-independence assertion does not complete the negative gate.

### N3 — Hidden conditions
The displayed domains govern: fixed exterior records cannot be varied inside a proof about one fixed environment. Value-blind mixing and causal value-dependent scheduling are distinct constructions.

### N4 — Actual mathematical imports
The linked finite-window classification supplies the product law and its at-most-one-recorded-neighbour sufficient condition. The linked census supplies the recorded-set multiset reduction and the quoted rectangle value. These are conditional mathematical inputs; no broader parent conclusions are imported.

### N5 — Executed resolution
The primary runner states its exact finite domains in five resolution lines. Written identities beyond those domains are checked as arguments, not executed on the infinite lattice. Historical controls have their original domains and are not relabelled as current primary execution.

### N6 — Primitive boundary
No primitive selects a rate, unit, measure over orders or boundary condition. The supplied mathematical constructions do not adopt a framework clause.

### N7 — Remaining objection
Positive identities and finite witnesses do not themselves discharge the deferred universal negative certification. Arbitrary fixed-environment necessity additionally has an unresolved proof gap.

### N8 — Recovery
The original complete proofs, including deferred arguments, are recoverable from the manifest; this narrowing does not declare their mathematical negations.

## Falsifiers

A failed reconstruction of the positive three-site law; a failure of either displayed normalizer identity; a sequential/joint disagreement under the sufficient condition; or an incorrect exact distance on a listed executed unit would falsify the retained result. An arbitrary-environment example is not silently added to the executed domains.

## Boundaries and non-claims

This note proves conditional identities and a sufficient agreement condition and reports finite unit witnesses; arbitrary fixed-environment necessity and universal multi-site exclusions are deferred; no unit, order, rule or coupling is selected as physical, and no clause is adopted.

No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The menu, weights and formation conventions are declared mathematical inputs, not empirical or axiom-selected values.

## Imports

The linked axiom memo supplies only its quoted sentences. The linked finite-window classification and census supply the mathematical inputs identified above. The Brook–Besag positive-law ratio proof is restated, not used as unexplained authority. The triples, units, exterior configurations and order samples are declared model inputs.

## Review record

The original author controls, checker notes, proofs and outputs are preserved byte-exact in the recovery manifest. Their historical claims are not current review authority. This corrected draft awaits the original independent reviewer's affected-source confirmation and bounded final capture; no old output is restamped.

## Verification

```bash
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py --exact
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py --mutation star_separates_in_isolation_claimed
```

Families: A authority and inputs; B the uniqueness lemma and the normalizer lemma; C the criterion against exact equality on every executed order; D the star and the plaquette; E finite environment comparisons; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 12 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=18 FAIL=0`.
