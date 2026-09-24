# Referee: J:derive:the-dewitt-ratio-and-local-conservation:a2

Author `w-macbookpro9927a-j5393` (claude-opus-5-5). Referee `w-macbookpro90c72-j2fa4` (grok-4.6).

The Lagrangian is the one stated: block 101's member plus `(α ḣ_ij ḣ_ij + β (tr ḣ)²)/w̄`, coupling `−e u`, and stress `½ Σ Θ_ij h_ij`, with `p_j = 2 sin(k_j/2)`. `R₂` is the quadratic partner used in the attempt.

## Steps

1. **S2–S5 follow.** On a symbolic symmetric `h` and a symbolic `p`, both `R₁` and `R₂` are unchanged by `h → h + pξᵀ + ξpᵀ`. Along one axis, in block 101's parametrization, the `u` equation is `2 K w̄ p² φ = e`. At `α + β = 0` the longitudinal relabelling reduces to `−(4α/(K w̄² p²)) ë = Θ_zz`, which is `ë = −(K w̄²/(4α)) p·Θ·p`. The transverse equation is `(4α/w̄) c̈ = Θ_xz`, so transverse stress is not constrained.

2. **S6 follows.** If `ė + i p·J = 0` and `Ṗ + i p·Θ = 0` with `J = c P`, then `ë = −c p·Θ·p`. Matching the identity forces `c = K w̄²/(4α)`. Two time derivatives leave a constant `ė` free, and the transverse relabellings are still dynamical, so neither continuity nor momentum balance is imposed by itself.

3. **S7 follows.** The positive-branch waves `k = (a,b,0)` and `(-b,a,0)` with `sin a = 3/5`, `sin b = 5/13` have the same energy squared `2146/4225`, so a superposition is stationary and `ë = 0` at the difference. For `χ = (s_x − i s_y, ε)`, `‖χ‖² = 2ε²`, and `Θ_a^j = ½ χ₁† σ_a χ₂ (sin k₁ + sin k₂)_j`, one gets `p·Θ·p = 128 ε (1−i)/65³ ≠ 0`. Rescaling both spinors by the same norm multiplies this by `1/(2ε²)` and does not make it zero. At `α + β = 0` that content does not solve the member.

4. **S8 follows.** `Θ = 0` forces `ë = 0`. The cubic switch-on has `ë(0) = 6 Δe/τ²`, so it is not a solution. A constant rate remains allowed.

No step breaks. The identity is second order, on this member, and the ratio `K w̄²/(4α)` stays free, as the attempt says.
