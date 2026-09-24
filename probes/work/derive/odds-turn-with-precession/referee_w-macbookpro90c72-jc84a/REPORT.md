# Referee: odds turn with precession, a2

Author `w-macbookpro9927a-jb8c1` (claude-opus-5-5). Referee `w-macbookpro90c72-jc84a` (grok-4.6).

Precession oscillates the turn channel. A sound-like `ω ∝ |k|` needs the staggered sea and no relaxation. With any `Γ > 0` the longest staggered waves are overdamped.

## What was recomputed

1. **Ordered sea.** `(n × s)·n = 0`, so precession about the lean kills every axial profile. The neighbour average is `γ = (1/3) Σ cos k_j`, and `1 − γ = E/6`. On the sea `F = c (KF)⁶`, one neighbour's logarithmic derivative is one sixth of the site's. The turn equation `τ̇ = −(Γ + Ω n×)(τ − τ̄)` then has eigenvalues `−(Γ ∓ iΩ) E/6`, so `ω = (±Ω − iΓ) E/6`. The real part is `−Γ E/6 ≤ 0` for every `Ω/Γ`.

2. **Staggered sea.** With the sense of precession flipped on the opposite sublattice, the circular amplitudes satisfy `λ² + 2Γλ + (Γ²+Ω²)(1−γ²) = 0`. At `Γ = 0`, `ω = ±Ω √(1−γ²)`, and along an axis this is `±Ω |k|/√3 + O(k³)`. For `Γ > 0` the slow root is `−(Γ²+Ω²)(1−γ²)/(2Γ)`, hence diffusion constant `(Γ²+Ω²)/(6Γ)`. Oscillation starts near `|k| = √3 Γ / √(Γ²+Ω²)`. The real part is never positive.

3. **Flip.** `Z(β)` is even. For `ℓ ≤ 5` the Legendre multiplier satisfies `λ_ℓ(−β) = (−1)^ℓ λ_ℓ(β)`, so the staggered pattern at `−|β|` is the ordered sea at `|β|` read on the opposite sublattice.

The numerical window `0.5085 < β₀ < 0.5086` and the 60-profile scan were not rebuilt. Stability of the complement modes is the attempt's argument, not this check.

`SUMMARY: confirmed - linear waves need the staggered sea and Γ = 0.`
