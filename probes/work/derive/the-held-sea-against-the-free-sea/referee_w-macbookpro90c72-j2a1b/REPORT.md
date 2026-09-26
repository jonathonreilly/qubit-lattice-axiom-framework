# Referee: the held sea against the free sea, attempt 1

Attempt `w-macbookpro90c72-j29ee`. The kernel algebra, the bounds, and the line formula are rebuilt here. The attempt's script is not imported.

The walk symbol is `s(k)·σ` with `s(k) = (sin k₁, sin k₂, sin k₃)`. The held sea freezes the negative projector of that walk. The free sea sums the negative eigenvalues of `φHφ`.

## Verdicts

**Held sea.** On every nonzero mode of the `4³` and `6³` tori, `Σ_bonds (u_x+u_y) = 0` and `Σ_bonds (u_x+u_y)²` equals `N(3+Σ cos q_a)`, twice that when `2q ≡ 0`. Therefore `Π_fix = (β/8)(3+Σ cos q_a)`, `c₀ = 3β`, and `κ_fix = −β/4`. With `β = −I/3` this is `κ_fix = I/12`.

**Kernel.** `tr(P₊(n)P₋(m)) = (1−n·m)/2`, and `(n·σ)² = |n|²`. On a two-level system the virtual term is `(a−b)²/(a+b)`. The second-order formula for a gapped group is the Rayleigh–Schrödinger expansion, imported at the scope stated in the attempt. For `2q ≢ 0` the two channels do not interfere, and `ΔΠ = −⟨F⟩/8` with the stated `F`.

**Bounds.** The hat-difference identity and `2−2c ≥ 1−c²` hold. The chord inequalities `sin x ≥ x−x³/6` and `cos x ≥ 1−x²/2` follow from third and second derivatives equal to `1−cos`, which are nonnegative, with vanishing jet at the origin. They give `δ_c = (431/512)(1535/1536)` and the factor `23/24`. The axis integral is `(4π/15) log(1/(4t))`, and
`C = δ_c⁴ (23/24)⁴ · 16/(16875 π²)`.
Eight Dirac cells, each inside a ball of radius `π√3/2`, give
`⟨F⟩ ≤ π|q|⁴ (1/6 + ½ log(√3/|q|))`
for `|q| < √3`. So `ΔΠ/|q|² → 0`, and both seas have stiffness `I/12`.

**Sign.** `F ≥ 0`, so `ΔΠ ≤ 0` wherever the formula applies. Along a small axis the lower bound is positive. At one algebraic point off the axes, `F` is positive. At every `q ∈ {0, π}³`, `|s(k+q)| = |s(k)|`, so `F` vanishes; those are the modes with `2q ≡ 0`, already outside the non-interference step. The sentence “negative for every `q ≠ 0`” does not cover them.

**Zero modes.** On an even torus the eight Dirac points contribute `−sin(2π/L)/N` at `q = (2π/L)e₁`, which is `cot(π/L)/(2L³) = 1/(2π L²) + O(L⁻⁴)` per `|q|²_lat`.

**Long range.** A kernel with `Σ |r|⁴ |R(r)| < ∞` would make `ΔΠ` of class `C⁴`. The upper bound is `o(|q|³)`, so the Taylor polynomial through order 3 would vanish, and the lower bound `t⁴ log(1/(4t))` would be impossible. The difference has no finite reach.

**Line.** The antiderivative of `sin²h/cos h` is `ln(sec h+tan h)−sin h`. Then `ΔΠ₁ = −q²/(24π)+O(q⁴)`, `κ_fix = 1/(2π)`, and `κ_opt = 1/(3π)`.

## What stays open

The decimal value of `I`, block 76's eleven torus entries, the share carried by the zero modes, and the coefficient `1/(120π²)` were not rebuilt.

## Result

HIT: confirmed. The free sea's second-order deficit is a negative zone integral of order `|q|⁴ log(1/|q|)`. Both seas have stiffness `I/12`. The difference is long-ranged. On a line the free sea is softer by a third.
