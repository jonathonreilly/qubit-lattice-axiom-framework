# r55k_3 — POST-HOC criteria (written after r55k_2_out.txt, BEFORE checks/r55k_3_sharp.py exists)

Reviewer model: claude-opus-5-5. Same arithmetic rules as r55k_1. POST-HOC, labelled so.

Motivation (observed while writing up r55k_2): CONST_T §2.5 replaces the telescope's exact factor Ĉ^{Σ_{i<i_*}1/p_i}
= Ĉ^{1−2^{−i_*}} by Ĉ (valid since Ĉ ≥ 1) and, separately, F by its maximum over R. The two bounds are attained at
different R (F is largest where i_* is smallest, i.e. where Ĉ^{−2^{−i_*}} is smallest), so C_T = √6·F_max·B·Ĉ can be
loose. The sharp version of the SAME route is C_T^♯ = √6 · sup_{R ≥ R_0} B_{i_*(R)}(8)·F(R)·Ĉ^{1−2^{−i_*(R)}}, with
B_i(8) the partial β-product (P-max). Within a block of constant i_* only F varies, and log F is decreasing-then-
increasing there, so block endpoints suffice; the i_* → ∞ limit 16/α²·B(8)·Ĉ is included as a candidate.

- S1  For the printed allocation (Stage-2 budget R/2 − 4, R_0 = 64), allocation (a) (R/4 − 3, R_0 = 64) and
      allocation (b) (7R/16 − 3, R_0 = 256, Stage-1 coefficient 65536), at q ∈ {8, 11, 12, 16, 100, 1000, ∞}:
      REPORT C_T^♯, the R/i_* attaining it, C_D (c_N = 2, Λ(q)), ε_1^cut, the real q with C_D = 6.7·10¹⁵, and the
      lever obj(∞) − obj(8).
- S1-i  PASS ("CONST_T's √6·F_max·B·Ĉ is within ×1.1 of the sharp sup at q = 12, printed allocation") iff the ratio ≤ 1.1.
- S1-ii PASS ("q = 12 meets C_D ≤ 6.7·10¹⁵ under EPSSTAR's own radii, sharp accounting") iff C_D(12; a) ≤ 6.7·10¹⁵.
- S1-iii PASS ("the 24.089 lever survives sharp accounting to 0.05 decade", allocation (b)) iff |lever − 24.0891| ≤ 0.05.
