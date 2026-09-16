---
claim_id: admissibility_rule_unsoldered_formation_law_in_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_and_the_simulated_algebraic_decay_of_the_initial_plane_memory_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For the unsoldered (sphere) formation law of the covariant rule with overlap weight e^{beta s.s'} on Z^3 in level order — the record at x drawn from K_beta(s | s_{x-e_1}, s_{x-e_2}, s_{x-e_3}) proportional to e^{beta s.S}, S the sum of the three recorded predecessors, read as the synchronous level automaton on Z^2: (T1) K_beta(.|S) is the exponential-overlap law with concentration kappa = beta |S| about S/|S|; E[s|S] = A(kappa) S/|S| and E[s s^T|S] = (A/kappa) I + (1 - 3A/kappa) u u^T with A(kappa) = coth kappa - 1/kappa, and A(kappa) < kappa/3; from the aligned plane the one-step magnetization is A(3 beta) and the one-step transverse second moment 2A(3 beta)/(3 beta) (proved; symbolic and exact enclosures); (T2) the linearized transverse mean is the average of the three predecessors' transverse coordinates — gain one, forced by rotation covariance — with exact one-step variance A(3 beta)/(3 beta) per component (proved; block 13's second-order statement re-proved at scope); (T3) the return sums P_k = sum_y p_k(y)^2 of the three-predecessor level walk obey 3 sqrt3/(4 pi k) - 1/k^2 - (5/(2k)) e^{-k/4} <= P_k <= 3 sqrt3/(4 pi k) + 27/k^2 + e^{-sqrt(k)/7}, so k P_k tends to 3 sqrt3/(4 pi), and sum_{k<=t} P_k >= (3 sqrt3/(4 pi)) H_t - 1/4 for every t (proved; the sums exact for k <= 150, the constants enclosed rationally); (T4) on every periodic L x L level plane the automaton has a unique invariant law, invariant under all rotations, so the magnetization from any initial plane tends to zero, and on the one-site plane m_t = A(3 beta)^t exactly (proved); (T5) the linearized transverse field from the aligned plane has variance v_t = (A(3 beta)/(3 beta)) sum_{k<t} P_k per component, growing like gamma(beta) log t with gamma(beta) = (3 sqrt3/(4 pi)) A(3 beta)/(3 beta), and has no stationary law with finite variance (proved). Executed and not proved (frontier discovery): the nonlinear law simulated on periodic planes up to 512 x 512 for 20000 levels at beta = 3, 6, 12, 24 loses the magnetization of its initial plane with no plateau, at local exponents above gamma(beta) that approach it as beta grows, while the six-axis formation law at the weights (e^beta, e^-beta, 1) keeps its plane at the same beta; the infinite-plane statement is a conjecture named as such. No menu, reading, order or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_2026_09_16.py
---

# The unsoldered formation law in level time: gain-one spin waves with the local-limit constant, finite planes forget, and the simulated algebraic decay of the initial plane's memory

**Date:** 2026-09-16
**Type:** bounded_theorem (T1–T5); frontier discovery for the executed nonlinear decay
**Status:** bounded-support (exact; conditional on the named supplied readings; the infinite-plane decay simulated, not proved; unaudited)

## Result up front

The campaign now knows both sides of the six-axis menu — the static reading
orders at strong coupling (block 17) and so does the formation reading (block
25) — and one side of the sphere menu: the static sphere law orders on `Z³`
for `β > 76/100` (blocks 19, 22). The formation side of the sphere menu was
unworked. Block 13 linearized it and found gain one: a new record's transverse
coordinate is the plain average of its three predecessors' plus a noise of
variance `1/(3β)`, and a plain average on a two-dimensional level plane never
settles — the variance grows like the logarithm of the level. Block 13 left
"whether an aligned region exists at all" open.

This note proves the exact one-step identities of the nonlinear kernel, the
local-limit constant `3√3/(4π)` of the level walk with explicit error bounds
(block 13 had only two-sided bounds a factor thirty apart), that every finite
periodic plane forgets its initial plane, and the exact exponent
`γ(β) = (3√3/(4π))·A(3β)/(3β)` of the linearized field. Then it does what the
theorems cannot: it runs the nonlinear law. Started from a plane of identical
records, the sphere formation law loses its magnetization at every coupling
tried (`β = 3, 6, 12, 24`), with no plateau over twenty thousand levels on
planes of half a million sites, at rates above the spin-wave value and
approaching it as `β` grows; the six-axis formation law with the same overlap
weight restricted to the axes (`p, q, r = e^{β}, e^{−β}, 1`) keeps its plane
at the same `β`. In plain words: with a continuum of directions to choose
from, records laid down one after another drift slowly away from the direction
they started with, and the drift never stops; with six directions only, they
hold. The static reading of the sphere menu holds too (block 19). So the
reading decides memory for the continuous menu, and the menu decides whether
the formation reading keeps it. The infinite-plane statement for the sphere
formation law is a conjecture supported by the simulations and by the exact
linear theory; it is not proved here.

Exactly: the kernel's moments and `A(κ) < κ/3` (T1); gain one and the
one-step variance `A(3β)/(3β)` (T2); the two-sided bounds on `P_k` with the
constant `3√3/(4π)` and `Σ_{k≤t} P_k ≥ (3√3/(4π))H_t − 1/4` (T3); the unique
rotation-invariant law of every finite plane and `m_t = A(3β)^t` on one site
(T4); `v_t = (A(3β)/(3β)) Σ_{k<t} P_k` and the exponent `γ(β)` (T5). Executed
with exact arithmetic: 20 checks, 14 mutations. Simulated (control and refuting
specs, not the runner): the nonlinear decay, the six-axis side-by-side, the
linear model against its exact variance, finite-size series, an independent
sampler.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 13's open item (PR #8147): whether an aligned region of the sphere formation law exists at all; the campaign's record-dynamics row for the continuous menu"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem_plus_decisive_artifact
next_trace_action: "T1-T5 exact; the nonlinear decay of the sphere formation law's magnetization is executed at beta = 3, 6, 12, 24 and named as a conjecture for the infinite plane. Open: a proof that the sphere formation law on Z^3 has no invariant law reached from an aligned plane with positive magnetization (the twist argument fails in level time; recorded under N1); the growth of the memory time with the plane size (L^2 in the linear theory) against the six-axis law's. Consumers: the campaign's decision record (memory under the two readings and two menus); #8093's assembly"
conditional_surface_status: "T1-T5 proved for every beta > 0 under the records-only reading, positivity of the overlap weight, the sphere menu and the monotone level order as supplied conditions; the nonlinear infinite-plane decay simulated on periodic planes up to 512 x 512 for 20000 levels (control and refuter outputs in the pack), not proved; three standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule's product form and its one-site conditional given a recorded set; the unsoldered menu, the monotone level order and its level reading are declared below (blocks 05, 08, 12, 13, 18, 19, 25 — open PRs #8003, #8138, #8146, #8147, #8152, #8153, #8168 — are referenced as evidence addresses only). All proposed and unaudited.

Declared objects.
- **The unsoldered menu and rule.** Values are unit vectors `s ∈ S²` (the unsoldered reading of the qubit, block 18's menu); the covariant overlap weight `φ(s, s') = e^{β s·s'}` with `β > 0` (the static law of this weight is blocks 19–23's object). The one-site conditional given a recorded set `A` of neighbours is `K(s | s_A) ∝ Π_{y∈A} φ(s, s_y)` against the uniform surface measure.
- **Space-time and level time.** Sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`; records form level by level, the record at `x` drawn from `K_β(· | s_{x−e_1}, s_{x−e_2}, s_{x−e_3})`, independently across a level given the previous one; level `0` carries a supplied plane. The **level automaton** is the Markov chain of level configurations on `(S²)^{Z²}` after the bijection `x ↦ (x_2, x_3)` of each level; its neighbourhood is `{(0,0), (−1,0), (0,−1)}`. The **plane coordinates** of the three predecessors are the shifts `(0,0)`, `(−1,0)`, `(0,−1)`.
- **The sphere kernel.** For `S ∈ R³`, `K_β(ds | S) = (κ/(4π sinh κ)) e^{κ s·û} dσ(s)` with `κ = β|S|`, `û = S/|S|` (uniform when `S = 0`), `dσ` the surface measure. `A(κ) = coth κ − 1/κ` (the mean cosine to `û`).
- **The magnetization.** From the aligned plane (every level-`0` record equal to `e`), `m_t = E[s_x·e]` at any site `x` of level `t` (the same at every site by translation invariance).
- **The level walk.** The walk on `Z²` with steps `(0,0)`, `(−1,0)`, `(0,−1)`, each with probability `1/3`; `p_k(y)` its `k`-step law; `P_k = Σ_y p_k(y)²`; `u(θ) = |φ(θ)|²` with `φ(θ) = (1 + e^{−iθ_1} + e^{−iθ_2})/3`, so `u = (3 + 2cos θ_1 + 2cos θ_2 + 2cos(θ_1 − θ_2))/9`.
- **The linearized field.** `θ_x = (θ_{x−e_1} + θ_{x−e_2} + θ_{x−e_3})/3 + ξ_x` on levels `t ≥ 1` with `θ ≡ 0` on level `0` and `ξ_x` i.i.d. centred with variance `σ² = A(3β)/(3β)` per component (two components); `v_t` its variance per component at level `t`; `H_t = Σ_{k≤t} 1/k`.
- **The six-axis side-by-side.** The six-axis formation law of block 25 with the overlap weight restricted to the axes: `(p, q, r) = (e^{β}, e^{−β}, 1)`.

## Prior art and what is new

The exponential-overlap law on the sphere is the von Mises–Fisher law and `A(κ)` is the Langevin function; their moments are textbook facts, re-derived here in two lines. The absence of a stationary law for a gain-one average with noise on a two-dimensional lattice is block 13's T2/T5 (PR #8147), whose bounds on the return sums (`1/(36n)` and `9π/(16n)`) are replaced here by the constant `3√3/(4π)` with explicit errors (a local limit theorem for this walk, proved by hand from the integral representation). The impossibility of continuous symmetry breaking in two-dimensional equilibrium systems (Mermin–Wagner; Dobrushin–Shlosman; Pfister) does not apply to the level automaton, which is a non-equilibrium chain: an in-plane twist costs an amount proportional to the number of levels, so the relative-entropy box argument gives nothing (N1). Continuous-symmetry order in non-equilibrium two-dimensional dynamics is possible in general (Toner–Tu on Vicsek-type flocking), which is why the question is not settled by analogy and why it is executed here. None of these is used as authority. What is new: (i) the exact nonlinear identities T1 and the finite-plane theorem T4 for the sphere formation law; (ii) the level walk's local-limit constant with explicit two-sided error bounds and the harmonic lower bound with the computer-assisted constant `1/4` (T3); (iii) the exponent `γ(β)` (T5); (iv) the executed nonlinear decay at four couplings with the six-axis side-by-side at the same weight — the discriminator: under the sphere menu the reading decides memory (static keeps it, block 19; formation loses it, here), under the six-axis menu both readings keep it (blocks 17, 25).

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | the kernel's moments; `A(κ) < κ/3`; one-step magnetization `A(3β)` | two integrals; `sinh²κ ≥ κ² + κ⁴/3` | B |
| T2 | gain one; one-step transverse variance `A(3β)/(3β)` | the second-order expansion; covariance | C |
| T3 | `P_k` between `3√3/(4πk) ∓` explicit errors; `Σ_{k≤t}P_k ≥ (3√3/(4π))H_t − 1/4` | the integral representation; Gaussian integrals; exact sums to `150` | D |
| T4 | finite planes forget; `m_t = A(3β)^t` on one site | a uniform minorization; rotation invariance of the unique law | E |
| T5 | `v_t = σ² Σ_{k<t}P_k`; `γ(β)`; no stationary law with finite variance | the path representation; T3 | E |
| executed | the nonlinear decay; the six-axis side-by-side | simulation (control, refuter) | — (specs) |

## Theorem T1 — the kernel

**Statement.** (a) `K_β(· | S)` has mean `A(κ)û` and second moment `E[s sᵀ | S] = (A(κ)/κ) I + (1 − 3A(κ)/κ) ûûᵀ`, where `κ = β|S|`, `û = S/|S|`; in particular `E[(s·û)²] = 1 − 2A/κ` and the transverse second moment is `E|s − (s·û)û|² = 2A/κ`. (b) `0 < A(κ) < κ/3` for `κ > 0`, and `A'(κ) ≤ 1/(3 + κ²)`. (c) From the aligned plane, `m_1 = A(3β)` and the one-step transverse second moment is `2A(3β)/(3β)`; more generally `m_{t+1} = E[A(β|S|) (S·e)/|S|]` with `S` the sum of the three predecessors at level `t`.

**Proof.** (a) With `w = s·û`, the surface measure gives `∫ e^{κ s·û} dσ = 2π ∫_{−1}^{1} e^{κw} dw = 4π sinh κ/κ`, `E[w] = ∫ w e^{κw} dw / ∫ e^{κw} dw = coth κ − 1/κ` and `E[w²] = 1 − 2A/κ` (integration by parts; B1). The law is invariant under rotations about `û`, so `E[s] = E[w] û` and `E[s sᵀ] = a I + b ûûᵀ` with `a + b = E[w²]` and trace `3a + b = 1`, whence `a = A/κ`, `b = 1 − 3A/κ`. (b) `A'(κ) = 1/κ² − 1/sinh² κ`, and `sinh² κ = Σ_{n≥1} 2^{2n−1}κ^{2n}/(2n)! ≥ κ² + κ⁴/3`, so `A'(κ) ≤ 1/κ² − 1/(κ² + κ⁴/3) = 1/(3 + κ²) < 1/3`; as `A(0⁺) = 0`, `A(κ) = ∫_0^κ A' < κ/3`; positivity from `A' > 0` (`sinh κ > κ`). (c) At the aligned plane `S = 3e`, `κ = 3β`, `û = e`; apply (a). The general identity is the tower property with (a). ∎ (B1–B3: the moments symbolically; the series and the bound; exact rational enclosures of `A(3β)` at `β = 3, 6, 12, 24`: `[8888, 8889]/10⁴`, `[9444, 9445]/10⁴`, `[9722, 9723]/10⁴`, `[9861, 9862]/10⁴`.)

## Theorem T2 — gain one

**Statement.** Write the unit vectors near the pole `e` as `s = (θ, √(1 − |θ|²))` with `θ ∈ R²` and likewise `s_i = (θ_i, ·)` for the three predecessors. Then `β s·(s_1 + s_2 + s_3) = 3β − (β/2) Σ_i |θ − θ_i|² + O(4)`: the quadratic form is minimized at the average `(θ_1 + θ_2 + θ_3)/3` with Hessian `−3β I`. The linearized transverse mean has gain one; the exact one-step transverse variance at the aligned plane is `A(3β)/(3β)` per component.

**Proof.** `s·s_i = θ·θ_i + √(1 − |θ|²)√(1 − |θ_i|²) = 1 − |θ − θ_i|²/2 + O(4)`; sum and multiply by `β`. The gradient of `Σ_i |θ − θ_i|²` vanishes at the average and its Hessian is `6I`. Gain one is forced by covariance: the kernel depends on the predecessors through their sum and is covariant under rotations, so shifting all three transverse coordinates by a common small `δ` shifts the mean by `δ`, and the symmetric linear map with that property is the average. The one-step variance is T1(c): `2A(3β)/(3β)` over two components. ∎ (C1, symbolically in a scaling parameter.)

*Reading.* Block 13 (PR #8147, T5b) obtained the same expansion for a general zonal overlap with variance `1/(3β)` at second order; here the variance is the exact one-step value `A(3β)/(3β)`, which tends to `1/(3β)` as `β → ∞`.

## Theorem T3 — the level walk's constant

**Statement.** For every `k ≥ 1`,
```
3√3/(4πk) − 1/k² − (5/(2k)) e^{−k/4}  ≤  P_k  ≤  3√3/(4πk) + 27/k² + e^{−√k/7};
```
hence `k P_k → 3√3/(4π)`. Moreover `Σ_{k≤t} P_k ≥ (3√3/(4π)) H_t − 1/4` for every `t ≥ 1`, so `Σ_{k≤t} P_k ≥ (3√3/(4π)) log t − 1/4`.

**Proof.** *The representation.* `p_k(y) = (2π)^{−2} ∫_{[−π,π]²} φ(θ)^k e^{−iθ·y} dθ` and, by Parseval, `P_k = (2π)^{−2} ∫ u(θ)^k dθ` with `u = |φ|²`. *The identity.* `1 − u = (4/9)[sin²(θ_1/2) + sin²(θ_2/2) + sin²((θ_1 − θ_2)/2)]` (D3). *Bounds on `1 − u`.* From `x²/4 − x⁴/48 ≤ sin²(x/2) ≤ x²/4` (all real `x`): `Q − W ≤ 1 − u ≤ Q` on `R²`, with `Q(θ) = (1/9)(θ_1² + θ_2² + (θ_1 − θ_2)²) = θᵀMθ`, `M = (1/9)[[2, −1], [−1, 2]]`, `det M = 1/27`, `Q ≥ |θ|²/9`, and `W = (1/108)(θ_1⁴ + θ_2⁴ + (θ_1 − θ_2)⁴) ≤ |θ|⁴/12` (as `(θ_1 − θ_2)⁴ ≤ 8(θ_1⁴ + θ_2⁴)`). On the square, from `sin²(x/2) ≥ x²/π²` for `|x| ≤ π` (dropping the third term): `1 − u ≥ (4/(9π²))|θ|²`. *Upper bound.* Let `ρ = (12/k)^{1/4}` (`ρ < π`). Outside `|θ| ≤ ρ`, `u^k ≤ (1 − 4ρ²/(9π²))^k ≤ e^{−(4√12/(9π²))√k} ≤ e^{−√k/7}`, and the normalized area is at most `1`. Inside, `u ≤ 1 − Q + W ≤ e^{W − Q}` and `kW ≤ kρ⁴/12 = 1`, so `u^k ≤ e^{−kQ} e^{kW} ≤ e^{−kQ}(1 + e·kW)`; therefore `(2π)^{−2} ∫_{|θ|≤ρ} u^k ≤ (2π)^{−2}[∫_{R²} e^{−kQ} + (ek/12) ∫_{R²} e^{−k|θ|²/9} |θ|⁴] = (2π)^{−2}[3√3π/k + (ek/12)(1458π/k³)] ≤ 3√3/(4πk) + 27/k²` (`121.5e/(4π) < 27`; the Gaussian integrals: D3). *Lower bound.* On `{Q ≤ 1/2}` (inside the square, as `|θ| ≤ 3/√2 < π` there), `u ≥ 1 − Q` and `log(1 − Q) ≥ −Q − Q²`, so `u^k ≥ e^{−kQ}(1 − kQ²)`; hence `P_k ≥ (2π)^{−2}[∫_{R²} e^{−kQ} − ∫_{Q>1/2} e^{−kQ} − k ∫_{R²} e^{−kQ} Q²] ≥ (2π)^{−2}[3√3π/k − e^{−k/4}·6√3π/k − k·(3√3π/k)(2/k²)] ≥ 3√3/(4πk) − (5/(2k))e^{−k/4} − 1/k²` (`∫ e^{−kQ}Q² = (3√3π/k)(2/k²)`: D3; `3√3/(2π) < 1`, `6√3/(4π) < 5/2`). *The harmonic bound.* For `t ≤ 150` the exact sums satisfy `Σ_{k≤t} P_k ≥ (3√3/(4π))H_t − 6/25` (D3, exact rationals with `3√3/(4π)` enclosed from above). For `t > 150`, the lower bound gives `Σ_{150<k≤t} P_k ≥ (3√3/(4π))(H_t − H_{150}) − Σ_{k>150}[1/k² + (5/(2k))e^{−k/4}] ≥ (3√3/(4π))(H_t − H_{150}) − 1/100`; adding, `Σ_{k≤t} P_k ≥ (3√3/(4π))H_t − 1/4`. Finally `H_t ≥ log t`. ∎ (D1: the trinomial form of `p_k` by enumeration; D2: the two-sided bounds for `k ≤ 150` with `√3`, `π` and the exponentials enclosed rationally, and `k²|P_k − 3√3/(4πk)| < 1`; D3: the identity, the Gaussian integrals, the harmonic bound.)

*Reading.* The exact sums lie below `3√3/(4πk)` by about `1/(10k²)`; the stated errors are what the elementary argument gives.

## Theorem T4 — finite planes forget

**Statement.** On the periodic `L × L` level plane the level automaton has a unique invariant law `π_L`, invariant under every rotation of `S²`; from any initial plane, `|E[s_x · e] at level t| ≤ 2(1 − δ_L^{L²})^t` with `δ_L = 6β/(e^{6β} − 1)`; in particular the magnetization tends to `0`. On the one-site plane (`L = 1`), from the aligned plane, `m_t = A(3β)^t` exactly.

**Proof.** The density of `K_β(· | S)` against the uniform probability law on the sphere is `(κ/sinh κ) e^{κ s·û} ≥ (κ/sinh κ) e^{−κ} = 2κ/(e^{2κ} − 1)`, a decreasing function of `κ` (E2), and `κ = β|S| ≤ 3β`; so every site's conditional has density at least `δ_L := 6β/(e^{6β} − 1)` (and `1` when `S = 0`). The level kernel is the product over the `L²` sites, so it has density at least `δ_L^{L²}` against the product uniform law: a uniform minorization, which gives a unique invariant law and total-variation distance `≤ (1 − δ_L^{L²})^t` from it after `t` levels. The kernel commutes with the simultaneous rotation of all records (`K_β(Rs | RS) = K_β(s | S)`), so `π_L ∘ R^{−1}` is invariant and equals `π_L`; the vector `E_{π_L}[s_x]` is then fixed by every rotation, hence `0`, and `|E_t[s_x·e]| ≤ 2(1 − δ_L^{L²})^t`. For `L = 1` the chain is `s_{t+1} ∼ K_β(· | 3s_t)`, with `E[s_{t+1}·e | s_t] = A(3β)(s_t·e)` by T1(a) (`κ = 3β`, `û = s_t`); iterate. ∎ (E1: the one-site recursion symbolically; E2: the minorization identities.)

*Reading.* Every finite plane forgets, so the question is the growth of the memory time with `L`: the six-axis formation law's contours make it exponential in `L` in its ordered phase (block 25's route on a torus), while gain-one diffusion makes the linearized sphere field's memory time of order `βL²`. That difference of scale is what the executed nonlinear runs test on planes far larger than the levels run.

## Theorem T5 — the linearized field

**Statement.** From the aligned plane, `v_t = σ² Σ_{k<t} P_k` per component, `σ² = A(3β)/(3β)`; hence, with `γ(β) := (3√3/(4π))·A(3β)/(3β)`,
```
σ² ((3√3/(4π)) H_{t−1} − 1/4)  ≤  v_t  ≤  σ² ((3√3/(4π)) H_{t−1} + 150)      (t ≥ 2),
```
so `v_t = γ(β) log t + O(1)` and `v_t → ∞`; the linearized field has no stationary law with finite variance; and the second-order proxy `e^{−v_t}` of the magnetization decays like `t^{−γ(β)}`. Exactly, `γ(β) ∈ [408, 409]/10⁴` at `β = 3`, `[216, 217]/10⁴` at `6`, `[1116, 1117]/10⁵` at `12`, `[566, 567]/10⁵` at `24`, and `γ(β) → √3/(4πβ)` as `β → ∞`.

**Proof.** Unfolding the recursion, `θ_x = Σ_{k<t} Σ_y p_k(y) ξ_{x − (0, y), t−k}` (the level walk started at `x`'s plane coordinates; T3's `p_k`), a sum of independent centred terms, so `Var = σ² Σ_{k<t} Σ_y p_k(y)² = σ² Σ_{k<t} P_k`. The bounds are T3 with `Σ_{k≥1}(27/k² + e^{−√k/7}) < 150`. A stationary law with finite variance would give, started from it, a variance at level `t` at least `v_t` (the noise terms of levels `1..t` are independent of the initial field), impossible as `v_t → ∞`. The enclosures of `γ` are exact arithmetic (E3). ∎

*Reading.* At second order the sphere formation law is exactly block 13's massless causal law with the sphere's own noise; its magnetization proxy decays algebraically with an exponent that vanishes like `1/β`. The nonlinear law can only be worse at keeping its plane than this proxy suggests if the neglected cubic terms push the field further, and the executed runs say they do.

## Executed: the nonlinear law simulated (frontier discovery, not proved)

Controls `specs/supervisor_control_block26_sphere_sim.py` (the sphere formation law on a periodic `L × L` level plane from the aligned plane; each record drawn exactly from `K_β(· | S)` by inverting the cosine's law and drawing a uniform azimuth), `specs/supervisor_control_block26_sixaxis_sim.py` (block 25's six-axis law at `(e^{β}, e^{−β}, 1)`), and `specs/supervisor_control_block26_fit.py` (the table); refuting spec `specs/supervisor_control_block26_refuter.py` (an independent sampler built by a rotation of a pole sample; the linear model against its exact variance; a finite-size series). Outputs in `.out.txt`. `|m|` is the norm of the plane-averaged record; `exp[a, b]` is the slope of `−log|m|` against `log t` over `[a, b]`.

| `β` | `L` | levels | `m(500)` | `m(5000)` | `m(20000)` | `exp[500, 5000]` | `exp[5000, 20000]` | `exp[500, 20000]` | `γ(β)` | run |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 512 | 20000 | 0.5118 | 0.3863 | 0.2735 | 0.1181 | 0.2629 | 0.1864 | 0.04084 | control |
| 6 | 256 | 20000 | 0.7827 | 0.7322 | 0.6711 | 0.0358 | 0.0399 | 0.0324 | 0.02170 | control |
| 6 | 512 | 20000 | 0.7826 | 0.7349 | 0.6823 | 0.0275 | 0.0498 | 0.0395 | 0.02170 | control |
| 12 | 512 | 20000 | 0.8951 | 0.8715 | 0.8515 | 0.0120 | 0.0154 | 0.0145 | 0.01117 | control |
| 12 | 512 | 20000 | 0.8941 | 0.8673 | 0.8567 | 0.0132 | 0.0076 | 0.0103 | 0.01117 | refuter (independent sampler) |
| 24 | 512 | 20000 | 0.9483 | 0.9367 | 0.9268 | 0.0055 | 0.0071 | 0.0066 | 0.00566 | control |

Six-axis formation law at `(e^{β}, e^{−β}, 1)`, `256 × 256`, `3000` levels (control `..._sixaxis_sim`): mean fraction of dissenting records `5.6·10⁻⁴` at `β = 3`, `2.8·10⁻⁵` at `β = 4`, `0` at `β = 6` — the plane is kept. Small periodic planes at `β = 6` (refuter, the projection on the initial direction): `L = 32` wanders through `0.29` at `t = 4500` and crosses zero by `t ≈ 12500` (the scale `βL² ≈ 6·10³` of T4); `L = 64` and `L = 128` wander between `0.57` and `0.79` without losing the sign within `20000` levels; the large planes above are far from this regime (`βL² ≥ 4·10⁵`).

What the runs say. (i) At every `β` the magnetization decays with no plateau over the whole run, on planes whose linear size squared exceeds the number of levels by more than a factor ten, so the finite-plane forgetting of T4 (memory time of order `L²` or longer) is not what is seen: the two plane sizes at `β = 6` agree. (ii) The local exponent is at or above `γ(β)` at every `β` and grows along the run — strongly at `β = 3` (`0.12` to `0.26`), hardly at `β = 24` (`0.0055` to `0.0071` against `γ = 0.0057`); the ratio to `γ(β)` falls toward one as `β` grows, so the exact linear theory is the large-`β` limit of what the nonlinear law does and the neglected terms only speed the loss of memory up. (iii) The linear model, simulated with the same noise, reproduces its exact variance `σ² Σ_{k<t} P_k` and decays more slowly than the nonlinear law at the same `β`: the neglected cubic terms speed the loss of memory up. (iv) The six-axis formation law at the same overlap weight keeps its plane: the fraction of dissenting records stays at `6·10⁻⁴` (`β = 3`), below `10⁻⁴` (`β = 4`) and at `0` (`β = 6`) over `3000` levels, as block 25 proves for large enough `p`. **Conjecture (not claimed as a theorem):** on the infinite plane the sphere formation law started from an aligned plane has `m_t → 0` for every `β > 0`, at least as fast as `t^{−γ(β)}`.

## No-Go Discipline Gate

The executed sentence is negative for the sphere formation law (it loses its plane) and is not a theorem; its escapes are named.

### N1 — Routes by which the executed conclusion could be wrong, and by which a proof was sought
1. *A plateau beyond the levels run.* The linear theory predicts none (`v_t → ∞`, T5), the local exponents grow rather than shrink along the runs, and no plane size shows saturation; but only `2·10⁴` levels at `β ≤ 24` are executed. The falsifier is stated.
2. *Finite-size forgetting mistaken for infinite-plane decay.* Excluded on the run's scale by T4's `L²` estimate and by the agreement of `L = 256` and `L = 512` at `β = 6`; the finite-size series in the refuter shows the small planes decaying faster, as they must.
3. *The sampler.* Two independent samplers agree; both reproduce `A(κ)` and `1 − 2A/κ` to Monte-Carlo accuracy (refuter).
4. *A proof by a two-dimensional symmetry argument.* Attempted: rotating the whole trajectory by an in-plane twist `φ(x_⊥)` changes each site's conditional through the differences `φ(x_⊥) − φ(x_⊥ − e_j⊥)`, whose relative-entropy cost per site is of order `|∇φ|²` times the local transverse spread, of order one per site per level; over `T` levels the cost is proportional to `T`, so no twist of bounded cost exists and the box argument that closes the equilibrium case gives nothing here. Not a wall; recorded so that the next attempt starts elsewhere (a dynamical argument on the transverse second moment is the natural next route: T1(c) gives the exact one-step recursion `m_{t+1} = E[A(β|S|)(S·e)/|S|]`).
5. *The exponent comparison.* The linear exponent is exact (T5); the nonlinear local exponents are fits over decades with the plane-average noise of a `512 × 512` plane; only their ordering and trend are used.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, the sphere menu and the level order as declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| block 13 (PR #8147) | the gain-one law and its bounds; its open item | sibling (re-proved at scope where used) |
| blocks 18, 19, 22, 25 (open PRs) | the menu; the static sphere order; the six-axis formation order | placement only (evidence addresses) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the sphere formation law loses its plane; the six-axis keeps it" | executed: the kernel's moments and normalizer symbolically; `A(κ) < κ/3` at ten points by enclosure; the expansion and its minimizer | executed: the one-site chain; the minorization; the six-axis deviations at `(e^{β}, e^{−β}, 1)` | executed: the path identity for `k ≤ 6`; `P_k` exactly for `k ≤ 150` against the bounds; the Gaussian integrals | executed: the harmonic bound to `150`; `γ(β)` enclosed at four couplings | T1–T5 proved for every `β > 0`; the nonlinear infinite-plane decay simulated at four couplings, not proved |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling, menu or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "A simulation of twenty thousand levels proves nothing about the infinite plane, and the exact part is a textbook exercise plus a local limit theorem." Reply: the exact part is stated as what it is, and the local-limit constant with explicit errors is more than block 13 had; the simulation is the campaign's first look at the sphere formation law and it answers the question the campaign asked — whether the two readings keep memory the same way — in the only currency available today, with the exact linear theory as the yardstick and the falsifier named. Conceded: the infinite-plane statement is a conjecture; the local exponents drift, so no single number is claimed for the nonlinear decay.

### N8 — Cross-cycle echo
Block 13's gain dichotomy is the linear core; block 19's static order is the counterpart the runs are measured against; block 25's six-axis contours are why the discrete menu holds; block 20's "the menu decides" on planes has its formation-time echo here.

## Falsifiers
- A kernel moment differing from `A(κ)`, `1 − 2A/κ`, a normalizer other than `sinh κ/κ`, or `A(κ) ≥ κ/3` at some `κ > 0` (B1–B3).
- A second-order expansion with a minimizer other than the average, or a one-step variance other than `A(3β)/(3β)` (C1).
- A `p_k` differing from the trinomial form, a `P_k` outside the stated two-sided bounds, a Gaussian integral of the proof with a different value, or `Σ_{k≤t}P_k < (3√3/(4π))H_t − 6/25` at some `t ≤ 150` (D1–D3).
- `m_t ≠ A(3β)^t` on the one-site plane, a density bound below `2κ/(e^{2κ} − 1)`, a `γ(β)` outside the stated enclosures, or a six-axis deviation differing from the closed forms (E1–E4).
- For the discovery claim: a simulated magnetization of the sphere formation law settling at a positive plateau on scales `t ≪ L²` at some `β`.

## Boundaries and non-claims
This note proves, for the unsoldered formation law `K_β(s | s_1, s_2, s_3) ∝ e^{β s·(s_1 + s_2 + s_3)}` in level time, the exact one-step identities of its kernel, the local-limit constant `3√3/(4π)` of the level walk's return sum with explicit error bounds, the loss of the initial plane's memory on every finite periodic plane, and the exponent `γ(β) = (3√3/(4π))·A(3β)/(3β)` of the linearized transverse field; the algebraic decay of the nonlinear law's magnetization on the infinite plane is executed by simulation and is not proved; it does not select a menu, reading, order or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

Further: whether the sphere formation law on the infinite plane has an invariant law with positive magnetization reached from some initial plane is not claimed either way; the nonlinear decay rate is not claimed as a number; the static sphere law is used only as the counterpart (block 19, an open PR, evidence address); other menus, orders and readings are not treated.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. PRs #8003, #8138, #8146, #8147, #8152, #8153, #8156, #8168 (open) referenced as evidence addresses for the monotone class, the formation law on `Z³`, the level-time reading, the gain-one law, the menus, the static sphere order and its threshold, and the six-axis formation order.
- Re-proved at scope: the moments of the exponential-overlap law (von Mises–Fisher) and the bound on the Langevin function `A(κ)`; block 13's gain-one expansion; the local limit constant of the level walk from the integral representation; the minorization argument for the finite plane.
- Named standard imports at definition level (never as authority for physics): Parseval's identity on the torus; the uniform-minorization (Doeblin) bound for Markov chains; the tower property and the strong law used in the simulations' averages.
- Reference only (named, not used): Mermin–Wagner, Dobrushin–Shlosman and Pfister (equilibrium two-dimensional continuous symmetry); Toner–Tu and Vicsek (non-equilibrium flocking order); Toom (the discrete counterpart, block 25).

## Review record
Supervisor-run block (owner directive 2026-09-16: "keep running the campaign for 12 more hours"; the lane's proof-shaped queue exhausted after block 25's sharpening). The lane assessment found the sphere formation law unworked (block 13's open item) and the six-axis comparison free. Exploration: the sphere law at `β = 3, 6, 12` on a `256 × 256` plane lost its magnetization with no plateau over `3000` levels at rates tracking `γ(β)` at large `β`; the six-axis law at the same weight kept its plane. The exact control (`specs/supervisor_control_block26_exact.py`) verified the kernel moments, the bound `A(κ) < κ/3`, the return sums against the two-sided bounds (the exact sums lie below `3√3/(4πk)` by about `1/(10k²)`), the quadrature value of `kP_k` to `10⁴` steps, and the exponents; the lens pass is in `GOAL_block26.md`. Facts settled while executing: the intervals for `γ(β)` at `β = 6` and `12` had to be moved down one unit in the last digit after the exact enclosure (`0.021696`, `0.011167`); the harmonic bound's proved constant is `1/4` through a computer-assisted step (exact sums to `150` plus the tail bound), the elementary tail alone giving only `6`; the twist argument for a proof was tried and fails in level time (N1). The refuting pass (`CHECKER_block26_findings.md`) used an independently coded sampler, the linear model against its exact variance, a finite-size series, `P_k` by a second method, and the sampler's moments by Monte Carlo.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_2026_09_16.py
python3 scripts/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_2026_09_16.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_2026_09_16.py --mutation return_lower_bound_wrong
```

Families: A authority and inputs; B the kernel's moments and the bound; C gain one; D the level walk and its constant; E finite planes, the exponent, the six-axis deviations; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 14 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
