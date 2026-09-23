---
claim_id: admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_ordered_phase_obligation_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the positive six-axis product rule and supplied monotone formation class: exact level-time kernel; correspondence between spatially invariant stationary level laws and fully translation-invariant formation laws; closed noise formulas; strict majority preference across both 2:1 patterns iff p > max(q,r) and p^2 q > r^3; finite-island eroder bound; stochastic domination; finite nonempty cross-section metastability. The prescribed consistent two-dimensional rectangle family has a unique extension and exponential row/column correlations. No classification of all two-dimensional stationary laws or diagonal order is proved. The three-dimensional ordered phase remains conditional on the explicitly unproved stability obligation. Broader negative certification is deferred."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
  - admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_bounded_theorem_note_2026-09-15
runner: scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py
---

# The strong-coupling side of the three-dimensional formation law: a majority automaton in level time — the eroder theorem, the exact noise map, finite-cross-section metastability, and the exact obligation for an ordered phase

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; the ordered phase is an obligation, not a claim; unaudited)

## Result up front

Read the three-dimensional formation law in a different time: not plane by
plane, but level by level, where a level is the set of sites whose three
coordinates add to a fixed number. In that time the law is a plain cellular
automaton: every site on a level looks at exactly three sites on the previous
level, arranged like a site, its neighbor to the south and its neighbor to the
west, and draws its record from the rule's conditional given those three.
When the rule strongly prefers a neighbor's own value, that conditional
becomes a majority vote with small noise, and we prove exactly how small: the
odds of overruling a unanimous or a two-to-one vote fall like one over the
preference. A noiseless majority vote of this shape is an eroder: any finite
island of dissent is wiped out in a number of steps we compute exactly. On a
finite cross-section the law always has one stationary state, but as the
preference grows that state takes ever longer to reach — the six uniform
records become traps. For the prescribed two-dimensional rectangle-law
extension, row and column correlations decay at every positive coupling. With
only two earlier neighbors its limiting update chooses between distinct parents;
this does not classify all stationary laws or diagonal correlations. Whether the three-dimensional law really has six
ordered phases at strong coupling is exactly the classical question of whether
a noisy majority eroder is stable; we state that obligation precisely, with
the exact noise parameters it needs, and we do not claim it.

Exactly: the level automaton has neighborhood `{(0,0), (−1,0), (0,−1)}` after
projecting `x ↦ (x_2, x_3)` (S0); `P(a | a,a,a) = p³/(p³ + q³ + 4r³)`,
`P(a | a,a,b⊥) = p² r/(r(p²+q²) + r²(p+q) + 2r³)`,
`P(a | a,a,−a) = p² q/(pq(p+q) + 4r³)`, `P(a | a,b,c) = p/(3(p+q))` (S1); a
finite island dies within `M_1 + M_2 + M_3 − t_0 + 1` levels (S2); the
coarse-graining is dominated by the majority automaton with noise
`ε(p) = max(1 − p³/(p³+q³+4r³), 1 − p²q/(pq(p+q)+4r³), 1 − p²r/V_3)`, equal to `0.2958…` at `(10,1,2)` and `0.0206…` at `(100,1,2)` (S3); on the `2×2` cross-section the memory of the starting constant plane after eight steps (the total-variation distance between the laws started from the all-`+x` and the all-`−x` planes) rises from `0.000003` at `p = 3` to `0.5493` at `p = 100`, while the approach to the set of constant planes (the orbit quotient) contracts at every coupling (S4). Executed with exact
arithmetic: 20 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 08's region c < 1/3 leaves the strong-coupling side of the Z^3 formation law open (its queue item 'strong coupling c >= 1/3'); the campaign's standing question 'one law or several' now for the formation law; the derivation campaign's assembly (#8093): the formation-law node's phase structure"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the strong-coupling side is structured exactly (level automaton; noise map; eroder; domination; metastability) and reduced to one classical obligation (stability of the noisy majority eroder) with its exact inputs; a re-proof of that theorem at scope is the next block if the owner wants the ordered phase as a theorem; consumers: the campaign's queue; #8093's assembly; the parked statistical-bridge material (read-only)"
conditional_surface_status: "S0–S5 proved for every positive triple (S4 for every finite cross-section); executed at (p,1,2) for p in {3,10,30,100,1000}; S6 is an obligation, stated with the reference it would rest on and not claimed; conditional on the records-only reading, positivity, the six-axis menu and the monotone class as supplied conditions"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "S0 is a projection identity; S1 closed forms verified symbolically; S2 an elementary maximum argument; S3 a site-by-site coupling; S4 spectral continuity plus absorption in the limit; S5 the eigenvalues of K; S6 is not a theorem here and is labeled an obligation everywhere; every number an exact rational"
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable."

**Readings carried, named, nothing new adopted.** As in blocks 01–11: the
records-only reading, positivity, the six-axis menu with orbit weights
`(p, q, r)`, the monotone class with a corner (here `κ = (+,+,+)`; the others by
reflection). Block 08's objects: the box law, the plane chain `P_C` on a
cross-section `C`, the sensitivities and the region `c < 1/3`; block 09's
Gibbs identification. Notation: `Z_1 = p + q + 4r`, `K = φ/Z_1`,
`V_3 = r(p² + q²) + r²(p + q) + 2r³`.

**Level time.** For `x ∈ Z^3` the level is `ℓ(x) = x_1 + x_2 + x_3` and
`L_t = {x : ℓ(x) = t}`. The projection `π(x) = (x_2, x_3)` is a bijection
`L_t → Z^2` for every `t`. The predecessors of `x` project to
`π(x − e_1) = π(x)`, `π(x − e_2) = π(x) − (1, 0)`, `π(x − e_3) = π(x) − (0, 1)`.

**The binary coarse-graining and the majority automaton.** For a value `a ∈ M`
write `ξ_x = 1{v_x ≠ a}`. The majority automaton with noise `ε` is the
synchronous process `η` on `Z^2` (in level time) in which `η_y = 1` if at least
two of `η_y, η_{y−(1,0)}, η_{y−(0,1)}` (on the previous level) are `1`, and
otherwise `η_y = 1` with probability `ε`, independently over sites given the
previous level. Its noiseless version (`ε = 0`) is the majority rule.


### Linked source authority

- [Monotone rectangle formation law](ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md): P1 supplies the prescribed rectangle law, P4 its row/column K-chains, and the finite rectangle consistency identity supplies the selected extension.

- [Admissibility Rule Three Dimensional Monotone Formation Law Plane Chain Coupling Region Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md): only its explicit hypotheses and conclusions are used.
- [Admissibility Rule Three Dimensional Formation Law Markov Graph Eight Corner Laws Sweep Imprint Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_MARKOV_GRAPH_EIGHT_CORNER_LAWS_SWEEP_IMPRINT_BOUNDED_THEOREM_NOTE_2026-09-15.md): only its explicit hypotheses and conclusions are used.
- [Admissibility Rule Three Body Term Exceptional Locus Exact Classification Bounded Theorem Note 2026-09-15](ADMISSIBILITY_RULE_THREE_BODY_TERM_EXCEPTIONAL_LOCUS_EXACT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md): only the five explicit triple-pattern formulas are used here; exhaustive classification is deferred.

## Prior art and what is new

Block 08 proved uniqueness and decay for `c < 1/3` by a causal coupling and
named the strong-coupling side as open; block 09 identified the `Z^3` law as
Gibbs for a finite-range specification. The classical theory of probabilistic
cellular automata contains the object identified in S0: a synchronous automaton
on `Z^2` with the north-east-center neighborhood, and the theorem (Toom 1980)
that a monotone eroder with small independent noise is non-ergodic — the
noisy north-east-center majority has at least two invariant laws. Modern
Peierls-bound presentations of that theorem exist. None of it is on `main`
(search recorded in `ROUTE_PORTFOLIO.md`), and per the lane's policy it is a
reference here, never authority: this note does not re-prove it and does not
use it to claim anything. The static law's ordered phase is likewise unproved
on `main` (block 03's region is the uniqueness side).

New here: the level-time identification (S0), the exact noise map (S1), the
eroder theorem with its exact bound (S2), the domination lemma (S3), the
finite-cross-section metastability (S4), the two-dimensional contrast (S5),
and the exact statement of the ordered-phase obligation with the block's
recorded attempt (S6).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| S0 level-time automaton; spatially invariant stationary laws ↔ translation-invariant `Z^3` laws | proved; the projection executed (B1) |
| S1 the noise map, closed forms, limits, the majority-preference condition | proved; verified symbolically against the definition; values at five couplings (B2–B4) |
| S2 the eroder theorem with the exact bound | proved; executed on 300 random islands, a line and a triangle (C1–C2) |
| S3 the domination lemma; `ε(p)` exact | proved; `ε(p)` executed as the maximum over all 216 triples (B5) |
| S4 unique stationary law at finite `W`; `λ_2 → 1` as `p → ∞` | proved; the full-chain memory table and the orbit-quotient contraction table on `2×2`, the absorption probability at `p = 10^6` (D1–D2) |
| S5 prescribed rectangle extension and axial correlation bound | proved; the eigenvalue executed (D3) |
| S6 the ordered phase in three dimensions | obligation: the stability theorem for the dominating automaton; not re-proved; the attempt's obstruction recorded |
| the static law's ordered phase; the exact threshold `ε_0`; the plane chain on the infinite cross-section at strong coupling | open; not this note |

## Theorem S0 — the formation law is a north-east-center automaton in level time

**Statement.** Under the monotone class the configuration on `L_t` given the
configurations on `L_{t−1}, L_{t−2}, …` depends only on `L_{t−1}` and is the
product measure `Π_{x ∈ L_t} r(· | v_{x−e_1}, v_{x−e_2}, v_{x−e_3})`. After the
projection `π`, this is a synchronous probabilistic cellular automaton on `Z^2`
with neighborhood `{(0,0), (−1,0), (0,−1)}` and kernel the rule's three-neighbor
conditional. It is defined at every positive coupling (each level is a product
measure given the previous one), commutes with the translations of `Z^2`
(the level-preserving translations of `Z^3`), and its stationary two-sided
chains with spatially translation-invariant level marginals are exactly the `Z^3`-translation-invariant laws of the formation
process; in block 08's region its invariant law is unique and equals block
08's `Z^3` law.

*Proof.* Every predecessor of `x ∈ L_t` lies on `L_{t−1}` (`ℓ(x − e_i) = t − 1`),
so the level chain is Markov and each level is a product given the previous
one; the projections of the predecessors are as displayed. A level-preserving
translation `x ↦ x + u`, `ℓ(u) = 0`, commutes with the kernel by the rule's
translation covariance; the shift by `e_1` maps `L_t` to `L_{t+1}` with the
same kernel. Stationarity gives invariance under this time shift; spatial
translation invariance of the level marginal gives invariance under the two
level-preserving generators. These three generators span all translations of
`Z^3`. Conversely a fully translation-invariant formation law supplies both
invariances. An arbitrary stationary level law alone gives only time-shift
invariance, not spatial invariance. In the region, block 08's discrepancy
bound between two level chains started from any two levels is `(3c)^n` per
site after `n` levels, so the invariant law is unique and is the `Z^3` law of
Q4e. ∎ Executed: the projected predecessor offsets for a sample of sites (B1).

The plane chain of block 08 and the level chain are two Markov structures of
the same law; at strong coupling the level chain is the well-defined object
(a synchronous product update needs no in-plane limit), and the ordered-phase
question is asked of it.

## Theorem S1 — the exact noise map

**Statement.** For a value `a` and `b ⊥ a`, `c ⊥ a, b`:
`P(a | a,a,a) = p³/(p³ + q³ + 4r³)`,
`P(a | a,a,b) = p² r/(r(p² + q²) + r²(p + q) + 2r³)`,
`P(a | a,a,−a) = p² q/(pq(p + q) + 4r³)`,
`P(a | a,b,c) = P(b | a,b,c) = P(c | a,b,c) = p/(3(p + q))`, and
`P(−a | a,b,c) = q/(3(p + q))`.
For fixed `q, r` and `p → ∞` the three deviations `1 − P(majority)` are
`(q³ + 4r³)/p³ + O(p^{−4})`, `r/p + O(p^{−2})` and `q/p + O(p^{−2})`
respectively, and the tie splits evenly. The majority value of a `2:1` triple is
its strictly most likely output across both patterns iff
`p > max(q, r)` and `p² q > r³`.

*Proof.* Direct evaluation of `Π_i φ(s, a_i)/Z_3(a)` for each pattern (the five
pattern values `V_1, …, V_5` of block 11). For `(a, a, b)`: the weights are
`p² r` (`s = a`), `q² r` (`−a`), `p r²` (`b`), `q r²` (`−b`), `r³` (each of
`±c`), so `a` is the most likely iff `p² r > max(q² r, p r², q r², r³)`, i.e.
`p > max(q, r)`; for `(a, a, −a)`: weights `p² q`, `p q²`, and `r³` for the
four orthogonal values, so `a` wins iff `p > q` and `p² q > r³`, an additional condition not implied
by `p > max(q, r)`. For example `(p,q,r)=(3,1/100,2)` has majority weight
`9/100` below each orthogonal weight `8`. Combining the two patterns gives
exactly the two stated strict inequalities. The expansions are the leading terms of the ratios. ∎
Executed: the closed forms against the definition, symbolically (B2); the
values at `(p, 1, 2)` for `p = 3, 10, 30, 100, 1000` (B3); the preference
condition on both strict boundaries and the rational counterexample (B4).

## Theorem S2 — the majority rule is an eroder, with an exact bound

**Statement.** Let a finite set of `1`s sit on level `t_0` of the noiseless
majority automaton (a site is `1` iff at least two of its three predecessors are
`1`), with coordinate maxima `M_i = max_{x} x_i` over the island (in the
`Z^3` coordinates). Then the coordinate maxima never increase from level to
level, and the island is empty at every level `t > M_1 + M_2 + M_3`; it dies
within `M_1 + M_2 + M_3 − t_0 + 1` levels.

*Proof.* Let `x` be `1` on level `t + 1` with `x_i > M_i(t)` for some `i`. The
two predecessors `x − e_j`, `j ≠ i`, have `i`-th coordinate `x_i > M_i(t)`, so
they are `0`; only `x − e_i` can be `1`; `x` is not a majority: contradiction.
Hence `M_i(t + 1) ≤ M_i(t)`. A `1` at `x ∈ L_t` has `Σ_i x_i = t` and
`x_i ≤ M_i(t) ≤ M_i(t_0)`, so `t ≤ Σ_i M_i(t_0)`. ∎ Executed: 300 random
islands on levels `3` to `12` all die within the bound; a line of six `1`s dies
in exactly six levels and a filled triangle of fifteen in exactly nine, both
equal to the bound (C1–C2).

Infinite sets of `1`s are not covered: a suitably oriented half-plane of `1`s
persists; the eroder property concerns finite islands, which is what the
stability question needs.

## Theorem S3 — domination by the noisy majority automaton

**Statement.** Fix a value `a` and let
`ε = max { 1 − r(a | u, v, w) : (u, v, w) ∈ M³ with at least two entries equal to a }`,
an exact rational. There is a coupling of the formation process (in level
time, from any initial level) with the majority automaton `η` with noise `ε`
(from an initial level with `η ≥ ξ`) such that `ξ_x ≤ η_x` at every site of
every level, where `ξ_x = 1{v_x ≠ a}`. Consequently
`P(v_x ≠ a) ≤ P(η_x = 1)` for every `x`. At `(p, 1, 2)`: `ε = 35/44, 21/71, 71/971, 211/10211, 2011/1002011` `= 0.7954…, 0.2958…, 0.0731…, 0.0206…, 0.0020…` for `p = 3, 10, 30, 100, 1000`; the maximum is attained at the antipodal `2:1` triple `(a, a, −a)` for `p = 3, 10` and at the orthogonal `2:1` triple `(a, a, b)` for `p = 30, 100, 1000` (the antipodal deviation is `q/p + O(p^{−2})`, the orthogonal one `r/p + O(p^{−2})`, and `r > q` at these couplings); in general `ε = max(q, r)/p + O(p^{−2})`.

*Proof.* Build both processes level by level, site by site, given the previous
level with `ξ ≤ η`. At `x`: if at least two of `η`'s predecessors are `1`, set
`η_x = 1 ≥ ξ_x`. Otherwise at most one of `η`'s predecessors is `1`, hence at
most one of `ξ`'s (since `ξ ≤ η`), so at least two of `v`'s predecessors equal
`a` and `P(ξ_x = 1 | past) = 1 − r(a | v_{A_x}) ≤ ε`; couple `ξ_x` with a
Bernoulli(`ε`) variable `η_x` monotonically. The sites of a level are drawn
independently given the previous level in both processes, so the coupling is
legitimate site by site. ∎ Executed: `ε` as the exact maximum over all 216
triples at the five couplings, with the attaining pattern (B5).

## Theorem S4 — finite cross-sections: unique but metastable

**Statement.** For every finite nonempty cross-section `C` and every positive coupling
the plane chain `P_C` has a unique stationary law (block 08, Q3a). As
`p → ∞` with `q, r` fixed, `P_C(p) → P_C(∞)`, the plane transfer of the
majority-with-random-ties automaton restricted to `C`, in which each of the six
constant planes is absorbing; hence at least six eigenvalues of `P_C(p)` tend
to `1`, and the second-largest eigenvalue modulus of `P_C(p)` tends to `1`: the
relaxation time diverges.

*Proof.* The entries of `P_C(p)` are rational functions of `p` with limits: for
a constant plane `w ≡ a`, every site of the next plane has a unanimous
recorded set (`(a)`, `(a, a)` or `(a, a, a)` according to its position in `C`),
and `r(a | a) = p/Z_1`, `r(a | a, a) = p²/Z_2(a,a)`, `r(a | a,a,a) = p³/Z_3(a,a,a)`
all tend to `1`; so `P_C(∞)(w ≡ a, w ≡ a) = 1`. A stochastic matrix with six
absorbing states has eigenvalue `1` with multiplicity at least six; the
eigenvalues of `P_C(p)` (with multiplicity) converge to those of `P_C(∞)`
(continuity of the roots of the characteristic polynomial in its
coefficients); for finite `p` the eigenvalue `1` is simple (positivity), so at
least five other eigenvalues tend to `1`. ∎ Executed on the `2×2`
cross-section at `(p, 1, 2)`, on the full `1296`-state chain with integer
numerators over a common denominator: the total-variation distance between the
`n`-step laws started from the all-`+x` and the all-`−x` planes, `n = 1, 2, 4,
8`, is `0.4284, 0.0828, 0.0029, 0.000003` at `p = 3`,
`0.7985, 0.5096, 0.1544, 0.0101` at `p = 10`, `0.9296, 0.7959, 0.5051, 0.1659`
at `p = 30`, `0.9769, 0.9273, 0.7952, 0.5493` at `p = 100` — the memory of
which constant plane the chain started from, rising toward one with `p` at
every `n` (D1). The `48`-fold orbit quotient identifies the six constant
planes, so its contraction measures only the approach to the *set* of constant
planes: its maximal row-to-row total variation after `n` steps is
`0.0720, 0.0020, 0.0000, 0.0000` at `p = 3` and `0.7349, 0.4139, 0.1103,
0.0059` at `p = 100`, contracting at every coupling and lying below the
full-chain memory at every `(p, n)` (D1b); the probability that the constant
plane maps to itself is at least `1 − 10^{−5}` at `p = 10^6` (D2). The two
tables together are the metastability: fast collapse onto an ordered plane,
slow forgetting of which one.

## Theorem S5 — the prescribed rectangle extension and axial correlation bound

**Statement.** The two-dimensional monotone formation law (block 05's
rectangle law) has a unique plane extension with those prescribed rectangle
marginals at every positive coupling, its rows and columns are `K`-chains (block 05, P4),
and the correlation along a row of any function of the record decays like
`max(|p − q|, |p + q − 2r|)^d/Z_1^d` with `d` the distance, a ratio strictly
below one at every positive coupling: the two-dimensional law has no
long-range order along rows or columns at any coupling. In level time the
two-dimensional process is a synchronous automaton on `Z` with the
two-predecessor neighborhood `{0, −1}`, whose deterministic limit at `p → ∞`
chooses one of two differing predecessors with probability `1/2` each: this is the stated two-parent limiting choice rule.

*Proof.* Uniqueness: the rectangle law is one law (P1) and consistent under
translation (block 08, Q2b), so its extension with those rectangle marginals is unique. This is not a
uniqueness theorem for every stationary law of the two-predecessor automaton,
nor a claim about diagonal order. The row
statement: `K` has eigenvalues `1`, `(p − q)/Z_1` (multiplicity three) and
`(p + q − 2r)/Z_1` (multiplicity two), all but the first of modulus below one
for positive weights (`|p − q| < Z_1` and `|p + q − 2r| < Z_1`), and the
correlation of `f(v_0)` with `g(v_d)` along a `K`-chain with the uniform start
is bounded by the second eigenvalue's `d`-th power. The two-predecessor limit:
`r(s | a, b) ∝ φ(s,a) φ(s,b)` with `a ≠ b` gives weights `p φ(a,b)` for
`s = a` and for `s = b`, equal, and lower-order weights elsewhere. ∎ Executed:
the eigenvalue `(p − q)/Z_1` at the five couplings (D3).

## S6 — the ordered phase in three dimensions: the exact obligation

**What would prove it.** Let `η` be the majority automaton with noise `ε` of
S3 (neighborhood `{(0,0), (−1,0), (0,−1)}` in level time, a monotone eroder by
S2). *Obligation O:* there is `ε_0 > 0` such that for `ε < ε_0`, starting from
the all-`0` level, `sup_{x, t} P(η_x = 1) ≤ δ(ε)` with `δ(ε) < 1/2`. Given O:
by S3 the formation process started from the all-`a` level satisfies
`P(v_x ≠ a) ≤ δ(ε(p))` at every site of every later level; every Cesàro limit
point of its level laws is an invariant law of the level automaton (the kernel
is Feller: a level's cylinder law is a finite product) with
`P(v_y = a) ≥ 1 − δ` at every site; the six values give six invariant laws,
pairwise distinct since `1 − δ > 1/2 > δ`; hence at least six extremal
invariant laws: an ordered phase, and block 08's uniqueness fails there. The
threshold in `p` is where `ε(p) = max(q, r)/p + O(p^{−2})` crosses `ε_0`.

**What is known and not used.** O is the classical stability theorem for
noisy monotone eroders (Prior art). Under the lane's policy it is a reference
and not authority; nothing above relies on it, and this note does not state the
ordered phase as a result.

**The block's own attempt, and its exact obstruction.** The natural contour route: a `1` at `x` (from the all-`0` level) is explained by a backward tree in
which every non-noise node has two `1`-predecessors and every leaf is a noise
site; `P(x = 1)` is bounded by the sum over explanations of `ε^{(number of
distinct noise sites)}`. The union bound needs the number of minimal
explanations with `k` distinct noise sites to be at most `C^k` uniformly in
the level. That fails for the naive tree: a line of `k` noise sites sustains
an island of about `k²/2` sites for `k` levels, so the closure is quadratic in
`k` while its nodes are exponential; and minimal noise sets need only be
"connected at scale `k`", which the naive count does not bound by `C^k`. The
classical proof replaces the tree by a sparse contour whose total length is
linear in the number of noise sites, using the eroder's geometry; that
construction is the missing lemma, named here and not reproduced.

## No-Go Discipline Gate — deferred broader certification

This revision retains the constructive identities, quantitative bounds and named
finite witnesses above. It does not certify the broader exclusion claims in the
original packet. The original N1–N8 text and every recovery route are preserved
byte-exact in [the PR8146 history manifest](work_history/review_loop/pr8146/original-manifest.json)
under PR8146; the original branch remains a recovery handle for unlanded work.

### N1 — Route coverage
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
- A pattern whose closed form in S1 disagrees with the definition (B2), or a coupling satisfying both `p > max(q, r)` and `p² q > r³` at which a `2:1` triple's majority is not the most likely output (B4).
- A finite island of the noiseless majority rule surviving beyond `M_1 + M_2 + M_3 − t_0 + 1` levels (C1).
- A triple with at least two entries `a` at which `1 − r(a | triple)` exceeds the printed `ε` (B5).
- A cross-section and coupling at which the constant plane is not asymptotically absorbing; a full-chain memory number or a quotient contraction number that decreases with `p`; a quotient number above the full chain's (D1–D2).
- A positive triple at which `|p − q| ≥ Z_1` or `|p + q − 2r| ≥ Z_1` (D3).

## Boundaries and non-claims
This note structures the strong-coupling side of the three-dimensional monotone formation law and reduces its ordered phase to one exact obligation; it does not prove an ordered phase, does not select an order, corner or coupling as physical, states nothing about the static law's ordered phase, and gives no numeric threshold. No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision. The classical stability theorem for noisy eroders is a reference named here and under Prior art, not authority and not re-proved; the probability and spectral results listed under Imports are mathematical inputs, not physical premises.

Further: the plane chain on the infinite cross-section is not constructed at strong coupling (the level automaton is the object there); the exact threshold `ε_0` is not given; the attempt in S6 is recorded as an obstruction, not as a negative theorem.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Blocks 05 (on main), 08 and 09 (stacked): proposed, unaudited; the parts used are restated.
- Mathematical imports: countable extension of consistent finite-dimensional laws on the finite-alphabet product space; existence of stationary two-sided Markov chains from invariant marginals; weak compactness and the Cesàro invariant-measure argument for a Feller kernel on a compact product space; continuity of roots of finite characteristic polynomials. Their hypotheses are the finite alphabet, positive local transition probabilities, finite dependence of each cylinder update, and (for the spectral argument) a finite nonempty cross-section. These are used as mathematical theorems, not merely definitions.
- The exact algebra, eroder bound and coupling are proved above. The stability theorem in S6 remains an unproved conditional obligation.
- Reference only (never authority, not used): the stability theorem for noisy monotone eroders — Toom (1980), with modern Peierls-bound presentations — and the north-east-center automaton as the classical example; named here and under Prior art.

## Review record
Supervisor-run block (owner directive: keep going on the strong-coupling phase; no subagents). The control (`specs/supervisor_control_block12_strong_coupling.py`) computed the noise map, the eroder bound on islands, the `2×2` contraction table and the two-dimensional eigenvalue before the contract; the lens pass is in `GOAL_block12.md`; the primary seat wrote S0–S6 and the runner; the refuting pass (`CHECKER_block12_findings.md`) recomputed `ε(p)` from the three closed-form patterns and the `2×2` numbers on the full `1296`-state chain instead of the orbit quotient, and the eroder bound with an exhaustive small-island generator. Facts settled while executing: the runner's first literal for `ε(100)` was the antipodal deviation (`101/7754`) while the maximum is the orthogonal one (`211/10211`) — the largest deviation switches from the antipodal to the orthogonal `2:1` triple between `p = 10` and `p = 30` at `(p, 1, 2)` (refuting pass, R3); the orbit quotient identifies the six constant planes, so its contraction is not the chain's slow mode — the full-chain memory table was added as D1 and the quotient demoted to D1b (refuting pass, R1); the quotient's total variation is a lower bound for the full chain's by the data-processing inequality, not an upper bound.

## Verification

```bash
python3 scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py
python3 scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py --exact
python3 scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py --mutation eroder_bound_violated_claimed
```

Families: A authority and inputs; B the level projection, the noise map, the preference condition, `ε(p)`; C the eroder theorem on islands; D the full-chain memory table, the quotient contraction, absorption, the two-dimensional eigenvalue; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
