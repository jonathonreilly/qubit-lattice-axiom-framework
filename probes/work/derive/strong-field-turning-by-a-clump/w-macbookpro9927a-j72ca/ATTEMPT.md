# Strong-field turning by a clump — attempt 2 of 2

**Worker:** `w-macbookpro9927a-j72ca` (claude-opus-5-5).

**Checks:** `check.py` in this directory. It runs six check families (Q, R, C, S, N, K) in about 6 s. They are exact unless labelled.

**Disclosures.**
- The claim tool printed no earlier attempt on this problem.
- My own related units: #8721, a clause for lengths, which covers the family of ray laws with lengths, and #8760, the ray limit of the clocked walk, which covers lattice Berry curvature. Neither computes a turn angle beyond first order or a capture threshold.
- On this machine the worker prefix `w-macbookpro90c72` is shared with another agent. This attempt runs under a private prefix.

## 1. Statement

The ray law is the task's, and also block 98's (PR #8878) at long waves, where `M = Hess(ε²/2) = 1`:

`dv/dt = −w² ∇u + 2 (v·∇u) v`,  `|v| = w = e^u`,  `u = −A/r`,  `A > 0`.

A ray comes in from infinity with impact parameter `b`. Write `ε = A/b` and `e = 2.71828…`.

**(b) Capture.**
- If `b < eA`, the ray never returns: `r` decreases monotonically to 0.
- If `b = eA`, it winds onto the circular ray `r = A`.
- If `b > eA`, it escapes.
- So the critical impact parameter is exactly `b_c = e A`.

**(a) The turn at all orders.** For `b > eA` the ray turns towards the centre by

`χ = 2 ∫_0^1 dy / [(1 + W₀(−y A/b)) √(1 − y²)] − π = Σ_{n≥1} c_n (A/b)^n`,  `c_n = √π nⁿ Γ((n+1)/2) / (n! Γ(n/2 + 1))`.

- The first coefficients are `c_n = 2, π, 6, 4π, 250/9, 81π/4, …`, so `χ = 2A/b + π(A/b)² + 6(A/b)³ + …`.
- `W₀` is the principal branch of Lambert's W.
- The series converges exactly when `b > eA`.
- Near the threshold, `χ = −log(1 − eA/b) + C + o(1)` with `C = Σ_n (c_n e^{−n} − 1/n) = −0.4658175633…`.
- The first term, `2A/b = 2|U(b)|`, is block 98's T3.

## 2. Steps

**S1 (PROVED; CHECKED, family R). Two invariants.**
- Along the law, `d(|v|² − w²)/dt = 4(v·∇u)(|v|² − w²)`, so `|v| = w` holds for all time once it holds at the start.
- For radial `u`, `d/dt (x × v e^{−2u}) = e^{−2u}[x × (−w²∇u) + 2(v·∇u) x × v − 2(v·∇u) x × v] = 0`, since `x × ∇u = 0`.
- So the motion is planar, and `J = r |v| sin φ e^{−2u} = r sin φ / w` is conserved. Here `φ` is the angle between `x` and `v`.
- At infinity `w → 1`, so `J = b`.

**S2 (PROVED; CHECKED). The law's origin.**
- Hamilton's equations for `H = w(x)|p|` (the long-wave form of `w|sin k|`) with `v = ∂H/∂p` reproduce the law.
- So these are the rays of the index `n = 1/w = e^{A/r}`, and S1 is Bouguer's invariant `r n sin φ = b`.
- S2 is used only for orientation. S1 and S3 are derived from the law itself.

**S3 (PROVED). Radial and angular motion.** From `|v| = w` and S1:
- `v_r² = w²(1 − b²/f(r)²)`, with `f(r) = r e^{A/r} = r/w`;
- `φ̇_polar = b w²/r²`;
- so on each monotone branch `dφ_polar/dr = b / (r √(f² − b²))`.

**S4 (PROVED; CHECKED, family C). Capture.**

*Properties of `f`.* `f′(r) = e^{A/r}(1 − A/r)`. This is negative on `(0, A)` and positive on `(A, ∞)`. Also `f(r) → ∞` as `r → 0⁺` and as `r → ∞`. So `f ≥ f(A) = eA`, with equality only at `r = A`.

*If `b < eA`:* `v_r² ≥ w²(1 − b²/(eA)²) > 0` at every `r`. So `v_r` never vanishes, and the ray, which comes in with `v_r < 0`, has `r` strictly decreasing for all time. Suppose `r → r* > 0`. Then `v_r → −w(r*)√(1 − b²/f(r*)²) ≠ 0`, which contradicts convergence. So `r → 0`: the ray is captured. The time taken is infinite, because `∫ dr/w = ∫ e^{A/r} dr` diverges at 0.

*If `b > eA`:* `f = b` has exactly one root `r₀ > A`, which is the outer turning point. The ray turns there and escapes symmetrically.

*If `b = eA`:* `v_r² = w²(1 − (eA)²/f²) ≈ w²(r − A)²/A²` near `r = A`, so `v_r ∝ |r − A|` and the ray approaches the circle in infinite time, with a logarithmic approach.

*The circle is a ray.* On `r = A` with tangential `v` and `|v| = w(A) = 1/e`, the law gives `dv/dt = −w²∇u = −(e^{−2}/A) r̂`. That is exactly the centripetal acceleration `|v|²/A` (family C). The circle is unstable, because `f` has a minimum there.

**S5 (PROVED; CHECKED, family S). One integral.**
- The swept polar angle is `Δφ = ∫_{r₀}^∞ b dr/(r√(f² − b²))`.
- With `x = A/r` and `β = b/A`, this becomes `∫_0^{x₀} β dx/√(e^{2x} − β²x²)`. Here `x₀ < 1` is the small root of `β x e^{−x} = 1`, and it exists iff `β ≥ e`.
- Now set `y = β x e^{−x}`. It increases on `[0, 1)`, since `dy/dx = βe^{−x}(1 − x)`, and it maps `[0, x₀]` onto `[0, 1]`. Then `β dx/√(e^{2x} − β²x²) = dy/((1 − x)√(1 − y²))`. The squares of the two sides agree symbolically, and both sides are positive.
- On this branch `x = −W₀(−y/β)`.
- The turn is `χ = 2Δφ − π`, which vanishes for a straight line.

**S6 (PROVED; CHECKED to z¹⁴). The tree series.** Let `T(z) = −W₀(−z)`, so that `T = z e^T` and `T(0) = 0`.
- Differentiating gives `T′(1 − T) = e^T = T/z`, so `z T′ = T/(1 − T)`.
- Lagrange inversion gives `T = Σ_{n≥1} n^{n−1} zⁿ/n!` for `|z| < 1/e`. This standard step is listed under ASSUMED and checked by sympy to `z¹⁴`.
- Hence `1/(1 − T) = 1 + zT′ = Σ_{n≥0} nⁿ zⁿ/n!`, with `0⁰ = 1`.

**S7 (PROVED; CHECKED). Termwise integration.**
- For `0 ≤ y ≤ 1` and `0 ≤ ε < 1/e`, every term `nⁿ(εy)ⁿ/(n!√(1−y²))` is nonnegative, so Tonelli allows integrating term by term.
- The moments are `I_n = ∫_0^1 yⁿ/√(1 − y²) dy = (√π/2) Γ((n+1)/2)/Γ(n/2 + 1)`, a Beta integral checked for `n ≤ 8`.
- `2I₀ = π` cancels the `−π`. So `χ = Σ_{n≥1} 2nⁿ I_n εⁿ/n!`, which is the statement.

**S8 (PROVED). Convergence is exactly the escape range.**
- For `ε < 1/e`, the integrand of S5 is `1/√(1 − y²)` times a function bounded on `[0, 1]`, because `1 + W₀(−εy) ≥ 1 + W₀(−ε) > 0`. So `χ` is finite, and the positive series converges to it (S7).
- At `ε = 1/e`, `1 + W₀(−y/e) = √(2(1 − y)) + O(1 − y)`, so the integrand is `1/(2(1 − y)) + O((1 − y)^{−1/2})`. The integral diverges, and by Tonelli so does `Σ c_n e^{−n}`.
- For `ε > 1/e` the terms `c_n εⁿ ≥ c_n e^{−n}` do not tend to 0, since `n c_n e^{−n} → 1`, family K. This limit is numerical here; it also follows from Stirling's formula.
- So the radius of convergence of the series in `A/b` is exactly `1/e`. That is exactly the capture threshold of S4.

**S9 (PROVED form; numerical constant). The threshold.**
- Write `δ = 1 − eA/b`. Split off the part of the integrand that is singular near `y = 1`, `1/(2√((1 − y)(1 − y + δ))`. Its integral is `arcsinh(1/√δ) = −(1/2) log δ + log(1 + √(1+δ))`.
- The remainder converges as `δ → 0`, by dominated convergence, since the difference is `O((1 − y)^{−1/2})` uniformly.
- So `χ = −log δ + C + o(1)`, with `C = 2∫_0^{π/2}[1/(1 + W₀(−sin t/e)) − cos t/(2(1 − sin t))] dt − π + 2 log 2`.
- The same constant is `Σ_n (c_n e^{−n} − 1/n)`. Both evaluate to `−0.4658175633` (family K). A closed form was not found.

**S10 (executed, float; family N).**
- The law was integrated directly as an ODE: DOP853 at `rtol 1e−12`, starting at `10⁵ max(b, A)` with `J = b`, and accumulating the velocity angle through `θ̇ = −(v × ∇u)`.
- It reproduces `χ` to `10⁻⁶` at `b = 50A, 10A, 5A, 3A`: `0.04130674, 0.23903362, 0.61043744, 1.99974611`. The series agrees with the integral to `10⁻⁹`.
- Near the threshold it gives `4.016503` at `b = 2.75A` and `6.903002` at `b = 2.72A`. The ray then passes at `r_min = 1.037A`, just outside the circular ray.
- At `b = 2.71A, 2.5A, A`, below `eA = 2.71828A`, every ray reaches `r < A/4`.

**S11 (link to block 98).** `c₁ = 2` gives `χ = 2A/b + O(A²/b²) = 2|U(b)|`, which is block 98's T3 with `U(b) = −A/b`. The next order is `π(A/b)²`, and the orders beyond are the series above.

**ASSUMED.**
- Lagrange inversion for the tree function, the form used in S6.
- Tonelli's theorem for nonnegative series.
- Dominated convergence in S9.
- The ray law as stated. The task supplies it, and block 98 attributes it to block 54's T4.

## 3. Scope and where it stops

1. **The stated law only.** Block 98's corrigendum says that with block 59's bond rates and lengths, and block 60's curvature member (β = 1), the turn doubles at first order. That changes the law, and the capture threshold and the series here are for the law as stated. The same Lambert-W route applies to any law that conserves `x × v g(u)` with a monotone radial index.

2. **`u = −A/r` down to `r = 0`.** A real clump has a regular core. In block 95's control the central clocks run at `e^{−11}`, so there `u ≥ −11`. With `u` bounded below, `r n(r) → 0` at the centre, so every ray has an inner turning point. What the pure law calls capture then becomes long trapping, not true capture. The threshold `eA` and the series hold unchanged for every ray whose outer turning point `r₀` lies outside the core. Rays with `b < eA` reach the circular ray `r = A`, so true capture needs the core to sit inside `r = A`.

3. **Long waves.** At finite wave number the law carries `M = Hess(|sin k|²/2) ≠ 1`. Rays then depend on `k`, and the index picture of S2 changes. This is not treated.

## 4. What would finish the clump question

- Block 95's clump: its far-field `A`, from the control's measured `u(r)`, and its core radius. That decides whether the circular ray `r = A` lies outside the core, and so whether capture is real or only long trapping.
- The lengths member (β = 1): redo S1–S8 with its law.
