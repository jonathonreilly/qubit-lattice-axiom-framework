# Referee report: J:derive:pinned-loop-expansion:a2

- **Author:** `w-jonathonsmac4f50-ja55c` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j6cc6` (`grok-4.6`). Different model family.
- **Checks:** spectrum, cycle and theta weights, plaquette counts, edge-set counts, and the Kotecký–Preiss arithmetic, recomputed. The author's script is not called.

## The statement

At the pinned scale the occupied-set weight is `(6z)^|A| Φ(A)`, and `Φ` is a sum over leafless edge sets. Cycles weigh `3 l₁ⁿ + 2 l₂ⁿ`. A theta graph of strands `a,b,c` weighs `6(l₁^{a+b}l₂^c + l₁^{a+c}l₂^b + l₁^{b+c}l₂^a) + 2 l₂^{a+b+c}`. On `Z³` the density is `ρ₀ + 12 w₄ ρ₀⁴ + O(ρ₀⁵)` and the neighbour covariance begins at `4 w₄ ρ₀⁴`.

## Steps

**1.** `K₁` is doubly stochastic. The odd mode `(+1,−1,0,…)` has eigenvalue `(p−q)/S`, and the even traceless mode `(1,1,−1,−1,0,0)` has `(p+q−2r)/S`. Then `tr K₁ⁿ − 1 = 3 l₁ⁿ + 2 l₂ⁿ`, checked at three weight triples for `n = 3,4,5`.

**2.** A leaf integrates to zero because each row of `K₁` sums to 1. A path of two edges and a 3-star both have `Φ = 1`.

**3.** Content enumeration (not the author's transfer code) matches the theta formula on `(2,2,2)` and on `(1,2,2)`, and matches `tr K⁴` on a 4-cycle, at `(3,1,2)`, `(5,1,1)` and `(7,2,1)`.

**4.** Twelve unit plaquettes meet at a vertex and four contain a given edge. Expanding `(1−ρ₀)` and `(1−ρ₀)²` puts `12 w₄` and `4 w₄` on `ρ₀⁴`.

**5.** Connected `n`-edge sets through the origin number `6, 45, 380, 3402`, each at most `36ⁿ`.

**6.** `x⁴/(1−x) = 10556001/43000000 ≤ 1/4` at `x = 57/100`. The roots are `λ ≤ 0.002466` (all `z`) and `λ ρ₀^{1/3} ≤ 0.002914` (small `z`). The small-`z` comparison `(ρ₀ e^{1/4})^{|V|} ≤ (ρ₀ e^{1/4})^{|E|/3}` needs `ρ₀ ≤ e^{−1/4}`; the densities quoted on `(p,1,2)` satisfy it. The Kotecký–Preiss criterion itself remains assumed, as in the attempt.

**7–8.** `(6z)^{|A|} 6^{|E|+c−|A|} = z^{|A|} 6^{|E|+c}`. On `(p,1,2)`, `λ ≥ 1/6`, and the small-`z` cap is about `5.3·10^{-6}` at `p = 3` and `6.7·10^{-7}` at `p = 6`.

## Verdict

The partial result survives. Part (c) was not attempted. The no-clumping region is only the cluster-expansion bound above.
