# BFT_A_LOG (BFT lane A)

## Session 1, 2026-10-28 UTC
- 04:40-04:47 read (read-only): REVIEW_S22 (all), PROOF l.2305-2312, 2995-3010, 3150-3240, 3370-3530, 5289-5300, 5596-5712,
  6255-6368; RTARGET §33-37; LINEAR_PACKAGE §1-4, §6, §10; SF §6.2, §7.2; REVIEW_HIST_S4 S4-1; REVIEW_SQ_S1 (S1-4, strategic).
  BFT_B.md did not exist at 04:47.
- 04:48 checks/ba1_criteria.md written (before the script). Then checks/ba1_cz.py.
- 04:48:43-04:48:44 ba1 under the numeric lock (mkdir lock, load 2.8, 42% free; nice 10; thread env vars 1; python3 without
  -I; no timeout; rmdir once; no process left). 1.4 s, peak RSS 0.67 GB. A1, A2, A3 PASS (BFT_A §4).
- ≈04:55 BFT_A.md written in ONE write (§1 definitions, §2 statements, §3 proofs, §5 outcome). §2 was composed before §3 in
  reasoning only; it is not a file-order pre-statement (disclosed in the §2 heading). 04:56 corrections in place: the §2/§3
  timestamps (a first draft wrongly said 04:53-05:05 and "from 05:05"), C_ρ (the BCH commutator term of ρ was undercounted:
  now 10.2p_L² + L²), BA-8's y = 0 term, BA-12's Taylor constant and the [A^T, χ]A commutator term.
- Results (unreviewed): BA-2 COMP-F2 (the lift is not a centre for any decaying norm); BA-4/BA-5 (second-order centring
  cancellation; the polar part has no y² term); BA-6 (§33 X_c too weak for (CL-2) at soft levels, Ω = k; 𝔐^∇ fixes it); BA-7/BA-8
  (COMP-F1 absorbed inside one coarse unit); BA-9 ((CL-4) in Balaban's convention); Theorem BA (BFT-0/1/2 on 𝒞_glob ⇐
  (H-lin^∇) + (H-rem^∇) + (FP♯')); BA-11/BA-12 ((G♯-patch) ⇐ (COMM) + (UHL) + (SL-cov)).
- Not done: (H-lin^∇) (OPEN), (H-rem^∇) beyond second-order sizes (ARGUED), (UHL), (SL-cov), G0-F3. No commits, PRs, pushes; no
  edits outside BFT_A.md, BFT_A_LOG.md, checks/ba1_*.

## Session 2, 2026-10-28 UTC (lead of BFT lane A, session 2)
- ≈05:13-05:38 read (read-only): REVIEW_BFT_A_S1 (all, binding), BFT_A.md (all), BFT_A_LOG.md, LINEAR_PACKAGE.md (all),
  RTARGET §33-37 (l.572-667), checks/c26_led.py + c26_criteria.md + c26 outputs (symbol code to be reused by ba2).
  REVIEW_BFT_B_S1.md did not exist at 05:13 (checked).
- 05:39:15 §6 [RBA1-fix] appended to BFT_A.md (F1-F8; l.18, l.93, l.292 relabelled by appended notes, nothing above §6
  edited). 05:39:32 one in-place correction inside §6 (the F6 Lipschitz constant, made with the Edit tool). **Disclosure:
  the Edit tool rewrote the file, so BFT_A.md's APFS birth time is now 05:39:32 UTC, not session 1's 04:55:24 UTC (that
  value is recorded in REVIEW_BFT_A_S1 Part 1).** From here on BFT_A.md is only appended to (shell >>), not rewritten.
- 05:40:30 §7 PRE-STATED (session 2) appended (statements BL-1..BL-7, BL-C, failure modes BA2-F1..F5, ba2 plan); no
  session-2 proof was in the file at that time. stat taken immediately after (times printed in local EDT by stat with a
  Z-format string; they are EDT = UTC-4, i.e. born 05:39:32Z, modified 05:40:30Z):
  `BFT_A.md born 2026-10-28T01:39:32Z | modified 2026-10-28T01:40:30Z | size 56805 bytes`
  same stat re-taken with TZ=UTC at 05:41:04Z (file unchanged since 05:40:30Z): `BFT_A.md born 2026-10-28T05:39:32Z | modified 2026-10-28T05:40:30Z | size 56805 bytes`
- 05:42:40 checks/ba2_criteria.md written (APFS birth 05:42:40Z; its header says "≈05:44", a rounding error in the
  header; the file time is the record). 05:44:54 checks/ba2_lin.py (written with the Write tool, then one sed fix of a
  sparse abs() call; its birth time 05:44:54Z is after the criteria). The script imports checks/c26_led.py (read-only).
- 05:45 ba2 launched in the background under the numeric lock; the lock was held by another agent of this session
  (a scratchpad python process started ≈05:44Z), so the run waited.
- 05:49:40 §8 proofs appended (BL-1..BL-7, BL-C). While proving, two dated notes were added inside §8 rather than
  editing §7: (1) 8.7 "Qualification": BL-6 (a)'s parenthetical claim is proven for the image representative, but that
  representative's source can vanish (d* only sees plane directions), so BL-7 (d)'s "(G♯-up) not implied" is narrowed to
  "not implied via the image representative"; (2) 05:50:21 a correction of a too-strong constant in the 8.7 step example
  (conclusion unchanged).
- 05:51:36-05:53:33 ba2 under the numeric lock (load 5.39, 53% free; nice 10; thread variables 1; python3 without -I;
  no timeout; rmdir once; no process left; no __pycache__ in checks/). V 8.3 s / 0.82 GB, M 108.7 s / 0.27 GB. All
  pre-registered criteria PASS (V0-V4, Q1-Q3 for every κ and α). Results in BFT_A §9.
- ≈05:52 read REVIEW_BFT_B_S1.md (born 05:25:02Z; written without REVIEW_BFT_A_S1): its merged open list names (G♯-res)
  as feeding BFT-3; noted in BFT_A §10 (m > 0 version ARGUED only).
- 05:54:34 §9 (ba2) and §10 (outcome) appended. Final stat: `BFT_A.md born 05:39:32Z | modified 05:54:34Z | size 79088`.
- Results (unreviewed): BL-5 (a) (G♯-res) PROVEN for gauge-invariant outputs (data + residual sources, α ≤ θ, uniform in
  k, T); BL-5 (c) α ≤ θ necessary and ω^R_0 must be L^{θk}; BL-6 (b) F3's slot fails for θ ≤ 1 - α; BL-4 upper-level
  curvature Hölder of the data response. OPEN: (G♯_0-lev0), (G♯-up), (G♯-rough), (G♯_0-field^∇), m > 0 written proofs.
- No commits, PRs, pushes; no CL or axiom edits; files written: BFT_A.md, BFT_A_LOG.md, checks/ba2_criteria.md,
  checks/ba2_lin.py, checks/ba2_outV.txt, checks/ba2_outM.txt, checks/ba2_time.txt.

## Session 3, 2026-10-28 UTC (lead of BFT lane A, session 3)
- ≈06:09-06:30 read (read-only): REVIEW_BFT_A_S2.md (all, binding), BFT_A.md (all), BFT_A_LOG.md, LINEAR_PACKAGE.md
  (l.1-400: §1-§6), PROOF_session16_snapshot.md l.1960-1990 (LES statement, for B7), RTARGET.md l.590 (weighted Campanato),
  checks/ba2_lin.py, ba2_criteria.md, ba2_time.txt, checks/c26_led.py l.1-130 (chain code reused by ba3).
- Start stat (TZ=UTC, 06:30:26Z): `BFT_A.md born 2026-10-28T05:39:32Z | modified 2026-10-28T05:54:34Z | size 79088`.
- 06:30:57Z §11 [RBA2-fix] appended (shell >>). Its heading says "≈06:35 UTC": a wrong estimate written into the heading
  before the append; the file time 06:30:57Z is the record. Stat after: size 85494.
- 06:32:01Z §12 PRE-STATED (session 3) appended (shell >>; statements and definitions only; no session-3 proof in the
  file; no ba3 file existed: `ls checks | grep -c ^ba3` = 0 at 06:30:26Z). stat taken immediately after (TZ=UTC):
  `BFT_A.md born 2026-10-28T05:39:32Z | modified 2026-10-28T06:32:01Z | size 93716 bytes`
  Disclosure: exploratory reasoning (not recorded) preceded §12, as for §7; §12's file-order priority is the only claim.
- 06:33:50Z checks/ba3_criteria.md written (APFS birth 06:33:50Z; its header says "≈06:34"). Then checks/ba3_rough.py
  (Write tool, before any run; imports checks/ba2_lin.py and checks/c26_led.py read-only).
- 06:36:20Z-≈06:36:35Z ba3 under the numeric lock (load 2.38, 35% free; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1;
  PYTHONDONTWRITEBYTECODE=1; python3 without -I; no timeout; rmdir once; no process left and no __pycache__ in checks/,
  verified 06:39:08Z). 14.8 s, peak RSS 0.73 GB. All pre-registered criteria PASS (R0, R1a-c, R2, R3, R4, R5a-c).
  Outputs checks/ba3_out.txt, checks/ba3_time.txt.
- 06:41:13Z §13 proofs appended (after ba3 had run; the proofs were written knowing the ba3 outputs, which test only
  exact identities and deterministic bounds). 06:42:14Z a dated correction to 13.4's constant (5/κ_- → 8/κ_-; heading
  "≈06:43"), §14 (ba3) and §15 (outcome) appended. Final stat: `BFT_A.md born 05:39:32Z | modified 06:42:14Z | size 121185`.
- Results (unreviewed): PROVEN-HERE Lemma RS, BR-1, BR-2 (level-0 image of a rough current has exactly its sup size:
  BA3-F4 occurs), CR-1 (commutator row is residual type), SPD (BCH₂ row, carried current ≤ C_SPDκL^{-(m-l)}η²), TS,
  Proposition W and Theorem W (weighted gauge-invariant data + residual sources), Lemma Λ (C_Λ = 10), LR-pot (tent-axial
  slice, potentials), Corollary FP. NOT PROVEN: Theorem G♯-rough (reduced to the level-0 images; X_s part ⇐ (RP)),
  Theorem H-lin_inv ((G♯-rough) + (SB) ⇒ it). OPEN: (RP), (SB), LR-grad.
- No commits, PRs, pushes; no CL or axiom edits; files written: BFT_A.md, BFT_A_LOG.md, checks/ba3_criteria.md,
  checks/ba3_rough.py, checks/ba3_out.txt, checks/ba3_time.txt.

## Session 4, 2026-10-28 UTC (lead of BFT lane A, session 4)
- ≈07:04-07:19 read (read-only): REVIEW_BFT_A_S3.md (all, binding), BFT_A.md l.1-60, l.437-480, l.797-1222, BFT_A_LOG.md,
  LINEAR_PACKAGE.md l.49-260, l.330-384, the reviewer probe scratchpad/revbftA3/rev3_probe.py + probe_out.txt,
  checks/ba2_lin.py function list. Reasoning beyond reading took place before the first edit (disclosed in §16).
- Start stat (TZ=UTC, 07:19:03Z): `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T06:42:14Z size 121185`;
  `ls checks | grep -c ^ba4` = 0.
- 07:19:47Z §16 PRE-STATED (session 4) appended (shell >>; first edit of the session; statements, definitions, failure
  modes, ba4 plan only). stat immediately after (TZ=UTC):
  `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T07:19:47Z size 129454`
- 07:21:53Z checks/ba4_criteria.md written (Write tool; trend criteria with a-priori thresholds only, no session-4 proof
  constant: none had been written). 07:24:02Z checks/ba4_lrl.py (Write tool), 07:24:25Z one scripted fix (flux helper
  cleanup, S2 formula) before any run.
- 07:24:45Z-07:27:00Z ba4 under the numeric lock (load 2.61, 46% free; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1;
  PYTHONDONTWRITEBYTECODE=1; python3 without -I; no timeout; no trap; one rmdir). Parts D3 127 s / 0.44 GB, D1a 1.3 s /
  0.33 GB, D1b 2.5 s / 0.50 GB, D2 3.8 s / 0.66 GB. S1-S3, T1, T3 PASS; **T2 FAIL** (Q_XR trend over T = 2..5).
- 07:32:32Z checks/ba4b_criteria.md and checks/ba4b_diag.py written in one shell command (criteria first in the command;
  same-second birth times; **post-hoc**, after ba4's outputs were read). 07:32:44-07:32:46Z ba4b under the lock (45% free,
  2.0 s / 0.49 GB): discriminator FAIL (log growth of B(T) not excluded at T ≤ 6); Q_XR ≤ B(T) at all T.
- 07:33:54Z checks/ba4c_profile.py (post-hoc, informational, no criterion); 07:34:03-07:34:05Z under the lock (40% free,
  1.9 s / 0.87 GB). Afterwards: no process left, lock directory gone, no __pycache__ in checks/ (verified 07:41Z).
- 07:36:19Z §17 [RBA3-fix] appended; 07:38:33Z §18 proofs appended (all session-4 constants first written here, after the
  runs); 07:40:45Z dated correction to 18.2 (ii) (torus wrap of the box cube), §19 (ba4, ba4b, ba4c) and §20 (outcome)
  appended; 07:41:05Z a dated wording correction to §19. All by shell >>. Final stat:
  `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T07:41:05Z size 164731` (birth unchanged: no rewrite).
- Results (unreviewed): PROVEN-HERE Lemma TK, **LRL (a)**, Lemma FC, **Theorem XR** (X_s part of (G♯-rough), every
  0 ≤ l < k), **Theorem XB** (X_s response of carrier-decaying co-closed currents, with Lemma TOP repairing the review's
  top term, which carried a log T), **Corollary HX** ((H-lin^∇) for the X_s outputs, m = 0), Proposition CO (reduction of
  the curvature outputs to (CO-0)/(CO-up), both OPEN). LRL (b) OPEN. Numerics: LRL (a) ratio T-flat and depth-saturating;
  Theorem XR's trend over T ≤ 6 not established (T2, ba4b FAIL).
- No commits, PRs, pushes; no CL or axiom edits; files written: BFT_A.md, BFT_A_LOG.md, checks/ba4_* , checks/ba4b_*,
  checks/ba4c_*.

## Session 5, 2026-10-28 UTC (lead of BFT lane A, session 5)
- ≈07:58-08:28 read (read-only): REVIEW_BFT_A_S4.md (all, binding), BFT_A.md l.437-575, l.869-998, l.1226-1673, BFT_A_LOG.md,
  LINEAR_PACKAGE.md l.164-205, l.356-384, l.462-493, the reviewer's scratchpad/revbftA4/rev4_rp.py, rp*_out.txt and
  rev4_probe.py l.1-120. Reasoning beyond reading took place before the first edit (disclosed in §21).
- Start stat (TZ=UTC, 08:08:57Z): `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T07:41:05Z size 164731`;
  `ls checks | grep -c ^ba5` = 0.
- 08:29:07Z §21 PRE-STATED (session 5) appended (shell >>; first edit of the session; statements, definitions, failure
  modes, ba5 plan only). stat immediately after (TZ=UTC):
  `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T08:29:07Z size 173466`
- 08:30:35Z checks/ba5_criteria.md written (Write via shell heredoc; exactness tolerances, a-priori factor 2, trend rules;
  no session-5 constant). 08:32:34Z checks/ba5_y.py (Write tool), 08:33:04Z one scripted fix (B1 cube side) before any run.
- 08:33:12Z acquisition 1 (load 2.06, 41% free): P1 PASS. P2 stalled at r = inf (CG on a roundoff RHS).
  - ≈08:43Z I stopped it with `pkill -f "ba5_y.py P2"`. The pattern also matched the parent shell, which died before its
    rmdir.
  - Verified no ba5 process was left, then released the lock by one manual rmdir at 08:43:52Z.
  - 08:44:00Z post-hoc script fix: r = inf uses the exact 0 of Lemma LD after printing the roundoff; RSS label GB → MB.
- 08:44:11Z-08:48:52Z acquisition 2 (load 2.68, 37% free; one rmdir): P2 (63 s), P4a (18 s), B1 (2 s), P4b (198 s). Peak
  RSS 0.80 GB. nice 10, thread variables 1, PYTHONDONTWRITEBYTECODE=1, python3 without -I, no timeout, no trap.
  - Results: P1, P2a, P2b, P3, Y1-Y4 PASS; **B1 FAIL** (bootstrap proxy not decreasing for r/n ≤ 3).
  - No process left, no __pycache__ in checks/. Record: checks/ba5_time.txt.
- 08:46:05Z §22 [RBA4-fix] appended (P2'', T1-T7, scope lines). T3: barycentre identity proven. T2: adopted, with a dated
  remark that the review's count formula looks wrong (the count is (8/3)t(t² + 2); the original bound holds).
- 08:51:40Z §23 proofs appended (all session-5 constants first written here, after the runs; three dated precisions to
  §21: φ ∈ C^{3,1}, the Case A/B split at T ≥ 8L^c, a stronger support statement in LD).
- 08:52:26Z §24 (ba5) and §25 (outcome) appended. All by shell >>. Final stat:
  `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T08:52:26Z size 207093` (birth unchanged: no rewrite).
- Results (unreviewed):
  - PROVEN-HERE: Lemma PC, Lemma DUAL, Lemma LD, Lemma EX, Lemmas DX/DB, **Theorem Y** (localized level-0 source response,
    dual form, k, T-uniform), **Theorem CO-0R**, Lemma RH, **Theorem CO-upR**, **Corollary G♯R** (Theorem G♯-rough, all
    gauge-invariant outputs, m = 0, α < θ), **Theorem CO-B**, **Corollary HL** (Theorem H-lin_inv, m = 0, trivial
    background, co-closed BCH₂ rows).
  - OPEN: LRL (b) (not attempted), the non-co-closed BCH₂ remainder, m > 0, nontrivial background.
- No commits, PRs, pushes; no CL or axiom edits. Files written: BFT_A.md, BFT_A_LOG.md, checks/ba5_criteria.md,
  checks/ba5_y.py, checks/ba5_out_{P1,P2,P4a,P4b,B1}.txt, checks/ba5_err_{P1,P2,P4a,P4b,B1}.txt, checks/ba5_time.txt.

## Session 6, 2026-10-28 UTC (lead of BFT lane A, session 6)
- ≈09:12-09:24 read (read-only): REVIEW_BFT_A_S5.md (all, binding; born 09:10:51Z), BFT_A.md l.1-330, l.380-580, l.885-945,
  l.1050-1070, l.1101-1160, l.1240-1260, l.1676-2182, BFT_A_LOG.md, LINEAR_PACKAGE.md l.170-182, l.460-472, PROOF.md
  l.3418-3475, checks/ba5_y.py (all), checks/ba5_criteria.md. Reasoning beyond reading took place before the first edit
  (disclosed in §26).
- Start stat (TZ=UTC, 09:24:56Z): `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T08:52:26Z size 207093`;
  `ls checks | grep -c ^ba6` = 0.
- 09:30:07Z §26 PRE-STATED (session 6) appended (shell >>; first edit of the session; statements, definitions, failure
  modes, ba6 plan only; Steps 2, 3 and 4 pre-stated together). stat immediately after (TZ=UTC):
  `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T09:30:07Z size 218296`
- 09:30:35Z checks/ba6_criteria.md written (shell heredoc; exactness tolerances, inequality checks, a-priori factor 2,
  trend rules; no session-6 constant). 09:31:37Z checks/ba6_w0.py (Write tool; imports checks/ba5_y.py read-only),
  09:31:57Z one scripted fix (precompute the gradients in E5) before any run.
- 09:32:18Z-09:33:50Z ba6 under the numeric lock, one acquisition (pre-launch check: load 5.51, 34% free; at acquisition:
  load 7.78, 31% free; nice 10; thread variables 1; PYTHONDONTWRITEBYTECODE=1; python3 without -I; no timeout; no trap;
  no pkill; one rmdir). Part A 22 s / 79 MB, part K 70 s / 755 MB peak (k = 2, T = 4). All criteria PASS (E1, E4, H1, H2,
  N1, N2, LE1). Record checks/ba6_time.txt. Check at 09:37:30Z: `pgrep -fl ba6_w0.py` → none; `ls -d checks/__pycache__`
  → absent; lock directory absent.
- 09:33:01Z §27 [RBA5-fix] appended (P1''', S4-T2, U1-U9, plus U4' sharpening and the support-side precision; written
  while part K ran, independent of ba6). 09:39:26Z §28 proofs appended (all session-6 constants and PROVEN-HERE headings
  first written here, after the runs; four dated precisions to §26). 09:40:30Z §29 (ba6) and §30 (outcome) appended. All
  by shell >>. Final stat: `BFT_A.md born 2026-10-28T05:39:32Z mod 2026-10-28T09:40:30Z size 256215` (birth unchanged:
  no rewrite).
- Results (unreviewed):
  - PROVEN-HERE: Lemma CS, Lemma TOPD, Lemma LE, **Theorem YH**, **Theorem W0** ((G♯_0-lev0), m = 0), Corollary WR (a),
    **Theorem GU** ((G♯-up), m = 0, α < θ), **Corollary LIN0** (gauge-invariant (H-lin^∇) on BL-7's pair, level-wise
    co-closed sources), Lemma FG, Lemma BOG, Proposition NC, Corollary NC, U4' (L^c ≥ max(260, 3476C_j)), Lemma BW,
    Theorem Y_m's 𝒩_m part.
  - OPEN: (NC-Γ) (gauge-fixing-dependent remainders V_l), DX_m/DB_m and the weighted Hölder parts (m > 0), nontrivial
    backgrounds, the gauge-variant half. ARGUED: 𝒬_{H,m}.
- No commits, PRs, pushes; no CL or axiom edits. Files written: BFT_A.md, BFT_A_LOG.md, checks/ba6_criteria.md,
  checks/ba6_w0.py, checks/ba6_out_{A,K}.txt, checks/ba6_err_{A,K}.txt, checks/ba6_time.txt.

## Session 7, 2026-10-28 UTC (lead of BFT lane A, session 7)
- ≈09:55-10:12 read (read-only): REVIEW_BFT_A_S6.md (all, binding), BFT_A.md l.14-30, l.200-235, l.437-470, l.800-842,
  l.910-935, l.1716-1730, l.1962-1973, l.2018-2034, l.2185-2728, BFT_A_LOG.md, BFT_B.md l.2009-2068, l.2121-2160,
  l.2446-2565, PROOF.md l.2101-2125, l.3418-3440, checks/ba6_w0.py, checks/ba6_criteria.md, checks/ba5_y.py (Chain class).
  Reasoning beyond reading took place before the first edit (disclosed in §31).
- LEAD DECISION recorded in §31: both BFT lanes use lane B's elliptic slice S_E as the single gauge fixing (Γ := Γ_E).
- Start stat (TZ=UTC, 10:12:49Z): `BFT_A.md born 2026-10-28T05:39:32Z | mod 2026-10-28T09:40:30Z | size 256215`;
  `ls checks | grep -c ^ba7` = 0.
- 10:13:50Z §31 PRE-STATED (session 7) appended (shell >>; first edit of the session; statements, definitions, failure
  modes, ba7 plan only; Steps 2, 3 and 4 pre-stated together). stat immediately after (TZ=UTC):
  `BFT_A.md born 2026-10-28T05:39:32Z | mod 2026-10-28T10:13:50Z | size 268696`
- 10:15:19Z checks/ba7_criteria.md written (shell heredoc; exactness tolerances, inequality checks, a-priori factor 2,
  trend rules; no session-7 constant). 10:16:13Z checks/ba7_s7.py (Write tool; imports checks/ba5_y.py and checks/ba6_w0.py
  read-only); no fix before the run.
- 10:16:53Z-10:17:37Z ba7 under the numeric lock, one acquisition (pre-launch check 10:16:15Z: load 2.59, 44% free; at
  acquisition: load 3.36, 43% free; nice 10; thread variables 1; PYTHONDONTWRITEBYTECODE=1; python3 without -I; no
  timeout; no trap; no pkill; one rmdir). Part A 14 s / 118 MB, part K 30 s / 314 MB (k = 3, T = 1). All criteria PASS
  (E1, E2, H3a, H3b, N3). Record checks/ba7_time.txt. Check at 10:19:39Z: `pgrep -fl ba7_s7` → none (exit 1);
  `ls -d checks/__pycache__` → absent; lock directory absent.
- 10:17:18Z §32 [RBA6-fix] appended (P6-1..P6-7; written while part K ran, independent of ba7). 10:25:20Z §33 proofs
  appended (all session-7 constants and PROVEN-HERE headings first written here, after the runs; seven dated precisions
  to §31/§32, incl. a line-number correction to P6-2's citations). 10:26:38Z §34 (ba7) and §35 (outcome) appended. All by
  shell >>. Final stat: `BFT_A.md born 2026-10-28T05:39:32Z | mod 2026-10-28T10:26:38Z | size 305985` (birth unchanged:
  no rewrite).
- Results (unreviewed):
  - PROVEN-HERE: Lemma GE, Lemma TD, Lemma CD (given (GI)), Lemma IP, Lemma LES-dd, Theorem W0-loc, Lemma WT, Lemma QH_m,
    **Theorem W0_m** (weighted W0, all parts, 0 ≤ m ≤ m_Y), Proposition SM (a)-(b).
  - PROVEN as implications: **Proposition SR** ((NC-Γ) sup of f_0 for Γ_E without the factor k ⇐ (PW-ℓ¹) + SPD);
    Proposition SM (c) (configuration half for T ≤ 4 ⇐ lane B).
  - ARGUED: Proposition CD2; the obstruction (ND) of Proposition OB for generic configurations; Γ_EK_x invertibility.
  - OPEN: (PW-ℓ¹) (the named wall of (NC-E)); the rest of (NC-E); DX_m, DB_m; whether m_Y suffices downstream.
- No commits, PRs, pushes; no CL or axiom edits. Files written: BFT_A.md, BFT_A_LOG.md, checks/ba7_criteria.md,
  checks/ba7_s7.py, checks/ba7_out_{A,K}.txt, checks/ba7_err_{A,K}.txt, checks/ba7_time.txt.

## Session 8, 2026-10-28 UTC (lead of BFT lane A, session 8)
- ≈10:58-11:21 read (read-only): REVIEW_BFT_A_S7.md (all, binding), BFT_A_LOG.md, BFT_A.md l.440-500, l.598-612,
  l.890-945, l.1123-1160, l.1688-1757, l.1874-2018, l.2185-2484, l.2729-3266, BFT_B.md l.2014-2075, l.2143-2160,
  l.2231-2258, checks/ba5_y.py l.1-240, checks/c26_led.py l.55-100, scratchpad/revbftA7/rev7_diag.py, out_D2.txt.
  Reasoning beyond reading took place before the first edit (disclosed in §36).
- Start stat (TZ=UTC, 11:21:54Z): `BFT_A.md born 2026-10-28T05:39:32Z | mod 2026-10-28T10:26:38Z | size 305985`;
  `ls checks | grep -c ^ba8` = 0.
- 11:23:19Z §36 PRE-STATED (session 8) appended (shell >>; first edit of the session; definitions, statements, failure
  modes, ba8 plan only; no forward reference). stat immediately after (TZ=UTC):
  `BFT_A.md born 2026-10-28T05:39:32Z | mod 2026-10-28T11:23:19Z | size 315783`
- REQUEST TO LANE B (logged, not edited in BFT_B): the named hypothesis (GE-T) of BFT_A §36.0 (an ℓ¹ bound, per level,
  for the S_E representative of the funnel-compensated root-consistent chain u⃗^♮ of a co-closed dipole-type level-0
  field: ||(Π_Eu⃗^♮)_l||_1 ≤ C_GTL^{-3l}R).
- 11:24:37Z checks/ba8_criteria.md written (shell heredoc; exactness tolerances, a-priori factor rules; it records the sign
  error of §36.0's Π^♯, found while writing it, before any script). 11:25:56Z checks/ba8_fun.py (Write tool; imports
  checks/ba5_y.py and checks/c26_led.py read-only); syntax check by ast.parse only; no fix before the run.
- 11:27:02Z-11:28:51Z ba8 under the numeric lock, one acquisition (load 2.33, 38% free at acquisition; nice 10; thread
  variables 1; PYTHONDONTWRITEBYTECODE=1; python3 without -I; no timeout; no trap; no pkill; one rmdir). E1 1 s / 102 MB,
  E2 108 s / 297 MB. E1 PASS; BA8-F3 OCCURS; BA8-F4, BA8-F6 do not occur. Record checks/ba8_time.txt. Check after the run:
  `pgrep -fl ba8_fun` → none (exit 1); `ls -d checks/__pycache__` → absent; lock directory released by the rmdir.
- 11:35:55Z §37 [RBA7-fix] appended (P7-1..P7-8). 11:38:50Z §38 proofs appended (all session-8 constants and PROVEN-HERE
  headings first written here, after the run; four dated precisions to §36, incl. the sign of Π^♯ and the range of (GE-T)).
  11:39:34Z §39 (ba8) and §40 (outcome) appended. All by shell >>. Final stat:
  `BFT_A.md born 2026-10-28T05:39:32Z | mod 2026-10-28T11:39:34Z | size 351969` (birth unchanged: no rewrite).
- Read for Step 3 (read-only, after the run): BFT_B.md l.73-100, l.410-428, l.2084-2090, l.2290-2300, l.2447-2450; SF.md
  l.840-856, grep of M_min/m_1; REVIEW_S22.md l.405-432; RLARGE.md grep R_bg; FLOW.md grep SF-bg. REVIEW_BFT_B_S6 not read
  (its verdicts are cited from REVIEW_BFT_A_S7).
- Results (unreviewed):
  - PROVEN-HERE: Lemma DF, **Theorem PW-cc** (co-closed half of the dual (PW-i), every level), Proposition RF, Proposition
    TE (identity), Lemma RC (sign corrected).
  - PROVEN as an implication: Theorem PW-E ((GE-T) ⇒ (PW-i) for Γ_E).
  - ARGUED (with ba8): Proposition FS (funnel spike ≈ 0.003 own units, level- and k-independent); (GE-T) and (PW-i) for
    Γ_E expected FALSE for large k; (NC-Γ) for Γ_E expected FALSE away from the critical set; requirement table MR (no rate
    threshold; two rows NOT DETERMINED).
  - OPEN: (PW-ii); a slice top-anchored for Y^p and 𝔐^∇-compatible for configurations; the weighted (NC-E).
- REQUEST TO LANE B (amended): (GE-T) as stated is expected false for S_E (BFT_A 38.8); the useful question for lane B is
  a slice whose representative of Y^p is top-anchored at roots.
- No commits, PRs, pushes; no CL or axiom edits. Files written: BFT_A.md, BFT_A_LOG.md, checks/ba8_criteria.md,
  checks/ba8_fun.py, checks/ba8_out_{E1,E2}.txt, checks/ba8_err_{E1,E2}.txt, checks/ba8_time.txt.
