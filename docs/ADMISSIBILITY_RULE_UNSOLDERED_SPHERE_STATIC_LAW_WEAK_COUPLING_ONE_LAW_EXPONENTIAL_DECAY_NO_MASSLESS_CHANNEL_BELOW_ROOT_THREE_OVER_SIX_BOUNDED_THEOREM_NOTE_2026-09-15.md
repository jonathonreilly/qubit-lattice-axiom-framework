---
claim_id: admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_below_root_three_over_six_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the static law of the exponential zonal rule on the pure-state sphere under the unsoldered reading on Z^3 — one-site conditional P_h(ds) proportional to exp(beta s.h) dsigma(s) with h the sum of the six neighbouring records, finite windows with exterior records, and the torus law of block 19 — with L(x) = coth x - 1/x and alpha = 2 sqrt(3) beta: (W1) TV(P_h, P_h') <= (beta/(2 sqrt 3)) |h - h'| for all h, h', because d/dt P_{h_t}(A) = beta Cov(s.Delta, 1_A), |Cov(X, 1_A)| <= sigma_X/2, and the covariance of s under P_h has eigenvalues L'(x) and L(x)/x (x = beta|h|), both at most 1/3 by series with nonnegative coefficients (proved; the identities and the coefficient ratios 6/(n(2n-1)) and 3/(2n+1) executed symbolically); (W2) hence each neighbour's coefficient is at most beta/sqrt 3 and every row sum at most alpha, with alpha < 1 iff beta < sqrt(3)/6 (proved; executed); (W3) the finite-window comparison bound by the coupled random-scan chain, |mu_Lambda^omega(f) - mu_Lambda^omega'(f)| <= sum_x delta_x(f) (D_Lambda b)_x with D_Lambda = sum_k C_Lambda^k, re-proved for the sphere with the maximal coupling of densities and a time-t bound (proved; the maximal coupling, the fixed point and the walk bounds executed exactly); (W4) for beta < sqrt(3)/6 the finite-window laws with any exterior records have a common limit on cylinder functions, the specification has exactly one infinite-volume static law, and it is rotation-invariant (proved); (W5) in that law and on every torus |<s_0 . s_x>| <= alpha^{|x|_1}/(1 - alpha) (torus distance on the torus), so M_N^2 <= ((1+alpha)/(1-alpha))^3/((1-alpha) N) and sup_k <|s^(k)|^2> <= ((1+alpha)/(1-alpha))^3/(1-alpha) uniformly in the side: no massless channel (proved; the geometric sums executed); (W6) with block 19 (PR #8153, an evidence address) the gravity node's kernel exists in this reading for beta > 3 sqrt(3) pi/8 and cannot for beta < sqrt(3)/6; the band between is open (a placement corollary). Three standard mathematical imports named at definition level; no coupling, reading or rule is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py
---

# The unsoldered sphere static law at weak coupling: one law, exponential decay, and no massless channel below `β = √3/6` — the Green-function channel is a strong-coupling feature with an explicit window

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Blocks 19 and 20 (PRs #8153, #8154) place the gravity node's kernel in the
transverse channel of the ordered unsoldered static law on `Z³`, and nowhere
on a plane or a line. This note settles the other side of the coupling axis
on `Z³`. Below `β = √3/6` the law is unique, its correlations decay
exponentially, its structure factor is bounded uniformly in the wavevector,
and the long-range-order parameter vanishes. So the kernel is a strong-coupling
feature of this reading: present for `β > 3√3π/8`, absent for `β < √3/6`, and
the band between the two constants is left open.

The mechanism is a one-site contraction, the same route block 03 ran for the
six-axis rule, now for a continuous menu. The rule's one-site conditional is
`P_h ∝ e^{β s·h}` with `h` the sum of the six neighbouring records. Moving one
neighbour moves `h` by at most `2`, and the conditional's total-variation
response to a change of `h` is at most `β|Δh|/(2√3)`: the derivative of
`P_h(A)` along a segment is `β` times a covariance of `s·Δh` with an
indicator, the indicator's standard deviation is at most `1/2`, and the
variance of any component of `s` under any `P_h` is at most `1/3`. That last
fact is the only analysis in the note: the covariance of `s` under `P_h` has
the longitudinal eigenvalue `L'(x)` and the transverse eigenvalue `L(x)/x`,
with `L(x) = coth x − 1/x` and `x = β|h|`, and both are at most `1/3` because
the relevant differences are power series with nonnegative coefficients. So
each of the six neighbours has coefficient at most `β/√3`, the row sum is
`α = 2√3β`, and `α < 1` is `β < √3/6`. The coupled random-scan chain of block
03 then gives the finite-window comparison bound, from which uniqueness,
exponential decay and the bounds on the torus follow.

Exactly: `TV(P_h, P_{h'}) ≤ (β/(2√3))|h − h'|` (W1); `α = 2√3β` (W2);
the comparison bound (W3); one rotation-invariant law for `β < √3/6` (W4);
`|⟨s_0·s_x⟩| ≤ α^{|x|₁}/(1 − α)`, `M_N² ≤ ((1+α)/(1−α))³/((1−α)N)`,
`sup_k ⟨|ŝ(k)|²⟩ ≤ ((1+α)/(1−α))³/(1−α)` (W5); the window
`[√3/6, 3√3π/8]` (W6). Executed with exact arithmetic: 20 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's gravity node (#8093): 'the covariant scalar record statistic whose two-point function on the formation law is the lattice Green function'; blocks 19 and 20 (PRs #8153, #8154) locate it in the transverse channel of the ordered unsoldered static law on Z^3 and show it needs the third dimension; its coupling window on Z^3"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the weak-coupling side is settled: for beta < sqrt(3)/6 the unsoldered static law on Z^3 is unique with exponential decay and a bounded structure factor, so the kernel cannot exist there; the kernel is a strong-coupling feature with the open band [sqrt(3)/6, 3 sqrt(3) pi/8]. Open: the band; the normalization; the Born overlap. Consumers: #8093's assembly (the gravity node's coupling dependence); the campaign's queue"
conditional_surface_status: "W1-W5 proved for every beta < sqrt(3)/6 on finite windows, on tori of even side and in the infinite-volume limit; W6 a placement corollary conditional on block 19 (open PR) for the strong-coupling half; the algebraic skeleton executed exactly (the covariance identities, the coefficient ratios, the derivative identity, the maximal coupling, the fixed point on the cube window, the walk bounds on the 7^3 box, the geometric sums); conditional on the sphere as the possibility domain, the unsoldered and static readings and the exponential overlap as supplied conditions; three standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "Each site has a domain of local possibilities.", "No possibility is privileged.", "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", and "Records form.". The landed possibility-covariance note (`docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`, section "Empty-neighbourhood sphere laws") supplies the pure-state sphere `S²` as the possibility domain and the unsoldered reading. Block 03 (`docs/ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the static reading of finite windows with exterior records, the notion of an infinite-volume static law (the specification), and the coupling route re-proved here for the sphere. All proposed and unaudited; block 19 (PR #8153, open) is referenced under Prior art as the evidence address for the strong-coupling half of W6.

Declared objects.
- **The rule and its windows.** Records `s_x ∈ S²`; `β > 0` supplied; the one-site conditional given the neighbouring records, `P_h(ds) = e^{β s·h} dσ(s)/Z(h)`, `h = Σ_{y ~ x} s_y`, `Z(h) = ∫ e^{β s·h} dσ = 4π sinh(β|h|)/(β|h|)`, `dσ` the uniform surface measure. For a finite window `Λ` with exterior records `ω` on the sites adjacent to `Λ`: `μ_Λ^ω(ds_Λ) ∝ Π_{⟨xy⟩ ⊂ Λ} e^{β s_x·s_y} Π_{x ∈ Λ, y ∉ Λ, y ~ x} e^{β s_x·ω_y} Π_{x ∈ Λ} dσ(s_x)`; its conditional at `x` given the other records is `P_{h_x}` with `h_x` the sum over the six neighbours (interior records or exterior ones). The torus law `μ_L` of block 19 on `(Z/2LZ)³`, `N = (2L)³`, has the same conditionals. An **infinite-volume static law** is a probability measure on `(S²)^{Z³}` whose conditional law on every finite window given the exterior records is `μ_Λ^ω` (block 03's specification reading).
- **The function `L`.** `L(x) = coth x − 1/x` for `x > 0`, `L(0) = 0`; `L'(x) = 1/x² − 1/sinh² x`.
- **Coefficients.** `c := β/√3`; `α := 6c = 2√3 β`. For a window `Λ`: `C_Λ` the matrix with `(C_Λ)_{xy} = c` when `x, y ∈ Λ` are neighbours and `0` otherwise; `D_Λ = Σ_{k ≥ 0} C_Λ^k`; for exterior records `ω, ω'`, `b_x = c · #{y ∉ Λ : y ~ x, ω_y ≠ ω'_y}`.
- **Oscillations.** For `f` on `(S²)^Λ`, `δ_x(f) = sup{|f(ζ) − f(ζ')| : ζ, ζ' differ only at x}`; `‖f‖_δ = Σ_x δ_x(f)`. A local function depends on the records in a box `Δ_ℓ = {|x|₁ ≤ ℓ}`.
- **Transforms and order parameter** on the torus: `ŝ(k) = N^{−1/2} Σ_x e^{ik·x} s_x`; `M_N² = N^{−2}⟨|Σ_x s_x|²⟩`; `d_T(0, x)` the torus `ℓ¹` distance.

## Prior art and what is new

The one-site contraction criterion for uniqueness is Dobrushin's (1968), with exponential decay of correlations under it (Dobrushin–Shlosman; Föllmer; Künsch); for the classical three-component model it is textbook. None is used as authority; W1–W5 are re-proved at scope. On `main`, block 03 re-proves the criterion by the coupled random-scan chain for the six-axis rule (finite menu) and states the region in the rule's weights; block 02 gives existence by compactness for the finite menu. What is new here: (i) the explicit constant `√3/6` for the sphere rule from an exact bound on the covariance of a record under any field (`L'(x) ≤ 1/3`, `L(x)/x ≤ 1/3`, proved by series); (ii) block 03's coupling route re-proved for a continuous menu, with the maximal coupling of densities and a time-`t` bound in place of the limit coupling, and existence obtained from the comparison bound and the consistency of the finite-window laws rather than imported; (iii) the decay and structure-factor bounds on the torus by freezing one site; (iv) the placement: the Green-function channel of block 19 is a strong-coupling feature with an explicit open band.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| W1 | `TV(P_h, P_{h'}) ≤ (β/(2√3))|h − h'|` | the derivative identity; the indicator's variance; the covariance eigenvalues `L'`, `L/x ≤ 1/3` | B, C |
| W2 | `c_{xy} ≤ β/√3`; `α = 2√3β`; `α < 1 ⇔ β < √3/6` | `|Δh| ≤ 2` | C |
| W3 | the finite-window comparison bound | the coupled random-scan chain; the maximal coupling of densities; the fixed point `D_Λ b` | D |
| W4 | one rotation-invariant infinite-volume static law for `β < √3/6` | W3 with the walk bound and the consistency of the finite-window laws | D |
| W5 | `|⟨s_0·s_x⟩| ≤ α^{|x|₁}/(1−α)`; the torus bounds | W3 with one site frozen; the geometric sums | D |
| W6 | the window `[√3/6, 3√3π/8]` | W5 with block 19 | — |

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

**Statement.** For `β < √3/6`: (a) for every local `f` (depending on `Δ_ℓ`) and any exterior records `b, b'`, `|μ_{Λ_L}^b(f) − μ_{Λ_L}^{b'}(f)| ≤ ‖f‖_δ α^{L−ℓ+1}/(1 − α)`, `Λ_L = {|x|_∞ ≤ L}`; (b) `μ(f) := lim_{L→∞} μ_{Λ_L}^{b_L}(f)` exists for every local `f` and every choice of exterior records `b_L`, and does not depend on the choice; (c) `μ` extends to a probability measure on `(S²)^{Z³}` that is an infinite-volume static law; (d) it is the only one; (e) it is invariant under every simultaneous rotation of all records, so `⟨s_0⟩_μ = 0`.

**Proof.** (a) On `Λ_L` every row sum of `C_Λ` is at most `α < 1`, and `b_y ≤ 6c 1[y ∈ ∂_in Λ_L] = α 1[y ∈ ∂_in Λ_L]`; by W3 and the walk bound, `|μ_{Λ_L}^b(f) − μ_{Λ_L}^{b'}(f)| ≤ Σ_{x ∈ Δ_ℓ} δ_x(f) Σ_k Σ_{y ∈ ∂_in Λ_L} (C_Λ^k)_{xy} α ≤ ‖f‖_δ α Σ_{k ≥ L−ℓ} α^k`, since a walk from `Δ_ℓ` to `∂_in Λ_L` has length at least `L − ℓ`. (b) For `L' > L`, conditioning `μ_{Λ_{L'}}^{b'}` on the records outside `Λ_L` gives `μ_{Λ_L}^{ζ}` with `ζ` those records (read off the density), so `μ_{Λ_{L'}}^{b'}(f) = ∫ μ_{Λ_L}^{ζ}(f) μ_{Λ_{L'}}^{b'}(dζ)` and, by (a), `|μ_{Λ_{L'}}^{b'}(f) − μ_{Λ_L}^{b}(f)| ≤ ‖f‖_δ α^{L−ℓ+1}/(1 − α)`. The differences tend to zero uniformly in the later index and in the exterior records, so the limit exists and is the same for every choice. (c) The limits define, for each box `Δ_ℓ`, a probability law on `(S²)^{Δ_ℓ}` (limits of laws applied to continuous functions of the box's records; the consistency between boxes holds in the limit); the extension theorem for consistent finite-dimensional laws (named under Imports) gives `μ`. `μ` is an infinite-volume static law: for a finite window `Λ` and local `f`, `μ(f) = lim μ_{Λ_{L'}}^b(f) = lim ∫ μ_Λ^{ζ}(f) μ_{Λ_{L'}}^b(dζ) = ∫ μ_Λ^{ζ}(f) μ(dζ)`, because `ζ ↦ μ_Λ^ζ(f)` is a continuous local function. (d) If `ν` is an infinite-volume static law, then `ν(f) = ∫ μ_{Λ_L}^{ζ}(f) ν(dζ)` and by (a) `|ν(f) − μ_{Λ_L}^b(f)| ≤ ‖f‖_δ α^{L−ℓ+1}/(1 − α) → 0`, so `ν = μ` on local functions, hence on the cylinder algebra, hence everywhere (two probability measures agreeing on a generating π-system coincide). (e) A simultaneous rotation `R` of all records maps `μ_Λ^ω` to `μ_Λ^{Rω}` (the overlap and `dσ` are invariant), so the image of `μ` under `R` is again an infinite-volume static law and equals `μ` by (d); hence `⟨s_0⟩_μ = R⟨s_0⟩_μ` for all `R`, i.e. `⟨s_0⟩_μ = 0`. ∎

## Theorem W5 — exponential decay; no massless channel

**Statement.** For `β < √3/6` and `x ≠ 0`: (a) in the law `μ` of W4, `|⟨s_0·s_x⟩| ≤ α^{|x|₁}/(1 − α)`; (b) on the torus `(Z/2LZ)³` for every `L ≥ 1`, `|⟨s_0·s_x⟩_L| ≤ α^{d_T(0,x)}/(1 − α)`; hence (c) `M_N² ≤ ((1+α)/(1−α))³/((1−α)N)` and (d) `⟨|ŝ(k)|²⟩ ≤ ((1+α)/(1−α))³/(1 − α)` for every `k`, uniformly in `L`.

**Proof.** (a) Take `Λ = Λ_L ∋ 0, x` with exterior `b`, and bounded `f = f(s_0)`, `g = g(s_x)`. Conditioning `μ_Λ^b` on `s_x = a` gives the law on `Λ ∖ {x}` with exterior records `(b, a)` (read off the density), so `μ_Λ^b(f g) = ∫ μ_Λ^b(da) g(a) μ_Λ^b(f | a)`. W3 on the window `Λ ∖ {x}` with the exteriors `(b, a)` and `(b, a')`, which differ only at `x`, has `b^{diff}_z = c 1[z ~ x]`, so `|μ_Λ^b(f | a) − μ_Λ^b(f | a')| ≤ δ_0(f) c Σ_{z ~ x} Σ_k (C^k)_{0z} ≤ δ_0(f) c Σ_{k ≥ |x|₁ − 1} α^k = δ_0(f) α^{|x|₁}/(6(1 − α))`, since a walk from `0` to a neighbour of `x` has length at least `|x|₁ − 1` and `c = α/6`. Then `Cov_Λ(f, g) = ∫ μ_Λ^b(da) g(a) [μ_Λ^b(f | a) − μ_Λ^b(f)]` and `|μ_Λ^b(f | a) − μ_Λ^b(f)| ≤ sup_{a'} |μ_Λ^b(f | a) − μ_Λ^b(f | a')|`, so `|Cov_Λ(f, g)| ≤ ‖g‖_∞ δ_0(f) α^{|x|₁}/(6(1 − α))`. With `f = s_0·e_i` (`δ_0 = 2`) and `g = s_x·e_i` (`‖g‖_∞ ≤ 1`), summing over `i = 1, 2, 3`: `|Σ_i Cov_Λ(s_0·e_i, s_x·e_i)| ≤ α^{|x|₁}/(1 − α)`. Let `L → ∞`: each expectation is of a local function, so the covariances tend to those of `μ`, and by W4(e) `⟨s_0·s_x⟩_μ = Σ_i Cov_μ(s_0·e_i, s_x·e_i)`. (b) On the torus, conditioning on `s_x = a` gives the law on the window `T ∖ {x}` with exterior `a`; the torus graph minus a site has row sums at most `α`, and a walk from `0` to a neighbour of `x` has length at least `d_T(0, x) − 1`; the same computation gives the bound, and the torus law is rotation-invariant (its density and `dσ` are), so `⟨s_0⟩_L = 0`. (c) By translation invariance `M_N² = N^{−1} Σ_x ⟨s_0·s_x⟩_L ≤ N^{−1} (1 − α)^{−1} Σ_x α^{d_T(0,x)}`, and `Σ_{x ∈ T} α^{d_T(0,x)} = Π_{i=1}^3 (1 + 2Σ_{j=1}^{L−1} α^j + α^L) ≤ ((1 + α)/(1 − α))³`. (d) `⟨|ŝ(k)|²⟩ = Σ_x e^{ik·x} ⟨s_0·s_x⟩_L`, so `|⟨|ŝ(k)|²⟩| ≤ Σ_x |⟨s_0·s_x⟩_L| ≤ (1 − α)^{−1} ((1 + α)/(1 − α))³`. ∎

The geometric identities and the torus sum are executed (D4); the frozen-site conditional on a small window (D5).

## Corollary W6 — the coupling window of the Green-function channel

**Statement (conditional on block 19 for the strong-coupling half).** Under the unsoldered static reading with the exponential overlap on `Z³`: for `β > 3√3π/8` the transverse structure factor is sandwiched between multiples of `1/(βE(k))` with a positive lower constant (block 19's G5), and for `β < √3/6` the structure factor is bounded uniformly in `k` and `L` while `M_N² → 0` (W5). So the gravity node's kernel is a strong-coupling feature of this reading, and nothing is claimed for `√3/6 ≤ β ≤ 3√3π/8`.

**Proof.** The two halves are W5(c)–(d) and block 19's G3–G5; the latter is an open PR cited as an evidence address, not as authority. ∎

## No-Go Discipline Gate

The negative sentence is W5(d) with W6: no massless channel for `β < √3/6`. Escapes named, not closed: the band `[√3/6, 3√3π/8]`; other overlaps (the Born overlap is not treated); the formation reading (block 13).

### N1 — Routes by which the negative could fail
1. *The covariance bound `1/3` fails at some field* — closed: the eigenvalues are `L'(x)` and `L(x)/x`, both at most `1/3` by series with nonnegative coefficients (B2–B3 executed to `n = 12` and in closed form).
2. *The derivative identity or the indicator bound* — closed: executed on a finite weighted space (C1); `p(1 − p) ≤ 1/4`.
3. *The coupling argument needs a finite menu* — closed: the maximal coupling of densities and the time-`t` bound replace the finite-menu steps of block 03 (D1–D2).
4. *The walk bound or the geometric sums* — closed: executed exactly on the `7³` box and symbolically (D3–D4).
5. *The torus has no exterior* — closed: one site is frozen and becomes the exterior (D5).
6. *The band, other overlaps, the formation reading* — escapes, named above.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, the parent note's sphere law and reading, block 03's static reading and specification, and the supplied overlap.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the five sentences under Premises | yes (premise) |
| the possibility-covariance note (`main`) | the sphere domain and the unsoldered reading | yes (premise, proposed) |
| block 03 (`main`) | the static reading, the specification, the coupling route (re-proved here) | yes (premise, proposed) |
| block 19 (PR #8153) | the strong-coupling half of W6 | W6 only (evidence address) |
| block 20 (PR #8154) | context (the dimension placement) | no |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no massless channel below `√3/6`" | executed: the covariance identities and the coefficient ratios; the derivative identity; the antipodal value; the threshold arithmetic | executed: the maximal coupling on a finite weighted space; the frozen-site conditional on a small window | executed: the walk bounds `(C^k)_{0x} = 0` for `k < |x|₁` and `Σ_y (C^k)_{0y} ≤ α^k` on the `7³` box | executed: the fixed point `u* = D b` on the cube window; the geometric sums and the torus sum | proved for every `β < √3/6` on finite windows, tori and the infinite-volume law (W1–W5); the band not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or overlap; none is a wall.

### N7 — Steelman
Hostile reviewer: "The one-site contraction criterion for the classical three-component model is in every textbook, and `√3/6` is far below the true threshold." Reply: the framework question is the coupling window of the gravity node's kernel under the reading that supplies it, which needed an explicit constant proved at scope from the rule's own one-site conditional; the constant is not sharp and is not claimed to be — the zero-field antipodal value shows the coefficient's slack there is a factor `2/√3`, and the band is stated as open. Conceded: the band is wide; the sharper coefficient (the supremum over fields of a mean absolute deviation) is not proved.

### N8 — Cross-cycle echo
Block 03's contraction region for the six-axis rule is the same criterion with a finite menu; block 08's causal coupling region is its formation-law counterpart; block 19's ordered phase is the other end of this note's axis; block 20's dimension placement is the other axis of the same kernel.

## Falsifiers
- A covariance identity of W1(i) that fails, or a coefficient ratio other than `6/(n(2n−1))` or `3/(2n+1)` for some `n ≤ 12`, or a closed-form coefficient that differs from the series (B1–B3).
- A failure of the derivative identity on the finite weighted space, of `p(1 − p) ≤ 1/4`, of the chain of constants, of `√3/6 > 28/100`, of the antipodal value `tanh(β/2)` or of the limit `√3/2` (C1–C3).
- A maximal coupling with disagreement probability other than `TV` (D1); a fixed point other than `D_Λ b`, or `D_Λ` with a negative entry, on the cube window (D2); a walk bound violated on the `7³` box (D3); a geometric identity or the torus sum bound that fails (D4); a frozen-site conditional that is not the window law with that exterior (D5).

## Boundaries and non-claims
This note proves, for the unsoldered static law with the exponential overlap on `Z³`, that below `β = √3/6` there is exactly one infinite-volume static law, with exponential decay of the record correlations and a structure factor bounded uniformly in the wavevector and the side; it does not locate the true threshold, does not treat the band `[√3/6, 3√3π/8]`, does not treat the Born overlap, does not re-prove the strong-coupling half of the placement (block 19's open PR), does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- The possibility-covariance note and block 03 (both on `main`): the readings, the specification and the coupling route; proposed, unaudited. PR #8153 (open) referenced as the evidence address for W6's strong-coupling half; PR #8154 for context.
- Re-proved at scope: W1 (the covariance eigenvalues and the series inequalities; the derivative identity; the quadratic-form inequality), W2, W3 (the maximal coupling of densities; the coupled chain; the fixed point; the time-`t` bound), W4 (the walk bound; the consistency of finite-window laws), W5.
- Named standard imports at definition level (never as authority for physics): the extension theorem for consistent finite-dimensional laws on a countable product of compact spaces (Kolmogorov); the uniqueness of a probability measure given on a generating π-system; the exponential series of `sinh` and `cosh`.
- Reference only (named, not used): Dobrushin (1968); Dobrushin–Shlosman (1985); Föllmer (1982); Künsch (1982).

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane at each conclusion; no subagents). The controls (`specs/supervisor_control_block21_weak_coupling.py`) first checked a cruder route — `TV ≤ tanh(osc/4)` on random finite instances, giving the threshold `artanh(1/6) = (1/2) log(7/5)` — then found by a numerical sweep over fields that the one-site conditional's response is about half that bound, computed the exact antipodal value `tanh(β/2)`, verified the covariance eigenvalue formulas and the series ratios, and swept the mean absolute deviation (maximal at zero field, `1/2`, unproved); the contract was then written on the variance route, which is exact and uniform and gives `√3/6`; the lens pass is in `GOAL_block21.md`; the primary seat wrote W1–W6 and the runner; the refuting pass (`CHECKER_block21_findings.md`) checked W1 against direct quadrature at random fields including large ones, the eigenvalue bounds on a grid, the decay bound's direction on the exactly solvable open chain (`⟨s_0·s_r⟩ = L(β)^r`, three sites by quadrature), the fixed point on a `3×3×3` box by floating-point linear algebra, and the torus sum. Facts settled while executing: sympy needs the exponential rewrite to verify the hyperbolic identities; the coefficient ratios have closed forms `6/(n(2n−1))` and `3/(2n+1)`.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py --mutation claim_channel_below_threshold_injected
```

Families: A authority and inputs; B the covariance identities and the series inequalities; C the derivative identity, the constants, the antipodal value; D the maximal coupling, the fixed point, the walk bounds, the geometric sums, the frozen-site conditional; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
