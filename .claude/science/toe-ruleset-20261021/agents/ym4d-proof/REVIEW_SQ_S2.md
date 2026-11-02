# REVIEW_SQ_S2: hostile review of lane G session 2 (SQ.md [RSQ1-fix] edits, Corollary DESC-ε, §11, checks q3, q3b)

Reviewer: an independent agent. I wrote none of SQ.md, SQ_LOG.md or the checks, and I edited no file except this one. No
commits, PRs or pushes.

Inputs (read-only):
- SQ.md l.1-385 (§T, §T2, §0 with every [RSQ1-fix]) and l.558-883 (§8-§12).
- SQ_LOG.md (all).
- REVIEW_SQ_S1.md (all).
- checks/q3_criteria.md, q3_src_decay.py, q3_out.txt, q3_time.txt; checks/q3b_criteria.md, q3b_d4_plaq.py, q3b_out.txt,
  q3b_time.txt.
- REVIEW_S22.md Part 5 (l.372-436).
- RTARGET.md §33 (l.572-600).
- LINEAR_PACKAGE.md l.176-177 (LES-sup, LES-div).
- PROOF.md: LES (l.2073-2080), LES-sup (l.2388-2395), LES-div (l.3394-3400).

Scratch work is in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/rsq2/`:
- rv.py: the reviewer's checks R1-R3. It reuses only q3's box Chain class; the periodic chain and the REFL extension are
  written independently.
- run.sh, lock_log.txt, and the re-run outputs.

Line numbers are SQ.md's unless another file is named.

---

## Bottom line

- **Step 1 ([RSQ1-fix]) is complete and correct.** Corollary DESC-ε is right as written: the constant C'/√c_♭ = 53·√640 ≈ 1341
  and the threshold η_♭ ≈ 1.1·10⁻²⁶ at C_D = 2. It is correctly CONDITIONAL ⇐ (REG-min).
- **Lemma REFL, Lemma SHIFT and Theorem REG-lin are correct.**
  - I checked REFL by hand (Q's tent symmetry T(u) = T(2L-2-u), crossing conventions, copy count) and numerically (R2).
  - On the reflection torus, E_per,min = 2^d·E_box,min to 10 digits.
  - ext(box minimiser) is a periodic critical point (gradient ratio ≤ 10⁻¹²), for d = 2, 3, pure data, the q3 (C) source and
    random sources on every row.
  - REG-lin's constants check out (the 23409 copy count; 0.6; 16; the exponent sums).
- **Theorem REG-lin-src: CONFIRMED-WITH-FIX.**
  - (a) is correct, but "no level weights" must be scoped (S2-3).
  - The boundary-compatibility hypothesis is superfluous for (b) (S2-2); it is needed only for (c).
- **q3: the FAILs are honest, but the reading overclaims.**
  - The A1 zeros are exact by construction. q3's vortex sits where the transported weight T_{L^m} ⊗ T_{L^m} is affine, so its
    transported circulation is identically 0.
  - So q3 (A) is the top-datum test in disguise. It cannot test REVIEW_SQ_S1's level sum in either direction.
  - My R1 supplies the missing test: vortices placed at the tent peak have nonzero transport. Their response is exactly
    proportional to the top-datum response (deviation ≤ 4·10⁻¹³), as SHIFT predicts, and the aligned all-level sum stays
    bounded.
  - "Criterion-design error" for QA d = 3 is a fair reading. QB's PASS is confounded in exactly the same way as QA's FAIL.
  - q3b's two-depth doubling is not evidence of growth: q2's pure-data C_D also doubled, 0.22 → 0.45, and is now proven bounded.
- **§11.6 (non-abelian) is ARGUED, and its main conclusion is right.** The large-branch exclusion is the critical step, and
  the sup route relocates it rather than removing it.
  - "(REG-min) ⇐ (BFT-cone) + (MIN-reg)_cone" is close to circular. BFT's ball is a ball in the weighted norm 𝔐, so
    (MIN-reg)_cone already contains (REG-min).
  - BFT as stated also promises only some θ_w ∈ (0, 2], while DESC needs θ_w > 1 (S2-6).

---

## Priority 1. [RSQ1-fix] edits and Corollary DESC-ε

### The fixes (S1-1 … S1-6, §7, M-1 … M-7)
All are present and tagged, with the original text kept: l.82-97, 109-115, 132-134, 181-183, 216-231, 243-247, 263-287,
357-372, 375-379, 493-499, 512, 547-553, 574, 593-597, 608-609, 634-638.
- The figures match REVIEW_SQ_S1's table:
  - θ_0 = 7.6·10⁻⁹ at C_D = 2;
  - price 3·10⁻²³;
  - "net loss of 6-9 orders";
  - θ_♯ ≈ 3.5·10⁻⁶.
- The session-1 tally is corrected to 6 / 2 / 2 (l.634-638).

Two defects:
- **S2-1a (pointer, l.284-285).** "residual sources at levels ≥ 1 cost no depth factor; §11.3, q3". §11.3 is REG-lin (pure
  data); the residual-source statement is §11.2 SHIFT / §11.4 (a). Also, q3 does not show this (Priority 2).
  - **Fix:** read "§11.2, §11.4 (a); q3 A1 is consistent with SHIFT but is not a test of it (exact by construction); see
    REVIEW_SQ_S2 R1".
- **S2-1b (l.286 against l.744).** The re-plan says "the linear estimate in the RTARGET §33 Hölder pair (level weights …)". But
  §11.4 (a) claims that residual sources need no level weights. The two statements concern different source classes (S2-3).
  - **Fix:** add "(level weights are needed for general co-closed currents j_l, §33; not for paired residual sources, SHIFT)".

### Corollary DESC-ε (l.312-343): CONFIRMED (CONDITIONAL ⇐ (REG-min); the implication is PROVEN)
I re-derived every step.
- **Case (i), ω a level-0 plaquette:** E ≥ τ²/(2N) ≥ c_♭τ².
- **Case (ii), ω a residual:** the endpoint-block plaquettes have height i < i + ½, so KQ (lower) applies at τ ≥ 73.6Ny²
  (with τ ≤ 1/(73.6Nc'²A'²)).
- **Case (iii), ω = q a level-i plaquette:**
  - every object of 𝒞(q) other than q has height < i, since box_i of 𝒞(q) is the single plaquette q and q's link residuals
    have height i - ½;
  - FORCE (strict form) gives θ_q ∈ [τ, C'τ);
  - nesting and competitor give E ≥ 𝓔^{𝒞(q)};
  - DESC (b) at depth i < k gives ≥ c_♭min{θ_q/C', τ}² ≥ c_♭τ²/C'².
  - This is not circular: DESC itself does not use DESC-ε.
  - Every case contradicts E < c_♭τ²/C'² strictly.
- **(ii)** is correct (DESC (a) rules out θ ≥ C'τ, then DESC (b) applies).
- **(iii):**
  - the δ-limit is correct, since (1 + δ)²E < η_♭ ⇒ τ ≤ τ_♭;
  - the E = 0 case is handled;
  - the log bound uses θ ≤ C'τ_♭ ≤ θ_0 ≤ ½.
- **Constants:**
  - C'/√c_♭ = 53·25.30 = 1341 ✓ (≈ 1.3·10³);
  - η_♭ = c_♭τ_♭²/C'² with τ_♭ = θ_0/C' = 1.43·10⁻¹⁰ gives 2.06·10⁻²⁰/640/2809 = 1.1·10⁻²⁶ ✓;
  - C'_AE-replacement 1.011²·2·2809·640 ≈ 3.7·10⁶ (not stated in SQ; harmless).
- **The A5 consequence (l.223)** is correct as an order of magnitude: ε_1 ≲ (η_♭/4C_3)^{1/2} ≈ 5·10⁻¹⁴/√C_3, and price
  ≈ (c_♭/C'²)ε_1² ≈ 1.6·10⁻³³/C_3.
- **One precision fix (minor, M2-1).** In (iii), the level-0 plaquettes obey the sharper ||1 - U_0(p)|| ≤ √(2NE) directly. The
  stated 1.3·10³√E is valid but crude for them. Optional.

**Verdict P1: Step 1 DONE; DESC-ε CONFIRMED as CONDITIONAL. Fixes: S2-1a, S2-1b (wording).**

---

## Priority 2. q3, q3b: fair reading or rationalisation?

### Order and honesty: clean
- §T2 was written at 04:24, q3_criteria at 04:26:02 and q3_src_decay.py at 04:27:01, all before the run at 04:29:56.
- q3b_criteria (04:38:20) states in its own text that it was written after q3's run; the script followed at 04:38:32 and the
  run at 04:38:46.
- No criterion was edited after a run.
- **Re-run (reviewer):** q3 and q3b were run verbatim from copies with identical SHA-1 (f3bc7d28…, e5d1ae34…), under one lock
  hold (mkdir 04:59:24, rmdir 05:00:36 UTC; load 3.15, 41% free, nice 10, threads 1).
  - The output is identical to the records in every printed digit, excluding wall-clock lines.
  - q3 ran in 65.2 s with a 202 MB peak footprint; q3b in 0.60 s with 87 MB.
  - rv.py ran in the same hold: 6.8 s, 150 MB.
  - No process was left running, and the lock directory is gone.

### Why A1 gives 0.0000 exactly: by construction (answers the brief's question)
- **The mechanism.**
  - By SHIFT + TOP, a source at level l changes only the effective datum. Its fine response is the pure-data response times
    c := dS_k(P)/dB_k(P).
  - dS_k(P) = Q_2^m(ds_l)(P) = Σ_p w(p)ds_l(p), with w = T_{L^m} ⊗ T_{L^m} ⊗ (transverse indicators). This is the kernel
    stated at SQ §2 l.398: Q_2^m has kernel L^{-m}T_{L^m}.
  - For the unit vortex on ∂p_0, Σ_p w·ds = -Δ_2w(p_0) = -[T''(b_0)T(b_1) + T(b_0)T''(b_1)]·χ.
  - q3 places p_0 at base (M-1)/2 (M = L^{k-1-l}). The neighbours b ± 1 then lie in the rising affine part [0, M-1] of the
    tent, so T'' = 0 there and **dS_k(P) = 0 identically**.
- **The consequence.**
  - The B̃-chain has zero datum, so it is pure gauge: F̂_0 = 0, r̂ = 0, and 𝔑 = 4 = the source's own weighted circulation.
  - This is an algebraic identity, not a measurement. It is not PROOF's J-str either: it is the discrete harmonicity of the
    bilinear tent.
- **Reviewer check R1** (rv.py; vortex moved to base M-1, the tent peak, i.e. the block boundary under P's centre lines):
  - **Transport is nonzero:** c = 3.704·10⁻² = 1/27 at l = k - 2 (d = 2), 1.235·10⁻² (d = 3), 4.12·10⁻³ (d = 4).
  - **F̂_0(source at level l) = c·F̂_0(top datum)**, with max deviation ≤ 4·10⁻¹³ relative, at every d and k tested
    (d = 2: k ≤ 4; d = 3: k ≤ 3; d = 4: k = 2). This is SHIFT + TOP, now tested non-trivially.
  - **The aligned all-level sum (every level at the peak, plus the top) stays bounded.** It sits only slightly above the top
    datum alone:

    | d | k | N_0 | 𝔑 | top alone (N_0 / 𝔑) |
    |---|---|---|---|---|
    | 2 | 2 | 7.77 | 7.77 | 7.49 / 7.49 |
    | 2 | 3 | 9.07 | 9.07 | 8.73 / 8.73 |
    | 2 | 4 | 9.31 | 9.94 | 8.96 / 8.96 |
    | 3 | 3 | 6.34 | 6.87 | 6.26 / 6.78 |
    | 4 | 2 | 0.84 | 2.19 | 0.84 / 1.80 |

    The geometric sum Σ L^{-(k-1-l)} of SHIFT is visible: the c-values fall by ≈ 1/27 per level.

### Verdicts on the readings (l.795-805)
- **(i) "QA d = 3 FAIL is a criterion-design error": FAIR, but mis-located and incomplete.**
  - The measured (A) response is the top-datum response, exactly, by the identity above. So QA's d = 3 growth is pure-data
    growth. Better evidence than SQ cites: q3's own energy column shows that d = 3 is not scale-invariant (E = 1.46, 0.89,
    0.46 at k = 1-3, against d = 4's 1.78, 1.68).
  - The primary design error is the degenerate placement of the (A) sources, which made the level-sum test vacuous. The d = 3
    choice is secondary, and it was foreseeable after q2's d = 2 lesson (REVIEW_SQ_S1 P6).
  - **Fix S2-4a:** say so.
- **(ii) "A1 is the measured form of SHIFT … the level-sum mechanism … does not occur": OVERCLAIM.** A1 is consistent with
  SHIFT, but it tests nothing about level sums (zero transport by construction). The level-sum statement rests on SHIFT's
  proof, which is correct, and on R1.
  - **Fix S2-4b:** replace with "A1's zeros are exact by construction (the vortex sits in the affine part of T_{L^m}). SHIFT's
    non-trivial content is confirmed by REVIEW_SQ_S2 R1".
- **(iii) The B/C contrast and q3b: weak, and labelled about right. One sentence is false.**
  - **Symmetric treatment.** By reading (i), d = 3 cannot separate a log from d = 3 scaling, so QB's PASS carries no more
    weight than QA's FAIL. The usable signal is the same-dimension contrast: (B) R_ctr grows 0.90 → 1.75 → 2.67, while (C)
    R_ctr is flat at 0.113, 0.091, 0.100.
  - **q3b.** B4 doubling at k = 1 → 2 (0.995 → 2.014) is matched by q2's provably bounded pure-data C_D (0.22 → 0.45). Two
    depths cannot separate "grows" from "saturates", so RB PASS is not evidence. (q3b's criteria do call it "WEAK", which is
    honest.)
  - **The caveat sentence is false for d = 3 (l.802-803).** It says (C)/(C4) "are flat anyway, so the boundary layer did not
    dominate". In d = 3, (C)'s N_0 grows (0.173, 0.203, 0.276): that is QC's FAIL.
    - R3 locates the sup: the argmax is the (0,1) plaquette at site (n-1, n-1, (n-1)/2), i.e. at P's centre lines, distance
      ≥ n - 1 from every face, at k = 1, 2, 3. So the growth is interior and is not a boundary layer.
    - The compatibility caveat is moot here anyway (S2-2).
  - **Fix S2-4c:** "(C)'s N_0 growth in d = 3 is interior, at P's centre lines (REVIEW_SQ_S2 R3), and is attributed to d = 3
    scaling (post hoc); (C4)'s N_0 is flat over two depths. Boundary compatibility is irrelevant to (b)."
- **(iv) Mislabel in q3_criteria (not editable now; note it in SQ).**
  - p*_0 with base ((n-1)/2, (n-1)/2) is the centre of the level-0 block under P's corner vertex (0, 0), not "the fine
    plaquette at the centre of P". P's centre is at fine n - ½.
  - The same holds for X* and the (A) vortices. So R_ctr is measured at the vertex-block centre, distance ≈ n/2 from two
    faces.
  - This does not change any verdict, but "centre of P" should read "centre of P's corner block" (**M2-2**).
- **"Answer to Q3" (l.804-805).**
  - "Loses NOTHING for residual sources at any level or for pure data" is correct as theorems: SHIFT and REG-lin.
  - "Loses a depth factor for curl-ful level-0 plaquette sources" is EXPECTED but NOT shown. It rests on:
    - the classical L^∞ unboundedness of Calderón-Zygmund operators [literature; not proven here];
    - LES-sup's crude loss of n (a method bound);
    - weak numerics.
  - **Fix S2-4d:** label it ARGUED (expected CZ log). G4-F2 "OCCURS" (l.782, 868) → "expected (CZ); not proven; sup|q_0| +
    sup|dq_0| suffices (REG-lin-src (b))".

**Verdict P2: q3 OVERALL FAIL stands as recorded; the reading is partly rationalisation (the A1 and level-sum claims, the
d = 3 caveat). The fixes S2-4a-d are binding. q3b PASS stands as recorded, with no evidential weight beyond "consistent".**

---

## Priority 3. Lemma REFL and Theorem REG-lin: CONFIRMED (given LES-sup)

### REFL (l.664-697)
- **(a) Commutation.**
  - Blocks map to blocks: -1 - (LX + s) = L(-1 - X) + (L - 1 - s).
  - Q's in-plane weights are invariant under s ↦ -2 - s (T(u) = T(2L-2-u)), with a sign flip on the normal component.
  - The transverse block averages are invariant.
  - d and d* commute with ext (pull-back by a lattice automorphism with orientation signs).
- **(b) Crossing objects.**
  - A crossing plaquette has two crossing links (0) and two mirror links with equal values, so dB = 0.
  - A crossing coarse link's template [-L, L-2] is self-mirrored with opposite values, so QB = 0.
- **(c) Energy.** Non-crossing templates lie in one copy: [LX, LX + 2L - 2] ⊂ [0, N^{(i)} - 2] for 0 ≤ X ≤ N^{(i+1)} - 2.
  Hence E^per_cell = 2⁴E^src.
- **(d) Minimiser.** The convexity / G-averaging argument is correct, and it already suffices: ext(box minimiser) attains
  inf E^per, so the EL equations hold at every link. The separate "box d*-sum" sentence is redundant.
  - **Compatibility with the averaging operators** (the brief's question): yes, Q∘ext = ext∘Q at every level, including the
    level-k torus of side (4, 4, 2, 2), where all transverse level-k links are crossing and hence 0.
- **Numerically (R2):**
  - E_per,min/(2^d E_box,min) = 1.0000000000;
  - gradient of E_per at ext(box minimiser) ≤ 10⁻¹² relative;
  - for d = 2 (k = 2, 3) and d = 3 (k = 1, 2), with top data, q3's (C) and random sources on every row.

### REG-lin (l.711-740)
- **(a)** The competitor 0 gives E_min ≤ κ_{k-1}θ²/2.
- **(b)** The EL in B_{i+1} gives r_i = (κ_{i+1}/κ_i)Q^Tr_{i+1}. ||Q^T||_{∞→∞} = Q's column sum: T(u) + T(u + L) = L along the
  link, then L^{-1} for each of three transverse directions, giving L^{-3} ✓.
- **(c) LES-sup on Z⁴.**
  - PROOF l.2073 (LES) is stated for 2-forms on Z⁴ with dF = K and d*F = J on Q_R(x_0); l.2388 (LES-sup) is the same
    without the a-priori sup. So a periodic lift is admissible, and R = 16n ≥ 16 holds for every k ≥ 1.
  - Copies: 9 in-plane (period 2n, window 16n + 1) and 17 transverse, so 9²·17² = 23409; √23409/256 = 0.598 ✓.
  - R·sup|J| = 16κ_{k-1}θn^{-2} ✓.
- **(d)** F_l = Q_2^lF_0 - Σd(Q^{l-1-i}r_i). Q_2's row sum is L² with nonnegative weights. The exponent
  2(k-l) + (l-1-i) - 3(k-1-i) = -(k-l) - 2(l-1-i) ✓, and the sum is ≤ L²/(L² - 1).
- **Remark (2)** ("q2 consistent with the proven bound") is vacuous while C_LES is uncomputed. Say "not contradicted"
  (**M2-3**).

**Verdict P3: REFL CONFIRMED (hand + R2); REG-lin CONFIRMED (PROVEN given LES-sup, C_LES uncomputed); counted correctly as
one item.**

---

## Priority 4. Lemma SHIFT, Theorem REG-lin-src (l.699-782)

### (a) residual sources: CONFIRMED; wording needs scoping (S2-3, binding)
- The identity QB_i - B_{i+1} + s_i = QB̃_i - B̃_{i+1} is exact.
- The exponent sum 2(k-j) + (j-1-i) - 2(k-1-i) = -(j-1-i) ✓.
- R1 confirms the exactness non-trivially.
- **"No level weights" is true only in a narrow sense.**
  - σ_r carries the decay-class weights L^{2(k-1-i)}. The claim means "no summable extra weights ω_l".
  - The class is the PAIRED currents (κQ^Ts_i at level i, -κs_i at level i + 1) of energy-residual sources. It is not
    RTARGET §33's class of general co-closed currents j_l (l.577-579), where G♯_0-soft needs Ω < ∞.
- **The non-abelian a-priori argument does not consume (a).** At a minimiser, the EL equations carry unpaired currents such
  as (De_i)^Tr̂_i and (DR)^TF̂. REVIEW_SQ_S1's level-sum concern lives in exactly those currents. §11.6 (NA-3) treats them
  multiplicatively through the residual recursion, which is the right move, but this is ARGUED.
- **Reviewer count [ARGUED].**
  - Such currents at level l reach J_0 through (Q^T)^l, contributing ≈ L^{3(k-l)}sup|j_l| to n³sup|J|.
  - With j_l ≈ m_l·r̂_l and r̂_l decaying only like L^{-2(k-1-l)} (Σ_dec's (D2)), each level contributes ≈ C_eKθ²L², i.e. a
    sum of order k.
  - With L^{-3(k-1-l)} residual decay, which the EL recursion gives (REG-lin (b), NA-3), the sum is geometric.
  - So the non-abelian bootstrap norm must carry the residual exponent 3 (or any exponent > 2), not (D2)'s 2.
- **Fix S2-3:**
  - at l.744, add "(paired energy-residual sources; general EL currents at every level are not covered, Remark (1))";
  - at l.805 and §12 l.866, the same;
  - in (NA-3)/(NA-4), define 𝔑 with residual weight L^{3(k-1-i)} (or (2 + δ)) and say why.

### (b) Lipschitz level-0 source: CONFIRMED; the boundary-compatibility hypothesis is SUPERFLUOUS (S2-2, binding)
- **The constants check out:**
  - competitor 0 gives E_min ≤ ½||q_0||² + κθ²/2;
  - ||q_0||² ≤ 24n⁴·sup|q_0|² = 24σ_0²;
  - LES allows dF = K;
  - n²·16n·λ_0n^{-3} = 16λ_0.
- **But λ_0 = L^{3k}sup|dq_0| involves only the exterior derivative, and it does not see the reflection.**
  - Take a crossing 3-cell (a, b, c) spanning x_a ∈ [-1, 0]. Its two (b, c)-faces carry the EVEN component q_bc with equal
    values (contributing ∂_aq_bc = 0), and its (a, b)- and (a, c)-faces are crossing plaquettes (0).
  - So d(ext q_0) = 0 on crossing 3-cells, and sup|d ext q_0| = sup_box|dq_0| for EVERY q_0.
  - The odd-component "jump" across a face enters only ∂_aq_{a·}, which d of a 2-form never contains.
- **Fix:**
  - l.748-753: compatibility is needed for (c) only;
  - l.656: rename λ_0 "coarse-unit sup of dq_0", not "Lipschitz size";
  - (b) is then strictly stronger than stated.
- **The answer to the brief's question.** "Sup alone is not enough at level 0" is correct for sup|q_0| alone, and only as
  EXPECTED (S2-4d). Sup|q_0| + sup|dq_0| IS enough (b). (NA-2) needs exactly this form: the covariant Bianchi defect is a sup
  bound on dF̂.

### (c) Hölder level-0 source: CONFIRMED in kind
- The Coulomb representative on the period-cell torus, ΔB^C = ext J - d*(ext q_0), fits LES-div's divergence form (PROOF
  l.3394).
- The unit conversions check out:
  - R^{-α}(R^{-4}ψ)^{1/2}·n^{2+α} = ψ^{1/2};
  - n^{2+α}[g]_α,fine = [q^c]_α;
  - n³H_0 = κsup|r|;
  - the Campanato-to-sup telescoping gives 16ψ^{1/2}.
- Here compatibility IS needed: d* contains ∂_a^*q_{a·}.
- k ≤ 2 (n < 16) is handled by finite dimensionality. State this as "constants depending on L", not "as in PROOF" (**M2-4**).

**Verdict P4: SHIFT CONFIRMED; REG-lin-src CONFIRMED-WITH-FIX (S2-2, S2-3), counted as one item. "Sup alone not enough at
level 0" is correct only as ARGUED/expected, and only for sup|q_0| without sup|dq_0|.**

---

## Priority 5. Non-abelian (REG-min) and BFT (§11.6)

- **(NA-0) DESC needs θ_w > 1: CONFIRMED (re-derived).**
  - MSG-dec's increment is (curvature/residual decay)/(link decay) = L^{-(θ_w-1)(k-i)}.
  - SUP-price steps (3) and (5) stay geometric for θ_w > 1.
  - Note: K, C_err and τ_♭ degrade like (1 - L^{1-θ_w})^{-1}, so the price → 0 as θ_w ↓ 1. Say so.
  - **Consequence: BFT as stated is insufficient.** Its claim is existential, "there exist … θ_w ∈ (0, 2]" (REVIEW_S22 l.399).
    PROOF/N5 needs θ_w = 0 and SF needs θ_w > 0 (l.426-427). SQ's need, θ_w > 1, is the strongest, so it must be a
    requirement on lane A.
- **(NA-1) free boundary: ARGUED, plausible.**
  - Reflection invariance gives hol(T) = hol(RT), so contours pair with their reverses, M̄ is Hermitian, and W_0(M̄) = 1 on
    crossing links.
  - Palais applies (a finite group). The S4' reflection covariance remains to be checked.
- **(NA-2): ARGUED, and it is the session's best structural point.**
  - In covariant form, the level-0 step is REG-lin-src (b): sup of dF̂ (the Bianchi defect, link × curvature) and of d*F̂.
  - It is not the abelianised CZ case that q3 B / q3b B4 test.
  - Two caveats:
    - the Wilson EL gives sin-type, not log, currents (a cubic correction);
    - E_𝒞 must be identified with BFT's 𝔉_k restricted to the cone; this is not stated.
- **(NA-3)/(NA-4): ARGUED.** The multiplicative bound on the residual recursion, Π(1 + CL³m_i) < ∞, is the correct mechanism.
  The norm fix S2-3 is needed.
- **(NA-5) "the large-branch exclusion is the genuinely hard critical-dimension step; the sup route moves it": AGREED, and
  sharper than SQ states.**
  - **Circularity (S2-6, binding).** BFT-0's uniqueness ball is ||X||_𝔐 ≤ C_0ε, with 𝔐 weighted by L^{θ_w(k-j)}
    (REVIEW_S22 l.393, 405). Membership already IS the weighted decay.
    - So (MIN-reg)_cone, "every τ_R-small minimiser lies in BFT's ball", implies (REG-min) by itself, at rate θ_w, for the
      sup part of 𝔐.
    - BFT then adds only identification and Hölder regularity, which DESC does not use. DESC needs "every small minimiser in
      Σ_dec" and no uniqueness.
    - The line "(REG-min) ⇐ (BFT-cone) + (MIN-reg)_cone" (l.843-848) is therefore true but nearly tautological. The whole
      wall is (MIN-reg)_cone.
  - **Why it is critical [reviewer ARGUED].** The natural proofs of (MIN-reg)_cone are:
    - (α) uniqueness in a LARGE (unweighted, τ_R-sup) neighbourhood, plus continuation in θ from the flat minimiser;
    - (β) Uhlenbeck-type small-energy regularity.
    - Route (α) in unweighted sup fails uniformly in depth: by SHIFT, unweighted residual sources accumulate (S_j ≈ Σ_i
      sup|s_i|, a factor k). Convexity on the τ_R-sup ball fails too: the fine gap ≈ n^{-2} is far below the unweighted
      curvature τ_R.
    - Route (β) needs the 4D critical Sobolev step ||F||_{L²}·||δa||²_{L⁴} ≤ C||F||_{L²}||∇δa||²_{L²}, i.e. an (MS-Sob)-type
      ℓ⁴ estimate, at one level and in a Coulomb gauge.
    - So the step the sup route was introduced to avoid returns inside (MIN-reg)_cone. Whether the open-wall count actually
      drops (the "merger", §0 fix (4)) is UNDECIDED. It drops only if the single-level ℓ⁴ step is easier than (MS-Sob)/(SQ)
      across levels, which is plausible (lattice Sobolev on one box is depth-uniform) but not shown.
- **SQ's claim "BFT as stated does not apply; a box form is needed" (l.844-846): partly wrong.** BFT's claim already covers
  "every non-wrapping box with the boundary convention of N5-sf0" (REVIEW_S22 l.400-401). What remains is to check that this
  convention is the free (natural) boundary of the cone, and that BFT's data hypothesis (V_k small on every level-k plaquette
  of the box) admits box_k = P alone. **Fix S2-5.**

**What BFT lane A must deliver for (REG-min)**, precisely (these are proposals for lane A's owner):
1. **BFT-0/1 on the cone box with the free boundary.** Either through REFL on the reflection torus of level-k side
   (4, 4, 2, 2), below T_0 (so a small-torus or box version), or in N5-sf0's box form once its convention is confirmed to be
   the free one.
2. **The data hypothesis.** The top is one plaquette's four links, and the constants are uniform in k.
3. **θ_w > 1 strictly, as a stated value, not an existential.** The residual (soft-fluctuation) exponent should preferably be
   ≥ 2 + δ, and its sup part must dominate Σ_dec's (D1)-(D2).
4. **The crucial item: a uniqueness or ε-regularity clause in a ball large enough to contain every cone minimiser whose
   sizes are all < τ_R at every level** (unweighted), or else a separately proven (MIN-reg)_cone. Without item 4, BFT gives
   (REG-min) only for the BFT critical point, and DESC case (iii) does not run.
5. **The identification** of the cone energy E_𝒞(q) (Wilson s + κφ) with 𝔉_k restricted to the cone.

Items 1-3 are BFT-type and plausibly follow from COMP in 𝔐. Item 4 is the critical-dimension step and is not in BFT as
stated.

**Verdict P5: §11.6 is ARGUED throughout and correctly labelled. Its conclusion (relocated, not removed) is CONFIRMED. The
dependence statement needs S2-6 (circularity) and S2-5 (the box clause). Nothing in §11.6 should be counted.**

---

## Priority 6. Re-runs (lock discipline)
- **The hold:** `until mkdir …/locks/numeric; do sleep 20; done`, then q3, q3b and rv.py, then one rmdir.
  - mkdir 04:59:24, rmdir 05:00:36 UTC.
  - Load 3.15 at start, 41% free.
  - nice 10, all BLAS threads 1, python3 without -I, no `timeout`.
  - Peak footprints 202 / 87 / 150 MB.
  - No process was left running.
- **q3 and q3b:** identical to the records in every printed digit.
- **rv.py:** R1 (SHIFT/A1), R2 (REFL), R3 (location of (C)'s sup), as quoted above.
- **SQ's own resource discipline** in session 2 (three holds, each with one mkdir and one rmdir, and all peaks < 1 GB) is
  consistent with SQ_LOG.

---

## Corrected tally

| Item | SQ's status | Reviewer |
|---|---|---|
| Step 1 [RSQ1-fix] | DONE | CONFIRMED (S2-1a, S2-1b wording) |
| Corollary DESC-ε | CONDITIONAL ⇐ (REG-min) | CONFIRMED as CONDITIONAL (M2-1 optional) |
| Lemma TOP | PROVEN, not counted | CONFIRMED |
| Lemma REFL | PROVEN (with REG-lin) | CONFIRMED (hand + R2) |
| Theorem REG-lin | PROVEN given LES-sup, counted | CONFIRMED (M2-3) |
| Lemma SHIFT | PROVEN (with REG-lin-src) | CONFIRMED (R1, non-trivial) |
| Theorem REG-lin-src | PROVEN, counted | CONFIRMED-WITH-FIX (S2-2: compatibility not needed for (b); S2-3 scope; M2-4) |
| q3 | FAIL (QA, QC) | FAIL stands; reading fixes S2-4a-d; A1 exact by construction |
| q3b | PASS | PASS stands; no evidential weight beyond "consistent" |
| "G4-F2 occurs" | stated as fact | ARGUED/expected (CZ), for sup|q_0| alone |
| (NA-0)-(NA-5), BFT dependence | ARGUED | ARGUED; (NA-0) re-derived; S2-5, S2-6 |
| (REG-min) | OPEN | OPEN; its wall = (MIN-reg)_cone (item 4 above) |

**Claimed 8 / 3 / 2 (PROVEN counted / CONDITIONAL / OPEN): CONFIRMED.** That is 6 from session 1 plus REG-lin and
REG-lin-src; PRICE-iii, linear MS-Sob and DESC-ε; (REG-min) and non-abelian (SQ). No item is moved. The fixes are wording and
scope fixes, plus one hypothesis removal that strengthens REG-lin-src (b).

## Binding fixes (next lane-G session)
1. **S2-1a / S2-1b.** Correct the l.284-285 pointer (§11.2, §11.4 (a), not §11.3 / q3). Reconcile l.286 ("level weights")
   with l.744: level weights are needed for general currents, not for paired residual sources.
2. **S2-2.** REG-lin-src (b): drop the boundary-compatibility hypothesis; keep it for (c). Rename λ_0 at l.656.
3. **S2-3.** Scope "no level weights" / "loses NOTHING for residual sources" (l.744, 773-778, 805, 866) to paired
   energy-residual sources. In (NA-3)/(NA-4), use residual weight L^{3(k-1-i)} (or exponent > 2) in 𝔑, with the reason (the
   level count of unpaired EL currents).
4. **S2-4a-d.** q3 reading (l.795-805):
   - A1's zeros are exact by construction;
   - (A) is the top-datum test, so it neither confirms nor refutes REVIEW_SQ_S1's level sum, and SHIFT plus REVIEW_SQ_S2 R1
     carry that claim;
   - QB's PASS is as confounded as QA's FAIL;
   - q3b's doubling is matched by q2's provably bounded doubling;
   - the "(C) flat anyway" caveat is false in d = 3, where the growth is interior (R3);
   - "G4-F2 OCCURS" (l.782, 868) → "expected (CZ), not proven".
5. **S2-5.** l.844-846: BFT includes a box clause (N5-sf0 convention); check it instead of asserting non-applicability.
6. **S2-6.** l.843-848: state that (MIN-reg)_cone with BFT's 𝔐-ball already implies (REG-min). The wall is (MIN-reg)_cone, and
   lane A must deliver items 1-5 above, item 4 being the critical one. State that θ_w > 1 must be required of BFT, not
   assumed (BFT is existential in θ_w).
7. **Minor.**
   - M2-1: sharper level-0 size in DESC-ε (iii).
   - M2-2: note in SQ that q3's "centre of P" is the centre of P's corner block.
   - M2-3: "not contradicted" in place of "consistent" at REG-lin Remark (2).
   - M2-4: (c) at k ≤ 2.
   - M2-5: (NA-0) should say that the constants blow up as θ_w ↓ 1.
   - M2-6: (NA-2) should note the sin-versus-log EL correction and the E_𝒞 ↔ 𝔉_k identification.

## Strategic verdict
1. **Keep the linear package.**
   - REG-lin is a clean, depth-uniform, torus-free linear theorem. REFL is a reusable device for every cone-local lane (it
     turns free boundaries into interior estimates on Z⁴ with no torus side condition).
   - SHIFT shows that energy-residual sources cost no level sum.
   - REG-lin-src (b) shows that level-0 sources cost nothing once sup|dq| is controlled. (b) is the right linear input for
     (NA-2).
2. **The headline numerics claim is weaker than written.** q3 does not test the level sum (A1 is degenerate). The non-trivial
   test is REVIEW_SQ_S2 R1, which supports SHIFT. The CZ loss at level 0 is expected classically, and q3/q3b are merely
   consistent with it.
3. **The wall did not move closer.**
   - (REG-min) ⟸ (MIN-reg)_cone essentially alone, and (MIN-reg)_cone needs either large-ball uniqueness (which fails in
     unweighted sup by a depth factor) or Uhlenbeck-type small-energy regularity (a single-level critical ℓ⁴ step).
   - So the sup route trades multi-level (SQ)/(MS-Sob) for a single-level (MS-Sob)-type step inside (MIN-reg)_cone. That may
     be a real gain (single-box lattice Sobolev is depth-uniform), but it is unproven. Keep (SQ-dev) as the parallel route.
4. **Recommended next target.**
   - Write (MIN-reg)_cone as a precise lemma. Try route (β): one level, Coulomb gauge on box_0 via REFL, small cone energy
     E_𝒞 ≤ κ_+θ²/2, and τ_R-sup at every level.
   - Find out whether the ℓ⁴ step there is single-level and depth-uniform. That one question decides whether lane G's merger
     reduces the wall count.
   - In parallel, send BFT lane A items 1-5, with item 4 and θ_w > 1 flagged as SQ's requirements.
5. **Do not:**
   - cite q3 A1 as a measurement of SHIFT;
   - cite q3b as evidence of growth;
   - describe (REG-min) ⇐ BFT as a reduction while (MIN-reg)_cone is unaddressed;
   - count anything in §11.6.
