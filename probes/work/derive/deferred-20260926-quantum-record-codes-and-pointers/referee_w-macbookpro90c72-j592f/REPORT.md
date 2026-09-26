# Referee: deferred-20260926-quantum-record-codes-and-pointers a1

Worker `w-macbookpro90c72-j592f` (`grok-4.6`). Author `w-jonathonsmac4f50-j07c6` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed, and the sharpening holds. The depolarized pointer's required generator has a negative off-diagonal already at order `η`. No positive implementation can match it through order `η²`.

## What was checked

- **The couplings.** Every route matrix is symmetric, zero on the diagonal and in each row, and at most `1/2`. `S(−e₁)` is `1/2` on both colour pairs used by the author's witness. Every rate is therefore at least `1/20`.
- **The preparation.** `B⁻¹ = (I − q 11ᵀ)/r` with `r + 14q = 1`. The swapped pair entry is `q²(1+r²) S_{ij}/r²`.
- **The author's entry.** It is `−η² [1+(1−η)²] / [784 (1−η)²]` for symbolic `η`, and the same on the full 12-torus at `η = 1/2, 1/5, 9/10`. There are 864 even sites and 4320 routed stencils; exactly two contain the three consecutive sites.
- **The first-order witness.** `G = η(η−2)(η²−14η+14) / [784 (1−η)²] = −η/28 − η²/56`. The quadratic roots are `7 ± √35`, and `√35 < 6`, so both lie above 1. The entry is negative for every `0 < η < 1`. On the torus it matches at `η = 1/2, 1/5, 1/100`, and equals `−87/3136` at `η = 1/2`, which is `87/5` times the author's `−5/3136`.
- **A second algorithm.** Propagating `(B⁻¹)^{⊗4}` through the sparse generator on the `14⁴` stencil and contracting with `B^{⊗4}` reproduces both numbers at `η = 1/2`.

A positive generator cannot have a negative off-diagonal, so its sup-entry distance from `G` is at least `η/28 − O(η²)`. The random single-site search was not repeated.
