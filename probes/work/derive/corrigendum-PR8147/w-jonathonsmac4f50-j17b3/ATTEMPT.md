# Corrigendum packet for PR #8147 (block 13) — attempt a1

Worker `w-jonathonsmac4f50-j17b3` (model claude-opus-5). Check script: `check.py` in this directory (symbolic and exact; one
60-digit numerical scan, labelled; under 1 s).

**Sources read in full.**

- Block 13's note, runner and cache on `origin/physics-loop/admissibility-induced-law-block13-causal-gaussian-two-point-heat-kernel-20260915`.
- The finder's log (`J:attack-g:PR8147`, grok-4.6) and the confirmation (`J:confirm:J-attack-g-PR8147`).
- Every file changed by PRs #8146, #8148–#8158, #8168, #8170–#8180, searched for block 13, #8147, `K²/9`, `(u,u,u)`, the level line and
  `u² =`.

## 0. The defect, located

T3(ii) (note line 225) says that at gain `g = 3w = 1` (`w = 1/3`), "along `k = (u,u,u)` the symbol is `u² = K²/9` with `K = Σ k_j`".
The symbol is T3(i)'s `S_w(k) = |1 − w Σ_j e^{−ik_j}|²`. On the line `k = (u,u,u)` it is `|1 − 3w e^{−iu}|²`, which at `w = 1/3`
equals `|1 − e^{−iu}|² = 4 sin²(u/2)`. This is `u²` only at `u = 0`.

The runner's D2 (lines 287–296) could not see this: it takes `sp.series(level, e, 0, 4)`, which keeps terms through `e³`, where the
series is exactly `e²`.

## 1. The corrected statement

**T3(ii)′.** For every gain `g = 3w`, along `k = (u,u,u)`:

`S_w(u,u,u) = (1 − g)² + 4g sin²(u/2)`.

At `g = 1` this is `4 sin²(u/2) = 2 − 2cos u = u² − u⁴/12 + u⁶/360 − … = K²/9 − K⁴/972 + O(K⁶)`, with `K = 3u`. On the transverse plane
`K = 0` the symbol is `|k|⁴/36 + O(|k|⁶)`, as stated. Under the parabolic scaling `K ~ |k_⊥|²` the leading form is
`K²/9 + |k_⊥|⁴/36`.

**The largest domain on which the original holds.** The exact equality `S(u,u,u) = u²` holds on `{0}` only. Everywhere else
`S(u,u,u) < u²`, and `u²` is the leading term.

## 2. Steps

**S1 (PROVED; CHECKED E1).** `Σ_j e^{−ik_j} = 3e^{−iu}` on the line, so `S_w(u,u,u) = |1 − 3w e^{−iu}|² = 1 − 6w cos u + 9w²`. This
equals `(1 − 3w)² + 6w(1 − cos u) = (1 − g)² + 12w sin²(u/2) = (1 − g)² + 4g sin²(u/2)`. At `g = 1`, `S = 4 sin²(u/2)`.

*CHECKED:* symbolically for every `w`, independently from T3(i)'s cosine form and from the modulus.

**S2 (PROVED; CHECKED E2).** `4 sin²(u/2) = u²` iff `|sin(u/2)| = |u/2|` iff `u = 0`, since `|sin x| < |x|` for `x ≠ 0`
(`sin x = ∫₀^x cos t dt < x` for `x > 0`, because `cos t < 1` on `(0, x]` except at isolated points; sine is odd).

*CHECKED:*

- the series `S − u² = −u⁴/12 + u⁶/360 − u⁸/20160 + …`;
- the exact values `S = 1, 2, 3, 4` at `u = π/3, π/2, 2π/3, π`;
- `S − u² < 0` at 200 points of `(0, π]` (60 digits, labelled numerical).

**S3 (CHECKED E3).** The runner's own D2 computation, re-run: `series(S(e,e,e), e, 0, 4)` is `e²` and passes, while order 6 gives
`e² − e⁴/12`.

**S4 (PROVED; CHECKED E4, E5).**

- *The transverse clause.* On `K = 0` the `e⁴` coefficient is `(q₁² + q₁q₂ + q₂²)²/9 = |k|⁴/36`, there is no `e⁵` term, and the `e⁶`
  term is nonzero. So "`|k|⁴/36 + O(|k|⁶)`" is right.
- *The level direction.* The leading term is `K²/9`.
- *The parabolic scaling.* Under `K = λ²K̃`, `k_⊥ = λa`, the symbol is `λ⁴(K̃²/9 + |a|⁴/36) + O(λ⁵)`. The mixed term `−K Σ k_j³/27` is
  `O(λ⁵)`. So the leading parabolic form `K²/9 + |k_⊥|⁴/36` of the result-up-front is correct as an expansion.

**S5 (PROVED) Nothing downstream uses the exact level value.**

- T3(iii) (the walk identity `p_{2n} = (C(2n,n)/4^n) P_n` and the Green-function contrast) uses T2, T4 and a walk count.
- The *Reading* uses only "quadratic in the level direction, quartic transversally", which is the leading order.
- T1, T2, T4 and T5 do not mention the symbol.

## 3. Uses of the defective statement (task (b))

| where | statement | verdict |
|---|---|---|
| #8147 note line 225 (T3(ii)) | "along `k = (u,u,u)` the symbol is `u² = K²/9`" | needs its own repair: T3(ii)′ |
| #8147 note lines 237–240 (proof of (ii)) | "Substitute and expand to fourth order" (the level term's `−u⁴/12` is not in the stated result) | needs its own repair: state the exact line value (S1) |
| #8147 note line 4 (claim_scope) | "at g = 1 its expansion is K^2/9 along the level direction and \|k\|^4/36 in the transverse plane (parabolic)" | holds as a leading-order expansion; add "to leading order (exactly 4 sin²(K/6) on the level line)" |
| #8147 note line 43 (result up front) | "expansion `K²/9 + \|k_⊥\|⁴/36` at `g = 1`" | holds (S4: the parabolic leading form) |
| #8147 note lines 227–234 (T3(iii)), 250–255 (Reading), T1, T2, T4, T5 | the walk identity, the Green-function contrast, "parabolic" | unaffected |
| #8147 note line 336 (N5) and runner line 406 | "the level-direction and transverse expansions at g = 1" | unaffected (expansions) |
| #8148 (block 14) lines 36, 66, 318, 332 | "the law a gravity Green function would need (block 13)"; "block 13's parabolic kernel" | unaffected (context, leading order) |
| #8153 (block 19) lines 52, 253, 285, 313 | "its kernel is parabolic"; context | unaffected |
| #8155 (block 21) line 140; #8156 (block 22) lines 143, 169 | context | unaffected |
| #8170 (block 26) lines 31, 66, 92, 117, 149, 190, 221–222, 227 | block 13's T2/T5 and gain-one law (block 26 uses its own exact multiplier identity) | unaffected |
| #8172 (block 28) line 126 | "the directed heat kernel of block 13" | unaffected |
| #8173 (block 29) line 174 | "the formation reading's kernel is a heat kernel" | unaffected |
| #8178 (block 34) lines 92, 162, 176, 188 | block 13 as evidence address (its own exact identity `1 − \|φ\|² = (4/9)[…]`) | unaffected |
| #8180 (block 35) lines 92, 155, 181 | the heat-kernel reading | unaffected |
| #8179 decision record line 13 | the formation reading's kernel is not the comparator's | unaffected |
| #8146, #8150–#8152, #8154, #8157, #8158, #8168, #8171, #8174–#8177 | no use | unaffected |

## 4. The exact lines that must change (task (c))

Note (`docs/…CAUSAL…_2026-09-15.md` on the PR branch):

- **Line 225.** Replace "along `k = (u,u,u)` the symbol is `u² = K²/9` with `K = Σ k_j`" by "along `k = (u,u,u)` the symbol is
  `4 sin²(u/2) = K²/9 − K⁴/972 + O(K⁶)` with `K = Σ k_j = 3u` (for every gain, `(1 − g)² + 4g sin²(u/2)`)". Keep the transverse clause
  as is.
- **Lines 237–240.** Replace "Substitute and expand to fourth order" by "On the level line `Σ e^{−ik_j} = 3e^{−iu}`, so the symbol is
  `|1 − e^{−iu}|² = 4 sin²(u/2)` exactly; on `K = 0` expand to fourth order". Keep the rest.
- **Line 4 (optional precision).** "at g = 1 its expansion is K^2/9 along the level direction" → "at g = 1 its leading terms are K^2/9
  along the level direction (exactly 4 sin^2(K/6) on the level line)".

Runner (`scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py`):

- **Line 288.** `level = sp.series(s1.subs({k1: e, k2: e, k3: e}), e, 0, 4).removeO()`. Add the exact check
  `sp.simplify(s1.subs({k1: e, k2: e, k3: e}) - 4 * sp.sin(e / 2) ** 2) == 0`. If the series is kept, take it to order 6 and compare
  with `e**2 - e**4/12`.
- **Lines 295–296 (D2).** The condition `sp.simplify(level - e ** 2) == 0` becomes the exact identity above. The label becomes "T3(ii):
  at g = 1 the symbol along (u,u,u) is 4 sin^2(u/2) = K^2/9 + O(K^4), and on the transverse plane it is |k|^4/36 + O(k^6) (quartic):
  parabolic".
- **New mutation (family D).** Add `level_symbol_exactly_u2_claimed`, which replaces the exact identity by `s1(u,u,u) == u**2` and
  must fail family D.
- **Cache.** The runner cache (`logs/runner-cache/…heat_kernel_2026_09_15.txt`, line 28, the printed D2 label) must be re-pinned after
  the label change.

## 5. What remains

Nothing for this defect. For every other statement listed, the corrected T3(ii)′ implies what that statement uses. The general-gain
formula `(1 − g)² + 4g sin²(u/2)` also shows the level-line gap `(1 − g)²` at `g < 1`, consistent with T2(a)'s exponential decay.
