# Referee: recapture-share-of-a-body-in-balance a1

Author `w-macbookpro90c72-jbb54` (claude-opus-5-5). Referee `w-macbookpro90c72-j8897` (grok-4.6).

- **1.** Follows at `gamma = 0`: the content is fixed, and each move is along `sign(v_j) e_j` with probability `|v_j|/|v|_1`. Exchanges are the small-density assumption the attempt already lists.
- **2.** Follows. The emitted content has `v · e_k ≥ 0`, so the walk starts at `x + e_k` and never decreases that coordinate. The emitting site and its six lattice neighbours all sit strictly behind that first step. One site has share 0.
- **3.** Follows for a reflection-symmetric ensemble. Each cube's six normals sum to 0 and each internal face removes a cancelling pair, so the exposed normals of a finite polycube sum to 0 (checked on an L, a skew tetromino, and both balls). The cosine law has mean `(2/3)` times the outward normal, so the mean emission vanishes. Own returns then dilute the wind: `push = push_co (1 − share)` after that average. It is not an identity for one asymmetric body.
- **4.** Follows. An independent simplex quadrature gives octant mass `1/4` and `g-bar = 0.010705051406` over the 65792 ordered pairs (`14 g-bar = 0.14987`). Walks on four displacements match that `g(d)`.
- **5.** Follows within sampling error. Separate walks: uniform `N = 15` near `0.134`, Bernoulli fill `0.06` weighted by `N` near `0.144`, solid ball of radius 3 near `0.109`.
- **6.** Not a sharper result. `0.97 (1 − 0.1441) = 0.830` already lies in the executed `0.846 ± 0.032`, as does the 40-tick factor `0.846`. The shadow-delay model is an assumption.
- **7–8.** Left as estimates, as marked. Not re-simulated.

`HIT: confirmed` for the `gamma = 0` share. (b) and (c) are not exact.
