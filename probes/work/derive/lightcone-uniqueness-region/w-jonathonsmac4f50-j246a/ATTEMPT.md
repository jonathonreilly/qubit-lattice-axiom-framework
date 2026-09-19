# lightcone-uniqueness-region: derivation attempt 2 of 3

Worker `w-jonathonsmac4f50-j246a` (claude-opus-5), unit `J-derive-lightcone-uniqueness-region-a2`.

**Sources and provenance**
- **The object** is `probes/lib/formation_levelplane.py` with dim `3s` and the sphere menu. The record at level `t+1` and site `x ∈ Z³` is drawn from `μ_{βS_x}`, and `S_x` is the sum of the 7 records at `(t, x)` and `(t, x ± e_j)`.
- **The kernel.** `μ_V` has density `e^{V·s}/Z(|V|)` on `S²`, and `A(κ) = coth κ − 1/κ`.
- **The TV sensitivity** `|V − V'|/(2√3)` is block 27's F27.1 (PR #8171, `RESULTS_block27.md`).
- **The GIVEN** (the failure of the covariance step) is the round-1 referee reports on `lightcone-formation` a5 and a6 (`referee_w-jonathonsmac4f50-j63d8` and `-jdb2a`). Those were written by claude-opus-5, my model family. I formed my plan before reading them and use nothing from them beyond the GIVEN.

**Metric and notation**
- The metric on `S²` is the chordal one, `|s − s'|`, and "Lip" means 1-Lipschitz for it.
- `W1(μ, ν) := sup_{f Lip} (E_μ f − E_ν f)`. This is the dual form; no duality theorem is used.
- The influence in direction `u` at `V` is `‖D_u(V)‖ := sup_{f Lip} Cov_V(f, u·s)`, the derivative of `V ↦ E_V f`.

## 1. Statement attempted

(a) The W1 influence of the vMF kernel:
- **Exact for equal-norm moves (finite mirror identity):** for `|V| = |V'| = κ > 0`, `W1(μ_V, μ_{V'}) = (A(κ)/κ)|V − V'|`.
  - Hence `‖D_u(V)‖ = A(κ)/κ` for `u ⊥ V`.
  - At `V = 0` it is `1/3` in every direction.
  - `A(κ)/κ < 1/3` for `κ > 0`.
- **Bounded in every direction:** `‖D_u(V)‖ ≤ |cos α| R(κ) + |sin α| A(κ)/κ`, where `α` is the angle between `u` and `V`, and `R(κ) = A'(κ) + I(κ)` is explicit.
- **Rational sweep:** `sup_{κ ≤ 21/10} √(R² + (A/κ)²) ≤ 0.47580 < 10/21`.

(b) The uniqueness region for 7 predecessors:
- **W1, unconditional.** For every `β ≤ 3/10` the level chain forgets its initial records: the memory `m_t = E[s_x·e₀]` from the aligned start is at most `c^t`, with `c = 7βL(β) < 1`. It also has at most one invariant law, uniformly in the torus side `L ≥ 3`.
- **TV.** Block 27's constant gives `β < √3/7 = 0.2474`. No TV–Dobrushin argument can pass `ln(4/3) = 0.2877`, and `3/10 > ln(4/3)`, so W1 gives the larger region.
- **The W1 route's ceiling** is `3/7 = 0.4286`. It reaches `3/7` exactly if the directional lemma of S8 holds.

(c) Comparison with the executed onset of memory: N2.

## 2. Steps

**S1 (PROVED). The Dobrushin contraction in Lipschitz form.**
- Let `F` depend on finitely many records of one level. Set `δ_x(F) = sup |F(τ) − F(τ')|/|τ_x − τ'_x|` over `τ, τ'` that differ only at `x`, and `Δ(F) = Σ_x δ_x(F)`.
- Let `P` be the one-level operator, `PF(σ) = ∫ F ∏_x μ_{βS_x(σ)}(dτ_x)`.
- Suppose `σ, σ'` differ only at `y`. Then `V_x = βS_x` changes only at the 7 sites `x` with `y ∈ pred(x)`, and there `|V_x − V'_x| = β|σ_y − σ'_y|`.
- Swap the 7 affected factors one at a time. At each swap, the integrand is `δ_x(F)`-Lipschitz in `τ_x`. Suppose `|E_V g − E_{V'} g| ≤ L|V − V'|` for Lip `g` and `V, V'` in the ball `B(7β)`. Then `δ_y(PF) ≤ βL Σ_{x: y∈pred(x)} δ_x(F)`.
- Every site has exactly 7 predecessors, so `Δ(PF) ≤ 7βL Δ(F)`, and `Δ(PᵗF) ≤ cᵗ Δ(F)` with `c = 7βL`.
- `PᵗF` depends on finitely many initial records. Changing them one at a time gives `|PᵗF(σ) − PᵗF(σ')| ≤ 2cᵗΔ(F)`.
- **Memory.** Take `F = s_x·e₀` and compare the all-`e₀` start with the all-`(−e₀)` start, which is its reflection. This gives `m_t ≤ cᵗ`.
- **Uniqueness.** For two invariant laws `π, π'`, `|π(F) − π'(F)| = |π(PᵗF) − π'(PᵗF)| ≤ 2cᵗΔ(F) → 0`.
- **The needed `L`.** The segment from `βS` to `βS'` lies in the convex ball, and `d/dt E_{V_t} f = Cov_{V_t}(f, (V' − V)·s)`. So `L = sup_{|V| ≤ 7β, |u| = 1} ‖D_u(V)‖` suffices.

**S2 (PROVED; CHECKED `E1`). The finite mirror identity.**
- Let `|V| = |V'| = κ`, `w = (V − V')/|V − V'|`, and let `ρ_w` be the reflection across `w^⊥`.
- `V·(V − V') − |V − V'|²/2 = (|V|² − |V'|²)/2 = 0`, so `ρ_w V = V'` and `ρ_w` swaps `μ_V` and `μ_{V'}`.
- `p_V/p_{V'} = e^{(V−V')·s}`, with the same normaliser, so `p_V − p_{V'} > 0` exactly on `{w·s > 0}`.
- For Lip `f`: `E_V f − E_{V'} f = ∫_{w·s>0} (f(s) − f(ρ_w s))(p_V − p_{V'})`. This is at most `∫_{w·s>0} 2(w·s)(p_V − p_{V'})`.
- That bound equals `E_V[w·s] − E_{V'}[w·s] = A(κ)(V − V')·w/κ = (A(κ)/κ)|V − V'|`, using `E_V s = A(κ)V/κ`.
- `f = w·s` attains it.
- Letting `V' → V` with `u ⊥ V` gives `‖D_u(V)‖ = A(κ)/κ`.
- At `V = 0` the same mirror across `u^⊥` gives `E₀[(u·s)²] = 1/3` in every direction.

**S3 (PROVED; CHECKED `E2`). `A(κ)/κ` decreases.**
- `κA' − A = g(2κ)/(κ sinh²κ)`, with `g(x) = cosh x − 1 − x²/4 − (x/4)sinh x = Σ_{m≥3} (2 − m)x^{2m}/(2(2m)!) < 0`.
- So `A(κ)/κ` decreases strictly from `1/3`.

**S4 (PROVED; CHECKED `E3`). The parallel direction.**
- Take `V = κe₃` and Lip `f`. Averaging over rotations about `e₃` gives `F(z)`, which is 1-Lipschitz for the same-azimuth chord.
- `Cov_V(f, z) = ∫F′|W|`, where `W(z) = ∫_{−1}^z (t − A)q(t)dt ≤ 0` and `q` is the height density.
- Keep only two constraints:
  - `|F′| ≤ 1/√(1−z²)`;
  - the vertical chords `F(z) − F(−z) ≤ 2z`.
- Write `h(z) = F′(z) + F′(−z)`. Then:
  - `F′(z)|W(z)| + F′(−z)|W(−z)| ≤ λ(z)Δ(z) + h·m(z)`, with `λ(z) = 1/√(1−z²)`, `m = |W(−z)|` and `Δ(z) = |W(z)| − |W(−z)|`;
  - `Δ(z) = (coth κ sinh κz − z cosh κz)/sinh κ`, which is `≥ 0` because `tanh` is concave;
  - `m` does not increase;
  - `∫₀^z h ≤ 2z`.
- By Abel summation, `Cov_V(f, z) ≤ A'(κ) + I(κ) =: R(κ)`, where `I(κ) = ∫₀¹ (λ − 1)Δ`. The same bound holds for `−z`, applied to `−f`.
- In series form, `I sinh²κ = Σ_j d_j κ^{2j+1}` with:
  - `d₁ = 1/36` and `d₂ = 1/225`;
  - `d_j > 0` for `j ≤ 30`, exact;
  - an explicit tail bound.

**S5 (PROVED; CHECKED `E4`). Every direction, and the unconditional region.**
- Rotate about the axis so that `u = cos α V̂ + sin α e₁`. Then `Cov(f, u·s) ≤ |cos α| R(κ) + |sin α| A(κ)/κ`, by S2 and S4. The bound is at most `√(R² + (A/κ)²)`.
- **The sweep.** On 15 subintervals of `[0, 21/10]`, exact rational upper bounds for `κ/sinh κ`, `A/κ = (κ/sinh κ)P₁`, `A' = (κ/sinh κ)²P₂` and `I = κ(κ/sinh κ)²Q` give `√(R² + (A/κ)²) ≤ 0.47580 < 10/21`.
  - `P₁, P₂, Q` are power series with nonnegative leading coefficients and explicit geometric tails.
- **The region.** With S1, `c = 7βL ≤ 7 · (3/10) · 0.47580 = 0.9992 < 1` for every `β ≤ 3/10`.

**S6 (PROVED; CHECKED `E5`). Ceilings.**
- **TV.** Let the other six predecessors sum to `0`; E5 gives an explicit configuration. Flipping one predecessor to its antipode then costs `TV(μ_{βe}, μ_{−βe}) = tanh(β/2)`.
  - So every TV–Dobrushin coefficient is at least `7 tanh(β/2)`, and the TV route fails for `β ≥ 2 artanh(1/7) = ln(4/3) = 0.2877 < 3/10`.
  - Block 27's constant gives `7β/√3 < 1`, i.e. `β < √3/7 = 0.2474`.
- **W1.** Let the other six sum to `−σ`, again explicit. The kernel then sits at `V = 0`, and a small turn of `σ` costs `β/3` per unit.
  - So every sitewise W1 coefficient is at least `7β/3`, and the W1 route cannot pass `3/7`.

**S7 (ASSUMED, not proved: the directional lemma).**
- The lemma: `‖D_u(V)‖ ≤ A(|V|)/|V|` for every `u`, i.e. the perpendicular direction is the worst.
- It is proved here for `u ⊥ V` and at `V = 0` (S2).
- For `u ∥ V` it holds with room in N1's linear programs. It is not proved there: the relaxed bound `R` exceeds `A/κ` for `κ ≲ 0.4`.
- With the lemma, `L = 1/3`, attained at `V = 0`, and the region is exactly `β < 3/7`.

**N1 (numerical, labelled). Linear programs on grids.**
- In the parallel direction the LP gives `0.3297`, `0.2821` and `0.1896` at `κ = 0.25, 1, 2`. The relaxed bound `R` is `0.3361`, `0.2995` and `0.2057`, and `A/κ` is `0.3320`, `0.3130` and `0.2687`.
- On the sphere grid (`N = 500`) at `0°/45°/90°` from `V`:
  - `κ = 1`: `0.2825/0.2983/0.3134`, against `A/κ = 0.3130`;
  - `κ = 2`: `0.1900/0.2323/0.2690`, against `A/κ = 0.2687`.
- The influence grows toward the perpendicular.
- A finer 900-point grid, run as exploration and not in `check.py`, gave the same ordering at `κ = 0.5, 1, 2, 3`. The maximum was within `0.0003` of `A/κ`.

**N2 (numerical, labelled). The executed runs**, parsed from `logs/probes/X:*`: the light-cone sphere, `m·e₀` at the last tabulated level.

| β | L | m·e₀ | level |
|---|---|---|---|
| 0.4 | 64 | −0.0064 | 2500 |
| 0.6 | 32 | +0.3945 | 2500 |
| 1 | 24 | +0.7396 | 3000 |
| 1 | 48 | +0.7576 | 3000 |
| 1 | 96 | +0.7600 | 1500 |
| 1.5 | 48 | +0.8519 | 3000 |
| 2 | 48 | +0.8938 | 3000 |

- In these logs the onset lies between `β = 0.4` and `0.6`. The task states `0.6–0.75` on `32³` planes, and the `β = 0.6, L = 32` run here keeps its direction.
- Either way the proved region `β ≤ 3/10` lies below the onset, and so does the conditional `3/7`. The run at `β = 0.4 < 3/7` loses its direction, which is consistent with the lemma.

## 3. Where the route stops

- **The directional lemma (S7).** The triangle split of S5 costs up to a factor `√2` near `V = 0`. Combining the mirror plan for the perpendicular part with the parallel plan in one coupling would remove it.
- The LP optimum in the parallel direction is reproduced by a decreasing matching along meridians. This is numerical and not used above.

## 4. What would finish it

- A proof of `sup_{|u|=1} sup_{f Lip} Cov_V(f, u·s) ≤ A(|V|)/|V|`. It suffices to prove it for `|V| ≤ 3`, where it gives `β < 3/7`.
  - One possible route: show that the W1 norm of `cos α D_∥ + sin α D_⊥` is at most `√(cos²α ℓ_∥² + sin²α ℓ_⊥²)`. The LP values fit that form to 3 decimals.
- Past `3/7`, a non-sitewise argument would be needed, for example block couplings or the reversibility with respect to `π = ∏Z` from round 1.
