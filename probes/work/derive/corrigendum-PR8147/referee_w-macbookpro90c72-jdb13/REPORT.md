# Referee report: J:derive:corrigendum-PR8147:a1

- **Author:** `w-jonathonsmac4f50-j17b3` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-jdb13` (`grok-4.6`). Different model family.
- **Checks:** the symbol recomputed in sympy from `|1 − w Σ e^{−ik_j}|^2`. The author's script is not called. The line-by-line survey of later PRs was not repeated.

## The statement

T3(ii) says that at gain 1, along `k = (u,u,u)`, the symbol is `u² = K²/9`. The attempt replaces that by `4 sin²(u/2) = K²/9 − K⁴/972 + O(K⁶)`, and says the transverse and parabolic leading forms are unaffected.

## Steps

**E1.** On the level line `Σ e^{−ik_j} = 3 e^{−iu}`, so `S = |1 − 3w e^{−iu}|^2 = 1 − 6w cos u + 9w²`. That is `(1 − 3w)² + 6w(1 − cos u) = (1 − g)² + 4g sin²(u/2)` with `g = 3w`. At `g = 1`, `S = 4 sin²(u/2)`.

**E2.** The Taylor series is `u² − u⁴/12 + u⁶/360 − u⁸/20160`. With `K = 3u` the first two terms are `K²/9 − K⁴/972`. Also `4 sin²(u/2)` is `1, 2, 3, 4` at `u = π/3, π/2, 2π/3, π`. For `x > 0`, `x − sin x` has derivative `1 − cos x ≥ 0` and is not flat, so `|sin(u/2)| < |u/2|` on `(0, π]` and the equality `S = u²` holds only at `u = 0`.

**E3.** The series through order 3 is exactly `e²`, which is why a check that stops there passes. Through order 5 it is `e² − e⁴/12`.

**E4.** On `K = 0`, the symbol in powers of a small transverse momentum has no `e²` term and no `e⁵` term, the `e⁴` coefficient is `|k|⁴/36`, and the `e⁶` coefficient is not zero. So `|k|⁴/36 + O(|k|⁶)` stands.

**E5.** Under `K = λ² K̃` and a transverse momentum of order `λ`, the symbol through `λ⁴` is `λ⁴(K̃²/9 + |a|⁴/36)`. The leading parabolic form survives.

## Verdict

The corrigendum survives. The level line is `4 sin²(u/2)`, not `u²`, and the transverse and parabolic leading terms do not change.
