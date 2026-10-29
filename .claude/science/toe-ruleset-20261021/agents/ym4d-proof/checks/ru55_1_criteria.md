# ru55_1 — criteria (written 2026-10-29T00:36Z UTC, BEFORE checks/ru55_1_tc.py exists)

Question: RLARGE_U55 §2 (U3). Is (TC) infeasible with RLARGE's own ε_loc (re-derived independently of dag55_3), does Lemma
W-cb♯'s inequality chain close at its extreme, what does the repair change, and does the quietness-threshold form (SMALLNESS_DAG
§8.1) move ε^J_♮? Exact integers/Fractions only; square roots never enter a verdict (every comparison is made between squares,
which are rational here); a float may be printed only as a labelled display.

Inputs (d = 4, L = 3): A_d = (d−1)L(L−1)/2 = 9; n_ℓ = 4L³(L−1) = 216; n_P = 6n_ℓ = 1296; b_1(κ) = n_P + 12κ(1 + A_d)²;
δ_0 = min{1/(640N), 2/N³}; c_pr = 1/(640·53²); C_♭ = L² + 1 + (12 + 3L)A_d; ε^J_loc/ε_1 = 1/(157(1 + A_d)√N).
Grid: (N, κ) ∈ {2, 3} × {1, 1/4}; plus κ → 0 (b_1 → n_P) for G2b. All quantities are in units of ε_1 or ε_1² on the live
branch, whose conditions are gated (B).

(B) Branch gates (must PASS at every grid point or the point is not reported): B1 ε_loc's square-root entry is active
(4·N·b_1 ≥ 16, i.e. (ε_loc/ε_1)² = 1/(4Nb_1) ≤ 1/16); B2 η_q's middle entry is active for every ε_1 ≤ 10⁻³⁰
(1/(256NA_d) ≤ 1/(2L²) and 10⁻³⁰/(256NA_d) ≤ δ_0/A_d).

Gates (pre-registered verdict rules):
- G1 (TC as written). R² := ((16N+3)A_dη_q)²/(ε_loc/2)², computed from the two definitions (not from a closed form). Verdict
  FAILS iff R² > 1, HOLDS iff R² ≤ 1. Also verify R² == (16N+3)²b_1/(4096N) exactly (closed-form cross-check; PASS iff equal).
  Report R² exactly and R as an isqrt enclosure (display).
- G2 (U3's own fix vs CL (c)). U3 proposes ε_loc ≥ (16N+3)ε_1/(128N); CL (c) needs ε_loc² ≤ ε_1²/(4Nb_1). INCOMPATIBLE iff
  ((16N+3)/(128N))² > 1/(4Nb_1). G2a: same at the √2-relaxed ceiling ε_loc² < ε_1²/(2Nb_1) (all of CL's numerator given away):
  INCOMPATIBLE iff ((16N+3)/(128N))² ≥ 1/(2Nb_1). G2b: same as G2a with b_1 replaced by n_P (κ → 0, the plaquette term alone).
- G3 (W-cb♯ chain at its extreme). Scale t = 1, δ := A_dη* = t/(16N+3) (the supremum allowed in case (β2)). Check exactly:
  (a) t − 3δ ≥ 16Nδ; (b) t − 3δ ≥ t/2; (c) with x := t − 3δ: x/(2N) − 4δ ≥ x/(4N); (d) x²/(4N) ≥ t²/(16N).
  PASS iff (a)-(d) all hold at N = 2 and N = 3.
- G4 (a_cb♯'s entries, units ε_1², at ε_1 < t_pr so every min{·, t_pr²} takes its first argument): e1 := c_pr(ε_loc/ε_1)²/4,
  e2 := κ(ε_loc/ε_1)²/(64N), e3 := c_pr(η*/ε_1)² with η* := min{η_q, ε_loc/(2(16N+3)A_d)} (compared via squares).
  PASS iff e3 < min{e1, e2} at every grid point. Report a_cb♯/a_bad = e3/c_pr exactly, and verify exactly that
  (old third entry c_pr(η_q/ε_1)²)/e3 == R² (PASS iff equal at every point).
- G5 (a_D♯ = a_cb♯): PASS iff e3 < c_pr (= a_bad/ε_1²) at every point.
- G6 (quietness-threshold form, SMALLNESS_DAG §8.1): with η′ := η_q/R, compare (η′/2)² with (ε^J_loc/C_♭)² exactly
  ((η′/2)² = (η_q/ε_1)²/(4R²)). Report per point which entry of ε^J_♮ ≤ min{η′/2, ε^J_loc/C_♭} is the smaller; verdict
  "ε^J_♮ UNCHANGED" iff the ε^J_loc/C_♭ entry is ≤ η′/2 at the point (it was the smaller before, which is also checked).
- G7 (joint-collar variant, informational): R_J² := ((16N+3)A_dη_q)²/(ε^J_loc/2)² exactly; report.
Controls (each must behave as stated, else the script reports UNABLE TO DECIDE):
- C1 (G1 can output HOLDS): replace ε_loc by ε_1/4 (CL's other min entry) → R² ≤ 1 at every point (expected (35/64)², (51/96)²…
  i.e. HOLDS); and in that case η* == η_q (no shrink: the repair is the identity when (TC) holds).
- C2 (G3 can FAIL): rerun G3 with δ := 2t/(16N+3) (twice the supremum) → (a) must FAIL at N = 2 and N = 3.
- C3 (G4's equality test can FAIL): (old third entry)/e3 compared with R (not R²) must be unequal at every point.

Time correction (appended): the header says 00:36Z; `date -u` run immediately after writing this file printed 00:34:13Z. The file was written at 00:34Z, before any script.
