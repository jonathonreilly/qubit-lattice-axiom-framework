# The bond-rate law beyond second order: which completions keep the uniform field the global minimum?

Attempt 3 of 3. Worker `w-macbookpro90c72-j4e2d`, model `claude-opus-5-5`. The plan below is my own; no earlier attempt at this problem exists on `ai/probes`. There is no overlap with my earlier units in this session. Script: `check.py` in this directory, which prints 20 checks, a `SUMMARY` line and a `HIT` line.

Sources, read on their PR branches:
- block 53, PR #8568: the site-rate law in `log w`, and no master clock;
- block 55, PR #8571, T4: the unit of rate is not a variable;
- block 59, PR #8581: bond rates of weight one. This includes item 3 (the law is for `log c_b`), T2 (each rate is sourced by the energy it times) and T3 (the three-number law);
- block 60, PR #8590: a ledger linear in the rates;
- block 84, PR #8652: the balance;
- block 89, PR #8678: log rates, the exact mass, the threshold `⟨1/|s|⟩/4`, and no global minimum under a quadratic law.

## 1. Statement attempted

**Setting.** Every definition here is quoted from the sources above.

**Bond rates and the law.** Bond rates `c_b > 0` have weight one, and the law's variable is `u_b = log c_b`. Block 59's law (T3) is

    c_0 u_b + α Σ_coll u + β Σ_perp u + δ Σ_par u = s_b,    c_0 = −2α − 8β − 4δ,

over the 14 bonds whose midpoints lie within one site of `b`: 2 collinear, 8 perpendicular and touching, and 4 parallel. `M` is its matrix. Its energy is

    ½⟨u, −Mu⟩ = ½ Σ_pairs K_X (u_b − u_b')²,    K = (α, β, δ) by class.

The source is the hop energy `t_b = ∂⟨H⟩/∂ log c_b` (block 59 T2).

**The balance.** Block 89's balance, per site, is the sea's energy plus the law's energy, taken at a fixed unit (the mean log rate).

**The alternation family.** It is

    𝒜 = { u_b = δ_j (−1)^{x_j} on the bonds of axis j : (δ_1, δ_2, δ_3) ∈ ℝ³ }.

Block 89's balance is the diagonal of this family, `δ_j = δ`.

**The sea on 𝒜.** On 𝒜 the walk has `E² = |s|² + μ`, with `μ = Σ_j sinh² δ_j` (block 89 T1b). So the sea's gain per site is

    G(μ) = ⟨√(|s|² + μ)⟩ − ⟨|s|⟩.

The threshold is `κ_c = ⟨1/|s|⟩/4`, with `κ = α + 2β`.

**Claims.**

**(a)** The listed principles admit exactly the local ledgers of weight one,

    F = Σ_b c_b f_b(v_b),

where the energy per tick `f_b` is a covariant function of the log ratios `v_b` to the 14 neighbours, `f_b(0) = 0`, and the Hessian is `−M`.

The pair ledgers among these are

    F = Σ_X K_X Σ_{X-pairs} √(c_b c_b') φ_X(log(c_b/c_b')),    φ_X even,  φ_X(0) = 0,  φ_X''(0) = 1.

So they leave one free even profile per class.

Two members are singled out:
- **N2, the rate-weighted law.** It is the unique pair ledger whose energy per tick is linear in the law's variable:

      F = ½ Σ_b c_b (−M log c)_b = Σ_pairs (K/2)(c_b − c_b') log(c_b/c_b'),    φ = x sinh(x/2).

- **N1.** It is the unique massless linear combination of bond rates and of block 54's pair clocks `√(c_b c_b')`:

      F = 2 Σ K (√c_b − √c_b')²,    φ = 4(cosh(x/2) − 1).

The power family `φ_p = (cosh px − 1)/p²` joins them. As `p → 0` it gives the weight-one twin of block 89's quadratic law, and `p = 1/2` gives N1.

**(b)** Take `α, β ≥ 0`, not both zero.
1. If the profiles grow as `o(e^{|x|/2})`, the balance is unbounded below at every `κ`. This covers block 89's quadratic law, every polynomial profile, and `φ_p` with `p < 1/2`.
2. On block 89's diagonal:
   - profiles `≥ 4(cosh(x/2) − 1)` make the uniform field the strict global minimum for every `κ ≥ κ_c`;
   - in the power family this holds exactly when `p ≥ 1/2`;
   - boundedness at `κ_c` requires `liminf φ e^{−x/2} ≥ √3/(6κ_c) = 1.268`.
3. On all of 𝒜:
   - profiles `≥ x sinh(x/2)` make the uniform field the strict global minimum for every `κ ≥ κ_c`. These include N2 and every `φ_p` with `p ≥ 1`;
   - under N2 the cost is `2κ Σ_j δ_j sinh δ_j`, and the cheapest alternation of a given mass lies along one axis;
   - N1 does not keep the uniform field global on 𝒜. At `β/κ = 1/10` the uniform field is not the global minimum on `[κ_c, 0.2287)`. For `β/κ < 0.049` the balance is unbounded below on `[κ_c, 1/(4 + 8β/κ))`.
4. Whenever 2 or 3 applies, the transition at `κ_c` is continuous. The minimising `μ*` tends to 0 as `κ ↑ κ_c`, with

       μ* log(1/μ*) ≃ 4π²(κ_c − κ),

   which is the same for every completion.

**(c)** This part is executed, not proved. Under N2, each `κ < κ_c` has one minimiser. It lies on one axis, `δ⃗ = (a*, 0, 0)`, with rest energy `m* = sinh a*`. There is no runaway at any `κ > 0`: `a* ≈ 1/(2κ) − 1` for small `κ`. The table is in S17.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S0 — ASSUMED (floating point).** The B-family bounds are float64 evaluations of monotone Riemann sums. They are assumed accurate to relative `1e-10`.
- `scipy.special.i0e` was compared with 30-digit mpmath at 2000 grid points: the maximum relative deviation is `6.7e-16` [B0].
- A safety factor of `1e-9` is applied to every bound.
- Every margin used is at least `6e-2`, with two exceptions. B6's witness has a margin of `4e-3`. The threshold bracket in B1 only has to contain block 89's `0.91067`.

**S1 — PROVED. The weight is one.**
1. Block 53 says only ratios of rates mean anything: multiplying every rate by `λ` must change nothing observable.
2. The sea's energy is the sum of the negative eigenvalues of `H(c) = Σ_b c_b h_b`. `H` is linear in `c`, so `E_sea(λc) = λ E_sea(c)`.
3. Suppose the law's ledger has weight `w`. At unit `λ` the balance is `λ E_sea + λ^w F`, so the minimising ratios depend on `λ` unless `w = 1`.
4. Block 89's quadratic law with a pure-number `κ` has `w = 0`. Its second-order balance at unit `λ` is `(6κ − (3/2)λ⟨1/|s|⟩)δ²`, so its threshold is `λ⟨1/|s|⟩/4`. Whether the bonds alternate would then measure the unit.
5. If instead `κ` is a fixed rate, it is a master clock, which block 53 excludes.
6. So the ledger has weight one, and the weight must come from the rates themselves. Locally that means `F = Σ_b F_b` with `F_b(λc) = λ F_b(c)`, that is, `F_b = c_b f_b(v_b)`, with `v_b` the log ratios to the neighbours.
7. This is block 60's ledger linear in the rates: each rate times an energy per tick of weight zero.

[A1]

**S2 — PROVED. No mass.** Write `F = Σ_b e^{u_b} f_b(v_b)`.

*Euler identity.* `F(u + t·1) = e^t F(u)`. Differentiating once in `t` and once in `u_b` gives `Σ_b' ∂_b ∂_b' F = ∂_b F`.

*First derivatives at `u = 0`.* By covariance, `∂f_b/∂v_{bb'}(0) = g_X` depends only on the class `X` of the pair. A proper rotation swaps the two members of any neighbouring pair: a rotation by π about the axis midway between them, or about a face diagonal for perpendicular pairs. So `g_X` is the same seen from either end, and `∂_b F(0) = f(0) + Σ_b' (g − g) = f(0)`. The Hessian therefore satisfies `H·1 = f(0)·1`.

*Second order at a fixed unit.* It is

    ½ f(0) Σ_b u_b² + (a shift-invariant form),

because `Σ_b u_b Σ_b' g_X (u_b' − u_b) = −Σ_pairs g_X (u_b − u_b')²`.

*Matching.* Block 59's second order is `−M`, which vanishes on `(1,1,1)` at `k → 0` (T3). With `f(0) ≠ 0` the operator becomes `−M + f(0)`, a mass at every `k`. So a completion of block 59's law needs `f(0) = 0`.

[A2 verifies `F(u+t) = e^t F(u)` and that the rows sum to `f(0)` on a ring with a generic `f`.]

**S3 — PROVED. Pair ledgers.** Take pair energies per tick `f_b = Σ_X Σ_{b'∈X(b)} g_X(u_b' − u_b)`. Then

    F = Σ_pairs [c_b g_X(u_b' − u_b) + c_b' g_X(u_b − u_b')] = Σ_pairs √(c_b c_b') φ_X(u_b − u_b'),
    φ_X(x) = e^{x/2} g_X(−x) + e^{−x/2} g_X(x).

- `φ_X` is even.
- Every even `φ` arises, from `g = φ e^{x/2}/2`.
- Equivalently, every symmetric weight-one `Ψ(c, c')` equals `√(cc') φ(log(c/c'))`.
- `f(0) = 0` holds exactly when `φ(0) = 0`.
- At second order a pair contributes `φ''(0)(u − u')²/2`. This matches `K_X (u − u')²/2` exactly when `φ_X''(0) = 1`.

[A3. A4 builds the 14-neighbour classes on the `4³` torus (8, 2 and 4 per bond) and shows that the Hessian of `Σ K √(cc') φ` equals `−M(k)` of block 59 T3 at all 64 momenta, to `3e-14`.]

**S4 — PROVED. The two members.**

*N1.* Take `A Σ c_b + Σ_X B_X Σ_{X-pairs} √(c_b c_b')`. Its second-order coefficients are:
- the mass, `A/2 + Σ_X B_X n_X/4`, with `n = (2, 8, 4)`;
- the pair term, `−B_X/8`, from `e^{(u+u')/2} → (u² + u'²)/4 − (u − u')²/8`.

No mass and matching force `B_X = −4K_X` and `A = 2 Σ K_X n_X`. The result is `2 Σ K (√c_b − √c_b')²`. Its law is `2√c_b (L√c)_b = source`, with `L = −M`. Source-free, this is `c_b = (Σ K √c_b' / Σ K)²`: block 53's rule with the mean of order ½.

*N2.* Take an energy per tick linear in the log ratios, `f_b = Σ γ_X (u_b' − u_b)`. Its second order is `−Σ γ_X (Δu)²`, which matches only when `γ_X = −K_X/2`. So

    F_N2 = ½ Σ_b c_b (L u)_b = Σ_pairs (K/2)(c_b − c_b')(u_b − u_b') ≥ 0.

Its law is `½[c_b (Lu)_b + (Lc)_b] = source`: block 59's operator read in log rates and weighted by the rate, averaged with the same operator read in rates.

[A5: the sympy solutions, and both torus identities for random `u`.]

**S5 — CHECKED. Premise E² = |s|² + μ.** On the `4³` torus, with independent `δ_j`, the spectrum of block 59's walk equals `±√(Σ sin² k_j + Σ sinh² δ_j)` to `6e-15`. The cases checked are `(0.3, 0, 0)`, `(0.3, 0.5, 0.2)`, `(0.4, 0.4, 0.4)`, `(1.1, 0, 0.7)` and 0. So the sea's gain on 𝒜 is `G(μ)`, and it depends on `δ⃗` only through `μ`. [A7]

**S6 — CHECKED. The cost on 𝒜.** On the torus, the exact multiset of unordered pairs per site is:
- collinear: `{δ_j, −δ_j}`, once for each `j`;
- perpendicular: `{±δ_i, ±δ_j}`, once for each `i < j` and each of the four sign choices;
- parallel: `{δ_j, δ_j}` and `{−δ_j, −δ_j}`, each once.

For any profiles this gives

    cost = α Σ_j φ(2δ_j) + 2β Σ_{i<j} [cosh((δ_i+δ_j)/2) φ(δ_i−δ_j) + cosh((δ_i−δ_j)/2) φ(δ_i+δ_j)].

- `δ_par` never enters.
- On the diagonal the cost is `3κ φ(2δ)`.
- For N2 the cost is exactly `2κ Σ_j δ_j sinh δ_j`, which depends only on `κ`.

[A6: symbolic in `δ_1, δ_2, δ_3`, with `φ` an undetermined function.]

**S7 — PROVED. Facts about G.**

*Bessel form.* `⟨e^{−t|s|²}⟩ = K3(t) := (e^{−t/2} I_0(t/2))³`. Then

    ⟨1/|s|⟩ = π^{−½} ∫ K3 t^{−½} dt,
    G(μ) = (2√π)^{−1} ∫ (1 − e^{−tμ}) K3 t^{−3/2} dt.

*Bounds.* `√μ − ⟨|s|⟩ ≤ G(μ) < √μ`, from subadditivity of the square root, and `⟨|s|⟩ ≤ √⟨|s|²⟩ = √(3/2)`.

*The remainder J.* `J(μ) := ⟨1/|s|⟩μ/2 − G(μ) = ⟨(√(|s|²+μ) − |s|)²/(2|s|)⟩ ≥ 0`, and

    J(μ)/μ² = (2√π)^{−1} ∫ ψ(tμ) t^{½} K3(t) dt,    ψ(x) = (x − 1 + e^{−x})/x².

- `ψ` is decreasing: `x³ψ' = 2 − x − (x+2)e^{−x}`, which vanishes at 0 and has derivative `−1 + (1+x)e^{−x} ≤ 0`.
- So `J(μ)/μ²` is decreasing in `μ`.

*Properties of K3.*
- `K3` is decreasing, since `(e^{−x} I_0)' = e^{−x}(I_1 − I_0) < 0`.
- `K3 ≤ (π/2)³ (πt)^{−3/2}`, because `1 − cos θ ≥ 2θ²/π²`.
- Every integrand used is a product of positive decreasing factors, so left and right Riemann sums bracket the integrals. The `J` integrand is bounded below cellwise by `ψ(t_{i+1}μ) t_i^{½} K3(t_{i+1})`.

*Asymptotics.* Near the 8 zeros of `|s|`, `|s| = |q|(1 + O(q²))`. So

    J(μ) = (μ²/4π²)(log(1/μ) + j_0) + o(μ²).

[B5: the slope of `J/μ²` against `log(1/μ)` on `[1e-6, 1e-5]` is bracketed in `[0.02523, 0.02547]`, which contains `1/(4π²) = 0.02533`. Executed: `j_0 = 3.628`.]

**S8 — PROVED. Claim (b1).** On the diagonal, the cost `3[αφ_coll(2δ) + 2βφ_perp(2δ)]` is `o(e^δ)` while `G ≥ √3 sinh δ − √(3/2)`, so `B → −∞`. On one axis, the cost `αφ(2a) + 8βφ(a)cosh(a/2)` is `o(e^a)` while `G ≥ sinh a − √(3/2)`. Boundedness at `κ` needs `liminf φ(x) e^{−x/2} ≥ √3/(6κ)`. [B2: exact witnesses for `x²/2` and `p = 0.45`, at `κ = 1` and `κ = 10`.]

**S9 — CHECKED (S0). The threshold bracket.** `⟨1/|s|⟩ ∈ [0.910594, 0.910782]`, so `κ_c ∈ [0.227648, 0.227696]`. [B1]

**S10 — CHECKED (S0). N1 on the diagonal: 12κ_c(cosh δ − 1) > G(3 sinh² δ) for every δ > 0.** The check uses three regions.
1. *Small, `δ ≤ asinh 1`.* First, `2μ − 12(cosh δ − 1) = 6(cosh δ − 1)²`, and `(cosh δ − 1)²/sinh⁴ δ = (cosh δ + 1)^{−2} ≤ ¼` [A8]. So it suffices that `J(μ)/μ² > κ_c/6`. By monotonicity this holds for all `μ ≤ 3`, because the bound gives `J(3)/9 ≥ 0.0493 > κ_hi/6 = 0.0379`.
2. *Middle.* 699 monotone cells on `[0.881, 1.496]` all hold. The minimum margin is 22%.
3. *Large, `δ ≥ 1.496`.* Here `G < √3 sinh δ ≤ 12κ_lo(cosh δ − 1)`, because `12κ_lo tanh(δ/2) ≥ √3`.

[B4]

**S11 — PROVED. Claim (b2).** Profiles `≥ φ_N1` give `cost ≥ 12κ(cosh δ − 1) > G` for `κ ≥ κ_c` (S10). For the power family:
- `∂_p φ_p = [pxsinh(px) − 2(cosh px − 1)]/p³ ≥ 0`, since `z sinh z − 2(cosh z − 1) = 4 sinh(z/2) cosh(z/2) (z/2 − tanh(z/2))` [A8];
- so `p ≥ ½` gives `φ_p ≥ φ_N1`;
- `p < ½` gives `φ_p = o(e^{x/2})`, which fails by S8.

**S12 — PROVED. Concavity.** `h(y) = √y asinh √y` satisfies `h'' < 0`. With `z = √y`,

    h'' = [(z/√(1+z²) − asinh z)/(2z²) − z/(2(1+z²)^{3/2})]/(2z),

and `asinh z > z/√(1+z²)`, because the difference has derivative `z²/(1+z²)^{3/2}` [A8]. Since also `h(0) = 0`, `h` is strictly subadditive. Under N2 on 𝒜 the cost is `2κ Σ h(sinh² δ_j) ≥ 2κ h(μ)`, with equality only when at most one `δ_j ≠ 0`.

**S13 — CHECKED (S0). N2 on one axis: 2κ_c a sinh a > G(sinh² a) for every a > 0.** The check uses three regions.
1. *Small.* `2μ − 2a sinh a = 2 sinh a (sinh a − a) ≤ μ²/3`, because `6(sinh a − a) ≤ sinh³ a` (the derivative of the difference is `3(cosh a − 1)²(cosh a + 2)` [A8]). So it suffices that `J/μ² > κ_c/3`. This holds for all `μ ≤ 1`, i.e. `a ≤ 0.881`, because `J(1) ≥ 0.0805 > κ_hi/3 = 0.0759`.
2. *Middle.* 699 cells on `[0.881, 2.196]` all hold. The minimum margin is 6.7%.
3. *Large, `a ≥ 1/(2κ_lo)`.* Here `G < sinh a ≤ 2κ_lo a sinh a`.

[B3]

**S14 — PROVED. Claim (b3).** Take profiles `≥ x sinh(x/2)`. The difference `x sinh(x/2) − 4(cosh(x/2) − 1) = 2[z sinh z − 2(cosh z − 1)] ≥ 0` [A8], so these profiles dominate N1's as well. Each coefficient in S6 is positive, so for `δ⃗ ≠ 0` and `κ ≥ κ_c`

    cost(δ⃗) ≥ 2κ Σ_j δ_j sinh δ_j ≥ 2κ_c h(μ) > G(μ),

by S12 and S13. Power profiles with `p ≥ 1` qualify, because `cosh x − 1 − x sinh(x/2) = sinh(x/2)(2 sinh(x/2) − x) ≥ 0` [A8] and `φ_p` is monotone in `p`. For `κ < κ_c` the uniform field is not even a local minimum: the Hessian on 𝒜 is `2(κ − κ_c)|δ⃗|²`.

**S15 — CHECKED (S0) and executed. N1 on 𝒜.** On one axis the cost is `κ C_r(a)`, with `r = β/κ` and

    C_r(a) = (1 − 2r)·4(cosh a − 1) + r(16 cosh a − 32 cosh(a/2) + 16) ~ (2 + 4r)e^a,

while `G ~ e^a/2`.
- *Exact asymptotics.* The balance is unbounded below exactly when `κ < 1/(4 + 8r)`, and `1/(4 + 8r)` exceeds `κ_c` when `r < (1/κ_c − 4)/8 = 0.049`.
- *Witness.* At `r = 1/10` and `a = 2.2`, `G/C ≥ 0.22869 > κ_hi`, so the uniform field is not global on `[κ_c, 0.2287)` [B6].
- *Executed* [C5]:
  - on the one-axis line the uniform field is global above `κ_c` exactly when `r ≥ r_0 = 0.1102`;
  - first-order transitions occur at `κ = 0.2358` (jump to `a = 3.00`) for `r = 0.05`, and at `κ = 0.2287` (`a = 2.21`) for `r = 0.1`;
  - 1000 sampled three-axis configurations at `r = 0.25` and `0.5` show no violation. This is not proved.

**S16 — PROVED. Continuity and the law (b4).** Suppose S11 or S14 applies. Then the one-axis ratio `R(μ) = G(μ)/(2κ_c h(μ))` is below 1 for `μ > 0` and tends to 1 as `μ → 0`. The same holds on the diagonal with that line's cost.
- *Continuity.* `B ≥ 2h(μ)(κ − κ_c R)` is positive for `μ ≥ ε` once `κ > κ_c − η(ε)`, and `η(ε) > 0` because `R` is continuous, below 1, and tends to 0 at infinity. So the minimiser's `μ*` tends to 0 as `κ ↑ κ_c`.
- *Law.* Along any direction, `B = −2(κ_c − κ)μ + (μ²/4π²) log(1/μ) + O(μ²)`, by S7 and because every completion agrees at second order. So `μ* log(1/μ*) ≃ 4π²(κ_c − κ)`. The `O(μ²)` constant depends on the completion and the direction. For N2 on one axis the refined form is

      μ*[log(1/μ*) + j_0 − ½ − 4π²κ/3] = 4π²(κ_c − κ),

  which is checked to 0.1% at `κ = 0.227` and `0.225` [C2].

**S17 — executed. Claim (c) under N2** [C1–C3]. `κ = Q(a) := G'(sinh² a) sinh a cosh a/(sinh a + a cosh a)` is strictly decreasing on both lines, so each line has one minimiser for each `κ < κ_c`. The global minimiser lies on one axis (S12). The rest energy is `m* = sinh a*`, per block 89 T1; the dispersion stays isotropic although the bond pattern picks an axis.

| κ | a* | m* = sinh a* | B* per site | diagonal δ* | √3 sinh δ* | B diagonal |
|---|---|---|---|---|---|---|
| 0.227 | 0.0696 | 0.0697 | −2.96e−6 | 0.0337 | 0.0583 | −2.14e−6 |
| 0.225 | 0.1674 | 0.1682 | −6.55e−5 | 0.0754 | 0.1307 | −4.19e−5 |
| 0.220 | 0.3543 | 0.3618 | −7.98e−4 | 0.1439 | 0.2502 | −4.28e−4 |
| 0.210 | 0.6954 | 0.7528 | −6.85e−3 | 0.2492 | 0.4362 | −2.86e−3 |
| 0.200 | 1.0046 | 1.182 | −0.0236 | 0.3437 | 0.6072 | −8.27e−3 |
| 0.180 | 1.5220 | 2.181 | −0.110 | 0.5337 | 0.9688 | −0.0324 |
| 0.150 | 2.2476 | 4.680 | −0.488 | 0.8740 | 1.714 | −0.129 |
| 0.100 | 3.9956 | 27.17 | −4.29 | 1.8639 | 5.451 | −0.873 |
| 0.050 | 9.0000 | 4052 | −404 | 4.7732 | 102.4 | −16.6 |

- *Far from threshold.* `2κ(tanh a* + a*) = 1 − 3/(4 sinh² a*) + …`, so `a* ≈ 1/(2κ) − 1`. There is no runaway.
- *Controls* [C3]:
  - 96³ midpoint zone sums agree with the Bessel form to `1.3e-5`;
  - a free three-axis minimisation at `κ = 0.2` lands on `(1.0046, 0, 0)` with `B = −0.02356`.

**S18 — executed. Cross-check with block 89** [C4]. Under the quadratic law on the diagonal, this machinery gives `δ* = 0.084, 0.167, 0.313, 0.480` at `κ = 0.225, 0.22, 0.21, 0.20`. Block 89 has `0.084, 0.168, 0.312, 0.480`. At `κ = 0.25` it gives a barrier of 0.82 at `δ = 1.87`, with the energy below the uniform value from `δ = 2.51`, as in block 89.

## 3. Which completion is most natural, and where the route stops

The principles fix the class (S1–S3). They do not pick the profile.

**Why N2.** I take N2 as the most natural member:
- it is block 60's ledger (each rate times an energy per tick) with the energy per tick linear in block 53's and block 59's variable, the log rate;
- its alternation cost depends on the law only through `κ = α + 2β`, the same combination that sets the threshold, and this holds in every direction of 𝒜.

**The other reading.** "Linear in the clock rates", with block 54's pair clocks counted as rates, gives N1 instead. N1 is the borderline member of the growth condition, and its global structure on 𝒜 depends on `β/κ` (S15).

**Where no step fails.** No step fails. The limits of the scope are:
- **The configurations.** "Global" is over the alternation family 𝒜, which is where block 89's exact mass holds. It does not cover other wave vectors, the anisotropic mode of blocks 88 and 89 T3, or inhomogeneous patterns.
- **The ledgers.** The decision covers pair ledgers. Ledgers with three-bond terms are not treated.
- **N1.** Whether N1 keeps the uniform field global on all of 𝒜 for `β/κ ≥ 0.110` is executed, not proved.
- **The sea.** The sea remains a comparator (block 78).

## 4. What would finish it

1. Extend the global statement beyond 𝒜: an energy bound over all bond-rate fields for N2. A candidate route is `F_N2 = ½⟨c, L log c⟩` against the concavity of the sea in `c`.
2. Settle N1 on 𝒜 for `β/κ ≥ 0.110`: the three-axis bounds of S13, run with N1's non-separable cost.
3. Treat the anisotropic mode under N1 and N2. Asymptotically N2's cost `~ 6βεe^{2ε}` beats the sea's `~ (2/π)e^{2ε}`; this needs the S10-type bounds.
4. Give a principle that selects between N1 and N2, or an observable that separates them. Near threshold they agree: the same `κ_c`, the same continuous transition and the same leading law. They differ in the axis structure and in runaway: N1 on the diagonal runs away below `√3/12 = 0.144`, while N2 never runs away.
