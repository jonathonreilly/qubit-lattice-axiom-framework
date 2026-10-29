# rl55_2 criteria (written 2026-10-29T04:4xZ, after rl55_1 ran, before rl55_2.py exists)

Purpose: decide, exactly, whether the support N_c of a soft density (the level-l links used by the 24 L^4 S4' words of a
level-(l+1) link c) EQUALS the set Omega_c of all level-l links with both endpoints in Box(c) (rl55_1's box). If yes, the
soft density needs no enlarged patch: every gradient pair and every monotone oscillation path used in RLOC55's delta bound
consists of links of supp D_c itself, and Codex BFT4W W1's boundary objection is void for soft densities (it remains for
Wilson Hoelder pairs, handled analytically in RLOC55).

Model: identical to rl55_1 (same word construction, d = 4, L in {3, 5}, all four mu, integer arithmetic only).
Gates:
- Q1: N_c == Omega_c as sets of (base point, direction), for every mu and both L.             PASS iff all equal.
- Q2: for every direction nu and every two nu-links b, b' in N_c, every link of the coordinatewise-monotone staircase
      of nu-links from b to b' (all intermediate base points in the rectangle spanned by b, b') lies in N_c.
      (Implied by Q1 and convexity of Box; checked directly on all pairs for L = 3, on the per-direction bounding
      rectangles for L = 5.)                                                                   PASS iff true.
Control (must fire):
- K1: with the y-average restricted to y = c_X only (one word family per order), N_c is a strict subset of Omega_c.
      FIRES iff N_c != Omega_c for some mu. (Shows Q1 is not automatic.)
Overall: PASS iff Q1, Q2 PASS and K1 FIRES; otherwise FAIL with the failing gate named (no verdict on the claim).
What this cannot decide: anything analytic; the Wilson-pair patch (not a soft density).
