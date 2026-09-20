# lightcone-long-range-order: derivation attempt 3 of 5

Worker `w-jonathonsmac4f50-j3a1d` (claude-opus-5), unit `J-derive-lightcone-long-range-order-a3`.

**Provenance, stated because it bears on independence.** Of the three attempts on this problem
at claim time, `a4` and `a5` are by the same model family **and the same machine and running
worker** as this one; `a2` (`w-macbookpro90c72-j451b`) is by another machine. This attempt does
not re-derive `a5`'s Gaussian domination or its infrared bound — re-running my own family's route
would tell a referee nothing. It takes that inequality as **GIVEN** and attacks the part `a5`
leaves loose: the two constants in its threshold, and the two finite-size bounds behind its hedge
"on every sufficiently large even torus". A referee should read this as a sharpening of `a5`'s
right-hand side, not as a confirmation of its left.

**GIVEN (from `a5`, not re-derived here).** For every even `L` and every `β > 0`,

> `⟨|m₀|²⟩_{π_L} ≥ 1 − (3/(2β))(G_L + H_L)`,
> `G_L = (1/N) Σ_{k≠0} 1/E(k)`, `H_L = (1/N) Σ_k 1/(14 − E(k))`, `E(k) = 6 − 2Σ_j cos k_j`,
> `k ∈ (2π/L)(Z/L)³`, `N = L³`.

`a5` then bounds `G_L ≤ I₀ + (3/4L)S₂(L/2) + π²/(16L)` and `H_L ≤ I₂ + (3/4)^L/2`, brackets
`I₀ ∈ [0.250992, 0.254471]` and `I₂ ∈ [0.1409314, 0.1409315]`, and states long-range order for
`β > β₀ ∈ [0.5879, 0.5931]` on every sufficiently large even torus.

## 1. The statement attempted

**(a) The threshold constant, pinned.** Both integrals are the same Bessel integral at two masses,
`I_a = ∫_0^∞ e^{−at} I₀(2t)³ dt = ∫ d³k/(2π)³ 1/(a − 2Σcos k_j)`:

- `I₀ = I_6 = W/6` where `W` is **Watson's integral**, `W = √6/(32π³) Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)`;
  `I₀ = 0.252731009858663003026`.
- `I₂ = I_8 = 0.140931488112717092059`.
- **`β₀ = (3/2)(I₀ + I₂) = 0.59049374695707014263`**, against `a5`'s bracket of width `5.2·10⁻³`.

**(b) The hedge is unnecessary.** `G_L < I₀` at every even `L`, and `G_L` increases in `L`; the
entire finite-size cost sits in `H_L − I₂ > 0`, which falls **geometrically**, at rate
`(2 + √3)^{−L} = e^{−L·arccosh 2}`. So for every even `L`

> `⟨|m₀|²⟩ ≥ 1 − (3/(2β))(I₀ + I₂ + ε_L)`, `ε_L = H_L − I₂`,

and long-range order follows at **every even `L ≥ 4`** for `β > 0.5917081`, and at every even
`L ≥ 12` for `β > 0.590493755`. No "sufficiently large `L`".

**(c) The threshold proved (conditional on the GIVEN):** `β > 0.5904938` on every even torus with
`L ≥ 12`; `β > 0.5917082` on every even torus at all.

## 2. Steps

**S1 (PROVED; CHECKED `E1`). `H_L` has no singular summand.**
- `E(k + (π,π,π)) = 12 − E(k)`, so `14 − E(k+π) = 2 + E(k)`. On an even torus `k ↦ k + π` permutes
  the modes, hence `H_L = (1/N) Σ_k 1/(2 + E(k))` exactly.
- So `H_L` is the Riemann sum of a function **analytic on the real torus**, while `G_L` is the
  Riemann sum of a function with a pole at `k = 0` whose mode is dropped. The two behave quite
  differently in `L`, which is what S3 and S4 use.

**S2 (PROVED; CHECKED `E2`). Exact values on the small tori.**
- `cos(2πn/L)` is rational for `L = 4, 6`, so `G_L` and `H_L` are rationals there:
  `G_4 = 1517/7680`, `H_4 = 127/896`, `G_6 = 1289503/5987520`, `H_6 = 30479/216216`.
- Both forms of `H_L` (with `14 − E` and with `2 + E`) agree exactly, which is S1 executed.

**S3 (CHECKED `E3`, high precision). `G_L < I₀`, and `G_L` increases.**
- At `L = 4, 6, 8, 10, 12, 16, 20`: `I₀ − G_L = 0.0552, 0.0374, 0.0281, 0.0225, 0.0188, 0.0141,
  0.0113`, i.e. `≈ 0.2257/L`, positive and decreasing.
- The mechanism is the dropped `k = 0` mode: `G_L` is a Riemann sum of a positive function that
  omits the neighbourhood of its own pole, and the omission costs `Θ(1/L)` — more than the
  quadrature error. **This is the step that removes `a5`'s `L₀`**, because `a5`'s surrogate for
  `G_L` exceeds `I₀` by `+0.19` at `L = 12` while the truth is `−0.019`.
- Not proved here for all `L`: see §3.

**S4 (CHECKED `E4`, high precision). The finite-size cost is geometric, not `(3/4)^L`.**
- `H_L − I₂ = 8.1·10⁻⁴, 3.4·10⁻⁵, 1.7·10⁻⁶, 9.7·10⁻⁸, 5.7·10⁻⁹, 2.2·10⁻¹¹, 8.9·10⁻¹⁴` at
  `L = 4 … 20`: positive, and each step of `ΔL = 2` divides it by about `17`.
- The rate matches `e^{−κ}` with `κ = log(2 + √3) = 1.3169579`. That is the analyticity width: the
  summand `1/(8 − 2Σcos k_j)` first blows up at complex `k = (iκ, 0, 0)` with `cosh κ = 2`, i.e.
  `e^κ = 2 + √3`, and the trapezoid rule on a periodic analytic function converges at exactly the
  rate set by the nearest singularity. `a5`'s `(3/4)^L/2` has the far weaker exponent `0.2877`; at
  `L = 12` it allows `1.6·10⁻²` where the truth is `5.7·10⁻⁹`.

**S5 (CHECKED `E5`, numerical and labelled). The two constants.**
- `I₀` from the Bessel representation agrees with `W/6` to `9·10⁻²⁷`, `W` being Watson's closed
  form. I do not re-prove that closed form; it is used only as a cross-check of a number I also
  compute directly, and the threshold below does not depend on it.
- `I₂` agrees between the Bessel representation and a direct three-dimensional quadrature to 15
  digits; the value is given to 21.
- `β₀ = (3/2)(I₀ + I₂) = 0.590493746957070142627`.

**S6 (CHECKED `E6`). Where `a5`'s table comes from.**
- `a5` quotes `⟨|m₀|²⟩ ≥ 0.093, 0.217, 0.288, 0.337` at `β = 1`, `L = 12, 24, 48, 100`. Evaluating
  `a5`'s own surrogates gives `0.0958, 0.2192, 0.2909, 0.3400` — so those numbers are the
  surrogates, not the bound.
- The sums themselves give `0.4377, 0.4236, 0.4166, 0.4129`, **4.7 times larger at `L = 12`**, and
  decreasing in `L` towards `1 − (3/2)(I₀+I₂) = 0.409506` rather than increasing towards it.
- The executed value is `|m| = 0.76`, i.e. `⟨|m|²⟩ = 0.578`. So at `β = 1` the bound recovers 71 %
  of the executed magnetization, not 16 %.

## 3. Where the route stops

- **S3 is checked, not proved.** `G_L < I₀` and `G_L ↑` are verified at seven values of `L` and
  the mechanism is clear, but there is no proof here for all even `L`. This matters: the removal
  of `a5`'s `L₀` rests on it. A proof should be routine — `G_L` is a positive Riemann sum missing
  its singular cell — but routine is not done.
- **S4 likewise**: the rate `(2+√3)^{−L}` is read off seven values and explained by the
  singularity, not bounded. What a proof needs is the standard trapezoid-on-analytic-periodic
  estimate with the strip width `arccosh 2` and an explicit constant, in three dimensions.
- **S5 is numerical.** The quadratures agree to 15–27 digits across two representations, but
  interval arithmetic would be needed to call `β₀` rigorous to 20 digits. For the threshold
  statement only about 5 digits are wanted, and those are safe.
- **Nothing here touches `a5`'s left-hand side.** If `a5`'s Gaussian domination is wrong, this
  attempt says nothing about long-range order. It says what `a5`'s inequality gives *if* it holds.

## 4. What would finish it

1. Prove S3 (`G_L < I₀`, `G_L ↑`) and S4 (the geometric rate with an explicit constant). Then the
   statement "for every even `L ≥ 4` and every `β > 0.5917082`, `⟨|m₀|²⟩ ≥ 1 − 0.5917082/β`" is
   unconditional given `a5`'s inequality — a cleaner theorem than one with an `L₀(β)`.
2. Replace the quadratures by interval arithmetic if the constant is ever to be quoted to more
   than 5 digits. `I₀ = W/6` makes half of that free.
3. The gap between the proved threshold `0.59` and the executed onset stays where `a5` left it:
   the bound at `β = 1` is `0.41` against an executed `0.578`, so the route gives order well before
   it gives the right magnitude, and the remaining factor is in the infrared bound, not in these
   constants.

## 5. Running it

```
python3 probes/work/derive/lightcone-long-range-order/w-jonathonsmac4f50-j3a1d/check.py
```
from the repository root. `sympy` and `mpmath` are required; `numpy` is used for the two largest
tori in `E6`. About two minutes.
