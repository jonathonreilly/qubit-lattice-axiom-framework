# Referee: lightcone-long-range-order a4

Worker `w-macbookpro90c72-j05d2` (`grok-4.6`). Author `w-jonathonsmac4f50-j539b` (`claude-opus-5`). The attempt's script is not imported. The rung reflection is not used.

## Verdict

Confirmed. Route (ii) gives long-range order of the layer marginal for `β ≥ 7`. The bound is coarser than the reflection route.

## What was checked

- **Edge forms.** On the 4-torus and the 6-torus, `Σ_edges (s_u−s_v)(h_u−h_v) = (h, −Δσ)` and `Σ_edges (h_u−h_v)² = 2(h, −Δh)`, with `σ = s₀ + s₁` and `−Δ` the six-neighbour Laplacian. Self-edges contribute nothing to the square, and each nearest-neighbour bond appears twice.
- **Mode.** A cosine mode has norm `N/2` and Rayleigh quotient `E(k)`. With the quadratic form twice the lattice energy, one spin component is bounded by `2N/(β E(k))`, and three components by `6N/(β E(k))`.
- **Cap.** The normalized area of a spherical cap of half-angle `δ` is `(1−cos δ)/2`. Points inside it have dot product at least `cos 2δ`. Convexity of `log Z` then gives the edge lower bound, and `e_v ≥ 7e − 6` because the other six edge types are at most 1.
- **Threshold.** The cubic return series matches the binomial sum through order 15. With 400 exact terms and an integral tail, `I₀ ≤ 0.256631`. The resulting lower bound on `⟨|m₀|²⟩` is `−0.0838` at `β = 6` and `0.0489` at `β = 7`. At `β = 10` it is positive on tori of side 24, 48 and 100 (`0.279`, `0.287`, `0.291`).

The layer-symmetric sector does not see the vertical edges, so the energy bound is what closes this route.
