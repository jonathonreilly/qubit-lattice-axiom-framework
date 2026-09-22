---
claim_id: admissibility_rule_sphere_static_law_weak_coupling_comparison_and_correlation_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For a supplied uniform-sphere exponential nearest-neighbour static specification on Z^3: W1 bounds the one-site total-variation response, W2 gives alpha=2sqrt(3)beta, W3 proves finite-window comparison, W4 constructs the unique rotation-invariant DLR law when alpha<1, and W5 bounds correlations, torus magnetization and structure factors. Torus results require L>=2. No strong-coupling comparison or physical kernel classification is retained."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py
---

# Sphere Static Law Weak Coupling Comparison And Correlation Bounds

**Type:** bounded_theorem

**Status:** bounded-support; conditional supplied model; unaudited.

## Result up front

For a supplied uniform-sphere exponential nearest-neighbour static specification on Z^3: W1 bounds the one-site total-variation response, W2 gives alpha=2sqrt(3)beta, W3 proves finite-window comparison, W4 constructs the unique rotation-invariant DLR law when alpha<1, and W5 bounds correlations, torus magnetization and structure factors. Torus results require L>=2. No strong-coupling comparison or physical kernel classification is retained.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Quantitative mathematical bounds for explicitly supplied sphere static models; no physical channel classification."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Original independent affected-source confirmation and bounded finite evidence capture; retained-grade audit remains separate."
conditional_surface_status: "For a supplied uniform-sphere exponential nearest-neighbour static specification on Z^3: W1 bounds the one-site total-variation response, W2 gives alpha=2sqrt(3)beta, W3 proves finite-window comparison, W4 constructs the unique rotation-invariant DLR law when alpha<1, and W5 bounds correlations, torus magnetization and structure factors. Torus results require L>=2. No strong-coupling comparison or physical kernel classification is retained."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The linked repository context is [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md); [POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md); [ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06](ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md). The possibility parent supplies conditional representation vocabulary; it does not select this probability law. We explicitly supply the uniform surface measure on S², beta>0, the exponential pair weight and the static specification. These are mathematical model premises, not consequences selecting physics from the axioms. The independent d-dimensional nearest-neighbour model omits all couplings outside that dimension; a two-dimensional model is not the marginal of a plane in an interacting three-dimensional model. All torus claims below use L>=2 (side at least four), so neighbours are distinct.

Declared objects.
- **The rule and its windows.** Records `s_x ∈ S²`; `β > 0` supplied; the one-site conditional given the neighbouring records, `P_h(ds) = e^{β s·h} dσ(s)/Z(h)`, `h = Σ_{y ~ x} s_y`, `Z(h) = ∫ e^{β s·h} dσ = 4π sinh(β|h|)/(β|h|)`, `dσ` the uniform surface measure. For a finite window `Λ` with exterior records `ω` on the sites adjacent to `Λ`: `μ_Λ^ω(ds_Λ) ∝ Π_{⟨xy⟩ ⊂ Λ} e^{β s_x·s_y} Π_{x ∈ Λ, y ∉ Λ, y ~ x} e^{β s_x·ω_y} Π_{x ∈ Λ} dσ(s_x)`; its conditional at `x` given the other records is `P_{h_x}` with `h_x` the sum over the six neighbours (interior records or exterior ones). The torus law `μ_L` on `(Z/2LZ)³`, `N = (2L)³`, has the same conditionals. An **infinite-volume static law** is a probability measure on `(S²)^{Z³}` whose conditional law on every finite window given the exterior records is `μ_Λ^ω`.
- **The function `L`.** `L(x) = coth x − 1/x` for `x > 0`, `L(0) = 0`; `L'(x) = 1/x² − 1/sinh² x`.
- **Coefficients.** `c := β/√3`; `α := 6c = 2√3 β`. For a window `Λ`: `C_Λ` the matrix with `(C_Λ)_{xy} = c` when `x, y ∈ Λ` are neighbours and `0` otherwise; `D_Λ = Σ_{k ≥ 0} C_Λ^k`; for exterior records `ω, ω'`, `b_x = c · #{y ∉ Λ : y ~ x, ω_y ≠ ω'_y}`.
- **Oscillations.** For `f` on `(S²)^Λ`, `δ_x(f) = sup{|f(ζ) − f(ζ')| : ζ, ζ' differ only at x}`; `‖f‖_δ = Σ_x δ_x(f)`. A local function depends on the records in a box `Δ_ℓ = {|x|₁ ≤ ℓ}`.
- **Transforms and order parameter** on the torus: `ŝ(k) = N^{−1/2} Σ_x e^{ik·x} s_x`; `M_N² = N^{−2}⟨|Σ_x s_x|²⟩`; `d_T(0, x)` the torus `ℓ¹` distance.



## Prior art and what is new


The one-site contraction criterion for uniqueness is Dobrushin's (1968), with exponential decay of correlations under it (Dobrushin–Shlosman; Föllmer; Künsch); for the classical three-component model it is textbook. None is used as authority; W1–W5 are re-proved at scope.  The contribution retained here is the explicit mathematical bounds for the supplied model. No comparison with physical channels is used.

## Theorem W1 — the total-variation response of the one-site conditional

**Statement.** For all `h, h' ∈ R³`, `TV(P_h, P_{h'}) ≤ (β/(2√3)) |h − h'|`.

**Proof.** (i) *The covariance of a record under a field.* Fix `h ≠ 0`, `x = β|h|`, `ĥ = h/|h|`. Under `P_h`, `s·ĥ` has density `∝ e^{xt}` on `[−1, 1]`, so `E[s·ĥ] = L(x)` and `E[(s·ĥ)²] = 1 − 2L(x)/x` (both by integrating `e^{xt}` and `t e^{xt}`, `t² e^{xt}` over `[−1, 1]`); hence `Var(s·ĥ) = 1 − 2L/x − L² = 1/x² − 1/sinh² x = L'(x)`. For a unit `e ⊥ ĥ`, `E[s·e] = 0` (the reflection `e → −e` preserves `P_h`) and `E[(s·e)²] = (1 − E[(s·ĥ)²])/2 = L(x)/x` (the two transverse directions share `1 − (s·ĥ)²`); the cross moments `E[(s·ĥ)(s·e)]` and `E[(s·e)(s·e')]` vanish by the same reflections. So the covariance matrix of `s` under `P_h` is diagonal in the frame `(ĥ, e, e')` with eigenvalues `L'(x), L(x)/x, L(x)/x`; at `h = 0` it is `I/3`. (ii) *Both eigenvalues are at most `1/3`.* `L'(x) ≤ 1/3` is, after multiplying by `3x² sinh² x > 0`, `3 sinh² x − 3x² ≤ x² sinh² x`. With `sinh² x = (cosh 2x − 1)/2`, the left side is `Σ_{n ≥ 2} (3/2) 2^{2n} x^{2n}/(2n)!` and the right side `Σ_{n ≥ 2} (1/2) 2^{2n−2} x^{2n}/(2n−2)!`; the ratio of the coefficients of `x^{2n}` is `6/(n(2n−1)) ≤ 1` for `n ≥ 2`, so the inequality holds termwise for `x > 0`. `L(x)/x ≤ 1/3` is, after multiplying by `x sinh x > 0`, `x cosh x − sinh x ≤ (x²/3) sinh x`; the left side is `Σ_{n ≥ 1} 2n x^{2n+1}/(2n+1)!`, the right side `Σ_{n ≥ 1} x^{2n+1}/(3(2n−1)!)`, and the coefficient ratio is `3/(2n+1) ≤ 1` for `n ≥ 1`. Hence for every `h` and every `Δ ∈ R³`, `Var_h(s·Δ) ≤ |Δ|²/3`. (iii) *The derivative.* For `h_t = h + tΔ`, `Δ = h' − h`, and a Borel set `A ⊂ S²`, `P_t(A) := P_{h_t}(A) = ∫_A e^{β s·h_t} dσ / Z(h_t)` is smooth in `t` and `d/dt P_t(A) = β [E_t((s·Δ) 1_A) − P_t(A) E_t(s·Δ)] = β Cov_t(s·Δ, 1_A)`. By the quadratic-form inequality, `|Cov_t(s·Δ, 1_A)| ≤ σ_t(s·Δ) · σ_t(1_A) ≤ (|Δ|/√3) · (1/2)`, since `Var(1_A) = P_t(A)(1 − P_t(A)) ≤ 1/4`. (iv) *Integrate.* `|P_{h'}(A) − P_h(A)| ≤ ∫_0^1 |d/dt P_t(A)| dt ≤ β|Δ|/(2√3)` for every `A`, and `TV` is the supremum over `A`. ∎

The identities of (i) and the coefficient ratios of (ii) are executed symbolically (B1–B3); the derivative identity of (iii) on a finite weighted space, the indicator's variance bound and the chain of constants (C1–C2).

## Theorem W2 — the coefficients and the threshold

**Statement.** If two neighbourhood configurations of a site differ only at one neighbour `y`, the conditionals at the site satisfy `TV ≤ c = β/√3`; every row sum of `C_Λ` is at most `α = 2√3 β`; and `α < 1` if and only if `β < √3/6`. At zero field the antipodal change has `TV(P_e, P_{−e}) = tanh(β/2)` exactly, so at that configuration the bound `β/√3` is within the factor `2/√3` of the truth as `β → 0`.

**Proof.** `|h − h'| = |s_y − s'_y| ≤ 2`, so W1 gives `TV ≤ 2β/(2√3) = β/√3`; a site has six neighbours, so the row sum is at most `6β/√3 = 2√3β`; `2√3β < 1 ⇔ β < 1/(2√3) = √3/6`. For the antipodal pair with `h = e`, `h' = −e`: the two densities are `e^{±β t}/Z` in `t = s·e`, `Z = 4π sinh β/β`, and `TV = ∫(p − q)_+ = (2π/Z) ∫_0^1 (e^{βt} − e^{−βt}) dt = (4π(cosh β − 1)/β)/Z = (cosh β − 1)/sinh β = tanh(β/2)`; and `tanh(β/2)/(β/√3) → √3/2`. ∎ (Executed: the threshold arithmetic, `√3/6 > 28/100`, the antipodal value and the limit; C2–C3.)

## Theorem W3 — the finite-window comparison bound by coupling (re-proved for the sphere)

**Statement.** Let `Λ` be a finite window with `n` sites, `ω, ω'` two exterior assignments, `μ = μ_Λ^ω`, `μ' = μ_Λ^{ω'}`, and suppose every row sum of `C_Λ` is at most `α_Λ < 1`. Then for every bounded measurable `f` on `(S²)^Λ`, `|μ(f) − μ'(f)| ≤ Σ_x δ_x(f) (D_Λ b)_x`, with `D_Λ = Σ_{k ≥ 0} C_Λ^k = (I − C_Λ)^{−1}` entrywise nonnegative.

**Proof.** *Step 0 (the maximal coupling of two densities).* For probability densities `p, q` on `S²` with respect to `dσ`, let `m = ∫ min(p, q) dσ`; then `∫(p − q)_+ dσ = ∫(q − p)_+ dσ = 1 − m = TV(p, q)`. Draw `(S, S')` as follows: with probability `m` draw `S` from `min(p, q)/m` and set `S' = S`; otherwise draw `S` from `(p − min(p, q))/(1 − m)` and, independently, `S'` from `(q − min(p, q))/(1 − m)`. The marginals are `p` and `q`, and on the second branch the two densities have disjoint supports, so `P(S ≠ S') = 1 − m = TV(p, q)`. (Executed on a finite weighted space, D1.) *Step 1 (one site).* For records `ζ, ζ'` on `Λ` and the exteriors `ω, ω'`, the conditionals at `x` are `P_{h_x(ζ, ω)}` and `P_{h_x(ζ', ω')}`, and W1 gives `TV ≤ (β/(2√3)) Σ_{y ~ x} |ζ_y − ζ'_y| ≤ Σ_{y ∈ Λ, y ~ x} c 1[ζ_y ≠ ζ'_y] + b_x = (C_Λ 1[ζ ≠ ζ'])_x + b_x`. *Step 2 (the coupled random-scan chain).* Run two copies of the random-scan update (a uniform site `X`, its record redrawn from the conditional), with the same `X` and the maximal coupling of the two conditionals at each step. With `u^t_x = P(η^t_x ≠ η'^t_x)`: `u^{t+1}_x = (1 − 1/n) u^t_x + (1/n) E[TV(P_{h_x(η^t, ω)}, P_{h_x(η'^t, ω')})] ≤ (1 − 1/n) u^t_x + (1/n)((C_Λ u^t)_x + b_x) =: Φ(u^t)_x`, and `Φ` is affine with nonnegative coefficients, hence monotone, so `u^t ≤ Φ^t(u^0) ≤ Φ^t(1)`. *Step 3 (the fixed point).* The linear part of `Φ` has row sums at most `1 − (1 − α_Λ)/n < 1`, so `Φ` is a contraction in the maximum norm; its unique fixed point is `u* = D_Λ b`, since `‖C_Λ‖_∞ ≤ α_Λ < 1` makes `Σ_k C_Λ^k` a finite sum in norm, equal to `(I − C_Λ)^{−1}` and entrywise nonnegative; and `Φ^t(1) → u*`. (Executed on the cube window, D2.) *Step 4 (stationarity).* The conditional of `μ_Λ^ω` at `x` given the other records is `P_{h_x}` (read off the density), so resampling `x` from it leaves `μ` fixed; likewise `μ'`. *Step 5 (the bound at time `t`).* Start the coupled chain from independent draws of `μ` and `μ'`; by Step 4, `η^t ∼ μ` and `η'^t ∼ μ'` for every `t`. Ordering the sites and telescoping through configurations that agree with `η'^t` on the first `i` sites and with `η^t` elsewhere, `|f(η^t) − f(η'^t)| ≤ Σ_x δ_x(f) 1[η^t_x ≠ η'^t_x]`, so `|μ(f) − μ'(f)| = |E[f(η^t) − f(η'^t)]| ≤ Σ_x δ_x(f) u^t_x ≤ Σ_x δ_x(f) Φ^t(1)_x` for every `t`; letting `t → ∞` gives the statement. No limit coupling is needed. ∎

*Walk bound (executed, D3).* `(C_Λ^k)_{xy} = c^k · #{nearest-neighbour walks of length k from x to y inside Λ}`, so `Σ_y (C_Λ^k)_{xy} ≤ (6c)^k = α^k` and `(C_Λ^k)_{xy} = 0` for `k < |x − y|₁`; hence `Σ_{k} (C_Λ^k)_{xy} ≤ α^{|x−y|₁}/(1 − α)` when `α < 1`.

## Theorem W4 — one law for `β < √3/6`

**Statement.** For `β < √3/6`: (a) for every continuous local `f` (depending on `Δ_ℓ`) and any exterior records `b, b'`, `|μ_{Λ_L}^b(f) − μ_{Λ_L}^{b'}(f)| ≤ ‖f‖_δ α^{L−ℓ+1}/(1 − α)`, `Λ_L = {|x|_∞ ≤ L}`; (b) `μ(f) := lim_{L→∞} μ_{Λ_L}^{b_L}(f)` exists for every continuous local `f` and every choice of exterior records `b_L`, and does not depend on the choice; (c) `μ` extends to a probability measure on `(S²)^{Z³}` that is an infinite-volume static law; (d) it is the only one; (e) it is invariant under every simultaneous rotation of all records, so `⟨s_0⟩_μ = 0`.

**Proof.** (a) On `Λ_L` every row sum of `C_Λ` is at most `α < 1`, and `b_y ≤ 6c 1[y ∈ ∂_in Λ_L] = α 1[y ∈ ∂_in Λ_L]`; by W3 and the walk bound, `|μ_{Λ_L}^b(f) − μ_{Λ_L}^{b'}(f)| ≤ Σ_{x ∈ Δ_ℓ} δ_x(f) Σ_k Σ_{y ∈ ∂_in Λ_L} (C_Λ^k)_{xy} α ≤ ‖f‖_δ α Σ_{k ≥ L−ℓ} α^k`, since a walk from `Δ_ℓ` to `∂_in Λ_L` has length at least `L − ℓ`. (b) For `L' > L`, conditioning `μ_{Λ_{L'}}^{b'}` on the records outside `Λ_L` gives `μ_{Λ_L}^{ζ}` with `ζ` those records (read off the density), so `μ_{Λ_{L'}}^{b'}(f) = ∫ μ_{Λ_L}^{ζ}(f) μ_{Λ_{L'}}^{b'}(dζ)` and, by (a), `|μ_{Λ_{L'}}^{b'}(f) − μ_{Λ_L}^{b}(f)| ≤ ‖f‖_δ α^{L−ℓ+1}/(1 − α)`. The differences tend to zero uniformly in the later index and in the exterior records, so the limit exists and is the same for every choice. (c) The limits form a positive normalized linear functional on continuous functions of each compact box product; the representation theorem for such functionals gives a Borel probability law. Thus the limits define, for each box `Δ_ℓ`, a probability law on `(S²)^{Δ_ℓ}` (limits of laws applied to continuous functions of the box's records; the consistency between boxes holds in the limit); the extension theorem for consistent finite-dimensional laws (named under Imports) gives `μ`. `μ` is an infinite-volume static law: for a finite window `Λ` and continuous local `f`, `μ(f) = lim μ_{Λ_{L'}}^b(f) = lim ∫ μ_Λ^{ζ}(f) μ_{Λ_{L'}}^b(dζ) = ∫ μ_Λ^{ζ}(f) μ(dζ)`, because `ζ ↦ μ_Λ^ζ(f)` is a continuous local function. The preceding DLR identity is first obtained on continuous local test functions. Both sides define probability measures; equality on continuous functions on each compact finite product implies equality of their Borel laws, and a monotone-class extension gives the DLR identity for bounded measurable functions. (d) If `ν` is an infinite-volume static law, then `ν(f) = ∫ μ_{Λ_L}^{ζ}(f) ν(dζ)` and by (a) `|ν(f) − μ_{Λ_L}^b(f)| ≤ ‖f‖_δ α^{L−ℓ+1}/(1 − α) → 0`, so `ν = μ` on continuous local functions; these determine each finite-dimensional Borel law on the compact sphere product, hence the cylinder probabilities, hence the whole measure. (e) A simultaneous rotation `R` of all records maps `μ_Λ^ω` to `μ_Λ^{Rω}` (the overlap and `dσ` are invariant), so the image of `μ` under `R` is again an infinite-volume static law and equals `μ` by (d); hence `⟨s_0⟩_μ = R⟨s_0⟩_μ` for all `R`, i.e. `⟨s_0⟩_μ = 0`. ∎

## Theorem W5 — exponential decay

**Statement.** For `β < √3/6` and `x ≠ 0`: (a) in the law `μ` of W4, `|⟨s_0·s_x⟩| ≤ α^{|x|₁}/(1 − α)`; (b) on the torus `(Z/2LZ)³` for every `L ≥ 2`, `|⟨s_0·s_x⟩_L| ≤ α^{d_T(0,x)}/(1 − α)`; hence (c) `M_N² ≤ ((1+α)/(1−α))³/((1−α)N)` and (d) `⟨|ŝ(k)|²⟩ ≤ ((1+α)/(1−α))³/(1 − α)` for every `k`, uniformly in `L`.

**Proof.** (a) Take `Λ = Λ_L ∋ 0, x` with exterior `b`, and bounded `f = f(s_0)`, `g = g(s_x)`. Conditioning `μ_Λ^b` on `s_x = a` gives the law on `Λ ∖ {x}` with exterior records `(b, a)` (read off the density), so `μ_Λ^b(f g) = ∫ μ_Λ^b(da) g(a) μ_Λ^b(f | a)`. W3 on the window `Λ ∖ {x}` with the exteriors `(b, a)` and `(b, a')`, which differ only at `x`, has `b^{diff}_z = c 1[z ~ x]`, so `|μ_Λ^b(f | a) − μ_Λ^b(f | a')| ≤ δ_0(f) c Σ_{z ~ x} Σ_k (C^k)_{0z} ≤ δ_0(f) c Σ_{k ≥ |x|₁ − 1} α^k = δ_0(f) α^{|x|₁}/(6(1 − α))`, since a walk from `0` to a neighbour of `x` has length at least `|x|₁ − 1` and `c = α/6`. Then `Cov_Λ(f, g) = ∫ μ_Λ^b(da) g(a) [μ_Λ^b(f | a) − μ_Λ^b(f)]` and `|μ_Λ^b(f | a) − μ_Λ^b(f)| ≤ sup_{a'} |μ_Λ^b(f | a) − μ_Λ^b(f | a')|`, so `|Cov_Λ(f, g)| ≤ ‖g‖_∞ δ_0(f) α^{|x|₁}/(6(1 − α))`. With `f = s_0·e_i` (`δ_0 = 2`) and `g = s_x·e_i` (`‖g‖_∞ ≤ 1`), summing over `i = 1, 2, 3`: `|Σ_i Cov_Λ(s_0·e_i, s_x·e_i)| ≤ α^{|x|₁}/(1 − α)`. Let `L → ∞`: each expectation is of a local function, so the covariances tend to those of `μ`, and by W4(e) `⟨s_0·s_x⟩_μ = Σ_i Cov_μ(s_0·e_i, s_x·e_i)`. (b) On the torus, conditioning on `s_x = a` gives the law on the window `T ∖ {x}` with exterior `a`; the torus graph minus a site has row sums at most `α`, and a walk from `0` to a neighbour of `x` has length at least `d_T(0, x) − 1`; the same computation gives the bound, and the torus law is rotation-invariant (its density and `dσ` are), so `⟨s_0⟩_L = 0`. (c) By translation invariance `M_N² = N^{−1} Σ_x ⟨s_0·s_x⟩_L ≤ N^{−1} (1 − α)^{−1} Σ_x α^{d_T(0,x)}`, and `Σ_{x ∈ T} α^{d_T(0,x)} = Π_{i=1}^3 (1 + 2Σ_{j=1}^{L−1} α^j + α^L) ≤ ((1 + α)/(1 − α))³`. (d) `⟨|ŝ(k)|²⟩ = Σ_x e^{ik·x} ⟨s_0·s_x⟩_L`, so `|⟨|ŝ(k)|²⟩| ≤ Σ_x |⟨s_0·s_x⟩_L| ≤ (1 − α)^{−1} ((1 + α)/(1 − α))³`. ∎

The geometric identities and the torus sum are executed (D4); the frozen-site conditional on a small window (D5).

## No-Go Discipline Gate

Broad negative certification is withheld. The original five-route tables listed proof obligations and changes of scope rather than five independent attacks on the exact exclusion. They do not establish a negative certificate. Full original arguments remain available in the archive and original branches are retained. W6 and the comparison with a strong-coupling gravity channel are withdrawn. W1–W5 remain mathematical comparison, construction and quantitative bounds for the supplied specification.

## Falsifiers
- A covariance identity of W1(i) that fails, or a coefficient ratio other than `6/(n(2n−1))` or `3/(2n+1)` for some `n ≤ 12`, or a closed-form coefficient that differs from the series (B1–B3).
- A failure of the derivative identity on the finite weighted space, of `p(1 − p) ≤ 1/4`, of the chain of constants, of `√3/6 > 28/100`, of the antipodal value `tanh(β/2)` or of the limit `√3/2` (C1–C3).
- A maximal coupling with disagreement probability other than `TV` (D1); a fixed point other than `D_Λ b`, or `D_Λ` with a negative entry, on the cube window (D2); a walk bound violated on the `7³` box (D3); a geometric identity or the torus sum bound that fails (D4); a frozen-site conditional that is not the window law with that exterior (D5).

## Boundaries and non-claims

For a supplied uniform-sphere exponential nearest-neighbour static specification on Z^3: W1 bounds the one-site total-variation response, W2 gives alpha=2sqrt(3)beta, W3 proves finite-window comparison, W4 constructs the unique rotation-invariant DLR law when alpha<1, and W5 bounds correlations, torus magnetization and structure factors. Torus results require L>=2. No strong-coupling comparison or physical kernel classification is retained. This note does not select a physical reading, coupling, rule or dimension and adopts no clause.

No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The standard mathematical imports are stated explicitly; they supply mathematical tools, not physical selection.

## Imports
- Re-proved at scope: W1 (the covariance eigenvalues and the series inequalities; the derivative identity; the quadratic-form inequality), W2, W3 (the maximal coupling of densities; the coupled chain; the fixed point; the time-`t` bound), W4 (the walk bound; the consistency of finite-window laws), W5.
- Additional explicit measure-theoretic imports: representation of a positive normalized linear functional on continuous functions of a compact metric space by a Borel probability measure; determination of that measure by continuous functions; monotone-class extension from cylinder tests.
- Named standard imports at definition level (never as authority for physics): the extension theorem for consistent finite-dimensional laws on a countable product of compact spaces (Kolmogorov); the uniqueness of a probability measure given on a generating π-system; the exponential series of `sinh` and `cosh`.
- Reference only (named, not used): Dobrushin (1968); Dobrushin–Shlosman (1985); Föllmer (1982); Künsch (1982).


## Review record

[Original recovery manifest](work_history/review_loop/pr8154/original-manifest.json) and [recovery instructions](work_history/review_loop/pr8154/README.md) preserve the complete original versions. The canonical execution address is [runner cache](../logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.txt); execution evidence must match the current source and declared inputs; historical caches are not restamped.

The original branch, full note, runner, cache, historical programs and outputs are preserved byte-exact in the recovery archive. Historical controls are evidence of their recorded finite domains, not a new execution or a proof of an infinite-lattice statement. The canonical primary retains its original twenty finite checks and thirteen mutation definitions; the historical mutation census is not a new review.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py --mutation claim_channel_below_threshold_injected
```

Families: A authority and inputs; B the covariance identities and the series inequalities; C the derivative identity, the constants, the antipodal value; D the maximal coupling, the fixed point, the walk bounds, the geometric sums, the frozen-site conditional; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. The historical mutation census assigned each of the 13 declared mutations to one family; no new mutation census is claimed. Expected final line: `TOTAL: PASS=20 FAIL=0`.
