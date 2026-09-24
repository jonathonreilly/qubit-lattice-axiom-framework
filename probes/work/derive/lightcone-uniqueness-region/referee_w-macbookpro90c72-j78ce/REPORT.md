# Referee: lightcone-uniqueness-region a3

Worker `w-macbookpro90c72-j78ce` (`grok-4.6`). Author `w-jonathonsmac4f50-je99d` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed. The chordal influence of the von Mises–Fisher kernel is exactly `1/3`. Seven predecessors therefore contract for every `β < 3/7`, and that is where this Dobrushin bound stops.

## What was checked

- **Moments.** The integrals of `z^m e^{az}` on `[-1, 1]`, the identity `I(a) = 4(a cosh a − sinh a)/a³`, and `A = coth k − 1/k` as the mean of `z`.
- **Energy gaps.** `D₀ − B_⊥` and `D₀ − B_∥` reduce to `F_⊥` and `F_∥` over positive denominators. `k⁴ F_⊥` is the stated hyperbolic polynomial.
- **Signs.** `G_⊥` starts at `(4/15) k⁸` and `G_∥` at `(16/15) k¹⁰`. Every Taylor coefficient through degree 39 is nonnegative, and the dominant exponential beats the remainder from degree 30 on. So both truncated energies stay at most `1/(12π)`, strictly for `k ≠ 0`.
- **The constant.** `∫ (u·s)² dS/(4π) = 1/3`, and `√(|B| D₀) = 1/3`. The linear function attains the bound at `V = 0`.
- **Thresholds.** `tanh(ln(4/3)/2) = 1/7`, so a total-variation comparison of seven predecessors reaches 1 at `ln(4/3)`. The order `√3/7 < ln(4/3) < 3/10 < 3/7 < 0.55` is exact. `7 · (1/3) · (3/7) = 1`.

The ball extension uses Green's identity and the spherical-harmonic solution of the Neumann problem, as the attempt states. The window from `3/7` up to the executed onset bracket `(0.55, 0.60)` is still open.
