# la55_4 — extension of la55_2 to the link size s = 1/27 (covers Corollary WR (b)'s range eta <= 1/9) (criteria first)
Written 2026-10-29 UTC before checks/la55_4_bch27.py exists, after reading CODEX_REVIEW_DICT D5 (which notes BFT_A's WR (b) uses
2 + 9 eta <= 3 for eta <= 1/9). With ||x|| <= eta <= 1/9, every own link size obeys s_j <= L^{-(k-j)} eta <= eta/3 <= 1/27.
Same bound and same rigorous enclosure as la55_2 (f(sigma) with E_up = Taylor sum to degree 20 + 2 sigma^21/21!; Fraction only).
PASS criteria (pre-registered):
- E1: 6 s^2 + F_up(4/27) <= 9 s^2 at s = 1/27 (then for all s <= 1/27 by monotonicity of f(sigma)/sigma^2, la55_2 B3).
- E2: u_up(4/27) < 1.
- CONTROL (designed to FAIL): the same inequality at s = 1/24 (sigma = 1/6) must FAIL with the LOWER enclosure (i.e. even the
  lower value of 6 s^2 + f(4s) exceeds 9 s^2 there) — this shows the radius 1/27 is close to where this *bound* (not necessarily the
  true |q_p|) stops giving 9, so E1 is a test that could have failed.
Exit 0 iff E1, E2 pass and the control fails.
