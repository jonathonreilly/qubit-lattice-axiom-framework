---
claim_id: admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Under the supplied positive six-axis product rule and monotone formation class, for c < 1/3 the constructed infinite laws satisfy the finite-range DLR specification. The explicit single-site formula and full-support conditional uniqueness yield a containing Markov graph; genuine diagonal dependence is conditional on the stated nonzero mixed differences. The eight corner laws are proved distinct at (3,1,2), including the exact opposite-corner witness; no all-parameter opposite-corner distinctness is asserted. Covariance of the family and its equal probability mixture hold throughout c < 1/3. Exact finite-column irreversibility witnesses remain. Ergodic decomposition and broader negative certification are not established here."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06
  - admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
  - admissibility_plane_formation_diagonal_interaction_note_2026-09-08
runner: scripts/admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15.py
---

# The three-dimensional formation law: the face-diagonal specification and eight distinct corner laws at the witnessed triple

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings and on block 08's region; unaudited)

## Result up front

The constructed three-dimensional formation laws have an explicit finite-range
conditional specification. At the witnessed triple `(3,1,2)`, changing a
face-diagonal record changes a site's conditional, and all eight corner laws
are distinct. The full-support conditional lemma and exact kernel witnesses are retained;
the universal static-law exclusion previously inferred from them is deferred. Rotations
permute the corner laws, and their equal mixture is a probability law invariant
under those rotations. This construction supplies no physical selection of an
order or mixture. Exact finite-column joint laws also witness sweep reversal.

Exactly: with `K_3(a, b, c) = Σ_s K(a, s) K(b, s) K(c, s)` and the corner
`κ ∈ {±1}^3`, `μ_κ` is Gibbs for the potential `−log K` on edges and
`+log K_3` on the predecessor triples `{y − κ_i e_i}` (R1); its full
conditional at `x` depends on `x + κ_i e_i − κ_j e_j` (TV
`793975879125/24719290847393` at `(3, 1, 2)` for one change); a full-support
law determines its finite-range specification (L2); the universal exclusion
formerly stated in R2 is deferred; at `(3,1,2)` the
eight `μ_κ` are pairwise distinct (R3; within a point-reflection pair, TV
`1646222697/263752139417` between the conditionals); the `2×2` column's plane
chain is irreversible with `TV(J, J^T) = 0.04934…` at `(3, 1, 2)` and `0` at
the constant rule (R4). Executed with exact arithmetic: 22 checks,
15 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the owner's sequencing gate (2026-08-26): what the Admissibility rule induces on the infinite lattice is unidentified; the campaign's standing question since block 01: formation law versus static law, now on Z^3 itself; the derivation campaign's assembly (#8093): the formation-law node and whether a covariant formation law exists (#8096: no covariant sequential order)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use the explicit DLR specification, containing graph, conditional and TV witnesses, and the covariant probability mixture. Certification of excluded nearest-neighbor Markovity and separation from every static Gibbs law is deferred with its full original proof archived."
conditional_surface_status: "L1 full-exterior DLR identity and R1 containing graph hold in the c<1/3 constructed-law region; explicit diagonal dependence and mixed-ratio witnesses retain their stated hypotheses. R2 universal static-law/graph exclusion is deferred. R3 eight-law distinctness at (3,1,2); family covariance throughout the region; finite R4 witnesses unchanged."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Finite exterior-cylinder identities pass to the limit; L2 is full-support conditional uniqueness; explicit kernels, mixed ratios and finite TV witnesses support the retained constructions. R2 exclusion certification is deferred."
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "No possibility is privileged." — "Records form." — "Only records
are readable."

**Readings carried, named, nothing new adopted.** The records-only reading,
positivity, the six-axis menu with orbit weights `(p, q, r)`, the monotone
class as a supplied order class — all as in blocks 01–05 and 08. New here: the
corner `κ ∈ {±1}^3` of the class is made explicit; the class `𝓜_κ` has
predecessor sets `A^κ_y = {y − κ_i e_i}` and successor sets `{y + κ_i e_i}`;
block 08 treats `κ = (+,+,+)` and every other corner is its image under the
reflection `R_κ : x ↦ (κ_1 x_1, κ_2 x_2, κ_3 x_3)` of the box (its laws are the
images of block 08's). The region is block 08's `c < 1/3`, with
`c = max(c_1, c_2, c_3)` the one-neighbor sensitivity, which does not depend
on `κ`.

**Objects from block 08 (on the stacked branch; proposed, unaudited).** The box
law `μ^κ_B = (1/6) Π_{y ∈ A^κ_x} K(v_y, v_x) / Π_{|A^κ_x| ≥ 2} K_{|A^κ_x|}(v_{A^κ_x})`
(Q1e); the `Z^3` law `μ_κ` for `c < 1/3`, unique, translation invariant, the
limit of the box laws as the corner recedes (Q4e); the plane chain and its
stationary law `π` on a cross-section `C` (Q3); the third difference of
`log K_3` (Q1f): `2160/2197 ≠ 1` at `(3, 1, 2)`, `686196/704969 ≠ 1` at
`(5, 2, 4)`, `1` at the constant rule.

**The static side (block 02, on main).** The nearest-neighbor specification
`γ^S` whose single-site kernel is the rule with all six neighbors recorded,
`γ^S_x(s | ω) = Π_{y ~ x} φ(s, ω_y)/Σ_t Π_{y ~ x} φ(t, ω_y)`; its Gibbs measures
on `Z^3` are the static laws (existence by block 02's Theorem C; uniqueness
where `6c_1 < 1` by block 03; undecided at the silent triples).

**The two-dimensional side (the plane-law note, on main since 2026-09-15;
proposed, unaudited).** The plane law of the top-left class is Gibbs for
`−log K` on axial edges and `+log K^2` on the chosen diagonals; opposite
corners coincide (block 05's P7(a)); the two diagonal classes differ for every
nonconstant triple; the center's conditional given its eight neighbors is not
the static rule.

**Notation.** `G_κ(x) = {x ± e_i} ∪ D_κ(x)`, `D_κ(x) = {x + κ_i e_i − κ_j e_j : i ≠ j}`
(six face-diagonal sites). The three triples containing `x` are
`T^κ_{x + κ_i e_i} = {x, x + κ_i e_i − κ_j e_j, x + κ_i e_i − κ_k e_k}`
(`{i, j, k} = {1, 2, 3}`); their grouping of `D_κ(x)` into three pairs is
`𝒯_κ(x)`. A cylinder is a set fixing finitely many coordinates. A law `μ` on
`M^{Z^3}` has full support if every cylinder has positive `μ`-probability.


### Linked source authority

- [Admissibility Rule Three Dimensional Monotone Formation Law Plane Chain Coupling Region Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md): only its explicit hypotheses and conclusions are used.

- [Admissibility Rule Infinite Strip Row Sweep Formation Law Versus Static Law Bounded Theorem Note 2026-09-06](ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md): the actual predecessor premise, restricted to the quoted theorem hypotheses.
- [Admissibility Plane Formation Diagonal Interaction Note 2026-09-08](ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md): the actual predecessor premise, restricted to the quoted theorem hypotheses.

## Prior art and what is new

Block 01 (on main) classified formation against static laws on finite windows
(equal iff every record forms with at most one recorded neighbor) and re-proved
the Brook ratio lemma; block 02 separated the two on strips by a statistic;
the plane-law note (on main) identified the two-dimensional plane law's Gibbs
potential, proved the two diagonal classes differ, and showed the center's
conditional is not the static rule; block 08 (stacked) built the
three-dimensional law and its region. The time-directed-sweep note of
2026-09-05 (on main) concerns the record-side image of a current under a
supplied sweep on a different object, not the reversibility of the record law.
The classical references — Gibbs specifications and the DLR equations, the
uniqueness of conditional probabilities and of finite measures — are explicit
mathematical imports under Imports; ergodic decomposition is not used.

New here: the Gibbs identification of the three-dimensional law (R1); the
explicit conditional discrepancy and full-support conditional uniqueness (L2); the eight-fold distinctness of the corner
laws and the structure of the covariant family (R3); the irreversibility of the
plane chain and the visibility of the sweep and of the corner in the record
statistics (R4).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| L1: the `Z^3` law is Gibbs for the interior specification | proved (finite conditional identity passed to the limit) |
| L2: a full-support law determines its continuous finite-range specification; `μ_κ` has full support | proved |
| R1: the Markov graph `G_κ`; the dependence on the face-diagonal sites | proved from L1; witness executed at `(3, 1, 2)` (B1–B3) |
| R2 universal static-law and nearest-neighbor graph exclusion | deferred; exact conditional/mixed-ratio witnesses retained |
| R3: covariant orbit and probability mixture; eight distinct laws at (3,1,2) | covariance general in the region; distinctness uses the within-pair witness (C1–C4) |
| R4: irreversibility and the corner's visibility on the `2×2` column | executed at three triples (D1–D4); the `Z^3` statement from R3 |
| R5: the two-dimensional contrast | cited (the plane-law note); the count comparison is restricted to the witnessed setting |
| nonzero third difference at every nonconstant triple | false at the displayed exceptional constructions; no exhaustive claim |
| eight laws outside the witnessed parameter; affine independence | open |

The nonzero third differences at the two declared triples are finite
witnesses. The exceptional-construction note displays nonconstant points with
vanishing third differences; its exhaustive-locus conclusion is deferred.
R3 opposite-corner distinctness remains confined to `(3,1,2)`.

## Lemma L1 — the `Z^3` law is Gibbs for the interior specification

**Statement.** For `c < 1/3` and every corner `κ`, `μ_κ` satisfies the DLR
equations of the specification `γ^κ` with potential `Φ_{xy} = −log K(v_x, v_y)`
on nearest-neighbor edges and `Φ_{T} = +log K_3(v_T)` on the predecessor
triples `T = A^κ_y`, `y ∈ Z^3`: for every finite `Λ` and every configuration
`ω` off `Λ`, `μ_κ(v_Λ | ω) = γ^κ_Λ(v_Λ | ω) ∝ exp(−Σ_{A ∩ Λ ≠ ∅} Φ_A)`, where
the sum runs over the finitely many edges and triples meeting `Λ`.

*Proof.* Let `∂Λ` be the set of sites outside `Λ` that share an edge or a
triple with a site of `Λ` (finite: the reach of the potential from `Λ`). Take
a box `B ⊇ Λ ∪ ∂Λ` whose corner is far enough that every site `y` whose triple
`A^κ_y` meets `Λ` has all three predecessors in `B` — every such `y` lies in
the three-predecessor region of `B`, away from its three coordinate planes.
In block 08's product form of `μ^κ_B`, the factors containing a site of `Λ`
are exactly the edge factors `K(v_x, v_y)` for edges meeting `Λ` and the
normalizers `1/K_3(v_{A^κ_y})` for triples meeting `Λ` (no `K_2`
normalizer meets `Λ`, since those sit on the coordinate planes of `B`). In the
conditional `μ^κ_B(v_Λ | v_{B ∖ Λ})` every factor not containing a site of `Λ`
cancels, leaving `γ^κ_Λ(v_Λ | v_{∂Λ})` exactly. For any fixed exterior cylinder event `E` (supported outside `Λ`), choose the
box also to contain its finite support. Multiplying the conditional identity by
`1_E` and integrating gives
`E_{μ^κ_B}[1_E 1_{v_Λ=a}] = E_{μ^κ_B}[1_E γ^κ_Λ(a | v_{∂Λ})]`.
Both integrands depend on finitely many coordinates. Finite-window convergence
therefore passes this identity to `μ_κ` for every exterior cylinder event.
The exterior cylinders form a generating π-system; equality of the two finite
measures extends to the entire exterior sigma algebra. Thus `γ^κ_Λ` is a
version of the conditional law given the full exterior, which is the DLR
identity. The displayed continuous kernel is defined for every exterior
configuration; conditional-law equality is almost sure. ∎

## Lemma L2 — a full-support law determines its continuous specification

**Statement.** Let `μ` be a law on `M^{Z^3}` with full support, and let `γ`,
`γ'` be two specifications whose single-site kernels `γ_x(s | ω)`,
`γ'_x(s | ω)` depend on `ω` only through finitely many coordinates. If `μ` is
Gibbs for both, then `γ_x(· | ω) = γ'_x(· | ω)` for every `x` and every `ω`.
Moreover `μ_κ` has full support: every cylinder fixing `n` coordinates has
`μ_κ`-probability at least `(min_{k, a, s} r(s | a))^n > 0`.

*Proof.* Both kernels are versions of the conditional probability
`μ(v_x = s | v_{Z^3 ∖ x})`, so they agree `μ`-almost surely. Write
`γ_x(s | ω) = g(ω_N)`, `γ'_x(s | ω) = g'(ω_N)` for a finite `N` containing both
dependency sets. The event `{ω_N : g(ω_N) ≠ g'(ω_N)}` is a finite union of
cylinders of `μ`-probability zero; with full support each cylinder has positive
probability, so the union is empty: `g = g'` on every value of `ω_N`. Full
support of `μ_κ`: under every box law the probability of a cylinder fixing `n`
coordinates is a sum of products of kernel values, each product containing
exactly `n` factors of the fixed sites and the remaining factors summing to
one, so it is at least `δ^n` with `δ = min r(s | a) > 0` over all kernels and
values; the bound passes to the limit. ∎

## Theorem R1 — the Markov graph of the three-dimensional law

**Statement.** For `c < 1/3` and every corner `κ`, the full conditional of
`μ_κ` at `x` is
`γ^κ_x(s | ω) ∝ Π_{y ~ x} K(s, ω_y) / Π_{i=1}^{3} K_3(s, ω_{x + κ_i e_i − κ_j e_j}, ω_{x + κ_i e_i − κ_k e_k})`,
a function of the twelve sites `G_κ(x)`; `μ_κ` is a Markov field for the graph
`G_κ` (edges `x ∼ x ± e_i` and `x ∼ x + κ_i e_i − κ_j e_j`); and the dependence
on each face-diagonal site is genuine: at `(3, 1, 2)`, with all axial neighbors
and the other five diagonal sites at `+x`, changing `ω_{x + e_1 − e_2}` from `+x`
to `−x` changes `γ^κ_x` by total variation `793975879125/24719290847393`
(`0.03211968…`); at every triple where the third difference of `log K_3` is
nonzero, some such change has nonzero effect.

*Proof.* L1 gives the DLR equations; the single-site kernel is the `Λ = {x}`
case, whose potential terms are the six edges at `x` and the three triples
containing `x` (`x ∈ A^κ_y` iff `y = x + κ_i e_i`, with co-members
`y − κ_j e_j = x + κ_i e_i − κ_j e_j`). The Markov property for `G_κ` is the
statement that the kernel depends on `ω` only through `G_κ(x)`. Dependence on
`a = ω_{x + κ_1 e_1 − κ_2 e_2}`: the ratio `γ^κ_x(s | ω)/γ^κ_x(s' | ω)` contains
`K_3(s', a, b)/K_3(s, a, b)` with `b = ω_{x + κ_1 e_1 − κ_3 e_3}` and no other
factor in `a`; it is constant in `a` for all `s, s', b` iff
`log K_3(s, a, b) − log K_3(s', a, b)` is constant in `a`, i.e. iff every
mixed second difference `Δ_s Δ_a log K_3(·, ·, b)` vanishes; a nonzero third
difference `Δ_s Δ_a Δ_b log K_3` (block 08, Q1f) means two of these second
differences differ, so one is nonzero. Executed: the witness above (B1); the
kernel does not depend on the sites `x + e_i + e_j` or `x − e_i − e_j` (B2,
by construction of the formula); the third difference at both declared
triples (B4). ∎

## R2 — retained conditional witnesses; exclusion certification deferred

R1 gives an explicit single-site conditional and the exact nonzero
face-diagonal TV witness at `(3,1,2)`. The third-difference ratios are
`2160/2197` at `(3,1,2)` and `686196/704969` at `(5,2,4)`, with ratio one
at the constant control. L2 supplies the conditional-uniqueness lemma.

The original conclusion excluding nearest-neighbor Markovity and every static
Gibbs law, and its full inference proof, are preserved byte-exact under PR8139
in the history manifest. Their negative certificate remains incomplete and
that universal exclusion is not asserted as a current accepted conclusion.
The constructive DLR identity, containing graph and finite witnesses stand
within their explicit hypotheses.

## Theorem R3 — eight corner laws, one covariant family

**(a) Dependency sets.** `D_κ(x) = D_{κ'}(x)` iff `κ' = ±κ`; the groupings
`𝒯_κ(x)` are pairwise distinct for all eight `κ`.

*Proof.* `D_κ(x) − x = {κ_i e_i − κ_j e_j}`; replacing `κ` by `−κ` negates
every element, and the set is closed under negation (swap `i, j`), so
`D_{−κ} = D_κ`. If `κ' ∉ {κ, −κ}`, some coordinate agrees and some differs, say
`κ'_1 = κ_1`, `κ'_2 = −κ_2`; then `κ_1 e_1 − κ_2 e_2 ∈ D_κ − x` but the
`(1, 2)`-type elements of `D_{κ'} − x` are `±(κ_1 e_1 + κ_2 e_2)`, so the sets
differ. The grouping of `κ` pairs `κ_i e_i − κ_j e_j` with `κ_i e_i − κ_k e_k`
(common first index `i`); for `−κ` the same two elements are `−κ_i e_i + κ_j e_j`
and `−κ_i e_i + κ_k e_k`, which in the grouping of `−κ` have common first
indices `j` and `k` respectively, so they are in different groups. Executed for
all eight corners (C1, C2). ∎

**(b) Distinctness at the witnessed triple.** At `(p,q,r)=(3,1,2)`, where
`c < 1/3`, the eight laws `μ_κ` are pairwise distinct. The following proof
does not assert opposite-corner distinctness at every nonzero-third-difference triple.

*Proof.* For `κ' ∉ {κ, −κ}` pick `z ∈ D_κ(x) ∖ D_{κ'}(x)`: `γ^κ_x` depends on
`ω_z` (R1; the witness at `(3, 1, 2)` is the `(1, 2)`-type site, and the other
types follow by the axis symmetry of block 08's Q1c) while `γ^{κ'}_x` does not;
by L2, `μ_κ ≠ μ_{κ'}`. For `κ' = −κ` the dependency sets coincide and the
groupings differ; the two kernels are different functions of the same twelve
sites: at `(3, 1, 2)`, with all axial neighbors `+x` and the diagonal values
`(+x, +x, +y, −x, +y, −x)` on `(x+e_1−e_2, x+e_1−e_3, x+e_2−e_1, x+e_2−e_3, x+e_3−e_1, x+e_3−e_2)`,
`γ^{+++}_x` and `γ^{−−−}_x` differ by total variation
`1646222697/263752139417` (`0.00624155…`, the maximum over the `6^6` diagonal
assignments with these axial values; C3), so `μ_{+++} ≠ μ_{−−−}` by L2, and
by the reflection symmetry every point-reflection pair is a reflected copy of
this one. ∎

**(c) The covariant family.** The 24 proper cubic rotations act on the eight
corners transitively, and a rotation `g` maps `μ_κ` to `μ_{gκ}` (it maps the
class `𝓜_κ` to `𝓜_{gκ}` and the rule is covariant). The stabilizer of a corner
is the three-fold rotation group about its body diagonal, under which `μ_κ` is
invariant (block 08's axis symmetry, Q1c). At `(3,1,2)`, (b) excludes every
other proper rotation. Throughout `c < 1/3`, the equal mixture
`μ̄ = (1/8) Σ_κ μ_κ` is a probability law invariant under all proper cubic
rotations, axis reflections and translations: these transformations permute
its summands. This is a mathematical construction; the supplied axioms do not
select its physical adoption. Single-site covariance decay alone does not
prove full translation mixing or an eight-component ergodic decomposition;
no such decomposition is claimed here. ∎

## Theorem R4 — the imprint of the sweep

**(a) On `Z^3` at the witnessed triple `(3,1,2)`.**
`μ_κ` is not invariant under the reflection of any single axis, nor under any
product of reflections other than the identity: the reflection `R` of the axis
`i` maps `μ_κ` to `μ_{κ'}` with `κ'_i = −κ_i`, a different law by R3(b). In
particular the reflection of the sweep axis `e_1` changes the law: the finished
record field distinguishes the direction in which its planes formed.

**(b) On the `2×2` column, exactly.** Let `π` be the stationary plane law and
`J(w, v) = π(w) P(w, v)` the two-plane joint law (block 08, Q3). The reversed
sweep (`κ_1 ↦ −κ_1`, the in-plane structure unchanged) has the law of the
reversed chain, whose two-plane joint law is `J^T`. At `(3, 1, 2)`
`TV(J, J^T) = 0.04934116…` (an exact rational, printed under `--exact`); at
`(5, 2, 4)` `0.0311…`; at the constant rule `0` (D1). The one-plane law is the
same for both sweep directions (the same transfer matrix), so the sweep
direction is visible only in the joint law of consecutive planes. The in-plane
reflection `x_2 ↦ 1 − x_2` of the cross-section changes the one-plane law:
`TV(π, π ∘ R_2) = 0.02177093…` at `(3, 1, 2)`, `0` at the constant rule (D2).
The eight predecessor structures on the `2×2` column give exactly four distinct
one-plane laws, paired by the sweep direction (D3); the eight column laws are
pairwise distinct (the four one-plane laws, each split by the joint law's
asymmetry, D4).

*Proof of (b).* The reversed class's column law is the image of the column law
under `x_1 ↦ −x_1`; the image of a stationary chain is the reversed stationary
chain, with transition `P^*(v, w) = π(w) P(w, v)/π(v)` and joint law `J^T`; the
two column laws coincide iff `J = J^T`. The in-plane reflection maps the class
`(κ_1, κ_2, κ_3)` to `(κ_1, −κ_2, κ_3)`, whose transfer matrix is the reflected
one; its stationary law is `π ∘ R_2`. ∎

**(c) What this is and is not.** The imprint is that of a supplied order: the
monotone class comes with a corner and a sweep, and the finished records
remember both. No arrow of time follows: the axioms supply no order, and a
covariant construction (the equal mixture, or a covariant random order) has no
such imprint by construction. At the witnessed triple each of the eight supplied classes leaves a
distinct record law. This statement is not extended to every parameter triple.

## R5 — two dimensions for contrast (cited)

In two dimensions (the plane-law note, on main) the point reflection maps the
top-left class to the bottom-right one and preserves both the diagonal pair set
and its grouping (pairs, not triples), so opposite corners coincide (block 05's
P7(a)) and there are two laws, distinguished by the axis reflections. In three
dimensions the point reflection preserves the dependency set but not its
grouping into triples (R3a); at `(3,1,2)` the independent conditional witness
then proves eight distinct laws. Different groupings alone do not prove distinctness. The two-dimensional analogue
of the conditional witness is the plane-law note's statement that the center's conditional given
its eight neighbors is not the static rule.

## No-Go Discipline Gate — deferred broader certification

This revision retains the constructive identities, quantitative bounds and named
finite witnesses above. It does not certify the broader exclusion claims in the
original packet. The original N1–N8 text and every recovery route are preserved
byte-exact in [the PR8146 history manifest](work_history/review_loop/pr8146/original-manifest.json)
under PR8139; the original branch remains a recovery handle for unlanded work.

### N1 — Route coverage
The specifically deferred conclusions are R2 exclusion of nearest-neighbor
Markovity and separation from every static Gibbs law.
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

- A configuration at `(3, 1, 2)` on which `γ^{+++}_x` does not change when
  `ω_{x + e_1 − e_2}` changes with everything else at `+x` (the executed total
  variation would vanish; refutes R1's witness).
- A corner `κ' ∉ {κ, −κ}` with `D_{κ'}(x) = D_κ(x)`, or two corners with the
  same triple grouping (refutes R3(a)).
- Equality of `γ^{+++}_x` and `γ^{−−−}_x` on all `6^6` diagonal assignments
  with axial values `+x` at `(3, 1, 2)` (refutes the within-pair witness).
- `J = J^T` on the `2×2` column at `(3, 1, 2)`, or `π = π ∘ R_2` there (refutes
  R4(b)); a nonzero value at the constant rule (refutes the control).
- A box and a window on which the box law's conditional is not `γ^κ_Λ` although
  the window's reach lies in the three-predecessor region (refutes L1's finite
  identity).

## Boundaries and non-claims

This note describes the monotone class with a corner on `Z^3` in block 08's
region; it states nothing about the static law's uniqueness, nothing for
`c ≥ 1/3`, nothing about a physical order or corner, and derives no arrow of
time — the imprint of the sweep is that of a supplied order. No plane, bridge,
Born or gravity statement enters this note; this note does not fire wake
condition 1 of the parked statistical-bridge decision. The Gibbs–DLR
formalism, the uniqueness of conditional probabilities and finite-measure uniqueness theorem are mathematical inputs at the stated
scope; no ergodic decomposition is claimed.

Further: the third difference is executed at two triples, not proved nonzero
at every nonconstant triple; the within-pair witness is at `(3, 1, 2)` only
(the other pairs follow by reflection at that triple); the `2×2` column is the
only exact surface for R4(b); the affine independence of the eight laws and the
uniqueness of the covariant law in their convex hull are not claimed; the
random-priority law's Markov structure is not analyzed.

## Imports

- `minimal_axioms` (the framework premise node): the sentences quoted under
  Premises.
- Block 08 (stacked; proposed, unaudited): the `Z^3` law, product form,
  region, decay, plane chain. Block 02 (on main): the static specification. The
  plane-law note (on main): the two-dimensional contrast.
- Re-proved at scope: L1 (a finite conditional identity passed to the limit),
  L2 (uniqueness of finite-range kernels under full support), R1 and the
  stated finite R3–R4 witnesses; R2 exclusion certification is deferred.
- Mathematical imports: existence and almost-sure uniqueness of conditional
  probabilities on finite-alphabet countable product spaces; uniqueness of
  finite measures agreeing on a generating π-system, used to extend the
  exterior-cylinder identity to the full exterior sigma algebra. Finite range
  makes the tested functions cylinder functions; positivity gives full support
  for the pointwise comparison. These are probability theorems, not definitions.
- The pointwise ergodic theorem and ergodic decomposition are not used here.

## Review record

Supervisor-run block (owner directive 2026-09-15: no subagents). The control
(`specs/supervisor_control_block09_markov_corner_arrow.py`) computed the
dependence witness, the eight dependency sets and groupings, the within-pair
witness, the irreversibility and in-plane-reflection total variations, and the
four one-plane laws before the contract; the lens pass is in `GOAL_block09.md`;
the primary seat wrote the lemmas and the runner; the refuting pass
(`CHECKER_block09_findings.md`) recomputed the witnesses by disjoint routes;
the fold is in `REVIEW_HISTORY.md`. Facts settled while executing: the runner's decimal comparisons were
replaced by exact rational literals (the source float-scan flags decimal
strings); a phrase stating that no arrow is derived collided with a
forbidden token by substring and was reworded; the plane-law note landed on main on
2026-09-15, so the stack was rebased onto that main to carry it as a declared
input.

## Verification

```bash
python3 scripts/admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15.py
python3 scripts/admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15.py --exact
python3 scripts/admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15.py --mutation joint_law_symmetric_claimed
```

Families: A authority and inputs; B the Markov graph (the dependence witness,
the excluded sites, the third difference); C the eight corners (sets,
groupings, the within-pair witness, the transitivity of the rotations); D the
`2×2` column (irreversibility, the in-plane reflection, the four one-plane
laws, the eight column laws); F fences, forbidden phrases, the floating-point
self-scan and the placement of the classical names; G the resolution lines.
Each of the 15 declared mutations perturbs one object or one comparison and
fails in exactly one family; `--exact` prints the exact total variations.
Expected final line: `TOTAL: PASS=22 FAIL=0`.
