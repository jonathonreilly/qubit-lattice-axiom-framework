# REVIEW_SF_S3: hostile review of lane F session 3 (SF.md [RSF2-fix] edits; §9-§11: Lemmas LOC-s′, QC, Theorem CE-Q (band), (CE-Q^∞), Lemma SF-N♮, Lemma GEO-col, Theorem CE-col, Corollary CE-exp-col, Proposition RATE; check s3)

Reviewer: an independent agent that wrote none of SF.md. I edited no file except this one. No commits, PRs or pushes.

Inputs (read 2026-10-28 ~04:40-05:10 UTC):
- SF.md §0 l.1-38, §2 l.61-135, l.176-186, l.224-237, §3 l.260-275, l.330-346, l.386-392, l.436-446, l.501-512, l.560-585,
  §6-§8 l.618-999, §9-§11 l.1001-1303 in full; SF_LOG.md in full; REVIEW_SF_S2.md in full (binding list, Part G).
- checks/s3_criteria.md, s3_sf.py (line by line), s3_out.txt, s3_time.txt; birth/mod times (`stat`).
- PROOF.md Theorem CE, Lemmas CE-geo, TG l.1857-2028; CE-geo' + new constants l.2264-2293; [S22] Proposition NAH-unif′ l.6250-6259.
- RLARGE.md §0 l.40-104, §2-§4.2 l.227-411 (branch (ii) l.310-331). HIST.md TERM-an/NORM-an D_c(y_0) l.1565-1569, l.1628-1633.
  FLOW.md Lemma F-Π l.156-171, l.409-420.
- md5 now: SF 63503687… (= SF_LOG's final), PROOF 4a7bbccc… (= SF's session-3 read), REVIEW_SF_S2 e0f0e111… (= SF's),
  s3_criteria 0fdc251a… (= SF_LOG), s3_sf.py 3015594f….

Scratch (lock-guarded runner and outputs): scratchpad `revSF3/` (run.sh, rev_s3_out.txt, rev_time.txt, rev_lock.txt).

---

## Bottom line

- **RSF2 fixes: all 14 binding items applied.** 13 are CONFIRMED. Item 5 (SF-thr-k) is CONFIRMED in a better form than the
  review asked for: it is re-based on PROOF [S22] NAH-unif′, (H-K) + (H-C⁺) + (H-ℂ) with (H-G) derived, which matches PROOF
  l.6250. Four stale-text spots remain (Part A).
- **Theorem CE-Q (band), analytic part: CONFIRMED-WITH-FIX (counted).** I re-derived Steps 0-6: the field on the band, the
  chart, readability at radius 7, the localisation radii, the large-component cost (C_3 with prefactor 512, C_2, C_1), the
  Mayer/cluster bounds and the hard-core step. The three in-place corrections (c1)-(c3) are mutually consistent.
  - **One hypothesis is missing (Q1).** Step 4 runs Theorem CE's Step 1 on the small part at rate κ_c. That needs
    H'_0 ≤ min{log 2, (32K_0)^{-1}e^{-2(κ_c-κ_0)}}. The "Statement as proven" replaced §9.1's Ĥ_0 ≤ c_0(κ_c) by
    Ĥ_0 ≤ c_0(κ_c - κ_0 - 2). That, and c_* ≤ 1/16, are each weaker than this need, by factors e^{2κ_0+4} and ≈ 400e^{κ_0+3}.
  - Three small fixes: a factor 2 (Q2), a symbol clash (Q3), and a garbled line (Q6).
- **M ∝ log(1/g_0) is NOT acceptable downstream as it stands.** It turns g-independent constants in SF-blk/RATE, FLOW F-Π
  (C_Π ∝ M⁶) and RLARGE/HIST (I_k^E)(b) into g-dependent ones (Part B-7 lists the consumers).
  - It is also unnecessary. Collars whose radius depends on the shell (radius ≈ 7 + ⌈2(j+1)log 2/(μM)⌉ cubes for a shell-j site)
    cost e^{O(κ̂ j⁴)} per site. The shell's e^{-4^jp²/16} beats that, so M can stay g-independent (Fix Q4).
- **(CE-Q^∞): the handoff to RLARGE branch (ii) is NOT coherent as written.**
  1. 𝔇 is an event in the full white noise Z. It depends on the gauge-direction components (1 - Π_U)Z, which 𝒞 kills (SF-WN),
     so it has no U-variable meaning.
  2. "|Λ|2^{n/2}e^{-a_*/(4g_0²)}" is the μ_wn-MASS of 𝔇, not its contribution: e^{ΣH} on 𝔇 is e^{O(1/g_0²)} (SF's own
     l.1042-1044).
  3. The |Λ| factor is a union bound. The deep set must be EXTRACTED per site as a polymer support, not priced globally.
  4. Branch (ii)'s hypothesis (SG^fl)_k lists "(SF)_k's cluster expansion" as an input (RLARGE l.320-322), so there is a
     circularity to rule out.

  Restated target in Part C.
- **Lemma SF-N♮: CONFIRMED (not counted).** One displayed bound is off in the 5th digit (1.0153/0.9762 = 1.0400**3** > 1.04).
  The exact values give 1.0398, so the lemma stands. src-1 is discharged.
  - CE-exp^0, SF-A2^0 and CE-Q are CONDITIONAL ⇐ (FP-loc)_0 + a background-class clause (gauge logs ≤ min{r_T/4, α_𝔫} on every
    pattern). CONFIRMED, provided that clause is recorded as a hypothesis of the class: its Lemma AX derivation is a remark (l.350,
    l.1205), not a written proof.
- **Theorem CE-col: CONFIRMED (counted).** I re-derived Steps 1-4: collar linking, the GEO-col constants 6 / 625 / 624², Cayley,
  and the re-indexing. GEO-col, CE-exp-col and RATE are CONFIRMED too (κ_c^* = 1149.92 reproduced).
  - "Decay survives iteration once κ_c ≥ 1149.9" is the RATE statement only. The NORM condition SF displays itself (l.1264-1265)
    closes for d ≥ 1 only from **κ_c ≈ 1854** (my arithmetic, Part D-4). Both close from κ_c ≥ 1854.
  - Remaining: (SF-irr) for the d < 1 polymers; the inherited activities as (H-exp) inputs (item (iv)); and a CE-col version of
    CE-Q. CE-Q is built on the 273-route Theorem CE and CE-exp, so it cannot be iterated as it stands.
- **s3: honest and reproduced.**
  - The criteria were born before the script (04:29:22 vs 04:30:22 UTC). The md5 matches.
  - My re-run under the lock is byte-identical: OVERALL PASS 13/13.
  - Evidential power is lower than "9 evidential" claims (Part E). A1's slack is ≈ 10⁴. A3 is near-automatic for this model.
    B1-B2 test Hölder's inequality. C3 equals 1 by construction. The informative criteria are A1 (weakly), C1 and C2.
- **Corrected tally (SF.md after session 3):**
  - PROVEN-HERE 26 + 1 standard (counted 9, not counted 17): SF's numbers, with CE-Q counted only with Fix Q1.
  - CONDITIONAL 5.
  - ARGUED **1** ((CE-s)), not 2. SF-A3^0's Q ≠ ∅ part is now band = CE-Q (CONDITIONAL) plus deep = (CE-Q^∞) (OPEN). It is no
    longer ARGUED, and it must not be listed twice.
  - 0 GAP, 0 WRONG. No PROOF.md tally change.

---

# PART A: the [RSF2-fix] edits (fix number = REVIEW_SF_S2 Part G)

| # | SF line | fix | verdict | note / fix |
|---|---|---|---|---|
| 1 | l.175-186, l.663-669, l.834-848, §8.1 l.962, l.969 | CEk-1: (L-hol)_k withdrawn → (L-loc)_k; the operator half of (OP-loc)_k retired | CONFIRMED | The inference "A5 (B) with growing data" is struck through (l.836-838). The (L-loc)_k statement matches REVIEW_SF_S2 B-6. |
| 2 | l.440-444, l.785-786, l.849-856 | CEk-2: inherited activities; rate non-closure; (CE-col) named | CONFIRMED | The corrected CE-exp^k list (i)-(v) is right. |
| 3 | l.656-657, l.804-807 | CE0-1: distance caveat deleted | CONFIRMED | |
| 4 | l.822-825 + §10.1 Step 0 | CE0-2/CQ-1: chart indicator; U-variable pricing outside the chart | CONFIRMED | On the band 1_D ≡ 1 (Step 0: ρ_* ≤ r_T/8 ≤ 1/64, and e^{1/64} - 1 = 0.0157 < ε^thr_N for N ≤ 400). The "beyond it" half is (CE-Q^∞), and its handoff is Part C. |
| 5 | l.266-273, l.954, l.983, §11.1 | SF-thr-k re-based | CONFIRMED (supersedes the review's wording) | PROOF l.6250: NAH-unif′ ⇐ (H-K) + (H-C⁺) + (H-ℂ), (H-G) derived by HG-ind. "Margin ≈ 8, 0.11-0.13" matches. |
| 6 | l.86-90 | BG-1 | CONFIRMED | Now (i) ⇐ NAH-unif′ hypotheses, (ii) = (H-ℂ), (iii) not supplied. |
| 7 | l.718-722, l.887-893 | GP-1/GP-2 | CONFIRMED | |
| 8 | l.702-708 | GPa-1 ((G♯-patch) stated) | CONFIRMED | Quantifiers, constants and conclusion form are all present. |
| 9 | l.682-684 | G♯-1/G♯-2 | CONFIRMED | |
| 10 | l.939-941 | src-1/src-2 | CONFIRMED | src-1 is discharged via SF-N♮ (holomorphy for a ≤ 2r_𝔫, field in D_c(y_♭), y_♭ ≤ 1/40 < y_0 = 1/20, HIST l.1565). |
| 11 | l.127-132, l.563, l.575 | stale text | CONFIRMED, **3 new stale spots** | (a) §4.3 l.582-585 and §8.2 l.985-986 still call M "g-independent" (M ≥ 3.19·10¹³). This is false after CE-Q's (M-Q); mark it, or apply Fix Q4. (b) §9.1 l.1021 defines j_max with (B1); the proof uses (B1′) (l.1126). (c) §9.1's Γ (11⁴, 13⁴), η̂ display, rate "of CE-exp^0" and the "Ĥ_0 ≤ c_0(κ_c)" condition are superseded by l.1167-1169. Add "[superseded by §10.1]" at l.1030-1039. |
| 12 | l.72-73 | SF-thr-2 (ε^J_loc kept as an assumption) | CONFIRMED | |
| 13 | l.711-713, SF_LOG "Notes for other owners" | (MIN-reg) → lane D | CONFIRMED | |
| 14 | l.791-795, s3 A | check design | CONFIRMED (with Part E's caveat on how strong the "edge test" is) | |

---

# PART B: Theorem CE-Q (band) — re-derivation

### B-1. Step 0 (field, chart): CONFIRMED
For Z ∉ 𝔇 at s ≡ 1: |A_b| ≤ g_0√NΣ_ya_{by}|Z_y| ≤ g_0√NN_02^{j_max+1}p ≤ ρ_* by (B1′). Then
||1 - e^{A_b}||_op ≤ e^{ρ_*} - 1 ≤ e^{1/64} - 1 (r_T ≤ 1/8, l.120). So the chart indicator is 1, given SF-thr's ε^thr_N.

### B-2. Step 1 (structure, readability; correction c3): CONFIRMED
- R-linking is at index distance ≤ 7, so a class R̄_α is decided by Z on R̄_α^{(7)}: every cube within 7 of the class is inspected,
  and nothing outside can link. Radius 5 (the first value) does not suffice. (c3) is necessary and right.
- U_α is *-connected (radius-7 boxes around cubes ≤ 7 apart overlap).
- |U_α| ≤ 15⁴|R̄_α| ≤ 15⁴|Q_α| (each cube of R̄_α holds a Q-site), and |U_α^+| ≤ 17⁴|Q_α|.
- d(U_α) ≤ 2(|U_α| - 1): centre-to-centre segments of touching cubes have length ≤ 2 inside the two closed cubes.
- A large X (d(X) = 0, index diameter ≤ 1) lies in R^{(2)}. It belongs to one class: two classes reached from one X are ≤ 3 apart
  in index, so they are one class.

### B-3. Step 2 (radii, field on W_α, small pieces): CONFIRMED
- Radii r_y = 2^{-(j_y+1)}e^{μδ} for far Q-sites, read pointwise in Z. That is legitimate: F_{X,S} is the radius-free Möbius sum.
- (1 + r_y)2^{j_y+1} ≤ 2e^{μδ}, from δ ≥ M + 1 and (M-Q) (μM ≥ 2(j_max + 1)log 2 ⇒ e^{μM} ≥ 4^{j_max+1}).
- Contributions to the field:
  - other-class Q-sites inside U_α^+ are at index distance ≥ 6 from W_α, give a factor e^{-5μM}, total ≤ ρ'/2;
  - good sites of U_α^+ give ≤ ρ'/2;
  - S-sites give ≤ ρ';
  - own Q-sites give σ^α_b.
  So |A_b| ≤ 2ρ' + σ^α_b ≤ ρ_*.
- Small X: field ≤ ρ'. A Q-site in S costs r^{-1} ≤ e^{-μδ/2}. With W(μ/2) ≤ w_8 under (M-W), CE-exp's Steps 1-2 give |H'(Y)| ≤
  H'_0e^{-κ_cd(Y)}.

### B-4. Step 3 (cost of a large component): CONFIRMED (constants re-derived)
- The (u + v)^k ≤ 2^{k-1}(u^k + v^k) split gives a baseline ≤ 32·#terms·T(ρ') = 2|W_α|h_0 ≤ 1250h_0|Q_α|.
- Cubic: 4·2S_T·4³r_T^{-3}g_0^{-2} = 512S_Tr_T^{-3}g_0^{-2}. With n_b, QC's 4N_0³ and t³ = 8g_0³N^{3/2}8^jp³, this gives
  C_3 = 16384S_Tn_bN_0³N^{3/2}/r_T³ ✓. (The "512 not 2048" correction is right.)
- Jacobian: (2N/9)·4N_0²·4g_0²N4^jp² gives (32/9)N²N_0²g_0²4^jp² ✓.
- Source: Σ_cσ_c ≤ n'_c·4N_0Σt, so C_1 = 64K_𝔫c_yy_bgn'_cN_0√N ✓ and the 288 entry ✓. Every pattern field is ≤ ρ_* ≤ r_𝔫/2, so
  SF-src applies.
- c(j) ≤ (3/16)4^jp² under (B2)-(B3) and 2^jp ≥ 1 ✓.
- Lemma QC (Hölder with row sums ≤ N_0 and column sums ≤ 4N_0 from the symmetry of 𝒞): CONFIRMED.

### B-5. Steps 4-5 (clusters; correction c1): CONFIRMED-WITH-FIX
- The cluster rewrite is a bijection.
  - Every Q-site lies in some U_α ⊂ Ŷ_α, so sites outside the clusters are good.
  - K-members can contain Q-sites (through S of small X), but then they overlap Ŷ_α: same cluster. The K-bound does not depend
    on j, and each Q-site's shell weight is charged once, to its G-member.
  - Disjoint 𝒵 carry independent Z.
- (c1) κ̂ := κ_1 - κ_0 makes the K-members' bound e^{-κ_0d}, and (g5') applies ✓. Tree bound (g2) ✓. G-member S-sum W̃ ≤ w_8
  (κ̂ < κ') ✓. Γ = exp(546·15⁴κ̂ + 17⁴w_8) ✓. Shell masses 2^{n/2}e^{-4^jp²/4}, with 1/μ_1(good) ≤ 2 ✓.
- **Fix Q2.** z(𝒵) is the sum of the pure part (Q ∩ 𝒵 = ∅) and the mixed part, not one or the other. The bound is
  |z(𝒵)| ≤ C_KH'_0e^{-κ_1d} + 16eM⁴η̂e^{-(κ̂-2)d} ≤ 2C_KĤ_0e^{-(κ_c-2κ_0-4)d}. Replace Ĥ_0 by 2Ĥ_0 in Step 6 and in the statement
  (harmless).
- **Fix Q5 (cosmetic).** Σ_{j≥0}e^{-4^jp²/16} ≤ 2e^{-p²/16} fails at p = 1 (sum ≈ 2.24) but holds for p ≥ 1.3. (B3)'s "p ≥ 1" should
  read p ≥ 2. Irrelevant in practice: p_0 ≈ 4·10⁵ from η̂M⁴ ≤ 1/32 (546·15⁴κ̂ ≈ 8.5·10⁹ at κ_c = 4κ_0 + 6).

### B-6. Step 6 (hard-core step; correction c2): CONFIRMED-WITH-FIX (Fix Q1, binding)
- Parametrising Steps 3-4 with κ := κ_c - κ_0 - 2 (so κ_1(κ) = κ_c - 2κ_0 - 4) is valid. Theorem CE's Steps 3-4 use the activities
  only through |z| ≤ r_Y on the closed polydisc, the hard-core polynomial over disjoint polymers, and the third entry of c_0.
- The output rate κ - 3κ_0 - 3 = κ_c - 4κ_0 - 5 is right.
- **Fix Q1 (missing hypothesis).** Step 4's Mayer expansion of the small part is Theorem CE's Step 1 at rate κ_c. It needs
  H'_0 ≤ log 2 and H'_0 ≤ (32K_0)^{-1}e^{-2(κ_c-κ_0)}. The statement as proven (l.1167-1168) lists Ĥ_0 ≤ c_0(κ_c - κ_0 - 2), whose
  second entry is (32K_0)^{-1}e^{-2(κ_c-2κ_0-2)}: weaker by e^{2κ_0+4}. Its third entry is weaker too (ratio
  6400e^{4κ_0+7}/8). c_* ≤ 1/16 gives H'_0 ≤ e^{-2(κ_c-2κ_0-2)}/(512eK_0²): weaker by ≈ 400e^{κ_0+3}.
  - **Add "H'_0 ≤ c_0(κ_c)"** (as §9.1 had) to the statement.
  - It is met for g_0 small (H'_0 = O(g_0M⁴p³)), so nothing else changes.
- **Fix Q3.** "C_1" denotes both the band constant (B3) and Theorem CE's prefactor 2κ_0B in |𝓗_𝒵| ≤ C_1Ĥ_0…. Rename the band
  constants (e.g. C_1^Q, C_2^Q, C_3^Q).
- **Fix Q6.** l.1176 "some field |A_b| ≥ ... can exceed ρ_*" is garbled. It should read "the field |A_b| at real s may exceed
  ρ_*".
- **Disclosure.** The proof was rewritten in place at 04:37-04:38, after s3 ran (04:33). That is disclosed (l.1109-1112,
  SF_LOG). None of the s3 criteria tests a CE-Q constant other than D4's shell sum, so no criterion was affected. I accept it as
  disclosed.

### B-7. M ∝ log(1/g_0): consumers, and a fix that removes it
Where the growth comes from:
- (M-Q) μM ≥ 2(j_max + 1)log 2 with 2^{j_max} ≍ 1/(g_0p) forces M ≳ 2log_2(1/(g_0p))·log 2/m_1 ≈ 2.9·10¹⁰·log_2(1/(g_0p)).
- (M-W) alone needs M ≳ 6.4·10¹³. So (M-Q) binds only for g_0 ≲ 2^{-2200}. Asymptotically it binds, and the UV statement is
  asymptotic.

Consumers that assumed a g-independent M:
1. **SF-blk / Proposition RATE** (SF l.224-226, l.1257-1265). The level-(k+1) cubes have "side M in level-(k+1) units", the
   same M at every level. With M_k = M(g_k) the cube size changes between levels. A re-cubing step is then needed, and RATE's
   κ_c^* rises.
2. **FLOW Lemma F-Π / Claim l.409-420.** C_Π = 64M⁶α^{-2}Σ…, so C_ρ = C_ΠE_2 + 1 ∝ M⁶. The F-flow bracket
   β_± = β_0' ± C_ργ²/log L and the condition C_ργ² ≤ ½β_0'log L become g-dependent. γ²log⁶(1/γ) → 0, so they survive, but
   every FLOW constant must be restated.
3. **RLARGE §4.1 (I_k^E)(b)** (l.389: "per-cube g-independent sup bound E_0 on a g-independent domain") and **HIST (I_k^E)'**:
   per-cube bounds of M-cubes scale like M⁴ or M³.
4. **RLARGE §4.2 rows 6, 3, l.139.** These are rates "in M-units" and per-cube large-field weights (Ce^{-a/g²})^{#cubes}; the
   e^{B_0} per boundary cube grows like M³. They are still dominated by e^{-a/g²}, but the constants become g-dependent.
5. **SF's own** g_CE (CE-exp^0, l.819: "O(g_0) at fixed (p, M)") and p_0 (l.1171: p_0 depends on log M, hence on
   log log(1/g_0)). So "fixed p" is not literally g-independent either.
6. **PROOF N6** (M ≳ 457/m_*) is only a lower bound and is unaffected. The torus constraint M ≤ T_k/3 already excludes the last
   ≈ 28 levels (L = 3); that is pre-existing (session 2) and is made slightly worse.

**Fix Q4 (recommended; removes the growth).** Use shell-dependent collars. Give a shell-j Q-site the cube radius
r_j := 7 + ⌈2(j + 1)log 2/(μM)⌉. Call X large if it lies within r_{j_y} + 1 of some Q-site y, and link classes at distance
r_{j_y} + r_{j_{y'}}.
- Then the far-site Cauchy cost 2^{j+1}e^{-μδ} ≤ e^{-μδ/2} holds by construction, and (M-Q) is no longer needed.
- Readability holds with U_α := the union of the radius-r_{j_y} boxes.
- The polymer cost per shell-j site is e^{O(κ̂(2r_j + 1)⁴)} = e^{O(κ̂ j⁴)} (for M ≥ M_W, (r_j - 7) ≤ (j + 1)/1100). The shell's
  e^{-(1/16)4^jp²} beats it, uniformly in j, once p ≥ p_0, with p_0 independent of g_0 and M.
- 2^{j_max} ≍ 1/(g_0p) then enters only through the band edge. M stays g-independent and the downstream consumers are
  untouched.
- The proof is Steps 1-6 with 15⁴, 17⁴ replaced by (2r_j + 1)⁴, (2r_j + 3)⁴ per site. That is session-scale work.

---

# PART C: (CE-Q^∞) and the RLARGE branch (ii) handoff

**Verdict: OPEN, and the handoff is NOT coherent as stated. Restate it.**
1. **𝔇 is not a U-event.** SF-WN (l.386-389): 𝒞 = Π_UÕ^{-1/2}Π_U kills (1 - Π_U)Z. Whether |Z_y| > 2^{j_max+1}p depends on those
   gauge-direction components, which never reach U. "Price 𝔇 in U-variables" therefore has no meaning.
   - **Fix C-1.** Integrate (1 - Π_U)Z out first. Π_U is block-diagonal (§0 l.26), so this is block-local, and the integrand does
     not depend on it. Then define the shells on Π_UZ, per block. The measure on Π_UZ is a product over blocks, so CE cubes of
     side ≥ 1 block keep Setting CE.
2. **Mass is not contribution.** μ_wn(𝔇) ≤ |Λ|2^{n/2}e^{-a_*/(4g_0²)} is right (the a_* algebra is re-derived: the floor of the
   largest j costs a factor 2, and (B1′) with ρ' ≤ ρ_*/4 gives the second entry).
   - But on 𝔇, e^{ΣH} is the ratio of the Haar integrand to the Gaussian. In the Π_UZ directions it is as large as
     e^{+|Π Z|²/2}·(Haar density), i.e. e^{O(1/g_0²)}. So the deep contribution is not bounded by mass × sup.
   - §11.1 ("weight ≤ …") and §11.2 ("weight e^{-O(1/g_0²)} per site") must say **μ_wn-mass**. The contribution must be bounded
     in Haar variables: |integrand| ≤ the Haar density times the probability of a U-defect.
3. **The |Λ| factor needs extraction, not pricing.** A union bound over sites is not uniform in the volume, and in the
   thermodynamic limit it is not small.
   - **Fix C-3.** Sum over the deep set D ⊂ Λ (sites with j > j_max). Each deep site carries its own e^{-a_*/(4g_0²)}-type
     weight. Run the band expansion (CE-Q, with collars around D as in Fix Q4) on the complement, with D's neighbourhood as
     polymer support.
   - This is exactly the form RLARGE's branch-(ii) bound has: it is multiplicative, (C_fle^{-a_fl/g²})^{|A∖B_V|} (l.313).
4. **A translation lemma is missing.** Branch (ii) prices PLAQUETTE events ||1 - U_p|| ≥ τ (PLD-desc). A deep Π_UZ at a block
   gives, via Π_UZ = Õ^{1/2}A (Õ^{1/2} exponentially local), an exponentially localised LARGE SLICE FLUCTUATION A, not a large
   plaquette.
   - The missing step is "large slice fluctuation near x ⇒ plaquette ≥ τ or kernel mismatch ≥ ε near x". That is a local slice
     coercivity, the same object SF names at l.1177-1178.
   - **This, not "U-variable pricing", is the real content of (CE-Q^∞).** Name it, e.g. **(SL-coer)**.
5. **Circularity check.** RLARGE l.319-322 lists "(SF)_k's cluster expansion (OPEN, node A)" among (SG^fl)_k's inputs. If
   (CE-Q^∞) is sent to branch (ii), it must be shown that (SG^fl)_0 consumes only the band part (CE-Q), not (CE-Q^∞). Otherwise
   the handoff is circular. Record this in the owner note to RLARGE.

**Restated (CE-Q^∞) [OPEN].** After (1 - Π_U)Z is integrated out:
- the stage-0 integral restricted to configurations with a non-empty deep set D (in Π_UZ) is
  Σ_{D≠∅}(polymer activities supported on D's r_*-neighbourhood) × (the band expansion off it);
- each deep site carries a factor ≤ C e^{-a'/g_0²} in Haar variables;
- the (SL-coer) step converts a deep site into a priced U-defect.

---

# PART D: Lemma SF-N♮, Theorem CE-col and its corollaries

### D-1. Lemma SF-N♮ (l.1047-1054, proof l.1186-1206): CONFIRMED (not counted)
- (1) The spread is gauge invariant under real gauges; |Ad_hA| = |A|.
- (2) The loop factorisation is right. I re-checked both orientations: the ε = -1 factor gives e^{-Ad_{P_i}A}P_i. The text's index
  shift (P_i vs P_{i-1} for ε = +1) is a typo.
- (3) |E - 1| ≤ e^{ℓa} - 1 (submultiplicative, HS or operator norm).
- (4) ||D log(1 + W)|| ≤ 1/(1 - |W|). I re-derived the numbers:
  - ℓa ≤ 4y_♭/6.6 ≤ 0.015152, |W_0| ≤ 0.008368, w ≤ 0.023635;
  - with ℓa e^{ℓa} as the bound on |E - 1|: e^{0.015152}/0.976365 = 1.0398, so |E - 1|/(1 - w) ≤ 1.0398ℓa ≤ 1.04ℓa ✓.
  - **But the displayed chain "ℓa·e^{0.0152}/0.9762 ≤ 1.04ℓa" is false as printed** (1.04003). Fix SN-1: use the unrounded values
    or write 1.05 (then 2.1p_La ≤ c_ya still).
- (5) θ ≤ ½/max(1, C_N) follows from the choice of y_♭.
- y_bg ≤ 2.08p_Lα_𝔫 ≤ c_yr_𝔫, and y ≤ y_♭ ≤ 1/40 < 1/20 = HIST's y_0. ✓
- **Consequences:**
  - CE-exp^0, SF-A2^0 and CE-Q are CONDITIONAL ⇐ (FP-loc)_0 + the background clause. CONFIRMED.
  - **Fix SN-2:** record "gauge logs ≤ min{r_T/4, α_𝔫} on every pattern" as an explicit hypothesis of the background class. Its
    derivation from BR1 + Lemma AX (10p_Lℓε' ≤ α_𝔫, i.e. ε' ≲ 10⁻⁷, far above N5's threshold) is a bracketed remark (l.350,
    l.1205), not a written step.
  - The "(FP-loc)_0 alone" wording should carry the clause each time (§11.1 does, §11.2 does not).

### D-2. Lemma GEO-col (l.1061-1064, l.1210-1221): CONFIRMED (not counted)
- (a) Via (g1'): N(τ) ≤ 16 + 16ℓ for any connected union of segments.
- (b) Three segments of length ≤ 2 inside the convex cubes a, Q, b' join τ_i and τ_j, and stay inside ∪(∪c_i)^+.
- (c) The 2-connectivity graph has degree 5⁴ - 1 = 624, and a closed walk of length 2(m - 1) encodes the set. a' = log(2·624²) gives
  Σ ≤ 2e^{-a'} = 1/624², and κ̃_0 = 16a' = 217.047 turns d^+ ≥ |c|/16 - 1 into K̃_0 = e^{κ̃_0}/624².
- (d) 5⁴.
- (e) The polymer Y' is built from the cubes of c^+ that τ meets. Fine.

### D-3. Theorem CE-col (l.1065-1070, l.1223-1245): CONFIRMED (counted)
- Step 1 (linked-component Mayer):
  - (∪X)^+ = ∪X^+, so different components have disjoint supports, and the decomposition is unique;
  - the cores are 2-connected;
  - Π e^{-κd(X_i)} ≤ e^{-κ'(d^+(c)-6(n-1))}Π e^{-κ_0d(X_i)} (GEO-col (b), d^+(X) ≤ d(X));
  - with (g5') over X ⊂ c, |K(c)| ≤ e^{-κ'd^+}2H_0K_0|c|e^u, and u ≤ |c|/16 ≤ 1 + d^+ (second entry of c̃_0, GEO-col (a)).
  So C_K = 32eK_0 and κ_1 = κ - κ_0 - 2 ✓.
- Step 2: independence on disjoint c^+ ✓.
- Step 3: the exponential formula holds for any reflexive symmetric incompatibility relation (here c^+ ∩ c'^+ ≠ ∅), and Lemma TG
  is graph-generic ✓.
- Step 4:
  - relaxing to c_j ∩ c_{p(j)}^{(2)} ≠ ∅ (GEO-col (d)), |c|^m ≤ m!e^{|c|} with |c| ≤ κ̃_0(1 + d^+), and GEO-col (c) over 2-connected
    cores give per-vertex 625e^{κ̃_0}K̃_0 and root |Y|e^{κ̃_0}K̃_0;
  - Cayley ≤ (n - 1)!4^{n-1}, so the term is ≤ κ̃_0B̃H_0(4B̃H_0e^{6κ_3})^{n-1}e^{-(κ_3-1)d^+(Y)} (a spare 1/625 is dropped);
  - the third entry e^{-6κ_3}/(8B̃) matches c̃_0;
  - the rate is κ - κ_0 - 2κ̃_0 - 3 ✓.
- Re-indexing: Y ⊂ Y' ⊂ Y^+ with d(Y') ≤ d^+(Y) + 1, at most 2^{|Y'|} preimages, and the output reads Φ on Y'^+.
  **The output is in the input locality class (functions of Φ on X^+)**, so the theorem composes in locality. ✓
- The claim "the collar enters only the linking" is accurate: no d(X^+) appears. The e^{272κ'} and 1/273 are gone.

### D-4. Corollary CE-exp-col and Proposition RATE: CONFIRMED; the norm half is computed here
- CE-exp-col:
  - the collar-free hull: d(Y_0) ≤ d(X) + Σ(2n_y + 3), and F_{X,S} reads ∪X^+ ∪ S ⊂ ∪Y_0^+;
  - W_3 with e^{3κ'}, sufficient μM ≥ 5κ' + 4 log M + 8;
  - input requirement κ ≥ κ_c + 16 log 2 + 1296W_3 (≈ κ_c + 46.4).
- RATE: 2κ_c ≥ 6κ_0 + 6κ̃_0 + 10 + 64 log 2 + 1296w_8 = 2299.84 ⇔ κ_c ≥ 1149.92. Reproduced, and s3 D2 agrees.
- **The norm half (not done in SF).** SF's displayed condition (l.1264-1265) for d ≥ 1 is
  C̃_1H''_0·2^{16}e^{r}·16L⁴K_0e^{-(κ(L-1)-κ_0L-1)} ≤ (next input norm), with κ = r - 16 log 2 and the input normalisation
  H''_0 = 2^{16}e^{1296W_3}h_0. I evaluated it with log C̃_1 = 580.75 (log B̃ = 574.68). The log of the ratio is +703.6 at
  κ_c = 1149.92, and it reaches ≤ 0 first at **κ_c ≈ 1854** (L = 3).
  - So both rate and norm (d ≥ 1) reproduce from κ_c ≳ 1.85·10³ (reviewer arithmetic: ARGUED, not a check).
  - Fix RT-1: state RATE as "rate closes from 1149.9; the d ≥ 1 norm closes from ≈ 1854; d < 1 = (SF-irr)". "Decay survives
    iteration at L = 3 once κ_c ≥ 1149.9" (§9.3, l.1261) must say "rate".
- What remains for (CE-col) to be usable at k ≥ 1:
  - (SF-irr), the d < 1 extraction, unchanged;
  - (iv), the blocked inherited activities as (H-exp) inputs. Strictly local activities need only the UNIFORM polydisc
    (CE-exp-𝒞's strictly-local branch). So this reduces to (I_k^E)(b)'s analytic per-cube bound, the same type as (L-loc)_k;
  - **CE-Q itself is built on Theorem CE and CE-exp (the 273 route).** A CE-col version of CE-Q (one more Mayer layer, at rate
    loss κ_0 + 2) must be written before the band can be iterated. Its RATE threshold rises by ≈ 3(κ_0 + 2)/2 ≈ 230.

---

# PART E: s3 (MANDATORY NUMERIC LOCK) and check design

- **Provenance.**
  - s3_criteria.md: born 04:29:22 UTC, mod = birth, md5 0fdc251a… = SF_LOG.
  - s3_sf.py: born 04:30:22 UTC, after the criteria.
  - Output and timing: born 04:33:31, modified 04:33:35 UTC.
  - No post-run edit.
- **Re-run (this review).**
  - `until mkdir …/locks/numeric 2>/dev/null; do sleep 20; done`. The lock was held by another process at first and acquired at
    04:51:21 UTC. Load 3.31 (< 8, re-checked inside the lock).
  - nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`; no trap.
  - Exactly one `rmdir`, released 04:51:25 UTC. 3.56 s, peak RSS 81 MB, exit 0. No process left running.
  - **Output byte-identical to checks/s3_out.txt: OVERALL PASS 13/13.** Record: scratchpad revSF3/rev_lock.txt, rev_time.txt.
- **Code review (line by line).** No bug. A's B_S is a valid sup on the refined set. B's Ablk (sum over the 4 links) is the worst
  case of QC's operator-norm block. C's aligned construction gives E = e^{ℓaŴ} commuting with Λ (I checked both orientations).
- **The thin 1.08·10⁻⁴ vs 10⁻⁴ margin.** A2 is a non-vacuity floor fixed before the script existed, so the pass is honest. What
  it reveals is that A1 has slack ≈ 10⁴: A1 would catch only an error by a factor ≳ 10⁴. "Edge test" overstates it. The domain
  edge is approached in the worst-case alignment, but g at the real points is far from its pole.
- **Near-automatic or construction-level criteria** (informational; none is false):
  - A3 holds whenever Σ_{y∈F∖S}|b_y|(1 + r_y) ≥ 10⁻³, which is automatic since ρ_S saturates S alone.
  - B1/B2 test Hölder's inequality, a theorem.
  - C3's ratio is exactly 1 by the commuting construction. It shows sharpness, not correctness.
  - D1-D4 are ARITHMETIC, as labelled.
- **Informative:** A1 (weak), C1 (worst 0.909: c_y has 10% slack against ℓ = 2p_L), C2. A future CE-Q check should test a CE-Q
  CONSTANT: e.g. Step 3's c(j) ≤ (3/16)4^jp² on a toy kernel, or Fix Q1's Mayer condition.

---

# PART F: corrected tally and binding fixes

**Tally of SF.md after session 3 (all items reviewed here):**
- PROVEN-HERE 26 + 1 standard (SF's count stands):
  - counted 9, all CONFIRMED: SF-J, SF-T0, SF-DC, CE^+, SF-blk, LOC-s, CE-exp, **CE-Q (analytic part; CONFIRMED-WITH-FIX Q1,
    Q2)**, **CE-col (CONFIRMED)**;
  - not counted 17: the 13 of session 2, plus LOC-s′, QC, SF-N♮ (Fix SN-1 cosmetic) and GEO-col, all CONFIRMED. CE-exp-col and
    RATE are CONFIRMED (corollary and arithmetic, not added).
- CONDITIONAL 5:
  - SF-thr-k: ⇐ (H-K) + (H-C⁺) + (H-ℂ).
  - SF-A2^0, CE-exp^0, CE-Q as a statement on the integral: ⇐ (FP-loc)_0 + the background clause (Fix SN-2).
  - CE-exp^k.
- ARGUED **1** ((CE-s)). SF-A3^0's Q ≠ ∅ part is withdrawn as ARGUED: it is now CE-Q (band) + (CE-Q^∞) (deep).
- OPEN names:
  - (FP-loc)_k, (N5-reg)_k, (L-loc)_k [B-NA wall];
  - **(CE-Q^∞) restated (Part C), with (SL-coer) named**;
  - **CE-Q-col** (a CE-col version of CE-Q, needed for k ≥ 1);
  - (CE-col)'s item (iv) (inherited activities as inputs);
  - (SF-irr) and the A4 items;
  - (a5-G♯)/(G♯-patch), (R♯) at ψ^r [B-NA];
  - lane D: (MIN-reg), (a5-U), (a3-q).
- 0 GAP, 0 WRONG. **No change to PROOF.md's tally.** No RLARGE §4.2 row is discharged.

**Binding fixes (next SF session):**
1. **Q1:** add H'_0 ≤ c_0(κ_c) (log 2 and (32K_0)^{-1}e^{-2(κ_c-κ_0)}) to Theorem CE-Q's statement (l.1167-1168).
2. **Q2:** |z(𝒵)| ≤ 2C_KĤ_0…: put the factor 2 into Ĥ_0 (l.1164-1166).
3. **Q3:** rename the band constants C_1, C_2, C_3 so they do not clash with Theorem CE's C_1.
4. **Q4 (strongly recommended):** shell-dependent collars r_j, so that (M-Q) is dropped and M stays g-independent. If this is not
   done, mark every consumer in B-7 (SF-blk/RATE, FLOW F-Π C_Π ∝ M⁶, RLARGE/HIST (I_k^E)(b), SF's g_CE and p_0) as
   g-dependent, and correct §4.3 l.582-585 and §8.2 l.985-986.
5. **Q5/Q6:** p ≥ 2 in (B3); repair the garbled l.1176.
6. **C-1-C-5:** restate (CE-Q^∞) as in Part C: integrate out (1 - Π_U)Z first; "μ_wn-mass", not "weight", in §10.1, §11.1, §11.2;
   per-site extraction of the deep set; name (SL-coer); add the circularity note for RLARGE's owner ((SG^fl)_0 must use the band
   part only).
7. **SN-1:** fix the 1.04 display (l.1197). **SN-2:** carry the background-class clause as an explicit hypothesis wherever
   "(FP-loc)_0 alone" appears (§11.2 l.1295).
8. **RT-1:** RATE and §9.3, §11.1 say "rate". Add the d ≥ 1 norm closure threshold (≈ 1854 by this review's arithmetic; re-derive
   it).
9. **Stale text:** §9.1 l.1021 (B1) → (B1′); mark §9.1 l.1030-1039's constants "[superseded by §10.1]".
10. **Tally:** ARGUED 1, not 2. Do not list SF-A3^0's deep part as ARGUED.
11. **Check design:** the next check must test a CE-Q constant (Part E). Label A3, B1-B2 and C3 as low-power in the outcome text.

---

# PART G: strategic verdict

**Verdict: CE-Q (band) and CE-col are real gains. The stage-0 band is now one convergent gas, and the cluster expansion
composes in rate (and, from κ_c ≈ 1.85·10³, in the d ≥ 1 norm). The open frontier has moved from "how to expand" to two items:
(CE-Q^∞), whose real content is a local slice-coercivity statement, and (SF-irr).**

Order of attack:
1. **Fix Q4 + Q1 first.** These are session-scale, inside lane F, and they protect every downstream constant. A g-dependent M
   would ripple into FLOW and RLARGE for no reason.
2. **CE-Q-col.** Re-run CE-Q on Theorem CE-col and CE-exp-col (the band with collar linking). Without it the band cannot be
   iterated, and (CE-col)'s gain is unusable at k ≥ 1.
3. **(CE-Q^∞) as restated.** The (1 - Π_U)Z integration and the per-site extraction are bookkeeping. **(SL-coer)** is the hard
   core: large slice fluctuation ⇒ local plaquette or kernel defect. It is the stage-0 instance of the local coercivity that
   RLARGE branch (iii) (CLS-sf, (AE)) also needs. Coordinate with the CLS-sf/(AE) owner rather than duplicating it. It must not
   be handed to branch (ii) as "pricing" until the circularity check passes.
4. **(SF-irr)** (d < 1 extraction) stays the A4 wall. The norm closure computed here (κ_c ≳ 1854) shows that the d ≥ 1 part is
   not the obstruction.
