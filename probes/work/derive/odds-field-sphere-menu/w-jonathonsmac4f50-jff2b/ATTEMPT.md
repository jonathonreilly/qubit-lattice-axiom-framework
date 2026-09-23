# odds-field-sphere-menu, attempt 2 of 4

**The lean's massless point, the ordered odds with a transverse channel free of mass, and what a record and a mass feed in.**

Worker `w-jonathonsmac4f50-jff2b` (`claude-opus-5-5`), unit `J:derive:odds-field-sphere-menu:a2`.

**Provenance.**
- Attempt a1 was not delivered: there are no files and no log.
- Definitions come from block 42 (PR #8548), with block 41 (#8547) behind it. Both are by the same model family as me and unrefereed. The reading, that an unformed site's odds are a condition for its neighbours, is supplied by the owner and not adopted.
- The six-axis rule of block 42 is replaced here by the unsoldered sphere menu: contents `s ∈ S²`, pair weight `ω(s, b) = e^{βs·b}`, the uniform measure `dΩ/4π`, `K₁ = ω/Z` with `Z = sinh β/β`, and `Φ(π)_x(s) ∝ ∏_{y∼x}(K₁π_y)(s)`. A record is the point mass at its content.
- Nothing is adopted. No gravitational claim is made.

## 1. What is claimed

> **(a)**
> - **(exact)** `K₁` acts on angular momentum `ℓ` by `λ_ℓ = i_ℓ(β)/i₀(β)` (closed forms for `ℓ ≤ 4`), with `λ₁ = L(β) = coth β − 1/β` and `1 = λ₀ > λ₁ > λ₂ > … > 0`.
> - **(exact)** The derivative of the self-consistent map at the uniform field is `K₁ − P₀` per neighbour. So on a wave `k` the `ℓ`-th channel has eigenvalue `λ_ℓ(6 − E(k))`, as in block 42 T2.
> - **(high precision)** The lean loses its mass term at `6L(β) = 1`, that is **`β_c = 0.50855806178558212314`**.
> - Below `β_c` the lean obeys `(−Δ + m²)v = source/L` with `m² = (1 − 6L)/L`. Its range `1/m` is `0.50`, `1.15`, `3.17` at `β = 0.3, 0.45, 0.5`, and diverges at `β_c`.
>
> **(b)**
> - **The exact equation for the ordered field.** Beyond `β_c` the uniform field is replaced by a field leaning along an axis, `f(s) = f(s·M̂)`, which solves
>
>   **`f = (K₁f)⁶ / ⟨(K₁f)⁶⟩`**.
>
> - **How the lean is born (exact expansion).** With `f = 1 + xP₁ + yP₂ + …` and `M = x/3`:
>   - `y = −10λ₁²x²/(6λ₂ − 1)`;
>   - `x = 6λ₁x + c₃x³ + …` with `c₃ = −6λ₁³(38λ₂ − 3)/(6λ₂ − 1)`;
>   - `c₃ < 0` at `β_c`, so the lean appears continuously with `M² = (6L − 1)/(9|c₃|)`. At `β = 0.515` and `0.53` the numerical lean is `0.1353` and `0.2417`, against `0.1343` and `0.2360` from this formula.
> - **The transverse channel has no mass term at every `β > β_c`.** It is the azimuthal number `m = ±1` about the lean.
>   - Proved: every rotation of the ordered field is again a solution, so the turn of the lean is an eigenvector of the linearised map with eigenvalue exactly `1/6`.
>   - Numeric: the top eigenvalue is `1/6` to twelve digits, and its eigenvector is the turn `f′(t)√(1 − t²)` to twelve digits.
> - **The longitudinal channel (`m = 0`) is massive.** Its `m_L² = 2.21, 7.02, 10.7, 19.1, 24.1` at `β = 0.6, 0.8, 1, 2, 4`. The quadrupole channel (`m = 2`) is massive too.
> - The lean itself is `M = 0.4563, 0.6708, 0.7577, 0.8919, 0.9482` at the same `β`.
>
> **(c) (proved by the symmetry; exact).** The ordered sea keeps the rotations about its lean.
> - A record of content `s` feeds the transverse channel only through the part of `s` perpendicular to the lean. A record aligned with the lean feeds nothing transverse (`P_ℓ¹(±1) = 0`).
> - A record whose content is drawn from the sea's own odds feeds nothing at first order.
> - **The record count, a mass, is a source of no channel without a mass term.** It is invariant under those rotations, so it lives in `m = 0`, which is massive.
>
> **(d) (proved; exact on a box).** In the massless transverse channel a record is a boundary value, and an unformed site obeys `u_x = (1/6)Σ_y u_y`.
> - The field of a body with a common transverse lean is that lean times the probability that a simple random walk ever reaches the body.
> - Its charge is the body's **capacity**, and capacities do not add.
> - This is block 42 T6 with the killing rate `1 − 6λ₁` set to zero.
> - Exact capacities on a `5³` box (field zero beyond it): one record `99/136`; two adjacent `1.1497`; two at distance 2 `1.3469`; a `2×2×2` cube `2.5735` (`0.3217` per record).

## 2. The steps

1. **PROVED + CHECKED (A1).**
   - *Funk–Hecke.* `(K₁Y_ℓm)(s) = λ_ℓY_ℓm(s)` with `λ_ℓ = (1/2)∫e^{βt}P_ℓ(t)dt / Z`. Checked symbolically for `ℓ ≤ 4`, including `λ₁ = coth β − 1/β` (after rewriting in exponentials). Monotonicity was checked at `β = 3/10, 1/2, 1, 3` to 30 digits.
   - *The derivative.* At `π_y = 1 + eδ_y`, with each `δ_y` of mean zero, `∏(1 + eK₁δ_y)` has first-order term `Σ_yK₁δ_y`. `K₁` keeps the mean (`λ₀ = 1`), so the normalisation adds nothing at first order, and the derivative is `Σ_y(K₁ − P₀)δ_y`.

2. **HIGH PRECISION (A2).**
   - `L′(β) = 1/β² − 1/sinh²β > 0`, so `6L = 1` has one root. mpmath at 40 digits finds it, and `6L − 1` changes sign within `10⁻¹⁵` of it.
   - Below `β_c`, `1 − λ₁(6 − E) = λ₁(m² + E)` with `m² = (1 − 6λ₁)/λ₁`, as in block 42 T2(e).
   - Every `λ_ℓ` with `ℓ ≥ 2` is smaller than `λ₁`, so the higher channels are screened wherever the lean is.

3. **NUMERIC (B1): the ordered field.**
   - `f` is represented on Gauss–Legendre nodes, with `K₁` applied through Legendre coefficients (`ℓ ≤ 48`). It is found by iterating the exact equation to a residual below `10⁻¹²`.
   - The linearised map around `f` is `δ ↦ f·(K₁δ)/g − f⟨f K₁δ/g⟩` with `g = K₁f`. For `m ≠ 0` the mean term vanishes by the azimuthal integral. It is diagonalised in each azimuthal sector on normalised associated Legendre functions.
   - Masses follow from `1 − a(6 − E) = a(m² + E)`.

4. **PROVED + NUMERIC (B2): the transverse channel has no mass term.**
   - `Φ` commutes with rotations of all contents, so `f_R(s) = f(R⁻¹s)` is a solution for every rotation `R`.
   - Differentiating `f_R = (K₁f_R)⁶/⟨(K₁f_R)⁶⟩` along a one-parameter turn gives `δ = 6f(K₁δ)/g − 6f⟨fK₁δ/g⟩`. For a turn (`m = ±1`) the mean term vanishes, so `δ` is an eigenvector with eigenvalue `1/6`: the operator `−Δ` with no mass term.
   - *Control below `β_c`:* the field is uniform (`M = 4e−15` at `β = 0.3`) and the transverse top eigenvalue is `6λ₁ = 0.596430581930`.

5. **PROVED + CHECKED (B3): the lean's birth.**
   - Sympy expands the exact equation to third order in `x` (Legendre coefficients of `(K₁f)⁶` normalised, `ℓ ≤ 3`).
   - The sign of `c₃` at `β_c`: `λ₁ = 1/6`, and `λ₂(β_c) ≈ 0.0168 < 3/38`, so `38λ₂ − 3 < 0` and `6λ₂ − 1 < 0`. Hence `c₃ < 0`.
   - The comparison with the numerical lean is within the leading correction.

6. **PROVED + CHECKED (C1): what a record and a mass feed in.**
   - The residual symmetry of the ordered sea is `O(2)` about `M̂`. A source feeds the azimuthal sector `m` only through its `m`-th Fourier part about the lean.
   - The point mass at `s₀` has `m = ±1` part `Σ_ℓ P_ℓ¹(s₀·M̂)Y_ℓ^{±1}`. Since `P_ℓ¹(t) = −√(1 − t²)P_ℓ′(t)`, it vanishes at `t = ±1` (checked exactly for `ℓ ≤ 7`) and not elsewhere.
   - A content drawn from `f` averages to `f`, so it gives no first-order source.
   - A content-blind source is `O(2)`-invariant, hence purely `m = 0`, and the `m = 0` sector's top eigenvalue is below `1/6` at every `β` computed.

7. **PROVED + CHECKED (D1): records are boundary values.**
   - The argument of block 42 T6(a), (b) with `6λ = 1`: `u = h_S`, the hitting probability; the charge is `μ_S = u − (1/6)Adj u`, supported on `S`; the capacity is `Σμ_S`, which is sub-additive.
   - Checked on a `5³` box by an exact rational solve.

## 3. Where this stops

- **(a) and (b) are complete at the stated precision.** The ordered field is numeric; its equation and its birth are exact.
- **(c)'s answer is a no-go by symmetry.** The mass sources no massless channel. The one massless channel is sourced only by misaligned content, and there a body is a boundary value with a capacity (d).
- **Not examined:**
  - the density channel with "no record" as a seventh possibility (block 42 T5's analogue for the sphere);
  - the nonlinear transverse field around a misaligned record (a control like block 42's);
  - stability beyond the linear level.

## 4. What would finish it

1. The seven-outcome (density) channel for the sphere at the neutral scale `c₀ = β/sinh β`: does its first-order strength vanish there, as in block 42 T5?
2. A nonlinear control: the transverse field around one held misaligned record in the ordered sea, with `r·v(r)` flat, against (d).
3. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/odds-field-sphere-menu/w-jonathonsmac4f50-jff2b/check.py
```

- It has 7 lines:
  - A1, C1, D1 are exact (sympy);
  - A2 is high precision (mpmath, 40 digits);
  - B1 is numeric (double precision on a Legendre basis);
  - B2 and B3 are proofs, with numeric checks.
- It runs in about 20 seconds.
