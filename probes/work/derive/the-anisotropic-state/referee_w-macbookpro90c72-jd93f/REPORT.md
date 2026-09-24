# Referee: the-anisotropic-state a1

Author `w-macbookpro90c72-j5081` (claude-opus-5-5). Referee `w-macbookpro90c72-jd93f` (grok-4.6).

**Sea.** `√(a e^{4ε} + b e^{-2ε})` is convex. At `ε = 0` its second derivative is `(4a² + 14ab + b²)/|s|³`. The difference of that integrand from `9ab + 2(a+b)²` has cyclic sum zero, so the zone average is `χ_a + 2⟨|s|⟩` and `F''(0) = 72β − (χ_a + 2⟨|s|⟩)`.

**No global minimum.** `√(e^{4ε} s_x² + e^{-2ε} s_⊥²)` is at least `e^{2ε}|s_x|` and at least `e^{-ε}|s_y|`. With `⟨|sin k|⟩ = 2/π` and `⟨|s|⟩ ≤ √3`, `F` lies below `F(0)` for `ε ≥ max(1, (3π/8)(36β+√3))` and for `ε ≤ −max(1, 3π(36β+√3))`. Checked at rational `β` from `1/50` to `3`.

**Walk.** The zeros stay at `k ∈ {0, π}³`. The speeds `e^{2ε}`, `e^{-ε}`, `e^{-ε}` multiply to 1. With alternation, `E² = Σ_j t_j² (sin² k_j + sinh² δ_j)`. On the `4³` torus with `t = (2, 1/2, 1)` and `e^δ = (3, 1, 2)` the lowest eigenvalue of `H²` is `1105/144`. The second derivative in `δ_j` at zero is `−t_j² ⟨1/E⟩`. Along the chains, `t_x² ⟨1/E⟩` is at least `(2/π) e^{2ε} log(1 + π e^{3ε}/(2√2))`, which diverges.

The midpoint-grid window for a metastable planar state was not rebuilt.

`HIT: confirmed`.
