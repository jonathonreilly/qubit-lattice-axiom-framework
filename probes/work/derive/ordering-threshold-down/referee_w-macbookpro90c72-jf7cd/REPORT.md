# Referee report: J:derive:ordering-threshold-down:a2

- **Author:** `w-jonathonsmac4f50-j3960` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-jf7cd` (`grok-4.6`). Different model family.
- **Checks:** the three rational deviations, factored again. The author's script is not called.

## The statement

With the three noise deviations `d₁`, `d₂`, `d₃` as written, `d₂ > d₁` exactly when `p > q`, and `d₂ = d₃` exactly on `q = r` or on `pq = q² + 2qr + 4r²`. Each one is the strict maximum at an explicit positive triple, so none is the noise parameter on the whole octant.

## Steps

**1.** At `p = q = r` each deviation is `5/6`.

**2.** `d₂ − d₁ = (p − q) C / (D₁ D₂)`, where `C = p²(pq² + q³ + 4r³)` and both denominators are sums of positive monomials. Every coefficient of `C` is positive, so for positive weights the difference has the sign of `p − q`. Inside `p > q`, `d₁` sits strictly below `d₂` and is not the maximum.

**3.** The numerator of `d₃ − d₂` is `−p²(q − r)(pq − q² − 2qr − 4r²)`. It vanishes at `(10,1,1)`, `(4,1,1)` and on the surface point `(7,1,1)`, where both deviations equal `11/60`.

**4.** Strict maxima: `d₂` at `(3,1,2)` (`0.795` against `0.654` and `0.550`), `d₃` at `(3,2,1)` (`0.550` against `0.471` and `0.308`), `d₁` at `(1,3,2)` (`0.983` against `0.962` and `0.932`).

Block 30's note was not re-read. The polynomial comparison does not depend on it.

## Verdict

The factorizations survive. No one of the three deviations dominates the positive octant, and `p > q` kills `d₁` but not the flip between `d₂` and `d₃`.
