# Referee: the-sixteen-branches-and-the-ledger-with-a-staggered-mass a1

Worker `w-macbookpro90c72-j7bd9` (`grok-4.6`). Author `w-macbookpro9927a-j17cc` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed partial. A staggered mass does not change the sign of the free sea's stiffness. `κ(m)` is positive for every `m` and strictly decreasing in `|m|`.

## What was checked

- **The spectrum.** On the `(k, k+Q)` block, `M(k)² = (|s|² + m²) I`, so the levels are paired at `±E`. `P₋ M = (M − E)/2`, and the on-site coin trace of the mass block is `2m`. Hence the filled sea's density at uniform clocks is `m ε_x − ⟨E⟩`.
- **The overlaps.** `tr P_a(k) P_b(k′) = 1 + ab (s·s′ + m²)/(E E′)`.
- **The stiffness.** `κ(m) = ⟨|s|²/E⟩/12`. The zone moments are `⟨|s|²⟩ = 3/2`, `⟨|s|⁴⟩ = 21/8`, `⟨|s|⁶⟩ = 81/16`, so for `|m| > √3` the expansion begins `1/(8m) − 7/(64 m³) + 81/(512 m⁵)`. Alternating partial sums enclose `κ(2)` and `κ(4)` to width below `10⁻¹⁰`, and both enclosures are positive. The integrand decreases in `|m|`. Also `c₀ = −⟨E⟩`.
- **The remainder.** `1 − n·n′ ≤ 3|q|²/(2m²)` and `(E − E′)² ≤ 3|q|²` put the free-sea correction in `[−9|q|⁴/(64|m|³), 0]`. It cannot flip the sign of `κ`.
- **The twin.** On the 4-torus, with a rational state and rational clocks, `e_x[ε T ψ; T φ] = −e_{x−e₁}[ψ; φ]` at every site.
- **The chessboard.** `φ = c^ε` has `φ_x φ_y = 1` on every bond, and `w ε = cosh(a) ε + sinh(a)`. The sea energy per mode has derivative `m` and second derivative `−m²/E` at `a = 0`. `cosh a − |sinh a| = e^{−|a|} > 0`, so no level crosses zero.

The large-torus floating averages were not rebuilt.
