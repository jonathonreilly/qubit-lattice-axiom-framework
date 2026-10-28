# REVIEW_SF_S5: hostile review of lane F session 5 (SF.md [RSF4-fix] edits; §15-§17: Lemmas MSG_0, W-Lip, GF-dec, BCH-L; Propositions FP-uniq, FP-sh; (FP-det); Theorem SLC-sh; Proposition DX′; Lemmas KF, DX-rel; (CH-c), (TH-ch), Proposition CH-assign; dependency order O0-O6; check s5)

Reviewer: an independent agent that wrote none of SF.md. I edited no file except this one. No commits, PRs or pushes.

Inputs (read 2026-10-28 ~06:35-06:50 UTC):
- SF.md l.1806-2201 (§15-§17) in full. [RSF4-fix] spots l.1304, 1386, 1456, 1474, 1544, 1567-1572, 1579-1586, 1633, 1655-1660,
  1669-1724, 1728, 1778. SF_LOG.md session-5 block (l.177-240). REVIEW_SF_S4.md in full.
- checks/s5_criteria.md, s5_out.txt, s5_time.txt in full. s5_sf.py D-section (l.296-364) line by line; the rest skimmed.
- HIST §20.0-§20.2 (Theorem MSG, l.1182-1260).
- RLARGE.md (md5 24a73553… = SF's read) at l.50-129, l.230-399, l.680-794, l.1017-1022.
- PLD §15.4 (l.1104-1146).
- HW l.182-207, 596-605, and the a_bad uses.
- PROOF l.5418 (λ_min of N5-sf0).
- md5 now:
  - SF 83843fef… (= SF_LOG's final);
  - s5_criteria ad0e4d71…, s5_sf.py 6edaee23…, s5_out b9a1f55d… (all = SF_LOG);
  - HIST 468e9f03…, PROOF 4a7bbccc… (= SF's reads).

Scratch: scratchpad `revSF5/`. It holds:
- indep.py, my independent mpmath re-derivation of the F-arithmetic and the cross-lane scalings (not SF's code), and indep_out.txt;
- rev_s5_out.txt, rev_s5_time.txt, rev_lock.txt.

---

## Bottom line

- **RSF4 fixes:** all 9 binding groups are applied in place and tagged. DX-1 and DX-2 are correctly downgraded and superseded.
- **MSG_0, W-Lip, GF-dec, BCH-L, FP-uniq, FP-sh, SLC-sh, KF, DX-rel: CONFIRMED.**
  - I re-derived GF-dec's constants (c_D = 1/324, q, m_FP = 3.858·10⁻⁴/block, S_4(q) = 1.7333·10¹⁶, G_∞ ≤ 5.8954·10²³) and the
    radius chain.
  - **The chain is tight:** (I1) = 0.4995 and (I4)/r = 0.990 at SF's point. The optimum is ζ_max = 2.209·10⁻⁵⁵, against SF's 2.188.
    The difference is immaterial.
- **Gribov question.** It is settled on E_good(τ_c) by an actual argument. It is not convexity. It is (a) a localised
  Faddeev-Popov insertion (FP-sh counts only the zero in 𝒩(U_0), so far copies never enter, whether or not they exist), plus (b) a
  sup-norm contraction with an a priori orbit bound (FP-uniq (5)). Together these exclude every other slice point with
  |A′|_∞ ≤ r_sol.
  - **s5 D3's failure does not weaken this.** It is a failed positive control: it shows only that the copy-finder is too weak. It
    does not test the proof. Its one cost is that D2 has no demonstrated sensitivity.
- **(CH-c) / CH-assign: the set inclusion and the circularity argument (iii) are CORRECT. The assignment is WRONG in two citations,
  and the circle is NOT closed as written (Fix CH-1, binding):**
  - (a) The "[v2-E8] event" is routed to RLARGE. But RLARGE prices it as (D-c) → (D-b) → §3.4 → **branches (ii)/(iii)** (RLARGE
    l.258-260, l.367-368). At stage 0, the rough inter-cube fine plaquettes above τ_c that are uncut by χ_Q are in supp μ^+ ∩ (CH-c).
    So (SG^fl)_0 ⇐ (SF)_0 ⇐ RLARGE (D-c) ⇐ branch (ii) ⇐ (SG^fl)_0. They must go to DX-rel.
  - (b) "∂Λ(𝔥)-adjacent plaquettes are HIST boundary terms (e^{B_0} per boundary cube)" is the reading that REVIEW_PLD_S3 SG-1
    withdrew. e^{B_0} is a cost, not a suppression. RLARGE (D-d)/E10 is **OPEN** (l.261-265).
  - So (CH-c) is **CONDITIONAL ⇐ DX-rel + (DX-loc) + RLARGE E10 + a V-side scope hypothesis**, not "assigned / discharged".
- **DX′: CONFIRMED as stated** (CONDITIONAL ⇐ (FP-det) + (BGC); the inclusion and per-block factor PROVEN). DX-1 does not arise:
  the bound is relative to the white-noise reference. The g_0-ceiling it implies is unevaluated and must be (Fix DX′-1).
- **(TH-ch) is consistent but insufficient.** (TH-bg) needs ε_bg ≤ 2.51·10⁻⁶² = 5.8·10⁻⁴τ_c. With BR1 (iii)'s ε_bg ≲ C_bgε_1, the
  binding threshold condition is **ε_1 ≤ min{τ_c, 2.51·10⁻⁶²/C_bg}**, not ε_1 ≤ τ_c (Fix TH-1).
- **Cross-lane thresholds.** No lane found needs ε_1 BOUNDED BELOW by a g-independent constant (every lane's ε_1 condition is an
  upper bound or a min{}). But ε_1 ≈ 10⁻⁵⁹ to 10⁻⁶⁵ makes several derived constants explode (the table in Part E):
  - RLARGE n_* ≈ 5·10¹¹⁸;
  - n_♯ ≈ 7·10¹²⁷ (joint route) to 7·10²⁴⁵ (RS route);
  - HW a_bad ≈ 10⁻¹²³ to 10⁻¹³³.
  It also turns the torus/final-levels caveat from O(1) levels into ≈ 60 levels. Every lane's quoted ε_1 = 0.5 arithmetic becomes
  non-admissible.
- **s5: honest and reproduced.** Criteria born 06:16:32 UTC, before the script (06:19:23). The pre-run desk fix at 06:21:07 came
  before the output (06:21:27). My re-run under the lock is **byte-identical: OVERALL FAIL 19/20 (D3)**.
- **Corrected tally:**
  - PROVEN-HERE 44 + 1 standard, with CH-assign scoped to the inclusion + (iii);
  - CONDITIONAL 8: SF's 7 + (CH-c);
  - ARGUED 3;
  - "(CH-c) assigned" is withdrawn from "Discharged";
  - new dependencies: RLARGE E10 and an (FP-det) cube-size condition.

---

# PART A: [RSF4-fix] edits (fix numbers = REVIEW_SF_S4 Part F)

| # | SF line | verdict | note |
|---|---|---|---|
| 1 DX-1 | l.1669-1675, l.1689 | CONFIRMED | a′'s (P)/kernel exponent is downgraded to ARGUED. Superseded by DX′ and DX-rel (Part C). |
| 2 DX-2 | l.1676-1679, l.1703 | CONFIRMED | Branch (i) is removed from (O2) and KF is cited instead. |
| 3 SC-1..3 | l.1655-1660 | CONFIRMED | The ½-chart form is explicitly not attacked. SLC-sh meets SC-1..3 (C-4). |
| 4 D-1 | l.1704-1706 | CONFIRMED (naming) | The content is in §16.3. The assignment is defective (Part D). |
| 5 D-2, D-3 | l.1706-1711 | CONFIRMED | |
| 6 GD-1, DL-1 | l.1567-1572, l.1579-1585 | CONFIRMED | a_*^B ∝ ρ_*²: under ρ_* → ρ_band this becomes ∝ ρ_band² ≈ 10⁻¹²² (Part C-5). |
| 7 CQ-1 | l.1386, l.1474, l.1544 | CONFIRMED | 807.4566 reproduced by s5 F3. |
| 8 RT-1 | l.1304, l.1728 | CONFIRMED | |
| 9 cosmetic | l.1633, l.1720 | CONFIRMED | |
| HALO-b | l.1456 | CONFIRMED | |
| tally | l.1778 | CONFIRMED | |

---

# PART B: the shrunk-chart gauge fixing (O1)

### B-1. Lemma MSG_0 (l.1833-1840; proof l.1917-1935): CONFIRMED (a correct specialisation of HIST Theorem MSG)
- (1) γ_{c_X} = ∅ ⇒ g_ax(c_X) = 1. γ_x ⊂ B(X), so g_ax on B(X) reads only B(X) ✓.
- (2) Path covariance hol_{g·W}(z → z′) = g(z)hol_Wg(z′)^{-1} under SF's left action. So (g_ax·U_0)_b = hol_U(γ_x)^{-1}hol_{U_0}(π)hol_U(γ_y)
  and U_b = hol_U(γ_x)^{-1}hol_U(π)hol_U(γ_y). Unitary invariance gives the identity ✓. This is HIST MSG step (2) (l.1236-1238) with
  V := U and g(c_X) = 1, transposed from HIST's g^†Ug convention ✓.
- (3) The intra-block ladder has Σ_{ν>μ}|x_ν - c_ν| ≤ (d - 1)h plaquettes (= 3 ≤ A_d = 9 at d = 4, L = 3). (F4) is applied to U_0 and
  to U separately ✓.
- (4) The inter-block ladder is ≤ (d - 1)hL = A_d ✓. ||hol_W(S_c) - V_c|| ≤ A_dτ + 18.4y² + τ ≤ (A_d + 2)τ by (S2) ✓. In total,
  2·[A_d + (A_d + 2)]τ = (4A_d + 4)τ ✓.
- (5) (S0) ⇒ ||·|| ≤ ½. (F1) ⇒ C_0 = 1.011·40 = 40.44 ✓.
- (6) g_ax(g′·U_0) = g_ax(U_0)g′^{-1}, so A^0 is an orbit function ✓.
- **"Reads two blocks per link":** true for A^0. The *bound* also reads V_c and the contours of c ⊂ B(X) ∪ B(Y) ✓.
- **Volume independence of C_0:** true. No recursion (MSG step (6)) is used at one scale ✓.
- s5 A1-A7 reproduced. The A7 negative control is meaningful.

### B-2. Lemma W-Lip (l.1841-1843; l.1937-1944): CONFIRMED (structure checked)
- The holonomy differences (≤ #links·ρ) are correct.
- The (F3) factor 2 is correct.
- The fixed-point comparison |X_0 - X_0′| ≤ 1.59δ is correct.
- I did not re-derive NA-alg (a)'s internal constants (0.052, 0.163, 4.5y′); they are cited.
- C_W = 95.15 is reproduced.

### B-3. Lemma GF-dec (l.1844-1851; proof l.1946-1967): CONFIRMED (re-derived)
- **(a)** M_X(vδ_y) = L^{-d}Ad(U_b)v for y = c_X + e_μ. Hence σ_min(M_X) ≥ L^{-d} and ||M_X^+|| ≤ L^d ✓. s5 B3 measures 2.06-2.83·L^{-d}.
- **(b) is the key step and it is right.**
  - ℓ_P(D_Uλ) = Ad(T_P)λ(y) because λ(c_X) = 0. Cauchy-Schwarz gives |λ(y)|² ≤ dhΣ_P|(D_Uλ)_b|².
  - A direction-μ link at z lies on ≤ hL^{d-1} ≤ L^d axial paths from c_X.
  - So ||λ||² ≤ dhL^d||D_Uλ||².
  - **No property of U is used:** the gap is a Dirichlet point per block.
  - c_D = 1/324 at d = 4, L = 3.
- **(c)** G_res(X, Y) = 0 for |X - Y|_∞ > 1. The Neumann series at c = (c_D + 4d)/2 gives q^{|X-Y|}/(c(1 - q)) = q^{|X-Y|}/c_D ✓.
  m_FP = -log q = 3.858·10⁻⁴ ✓.
- **(d)** The inverse formula is right; s5 B5 checks it to 3·10⁻¹⁵.
- **(e)** G_∞ ≤ L^d + c_D^{-1}S_d(q)(1 + 4d·3^dL^d). I recomputed S_4(q) by direct summation: 1.73329·10¹⁶, G_∞ = 5.89536·10²³ ✓.
- **"Gap 1/324 for every background; decay 3.9·10⁻⁴ per block": verified as stated.**
- **Non-binding remark (the source of every astronomical number).** The Neumann rate is ≈ c_D/(4d). A Chebyshev /
  Demko-Moss-Smith bound for banded positive operators gives a rate ≈ 2√(c_D/(4d)) ≈ 2.8·10⁻² per block. That lowers S_4 by ≈ 10⁷
  and G_∞ by ≈ 3·10⁷. Since ζ ∝ G_∞^{-2} (Part B-5), τ_c would rise by ≈ 10¹⁵. s5 B6's measured 1-2 per block says even this is
  conservative.

### B-4. Lemma BCH-L (l.1852-1854; l.1969-1975): CONFIRMED
- |g| ≤ G(0.6) = 2.327 on the ℓ¹-ball of radius 0.6 ✓.
- Cauchy on the radius-0.3 disc ✓.
- Schwarz from Dg(0) = 0 ✓.
- c_g = G(0.6)/0.09 = 25.85 ✓, and c′_g = √Nc_g ✓.

### B-5. Proposition FP-uniq (l.1855-1861; proof l.1977-1999): CONFIRMED
- (1) e^{λ(x)}e^{A^0_b}e^{-Ad(U_b)λ(y)} gives A(λ) = A^0 - D_Uλ + R(λ), with R(0) = 0 ✓.
- (2) |h_U(A)(X)| ≤ dh|A|_∞ and |(P_resD^*A)_X| ≤ 2dL^{d/2}|A|_∞. So X_∞ = 72 ✓ (≥ dh).
- (3) The ℓ¹-size of each triple is ≤ s_0 + 2r. BCH-L gives |R - R′| ≤ 2c′_g(s_0 + 2r)||λ - λ′||_∞ ✓. Lip(T) ≤ ½ by (I1) ✓.
  T(B_r) ⊂ B_r by (I2) ✓.
- (4) r_sol dominates s_0 + 2r_* + 2c′_g(s_0 + 2r)r_* ✓.
- **(5) Uniqueness in A: the actual anti-Gribov argument.**
  - g′(y) = U_b^{-1}e^{-A′_b}g′(x)e^{A^0_b}U_b propagates ||1 - g′|| ≤ dh(r_sol + s_0) from the centre along γ_y.
  - So λ′ := log g′ lies in Λ ∩ B_r by (I4), and λ′ is a zero of Φ_ω. By (3), λ′ = λ_*.
  - This is correct and volume-independent.
  - The post-proof ε^thr_N caveat for N > 12 is right.
- **Radius chain (indep.py, mpmath, my own bisection).**
  - At SF's point (ζ = 2.1880·10⁻⁵⁵, r = 509.36·G_∞ζ): (I1) = 0.49950, (I2) holds, (I3) holds, (I4)/r = 0.9901, (S0) holds ✓.
    r_* = 5.1596·10⁻³¹, r_sol = 1.0319·10⁻³⁰, τ_c = 4.3386·10⁻⁵⁹ ✓ (all of s5 F2 reproduced).
  - The optimum over ρ is ζ_max = 2.209·10⁻⁵⁵ at ρ ≈ 505, i.e. τ_c = 4.38·10⁻⁵⁹: a 1% change. **Scaling:** ζ ≈ 1/(4032c′_gX_∞G_∞²),
    so every threshold is ∝ G_∞^{-2}.
- Cosmetic: §15.1 says "(I1) 2c′_gq_∞(s_0 + 2r)". The proof's Lipschitz constant is G_∞X_∞·2c′_g(s_0 + 2r) = 2c′_gq_∞(s_0 + 2r). Same thing ✓.

### B-6. Proposition FP-sh (l.1862-1870; proof l.2000-2024): CONFIRMED
- (0) E_good is 𝒢_V-invariant (M̄_c is root-covariant and g(c_X) = 1) ✓.
- (1) J(U_0, ω) = c_N^{n_Λ}/Δ(A_*), since j(0) = 1 at the zero, which is non-degenerate (||DT|| ≤ ½) ✓.
- (2)-(3) The substitution U_0 → g^{-1}·U_0 is right. I checked the 𝒩 and Φ covariance with SF's left action:
  1_{𝒩(g^{-1}·U_0′)}(g) = 1_{𝒩(U_0′)}(1) and Φ^{g^{-1}·U_0′}(g) = Φ^{U_0′}(1) ✓.
- (4) The two-sided identification via FP-uniq (5) ✓.
- (5) ∫γ̃(ω)δ(χ_U(A) - (0, ω))dω = δ(h_U(A))γ̃(P_resD^*A) ✓. The post-proof c-number c_N^{-n_Λ} is correct.
- **Answer to priority 4:**
  - "No Gribov copy enters" is exact. The insertion is localised to 𝒩(U_0), and this is the standard small-field device.
  - The uniqueness clause of (FP-loc)_0 is PROVEN on the r_sol-chart, not on the ½-chart. That is all E_good needs.
  - The argument is contraction + an a priori bound, not convexity of a gauge functional; none is needed.
- **Note FS-1 (non-binding but should be written).**
  - "The truncation is invisible" (p_X small) needs u_0ζ² ≫ N·m_X, i.e. g_0 ≲ 4·10⁻⁵⁷ for p_X ≤ ½ (indep). The exact identity
    does not need it (Z_ζ is a c-number either way).
  - The band condition (C-5) implies it with room to spare. State the implication.
- **Note FS-2 (the chart is larger than E_good).**
  - {|A|_∞ ≤ r_sol} contains fields with plaquettes up to ≈ 4r_sol ≈ 4·10⁻³⁰ ≫ τ_c. So 1_{E_good}(e^AU) is a nontrivial, non-convex
    cut inside the chart.
  - DX′ handles this correctly (TILT takes an arbitrary event E_𝔅 ⊂ E_good ∩ chart), and the band lies inside E_good. Write it once
    explicitly in FP-sh's reading.
- **(FP-det): ARGUED is the right status.** The bound ||K||_{B∞→B∞} ≤ 2c′_gq_∞r_sol ≤ ½ is right.
  - **Note FD-1 (to add to the (FP-det) statement):** the polymer decay is m_FP ≈ 3.9·10⁻⁴ per L-block, with a G_∞ ≈ 6·10²³ prefactor.
    CE-Q-col's norm needs rate κ_c ≈ 2.9·10³ per **M-cube**.
  - This is compatible only because M/L ≈ 10¹⁴ blocks: e^{-m_FP·M/L} ≈ e^{-4·10¹⁰}.
  - Record the condition m_FP·M/L ≥ κ_c + log G_∞ + O(1) as an (M-W)-type hypothesis of (FP-det). It holds at M = M_W3; it fails at
    any M ≲ 10⁸.

### B-7. s5 D3 and the Gribov question (priority 4)
- Pre-registration was honoured. Criteria l.37-39 say "If no run converges, D3 is reported as INCONCLUSIVE and counts as FAIL". The
  criteria were born before the script.
- **Why D3 failed (design, from s5_sf.py l.354-364):**
  - The starts are N(0,1)·U(0.6, 1.4) per component, i.e. per-site rotations up to |λ| ≈ 3-4 ≈ π. A_of uses the principal su(2) log,
    so Φ is discontinuous across the cut.
  - The backtracking stops at t ≈ 10⁻⁴ and accepts the step anyway (l.334-338).
  - A plain Newton method on a non-smooth landscape from far starts is not a copy-finder.
  - s4 D2 found non-small zeros of h_U∘A (max|A| 0.35-0.50) by another route. Gribov-type copies of the h_U part are exhibited; for the
    full χ_U = (h_U, P_resD^* = ω) they are not.
- **Verdict:**
  - D3 is a failed positive control. It *fails to test* whether localisation is load-bearing.
  - It does not weaken FP-uniq or FP-sh: their proofs never assume absence of far copies, and FP-sh is exact even if copies exist.
  - The only cost is evidential: D2's "same zero from 10 starts" has no demonstrated sensitivity, and D2's starts lie in a ball where
    the contraction already forces uniqueness.
  - A real control would relax a gauge functional along random 𝒢_V-orbits (Los-Alamos-type over-relaxation) under the χ_U
    constraint.
- Non-binding check-design fix: a far-copy finder by orbit relaxation, not Newton from random λ.

### B-8. Theorem SLC-sh (l.1871-1875; l.2026-2033): CONFIRMED
- r_sol ≤ a_θ ⇒ θ_1 = 2(C_coer r_sol + C′g_0²) ≤ 2(C_coer a_θ + C′g_0²) = ½ exactly ✓.
- K_{Ω^+} = 𝒞1_{Ω^+}𝒞/||C|| depends only on Ω (SC-1) ✓.
- Straddling terms are inside T(Ω^+) (SC-2) ✓, and the chart is stated (SC-3) ✓.
- The (FP-det) terms are linear in |A| (once (FP-det) holds) and enter C_Ω ✓.
- REVIEW_SF_S4 C-6's reformulation is executed as recommended. The Gribov content of the session-4 wall is gone.

---

# PART C: pricing on the chart and in the holes (priority 5)

### C-1. Proposition DX′ (l.1876-1884; l.2035-2053): CONFIRMED as stated (CONDITIONAL ⇐ (FP-det) + (BGC); inclusion and factor PROVEN)
- **(a) Band in E_good.**
  - Plaquettes: ε_bg + 4ρ_band ≤ τ_c/2 + 2τ_c/C_W ✓.
  - Mismatch: ≤ ε_bg + C_Wρ_band ≤ τ_c ✓.
  - X_∞ρ_band ≤ ζ ✓.
  - ρ_band = min{τ_c/(2C_W), s_0/(√NX_∞)} = 2.28·10⁻⁶¹ (τ_c entry binding; reproduced).
- **(b)-(c)** Inclusion and multiplicity m_sh ✓. **(d)** TILT with a fixed K and θ_1 ≤ ½ ✓.
- **(e)** No background action and no defect enter a′ ✓.
  - The background is critical (SF l.126: BR1 (ii)), so there is no O(u_0) linear term.
  - The 𝔫 linear source is O(1) and is in C_Ω.
  - **DX-1 does not arise: CONFIRMED.**
- **Fix DX′-1 (binding, statement).** The "g_0² below a g-independent but astronomically small number" (l.2050) must be evaluated and
  carried to O0. It is the binding coupling ceiling of the whole stage.
  - Inputs: a′ = a_sh²/(8N||C||m_sh), with ||C|| ≤ 1/λ_min (N5-sf0's gap, PROOF l.5418 quotes ≈ 7·10⁻⁸² in one form).
  - a_sh ∝ ρ_band ≈ 2·10⁻⁶¹; m_sh ≈ (2R_sh/L)⁴ ≈ 10⁴⁸; |Ω_B| ≈ 10⁴⁸-10⁵⁰.
  - My order-of-magnitude estimate (not a derivation): g_0² ≲ 10⁻³⁰⁰. Let SF compute it.
- **Fix DX′-2 (binding, band re-tune).** "CE-Q-col holds verbatim with ρ_* → ρ_band" (l.2037) is right for the analytic estimates. But
  (B1′)/GD-1 now read 2ρ′ + g_0√NN_r2^{j+1}p ≤ ρ_band.
  - So j_max, a_*^B ∝ ρ_band² and the band's g_0-window all move. The window is g_0 ≲ ρ_band/(4√NN_rp_0) ≈ 10⁻⁶⁶/N_r.
  - State these as the re-tuned hypotheses. Do not leave them implicit in "stronger hypotheses".

### C-2. Lemma KF (l.1885-1887; l.2056-2066): CONFIRMED (re-derived)
- Nφ = Re tr((1 - X)G), with G = H + iθ1 (SU(N) maximiser: the anti-Hermitian part is scalar) ✓.
- The three terms are bounded correctly: Re tr(1 - X) = ½Σt_a², the trace-norm bound for the normal (1 - X), and |sin| ≤ t ✓.
- ½t² - ct ≥ ¼t² - c², and Nc² = 1354.24Ny⁴ ✓. The upper bound uses ||G|| ≤ ||M|| ≤ 1 ✓.
- The n_c lower bound uses only φ ≤ ||V - W_0|| (no spread condition), so it holds for every M ✓.

### C-3. Lemma DX-rel (l.1888-1895; l.2068-2090): CONFIRMED as an inequality of the hole integrand
- **Numerator.** s ≥ ||1 - W||²_op/(2N) ✓. KF gives a_c (y_c ≤ 1.011√NA_dτ_c, from the block-pair plaquettes ≤ τ_c) ✓. 1/n_c ≤ e(u_0κ_s)^{N²-1}/c′_N ✓.
- **Reference.** s(U_p) ≤ ε_bg²/2 ✓; φ_c(U) ≤ 1.03ε_bg² ✓; 1/n_c(U) ≥ 1 ✓.
- **Both post-proof corrections are right and necessary.**
  - The kernel values must be in (TH-bg).
  - Holes are 4^d blocks: a defect plaquette touches ≤ 2^d blocks, and the union of their 3^d-neighbourhoods is a 4^d block cube.
  - n_R = 82944, n_1 = 497664 (an overcount, safe), n_K = 1024 ✓.
  - The a_p entry gives ε_bg ≤ τ_c/√(2Nn_1) = 2.5108·10⁻⁶² (indep; s5 F2's 4.4636·10⁻⁶² is the 3^d count, as SF says).
- **The hole is bounded:** correct. For X outside the hole, no neighbour Y carries a defect, so MSG_0's hypotheses hold on every
  block pair meeting X.
- **Note DR-1 ((DX-loc) scope, not binding here).**
  - The *gauge-fixed* field outside the hole is a nonlocal function of the data, through (χ_UΓ)^{-1} (range ≈ 1/m_FP ≈ 2600 blocks,
    prefactor G_∞).
  - So "factorisation across ∂R(D)" in (DX-loc) is a decay statement at rate m_FP, not an exact factorisation.
  - The (FP-det) cube-size condition FD-1 applies there too.
  - The hole's Gaussian normalisation costs a polynomial ≈ u_0^{(N²-1)n_R/2} ≈ u_0^{331776} per defect. It is beaten by
    e^{-u_0a/2} only for g_0 tiny: fine, but put it in DX′-1's ceiling.

### C-4. (SL-coer′) with K fixed in advance: CONFIRMED (B-8). The ½-chart statement is correctly abandoned.

---

# PART D: (CH-c), (TH-ch), CH-assign and the order O0-O6 (priority 6)

### D-1. What is right
- **(iii) is correct and important.**
  - (SG^fl)_0 is E_{μ^+}[exp(tΣ⟨u, Y⟩) | V] over the whole cut-good fixed-V law μ_V ∝ 1_cut e^{-S_W/g_0²}K_0 (PLD l.1109).
  - So its derivation via (G0-2) = (SF)_0 must already price every configuration in supp μ^+.
  - Pricing any part of supp μ^+ ∩ (CH-c) by branch (ii) ⇐ (SG^fl)_0 is circular.
  - So **(CH-c) must never go to branch (ii)**, and the order is non-circular *because of that*, not because branch (ii) comes later. ✓
- **The set inclusion of (i)** is correct as far as it goes. Under (TH-ch), cut-good + (E1) on cube interiors + soft residual ≤ ε_* ≤ τ_c
  (G0-3, PLD l.1131) implies E_good *except* on (α) inter-cube fine plaquettes, (β) ∂Λ(𝔥)-adjacent plaquettes and (γ) mismatches above
  the soft threshold.
- **(ii)'s domain claim** holds for the plaquettes of A, which are < ε_1 by G0-3's "cut extended to all plaquettes near A".

### D-2. Fix CH-1 (binding): the [v2-E8] leg reopens the circle
- RLARGE's χ_Q reads **cube-interior plaquettes only, and is never changed** (RLARGE l.55-56).
  - So at stage 0, inter-cube fine plaquettes are uncut in μ^+.
  - Those above τ_c are in supp μ^+ ∩ (CH-c), away from A.
- CH-assign (l.2097-2098) and O4 (l.2123-2124) send them to RLARGE's "[v2-E8] event".
- RLARGE prices that event as **(D-c), "priced as (D-b)"** (l.258-260). (D-b) is priced by §3.4 (l.367-368): "PLD §9.5's split at η_♭′
  gives a KN mismatch (branch (i)) or a plaquette of N_1(Q) ≥ η_♭′, priced as above (**branches (ii)/(iii)**)".
- So, as cited: (SG^fl)_0 ⇐ (SF)_0 ⇐ pricing of (α) ⇐ RLARGE (D-c)/(D-b) ⇐ branch (ii) ⇐ (SG^fl)_0. The alternative leg, branch (iii),
  is ARGUED (CLS-sf) and is built for coherent backgrounds, not single rough plaquettes.
- **Fix.** At stage 0, price every fine plaquette > τ_c (interior or not) and every mismatch > τ_c by **DX-rel + (DX-loc)**, in-step.
  This is exactly what DX-rel is: Wilson/kernel positivity relative to the background, on a bounded hole.
- Then replace "the [v2-E8] event" in CH-assign (i), O4 and the RLARGE owner note by "DX-rel-priced defects".
- Add an RLARGE owner note: at stage 0, §3.4's plaquette leg above τ_c for (D-b)/(D-c) is DX-rel, not (ii)/(iii).

### D-3. Fix CH-2 (binding): boundary-adjacent plaquettes are OPEN, not "HIST boundary terms"
- CH-assign (l.2095-2096) says the ∂Λ(𝔥)-adjacent plaquettes "are HIST boundary terms (e^{B_0} per boundary cube)".
- RLARGE v2 (D-d) (l.261-265) states the opposite: "e^{B_0} is a cost, not a suppression" (REVIEW_PLD_S3 SG-1). This family needs its
  own e^{-a/g²}, and it is **OPEN (E10)**.
- DX-rel can price the interior side of such a defect only if the hole does not meet ∂Λ(𝔥). A hole that meets the history boundary
  needs E10.
- Fix: cite (D-d)/E10 as OPEN. (CH-c) inherits it.

### D-4. Fix CH-3 (binding, scope): E_good presupposes a V-event, and ε_bg must be local
- §15.0 defines ε_bg as a GLOBAL maximum, and O0 says ε_bg comes "from BR1 (iii)".
- But V is cut only on level-1 cube interiors. Level-1 inter-cube plaquettes of V can be rough. That is the actual level-(k+1) [v2-E8]
  event, about the N5 *background*.
- Near such a V-plaquette, U(V) is not ε_bg-small, so FP-sh's hypothesis ε_bg ≤ τ_c/2 fails there, and the global statement fails.
- Fix:
  - state (SF)_0 on a V-event 𝒱^sf(Λ′) (all level-1 plaquettes of V on Λ′ < ε_1, matching (SG^fl)'s domain, PLD l.1144-1146);
  - define ε_bg as a max over Λ′;
  - leave the rough-V complement to RLARGE's level-1 defect pricing, which is not SF's (CH-c).
- With this scope, the localised versions of GF-dec/FP-uniq on Λ′ go into (DX-loc), next to the frozen-hole complement already there.

### D-5. Fix TH-1 (binding): (TH-ch) must carry the (TH-bg) constraint
- (TH-bg) needs ε_bg ≤ 2.51·10⁻⁶² (a_p entry alone; the κ_s-kernel entry lowers it further).
- BR1 (iii) gives ε_bg ≲ C_bgε_1 (SF l.2112, a bracketed remark).
- So the stage-0 threshold condition is **ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}** ≈ 5.8·10⁻⁴τ_c/C_bg. This is not ε_1 ≤ τ_c.
- O0 lists the steps in the right order but states the outcome too weakly. Write the min and compute C_bg from PROOF l.5637
  (3p_Lr(ε)).
- The s5 F2 "consistency" covers only (I1)-(I4) and (S0). It does not cover (TH-bg) against BR1.

### D-6. The order O0-O6 (l.2114-2132)
- O1 → O2 → O3 → O5 → O6 is non-circular: O1 consumes HIST MSG (2)-(4), NA-alg, NA-FP (i)-(ii) only, and O2-O3 consume O1 + SLc/TILT/DL.
- **As written, O4 cites RLARGE [v2-E8] and "boundary terms". By D-2 this routes through branch (ii), and by D-3 it relies on an OPEN
  family.** So O0-O6 is NOT non-circular as written.
- After Fixes CH-1..CH-3 and TH-1:
  - O4 ⇐ DX-rel (PROVEN inequality) + (DX-loc) [OPEN] + RLARGE E10 [OPEN] + the bare-level history (cut-bad cubes, outside Λ(𝔥), bare
    R1 by Wilson positivity, RLARGE App. A);
  - no (SG^fl)_0, no branch (ii), no (H-w) weight source;
  - and then the order is non-circular.
- **Status:** (CH-c) is **CONDITIONAL ⇐ DX-rel + (DX-loc) + E10 (+ the D-4 V-scope)**. It is NOT "assigned / discharged" (§17.1
  l.2154, l.2173). CH-assign stays PROVEN-HERE as a set inclusion + the circularity argument (iii).
- **k ≥ 1:** (GF-dec)_k is correctly named OPEN. At k ≥ 1 the DX-rel analogue needs CLS-sf (branch (iii)), which is ARGUED. The k ≥ 1
  statement "at most ARGUED" stands.

---

# PART E: τ_c ≈ 4·10⁻⁵⁹ and the other lanes' thresholds (priority 7)

Method: I grepped every lane for ε_1 conditions, then recomputed the derived constants by scaling the sources' own quoted reference
values (indep.py; [arithmetic]). **No lane found requires ε_1 ≥ (g-independent constant)**: every ε_1 condition is an upper bound or
enters through min{}. So there is no hard conflict. The consequences are below.

| lane / item (source) | condition or constant | at ε_1 = 0.5 (as quoted) | at ε_1 ≤ τ_c ≈ 4.3·10⁻⁵⁹ | verdict |
|---|---|---|---|---|
| SF (TH-bg) + BR1 (iii) | ε_bg ≤ 2.51·10⁻⁶², ε_bg ≲ C_bgε_1 | n/a | ε_1 ≲ 2.5·10⁻⁶²/C_bg | **TH-1: (TH-ch) too weak** |
| RLARGE [v2-C] N5 compat. (l.68-74) | ε_1 ≤ N5 level-0 threshold ≈ 2·10⁻³²/C_Δ | violated at 0.5 | satisfied | consistent (helps) |
| RLARGE [v2-E8] (l.75) | ε_1 ≤ ε_* < 2sin(π/N); (TH-ch) also needs ε_* ≤ τ_c | ok | ok (ε_* lowered) | consistent; KN price e^{-κε_*²/(256Ng²)} shrinks |
| RLARGE η_1 (l.63) | min{ε_1/18, ε_1²/(4608N)} | 2.7·10⁻⁵ (N = 2) | 2.0·10⁻¹²¹ | g-indep.; a_RS ∝ η_1² ≈ 10⁻²⁴³ |
| RLARGE n_* = ⌊4/(a″β_-)⌋, a″ < ε_1²/(4N) (l.791, l.1017) | slope (n_* + 1)a″β_- > 4 | 382 / 255 (SU(2)/SU(3)) | **≈ 5·10¹¹⁸ / 3·10¹¹⁸** | finite, but the RLF-0 counterterms run over shapes of ≤ 5·10¹¹⁸ cubes |
| HIST n_♯ (h4, l.700) | ∝ 1/a_♯ | 5·10¹¹-4·10¹⁵ (joint, η_q linear); 4·10¹³-3·10¹⁷ (RS, η_1 quadratic) | **7·10¹²⁷-5·10¹³¹ (joint); 7·10²⁴⁵-5·10²⁴⁹ (RS)** | finite, g-indep.; SHADOW's box radius R_* ∝ n_♯ |
| RLF torus clause (RLARGE l.113-116; SF-last; SF B-5 halo caveat) | clusters ≤ n_* cubes must fit the level-k torus | O(1) final levels affected | ≈ log_L(n_*^{1/4}) ≈ **60 final levels** (n_♯: ≈ 130-260) | **conflict to record**: (SF-last)/torus caveat must cover these levels; "shapes up to translation" fails for wrapped clusters |
| HW a_bad = c_pr·min{ε_1², t_pr²} (l.203, 603) | c_pr = c_♭/C′² | min-branch quoted | ≈ 1.0·10⁻¹²³ (REG-min branch, ε_1 < t_pr); ≈ 10⁻¹³³ via (AE) | consistent (min); the "when ε_1 ≥ C′τ_♭" sub-case is now never active; HW's history slope again needs n·θa_badβ_- > 4 ⇒ n ≈ 10¹²⁴ |
| PLD (G0-1)(c) (l.1127-1128) | 10p_Lℓε_1 ≤ α_* | ok | ok | consistent |
| PLD (G0-1)(a) | (ε/g_0²)α_* ≤ λ_min/(2g_0²), λ_min ≈ 7·10⁻⁸² | 0.5·α_* ≫ λ_min: violated | 4·10⁻⁵⁹·2·10⁻³² ≪ 3.5·10⁻⁸² | consistent (helps) |
| PLD Prop. INH (l.1067) | ε_1 ∈ (0, 0.517] | ok | ok | consistent (scale-free) |
| PLD (SG^net)/(SG^fl) t-range (l.1144-1146) | t ≤ ε_1/(σ_fl²g²) | | a_fl(τ/2) ∝ τ²/σ_fl² ≈ 10⁻¹²⁸ | consistent; g-ceiling only |
| HIST MSG ε_M, RS-lin η_q (l.180) | upper bounds | | | consistent |
| FLOW (F_R), BFT_A/B | no ε_1 condition found | | | none |

**Global consequence (to record in O0 and in every lane's "g_0 small" clause).** The coupling ceiling g_* is the minimum of:
- the band window, g_0 ≲ 10⁻⁶⁶/N_r;
- the 't Hooft truncation, g_0 ≲ 4·10⁻⁵⁷;
- the large-field per-cube price e^{-a_♯/g²} against entropy, with a_♯ ≈ 10⁻²⁴³ on the RS route, so g ≲ 10⁻¹²²;
- DX′-1, g_0² ≲ 10⁻³⁰⁰ (estimate).

It is g-independent and K-independent, so UV stability stays well posed (uniform in a, at a physical scale where g = g_*). But the
lanes' quoted numerics at ε_1 = 0.5 (RLARGE C, HIST h4, HW a_bad, RLARGE l.1022) are now outside the admissible range. They should be
relabelled "illustrative, not admissible under (TH-ch)".

---

# PART F: s5 (MANDATORY NUMERIC LOCK)

- **Provenance (stat born times, EDT +4 h).**
  - s5_criteria.md: born = mod 06:16:32 UTC.
  - s5_sf.py: born 06:19:23, mod 06:21:07. The SF_LOG pre-run desk fixes were G_meas definition, C size cap and F2 print scope; none
    touches a criterion.
  - s5_out.txt: born 06:21:27, mod 06:21:43. s5_time.txt: 06:22:06.
  - §15 is recorded at 06:15:49 (SF_LOG l.189). I can verify it only as prior to the criteria by the log, not by mtime (SF.md was edited
    later).
  - **The criteria came before the script: yes.** The D3 FAIL is reported, not rescued.
- **Re-run.**
  - `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`: acquired at once, 06:44:54 UTC, load 3.46 (< 8).
  - OMP/OPENBLAS/MKL/VECLIB threads 1; nice 10; python3 without -I; no `timeout`; no trap.
  - s5: 15.6 s, peak RSS 111 MB, exit 0. Then indep.py in the same window, exit 0.
  - Exactly one `rmdir`, 06:45:10 UTC. pgrep is empty afterwards.
  - **rev_s5_out.txt is byte-identical to checks/s5_out.txt (diff empty): OVERALL FAIL 19/20 (D3).**
  - Record: revSF5/rev_lock.txt.
- **Evidential power.**
  - A1-A2 are real and A7 is a meaningful negative control.
  - B is d = 2 only. B1/B3 at Haar-random backgrounds support "every background".
  - C is real. E1/E2 are real (E3: the y⁴ term is never exercised).
  - D1-D2 are low (the contraction regime), and D3 failed for design reasons (B-7).
  - F is arithmetic, reproduced independently. F1/F2's 3^d hole counts are stale, as SF records (l.2072-2074).

---

# PART G: corrected tally and binding fixes

**Tally of SF.md after session 5 (reviewer-corrected):**
- **PROVEN-HERE 44 + 1 standard** (counted 10 unchanged; not counted 34).
  - MSG_0, W-Lip, GF-dec, BCH-L, FP-uniq, FP-sh, SLC-sh, KF, DX-rel: CONFIRMED.
  - CH-assign: CONFIRMED only as the set inclusion + the circularity argument (iii); its routing sentence is withdrawn by CH-1/CH-2.
- **CONDITIONAL 8:** SF's 7 (DX′ CONFIRMED ⇐ (FP-det) + (BGC)) + **(CH-c) ⇐ DX-rel + (DX-loc) + RLARGE E10 + the D-4 V-scope**.
- **ARGUED 3:** (CE-s); session-4 DX's a′ (superseded); (FP-det).
- **OPEN names:** SF's list + **RLARGE E10 now on lane F's path**. (FP-det) gains the cube-size condition FD-1.
- **"Discharged this session":** keep SLC-sh, (FP-loc)_0's uniqueness clause on the shrunk chart, (DX-rel), DX-1/DX-2/SC-1..3/D-1..D-3.
  **Remove "(CH-c) assigned".**
- 0 GAP. **1 WRONG sentence** (CH-assign's routing of [v2-E8] and the boundary family). No PROOF.md tally change. No RLARGE §4.2 row
  discharged.

**Binding fixes (next SF session):**
1. **CH-1:** at stage 0, every fine plaquette > τ_c (inter-cube included) and every mismatch > τ_c is priced by DX-rel + (DX-loc), never
   via RLARGE (D-c)/(D-b) → §3.4 → branches (ii)/(iii). Amend CH-assign (i), O4 and the RLARGE owner note. Add an RLARGE note for §3.4
   at stage 0.
2. **CH-2:** ∂Λ(𝔥)-adjacent defects are RLARGE (D-d)/E10, OPEN. e^{B_0} is a cost, not a price. (CH-c) inherits E10.
3. **CH-3:** state (SF)_0 on a V-event 𝒱^sf(Λ′) with a local ε_bg. The level-1 inter-cube roughness of V is RLARGE's, not (CH-c).
4. **TH-1:** (TH-ch) := ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg} (with ε_* ≤ τ_c and the κ_s kernel entry). Compute C_bg.
5. **DX′-1:** evaluate the g_0-ceiling of DX′ (with ||C|| ≤ 1/λ_min, m_sh, |Ω_B|, TILT's determinant) and of DX-rel's hole
   normalisation. Carry g_* to O0.
6. **DX′-2:** write the re-tuned (B1′)/GD-1 hypotheses with ρ_band (j_max, a_*^B ∝ ρ_band², the g_0-window).
7. **Status edits:** §17.1 (CH-c) row → CONDITIONAL. O0-O6 "non-circular" holds only after 1-3.
8. **Non-binding:**
   - FD-1 (m_FP·M/L ≥ κ_c + log G_∞ + O(1) in (FP-det));
   - FS-1 (truncation invisibility ⇐ band);
   - FS-2 (chart ⊋ E_good, stated once);
   - DR-1 ((DX-loc) factorisation is a decay statement);
   - the Chebyshev/Demko-Moss-Smith bound for G_res^{-1} (τ_c up by ≈ 10¹⁵);
   - D3 redesign;
   - cross-lane relabelling of the ε_1 = 0.5 numerics.

---

# PART H: strategic verdict

**Session 5 is a real advance.**
- The Gribov wall of session 4 is gone, by the reformulation REVIEW_SF_S4 recommended:
  - an exact, volume-independent, background-independent local gauge fixing on E_good;
  - a localised FP insertion, so far copies are irrelevant;
  - a contraction-based uniqueness clause;
  - an explicit exponentially local inverse of χ_UΓ.
- MSG_0 + GF-dec + FP-uniq/FP-sh are clean, elementary and checkable. Their only cost is numerical.
- What remains of (FP-loc)_0 on E_good is (FP-det) (a walk expansion, ARGUED).
- The deep part (DX′) and the hole pricing (DX-rel) are correctly relative, so DX-1 is cured.

**But the out-of-chart assignment is not closed.**
- CH-assign's own argument (iii) proves that (CH-c) must never touch branch (ii). Its routing of the inter-cube and boundary families
  then cites RLARGE pricings that touch branch (ii) (E8 via §3.4) or do not exist (E10).
- The repair is cheap for E8: DX-rel already prices it in-step.
- E10 is a genuine OPEN item that now sits on lane F's path.

**Strategic risk: constants, not logic.** Every threshold is ∝ G_∞^{-2}. That collapses ε_1 to ≲ 10⁻⁶² and the coupling ceiling to
≲ 10⁻¹⁵⁰ (estimate), and it inflates n_*/n_♯ to 10¹¹⁸-10²⁴⁵. This is mathematically harmless (g- and K-independent) but expensive
downstream: about 60 final levels fall under the torus caveat. The cheapest lever is G_∞:
- a Chebyshev-type decay bound for G_res^{-1};
- or a sharper ℓ^∞ inverse using s5 B6's measured 1-2 per block.

**Order of attack:**
1. CH-1..CH-3 and TH-1 (wording plus one DX-rel routing);
2. DX′-1/DX′-2 (evaluate g_*);
3. (FP-det) as a walk expansion with FD-1;
4. (DX-loc) under D-2, including the localised FP-uniq on Λ′ and the frozen-hole complement;
5. sharpen G_∞ before any other lane re-tunes to τ_c;
6. E10 with the RLARGE owner.
