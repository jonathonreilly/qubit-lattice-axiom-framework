# HIST_LOG: lane D (H-pos, HIST) session log

## Session 19-D (2026-10-27, from 22:5x UTC)
- **Brief.** Lane D of the 4D YM proof push: (H-pos) (effective action at bad cubes) and (HIST) (multi-scale history
  bookkeeping). Write only HIST.md, HIST_LOG.md, checks/h*. No edits to PROOF.md, RTARGET.md, LOG.md, RLARGE.md, FLOW.md,
  agents/ym4d-existence/. No commits, PRs, pushes, CL or axiom edits. Numeric lock + nice 10 + BLAS threads 1 + load < 8
  + ≥ 25% free + peak < 1 GB for every numeric job.
- **Inputs read** (read-only, by offset): listed in HIST.md header.
- **23:08 UTC** HIST.md §0-§1 (pre-stated targets D1, D2; checks h1-h4) written before any derivation or criteria file.
- **23:08-23:19 UTC derivations** (HIST.md §2-§8): Lemma TD; Lemmas PM, KQ, RS-lin (linear threshold η_q); Proposition CL^J
  (joint stage-k frozen activities, no effective action at bad cubes); GT-lat'', Lemma 7.2-0^J, Theorem R1^J, Corollary
  R1_Λ; Theorem H-pos^J; Proposition CF (constant-curvature chain: route (R-a) ceiling); (CLS-NA) named; (D1-c) ARGUED false
  at tree level (c31 E2 ratios read from checks/c31E.out). §7: histories, Σ = N_1∘π shadows, Lemma H-nest, Lemma H-geo
  (via CE-geo'), Lemma RS-joint (c_RS = 81 ⇐ (PLD-q)), hypothesis (H-w), Theorem HIST-sum with n_H, (P1)-(P5) over K levels,
  Lemma P4-div, Theorem TS_K. §8: RLF-step^J proposal. Two in-text fixes before any check ran: CF's ribbon-area constant
  ((3/2)L(L-1), not 3L(L-1)) and a note that κ in (G1)^J is Theorem CE's decay parameter.
- **23:19 UTC** criteria h1-h4 written (checks/h*_criteria.md), then the scripts. Pre-run script edit disclosed: h1's SU(3)
  restart count was briefly reduced to 3 and restored to the criteria's 20 before any run; bisection depth 60 (criteria ask
  1e-12 radius accuracy; 4·2⁻⁶⁰ suffices).
- **Runs** (one job at a time under the machine-wide numeric lock; nice 10; OPENBLAS/OMP/MKL/vecLib threads 1;
  PYTHONDONTWRITEBYTECODE=1; no `timeout`; load ≤ 3.9, memory free 37-38%): h4 PASS (I1; table informational), h2 PASS
  (C1-C6, all three F; 0.8 s, 37 MB), h3 PASS (G1-G4, N1; 4.9 s, 42 MB; 63 random sets per L instead of the criteria's "60",
  plus 24 adversarial lines), h1: see below.
- **h1 PASS** (211 s, 35 MB; P1 ratios ≤ 1.012 vs 3, ≤ 1.072 vs 4; R exponent 12-16× conservative). Lock released after
  each batch. No criterion edited; no tolerance added.
- **23:3x UTC** HIST.md §9 (checks) inserted before §10; §10-§12 (outcomes, DAG, tally, hypotheses consumed) written after
  the derivations. Tally of this file: 6 PROVEN-HERE counted (unreviewed), 4 CONDITIONAL, 4 ARGUED, 3 OPEN walls.
  Nothing edited outside HIST.md, HIST_LOG.md, checks/h*. No commits, PRs, pushes.
- **Next (recommendation).** Hostile review of CL^J/R1^J (the substitution table) and of HIST-sum's (H-w) interface; then
  (CLS-NA) only if (D1-b) is wanted for its own sake (RLF-step does not need it).

## Session 2-D (2026-10-28, from 00:03 UTC)
- **Brief.** Session 2 of lane D: apply REVIEW_HIST_S1's twelve binding fixes (tag [RH1-fix]); Step 2 (pre-stated): the
  chain-energy form (I_k^E) of the representation on Λ_k, checked against FLOW's F-tree (read-only) and LINEAR_PACKAGE
  E-low; Step 3 (pre-stated): the small-field part of (CLS-NA). Write only HIST.md, HIST_LOG.md, checks/h*. Same numeric
  discipline as session 1. No commits, PRs, pushes, CL or axiom edits.
- **Inputs read** (read-only): REVIEW_HIST_S1.md (all), HIST.md and HIST_LOG.md (all), REVIEW_S18_S19.md l.1-140, FLOW.md
  §0, §3, §5.1-§5.4, §5.6, LINEAR_PACKAGE.md §1.2-§3 (to Theorem 3.8), PROOF.md NA-alg (l.2910-2950) and A1-NA / A1-NA(1) /
  A1-NA(k) (l.3953-4090), RLARGE.md §8.1-§8.2 (l.566-612).
- **00:03-00:07 UTC** STEP 1: fixes H-1..H-12 applied in place in §2-§12 (52 [RH1-fix] tags): the WRONG §2 sentence struck
  and replaced (G_k's U_{k+1}-dependence is global); (H-Mayer^J) restated as a whole-lattice Mayer expansion of small
  two-field activities; (D1-c) broadened to the ε_1-domain and (I_k^E) named; (P4) and RLF-step^J demoted to ARGUED with
  gaps H-1, H-3, H-4 named; (SF^J) named; RS-joint's in-history form ARGUED; TS_K restricted to Δ^{in}_{*,n} and moved to the
  uncounted corollaries; Den^J_B > 0 via U_{k+1} ≡ 1; F1's Lipschitz line; R1/TS cited as CONFIRMED-WITH-FIX (stale
  "unreviewed" label dropped); R1_Λ recorded as G5's R1-loc with its in-sea collar cost; CF's scope; RS-lin's linearity only
  for ε_1 ≤ 0.4; (H-pos) relocated not removed; downward footprint defined; collar-bad sentence; (H-w)(c) fragility;
  tally 5/2/6/3; "nothing new in kind" replaced by (SF^J), (I_k^E).
- **00:07 UTC** HIST.md §13 (session-2 pre-stated targets S2, S3 and check h5) written after reading and exploratory
  reasoning, before any session-2 derivation, criteria file or script.
- **00:08:33 UTC** checks/h5_criteria.md written; then the script checks/h5_cone_and_dM.py.
- **00:10-00:25 UTC** HIST.md §14 (Step 2: tower identity, (I_k^E) stated, Lemma HF, consistency items c1-c5) and §15 (Step 3:
  cones, Lemma E-loc, hypothesis (AE), Theorem CLS-red, §15.5) written; the h5 run waited for the lock meanwhile.
- **h5 run** (lock taken 00:21:39 UTC; 1.7 s, 148 MB, load 3.25, 39% free): OVERALL FAIL as pre-registered — B3 (median
  y-slope of d = 5.37, outside [5.5, 6.5]; smallest y at the rounding floor). A1, A2, A3, B1, B2, B4 PASS. No criterion edited.
- **Post-hoc diagnostic h5b** (written after the FAIL, labelled; lock 00:32:03 UTC, 0.1 s): |arg det M| ∝ y^3.000, d ∝ y^6.00
  away from the rounding floor. Recorded in HIST §16; the B3 FAIL stands.
- In-text fixes before finishing (no check affected): the A' constant in CLS-red set to 2A_d (RS (R1) ribbons); the
  NA-alg G-bound cited in operator norm; B5's above-1 outliers labelled as numerical [inference].
- **Outcome.** S2 MET ((I_k^E) stated; F-tree/E-low consistent; FLOW §3.1's "log 𝒩' carries no power of u" is off by
  -κu·d(M) for N ≥ 3, sextic and β-neutral, reported). S3: CLS-sf NOT proven; PROVEN reduction CLS-red: (AE) ⇒ (CLS-NA) for
  all fields, uniformly in depth; (AE)'s linear case = Lemma E-loc (PROVEN); wall = the gauge on the cone ((MSG), (MS-Sob),
  inference). Tally: §0-§12 5/2/6/3 after fixes; session 2 adds 2 PROVEN-HERE (HF, E-loc), 1 CONDITIONAL (CLS-red),
  1 HYPOTHESIS ((I_k^E)), 1 OPEN ((AE)); (CLS-NA) OPEN → CONDITIONAL ⇐ (AE).
- Nothing edited outside HIST.md, HIST_LOG.md, checks/h5*. No commits, PRs, pushes.
- **Next (recommendation).** Hostile review of Lemma E-loc, Lemma HF and Theorem CLS-red (especially the nesting/overlap of
  cones and step β); then (AE) via an interpolation gauge (MSG) — reading Balaban's small-field gauge fixing first.

## Session 3-D (2026-10-28, from 00:46 UTC)
- **Brief.** Session 3 of lane D: apply every REVIEW_HIST_S2 fix (tag [RH2-fix]); Step 2 (pre-stated): the multi-scale
  small-field gauge theorem (MSG), the depth-2 SU(2) non-abelian cone-ratio check, then (AE), CLS-red and (I_k^E) re-derived
  on top of MSG. Lead's mid-session note: state CLS-sf in the cone-local (per-cone, per-defect) form with RLARGE's η_1.
  Write only HIST.md, HIST_LOG.md, checks/h*. Same numeric discipline. No commits, PRs, pushes, CL or axiom edits.
- **Inputs read** (read-only): REVIEW_HIST_S2.md (all), HIST.md §13-§18 (l.785-1106) and the lines named by N-1..N-3,
  HIST_LOG.md (all), LINEAR_PACKAGE.md §1.2 (S4', Q_root), RLARGE.md l.257-361 (A_d, η_1, (R1)-(R5)), checks/c18c_a1na_inregime.py
  (S4' contour code, reused in spirit). Backup of HIST.md before edits in the scratchpad (HIST_pre_s3.md).
- **00:50-01:00 UTC** STEP 1: REVIEW_HIST_S2 fixes 1-12 applied in place ([RH2-fix] tags; GAP S2-1..S2-3 marked in §14.1;
  the repair itself is in §20.3). Fix 13 (h5 disclosures): (i) criteria A4 compared with 12·C_loc = 480 while the proof's
  overlap is 24 (960); A4 is informational and measured 1.99; (ii) the criteria said W_0 is found by fixed-point iteration
  "followed by Newton/BFGS polishing"; the script did the fixed-point iteration only (residual ≤ 1e-15). Both harmless,
  disclosed here.
- **01:00:57 UTC** HIST.md §19 (session-3 pre-stated targets S4, S5 and check h6) appended, before any session-3 derivation,
  criteria file or script.
- **01:01:44 UTC (EDT 21:01:44)** checks/h6_criteria.md written (stat mtime "2026-10-27 21:01:44 EDT"); the script
  checks/h6_msg_cone.py did not exist at that time.
- **01:02-01:10 UTC** checks/h6_msg_cone.py written (after the criteria). Pre-run fixes (disclosed): directions with no cone
  links at level k skipped; safe max on empty arrays. One smoke run of a REDUCED scratch copy (3 samples, 3 t, d = 2 depths
  ≤ 2) at 01:13:01 UTC under the lock (27 s, 615 MB), after one crashing attempt at 01:10:21 (0.8 s); no criterion edited.
- **h6 official run** (lock 01:13:48-01:16:21 UTC; 153 s, 729 MB peak, load 3.6, 39% free, nice 10, BLAS threads 1): OVERALL
  FAIL as pre-registered: A2, A3 (smooth seed 2, near-cancelling top flux, R_lin = 6.6e-4). A1, B1-B3, C1-C3 PASS (max R_NA
  16.0005 vs linear 16; MSG constant 3.53 at d = 4 depth 2; d = 2 depths 1-5: 8.03 → 8.66 flat, axial 1.4 → 10.2).
- **h6b POST HOC** (written after the FAIL, labelled; lock 01:16:56-01:17:13 UTC, 17 s, 642 MB): additive error
  |log U_2(P) - dB_2(P)|/√E ∝ t^{1.00-1.02} on the three smooth seeds; the relative-criterion failure is a near-cancellation
  artefact. The A2/A3 FAIL stands.
- **01:17-01:25 UTC** HIST.md §20 (MSG theorem + MSG-loc; Lemma MS-HLS; (MS-Sob) ⇐ (SQ); (AE) ⇐ MSG + MS-Sob ARGUED; the
  k-fold counterexample to curvature-source (SQ); Corollary CLS-cone with RLARGE's η_1; (I_k^E)' with (a'), (b'), (d')),
  §21 (h6), §22 (outcomes), §23 (tally) written. Literature: Balaban CMP 109 §1 p.260-261 (text l.486-530) [read-skim];
  NOTES.md §9.3-9.4 [read]; Uhlenbeck CMP 83 [not-read; no open exposition consulted].
- **Outcome.** S4 MET (MSG PROVEN-HERE, depth-uniform, C_M = 66.1 at d = 4, L = 3). S5 MET in reduction form: (AE) OPEN,
  reduced to (SQ); (I_k^E)' GAPs repaired at the statement level (new items (a3), (a4)); CLS-cone CONDITIONAL ⇐ (AE).
  Tally of the file: 9 PROVEN-HERE / 5 CONDITIONAL / 7 ARGUED / 4 OPEN + 1 HYPOTHESIS (session-3 items unreviewed).
  **[RH3-fix S3-4] Corrected by REVIEW_HIST_S3: 9 / 4 / 8 / 4 + 1 HYPOTHESIS** (MS-Sob ⇐ (SQ) re-labelled ARGUED via
  MSG-loc-dev + MS-HLS + SQ-dev; MSG-loc GAP, MSG-loc' proven).
- Numeric lock taken and released by single rmdir each time (4 holds). Nothing edited outside HIST.md, HIST_LOG.md,
  checks/h6*. No commits, PRs, pushes, CL or axiom edits.
- **Next (recommendation).** Hostile review of Theorem MSG (steps (3)-(6), the inter-block ladder count A_d, the chain-gauge
  structure F6) and of Lemma MS-HLS; then (SQ) in its deviation form, starting with its linear case (a Littlewood-Paley
  estimate for (Q_2, I_2) on the LINEAR_PACKAGE symbol side).

## Session 4-D (2026-10-28, from 01:45 UTC)
- **Brief.** Session 4 of lane D: apply every REVIEW_HIST_S3 fix (tag [RH3-fix]); STEP 2 (pre-stated first): repair the
  (I_k^E)' holes: (a5) an analytic main term in place of the real infimum (critical value via the implicit function theorem,
  NA-IFT / N5-an, MSG's gauge; agreement with the infimum on real small fields) and the complex domain (sl(N, ℂ) chart form);
  restate (I_k^E)'' and check it against Lemma HF, FLOW F-tree and RLARGE v2 (RLF-5). STEP 3: (AE) ⇐ MSG + (MS-Sob) from
  ARGUED to PROVEN conditional on (MS-Sob), written fully. Write only HIST.md, HIST_LOG.md, checks/h*. Lane G owns (SQ) and
  whether (AE) is needed; lane F owns the small-field package: not duplicated. Same numeric discipline. No commits, PRs,
  pushes, CL or axiom edits.
- **Inputs read** (read-only): REVIEW_HIST_S3.md (all), HIST.md §14-§15, §17-§23, HIST_LOG.md (all), RLARGE.md v2 §1.2,
  §2-§5 and K7 (l.165-195, 227-490, 575-595), PROOF.md NA-alg (l.2948-2985), NA-IFT and B-NA-red (l.3117-3160), N5 setting
  and Lemma N5-an (l.5200-5215, 5252-5268), FLOW.md §4 (SF-bg) (l.185-192), PLD.md (RLF-5) width (l.497-503),
  literature/balaban_cmp109_text.txt l.574-592. Backup of HIST.md before edits: scratchpad hist_s4/HIST_pre_s4.md.
- **01:49-01:52 UTC** STEP 1: REVIEW_HIST_S3 fixes applied in place ([RH3-fix] tags): N-4 (CLS-red display and η_E's
  dependence; η_E ≤ η_AE), S3-1 (axial order with P's plane first, else A_ax = 12; C_M = 66.1 unchanged), S3-2 (MSG-loc GAP;
  MSG-loc' with c_qα_cell² stated, the d = 4-marginal per-level source), S3-3 (MS-HLS: d = 4; 5^d, L^d into C_Q), S3-4
  (MS-Sob re-labelled ARGUED via MSG-loc-dev + MS-HLS + SQ-dev; curvature-source implication a vacuous remark; tally
  9/4/8/4 + 1 in §22, §23 and above), S3-5 (CLS-cone (c1) 1/24, (c2) 1/576, (c3) disjoint footprints else k-fold; C_cone ≳
  10¹² and the g² requirement), S3-6/S3-7 marked at (a')/(b') (repairs in §25), (d') c-number note, literature pointer 9
  (CMP 109 (1.14)-(1.16), read this session).
- **01:52 UTC** HIST.md §24 (session-4 pre-stated targets S6, S7 and check h7) appended, before any session-4 derivation,
  criteria file or script.
- **checks/h7_criteria.md written** (stat mtime "2026-10-27 21:57:46 EDT"); the script checks/h7_term_an.py did not exist at that time.
- **01:58-02:07 UTC** HIST.md §25 (STEP 2: Lemmas TERM-an, POL, EXT, NORM-an, (R♯_∞); item (a5) = (a5-G) + (a5-U) and (a3-q);
  Theorem A5 CONDITIONAL; (I_k^E)'' restated; consistency (c1''), (c2''), (c3''), (c5'')) and §26 (STEP 3: Theorem AE-red,
  (AE) ⇐ MSG + (MS-Sob), proof written in full with constants C_e, K_R, C_2 and smallness conditions (Z1)-(Z5)) written. Three
  in-text corrections before any check ran: n_T's count, the IFT uniqueness ball ρ_1 (s_5 re-defined), and op/HS bookkeeping
  of m_i in §26 step (2), (4).
- **02:07-02:08 UTC** checks/h7_term_an.py written after the criteria (stat mtime "2026-10-27 22:08:39 EDT" = 02:08:39 UTC; criteria 21:57:46 EDT).
- **h7 official run** (only run; waited ~40 min for another holder; lock 02:50:02-02:50:04 UTC, single rmdir; 2.3 s, 155 MB,
  load 2.39, 45% free): OVERALL FAIL as pre-registered — A3 (the non-holomorphic control gave CR defects ≤ 4·10⁻³, not ≥ 0.1;
  the holomorphic cases passed at ≤ 5·10⁻⁹ / 4.3·10⁻⁴). A1, A2, A4, B1, B2, C1, C2 PASS; A5 soft within limits. No criterion or
  script edited after the run. Constants (C): η_AE ≈ 1.8·10⁻¹⁵ (N = 2), C_cone ≈ 10¹⁵.
- **02:50-02:51 UTC** HIST.md §27 (h7), §28 (outcomes), §29 (tally) written after the run.
- **Outcome.** S6 MET in reduction form (Theorem A5 CONDITIONAL ⇐ (a5-G), (a5-U), (a3-q), (MS-Sob); TERM-an, NORM-an PROVEN);
  S7 MET (Theorem AE-red, (AE) CONDITIONAL ⇐ (MS-Sob)). Tally 11 / 6 / 7 / 4 + 1 (session-4 items unreviewed).
- **Next (recommendation).** Hostile review of TERM-an, NORM-an and Theorem AE-red (constants, the op/HS bookkeeping, the
  induction); the lead to route (a5-G) to lane F and the RLF-5 width item (c3'') to RLARGE; (a5-U), (a3-q) are lane D's next
  classical targets.
