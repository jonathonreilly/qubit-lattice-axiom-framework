# J:derive:collisionless-force-between-extended-bodies:a1 — the body force by beam propagation, the remainder figures reconciled, and what a run can resolve

**Provenance.**
- Worker `w-macbookpro90c72-j10fe`, model `claude-opus-5-5`, one session.
- The claim printed one prior attempt: a3, by `w-macbookpro90c72-j0662` (issue #8654). It is the same model family, in fact an earlier session of this same model, and it is unrefereed. This attempt is therefore **not independent of a3 in model family**.
- It takes a different route where a3 had one:
  - **The body sums.** a3 used per-pair Dirichlet quadrature. Here, the beam of body 1 is propagated through the lattice by block 48's transport equation and read on body 2. No per-pair value is computed.
  - **The remainder.** Checked by extrapolating the quadrature, besides the exact symbolic values.
- Beyond a3 it adds:
  - the reconciliation of the quoted remainder figures, which corrects a statement in a3;
  - the mapping to the executed computation's normalisation;
  - the share of the aligned pairs;
  - the statistics of random fillings.
- **Sources.**
  - The single-site law is block 48 T3 on PR #8558's branch (`docs/ADMISSIBILITY_RULE_FREE_CAPTURING_BODIES_ARE_CARRIED_BY_THE_WIND_…_2026-09-21.md`), as the task restates it.
  - The executed geometry is from `C:off-axis-force-small-gamma` in `probes/tasks/computations.json`: balls of radius 6, fill 0.025, offsets `(16,0,0), (11,11,0), (9,9,9)`.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**The law (GIVEN).** The attraction on a transparent site at `x` from a capturing site at `0` (independent records, `γ = 0`, small `ρ`), in units of `ρ/(4π√3)`, is

`F(x) = Σ_{octants σ reaching x} σ∘E[Φ(W)]/((n+1)(n+2))`,  with `Φ(w) = w(w·w)^{−5/2}`, `W ~ Dirichlet(|x| + 1)`, `n = |x|₁`.

It points towards the capturing site. The multiplicities are `m = 1, 2, 4` off the coordinate planes, on a plane, and on an axis.

**The body coefficient.** `C = Σ_{pairs} F·r̂ · r²/(N₁N₂)`, over all pairs of capturing sites, one in each body, with `r` the vector between the centres.

**Claims.**
- **(a) Executed; two machineries agree to `1e−14`.** For radius-6 balls (925 sites) with centres at the executed offsets, averaged over random positions:

  | offset | `C` | ratio to `(1,0,0)` | `F r²/(Q₁Q₂K₀)` at `ρ → 0` | share from aligned pairs (`m = 2, 4`) |
  |---|---|---|---|---|
  | `(16,0,0)` | 2.10686 | 1 | 0.9364 | 0.328 |
  | `(11,11,0)` | 2.24125 | 1.0638 | 0.9961 | 0.184 |
  | `(9,9,9)` | 2.26035 | 1.0728 | 1.0046 | 0.040 |

  The collisional law has `C = 9/(4(1 − ρ))` in every direction, i.e. `F r²/(Q₁Q₂K₀) = 1`.
- **(b) Exact.** The remainder figures quoted in the task, "deviation times `|x|₁`: −16, −24, +5.6 towards (1,2,2), (1,1,1), (28,1,1)", and block 48's `−6.3` towards `(11,16,33)`, are the law's **absolute** deviations `n(C − m|r̂|₁²)`. Their exact limits are:
  - `−12025/729 ≈ −16.50`;
  - `−24`;
  - `12570225/2248091 ≈ 5.59`;
  - `−2443750200/393832837 ≈ −6.21`.

  The **relative** coefficients `c` in `C = m|r̂|₁²(1 + c/n + O(n⁻²))` are `−481/81, −8, 167603/34322, −1357639/537289`. So the quoted figures agree with the law.
- **(c) Executed.** One filling at fill 0.025 (about 23 sites per body) scatters by about 0.24 around these means (11%). The gap `C(111) − C(100) = 0.153` therefore needs, for three standard deviations:
  - about 46 fillings if each offset gets new bodies;
  - about 24 if one pair of bodies is moved between the offsets.

  Six seeds cannot resolve it. A run is best compared with the law summed over that run's own sites.

## 2. Steps

**S1 (PROVED; CHECKED E.walk, E.simplex). The law from the transport equation.**
- **The hitting probability.** For contents in octant `σ` with step frequencies `w` on the simplex, the probability that the directed walk from `0` passes `x` is the multinomial `h_σ(x, w)`. It solves `h(x) = Σ_k w_k h(x − σ_k e_k)` with `h(0) = 1`, and sums to 1 on every shell (block 48 T3(a,b)). CHECKED exactly for three rational step laws, `n ≤ 8`.
- **The simplex density.** `∫_Δ h(x, w) dw = 1/((n+1)(n+2))`, so `(n+1)(n+2)h(x, ·)` is the `Dirichlet(|x| + 1)` density. CHECKED exactly for all 35 sites with `n ≤ 4`.
- **The force as an integral.** `E[Φ(W)]/((n+1)(n+2)) = ∫_Δ Φ(w) h(x, w) dw`. With `dΩ = dw/|w|³ = |s|₁³ dw` (CHECKED), this is block 48's `∫ |s|₁ s h dΩ`.

**S2 (PROVED). The body sum as a beam.**
- **Fubini.** Summing S1 over pairs:

  `Σ_{i ∈ B₁, j ∈ B₂} F(x_j − x_i)·r̂ = Σ_σ ∫_Δ (σ∘Φ(w))·r̂ · H_σ(w) dw`,

  where `H_σ(w) = Σ_{i,j} h_σ(x_j − x_i, w)` is the beam that body 1 sends through body 2's sites.
- **Computing the beam.** For fixed `w` it is computed by propagating the transport equation from the indicator of body 1 and summing, over the steps, the mass on body 2's sites. A walk visits each shell once, so the time sum at a site is `Σ_i h(x − x_i)`.
- **Truncation is exact.** The walks are monotone in every coordinate, so mass that leaves the box never returns.
- **Multiplicities come for free.** A pair on a coordinate plane is reached by the walks of both octants that differ in the sign along the zero axis (zero steps along it). The octant sum therefore carries `m = 2, 4` automatically, and the components along the zero axes cancel (block 48 T3(e)).
- **The `w` integral.** Collapsed coordinates `w = (u, (1 − u)v, (1 − u)(1 − v))`, `dw = (1 − u) du dv`, with Gauss–Legendre nodes in `u` and `v` (24 × 24; 32 × 32 gives the same five digits).

**S3 (PROVED). The mean over random positions.**
- `C` is a sum over pairs with one site in each body. For independent bodies with sites placed uniformly, with or without replacement, the expectation of the pair sum is `N₁N₂` times the average of `F·r̂` over all pairs of the two balls.
- For Bernoulli fillings normalised by the actual counts `N₁N₂`, the mean of the ratio differs from this by `O(1/N)`. Executed: `2.1075` against `2.1069` at `(1,0,0)`.

**S4 (executed; notes). The numbers.**
- The beam route gives `2.10686, 2.24125, 2.26035`.
- A per-pair Dirichlet table (Gauss–Jacobi, the machinery a3 used, here only as a cross-check) gives the same values to `1.2e−14`. These agree with a3's `2.1069, 2.2413, 2.2603`.
- The pairs with a zero coordinate, i.e. with `m = 2` or `4`, carry `32.8%` of `C` at `(1,0,0)`, `18.4%` at `(1,1,0)` and `4.0%` at `(1,1,1)`.

**S5 (PROVED; CHECKED E.collisional). The executed normalisation.**
- With `⟨|s|₁⟩ = 3/2`, the capture rate per site is `q₁ = ρ√3/2`, and `K₀q₁² = (9/(4(1 − ρ))) · ρ/(4π√3)`. So

  `F r²/(Q₁Q₂K₀) = (4/9)(1 − ρ) C`.
- The collisionless law is first order in `ρ`, so at `ρ → 0` the predicted ratios to `K₀` are `(4/9)C`: `0.936, 0.996, 1.005`.
- At `ρ = 0.05` the factor `1 − ρ`, and the exchange corrections of order `ρ` that the law omits, both enter at the 5% level.

**S6 (PROVED; CHECKED E.remainder; notes). The remainder, and the quoted figures.**
- **The expansion.** `W` has mean `μ = (x + 1)/(n + 3)` and covariance `(diag μ − μμᵀ)/(n + 4)`. Its third central moments are `O(n⁻²)`, and `Φ` has bounded derivatives on the simplex (`w·w ≥ 1/3`). So `E[Φ(W)] = Φ(μ) + ½Σ_{ij} ∂_i∂_jΦ(μ) Cov_{ij} + O(n⁻²)`.
- **The coefficient.** With `x = nŷ`, `μ = ŷ + (1 − 3ŷ)/n + …` and `1/((n+1)(n+2)) = n⁻²(1 − 3/n + …)`, the relative coefficient is

  `c = −3 + ŷ·[∇Φ(ŷ)(1 − 3ŷ) + ½Σ ∂_i∂_jΦ(ŷ)(diag ŷ − ŷŷᵀ)_{ij}] / ŷ·Φ(ŷ)`.

  The values are computed exactly with sympy, and the absolute coefficient is `c·m|r̂|₁²`.
- **Independent check (notes).** The quadrature's `n(C − m|r̂|₁²)` at `n = 60, 240, 960`:

  | direction | n = 60 | n = 240 | n = 960 | limit |
  |---|---|---|---|---|
  | `(1,2,2)` | `−15.02` | `−16.09` | `−16.39` | `−16.50` |
  | `(1,1,1)` | `−20.78` | `−23.08` | `−23.76` | `−24` |
  | `(28,1,1)` | `5.60` | `5.60` | `5.59` | `5.59` |
  | `(11,16,33)` | `−6.95` | `−6.45` | `−6.27` | `−6.21` |

  Extrapolating the relative deviations reproduces `−481/81, −8, 167603/34322` to four digits.
- **The quoted figures.** They match the absolute limits within 0.5. They come from block 48's refuting pass W4, "a Monte Carlo over contents and paths at the shell `n = 60`", whose "deviation" is the absolute one.
- **A correction to a3.** a3 wrote that these figures "are not this law's remainder coefficients". That statement set the relative coefficients against absolute figures, and it does not stand.

**S7 (PROVED). Why the axis direction is not 1.4–1.5 for these bodies.**
- The computation's text expects "about 1.4 to 1.5 near the axis". That is a **point pair** near an axis: `m = 1`, `|r̂|₁² ≈ 1`, and the `1/n` correction `+4.88/n` at `n ≈ 16`.
- For two balls of radius 6 whose centres are 16 apart, the pair offsets spread up to `±12` sites across the line of centres. The coefficient `m|r̂|₁²` is averaged over that spread: `|r̂|₁²` rises quickly off the axis (e.g. 2.2 at `(16, 5, 5)`), and the pairs exactly on the planes or the axis carry `m = 2` or `4`. The result is 2.107.

**S8 (executed; notes). What a run can resolve.**
- Four thousand pairs of Bernoulli(0.025) fillings give per-filling standard deviations `0.246, 0.247, 0.239`.
- The difference `C(111) − C(100)` has per-filling standard deviation `0.343` with new bodies per offset, and `0.249` with one pair moved between the offsets. For three standard deviations on the gap `0.153`, that needs `46` and `24` fillings respectively.
- The computation asks for at least 6 seeds. If each seed draws new bodies, its mean difference has error `≈ 0.14`, about the size of the gap. If the bodies are fixed across seeds, the prediction to compare with is the law summed over those bodies' sites, which the per-pair table here computes in seconds.

## 3. The first failing step

None for the task as posed: the prediction is computed, with multiplicities, by two machineries.

What is not exact:
- The body averages are floating-point quadratures. They are convergent and agree across machineries to `1e−14`, but they have no rigorous error bound.
- Finite-density corrections are not computed.

## 4. What would finish it

1. **Rigorous enclosures of the body coefficients.** For example, interval quadrature of `Φ` against the Dirichlet weight (`Φ` is analytic on a neighbourhood of the simplex), which would put certified digits on 2.10686, 2.24125, 2.26035.
2. **The first correction in `ρ`.** Exchange of contents displaces records, so the collisionless law is first order in `ρ` (block 48 T3). The executed densities 0.05 and 0.3 need its next order to be compared quantitatively.
3. **The executed comparison.** Sum the law over each run's own sites, and pool at least 24–46 fillings, to resolve the predicted 6–7% direction dependence.

## 5. Running it

```
python3 probes/work/derive/collisionless-force-between-extended-bodies/w-macbookpro90c72-j10fe/check.py
```

The run takes about 21 s, most of it the beam propagation. It makes four exact checks (Fractions, sympy). The `note` lines are floating point:
- the quadrature against the leading term at large `n`;
- the beam and the per-pair table;
- the filling statistics.
