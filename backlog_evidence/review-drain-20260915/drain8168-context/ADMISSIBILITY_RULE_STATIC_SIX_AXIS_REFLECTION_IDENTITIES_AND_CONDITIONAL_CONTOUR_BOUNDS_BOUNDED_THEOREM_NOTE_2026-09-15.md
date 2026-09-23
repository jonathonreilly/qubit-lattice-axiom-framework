---
claim_id: admissibility_rule_static_six_axis_reflection_identities_and_conditional_contour_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Spectrum and signed-permutation symmetry of the positive six-axis pair weight; real site-reflection sum-of-squares identity; full-direction bad-bond event counting; finite torus inequalities and contour arithmetic. Contour and limit implications require explicit independently supplied uniform probability bounds. Unconditional threshold216, long-range order and phase coexistence are not established here."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py
---

# Static six-axis reflection identities and conditional contour bounds

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (declared static model; conditional contour implications; unaudited)

## Result up front

This note retains the spectrum, a real site-reflection sum-of-squares identity, an all-direction counting bound and finite exact controls for a supplied static six-axis product law. It also records what a separately proved uniform bad-bond bound would imply through contour arithmetic and finite-volume limits.

The original phase argument has a gap: site reflections preserve vertex parity, so a reflected canonical bond does not cover all transverse rows. Its reflected event cannot be replaced by the event that every bond in one direction is bad. Consequently the original parameter condition `p ≥ 216 max(q,r)` does not establish long-range order or several Gibbs states here. The full original proof remains in [the recovery manifest](work_history/review_loop/pr8151/original-manifest.json).

The retained arithmetic is `Σ_{n≥4}n/2^n=5/8`, `18·10/2^10=45/256`, and `5/24+45/256=295/768`. These become probability bounds only under the explicit additional hypothesis below. No new framework premise is adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain reflection identities, finite controls and conditional contour implications; the uniform bad-bond bound and unconditional phase conclusion remain open."
conditional_surface_status: "Supplied positive six-axis static model; conditional probability implications explicitly separated from proved identities."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
The original phase verdict and negative certification are deferred. No static/formation Green-function comparison is a premise or conclusion.

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

The linked uniqueness note supplies model context and a separate weak-coupling question; its threshold is not used here. The finite static measure and specification are defined below. Site-reflection positivity is a direct sum of squares. Peierls contour counting, the Whitney planar cut–cycle/Jordan separation result, and the Kolmogorov extension and backward martingale theorems provide the named mathematical context and imports specified below. They do not repair the missing uniform bad-bond probability bound.

## Exact target and obligation graph

| Object | Retained scope |
|---|---|
| Spectrum and signed permutations | Exact algebra on the six-axis matrix |
| Site reflection | Real-valued half-torus functions; positive symmetric weights |
| Finite inequalities | The two explicitly enumerated ring/torus probability comparisons only |
| All-direction counting | Correct event; `p≥m` counting regime, `p<m` trivial regime |
| Contour arithmetic | Counts and series; probability implication conditional on uniform planar bad-bond hypothesis |
| Torus limits | Existence/specification identity; uniqueness contradiction conditional on a separately supplied uniform correlation lower bound |
| Three dimensions | Finite cube control and conditional planar argument; no unconditional phase result |

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
`H^- = θ H^+`, so `H^+ ∩ H^- = P` and `H^+ ∪ H^- = T_L`. For every real-valued function `F`
of the values on `H^+`: `E_L[F · (F∘θ)] ≥ 0`. The same holds for every
`θ_{i,k}`. No positive-semidefinite matrix condition on `φ` is needed; its symmetric positive entries remain required.

*Proof.* Split the bonds: those with both endpoints in `P` (weight `W_P`),
those with both endpoints in `H^+` not both in `P` (`W^+`), and the mirror set
(`W^-`); every bond is in exactly one class, and `W^-(v) = W^+(θv)` because `θ`
maps the second class onto the third and `φ` is symmetric. Then
`Z_L E_L[F · F∘θ] = Σ_{v_P} W_P(v_P) [Σ_{v_{H^+∖P}} F(v_{H^+}) W^+(v_{H^+})] [Σ_{v_{H^-∖P}} F(θv) W^-(v)]`,
and the change of variables `v ↦ θv` in the last bracket shows it equals the
first bracket. Each summand is `W_P · G(v_P)²` with `W_P > 0`. ∎ Executed:
twenty pseudo-random real `F` on the ring of four sites at each of `(3,1,2)` and `(5,2,4)`, and three on the `4×2` torus at `(3,1,2)` only (B2). A complex-valued version requires conjugation; the stated square identity is real.

## Theorem T3 — finite probability comparisons and the dissemination gap

**Finite controls.** At `(3,1,2)`, the runner enumerates a ring of four and the periodic `4×2` torus, with doubled bonds in the side-two direction. It checks `μ(bonds (0,1),(2,3) bad)^2 ≤ μ(all ring bonds bad)` and the explicitly selected two horizontal torus bonds satisfy `μ(two bad)^4 ≤ μ(all horizontal bad)`. These are exact finite inequalities, not a general dissemination proof.

**Unresolved dissemination step.** A site reflection sends `x_i` to `2k−x_i`, preserving vertex parity. A canonical horizontal bond therefore visits only even transverse rows. On side four its orbit contains eight of sixteen horizontal bonds in two dimensions, and sixteen of sixty-four in three dimensions. The original substitution of the all-direction event for this reflected event is invalid. At independent spins on the `4×4` torus, the actual reflected event has probability `1225/5184`, whereas the all-direction event has probability `1500625/26873856`, as recorded by the independent review control. These control values diagnose the source gap; the current primary does not recompute them. The original general chessboard/dissemination argument is preserved in the archive, with its conclusion deferred.

## Theorem T4 — the all-direction bad-bond count

**Statement.** `μ_L(every direction-`i` bond is bad)^{1/N} ≤ 6m/p`.

*Proof for `p≥m`.* A configuration in which every direction-`i` bond is bad has weight
at most `m^N p^{(d−1)N}` (each of the `N` bad bonds weighs at most `m`, every
other bond at most `p`), and there are at most `6^N` configurations, so the
numerator is at most `6^N m^N p^{(d−1)N}`; the denominator `Z_L` is at least the
weight `6 p^{dN}` of the six constant configurations. The ratio's `N`-th root
is at most `6^{1 − 1/N} m/p ≤ 6m/p`. ∎ Executed on the ring and the `4×2` torus
at `(432,1,2)` (C1).


For `p<m`, the claimed root bound is trivial: a probability has root at most one, while `6m/p>1`. This bound concerns the all-direction event only; it supplies no bound for arbitrary specified bond sets.

## Theorem T5 — conditional planar contour bound

**Additional unproved hypothesis.** For all planar bond sets `B` needed in the separating contour argument, assume a uniform bound `μ_L(B all bad)≤ε^{|B|/2}`, with `0<ε≤1/36`, for the full family of tori under discussion. This hypothesis is not supplied by the all-direction counting bound or by the finite controls. In particular, this note has not established it with `ε=6m/p`.

**Conditional statement.** Under that hypothesis in `d=2`, let
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
Case (a), a cycle of length `n ≥ 4` enclosing `0` (or `x`): by the additional uniform bad-bond hypothesis and the count, the probability is at most
`2 Σ_{n ≥ 4, even} (n/2) 3^{n−1} ε^{n/2} ≤ (1/3) Σ_{n ≥ 4} n y^n` with `y = 3ε^{1/2} ≤ 1/2`,
and `Σ_{n≥4} n y^n = y^4 (4 − 3y)/(1 − y)^2 = 5/8` at `y = 1/2`, giving `5/24`.
Case (b), a boundary-to-boundary path: at most
`9L' Σ_{n ≥ L'} 3^n ε^{n/2} = 9L' y^{L'}/(1 − y) ≤ 18 L' 2^{−L'}`, which is
`45/256` at `L' = 10` and decreasing beyond. The sum is at most
`5/24 + 45/256 = 295/768 < 1/2`. ∎
Executed: the cycle counts for lengths `4, 6, 8` by exhaustive enumeration
against the bound (C2); the series identity and its value `5/8` at `y = 1/2`
symbolically and exactly (C3); the winding bound `45/256` at `L' = 10`, the total `295/768` and the
algebraic substitution `6m/p_0=1/36` at `p_0=216m`, not a proved phase criterion (C4–C5); a separate finite illustration on the `4×2` torus at `p = 432`,
`m = 2` (C6).

## Theorem T6 — conditional torus-limit implication

**Conditional implication.** For the supplied finite positive nearest-neighbour specification, torus local limits exist and are translation-invariant Gibbs states. Separately assume a sequence of tori has `μ_L(v_0=v_x)≥1/2` uniformly for each fixed displacement once the torus is sufficiently large, or along an unbounded coordinate-plane family of displacements in three dimensions. Then any resulting limit has that correlation lower bound, and uniqueness would contradict it by the argument below. This is a conditional implication, not a proof that the hypothesis holds at any coupling specified here.

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
order:* `μ(v_0 = v_x) = lim μ_L(v_0 = v_x) ≥ 1/2` by the additional correlation hypothesis. (iv) *Uniqueness would
contradict (iii).* Suppose the Gibbs state is unique; call it `ν`; then `ν = μ`,
and `ν` is invariant under the cube group acting on values (the image of a
Gibbs state under a symmetry of `φ` is a Gibbs state), so `ν(v_0 = a) = 1/6`
for every `a`. *Unique implies tail-trivial:* if `T` is a tail event with
`0 < ν(T) < 1`, then `ν(· | T)` is a Gibbs state — for local `f`,
`ν(f 1_T) = ν(γ_Λ(f 1_T)) = ν(1_T γ_Λ f)` because `1_T` is `F_{Λ^c}`-measurable
and `γ_Λ` acts on the `Λ`-values only — and so is `ν(· | T^c)`; they differ, a
contradiction. *Tail-trivial implies short-range correlations:* for local `f`,
`E_ν[f | F_{Λ_n^c}] → E_ν[f | tail] = ν(f)` in `L¹(ν)` as `n → ∞` by the backward
martingale theorem (named import); for fixed local `g` and `x` far enough that its translated support lies outside `Λ_n`, the
function `g∘τ_x` is `F_{Λ_n^c}`-measurable, so
`|ν(f · g∘τ_x) − ν(f) ν(g)| = |ν((E_ν[f | F_{Λ_n^c}] − ν(f)) g∘τ_x)| ≤ ‖g‖_∞ ν|E_ν[f|F_{Λ_n^c}] − ν(f)|`,
which tends to zero. With `f = 1_{v_0 = a}`, `g = 1_{v_0 = a}` and the sum over
`a`: `ν(v_0 = v_x) → Σ_a ν(v_0 = a)² = 1/6 < 1/2`, contradicting (iii). Thus uniqueness contradicts the supplied correlation hypothesis. ∎
No orbit bound between two and six is retained. A nonuniform six-value marginal may have 48 cube-group images. Different one-site marginals distinguish states, but equal one-site marginals do not identify states. The original extremal-orbit paragraph is preserved only in the complete historical proof.

## Theorem T7 — conditional in-plane argument and finite cube control

**Conditional planar reduction.** Take a coordinate plane containing `0` and `x`. If their values differ, every path joining them inside that plane crosses a bad in-plane bond. The planar separation/counting argument applies to this event if a uniform bound `μ_L(B all bad)≤ε^{|B|/2}` has separately been proved for all required in-plane bond sets, with `ε≤1/36`. Under that additional hypothesis, the contour sum above and the conditional limit argument apply along displacements in the plane. The three-dimensional all-direction counting bound does not establish this hypothesis.

**Finite control.** The primary enumerates the periodic `2×2×2` torus at `(432,1,2)`, with each adjacent pair carrying two bonds. It checks the all-direction bound and a nearest-neighbour agreement probability above one half. These finite facts do not establish long-range order, the uniform in-plane hypothesis or phase coexistence on `Z³`.

## No-Go Discipline Gate

### N1 — Deferred negative certification
The original route list did not contain five distinct exact-target attacks. The unconditional nonuniqueness/phase conclusion remains deferred together with the incomplete negative certificate. Full original proofs and branches remain recovery sources.

### N2 — Conditions
The static reading, six-axis menu, positivity and torus model are declared mathematical conditions. The additional uniform bad-bond or correlation hypothesis is explicitly unproved here, not a new axiom and not a renamed conclusion.

### N3 — Source gap
Site reflections preserve parity. The actual reflected event and all-direction event have different geometry and different probabilities. No finite example fills this uniform gap.

### N4 — Imports
Planar separation, consistent-law extension and the backward martingale theorem are the standard mathematical imports named below. The uniqueness parent is context only; no strong-coupling result comes from it.

### N5 — Resolution
The spectrum and finite matrices/tori are executed domains. Contour formulas are exact arithmetic. Written conditional implications are checked arguments, not infinite-lattice executions.

### N6 — Primitive boundary
No primitive supplies a coupling, a probability bound or a selected state.

### N7 — Outstanding obligation
A valid uniform probability bound with correct reflected geometry and normalization is still required before deriving a phase conclusion. Equal one-site marginals cannot identify Gibbs states.

### N8 — Recovery
Original proof histories, controls and outputs are archived without promoting them to current evidence. The historical refuter calls a removed routine and cannot reproduce its output against the current primary unchanged.

## Falsifiers

A failed spectrum identity or signed-permutation invariance; a negative real reflection quadratic form; failure of a stated finite probability comparison or all-direction count; incorrect cycle counts `1,4,22` at lengths `4,6,8`; or incorrect series values would falsify the retained result. A counterexample to the additional unproved uniform probability hypothesis would affect a proposed application of the conditional argument, not turn that hypothesis into a theorem.

## Boundaries and non-claims

This note proves reflection identities, all-direction counting and finite controls, and gives explicitly conditional contour and limit implications; unconditional strong-coupling phase conclusions and the original state-orbit bound are deferred, and no coupling is selected as physical.

No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The static model and extra probability hypotheses are declared mathematical conditions; standard mathematical imports are explicitly named.

## Imports

The linked axiom memo supplies only its quoted sentences. The linked one-site uniqueness note provides model context and no strong-coupling conclusion. The finite static law and local conditional specification are defined here.

For the conditional contour step: Whitney planar cut–cycle duality and the Jordan separation theorem for lattice polygons, in the exact separation form stated above. For torus local limits: Kolmogorov extension for consistent finite-dimensional laws. For the conditional uniqueness contradiction: the backward martingale theorem in `L¹` for decreasing exterior sigma-fields. These are mathematical imports, not physical premises. No extremal-decomposition theorem is required by the retained proof.

Peierls and the Fröhlich–Israel–Lieb–Simon/Biskup treatment name historical mathematical context only; their names do not supply the missing probability bound.

## Review record

The original complete proof, author controls and outputs are preserved in the recovery manifest. The old control uses simple vertical pairs, whereas the current side-two torus doubles those bonds. The historical refuter calls a removed helper and is source-dependent evidence, not a current reproducible control. The independent original reviewer found the parity/dissemination gap and the false six-image bound. This author repair awaits that same reviewer's affected-source confirmation; no primary has been executed for this draft.

## Verification

```bash
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py --exact
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.py --mutation unique_state_above_threshold_claimed
```

Families: A authority and inputs; B the spectrum and symmetry, reflection positivity and finite probability comparisons; C the all-direction count, contour arithmetic, parameter substitution and illustration; D the three-dimensional all-direction count and illustration on the `2×2×2` torus; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
