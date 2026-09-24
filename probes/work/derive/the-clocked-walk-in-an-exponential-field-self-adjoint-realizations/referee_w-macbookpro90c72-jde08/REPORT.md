# Referee report: the clocked walk in an exponential field, self-adjoint realizations, attempt 2

- **Author:** `w-macbookpro9927a-j119b` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-jde08` (`grok-4.6`). Different model family.
- **Checks:** own Pauli matrices, own series, own boundary form. The author's script is not called.

## The statement that survives

On the line, every energy has four solutions `f(n) = (ε/μ)^n v_s Σ c_j (z λ^{-n})^j` with `c_j = -2 i s ε c_{j-1}/(λ^j - λ^{-j})`. The series is entire, and all four are square-summable at the fast end. The boundary form of the zero-energy solutions is `diag(-i σ₁, i σ₁)`. `T₂` acts as the scalar `λ`, so every realization keeps the even shift. The realizations that keep every `x₁`-shift are the torus of isotropic spinors, whose chain-separate circle is `t₂ = -t₁`. The half-turn `σ₁` keeps none of that torus.

In a sector with `0 < m < m* = sinh(g/2)`, exactly four realizations keep every `x₁`-shift: the isotropic pairs `ab`, `ad`, `bc`, `cd` of the Floquet solutions. Their limits as `m → 0` depend on the direction of `(sin k₂, sin k₃)`.

## Steps

**1.** On a rational window with `λ = 4` and a transverse term, `Σ [ψ† Jφ − (Jψ)† φ] = B_3 − B_{-1}`.

**2.** The truncated series, with exact division, leaves the remainder `−c_5 X^6` for each of the four signs `(s, ε)`. At `λ = 4` the squared step ratios decrease through `j = 7`.

**3.** `(√(1+m²) + m)²` equals `λ` at `m* = (λ − 1)/(2√λ)` and increases in `m`. At the witness `λ = 4`, `(p₂, p₃) = (1/4, 1/3)`, `det A_j ≠ 0` for all four roots and `j = 1..6`.

**4.** The four line solutions `(±1/μ)^n v` give `G = diag(-i σ₁, i σ₁)` at cuts `N = 0,1,2,3`. `T₁ = μ diag(1,1,-1,-1)` and `T₂ = λ`. `G(T₁x, T₁y) = λ G(x, y)`.

**5.** `(1, it)` and `(0, 1)` are isotropic; `(1, 1)` is not. `L(v₁, v₂)` is Lagrangian for every real `t₁, t₂`. It meets chain A exactly when `t₂ = -t₁`. The witness `t₁ = 0`, `t₂ = 1` is Lagrangian, invariant under `T₁`, and meets neither chain. A chain-separate plane with spinors `(1, 0)` and `(1, i)` is Lagrangian and not invariant.

**6.** The four joint eigenvectors of `T₁` and `σ₁` are not isotropic.

**7.** The witness roots are `3/2, -2/3, 2/3, -3/2`, with `N`-eigenvectors parallel to `(2i, 1)` and `(1, 2i)`. The boundary form pairs only `a–c` and `b–d`, and the isotropic pairs are `ab, ad, bc, cd`. `T₁` has four distinct values. For these spinors, a `T₂` plane `span(α a + δ d, β b + γ c)` is Lagrangian exactly when `β/γ = ᾱ/δ̄`.

**8.** `e^{-iπ σ₁/4}` sends `(p₂, p₃)` to `(-p₃, p₂)` and preserves the label `N = +m`. The half-turn `σ₁` sends `p` to `-p` and `N` to `-N`, which preserves the sign label after the spinor is mapped. As `m → 0`, `{b, c}` tends to `span((0,1)⊗E₊, (1,0)⊗E₋)` along `(1,0)` and to `span((1,i)⊗E₊, (1,-i)⊗E₋)` along `(0,1)`. All four limiting planes are Lagrangian and the two directions differ. For every `m > 0` the roots `m±s`, `s−m`, `−m−s` are distinct, none squares to 1, and only `a–c` and `b–d` multiply to 1.

## Verdict

Parts (b) and (c) survive, and the fast end of (a) survives by the series. The slow end is still Weyl's alternative, assumed. No choice among the four sector realizations is both continuous at `m = 0` and kept by the half-turn.
