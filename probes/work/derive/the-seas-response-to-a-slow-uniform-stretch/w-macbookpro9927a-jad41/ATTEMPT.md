# The sea's response to a slow uniform stretch: an exact inertia, positive at every mass, never the member's form

Worker `w-macbookpro9927a-jad41` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in about 8 seconds with a peak of about 75 MB, on one thread.

The families are:
- **P**: the operator identity.
- **M**: the cubic parts.
- **H**: the hopping coefficients.
- **L**: the Laplace and series representation.
- **R**: the interval certificates.
- **K**: the member's form.

P, M, H, L and K are exact (fractions and sympy). R is interval arithmetic with outward rounding (mpmath `iv`, ASSUMED A1). There are no floating-point claims.

## Sources, provenance and overlap

**The setting** is quoted from the task.
- Block 54's walk with block 139's staggered mass: `H(h) = Σ_a σ_a e_a^i(h) sin k_i + μ(−1)^{x1+x2+x3}`, with `e = (1+h)^{−1/2}`.
- The half-filled sea.
- The cranking inertia `M = 2 Σ |⟨p|dH|h⟩|²/ΔE³`.

**Block 139 as landed on main** (`ef918c1910`, `docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_…_2026-09-25.md`). It gives the walk with rest energy as `H + mε`, where `ε(x) = (−1)^{x₁+x₂+x₃}`, and states "`m ε` anticommutes with `H`, so `(H + m ε)² = H² + m²`". Here `m` is written `μ`. P2 re-checks the anticommutation exactly.

**Block 146** (PR #9237, open, read on its branch). It gives the member's kinetic term `α tr(Ḣ²) + β(tr Ḣ)²` (blocks 124 and 134–136). On a uniform stretch `h = 2λδ` its value is `c_k λ̇²` with `c_k = 12α + 36β`, which is `−24α` at the closing ratio `β = −α`. K1 recomputes both numbers.

**Provenance.** The claim printed no prior attempts on this problem. One earlier unit of mine overlaps it:
- **#9198** ("what the walker's sea induces in the member", `w-macbookpro9927a-j5403`). This was block 62's framed walk at `μ = 0`. It gave the massless sea's inertia as `T = (1/32)[B′ tr ḣ² − A′(tr ḣ)² − (B′ − 3A′) Σ ḣ_ii²]`. The values were floats: `A′ = ⟨s₁²s₂²/r⁵⟩ = 0.0731096`, `B′ = ⟨s₁⁴/r⁵⟩ = 0.1573435` and `B′ − 3A′ = −0.06199`.
- In this note's notation, `Q_E/Q_T = 3A′/B′` and `D(0) = 2(3A′ − B′)`. So R1 and R2 turn #9198's floating-point anisotropy into certified intervals: `3A′ − B′ = D(0)/2 ∈ [0.061935, 0.062042]`.
- Everything else here is new:
  - the staggered mass `μ ≠ 0`;
  - the operator identity;
  - the exact per-mode formula at every `μ`;
  - the exact hopping coefficients;
  - the sign of `D` at every `μ`;
  - the comparison of a positive response with the member's indefinite form.

## Definitions

**The operators.** `S_i = sin P_i = (T_i − T_i†)/(2i)`, with `(T_iψ)(x) = ψ(x + e_i)`, on `Z³` or on an even periodic box. `Γ = (−1)^{x₁+x₂+x₃}`. `s = (S₁, S₂, S₃)`, and on a plane wave `s_i = sin k_i`. We write `x_i = s_i²`, `E² = |s|² + μ²`, and `⟨·⟩` for the Brillouin-zone average.

**The stretch.** `e = (1+h)^{−1/2} = 1 − h/2 + O(h²)`. So for a symmetric direction `δh`, `dH = X = σ·b` with `b = −½ δh s`. Measured instead by the frame displacement `δe` (`e = 1 + δe`), `b = δe s`.

**The inertia.** Per site, `m(δh) = M/N`. The cubic parts use unit directions of Frobenius norm² 2 for the traceless ones:
- `T₂`: `δh = e₁e₂ᵀ + e₂e₁ᵀ`;
- `E`: `δh = diag(1, −1, 0)`;
- `A₁`: `δh = 1` (the dilation).

Their values are `m_T`, `m_E` and `m_A`.

**The anisotropy function.** `D(μ) = ⟨2w/E⁵⟩`, with `w = 2x₁x₂ − ½(x₁ − x₂)²`.

**The member's variables.** A cubic-invariant quadratic form is written `Q(ḣ) = a tr ḣ² + b (tr ḣ)² + c Σ_i ḣ_ii²`. Here `c` is the cubic-only term. The member's family is `c = 0`, with `a = α`, `b = β`.

## (1) The statement attempted

For every `μ ≥ 0`, for the half-filled sea:

- **(a) The inertia.** It is `m(δh) = ⟨(|s × δh s|² + μ²|δh s|²)/(16E⁵)⟩`. This is positive semidefinite, and positive on every traceless `δh ≠ 0`. Its dilation part is `m_A = ⟨μ²|s|²/(16E⁵)⟩`, which vanishes if and only if `μ = 0`.
- **(b) The splitting.** `m_E − m_T = ⟨w/(8E⁵)⟩ = D/16` per unit `δh`, and `D/4` per unit `δe`. For `μ² > 3`, `D = (3/4)μ⁻⁵ − (65/16)μ⁻⁷ + (8155/512)μ⁻⁹ − (113085/2048)μ⁻¹¹ + (11823735/65536)μ⁻¹³ − …`.
- **(c) The sign of `D`.** `D(μ) > 0` for every `μ ≥ 0`, and `D(0) ∈ [0.12387, 0.12408]`.
- **(d) The member's variables at `μ = 0`.** `b/a = −(1 + c/a)/3` exactly, with `c/a ∈ [0.3936, 0.3943]` and `b/a ∈ [−0.4648, −0.4645]`.
- **(e) The member's form.**
  - At `β = −α` the member's form is `−24αλ̇²` on the dilation and `+2α` on a unit shear. So it is indefinite for every `α ≠ 0`.
  - No positive semidefinite form, and no positive sum of such forms, equals it.
  - By (c), the sea's form has `c = (m_E − m_T)/2 > 0` at every `μ`. So it lies outside the member's family even on the traceless directions, where the member's form is isotropic (`m_E = m_T`).

## (2) Steps

**Step 1 (PROVED; CHECKED P1, P2): the operator identity.**

*The algebra.* The `S_i` are Hermitian and commute. `Γ² = 1`, and `ΓT_i = −T_iΓ`, so `ΓS_i = −S_iΓ`. The components of `b` are linear in the `S_i`. Hence:
- `H = σ·s + μΓ`;
- `(σ·s)² = |s|²`;
- `{σ·s, Γ} = 0`.

So `H² = |s|² + μ² = E²`, and `E²` commutes with every `S_i`, every `σ_a` and `Γ`.

*The Inglis sum as a trace.* `X` commutes with `E²`, so it preserves each eigenspace of `E²`. Within an eigenspace the states are `±E`. Hence every pair `(p, h)` has `ΔE = 2E`, and
`Σ_{p,h} |⟨p|X|h⟩|² g(ΔE) = Tr(P₊ X P₋ X g(2E))`, with `P± = ½(1 ± H/E)`.

For `μ > 0`, `E ≥ μ > 0`. At `μ = 0` the states with `s = 0` form a null set per site.

*Expanding.* By cyclicity and `[E, X] = 0`, the terms linear in `H` cancel. So
`Tr(P₊XP₋X g) = ¼ Tr[(E²X² − (HX)²) g/E²]`.

Write `C = (σ·s)(σ·b)`. Then `(HX)² = C² + μΓ(CX + XC) + μ²ΓXΓX`, and `ΓXΓX = −X²`:
- `CΓ = ΓC`, because `C` carries two factors that each anticommute with `Γ`.
- `Tr(Γ Y f) = 0` for any `Y` and `f` built from `σ` and the `S_i`. Those are diagonal in the plane waves, while `Γ` sends `k` to `k + (π, π, π)`.

At fixed `k`:
`Tr_spin[E²X² − C² + μ²X²] = 4(|s × b|² + μ²|b|²)` (P1).

*The formula.* With the task's weight `g(ΔE) = 2/ΔE³`:
`M = Σ_k (|s × b|² + μ²|b|²)/(4E⁵)`.

Per site, with `b = −½δh s`, this is (a)'s formula.

*The exact check.* P2 checks the full-space identity `Tr(E²X² − (HX)²) = 4 Σ_k(|s × b|² + μ²|b|²)` exactly, Γ-terms included. It uses the periodic `4³` lattice (128 states, `sin k ∈ {0, 1, 0, −1}`), `μ ∈ {0, 1, 2/3}` and four stretches (`T₂`, `E`, `A₁` and a generic rational one), with Gaussian-rational matrices.

**Step 2 (PROVED; CHECKED M1, M3): positivity and the dilation.**
- Both terms of the integrand are non-negative, so `m` is positive semidefinite for every `μ`.
- `s × (δh s) ≡ 0` holds if and only if `δh = λ1` (M3). So for traceless `δh ≠ 0`, `|s × δh s|²` is a nonzero polynomial. It is positive on an open set, so `m > 0`.
- For `δh = 1`, `s × s = 0`, so `m_A = ⟨μ²|s|²/(16E⁵)⟩`. This is zero if and only if `μ = 0`.
- Directly: at `μ = 0`, `H(ε1) = (1+ε)^{−1/2} H(0)`. The eigenvectors do not move, so no interband element exists.
- M1 checks that `|δh s|²` is the same for `E` and `T₂`, and that `|s × E s|² − |s × T s|² = 2w`. So `m_E − m_T = ⟨2w/(16E⁵)⟩`.

**Step 3 (PROVED; CHECKED M2, M4): the cubic form and the member's variables.**
- The integrand is invariant under `(s, δh) → (Ps, PδhPᵀ)` for the 48 signed permutations. The Brillouin-zone measure is invariant under `k → Pk`, since `sin` is odd.
- The invariant quadratic forms on symmetric 3×3 matrices form a 3-dimensional space, spanned by `tr h²`, `(tr h)²` and `Σ h_ii²` (M2, solved exactly).
- On the three unit directions, `Q` takes the values `Q_T = 2a`, `Q_E = 2(a + c)` and `Q_A = 3a + 9b + 3c` (M4).
- At `μ = 0`, `Q_A = 0`, so `b/a = −(1 + c/a)/3` exactly.

**Step 4 (PROVED; CHECKED H1, H2): the hopping expansion.**
- For `μ² > 3`, `E⁻⁵ = μ⁻⁵ Σ_n C(−5/2, n)(|s|²/μ²)^n` converges uniformly, since `|s|² ≤ 3`.
- The axes are independent under the uniform measure, with `⟨x^n⟩ = C(2n, n)/4^n` (H1 checks `n ≤ 6` by direct integration).
- H1 gives the five coefficients in (b). The first two are the quoted `3/4` and `−65/16`, and their ratio is `−65/12`.
- H2 checks the normalisations: `m_E − m_T` is `D/16` per unit `δh` and `D/4` per unit `δe`. The factor is common to all three parts, so no ratio or sign depends on it.

**Step 5 (PROVED; CHECKED L1, L2): the Laplace representation.**

*The representation.* For `E > 0`, `E⁻⁵ = Γ(5/2)⁻¹ ∫₀^∞ t^{3/2} e^{−tE²} dt`. The averages may be exchanged (Fubini), because:
- `|w| ≤ 3x₁x₂ + ½(x₁² + x₂²) ≤ (3/2)|s|⁴`, so `|w|/E⁵ ≤ (3/2)/|s|`;
- near each of the eight zeros of `s`, `|s| ≥ (2/π)|k − k₀|`.

The integrand factorises over the axes. With `f_p(t) = ⟨x^p e^{−tx}⟩` (L2):
- `⟨w e^{−t|s|²}⟩ = 3f₁²f₀ − f₂f₀² =: A − B`;
- `D(μ) = (2/Γ(5/2)) ∫₀^∞ t^{3/2} e^{−tμ²}(A − B) dt`.

At `μ = 0`:
- `Q_E` and `Q_T` are the same multiple of `I_A = ∫t^{3/2}A` and `I_B = ∫t^{3/2}B`;
- so `Q_E/Q_T = I_A/I_B`.

*The series.* With `θ = 2k` uniform, `x = (1 − cos θ)/2` and `z = t/2`:
- `f₀ = e^{−z}S₀`;
- `f₁ = ½e^{−z}(S₀ − S₁)`;
- `f₂ = ¼e^{−z}(S₀ − 2S₁ + S₂)`.

Here `S_j = ⟨cos^jθ e^{z cos θ}⟩`, expanded termwise with `⟨cos^{2m}θ⟩ = C(2m, m)/4^m`. The terms are:
- `S₀`: `z^{2m}/(4^m m!²)`;
- `S₁`: `z^{2m+1}/(2·4^m m!(m+1)!)`;
- `S₂`: `z^{2m}(2m+2)(2m+1)/((m+1)!² 4^{m+1})`.

All terms are positive. L1 checks the identities to order `t¹²` against `Σ(−t)^n⟨x^{p+n}⟩/n!`. The ratio of consecutive terms is `z²ρ_m`, with `ρ_m` decreasing in `m` (L1). So once `z²ρ_m < 1`, the remainder after term `m` is at most `T_{m+1}/(1 − z²ρ_m)`.

**Step 6 (PROVED): the brackets and the tails.**

*Shape of the integrands.*
- `f_p = ∫x^p e^{−tx} dρ(x)` is positive and decreasing, since `f_p′ = −f_{p+1}`.
- It is log-convex. By Cauchy–Schwarz, `(f_p′)² ≤ f_p f_p″`.
- Products of positive, decreasing, log-convex functions keep all three properties, and `e^{−tν}` has them too.
- So `F = Ae^{−tν}` and `G = Be^{−tν}` are convex and decreasing.

*The brackets.* On a cell `[t_i, t_{i+1}]`, with weight `t^{3/2}`, let `W_i = ∫t^{3/2}` and `c_i = ∫t^{5/2}/W_i`.
- Jensen gives `∫t^{3/2}F ≥ W_i F(c_i) ≥ W_i F(c̄_i)`, for a machine number `c̄_i ≥ c_i`.
- Convexity gives the chord bound `∫t^{3/2}G ≤ W_i[(1 − λ_i)G(t_i) + λ_i G(t_{i+1})]`, with `λ_i = (c_i − t_i)/(t_{i+1} − t_i)`.

*Upper tail bounds.* Write `f_p = π⁻¹∫₀¹ x^{p−½}(1−x)^{−½}e^{−tx} dx`.
- On `[0, ½]`, `(1−x)^{−½} ≤ 1 + 2(√2 − 1)x` (chord of a convex function).
- On `[½, 1]`, `e^{−tx} ≤ e^{−t/2}`, with integral `π/2` for `p = 0` and at most `√2` for `p ≥ 1`.
- `e^{−t/2}t^{p+½}` decreases for `t ≥ 2p + 1`.
- So for `t ≥ T ≥ 5`, `f_p ≤ κ_p t^{−p−½}` with `κ_p = (Γ(p+½)/π)(1 + (2p+1)(√2−1)/T) + c_p e^{−T/2}T^{p+½}`, where `c₀ = ½` and `c_{1,2} = √2/π`.

*Lower tail bounds.*
- `(1−x)^{−½} ≥ 1`.
- `∫₁^∞ x^{p−½}e^{−tx} dx ≤ e^{−t/2}Γ(p+½)(2/t)^{p+½}`.
- So `f_p ≥ λ_p t^{−p−½}` with `λ_p = (Γ(p+½)/π)(1 − 2^{p+½}e^{−T/2})`.

*The tail integrals.* So `∫_T^∞ t^{3/2}A ∈ [3λ₁²λ₀, 3κ₁²κ₀]/T` and `∫_T^∞ t^{3/2}B ∈ [λ₂λ₀², κ₂κ₀²]/T`. For `ν > 0` the lower tail is replaced by 0 and the upper by `e^{−Tν}` times the bound.

**Step 7 (CHECKED R1–R3, H3): the certificates.**

*The grid.* The cells are `t ∈ [0, 1]` in steps of `1/256`, then a factor `65/64` per cell up to `T = 400.5`: 635 cells in all. At every node and every `c̄_i`, the value comes from Step 5's series with a rigorous remainder, at 110 bits.

*R1.*
- `I_A ∈ [0.291535, 0.291618]` and `I_B ∈ [0.209143, 0.209204]`.
- So `D(0) = 2(I_A − I_B)/Γ(5/2) ∈ [0.12387, 0.12408]`, and `D(0) > 0`.

*R2.*
- `Q_E/Q_T ∈ [1.39355, 1.39434]`.
- Hence `c/a ∈ [0.3936, 0.3943]` and `b/a ∈ [−0.4648, −0.4645]`.

*R3.*
- For `ν = μ² ∈ [ν₀, ν₁]`: `D ≥ (2/Γ(5/2))(∫t^{3/2}e^{−tν₁}A − ∫t^{3/2}e^{−tν₀}B)`.
- The lower bracket is positive on 25 cells covering `[0, 16]`. The cells are adaptive, and the least margin is `1.5·10⁻⁴`.

*H3.* For `ν ≥ 16`, Taylor with remainder gives `(1+y)^{−5/2} = 1 − (5/2)y + R`, with `0 ≤ R ≤ (35/8)y²`. Hence
`D ≥ 2μ⁻⁵[3/8 − (65/32)/ν − (35/8)W⁺/ν²]`, where `W⁺ = ⟨(3x₁x₂ + ½x₁² + ½x₂²)|s|⁴⟩ = 583/128`.
The bracket equals `44619/262144 > 0` at `ν = 16`, and it increases with `ν`.

So `D(μ) > 0` for every `μ ≥ 0`.

**Step 8 (PROVED; CHECKED K1, K2): the member's form against a positive response.**
- On `ḣ = 2λ̇1`: `α tr ḣ² + β(tr ḣ)² = (12α + 36β)λ̇²`, which is `−24αλ̇²` at `β = −α`.
- On the unit shear `T₂`: `+2α`.
- The product of the two values is `−48α²`. So for every `α ≠ 0` the form takes both signs.
- A positive semidefinite form, or any positive sum of them, takes no negative value. So none equals the member's form, and neither does its negative, which takes no positive value.
- Moreover, by Step 7 the sea's `c = (Q_E − Q_T)/2 = D/32` per unit `δh` is positive at every `μ`. So the sea's form is not in the member's family even after its dilation part is removed.

**The quoted claims, item by item.**

| quoted | here |
|---|---|
| `M` positive semidefinite | holds (Step 2), and is positive on every traceless stretch |
| dilation part vanishes at `μ = 0` | holds (Step 2), and is positive for every `μ > 0` |
| `m_E − m_T = D/4` | holds exactly per unit frame displacement `δe`; per unit `δh` it is `D/16` (a common factor) |
| `D = (3/4)μ⁻⁵ − (65/16)μ⁻⁷ + O(μ⁻⁹)` | holds exactly; the next three coefficients are in (b) |
| `D(0) ≈ 0.124` | `D(0) ∈ [0.12387, 0.12408]`, and `D > 0` at every `μ` |
| cubic-only term `≈ +0.39α` | `c/a ∈ [0.3936, 0.3943]` |
| `β/α ≈ −0.47` | `b/a ∈ [−0.4648, −0.4645]`, which is `−0.465` to three digits; the quoted second digit is off |

## ASSUMED

- **A1.** mpmath's interval arithmetic (`iv`) returns an interval containing the exact result for `+`, `−`, `×`, `÷`, `sqrt`, `exp` and `π` (outward rounding). Family R depends on it. Where an interval comparison is undecided, the code counts it as a failure, and a cell is then subdivided.
- **A2.** The cranking formula is the task's definition of the inertia: leading adiabatic order, at `h = 0`, first order in the stretch. At `μ = 0` the sea is gapless at eight points. The integral converges there, since the integrand is at most a constant times `1/|s|`. Whether leading-order adiabatic response is the right physics for a gapless sea is not addressed.

## (3) Where the route stops

No step fails. The scope is:
- a uniform stretch, at first order about `h = 0`;
- the half-filled sea of the stated walk with the staggered mass;
- the task's normalisation of `M`.

No gravitational identification is made.

## (4) What would extend it

- Certified curves `c/a(μ)` and `b/a(μ)` for all `μ`, not only at `μ = 0`. The same brackets apply to `Q_T`, `Q_E` and `Q_A` separately.
- The response at a stretched background `h ≠ 0`.
- The `q`-dependent response of the same sea, as in #9198's `q²` part, with the staggered mass.
