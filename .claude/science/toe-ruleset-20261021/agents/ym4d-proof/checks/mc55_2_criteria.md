# mc55_2 — criteria (written 2026-10-29T06:05:18Z, before any mc55 script exists)

Purpose: verify exactly the quintic-tent facts used by MINCB55 Lemma GI_j (the interpolating lift) and the blend constant.
Exact polynomial arithmetic over Q (coefficient lists of Fractions); algebraic numbers only through exact squares.

Object: s5(t) := 1 - 10 t^3 + 15 t^4 - 6 t^5 (BFT_B "quintic tents"). Control: s3(t) := 1 - 3 t^2 + 2 t^3.
Gates for s5 (all must hold):
- T1: s5(t) + s5(1-t) == 1 as polynomials.
- T2: s5(0) = 1, s5(1) = 0, s5'(0) = s5''(0) = 0, s5'(1) = s5''(1) = 0 (C^2 gluing at both ends of the tent).
- T3: s5'(t) == -30 t^2 (1-t)^2 as polynomials (hence s5 is monotone and 0 <= s5 <= 1 on [0,1]).
- T4: max_[0,1] |s5'| = 15/8: |s5'(1/2)| == 15/8 and 15/8 - 30 t^2 (1-t)^2 == 30 (t^2 - t + 1/4)(something >= 0) verified via the
  identity 1/4 - t(1-t) == (t - 1/2)^2.
- T5: max_[0,1] |s5''| < 289/50 (= 5.78): s5''' has roots r solving 6 r^2 - 6 r + 1 = 0; reduce s5''(t)^2 modulo 6t^2 - 6t + 1 to
  an exact rational constant c and check c < (289/50)^2; also s5''(0) = s5''(1) = 0.
- T6: max_[0,1] |s5'''| = 60: |s5'''| at t = 0, 1/2, 1 equals 60, 30, 60, and s5'''' has its single root at 1/2.
- T7: the 1-D tent chi(z) := s5(|z|) (0 for |z| >= 1) has chi(0) = 1 and chi(n) = 0 for integers n != 0, and chi(t) + chi(t-1) = 1
  on [0,1] (T1).
- T8: the d = 4 blend constant: max over multi-indices |beta| <= 3 of prod_nu sup|w^(beta_nu)| with sup|w| = 1, sup|w'| = 15/8,
  sup|w''| <= 289/50, sup|w'''| = 60 equals 60; C_blend := 2^4 * 60 * 4 = 3840 (the factor 4 = max L^1 distance between cell
  corners in units of D_1).
Designed control (must FAIL T2, otherwise the check is NON-DISCRIMINATING and the verdict is FAIL): s3 satisfies T1 but its second
derivative at 1 is 6 != 0, so T2 must FAIL for s3.
Verdict: PASS iff T1-T8 hold for s5 and T2 FAILS for s3.
