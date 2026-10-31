# REVIEW_SQ_S3: hostile review of lane G session 3 (SQ.md [RSQ2-fix] edits, §T3, §13-§14, check q4)

Reviewer: an independent agent. I wrote none of SQ.md, SQ_LOG.md or the checks, and I edited no file except this one. No
commits, PRs or pushes.

Inputs (read-only):
- SQ.md l.136-142 (Σ_dec), l.143-182 (constants, E2, BCH-p), l.286-345, l.655-666, l.745-772, l.799-942 (every [RSQ2-fix]),
  l.953-1216 (§T3, §13, §14).
- SQ_LOG.md (session 3 entries, l.96-134).
- REVIEW_SQ_S2.md (all; format and fix list).
- checks/q4_criteria.md, q4_kernel_ids.py, q4_out.txt, q4_time.txt; the author's post-hoc copy in the scratchpad
  (q4run/q4_diag.py, diag_out.txt).
- BFT_B.md l.236-241 (scope of BFT's box clause), l.2501-2545 (Theorem RH, NF-uniq, NF-cov, REF/(N1-bd), NF-ex).
- RLARGE.md v3 §2.1-§3.2 (l.281-380: defects, FV, where (CLS-min) prices the coherent background).
- PROOF.md l.5435-5460 (Theorem N5-sf0), l.5814-5821 (Lemma LOC), l.5926-5930 (N5-sf_i (b)); grep of PROOF for
  "non-wrapping", "Neumann", "Dirichlet".
- REVIEW_S22.md l.396-401 (BFT claim text).

Scratch work is in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/rsq3/`:
- q4_copy.py: q4 verbatim (SHA-1 902df641…, identical to checks/q4_kernel_ids.py);
- rv3.py: the reviewer's checks R1-R3 (written independently; only the data model of q4 is reused);
- run.sh, lock_log.txt and all outputs.

Line numbers are SQ.md's unless another file is named.

---

## Bottom line

- **Provenance is clean.**
  - §T3 precedes Step 1, the criteria precede the script, and the run precedes §13. The 98 422-byte figure is consistent
    but only self-reported.
  - One pre-statement formula (tr|M| in §T3) was silently corrected (M3-1).
  - The [RSQ2-fix] edits are complete except one scope tag (M3-2).
  - **S2-5 is CONFIRMED and sharpened.** PROOF's "non-wrapping boxes" are gauge charts inside a torus, and BFT_B l.240 itself
    says the box clause is unproven (S3-1).
- **The counted proofs are correct.**
  - Lemma CC-NA, Lemma RT-NA + Proposition RES-dec, and Lemma STOKES-NA + Corollary STOKES-it are CONFIRMED (re-derived;
    identities checked numerically in R2-R3), with minor fixes only.
  - RES-dec is a real advance: residual decay with exponent > 2 on the whole τ-small class, with no bootstrap.
  - Theorem RED-0 is a correct implication but a corollary, so it should not be counted. The tally is **11 / 3 / 2, not
    12 / 3 / 2** (S3-3).
- **(EPS-0) and bubbling.**
  - (EPS-0) is expected TRUE deterministically.
  - τ-small cone minimisers have energy ≲ θ² ≪ ε_0 at every scale, and plaquettes deep in Lüscher's admissible sector. So no
    instanton, dislocation or bubble exists in the hypothesis class.
  - §13.6's large branch is an artefact of using the supercritical sup norm. "G6-F4 OCCURS" overclaims (S3-5).
  - §13.6's (b1) is WRONG as stated: on the lattice the Bianchi-defect term is a critical potential, small in ℓ² (S3-4).
- **The proposed defect architecture is not the fix.**
  - Real bubbles are already priced by RLARGE.
  - The leftover concentrated configurations have action ≲ θ², so no e^{-8π²/g²} price applies.
  - Restricting the domain is either vacuous (critical sense) or circular (scale-weighted sense).
  - The restricted (EPS-0) is not automatic. It is (EPS-0a) single-level ε-regularity (standard in structure) plus
    **(EPS-0b) the critical source bound n³sup|𝒮| ≤ Cθ, which is the real wall** (S3-6).
- **q4.**
  - The FAIL re-runs identically and stands.
  - Its cause is the BFGS maximiser's first-order error (3·10⁻⁸), not finite-difference noise. With a Newton W_0, K3 passes
    at 2.5·10⁻¹⁰ (S3-8).

---

## Priority 1. Provenance, [RSQ2-fix] edits, S2-5

### Order (clean, with one unflagged pre-statement change)
- File times match the log: q4_criteria.md 06:16:34 EDT (10:16:34 UTC), q4_kernel_ids.py 06:17:12, q4_out/q4_time 06:17:57;
  SQ.md 06:27:08, SQ_LOG.md 06:27:42. The criteria precede the script, the script precedes the run, and the run precedes §13
  (§13's own header says so). The one pre-run script edit (SU(3) count 5 → 20, to match the criteria) is disclosed.
- **The 98 422-byte claim for SQ.md at the §T3 append is consistent but not independently verifiable** (SQ.md is untracked;
  no pre-session snapshot exists). Check: today l.1-952 are 101 334 bytes and §T3 is 4 719 bytes; the [RSQ2-fix] insertions
  that I can delimit total ≈ 7.2 kB, against the ≈ 7.6 kB implied by 98 422 bytes (the gap is inline tags my delimiter
  missed, e.g. l.747-748). The claim stands as a self-report.
- **§T3 vs §13 drift.** Disclosed in the log: RES-dec "critical point" → "minimiser"; STOKES-NA's form; C_q, τ_*, C_r. Not
  disclosed: §T3 l.966 writes the kernel as φ_M(V) = N⁻¹(tr|M| - Re tr(V⁻¹M)). tr|M| is the **U(N)** maximum of
  Re tr(W⁻¹M); for SU(N) it equals the §13.0 form only when the polar factor has determinant 1 (always for SU(2), where M is a
  real multiple of an SU(2) element; not for SU(3)). §13.0 silently uses the right (SU(N), W_0) form. **M3-1:** note the
  correction under §13.0. Not load-bearing.

### The [RSQ2-fix] edits: all present, tagged, original text kept
S2-1a/b (l.288-292), M2-1 (l.344-345), S2-2 (l.663 inline; l.762-771 item (1)), M2-3 (l.747-748), S2-3/M2-4 (l.762-771 items
(2)-(3); l.879-883 (𝔑's residual weight); l.931-932), S2-4a-d with M2-2 (l.801-804, l.827-842), M2-5/S2-6 (l.852-855),
M2-6 (l.869-872), S2-6 (l.896-901, l.936-938), S2-5 (l.902-910). Each says what REVIEW_SQ_S2 asked. One gap:
- **M3-2 (S2-3 scope, incomplete).** The "Answer to Q3" (l.825-826) still says "loses NOTHING for residual sources at any
  level"; S2-3 asked for the paired-source scope there too (REVIEW_SQ_S2 l.261). (vi') at l.841 corrects only the
  level-0 half. **Fix:** add "(paired energy-residual sources; S2-3)" after "at any level".

### S2-5 (the box clause): SQ's reading is CORRECT, and stronger than SQ states
- PROOF l.5443-5460 (N5-sf0): T ≥ T_0 is a **torus** hypothesis; the background classes 𝔑(α) are local real gauges g_□ on
  Ω^+_□ inside the torus. I widened the search to every "non-wrapping box" in PROOF. Each one (Lemma LOC l.5818, N5-sf_i (b)
  l.5928, l.6318) is a **gauge-chart region inside a torus problem** (an AX gauge on a box that does not wrap). None is a
  free/Neumann boundary for the field. (PROOF's Neumann objects, l.1015, 1109, 2502, 2743, 5210, are block Poincaré
  inequalities and the like, not a field boundary condition.)
- **BFT_B l.240 settles it from lane A's own side:** "Proven on tori T ≥ T_0 only; BFT's 'every non-wrapping box with the
  boundary convention of N5-sf0' clause is not covered here."
- **Fix S3-1 (wording, l.902-910):** delete "checked on a limited reading … lane A should confirm". Read instead: "The
  N5-sf0 convention is a gauge-chart convention inside a torus (PROOF l.5443-5460, l.5818, l.5928). BFT_B l.240 records
  that the box clause is not proven. So the free-boundary cone-box clause is genuinely missing, not merely unread (§13.8
  item (3) stands)."

**Verdict P1: provenance clean (one self-report not verifiable; one unflagged §T3 formula change, M3-1). Step 1 DONE except
M3-2. S2-5 CONFIRMED and sharpened (S3-1).**

---

## Priority 2. The four counted items

### Lemma K (l.1014-1030): CONFIRMED (not counted, correctly)
I re-derived (a)-(e).
- (a): Re tr((aWb)⁻¹aMb) = Re tr(W⁻¹M), so the maximum value is bi-invariant. Uniqueness of the maximiser is not needed.
- (b): the envelope step needs a **unique** maximiser. That holds near SU(N) (Lemma PM's regime) but not at every M.
- (c): sharper than stated. Re tr(W_0(e^{tμ}M)⁻¹e^{tμ}M) is constant in t, so the left M-gradient of φ is exactly
  N⁻¹Re tr(V⁻¹μM). No envelope theorem and no smoothness are needed. This is why CC-NA needs no smallness.
- (d): stationarity gives A = W_0⁻¹M = H + ic·1 (the anti-Hermitian part of A is central).
  - Re tr((e^{-X} - 1)X) = Σθ_j sin θ_j ≥ |X|²(1 - θ_max²/6), and θ_max²/6 ≤ 0.41x² ≤ x².
  - The A - 1 term is ≤ σ'|X|·||e^{-X} - 1||_HS.
  - Upper bound: ||A||_op ≤ 1 + σ' and ||e^{-X} - 1||_HS ≤ √N·x.
  - Both bounds hold; numerically confirmed in R2 below.
- (e): with U' = V⁻¹W_0:
  - φ = s(U') + N⁻¹tr(Re(1 - U')(H - 1)) + N⁻¹c·Im tr U';
  - |tr(R(H - 1))| ≤ σ'·tr R for R ≥ 0;
  - |Im tr U'| ≤ Σ|θ|³/6;
  - s(U') ≥ x²/(2N).
  - This gives φ ≥ s(U')(1 - 1.3σ'), so the stated (1 - 2σ' - x²) is valid with room.

**M3-3:** add "(maximiser unique; e.g. ||M - S|| < ¼ for some unitary S)" to (b), and therefore to RT-NA's hypotheses. RT-NA
uses (b); CC-NA uses only (c).

### Lemma CC-NA (l.1032-1046): CONFIRMED (PROVEN-HERE; counted)
- **(i) Non-root sites.**
  - The S4' contours T^σ_y = P^σ(c_X → y)S_yP^σ(c_{X'} → y + Le_μ)^† begin and end at roots. So a level-(l+1) gauge at a
    non-root site leaves every M̄_{c'}(U_{l+1}) invariant.
  - No plaquette term lives at level ≥ 1, and U_l is not varied.
  - The variation therefore sees only the kernel terms of the box_{l+1} links at z, with derivative ⟨(D*j_l)(z), μ⟩.
  - The entering-link sign (-Ad_{U⁻¹}j) is the right-gradient rule of §13.0.
- **(ii) Roots.**
  - Outgoing contours start at c_Y (H ↦ e^{tμ}H) and incoming ones end there (H ↦ He^{-tμ}).
  - So M̄_{c'} ↦ e^{tμ}M̄_{c'} or M̄_{c'}e^{-tμ}.
  - With K (c) for left and right gradients, the M-side derivative is exactly -⟨(D*j_{l+1})(Y), μ⟩. I checked the signs of
    both conversions (R3).
  - Other links' contours stay inside their own endpoint blocks and do not pass through c_Y.
- **(iii) Top.**
  - The composite gauge (e^{tμ} at c_Y and at every root below it, 1 elsewhere) leaves every term below the top invariant,
    by K (a) at each level with the composite rule of F6.
  - V is fixed, so only the top kernel terms move, and stationarity in U_{<k} gives (D*j_{k-1})(Y) = 0.
- **(iv)** The downward induction is correct, and the free boundary is respected (D* sums box links only).
- "No smallness": correct (only K (c) is used).
- **M3-4 (wording only).** A contour can pass through a root in its interior. Example: a funnel that leaves c_Y in the −μ
  direction, followed by S_y running back through c_Y. An interior visit contributes e^{-tμ}e^{tμ} = 1, so (i)-(ii) are
  unaffected. Say "interior visits of a contour to the gauged site cancel; only endpoints count" in place of "(the two
  factors at z cancel)".

### Lemma RT-NA and Proposition RES-dec (l.1048-1096): CONFIRMED (PROVEN-HERE; counted as one item), with three precision fixes
**RT-NA.**
- U(b) ↦ e^{tμ}U(b) gives H_T ↦ Ad_{Q_T}(e^{ε_Ttμ})H_T, with the backward prefix (prefix)·U(b)⁻¹. This is checked by finite
  differences on a backward traversal in R3.
- The M̄-part of K (b) is ⟨∇^L_Mφ, Ad_Qμ⟩ = -κ_{l+1}⁻¹⟨j_{l+1}, Ad_Qμ⟩. The (H_T - M̄)-part is e_l.
- The EL sum is the identity. G6-F1 does not occur: the spread enters only multiplied by Z ∝ the residual. **Agreed.**
- **M3-5:** "T ∋ b" must count **multiplicity**. An axial funnel ending at y by a −μ step re-traverses the first links of
  S_y backwards, so b can occur twice in one contour. The bounds survive, because the (s) and (f) counts are per
  occurrence.

**The funnel cancellation (l.1061-1074).** I re-derived it.
- For fixed (σ, ŷ), the funnel P^σ(c_Y → ŷ) serves the contour (σ, ŷ) of every outgoing box_{l+2} link at Y, and the contour
  (σ, ŷ - Le_ν) of every incoming one (same σ at both ends, LINEAR_PACKAGE §1.2).
- The outgoing prefix is the funnel segment Q_b. The incoming prefix is A·F_2^†U(b)⁻¹ = H_TF_1 = H_TQ_b, as SQ writes.
- So the (f)-part is Σ_{(σ,ŷ)}(ε_b/(24L⁴))Ad_{Q_b}⁻¹[Σ_out j - Σ_in Ad_{H_T}⁻¹j].
- The bracket is D*j_{l+1}(Y) = 0 up to Σ_in(Ad_{U⁻¹} - Ad_{H_T⁻¹})j, which is ≤ 8·max(x + σ' + σ)·max|j|.
  ||Ad_Aη - Ad_Bη|| ≤ 2||A - B||·|η| holds for unitary A, B.
- (s)-weight: b lies on S_y for exactly L sites y, each carrying 24 σ-contours of weight 1/(24L⁴). So the weight is L⁻³
  exactly. ✓
- Remainder: |Z| ≤ √Nx ≤ 1.1N^{3/2}κ⁻¹|j| (K (d) lower), σ ≤ 2A_df, and the weight is ≤ L⁻³ + 8.
  This gives |e| ≤ 1.1·2·8.04·√NA_df·max|j| = 17.7√NA_df·max|j|. ✓
- **Corollary:** the per-level factor L⁻³ + 8(x + 6A_df) + 17.7√NA_df is correct (σ + σ' ≤ 6A_df by RS (R1) and PM).

**RES-dec (l.1078-1089).**
- **Constants.** C_q = 8 + 48·9 + 17.7·√2·9 = 665.3 ✓ (A_d = 9 at L = 3, l.143). τ_* = (1/9 - 1/27)/(2·665) = 5.57·10⁻⁵ ✓.
  q ≤ (L⁻² + L⁻³)/2 = 0.0741, so θ_r = log 13.5/log 3 = 2.369 ✓.
- **Step (1).** The competitor U ≡ 1 in a top gauge gives E = κ_{k-1}s(V_P) ≤ κ_+(π²/8)θ² (θ_max ≤ (π/2)θ) ✓. Then
  κ_-φ_c ≤ E, and K (e) gives x_c ≤ (2.2·1.234Nκ̂)^{1/2}θ = 1.65√(Nκ̂)θ ✓.
- **Steps (2)-(3).** These follow by iterating the Corollary under τ-smallness, then K (d) upper at the top and K (d) lower at
  level l: 1.1·1.01·1.65 = 1.83 ≤ 1.9 ✓.
- **No bootstrap: CONFIRMED.**
  - The hypothesis is unweighted sup smallness (< τ at every level).
  - The conclusion is weighted decay with exponent > 2, which strictly dominates (D2)'s exponent 2.
  - No uniqueness, no continuity and no a-priori decay are used.
  - This is the session's genuine advance: the residual half of (REG-min) is unconditional on the τ-small class.
- **Remark (2):** the G6-F2 reading is right. The O(τ) loss is additive per level and comes from the holonomy rotation
  Ad_{H_T}. Abelian: exact L⁻³.
- **M3-6 (stated scope):** RES-dec's "every τ-small minimiser" includes "every cone plaquette below the top < τ" at levels
  ≥ 1. That is a hypothesis, not a consequence. At level 0 it is automatic (||1 - U_0(p)|| ≤ √(2NE) ≤ 1.6√(Nκ_+)θ, M2-1).
  Say so: it is the only place where the sup-smallness of coarse curvature enters, and it is the hook of §13.6's feedback.

### Lemma STOKES-NA and Corollary STOKES-it (l.1098-1122): CONFIRMED (PROVEN-HERE given HIST MSG step (1), E2, BCH-p; counted as one item)
**The chain.**
1. Axial gauge on R_q (2L × 2L × L × L): |a| ≤ m.
2. E2 per link: a_j = Qa - ρ̃ + e.
3. d(Qa)(q) = Σw_pda(p), with w_p ≥ 0 and Σw_p = L².
4. BCH-p at both ends.
5. Collection: L²f̂ + L²C_pm² + 4.044x + 4C_e(m² + 1.011mx) + C_p((p_L + 1)m + 2.03x)².

All five steps check.

**C_S.** At C_p = 34√2, A_ax' = 12.13, C_e = 3790, p_L = 11, the three terms are 6.4·10⁴, 2.65·10⁶ and 1.05·10⁶. So
C_S ≈ 3.77·10⁶ ✓.

**STOKES-it.**
- The three increments sum to ≤ B_0, ≤ G/4 and ≤ G/4 under θ ≤ θ_S. Here qL² ≤ (1 + 1/L)/2 < 1 and q²L² < 1.
- So the induction closes at G = 2(1.011A_0 + B_0) ✓.
- The main coefficient is exactly L² (Q_2's row sum), so there is no per-level excess, and G6-F3 does not occur. **Agreed.**

**Fixes.**
- **M3-7:** "y_c ≤ 1/20" (l.1101) is undefined in §13. Name it (E2's hypothesis from §0.3), or drop it.
- **S3-2 (substantive, for §13.6).** STOKES-NA is stated with f̂ = max over R_q. The linear identity it uses is a Q_2-weighted
  **average**, Σ_p w_p da(p) with Σw = L². That is an ℓ¹ statement, which the max discards. Keep the averaged form as
  Lemma STOKES-NA (avg):
  |log U_j(q)|_op ≤ Σ_p w_p|log U_{j-1}(p)|_op + 4.044x + C_S(f̂ + x)².
  It costs nothing, and it is what §13.6's feedback needs (Priority 3).

### Theorem RED-0 (l.1124-1134): the implication is CONFIRMED; counting it as a separate item is NOT
- (EPS-0) ⟹ (REG-min) composes correctly:
  - τ_R = min{τ_0, τ_*, τ_S, θ_S/C'};
  - FORCE (strict) gives θ < C'τ_R ≤ θ_S;
  - (D1) comes from STOKES-it (|log|_op ≥ ||1 - U||);
  - (D2) comes from RES-dec, since q < L⁻² and the top residual is ≤ 1.65√(Nκ̂)θ ≤ C_rθ.
- The converse is trivial.
- **Tally correction S3-3:** RED-0 is a corollary of the two counted items. One direction is a definition, the other is
  composition. It should not be a fourth counted PROVEN item. Session 3 counts **3** (CC-NA; RT-NA + RES-dec; STOKES-NA +
  STOKES-it), with RED-0 PROVEN as a corollary, uncounted. File tally: **11 / 3 / 2**, not 12 / 3 / 2.
- **Content check (what RED-0 really reduces).** (D1) at levels ≥ 1 from level 0 is Stokes. The real content is RES-dec
  (residuals) plus the observation that the curvature half of (REG-min) is the level-0 sup alone. That is a genuine
  reduction of the target's FORM. It is not a reduction of difficulty. (EPS-0) is the whole critical step (Priority 3), so
  §14's "the wall is (EPS-0)" is right.

**Verdict P2: CC-NA CONFIRMED; RT-NA + RES-dec CONFIRMED (M3-3, M3-5, M3-6); STOKES-NA + STOKES-it CONFIRMED (M3-7; S3-2
recommended); RED-0 CONFIRMED as an implication but uncounted (S3-3). No GAP, no WRONG among the counted proofs.**

---

## Priority 3. (EPS-0) and bubbling: the strategic question

### §13.6 line by line
- **Level-0 equation and source size.**
  - The Wilson EL equation D*_{U_0}𝒫 = 𝒮 with 𝒮 = -(𝒯j_0 - e_{-1}) is correct (RT-NA at l = -1).
  - Under τ-smallness alone, n³sup|𝒮| ≤ Cθ(L³q)^k = Cθ·n^{δ(τ)}, with δ(τ) := log_L(1 + C_qL³τ).
  - Note the size: **δ(τ_*) = log_3(1 + 665·27·5.57·10⁻⁵) = log_3 2.0 = 0.63**, a real power, not a log.
  - The source bound that a box-scale estimate needs is n³sup|𝒮| ≤ Cθ, i.e. a level-0 residual exponent of exactly 3 (the
    critical value; see "Coupling" below).
- **Lattice Kato: CONFIRMED** (Cauchy-Schwarz: ⟨û, u - Ad_Uu'⟩ ≥ |u| - |u'|; no smallness). Trivial; correctly uncounted.
- **(b1) is NOT an obstruction on the lattice; SQ's "supercritical at scale n" is WRONG (S3-4).**
  - The Bianchi defect D𝒫 is O(|𝒫|²) pointwise (BCH of the transported face holonomies).
  - A lattice difference is bounded by neighbouring values, so |D*(D𝒫)(x)| ≤ C·(M|𝒫|)(x)², M the neighbour maximum.
  - The term is therefore a **potential** term V·(M|𝒫|) with V = CM|𝒫|, and Σ_{box}V² ≤ C'E ≤ C''θ²: small in the
    critical norm ℓ² (= L^{d/2}).
  - Even read as a drift with coefficient |𝒫|, its critical norm is ℓ⁴ (= L^d), and on the lattice
    ||𝒫||_{ℓ⁴} ≤ ||𝒫||_{ℓ²} ≤ √(2NE): small.
  - The quantity "|𝒫| ≤ τ in lattice units" is a supercritical norm and is the wrong yardstick.
- **(b2) is standard [reviewer ARGUED].**
  - With a potential small in the critical norm, ∫Vu²η² ≤ ||V||_{ℓ²}||uη||²_{ℓ⁴} ≤ ||V||C_Sob²||∇(uη)||² is absorbed for
    ||V|| ≤ c (Uhlenbeck's absorption). This gives the L^{2+} (indeed L^p, p ≲ 1/θ) step, after which Moser runs with a
    supercritical potential.
  - The lattice Sobolev inequality on one box is scale-free.
  - On the free-boundary box this needs the nonlinear REFL of §11.6 (NA-1), still ARGUED.
- **Coupling. "G6-F4 OCCURS" is an overclaim (S3-5).**
  - What §13.6 shows: the sup-norm closure A ≤ C_1 + C_2exp(C_3Aθ) (A := n²sup|F_0|/θ, a priori A ≤ Cn² by M2-1) does not
    exclude A ≳ 1/θ.
  - That is a statement about the **method**: a supercritical a-priori bound fed into a critical estimate.
  - It is not shown that any τ-small minimiser has A ≳ 1/θ, and SQ's own sentence l.1157-1158 says excluding it "is the
    genuine content of ε-regularity".
  - **Fix:** "G6-F4 OCCURS" (l.1152, 1196, 1200) → "G6-F4 occurs for the sup-norm closure of §13.6 (the large branch is not
    excluded by this argument); no large-branch minimiser is exhibited, and none is expected (below)".

### (i) Can (EPS-0) be TRUE deterministically, or do instanton-like configurations violate it?
**Verdict: (EPS-0) is expected TRUE as a deterministic statement. Instanton-like (bubbling) configurations cannot violate it,
because none exists in its hypothesis class [reviewer ARGUED; standard facts cited as literature, not re-proven here].**

1. **The energy is small at every scale, automatically.**
   - Every τ-small cone minimiser has E_𝒞 ≤ κ_+(π²/8)θ² (RES-dec step (1)'s competitor).
   - Hence its level-0 ℓ² curvature is ≤ C√(Nκ_+)θ on every sub-box and at every scale. This is the scale-invariant
     (critical) quantity in d = 4.
   - Pointwise, ||1 - U_0(p)|| ≤ √(2NE) (M2-1).
2. **Bubbling needs an energy quantum.**
   - 4D Yang-Mills is conformally critical. Uhlenbeck's ε-regularity says a critical point whose energy on B_R is below an
     absolute ε_0 obeys sup_{B_{R/2}}|F| ≤ CR⁻²||F||_{L²(B_R)}.
   - Concentration (a bubble) requires ≥ ε_0 of energy in arbitrarily small balls. A bubble is a non-flat finite-energy YM
     connection on S⁴, hence carries ≥ 8π² (instanton bound; and the gap theorem: small-energy YM on R⁴ is flat)
     [literature: Uhlenbeck 1982; not re-proven].
   - Here the available energy is ≲ θ² ≲ (C'τ)² ≈ 10⁻⁸, so it is ≪ ε_0.
3. **The lattice adds nothing that would evade this.**
   - Lattice "small instantons" (dislocations that fall through the lattice with action < 8π²/g² · …) need plaquettes at O(1)
     distance from 1.
   - Lüscher's admissibility (all ||1 - U(p)|| below a fixed ε_L ≈ 0.03) makes the topological charge an integer with a
     Bogomolny-type action bound [literature; not re-proven].
   - With ||1 - U_0(p)|| ≤ √(2NE) ≲ 10⁻⁴, the minimiser is deep inside the admissible sector with charge 0.
   - A τ-small minimiser therefore cannot host an instanton or a dislocation.
4. **What G6-F4's "large branch" is.**
   - A configuration with sup|F_0| ≈ θ/r² on a ball of radius r ≪ n and energy ≈ θ² is kinematically τ-small. It is
     consistent with every sup constraint SQ imposes.
   - It is excluded only by being a **critical point** with small critical energy, i.e. by ε-regularity.
   - So the large branch is the shadow of using the supercritical sup norm as the a-priori norm. It is the critical
     analogue of an Uhlenbeck bubble only in form: it lacks the energy quantum that a real bubble must carry.

### (ii) The proposed architecture (concentration = large-field defect, priced by e^{-8π²/g²}): verdict
**NOT the right fix for this wall, and not needed.**
- **Not needed.** Genuine bubbles (local energy ≥ ε_0, or charge ≠ 0) are already outside the τ-small minimiser class
  (points 2-3). Where they occur in the RG measure, they are bad or collar-bad cubes, which RLARGE v3 §2.3 already routes:
  Wilson positivity, Peierls, LF-count. Nothing new is required there, and the LF-count reading is consistent.
- **Does not apply to what is left.** The configurations that the sup argument fails to exclude carry action ≲ θ². A
  Peierls or instanton price for them is e^{-cθ²/g²} (no suppression at θ ≲ g), not e^{-8π²/g²}.
  - (CLS-min) is a **lower** bound on the cone infimum ℰ_P(V) (RLARGE §3.2). A hypothetical cheap concentrated competitor
    would lower the infimum, and moving it into a "defect" sector does not give it a large price. It is a small-field
    configuration in Balaban's sense at every scale (in the units of the scale where it lives its plaquettes are ≈ θ).
- **Restricting the minimisation domain is not harmless** for SQ's machinery. A minimiser over a constrained set satisfies
  the EL equations only where the constraint is inactive. CC-NA, RT-NA and RES-dec all use the EL equations.
  - In the critical (energy-at-every-scale) sense the constraint IS inactive for τ-small minimisers (point 1). So the
    restricted problem has the same minimisers and the restriction is vacuous.
  - In the sup sense (small field at every level with fixed thresholds), the constraint does not exclude concentration.
  - With scale-weighted thresholds (≤ CθL^{-2(k-l)} at level l), it is the decay class itself, which is circular (S2-6
    again).
- **So the restricted (EPS-0) is NOT automatic.** Its smallness hypothesis is built in and automatic, but its conclusion
  is a theorem: lattice ε-regularity for cone minimisers with the multi-level source. That is route (b), with (b1)-(b2)
  resolved in its favour (S3-4) and the source 𝒮 as the only real obstruction.

### The precise restated (EPS-0) (binding fix S3-6: replace l.1125-1126's definition by this, and keep the old text)
- **(EPS-0)** [unchanged in conclusion; hypothesis read critically]. There are θ_0 > 0 and A_0 < ∞ depending only on
  (N, L, κ_±) such that for every k, every level-k plaquette P and every minimiser of E_𝒞(P) that is τ_0-small at levels
  ≥ 1, with θ = ||1 - V_P|| ≤ θ_0:
  max_{level-0 p}||1 - U_0(p)|| ≤ A_0θn⁻².
  - Level-0 smallness is automatic: sup ≤ √(2NE) and ℓ²-energy ≤ κ_+π²θ²/8 on every sub-box.
  - No other smallness is assumed.
- **It splits into two statements:**
  - **(EPS-0a) lattice ε-regularity, single level.** There are ε_*, C depending on (N, L) such that for every level-0
    cube B_R of the REFL extension of a cone critical point:
    if Σ_{B_R}|𝒫|² ≤ ε_* and R³sup_{B_R}|𝒮| ≤ ε_*^{1/2}, then
    sup_{B_{R/2}}|𝒫| ≤ C[R⁻²(Σ_{B_R}|𝒫|²)^{1/2} + R·sup_{B_R}|𝒮|].
    - This is deterministic, single-level and scale-free.
    - Its inputs are Kato (PROVEN), the Weitzenböck/Bianchi-defect bound as a critical potential (S3-4), 4D lattice
      Sobolev, Moser, and the nonlinear REFL (ARGUED).
    - Expected provable by standard means.
  - **(EPS-0b) critical source bound.** For every τ_0-small minimiser: n³sup_{box_0}|𝒮| ≤ C_𝒮θ, C_𝒮 depth-uniform. That is,
    the level-0 residual current has exponent exactly 3.
    - **This is the real wall.** RES-dec gives exponent 3 - δ(τ) under sup smallness. Remark (3) gives exactly 3 on the
      decay class (circular).
- (EPS-0) ⟸ (EPS-0a) at R ≍ n + (EPS-0b), since E ≤ κ_+π²θ²/8 ≤ ε_* for θ ≤ θ_0.

### How (EPS-0b) can be decoupled [reviewer ARGUED; a programme, not a proof]
- **Where the factor comes from.** The funnel factor at level l is 1 + C(x + f_{l+1}), with f_{l+1} the LOCAL level-(l+1)
  curvature on the relevant block.
  - With STOKES-NA (avg) (S3-2), f_l(z) ≤ L^{-2l}·||F_0||_{ℓ¹(B_{CL^l}(z))} + (residual terms) by the Q_2 average, which is
    an ℓ¹ average in the four dimensions of the template.
  - For a concentrated profile (energy ε² at scale r), this is ≈ ε(r/L^l)² for L^l ≥ r. That **dilutes**, so Σ_l f_l
    converges, whereas the max-form STOKES-NA gives ≈ ε per level, i.e. a sum ≈ k·ε.
  - Π_l(1 + Cf_l) is therefore bounded by exp(C·𝔇(z)), where
    𝔇(z) := Σ_l L^{-2l}||F_0||_{ℓ¹(B_{L^l}(z))} ≤ Σ_l E_0(B_{L^l}(z))^{1/2}
    is a Dini-Morrey quantity at z.
- **The iteration.** Run a scale-ordered Campanato/harmonic-replacement iteration for MINIMISERS, from scale n down. At scale
  ρ, the coarse factors (L^l ≥ ρ) are controlled by the Morrey bound already established. The fine factors (L^l < ρ) are
  bounded by log_L(ρ)·E_0(B_ρ)^{1/2}, which is again controlled at that stage.
  - Whether the log at the first step (ρ ≈ n gives k·√E) closes depends on using the averaged form with transverse dilution.
    I have not shown that it does.
- **A parallel route that avoids the sup bootstrap entirely (route (α) in the CRITICAL norm).** §13.7's non-convexity
  argument compares the curvature correction with the Poincaré gap n⁻² (||a||² scale). In d = 4 the correct comparison is
  with the Dirichlet form:
  |⟨F, [a ∧ a]⟩| ≤ ||F||_{ℓ²}||a||²_{ℓ⁴} ≤ C_Sob²||F||_{ℓ²}||∇a||².
  - So E_𝒞 is convex on a Coulomb-slice ball {||∇a||_{ℓ²} ≤ Cθ} once ||F||_{ℓ²} ≤ c, which is automatic.
  - On the lattice, sup|a| ≤ ||a||_{ℓ⁴}, so the compact-group Taylor remainders are controlled too.
  - Uniqueness of the small-energy minimiser in that ball would identify it with the perturbative (BFT/REG-lin-type) critical
    point. (EPS-0) then follows from the perturbative construction.
  - The inputs are (α1) a lattice **Uhlenbeck gauge** under small ℓ² curvature on the REFL box (BFT_B's NF-ex needs the sup
    hypothesis max n|A| ≤ ε_0, which is the decay scale, so it does not supply this) and (α2) convexity of the kernel terms
    in the same slice.
  - **So §13.7's sentence "convexity in a ball needs level-0 curvature ≲ n⁻²" is a method statement for the sup/gap
    comparison, not a fact (S3-7).**

### Strategic verdict on (EPS-0)
- (EPS-0) is the right wall, and it is a critical-norm ε-regularity/uniqueness statement for small-energy minimisers,
  expected TRUE.
- It is not a large-field problem. Do not route it to RLARGE's Peierls/instanton pricing.
- Its single non-standard ingredient is the critical source bound (EPS-0b). Equivalently: the multi-level funnel feedback
  must be summed in a Morrey/ℓ¹-averaged norm, not in sup.

---

## Priority 4. q4: K3 FAIL

### The lock hold
- `until mkdir …/locks/numeric; do sleep 20; done` waited for another holder. Then mkdir 10:49:58 UTC (load 3.47, 34%
  free), q4_copy.py, rv3.py, one rmdir at 10:50:13.
- nice 10, all BLAS threads 1, python3 without -I, no `timeout`, no trap.
- q4 ran in 11.6 s (57 MB peak); rv3 in 3.1 s (57 MB). No process was left running (pgrep empty).
- (The lock directory present afterwards belongs to a later holder.)

### The re-run
**Identical to checks/q4_out.txt in every line** (diff empty): K3 max 1.894·10⁻⁸ against 1e-8. **OVERALL FAIL as
pre-registered: stands.**

### Is the post-hoc reading honest? Honest in outcome; its mechanism is mis-described (fix S3-8)
- **R1 (Newton W_0).** A Newton solve of the SU(N) stationarity condition gives a residual ≤ 7·10⁻¹⁸. Against it:
  - q4's BFGS W_0 (SU(3)) is off by **||W_Newton - W_BFGS||_op = 3.0·10⁻⁸**;
  - for SU(2), q4's polar factor is exact (9·10⁻¹⁷).
  - So q4's criteria precondition "SU(3): computed numerically to ≤ 1e-13" was NOT met.
- **The K3 excess is first-order, not finite-difference noise.**
  - At s = 0, q4 sets V := W_BFGS(M). The finite difference then measures N⁻¹Re tr((W_0^true - V)*δ), which is O(3·10⁻⁸·|δ|).
  - Subtracting exactly this first-order prediction leaves ≤ 2.4·10⁻¹⁰ (SU(3)) and 1.7·10⁻¹⁰ (SU(2)).
  - So the whole excess is the maximiser's error. It does not depend on h and does not come "at the finite-difference step"
    as SQ §14 l.1205 says.
- **"The formula side is 0 exactly" (l.1205; SQ_LOG l.120) is tautological.** Z = W - V with V := the same computed W, so it
  carries no information. Delete it.
- **K3 with the accurate W_0 passes:** 2.5·10⁻¹⁰ (SU(3)) and 1.6·10⁻¹⁰ (SU(2)) at q4's h = 1e-5. At h = 1e-4 the same
  exact-W_0 test gives 1.6-2.5·10⁻⁸: the O(h²) curvature of the max term. So the 1e-8 threshold was also tight against
  truncation at larger h. q4's h = 1e-5 was adequate.
- **K2's 3.0·10⁻⁸ (PASS) has the same origin** (BFGS error at the s ≠ 0 points). Its margin is real but smaller than q4's
  "O(h²) ≈ 1e-10" design note suggests.
- **Lemma K (b) is not implicated.**
- **Independent identity checks (R2, R3; reviewer, post hoc to q4 but pre-stated in rv3.py's header):**
  - the Riesz representative of j by finite differences: 0/400 violations;
  - K (d): min |j|/lower = 1.41 (SU(2)), 1.23 (SU(3)) ≥ 1, and max |j|/upper = 1.00 (SU(2), sharp), 0.81 (SU(3)) ≤ 1;
  - K (e): min φ/bound = 2.0, 1.5 ≥ 1, at x ≤ 0.4 and η ≤ 0.05;
  - K (c), left and right: |V-grad + M-grad| ≤ 2.2·10⁻¹⁰;
  - RT-NA's backward-traversal per-contour derivative (prefix·U(b)⁻¹, ε = -1): ≤ 2.3·10⁻¹⁰.
  - All PASS.
- **Scope note.** q4 and R1-R3 test the per-term identities of Lemma K and RT-NA's per-contour derivative. Neither tests
  CC-NA or the funnel cancellation on an actual cone (no S4' contour geometry is built). Those rest on the hand proofs,
  which I confirm (Priority 2).

**Verdict P4: FAIL stands as recorded and was reported honestly. The reading's mechanism is wrong ("noise at the FD step");
it is a first-order W_0 optimiser error of 3·10⁻⁸ that violated q4's own accuracy precondition. "Formula side exactly 0" is
vacuous. With an accurate W_0, K3 passes at 2.5·10⁻¹⁰.**

---

## Route (a) (§13.7) and the BFT-1 clause request (§13.8)
- **§13.7 reading: CONFIRMED.**
  - NF-uniq (BFT_B l.2532) is uniqueness of the critical point of the gauge functional Φ_{U,X} in 𝒲_δ, not of E_𝒞.
  - (N1-bd) (l.2538) is sup|w^c| ≤ C_B sup|(dw)^c|.
  - Two additions:
    - NF-ex (l.2542) itself needs max n|A| ≤ ε_0, a decay-scale hypothesis. So route (a) is downstream of (EPS-0) in its
      existence step too, not only in its use.
    - The status tag "PROVEN-HERE as stated" overstates. The reading is a reading, and the convexity-gap sentence is ARGUED
      and, per S3-7, misleading. **M3-8:** relabel §13.7 "reading (CONFIRMED by review); the convexity statement ARGUED
      for the sup/gap comparison only".
- **§13.8: CONFIRMED with S3-1 and S3-6.**
  - Item (3): the box clause is unproven, per BFT_B l.240.
  - Item (4): replace "an ε-regularity or large-ball clause" by "(EPS-0a) + (EPS-0b), or a critical-norm (Uhlenbeck-gauge)
    uniqueness clause for small-energy cone minimisers".
  - Items (1), (2), (5) are unchanged.
  - θ_r > 2 is DELIVERED (RES-dec). The BFT-side requirement is now only that BFT's residual norm be no weaker than RES-dec's.

---

## Corrected tally

| Item | SQ's status | Reviewer |
|---|---|---|
| Step 1 [RSQ2-fix] | DONE | DONE except M3-2 (one scope tag missing); S2-5 CONFIRMED and sharpened (S3-1) |
| Lemma K | PROVEN, not counted | CONFIRMED (M3-3: uniqueness of W_0 for (b)) |
| Lemma CC-NA | PROVEN, counted | CONFIRMED (M3-4 wording) |
| RT-NA + RES-dec | PROVEN, counted (one) | CONFIRMED (M3-5 multiplicity; M3-6 scope) |
| STOKES-NA + STOKES-it | PROVEN, counted (one) | CONFIRMED (M3-7; S3-2 averaged form recommended) |
| Theorem RED-0 | PROVEN, counted | CONFIRMED as an implication; **uncounted corollary** (S3-3) |
| Lattice Kato | PROVEN, not counted | CONFIRMED (trivial) |
| §13.6 (b1) | unsettled, "supercritical" | **WRONG as stated**: a critical potential term on the lattice (S3-4) |
| §13.6 (b2) | unsettled | standard [ARGUED] |
| G6-F4 | OCCURS | occurs for the sup closure only; no large-branch minimiser exhibited; not expected (S3-5) |
| §13.7 | PROVEN-HERE as stated | reading CONFIRMED; convexity sentence ARGUED, misleading (S3-7, M3-8) |
| q4 | FAIL (K3) | FAIL stands (re-run identical); cause is the first-order BFGS W_0 error 3·10⁻⁸ (S3-8); K3 passes with Newton W_0 |
| (EPS-0) = (REG-min) | OPEN | OPEN; restated as (EPS-0a) + (EPS-0b) (S3-6); expected TRUE |

**Claimed 12 / 3 / 2 → corrected 11 / 3 / 2** (PROVEN-HERE counted / CONDITIONAL / OPEN). Session 3 contributes 3 counted
items, not 4. No item is GAP or WRONG among the counted proofs.

## Binding fixes (next lane-G session)
1. **S3-1** (l.902-910): S2-5 is settled. The N5-sf0 boxes are gauge charts in a torus, and BFT_B l.240 says the box clause
   is unproven. Delete "limited reading".
2. **S3-3** (§14 l.1207-1213): RED-0 is an uncounted corollary; file tally 11 / 3 / 2.
3. **S3-4** (l.1148-1150): (b1) is a critical potential term on the lattice (neighbour-max bound, ℓ⁴ ≤ ℓ²), not a
   supercritical drift.
4. **S3-5** (l.1152, 1196, 1200): "G6-F4 OCCURS" → "occurs for the sup-norm closure; not exhibited; not expected".
5. **S3-6** (l.1125-1126, l.1159-1162, §13.8 item (4)): restate (EPS-0) with the critical hypothesis made explicit, and split
   it into (EPS-0a) (single-level ε-regularity) and (EPS-0b) (n³sup|𝒮| ≤ Cθ); name (EPS-0b) as the wall.
6. **S3-7** (§13.7 l.1170-1175): the n⁻²-gap non-convexity is a sup/gap-comparison statement. In d = 4 the
   Dirichlet-form comparison gives slice convexity under small ℓ² curvature, given a lattice Uhlenbeck gauge (not supplied
   by NF-ex).
7. **S3-8** (§14 l.1201-1206, SQ_LOG l.118-120): q4's reading should say:
   - "the K3 excess is the first-order error of the SU(3) BFGS maximiser (||ΔW_0|| = 3·10⁻⁸, REVIEW_SQ_S3 R1), which
     violates q4's own '≤ 1e-13' precondition; with a Newton W_0, K3 = 2.5·10⁻¹⁰";
   - delete "the formula side is 0 exactly" (tautological).
   - A future identity check computes W_0 by Newton on the stationarity condition.
8. **Minor:** M3-1 (§T3's tr|M| kernel), M3-2 (Answer-to-Q3 scope), M3-3, M3-4, M3-5, M3-6, M3-7 (y_c undefined), M3-8.
   S3-2 (STOKES-NA averaged form) is recommended, not binding.

## Strategic verdict
1. **Keep §13.2-§13.4. They are real.**
   - CC-NA and the nonlinear funnel cancellation give residual decay with exponent > 2 on the whole τ-small class, with no
     bootstrap. This is the first non-abelian piece of (REG-min) proven unconditionally.
   - STOKES-NA shows the curvature half reduces to level 0 with coefficient exactly L².
2. **(EPS-0) is not a bubbling problem.**
   - Its hypothesis class has energy ≲ θ² ≪ ε_0 at every scale and plaquettes inside Lüscher's admissible sector.
   - Instantons and dislocations cannot occur there. The large branch of §13.6 is a supercritical-norm artefact.
   - Do not move the wall into RLARGE's defect sector: the leftover configurations have action ≲ θ² and no large price.
3. **The wall is one estimate: (EPS-0b), the critical (exponent-3) bound on the level-0 source.** Equivalently, the funnel
   feedback must be summed in an ℓ¹-averaged/Morrey norm.
4. **Recommended next target, in order.**
   - (1) Write STOKES-NA (avg) (S3-2) and redo RES-dec's per-level factor with LOCAL, averaged curvature. Test whether
     Π(1 + Cf_l) is bounded by exp(C𝔇) with 𝔇 a Dini-Morrey sum.
   - (2) Prove (EPS-0a) on Z⁴ (no free boundary first). It is standard in structure, and (b1)/(b2) are not obstructions.
   - (3) In parallel, the critical-norm route (α): a lattice Uhlenbeck gauge under small ℓ² curvature, plus slice
     convexity. If (α1) is reachable on the lattice (where sup ≤ ℓ⁴ helps), it gives minimiser uniqueness and makes
     (EPS-0b) unnecessary.
5. **Do not:**
   - cite G6-F4 as an occurring failure of minimisers;
   - count RED-0;
   - describe §13.7's gap argument as a proof that uniqueness fails;
   - price level-0 concentration through e^{-8π²/g²}.
