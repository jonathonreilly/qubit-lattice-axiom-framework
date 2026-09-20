# corrigendum-PR8147: derivation attempt 2 of 2

Worker `w-jonathonsmac4f50-j3b64` (claude-opus-5), unit `J-derive-corrigendum-PR8147-a2`.

**Provenance, stated because it bears on independence.** Attempt `a1`
(`w-jonathonsmac4f50-j17b3`) was written by the same model family, on the same machine, by the
same running worker. This is not an independent second opinion on it. `a1`'s corrected symbol is
right and I do not dispute it; re-deriving it along `a1`'s route would tell a referee nothing.
I tested the two things `a1` asserts without checking — that `{0}` is the useful answer to the
task's "largest domain on which the original holds", and that its table of downstream uses is
complete — and both tests returned something.

**Source.** Block 13 = PR #8147 at head `9c364d1d6f75`, the head `a1` pins; `check.py` re-pins it
and fetches the branch if absent.

## 1. The statements attempted

**(a) The corrected statement** — same as `a1`, re-derived here by two routes that do not share a
step with it: from the modulus `|1 − wΣe^{−ik_j}|²` and from the note's own cosine form,

> `S_w(u,u,u) = (1 − g)² + 4g sin²(u/2)`, `g = 3w`; at `g = 1`, exactly `4 sin²(u/2)`.

**(b) The domain, in the form the task asks for.** As an equality the note's `u²` holds at `u = 0`
and nowhere else (`4sin²(u/2) < u²` for `u ≠ 0`), which is `a1`'s answer and is true but tells a
reader nothing about where the note may be used. The relative error
`r(u) = 1 − 4sin²(u/2)/u² = u²/12 − u⁴/360 + u⁶/20160 − …` gives the usable answer:

| tolerance | `\|u\| ≤` | `\|K\| = 3\|u\| ≤` |
|---|---|---|
| 1 % | 0.347106 | **1.04132** |
| 5 % | 0.782537 | 2.34761 |
| 10 % | 1.11849 | 3.35547 |

and at the zone boundary `u = π` the surrogate is wrong by `1 − 4/π² = 59.47 %`. The exact symbol
**saturates at 4**; `u²` does not. So any downstream statement that integrates over the whole zone
would feel this, and only leading-order statements are safe.

**(c) The one downstream place where that matters, which `a1` does not list.** Note **line 195**,
inside T2(b)'s upper bound on the return probability `P_n`:

> `|φ|² = 1 − (2/9)[(1−cos k₁) + (1−cos k₂) + (1−cos(k₁−k₂))] ≤ 1 − (4/(9π²))(k₁² + k₂²)`
> on `[−π,π]²` (using `1 − cos u ≥ 2u²/π²` there)

This is the only downstream line that compares the exact symbol with a quadratic. It is **sound**,
and two facts about it are worth recording because neither is in `a1`'s packet.

## 2. Steps

**S1 (PROVED; CHECKED `F1`). The symbol.** `Σ_j e^{−ik_j} = 3e^{−iu}` on the level line, so
`S_w = |1 − 3we^{−iu}|² = (1−3w)² + 6w(1 − cos u) = (1−g)² + 4g sin²(u/2)`. Verified symbolically
from the modulus form and, independently, from the note's cosine form.

**S2 (PROVED; CHECKED `F2`). The domain.** `|sin x| < |x|` for `x ≠ 0` gives `4sin²(u/2) < u²`
away from the origin (checked at 259 points of `(0,13]`); the series of `r(u)` and the three
tolerance radii are exact and high-precision respectively.

**S3 (PROVED; CHECKED `F3`). Why the runner passed.** The runner's D2 takes
`series(level, e, 0, 4)`, which is exactly `e²`, so its comparison with `e**2` succeeds. At order
6 the series is `e² − e⁴/12`: **one more term in D2 would have caught it.**

**S4 (PROVED; CHECKED `F4`). Line 195 is sharp, and its step order is load bearing.**
- *Sharp.* `(1 − cos u)/u² = ½ sinc²(u/2)` decreases on `(0,π]`, so its minimum there is at
  `u = π`, where `1 − cos π = 2 = 2π²/π²`. Equality holds at `u = 0` and `u = ±π`, and `2/π²` is
  the largest constant for which the inequality holds on `[−π,π]`.
- *Load bearing.* The inequality is **false** outside `[−π,π]` — at `u = 4, 5, 2π` the right side
  exceeds the left — and on the square `k₁ − k₂` ranges over `[−2π, 2π]`. T2(b) is sound only
  because it **drops the `(k₁−k₂)` term first** (it is non-negative) and applies the inequality to
  the two terms whose arguments stay in `[−π,π]`. Applying it to all three, in the order a reader
  might reasonably take, would be a false step that happens to give the same constant.

**S5 (PROVED; CHECKED `F5`). The constant.**
`(2π)^{−2}∫_{R²} e^{−(4n/9π²)|k|²} = 9π/(16n)`, so T2(b)'s stated bound follows from S4's step.

**S6 (CHECKED `F6`). The audit, and why no mutation caught it.** Exactly five lines of the note
carry the level symbol or a quadratic surrogate: 4, 43, 195, 225, 350. `a1` lists 4, 43 and 225.
Of the two it does not list, 195 is S4, and **line 350 is the note's own refutation-target list**:

> "A symbol coefficient not matching block 09's graph, **a level-direction expansion other than
> `K²/9`**, or a transverse quartic other than `|k|⁴/36` (D1–D2)"

That wording is why the mutation family could not catch this defect: **the expansion *is* `K²/9`.**
The gate asks for the leading term, and the leading term was never wrong. It should ask for a
level-line **symbol** other than `4sin²(u/2)`. This is a third line for the packet's (c), beside
the runner's series order in S3 — and it is the structural reason the defect survived a runner,
a cache and a mutation family.

## 3. Where the route stops

- I did not re-verify `a1`'s verdicts for the other campaign PRs (#8148, #8153, #8155, #8156,
  #8170, #8172, #8173, #8178, #8179, #8180). `a1`'s table reads correctly and the search patterns
  it used are appropriate; my audit covers block 13's own note only, which is where the two
  missing lines were.
- The audit is line-level over one file. A statement that uses the level symbol without writing
  `u²`, `K²/9` or `(u,u,u)` would not be found.
- S4's sharpness rests on the monotonicity of `sinc` on `[0,π]`, which I state and check at sample
  points rather than prove.

## 4. What would finish it

1. The packet's (c) gains two entries beyond `a1`'s: note **line 350**'s refutation target should
   name the symbol, not the expansion; and the runner's D2 should compare against
   `4 sin(e/2)**2` exactly (`a1` already proposes this, and adds a mutation
   `level_symbol_exactly_u2_claimed` — with line 350 corrected, that mutation now has a gate to
   fail).
2. Note line 195 deserves a parenthesis saying why the `(k₁−k₂)` term is dropped before the
   inequality is applied. Nothing is wrong; the next reader should not have to rediscover it.
3. If the note ever quotes the level symbol outside the small-`K` regime, the numbers in §1(b) are
   the ones to quote with it.

## 5. Running it

```
python3 probes/work/derive/corrigendum-PR8147/w-jonathonsmac4f50-j3b64/check.py
```
from the repository root (it fetches block 13's branch if absent). `sympy` and `mpmath` required.
Under a minute.
