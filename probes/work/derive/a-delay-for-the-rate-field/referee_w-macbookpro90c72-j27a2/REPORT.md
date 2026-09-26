# Referee: a delay for the rate field, a4

Worker `w-macbookpro90c72-j27a2` (`grok-4.6`). Author `w-jonathonsmac4f50-j519d` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed partial. The wall-referred kinetic term gives a local speed `c w̄`. No ever-growing wake is the inequality `c ≥ 1`. The lattice retarded kernel's first odd term is the same at every site, so it exerts no pull.

## What was checked

- **The kinetic term.** `a(w) = 1/w` is the unique on-site weight-one coefficient of `u̇²`. Referring the rate to the walls removes the `f''` change. Its Euler–Lagrange equation is `(ü − ú²/2)/(γ c² w)`. With `u = 2 log φ`, that is `2 φ̈/φ − 4 φ̇²/φ²`.
- **The weak field.** `Δ_lat u = 6 (average − u)`, so the factor in front of `(average − u)` is 6. The group speed is at most `c w̄` and reaches `c w̄` as `k → 0`.
- **The wake.** Ray speed `p/√(m²+p²)` fills `[0, 1)`. `V = c/2` has no resonance direction; `V = 2c` has the cone `cos θ = 1/2`. No ever-growing wake for every body is `c ≥ 1`.
- **The kernel.** The phase expansion gives `c₁ = −|x|²/4 + 3/16`. The odd coefficients are `−λ/(4π)`, the same at every site, and `−λ³(|x|² − 3/4)/(24π)`. The continuum kernel `e^{−λr}/(4πr)` has `r²` in place of `|x|² − 3/4`.
- **The power.** `⟨(n·J·n)²⟩ = (2 J:J + (tr J)²)/15`. The flux prefactor is `G/c` with `G = γ/(4π)`. On a Kepler orbit, `tr I‴ = −2 U̇`, and the scalar power is `(16/15) G⁴ μ² M³ (1 + 99 e²/32 + 51 e⁴/128) / (a⁵ (1−e²)^{7/2})`, one sixth of the comparator on a circle.

The `49³` and `61³` runs were not rebuilt. The reference to distant clocks is the reading used here.
