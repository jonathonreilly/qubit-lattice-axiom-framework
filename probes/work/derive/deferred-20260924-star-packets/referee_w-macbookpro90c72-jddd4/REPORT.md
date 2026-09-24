# Referee: deferred-20260924-star-packets a1

Worker `w-macbookpro90c72-jddd4` (`grok-4.6`). Author `w-macbookpro9927a-j8cdc` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed partial. An energy-stationary supply can track the star's occurrence at `λ = 0` up to an `O(ε³)` coherence. One prepared output costs `O(ε)`. For every `λ ∈ (0,1]` the electric term splits the zero cluster, and the born ensemble keeps a finite coherence across that split.

## What was checked

- **The model.** Sixteen Gauss states, four with one record and twelve with three. On `N=3`, `h² = (1+3ε²)h` with trace `3(1+3ε²)`. On `N=1` the spectrum is `{0,1,1,1+3ε²}`. Both instruments have loss `4W` on `N=1` and none on `N=3`. `W − εF` kills the dressed input.
- **One jump.** `span{A, s}` is invariant under `H_λ` and the loss, and `N=1` does not mix with `N=3`. Both instruments turn `ss*` into an `ε`-free ensemble of trace 4.
- **`λ = 0`.** The slow no-event root is `−6κ + (18κ − 12i κ²/δ)ε² + O(ε⁴)`. Its high component is `−2√3 i (κ/δ) ε³ + O(ε⁵)`, which is the unborn coherence `4√3 (κ/δ) ε³ e^{−12κt} (1+O(ε²))`.
- **Prepared outputs.** Their spectral weights are `c ε²/(1+3ε²)` for `c ∈ {2, 1, 3/2}`, so the stationary-supply cost is `2√c ε + O(ε³)`.
- **`λ > 0`.** Six occupied states sit exactly at `2Kλ`. The other six `N=3` states form three copies of the stated `2×2` block, and `μ₋ − 2Kλ = 3Kλ ε²(1−3ε²) + O(ε⁶)`. The ensemble coherence across the split is exactly `2√2/9` (resolved) and `4√2/9` (coherent). The dressed input's own coherence is `2√3 (Kλ/δ) ε⁵ + O(ε⁷)`.

The 256-dimensional semigroup was not integrated again. The birth weight's uniform limit `1 − e^{−12κt}` is the landed Duhamel estimate; multiplied by the coherence above, it is the trace-distance miss of every energy-stationary supply.
