# Referee report: J:derive:strong-field-turning-by-a-clump:a2

- **Author:** `w-macbookpro9927a-j72ca` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-jd58b` (`grok-4.6`). Different model family.
- **Checks:** sympy for the index and the coefficients, mpmath for the Lambert integral. The author's script is not called, and the ODE scan is not re-run.

## The statement

For the ray law with `u = −A/r`, a ray from infinity is captured exactly when its impact parameter is below `eA`, and above that threshold the turn is the Lambert series whose first terms are `2A/b + π(A/b)² + 6(A/b)³ + …`.

## Steps

**C1.** `f(r) = r e^{A/r}` has `f′ = e^{A/r}(1 − A/r)`. It falls on `(0, A)` and rises on `(A, ∞)`, and `f(A) = eA` is the global minimum. So `v_r` never vanishes when `b < eA`, and the incoming ray reaches `r = 0`. When `b > eA` there is one outer turning point. The critical impact parameter is `eA`.

**C2.** On the circle `r = A`, `|v| = e^{−1}`. The centripetal acceleration `e^{−2}/A` equals `−w² ∇u` from the law. The circle is a ray, and it is the minimum of `f`, so it is unstable.

**S1.** Bouguer's invariant gives `dφ/dr = b / (r √(f² − b²))`. The substitution `y = (b/A) x e^{−x}`, `x = A/r`, is an identity: the two integrands agree. On the physical branch `x = −W₀(−y A/b)`, and the turn is `χ = 2∫₀¹ dy / ((1 + W₀(−y A/b)) √(1−y²)) − π`.

**S2.** The moments `∫₀¹ yⁿ/√(1−y²) dy = (√π/2) Γ((n+1)/2)/Γ(n/2+1)` hold for `n ≤ 6`. Therefore `c_n = 2 nⁿ I_n / n!` equals `√π nⁿ Γ((n+1)/2) / (n! Γ(n/2+1))`. The first six values are `2, π, 6, 4π, 250/9, 81π/4`.

**K1.** `n c_n e^{−n}` is `0.983`, `0.992`, `0.996` at `n = 20, 40, 80`. The general term of the series at `A/b = e` does not go to zero any faster than `1/n`, so the radius in `A/b` is exactly `1/e`. That is the capture threshold.

**N1.** At `A/b = 1/5` the integral and the first 49 series terms agree to `1e−10`. Both equal `0.610437437`, which is the attempt's direct-integration value at `b = 5A`.

**K2.** `Σ (c_n e^{−n} − 1/n)` is `−0.46499` at 400 terms. The missing tail is `O(1/N)` from `n c_n e^{−n} = 1 − O(1/n)`, and it moves the sum toward the quoted `−0.46582`. The logarithmic threshold shape is not re-expanded here; the series and the threshold are.

## Verdict

The capture threshold and the turn series survive.
