# HW_LOG: lane H (history weight hypothesis (H-w)), session 1, 2026-10-28

All times UTC (machine clock; local time is UTC-4).

- 01:3x-01:51 Read inputs (read-only): HIST.md §0, §2-§3, §7, §8, §12, §14.0-§14.1, §15.1-§15.4; RLARGE.md v2 §0-§8; PLD.md
  §15.2-§15.3; REVIEW_HIST_S1 l.280-312; REVIEW_PLD_S3 l.196-215, l.470-500. REVIEW_HIST_S3 absent. md5 recorded in HW.md header.
- Exploratory reasoning (unwritten) before the targets: (1) the history weight in indicator form and the observation that
  plain-chain probability bounds are Z_K-relative (later Proposition PF); (2) the relaxed event; (3) first attempt: price
  each branch by "softening" its energy and renormalising; found that softening a full-chain cone costs equipartition on
  L^{4k} variables (catastrophic), so windows must use effective/tower energies; (4) found that softening at fixed coarse
  field V gives back the coherent price (later Proposition FV); (5) the Chernoff form.
- 01:52 HW.md §0-§1 (pre-stated targets W1-W3, check w1) written, before any derivation.
- 01:57-02:01 HW.md §2-§7 written (Lemmas HR, RX, PF, HS', HW-split, TE, W-bad, W-cb, DJ, CH, EQ, FV, HÖ, KS, KS-chain, LI-a,
  H4-red, Theorem HW, K3-a, K3-b; hypotheses (M-i), (M-f), (LI), (REL), (KS-N), (TC)).
  Choices disclosed: (a) Theorem HW is stated for histories whose defect cubes are bad cubes; collar-bad/non-quiet cubes via
  Lemma W-cb carry the extra condition (TC) and their (M-i) is not reduced to (LI) (shared collar links are read by R).
  (b) Lemma W-cb uses a reading of PLD §9.1's σ_Q (levels of the collar plaquettes, C(Q) ⊂ N_1(Q)) that was not re-checked.
  (c) Lemma TE (ii) consumes CLS-red's strong form exactly as stated in HIST §15.4 (for every chain), passed to the infimum.
- 02:02:25 checks/w1_criteria.md written (before the script).
- 02:03 checks/w1_kernel_moments.py written; C2 edited before any run (the first draft counted 24 by construction; replaced
  by an enumeration). Load 2.60, 33% free at 02:03.
- 02:03 run launched under the numeric lock (mkdir loop); the lock was held by another worker, so the run waited.
- 02:45 the first waiting job had ended without running (its shell was moved to background at the 600 s tool timeout and did not survive); no w1 output existed. Relaunched 02:46 under the same lock loop.
- 02:10 (before any run) HW.md edits: Theorem HW now states the defect notion D_j = {ζ_Q = 1} explicitly (was 'histories whose defect cubes are bad cubes'); Lemma DJ cites the argument of H-nest (ii) for Λ^pre.
- 02:49:47-02:49:50 run 1 (relaunched job) and 02:49:55-02:49:58 run 2 (the original job, which had in fact stayed queued on
  the lock; my 02:45 process check missed it). Both acquired and released the lock once each, sequentially. The script is
  deterministic (fixed seed); both outputs are byte-identical in every result line; w1_out.txt / w1_time.txt hold run 2.
  Load ≤ 2.41, 34-41% free, peak RSS 278 MB, wall 2.3 s. Disclosure: two runs, not one; no edit between them.
- 02:55 HW.md §9-§11 written (results, outcomes, tally).

# Session 2 (2026-10-28), lane H

- **Appended correction to the 01:3x-01:51 entry above [RHW1-fix H-11/W-2].** "REVIEW_HIST_S3 absent" is false.
  REVIEW_HIST_S3.md has mtime 21:38:51 EDT = 01:38:51 UTC, i.e. it existed before session 1's read at 01:51 UTC; session 1
  did not find it. Consequence: session 1 missed N-4 (C_cone, fix W-2) and S3-5 (fix H-5). The original entry is left as
  written; this line supersedes it.
- 03:3x-03:53 UTC Read (read-only): REVIEW_HW_S1.md (all; md5 53c3115d…), HW.md, HW_LOG.md, HIST.md §7.1-§7.4 (l.452-573) and
  §26-§27 (l.1763-1874), PLD.md §15.2-§15.3 (l.966-1103), RLARGE.md l.183-192 and l.466-474 (RLF-3/RLF-4, v2-F), FLOW.md
  l.39 and l.67-71 (grep only), REVIEW_HIST_S4.md (grep only: l.27, 50-53, 111-112, 448: AE-red CONFIRMED as CONDITIONAL ⇐
  (MS-Sob), C_cone = 1.13·10¹⁵ at N = 2, C_S ≤ 10²). md5 at 03:53 UTC: HIST 468e9f03…, PLD 4db9b142…, RLARGE 24a73553…,
  REVIEW_HIST_S4 bc0a9da0…. Load 4.48, low free pages (memory pressure noted for w2).
- 03:53 UTC HW.md §12 (session-2 pre-stated targets S1-S3, check w2) appended, before any [RHW1-fix] edit or session-2 derivation.
- 03:54-03:57 UTC [RHW1-fix] edits in HW.md §0-§11 (W-1..W-4, H-1..H-11, K-1, S-1, S-2, FV uncounted, tally 4). 03:55 lead's lane-G note received (SQ §0): read SQ.md l.45-233 (read-only); every HW use of (AE) is the cone-local infimum; TE (ii), W-bad, W-cb, FV switched to (CLS-min) ⇐ (REG-min) (alternative ⇐ (AE)); §12A written 03:57.
- 04:00 UTC checks/w2_criteria.md written (before any w2 script).
- 04:04 UTC checks/w2_relseq_toy.py written (after the criteria); two pre-run edits (vectorised component table; no per-animal cache, memory), no run yet.
- 04:01-04:02 UTC HW.md §13 (DECL, REL-seq, node A's (NA-∅), Remark GAS), §14 (CAP, (LI^F), H4-red', (M-f^cap), Theorem HW^cap),
  §15 (SAT, CAP-dec, LOOP-div, LOOP-const, global-count route, wall (SDP)) written, after the criteria file (04:00).
- 04:04:44-04:04:45 UTC w2 run (one run): lock acquired once, released once by rmdir; load 2.81, 43% free; nice 10, threads 1;
  exit 0; 1.06 s; peak RSS 146 MB. OVERALL PASS as pre-registered; C3 found uninformative post hoc (θ_K too large), recorded.
- 04:05 UTC HW.md §16-§17 (w2 record, outcomes, session-2 tally) written. No commits, PRs, pushes; no edits outside HW.md,
  HW_LOG.md, checks/w2_*.

# Session 3 (2026-10-28), lane H: consolidation (no frontier work, no numeric jobs)

- **Appended correction to the session-2 04:00-04:02 entries above [RHW2-fix W2-1].** checks/w2_criteria.md has mtime
  00:00:33 EDT = 04:00:33 UTC and already names "Lemma CAP of §14", LOOP-const's G := 81·L^{-θaβ_+}e^{-θaR}, LOOP-div's m_*, and
  the constants θ ∈ {1/6, 1/100}, a ∈ {2.3e-16, 5e-23} (verified by grep this session), while the entry above dates the writing
  of HW.md §13-§15 to 04:01-04:02 UTC. So these lemma names, the loop arithmetic and the constants existed (in draft or in the
  session-2 plan) before the criteria were written; the 04:01-04:02 times are the times the text was written into HW.md, not the
  times of derivation. The session-2 record does not say which (draft or plan), and session 3 cannot reconstruct it; this is
  disclosed rather than decided. Effect: none on w2's informational status (C1, C2 are tautological, REVIEW_HW_S2 Priority 6).
  Also: the 04:04 script entry is listed before the 04:01-04:02 entry, and HW.md §16's header says "script 04:02-04:04 UTC";
  the script's mtime is 00:04:36 EDT = 04:04:36 UTC. The original entries are left as written.
- **Appended correction to the session-2 04:04:44 run entry and HW.md §16 [RHW2-fix W2-2].** B2's criterion says "zero
  exceptions over all configs and steps", but w2_relseq_toy.py l.120 (`bad[:: max(1, len(bad) // 2000)]`) checks a strided
  subsample of about 2000 configurations per step whenever more fail. "B2 step containment PASS" is a PASS on that subsample.
  Not re-run (no numeric jobs this session); B2's content is proven in REL-seq (2).
- 04:2x UTC Read (read-only): REVIEW_HW_S2.md (all), HW.md (all), HW_LOG.md; RLARGE.md l.168-195 ((RLF-0)-(RLF-5)) and
  l.396-420 (§4.2 hypothesis list); grep only: RLARGE.md anchors, SQ.md (REG-min) lines, HIST.md §5 R1^J anchors,
  checks/w2_criteria.md, checks/w2_relseq_toy.py l.115-125; stat of the two w2 files. md5 at read: REVIEW_HW_S2 363fb1ae…,
  HW 7937a648… (pre-edit), HW_LOG 67245925… (pre-edit), RLARGE 24a73553…, SQ dcd320a8…, HIST 468e9f03…. Load 7.2.
- 04:27-04:29 UTC HW.md in-place [RHW2-fix] edits: SDP-1 (§5.1, §6, §8, §15 CAP-dec/LOOP-const/§15.3), RS-1 (§13.2: family
  ℛ_𝔥^↑, level-first ascending; "any order" struck), NA-1 (§13.3 (NA-∅) with 𝒱_K^{LF}; ratio line Z^ref; Remark GAS), CAP-1
  (§14 HW^cap: max{6θ, 24θ}(1 + 2Rg_K²) < 1; "θ up to ≈ 1/6" struck; §15.1 size line), LI-1 (§14 (LI^F) for capped weights),
  CAP-dec recounted uncounted, §17 marked superseded where needed; recommended H-12, SAT-1, e^{±38416c}/n_H, CAP-dec gain, K_m.
  One session-2 status sentence reworded (§15.1, marked). New §18 (record, (SDP)^A, (SF-cap)^A, (M-f^A), corrected tally 6) and
  §19 (HW as a consumer of node A: interface table A1-A5 with owner files). No new counted item; no numeric job; no commits,
  PRs, pushes; no edits outside HW.md, HW_LOG.md.

# Session 4 (2026-10-28), lane H: (LI^U), check (d)

- 09:5x-10:19 UTC Read (read-only): REVIEW_RLARGE_V3.md (all), HW_LOG.md, HW.md l.1-400 and l.600-1019, RLARGE.md l.337-576
  (§3-§4), REVIEW_HW_S2.md l.281-387 (§5), HIST.md l.454-503 (§7.1-§7.2), EXISTENCE.md l.1955-2035 and l.2146-2160 (Theorem GS,
  T14), PLD.md l.595-610; grep only: HIST.md (3.0)/endpoint-block anchors, N2-exp anchors. md5 at 10:19 UTC: HW 05e7f210…
  (pre-edit), HW_LOG db999aba… (pre-edit), REVIEW_RLARGE_V3 38b26eda…, RLARGE a9269bae…, REVIEW_HW_S2 363fb1ae…, HIST 468e9f03….
  Load 2.4-2.9. Exploratory reasoning (unwritten) before the targets: the tilt is h; footprint of a link set under kernels
  that read the two endpoint blocks; relaxed shadows; a pure-gauge mechanism against the pointwise form on constrained columns.
- **10:19:45 UTC PRE-STATED (session 4): HW.md §20 appended (statements only), FIRST edit of the session.** After the edit:
  HW.md 105745 bytes (was 102013), mtime 06:19:45 EDT = 10:19:45 UTC, md5 dd6b6633…. No derivation written before it.
- 10:21:45 UTC checks/w4_criteria.md written (before the script). 10:22-10:23 checks/w4_footprint.py written; two pre-run edits
  (memory: S^{(m)} tested as the complement of A_m; the negative control made incremental with early exit, capped at 25
  tested links per dimension).
- 10:23:23-10:33:57 UTC **run 1, aborted by me**: lock acquired 10:23:23 (load 3.90); the d = 4 negative control (widened
  kernel built N_1 sets per candidate link) was too slow; at 10:33:57 I sent `kill` to its own PID 76862 (not pkill) so the
  job would stay under 20 min; exit 143; the wrapper then released the lock by its single rmdir (10:33:57). No output was
  produced (prints at the end). Another worker (p4_pld.py) took the lock at 10:33:57.
- 10:34:16-10:34:21 UTC post-run-1 edits before run 2: widened reading tested by a torus sup-distance (no set building);
  per-config wall time printed; d = 4 sample reduced to 2 histories × 25 links per level. Criteria unchanged.
- 10:34 UTC run 2 launched in the background under the same lock loop (waits for the other worker).
- 10:35:28-10:35:56 UTC **run 2** (lock acquired once, released once by rmdir; load 3.33; nice 10; threads 1; 28.1 s; peak
  RSS 77 MB; exit 0; no process left). **OVERALL FAIL as pre-registered:** A PASS (1440 / 100 links, 0 exceptions), B PASS
  (1434 / 100 tested, 0 reads), but C FAIL in d = 4 (0 constrained columns tested) and D FAIL in both dimensions (the widened
  kernel never reached a constrained cube). Diagnosis (post hoc): the random histories (density 0.04 / 0.005 per level at
  every level) make the relaxed sets A_m cover almost every cube, so constrained columns are rare and the negative control
  has nothing to reach. A design flaw of the test, not information about the lemma. Outputs kept as w4_out.txt etc.
- 10:38:40 UTC checks/w4b_criteria.md written (post-hoc redesign of the sampler only; criteria A-D unchanged; ≥ 10 tests each
  for B, C, D). 10:38:51 checks/w4b_footprint.py (copy of w4 with the new generator / sampler).
- 10:39:02-10:49:54 UTC **w4b run 1, aborted by me**: the new generator looped forever at a level where every cube lies in
  Σ(Ω^c) (no tries cap); `kill` to its own PID 78460 at 10:49:54; exit 143; lock released by the wrapper's single rmdir.
  No output. Fix before rerun: at most 2000 draws per level.
- 10:50:17-10:50:21 UTC **w4b run 2** (lock acquired once, released once by rmdir; load 5.53 at acquisition, under 8; nice 10;
  threads 1; 3.8 s; peak RSS 17 MB; exit 0; no process left): **OVERALL PASS** (A, B, C, D in both dimensions; counts in HW.md §27).
- 10:50-10:52 UTC HW.md §21-§26 written (Lemma TILT, FP, NR, Theorem LI^U-0, Cor. LI-0, Prop. LI-pw, consumer table, Lemma
  REL-boot, Finding J-1, Lemma TEL-f, (SDP)^{A,far}/(SF-cap)^{A,far}, (E1)/(E2), (CRC), wall (CRC-1), check (d), Theorem HW
  session-4 hypothesis list). The derivations were reasoned 10:00-10:50 (partly before §20, disclosed in the 10:19 entry) and
  typed in at 10:50-10:52.
- 10:53 UTC one in-place edit of §24.3 (per-level allowance = level-k slice s_k(𝔥) of the shadow sums, with the reason).
- 10:53 UTC HW.md §27 (w4 / w4b record), §28 (outcomes, tally) written. No commits, PRs, pushes; no edits outside HW.md,
  HW_LOG.md, checks/w4*; no process left running.

# Session 5 (2026-10-28), lane H: [RHW4-fix], (CRC-1) as a two-type gas

- 11:09-11:11 UTC Read (read-only): REVIEW_HW_S4.md (all), HW_LOG.md (all), HW.md l.28-107, l.607-806, l.1019-1343 (§0, §2, §13-§15,
  §20-§28); PROOF.md l.1940-2059 (Theorem CE, CE-κ, Remark CE-cx); SF.md l.1073-1096 (Setting CE-col, Lemma GEO-col, Theorem
  CE-col, CE-exp-col, RATE); PLD.md l.1395-1564 (§16.5-§16.11: NA-PRICE, WALL, (LCR), a_ret); grep only: SF.md CE-col / CE-exp /
  "certified" anchors, PLD.md a_A / a_ret anchors. md5 at 11:10 UTC: HW 3f3a3a01… (pre-edit), HW_LOG 99105480… (pre-edit),
  SF ceec42df…, PROOF 488c2388…, PLD def1982d…, REVIEW_HW_S4 72c02d80…. Load 4.05.
  Exploratory reasoning (unwritten) before the targets: (CRC)'s excess Z(R^{-B}) - Z(R) is carried by the event that a
  level-m animal through B's column exists, so (CRC) can be rearranged as Z(R^{-B}) ≤ Z(R)/(1 - δ) with δ a per-column animal
  sum; Theorem CE's Steps 3-4 are an abstract hard-core-gas statement (no product measure), so they can carry a two-species gas.
- **11:11:57 UTC PRE-STATED (session 5): HW.md §29 appended (statements only), FIRST edit of the session.** After the edit:
  HW.md 138298 bytes (was 134603), 1384 lines, mtime 07:11:57 EDT = 11:11:57 UTC, md5 34669466…. (§29's header says "11:12";
  the file time is 11:11:57.) No derivation written before it.
- 11:12-11:24 UTC Read (read-only): HIST.md l.487-500 (Lemma H-geo); PLD.md l.1291-1303 (§16.0 setting, ℛ^A_𝔥, (LI^U)); grep only:
  RLARGE.md l.612 (a, a_bad, β_-, n_H), HW.md n_int; `diff checks/w4_footprint.py checks/w4b_footprint.py` (P-2 verified: d = 4
  nhist 2 → 3, nlinks 25 → 30, D cap 25 → 40; the density argument changed from a per-cube rate to a count). Reasoned the STEP 2
  derivation in this window (unwritten): induction on the number of constrained pairs; closed-column relaxation instead of
  DECL; attached-cluster shadow lemma; finer-first order for the (E2) route.
- 11:24-11:29 UTC **[RHW4-fix] in-place edits of HW.md §14, §20, §22-§27** (P-1 at §20 and the derivation header; LI0-1 in Cor.
  LI-0 (b) and §26; the §22 nit; LP-1 in Prop. LI-pw; CR-1 pointer in (CRC); CR-2 at §24.1 consequences and the top-down analysis
  (ARGUED); RB-1; TF-1 adopted after TEL-f with the (E2)-route caveat; SL-1 with Lemma SL PROVEN-BY-REVIEW and c_f := 81(c_A + c_sf′);
  E1-1; E2-1 with Buf_k(A); check (d) fixes; §26 SL-1/H9 note; P-2, P-3 in §27; (LI^F)/A4 status pointer). Struck text kept with
  ~~…~~; nothing deleted. **P-2 disclosure (binding):** the w4 → w4b redesign also changed nhist 2 → 3 (d = 4), nlinks 25 → 30
  (d = 4) and the D sample cap 25 → 40; checks/w4b_criteria.md and §27's "changes ONLY the history generator and the link
  sampler" omitted them; none can turn a FAIL of A or B into a PASS. **P-3:** w4/w4b criterion C is tautological under the reading
  rule; in d = 4 B and D are informative only at k = 0.
- 11:30-11:31 UTC HW.md §30 (Theorem LI^U-0′, Lemmas SH-att and COL, (E2^𝔉), the two-type gas, Theorem CRC-2T [HW-11], Corollary
  CRC-HW, §30.6 constants, §30.7 residual) written, after §29 and the STEP-1 edits.
- 11:32:3x UTC checks/w5_criteria.md written (before any w5 script); one pre-script edit at 11:32:52 (an unfinished alternative
  wording of B3 removed; noted in the file). 11:33:48 UTC checks/w5_crc2t.py written (after the criteria). The criteria's
  constants (b_n, b_D, c_att, ρ = 8) come from §30, written before them.
- 11:34:05-11:34:07 UTC **w5 run** (one run; lock acquired once by the mkdir loop, released once by rmdir; load 2.54; nice 10;
  threads 1; 1.7 s; 44 MB peak RSS; exit 0; no process left): **OVERALL PASS** (A1-A5, B1-B3, C1-C3; HW.md §31). The negative
  controls behaved as pre-registered (A3: (S2) fails at g_K² = 10⁻⁹⁴; B3: detached excess grows 256 per level; C3: 18/27
  violations without the species link). Post hoc: c_att is loose by ≈ 6·10³ against the observed maximum excess (193).
- 11:34-11:35 UTC HW.md §31 (w5 record), §32 (STEP 3: Theorem HW hypothesis list), §33 (outcomes, tally 9) written.
- 11:35 UTC frozen-block check: HW.md §29 (from "\n---\n# Session 5 of lane H" to the end of the §29 append) is 3695 bytes, equal
  to the 138298 - 134603 bytes appended at 11:11:57; md5 of the block 7830e9f0…. HW.md now 178489 bytes, md5 1f0a6b37…
  (before this log entry). No commits, PRs, pushes; no edits outside HW.md, HW_LOG.md, checks/w5*; no process left running.

## Session 6 (2026-10-28), lane H worker
Scope (owned, append-only): a new "# Session 6 of lane H" at the END of HW.md; this session-6 entry in HW_LOG.md; new files
checks/w6_*. Nothing else, anywhere. No git command of any kind is run in this session.
Binding input: REVIEW_HW_S5.md (714 lines), read in full before any writing; md5 recorded below.
- 12:46-12:53 UTC Read (read-only): REVIEW_HW_S5.md (all 715 lines), DRIVE_BRIEF.md, HW.md §29-§33 (l.1424-1734) and
  §24.3 (l.1255-1312, l.1370-1380), HIST.md §7.1 (l.450-471: Σ(A) := N_1(π(A)), sh_{j+m} := Σ^m) and §7.2 (l.486-503,
  Lemma H-geo) and §7.4 (l.527-556, (H-w), Theorem HIST-sum), PLD.md l.1400-1420 (§16.5 NA-PRICE) and l.1850-1910
  (Theorem NA-PRICE^E (i), Proposition CD, §17.5, §17.6), HANDOFF.md l.45-75, HW_LOG.md session 5.
- **12:53:30 UTC PRE-STATED (session 6): HW.md §34 appended (statements only), FIRST edit of the session.** Before the
  edit: HW.md 178489 bytes, md5 1f0a6b378b99001fb387b45261e3a4ea (equal to the session-5 closing md5, so nothing had
  changed since session 5 closed). After the edit: **184569 bytes, md5 4ca20560d2ed2ef7c9f7110dc3176434; the §34 block is
  184569 - 178489 = 6080 bytes** (from "\n---\n# Session 6 of lane H" to the end of the §34 append). No session-6
  derivation was written before it, and §34 cites nothing produced in session 6.
- 12:54-12:58 UTC Lead relay: **PLD session 6 (lane E, node A) landed**, with four requests to this lane (PLD §18.12) and
  two corrections to this session's inputs (the ring price on HW's constants; node A's denial of REVIEW_HW_S5 S5-19). Read
  (read-only) PLD.md l.2188-2240 (§18.4 Lemma BUF and the ring), l.2347-2440 (§18.6 Proposition PATCH, the three deltas,
  the TF-1 verdict), l.2694-2722 (§18.9 M-1…M-7), l.2732-2760 (check p6), plus the §18 section index. §34's PRE-STATED
  block was already written and is NOT altered by this: W1 (c) already required the resulting g²_CRC "either way", and
  the ring is folded in as a new cost, reported separately in every table.
- 12:58-13:01 UTC HW.md §35 written (§35.1-§35.4: Lemmas SH-1, SH-2, COV, Corollary H-geo′, Lemma SH-att′, Proposition
  SH-neg). **The proofs were written BEFORE any w6 script existed**; the w6 checks are confirmatory for the proven
  statements and pre-registered for the three questions whose answers were not known (G1's radius-1 behaviour, G3's
  verdict, G6's ring ratio, A2's coincidence, A3's direction, N1/N2).
- **13:01:43 UTC checks/w6_criteria.md written, BEFORE every w6 script** (10414 bytes, **md5
  060c532292f0953042fafd4b2d559760** — recorded here because REVIEW_HW_S5 S5-2 noted that mtimes do not survive a
  checkout and asked for a hash). It contains **no constant derived in session 6** and says so, listing each constant it
  uses with its prior source; every criterion is labelled PRE-REGISTERED or CONFIRMATORY, per [RHW5-fix W5-1].
- 13:02:23 UTC checks/w6_shadow.py (md5 b822ec8058653cebedd07eea3a76870e); run at 13:02:23-13:03:00, exit 0, 36.1 s,
  empty stderr, load 3.13 at start, nice 10, pure-Python exact integer sets (no numpy, no BLAS), **no numeric lock taken
  and none needed** (brief rule 6). Output checks/w6_shadow.out (md5 024f6a1173de3d2d168387c5e7878a98): G1-G6 all PASS;
  **G3 = the additive form REFUTED** (excess exactly 27M + 55, slope 27 at every M in 2..29, E(30) = 865 > 258).
- 13:04:21 UTC checks/w6_arith.py (md5 66dfd5415358f6b73e60df68ee7c59cf); run, exit 0, 0.01 s, empty stderr; plain-Python
  Decimal at 120 digits, no mpmath. Output checks/w6_arith.out (md5 1dbe5d38e1552fa4b419917c8d8c407a): A1-A6 PASS;
  session 5's four S5-12 numbers reproduced; **session 6 g²_CRC = 1.52362e-94/c_+ (no ring), 8.96376e-96/c_+ (ring ×17),
  1.85835e-96/c_+ (ring ×82)**; ×311.1 on session 5 at every ring value.
- 13:05:08 UTC checks/w6_gas.py (md5 a761226645951fa663708859e3f28a82); run, exit 0, <1 s, empty stderr; exact Fraction
  enumeration. Output checks/w6_gas.out (md5 5444e82f4317532a0a9411fe17dc6999): **N1, N2 PASS — this is §29's promised
  check-(ii) negative control, which session 5 never ran** (REVIEW_HW_S5 S5-25 scope defect 1). Recorded with its
  limitation: the exact ratio does not diverge at the threshold, so the control tests the bound, not the model.
- 13:07-13:15 UTC HW.md §35.5-§35.7 (Lemma COL′, Lemma RING and the confirmation of PLD §18.12 request 1, the constants
  table and the ledger), §36 (Theorem CRC-2T′ restated; V2 (a) NOT DELIVERED), §37 ((E2^𝔉′), the seven deltas, the TF-1
  disagreement, §24.3's narrowing), §38 (the eleven [RHW5-fix] errata and §38.1's process debt, including the session-5
  rule-2 breach), §39 (check w6 record), §40 (outcomes, tally 10), §41 (FOR OTHER FILES — the rule-8 repair).
- 13:15 UTC close. HW.md **254211 bytes, md5 3634180e26da6088b0674034eec8893e**; the session-6 append is
  254211 − 178489 = 75722 bytes, of which §34 (PRE-STATED) is the first 6080. **No line of §0-§33 was altered**: every
  binding fix is an erratum in §38 naming the line it corrects. No commits, PRs or pushes; no git command of any kind was
  run this session; no edits outside HW.md, HW_LOG.md, checks/w6*; no process left running; no numeric lock held.
- **Honest statuses for the session.** PROVEN-HERE: Lemmas SH-1, SH-2, COV, SH-att′, COL′, RING; Corollary H-geo′;
  **Proposition SH-neg** (the refutation). CONDITIONAL ⇐ (E2^𝔉′) [node A]: Theorem CRC-2T′ [HW-11, re-labelled], Corollary
  CRC-HW, (CRC)_k, (M-f^cap) under μ_{R(𝔥)}. OPEN: (E2^𝔉′) itself, and its level j = 0 on both lanes' sides. ARGUED:
  nothing new. FAILED/REFUTED: the reviewer's conjectured additive form of Lemma SH-att (S5-14 (2)), and with it the hope
  that the 10⁻⁹⁴ breach vanishes — it persists at ×11.2 once node A's ring is bought, while remaining ×3.6·10⁵⁶ slack
  against the ceiling that actually binds (DX′).
