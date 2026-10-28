# REVIEW_HW_S5: hostile review of lane H session 5 (HW.md §29-§33, l.1425-1734; HW_LOG session 5; checks/w5*)

Reviewer: an independent agent that wrote none of HW.md, HW_LOG.md or checks/w5*. I edited no file but this one. No git
command of any kind was run; no commits, PRs or pushes.

Inputs (read-only; md5 prefix at review time):
HW.md `1f0a6b37…` (1734 lines; §0, §20-§33 read in full, §13-§19 for definitions), HW_LOG.md `fd3474d2…`,
REVIEW_HW_S4.md `72c02d80…` (all; its md5 is exactly the one HW l.1427 declares binding),
checks/w5_criteria.md `8d71d000…`, checks/w5_crc2t.py `2fc806a7…`, checks/w5_out.txt `204fda62…`, w5_time.txt,
w5_stderr.txt; PLD.md `198a3a0f…` (§16.5, §16.7, §16.8, §17.4-§17.6), RLARGE.md `a9269bae…` (§5.4 l.600-620),
REVIEW_RLARGE_V3.md `38b26eda…` (Part 1 S-1…S-5, Part 4 constants table, Part 6), REVIEW_SF_S7.md (l.45, l.320-340),
HIST.md `468e9f03…` (§7.2 Lemma H-geo l.486-497; Theorem HIST-sum l.548-556), HANDOFF.md `9138a176…`.
Scratch (my own re-derivations): scratchpad `redo_w5A.py`, `redo_w5B.py`, `redo_w5B2.py`, `redo_w5C.py`, `scan29.py`.

"Line" means a line of HW.md unless another file is named. Status words as in PROOF.md.

---

## Bottom line

- **Theorem CRC-2T (l.1554-1604) is a CORRECT implication. I tried hard to break it and could not.** The induction is on
  the finite integer N(R) = |S_R|, every inner application is at a strictly smaller value, the telescoping identity is
  exact, and the two-species cross term is handled in the one place where it occurs (step (6)). Specifically:
  - the induction is **not** a nonlinear bootstrap (V-F4), as the session claims and as I verified;
  - the common error the brief warned about — a one-species convergence criterion applied to a two-species gas — is **not
    committed**: (S1) is exactly the species-1 (far-defect collar) criterion, (S2)+(T) the species-2 criterion with the
    species-1 sum already folded in, and the far-defect → animal direction is paid by the induction's own constant c_U with
    the closing inequality 2ε_2 ≤ c_U. The only self-consistency in the constants (c_U on both sides, via b_n) is resolved
    trivially by the choice c_U := 1; it is not a fixed-point problem.
  - **S5-4, S5-5, S5-6, S5-7: CONFIRMED.**
- **But there is no cluster expansion, and §30.4's "gas" is never used as a gas (S5-8: NARROWED).** No polymer partition
  function, no compatibility/hard-core relation, no Mayer identity and no Kotecký–Preiss criterion appear in the proof.
  §29 Target V2 (a) asked for the ratio to be bounded "by the gas's partition-function ratio, or by its polymer sum"; that
  is never established. §33's "(a) The gas written" is a bestiary, not a theorem. The session half-admits this at
  l.1605-1611; the headline and §33 do not.
- **The smallness condition is SATISFIABLE and NOT self-defeating (S5-11: the single most consequential finding).** I
  traced the g-dependence of every constant in g²_CRC. a = θa_bad = θc_prε_1² with ε_1 fixed at its own g-independent
  ceiling; θ's constraint (H5) *relaxes* as g → 0; c_att, b_n, b_D are pure geometry; C_ℓ's λ_* → 6θ; a_A ≥ θa_bad. So
  g²_CRC is a **fixed positive number**, not a moving target. The condition g_K² < g²_CRC is a legitimate smallness
  condition on the coarse (renormalised) coupling, uniform in K and T. **The brief's vacuity worry does not materialise.**
- **The session's own cost accounting is, however, wrong in attribution (S5-12, S5-13: NARROWED, and this reverses the
  session's headline).** I computed, in independent 120-digit Decimal arithmetic:
  - (S2)'s ceiling g²_CRC(c_+ = 1) = 4.89789·10⁻⁹⁷;
  - **REL-boot's own r ≤ ½ ceiling** at the session's own c_f = 531441c_+ (B_* = 531441c_+ + 1) = **4.89802·10⁻⁹⁷**;
  - **HIST-sum's own condition** 6400C_ℓe^{38417B_0}e^{−a/g_K²} ≤ ½ (HIST l.551) at B_0 = 531441c_+ + 2 = **4.898·10⁻⁹⁷**;
  - **n_H(a, B_0)** = ⌊(4 + 38416B_0/log L)/(aβ_-)⌋ (HIST l.550) at the same B_0 = **9.991·10⁹⁶·c_+**, which is n_T to four
    significant figures.
  So **(S2) and (T) impose nothing whatever beyond H8′'s own pre-existing r ≤ ½ and n_♯ ≥ n_H(a, B_0)**. The entire
  tightening is caused by one number: the **×6561 that Lemma SH-att's N_4 step puts into c_f** (81(c_A + c_sf′) →
  531441c_+, l.1625). §32 l.1709-1712 half-notices this ("the same order of ceiling"); §30.6 and §33 and the HANDOFF
  nevertheless present (S2) as the binding new constraint and "n_♯ grows by ≈ 10¹⁰" against a stale n_H.
- **"FAILS at the recorded ceiling" is true but misleadingly framed (S5-13).** REVIEW_RLARGE_V3 l.61 records that the g_K
  ceilings "still do not bind against DX′", and REVIEW_SF_S7 l.335 records the binding program ceiling as
  g_0² ≈ 2.5·10⁻¹⁵²/C_Ω. 4.9·10⁻⁹⁷/c_+ exceeds that whenever c_+ ≲ 2·10⁵⁵·C_Ω. **At the recorded constants (S2) costs the
  program nothing.** HANDOFF's "g_0 therefore has to be lowered. Recheck the downstream constants, including the SF
  thresholds" is an over-reaction that should be withdrawn.
- **The ×6561 is loose, and the session dismisses the sharpening it most needs (S5-14).** A one-line change in SH-att's case
  (a) (use sh_{j+r}(P) ⊇ N_1(π^r(P)), hence sh_{j+r}(Y_i) ⊂ N_3(sh_{j+r}(P))) gives 2401 in place of 6561 for free. And the
  session's own check B2 — plus my own re-runs at M = 20, 40, 80 and an adversarial sampler — show the *additive* excess is
  ≤ 258 per Y-cube and **depth-stable**, i.e. the lemma is loose by ≈ 5·10³. §30.6 l.1652 says a sharper SH-att "is not
  needed". It is exactly what is needed, since it is the sole cause of the ceiling breach the session headlines.
- **The wall has MOVED, not closed (S5-16).** (E2^𝔉) is strictly stronger than the (E2) it replaces, in three named ways,
  and in **three further ways the session does not name**: PLD's own delivered allowance is the slice s_k(𝔥) and the (E1)
  "any w" form (PLD l.1856, l.1904-1906), not the union form; PLD covers **k ≥ 2 only** ((LCR)_0 OPEN, PLD l.1905), while
  (E2^𝔉) includes a level-0 clause; and (E2^𝔉)'s F_< is a **free, unquantified symbol** (l.1528).
- **Provenance: VERIFIED for §29, NOT-VERIFIABLE for the criteria/script order, and binding rule 2 is BREACHED.** §29's
  pre-stated block is byte-identical to the log's 11:11:57 record (I located it by brute-force hash search: 3695 bytes at
  offset 144433, md5 `7830e9f0…`), and HW.md's md5 matches the log's final record. But all file mtimes in this worktree are
  2026-10-28 08:03:19, so the criteria-before-script claim rests on the log alone. Worse, and independent of timestamps:
  **checks/w5_criteria.md contains b_n, b_D, c_att — constants derived in §30 of this same session** (the log l.150-151
  admits it), which the brief's rule 2 forbids outright, and A1/A4/A5's PASS bands are brackets drawn around §30.6's own
  hand values. Those three criteria are reproduction checks, not pre-registrations.
- **w5 re-derived independently: every verdict reproduces.** I recomputed Part A in plain-Python `Decimal` at 120 digits
  (no mpmath, no BLAS, no lock), Part B in pure Python, and Part C in **exact `Fraction` arithmetic**. A1-A5 reproduce to
  5 s.f.; B1-B3 reproduce exactly (1106 / 2386); C1 = 0 exceptions, C2 = 0 violations, C3 = 18 violations — all exact.
  **OVERALL PASS stands.** Two scope defects: §29's promised negative control for check (ii) ("activities above the stated
  threshold, where the bound must fail or the expansion must diverge") was **never run** (no grid point has 2z² ≥ 1; the
  maximum is 0.783), and C3 is a different control; and the "OVERALL PASS" banner encodes a substantive negative (A3).
- **All six [RHW4-fix] binding fixes of REVIEW_HW_S4 were really applied**, struck not deleted, each tagged. I checked each
  one at its line. One of them (SL-1) is then silently superseded by §32 (S5-21).
- **Tally: I confirm 1 new counted item ([HW-11]), total 9**, as HW claims — but as an *implication*, with the hypothesis
  (E2^𝔉) now carrying more weight than the implication removes.

---

## Part 1. Provenance, process, and the binding rules

### S5-1 (CONFIRMED): §29's pre-statement is byte-identical to the log's record
- HW_LOG l.131-133 records: at 11:11:57 UTC HW.md became 138298 bytes (was 134603), md5 `34669466…`; l.157-158 records the
  §29 block ("from `\n---\n# Session 5 of lane H` to the end of the §29 append") as 3695 bytes, md5 `7830e9f0…`.
- I did not take the log's word for the block boundary. I hashed every window of every length in 3693…3697 bytes over the
  whole file and found **exactly one** match for the recorded prefix: length 3695 at byte offset 144433, which is precisely
  the offset of `\n---\n# Session 5 of lane H` (HW l.1424-1465). So §29 has not been touched since 11:11:57.
- 138298 − 134603 = 3695 ✓. Bytes before the block today = 144433, so the 11:24-11:29 in-place [RHW4-fix] edits added
  9830 bytes to §0-§28 — consistent with the log and with 144433 − 134603.
- HW.md's md5 today is `1f0a6b378b99…`, exactly the log's l.158 `1f0a6b37…`. Nothing has changed since the log closed.
- REVIEW_HW_S4.md's md5 is `72c02d80…`, exactly what l.1427 declares binding. The binding document is the real one.
- w5_stderr.txt independently corroborates §31's resource line (1.72 s real, 43859968 B peak RSS = 44 MB); w5_time.txt
  shows one `lock acquired 11:34:05 / exit 0 / lock released 11:34:07`, one acquisition and one release, load 2.54. No
  pkill, nothing left running.

### S5-2 (NOT-VERIFIED, and the reason is not the session's fault): "criteria before script" cannot be checked here
- Every file in this worktree has mtime 2026-10-28 08:03:19 (checkout), including w5_criteria.md, w5_crc2t.py, w5_out.txt,
  HW.md and HW_LOG.md. REVIEW_HW_S4 could check mtimes against the log (its Priority 1); **I cannot**.
- The claim (criteria 11:32:52, script 11:33:48) therefore rests on HW_LOG l.149-151 alone, plus content consistency: the
  criteria do read like a specification of the script rather than a transcript of it (e.g. criteria A2's `n_sharp :=
  max(ceil(...) − 1, 2e87)` is implemented as `nsh = max(mp.ceil(nT) − 1, mp.mpf('2e87'))`, w5_crc2t.py l.35, and B's
  sampler description l.22-23 matches l.81-97).
- The disclosed pre-script edit of B3 ("an unfinished alternative wording … removed", criteria l.29) is honestly flagged.
- *Verdict:* NOT-VERIFIED, no adverse inference. Future sessions should record a hash of the criteria file in HW_LOG, as
  the session already does for HW.md blocks; that survives a checkout and a byte count does not.

### S5-3 (CONFIRMED as a RULE BREACH; binding): the w5 criteria contain same-session constants
- The brief's binding rule 2: "Criteria may contain no constant derived in the same session."
- checks/w5_criteria.md l.8-12 defines its PASS conditions in terms of **b_n := 531441*38418*c_+ + 38417*c_U**,
  **b_D := 38416*(531441*c_+ + c_U)** and **c_att = 1 + 153664*8** — all three first derived in §30.4 (l.1549-1550) and
  §30.2 (l.1501), i.e. **in this session**, at 11:30-11:31, before the criteria at 11:32. HW_LOG l.150-151 states this
  plainly: "The criteria's constants (b_n, b_D, c_att, ρ = 8) come from §30, written before them." It is disclosed and
  then not labelled a breach.
- The consequence is not cosmetic. Criterion **A1**'s band is `[4.0e-97, 5.5e-97]` with the parenthesis "(the hand value of
  §30.6: 4.9e-97/c_+)" (criteria l.10); **A4**'s band `[5e96, 2e97]` brackets §30.6's hand value 1.0·10⁹⁷; **A5**'s band
  `[1.0e-97, 2.0e-97]` brackets §30.6's 1.6·10⁻⁹⁷. All three bands were drawn **around answers already computed by hand in
  §30.6**. A1, A4 and A5 therefore test only that the script reproduces §30.6's hand arithmetic. That is a useful thing to
  test — but it is a *reproduction* check, and §31's "A (arithmetic, 50-digit)" and §33's "Check w5: OVERALL PASS" present
  it as a pre-registered verdict.
- A2 and A3 are genuinely informative: A3 (the behaviour at g_K² = 10⁻⁹⁴) could not have been read off §30.6's band logic.
- This is REVIEW_HW_S4's P-3 pattern (criterion C tautological) recurring one session later, now in a stronger form,
  because this time it is the headline constant.
- *Fix:* say in §31 that A1, A4 and A5 are reproduction checks of §30.6's hand arithmetic and that the criteria breach
  rule 2; keep the criteria file frozen.

---

## Part 2. §30.1: the column-relaxed family and Theorem LI^U-0′

### S5-4 (CONFIRMED): the family 𝔉_𝔥 is well-defined and closed under exactly the operations the proof uses
- l.1477: 𝔉_𝔥 := {R^{−𝒞} : 𝒞 finite, upward closed}, E = ∅. I checked the three closure facts the proof needs:
  - [𝒟] (closed column of a set of cubes) is upward closed ✓;
  - Col(Y) (open column) is upward closed ✓;
  - the relaxed set of the telescoping intermediate R_{t−1} is upward closed (step (1)) — see S5-5.
- One pedantic gap, harmless: a pair (m+1, π(x)) in the upward closure of 𝒞 need not lie in S(𝔥) at all, so 𝒞 ∪ {…} is not
  literally upward closed as a set of pairs. It is immaterial because R_{S(𝔥)∖𝒞} = R_{S(𝔥)∖(𝒞 ∪ anything off S(𝔥))}: one may
  always replace 𝒞 by its upward closure without changing R. Say so in one clause.
- l.1478's chain Z(R) ≥ Z(R(𝔥)) ≥ Z(∅) > 0 is right (R(∅) is the most constrained pattern, Z(R(∅)) = Z(∅) by RX (iii), as
  REL-boot already used).
- Minor: l.1483-1484 defines Z^F(R) := ∫W·F_<·1_R but never says Z^F(R) > 0. With F_< ≥ 1 (the application: Φ ∈ [1, e^{θπ}])
  it is automatic; with the stated "F_< ≥ 0 bounded" it is not. Add "F_< ≥ 0 bounded with Z^F(∅) > 0".

### S5-5 (CONFIRMED): Theorem LI^U-0′ is the right one-change extension, and it is the fix REVIEW_HW_S4 CR-1 demanded
- l.1486-1493. I re-derived both changed steps against REVIEW_HW_S4's confirmation of Theorem LI^U-0:
  - *Constraints.* 1_{R,m} reads U_m only on links interior to cubes of S_R^{(m)}; FP (ii) puts a footprint link interior to
    a level-m cube inside π^{m−k}(x) for an endpoint cube x; R-freeness of x gives (m, π^{m−k}(x)) ∉ S_R. CORRECT. The
    substitution of "x is R-free" for LI^U-0's persistence argument is exactly the right move: R-freeness is *defined* as
    the conclusion persistence was used to produce (l.1481-1482).
  - *Spectators.* Excluded by hypothesis (FP (iii)) rather than by (A2). CORRECT, and this is the step REVIEW_HW_S4 CR-1
    said must change. The hypothesis is stated in the only usable forms (F ≡ 1, or spectators off the relaxed columns).
- The parenthesis at l.1494 recovers Theorem LI^U-0 as the special case R = R(𝔥), π(x) ∈ A_{k+1}(𝔥). CORRECT.
- Where the proof uses it (step (5), l.1583) it needs **both** R''-freeness of 𝒟's cubes (for h^{R'',1}_m) **and**
  (m, x) ∉ S_{R''} (for 1_{R'',m}). Both hold because R' relaxes the *closed* column [𝒟], not the open one. The text says
  this at l.1572 ("In R′, every cube of 𝒟 is unconstrained at levels ≥ m") — correct, but the distinction between "R-free"
  (open column) and "unconstrained at level m" is load-bearing and is nowhere stated as such. Add one sentence.

---

## Part 3. §30.2: the two geometric lemmas

### S5-6 (CONFIRMED): Lemma SH-att is correct, and its constants are right as arithmetic
I re-derived every step of l.1498-1510.
- Forest construction, trees τ_i with one anchor z_i ∈ P, Σ|Y_i| = |Y|, Euclidean length ℓ_i ≤ 2ρ|Y_i| in d = 4 ✓.
- Case (a) (ℓ_iL^{−r} < 1): π^r(Y_i) ⊂ N_1(π^r(z_i)); H-geo (i) gives sh ⊂ N_3(π^r(·)); N_3(N_1(·)) = N_4(·);
  π^r(P) ⊂ sh_{j+r}(P). Since sh commutes with unions, **all** case-(a) trees at a given level are jointly inside
  N_4(sh_{j+r}(P)), so the factor |N_4(X)| ≤ 9⁴|X| = 6561 appears once per level, not once per tree. CORRECT — and this is
  the step that converts a would-be depth term into a multiple of ‖P‖_sh. The 6561 is **load-bearing**, not decorative.
- Case (b) (r ≤ r_i := ⌊log_Lℓ_i⌋): CE-geo′ (g1′) gives |π^r(Y_i)| ≤ 16 + 32ℓ_iL^{−r}; ×2401 = 7⁴ for N_3;
  Σ_{r≥1} 2401·32ℓ_iL^{−r} = 2401·32ℓ_i/(L−1) = 2401·16ℓ_i at L = 3; r_i ≤ ℓ_i; ℓ_i ≤ 2ρ|Y_i|; total 2401·64ρ|Y| ✓.
  c_att(ρ) = 1 + 153664ρ with 153664 = 2401·64 ✓, c_att(8) = 1229313 ✓ (I recomputed).
- The "Reading" at l.1511-1513 is the right diagnosis and matches B3 (see S5-24).

### S5-7 (CONFIRMED): Lemma COL and the b_n / b_D bookkeeping
- HIST l.489-492 H-geo (iv): Σ_{m=0}^{M}|sh_{j+m}(𝒟)| ≤ 38417n + 38416M, with 38416 = 2401·16 = 14⁴ ✓.
- |[𝒟] ∩ S_R| ≤ Σ_{r=0}^{K−1−m}|π^r(𝒟)| ≤ Σ|sh_{m+r}(𝒟)| ≤ 38417n + 38416(K−1−m) ✓ (π^r ⊂ Σ^r).
- ‖col 𝒟‖_sh ≤ 81n + 81(38417n + 38416(K−1−m)) = 81[38418n + 38416(K−1−m)] ✓ via Lemma SL (reviewer-proven in S4) with
  𝒰_{k+1} ↔ 𝒟.
- Composing with SH-att's 6561: the n-coefficient is 531441·38418·c_+ and the depth coefficient 531441·38416·c_+; adding
  step (3)'s own c_U(38417n + 38416(K−1−m)) gives exactly **b_n = 531441·38418c_+ + 38417c_U** and
  **b_D = 38416(531441c_+ + c_U)** ✓. I recomputed the integers: b_n(c_A = 0) = 20416938755,
  b_D(c_A = 0) = 20415875872, both equal to §31's printed values and to the script's.
- 𝒟 is *-connected (step (2)), which H-geo requires. ✓

---

## Part 4. Theorem CRC-2T (l.1554-1604): the headline. I could not break it.

This is the part the brief asked to attack hardest. I walked every step and looked for the standard failure modes.

### S5-8 (CONFIRMED): the induction is well-founded and strictly decreasing
- The induction is on N(R) := |S_R| ∈ ℕ, over all R ∈ 𝔉_𝔥 at fixed (𝔥, T, K), with a **fixed** constant c_U.
- Base: #_R(𝒞′) = 0 ⇒ R^{−𝒞′} = R ⇒ ρ = 1, which covers N(R) = 0 ✓.
- Inner uses, each at strictly smaller N:
  - step (1): N(R_{t−1}) ≤ N(R) − 1 because (m_t, x_t) ∈ S_R is relaxed in R_{t−1} and S_{R_{t−1}} ⊂ S_R ✓;
  - step (3): the hypothesis at R_{t−1} with 𝒞′ = [𝒟] ✓;
  - step (4): the hypothesis at R′ = R_{t−1}^{−[𝒟]}, N(R′) ≤ N(R_{t−1}) < N(R) ✓.
- The claim for R itself is never used in bounding p_t. **So V-F4 (a nonlinear bootstrap needing an a-priori value of a
  supremum) is genuinely absent**, and l.1598-1601's defence of this is correct. This was REVIEW_HW_S4's stated reason why
  REL-boot's device "does not transfer as set up" (S4 Priority 6); the session found the right replacement — induct on the
  finite number of constrained pairs instead of on a sup over (𝔥, B). That is the real idea of the session.
- Upward-closedness of R_{t−1}'s relaxed set: the remaining pairs {(m_s, x_s) : s ≥ t} are the coarser part of 𝒞′ because
  the list is level-ascending and a parent has strictly larger level, hence a strictly later index ✓ (modulo S5-4's
  pedantic gap).

### S5-9 (CONFIRMED): the exact identities and the step event
- ρ^F_R(𝒞′) = Π_t Z^F(R_{t−1})/Z^F(R_t) = Π_t[1 − p_t]^{−1} with p_t = μ^F_{R_{t−1}}(R_{t−1}∖R_t): exact, since R_t ⊂ R_{t−1}
  gives Z^F(R_t) = Z^F(R_{t−1})(1 − p_t) ✓.
- Step (2): if a *-component C of D_{m_t} ∩ S^{(m_t)}_{R_t} with > n_♯ cubes omitted x_t, then C ⊂ S^{(m_t)}_{R_{t−1}} and the
  configuration would already violate R_{t−1}. So x_t ∈ C and C contains a *-connected 𝒟 ∋ x_t of exactly n_♯ + 1 cubes;
  the count 6400^{n_♯} is (g3) ✓. This is REL-seq step (2) verbatim as claimed.
- Steps (3) and (4): the two relaxation inequalities 1_{R_{t−1}} ≤ 1_{R′} ≤ 1_{R''} and the ratio identity
  μ^F_{R}(E) ≤ ρ^F_{R}(𝒞′)·μ^F_{R^{−𝒞′}}(E) are both exact ✓.
- Step (4)'s event bookkeeping, which is the delicate part, is **correct**: on {Y(c) = Y}, every y ∈ Y has its open column
  relaxed in R'' = R′^{−Col(Y)} and is therefore R''-free, so Y ∩ Buf^{R''}_ρ = ∅; and every b ∉ Y that is not R''-free is
  also not R′-free, hence by maximality of the ρ-chained cluster b ∉ D_{m−1}. Therefore
  {Y(c) = Y} ⊂ E_Y = {Y ⊂ D_{m−1}} ∩ {Buf^{R''}_ρ(col 𝒟 ∪ Y) ∩ D_{m−1} = ∅} ✓, and E_Y is a function of U_{m−1} ✓
  (bad-only, history-independent D). Y and col(𝒟) are disjoint by construction (col 𝒟 is R′-free, Y is not) ✓.
- #_{R′}(Col Y) ≤ Σ_{r≥1}|π^r(Y)| ≤ ‖col 𝒟 ∪ Y‖_sh ✓.

### S5-10 (CONFIRMED): the collar sum in step (6) is the two-species criterion, and it is verified
- x := C_Ae^{−a_Au_{m−1}}e^{c_+c_att} ≤ x_* via u_{m−1} ≥ u_K − R (take j = m−1, m = K in (F_R) lower half) ✓.
- Σ_Y x^{|Y|} ≤ Π_{b∈N_ρ(col 𝒟)}(1 + Σ_{Y′∋b}x^{|Y′|}): each ρ-component of Y has at least one cube within ρ of col(𝒟) and
  distinct components get distinct anchors, so the map Y ↦ (anchors, components) is injective into the product's expansion,
  whose terms are all ≥ 0. The inequality direction is right (it over-counts) ✓.
- Σ_{Y′∋b}x^{|Y′|} ≤ Σ_{s≥1}Δ_ρ^{2(s−1)}x^s = x/(1 − Δ_ρ²x) ≤ 2x under **(S1)** ✓. **This is precisely the species-1
  (far-defect) convergence criterion**, of the standard Δ²z ≤ ½ form, with Δ_ρ the ρ-connectivity degree. It is verified.
- |N_ρ(col 𝒟)| ≤ 81n(2ρ+1)⁴ ✓, and 162(2ρ+1)⁴x ≤ Δ_ρ²x·162(2ρ+1)⁴/Δ_ρ² ≤ ½·162/(2ρ+1)⁴ = 0.00097 ≤ log 2 ✓ (I checked
  the arithmetic: 162/17⁴ = 1.94·10⁻³). So Σ_Y x^{|Y|} ≤ 2^n ✓.
- **The cross-species term in the other direction** (a far defect spawning further animals through its own relaxed column)
  is paid in step (4) by ρ^F_{R′}(Col Y) ≤ e^{c_U‖·‖_sh}, i.e. **by the induction's own constant**, and closed by
  2ε_2 ≤ c_U. So both directions of the two-species interaction are accounted for. The brief's "one-species criterion
  applied to a two-species gas" error is not present.
- Step (7): u_m ≥ u_K + β_-(K−m)log L − R gives the factor e^{(K−m)[b_D − naβ_-log L]} ≤ 1 by **(T)** with n = n_♯ + 1 and
  K − m ≥ 1 ✓; and the remainder is exactly ε_2 ✓. Step (8): −log(1 − p) ≤ 2p for p ≤ ½ ✓.
- Step (5) is where (E2^𝔉) and Lemma KS do the work. The peel's claim that the level-m links of int 𝒟 enter only through
  K_{m−1}, 1_{R'',m} and h^{R'',1}_m is right: K_m's contribution *is* h^{R'',1}_m, and LI^U-0′ removes it (S5-5). λ_c =
  6θu_m/u_{m−1} ≤ 6θ(1 + Rg_K²) ≤ λ_* by H5 and u_{m−1} ≥ u_K = 1/g_K² ✓. (Lemma CH, CAP (ii)-(iii), KS (c) and TILT (ii)
  are pre-existing and were confirmed in earlier reviews; I did not re-prove them.)

### S5-8 continued (NARROWED): the "two-type polymer gas" is a description, not an object
- **There is no cluster expansion in §30.** §30.4's species, activities z_1, z_2 and "column/collar linking" are a
  bestiary: no polymer partition function is defined, no compatibility (hard-core) relation is used, no Mayer identity
  appears, and no Kotecký–Preiss criterion is invoked (l.1610 says so: "the KP name is cited for orientation only;
  nothing of it is used"). z_1 appears only as the symbol x in step (6) and z_2 only as the step bound in step (6)-(7).
- Consequently **§29 Target V2 (a) is not met as written**: nowhere is ρ bounded "by the gas's partition-function ratio, or
  by its polymer sum". §33 l.1720's "(a) The gas written" should read "the gas described; the proof is an induction, not an
  expansion, and no gas partition function is constructed".
- This is a presentation finding, not a defect of the mathematics. In fact the induction is **better** than the expansion
  the target asked for, because it needs no polymer representation of 1_R — which REVIEW_HW_S4 Priority 6 identified as
  the real obstruction ("The obstruction is the representation, not convergence"). The session should claim that, instead
  of claiming a gas.
- l.1605-1614's "Relation to Theorem CE / CE-col" is honest and, as far as I can check it, accurate: CE's Steps 1-2 have no
  analogue, the κ_0/κ̃_0 thresholds (3κ_0+3 ≈ 457, κ_0+2κ̃_0+3 ≈ 588 — I checked both from κ_0 = 151.3, κ̃_0 = 217.05) are
  additive constants that b_n ≈ 2·10¹⁰c_+ dwarfs. CONFIRMED.

---

## Part 5. The smallness condition: is it satisfiable at all? (the brief's key question)

### S5-11 (CONFIRMED, and the answer is YES): g²_CRC is a fixed positive number, not a moving target
I traced the g-dependence of every quantity in g²_CRC := a/(b_n + aR + log(12800C_ℓ)).
| quantity | definition / source | g-dependence |
|---|---|---|
| ε_1 | ≲ 6.7·10⁻⁴⁰, an **upper** ceiling from (TH-ch″) (RLARGE l.71-72, REVIEW_SF_S7 C-3) | none; chosen at the ceiling to maximise a_bad |
| a_bad | c_prε_1², c_pr = c_♭/C′² = 5.5625·10⁻⁷ (REVIEW_RLARGE_V3 l.266) ⇒ 2.497·10⁻⁸⁵ | **none** (RLARGE l.613: "Every row is K-independent and g-independent") |
| a = θa_bad | θ < 1/24 from H5, max{6θ,24θ}(1+2Rg_K²) < 1 | H5 **relaxes** as g → 0, so a does not shrink |
| a_A | min{λκε_1²/256, 6θa_bad, a_cd} (PLD l.1416, l.1906) | none; ≥ θa_bad at the recorded κ, λ |
| R | (F_R)'s one-step drift bound | none (a property of the chain) |
| c_att, b_n, b_D, Δ_ρ | pure geometry × c_+ | none |
| C_ℓ, λ_* | λ_* = 6θ(1+2Rg_K²) → 6θ; log C_ℓ ≈ 93-140 + log C_fc | weakly **decreasing** in g_K |
| c_+ = c_A + c_U | c_A = c_cd (PLD l.1856) or 6c_U^{PLD} + c_ns (PLD l.1417), c_U := 1 | none (uncertified, but g-free) |
- The one constraint that ties ε_1 to g runs the *helpful* way: RLARGE_INTEGRATION_LOG l.102 records g² ≪ ε_1²·10⁻¹³, an
  **upper** bound on g given ε_1, i.e. ε_1 is fixed first and g afterwards.
- **Therefore the condition g_K² < g²_CRC ≈ 4.9·10⁻⁹⁷/c_+ is a legitimate, satisfiable smallness condition.** It bounds the
  coarsest (renormalised) coupling g_K uniformly in K and T; nothing recedes as g_0 is lowered. §30.6 l.1641-1642's "It is
  a g-independent ceiling, so the theorem applies with g_0 lowered; nothing is circular" is **CORRECT**, and I could not
  construct any self-defeating feedback. This is the single most consequential thing I can report, and it is good news for
  the session.

### S5-12 (NARROWED; this reverses the session's attribution): (S2) and (T) impose nothing new
Computed in plain-Python `Decimal(prec=120)` (scratchpad `redo_w5A.py`), at c_+ = 1, a = 1.0·10⁻⁸⁶, β_- = 0.186, L = 3:
| condition | source | ceiling / threshold |
|---|---|---|
| **(S2)** g_K² < a/(b_n + aR + log 12800C_ℓ) | HW l.1639 | **4.89789·10⁻⁹⁷** |
| REL-boot r ≤ ½, B_* = c_f + 1 = 531441c_+ + 1 | HW l.1195, l.1710 | **4.89802·10⁻⁹⁷** |
| HIST-sum 6400C_ℓe^{38417B_0}e^{−a/g_K²} ≤ ½, B_0 = 531441c_+ + 2 | HIST l.551 | **4.898·10⁻⁹⁷** |
| **(T)** n_♯ + 1 ≥ b_D/(aβ_-log L) | HW l.1552 | **9.99104·10⁹⁶·c_+** |
| n_H(a, B_0) = ⌊(4 + 38416B_0/log L)/(aβ_-)⌋, B_0 = 531441c_+ | HIST l.550 | **9.99102·10⁹⁶·c_+** |
- The four ceilings agree to four significant figures and the two thresholds agree to five. **(S2) is numerically the same
  inequality as REL-boot's r ≤ ½ and HIST-sum's own smallness condition; (T) is numerically the same threshold as
  n_♯ ≥ n_H(a, B_0).** Both of those are in H8 / H8′ already and were there before this session.
- So **the new cost of session 5 is not (S2) or (T) at all. It is the single factor 6561** that Lemma SH-att's N_4 step puts
  into c_f via Corollary CRC-HW (l.1625: c_f := 531441c_+, where SL-1 had c_f := 81(c_A + c_sf′)). That factor propagates
  into B_*, into B_0, into HIST-sum, into REL-boot and into n_H. At session 4's c_f = 81(c_A + c_sf′) the same REL-boot
  ceiling is **3.214·10⁻⁹³/(c_A + c_sf′)** — i.e. the recorded 10⁻⁹⁴ ceiling was *already* breached for c_A + c_sf′ ≳ 32,
  which, since c_A is uncertified, means the breach was latent in session 4 too.
- §32 l.1709-1712 gets within one sentence of this ("REL-boot's r ≤ ½ … gives the same order of ceiling … and n_H(a, B_0)
  the same order of n_♯"), but §30.6, §33 l.1723-1725 and HANDOFF l.57-59 all present (S2) as the binding new constraint.
  **The diagnosis must be rewritten to localise the whole cost in SH-att's 6561.**
- Two stale comparators in the same paragraph:
  - §30.6 l.1643 compares n_T ≈ 1.0·10⁹⁷c_+ "against n_H ≳ 2·10⁸⁷" and concludes "n_♯ grows by ≈ 10¹⁰". But
    REVIEW_RLARGE_V3 l.274 and l.415 (fix N3-1) already corrected the record: **n_H ≥ 1.810·10⁹¹** once B_0 ≥ 1, because
    "the dominant term is c_B, not 4"; and at HW's own B_0 = 531441c_+ it is 1.0·10⁹⁷c_+. The quoted 2·10⁸⁷ is the
    B_0 → 0 limit and is not a comparator for anything on this route. **WRONG as an attribution.**
  - §30.6 l.1640 says g²_CRC is below "the recorded (RLF-δ) ceiling 10⁻⁹⁴ and the n_H ceiling 2.7·10⁻⁹¹ by a factor
    ≳ 2·10²". I computed the two factors: **204.17** and **5.513·10⁵**. "≳ 2·10²" is true as a lower bound for both but
    hides a difference of 2700×. Give both numbers.

### S5-13 (NARROWED; the session over-reports the damage): the breach does not bind against DX′
- REVIEW_RLARGE_V3 l.61, reviewing exactly this family of ceilings: "The coupling ceiling is g_K² ≲ 2.7·10⁻⁹¹, not
  10⁻⁸⁸. **It still does not bind against DX′.**" REVIEW_SF_S7 l.335 records the binding program ceiling as
  **g_0² ≈ 2.5·10⁻¹⁵²/C_Ω**, and RLARGE l.618 repeats it.
- 4.9·10⁻⁹⁷/c_+ > 2.5·10⁻¹⁵²/C_Ω ⟺ c_+ < 1.96·10⁵⁵·C_Ω. So at the recorded constants **(S2) is slack by about 55 orders of
  magnitude against the ceiling the program already carries, and costs nothing.**
- Neither §30.6, nor §32's "Constants against the record", nor §33, nor HANDOFF l.57-59 mentions DX′. HANDOFF's
  "g_0 therefore has to be lowered. Recheck the downstream constants, including the SF thresholds" is therefore an
  over-reaction that should be withdrawn, and the honest line is: *this route's ceiling tightens by ≈ 2·10² (and n_♯ by
  ≈ 6.6·10³), both of which remain slack against DX′ provided c_+ ≲ 2·10⁵⁵·C_Ω — a proviso that is open only because c_A
  is uncertified (PLD l.1902: c_lcr not certified).*
- *This is not a licence to relax.* The point is the opposite of comfort: the breach is a **bookkeeping** event, and the
  real risk remains that c_A is uncertified. Say which it is.

### S5-14 (CONFIRMED; the cheapest real gain in the lane, and the session waves it away)
§30.6 l.1651-1652: "The size of b_n is pure geometry × allowance … A sharper SH-att or column bound lowers it; **not
needed**." Given S5-12, it is the only thing needed. Two concrete gains:
1. **Free, immediate: 6561 → 2401.** In SH-att case (a), instead of sh_{j+r}(Y_i) ⊂ N_4(π^r(z_i)) ⊂ N_4(sh_{j+r}(P)), use
   sh_{j+r}(P) = Σ^r(P) ⊇ N_1(π^r(P)) (because Σ(X) = N_1(π(X)) ⊇ N_1(π(X)) and Σ^{r}(X) ⊇ N_1(π^r(X)) by induction).
   Then sh_{j+r}(Y_i) ⊂ N_3(π^r(Y_i)) ⊂ N_3(N_1(π^r(P))) ⊂ N_3(sh_{j+r}(P)), so the factor is |N_3| = 7⁴ = 2401, not 9⁴.
   Effect: b_n → 7471609475c_+, **g²_CRC → 1.338·10⁻⁹⁶/c_+** (I computed it), a gain of ×2.73 on both the ceiling and n_♯.
2. **Empirically available: the multiplicative factor may be removable entirely.** The session's own B2 (the "sharper
   excess form" e := ‖P∪Y‖_sh − ‖P‖_sh ≤ c_att|Y|, with **no** 6561) had 0 violations with max 193 per Y-cube. I suspected
   this was an artefact of the shallow M = 10 and tested the obvious adversary (two cubes at ℓ^∞ distance 8 whose
   projections stay at distance 1 for ever, e.g. −1 and +7). It is **not** an artefact: the excess saturates, because
   N_1 ∘ π drives both sets to the same fixed point within two levels. I re-ran B at M = 10, 20, 40 on two seeds (max
   excess per Y-cube 193 and 230, **identical at all three depths**) and an adversarial sampler with |Y| = 8 spread at
   distance exactly ρ in random axis directions at M = 40 (max **257.25**). Against c_att = 1229313 and the 6561.
   - If the sharp form ‖P ∪ Y‖_sh ≤ ‖P‖_sh + c|Y| is provable, b_n → 81·38418c_+ ≈ 3.11·10⁶c_+ and
     **g²_CRC → 3.21·10⁻⁹³/c_+**, i.e. **above the recorded 10⁻⁹⁴ ceiling for c_+ ≤ 32** — the breach the session
     headlines simply disappears.
   - I did **not** prove the sharp form and I am not asserting it: the N_1 ∘ π merging argument wants a lemma of the shape
     "π^r(Y) ⊂ N_1(π^r(P)) ⇒ Σ^{r+c}(P ∪ Y) = Σ^{r+c}(P) for a fixed c", which is plausible from the fixed-point structure
     but is not in HIST §7.2. **That lemma is the highest-value cheap target in this lane**, and it is squarely inside the
     lead's D3 ("the constants are the enemy").

---

## Part 6. (E2^𝔉): what it really asks

### S5-15 (CONFIRMED): the reduction is genuine, not a relabelling
- (E2^𝔉) (l.1524-1530) is a **per-level, local** estimate under each pattern's own past law with its own one weight; (CRC)
  was a **global, multi-level** partition-function ratio. Theorem CRC-2T is 40 lines of real work connecting them. I
  checked that nothing in HW's own steps is R-dependent: steps (3)-(4) use one constant c_U for all patterns, (S1)/(S2)/(T)
  are R-free, SH-att and COL are geometric, LI^U-0′ holds for all R ∈ 𝔉_𝔥. **Within HW, the uniformity is uniform.**
- The monotone structure is favourable and the session does not say so: relaxing constraints raises h pointwise
  (1_{R} ≤ 1_{R^{−𝒞}}), so the family 𝔉_𝔥 is ordered and R(𝔥) is its minimum weight. A node-A proof that does not read the
  detailed hole pattern has a fair chance of being uniform. Worth one sentence in §30.7 as the reason for optimism, since
  §30.7 currently offers none.

### S5-16 (CONFIRMED-WITH-FIX; binding): (E2^𝔉) has three undeclared deltas against what node A states
§30.3 l.1533-1537 names two features honestly (family uniformity; union-form allowance). Three more are not named, and
each is load-bearing:
1. **The allowance form is not PLD's.** PLD's NA-PRICE (l.1408) gives e^{c_A‖S‖_sh} — **S's own** shadow sum — and PLD's
   newest Theorem NA-PRICE^E (i) (l.1856) and §17.6 (l.1904-1906) give e^{c_A s_k(𝔥)} — **the slice**, the very form
   REVIEW_HW_S4 SL-1 found mis-indexed. (E2^𝔉) needs e^{c_A‖col Γ ∪ Y‖_sh} — the **union over the whole attached patch**.
   These are not notational variants: for scattered Y, Σ_y‖{y}‖_sh carries the per-cube depth term 81 + 256(K−j−2) that
   l.1511-1513 and PLD §16.6 (b) identify as unaffordable at a_A ≈ 10⁻⁸⁶, and only attachment to col Γ kills it. **So the
   union form is the real new content of (E2^𝔉), and node A must know that Y is ρ-attached to col Γ.** Say this in H6′.
2. **The level range.** (E2^𝔉) is asked "for every level j ≥ k_0" **and** carries a level-0 clause (l.1530). PLD §17.6
   l.1905 states: "Levels k ≥ 2; k = 1 needs the level-0 analogue of MD (Wilson level, no kernel: (LCR)_0, **OPEN**) and
   is not covered." So H6′ already includes a sub-clause that node A's own lane records as open and uncovered. §32's H6′
   row does not flag the level restriction.
3. **The weight class / F_<.** l.1528's ν := ν^{R,F}_j has a **free, unquantified** F_<. §30.1 l.1483 fixes "F_< a fixed
   bounded weight" and §30.5 l.1630 says node A's input is "asked with the finer spectators inserted". If F_< is
   universally quantified over bounded weights of U_0…U_{k_0−1}, the hypothesis acquires (E1)-like sup strength through the
   back door — the very thing E1-1 says is expected false. The intended class is the specific capped product
   Π_{k′<j}Φ_{k′}; **say so in the statement of (E2^𝔉)**, not only in the prose of §30.5.
- l.1530's level-0 clause is also **ill-formed**: it puts Γ at level 0 and "Y at level 0", but the main clause requires Y
  at level j and Γ at level j+1 with Y outside col(Γ) — at level 0 there is no finer level and col(Γ) is undefined. State
  the level-0 clause with Y = ∅ (or drop col from it).

### S5-17 (NARROWED, in the session's favour): HW's own session-5 doubt about (E2) overshoots
- l.1298-1302 (the [RHW4-fix E2-1] block) records a new doubt: "E1-1's mechanism is not obviously stopped by a good buffer
  [inference, session 5]: bad-only goodness reads only the INTERIOR plaquettes of the buffer cubes, so far curvature can
  sit on the straddling plaquettes between buffer cubes or between the buffer and the column (the LI-pw mechanism)."
- The observation about straddling plaquettes is **correct and important** — it is exactly Proposition LI-pw's device. But
  the inference does not transfer to (E2^𝔉), for a reason the session does not give: **LI-pw is a pointwise statement and
  (E2^𝔉) is an expectation.** LI-pw needs no measure; it exhibits two configurations. (E2^𝔉) bounds
  E_{ν^w}[…] = E_ν[w·…]/E_ν[w] for the **one** weight w = h^{R,1}_j ∈ [0,1], and a buffer configuration carrying O(1)
  straddling holonomy at level j costs level-j action of order u_j = 1/g_j², i.e. has ν-probability e^{−c/g_j²}. The
  measure suppresses precisely the configurations LI-pw constructs. So the LI-pw mechanism is not an obstruction to
  (E2^𝔉), and §24.3's doubt should be narrowed to say so.
- **What is left of the doubt is the real difficulty, and it is a different one:** ν^w(·) ≤ ν(·)/E_ν[w] with
  E_ν[w] = Z^F(R)/Z^F(past), so (E2^𝔉) fails unless conditioning on the coarser constraints costs no volume factor. That
  is a positivity-of-density statement with a boundary allowance — which is exactly what the union-form e^{c_A‖·‖_sh}
  encodes. **State the difficulty in that form** (it is also why the allowance form of S5-16 (1) is the crux), rather than
  as the straddling-plaquette worry.
- Status of this finding: my inference, labelled as such. It makes the route *more* plausible than §24.3 now says, and it
  relocates the burden onto the allowance.

---

## Part 7. Consumption on the HW route (§30.5, §32)

### S5-18 (CONFIRMED): Corollary CRC-HW is a correct implication
- l.1617-1625. The Y-decomposition at level k relative to R(𝔥) is the same device as step (4); col(𝒰_{k+1}) is R(𝔥)-free by
  persistence (π(y) ∈ 𝒰_{k+1} ⊂ A_{k+1}) ✓; h^{R(𝔥)}_k ≤ h^{R(𝔥)^{−Col Y}}_k pointwise ✓; the past law is unchanged because
  Col(Y) touches only levels ≥ k+1, so E_ν[h^{R^{−Col Y}}]/E_ν[h^{R}] = ρ^F_{R(𝔥)}(Col Y) ✓; the Y-sum is step (6) with
  n → |𝒰_{k+1}| ✓; Lemma SL gives Σ_k‖col 𝒰_{k+1}‖_sh ≤ 81Σ_k|𝒰_{k+1}| + 81s(𝔥) ✓. Hence
  C_fc′ = 2C_fc·e^{531441c_+} and c_f = 6561·81·c_+ = 531441c_+ ✓.

### S5-19 (CONFIRMED as a real cost the session under-weighs; binding): the route of record abandons TF-1's benefit
- REVIEW_HW_S4's TF-1 was adopted (l.1244) **and then switched off for the route of record** (l.1250-1253, l.1626-1631):
  the (E2) route uses the **finer-first** order.
- The reason given (l.1626-1629) is correct: in coarse-first order Φ_m reads U_m on the column of a history cube, i.e. on
  int 𝒟, and step (5)'s peel fails.
- But the **cost** is exactly what TF-1 existed to remove. REVIEW_HW_S4 Priority 5: "With HW's finer-first order, node A's
  law ν^{(k)}_k carries the finer capped spectators Φ_{k′<k}. … **no node-A statement is written under such laws**: PLD's
  family ℛ^A_𝔥 has constraint patterns only, and its (SF-cap)^{A,+} allows F only on the columns of A′." So on the route of
  record, node A is being asked for a statement under a law **no PLD statement covers**, which is the mismatch TF-1 fixed.
  §30.5 calls this "the TF-1 caveat" and claims the finer-first law "is the law HW §24.2 originally wrote" — true, but that
  law was the object of the S4 objection, not its resolution.
- *Fix:* say in §30.5 and in H6′ that the finer-first choice **reinstates** the node-A law mismatch TF-1 removed, and that
  TF-1 survives only for the (E1) form, which E1-1 expects false. Together with S5-16 (3) this is one item: name the
  weight class of (E2^𝔉) and say that PLD does not currently state anything under it.

### S5-20 (CONFIRMED): §32's hypothesis list is correct as a list
- H1-H5 unchanged ✓; H6′ = (E2^𝔉) OPEN ✓; H8′ correct ✓; H9 struck with the right justification ("discharged as an
  implication") ✓; the (E1) alternative retained as logically sufficient and expected false ✓; the "No longer hypotheses"
  list correctly includes (CRC) and (CRC-1) **as implications** ✓.
- The one substantive omission: H6′ should carry the three deltas of S5-16 and the law-class note of S5-19.
- Also: Theorem CRC-2T with F ≡ 1 covers the **off-route** consumers §23's table names (RLARGE K8 / EXISTENCE's
  single-cube union bound). §32 does not say so, and should, in one clause — it is free.

### S5-21 (CONFIRMED-WITH-FIX): three symbol collisions, each capable of producing a false circularity
1. **c_f.** SL-1 set c_f := 81(c_A + c_sf′) (l.1273, l.1373); §32 l.1690 sets c_f = 531441c_+ with c_+ = c_A + 2ε_2, and
   **c_sf′ silently disappears** (absorbed into (E2^𝔉)'s single c_A). Say that (E2^𝔉)'s c_A stands for c_A + c_sf′, and
   that §32 supersedes SL-1's value.
2. **C_ℓ.** §30.4 l.1543 defines C_ℓ := (1 − λ_*)^{−3n_int/2}C_fc (unprimed), and ε_2 — hence (S2) — is computed with it.
   §32 l.1690 defines C_ℓ = (1 − λ_*)^{−3n_int/2}C_fc′ with C_fc′ = 2C_fc·e^{531441c_+}. Same symbol, two values. My
   arithmetic used the §30.4 value, which is the one (S2) needs; the difference is additive ≈ 5.3·10⁵c_+ in the log and
   immaterial against b_n ≈ 2.04·10¹⁰c_+, but an integrator feeding the primed C_ℓ into REL-boot's r is doing the right
   thing and feeding it into ε_2 is not.
3. **c_U.** HW's c_U is the (CRC) constant; PLD's c_U is the (LI^U) ratio constant, and PLD l.1417 has
   **c_A = 6c_U + c_ns**. Read with HW's c_U := 1 (the §30.6 input choice) that reads as c_A = 6 + c_ns feeding
   c_+ = c_A + c_U — an apparent circularity. It is not one: PLD's c_U is 0 on this route (Theorem LI^U-0; REVIEW_HW_S4
   X-2) and PLD's own session-5 form is c_A := c_cd (l.1856) with no c_U at all. But §30.6's "Order of constants
   (non-circular)" depends on the reader knowing this, and §30 never says it. **One sentence: "PLD's c_U (the (LI^U)
   constant) is 0 on this route and is a different symbol from HW's (CRC) c_U."**
- Related, minor: §30.6's "c_U^{in} = 1 … c_U^{out} = 2ε_2" is correct but §32 states c_+ = c_A + 2ε_2 (the output) in
  formulas whose derivation used the input value. It is monotone so the bound holds, but say "read c_+ ≤ c_A + 1 wherever
  the derivation needs it".

### S5-22 (CONFIRMED): the [RHW4-fix] fixes, one by one
| S4 binding fix | where applied | verdict |
|---|---|---|
| 1. SL-1 (slice → ‖S‖_sh, Lemma SL, c_f := 81(c_A+c_sf′)) | l.1261-1274 (old text struck `~~…~~`), l.1373 | **APPLIED**, then superseded by §32 without a note (S5-21 (1)) |
| 2. LI0-1 ("exactly absent" → far weight) | l.1132 (struck), l.1142, l.1375-1376 | **APPLIED**, both places |
| 3. LP-1 (k ≤ K−2 fixed depth; "→ 1" not "≥ ½"; x away from ∂π(x); n_♯ cubes *-connected) | l.1152-1157 | **APPLIED**, all four clauses |
| 4. CR-1 (LI^U-0′ for R^{−B}) and CR-2 (top-down analysis ARGUED; S-3/S-4 restricted to (E1)) | l.1175-1177 + §30.1; l.1218-1220, l.1307-1310 | **APPLIED**; CR-1 discharged by a real theorem, not a pointer |
| 5. E1-1 ("expected false in sup form", energetic mechanism, Stokes reading struck) and E2-1 (Buf_k(A) defined; screening named) | l.1286-1292; l.1293-1305 | **APPLIED**; E2-1 goes beyond the fix by adding a new doubt (see S5-17) |
| 6. P-1, P-2 (log + §27 disclosure) | l.1030, l.1072; l.1394-1397 | **APPLIED**; w4b_criteria.md correctly left frozen |
| Recommended: TF-1 | l.1244-1253 | **ADOPTED and then switched off for the route of record** (S5-19) |
| Recommended: RB-1, P-3, (LI^F)/A4 pointer, §22 nit, check (d) fixes | l.1225-1227, l.1398-1401, l.721, l.1142, l.1348 | **APPLIED** |
| Recommended: N_r collar enlargement | l.1304-1305 | declined, with a reason ✓ |
- Append-only discipline respected throughout: I found struck text preserved at l.1132, l.1261-1263, l.1375 and nothing
  deleted. §29 is byte-frozen (S5-1).
- The two cross-lane items (X-1, X-2) were correctly **not** acted on inside HW. But HW.md has **no
  "## FOR OTHER FILES (not edited)" section** (I grepped), although §30.3, §30.7 and §32 all raise demands on PLD/node A
  and on RLARGE (which still contains no occurrence of "CRC" or "(E2^𝔉)" at all — I grepped RLARGE.md). That is the
  brief's rule 8. **Add one.**

---

## Part 8. Check w5, re-derived independently

I re-ran all three parts with my own code, deliberately avoiding the session's toolchain: plain-Python `Decimal` at 120
digits for A (no mpmath), pure-Python sets for B (no numpy), and **exact `Fraction` arithmetic** for C (no floats, no
numpy). No numeric lock was taken and none was needed (exact/symbolic arithmetic, per the brief's rule 6).

### S5-23 (CONFIRMED): Part A reproduces at every scanned point
| quantity | w5_out.txt | my Decimal(120) | verdict |
|---|---|---|---|
| g²_CRC·c_+ | 4.898·10⁻⁹⁷ | 4.89789·10⁻⁹⁷ (c_A = 0), 4.89790·10⁻⁹⁷ (c_A = 1, 100) | **reproduces** (A1) |
| n_T/c_+ | 9.99·10⁹⁶ | 9.99104·10⁹⁶ | **reproduces** (A4) |
| log ε_2 at g²_CRC/2 | −2.04·10¹⁰⁷ | −2.0399·10¹⁰⁷ ≤ log ½ | **reproduces** (A2) |
| log ε_2 at g_K² = 10⁻⁹⁴ | +2.03·10¹⁰⁷ | +2.0299·10¹⁰⁷ > 0 | **reproduces** (A3): (S2) **does** fail there |
| g²_ret·c_+ | 1.63·10⁻⁹⁷ | 1.62689·10⁻⁹⁷ | **reproduces** (A5) |
| b_n(c_A=0), b_D(c_A=0), c_att, Δ_ρ² | 20416938755, 20415875872, 1229313, 6.9756·10⁹ | identical integers | **reproduces** |
- A1-A5 PASS at all 12 scanned (c_A, C_ℓ, R). I also checked §30.6's claim that (S1) follows from (S2) when
  log C_A ≤ log C_ℓ + 2·10¹⁰c_+: correct, using a_A(1/g_K² − R) ≥ a(1/g_K² − R) at g_K² ≤ 1/(2R).
- Two code nits, immaterial to every verdict: `mp.dps = 50` cannot represent `ceil(nT) − 1` or `nsh + 1` at the 10⁹⁷ scale,
  so the script's n_♯ is effectively n_T (an error of 1 part in 10⁹⁷); and §31's "(S2) fails" is tested as `log ε_2 > 0`
  rather than `> log ½` (implied, so harmless). §31's "Exact arithmetic (log space)" should read "50-digit".
- **A3 is the headline, labelled as a control.** A negative control whose PASS *is* the substantive negative result is a
  presentational hazard: §31 l.1668's "**OVERALL PASS (A1-A5, B1-B3, C1-C3)**" is literally true and reads as success.
  §30.6 and §33 do state the failure. *Fix:* add "(A3's PASS records a FAIL of (S2) at the recorded coupling)" to §31's
  OVERALL line.

### S5-24 (CONFIRMED, with a scope addition): Part B reproduces, and I extended it
- B1 (0 violations), B2 (0 violations, max excess per Y-cube 193.0), B3 (detached excess 1106 at M = 5, 2386 at M = 10,
  growth 256/level): **all reproduce exactly** in my own implementation.
- 256 = 4⁴ matches §30.2's reading "81 + 256(K − j − 2)" ✓.
- My addition (post hoc, labelled): the B2 excess is **depth-stable** (193 at M = 10, 20, 40 on the session's seed; 230 on
  another; 257.25 under an adversarial sampler at M = 40), and B3's detached growth stops once the two columns do merge
  (2642 at M = 15), confirming that the construction's 3^{M+2} separation is what keeps it unmerged. §31's "the lemma's
  constant is loose by ≈ 6·10³; informational" is right about c_att but understates: **the multiplicative 6561 also looks
  removable**, which is S5-14.

### S5-25 (CONFIRMED, with two scope defects): Part C reproduces exactly in rational arithmetic
- C1: **0 exceptions** over the 5222 configurations of R^{−B}∖R (exact) ✓. C2: **0 violations** at all 27 grid points
  (exact) ✓. C3: **18 violations** (exactly the 18 points with q′ > q; the 9 points with q′ = q cannot violate, since
  z = q there) ✓.
- The bound is genuinely **tight**, which §31 does not say: at (p, q, q′) = (0.02, 0.001, 0.001) the exact ratio is
  1.0000019970 against the bound 1.0000020000 — the per-step union bound captures the excess to 0.15%. That is good
  evidence that the step-(2) count (2 animals through the site, 6400^{n_♯} in general) is sharp. I verified the bound's
  derivation is legitimate: conditioning on R^{−B} (a decreasing event) can only lower an increasing event, so
  p ≤ 2z² by Harris/FKG. l.1733's "Harris … inside the toy check (not in any proof)" is accurate.
- **Scope defect 1 (binding, undisclosed): §29's promised negative control was never run.** §29 l.1462-1464 pre-registers
  "(ii) … with a negative control (**activities above the stated threshold, where the bound must fail or the expansion
  must diverge**)". No grid point has 2z² ≥ 1: the maximum over the grid is z = 0.6256 at (0.3, 0.1, 0.9), so
  2z² = 0.783 < 1. **The divergence side is untested**, and criteria C3 (dropping the finer contribution) is a *different*
  control. The substitution happened between §29 and the criteria file and is nowhere disclosed. Disclose it, or add two
  grid points with 2z² > 1.
- **Scope defect 2 (as a status note): C does not test the two-species step.** §31's scope line says C "tests the step
  containment and the two-species activity formula". What it tests is z = q + (1−(1−p)³)(q′−q) and the animal count 2. It
  has **no coverage of step (6)** — the collar sum Σ_Y x^{|Y|}, Lemma SH-att, (S1), or Δ_ρ² — which is the only genuinely
  two-species step in the proof. So **(S1)'s convergence has no numerical coverage at all** in w5 beyond the arithmetic of
  A2. Say so in §31's scope line.

---

## Part 9. Corrected tally

| item | HW claim | my verdict |
|---|---|---|
| §29 pre-statement | frozen at 11:11:57, 3695 bytes | **VERIFIED** (hash-search located the exact block, md5 `7830e9f0…`); S5-1 |
| criteria before script | 11:32:52 vs 11:33:48 | **NOT-VERIFIED** (mtimes normalised by checkout); S5-2 |
| w5 criteria | "written BEFORE the script" | **RULE-2 BREACH**: contains b_n, b_D, c_att from §30; A1/A4/A5 are reproduction checks; S5-3 |
| Theorem LI^U-0′ | PROVEN-HERE, counted with [HW-11] | **CONFIRMED**; it is the right discharge of CR-1; S5-5 |
| Lemma SH-att | PROVEN-HERE, uncounted | **CONFIRMED**; constants right; 6561 load-bearing but improvable to 2401 for free, and empirically removable; S5-6, S5-14 |
| Lemma COL | PROVEN-BY-REVIEW + H-geo, uncounted | **CONFIRMED**; b_n / b_D bookkeeping exact; S5-7 |
| §30.4 "the two-type gas" | V2 (a) MET, "the gas written" | **NARROWED**: a description, not an object; no gas partition function, no compatibility relation, no expansion; V2 (a) not met as written; S5-8 |
| **Theorem CRC-2T [HW-11]** | CONDITIONAL, implication PROVEN-HERE, counted | **CONFIRMED.** Induction well-founded; identities exact; (S1) is the species-1 criterion and both cross-species directions are handled; no one-species/two-species error; V-F1…V-F4 all genuinely avoided; S5-8…S5-10 |
| (S1), (S2), (T) explicit | V2 (c) MET; (S2) binding | CONFIRMED as arithmetic; **NARROWED** as attribution: (S2) ≡ REL-boot's r ≤ ½ ≡ HIST-sum's condition, (T) ≡ n_♯ ≥ n_H(a,B_0), all at the session's own c_f; S5-12 |
| "g-independent ceiling, nothing circular" | l.1641-1642 | **CONFIRMED** — the condition is satisfiable and not self-defeating; this is the brief's key question and the answer is favourable; S5-11 |
| "(S2) FAILS at the recorded ceiling; g_0 must be lowered" | §30.6, §33, HANDOFF | **NARROWED**: true arithmetically, but the breach does not bind against DX′ (g_0² ≲ 2.5·10⁻¹⁵²/C_Ω) for c_+ ≲ 2·10⁵⁵C_Ω; HANDOFF's "recheck the SF thresholds" should be withdrawn; S5-13 |
| "n_♯ grows by ≈ 10¹⁰" against n_H ≳ 2·10⁸⁷ | l.1643 | **WRONG as an attribution**: n_H ≥ 1.81·10⁹¹ is the reviewed value (REVIEW_RLARGE_V3 N3-1), and at HW's own B_0 it is 1.0·10⁹⁷c_+ ≈ n_T; S5-12 |
| "by a factor ≳ 2·10²" for both ceilings | l.1640 | CONFIRMED-WITH-FIX: 204.17 and 5.513·10⁵; give both; S5-12 |
| Corollary CRC-HW | CONDITIONAL, implication PROVEN-HERE, uncounted | **CONFIRMED**; S5-18 |
| (E2^𝔉) as the residual | "two features, both named" | **CONFIRMED-WITH-FIX**: three further deltas (allowance form ≠ PLD's; level-0 clause PLD records OPEN; free F_<), plus a mis-levelled level-0 clause; S5-16 |
| §24.3's new doubt about (E2)'s screening | [inference, session 5] | **NARROWED**: LI-pw is pointwise, (E2^𝔉) is an expectation; the straddling-plaquette worry does not transfer. The real difficulty is the no-volume-cost conditioning, which the union allowance encodes; S5-17 |
| TF-1 "adopted" | V1 MET, with caveat | **CONFIRMED-WITH-FIX**: on the route of record TF-1 is switched off, reinstating the node-A law mismatch it removed; S5-19 |
| Theorem HW (session-5 form), §32 | CONDITIONAL, H1-H5, H6′, H8′ | **CONFIRMED-WITH-FIX** (S5-16, S5-19, S5-21; add the off-route consumers) |
| six [RHW4-fix] binding fixes | V1 MET | **CONFIRMED**, all six, each tagged, struck not deleted; S5-22 |
| check w5 | OVERALL PASS | **CONFIRMED** — every verdict reproduces in independent exact/120-digit arithmetic; two scope defects (§29's (ii) control never run; no coverage of step (6)); S5-23…S5-25 |
| counted tally | 8 + 1 = 9 | **CONFIRMED** as a count; the counted item is an implication |

---

## (a) Binding fixes for the session owner

1. **[RHW5-fix CST-1] Rewrite §30.6's cost accounting.** State that (S2) is numerically the same inequality as REL-boot's
   r ≤ ½ (B_* = 531441c_+ + 1) and HIST-sum's own condition (HIST l.551), and that (T) is numerically n_♯ ≥ n_H(a, B_0)
   (HIST l.550) at the session's own B_0; both to 4-5 significant figures (4.898·10⁻⁹⁷ and 9.991·10⁹⁶c_+). Conclude that
   **the entire tightening is the ×6561 of SH-att's N_4 entering c_f**, not (S2) or (T).
2. **[RHW5-fix CST-2] Record DX′.** Add to §30.6 and §32: the binding program ceiling is g_0² ≲ 2.5·10⁻¹⁵²/C_Ω
   (REVIEW_SF_S7 l.335; RLARGE l.618; REVIEW_RLARGE_V3 l.61 "It still does not bind against DX′"), so g²_CRC is slack
   against it whenever c_+ ≲ 2·10⁵⁵·C_Ω, and the open risk is that c_A is uncertified (PLD l.1902), not that g_0 must
   move. Correct HANDOFF's "g_0 therefore has to be lowered. Recheck the downstream constants, including the SF
   thresholds" (that is the lead's file, so put it in the new FOR OTHER FILES section).
3. **[RHW5-fix CST-3] Replace the stale n_H comparator** at l.1643: n_H ≥ 1.810·10⁹¹ is the reviewed value
   (REVIEW_RLARGE_V3 Part 4 / fix N3-1), and at HW's own B_0 = 531441c_+ it is 1.0·10⁹⁷c_+. Strike "n_♯ grows by
   ≈ 10¹⁰"; the honest figure is ≈ 6.6·10³ (the c_f jump) against session 4's own value. Give both ceiling factors
   (204.17 and 5.513·10⁵) at l.1640.
4. **[RHW5-fix SH-1] Sharpen Lemma SH-att, and retract "not needed" (l.1652).** (i) Immediately: replace N_4 by N_3 using
   sh_{j+r}(P) ⊇ N_1(π^r(P)), giving 2401 for 6561 and g²_CRC = 1.338·10⁻⁹⁶/c_+. (ii) Record as the lane's cheapest open
   target the sharp form ‖P ∪ Y‖_sh ≤ ‖P‖_sh + c·|Y|, with the evidence: B2's 0 violations, my depth-stability at
   M = 10/20/40/80 and adversarial max 257.25 per Y-cube, and the pay-off g²_CRC → 3.21·10⁻⁹³/c_+ (above the recorded
   10⁻⁹⁴ ceiling for c_+ ≤ 32). State that it is **not proven** and what the missing lemma is (π^r(Y) ⊂ N_1(π^r(P)) ⇒
   Σ^{r+c}(P ∪ Y) = Σ^{r+c}(P) for a fixed c).
5. **[RHW5-fix E2-2] Complete the statement of (E2^𝔉)** (l.1524-1530, and H6′ at l.1699): name the class of F_< (the
   capped product Π_{k′<j}Φ_{k′}, not an arbitrary bounded weight); fix the level-0 clause (Y = ∅ / no col at level 0);
   and declare the three deltas against node A's present statements — the union-form allowance over col Γ ∪ Y (**not**
   PLD's ‖S‖_sh at l.1408 nor the slice s_k(𝔥) at PLD l.1856/l.1906), the levels j ≥ k_0 including j ≤ 1 (PLD l.1905
   covers k ≥ 2 only; (LCR)_0 OPEN), and the family uniformity.
6. **[RHW5-fix TF-2] Weigh the TF-1 reversal** (§30.5, H6′): say that the finer-first order reinstates the node-A law
   mismatch REVIEW_HW_S4 TF-1 removed, i.e. node A is asked for a statement under a law no PLD statement is written for.
7. **[RHW5-fix GAS-1] Downgrade the gas framing.** §30.4 and §33 l.1720: "the gas described"; say plainly that no polymer
   partition function, compatibility relation or cluster expansion is constructed or used, that §29 V2 (a)'s
   "bounded by the gas's partition-function ratio or polymer sum" is **not** delivered, and that the induction is better
   than the expansion asked for because it needs no polymer representation of 1_R.
8. **[RHW5-fix SYM-1] Fix the three symbol collisions** (S5-21): c_f (SL-1's 81(c_A+c_sf′) superseded by §32's 531441c_+,
   with c_sf′ absorbed into c_A); C_ℓ (§30.4 unprimed in ε_2 vs §32 primed); c_U (HW's (CRC) constant vs PLD's (LI^U)
   constant in PLD l.1417's c_A = 6c_U + c_ns — add "PLD's c_U = 0 on this route and is a different symbol").
9. **[RHW5-fix W5-1] Disclose the w5 defects in §31:** that the criteria contain same-session constants (rule-2 breach)
   and that A1/A4/A5 are reproduction checks of §30.6's hand values; that §29's check-(ii) negative control (activities
   above the threshold / divergence) was **never run**, since max 2z² = 0.783, and that C3 is a different control; that C
   has no coverage of step (6), SH-att, (S1) or Δ_ρ²; and that A3's PASS records a FAIL of (S2) at the recorded coupling.
   Record a hash of the criteria file in HW_LOG for future provenance (mtimes do not survive a checkout).
10. **[RHW5-fix SC-1] Add a "## FOR OTHER FILES (not edited)" section** to HW.md (the brief's rule 8) carrying: the H6′
    deltas for PLD/node A; the HANDOFF correction of fix 2; and the fact that RLARGE.md still contains no occurrence of
    "CRC" or "(E2^𝔉)" — its row 10g / critical-path item 1 should be re-labelled from "(CRC-1), a two-species cluster
    expansion" to "(E2^𝔉), good-buffer screening uniform over 𝔉_𝔥, with a union-form allowance".
11. **[RHW5-fix NIT] Small items:** state Z^F(∅) > 0 (l.1484); state that step (5) needs both R''-freeness *and*
    (m, x) ∉ S_{R''} (l.1572); add the WLOG upward-closure clause (S5-4); note that Theorem CRC-2T with F ≡ 1 also serves
    the off-route consumers of §23's table; narrow §24.3's session-5 doubt per S5-17 and replace it by the
    no-volume-cost-conditioning statement.

## (b) My own tally of what session 5 actually adds

**PROVEN-HERE (verified by me, from stated hypotheses, no open input):**
- **Theorem LI^U-0′** — future insensitivity on R-free cubes for every R ∈ 𝔉_𝔥. Discharges REVIEW_HW_S4 CR-1 outright.
- **Lemma SH-att** — attachment removes the per-cube depth term; constants 6561 / c_att(ρ) = 1 + 153664ρ correct.
- **Lemma COL** — column shadows and |[𝒟] ∩ S_R|, from H-geo (iv) + Lemma SL.
- **The implication** "H1-H5 + H8′ + (E2^𝔉) ⇒ (CRC) for every column-relaxed pattern" (Theorem CRC-2T) — the induction
  itself, including the well-foundedness, the exact telescoping, the step containment, and both species' convergence
  criteria. **This is the session's real result and it survives.**
- **Corollary CRC-HW** as an implication, with C_fc′ = 2C_fc e^{531441c_+} and c_f = 531441c_+.
- **The arithmetic of §30.6** (reproduced independently): g²_CRC, n_T, g²_ret, b_n, b_D, c_att, Δ_ρ².

**CONDITIONAL (⇐ one named open input):**
- **(CRC) for all of 𝔉_𝔥, and hence (CRC)_k**, ⇐ (E2^𝔉) [node A]. Counted [HW-11]. Correct as an implication.
- **Theorem HW (session-5 form)** ⇐ H1-H5, H6′ = (E2^𝔉), H8′.
- **(M-f^cap) under μ_{R(𝔥)}** ⇐ (E2^𝔉), via Corollary CRC-HW.

**ARGUED (convincing, identified hole):**
- Nothing new is ARGUED in session 5. (Proposition LI-pw stays ARGUED from session 4, now with LP-1 applied.)
- My own §24.3 narrowing (S5-17: the LI-pw mechanism does not reach the averaged (E2^𝔉)) is ARGUED, mine, and labelled.

**OPEN:**
- **(E2^𝔉)_{θ,ρ}** [node A], with the three undeclared deltas of S5-16 — the single residual of the whole route.
- The sharp form of Lemma SH-att (S5-14) — not needed for correctness, needed for the constants.
- Everything session 4 left open outside HW: (CLS-min) ⇐ (REG-min) [SQ], (F_R) [FLOW], (KS-N), c_A/c_lcr certification.

**NOT ADDED, despite the headline:** a cluster expansion, a polymer gas, a Kotecký–Preiss criterion, or any
partition-function bound of the gas; and any reduction in the program's binding coupling ceiling or in n_♯ (the changes
in both are consequences of SH-att's 6561, not of the theorem).

## (c) May (CRC-1) be treated as discharged for (LI^U)?

**No — but it may be retired as a wall, which is different and is real progress.** Precisely:

1. **(CRC-1), the same-level regress, is DISSOLVED as a logical obstruction.** REVIEW_HW_S4 identified the obstruction as
   "the representation, not convergence", and as the non-closure of the m = k + 1 step of the top-down induction
   (l.1321: "For m = k + 1 it is (CRC)_k itself: the induction does not close"). Theorem CRC-2T closes it, by inducting on
   the number of constrained pairs instead of on the level. I checked this and could not break it. **The wall (CRC-1)
   should be struck from RLARGE's critical path.**
2. **(CRC) itself is NOT discharged.** It is CONDITIONAL on (E2^𝔉), which is strictly stronger than the (E2) it replaces
   (family uniformity; union-form allowance over the whole attached patch; ρ = 8 buffer) and is **not** what node A
   currently states (S5-16: PLD gives the slice form or ‖S‖_sh, for k ≥ 2, under the (E1) "any w" class). Any downstream
   file that writes "(CRC) PROVEN" or treats H9 as closed would be wrong.
3. **For (LI^U) specifically** — RLARGE's #1 critical-path item, which REVIEW_RLARGE_V3 Part 6 defines as "future
   insensitivity, uniform over the relaxed laws" — session 5 is a genuine advance: the pointwise form was already refuted
   (LI-pw, session 4) and the averaged form is now an *implication from a per-level local hypothesis* rather than a
   free-standing global wall. The right re-labelling of the critical-path item is **"(E2^𝔉): good-buffer screening,
   uniform over 𝔉_𝔥, with a union-form allowance over the attached patch and a level-0 clause"** — one node-A statement,
   not a cluster-expansion project.
4. **Net on the hypothesis ledger:** the route traded one HW-owned wall of "cluster-expansion strength" for one
   node-A-owned hypothesis that is a strengthening (in three named ways) of a hypothesis node A already owed. That is a
   favourable trade *if* node A's screening proof is indifferent to which coarser columns are relaxed and can carry the
   union-form allowance. HW is right that nothing in HW decides it. It is now PLD's call, and REVIEW_PLD_S5 should be
   asked the three S5-16 questions explicitly.

## (d) The single biggest live wall in this lane

**The allowance form in (E2^𝔉): node A must be allowed e^{c_A‖col Γ ∪ Y‖_sh} — the union-form shadow sum of the WHOLE
attached patch — and not a per-set or slice allowance.**

This is the crux, not the family uniformity and not the screening heuristic:
- A per-cube or per-set allowance on scattered far defects Y carries the depth term 81 + 256(K − j − 2) per cube
  (l.1511-1513; PLD §16.6 (b); and my own B3 re-derivation, 256 per level), which at a_A ≈ 10⁻⁸⁶ is not affordable at any
  coupling. Only attachment to col Γ removes it, and that is what Lemma SH-att is for.
- Node A's present statements deliver a different form (PLD l.1408 ‖S‖_sh; PLD l.1856 and l.1904-1906 the slice s_k(𝔥)),
  for k ≥ 2 only, and under the (E1) "any w" class that HW's own E1-1 expects to be false. So H6′ is not "a node-A item
  pending labour": it is **a differently-shaped statement that nobody has yet written down**.
- The family uniformity over 𝔉_𝔥, by contrast, has a favourable monotone structure (S5-15) and is the kind of quantifier
  a screening proof usually survives; and the screening heuristic itself is in better shape than §24.3's new doubt says
  (S5-17), because (E2^𝔉) is an expectation under one weight and the measure suppresses the LI-pw configurations at cost
  e^{−c/g_j²}.
- Runner-up, and the one the session should fix itself because it is cheap and it is entirely HW's: **Lemma SH-att's
  6561** (S5-14). It is the sole cause of the ceiling and n_♯ movement that the session headlines, it is provably
  improvable to 2401 in one line, and the evidence that it is removable altogether is already in the session's own
  check B2.

---

## What I could not break (said plainly, since a review that breaks nothing is also a failed review)

- The induction of Theorem CRC-2T. I attacked the well-foundedness (strict decrease of N at every inner use), the
  telescoping identity (exact), step (2)'s containment (I re-derived the component argument), step (4)'s event algebra
  (the three R-freeness / maximality clauses all hold), step (5)'s peel (both the R''-freeness and the
  (m, x) ∉ S_{R''} conditions hold, and LI^U-0′ covers the level-m kernel), step (6)'s Mayer-type factorisation
  (over-counts, so the direction is right) and step (7)'s depth cancellation. Every one holds.
- The two-species question the brief flagged. (S1) *is* the species-1 criterion, in the standard Δ²z ≤ ½ form; the
  cross-species terms appear in exactly two places and both are paid (step (6) folds the collar sum into the animal
  activity as 2^n; step (4) pays the reverse direction with the induction's own c_U, closed by 2ε_2 ≤ c_U). The
  apparent self-consistency (c_U inside b_n inside ε_2 inside 2ε_2 ≤ c_U) is resolved by the fixed choice c_U := 1 and is
  not a fixed-point problem.
- The satisfiability question. I could not make g²_CRC recede: a, a_A, a_bad, ε_1, R, c_att, b_n, b_D and c_A are all
  g-free, and the one ε_1-vs-g constraint on record runs the helpful way. The condition is a genuine, achievable
  smallness condition on the coarse coupling.
- The geometry. SH-att's and COL's constants are arithmetically right (I recomputed every integer), and SH-att's
  multiplicative 6561 is load-bearing against a depth term, not padding — even though it is loose.
- The provenance of §29. I did not take the log's block boundary on trust; a brute-force hash search over all window
  lengths 3693-3697 found exactly one match, at exactly the claimed offset.
- w5. Every one of the eleven verdicts reproduces in arithmetic I wrote myself, with a different toolchain, including
  exact rationals for Part C. The failure it reports (A3) is real and correctly reported as a failure of (S2) at the
  recorded coupling.
