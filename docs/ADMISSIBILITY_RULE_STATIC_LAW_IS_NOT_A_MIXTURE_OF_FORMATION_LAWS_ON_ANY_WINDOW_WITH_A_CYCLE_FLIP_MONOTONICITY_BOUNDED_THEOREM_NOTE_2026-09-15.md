---
claim_id: admissibility_rule_static_law_is_not_a_mixture_of_formation_laws_on_any_window_with_a_cycle_flip_monotonicity_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On every finite window of Z^3 with the six-axis menu and the covariant positive product rule (p, q, r), executed at (3, 1, 2), under the records-only reading: (X1) for every order, flipping one record of the constant pattern from b to -b (or to an orthogonal value when p = q) does not decrease the order's weight ratio mu_sigma / prod_edges K, and increases it strictly iff the flipped site lies in a recorded set of size at least two (proved; executed on every order-site pair of the plaquette and 2x3 and on every class-site pair of the cube); (X2) for every probability law on orders, the mixture of the sequential laws equals the static law iff the law charges only orders in which every site records at most one neighbour; on any window containing a cycle no order qualifies, so no mixture over orders — uniform, random-priority, any value-blind clock law, any convex combination — is the static law (proved for every non-constant rule; executed on the path, the star, 2x3 and the plaquette, reproducing the census note's uniform value); (X3) the same statement for a unit in a constant environment against its joint law, with the criterion of the formation-unit note (proved; executed); (X4) value-dependent order laws are the open boundary (the plaquette case is settled in the rate-clause note). No order, mixture, rule or coupling is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
runner: scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py
---

# The static law is not a mixture of formation laws on any window with a cycle: a one-record flip raises every order's weight, so a mixture over orders is the static law exactly when it charges only orders where every site records at most one neighbour

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Lay records down in some order and you get a pattern law that depends on
the order; average over orders with any weights you like — a uniform
shuffle, random priorities, clocks that fire faster near existing records —
and you get a mixture. Could some mixture be the static law the rest of the
repository uses? Two earlier notes said no on one square, using the
square's symmetries. Here is the reason that needs no symmetry at all. Take
the pattern in which every record is the same value, and flip one record to
its opposite. For every order, the flip can only raise the order's weight
relative to the static edge product, and it raises it strictly exactly when
the flipped site was among the recorded neighbours of some site that saw two
or more. A mixture that equals the static law must leave the ratio unchanged,
so every order it charges must have no site that records two neighbours. On
any window with a cycle there is no such order: the last corner of the cycle
to form always sees two. So the static law is not a mixture of formation
laws there, whatever the mixing. On windows without cycles the criterion
tells you exactly which mixtures work: those that only charge orders in
which every record sees at most one neighbour.

Exactly: `w_σ(v^z) − w_σ(v) ≥ 0` with strictness iff `z ∈ ∪_{|A_x| ≥ 2} A_x`
(X1), from `K_k(b,…,b) − K_k(−b,b,…,b) = ((p−q)/Z_1)[(p/Z_1)^{k−1} − (q/Z_1)^{k−1}]`;
on `2×3` the uniform mixture sits at `372254646387017/12790481418000000` from the
static law (the census note's value) and every mixture does not reach it;
on the path `4` of `6` orders qualify and their mixtures are the static law,
on the four-leaf star `48` of `120`. Executed with exact arithmetic:
17 checks, 10 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the campaign's standing question whether the static law used across the repository can arise from the axioms' formation reading by any randomization of the order (the census note's 'witness-generating device'; the rate-clause and formation-unit notes' plaquette results); the derivation campaign's assembly (#8093): the status of the static reconstruction"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "closed for value-blind randomization on every window with a cycle: the static law is not a mixture of formation laws; the exact criterion on cycle-free windows. Open boundary: value-dependent order laws beyond the plaquette. Consumers: #8093's assembly (the static reconstruction is neither a formation law nor a mixture of them); PRs #8148, #8149 (their plaquette results are instances)"
conditional_surface_status: "X1–X3 proved for every finite window and every non-constant rule; executed at (3,1,2); conditional on the records-only reading, the six-axis menu and the product rule as supplied conditions"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a monotone comparison of two patterns per order (X1) from the exact normalizer lemma; a termwise-nonnegative sum forced to vanish (X2); the cycle lemma of block 01; every number an exact rational"
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
along an order `σ` of the window `Λ` the site `x` records with its recorded
neighbours `A_x(σ)` only, `μ_σ(v) = Π_x r(v_x | v_{A_x})`,
`r(a | ∅) = 1/M`, `r(a | A) = Π_{y∈A} K(v_y, a)/K_{|A|}(v_A)`, `K(b,a) = φ(a,b)/Z_1`,
`K_k(v_A) = Σ_s Π_{y∈A} K(v_y, s)`, `K_1 ≡ 1`; block 01's Theorem B (if every
`|A_x| ≤ 1` then `μ_σ` is the static law) and its cycle lemma (on a window
with a cycle every order has a site with `|A_x| ≥ 2`, the last vertex of the
cycle to form). The census note
([`ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`](ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md)):
Lemma L (the multiset key) and Theorem 3 (the uniform mixture on `2×3`). The
static law `Π_edges φ(v_e)/Z`. The six-axis menu, positivity, the product rule
`(p,q,r)`, `Z_1 = p + q + 4r`.

**Mixtures.** A probability `P` on the orders of `Λ`; `μ_P = Σ_σ P(σ) μ_σ`.
Every value-blind randomization of the order is of this form: the uniform
shuffle, random priorities, clocks whose rates depend on the recorded set
(the rate-clause note, PR #8148, R1), any convex combination.

**Weights and flips.** `w_σ(v) = μ_σ(v)/Π_edges K(v_e) = M^{−n_0(σ)} Π_{x: |A_x| ≥ 2} 1/K_{|A_x|}(v_{A_x})`,
`n_0(σ)` the number of sites with `A_x = ∅` (each edge's `K` appears once, at
its later endpoint; `K_1 ≡ 1`). The static law is `Π_edges K · Z_1^{|E|}/Z`, a
constant multiple of `Π_edges K`. For a value `b`, `v ≡ b` is the constant
pattern and `v^z` the pattern with site `z` set to `−b` (to a `c ⊥ b` when
`p = q`).

**The normalizer lemma (from the formation-unit note, PR #8149; re-proved).**
For `k ≥ 2`: `K_k(b,…,b) − K_k(−b,b,…,b) = ((p−q)/Z_1)[(p/Z_1)^{k−1} − (q/Z_1)^{k−1}] > 0`
for `p ≠ q` (both factors have the sign of `p − q`), and
`K_k(b,…,b) − K_k(c,b,…,b) = [(p−r)(p^{k−1} − r^{k−1}) + (q−r)(q^{k−1} − r^{k−1})]/Z_1^k > 0`
unless `p = q = r`. *Proof.* `K_k(a,b,…,b) = Σ_s K(a,s) K(b,s)^{k−1}` and
`K(b,·) − K(−b,·)` is `±(p−q)/Z_1` at `s = ±b`, zero elsewhere; likewise for
`c`. ∎

## Prior art and what is new

Block 01 (on `main`) compared single orders with the static law (Theorem B
and the cycle lemma); the census note computed the uniform mixture on `2×3`
and the cube and called it a witness-generating device; the rate-clause and
formation-unit notes (PRs #8148, #8149, open) excluded every covariant rate
law and every convex combination on the plaquette, using the plaquette's
symmetries. Nothing on `main` treats general mixtures on general windows
(search recorded in `ROUTE_PORTFOLIO.md`).

New here: the flip lemma (X1) as a symmetry-free mechanism; the mixture
theorem with its exact criterion on every window (X2); the constant-environment
version for units (X3); the boundary (X4).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| X1 the flip lemma with the strictness criterion | proved; executed on every (order, site) pair of the plaquette (96) and `2×3` (4320) and every (class, site) pair of the cube (4336) (B1–B2) |
| X2 the mixture theorem; the cycle corollary | proved; executed: the criterion on the path and the star (mixtures over qualifying orders equal the static law, any other differs); the uniform and random mixtures on `2×3` and the plaquette; the cycle lemma on all classes (C1–C4) |
| X3 units in a constant environment | proved; executed on the domino and the path in the all-`+x` environment and in isolation (D1–D2) |
| X4 value-dependent order laws | open beyond the plaquette; named |
| windows with a cycle but other menus; the static law's own phase | open; not this note |

## Theorem X1 — the flip lemma

**Statement.** For every window, every order `σ`, every value `b` and every
site `z`: `w_σ(v^z) ≥ w_σ(v)`, with equality iff `z ∉ ∪_{x: |A_x(σ)| ≥ 2} A_x(σ)`.

*Proof.* `v_z` enters `w_σ` only through the factors `1/K_{|A_x|}(v_{A_x})`
with `z ∈ A_x` and `|A_x| ≥ 2` (the factor of `x = z` itself does not contain
`v_z`). In `v` every member of `A_x` equals `b`; in `v^z` the member `z`
equals `−b` (or `c`) and the others still `b`; by the normalizer lemma each
such `K` strictly decreases, so each such factor strictly increases, and no
other factor changes. ∎ Executed: every (order, site) pair of the plaquette
and of `2×3`, and every (multiset class, site) pair of the cube — `w_σ` depends
on `σ` only through the recorded sets — with strictness exactly on the
predicted pairs (B1); the lemma symbolically for `k = 2..6` (B2).

## Theorem X2 — the mixture theorem

**Statement.** For every finite window `Λ`, every non-constant rule and
every probability `P` on orders: `μ_P` is the static law of `Λ` iff every
order charged by `P` has `|A_x(σ)| ≤ 1` for all `x`. In particular, on every
window containing a cycle, no mixture of formation laws is the static law.

*Proof.* (⇐) Each charged `μ_σ` is the static law by Theorem B, hence so is
the mixture. (⇒) If `μ_P` is the static law then `μ_P/Π_edges K` is constant,
so for every `z`: `0 = Σ_σ P(σ)[w_σ(v^z) − w_σ(v)]`, a sum of nonnegative
terms by X1; hence every charged `σ` has `z ∉ ∪_{|A_x| ≥ 2} A_x`. Over all
`z ∈ Λ` the union is empty for every charged `σ`: no site records two or more
neighbours. The cycle lemma gives the particular case. ∎ Executed: on the
path (`4` of `6` orders qualify) and the four-leaf star (`48` of `120`) the
uniform mixture over qualifying orders equals the static law exactly and
pseudo-random mixtures that charge a non-qualifying order differ (C1–C2); on
`2×3` the uniform mixture reproduces the census note's distance and
pseudo-random mixtures differ (C3); the cycle lemma on every class of the
plaquette, `2×3` and the cube (C4).

*Reading.* Randomizing the order buys nothing toward the static law: the
missing normalizers can only be averaged, never cancelled, because a flip
moves every one of them the same way. The static reading is not a
formation law and not an average of formation laws on any window with a
square in it.

## Theorem X3 — units in a constant environment

**Statement.** Let `U` be a unit whose outside neighbours all carry the same
record `b`, and let `μ^{joint}` be its joint law (the formation-unit note, U1).
For every probability `P` on the orders of `U`: `Σ_σ P(σ) μ_σ(· | v_O) = μ^{joint}(· | v_O)`
iff every charged order satisfies the criterion of the formation-unit note
(no site records an inside neighbour together with a second recorded
neighbour). In a full constant environment every connected unit with two or
more sites therefore has no such mixture.

*Proof.* With the outside records equal to `b`, the constant inside pattern
`v ≡ b` and its flips `v^z` (`z ∈ U`) have all members of every recorded set
equal to `b` except the flipped one, so X1's argument applies verbatim to the
ratio `μ_σ/Π K` over the edges inside `U` and from `U` to `O`, whose constant
multiple is the joint law; strictness occurs iff `z` lies in a recorded set
of size at least two, and the recorded sets of size at least two that contain
an inside site are exactly the criterion's violations. The last sentence is
the formation-unit note's U4. ∎ Executed: the domino and the path in the
all-`+x` environment (every order violates; every mixture differs) and in
isolation (mixtures over qualifying orders equal the joint law) (D1–D2).

## X4 — the boundary

For an order law that depends on the recorded values, `P(σ | v)` changes
with the flip and X1 gives no comparison. The rate-clause note settles the
plaquette for every covariant value-dependent clock law by symmetry; larger
windows with value-dependent order laws are open.

## No-Go Discipline Gate

The negative sentence is X2's cycle corollary (and X3's environment
corollary): no mixture over orders is the static (joint) law. Proved for
every non-constant rule.

### N1 — Routes by which a mixture could still reach the static law

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 cancellation among orders | some orders over-weighting, others under-weighting a pattern | the flip moves every order's weight the same way (X1), so a sum of nonnegative terms vanishes only termwise | RULED OUT AT SCOPE |
| 2 value-dependent order laws | `P(σ | v)` compensating the flip | outside X1; the plaquette is settled by symmetry (PR #8148); larger windows open | X4 |
| 3 the constant rule | `p = q = r` | every law uniform | trivial |
| 4 other menus | a menu where some normalizer is constant in one argument | outside the six-axis menu; obligation named | not attempted |
| 5 non-constant environments for units | the flip's monotonicity uses equal recorded values | X3 restricted to constant environments; per-order statements in PR #8149 | narrowed |

### N2 — Wall-independence audit
Walls: the records-only reading, the product rule, positivity. Independent; each defines the object.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: none in the theorems.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 01 (main): Theorem B; the cycle lemma | single orders | X2's "if" and the corollary | yes |
| the census note (main): Lemma L; Theorem 3 | the multiset key; the uniform mixture | the class reduction of the executions; the reproduced value | yes |
| PRs #8148, #8149 (open; not inputs) | the plaquette by symmetry; the criterion and lemma | X3's criterion; the lemma re-proved here | context only |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "no mixture over orders is the static law on a window with a cycle" | executed: the lemma for `k = 2..6`; the flip on every order–site pair of two windows and every class–site pair of the cube | executed: every pattern of the path, the star, the plaquette and `2×3` in the mixture checks | executed: every order class of three windows | executed: five windows, two environments | proved for every window and every non-constant rule (X2); value-dependent order laws open (X4) |

### N6 — Partial-closure paths and primitive scan
The realized-state primitive supplies no measure over orders; none is assumed — the theorem quantifies over all. No primitive is a wall.

### N7 — Steelman
Hostile reviewer: "A three-line argument; the plaquette results already said this." Reply: they said it for one window through its symmetries; this says it for every window with one mechanism, gives the exact criterion where mixtures do work, and needs nothing but the normalizer lemma. Conceded: value-dependent order laws are open beyond the plaquette.

### N8 — Cross-cycle echo
Block 01's Theorem B, the seeded-growth result of PR #8148 and X2's criterion are one fact: every record seeing at most one neighbour is exactly when the formation reading meets the static one. No structurally similar wall was retired.

## Falsifiers
- An (order, site) pair on the plaquette or `2×3`, or a (class, site) pair on the cube, where the flip lowers the weight or where strictness disagrees with the criterion (B1); a `k ≤ 6` where the lemma's closed form fails (B2).
- A mixture over qualifying orders of the path or the star that is not the static law, or a mixture charging a non-qualifying order that is (C1–C2); a uniform `2×3` mixture differing from the census value (C3); a class of any of the three windows with all recorded sets of size at most one (C4).
- A domino or path order in the all-`+x` environment that satisfies the criterion or a mixture equal to the joint law there; an isolated qualifying mixture that is not the joint law (D1–D2).

## Boundaries and non-claims
This note proves that mixtures of formation laws are the static law only when they charge orders in which every record sees at most one neighbour, and never on a window with a cycle; it does not treat value-dependent order laws beyond the plaquette, other menus, or non-constant environments for units, does not select an order, mixture, rule or coupling as physical, and adopts no clause. No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 and the census note (both on `main`): proposed, unaudited; the parts used (Theorem B, the cycle lemma, Lemma L, Theorem 3's value) are restated. PRs #8148 and #8149 (open) are referenced for context only; the normalizer lemma is re-proved here.
- Re-proved at scope: the normalizer lemma, X1, X2, X3.

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane and take it; no subagents). The control (`specs/supervisor_control_block16_flip_monotonicity.py`) checked the flip lemma on every order–site pair of three windows and the forest criterion before the contract; the lens pass is in `GOAL_block16.md`; the primary seat wrote X1–X4 and the runner; the refuting pass (`CHECKER_block16_findings.md`) recomputed the flip comparison from the full sequential laws instead of the weight formula, the qualifying orders by a direct search for a site with two recorded neighbours, and the `2×3` uniform mixture by the census runner's cache. Facts settled while executing: the cube's flip check runs on its 542 multiset classes rather than its 40,320 orders (the weight depends on the order only through the recorded sets; the control checked all 322,560 order–site pairs); X3 is stated for constant environments only, because the flip's monotonicity needs every other member of a recorded set to carry the same value as the flipped one.

## Verification

```bash
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py --exact
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py --mutation mixture_equals_static_claimed
```

Families: A authority and inputs; B the lemma and the flip lemma; C the mixture theorem on the path, the star, `2×3` and the plaquette, and the cycle lemma; D units in a constant environment; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 10 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=17 FAIL=0`.
