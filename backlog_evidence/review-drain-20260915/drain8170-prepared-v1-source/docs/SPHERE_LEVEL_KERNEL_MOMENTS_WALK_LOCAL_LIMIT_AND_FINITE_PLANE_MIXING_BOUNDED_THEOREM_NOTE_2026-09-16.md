---
claim_id: sphere_level_kernel_moments_walk_local_limit_and_finite_plane_mixing_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Supplied sphere level kernel: exact moments and conditional mean Jacobian; three-step planar walk local-limit and harmonic bounds; finite periodic-plane minorization and invariant law; separately supplied additive-noise recursion variance and scalar proxy. No nonlinear infinite-plane decay or physical selection claim."
upstream_dependencies: [minimal_axioms, admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06]
runner: scripts/sphere_level_kernel_moments_walk_local_limit_finite_plane_mixing_2026_09_16.py
---

# Sphere level-kernel moments, walk local limits and finite-plane mixing

**Type:** bounded_theorem
**Status:** conditional-support; source review and execution remain separate from audit status.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
artifact_role: theorem_plus_decisive_artifact
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Scope and premises

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply lattice, site possibility, local admissibility and records. The [finite-window product-rule classification](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies records-only product-rule vocabulary. Neither selects the continuous sphere menu, exponential pair weight, β, level schedule, conditional independence across a level, or a physical stochastic process. These are the explicit conditions below.

The proof uses sphere integration, convergent power series, Parseval on the torus, Gaussian integration, independent-noise variance addition, the tower property, and uniform minorization for a Markov kernel. These mathematical tools are disclosed; no empirical fit enters any theorem. Complete originals, attempted routes and raw outputs are preserved in [historical recovery](work_history/repo/review_feedback/pr8170-evidence/README.md).

## Declared objects

- **The unsoldered menu and rule.** Values are unit vectors `s ∈ S²` (a supplied continuous menu); the covariant overlap weight `φ(s, s') = e^{β s·s'}` with `β > 0` (a supplied coupling family). The one-site conditional given a recorded set `A` of neighbours is `K(s | s_A) ∝ Π_{y∈A} φ(s, s_y)` against the uniform surface measure.
- **Space-time and level time.** Sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`; records form level by level, the record at `x` drawn from `K_β(· | s_{x−e_1}, s_{x−e_2}, s_{x−e_3})`, independently across a level given the previous one; level `0` carries a supplied plane. The **level automaton** is the Markov chain of level configurations on `(S²)^{Z²}` after the bijection `x ↦ (x_2, x_3)` of each level; its neighbourhood is `{(0,0), (−1,0), (0,−1)}`. The **plane coordinates** of the three predecessors are the shifts `(0,0)`, `(−1,0)`, `(0,−1)`.
- **The sphere kernel.** For `S ∈ R³`, `K_β(ds | S) = (κ/(4π sinh κ)) e^{κ s·û} dσ(s)` with `κ = β|S|`, `û = S/|S|` (uniform when `S = 0`), `dσ` the surface measure. `A(κ) = coth κ − 1/κ` (the mean cosine to `û`).
- **The magnetization.** From the aligned plane (every level-`0` record equal to `e`), `m_t = E[s_x·e]` at any site `x` of level `t` (the same at every site by translation invariance).
- **The level walk.** The walk on `Z²` with steps `(0,0)`, `(−1,0)`, `(0,−1)`, each with probability `1/3`; `p_k(y)` its `k`-step law; `P_k = Σ_y p_k(y)²`; `u(θ) = |φ(θ)|²` with `φ(θ) = (1 + e^{−iθ_1} + e^{−iθ_2})/3`, so `u = (3 + 2cos θ_1 + 2cos θ_2 + 2cos(θ_1 − θ_2))/9`.
- **The supplied auxiliary field.** `θ_x = (θ_{x−e_1} + θ_{x−e_2} + θ_{x−e_3})/3 + ξ_x` on levels `t ≥ 1` with `θ ≡ 0` on level `0` and `ξ_x` i.i.d. centred with variance `σ² = A(3β)/(3β)` per component (two components); `v_t` its variance per component at level `t`; `H_t = Σ_{k≤t} 1/k`.

## Kernel moments and strict mean bound


**Statement.** (a) `K_β(· | S)` has mean `A(κ)û` and second moment `E[s sᵀ | S] = (A(κ)/κ) I + (1 − 3A(κ)/κ) ûûᵀ`, where `κ = β|S|`, `û = S/|S|`; in particular `E[(s·û)²] = 1 − 2A/κ` and the transverse second moment is `E|s − (s·û)û|² = 2A/κ`. (b) `0 < A(κ) < κ/3` for `κ > 0`, and `A(κ) < 1`. (c) From the aligned plane, `m_1 = A(3β)` and the one-step transverse second moment is `2A(3β)/(3β)`; more generally `m_{t+1} = E[A(β|S|) (S·e)/|S|]` with `S` the sum of the three predecessors at level `t`.

**Proof.** (a) With `w = s·û`, the surface measure gives `∫ e^{κ s·û} dσ = 2π ∫_{−1}^{1} e^{κw} dw = 4π sinh κ/κ`, `E[w] = ∫ w e^{κw} dw / ∫ e^{κw} dw = coth κ − 1/κ` and `E[w²] = 1 − 2A/κ` (integration by parts; B1). The law is invariant under rotations about `û`, so `E[s] = E[w] û` and `E[s sᵀ] = a I + b ûûᵀ` with `a + b = E[w²]` and trace `3a + b = 1`, whence `a = A/κ`, `b = 1 − 3A/κ`. (b) For `κ > 0`, define `f(κ) = (κ² + 3)sinh κ − 3κ cosh κ`. Expanding the entire functions gives
`f(κ) = Σ_{n≥2} 4n(n−1) κ^{2n+1}/(2n+1)! > 0`:
the coefficient is `[ (2n)(2n+1) + 3 − 3(2n+1) ]/(2n+1)! = 4n(n−1)/(2n+1)!`, with the constant/linear/cubic terms zero.
Dividing `f(κ)>0` by `3κ sinh κ>0` gives `A(κ)<κ/3`.
Also `A'(κ)=1/κ²−1/sinh²κ>0` since `sinh κ>κ`, and `A(0+)=0`, so `A>0`.
Since the kernel has a strictly positive continuous density on the sphere and `w<1` almost surely, `A=E[w]<1`.
The former derivative upper bound is false: at `κ=1`, `sinh²1 > 1+1/3+2/45=62/45>4/3`, whence `A'(1)>1/4`.
This counterexample is retained as a rejection control; it is not used to infer an upper derivative bound. (c) At the aligned plane `S = 3e`, `κ = 3β`, `û = e`; apply (a). The general identity is the tower property with (a). ∎ (B1–B3: the moments symbolically; the series and the bound; exact rational enclosures of `A(3β)` at `β = 3, 6, 12, 24`: `[8888, 8889]/10⁴`, `[9444, 9445]/10⁴`, `[9722, 9723]/10⁴`, `[9861, 9862]/10⁴`.)

## Conditional mean derivative and quadratic mode

**Statement.** Near the pole, `s=(θ,√(1−|θ|²))` and `s_i=(θ_i,√(1−|θ_i|²))`. The exponent has expansion
`β s·Σ_i s_i = 3β − (β/2)Σ_i|θ−θ_i|² + O(4)`.
Its quadratic maximum is the average `Σ_i θ_i/3`, with Hessian `−3β I`.
The exact conditional transverse mean has derivative `A(3β)Σ_i θ_i/3`, not gain one. The normalized mean direction has derivative `Σ_i θ_i/3`. The exact aligned one-step variance is `A(3β)/(3β)` per component.

**Proof.** `s·s_i=θ·θ_i+√(1−|θ|²)√(1−|θ_i|²)=1−|θ−θ_i|²/2+O(4)`; summing proves the expansion. The squared-distance sum has gradient zero at the average and Hessian `6I`, so the exponent has negative Hessian and a maximum there. Put `S=Σ_i s_i`. Its transverse part is `Σ_i θ_i`, its longitudinal part is `3+O(|θ_i|²)`, and `|S|=3+O(|θ_i|²)`. Substitution into the exact mean `A(β|S|)S/|S|` gives transverse derivative `A(3β)Σ_i θ_i/3`; normalization divides out the nonzero mean length. For a common rotation by angle `h`, the exact transverse mean is `A(3β)sin h`, whose derivative is `A(3β)<1`. Rotational covariance rotates this shorter mean vector, not a unit vector. The variance follows from the two equal transverse entries of the second-moment tensor at `κ=3β`. ∎

The gain-one additive-noise recursion below is separately supplied. Matching its noise variance to this one-step variance is a declared modeling choice. It does not derive an exact nonlinear evolution equation.

## Level-walk local-limit constant (historical proof label T3)


**Statement.** For every `k ≥ 1`,
```
3√3/(4πk) − 1/k² − (5/(2k)) e^{−k/4}  ≤  P_k  ≤  3√3/(4πk) + 27/k² + e^{−√k/7};
```
hence `k P_k → 3√3/(4π)`. Moreover `Σ_{k≤t} P_k ≥ (3√3/(4π)) H_t − 1/4` for every `t ≥ 1`, so `Σ_{k≤t} P_k ≥ (3√3/(4π)) log t − 1/4`.

**Proof.** *The representation.* `p_k(y) = (2π)^{−2} ∫_{[−π,π]²} φ(θ)^k e^{−iθ·y} dθ` and, by Parseval, `P_k = (2π)^{−2} ∫ u(θ)^k dθ` with `u = |φ|²`. *The identity.* `1 − u = (4/9)[sin²(θ_1/2) + sin²(θ_2/2) + sin²((θ_1 − θ_2)/2)]` (D3). *Bounds on `1 − u`.* From `x²/4 − x⁴/48 ≤ sin²(x/2) ≤ x²/4` (all real `x`): `Q − W ≤ 1 − u ≤ Q` on `R²`, with `Q(θ) = (1/9)(θ_1² + θ_2² + (θ_1 − θ_2)²) = θᵀMθ`, `M = (1/9)[[2, −1], [−1, 2]]`, `det M = 1/27`, `Q ≥ |θ|²/9`, and `W = (1/108)(θ_1⁴ + θ_2⁴ + (θ_1 − θ_2)⁴) ≤ |θ|⁴/12` (as `(θ_1 − θ_2)⁴ ≤ 8(θ_1⁴ + θ_2⁴)`). On the square, from `sin²(x/2) ≥ x²/π²` for `|x| ≤ π` (dropping the third term): `1 − u ≥ (4/(9π²))|θ|²`. *Upper bound.* Let `ρ = (12/k)^{1/4}` (`ρ < π`). Outside `|θ| ≤ ρ`, `u^k ≤ (1 − 4ρ²/(9π²))^k ≤ e^{−(4√12/(9π²))√k} ≤ e^{−√k/7}`, and the normalized area is at most `1`. Inside, `u ≤ 1 − Q + W ≤ e^{W − Q}` and `kW ≤ kρ⁴/12 = 1`, so `u^k ≤ e^{−kQ} e^{kW} ≤ e^{−kQ}(1 + e·kW)`; therefore `(2π)^{−2} ∫_{|θ|≤ρ} u^k ≤ (2π)^{−2}[∫_{R²} e^{−kQ} + (ek/12) ∫_{R²} e^{−k|θ|²/9} |θ|⁴] = (2π)^{−2}[3√3π/k + (ek/12)(1458π/k³)] ≤ 3√3/(4πk) + 27/k²` (`121.5e/(4π) < 27`; the Gaussian integrals: D3). *Lower bound.* On `{Q ≤ 1/2}` (inside the square, as `|θ| ≤ 3/√2 < π` there), `u ≥ 1 − Q` and `log(1 − Q) ≥ −Q − Q²`, so `u^k ≥ e^{−kQ}(1 − kQ²)`; hence `P_k ≥ (2π)^{−2}[∫_{R²} e^{−kQ} − ∫_{Q>1/2} e^{−kQ} − k ∫_{R²} e^{−kQ} Q²] ≥ (2π)^{−2}[3√3π/k − e^{−k/4}·6√3π/k − k·(3√3π/k)(2/k²)] ≥ 3√3/(4πk) − (5/(2k))e^{−k/4} − 1/k²` (`∫ e^{−kQ}Q² = (3√3π/k)(2/k²)`: D3; `3√3/(2π) < 1`, `6√3/(4π) < 5/2`). *The harmonic bound.* For `t ≤ 150` the exact sums satisfy `Σ_{k≤t} P_k ≥ (3√3/(4π))H_t − 6/25` (D3, exact rationals with `3√3/(4π)` enclosed from above). For `t > 150`, the lower bound gives `Σ_{150<k≤t} P_k ≥ (3√3/(4π))(H_t − H_{150}) − Σ_{k>150}[1/k² + (5/(2k))e^{−k/4}] ≥ (3√3/(4π))(H_t − H_{150}) − 1/100`; adding, `Σ_{k≤t} P_k ≥ (3√3/(4π))H_t − 1/4`. Finally `H_t ≥ log t`. ∎ (D1: the trinomial form of `p_k` by enumeration; D2: the two-sided bounds for `k ≤ 150` with `√3`, `π` and the exponentials enclosed rationally, and `k²|P_k − 3√3/(4πk)| < 1`; D3: the identity, the Gaussian integrals, the harmonic bound.)

*Reading.* The exact sums lie below `3√3/(4πk)` by about `1/(10k²)`; the stated errors are what the elementary argument gives.

## Finite periodic-plane mixing (historical proof label T4)


**Statement.** On the periodic `L × L` level plane the level automaton has a unique invariant law `π_L`, invariant under every rotation of `S²`; from any initial plane, `|E[s_x · e] at level t| ≤ 2(1 − δ_L^{L²})^t` with `δ_L = 6β/(e^{6β} − 1)`; in particular the magnetization tends to `0`. On the one-site plane (`L = 1`), from the aligned plane, `m_t = A(3β)^t` exactly.

**Proof.** The density of `K_β(· | S)` against the uniform probability law on the sphere is `(κ/sinh κ) e^{κ s·û} ≥ (κ/sinh κ) e^{−κ} = 2κ/(e^{2κ} − 1)`, a decreasing function of `κ` (E2), and `κ = β|S| ≤ 3β`; so every site's conditional has density at least `δ_L := 6β/(e^{6β} − 1)` (and `1` when `S = 0`). The level kernel is the product over the `L²` sites, so it has density at least `δ_L^{L²}` against the product uniform law: a uniform minorization, which gives a unique invariant law and total-variation distance `≤ (1 − δ_L^{L²})^t` from it after `t` levels. The kernel commutes with the simultaneous rotation of all records (`K_β(Rs | RS) = K_β(s | S)`), so `π_L ∘ R^{−1}` is invariant and equals `π_L`; the vector `E_{π_L}[s_x]` is then fixed by every rotation, hence `0`, and `|E_t[s_x·e]| ≤ 2(1 − δ_L^{L²})^t`. For `L = 1` the chain is `s_{t+1} ∼ K_β(· | 3s_t)`, with `E[s_{t+1}·e | s_t] = A(3β)(s_t·e)` by T1(a) (`κ = 3β`, `û = s_t`); iterate. ∎ (E1: the one-site recursion symbolically; E2: the minorization identities.)

The displayed finite-plane rate is the only nonlinear memory bound asserted here.

## Supplied auxiliary-field variance (historical proof label T5)


**Statement.** From the aligned plane, `v_t = σ² Σ_{k<t} P_k` per component, `σ² = A(3β)/(3β)`; hence, with `γ(β) := (3√3/(4π))·A(3β)/(3β)`,
```
σ² ((3√3/(4π)) H_{t−1} − 1/4)  ≤  v_t  ≤  σ² ((3√3/(4π)) H_{t−1} + 150)      (t ≥ 2),
```
so `v_t = γ(β) log t + O(1)` and `v_t → ∞`; the declared scalar proxy `e^{−v_t}` is of order `t^{−γ(β)}`. This proxy is not asserted to equal any nonlinear sphere magnetization. Exactly, `γ(β) ∈ [408, 409]/10⁴` at `β = 3`, `[216, 217]/10⁴` at `6`, `[1116, 1117]/10⁵` at `12`, `[566, 567]/10⁵` at `24`, and `γ(β) ∼ √3/(4πβ)` as `β → ∞`.

**Proof.** Unfolding the recursion, `θ_x = Σ_{k<t} Σ_y p_k(y) ξ_{x − (0, y), t−k}` (the level walk started at `x`'s plane coordinates; T3's `p_k`), a sum of independent centred terms, so `Var = σ² Σ_{k<t} Σ_y p_k(y)² = σ² Σ_{k<t} P_k`. The bounds are the local-limit theorem with `P_0=1` explicitly included: `1 + 27π²/6 + 98 < 150`, since the decreasing exponential tail is bounded by `∫_0^∞ e^{−√x/7} dx=98`. The lower bound may discard the positive `P_0` term. Summability of the two-sided error gives the stated logarithmic asymptotic. Since `A(3β)→1`, the displayed large-β equivalence follows. The enclosures of `γ` are exact arithmetic (E3). ∎

## Six-axis finite conditional identities

For the supplied six-point menu `{±e_1,±e_2,±e_3}`, assign pair weights `p=e^β`, `q=e^{−β}`, `r=1` for equal, antipodal and orthogonal records. With an aligned target value and respectively three equal predecessors, two equal plus one antipodal, or two equal plus one orthogonal, direct enumeration gives target weights `p³`, `p²q`, `p²r` and total weights `p³+q³+4r³`, `pq(p+q)+4r³`, `r(p²+q²)+r²(p+q)+2r³`. Subtracting their normalized probabilities from one yields
`(e^{−3β}+4)/(e^{3β}+e^{−3β}+4)`,
`(e^{−β}+4)/(e^β+e^{−β}+4)`, and
`(e^{−2β}+e^β+e^{−β}+2)/(e^{2β}+e^{−2β}+e^β+e^{−β}+2)`.
For the aligned triple the deviation is below `1/1600` at β=3 and below `1/10^7` at β=6, using the exponential series lower bounds. These are one-site identities, not infinite-time simulation claims.

## Boundary and recovery

Finite-plane minorization supplies the displayed contraction rate. It supplies neither a βL² nonlinear memory scale nor a lower bound on memory time. The time/size limits are not interchanged. The separately supplied auxiliary model does not determine the effect of cubic nonlinear terms. No nonlinear exponent ordering or asymptotic phase comparison follows from the archived histories.

Current-main context has changed since the original packet: the six-axis formation result now has a reviewed T0–T7 construction under its stated small-noise assumptions. The static six-axis reflection/contour result remains conditional. Neither is a premise of this sphere proof; the former four-cell settled memory map is withdrawn. Their exact paths and hashes are recorded as context in the author input plan, without adding theorem dependencies here.

The complete auxiliary finite-variance contradiction is retained readably in the recovery appendix. Its conditional mathematics is not rejected; formal negative certification and separate active promotion are deferred. Historical nonlinear decay/exponent conjectures and the time-dependent twist entropy obligation remain open, with branch recovery retained. Historical fitting scripts are not promoted: missing split inputs and absent projections are not manufactured.

## No-Go Discipline Gate

### N1 — Actual routes and limits
The historical five entries are diagnostics/attempts, not five closed independent attacks: later plateau remains open; finite-size exclusion was unsupported and withdrawn; sampler comparisons are finite diagnostics; the fixed-twist entropy outline leaves time-dependent twists and terminal entropy control open; exponent ordering is contradicted by retained historical rows. No broad negative certification is claimed. Finite-plane convergence is the direct corollary of the explicit uniform minorization proved above, not a route no-go.

### N2 — Premise independence
No repository wall is imported. The sphere kernel, β>0, finite periodic geometry and level-product kernel are supplied together as the finite-plane theorem's hypotheses. No unsupported independence certificate is issued.

### N3 — Hidden conditions
The auxiliary recursion additionally requires independent centered noise of the declared finite variance, independent of the initial field. It is not the exact nonlinear conditional mean map.

### N4 — Dependency roles
Only the two linked authorities supply framework and finite-product vocabulary. All moment, walk and finite-plane arguments are written here. Historical phase/simulation comparisons and certificates confer no current authority.

### N5 — Resolution
The runner checks symbolic moments, finite coefficient identities and rational enclosures; finite path enumeration and return sums through k=150; symbolic one-site/minorization identities; auxiliary variance constants. General local-limit and invariant-law results have written proofs. No nonlinear simulation or infinite-plane execution is part of this corrected primary. Exact execution counts belong to its future captured stdout, not this preparation.

### N6 — Open choices
No new axiom or primitive is proposed. Selecting a physical menu, coupling or formation schedule remains outside this supplied model.

### N7 — Strong alternative
Finite histories can be compatible with later plateaus, size-dependent behavior or nontrivial infinite-plane laws. Those possibilities are not ruled out here. The finite-plane theorem and auxiliary variance identity retain their own stated domains.

### N8 — Historical comparisons
The former equilibrium analogy and fixed-twist outline do not close a nonequilibrium infinite-plane theorem. The corrected current-main formation result concerns its own six-axis model and threshold. No echo between these results supplies the missing sphere argument.

## Verification

Paired [exact runner](../scripts/sphere_level_kernel_moments_walk_local_limit_finite_plane_mixing_2026_09_16.py) retains the complete finite return-sum fixtures and exact rational enclosures. Future cache path: `logs/runner-cache/sphere_level_kernel_moments_walk_local_limit_finite_plane_mixing_2026_09_16.txt`; JSON uses the same stem under `logs/runner-cache`. No cache is asserted present by this source preparation.

```bash
python3 scripts/sphere_level_kernel_moments_walk_local_limit_finite_plane_mixing_2026_09_16.py
python3 scripts/sphere_level_kernel_moments_walk_local_limit_finite_plane_mixing_2026_09_16.py --list-mutations
```

The original 14 mutation sources remain recoverable. Twelve mathematical mutation names remain active; two prose-policy mutations are retired with the old prose scanner, and two decisive new mathematical controls cover the corrected series coefficient and exact mean gain. No mutation census has been executed on this source. The inherited 900-second cap is retained, with a proposed external 768 MiB process-tree cap for SymPy and the fixed exact k≤150 workload.
