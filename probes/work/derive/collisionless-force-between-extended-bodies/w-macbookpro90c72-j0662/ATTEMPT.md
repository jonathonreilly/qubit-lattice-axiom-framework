# J:derive:collisionless-force-between-extended-bodies:a3 — w-macbookpro90c72-j0662

Attempt 3 of 3, by claude-opus-5-5 (all of `check.py` and this file). At claim time no other attempt or log existed
for this problem. `python3 check.py` prints 4 `ok` lines, exits 0 with `FAIL` empty, and runs in about 9 s.

What is exact and what is floating point:
- **Exact:** the quadrature is tested against exact Dirichlet moments (`Fraction`), and the law's `1/n` remainder is
  obtained by the delta method (sympy).
- **Floating point, labelled:** the quadrature of `Φ`, the symmetry test, and the body averages.

Nothing is adopted and no gravitational claim is made.

**The law used** is the unit's own statement of the single-site law (independent records, `γ = 0`, small density). The
force on a transparent site at `x` from a capturing site at `0` is

`F(x) = −(ρ/(4π√3)) Σ_{octants σ reaching x} σ∘E[Φ(W)]/((n+1)(n+2))`,

with `Φ(w) = w(w·w)^{−5/2}`, `W ~ Dirichlet(|x|+1)` and `n = |x|₁`.

It is consistent with its stated origin (PROVED in outline):
- the multinomial hitting probability of the directed walk is `n!/∏x_k! ∏w^{x_k} = Dir_{x+1}(w)/((n+1)(n+2))`;
- the octant of the sphere maps to the simplex with `dΩ = dA/(√3|w|³)`;
- the capture weight is `|s|₁ = 1/|w|`;
- together these give `w|w|^{−5}` and the factor `1/√3`.

## 1. Statement attempted

**(a) The prediction.** Take two bodies, each 20 capturing sites at uniformly random positions in a ball of radius 6
(925 sites). Put the centres at `(16,0,0)`, `(11,11,0)` and `(9,9,9)` (separations 16, 15.6, 15.6), and sum the law
over all site pairs. The attraction along the separation, times `r²/(N₁N₂)`, in units of `ρ/(4π√3)`, is:

| direction | mean over positions | sampled (200 pairs of bodies) | leading term only | point pair `m(|r|₁/r)²` |
|---|---|---|---|---|
| `(1,0,0)` | **2.1069** | 2.073 ± 0.017 | 2.054 | 4 |
| `(1,1,0)` | **2.2413** | 2.241 ± 0.018 | 2.542 | 4 |
| `(1,1,1)` | **2.2603** | 2.276 ± 0.018 | 2.712 | 3 |

- Ratios to `(1,0,0)`: **1.064** and **1.073**. The collisional law gives `9/4 = 2.25` in every direction.
- Bodies of this size and spacing therefore feel a **nearly isotropic** collisionless force, within 6.4% of the
  collisional value. The axis direction is the weakest.
- A single configuration of 20 + 20 sites scatters by about 0.25 around these means.
- **The finite-`n` terms do the work.** The leading term alone would give 2.05, 2.54 and 2.71. The exact law's `1/n`
  remainder (item (b)) removes most of the leading term's anisotropy at `n ≈ 16–28`.
- The on-axis and on-plane multiplicities (`m = 4, 2`) enter only through the few exactly aligned pairs.

**(b) The law's remainder, exactly.**
- `|F(x)| = |lead(x)|·(1 + c(x̂)/|x|₁ + O(|x|₁^{−2}))`, where `lead(x) = −m x n²/|x|⁵` has magnitude `m|x|₁²/|x|⁴`.
- `c = −3 + [x̂·(∇Φ·(1 − 3ŷ))]/|Φ| + [x̂·½Σ_ij(diag ŷ − ŷŷᵀ)_ij ∂_i∂_jΦ]/|Φ|`, evaluated at `ŷ = x/|x|₁`.
- Its values are **`c = −8` on the body diagonal, `−481/81` towards `(1,2,2)`, and `167603/34322 ≈ 4.883` towards
  `(28,1,1)`.**
- The unit quotes "deviation times `|x|₁`: −16, −24, +5.6 towards (1,2,2), (1,1,1), (28,1,1)" as established. These are
  not this law's remainder coefficients. They may refer to another quantity, for example an executed simulation, or
  another normalisation. This attempt computes the stated law.

## 2. Steps

**S1 — the quadrature. CHECKED** (exact comparison).
- Write `W₁ ~ Beta(a₁, a₂+a₃)` and `(W₂, W₃)/(1−W₁) ~ Beta(a₂, a₃)`, independent, and use Gauss–Jacobi with 40 nodes
  in each.
- Against the exact moments `E∏W_i^{e_i} = ∏(a_i)_{e_i}/(A)_E`, on five parameter sets and six monomials, the worst
  relative error is `2e−14`.
- `Φ` is smooth on the simplex (`|w| ≥ 1/√3`), so the quadrature of `Φ` converges geometrically. 40 and 120 nodes
  agree to every printed digit (checked during the attempt).

**S2 — the remainder. PROVED** (delta method); **CHECKED** (exact symbolic values); the quadrature approaches each
value (floating point).
- `W` has mean `μ = (x+1)/(n+3) = ŷ + (1 − 3ŷ)/n + O(n^{−2})` and covariance `(diag ŷ − ŷŷᵀ)/n + O(n^{−2})`.
- The prefactor is `1/((n+1)(n+2)) = n^{−2}(1 − 3/n + …)`.
- `Φ` has degree `−4`, so `Φ(ŷ)/n² = lead/m`. The relative correction along `Φ̂` is the formula in §1(b).
- On the diagonal the shift term vanishes, because `μ = ŷ` exactly. The covariance term is `−5` and the prefactor `−3`.
  Total `−8`.

**S3 — symmetry. CHECKED** (floating point, to `4e−15`).
- The law is covariant under the 48 cube symmetries.
- On a coordinate plane two octants reach the site and the normal components cancel. On an axis four octants reach it.

**S4 — the bodies.**
- **PROVED:** because the force is a sum over pairs, the mean over uniformly random positions (with or without
  replacement) is `N₁N₂` times the average of `F` over the pair offsets of two uniform balls. The offset counts are the
  ball's integer autocorrelation, CHECKED to sum to `925²`.
- **Floating point:** the three means, the 200 sampled pairs of bodies (which agree within 2σ), the leading-term
  values, and the point-pair factors.

**ASSUMED.**
- The single-site law as the unit states it. Its derivation from the multinomial hitting probability is outlined above.
- The units: `ρ/(4π√3)` per pair over `r²`, in which the unit gives the collisional law as `9/4`. The collisional
  coefficient `K₀q₁²` itself is not re-derived here.

## 3. Where the route stops
- The comparison with the collisional value uses the unit's statement that it is `9/4` in these units. Re-deriving
  `K₀q₁²N₁N₂/r²` at `ρ → 0` from blocks 45 and 47 was not done.
- The prediction is for independent records (`γ = 0`), small density, and the single-site law summed pairwise. It
  therefore has no shadowing between the capturing sites of one body, whose effects would be second order in the
  capture fraction.

## 4. What would finish it
- The computation `C:off-axis-force-small-gamma` tests these three numbers directly. Its runs should find ratios near
  1.06 and 1.07, not the point-pair 1 and 0.75. Near-isotropy, within 7% of `9/4`, is the prediction.
- Closing the discrepancy in the quoted remainder coefficients: re-reading the source of −16, −24, +5.6 against §1(b).
- A second-order treatment: shadowing between the capturing sites of one body, and between the two bodies.
