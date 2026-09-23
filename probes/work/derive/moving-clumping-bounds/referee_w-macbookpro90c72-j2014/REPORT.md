# Referee: moving-clumping-bounds a2

Author `w-macbookpro90c72-j046a` (claude-opus-5-5). Referee `w-macbookpro90c72-j2014` (grok-4.6).

- **S1 holds.** The two-point maximiser of total variation for a multiplier in `[m,M]` is `(√M−√m)/(√M+√m)`, attained at mean `√(Mm)`. At `M/m=9/4` the value is `1/5`. a1's `(M−m)/(M+m)` is strictly larger (`5/13` at that ratio).
- **S2 threshold holds.** `6 tanh(¼ log R) < 1` iff `R < 49/25`.
- **Correction, not a reopened window.** At `(3,1,2)` the worst content-to-content spread is `(p/q)² = 9`, not the stated `4`. Both exceed `49/25`, so there is still no uniqueness certificate at any `c`.

The chessboard and Peierls constants above the transition were not recomputed. Dobrushin's theorem stays assumed, as the author marked.

`HIT: confirmed` for the sharp bound and the `49/25` window.
