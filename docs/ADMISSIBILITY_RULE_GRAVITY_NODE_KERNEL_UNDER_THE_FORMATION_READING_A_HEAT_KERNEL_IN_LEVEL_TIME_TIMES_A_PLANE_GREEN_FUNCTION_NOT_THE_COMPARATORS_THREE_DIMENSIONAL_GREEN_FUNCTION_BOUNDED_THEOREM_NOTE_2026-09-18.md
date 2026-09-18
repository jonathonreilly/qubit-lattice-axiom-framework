---
claim_id: admissibility_rule_gravity_node_kernel_under_the_formation_reading_a_heat_kernel_in_level_time_times_a_plane_green_function_not_the_comparators_three_dimensional_green_function_bounded_theorem_note_2026-09-18
claim_type: bounded_theorem
claim_scope: "For the unsoldered (sphere) formation law of block 26 (PR #8170) in level time, linearized about the aligned plane (gain one; per-component transverse noise variance sigma^2 = A(3 beta)/(3 beta)), on the periodic L x L level plane: (T1) the space-time covariance of a mode is Cov(theta^_k(t), theta^_k(t+s)) = sigma^2 phi(k)^s (1 - u^t)/(1 - u) with phi(k) = (1 + e^{i k_1} + e^{i k_2})/3 and u = |phi|^2 < 1 off the zero mode, and sigma^2 t at the zero mode, so the stationary kernel on the nonzero modes is C_s = sigma^2 (I - P P*)^{-1} P*^s — the two-dimensional Green function of I - P P* across the level plane times the s-step heat kernel along levels (proved; the cross-level covariances Sigma_{t,t+s} = Sigma_t (P^s)^T verified by exact rational recursions on the tori L = 3, 4 against Re phi(k)^s for every cosine character); (T2) the small-k form 1 - u(k) = k^T M k + O(k^4), M = (1/9)[[2,-1],[-1,2]] with eigenvalues 1/9 along (1,1) and 1/3 along (1,-1), invariant under the group of order six permuting the three predecessor directions {k_1, k_2, k_1 - k_2}, against the comparator's E(k) = sum_i 2(1 - cos k_i) = |k|^2 + O(k^4) on Z^3 with the 48 signed permutations (proved); (T3) for every nonzero mode |C_s(k)|/C_0(k) = |phi(k)|^s <= exp(-2|k|^2 s/(9 pi^2)) on the square, so the kernel is diffusive (in-plane scale |k|^{-1} ~ s^{1/2}) and drifts along the causal cone's axis (phi = 1 + i(k_1 + k_2)/3 + O(k^2)), while the comparator's 1/E(k) is not of the product form (plane factor) x (propagator) in any direction (proved). Executed and not claimed: on a 256 x 256 plane at beta = 6, 12, 24 the nonlinear sphere formation law's equal-level transverse structure factor is the linearized kernel sigma^2/(1 - u(k)) times a normalization 0.83-0.89, 0.90-0.94, 0.94-0.97 (rising with |k| and with beta), and its cross-level correlations reproduce phi(k)^s in modulus and phase up to s = 64 within a few percent. Not claimed: any gravity node's kernel derived under the formation reading (the comparator's kernel of block 19 is located and shown not to be this object; what replaces it is the theorems above); other menus or orders. No reading, rule or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py
---

# The gravity node's kernel under the axiom's reading: a heat kernel in level time times a plane Green function, diffusive and three-fold symmetric, not the comparator's three-dimensional Green function

**Date:** 2026-09-18
**Type:** bounded_theorem
**Status:** bounded-support (exact for the linearized field; the nonlinear law executed against it; conditional on the named supplied readings; unaudited)

## Result up front

The gravity lane's Green-function kernel was located by block 19 in the
transverse channel of the ordered sphere law under the *static* reading — the
frozen comparator, the rule as the full conditional of one joint law on `Z³`.
The axiom says records form. This note asks what that channel is under the
axiom's own reading, in level time, and answers exactly for the linearized
field: the space-time covariance of every nonzero mode of the level plane is
`σ² φ(k)^s/(1 − |φ(k)|²)`, with `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`. As an
operator on the plane, `C_s = σ²(I − PP*)^{−1} P*^s`: the two-dimensional
Green function of `I − PP*` across the plane, times the `s`-step heat kernel
along levels. It is diffusive — correlations `s` levels apart live at in-plane
scales `√s` — it drifts along the axis of the causal cone, its small-wavevector
form `kᵀMk` has the three-fold symmetry of the three predecessor directions
and not the cubic symmetry of the lattice, and its zero mode is not stationary
but random-walks (block 34). The comparator's kernel `1/(βE(k))` is the
inverse of an isotropic three-dimensional operator with no distinguished
direction and no product structure; it is a different object, and it does not
arise under the formation reading.

The nonlinear law is then run on a `256 × 256` plane at `β = 6, 12, 24`. Its
equal-level transverse structure factor is the linearized kernel times a
normalization below one (`0.83–0.89`, `0.90–0.94`, `0.94–0.97`, rising with the
wavevector and with `β`), and its cross-level correlations reproduce the heat
kernel in modulus and phase up to sixty-four levels within a few percent. So
the exact statement is also the right description of the real law at strong
coupling, up to a normalization that tends to one as `β` grows.

In plain words: under the frozen picture, two records far apart in any
direction are correlated like the poles of a magnet, with a long-range
Coulomb-like kernel in three dimensions, and that kernel is where the gravity
lane found its potential. Under the axiom's picture the same records are laid
down level by level: correlations across the plane are long-range in the
two-dimensional way, but correlations across levels spread only by diffusion,
a little further each level, along the direction in which records form. There
is no three-dimensional potential in it. Whatever the gravity node's kernel is
under the axioms, it is not the comparator's, and this note gives what it is
for the linear part of the law.

Exactly: the space-time covariance (T1); the small-wavevector forms and the
symmetries (T2); the scaling and the non-product form of the comparator (T3).
Executed with exact arithmetic: 14 checks, 7 mutations. Simulated (controls
and refuting spec): the nonlinear law's structure factors and cross-level
ratios; a floating-point cross-level recursion on a larger torus.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the decision record's consequence (2026-09-18): the gravity node's Green-function kernel was located in the comparator (block 19) and must be re-derived in the formation reading or given up"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the linearized kernel under the formation reading given exactly (heat kernel times plane Green function; diffusive; three-fold symmetric; zero mode random-walking) and shown not to be the comparator's; the nonlinear law's structure factor measured at 0.83-0.97 of it. Next: what the gravity lane's construction gives when its input is this kernel (a gravity-lane obligation, not this campaign's); spin-wave theory as a theorem (the normalization c(beta)). Consumers: the gravity lane; the campaign's decision record"
conditional_surface_status: "T1-T3 proved for the linearized field (symbolic identities; exact rational cross-level recursions on tiny tori); the nonlinear comparison executed and not claimed; no kernel of any gravity node derived; conditional on the records-only reading, positivity, the unsoldered sphere menu and the monotone order as supplied conditions; the standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule and its one-site conditional given a recorded set; the sphere formation law in level time, its linearization and the torus modes are the objects of blocks 26 and 34 (PRs #8170, #8178, open hand-offs referenced as evidence addresses); the comparator's transverse channel is block 19's (PR #8153). All restated here as declared objects and re-executed. All proposed and unaudited.

Declared objects.
- **The axiom's law and the comparator.** The formation law: records `s_x ∈ S²` laid down level by level (`τ(x) = x₁ + x₂ + x₃`), each drawn from `K_β(· | S) ∝ e^{β s·S}` with `S` the sum of the three predecessors; in plane coordinates the predecessors of `(i, j)` are `(i, j)`, `(i − 1, j)`, `(i, j − 1)` on the level below. The **comparator**: the static sphere law on `Z³` with weight `e^{β s·s'}` per bond (block 19), whose transverse channel obeys `⟨|ŝ_⊥(k)|²⟩ ≤ 1/(βE(k))`, `E(k) = Σ_{i=1}^{3} 2(1 − cos k_i)`.
- **The linearized field and its modes.** `θ_{t+1} = Pθ_t + ξ_t` on the periodic `L × L` level plane with `P` the average over the three predecessors and `ξ` i.i.d. of variance `σ² = A(3β)/(3β)` per component; modes `θ̂_k`, multiplier `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`, `u(k) = |φ(k)|²`, `P*` the adjoint (block 34).
- **The kernel.** `C_s(k) := Cov(θ̂_k(t), θ̂_k(t+s))` in the stationary regime of the nonzero modes; as an operator `C_s = Σ_x Cov(θ_{x,t}, θ_{x',t+s})`; `M = (1/9)[[2, −1], [−1, 2]]`.
- **Executed observables.** On a plane of side `L = 256` after `2000` levels, over the next `2000`: the equal-level transverse structure factor `S₀(k) = E|ŝ_⊥(k)|²` per component (the two components orthogonal to the initial direction, unitary transform) and `C_s(k) = E[ŝ_⊥(k, t) ŝ_⊥(k, t+s)*]`, both compared to `σ²/(1 − u(k))` and `φ(k)^s`.

## Prior art and what is new

Block 13 (PR #8147) found that the causal Gaussian law's two-point function is a heat kernel in level time and never the lattice Green function; block 19 located the gravity lane's kernel in the comparator's transverse channel; block 34 (PR #8178) gave the torus modes. What is new: (i) the full space-time covariance of the linearized sphere formation law in closed form and its reading as a plane Green function times a level-time heat kernel (T1); (ii) the exact small-wavevector forms and symmetry groups of the two kernels, side by side (T2); (iii) the diffusive scaling and drift of the formation kernel and the proof that the comparator's kernel has no product structure in any direction (T3); (iv) the measurement of the nonlinear law's kernel against the linear one at three couplings, with its normalization.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | `C_s(k) = σ²φ^s(1 − u^t)/(1 − u)`; `C_s = σ²(I − PP*)^{−1}P*^s` | the mode recursion; exact rational cross-level recursions on tiny tori | B |
| T2 | `1 − u = kᵀMk + O(k⁴)`, eigenvalues, the order-six symmetry; `E = |k|² + O(k⁴)`, the cubic symmetry | series; substitutions; orbits | C |
| T3 | `|φ|^s ≤ e^{−2|k|²s/(9π²)}`; the drift; `1/E` not a product | `log(1 − y) ≤ −y`; series; a mixed derivative | D |

## Theorem T1 — the space-time covariance

**Statement.** From `θ_0 = 0`, for every mode `k` and every `t ≥ 1`, `s ≥ 0`: `Cov(θ̂_k(t), θ̂_k(t+s)) = φ(k)^s Var θ̂_k(t)`, and `Var θ̂_k(t) = σ²(1 − u^t)/(1 − u)` for `u = u(k) < 1`, `σ²t` at the zero mode. Hence on the nonzero modes the stationary kernel is `C_s(k) = σ² φ(k)^s/(1 − |φ(k)|²)`, i.e. `C_s = σ²(I − PP*)^{−1} P*^s` as an operator on the plane; on the zero mode `Cov(θ̄_t, θ̄_{t+s}) = σ²t/L²` for every `s`.

**Proof.** `θ̂_k(t+s) = φ^s θ̂_k(t) + (noise of levels t+1..t+s)`, and the later noise is independent of `θ̂_k(t)`, so the covariance is `φ^s` times the variance; the variance recursion `V(t+1) = uV(t) + σ²` sums geometrically (block 34, T1.3). In matrix form `Σ_{t,t+s} = Σ_t (P^s)ᵀ` for the real field, and `(I − PP*)^{−1}` is the sum `Σ_j (PP*)^j` that the geometric sum represents. ∎ Executed: the identities symbolically for `t ≤ 8`, `s ≤ 3` (B1); on the tori `L = 3, 4` the exact rational recursion `Σ_{t+1} = PΣ_tPᵀ + I` with `Σ_{t,t+s} = Σ_t(P^s)ᵀ` gives, for every cosine character of a nonzero mode, `Cov/Var = Re φ(k)^s` at `s = 1, 2, 3`, and `t/L²` for the plane average (B2).

*Reading.* Across a level plane the kernel is a two-dimensional Green function (block 34: its site variance diverges like `2γ log L` on the torus and `γ log t` on the plane; the structure function `E|θ_x − θ_{x+r}|²` is finite and grows like `4γ log|r|`); along levels it is the heat kernel of the level walk with multiplier `φ`. The zero mode carries the direction and random-walks (block 34).

## Theorem T2 — the small-wavevector forms and the symmetries

`1 − u(k) = kᵀMk + O(|k|⁴)` with `M = (1/9)[[2, −1], [−1, 2]]`, eigenvalues `1/9` along `(1, 1)` and `1/3` along `(1, −1)`: the plane Green function is anisotropic, stiffer across the cone's axis than along it (C1). `u` is invariant under `k₁ ↔ k₂` and `(k₁, k₂) ↦ (k₁ − k₂, −k₂)`, which generate a group of order six permuting the three predecessor directions `{k₁, k₂, k₁ − k₂}` — the symmetry of the causal cone, not of the lattice (C2). The comparator's `E(k) = Σ 2(1 − cos k_i) = |k|² + O(|k|⁴)` is isotropic and invariant under the `48` signed permutations of `(k₁, k₂, k₃)` (C1–C2).

## Theorem T3 — the scaling, the drift, and the non-product form of the comparator

For every nonzero mode `|C_s(k)|/C_0(k) = |φ(k)|^s = u^{s/2} ≤ e^{−(1 − u)s/2} ≤ e^{−2|k|²s/(9π²)}` on the square `|k_i| ≤ π` (from `log(1 − y) ≤ −y` and block 34's `1 − u ≥ 4|k|²/(9π²)`): correlations `s` levels apart survive only at in-plane scales `|k|^{−1} ≳ √s` — diffusive scaling `r² ~ s`. And `φ(k) = 1 + i(k₁ + k₂)/3 + O(|k|²)`: the heat kernel drifts by one third of a step along each predecessor direction per level, i.e. along the axis of the causal cone (D1). The comparator's `1/E(k)` is not of the form `f(k₁, k₂) g(k₃)` in any direction — `∂²log E/∂k₁∂k₃ ≠ 0` — so it cannot be read as a plane Green function times a propagator; it has no causal direction (D2). The formation kernel is exactly of that form.

## Executed: the nonlinear law on a large plane (not proved)

Control `specs/supervisor_control_block35_kernel_sim.py` (block 26's exact sampler on a `256 × 256` periodic plane from the aligned plane; the transverse components orthogonal to the initial direction — the average direction moves only on the scale `3βL²/A(3β) ≈ 10⁶` levels, far beyond the run; the structure factor and the cross-level products accumulated over levels `2001–4000`). Output in `.out.txt`.

| `β` | `|m|` | `S₀(k)/[σ²/(1 − u(k))]`, `|k| < 0.3` | `0.6–1.0` | `1.5–2.2` | `3.2–5.0` | `C_s/C_0` against `φ^s` at `k = 2π(4,1)/L`, `s = 64` (modulus) | at `k = 2π(8,8)/L`, `s = 64` |
|---|---|---|---|---|---|---|---|
| 6 | `0.736` | `0.830` | `0.861` | `0.878` | `0.887` | `0.909 / 0.946` | `0.798 / 0.760` |
| 12 | `0.876` | `0.898` | `0.934` | `0.936` | `0.938` | `0.965 / 0.946` | `0.726 / 0.760` |
| 24 | `0.937` | `0.940` | `0.967` | `0.966` | `0.967` | `0.986 / 0.946` | `0.768 / 0.760` |

What the runs say. (i) At every coupling the equal-level structure factor is the linearized kernel `σ²/(1 − u(k))` times a normalization `c(β)` below one — `0.89`, `0.94`, `0.97` at short wavelengths — slightly lower at the longest wavelengths (`0.83`, `0.90`, `0.94`); `c(β) → 1` as `β` grows. (ii) The cross-level correlations reproduce `φ(k)^s` in phase exactly (the drift) and in modulus within a few percent up to `s = 64` at all wavevectors shown, the residual growing with `s` and with `1/β`. (iii) The structure function `E|θ_x − θ_{x+r}|²` along the lattice directions and the diagonal is the linear one times a ratio falling from the short-wavelength `c(β)` at `r = 1` (`0.88`, `0.94`, `0.97`) to the long-wavelength one at `r = 32` (`0.84`, `0.89`, `0.93`). So the real law's transverse correlations at strong coupling are the exact linear kernel with a coupling-dependent normalization, as block 29 found for the comparator's channel (`0.9–1.0`); the two channels differ in their form, not in their normalization.

## No-Go Discipline Gate

The note's sentences are positive (an exact kernel) and one negative (the comparator's kernel is not it); the gate applies.

### N1 — Routes by which the sentences could fail
1. *The modes* — a circulant on the torus; the identities are symbolic and the tiny tori check the chain exactly (T1).
2. *The comparator misdescribed* — its transverse channel is taken as block 19 states it (an infrared bound by `1/(βE(k))`), and only its functional form is used (T2–T3); no property of the comparator beyond `E(k)` enters.
3. *A product structure of `1/E` in a rotated frame* — excluded: the mixed derivative is computed in the lattice frame, and the product form is not invariant under rotations that mix `k₃` with `k₁`, so no frame gives it; the formation kernel's product structure holds in the level-time frame by construction.
4. *The measurement* — the transverse frame is fixed to the initial direction; the average direction stays within the small-angle regime over the run (block 34's memory time); the normalization `c(β)` could carry a frame contribution at the longest wavelengths, which is where it dips.
5. *What the gravity node's kernel becomes* — not derived; the gravity lane's construction took the comparator's channel as input, and re-running that construction with this kernel is the gravity lane's obligation.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, and blocks 19, 26, 34's objects as declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| block 26 (open PR #8170) | the law, the linearization, `σ²` | yes (restated) |
| block 34 (open PR #8178) | the torus modes, `1 − u ≥ 4|k|²/(9π²)` | yes (restated; T3) |
| block 19 (open PR #8153) | the comparator's transverse channel `1/(βE(k))` | yes (its form only) |
| block 13 (open PR #8147) | the heat-kernel reading of the causal Gaussian law | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "under the formation reading the linearized kernel is a plane Green function times a level-time heat kernel, not the comparator's 3D Green function" | executed: the mode covariance identity; the small-k forms; the drift; `log(1 − y) ≤ −y` | executed: the exact cross-level recursions on tiny tori | executed: the symmetry groups; the non-product form of `1/E` | executed: the diffusive bound for every nonzero mode | T1–T3 for every `L`, `β`; the nonlinear law's normalization executed, not claimed; no gravity kernel derived |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "You have shown the linear kernels differ; the gravity lane used the nonlinear comparator at strong coupling, and its kernel was the nonlinear channel's infrared form." Reply: the nonlinear law's channel is measured here to be the linear kernel times `0.83–0.97` at every wavevector, exactly as the comparator's was measured to be its linear kernel times `0.9–1.0` (block 29); the forms differ at the linear level and the nonlinear corrections are normalizations. Conceded: no gravity kernel is derived here; the lane's construction has to be re-run with this input.

### N8 — Cross-cycle echo
Block 13's heat kernel returns as the level-time factor; block 34's zero mode as the non-stationary part; block 29's normalization measurement as the method; the decision record's consequence as the reason for the block.

## Falsifiers
- The covariance identity failing symbolically; a tiny torus where the cross-level recursion and `Re φ^s` differ (B1–B2).
- A second-order form other than `kᵀMk`, eigenvalues other than `1/9, 1/3`, a substitution that fails to leave `u` invariant, an orbit of size other than six, `E` failing a signed permutation (C1–C2).
- The decay bound failing, a drift other than `(k₁ + k₂)/3`, or `log(1/E)` with vanishing mixed derivative (D1–D2).

## Boundaries and non-claims
This note proves that, under the axiom's reading, the linearized transverse field of the sphere formation law has the space-time covariance `σ² φ(k)^s/(1 − |φ(k)|²)` on the nonzero modes of the level plane — the two-dimensional Green function of `I − PP*` across the plane times the `s`-step heat kernel along levels, diffusive (`r² ~ s`), drifting along the causal cone's axis, with the three-fold symmetry of the three predecessor directions and a diffusing zero mode — and that the comparator's three-dimensional lattice Green function `1/(βE(k))`, isotropic under the cubic group and not a product of a plane factor and a propagator, is not this object; it measures the nonlinear sphere formation law against the linearized kernel on a large plane; it does not derive a gravity node's kernel under the formation reading, does not treat other menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. Blocks 19, 26, 34 (PRs #8153, #8170, #8178, open): the comparator's channel, the law and linearization, the torus modes; restated. Block 13 (PR #8147, open) as an evidence address.
- Named standard imports at definition level (never as authority for physics): the diagonalization of a circulant by the characters of `Z_L²` (Fourier); the geometric series.
- Reference only (named, not used): Goldstone (1961) for the comparator's massless channel as block 19 described it.

## Review record
Supervisor-run block (owner 2026-09-18: "use the rest of your limit, work the next block", after the correction that the formation reading is the axiom and the static law only the comparator). Lens: the gravity kernel of block 19 is a comparator object; the question is what the same channel is under the axiom's reading, and for the linear part it is exactly computable from block 34's modes. Controls: block 26's sampler on a `256 × 256` plane (`specs/supervisor_control_block35_kernel_sim.py`); a scaling slip in the real-space structure function (a factor `L`) caught by the ratio to the linear value being `≈ 256 c(β)` and corrected. Lens pass on the contract: the exact sentences confined to the linearized field; no gravity kernel derived or claimed; the comparator described only through the form of `E(k)`. Primary: T1–T3 (runner, 14 checks, 7 mutations). Refuting pass (`CHECKER_block35_findings.md`, `..._refuter.py`): a floating-point cross-level recursion on `L = 8` against `φ^s`; the small-k forms numerically; a second measurement at `β = 12` in the frame rotating with the plane average against the fixed-frame one. Fold: none beyond the scaling slip.

## Verification

```bash
python3 scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py
python3 scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py --list-mutations
python3 scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py --mutation small_k_form_wrong
```

Families: A authority and inputs; B the space-time covariance; C the small-wavevector forms and symmetries; D the scaling and the comparator's non-product form; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 7 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=15 FAIL=0`.
