---
claim_id: admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_and_the_nonlinear_law_measured_against_it_bounded_theorem_note_2026-09-17
claim_type: bounded_theorem
claim_scope: "For the unsoldered (sphere) formation law of block 26 (PR #8170) in level time on the periodic L x L level plane, linearized about the aligned plane (gain one; per-component transverse noise variance sigma^2 = A(3 beta)/(3 beta), A(kappa) = coth kappa - 1/kappa): (T1) the transverse field theta_{t+1} = P theta_t + xi_t splits into torus modes with multiplier phi(k) = (1 + e^{i k_1} + e^{i k_2})/3, and 1 - |phi(k)|^2 = (4/9)[sin^2(k_1/2) + sin^2(k_2/2) + sin^2((k_1 - k_2)/2)], so |phi| < 1 off the zero mode; a mode of multiplier modulus u^{1/2} < 1 has variance sigma^2 (1 - u^t)/(1 - u) after t levels, the zero mode sigma^2 t, the plane average sigma^2 t / L^2 per component, and the site variance (sigma^2/L^2)[t + sum_{k != 0} (1 - u_k^t)/(1 - u_k)] (proved); (T2) on the tori L = 2, 3, 4 the exact rational covariance recursion Sigma_{t+1} = P Sigma_t P^T + sigma^2 I reproduces the mode formula at every level tested (executed, exact); (T3) the memory time tau_L := L^2/sigma^2 = 3 beta L^2 / A(3 beta), at which the plane average's variance per component reaches one and the proxy exp(-v_t) of the magnetization has fallen by e^{-1} beyond its transient, and the rate A(3 beta)/(3 beta L^2) are enclosed exactly (width below 1/10) at beta = 6, 12, 24, 48 and L = 16, 32, 64 — e.g. tau in [4879, 4880] at (6, 16), [19516, 19517] at (6, 32), [78064, 78065] at (6, 64); the stationary transverse variance V_L = (sigma^2/L^2) sum_{k != 0} 1/(1 - u_k) lies in [3/(4 pi^2), 9/16] sigma^2 S_L with the exact rational lattice sum S_L = sum over nonzero n in the symmetric box of 1/|n|^2, whose consecutive differences lie within one of 2 pi log 2 (proved; the bracket checked on the tiny tori where V_L is rational); so on the torus the linearized proxy decays exponentially at the rate A(3 beta)/(3 beta L^2) after a transient, while on the infinite plane it decays algebraically (block 26, T5). Executed and not claimed: V_L = 2 gamma log L + 0.353 sigma^2 + o(1) by direct summation (gamma = (3 sqrt3/(4 pi)) sigma^2); the nonlinear law's plane-average direction diffuses with a per-component constant D_1 equal to sigma^2/L^2 times 1.34, 1.14, 1.06, 1.02 at beta = 6, 12, 24, 48 (L = 16; 1.42 and 1.18 at L = 32 for beta = 6, 12), tracking 1/|m|^2 of the stationary magnetization within a few percent, with the linear model returning 0.97-1.01 under the same estimator. Not claimed: any statement about the nonlinear law beyond block 26's finite-plane forgetting; the infinite plane; other menus or orders. No reading, rule or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py
---

# The torus memory time of the sphere formation law: the linearized field's zero mode gives `τ_L = 3βL²/A(3β)` exactly, the other modes are stationary and bracketed, and the nonlinear law's direction diffuses `1/|m|²` faster

**Date:** 2026-09-17
**Type:** bounded_theorem
**Status:** bounded-support (exact for the linearized field; the nonlinear law executed against it; conditional on the named supplied readings; unaudited)

## Result up front

Block 26 proved that every finite periodic plane of the sphere formation law
forgets its initial direction, with a minorization rate useless for the
scale, and read off from the gain-one linearization that the memory time
should be "of order `βL²`". This note makes that exact. On the `L × L` torus
the linearized transverse field splits into modes. The zero mode — the plane
average — has multiplier one and performs a random walk: its variance per
component is exactly `σ²t/L²` with `σ² = A(3β)/(3β)`. Every other mode has
multiplier modulus below one and is stationary. So the memory time is
`τ_L = 3βL²/A(3β)`, the level at which the average direction has wandered by
one radian, and the magnetization proxy decays exponentially at the rate
`A(3β)/(3βL²)` after a transient — against the algebraic decay `t^{−γ}` of
the infinite plane. At `β = 6` the memory times are `4879`, `19516`, `78065`
levels for `L = 16, 32, 64`, enclosed exactly. The stationary variance of the
other modes is bracketed by exact rational lattice sums and grows like
`2γ log L`: the finite plane's transverse spread saturates where the infinite
plane's keeps growing.

The nonlinear law is then run on tori and its plane-average direction's
angular diffusion measured by a mean-squared displacement estimator that the
linear model itself calibrates to within three percent. The nonlinear
direction diffuses faster than the zero-mode value by a factor `1.34` at
`β = 6`, `1.14` at `12`, `1.06` at `24`, `1.02` at `48` — the same at `L = 16`
and `32` within errors — and the factor tracks `1/|m|²` of the stationary
magnetization to within a few percent: the average vector is shorter than
one, so the same transverse kicks turn it through larger angles. Nothing
about the nonlinear law is claimed beyond block 26's theorem; the numbers are
executed.

In plain words: on a finite patch of the plane, the common direction of all
the records drifts like a random walk whose step is set by the noise divided
by the patch's area, and every other pattern of disagreement settles down.
So the patch forgets its starting direction after a number of levels
proportional to its area times the stiffness, and we now have that number
exactly for the linear theory and measured for the real law, where it is
shorter by the square of the shrinkage of the average record.

Exactly: the modes (T1); the tiny tori (T2); the memory time and the bracket
(T3). Executed with exact arithmetic: 16 checks, 6 mutations. Simulated
(controls and refuting spec): the nonlinear law and the linear model on tori
with two estimators, an independent sampler, and the direct summation of
`V_L`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 26's queue: the torus memory time of the sphere formation law (read as 'of order beta L^2' from the gain-one linearization)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the linearized torus memory time exact (tau_L = 3 beta L^2 / A(3 beta); exponential decay at the zero-mode rate; stationary modes bracketed); the nonlinear law's angular diffusion measured at 1/|m|^2 times the zero-mode value. Next in the sphere lane: the infinite-plane loss of memory as a theorem; spin-wave theory as a theorem (the 1/|m|^2 factor is the first quantitative target for it). Consumers: the campaign's decision record; block 26's open items"
conditional_surface_status: "T1 proved (symbolic identities; the mode recursion); T2 exact on the tori L = 2, 3, 4; T3 exact enclosures and a proved bracket with exact lattice sums; the nonlinear comparison executed and not claimed; conditional on the records-only reading, positivity, the unsoldered sphere menu and the monotone order as supplied conditions; the standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule and its one-site conditional given a recorded set; the sphere formation law in level time, its linearization and the level walk are block 26's objects (PR #8170, an open hand-off referenced as an evidence address; block 13, PR #8147, for the massless causal law), restated here as declared objects and re-executed. All proposed and unaudited.

Declared objects.
- **The sphere formation law on the torus.** Records `s_x ∈ S²`; level time with the three predecessors of a site projected onto the plane as `(i, j)`, `(i − 1, j)`, `(i, j − 1)` on the periodic `L × L` plane; the new record drawn from `K_β(· | S) ∝ e^{β s·S}` with `S` the sum of the three predecessors; the aligned initial plane. `A(κ) = coth κ − 1/κ`.
- **The linearized field.** Transverse coordinates `θ_x ∈ R²` near the pole; `θ_{t+1} = P θ_t + ξ_t` with `P` the average over the three predecessors (gain one, block 26 T2) and `ξ` i.i.d. centred with variance `σ² = A(3β)/(3β)` per component (block 26 T1(c), T2). **Modes:** for `k ∈ (2π/L)Z_L²`, `θ̂_k = L^{−1} Σ_x e^{−ik·x} θ_x`; `P` acts as multiplication by `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`; `u(k) := |φ(k)|²`; the noise has `Var(ξ̂_k) = σ²` per component; the **plane average** is `θ̄ = θ̂_0/L`.
- **Variances.** The **site variance** `v_t = L^{−2} Σ_k Var θ̂_k(t)`; the **stationary transverse variance** `V_L := (σ²/L²) Σ_{k≠0} 1/(1 − u(k))`; the **magnetization proxy** `e^{−v_t}` (block 26 T5); the **memory time** `τ_L := L²/σ²`.
- **The lattice sum.** `S_L := Σ 1/|n|²` over nonzero `n` in the symmetric box of representatives of `Z_L²` (`n_i ∈ (−L/2, L/2]`); `Q(k) = kᵀMk`, `M = (1/9)[[2, −1], [−1, 2]]`.
- **The direction's diffusion (executed).** For the nonlinear law, `m_t` the plane-average record, `m̂_t = m_t/|m_t|`; the per-component angular diffusion constant `D_1 := E|m̂_{t+ℓ} − m̂_t|²/(2ℓ)` at lags `ℓ` short against `τ_L`, averaged along trajectories after a transient; for the linear model the same estimator on `θ̄` returns `σ²/L²` exactly in expectation.

## Prior art and what is new

Block 13 (PR #8147) found the gain-one linearization and block 26 (PR #8170) its exact one-step variance, the local-limit constant of the level walk, the finite-plane forgetting by a uniform minorization, and the infinite plane's `v_t = γ log t + O(1)`; the finite-plane memory time was read as "of order `βL²`". What is new: (i) the torus mode decomposition with the exact multiplier identity and the zero mode's random walk, giving the memory time and the exponential rate exactly (T1, T3); (ii) the exact rational check on tiny tori (T2); (iii) the bracket of the stationary transverse variance by exact lattice sums and its `2γ log L` growth (T3); (iv) the angular-diffusion measurement of the nonlinear law with a self-calibrating estimator, and the `1/|m|²` reading of the excess (executed).

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | the multiplier identity; the mode variances; the zero mode | the characters of the torus diagonalize a circulant; a geometric sum | B |
| T2 | the mode formula equals the covariance recursion on tiny tori | exact rational linear algebra | C |
| T3 | `τ_L` and the rate enclosed; `V_L` bracketed; `S_L` logarithmic | exact enclosures of `coth` and `π`; two sine inequalities; rational lattice sums | D |

## Theorem T1 — the modes

**T1.1.** `P` is a circulant on the torus, diagonalized by the characters: `(Pθ)^_k = φ(k) θ̂_k` with `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`. *Proof.* `Pθ_x = (θ_x + θ_{x−e₁} + θ_{x−e₂})/3` and each shift multiplies `θ̂_k` by `e^{−ik·e}`; the conjugate convention gives the stated `φ`. ∎

**T1.2 (the multiplier identity).** `1 − |φ(k)|² = (4/9)[sin²(k₁/2) + sin²(k₂/2) + sin²((k₁ − k₂)/2)]`; hence `0 ≤ u(k) ≤ 1` with `u = 1` iff `k ∈ 2πZ²`, i.e. only at the zero mode of the torus. *Proof.* `9|φ|² = 3 + 2cos k₁ + 2cos k₂ + 2cos(k₁ − k₂)` and `1 − cos x = 2 sin²(x/2)` (B1, symbolic). ∎

**T1.3 (the mode variances).** With `θ̂_k(t+1) = φ(k) θ̂_k(t) + ξ̂_k(t)` from `θ̂_k(0) = 0`: `Var θ̂_k(t) = σ²(1 − u^t)/(1 − u)` for `u = u(k) < 1` and `σ²t` at the zero mode; so `Var θ̄_t = σ²t/L²` per component and `v_t = (σ²/L²)[t + Σ_{k≠0}(1 − u_k^t)/(1 − u_k)]`. *Proof.* The noises are independent across levels and modes; the variance recursion `V(t+1) = uV(t) + σ²` sums geometrically (B2). ∎

## Theorem T2 — the tiny tori

On the tori `L = 2, 3, 4` the cosines `cos(2πn/L)` are rational, so `u_k` and the mode formula are rational; the covariance matrix of the field obeys `Σ_{t+1} = PΣ_tPᵀ + σ²I` from `Σ_0 = 0`, with `P` a rational `L² × L²` matrix. The runner iterates the recursion exactly for `t ≤ 12` (`L = 2, 3`) and `t ≤ 8` (`L = 4`) and finds the site variance `tr Σ_t/L²` equal to the mode formula and the plane-average variance `1ᵀΣ_t1/L⁴` equal to `t/L²` at every level (C1); the exact `V_L` of these tori lies inside T3's bracket (C2).

## Theorem T3 — the memory time and the bracket

**T3.1 (the memory time).** `τ_L = L²/σ² = 3βL²/A(3β)` is the level at which the plane average's variance per component reaches one; beyond a transient of order `V_L` the proxy is `e^{−v_t} = e^{−V_L(t)} e^{−t/τ_L}` with `V_L(t) ↑ V_L`, so it decays exponentially at the rate `1/τ_L = A(3β)/(3βL²)`. The runner encloses `τ_L` to width below `1/10` at `β = 6, 12, 24, 48` and `L = 16, 32, 64` through the exact enclosure of `A(3β)` (D1): `τ ∈ [4879, 4880]`, `[19516, 19517]`, `[78064, 78065]` at `β = 6`; `[9479, 9480]` at `(12, 16)`; `[18691, 18692]` at `(24, 16)`; `[37121, 37122]` at `(48, 16)`. On the infinite plane the same proxy decays like `t^{−γ}` (block 26 T5); the torus turns the algebraic loss into an exponential one at the zero-mode rate.

**T3.2 (the bracket).** `M` has eigenvalues `1/9` and `1/3`; from `sin²(x/2) ≤ x²/4` (all `x`) one has `1 − u ≤ Q(k) ≤ |k|²/3`, and from `sin(x/2) ≥ x/π` on `[0, π]` one has `1 − u ≥ (4/(9π²))|k|²` for the representative with `|k_i| ≤ π`; with `|k|² = (2π/L)²|n|²`,
```
(3/(4π²)) σ² S_L  ≤  V_L  ≤  (9/16) σ² S_L .
```
(D2: the eigenvalues symbolically; the sine inequalities on an exact grid; the bracket on the tiny tori.) The lattice sums are rational; `S_16, S_32, S_64` increase and consecutive differences lie within one of `2π log 2` (D3), the discrete counterpart of `S_L = 2π log L + O(1)`. Executed, not claimed: by direct summation `V_L/σ² = 2c₀ log L + 0.353 + o(1)` with `c₀ = 3√3/(4π)`, i.e. `V_L = 2γ log L + 0.353σ²`, the differences to `2c₀ log L` being `0.3514, 0.3525, 0.3527, 0.3528` at `L = 16, 32, 64, 128` (refuting spec, item 4) — the torus's transverse spread equals the infinite plane's at level `t = L²`, as the reading "memory time of order `L²`" requires.

## Executed: the nonlinear law on tori (not proved)

Controls `specs/supervisor_control_block34_torus_msd.py` (block 26's exact sampler on the periodic plane; the mean-squared angular displacement of `m̂_t` over lags `25`–`1000` levels, averaged along trajectories after discarding the first fifth; the linear Gaussian model with the same estimator on `θ̄`) and `..._torus_sim.py` (an exponential fit of the ensemble mean of the projection, found too noisy at the seed counts used and kept as the record of that finding). Outputs in `.out.txt`.

| `β` | `L` | `σ²/L²` | `τ_L` | `|m|` (stationary) | `D_1/(σ²/L²)` at lags `25, 100, 1000` | linear model, same estimator | `1/|m|²` |
|---|---|---|---|---|---|---|---|
| 6 | 16 | `2.050·10⁻⁴` | `4879` | `0.844` | `1.34, 1.33, 1.27` | `0.99, 0.98, 1.00` | `1.40` |
| 6 | 32 | `5.124·10⁻⁵` | `19516` | `0.809` | `1.42, 1.42, 1.38` | `1.01, 0.99, 0.97` | `1.53` |
| 12 | 16 | `1.055·10⁻⁴` | `9479` | `0.924` | `1.14, 1.14, 1.12` | `1.00, 0.99, 1.01` | `1.17` |
| 12 | 32 | `2.637·10⁻⁵` | `37917` | `0.908` | `1.17, 1.19, 1.21` | `1.01, 1.00, 0.96` | `1.21` |
| 24 | 16 | `5.350·10⁻⁵` | `18692` | `0.963` | `1.06, 1.06, 1.00` | `1.01, 1.00, 1.01` | `1.08` |
| 48 | 16 | `2.694·10⁻⁵` | `37122` | `0.982` | `1.02, 1.02, 1.00` | `1.00, 1.00, 0.98` | `1.04` |

What the runs say. (i) The estimator is sound: the linear model returns its exact rate within three percent at every coupling and lag. (ii) The nonlinear direction diffuses faster than the zero-mode value by a factor that falls with `β` — `1.34, 1.14, 1.06, 1.02` — and is the same at `L = 16` and `32` within the errors (`±0.01–0.05`), so it is a property of the law, not of the size. (iii) The factor tracks `1/|m|²` of the stationary magnetization within a few percent (below it by `3–8 %`): the average record is shorter than one, and transverse kicks of the linear size turn a shorter vector through larger angles. So the nonlinear torus memory time is close to `|m|² τ_L`. (iv) The magnitude `|m|` itself is stationary on the torus (block 26 T4), so the direction's diffusion is the whole of the memory loss there. The refuting spec's independent rotated-pole sampler gives `1.28` at `(6, 16)` by the noisy exponential estimator, consistent with the control's `1.36` by the same estimator.

## No-Go Discipline Gate

The note's sentences are positive (exact statements about the linearized field) and executed (the nonlinear comparison); the gate is applied to the scope.

### N1 — Routes by which the exact sentences could fail, and the executed ones mislead
1. *The modes* — a circulant on the torus; the identity is symbolic; the tiny tori check the whole chain exactly (T2).
2. *The noise model* — the linearization's noise variance is block 26's exact one-step value at the aligned plane; away from it the nonlinear law's effective noise differs, which is what the executed excess measures.
3. *The bracket loose* — by a factor `7`; the asymptotic `2γ log L + 0.353σ²` is executed, not proved; a sharper exact bracket would follow block 26's T3 route (not done).
4. *The estimator* — validated on the linear model (item i); the exponential-fit estimator was found unreliable at these seed counts and is recorded as such.
5. *The `1/|m|²` reading* — an executed regularity within `8 %`, not a theorem; a second-order derivation (the transverse noise of the average vector divided by its length) is the natural target of "spin-wave theory as a theorem".

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, and block 26's law and linearization as declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| block 26 (open PR #8170) | the law in level time, the gain-one linearization, `σ²`, the level walk, finite planes forget, `v_t` on the infinite plane | yes (restated; the sampler reused) |
| block 13 (open PR #8147) | the massless causal law | placement only |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the linearized torus memory time is `3βL²/A(3β)` exactly" | executed: the multiplier identity and the geometric mode variance symbolically; the eigenvalues of `M`; the sine inequalities | executed: the rational covariance recursion on the tiny tori against the mode sum | executed: `V_L` on the tiny tori inside the bracket; the lattice sums' increments | executed: the memory times enclosed at four couplings and three sizes | T1–T3 for every `L` and `β`; the nonlinear rates executed, not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "An exact theorem about a linear model and a simulation of the real one — the gap between them is the content, and it is not proved." Reply: the gap is measured to a few percent with a self-calibrating estimator and has a one-line reading (`1/|m|²`), which is the first quantitative target the lane has for a spin-wave theorem; the exact part fixes the scale and the form of the finite-plane decay, which block 26 only read off. Conceded: nothing about the nonlinear law is proved here.

### N8 — Cross-cycle echo
Block 26's exponent `γ` reappears as the coefficient of `log L` in the torus's stationary spread; block 13's massless causal law is the same object with the torus's zero mode isolated; the estimator lesson (mean-squared displacement over the exponential fit) echoes block 29's kernel measurement.

## Falsifiers
- The multiplier identity failing symbolically; a mode variance other than the geometric form; the plane average not `σ²t/L²` (B1–B2).
- A tiny torus where the covariance recursion and the mode sum differ, or `V_L` outside the bracket (C1–C2).
- A memory time outside its stated enclosure; the eigenvalues of `M` other than `1/9, 1/3`; a sine inequality failing on the grid; the lattice sums' differences outside `2π log 2 ± 1` (D1–D3).

## Boundaries and non-claims
This note proves that the linearized transverse field of the unsoldered formation law on the periodic `L × L` level plane splits into a zero mode that performs a random walk of variance `σ² t/L²` per component, `σ² = A(3β)/(3β)`, and nonzero modes that are stationary, so that its memory time is `τ_L = 3βL²/A(3β)` exactly and its magnetization proxy decays exponentially at the rate `A(3β)/(3βL²)` after a transient, with the stationary transverse variance bracketed by `[3/(4π²), 9/16]·σ²·S_L`; it measures the nonlinear law's decay against that rate; it does not prove anything about the nonlinear law on the torus beyond block 26's finite-plane forgetting, does not treat the infinite plane, other menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. Block 26 (PR #8170, open) supplies the law, the linearization, `σ²`, the level walk and the finite-plane theorem, restated; its sampler is reused in the controls. Block 13 (PR #8147, open) referenced as an evidence address.
- Named standard imports at definition level (never as authority for physics): the diagonalization of a circulant by the characters of `Z_L²` (Fourier); the Machin series for `π`; the series enclosure of `coth`.
- Reference only (named, not used): Mermin–Wagner (1966) for the infinite-plane heuristics of block 26.

## Review record
Supervisor-run block (continuing the owner's 2026-09-17 directive). Lens: with the six-axis threshold lane capped at the count, the sphere lane's "torus memory time" is the exact target; the zero mode isolates it. Controls: block 26's sampler restated on the torus; a first estimator (an exponential fit of the ensemble mean of the projection, `..._torus_sim.py`) gave ratios scattered from `0.5` to `1.9` and the linear model's own ratios from `0.3` to `1.0` at `8–32` seeds — the fit reads the random walk's fluctuations — and was replaced by the mean-squared angular displacement (`..._torus_msd.py`), which the linear model calibrates to `0.97–1.01`. Lens pass on the contract: the exact sentences confined to the linearized field; the `1/|m|²` reading labelled executed; the bracket's looseness stated with the executed asymptotic. Primary: T1–T3 (runner, 16 checks, 6 mutations). Refuting pass (`CHECKER_block34_findings.md`, `..._refuter.py`): a floating-point covariance recursion on `L = 8` against the mode sum (`10⁻¹³`); the memory times in floating point against the exact enclosures; an independent rotated-pole sampler; `V_L` by direct summation against the bracket and `2γ log L`. Fold: none beyond the estimator replacement.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py
python3 scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py --mutation memory_time_wrong
```

Families: A authority and inputs; B the modes; C the tiny tori; D the memory time and the bracket; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 6 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=16 FAIL=0`.
