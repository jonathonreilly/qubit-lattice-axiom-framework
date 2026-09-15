---
claim_id: admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_and_several_gibbs_states_reflection_positivity_chessboard_peierls_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the static law of the six-axis covariant positive product rule with weights (p, q, r) on same, antipodal and orthogonal pairs, m = max(q, r): (T1) the weight matrix has eigenvalues p + q + 4r, p - q (three times) and p + q - 2r (twice) and is invariant under the full cube group, which acts transitively on the six values (proved; executed); (T2) on every torus of even side the law is reflection positive for reflections through planes containing sites, for every positive weight matrix (proved; executed on a ring and a 4x2 torus); (T3) the chessboard estimate for events attached to unit cells and reflected by site reflections (re-proved; executed); (T4) the probability that every bond of one direction joins different values has N-th root at most 6m/p on the torus of N sites (proved; executed); (T5, two dimensions) for p >= 216 m and a torus of side at least 44, the torus law gives v_0 = v_x with probability above 1/2 for every x within a quarter of the side: long-range order, by planar cut-cycle duality and contour counting with explicit constants (proved; the counts and series executed exactly); (T6) every limit point of the torus laws is a translation-invariant Gibbs state with that long-range order, and a unique Gibbs state would be extremal, hence tail-trivial, hence short-range correlated, so the static law on Z^2 has at least two Gibbs states for p >= 216 m (proved at scope, with the backward martingale theorem named as the standard import); (T7, three dimensions) the same chain with the dual-surface connectivity lemma of the cubic lattice named as an import gives long-range order and at least two Gibbs states on Z^3 for p >= 34,992,000 m (conditional on that lemma; constants executed). No coupling is selected as physical; the thresholds are existence constants, not optimal; the formation law's phase (block 12's obligation) is untouched; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py
---

# The static six-axis law at strong coupling has long-range order and several Gibbs states: reflection positivity through site planes, a chessboard estimate, and contour counting with explicit constants — a theorem on `Z²`, conditional on one named lemma on `Z³`

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; the two-dimensional statement is unconditional; the three-dimensional one is conditional on the named dual-surface connectivity lemma; unaudited)

## Result up front

Block 03 settled the weak-coupling side of the static law: one Gibbs state
where the influence of a single neighbour is small enough. This note settles
the other side, in two dimensions outright and in three dimensions up to one
named lemma of lattice topology. When the weight for agreeing neighbours is
large enough compared with the weights for disagreeing ones — at least `216`
times, in two dimensions — the record at the origin and the record far away
agree with probability above one half in every finite torus, and that
long-range agreement survives in the infinite lattice: the static law then
has more than one Gibbs state, the six axis values being the candidates for
what a state prefers. The proof is the classical one made exact: the torus law
is reflection positive through planes containing sites whatever the weights;
reflection positivity gives the chessboard estimate; the chessboard estimate
turns "these `n` bonds all disagree" into a bound `(6m/p)^{n/2}`; and a
count of the closed dual curves that could isolate the origin sums to less
than one half. The constants are crude and are not claimed to be
sharp: block 03's thresholds and this one leave a wide band where nothing is
decided. The three-dimensional version needs the fact that a minimal
separating set of bonds in the cubic lattice is connected as a dual surface;
that fact is named, not re-proved, and the three-dimensional conclusion is
conditional on it.

Exactly: `E_L[F · F∘θ] ≥ 0` for site reflections (T2);
`μ_L(∩ A_c) ≤ Π μ_L(A_c^{diss})^{1/N}` (T3); `μ_L(all bonds of one direction bad)^{1/N} ≤ 6m/p`
(T4); in two dimensions with `ε = 6m/p ≤ 1/36`,
`μ_L(v_0 ≠ v_x) ≤ 5/24 + 45/256 = 295/768 < 1/2` (T5), hence at least two Gibbs states
for `p ≥ 216 m` (T6); in three dimensions `p ≥ 34,992,000 m` (T7, conditional).
Executed with exact arithmetic: 20 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the campaign's standing question 'one law or several' for the static law of the six-axis rule: block 03 (on main) gives the uniqueness region; the strong-coupling side is open on main (the two-site criterion note names an ordering argument as open); the static law is the reading that carries the repository's Green functions (blocks 13-16)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the strong-coupling side is settled on Z^2 (at least two Gibbs states for p >= 216 m) and reduced on Z^3 to one named lattice-topology lemma with explicit constants; sharpening the constants and re-proving the lemma are the next items. Consumers: #8093's assembly (the static reading's phase structure); block 12 (PR #8146: the formation law's counterpart obligation); the campaign's queue"
conditional_surface_status: "T1-T6 proved for every positive weight triple (T5-T6 for p >= 216 max(q, r) on Z^2); T7 conditional on the dual-surface connectivity lemma; executed at (p, 1, 2); conditional on the six-axis menu and the product rule as supplied conditions; the backward martingale theorem and planar cut-cycle duality named as standard imports"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a sum-of-squares identity (T2); an iterated quadratic-form inequality (T3); a counting bound on a partition function (T4); planar cut-cycle duality with an explicit contour count and a geometric series (T5); the DLR limit, conditioning on tail events and the backward martingale theorem (T6); every constant an exact rational"
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable."

**Readings carried, named, nothing new adopted.** The static reading of the
rule (block 01 on `main`; block 03 on `main` for its uniqueness region,
[`ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md)):
the Gibbs specification with nearest-neighbour weights `φ(a, b) = p, q, r` on
same, antipodal and orthogonal pairs of the six-axis menu, positive; `m = max(q, r)`.
The lattice is `Z^d`, `d = 2` or `3`; the six-axis menu is the same in both.

**Tori and their laws.** `T_L = (Z/2L Z)^d`, `N = (2L)^d` sites, `dN` bonds
(`d` directions); `μ_L(v) = Π_{bonds} φ(v_x, v_y)/Z_L`. A bond is *good* if its
endpoints carry equal values, *bad* otherwise. **Cells:** the unit cubes
`[x, x + 1]^d`, `x ∈ T_L`; a bond `(x, x + e_i)` has the *canonical cell* `x`;
each cell is canonical for `d` bonds. **Site reflections:** for `1 ≤ i ≤ d` and
`k ∈ Z/2L`, `θ_{i,k}` reflects `x_i ↦ 2k − x_i`; it fixes the planes `x_i = k`
and `x_i = k + L` pointwise, maps bonds to bonds and cells to cells.

**Gibbs states.** A probability `μ` on `M^{Z^d}` is a Gibbs state of the static
specification if for every finite `Λ` and local `f`, `μ(f) = μ(γ_Λ f)` with
`γ_Λ f(w) = Σ_{v_Λ} f(v_Λ w_{Λ^c}) Π_{bonds meeting Λ} φ / Z_Λ(w)`. The tail
σ-field is `∩_n F_{Λ_n^c}`.

## Prior art and what is new

Block 03 (on `main`) proved the uniqueness region on `Z³` by the one-site
contraction criterion and named the other side open; the two-site criterion
note (on `main`) names "an ordering argument" as its open route 5. Reflection
positivity and chessboard estimates are the Fröhlich–Israel–Lieb–Simon method
(1978), applied to discrete symmetry breaking by Fröhlich–Lieb and in Biskup's
lecture notes; Peierls's contour argument (1936) is classical; planar
cut–cycle duality is Whitney's theorem (Diestel, Prop. 4.6.1), resting on the
Jordan curve theorem for lattice polygons; the connectivity of a minimal
separating bond set in `Z³` as a dual surface is Timár's lemma (2013); the
backward martingale theorem is Lévy's. All are re-proved here except the three
named imports (the Jordan curve theorem for lattice polygons, the backward
martingale theorem, and Timár's lemma for `Z³`), which are cited at
definition level and never as physics. Nothing on `main` (search recorded in
`ROUTE_PORTFOLIO.md`) treats the six-axis static law's ordered side.

New here: the exact statement for this rule with explicit constants; the
observation that site reflections need no positivity of the weight matrix
(so the argument covers weights where the matrix is indefinite, such as
`(5, 2, 4)`, which block 03 also treats); the two-dimensional theorem; the
three-dimensional conditional statement with its constants.

## Exact target and obligation graph

| obligation | status here |
|---|---|
| T1 spectrum; cube-group invariance and transitivity | proved; executed symbolically and on the 48 signed permutations (B1) |
| T2 reflection positivity through site planes, any weights | proved; executed on the ring of 4 and the `4×2` torus at `(3,1,2)` and `(5,2,4)` (B2) |
| T3 the chessboard estimate | re-proved; executed on the ring and the `4×2` torus (B3) |
| T4 the disseminated bound `ε ≤ 6m/p` | proved; executed on the ring and the `4×2` torus (C1) |
| T5 two dimensions: contour count, series, winding term, threshold `216 m` | proved; the counts for lengths 4–8, the series at `y = 1/2` and the winding bound executed exactly (C2–C4) |
| T6 long-range order ⇒ at least two Gibbs states | proved at scope (the backward martingale theorem named) |
| T7 three dimensions | conditional on the dual-surface connectivity lemma; the connected-set bound and the series executed (D1–D2) |
| optimal thresholds; the band between block 03's thresholds and these; the formation law's phase | open; not this note |

## Theorem T1 — spectrum and symmetry

**Statement.** The `6×6` matrix `φ` has eigenvalues `Z_1 = p + q + 4r` (the
constant vector), `p − q` (the three functions odd under `a ↦ −a`) and
`p + q − 2r` (the two even functions summing to zero). The full cube group of
48 signed axis permutations preserves `φ` and acts transitively on the six
values.

*Proof.* `φ f(a) = p f(a) + q f(−a) + r Σ_{b ⊥ a} f(b)`; on odd `f` the last sum
vanishes; on even zero-sum `f` it equals `−f(a) − f(−a) = −2f(a)`. The weights
depend only on whether a pair is same, antipodal or orthogonal, which every
signed permutation preserves; the axes form one orbit. ∎ (B1.)

*Remark.* `φ` is positive semidefinite iff `p ≥ q` and `p + q ≥ 2r`; at `(5,2,4)`
it is indefinite. Nothing below uses definiteness.

## Theorem T2 — reflection positivity through site planes

**Statement.** Let `θ = θ_{1,0}` and `P = {x : x_1 ∈ {0, L}}`, `H^+ = {0 ≤ x_1 ≤ L}`,
`H^- = θ H^+`, so `H^+ ∩ H^- = P` and `H^+ ∪ H^- = T_L`. For every function `F`
of the values on `H^+`: `E_L[F · (F∘θ)] ≥ 0`. The same holds for every
`θ_{i,k}`. No condition on `φ` is needed.

*Proof.* Split the bonds: those with both endpoints in `P` (weight `W_P`),
those with both endpoints in `H^+` not both in `P` (`W^+`), and the mirror set
(`W^-`); every bond is in exactly one class, and `W^-(v) = W^+(θv)` because `θ`
maps the second class onto the third and `φ` is symmetric. Then
`Z_L E_L[F · F∘θ] = Σ_{v_P} W_P(v_P) [Σ_{v_{H^+∖P}} F(v_{H^+}) W^+(v_{H^+})] [Σ_{v_{H^-∖P}} F(θv) W^-(v)]`,
and the change of variables `v ↦ θv` in the last bracket shows it equals the
first bracket. Each summand is `W_P · G(v_P)²` with `W_P > 0`. ∎ Executed:
twenty pseudo-random `F` on the ring of four sites and five on the `4×2` torus,
at `(3,1,2)` and at the indefinite triple `(5,2,4)` (B2).

## Theorem T3 — the chessboard estimate

**Statement.** Let `S` be a set of cells and, for `c ∈ S`, `A_c` an event
depending on the values at the corners of `c`. For `c' ∈ T_L` let `A_c^{(c')}` be
the image of `A_c` in the cell `c'` under a composition of site reflections
carrying `c` to `c'` (the images of the events used below do not depend on
the composition), and let `A_c^{diss} = ∩_{c'} A_c^{(c')}`. Then
`μ_L(∩_{c∈S} A_c) ≤ Π_{c∈S} μ_L(A_c^{diss})^{1/N}`.

*Proof.* The bilinear form `(F, G) ↦ E_L[F · G∘θ]` on functions of `H^+` is
positive semidefinite by T2, so it satisfies the quadratic-form inequality
`E_L[F · G∘θ] ≤ E_L[F · F∘θ]^{1/2} E_L[G · G∘θ]^{1/2}`. Fix the direction `1` and
write the torus as `2L` slabs of cells `{k ≤ x_1 ≤ k + 1}`. For a product of
indicator functions `Π_k 1_{B_k}` with `B_k` an event of slab `k`, reflect
through the plane `x_1 = 1` (between slabs `0` and `1`) with `F = Π_{k ≤ 0}`,
`G = Π_{k ≥ 1}` (indices modulo `2L`; the two halves are `L` slabs each):
`μ_L(∩_k B_k) ≤ μ_L(∩_{k≤0} B_k ∩ θ(∩_{k≤0} B_k))^{1/2} μ_L(∩_{k≥1} B_k ∩ θ(∩_{k≥1} B_k))^{1/2}`.
Each factor's event is again a product over slabs, now with the pattern of
events symmetric about the plane; iterating with the reflections through
`x_1 = 2, 3, …` (each time halving the number of "original" slab positions
and doubling their reflected copies) gives, after `log_2(2L)`-many steps when
`2L` is a power of two and by the standard refinement otherwise,
`μ_L(∩_k B_k) ≤ Π_k μ_L(B_k^{(1)})^{1/(2L)}`, where `B_k^{(1)}` is the event `B_k`
disseminated to every slab position along direction `1`. Apply the same
argument in direction `2` to the events `B_k^{(1)}` (each is a product over
the direction-`2` slabs of reflected copies), and then in direction `3`; the
exponents multiply to `1/N`, and the fully disseminated event of `A_c` is
`A_c^{diss}`. For the bond events used below, "the direction-`i` bond at the
origin corner of the cell is bad", the image in every cell is "the
corresponding bond is bad" whatever the path of reflections, and the
disseminated event is "every direction-`i` bond is bad"; for the joint event
"both canonical bonds of the cell in directions `i, j` are bad", the
disseminated event is contained in the former. ∎ Executed: on the ring,
`μ(bonds (0,1) and (2,3) bad) ≤ μ(all bad)^{2/4}`; on the `4×2` torus,
`μ(two given direction-1 bonds bad) ≤ μ(all direction-1 bonds bad)^{2/8}` (B3).

## Theorem T4 — the disseminated bound

**Statement.** `μ_L(every direction-`i` bond is bad)^{1/N} ≤ 6m/p`.

*Proof.* A configuration in which every direction-`i` bond is bad has weight
at most `m^N p^{(d−1)N}` (each of the `N` bad bonds weighs at most `m`, every
other bond at most `p`), and there are at most `6^N` configurations, so the
numerator is at most `6^N m^N p^{(d−1)N}`; the denominator `Z_L` is at least the
weight `6 p^{dN}` of the six constant configurations. The ratio's `N`-th root
is at most `6^{1 − 1/N} m/p ≤ 6m/p`. ∎ Executed on the ring and the `4×2` torus
at `(3,1,2)` (C1).

**Corollary (bad-bond sets).** Let `B` be a set of `n` bonds. Its bonds occupy
at least `⌈n/d⌉` distinct canonical cells; attaching to each such cell the
event that its bonds in `B` are all bad and applying T3 with T4,
`μ_L(every bond of B is bad) ≤ (6m/p)^{n/d}`.

## Theorem T5 — long-range order on the two-dimensional torus

**Statement.** Let `d = 2` and `ε = 6m/p ≤ 1/36` (i.e. `p ≥ 216 m`); let
`L' ≥ 10`, `L ≥ 2L' + 2` and `x ∈ T_L` with `|x|_∞ ≤ L'/2`. Then
`μ_L(v_0 ≠ v_x) ≤ 5/24 + 18 L' 2^{−L'} ≤ 295/768 < 1/2`.

**Lemma (planar cut–cycle duality; the named import).** Let `Λ ⊂ T_L` be the
box `[−L', L']²`, a plane graph, and `Λ^*` its dual with the outer face as one
vertex. If a set `B` of bonds of `Λ` meets every path in `Λ` from `0` to `x`, then
`B` contains a subset whose dual edges form a simple cycle of `Λ^*`; the cycle
either avoids the outer-face vertex and then encloses exactly one of `0, x`,
or passes through it and then its remaining edges form a dual path from the
boundary of `Λ` to the boundary of `Λ` separating `0` from `x`. (Planar cut–cycle duality; its topological input is the separation theorem
for lattice polygons; both named under Imports.)

**Lemma (contour counts).** The number of simple dual cycles of length `n`
enclosing `0` and avoiding the boundary is at most `(n/2) 3^{n−1}` (the cycle
crosses the horizontal half-line from `0` at one of at most `n/2` dual edges
within distance `n/2`, and from there is a self-avoiding closed walk with at
most `3` choices per step). The number of dual paths of length `n` starting at
the boundary of `Λ` is at most `(8L' + 4) 3^{n} ≤ 9L' · 3^n` for `L' ≥ 4` (the box
has `8L' + 4` boundary bonds); a boundary-to-boundary dual path separating `0`
from `x` has length at least `L'`: both points lie at distance at least `L'/2`
from the boundary, a lattice path joins them inside the box `|·|_∞ ≤ L'/2`, the
dual path must cross it, and so travels at least `L'/2` from the boundary and
back.

*Proof of T5.* If `v_0 ≠ v_x`, every path from `0` to `x` in `Λ` contains a bad
bond, so the bad bonds meet every such path and the duality lemma applies.
Case (a), a cycle of length `n ≥ 4` enclosing `0` (or `x`): by the corollary of
T4 with `d = 2` and the count, the probability is at most
`2 Σ_{n ≥ 4, even} (n/2) 3^{n−1} ε^{n/2} ≤ (1/3) Σ_{n ≥ 4} n y^n` with `y = 3ε^{1/2} ≤ 1/2`,
and `Σ_{n≥4} n y^n = y^4 (4 − 3y)/(1 − y)^2 = 5/8` at `y = 1/2`, giving `5/24`.
Case (b), a boundary-to-boundary path: at most
`9L' Σ_{n ≥ L'} 3^n ε^{n/2} = 9L' y^{L'}/(1 − y) ≤ 18 L' 2^{−L'}`, which is
`45/256` at `L' = 10` and decreasing beyond. The sum is at most
`5/24 + 45/256 = 295/768 < 1/2`. ∎
Executed: the cycle counts for lengths `4, 6, 8` by exhaustive enumeration
against the bound (C2); the series identity and its value `5/8` at `y = 1/2`
symbolically and exactly (C3); the winding bound `45/256` at `L' = 10`, the total `295/768` and the
threshold `p_0 = 216 m` (C4); an illustration on the `4×2` torus at `p = 432`,
`m = 2` (C5).

## Theorem T6 — from long-range order to several Gibbs states

**Statement.** Let `d = 2` and `p ≥ 216 m`. Every limit point `μ` of `(μ_L)_L`
(in the topology of local functions) is a translation-invariant Gibbs state of
the static specification with `μ(v_0 = v_x) ≥ 1/2` for every `x`. The static
law on `Z²` has at least two Gibbs states; every extremal state of the
symmetry orbit generated from a non-symmetric extremal state is distinct, and
the orbit has between two and six members.

*Proof.* (i) *Limit points exist and are Gibbs.* The laws of the values on any
fixed finite box are probabilities on a finite set, so a subsequence
has a limit on every local function (diagonal extraction), and the limit is a
probability on `M^{Z^d}` by the extension theorem for consistent finite-dimensional laws (cited at
definition level, as in block 08). For a finite `Λ` and `L` large enough that the torus
neighbourhood of `Λ` coincides with its `Z^d` neighbourhood, the torus law's
conditional law of `v_Λ` given the rest is `γ_Λ` (the weights are
nearest-neighbour), so `μ_L(f) = μ_L(γ_Λ f)`; `γ_Λ f` is local, so the identity
passes to the limit: `μ(f) = μ(γ_Λ f)`. (ii) *Translation invariance:* `μ_L` is
invariant under torus translations, and for a fixed translation and local `f`
the identity `μ_L(f∘τ) = μ_L(f)` holds for all large `L`. (iii) *Long-range
order:* `μ(v_0 = v_x) = lim μ_L(v_0 = v_x) ≥ 1/2` by T5. (iv) *Uniqueness would
contradict (iii).* Suppose the Gibbs state is unique; call it `ν`; then `ν = μ`,
and `ν` is invariant under the cube group acting on values (the image of a
Gibbs state under a symmetry of `φ` is a Gibbs state), so `ν(v_0 = a) = 1/6`
for every `a`. *Unique implies tail-trivial:* if `T` is a tail event with
`0 < ν(T) < 1`, then `ν(· | T)` is a Gibbs state — for local `f`,
`ν(f 1_T) = ν(γ_Λ(f 1_T)) = ν(1_T γ_Λ f)` because `1_T` is `F_{Λ^c}`-measurable
and `γ_Λ` acts on the `Λ`-values only — and so is `ν(· | T^c)`; they differ, a
contradiction. *Tail-trivial implies short-range correlations:* for local `f`,
`E_ν[f | F_{Λ_n^c}] → E_ν[f | tail] = ν(f)` in `L¹(ν)` as `n → ∞` by the backward
martingale theorem (named import); for `x` outside `Λ_n` and local `g`, the
function `g∘τ_x` is `F_{Λ_n^c}`-measurable, so
`|ν(f · g∘τ_x) − ν(f) ν(g)| = |ν((E_ν[f | F_{Λ_n^c}] − ν(f)) g∘τ_x)| ≤ ‖g‖_∞ ν|E_ν[f|F_{Λ_n^c}] − ν(f)|`,
which tends to zero. With `f = 1_{v_0 = a}`, `g = 1_{v_0 = a}` and the sum over
`a`: `ν(v_0 = v_x) → Σ_a ν(v_0 = a)² = 1/6 < 1/2`, contradicting (iii). Hence
at least two Gibbs states. (v) *The orbit.* `μ` is a mixture of extremal
states (the extremal decomposition of Gibbs states); if every extremal
component were symmetric under the cube group, each would have
`ν_e(v_0 = a) = 1/6` and, being extremal hence tail-trivial, `ν_e(v_0 = v_x) → 1/6`,
so `μ(v_0 = v_x) → 1/6` by exchanging the limit with the integral over the
extremal decomposition (the integrand is bounded by one), contradicting (iii). So some
extremal state has a non-uniform one-site law; its images under the 48
signed permutations are extremal Gibbs states, distinct iff the one-site laws
differ; the number of distinct images is the orbit size of a non-uniform
function on six points under a transitive action, between `2` and `6`. ∎

*Reading.* Below block 03's thresholds one state; above `216 m` in two
dimensions several; the states are told apart by which axis the origin's
record prefers. The band in between is undecided by these two arguments.

## T7 — three dimensions, conditional on one lemma

**The lemma (named import; not re-proved).** In `Z³`, if `A` is a finite
connected set of sites and `B` the set of bonds joining `A` to the unbounded
component of its complement, then the dual plaquettes of `B` form a set
connected under the adjacency "sharing a dual edge" (each dual plaquette has
`12` such neighbours). (Named under Imports.)

**Statement (conditional).** Assume the lemma. Let `d = 3`, `ε = 6m/p` and
`y = 144 ε^{1/3} ≤ 4/5` (i.e. `p ≥ 34,992,000 m`). Then for a box of side
`2L'` inside the torus and `|x|_∞ ≤ L'/2`, `μ_L(v_0 ≠ v_x) ≤ (1/36) Σ_{n≥6} n y^n + (winding term) < 1/2`
for `L'` large, and every limit point of `μ_L` is a Gibbs state on `Z³` with
`μ(v_0 = v_x) ≥ 1/2`; the static law on `Z³` has at least two Gibbs states.

*Proof (given the lemma).* Let `A` be the good cluster of `0` within the box
and suppose `x ∉ A`. If `x` lies in the unbounded component of `A`'s
complement (in the box, the component touching the boundary), the lemma
gives a connected dual surface of bad bonds of size `n ≥ 6` separating `0`
from `x`; otherwise `x` lies in a bounded component and the same lemma applied
to the good cluster of `x` gives a surface around `x`; surfaces that reach the
box boundary have size at least `L'` and are handled like the winding term.
A connected set of `n` plaquettes containing a given plaquette is encoded by a
closed walk of `2(n−1)` steps in the adjacency graph (a depth-first traversal
of a spanning tree), so there are at most `12^{2(n−1)} = 144^{n−1}` of them; the
surface around `0` contains a plaquette crossing the ray from `0` within
distance `n`, at most `n` choices. With the corollary of T4 (`d = 3`):
`μ_L(v_0 ≠ v_x) ≤ 2 Σ_{n≥6} n · 144^{n−1} ε^{n/3} = (1/72) Σ_{n≥6} n y^n`, and
`Σ_{n≥6} n y^n = y^6 (6 − 5y)/(1−y)^2 = 8192/625` at `y = 4/5`, so the bound is
`(1/72)(8192/625) = 1024/5625 < 1/2` with room for the winding term. T6's chain is dimension-free. ∎ Executed: the number of
connected plaquette sets under the `12`-neighbour adjacency for `n ≤ 5` by
enumeration against `144^{n−1}` (D1); the series at `y = 4/5` and the threshold
(D2).

## No-Go Discipline Gate

The negative sentence inside the theorem is "the Gibbs state is not unique"
(T6, T7); the positive conclusion rests on it. Proved for `d = 2` at
`p ≥ 216 m`; conditional for `d = 3`.

### N1 — Routes by which the state could still be unique above the threshold

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a symmetric unique state with long-range order | `ν(v_0 = v_x) ≥ 1/2` for a tail-trivial `ν` | tail triviality forces `ν(v_0 = v_x) → 1/6` (T6 iv) | RULED OUT AT SCOPE |
| 2 the torus limits not being Gibbs | boundary effects | the torus law's conditional laws inside a box are the specification's kernels for large `L` (T6 i) | RULED OUT AT SCOPE |
| 3 failure of the chessboard estimate for bond events | events not attached to cells | bond events are cell events (the corner values), disseminated by site reflections (T3) | RULED OUT AT SCOPE |
| 4 the three-dimensional contour lemma failing | a minimal separating set that is not dual-connected | named import; the `Z³` conclusion is conditional on it (T7) | OBLIGATION NAMED |
| 5 the band between block 03's thresholds and `216 m` | anything | undecided; not claimed either way | open |

### N2 — Wall-independence audit
Walls: the static reading, the six-axis menu, positivity of the weights, the torus with even side. Independent; each defines the object.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: "canonical cell" is a defined term; none in the theorems otherwise.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 03 (main): the uniqueness region | the weak-coupling side | the other side; the undecided band named | yes |
| block 01 (main): the static reading | the object | the object | yes |
| block 12 (PR #8146, open; not an input) | the formation law's phase | the contrast in the boundaries | context only |
| planar cut–cycle duality with the separation theorem for lattice polygons; the backward martingale theorem; the dual-surface connectivity lemma | standard mathematics | named imports at definition level (T5, T6, T7) | declared |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "not unique above the threshold" | executed: the eigenvalues; the 48 symmetries; the series identities; the counts | executed: every configuration of the ring and the `4×2` torus in T2–T4 | executed: the chessboard instances; the disseminated ratios | executed: the two-dimensional illustration on the `4×2` torus at `p = 432` | proved for every positive triple with `p ≥ 216 m` on `Z²` (T5–T6); conditional on `Z³` (T7) |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling; none is a wall. The thresholds are existence constants and are not claimed optimal.

### N7 — Steelman
Hostile reviewer: "Textbook chessboard–contour argument with an absurd constant, and the interesting dimension is conditional." Reply: the two-dimensional theorem is unconditional and exact for this rule with every step re-proved except three named standard imports; the site-reflection observation removes the positive-definiteness condition that the bond-reflection route would need; the three-dimensional constant and the single missing lemma are stated precisely so that the remaining work is named. Conceded: the constants are crude and the band is wide.

### N8 — Cross-cycle echo
Block 03 (uniqueness by one-site contraction) and this note are the two sides of the same question for the static reading; block 12's obligation is the formation law's counterpart, untouched here.

## Falsifiers
- An eigenvalue of `φ` outside the three listed, or a signed permutation not preserving `φ` (B1).
- A function `F` on the ring or the `4×2` torus with `E[F · F∘θ] < 0` (B2); a chessboard instance violated (B3); a disseminated ratio above `(6m/p)^N` (C1).
- A count of enclosing dual cycles of length `4, 6` or `8` above `(n/2) 3^{n−1}`, a series value at `y = 1/2` other than `5/8`, or a winding bound at `L' = 10` other than `45/256` (C2–C4); the `4×2` illustration at `p = 432` below `1/2` (C5).
- A connected plaquette set count for `n ≤ 5` above `144^{n−1}`, or the three-dimensional series at `y = 4/5` at or above `1/2` (D1–D2).

## Boundaries and non-claims
This note proves long-range order and the existence of at least two Gibbs states for the static six-axis law on `Z²` when `p ≥ 216 max(q, r)`, and states the same on `Z³` for `p ≥ 34,992,000 max(q, r)` conditional on the named dual-surface connectivity lemma; it does not claim optimal thresholds, says nothing about the band between block 03's thresholds and these, says nothing about the formation law's phase (block 12's obligation stands), does not count the extremal states beyond the orbit bound, and does not select a coupling as physical. No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the three standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 03 (on `main`): the uniqueness side, referenced for the contrast; block 01 (on `main`): the static reading. Proposed, unaudited.
- Re-proved at scope: T1, T2, T3, T4, T5's counts and series, T6's chain except the named theorem.
- Named standard imports at definition level (never as authority for physics): Whitney's planar cut–cycle duality with the Jordan curve theorem for lattice polygons (T5); Kolmogorov's extension and the backward martingale theorem (T6); Timár's dual-surface connectivity lemma for `Z³` (T7, on which T7 is conditional).
- Reference only (named, not used): the Fröhlich–Israel–Lieb–Simon method and Biskup's lecture notes for the chessboard route; Peierls's argument.

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane and take it; no subagents). The control (`specs/supervisor_control_block17_static_order.py`) computed the spectrum, reflection positivity and chessboard instances, the disseminated ratio, the connected-set counts and the threshold before the contract; the lens pass is in `GOAL_block17.md`; the primary seat wrote T1–T7 and the runner; the refuting pass (`CHECKER_block17_findings.md`) recomputed reflection positivity by an explicit sum-of-squares decomposition, the chessboard instance by the two-step quadratic-form inequality, the contour counts by a second enumeration, and the series by numeric summation of partial sums. Facts settled while executing: the runner's first expected count of enclosing dual cycles of length six forgot the domino's two orientations (the count is `4`, within the bound); the three-dimensional threshold was first checked in units of `m` against its value at `m = 2`; three tokens the lane forbids as substrings were reworded; the refuting pass's first second-adjacency routine counted collinear bonds and was corrected to the common-unit-square adjacency.

## Verification

```bash
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py --exact
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py --mutation unique_state_above_threshold_claimed
```

Families: A authority and inputs; B the spectrum and symmetry, reflection positivity, the chessboard instances; C the disseminated bound, the two-dimensional counts, series, winding bound, threshold and illustration; D the three-dimensional counts and series; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
