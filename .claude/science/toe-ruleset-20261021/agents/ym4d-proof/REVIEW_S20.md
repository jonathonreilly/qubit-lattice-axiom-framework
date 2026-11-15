# REVIEW_S20: hostile review of session 20 (R1819 fixes; RW-ℓ²; N5-w0 in exact rationals; Theorem NAH1, Corollary N5-sf1, Proposition NAH-ind; LINEAR_PACKAGE v1.1; c36)

Reviewer: an independent agent that wrote none of the proof. I edited no other file. No commits, PRs or pushes.

Inputs:
- REVIEW_S18_S19.md (format; its 10 binding fixes).
- `diff PROOF_session19_snapshot.md PROOF_session20_snapshot.md`. PROOF.md is byte-identical to the session-20 snapshot
  (`cmp` empty). Read by offset: header l.1-40; N5 node l.2160-2165; tally l.4525-4537; RW l.5282-5313; N5-sf0 l.5348-5414;
  N5-sf_i l.5416-5428; N5-w0 l.5430-5455; the [S20] block l.5472-5795 in full.
- RLARGE.md: every `R1819` hit (l.101-113, 126-129, 389-394, 483-486, 625-634, 655-663, 855-858) and (SF) l.601.
- RTARGET.md §43 annotation, §44, §45. LOG.md session 20 (l.885-925).
- `diff LINEAR_PACKAGE_v1_snapshot.md LINEAR_PACKAGE.md` (all hunks); strip conditions spot-checked against
  PROOF_session16_snapshot.md l.2706-2735.
- checks/c36_criteria.md, c36_nah1.py (parts B, C read line by line), c36_consts.py, c36B_diag.py, all stored outputs,
  c36_time.txt. All re-run (Part 4), plus one reviewer diagnostic (kcurv.py, Part 4).

Scratch work (copies of the scripts, the lock-guarded runner, re-run outputs) is in the scratchpad directory `rev20/`.

---

## Bottom line

- **The R1819 fixes are applied, and correctly**, with three loose ends (none affects validity):
  - The N5 ↔ RLARGE threshold compatibility (RLARGE l.101-106) is now **stale in substance**. It still says
    the compatibility costs "astronomically larger, still g- and K-independent" constants. After session 20, the N5
    threshold at level i ≥ 1 is only known in the per-level form, which shrinks by ≈ 10⁻⁴⁰ per level (NAH-ind). RLARGE's
    thresholds are therefore K-independent only under (BG-unif). The note also says "recorded here and in (SF)", but (SF)
    (l.601) does not contain it.
  - The level-1 locality exception (walk terms not finite range) is missing from the header, the tally line and the
    [S20] N5 node status.
  - The W0-1 annotation's "same footing as the product-rule one" holds only at κ ≡ 1, L = 3, d = 4.
- **(R1-loc) is named precisely and labelled ARGUED** in (W1-ret') (d) (l.631-633) and §8.3 step 2 (l.657-662). RLF-step
  is recorded as CONDITIONAL also on (R1-loc) (l.858). Accepted.
- **W0-1 / c36 C: CONFIRMED. Lemma N5-w0's rate is now a genuine computer-assisted proof in exact arithmetic.**
  - Every entry is a Python `Fraction`. The zero pattern, the symmetry and both sums are exact. γ_0 is the exact rational
    PG value (1/(3.5·10⁶))·(½)/9, and the only transcendental step is replaced by analytic inequalities:
    e^x - 1 ≤ xe^x, and e^{20m} ≤ 1 + 40m for 20m ≤ 1.25.
  - No interval arithmetic is needed. I reproduced N_0 = 10462237/410670 and the first moment 449171/10935 exactly.
  - Scope: κ ≡ 1, L = 3, d = 4.
- **Proposition RW-ℓ²: CONFIRMED-WITH-FIX.**
  - The P-bound (Cauchy-Schwarz over the covering), the R-bound (Schur test on RW (i)'s symmetric entrywise majorant), the
    multiplicity count k ≤ 3 per direction and the sup-norm corollary are all right.
  - Fix: μ_𝒫 ≤ 3^d needs a **product** partition, whereas RW's Setting allows "or similar". For a general box partition
    with sides in [R, 2R), a volume count gives μ_𝒫 ≤ 5^d, i.e. /25 instead of /9.
  - Fix: N5-sf0's (RW1-n) also holds for complex backgrounds (by the Neumann series around the real symmetric K_0). Say
    so, because BR1 (v) uses 𝔠_∞'s sup-norm form at complex V.
- **Theorem NAH1 (with U0, FPq, N5-an♭, BR1, SC1, LOC) and Corollary N5-sf1: CONFIRMED-WITH-FIX (constants level).**
  - I re-derived the exact lift, the Kato/block-mean FP inverse, the contraction and its transversality constants, the
    Schur complement and LOC's two terms.
  - Four constants-level defects:
    - (i) α' = 2(α + r) can exceed N5-an♭'s r_♭/2;
    - (ii) LOC's margin ignores the entry range r_1;
    - (iii) the units of T are mixed;
    - (iv) "the largest ε such that" is not the right definition (non-monotone conditions).
- **(MIN_1) and the level-1 locality exception are correctly not hidden** in the theorem texts and in RTARGET §45. They are
  not repeated in the three summary places listed above (fix 7).
- **Proposition NAH-ind, and the 10⁻⁴⁰ per-level threshold loss: the loss is NOT intrinsic. It is an artefact of the
  estimate chain. A change of norm alone does not cure it; measuring curvature instead of displacement does.**
  - The 10⁴⁰ is constants: 𝔠_∞ ≈ 2·10³⁷ comes from the proven decay rate 10⁻¹⁰ and R_* ≈ 1.7·10¹².
  - The residual floor ≥ 36p_L/λ_min ≈ 10⁴, which the ledger calls "not a constants artefact", is an artefact of bounding
    the *new curvature* by triangle inequality through the *displacement* ||A*||_∞ ≤ ||C||·||∇f||.
  - The first-order curvature response 1 - dCd^* is an ℓ²-contraction (ΠOΠ ≥ (dΠ)^*dΠ gives 0 ≤ dCd^* ≤ 1), independent
    of λ_min.
  - Measured on c36 B's model (Part 4, kcurv), the true per-level amplification is ≈ 0.24 (fine curvature ≈ 0.12 ≈ 1/L²), not ≥ 10⁴.
  - The compounding itself is an artefact of composing per-level worst cases. The repair route and a precise (BG-unif)
    are given at the end.
- **(BG-unif) is named, not precisely stated.** It has no quantifier structure, no class, and no statement of which
  constants it hands NAH-ind. It also asks for more than is needed (L^{-2(k-j)} decay, where a level-independent C·ε
  suffices). It is ambiguous whether its proof may use the per-level covariances; if it may, it is circular with NAH-ind.
  A precise template is given below.
- **LINEAR_PACKAGE v1.1: errata only (verified hunk by hunk; no statement, constant or pointer changed). Fit for outside
  readers: YES**, with the companion snapshot. Three cosmetic items for a later v1.2 do not block release.
- **c36: honestly recorded.** B's failure at t = 0.15 is recorded as a FAIL, with no criterion edited. The diagnostic is
  labelled post-run and disclosed. One informational result (B4: a negative Schur-Hessian eigenvalue at t = 0.05) is not
  mentioned in the ledger and should be (it is not a defect).
- **Corrected tally: 72 / 2 / 7 / 24 + 1, as claimed.**

---

# PART 1: the R1819 fixes (REVIEW_S18_S19 binding fixes 1-10)

| # | Fix | Where now | Verdict |
|---|---|---|---|
| 1 | SF-1 R_g orientation | PROOF l.5388-5389, l.5419-5420 | **Applied correctly.** N5-cov gives Õ(gU, gV) = R_gÕ(U, V)R_g^{-1}, so K_{Ω_□} = R_g^{-1}(Õ(gU, gV))_{Ω}R_g and (NA-H_loc) uses R_gÕ_iR_g^{-1} = Õ_i(g_□U, g_□V). Both are now consistent with N5-cov |
| 2 | SF-2 gap sizes | header l.13-14, l.35-36; N5 node l.2162-2164; N5-sf0 l.5348-5356, l.5375-5376 | **Applied.** The numbers (7·10⁻⁸², 4·10⁻⁵¹ → 6.6·10⁻¹⁰) are reproduced by c36_consts (Part 4) |
| 3 | SF-3 existence theorem | N5-sf0 heading l.5349-5352; RTARGET §43 annotation (text above it not edited) | **Applied correctly** |
| 4 | SF-4, SF-5 | l.5371-5373 (ν_w), l.5378-5382 (holomorphy domain) | **Applied.** The SF-5 reading (open polydisc of radius r_* ≥ α_*, neighbourhoods of 𝔑(α) for α < α_*) is right |
| 5 | RW-1, RW-2 | l.5305-5313 | **Applied correctly.** The RW-2 inequality R ≥ R_* + (2/(aL))log(s̄/(2θ)) follows from ε_R(R) ≤ ½e^{-aL(R-R_*)/2} |
| 6 | W0-1 | l.5432-5439, l.5512-5516; c36 C | **Applied, and the label now holds** (Part 2). Scope note below (fix 11) |
| 7 | (NA-H_loc) presupposes the level-i minimiser | l.5425-5428 | **Applied** |
| 8 | RLARGE F1, F2, G5, compatibility, c_RS | RLARGE l.389-394 (F1), l.126-129 and l.483 (F2), l.631-633 and l.657-662 (G5 = (R1-loc)), l.101-106 (compatibility), l.113 (c_RS) | **Applied, with one loose end.** F1: the Lipschitz step gives C_♮ := max(3, 2 + C'C), which is correct. F2: T_k = T·L^{K-1-k} matches "a level-k cube = one level-(k+1) site". G5: (R1-loc) is named, ARGUED, and the three ingredients REVIEW_S18_S19 listed are stated. The compatibility note is now stale (below) |
| 9 | optional: γ_i doubles; M' | l.5127-5131; l.5142-5144 | **Applied correctly.** ⟨A_P, dλ⟩ = ⟨d^*A_P, λ⟩ = 0 since d^*A_P ∈ Λ_res^⊥ and λ ∈ Λ_res; the old γ_i values remain valid lower bounds |
| 10 | LINEAR_PACKAGE v1.1 | LINEAR_PACKAGE.md | **Applied** (Part 3) |

**Loose end on fix 8 (binding, fix 9 below). RLARGE l.101-106.**
- The note quotes N5-sf0's level-0 thresholds only and concludes "still g- and K-independent".
- RLARGE's small-field region is a level-k notion at every level k ≤ K. The package (SF)_k needs N5 at every level.
- After session 20, the level-k threshold is proven only in the per-level form ε_k ≲ ε_*(36p_L𝔠_∞)^{-k} (Proposition
  NAH-ind). The constants a'' ∝ ε_1² and n_♯ would then depend on K, which RLF forbids.
- So the compatibility condition is satisfiable with K-independent constants **only under (BG-unif)** (or any other
  level-uniform N5 threshold). That is a real dependence of RLF on N5's uniformity, not "only finiteness".
- Also: "recorded here and in (SF)" is false. (SF)_k (l.601-602) does not mention it.
- Fix: amend the note, and add "(with level-uniform thresholds)" to (SF)_k.

**N5 threshold compatibility, units.** RLARGE's ε_1 is an operator-norm cut ||1 - U_p||_op < ε_1, while N5 uses |log U_p|_HS.
"Matching units" should name the conversion (|log U|_HS ≤ √N·arcsin-type bound in ||1 - U||_op for ||1 - U||_op < 1). This
is cosmetic.

---

# PART 2: session 20

## Proposition RW-ℓ² (l.5486-5510): CONFIRMED-WITH-FIX

- **P(t).**
  - Each G_□(t)1_□f is supported in Ω_□, so pointwise |Σ_□g_□(x)|² ≤ #{□ : x ∈ Ω_□}Σ_□|g_□(x)|² by Cauchy-Schwarz.
  - Summing over x: ||P f||² ≤ μ_𝒫Σ_□||G_□1_□f||² ≤ μ_𝒫(γ' + t)^{-2}||f||², because 𝒫 is a partition. Correct.
- **R(t).** RW (i)'s proof gives the entrywise bound Σ_□|R_□|(x, y) ≤ (2S_m/(γ' + t))e^{-md(x,y)}1[d > RL].
  - It comes from Σ_z|K|(x, z)(2/(γ' + t))e^{-md(z,y)} ≤ (2/(γ' + t))e^{-md(x,y)}N_m(|K|).
  - For fixed (x, y) only the □ ∋ y contributes. The majorant depends on d only, so it is symmetric, and the Schur test
    gives the ℓ² bound by its row sum.
  - The row sum is ≤ (2S_m/(γ' + t))e^{-mRL/2}·4coth⁴(m/4) ≤ ε_R(t), by monotonicity in a ≤ m. Correct.
- **Gap.** (K + t)^{-1} = P(1 - R)^{-1} with ||R|| ≤ ε_R < 1, so for real symmetric K > 0, λ_min = ||K^{-1}||^{-1}
  ≥ γ'(1 - ε_R)/μ_𝒫^{1/2}. Correct.
- **Multiplicity.** x ∈ Ω_□ iff, in every direction, x_μ is within distance R of the interval I_μ(□).
  - The disjoint intervals of length ≥ R that meet a window of 2R + 1 points: the k - 2 inner ones lie in the window minus
    its end points, so (k - 2)R ≤ 2R - 1 and k ≤ 3.
  - The wrapped case gives ⌊T/R⌋ ≤ 3. Correct.
  - **But the product of the per-direction counts bounds μ_𝒫 only for a product partition** (each box a product of
    intervals from one-dimensional partitions). RW's Setting (l.5283-5284) reads "R - 1 boxes per direction of side R and
    one of side R + (T mod R), **or similar**". That is a product partition as written, and the "or similar" must be
    removed or restricted.
  - Note the typo: it should be ⌊T/R⌋ - 1 boxes of side R, not R - 1.
  - For general box partitions with sides in [R, 2R): every □ with x ∈ Ω_□ meets the ℓ^∞ ball of radius R about x, hence
    contains a side-R cube inside the ball of radius 2R. So μ_𝒫 ≤ ((4R + 1)/R)^d ≤ 5^d, and the gap is /25 instead of /9.
- **Sup-norm corollary (l.5508-5510).**
  - Σ_y|G_□|(x, y) ≤ n_Ω^{1/2}(Σ_y||G_□(x, y)||²_HS)^{1/2} ≤ ((N² - 1)n_Ω)^{1/2}||G_□||, using the N² - 1 rows of the block x.
  - N_0(|P|) ≤ μ_𝒫max N_0(|G_□|): only the □ with x ∈ Ω_□ contribute, and that number is μ, not μ^{1/2}, as written.
  - N_0((1 - R)^{-1}) ≤ (1 - ε_R)^{-1}. Correct.
  - The comparison "beats RW (ii) by ~10¹⁴" is reproduced: 3.95·10⁵¹ / 1.96·10³⁷.
- **ℓ² bound for 𝒞.** Σ_{b'}||𝒞(b, b')||²_HS ≤ (N² - 1)||𝒞||² and ||𝒞||² ≤ ||Õ^{-1}||. Correct.
- **Fix RW2-1 (binding).** State the product-partition hypothesis, or use 5^d.
- **Fix RW2-2 (binding, because BR1 (v) needs it).**
  - "Where it applies" restricts (RW1-n) to real backgrounds, but BR1 (v) and NAH1 (a) use 𝔠_∞ (whose minimum is the RW-ℓ²
    form) at complex V.
  - (RW1-n) does hold at complex backgrounds: ||(K_0 + t)^{-1}|| ≤ 1/(γ_0 + t) with K_0 the real symmetric compression of
    Õ(1, 1). Δ_□ is complex symmetric, so its block majorant is symmetric and ||Δ_□|| ≤ N_0(|Δ_□|) ≤ C_Δα_*. The Neumann
    series then gives ||(K_{Ω_□} + t)^{-1}|| ≤ 1/(γ' + t).
  - Only the λ_min statement needs reality. Add this sentence.

## Lemma N5-w0 in exact arithmetic, c36 C (l.5432-5439, l.5512-5516): CONFIRMED (genuinely computer-assisted)

I read part_C line by line (c36_nah1.py l.119-301).
- **Exactness.**
  - `norm = Fraction(1, 24·L^d)`, so the S4' weights w and the Q templates are Fractions.
  - ||w||² is a Fraction.
  - P_res (l.216-240) zeroes the centre and subtracts the mean over the L^d - 1 other sites (`m / nB`, Fraction). This is
    exactly the orthogonal projector onto {λ(c) = 0, Σλ = 0} = span(δ_c, 1_B)^⊥.
  - Π = 1 - ww^T/||w||² per block. d*d is integer.
  - So every row of Õ_0 = ΠO_0Π + (1 - Π) is exact. Zero entries are removed exactly (`add` pops exact zeros), so the
    support test and the sums use no tolerance.
- **What is proven.**
  - The 324 reference rows determine all rows by block translation.
  - C1: support inside the 3⁴ blocks, ℓ¹ base-point distance ≤ 11; ν_w = 30/13 exactly.
  - C2: symmetry on reference-block pairs. Symmetry also holds structurally: Π, d^*d, Q^TQ and dP_resd^* are each symmetric.
  - C3: N_0 = 10462237/410670 and M1 = 449171/10935.
  - C4: M1·m(1 + 40m) ≤ γ_0/2 at m = 193/10¹², and ≤ γ_0/4 at m_4 = 966/10¹³, as Fraction comparisons. γ_0 is the
    Fraction (1/3500000)(1/2)/9, which is exactly PG's proven c_1 = 1/(3.5·10⁶) (PROOF l.2670-2681) with c_E = ½ at i = 0.
  - The analytic steps are D_m = Σ|Õ|(e^{md} - 1) ≤ Σ|Õ|md·e^{md} ≤ m·M1·e^{11m} ≤ m·M1·(1 + 40m), because
    e^x ≤ 1 + 2x on [0, 1.256].
  - Block norms are scalars, because Õ(1, 1) = Õ_0 ⊗ 1. **No float enters the chain.** Interval arithmetic is unnecessary.
- **Reproduced exactly** (Part 4): the same two fractions, and C1-C4 PASS.
- **Residual trust.** The proof is as good as the code's transcription of O_0 = d^*d + κQ^TQ + dP_resd^* in the ledger's
  normalisation.
  - It agrees with c35's independent float matvecs to 1e-10 relative.
  - c35 A2 tied Õ(1, 1) = Õ_0 ⊗ 1 to the SU(2) model.
  - I checked the d*d, Q^TQ and fixing routines against the definitions (orientation conventions of `dd` and `fix`
    included). This is standard for a computer-assisted lemma, and acceptable.
- **Fix W0-2 (scope, binding).** The annotation's "N5-sf0's second threshold (≈ 1.7·10⁻²⁴/C_Δ) stands on the same footing
  as the product-rule one" holds at κ ≡ 1, L = 3, d = 4 only. The product-rule threshold is for general (κ_±, L). Add
  "(κ ≡ 1, L = 3)".

## Lemma U0 (l.5530-5550): CONFIRMED

- (i): in T^σ_y the two axial legs stay in B(X) and B(Y), and the straight leg crosses exactly one μ-face, so every
  transporter equals V_c and M̄_c = V_c.
- (ii): plaquettes with one crossing direction give V_cV_c^{-1} = 1. At a corner, the four crossing links are the four
  links of V_P.
- (iii): covariance is right.
- (iv): the Wilson gradient bound is right. Re tr(XW) = ½tr(X(W - W^†)), so |Re tr(XW)| ≤ |X||(W - W^†)/2|_HS ≤ |X||log W|
  (Σsin²θ ≤ Σθ²). Each link lies in 6 plaquettes. The soft term is stationary at the lift.
- c36 A re-run identical.

## Lemma FPq (l.5552-5568): CONFIRMED

- **(i) Kato.** |D_Uλ| ≥ |d|λ|| per link (Ad orthogonal). |λ| vanishes at the centres. The Dirichlet-at-centre grid gap
  applies on in-block links.
- **c_D.** I re-ran c36_consts: an exact LDLᵀ of Lap - (2663/31250)·1 has all pivots positive, so c_D(3) > 0.085216. The
  Dirichlet Laplacian is built correctly (degree counts include edges to the centre).
- **(ii) block mean.**
  - M_1M_1^* = (L^d - 1)L^{-2d} per block.
  - ||M_U - M_1|| ≤ η_ML^{-d/2} (Cauchy-Schwarz over L^d sites).
  - The transport length is d(L - 1)/2 = 2(L - 1) at d = 4, so η_M = e^{4(L-1)α_b} - 1. Weyl applies.
  - The two-case argument checks out with ||D|| ≤ 2√d used consistently in the case split, and gives
    K_FP = max{24.3, 514.5} = 514.5.
- **Cosmetic.** BR1 applies FPq at U^(0), whose block-interior links are exactly 1 (Lemma U0). So α_b = 0, and "≤ 3(L - 1)ε
  by AX" (l.5606) is unnecessary.

## Lemma N5-an♭ (l.5570-5581): CONFIRMED as an existence statement (same composition argument as N5-an, reviewed)

## Lemma BR1 (l.5583-5623): CONFIRMED-WITH-FIX

- **Contraction.**
  - C_0Π_0O_0x = x on ker h_0.
  - Φ(A) - Φ(A') = C_0Π_0∫[Hess f(0) - Hess f(A_s)](A - A').
  - Lip ≤ 𝔠_∞C_♭r = 12𝔠_∞²C_♭ε ≤ ½, and ||Φ(0)||_∞ ≤ 6𝔠_∞ε_V (U0 (iv)), so r = 12𝔠_∞ε maps the ball into itself.
  - The radius conditions r ≤ r_♭/2 and links ≤ r_♭/6 are each in ε_br. Correct.
- **Transversality (ii).** I re-derived each step:
  - ⟨(ν, -μ), 𝔉λ⟩ = 0, from ⟨D_0P_0D_0^*A*, τλ⟩ = ⟨ν, P_0D_0^*τλ⟩;
  - 𝔉 = -χ_0dexp^{-1}D_{U(V)}, which is -χ_0Γ_0 at A* = 0;
  - ||χ_0|| ≤ ||h_0|| + ||D_0|| ≤ √(2(L - 1)) + 2√d = 6 at L = 3;
  - ||dexp^{-1} - 1|| ≤ 0.5847·|ad_A| ≤ 1.2r, since z/(1 - e^{-z}) - 1 has coefficient sum 1/2 + 1/12 + 1/720 + … < 0.59;
  - ||D_{U(V)} - D_0|| ≤ 3.5r√d, since each site heads d links;
  - total ≤ 6·(1.2r·2√d + 3.5r√d) ≤ 72r ≤ 1/(2K_FP). Correct.
  - dim Λ equals the dimension of χ_0's target, so injective implies onto.
- **(iii).** ε' = ε + max(4r, 3p_Lr) = (1 + 36p_L𝔠_∞)ε. Correct.
  - Non-degeneracy modulo 𝒢_V: on the complement ker h ∩ ker P_resD^* of D_UΛ, ⟨v, F_AAv⟩ = ⟨v, Ov⟩ ≥ λ_min||v||², and
    F_AA kills D_UΛ at a critical point. Correct.
- **(iv), (v).** Correct, given fix RW2-2: for complex V, 𝔠_∞'s sup-norm form needs (RW1-n) at complex backgrounds. Without
  it, (v) holds with the coth⁴ form of 𝔠_∞ (≈ 4·10⁵¹), i.e. a smaller ε_br at complex V.
- **(MIN_1).** It is named, and E_1^br ≠ E_1^NA is kept separate throughout (l.5619-5620, 5723, 5792). Correctly not hidden.
  - Suggestion: the RG needs the background only on the small-field set, where RLARGE handles the complement. So (MIN_1)
    can be weakened to "U(V) is the unique minimiser of F(·, V) among U with (U, V) in the level-0 small-field class",
    which is the form Balaban uses (CMP 102b). That is a local statement plus a convexity argument on the class, not
    global uniqueness on SU(N)^links.
- c36 B (t = 0.05) re-run identical.

## Lemma SC1 (l.5625-5641): CONFIRMED

- E'' = g_BB + g_Baa' with g_aaa' = -g_aB.
- g_aB ⊥ D_UΛ: F(·, e^BV) is 𝒢-invariant for every B, so the orbit-directional derivative vanishes at a = 0 for all B.
- ker F_AA = D_UΛ, via admissibility and Õ > 0.
- The representative x ∈ ker h ∩ ker P_resD^* solves Ox = -g_aB, so x = -Cg_aB.
- Independence of the fixing weight and of the slice follows (they change x by D_UΛ).
- c36 B2 and B3 and D1 re-run identical.

## Lemma LOC (l.5643-5657): CONFIRMED-WITH-FIX

- **(i).** M_{m_1}(ABC) ≤ N(A)N(B)M(C) gives 8coth⁴(a/2)/γ' · e^{m_1r_1}C_Δα' · 2/γ_0 = A_inα'. Correct.
- **(ii).** Every term of K^{-1}(K - K^♮)(K^♮)^{-1} has z or z' outside Λ''.
  - Splitting e^{-m_1d} and summing gives 2·c_K·4coth⁴(m_1/4)·N_0·(2/γ')e^{-m_1D/2} = 16(…).
  - The stated A_out (32(…)) is conservative. Correct.
- **Fix LOC-1 (binding, constants).** Two hypotheses must be satisfied when LOC is used:
  - "Λ'' ⊃ Λ', the links whose entries' variables are inside the gauge box";
  - "b, b' at distance ≥ D from every link outside Λ'".
  - In NAH1 (b) (l.5697-5698) LOC is applied with Λ' := Λ'' = all level-0 links in the blocks of Λ_1. But entries Õ(b, b')
    with b within ≈ r_1 + 3L of the edge of Λ'' have variables outside the gauge box.
  - The "-4" margin in Λ_1's central part (2 level-1 units = 2L level-0 units each side) is smaller than r_1 = 8L - 4.
  - Fix: take Λ' := Λ'' minus a collar of width r_1 + 3L, and the central part of side ℓ_1 - 2⌈(D + r_1 + 3L)/L⌉ - 4.
    This changes only ℓ_1 by O(1).

## Theorem NAH1 (l.5659-5714): CONFIRMED-WITH-FIX

- **Bookkeeping.** I re-derived δ_Sch's four terms.
  - ΔF_BB: C_♭α'.
  - ΔF_BA·C·F_AB + F^0_BA·C·ΔF_AB: 2·(C_♭α'/2)·4c_Ccoth⁴·S_F.
  - F^0ΔCF^0: the A_in and A_out terms.
  - The far part: S_F²c_Ke^{-m_1(Ld_1 - 16L)}, summed at rate μ_1 - m ≥ μ_1/2.
- **Other steps.** The level-weight conversion e^{md_1} ≤ e^{16m}e^{(m/L)d_0} and N_{m/L}(|C|) ≤ 4c_Ccoth⁴(m_1/4) are
  right. The product formula for δ_H^{(1)} is right.
- **Asymptotics.** ρ(ε), D(ε) = O(log 1/ε) gives α' = O(ε log 1/ε) and δ_H^{(1)} → 0. This holds because the exponential
  terms are set to O(ε) by the choice of ρ, D, and log n_ρ = O(log ρ). The constant is astronomically large but finite.
- **(a)-(c)** follow. NAH1-F1/F2/F3 do not occur, as claimed. FPq is background-uniform, the lift is exact and global, and
  LOC localises.
- **Fix NAH1-1 (binding).** N5-an♭'s deviation bound "(2S_♭/r_♭)α for (u, v) of size α ≤ r_♭/2" is applied with α' = 2(α + r).
  - ε_H's conditions give α ≤ r_♭/6 and r ≤ r_♭/2, hence α' ≤ 4r_♭/3, which is outside the r_♭/2 polydisc.
  - Either measure the deviation in N5-an♭'s own chart (A, u) = (A*, log U^(0) link), where |u| ≤ α ≤ r_♭/6 and
    |A| ≤ r ≤ r_♭/2 are both inside, and replace C_♭α' by C_♭max(α, r).
  - Or add α'(ε) ≤ r_♭/2 to ε_H's conditions.
- **Fix NAH1-2 (binding).** Fix LOC-1 above (margin).
- **Fix NAH1-3 (notation).** T means the level-1 side in level-1 blocks in N5-sf0 (Ω^+ spans ≤ 4R_* + 5 < T_0 blocks), but
  in NAH1/N5-sf1, T ≥ ⌈ℓ_1/L⌉ + 1 and T ≥ 4R^{(1)} + 6 only make sense for the level-2 side. Name the units (the same issue as
  REVIEW_S18_S19's F2).
- **Fix NAH1-4 (binding wording).** "ε_H := the largest ε ≤ ε_br such that …" (l.5674) and "ε_*^{(1)} := the largest ε ≤ ε_H
  with …" (l.5717). The conditions are not monotone in ε (ceilings in ρ(ε), D(ε)), and the theorem is stated for every
  ε ≤ ε_H. Define ε_H := sup{ε' ≤ ε_br : the conditions hold for every ε ≤ ε'}. This is positive because every condition
  holds for all small ε.
- **Scope.** The class change 𝔑_1(α) → 𝔅_1(ε) and E_1^NA → E_1^br are both stated (l.5682, l.5660). The locality exception is
  stated in N5-sf1 (l.5720-5721). Correct as far as it goes.

## Corollary N5-sf1 (l.5716-5723): CONFIRMED (counted with NAH1)

- CT♯ with ||Δ_□|| ≤ δ_H^{(1)}, then RW and RW-ℓ², exactly as in N5-sf_i.
- The locality exception is honest. But the same exception is absent from the header (l.14-16), the tally line (l.4532)
  and the [S20] N5 node status (l.5791-5795): fix 7.

## Proposition NAH-ind (l.5725-5765): CONFIRMED as an implication (not counted). Its *reading* is overstated: see the strategic verdict

- The recursion for ε_{i+1} and C_♭^{(i+1)} follows from BR1/SC1 run with (I_i).
- "γ_i = γ_1 for all i ≥ 1" is right (N5-triv).
- The statement l.5754-5758, "This is not a constants artefact … the sup-norm Newton step used here costs N_0(|C|) ≥ ||C||
  = 1/λ_min per level", is true of *this estimate chain* and false as a statement about the problem. Reword (fix 8).

## Constants table (l.5767-5783): CONFIRMED arithmetic

All entries are reproduced by c36_consts and c36 D, and the measured rows are labelled measured:
- 2c_E = 0.00814, γ_0 = 1.5873·10⁻⁸, γ_1 = 1.2917·10⁻¹⁰;
- 𝔠_∞ = 1.96·10³⁷ (N5-w0) and 1.33·10⁵³ (product rule);
- 1 + 36p_L𝔠_∞ = 7.77·10³⁹;
- the RW-ℓ² gap 6.61·10⁻¹⁰;
- γ_meas ratio 0.9966; the proven/measured ratio 3.08·10⁸.

The level-1 RW-ℓ² gap "≈ 5·10⁻¹²" is 6.6·10⁻¹⁰·2c_E = 5.4·10⁻¹² if γ'_1/γ_1 = γ'/γ_0. Write "≥ γ_1/36 = 3.6·10⁻¹²" for the
proven floor (from γ'_1 ≥ γ_1/2, ε_R ≤ ½).

## (BG-unif) (l.5759-5765): named, NOT precisely stated

What is missing:
- (a) quantifiers: for which k, T, and which class of top fields;
- (b) which objects: the tower of level-j critical points (branch values E_j^br at every level, or the composite minimiser);
- (c) which constants it delivers to NAH-ind. These must replace BR1's ε_{i+1} ≤ ε_i/(1 + 36p_L𝔠_∞^{(i)}) and the
  C_♭^{(i+1)} recursion;
- (d) that its proof must not use the per-level covariances C^{(j)} as Newton inverses. Otherwise it is NAH-ind again.

It also demands own-units curvature O(L^{-2(k-j)}) at level j. That is true for smooth backgrounds but not needed: a
level-independent C_BG·ε suffices.

Precise template:

> **(BG-unif).** There are ε_BG > 0, C_BG < ∞, m_BG > 0 and T_BG, depending only on (N, L, κ_±), such that for every k ≥ 1,
> every torus with level-k side ≥ T_BG and every level-k field V_k (complex neighbourhood of radius ε included) with own-units
> plaquette logs and level-(k+1) soft fluctuations ≤ ε ≤ ε_BG, there is a tower U_{k-1}, …, U_0 with U_j a critical point of
> F_j(·, U_{j+1}) (U_k := V_k), unique in the composite slice ball of sup-radius C_BG·ε about the composite lift, such that
> for every j < k:
> - (i) own-units plaquette logs of U_j and soft fluctuations ρ(U_j, U_{j+1}) are ≤ C_BG·ε;
> - (ii) U_j is holomorphic in V_k on the neighbourhood with the same bound;
> - (iii) |∂U_j(x)/∂V_k(y)| ≤ C_BG·e^{-m_BG·d_j(x, y)};
> - (iv) the N_0-Lipschitz constants of Hess E_j^br in the chart at the lift are ≤ C_BG.
>
> The proof is by one contraction for the composite functional, whose linearisation is the composite operator of
> Theorem N2-lin / Proposition BG-b-lin (uniform C_R, C_f), not by iterating BR1.

Then (I_i) holds with ε_i ≡ min(ε_BG, ε_*/C_BG) and C_♭^{(i)} ≤ C_BG, uniformly in i. That is exactly what NAH-ind needs.

---

# PART 3: LINEAR_PACKAGE v1.1

- **Errata only: CONFIRMED.**
  - I read every `diff` hunk against v1:
    - the header;
    - §0 (BG-b row: ε_1, B_LF; Phys at n = L; Phys^{(k)}; ||·||_B);
    - the §4 strip-conditions paragraph (checked against PROOF_session16_snapshot l.2706-2735: (P5) ρ_β, (P6) e_Ψ,
      (P7) br_V are as summarised);
    - §6 wording; §9 (Z_ref pointer, unread-papers list, the dated status note); §11 bibliography; §12 change log.
  - No statement, constant, proof or line pointer changed. All eight REVIEW_S18_S19 Part 3 items landed.
- **Fit for outside readers: YES**, shipped with PROOF_session16_snapshot.md as the document says. Remaining items are
  cosmetic. They do not mislead, and can wait for a v2:
  1. The "Review status" paragraph (l.14-17) lists reviews up to REVIEW_S16_S17. Add "REVIEW_S18_S19 (v1 → v1.1 errata)".
  2. The v1.1 status note in §9 points to "PROOF.md [S18]-[S19]" (a live, moving file). Point to PROOF_session19_snapshot.md.
  3. The Z_ref pointer goes to RLARGE.md (RLF-4), a working file whose own definition defers to node A. One phrase
     saying what Z_ref is meant to be (a reference normalisation at the same cutoff) would be self-contained.

---

# PART 4: checks (re-run)

Setup:
- Copies of c36_nah1.py, c36_consts.py and c36B_diag.py (diag re-pointed to the copy) in scratchpad `rev20/`, so nothing
  was written into `checks/`.
- Each job: `until mkdir …/locks/numeric; do sleep 20; done`, then a wait for load (1-min) < 8, the job, and `rmdir` exactly
  once (no trap); nice 10; OPENBLAS/OMP/MKL/vecLib threads 1; PYTHONDONTWRITEBYTECODE = 1; no `timeout`; python without -I.

Load (1-min) was 2.2-3.7 and free memory 35-37% before each job. A first attempt at D failed on import because I had not
copied c35_n5bg.py; it was re-run after copying it. That was my error, not the check's.

| Part | Result | Time | Peak (footprint) | vs stored |
|---|---|---|---|---|
| c36 C (exact rationals) | PASS: N_0 = 10462237/410670, M1 = 449171/10935, ν_w = 30/13, dmax 11, C4 both inequalities | 9 s | 181 MB | identical (timing only) |
| c36 A (exact lift) | PASS: 7.53e-14, corners 0.0, 3.16e-16, 4.98e-14 | 2 s | 25 MB | identical |
| c36 D (level-1 Bloch) | PASS: D1 9.7e-14, 0.030950; γ_meas(1) = 0.03971196, γ_meas(0) = 0.03984916, ratio 0.9966 | 89 s | 959 MB (< 1 GB) | identical (timing only) |
| c36 B (d = 2 branch + Schur) | **FAIL**, the same as stored: t = 0.05 B1-B3 hold (B2 ≤ 2.1e-7; B4 -0.003808); t = 0.15 diverges to nan, LinAlgError at B4 | 262 s | 32 MB | identical (timing, paths) |
| c36_consts | c_D > 2663/31250 certified; K_FP 514.475; 𝔠_∞ 1.96e37 / 1.33e53; gaps 4.05e-51, 7.00e-82 → 6.61e-10 | 0.4 s | 19 MB | identical |
| c36B_diag (post-run) | converges at angles 0.147, 0.296, 0.512, (0.596 slowly); diverges at 0.781 | 25 s | 26 MB | identical |

**Reviewer diagnostic kcurv.py (mine; not a c36 criterion; scratchpad `rev20/kcurv.py`, output `kcurv.out`).**
- Setting: c36 B's d = 2 SU(2) model (L = 3, coarse 2 × 2, κ = 1), run at the converged critical branch U(V).
- Ratios measured against ε_V = max coarse |log V_P|:
  - K_p = max fine |log U_p| / ε_V;
  - K_ρ = max |ρ_c| / ε_V;
  - K_A = max|A*| / ε_V.

| background | ε_V | lift K0 | K_p | K_ρ | K_A |
|---|---|---|---|---|---|
| random, t = 0.005 (2 seeds) | 0.018 | 1.000 | 0.117-0.121 | 0.194-0.202 | 0.221 |
| random, t = 0.02 | 0.071 | 1.000 | 0.117-0.121 | 0.194-0.203 | 0.221 |
| random, t = 0.05 | 0.18 | 1.000 | 0.117-0.121 | 0.195-0.203 | 0.221 |
| one excited coarse link, t = 0.01, 0.1 | 0.01, 0.1 | 1.000 | 0.118 | 0.236 | 0.222 |

Reading:
- The lift carries the full coarse curvature on its corners (K0 = 1, as Lemma U0 says).
- The critical branch spreads it: **K_p ≈ 0.12 ≈ 1/L² = 0.111**, and K_ρ ≈ 0.2-0.24. Both are flat in ε_V, so this is the
  linear regime.
- The true one-level amplification of (curvature, soft fluctuation) is therefore ≈ 0.24 < 1. The proven chain's factor is
  1 + 36p_L𝔠_∞ ≈ 8·10³⁹, and ≈ 10⁴ even with 𝔠 = 1/λ_min. Displacement is also small: K_A ≈ 0.22, against the bound
  12𝔠_∞ (≥ 300 at true constants).
- Caveats: d = 2, a 2 × 2 coarse torus, measured only. The d = 4 number is the c37 target recommended below.

**Honesty of the record.**
- B's FAIL at t = 0.15 is recorded as FAIL with the residual sequence, and no criterion was edited (criteria mtime
  20:01 < script 20:14 < outputs).
- c36B_diag.py (20:44) post-dates c36B.out (20:38), and is labelled "post-run diagnostic, disclosed, not a criterion" in
  c36_time.txt and the ledger.
- The pre-run change of B's re-solve (Newton → preconditioned contraction) is disclosed.
- c36_consts.py also post-dates the runs. It is labelled informational except c_D, which it certifies exactly (re-run:
  the exact LDLᵀ holds). The ledger calls it "scratch consts.py" (l.5554). It is checks/c36_consts.py: fix the pointer.
- **Not reported in the ledger:** B4 at t = 0.05 printed "Schur Hessian on the complement of coarse gauge directions: min
  nonzero eigenvalue -0.003808".
  - This is not a defect. H_1(V) = Hess E_1^br at a non-critical V need not be ≥ 0. At V = 1 its kernel includes the
    toron (constant) directions of the coarse 2 × 2 torus besides the gauge ones, and a non-flat V splits them at O(t²)
    (t² = 0.0025).
  - Õ_1's positivity comes from the κ_1 soft term, which B4 does not include.
  - But an informational result of a pre-registered check should be reported. Add one line.
- "B FAIL as pre-registered" (l.5623, l.5786) reads as if the failure had been predicted. Write "B FAIL (criterion
  pre-registered)".

---

# Overclaims

1. **PROOF l.5754-5758, LOG l.909-910, header l.18-19:** "not a constants artefact … set by the sup-norm Newton step,
   N_0(|C|) ≥ 1/λ_min". The ≈ 10⁴ floor belongs to the displacement/triangle-inequality estimate. The true per-level
   curvature amplification is < 1 in the tested model (Part 4). Fix 8.
2. **RLARGE l.104-106:** "still g- and K-independent". This is now conditional on level-uniform N5 thresholds ((BG-unif)).
   Fix 9.
3. **PROOF l.5438-5439:** "same footing as the product-rule one". True only at κ ≡ 1, L = 3. Fix W0-2.
4. **PROOF l.5492:** μ_𝒫 ≤ 81 "for the partitions of Theorem RW". True only for product partitions. Fix RW2-1.
5. **Header, tally, N5 node:** level-1 N5 without the locality exception. Fix 7.
6. **Imported items.** None is load-bearing for an S20 PROVEN claim. CMP 102 is cited for (BG-unif) only, as context [P].

# Verdict counts and tally

**Counted items (S20).**
- Theorem NAH1 with Lemmas U0, FPq, N5-an♭, BR1, SC1, LOC and Corollary N5-sf1: **CONFIRMED-WITH-FIX**. The fixes are
  NAH1-1 to NAH1-4, LOC-1 and RW2-2. All are constants or notation, and none affects validity.
- 0 GAP, 0 WRONG.

**Uncounted items.**
- Proposition RW-ℓ²: CONFIRMED-WITH-FIX (RW2-1, RW2-2).
- Lemma N5-w0 exact redo: CONFIRMED, now computer-assisted (fix W0-2, scope).
- Proposition NAH-ind: CONFIRMED as an implication; its reading is overstated (fix 8).
- (BG-unif): named, not precise (template above).
- The R1819 edits: applied (Part 1).
- c36: re-run as tabulated.

**Corrected tally: 72 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path)
+ 1 comparison branch, as claimed** (71 confirmed by REVIEW_S18_S19, + 1 NAH1). N5 stays OPEN.

# Required fixes (binding for the next session)

1. **NAH1-1:** N5-an♭'s polydisc. Use the (A*, u) chart with C_♭max(α, r), or add α' ≤ r_♭/2 to ε_H.
2. **LOC-1 / NAH1-2:** a collar of width r_1 + 3L in Λ', and ℓ_1's margin enlarged accordingly.
3. **NAH1-3:** state the units of T in NAH1/N5-sf1 (level-2 side) against N5-sf0 (level-1 side).
4. **NAH1-4:** ε_H, ε_*^{(1)} as sup over ε' such that the conditions hold for all ε ≤ ε'.
5. **RW2-1:** product partitions in RW's Setting (drop "or similar"; ⌊T/R⌋ - 1, not R - 1), or 5^d in RW-ℓ².
6. **RW2-2:** (RW1-n) at complex backgrounds (Neumann series), as used by BR1 (v) and NAH1 (a).
7. **Locality exception** (level-1 walk terms not finite range; H_1 localised by LOC only) added to header l.14-16, tally
   l.4532 and N5 node l.5791-5795.
8. **NAH-ind reading** (l.5751-5758, l.5780-5783, LOG l.909-910, header l.18-19): "NAH1-F4 occurs for this estimate chain.
   The 10⁴⁰ is constants (𝔠_∞). The residual 36p_L/λ_min floor is an artefact of bounding curvature by displacement. Not
   shown to be intrinsic. The measured per-level amplification is < 1 (REVIEW_S20 Part 4)."
9. **RLARGE l.101-106:** the compatibility now needs level-uniform N5 thresholds ((BG-unif)). "Recorded in (SF)" is false:
   add it to (SF)_k l.601 or delete the clause.
10. **W0-2:** the scope (κ ≡ 1, L = 3, d = 4) of "same footing".
11. **c36 record:** B4's informational line (the negative Schur-Hessian eigenvalue, with its explanation); "FAIL (criterion
    pre-registered)"; the consts.py pointer (l.5554 → checks/c36_consts.py).
12. **(BG-unif):** replace the prose with a precise statement (template in Part 2), including the no-circularity clause.
13. **Optional:** (MIN_1) weakened to small-field-class uniqueness (Balaban's form); FPq at U^(0) has α_b = 0; the level-1
    gap floor γ_1/36; LINEAR_PACKAGE Part 3 items 1-3 at the next version.

---

## Strategic verdict: the Newton-step threshold loss, and the route to uniformity in K

**Verdict: an artefact of the proof, not of the problem. But it is fatal for the per-level induction as written. No norm
change alone repairs it; the repair is a curvature-to-curvature estimate.**

The loss factor 1 + 36p_L𝔠_∞ comes from three things multiplied together. Each is removable, or absent in truth.

1. **𝔠_∞ ≈ 2·10³⁷ instead of ≈ 25: constants.**
   - 𝔠_∞ is the sup-norm bound on C. It is huge because the proven decay rate is 10⁻¹⁰ (so coth⁴ ≈ 10⁴²) or the
     partition is R_* ≈ 1.7·10¹² (so n_Ω^{1/2} ≈ 10²⁷).
   - At the measured constants (gap 0.04, decay ≈ 0.43) it would be O(10-100).
   - This part *is* the c_1 / decay-rate lever: a sharper rigorous rate removes ~35 of the 40 orders.
2. **The 1/λ_min ≈ 25 floor: an artefact of measuring displacement, not curvature.**
   - BR1 bounds the new background's curvature by triangle inequality: ε + 4r and ρ ≤ 3p_Lr, with r = 12||C||_∞ε. This
     costs ||C|| ≥ 1/λ_min, in every norm, because the operator norm is at least the spectral radius. So a weighted or
     energy norm alone **cannot** remove it, and an ℓ² norm is worse (extensive).
   - But the quantity that matters is the curvature of U(V) and its soft fluctuation, not the displacement.
   - To first order (abelian linearisation), the lift's curvature is F_0 (corner plaquettes), ∇f(0) = d^*F_0, and
     A_1 = -Cd^*F_0. So the new curvature is **F_1 = (1 - dCd^*)F_0** and the new soft fluctuation is ρ_1 = -QCd^*F_0.
   - Since ΠOΠ ≥ (dΠ)^*(dΠ) and ΠOΠ ≥ κ(QΠ)^*(QΠ) on the slice, 0 ≤ dCd^* ≤ 1 and ||QCd^*|| ≤ κ^{-1/2}.
     **Both responses are ℓ²-bounded by O(1) whatever λ_min is.** The soft low modes that make λ_min small are exactly
     those that d (and Q) barely see.
   - This is not yet a sup-norm bound: the sup-norm version needs the ℓ¹ rows of these kernels, i.e. a decay rate. But
     it shows that 1/λ_min is not the right size of the response.
   - Measured: on c36 B's model, the per-level amplification of max curvature is ≈ 0.12 ≈ 1/L², and of the soft fluctuation
     ≈ 0.2-0.24 (Part 4, kcurv; d = 2, measured only). The proven chain claims ≥ 10⁴ even at true constants.
3. **The compounding: an artefact of composing per-level worst cases.**
   - Even with a sharp per-level constant K, the per-level induction gives ε_k ≥ ε_0K^{-k}. That is uniform iff K ≤ 1
     (with the O(ε) non-linear corrections absorbed, which needs K < 1 strictly).
   - The linear composite map is uniformly bounded (Theorem N2-lin's C_R). So even if the one-level sup-norm K exceeded 1,
     the composite would not compound.

**Repair route (in order).**
- **(R-a) The one-level curvature lemma (session-scale; decides whether the per-level route can work at all).**
  - Replace BR1 (iii)'s triangle inequality by: max|log U(V)_p|, max|ρ_c(U(V), V)| ≤ K_curv·ε_V + C_2ε_V².
  - K_curv is the ℓ^∞ → ℓ^∞ norm of the linear abelian background map (coarse curvature) ↦ (fine curvature, soft
    fluctuation) at the trivial background.
  - C_2 is the second-order remainder. This is where 𝔠_∞ and C_♭ enter, but only multiplied by ε².
  - First measure K_curv in d = 4, L = 3 (Bloch/FFT, as in c36 D). If K_curv < 1 with margin, the per-level induction
    closes with ε_{i+1} = ε_i·(1 - K_curv)/(C_2-dependent), i.e. *uniform*, because the C_2ε² term is absorbed for ε below
    a level-independent threshold.
  - For a rigorous K_curv one needs a rigorous ℓ¹ bound on the response kernel: a computer-assisted decay estimate at the
    true rate. That is harder than c36 C (the kernel is not finite range), but it is finite-dimensional in Bloch form.
  - Also replace the C_♭^{(i+1)} recursion by a bound on the second-order remainder of the same form.
- **(R-b) If K_curv ≥ 1, or its rigorous version is out of reach: (BG-unif) in the precise form above.**
  - One contraction for the composite functional, with the composite linear operator (N2-lin/BG-b-lin, uniform constants)
    as the inverse.
  - This is Balaban's route (CMP 95/96/102b), and the non-linear part needs only second-order remainders about the linear
    composite background.
  - It is paper-scale, but it is the standard route, and NAH-ind then needs nothing more.
- **Not recommended:** further per-level steps (level 2, …) in the current displacement form. They will reproduce the 10⁴⁰
  per level by construction. A sharper PG constant alone is also not recommended: it removes (1) but not (2) or (3).

**Next session, recommended.**
- The binding fixes above, which take under a session.
- Then (R-a)'s measurement of K_curv in d = 4 (a c37 with criteria first: K_curv on the trivial background, per-mode and
  real-space; pre-register "K_curv < 1").
- Then, depending on the result, (R-a)'s lemma or (R-b).
