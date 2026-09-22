---
claim_id: admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For a finite window with supplied total formation order and positive six-axis product rule: exact recorded-set factorization, containing Markov graph, vacuum-normalized potential and maximal-set mixed-difference identities. Exact plaquette/star and mixed-ratio witnesses at the declared triples. A nearest-neighbor graph suffices when every recorded set has at most one element. The converse/minimal-graph and excluded-graph conclusions are explicitly deferred; their full original proof is archived."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
  - admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_bounded_theorem_note_2026-09-15
runner: scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py
---

# Recorded-set Gibbs factorization, a containing graph and exact potential witnesses

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact on finite windows; conditional on the named supplied readings; unaudited)

## Result up front

Whatever order the records form in, the finished pattern obeys a law of the
same shape: each pair of adjacent records is coupled by the rule's kernel, and
each group of neighbors that a site "saw" when it formed is coupled all
together by a normalizer term. So the pattern law is always a Gibbs law, and
its "who influences whom" graph is the lattice's adjacency plus, for every site,
the pairs among the neighbors it saw. Those extra pairs are never lattice neighbors themselves. The displayed graph
always contains a valid Markov graph. The explicit maximal-set potential
identities and mixed-ratio witnesses are retained. Certification of the
converse nearest-neighbor criterion and excluded-graph/minimality conclusions
is deferred; the sufficient direction is retained.

Exactly: `μ_σ(v) = (1/6)^{#{x : A_x = ∅}} Π_{xy ∈ E(W)} K(v_x, v_y) / Π_{|A_x| ≥ 2} K_{|A_x|}(v_{A_x})`
(T1); Markov for `G_σ = E(W) ∪ ⋃_x binom(A_x, 2)` (T2); the unique vacuum-
normalized potential has a nonzero term on every maximal recorded set of size
`k` with nonzero `k`-th mixed difference of `log K_k` — ratios `169/121`,
`169/165`, `25313305500289/23811286661761`, … for `k = 2, 3, 4, …, 6` at
`(3, 1, 2)` (T3); T4 retains the sufficient nearest-neighbor condition; its converse is deferred. Executed
with exact arithmetic: 18 checks, 10 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the campaign's standing question (block 01): when is the formation law of a covariant nearest-neighbor rule the static law, and what is it otherwise; the derivation campaign's formation-law node (#8093) and the multiset key of #8102 (the law depends on the order through the recorded sets of size at least two); the owner's sequencing gate (2026-08-26)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use the recorded-set factorization, containing graph and explicit potential identities. The converse nearest-neighbor criterion and excluded-graph/minimality certification remain deferred with original proofs preserved."
conditional_surface_status: "T1 and T2 finite-window factorization and containing graph; T3 potential identities under stated hypotheses; T4 sufficient direction only; T5 range bound and conditional body-count identities; exact T6 potential witnesses. Converse and excluded-graph certification deferred."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "T1 is the regrouping of the product of conditionals; T2 is read off T1; T3 re-proves the uniqueness of the vacuum-normalized potential of a positive law on a finite set and computes its recorded-set terms as mixed differences; T4 retains the sufficient condition only; every number printed is an exact rational"
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "When present, a record locks exactly one
admissible local possibility." — "Only records are readable."

**Readings carried, named, nothing new adopted.** The records-only reading;
positivity; the six-axis menu with orbit weights `(p, q, r)`; block 01's
definition of the formation law of a total order `σ` on a finite window `W`
(a finite induced subgraph of `Z^3` with its nearest-neighbor edges `E(W)`):
`μ_σ(v) = Π_x r(v_x | v_{A_x})`, where `A_x = {y ∼ x : y before x in σ}` is
the recorded set of `x`, `r(s | ∅) = 1/6` and
`r(s | a_1, …, a_k) = Π_i φ(s, a_i)/Z_k(a) = Π_i K(a_i, s)/K_k(a)` with
`K_k(a) = Σ_s Π_i K(a_i, s)` (block 08's notation; `K_1 ≡ 1`, `K_2 = K^2`). No
order is selected as physical.

**Vacuum and mixed differences.** Fix the vacuum value `0 = P(+e_1)` (any
value would do, by the internal covariance). For a function `F` of `k` menu
values, the `k`-th mixed difference at `a = (a_1, …, a_k)` is
`Δ_k F(a) = Σ_{S ⊆ {1..k}} (−1)^{k − |S|} F(a_S, 0_{S^c})`; `F` is a sum of
functions of proper subsets of its arguments iff `Δ_k F ≡ 0`. For `F = log K_k`
the exponential of `Δ_k F` is a ratio of products of `K_k`-values, an exact
rational.

**The recorded-set graph.** `G_σ` has vertex set `W` and edge set
`E(W) ∪ ⋃_x binom(A_x, 2)`. A recorded set is maximal if it is contained in no
other recorded set of `σ`. On `Z^3` two neighbors of a site are at distance
`√2` (orthogonal) or `2` (opposite), never adjacent: the lattice is bipartite.


### Linked source authority

- [Admissibility Rule Three Dimensional Monotone Formation Law Plane Chain Coupling Region Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md): only its explicit hypotheses and conclusions are used.

- [Admissibility Rule Formation Law Versus Static Law Finite Window Classification Bounded Theorem Note 2026-09-06](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md): the actual predecessor premise, restricted to the quoted theorem hypotheses.

## Prior art and what is new

Block 01 (on main) proved that `μ_σ` equals the static law iff every recorded
set has at most one element (Theorem B), re-proved Brook's ratio lemma and
referenced Hammersley–Clifford only. Blocks 08–09 (stacked) and the plane-law
note (on main) computed the monotone class's Gibbs potentials in three and two
dimensions and, on `Z^3`, the containing graph and conditional witnesses;
current certification of the static-law exclusion is deferred.
The concurrent #8102 (open; not an input) proved that `μ_σ` depends on `σ`
only through the multiset of recorded sets of size at least two — consistent
with T1, which displays that dependence. The uniqueness of the vacuum-
normalized potential of a positive law on a finite set (Grimmett's proof of
Hammersley–Clifford) is a classical reference re-proved here at scope.

New here: the recorded-set Gibbs form for every order (T1), the Markov graph
(T2), the canonical-potential terms on the recorded sets and their
irreducibility up to `k = 6` (T3), the sufficient nearest-neighbor condition (T4), the range statement (T5), and the executed
plaquette and star potentials (T6).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| T1 the product form for every order | proved (regrouping); executed on the plaquette's 24 orders and the star's 24 orders (B1) |
| T2 the Markov graph | proved from T1 |
| T3(a) uniqueness of the vacuum-normalized potential; Markov for `G` ⇒ support on cliques of `G` | re-proved (inversion on the subset lattice) |
| T3(b) the recorded-set terms are mixed differences; nonzero on maximal sets when `Δ_k log K_k ≠ 0` | proved; `Δ_k log K_k ≠ 0` executed for `k = 2..6` at `(3,1,2)`, `(5,2,4)`; zero at `(2,2,2)` (B2, B3) |
| T4 sufficient nearest-neighbor condition | proved when every recorded set has size at most one; converse/excluded-graph certification deferred |
| T5 range and body count | proved from T1–T3 |
| T6 the plaquette and the star potentials | executed (C1–C4) |
| `Δ_k log K_k ≠ 0` at every nonconstant triple; infinite-volume laws for non-monotone classes | open; not this note |

The mixed differences are witnessed nonzero at the two declared triples.
Nonzero at every nonconstant triple is not a valid general premise: the
exceptional-construction note supplies three-body zero examples. The
higher-body identities retain their explicit nonvanishing hypotheses.

## Theorem T1 — the recorded-set product form

**Statement.** For every finite window `W` and total order `σ`,
`μ_σ(v) = (1/6)^{n_0} Π_{xy ∈ E(W)} K(v_x, v_y) / Π_{x : |A_x| ≥ 2} K_{|A_x|}(v_{A_x})`,
with `n_0 = #{x : A_x = ∅}`.

*Proof.* Every edge `xy` of `W` is recorded exactly once, by its later
endpoint (when the later site forms, the earlier is a recorded neighbor), so
`Π_x Π_{y ∈ A_x} K(v_y, v_x) = Π_{E(W)} K`. A site with `A_x = ∅` contributes
`1/6`; one with `|A_x| = 1` contributes `K(v_y, v_x)` (`K_1 ≡ 1`); one with
`|A_x| ≥ 2` contributes `Π_{y ∈ A_x} K(v_y, v_x)/K_{|A_x|}(v_{A_x})`. ∎
Executed: on the plaquette (cycle4) and the star (star4), for all `24` orders
each, the product form equals the product of conditionals on every
configuration (B1).

## Theorem T2 — the Markov graph

**Statement.** `μ_σ` is a Markov field for `G_σ`: its conditional at `x`
given the rest depends only on the `G_σ`-neighbors of `x`.

*Proof.* In `μ_σ(v_x = s | rest)` every factor of T1 not containing `x`
cancels; the remaining factors are the edge factors at `x` and the normalizers
`K_{|A_y|}(v_{A_y})` of the sites `y` with `x ∈ A_y`, which involve the other
members of `A_y` — `G_σ`-neighbors of `x` by definition. ∎

## Theorem T3 — the canonical potential and its recorded-set terms

**(a) Uniqueness (re-proved).** Let `μ > 0` be a law on `M^W`. There is exactly
one family `(Φ_S)_{S ⊆ W}` with `log μ(v) = Σ_S Φ_S(v_S)` and `Φ_S(v_S) = 0`
whenever some coordinate of `v_S` equals the vacuum; it is
`Φ_S(v_S) = Σ_{T ⊆ S} (−1)^{|S ∖ T|} log μ(v_T, 0_{W ∖ T})`. If `μ` is a Markov
field for a graph `G`, then `Φ_S = 0` unless `S` is a clique of `G`.

*Proof.* Existence and uniqueness are the inclusion–exclusion inversion on the
subset lattice of `W`, applied to `f(T) = log μ(v_T, 0_{T^c})` for fixed `v`. For the
clique statement take `S` with two non-adjacent sites `x, y ∈ S`; write
`Φ_S = Σ_{T ⊆ S ∖ {x,y}} (−1)^{|S ∖ T| } [f(T ∪ {x, y}) − f(T ∪ {x}) − f(T ∪ {y}) + f(T)]`
by grouping the four subsets differing at `x, y`; each bracket equals
`log [μ(v_x = s | rest) / μ(v_x = 0 | rest)]` evaluated at two configurations
of the rest differing only at `y`, which are equal by the Markov property
(`y` is not a `G`-neighbor of `x`); so every bracket vanishes. ∎

**(b) The recorded-set terms.** Let `A` be a maximal recorded set of `σ` with
`|A| = k ≥ 2` and let `m_A` be the number of sites whose recorded set equals
`A`. Then `Φ_A(v_A) = −m_A · Δ_k log K_k(v_A)`, and `Φ_A ≠ 0` iff
`Δ_k log K_k ≢ 0`.

*Proof.* In T1's form, `log μ_σ` is a sum of the constant `n_0 log(1/6)`, the
edge terms `log K(v_x, v_y)` (functions of pairs), and the terms
`−log K_{|A_y|}(v_{A_y})` (functions of the recorded sets). The `S`-term of the
vacuum-normalized potential of a sum is the sum of the `S`-terms, and the
`S`-term of a function of `v_B` is zero unless `S ⊆ B`, in which case it is
the `S`-mixed difference of that function with the vacuum at `B ∖ S`. For
`S = A` maximal: no edge contains `A` (`k ≥ 2` and the pairs of `A` are
non-adjacent), and the only recorded sets containing `A` are those equal to
`A` (maximality), each contributing `−Δ_k log K_k(v_A)`. ∎ Executed: the ratio
`exp(Δ_k log K_k)` at a witness assignment for `k = 2, …, 6` is
`169/121, 169/165, 25313305500289/23811286661761, 2241861381895613/2214449659543773, …`
at `(3, 1, 2)` and `961/784, 1291123/1244800, 845934898201600/806460091894081, …`
at `(5, 2, 4)`, none equal to `1` (B2); at the constant rule every searched
ratio is `1` (B3). (For `k = 2` the statement is `K^2` not of rank one, i.e.
nonconstant; for `k = 3` it is block 08's third difference.)

## Theorem T4 — a sufficient nearest-neighbor condition

**Statement.** If every recorded set of `σ` has at most one element, `μ_σ`
is a Markov field for `E(W)`.

*Proof.* T1 has no normalizer term, so `G_σ=E(W)` and T2 applies. ∎

The original converse, excluded-graph conclusion and minimality inference,
including the full proof with its nonzero maximal-set hypotheses, are retained
byte-exact under PR8141 in the history manifest. Their negative certificate
is incomplete, so those conclusions are deferred. T3's explicit potential
formula and finite nonzero mixed-ratio witnesses remain live.

## Theorem T5 — the range and the body count of the induced interaction

**Statement.** The potential of T1 couples adjacent sites (the rule's own
range), orthogonal co-recorded neighbors (distance `√2`), opposite co-recorded
neighbors (distance `2`), and nothing farther; its canonical terms on maximal
recorded sets are genuine `k`-body terms for every `k ≤ 6` that occurs, at the
triples of T3. Under that nonzero sixth-difference hypothesis, a site with all six
neighbors recorded (formed last in its neighborhood) carries a six-body term.

*Proof.* Every recorded set is a subset of a neighborhood; the pairs inside a
neighborhood are at distance `√2` or `2`; T3(b) gives the body count. ∎

## T6 — two executed canonical potentials

**The plaquette** `a — b, a — c, b — d, c — d` with the order `(a, b, c, d)`
(`d` records `b` and `c`): at `(3, 1, 2)` the canonical potential has the pair
term `exp Φ_{bc} = 12/13` at the witness `(a, b, c, d) = (−x, +y, +z, −y)`
(nonzero for some configuration; `{b, c}` is the co-recorded non-adjacent
pair), `exp Φ_{ad} = 1` on all `1296` configurations (`{a, d}` is the other
non-edge, never co-recorded), the edge terms `exp Φ_{ab} = 3`,
`exp Φ_{bd} = 3/4` at the witness, and `exp Φ_{abcd} = exp Φ_{bcd} = 1` at the
witness (C1–C3). So this formation law is Markov for the plaquette plus the
diagonal `{b, c}` — an explicit two-dimensional diagonal
interaction of the plane-law note, at its smallest.

**The star** `x` with leaves `l_1, l_2, l_3`, the center last: the three-body
term on the leaves is nonzero, `exp Φ_{l_1 l_2 l_3} = 165/169` at
`(l_1, l_2, l_3) = (−x, −x, +y)` (C4) — block 08's three-body term at its
smallest, on a tree with no plaquette: the formation law of a tree swept from
its center outward is nearest-neighbor Markov (every leaf records one site,
the sufficient condition), while the leaves-first order has the displayed
nonzero three-body potential witness. The excluded-graph inference is deferred.

## No-Go Discipline Gate — deferred broader certification

This revision retains the constructive identities, quantitative bounds and named
finite witnesses above. It does not certify the broader exclusion claims in the
original packet. The original N1–N8 text and every recovery route are preserved
byte-exact in [the PR8146 history manifest](work_history/review_loop/pr8146/original-manifest.json)
under PR8141; the original branch remains a recovery handle for unlanded work.

### N1 — Route coverage
The specifically deferred conclusions are the T4 converse/iff criterion and
the excluded-graph/minimality conclusions.
The original list includes unattempted and out-of-domain routes. It is not a
completed route search; broader negative certification is deferred.

### N2 — Walls
The positive weights, six-axis menu, product rule and specified formation class
remain supplied conditions, not deductions or selected physical inputs.

### N3 — Hidden walls
The statements above carry their finite-window, parameter, nonvanishing and
invariance hypotheses explicitly. No unrestricted exclusion follows.

### N4 — Citation scope
Linked source arguments support only their stated mathematical hypotheses.
Historical branch review and cache records are provenance, not authority.

### N5 — Resolution
Exact finite witnesses and the proved formula domains remain as stated above.
They do not establish exhaustive route, phase or infinite-law classification.

### N6 — Partial closure
The positive results are preserved. Unproved exclusions remain open with their
original attempted routes recoverable; no new premise closes them.

### N7 — Steelman
A quantitative bound or finite discrepancy does not settle every alternative
law or order. This revision concedes that gap rather than asserting closure.

### N8 — Recovery
The history manifest binds original heads, paths, decompressed SHA256 hashes and
archive hashes. This deferred certificate is not a passing negative-claim gate;
any future broader exclusion must complete the applicable discipline.

## Falsifiers
- An order of the plaquette or the star on which T1's product form differs from the product of conditionals (B1).
- A `k ≤ 6` at `(3, 1, 2)` or `(5, 2, 4)` for which every searched mixed-difference ratio equals `1`, or a nonzero ratio at the constant rule (B2, B3).
- A configuration of the plaquette on which `exp Φ_{ad} ≠ 1`, or `exp Φ_{bc} = 1` on all configurations (C1, C2).
- A vanishing three-body term on the star's leaves for all leaf values (C4).
- A pair of adjacent sites inside a recorded set (impossible on `Z^3`; would refute the stated lattice pair geometry).

## Boundaries and non-claims
This note describes formation laws on finite windows for every order; it states nothing infinite-volume beyond citing blocks 08–09 for the monotone class, nothing about the static law beyond block 01's equality case, and selects no order as physical. No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision. The vacuum-normalized potential and its clique property are classical references re-proved here at the scope used; no value, constant or theorem is imported as authority.

Further: the mixed differences are executed at two nonconstant triples and one witness assignment per `k`, not proved nonzero at every nonconstant triple; T6 covers two windows; the sum rule and other non-product covariant rules are outside T1.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on main), blocks 08 and 09 (stacked), the plane-law note (on main): proposed, unaudited; the parts used are restated.
- Re-proved at scope: the Möbius inversion on the subset lattice and the uniqueness of the vacuum-normalized potential; its clique property under a Markov hypothesis (the standard Hammersley–Clifford / Grimmett argument).
- No literature value, constant, or theorem enters as authority; the classical names appear only here and under Prior art.

## Review record
Supervisor-run block (owner directive 2026-09-15: no subagents). The control (`specs/supervisor_control_block10_recorded_set.py`) computed the mixed-difference ratios for `k = 2..6`, the plaquette potential and the star potential before the contract; the lens pass is in `GOAL_block10.md`; the primary seat wrote T1–T6 and the runner; the refuting pass (`CHECKER_block10_findings.md`) recomputed the plaquette and star terms by the closed form `exp(−Δ_k log K_k)`
and with the vacuum moved to `−x`, instead of the subset-lattice inversion; the fold is in `REVIEW_HISTORY.md`. Facts settled while executing: a word for the covered maximal sets collided
with a forbidden token and was reworded; the classical names were moved out of
the obligation table, Theorem T3, the steelman and the Review record.

## Verification

```bash
python3 scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py
python3 scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py --exact
python3 scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py --mutation plaquette_nonedge_term_claimed
```

Families: A authority and inputs; B the product form and the mixed differences; C the plaquette and star potentials and their Markov graphs; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 10 declared mutations fails in exactly one family. Expected final
line: `TOTAL: PASS=18 FAIL=0`.
