# The member's zero modes on a closed lattice: blocks 146, 147 and 148 checked independently

Task `J:derive:the-members-zero-modes-on-a-closed-lattice:a1`, worker `w-macbookpro9927a-j7245`, model claude-opus-5-5.
Checker: `check.py` in this directory. It is exact (sympy), takes about 2 s, and reports `TOTAL: PASS=6 FAIL=0`.

**Sources.**
- **Landed** on `origin/main` at `25b8c1874f2ea657653dbb298bf383c18d81e0b5`: blocks 60 (T5(b)), 101, 124, 129 and 139, and blocks 134–136 for `α = K/4` and `β = −α`.
- **Open PRs**, read on their branches:
  - block 146 (#9237, head `600adb94e5`);
  - block 147 (#9240, head `328ab48910`);
  - block 148 (#9241, head `e594fcd0c2`).

  These three are the supervisor's own derivations and have not been refereed by another model family.
- **Earlier attempts:** none on this problem.
- **Related work by this worker:** #9245 (block 144's pull) and #9225/#9226 (the member's relabellings).

## 1. Statement attempted

The three blocks are checked within their own supplied models. Nothing is adopted and no gravitational claim is made.

- **Blocks 146 and 147** use the homogeneous action `c_k ℓ³ λ̇²/w − w m(λ)`, with `ℓ = e^λ` (block 60 T5(b), `s = 3` from block 129).
- **Block 148** uses `−8αV Σ_{i<m} λ̇_i λ̇_m/w − w m`, with `V = ℓ₁ℓ₂ℓ₃` supplied.

The checks are independent in three ways:
- **Equations derived here.** The Euler–Lagrange equations come from these actions by sympy's `euler_equations`. They are not taken from the notes' reduced forms.
- **Solutions substituted.** Every stated solution is substituted into those equations.
- **Different builds for the finite facts.**
  - The torus average is computed by counting.
  - The staggered square is checked on a position-space build.
  - The hard-core sign argument is checked on a torus other than block 147's.

## 2. Steps

**Step 1. Block 146 T1: the uniform-stretch coefficient and the constraint. CHECKED A1.**
- On `h = 2λδ`, `α tr(Ḣ²) + β(tr Ḣ)² = (12α + 36β)λ̇²`, which is `−24α` at `β = −α`.
- From the derived equations:
  - varying `w` gives the constraint `−c_k ℓ³ λ̇² − m = 0` at `w = 1`;
  - the constraint's time derivative equals `λ̇` times the length's equation, for every `m(λ)`.
- So the length's equation keeps the constraint.
- The claim that the uniform part of `R₁ = ∂_i∂_jh_ij − ∇²tr h` vanishes is immediate, since `R₁` is a sum of derivatives.

**Step 2. Block 146 T2: the coupling and the pressure form. CHECKED A1.**
- **The coupling.** `∫ e^{ip·r}/p² d³p/(2π)³ = (1/(2π²r)) ∫₀^∞ sin(pr)/p dp = 1/(4πr)`, with the last integral evaluated by sympy. So `u = −e/(4Kp²)` gives `u = −m/(16πK r)` and `G = 1/(16πK)`.
- **The Friedmann form.** Solving `ρ/(24α) = (8πG/3)ρ` for `α` gives exactly `α = K/4`.
- **The pressure form.** Solve the derived constraint and length's equation, with `dm/dλ = −3pℓ³`, for `m` and `λ̈`. This gives `λ̈ + λ̇² = −(ρ + 3p)/(48α)`, which is `−(4πG/3)(ρ + 3p)` at `α = K/4`.

**Step 3. Block 146 T3: top-speed and rest content. CHECKED A2.**
- `ℓ = (1 + t/t₁)^{1/2}` with `t₁ = √(6α/ε)` and `m = ε/ℓ`, and `ℓ = (1 + t/t₀)^{2/3}` with `t₀ = (4/3)√(6α/m₀)` and `m = m₀`, each satisfy the derived constraint and length's equation.
- `p = ρ/3` for `m = ε/ℓ`, and a mixture's pressure is that of its top-speed part.
- `H(k)/ℓ(t)` commutes with itself at all times, so a walker keeps its wave vector and its energy is exactly `E(k)/ℓ`.

**Step 4. Block 147 T1: the sea. CHECKED B1 and B2.**
- **`I` on the `4³` torus.** On this torus `sin² k_a` is 0 or 1. Counting the components with value 1 gives `I = Σ_n C(3,n)√n / 8 = (3 + √3 + 3√2)/8`.
- **The staggered square, built in position space** on the `4³` torus.
  - Take `H = Σ_a S_a σ_a/ℓ + μ(−1)^{x₁+x₂+x₃}` at `ℓ = 3/2`, `μ = 2/5`.
  - Then `H² = (Σ_a S_a²)/ℓ² + μ²` exactly: the staggered term anticommutes with every hop.
  - So the modes are `±√(μ² + s²/ℓ²)`.
  - As a control, a deliberately flipped staggered sign at one site makes the identity fail.
- **The massive mode's pressure.** `p/ρ = y/(3(μ² + y))` with `y = s²/ℓ²`, so `0 ≤ p/ρ < 1/3`.
- **The hard-core sign argument (T1(d)), on a `4×2×2` torus.**
  - Two records, 960 states in the one-record-per-site space, 10752 hops.
  - Every hop flips the product of the occupied sites' signs.
  - So the compressed hopping anticommutes with that product, and its spectrum is symmetric about the books' zero.

**Step 5. Block 147 T2: the bounce. CHECKED B1.**
- With `m = m₀ − I/ℓ`, the derived constraint vanishes at `λ̇ = 0`, `ℓ = I/m₀`.
- The derived length's equation there gives `λ̈ = m₀⁴/(48αI³) > 0`.
- The stated history `t(ℓ) = ±(√(24α)/m₀²)[(2/3)(m₀ℓ − I)^{3/2} + 2I(m₀ℓ − I)^{1/2}]` satisfies `(dt/dℓ)² = 24αℓ/(m₀ − I/ℓ)`, which is `1/ℓ̇²` from the constraint.
- Each massive mode's `√(μ² + s²/ℓ²)` falls with `ℓ`. That gives T2(c)'s two cases, `m₀ > μ` and `m₀ ≤ μ`: the sea's energy rises monotonically toward `m₀ − μ` from below.

**Step 6. Block 148: three lengths. CHECKED C1.**
- **The kinetic term.** On `h_ii = 2λ_i` it is `4(α + β)Σλ̇² + 8βΣ_{i<m}λ̇_iλ̇_m`, which is `−8αΣ_{i<m}λ̇_iλ̇_m` at `β = −α`.
- **Kasner (empty lattice).** Divided by `V`, the derived equations involve only `λ̇` and `λ̈`.
  - `λ_i = p_i log t` with `p = (−u, 1 + u, u(1 + u))/(1 + u + u²)` satisfies all four equations for symbolic `u`.
  - `Σp = Σp² = 1`, and `(Σp)² − Σp² = 2Σ_{i<m}p_ip_m`.
- **The rest-content family** `V = (3m₀t²/2 + Dt)/(16α)`, `λ̇_k = S − (m₀t + D_k)/(8αV)`.
  - `Σλ̇_k = S = V̇/V`.
  - The three length equations and the constraint vanish on the cone `D₀² + D₁² + D₂² = 2(D₀D₁ + D₀D₂ + D₁D₂)`, checked on both roots for `D₂`.
  - Off the cone the constraint fails (control at `D = (1, 2, 7)`).
  - `λ̇_k t → 2/3` as `t → ±∞`.
  - `t → −t`, `D → −D` reverses the family.

**Step 7. Additions. CHECKED D1.**
- **(i) The rest-content family starts as Kasner.** As `t → 0⁺` (where `V → 0`), `λ̇_k t → p_k = 1 − 2D_k/D`. These satisfy `Σp_k = 1`, and on the cone `Σp_k² = 1`. So the family goes from Kasner near `V = 0` to the alike `t^{2/3}` stretch where `V` is large (the Heckmann–Schücking shape named in block 148's prior art). This is exact.
- **(ii) Unequal lengths break the exact `1/ℓ` law.**
  - `[Σ_a σ_a s_a/ℓ_a, Σ_a σ_a s_a/ℓ'_a] ≠ 0` unless the three ratios `ℓ'_a/ℓ_a` agree.
  - So a walker does not keep its band state exactly when the lengths change unequally.
  - Block 146's exact `1/ℓ` energy law for top-speed walkers therefore does not carry over to three lengths. "Top-speed content with three lengths" (block 148's next action) needs slow stretching (adiabatic following) or a non-adiabatic treatment.

## 3. Findings and scope

- **No error found.** Every numbered claim of blocks 146, 147 and 148 that the checker tests holds exactly within the stated models.
- **Scope, as the blocks state it.**
  - The homogeneous models are supplied minisuperspace actions. They use the member's second-order kinetic coefficient with a supplied volume factor (`ℓ³`, `V`), not a derived nonlinear completion.
  - `α = K/4` in block 146 T2 is the same condition as blocks 134–136, met again.
  - `I(4³)` is a torus value, and the `Z³` zone average differs.
  - Which zero of energy the member sees (block 147 T2 against T3) is a reading question that the models do not decide.

## 4. What would extend it

1. Top-speed content with three lengths, adiabatically at late times: the linear shear modes about the `t^{1/2}` stretch. They involve cubic lattice averages `⟨s₁⁴/|s|³⟩` and `⟨s₁²s₂²/|s|³⟩`.
2. The hard-core sea's energy under one record per site, in two and three dimensions, beyond the sign argument.
3. The volume factor for three lengths from the member's nonlinear order (block 148's next action).
