# REVIEW_SF_S6: hostile review of lane F session 6 (SF.md [RSF5-fix] edits; §18-§20: Lemmas CD, CHEB, RINV, Proposition GF-A, Lemmas KKT, BOXG, Proposition GF-B (computer-assisted), Corollary CHAIN-6, Lemma FH, Corollary FP^𝔥, the (DX-loc) decomposition, (GF-dec)_k, threshold re-evaluation; check s6)

Reviewer: an independent agent that wrote none of SF.md. I edited no file except this one. No commits, PRs or pushes.

Inputs (read 2026-10-28 ≈07:30-07:55 UTC):
- SF.md l.2305-2589 (§18-§20) in full; the [RSF5-fix] spots l.1812-1830, 1910-1921, 2000-2015, 2040-2100, 2100-2230 (20 tags; 22 string
  hits, 2 of them in session-6 prose). SF_LOG.md session-6 block (l.242-311). REVIEW_SF_S5.md in full.
- checks/s6_criteria.md in full; s6_sf.py (514 lines) line by line; s6_out.txt, s6_time.txt.
- PROOF.md: 𝔠_∞ (l.5596-5606), Lemma BR1 (l.5661-5700), l.5859-5870 (R20-fix 8), Lemma CURV1 (l.5990-6012, l.6040-6052), header l.30-40.
- md5 now: SF 62079998… (= SF_LOG's final); s6_criteria 3964da2e…, s6_sf.py dd959a93…, s6_out 7e123ac5… (all = SF_LOG);
  PROOF 4a7bbccc…, RLARGE 24a73553…, HIST 468e9f03… (= SF's reads).

Scratch (scratchpad `revSF6/`): indep_cert.py (my own code; SF's script not imported or copied), indep_out.txt, indep_time.txt,
rev_s6_out.txt, rev_s6_time.txt, rev_lock.txt.

---

## Bottom line

- **RSF5 fixes: all binding fixes applied in place (20 tags) and correct.** The evaluated ceilings reproduce (F1 and my hand
  arithmetic): g_{DX′}² ≈ 1.49·10⁻²³⁷/(C_ΩN′²f⁸), hole ceiling 1.6·10⁻¹²⁶ (u_0 = 1/g_0², HIST l.873). Two non-binding notes below.
- **Lemma CD, CHEB, RINV, Proposition GF-A: CONFIRMED.** I re-derived every constant: c_D^K = 2663/31250 (exact LDLᵀ, own matrix),
  θ = m_FP^A = 0.146219/block, Γ_1 = 1.95145·10⁷, c_R = 330.659, **G^A = 6.47214·10⁹**. Background- and N-independent; frozen sets too.
- **Proposition GF-B (computer-assisted): CONFIRMED. Audit verdict: the certificate is valid, and I reproduced it independently
  with a stricter method.**
  - My version: own bordered operator, own torus inverse and relabelling. The residual E is computed **without BLAS**, as sequential
    sums of exact terms with the Higham bound. Every bound uses upward rounding (nextafter). The op-norm bound is min{Frobenius, Schur,
    Collatz-Wielandt}. The final formula is combined in exact rationals.
  - My result: **G^♯(0) ≤ 36.5473**, against SF's 37.0430 (so SF's number is a valid, slightly looser bound). The float value is 35.7303.
  - The uniform form at plaquettes ≤ 10⁻⁶ gives ≤ 38.37 (w = 1), against SF's 39.36.
  - e_1 = 3.33·10⁻³ and e_2 = 6.61·10⁻² agree with SF to 3 digits. The maximum residual entry bound is 9.265·10⁻⁷ in both.
  - The perturbation from U = 1 (KKT covariance + BOXG + the Δ count) is rigorous. It needs one explicit sentence (GB-1).
  - SF's "classical dgemm" caveat is no longer load-bearing, because my BLAS-free run gives a smaller bound.
- **CHAIN-6: CONFIRMED** (τ ∝ G^{-2}): τ^A = 3.60·10⁻³¹, τ^♯ = 1.10·10⁻¹⁴ (mine, at 36.55: 1.13·10⁻¹⁴).
- **The argument that τ_c = τ^A is the PROVEN admissible threshold is correct.** It holds because a single threshold is needed for both
  E_good and the frozen-hole charts. τ^♯ ⇐ (GF-B^𝔥) is correctly OPEN.
- **NEW BINDING DEFECT (TH-2): the ε_1 ceiling is NOT set by C_bg.** BR1 itself is valid only for ε_V ≤ ε_br. ε_br contains
  1/(24𝔠_∞²C_♭) = 1.04·10⁻⁷⁶/C_♭ (PROOF l.5663), so **ε_1 ≤ ε_br/(1.011√N) ≈ 5.9·10⁻⁷⁷/C_♭**, with C_♭ unevaluated (PROOF l.6052).
  - This binds below (TH-ch′)'s 1.50·10⁻⁷⁴ unless C_♭ ≲ 4·10⁻³.
  - It binds below the τ^♯ column's 4.59·10⁻⁵⁸ by ≥ 18 orders.
  - The τ^♯ column of §19.4 and "ε_1 ≤ 4.59·10⁻⁵⁸" are therefore not admissible.
  - (GF-B^𝔥) moves τ_c and the coupling ceilings, **not ε_1**.
  - At C_♭ = 1: n_* ≈ 2.7·10¹⁵⁴ and ≈ 81 final levels.
- **Priority 4: C_bg (and ε_br) are NOT intrinsic.** 𝔠_∞ ≈ 2·10³⁷ is the same species of bound as session 5's G_∞: it comes from a
  proven decay rate of ~10⁻¹⁰. PROOF's own R20-fix 8 (l.5864-5866) calls the 10⁴⁰ "constants" and records the measured ||C|| ≈ 25.
  - **Recommendation: a GF-B-type certificate for N_0(|C_0|)** of the level-0 operator at U^(0)(V). It is one certificate with three
    payoffs: 𝔠_∞, RW-ℓ²'s λ_min and the decay rate m_1. See Part D.
- **FH: CONFIRMED.**
- **FP^𝔥: CONFIRMED only in its [post-proof] two-step form.** The statement as written (l.2488-2491) is WRONG: the boundary links are
  not small. It must be restated (FP-1, binding). It covers fluctuation holes R(D) under global BR1 smallness, not the rough-V boundary
  ∂Λ′.
- **(DX-loc-2) ARGUED, (DX-loc-3) decoupling OPEN, (DX-loc-4) OPEN, (GF-dec)_k remark: statuses correct.**
- **s6: honest and reproduced.** The criteria (07:18:35) were written before the script (07:21:58). My re-run under the lock is
  **identical except the two timing strings: OVERALL PASS 17/17.**
- **Corrected tally: PROVEN-HERE 53 + 1 standard (+ CD as a PROVEN citation, not PROVEN-HERE) / CONDITIONAL 8 / ARGUED 4.**
  2 WRONG sentences (TH-2 in §19.2 l.2477 / §19.4 l.2537 / §20.2 l.2577; FP^𝔥's pre-correction statement).

---

# PART A: [RSF5-fix] edits (REVIEW_SF_S5 Part G numbering)

| # | SF line | verdict | note |
|---|---|---|---|
| 1 CH-1 | l.2159-2166, O4 l.2212-2217, owner note l.2225-2228 | CONFIRMED | every plaquette/mismatch > τ_c priced by DX-rel + (DX-loc); the circle is broken as recommended |
| 2 CH-2 | l.2168-2171 | CONFIRMED | E10 OPEN; e^{B_0} a cost |
| 3 CH-3 | l.1822-1827 | CONFIRMED | 𝒱^sf(Λ′), local ε_bg. **But BR1 is stated with the global ε_V (SF says so, l.2190), so U(V) on 𝒱^sf(Λ′) exists only through (DX-loc-4)** |
| 4 TH-1 | l.2179-2190 | CONFIRMED as far as it goes; **incomplete (TH-2, Part C-3)** | C_bg = 1.011√N·36p_L𝔠_∞ = 1.3869·10⁴⁰ reproduced. BR1's domain ε_V ≤ ε_br is missing from (TH-ch′) |
| 5 DX′-1 | l.2078-2091 | CONFIRMED | hand check: a_sh = 1.759·10⁻⁶⁴, R_sh = 1.61·10¹² (ln = 77.75 ⇒ f), m_sh = 1.327·10⁴⁸, |Ω_B| = 4.30·10⁵⁰, a′ = 6.42·10⁻¹⁸⁷ ⇒ 1.49·10⁻²³⁷ (N′²f⁸ scaling right) |
| 6 DX′-2 | l.2092-2097 | CONFIRMED | a_*^B = (ρ_band/(4√3N_r))² = 1.08·10⁻¹²³/N_r²; window 5.10·10⁻⁶⁷ |
| 7 status | l.2250-2252, 2271, 2282 | CONFIRMED | |
| 8 non-binding | FS-1/FS-2/FD-1 l.2043-2052; DR-1 l.2136-2140; tightness l.2003; D3 l.2011 | CONFIRMED | |

Non-binding notes:
- **A-1 (hole ceiling, l.2087-2089).** It uses a_p only. DX-rel prices each defect at min{a_p, a_c}, and a_c ≈ κ_sτ_c²/(4N) (KF) is below
  a_p for κ_s < 2. The ceiling scales ≈ linearly in a, so write min{a_p, a_c}. The u_0 normalisation is right: u_0 = 1/g_0² (HIST l.873).
- **A-2.** "C_K and the pattern entropy … lower it by O(1) factors in the exponent" is vague. Say "by an O(1) factor in u_0" (log terms).

---

# PART B: every-background tier (priority 2)

### B-1. Lemma CD (l.2329-2331; l.2386-2392): CONFIRMED (citation, re-certified)
- Kato: |Ad(U_b)λ(y) - λ(x)| ≥ ||λ(y)| - |λ(x)||. Drop the inter-block links to get the block-Neumann form with a Dirichlet point at
  the centre. The upper bound ||D_Uλ||² ≤ 2Σ_b(|λ(x)|² + |λ(y)|²) = 4d||λ||² ✓.
- **My exact check** (own 80×80 matrix):
  - H - (2663/31250)·1 has all Fraction pivots > 0 (min 1.1227·10⁻⁴);
  - at c = 0.08522 and at 0.0853 a pivot is ≤ 0;
  - λ_min = 0.0852175382.
- Status: it is a citation of PROOF FPq (i). It is **not** PROVEN-HERE, so it is removed from the 54 (Part F).

### B-2. Lemma CHEB (l.2332-2334; l.2394-2401): CONFIRMED
- p(x) = (1 - T_D(t(x))/T_D(σ))/x is a polynomial of degree D - 1, and p(G)(X, Y) = 0 at |X - Y| = D (block range 1; torus distance).
- sup_{[a,b]}|1/x - p| ≤ 1/(aT_D(σ)) ✓, and T_D(σ) = cosh Dθ ✓.
- On a torus, the shell count N_D = (2D + 1)^d - (2D - 1)^d is an upper bound (the torus embeds injectively in the ℓ^∞ box) ✓.

### B-3. Lemma RINV (l.2335-2338; l.2403-2411): CONFIRMED (the count re-derived)
- M_UR_U = 1 (single-link transports at c ± e_μ) ✓, and ||R(X, X)|| = L^d/√(2d) ✓.
- Values of D^*DR_Uη:
  - 2da at the 2d sites c + s (no other support neighbour);
  - ≤ 2a at the 2d(d - 1) sites c + s + s′ (s′ ≠ ±s);
  - a at c + 2s ∈ B(Y + s) (L = 3).
- So (Y, Y) ≤ a√(8d³ + 8d(d - 1)) and (Y + s, Y) ≤ L^d/(2d). Row and column sums are ≤ c_R = 330.6588 ✓.

### B-4. Proposition GF-A (l.2339-2344; l.2413-2419): CONFIRMED (re-derived)
- (χ_UΓ)^{-1}(η, ω) = R_Uη + G_res^{-1}(ω - P_resD^*DR_Uη): substitute λ = R_Uη + λ′, λ′ ∈ Λ_res ✓.
- Row sums: L^d/√(2d) + Γ_1c_R (η columns) + Γ_1 (ω columns) ✓.
- The entry bound uses the column sums of P_resD^*DR (≤ c_R, same count) and |X - Z| ≥ D - 1 ✓.
- My mpmath (summed to D = 700, explicit tail): σ = 1.010709036, θ = 0.14621886, Γ_1 = 1.95144690·10⁷, **G^A = 6.47214475·10⁹** ✓.
- s6 A4 printed "tail 0.0e+00": that is a float underflow of a ≈ 10⁻¹²⁵⁰ mpf, not a zero. Harmless.
- **Verdict:** "G_∞ ≤ 6.47·10⁹, m_FP^A = 0.146/block, every background, frozen holes too": TRUE.

---

# PART C: GF-B, CHAIN-6 and thresholds (priorities 3-4)

### C-1. Lemmas KKT (l.2345-2348; l.2423-2428) and BOXG (l.2349-2351; l.2430-2432): CONFIRMED
- **KKT injectivity.** ⟨λ, P_ΛD^*Dλ⟩ = ⟨M′λ, μ⟩ = 0 ⇒ λ = 0 (CD); then M′^Tμ = 0 ⇒ μ = 0 (σ_min ≥ L^{-d}).
- **KKT recovery.** P_resM′^T = 0 because ran M′^T = Λ ⊖ Λ_res.
- **KKT at U = 1.** The diagonal of D^*D is exactly 2d·1 for EVERY U (Ad orthogonal). The off-diagonal entries are -1, and M′_1 = Σ_y.
  So the entries are in {0, ±1, 2d} ✓.
- **KKT covariance.** D_{gU} = Ad_links(g)D_UAd_sites(g)^{-1} and M′_{gU} = Ad(g(c))M′_UAd(g)^{-1}. Λ is preserved by any site-wise Ad
  (g need not lie in 𝒢_V; this is an algebraic identity of linear maps) ✓.
- **BOXG.** The axial (comb) tree from c, and the ladder of Σ_{ν>μ}|x_ν - c_ν| ≤ (d - 1)h_B plaquettes inside the box ✓.
- **BOXG constants.** h_B = L(R_t + 1) + h = 19 and δ = 57ε ✓.

### C-2. Proposition GF-B proof (l.2434-2453): CONFIRMED, with one sentence to add (GB-1)
- **(1)** E is supported in |Z|_∞ ≤ R_t + 1, and n_T ≥ 2R_t + 3 = 13 makes the torus residual equal the ℤ⁴ residual ✓.
- **(2)-(3)** The column-wise gauge K̃_U(X, Y) = 𝔊_X^{(Y)-1}K̃(X - Y)𝔊_Y^{(Y)} is valid. Covariance gives the stated E_U.
  - Every Δ^{(Y)} entry used has both blocks inside the box (|Z - Y| ≤ R_t, |X - Y| ≤ R_t + 1; Δ(X, X) only for |X - Y| ≤ R_t).
  - Laplacian entries are -(Ad(gU_b) - 1), each ≤ 2δ, so each block is ≤ 4dδ by Schur, over 2d + 1 blocks ✓.
  - M′ entries are avg_σ(Ad(T^σ) - 1), each ≤ 2dhδ (≤ dh links per axial path, any ordering; M_U averages over orderings, SF l.1955).
    The row norm is ≤ 2dh√(L^d - 1)δ, and the same holds for -M′^T. Hence c_Δ(w) = (2d + 1)4d + 2dh√(L^d - 1)(1 + w) ✓
    (= 287.108 at w = 1).
- **(4)** 𝒦_U^{-1} = K̃_U - K̃_UW^{-1}(1 + F)^{-1}WE_U with F = WE_UW^{-1} ✓. |||·||| is the induced norm of ℓ^∞(blocks; ℓ²), so it is
  submultiplicative and the Neumann series converges ✓. Then |||P_λ𝒦_U^{-1}D|||_sp ≤ k_0 + k_1(e_2 + c_Δδk_4)/(1 - ε_W) ✓.
- **GB-1 (binding, one sentence).** The step |||WΔ^{(·)}K̃W^{-1}||| ≤ c_Δδk_3 sums over columns Y with a Y-DEPENDENT Δ^{(Y)}. It is valid
  because the entry bound b(X, Z) ≥ ||WΔ^{(Y)}(X, Z)|| is uniform in Y. That gives sup_XΣ_Y ≤ (sup_XΣ_Zb(X, Z))·(sup_ZΣ_Y||K̃(Z - Y)W^{-1}||).
  Write this; as printed, "|||WΔ^{(·)}|||" is not a defined object.
- **GB-2 (non-binding, wording, l.2463).** "Only a LOCAL plaquette bound is used (compatible with CH-3's V-scope)" overstates it.
  G_∞(U) is a sup over all blocks, so the hypothesis is needed on every box of the torus. On 𝒱^sf(Λ′) with rough V outside, GF-B does not
  apply as stated; that needs a boundary version, like (GF-B^𝔥).

### C-3. The computer-assisted proof: AUDIT
**What must be rigorous, and is.**
- K̃ is DEFINED as fixed floats at the 126 representatives, extended by the hyperoctahedral relabelling. Its accuracy is irrelevant to
  validity. Only (a) the exactness of its norms and (b) a rigorous enclosure of E = 𝒦^{sc}K̃ - 1 at all 28561 blocks matter.
- Norms of nonnegative entrywise upper bounds dominate the true block norms (Perron-Frobenius monotonicity). Frobenius and
  √||BᵀB||_∞ are valid op-norm bounds.
- Orbit sums are exact, because K̃(Z) is a row/column permutation of K̃(rep) and the bounds are permutation-invariant.

**s6's implementation (s6_sf.py l.271-331), line by line.**
- 𝒦^{sc} entries in {±1, 8} make every product exact. The γ_730 bound for any summation order is right for IEEE dgemm without
  Strassen. The (1 + g_E) factor covers the float evaluation of |𝒦||K̃|.
- The margins (1 + 4u), (1 + γ_{n+2}) and INFL = 1 + 10⁻⁹ are ad hoc but dominate every neglected second-order term, by ≥ 10⁶.
- One soft spot: the BLAS assumption. It is removed by my run below.

**My independent certificate (revSF6/indep_cert.py; criteria: reproduce G^♯(0) ≤ SF's 37.0430 and G^♯(0) ≥ the float estimate).**
- **Operator.** Rebuilt from the definitions in centred cell coordinates, with asserts: entries in {±1, 8}, and C_{-W} = C_W^T.
- **K̃.** My own torus-11 FFT inverse at the 126 representatives (imaginary part ≤ 2.3·10⁻¹⁷) and my own relabelling (agrees with direct
  FFT at 5 non-representative Z to 1.2·10⁻¹⁶). Orbit counts are by enumeration (sum = 11⁴).
- **E.** All 28561 blocks, no BLAS. Each entry is a sequential sum of its ≤ 10 exact terms (80 for the M′ row) plus -δ. The bound is
  |E| ≤ |fl| + γ_n·Σ|t|, with every operation rounded upward.
- **Op norms.** min{Frobenius, Schur √(r·c), Collatz-Wielandt √max(BᵀBx/x)}, all with upward rounding.
- **Sums and the final formula.** In exact rationals (√80 ≤ 8.9443).
- **Results:**

| | SF s6 B2 | reviewer (independent) |
|---|---|---|
| e_1 (w = 1000) | 3.3377·10⁻³ | 3.3255·10⁻³ |
| e_2 | 6.6078·10⁻² | 6.6066·10⁻² |
| k_0 / k_1 / k_3 / k_4 (w = 1000) | 36.826 / 3.2725 / 3.3078 / 37.578 | 36.361 / 2.8076 / 2.8388 / 37.109 |
| max residual entry bound / inner (|Z| ≤ 4) | 9.26·10⁻⁷ / 1.9·10⁻¹³ | 9.265·10⁻⁷ / 1.8·10⁻¹⁴ |
| **G^♯(0)** | **37.043038** | **36.547270** |
| G^♯(δ), plaquettes ≤ 10⁻⁶, w = 1 | 39.354 (hand) | 38.374 (ε_W = 0.050) |
| G^♯(δ) at ε = τ^♯/2 | 37.04304 | 36.5473 |
| float U = 1 value G_est | 35.730298 | 35.730298 |

- **Verdict: CONFIRMED.**
  - Both are rigorous upper bounds of the same quantity. Mine is tighter only through the Collatz-Wielandt bound.
  - The residual is truncation-dominated: rounding contributes ≤ 10⁻¹³, so the BLAS question is immaterial.
  - The perturbation to nearly flat backgrounds is rigorous (C-2), and B4's d = 2 end-to-end test (8.6896 ≤ 9.2278) is a meaningful
    test of the whole chain.
  - GF-B may be counted PROVEN-HERE (computer-assisted).

### C-4. Corollary CHAIN-6 (l.2465-2477): CONFIRMED
- G_∞ enters FP-uniq only through its defining inequality. The G-independent conditions ((S0), s_0 + 2r ≤ 0.3, …) are far from binding.
- Scaling check: 4.3386·10⁻⁵⁹·(5.8954·10²³/G)² gives 3.5998·10⁻³¹ (G^A) and 1.0989·10⁻¹⁴ (G^♯), both within 0.06% of s6 C.
- C1's self-consistency (ε = τ_c/2 ⇒ δ = 3.1·10⁻¹³, ε_W = 3.34·10⁻³) ✓.

### C-5. Thresholds: τ_c, (TH-ch′), and the new binding defect TH-2
- **τ_c = τ^A = 3.60·10⁻³¹ admissible everywhere: CONFIRMED.**
  - The argument at l.2501-2503 is right: one threshold must serve E_good and the frozen-hole charts.
  - Plaquettes in (τ^A, τ^♯] would be non-defects that break the hole charts (whose G is G^A).
- **1.10·10⁻¹⁴ ⇐ (GF-B^𝔥) OPEN: CONFIRMED.** D2's 0.03% shift at d = 2 is evidence only.
- **TH-2 (binding, NEW).** BR1 (PROOF l.5661-5668) holds only for ε_V ≤ ε ≤ ε_br, where
  ε_br = min{ε_*/(1 + 36p_L𝔠_∞), **1/(24𝔠_∞²C_♭)**, r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP)}.
  - With 𝔠_∞ = 2·10³⁷ the second entry is **1.04·10⁻⁷⁶/C_♭**.
  - The other entries are ≈ 2.5·10⁻⁷²/C_Δ, 2·10⁻³⁹r_♭, r_♭/144 and 3·10⁻⁴¹/K_FP.
  - C_♭ is not explicit in PROOF (l.6052, "What it is not: explicit (r_♭, S_♭, …)").
  - Via ε_V ≤ 1.011√Nε_1: **ε_1 ≤ 5.95·10⁻⁷⁷/C_♭**. This is absent from (TH-ch′) (l.2180), from O0 and from §19.4.
  - Consequences:
    - (a) At τ^A it binds unless C_♭ ≲ 4·10⁻³.
    - (b) The τ^♯ column of l.2475 and §19.4 (ε_1 = 4.59·10⁻⁵⁸) is inadmissible by ≥ 18 orders for any C_♭ ≳ 10⁻¹⁹.
    - (c) "The ε_1 ceiling is now set by C_bg" (l.2477) and "ε_1 ≤ 1.50·10⁻⁷⁴ (resp. 4.59·10⁻⁵⁸), set by C_bg" (l.2577) are WRONG.
    - (d) "The two remaining levers are C_bg … and (GF-B^𝔥)" (l.2537) is wrong for ε_1. Both ε_1 entries are 𝔠_∞-driven (∝ 𝔠_∞^{-1}
      and ∝ 𝔠_∞^{-2}). (GF-B^𝔥) moves only τ_c-driven quantities (ρ_band, the DX′/hole/FS-1 ceilings, the band window).
  - Fix:
    - (TH-ch″) := (TH-ch′) ∧ ε_1 ≤ ε_br/(1.011√N) (and ε_* ≤ τ_c as before);
    - carry C_♭ symbolically, or evaluate it;
    - recompute the ε_1-driven rows of §19.4. At C_♭ = 1: n_* (SU(2)) ≈ 2.7·10¹⁵⁴, ≈ 81 final levels, n_♯ (joint) ≈ 3.6·10¹⁶³-2.9·10¹⁶⁷
      [arithmetic].
- **Lemma CURV1 (PROOF [S21]) does not rescue this at current constants.**
  - It replaces BR1 (iii)'s linear factor by K_p(Z) + θ (≈ 2.27 plain rows).
  - But it keeps ε_θ ∋ ε_br and adds C_θ ∋ 288𝔠_∞³C_♭. So C_θε_V ≤ 1 needs ε_V ≲ 4·10⁻¹¹⁵/C_♭.
  - Both routes are throttled by 𝔠_∞.

---

# PART D: is BR1 (iii)'s constant intrinsic? (priority 4) — No. Recommendation.

**Diagnosis.**
- C_bg = 1.011√N·36p_L𝔠_∞, and ε_br ∝ 𝔠_∞^{-2}. 𝔠_∞ ≈ 2·10³⁷ (PROOF l.5604, l.5859) is a sup-norm covariance bound N_0(|C_0|) built
  from the proven decay rate (≈ 10⁻¹⁰, R_* ≈ 1.7·10¹²). That is exactly the mechanism that made session 5's G_∞ = 5.9·10²³.
- PROOF itself says so:
  - R20-fix 8 (l.5864-5866): "The 10⁴⁰ is constants (𝔠_∞ …)"; the triangle-inequality factor is "not shown to be intrinsic";
  - the measured ||C|| = 1/λ_min ≈ 25 (c35 C3, c36 D).
- So C_bg is a crude bound of the same type, and the GF-B technique transfers.

**Recommended certificate ((𝔠_∞-cert), suggested name).** Bound N_0(|C_0|) for C_0 = (Π_0O_0Π_0)^{-1} on ker h_0 at U^(0)(V), V near 1:
1. Write the constraint in bordered form, as in KKT: (O_0, h_0^T; h_0, 0). This makes the target space U-independent.
2. At V = 1, U^(0) = 1 (Lemma U0), and the operator is translation-invariant, scalar ⊗ 1_{su(N)}: the Wilson Hessian plus the
   soft-kernel Hessian, with κ_s ∈ [κ_-, κ_+]. Certify a finite-range inverse on a torus, with the residual enclosed exactly as in C-3.
   - The block has d·L^d = 324 link dofs, so it costs ≈ 64× GF-B, i.e. minutes.
   - Uniformity in κ_s: a κ-grid plus a κ-Lipschitz perturbation term, or κ as an interval parameter.
3. Perturb to V ≠ 1. U^(0)(V) has block-interior links exactly 1 and inter-block links V_c. In a coarse axial gauge on the R_t-box
   (Lemma AX / a BOXG analogue at level 1), every link is within O(R_tLε_V) of 1. The Δ count is as in GF-B.

**Expected payoff (order of magnitude; my estimate, not a derivation).**
- 𝔠_∞: 10³⁷ → 10¹-10³. Then:
  - C_bg → ≈ 10⁴-10⁶;
  - ε_br's entry → ≈ 10⁻⁶/C_♭;
  - CURV1's C_θ → polynomial size, so CURV1's linear constant (≈ 0.12 closed-input) becomes usable.
- ε_1 at τ^A → ≈ 10⁻³⁹-10⁻⁴⁰. At τ^♯ ⇐ (GF-B^𝔥) → ≈ 10⁻²³. The ε_1-driven constants fall by 70-100 orders in n_*.
- **The same certificate also gives:**
  - a certified λ_min(Õ) (DX′-1 uses RW-ℓ²'s 6.6·10⁻¹⁰, against a measured ≈ 0.04);
  - via CHEB, a decay rate ≈ 2√(λ_min/||Õ||)/r_1 ≈ 10⁻¹ in place of m_1 = 4.83·10⁻¹¹.
  - The latter shrinks R_sh, m_sh and |Ω_B| by ≈ 10⁹ each, i.e. g_{DX′}² gains ≈ 10⁷⁰. **The binding coupling ceiling is the same
    lever.**

**Order:** (𝔠_∞-cert) BEFORE (GF-B^𝔥).
- (GF-B^𝔥) alone moves τ_c but not ε_1 (TH-2).
- (𝔠_∞-cert) moves ε_1, C_bg, ε_br, CURV1 and DX′ at once.

---

# PART E: frozen holes and (DX-loc) (priority 5)

### E-1. Lemma FH (l.2370-2373; l.2481-2486): CONFIRMED
- Λ^𝔥 ⊂ Λ, so CD holds. The compression keeps block range 1 and the spectrum in [c_D^K, 4d].
- Λ_res^{U,𝔥} = ⊕_{X∉𝔥}Λ_{res,X} because M_U is block-diagonal. RINV's counts only drop.
- The links into frozen sites contribute |λ(x)|² to the quadratic form, which is consistent with the linearisation at g = 1 on 𝔥.
- s6 D1 reproduced.

### E-2. Corollary FP^𝔥 (l.2487-2500): the statement as written is WRONG; the [post-proof] two-step form is CONFIRMED
- **The original statement is wrong**, as SF found: with g = 1 on hole sites, (g_ax^∁·U_0)_b = g_ax(x)U_{0,b} on X → Y links is not small.
- **The corrected construction is right.**
  - The axial comb tree of B(Y) is a spanning tree, one link per non-centre site, so the fixing (gU_0)_b = U_b on it is exact:
    recursive unique solution, Haar-invariant, Jacobian 1.
  - The remaining integrand is 𝒢_V^𝔥-invariant.
  - g_ax = 1 on the fixed hole sites, because the same tree is used: hol_{U_0}(γ_x) = hol_U(γ_x).
  - On X → Y boundary links the base point is MSG_0's representative. Y is defect-free: if Y carried a plaquette or coarse-link defect,
    its neighbour X would be in 𝔥.
  - FP-uniq (5)'s propagation runs inside non-hole blocks only ✓.
- **FP-1 (binding, statement).** Replace the statement l.2488-2490 by the two-step form: (i) exact block-internal axial gauge on every
  hole block; (ii) FP-sh^𝔥 with 𝒢_V^𝔥 and (χ_UΓ)^𝔥. Delete "verbatim transposition" and "PROVEN-HERE" for the unrepaired text.
- **FP-2 (binding, scope).** FP^𝔥 covers the fluctuation holes R(D) when U(V) exists globally (BR1 with global ε_V). It does NOT cover
  the rough-V boundary ∂Λ′ of CH-3. There U(V) itself is defined only via (DX-loc-4).
  - So §20.1's "(DX-loc-1) PROVEN with G^A" must read "(DX-loc-1) for fluctuation holes, PROVEN with G^A; the ∂Λ′ part ⇐ (DX-loc-4)".
  - §18.2 l.2374's own decomposition included "the rough-V set" in (DX-loc-1).

### E-3. (DX-loc-2) ARGUED (l.2508-2512): CONFIRMED as ARGUED
- The lower bound needs criticality (BR1 (ii)) plus a second-order Taylor bound per link on |A_b| ≤ u_0^{-1/2}. That is plausible.
- The Jacobian between the reference's slice gauge and the hole's axial gauge is unwritten, as SF says.
- Nit: the ball's Haar volume is (c_Nu_0^{-(N²-1)/2})^{|R|}, not (c_Nu_0^{-1/2})^{(N²-1)|R|}.

### E-4. (DX-loc-3) and (DX-loc-4): CONFIRMED as named
- "Covariance part in hand" should read "CHEB applies (positivity + finite range r_1; rate not evaluated)". It is not a counted item.
- The decoupling of the reference across ∂R(D) is OPEN (DR-1). (DX-loc-4) is OPEN.

### E-5. (GF-dec)_k remark (l.2519-2520): CONFIRMED
- The inputs (a)-(c) are the right ones. (b) for the composite M^{(k)} is the open input.

---

# PART F: s6, tally, binding fixes

### F-1. s6 provenance and re-run
- **Birth times (stat, EDT +4 h):**
  - criteria 07:18:35;
  - script born 07:21:58, modified 07:23:48 (pre-run desk fixes; logged; none touches a criterion);
  - output 07:23:55-07:24:28;
  - time record 07:26:29.
- §18 at 07:16:13 can be verified only by the log (SF.md was edited later).
- **The criteria came before the script: yes.**
- **Re-run under the MANDATORY NUMERIC LOCK:**
  - `until mkdir …/locks/numeric` acquired at once at 07:43:09 UTC, load 4.68 (< 8), memory free 44% (≥ 35%);
  - OMP/OPENBLAS/MKL/VECLIB threads 1, nice 10, python3 without -I, no `timeout`, no trap.
- **s6_sf.py:** 31.5 s, peak RSS 772 MB, exit 0. **The output is identical to checks/s6_out.txt except the two timing strings (B2 "16.5 s",
  B4 "7.0 s") and the total time: OVERALL PASS 17/17.**
- **indep_cert.py:** 64.4 s, 447 MB, exit 0.
- Exactly one `rmdir`, at 07:45:10 UTC. pgrep is empty afterwards. Record: revSF6/rev_lock.txt.
- **Evidential power:**
  - A1 and B2 are proofs, and A1n is a real control.
  - A2/A3/B4/D1 are at d = 2. B4 is a genuine end-to-end test, and B4c shows that BOXG is load-bearing.
  - F1 is arithmetic.

### F-2. Corrected tally (SF claims 54 + 1 / 8 / 4)
- **PROVEN-HERE 53 + 1 standard:**
  - counted 10, unchanged;
  - not counted 43 = session 5's 34 + CHEB, RINV, GF-A, KKT, BOXG, GF-B (computer-assisted, CONFIRMED by an independent certificate),
    CHAIN-6, FH, FP^𝔥 (as corrected, FP-1/FP-2).
- **Lemma CD:** a PROVEN citation (PROOF FPq (i)), re-certified. It is not PROVEN-HERE.
- **CONDITIONAL 8:** unchanged. **ARGUED 4:** + (DX-loc-2).
- **OPEN names:** SF's list ((GF-B^𝔥) new). Plus the unevaluated C_♭ now in the ε_1 ceiling (TH-2), and (𝔠_∞-cert) recommended
  (not an OPEN item).
- **WRONG sentences, 2:**
  - (1) the C_bg-ceiling claims at l.2477, l.2537, l.2577 and the τ^♯ ε_1 column (TH-2);
  - (2) FP^𝔥's pre-correction statement l.2488-2491 (FP-1).
- 0 GAP. No PROOF.md tally change. No RLARGE §4.2 row discharged.

### F-3. Binding fixes (next SF session)
1. **TH-2:** (TH-ch″) := (TH-ch′) ∧ ε_1 ≤ ε_br/(1.011√N) (BR1's domain; 1/(24𝔠_∞²C_♭) entry ≈ 5.95·10⁻⁷⁷/C_♭).
   - Carry C_♭.
   - Recompute the ε_1-driven rows of §19.4.
   - Strike "set by C_bg" (l.2477, l.2577) and fix the "levers" sentence (l.2537): 𝔠_∞ drives ε_1; (GF-B^𝔥) drives only the τ_c rows.
2. **FP-1:** restate Corollary FP^𝔥 in the two-step form.
3. **FP-2:** scope (DX-loc-1) to fluctuation holes. The ∂Λ′ part goes to (DX-loc-4). Amend §20.1 and §20.2.
4. **GB-1:** write the Y-uniform entry bound behind |||WΔ^{(·)}K̃W^{-1}||| ≤ c_Δδk_3.
5. **Tally:** CD as a citation; 53 + 1.

**Non-binding:**
- A-1 (min{a_p, a_c} in the hole ceiling), A-2;
- GB-2 (the "LOCAL bound" wording);
- E-3 nit; E-4 wording;
- record the reviewer's G^♯(0) ≤ 36.547 as an independent confirmation (do not replace SF's number without SF's own check);
- "44 orders at locally small backgrounds" (l.2569) is not on the proven path; say "⇐ (GF-B^𝔥)".

---

# PART G: strategic verdict

**Session 6 is a real, correct advance on the constants front, and its headline survives a hostile, independent re-certification.**
- GF-A buys 28 orders unconditionally: G_∞ ≤ 6.47·10⁹ and rate 0.146 per block, for every background and frozen holes. It uses three
  elementary tools: a Kato gap, a Chebyshev decay lemma and a one-link right inverse.
- GF-B is a clean computer-assisted proof. The bordered integer form at U = 1 makes the enclosure easy, and the column-wise local axial
  gauge reduces nearly flat backgrounds to an O(δ) perturbation.
- I reproduced GF-B BLAS-free with directed rounding at 36.55 ≤ 37.04.
- FD-1 now holds from M ≥ 6·10⁴. The Gribov and locality structure of sessions 5-6 is sound.

**But the bottleneck has moved, and SF mislocated it.**
- ε_1 is pinned by BR1's own domain (1/(24𝔠_∞²C_♭)), not by C_bg and not by τ_c.
- 𝔠_∞ ≈ 2·10³⁷ is the same decay-rate-driven crude bound that GF-A/GF-B just removed from G_∞. The measured value is ≈ 25.
- So the strongest next move is **(𝔠_∞-cert): a GF-B-type certificate for the level-0 covariance at U^(0)(V)**. It also certifies
  λ_min(Õ) and a decay rate, and so attacks the binding coupling ceiling (DX′) at the same time.
- Only after it does (GF-B^𝔥) (a boundary-layer approximate inverse at frozen holes) pay for ε_1-driven quantities.
- Meanwhile (DX-loc-3)'s decoupling, (DX-loc-4) (a local BR1, which also carries CH-3's ∂Λ′) and RLARGE E10 remain the logical OPEN
  items on lane F's path.

**Order of attack:**
1. TH-2, FP-1, FP-2, GB-1 (wording plus one threshold);
2. (𝔠_∞-cert) with PROOF's BR1 owner;
3. (DX-loc-4);
4. (GF-B^𝔥);
5. (DX-loc-3) decoupling and E10.
