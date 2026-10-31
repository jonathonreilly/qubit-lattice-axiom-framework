# ba7 criteria (BFT lane A, session 7). Written before checks/ba7_s7.py exists (see BFT_A_LOG for the file times).

Tests statements of BFT_A §31 (PRE-STATED, session 7). Thresholds are exactness tolerances, inequality checks, the
a-priori factor 2 and trend rules. No constant derived in session 7 appears here (the 12 of Lemma IP is part of the
pre-stated statement, §31.1, and is tested as stated). Model: the matrix-free abelian chain of checks/ba5_y.py
(read-only import; L = 3, κ ≡ 1, d = 4), its Qop/QTop, d* = Σ_μ backward differences (ba6 div1), p = the (0,1)-plaquette
at the origin.

- **E1 (Lemma TD), k = 2, T = 2.** Random S'_0 (level 0, cube side 5), S'_1 (level 1, cube side 3); S_0 := S'_0 -
  (T'_0 - Π_ccT'_0) with T'_0 := S'_0 + Q_0^TS'_1, S_1 := S'_1. ζ_1 := Π_cc(random level-1 1-form on a cube of side 3).
  b_1 := S_1 + ζ_1, c_1 := S_1 - b_1, c_0 := S_0 + Q_0^Tb_1, residual source s_0 := -b_1.
  - (a) composite-co-closed: max|d*(S_0 + Q_0^TS_1)| ≤ 1e-10·max|S|.
  - (b) level-wise co-closed: max|d*c_m| ≤ 1e-10·max|c_m| for m = 0, 1.
  - (c) outputs: solving with source S and with (c, s_0), max|Δf_0| ≤ 1e-8·max|f_0| and max|Δr_j| ≤ 1e-8·max|r_j| (j = 0, 1).
  - (d) restriction formula: u_1 := d*b_1 obeys max|u_1 + (d*S_0)|_{roots}| ≤ 1e-10·max|d*S_0| for the root offset
    o ∈ {0, 1} (root of block Y = 3Y + o·(1,1,1,1)) that the code uses; PASS iff it holds for one of them (reported).
  PASS iff (a)-(d).
- **E2 (Lemma IP), level 0 of the (k, T) = (2, 2) torus (side 18), s = 3 and s = 9.** I_s := s³Q_str^T (Q_str of ba6
  qstr, its transpose implemented directly), 𝔐_s := block mean per component.
  - (a) transpose: |⟨Q_strv, u⟩ - ⟨v, Q_str^Tu⟩| ≤ 1e-12·(|⟨Q_strv, u⟩| + 1) for random v, u; (b) I_s1 = 1 to 1e-12;
  - (c) Poincaré: Σ|Y - I_s𝔐_sY| ≤ 12sΣ|∇Y| for Y in {random normal, smooth (cos waves, wavelengths = torus side), a
    half-space step in one coordinate, one level-l component at a time}. Ratios reported.
  PASS iff (a)-(c).
- **E3 (depth signal for U_H and D_N of §26.5).** (k, T) ∈ {(1, 1), (2, 1), (3, 1), (2, 3)}; (3, 1) and (2, 3) have the
  same fine torus (side 27).
  - **H3a (factor 2, same fine torus):** U_H(3, 1) ≤ 2·U_H(2, 3).
  - **H3b (depth trend at T = 1):** U_H(3, 1) - U_H(2, 1) ≤ U_H(2, 1) - U_H(1, 1) + 0.02·U_H(2, 1).
  - **N3 (factor 2):** D_N(3, 1) ≤ 2·max(D_N(2, 1), D_N(2, 3)).
  Informational: S1 = Σ|dY^p_0| at each point; CG residuals.
  If a (k, T) case cannot be run (code error at T = 1), the criteria that use it are reported N/A, not PASS.
- Resources: every part < 20 min and < 1 GB RSS. Lock, nice 10, threads 1, python3 without -I, no timeout, no trap.
