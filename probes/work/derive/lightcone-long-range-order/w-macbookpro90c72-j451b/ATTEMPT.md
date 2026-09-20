# Long-range order under light-cone formation: the doubled graph is a slab

Independent attempt 2 of 5. Worker `w-macbookpro90c72-j451b`, model claude-opus-5.
Plan formed before reading `w-jonathonsmac4f50-j539b` (a4) and `w-jonathonsmac4f50-ja59c` (a5); §3 states exactly
where it agrees with them, where it is new, and one place where a5's text is wrong.

## 1. The statement attempted

**Objects (GIVEN, refereed).** `L` even. `Γ_L` has vertices `(x,ε)`, `x ∈ (Z/L)³`, `ε ∈ {0,1}`, and edges
`{(x,0),(y,1)}` for `y − x ∈ N7 = {0, ±e₁, ±e₂, ±e₃}`. `μ_L` is the sphere-menu (`ν = 3`) Heisenberg ferromagnet on
`Γ_L`: density `∝ exp(β Σ_{edges} s_u·s_v)`, uniform a priori measure on `S²` at each vertex. The stationary law
`π_L` of the light-cone formation law is the layer-0 marginal of `μ_L`, `π_L(s) ∝ Π_x Z(β|S_x(s)|)`.
`E(k) = 6 − 2Σ_j cos k_j`, `b(k) = 1 + 2Σ_j cos k_j`, `k ∈ (2π/L)(Z/L)³`, `N = L³`, `m₀ = (1/N)Σ_x s_{(x,0)}`.

**R1 (the structure).** For every even `L`,

  `Φ(x,ε) = (x, (ε + x₁ + x₂ + x₃) mod 2)`

is a graph isomorphism `Γ_L → (Z/L)³ □ K₂`, the **two-layer nearest-neighbour slab**: the self-edge `δ = 0` of the
7-stencil becomes the rung `{(x,0),(x,1)}`, and `δ = ±e_j` becomes an ordinary nearest-neighbour edge *inside one
layer*. `Φ` is an involution. All 7 couplings are `β`, so `μ_L` is the isotropic nearest-neighbour Heisenberg
ferromagnet on the slab — equivalently, on the 4-dimensional torus `(Z/L)³ × (Z/2)` with the two vertical bonds
carrying `β/2` each. Consequently the reflections needed below are the *standard* site- and bond-plane reflections
of a hypercubic torus, and the referee's objection ("the reflections used preserve the bipartition and vertical
edges never cross a reflection plane") does not arise: in the slab picture the vertical direction has its own
bond plane, which cuts every rung and no other edge.

**R2 (the bound).** For every even `L` and every `β > 0`,

  `⟨|m₀|²⟩_{π_L} ≥ 1 − (3/(2β)) (G_L + H_L)`,  `G_L = (1/N)Σ_{k≠0} 1/E(k)`,  `H_L = (1/N)Σ_k 1/(14 − E(k))`.

**R3 (route (ii) closes with no loss).** The passage from the doubled-graph magnetization to the one-layer
magnetization needs *no* energy bound and *no* reflection: layer exchangeability plus Cauchy–Schwarz give
`⟨|M|²⟩ ≤ 4⟨|M₀|²⟩` exactly, and `4N² = |Γ_L|²`, so the constant is unchanged.

**The threshold.** `G_L → W₁ = ∫ d³k/(2π)³ 1/E(k)` and `H_L → W₂ = ∫ d³k/(2π)³ 1/(14 − E(k))`, the first from
below and the second from above, with `G_L + H_L < W₁ + W₂` at every size checked (S8), so long-range order
`⟨|m₀|²⟩ ≥ 1 − β₀/β > 0` holds on every sufficiently large even torus for

  **`β > β₀ := (3/2)(W₁ + W₂) = 0.5904937…`**

with `W₂ ∈ [0.1409314881127, 0.1409314881130]` (exact rational bracket, CHECKED C8) and `W₁ = W_sc/6 = 0.2527310099…`,
`W_sc = 1.5163860591…` the simple-cubic Watson constant (value ASSUMED A2; rational lower bound CHECKED C9).

**A second, independent threshold** that survives even if a referee kills the rung reflection: deleting the rungs
leaves two disjoint copies of the nearest-neighbour Heisenberg ferromagnet on `(Z/L)³`, so by Ginibre monotonicity
(ASSUMED A3) `π_L` dominates that model's two-point function, and the classical infrared bound for it gives order
for `β > 3W₁ = W_sc/2 = 0.7581930296…` (CHECKED C11). Strictly weaker than `β₀`, on strictly weaker machinery.

## 2. Steps

**S1 (GIVEN).** `π_L` is the layer-0 marginal of `μ_L`; `μ_L` is invariant under every automorphism of `Γ_L`.

**S2 (PROVED; CHECKED C1, C2).** `Φ` is an isomorphism `Γ_L → (Z/L)³ □ K₂`. `τ(x) = x₁+x₂+x₃ mod 2` is well
defined on `(Z/L)³` because `L` is even; `Φ∘Φ = id`. Take a `Γ_L` edge `{(x,0),(x+δ,1)}`, `δ ∈ N7`. Then
`Φ(x,0) = (x, τ(x))` and `Φ(x+δ,1) = (x+δ, 1 + τ(x) + τ(δ))`. If `δ = 0`: the image is `{(x,τ(x)), (x,1+τ(x))}`,
a rung. If `δ = ±e_j`: `τ(δ) = 1`, so the image is `{(x,τ(x)), (x+δ,τ(x))}`, a nearest-neighbour edge inside
layer `τ(x)`. Both maps are onto: every rung `{(x,a),(x,a+1)}` is the image of `{(x,0),(x,1)}`, and every
in-layer edge `{(x,a),(x+e_j,a)}` is the image of `{(x,0),(x+e_j,1)}` when `a = τ(x)` and of
`{(x+e_j,0),(x,1)}` when `a = τ(x)+1`. Both graphs are 7-regular with `7L³` edges, and `Φ` is a bijection on
vertices, so the edge map is a bijection. C1 compares the two edge sets as sets, exactly, at `L = 4, 6`.

**S3 (PROVED; CHECKED C3, C4).** The `Γ_L` Laplacian `L_Γ = 7·Id − A` has spectrum `{7 − b(k)} ∪ {7 + b(k)}`
(`A` is bipartite with blocks the circulant of symbol `b(k)`, so its spectrum is `±b(k)`), i.e. `{E(k), 14 − E(k)}`.
The slab Laplacian is the Cartesian sum, spectrum `{E(k), E(k) + 2}`. These agree because `7 − b(k) = E(k)` and
`7 + b(k) = 8 + 2Σcos k_j = E(k+π*) + 2` with `π* = (π,π,π)`, and `k ↦ k+π*` permutes the modes. C3 checks the two
identities symbolically; C4 checks that the two multisets coincide exactly, and that `Σ_{Λ≠0} 1/Λ` agrees between
the two parametrizations, at `L = 4, 6` in exact rational arithmetic.

**S4 (ASSUMED A1, at the exact scope used).** *Gaussian domination.* For the nearest-neighbour ferromagnet with
unit spins in `S^{ν−1}` and couplings `J_e > 0` on a torus `(Z/L₁)×…×(Z/L_d)`, `L_i` even, with `J` constant in each
direction, `Z(h) ≤ Z(0)` for every edge field `h`, where
`Z(h) = ∫ Π dσ exp(−Σ_e (J_e/2)|s_u − s_v − h_e|²)` (Fröhlich–Israel–Lieb–Simon 1978; the reflections are the
standard site- and bond-plane reflections in each direction). Applied at `d = 4`, `(L,L,L,2)`, `J = (β,β,β,β/2)`,
which by R1 is exactly `μ_L`. The only non-textbook feature is `L₄ = 2`: that direction has one bond plane, which
cuts both of its edges, and the reflection through it is the layer swap of the slab. **This is the one step a
referee should attack**, and it is where a4 and a5 also sit.

**S5 (PROVED from S4).** *The infrared bound.* Write `h_u = ε v_u e` with `v` a real eigenvector of the weighted
Laplacian `L_J` (`L_J v = Λ v`), `e` a unit vector of `R^ν`, `ε ∈ R`, and take the gradient edge field
`h_{uv} = h_u − h_v`. Since `Σ_e J_e|s_u−s_v−(h_u−h_v)|² = Σ_e J_e|s_u−s_v|² − 2(s, L_J h) + (h, L_J h)`,
S4 reads `⟨exp((s, L_J h))⟩ ≤ exp((h, L_J h)/2)`, i.e. with `X = Σ_u v_u (s_u·e)`,
`⟨exp(εΛX)⟩ ≤ exp(ε²Λ|v|²/2)`. Averaging the `±ε` versions kills `⟨X⟩` and the `ε²` coefficients give
`(Λ²/2)⟨X²⟩ ≤ Λ|v|²/2`, hence `⟨X²⟩ ≤ |v|²/Λ`. Summing over `ν` orthonormal `e`:

  `⟨|Ŝ_α|²⟩ ≤ ν/Λ_α` for a unit eigenvector `v^{(α)}`, `Ŝ_α = Σ_u v^{(α)}_u s_u`.

With `J = β` on all edges, `L_J = β L_Γ`, `Λ_α = β·(Λ_Γ)_α`, so `⟨|Ŝ_α|²⟩ ≤ ν/(β(Λ_Γ)_α)`. No factor of 2 is
available here: the lattice weight `exp(βΣ s·s')` is `exp(−(β/2)Σ|s−s'|²)` up to a constant, so the quadratic
form in S4 is `(β/2)(·, L_Γ ·)` exactly.

**S6 (PROVED).** *Sum rule.* In an orthonormal eigenbasis, `Σ_α ⟨|Ŝ_α|²⟩ = ⟨Σ_u |s_u|²⟩ = |Γ_L| = 2N`, because the
spins are unit vectors. The unique zero mode is `v^{(0)} = |Γ_L|^{-1/2}𝟙` (`Γ_L` is connected), giving
`Ŝ_0 = |Γ_L|^{-1/2} M`, `M = Σ_u s_u`. Hence

  `⟨|M|²⟩/|Γ_L|² = 1 − (1/|Γ_L|)Σ_{α≠0}⟨|Ŝ_α|²⟩ ≥ 1 − (ν/β)(1/|Γ_L|)Σ_{α≠0} 1/(Λ_Γ)_α = 1 − (3/(2β))(G_L + H_L)`,

using S3 for the spectrum. `14 − E(k) ≥ 2 > 0` for all `k`, so `H_L` is finite; `E(k) = 0` only at `k = 0`.

**S7 (PROVED; CHECKED C5).** *Route (ii), the one-layer reduction.* Let `M_a = Σ_x s_{(x,a)}`, so `M = M₀ + M₁` and
`m₀ = M₀/N`. The layer swap `(x,0) ↔ (x,1)` is an automorphism of `Γ_L` (because `N7 = −N7`), so by S1
`⟨|M₀|²⟩ = ⟨|M₁|²⟩`. By Cauchy–Schwarz twice,
`⟨M₀·M₁⟩ ≤ ⟨|M₀||M₁|⟩ ≤ ⟨|M₀|²⟩^{1/2}⟨|M₁|²⟩^{1/2} = ⟨|M₀|²⟩`. Hence
`⟨|M|²⟩ = ⟨|M₀|²⟩ + ⟨|M₁|²⟩ + 2⟨M₀·M₁⟩ ≤ 4⟨|M₀|²⟩`, and since `|Γ_L|² = 4N²`,

  `⟨|m₀|²⟩ = ⟨|M₀|²⟩/N² ≥ ⟨|M|²⟩/|Γ_L|² ≥ 1 − (3/(2β))(G_L + H_L)`.   **This is R2.**

The inequality `⟨|M|²⟩ ≤ 4⟨|M₀|²⟩` is saturated iff `M₀ = M₁` a.s.; no energy input, no reflection, and the
constant of S6 is carried through unchanged.

**S8 (PROVED; CHECKED C6, C7).** *The mode sums converge to the constants.*
`G_L = L⁻³Σ_{k≠0} 1/E(k)` and `H_L = L⁻³Σ_k 1/(14 − E(k))` are Riemann sums over `(2π/L)(Z/L)³`.
`1/(14 − E)` is continuous on the torus (`14 − E ≥ 2`), so `H_L → W₂` by uniform continuity. For `G_L`, fix
`δ > 0`. Outside `|k| ≤ δ` the integrand is continuous, so those sums converge to the integral over that region.
Inside, `E(k) = 4Σ_j sin²(k_j/2) ≥ (4/π²)|k|²` on `[−π,π]³`, and with `k = 2πn/L`, `R := δL/2π`:

  `L⁻³Σ_{0<|k|≤δ} 1/E ≤ (π²/4)·L⁻³(L/2π)²·Σ_{0<|n|≤R} 1/|n|² = (1/(16L))·Σ_{0<|n|≤R} 1/|n|².`

For the lattice sum, compare each `n ≠ 0` with its unit cube `Q_n`: every `x ∈ Q_n` has `|x| ≤ |n| + √3/2`, and
`|n| ≥ 1` gives `|n| + √3/2 ≤ (1 + √3/2)|n|`, so `1/|n|² ≤ (1+√3/2)²/|x|²` on `Q_n`; the cubes are disjoint and
contained in `|x| ≤ R + 1`, so

  `Σ_{0<|n|≤R} 1/|n|² ≤ (1+√3/2)² ∫_{|x|≤R+1} d³x/|x|² = 4π(1+√3/2)²(R+1) ≤ 44(R+1).`

Hence `L⁻³Σ_{0<|k|≤δ} 1/E ≤ (44/16)(δ/2π + 1/L) → 11δ/(4π)`, which is `O(δ)` uniformly in `L`; the same estimate
gives `∫_{|k|≤δ} 1/E ≤ (π²/4)·4πδ = π³δ`. Letting `L → ∞` and then `δ → 0` gives `G_L → W₁`. Therefore
`lim_L (G_L + H_L) = W₁ + W₂`, and any `β > β₀ = (3/2)(W₁+W₂)` gives a `c(β) > 0` and an `L₀(β)` with
`⟨|m₀|²⟩ ≥ c(β)` for every even `L ≥ L₀(β)`.

C7 checks the sharper `Σ_{0<|n|≤R} 1/|n|² ≤ 13R` in exact rationals for every integer `R ≤ 40`. C6 computes
`G_L, H_L` exactly at `L = 4, 6, 12` (at `L = 12` in `Q(√3)`): `G` increases, `0.197526 < 0.215365 < 0.233942`,
and `H` decreases, `0.141741 > 0.140966 > 0.140931`, and `G_L + H_L < W₁ + W₂` at each of the three sizes — at
these sizes the finite-volume constant is already **smaller** than the limiting one, so the threshold is not
approached from the side that would make finite `L` worse than the limit.

**S9 (CHECKED C8, C9, C10; value of `W₁` ASSUMED A2).** *The constants.* With `φ(k) = (1/3)Σcos k_j` and
`p_n = ∫φ^n d³k/(2π)³` the simple-cubic return probabilities (`p_{2m} = 6^{-2m}Σ_{i+j+k=m}(2m)!/(i!²j!²k!²)`,
`p_odd = 0`):
`W₁ = (1/6)Σ_n p_n = W_sc/6`, and `W₂ = (1/8)Σ_m (9/16)^m p_{2m}`, from `14 − E = 8 + 2Σcos k_j` and
`∫(Σ_j cos k_j)^n = 6^n p_n / 2^n`. The `W₂` series has the geometric tail `Σ_{m≥M} ≤ (2/7)(9/16)^M`
(`p ≤ 1`), so C8 brackets `W₂` two-sidedly in exact rationals at `M = 60` (width `< 3·10⁻¹⁶`). The `W₁` series has
tail `Θ(M^{-1/2})`, so exact partial sums give only a rigorous *lower* bound (C9: `W₁ ≥ 0.2426709…` at `M = 60`,
consistent); its **value** is taken from Watson's closed form
`W_sc = (√6/(32π³))Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)` and is **ASSUMED (A2)** — it enters only the numerical value of
`β₀`, never R1, R2 or R3.

**Consistency with the executed numerics (CHECKED C11).** At `β = 1`, R2 gives `⟨|m₀|²⟩ ≥ 1 − β₀ = 0.40951`,
i.e. `|m₀| ≥ 0.6399`; the executed value is `0.76`, i.e. `0.5776 ≥ 0.40951`. The bound is satisfied and not tight,
as an infrared bound should be.

## 3. Relation to a4 and a5, and one correction

- **a5 (`w-jonathonsmac4f50-ja59c`)** states the same final inequality `⟨|m₀|²⟩ ≥ 1 − (3/(2β))(G_L+H_L)` and the
  same limiting constant. S5–S7 here were derived independently and **confirm a5's constant exactly**, by a route
  that replaces a5's bespoke reflection with R1. a5's proved threshold is `β > 0.5931` (the top of its rigorous
  bracket for `I₀`); the value `0.5904937` stated here is a5's own named sharpening target, and it is reached only
  on A2, so **the rigorous threshold is not improved**. What is new is R1 and R3.
- **a5 §3 is wrong on route (ii).** It says: "exchangeability of the layers does not bound it. So route (ii)
  reduces to bounding that [vertical-edge] energy." S7 bounds it with two applications of Cauchy–Schwarz and no
  energy input, losing nothing: `⟨|M|²⟩ ≤ 4⟨|M₀|²⟩` because `⟨M₀·M₁⟩ ≤ ⟨|M₀|²⟩^{1/2}⟨|M₁|²⟩^{1/2}` and the two
  layers are exchangeable. The vertical-edge energy never has to be estimated.
- **a4 (`w-jonathonsmac4f50-j539b`)** avoids the rung reflection and pays for it with a threshold near `7` via an
  energy bound (its S4–S7). S7 here shows the layer reduction itself is free; a4's energy work would still be
  needed for anything that replaces S4.
- **Route (iii)** (a sum-rule lower bound on `E|S_x|`, block 22 / PR #8156) is not needed and was not attempted.

## 4. What would finish it

1. **Discharge A1 at `L₄ = 2`.** Write out the FILS chessboard argument for the slab: one bond plane in the
   vertical direction, cutting every rung. This is the whole remaining mathematical content of the threshold.
2. **Discharge A2.** A rigorous two-sided rational bracket for `W₁`. The obstruction is the `Θ(M^{-1/2})` tail:
   `Σ_{m≥M} p_{2m} = ∫ φ^{2M}/(1−φ)`, and Cauchy–Schwarz fails because `∫(1−φ)^{-2} = ∞` in `d = 3`. Hölder with
   `p = 5/4` works in principle and needs a rigorous rational upper bound for `∫(1−φ)^{-5/4}`.
3. **Sharpen `β₀`.** The energy-improved ("water-filling") sharpening is a4's territory and is not duplicated here.
4. **Infinite volume.** S8 gives order at every even `L ≥ L₀(β)`; a translation-invariant infinite-volume
   Gibbs state with `⟨s_0·s_x⟩ ≥ c(β) > 0` needs the usual compactness plus a lower semicontinuity argument.
5. **Six-axis menu.** Untouched. R1 is menu-independent (it is a statement about `Γ_L` alone), so it transfers
   verbatim; S5–S7 use only unit-length records and would need the stationary-law identification for that menu.
