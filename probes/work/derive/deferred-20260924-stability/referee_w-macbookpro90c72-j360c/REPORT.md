# Referee: deferred stability, a1

Author `w-macbookpro9927a-jbeaa` (claude-opus-5-5). Referee `w-macbookpro90c72-j360c` (grok-4.6).

The author's script was not imported. Differentiating under the zone average, Taylor's remainder, and Jensen's bound `⟨|s|⟩ ≤ √(3/2)` are imports. The global scan and the chord inequality were not rebuilt.

## What holds

For arithmetic rates `(1+2ε, 1−ε, 1−ε)`, `d²√Q/dε² = 9ab/Q^{3/2}`. The first derivative averages to zero over the three choices of special axis. The cubic coefficient of the sea energy is

`e₃ = (3/2) ⟨Σ_i u_i (u_j − u_k)² / |s|⁵⟩`,

and the numerator `σ₁σ₂ − 9σ₃` is that sum of squares. A monotone lower sum on 24³ boxes of `[0, π/2]³`, with outward rounding, gives `e₃ ≥ 0.13210`.

For log rates `(e^{2ε}, e^{−ε}, e^{−ε})` the first derivative again averages to zero. The second-order axis average is `χ_a + 2⟨|s|⟩`. The cubic numerator `σ₁³ + (9/2)σ₁σ₂ + (81/2)σ₃` is a sum of nonnegative terms, so this cubic has the opposite sign.

The law cost `36β ε²` has no cubic term. At either quadratic threshold the cubic decides the path: arithmetic rates descend for small `ε < 0`, and log rates descend for small `ε > 0`. On `|ε| ≤ 1/100` the fourth-derivative remainder is at most `K |ε|⁴` with the exact rational

`K = (162/24) (51/50)² (12248/10000) / (49/50)⁷`.

At `ε = −e₃,lo/(2K) = −0.00667`, the path energy is negative for every positive quadratic coefficient up to `e₃,lo²/(4K)`. In `β` that is an interval of width `1.223×10^{-5}` above `χ_a/72`.

`SUMMARY: confirmed — at either threshold the uniform rates are not a local minimum along the traceless path, and the arithmetic descent continues a certified distance above threshold.`
