# SF_LOG: lane F (small-field package (SF^J)_k), session 1 (2026-10-28 UTC)

Role: lane F. Write access used: SF.md, SF_LOG.md, checks/s1_*. Nothing else edited. No commit, PR, push, CL or axiom edit.

## Timeline (UTC, 2026-10-28)
- 01:39:31 inputs' md5 recorded (SF.md header). Read: RLARGE v2 §0-§1, §4, §6-§8; RLARGE_INTEGRATION_LOG; PROOF header,
  Theorem CE block, CE-geo', Setting N5-bg through Proposition N5-sf_i, NAH1 setting, NAH-ind; HIST §8, §14.0-§14.1, §20-§23;
  PLD §9.3-§9.4, §15.2; FLOW §4 (SF clauses); REVIEW_S20 (bottom line, BG-unif template, repair route);
  REVIEW_S15_CONVERGENCE (node A DAG). PROOF has no [S21] block (session-21 curvature lemma not landed; not consumed).
- 01:39-01:44 SF.md §0-§2 written (decomposition and all pre-stated lemmas), before any proof.
- 01:45-01:46 SF.md §3 (proofs) written; post-proof annotations at 01:46 (SF-thr-k restated ⇐ (N5-unif); SF-A2^0 bound
  corrected by the √N normalisation of A; an unsupported numeric estimate of N_0(|𝒞|) removed).
- s1 criteria written before any s1 script: `stat`: checks/s1_criteria.md mtime 2026-10-28 01:47:31 UTC, size 4925 bytes;
  at that time `ls checks/s1_*` listed only s1_criteria.md (no script existed).
- 01:48 tool-artefact repair (disclosed): the Write of s1_criteria.md (and SF.md §2) had appended stray tool-markup lines after
  the last criterion line (`</content>`, `</invoke>` and a fragment of the next command). They were removed from both files;
  NO criterion text was changed (the removed lines are after "criteria are not edited after the script exists."). New
  mtime/size/md5 recorded on the next line; still no s1 script exists.
  criteria after repair: mtime 2026-10-28 01:48:14 UTC size 4541 bytes
  md5 6eb8a8793308ca9e6c5d33f046c3e042; ls checks/s1_*: checks/s1_criteria.md 
- 01:49 criteria REVISION (disclosed; before any s1 script existed): section A's model changed (R = 2 → 1, boxes = single blocks,
  m² = 1 → 4, 𝒴 = blocks (0,0), (6,6); A6 distance 5 → 2 blocks) because the first model made Ω(𝒴^+) the whole torus (A2 vacuous,
  A6 impossible). Recorded inside the criteria file. B-E unchanged.
  criteria final: mtime 2026-10-28 01:49:54 UTC size 4867 bytes, md5 cf928f420714402d12d4e9d8d487b9ff; ls checks/s1_*: checks/s1_criteria.md 
- 01:52 SF-J (2) corrected while waiting for the lock (exp chart full-measure only for N = 2; SU(3) counterexample); SF-A2^0's
  chart identity restricted to the small-fluctuation support. §4 (outcome, tally) written.
- 01:56:18-01:56:29 s1 run 1 under the numeric lock (load 2.9, 36% free, 285 MB). Reporting bug (numpy bool `is True`); labels
  unusable, numbers fine. Kept as checks/s1_out_firstrun.txt, s1_time_firstrun.txt.
- 01:57 post-run fix 1 (reporting only). 02:08 SF-thr constant 1.0107 → 1.0108 after reading E4's value.
- 02:50:08-02:50:19 s1 run 2 under the lock (waited ~52 min for another holder; load 2.3, 43% free, 302 MB). Numbers identical.
  OVERALL FAIL as pre-registered (E4 only: 1.010721 > 1.0107, a 5th-digit slip inherited from HIST §20.0 (F1); uses are 1.011).
- Lock: acquired with the mandated mkdir loop, released with exactly one rmdir per run; no trap; no timeout; python without -I.
- No commit, PR, push, CL or axiom edit. Files written: SF.md, SF_LOG.md, checks/s1_criteria.md, s1_sf.py, s1_out.txt,
  s1_time.txt, s1_out_firstrun.txt, s1_time_firstrun.txt.

# Session 2 (2026-10-28 UTC)

Role: lane F, session 2. Write access used: SF.md, SF_LOG.md, checks/s2_*. Nothing else edited. No commit, PR, push, CL or axiom edit.

## Timeline (UTC; file times from `stat`, local EDT = UTC - 4)
- Before 03:45: read REVIEW_SF_S1 (binding) in full, SF.md, SF_LOG.md, HIST §25.4-§25.6, PROOF Theorem CE, CT♯/RW/RW-triv/N5-sf0,
  B-NA-red/(G♯)/(R♯)/BNA-F1-F3, [S15] items, (R♯_ω), [S21] NAH-unif + N5 status, RTARGET §33-§35, RLARGE l.49-80/l.681, PLD
  l.1110-1120, HIST l.1768-1778/l.1185. Coordinator correction received (sup-norm (a5-G) is false, REVIEW_HIST_S4 S4-1; restate in
  the §33 pair; (a5-U) and the energy hypothesis on R_{3ε_1} with s_5 ≤ ε_1/5); REVIEW_HIST_S4 S4-1/S4-2/fixes/verdict read.
- 03:45:30 SF.md §6 (session-2 pre-statements: STEP 2 Theorem CE-exp and corollaries; STEP 3 restatements, Lemma BS, G-pert,
  U-red, new names; STEP 1 new lemmas SF-J', SF-src, (SF-N♮)) appended, before any session-2 proof. (A heading timestamp first
  typed as "03:46-03:58" was corrected at once to the actual append time 03:45:30.)
- 03:46:33 checks/s2_criteria.md written (md5 366105b1c4ea59480bb5413412a144e7); `ls checks/s2*` before it: no match (no script).
- checks/s2_sf.py written after the criteria (birth 03:47:49 UTC, after the criteria at 03:46:33 UTC). STEP 1 fixes applied in place in §0-§4, each tagged [RSF1-fix].
- 03:52:08-03:52:17 s2 run 1 under the numeric lock (mkdir loop; acquired after another holder released; load 4.00 at
  acquisition, 50% free; nice 10, BLAS/OMP threads 1, python3 without -I; 8.8 s, peak RSS 61 MB; exactly one rmdir; no trap, no
  timeout). **OVERALL PASS 14/14** (A1-A4, B1-B3, C1-C2, D1-D3, E1-E2). No re-run, no post-run edit of the script or criteria.
- 03:53-03:55 SF.md §7 (proofs) and §8 (outcome, tally, owner notes) appended; then a placeholder timestamp in U-red's post-proof
  note was replaced by the actual time, and §8.1's tally sentence was rewritten for clarity (same numbers).

## s2 results (checks/s2_out.txt)
- A (LOC-s, d = 1 ring, kernel with no zero entry): Σ_SF_S = Φ to 0.0; F_S unchanged under re-drawing off B ∪ S (0.0); Cauchy
  bound max ratio 0.076; non-vacuous (1.8e-2; 3.0e-3 at |S| ≥ 3).
- B (HULL, d = 4, 7⁴ cubes, M = 2): connectivity, q(y) ∈ Y, length bound (equality attained), δ - Mn ≥ 1: all PASS.
- C: κ' = 469.036, w_8 = 0.02724, 273κ' + 1296w_8 = 128082.1; M_min = 3.1873e13 at m_1 = 4.83e-11 (W = 0.02717).
- D: Haar fraction of exp(D_N): SU(3) 0.9752, SU(4) 0.9486 (SU(5) 0.9257, SU(2) 1.0000); exactly one spread-< 2π traceless log per
  sample; reconstruction 3.1e-15.
- E: Lemma BS never violated (max slack -1.5e-2); 4(e^0.01 - 1) = 0.040201.
- Note on REVIEW_SF_S1 fix 15 (validate RW at s ≡ 1 before zero patterns): s2 implements no RW, so it does not apply; it stays a
  requirement for any future RW check.

## Files written this session
SF.md (§0-§4 tagged fixes; §6-§8 appended), SF_LOG.md (this block), checks/s2_criteria.md, checks/s2_sf.py, checks/s2_out.txt,
checks/s2_time.txt.

# Session 3 (2026-10-28 UTC)

Role: lane F, session 3. Write access used: SF.md, SF_LOG.md, checks/s3_*. Nothing else edited. No commit, PR, push, CL or axiom edit.

## Timeline (UTC; file times from `stat`, local EDT = UTC - 4)
- Before 04:25: read REVIEW_SF_S2 (BINDING) in full, SF.md, SF_LOG.md, PROOF.md (md5 4a7bbccc…; Theorem CE/CE-geo/TG/CE-geo',
  Setting N5-0, [S21] NAH-unif + [R21-fix] block, the whole [S22] block), HIST §25.1 (TERM-an), §25.4 (NORM-an), REVIEW_HIST_S4 M-3.
  04:25:21 md5: REVIEW_SF_S2 e0f0e111…, RTARGET 770cb551…, HIST 468e9f03…, SF ab0199f0…; `ls checks/s3*`: no match.
- 04:26:13 SF.md §9 (session-3 pre-statements: STEP 2 (CE-Q) with LOC-s′, QC, Theorem CE-Q, (CE-Q^∞); STEP 3 Lemma SF-N♮; STEP 4
  GEO-col, Theorem CE-col, CE-exp-col, Proposition RATE) appended, before any session-3 proof.
- 04:26-04:29 STEP 1 fixes applied in place, each tagged [RSF2-fix] (BG-1, SF-thr-2, SF-N-1 wording, OP-1/2/3 → operator half only,
  Remark (cost) CEk-2, §4.2/§4.3 stale text, SF-thr-k re-based on PROOF [S22] NAH-unif′, CE0-1 caveat deleted (2 places), CE0-2/CQ-1
  scope, CEk-1 (L-hol)_k → (L-loc)_k with the reason, CEk-2 inherited activities + rate non-closure → (CE-col), G♯-1/G♯-2, GPa-1
  ((G♯-patch) stated precisely), (MIN-reg) re-homed, GP-1/GP-2 (G-pert scope; "reading" withdrawn), src-1/src-2, §8.1-§8.2 rows,
  the five tautological s2 criteria marked).
- 04:29:22 checks/s3_criteria.md written (md5 0fdc251afd3c9f4c56f46dfdff9e158b; birth = mod 04:29:22); `ls checks/s3*` before: no match.
- 04:30:22 checks/s3_sf.py written (birth after the criteria).
- 04:33:31-04:33:35 s3 run under the numeric lock (`until mkdir …/locks/numeric`, acquired at once; load 3.34 < 8; nice 10;
  OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`, no trap; exactly one `rmdir`; 3.3 s, peak RSS 80 MB, exit 0).
  **OVERALL PASS 13/13.** No re-run, no post-run edit of the criteria or the script.
- 04:34-04:36 SF.md §10 (proofs) and §11 (outcome) appended. 04:37-04:38 the CE-Q proof (Steps 1-6) rewritten in place to absorb
  three in-line corrections made while proving (κ̂ := κ_c - 2κ_0 - 2; Steps 3-4 applied with κ := κ_c - κ_0 - 2, rate κ_c - 4κ_0 - 5;
  U_α := R̄_α^{(7)} so that the component structure is readable inside clusters, with the field bound 2ρ' + σ and (B1′)); disclosed
  in the text. 04:38-04:39 two constant fixes (cubic prefactor 512, not 2048; chart bound e^{1/64} - 1) and a rate-only caveat
  added to Proposition RATE. Final SF.md md5 63503687… (before this log block's last line).

## s3 results (checks/s3_out.txt)
- A (LOC-s′ edge test; pole 10⁻³ outside the refined domain): 0 violations in 791 sets (233 skipped: no admissible radius); max
  |F_S|/B_S = 1.08·10⁻⁴ (threshold 10⁻⁴: thin); the unrefined polydisc contains the pole for some S (refinement load-bearing).
- B (Lemma QC): scalar and 4-link block Hölder bounds hold in 400 trials; max linear ratio 0.787, cubic 3.2·10⁻².
- C (Lemma SF-N♮, SU(2)/SU(3), 22-factor loops): max (y - y_bg)/(c_ya) = 0.909 = ℓ/c_y (aligned samples attain y - y_bg = ℓa
  exactly); y_bg ≤ 2.2p_Lα always.
- D (arithmetic): κ̃_0 = 217.047; κ_0 + 2κ̃_0 + 3 = 588.41; rate closure at L = 3 for κ_c ≥ κ_c^* = 1149.92; the 273 route never
  closes on [3κ_0 + 3, 10⁸]; CE-Q shell sums bounded.
- Tautologies: none by design; D1-D4 are labelled ARITHMETIC (non-evidential).

## Notes for other owners
- **(MIN-reg) → lane D** (with (a5-U), (a3-q); REVIEW_SF_S2 D-6). It is the global half of (a5-U) renamed; lane F does not attack it.
  The "(Linear case …)" sentence of SF §6.2 belongs to lane D's (a3-q) linear-case target. HIST is not edited by lane F.
- (CE-Q^∞) (deep shells, field beyond the analyticity polydisc) is a U-variable large-field item: RLARGE §3.2 branch (ii) owner.
- Theorem CE-col is a re-proof of Theorem CE with collar linking; PROOF's ledger owner decides whether to carry it.

## Files written this session
SF.md (§0-§8 [RSF2-fix] edits; §9-§11 appended), SF_LOG.md (this block), checks/s3_criteria.md, checks/s3_sf.py, checks/s3_out.txt,
checks/s3_time.txt.

# Session 4 (2026-10-28 UTC)

Role: lane F, session 4. Write access used: SF.md, SF_LOG.md, checks/s4_*. Nothing else edited. No commit, PR, push, CL or axiom edit.

## Timeline (UTC; file times from `stat`, local EDT = UTC - 4)
- Before 05:14 (reading): REVIEW_SF_S3 (BINDING) in full, SF §9-§11 and the stale spots, SF_LOG, RLARGE §3.1-§3.4 (l.290-380),
  PROOF Theorem CE/CE-geo/TG (l.1857-1960), CE-geo' (l.2264-2295), NA-FP (l.3040-3075), Setting N5-bg (l.5255-5275).
  md5 at that time: REVIEW_SF_S3 fbf4d6d6…, SF 63503687…, SF_LOG 464a785c…, PROOF 4a7bbccc…, RLARGE 24a73553….
- 05:14-05:19: STEP 1 fixes applied in place, each tagged [RSF3-fix]: stale M (§4.3, §8.2); (B1′)/p ≥ 2/C^Q renaming in §9.1;
  §9.1 constants marked superseded; Q1 and Q2 in §10.1's statement; Q3, Q6; the 273-route note; SN-1 (exact 1.03984); SN-2 ((BGC)
  made an explicit hypothesis); C-1..C-5 wording ("μ_wn-mass", handoff withdrawn); tally ARGUED 1; s3 low-power labels.
  SF md5 after: c25ce091….
- 05:20:24: SF.md §12 (session-4 pre-statements: Setting CE-Q-col, Lemmas HALO, SH, Theorem CE-Q-col, RATE-Q; Lemmas GD, DL, SLc, TILT,
  Proposition RES, (SL-coer′), Proposition DX) appended, before any session-4 proof. SF md5 after: e50d66dd….
- 05:22:00: checks/s4_criteria.md written (birth = mod 05:22:00, md5 06c44d6a…). `ls checks/s4*` just before it: no match.
- 05:24:27: checks/s4_sf.py written (birth after the criteria).
- 05:25:24-05:25:32: s4 run under the numeric lock. The mandated `until mkdir …/locks/numeric` loop acquired the lock at once. Load
  5.87 < 8; 43% memory free just before. nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`, no trap;
  exactly one `rmdir`. 7.5 s, peak RSS 257 MB, exit 0. **OVERALL PASS 21/21.** No re-run, and no edit of the criteria or the script
  after the run. No process left running.
- 05:28-05:31: SF.md §13 (proofs) and §14 (outcome) written; appended at 05:31:19.
- 05:32-05:33: post-proof corrections, each marked [post-proof]:
  - SLc's domain ρ ≤ ρ_* (SF-src needs r_𝔫/2);
  - SLc-X's θ convention (factor 2 for TILT; a_θ := (1 - 4C'g_0²)/(4C_coer));
  - DX's kernel exponent: a wrong ε_1/8 conversion replaced by a_ker(ε_c) := branch (i)'s exponent;
  - the RT-1 tags in §10.3 and §11.1.
  Final SF md5 e6835ab9… (before this log block).

## s4 results (checks/s4_out.txt, md5 1cd744d2…)
- **A (Lemma HALO):** d = 2 and 3 tori, 70 trials. 0 violations of (a)-(e) (4124 pairs in (b), 3036 of them with ℓ ≥ 2; 42 in (c)).
  Negative control: "n ≥ ℓ" is violated 139 times, so the factor 4 log 2 in ℓ_j is load-bearing.
- **B (Lemma SH):** 96 grid points with ℓ_j ≥ 2 reached. Pointwise inequality: 0 violations. Shell-sum ratio max 1.4959 ≤ 2.
- **C (arithmetic):**
  - κ̃_0 = 217.0472, log B̃ = 574.677, log C̃_1 = 580.750; CE-col rate threshold 1149.921.
  - Norm threshold in the displayed form 1853.49 (log ratio 703.57 at 1149.92: the reviewer's numbers reproduced); in the next-input form
    2499.39.
  - CE-Q-col: rate threshold 1478.492; norm 2073.23 (displayed) / 2938.18 (next-input).
  - SN-1: 1.039844 (the rounded display gives 1.040070). Σ_{j≥1}e^{-(4^j-1)/8} = 0.841.
  - p_0: CE-Q-col 4.24·10⁴, against 7.2-7.7·10⁵ for session-3 CE-Q (M_W3 = 3.14·10¹⁴).
- **D:**
  - TILT: 0 violations, max ratio 0.344 (plain MC has infinite variance at θ = 0.9; the exact-tilt reference agrees).
  - RES (SU(2) 4×4): 5/5 witnesses with max|A| 0.35-0.50, |h| ≤ 6·10⁻¹⁷ and plaquette change ≤ 3.3·10⁻¹⁶.
  - Control: generic slice directions of the same size move plaquettes by 0.36-0.51.

## Notes for other owners
- **Withdrawn:** session 3's note "(CE-Q^∞) → RLARGE §3.2 branch (ii) owner". It was circular: branch (ii) ⇐ (SG^fl)_0 ⇐ SF's
  cluster expansion. Proposed order (SF §13.2): CE-Q-col (band) and DX (deep, priced by (SL-coer′) + bare positivity / branch (i) /
  TILT; CLS-sf at k ≥ 1) come before (SG^fl)_0. Owner note for RLARGE: read (SG^fl)_k's input "(SF)_k's cluster expansion" as
  "CE-Q-col + DX". RLARGE is not edited by lane F.
- **(SL-coer′)** is the nonlinear, local core of (FP-loc)_0's "uniqueness of the slice intersection on the chart" (PROOF NA-FP owner).
  Proposition RES shows the reviewer's defect-only wording is false on ker h_U (residual-gauge copies).
- Theorem CE-Q-col removes (M-Q). REVIEW_SF_S3 B-7's consumers (FLOW F-Π, RLARGE/HIST (I_k^E)(b), SF-blk/RATE) need no change on this
  route.
- RT-1 for whoever carries Proposition RATE: the d ≥ 1 norm iteration closes from κ_c ≈ 2499 (CE-col) / 2938 (CE-Q-col). The
  reviewer's ≈ 1854 is the same-rate form.

## Files written this session
SF.md ([RSF3-fix] edits in §4.3, §8.2, §9.1-§9.3, §10.1-§10.3, §11; §12-§14 appended), SF_LOG.md (this block), checks/s4_criteria.md,
checks/s4_sf.py, checks/s4_out.txt, checks/s4_time.txt.

# Session 5 (2026-10-28 UTC)

Role: lane F, session 5. Write access used: SF.md, SF_LOG.md, checks/s5_*. Nothing else edited. No commit, PR, push, CL or axiom edit.

## Timeline (UTC; file times from `stat`, local EDT = UTC - 4)
- Before 06:11 (reading): REVIEW_SF_S4 (BINDING) in full; SF §12-§14 (l.1351-1749) and spots l.56-165, 355-386, 1015-1072,
  1112-1131, 1200-1211; SF_LOG in full; HIST §20.0-§20.2 (Theorem MSG, MSG-loc′, MSG-loc; l.1182-1306) and (H-w) l.526-541;
  PROOF Lemma FP-ab + application (l.2440-2492), Proposition PG^{(k)} (l.2969-2985), Lemmas NA-alg/NA-crit/NA-inv and
  Proposition NA-FP (l.2995-3084), Setting N5-bg + Lemma N5-cov (l.5255-5284); RLARGE §3.1 end + §3.2 (l.300-332); PLD §15.2
  (l.966-1024) and §15.4 (l.1104-1146).
  md5 at 06:11: REVIEW_SF_S4 1b9d442f…, SF e6835ab9… (= session-4 final), SF_LOG 931bca87…, HIST 468e9f03…, PROOF 4a7bbccc…,
  RLARGE 24a73553…. `ls checks/s5*`: no match.
- 06:15:49: SF.md §15 ('PRE-STATED (session 5)': conventions; STEP 2 Lemmas MSG_0, W-Lip, GF-dec, BCH-L, Propositions FP-uniq, FP-sh,
  Theorem SLC-sh, Proposition DX′, Lemmas KF, DX-rel; STEP 3 (CH-c), (TH-ch), Proposition CH-assign, dependency order) appended, before
  any session-5 proof, before the [RSF4-fix] edits and before the s5 criteria. `stat` (local EDT): SF.md mtime 2026-10-28 02:15:49
  (= 06:15:49 UTC), size 207436 bytes, md5 2057708704de7d279b0e265a8d0c3052.
- 06:16:32: checks/s5_criteria.md written (birth = mod 06:16:32 UTC, size 5382, md5 ad0e4d718bd1e5e3c375fa334bb5be2c); `ls checks/s5*` just
  after: only s5_criteria.md (no script).
- 06:19:23: checks/s5_sf.py written (birth after the criteria). 06:21:07: pre-run desk fixes to the script only (G_meas computed as the
  (η, ω)-split row sum that GF-dec (e) defines; C's random sizes capped at 0.99r so no pair is skipped; F2's ε_bg printout restricted to
  the a_p entry, because the kernel coupling of DX-rel is the soft-kernel κ of Setting N5-bg, not CE's κ_0). No run had happened.
- 06:21:27-06:21:43: s5 run (the only run) under the numeric lock: the mandated `until mkdir …/locks/numeric` loop acquired it at once;
  load 3.74 < 8; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`, no trap; exactly one `rmdir`. 15.4 s,
  peak RSS 114 MB, exit 0. **OVERALL FAIL 19/20: D3 FAILED as pre-registered** (control: 0 of 12 Newton runs from O(1) starts converged,
  so no far Gribov copy was exhibited; "INCONCLUSIVE counts as FAIL"). Everything else PASS. No re-run; no edit of criteria or script
  after the run. md5: s5_sf.py 6edaee23…, s5_out.txt b9a1f55d…, s5_criteria.md ad0e4d71… (unchanged).
- 06:22-06:24: STEP 1 fixes applied in place, each tagged [RSF4-fix]: RT-1 citations (2499.39 / 2938.18 as THE iteration thresholds;
  1853.49 same-rate only; §10.3 and §13.3); CQ-1 (807.46 in §12.1; p_0 ≈ 6.45·10⁴ at κ_c = 2938.2 in §13.1, two places); HALO (b)
  tightness (4 log 2 needed); GD-1 (block constants C_i^{Q,B} ≤ L⁴C_i^Q, n_B, (M/L)⁴, (B1′)-(B3), a_*^B); DL-1 (4L⁴e^{μ·diam B} in
  a_deep; chart radius 1.011√N/2 in R_DL); RES-1 (1/N) and RES-2 (residual gauge averaged, not fixed; soft-gauge Gribov issue in
  (FP-loc)_0's uniqueness clause); SC-1..SC-3 in (SL-coer′); DX-1 (the pricing line is wrong as written; whole removed region; a′'s
  (P)/kernel exponent ARGUED); DX-2 (stage-0 citation → pointwise kernel bound; (O2) list); D-1 ((CH-c) named, in (O2)); D-2 ((DX-loc)
  uses only (H-w)'s (a)-(c)); D-3 ((O3) inputs completed); threshold note; k ≥ 1 halo-vs-torus caveat; §14.1 tally line (ARGUED 2,
  (CH-c), (DX-rel) recorded). SF md5 after: 5e68178b….
- 06:27-06:29:56: SF.md §16 (proofs: MSG_0, W-Lip, GF-dec, BCH-L, FP-uniq, FP-sh with (FP-det) ARGUED, SLC-sh, DX′; KF, DX-rel; CH-assign
  and the exact dependency order O0-O6) and §17 (outcome, tally, check s5) appended. Corrections made while proving, each marked
  [post-proof]: FP-uniq's principal-log condition (ε^thr_N for N > 12); FP-sh's c-number c_N^{-n_Λ}; DX′ does not use (TH-ch); KF/DX-rel
  notation κ_s (soft-kernel coupling, not CE's κ_0); DX-rel's (TH-bg) must include the background kernel values.
- 06:30:47: second [post-proof] correction in DX-rel: holes are 4^d blocks, not 3^d (n_R = 82944, n_1 = 497664, n_K = 1024 at d = 4, L = 3;
  ε_bg ≤ 2.51·10⁻⁶² by hand from F2's τ_c). s5 F1/F2 printed the 3^d values; the script and its output are NOT edited. SF md5 83843fef….

## s5 results (checks/s5_out.txt, md5 b9a1f55d…): OVERALL FAIL 19/20 (D3)
- A (MSG_0): 0 violations (A1 1440 intra-block links, max ratio 0.221; A2 1440 ladder tests, max ratio 0.839); identity, locality, orbit
  invariance exact; negative control A7: a corner root breaks orbit invariance (1.93).
- B (GF-dec, d = 2): λ_min(Γ^TΓ)/c_D = 7.9-14.8 incl. Haar-random backgrounds; ||D_U||² ≤ 8; σ_min(M_X)L^d ≥ 2.06; decay bound ratio ≤ 0.035;
  inverse formula to 3·10⁻¹⁵. Measured decay 1.0-2.1 per block vs bound 1.39·10⁻².
- C (BCH-L): 0/2080 violations; max ratio 0.546 (c_g = 25.85).
- D (FP-uniq): Newton converges, ||λ_*|| far below the bound; 10/10 in-ball starts per case give the same zero. **D3 FAILED (control):
  0/12 O(1) starts converged; no far Gribov copy exhibited.**
- E (KF): 0/4200 violations of both bounds; the y⁴ correction never needed in samples.
- F: c_D = 1/324, m_FP = 3.858·10⁻⁴, G_∞ ≤ 5.90·10²³; chain ζ = 2.19·10⁻⁵⁵, r_sol = 1.03·10⁻³⁰, τ_c = 4.34·10⁻⁵⁹ consistent; 807.4566.

## Notes for other owners
- **PROOF NA-FP / (FP-loc):** Propositions FP-uniq and FP-sh (SF §16.1) prove the stage-0 uniqueness clause on a shrunk chart, with an
  explicit, background-independent inverse of χ_UΓ (GF-dec). What remains is (FP-det) (ARGUED: walk expansion of log det).
- **RLARGE (proposed, not edited):** read (SG^fl)_k's "(SF)_k's cluster expansion" as "CE-Q-col (ρ_band) + DX′ + (DX-loc) + (CH-c) per
  CH-assign"; add τ_c and (TH-ch) (ε_1 ≤ τ_c) to [v2-C]. Under (TH-ch) branch (ii) prices no part of the out-of-chart region.
- **STEP 3 premise corrected:** (CH-c) is NOT priced by branch (ii) (that would be circular for any defect band inside the cut-good law);
  it is empty in-step under (TH-ch), or priced by DX-rel.
- **HIST (MSG) owner:** MSG_0 is the one-step MSG gauge with the background as reference; no box needed at one scale.

## Files written this session
SF.md ([RSF4-fix] edits in §10.3, §12.1, §13.1-§13.3, §14.1; §15-§17 appended), SF_LOG.md (this block), checks/s5_criteria.md,
checks/s5_sf.py, checks/s5_out.txt, checks/s5_time.txt.

# Session 6 (2026-10-28 UTC)

Role: lane F, session 6. Write access used: SF.md, SF_LOG.md, checks/s6_*. Nothing else edited. No commit, PR, push, CL or axiom edit.

## Timeline (UTC; file times from `stat`, local EDT = UTC - 4)
- Before 06:59 (reading): REVIEW_SF_S5 (BINDING) in full; SF §15-§17 (l.1806-2201); SF_LOG l.170-240; RLARGE l.50-80, 250-268,
  360-372; PROOF Lemma FPq (l.5630-5640), Lemma BR1 (l.5661-5700), 𝔠_∞ (l.5600-5606, l.5859), N5-sf0 gap (l.5414-5420).
  md5 at 06:59: REVIEW_SF_S5 4449034c…, SF 83843fef… (= session-5 final), SF_LOG fa3a8d57…, RLARGE 24a73553…, PROOF 4a7bbccc…,
  HIST 468e9f03…, PLD 4db9b142…. `ls checks/s6*`: no match. The numeric lock directory existed at 06:59 (held by another agent
  since 06:55 UTC).
- 07:02-07:06 (EXPLORATORY, scratch only, not a check; each run under the numeric lock, acquired at once, one rmdir each):
  sf6/explore1.py (1.1 s, 490 MB) and sf6/explore2.py (8.7 s, 36 MB): d = 4, L = 3, U = 1 scalar problem. Findings used to choose the
  session-6 route (not cited as evidence): the Kato block gap and the periodic-cell gap coincide (0.0852175); the U = 1 inverse of
  χΓ has total block row sum ≈ 34.7 (torus 6⁴), η-column ≈ 32.5; its entries decay ≈ e^{-1.85} per block along an axis and much faster
  off-axis (n = 13 torus).
- 07:09: sf6/arith1.py (scratch arithmetic for the STEP-1 table, under the lock, < 1 s; reproduced in s6 F1).
- 07:09-07:15: STEP 1 fixes applied in place, each tagged [RSF5-fix] (20 tags): FP-uniq tightness ((I1) = 0.4995, (I4)/r = 0.990,
  ζ_max = 2.209·10⁻⁵⁵, ∝ G_∞^{-2}); D3 = failed positive control that does not test the proof, D2 without demonstrated sensitivity (§16.1,
  §17.3); DX′-1 (coupling ceilings evaluated: g_{DX′}² ≈ 1.49·10⁻²³⁷/(C_ΩN′²f⁸) with RW-ℓ²'s gap, ≈ 1.58·10⁻³⁰⁹/(…) with the product-rule
  gap; DX-rel hole ceiling g_0² ≲ 1.6·10⁻¹²⁶); DX′-2 (re-tuned (B1′), j_max, a_*^B = 1.08·10⁻¹²³/N_r², band window ≈ 5.1·10⁻⁶⁷/max{N_r, 2N_μ});
  FS-1, FS-2, FD-1, DR-1 notes; CH-1 (every plaquette/mismatch > τ_c, inter-cube included, priced by DX-rel + (DX-loc), never via RLARGE
  (D-c)/(D-b) → §3.4 → branches (ii)/(iii)); CH-2 (∂Λ(𝔥)-adjacent family = RLARGE (D-d)/E10, OPEN; e^{B_0} a cost); CH-3 (E_good on a
  V-event 𝒱^sf(Λ′) with local ε_bg); (CH-c) CONDITIONAL ⇐ DX-rel + (DX-loc) + E10 + CH-3; TH-1 ((TH-ch′) ε_1 ≤ min{τ_c, τ_c/(2C_bg),
  ε_bg^{(TH-bg)}/C_bg}, C_bg = 1.39·10⁴⁰ from BR1 (iii); ε_1 ≤ 1.81·10⁻¹⁰² at session-5 constants) with the derived-constant table (n_* ≈
  2.9·10²⁰⁵, ≈ 108 final levels); O4 corrected; owner notes; §17.1/§17.2 status rows. SF after STEP 1: 2026-10-28 03:11:26 EDT, 262005 bytes,
  md5 46516d07….
- 07:16:13: SF.md §18 ('PRE-STATED (session 6)': conventions; STEP 2 Lemmas CD, CHEB, RINV, Proposition GF-A, Lemmas KKT, BOXG,
  Proposition GF-B (computer-assisted), Corollary CHAIN-6; STEP 3 Lemma FH, the (DX-loc) decomposition, the (GF-dec)_k remark) appended,
  before any session-6 proof and before the s6 criteria; it cites only PROVEN items (PROOF FPq (i), GF-dec (a)-(d), NA-FP (i)-(ii),
  MSG_0, (F2)/(F4), FP-uniq). `stat` (local EDT): SF.md mtime 2026-10-28 03:16:13 (= 07:16:13 UTC), size 271441 bytes, md5
  cd64bc7a13b47ffc42dccf557b7b9240. `ls checks/s6*`: no match.
- 07:18:35: checks/s6_criteria.md written (birth = mod 07:18:35 UTC, 6472 bytes, md5 3964da2e…); `ls checks/s6*` just after: only
  s6_criteria.md.
- 07:21:58: checks/s6_sf.py written (birth after the criteria). 07:22-07:23:48: pre-run desk fixes to the script only, no run had
  happened: RINV's spurious "R = R/L^d" rescaling removed (R must carry L^d/(2d), as pre-stated); per-block Λ_res bases instead of a
  dense Q on the 13×13 torus (memory); GtG dropped before the dense inverse (memory); relabelling memoised; Frobenius sums via
  np.sum with the same γ_n bound; chain grid ρ ∈ [500, 540] step 0.5 and 150 bisection steps (time). No criterion touched.
- 07:23:55-07:24:28: s6 run (the only run) under the numeric lock: the mandated `until mkdir …/locks/numeric` loop acquired it at
  once; load 2.13 < 8; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`, no trap; exactly one `rmdir`
  (07:24:28). 32.4 s, peak RSS 776 MB (footprint 862 MB), exit 0; pgrep empty afterwards. **OVERALL PASS 17/17.** md5: s6_sf.py
  dd959a93…, s6_out.txt 7e123ac5…, s6_criteria.md 3964da2e… (unchanged). checks/s6_time.txt written 07:26:29 from the run's
  /usr/bin/time record. No re-run; no edit of criteria or script after the run.
- 07:27-07:28:34: SF.md §19 (proofs: CD, CHEB, RINV, GF-A, KKT, BOXG, GF-B (computer-assisted), CHAIN-6, FH, FP^𝔥; the (DX-loc)
  decomposition; the derived-constants table) and §20 (outcome, tally, check s6) appended.
- 07:29:48 (SF mtime; SF md5 62079998…, 294602 bytes): one [post-proof] correction in Corollary FP^𝔥 (found on re-reading): with g = 1 on hole sites the boundary links are not
  small; corrected to a two-step fixing (exact block-internal complete axial gauge on every hole block first, then FP-sh^𝔥). Also a
  [post-proof] note in §19.4: s6's "inf" in a REPORT line is a float overflow; the value is ≈ 3·10¹⁷(0.5/ε_1)⁴ by hand.

## s6 results (checks/s6_out.txt, md5 7e123ac5…): OVERALL PASS 17/17
- A: c_D^K = 2663/31250 re-certified exactly (min pivot 1.12·10⁻⁴; control at 0.0853 fails); CHEB ratio ≤ 0.28 at d = 2 (control 10θ violated);
  RINV tight (0.92-0.945 of c_R); **G^A = 6.472145·10⁹, m_FP^A = 0.146219/block** (every background).
- B: relabelling exact to 4·10⁻¹⁶; **certified G^♯(0) = 37.043038** (e_1 = 3.34·10⁻³, w = 1000); float estimate 35.730 (ratio 1.037); d = 2 end-to-end:
  measured 8.6896 ≤ certified 9.2278 at a gauge-rotated, nearly flat background; the gauge step is load-bearing (entries differ by 2.0).
- C: **τ^A = 3.602·10⁻³¹** (PROVEN admissible), **τ^♯ = 1.0995·10⁻¹⁴** (⇐ (GF-B^𝔥)); (TH-ch′) ε_1 ≤ 1.50·10⁻⁷⁴ resp. 4.59·10⁻⁵⁸ (C_bg-dominated);
  FD-1 holds from M ≥ 6.05·10⁴.
- D: frozen holes keep the gap and the CHEB decay; at U = 1 a 3-block frozen hole changes G_meas by 0.03% (d = 2).
- F: the STEP-1 table reproduced.

## Notes for other owners
- **PROOF NA-FP / FPq owner:** GF-A (every background) and GF-B (computer-assisted, locally small backgrounds) bound (χ_UΓ)^{-1} in the
  sup-block norm by 6.47·10⁹ and 37.04; PROOF FPq (i)'s c_D(3) is the input. KKT's bordered form has integer entries at U = 1.
- **RLARGE (proposed, not edited):** at stage 0, §3.4's plaquette leg above τ_c for (D-b)/(D-c) is DX-rel (in-step), not branches (ii)/(iii);
  (D-d)/E10 is on lane F's path; [v2-C]'s threshold list should carry τ_c and (TH-ch′). Every lane's ε_1 = 0.5 numerics are illustrative,
  not admissible; with the PROVEN τ_c, ε_1 ≤ 1.5·10⁻⁷⁴ and n_* ≈ 4·10¹⁴⁹.
- **BR1 owner (PROOF [S20]):** C_bg = 1.011√N·36p_L𝔠_∞ ≈ 1.4·10⁴⁰ is now the binding lever for ε_1 (𝔠_∞ ≈ 2·10³⁷); any sharpening of 𝔠_∞
  moves ε_1 linearly.

## Files written this session
SF.md ([RSF5-fix] edits in §15.0, §15.2, §16.1, §16.2, §16.3, §17.1-§17.3; §18-§20 appended), SF_LOG.md (this block), checks/s6_criteria.md,
checks/s6_sf.py, checks/s6_out.txt, checks/s6_time.txt.

# Session 7 (2026-10-28 UTC)

Role: lane F, session 7. Write access used: SF.md, SF_LOG.md, checks/s7_*. Nothing else edited. No commit, PR, push, CL or axiom edit.

## Timeline (UTC; file times from `stat`, local EDT = UTC - 4)
- Before 07:56:41 (reading only, no computation): REVIEW_SF_S6 in full (md5 cd663df8…); SF §18-§20 (l.2305-2588), §16.1 DX′ (l.2040-2100),
  §16.3 TH-1 (l.2141-2228); SF_LOG l.230-311; PROOF (md5 4a7bbccc…) l.5149-5236, 5255-5318, 5415-5588, 5596-5704, 5852-5873, grep of 𝔠_∞ / C_♭;
  checks/c36_nah1.py l.1-305 and c36C.out; revSF6/indep_cert.py l.1-60. md5 at 07:56: SF 62079998… (= session-6 final), SF_LOG 82083e0a…,
  RLARGE 24a73553…, HIST 468e9f03…. `ls checks/s7*`: no match.
- 07:57:19: SF.md §21 'PRE-STATED (session 7)' appended (the FIRST edit of the session; statements only, no session-7 constants): conventions;
  STEP 1 list; STEP 2 Lemma HO, Propositions CI-0, CI-bg, Corollary CI-BR1, Lemma CHEB-f, the DX′ re-evaluation; STEP 3 (GF-B^𝔥) target.
  `stat`: SF.md mtime 2026-10-28 03:57:19 EDT, 301976 bytes, md5 ce9f6be2…. `ls checks/s7*`: no match. One immediate correction of the
  heading's own time ("≈07:58" → "07:57:19", byte count unchanged) at 07:57:35 (SF md5 then 6aca0228…), logged here.
- 07:58-08:03:20 (SF mtime; 308948 bytes, md5 e6cc979d…): STEP 1, REVIEW_SF_S6's binding fixes applied in place, each tagged [RSF6-fix]
  (18 tags + the §21.1 mention): GB-1 (§19.2 GF-B proof step (3): the Y-uniform entry bound b(X, Z)); TH-2 ×4 ((TH-ch″) defined after
  TH-1 in §16.3; §19.2's "set by C_bg" sentence struck and the (TH-ch′) row qualified; §19.4's levers sentence struck and the ε_1-driven
  rows recomputed at 5.95·10⁻⁷⁷/C_♭ (C_♭ = 1: n_* 2.7·10¹⁵⁴/1.8·10¹⁵⁴, n_♯ 3.5·10¹⁶³-2.8·10¹⁶⁷ / RS 2.0·10³¹⁷-1.5·10³²¹, a_bad 1.8·10⁻¹⁵⁹,
  ≈ 81 levels; hand arithmetic, reproduced in s7 C6); §20.2's threshold line); FP-1 (FP^𝔥's wrong statement struck, the two-step
  statement written); FP-2 (scope in FP^𝔥, §18.2, §20.1 (DX-loc) and FH rows); tally (53 + 1; CD a citation); non-binding A-1/A-2,
  GB-2 (+ the reviewer's G^♯(0) ≤ 36.5473 recorded), E-3, E-4, the "44 orders" sentence.
- 08:00:5x-08:03:15 (EXPLORATORY, scratch sf7/, not evidence; under the numeric lock, acquired at 08:02:31, load 4.08, free 41%, one
  rmdir 08:03:15): sf7/ex1.py (44 s, peak RSS 397 MB): exact HO covariance of Õ_0 and 1 - Π under 3 generators, 0 mismatches; float
  λ_min on the 7⁴ grid 0.0407; column decay by ℓ^∞ shells on the 7-torus. The lock directory was held by another agent at 08:00.
- 08:05-08:08: a 1-second inspection outside the lock (python reading sf7/rows.pkl to get the common denominator of the exact rows;
  ≈ 100 MB): disclosed, not a numeric job of the session's design but a computation nonetheless.
- 08:09:17-08:10:4x (EXPLORATORY, under the lock, load 2.72, free 39%, one rmdir): sf7/ex2.py (one canonical column, R = 5, n = 12):
  81.7 s, **peak RSS 1.36 GB, footprint 2.24 GB: OVER the 1 GB budget (int64 index arrays and an unslabbed residual)**; disclosed. Its
  findings, used to choose the s7 method parameters (not evidence): 8 orbits of link types (sizes 64, 96, 32, 48, 48, 8, 24, 4); the
  column's residual type-sums at m = 0 total 0.24 (max 2.4·10⁻³), at m = 0.05 total 1.13 (so the m grid stops at 0.03); |K̃| column
  total 55.6; the residual sits at midpoint distances 16-68 (the truncation shell). s7_sf.py was rewritten to slab the residual and use
  int32 indices.
- 08:12:41: checks/s7_criteria.md written (birth = mod 08:12:41 UTC, 5062 bytes, md5 06238199…); `ls checks/s7*` just before: no match,
  just after: only s7_criteria.md. It quotes PROOF's constants only; R = 5, n = 12 and the m grid are method choices (logged above).
- 08:16:53: checks/s7_sf.py born (after the criteria). 08:17-08:18:03 pre-run desk fixes, no run had happened: the exact spot check
  compares Fractions (not a float difference); torus columns inverse-FFT'd one at a time (memory). A `python3 -m py_compile` syntax check
  at 08:18 created checks/__pycache__/s7_sf.cpython-313.pyc, which I removed at once (with the then-empty directory); nothing else.
  md5 at the run: s7_sf.py 05c1d69e…, s7_criteria.md 06238199….
- 08:18:31-08:24:29: s7 run (the only run) under the numeric lock: the mandated `until mkdir …/locks/numeric` loop acquired it at once;
  load 2.77 < 8, free 46% ≥ 35%; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`, no trap; exactly one rmdir
  (08:24:29). 358 s, max RSS 909 MB (867 MiB), **peak footprint 1.18 GB (over 1 GB on that measure; R1 used RSS)**, exit 0; pgrep empty
  afterwards; no __pycache__ (PYTHONDONTWRITEBYTECODE). **OVERALL PASS 17/17.** md5: s7_out.txt c97d39df…, s7_time.txt d5f5d16e… (lock
  record + /usr/bin/time, written 08:24:5x). No re-run; no edit of criteria or script after the run.
- 08:25-08:26:12 (SF mtime; 324498 bytes, md5 ceec42df…): SF.md §22 (proofs: HO, CI-0, CI-bg, CI-BR1, CHEB-f, the N5-sf0
  re-evaluation, DX′-1 and the derived rows; STEP 3 not attempted) and §23 (outcome, tally, check s7) appended.

## s7 results (checks/s7_out.txt): OVERALL PASS 17/17
- A: exact rows reproduce N_0(|Õ_0|) = 10462237/410670; exact HO covariance (0 mismatches; control 490902); 8 orbits; q = 161215/985608.
- B: k_0 = 132.842, e_0 = 0.43814 (certified, midpoint metric; e_0.02 = 0.7835, e_0.03 > 1); B2x 320 exact samples inside their radii;
  float N_0(|G_12|) = 132.94 ≤ certified 236.43; R = 2 control residual 6.74 vs 0.242.
- C: **𝔠_∞^♯ = 236.4346** (PROOF 2.0·10³⁷); **λ_min ≥ 4.2295·10⁻³** (γ_0 = 1.59·10⁻⁸, RW-ℓ² 6.6·10⁻¹⁰; measured 0.0398); rate 0.02 with
  N ≤ 716; C_bg = 1.640·10⁵; ε_br entries 1.82·10⁻²⁹/C_Δ, 7.45·10⁻⁷/C_♭, 1.76·10⁻⁴r_♭, r_♭/144, 4.76·10⁻⁹; (TH-ch″) at τ^A:
  ε_1 ≤ min{1.27·10⁻³⁹, 1.04·10⁻²⁹/C_Δ, 4.26·10⁻⁷/C_♭, …}; N5-sf0 with the certified gap: ε_* = 2.48·10⁻¹³/C_Δ (control 1.745·10⁻²⁴/C_Δ);
  CHEB-f μ = 5.37·10⁻⁴, N_μ(|Õ^{1/2}|) ≤ 5.7·10¹⁶; DX′-1 g_0²C_Ω ≲ 2.5·10⁻¹⁵² (τ^A; was 7.3·10⁻¹⁸⁰; control 1.49·10⁻²³⁷ reproduced).

## PROPOSED PROOF.md EDIT (for PROOF's owner; PROOF not edited by lane F)
1. After the 𝔠_∞ definition (l.5604-5606) add: "[proposed, SF §22.3 Proposition CI-bg (computer-assisted, check s7, criteria first):
   at κ_0 = 1, L = 3, d = 4, every N, for every (U, V) ∈ 𝔑(α_*), real or complex, on tori T ≥ T_0: N_0(|C(U, V)|) ≤ 𝔠_∞^♯ :=
   k′_0 + δ + k_0(e_0 + δk_0)/(1 - e_0 - δk_0) = 236.4346, with k_0 = 132.842054, k′_0 = k_0, e_0 = 0.4381436, δ = γ_0/2 (≥ C_Δα_*);
   it may replace 𝔠_∞ in BR1, NAH1 (level 0), CURV1 and HG1 (iv). For |κ_0 - 1| ≤ 2.6·10⁻² it stays finite (q = 161215/985608)]".
2. BR1's ε_br with 𝔠_∞^♯: ε_br = min{ε_*/(1 + 36p_L𝔠_∞^♯) = ε_*/93629.1, 1/(24𝔠_∞^♯²C_♭) = 7.45·10⁻⁷/C_♭, r_♭/(24𝔠_∞^♯) = 1.76·10⁻⁴r_♭,
   r_♭/144, 1/(1728𝔠_∞^♯K_FP) = 4.76·10⁻⁹}; 1 + 36p_L𝔠_∞ ≈ 9.36·10⁴ (l.5859/l.5911: "≈ 7.8·10³⁹" → "≈ 9.4·10⁴ with 𝔠_∞^♯"; the
   R20-fix 8 diagnosis is confirmed: the 10⁴⁰ was constants).
3. Proposition RW-ℓ² / N5-sf0 (b) gap line: add "[proposed: λ_min(Õ(U, V)) ≥ 4.2295·10⁻³ on real 𝔑(α_*) (SF CI-bg), and λ_min(Õ_0) ≥
   4.229507·10⁻³ (SF CI-0)]".
4. N5-sf0's evaluated threshold (l.5468-5473): with γ_0 → λ_min(Õ_0) ≥ 4.229507·10⁻³ as the compression bound (the only use of γ_0 in
   (b)'s proof), N5-w0's m_4 becomes 2.57·10⁻⁵, R_* = 3.23·10⁶, T_0 = 1.29·10⁷, ε_* = 2.48·10⁻¹³/C_Δ (s7 C4; control reproduces
   1.745·10⁻²⁴/C_Δ). This is an owner decision (it re-runs a PROVEN theorem's arithmetic).
5. CURV1's C_θ ∋ 288𝔠_∞³C_♭: with 𝔠_∞^♯ it is 3.81·10⁹C_♭ (was ≈ 2.3·10¹¹⁴C_♭) [arithmetic: 288·236.4346³ = 3.806·10⁹]; ε_θ's
   1/(80(48𝔠_∞ + 1)) = 1.10·10⁻⁶.
6. Named OPEN input: (C_♭-eval), explicit (r_♭, S_♭) for N5-an♭ (the soft term's continuation and the two inverses).

## Notes for other owners
- **RLARGE / HIST / HW:** under (TH-ch″) with 𝔠_∞^♯, ε_1 ≈ 1.27·10⁻³⁹ at τ^A modulo C_Δ, C_♭ (n_* ≈ 6·10⁷⁹ illustrative, ≈ 42 final
  levels), against 5.95·10⁻⁷⁷/C_♭ after TH-2 alone.
- **SF next session:** (GF-B^𝔥); (C_♭-eval) with PROOF's owner; a sharper CHEB-f (μ is the DX′ lever; the certified gap is 9.4×
  below the measured one, so a Collatz-Wielandt/ℓ² bound on Õ^{-1} would raise a and μ).

## Files written this session
SF.md ([RSF6-fix] edits in §16.1, §16.3, §18.2, §19.2-§19.4, §20.1-§20.2; §21-§23 appended), SF_LOG.md (this block),
checks/s7_criteria.md, checks/s7_sf.py, checks/s7_out.txt, checks/s7_time.txt. Scratch: sf7/ (oper.py, cert.py, ex1, ex2, run.sh, rows.pkl).
- 08:29: one-line arithmetic check (python, < 0.1 s, outside the lock) of the proposed-edit numbers 3.806·10⁹, 1.10·10⁻⁶, 93629.1.
