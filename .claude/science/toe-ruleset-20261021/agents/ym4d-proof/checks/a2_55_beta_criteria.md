# a2_55_beta — pre-registered criteria (written before the script exists)
Input taken verbatim from CODEX_REVIEW_ALIGN F5 (not recomputed here): for the 5-adic 4-point DD scheme, ‖S_c^5‖²·5^5 = 51447766041/30517578125,
i.e. ‖S_c^5‖² = 51447766041/5^20. C^{1,β} is certified at depth n by ‖S_c^n‖ ≤ L^{−nβ} (the criterion al55_sub used: "norm²·L^n < 1" for β = 1/2).
- **B1 PASS iff** 51447766041^5 < 5^77 exactly (integers) — certifies β = 23/50 (‖S_c^5‖² ≤ 5^{−4.6}).
- **Control CB (must FIRE, i.e. the inequality must FAIL):** 51447766041^10 < 5^153 (β = 47/100) is false — shows the certificate's margin is
  below 0.47.
Cannot decide: the input value itself; regularity at other depths; anything about L ≥ 7.
