# Results for queue item 8f

Source `be5e58b30`. All runs under `lab_ops.py numeric-lock`, holder `witness-8f`, one job at a time, BLAS threads 1, `nice`, 2 GB self-stop, memory free 68 to 69 percent. Criteria: `CRITERIA.md`, written first. No run stopped at the memory limit.

| Check | Outcome | Criterion |
|---|---|---|
| W1 `v0_jets.py` | d = 3, d = 4, 3010 triples: rank t_3 = 20, rank t_4 = 125, null space 2885, t_3 on it below 3e-15 of the top singular value | Pass. The first run had a family with no relations (null space 0), so it tested nothing; the family was rebuilt with products in both orders. Jet check 4e-6, not the 1e-6 registered: **departure**, a limit of the five-point fit |
| W2 `near_flux.py`, `near_scaled.py` | Fourier value inside every enclosure. Width at (3,3,2,2): 0.165 at grid 112, 112, 56, 56 | Pass after refinement. The first grid gave width 0.38 and failed the registered 0.2; the grid was refined and no criterion was changed |
| W3 `fibre_split.py`, `fibre_edge.py` | (a) L = 1: delta_pp = 0.1497888 against P_infinity(0) = 0.1497876, 8e-6 relative. (b) W-measurable coarse plaquette: fibre variance 0. Coarse plaquette variance independent of L to 6 digits. (c) delta >= 0 and Cauchy-Schwarz at every L. (d) L^4 delta_pp 0.147 to 0.127, 13.6 percent, from L = 15 to 21 for the pair; 2.1 percent at a block centre | Pass. At L = 1 the near off-diagonal value needs a finer theta grid (G = 12 gives -4.8e-5 against -5.54e-5), by aliasing at offset comparable to the grid; for L >= 3 G = 8 and 12 agree to 3 to 6 digits, so no table value uses L = 1 |
| W4 `singlet_rp.py` | Pairings 9, 3, 3 exact. Toy: E[Theta F F] = -0.01153(1), -0.002687(2) at h = 0.6, 0.4 against leading -0.01555, -0.003072, ratio 0.74, 0.87 | Pass, negative at about 1200 standard errors |
| W5 `abelian_td.py` | Ratio 1: -4e-16 relative. Ratio 1.01, 1.1, 2: -6.2e-7, -6.2e-6, -7.4e-5, 4 negative directions. Ratio 0.9, 0.5: -0.05, -0.53, 36 negative directions | Pass. Abelian analogue only |

What these establish: W1 and W4 test proved statements and can only refute them. W2's enclosures are computed bounds, with rounding far below their width. W3's values are computed values, not bounds, and the L^-4 trend is a trend. None of this says anything about the actual Wilson law.
