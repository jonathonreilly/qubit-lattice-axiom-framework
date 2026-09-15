# GOAL — block 21: the weak-coupling side of the unsoldered sphere static law on `Z³` — one law, exponential decay, no massless channel below `β = √3/6` (2026-09-15)

**Owner directive (2026-09-15):** don't stop; assess the next lane at each conclusion; no subagents; derivations over computation.

**Why this block.** Blocks 19 and 20 (PRs #8153, #8154) show the gravity node's kernel lives in the transverse channel of the ordered unsoldered static law on `Z³`, and nowhere on a plane or line. What happens on `Z³` at weak coupling? This block proves that below an explicit coupling the law is unique with exponentially decaying correlations, its structure factor is bounded uniformly in the wavevector, and the long-range-order parameter vanishes: the kernel is a strong-coupling feature of the reading, with an explicit window `[√3/6, 3√3π/8]` in which nothing is claimed.

**Object.** The one-site conditional of the rule given the six neighbours, `P_h(ds) ∝ e^{β s·h} dσ(s)` with `h = Σ_{y~x} s_y`; finite windows with exterior records; the torus law of block 19; `α := 2√3 β`.

**Contract.**
- W1 (the derivative bound): for `h, h' ∈ R³`, `TV(P_h, P_{h'}) ≤ (β/(2√3))|h − h'|`. Route: `d/dt P_{h_t}(A) = β Cov_{h_t}(s·Δ, 1_A)`, `|Cov(X, 1_A)| ≤ σ_X/2`, and `Var_h(s·Δ) ≤ |Δ|²/3` because the covariance of `s` under `P_h` has eigenvalues `L'(x)` (longitudinal) and `L(x)/x` (transverse, twice), `x = β|h|`, `L(x) = coth x − 1/x`, both at most `1/3` by series with nonnegative coefficients (ratios `6/(n(2n−1))` and `3/(2n+1)`).
- W2 (Dobrushin coefficients): changing one neighbour changes `h` by at most `2`, so `c_{xy} ≤ β/√3` and every row sum is at most `α = 2√3 β`; `α < 1 ⇔ β < √3/6`. Remark: at zero field the antipodal change has `TV = tanh(β/2)` exactly, so the coefficient is within a factor `2/√3` of the worst case there.
- W3 (finite-window comparison by coupling, re-proved for the sphere): block 03's route with the maximal coupling of densities and the time-`t` bound (no limit coupling): `|μ_Λ^ω(f) − μ_Λ^{ω'}(f)| ≤ Σ_x δ_x(f)(D_Λ b)_x`, `D_Λ = Σ_k C_Λ^k`.
- W4 (one law): for `β < √3/6` the finite-window laws with any exterior records have a common limit on cylinder functions, the specification has exactly one Gibbs law, and it is rotation-invariant.
- W5 (exponential decay; no channel): `|⟨s_0·s_x⟩| ≤ α^{|x|₁}/(1 − α)` in the unique law and on every torus (torus distance); hence `M_N² ≤ ((1+α)/(1−α))³/((1−α)N)` and `sup_k ⟨|ŝ(k)|²⟩ ≤ ((1+α)/(1−α))³/(1−α)` uniformly in `L`.
- W6 (the window): the kernel exists for `β > 3√3π/8` (block 19, evidence address) and cannot for `β < √3/6` (W5); the band between is open.
- N-gate for the negative "no channel below `√3/6`": escapes — the band; other overlaps; the formation reading.

**Lens pass (self-run panel).**
- *"Dobrushin uniqueness for the classical three-component model is textbook."* Yes; the content is the explicit constant for this rule from an exact variance bound, the re-proof at scope, and the placement (the kernel's coupling window).
- *"Why the variance route and not the sharper `tanh(β/2)`?"* The sharper coefficient needs the supremum over all fields of the mean absolute deviation, which the control finds at zero field but which is not proved; the variance bound is exact and uniform.
- *"The torus has no boundary; how does the comparison bound give decay there?"* Freeze one site: the torus minus a site is a window whose exterior is that site; the same bound applies.
- *"Existence of the infinite-volume law."* Not imported: the finite-window limits exist by the comparison bound and the consistency of finite-window laws, and define the law on cylinder functions (the extension named at definition level, as in block 03).

**Forbidden phrases (beyond the lane's standing list):** "phase transition", "critical", "converge", "certified", "emergent", "the physical coupling", "the transition point".

**Prior-art search at `origin/main` (07583e5fc2).** Block 03 (the six-axis rule's one-site contraction region by coupling); nothing for the sphere-valued rule; the classical no-order notes are two-dimensional and quantum. Open PRs: #8153, #8154 (this lane).
