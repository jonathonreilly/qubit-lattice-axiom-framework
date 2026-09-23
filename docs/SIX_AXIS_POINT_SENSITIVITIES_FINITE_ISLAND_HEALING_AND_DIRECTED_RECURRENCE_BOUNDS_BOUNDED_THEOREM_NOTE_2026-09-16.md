---
claim_id: six_axis_point_sensitivities_finite_island_healing_and_directed_recurrence_bounds_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Exact point evaluations of the positive six-axis product conditional; a finite nonempty-island eroder and noise union bound for a supplied majority automaton; and a nonnegative directed recurrence comparison under an explicitly supplied coefficient. No interval uniqueness region, model coupling or asymptotic memory threshold is asserted."
upstream_dependencies: [minimal_axioms, admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06]
runner: scripts/six_axis_point_sensitivities_finite_island_healing_directed_recurrence_bounds_2026_09_16.py
---

# Six-axis point sensitivities, finite-island healing and directed recurrence bounds

**Type:** bounded_theorem

**Status:** bounded-support; supplied mathematical models; unaudited.

## Result up front

The three results below are exact finite arithmetic, a full finite-island proof and a full recurrence comparison proof. The coefficient in the recurrence is supplied. No coupling for a sphere process is constructed by the recurrence calculation. Historical simulation scans are preserved with their actual protocols in the [recovery record](work_history/repo/review_feedback/pr8172-evidence/README.md); they do not establish permanent memory or a transition threshold.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Exact finite identities and conditional bounds for supplied local models."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independent affected-source confirmation and bounded runner capture; broader model and threshold claims remain deferred."
conditional_surface_status: "Positive six-axis weights, finite nonempty island, independent Bernoulli noise and nonnegative recurrence coefficient are supplied conditions."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework vocabulary. The [finite-window product-rule source](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies the finite six-axis menu and product conditional. Neither selects the weights, synchronous update law, noise or recurrence coefficient as physical. No registered primitive supplies any of those choices.

Let `M={±e₁,±e₂,±e₃}`, and let `φ(v,w)` equal positive `p,q,r` for equal, antipodal and orthogonal pairs. Define

`K(v|a,b,c)=φ(v,a)φ(v,b)φ(v,c)/Σ_w φ(w,a)φ(w,b)φ(w,c)`.

For `(q,r)=(1,2)`, let `c(p)` be the maximum total-variation distance of these conditionals over all 216 predecessor triples and five replacements of their first entry. Total variation is half the sum of six absolute coordinate differences.

On `Z³` write `τ(x)=x₁+x₂+x₃`. For the healing result the supplied process is `η_x=maj(η_{x−e₁},η_{x−e₂},η_{x−e₃})∨ζ_x`, with independent Bernoulli(`ε`) noise for `τ≥1`, `0≤ε≤1`. Initially exactly the nonempty finite set `I⊂{τ=0}` has value one. Set `M_j=max_{i∈I}i_j` and `D=Σ_j M_j≥0`. The nonnegativity follows by comparing the maxima with any island point, whose coordinate sum is zero. Set

`F_T(I)={x:τ(x)=T, x≥i for some i∈I}`,

`U(I)={y:1≤τ(y)≤D+1, y≤x for some x∈F_{D+1}(I)}`.

All coordinate inequalities are componentwise. The empty island is excluded from this definition because its coordinate maxima are undefined. The event refers to a one somewhere in this specified cone, including a noise-created one; it is not genealogical persistence of an original site.

For the recurrence result separately supply `g≥0`, nonnegative arrays `D_t(x)` on level `t`, a level-zero site `x₀`, and

`D₀(x)≤2·1{x=x₀}`, `D_{t+1}(x)≤g Σ_{j=1}^3 D_t(x−e_j)`.

Let `p_t(z)` be the distribution of the sum of `t` independent uniform steps from `{e₁,e₂,e₃}`. In plane coordinates,

`p_t(a,b,t−a−b)=t!/[a!b!(t−a−b)!]·3^(−t)`

when all three coordinates are nonnegative integers, and zero otherwise.

## Exact point evaluations

**Statement.** `3c(37/10)=406962630/413162167<1` and `3c(19/5)=871815/862244>1`. These are two point evaluations, not an interval criterion. The explicit small-p check is `3c(1/10)=87/52>1`; failure of this sufficient numerical inequality does not prove nonuniqueness of any process.

**Proof and finite certificate.** Form the six positive weights above for each ordered triple and each replacement, divide by their exact sum, and take half the sum of absolute differences. There are exactly `216·5` comparisons. This exhaustive rational calculation is implemented by `conditional` and `sensitivity` in the paired runner. It evaluates both displayed maxima as reduced fractions; at the first two points a maximizing pair is `(a,b,c)=(e₁,e₁,e₁)` and replacement `a′=−e₁`. At `p=1/10`, predecessors `(e₂,e₁,−e₁)` and replacement `e₃` attain `87/52` after multiplication by three. The finite enumeration verifies the upper maximum as well as these witnesses; no monotonicity inference between or beyond these inputs is used.

For triples with at least two target entries, permutation and cubic symmetry leave three cases: `(a,a,a)`, `(a,a,−a)` and `(a,a,b)` with `b⊥a`. Their probabilities of a non-target value are respectively

`d₁=(q³+4r³)/(p³+q³+4r³)`,

`d₂=1−p²q/[pq(p+q)+4r³]`,

`d₃=1−p²r/[r(p²+q²)+r²(p+q)+2r³]`.

For the first case, the target, antipode and four orthogonal targets have weights `p³,q³,r³`. For the second they have weights `p²q,pq²,r³`. For the third, enumerating the six possible output values gives weights `p²r,q²r,pr²,qr²,r³,r³`. Summing each list and subtracting the normalized target weight proves the formulas.

At `(p,q,r)=(285717,1,2)` the three fractions are `11/7774759963232282`, `285749/81634489838`, `571445/81634775534`; at `(285718,1,2)` they are `33/23324524793166265`, `142875/40817530637`, `571447/81635346971`. Thus their maximum is greater than `7/10⁶` at the first integer and at most that number at the second, by cross multiplication. This note asserts these two evaluations, without extending them to all larger p or applying a phase theorem. ∎

## Finite-island healing theorem

**Statement.** Under the noiseless majority rule a nonempty finite island `I` is empty at level `D + 1`. Under noise `ε`, `P(η has a one in F_{D+1}(I)) ≤ min(1, |U(I)| ε) ≤ min(1, 18(D + 1)³ ε)`.

**Proof.** *The eroder bound.* If `x` is a one at level `t + 1` with `x_i > M_i(t)` for some `i`, then its two predecessors `x − e_j`, `j ≠ i`, have `i`-th coordinate `x_i > M_i(t)` and are zeros, so `x` has at most one one-predecessor and is not a majority: the coordinate maxima never increase. A one at level `t` has `Σ_i x_i = t` and `x_i ≤ M_i`, so `t ≤ D`: level `D + 1` is empty (C1). *The coupling.* Run the noisy and the noiseless automata with the same island. If no noise site lies in `U(I)`, then by induction on the level every site of `U(I)` and every site of `F_{D+1}(I)` — whose predecessors down to level `1` lie in `U(I)` — carries the same value in both runs, so `F_{D+1}(I)` carries no one. Hence the event has probability at most `P(ζ = 1 somewhere in U(I)) ≤ |U(I)| ε`. *The count.* Fix an island point `i⁰ ∈ I` and translate every lattice coordinate by `−i⁰`. Since `τ(i⁰)=0`, levels and `D` are unchanged, as are the region cardinality and the noise law. In these translated coordinates each maximum `M_j` is nonnegative, so `M_j ≤ D` and every island point obeys `i_j ≤ D`. The following count is in these translated coordinates. A site `y ∈ U(I)` at level `s ∈ [1, D + 1]` satisfies `y ≤ x` for some `x` at level `D + 1` with `x ≥ i`, `i ∈ I`; then `x_j = D + 1 − Σ_{k≠j} x_k ≤ D + 1 − Σ_{k≠j} i_k = D + 1 + i_j ≤ 2D + 1`, so `y_j ≤ 2D + 1 =: B` for each `j`. The number of `y` at level `s` with all `y_j ≤ B` is the number of non-negative `d_j = B − y_j` with `Σ d_j = 3B − s`, i.e. `C(3B − s + 2, 2) ≤ C(6D + 5, 2) = (6D + 5)(6D + 4)/2`; over `D + 1` levels, `|U(I)| ≤ (D + 1)(6D + 5)(6D + 4)/2 ≤ 18(D + 1)³`, the difference being `(D + 1)(9D + 8)` (C2). ∎

The probability of an empty target cone is therefore at least `1−min(1,18(D+1)³ε)`; equality is not asserted. For large D the bound may be vacuous. No ordered-phase hypothesis is needed for this finite assertion. At level t, the third coordinate of a represented site `(a,b)` is `t−a−b`, not `−a−b`.

The region enumerator first translates by an island point. In the normalized coordinates `B=2D+1` is a valid upper bound on all three coordinates. Since `y₁+y₂+y₃=s≥1`, each coordinate is also at least `s−2B≥1−2B`, so the retained wider lower bound `−3B−3` loses no site. A candidate y is in U exactly when `Σ_j max(i_j,y_j)≤D+1` for some i: necessity follows from i,y≤x; conversely raise any coordinate of `max(i,y)` by the nonnegative remaining integer to obtain a level-`D+1` witness x. This proves completeness of the enumeration, including arbitrarily translated islands. The singleton region has three sites; the triangle `{(0,0,0),(1,0,−1),(0,1,−1)}` has 76, invariant under a level-zero translation.

## Directed recurrence comparison theorem

**Statement.** Under the explicitly supplied recurrence hypotheses,

`D_t(x)≤2(3g)^t p_t(x−x₀)` and `Σ_{τ(x)=t}D_t(x)≤2(3g)^t`.

At `t=0` the right hand side is defined as `2·1{x=x₀}`; this also handles `g=0` without an ambiguous power. For `g=0`, all later arrays vanish by the assumed inequality. If `3g<1`, the displayed upper bound decays geometrically.

**Proof.** Define `E₀=2δ_{x₀}` and `E_{t+1}(x)=gΣ_j E_t(x−e_j)`. Nonnegativity and the initial upper bound give `D_t≤E_t` by induction: the inequality at the next level follows by multiplying each predecessor comparison by g and summing. Expanding the equality recursion, each directed path of length t contributes `2g^t`. A site at displacement `(a,b,c)`, `a+b+c=t`, is reached by exactly `t!/(a!b!c!)` paths; this is the multinomial count from choosing the ordered positions of each of the three steps. Consequently `E_t=2g^t·3^t p_t=2(3g)^t p_t`. Summing the normalized walk law, whose total is one by its product construction, gives the level-sum bound. The support is contained in the forward cone by the same induction. ∎

Substituting `g=β/√3` is only an algebraic specialization, giving `2(√3β)^t p_t`. To use it for a coupled sphere process one must separately prove that process satisfies the supplied recurrence, with its exact hypotheses and input identity. For two arbitrary distinct initial directions the chordal distance is at most two, not necessarily equal to two. No sphere coupling theorem from unlanded work is used here.

## Scope and recovery

The current static six-axis reflection result retains conditional contour implications because parity leaves a dissemination gap. The corrected cubic-walk/sphere-static result supplies `β>76/100` as a sufficient supplied-model condition under its zero-field parent and Gaussian-domination import, not a transition location. The current formation stability construction has its own supplied process and small-noise hypotheses. These comparisons are recorded as context with exact current paths in the recovery appendix; none is a premise of the three proofs here.

All original proofs, proposed broader statements, eight original mutations, five historical control/simulation programs and their full raw outputs, and the 79-entry inherited campaign packet are preserved in the recovery record. The false half-line statement and incomplete coupling application are superseded. Actual asymptotic threshold and broad negative certification remain deferred, with their research content and branch retained. Four historical attempted categories do not become five certified routes. No audit verdict is supplied.

## Verification boundary

[The paired runner](../scripts/six_axis_point_sensitivities_finite_island_healing_directed_recurrence_bounds_2026_09_16.py) checks exact fractions, the original 300 seeded finite islands and 120 region counts, translated decisive examples, the original polynomial bound and the recurrence through six steps. These finite controls supplement the complete written proofs; they do not establish a universal theorem by check count. Proposed execution is pending. Its five resolution lines distinguish current exact controls from historical simulations and proof-only general statements. The primary never reads or executes historical simulation programs or outputs.
