# REVIEW_HIST_S4: hostile review of lane D session 4 (HIST.md §24-§29 and the [RH3-fix] changes)

Reviewer: an independent agent that wrote none of HIST.md, SF.md or the checks. I edited no other file. No commits, PRs or
pushes.

Inputs (read-only):
- REVIEW_HIST_S3.md (format; fixes 1-9).
- HIST.md §15.3-§15.4 (l.1005-1054), §20-§23 (l.1182-1506), §24-§29 (l.1508-1900); all 18 [RH3-fix] tags (grep).
- HIST_LOG.md session 4-D (l.109-146).
- checks/h7_criteria.md, h7_term_an.py, h7_out.txt, h7_time.txt, and their mtimes. Script re-run under the numeric lock,
  with one post hoc diagnostic (below).
- RLARGE.md v2 (RLF-5) l.190-193, K7 l.583-585; PLD.md §9.4 (RLF-5) width l.497-503.
- PROOF.md NA-IFT, B-NA-red, (FP♯'), NA-crit', BNA-F1-F3 (l.3136-3197); RTARGET.md §33 norms (l.592-612).
- SF.md §2 (SF-N) l.102-106, §3.2 SF-J (2) l.217-228, SF-A2^0 l.284-305, §4.2 l.466-471 (lane F's corrections).
- literature/balaban_cmp109_text.txt l.574-592 (pointer 9).

Scratch work (diagnostic script, re-run outputs, lock log) is in the scratchpad directory `revhist4/`.

---

## Bottom line

- **The RH3 fixes are correct (17 of 18 clean).**
  - MSG-loc' with c_qα² is right as stated (re-derived: B' = 21.0, c_q = 66A_de^{4C_*ε}/L² ≈ 66), with one wording fix:
    α_cell must be the maximum over the coarse cells met by the block pair (N-5).
  - l.1440 has a sign slip in the c-number (N-6).
  - §20.3 (B)'s "C_cone ≳ 10¹²" is now superseded by §26's ≈ 10¹⁵ (N-7).
- **Lemma TERM-an: CONFIRMED.** I re-derived (i)-(iii), including both expansions and every constant (9.11y², 18.4y²,
  4.6y²/N, θ = 18.4y²(2 + 2c_N)). Chart-free, SU(N)-gauge invariant, explicit.
- **Lemma NORM-an: CONFIRMED.**
  - The "contour shift" is an exact identity on a compact group. J(A) = ∫f(AV)dV is holomorphic on SL(N, ℂ) and constant on
    SU(N), and SU(N) is maximal totally real, so J is constant.
  - No decay or boundary terms are needed, only that the integrand is entire in V. It is: V⁻¹ is the adjugate, and
    det W_0^ℂ = 1 because X_0^ℂ is traceless.
  - Lane F's linear-source correction does not break it, but the "no linear term" sentence and the §25.4 [inference] need
    rewording (S4-4).
- **Lemmas POL, EXT, (R♯_∞): CONFIRMED** (all constants re-derived).
- **Theorem A5: NOT a valid CONDITIONAL as written. Two binding defects:**
  - **S4-1 (fatal as written, short to fix).** (a5-G) asks for ||𝓛⁻¹||_{ℓ^∞→ℓ^∞} ≤ G uniformly in depth. That is false already
    at the trivial chain: a variational bound gives G ≳ L^{2(k-1)}. It is PROOF's established failure mode BNA-F2: sup norms
    do not close, and PROOF's (G♯) lives in RTARGET §33's level-weighted Schauder pair.
    - HIST's parenthesis "(this is PROOF's (G♯) at U = 1 in sup norms)" misreads PROOF.
    - With (a5-G) restated in the (G♯) pair, (R♯_∞) has to be replaced by PROOF's (R♯) in that pair, which is OPEN ("expected,
      not written").
    - So the depth-uniform radius currently rests on a false hypothesis.
  - **S4-2 (base-set gap).** Parts (B) and (C) use (a5-U) and (a3-q) at the points Ue^Z of P_{s_5}(U), which leave R_{2ε_1}
    where those hypotheses are stated.
  - The contour/identity-theorem logic, the gluing and the gauge invariance are otherwise sound.
  - **Re-label ARGUED. It becomes CONDITIONAL as soon as S4-1 and S4-2 are applied** (both are statement-level edits).
- **Theorem AE-red: CONFIRMED as CONDITIONAL ⇐ (MS-Sob).**
  - Every error term was re-derived. The op/HS bookkeeping is right.
  - C'_AE = 2C_locN is fixed before η_AE, and the induction re-derives the same constant.
  - C_e = 1.883·10⁴, C_2 = 5.55·10⁷, η_AE = 1.78·10⁻¹⁵ and C_cone = 1.13·10¹⁵ (N = 2, C_S ≤ 10²) are reproduced.
  - The largest admissible η_AE is ≈ 2.7·10⁻¹⁵. h7's factor-2 grid gives 1.78·10⁻¹⁵, which is fine.
- **(I_k^E)'' and the RLF-5 width: a real inconsistency between statements, not between proofs.**
  - (b'') puts every polymer E_k on a g-independent width α_E. PLD's ARGUED width for the returned large-field remainders is
    O(g/√κ).
  - The fix is to re-centre the inner integration of the frozen activity at the holomorphic critical branch (A5 (B) type).
    That removes the linear phase that causes the O(g/√κ). Fallback: a second polymer class whose e^{-a/g²} size pays the
    Cauchy loss (S4-5).
- **h7: honest. Criteria precede the script (21:57:46 < 22:08:39 EDT). The A3 FAIL stands as recorded. The re-run reproduces
  every line.**
  - Post hoc, the A3 test has almost no power for φ^ℂ: its CR defect, 4.3·10⁻⁴, lies inside the control's range.
  - For X_0^ℂ the separation is real but was not what was pre-registered.
  - My central-difference Wirtinger diagnostic does discriminate, and it supports both objects: ≤ 1.2·10⁻⁸ against a control
    ≥ 10⁻⁷ (Priority 7).
- **Corrected session-4 tally: 2 PROVEN-HERE / 1 CONDITIONAL / 1 ARGUED.** The claim was 2/2/0.
  - **Whole file: 11 / 5 / 8 / 4 + 1 HYPOTHESIS** (claimed 11/6/7/4 + 1).

---

## Priority 1. The RH3 fixes (18 tags)

| Tag (line) | Fix | Verdict |
|---|---|---|
| l.1022 | N-4: η_E depends on C'_AE, ε_AE, η_AE; η_E ≤ η_AE | CONFIRMED |
| l.1030-1031 | N-4: CLS-red display with C_cone = max{C'_AE/(2N), 2/η_E} | CONFIRMED. The proof text (γ)/(δ) at l.1045-1047 still shows the old constants; the l.1021-1022 bracket covers them. Acceptable. |
| l.1218-1222 | S3-1: A_ax = 9 with P's plane first, else 2(2L-1) + (d-3)(L-1) = 12 | CONFIRMED. Ladder Σ_{ν>μ}x_ν: 5+2+2 = 9 vs 2+5+5 = 12. 1.011(1.011·3·12 + 19) = 56.0 < 66.1, so C_M is unchanged. |
| l.1228-1229 | S3-1 in the construction | CONFIRMED. The intra-block paths γ_x (order 0, …, d-1) are unaffected. |
| l.1273-1277 | Literature pointer 9 | CONFIRMED against text l.574-592: "in the axial gauges", (1.14), (1.16) on X^{-2}. |
| l.1284-1297 | S3-2: MSG-loc GAP; MSG-loc' with c_qα_cell² | CONFIRMED-WITH-FIX (N-5) |
| l.1296 | cross-reference to (SQ-dev) | CONFIRMED |
| l.1318-1322 | S3-3: d = 4; L^{(d-4)(j_1+j_2)/2}; 5^d and L^d go into C_Q | CONFIRMED (‖g_j‖²_2 = dL^{dj}L^{-2j}h_j gives exactly this factor) |
| l.1325-1331 | S3-4: MS-Sob ⇐ MSG-loc-dev + MS-HLS + SQ-dev, ARGUED | CONFIRMED |
| l.1330 | (SQ-dev) includes c_qα² | CONFIRMED |
| l.1333 | curvature-source implication demoted to a vacuous remark | CONFIRMED |
| l.1363-1365 | net status of (AE) | CONFIRMED (and superseded by §26, correctly) |
| l.1383-1394 | S3-5: (c1) 1/24, (c2) 1/576, (c3) disjoint footprints or k-fold; size remark | CONFIRMED; the numbers need updating (N-7) |
| l.1418-1420 | S3-6 marked; repaired in §25 | CONFIRMED as marking (the repair is Priority 2/4) |
| l.1421-1424 | S3-7: read Ve^{H}, H Hermitian traceless | CONFIRMED. (b')'s text at l.1425-1433 keeps the struck notation, marked; (b'') l.1726 is correct. |
| l.1440-1442 | (d') c-number note | CONFIRMED-WITH-FIX (N-6, sign) |
| l.1484-1486 | §22 corrected outcomes | CONFIRMED |
| l.1496-1500 | §23 corrected tally 9/4/8/4 + 1 | CONFIRMED |

**MSG-loc' (l.1287-1292).** Steps (3)-(6) with step (5) kept local give:
- (2A_d + 2)ε̂ + A_dL⁻²(1.011ε̂ + 33α²e^{4α}).
- With (F3)'s factor 2 this is 2B'ε̂ + c_qα², where B' = 2A_d + 2 + 1.011A_d/L² = 21.01 and c_q = 66A_de^{4α}/L² (= 66 at
  d = 4, L = 3). Correct.
- Step (4)'s 18.4y² is ≤ ε̂ locally, because y ∝ ε̂.
- (F3)'s condition ||1 - U^g|| ≤ ½ uses the global ε. That is allowed, since MSG's hypotheses stay global.

**N-5 (wording, binding).** The V-curvature term enters through max_p||1 - V(p)|| over the ladder plaquettes of steps (3)-(4).
Those plaquettes span the block pair X ∪ Y, and their coarse cells are all the cells meeting X ∪ Y, not only "b's coarse
cell". Define α_cell(b) := max{|a_{i+1}(c)| : c a coarse edge of a cell meeting b's block pair}. The iterated form is then
unchanged, because the neighbourhoods do not grow.

**N-6 (sign, cosmetic).** (d') lists "the kernel normalisation -Σ_clog∫e^{-κu_kφ}". The field-independent part of that term is
+((N² - 1)/2)log(κu_k) + const per link, since 𝒩_0 ~ c(κu)^{-(N²-1)/2}. The displayed "-((N² - 1)/2)log(κu_k)" is the part
of log𝒩_c. SF's ν(M) := log n_c + ((N² - 1)/2)log(κu_0/2π) agrees with this reading. It is a c-number either way.

**N-7 (numbers).** l.1391-1394 says "η_AE ≲ … ≈ 3·10⁻¹³, C_cone ≳ 10¹²" and "≳ u_kε_1²·10⁻¹³". After §26/h7 C the values are
η_AE ≈ 1.8·10⁻¹⁵ and C_cone ≈ 1.1·10¹⁵ (N = 2). Update these, and see Strategic point 3 for what this implies for ε_1.

---

## Priority 2. Lemma TERM-an (§25.1, l.1554-1597) and Lemma NORM-an (§25.4, l.1628-1649)

### TERM-an: CONFIRMED (PROVEN-HERE, counted)
- **(i)** s^ℂ is entire, conjugation invariant and equals s on SU(N). On P_r, ||U_p||, ||U_p⁻¹|| ≤ e^{4r}, so |s^ℂ| ≤ 1 + e^{4r}.
- **(ii) Expansion.** e^{-X}M = (1 - X + R_X)(1 + Ȳ + E) gives K = E + R_X + (R_X - X)(Ȳ + E).
  - On |X| ≤ 3y, y ≤ 1/20: |R_X| ≤ (9y²/2)e^{3y} = 5.23y², |E| ≤ (y²/2)e^y = 0.53y², and |(R_X - X)(Ȳ + E)| ≤ 3.35y².
  - So |K| ≤ 9.11y². Only submultiplicativity and the series are used, so these hold verbatim for complex arguments.
  - Ǩ is the holomorphic continuation of K*. On real data (e^{-X}M)* = M̌e^X and (Ȳ - X)* = -(Ȳ - X), so K* = Ǩ.
  - Φ^ℂ restricts to NA-alg's Φ on su(N), and uniqueness in B^ℂ identifies the fixed points.
- **(ii) Stationarity.** G - Ǧ = 2(Ȳ - X) + K - Ǩ, so the fixed-point equation is Π_0(G - Ǧ) = 0.
  - Then |G - 1| ≤ 9.2y² + 9.11y² ≤ 18.4y² and |K + Ǩ| ≤ 18.22y².
  - Holomorphy follows from locally uniform convergence of holomorphic iterates. Use a fixed y on {|Y_j| ≤ y}.
- **(iii)** Y_j is traceless: e^{tr Y_j} = 1 and |tr Y_j| ≤ √N·y_0 < 2π.
  - φ^ℂ = φ on real chains: W_0(M̄) = Se^{X_0} by left covariance, and Re tr Z = ½(tr Z + tr Z*). Correct.
  - Gauge: S⁻¹T_j and V' are conjugated by g(c_Y). Correct.
- **Local expansion.** The order-1 term vanishes by stationarity (G - Ǧ ∝ 1, tr ρ = 0).
  - Order 2 is -tr(ρ²)/(2N) - (1/4N)tr(ρ²(K + Ǩ)), with |·| ≤ 18.3y²|ρ|²/(4N) ≤ 4.6y²|ρ|²/N.
  - Orders ≥ 3: |G|_HS ≤ √Ne^{4y}, which gives e^{4y+|ρ|}|ρ|³/(6√N). Correct.
- **Global form.** I re-derived φ^ℂ(W_0^ℂV'') = s + (1/2N)[tr(Γ(D + D*)) - c·tr D], with D + D* = DD*.
  - The branch |D| < r_N: |θ_j| ≤ (π/2)|1 - e^{iθ_j}|, Σθ_j = 0, and |Im tr V''| ≤ (π³/72)|D|². The bound (1 + 2c_N) is loose
    but valid.
  - The branch |D| ≥ r_N gives N/r_N². Here |c| ≤ ||G - Ǧ|| (op).
  - θ = 18.4y²(2 + 2c_N). Correct.
- **Observation (non-binding).** h7 A2 prints |X_0 - Ȳ|/(9.2y²) = 0.000.
  - This is structural. On real data the second-order part of X_0 - Ȳ is the anti-Hermitian part of the Hermitian avg Y_j²/2
    and Ȳ²/2, which is 0. By the identity theorem it vanishes for complex data too, so X_0 - Ȳ = O(y³).
  - The 9.2y² bound is valid but loose by a factor ~ y. θ does not improve, since G - 1 has a genuine O(y²) part.

### NORM-an: CONFIRMED (PROVEN-HERE, counted); two wording fixes
- **(i) Haar shift.** This is the legitimate form of the contour shift on a compact group. It is an identity, not a deformation.
  - J(A) = ∫_{SU(N)}f(AV)dV is holomorphic on SL(N, ℂ): differentiate under the integral over a compact set.
  - J(A) = J(1) on SU(N) (Haar).
  - SU(N) is a maximal totally real submanifold of the connected SL(N, ℂ), so J ≡ J(1).
  - What is needed: f entire on SL(N, ℂ), or at least holomorphic on a connected open set containing A·SU(N) for all A on a
    path from 1 to W_0^ℂ.
  - e^{-κuφ^ℂ_c(V)} qualifies, since it is entire in V (V⁻¹ = adjugate, det V = 1). det W_0^ℂ = det S·e^{tr X_0} = 1.
  - No decay at infinity and no boundary term arise, because the group is compact.
- **(ii)** The steps check:
  - |e^{-κuΔ} - 1| ≤ κuθse^{κuθs}, and |e^{-κu(s+Δ)}| ≤ e^{-κu(1-θ)s}.
  - te^{-at} ≤ (2/(ea))e^{-at/2}.
  - Z(Λ) ≥ e⁻¹v(1/Λ) for Λ ≥ ½, and Z(λ) = ∫λe^{-λt}v(t)dt ≤ c'_+Γ(D/2 + 1)λ^{-D/2}.
  - The ratio is ≤ C^Z_N·4^{D/2}.
  - So |𝒩^ℂ/𝒩_0 - 1| ≤ C_Nθ, uniformly in u ≥ 1/(2κ), hence uniformly in g.
- C_N exists but is not computed. The width condition C_Nθ ≤ ½ is therefore g-independent but not explicit. Say so in §25.6
  (d''), where α_E is chosen.
- **SF's three corrections do not break NORM-an or TERM-an.**
  - (1) The exponential chart covers full Haar only for N = 2. HIST never integrates through the chart. NORM-an's v(t) ~ c_vt^{D/2}
    is a small-t (identity-neighbourhood) statement, and v ≡ 1 for t ≥ 2 covers the rest. POL, EXT and P_r use e^Z only for
    ||Z|| ≤ 1/8.
  - (2) The missing √N in A = g_0√N𝒞Z enters only (c3'')'s quoted PLD width. It should read O(g√N/√κ), which is N-fixed and
    harmless.
  - (3) The linear source: see S4-4.
- **S4-4 (wording, binding).**
  - The Reading's "after the shift the integrand is s(V'')(1 + O(y²)), with no linear term (stationarity)" is about the
    integration variable V''. It is correct there.
  - As a function of the fine field, 𝔫_c = O(y²) with y the TOTAL contour spread (background + fluctuation). At a background
    with spread y_bg ≠ 0, 𝔫_c therefore has a linear term in the fluctuation A, of size O(y_bg)·|A|. That is exactly lane F's
    "non-vanishing linear source", since U(V) is critical for F and not for F + Σlog n_c.
  - HIST's bound sharpens SF's "order g_0p per coarse link" to O(y_bg·g_0√N·p) and is consistent with it.
  - Add one sentence to (d'') and to the NORM-an Reading saying so.
  - Also, the [inference] (l.1647-1649) that "the same shift applies to the sea average of any ENTIRE function of the fine
    field" is overstated. The kernel e^{-κuφ_{M̄}(V)} is entire in V, but NOT in the fine field. φ contains the support function
    max_W Re tr(W⁻¹M̄), which is holomorphic only on D_c(y_0), where the maximiser is unique.
  - So the width loss sits in the small-field restrictions (the indicators AND D_c(y_0)), not in the indicators alone. Re-word
    it; it stays an inference.

---

## Priority 3. The complex domain: Lemma POL (l.1599-1615), Lemma EXT (l.1617-1626), (b''), (R♯_∞)

- **Notation (§25.0).** The real/imaginary split of Z ∈ sl(N, ℂ) gives X ∈ su(N), and iY Hermitian traceless (tr X = i·Im
  tr Z = 0). Correct.
  - Real points of P_r: e^Z unitary gives e^{Z*} = e^{-Z}, and exp is injective on ||·|| < π, so Z ∈ su(N). Correct.
  - S3-7 is applied correctly in 𝔇_{ε,α}.
- **POL (i): CONFIRMED.**
  - A*A = e^{-X+iY}e^{X+iY}, H = ½log(A*A), V = Ae^{-H} unitary, tr H = 0, det V = 1.
  - ||A*A - 1|| ≤ e^{1/2} - 1, so ||G|| ≤ 0.5231.
  - Schwarz's lemma for ζ ↦ G(X, ζY/(8||Y||)) (G(X, 0) = 0) gives ||H|| ≤ 4.185||Y||.
  - ||e^{X+iY} - e^X|| ≤ e^{||X||}(e^{||Y||} - 1) (termwise series bound) = 1.207||Y||. The total is 7.54||Y|| ≤ 9.2||Y||.
  - h7 B2 measures the true constants as ≈ 1.0 and 0.005.
- **POL (ii): CONFIRMED.** ||V - 1|| ≤ (7.6 + 1)r, the plaquette moves by ≤ 4·10.2r, and the converse is trivial.
- **POL (iii): CONFIRMED.**
  - ||e^{-a}(e^w - e^a)|| ≤ e^{||a||}(e^r - 1) ≤ 1.17r, and -log(1 - x) ≤ x/(1 - x), giving 1.27r.
  - The polydisc in w-coordinates exists wherever a small-log gauge exists.
  - The domain itself is chart-free (P_r and 𝔇 need no gauge), so "in a local MSG gauge" is only the coordinate statement.
    Note that MSG concerns chains, not level-k fields alone. On a level-k field, a bounded-box axial gauge suffices for (iii).
- **EXT: CONFIRMED.** The steps check:
  - U_1⁻¹U_2 = e^{Z_1}e^{-Z_2} is unitary, and ||X_12|| ≤ 0.522r (F1, with the principal log traceless near 1).
  - e^{0.772r} - 1 ≤ 0.81r (r ≤ 1/8; this is tight, 0.8108 at r = 1/8, and still fine), so ||Z'|| ≤ 0.9r.
  - The real points form an open subset of a maximal totally real submanifold. The identity theorem applies on the connected
    overlap P_{r/4}(U_2).
- **(b'') (l.1726-1729): CONFIRMED** as a statement: P_r(U^r) ⊂ 𝔇_{ε_1+41r, 4.19r} ⊂ 𝔇_{2ε_1, α_E}. It is one gauge-covariant,
  chart-free domain with genuine polydiscs, and it is the object K7 asks for. Its consistency with RLF-5 is Priority 5.
- **Sup-norm remainder (R♯_∞) (l.1674-1681): CONFIRMED as an estimate.**
  - n_T counts V, the links of the two endpoint blocks, and the crossing links; m_T depends on (L, d).
  - Cauchy's estimates per term, summed over the ≤ m_T terms through a link, give NA-IFT's two ℓ^∞ bounds with
    C = O(m_Tn_T²S_T/r_T³).
  - **But it is the remainder bound in the wrong norm pair** (S4-1): NA-IFT needs (R♯) in the same pair as (G♯), and in ℓ^∞
    (G♯) is false. Keep (R♯_∞) as a correct, not-counted remark.

---

## Priority 4. Theorem A5 (§25.5, l.1651-1718)

### S4-1 (binding; fatal as written): (a5-G) is false in ℓ^∞→ℓ^∞, uniformly in depth
- **Claim.** At the trivial chain (ψ^r = 1, U = 1) and for any slice with a Feynman term:
  ||𝓛⁻¹||_{ℓ^∞→ℓ^∞} ≥ c·L^{2(k-1)}, with c > 0 depending only on (N, L, d, κ).
- **Proof (variational, elementary).** Take a source j on the level-0 links: a smooth, divergence-free, unit-sup vector field
  supported in a level-0 box of side R := L^{k-1} inside the descendants of Λ_k, with ||j||_{ℓ¹} ≍ R⁴. Take a test chain x:
  - x_0 := j (so ⟨j, x⟩ ≍ R⁴);
  - x_i := Q^ix_0 for i ≤ k - 1;
  - x_k = 0 (it is the data).
  - This chain is in the slice up to an O(1) correction, because j is divergence free and smooth at scale R.
  - Its quadratic form ⟨x, 𝓛x⟩ (chain energy plus the Feynman term):
    - Σ|dx_0|² ≍ R⁻²·R⁴ = R², and the Feynman term is of the same order.
    - The kernel terms at levels ≤ k - 1 vanish, because x_{i+1} = Qx_i exactly.
    - The level-k kernel terms see |Qx_{k-1} - x_k| = |Qx_{k-1}|. In own units Q sums L fine links, so x_i has own-unit
      amplitude ≍ L^i. These terms therefore carry ≍ (L·L^{k-1})² = L²R² on O(1) links.
    - In total ⟨x, 𝓛x⟩ ≲ C(1 + κL²)R².
  - 𝓛 > 0 on the slice (trivial chain, Feynman term). Then ||𝓛⁻¹j||_∞ ≥ ⟨j, 𝓛⁻¹j⟩/||j||_1 ≥ ⟨j, x⟩²/(⟨x, 𝓛x⟩||j||_1) ≳
    R⁸/(R²·R⁴) = R² = L^{2(k-1)}. ∎
  - Status: an elementary sketch (projecting x onto the slice and tracking the constants are routine, not written), but the
    conclusion is robust. It is the R² growth of the inverse Laplacian between sup norms on a box of side R.
- **Why.** In own units at level 0, the chain Hessian contains the level-0 lattice Laplacian on a box of side ≍ L^k, and the
  kernel springs above it are soft. This is precisely PROOF's BNA-F2 (l.3181-3187): "sup norms do not close"; the linear
  inverse must gain a derivative; the natural pair is a coarse-unit Schauder pair.
  - PROOF's (G♯) is stated in RTARGET §33's norms (Y with level weights ω, X_c with ||dB_i||, D = ||·||_{∞,m}) for that reason
    ([R1314-fix] (2), l.3166-3169).
  - So HIST's l.1666 "(At ψ^r = trivial chain this is PROOF's (G♯) at U = 1 in sup norms.)" is wrong.
  - The exponential weights e^{±κ_5d(·, b_0)} are also undefined as written. In level-0 units the response is not exponentially
    local inside a block; d must be the distance between level-k ancestors.
- **Consequence.**
  - With (a5-G) false, the conditional is vacuous.
  - NA-IFT is norm-agnostic, so the repair is a restatement:
    - (a5-G♯) := PROOF's (G♯) (and its weighted forms) at every ε_R-regular real critical chain, in the RTARGET §33 pair, with
      D the level-k sup norm;
    - (R♯) in the same pair [OPEN, owned by PROOF/N2: "expected from NA-alg and the scaling count, not written"].
  - Then s_5 is defined from (G, G_D, G_w, C, C_w) of that pair. The polydiscs P_{s_5}(U) are still level-k sup-norm
    polydiscs, so EXT, the gluing and (C)'s gauge invariance go through unchanged.
  - (R♯_∞) is no longer used.
  - The depth-uniform radius is then exactly as good as (G♯) + (R♯), which is the B-NA wall itself. Say so: A5 does not add a
    new wall, it moves (a5) into B-NA's.

### S4-2 (binding): the base set R_{2ε_1} is left by the polydiscs
- (B) asserts F_U = 𝓔^♭_k on the real points of P_{s_5}(U). Its openness step invokes (a5-U), and through (A) also (a3-q) and
  AE-red, at Ue^{Z_1}.
- But Ue^{Z_1} ∈ R_{2ε_1 + 4.04s_5}, not R_{2ε_1}, when U is near ∂R_{2ε_1}. EXT (with f = 𝓔^♭ on the union of real points of
  P_{s_5}(U)) inherits the gap.
- **Fix.** State (a5-U) and (a3-q) on R_{3ε_1}(Λ_k), take δ = 3ε_1 in (A) (so δ_a ≥ 3ε_1/… adjusts the constants), and
  require s_5 ≤ ε_1/5. Equivalently, keep the hypotheses on R_{2ε_1} and glue only over U ∈ R_{ε_1}, and then (b'') must use
  𝔇_{ε_1,α_E}.
- Also, in the openness step "by (A) it is a critical chain" is the wrong citation. The minimiser for Ue^Z lies near Ψ_U(Z_1),
  inside the analyticity polydisc (radius r_T about ψ*), so it is critical because E^♭ is smooth there. Cite that.
- Add one sentence: the contraction maps the real slice ball into itself for real Z, so Ψ_U(Z) is real for real Z (needed for
  "F_U = E^♭(minimiser)").

### Minor (A5)
- **M-1.** Restrict the chain variables to those read by 𝒞^♭-terms. Otherwise E^♭ is independent of some descendant variables,
  and (a5-U)'s uniqueness fails trivially.
- **M-2.** "Unique modulo chain gauge" must mean modulo chain gauges trivial at the level-k sites, i.e. the stabiliser of U.
- **M-3.** "ε_R-regular … so all contour spreads y ≤ y_0 in MSG gauges": the spread |log(S⁻¹T_j)| is gauge invariant and ≤
  1.011√N·A_dε_R by the lasso. MSG is not needed. Also require a strict margin (y ≤ y_0/2) so that E^♭ is analytic on a
  neighbourhood.

### What is sound in A5
- (A)'s use of AE-red: δ = 2ε_1 gives E ≤ 4C_3ε_1² ≤ η_AE, and the size clause gives ≤ C_♮√(4C_3)ε_1 ≤ ε_R. A minimiser on a
  boundaryless manifold is critical.
- (B)'s O-is-closed step (the inf is continuous in the top field). The open step after S4-2.
- (C): EXT, ⊃ 𝔇, gauge invariance by the identity theorem, and densities that are well defined without measurable selection.
- (D) is trivial.
- "An agreement claim with an unnamed uniqueness step" is avoided: (a5-U) is named, and the local slice theorem is used only
  qualitatively at fixed k, T.

---

## Priority 5. (I_k^E)'' (§25.6, l.1720-1735) and the RLF-5 width (c3'', l.1749-1755)
- **(a'')**: CONFIRMED given A5. The outer-layer and (c5) defects going to (a4)'s boundary factor follows (c3). Note that (a'')
  inherits S4-1/S4-2.
- **(d'')**: CONFIRMED with N-6 and S4-4.
- **(c1'') HF**: CONFIRMED.
  - k̃^ℂ = φ^ℂ + d^ℂ is algebraic.
  - On real data d = O(y⁶), so its Taylor terms of degree < 6 vanish and the order-6 Schwarz lemma applies.
  - For N = 2, d^ℂ ≡ 0.
- **(c2'')**: CONFIRMED. One addition: 𝔫_c = O(y²) is a u-independent quadratic term at the trivial field, so it shifts β at
  relative order g² (one loop), through Γ_k's 𝒩'_1 term as (d') says. It does not enter β[𝓔^{an}].
- **(c5'')**: CONFIRMED (conditional on (a5-U) at level k + 1).
- **Is the RLF-5 width issue a real inconsistency?** Yes, at the level of statements.
  - (b'') requires every polymer E_k(X; ·) to be holomorphic on 𝔇_{2ε_1, α_E} with g-independent α_E.
  - RLARGE (RLF-5) returns large-field remainders that feed "the polymers [of] the level-(k+1) representation". PLD §9.4's
    only analysis (ARGUED) gives width O(g/√κ) (O(g√N/√κ) after SF's √N).
  - Both cannot hold for the same polymers. Neither statement is proven, so this is a conflict of targets (K7 unresolved), not
    a contradiction between proofs.
- **Where the O(g/√κ) comes from.** It is not intrinsic.
  - PLD's phase φ is LINEAR in the imaginary part of the boundary data, with coefficient (κ/g²)·(inner residual). It is linear
    only because the inner integration is centred at the REAL configuration.
  - If the inner variables are re-centred at the holomorphic critical branch of the frozen region (exactly A5 (B)'s object,
    or NA-IFT on the frozen box), the linear term cancels by stationarity, the same mechanism as NORM-an.
  - What remains is O(ρ·(fluctuation)²/g²) = O(ρ), so the width is g-independent. The price is that the cut-good indicators
    must be defined on the fluctuation about the complex background, as in Balaban's treatment of regular G^c-configurations
    (CMP 109 p.261 [read-skim in S3]).
- **S4-5 (binding; integration item for the lead, RLARGE.md not edited).** Two options:
  - (1) Primary: state (RLF-5) as "the returned remainders are holomorphic on 𝔇_{2ε_1, α_E} after re-centring the inner
    integral at the holomorphic critical branch". Record the indicator-redefinition as its proof obligation.
  - (2) Fallback: split (b'') into small-field polymers at width α_E and large-field polymers at width c·g/√κ with size
    e^{-a/g²}. That size pays the (√κ/g)³ Cauchy loss of C³ bounds and the e^{C|Y|√κ/g} growth. The second class must then be
    carried separately through (SF^J)_k's cluster expansion, which is a node A norm decision.
  - (c3'')'s text currently states option (2) only as an inference. Add option (1), and rewrite the "indicators" sentence as
    in S4-4.

---

## Priority 6. Theorem AE-red (§26, l.1763-1849): CONFIRMED as CONDITIONAL ⇐ (MS-Sob)

**(MS-Sob) as consumed (l.1765-1769).** It is precise and per level. It is plausible in kind, but OPEN:
- the smooth example gives θ⁴ per level ≍ E²;
- level-0 noise gives L^{4k}ε⁴ ≤ C_S(L^{4k}ε²)².

It is a hypothesis on the canonical MSG gauge (axial order with P's plane first).

**Step by step (all re-derived):**
1. **Sizes.**
   - (a) Level 0: ||1 - U_0||² ≤ 2NE.
   - (b) Strong induction through nesting (§15.1; reviewed S2), with F2.
   - (c) Lasso over two ribbons: A'√C''√E ≤ ½ by (Z2); c' = 1.0107√N. The KQ dichotomy x ≤ 73.6Ny'² ≤ √C''√E (Z2) or
     x ≤ √(4N/κ)√E.
   - So ε̃ = C_♮√E. Correct.
2. **Gauge.** MSG at ε̃ ≤ ε_S ≤ ε_M; (MS-Sob) at ε̃. The (Z3) conditions p_Lm ≤ 1/8 and 4m_0 ≤ 1/8 are what F3/F5 need.
   Correct.
3. **Exact recursion.** a_{i+1} = [log(e^{X_0}e^{-ρ̃}) - X_0 + ρ̃] + Ȳ + (X_0 - Ȳ) - ρ̃. With Ȳ = Qa_i + Σw_j(Y_j - Σ_{T_j}±a_i),
   the displayed decomposition of e_i is exact.
4. **The error e_i.**
   - The three terms and their norms: F5 + F3 give 2s²e^s (s ≤ p_Lm). NA-alg gives 9.2y_c². F5 with two factors + F3 gives
     2t²e^t ≤ 4(9y_c² + ||ρ̃||²)e^t.
   - The coefficients of m², 2√Np_L²e^{1/8} + 9.4Np_L² + 36.8N^{3/2}p_L²e^{1/4}, give C_e = 1.883·10⁴ at N = 2, L = 3 (I
     recomputed it by hand: 387.7 + 2274.8 + 16170).
   - The multiplicity 2d is correct: a link inside block X lies only on contours (axial pieces or straight legs) of the 2d links
     incident to X, and a crossing link only on its parallel. So Σ_cm⁴ ≤ 2dΣ|a|⁴.
   - The φ-coefficient (1/(2N))(1 - 18.4y'² - (2√N/3)e^{|ρ|}|ρ|) is a valid weakening of TERM-an's local expansion
     (e^{4y_0} ≤ 2).
5. **Top plaquette.** R_top: (4m_k)² = 16C_M²C_♮²E, √N·2·16·e^{1/2}. Conservative (e^{1/8} suffices).
   - Unrolling stays on cone links (contours stay in endpoint blocks, l.1040-1042).
   - T_R: n⁻⁴·n²-multiplicity, ≤ 2 plaquettes per in-plane link, |L(R_0)| ≤ 8n⁴, Cauchy-Schwarz with (MS-Sob) at level 0, so
     K_R = 64√8√Ne^{1/2}. Correct.
   - The depth sum is geometric: Σ√8L^{-m} ≤ √8L/(L - 1). It is not k-fold, because (MS-Sob) is per level.
6. **Collecting.**
   - E-loc (5) Cauchy-Schwarz weight (1 + Σ_mL^{-m}) = (2L - 1)/(L - 1), and 8L^{-m} ≤ 8 inside.
   - C_loc = 40 at L = 3, κ = 1, and C'_AE = 160 (N = 2).
   - The bracket terms are each ∝ √η_AE·√E. The closing inequality (Z5) is explicit.
   - The conjugation back by g(X_P) is correct.

**Constants (h7 C, reproduced).**
- N = 2, C_S ≤ 10²: C_2 = 5.55-5.75·10⁷. (Z5) binds, at √η ≤ (12.649 - 9.798)/C_2, i.e. η_AE ≤ 2.6·10⁻¹⁵. The factor-2 grid
  gives η_AE = 1.776·10⁻¹⁵, ε̃ = 5.3·10⁻⁷, C_cone = 2/η_AE = 1.13·10¹⁵.
- C_S = 10⁴: η_AE = 8.9·10⁻¹⁶.
- N = 3: η_AE = 4.4-8.9·10⁻¹⁶.
- "C'_AE fixed before η_AE": CONFIRMED. C'_AE := 2C_locN and C_2 is independent of η_AE.
- **Wording.** "η_AE ≈ 1.8·10⁻¹⁵" holds for C_S ≤ 10². In general η_AE = η_AE(C_S, ε_S), with C_S the unknown (MS-Sob)
  constant. Write η_AE as a function of (C_S, ε_S), not as a number, wherever it is propagated (A5's δ_a, CLS-cone's price).

**Readings (l.1840-1846): CONFIRMED.**
- (i) No per-level constant is iterated.
- (ii) MSG-loc (GAP) is not used, only MSG sup bounds and (MS-Sob).
- (iv) (i)-(ii) of (AE) follow from (iii).
- The status change (AE) OPEN → CONDITIONAL ⇐ (MS-Sob) is correct. The OPEN wall is (MS-Sob), ⇐[ARGUED] MSG-loc-dev + MS-HLS
  + (SQ-dev).

**Target S7: MET.**

---

## Priority 7. h7 (re-run) and what the A3 control failure means

### Procedure and honesty
- Mtimes: h7_criteria.md 21:57:46 EDT, h7_term_an.py 22:08:39, h7_out.txt 22:50:04, h7_time.txt 22:50:57. **The criteria
  predate the script.** The run window 02:50:02-02:50:04 UTC matches h7_out's mtime.
- The script implements the criteria as written, and I checked the A3 code against the text:
  - forward differences, h = 1e-6;
  - CR defect relative to |F(Y + hD) - F(Y)|;
  - control = the real map Φ_R with Π using *.
- The script writes no files. The A3 FAIL is recorded as pre-registered and not softened; the post hoc reading is labelled as
  such.

### Re-run
- **Conditions.** The numeric lock was taken 03:34:29 UTC (after waiting for another holder) and released 03:34:32 UTC by
  exactly one rmdir, with no trap. Load 3.6; 36% memory free beforehand. nice 10, BLAS/OMP threads 1, python3 without -I, no
  timeout. Outputs went to the scratchpad only.
- **Official script.** Output is IDENTICAL to h7_out.txt except the runtime line (2.4 s; 154 MB). OVERALL FAIL (A3), exactly as
  recorded. C reproduces η_AE = 1.776·10⁻¹⁵ and C_cone = 1.13·10¹⁵.
- **Post hoc reviewer diagnostic** (`revhist4/h7r_diag.py`; 0.55 s, 59 MB; not a criterion, does not change the FAIL).
  - Method: central-difference Wirtinger split, h = 10⁻⁴, F(Y + htD) ≈ F + h(ta + t̄b). Report |b|/|a|, which is 0 for a
    holomorphic F. 10 samples each, m = 3.

  | N, y | X_0^ℂ max | φ^ℂ max | control (real map) max / min | control minus Ȳ |
  |---|---|---|---|---|
  | 2, 0.005 | 6.4e-10 | 6.9e-10 | 4.6e-07 / 1.2e-07 | 1.0 |
  | 2, 0.02 | 9.3e-10 | 2.3e-09 | 1.8e-05 / 9.3e-07 | 1.0 |
  | 2, 0.05 | 1.2e-09 | 1.2e-08 | 1.1e-04 / 1.1e-05 | 1.0 |
  | 3, 0.005 | 5.0e-10 | 1.1e-09 | 4.7e-04 / 1.3e-04 | 1.0 |
  | 3, 0.02 | 4.8e-10 | 8.9e-10 | 2.3e-03 / 2.4e-04 | 1.0 |
  | 3, 0.05 | 5.5e-10 | 7.4e-09 | 6.3e-03 / 3.2e-04 | 1.0 |

  - With the holomorphic leading term Ȳ removed, the control is maximally non-holomorphic (|b| = |a|).
  - The holomorphic objects sit at roundoff/truncation level (≤ 1.2·10⁻⁸). The control's own minimum is 10-10⁵ times larger.
  - So a properly designed test does discriminate, and it supports both X_0^ℂ and φ^ℂ. h7's forward-difference A3 did not:
    its φ value is truncation-dominated.

### What the control failure says about the test's power
- The control's non-holomorphic part is Π(K) - Π_0(½(K - Ǩ)), which is O(y²) in value. Its anti-holomorphic derivative is
  O(y) relative to the holomorphic leading term Ȳ (derivative 1).
  - So with y = 0.02 the forward-difference CR defect of the control is O(y) ≈ 10⁻⁴-10⁻² (observed median 3.4·10⁻⁴).
  - The pre-registered requirement "control ≥ 0.1" was impossible at this y. A3's design was wrong, not the lemma.
- **Power for X_0^ℂ.** The holomorphic defect, 5·10⁻⁹, is the O(h·|F''|/|F'|) truncation. It sits ≳ 800× below the control's
  minimum. So the test does separate the two, but only by comparing with the control's measured range, not by the
  pre-registered thresholds. Post hoc.
- **Power for φ^ℂ: essentially none.** φ^ℂ's defect, 4.3·10⁻⁴, lies inside the control's range (3.9·10⁻⁶ to 4·10⁻³).
  - The reason is that |∂φ/∂Y| ≍ |ρ|·|dA| is small (ρ = 0.02), so the forward-difference truncation h|φ''|/|φ'| is inflated.
  - The A3 φ-test cannot distinguish a holomorphic φ^ℂ from one with a relative O(10⁻³) anti-holomorphic part.
  - The central-difference diagnostic above can: φ^ℂ comes out ≤ 1.2·10⁻⁸ against the control's ≥ 10⁻⁷.
- **Conclusion.** The holomorphy of X_0^ℂ and φ^ℂ rests on the proof alone: uniform limits of holomorphic iterates, then
  composition with entire functions. I checked that proof and it is sound.
- **A discriminating test** would use central differences (O(h²) truncation) with the Wirtinger split b = ∂̄F·D̄, and report
  |b|/|a|. It would also test the control on F - Ȳ (removing the holomorphic leading term), or at larger y. My post hoc
  diagnostic does exactly this (above). It is not a criterion change and it does not alter the A3 FAIL.

---

## Corrected tally (session 4)

| Item | Claimed | Verdict |
|---|---|---|
| Lemma TERM-an | PROVEN-HERE, counted | CONFIRMED |
| Lemma NORM-an | PROVEN-HERE, counted | CONFIRMED (S4-4 wording; C_N existence-only) |
| Theorem AE-red | CONDITIONAL ⇐ (MS-Sob) | CONFIRMED (state η_AE as a function of C_S) |
| Theorem A5 | CONDITIONAL ⇐ (a5-G), (a5-U), (a3-q), (MS-Sob) | ARGUED: (a5-G) false as stated (S4-1); base-set gap (S4-2). CONDITIONAL ⇐ (a5-G♯) + (R♯) + (a5-U) + (a3-q) + (MS-Sob) after the restatement |
| POL, EXT | PROVEN, not counted | CONFIRMED |
| (R♯_∞) | PROVEN, not counted | CONFIRMED as an estimate; not the one NA-IFT needs (S4-1) |
| A5 (D), (c1''), (c5'') | PROVEN, not counted | CONFIRMED |
| (I_k^E)'' | HYPOTHESIS | Stated; inherits S4-1/S4-2; conflicts with (RLF-5)'s width as stated (S4-5) |
| h7 | FAIL (A3) as pre-registered | honest; reproduced identically; A3 has ~no power for φ^ℂ; the post hoc Wirtinger test supports holomorphy |

- **Session 4: 2 PROVEN-HERE (TERM-an, NORM-an) / 1 CONDITIONAL (AE-red) / 1 ARGUED (A5) + HYPOTHESIS (I_k^E)''.** The claim
  was 2/2/0.
- **Whole file: 11 PROVEN-HERE / 5 CONDITIONAL / 8 ARGUED / 4 OPEN + 1 HYPOTHESIS.** The claim was 11/6/7/4 + 1.
  - CONDITIONAL: RS-joint, HIST-sum, CLS-red, CLS-cone, AE-red.
  - ARGUED: the 7 after session 3, minus "(AE) ⇐ MSG + MS-Sob" (now AE-red), plus A5.
  - OPEN: (MS-Sob), (SQ-dev) incl. MSG-loc-dev, (D1-b), (H-w).
  - The new hypothesis items (a5-G♯), (R♯) (PROOF-owned), (a5-U) and (a3-q) are items of (I_k^E)'', and are not counted by the
    file's convention.
- **Targets.**
  - S6: MET in reduction form only after S4-1/S4-2. As written, its "not success" clause (a radius that depends on depth) is
    NOT avoided, because the radius's depth-uniformity rests on a false hypothesis.
  - S7: MET.

## Binding fixes (next lane-D session)
1. **S4-1.** Restate (a5-G) as PROOF's (G♯) in RTARGET §33's pair, at every ε_R-regular real critical chain, with D the
   level-k sup norm and the weights in level-k ancestor distance. Add (R♯) in the same pair as an OPEN hypothesis (PROOF/N2
   owner). Delete l.1666's parenthesis, demote (R♯_∞) to a remark, and record the ℓ^∞ lower bound ||𝓛⁻¹||_{∞→∞} ≳ L^{2(k-1)}
   (this review) as the reason. Re-label A5 CONDITIONAL on the restated list.
2. **S4-2.** Put (a5-U) and (a3-q) on R_{3ε_1} (or glue over R_{ε_1} and use 𝔇_{ε_1,α_E} in (b'')). Add s_5 ≤ ε_1/5. Fix the
   "(A)" citation in the openness step. Add the reality of Ψ_U(Z) for real Z, and M-1-M-3.
3. **S4-4.** NORM-an Reading and (d''): 𝔫_c has a linear fluctuation term O(y_bg)·|A| (lane F's source). The [inference]: the
   kernel is entire in V, not in the fine field; the width loss sits in the small-field restrictions (indicators and D_c(y_0)).
4. **S4-5.** (c3''): add the re-centring option (holomorphic critical branch of the frozen region) as the primary fix for
   (RLF-5)'s O(g/√κ). Keep the two-class option as the fallback. Use O(g√N/√κ).
5. **N-5.** MSG-loc': α_cell(b) := the max over the coarse cells meeting b's block pair.
6. **N-6.** (d'): the c-number of -log𝒩_c is +((N² - 1)/2)log(κu_k) + const.
7. **N-7.** §20.3 (B) size remark: η_AE ≈ 1.8·10⁻¹⁵ (C_S ≤ 10²), C_cone ≈ 10¹⁵. Write η_AE(C_S, ε_S) wherever it is
   propagated.
8. **h7.** Add a one-line post hoc note to §27 (no criterion change). The A3 φ-test lies inside the control's range, so it
   gives no evidence. A future h-check should use central-difference Wirtinger ratios (as in the reviewer's diagnostic).

## Strategic verdict
1. **AE-red is the session's solid gain.** (AE) is now exactly (MS-Sob), with explicit, depth-uniform constants, and the
   energy cap alone implies every-level smallness. The lane-D small-field classical chain is now:
   CLS-cone ⇐ CLS-red ⇐ AE-red ⇐ (MS-Sob) ⇐[ARGUED] (SQ-dev).
2. **TERM-an and NORM-an are real and reusable.** The exact Haar shift to the complex maximiser is the right tool, and it
   settles the kernel-normalisation width (g-independent).
   - Its natural extension is the re-centring cure for (RLF-5) (S4-5), which should go to whoever owns (RLF-5) now.
3. **A5 does not add independent progress on the analytic main term.** After S4-1 its hypotheses (G♯) + (R♯) at non-trivial
   critical chains ARE the B-NA wall (PROOF BNA-F2/F3: multi-scale Schauder + smooth gauge).
   - Lane D should not spend sessions on (a5-G♯). Its own items are (a5-U) and (a3-q). Both are classical, and (a3-q)'s linear
     case is the next concrete target.
4. **The constants are now extreme, and they compound.** A5 needs ε_1 ≤ ½√(η_AE/C_3) ≈ 2·10⁻⁸/√C_3. CLS-cone's per-defect price
   is then u_kε_1²/(2NC_cone) ≈ u_k·10⁻³¹/C_3.
   - That is depth-uniform, so it is valid for a proof. It also strengthens REVIEW_HIST_S3's recommendation: the lead should
     decide whether the main path needs the ENERGY form at all.
   - A per-scale sup pricing (MSG-type conditions at each level, as in Balaban CMP 109 (1.14)-(1.16)) would avoid (MS-Sob),
     η_AE and these constants entirely.
   - [inference; it needs the lead's reading of RLARGE §8 / PLD, as before.]
5. **Do not:** count A5 as CONDITIONAL before S4-1, treat (R♯_∞) as discharging (R♯), or read h7 A3 as evidence for φ^ℂ's
   holomorphy.
