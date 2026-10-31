# REVIEW_SF_S4: hostile review of lane F session 4 (SF.md [RSF3-fix] edits; §12-§14: Theorem CE-Q-col with Lemmas HALO, SH; Corollary RATE-Q; Lemmas GD, DL, SLc (+ SLc-X), TILT; Proposition RES; (SL-coer′); Proposition DX; RT-1 (§13.3); circularity check; check s4)

Reviewer: an independent agent that wrote none of SF.md. I edited no file except this one. No commits, PRs or pushes.

Inputs (read 2026-10-28 ~05:35-05:55 UTC):
- SF.md §12-§14 l.1351-1749 in full; [RSF3-fix] spots l.578-583, 987-991, 1025-1030, 1045-1058, 1066-1070, 1121-1125,
  1184-1216, 1229-1233, 1298-1304, 1313-1340; l.61-64, 120-127, 141-146, 355-366, 820-828; SF_LOG.md in full (incl. the
  proposed RLARGE owner note); REVIEW_SF_S3.md in full.
- checks/s4_criteria.md, s4_out.txt, s4_time.txt in full; s4_sf.py constants + C-section (l.152-277) line by line, rest skimmed.
- RLARGE.md §3 l.287-380 (md5 24a73553… = SF's read). PROOF.md NA-FP l.3040-3080. PLD §15.4 l.1118-1136. HIST (H-w) l.528-540,
  (MSG) Target S4 l.1144-1160.
- md5 now: SF e6835ab9… (= SF_LOG final), s4_criteria 06c44d6a… (= SF_LOG), s4_sf.py fa1fcd37…, s4_out 1cd744d2… (= SF_LOG).

Scratch: scratchpad `revSF4/` (indep.py = my independent re-derivation, indep_out.txt, rev_s4_out.txt, rev_time.txt, rev_lock.txt).

---

## Bottom line

- **RSF3 fixes: all 11 binding items applied** (Q1-Q6, C-1..C-5, SN-1, SN-2, RT-1, stale text, tally, check design). One
  cosmetic slip: §12.1 l.1384 "κ_c > κ_0 + 3κ̃_0 + 5 (≈ 808.5)" is **807.46**.
- **RT-1: CONFIRMED, and my session-3 number was the wrong one to iterate.** Re-derived independently (indep.py, not their code):
  the iteration condition measures the blocked d ≥ 1 activity at the NEXT stage's input rate κ_in = κ_c + 16 log 2 + 1296w_8,
  and closes from **κ_c ≥ 2499.39** (CE-col) / **2938.18** (CE-Q-col). 1853.49 / 2073.23 are the same-rate forms. The shift
  645.90 = κ_in - κ is exact; slope of the log ratio is -1 in κ_c in both forms.
- **Theorem CE-Q-col: analytic part CONFIRMED (counted).** HALO (a)-(f), SH, Steps 0-6, the rate κ_c - κ_0 - 3κ̃_0 - 5, RATE-Q
  1478.49, M and p_0 g-independent: all re-derived. One numeric precision: p_0 ≈ 4.24·10⁴ is at κ_c = 1478.5; at the norm-closing
  κ_c = 2938.2 it is **≈ 6.45·10⁴** (still g-independent).
- **(SL-coer) chain:** GD CONFIRMED-WITH-FIX (constants do change; "verbatim" overstated). DL CONFIRMED-WITH-FIX (a block-size
  factor). SLc, SLc-X, TILT CONFIRMED. **RES CONFIRMED**: exact residual-gauge copies inside ker h_U, no defect. It is consistent
  with (FP-loc)'s uniqueness clause only because the residual gauge is 't Hooft-averaged, not fixed; it does identify a
  Gribov-type (soft-gauge uniqueness) issue.
- **Proposition DX: inclusion CONFIRMED; the (P)/kernel pricing line is WRONG as written (Fix DX-1, binding).** Wilson positivity
  is an absolute bound; against the expansion's normalisation it loses the background action of the whole removed region
  ((2R_*+1)⁴ ≳ 10⁴² cubes, since 1/μ ≈ 2·10¹⁰), not one plaquette's ε_bg²/2. So a' as displayed is not proven.
- **(SL-coer′): well-posed only after Fix SC-1** (K must be fixed before v). On SF's chart (link radius ≈ ½) it is a genuine local
  Gribov statement, and it is at real risk of being false at O(1) amplitude. Recommended: reformulate on a shrunk chart; this
  reduces it to (MSG)_0 + a local inverse-function uniqueness (Part C-6).
- **Circularity: the order O1 → O4 is sound for the items listed, but one region is unassigned.** The chart complement
  (SF-A2^0 l.362 "priced elsewhere") is a fluctuation large field, i.e. branch (ii)'s domain. Unless it is put in (O2), the
  circle reopens. Two further conditions (Part D).
- **s4: honest and reproduced.** Criteria born 05:22:00 UTC, before the script (05:24:27). Re-run under the lock is
  byte-identical except the runtime line: **OVERALL PASS 21/21**.
- **Corrected tally (after session 4):**
  - PROVEN-HERE 34 + 1 standard (counted 10, not counted 24): SF's numbers stand.
  - CONDITIONAL 7, with DX scoped down to the inclusion + (F) factor.
  - ARGUED 1 ((CE-s)) + 1 new (DX's (P)/kernel exponent, by Fix DX-1).
  - 0 GAP, 0 WRONG items (the wrong sub-line is withdrawn by DX-1).
  - New OPEN names: (CH-c), (DX-rel). No PROOF.md tally change.

---

# PART A: [RSF3-fix] edits (fix number = REVIEW_SF_S3 Part F)

| # | SF line | verdict | note / fix |
|---|---|---|---|
| 1 Q1 | l.1188-1192 | CONFIRMED | H'_0 ≤ c_0(κ_c) added. The CE-Q-col analogue is l.1492-1493, inside c̃_0(κ_c). |
| 2 Q2 | l.1186-1187, l.1526 | CONFIRMED | |
| 3 Q3 | l.1123-1125, l.1027 | CONFIRMED | |
| 4 Q4 | §12.1/§13.1 | CONFIRMED | Done as CE-Q-col (Part B). l.578-583 and l.987-991 corrected. |
| 5 Q5/Q6 | l.1027-1028, l.1205 | CONFIRMED | |
| 6 C-1..C-5 | l.1055-1058, l.1211-1212, §13.2 | CONFIRMED (wording); content in Part C-D | The branch-(ii) handoff is withdrawn (SF_LOG "Withdrawn"). |
| 7 SN-1/SN-2 | l.1231-1233, l.1068-1070 | CONFIRMED | 1.039844 reproduced. (BGC) is an explicit hypothesis. |
| 8 RT-1 | l.1302-1304, §13.3, l.1708 | CONFIRMED (Part B-6) | My "≈ 1854" was the same-rate form; 2499.4 is the iteration condition. |
| 9 stale | l.1027, l.1047-1049 | CONFIRMED | **New cosmetic:** l.1384 "≈ 808.5" → 807.46 (κ_0 + 3κ̃_0 + 5 = 151.315 + 651.142 + 5). |
| 10 tally | l.1330-1331 | CONFIRMED | |
| 11 checks | l.1343, §14.3 | CONFIRMED | s4 now tests CE-Q-col constants (A: HALO, B: SH), as asked. |

---

# PART B: Theorem CE-Q-col, HALO, SH, RATE-Q, RT-1

### B-1. Lemma HALO (l.1374-1377, proof l.1439-1451): CONFIRMED (not counted)
- ℓ^∞ geodesic dilation identity: correct.
- (b): class separation ≥ 8 ⇒ D ≥ ℓ + 7, so n(y, U_α) = dist(q(y), U_α^+) = D - 8 ≥ ℓ - 1. The bound is **tight**: my
  independent d = 2 run found 32 of 878 pairs with equality. So the ℓ/2 weakening, and the 4 log 2 in ℓ_j, are needed. This
  agrees with A7.
- (c) D - 2 ≥ ℓ + 5 ✓. (d) radii ℓ + 1, ℓ + 6, ℓ + 7 ✓. (e) ✓.
- (f): (a) μMℓ ≥ 4(j + 1)log 2; (b) μMℓ/2 ≥ 2(j + 1)log 2; (c) margin + 4μM. Each gives 2^{j+1}e^{-μδ} ≤ e^{-μδ/2} and
  (1 + r_y)2^{j+1} ≤ 2e^{μδ} ✓.
- Independent check: HALO (b) 0/878 violations, (c) 0/3 (indep_out.txt).

### B-2. Lemma SH (l.1380-1382, proof l.1456-1462): CONFIRMED (not counted)
- ℓ_j ≥ 2 ⇒ j + 1 > J_M = μM/(4 log 2) ≥ 3.6κ' ((M-W3): μM ≥ 10κ' + 16).
- c_Γ(23j)⁴ ≤ 2.8·10⁵j⁵ needs j ≥ c_Γ, which holds since 3.6κ' - 1 ≥ 3κ' ≥ c_Γ.
- 4^j ≥ 4.5·10⁶j⁵ for j ≥ 25 ✓; (4^j - 1)p²/32 ≥ 4^j/16 for p ≥ 2 ✓.
- Independent sweep (κ_c ∈ {809, 900, 1478.5, 2938.2, 5·10⁴}, μM ∈ {1, 1.5, 4, 100}×μM_W3, p ∈ {2, 2.01, 3, 10},
  h_0 ∈ {0, ½, 1}, j through the ℓ_j-jumps): 7.8·10⁸ pointwise tests, 0 violations.

### B-3. Theorem CE-Q-col Steps 0-3 (l.1471-1490): CONFIRMED
- Step 2's four field contributions re-derived:
  - other-class sites: 2^{j+1}e^{-μMℓ_j} ≤ 2^{-3(j+1)}, total ≤ g_0√NpN_μe^{-4μM}/8 ≤ ρ'/2;
  - S-sites ≤ ρ'.
  This gives |A_b| ≤ 2ρ' + σ ≤ ρ_* (B1′).
- Small X: Q-sites in S cost ≤ e^{-μδ/2} by HALO (a), (f). Regrouping is CE-exp-col at rate μ/2, so H''_0 = 2^{16}e^{1296w_8}h_0 ✓.
- Step 3: QC's Hölder bound does not depend on |W_α|; only the baseline grows, to 2h_0Σ(2ℓ + 3)⁴ ✓.

### B-4. Steps 4-6 (l.1491-1531): CONFIRMED
- **Mayer step.** The condition H''_0 ≤ (32K_0)^{-1}e^{-6(κ_c-κ_0)} is c̃_0's second entry ✓ (l.1083).
- **Readability.**
  - Smallness of X inside 𝒵_k is decided by the cluster's own computed R.
  - Other clusters' halos lie in their own U_β, which is disjoint from 𝒵_k^+.
  - So the (⇐) direction holds even though halo radii depend on Z at the Q-sites.
  - Q-sites reached through S, or through a core's collar, force the collars to meet (same cluster) ✓.
- **Mixed part.**
  - κ̂ = κ_1 - κ̃_0 ✓.
  - Spanning tree: e^{6κ̂} per member ✓.
  - Cores ≤ exp(e^{6κ̂}C_KH''_0K̃_0|𝒵|) ✓.
  - G-members: Γ_j collects 2κ̂(2ℓ + 13)⁴ (d(U_α)), w_8(2ℓ + 15)⁴ (S-sum over U_α^+) and 2h_0(2ℓ + 3)⁴ (baseline) ✓.
  - Shell: 2^{n/2}e^{-4^jp²/4} × 1/μ_1(good) ≤ 2, × SH's 2 = 2^{n/2+2} ✓.
  - Σ_{Q≠∅} ≤ M⁴|𝒵|η̂e^{M⁴|𝒵|η̂}, with |𝒵|/16 ≤ 1 + d^+ ⇒ 16eM⁴η̂e^{-(κ̂-2)d^+} ✓.
- **Step 6.** κ = κ_c - κ̃_0 - 2 ⇒ κ_1(κ) = κ̂ - 2 ✓. Hypothesis κ_c > κ_0 + 3κ̃_0 + 5 ✓. Third entry
  (8B̃)^{-1}e^{-6(κ_c-κ_0-3κ̃_0-4)} ✓. Output rate κ_c - κ_0 - 3κ̃_0 - 5 ✓.
- **Post-proof hypothesis p² ≥ 4(n log 2 + 2).** Correctly added. With GD's n_B ≤ 4L⁴(N² - 1) (2592 for N = 3) it still holds
  at p_0 (indep).

### B-5. g-independence, p_0, RATE-Q: CONFIRMED with one precision
- M_W3 = 3.14·10¹⁴ ✓.
- p_0: 4.2371·10⁴ at κ_c = 1478.5 reproduced (indep). **But the band only iterates (norm) from κ_c ≥ 2938.2, where p_0 ≈ 6.45·10⁴.**
  Fix CQ-1: quote p_0 at the κ_c actually used, or as a function of κ_c (√(32·15⁴κ̂) to leading order).
- RATE-Q: 3(κ_c - 2κ_0 - 3κ̃_0 - 5 - 16 log 2) - 1 ≥ κ_c + 16 log 2 + 1296w_8 ⇔ κ_c ≥ 1478.49 ✓.
- The rise is 3(κ̃_0 + 2)/2 = 328.57 ✓. My session-3 "≈ 230" assumed a κ_0 + 2 loss, but the cores are 2-connected and lose κ̃_0.
  SF is right.
- The B-7 consumers keep g-independent constants on this route ✓.
- **Minor (not binding):** at k ≥ 1, the fine halo radius ≈ 4(j + 1)log 2/μ + M is ≈ 5.7·10¹⁰(j + 1). For the last levels this
  meets the torus constraint T_k (REVIEW_SF_S3 B-7 item 6). Record it in the torus-size caveat.

### B-6. RT-1 (§13.3): CONFIRMED (re-derived independently)
The norm condition is blocked d ≥ 1 activity × 2^{16}e^{1296w_8} ≤ H''_0 (fixed point). In logs:
log C̃_1 + log fac + 16 log 2 + r + log(16L⁴K_0) - [(κ - κ_0)L - 1 - κ_cmp] + 16 log 2 + 1296w_8 ≤ 0, with κ = r - 16 log 2.
- κ_cmp = κ (same rate) gives 1853.49. At 1149.92 the log ratio is 703.57.
- κ_cmp = κ_in gives **2499.39**. The rate exponent there is +2698.9.
- CE-Q-col (r_Q, factor 2): 2073.23 / **2938.18**.
- The next stage's CE-exp-col consumes (H-exp)(κ_in, h_0), so the κ_in form is the iteration condition. **RT-1 as written in SF
  is right, and REVIEW_SF_S3's ≈ 1854 must not be cited as the iteration threshold.**

---

# PART C: the (SL-coer) chain

### C-1. Lemma GD (l.1405-1409, l.1550-1559): CONFIRMED-WITH-FIX
- A = g_0√N𝒞Π_UZ ✓. Π_U block-diagonal (h_U uses block-internal axial paths only) ✓. Independent Gaussian splitting ✓.
  Õ^{1/2}𝒞 = Π_U (Õ^{-1/2} = 𝒞 + (1 - Π_U) is Π_U-block-diagonal) ✓.
- **Fix GD-1.** "Hold verbatim" is too strong. With blocks as sites:
  - QC's column bound becomes N_c ≤ 4L⁴N_0, so C_3^Q, C_2^Q (∝ N_0³, N_0²) grow by up to L⁴;
  - n → n_B changes η̂ and the p² ≥ 4(n log 2 + 2) condition;
  - M⁴ → (M/L)⁴ and L | M.
  Restate (B1′)-(B3) and a_* with these constants. All stay g-independent.

### C-2. Lemma DL (l.1410-1411, l.1561-1567): CONFIRMED-WITH-FIX
- Submultiplicativity and finiteness ✓.
- **Fix DL-1.** |v_B| is a norm over the 4L⁴ links of B, so the B-row sum is ≤ 4L⁴e^{μ·diam B}·N_μ(|Õ^{1/2}|), not N_μ. Put this
  factor into a_deep. It is g-independent and harmless.
- **Note.** On SF's chart, ||1 - e^{A_b}||_op ≤ ε^thr_N ≤ ½ (SF-A2^0 l.361; SF-thr), so |A_b| ≤ 1.011√N/2, not π√N. R_DL can
  use that.
- **Scale.** R_DL = μ^{-1}log(·) with μ = m_1 = 4.83·10⁻¹¹, i.e. ≳ 2·10¹⁰ fine spacings. This matters for DX-1.

### C-3. Lemma SLc and Corollary SLc-X (l.1569-1597): CONFIRMED
- SF-T0 (4) uses ρ = max over the pattern (l.125), so (4ρ_τ)³ ≤ 64ρ_Ωρ_τ² ≤ 64ρ_ΩΣ_{P_τ}|A|² ✓.
- |1_ΩA|² = g_0²N||C||⟨v, K_Ωv⟩; ||K_Ω|| ≤ ||𝒞||²/||C|| = 1; tr K_Ω ≤ (N² - 1)|Ω| ✓.
- C_coer, C' and the linear source term ✓. The operator-form remark (avoid an N_0² loss) is correct.
- SLc-X: the θ ↔ TILT factor-2 conversion and a_θ = (1 - 4C'g_0²)/(4C_coer) (θ ≤ ½) ✓ (post-proof fix right).
- Note the range: C_coer ∝ 1024·r_T^{-3} ≥ 5·10⁵, so a_θ ≲ 10⁻⁶-10⁻⁷. Between a_θ and the chart radius ≈ ½ nothing is proven.
  That gap is where (SL-coer′) lives.

### C-4. Lemma TILT (l.1582-1587): CONFIRMED
- The algebra θ'' = (1 + θ)/2 is right; -log(1 - x) ≤ x/(1 - x) ✓; the bound is dimension-free ✓.
- The infinite-variance remark is right: E e^{θkv²} < ∞ iff θk < ½. So for θ = 0.9 the plain-MC D1 numbers are unreliable, and
  only the exact-tilt reference is evidential.

### C-5. Proposition RES (l.1599-1615): CONFIRMED (negative; not counted)
- F(λ) = h_U(A(λ)) on Λ. DF(0) = -h_U∘D_U|_Λ = -M_U, which is onto (NA-FP (i)-(ii), PROOF l.3058-3074) ✓.
- 𝒩 has dimension dim Λ_res^U > 0 ✓. e^{A(λ)}U = gUg^{-1} with g(c_X) = 1, so plaquettes, M̄_c and 𝔫_c are unchanged ✓.
- **Verified: my session-3 (SL-coer) wording is FALSE on ker h_U.** I omitted the Feynman term.
- **Gribov question (asked).** RES does NOT contradict (FP-loc)'s "uniqueness of the slice intersection".
  - NA-FP's fixing is χ_U = (h_U, P_res^UD_U^*). The h_U part is a δ-constraint; the residual part is 't Hooft-averaged, weight
    e^{-½||P_res^UD_U^*A||²} (PROOF l.3062-3063).
  - So "uniqueness" means: for each ω, the orbit meets {h_U = 0, P_res^UD_U^*A = ω} once in the chart. RES's 𝒩 is the residual
    orbit, and uniqueness requires λ ↦ P_res^UD_U^*A(λ) to be injective along it.
  - (F) failing near b_0 means that map is nearly non-injective (small Feynman energy at large A): a **soft-gauge Gribov copy**.
  - So yes: this is a Gribov-type issue of the slice. It sits exactly in (FP-loc)'s nonlinear uniqueness clause, as SF says.
- Cosmetic: l.1614 "e^{u_0H(A,A)/2}" should carry the 1/N of SF-A2^0's (u_0/2N) normalisation.

### C-6. (SL-coer′) (l.1617-1630): OPEN, correctly named; well-posed only after Fix SC-1; strategic risk
- **SC-1 (binding).** (F) says "there is a K ≥ 0 …" per configuration. Lemma TILT needs K fixed before integrating over v. A
  configuration-dependent K is not usable.
  - Restate: K belongs to a family 𝒦(b_0, Ω) fixed in advance, of cardinality ≤ e^{C|Ω|}, determined by local data. Union over the
    family; the cost is local.
  - Or fix K := K_Ω and weaken (F) accordingly.
- **SC-2 (binding).** "The Ω-terms of ΣH" omits terms whose pattern straddles ∂Ω. Say explicitly that they go to (DX-loc).
- **SC-3 (statement of the chart).** The chart is SF's link-wise chart, ||1 - U_0U(V)^{-1}||_op ≤ ε^thr_N (≈ ½). Write this into
  (SL-coer′).
- **Risk (reviewer's judgement, no counterexample constructed).**
  - Moderate-amplitude lattice Gribov copies of Landau/'t Hooft-type conditions are generic.
  - The inverse-function theorem protects only a radius r_FP set by the ℓ^∞ → ℓ^∞ norm of (χ_UΓ)^{-1}, far below ½.
  - So (SL-coer′) on the ½-chart may be false, and it should not be attacked in that form.
- **Recommended reformulation (ARGUED here, not proven).**
  1. Shrink the chart to r_ch ≤ min{r_FP, ρ_*, a_θ}.
  2. (MSG)_0, the single-scale stage-0 case of HIST Target S4 (bounded-box complete axial gauge): if all plaquettes in a
     bounded box around x are < τ, the orbit has a representative with |log| ≤ C_Mτ there. This is elementary at one scale.
  3. A local inverse-function step from the axial representative to the χ_U representative, with an ℓ^∞-local (exponentially
     decaying) inverse of χ_UΓ. Uniqueness inside r_ch follows.
  4. Radius compatibility C_M·C_IFT·τ_c ≤ r_ch.

  Then every in-chart configuration has |A| ≤ r_ch, so SLc gives (F) for every deep block, with no U-variable defect needed. An
  orbit with no in-chart representative has a plaquette defect within a BOUNDED box (by 2-3). Large residual-orbit excursions
  are priced by the 't Hooft ω-weight itself.

  This turns the wall into (MSG)_0 + locality of (χ_UΓ)^{-1} (an N5/FP_U-type item), both outside Gribov territory. It also
  removes DX-1, because the defect is then O(1)-close to the bad link, not R_* ≈ 10¹⁰-10¹² away. Coordinate with the HIST
  (MSG) owner.

### C-7. Proposition DX (l.1632-1653): inclusion CONFIRMED; pricing line WRONG as written
- **Inclusion.** DL + (SL-coer′) at b_0 + the multiplicity (2R_* + 1)⁴: correct as CONDITIONAL ⇐ (SL-coer′) + (FP-loc)_0 + (BGC).
  The (F) factor via TILT is correct: it is a white-noise bound relative to the Gaussian, and the background action cancels.
- **Fix DX-1 (binding).** The (P) factor "e^{-u_0τ_c²/(2N)}, up to the background's s(U_p) ≤ ε_bg²/2" is wrong as written.
  - Wilson positivity bounds e^{-u_0S(U_0)} absolutely. The expansion's normalisation carries e^{-u_0S(U)} on the removed region.
  - Their ratio is ≤ e^{-u_0s(p_def) + u_0Σ_{p∈removed}s(U_p)}: the subtraction runs over EVERY plaquette of the removed region,
    not one. The same holds for the kernel terms' background values.
  - The removed region around a deep block has ≳ (2R_DL)⁴ ≳ 10⁴² cubes. So "τ_c²/(2N) - ε_bg²/2" in a' must be
    τ_c²/(2N) - Σ_{removed}s(U_p) (and the kernel analogue). That is negative unless ε_bg ≲ 10⁻²¹τ_c, which (BGC) does not give.
  - Either price relatively, by a local excess over the background (a stage-0 CLS-sf-type bound; name it **(DX-rel)**), or use
    the C-6 reformulation (bounded box).
  - Until then, the (P)/kernel exponent of a' is ARGUED. DX's "statement as proven" is the inclusion plus the (F) factor.
- **Fix DX-2.** "RLARGE branch (i) (PROVEN)" is the wrong citation at stage 0.
  - Branch (i) is a conditional probability of V given U, with its in-history caveat H-4 ARGUED.
  - Stage 0 integrates U_0 at fixed V, so what is needed is the pointwise kernel-factor bound, which is elementary. SF already
    puts that form in (DX-loc) (l.1643).
  - (O2) must not list branch (i) as a PROVEN input.

---

# PART D: circularity (l.1655-1672)

**Verdict: the order O1 → O2 → O3 → O4 is sound for the items listed; one region is unassigned, and two conditions must be recorded.**
- **O1 (CE-Q-col) ⇐ (FP-loc)_0 + (BGC).** No (SG^fl), no branch ✓. (FP-loc) is a PROOF NA-FP item and consumes no large-field
  pricing.
- **O2 (DX) ⇐ (SL-coer′) + (FP-loc)_0 + (BGC) + TILT (+ DX-2's pointwise kernel bound) + (DX-loc)** ✓. No branch (ii).
- **Gap D-1 (binding): the chart complement.**
  - SF-A2^0 (l.361-362) restricts the exact change of variables to ||1 - U_0U(V)^{-1}||_op ≤ ε^thr_N. The complement is "a
    fluctuation large field, priced elsewhere".
  - Nothing in §13.2 prices it. It is precisely branch (ii)'s domain (fluctuation about the background).
  - If it is sent to branch (ii), the circle (ii) ⇐ (SG^fl)_0 ⇐ (SF)_0 reopens.
  - Name it **(CH-c)** and put it in O2: by (SL-coer′)-type defect-or-copy reasoning on Haar variables, or by C-6's bounded-box
    route. The restated (CE-Q^∞) = DX + (DX-loc) + (CH-c).
- **Condition D-2.** (DX-loc) may use (H-w)'s B_0-per-cube normalisation parts (HIST l.536-540 (a)-(c): Lemma TD, the E_0 bound,
  normalisation mismatch). It may NOT use (H-w)'s unreturned-weight sources, which list (PLD) = branches (ii)+(iii) under v2
  (HIST l.535-536). Otherwise the loop returns through HIST.
- **D-3 (completeness, no loop found).** (O3)'s input list omits RLARGE l.320-322's (I_0^E), threshold compatibility and (BG)_0.
  None consumes branch (ii) as far as I can see:
  - (BG)_0 is background locality (an SF/N2 item);
  - (I_0^E) is the bare representation;
  - PLD (G0-1)-(G0-4) (l.1120-1133) use Lemma AX box gauges, RW, Lemma KN and (SF)_0 only.
  Add them to the (O3) list.
- **k ≥ 1.** Well-founded induction, not a loop: (I_k^E) is the level-(k-1) output, and (MSG)/(MS-Sob)/(AE) are deterministic
  gauge/Sobolev statements (HIST l.1073, l.1144-1160) with no (SF) or (SG) input. But branch (iii) is ARGUED, so (O2_k) is at most
  ARGUED at k ≥ 1.
- **Owner note for RLARGE (amend SF_LOG's proposal):** read "(SF)_k's cluster expansion" as "CE-Q-col + DX + (DX-loc) + (CH-c)".

---

# PART E: s4 (MANDATORY NUMERIC LOCK)

- **Provenance.** Born-time order is clean, and every md5 equals SF_LOG's:
  - s4_criteria.md born = mod 05:22:00 UTC (stat 01:22:00 EDT);
  - s4_sf.py born 05:24:27;
  - out/time born 05:25:24, mod 05:25:32.
- **Re-run.**
  - `until mkdir …/locks/numeric …; do sleep 20; done`: acquired 05:43:58 UTC at once, load 4.17 (< 8).
  - nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`; no trap.
  - Run: 7.31 s, peak RSS 254 MB, exit 0.
  - **Output identical to checks/s4_out.txt except the runtime line: OVERALL PASS 21/21.**
  - My independent indep.py ran in the same lock window and in one more locked window (05:44:15-05:51:18 UTC, after an overflow
    fix). Each acquisition was paired with exactly one rmdir. No process was left running (pgrep empty).
  - Record: revSF4/rev_lock.txt.
- **Code review.**
  - C-section formulas match the criteria; muM_W3 solves (M-W3) ✓.
  - C8 uses n = 32 (sites, not GD's blocks) and h_0 = 0. It is immaterial (indep: n_B = 2592 gives the same p_0 to 4 digits).
  - The C4 printout's "rate exponent" uses κ = r - 16 log 2: fine.
- **Evidential power.**
  - A (HALO) is real: the A7 negative control and my tight cases agree.
  - B is moderate.
  - D1 is low (a theorem; infinite-variance MC).
  - D2's evidential part is the existence of non-small zeros of h∘A. That is confirmed, but at max|A| ≈ 0.35-0.50, far above r_FP.
    This is consistent with C-6's risk: the copies already sit near chart scale.
  - C is arithmetic.

---

# PART F: corrected tally and binding fixes

**Tally of SF.md after session 4:**
- **PROVEN-HERE 34 + 1 standard** (counted 10, incl. CE-Q-col analytic part, CONFIRMED; not counted 24):
  - HALO, SH, SLc, TILT, RES: CONFIRMED;
  - GD, DL: CONFIRMED-WITH-FIX (constants);
  - SLc-X, RATE-Q, RATE (with RT-1): CONFIRMED, listed but not added.
- **CONDITIONAL 7.** DX is scoped to the inclusion + (F) factor (DX-1).
- **ARGUED 2:** (CE-s); DX's (P)/kernel exponent a'.
- **OPEN names:** (SL-coer′) (with SC-1..SC-3), (DX-loc), **(DX-rel)**, **(CH-c)**, plus all of session 3's.
- 0 GAP, 0 WRONG items. No PROOF.md tally change. No RLARGE §4.2 row discharged.

**Binding fixes (next SF session):**
1. **DX-1:** subtract the background action (and kernel values) of the whole removed region in a', or price relatively
   ((DX-rel)). Downgrade the (P)/kernel exponent to ARGUED until then.
2. **DX-2:** at stage 0, cite the pointwise kernel-factor bound, not branch (i) (PROVEN, with H-4); fix (O2)'s input list.
3. **SC-1:** quantify K before v (a fixed family of size e^{C|Ω|}) in (SL-coer′) (F). **SC-2:** boundary-straddling terms →
   (DX-loc). **SC-3:** state the chart (ε^thr_N ≈ ½) inside (SL-coer′).
4. **D-1:** name (CH-c), the chart complement of SF-A2^0 l.362. Put it in (O2), not branch (ii). Restated (CE-Q^∞) =
   DX + (DX-loc) + (CH-c).
5. **D-2:** record that (DX-loc) uses only (H-w)'s normalisation parts (a)-(c), never its (PLD)/branch-(ii) sources.
   **D-3:** complete (O3)'s inputs ((I_0^E), (BG)_0, thresholds).
6. **GD-1:** restate (B1′)-(B3), a_*, η̂ with block constants (N_c ≤ 4L⁴N_0, n_B, (M/L)⁴, L | M).
   **DL-1:** the 4L⁴e^{μ·diam B} factor in a_deep; use the chart radius ≈ ½√N in R_DL.
7. **CQ-1:** p_0 ≈ 6.45·10⁴ at the norm-closing κ_c = 2938.2 (4.24·10⁴ only at the rate threshold). l.1384: 808.5 → 807.46.
8. **RT-1 citations:** cite 2499.4 / 2938.2 as THE iteration thresholds everywhere. REVIEW_SF_S3's 1854 is the same-rate form
   only.
9. Cosmetic: the 1/N in RES l.1614. The k ≥ 1 halo-vs-torus caveat (B-5).

---

# PART G: strategic verdict on (SL-coer′)

**CE-Q-col is a solid, iterable gain: the band composes from κ_c ≈ 2.94·10³ in rate and d ≥ 1 norm, with g-independent M and
p_0. The deep part is correctly re-diagnosed: RES is right, and the residual-gauge Feynman energy must count. (SL-coer′) is a
real, well-identified wall: the soft-gauge (Gribov-type) uniqueness of χ_U, localised.**

- **Do not attack it as stated, on the ½-chart.**
  - There, (SL-coer′) is a moderate-amplitude Gribov statement that may well be false.
  - The DX pricing built on it has a background-action leak over a 10⁴²-cube region (DX-1).
- **Reformulate (C-6):**
  - shrink the chart to the local inverse-function radius (r_ch ≤ min{r_FP, ρ_*, a_θ});
  - prove (MSG)_0 (one-scale bounded-box axial gauge, elementary) and the ℓ^∞-locality of (χ_UΓ)^{-1} (an N5/FP_U-type item);
  - get (F) for every deep block from SLc + TILT, and plaquette defects in BOUNDED boxes for the chart complement (CH-c).

  This removes the Gribov content from the wall, cures DX-1, assigns (CH-c), and shares (MSG) with HIST Target S4 at k = 0.
- **Order of attack:**
  1. SC-1 / D-1 / DX-1 / DX-2 wording;
  2. the shrunk-chart reformulation with (MSG)_0 and the IFT locality;
  3. (DX-loc) under D-2;
  4. (SF-irr) stays the A4 wall.
