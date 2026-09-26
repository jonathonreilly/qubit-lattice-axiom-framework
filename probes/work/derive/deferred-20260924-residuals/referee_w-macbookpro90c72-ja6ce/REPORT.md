# Referee: deferred-20260924-residuals a1

Attempt `w-macbookpro9927a-j1af8`. The bright-from-dark block is rebuilt from the rotor-cube words. The attempt's script is not imported.

The cube has six occupied sites and one minus sign. Outside sites are `(0,3,5,6)` and inside sites are `(1,2,4,7)`. An edge exists when the site labels differ by a bit in `{1,2,4}`. Dark middle words are those with no empty edge.

## Verdicts

**S.** There are 36, 96 and 36 words of grade 0, 1 and 2. Of the middle words, 24 are dark and 72 are bright. The tree block has determinant ±1. At the flat phase the 72×24 block has rank 23 and the all-ones vector is in its kernel.

**H.** Of the 32 phases in `{±1}^5`, exactly eight are rank-deficient:

`(1,1,1,1,1)`, `(1,1,1,−1,−1)`, `(1,−1,−1,1,−1)`, `(1,−1,−1,−1,1)`, `(−1,1,−1,1,1)`, `(−1,1,−1,−1,−1)`, `(−1,−1,1,1,−1)`, `(−1,−1,1,−1,1)`,

with kernel dimensions `1, 1, 2, 1, 1, 2, 4, 2`. At each, the pencil `[B | ∂₁B K | … | ∂₅B K]` has column rank `rank(B) + 5 dim K`. The three first-mark inputs overlap every kernel by `1/12`, `1/12` and `1/6` per dimension.

**G.** Twenty monomial pivots that are units on `(ℂ*)^5` leave a 52×4 residual. Four residual rows avoid the last column, and one 3×3 minor of that block is `−(z₂³ − z₄³ z₅)(z₂³ z₅ − z₄³)(z₁ z₃ + 1)`. The last-column entries include `z₅+1`, `z₂+z₄`, `z₃+z₄ z₅` and `z₃+z₅`. Setting those to zero forces `(z₂,z₃,z₄,z₅) = (−1,1,1,−1)`, and the remaining gcd is `z₁+1`. That is the half-period point `(−1,−1,1,1,−1)`.

## What stays open

The exponent `5/2` is exact only if no dark phase lies off `{0, π}^5`. The rank-deficient 4×3 branch of the residual is not excluded. The 300-start search and the 7⁵ grid were not rerun. The lower bound is imported from the landed note, not re-proved. The two residuals of #8960 stay open.

## Result

HIT: confirmed as a partial. The eight half-period phases, their pencils, and the input overlaps are as stated, and the last-column branch of the residual is only `(−1,−1,1,1,−1)`.
