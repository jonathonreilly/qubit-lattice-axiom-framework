# The DeWitt ratio and local conservation — attempt 2 of 2

**Worker:** `w-macbookpro9927a-j5393` (claude-opus-5-5).

**Checks:** `check.py` in this directory has six families (Q, A–E). All are exact, using sympy and Gaussian rationals with √, and run in about 1 s.

**Disclosures.**
- The claim tool printed no earlier attempt on this problem.
- Two of my own units touch the same member and kinetic term:
  - #8734, the kinetic term under the two blindness demands, found that a gradient relabelling is a symmetry iff `β = −α`.
  - #8830 treated the kinetic sign.
- Neither of them adds sources.

## 1. Statement

**The model.** Take block 101's second-order Lagrangian (PR #8895). It is block 60's curvature member plus block 62's kinetic term, with the clock coupled as in block 55. Add the content's stress in the way block 62 fixes it. Block 62 gives `∂⟨H⟩/∂h_ij = −½Θ_(ij)`, so the content adds `+½ Σ_ij Θ_ij h_ij` on every component of `h`. That coupling source vector is the one of block 62's T5.

`L = (α ḣ_ij ḣ_ij + β (tr ḣ)²)/w̄ + K w̄ (u R₁ + R₂) − e u + ½ Θ_ij h_ij`

Here `R₁ = −(p·h·p − p² tr h)` and `R₂` is block 62's quadratic partner (block 101's runner). The lattice momentum is `p_j = 2 sin(k_j/2)`, at any lattice wave vector.

**(a) The relabelling identity.** At `α + β = 0` the relabellings impose exactly one condition on the sources at each lattice wave vector:

`ë = −(K w̄²/(4α)) p·Θ·p`.

- This is the second label-time derivative of the lattice continuity equation `ė + i p·J = 0`, combined with the momentum equation `Ṗ + i p·Θ = 0`, **exactly when the content's energy current is `J = (K w̄²/(4α)) P`**. That factor is the strains' speed squared times the momentum density.
- It is **not** the continuity equation itself. A constant rate `ė` is left free, as in block 101's T4.
- It does **not** yield the momentum equation. The transverse relabellings move, `(4α/w̄) c̈ = Θ_xz`, and they absorb the transverse stress.

**Block 54's walk.** The walk's own content breaks the identity exactly. Superpose two positive-branch plane waves of equal energy. The superposition is stationary, so `ë = 0`, but `p·Θ·p ≠ 0` at their difference wave vector. At `α + β = 0` the member therefore has no solution with the walk as its content.

**(b) Formation.** A record that forms at rest (`Θ = 0`) can change no Fourier component of the energy except at a constant rate.
- Energy converted in place is allowed (blocks 58 and 67).
- Energy that is moved needs a stress with `p·Θ·p = −(4α/(K w̄²)) ë`. That is the momentum flux of a current `J = (K w̄²/(4α)) P`.

## 2. Steps

**S1 (definitions; quoted, family Q).**
- Block 101: the kinetic term `(α ḣ_ij ḣ_ij + β (tr ḣ)²)/w̄`, the member `F₂ = −K w̄ (u R₁ + R₂)`, the coupling `−e u`, and the relabelling equation `d/dt[(α + β) ξ̇_L + β φ̇] = 0` without stress.
- Block 62: the frame response `Θ_a^j = Re ψ†σ_a S_jψ`, with `∂⟨H⟩/∂h_ij = −½Θ_(ij)`, and T5's source vector `(½Θ_11, ½Θ_22, ½Θ_33, Θ_(12), Θ_(13), Θ_(23); −e)`.
- The stress therefore enters as `+½ Σ_ij Θ_ij h_ij`, through every component of `h`, including the relabelling directions.

**S2 (PROVED; CHECKED, family A). Blindness.** For every symbolic `h`, `p` and `ξ`: `R₁(h + pξᵀ + ξpᵀ) = R₁(h)` and `R₂(h + pξᵀ + ξpᵀ) = R₂(h)`.

**S3 (PROVED; CHECKED, family A). The relabelling equation at any wave vector.**
- Project the Euler–Lagrange equations of `h` onto the gradient relabelling direction `δh = 2ppᵀ`.
  - The member contributes nothing, by S2.
  - The kinetic momentum along `δh` is `(4/w̄)(α p·ḣ·p + β p² tr ḣ)`.
  - The stress gives `p·Θ·p`.
- So `d/dt[(4/w̄)(α p·ḣ·p + β p² tr ḣ)] = p·Θ·p`.
- Identically, `α p·ḣ·p + β p² tr ḣ = (α + β) p² tr ḣ − α Ṙ₁`.

**S4 (PROVED; CHECKED, family A). The identity.**
- The Euler–Lagrange equation of `u` is the constraint `K w̄ R₁ = e`, block 101's T2.
- At `α + β = 0`, S3 becomes `d/dt[−(4α/w̄) ė/(K w̄)] = p·Θ·p`.
- That is `ë = −(K w̄²/(4α)) p·Θ·p`, at every lattice wave vector and exactly at second order.
- If `α + β ≠ 0`, the same equation only drives `(α + β) p² tr ḣ`, the longitudinal relabelling. That puts no condition on the sources. So `α + β = 0` is exactly the ratio at which the relabellings constrain the sources.

**S5 (CHECKED, family B). The whole system along one axis.** With block 101's parametrization at `p ∥ z`, the Euler–Lagrange equations with the stress are:
- `2K w̄ p² φ = e`, the constraint;
- `d/dt[(8/w̄)((α + β) ξ̇_L + β φ̇)] = Θ_zz`;
- `(4α/w̄) c̈_x = Θ_xz`, and likewise `c_y` with `Θ_yz`: the transverse relabellings move and give no condition;
- `(4α/w̄) ä + K w̄ p² a = (Θ_xx − Θ_yy)/2`, and likewise `b` with `Θ_xy`: the transverse traceless stress sources the travelling strains.

At `α + β = 0` the `ξ_L` equation reduces to `−(4α/(K w̄² p²)) ë = Θ_zz`, which is S4 with `p ∥ z`.

**S6 (PROVED; CHECKED, family C). What the identity is.**
- Suppose the content obeys `ė + i p·J = 0` and `Ṗ_j + i Σ_i p_i Θ_ij = 0`, with `J = cP`. Then `ë = −c p·Θ·p`.
- This equals S4 iff `c = K w̄²/(4α)`.
- The identity has two time derivatives. So it does not fix the first-order continuity equation: a constant rate `ė(k)` at each `k` is left free.
- The transverse relabellings take up the transverse projection of `p·Θ`, so no momentum equation is imposed.
- The task asks for the momentum density as the source of the relabellings. The covariant stress coupling realises exactly that. With conservation, `Θ_zz = iṖ_z/p`, so the `ξ_L` equation integrates to `(8/w̄)((α + β) ξ̇_L + β φ̇) = i P_z/p + C`.
- Adding a separate `P·ξ̇` source on top would count the momentum twice. With conservation, the right side of S3 would then cancel and force `ë = 0`.

**S7 (CHECKED, family D). Block 54's walk against the identity.**
- Use the identity frame with `w̄ = 1`, so `H = Σ_j σ_j S_j`.
- Take the positive-branch plane waves `k₁ = (a, b, 0)` and `k₂ = (−b, a, 0)`, with `sin a = 3/5`, `cos a = 4/5`, `sin b = 5/13`, `cos b = 12/13`.
- They have equal energy `ε = √(2146/4225)`, so their superposition is stationary and `ë(q) = 0` at `q = k₂ − k₁`.
- Block 62's `Θ_a^j = Re ψ†σ_a S_jψ` at `q` is `½ χ₁†σ_aχ₂ (sin k₁ + sin k₂)_j`. The products `p_i p_j` at `q` are rational: `64/65, 4/65, −16/65`.
- The result is `p·Θ·p = 128ε(1 − i)/65³ ≠ 0`, whereas S4 requires 0.
- So at `α + β = 0` the member has no solution with this content. This is block 62's T5 static failure (the walk's stress is not divergence-free in the member's lattice symbol), now forced at every label time.
- At long waves the walk carries energy at unit speed, `J ≈ P`. So S6's condition is `K w̄²/(4α) = 1`, which is block 62's open question `α = K/4`.

**S8 (CHECKED, family E). Formation (b).**
- At rest, `Θ = 0`, so `ë = 0` at every wave vector. Block 101's switch-on has `ë(0) = 6Δe/τ²` and therefore has no solution. Bounded content keeps `e(k)` constant.
- Formation that converts energy in place, as in blocks 58 and 67, is consistent.
- Formation that moves energy must carry the stress of S6: a current `J = (K w̄²/(4α)) P`.

**ASSUMED.**
- The coupling of S1: block 62's `∂⟨H⟩/∂h = −½Θ` taken as the content's source for every component of `h`, which is its T5.
- Block 101's `R₂`.
- Content momentum balance and energy continuity with the member's symbol `p`, where S6 uses them. The walk's own versions fail at finite `k` (S7).

## 3. Where it stops

1. **The exact lattice level.** S7 shows that the walk's exact content is not consistent at `α + β = 0`. The member reads divergences with `p_j = 2 sin(k_j/2)`, while the walk's momentum flux is built from `S_j`, whose symbol is `sin k_j`. Block 62 names the repair: a bond-placed member whose `h` lives where the walk's exactly conserved bond current lives. That is not attempted here.
2. **The first-order law.** S4 is second order. The first-order continuity equation needs, in addition, the integration constant set by the history. Starting from rest with `P = 0`, S6's integrated form gives `ė = −i (K w̄²/(4α)) p·P`.
3. **The ratio `K w̄²/(4α)`.** It is free. For unit-speed content it must equal 1, which is `α = K w̄²/4`, and nothing here fixes it.

## 4. What would finish it

- A member written on the walk's bonds, redone through S3–S7. Does the walk's exactly conserved bond current then satisfy the identity at every `k`?
- A reason for `α = K w̄²/4`.
- For formation, a clause that carries the stress of S8 whenever energy moves.
