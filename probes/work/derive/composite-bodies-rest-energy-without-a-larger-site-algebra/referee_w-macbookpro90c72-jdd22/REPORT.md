# Referee: composite-bodies-rest-energy-without-a-larger-site-algebra a3

Author `w-jonathonsmac4f50-j8f94` (`claude-opus-5-5`). Referee `w-macbookpro90c72-jdd22` (`grok-4.6`).
The attempt is `probes/work/derive/composite-bodies-rest-energy-without-a-larger-site-algebra/w-jonathonsmac4f50-j8f94/`.
Checks below are an independent script (own index order, own quadrature, own 4×4 inverses). The author's `check.py` was not imported.

The statement attempted is the task's (a)(b)(c): a two-walker binding energy inside `M_2(C)` per walker, the fall when that interaction is timed by the local clock, and what an untimed interaction does. Parked entry 4 is not touched. Blocks 53 and 54 stay supplied clauses.

## Step verdicts

1. **ASSUMED, accepted.** Distinguishable walkers, block 54's `D` with symbol `sin k`, and the two interactions, are the setting the task names. Symmetrized identical particles are explicitly left out. That does not weaken (a)–(c) for distinguishable pairs.

2. **FOLLOWS.** `σ_z` is diagonal, so the line splits into four sectors. Co-moving kinetic energy is `2 sin(K/2) cos q`; counter-moving is `2 cos(K/2) sin q`. Verified by expansion. `D = (i/2)(T − T†)` has symbol `sin k`.

3. **FOLLOWS.** For `a > 2|b|`, trapezoid quadrature reproduces `(1/2π) ∫ dq/(a − 2b cos q) = 1/√(a² − 4b²)` to `2·10⁻¹⁶`. The attractive contact condition then gives `E = −√(V² + 4 sin²(K/2))` (co-moving) and `E = −√(V² + 4 cos²(K/2))` (counter-moving). The series `E² = V² + K² − K⁴/12` and `E² = V² + 4 − K²` at `K = 0` are exact. Co-moving: rest energy `M = |V|`, `c = 1`. Counter-moving: band minimum at `K = 0`.

4. **FOLLOWS.** On a 6-ring the position-space spectrum matches the union of the `K`-blocks to `3·10⁻¹⁵`. On a 48-ring every sampled `K` matches the closed forms to `3·10⁻¹³` in both sectors.

5. **FOLLOWS at the order claimed in the step, not as an all-K identity.** The separable channels integrate to `1 = V_n(1 + 3b²/E²)/E` and `1 = V_n(1 + b²/E²)/E` through `O(b²)`, hence `c² = 3/2` and `c² = 1/2`. An 80-ring finite difference gives `1.494` and `0.500` (`V_n = −0.7`) and `1.499` and `0.500` (`V_n = −2.5`). Section 1 writes `E² = V_n² + 6 sin²(K/2)` without a remainder. That stronger formula does not follow: at `K = 1.2`, `V_n = −1.5`, a 96-ring gives `|E² − (V_n² + 6 sin²(K/2))| = 0.18`. Step 5 already keeps `O(b⁴)`. The at-rest acceleration uses only `∂²(E²/2)|_0`, so the HIT is unaffected.

6. **FOLLOWS as a band minimum; the quoted `0.81` and `0.90` are that worker's `24³`/`32³` finite differences, not a theorem.** Own `4³` secular root matches full diagonalization to `10⁻¹⁴`. On `12³`, `V = −5`, `E(0) = −6.028` sits below the continuum edge `−2√3 ≈ −3.464`, and `(E² − E0²)/K²` is `−0.793`, `−0.797`, `−0.800` on the axis, face diagonal and body diagonal. `V = −8` on the axis is `−0.881`. Same sign, same isotropy, and within a few hundredths of the finer-grid window `−0.81` to `−0.90`. The ground pair falls up.

7. **FOLLOWS.** For `w = e^{gx}`, each degree-one timed term (kinetic `√w D √w`, contact `w(x)`, bond `√(w1 w2)`) satisfies `H T_a = λ_a T_a H` with `λ_a = e^{ga}`. Expanding in `a` gives `d⟨K⟩/dt = −g ⟨H⟩`. On the interior of a 10-chain the timed defect is `10⁻¹⁶`; the untimed defect is `0.34`. Untimed, only `H_kin` is pulled. At `K = 0` the co-moving kinetic symbol is identically `0`, so an untimed contact pair at rest does not fall.

8. **FOLLOWS at ray level; the executed signs agree.** `∂²_K(E²/2)` at `K = 0` is `+1` (co-moving contact, acceleration `−g`) and `−1` (counter-moving, `+g`). Nearest-neighbour quadratic curvatures give `−(3/2)g` and `−(1/2)g`. Own propagation on a 72-chain (`g = 0.008`, width `8`, `t ≤ 12`): co-moving timed `a/g = −1.089`, untimed `−0.037`, counter-moving timed `+1.009`, nearest-neighbour even channel `−1.499`. The `0.09` co-moving residual is this shorter packet, not a second acceleration law. The ray limit remains an assumption, as the attempt says.

No earlier step fails. The quantifiers match the task: one walker still has no on-site mass in `M_2(C)`; binding supplies `M = |V|` for the co-moving contact pair; universal free fall does not follow without a timing clause and without `∂²(E²/2) = 1` at rest.

`HIT: confirmed`.
