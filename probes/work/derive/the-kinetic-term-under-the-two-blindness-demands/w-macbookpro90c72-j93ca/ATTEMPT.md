# J:derive:the-kinetic-term-under-the-two-blindness-demands:a1: blindness in the label leaves block 62's two kinetic numbers and then fixes β = −α; α/K stays declared

**Provenance.**
- Worker `w-macbookpro90c72-j93ca`, model `claude-opus-5-5`, one session. Attempt 1 of 2; the claim printed no prior attempts.
- **Plan, formed before reading the notes in detail:**
  1. A label-dependent rotation of the coin axes should shift the frame's rate by an antisymmetric matrix, so blindness removes one of the three invariants.
  2. A label-dependent relabelling should then be a symmetry only for one kinetic ratio, with the rates acting as the multiplier.
- **Sources.** Definitions come from block 62 (#8592; T1, T3, T4: the frame, the metric `g^{ij} = Σ_a E^i_a E^j_a`, the member `R₁`, `R₂`, the kinetic family `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]`, the mode determinant) and block 60 (#8590; T5: the local kinetic term `Σ c_k ℓ^s(dλ/dt)²/w` and the comparator's `c_k = −6K`). Block 64's statement is taken as the task restates it.
- **Comparators, named only:**
  - DeWitt's supermetric (`β = −α` is its value);
  - the uniqueness results for representations of the hypersurface-deformation algebra (Hojman–Kuchař–Teitelboim).
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Setting.**
- The frame is the matrix `E[j, a] = e^j_a` (bond direction `j`, coin axis `a`), with inverse metric `g⁻¹ = EEᵀ`.
- The frame's rate per tick is `K = ĖE⁻¹/w`, i.e. `K^j_k = e^a_k ė^j_a/w`.
- The three local quadratic invariants, with indices moved by the metric:
  - `I₁ = K_{jk}K^{jk}` (`tr(KᵀK)`);
  - `I₂ = K^j_k K^k_j` (`tr K²`);
  - `I₃ = (K^j_j)²`.
- The weight-one density is `(det e/w)·Q(ĖE⁻¹) = w det e·Q(K)`. `ė` has weight one and `w` weight one, so the density has the weight of block 60 T5's `(dλ/dt)²/w`.

**Claims.**

**(a) (PROVED; CHECKED K.rot, sympy exact for a generic rational frame, symbolic rates and a symbolic antisymmetric matrix.)**
- A rotation of the coin axes that varies in place and in the label, `E → ERᵀ`, changes `K` by `E(ṘᵀR)E⁻¹/w`. Lowered with the metric, that change is `E⁻ᵀ(ṘᵀR)E⁻¹/w`, **exactly antisymmetric**, and it is arbitrary at each site and label.
- The symmetric part of the lowered `K` is **exactly `−ġ/(2w)`**.
- **The invariants split.** `I₁ = |S|² + |A|²` and `I₂ = |S|² − |A|²`, while `I₃` sees only `S`. So `c₁I₁ + c₂I₂ + c₃I₃` is blind iff `c₁ = c₂`.
- **The result.** Exactly two numbers remain: `(det e/w)[α tr(g⁻¹ġ g⁻¹ġ) + β(tr g⁻¹ġ)²]`. At first order around the identity frame (`h = −(ε + εᵀ)`) this is `(1/w)[α ḣ_ij ḣ_ij + β ḣ²]`, block 62's family.

**(b) (PROVED; CHECKED K.iso, K.modes.)**
- **The isotropic stretch.** For `h = 2λδ` the kinetic term is `(12α + 36β)(dλ/dt)²/w`. So block 60 T5's `c_k = 12α + 36β`. A closed lattice moves uniformly iff `β < −α/3`; `α > 0` is needed for real travelling disturbances.
- **The mode determinant.** Block 62 T4's `7×7` determinant is reproduced as a constant times `X³α²(α + β)(p²)²(p² − 4αX)²`.
- **At `β = −α`:**
  - `(h, u) = (ppᵀ, 2αX/K)` is a null vector for every `p` and `X`.
  - The quadratic Lagrangian `L = α ḣ_ij ḣ_ij + β ḣ² + K(uR₁ + R₂)` changes under the **gradient relabelling in the label** `h → h + ppᵀζ(t)`, with `u → u − (2α/K)ζ̈`, by exactly `−2α d(ζ̇R₁)/dt`. That is a total derivative, and it is one **only** at `β = −α`.
  - **The multiplier.** The rates act as the multiplier of this symmetry, as the rate of a clock does for the comparator's time reparametrisation.
  - **On a constraint surface.** Without the shift of `u`, it is a symmetry where `R₁` is constant in the label, i.e. on the rates' constraint with the content fixed.
- **Transverse relabellings in the label** (`p·ξ = 0`) cost `2αp²|ξ̇|²` for **every** `(α, β)`. No field of the clauses couples to them; a shift-like vector field would be needed.
- `(α, β) = (K/4, −K/4)` gives `c_k = −6K`, block 60 T5's comparator value.

**(c) What fixes the ratios.**
- **`β/α`.** The label-extension of block 64's blindness to relabellings, for gradient relabellings with the rates as multiplier, fixes `β = −α`. Full blindness to relabellings in the label (including transverse ones) cannot be met by any `(α, β)` within the clauses.
- **`α/K`.** The travelling pair has `X = Kw̄²p²/(4α)`. It moves at the walker's top speed iff `α = K/4`. No clause of blocks 53 to 65 makes the field's disturbances share the walker's light cone, so `α/K` stays **declared**, as do `K` and the existence of the kinetic term.

## 2. Steps

**S1 (definitions).**
- `E → ERᵀ` is the rotation of the coin axes: `e^j_a → R_{ab} e^j_b`.
- `ṘᵀR` is antisymmetric, since `RᵀR = 1`.
- Block 62's member: `R₁ = −(p·h·p − p²h)` and `R₂ = −¼p²h_ijh_ij + ½|hp|² − ½(p·h·p)h + ¼p²h²`. Both are unchanged by `h → h + p_iξ_j + p_jξ_i` (block 62 T3).

**S2 (PROVED; CHECKED K.rot).**
- **The shift.** `K′ = (ĖRᵀ + EṘᵀ)R E⁻¹/w = K + E(ṘᵀR)E⁻¹/w`. Lowering with `g = E⁻ᵀE⁻¹` gives `E⁻ᵀ(ṘᵀR)E⁻¹/w = MᵀΩM` with `M = E⁻¹`, which is antisymmetric.
- **The symmetric part.** `ġ = −g(ĖEᵀ + EĖᵀ)g`, and `Eᵀg = E⁻¹`, so `½(gK + (gK)ᵀ) = −ġ/(2w)`.
- **The split.** With `gK = S + A`, the cross terms of `I₁` and `I₂` vanish by transposition and cyclicity, so `I₁ = |S|² + |A|²` and `I₂ = |S|² − |A|²` (norms with `g⁻¹`). Also `tr K = tr(g⁻¹S)`. Since `A` can be shifted arbitrarily, only `c₁ = c₂` survives.
- **CHECKED** for `E = [[2,1,0],[½,3,1],[0,−1,2]]` with 9 symbolic rates and 3 symbolic rotation rates:
  - `I₁ + I₂` and `I₃` are unchanged;
  - `I₁ − I₂` is not;
  - `sym(gK) = −ġ/(2w)`;
  - to first order, `tr S² = tr ḣ²/4` and `(tr K)² = (tr ḣ)²/4`.

**S3 (PROVED; CHECKED K.iso).**
- For `h = 2λδ`: `ḣ_ij ḣ_ij = 12λ̇²` and `ḣ² = 36λ̇²`.
- Block 60 T5(b) needs `c_k < 0` for uniform motion, where `c_k = 12α + 36β`.
- `c_k(β = −α) = −24α`, and `c_k(K/4, −K/4) = −6K`.

**S4 (PROVED; CHECKED K.modes).**
- **The determinant.** The mode equations `X∂kin/∂h + ∂(K(uR₁ + R₂))/∂h = 0`, `KR₁ = 0` form a symmetric `7×7` system, and its determinant factors as stated. The null vector follows.
- **The symmetry.** Under `δh = ppᵀζ`:
  - the kinetic term changes by `2ζ̇(α p·ḣ·p + βp²ḣ) + (α + β)p⁴ζ̇² = −2αζ̇Ṙ₁ + (α + β)(2p²ḣζ̇ + p⁴ζ̇²)`;
  - `R₁` and `R₂` are unchanged;
  - `δu = −(2α/K)ζ̈` adds `−2αζ̈R₁`.

  The total is `−2α d(ζ̇R₁)/dt + (α + β)(…)`, checked with `h`, `u`, `ζ` as symbolic functions of the label.
- **Transverse.** With `ξ = (p₂, −p₁, 0)ζ(t)`, the `ζ̇²` coefficient is `2αp²(p₁² + p₂²)`, with no `β` (the trace of `δh` vanishes). The potential is unchanged and no multiplier couples, so no `(α, β)` with `α ≠ 0` makes it a symmetry.

**S5 (PROVED; CHECKED K.speed).** `X = Kp²/(4α)` equals `p²` iff `α = K/4`.

## 3. The first failing step

**Full blindness to relabellings in the label.** It fails at S4 for transverse relabellings, at every `(α, β)`: they cost `2αp²|ξ̇|²` and nothing in the clauses can absorb it. In the comparator a shift vector does this; the framework has no such field.

Everything else claimed holds at second order, and part (a) holds exactly for every frame.

## 4. What would finish it

1. **Beyond second order.** Whether the gradient-relabelling symmetry, with the rates as multiplier, extends past second order for block 64's `D*` together with `(α, −α)`. That would be the closure of a constraint algebra, the comparator's route to `β = −α` without choosing it.
2. **A shift-like vector field.** Whether one exists in the framework's vocabulary, for instance from bond rates (block 59) or the frame's twist (block 65), to carry the transverse relabellings.
3. **A reason for one light cone.** Whether any clause shares a light cone between the walker and the field. That would fix `α = K/4`.

## 5. Running it

```
python3 probes/work/derive/the-kinetic-term-under-the-two-blindness-demands/w-macbookpro90c72-j93ca/check.py
```

The run takes about 20 s. It prints four exact checks, then the SUMMARY and HIT lines.
