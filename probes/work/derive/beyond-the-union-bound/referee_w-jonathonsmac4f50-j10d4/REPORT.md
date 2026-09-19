# Referee report: J:derive:beyond-the-union-bound:a4

- **Author:** w-macbookpro90c72-j5968 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j10d4 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j5968__f57f7576__20260919T010015Z`.

**Disclosure.** This referee's model family wrote another attempt on this problem (w-jonathonsmac4f50-jae8a: the refinement-history count,
`p ≥ 84` on `(p,1,2)`). That is a different route, and a4 does not build on it. `check.py` is independent code: exact Fractions, integer
power series, and brute-force enumeration of trees. Nothing is taken from the author's script.

## The claim

- **(A) A thinned tree count.** Thin block 30's typed tree by forbidding diamonds. Then `(a₁, a₂, a₃) = (12/25, 1/5, 2/25)` is an exact
  super-solution of the thinned `U`-system at `x = 3/20 > 4/27`, with `U = 78/25`, `D̄ = 72` and `R̄ = 8254954121/78125000`.
  - The t-trick ceiling becomes `ε₂ < 1/2000`, first met on `(p,1,2)` at `p = 4004` (block 30 has 4165).
  - The extension to the true seed weight `y > 0` is ASSUMED.
- **(B) A set-count no-go.** The overlapping-cone product fails on the diamond animal.

## Step by step

**Step 1 (block 30 arithmetic): holds.** This is re-derived inside X4.

**Step 2 (G-lifts are diamond-free): holds.** X2 enumerates trees up to 7 nodes. Every tree whose lattice embedding is injective is
diamond-free:

| nodes `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| injective | 1 | 3 | 12 | 55 | 270 | 1386 | 7329 |
| diamond-free | 1 | 3 | 12 | 55 | 270 | 1386 | 7344 |
| all | 1 | 3 | 12 | 55 | 273 | 1428 | 7752 |

**Step 3 (thinned system): holds.**
- X1 finds 48 allowed occupancy pairs out of 64, and 216 allowed triples out of 512, with this referee's own diamond test.
- X2: the system `a₁ = xU`, `a₂ = x²(U² − P²)`, `a₃ = x³ Σ A_sA_tA_r`, expanded as an integer power series, reproduces the brute-force
  diamond-free counts for `n = 1..7`.
- The map is monotone, so a super-solution bounds the generating function.

**Step 4 (super-solution): holds.** X3:
- the three margins are `3/250`, `107/62500` and `508933/125000000`;
- the `D` margin is `6937/312500`;
- `R̄ = 8254954121/78125000`.

**Step 5 (ceiling, `p = 4004`): holds as arithmetic at `y = 0`.** X4:
- `max t²(3/20 − t) = 1/2000`, attained at `t = 1/10`;
- `ε₂(4003) > 1/2000 > ε₂(4004) = 729/1458185`;
- `t + ε₂/t² < 3/20`, and `ε₁R̄ < 10⁻⁷`.

**The ASSUMED extension to `y > 0`: needs a correction** (X6).
- The attempt justifies the extension by comparing absolute margins (`2·10⁻²` in `D`) with `y`.
- The relevant comparison is relative. `D̄ = 72` has relative margin `3.08·10⁻⁴`. The factor multiplying `D`'s right side is
  `(1 + yF)⁶ − 1 ≥ 6yR̄ = 3.26·10⁻⁴` at `p = 4004`, which is larger. So the stated certificate does not carry over as it stands.
- A larger `D` fixes it. `(12/25, 1/5, 2/25)` with `D = 80` and `F = 120` is a super-solution at `x = 3/20`, `y = 5.14·10⁻⁷`. This uses
  block 30's slot structure with factors `(1+yF)⁶` and `(1+yF)⁵`.

**Step 6 (set-count no-go): holds.** X5, at `p = 14`: `w(S) = ε₁ε₂² = 1587/3696187 > (ε₁ε₂)² = 4761/933119209`.

**Step 7 (small-cone numerics):** evidence only, as the attempt says.

## Verdict

The partial claim survives: the `y = 0` domain statement, the ceiling arithmetic and the set-count no-go. The `y > 0` step, which the
attempt marks ASSUMED, needs a larger `D̄` than stated; `D̄ = 80` works.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
