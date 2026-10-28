# REVIEW_FLOW_S8: hostile review of lane C session 8 (FLOW.md §57-§63 and the [RFL7-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f11*. This file is the only one I edited.
No commits, PRs or pushes.

Inputs (read-only, by offset):
- REVIEW_FLOW_S7.md (all).
- FLOW.md: l.240-247, l.849-856, l.1114-1124, l.1885-1944 (§37, COV-⊥-C, GS-2 (e)), l.2184-2423 (§44-§46: B-flux, G-mag,
  GH-log, MS, (L-loc2), N-f, COV-GI-∞, required values), l.2480-2488, l.2574-2606, l.2626-2645, l.2768-2790,
  §57-§63 (l.2803-3100) in full.
- FLOW_LOG.md l.300-350 (session 8).
- checks: f11_criteria.md (all), f11_scalar_vir.py (all of l.1-34 and l.100-379), f11_out.txt, f11_time.txt; f9_out.txt
  l.21-32 (G2).
  - BSD stat (UTC; local EDT +4 h): f11_criteria.md born 06:51:34 (4927 B); f11_scalar_vir.py born 06:53:32, modified
    06:54:55 (15775 B, md5 5f9beabc…, matches FLOW_LOG); f11_out.txt born 06:55:52, modified 07:02:17 (4064 B);
    f11_time.txt 07:02:17 (101 B). All agree with FLOW_LOG.
  - The §57 pre-statement md5 (FLOW_LOG l.316-318) cannot be re-verified, because FLOW.md has changed since. The ordering
    criteria → script → smoke → official run is confirmed by the stats.

Numerics (scratchpad `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow8/`):
- All runs: nice 10, all BLAS threads = 1, plain `python3` (no -I), no `timeout`, no trap, no process left running, nothing
  written to checks/.
- **Lock acquisition 1, 07:13:50-07:14:59 UTC, released once with `rmdir`.** Load 3.46. **Memory free was 33% at
  acquisition**, below the 35% floor. It had been 38% one minute earlier.
  - My independent quadrature (`indep_c0.py`, mpmath, no scipy) completed in under 1 s, 13 MB.
  - The f11 re-run had started. I **aborted it** (killed the python process) because memory was at 33-34%. The lock was
    then released once.
- **Lock acquisition 2, 07:15:27 UTC, released once with `rmdir`.** Load 2.42, memory free 36%.
  - `indep_ia.py` (I_a at 80 digits) ran in under 1 s.
  - The f11 re-run from a scratchpad copy: the only change is HERE pointed at checks/, to read f9_out.txt. **Identical to
    checks/f11_out.txt** (15/15), 379.9 s, peak RSS 706 MB. Released 07:21:47 UTC. See §5.4.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **[RFL7-fix] S7-1, S7-4, S7-5: all applied** (11 tags, as claimed). Leftover: the in-place "(vi) ARGUED/given (vi)"
  qualifiers in §44-§45 and l.856 are not annotated now that §58 proves (vi) (fix S8-6).
- **Theorem G-mag (vi): CONFIRMED.** I checked (a), (b1), (b2) and (c) line by line.
  - The exact one-coordinate formula (a) is correct, and so is the limit s/sinh s (Watson's U² spectrum, λ = 2s²).
  - Labelling: "one import" understates the external input. Also used are Skorokhod's representation, Lévy's continuity
    theorem, the functional CLT for a continuous-time Lévy process (not Donsker's i.i.d. theorem), and the K-L spectrum of the
    demeaned bridge. These are all textbook facts. The K-L spectrum has a one-line proof, which should be added (S8-1).
  - **Numerics:**
    - My mpmath quadrature reproduces κ_0, I_a, I_b and c'_0 = 1.385868559e-3 to every printed digit.
    - **Richardson extrapolation of f9's own sequence (model c'_0 + aφ + bφ²) gives 1.385871818e-3. That differs from c'_0 by
      3.3e-9 (cubic Richardson: 1.8e-9), ten times tighter than f11's 3.5e-8.** The 3.5e-8 is the error of f9's
      geometric extrapolation (ratio 0.509 rather than 1/2), not a defect of (vi).
- **Lemma VIR-eq and (Q1)(a): CONFIRMED**, with two wording fixes:
  - near t = 0 the Duhamel bound must carry a factor t (S8-2);
  - "A_0 absolute" should read "A_0 depending only on N and H_1".
  - The mass and proper-time forms are equivalent as claimed. 𝔠_α(ℓ²) = −(21q_α²/(48π²))log ℓ + O(q_α²) is checked.
- **(Q1)(c) (well-posedness): correct, but not a new item.** It restates COV-GI-∞ (l.2382-2386, which already defines c^⊥_n
  as total − ghost) together with GH-log (b), (c). I do not count it separately.
- **(Q1)(d): well posed for limit points**, and a single number given (L-loc2), since (vi) is now proven. It is the correct
  binding form of (V-IR), and it is OPEN as stated.
- **(R1), (R2), (R-damp): CONFIRMED in soft form** (C_R, c_W shown finite, not computed).
  - Two N ≥ 3 wording errors, neither load-bearing (S8-3):
    - the maximiser formula ψ_i = arg m_i − N^{-1}Σarg m_j is exact only when Σarg m_j = 0;
    - r_* and C_R depend on all diagonal fluxes h_iF_k, not on q_αF_k or φ_k alone.
  - (R-damp)'s n-uniform bound c_-κ^{-1}P_⊥ ≤ P_⊥𝒞_nP_⊥ ≤ c_+κ^{-1}P_⊥ holds in every root sector. GS-2 (e) has constant 1 for
    every m, so the per-step product is legitimate.
- **Lemma S-red: CONFIRMED.**
  - (i)-(iv) check exactly. My consistency test of (iv) against f11's own numbers matches to 4 digits at both n (§5.3).
  - The Harper-gap "standard" import in (ii) is unnecessary: on each finite flux-quantised fibre, a zero mode is
    covariantly constant, which is impossible at nontrivial plaquette holonomy (S8-4).
- **f11: CONFIRMED as an implementation and consistency check.** The S-VIR threshold is weak evidence (§5.2).
  - S-VIR is algebraically equivalent, by S-red (iii), to |ρ_2 − ρ_1| ≤ 0.25·2c_g log 3 = 5.8e-4. The observed value is
    1.46e-4.
  - With two levels and |ρ_n| ≈ 0.7 × the log step, it cannot tell bounded ρ_n from a slow log drift.
- **Lemma S-red's question "is sup|ρ_n| < ∞ provable from COV-⊥-C / R-damp?": NO.**
  - The proxy has no P_⊥, and 𝒞_n = C_n·1 is explicit.
  - More fundamentally, two-sided operator bounds do not control a second F-derivative.
  - A route is in §6.
- **Nielsen-Olesen: a real obstruction, but only to one proof device**: the finite-f determinant-lemma split with the
  *unregulated* fine H|_{ker D_0^*}.
  - It does not obstruct (V-IR) or the β extraction. β is the f² germ at f → 0 with n fixed, where |q_αf| ≤ q_αε_0ℓ^{-2}
    is dominated by the IR mass ~ sℓ^{-2}. By MS (iv) and F-id-exp, that germ equals a p² coefficient of the Hessian at
    U = 1, where every operator is nonnegative.
  - **Route: the vector S-red in two-point form at U = 1** (§7).
  - Analytic continuation to imaginary f does not help.
- **Corrected tally: 46 PROVEN-HERE (claimed 47).** The difference is (Q1)(c), which duplicates COV-GI-∞.

---

## 1. Priority 1: the [RFL7-fix] edits

11 tag occurrences at l.242, 1118, 2383, 2486, 2577, 2601, 2629, 2635, 2636, 2777, 2806, as claimed (l.3070).

| Fix | Where | Verdict |
|---|---|---|
| S7-1, Δ_FP ≠ FP_U^{-1}, Haar quotient | l.2636-2640 | APPLIED, verbatim in content. The stray-term estimate (+2c_gq²log ℓ, cancelling β[G_gh]) is stated. |
| S7-1, annotation at §5.1 | l.242-243 | APPLIED. |
| S7-1, annotation at the 𝔊 definition | l.1118-1120 | APPLIED (subscripted form; same content). |
| S7-1, stale "l.1100-1103" | l.2629, l.2635 | APPLIED. "l.1115-1121" is correct now (the 𝔊 bullet is l.1115-1121). |
| S7-4, truncation bound | l.2576-2580 | APPLIED. The weighted bound is the one asked for, with (1 + \|x\|)^k ≤ C_εe^{ε\|x\|}. |
| S7-4, uniformity on 𝒦_n | l.2601-2604 | APPLIED. |
| S7-5, COV-GI-∞ bold line | l.2383 | APPLIED in place. |
| S7-5, §48 pointer | l.2486-2487 | APPLIED. |
| S7-5, §55 minimal list | l.2777-2785 | APPLIED. The route-internal items are correctly moved under "means of proof". |

Leftover (fix S8-6). After §58, these sites still state (vi) as ARGUED or as a hypothesis:
- l.2206 ("(vi) ARGUED, not counted");
- l.2216-2220 (the ARGUED sketch);
- l.2247 and l.2252 ("given G-mag (vi)");
- l.2264, l.2286;
- l.2372 ("and G-mag (vi) for the existence");
- l.856 ("Proposition GH-log, given G-mag (vi)").

§58 says the qualifiers "drop" (l.2858, l.2937-2938), but none of these sites carries a pointer. Add
"[RFL8-fix: (vi) PROVEN-HERE, §58]" at each.

## 2. Priority 4: Theorem G-mag (vi) (§57 (Q3), §58)

### 2.1 Line by line

- **(a) (l.2895-2900): CORRECT.**
  - Under the 4D bridge the coordinates are independent 1D bridges, because the rate-1 Poisson clocks are independent and
    the endpoint conditioning factorises.
  - Given x, Campbell gives E exp(i∫(θx + ψ)dy) = exp(∫(2cos(θx + ψ) − 2)ds). There are a.s. no common jumps, so x_{s−} = x_s at
    the jumps of y.
  - 1{y_t = 0} = ∫dψ/2π e^{iψy_t}, and P(y_t = 0) = j_0(t).
  - I re-derived the formula and agree.
- **(b) scaling (l.2901-2905): CORRECT.**
  - With θ = s/t and ψ = η/√t, (θx_{tu} + ψ) = (sX(u) + η)/√t, and c_t = π^{1/2}/(2π√t j_0) → 1.
  - Φ(X) = exp(s²[(∫X)² − ∫X²]) by completing the square.
- **(b1) bridge invariance principle (l.2906-2917): CORRECT, compressed.**
  - The density ρ_t(z) = p_{δt}(z√t)/p_t(0) → δ^{-1/2}e^{−z²/(4δ)} uniformly, by the local CLT. That is the bridge/free
    density for variance 2.
  - Near u = 1, time reversal and the density bound ≤ p_{(1−δ)t}(0)/p_t(0) ≤ C, with Doob, give E sup|X^t|² ≤ 8Cδ.
  - The exponential-martingale tail is in fact e^{−ct^{1/4}}, stronger than the stated e^{−t^{1/8}}.
  - "(1)-(2) give fdd convergence and tightness" is the standard approximation step: convergence on [0, 1 − δ] in D, plus a
    uniformly small oscillation on [1 − δ, 1], then δ → 0 (Billingsley Thm 3.2). Add a citation or one sentence.
  - **Import labelling:** what is used is the functional CLT for a Lévy process in D[0, 1] (e.g. Jacod-Shiryaev VII.3, or
    Donsker on the integer skeleton plus control between integer times), not Donsker's i.i.d. theorem as such. The
    hypotheses are correctly identified (independent stationary increments, mean 0, variance 2).
- **(b2) the functional (l.2918-2927): CORRECT.**
  - Where |η| ≤ π√t − |s|t^{1/8}, we have |a| ≤ π and 1 − cos a ≥ 2a²/π². With Jensen, the η-integral bound is π^{3/2}/2. ✓
  - On the strip, cos a ≤ −½ for large t (a is within O(t^{−3/8}) of ±π). ✓
  - Φ_t ≤ 2π^{1/2}√t always, and √t·e^{−t^{1/8}} → 0. ✓
  - Skorokhod (D with J1 is Polish), then bounded convergence. ✓
  - The demeaned bridge U² = ∫(b − b̄)² has K-L eigenvalues 1/(4π²k²) with multiplicity 2. The trace check 1/12 is
    consistent but **does not prove the spectrum**.
  - One-line proof (S8-1): b − b̄ has covariance G(u − v) = 1/12 − |u − v|/2 + (u − v)²/2. That is the Green's function of
    −d²/du² on the circle, restricted to mean-zero functions, so its eigenfunctions are cos 2πku and sin 2πku with
    eigenvalue (2πk)^{-2}.
  - Then E e^{−λU²} = Π_k(1 + λ/(2π²k²))^{-1}, and at λ = 2s² this is s/sinh s. ✓
- **(c) (l.2928-2938): CORRECT.**
  - ψ = ½∫_0^Tm dt/t − I_2 + I_3, using 1 − cos x = x²/2 − h(x) and P·E_tA² = m (G-mag (iii)).
  - The I_2 integrand, after t = sT, is ((sT)²P(sT))s^{-3}E h(sA/t). It is dominated by C's on (0, 1] (h ≤ x⁴/24 and (iv)), and
    its limit is E h(s𝒜) = s²/6 − 1 + s/sinh s.
  - Uniform integrability of (A/t)² from (iv) licenses E h(sA/t) → E h(s𝒜). ✓
  - I_3 is dominated by 2Cs^{-3}. ✓
  - ½∫_0^Tm dt/t = c_g log T + ½κ_0 + O(1/T), since m − m_∞ = −m_∞/(4t) + O(t^{-2}) (I checked this with the Bessel series). ✓
- **Consequences (l.2937-2938): CORRECT.**
  - GH-log (a) gives c'(q_αℓ²f) − c'(q_αf) → 0, so (c) and (d) hold unconditionally.
  - COV-GI-∞'s root-sector group coefficients exist given (L-loc2).

### 2.2 Numerics

| quantity | f11 | reviewer (mpmath, own code) |
|---|---|---|
| κ_0 | 6.154034377778e-4 | 6.15403437777779e-4 |
| I_a | 9.242186397107e-3 | 9.24218639736478e-3 (80 digits; a 30-digit first attempt lost all digits to the s^{-3} cancellation and was discarded) |
| I_b | 0.1794994694614 | 0.179499469461363 |
| c'_0 | 1.385868559126e-3 | 1.38586855912469e-3 |

- **Richardson on f9's sequence (independent of the formula).** f9's c'(φ) at Q = 128, 256, 512 gives the following
  extrapolations:
  - linear: 1.385890589e-3;
  - quadratic: **1.385871818e-3** (−c'_0 = **3.3e-9**);
  - cubic (Q = 64-512): 1.385870394e-3 (1.8e-9).
- (c'(φ) − c'_0)/φ is monotone (1.109 … 1.286)e-4, with increments 7.7, 4.8, 2.7, 1.7, 0.8 e-6 that shrink by about 0.6 per
  halving. A residual δ/φ term would make the increments grow. The increments therefore bound |c'_0^true − c'_0| ≲ 2e-8, and
  Richardson brings this to a few e-9.
- **Verdict on G-c0:** the pre-stated 5e-6 threshold is loose, but not uninformative. A sign error on I_a would move c'_0 by
  1.2e-4, and one on ½κ_0 by 6e-4. **The actual agreement is about 3e-9 relative to 1.4e-3, i.e. 2e-6 relative.**

### 2.3 Verdict

**Theorem G-mag (vi): CONFIRMED (PROVEN-HERE).** Fix S8-1: list the standard facts used, and add the K-L one-liner and the
Billingsley sentence. The rate c'(φ) − c'_0 = O(φ) is not proved. FLOW says so (l.2943). Numerically the rate constant is
→ 1.29e-4.

## 3. Priority 3: (Q1), the operator-level (V-IR) and Lemma VIR-eq (§57 (Q1), §59)

- **(Q1)(a) (l.2948-2954): CORRECT.**
  - K_FD_0 = HD_0 + D_0Δ_0 = D_0Δ_0 at critical U_f. So K_F = H|_{ker D_0^*} ⊕ (Δ_0 on (ker D_0)^⊥), and θ_α = [f²]τ tr_{ker D_0^*}e^{−tH}.
  - With §46 and V-heat (ii): [f²]τ tr_C e^{−tK_F} = q²t²j_0⁴(R_12 + 2R_S).
  - G-mag (iii) gives [f²]τe^{−tΔ_0} = −m/2 = q²t²j_0⁴R_S (R_S = −ρ²/6). Subtracting gives (a).
  - The bound: R_12 + R_S = (1 + ρ)² − ρ²/2 + ρ/(2t) + 4γ(1 − ρ)/t, with ρ = I_1/I_0(2t) ≤ t. Hence θ_α = O(t) as t → 0 and bounded
    for all t. ✓
- **Lemma VIR-eq (l.2955-2967): CORRECT, two wording fixes (S8-2).**
  - (1) The gap is right. IMS gives K_F,f ≥ −C|f|^{2/3}; it is consistent with the true Nielsen-Olesen bottom −|q_αf|, and
    lossy, which is harmless.
  - (2) Existence: MS (ii)-(iii) for the gapped K_F + μ, Δ_f + μ. ✓
  - (3) The Combes-Thomas semigroup bound is right: the Hermitian part of e^{ηx}Ke^{−ηx} − K is O(η²) for finite-range K.
    **However, the stated derivative bound C_μ(1 + t)^{2j}e^{−μt/2} does not dominate near t = 0 against dt/t.** The Duhamel
    formula ∂_fe^{−tK} = −∫_0^te^{−(t−s)K}(∂_fK)e^{−sK}ds gives a factor t per derivative, so the bound should read
    C_μt(1 + t)^{2j}e^{−μt/2}.
    - The sentence "near t = 0 the integrand's f² part is O(t), see (a)" is a pointwise statement about the coefficient. It
      is not the uniform-in-f domination of the difference quotient that dominated convergence needs.
    - Fix: replace (1 + t)^{2j} by t(1 + t)^{2j} and cite the Duhamel factor.
  - (4) The comparison is right: |e^{−μt} − 1| ≤ μt on [0, 1/μ], plus E_1(1). But **A_0 = C_θ(1 + E_1(1)) depends on N (and
    H_1) through γ_α**, so it is not "absolute" (l.2820, l.2966).
  - (5) 𝔠_α(ℓ²): (7/2)q²/(16π²)·2log ℓ = (21q²/(48π²))log ℓ. ✓
- **(Q1)(c) (l.2968-2973): CORRECT given (L-loc2), and DUPLICATE.**
  - The torus action block-diagonalises everything into the Cartan and root sectors, so c^tot_{n,α} exists per sector.
  - G_⊥ := total − G_gh, and GH-log (b) gives the radius 2q²sup|c'|; with §58 the set is a point.
  - COV-GI-∞ (l.2380-2386) already defines c^⊥_n as the f² coefficient of total − G_gh. (Q1)(c) adds only the GH-log (b)
    radius, which is a one-line corollary. Keep it as a remark, not a counted item.
- **(Q1)(d) (l.2825-2830): well posed, and the right statement.**
  - It is stated for every limit point, against a comparator that exists (VIR-eq), with an n-uniform A.
  - It is now a single number given (L-loc2).
  - It matches §46's required value: c^⊥ + c^gh = −(21 + 1)q²/(48π²)log ℓ per root, i.e. β_0^std.
  - It does not mention the fine/level-n split, and it should not: (d) is the statement, and how it is proved is open.
  - It is consistent with the J_n^⊥ definition at l.849-853, whose bracket is exactly the IR-safe fine-plus-IR-term unit
    that 𝔪_α(ℓ^{-2}) models. **OPEN, as declared.**

## 4. Priority 2: (R1), (R2), (R-damp) (§57 (Q2), §59)

- **(R1) (l.2974-2984): CORRECT (soft).**
  - At B = 1: 𝔇_c = id on su(N), T_k(1) = Q_root, and R_k(1) = Q_root − Q_str + d∘h = 0 (LINEAR_PACKAGE §1.2).
  - For general B, in the Cartan gauge symmetric about c_X, every ingredient is analytic in the level-k fluxes on the
    finite support, with bounds uniform in c (magnetic translations) and in k (level units). Cartan gauge changes are
    phases, which leave entry moduli unchanged. So |R_k(c, b)| = O(F) entrywise, and Schur's test applies.
  - **Wording (S8-3):** for N ≥ 3, R_k depends on the diagonal fluxes h_iF (all i), not on q_αF alone. Restate as
    ||R_k(B)|| ≤ C_R|F|, with |F| := max_i|h_iF| and C_R depending on N.
  - The remainder is first order in F, unlike the Cartan sector (τd = 0 there). It is correctly flagged (l.3010-3011).
- **(R2) (l.2984-2996): CORRECT (soft), with an N ≥ 3 wording error.**
  - The straight-leg weight sum has modulus ≤ Q_str(c, b) (triangle inequality). ✓
  - SU(2): sums of SU(2) matrices are quaternionic, so M̄ = rW. det changes only at second order in root directions, so the
    root block of DW_♮ is r^{-1}, and r ≥ 1 − ½(q a_LF)². ✓
  - **N ≥ 3: "the maximiser … is V = diag(e^{iψ_i}), ψ_i = arg m_i − N^{-1}Σarg m_j" is exact only if Σarg m_j = 0** (Lagrange:
    r_isin(arg m_i − ψ_i) must be the same for every i). Since Σarg m_j = O(F³), the true maximiser differs by O(F³), and
    r'_i ≥ 1 − c_W F² still holds. Write "up to O(|Σarg m_j|)".
  - The second variation ½|y|²(r'_i + r'_j) and the unimodular linear couplings check. The root output is bounded by
    (|δM_ij| + |δM_ji|)/(r'_i + r'_j) ≤ (weight sum)/min r'. ✓
  - As with (R1), r_* depends on max_i|h_iF|. ✓
  - The product bound uses only the nonnegativity of Q_str and GS-2 (e) for the real field |v|. ✓
- **(R-damp) (l.2996-3003): CORRECT.**
  - Covariance gives P_⊥(B_{k+1})T_k = P_⊥(B_{k+1})T_kP_⊥(B_k), so P_⊥A_j factorises.
  - D^♭_{B'} = D_{B'}, so P_⊥(B_{k+1})D^♭ = 0 and P_⊥T_kP_⊥ = P_⊥(T^str + R)P_⊥.
  - GS-2 (e) (l.1895) holds with constant 1 for m = 1, so the per-step norm is ≤ r_*^{-1}L^{-1} + C_R|φ_k|.
  - Σ|φ_k| ≤ 2q_αε_0/(L² − 1), Σφ_k² ≤ 4q_α²ε_0²/(L⁴ − 1), and e_1 is as stated (2c_Wq²ε_0² over-bounds 8c_Wq²ε_0²/(L⁴ − 1)).
  - The 𝒞_n bounds have the same structure as COV-⊥-C (b) (l.1931-1936), with the root-sector π_± of §30. ✓
  - **With S8-3, read φ_k as max_i|h_iF_k| throughout.**
  - The Reading (l.3008-3010) is correctly modest: operator bounds, not an f² coefficient, and P_⊥(B_n) is non-local.
- **Verdict:** three items, CONFIRMED soft. They are honestly marked "constants not computed".

## 5. Priorities 5 and 6: Lemma S-red and f11

### 5.1 Lemma S-red (§57 (Q4), §60): CONFIRMED

- (i) Gap at f = 0: in each Bloch fibre, Δ_0φ = 0 ⇒ φ constant at θ = 0, and M_0 is nonzero on constants. IMS and MS give C². ✓
- (ii) The matrix determinant lemma per flux-quantised fibre, with ℓ^{-4} level sites per fine site. ✓
  - **"the 2D Harper operator at flux f ∉ 2πZ has a gap above 0; standard" is unnecessary (S8-4).** On each finite
    flux-quantised fibre, Δ_f(θ)ψ = 0 forces ψ covariantly constant, hence |ψ| constant with trivial plaquette holonomy, so
    ψ = 0. Each fibre matrix is therefore invertible, which is all (ii) uses.
- (iii) (G_S(f) − G_S(0))/f² = ψ(f) − ψ(ℓ²f) + (Y(f) − Y(0))/f². ✓
  - ℓ^{-4}(g(ℓ²f) − g(0)) = f²ψ(ℓ²f), and ψ(f) − ψ(ℓ²f) = 2c_g log ℓ + c'(f) − c'(ℓ²f) → 2c_g log ℓ by §58.
  - **Wording (S8-4):** the parenthetical "the level-n quantity log 𝒦_n + log Δ^{(n)}_F is IR safe" (l.2871) is stronger than
    what is proven, which is only that the F^{-2} quotient has a limit. Say "has an F² limit ρ_n".
- (iv) 𝔠^S(ℓ²) = 2c_g log ℓ + ½κ_0 − ½∫_{ℓ²}^∞(m − m_∞)dt/t, so c^S_n − 𝔠^S(ℓ²) = ρ_n − ½κ_0 + O(ℓ^{-2}). (V-IR-S) ⟺ sup|ρ_n| < ∞
  is then immediate. ✓

### 5.2 Is the 25% S-VIR threshold meaningful?

- By (iii), S-VIR is *identically* the statement |ρ_2 − ρ_1| ≤ 0.25·(2c_g log 3) = 5.80e-4. The observed ρ_2 − ρ_1 = −1.459e-4,
  i.e. 6.3%.
- **The test excludes:** a wrong IR scale, e.g. a cutoff at ℓ instead of ℓ² (ratio 0.5), or no IR saturation. That is
  useful.
- **It cannot discriminate (V-IR-S) from its failure.** A slow drift ρ_n ≈ ρ_∞ − δ log ℓ with δ up to about 0.25·2c_g would
  pass. The observed increment alone is equally compatible with ρ_n bounded with an O(ℓ^{-1}) or O(ℓ^{-2}) approach, and
  with δ ≈ 1.3e-4 per log 3 (6% of the coefficient).
- A meaningful n-uniformity test needs n = 3 with a pre-stated rate prediction:
  - bounded with an ℓ^{-2} approach: |ρ_3 − ρ_2| ≈ 1.6e-5;
  - ℓ^{-1} approach: about 4.9e-5;
  - log drift: about 1.46e-4.
  - Alternatively, compute ρ_∞ directly from the level-unit block-spin limit (§8).
- n = 3 in the f11 setting (magnetic Bloch, dense cells 9× larger per dimension) is out of budget. The two-point form at
  U = 1 (§6, §8) is momentum-diagonal and is the cheap route.
- **f11 does not overclaim** (l.3065-3066). It says "supports … two levels cannot show n-uniformity". The verdict line
  "PASS" should be read as "no S8-F2 at n ≤ 2", not as evidence of uniformity.

### 5.3 IR safety and internal consistency

- S-IR: the fitted f²log(1/f) coefficient of the total is 2.0e-8 and 3.0e-8, while the pieces give ±0.94 c_g and ±0.85 c_g on the
  same window and fit. So the fit can see a log, and the total has none.
  - This is an **implementation** confirmation of S-red (i), which proves C² at each n anyway. It is not independent
    evidence.
  - The pieces' 0.94 and 0.85 (not 1) are the finite-window values (Φ ∈ [0.2, 0.8]), as stated.
- S-stab: a1 agrees to 3e-7 relative between the four largest and four smallest fluxes, so the even polynomial model
  suffices. (The 1% threshold is loose.)
- **Reviewer consistency test (new).** S-red (iv) predicts that (c^S_n − 𝔠^S(ℓ²)) − (ρ_n − ½κ_0) = ½∫_{ℓ²}^∞(m − m_∞)dt/t. I computed
  the right side independently in mpmath:

  | ℓ² | f11, left side | reviewer, right side |
  |---|---|---|
  | 9 | −2.9527e-5 | −2.9527e-5 |
  | 81 | −3.2593e-6 | −3.2600e-6 |

  This ties f11's κ_0, 𝔠^S quadrature and ρ_n bookkeeping together, and it shows the O(ℓ^{-2}) term with the right sign and
  size (≈ −m_∞/(8ℓ²)).
- Part R: R1 tests the 2D reduction against a direct 4D torus with all 24 orders at **n = 1 only**. At n = 2 the reduction
  (two orders × a plain 34 average with alias weights |D_ℓ|²) is not directly tested. R4 tests C_n at n = 2.
  - The factorisation argument is exact: the axial phase depends only on whether 1 precedes 2, and the 34 legs carry no
    phase. So the risk is low, but name it as untested.

### 5.4 f11 re-run

- The re-run went in lock acquisition 2 (07:15:27-07:21:47 UTC; load 2.42, memory free 36%). It ran from a scratchpad copy
  whose only change is HERE → checks/.
- **The output is IDENTICAL to checks/f11_out.txt** apart from the start-time and timing lines: 15/15 verdict lines PASS,
  and both controls fail as required.
- 379.9 s, peak RSS 706 MB.
- The first attempt (in acquisition 1) was aborted at 33-34% memory, as recorded in the header.
- No process was left running, and checks/ has no `__pycache__`.

## 6. Priority 6: is sup_n|ρ_n| < ∞ provable from COV-⊥-C / R-damp?

**No, and FLOW does not claim it.**
- The scalar proxy has no gauge group, no P_⊥ and no transverse noise. 𝒞_n = C_n(f)·1 is explicit (COV-sc), so COV-⊥-C and
  R-damp do not even apply.
- More fundamentally, ρ_n is the F² coefficient (a second F-derivative) of τ_n log det(𝒦_nΔ^{(n)}_F). Two-sided operator
  bounds of the type c_- ≤ ℓ²𝒦_nΔ^{(n)} ≤ c_+ bound the log det, not its second derivative.

**Route (precise).**
1. Use F-id at U = 1, the scalar analogue of MS (iv) and F-id-exp. G_S,n is a gapped finite-range covariant density, so
   2c^S_n is the p² coefficient (12,12 component) of the Hessian kernel ĥ_n(p) of G_S,n at U = 1. In momentum space this is
   a one-loop vacuum polarisation with the U = 1 propagator (Δ + C^{-1}M^†M)^{-1}. By Woodbury,
   Δ^{-1} − Δ^{-1}M^†(C + MΔ^{-1}M^†)^{-1}MΔ^{-1}.
   - The vertices are the first and second derivatives of Δ_U, M_U (axial transporters) and C_n(U) at U = 1.
   - Everything is translation invariant on the level lattice, so there is no magnetic Bloch decomposition and no Harper
     spectrum.
2. Split this as the mass-regulated fine bubble, which gives 𝔠^S/𝔪^S, plus ρ_n. ρ_n is the p² coefficient of a level-unit
   kernel built from ℓ²Ĝ_n(k) := ℓ²MΔ^{-1}M^†(k) (alias sum over (Z/ℓ)⁴) and C_n.
3. The n-uniform input is the convergence in level units of ℓ²Ĝ_n(k) → Ĝ_∞(k) (the alias sum of the continuum block
   form factor; §60 Reading (2)), **together with its first two k-derivatives**, on compacta away from k ∈ 2πZ⁴. Near k = 0,
   Ĝ_n λ_n must be used in the Woodbury combination, which is bounded above and below.
   - In two-point form the C^{1,1}-at-0 issue (l.3036-3037) becomes an integrability question for the IR region of a loop
     integral. Second k-derivatives of λ_n/|k|² are bounded a.e. and the IR-safe combination has no 1/|k|⁴.
   - This is standard block-spin (Gawędzki-Kupiainen / Balaban) propagator technology, and gives ρ_n → ρ_∞ with an
     explicit rate.
4. The same scheme is the vector route (§7).

## 7. Priority 7: the Nielsen-Olesen obstruction (§60 Reading (3), §62 l.3082-3083)

### 7.1 What is true

- At U_f, H|_{ker D_0^*} has spectrum down to ≈ −|q_αf| (the spin-aligned lowest Landau band, with the 34 directions free):
  §45 Reading (2).
- In 4D the negative part of this band gives τ log H an imaginary part ∝ f². That is the lattice Nielsen-Olesen/Savvidy
  imaginary part. So "log det_{ker D_0^*}H has no real f-expansion" is correct.
- The S-red-type split det(H + M^TΠM) = det H·det Π·det(Π^{-1} + MH^{-1}M^T) at finite constant f therefore fails in the vector
  root sector:
  - with complex logs, the pieces are not individually real C² densities;
  - with log|det|, MH^{-1}M^T has a non-integrable singularity where the band crosses 0.
- **FLOW's diagnosis is correct.**

### 7.2 Does the RG need the constant-Cartan background for the vector root sector?

**No.** The constant-Cartan background is a computational device. It is needed for two things:
- the exact ghost scaling (GH-log: the same function g at two levels);
- the closed-form heat traces (V-heat, G-mag).

Neither requires a statement about H on ker D_0^* at finite f:

1. **β is a germ at f → 0 with n fixed, in the regime where the IR mass dominates the tachyon.**
   - β is extracted on |f| ≤ ε_n ≤ ε_0L^{-2n} = ε_0ℓ^{-2} (Lemma N-f, COV-GI-∞) and then f → 0.
   - The Nielsen-Olesen modes sit at −|q_αf| ≥ −q_αε_0ℓ^{-2}. The IR term gives Ã(U_f) ≥ c_n/2 > 0 (N-f), and the comparator
     K_F + ℓ^{-2} is gapped by Lemma VIR-eq (1).
   - **Yes, this is the regime used.** Both sides of (Q1)(d) are f² germs of gapped C² densities, and the tachyon never
     enters.
   - (N-f's window (c_n/2C'_n)^{3/2} is lossy, from IMS |f|^{2/3}, but any window suffices for a germ.)
2. **The germ can be computed at U = 1.** MS (iv) with F-id-exp says that 2 × the f² coefficient of a gapped covariant
   density equals H_0(𝓛Φ, 𝓛Φ), i.e. the p² coefficient of the Hessian kernel at **U = 1**. At U = 1:
   - H(1) = d^*d ≥ 0 per colour;
   - Ã(1) ≥ c_n (N-f (ii));
   - K_F(1) = d^*d + dd^* ≥ 0.
   No negative mode exists, and the second-order expansion never sees one.
3. **Analytic continuation in f (imaginary f): NO.** At imaginary f the links e^{−fx} are non-unitary, H loses Hermiticity
   and positivity, and nothing is gained. The total is already real-analytic in f near 0 (gapped), so continuation adds no
   information to it.
4. **Smooth localised background of small total flux: YES, but only as the same thing as (2).** At second order every smooth
   background probes the same Hessian kernel at U = 1. The cleanest is a plane-wave background a(x) = ε e_1 cos(p·x), with the
   ε² p² coefficient.

### 7.3 The route (vector S-red in two-point form)

- **(V1)** By MS (iv) and F-id-exp (given (L-loc2)), 2c^tot_{n,α} = the p² coefficient (12,12) of the Hessian at U = 1 of the
  root-α block of ½log det Ã − log det Δ' + ½log det 𝒞_n.
  - Subtract the ghost exactly (GH-log (c), now unconditional): c^⊥_{n,α} = c^tot_{n,α} + 2c_gq_α²log ℓ.
  - Do NOT apply F-id to G_⊥ or its level-n group separately. Their Hessian kernels are not exponentially decaying
    (P_⊥, massless Δ_0).
- **(V2)** Write the U = 1 Hessian as one-loop diagrams with the propagator Ã(1)^{-1}, Fourier diagonal on the level-n
  lattice. Decompose it by Woodbury about K̃ := H(1) + D E'D^*(1), as in S-red:
  Ã^{-1} = K̃^{-1} − K̃^{-1}M^T(𝒞_n + MK̃^{-1}M^T)^{-1}MK̃^{-1}.
  - **Check first:** whether K̃ has zero modes beyond k = 0 on the residual gauge directions Λ_res (E' excludes them). If it
    does, use K_F(1) + μ as the reference and carry μ.
- **(V3)** The fine bubble with K̃^{-1} → (K_F + ℓ^{-2})^{-1} has p² coefficient 2𝔪_α(ℓ^{-2}) (F-id for the gapped K_F + μ at
  U = 1, consistent with VIR-eq (b)).
  - The remainder ρ^V_n is the p² coefficient of an IR-safe level-unit kernel: the Woodbury term, the 𝒞_n vertex terms,
    the level-n ⊥ group via its U = 1 Hessian inside the total, and the mass difference.
  - **(V-IR) (Q1)(d) ⟺ sup_n|ρ^V_n| < ∞**, the vector analogue of S-red (iv). This is consistent with the J_n^⊥ definition
    (l.849-853), which is already a U = 1 one-loop integrand.
- **(V4)** The n-uniform bound needs §6 step 3 for the vector block-spin propagator, **plus the explicit first derivative
  of T_k(B) at B = 1** (the linear part of R_k). (R1)'s soft O(F) bound does not give it, and the 𝒞_n and M vertices at
  U = 1 need it.

**Verdict:** the Nielsen-Olesen obstruction is CORRECTLY identified, but it is an obstruction to the finite-f split only.
It does not block (V-IR). Edit §60 Reading (3) and §62 l.3082-3083 (S8-5) to add: "at finite constant f; at U = 1 (two-point
form via MS (iv) and F-id-exp) all operators are nonnegative and the split is available; see REVIEW_FLOW_S8 §7.3".

## 8. Per-item verdicts

| Item | Verdict | Fix |
|---|---|---|
| [RFL7-fix] S7-1, S7-4, S7-5 (11 tags) | **APPLIED** | S8-6 (the stale (vi) qualifiers at l.856, 2206, 2216, 2247, 2252, 2264, 2286, 2372) |
| (Q3) Theorem G-mag (vi) (§58) | **CONFIRMED**; numerics: quadrature reproduced exactly; Richardson on f9 3.3e-9 | S8-1 (import list; K-L one-liner; Billingsley step) |
| (Q1)(a) θ_α | **CONFIRMED** | — |
| (Q1)(b) Lemma VIR-eq | **CONFIRMED** | S8-2 (Duhamel factor t at t → 0, l.2963; "A_0 absolute" → depends on N, H_1, l.2820, l.2966) |
| (Q1)(c) well-posedness | **CORRECT given (L-loc2); duplicate of COV-GI-∞ + GH-log (b)** | not counted |
| (Q1)(d) (V-IR) binding form | **WELL POSED; the right statement; OPEN** | — |
| (R1) | **CONFIRMED (soft)** | S8-3 (flux = max_i\|h_iF\| for N ≥ 3) |
| (R2) | **CONFIRMED (soft)** | S8-3 (N ≥ 3 maximiser exact only up to O(Σarg m_j)) |
| (R-damp) | **CONFIRMED** (n-uniform; GS-2 (e) constant 1) | S8-3 (φ_k → max_i\|h_iF_k\|) |
| Lemma S-red (i)-(iv) | **CONFIRMED** (reviewer consistency test matches f11 to 4 digits) | S8-4 (Harper import unnecessary; "IR safe" parenthetical) |
| f11 G | **PASS**, and stronger than reported (3e-9 by Richardson) | — |
| f11 R, S | **CONFIRMED**; R1 at n = 1 only | — |
| f11 S-VIR (25%) | **PASS but weak**: ⟺ \|ρ_2 − ρ_1\| ≤ 5.8e-4; cannot test uniformity | next target |
| sup\|ρ_n\| from COV-⊥-C/R-damp | **NO** (not applicable; operator bounds ≠ second derivatives) | route §6 |
| Nielsen-Olesen obstruction | **CORRECT, but only for the finite-f split**; β needs no constant background for the vector sector | S8-5; route §7.3 |
| Procedure | Disclosed: smoke test 1 at 34% memory (floor 35%); two pre-run script edits; heading cosmetic edit after the stat | — |

**Corrected tally: 46 PROVEN-HERE (claimed 47)** = 40 + G-mag (vi) + VIR-eq (with (Q1)(a)) + (R1) + (R2) + (R-damp) + S-red.
- (Q1)(c) is a remark (a duplicate of COV-GI-∞ with GH-log (b)), not an item.
- **Scope annotations:**
  - G-mag (vi): textbook probabilistic facts used (S8-1).
  - (R1), (R2), (R-damp): soft (constants not computed); N-dependent via max_i|h_i|.
  - VIR-eq: A_0 depends on N.
  - S-red (iii): uses §58.
- **IMPORTED-AND-REVERIFIED:** L4b; the Lévy-process functional CLT (Donsker), hypotheses checked.
- **ARGUED, not counted:** (L-loc2). **OPEN:** (Q1)(d); (V-IR-S); (L-loc2) (proof); the UNIV-rate items; the rate
  c'(φ) − c'_0 = O(φ).

## 9. Binding fixes for the next lane-C session

1. **S8-1 (§58 imports).**
   - At l.2939, list the standard facts used: the functional CLT for Lévy processes (in place of "Donsker"), Skorokhod's
     representation, Lévy's continuity theorem, and the K-L spectrum of the demeaned bridge.
   - Prove the K-L spectrum in one line: covariance 1/12 − |u|/2 + u²/2 is the mean-zero circle Green's function of
     −d²/du², eigenvalues (2πk)^{-2}, multiplicity 2.
   - Add the Billingsley Thm 3.2 sentence at l.2917.
2. **S8-2 (VIR-eq).**
   - At l.2963, change the derivative bound to C_μt(1 + t)^{2j}e^{−μt/2} (Duhamel gives a factor t per derivative), and
     replace "near t = 0 the integrand's f² part is O(t)" by that uniform bound.
   - At l.2820 and l.2966, change "A_0 absolute" to "A_0 depending only on N and H_1".
3. **S8-3 (N ≥ 3 wording in (Q2)).**
   - At l.2841-2846 and l.2978-3001, read the flux in C_R, r_* and φ_k as max_i|h_iF_k|.
   - At l.2989-2990, write "the maximiser is V = diag(e^{iψ_i}) up to O(|Σ_jarg m_j|) = O(F³)".
4. **S8-4 (S-red).**
   - At l.3021-3022, replace the Harper-gap import with the fibrewise zero-mode argument.
   - At l.2871, change "IR safe" to "has an F² limit".
5. **S8-5 (Nielsen-Olesen scope).** Add the sentence of §7.3's verdict to §60 Reading (3) (l.3038-3041) and §62
   (l.3082-3083).
6. **S8-6 (stale (vi)).** Pointer "[RFL8-fix: (vi) PROVEN-HERE, §58]" at l.856, 2206, 2216, 2247, 2252, 2264, 2286, 2372.
7. **Tally (§63 l.3088-3090):** 46. (Q1)(c) becomes a remark.

## 10. Next target

1. **(V-IR-S) in two-point form at U = 1 (scalar, §6): check f12.**
   - Criteria first, then the script. Compute c^S_n as the p² coefficient of the U = 1 one-loop vacuum polarisation in
     momentum space (block-spin alias sums; heat-kernel factorisation per direction for the 1/λ alias sums).
   - **Pre-state:**
     - (a) reproduction of f11's c^S_1 = 7.12343e-4 and c^S_2 = 2.88549e-3 to ≤ 1e-8 absolute. This is an independent test
       of the F-id link in the proxy.
     - (b) ρ_3, ρ_4 (ℓ = 27, 81), with the discriminating prediction |ρ_3 − ρ_2| ≤ |ρ_2 − ρ_1|/3 = 4.9e-5 (bounded, approach at
       least as fast as ℓ^{-1}), against a log drift (≈ 1.46e-4).
     - (c) ρ_∞ from the level-unit continuum block-spin limit.
   - Jobs < 20 min and < 1 GB under the lock.
2. **Prove (V-IR-S)** by §6 step 3 (level-unit convergence of the block-spin Green's-function symbol with two k-derivatives,
   IR-safe Woodbury combination).
3. **State and prove the vector two-point reduction (V1)-(V3) of §7.3:** (V-IR) ⟺ sup_n|ρ^V_n| < ∞. First settle the
   Λ_res zero-mode question for K̃, and compute DT_k(1) (the linear part of R_k) explicitly.
4. **Prove (L-loc2)** (short; it closes COV-GI-∞, MS (iv), and with it (Q1)(c) and (V1)).
5. Wording fixes S8-1 to S8-6.
