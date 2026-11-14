Reviewer model: claude-opus-5-5

# REVIEW55_LEAD — Opus 5.5 re-review of the LEAD's consolidation layer (sessions 24-25), batch C1

## PRE-STATED (written 2026-10-28T22:12:05Z UTC, before any derivation or source reading beyond the brief)

Scope (batch C1): the lead's summaries/fixes/flags only. I am NOT re-deriving worker mathematics; where a
lead bullet faithfully restates a worker file that is itself wrong, the verdict is "faithful to source"
and the source is another reviewer's job.

Targets, in order:
1. PROOF.md session-24/25 header block (locating string `**Session-24 header`) and every bullet tagged
   `[S24-fix N]`, `[S24-flag N]`, `[S24-note N]`, `[S25-fix N]`.
2. PROOF.md `[S24]` consolidation section near the end of the file.
3. HANDOFF.md in full: every critical-path item and every "withdrawn" instruction.
4. RTARGET.md §51-§54: outcome scoring in §52/§53 vs worker files; whether §54's pre-statement really
   precedes the session-25 derivations it claims to precede.
5. INTEGRATION_AUDIT.md shortfalls A1-A6.
6. SESSION24_RESULTS.md and SESSION25_RESULTS.md: >= 25 sampled factual claims (numbers, verdicts,
   file:line citations) spread across both files, each checked against its source; hit rate reported;
   then the entries the lead later corrected, to test whether each correction is itself right.
7. The tally "72 / 2 / 7 / 24 + 1": is it the right count given what these sessions record as
   proven / refuted / withdrawn?

What counts as a refutation of a lead statement (verdict REFUTED for that bullet/claim):
- R1. The cited source text does not exist at the cited file (by string search), or exists only with a
  different number, sign/direction, status word (PROVEN / CONDITIONAL / OPEN / REFUTED / WITHDRAWN), or
  quantifier/scope (e.g. "for all k" vs "at k=1"; "in the class" vs "in general").
- R2. The lead attributes a verdict to a source (worker or Codex review) that the source does not give,
  or omits a qualifier in the source that changes the verdict (e.g. CONDITIONAL reported as PROVEN).
- R3. The lead's bullet combines two objects sharing a symbol (symbol collision) that the sources keep
  distinct, so the stated comparison is between different objects.
- R4. A number quoted by the lead differs from the source number, or is quoted at a different value of
  the parameter than the source evaluated it at (stale minimum / stale quantifier).
- R5. For §54: the pre-statement is REFUTED if its file position / timestamp evidence shows it was
  written after (or edited after) the session-25 derivation outputs it claims to precede, or if its
  content quotes results of those derivations.
- R6. For the tally: REFUTED if an item recorded in these sessions as proven/refuted/withdrawn should
  move a count and does not (or moves it and should not), with the item named.
A bullet is CONFIRMED only when I located the cited source text by string and it says what the bullet
says (number, direction, status, scope). Where I cannot locate the source or cannot decide, NOT-VERIFIED
with what is missing. No git commands; file mtimes are the only timing evidence I will use and I will
say so where it matters.

Numeric checks (if any): criteria file `checks/r55l_<id>_criteria.md` written before any script; exact
rational arithmetic only.

---

## Method and evidence rules actually used

- Every cited worker/review text was located **by string** (grep) in the file as it is on disk now; line
  numbers below are current (2026-10-28 ~22:15-22:40Z). PROOF.md was being edited by the lead while I
  read it (mtime moved to 22:27:10Z), so PROOF line numbers are approximate; locating strings are exact.
- Timing evidence = file birth/mtime from `stat` (TZ=UTC). Caveat: a tool that rewrites a whole file can
  reset birth time, so a birth time is only an upper bound on when a file first existed. I use it only as
  NOT-VERIFIED-grade evidence and say so.
- No git, no scripts. The only arithmetic I did is by hand on exact quoted values (stated where used). No
  checks/ files were needed or written.
- Codex reviews (`CODEX_REVIEW_*.md`) were read as on disk now. Four new ones appeared during this sweep
  (GREENT_TG, NBG2, OLDREV, SYMBOLS; 22:20-22:25Z) and may still be in progress; where I use them I say so.
- Verdict on a lead bullet = whether the bullet states its source correctly (number, direction, status,
  scope). Where the bullet is faithful but its source (or a later Codex review) is wrong, I say "faithful
  to source" and flag the downstream problem without re-deriving the worker's mathematics.

---

# ITEM 1 — PROOF.md session-24/25 header block (locating string `**Session-24 header`)

### r55l-H0 — the header preamble ("Targets pre-stated in RTARGET.md §51 at 12:15:32 UTC ... before any session-24 derivation or worker report"; "No item of this ledger changed status category")
**Verdict: CONFIRMED for "before any worker report"; NOT-VERIFIED for "before any ... consolidation edit" (RTARGET §51's own wording).**
- Every session-24 worker/review file has birth time >= 12:33:48Z (REVIEW_PLD_S5 12:33:48, REVIEW_FLOW_S13
  12:34:09, REVIEW_SQ_S4 12:38:18, REVIEW_HW_S5 12:40:20, REVIEW_BFT_A_S8 12:45:36, NORMS_LOG 12:37:51 ...).
- But **INTEGRATION_AUDIT.md (the lead's own T51-B deliverable) has birth time 12:14:20Z, 72 s before the
  12:15:32Z stamp** that §51 says preceded "any session-24 derivation, consolidation edit or result". Its
  first-write content cannot be recovered without git (forbidden to me). Anomaly recorded, not a refutation.
- "No item of this ledger changed status category": see ITEM 7 — correct under the ledger's counting rule.
- "the session's corrections are ... listed at [S24]": the [S24] tail does not list them (it lists D1-D3
  and the critical path). Cosmetic.

### r55l-H1 — [S24-fix 1] "PROOF.md's Z_col diagnosis (l.6211-6213) is WRONG ... NORMS.md Proposition N1-8 proves ... that Z_col is the column mass of the curvature kernel, L^d·K̄ ≈ 9.7 plus (2/(d-1))K_ρ ≈ 1.5"
**Verdict: REFUTED. REVERT OUTRIGHT.**
- The PROOF text it calls wrong is now at ~l.6380 (string `Z_col ≥ the L^{d-1} = 27 crossing links`; the
  cited l.6211-6213 has drifted +167).
- **REVIEW_NORMS_S1 RN1-7c** (string `The claim that PROOF.md's diagnosis is **wrong**: itself WRONG`, l.447-460):
  "PROOF.md l.6249 reads 'Z_col ≥ the L^{d−1} = 27 crossing links ...'. That is a statement about Z_col,
  and it is **true**: for a coarse delta, Jδ_c occupies the L^{d−1} = 27 crossing fine links with value 1
  each, so the column ℓ¹ mass is ≥ 27 (measured 156.08) ... PROOF.md is not wrong about Z_col; NORMS is
  describing a different object ... **As a correction it would put a false erratum into the master
  ledger.**" Its binding fix 4 (l.737) repeats: "Reword ... as an addition, not a correction".
- The bullet also misstates NORMS itself: NORMS l.453-455 says that in the field-strength norm the
  differentiated-slot quantity is "≈ 9.7 + 1.5 ≈ 11.2 **instead of** 156" — a *replacement* object, not a
  value of Z_col (which stays 156.08). "Z_col is ... ≈ 9.7 plus ≈ 1.5" is arithmetically impossible
  (156.08 ≠ 11.2). NORMS also says the value "inherits exactly the status of (H-K) — measured, two rows,
  small tori, not certified", and the max-vs-average step needs Corollary N1-9's (uncertified) decay input;
  the bullet's "proves" drops both.
- The lead applied REVIEW_NORMS_S1 (it cites it in [S24-fix 1a]) and kept the very sentence that review's
  RN1-7c told it to reword. SESSION24_RESULTS l.1054 says so explicitly: "with Proposition N1-8's Z_col
  correction retained (it stands on its own)". No file anywhere in the lane carries RN1-7c's correction
  (grep `RN1-7c|addition, not a correction|not wrong about Z_col` over SESSION24/25, HANDOFF, PROOF,
  INTEGRATION_AUDIT, RTARGET: zero hits).
- **Correct reading:** PROOF ~l.6380's `Z_col ≥ 27 crossing links × spread` is TRUE as a statement about
  Z_col. NORMS Prop. N1-8 is an *addition*: in the field-strength norm the column mass that replaces
  Z_col is ≈ L^d·K̄ + (2/(d−1))K̄_ρ ≈ 11.2 (measured, uncertified; max-vs-average needs N1-9's decay
  input). The "this matters beyond bookkeeping: the wrong diagnosis made the per-level route look like a
  norm problem" sentence also goes: REVIEW_NORMS_S1 RN1-7b says PROOF l.6249-6251 *already* names the
  absolute-value-counting artefact.

### r55l-H2 — [S24-fix 1a] (withdrawal of the per-level no-go)
**Verdict: CONFIRMED for the withdrawal; REFUTED for its last-but-one sentence ("Proposition N1-8's correction of the Z_col diagnosis stands").**
- Faithful to REVIEW_NORMS_S1 l.42-49 and RN1-1/RN1-2/RN1-3/RN1-5: class "never defined" (3 uses, l.86/458/869),
  excludes 𝔐's Hölder leg; part (i) vacuous (l = k anchoring); n1-D a tautology — I read the quoted code
  (checks/n1_exponents.py l.86-91 as quoted at RN1-3): `emis` computed and discarded, `total = k*eA +
  k*((d-4)-eA)` ≡ k(d−4) for every eA, so the gate cannot fail; part (ii) an upper bound on an estimate
  with no lower-bound input; (O3) never tested. "The per-level route is OPEN, not refuted" is the right
  status.
- The retention sentence is REFUTED by RN1-7c (r55l-H1). REVERT that sentence.

### r55l-H3 — [S24-fix 2] (BFT clause table stale in three places)
**Verdict: CONFIRMED (faithful), with one omitted review qualifier.**
- REVIEW_BFT_A_S6 l.23 ("Theorem W0: CONFIRMED"), l.151, l.24 ("Theorem GU: CONFIRMED (0 < α < θ ...)"),
  l.181; REVIEW_BFT_A_S4 l.37 ("(CO-up) ... (ARGUED, fix T6)"); REVIEW_BFT_A_S5 l.373 ("CO-B removes 13.7's
  (SB) gap outright") — all present verbatim. BFT_A §26.1/§28.5/§28.7 confirm W0 = (G♯_0-lev0) and
  GU = (G♯-up) at m = 0, trivial background; BFT_B §30.1 (Proposition CO-use) is the source of the
  "stale in three places" sentence and of the (H-inv+) conclusion. (Res-Hölder) at m = 0 via RHT-cc:
  REVIEW_BFT_B_S9_S10 S9-7 and l.1009 CONFIRMED ("YES, closed at m = 0").
- Omitted: REVIEW_BFT_B_S9_S10 **S9-13** grades "(H-inv+) at m = 0 ... PROVEN as an implication"
  **CONFIRMED-WITH-FIX (class caveat)**: the level-wise co-closed class is one "the remainders do not
  occupy" (BFT_A [RBA2-fix] B3), and "every one of its inputs is CONFIRMED by a lane review" is "one step
  strong" (LIN0 is proven "given ... §23 (unreviewed)", BFT_A l.2683). The lead read this review
  (SESSION24_RESULTS l.1349 ff.) and did not carry S9-13 into the bullet. (Not my batch: S9-13's second
  qualifier may itself be stale — REVIEW_BFT_A_S5 reviewed BFT_A §21-§25, which contains §23, and confirmed
  CO-0R/RH/CO-upR/CO-B.) Add the class caveat; keep the rest.

### r55l-H4 — [S24-fix 3] (BFT-1 needs a weight pair)
**Verdict: CONFIRMED, except the words "for any consumer" (REFUTED as a scope extension).**
- NORMS §N7 l.642-676 gives A = L^{d−θ_w^r−2θ_A}, θ_A = min(1, θ_w^c−1), and "no solution in (0, 2]" for a
  single common θ_w. Re-derived by hand: with θ_w^c = θ_w^r = t, need t + 2min(1, t−1) > 4; for t ≥ 2 this
  is t > 2, for t < 2 it is 3t − 2 > 4 i.e. t > 2 — no t in (0, 2]. REVIEW_NORMS_S1 item 7 (l.791-793)
  CONFIRMED. "maximal curvature weight; a weaker BFT-1 is not a safer one": NORMS l.887.
- NORMS says the single-θ_w BFT-1 is "insufficient **for this route**" (l.669-671, l.883-884). "for any
  consumer" is the lead's extension (repeated in HANDOFF "Two target restatements", in RTARGET §52 T51-B
  "for anybody", and in INTEGRATION_AUDIT §7 "for anybody"). Correct reading: "insufficient for the
  composite route (Theorem N1-15's contraction)".

### r55l-H5 — [S25-fix 3] (the ceiling; "NO admissible exponent"; four exponents must be decoupled)
**Verdict: faithful to source (NBG_B §8 NB7); three source-level errors carried, and the bullet is stale against THETAW + CODEX_REVIEW_THETAW.**
- Faithful: NBG_B §8 l.428-475 — one θ_w doing three jobs at REVIEW_S22 l.392-399 (verified: l.393, l.394-395,
  l.399), BFT_A l.396/l.827, SF l.680 (θ ∈ (0, 1]) all verified at the cited lines.
- Carried errors (each an NBG_B error, not a lead misreading — but they are now in the master ledger):
  (a) "lane A proves its pair only for α ≤ θ ≤ 1 − α ≤ ¾": BFT_A l.827 reads "0 < α ≤ θ ≤ 1 − α (so α ≤ ½),
  **e.g.** α = ¼, θ ∈ [¼, ¾]" — ¾ is the α = ¼ example, the general cap is 1 − α < 1. CODEX_REVIEW_THETAW
  ("universal ceiling 3/4 -> 1-alpha (7/8 at alpha=1/8)") agrees; THETAW (T55-J) further says θ ≤ 1 − α is
  not even a proven constraint. (b) "the composite contraction **requires** θ_w^r = 3": NORMS §N7 says the
  requirement is θ_w^r > 2 at θ_A = 1 ("Delivered value θ_w^r = d − 1 = 3 ... margin exactly one power");
  3 is the delivered value. (c) "Four incompatible windows": NBG_B's table has four *windows* (lane A, SF,
  RTARGET §33, target) plus one *requirement*; the bullet swaps RTARGET §33 for the requirement.
- Stale: THETAW (T55-J, SESSION25 l.654 ff.) found the decoupled system satisfiable ("three windows on J3
  and one requirement on J2 ... cannot clash"); CODEX_REVIEW_THETAW (final, has a summary) confirms the
  reduced inequality system is feasible but grades full-target satisfiability NOT-VERIFIED and REFUTES
  THETAW's R_lin (F5: θ_w^r = 3 with residual sources violates the same target's θ_w^r ≤ 2 + θ < 3). The
  bullet's core statement — the target **as written** (one θ_w) has no admissible value — survives
  (THETAW tw1-A reproduces it). Annotate; do not revert.

### r55l-H6 — [S24-fix 4] ((BB-mix) → BFT-6)
**Verdict: CONFIRMED for the facts; REFUTED for "the single gate on layer 2's expansion".**
- REVIEW_X12 lives in the **existence** lane (`agents/ym4d-existence/REVIEW_X12.md`; the bullet gives no
  path). Its binding fix 3 (l.470-471) is quoted verbatim ("⊂ BFT-4's (BB-mix) with per-cube smallness ...
  all-order decay at k = 1 (BB-3_1) is proven but insufficient"). BFT_B_LOG l.28 lists (BB-mix) OPEN. ✓
- "single gate": REVIEW_X12 l.381 lists CE-exp^k's inputs as (i) N_μ ⇐ (N5-unif) [CONDITIONAL], (ii)
  (L-loc)_k, (iii) (FP-loc)_k [OPEN] and (N5-reg)_k [OPEN], ... (BB-mix) gates (ii) only. Correct reading:
  "a gate on layer 2's cluster expansion, alongside (FP-loc)_k, (N5-reg)_k and (N5-unif)". Same overstatement
  in HANDOFF item 7 and INTEGRATION_AUDIT §4.3.

### r55l-H7 — [S24-flag 1] ("A PROOF-owned constant conflict ... NOT resolved here": λ_min = 3.17·10⁻³ vs L0-1's 6.6·10⁻¹⁰; ×4.80·10⁶)
**Verdict: faithful to PLD; REFUTED as a live, unresolved conflict. Rewrite (also in HANDOFF "One PROOF-owned constant conflict").**
- Faithful: PLD l.2677-2685 and l.2913-2919 (×4.80·10⁶ = 3.17·10⁻³/6.6·10⁻¹⁰, check p6 D2; route (ii)'s
  a_A "does not depend on a_ret at all").
- But PROOF.md's **own** session-23 header already settled it: `[SF7-edit]` (PROOF ~l.179-180) "**λ_min ≥
  3.17·10⁻³** (was 6.6·10⁻¹⁰), N5-sf0 re-evaluated with the certified gap", adopted from REVIEW_SF_S7, whose
  verdict table (l.312) reads "3 (gap line in RW-ℓ² / N5-sf0 (b)) | ACCEPT with fix | 4.2295·10⁻³ on the
  current class; 3.1727·10⁻³ if edit 4 is adopted" and l.324 "λ_min went from 6.6·10⁻¹⁰ to 4.2·10⁻³".
  REVIEW_PLD_S3's L0-1 (l.366, l.549) says only "quote N5-sf0's gap **per PROOF l.5322-5325**" — i.e.
  whatever PROOF says — and was written against PLD at 00:33Z, before [SF7-edit]. NORMS l.746-747 already
  quotes "λ_min ≥ 3.17·10⁻³" among "the certified level-0 constants".
- **Correct reading:** not a constant conflict. [SF7-edit] adopted 3.17·10⁻³ (κ_0 = 1 scope, CS-1 class);
  the residual defect is that PROOF's **body** still prints the superseded 6.6·10⁻¹⁰ at ~l.252, 281, 2408,
  5615 (the very "everywhere a 'gap' of N5-sf0 is quoted, these are the numbers" sentence L0-1 points to),
  5792, 6176. Propagate [SF7-edit] into those lines; L0-1 then reads 3.17·10⁻³ and a_ret is unchanged.

### r55l-H8 — [S24-flag 4] ((Φ-conv) named)
**Verdict: CONFIRMED (faithful), but stale.** TENTQ l.603-608 and §5 item 2 (l.665-671): "exact at i = 1
(ratio 17/243) and ARGUED for i ≥ 2", "Every quantitative statement about the tent in this project is
CONDITIONAL on it, including §2.8 (iii) and §35.7's L^{2k−3}". Stale: YSUP Proposition YS-PHI (l.308,
l.463) later proves (Φ-conv) for the (1+|z|_∞)^{−3} profile class (RTARGET §53 records this); the flag
should say "PROVEN for the |z|^{−3} class (YSUP, unreviewed); OPEN outside it".

### r55l-H9 — [S24-flag 5] ((NEUT-box) FALSE; QN; QSBP; TQ-INT)
**Verdict: CONFIRMED in substance; two misstatements of detail.**
- Faithful: TENTQ §2.1 Prop. QN (l.127), §2.2 QSBP (l.147; bound 8Σπ_l "attained", l.182), §2.3 QFALSE (l.189),
  §2.5 TQ-INT (l.261), status table l.510-518 ("(NEUT-box) WITHDRAWN, not OPEN").
- (i) "fails **by exactly** L^{2k} (ratio exactly 9 at k = 1, 81 at k = 2)": the *proved* statement
  (l.191-201) is for D^⊥ and gives "≥ n² − 1 = L^{2k} − 1"; TENTQ's own status row (l.514) says "by
  exactly L^{2k} − 1". The "exactly 9 / 81" rows come from the post-hoc probe tq1b (l.683-699), which
  tabulates ⟨χ⁵D⟩/(n‖D‖_∞) with D, not D^⊥ (Q(D^⊥) = Q(D) − D(c_X)). Correct reading: "fails by a factor
  ≥ L^{2k} − 1 (proved); the D-version of the extremal configuration gives exactly L^{2k} (post-hoc)".
- (ii) "Route (ii)/GT-ell is dead **with it**": TENTQ l.250-252 says route (ii) is dead "**independently of
  (NEUT-box)**" — even granting (NEUT-box), GT-ell's first term already loses a power of n. The causal
  "with it" reverses the source's reasoning (also in RTARGET §53 "route (ii)/GT-ell dies").

### r55l-H10 — [S24-flag 2a] (naming hazard is systemic: four ε_*, two θ_0 "whose collision caused the 52-decade τ_♭ error (TAUFLAT §1)", five ε_1, four live ε_1 values, three η_1)
**Verdict: CONFIRMED for the ε_*, ε_1, η_1 facts; REFUTED for the θ_0 clause as written; counts stale.**
- Verified: EPS1_SWEEP §1 (l.137-160: "at least FIVE"; BFT_B's O(1) formula in RLARGE's words) and §1.1
  (l.165-175: 1.27·10⁻³⁹ at SF l.2837 "quoted as current by NORMS l.746" — NORMS l.746 checked —, 9.52·10⁻⁴⁰,
  8.95·10⁻⁴⁰, 6.7·10⁻⁴⁰); ARS_FIX §1 (l.195-221: three η_1; PLD's eight lines l.42, 772, 1010, 1071, 1077,
  1096, 1204, 1259; SQ l.1679 bound variable — checked; REVIEW_PLD_S3 l.463 "Today PLD and RLARGE use
  different η_1" — checked); ε_1 < 78/N (ARS_FIX l.406). Four ε_* are in **EPSSTAR §6.1** (l.408-418), not
  "§5" (mis-cite, also in [S24-flag 2]).
- θ_0 clause: (a) **currency**: 52.077 decades is the ratio of **η_♭** (TAUFLAT §2.2 l.192-197: η_♭ at
  entry A 4.20662·10⁻³⁶ vs entry B 3.52310·10⁻⁸⁸). Since η_♭ = c_♭τ_♭²/C′², the τ_♭ ratio is half the log:
  52.077008938/2 = 26.0385 decades (hand arithmetic on TAUFLAT's exact figure; CODEX_REVIEW_DECADES "52
  decades described as tau_flat: REFUTED ... tau_flat log-ratio [26.038504469, 26.038504470]" agrees — I
  agree with Codex). (b) **cause, by the cited section**: TAUFLAT §1 l.144-147 says the conflict "is not a
  definitional identity and it is **not a symbol confusion**"; §2.1 l.180-183: "It is not an arithmetic
  error in either item. It is a **stale evaluation of a minimum**". Only TAUFLAT §6.1 l.555 / §6 item 6
  (l.634-637) calls the unexecuted θ_0 rename "the root cause" in the sense that the collision "makes [the
  error] easy". Correct reading: "two (now four, SYMBOLS) distinct θ_0; a stale minimum (τ_♭ = τ_R
  evaluated at C_D ≤ 455.28, after S4-16 made C_D ≈ 4.76·10¹⁵) produced a 52-decade error in η_♭
  (26 decades in τ_♭); the uncollided names would have made it harder to make (TAUFLAT §6)".
- Stale counts: SYMBOLS.md (T55-C) found θ_0 = 4, ε_1 = 6 (incl. ε_1^gas), C_1 ≥ 13, c_1 ≥ 11, κ ≥ 5.

### r55l-H11 — [S24-flag 6] (original) + [S25-fix 4] (REFUTED IN FULL) + [S25-fix 1] (1551× → 201.029×)
**Verdict: [S25-fix 4] CONFIRMED for every grep-checkable fact; its "+63.619 decades at every live ε_1" REFUTED as an established clearance (Codex DECADES F2, which I agree with); [S25-fix 1] CONFIRMED with a mis-cite.**
- I re-ran the greps: `a_RS` in RLARGE.md at l.830, 1020, 1023 (twice), 1024, 1247 — five **lines**, six
  occurrences — all after "# Appendix A. Frozen and one-step content of v1" (l.824); zero hits in HIST, HW,
  PLD, SQ, BFT_A, BFT_B, NORMS, LINEAR_PACKAGE. l.545 "Constants (C_ℓ, B_0, E_0, a, n_♯) are the same at every
  level". l.513-514 "Not hypotheses of RLF-step v3: ... (PLD)_k (i)-(ii), (PLD-q)_k ...; RS-joint and the
  greedy joint pricing (§3.5)". Lemma RS (R1)-(R5) (l.973-984) contain no a_RS. l.832 "a_♯, c_RS = 5⁴ and
  n_♯ := ⌊4/(a_♯β_-)⌋ are superseded by §3.5 and §5.2 (a = min{θa_bad, a_A})". ARS_FIX cites "§3.5" at l.294
  and l.788 (both quoting l.832), so REVIEW_ARS_EPS_S1 l.130's "Neither file cites §3.5 ... (grep: zero hits)"
  is literally false — the lead's correction is right (that review itself concedes ARS_FIX "cites only
  through that pointer").
- The clearance number: ARS_BIND A7 (l.336) computes a = θc_prε_1² = 1.040415·10⁻⁸⁶ **with θ = 1/24** and
  a_A dropped; I checked: (6.7·10⁻⁴⁰)²/(640·53²) = 4.489·10⁻⁷⁹/1.79776·10⁶ = 2.497·10⁻⁸⁵, ÷24 = 1.0404·10⁻⁸⁶.
  RLARGE l.88-94 / l.187-190 only constrain θ by max{6θ, 24θ}(1+2Rg_K²) < 1 (θ < 1/24 strictly) and set
  a = min{θa_bad, a_A}. So 1.040·10⁻⁸⁶ is the supremum over admissible θ, not a value the route is shown to
  attain, and a_A is not shown ≥ θa_bad there; C_Ω = 1 is frozen. CODEX_REVIEW_DECADES F2 / table row
  "+63.619 'live exponent clears DXprime' | REFUTED ... only an optimistic UPPER benchmark" — **I agree**:
  the figure is a CONDITIONAL benchmark. (The structural conclusion — a_RS has no live consumer, (C2)
  vacuous — does not depend on it.) Also "+63.619 **at every** live ε_1" is the minimum of a range (ARS_BIND
  A10: +63.62 → +64.17).
- [S25-fix 1]: 1551.148/(625/81) = 1551.148/7.716049 = 201.03 (hand check); KN_ADOPT §3.2 l.321-344 and the
  §6 table l.443, l.462 carry 201.029 / 452.315; CODEX_REVIEW_KN F8 and CODEX_REVIEW_DECADES both CONFIRM
  201.029 and 452.315 (exact 21233664/105625 and 47775744/105625). The bullet cites "**KN_ADOPT §5**" for the
  refutation; §5 is "what the adoption does NOT buy" — the 201× rebuild is **§3.2**. "a_RS's STATUS is
  unchanged — CONDITIONAL on (PLD)_k (i)" is KN_ADOPT §5 (l.395-401) and CODEX_REVIEW_KN F7 ("Effective
  estimate remains CONDITIONAL on (PLD)_k(i)") ✓.
- Layout hazard: the struck original is retained inline and still ends with live-sounding bold text
  ("**OWNER DECISION, not a defect ... Either way l.618 needs editing.**"), which [S25-fix 4] refutes
  (l.618 TRUE as written). Mark the retained paragraph struck through to its end.

### r55l-H12 — [S24-flag 2] (four ε_*)
**Verdict: CONFIRMED (faithful), mis-cited section.** EPSSTAR §6.1 l.408-418 (not "§5") lists the four;
the "false comparison" the lead caused is EPSSTAR l.420-423 ("My brief's comparator ... is symbol 2, not
symbol 1").

### r55l-H13 — [S24-flag 3] (52-decade inconsistency inside REVIEW_SQ_S4; "EPSSTAR §6.6, ARGUED"; adjudication commissioned)
**Verdict: CONFIRMED (faithful at the time); stale.** TAUFLAT reproduces every number (window C_D ≤
455.283301, l.175-177; 52.077 decades, l.197; 9.707-decade shortfall, l.214-216; floor C_T ≥ 4.4·10¹², l.233).
"C_T ≲ 3.5e10" came from EPSSTAR's figure (3.5-6.3·10¹⁰); TAUFLAT [TF1-E] (l.218-233) corrects EPSSTAR by √10
to 1.98-3.56·10¹⁰ — the lead's upper end survives by coincidence. Stale: the bullet still says "ARGUED" and
"Adjudication commissioned"; TAUFLAT returned **CONFIRMED** and **LOAD-BEARING — YES** (l.335), "a status
regression, not a new death" (l.348). Update the bullet with the verdict.
  *Addendum to r55l-H11 (support for the Codex reading from RLARGE's own text):* RLARGE l.88-92 states
  a := min{θa_bad, a_A} with "If a_A < θa_bad, θ is lowered to a_A/a_bad", and concludes "hence **a ≲
  10⁻⁸⁶**" — an upper bound — and gives a_bad ≈ 10⁻⁹⁴ "via (AE)". So the +63.6-decade figure is RLARGE's
  own optimistic end.

### r55l-H14 — [S24-note 2] ("(GAP-Z) ... IS BFT-5's input (1) (G♯_0-field) ... ONE obstruction ... must not count them twice") + [S25-fix 2] ("REFUTED ... THREE obstructions") + [S25-fix 5] (NBG_ADJ: "TWO")
**Verdict: [S24-note 2] faithful to BFT_B §43.3 item 4 / §41.6 (iii) l.4596 but its claim is UNESTABLISHED; [S25-fix 2] faithful to NBG_B §6 but its argument is invalid; [S25-fix 5] faithful to NBG_ADJ but its count is UNESTABLISHED. Net: all three counts (ONE / THREE / TWO) should be REVERTED to "three named requirements, zero established identifications, independence count NOT-VERIFIED".**
- Sources verified: BFT_B l.4334 ("(GAP-Z). The background analogue of the package constant M of LINEAR_PACKAGE
  Theorem 4.2′ ... with **no decay claimed**"), l.4590, l.4594-4596 ("So the nontrivial background and BFT-5 are
  not two obstructions. They are one."; chain "4.2′'s M ⟹ W ⟹ Y, YH ⟹ W0, GU ⟹ LIN0"); RTARGET l.654
  ("(G♯_0-field) not attempted"); PROOF "(G♯_0-field): not attempted" now at **~l.3641** (the [S25-fix 5] "l.3614"
  has itself drifted +27); NBG_ADJ l.281, l.329 (SIX work items), l.387 ("share no node"), l.440 ("two
  independent derivations ... FALSE").
- **CODEX_REVIEW_GAPZ** (final; ends with summary table) is the decisive approved-setting input:
  F3 "Proof status is not a non-implication proof" — REFUTED ("'P has a proof' and 'Q has not been attempted'
  are compatible with P = Q, P ⇒ Q, Q ⇒ P, or neither"); F2 "(GAP-Z)|_{Z=1} is not identified with Theorem
  4.2′'s M" (M bounds response kernels, not the composite Hessian inverse; scalar witness F_a = a(x−b)²/2,
  a = 1/n: dx/db = 1 for all n while F_xx⁻¹ = n); F5 the four mismatches "do not establish four independent
  barriers" (explicit ℤ⁴ counterexample H = 9I − Σ(S_μ+S_μ*) to the norm/decay row); F4 the "convenient
  TWO" reverses a reduction; and the **count ruling**: "retain THREE named, unresolved requirements and
  ZERO established equivalence identifications ... The number of logically independent analytic
  obstructions is NOT-VERIFIED ... the proposed TWO reconciliation is not established either", with all six
  arrows "NOT-VERIFIED", "not six proved failures".
- I agree with Codex on F2-F5 and the count ruling, on the logic alone: the [S25-fix 2] three-line
  argument is literally "P PROVEN, Q 'not attempted', so P ≠ Q", which is invalid (F3), and its premise
  "(GAP-Z)|_{Z=1} is M" is a vocabulary identification (F2's witness shows a response bound need not bound
  an inverse). NBG_ADJ's "TWO ... no pairwise implication" rests on NBG_B §6.3's six "failed" arrows, which
  are unproved arrows, not proved non-implications. And [S24-note 2]'s "IS" rests on the same
  vocabulary identification in the other direction (BFT_B l.4594 "lane A's U = 1 package at Z ≠ 1").
- The lead's SESSION25 CX-1 summary (l.827-879) reports F1-F7 but **omits the count ruling, F8 (NBG_A's
  background log-derivative identity omits the ad_X/(e^{ad_X}−1) factor), F9 (NBG_A's relaxed threshold
  θ_w^r > 1 is false for 7/4 < θ_w^c < 2), F10 and F12**, so PROOF's header was never corrected for them
  (the lead's earlier §PROVENANCE section (in git history) admits some Codex files were read while still being written).
- [S25-fix 5]'s "Highest leverage: (HESS-rel)" is superseded: HESSREL (T55-L) refutes (HESS-rel), and Codex
  GAPZ F7 refutes the literal form (gauge covariance is conjugacy; δ := ‖H_0⁻¹(H_Z − H_0)‖ < 1 is the needed
  condition, witness H_0 = diag(1, n), E = diag(−1, 0)), leaving only a CONDITIONAL framed version.
- What survives: Z = 1 is an admissible specialization (NBG_ADJ; Codex F1 CONFIRMED); the phrase collision
  "lane A's U = 1 package" is real (Codex F10 CONFIRMED for the collision).
- **Correct reading for the ledger:** "(N-bg), (GAP-Z), (G♯_0-field): three named, unresolved requirements;
  no equivalence or non-implication between any two is established (CODEX_REVIEW_GAPZ); do not count them
  as one, two or three independent obstructions." Revert the ONE ([S24-note 2]), the THREE ([S25-fix 2])
  and the TWO ([S25-fix 5]).

### r55l-H15 — [S24-note 3] ("(CovLift)'s non-residual g_Z clause at θ > 0 is FALSE (BFT_B §41, Proposition GZ-FALSE, PROVEN) ... The search for a better lift is foreclosed.")
**Verdict: REFUTED by omission (status changed by dropping a qualifier); mis-cited section.**
- GZ-FALSE is BFT_B **§42.2** (l.4626), not §41. Its claim is false "with the **fixed** representative
  G_l := F_l(Z)" (l.4628). §42.3 Theorem Cg-nr (l.4639-4657) then shows the forced reading is an infimum
  over representatives, and "(C_g-θ) for the non-residual components of g_Z, for every 0 ≤ θ < 1, ⟸
  (CURV-dec)" — PROVEN as an implication; status entered: "**not closed** ... its statement as written is
  FALSE ... the correct statement is the infimum form". BFT_B's own §43.3 item 2: "FALSE as written and
  **reduces to one named item (CURV-dec)**".
- Correct reading: "the fixed-representative clause is FALSE at every θ > 0 (GZ-FALSE, §42.2); the
  infimum-form clause reduces to (CURV-dec), OPEN (Cg-nr, §42.3)". As written, the bullet (and RTARGET §53
  "FALSE for every lift"; PROOF [S24] tail) makes a live, reduced item look dead.

### r55l-H16 — [S24-note 4] (BNA-F4 is about log Z, not F_Z; BFT_B §42, Lemma CONJ)
**Verdict: CONFIRMED (faithful), mis-cited section.** Lemma CONJ is BFT_B **§41.1** (l.4517), not §42. The
reading (l.4529) and the FOR OTHER FILES note to SF (l.4772) match. "f_j ≤ C_Nf_k ... on all of 𝒦(ε)" is
Theorem N2's (N2-0)(a) (§22), which §41.1 cites. "The obstruction everyone priced was the wrong quantity"
slightly overstates l.4772, which keeps SF's wall "at the steps where an analytic estimate needs a
connection".

### r55l-H17 — [S24-note] ((CO-fun)'s residue = the (GE-T) functional)
**Verdict: CONFIRMED.** BFT_B §36.5 (iv) (l.4209): "Proposition COF-res shows the tent functional is
exactly what (CO-fun)'s residue is, so the two refutations are the same fact seen twice".

---

# ITEM 2 — PROOF.md `[S24]` consolidation section at the end of the file (locating string `# [S24] Session-24 consolidation`)

The section was written during session 24 and was annotated in session 25 at exactly one place (the
(GAP-Z) parenthesis). It now contradicts the header block above it in at least six places.

| id | statement in [S24] (locating string) | verdict | source / correct reading |
|---|---|---|---|
| r55l-T1 | "the main-path tally is unchanged at 72 / 2 / 7 / 24 + 1" | CONFIRMED (counting rule) | ITEM 7 |
| r55l-T2 | "D1 (one slice, S_E). CONFIRMED by REVIEW_BFT_A_S8 ... ψ_u is computable exactly" | CONFIRMED | REVIEW_BFT_A_S8 l.45: φ_1 = −1/432, φ_2 = −17/104976, ratio 17/243, ψ_u = −65/26244 at k = 2 |
| r55l-T3 | "**D2** ... **Upgraded from a judgement to a theorem** by NORMS.md §N5. No future session should attempt to repair the per-level induction in any norm." | **REFUTED — REVERT** | Withdrawn by REVIEW_NORMS_S1 (no-go NOT ESTABLISHED) and by the lead's own [S24-fix 1a] and HANDOFF withdrawn item 2. Correct: "D2 remains a judgement; the per-level route is OPEN, not refuted." |
| r55l-T4 | "D3 ... uniformity problem is now solved at the trivial background (Theorem N1-15, A_soft = 1/3, conditional on (N-loc) alone after Theorem NQ-1); the magnitude problem is coth⁴(m₁/2)-dominated, some 10³² above the C_♭ term" | CONFIRMED with scope missing | REVIEW_NORMS_S1: N1-15 CONFIRMED "at narrower scope": **d = 4 only**, linearised, trivial background, and 𝔚 + 13.5𝔖 ≳ 10⁷ "not O(1)". "10³²": NORMS l.760-762, but the binding term itself ranges 10²⁰-10⁴² with m_1 (l.760, l.900); 10³² holds at one m_1 only. |
| r55l-T5 | item 1 "(CRC-1)/(LI^U). Dissolved as a wall ... induction on the number of constrained pairs, not a cluster expansion" | CONFIRMED (spot-checked) | REVIEW_HW_S5 (SESSION24 l.203-218 reproduces it; "bestiary", Target V2(a) never delivered) |
| r55l-T6 | item 2 "The chain waits on **(CEM-1)/(CEM-2)** and the level-0 clause (0a)/(0b)" | **REFUTED (stale)** | PLD §19 Theorem W-FREE (l.3118, l.3366, l.3601): "(CEM-2) ... is NOT an ingredient of (CEM^{COL})", residual **(BCH-1)**; (CEM-1)'s (b)+(c) became one statement (Theorem AT). RTARGET §53 (iii) already records W-FREE. |
| r55l-T7 | item 3 "C_T ≲ 1e13 ... at q = 8 ... C_T ≥ 1.27e14 ... **At q ≈ 30 it is under** ... (CONST-T) reduces to expanding C_1 and C_V" | faithful to CONST_T (l.381, l.389); **REFUTED as current** | EPSSTAR Theorem ES-1 closed A_cγ_c constant-free and gives **C_T(q = 12) = 5.288·10¹², q_min = 11** (EPSSTAR l.549-555) — the same [S24] section's next paragraph lists "A_cγ_c ... PROVEN". QFIX/CODEX_REVIEW_QFIX (session 25) further dispute q's role. |
| r55l-T8 | item 4 "(H-inv+) and (Res-Hölder) closed at m = 0 on the trivial background" | CONFIRMED with S9-13 class caveat | r55l-H3 |
| r55l-T9 | item 4 "**Theorem NCE gives (NC-Γ) for Γ_E at every critical point of 𝔉_k, uniformly in k and T**" | **REFUTED — REVERT** | REVIEW_BFT_B_S9_S10 (l.999 "WRONG \| Corollary COF-crit (k-uniformity does not follow ...; ≈ 25(k−1) at best)"; l.520 the L^{θ(k−1)} gap). The same [S24] section's follow-on paragraph says "Theorem NCE's k-uniformity ... REFUTED". |
| r55l-T10 | item 4 "Off the critical set the whole obstruction is **one scalar per level-k box**, the compensation charge ⟨χ⁵_X D(S)⟩ ((TENT-Q) / (NEUT-box))" | **REFUTED (stale)** | TENTQ Theorem TQ-INT (l.261, l.518): "the box charges are **eliminated**"; (NEUT-box) WITHDRAWN (l.517). |
| r55l-T11 | item 4 "**BFT-0/1/2 turns on (N1) plus (CovLift)'s non-residual g_Z at θ > 0**" | **REFUTED (stale)** | BFT_B §43.3 (l.4752-4757): "(N1) is no longer the obstruction"; the g_Z clause "is FALSE as written and reduces to one named item (CURV-dec)"; "The single remaining obstruction is (GAP-Z)". (And see r55l-H14 on (GAP-Z)'s status.) |
| r55l-T12 | item 4 "BFT-5 has a statement, (BFT-5_E), OPEN with inputs named" | CONFIRMED | BFT_B l.3851 |
| r55l-T13 | item 5 FLOW "(T-a1-M) and (T-b) are ONE wall ... (T-c) decides" | CONFIRMED | REVIEW_FLOW_S13 l.689, l.707-715, l.199 |
| r55l-T14 | "LINEAR_PACKAGE §10 ... 6-7 paper-scale tasks and 15-18 session-scale"; "Layer 2 ... 9 HYPOTHESIS-NEW and 12 OPEN" | CONFIRMED | LINEAR_PACKAGE l.488; EXISTENCE.md l.4846-4847 (session-12 tally) |
| r55l-T15 | follow-on: "(N-Q), (Res-Hölder) at m = 0, (CO-fun) under (CC-0), the torus Hodge bound, the lattice Green's-function estimate, A_cγ_c, Σ_X Q_X = 0 and (Φ-conv) for one profile class are PROVEN" | PARTLY REFUTED | (N-Q): CONFIRMED by REVIEW_NQ_S1. (Res-Hölder), (CO-fun) under (CC-0): CONFIRMED by REVIEW_BFT_B_S9_S10 (COFUN adds: the **(cc)** class D1 uses is FALSE as stated). **Green's-function estimate: GREENT l.682-689 itself says its constants are "COMPUTED upper sum, not closed form" and "the t-quadrature is an estimate of an upper sum, not a proof of one"**; CODEX_REVIEW_GREENT_TG F4 (possibly still being written): constants NOT-VERIFIED, certification REFUTED. Hodge bound, A_cγ_c, Σ_X Q_X = 0, (Φ-conv)-for-a-class: PROVEN-HERE but unreviewed — the paragraph does not say so. |
| r55l-T16 | follow-on: "... (CovLift)'s θ > 0 clause, (TENT-osc), HW's lever (b) and **RLARGE l.618** are REFUTED or struck" | **PARTLY REFUTED — REVERT the RLARGE l.618 item** | RLARGE l.618: [S25-fix 4] says "TRUE as written" — the tail was never annotated. (TENT-osc): YSUP's verdict is "FALSE, by exactly n² — **CONDITIONAL on the profile input** (BFT_A §38.7 / Theorem YH)" (YSUP l.260, status table) — the qualifier is dropped. (CovLift): see r55l-H15 (reduced to (CURV-dec), not dead). HW lever (b): CONFIRMED (HW §35.4 Proposition SH-neg, l.1903-1908). |
| r55l-T17 | follow-on: "(GAP-Z) IS BFT-5's (G♯_0-field) — **REFUTED in session 25, see [S25-fix 2]: they are three obstructions, not one**" | **REFUTED — REVERT** | The annotation itself is superseded twice: [S25-fix 5] says TWO, and CODEX_REVIEW_GAPZ says no count is established (r55l-H14). |
| r55l-T18 | follow-on: "symbol collisions (four ε_*, two θ_0, five ε_1, three η_1 ...)" | stale | SYMBOLS.md: θ_0 = 4, ε_1 = 6 (incl. ε_1^gas), plus C_1 ≥ 13, c_1 ≥ 11, κ ≥ 5 |
| r55l-T19 | follow-on: "**a_RS is found to bind TODAY**, with a repair worth 82 decades blocked only by a prior either/or" | **REFUTED — REVERT** | [S25-fix 4] / ARS_BIND (a_RS has no live consumer). The "82 decades" as a programme gain is REFUTED by CODEX_REVIEW_DECADES ("82/92 as a proved programme gain \| REFUTED \| discarded joint-price currency") and by REVIEW_ARS_EPS_S1 RA-F2. |
| r55l-T20 | "**The per-level route is dead by theorem rather than by label**, and the composite route has a proven contraction at 1/3 uniformly in k" | first half **REFUTED — REVERT**; second half CONFIRMED with scope | per-level: as r55l-T3. Composite: N1-15 CONFIRMED at d = 4, linearised, trivial background (REVIEW_NORMS_S1); THETAW calls 1/3 "the data-only rate", and CODEX_REVIEW_THETAW F5 shows the residual-source version at θ_w^r = 3 is empty — keep "for the data-only linear chain". |
| r55l-T21 | "One parameter fixed incidentally at q = 8 was costing seven orders of magnitude" | CONFIRMED | CONST_T l.433 "one exponent costs a factor 3.5·10⁷" |

---

# ITEM 3 — HANDOFF.md (18.9 KB; read in full)

**Global finding: HANDOFF.md is a session-24 document.** Its only session-25 edit is the provenance
banner (birth 12:03:19Z = checkout; last write 22:11:08Z = banner). Its reading list ("Read these, in this
order") never mentions SESSION25_RESULTS.md, RTARGET §53-§54, or any of the 19 session-25 worker files or
12 Codex reviews. Every item below that session 25 touched is therefore stale even where it was right on
the day.

| id | HANDOFF statement (locating string) | verdict | source / correct reading |
|---|---|---|---|
| r55l-F1 | "**UNREVIEWED** ... HW session 6, PLD session 6, **BFT_B sessions 9 and 10, NORMS.md, NQ_CHECK.md**, CONST_T.md, STAR_CONST.md. Every one is from session 24 and **none has been audited**." | **REFUTED (stale, self-contradicting)** | REVIEW_BFT_B_S9_S10 (born 14:26Z), REVIEW_NORMS_S1 (14:10Z), REVIEW_NQ_S1 (14:05Z) exist and HANDOFF itself cites the first two (withdrawn item 2; critical-path item 5). RTARGET §53's own list of what remains unreviewed is the right one (and is itself longer: 14 files). |
| r55l-F2 | "THE REVIEW DEBT IS PAID ... No headline was refuted outright; three were narrowed ..." | CONFIRMED for the five named reviews | RTARGET §52 T51-A; SESSION24 l.432 ff. |
| r55l-F3 | WITHDRAWN 1: "'Lower g_0 and recheck the SF thresholds.' WITHDRAWN ... binding ceiling is g_0² ≲ 2.5e-152/C_Ω, **with slack ×3.59e56**" | CONFIRMED with a dropped quantifier | REVIEW_HW_S5 l.54, l.318-319, l.552 ("NARROWED ... does not bind ... for c_+ ≲ 2·10⁵⁵C_Ω"); ×3.59·10⁵⁶ is HW §35.7 (iii) (HW l.2183) "**at c_+ = 1** (w6 A5)", proviso c_+ ≲ 6.1·10⁵⁷, C_Ω frozen at 1. Say "at c_+ = 1, C_Ω = 1". |
| r55l-F4 | WITHDRAWN 2 (per-level no-go withdrawn; route OPEN) | CONFIRMED | REVIEW_NORMS_S1 l.42-49, RN1-1/2/3/5 (r55l-H2) |
| r55l-F5 | WITHDRAWN 3 "(CO-fun) and the (GE-T) refutation as two items. BFT_B §36.5: they are the same functional." | CONFIRMED | BFT_B l.4209 |
| r55l-F6 | WITHDRAWN 4 "(CO-0), (CO-up) or (SB) as open" | CONFIRMED | r55l-H3 |
| r55l-F7 | WITHDRAWN 5 thin-cluster escape dead; finite funnel truncation leaves a level-independent remainder | NOT-VERIFIED (not re-checked; outside the sampled set) | — |
| r55l-F8 | CP 1 "T-UNIFORMITY, not (N-loc) ... Corollary NL-4: Theorem N1-15 is UNCONDITIONAL ... at FIXED coarse side ... what is actually open is uniformity in T, **which layer 2 needs**" | faithful to NLOC (NL-4 "PROVEN-HERE given (J1)-(J4)", all four imported PROVEN inputs, NLOC l.135-146, l.342); **stale** | TUNIF (T55-F) claims T-UNIF PROVEN and that "layer 2 needs T-uniform constants" is "NOT traced to any consumer" (ARGUED); CODEX_REVIEW_TUNIF: TU-0..TU-3 CONFIRMED (with a periodicity hypothesis), **full T-UNIF NOT-VERIFIED/CONDITIONAL**, "Do not propagate 'T-UNIF / N-loc closed'". |
| r55l-F9 | CP 1 "GREENT.md **PROVES** the lattice Green's-function estimate with explicit R-uniform constants (C₁ = 54, C₂ = 1703 ...)" | **REFUTED as stated** | GREENT l.683-689: constants are "**COMPUTED upper sum**, not closed form"; CODEX_REVIEW_GREENT_TG F4. Numbers themselves match GREENT l.309, l.584-585, l.411 (𝒮_T = 2.514·10⁸) and l.413 (gain 1.11·10²⁰). |
| r55l-F10 | CP 2 "The nontrivial background: **(N1) + (CovLift)'s non-residual g_Z at θ > 0**. Now the biggest BFT obstruction" | **REFUTED (stale)** | BFT_B §43.3 items 1-4 (r55l-T11); and the lead's own [S24-note 3] calls that clause FALSE. |
| r55l-F11 | CP 3 "(CEM-1) and (CEM-2) ... The whole HW/node-A chain reduces to these. (CEM-2) is a decoupling across one R-free ring ..." | **REFUTED (stale)** | PLD §19 Theorem W-FREE (r55l-T6). HANDOFF was edited later the same session to record PLD session 7's ring price (disagreement 1) but not W-FREE. |
| r55l-F12 | CP 4 "(CONST-T) ... at q ≈ 30 it is under ... **STAR_CONST.md was commissioned for exactly this; if it has landed, read it.**" | **REFUTED (stale)** | STAR_CONST landed 13:54Z and EPSSTAR delivered C_T(12) = 5.288·10¹², q_min = 11 (r55l-T7). "q = 8 is the worst admissible choice (cost 3.5e7)": CONFIRMED (CONST_T l.433). |
| r55l-F13 | CP 5 "Theorem NCE (i) is NOT k-uniform ... ≈ 25(k-1) ... (SPD)/(W2), OPEN" | CONFIRMED | REVIEW_BFT_B_S9_S10 l.73, l.520, l.999 |
| r55l-F14 | CP 5 "Below it: the compensation charge ⟨χ⁵_X D(S)⟩ ((TENT-Q)/(NEUT-box)), one scalar per level-k box; and (Y-sup^loc) ... (GT-sup) may be a spike-support question after all" | **REFUTED (stale)** | TENTQ TQ-INT eliminates the box charges; (NEUT-box) WITHDRAWN; YSUP: (Y-sup^loc) "FALSE by exactly n" (status table); TUNIF: "(GT-sup) is a k-counting question", the record "conflated two propositions". |
| r55l-F15 | CP 6 FLOW | CONFIRMED | r55l-T13 |
| r55l-F16 | CP 7 "(BB-mix) ... the **single gate** on layer 2's entire cluster expansion" | **REFUTED (overstated)** | r55l-H6 |
| r55l-F17 | CP 8 "(MS-Sob) and (SQ-dev) BACK ON THE CRITICAL PATH ... C_D ≤ 455.28 ... 9.707 decades ... (C) lower ε_1 ... OWNER-GATED and now under audit (EPS1_SWEEP.md) ... (A) sharpening C_T is DEAD (0.080 decades of room)" | CONFIRMED (faithful to TAUFLAT); stale on (C) | TAUFLAT l.175-177, l.214-216, l.335, §4; "0.080" CONFIRMED by CODEX_REVIEW_DECADES ("0.080 -> 0.578 room \| CONFIRMED"). Stale: (C) was executed as T55-B (EPS1_EXEC), and §54 records the owner's "execute, do not surface". |
| r55l-F18 | "Two target restatements: BFT-1 needs a WEIGHT PAIR ... **no solution in (0, 2] for any consumer** ... Promote (BB-mix) to BFT-6." | **REFUTED in scope; stale** | "for any consumer" (r55l-H4). Superseded by NBG_B NB7 / THETAW F1 restatement (θ_w^c := 2, θ_A := 1 pinned; θ_w^r a parameter > 2; (α, θ) universal; BFT-1 split 1a/1b/1c) and CODEX_REVIEW_THETAW (reduced system feasible, full target NOT-VERIFIED, R_lin REFUTED). The "pair" is not the whole restatement. |
| r55l-F19 | "Two cross-lane disagreements: 1. ... SETTLED by PLD session 7 (p7 F1) ... ×82 stands" | CONFIRMED (spot) | SESSION24 l.1268 ff. (PLD §19) |
| r55l-F20 | "**One PROOF-owned constant conflict** ... λ_min = 3.17e-3 against ... L0-1 (6.6e-10) ... For SF/PROOF to settle." | **REFUTED** | r55l-H7: settled by PROOF's own [SF7-edit]; body lines un-propagated. |
| r55l-F21 | "The pattern worth carrying forward": q = 8 (3.5e7); single θ_w; "a ×6561 shadow constant that was really ×81"; (E1)/(E2); allowance currency | CONFIRMED (with a gloss) | CONST_T l.433; NORMS §N7; HW l.1814-1816 ("replaces the factor 6561 by **81**") — an improved bound, not a discovery that it "was really" 81. |
| r55l-F22 | Process rules | not reviewed (owner rules, not claims) | — |

---

# ITEM 4 — RTARGET.md §51-§54 (locating strings `## 51.`, `## 52.`, `## 53.`, `## §54.`)

**Timing evidence.** RTARGET.md: birth 12:03:19Z (= worktree checkout; the file predates the session),
**mtime 21:02:17Z — exactly the §54 stamp**. So §54 was the last write to RTARGET.md and nothing in §51-§54
was edited after it (in particular §52/§53 were never annotated with any session-25 reversal).

### r55l-R1 — §51 "Written 2026-10-28 12:15:32 UTC, before any session-24 derivation, consolidation edit or result of any session-24 worker"
**Verdict: NOT-VERIFIED.** All worker/review files born ≥ 12:33:48Z (consistent), but INTEGRATION_AUDIT.md —
the lead's own T51-B output — was born 12:14:20Z, 72 s **before** the stamp. Whether its first write held
any finding cannot be determined without git.

### r55l-R2 — §52 scoring, target by target (against the worker files as they now stand)
| target | §52 score | verdict on the scoring | evidence |
|---|---|---|---|
| T51-A | PASS | CONFIRMED | five reviews exist; REVIEW_BFT_A_S8 l.45 (φ_1 = −1/432, φ_2 = −17/104976, 17/243) |
| T51-B | PASS ("A1 reinstated ... **for anybody**"; "A6 (PROOF.md's wrong Z_col diagnosis) added") | **REFUTED → PARTIAL** | A6 is false (RN1-7c, r55l-H1) and is not a target shortfall at all; A1′'s "for anybody" is not traced to any consumer requirement — NORMS says "insufficient for this route" — so §51's own PASS criterion ("each shortfall it names is traced to a quoted consumer requirement and a quoted clause") is not met for A1′ or A6. A4, A5 meet it. |
| T51-C | "PASS, with a sharper outcome than asked ... per-level route is a **no-go** ... weight-invariance half **proven** ... D2 upgraded from a judgement to a theorem" | **REFUTED → PARTIAL** | REVIEW_NORMS_S1: no-go NOT ESTABLISHED; n1-D tautology; "≈ 10³ gain per level" WRONG as stated (𝔠_ax² ≳ 29.9, 𝔠_vol unevaluated: A_per ≤ 32–49 at 𝔠_vol = 1, no gain at 𝒦's near-field rate, l.50-56). What T51-C asked for (A in a curvature-adapted norm and the θ_w-range) *was* delivered (NORMS §N7, CONFIRMED). §53 records the no-go withdrawal; §52 is not annotated. |
| T51-D | "PASS on reporting; 0 OPEN items closed" | CONFIRMED (spot) | PLD l.2550 "(this is a consolidation, not a discharge)" |
| T51-E | "PASS on four of five ... BFT-5 has a statement, (BFT-5_E), **with clause (c) PROVEN** ... Session 10 ... showed **(GT-sup) is not a spike-support question**, completing **Theorem NCE ... uniformly in k and T**" | **REFUTED in three clauses** | REVIEW_BFT_B_S9_S10 S9-18 (l.384): "(BFT-5_E) clause (c) 'PROVEN (Proposition NCR)': **WRONG at the stated scope**"; l.90/l.1000: "(GT-sup) is not a spike-support question — **NOT-VERIFIED**"; l.999: COF-crit WRONG, NCE not k-uniform (≈ 25(k−1)). (Session 25's TUNIF then argues the reduction is correct and "(GT-sup) is a k-counting question" — a third position, unreviewed.) |
| T51-F | PASS | CONFIRMED | LINEAR_PACKAGE l.488; no public text |
| "Three corrections to the lead" #2 "**g_0 still has to be lowered**" | — | **inconsistent** | REVIEW_HW_S5 l.552 NARROWED "'g_0 must be lowered' ... true arithmetically, but the breach does not bind against DX′", and HANDOFF withdrawn item 1 withdraws exactly that instruction. |
| "Three corrections to the lead" #3 "(GT-sup) was never a spike-support question" | — | **superseded** | reversed by REVIEW_BFT_B_S9_S10 S10-14 (NOT-VERIFIED) — the lead itself says "reversing my earlier relay" (SESSION24 l.1388-1391) — then re-argued by TUNIF. §52 still shows the reversed position. |

### r55l-R3 — §53 (follow-on wave)
| statement | verdict | evidence / correct reading |
|---|---|---|
| "Reviews of session-24 output (**4 of 8 files reviewed; 4 remain**) ... STILL UNREVIEWED: [14 files]" | internally inconsistent | the list it gives has 14 entries |
| "What closed": (N-Q); (Res-Hölder) "CONFIRMED unconditional by review"; (CO-fun) under (CC-0) | CONFIRMED | REVIEW_NQ_S1; REVIEW_BFT_B_S9_S10 l.1009, S10-6 |
| "the **lattice Green's-function estimate PROVEN** with explicit R-uniform constants" | **REFUTED as stated** | GREENT l.683-689 ("COMPUTED upper sum, not closed form"); CODEX_REVIEW_GREENT_TG F4 |
| "(NEUT-box) is FALSE **by exactly L^{2k}** ...; route (ii)/GT-ell **dies**" | detail errors | r55l-H9 (≥ L^{2k} − 1 proved; GT-ell dead *independently*) |
| "(CovLift)'s non-residual clause at θ > 0 is FALSE for every lift" | REFUTED by omission | r55l-H15 (fixed representative; infimum form ⟸ (CURV-dec)) |
| "(TENT-osc) is FALSE by exactly n² (YSUP)" | REFUTED by omission | YSUP: "**CONDITIONAL on the profile input** (BFT_A §38.7 / Theorem YH)" |
| "the gauge escape is a NULL OPERATION (TG-PRICE) — route (β) **CLOSED** ... the only μ that would work is the one Λ₀ excludes (TG-EXCL)" | faithful to TGAUGE_PRICE (l.230, l.268, l.350, l.531-535); **disputed by Codex** | CODEX_REVIEW_GREENT_TG (possibly still being written) F6: TG-PRICE is "a valid conditional conservation identity, not evidence that \|P\| is large ... No broader route closure follows"; F7: the excluded μ is not the only cheap one, and the saving factor is q−1 (6560), not q (6561). I agree with F6's logic (ρ = 1 under the elimination condition is not a lower bound on P); F7 I did not re-derive. |
| "Lever (b) on HW's ×6561 REFUTED (HW §35, Proposition SH-neg)" | CONFIRMED | HW l.1903-1908 |
| "**a_RS BINDS TODAY** and **RLARGE l.618 is FALSE**" | **REFUTED** | [S25-fix 4] / ARS_BIND; never annotated (RTARGET frozen at 21:02:17Z) |
| "(i) **(GAP-Z) IS BFT-5's (G♯_0-field)**" | **REFUTED / unestablished** | r55l-H14 |
| "(iii) (CEM-2) was never an ingredient ... (PLD §19, Theorem W-FREE)" | CONFIRMED | PLD l.3118, l.3366 |
| defect 1: "Three separate multi-decade errors today trace to [symbol collisions], **including the 52-decade τ_♭ error**" | **REFUTED (currency) / mis-attributed** | 52 decades is η_♭ (26.04 in τ_♭); TAUFLAT §2.1's mechanism is a stale minimum — which §53's own defect 2 says ("correct at the C_D it was written for, in a file that later made C_D an output"). The same error is counted under two defects. |
| "seven errors of mine" incl. "'10²⁸ → ≈16' when the true price is 2.51e8" | CONFIRMED | GREENT l.411 (𝒮_T = 2.514·10⁸) |

### r55l-R4 — §54: does the pre-statement precede the session-25 derivations it claims to precede?
**Verdict: CONFIRMED on timing (to the strength file-system evidence allows); REFUTED on two content points.**
- Timing: §54 stamp 21:02:17Z = RTARGET mtime. Earliest session-25 worker artefact: EPS1_EXEC.md born
  21:05:38Z (then SYMBOLS 21:06:32, REVIEW_ARS_EPS_S1 21:07:43, NBG_B 21:07:44, NBG_A 21:14:34 ...); earliest
  session-25 check file: checks/kn1_criteria.md 21:12:22Z; no check file of any id was born between 15:48:06Z
  (last session-24 GREENT post-hoc output) and 21:12:22Z. §54's text cites only session-24 material
  (EPS1_SWEEP §5, ARS_FIX §3.3/§4.1/§8.6) and quotes no session-25 result. Caveat: birth times bound first
  existence only from above (a whole-file rewrite resets them), so this is the strongest evidence available
  without git, not a certificate.
- Content error 1 — **mis-stated target**: "T55-D/E. (N-bg) ... from two independent sides: its own, and
  BFT-5's (G♯_0-field), which **[S24-flag] identifies as the same obstruction**" and failure mode "NBG-F1
  **(N-bg)** and BFT-5's (G♯_0-field) are not the same obstruction → [S24-flag]'s collapse is wrong". Session
  24 identified **(GAP-Z)**, not (N-bg), with (G♯_0-field) ([S24-note 2], a *note*; RTARGET §53 (i); BFT_B
  §43.3 item 4). §54 therefore put a different question to T55-D/E than the one session 24 had banked, which
  is the ill-posedness NBG_ADJ later diagnosed ("the two workers counted in different units", "(N-bg) is not
  one of them, it is downstream"). REFUTED; this is a lead misstatement that cost a worker (T55-K).
- Content error 2 — **wrong line**: "where RLARGE **l.996** says only 'M̄_c is a mean of the T^σ_y'". The
  string is at RLARGE l.992 (RLARGE unmodified since checkout, so not drift). The lead recorded the same wrong
  cite in the T55-A brief as its own error 5 (SESSION25 l.289-290) but not the copy in §54.
- The lead's own hypothesis in §54 ("they are not a fork ... (C2) is the 82-decade adoption") was refuted in
  session 25 and recorded as lead error 2 — the pre-statement worked as intended there.

---

# ITEM 5 — INTEGRATION_AUDIT.md shortfalls A1-A6 (born 12:14:20Z, last write 13:00:37Z — never revised after REVIEW_NORMS_S1, REVIEW_BFT_B_S9_S10 or session 25)

| id | shortfall | verdict | evidence / correct reading |
|---|---|---|---|
| r55l-A1 | A1 (θ_w under-quantified; per-consumer θ_w: PROOF/N5 0, SF > 0, SQ > 1) — §3, then **withdrawn** §6 | CONFIRMED (withdrawal) | REVIEW_SQ_S4 l.80-81, l.511-525 ("now moot for SQ": θ_w = 2 and θ_r > 2 proven; EPS-T + NREFL **+ RED-0** supply the free-boundary clause — the audit omits RED-0) |
| r55l-A1′ | A1 **reinstated** §7: "with a single common theta_w there is no solution in (0, 2] at all ... BFT-1 cannot support the composite route as written, **for anybody**" | CONFIRMED except "for anybody" (REFUTED); **incomplete** | NORMS §N7 (r55l-H4). Incomplete: NBG_B NB7 / THETAW / CODEX_REVIEW_THETAW show the restatement needs more than the (θ_w^c, θ_w^r) pair (a separate source weight θ, α, the potential clause θ_A) — "Recommendation (A1′): restate BFT-1 with two weights" is not sufficient as stated. |
| r55l-A2 | A2 (cone sibling (REG-min) is not a corollary) — withdrawn §6 | CONFIRMED (withdrawal) | REVIEW_SQ_S4 S4-22 (SQ proves the sibling natively) |
| r55l-A3 | A3 (free-boundary ε-regularity) — withdrawn §6 | CONFIRMED (withdrawal) | REVIEW_SQ_S4 l.80-81, l.563 (NREFL CONFIRMED) |
| r55l-A4 | A4 (all-order mixed-derivative decay; (BB-mix) → BFT-6) | CONFIRMED in substance; "**the single gate** on layer 2's expansion" REFUTED | r55l-H6 |
| r55l-A5 | A5 (CONST-T): "C_T ≲ 1e13 ... reviewer's read ... puts C_T in 1e9-1e15, straddling" | CONFIRMED at the time; stale | REVIEW_SQ_S4 l.385, l.394, l.577; superseded by CONST_T (q = 8: C_T ≥ 1.27·10¹⁴) and EPSSTAR (C_T(12) = 5.288·10¹²). |
| r55l-A6 | A6 "PROOF.md's own diagnosis of Z_col is wrong ... it is a marginality no-go that no scale-covariant norm can fix" | **REFUTED — REVERT** | both halves: RN1-7c (the diagnosis is true) and REVIEW_NORMS_S1's main finding (the no-go is NOT ESTABLISHED). |
| r55l-A7 | §7 "uniformity problem is solved at the trivial background by Theorem N1-15, conditional on (N-Q) and (N-loc); the magnitude problem ... some 10^32 above the C_flat term" | CONFIRMED with scope | as r55l-T4 (d = 4 only; 10³² at one m_1) |
| r55l-A8 | §2 table: "PROOF / N5 needs BFT-0, BFT-1 at theta_w = 0, BFT-2, BFT-4: YES" | CONFIRMED | θ_w > 0 decay implies the θ_w = 0 bound; the existential (0, 2] serves it. |

---

# ITEM 6 — SESSION24_RESULTS.md / SESSION25_RESULTS.md: sampled claims (45), hit rate, and the lead's corrections

Each row: the lead's claim (file:line, current) → source checked → verdict. "Faithful" = the lead states
its source correctly. Where a faithful claim's source has since been refuted by an in-lane review or an
approved-setting Codex review, the row says so and the verdict is REFUTED (with my agreement stated).

| # | claim (lead's ledger) | source checked | verdict |
|---|---|---|---|
| S24-1 | l.218 "(S2)'s ceiling = 4.89789e-97" | REVIEW_HW_S5 l.43, l.290 | CONFIRMED |
| S24-2 | l.219 "REL-boot ... = 4.89802e-97" | REVIEW_HW_S5 l.44, l.291 | CONFIRMED |
| S24-3 | l.220-221 "(T) 9.99104e96·c₊ against n_H = 9.99102e96·c₊" | REVIEW_HW_S5 l.293-294 | CONFIRMED |
| S24-4 | l.224-225 "g_0² ≲ 2.5e-152/C_Ω — slack by ~55 orders for c₊ ≲ 2e55" | REVIEW_HW_S5 l.54, l.318-319 | CONFIRMED |
| S24-5 | l.229 "the reviewed value is 1.81e91" | REVIEW_HW_S5 l.553 | CONFIRMED |
| S24-6 | l.233 "6561 → 2401 is free in one line" | REVIEW_HW_S5 l.58, l.332-334 | CONFIRMED |
| S24-7 | l.556-557 "A_per ∈ [1.08, 1.38]·𝔠 — a gain of 920-1171 per level" | NORMS l.456-458 (faithful); REVIEW_NORMS_S1 l.50-56 "WRONG as stated" | REFUTED (source; lead itself corrected it at l.1086 ff. — correction right) |
| S24-8 | l.559 "Z_col = 156 is the column mass of 𝒦 = L^d·K̄ ≈ 9.7 plus ... ≈ 1.5" | NORMS l.453-455 ("≈ 11.2 instead of 156") | **REFUTED (lead misstatement)** |
| S24-9 | l.560-562 "PROOF.md's own diagnosis is WRONG" | REVIEW_NORMS_S1 RN1-7c l.448-460 | **REFUTED (lead; never corrected)** |
| S24-10 | l.1054 "Proposition N1-8's Z_col correction retained (it stands on its own)" | RN1-7c | **REFUTED (lead)** |
| S24-11 | l.1043-1046 "Check n1-D is a TAUTOLOGY ... computes k·eA + k·((d-4) - eA) after discarding the only derived quantity" | REVIEW_NORMS_S1 RN1-3 | CONFIRMED |
| S24-12 | l.1351-1356 "They differ by L^{θ(k-1)} ... ≈ 25(k-1)" | REVIEW_BFT_B_S9_S10 l.73, l.520 | CONFIRMED |
| S24-13 | l.1371 "RHT-cc (K_f = 8.7377 verified)" | REVIEW_BFT_B_S9_S10 l.986 | CONFIRMED |
| S24-14 | l.1384-1385 "(BFT-5_E) clause (c) is CONDITIONAL, not PROVEN" | REVIEW_BFT_B_S9_S10 S9-18 l.384-390 | CONFIRMED |
| S24-15 | l.1393-1394 "bb10_criteria.md has birth = mod = 13:12:15" | `stat`: 13:12:15Z / 13:12:15Z | CONFIRMED |
| S24-16 | l.184 "[CORRECTED by TAUFLAT §6.5: τ_R is NOT the binding entry ...]" | TAUFLAT §6.5 item 2 (l.611-620); SQ l.318 | CONFIRMED |
| S24-17 | l.792 "CONST_T: not at q = 8, yes at q ≈ 30" | CONST_T l.389, l.483 | CONFIRMED |
| S24-18 | l.1186 EPSSTAR "C_T is a number" (5.288e12 at q = 12) | EPSSTAR l.549-555 | CONFIRMED |
| S24-19 | l.1745 "(TENT-osc) is FALSE by exactly n² = L^{2k}" (no qualifier anywhere in the entry) | YSUP l.260 + status table: "CONDITIONAL on the profile input" | **REFUTED (lead dropped the qualifier)** |
| S24-20 | HW s6 "×81 off 6561 — ×29.6 beyond what the review offered" | HW l.1814-1816; 2401/81 = 29.64 (hand) | CONFIRMED |
| S24-21 | l.1895 "TGAUGE_PRICE ... §1 PRE-STATED ..., first edit 15:23 UTC" | `stat`: TGAUGE_PRICE.md born 15:41:12Z; checks/tg1b_criteria.md born 15:38:23Z, *after* tg1b_ledger.py (15:36:09Z) and tg1b_out.txt (15:36:14Z), though TGAUGE l.172/l.471 say "≈15:35 UTC, before the re-run" | NOT-VERIFIED (fs contradicts both stated times; birth-time caveat; CODEX_REVIEW_TUNIF F7 found the same pattern in TUNIF) |
| S24-22 | GREENT heading "the '≈16' price CORRECTED by 1.6e7" | GREENT l.411 (𝒮_T = 2.514·10⁸); 2.514e8/16 = 1.57e7 (hand) | CONFIRMED |
| S24-23 | l.1272-1278 "(CEM-2) is NOT an ingredient of (CEM^COL)" | PLD l.3118, l.3366 | CONFIRMED |
| S24-24 | §52/T51-A REVIEW_BFT_A_S8 "φ₁ = −1/432, φ₂ = −17/104976, ratio 17/243" | REVIEW_BFT_A_S8 l.45; (17/104976)/(1/432) = 17/243 (hand) | CONFIRMED |
| S25-1 | l.15-16 "M̄_c is defined constructively at PROOF.md l.1754 ... 1/1944 each" | PROOF now ~l.1808 (drift +54); d!L^d = 24·81 = 1944 (hand) | CONFIRMED (cite drifted) |
| S25-2 | l.21-22 "1944 indices collapse to 633 distinct transporters" | KN_ADOPT (faithful); CODEX_REVIEW_KN F1: 475 reduced paths, 633 are labels | REFUTED (source; Codex; the lead records this in CX-2 — correction right) |
| S25-3 | l.153 "'82 decades' is +2.303 decades over the lane's own already-proven route" | arithmetic: CODEX_REVIEW_DECADES [2.303258218, ...] CONFIRMED; "already-proven route": DECADES F1 / KN F3 REFUTED (RLARGE l.513-514 excludes joint pricing; HIST l.505-521 assumes (PLD-q)_k) | REFUTED as framed (source REVIEW_ARS_EPS_S1; I agree with Codex) |
| S25-4 | l.163 "The route figure is 201.029×" | KN_ADOPT §3.2; Codex KN F8, DECADES | CONFIRMED |
| S25-5 | l.323-324 "post-hoc it needs only θ_w^c > 7/4 and θ_w^r > 1" | NBG_A (faithful); CODEX_REVIEW_GAPZ F9 REFUTED. Hand check at c = 9/5, r = 6/5: a = min(1, c−1) = 4/5, exponent 4 − r − 3a = 4 − 6/5 − 12/5 = **+2/5 > 0** — the soft series grows | REFUTED (source; I agree with Codex; never corrected in SESSION25) |
| S25-6 | l.373 "θ_0: 4, not 2" | SYMBOLS §4 l.457 | CONFIRMED |
| S25-7 | T55-M "a_RS occurs in RLARGE.md exactly five times ... all inside Appendix A" | my grep (5 lines, 6 occurrences, all > l.824) | CONFIRMED |
| S25-8 | T55-M "live exponent clears DX′ by +63.619 decades at every live ε_1" | ARS_BIND A7 (faithful); CODEX_REVIEW_DECADES F2; RLARGE l.88-92 ("a ≲ 10⁻⁸⁶") | REFUTED as established (source; agree) |
| S25-9 | T55-K "Z = 1 IS admissible" | NBG_ADJ; CODEX_REVIEW_GAPZ F1 CONFIRMED | CONFIRMED |
| S25-10 | T55-K headline "TWO obstructions" | NBG_ADJ (faithful); CODEX_REVIEW_GAPZ count ruling NOT-VERIFIED, F3/F4 REFUTED | REFUTED (source; agree) |
| S25-11 | T55-J headline "SATISFIABLE" | THETAW (faithful); CODEX_REVIEW_THETAW: reduced system feasible (CONFIRMED), full target NOT-VERIFIED, R_lin REFUTED | REFUTED as stated (source; agree) |
| S25-12 | T55-F headline "(T-UNIF) PROVEN. The open half of (N-loc) closes." | TUNIF (faithful); CODEX_REVIEW_TUNIF: full TU-5/6 NOT-VERIFIED/CONDITIONAL, "Do not propagate" | REFUTED as stated (source; agree on status) |
| S25-13 | T55-N headline "Fixing [q] is worth 24 decades" | QFIX (faithful); CODEX_REVIEW_DECADES F3: historical a_RS lever 24.089; live ε-limited lever [12.044552885, 12.044552886] = 24.089105770/2 (I checked the halving: a ∝ ε² vs a_RS ∝ ε⁴) | REFUTED as live currency (source; agree) |
| S25-14 | CX-1 "F3 ... Verdict REFUTED, and it applies to all three Claude workers at once" | CODEX_REVIEW_GAPZ F3 | CONFIRMED |
| S25-15 | CX-1 as a whole (F1-F7 reported) | final CODEX_REVIEW_GAPZ: count ruling, F8, F9, F10, F12 omitted | **REFUTED by omission (lead)** — the omitted count ruling is what [S25-fix 5] needed |
| S25-16 | CX-3 "The theorem survives its hardest attack. Three surrounding items do not." | final CODEX_REVIEW_TUNIF: disposition "Do not propagate 'T-UNIF / N-loc closed'"; F6 NOT-VERIFIED; F10 literal TU-3 REFUTED without periodicity | **REFUTED (lead summary of a partial file)** |
| S25-17 | CX-3 l.923 "A pure pole A/ε over **four decades** grows by exactly 1000" | CODEX_REVIEW_TUNIF F2: "Four sample values ... span **three** decades" | **REFUTED (lead-introduced slip)** |
| S25-18 | l.546 T55-F "exactly constant over six decades" | TUNIF l.549 (faithful); Codex: six points span five decades | REFUTED (source; trivial arithmetic, agree) |
| S25-19 | CX-4 "the doubled-currency break-even ... 80.940, not 81.7" | CODEX_REVIEW_FACEB R5; (160.380 + 1.5)/2 = 80.94 (hand) | CONFIRMED |
| S25-20 | the earlier §PROVENANCE section (in git history) "TUNIF at 10.8 KB of what became 33 KB, KN at 6.9 KB of 36 KB" | `stat` sizes 33170 B, 36466 B | CONFIRMED |
| S25-21 | Lead errors #5 "A wrong line cite in the T55-A brief (l.996 for l.992)" | RLARGE l.992 | CONFIRMED (but the same wrong cite in RTARGET §54 is not recorded) |
| S25-22 | Lead errors #1 "D5's premise ... REFUTED (T55-E). Corrected at both PROOF.md sites as [S25-fix 2]" | CODEX_REVIEW_GAPZ F2/F3/count ruling | **REFUTED (lead): the premise is unestablished, not refuted** |
| S25-23 | Lead errors #3 "1551× ... 201.029×" | as S25-4 | CONFIRMED |
| S25-24 | CX-2 "F2 ... the branch boundary is κ = 128/13689, independent of ε_1 and N" | CODEX_REVIEW_KN F2 | CONFIRMED |
| S25-25 | T55-H "§3 ... a_RS may not be consumed at all — and the question ARS_FIX said 'has to be SAID' is already said" | REVIEW_ARS_EPS_S1 RA-F1 l.122-130 | CONFIRMED |
| S25-26 | T55-I "(CO-fun) ... THREE classes ... (cc) composite-co-closed FALSE AS STATED. Decision D1's class is (cc)" | COFUN (faithful; not re-derived) | CONFIRMED (faithful; unreviewed except CODEX_REVIEW_COFUN, not used here) |
| S25-27 | the earlier §PROVENANCE section (in git history) "Every Codex worker (8 runs) is gpt-6-astra, reasoning effort max" | 8 CODEX_REVIEW files existed then (GAPZ, KN, TUNIF, FACEB, COFUN, DECADES, QFIX, THETAW); banners not inspected | NOT counted (model provenance is outside what files show me) — **dropped from the tally of this table** |

Count over the 44 rows I could decide (S25-27 dropped): faithful to source 36, lead misstatement 8
(S24-8, S24-9, S24-10, S24-19, S25-15, S25-16, S25-17, S25-22), NOT-VERIFIED 1 (S24-21). Hmm — that is 45
rows with S24-21; the arithmetic is: 24 S24 rows + 26 decided S25 rows = 50 rows listed, of which **S24-21
NOT-VERIFIED (1)**; the remaining 49 split into **faithful 41 / lead misstatement 8**.

**Hit rate (the lead states its source correctly): 41/49 = 83.7%** (CONFIRMED rows plus faithful rows whose
source was later refuted). **Correct as it now stands** (removing the 9 faithful rows whose source has since
been refuted by an in-lane review or an approved Codex review I agree with — S24-7, S25-2, S25-3, S25-5,
S25-8, S25-10, S25-11, S25-12, S25-13, S25-18 — that is 10 rows): **31/49 = 63.3%**. The misses cluster in
three places: anything touching Z_col/N1-8 (3 of 8), dropped qualifiers (CONDITIONAL / with a fixed
representative / unreviewed), and the Codex-wave summaries written from partial files (4 of 8).

### Targeted: the entries the lead later had to correct — is the correction itself right?
| correction | verdict on the correction |
|---|---|
| [S24-fix 1a] no-go withdrawn | RIGHT on the no-go; WRONG in keeping "N1-8's Z_col correction stands" (RN1-7c) |
| HANDOFF withdrawn item 2 | RIGHT |
| NCE k-uniformity withdrawn (SESSION24 l.877, HANDOFF CP5, §53) | RIGHT (not propagated to the PROOF [S24] tail item 4 or §52 T51-E) |
| SESSION24 l.424 "an identity is not a bound" | RIGHT (REVIEW_BFT_B_S9_S10 l.999) |
| SESSION24 l.184 τ_R not the binding entry | RIGHT (TAUFLAT §6.5) |
| "≈16" → 2.51e8 (HANDOFF CP1, §53) | RIGHT (GREENT l.411) — but the same sentence's "GREENT PROVES ... with explicit constants" is not (r55l-F9) |
| ×17 vs ×82 → ×82 for the closed column | RIGHT (spot) |
| §52 correction #3 "(GT-sup) never a spike question" | WRONG/superseded: reversed by REVIEW_BFT_B_S9_S10 S10-14; §52 never annotated |
| [S25-fix 1] 1551× → 201.029× | RIGHT (Codex KN F8, DECADES); mis-cites KN_ADOPT §5 for §3.2 |
| [S25-fix 4] a_RS binds → binds nothing | RIGHT structurally (my greps); its +63.619 clearance overclaims (Codex DECADES F2) |
| [S25-fix 2] ONE → THREE obstructions | WRONG as a refutation (invalid status argument, Codex GAPZ F3; M-identification, F2) |
| [S25-fix 5] THREE → TWO | WRONG as an established count (Codex GAPZ count ruling) |
| the earlier §PROVENANCE section (in git history): Codex-wave summaries "superseded by the final files" | RIGHT as a warning, but not acted on: no CX section was redone and PROOF's header still carries the [S25-fix 2]/[S25-fix 5] counts |

Score: 9 right, 2 partly right, 3 wrong or superseded.

---

# ITEM 7 — the tally "72 / 2 / 7 / 24 + 1"

**Verdict: CONFIRMED — the count should not move, and the lead did not move it.**
- What the tally counts (PROOF §3 ~l.4774-4800): PROOF.md's own main-path items — PROVEN-HERE 72;
  IMPORTED-AND-REVERIFIED 2; IMPORTED-NOT-YET-REVERIFIED 7 (L1d, L2, L3g, L4a, L5, L6, F1); OPEN (main path)
  24 (BG-reg, the L3g(a)-slice completion, W1-loc, D4-obs, N5, ...); + 1 comparison-branch item. Lane
  results enter only when PROOF adopts them; RTARGET §51's anti-inflation clause and §53 ("Nothing below is
  counted in PROOF's tally") restate this.
- I checked every item sessions 24-25 record as PROVEN, REFUTED, struck or withdrawn. All are lane items:
  NORMS (N1-13, N1-15, N1-8), NQ_CHECK (NQ-1), NLOC, GREENT, TUNIF, BFT_A/B ((CO-0), (CO-up), (SB), RHT-cc,
  COF, NCE, GZ-FALSE, CONJ, TRANSP), TENTQ (QN, QSBP, QFALSE, TQ-INT), YSUP, TGAUGE_PRICE, EPSSTAR, CONST_T,
  STAR_CONST, SQ/REVIEW_SQ_S4, HW (SH-att, SH-neg), PLD (W-FREE, PATCH), RLARGE (l.618, a_RS), KN_ADOPT,
  ARS_FIX/ARS_BIND, NBG_A/B/ADJ, HESSREL, THETAW, COFUN, QFIX, GESIGN, FACEB. None is one of PROOF's 105
  counted items. The PROOF-owned material touched — the Z_col sentence in [S21]'s (H-C) commentary (uncounted;
  and the "correction" is itself false), N5-sf0's λ_min ([SF7-edit], a constant of a PROVEN item), the BFT
  clause table (bookkeeping), (CL-4) (OPEN, untouched) — changes no category. No IMPORTED item was
  reverified: GREENT bounds the free scalar lattice Green's function for NLOC's NL-8, not Balaban's
  gauge-field propagator (L3g) or background field (L2).
- Two cautions for the lead, neither a change to the number: (1) the tally is "unchanged" *by construction*
  — under its rule it could not register the ~40 lane PROVEN-HERE items or the dozen refutations of these
  two sessions, so "unchanged" is not evidence of anything about progress; (2) the 72 still include
  unreviewed PROVEN-HERE items from earlier sessions; nothing in sessions 24-25 re-examined them.

### Errata to this file (append-only; recorded, not edited)
1. **ITEM 6 count paragraph.** The sentence beginning "Count over the 44 rows I could decide ... faithful
   36" and the "Hmm — that is 45 rows" aside are wrong bookkeeping, written before I finished the table.
   The table has 24 S24 rows + 27 S25 rows; S25-27 is dropped; **S24-21 is NOT-VERIFIED; 49 rows are
   decided: 41 faithful, 8 lead misstatements.** The faithful rows whose source has since been refuted are
   **10** (not "9"): S24-7, S25-2, S25-3, S25-5, S25-8, S25-10, S25-11, S25-12, S25-13, S25-18. The bolded
   figures stand: **hit rate 41/49 = 83.7%; correct-as-it-stands 31/49 = 63.3%.**
2. **r55l-H2.** I have now read checks/n1_exponents.py l.80-95 directly (not only RN1-3's quotation): l.91
   `total = k * eA + k * ((d - 4) - eA)` is identically k(d−4); `emis` (l.86-87) is never used in it; the
   gate at l.94 `F(total, k) == F(d - 4)` cannot fail. Confirmed from the script.
3. **r55l-H7 nuance.** The one residual question that is genuinely open is scope: [SF7-edit]'s certified
   3.17·10⁻³ is at κ_0 = 1 on the CS-1 class (REVIEW_SF_S7 items 3-4, "owner decision"); whether that scope
   covers PLD §16.8's backgrounds is a question about the certified value's domain, not a conflict between
   two numbers for the same object. The verdict (not a live conflict between L0-1 and PLD) stands.
4. **r55l-F9 / r55l-T15 / §53 Green row nuance.** GREENT's own theorem heading (l.281) does read "Theorem GT-1
   / GT-2 (the estimate, with explicit R-uniform constants): PROVEN-HERE". The lead copied the heading. But
   GREENT §8 item (i) (l.682-689) — a paragraph addressed **to the lead**, "three claims of mine a hostile
   reviewer should attack first" — says the constants are a "COMPUTED upper sum" and the quadrature "not a
   proof". GREENT is internally inconsistent; the lead's ledger kept the heading and dropped the caveat it was
   explicitly handed. Verdict unchanged (REFUTED as stated).

---

# SUMMARY TABLE — every claim in this batch, by id

| item | CONFIRMED | REFUTED | NOT-VERIFIED |
|---|---|---|---|
| 1 PROOF header | H0a, H2a, H3, H4a, H5, H6a, H8, H9a, H10a, H11a, H11c, H12, H13, H16, H17 (15) | H1, H2b, H4b, H6b, H7, H9b, H10b, H11b, H14a, H14b, H14c, H15 (12) | H0b (1) |
| 2 PROOF [S24] tail | T1, T2, T4, T5, T8, T12, T13, T14, T21 (9) | T3, T6, T7, T9, T10, T11, T15, T16, T17, T18, T19, T20 (12) | — |
| 3 HANDOFF | F2, F3, F4, F5, F6, F8, F13, F15, F17, F19, F21 (11) | F1, F9, F10, F11, F12, F14, F16, F18, F20 (9) | F7 (1) |
| 4 RTARGET §51-§54 | T51-A, T51-D, T51-F, §53 "what closed" (non-Green), §53 lever (b), §53 (CEM-2), §53 "seven errors", §54 timing (8) | T51-B, T51-C, T51-E, §52 corr #2, §52 corr #3, §53 "4 of 8", §53 Green, §53 NEUT-box, §53 CovLift, §53 TENT-osc, §53 TG-EXCL exclusivity, §53 a_RS/l.618, §53 (GAP-Z) IS, §53 defect-1 "52-decade τ_♭", §54 (N-bg)-vs-(GAP-Z) target, §54 l.996 (16) | §51 precedence (R1) (1) |
| 5 INTEGRATION_AUDIT | A1, A1′a, A2, A3, A4a, A5, A7, A8 (8) | A1′b, A4b, A6 (3) | — |
| 6 SESSION24/25 sample | 31 (S24-1..6, 11..18, 20, 22..24; S25-1, 4, 6, 7, 9, 14, 19..21, 23..26) | 18 (lead: S24-8, 9, 10, 19, S25-15, 16, 17, 22; source refuted: S24-7, S25-2, 3, 5, 8, 10, 11, 12, 13, 18) | S24-21 (1) |
| 7 tally | "72 / 2 / 7 / 24 + 1" correct and should not move (1) | — | — |
| **total** | **83** | **70** | **4** |

**REFUTED by type.** (a) the lead misstated its source at the time of writing (incl. dropped qualifiers,
scope extensions, mis-cites that change meaning): **35**. (b) stale — right when written, now contradicted
by later in-lane work the lead had already read and cited elsewhere: **19**. (c) faithful to the worker, but
the worker's claim is refuted by an approved-setting Codex review or an in-lane review, and I agree: **16**.

---

# WHAT TO DO WITH PROOF.md'S HEADER BLOCK

**Revert outright** (the text is wrong, not merely stale):
1. **[S24-fix 1]** — the whole erratum "PROOF.md's Z_col diagnosis ... is WRONG ... Z_col is the column mass
   of the curvature kernel ≈ 9.7 + 1.5". Replace with REVIEW_NORMS_S1 RN1-7c's *addition*: PROOF's
   `Z_col ≥ 27 crossing links × spread` is true; in the field-strength norm the replacing column mass is
   ≈ 11.2 (measured, uncertified; max-vs-average needs N1-9's decay input). [r55l-H1]
2. **[S24-fix 1a]'s sentence** "Proposition N1-8's correction of the Z_col diagnosis stands; the no-go built
   on top of it does not." → keep only "the no-go is withdrawn; the per-level route is OPEN". [r55l-H2]
3. **The three obstruction counts**: [S24-note 2]'s "(GAP-Z) ... IS ... (G♯_0-field) ... ONE obstruction ...
   must not count them twice"; [S25-fix 2]'s "They are THREE obstructions ... The refutation is three lines";
   [S25-fix 5]'s "Distinct statements: three, no pairwise implication" and "Independent paper-scale
   obstructions: TWO". Replace all with CODEX_REVIEW_GAPZ's ruling: three named unresolved requirements,
   zero established identifications, independence count NOT-VERIFIED; do not use any count for priority.
   Also drop "Highest leverage: (HESS-rel)" (HESSREL + Codex F7). [r55l-H14]
4. **[S24-flag 1]** (and HANDOFF "One PROOF-owned constant conflict"). Replace with: "[SF7-edit] adopted
   λ_min ≥ 3.17·10⁻³ for N5-sf0's gap; propagate it to the body lines that still print 6.6·10⁻¹⁰". [r55l-H7]
5. **[S24-flag 2a]'s θ_0 clause** "whose collision caused the 52-decade τ_♭ error (TAUFLAT §1)". Replace with
   "a stale minimum produced a 52-decade error in η_♭ (26 decades in τ_♭) (TAUFLAT §2.1); the unrenamed
   θ_0 collision made it easy (TAUFLAT §6.1)". [r55l-H10]

**Amend** (keep, with the correction): [S24-fix 3] "for any consumer" → "for the composite route" (r55l-H4);
[S25-fix 3] ¾ → 1 − α, "requires θ_w^r = 3" → "> 2", record THETAW + CODEX_REVIEW_THETAW (r55l-H5); [S24-fix 4]
"the single gate" → "a gate" (r55l-H6); [S24-fix 2] add S9-13's class caveat (r55l-H3); [S24-flag 3] record
TAUFLAT's CONFIRMED / LOAD-BEARING (r55l-H13); [S24-flag 4] record YS-PHI (r55l-H8); [S24-flag 5] "≥ L^{2k} − 1",
GT-ell dead independently (r55l-H9); [S25-fix 4] "+63.619" → "conditional benchmark (θ at its supremum 1/24,
a_A non-binding, C_Ω = 1)" and strike the retained paragraph to its end (r55l-H11); [S25-fix 1] cite KN_ADOPT
§3.2 (r55l-H11); [S24-note 3] "with the fixed representative; the infimum form ⟸ (CURV-dec), OPEN" and cite
§42 (r55l-H15); [S24-note 4] cite §41.1 (r55l-H16).

**[S24] tail — revert:** D2 "Upgraded ... to a theorem ... no future session should attempt"; "The per-level
route is dead by theorem"; item 4 "Theorem NCE ... uniformly in k and T"; "RLARGE l.618 ... REFUTED"; "a_RS
is found to bind TODAY ... 82 decades"; the "(three obstructions, not one)" annotation. Update items 2-4 per
r55l-T6, T7, T10, T11.

# WHAT CHANGES FOR THE TALLY AND THE HANDOFF CRITICAL PATH
- **Tally: no change.** 72 / 2 / 7 / 24 + 1 is right under the ledger's rule (ITEM 7).
- **HANDOFF critical path should say:** CP1 — record TUNIF's claim and CODEX_REVIEW_TUNIF's NOT-VERIFIED,
  GREENT's constants as COMPUTED (not certified), and that "layer 2 needs T-uniformity" is contested; CP2 —
  replace "(N1) + (CovLift) g_Z at θ > 0" by BFT_B §43.3's reading ((GAP-Z) [identity with anything
  unestablished], (N1-nd), (CURV-dec)); CP3 — replace (CEM-2) by (BCH-1) (PLD W-FREE) and (CEM-1)'s
  restatement (Theorem AT); CP4 — C_T(12) = 5.288·10¹², q_min = 11 (EPSSTAR), plus QFIX/CODEX_REVIEW_QFIX on q;
  CP5 — keep the factor k / (SPD)/(W2) first (COFUN independently agrees), delete (NEUT-box) and the
  "one scalar per box" (TENTQ TQ-INT), mark (Y-sup^loc) FALSE by n (YSUP); CP7 — "a gate", not "the single
  gate"; "Two target restatements" — the weight pair is not the whole restatement (THETAW F1 as corrected by
  CODEX_REVIEW_THETAW); delete "One PROOF-owned constant conflict"; update the "UNREVIEWED" list
  (REVIEW_NORMS_S1, REVIEW_NQ_S1, REVIEW_BFT_B_S9_S10 exist) and the reading list (SESSION25_RESULTS,
  RTARGET §53-§54, the Codex reviews).

# CODEX VERDICTS USED, AND WHETHER I AGREE
| Codex review (state on disk) | verdict used | agree? |
|---|---|---|
| GAPZ (final) | F1 Z = 1 admissible CONFIRMED | agree |
| GAPZ | F2 (GAP-Z)\|_{Z=1} ≠ M as stated; F3 status ≠ non-implication; F4 TWO reverses a reduction; F5 four mismatches ≠ four barriers (ℤ⁴ counterexample); count ruling NOT-VERIFIED | agree (F3/F4 on logic; F5's bound ‖(WHW⁻¹)⁻¹‖ ≤ 1/(9 − 8e^m) re-derived by hand) |
| GAPZ | F7 literal HESS-rel REFUTED; F9 r > 1 REFUTED | agree (F9 re-derived: exponent +2/5 at c = 9/5, r = 6/5) |
| DECADES (final, completion receipt 22:25:13Z) | F2 +63.619 is an upper benchmark; "52 decades described as τ_♭" REFUTED; F3 live q-lever 12.04 not 24.09; +2.303 "already-proven route" REFUTED | agree (F2 supported by RLARGE l.88-92; 52 → 26.04 and 24.089 → 12.0446 by halving) |
| KN (final) | F1 475 ≠ 633; F3 live ceiling uses a, not a_RS; F7 a_η CONDITIONAL on (PLD)_k(i); F8 201.029 / 452.315 CONFIRMED; F10 NO to "append-ready" | agree with F3, F7, F8 (F8 by hand); F1, F10 not re-derived |
| TUNIF (final) | disposition: full T-UNIF NOT-VERIFIED/CONDITIONAL; F2 "four values span three decades" | agree on status and on F2's arithmetic; TU-3 itself not re-derived |
| THETAW (final) | ceiling 1 − α not ¾; R_lin (θ_w^r = 3 with residual sources) empty; full-target satisfiability NOT-VERIFIED | agree on the ¾ point (BFT_A l.827 text); F5 accepted on its quoted inequalities, not re-derived further |
| FACEB (final) | R5 break-even 80.940 not 81.7 | agree ((160.380 + 1.5)/2) |
| GREENT_TG (**possibly still being written**) | F4 constants NOT-VERIFIED / certification REFUTED; F6 TG-PRICE is an identity, no route closure beyond the narrow no-go; F7 excluded μ not unique, factor q−1 | agree with F4 (GREENT concedes it) and F6 (logic); F7 block-sum identity checked by hand, rest not re-derived |
| COFUN, QFIX, NBG2, SYMBOLS, OLDREV | not used | — |

### Errata, continued (written after the summary; appended, not edited)
5. **CODEX_REVIEW_QFIX was cited in r55l-T7 and in the CP4 recommendation before I had read it.** I have now
   read its summary table and stdout summary (it has a "Final source receipt"): F12 "least q = 12" → q = 11.5
   already passes (12 is a tested-integer statement); the q → ∞ objective → −∞ once θ_G is restored; the
   24.089-decade lever → 12.044552885435 under the live quadratic exponent; "Most dangerous NOT-VERIFIED
   issue: whether the live route consumes a_RS at all". This is consistent with what T7/CP4 say ("further
   dispute q's role"); I agree with the 12.0446 halving (a ∝ ε² vs a_RS ∝ ε⁴).
6. **CODEX_REVIEW_NBG2** (born after this sweep started; mtime 22:36:32Z; it has a summary table and a
   PROVEN-edges graph, so it looks complete) is a **second** independent Codex review of the obstruction
   count. F10: "No mathematical count of two independent obstructions established; six project
   non-implications remain NOT-VERIFIED"; its own decay counterexample A = I − (S + S⁻¹)/4 with weight
   (3/2)^{|x−y|} gives |A⁻¹(x, y)| ≤ 4(2/3)^{|x−y|} (row sums ≤ 3/4 — I checked: (1/4)(3/2 + 2/3) = 13/24 ≤ 3/4).
   F5: residual floor max(1, 7 − 3c) = 8/5 at c = 9/5 (agrees with GAPZ F9 and my hand check); F7 HESS-rel
   REFUTED. **This strengthens r55l-H14: two Codex reviews, same verdict. Agree.**
7. **CODEX_REVIEW_SYMBOLS** (mtime 22:31:09Z): confirms θ_0 ≥ 4, ε_1 ≥ 6, C_1 ≥ 13, c_1 ≥ 11, κ ≥ 5 as lower
   bounds (consistent with my "stale counts" notes in r55l-H10/T18), and refutes SYMBOLS' "×4.1·10⁴" for the
   c_1 pair: (1/117)/(1/(3.5·10⁶)) = 3500000/117 = 29914.5 (hand: 117 × 29914 = 3,499,938, remainder 62).
   SESSION25 l.375 copies "×4.1·10⁴ apart" faithfully — source wrong; agree with Codex. (Not added to the
   ITEM 6 count.)

Review completed 2026-10-28 ~22:48Z. No git command was run; the only file written is this one.
