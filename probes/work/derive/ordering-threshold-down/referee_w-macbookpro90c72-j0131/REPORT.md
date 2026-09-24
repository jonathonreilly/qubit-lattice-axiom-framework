# Referee: ordering-threshold-down a4

Worker `w-macbookpro90c72-j0131` (`grok-4.6`). Author `w-jonathonsmac4f50-jc31e` (`claude-opus-5`). The attempt's script is not imported.

## Verdict

Confirmed as a no-go. On the line `(p, 1, 2)` this history grammar does not prove a threshold below 58. Any sum that still contains the fork-free separated-pole chains diverges for every `p ≤ 57`.

## What was checked

- **Deviations.** The differences `d2 − d1`, `d3 − d1` and `d2 − d3` have numerators `p²(p−1)(p+33)`, `p²(2p²+11p−33)` and `p²(21−p)`. So `d1 ≤ max(d2, d3)` for every integer `p ≥ 1`, and `d2 = d3` at `p = 21`.
- **The ceiling.** `d3(57) = 125/3374 > 1/27 ≥ 127/3491 = d3(58)`. For `p ≥ 58`, `ε2 = d3` and `p² − 52p − 286` is positive and increasing, so `ε2 < 1/27` from there on. For `p ≤ 57` the maximum stays at least `1/27`.
- **Patterns.** The 27 moves split `8, 12, 6, 1` by bad-pair count, and the generating function is `(2+r)³`.
- **Blocks.** The block count matches brute force at `m = 1, 2, 3`. The balanced term is the largest trinomial coefficient, hence at least `3^m` over the number of compositions, and that cubes to at least `27^m/(m+1)⁶`.
- **Divergence.** At `p = 57`, `27 ε2 = 3375/3374`. The least multiple of 3 with `3375^m > 3374^m (m+1)⁶` is `m = 251802`, checked as integers. The chain sum then grows without bound.
- **Prefix.** Two coincident-pole steps and six gap steps open `ell`-gaps of at least 7. One balanced block restores the relative positions. The glued budget has `B = R`.

Whether a configuration realizes each of these chains is not decided. The no-go is for every bookkeeping that still sums their cylinder weights.
