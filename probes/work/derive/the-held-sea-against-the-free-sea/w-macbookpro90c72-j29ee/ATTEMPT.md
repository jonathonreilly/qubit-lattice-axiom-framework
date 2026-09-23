# J:derive:the-held-sea-against-the-free-sea:a1 — the free sea's second-order deficit below the held sea is an exact zone integral of order |q|⁴ log(1/|q|): both seas have the clock stiffness I/12 = 0.0995; block 76's 0.095 is a torus value

**Provenance.**
- Worker `w-macbookpro90c72-j29ee`, model `claude-opus-5-5`, one session. The claim printed no prior attempts.
- Objects come from:
  - the task statement;
  - harvest issue #8647 (the held sea, `the-field-energy-as-a-clocked-amplitude:a3`);
  - issue #8630 (a1, the free sea on a line);
  - block 76's note on PR #8611's branch: `docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_…_2026-09-22.md`, which supplies `H_w = φHφ`, `φ = e^{u/2}`, `E_sea` and the normalisation of `Π(q)` and `κ`.
- My plan was second-order perturbation theory for the difference, with the Dirac points' phase space counted. I formed it after reading #8647 and #8630 and before reading block 76's executed table.
- Every clause is supplied; nothing is adopted.

## 1. The statement attempted

**Objects.**
- **The walk.** `H = Σ_a σ_a S_a`, with `(S_a ψ)(x) = (1/2i)[ψ(x + e_a) − ψ(x − e_a)]` (block 54's `D_a`). Its symbol is `H(k) = s(k)·σ` with `s(k) = (sin k₁, sin k₂, sin k₃)`. The eigenvalues are `±|s(k)|`, with eigenvectors `u_±(k)`.
- **The clocked walk.** `H_w = φHφ` with `φ = e^{u/2}`, so `w = φ²`.
- **The held sea.** `E_fix[φ] = tr(P₋ φHφ)`, where `P₋` is the lower band of `H` (#8647).
- **The free sea.** `E_opt[φ] = Σ_{λ<0} λ(φHφ)`, the sum of the negative eigenvalues (block 76's `E_sea`).
- **The normalisation (block 76).**
  - For `u = ε cos(q·x)`: `E(ε) − E(0) = Π(q) ε² N + O(ε³)` per site.
  - `Π(q) = c₀/4 + (κ/4)|q|²_lat + …`, with `|q|²_lat = Σ_a 2(1 − cos q_a)`.
  - `κ` is the coefficient of `½Σ_bonds(u_x − u_y)²`, and block 76's `γ = 1/κ`.
  - Block 76 executed `κ = 0.0952 ± 0.0016` on tori up to `12³`.
- **Zone quantities.**
  - `I = ∫ |s(k)| d³k/(2π)³ = 1.19380` (numeric, a note).
  - On the `L`-torus, `I_L = (1/N) Σ_k |s(k)|` and `β_L = −I_L/3`.

**Claims.**
- **(a) The kernel.** For `2q ≢ 0`, the second-order kernel of `E_opt − E_fix` is exactly

  `ΔΠ(q) = Π_opt(q) − Π_fix(q) = −(1/8) ∫ d³k/(2π)³ F(k, q)`,

  `F(k, q) = [(a − b)²/(a + b)] · (1 − ŝ(k+q)·ŝ(k))/2`,  with `a = |s(k+q)|`, `b = |s(k)|`, `ŝ = s/|s|`.

  - **Sign.** `ΔΠ(q) < 0` for `q ≠ 0`.
  - **Bounds.** For `0 < t ≤ 1/8`:

    `C t⁴ log(1/(4t)) ≤ −8 ΔΠ(t e₁) ≤ π t⁴ (1/6 + ½ log(√3/t))`,

    with the bound on the right valid for every direction and every `|q| < √3`, and `C = δ_c⁴ (23/24)⁴ · 16/(16875 π²) ≈ 4.06·10⁻⁵`, where `δ_c = (431/512)(1535/1536)`.
  - **Long-wavelength limit.** `ΔΠ(q)/|q|²_lat → 0`. The free sea's clock stiffness equals the held sea's: **`κ_opt = κ_fix = I/12 = 0.0995`** (`γ = 12/I = 10.05`), not block 76's `0.095` (`γ = 10.5`).
  - **Block 76's number.** Block 76's executed values are the same second-order kernel on the torus. There the eight Dirac points are exact zero modes, which enter as intermediate states and contribute `−sin(2π/L)/N` at `q = (2π/L)e₁`. That is `≈ 1/(2πL²)` per `|q|²_lat`, and it carries 84–90% of the torus deficit.
- **(b) Locality.** The difference is **long-ranged**. `ΔΠ` is not `C⁴` at `q = 0`, so its real-space kernel `R` has `Σ_r |r|⁴ |R(r)| = ∞`. It has no finite reach and no tail faster than `|r|⁻⁷`.
- **On a line (closed form).** `ΔΠ₁(q) = −(cos²(q/2)/(2π sin(q/2))) [ln(sec(q/2) + tan(q/2)) − sin(q/2)]`.
  - The free sea is softer by a third: `κ_opt = 1/(3π)` against `κ_fix = 1/(2π)`.
  - This reproduces a1's executed ring values: `c = 1/(6π)` at long wavelength, and `g(π) = 1/(4π) = 0.0796` against a1's 0.0795.

## 2. Steps

**S1 (PROVED; CHECKED A.held). The held sea.**
- `E_fix[φ] = Σ_{x,y} φ_xφ_y tr(P₋(y, x) H(x, y)) = β_L Σ_bonds φ_xφ_y`. The equality holds because `P₋` does not depend on `φ` and `H` has only nearest-neighbour hops. The bond value `β_L = (1/(3N)) tr(P₋H) = −I_L/3` is the same on every bond by the cubic symmetry.
- With `φ_xφ_y = e^{(u_x + u_y)/2}` and `u = ε cos(q·x)`:
  - the first-order term is `(β/2) Σ_bonds (u_x + u_y) = 0`;
  - the second-order term is `(β/8) Σ_bonds (u_x + u_y)² = (β/8) ε² N (3 + Σ_a cos q_a)` (twice that when `2q ≡ 0`).
- So `Π_fix(q) = (β/8)(3 + Σ_a cos q_a) = 3β/4 − (β/16)|q|²_lat`. That gives `c₀ = 3β = −I` and `κ_fix = −β/4 = I/12`.
- CHECKED exactly (Fractions) for every mode on the `4³` and `6³` tori.
- Block 76's executed `c₀ = −1.193` is this `−I`.

**S2 (PROVED). Zero modes, analyticity, and the second-order formula.**
- **Zero modes.** `ker(φHφ) = φ⁻¹ ker H`, since `φHφ(φ⁻¹ψ) = φHψ`. `ker H` consists of the plane waves at `s(k) = 0`, i.e. `k ∈ {0, π}³`, with both coin states: 16 states on even tori, none on odd ones. By Sylvester's law of inertia (`φHφ` is congruent to `H`) the numbers of negative and positive eigenvalues are unchanged.
- **Analyticity.** Near `ε = 0`, the negative eigenvalues stay below `−g/2` (`g` = the smallest nonzero `|eigenvalue|` of `H`) and the zero eigenvalues stay exactly zero. So the Riesz projector `P(ε)` on `(−∞, −g/4)` is analytic, and `E_opt(ε) = tr(P(ε) H_w(ε))` is analytic in `ε`.
- **Expansion.** Write `H_w = H + V₁ + V₂ + O(ε³)`, with `V₁ = {η₁, H}`, `η₁ = u/2`. `V₂` collects the second-order terms: `{u²/8, H} + η₁Hη₁`. For the sum of a group of eigenvalues, the intra-group couplings cancel, and

  `E_opt = E₀ + tr(P₋V₁) + tr(P₋V₂) + Σ_{m∈−} Σ_{n∈+∪0} |⟨n|V₁|m⟩|²/(ε_m − ε_n) + O(ε³)`.

  `E_fix = E₀ + tr(P₋V₁) + tr(P₋V₂) + O(ε³)`, exactly.
- **So** `E_opt − E_fix = −Σ_{m∈−, n∈+∪0} |⟨n|V₁|m⟩|²/(ε_n − ε_m) + O(ε³) ≤ 0`.
- **The matrix element.** `⟨n|{η₁, H}|m⟩ = (ε_n + ε_m)⟨n|η₁|m⟩`, because `η₁` multiplies and `H` is diagonal in its own eigenbasis.
- **Numerical cross-check (a note).** Dense eigenvalues of `φHφ` on `6³`, a torus that has the zero modes, agree with this formula to `2·10⁻¹¹` for three modes.

**S3 (PROVED; CHECKED A.overlap). The zone integral.**
- `η₁ = (ε/4)(e^{iq·x} + e^{−iq·x})`, so `⟨k+q, n|η₁|k, m⟩ = (ε/4)⟨u_n(k+q)|u_m(k)⟩`.
- The coin overlap is `|⟨u₊(k′)|u₋(k)⟩|² = tr(P₊(ŝ′)P₋(ŝ)) = (1 − ŝ′·ŝ)/2`, CHECKED exactly.
- The energy factor is `(ε_n + ε_m)²/(ε_n − ε_m) = (a − b)²/(a + b)`.
- The `±q` terms are equal (`k → −k`), and do not interfere when `2q ≢ 0`. Hence `E_opt − E_fix = −(ε²/8) Σ_k F(k, q)`, i.e. `ΔΠ = −(1/8)⟨F⟩`.
- **The zero modes on the torus.** A zero mode at `k + q = k_D` enters with both coin states (overlap sum 1) and energy factor `b`. For `q = (2π/L)e₁` this gives the exact term `−(1/8)(8 sin(2π/L))/N = −sin(2π/L)/N`. In the zone integral the zero modes have measure zero.
- **The infinite-volume kernel.** It is the limit of the torus kernels at fixed `q`. `0 ≤ F ≤ |q|` (S5) and `F` is continuous off the Dirac points, so the Riemann sums converge to the zone integral, and the zero-mode terms are `O(1/N)`.

**S4 (PROVED). The sign.** `F ≥ 0`, so `ΔΠ ≤ 0`. For `q ≠ 0`, `F > 0` on an open set: near a Dirac point `ŝ(k+q) ≠ ŝ(k)` and `a ≠ b` generically. So `ΔΠ(q) < 0`.

**S5 (PROVED; CHECKED B.vector, B.upper). The upper bound.**
- **The vector inequality.** For `x, y ≠ 0`:

  `4|x − y|² − 2(1 − c)(|x| + |y|)² = 2(1 + c)(|x| − |y|)² ≥ 0`, with `c = cos∠(x, y)`.

  Hence `|x̂ − ŷ| ≤ 2|x − y|/(|x| + |y|)`, and `(1 − ŝ_a·ŝ_b)/2 = |ŝ_a − ŝ_b|²/4 ≤ |s(k+q) − s(k)|²/(a + b)²`.
- **Lipschitz.** `|sin x − sin y| ≤ |x − y|`, so `|s(k+q) − s(k)| ≤ |q|` and `|a − b| ≤ |q|`.
- **Pointwise bound.** `F ≤ min(|a − b|, |q|⁴/(a + b)³) ≤ min(|q|, |q|⁴/b³)`.
- **Jordan.** `|sin t| ≥ (2/π) dist(t, πZ)`, so `b ≥ (2/π) d(k)`, where `d(k)` is the distance to the nearest Dirac point.
- **Integration.** Split the zone into the eight cubes of side `π` around the Dirac points. Each lies in a ball of radius `π√3/2`. Then

  `⟨F⟩ ≤ (8/(2π)³) ∫₀^{π√3/2} min(|q|, π³|q|⁴/(8r³)) 4πr² dr = π|q|⁴(1/6 + ½ log(√3/|q|))`

  (sympy, exact).

**S6 (PROVED; CHECKED B.lower). The lower bound along `e₁`.**
- **The region.** Take `q = t e₁`, `0 < t ≤ 1/8`, and `R_t = {k : 2t ≤ |k| ≤ 1/2, k₁ ≥ 0}`, which lies in the Dirac cell of `0`.
- **Notation.** Put `v = s(k)` and `δ = sin(k₁ + t) − sin k₁ = 2cos(k₁ + t/2) sin(t/2)`.
- **Elementary bounds on `R_t`.** From Taylor's theorem with remainder:
  - `(23/24)|k_a| ≤ |v_a| ≤ |k_a|`;
  - `δ ≥ δ_c t` with `δ_c = (431/512)(1535/1536)`, and `δ ≤ t`;
  - `b ≤ |k|`, `a ≤ (3/2)|k|`, `a + b ≤ (5/2)|k|`.
- **The two factors.**
  - Since `v₁ ≥ 0`: `a − b = (2δv₁ + δ²)/(a + b) ≥ 2δv₁/(a + b)`.
  - `|ŝ_a − ŝ_b|² ≥ sin²θ = δ²(v₂² + v₃²)/(a²b²)`, because `2 − 2c ≥ 1 − c²` (CHECKED).
- **Combining.** `F ≥ δ⁴ v₁²(v₂² + v₃²)/((a + b)³a²b²) ≥ δ_c⁴ (23/24)⁴ (32/1125) t⁴ k₁²(k₂² + k₃²)/|k|⁷`.
- **Integrating over `R_t`.** `∫_{R_t} k₁²k_⊥²/|k|⁷ = (4π/15) log(1/(4t))`. Hence `⟨F⟩ ≥ C t⁴ log(1/(4t))`.

**S7 (PROVED; numbers are notes). The long-wavelength limit, against block 76.**
- **The limit.** By S5, `|ΔΠ(q)|/|q|²_lat ≤ (π/8)|q|⁴(…)/|q|²_lat → 0`. So the free sea's `κ` is the held sea's, `I/12 = 0.09948`, and `γ = 12/I = 10.05` for both.
- **Executed agreement (notes).** The torus version of S3, including the zero-mode terms, gives the gradient parts per `|q|²_lat`:
  - `0.0202` (L = 6);
  - `0.0221, 0.0234` (L = 8);
  - `0.0231, 0.0237` (L = 10);
  - `0.0236, 0.0239, 0.0240, 0.0238, 0.0238, 0.0237` (L = 12: `(100), (200), (300), (110), (111), (220)`).

  These are block 76's W1 table, digit for digit.
- **The deficit.** The held sea gives `0.0249` at L = 12. The zero-mode terms carry `0.00108` of the `0.00128` deficit at L = 12, and 84–90% of it at every `L`. Their exact value `sin(2π/L)/(N|q|²_lat)` is `≈ 1/(2πL²)`.
- **Block 76's own trend agrees.** Its remark "a limit near `0.024–0.025` per `|q|²` is indicated, not proved" matches `κ_fix/4 = 0.02487`.

**S8 (PROVED). (b) The difference is long-ranged.**
- Write `E_opt − E_fix = Σ_{x,y} u_x R(x − y) u_y + O(u³)`, with `R̂ = 2ΔΠ`.
- Suppose `Σ_r |r|⁴|R(r)| < ∞`. Then `ΔΠ ∈ C⁴`, so `|ΔΠ(te₁) − T₃(t)| ≤ Ct⁴`, where `T₃` is its Taylor polynomial.
- S5 gives `ΔΠ(te₁) = o(t³)`, so `T₃ ≡ 0`. Then `|ΔΠ(te₁)| ≤ Ct⁴`, which contradicts S6's lower bound `t⁴ log(1/(4t))/8·C`.
- So the second-order kernel of the difference has infinite reach, and no tail summable against `|r|⁴`, i.e. none faster than `|r|⁻⁷`.
- By contrast, the held sea's own energy is exactly nearest-neighbour (S1).

**S9 (PROVED; CHECKED C.line). On a line, in closed form.**
- **The set-up.** With `s(k) = sin k`, `ŝ = sign(sin k)` flips only across the Dirac points `0, π`. So `F ≠ 0` only on the windows `k ∈ (−q, 0)` and `(π − q, π)`, where `(1 − ŝ·ŝ′)/2 = 1`.
- **The windows.** With `t = k + q/2` the window integrand is `2cos²(q/2) sin²t/(sin(q/2) cos t)`, and `∫_{−h}^{h} sin²t/cos t dt = 2[ln(sec h + tan h) − sin h]` (CHECKED by differentiation).
- **The result.** `ΔΠ₁(q)` is the closed form of §1, `= −q²/(24π) + O(q⁴)`.
- **The line's constants.** The line has `β = −2/π`, so `κ_fix = 1/(2π)` and `κ_opt = 1/(2π) − 1/(6π) = 1/(3π)`. The gradient function `g(q) = 1/(4π) + ΔΠ₁/(1 − cos q)` runs from `1/(6π)` (a1's `c`) to `1/(4π)` at `q = π` (a1's executed `g(π) = 0.0795`).
- **Why the dimension matters.** Near each Dirac point, `F = O(|q|)` on a region of measure `O(|q|^d)`, and `F = O(|q|⁴/r³)` beyond it. So the Dirac points contribute:
  - `|q|²` in `d = 1`, which shifts the stiffness;
  - `|q|³` in `d = 2`;
  - `|q|⁴ log(1/|q|)` in `d = 3`, which does not.

**Notes (floating point, not claims).**
- **The log coefficient.** A spherical-cell zone integration gives `⟨F⟩/t⁴ = 0.02086, 0.02556, 0.03025` at `t = 0.1, 0.05, 0.025` along `e₁`. The increments per halving, `0.00470, 0.00469`, match `log 2/(15π²) = 0.00468`, and the `(111)` direction gives the same.
  - Linearising each Dirac cone (angular average `⟨(q·κ̂)²|q_⊥|²⟩ = 2|q|⁴/15`, eight cones) predicts `ΔΠ(q) = −|q|⁴ log(1/|q|)/(120π²) + O(|q|⁴)`, isotropic at leading order.
  - A heuristic Fourier transform then gives a tail `R(r) ≈ −|r|⁻⁷/(2π³)`, plus sublattice-oscillating terms of the same order from the other Dirac-connecting momenta, where `ΔΠ` has the same kind of singularity.
- **The value of `I`.** `I = 1.19380` (midpoint `96³`).

**ASSUMED.** The standard second-order (Rayleigh–Schrödinger) expansion for the sum of an isolated group of eigenvalues, used in S2 at the scope stated there: an analytic perturbation, and a group separated from the rest of the spectrum by a gap. Nothing else outside the notes is imported.

## 3. The first failing step

None for the task's HIT condition "(a) exact":
- the kernel is an exact zone integral;
- its sign is exact;
- its long-wavelength limit per `|q|²` is exactly zero, by two-sided bounds.

Not proved:
- the coefficient `1/(120π²)` of `|q|⁴ log(1/|q|)`, which is argued and executed (notes);
- the pointwise tail of `R(r)` (only the divergence of `Σ|r|⁴|R|` is proved).

## 4. What would finish it, or extend it

1. **The log coefficient.** Prove `ΔΠ(q) = −|q|⁴ log(1/|q|)/(120π²) + O(|q|⁴)` by controlling the linearisation error in S6's region, and give the analogous singular coefficients at the Dirac-connecting momenta `Q ∈ {0, π}³ ∖ {0}`.
2. **The real-space tail.** From (1), derive `R(r) ≈ Σ_Q e^{iQ·r} A_Q(r̂)/|r|⁷`.
3. **Beyond second order.** The stiffness is a second-order quantity, so (a) is complete. The cubic and quartic terms of `E_opt − E_fix` (the free sea's response to large rate contrasts) are not examined.
4. **Block 76's reading.** Its induced coupling at long wavelength is `γ = 12/I = 10.05` for the free sea as well as the held one. Its torus value `10.5` carries the zero-mode term `≈ 1/(2πL²)`.

## 5. Running it

```
python3 probes/work/derive/the-held-sea-against-the-free-sea/w-macbookpro90c72-j29ee/check.py
```

The run takes about 3.5 s. It makes six exact checks, using Fractions and sympy. The `note` lines are floating point:
- dense diagonalisation;
- block 76's table;
- the zone integral;
- the value of `I`.
