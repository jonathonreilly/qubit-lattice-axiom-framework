---
claim_id: admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule of orbit weights (p, q, r), under the records-only reading, on every finite window W of Z^3 and for every total formation order sigma with recorded sets A_x: (T1) the formation law is the product (1/6)^{#{x : A_x empty}} prod_{edges} K / prod_{|A_x| >= 2} K_{|A_x|}(v_{A_x}), a Gibbs law for the potential -log K on the edges and +log K_k on the recorded sets of size k >= 2; (T2) it is a Markov field for the recorded-set graph (the edges of W together with the pairs inside each recorded set); (T3) a positive law on a finite window has exactly one vacuum-normalized potential, and that potential of the formation law has a nonzero term on every maximal recorded set of size k >= 2 at which the k-th mixed difference of log K_k is nonzero — nonzero for k = 2, ..., 6 at (3, 1, 2) and (5, 2, 4), zero at the constant rule (executed) — while the pairs inside a recorded set are never adjacent; hence (T4) the formation law is a nearest-neighbor Markov field if and only if every recorded set has at most one element (block 01's condition, now for the Markov property), and otherwise it is Markov for no graph missing a co-recorded pair; (T5) the induced interaction reaches the orthogonal (sqrt 2) and opposite (distance 2) co-recorded neighbors and carries genuine k-body terms up to k = 6; (T6) executed canonical potentials: the plaquette whose last site records two neighbors (pair term 12/13 on the co-recorded non-adjacent pair; zero on the other non-edge on all 1296 configurations; zero four-body and three-body terms at the witness) and the star whose center forms last (three-body term 165/169 on the leaves). Nothing infinite-volume beyond citing blocks 08-09 for the monotone class; no order selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
  - admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_bounded_theorem_note_2026-09-15
runner: scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py
---

# Every formation law is a Gibbs law whose Markov graph is the recorded-set graph: nearest-neighbor Markov exactly when no site records two neighbors

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact on finite windows; conditional on the named supplied readings; unaudited)

## Result up front

Whatever order the records form in, the finished pattern obeys a law of the
same shape: each pair of adjacent records is coupled by the rule's kernel, and
each group of neighbors that a site "saw" when it formed is coupled all
together by a normalizer term. So the pattern law is always a Gibbs law, and
its "who influences whom" graph is the lattice's adjacency plus, for every site,
the pairs among the neighbors it saw. Those extra pairs are never lattice
neighbors themselves, and their coupling is genuine for groups of any size from
two up to six. The consequence: a formation law listens only to nearest
neighbors precisely when no site ever saw two of its neighbors at once — the
same condition under which the earlier note showed it coincides with the static
law. Otherwise it is not a nearest-neighbor law at all, of any kind: forming
records with the rule creates couplings at a range the rule itself does not
have. Nothing here picks an order.

Exactly: `μ_σ(v) = (1/6)^{#{x : A_x = ∅}} Π_{xy ∈ E(W)} K(v_x, v_y) / Π_{|A_x| ≥ 2} K_{|A_x|}(v_{A_x})`
(T1); Markov for `G_σ = E(W) ∪ ⋃_x binom(A_x, 2)` (T2); the unique vacuum-
normalized potential has a nonzero term on every maximal recorded set of size
`k` with nonzero `k`-th mixed difference of `log K_k` — ratios `169/121`,
`169/165`, `25313305500289/23811286661761`, … for `k = 2, 3, 4, …, 6` at
`(3, 1, 2)` (T3); nearest-neighbor Markov iff `max_x |A_x| ≤ 1` (T4). Executed
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
next_trace_action: "the structure of every formation law on a finite window is now the recorded-set Gibbs law; the infinite-volume versions exist for the monotone class (blocks 08-09); next: the region's boundary in (p, q, r); a covariant order class's infinite-volume structure needs a supplied construction. Consumers: the campaign's queue; #8093's assembly (the formation-law node: any single order induces a longer-range law than the rule); the parked statistical-bridge material (read-only)"
conditional_surface_status: "exact on every finite window and every order for T1, T2, T4's forward direction and T5; T3 and T4's converse at triples where the relevant mixed differences are nonzero (executed for k = 2..6 at (3,1,2) and (5,2,4)); T6 executed; conditional on the records-only reading, positivity, the six-axis menu; no infinite-volume claim beyond citation"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "T1 is the regrouping of the product of conditionals; T2 is read off T1; T3 re-proves the uniqueness of the vacuum-normalized potential of a positive law on a finite set and computes its recorded-set terms as mixed differences; T4 combines T3 with the bipartite structure of the lattice; every number printed is an exact rational"
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

## Prior art and what is new

Block 01 (on main) proved that `μ_σ` equals the static law iff every recorded
set has at most one element (Theorem B), re-proved Brook's ratio lemma and
referenced Hammersley–Clifford only. Blocks 08–09 (stacked) and the plane-law
note (on main) computed the monotone class's Gibbs potentials in three and two
dimensions and, on `Z^3`, the Markov graph and the separation from static laws.
The concurrent #8102 (open; not an input) proved that `μ_σ` depends on `σ`
only through the multiset of recorded sets of size at least two — consistent
with T1, which displays that dependence. The uniqueness of the vacuum-
normalized potential of a positive law on a finite set (Grimmett's proof of
Hammersley–Clifford) is a classical reference re-proved here at scope.

New here: the recorded-set Gibbs form for every order (T1), the Markov graph
(T2), the canonical-potential terms on the recorded sets and their
irreducibility up to `k = 6` (T3), the classification of nearest-neighbor
Markov formation laws (T4), the range statement (T5), and the executed
plaquette and star potentials (T6).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| T1 the product form for every order | proved (regrouping); executed on the plaquette's 24 orders and the star's 24 orders (B1) |
| T2 the Markov graph | proved from T1 |
| T3(a) uniqueness of the vacuum-normalized potential; Markov for `G` ⇒ support on cliques of `G` | re-proved (inversion on the subset lattice) |
| T3(b) the recorded-set terms are mixed differences; nonzero on maximal sets when `Δ_k log K_k ≠ 0` | proved; `Δ_k log K_k ≠ 0` executed for `k = 2..6` at `(3,1,2)`, `(5,2,4)`; zero at `(2,2,2)` (B2, B3) |
| T4 nearest-neighbor Markov iff `max |A_x| ≤ 1` | proved from T3 and bipartiteness at triples with the executed nonzero differences; forward direction unconditional |
| T5 range and body count | proved from T1–T3 |
| T6 the plaquette and the star potentials | executed (C1–C4) |
| `Δ_k log K_k ≠ 0` at every nonconstant triple; infinite-volume laws for non-monotone classes | open; not this note |

The strongest missing lemma is that `Δ_k log K_k` is nonzero at every
nonconstant triple for every `k ≤ 6`; T4's converse is stated where it is.

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

## Theorem T4 — nearest-neighbor Markov exactly when no site records two neighbors

**Statement.** If every recorded set of `σ` has at most one element, `μ_σ`
is a Markov field for `E(W)` (and equals the static law, block 01's Theorem B).
Conversely, at a triple where `Δ_k log K_k ≠ 0` for every `k ≤ 6` that occurs
as the size of a maximal recorded set (executed: every `k ≤ 6` at `(3, 1, 2)`
and `(5, 2, 4)`), if some recorded set has two or more elements then `μ_σ` is
not a Markov field for `E(W)`, nor for any graph in which some co-recorded
pair is not an edge.

*Proof.* Forward: T1 has no normalizer term, so `G_σ = E(W)` and T2 applies.
Converse: a recorded set with `≥ 2` elements is contained in a maximal one `A`
with `|A| = k ≥ 2`; by T3(b) `Φ_A ≠ 0`; `A` is not a clique of `E(W)` (its
pairs are non-adjacent, the lattice being bipartite), nor of any graph missing
one of its pairs; by T3(a) `μ_σ` is not Markov for such a graph. ∎

## Theorem T5 — the range and the body count of the induced interaction

**Statement.** The potential of T1 couples adjacent sites (the rule's own
range), orthogonal co-recorded neighbors (distance `√2`), opposite co-recorded
neighbors (distance `2`), and nothing farther; its canonical terms on maximal
recorded sets are genuine `k`-body terms for every `k ≤ 6` that occurs, at the
triples of T3. A site with all six neighbors recorded (formed last in its
neighborhood) carries a six-body term.

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
diagonal `{b, c}`, not for the plaquette — the two-dimensional diagonal
interaction of the plane-law note, at its smallest.

**The star** `x` with leaves `l_1, l_2, l_3`, the center last: the three-body
term on the leaves is nonzero, `exp Φ_{l_1 l_2 l_3} = 165/169` at
`(l_1, l_2, l_3) = (−x, −x, +y)` (C4) — block 08's three-body term at its
smallest, on a tree with no plaquette: the formation law of a tree swept from
its center outward is nearest-neighbor Markov (every leaf records one site,
Theorem B), while the same tree swept leaves-first is not (T4).

## No-Go Discipline Gate

The negative sentence is T4's converse ("not a nearest-neighbor Markov field
when some site records two neighbors"). It is proved from T3 at the triples
named; not a route no-go beyond that scope.

### N1 — Routes by which a formation law with a two-element recorded set could still be nearest-neighbor Markov

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 cancellation between overlapping recorded sets | terms on a non-maximal set cancelling | only maximal sets are covered; a `≥ 2` set lies in a maximal `≥ 2` set, whose term has no other contributor | ATTEMPTED (proof) |
| 2 a triple with `Δ_k log K_k = 0` | a nonconstant `(p, q, r)` at which some `k`-body term vanishes | executed nonzero at two triples for `k ≤ 6`; not proved for all nonconstant triples | not attempted; obligation named |
| 3 a non-bipartite window | co-recorded neighbors that are adjacent | not on `Z^3` or any of its induced subgraphs | RULED OUT BY PRIOR (the lattice axiom) |
| 4 the constant rule | `p = q = r` | every term vanishes; the independent uniform law is Markov for every graph; excluded by the variation clause restricted to the menu | ATTEMPTED (control) |
| 5 a non-product covariant rule | the sum rule | T1's regrouping uses the product form; a different rule is a different note (block 01's family G) | not attempted; obligation named |

### N2 — Wall-independence audit
Walls: `W_pos` (positivity: the canonical potential of a positive law), `W_menu`, `W_prod` (the product form of the rule), `W_Δ` (nonzero mixed differences), `W_var`. `W_Δ` implies `W_var` (the constant rule has zero differences); `W_var` does not imply `W_Δ` for every `k` (not proved). `W_pos` and `W_prod` are the definitions of the objects. No wall follows from another except as stated.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: "canonical" as the name of the vacuum-normalized potential (defined in T3(a), not an authority). No wall was promoted.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 01 (on main): Theorem B and the formation-law definition | equality with the static law iff `≤ 1` recorded | T4's forward direction and the equality case | yes (parent) |
| block 08 (stacked): Q1e–f | the monotone class's product form and third difference | the `k = 3` case of T3(b) | yes (parent) |
| block 09 (stacked): L2 | the `Z^3` statement for the monotone class | cited only in the trace | yes (context) |
| the plane-law note (on main) | the 2D diagonal interaction | T6's plaquette as its smallest instance | yes (context) |
| #8102 (open; not an input) | the multiset key | consistency remark | yes (context) |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "not a nearest-neighbor Markov field when some site records two neighbors" | executed: the mixed-difference ratios at witness assignments for `k = 2..6`, three triples; the plaquette's `{a, d}` term on all 1296 configurations | executed: every site's recorded set in every order of the plaquette and the star (48 orders) | executed: the canonical terms on the edges, the diagonal, the triple and the quadruple of the plaquette; the leaves' triple of the star | executed: the two windows' full potentials at the witnesses | proved on every finite window at the named triples; infinite volume only by citation (blocks 08–09) |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no order, rule or potential; none is a wall. A reframing that would make the formation law nearest-neighbor Markov is the adoption of an order class with `|A_x| ≤ 1` everywhere — impossible on any window with a plaquette (block 01) — or of a rule that is not of product class (block 01's family G, executed there as inconsistent). Not a new-axiom claim.

### N7 — Steelman
Hostile reviewer: "This is the classical clique theorem plus block 01; the only
new fact is a table of mixed differences." Reply: the classification of the Markov graph of every formation law and the identification of its canonical terms as mixed differences of the normalizers are not in block 01, whose Theorem B compares with one specific law; the plaquette computation shows the difference concretely (the `{a, d}` term vanishes while `{b, c}` does not — the graph, not merely the law, is what the order shapes). Conceded: the classical uniqueness argument is standard; it is re-proved, not imported.

### N8 — Cross-cycle echo
The nearest prior wall is block 01's Theorem B (retired by nothing; strengthened here from equality to the Markov property); blocks 08–09 are the monotone-class instances. No structurally similar wall was retired by a mechanism not considered here.

## Falsifiers
- An order of the plaquette or the star on which T1's product form differs from the product of conditionals (B1).
- A `k ≤ 6` at `(3, 1, 2)` or `(5, 2, 4)` for which every searched mixed-difference ratio equals `1`, or a nonzero ratio at the constant rule (B2, B3).
- A configuration of the plaquette on which `exp Φ_{ad} ≠ 1`, or `exp Φ_{bc} = 1` on all configurations (C1, C2).
- A vanishing three-body term on the star's leaves for all leaf values (C4).
- A pair of adjacent sites inside a recorded set (impossible on `Z^3`; would refute T4's use of bipartiteness).

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
