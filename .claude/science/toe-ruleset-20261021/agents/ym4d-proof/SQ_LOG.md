# SQ_LOG (lane G: the square-function estimate and the sup-route price)

## Session 1 (2026-10-28 UTC)
- **01:40-01:57 UTC** Read (read-only): HIST.md §0, §15, §20-§23; HIST_LOG tail; checks/h6_criteria.md; LINEAR_PACKAGE.md
  §1-§3; PROOF.md l.2948-2962 (NA-alg statements); RLARGE.md §3.2-§3.4; REVIEW_HIST_S3.md l.150-175, 250-320, 430-486
  (after the coordinator's lead's note arrived mid-reading); FLOW.md grep of (SF-bg). Exploratory reasoning (not
  written down before §T).
- **01:57:58 UTC** (stat mtime 21:57:58 EDT) SQ.md created with header and §T (pre-stated targets G0-G3, checks q1, q2),
  before any derivation or check file.
- **02:00:56 / 02:01:15 UTC** checks/q1_criteria.md, checks/q2_criteria.md written (stat mtimes 22:00:56, 22:01:15 EDT).
  One edit to q2_criteria C3 at ≈ 02:01 UTC, before any script existed (a garbled sentence about a d = 2 E-loc constant
  replaced by the plain criterion "e(k) > 0 and e(5) ≥ 0.5·e(3)"; disclosed here).
- **02:02-02:07 UTC** SQ.md §0 (verdict; Lemmas INF, MSG-dec, E2, BCH-p, FORCE, DESC; Theorem SUP-price; hypothesis
  (REG-min); Corollary PRICE-iii; §0.4 Q_str/Q_root), §2 (restatement), §3 (1D Bessel lemmas), §4 (SQ-lin), §5 (linear
  MSG-loc-dev and linear MS-Sob), §6 (non-abelian status), §7 (proposal for HIST's owner) written.
- **02:07-02:08 UTC** checks/q1_sq_lin.py written (after its criteria), then one edit (families made a lazy generator, for
  memory at k = 3) before any run.
- **02:08 UTC** smoke run of a REDUCED scratch copy of q1 (scratchpad q1smoke/: L = 3 depths ≤ 6, L = 5 ≤ 3, 4D k = 2 only)
  queued on the numeric lock (lock held by another lane's f6_iter_chain.py at the time).
- **02:09 UTC** checks/q2_decay_min.py written (after its criteria).
- **02:21 UTC** SQ.md edits before any run: §0.2 sentence "attained by a circulating field" withdrawn (not proven); §4.3
  constants restated as 34203 / 11401. q1's criteria quote 34200 / 11400 (0.01% stricter than proven); disclosed.
- **02:50:22-02:50:23 UTC** q1 smoke (reduced copy) under the lock, after waiting ≈ 40 min for another lane's lock hold.
  It printed all its measurements, then hit a KeyError in the summary (the reduced copy lacks k = 3). The smoke already showed
  the box family rising slowly with depth.
- **03:34:36 UTC** q2 smoke (reduced copy) under the lock: measurements printed, then a KeyError in the summary (reduced
  depths). No criterion edited after either smoke.
- **03:34:59-03:36:48 UTC** one lock hold: q1 run 1 crashed (ARPACK non-convergence, triangle family, large J;
  checks/q1_out_firstrun_crash.txt); q2 official run (7.8 s, 223 MB): OVERALL FAIL (C3 d = 2 half: the d = 2 energy scales like
  L^{-2k}); C1, C2, C4 PASS; C_D(d = 2) = 1.06 → 2.25 flat; d = 4 e = 0.111, 0.105.
- **03:45 UTC** q1 crash fix (dense eigvalsh for sizes ≤ 2500; ARPACK ncv = 96 above); no criterion change.
- **03:45-03:51:52 UTC** q1 run 2 under the lock (378 s; max RSS 782 MB; macOS peak memory footprint 1052 MB, ABOVE the 1 GB
  cap; resource-rule breach disclosed). OVERALL FAIL (A2: the box family is still rising at J = 9, λ = 9.29 against 8.52 at
  J = 6, ≤ the proven 14.93); A1, B1, B2, B3 PASS (R_D ≈ 1; adversarial 1.17 / 1.65; smooth R_F 1.00 → 1.93 against R_D
  0.24 → 0.28).
- **03:52 UTC** SQ.md §8-§10 (checks, outcomes, tally) written.
- Numeric lock: taken and released by a single rmdir each time (four holds: two smokes, the q1-run-1 + q2 hold, and q1 run 2).
  Nothing edited outside SQ.md, SQ_LOG.md, checks/q*. No commits, PRs, pushes, CL or axiom edits.
- **Outcome.** G0 settled: (SQ) is off the critical path for branch (iii). The price is CONDITIONAL ⇐ (REG-min) (weighted-sup
  regularity of τ-small cone-local minimisers, OPEN; linear case supported by q2). Linear (SQ) PROVEN for the D_j part, with
  explicit crude constants; non-abelian (SQ) OPEN and off-path.
- **Next (recommendation).** Hostile review of §0.3 (MSG-dec's level-dependent use of MSG steps (3)-(7); SUP-price step
  (5); DESC's height ordering and the KQ case). Then (REG-min): first its linear cone-local weighted-sup estimate (the
  free-boundary analogue of LINEAR_PACKAGE Theorem 3.8), then the product rule and the absorption.

## Session 2 (2026-10-28 UTC)
- **04:14-04:25 UTC** Read (read-only): REVIEW_SQ_S1.md (all; binding), SQ.md, SQ_LOG.md, RTARGET.md §33 (l.572-667) and
  §48-49, PROOF.md BNA-F1/F2/F3 (l.3200-3225), Lemmas REC, KF, Theorem G♯_0-soft, LES-div, (G♯_0-fine) (l.3340-3445), the [S22]
  composite-route block (TOWER-VAR, COMP, (CL-cl); l.6294-6370), LINEAR_PACKAGE.md §1, §3, §4 (l.49-260), HIST.md l.1404-1416,
  l.1672-1702, l.1784-1800 (A5, AE-red), SF.md l.94-99, 826-840; checks/q2_*. REVIEW_S22.md does not exist (checked 04:15,
  04:24 UTC). Exploratory reasoning on paper (reflection argument for the free-boundary cone box; a shift identity for
  residual sources), not written down.
- **04:24 UTC** SQ.md §T2 (session-2 pre-stated targets: Step 1, Q3, G4, G5) written before any session-2 derivation, before
  checks/q3_criteria.md and before any q3 script.
- **04:26:02 UTC** checks/q3_criteria.md written (stat mtime 00:26:02 EDT), before any q3 script.
- **04:27:01 UTC** checks/q3_src_decay.py written (stat mtime 00:27:01 EDT), after its criteria. A REDUCED scratch copy
  (scratchpad q3smoke/q3_smoke.py: d = 2 k ≤ 3, d = 3 k ≤ 2, summary removed) made for a smoke run.
- **04:27 UTC** load 11.1 (1 min), 38% free, the numeric lock held by another lane: a lock-guarded runner (scratchpad
  q3smoke/run_q3.sh: mkdir lock, wait for 1-min load < 8, smoke, then the full q3 only if the smoke exits cleanly, one rmdir)
  started in the background.
- **04:29:56-04:31:03 UTC** one lock hold (mkdir 04:29:56, rmdir 04:31:03; load 5.4 at start, 40% free, nice 10, threads 1):
  smoke of the reduced copy (1 s, clean exit), then the official q3 (66.4 s, max RSS 217 MB, peak footprint 203 MB).
  **OVERALL: FAIL as pre-registered (QA, QC); Q1, QB PASS.** QA: d = 2 flat (N_0 = 4.26, 7.49, 8.73, 8.96, 8.99, k = 1-5) but
  d = 3 grows (N_0 = 2.19, 4.01, 6.26). QB: R_ctr = 0.90, 1.75, 2.67 (grows). QC: N_0 = 0.173, 0.203, 0.276 (grows; R_ctr flat
  0.113, 0.091, 0.100). A1 (single-level sources): every source below the top gives fine response 0.0000 and N = 4.0000 (the
  source's own circulation) at every d, k; the A response equals the top-source (= top-data) response exactly. No
  criterion edited after the run.
- **04:38:20 / 04:38:32 UTC** checks/q3b_criteria.md, then checks/q3b_d4_plaq.py (stat mtimes 00:38:20, 00:38:32 EDT): a
  follow-up written AFTER q3's run (disclosed in its criteria: q3's d = 3 cannot separate a depth log from d = 3 scaling);
  d = 4, k = 1, 2 only (a weak two-depth test). Queued on the lock in the background (no smoke: it reuses q3's Chain class
  verbatim, which ran cleanly).
- **04:38:46 UTC** q3b under one lock hold (mkdir and rmdir 04:38:46; load 2.3, 56% free; 0.56 s, peak footprint 87 MB).
  **OVERALL: PASS (R1, RB, RC)**: B4 R_ctr = 0.995 → 2.014 (k = 1 → 2, grows); C4 N_0 = 0.113 → 0.079 (flat). Two depths only.
- **04:28-04:37 UTC** Step 1: REVIEW_SQ_S1's binding fixes applied in SQ.md, tagged [RSQ1-fix] (S1-1, S1-1a, S1-2 with
  Corollary DESC-ε written fully and §0.5 completed, S1-3, S1-4, S1-5, S1-6, §7, M-1 … M-7, the "L^{-1/2}" reading dropped,
  session-1 tally 6 / 2 / 2). Original text kept; corrections follow it. One forward pointer in the (REG-min) fix ("only at
  level 0 … §11.3, q3") was written before §11 existed and was checked against q3/q3b and §11 afterwards (it stands; §11.4,
  §11.5).
- **04:39 UTC** REVIEW_S22.md found (stat mtime 00:36 EDT); read l.330-437 (COMP-F1, (CL-cl), Part 5: BFT) and its fix list
  for SQ (l.498-499: note (REG-min) as the cone-local sibling of BFT-1). Aligned in §0.3's (REG-min) fix and §11.6.
- **04:41-04:45 UTC** SQ.md §11 (Lemmas TOP, REFL, SHIFT; Theorems REG-lin, REG-lin-src; q3/q3b record and reading; §11.6
  the non-abelian needs (NA-0)-(NA-5) and the BFT dependence, ARGUED) and §12 (outcomes, tally) written. During the write-up
  a boundary-compatibility hypothesis was found missing from REG-lin-src (b), (c) (odd reflected components jump at the
  faces) and added before §12; the q3 (C)/(C4) sources do not satisfy it (disclosed in §11.5).
- Numeric lock: three holds this session (q3 smoke + q3 at 04:29:56-04:31:03; q3b at 04:38:46), each one mkdir and one
  rmdir; no process left running. Nothing edited outside SQ.md, SQ_LOG.md, checks/q*. No commits, PRs, pushes, CL or axiom
  edits.
- **Outcome.** Linear (REG-min) PROVEN depth-uniformly (pure data, sup norm, θ_w = 2) by reflection + LES-sup; residual
  sources at every level cost nothing (SHIFT; q3 A1 exact zeros); level-0 curl-ful sources need Hölder/Lipschitz control (q3 B,
  q3b B4 grow). Non-abelian (REG-min) ⇐ (BFT-cone) + (MIN-reg)_cone [ARGUED]; the large-branch exclusion is the critical step,
  relocated, not removed.
- **Next (recommendation).** Hostile review of REFL (the reflection of Q at the coarse planes; the crossing-link
  conventions) and of REG-lin (c) (the copy count; LES-sup's box convention), then write (NA-2) as a lemma (covariant
  Bianchi and Euler-Lagrange defect bounds in the MSG gauge), which would test COMP-F1's reading directly.

## Session 3 (2026-10-28 UTC)
- **10:00-10:13 UTC** Read (read-only): REVIEW_SQ_S2.md (all; binding), SQ_LOG.md, SQ.md (all), REVIEW_RLARGE_V3.md l.55-80,
  300-320, 355-400 (K13, Part 6 top 3), BFT_B.md §15.0, §18.0-§18.3, §19.9-§19.13 (NF-uniq, NF-cov, REF/(N1-bd), NF-ex, KΠ),
  LINEAR_PACKAGE.md §1.2-§1.3 and Lemma 3.1 (J-str), HIST.md l.140-175 (PM step 3, Lemma KQ: φ's form). Exploratory reasoning
  (not written down).
- **10:13:26 UTC** (stat mtime 06:13:26 EDT, SQ.md 98422 bytes) SQ.md §T3 (session-3 pre-stated targets: Step 1, Target G6
  with CC-NA, RT-NA, RES-dec, STOKES-NA, RED-0, route verdicts, check q4, failure modes G6-F1…F4) appended: the first edit of
  session 3, before any [RSQ2-fix] edit, proof, criteria file or script.
- **10:13-10:16 UTC** Step 1: REVIEW_SQ_S2's binding fixes applied in SQ.md, tagged [RSQ2-fix] (S2-1a/b in §0.3; M2-1 in DESC-ε;
  S2-2 (λ_0 renamed, compatibility dropped for (b)), S2-3, M2-4 in §11.0/§11.4; S2-4a-d, M2-2 in §11.5; M2-3 in §11.3; S2-3
  (𝔑's residual weight), S2-5, S2-6, M2-5, M2-6 in §11.6; S2-3/S2-4d/S2-6 pointers in §12). S2-5 was checked on a limited
  reading of PROOF l.5443-5460 (N5-sf0's boxes are local charts inside a torus; no free-boundary statement found; disclosed
  as not a full check). Original text kept.
- **10:16:34 UTC** checks/q4_criteria.md written (stat 06:16:34 EDT, 2073 bytes), before any q4 script.
- **10:17:12 UTC** checks/q4_kernel_ids.py written after its criteria (one pre-run edit at 10:17: the SU(3) instance count
  raised from 5 to 20 to match the criteria).
- **10:17:46-10:17:57 UTC** q4 under one lock hold (mkdir 10:17:46, rmdir 10:17:57; load 5.66, 36% free; nice 10, threads 1;
  10.6 s, peak footprint 57 MB). **OVERALL: FAIL as pre-registered (K3: 1.89·10⁻⁸ > 1e-8); K1, K2, K4, K5, K6 PASS.** No
  criterion edited after the run.
- **10:23:04-10:23:14 UTC** post-hoc diagnostic (scratchpad q4run/q4_diag.py, a copy of q4 that also prints K3 per N; one lock
  hold): K3's excess is SU(3)-only (1.2-1.9·10⁻⁸; W_0 by BFGS), SU(2) ≤ 1.7·10⁻¹⁰, formula side exactly 0. Labelled post hoc.
  **[RSQ3-fix S3-8, added session 4]** Corrected reading: the excess is the first-order error of the BFGS W_0 (3·10⁻⁸),
  violating q4's ≤ 1e-13 precondition, not finite-difference noise; "formula side exactly 0" is tautological and withdrawn.
- **10:18-10:25:21 UTC** SQ.md §13 (Lemma K, CC-NA, RT-NA + RES-dec, STOKES-NA + STOKES-it, Theorem RED-0, §13.6 route (b) and
  the coupling, §13.7 route (a), §13.8 BFT-1 clause request) and §14 (outcomes, tally) appended after q4 ran.
- **10:25-10:27 UTC** same-session corrections inside §13 before this log entry (no reviewer had seen it): RES-dec's constants
  (C_q = 665 not 599, the e-term carries √N not N; τ_* = 5.6·10⁻⁵; C_r := 1.9Nκ̂^{3/2}, the κ-ratio restored; "critical point"
  → "minimiser" in the statement, since step (1) uses minimality); STOKES-it's proof rewritten as a clean induction with
  explicit θ_S; STOKES-NA's smallness now also m ≤ 1/C_e (needed for |e| ≤ m + 1.011x), C_S ≈ 3.8·10⁶; RED-0's τ_R made explicit.
- Numeric lock: two holds this session (q4; the diagnostic), each one mkdir and one rmdir; no process left running. Nothing
  edited outside SQ.md, SQ_LOG.md, checks/q*. No commits, PRs, pushes, CL or axiom edits.
- **Outcome.** (REG-min) ⟺ (EPS-0) (Theorem RED-0): the residual half of (REG-min) is PROVEN with no bootstrap (RES-dec,
  exponent θ_r > 2 from τ-smallness alone, via exact co-closedness CC-NA and the S4' funnel cancellation), and levels ≥ 1 follow
  from level 0 with no level sum (STOKES-NA). The wall is (EPS-0), the sup decay of the level-0 curvature of small cone
  minimisers; it stays coupled to all levels through the non-abelian funnel rotation of the residual currents (G6-F4
  occurs), so the large branch survives, localised as level-0 concentration. Route (a) gives the canonical sup Coulomb gauge,
  not minimiser uniqueness.
- **Next (recommendation).** Hostile review of §13.2-§13.5 (CC-NA's top step (iii) and the composite-gauge rule; RT-NA's
  prefix conventions and the funnel cancellation's in-link frame H_TQ_b; the weight counts L⁻³ and ω ≤ 1; STOKES-NA's use of
  HIST MSG step (1) on R_q). Then (EPS-0): a lattice ε-regularity theorem at level 0 that tolerates the funnel feedback,
  starting from (b1) (the Bianchi-defect divergence term).

## Session 4 (2026-10-28 UTC)
- **10:55-11:14 UTC** Read (read-only): REVIEW_SQ_S3.md (all; binding), SQ_LOG.md, SQ.md l.953-1217 (§T3, §13, §14),
  BFT_B.md §15-§16 (l.2014-2263: S_E, EP-int, EP-bd, EP-opt), §18.0 and §19.8-§19.13 (l.2453-2532, 2669-2750: NF-crit,
  NF-uniq, NF-cov, REF/(N1-bd), NF-ex, KΠ), the §21-§23 headings (KΠ-off, N2), HIST.md §20.2 (MSG, l.1213-1272). Exploratory
  reasoning (not written down).
- **11:14:39 UTC** (stat mtime 07:14:39 EDT; SQ.md 130554 bytes before, 138407 bytes after) SQ.md §T4 (session-4 pre-stated
  targets: Step 1, STEP 2 (NREFL, BIA, WB, SOB, EPS-T, EPS-0a), STEP 3 route (α) (GS, LU-ap, GAP, LU-ex, verdict) and route
  (β) (TPL, STOKES-avg, LEV-E, LOC-T, CARL, GARSIA, EPS-0b-avg), Theorem EPS-0 and corollaries, checks q4b and q5, failure
  modes S4-F1…F5) appended: the first edit of session 4, before any [RSQ3-fix] edit, proof, criteria file or script.
- **11:15-11:17 UTC** Step 1: REVIEW_SQ_S3's binding fixes applied in SQ.md, tagged [RSQ3-fix] (M3-2 in §11.5; S3-1 in §11.6;
  M3-1, M3-3, M3-4, M3-5, M3-6 in §13.0-§13.3; M3-7 and S3-2 in §13.4; S3-3, S3-6 in §13.5; S3-4, S3-5, S3-6 in §13.6; S3-7, M3-8
  in §13.7; S3-6/S3-1 in §13.8; S3-8, S3-3/S3-5 in §14) and S3-8 in this log's session-3 entry. Original text kept. M3-7's note
  was corrected at ≈ 11:17 after reading §0.3 l.167 (y_c's definition), before any later edit.
- **11:17:10 UTC** checks/q4b_criteria.md (stat 07:17:10 EDT, 1285 bytes), labelled POST HOC to q4, before any q4b script.
- **11:17:26 UTC** checks/q4b_newton.py (q4 verbatim except W0 by Newton and the P0 / BFGS-difference report).
- **11:25:21 UTC** checks/q5_criteria.md (stat 07:25:21 EDT, 3447 bytes), before any q5 script.
- **11:2x-11:29:07 UTC** checks/q5_lattice_ids.py written after its criteria; two pre-run edits (11:29): a redundant line in T1
  removed; the random-field scale multiplied by √2 so that |X_b|_op = uniform(0.3, 1) as the criteria state. No criterion edit.
- **11:29:41-11:29:50 UTC** q4b and q5 under one lock hold (mkdir 11:29:41, rmdir 11:29:50; load 3.46, 38% free; nice 10, threads
  1). **q4b: OVERALL FAIL as pre-registered (P0: 4.3·10⁻¹⁰ > 1e-13); K3 2.07·10⁻¹⁰ PASS, K1, K2, K4-K6 PASS** (3.0 s, 57 MB).
  **q5: OVERALL FAIL as pre-registered (T2: 0.80); T1, W1, W2, W3, B1, R1, G1 PASS** (5.6 s, 211 MB). No criterion edited after
  the runs.
- **11:30:42 / 11:31:13 UTC** post-hoc diagnostics (scratchpad s4diag/diag.py, diag2.py; one lock hold each): T2b with SQ §2's
  Q_str (average over all L⁴ starting points) gives 2.8·10⁻¹⁶ (the script's face-start Q_str was the wrong operator); q4b's P0
  residual is the SU(2) polar factor at complex-perturbed M (2.6·10⁻¹⁰), Newton SU(3) ≤ 1.2·10⁻¹⁷. Labelled post hoc.
- **11:32-11:40:36 UTC** SQ.md §15 (15.0 conventions; 15.1 NREFL, BIA, WB, SOB, Theorem EPS-T, Corollary EPS-0a; 15.2 TPL,
  STOKES-avg, LEV-E, LOC-T, CARL, GARSIA, Proposition EPS-0b-avg; 15.3 Theorem EPS-0 and corollaries; 15.4 GS, LU-ap, GAP,
  LU-ex, route (α) verdict; 15.5 check record) and §16 (outcomes, tally) appended after the checks ran. Same-session
  corrections before this entry (no reviewer had seen them): EPS-T's scale-invariant source hypothesis added (post-proof
  correction (6)); SOB's constant C_S = 3 made explicit; the Moser step formula written out; GAP's last inequality and LU-ex's
  constant C_U restated; the HS/op factor √N in Theorem EPS-0's constants.
- Numeric lock: three holds this session, each one mkdir and one rmdir; no process left running. Nothing edited outside
  SQ.md, SQ_LOG.md, checks/q*. No commits, PRs, pushes, CL or axiom edits.
- **Outcome.** (EPS-0) PROVEN as an implication (Theorem EPS-0), hence (REG-min) (RED-0) and its consumers (PRICE-iii, DESC-ε,
  (CLS-min)), all pending review. The mechanism: EPS-T (lattice ε-regularity with an ℓ^q source, via nonlinear reflection,
  Bianchi/Weitzenböck errors as critical potentials, and a finite lattice Moser iteration) plus EPS-0b-avg (the multi-level
  funnel product is the exponential of a Carleson sum controlled by the energy, integrable by Garsia's lemma though not
  bounded). The pointwise (EPS-0b) follows afterwards. Route (α): the lattice Uhlenbeck gauge (LU-ex) is PROVEN; multi-level
  slice convexity (CVX-K) is OPEN and not needed.
- **Next (recommendation).** Hostile review of EPS-T (steps (3)-(6)), LOC-T (locality of every maximum in §13.3's factor), CARL
  and LEV-E (no compounding), GAP and LU-ex. Then (if confirmed) propagate to RLARGE's (CLS-min) consumer and to BFT's clause
  request (§13.8 item (4) is then supplied by SQ itself).
