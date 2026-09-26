# The formation-response slope needs no electric moment: an independent proof for every normal state

Task `J:derive:deferred-20260925-ground-energy-and-response:a1`, worker `w-macbookpro9927a-jc63a`, model claude-opus-5-5 (owner-requested recovery).

**Files.**
- `check.py`: 5 exact sympy checks, under 1 s.
- `make_status.py` writes `RECOVERY_STATUS.json`: sha256-verified source revisions, the review PRE source, and the review record.

## Sources, corrections and overlap

**The disposition group.** `ground-energy-and-response` in `probes/work/deferred-science-20260925/unit-28.json` (sha256 `f67dca42…`) contains #9199, #9206 and #9208. All three come from the codex mobile-record lane. I chose one precise obligation, #9208's moment-free response. #9199 and #9206 are untouched and listed as obligations.

**#9208 as landed.**
- Landing commit `6b414efff9`. The note is identical on current `origin/main` `78db61c32a`: sha256 `558196a1…`.
- Frozen head `a4cb43ee99`, note sha256 `fb7e6482…`.

The landed response proof uses "a sufficient, deliberately nonminimal" fourth-moment domain, `Tr(M²ρ₀) < ∞` with `M = I + Σ_e E_e²`. The landed text also records that "the independent PRE also gives a stronger moment-free response result by a bounded strong-quotient argument … Those additions remain separately attributed". The review's PRE reconstruction is bundled as `sources/e02c3983…` (`review/science/PRE.md`). This attempt reproduces that result independently and validates its route step by step.

**The supplied model.** From #9208, restated:
- the full Gauss-physical space;
- `h = KD + δH₄`, with the gated electric term `D = Σ_{e=(a,b)} v_b E_e(E_e − q_a)`, where `v_b = 1[q_b = 0]`;
- bounded `H₄` and formation channels `L_μ` at fixed graph;
- the generator `𝓛ρ = −i[h, ρ] + Σ_μ D[L_μ]ρ`;
- Wilson shifts `W_ν|q, E⟩ = |q, E + ν⟩` for integer divergence-free `ν`, with quadratures `X = (W + W*)/2` and `Y = (W − W*)/(2i)`;
- the kick `e^{iθQ_β}` at preparation time `t`, followed by lag `u`, with response `χ_{α←β}(t, u) = d/dθ Tr[Q_α 𝓣_u(e^{iθQ_β}ρ_t e^{−iθQ_β})]` at `θ = 0`.

This sign convention is the PRE's. #9208's impulse `+ηV` reverses the sign, and its (5) is the nonnegative sum.

**Corrections preserved.**
- The response is an initial-lag slope at finite preparation time. No finite-lag kernel, attenuation law, spectrum or microscopic transfer follows.
- The graph is fixed, and nothing here is volume-uniform.
- The kick is a mathematical probe, not an implemented source.

**Provenance.**
- The claim printed no prior attempts on this problem.
- The related task `energy-moments-and-apparatus` was released by me earlier; it is distinct.
- No earlier unit of mine treats this lane.

## 1. Statement attempted

On a fixed finite even cubic torus, take any finite integer divergence-free loop `ν` and write `A_ν = Σ_e v_b ν_e²`. For every normal initial density `ρ₀`, every `t ≥ 0`, and `α, β ∈ {X, Y}`:

`lim_{u↓0} χ_{α←β}(t, u)/u = Tr ρ_t R_{αβ}`,

where:
- `R_XX = KA − (K/2)(W² + W⁻²)A`;
- `R_YY = KA + (K/2)(W² + W⁻²)A`;
- `R_XY = R_YX = (iK/2)(W² − W⁻²)A`.

Hence `R_XX + R_YY = 2KA_ν = F_ν`. On an elementary plaquette, `A_p = 2(v_{b₁} + v_{b₂})` and the sum is `4K⟨v_{b₁} + v_{b₂}⟩_t`.

No electric moment of `ρ₀` is needed. So #9208's (3)–(5) hold without its fourth-moment hypothesis.

The route requires a bounded mixed second difference of the electric energy. For a quartic electric term, the corresponding quotient is unbounded.

## 2. Steps

**S1. The response as a trace. PROVED.** `Q_β` is bounded, so `θ ↦ e^{iθQ_β}ρ e^{−iθQ_β}` is differentiable in trace norm, with derivative `i[Q_β, ρ]`. Hence

`χ = i Tr(Q_α 𝓣_u[Q_β, ρ_t]) = i Tr ρ_t[𝓣*_u Q_α, Q_β]`,

and `χ(t, 0) = 0` because `[X, Y] = 0`.

**S2. What commutes with `W`. PROVED (structural).**
- `W_ν` is field-only and preserves Gauss's law, so it commutes with every matter operator, every vacancy gate, every rotor shift and the Gauss projector.
- Hence `[H₄, Q] = 0` and `[L_μ, Q] = [L_μ*, Q] = 0`, so the bounded part `𝓥A = iδ[H₄, A] + Σ_μ(L_μ*AL_μ − ½{L_μ*L_μ, A})` gives `𝓥Q = 0`.

**S3. The exact commutator for the electric part. PROVED; CHECKED D1, D2, C1.**

*The mixed difference.* Let `𝓤_u(A) = e^{iuKD}Ae^{−iuKD}` and `f_ε(q, E) = D(q, E + εν) − D(q, E)`. Then `𝓤_u(W^ε) = W^ε e^{iuKf_ε}`. Per edge, the mixed second difference of `v E(E − q)` is `2ετ v n²` exactly, with no `E` and no `q` (D1). So `f_ε(q, E + τν) − f_ε(q, E) = 2ετA_ν`.

*The commutator.* Therefore

`[𝓤_u(W^ε), W^τ] = W^{ε+τ} e^{iuKf_ε}(e^{2iuKετA_ν} − I)`,

checked exactly on a single-edge rotor for all four sign pairs (C1). Its norm is at most `2K|u|·‖A_ν‖`, using `|e^{ix} − 1| ≤ |x|`, and `‖A_ν‖ ≤ Σ_e ν_e²`. On a plaquette, `A_p = 2(v_{b₁} + v_{b₂}) ≤ 4` (D2).

**S4. The strong limit for the electric part. PROVED; CHECKED L1.**
- On each basis vector, `e^{iuKf_ε} → 1` and `(e^{2iuKετA} − 1)/u → 2iKετA`, with norms bounded uniformly in `u`. So `(1/u)[𝓤_u(W^ε), W^τ] → 2iKετ W^{ε+τ}A` strongly. The span of basis vectors is dense, and the family is uniformly bounded.
- Forming the quadratures gives `(i/u)[𝓤_u(Q_α), Q_β] → R_{αβ}`, with the entries of §1 (L1).

**S5. The bounded remainder. PROVED.**

*Duhamel.* `𝓣*_u` is the Dyson perturbation of the unitary group `𝓤_u` by the bounded map `𝓥`, with `‖𝓥‖ ≤ M = 2δ‖H₄‖ + 2Σ_μ‖L_μ‖²`. So in the strong operator topology

`𝓣*_uQ − 𝓤_uQ = ∫₀^u 𝓤_{u−r}(𝓥 𝓣*_r Q) dr`.

The integrand is strongly continuous in `r` on bounded sets, and `𝓣*_r` is unital and contractive.

*Limits.*
- The left side has norm at most `uM`. Since `𝓤_rQ → Q` strongly, it follows that `𝓣*_rQ → Q` strongly.
- `𝓥` is a finite sum of left and right multiplications by bounded operators, so `Z_r := 𝓥𝓣*_rQ → 𝓥Q = 0` strongly.
- For fixed `ψ`: `‖𝓤_{u−r}(Z_r)ψ‖ ≤ ‖Z_rψ‖ + M‖(e^{−i(u−r)KD} − 1)ψ‖`, which tends to 0 uniformly for `r ∈ [0, u]` as `u ↓ 0`.
- Hence `Y_u := (𝓣*_uQ − 𝓤_uQ)/u` satisfies `‖Y_u‖ ≤ M` and `Y_u → 0` strongly. So `[Y_u, Q_β] → 0` strongly.

**S6. Conclusion. PROVED.**
- Combining S4 and S5: `(i/u)[𝓣*_uQ_α, Q_β] → R_{αβ}` strongly, with norm at most `2K‖A_ν‖ + 2M`.
- A uniformly bounded, strongly convergent family pairs with every trace-class `ρ_t`: expand `ρ_t = Σ_i λ_i|φ_i⟩⟨ψ_i|` and use dominated convergence.
- This gives §1 for every normal `ρ_t`. Every `ρ_t = 𝓣_tρ₀` is normal, so no electric moment of `ρ₀` enters. The proof never differentiates `Tr ρD`.

**S7. Sharpness of the route. CHECKED S1.**
- For a quartic electric term `E⁴`, the mixed second difference is `−(12E² + 2)`, which is unbounded. It changes in steps of `24E + 12`.
- For small `u > 0`, the phases `uK(12E² + 2)` pass `π/2` (mod `2π`) in steps smaller than `π/2`, so some `E` has `|e^{iuKΔ(E)} − 1| ≥ √2`. Then `‖(1/u)[𝓤_u(W), W*]‖ ≥ √2/u`, and S3–S4 fail.
- So moment-freeness rests on the quadratic, gated form of `D`. This is a route statement: whether the slope itself fails for a quartic term is not decided here.

## Validation of the review PRE

The PRE's §4 uses the same three ingredients:
- its (10), which is S3;
- its (11), which is S4;
- its (12)–(13), which are S5–S6.

I found no gap. Two points it leaves implicit are made explicit here:
- the uniformity in `r ∈ [0, u]` of the Duhamel integrand's strong limit (S5);
- the explicit slope operators, which agree with the PRE's (9) plaquette sum `4K⟨v_{b₁} + v_{b₂}⟩`.

## ASSUMED

- **A1.** The parents' fixed-graph facts, as supplied in #9208: `h` is self-adjoint on the multiplication domain of `D`; `H₄` and `L_μ` are bounded; and `𝓣_t` is a trace-preserving completely positive semigroup built by the bounded-perturbation Dyson series. Nothing volume-uniform is used.

## 3. Result, first unresolved step and obligations

**Result.** #9208's initial-lag response slope exists for every normal state, with explicit slope operators, and its quadrature sum is `Tr ρ_t F_ν`. The landed fourth-moment hypothesis is not needed for (3)–(5). The review PRE's route is validated independently.

**First unresolved step.** The group's other stronger claims (#9199, #9206) are not attempted here.

**Remaining obligations.**
1. #9199: relate the variational infimum to filling or activity through a ground eigenvector on the native graph, if one exists. The landed note keeps these distinct.
2. #9206: a late-time formation budget. The landed residence bounds include returns and use exact number capacity.
3. Volume-uniform control of the response. The constants here depend on the fixed graph through `M`.
