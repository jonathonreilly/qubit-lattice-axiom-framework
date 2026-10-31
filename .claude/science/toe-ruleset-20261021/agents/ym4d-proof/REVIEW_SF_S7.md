# REVIEW_SF_S7: hostile review of lane F session 7 ([RSF6-fix] edits; §21-§23: Lemma HO, Propositions CI-0, CI-bg, Corollary CI-BR1, Lemma CHEB-f, the N5-sf0 re-evaluation, DX′-1 and the derived rows; check s7; SF_LOG's proposed PROOF.md edits)

Reviewer: an independent agent that wrote none of SF.md. I edited no file except this one. No commits, PRs or pushes.

Inputs (read 2026-10-28 ≈08:30-09:05 UTC):
- SF.md l.2040-2110, 2175-2200, 2383-2388, 2450-2560, 2589-2636 (the [RSF6-fix] spots), §21-§23 (l.2645-2879) in full.
- SF_LOG session-7 block (l.313-393). REVIEW_SF_S6.md in full.
- checks/s7_criteria.md in full; s7_sf.py (714 lines) line by line; s7_out.txt; s7_time.txt.
- PROOF.md (read-only, md5 4a7bbccc…): Settings N5-0/N5-bg, N5-cov, AX, N5-an (l.5149-5330); N5-sf0 + N5-w0 (l.5415-5530);
  RW-ℓ², 𝔠_∞, U0, FPq, N5-an♭, BR1 (l.5555-5704); CURV1 (l.5990-6052); grep of every 𝔠_∞ use.
- checks/c36_nah1.py part C (the operator SF reuses); REVIEW_S20 on c36 C.
- SF's scratch sf7/ (file times and run records only).
- md5 now: SF ceec42df… (= SF_LOG's final); s7_sf.py 05c1d69e…, s7_criteria 06238199…, s7_out c97d39df… (all = SF_LOG).

Scratch (scratchpad `revSF7/`): rev7_cert.py and rev7_arith.py (my own code), run.sh, rev_lock.txt, rev7_cert_out.txt,
rev7_cert_time.txt, rev7_arith_out.txt, rev7_arith_time.txt.

---

## Bottom line

- **RSF6 fixes: all binding fixes (TH-2, FP-1, FP-2, GB-1, tally) are applied in place and correct.** The non-binding notes are
  applied too. One leftover: the §20.1 (DX-loc) row (l.2605) still says "covariance decay in hand" (E-4 was fixed only in §19.3).
  The TH-2 table reproduces (5.949·10⁻⁷⁷/C_♭, n_* 2.70·10¹⁵⁴, 80.9 levels, a_bad 1.84·10⁻¹⁵⁹).
- **Computer-assisted certificate (HO, CI-0): CONFIRMED.** I reproduced it independently. My version differs from SF's in four
  ways:
  - my own group action, with different orbit representatives and no Stab-symmetrisation;
  - my own Bloch inverse;
  - a residual computed **without BLAS** (sequential exact-product accumulation);
  - weights from mpmath upper bounds, with the row sums and the final formulas in Fractions.
  **Every certified number agrees with SF's to all printed digits**: k_0 = 132.842054, e_0 = 0.4381436, and the whole m-grid.
  So **𝔠_0 ≤ 236.434155, λ_min(Õ_0) ≥ 4.229507·10⁻³**, and the rate is 0.02 per fine unit (N_{0.02} ≤ 715.9).
- **CI-bg: CONFIRMED** for the class 𝔑(α_*) as PROOF currently defines it, real and complex, at κ_0 = 1: **𝔠_∞^♯ = 236.4346**,
  λ_min ≥ 4.22950·10⁻³. The perturbation step is rigorous: N5-an's entrywise bound is uniform in the column gauge (the GB-1
  point), the region needed is 10 ≤ R_* + 3 blocks, R_g is real orthogonal, and C_Δα_* ≤ γ_0/2 by definition.
  **Two defects:**
  - **WRONG (minor, KW-1):** "𝔠_∞ stays finite for |κ - 1| ≤ 2.6·10⁻²". The exact window is **|κ_0 - 1| < 2.5858·10⁻²**; at
    0.026 the Neumann quantity is 1.0031. Also, 236.43 holds only at κ_0 = 1. In the window 𝔠 = k′_0 + δ + k_0e_κ/(1 - e_κ).
  - **BINDING (CS-1):** CI-bg's δ is tied to the CURRENT α_*. The proposed N5-sf0 rerun (§22.6) enlarges 𝔑(α_*):
    C_Δα_* = 1.057·10⁻³ in place of 3.97·10⁻⁹. On that class **𝔠_∞^♯ = 315.19 and λ_min ≥ 3.1727·10⁻³** (mine). SF's C4 line and
    §22.6 combine the new ε_* with 𝔠 = 236.43, which is inconsistent. The corrected values are in Part C.
- **CHEB-f: CONFIRMED** (statement, ellipse lemma, and the counting 12D + 8, ×324). Reproduced: μ = 5.3690·10⁻⁴ per fine unit,
  N_μ(|Õ^{1/2}|) ≤ 5.718·10¹⁶.
- **Thresholds (priority 3): CONFIRMED as arithmetic, with one correction.** At τ^A: ε_1 ≤ min{1.2687·10⁻³⁹, 1.06·10⁻²⁹/C_Δ,
  4.26·10⁻⁷/C_♭, …}. The break-evens are C_Δ ≈ 8.4·10⁹ and C_♭ ≈ 3.4·10³². DX′: g_0²C_Ω ≲ 2.456·10⁻¹⁵².
  **TB-1 (binding, small):** the binding entry now uses ε_bg^{(TH-bg)}'s **a_p entry only**. The full (TH-bg) min{a_p, a_c}
  (a_c ≈ a_p/2 at κ_s = 1) and the n_K term lower it by a factor 0.7056, so **ε_1 ≲ 8.95·10⁻⁴⁰** (a_c is approximate in KF;
  state it as ≤).
- **N5-sf0 rerun (priority 4): VALID as a substitution**, at κ_0 = 1 only. γ_0 enters N5-sf0 only as the compression lower bound
  and through the choices it induces; CI-0 gives that bound on every torus.
  - My own chain reproduces m_4 = 2.5715·10⁻⁵, R_* = 3.2331·10⁶, T_0 = 1.2932·10⁷, ε_* = 2.4764·10⁻¹³/C_Δ (×1.42·10¹¹). The
    control reproduces 1.7451·10⁻²⁴.
  - It must carry CS-1. With CS-1: C_bg = 2.186·10⁵; at τ^A ε_1 ≤ min{9.52·10⁻⁴⁰ (×0.7056 by TB-1 → 6.7·10⁻⁴⁰), 1.13·10⁻¹⁸/C_Δ,
    2.40·10⁻⁷/C_♭, …}. The C_Δ break-even becomes 1.2·10²¹.
- **Process (priority 5):**
  - The memory overruns are real: s7 had a 1.18 GB footprint, ex2 2.24 GB (ex2 at 39% free).
  - **My own run also reached a 1.18 GB footprint** (RSS 760 MB), disclosed below. RSS is not the right budget measure.
  - The out-of-lock calcs were negligible in load but are rule breaks.
  - **SF_LOG l.393's "08:29" entry post-dates the file's own mtime (08:26:52 UTC):** a provenance error.
- **Corrected tally: PROVEN-HERE 58 + 1 standard** (SF's count stands) / CONDITIONAL 8 / ARGUED 4. 1 WRONG sentence (KW-1, three
  places), 1 binding consistency fix (CS-1), 1 binding threshold fix (TB-1), provenance fix PV-1.

---

# PART A: [RSF6-fix] edits (REVIEW_SF_S6 F-3)

| # | SF line | verdict | note |
|---|---|---|---|
| TH-2 | l.2191-2198 ((TH-ch″)), l.2496-2502, l.2574-2588, l.2631 | CONFIRMED | ε_br quoted correctly from PROOF l.5663. 1/(24·(2·10³⁷)²)/(1.011√3) = 5.949·10⁻⁷⁷ (mine). Scalings reproduced: n_* 2.70·10¹⁵⁴, RS 2.0·10³¹⁷-1.5·10³²¹, a_bad 1.84·10⁻¹⁵⁹, 80.9 levels |
| FP-1 | l.2511-2520 | CONFIRMED | wrong statement struck; two-step statement written. "Proof (of the struck statement, kept for the record)" is acceptable |
| FP-2 | l.2385-2386, 2521-2523, 2603, 2605 | CONFIRMED | |
| GB-1 | l.2454-2459 | CONFIRMED | the Y-uniform entry bound b(X, Z) and the two-sup factorisation are exactly right |
| tally | l.2611-2614 | CONFIRMED | 53 + 1, CD a citation |
| A-1/A-2, GB-2, E-3, E-4, "44 orders" | l.2090-2093, 2478-2482, 2546-2549, 2621 | CONFIRMED | **Leftover (non-binding):** the §20.1 (DX-loc) row l.2605 still reads "(DX-loc-3) covariance decay in hand"; apply E-4 there too |

---

# PART B: AUDIT of the computer-assisted certificate (priority 2)

### B-1. What must be rigorous
K̃ is a fixed dyadic array, so its accuracy affects only e_m, never validity. Validity needs four things:
- (a) exact covariance of Õ_0 and 1 - Π under a group that maps every column type to a canonical one;
- (b) upper bounds on the type masses of |K̃|, |K̃ - (1 - Π)| and |E| = |Õ_0K̃ - 1| over the full support of E;
- (c) row sums assembled correctly from column masses;
- (d) the Neumann / Schur steps.

### B-2. s7_sf.py, line by line
- **Operator** (l.81-197). It is c36 C's construction verbatim: same templates w, Q, the P_res projector, and
  Õ = Π(d^*d + κQ^TQ + dP_resd^*)Π + (1 - Π). That construction was validated in REVIEW_S20 against c35's independent float
  matvecs. A1 reproduces N_0 = 10462237/410670 exactly.
- **HO** (l.205-243, A2). The map g_link and the three generators are correct. Generators suffice because the link map is a
  group action. A2n is a real control.
- **E support.** K̃ lies in blocks [-6, 5]⁴ (the midpoint rule |6Z + MID - 2|_∞ ≤ 33 fits the n = 12 box exactly). E lies in
  [-7, 6]⁴, which the slab loop covers (l.430-462).
- **Enclosure** (l.531-535).
  - γ_{81·324+1} covers any classical summation order of the BLAS products.
  - The +2u covers the correctly rounded conversion of A.
  - The aggregated radius Σ_Z e^{md}·rad ≤ e^{mD_A}Σ_ja_ijv_j^m is valid by the triangle inequality and d(row, col) ≤ D_A on the
    support of A.
  - The identity entry is covered.
- **Row assembly** (l.551-556). Σ_ZX((Z, i), (0, j)) = S_c[π_h(i)] by translation plus covariance; d_mid is invariant. Correct.
- **Canonicalisation** (l.382-405). No link is self-reversed (that would need x_μ = h - ½), so "zeroed 0" is structural and the
  Stab-invariant copy is well defined.
  - **Note (non-binding):** Stab-invariance is not needed at all. Fixing one h_j per type defines K̃ unambiguously, and only Õ_0's
    covariance is used. My run proves this (B-3).
- **Formulas** (l.591-608). CI-0/CI-bg are exactly as stated. The weighted bound uses e^{m(r_1+1)}δ. C1's rate conversion uses e^m
  (|d_mid - d_base| ≤ 1).
- **k′_m = k_m to all digits is NOT a bug.** 1 - Π = ww^T/||w||² is rank one per block, so a row type with w_i = 0 has a zero
  (1 - Π) row, and the maximum sits at such a type. My float N_0(|G_12 - (1 - Π)|) = N_0(|G_12|) = 132.938670 exactly confirms it.
- **Exp.** np.exp ×(1 + 10⁻¹³) is acceptable. My run uses mpmath upper bounds instead and gets the same digits.

### B-3. My independent certificate (revSF7/rev7_cert.py)
**Method.**
- Only the exact rows are taken from SF's Ops (= c36 C). Everything else is my own.
- My own group action on doubled midpoints. Covariance of Õ_0 and 1 - Π is checked exactly under my generators (transposition,
  4-cycle, reflection of axis 3) plus 5 random elements: 0 mismatches. My control (reflection about x_0 = ½): 490794 mismatches.
- Orbits 4, 8, 24, 32, 48, 48, 64, 96. Representatives = MAX index (163, 268, 271, 305, 307, 318, 319, 323; SF used the minima).
- **No symmetrisation.**
- Own torus-12 Bloch inverse via a sparse symbol: residual ≤ 9.8·10⁻¹⁵, sampled λ_min 0.039849.
- **Residual without BLAS:** each of the 557172 exact-product terms is accumulated sequentially (γ_{2162} bound).
- Weights: mpmath upper bounds. The Z = 0 block of K̃ - (1 - Π) is done in exact rationals. Row sums and final formulas in
  Fractions.
- Exact-rational spot checks of 192 E entries (the 12 largest + 12 random per column): all inside their radius (worst 2.3·10⁻³).

**Results.**

| m | k_m | k′_m | e_m | SF |
|---|---|---|---|---|
| 0 | 132.842053680 | same | 0.4381435558 | 132.842054 / 0.4381436 |
| 0.005 | 137.953039896 | same | 0.5056698588 | 137.95304 / 0.5056699 |
| 0.01 | 143.331451671 | same | 0.5843553316 | 143.33145 / 0.5843553 |
| 0.02 | 154.968508774 | same | 0.7835354543 | 154.96851 / 0.7835355 |
| 0.03 | 167.928623693 | same | 1.0567 (fails) | 167.92862 / 1.0567 |

- Per-column E totals equal SF's column by column (0.24224, 0.22997, 0.34052, 0.21876, 0.33599, 0.25963, 0.32870, 0.30926).
- **N_0(|Õ_0^{-1}|), 𝔠_0 ≤ 236.434155; 𝔠_∞^♯(δ = γ_0/2) = 236.434599 (SF 236.434602); λ_min(Õ_0) ≥ 4.2295074·10⁻³;**
  **N_{0.02}^{mid}(|C|) ≤ 715.9133, N_{0.01} ≤ 344.8425, N_{0.005} ≤ 279.0713** (identical to SF).
- q = N_0(|ΠQ^TQΠ|) = 161215/985608, computed directly (not as a difference of rows).
- **Audit verdict: CI-0 is CONFIRMED (computer-assisted).** It is reproduced by a stricter, BLAS-free, symmetrisation-free method
  with different representatives. The truncation dominates (inner residual ≪ 10⁻¹²), so the BLAS caveat of §23.2 is immaterial.
- **Informational (answers SF_LOG's "Collatz-Wielandt" idea):**
  - The Perron root of the type-mass matrix of |G_12| is 96.32, against the row-sum maximum 132.94.
  - So **any absolute-value ℓ² bound gains at most ×1.38**.
  - The 9.4× gap to the measured ||C|| ≈ 25 comes from sign cancellation; only a sign-aware (Bloch) bound can recover it.

### B-4. CI-0 proof text
- (1)-(5) are correct.
- **Non-binding (CZ-1):** "Õ_0 is invertible on ℓ²(links of Z⁴)" (l.2683) needs one sentence. The row-sum Neumann argument gives
  ℓ^∞. ℓ² follows because every torus T ≥ 3 has spectrum ≥ λ_c, the tori sample a dense set of Bloch momenta, and the symbol is
  continuous.
- "Compressions … (Rayleigh)" l.2737 ✓.

### B-5. CI-bg (l.2757-2775)
- (1)-(3) are rigorous:
  - Ω^+_□ ⊇ the 10-block region around Y ∈ □.
  - N5-an's (2S_*/r_*)α entry bound is the same in every gauge whose variables are ≤ α. That makes sup_Y|Δ^{(Y)}| row-summable to
    C_Δα_*. The same holds for Π_U.
  - R_g is real orthogonal, also for complex backgrounds, and right inverse = inverse in finite dimension.
- The Schur gap uses that Õ_U^{-1} is real symmetric, and positivity uses N5-sf0 (b).
- δ = γ_0/2 is a valid upper bound. The sharp value is C_Δα_* = 3.97·10⁻⁹ (m = m_4); it is numerically irrelevant.
- **KW-1 (WRONG, l.2773, §23.1 l.2855, SF_LOG l.371):** "stays finite for |κ - 1| ≤ 2.6·10⁻²". Exact:
  (1 - e_0 - δk_0)/(qk_0) = **2.5858·10⁻²**; at 0.026 the quantity is 1.0031 > 1.
  - Fix: "for |κ_0 - 1| < 2.585·10⁻², with 𝔠 = k′_0 + δ + k_0e_κ/(1 - e_κ), e_κ := e_0 + δk_0 + |κ_0 - 1|qk_0 (≈ 473 at the
    half-window 1.29·10⁻²); 236.43 at κ_0 = 1 only."
- **CS-1 (binding):** add to the statement "δ := C_Δα_* for the α_* in force". See Part C-3.

### B-6. CI-BR1 (l.2776-2801): CONFIRMED (substitution)
I checked every 𝔠_∞ use in PROOF (grep). The level-0 uses are BR1 (proof and (iii), (v)), NAH1 (∂_VU = -CF_AB), CURV1
(l.6028: "N_0(|C_0|) ≤ 𝔠_∞") and HG1 (iv). Each uses 𝔠_∞ only as an upper bound for N_0(|C|) on 𝔑(α_*), and CI-bg is the same
object: Õ^{-1} - (1 - Π_U), PROOF's 𝔠_∞ including ν_w + C_Δα_*. The level-1 𝔠_∞^{(1)} is correctly excluded.
- Nit (l.2796): "≥ 2n_1/r_* ≳ 10⁷ S_*" should read "= 2S_*n_1/r_* ≥ 1.15·10⁷S_* (r_* ≤ 1/220)".

### B-7. CHEB-f (l.2802-2813): CONFIRMED
- ATAP Thm 8.2 (truncation error 2Mρ^{-n}/(ρ - 1)) mapped to [a, b]. The degree-(D - 1) polynomial vanishes at block distance D.
- The vertex argument: |z|² is quadratic in cos t with positive leading coefficient ((b - a)/2)², vertex ≤ -1. So x_L is the
  nearest point and x_R the farthest. x_L > 0 for ρ < ρ_0, so the ellipse avoids (-∞, 0].
- Counting: (2D + 1)⁴ - (2D - 1)⁴ = 64D³ + 16D, ℓ¹ ≤ 4(3D + 2), ×324 per block row. The tail ratio is ((D + 1)/D)³ρ^{-1/2} < 1.
- Mine: ρ_0 = 1.026106, θ = 0.0257711 per block, μ = 5.36898·10⁻⁴, x_L = 3.17·10⁻³, N_μ(|Õ^{1/2}|) ≤ 5.71806·10¹⁶,
  N_μ(|Õ^{-1/2}|) ≤ 2.01139·10¹⁷.
- The real-background spectrum [a, b] with b = N_0(|Õ_0|) + δ (Schur) is right.
- **The "decay 0.02 per fine unit" is CI-bg's weighted Neumann (C), not CHEB-f.** CHEB-f gives 5.4·10⁻⁴ for Õ^{±1/2}. Keep the two
  rates apart in PROOF edits.

---

# PART C: thresholds, next constants, the N5-sf0 rerun (priorities 3-4)

### C-1. (TH-ch″) at the current class (rev7_arith)
- C_bg = 1.63952·10⁵.
- The ε_br entries:
  - 1.86·10⁻²⁹/C_Δ (with ε_* = 1.745·10⁻²⁴; SF 1.82 with 1.7·10⁻²⁴);
  - 7.454·10⁻⁷/C_♭;
  - 1.762·10⁻⁴r_♭;
  - r_♭/144;
  - 4.757·10⁻⁹.
- At τ^A, (TH-ch′) gives 1.2687·10⁻³⁹, and the break-evens are **C_Δ 8.39·10⁹, C_♭ 3.36·10³²**. SF's reading is CONFIRMED.
- At τ^♯ the C_Δ entry binds for C_Δ > 2.7·10⁻⁷ (CONFIRMED).
- **TB-1 (binding).** The binding entry is ε_bg^{(TH-bg)}/C_bg with the a_p entry only, but (TH-bg) (l.2117) is
  ε_bg²(n_1/2 + 1.03κ_sn_K) ≤ ½min{a_p, a_c}. With a_c ≈ a_p/2 (KF, κ_s = 1; SF's own A-1) and n_K = 1024 the factor is
  0.7056, so **ε_1 ≲ 8.95·10⁻⁴⁰**. This was harmless while the entry did not bind. Now it binds: state ε_1 with min{a_p, a_c}
  (a_c from KF as an inequality, not "≈").
  - Downstream: n_* 1.19·10⁸⁰, ≈ 42.0 levels, a_bad 4.2·10⁻⁸⁵.
- **DX′-1 reproduced:** (i) 7.31·10⁻¹⁸⁰, (ii) 4.69·10⁻¹⁷³, (iii) **2.456·10⁻¹⁵²/C_Ω** (R_sh 1.568·10⁵, m_sh 1.195·10²⁰,
  |Ω_B| 3.87·10²²), g_0 ≲ 1.57·10⁻⁷⁶/√C_Ω.
  - Note: (i)/(ii) are at the placeholder N′ = 1, so "28 orders" is a lower bound on the honest gain. The rate alone is worth 56
    orders: the same N′ with m_1 gives 1.1·10⁻²⁰⁸.
  - Sensitivities: N′/10 → ×125; μ×2 → ×254; τ^♯ ⇐ (GF-B^𝔥) → 1.8·10⁻¹¹⁸.
- CURV1 edit 5 arithmetic: 288𝔠³ = 3.81·10⁹ ✓ and 1/(80(48𝔠 + 1)) = 1.101·10⁻⁶ ✓. **But** 53(48𝔠 + 1)² = 6.83·10⁹ is now the
  larger 𝔠-term, and 288A_incoth⁴(m_1/2)ℓ_θ with coth⁴ = 2.9·10⁴² (ℓ_θ ∝ 1/m_1) dominates C_θ. So CURV1 is still unusable until
  its rate inputs are replaced too:
  - c_K, m_1 by CI-bg's (730.4, 0.02): valid for C_0 and C^0;
  - LOC's A_in, A_out are not covered.

### C-2. The next binding constants, and whether they certify "the same way"
- **C_Δ** (N5-an): binds at τ^A iff C_Δ ≳ 8.4·10⁹, i.e. S_*/r_* ≳ 1.6·10⁵, which is not implausible.
  - It is an analyticity constant of Õ(U, V) and Π_U (soft kernel X_0(M), (hh^T)^{-1}, (MP_ΛM^T)^{-1}). It is not a linear-algebra
    inverse, so the CI method does not apply.
  - But BR1 and CI-bg only need N_0 of the deviation, i.e. an explicit row-sum Lipschitz bound near U = 1. That is a
    semi-analytic, finite computation (first-order perturbation of each ingredient, Neumann bounds), and it avoids the crude
    n_1·(2S_*/r_*) factor.
  - After the rerun (C-3) the break-even is 1.2·10²¹, so C_Δ would bind at τ^A only if C_Δ ≳ 10²¹. At τ^♯ it binds unless
    C_Δ ≲ 3.9·10⁴.
- **C_♭**: break-even 3.4·10³². Since C_♭ = 4S_♭n_1/r_♭ ≥ 2.3·10⁷S_♭, it would need S_♭/r_♭ ≳ 10²⁵ to bind. Practically
  non-binding at τ^A; same nature as C_Δ.
- **C_Ω** (DX′; C + 3(N² - 1)/2 from SLC-sh): enters linearly. It is an explicit hand constant, not a certificate.
- **The real levers for the coupling ceiling are N′ and μ** (CHEB-f is crude). A certified (Õ + t)^{-1} family in the CI style, with
  Õ^{±1/2} via the resolvent integral, would replace CHEB-f's rate 5.4·10⁻⁴ by ≈ 10⁻² and N′ 5.7·10¹⁶ by O(10³). Order of
  magnitude of the gain: ≥ 10⁸ in g_0² (my estimate from the sensitivities, not a derivation).
- **The ε_1 lever after the rerun is τ_c** ((GF-B^𝔥)). The binding entry ∝ τ_c/𝔠, so (GF-B^𝔥) now moves ε_1 by ≈ 16 orders
  (2.9·10⁻²³ at τ^♯ with the rerun, if C_Δ ≲ 3.9·10⁴). This **reverses REVIEW_SF_S6's "(GF-B^𝔥) does not move ε_1"**: that was true
  at 𝔠 = 2·10³⁷, and it is false now.

### C-3. The proposed N5-sf0 rerun (§22.6; SF_LOG edit 4)
- **Validity.** N5-sf0 uses γ_0 as the lower bound of (Õ(1, 1))_Ω, and through it m (𝔇_0(m) ≤ γ/2, N5-w0's exact first moment),
  α_*, γ′ and ε_R. CI-0's λ_min(Õ_0) ≥ 4.2295074·10⁻³ is such a bound on every torus, for compressions too.
  - The only scope change: κ_0 = 1. In the window use (1 - e_0 - |κ_0 - 1|qk_0)/k_0. PROOF's evaluated numbers are at κ ≡ 1 anyway.
  - N5-w0's e^{20m} ≤ 1 + 40m holds at m = 2.57·10⁻⁵.
  - α_* < r_* still (it needs S_* ≳ 2·10⁻⁸).
  - **VALID SUBSTITUTION.**
- **Reproduced** with my own chain: m_4 = 2.57152·10⁻⁵, R_* = 3.23311·10⁶, T_0 = 1.29324·10⁷, ε_* = 2.47635·10⁻¹³/C_Δ,
  ε_R(R_*) ≤ ½ checked, ×1.42·10¹¹.
- **CS-1 (binding).** The rerun enlarges 𝔑(α_*), to C_Δα_* = 1.0568·10⁻³. On the new class (mine):
  - **𝔠_∞^♯ = 315.19** (with δ ≤ λ/4: 315.25);
  - λ_min ≥ 3.1727·10⁻³;
  - C_bg = 2.1857·10⁵;
  - ε_br entries 1.98·10⁻¹⁸/C_Δ, 4.19·10⁻⁷/C_♭, 1.32·10⁻⁴r_♭, r_♭/144, 3.57·10⁻⁹;
  - (TH-ch″) at τ^A: ε_1 ≤ min{9.52·10⁻⁴⁰ (TB-1: ≈ 6.7·10⁻⁴⁰), 1.13·10⁻¹⁸/C_Δ, 2.40·10⁻⁷/C_♭, 7.5·10⁻⁵r_♭, 2.04·10⁻⁹}.
  - SF's "ε_br entry 2.6·10⁻¹⁸/C_Δ, (TH-ch″) 1.5·10⁻¹⁸/C_Δ" (l.2820, C4 l.3) used 𝔠 = 236.43 and is inconsistent.
  - Rule: a PROOF edit must adopt 𝔠, λ_min and ε_* **for the same class**. Either keep the old class (236.43 / 4.2295·10⁻³ /
    1.7·10⁻²⁴) or adopt the new one (315.19 / 3.1727·10⁻³ / 2.48·10⁻¹³).
- The new class is better for ε_1 whenever C_Δ ≳ 1.1·10¹⁰. It is slightly worse (×0.75) otherwise.

---

# PART D: process (priority 5)

- **Provenance.** The order holds: PRE-STATED 07:57:19 (first edit), fixes to 08:03:20, criteria 08:12:41 (stat: birth = mod),
  script born 08:16:53, the single run 08:18:31-08:24:29, §22-§23 to 08:26:12. Exploratory runs before the criteria (ex1, ex2,
  scratch cert.py born 08:08:52) chose R, n and the m grid. That is legitimate for a computer-assisted proof (validity does not
  depend on when the parameters were chosen) and it is disclosed.
- **PV-1 (fix the log):** SF_LOG l.393 records an "08:29" calculation, but SF_LOG.md's mtime is 08:26:52 UTC. Either the time is
  wrong or the line was written before the event. Correct the timestamp (the 3.806·10⁹, 1.10·10⁻⁶, 93629.1 values are right; I
  reproduced them).
- **Memory.** s7: RSS 909 MB, footprint 1.18 GB. ex2: 1.36 GB RSS, 2.24 GB footprint, run at 39% free. R1 was written against
  RSS (in MiB), so it passed while the footprint budget was broken. ex2 is the serious one: 2.2 GB on the shared 8 GB machine.
  - **Disclosure: my own rev7_cert.py run had RSS 760 MB and a peak footprint of 1.18 GB (over the 1 GB budget).** It ran under the
    lock at 44% free (load 3.11), 470 s, exit 0. I estimated ≈ 650 MB from array sizes; the footprint measure counts transient
    numpy and fft buffers that RSS does not.
  - **Recommendations:**
    - budget criteria on /usr/bin/time's "peak memory footprint" with a 25% margin;
    - one torus column per pass (X 63 MB);
    - compute K̃'s type sums from the torus column before building the padded array;
    - for scouting, n = 8 tori;
    - never start below 40% free.
- **Out-of-lock calcs** (the 1 s pickle read of ≈ 100 MB in memory; the < 0.1 s arithmetic): negligible load, but rule breaks.
  Treat any python invocation, file inspections included, as a numeric job, or do the arithmetic by hand.
- **The s7 re-run was SKIPPED, by rule.** Its footprint is 1.18 GB > 1 GB. My own smaller computation replaced it.
- **My lock record** (revSF7/rev_lock.txt): mandated loop, acquired 08:48:58Z at load 3.11 and 44% free; nice 10; BLAS threads 1;
  python3 without -I; no `timeout`, no trap; exactly one rmdir at 08:56:49Z. Afterwards: no process left, and no __pycache__ in
  checks/ (PYTHONDONTWRITEBYTECODE; s7_sf.py was imported read-only for Ops).

---

# PART E: tally, binding fixes, PROOF edits

### E-1. Tally
**PROVEN-HERE 58 + 1 standard** (counted 10; not counted 48 = 43 + HO, CI-0 (computer-assisted, independently reproduced), CI-bg,
CI-BR1, CHEB-f's application). CONDITIONAL 8. ARGUED 4.
- OPEN names: SF's list + (C_♭-eval).
- I add: C_Δ evaluation is now the item that matters (it binds iff C_Δ ≳ 8·10⁹ at the current class), and it is part of the
  existing N5-an "not computed".
- 1 WRONG sentence: KW-1 (l.2773, l.2855, SF_LOG l.371). 0 GAP. No RLARGE §4.2 row discharged.

### E-2. Binding fixes (next SF session)
1. **CS-1.** CI-bg's δ := C_Δα_* of the class in force. §22.6 and the C4 line: recompute with 𝔠 = 315.19, λ = 3.1727·10⁻³ on the
   rerun class (numbers in C-3), or state that 236.43 belongs to the old class.
2. **TB-1.** The binding ε_1 entry uses the full (TH-bg) (min{a_p, a_c}, n_K term): ε_1 ≲ 8.95·10⁻⁴⁰ (old class) / ≈ 6.7·10⁻⁴⁰
   (rerun class). Rescale the §22.7 ε_1 rows.
3. **KW-1.** Window < 2.585·10⁻², 𝔠(κ) as in B-5.
4. **PV-1.** The SF_LOG timestamp.
5. The §20.1 l.2605 E-4 leftover.

Non-binding: CZ-1 (the ℓ² sentence), the C_Δ nit, the "rate 0.02 is CI's, μ is CHEB-f's" wording, the "28 orders is a lower
bound" note, and the R1 memory measure.

### E-3. Proposed PROOF.md edits (SF_LOG l.367-382)

| # | verdict | condition |
|---|---|---|
| 1 (𝔠_∞^♯ after the 𝔠_∞ definition) | **ACCEPT with fixes** | KW-1 window; "at κ_0 = 1; on the class 𝔑(α_*) in force (CS-1)"; add "CI-0 independently reproduced (REVIEW_SF_S7)" |
| 2 (ε_br, the 9.4·10⁴ factor; R20-fix 8 confirmed) | **ACCEPT** | the same class as edit 1 |
| 3 (gap line in RW-ℓ² / N5-sf0 (b)) | **ACCEPT with fix** | 4.2295·10⁻³ on the current class; 3.1727·10⁻³ if edit 4 is adopted |
| 4 (N5-sf0 rerun with the certified gap) | **ACCEPT as a valid substitution (owner decision)** | κ_0 = 1 scope; carry CS-1 consistently through 𝔠_∞, ε_br, RW-ℓ², BR1 |
| 5 (CURV1's 288𝔠³C_♭ term) | **ACCEPT the arithmetic; REJECT any implied usability** | add that 53(48𝔠 + 1)² = 6.8·10⁹ and the coth⁴(m_1/2) term (≈ 10⁴²) dominate C_θ; CURV1 still needs (c_K, m_1) from CI-bg plus LOC's constants |
| 6 ((C_♭-eval) named) | **ACCEPT** | also name a C_Δ evaluation as the binding one |

---

# PART F: strategic verdict

**Session 7 is the largest constants advance of the lane, and it survives an independent, stricter reproduction to all printed
digits.**
- 𝔠_∞ went from 2·10³⁷ to 236 (315 on the rerun class).
- λ_min went from 6.6·10⁻¹⁰ to 4.2·10⁻³.
- C's decay went from 4.8·10⁻¹¹ to 0.02 per fine unit.
- ε_1 rose 37 orders (to ≈ 9·10⁻⁴⁰ with TB-1), and the DX′ ceiling rose ≥ 28 orders.
- The method is clean: covariance-reduced columns, a residual enclosure dominated by truncation, and a perturbation to every
  background that costs nothing (δk_0 ≈ 10⁻⁶).

**What changed strategically:**
- (i) The N5-sf0 rerun is cheap and valid. Take it with CS-1. It removes C_Δ from the τ^A ceiling for any C_Δ ≲ 10²¹ and shrinks
  R_*/T_0 by 10⁵-10⁶.
- (ii) With 𝔠_∞ small, the ε_1 ceiling ∝ τ_c/𝔠. **(GF-B^𝔥) now moves ε_1 (≈ 16 orders) as well as every τ_c row**, so it is the
  next certificate.
- (iii) The binding coupling ceiling (DX′, g_0² ≈ 2.5·10⁻¹⁵²/C_Ω) is now limited by CHEB-f's crude N′ and μ. A CI-type certified
  resolvent family for Õ^{±1/2} is the lever. Absolute-value ℓ² sharpening of the gap is capped at ×1.38 (B-3); the remaining
  9.4× is sign cancellation.
- (iv) C_Δ, C_♭, C_Ω are analytic and hand constants. Only C_Δ can bind (≳ 8·10⁹ now; ≳ 10²¹ after the rerun), and an explicit
  first-order Lipschitz bound is the right form.

**Order:**
1. CS-1, TB-1, KW-1, PV-1;
2. the rerun with PROOF's owner;
3. (GF-B^𝔥);
4. a certified Õ^{±1/2} (DX′);
5. C_Δ explicit;
6. (DX-loc-4), (DX-loc-3) decoupling, E10.
