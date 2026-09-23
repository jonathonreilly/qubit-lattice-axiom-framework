---
claim_id: extended_explanation_tree_finite_witness_counts_and_rational_recursion_certificates_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Exact finite marked-automaton constructions and charge identities for the declared explanation-tree algorithm: counts 16/10/1, 20/12/1, 23/12/2, exact consecutive periods 2/1/1 and local neutral arithmetic; four exact rational polynomial super-solutions and completed-square maximum. No global sharpness, universal upper budget, physical formation threshold or completed negative certification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/extended_explanation_tree_finite_witness_counts_rational_certificates_check_2026_09_16.py
---

# Finite explanation-tree witness counts and rational recursion certificates

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support; declared finite combinatorics and arithmetic, unaudited.
**Primary:** [exact finite checks](../scripts/extended_explanation_tree_finite_witness_counts_rational_certificates_check_2026_09_16.py).
**Cache:** [source-bound execution evidence](../logs/runner-cache/extended_explanation_tree_finite_witness_counts_rational_certificates_check_2026_09_16.txt).
**Recovery:** [full original history and deferred science](work_history/review_loop/pr8175/README.md).

## Result up front

Three explicit finite constructions have ratios 8/5, 5/3, 5/3 and consecutive
local-period counts 2, 1, 1. A two-refinement neutral period has `(r,e,a)=(0,4,2)`.
That local identity does not decide a global sharp constant. All witness marks,
algorithmic steps, accounting identities and rational certificates are retained.
The full corrected negative argument is readable in the recovery packet with
formal certification deferred; incomplete N1 coverage is not a mathematical
refutation. No primary, random-cone fixture or mutation was run during author
preparation. The expected primary count remains 20 checks; its new exact
per-witness period target replaces the former aggregate-only check.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite witness accounting and rational recursion arithmetic"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "original-reviewer affected confirmation and exact-source bounded evidence; global conclusions remain deferred"
conditional_surface_status: "explicit finite construction and algebraic identities only; no open handoff used as theorem authority"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axioms memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework context:
one fixed covariant nearest-neighbor rule; conditional probabilities vary
with nearest-neighbor conditions; records form; only records are readable.
It does not select the marked automaton, tree algorithm or weights below.
The primary also pins and reads the context-only finite product-law note
`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`.
No theorem from that note is needed by the finite construction. The historical
open handoffs are archived provenance, not mathematical authority. The
polynomial recursion and six-menu arithmetic are defined explicitly here.

Declared objects.
- **Level time and the one-sided automaton.** Sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`. A **noise set** `ζ` is a set of sites; the automaton sets `η_x = 1` if at least two of `η_{x−e_j}` are `1`, and otherwise `η_x = 1` if and only if `x ∈ ζ`; sites outside the window are `0`. This is a declared deterministic marked automaton; no probabilistic domination or selected physical rule is assumed. A **seed** is a 1-site with no 1-predecessor, an **amplified site** one with exactly one (its **direction** `j` is the index of that predecessor), a **processed-type site** one with at least two; the **winning pair** of a processed-type site is its two 1-predecessors of smallest index.
- **The graph `G`, the functionals, the excuse, bad pairs.** Arrows `{x, x − e_j}`, forks `{x, x ± (e_i − e_j)}`; `M_k(z) = z_k − τ(z)/3`; for a processed-type `v`, `Excuse_k(v)` is the winning-pair member with index `≠ k` (the smaller if both); for an amplified `v` with direction `j`, `Excuse_k(v) = v − e_j` for every `k`; the pair `(v, k)` is **bad** if `v` is amplified with direction `k`.
- **Clusters, poles, refinements — declared construction.** At level `s` the clusters are the level-`s` parts of the components of the graph on 1-sites of levels `≤ s` with an edge from each processed-type or amplified site to each of its 1-predecessors. A cluster carries three **poles** `(p_0, p_1, p_2)` (the root's cluster `{x}` with poles `(x, x, x)`); a **refinement** of a cluster `K` with poles `p_k` takes the excuses `u_k = Excuse_k(p_k)`, the clusters of the 1-predecessors of `K`, one representative fork between each pair of these clusters that a fork joins, and the minimal tree of clusters and forks connecting the clusters of `u_0, u_1, u_2`; each cluster of that tree receives the poles `u_k` it contains and, for the other charges, the endpoint of the fork toward the cluster of `u_k`; the forks of the tree become tree edges. A pole is **kept** if it is incident to an existing tree edge or is a bad amplified pole for its charge (the first pole if none is); a kept processed-type pole `v` with charge `k` gets the **excuse arrow** `{v, u_k}`, a kept amplified pole the **amplification arrow** to its single 1-predecessor. Seeds are singleton clusters and end the recursion.
- **The potential and the log.** `Span(K) = Σ_k M_k(p_k)`; `Φ = Σ_{unprocessed clusters} Span + #forks`, `Φ = 0` at the start. The construction's **log** records, at each refinement, `(b, kept, a, e, f, r, d)`: bad pairs, kept poles, amplified and processed-type kept poles, forks created, the rise `r = 1 − b + Σ_{forks created}(1 − Span(fork))` of `Φ`, and the number of distinct poles.
- **Finite counts.** `F=#forks`, `E=sum e`, `|A|=sum a`; for the explicitly reconstructed trees these equal distinct edge/node counts. The arithmetic ratio is `(E-3(|S|-1))/|A|` when `|A|>=1`. No universal budget is imported.
- **The witnesses.** `W1`: window `[0,4)²×[0,7)`, root `(3, 3, 4)`, marks `(0,0,0), (0,0,1), (0,1,0), (1,0,0), (1,0,2), (1,2,0), (1,3,1), (2,0,0), (2,2,3), (2,3,4), (3,0,2)`. `W2`: the same window, root `(3, 3, 6)`, the forty marks listed in the runner. `W3`: window `[0,5)²×[0,9)`, root `(4, 4, 5)`, the seventy-four marks listed in the runner.
- **Declared polynomial recursion.** `D=(1+xU)^2(1+3xD)(1+yF)^6`, `U=(1+xU)^3(1+yF)^6`, `F=(1+xU)^3(1+3xD)(1+yF)^5`, `R=(1+xU)^3(1+3xD)(1+yF)^6`. A rational triple `(Dbar,Ubar,Fbar)>=1` is a super-solution when it dominates the three right sides. Here `x=t+epsilon_2/t`, `y=epsilon_1/t^3` are declared algebraic weights only. No probability or formation threshold follows from a certificate.

## Theorem T1 — accounting identities and local period



**T1.1 (increments).** For an amplified `v` with direction `j`, `M_k(v − e_j) − M_k(v) = 1/3 − δ_{jk}`; for a processed-type `v`, `M_k(Excuse_k(v)) − M_k(v) = 1/3`. *Proof.* `τ` drops by one along either arrow; the coordinate `k` drops by one exactly when the arrow's direction is `k`. ∎

**T1.2 (the rise).** At a refinement of `K` with `b` bad pairs, `Σ_{clusters of the tree} Span + Σ_{forks of the tree} Span(fork) = Span(K) + 1 − b` (the pole-assignment identity justified below); hence `Φ` rises by `r = 1 − b + Σ_{forks created}(1 − Span(fork))`, which is `1 − b` at a fork-free refinement and at most `1 − b + f` when each created fork has nonnegative span; that condition is checked on the three finite witnesses, not imported as a universal construction theorem. Since `Φ = 0` at the start and `Φ = #forks` at the end (seeds are singleton clusters with `Span = 0`), `Σ_i r_i = F`. Trivially `Σ_i e_i = E`, `Σ_i a_i = |A|`, `b_i ≤ a_i` (a bad pole is amplified and kept) and `e_i + a_i ≤ 3`. The three witness logs satisfy these identities (B2); the runner also checks equality of accumulated counts with independently recounted distinct edges/nodes. For a general refinement history, the telescoping assertion is conditional on termination at singleton seeds and the stated pole assignment, not an existence theorem for all marked inputs.

**T1.3 (the two-level period).** A fork-free refinement keeping three processed-type poles has `b = 0`, `r = 1`, `e = 3`, `a = 0`; a fork-free refinement keeping two bad amplified poles and one processed-type pole has `b = 2`, `r = −1`, `e = 1`, `a = 2`. Their sum has `r = 0`, `e = 4`, `a = 2`: the pair leaves the potential where it was and spends four excuse arrows on two amplified nodes, `(e − 3r)/a = 2`. *Proof.* T1.2 with `f = 0`. ∎ The exact consecutive-period counts in `(W1,W2,W3)` are `(2,1,1)` (B3), four in total. The equality is local arithmetic; arbitrary repetitions and a sharp global ratio are not asserted.

**Pole-assignment proof.** Regard the finite cluster/fork incidence tree as an abstract tree. For each charge k, the terminal is the cluster containing its excuse u_k; every other vertex takes the intersection point on its first edge toward that terminal. Remove a leaf vertex not carrying all terminals. For each charge whose terminal is outside the leaf, the leaf's assigned point is its unique edge intersection q. For charges with terminal in the leaf, the adjacent vertex currently carries q, and deleting the leaf transfers their terminal value to that neighbor. Thus the change in the sum over all vertices for all charges is `sum_k M_k(q)=0`. Repeating leaf removal reduces the sum to `sum_k M_k(u_k)`. The coordinate calculation in T1.1 makes this `Span(K)+1-b`. Subtracting old cluster span and adding one to the fork counter per new fork gives the exact rise formula. Summing these actual potential differences gives the terminal potential minus the initial potential. At a singleton seed all three poles coincide, so their span is zero. This proves the stated identity under the explicit finite refinement conditions without importing the separate global budget.

## Theorem T2 — three exact finite constructions

The complete marks and deterministic construction are specified above and in
the linked primary. Reconstruct the automaton in increasing level order,
choose the first two live predecessor indices at each processed site, and
apply the declared cluster/pole algorithm. Recount edges and nodes separately.
The resulting finite identities are:

| Witness | E | amplified nodes | seeds | forks | ratio | consecutive periods |
|---|---:|---:|---:|---:|---|---:|
| W1 |16|10|1|0|8/5|2|
| W2 |20|12|1|0|5/3|1|
| W3 |23|12|2|1|5/3|1|

**Proof by explicit finite construction.** W1 has 27 nodes, 10 refinements and 10 bad
pairs; W2 has 33 nodes, 12 refinements and 12 bad pairs; W3 has 37 nodes, 13 refinements,
12 bad pairs and one fork. Every excuse arrow joins a processed-type live
site to a live predecessor, each amplification arrow joins a site with exactly
one live predecessor to that predecessor, and each seed has no live predecessor.
The point graph contains the root, is connected and has one fewer edges than
vertices, hence is a tree. All vertices are live sites. W1's eleven marks
are exactly its seed and ten amplified sites. These are finite claims verified
by the explicit algorithm and independently recounted witness records;
B2/B3/C1/C2/C5 reconstruct and test them, rather than assume a global theorem.
Subtracting the integer counts gives `E-3(|S|-1)-|A|=(6,8,8)` and
`3(|S|-1)+2|A|-E=(4,4,4)`; the ratios in the table follow by division. ∎

*Reading of the witnesses.* W1's log is `(0,1,0,1)`, `(1,2,1,1)`, `(0,2,0,2)`, `(1,3,1,2)`, `(0,3,0,3)`, `(2,3,2,1)`, `(0,3,0,3)`, `(2,3,2,1)`, `(1,3,1,2)`, `(3,3,3,0)` in `(b, kept, a, e)`: the root's single arrow, a bad pole appearing beside it, the width growing to three poles, then two periods of T1.3, and the bottom refinement with three bad poles all pointing at the seed. The three-pole width is sustained because the two amplification arrows of a two-bad refinement land on processed-type sites that are kept at the next level, and that level's three excuse arrows land on two amplified sites and one processed-type site — the excuse rule (the smaller index of the winning pair) and the one-sided rule's forced ones cooperate to keep three distinct poles incident without any fork.

The fixed seeded sample in C4 has 300 cones of depths 3 through 8 and four integer
noise percentages. Its resulting maximum is a property of that sample only.
It does not provide an upper bound over all inputs or demonstrate uniform
search coverage. The historical 40,000-cone search, candidate collapse,
hill-climbs and refuter outputs are fully archived; none is rerun in preparation.
The global negative inference from these counts is preserved separately with
explicit incomplete formal certification, not promoted by this finite table.

## Theorem T3 — rational polynomial certificates

For positive supplied `(p,q,r)`, define purely rational quantities
`d1=1-p^3/(p^3+q^3+4r^3)`,
`d2=1-p^2 q/(pq(p+q)+4r^3)`,
`d3=1-p^2 r/(r(p^2+q^2)+r^2(p+q)+2r^3)` and
`epsilon_1=d1`, `epsilon_2=max(d2,d3)`.
These may also be computed by enumerating the six signed coordinate axes:
weights p for equal values, q for opposite values on the same axis, and r
for perpendicular axes, taking predecessor triples `(a,a,a)`, `(a,a,-a)`
and `(a,a,b)` with b perpendicular to a. Summing the six products gives
exactly the three displayed denominators; dividing the target a product by
each sum gives the stated deviations. This defines the algebra without an
imported menu theorem or a probability domination claim.

At each tuple below, `(t,Dbar,Ubar,Fbar)` is an exact super-solution for the
declared recursion with `x=t+epsilon_2/t`, `y=epsilon_1/t^3`:

```python
{
        (453, 1, 2): (Fraction(77, 1000), Fraction(530590310409, 62500000000), Fraction(2581678475343, 1000000000000), Fraction(11343276538931, 1000000000000)),
        (232, 1, 1): (Fraction(19, 250), Fraction(3177134369, 390625000), Fraction(2565214474763, 1000000000000), Fraction(10810979357851, 1000000000000)),
        (905, 2, 4): (Fraction(39, 500), Fraction(8819680764063, 1000000000000), Fraction(2607018650019, 1000000000000), Fraction(2955282963089, 250000000000)),
        (677, 1, 3): (Fraction(77, 1000), Fraction(8860200884553, 1000000000000), Fraction(1306536163573, 500000000000), Fraction(5937627036121, 500000000000)),
    }
```

Here `Fraction(n,d)` denotes the exact rational n/d. Substitute each tuple
into the four finite products above. Clearing their positive denominators
verifies `Dbar>=rD`, `Ubar>=rU`, `Fbar>=rF`, the three values at least 1,
`x<4/27`, and `epsilon_1 Rbar<1/100000`; D1 checks these exact inequalities.
Independent original review recomputed the six-menu deviations and expanded
all binary port choices, rather than using the same closed forms.

The elementary identity
`t(4/27-t)=4/729-(t-2/27)^2`
proves its maximum on `[0,4/27]` is `4/729`, attained at `2/27`.
Direct rational substitution gives `d3(367,1,2)>4/729>d3(368,1,2)`.
The four comparison ratios `4165/453`, `2085/232`, `8330/905`, `6247/677`
each lie strictly between 8 and 10 by cross multiplication (D2/D3).
These are arithmetic comparisons, not validated old/new formation regions.
The original conditional probability interpretation requires a separate
construction/count theorem and the budget discussed in deferred science;
no such theorem or threshold is imported here. ∎

## No-Go Discipline Gate — DEFERRED applicability record

N1 is incomplete for formal negative certification. Witness validity and
implementation agreement are concrete finite tests; global compensation is
addressed only by the exhibited arithmetic. A different construction is
outside scope; attainment of a global constant 2 is unproved; certificate
arithmetic is a separate question. These are not five closed attack families.
N2: no repository wall is imported. N3: marked inputs, outside-zero window,
winning-pair rule, pole assignment and polynomial weights are explicit.
N4: the axioms are framework context, product-law source is context-only,
and historical handoffs have no theorem authority. N5: finite sites and
refinements are executed by the primary when captured; no spectral modes or
infinite lattice are executed. N6: preserve original branch and full negative
proof as deferred science. N7: the global constant may still improve below 2;
the local period does not force a change of construction. N8: a seeded sample
maximum does not imply a worst-case bound; earlier historical claims remain
recovery, not repeated authority.

## Boundaries and non-claims

This note retains exact finite construction counts, local charge identities and rational polynomial certificates for explicitly declared objects; no physical rule, order or coupling is selected.

A local ratio-two period does not establish a sharp global constant; the universal upper budget is not imported from an open handoff.

Formal negative certification is deferred in the readable recovery argument; finite witness validity is not a claim of five closed attack families.

## Imports

Finite graph connectivity, a finite tree's edge count, rational arithmetic,
and a completed-square identity suffice. The declared pole-assignment identity
is proved at scope. No global probabilistic domination, formation threshold,
physical identification or accepted no-go wall is imported. Historical
sampling and search outputs remain in their original exact recovery files.

## Verification

Expected output is `TOTAL: PASS=20 FAIL=0`: four input checks, three accounting,
five finite witness/sample checks, three certificate checks, four packaging
checks and one resolution-report check. There are ten mutation definitions,
including a new targeted period-count corruption; this is a source census,
not a new execution result. The primary writes stdout only. The unchanged
seeded 300-cone fixture is finite evidence, not an exhaustive theorem.

```bash
python3 scripts/extended_explanation_tree_finite_witness_counts_rational_certificates_check_2026_09_16.py
python3 scripts/extended_explanation_tree_finite_witness_counts_rational_certificates_check_2026_09_16.py --list-mutations
python3 scripts/extended_explanation_tree_finite_witness_counts_rational_certificates_check_2026_09_16.py --mutation period_counts_wrong
```
