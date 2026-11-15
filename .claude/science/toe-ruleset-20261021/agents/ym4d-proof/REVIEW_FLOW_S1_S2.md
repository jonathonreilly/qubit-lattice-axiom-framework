# REVIEW_FLOW_S1_S2: hostile review of lane C sessions 1-2 (FLOW.md: coupling flow (F), UNIV-1L, bare-coupling tuning)

Reviewer: an independent agent that wrote none of FLOW.md. I edited no other file. No commits, PRs or pushes.

Inputs (read-only):
- FLOW.md, all 798 lines, read by offset.
- FLOW_LOG.md.
- checks f1-f5b: criteria, scripts (the criteria-evaluation blocks), outputs, time files, and file birth/mtime metadata.
- PROOF.md: L4a-flow, L4a-Π, L4b (l.1099-1174); Prop. LF-count (l.4097-4126).
- RLARGE.md: §0, §1, §1A (l.40-135); Lemma RS (l.316-361); §7.1 LF-n and the R-8 definitions (l.366-380); §7.2 (iv) (l.470-483).
- REVIEW_PLD_S1_S2.md: PLD-AF and B6 (l.267-290, 480-481).
- REVIEW_S18_S19.md (format).
- PLD.md: the uses of (F) (grep; l.190-202 read).

Re-runs: f1-f4 under the numeric lock, with nice 10 and 1 thread, writing to the scratchpad `revflow/` (results in
§6). I did not re-run f5/f5b (863 s and 641 s); their outputs and criteria code were read.

---

## Bottom line

- **Session 1's exact tree-level results stand.** I re-derived these:
  - F-tree: no tree-level renormalisation, for every κ > 0, every odd L ≥ 3 and every depth, by induction on the
    alias recursion.
  - F-bg: the aliases are O(p³).
  - F-ren: renormalised terms stay renormalised.
  - F-tel: exact telescoping.
  - F-depth: λ' ≤ L^{-2}, by the Poisson alias sum.
  - F-Π: the Cauchy constant C_Π.
  - F-flow, F-tune: the shooting argument, step by step.

  F-split is **WRONG as stated** (session 2 says so itself) and should leave the count.
- **The normalisation is exact (F-norm: CONFIRMED).**
  - u = 1/g_k² = β_Wilson = 2N/g_std².
  - L4b's 1/g_std²(μ) = 1/g_0² − (11/3)N(16π²)^{-1}ln(Λ²/μ²) gives d(1/g_std²)/d ln μ = 22N/(48π²) = 11N/(24π²) = 2b_0,
    with b_0 = 11N/(48π²) (the standard β(g) = −b_0g³ = −(11N/3)g³/(16π²)).
  - So β_0^std = 2N·2b_0 = 11N²/(12π²) per log L. Numerically this is 0.092878N², 0.37151 for SU(2) and 0.83590 for
    SU(3).
  - The sign is right. Coarsening μ → μ/L lowers 1/g_std² by 2b_0 log L, so β_k = u_k − u_{k+1} > 0.
  - The instanton cross-check aβ' = 11N/3 holds in both normalisations.
- **The UNIV-1L chain is a genuine reduction, but less of it is closed than §20 says.**
  - U-tad, U-dec, U-pair, U-res and U-red are right.
  - U-Tay is right up to a garbled statement.
  - U-cov-IR is right as an *undifferentiated* propagator bound. **It does not give (R-a) for the propagator.** (R-a)
    concerns the p²-coefficient integrand, which contains external-momentum derivatives of C_n, and each derivative
    of the Dirichlet factors costs a factor ~ℓ. The parenthetical "(it holds for the propagator by Lemma U-cov-IR)" in
    (U-IR)(a) is a GAP. (U-IR-s) is not precisely stated.
- **(F) quantifier and PLD-AF: consistent, but the hand-off text must carry B6.**
  - FLOW proves (F_R) only along the chain's own effective sequence (Def F-g). There β_+ ≥ β_0^std = β_1 and
    β_- → β_1 as γ → 0, which is exactly B6's admissible quantifier.
  - However, §4 cites (RLF-δ) from RLF's "every coupling sequence obeying (F)" statement, which B6 shows is false as
    quantified.
  - The §10/§19A suggested RLARGE wording also omits the quantifier.
- **§19A's "single place that is literally false" is wrong twice over.**
  - (a) "1/g_i² ≥ 1/g_{i+1}²" is *not implied* by (F_R). It is not false, and it holds wherever b_i > C_ργ².
  - (b) It is not the single place. RLARGE §7.2 (iv) ("g_j ≤ g_K by (F)") and PLD.md Corollary PLD-fin
    ("0 < g_0 ≤ g_1 ≤ … ≤ g_k (the order (F) gives)", l.194) rely on the same monotonicity.
- **Lemma F-R's "iff" is only an "if".**
- **§10's claim that (F) with R = 0 needs the depth corrections to be small at n − j = 1 is false.** RLARGE's β_± are free
  constants, and Lemma F-R (i) supersedes it, but §10 is not annotated.
- **Check provenance for f1 cannot be verified, and the log's correction time is contradicted by the filesystem.**
  - All four f1-f4 criteria files have birth = mtime = 23:12:50 UTC, all at the same second (a re-write, e.g. `sed -i`).
  - That is after f1_tree_soft.py was created (23:09:26) and after both f1 runs (output created 23:11:40, last write
    23:12:38).
  - FLOW_LOG says the header times were corrected "at 23:18". The headers say "23:07 UTC [file mtime]", which is not
    the mtime of the current files.
  - f2-f4 criteria (current bytes) do predate their scripts. f5 and f5b ordering is verified.
  - The pre-registered f1 (F) FAIL was kept and the post-hoc F' is labelled. That is evidence against a favourable
    edit, but the ordering claim for f1 is not verifiable.

---

## 1. Priority 1: F-tree, F-tel, F-ren/F-bg, F-split + U-dec + U-pair, F-depth

### Lemma F-tree (l.209-227): CONFIRMED
- **Recursion.** Ĝ_{k+1} = κ^{-1}P_⊥ + 𝒬(Ĝ_k) is the Schur/Gaussian formula. Fine gradients map to coarse gradients
  (Q_root∘d = d∘ev), so a longitudinal residual is free. f1 (B) re-confirms it.
- **K = 0 term.** L^{-4}·|Q̃_0|²·Ĝ_k(p/L) ≈ L^{-4}·L²·L²P_⊥/|p|² = P_⊥/|p|². The phases and the projectors agree at
  leading order (P_T(p/L) and P_⊥(p) have the same direction).
- **K ≠ 0 terms.** q_K ≡ 0 mod 2π iff p ≡ 0, so (a) propagates. The bound at step k+1 on |p| ≥ δ uses (a) at step k
  on |q| ≥ δ/L, and (a) is assumed for every δ.
- **Conclusion.** The conversion from (b) to β = 1 via L4a-Π (Ĥ = β|ŝ|²P_⊥ + O(p⁴), invertible on the transverse
  space) is right. The quantifiers "every κ > 0, odd L ≥ 3, every depth" are honest: the induction is on k, and κ and
  L enter only through the K ≠ 0 bounds.
- **Scope note (not a defect).** f1 tests one step (Ĝ_0 → Ĝ_1) only; depth is covered by the proof alone.

### Lemma F-bg (l.229-240): CONFIRMED
- Stationarity gives κr = Ĝ_{k+1}^{-1}b, which is O(p²).
- For K ≠ 0 the straight Dirichlet factor in a direction α with K_α ≠ 0 vanishes at p_α = 0. This holds for the leg
  factor, (e^{ip_μ} − 1)/(e^{iq_μ} − 1), and for the transverse averages.
- So a_K = O(p)·O(p²) = O(p³). Also a_0 = L^{-1}b(1 + O(p)).

### Lemma F-ren (l.242-260): CONFIRMED-WITH-FIX
- The alias bookkeeping is right.
  - A fine-translation-invariant F has no K ≠ K' cross terms.
  - The K ≠ 0 terms are O(p⁶).
  - The K = 0 term gives c·β[F], with a universal factor c from the Fourier normalisation.
- **Fix FR-1.** The bracket at l.260 says (i) with β[F] ≠ 0 "is used only for F = 𝒯_j". That is false after session 2:
  Corollary U-red uses β[F∘Φ_0] = β^fine[F̄] for F = Γ^{W0}_n, with β ≠ 0.
  - It is still correct, by calibration rather than by trusting the L^{-4}·L⁸ factor.
  - The K = 0 limit is the same linear functional c·β[F] for every admissible F.
  - (iii) with F = 𝒯_j (β = 1, kernel term O(p⁴)) forces c = 1.
  - State this, and delete the bracket.

### Lemma F-tel (l.263-272): CONFIRMED-WITH-FIX
- The block-tridiagonal Schur/envelope induction is right. The FP and 𝒩'_1 factors are additive. The step from
  β[Γ_k + b_k𝒯_{k+1}] = 0 to β[Γ_k∘Φ] = −b_k via F-ren (ii), (iii) is right.
- **Fix FT-1.** F-tel applies F-ren to the *per-step* Γ_k. That needs Γ_k to be C² with an exponentially local Hessian.
  Γ_k's Hessian contains D³𝒯_k(1) and D⁴𝒯_k(1), i.e. D²Φ and D³Φ of the earlier tower.
  - These are explicit implicit-function compositions of the proven-local linear inverse (N2-exp) with explicit vertex
    tensors, so they are very likely derivable.
  - But they are not written. As §4 says, this is (SF-bg) at the trivial point.
- Hence §21's "(SF-bg) is no longer needed for the one-loop coefficient" is true for B_n (the composite route, U-tad).
  It is not true for the per-step b_k = −β[Γ_k] that Def F-g and Prop. F-rem use, nor for the identity B_n = Σb_k.
  - Narrow the statement, or prove the finite-order derivative locality at 1 by the implicit function theorem (a
    session-scale lemma).

### Lemma F-split (l.273-283): WRONG as stated; superseded by Prop. U-dec
- **Prop. U-dec (l.549-571): CONFIRMED** (at the Laplace level of the lane).
  - (i): Laplace on ∫K_comp dV = 1 at order u⁰ gives Λ(U_0, 𝔪) = ½log det(2π𝒞/u). Right.
  - (ii): eliminating the intermediates at fixed (U_0, V) is right. With U_0 fixed, an intermediate gauge transformation
    must extend to U_0, so there is no intermediate degeneracy. The level-0 𝒩'_1 factor sits inside Λ, consistently.
  - (iii): the averaging map is nonlinear even for U(1) (averages of phases and the polar part). So "affine" means the
    linearised Gaussian. That wording is fine.
- F-split omits Γ^dr for SU(N) (indeed for any non-affine averaging map). It is WRONG as a statement and only its β-level
  consequence survives, via U-pair.
  - **Fix FS-1:** remove F-split from the PROVEN-HERE count. Keep it as "superseded by U-dec (β-level content via
    U-pair)".
- **Lemma U-pair (l.573-595): CONFIRMED-WITH-FIX.**
  - (1): from (b) and (c), ξ(1^g) = 0, so Dξ(1) kills exact forms. Hypothesis (a) is never used.
  - (2): the curvature of DΦ_0v is O(p). Its aliases are O(p³). r̂ = O(p²).
  - (3): the point inversion about a level-n site is in B_4. It acts by +1 on Λ², with no colour action (orientation
    reversal gives X ↦ −X on links), and by −1 on Λ¹. So Ŵ(0) = 0 and Ŵ(p) = O(p).
  - The K ≠ 0 aliases give O(p⁵).
  - **Fix UP-1.** Applications (1) and (3) also need the O(|r|²) remainders of Γ^dr and Γ^W to be bounded bilinear forms
    with analytic (exponentially local) symbols. Only then is their Hessian O(p²)·O(p²). This is not in (U-loc) as
    stated: add it.
  - **Fix UP-2.** Drop (a), or say it is unused. "Uniformly in n" in (U-loc) is not needed for β[Q] = 0 at each n. It
    is harmless.

### Lemma F-depth (l.309-323): CONFIRMED
- Poisson: Σ_K|φ(q_K)|² = L⁴Σ_r|Σ_{w≡r}c_we^{ipw/L}|². The straight average has weight L^{-3} per residue class, so the
  sum is ≤ L⁴·L⁴·L^{-6} = L² and Λ ≤ L^{-2}.
- The operator sandwich, the boundedness of Δ_0 (the phase matching of Λ_pŝ(p/L)) and the honest FAIL of the
  pre-registered unprojected f1 (F) line are all right. The post-hoc λ' = 0.1067 ≤ 1/9 is correctly labelled.

### Lemma F-Π (l.142-158): CONFIRMED
- 16 (cubes per link) × 6400^{n−1} (shapes) × 4M⁴n (b_z) × (Mn)² × α^{-2} gives 64M⁶α^{-2}Σn³(6400e^{-κ_p})^{n−1}.
- The two-variable Cauchy estimate is right.
- For κ_p ≥ 457, 6400e^{-457} ≈ 10^{-194.7}, so the sum is ≤ 1 + 10^{-193}. Right.

### Lemma F-id (l.160-172): CONFIRMED
- Internal consistency check: for F = Σs, Q = ½Σ(Φ^a)² = (1/(2N))||Φ||²_HS, so c̄ = 1/(2N) and β = 2Nc̄ = 1 = β[Σs].
- The factor L^{-4} in RLARGE's δβ_k is RLARGE's, as the lemma says.

---

## 2. Priority 2: Lemma F-norm (l.502-521): CONFIRMED

Re-derived:
- **Plaquette expansion.** 1 − N^{-1}Re tr e^{iX} = tr X²/(2N). With X = a²F^aT^a and tr T^aT^b = δ/2,
  s = a⁴F^aF^a/(4N).
- **Sum over plaquettes.** Σ_{μ<ν} = ½Σ_{μ≠ν}, so uΣs → (u/(8N))∫ΣF^aF^a. Set equal to (4g_std²)^{-1}∫ΣF^aF^a, this gives
  u = 2N/g_std².
- **Lie coordinates.** t_a = i√(2N)T^a has −(1/N)tr(t_at_b) = δ_ab, ||t_a||²_HS = N and s(e^X) = ½Σ(X^a)². Right.
- **LF-count.** Its Balaban normalisation, with the normalised trace, is the same as RLARGE's.
- **Conventions, to be exact.**
  - b_0 = 11N/(48π²) is the coefficient of β(g) = μdg/dμ = −b_0g³.
  - d(1/g_std²)/d ln μ = +2b_0 = 11N/(24π²).
  - d u/d ln μ = 2N·2b_0 = 11N²/(12π²) = β_0^std.
  - The brief's "11N²/(12π²) = 2N × 2b_0" holds with 2b_0 = 11N/(24π²). It is NOT 2N × b_0.
- **Fix FN-1 (pointers).** The PROOF line numbers cited are stale:
  - "PROOF l.4089" (§0) and "l.4106-4109" (§15) are now l.4114-4116.
  - §19A's "l.4091-4102" is now l.4103-4106.
  - L4b is at l.1162-1174.

---

## 3. Priority 3: the UNIV-1L chain

### Lemma U-tad (l.531-547): CONFIRMED
- Global-colour invariance gives DF(1) = 0, since su(N) has no Ad-invariant vector. The chain rule then kills
  𝔉_U[D²Φ(v, v)].
- The listed functions are equivariant (M̄, P, k̃, 𝒩'_1, the slice). The tower is equivariant by uniqueness.
- Minor: "the Hessian at an arbitrary configuration" must be taken in an equivariant chart (e.g. exponential
  coordinates about each link value). That is implicit; say it.
- So B_n is determined by Gaussian data, DΦ (linear, proven) and explicit vertex tensors. U-F1 does not occur for B_n.
  For the per-step b_k, see FT-1.

### Corollary U-red (l.597-606): CONFIRMED, given (U-loc) and FR-1
- For ℓZ⁴-periodic, fully gauge-invariant F, the K = 0/K' ≠ 0 cross terms are O(|q_0|)·O(p³)·O(p) → no marginal part,
  and the K = 0 diagonal is the translation average.
- The normalisation c = 1 is by the FR-1 calibration.

### Lemma U-res (l.608-628): CONFIRMED (all constants re-derived)
- The four pieces give A, π²A (∫_{1/ℓ}^∞r^{-3} = ℓ²/2 times 2π²), 4π⁴A (BZ ⊂ B_{2π}), 2π²A log π, and A(2π)⁴π^{-4}, so
  c_UA = A(2π)^{-4}(1 + π² + 4π⁴ + 2π²log π + 16) ≈ 0.28A.
- The rate form's change of variables and the tail ∫_{|Q|≥πℓ}|φ_∞| ≤ Aπ²(πℓ)^{-2} are right.
- Remark (2) (routing independence via surface terms) is right at the level stated.

### Lemma U-Tay (l.632-648): CONFIRMED-WITH-FIX
- **Fix UT-1.** "σ_h = −β_0^std/(log of the scale ratio)" is dimensionally garbled. The proof and Theorem UNIV use
  σ_h·log ℓ = −β_0^std n log L with ℓ = L^n, i.e. **σ_h = −β_0^std** (u-units, per unit log ℓ). Correct the statement.
- **Fix UT-2.** "Apply Lemma U-res once more in the continuum" needs a continuum version of U-res (R⁴, with a UV
  regulator in place of the BZ boundary). The proof is the same split, but U-res as stated is a BZ lemma. Say "the same
  split on R⁴".
- The arithmetic is right. With ln(Λ²/m²) = 2ln(Λ/m), (11/12)N(16π²)^{-1}·2·4 = 11N/(24π²) = 2b_0, and F-norm gives
  β_0^std.
- The heat-kernel input is L4b (IMPORTED-AND-REVERIFIED, c2). The decomposition 11/12 = −1/12 (Ω²) + 1 (E²) matches the
  standard 11/3 = −1/3 + 4.

### Lemma U-cov-IR (l.650-662): CONFIRMED as stated; its advertised use is a GAP
- Re-derived:
  - Woodbury: (H_0 + 𝔪^T𝒞^{-1}𝔪)^{-1} = g − g𝔪^†(𝒞 + 𝔪g𝔪^†)^{-1}𝔪g, and 𝒞 + 𝔪g𝔪^† = Ĝ_n.
  - Ĝ_n ≥ 𝒞_n ≥ κ^{-1}P_⊥.
  - |D_ℓ(θ)| ≤ π/(ℓ|θ|) (sin(θ/2) ≥ |θ|/π).
  - max|q_α| ≥ |q|/2, and ω̂ ≥ 4|q|²/π².
  - Together these give (π⁶/4)κℓ^{-4}|q|^{-6} and the relative bound π⁴κ(ℓ|q|)^{-4}.
- **GAP UC-1.** (U-IR)(a) says "(it holds for the propagator by Lemma U-cov-IR)". It does not.
  - (R-a) is a bound on the p²-coefficient integrand, which contains first and second external-momentum derivatives of
    C_n(q + k, q + k), or of g(q + k), at k = 0 (f3's analytic differentiation).
  - For ℓ|q| ≥ 1 each q-derivative of D_ℓ is ~1/|θ|, i.e. ℓ|q| times larger relative to D_ℓ.
  - So ∂²(C_n − g) is only ≲ ℓ^{-2}κ|q|^{-6}·(…). That still fits the ℓ^{-2}|q|^{-6} form of (R-a), but needs:
    - derivative bounds on the Dirichlet factors;
    - uniform-in-n bounds on the coarse-momentum derivatives of P_⊥Ĝ_n(P)^{-1}P_⊥ (F-depth gives sup-norm convergence
      only, not derivatives);
    - the off-diagonal alias entries.
  - **Fix:** state U-cov-IR' (derivatives up to order 2: |∂^α(C_n − g)| ≤ Cκℓ^{-4+|α|}|q|^{-6+|α|}, |α| ≤ 2, |q| ≥ 1/ℓ)
    as an open, session-scale lemma. Delete the parenthetical claim.

### Theorem UNIV (l.664-689): CONFIRMED-WITH-FIX (the implication is right; the hypotheses need precision)
- Given (R-a)-(R-c), U-res + U-Tay + (U-IR)(c) give |B_n − β_0^std n log L| ≤ c_UA + A_cov. Right.
- Notation: R_0 should read c_U·max(A_IR, A_Tay) + A_cov, as the line below the theorem says.
- **Are the hypotheses precise?**
  - **(U-loc): nearly.**
    - Add UP-1, the O(r²) remainders.
    - Define ξ' explicitly, including "the slice and FP pieces", which is currently only gestured at.
    - With these it is a precise statement about explicit trivial-background objects. It is session-scale: per-level
      N5-triv locality plus U-dec's explicit Λ.
  - **(U-IR): not yet precise.**
    - J_n, "the ℓ-averaged p²-integrand of Γ^{W0}_n", is the integrand of a functional that is only ℓZ⁴-periodic. The
      way the ℓ⁴ alias pairs are folded into one BZ integrand, and the loop-momentum routing, must be fixed in the
      definition, as f5 does. The UV comparison object J_* is BF-Feynman gauge, while Γ^{W0} uses FP-ab's slice. The
      "sparse" difference is put inside (a) without a definition of what "sparse" means for the integrand.
    - (b) and (c) are precise.
    - As written, (a) bundles four different estimates:
      - the propagator derivatives (UC-1);
      - the IR-term vertices;
      - the slice modification;
      - the longitudinal sector.
      They should be stated separately, (a1)-(a4).
  - **(U-IR-s): GAP (imprecise).** "The scaling form of Lemma U-res with ε_{ℓ_n} ≤ A_sθ^n" must specify three things:
    - an n-independent profile φ_∞ and n-independent J_*;
    - that J_n = J_* − ℓ⁴φ_{ℓ}(ℓq) + E_ℓ, with the n-dependence only in φ_ℓ − φ_∞ and E_ℓ;
    - **a separate rate hypothesis for β[Γ^cov_n] → c_cov.** UNIV-rate's proof says "Γ^cov_n is included in
      φ_ℓ/E_ℓ", but Γ^cov is not part of the J_n integral.

### Corollary UNIV-rate (l.693-700): GAP (hypothesis), arithmetic right given a precise (U-IR-s)
- The proof is right *given* a correctly stated (U-IR-s) (c_∞ cancels in B_{n+1} − B_n).
- **Fix UR-1.** The f2 diagnostic "|slope − 1|·ℓ_mid² ≈ 0.27, 0.27, 0.26, 0.25, 0.25 for κ_c = 1" is mislabelled. Those
  are the κ_c = 0.25 values (0.0076·36 = 0.27, …, 0.0013·196 = 0.255). For κ_c = 1 they are 0.60, 0.58, 0.56, 0.56,
  0.55.
- **Fix UR-2.** §20's "|slope − 1|·ℓ_mid² → 0.168, 0.392, 0.804 … i.e. the ℓ^{-2} approach" overstates. In f5b the
  products are still falling (κ_c = 1: 0.541 → 0.392; κ_c = 4: 1.288 → 0.804). The data are consistent with
  O(ℓ^{-2}) as an upper rate, but do not show ℓ^{-2}. Say "consistent with".

---

## 4. Priority 4: the remainder C_ρ and the tuning theorem

### Proposition F-rem (l.351-356): CONFIRMED-WITH-FIX
- The bound |ρ_k| ≤ C_ΠE_2g_k² + g_k⁶ ≤ C_ρg_k² is right.
- C_ρ = C_ΠE_2 + 1 depends only on the (SF-g) constants (E_2, α, κ_p, M), which are uniform in k, K and T by
  hypothesis. So C_ρ is uniform in K and volume, as claimed.
- **Fix FR-2 (sign).** (SF-g) writes 𝒮^{LF}_k = −δβ_k𝒯_{k+1} + …, so β[𝒮^{LF}] = −δβ_k. The proof (l.354) and §6.1 (d)
  use +δβ_k. One of them must change, and must be matched to RLARGE's g̃_k convention ("(F) shifted by Σδβ_i"). This is
  harmless for |ρ_k|.

### Theorem F-flow, Corollary F-ll (l.358-369): CONFIRMED (conditional as labelled)
- R = 2R_0 comes from two applications of UNIV-1L.
- β_0'/2 ≤ β_- ≤ β_+ ≤ 3β_0'/2.
- In F-ll, g_k² ≤ 1/(u_n − R + β_-(n − k)log L) and Σ1/(a + bm) ≤ (1/b)log(1 + bM/a), plus the extra 1/a. Right.

### Theorem F-tune (l.373-397): CONFIRMED (conditional as labelled)
I checked each step:
- **Step 1.** g_0 ≤ g_* gives u_{k+1} ≥ γ^{-2} + β_+(K − k − 1)log L.
- **Step 2.**
  - The left limit at g_0^♯ uses continuity on 𝒜_{k−1}, and all s < g_0^♯ lie in 𝒜.
  - The right neighbourhood is built inductively in k (finitely many levels).
  - So some k* has g_{k*} = γ.
- **Step 3.** u_K ≤ γ^{-2} + R = g_1^{-2} ≤ g^{-2}.
- **Step 4.** The intermediate value theorem on (0, g_0^♯] ⊂ 𝒜. The smallest root exists.
- **Step 5.** The bounds follow from F-flow on [k, K].

Uniformity in K and volume holds given (SF-∞) and Def F-g's infinite-volume β. No monotonicity is used. FL-F4 does not
occur.

### Lemma F-ind (l.399-405): CONFIRMED-WITH-FIX
- R_0 = c_U·A + A_cov depends on trivial-background data only. β_- := β_0'/2 and R are fixed first, then C_ρ, then γ.
  There is no circularity in the constants.
- **Fix FI-1 (level-locality; binding).** The induction closes only if (SF-g)_k and (RLF-δ)_k at level k use the flow on
  [0, k] only.
  - RLF's statement involves g_K, the final coupling (Σ_k|δβ_k| ≤ Ce^{-a/g_K²}, LF-n with 1/g_i² ≥ 1/g_K² + …).
  - FLOW consumes only the per-level |δβ_k| ≤ g_k⁶.
  - F-ind must state that this per-level bound is derived (in RLARGE's (I_k) → (I_{k+1}) induction) from (F_R) on
    [0, k] for the chain's own sequence. That is a requirement on lane RLARGE. Record it in §4 and in the hand-off.
- **Fix FI-2 (PLD-AF/B6 consistency; binding).**
  - FLOW's own results are quantified correctly. F-flow and F-tune concern the chain's own sequence g_k(g_0), for which
    β_+ = β_0' + C_ργ²/log L ≥ β_1 = β_0^std and β_- = β_0' − C_ργ²/log L → β_1 as γ → 0. This is precisely B6's
    "(F) with β_- ≥ β_1 − o(1)". So FLOW is consistent with PLD-AF: no sequence with β_+ < β_1 is ever claimed.
  - But two places are not:
    - (a) §4 (RLF-δ) cites RLARGE §1A (RLF-0), whose quantifier "every coupling sequence … obeying (F)" B6 shows false.
      FLOW must consume the requantified form ("along the chain's own effective sequence, given (F_R) on [0, k]").
    - (b) The suggested RLARGE wording (§10, §19A) "(F_R): β_-(k − j)log L − R ≤ … + R" must carry B6's quantifier:
      "for the chain's own effective sequence (Def F-g)".
- **Note.** F-ind's β_- := β_0'/2 is only a lower bound used for constants. It is not a restriction of the class of
  sequences, so it does not conflict with B6.

---

## 5. Priority 5: §19A, the R note, and Lemma F-R

### Lemma F-R (l.702-710): CONFIRMED-WITH-FIX
- (i): if inf b_k > C_ργ² then R = 0. Right.
- (ii): if b_k ≤ 0 then u_k − u_{k+1} ≤ C_ργ². Right, but the quantifier order is: for each β_- > 0, failure once
  C_ργ² < β_- log L.
- (iii): right as an "if".
- **Fix FRR-1.** §19A (l.715) and §20 say "R = 0 iff every b_k > C_ργ²". Only "if" is proven. The gap
  0 < b_k ≤ C_ργ² is undecided, because ρ_k may have either sign.
  - The correct statement: "for some γ > 0, (F) with R = 0 holds if min_k b_k > 0 (given UNIV-rate, a condition on
    b_0, …, b_{k_0−1}); it fails for small γ if some b_k ≤ 0."
  - (iii)'s "iff" likewise.
- **Fix FRR-2.** §10 (l.409-411) says that (F) with R = 0 "would need |B_n − B_j − β_0'(n − j)log L| small at n − j = 1".
  That is false: RLARGE's β_± are free positive constants, and R = 0 needs only inf_k(b_k + ρ_k) > 0. Lemma F-R (i)
  supersedes it. Add an [S2] pointer at l.409.

### §19A consumer map: CONFIRMED-WITH-FIX
- The quotes checked against RLARGE are accurate: §0 (F), RS l.354-355, R-8 l.375, §7.2 (iv) l.482, LF-n l.366-368.
  The quotes from PROOF (LF-count l.4103-4106) are also accurate.
- **RS's monotonicity.** "1/g_i² ≥ 1/g_{i+1}²" is *not false* under (F_R). It is *not implied* by (F_R). By F-flow's own
  proof, u_i − u_{i+1} = b_i + ρ_i ≥ b_i − C_ργ², so it holds at every level with b_i > C_ργ² (all i ≥ k_0, given
  UNIV-rate). The repair factor (e^{a_RS R})^{n/c_RS} is right.
- **Fix RN-1.** Replace "literally false" with "not implied by (F_R)". It is also **not the single place**:
  - RLARGE §7.2 (iv) ("g_j ≤ g_K by (F)") uses the same monotonicity. The table row gives its repair, but the summary
    contradicts the table.
  - PLD.md Corollary PLD-fin (l.194) assumes "0 < g_0 ≤ g_1 ≤ … ≤ g_k (the order (F) gives)". PLD.md is missing from the
    map altogether. Its (F) uses are l.194, l.199 and l.208-209, plus l.392, where the upper half gets + R. Add a PLD row.
- **Fix RN-2.** The (P2) row has the polynomial bound with β_-. It must be β_+, since an upper bound on
  u_k = g_k^{-2} uses the upper half: g_k^{-6} ≤ (1/g_K² + β_+(K − k)log L + R)³.
- The other rows are right: §7.2 (iv) g_j² ≤ g_K²/(1 − Rg_K²), LF-n C → Ce^{aR}, X-NTAF's G_m positivity, and LF-count.
  "No consumer needs R = 0" stands.

---

## 6. Priority 6: checks

### Provenance (file birth/mtime, local −04:00 converted to UTC)

| file | birth | mtime | ordering |
|---|---|---|---|
| f1_criteria.md | 23:12:50 | 23:12:50 | **after** f1_tree_soft.py (born 23:09:26) and after f1_out (born 23:11:40, last 23:12:38) |
| f2/f3/f4_criteria.md | 23:12:50 | 23:12:50 | before f2 (23:13:22), f3 (23:14:54), f4 (23:15:47) scripts ✓ |
| f5_criteria.md | 23:39:11 | 23:39:23 | before f5_cov_kernel.py (23:56:21) ✓ |
| f5b_criteria.md | 00:01:16 | 00:01:16 | before f5b_quad.py (00:01:42) and before f5 finished (00:10:49) ✓ |

- **Finding CK-1 (record defect).** The four f1-f4 criteria files were re-created in one operation at 23:12:50 UTC.
  - FLOW_LOG l.8-9 says the header correction happened "at 23:18". The filesystem says 23:12:50.
  - Each header says "written 23:07 UTC [file mtime]", which is not the mtime of the current bytes.
  - For f1 the current bytes postdate the script and the first run. So "criteria before scripts" is **not verifiable**
    for f1.
  - The content shows no favourable editing: the pre-registered (F) line is kept and FAILED, and F' is labelled
    post-hoc.
  - **Fix:** a FLOW_LOG line recording the true re-write time, and that f1's criteria bytes postdate the f1 runs. Use
    `cp`/append in future, never `sed -i`, for criteria files.
- **f5 (A) and f5b (S) are roundoff FAILs.** Both are recorded honestly.
- **f5 (C) and (D) are FAILs.** Both are recorded. f5b was pre-registered after them and before f5's (E)-(G) were
  printed (consistent with the timestamps).
- **f5b (C') FAILs** for κ_c = 0.25 and 1. Recorded honestly.

### Fidelity of the reported numbers
- f1, f2, f3, f4, f5 and f5b outputs match FLOW §12/§20 (slopes, constants, ratios), with three exceptions:
  - **Fix CK-2.** "f5's κ_c = 0.25 values were off by up to 9%" (§20, FLOW_LOG). At ℓ = 3 the difference is
    0.0039405 vs 0.0035032, i.e. **12.5%**. It is ≈ 9.5% at ℓ = 5. The absolute offset is ℓ-independent
    (4.34-4.38·10⁻⁴), so the slope agreement claim stands.
  - The f2 κ-label (UR-1).
  - The f5b rate wording (UR-2).
- The f5 (G) threshold (|s^K·48π²| ≤ 0.05) is loose next to the measured 10⁻³ values. The script does evaluate it
  (l.346). The κ_c = 4 kernel-vertex slope is still 0.0016 at (11, 13), falling slowly from 0.0026. That is consistent
  with "no log", but not decisive at this ℓ.

### Re-runs (scratchpad revflow/, numeric lock held once, nice 10, 1 thread)
- Lock acquired 00:42:50 UTC (load 3.5), released once at 00:43:37 UTC.
- f1, f3 and f4: every PASS/FAIL line is byte-identical to the stored outputs. f1 (F) FAILs again at 2.3033; F' is
  0.10670.
- f2: identical except for the wall-clock stamps. All slopes match to the printed digits.
- Resources: 18 s / 50 MB, 23 s / 108 MB, 4.6 s / 40 MB and 1.9 s / 28 MB respectively.
- f5 and f5b were not re-run (cost). Their criteria-evaluation code (f5 l.336-351, f5b l.109-114) implements the
  pre-registered lines.

---

# Verdict counts and tally

**Counted items (FLOW §21 claims 21 PROVEN-HERE).**
- **Session 1.**
  - CONFIRMED: F-Π, F-id, F-tree, F-bg, F-depth, F-flow (+ F-ll), F-tune.
  - CONFIRMED-WITH-FIX: F-ren (FR-1), F-tel (FT-1), F-rem (FR-2), F-ind (FI-1, FI-2).
  - **WRONG as stated: F-split** (superseded by U-dec; its β-level use survives via U-pair).
- **Session 2.**
  - CONFIRMED: F-norm, U-tad, U-dec, U-res, U-red (given (U-loc), with FR-1), U-cov-IR (as stated).
  - CONFIRMED-WITH-FIX: U-pair (UP-1, UP-2), U-Tay (UT-1, UT-2), Theorem UNIV (precision of (U-IR), (U-loc)).
- **Uncounted (FLOW counts them "with Theorem UNIV").**
  - Corollary UNIV-rate: GAP ((U-IR-s) imprecise; Γ^cov).
  - Lemma F-R: CONFIRMED-WITH-FIX ("iff" → "if").
  - §19A: CONFIRMED-WITH-FIX (RN-1, RN-2).
  - The parenthetical in (U-IR)(a) ("holds for the propagator by U-cov-IR"): GAP UC-1.

**Corrected tally: 20 PROVEN-HERE** (21 − F-split), every one conditional exactly as labelled.
- The conditions are (SF-g), (RLF-δ), (SF-cont), (SF-∞).
- For the one-loop coefficient they are (U-IR) and (U-loc); for the per-step b_k and F-tel, also (SF-bg) at the trivial
  point (FT-1).
- 1 IMPORTED-AND-REVERIFIED (L4b), unchanged.
- OPEN: (U-IR) [s-P], (U-loc) [s], (U-IR-s) [s-P, to be restated], U-cov-IR' [s, new], and the finite-order IFT locality
  of the tower at 1 [s, new, or keep (SF-bg)].

# Required fixes (binding for the next lane-C session)

1. **FS-1:** F-split leaves the count; mark it "superseded by U-dec".
2. **FI-2 (B6):**
   - §4 (RLF-δ) consumes RLF's requantified per-level form along the chain's own sequence.
   - The suggested RLARGE wording in §10/§19A carries "for the chain's own effective sequence (Def F-g)".
   - Note that FLOW's sequence has β_+ ≥ β_1 and β_- → β_1.
3. **FI-1:** state in §4 and §9 that (SF-g)_k and (RLF-δ)_k are needed given (F_R) on [0, k] only. Record this as a
   requirement on RLARGE's (I_k) induction.
4. **UC-1:**
   - Delete "(it holds for the propagator by Lemma U-cov-IR)".
   - State U-cov-IR' (derivative bounds, coarse-momentum derivatives of P_⊥Ĝ_n^{-1}P_⊥, alias off-diagonals) as OPEN.
   - Split (U-IR)(a) into (a1) propagator, (a2) IR-term vertices, (a3) slice modification, (a4) longitudinal sector.
5. **(U-IR) definition:** define J_n exactly (alias folding, routing, and the slice vs BF-Feynman comparison).
6. **(U-IR-s):** restate it with the n-independent φ_∞ and J_*, and with a separate rate hypothesis for β[Γ^cov_n].
   Until then, UNIV-rate is a GAP.
7. **UP-1:** add the O(r²)-remainder locality to (U-loc), and define ξ' including the slice and FP pieces.
8. **FT-1:** narrow §21's (SF-bg) sentence to B_n, or prove the finite-order locality at 1 of the tower by the implicit
   function theorem.
9. **FR-1:** replace the l.260 bracket with the calibration argument (c = 1 from (iii)).
10. **FRR-1, FRR-2, RN-1, RN-2:**
    - "iff" → "if".
    - Add an [S2] pointer at §10 l.409.
    - "literally false" → "not implied". Name RLARGE §7.2 (iv) and PLD-fin (PLD.md l.194) as further monotonicity uses,
      and add a PLD row.
    - In the (P2) row, β_- → β_+.
11. **UT-1, UT-2:** σ_h = −β_0^std; give the continuum version of the U-res split.
12. **FR-2:** the δβ_k sign, matched to RLARGE.
13. **CK-1, CK-2, UR-1, UR-2, FN-1:**
    - CK-1: a log line for the 23:12:50 criteria re-write and f1's ordering.
    - CK-2: "up to 9%" → "up to 12.5%".
    - UR-1: the f2 κ-label (0.25, not 1).
    - UR-2: "consistent with ℓ^{-2}".
    - FN-1: the stale PROOF line pointers.

---

## Strategic verdict: (U-IR) vs (U-loc) vs the f6 iterated chain

- **What has been achieved.** UNIV-1L is now a reduction to estimates on explicit trivial-background objects. That is
  real progress:
  - D²Φ is out (for B_n).
  - The drift term has no marginal part.
  - The log coefficient is a residue.
  - The residue is −β_0^std.

  But the reduction moved the hard part rather than removing it. (U-IR)(a) is the lattice one-loop computation of the
  composite, gauge-covariantly IR-regulated Wilson functional, for SU(N), with the iterated S4' composite. For a
  propagator-only piece it is honest-session-scale (UC-1). The IR-term vertices, the slice and the longitudinal sector
  are paper-scale. Do not report UNIV-1L as nearly closed.
- **Do (U-loc) first.**
  - It is session-scale and precisely statable (after UP-1).
  - It needs only per-level N5-triv locality and the explicit Λ of U-dec.
  - It closes one of the two named hypotheses of Theorem UNIV outright.
- **Then U-cov-IR' (the derivative form).**
  - It is a direct extension of a proven lemma (Dirichlet-factor derivatives).
  - It also needs the uniform-in-n smoothness of P_⊥Ĝ_n^{-1}P_⊥ in coarse momentum, which F-depth's recursion should
    give with derivatives.
  - It makes the propagator part (a1) genuinely proven, and is the honest version of what §18 claims.
- **f6 (iterated two-level chain at ℓ = 9 vs the single block): run it, but as a falsification test, not as progress.**
  - It is cheap relative to the vertex bounds.
  - It tests the two things no proof touches yet: the composite structure, and the background-dependent 𝒞 (Γ^cov,
    (U-IR)(c)).
  - A log in the iterated kernel-vertex part, or a non-converging c^K, would show U-F2 before paper-scale effort goes
    into (a2).
  - f5/f5b alone are one non-iterated abelian scalar block with constant 𝒞 and a loose (G) threshold. They do not
    discriminate at the ~10⁻³ level for κ_c = 4.
  - Pre-register a tighter (G) line (e.g. |s^K·48π²| ≤ 0.005 and a falling sequence).
  - Write the criteria with `cp`/append discipline (CK-1).
- **Do not spend effort on R or on Lemma F-R refinements.** No consumer needs R = 0 (§19A stands after RN-1/RN-2), and
  everything in this lane is still conditional on the layer-1 package (SF-g), (RLF-δ), (SF-cont), (SF-∞). That package
  is Balaban-scale and shared with lanes A and B. The binding item with cross-lane consequences is FI-1/FI-2: RLARGE's
  (I_k) induction must deliver the per-level (RLF-δ)_k from (F_R) on [0, k] along the chain's own sequence. Without
  that, F-ind's non-circularity is asserted, not shown.
