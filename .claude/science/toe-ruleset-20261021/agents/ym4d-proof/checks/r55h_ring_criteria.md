# r55h_ring — criteria (written BEFORE checks/r55h_arith.py exists; supplements r55h_arith_criteria.md).
# Reviewer: claude-opus-5-5. RECORDS ONLY: every item below evaluates a formula; no item has a PASS/FAIL threshold,
# because the formulas (the reviewer's sharpened ring accounting) are derived in this review and so may not be
# pre-registered as constants (brief rule 4). Exact Fractions + rigorous log enclosures, as r55h_arith.

Inputs as r55h_arith_criteria.md (a = 1e-86, beta_- = 0.186, L = 3, c_A = 0, c_U = 1, C_l = 1, R = 0, s6 constants
C_sh = 81, h_n = 10002, h'_n = 10001, h_D = 10000, c_att(8) = 320001).

R1 (open ring, merged): relaxation Col(N_1(X)) ⊇ Col(Y); pair count <= sum_{r>=1}|Sigma^r X| <= ||X||_sh, so c_+ = c_A + c_U
   (no ring surcharge). Record g2CRC, n_T, c_f = 6561 c_+ and the REL-boot / HIST-sum ceilings (HIST as written and
   with H-geo') at c_+ = 1.
R2 (closed ring at level j, merged): pair count <= 81|X| + sum_{r>=1}|Sigma^r X| <= ||X||_sh + 80|X|, |X| = 81n + |Y|;
   so b_n -> b_n + 6480 c_U, the per-Y constant c_att -> c_att + 80 c_U/c_+ (i.e. x_* gains e^{80 c_U}), b_D unchanged.
   Record g2CRC, n_T, the (S1) ceiling, and the ratio of g2CRC(R2) to HW's x82 row (1.85835e-96) and x17 row (8.96376e-96).
R3 Record, for the x82 bound as HW tabulates it, the HW-route binding ceiling min{(S2), REL-boot, HIST-sum} with HIST as
   written (this is the number later files call "g2_CRC at the x82 ring" without the HIST minimum).
R4 Record decades (log10) of each R1-R3 ceiling against 2.5e-152 and against 1e-94.
