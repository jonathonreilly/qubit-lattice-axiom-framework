---
claim_id: sphere_formation_kernel_sensitivity_and_level_contraction_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For the supplied sphere exponential kernel, records-only reading and three-predecessor synchronous level order: all-parameter moment and sensitivity bounds; measurable causal contraction q=sqrt(3) beta; compact-Feller invariant-law existence and uniqueness for 0<=beta<1/sqrt(3); finite-marginal exponential approach and absolute aligned magnetization bound; exact one-site recursion and positive mean-map inequalities. Formal negative route certification is deferred outside this row. No physical kernel, menu, order or threshold is selected."
upstream_dependencies:
  - minimal_axioms
runner: scripts/sphere_formation_kernel_sensitivity_level_contraction_check_2026_09_16.py
---

# Sphere-kernel sensitivity and contraction of the supplied level law

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support; supplied-model theorem, unaudited.
**Primary runner:** [exact finite checks](../scripts/sphere_formation_kernel_sensitivity_level_contraction_check_2026_09_16.py).
**Cache destination:** [source-bound stdout](../logs/runner-cache/sphere_formation_kernel_sensitivity_level_contraction_check_2026_09_16.txt).

## Result up front

For the supplied kernel and synchronous level order below, the total-variation
sensitivity is at most `|V−V'|/(2√3)`. A measurable causal coupling contracts
expected chordal distance per site by `q=√3β` per level. For `0≤β<1/√3`,
compactness and the Feller property give an invariant law, the contraction
makes it unique and rotation invariant, and every initial law approaches it
in finite marginals with the stated explicit bound. The aligned magnetization
satisfies `|m_t|≤q^t`. The one-site periodic law has exact rate `A(3β)^t`.
All four original argument surfaces survive: sensitivity, invariant-law
contraction, magnetization/one-site recursion, and mean-map bounds. The
complete corrected uniform-route ceiling is readable deferred science in
[recovery](work_history/review_loop/pr8171/README.md), not a conclusion of this
bounded row. Finite symbolic controls do not execute an infinite level plane.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Behavior outside the supplied contraction region and physical selection of kernel, menu and order remain open."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Study larger-coupling behavior using an explicitly defined coupling or finite-block mechanism."
conditional_surface_status: "Supplied sphere kernel, records-only reading and synchronous three-predecessor level order; standard compact probability imports stated below."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared objects

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the framework
boundary: "There is one fixed nearest-neighbor admissibility rule, covariant
under lattice translations and proper cubic rotations.", "For each site, the
probability distribution over the possibilities is determined by, and varies
with, the nearest-neighbor conditions.", "Records form.", and "Only records
are readable." The following kernel, menu, reading and order are additional
supplied mathematical conditions, not selected by those sentences.

The current finite-menu formation/static note
`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`
is context for the terminology only. No classification or static-law theorem
is imported from it; the sphere proof below is self-contained. The primary
checks that historical context identity and binds its current bytes as a
context input, which is not a mathematical dependency edge.

- Values are unit vectors `s∈S²`; `β≥0` is supplied. Write `κ=|V|`,
  `û=V/|V|` for V≠0, `A(κ)=cothκ−1/κ`, `A(0)=0`, and
  `K_V(ds)=(κ/(4π sinhκ)) exp(V·s)dσ(s)`, uniform at V=0.
  Here dσ is sphere area measure; `F(V)=E[s]=A(κ)û`, F(0)=0.
- A level is `X=(S²)^{Z²}`. The new spin at coordinate `(i,j)` has law
  `K_{βS}`, where `S=s_(i,j)+s_(i−1,j)+s_(i,j−1)` from the preceding
  level. Sites draw independently conditional on that level. These are the
  three predecessors `x−e_j` in the supplied monotone level order on `Z³`.
- Chordal distance is `|s−s'|≤2`. `TV=(1/2)∫|f−g|dσ`, and
  `W_1=inf E|s−s'|` on the sphere. For a specified joint level coupling γ,
  `D(γ)=sup_x E_γ|s_x−s'_x|`; for laws define
  `d_∞(μ,ν)=inf_γ D(γ)`. Bounds below construct couplings, without assuming
  the infimum is attained. Finite marginal metrics use the sum of chordal
  distances over the specified finite set.
- For a fixed unit e, the aligned initial plane is identically e and
  `m_t=E[s_x·e]`. Translation invariance makes this independent of x.

## Imports

Standard mathematical imports are the existence of countable product
probability measures and iterated kernels on standard Borel spaces; compactness
of countable products of compact metric spaces; weak sequential compactness
of probability measures on a compact metric space; uniform density of continuous
cylinder functions; and determination of a countable-product law by its finite
marginals. Every use and its hypotheses appear below. No external theorem
supplies the kernel, order or physical interpretation. The finite-menu context
is not needed for these imports. No primitive supplies a state-selection rule.

## Exact target and obligation graph

| Argument | Claim and proof obligation | Finite primary coverage |
|---|---|---|
| Sphere sensitivity (T1) | direct moments, entire-series sign and continuity at zero | symbolic identities, 12 coefficients, ten rational enclosures |
| Level contraction (T2) | measurable common-density coupling, compact-Feller existence, finite-marginal uniqueness | contraction factor and two boundary enclosures |
| Magnetization (T3) | antipodal absolute-value inequality and conditional-mean recursion | six one-site rate enclosures |
| Mean-map bounds (T4) | linear test function and global entire-series lower bound | series through degree six and five rational enclosures |

## Theorem T1 — the sensitivity of the sphere kernel

**Statement.** For `V, V' ∈ R³`, with `κ = |V|`, `û = V/|V|`, `A = A(κ)`:
(a) `Var_{K_V}(w) = A'(κ) = 1/κ² − 1/sinh² κ`;
(b) for a unit vector `d` with `û·d = c`, `E_{K_V}[((s − Aû)·d)²] = A/κ + (1 − 3A/κ − A²) c²`;
(c) `1 − 3A/κ − A² ≤ 0` for every `κ > 0`, i.e. `A(κ)/κ` is decreasing; and `A/κ ≤ 1/3`;
(d) `TV(K_V, K_{V'}) ≤ |V − V'|/(2√3)` and `W_1(K_V, K_{V'}) ≤ |V − V'|/√3`.

**Proof.** (a) The law of `w` has density `∝ e^{κw}` on `[−1, 1]`, an exponential family in `κ` with log-normalizer `log(2 sinh κ/κ)`, whose first and second derivatives are the mean `A(κ)` and the variance; `A' = 1/κ² − 1/sinh² κ` (B1, symbolically). (b) Direct integration gives `Z(κ)=∫_{−1}^1 e^{κw}dw=2 sinhκ/κ`, `E[w]=Z'/Z=A`, and `E[w²]=Z''/Z=1−2A/κ`. Axial rotation symmetry gives zero transverse means and cross moments; each transverse second moment is `(1−E[w²])/2=A/κ`. Thus `E[s] = Aû` and `E[ssᵀ] = (A/κ)I + (1 − 3A/κ)ûûᵀ`; expand `E[((s − Aû)·d)²] = dᵀE[ssᵀ]d − 2A c (Aû·d) + A²c² = A/κ + (1 − 3A/κ)c² − A²c²` (B2). (c) `1 − 3A/κ − A² ≤ 0 ⇔ κ(1 − A²) ≤ 3A`; since `1 − A²` and `A` are what they are, use instead the equivalent form through (a): the claim is `κ A'(κ) ≤ A(κ)` (indeed `κA' = 1/κ − κ/sinh² κ` and `A = coth κ − 1/κ`, and `1 − 3A/κ − A² = (κA' − A)/κ` because `A² = coth² κ − 2coth κ/κ + 1/κ² = 1 + 1/sinh² κ − 2coth κ/κ + 1/κ²`, so `1 − 3A/κ − A² = −1/sinh² κ − 1/κ² + 2coth κ/κ − 3coth κ/κ + 3/κ² = 2/κ² − 1/sinh² κ − coth κ/κ`, and `(κA' − A)/κ = (1/κ − κ/sinh² κ − coth κ + 1/κ)/κ = 2/κ² − 1/sinh² κ − coth κ/κ`). Multiplying `κA' ≤ A` by `κ sinh² κ`: `sinh² κ − κ² ≤ κ sinh κ cosh κ − sinh² κ`, i.e. `2 sinh² κ ≤ (κ/2) sinh 2κ + κ²`. Both sides are power series with `2 sinh² κ = cosh 2κ − 1 = Σ_{m≥1} (2κ)^{2m}/(2m)!` and `(κ/2) sinh 2κ = Σ_{m≥1} (2κ)^{2m} (m/2)/(2m)!`; the difference is `κ² − κ² + Σ_{m≥2} (2^{2m}/(2m)!)(m/2 − 1) κ^{2m} ≥ 0` (B3: the coefficients `0, 0, 2/45, 2/315, …`). Finally the expansions `sinhκ=κ+κ³/6+O(κ⁵)` and `coshκ=1+κ²/2+O(κ⁴)` give `lim_{κ→0} A(κ)/κ=1/3`. The proved decrease gives `A/κ≤1/3`, strictly for κ>0 because the m=3 coefficient is positive. At κ=0 the uniform law has mean zero and covariance `I/3`, so the directional bound extends continuously. B4 checks ten rational points; the all-parameter bound is this written proof. (d) `f_V(s) = (κ/(4π sinh κ)) e^{V·s}` is smooth in `V` including `V = 0`, with `∂_V log f_V = s − A(κ)û` (as `∂_V log(κ/sinh κ) = (1/κ − coth κ) û = −Aû`). With `δ = V' − V` and `V_t = V + tδ`, `f_{V'} − f_V = ∫_0^1 f_{V_t} (s − A_t û_t)·δ dt`, so `TV(K_V, K_{V'}) ≤ (1/2) ∫_0^1 E_{K_{V_t}}|(s − A_t û_t)·δ| dt ≤ (|δ|/2) sup_t (E[((s − A_t û_t)·δ̂)²])^{1/2} ≤ (|δ|/2) sup_t (A_t/κ_t)^{1/2} ≤ |δ|/(2√3)`, using (b) with (c) (the coefficient of `c²` is non-positive, so the maximum over the angle is at `c = 0`) and `A/κ ≤ 1/3`. Since the chordal distance is at most `2`, the coupling that agrees off the total-variation part gives `W_1 ≤ 2·TV ≤ |δ|/√3`. ∎ (B1–B4.)

*Reading.* The number `1/√3` is the square root of the transverse variance per component of the uniform law; the bound is tight in the direction of the argument only at `V = 0`, where the exact sensitivity is `1/4` (the uniform law's mean absolute cosine is `1/2`).

## Theorem T2 — the causal coupling contracts

**Measurable coupling.** Given densities f=f_V and g=f_V', set h=min(f,g)
and α=∫h dσ. With probability α draw a common point with density h/α;
with probability 1−α draw the two points independently from
`(f−h)/(1−α)` and `(g−h)/(1−α)`. At α=0 or 1 use just the nonzero branch.
This is a measurable probability kernel in (V,V'): the densities and their
integrals are Borel functions, and normalized integrals on each nonzero branch
are measurable. Its marginals are f and g; its expected chordal cost is at
most `2(1−α)=2TV≤|V−V'|/√3`. Countable products give independent site pairs
conditional on the preceding coupled levels. This avoids any measurable
selection of optimal transport plans and needs no additive η error.

**Statement and contraction.** For that coupling, `D_(t+1)≤√3β D_t`.
Indeed at x, condition on the coupled preceding level:
`E[|s_x−s'_x||previous]≤(β/√3)|S_x−S'_x|≤(β/√3)Σ_(j=1)^3 |s_(x−e_j)−s'_(x−e_j)|`.
Take expectations and the supremum over x. Thus `D_t≤2q^t` for `q=√3β`.
At β=0 all new-site laws are uniform and one common draw couples them exactly;
the bound for t≥1 is zero, while the initial bound is D_0≤2.

**Existence.** The countable product X is compact metrizable. The transition
P sends a continuous cylinder function to a continuous cylinder function:
only finitely many predecessor coordinates enter, and their sphere densities
vary continuously, uniformly on compact parameter sets. Dominated integration
gives continuity. Continuous cylinders are uniformly dense in C(X), and P
is a sup-norm contraction, so P maps all C(X) to C(X): it is Feller.
For any initial law ν, take `ν_N=N^(-1)Σ_(t=0)^(N−1)νP^t`.
Compactness of probability laws on X gives a weakly convergent subsequence.
For f∈C(X), `(ν_NP−ν_N)(f)=(νP^N(f)−ν(f))/N→0`.
The Feller property lets the subsequential limit pass through Pf, hence the
limit μ is invariant. This existence argument works at every finite β;
the uniqueness and rate below require q<1.

**Uniqueness.** Let μ,μ' be invariant laws, couple their initial planes
arbitrarily and apply the measurable causal coupling. At each t their marginals
remain μ,μ'. For any finite Λ, the Wasserstein distance of their Λ marginals
for `Σ_(x∈Λ)|s_x−s'_x|` is at most `2|Λ|q^t→0`. Thus every finite marginal
coincides, and μ=μ'. Simultaneous rotations commute with P, so every rotated
μ is invariant and uniqueness makes μ rotation invariant. Couple any initial
law with μ to get `d_∞(νP^t,μ)≤2q^t` and the same finite-marginal bound.
Rotation invariance gives zero one-site mean, hence exponential decay of
one-site magnetization from any initial law. ∎

## Theorem T3 — exponential loss of aligned magnetization

For `0≤β<1/√3`, the aligned plane obeys `|m_t|≤(√3β)^t`.
Run the coupling from e and −e. Rotation by π about an axis perpendicular
to e maps the first marginal process to the second, so their projected means
are m_t and −m_t. Therefore
`2|m_t|=|E[s_x·e]−E[s'_x·e]|≤E|s_x−s'_x|≤2(√3β)^t`.
This uses no unproved nonnegativity of m_t.

On the one-site periodic plane the three predecessors are the same unit spin,
so the T1 mean identity gives
`E[s_(t+1)·e|s_t]=A(3β)(s_t·e)`.
Conditional expectation and m_0=1 give `m_t=A(3β)^t` exactly.
T1 gives `A(3β)≤β`, strictly for β>0. At β=0 the rate is zero after the
first update. These exact one-site conclusions do not assert equality of
one-site and infinite-plane rates. ∎

## Theorem T4 — positive mean-map bounds

For every V,V', `W_1(K_V,K_V')≥|F(V)−F(V')|`. Indeed for any coupling and
unit d, `|(E s−E s')·d|≤E|s−s'|`. Choose d parallel to the mean difference
(the zero case is immediate), then take the infimum over couplings.
For V=0,V'=δd with δ>0, the mean difference is A(δ).

The global bound is `1/3−δ²/45≤A(δ)/δ<1/3` for δ>0.
For the lower bound multiply by the positive number δ² sinhδ. The resulting
expression is
`H(δ)=δ coshδ−(1+δ²/3−δ⁴/45)sinhδ`.
Its coefficient of δ^(2n+1), for n≥1, is
`16n(n−1)(n−2)(n+2)/(45(2n+1)!)`; the n=0 coefficient is zero.
To verify it, combine `2n/(2n+1)!−1/[3(2n−1)!]`
with `1/[45(2n−3)!]` when n≥2. The n=1,2 coefficients vanish and all n≥3
are positive. Entire-series convergence gives H(δ)≥0 for every δ>0.
The upper bound follows from the strict decrease proved in T1.
The series `A(δ)/δ=1/3−δ²/45+2δ⁴/945−δ⁶/4725+…` and five rational
checks are finite corroboration, not the all-δ proof. ∎

## No-Go Discipline Gate

### N1 — Deferred negative certification
The historical packet names four items: sensitivity, coupling independence,
finite-marginal uniqueness and region. These are mostly proof obligations for
the positive theorem, not five distinct attacks against the uniform-route
ceiling. No fifth route is invented and no negative packet PASS is claimed.
The full corrected negative implication is deferred in recovery; the live
mean-map inequalities remain affirmative mathematical bounds.

### N2 — Wall relationships
No independent-wall count is asserted. Kernel, menu and order are joint
supplied hypotheses; their absence is not a proved physical obstruction.

### N3 — Explicit hypotheses
Sphere area measure, exponential kernel, records-only reading, synchronous
three-predecessor order and standard compact-probability imports are named.
The rotation symmetry used here is a property of the supplied kernel.

### N4 — Citation and residual matching
The axiom memo fixes the framework boundary only. The finite-menu note is
context, not authority for sphere moments or infinite-volume uniqueness.
No sibling static-law result or historical simulation closes a residual here.

### N5 — Actual primary resolutions
- per_element: symbolic variance/directional identities, twelve sign coefficients,
  log-density derivatives and finite exact rational bounds.
- per_site: six rational one-site rate checks and five mean-map bound checks;
  no stochastic one-site chains are executed by this primary.
- per_mode: checked and not executed — no spectral decomposition, quadrature,
  Monte Carlo or mode-resolved simulation is called by this primary.
- per_block: the contraction-factor arithmetic and two boundary enclosures;
  no finite block sampler is called.
- lattice_wide: checked and not executed — compactness, measurable coupling and
  infinite-plane uniqueness are written proofs, not finite runner executions.

### N6 — Partial closure and primitives
The accepted surface is the positive supplied-model proof. The deferred
negative argument and every original remain recoverable, with branch retention
required for partial closure. No additional axiom or primitive is adopted.

### N7 — Concrete strongest counter-route
A multistep block coupling could exploit correlations and cancellations lost
by the one-site triangle estimate. Its terminal task is a strict expected block
cost bound for a specified joint transition. State-restricted or alternative
transport costs also remain open. The present positive region is compatible
with success of those routes at larger beta; the deferred ceiling concerns
only the explicitly defined uniform single-predecessor criterion.

### N8 — Historical comparison
The original finite-menu causal-contraction and sphere static-law campaign
comparisons are preserved in recovery. They concern different kernels or
transition/specification objects and supply no additional route closure here.
Historical finite strong-coupling memory plots do not settle an infinite-plane
threshold. No claim of a completed cross-menu phase classification survives.

## Boundaries and non-claims

The sphere kernel, records-only reading and level order are supplied conditions; the theorem makes no physical selection.

The constant `1/√3` is a sufficient contraction bound, not a physical threshold.

Formal negative route certification is deferred; the full corrected argument is preserved as readable recovery science.

## Review record

[Exact history and limitations](work_history/review_loop/pr8171/README.md)
contains all original proof/source/cache/control/refuter versions. Historical
numerical and mutation results remain historical; no corrected-source primary,
simulation or mutation was executed during author preparation. In particular,
the refuter's capped residual-rejection routine can retain unresolved common
draws, and its printed last-level zero does not verify all preceding levels.
Its observed ratios are not promoted as valid exact-marginal coupling evidence.
The primary performs symbolic/rational checks only. The original zero-parameter
sampler failure and historical correction remain available in the archive.

## Verification

The primary's intended completed count is 16: four source checks, four kernel
checks, two contraction/rate checks, one mean-map check, four packaging checks
and one N5 printing check. Ten existing mutations remain available; their old
census is not fresh evidence. The primary emits stdout only, with no JSON
output, simulation or external helper invocation. Written compactness and
all-parameter proofs are separately reviewed mathematical content.
