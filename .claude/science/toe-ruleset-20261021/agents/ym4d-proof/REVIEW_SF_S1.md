# REVIEW_SF_S1: hostile review of lane F session 1 (SF.md: the small-field package (SF^J)_k / node A, lemmas A1-A4)

Reviewer: an independent agent that wrote none of SF.md. I edited no file except this one. No commits, PRs or pushes.

Inputs (read 2026-10-28 ~02:55-03:10 UTC):
- SF.md l.1-513 in full; SF_LOG.md in full.
- checks/s1_criteria.md, s1_sf.py (line by line), s1_out.txt, s1_out_firstrun.txt, s1_time.txt, s1_time_firstrun.txt, and the
  file birth/mod times (`stat -f %SB/%Sm`).
- RLARGE.md v2 l.49-80 ([v2-C], [v2-E8], χ_Q) and §4.2 table l.399-420 (rows 3, 3a, 4, 7, 8, 11, 16).
- PROOF.md: header l.1-60; Setting CE / Lemma CE-geo / Theorem CE l.1831-1912; Setting N5-bg l.5222-5240; Theorem RW
  l.5313-5322; Theorem N5-sf0 l.5382-5404; constants l.5436-5438; Lemma BR1 l.5628-5650; [S21] Proposition NAH-unif and the
  N5 node status l.6036-6099; l.701, l.3646, l.3811 (other uses of the same constants / exp chart).
- REVIEW_S20.md: bottom line l.21-78, (BG-unif) template l.316-345, verdicts/fixes/strategic verdict l.441-540. REVIEW_S21.md
  is a 1-line stub ("DRAFT (in progress; numbers pending)"), so there is no S21 review to defer to.
- HIST.md: l.880-920 (Lemma HF and the FLOW report), l.1185 ((F1)), l.1628-1736 (§25.4 Lemma NORM-an, §25.5 (a5-G), Theorem A5,
  §25.6 (I_k^E)''), l.1768-1778 (AE constants).
- FLOW.md l.120-135 (§3.1, log 𝒩'(P)); PLD.md l.1106-1130 ((SG^fl)_0); EXISTENCE.md l.2185-2196 (Proposition NA-3).
- md5 now: PROOF 490aaf34…, HIST 468e9f03…, FLOW 47bc2dff…, RLARGE 24a73553… (= SF's), REVIEW_S20 d7828b1f… (= SF's).
  **PROOF, HIST and FLOW changed after SF's 01:39 UTC read** (PROOF [S21] landed by ~01:59 UTC; HIST session 4 (§24-§29)
  pre-stated 01:52 UTC). Two of those changes bear directly on SF (items A1-2 and A2-5 below).

Scratch (lock-guarded runner, reviewer diagnostic, outputs): scratchpad `revSF1/` (run.sh, rev_diag.py, rev_s1_out.txt,
rev_diag_out.txt, rev_time.txt).

---

## Bottom line

- **Nothing counted is wrong.** The five counted items (SF-J, SF-T0, SF-DC, CE^+, SF-blk) are correct as proofs. SF-J needs
  a statement fix (the chart), SF-T0 a notation fix. The other three are CONFIRMED as written.
- **The "exponential chart covers full Haar only for N = 2" correction is right for the chart SF chose and wrong as a
  property of the exponential chart.** On D'_N := {A ∈ su(N): max_{a,b}|θ_a - θ_b| < 2π}, exp is injective, j > 0, and the
  image has full Haar measure for every N (the Weyl-alcove chart). The restriction of SF-A2^0 to the small-fluctuation set
  is therefore not forced by the chart. It is harmless, because the large-fluctuation set is priced separately anyway. No
  other file assumed full cover (searched).
- **The kernel-normalisation "source term" is real but overstated.** It is not "of order g_0p per coarse link". It is O(y_bg)
  times the fluctuation, where y_bg is the background's contour spread. It vanishes at flat backgrounds (consistent with
  EXISTENCE Proposition NA-3) and it is u-independent. **HIST §25.4 Lemma NORM-an (session 4, written after SF's read)
  already proves most of (SF-N)**: holomorphy, a g-uniform width, |𝔫_c| ≤ 2C_Nθ = O(y²). It does not change HF, F-tree or
  any tree-level or β-level statement.
- **SF-thr-k's chain is stale.** PROOF [S21] Proposition NAH-unif (PROVEN as an implication, unreviewed) now gives
  level-uniform N5-sf_j thresholds ⇐ (H-K) + (H-C). So "(N5-unif) ⇐[ARGUED] (BG-unif)" should be replaced by
  "(N5-unif) ⇐[implication, S21] (H-K) + (H-C)", with (H-C) the open part.
- **SF-thr and SF-thr-k conflate two fields.** N5's class is about the *background* (U(V), V). The cut χ_Q acts on the
  *integrated* field. SF-thr is a correct norm conversion. But "every cut-good plaquette satisfies the plaquette clause of
  N5-sf0 (a)" is a statement about the wrong field until it is chained through BR1 (iii) / CURV1 / NAH-unif. And the
  sentence "the soft clause |ρ_c| ≤ ε_N5 is not implied by any cut" is **false for the background**: BR1 (iii) and NAH-unif
  bound ρ(U(V), V) by the curvature of V. It is true only for the integrated field's soft fluctuation, which is the
  kernel-mismatch event.
- **(BG-loc) is not well-posed as written.** It has no boundary convention for terms straddling the frozen exterior, and
  "cone over Λ_k(𝔥)" is undefined in SF. It also duplicates the lane-F item HIST §25.5 (a5-G) (+ (a5-U)), which HIST has
  already stated precisely with the full-cone term set 𝒞^♭(Λ_k).
- **SF-V's central verdict is CONFIRMED, and it is stronger than SF says:**
  - Theorem CE as a black box needs a product measure on sites, so it can only be run in white-noise variables.
  - RW's s-weakened inverse K^{-1}(s; t) = P(1 - R(s))^{-1} is **not symmetric**, so there is no Gaussian measure μ_{C(s)}
    to decouple in A-variables. In the RW setting the white-noise representation is not a choice; it is forced.
  - Locality only in collar form (CE^+) is right at level 0.
  - The sup bound failing under μ_wn and holding after the per-site cut is right.
  - (V7)'s "the decay requirement sets M" applies only to the walk (𝒴-generated) activities of (CE-s). Strictly local
    activities satisfy CE's bound for every κ. V7 is an inference about (CE-s), not a property of the off-𝒴 expansion.
- **(OP-loc)_k: the failure is proven; the necessity is overstated.**
  - What is proven: SF-DC (b)-(d) fail for any K with one long-range entry (s1 A6, reproduced).
  - SF-DC (a) survives at any range. Columns outside 𝒴 still see only Ω_□' (reviewer R2), so l.139's "fails … even off 𝒴"
    is wrong.
  - The real defect is that every x depends on Z on all of 𝒴.
  - "Necessity" is a property of this route, not of the problem.
  - At k ≥ 1 the main-term *densities* are themselves only exponentially local (HIST Theorem A5 (C)). So (OP-loc) must cover
    the activities as well as the operator.
- **Corrected tally (this file): PROVEN-HERE 11 (counted 5: SF-J, SF-T0, SF-DC, CE^+, SF-blk; not counted 6) + 1 standard;
  CONDITIONAL 2; ARGUED 2; 0 GAP, 0 WRONG.** This is the tally SF claims, with the fixes below. No PROOF.md tally change: SF
  discharges no RLARGE §4.2 row.
- **s1: honestly recorded, and reproduced.**
  - The criteria file was born before the script (01:49:54 vs 01:51:02 UTC birth times).
  - The criteria md5 equals the logged cf928f42….
  - The run-1 reporting bug and its fix are disclosed.
  - E4's FAIL is recorded as a FAIL.
  - Re-run: byte-identical output (OVERALL FAIL, E4 only), lock 03:33:59-03:34:13 UTC, load 4.24, 44% free, 309 MB.
  - One defect of the check design: s1 never validates the RW implementation at s = 1. Reviewer R1 does.

---

# PART A: per-item verdicts

## A1 (background)

### A1-1. Lemma SF-thr (l.59-62, proof l.192-199): CONFIRMED-WITH-FIX (not counted)
- The proof is right:
  - |θ| = 2arcsin(|1 - e^{iθ}|/2), and the ratio is increasing with value 4arcsin(¼)/(½)·½ = 4arcsin(1/4) = 1.0107214 at x = ½.
  - The trace argument (|Σθ_j| ≤ 1.011Nε < 2π ⇒ Σθ_j = 0) is right.
  - The HS bound √N·max|θ| is right.
  - The [post-check] 1.0108 is a valid bound (R4).
- **Fix SF-thr-1 (l.61-62, "Consequently …"):** state what the consequence is: a *norm conversion* for whichever field is
  cut. N5-sf0 (a)'s plaquette clause is a clause on the **background** U of (U, V) (PROOF l.5398-5399). The cut χ_Q
  (RLARGE l.55) acts on the integrated field. The chain that puts the background in 𝔑(α_*) is:
  - cut on V = U_{k+1};
  - then SF-thr gives |log V_P|_HS ≤ 1.011√Nε_1;
  - then BR1 (iii) at level 0, or Lemma CURV1 / Proposition NAH-unif at level j, gives the curvature and the soft
    fluctuation of U(V) ≤ (K̄ + θ)η, (K̄_ρ + θ + C_θη)η;
  - then N5-sf0 (a).

  Write it this way.
- **Fix SF-thr-2:** χ_Q covers cube-interior plaquettes only (RLARGE l.55). The inter-cube plaquettes are handled by the
  EVENT of [v2-E8] (RLARGE l.75-79). "Every cut-good plaquette" must say so. RLARGE's [v2-C] also lists ε_loc, ε^J_loc;
  SF-thr-k treats ε_1 only.

### A1-2. Corollary SF-thr-k (l.63-66, l.201-207): CONDITIONAL, CONFIRMED-WITH-FIX (stale chain)
- The pre-stated "⇐ (BG-unif)" was correctly downgraded: REVIEW_S20 l.343 ("Then (I_i) holds … uniformly in i. That is
  exactly what NAH-ind needs") is a sentence without proof. **ARGUED was the right label at SF's read time.**
- **But PROOF [S21] Proposition NAH-unif (l.6036-6062; PROVEN as an implication, not counted, unreviewed) now proves the
  step that matters.** Under (H-K) (sup_iK_p^{(i)} < 1, K̄_ρ < ∞) and (H-C) (level-uniform constants), N5-sf_j holds at every
  level with thresholds ≥ ε_unif, independent of the depth. That is (N5-unif).
- **Fix SF-thr-k-1 (l.201-207, l.438 table row):** replace the chain by "(N5-unif) ⇐ [PROVEN implication, PROOF [S21] NAH-unif,
  unreviewed] (H-K) + (H-C); (H-K) measured with margin ≈ 10 at levels 0-1 (c37, not certified); (H-C) OPEN (Lemma E3's
  recursion compounds by ≈ 1.3·10³ per level); (BG-unif) (iv) via the composite contraction (REVIEW_S20 (R-b)) is the
  alternative route to (H-C)". Keep (BG-unif) ⇒ (N5-unif) as ARGUED only as the (R-b) route.
- **Fix SF-thr-k-2 (l.65-66, l.206-207): withdraw "the soft clause |ρ_c| ≤ ε_N5 is NOT implied by any cut".**
  - For the background (the object N5 is about) it IS implied by the curvature of V: BR1 (iii) |ρ_c(U(V), V)| ≤ 3p_Lr(ε)
    (PROOF l.5637) and NAH-unif's ρ ≤ (K̄_ρ + θ + C_θη)η.
  - Correct statement: "the integrated field's soft fluctuation ρ(U_k, U_{k+1}) is not controlled by any plaquette cut. It is
    the kernel-mismatch event (RLARGE §3.1). The background's ρ is controlled by V's curvature."

### A1-3. (BG-unif) (l.67-74): ACCEPTED as a hypothesis (with one transcription fix)
- **Fix BG-1 (l.70):** the template (REVIEW_S20 l.331-332) says "level-(k+1) soft fluctuations"; SF says "level-k soft
  fluctuations". The phrase "verbatim in substance" requires the template's wording, or a stated reason for changing it.
- **Note:** after [S21], (BG-unif) (iv) is the precise remaining content for the per-level route ((H-C) of NAH-unif), and
  (i)-(iii) follow from CURV1 + NAH-unif under (H-K). SF should record which clauses are now reduced.

### A1-4. (BG-loc) (l.75-79): NOT WELL-POSED as stated (OPEN name kept; statement to be repaired)
- "The tower defined on the cone over Λ_k(𝔥) with the exterior links frozen" does not say which terms of F_j are kept.
  - Terms straddling the frozen exterior involve large-field links, so conclusion (i) ("plaquette logs ≤ C_BGε") cannot hold
    for them.
  - The conclusions must be restricted to a collar-interior set, or the term set must be restricted.
- "Cone over Λ_k(𝔥)" is not defined in SF. The (BG-unif) slice ball's gauge slice also needs a boundary convention.
- "Dependence on the frozen exterior exponentially small" needs a form, e.g. |∂U_j(x)/∂W(e)| ≤ Ce^{-m_BGd_j(x, e)} for
  exterior links e.
- **Duplication:** HIST §25.5 (l.1660-1670), written after SF's read, assigns to lane F the precise item **(a5-G)**:
  - depth-uniform ℓ^∞ and weighted ℓ^∞ bounds on the slice Hessian inverse of the full-cone energy E^♭ at every ε_R-regular
    critical chain, plus surjectivity of the combined fixing map;
  - with (a5-U) + (a3-q), Theorem A5 (B) turns it into exactly a local tower with exponential locality, on the full-cone term
    set 𝒞^♭(Λ_k), which *is* a boundary convention.
- **Fix BG-loc-1:** restate (BG-loc) as "(a5-G) + (a5-U) [HIST §25.5] ⇒ (BG-loc)(i)-(iii) via Theorem A5 (B)". Check
  whether this is an implication or an identity of content. Retire the separate name if it is the same item.

## A2 (Gaussian + remainder)

### A2-1. Lemma SF-J (l.82-88, proof l.215-248): CONFIRMED-WITH-FIX (counted)
- Re-derived:
  - d exp_A = f(ad A) in the left trivialisation (Duhamel);
  - spec(ad A|_sl) = {λ_a - λ_b}_{a≠b} ∪ {0}^{N-1};
  - f(z)f(-z) = (2cosh z - 2)/z² = (sinh(z/2)/(z/2))²;
  - for anti-Hermitian A every factor is sin(μ/2)/(μ/2) > 0 when |μ| < 2π;
  - ℓ holomorphic on |z| < 2π, with spectral radius of ad A ≤ 2||A||_op;
  - the product-of-(1 + ζ_n) bounds (2/9)|w|², 1/135, 1/2160;
  - Σ_{a≠b}|z_ab|² = 2NΣ|λ|² (tr A = 0), Schur;
  - C_J = N/270 via Σ|z|⁴ ≤ 4||A||²_op·2N|A|²_HS.

  All right. s1 B1-B4 PASS (ratios 0.76, 0.39, 0.82).
- The (2) correction is correct for the chart D_N = {||A||_op < π}:
  - the SU(3) point (5π/6, 5π/6, π/3) has principal-log trace 2πi;
  - the trace is locally constant on the set where it is defined.
- **Fix SF-J-1 (l.218-226, l.467-468, l.289-290): the correction is chart-specific; do not state it as a property of "the
  exponential chart".**
  - Put D'_N := {A ∈ su(N): max_{a,b}|θ_a - θ_b| < 2π} (θ the eigen-angles).
  - (1) Every U ∈ SU(N) with N distinct eigenvalues (a Haar-full set) has exactly one traceless logarithm with spread
    < 2π. *Proof sketch:*
    - Lift the angles into a window [c, c + 2π). Every spread-< 2π choice arises this way with c = its minimum.
    - The angle sum is a step function of c that rises by 2π at each (simple) eigen-angle and runs through N + 1
      consecutive multiples of 2π per period. So the value 0 is taken on exactly one window, i.e. by one set of angles.
    - With repeated eigenvalues the step can be 4π and 0 may be skipped (e.g. diag(-1, -1, 1)); that set is Haar-null.
  - (2) Hence exp: D'_N → SU(N) is injective with image of full Haar measure.
  - (3) j > 0 on D'_N (all |θ_a - θ_b| < 2π), and log j is holomorphic there (spectral radius of ad A < 2π).
  - So the chart identity ∫f dU = c_N∫_{D'_N}f(e^AU_0)j(A)dA holds for **every** f ∈ L¹ and every N. This is the Weyl
    integration formula in exponential coordinates [STANDARD; the injectivity step above is elementary and should be written
    if used].
  - Reviewer R3 measures the coverage. The fraction of Haar SU(N) in E_N = exp(D_N) is 1.0000 (SU(2)), 0.9753 (SU(3)), 0.9476 (SU(4)) (4·10⁴ Haar samples each). The fraction with a
    traceless log of spread < 2π is 1.0000 for N = 2, 3, 4.
- **Consequence:** SF-A2^0's "[post-proof correction 01:52 UTC] F supported in the small-fluctuation set" is not forced by
  the chart. It is still the right domain for the *bounds*: SF-J (5)-(6) need ||A||_op ≤ π/2, and SF-T0 needs ρ ≤ r_T/8. The
  complement is priced as a fluctuation large field either way, so no conclusion of SF changes. The statement in §4.2 should
  read: "the chart D_N covers only a proper subset for N ≥ 3; D'_N covers full measure; SF uses D_N because its bounds live
  there".
- **Fix SF-J-2 (l.33-34 vs l.87):** the constants are for the Frobenius norm |A|²_F = -tr A². §0 allows "⟨A, B⟩ = -2tr AB or
  any fixed Euclidean structure". Under -2tr AB, |A|² = 2|A|²_F, so N/9 → N/18 and N/270 → N/1080, and the white-noise
  normalisation of SF-WN changes by √2. Fix one structure.

### A2-2. Lemma SF-cut (l.89-93, l.250-253): CONFIRMED (not counted)
- (a) is the expansion of Π(χ + (1 - χ)). (b) is Chernoff with E e^{|Z|²/4} = 2^{n/2}. (c) is right. s1 C1 PASS (max ratio
  0.164).
- Note (not a fix): (a) for "bounded measurable F". The application has F = exp(…) unbounded on Q-sites; integrable F
  suffices (finite torus, Gaussian tails). Say "F ∈ L¹(μ)".

### A2-3. Lemma SF-T0 (l.94-101, l.255-278): CONFIRMED (existence of constants; counted)
- (1) analyticity per term type is right: finitely many types, the plaquette term entire, the kernel term analytic via
  NA-alg (a)'s analytic implicit function.
- (2)-(3) right: the HS submultiplicativity gives |log(e^Xe^Y)| ≤ 2(|X| + |Y|) for |X| + |Y| ≤ ¼; Ad-invariance of |A_b|.
- (4) the Cauchy remainder is 2S_T(4ρ/r_T)³ ≤ the pre-stated 16S_T(4ρ/r_T)³.
- (5) checked against BR1 (ii) (PROOF l.5636): "U(V) is a critical point of F(·, V) (no fixing term)". The "Lagrange
  multipliers" in SF l.275 are BR1's proof device, not a constrained criticality, so Σ_τDτ(U(V))·A = 0 in every direction.
  CONFIRMED.
- **Fix SF-T0-1 (l.274):** "F := S_W + κ_0Σ_cφ̂_c" uses κ_0 for the kernel strength (Setting N5-bg's κ_0 ∈ [κ_-, κ_+]). SF §0
  l.31 uses κ_0 = 16 log 12800 (CE). Rename one of them (e.g. κ_k for the kernel) throughout SF.

### A2-4. Lemma SF-N0 (l.105-106, l.280-283): CONFIRMED (not counted)
W_0(aMb⁻¹) = aW_0(M)b⁻¹ and φ_{aMb⁻¹}(V) = φ_M(a⁻¹Vb) are both right, and Haar invariance gives n_c(aMb⁻¹) = n_c(M).

### A2-5. (SF-N) (l.102-104): LARGELY DISCHARGED by HIST §25.4 Lemma NORM-an (PROVEN-HERE [S4-D], counted in HIST; unreviewed)
- NORM-an (HIST l.1628-1649) proves the following, on the domain D_c(y_0) of TERM-an (iii), uniformly in u ≥ 1/(2κ):
  - log𝒩^ℂ_c = log𝒩_0 + 𝔫_c, with 𝒩_0 := ∫e^{-κu·s(V)}dV a c-number;
  - 𝔫_c is holomorphic, with |𝔫_c| ≤ 2C_Nθ, θ = 18.4y²(2 + 2c_N).
- That is (SF-N)'s "holomorphic, bounded uniformly in u_0 on a g-independent neighbourhood". SF's u_0-subtraction
  (N² - 1)/2·log(κu_0/2π) differs from log𝒩_0 by a u-uniform c-number (Laplace on 𝒩_0 alone), so the forms agree.
- What NORM-an does not give is the expansion ν = ν_0(M) + O(1/u_0). That clause is not used anywhere in SF.
- **Fix SF-N-1 (l.102-104, l.445, l.474, l.490):** re-base (SF-N) on NORM-an. Keep only (i) the domain match (NORM-an's
  D_c(y_0), contour spreads y ≤ y_0 in MSG gauges, against SF-T0's gauge-log polydisc |log(gU)_b| ≤ r_T/4) and (ii) the
  1/u_0 expansion if it is ever needed. Status: CONDITIONAL on the domain match (s).

### A2-6. Proposition SF-A2^0 (l.112-117, l.285-305): CONDITIONAL, CONFIRMED-WITH-FIX
- **√N correction: CONFIRMED.**
  - The stage-0 exponent is u_0Σ_ps + κu_0Σφ = (u_0/N)(S_W + κΣφ̂), with S_W = NΣs and φ̂ = Nφ (Setting N5-bg, PROOF l.5227).
  - So the Gaussian is e^{-(u_0/2N)⟨A, OA⟩}, the covariance is (N/u_0)C = Ng_0²C, and A = g_0√N𝒞Z.
  - Then |u_0V_τ| ≤ 128S_TN^{3/2}N_0³p³g_0/r_T³ and |log j| ≤ (N²/9)g_0²N_0²p². The arithmetic is right.
- **Fix SF-A2-1 (l.300-302): the source term is O(y_bg·g_0√NN_0(|𝒞|)p) per coarse link, not "of order g_0p".**
  - Reason:
    - n_c depends on M only through its bi-invariant class (SF-N0).
    - By NORM-an, log n_c = c-number + 𝔫_c with |𝔫_c| = O(y²) holomorphic in the contour variables.
    - A function that is O(y²) on a polydisc about the flat set has gradient O(y_bg) at a point of spread y_bg (Cauchy on a
      disc of radius ≍ y_bg).
  - At a flat background (y_bg = 0) the linear term vanishes. This agrees with EXISTENCE Proposition NA-3 (flat background:
    no additive drift, every N).
  - Reviewer R5 (SU(2), two-path contour average): d|M̄|/dt(0) = 5.6·10⁻¹¹ (zero, numerical) at spread 0 and −0.144·spread at spreads 0.01-0.08 (exactly linear in the spread).
  - So the statement "a source term the cluster expansion must carry" stays true. Its size is the background spread times
    the fluctuation size, with no u_0 enhancement.
- **Fix SF-A2-2 (l.293):** "(SF-WN, with C/u_0·N the covariance)" should read "covariance Ng_0²C = (N/u_0)C".
- **Fix SF-A2-3 (status, l.285, l.448):** after A2-5, SF-A2^0 is CONDITIONAL ⇐ (FP-loc)_0 + (domain match with NORM-an).

### A2-7. (FP-loc)_k, (N5-reg)_k (l.107-111): ACCEPTED as named items
- (N5-reg)_k is a fair new name: N5-sf0 (b) is stated for (U, V) ∈ 𝔑(α_*) globally.
- HIST (a5-G) is the main-term analogue. Cross-reference it.

## A3 (cluster expansion)

### A3-1. Lemma SF-WN (l.120-123, l.309-315): CONFIRMED (not counted)
- 𝒞 = Π_UÕ^{-1/2}Π_U is symmetric, and 𝒞² = C. The image law is the slice Gaussian. μ_wn is a product.
- One addition that strengthens SF-V (V1): for s ≠ 1, 𝒞^Π(s) is not symmetric (next item). So the white-noise
  representation is the only way to give the s-weakened field a law.

### A3-2. Lemma SF-DC (l.124-134, l.317-338): CONFIRMED (counted)
- Re-derived:
  - (K + t)P = 1 - R, so (K + t)^{-1} = P(1 - R)^{-1};
  - R_□ = R_□1_□;
  - the support propagation G_□ → Ω_□, then K → +r_K, then 1_{Ω_□^c};
  - the component induction;
  - (c) by entrywise integration of t^{-1/2}K^{-1}(s; t) (integrable at 0 and ∞);
  - (d) boxes of side < 2R blocks (RW Setting, PROOF l.5315), so distances ≤ R + 2R - 2 < 3R;
  - the M-cube consequence, because blocks at distance ≤ 3R - 1 have fine distance ≤ 3RL - 1 < M.
- s1 A1-A5 PASS (exact 0.0), A3 non-vacuous (6.3·10⁻⁴).
- **Check-design defect (s1, not SF-DC):** s1's `kinv_s` is never compared with (K + t)^{-1} at s ≡ 1. Its zero pattern is
  structural, so A1/A2/A5 would also pass for a wrong (but equally structured) formula.
  - Reviewer R1 builds K^{-1}(1; t) by an independent plain Neumann series (no Woodbury) and compares it with (K + t)^{-1}:
    max relative error 2.4·10⁻¹⁵ at t = 0, 1, 7 (PASS).
  - R2 reproduces (a)-(b) with that independent code: (a) and (b) exact 0.0 for finite-range K.
- Note: K^{-1}(s; t) is not symmetric (P is not), so 𝒞^Π(s) is a linear map, not a covariance square root. SF uses it only
  as Z ↦ A. Correct, and worth stating.

### A3-3. (OP-loc)_k (l.135-139, l.341-344): OPEN name ACCEPTED; necessity claim NARROWED
- **What is proven:** with one long-range entry K(x, z), z ∈ Ω_□, □ ∈ 𝒴, the 𝒴-columns reach outside Ω(𝒴^+). So SF-DC
  (b)-(d) fail. s1 A6 PASS (9.1·10⁻⁶) and reviewer R2.
- **Fix OP-1 (l.139 "fails at k ≥ 1 even off 𝒴"): withdraw.** SF-DC (a) uses only R(s)1_{□'} = 0 for □' ∉ 𝒴, which holds at
  any range of K, and G_{□'} is the compressed inverse on Ω_{□'}. The off-𝒴 columns stay local (R2: off-Ω entry exactly 0.0
  with the long-range entry present).
  - The real failure: D(x) ⊃ every 𝒴-component for every x. Every activity then depends on Z on 𝒴, at exponentially small
    but non-zero strength.
  - That is a statement about (CE-s)'s polymer connectivity, not about the off-𝒴 collar locality.
- **Fix OP-2 ("necessity PROVEN-HERE"):** the proven statement is "SF-DC's support propagation needs finite range". It does
  not show that a cluster expansion at k ≥ 1 needs (OP-loc). Theorem RW itself needs only exponential decay ((RW2):
  N_m(|K|) ≤ S_m), and the standard alternative is a second interpolation of K's long-range part (Balaban's localisation).
  That is (OP-loc)'s own first alternative, so the name is right but "necessity" should say "of this route".
- **Fix OP-3 (scope):** at k ≥ 1 the main-term densities are only exponentially local (HIST Theorem A5 (C):
  |∂𝓔^{an}_{k,x}/∂Z(b')| ≤ Ce^{-κ_5d(x, b')}). So SF-T0's level-k analogue fails in the same way. (OP-loc)_k must cover the
  activities (a localisation expansion of the main term) as well as Õ_k.

### A3-4. Lemma SF-geo (l.140-141, l.346-354): CONFIRMED (not counted)
- The vertex property (closed cubes that meet share a vertex of Q) is right, and so is the segment p_Q → v_Q of length ≤ 2
  inside Q.
- The Gray Hamiltonian path of 15 edges inside Q is right. τ' ⊂ ∪X ⊂ ∪X^+, as Setting CE's d(·) requires (PROOF l.1836-1837,
  "contained in ∪X").
- |X| ≤ 16(1 + d) (CE-geo'), so the bound is 273d + 272. s1 D1-D2 PASS.

### A3-5. Corollary CE^+ (l.142-146, l.356-363): CONFIRMED (counted)
- The regrouping H'(Y) = Σ_{X^+=Y}H(X) is right; it depends on Φ|_Y.
- The count 2^{|Y|} ≤ 2^{16(1+d(Y))} is right, and d(X) ≥ (d(Y) - 272)/273. H'_0 and κ' are as stated.
- Theorem CE's conclusion form (PROOF l.1896-1897, "depends only on {H(X): X ⊂ Y}") transfers to {H(X): X^+ ⊂ Y}.
- 273(3κ_0 + 3 + 16log2) = 127774 (s1 E1).

### A3-6. Lemma SF-s (l.147-149, l.365-371): CONFIRMED (standard; not counted)
The reading "Cauchy gain" needs s̄ ≫ 1. That is (V8); fine.

### A3-7. Proposition SF-V (l.150-166, l.373-401): CONFIRMED-WITH-FIX as a verdict (not counted)
This decides whether the cluster expansion can be run at all. Answer: **yes at level 0, in white-noise variables, modulo
(CE-s); not as written at k ≥ 1.**
- (V1) CONFIRMED, and stronger. CE's (H1) needs a product measure on sites. The A-field is correlated. Moreover:
  - the s-weakened 𝒞^Π(s) is non-symmetric, so no "decoupled Gaussian μ_{C(s)}" exists in this RW scheme;
  - a correlated-Gaussian CE variant (Brydges-Federbush / Dimock II style, factorising over s-decoupled regions) would
    need a *symmetric* decoupling (e.g. s-weakened covariance C(s) = Σ s-products of localised pieces);
  - **Fix V-1:** say "Theorem CE as stated (product measure) requires Z-variables. A symmetric-decoupling covariance would
    allow a correlated-Gaussian variant; RW's P(1 - R(s))^{-1} does not supply one."
- (V2) CONFIRMED at level 0 off 𝒴 (SF-DC (d) + CE^+).
- (V3) CONFIRMED that (CE-s) is required: component-wide dependence near 𝒴.
- (V4) CONFIRMED with OP-1/OP-3's narrowing.
- (V5) CONFIRMED. The polynomial growth of V_τ, log j in Z makes CE's Step-1 |z| ≤ log 2 impossible under μ_wn. ν_Q restores
  bounded support on Q^c and the product. The Q-polymers are a named part of (CE-s).
- (V6) CONFIRMED (real ν_Q; complexity in the activities; Theorem CE allows complex activities, PROOF l.1847).
- (V7) **Fix V-2:** the M ≳ 2.6·10¹⁵ requirement comes from the walk activities (decay e^{-m_1·fine distance}).
  - Activities supported on one M-cube plus collar (all of SF-A2^0's local terms) have H(X) = 0 for d(X) > 0, so they satisfy
    |H| ≤ H_0e^{-κd} for every κ.
  - Hence V7 is a statement about (CE-s), already tagged [inference] at l.394-395. Keep the tag, and say "for (CE-s)'s
    𝒴-activities".
  - Arithmetic reproduced: 2.646·10¹⁵, 1.53·10¹³, 4.93·10⁶¹.
- (V8) CONFIRMED. R ≥ R_* + (2/(aL))log(s̄/(2θ)). Note that Theorem N5-sf0 (b) is stated for R = R_*. Using R > R_* needs
  RW's hypotheses at the larger R (they hold: ε_R decreases in R) and T ≥ 4R + 6. Say so.

### A3-8. Proposition SF-A3^0 (l.167-170, l.403-408): ARGUED, CONFIRMED as labelled
The source term's size is now O(y_bg·g_0p) (A2-6). It is no worse than the Jacobian term at small curvature.

## A4 (reproduction)

### A4-1. Lemma SF-blk (l.173-181, l.412-425): CONFIRMED (counted)
- d_{k+1}(X̄) ≤ d_k(X)/L: τ ⊂ ∪X ⊂ ∪X̄ and meets every closed level-(k+1) cube of X̄.
- The (g4')/(g5') sums give 16L⁴K_0e^{d}.
- Thresholds: rate reproduction κ ≥ 227.47, contraction for d ≥ 1 at κ ≥ 302.33 (s1 E2). Both are below CE's 457.
- The disclaimer that d < 1 polymers are not contracted and need extraction is correct and important.
- Remark: the pre-stated hypothesis κ ≥ κ_0L/(L - 1) + 1 is stronger than what is used. SF says so; fine.

### A4-2. A4 remainder (l.182-184, l.427-428): carried hypotheses; no verdict.

---

# PART B: the four corrections and their cross-file consequences

| correction (SF line) | verdict | cross-file consequences (file:line) |
|---|---|---|
| exp chart full cover only for N = 2 (l.218-226, l.467-468) | **right for D_N, overstated as a chart property** (Fix SF-J-1: D'_N covers full Haar for all N) | No file assumes full cover. PROOF l.3646 ("exp is injective on ||X|| < π … Haar Jacobian on ||X|| ≤ ½") uses only a δ-ball: unaffected. EXISTENCE l.2188-2190 (Proposition NA-3): "log taken with spectrum in (-π, π)" is the principal log. For N ≥ 3 it is not su(N)-valued on a positive-measure set (trace ∈ 2πiZ). E[log V_C] = 0 still holds (inversion symmetry is exact for the principal log). Any su(N) reading needs the Lemma TL / SF-thr restriction: wording only. PLD l.1125 ("Haar Jacobian … Hessians O(1)"): consistent with SF-J ((N/12)tr A²); unaffected. |
| missing √N in A = g_0√N𝒞Z (l.285-299, l.469) | **CONFIRMED** (stage-0 exponent (u_0/N)(S_W + κΣφ̂)) | PLD l.1114-1117 writes "covariance g_0²C(𝔟(V), V)" "up to the normalisation constant of the action (a factor depending only on N)". The factor is N (RLARGE normalisation), so σ_fl² gains a factor N. Harmless (PLD says only finiteness is used), but make it explicit. PLD l.315/320 (s_i² = Ng_i²/κ, σ_k² ≤ Ng_k²(1 + 18/κ)) and RLARGE/HIST's e^{-ε²/(4Ng²)} forms already carry N: unaffected. No other file writes A = g𝒞Z (searched: `g𝒞Z`, `g_k𝒞`, `g_0²C`, `C/u`). |
| non-vanishing linear source from log n_c (l.300-302, l.469-470) | **right, size overstated** (Fix SF-A2-1: O(y_bg), zero at flat backgrounds) | HIST Lemma HF l.880-904 (φ- vs k̃-tower; d(M) = O(y⁶)) and FLOW Lemma F-tree / §3.1 l.120-131 (β[𝓔_k] = 1): **unaffected**. They are tree-level statements about critical values, and the normalisation is u-independent (one-loop functional Γ_k, FLOW §5.1). The source enters the fluctuation integral at O(g²·y_bg²) (one Gaussian contraction of a linear term in Z), i.e. beyond one loop, and in the CE as an activity. EXISTENCE Proposition NA-3 (l.2185): **consistent**: at a flat background the source vanishes. HIST §25.6 (d'') l.1731-1733 lists the normalisation as "c-number plus a holomorphic per-link term" without a linear-term remark. Add one there (owner HIST): 𝔫_c's gradient at the background is O(y_bg). |
| (F1) 1.0107 vs 1.011 (l.194-195, l.510-512) | **CONFIRMED** (max = 4arcsin(¼) = 1.0107214 > 1.0107) | HIST l.1185 ((F1) parenthetical) as SF says. **Not all uses are 1.011.** HIST l.1772 defines **c' := 1.0107√N** and uses it as an upper-bound constant in y'_η and (Z2) (l.1775-1778). Fix: c' := 1.011√N (all smallness conditions have slack; no conclusion changes). PROOF l.701 and l.3811 define c := 4arcsin(1/4) exactly and display "= 1.0107". If c enters symbolically, that is a display rounding only. The derived numbers (L > 1 + c(d+2) = 7.06; C_1 = 45.4) are unchanged at 1.010721. Change the display to 1.01072 or "< 1.0108". |

---

# PART C: s1 re-run (MANDATORY NUMERIC LOCK) and reviewer diagnostics

- Lock: `until mkdir …/locks/numeric 2>/dev/null; do sleep 20; done`; one `rmdir` at the end (no trap, no timeout); waited
  ~38 min for another holder. Acquired 03:33:59 UTC, released 03:34:13 UTC. Load 4.24 (< 8, checked before running), 44%
  free. nice 10, BLAS threads 1, `python3` without -I. Record in scratchpad revSF1/rev_time.txt.
- **s1 (checks/s1_sf.py, unchanged): 11.9 s, peak RSS 309 MB, exit 0. Output byte-identical to checks/s1_out.txt** (`diff`
  empty). A0-A6, B1-B5, C1, D1-D2, E1-E3 PASS; E4 FAIL (1.010721 > 1.0107); OVERALL FAIL as pre-registered. The ledger's
  record is accurate.
- **Reviewer diagnostics (revSF1/rev_diag.py; post hoc, not pre-registered, informational; 1.5 s, 124 MB):**
  - R1 (independent RW, plain Neumann series, all boxes, d = 2, 8 × 8 blocks, L = 2): K^{-1}(1; t) = (K + t)^{-1} to 2.4·10⁻¹⁵
    at t = 0, 1, 7 (N_0(|R|) = 0.067, 0.044, 0.010). This validates the RW formula SF-DC uses; s1 tested only zero patterns.
  - R2: finite range: SF-DC (a), (b) exact 0.0. One long-range entry (1e-3): (a) stays exactly 0.0, (b) becomes 1.1·10⁻⁴.
    Basis of Fix OP-1.
  - R3: Haar fraction in exp{||A||_op < π}: SU(2) 1.0000, SU(3) 0.9753, SU(4) 0.9476. Fraction with a traceless log of
    spread < 2π: 1.0000 for all three. Basis of Fix SF-J-1.
  - R4: 4arcsin(¼) = 1.010721021 (> 1.0107, < 1.0108, < 1.011).
  - R5: SU(2) two-path contour average, d|M̄|/dt(0) = 0 at spread 0, and −0.144·spread at spreads 0.01-0.08. So the linear
    source of log n_c is proportional to the background spread. Basis of Fix SF-A2-1.

---

# PART D: corrected tally and binding fixes

**Corrected tally of SF.md (all unreviewed before this file):**
- PROVEN-HERE 11:
  - counted 5: SF-J (with Fix SF-J-1/2), SF-T0 (Fix SF-T0-1), SF-DC, CE^+, SF-blk;
  - not counted 6: SF-thr (Fix SF-thr-1/2), SF-cut, SF-N0, SF-WN, SF-geo, SF-V (Fixes V-1, V-2).
- Standard 1: SF-s.
- CONDITIONAL 2: SF-thr-k (⇐ (N5-unif) ⇐[S21 implication] (H-K) + (H-C)); SF-A2^0 (⇐ (FP-loc)_0 + NORM-an domain match).
- ARGUED 2: (CE-s), SF-A3^0.
- OPEN names: (BG-loc) (NOT WELL-POSED; merge with HIST (a5-G)/(a5-U)), (N5-reg)_k, (OP-loc)_k (necessity narrowed); (SF-N)
  reduced to a domain match.
- 0 GAP, 0 WRONG.
- **No change to PROOF.md's 72 / 2 / 7 / 24 + 1**: SF discharges no RLARGE §4.2 row.

**Binding fixes (next SF session):**
1. **SF-J-1:** the chart correction is chart-specific. Add D'_N (full Haar, all N) with the injectivity argument, or state
   that D_N is chosen for the bounds. Rewrite §4.2's first bullet.
2. **SF-J-2:** fix one Euclidean structure on su(N) (Frobenius); adjust §0 l.33-34.
3. **SF-thr-1/2:** state the field chain (cut on V ⇒ background class via BR1 (iii)/CURV1/NAH-unif). Interior plaquettes only;
   inter-cube by [v2-E8]'s event. Also cover ε_loc, ε^J_loc.
4. **SF-thr-k-1:** re-base on PROOF [S21] Proposition NAH-unif ((H-K) + (H-C)).
5. **SF-thr-k-2:** withdraw "the soft clause is not implied by any cut" for the background. Restrict it to the integrated
   field.
6. **BG-1:** level-(k+1) soft fluctuations, as in the template.
7. **BG-loc-1:** restate (BG-loc) against HIST §25.5 (a5-G) + (a5-U) + Theorem A5 (B) (full-cone term set as boundary
   convention). Retire the duplicate name, or prove the implication.
8. **SF-N-1:** re-base (SF-N) on HIST §25.4 Lemma NORM-an. Leave only the domain match.
9. **SF-A2-1/2/3:** source size O(y_bg·g_0√NN_0p), vanishing at flat backgrounds (NA-3). Covariance Ng_0²C. Status line.
10. **SF-T0-1:** rename the kernel strength (κ_0 clash with CE's κ_0).
11. **OP-1/2/3:** withdraw "fails even off 𝒴". "Necessity" means necessity of this route. Extend (OP-loc)_k to the main-term
    densities (HIST A5 (C)).
12. **V-1/V-2:** (V1) add the non-symmetry of P(1 - R(s))^{-1}. (V7) is a (CE-s) statement.
13. **V8 note:** R > R_* needs T ≥ 4R + 6 and RW at R; say so.
14. **(F1) consumers (owners, not SF):** HIST l.1772 c' := 1.011√N; HIST l.1185 parenthetical; PROOF l.701, l.3811 displays.
15. **s1 design (for the next check):** validate any RW implementation at s ≡ 1 against (K + t)^{-1} before testing zero
    patterns.

**Owner-file notes (not SF's to edit):** PLD l.1114-1117 (factor N explicit); HIST l.1731-1733 (linear-term remark on 𝔫_c);
HIST l.1772, l.1185; PROOF l.701, l.3811; RLARGE row 3a (l.404) is stale after [S21] ("named, not precisely stated in
PROOF": [S21] NAH-unif now states the implication with (H-K), (H-C)).

---

# PART E: strategic verdict on the next SF target

**Verdict: the cluster expansion can be run at level 0, in white-noise variables, with collar locality and a per-site cut.
SF-V's analysis is the right skeleton.** Everything at stage 0 except two items is proven or reduced to already-proven items
(SF-J, SF-T0, SF-cut, SF-WN, SF-DC, CE^+, NORM-an):
- **(CE-s)**, the joint s-Mayer step;
- **(FP-loc)_0**.

The genuine wall is at k ≥ 1:
- the operator and the main-term densities are only exponentially local ((OP-loc)_k, OP-3);
- the background is regional ((a5-G)/(BG-loc));
- the thresholds are level-uniform only under (H-C).

**Recommended next target: (CE-s) written for an exponentially local K and exponentially local activities, with a second
interpolation for the long-range part ("(CE-s)^exp").** Reasons:
1. It is the composition that SF-A3^0 lacks, and it is where (V7)'s constants actually get fixed.
2. Written for exponential locality, the same lemma covers level 0 (finite range is a special case) and removes (OP-loc)_k
   as a separate item. One lemma, two levels, in line with "fewer, better" items.
3. It is a standard-in-kind expansion (Balaban's localisation; Brydges-Dimock-Hurd-type s-interpolation) with no new
   analytic input beyond Theorem RW (whose (RW2) already allows exponential decay) and Theorem CE. So it is session-scale
   with a clear failure mode: the polymer combinatorics of 𝒴-components coupled by long-range entries.

**Not recommended next:**
- (BG-loc) as a separate statement: it is HIST's (a5-G), already precise and assigned to lane F. Attack (a5-G) only after
  (CE-s)^exp, or in parallel with PROOF's (H-C) work, since both are the same level-uniform linear-analytic input.
- (FP-loc)_0 first: it matters, but it is a stage-0 detail and does not decide the route.
