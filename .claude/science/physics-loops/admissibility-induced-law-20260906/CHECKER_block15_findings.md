# Refuting pass — block 15 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block15_formation_unit.py`, refuting pass `specs/supervisor_control_block15_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the criterion (U2) | set arithmetic on recorded neighbours per site | a second implementation tracking each site's recorded neighbours as a list at formation time, compared with exact equality on every order of the isolated domino, path and plaquette and the star classes `k = 0, 1, 2` | agrees on every order |
| the star's joint law and its center-first sequential law (U3) | the normalized edge product; the sequential product of conditionals | the tree factorization `(1/6) Π_leaves K(v_center, v_leaf)` written by hand | equal on all `6^7` patterns, for both laws |
| the star in the mixed environment (U4) | `seq_law` | an order-by-order recursion: the center's uniform draw times each leaf's conditional given the center and its five outside records | equal on all patterns; differs from the joint law |
| the normalizer lemma (U2) | symbolic in `(p, q, r)` for `k = 2..6` | integers at `(3,1,2)` for `k = 2..8`: `Z_1^k (K_k(b..b) − K_k(−b,b..b)) = (p−q)(p^{k−1} − q^{k−1})` | equal; positive |

Findings: none in the primary. Two scope notes recorded in the fold: the star's environment executions cover three orders per environment (each star law is `6^7` patterns; the runner stays near one minute), and the lemma's orthogonal form is needed only when `p = q`.

Attempts to refute (nothing refuted): U2's "only if" was re-read for a site `w` whose recorded set `A_w` overlaps other sites' recorded sets — the comparison pattern sets every value in every `A_{w'}` containing `y` to `b`, which is one consistent pattern, and every such factor moves in the same direction (all differences in the Lemma have the sign of `p − q`, or are positive in the orthogonal form); U4 was re-read for a unit some of whose sites are interior (all six neighbours inside) — the argument uses the *last* site of the order, which has all neighbours recorded whether inside or outside, and at least one inside neighbour by connectedness; U1's telescoping path was re-read for positivity (every conditional is strictly positive, so no ratio is undefined). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
