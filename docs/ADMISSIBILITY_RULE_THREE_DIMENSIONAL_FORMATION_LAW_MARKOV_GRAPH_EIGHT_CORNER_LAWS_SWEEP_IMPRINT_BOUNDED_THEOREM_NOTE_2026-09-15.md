---
claim_id: admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule of orbit weights (p, q, r), under the records-only reading, for the monotone class with corner kappa in {+1,-1}^3 (predecessors x - kappa_i e_i) in the region c < 1/3 of the three-dimensional formation-law note (block 08): (R1) the Z^3 formation law mu_kappa is a Gibbs measure for the finite-range specification with potential -log K on nearest-neighbor edges and +log K_3 on the predecessor triples (proved by passing the finite-box conditional identity to the limit), hence a Markov field for the graph G_kappa of six axial and six face-diagonal neighbors x + kappa_i e_i - kappa_j e_j, and its full conditional depends on those face-diagonal sites (exact witness at (3,1,2): total variation 793975879125/24719290847393); (R2) a law with full support determines its continuous finite-range specification (proved), so mu_kappa is not a Markov field for the nearest-neighbor graph and differs from every Gibbs law of block 02's nearest-neighbor static specification on Z^3, unique or not, at every triple in the region where the third difference of log K_3 is nonzero (executed at (3,1,2), (5,2,4)); (R3) the eight corner laws are pairwise distinct: the four point-reflection pairs have four distinct dependency sets (proved), and within a pair the conditionals differ (exact witness at (3,1,2): total variation 1646222697/263752139417); they form one orbit of the proper cubic rotations, each law invariant only under the three-fold rotations about its own body diagonal, and their equal mixture is proper-cubic covariant and translation invariant but not translation-ergodic; (R4) the sweep leaves an imprint: on the 2x2 column the stationary plane chain is not reversible (total variation between the two-plane joint law and its transpose 0.04934... at (3,1,2), 0.031... at (5,2,4), 0 at the constant rule), the one-plane law is not invariant under the in-plane reflection (0.02177...), and the eight predecessor structures give exactly four one-plane laws, the sweep direction being visible only in the joint law; on Z^3 in the region the law is not invariant under the reflection of any axis (from R3). (R5) Two dimensions for contrast (the landed plane-law note): two laws, the point reflection preserving the diagonal pairs. No order or corner is selected as physical; no arrow of time follows (the imprint is that of a supplied order); nothing about the static law's uniqueness; nothing for c >= 1/3; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06
  - admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
  - admissibility_plane_formation_diagonal_interaction_note_2026-09-08
runner: scripts/admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15.py
---

# The three-dimensional formation law is a Markov field for the face-diagonal graph, not the nearest-neighbor one: eight distinct corner laws and the imprint of the sweep

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings and on block 08's region; unaudited)

## Result up front

Take the three-dimensional pattern law of the previous note — records laid
down on the lattice, each site waiting for the three sites behind it — in the
range of rule settings where that law is well defined. Ask what a site knows
about the rest once everything else is fixed. Under the static law, a site
listens only to its six nearest neighbors. Under the formation law it also
listens to six sites one step diagonally across a face, the ones that shared a
"behind" relation with it, and this extra listening is genuine (an exact
witness). Because a law that gives every pattern a positive chance is pinned
down by what its sites listen to, the formation law can never be a static law,
whether or not the static law is unique at that setting. The same reasoning
shows that the eight ways of choosing "behind" (the eight corners of a cube)
give eight different laws, none of them invariant under the rotations of the
lattice, though the eight together are permuted by those rotations and their
equal blend is invariant. And the direction of the sweep leaves a trace: on a
narrow column the joint law of two consecutive layers is not symmetric under
exchanging them, so past and future along the sweep can be told apart from the
finished records — the trace of a supplied order, not a derived arrow of time.

Exactly: with `K_3(a, b, c) = Σ_s K(a, s) K(b, s) K(c, s)` and the corner
`κ ∈ {±1}^3`, `μ_κ` is Gibbs for the potential `−log K` on edges and
`+log K_3` on the predecessor triples `{y − κ_i e_i}` (R1); its full
conditional at `x` depends on `x + κ_i e_i − κ_j e_j` (TV
`793975879125/24719290847393` at `(3, 1, 2)` for one change); a full-support
law determines its finite-range specification (R2), so `μ_κ` is not a
nearest-neighbor Markov field and differs from every static Gibbs law; the
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
next_trace_action: "the formation law of the monotone class on Z^3 is now separated from every static law by its Markov graph, and the covariant object of the class is the mixture of eight laws, not a law; next: the random-priority law's Markov structure and its relation to the mixture; consumers: the campaign's queue, #8093's assembly (the formation-law node: 'clause-needed' for a covariant single law), the parked statistical-bridge material (read-only)"
conditional_surface_status: "exact on the declared menu and triples; R1–R2 proved for every corner and every triple in block 08's region with the witness executed at (3,1,2) and the third difference at (3,1,2), (5,2,4); R3 proved (dependency sets) with the within-pair witness executed at (3,1,2); R4 executed on the 2x2 column at three triples and proved on Z^3 through R3; R5 cited; conditional on the records-only reading, positivity, the six-axis menu, the monotone class as supplied conditions and on block 08's region"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "R1 passes a finite conditional identity to the limit; R2 is a two-line uniqueness argument for full-support laws; R3 combines R2 with exact finite witnesses and the transitivity of the rotation group on the corners; R4 is exact finite computation on the 2x2 column plus R3; every number is an exact rational; nothing is claimed outside block 08's region"
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
uniqueness of conditional probabilities, ergodic decomposition — are named here
and under Imports and re-proved at scope where load-bearing.

New here: the Gibbs identification of the three-dimensional law (R1); the
separation from every static Gibbs law on `Z^3` through the Markov graph and a
full-support uniqueness lemma (R2); the eight-fold distinctness of the corner
laws and the structure of the covariant family (R3); the irreversibility of the
plane chain and the visibility of the sweep and of the corner in the record
statistics (R4).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| L1: the `Z^3` law is Gibbs for the interior specification | proved (finite conditional identity passed to the limit) |
| L2: a full-support law determines its continuous finite-range specification; `μ_κ` has full support | proved |
| R1: the Markov graph `G_κ`; the dependence on the face-diagonal sites | proved from L1; witness executed at `(3, 1, 2)` (B1–B3) |
| R2: not nearest-neighbor Markov; differs from every static Gibbs law | proved from L2 + R1 at every triple with nonzero third difference; executed at `(3, 1, 2)`, `(5, 2, 4)` (B4) |
| R3: eight distinct laws; the covariant orbit; the mixture | proved (dependency sets; transitivity); within-pair witness executed (C1–C4) |
| R4: irreversibility and the corner's visibility on the `2×2` column | executed at three triples (D1–D4); the `Z^3` statement from R3 |
| R5: the two-dimensional contrast | cited (the plane-law note); the count `2` versus `8` explained |
| the third difference nonzero at every nonconstant triple; the eight laws' distinctness outside the region; affine independence of the eight laws | open; not this note |

The strongest missing lemma is that the third difference of `log K_3` is
nonzero at every nonconstant triple (executed at two); R2 and R3 are stated
at triples where it is nonzero.

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
cancels, leaving `γ^κ_Λ(v_Λ | v_{∂Λ})` exactly. Hence, for every such box,
`μ^κ_B(v_Λ, v_{∂Λ}) = γ^κ_Λ(v_Λ | v_{∂Λ}) μ^κ_B(v_{∂Λ})` for every pair of
configurations on `Λ` and `∂Λ` — a finite identity among the values of the
marginal of `μ^κ_B` on the finite window `Λ ∪ ∂Λ`. As the corner recedes,
these marginals converge to those of `μ_κ` (block 08, Q4e), so the identity
holds for `μ_κ`; since `γ^κ_Λ` depends on the outside only through `∂Λ`, this
is the DLR equation. ∎ (The two-dimensional version is the plane-law note's
"positive finite-range identification"; the argument is the same one dimension
up, with triples in place of diagonal pairs.)

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

## Theorem R2 — the formation law is not a static law on `Z^3`

**Statement.** For `c < 1/3`, every corner `κ`, and every triple at which the
third difference of `log K_3` is nonzero (executed: `(3, 1, 2)`, `(5, 2, 4)`),
`μ_κ` is not a Markov field for the nearest-neighbor graph, and `μ_κ ≠ ν` for
every Gibbs measure `ν` of the static specification `γ^S` — whether the static
law is unique or not.

*Proof.* `μ_κ` has full support (L2) and is Gibbs for `γ^κ` (L1). If `μ_κ`
were a nearest-neighbor Markov field, its full conditional at `x` would be a
function of the six axial neighbors, contradicting R1's genuine dependence on
`x + κ_1 e_1 − κ_2 e_2`. If `μ_κ = ν` with `ν` Gibbs for `γ^S`, then `μ_κ` is
Gibbs for both `γ^κ` and `γ^S`, both finite-range, so by L2 `γ^κ_x = γ^S_x`
everywhere; but `γ^S_x` does not depend on `ω_{x + κ_1 e_1 − κ_2 e_2}` while
`γ^κ_x` does. ∎ At the silent triples this separates the formation law from
every static law without deciding how many static laws there are; where
`6c_1 < 1` (block 03) it separates it from the unique one. The finite-window
classification of block 01 (equality iff at most one recorded neighbor) is
consistent: in the bulk of `Z^3` every site records three.

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

**(b) Distinctness.** For `c < 1/3` at a triple with nonzero third difference,
the eight laws `μ_κ` are pairwise distinct.

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
invariant (block 08's axis symmetry, Q1c); by (b) `μ_κ` is invariant under no
other rotation. The equal mixture `μ̄ = (1/8) Σ_κ μ_κ` is invariant under all
proper cubic rotations, the axis reflections and all translations. It is not
translation-ergodic: each `μ_κ` is translation-mixing (block 08's covariance
bound, Q4b, decays exponentially), hence ergodic; distinct ergodic laws are
mutually singular, so `μ̄` has eight distinct ergodic components. ∎ No single
law of the class is proper-cubic covariant; the covariant object is a mixture
— consistent with the finite-window findings of #8096 (no covariant sequential
order) and #8102 (the uniform order mixture as a witness device), now on `Z^3`.

## Theorem R4 — the imprint of the sweep

**(a) On `Z^3`.** For `c < 1/3` at a triple with nonzero third difference,
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
such imprint by construction. The result says only that any single monotone
order leaves its direction readable in the record statistics, exactly and
without a clock.

## R5 — two dimensions for contrast (cited)

In two dimensions (the plane-law note, on main) the point reflection maps the
top-left class to the bottom-right one and preserves both the diagonal pair set
and its grouping (pairs, not triples), so opposite corners coincide (block 05's
P7(a)) and there are two laws, distinguished by the axis reflections. In three
dimensions the point reflection preserves the dependency set but not its
grouping into triples (R3a), so there are eight. The two-dimensional analogue
of R2 is the plane-law note's statement that the center's conditional given
its eight neighbors is not the static rule.

## No-Go Discipline Gate

The negative sentences of this note are R2 (not a static law; not
nearest-neighbor Markov) and R3(c)/R4 (no single covariant law; no invariance
under reflections). All are proved at scope from L2 and exact witnesses; none
is a route no-go beyond its scope.

### N1 — Routes by which the formation law could still be a static law, or covariant

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a static law with a longer-range specification | let the "static law" be Gibbs for a potential with face-diagonal and three-body terms | that is `γ^κ` itself; block 02's static specification is nearest-neighbor by the axiom's rule; a longer-range static rule is not the declared rule | RULED OUT BY PRIOR at scope (the rule is nearest-neighbor) |
| 2 a triple where the third difference vanishes | a nonconstant `(p, q, r)` with `log K_3` pair-additive | executed nonzero at `(3, 1, 2)`, `(5, 2, 4)`; not proved for every nonconstant triple; such a triple would make R1's face-diagonal dependence vanish and R2, R3 silent there | not attempted; obligation named |
| 3 `c ≥ 1/3` | outside block 08's region the `Z^3` law is not constructed | nothing claimed | not attempted; obligation named |
| 4 the mixture as "the" law | take `μ̄` as the physical law | it is covariant but not a Gibbs law for any single specification of the eight and not ergodic; selecting it is an owner decision, not a derivation | ATTEMPTED (its properties stated) |
| 5 a covariant random order | the random-priority construction (the owner's note on its branch, unlanded) | a different object with its own Markov structure, not analyzed here | not attempted; obligation named |
| 6 the constant rule | `p = q = r` | one uniform law; every statement collapses; excluded by the variation clause restricted to the menu | ATTEMPTED (control) |

### N2 — Wall-independence audit

Walls: `W_reg` (`c < 1/3`), `W_3` (nonzero third difference), `W_pos`,
`W_menu`, `W_class`. `W_reg` and `W_3` are independent: the constant rule has
`c = 0` and zero third difference; a triple with `c ≥ 1/3` can have nonzero
third difference (e.g. far along `(1, 1, t)`). `W_pos` gives L2's full support
and L1's product form; `W_menu` fixes the numbers; `W_class` defines the
objects. L1 and L2 need `W_reg` (for the object) and `W_pos`; R1's dependence,
R2 and R3(b) need `W_3` in addition; R4(b) is a finite computation needing
`W_pos` only.

### N3 — Hidden-wall scan

Scanned for "we assume", "by construction", "as is standard", "the framework
provides", "naturally", "obviously", "canonical", "registered", "background",
"bridge context". Hits: "by construction" in R4(c) (a covariant construction
has no imprint — a definition-level remark, not load-bearing). The cited steps
(the ergodic decomposition; distinct ergodic laws are mutually singular) are
named under Imports and used only in R3(c)'s last sentence.

### N4 — Per-citation table

| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 08 (stacked; proposed, unaudited): Q1e, Q1f, Q3, Q4b, Q4e | the `Z^3` law, its product form, its region and decay | L1, R1, R3(c), R4(b) | yes (parent; cited) |
| block 02 (on main; proposed, unaudited): Theorem C | the static specification and its Gibbs measures | the static side of R2 | yes (parent; cited) |
| block 03 (on main; proposed, unaudited): the region `6c_1 < 1` | uniqueness of the static law | contrast in R2 only | yes (contrast) |
| the plane-law note (on main; proposed, unaudited) | the 2D Gibbs identification; two classes; the center's conditional | R5; the pattern of L1 | yes (cited) |
| #8096, #8102 (open PRs; not inputs) | no covariant sequential order; the order mixture | R3(c)'s consistency remark | yes (context) |
| the time-directed-sweep note (on main) | the image of a current under a sweep | none (a different object) | non-match, dropped |

After dropping the non-match, the headline rests on the parents' cited
statements and this note's own proofs and executed witnesses.

### N5 — Resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "the formation law is not a static law on `Z^3`" | executed: the conditional's dependence on one face-diagonal site over all six values; the `6^6` diagonal assignments for the pair witness; the third difference | executed: the twelve dependency sites and the excluded sites of the kernel formula | executed: the eight corners' sets and groupings; the four one-plane laws | executed: the `2×2` column's joint law and its transpose over all `1296^2` pairs | proved from L1–L2 in the region at triples with nonzero third difference; not claimed elsewhere |

### N6 — Partial-closure paths and primitive scan

The registered primitives (`scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`) supply no order,
corner, specification or coupling condition; none is a wall. A reframing that
would close R3(c)'s "no covariant law" is the adoption of the mixture or of a
covariant random order as the supplied formation law — an owner decision,
recorded as such. `docs/repo/DEFERRED_DECISIONS.md` entry 1 is not fired.

### N7 — Steelman

Hostile reviewer: "L2 is too strong: Gibbs measures are defined by almost-sure
conditionals, and the specification is only determined up to null sets; the
witness compares kernels at a single configuration." Reply: with finite-range
kernels the comparison is between two functions of finitely many coordinates,
and a full-support law charges every cylinder, so an almost-sure equality of
such functions is an everywhere equality — the proof of L2; full support is
proved from the box laws' uniform positivity. "R3(c)'s ergodicity uses a limit
theorem you did not prove." Conceded and stated: the ergodic decomposition is
cited definition-level and used only for the last sentence of R3(c); the
distinctness of the eight laws (R3(b)) does not use it.

### N8 — Cross-cycle echo

The nearest prior wall is block 01's finite-window classification (formation =
static iff at most one recorded neighbor), which this note extends to `Z^3`
through a different mechanism (the Markov graph instead of the normalizer
identity); the plane-law note's two-dimensional conditional argument is the
same mechanism one dimension down. No structurally similar wall has been
retired.

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
formalism, the uniqueness of conditional probabilities and the ergodic
decomposition are classical references re-proved or cited at the scope used;
no value, constant or theorem is imported as authority.

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
  L2 (uniqueness of finite-range kernels under full support), R1–R4.
- Cited, definition-level: the DLR formulation of Gibbs measures for a
  finite-range specification (L1's statement); the pointwise ergodic theorem
  and the ergodic decomposition, used only for the last sentence of R3(c)
  (distinct ergodic translation-invariant laws are mutually singular).
- No literature value, constant, or theorem enters as authority; classical
  names appear only in this section and under Prior art.

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
