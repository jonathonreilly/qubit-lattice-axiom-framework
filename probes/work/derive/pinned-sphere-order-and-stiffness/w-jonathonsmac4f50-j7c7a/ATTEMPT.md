# pinned-sphere-order-and-stiffness, attempt 4 of 5: at the pinned scale the domination route closes, now for the sphere menu itself

Worker `w-jonathonsmac4f50-j7c7a` (`claude-opus-5-5`), unit `J-derive-pinned-sphere-order-and-stiffness:a4`.

**Provenance.**
- No attempt of this problem had been delivered: a1–a3 left nothing on `ai/probes`.
- The closest prior work is my own attempt on the sibling problem `moving-kernel-with-vacancies:a1` (issue #8616). It was
  written in this session by the same model family and is unrefereed.
  - It proved a split domination with strength `β − γ(c)`, which is zero at the pinned scale.
  - It gave an exact two-valued counterexample on the 2×2×2 torus, and only **numerical** evidence for the sphere menu.
- This attempt takes the step that attempt left open, for this problem's own menu. It adds:
  - a **rigorous** certificate that the full-`β` infrared bound is false for the **sphere** menu at `c₀`;
  - a no-go for a wider family of embeddings of the empty state;
  - the literal "records-only" reading of (b).
- Definitions come from the task, block 39 (PR #8530: T5) and block 19 (PR #8153: the template).
- Classical imports are marked ASSUMED: the Funk–Hecke theorem, the dipole selection rule, and the power series of `i_ℓ`.

## 1. What is claimed

**Setting.**
- A site is empty or holds a record `s`, with `s ∈ S²` (sphere, uniform probability measure) or `s = ±1` (two-valued). A
  record weighs `z`.
- Bond kernel: `B(∅,·) = 1` and `B(s,s') = c e^{βs·s'}`.
- The pinned scale is `c₀ = β/sinh β` (sphere) or `1/cosh β` (two-valued).
- The field is `σ_x = n_x s_x`, and `S^e(k) = ⟨|σ̂^e(k)|²⟩`, with `E(k) = Σ 2(1 − cos k_i)`.

> **(a) (exact).** `[[1, 1], [1, c e^{βs·s'}]]` is positive semidefinite exactly when `c ≥ c₀`. The eigenvalues of `e^{βs·s'}` are
> `i_ℓ(β) > 0`, and the constant mode's eigenvalue is `i₀ = sinh β/β`. This is block 39's T5, re-derived.
>
> **(b) ROUTE FAILS at the pinned scale.**
> 1. *No twist strength survives.* Embed records as `(s, 0)` and the empty state as `(0, h) ∈ R^{3+m}`: this covers every
>    rotation-symmetric position, and `h = 0` is block 19's and #8616's twist. Split
>    `B = f f' e^{−(β'/2)|σ−σ'|²} R`. The remainder `R` is positive semidefinite **iff** `c ≥ e^{β'h²} c₀(β − β')`. `c₀` is
>    strictly decreasing, so at `c = c₀(β)` only `β' = 0` is allowed.
> 2. *The bound (b)–(c) would deliver is false.* On the 4-ring, an even 1D torus where the argument would give
>    `S(k) ≤ 1/(βE(k))`, at `k = π`:
>    - **sphere**, `β = 8`, `z = 1`: `4β S(π) > 1.977921` (rigorous);
>    - **two-valued**, `e^β = 20`, `z = ½`: `S(π) = 77831376023/439056344017` exactly, and `4βS(π) > 2.1242`.
>
>    The full-lattice limit `z → ∞` respects the bound (`0.688` at `β = 8`, numeric). It is the vacancies at the pinned scale
>    that break it.
> 3. *The literal reading* ("twist only record–record bonds"):
>    - Its crossing kernel is **not** positive semidefinite across two shifts: at `e^β = 3` with shifts `{0, 2}`, the form is
>      `−6559/3645`, although each single-shift block is.
>    - Even a valid domination would bound a record-bond sum that is not the structure factor (#8616 X3).
>
> **(c) The constants, conditional.** Per component, `S^e(k) ≤ 1/(β'E(k))`, and the sum rule is `Σ_e Σ_k S^e(k) = Nρ` (exact).
> Together these give `M² ≥ ρ − (3/β') N⁻¹ Σ_{k≠0} 1/E(k) → ρ − 3G(0)/β'` with `G(0) = 0.2527 ≤ √3π/8`, and long-range order for
> `β'ρ > 3G(0)`. **At `c₀`, `β' = 0`**, so (c)–(e) get no constants from this route.

## 2. The steps

1. **PROVED + CHECKED (A1): (a).**
   - Two-valued: `c e^{βss'} − 1 = (c cosh β − 1) + c sinh β · ss'`. All principal minors are checked at `c₀` (singular) and at
     `c₀ ± 1/1000`, for `e^β = 3, 20`.
   - Sphere: by Funk–Hecke (**ASSUMED**), `e^{βs·s'}` has eigenvalue `i_ℓ(β) = ½∫e^{βt}P_ℓ(t)dt` with multiplicity `2ℓ+1`.
     - Its power series `β^ℓ Σ_k (β²/2)^k/(k!(2ℓ+2k+1)!!)` has positive terms. This is checked against the integral and against
       the recurrence `i_{ℓ+1} = i_{ℓ−1} − (2ℓ+1)i_ℓ/β` for `ℓ ≤ 4`; the general series is **ASSUMED** (DLMF 10.53.3).
     - The Schur complement on the empty entry is `c e^{βs·s'} − 1`. Its constant mode is `c i₀ − 1`, and its higher modes
       `c i_ℓ` are positive.
2. **PROVED + CHECKED (B1): no-go for the embedding family.**
   - Rotation symmetry makes `f` constant on records. Then `R(s,s') = (ce^{β'}/f²) e^{γ s·s'}` with `γ = β − β'`,
     `R(∅,s) = e^{(β'/2)(1+h²)}/(f_∅ f)` and `R(∅,∅) = 1/f_∅²`.
   - `R` is positive semidefinite iff its Schur complement on `∅` is, and that complement is
     `f⁻²(c e^{β'} e^{γ s·s'} − e^{β'(1+h²)})`. By step 1 this holds iff `c e^{β'} i₀(γ) ≥ e^{β'(1+h²)}`, that is
     `c ≥ e^{β'h²}/i₀(γ) = e^{β'h²} c₀(γ)`.
   - At `c = c₀(β)` this requires `i₀(β − β') ≥ e^{β'h²} i₀(β)`, and `i₀` is strictly increasing, so `β' ≤ 0`.
   - Checked exactly in the two-valued form (`cosh` for `i₀`) at four parameter points, with rational exponents.
3. **CHECKED, exact (B2): the two-valued witness.** Enumerate all 81 configurations of the 4-ring. The certificate is
   `4 · log(20) · S(π) > 1`, using a rational lower bound on `log 20 = 2 atanh(19/21)` from partial sums.
4. **PROVED (reduction) + CHECKED (B3), rigorous: the sphere witness.**
   - On the 4-ring at `c₀`, an occupied tree weighs `(c₀ i₀)^{#bonds} = 1`.
   - The full ring weighs `LF = Σ_ℓ (2ℓ+1) r_ℓ⁴`, with `r_ℓ = i_ℓ/i₀`.
   - For the ring's correlations use the dipole selection rule (**ASSUMED**): `s^a` couples `ℓ` to `ℓ ± 1`, with total weight
     `Σ|⟨ℓ+1|s|ℓ⟩|² = ℓ+1`. The identity `(2ℓ+1)(2ℓ+3)(ℓ 1 ℓ+1; 0 0 0)² = ℓ+1` is checked exactly for `ℓ < 12`. This gives
     `Z⟨s₀·s₁⟩ = Σ(ℓ+1)(r_ℓ³r_{ℓ+1} + r_ℓ r_{ℓ+1}³)` and `Z⟨s₀·s₂⟩ = Σ 2(ℓ+1) r_ℓ² r_{ℓ+1}²`.
     The two-site case reproduces the Langevin function `L(2β)` to 30 digits (numeric control).
   - Collecting the 16 occupancy patterns at `z = 1`:
     `S(π) = (7 + LF − 6r₁ − 2A + 2r₁² + O)/(3(15 + LF))`.
   - *Certificate.*
     - `i_ℓ(8) = a_ℓ sinh 8 + b_ℓ cosh 8`, with exact rationals `a_ℓ, b_ℓ` from the recurrence.
     - `r_ℓ = 8a_ℓ + 8b_ℓ coth 8`, with rational bounds on `coth 8` from a Taylor bound on `e^{16}` with remainder.
     - For `ℓ ≤ 30`, each `r_ℓ` is clamped to `[0, 1]`. Beyond, `r_ℓ ≤ (8^ℓ/(2ℓ+1)!!) e^{64/(4ℓ+6)} (8/sinh 8)`, bounded
       rationally using `e^8 > 2980` and `e < 25/9`. Successive tail terms fall by at least half.
     - The lower bound of `4βS(π)` is an exact rational, `> 1.977921`.
5. **CHECKED, exact (B4): the literal reading.** The kernel on `{∅, +1, −1} × {0, 2}` at `e^β = 3`, `c₀ = 3/5` is rational,
   because `q^{−d²/2}` with `d` even is rational. The vector `(−1, 1, ½, −1, ½, 1)` gives the form `−6559/3645`, and each
   single-shift block is positive semidefinite. X3 (#8616) is re-checked: the record-bond term is 0 against `E(k)Σσψ = 2`.
6. **PROVED + CHECKED (C1): (c)'s constants.**
   - Parseval: `Σ_k |σ̂^e(k)|² = Σ_x (σ^e_x)²`, and summing over `e` gives `Σ_x n_x`. The exact values `S(k)` on the 4-ring sum to
     `4ρ`.
   - The lower bound on `M²` is block 19's G3, with the density entering the sum rule.
   - At `c₀` step 2 forces `β' = 0`, so the bound is vacuous there.
7. **Remark (not claimed): the mechanism.**
   - At `c₀` an empty neighbour weighs what a record of random content weighs on average, so at moderate density the records are
     nearly free. `S(k)` then stays of order `ρ/3` at every `k`, which defeats `1/(βE(k))` once `β ≳ 1/(ρE_max)`.
   - In the full lattice, `z → ∞`, the law is block 19's (the factor `c₀^{#bonds}` is constant) and the bound holds.

## 3. Where this stops

- **(b) fails at the pinned scale**, and so does every conclusion (c)–(e) that was to come from it:
  - within the rotation-symmetric embedding family, for any `β' > 0`;
  - as an inequality for the full `β`, for both menus, with exact or rigorous witnesses.
- **Not shown.**
  - That long-range order is absent at `c₀`.
  - That no other route (not reflection-positivity–Gaussian domination) gives it.
  - The stiffness (e) at `c₀`. The exact rings show only that the naive coefficient `1/β` is exceeded at the zone boundary.
- The witnesses are rings and small tori. They refute an inequality that the argument would deliver on every even torus, and say
  nothing directly about infinite-volume order.

## 4. What would finish it

1. A route to order at `c₀` outside Gaussian domination. For example, at large `β` and `z`, where vacancies are suppressed by
   `≈ (2β)⁻⁶` per site: a chessboard estimate for vacancies combined with spin-wave control on the occupied set.
2. The stiffness at `c₀` from the actual law. The transverse structure factor at small `k` on large tori (numerics first), and
   whether the coefficient approaches `ρ²/(β σ_eff(ρ))` with `σ_eff` the effective conductance of the occupied network, or
   something else.
3. Theorem B of #8616 (small twists, full `β` above `c₁ > c₀`) for the sphere menu, with a proof in place of numerics.
4. A referee from another model family, on this attempt and on #8616.

## 5. Running it

```
python3 probes/work/derive/pinned-sphere-order-and-stiffness/w-jonathonsmac4f50-j7c7a/check.py
```

- It has 6 checks, exact or rigorous: `fractions`, `sympy`, and rational interval bounds for the sphere certificate.
- `mpmath` is used only for the Langevin control, and floats only for printing.
- It runs in about 3 seconds.
