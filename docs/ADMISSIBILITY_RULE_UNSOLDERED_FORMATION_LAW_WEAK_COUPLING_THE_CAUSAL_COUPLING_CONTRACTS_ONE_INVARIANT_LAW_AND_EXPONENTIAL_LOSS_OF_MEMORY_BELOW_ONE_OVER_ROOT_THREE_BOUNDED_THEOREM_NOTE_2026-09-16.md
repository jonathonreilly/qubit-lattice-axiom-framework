---
claim_id: admissibility_rule_unsoldered_formation_law_weak_coupling_the_causal_coupling_contracts_one_invariant_law_and_exponential_loss_of_memory_below_one_over_root_three_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For the unsoldered (sphere) formation law of the covariant rule with overlap weight e^{beta s.s'} on Z^3 in level order — the record at x drawn from K_beta(s | s_{x-e_1}, s_{x-e_2}, s_{x-e_3}) proportional to e^{beta s.S}, S the sum of the three recorded predecessors, read as the synchronous level automaton on Z^2: (T1) the kernel K_V(ds) = (|V|/(4 pi sinh|V|)) e^{V.s} dsigma has total-variation sensitivity TV(K_V, K_V') <= |V - V'|/(2 sqrt3) and Wasserstein sensitivity W_1(K_V, K_V') <= |V - V'|/sqrt3 for the chordal distance, through the exponential-family identity Var(w) = A'(kappa), the directional second moment E[((s - A u).d)^2] = A/kappa + (1 - 3A/kappa - A^2)(u.d)^2, the sign lemma 1 - 3A/kappa - A^2 <= 0 (A(kappa)/kappa decreasing, proved by a term-by-term series comparison) and A/kappa <= 1/3 (proved; symbolic and exact); (T2) the causal coupling of two initial planes contracts the per-site expected chordal distance by sqrt3 beta per level, so for beta < 1/sqrt3 the level automaton has exactly one invariant law, invariant under all rotations, and the law of any level from any initial plane is within 2 (sqrt3 beta)^t of it per site (proved); (T3) from the aligned plane the magnetization obeys m_t <= (sqrt3 beta)^t for beta < 1/sqrt3, and on the one-site plane m_t = A(3 beta)^t with A(3 beta) <= beta (proved); (T4) no coupling argument of this kind proves contraction beyond beta = 1, since W_1(K_V, K_V') >= |F(V) - F(V')| with F(V) = A(|V|) V/|V| and A(delta)/delta >= 1/3 - delta^2/45 (proved); the total-variation sensitivity is numerically 1/4 per unit at small |V| (route reach 2/3), the proved constant 1/(2 sqrt3) sits between. The constant 1/sqrt3 is the route's, not a threshold (block 26 executes the loss of memory at every coupling tried); no menu, reading, order or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unsoldered_formation_law_weak_coupling_causal_coupling_contracts_one_invariant_law_2026_09_16.py
---

# The unsoldered formation law at weak coupling: the causal coupling contracts, one invariant law, and exponential loss of memory below `1/√3`

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Block 26 ran the sphere formation law at strong coupling and watched the
memory of its initial plane fade algebraically, without a proof. This note
proves the weak-coupling side, where the loss is exponential and the proof is
a contraction: change one of a record's three predecessors and its law moves,
in total variation, by at most `1/(2√3)` times `β` times the size of the
change. Coupling two runs from different initial planes site by site, the
expected distance between corresponding records shrinks by the factor `√3β`
at every level. Below `β = 1/√3` this makes every initial plane forgotten
exponentially fast, leaves exactly one invariant law, invariant under all
rotations, and bounds the aligned plane's magnetization by `(√3β)^t`. The
constant comes from a sign lemma about the sphere kernel — its variance along
the axis never exceeds its variance across it — which is a one-line series
comparison once written as `A(κ)/κ` decreasing. The route cannot reach past
`β = 1` (the kernel's mean alone moves by a third of the change), and its
total-variation version would stop at `2/3`; block 26's runs say the memory
is lost at every coupling, so `1/√3` is a route constant, not a threshold.

This completes the campaign's four-way table of explicit weak-coupling
uniqueness regions: six-axis static (block 03), six-axis formation (block 08,
`3c < 1`), sphere static (block 21, `β < √3/6`), sphere formation (here,
`β < 1/√3`). In plain words: when the rule's preference for agreement is
weak, every arrangement of records loses its memory of where it started,
whichever menu and whichever reading; the two readings differ only in how
much preference it takes to keep a memory, and — for the sphere — in whether
any amount does (block 19 against block 26).

Exactly: the sensitivity bounds (T1); the contraction, uniqueness and
the exponential approach to the one law (T2); `m_t ≤ (√3β)^t` and the one-site rate `A(3β)^t`
(T3); the reach of the route (T4). Executed with exact arithmetic: 16 checks,
10 mutations; the total-variation bound against quadrature and the
magnetization against its bound in the control and refuter specs.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the campaign's table of explicit uniqueness regions across readings and menus (blocks 03, 08, 21); the weak-coupling side of the sphere formation law after block 26's strong-coupling runs"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the fourth cell of the table filled: the sphere formation law is ergodic with an explicit rate for beta < 1/sqrt3. Open: the band between 1/sqrt3 and the executed loss of memory at every coupling (block 26); a proof at strong coupling. Consumers: the campaign's decision record; #8093's assembly"
conditional_surface_status: "T1-T4 proved for every beta > 0 (T2-T3 with content for beta < 1/sqrt3) under the records-only reading, positivity of the overlap weight, the sphere menu and the monotone level order as supplied conditions; two standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule's product form and its one-site conditional given a recorded set; the unsoldered menu, the monotone level order and its level reading are declared below (blocks 05, 08, 18, 21, 26 — open PRs #8003, #8138, #8152, #8155, #8170 — are referenced as evidence addresses only). All proposed and unaudited.

Declared objects.
- **The unsoldered menu and rule; level time; the level automaton; the sphere kernel `K_β(·|S)`; `A(κ) = coth κ − 1/κ`; the magnetization `m_t` from the aligned plane** — as declared in block 26 (PR #8170), restated: values are unit vectors `s ∈ S²`; the record at `x` is drawn from `K_β(· | S)`, `S = s_{x−e_1} + s_{x−e_2} + s_{x−e_3}`, independently across a level given the previous one; `K_V(ds) = (|V|/(4π sinh|V|)) e^{V·s} dσ(s)` for `V ∈ R³` (uniform when `V = 0`), so `K_β(·|S) = K_{βS}`; `κ = |V|`, `û = V/|V|`, `w = s·û`; the level automaton is the Markov chain of level configurations on `(S²)^{Z²}`.
- **Distances.** The chordal distance `|s − s'|` on `S²` (diameter `2`); for laws on `S²`, `TV(μ, ν) = (1/2)∫|f_μ − f_ν| dσ` and `W_1(μ, ν) = inf E|s − s'|` over couplings; for laws on the level plane, the per-site distance `D = sup_x E|s_x − s'_x|` under a coupling.
- **The causal coupling.** Given two initial planes, two runs coupled level by level: at each site of the new level, the pair `(s_x, s'_x)` is drawn from a coupling of `K_β(·|S_x)` and `K_β(·|S'_x)` (`S_x, S'_x` the coupled predecessor sums) that attains `E|s_x − s'_x| ≤ W_1(K_β(·|S_x), K_β(·|S'_x)) + η` for a fixed `η > 0` (an optimal coupling exists on the compact sphere; the `η` is dropped at the end), independently across the sites of the level given the previous level.
- **The mean map.** `F(V) = E_{K_V}[s] = A(|V|) û`.

## Prior art and what is new

The contraction of a causal coupling as a uniqueness criterion for probabilistic cellular automata is the Dobrushin-type route that block 08 (PR #8138) carried for the six-axis formation law with total-variation sensitivities (`3c < 1`); the total-variation-to-Wasserstein step and the exponential-family identity `Var(w) = A'(κ)` are standard. What is new: (i) the sensitivity of the exponential-overlap kernel on the sphere to its predecessor sum, `TV ≤ |V − V'|/(2√3)`, through the sign lemma `A(κ)/κ` decreasing (a series comparison) and the directional second moment; (ii) the resulting ergodicity region `β < 1/√3` with the explicit rate `√3β` and the bound `m_t ≤ (√3β)^t`; (iii) the reach of the route (`β = 1` at most, `2/3` for the total-variation version), placed against block 26's executed loss of memory at every coupling; (iv) the fourth cell of the campaign's uniqueness table.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | `TV(K_V, K_{V'}) ≤ |V − V'|/(2√3)`; `W_1 ≤ |V − V'|/√3` | `Var(w) = A'`; the directional moment; the sign lemma; `A/κ ≤ 1/3` | B |
| T2 | `D_{t+1} ≤ √3β D_t`; one rotation-invariant invariant law for `β < 1/√3`; every initial plane forgotten exponentially | the causal coupling; the triangle inequality in `S` | C |
| T3 | `m_t ≤ (√3β)^t`; one site: `A(3β)^t`, `A(3β) ≤ β` | the antipodal comparison | C |
| T4 | the reach: `W_1 ≥ |F(V) − F(V')|`, `A(δ)/δ ≥ 1/3 − δ²/45` | the dual lower bound with a linear test function | D |

## Theorem T1 — the sensitivity of the sphere kernel

**Statement.** For `V, V' ∈ R³`, with `κ = |V|`, `û = V/|V|`, `A = A(κ)`:
(a) `Var_{K_V}(w) = A'(κ) = 1/κ² − 1/sinh² κ`;
(b) for a unit vector `d` with `û·d = c`, `E_{K_V}[((s − Aû)·d)²] = A/κ + (1 − 3A/κ − A²) c²`;
(c) `1 − 3A/κ − A² ≤ 0` for every `κ > 0`, i.e. `A(κ)/κ` is decreasing; and `A/κ ≤ 1/3`;
(d) `TV(K_V, K_{V'}) ≤ |V − V'|/(2√3)` and `W_1(K_V, K_{V'}) ≤ |V − V'|/√3`.

**Proof.** (a) The law of `w` has density `∝ e^{κw}` on `[−1, 1]`, an exponential family in `κ` with log-normalizer `log(2 sinh κ/κ)`, whose first and second derivatives are the mean `A(κ)` and the variance; `A' = 1/κ² − 1/sinh² κ` (B1, symbolically). (b) By block 26's T1(a), `E[s] = Aû` and `E[ssᵀ] = (A/κ)I + (1 − 3A/κ)ûûᵀ`; expand `E[((s − Aû)·d)²] = dᵀE[ssᵀ]d − 2A c (Aû·d) + A²c² = A/κ + (1 − 3A/κ)c² − A²c²` (B2). (c) `1 − 3A/κ − A² ≤ 0 ⇔ κ(1 − A²) ≤ 3A`; since `1 − A²` and `A` are what they are, use instead the equivalent form through (a): the claim is `κ A'(κ) ≤ A(κ)` (indeed `κA' = 1/κ − κ/sinh² κ` and `A = coth κ − 1/κ`, and `1 − 3A/κ − A² = (κA' − A)/κ` because `A² = coth² κ − 2coth κ/κ + 1/κ² = 1 + 1/sinh² κ − 2coth κ/κ + 1/κ²`, so `1 − 3A/κ − A² = −1/sinh² κ − 1/κ² + 2coth κ/κ − 3coth κ/κ + 3/κ² = 2/κ² − 1/sinh² κ − coth κ/κ`, and `(κA' − A)/κ = (1/κ − κ/sinh² κ − coth κ + 1/κ)/κ = 2/κ² − 1/sinh² κ − coth κ/κ`). Multiplying `κA' ≤ A` by `κ sinh² κ`: `sinh² κ − κ² ≤ κ sinh κ cosh κ − sinh² κ`, i.e. `2 sinh² κ ≤ (κ/2) sinh 2κ + κ²`. Both sides are power series with `2 sinh² κ = cosh 2κ − 1 = Σ_{m≥1} (2κ)^{2m}/(2m)!` and `(κ/2) sinh 2κ = Σ_{m≥1} (2κ)^{2m} (m/2)/(2m)!`; the difference is `κ² − κ² + Σ_{m≥2} (2^{2m}/(2m)!)(m/2 − 1) κ^{2m} ≥ 0` (B3: the coefficients `0, 0, 2/45, 2/315, …`). Finally `A/κ ≤ 1/3` is block 26's bound `A(κ) < κ/3` (`A' ≤ 1/(3 + κ²)`), re-checked (B4). (d) `f_V(s) = (κ/(4π sinh κ)) e^{V·s}` is smooth in `V` including `V = 0`, with `∂_V log f_V = s − A(κ)û` (as `∂_V log(κ/sinh κ) = (1/κ − coth κ) û = −Aû`). With `δ = V' − V` and `V_t = V + tδ`, `f_{V'} − f_V = ∫_0^1 f_{V_t} (s − A_t û_t)·δ dt`, so `TV(K_V, K_{V'}) ≤ (1/2) ∫_0^1 E_{K_{V_t}}|(s − A_t û_t)·δ| dt ≤ (|δ|/2) sup_t (E[((s − A_t û_t)·δ̂)²])^{1/2} ≤ (|δ|/2) sup_t (A_t/κ_t)^{1/2} ≤ |δ|/(2√3)`, using (b) with (c) (the coefficient of `c²` is non-positive, so the maximum over the angle is at `c = 0`) and `A/κ ≤ 1/3`. Since the chordal distance is at most `2`, the coupling that agrees off the total-variation part gives `W_1 ≤ 2·TV ≤ |δ|/√3`. ∎ (B1–B4.)

*Reading.* The number `1/√3` is the square root of the transverse variance per component of the uniform law; the bound is tight in the direction of the argument only at `V = 0`, where the exact sensitivity is `1/4` (the uniform law's mean absolute cosine is `1/2`).

## Theorem T2 — the causal coupling contracts

**Statement.** Under the causal coupling, `D_{t+1} ≤ √3β D_t` (with `η → 0`). Hence for `β < 1/√3`: the level automaton has exactly one invariant law `μ_β`; `μ_β` is invariant under every rotation of `S²`; and for every initial plane the law of level `t` is within `2(√3β)^t` of `μ_β` in the per-site distance, so the magnetization from any initial plane tends to `0` exponentially.

**Proof.** At a site `x` of level `t + 1`, `E[|s_x − s'_x| | level t] ≤ W_1(K_{βS_x}, K_{βS'_x}) + η ≤ (β/√3)|S_x − S'_x| + η ≤ (β/√3) Σ_j |s_{x−e_j} − s'_{x−e_j}| + η` (T1d and the triangle inequality); take expectations and the supremum over `x`: `D_{t+1} ≤ √3β D_t + η`, and `η` is arbitrary. With `D_0 ≤ 2` this gives `D_t ≤ 2(√3β)^t`. *Uniqueness.* Let `μ, μ'` be invariant laws; couple them as initial planes (any coupling) and run the causal coupling: the level-`t` laws are `μ` and `μ'` again, and for every finite set `Λ` of sites the Wasserstein distance of the `Λ`-marginals for the metric `Σ_{x∈Λ}|s_x − s'_x|` is at most `2|Λ|(√3β)^t → 0`; so the marginals coincide, and `μ = μ'`. *Rotation invariance.* The kernel commutes with the simultaneous rotation of all records (`K_β(R·|RS) = K_β(·|S)` pushed forward), so `μ_β ∘ R^{−1}` is invariant, hence equals `μ_β`. *The approach.* Couple the given initial plane with a `μ_β`-distributed plane; the level-`t` law of the second run is `μ_β`. ∎ (C1: the factor `√3β` and its position relative to `1` at `β = 5773/10⁴` and `5774/10⁴`, exact enclosures.)

## Theorem T3 — exponential loss of memory

**Statement.** For `β < 1/√3`, from the aligned plane `e`, `m_t ≤ (√3β)^t`. On the one-site periodic plane, from `e`, `m_t = A(3β)^t` exactly, and `A(3β) ≤ β`.

**Proof.** Run the causal coupling from the planes `e` and `−e` (`D_0 = 2`). By covariance under the rotation by `π` about an axis orthogonal to `e`, the second run's magnetization along `e` is `−m_t`. So `2m_t = |E[s_x·e] − E[s'_x·e]| ≤ E|s_x − s'_x| ≤ 2(√3β)^t`. The one-site rate is block 26's T4 (`E[s_{t+1}·e | s_t] = A(3β)(s_t·e)`), and `A(3β) ≤ β` is `A(κ) < κ/3`. ∎ (C2: `A(3β) < β` at rational `β` by exact enclosure.)

*Reading.* At `β = 0.3, 0.5` the simulated magnetization on a `256 × 256` plane falls below `10^{−2}` within `4` and `7` levels, close to `β^t` and well inside `(√3β)^t` (control, refuter).

## Theorem T4 — the reach of the route

**Statement.** For all `V, V'`, `W_1(K_V, K_{V'}) ≥ |F(V) − F(V')|`; and `A(δ)/δ ≥ 1/3 − δ²/45` for `δ > 0`, with `A(δ)/δ < 1/3`. Hence the Wasserstein sensitivity of the kernel to its predecessor sum is at least `(β/3)(1 − 3β²·(something bounded))` at small `|S − S'|`, so a contraction `3c < 1` of the causal coupling with `c` the per-predecessor Wasserstein sensitivity is impossible for `β ≥ 1`.

**Proof.** For any coupling and any unit `d`, `|(E s − E s')·d| ≤ E|s − s'|`; take `d` along `F(V) − F(V')` and the infimum over couplings. With `V = 0` and `V' = δ d`: `|F(V') − F(V)| = A(δ)`, and `A(δ) = δ/3 − δ³/45 + 2δ⁵/945 − …` is an alternating series with decreasing terms for small `δ`; the runner checks the series and the bounds `1/3 − δ²/45 ≤ A(δ)/δ < 1/3` at rational points (D1). For the last sentence: changing one predecessor by `s_1 − s'_1` changes `V = βS` by `β(s_1 − s'_1)`, so `c ≥ (β/3)(1 − β²|s_1 − s'_1|²/15)`, which exceeds `1/3` for `β > 1` and small changes. ∎

*Reading.* The total-variation version of the route stops at `β = 2/3` (the sensitivity `TV/|V − V'|` is `1/4` at small `|V|` and, by quadrature, never larger — executed, not proved); the proved `1/(2√3)` sits between `1/4` and the crude `1/2`. Block 26's runs lose the memory at every `β` tried; the region here is what the coupling proves, not where memory ends.

## No-Go Discipline Gate

This note's sentence is positive (uniqueness with a rate); its escapes are named for the route by which it could fail.

### N1 — Routes by which T2 could fail
1. *The sensitivity constant.* T1 is proved; executed against quadrature (`0.2499 ≤ 0.2887` per unit over `300` random pairs).
2. *The coupling's independence structure.* The sites of a level are coupled independently given the previous level, as the automaton draws them; the per-site bound uses only the predecessors' distances (T2's first line).
3. *Uniqueness from per-site approach.* Finite-dimensional marginals determine the law on the product space; the sum metric on `Λ` is a Wasserstein metric for the product topology (T2).
4. *The region.* `1/√3` is the route's; T4 bounds what any coupling of this kind can give (`β < 1`).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, the sphere menu and the level order as declared (restated from block 26, an open PR, evidence address).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| block 26 (PR #8170) | the declared objects; `A(κ) < κ/3`; the one-site rate | restated / re-checked at scope (B4, C2) |
| blocks 03, 08, 21 (open PRs) | the other three cells of the uniqueness table | placement only (evidence addresses) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the sphere formation law is ergodic below `1/√3`" | executed: `Var(w) = A'`; the directional moment; the sign lemma's series coefficients; the log-derivative | executed: `A(3β) < β` and the one-site rate; the reach series | executed: the total-variation bound against quadrature (control); the coupled contraction (refuter) | executed: the contraction factor and its position relative to `1` at the boundary by exact enclosure | T1–T4 proved for every `β > 0`; the region `β < 1/√3` is the route's |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling, menu or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "Block 08's argument with a different kernel; the constant is arbitrary." Reply: the kernel's sensitivity is the whole content and it needed the sign lemma, which is new; the constant is placed between the exact small-`|V|` value and the route's ceiling, both stated; the cell it fills was empty. Conceded: `1/√3` is not a threshold, and the interesting regime (block 26's) is untouched by this route.

### N8 — Cross-cycle echo
Block 21's `√3/6` for the static sphere law and this note's `1/√3` for the formation law are both route constants of the same coupling family; block 26's T4 (`A(3β)^t` on one site) is the `L = 1` instance of T3; block 08's `3c < 1` is the discrete counterpart.

## Falsifiers
- `Var(w) ≠ A'(κ)`, a directional second moment differing from `A/κ + (1 − 3A/κ − A²)c²`, a negative series coefficient in `(κ/2) sinh 2κ + κ² − 2 sinh² κ`, `A(κ) ≥ κ/3` at some `κ`, or `∂_V log f_V ≠ s − Aû` (B1–B4).
- A contraction factor other than `√3β`, or `√3β` not crossing `1` between `5773/10⁴` and `5774/10⁴`; `A(3β) ≥ β` at some `β > 0` (C1–C2).
- `A(δ)/δ` outside `[1/3 − δ²/45, 1/3)` at some `δ > 0` (D1).

## Boundaries and non-claims
This note proves, for the unsoldered formation law `K_β(s | s_1, s_2, s_3) ∝ e^{β s·(s_1 + s_2 + s_3)}` in level time, that the kernel's total-variation sensitivity to its predecessor sum is at most `1/(2√3)` per unit, that the causal coupling of two initial planes contracts the per-site chordal distance by `√3β` per level, and hence that for `β < 1/√3` the level automaton has one invariant law, rotation-invariant, reached exponentially fast from every initial plane, with the aligned plane's magnetization at most `(√3β)^t`; the constant `1/√3` is the route's, not a threshold; it does not select a menu, reading, order or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. PRs #8000, #8138, #8155, #8170 (open) referenced as evidence addresses for the other cells of the table and the declared objects.
- Re-proved at scope: the moments of the exponential-overlap law and the bound on `A(κ)` (block 26); the exponential-family variance identity; the causal-coupling contraction (block 08's route for the six-axis law).
- Named standard imports at definition level (never as authority for physics): the existence of an optimal coupling for the Wasserstein distance on a compact space (Kantorovich); the coupling inequality `W_1 ≤ diam · TV`.
- Reference only (named, not used): Dobrushin's uniqueness criterion and its Wasserstein forms for probabilistic cellular automata.

## Review record
Supervisor-run block (owner directive 2026-09-16: keep the campaign running twelve more hours). After block 26 the weak-coupling side of the sphere formation law was the proof-shaped remainder and the fourth empty cell of the campaign's uniqueness table. Exploration: the naive coupling (shared uniforms, rotated frames) has sensitivity of order one because nearly cancelling predecessors make the mean direction unstable; the total-variation route removes the direction from the estimate. The control (`specs/supervisor_control_block27.py`) verified the series coefficients, the identities, the total-variation bound against quadrature (`0.2499` per unit, maximum over `300` random pairs, against `0.2887`) and the magnetization at `β = 0.3, 0.5` against `(√3β)^t`. The lens pass is in `GOAL_block27.md`. Facts settled while executing: the sign lemma is exactly `A(κ)/κ` decreasing and reduces to a series comparison whose `κ²` terms cancel; the total-variation sensitivity is `1/4` at `V = 0` and numerically never larger, so the exact version of the route would reach `2/3`; the mean map's Lipschitz constant `1/3` caps every coupling argument at `β = 1`. The refuting pass (`CHECKER_block27_findings.md`) coupled two runs from antipodal planes with the total-variation-maximal coupling per site and measured the contraction of the per-site distance, estimated the sensitivity by Monte Carlo, and checked the one-site rate.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_formation_law_weak_coupling_causal_coupling_contracts_one_invariant_law_2026_09_16.py
python3 scripts/admissibility_rule_unsoldered_formation_law_weak_coupling_causal_coupling_contracts_one_invariant_law_2026_09_16.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_formation_law_weak_coupling_causal_coupling_contracts_one_invariant_law_2026_09_16.py --mutation sign_lemma_wrong
```

Families: A authority and inputs; B the kernel's sensitivity (identities, the sign lemma, the bound); C the contraction, the boundary, the one-site rate; D the reach; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 10 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=16 FAIL=0`.
