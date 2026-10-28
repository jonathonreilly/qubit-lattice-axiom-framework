# REVIEW_BFT_B_S3: hostile review of BFT lane B session 3 (BFT_B.md [RBB2-fix] edits, §9-§11; check bb3)

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md, PROOF.md, HIST.md, SF.md or EXISTENCE.md. This is the
only file I edited. No commits, PRs or pushes.

Inputs (read 2026-10-28 ≈06:55-07:10 UTC; BFT_B.md born = modified 06:50:41, 164390 bytes):
- BFT_B.md: every [RBB2-fix] tag in context (l.46, 81-90, 212, 385, 691-697, 727-737, 844, 854, 863, 877, 898, 940, 951,
  1013); §9-§11 and the session-3 FOR OTHER FILES (l.1025-1497) in full. BFT_B_LOG.md session 3 in full.
- REVIEW_BFT_B_S2.md in full (format; binding fixes).
- checks/bb3_criteria.md, checks/bb3_walk.py (line by line), checks/bb3.out, checks/bb3.out.time; `TZ=UTC stat` of all of
  them.
- BFT_A.md: §1 (l.18-47), BA-10/11/12 and Theorem BA (l.80-92), §3.9-§3.11 (l.205-275), §6 GAP 1/2 and the corrected pair
  (l.380-436), BL-6/BL-7 (l.684-731), §10 (l.757-796), §12 (l.869-942), §13.7 (l.1050-1068), §15 (l.1184-1222). There is
  no REVIEW_BFT_A_S3.md.
- PROOF.md: Theorem RW (l.5346-5372), Lemma U0 (l.5608-5622), NAH1 (a)/(b) (l.5770-5780).
- REVIEW_S22 Part 5 (BFT statement, l.395-437); SF.md (L-loc)_k (l.846-852); EXISTENCE.md H-Bal-3 (l.264-290); HIST.md
  (C) glued main term (l.1688-1696) and Target S4 / Theorem MSG (l.1064-1072, l.1144-1160, l.1213-1300).

Re-run: bb3 under the numeric lock. The record is at the end of this file.

---

## Bottom line

- **RBB2 fixes: all applied.** The **C2-3 deviation is JUSTIFIED and is an improvement on my predecessor's fix.**
  - The radii are ε_mix/16 for BB-mix′_1 and ε_B/16 for BB-3_1.
  - The s-weighted contraction runs at the level ε_mix, so the lift's *complex* curvature must sit below ε_mix. The literal
    ε_br/16 did not ensure that.
  - **Lemma U0-ℂ: CONFIRMED**, with two cosmetic slips.
  - One residual is unmarked: l.940 still says c_ρ = 2S_ρ/r_♭ is "used from here on", which §10.5 corrects.
- **Lemma N5-an♭-dens: CONFIRMED.**
  - The radius r_ρ ≤ r_♭ is right, from compactness and finitely many types.
  - c_ρ = 4S_ρ/r_ρ is safe (conservative). The two added ε-independent thresholds are right.
- **Theorem RW^∇_k: CONFIRMED as an implication**, with binding fixes:
  - **W-ls is false as written.** Lane A's norms are sums of sups, not sups of sums. The cost is a constant factor t ≤ 6.
  - Step 1's justification of the second pairing conflates the support of C^♯ with the region it reads (wording; the
    conclusion holds).
  - R ≥ 8 with T = 4R does not embed □^{(R+6)} in 𝕋.
  - **(W-loc) (iii) (Feynman form) is not lane A's current operator.** Lane A's configuration-level work is in a hard
    tent-axial slice. A hard-slice variant goes through, but it is not written.
- **Using (H-lin^∇) on the local tori is LEGITIMATE as a use of the hypothesis.**
  - Lane A's statements are periodic-torus statements, uniform in T ≥ 1 (or T ≥ 3).
  - The coarsest residual removes zero modes and torons, and periodic local tori avoid RW∇-F1.
  - **But the hypothesis pair (W-lin) + (W-comm) is not currently known to be jointly satisfiable in any one norm pair.**
    (COMM)'s plain level-l rows (GAP 1) need a (Pl) slot. BL-6 (b) shows (H-lin^∇) fails with that slot as written. And
    (W-lin) in 𝔐^∇ (configuration level) needs LR-grad, which is OPEN.
  - This is the dominant open item. §11's "now a theorem relative to lane A's linear inputs" must say so.
- **Theorem BB-mix_k: CONFIRMED as an implication.**
  - I re-derived:
    - the fixed point;
    - the s ≡ 1 identification;
    - the corrected 𝔈_Q (the trapezoid identity is exact for quadratic densities, which is what defeats RW∇-F3);
    - Lemma W-grad0;
    - the class splitting;
    - the cluster identity;
    - the Cauchy and lattice-animal counts, C_R K^{|X|-1} with K = 2^{41}/(s̄ - 1) and ||R||_𝒜 ≤ 2e^{m_0}C_R.
  - **At m = 0 the per-cube smallness comes from cube size (M_c ≥ 2R_W ∝ s̄), not from field size.** So
    κ_L = log(1/K)/M_c ~ log s̄/s̄ is tiny. The weighted form is needed for any consumer with a rate threshold.
- **Corollary BFT4-poly_k: CONFIRMED with narrowed wording.**
  - R_k contains E_∅ − S_W. E_∅ is a sum of *single-link, non-gauge-invariant* functions of size O(κε²), so R_k is of the
    same order as S_W.
  - The corollary is "the bounded-polymer clause of BFT-4 on 𝒞_glob, without gauge-invariant pieces", not "BFT-4 at every
    k on 𝒞_glob minus a detail".
- **Corollary BB-Lloc_k: CONFIRMED-WITH-FIX.** The per-piece bound e^{-κ_L diam} loses the lattice-animal entropy. Keep a
  factor K^{(|X|-1)/2}.
- **(BB-gi)_k: SERIOUS. It is the bridge from 𝒞_glob to BFT's class, not a cosmetic clause.**
  - RW∇-F2 is *witnessed*: E_∅ itself is not locally gauge invariant.
  - Consumers of per-polymer invariance:
    - BFT-4 as stated (every curvature-small V on every torus);
    - its Cauchy consequences at non-trivial backgrounds;
    - EXISTENCE H-Bal-3(3a)-form;
    - HIST (C)'s gauge-invariant glued main term.
  - A gauge-invariant *sum* suffices only on 𝒞_glob, and only for the value identity, c_k and (SF-∞)_B.
  - Fix: covariant centring (Part E). On 𝒞_glob it reduces (BB-gi)_k to one new input, a covariant smooth lift. Off
    𝒞_glob it is lane A's (UHL)/(SL-cov) package. HIST's Theorem MSG supplies the sup half of the local frames.
- **bb3: PASS; the re-run is byte-identical.** It tests algebra on a *massive* scalar model only. The m = 0, O(1/R) regime
  that RW^∇_k actually claims is untested.

---

# PART A: the [RBB2-fix] edits and the C2-3 deviation

| fix | where | verdict |
|---|---|---|
| R-1 | l.81-83 (pointer to B1-2); l.877 (05:57 §6.4 edit marked) | CORRECT |
| B4N-1 | l.691-695: ρ := r_ℂε_0/2 via BCH z = log(e^Be^{-Re B}) | CORRECT (|z| ≤ ρ(1 + Cρ) ≤ r_ℂε_0, |Re B| ≤ ε_0) |
| B4N-r1, B4N-r2 | l.697, l.854 | CORRECT |
| B4N-2 | l.844; l.1013 (applied 06:47, after §9, logged) | CORRECT; the after-§9 edit is disclosed in the log |
| BMW-1 | l.863 | CORRECT |
| C2-1 | l.46 (BB-geo (c): 4coth⁴ for link sums), l.898 (𝔠_♮ = (32/3)coth⁴(m/2)/γ') | CORRECT |
| C2-2 | l.737 (status), l.940 (c_ρ) | APPLIED. **Residual RS3-1:** l.940 says "c_ρ := 2S_ρ/r_♭, which is used from here on". §10.5 corrects this to 4S_ρ/r_ρ with two added thresholds, but l.940 has no forward pointer. Add one |
| C2-3 | l.84-90, 212, 385, 727-735, 951 | APPLIED, with a deviation (below) |
| C2-4 | l.735-736, l.951 | CORRECT |

**C2-3 deviation (ε_mix/16 and ε_B/16 instead of ε_br/16): JUSTIFIED.**
- BB-mix′_1's Step 2 needs ||Φ(0)|| ≤ 6·(the curvature level at which the s-weighted contraction closes), and that level
  is ε_mix(s̄) ≤ ε_br(R).
- With radius ε_br/16 the complex curvature is only ≤ 0.85ε_br. That can exceed ε_mix, so the s-weighted Lipschitz
  condition 12𝔠_s²C_♭s̄²ε ≤ ½ is not implied.
- REVIEW_BFT_B_S2's own parenthesis ("complex curvature ≤ ε_mix") already demanded this. The literal radius it proposed
  was inconsistent with that parenthesis. The lane's choice is the correct reading.
- Check: S := ε_V + 4ϱ ≤ ε_mix/2 + ε_mix/4. Then 6c_ℂS(1 + 2S) ≤ 6·1.1·0.75(1 + 1.5ε_mix)ε_mix ≤ 6ε_mix, since ε_mix is
  tiny. For BB-3_1: S ≤ ε_B/2, giving ≤ 6·0.6ε_B.
- BFT-2's polydisc fits: r_ℂε_0 ≤ ε_mix/16 for ε_0 ≤ ε_mix/2 and r_ℂ ≤ 1/8. BFT's r_ℂ is free in (0, 1], so this costs
  nothing.

**Lemma U0-ℂ (l.1117-1120; proof l.1270-1288): CONFIRMED.**
- (a) Each factor (e^zV^r)^{±1} is e^{w}·(unitary) with |w|_HS = |z|_HS. Moving the w's left conjugates them by unitaries,
  so V_P = e^{w_1}⋯e^{w_4}e^{Y_r}.
  - Every monomial of the product minus 1 has degree ≥ 1, so HS-submultiplicativity gives ≤ e^S − 1.
  - The log series bound holds, and tr log ∈ 2πiZ with |tr| < 2π puts the log in sl(N, C).
- (b) U0 (i)-(ii) hold for SL(N, C) (U0 states this, PROOF l.5608).
  - The corner holonomy is V_P (U0 (ii)), so Y = P_1^{-1}log U_pP_1 with |Y| ≤ e^{6ϱ}|log V_P|.
  - The soft gradient vanishes on the real domain, hence identically by the identity theorem.
  - The Wilson derivative −½tr(X(W − W^{-1})), 6 plaquettes per link, and 2|sinh Y| ≤ 2|Y|(1 + |Y|²/5) are all correct.
  - c_ℂ ≤ 1.0779·1.0018 ≤ 1.1 is correct.
- Cosmetic slips:
  - **RS3-2:** "for S ≤ 0.18" (l.1275) should read **S ≤ 0.17**. The reduced inequality 0.47 ≥ 2.53S + 1.06S² fails at
    S = 0.175. This is harmless, since S ≤ 3/40.
  - **RS3-3:** the "Use" line's 6·0.85ε needs ε ≤ 0.02, which is unstated. It holds for ε_mix.

# PART B: Lemma N5-an♭-dens (l.1112-1116; proof l.1252-1268): CONFIRMED

- (i) The plaquette density continues to the polynomial N − ½(tr U_p + tr U_p^{-1}), which is entire.
- (ii) The soft density is real-analytic through NA-alg's analytic X_0. The real configurations at which densities are
  evaluated (AX logs ≤ r/2, curvature small) form a compact set. Together with (iii), finitely many types modulo
  translation at fixed L, this gives one radius r_ρ and one bound S_ρ. Shrinking r_ρ ≤ r_♭ is free.
- (iv) **c_ρ = 4S_ρ/r_ρ is correct if the polydisc is one combined chart log** (base ≤ r_ρ/2 uses half the radius).
  - If the variables (A, u) are separate polydiscs of radius r_ρ each, as §9's statement literally reads, then 2S_ρ/r_ρ
    holds.
  - Either way the corrected constant is safe, and REVIEW_BFT_B_S2's "2S_ρ/r_♭" was too optimistic for the combined
    reading.
  - The two added thresholds of BB-mix′_1 (s̄r_s ≤ r_ρ/2 and 3(3L − 1)ε ≤ r_ρ/2) are the right ones and are ε-independent.
- Status "PROVEN-HERE (routine)" is appropriate.

# PART C: (H-RW^∇)_k and Theorem RW^∇_k

## C.1 The statement (§9.2, l.1081-1097) against BMk-1: CONFIRMED

Clauses (a)-(f) implement BMk-1:
- (a) smooth assignment;
- (b) column-in-□^{(1)} and the output supports;
- (c) local-sup "solid" replacements;
- (d) holomorphy, the s ≡ 1 identity and splitting;
- (e) cutoff multipliers;
- (f) the s-weighted remainder.

One simplification is legitimate *on 𝒞_glob*. BMk-1 (d) asked for holomorphy in the data. Here 𝓛 is data-independent
(centred at the trivial chain), so all data dependence sits in 𝔑. **This same simplification is the source of RW∇-F2**
(Part E).

## C.2 Lemmas W-ls, W-cut, W-mult, W-pair

- **W-ls (l.1100-1102; proof l.1194-1204): FALSE AS WRITTEN; fix RW3-1 (binding, constants).**
  - The proof sets N_z := "the maximum over j of the sum of these quantities at z" and asserts ||x||_𝔐 = sup_zN_z(x) "up
    to the order of max and sup, which commute" (l.1201).
  - But ||x||_𝔐 = max_j[||x^c_j||_∞ + ||∇^cx^c_j||_∞ + [∇^cx^c_j]_α + L^{k-1-j}||r^c_j||_∞] (BFT_A l.38) is a **sum of
    sups**. sup_z of the sum is smaller by up to a factor 4. Max and sup commute; sum and sup do not.
  - The same holds for 𝒴^∇:
    - (G) contributes ||G|| + [G]_α;
    - (P0) contributes ||j_0|| + [j_0]_α;
    - (R) and (Pl) contribute one term each;
    - the four components are summed.
  - Fix: apply the lemma term by term. Each summand is a local-sup seminorm with r_N = 3. This gives
    ||Σw_iu_i|| ≤ t·n·max|w|·max||u_i||, with t_X = 4 and t_Y ≤ 6. Equivalently, work in the equivalent norm sup_zN_z.
  - Every use (ε_W, N_P = 4^d, 𝔠_W, the 2^d counts in BB-mix_k (i) and σ) gains the factor t. R_W(s̄) scales by t_Y.
  - No statement changes form.
- **W-cut (l.1206-1218): CONFIRMED with its post-proof corrections.**
  - σ is C^{1,1} with |σ'| ≤ 2 and |σ''| ≤ 4.
  - ψ has |∂| ≤ 4/R and |∂²| ≤ 16/R² (scale R/4).
  - χ_I = w_I/Σw_J has |χ'| = |σ'|/(1 + σ)² ≤ 2 and |χ''| ≤ 4 + 8 = 12, so scale ¼ is right.
  - η has |η'| ≤ 1 and |η''| ≤ 3, so scale ½ is right.
  - **RS3-4 (cosmetic):** §9.0 (l.1040) and (e) (l.1095) define cutoffs only for ℓ ≥ ½, and χ has scale ¼. Neither
    W-mult's proof nor any count uses ℓ ≥ ½, so extend the definition to ℓ ≥ ¼.
- **W-mult (l.1220-1244): CONFIRMED** with the corrected C_M^X(ℓ) = 1 + (2d + 31)/ℓ + d/ℓ².
  - I re-derived (1)-(4).
  - Item (2): h is the own-step average of ∂φ.
  - Item (3): the Campanato product rule and Osc_2(x^c; B) ≤ dρ||∇^cx^c||.
  - Item (4): with Σ|w_{c,a}| ≤ 5L (BL-2 (b)) and the ℓ¹ spread 6L^{1-(k-j)}, the powers of L cancel exactly to 30/ℓ.
  - Both constants are k-independent. This is the real content: smooth cutoffs cost O(1/ℓ) in coarse units at every
    level.
- **W-pair (l.1108-1110; l.1246-1250): CONFIRMED.**

## C.3 Theorem RW^∇_k (l.1123-1132; proof l.1290-1348): CONFIRMED as an implication; fixes RW3-2, RW3-3, RW3-4

- **Step 1 (parametrix identity).** The conclusion 𝓛P_□y = π(M_{χ_□}y − R_□y) is correct. The sign convention and the
  first pairing (ψ ≡ 1 on □^{(4)} ⊂ □^{(R/2)}) check.
  - **RW3-2 (binding, justification).** l.1299 says "The second reads ιx' only on (supp ∂ψ_□)^{(3)} ⊂ □^{(R+3)}". Two
    claims are being conflated:
    - the **covector** C_ψ(u) reads x only on (supp ∂ψ)^{(3)}, because Σu_aB_{ab}x_b(ψ_a − ψ_b) vanishes where ψ is
      locally constant;
    - but the transfer ⟨C^♯, ιx'⟩_{𝕋_□} = ⟨ι^*C^♯, x⟩_𝕋 goes through the **representation**. By (W-loc) (ii) its pairing
      reads x on (supp C^♯)^{(3)} ⊂ □^{(R+6)}, where x' ≠ x.
  - Correct argument:
    - put x'' := x on □^{(R+6)} and 0 elsewhere;
    - ⟨ι^*C^♯, x⟩_𝕋 = ⟨C^♯, ιx''⟩_{𝕋_□}, by pairing locality on the embedded □^{(R+6)} (side 3R + 12 < T_W);
    - this equals C_ψ(u)(ιx''), which equals C_ψ(u)(ιx'), because x' and x'' agree on (supp ∂ψ)^{(3)}.
  - The T_W = 3R + 14 correction is exactly what this needs. Replace the sentence.
- **RW3-3 (binding, scope).** Step 1 also needs □^{(R+6)} to embed injectively in **𝕋** ("whose 3-neighbourhood □^{(R+6)}
  embeds" is used on both tori).
  - With T = 2M_c = 4R this needs 3R + 12 < 4R, i.e. R ≥ 13.
  - The theorem says R ≥ 8 (l.1124), so 8 ≤ R ≤ 12 with T = 4R is not covered.
  - Fix: R ≥ 13, or T ≥ 3R + 14. Irrelevant in practice (R ≥ R_W ≫ 1).
  - Also, BFT's class is every torus side ≥ T_0, and T a multiple of M_c is a restriction. Use cube sides in
    [M_c, 2M_c) and box sides in [R, 2R) (product partitions, as PROOF's R20-fix RW2-1). The counts change by constants.
- **RW3-4 (binding, hypothesis/operator mismatch).** (W-loc) (iii) assumes the Feynman form: 𝓛 acts on all of X with no
  hard slice. Step 1 uses this twice:
  - x' (truncated) and ψιx' are fed to 𝓑 and to 𝓛_□u = πỹ;
  - these are not in any slice.

  Lane A's operator is mixed.
  - Theorem BA's hypotheses are stated at "per-level covariant slice with Feynman terms on residual groups" (BFT_A l.206).
  - Lane A's session-3 configuration-level results (LR-pot, Corollary FP) are in the **hard** tent-axial slice S_tent
    (BFT_A l.894-897, l.936-940).

  The hard-slice variant does go through [inference, checked in outline]:
  - put P_□y := Π(ψ_□ι^*u), where Π is LR-pot's local projection (Π − 1 is a composite gauge direction, local,
    translation-covariant);
  - 𝓑 = Hess 𝔉_k(0) annihilates gauge directions (gauge invariance at a critical point), so 𝓑(Πψu, x) = 𝓑(ψu, x) and
    𝓑(u, Πψx) = 𝓑(u, ψx);
  - ⟨ỹ, (Π − 1)ψιx'⟩ = 0, because ψ ≡ 1 on a neighbourhood of □^{(4)} wider than Π's radius;
  - so the identity holds with C_ψ unchanged, *provided 𝓛 has no Feynman term*.

  With a mixed form (slice plus Feynman terms on residual groups), the Feynman part does not annihilate its gauge
  directions, and [Π, ψ] terms enter (W-comm). Fix: state which operator RW^∇_k is for. Either write the Π-variant
  (hard slice, no Feynman term) or require lane A's (H-lin^∇) for the pure Feynman operator. Until then (W-loc) (iii) is
  a hypothesis that lane A's present operator does not satisfy.
- **Step 2 (supports): CONFIRMED.**
- **Step 3 (bounds): CONFIRMED up to RW3-1.**
  - Transport of local-sup norms is valid: the seminorms are translation-invariant formulas on the embedded region.
  - The 5^d and 4^d counts check: ⌈2(R + 6)/R⌉ + 1 ≤ 5 and ⌈2(R + 3)/R⌉ + 1 ≤ 4 for R ≥ 8.
  - ε_W = 5^d(4C_c/R)G·C_M^Y(¼), with C_M^Y(¼) = 17, and R_W = 16·5^d·17·C_cG·s̄ are consistent (s̄ε_W ≤ ¼).
- **Step 4: CONFIRMED.**
  - π is onto X* even without the (Pl) slot. A level-l plain current j can be pushed down: ⟨j, x_l⟩ =
    ⟨Q^Tj, x_{l−1}⟩ − ⟨j, r_{l−1}(x)⟩, so by induction it is a residual source plus a level-0 current. That is BL-1's
    mechanism.
  - So invertibility uses (W-lin) only on 𝕋_□, as claimed. The by-product (W-lin) on 𝕋 with G' = (4/3)4^dG_P > G is not a
    bootstrap, and the file does not claim it is.
- **Step 5 (clause (d)): CONFIRMED.** I re-checked:
  - the Neumann series of 𝐑(s);
  - the 2^d count for 𝐈;
  - consistency (α)-(γ), with all distances (2R − 3, R − 4, R − 2) positive;
  - the class splitting;
  - holomorphy in the open polydisc.
- **Weighted remark: CONFIRMED as an implication of (W-lin)_m plus the localised (W-comm)**, which is honestly flagged as
  an added hypothesis. The e^{-m(R/2−7)} correction is right (3 units = r_N).

**Is (W-lin) on small tori (side 3R + 14) legitimate? YES, as a use of the hypothesis.**
- Lane A's statements are periodic-torus statements "uniformly in k, T": Proposition W and Theorem W for T ≥ 1, LR-pot for
  T ≥ 3. BFT_A l.206 states the same.
- Coarse translations preserve every level structure: blocks, roots and the tent slice.
- At the trivial chain the top residual r_{k−1} = Qx_{k−1} has weight κ_{k−1}, which removes the constant and toron modes;
  BL-6 (b) treats flat non-exact classes through the data.
- Lane A's imported Green bounds are "on mean-zero tori". That is internal to lane A's proofs, and the composite inverse
  has no mean-zero restriction.
- Periodic local tori are what avoids RW∇-F1 (sharp Dirichlet boundary layers).
- Requirement on lane A: state (H-lin^∇) for every T ≥ T_0, with T_0 independent of k and ≤ 3R + 14, and the slice
  convention fixed (RW3-4).

**But: the hypotheses are not known to be jointly satisfiable (strategic, binding wording RW3-5).**
- (W-comm) needs the plain level-l commutator rows [A^T, ψ]A (BFT_A l.244, GAP 1 l.387-391).
  - Their sizes are O(1/ℓ) per level in plain coarse units. They are representable in 𝒴^∇ only through a (Pl) slot.
  - BL-6 (b) (PROVEN) shows (H-lin^∇) **fails** with the (Pl) slot as written for θ ≤ 1 − α.
  - Lane A's repair (the rough/smooth split; G♯-rough, plus SB for the BCH₂ rows) is NOT PROVEN (BFT_A §13.4, §13.7).
- (W-lin) is a configuration-level 𝔐^∇ bound: x^c, ∇^cx^c and [∇^cx^c]_α.
  - Lane A proves the gauge-invariant outputs (BL-5 (a), Theorem W) and the potentials in S_tent (Corollary FP).
  - The gradient half (LR-grad) is OPEN.

So RW^∇_k is a correct theorem whose hypothesis set has, today, no known model in one norm pair.
- [Inference] The commutator row [Q, ψ]^Tr_l(u) can itself be split by lane A's Lemma RS. Its smooth (Range Q^T) part is
  residual-type by BL-1 (iii), with a k-uniform response; its rough part is a (G♯-rough) source.
- So GAP 1 for (COMM) plausibly reduces to **the same (G♯-rough) + (SB)-type bound** as Theorem H-lin_inv, and does not
  need a separate (Pl) slot.
- Recommend that lane A test this, analogous to CR-1.

Fix for l.1470: "The localisation wall of session 2 is now a theorem relative to lane A's linear inputs" →
"…is now an implication of (W-lin), (W-comm), (W-loc). Lane A has not yet established these jointly in one norm pair.
(W-comm)'s plain rows need the (Pl) slot, which BL-6 (b) refutes as written. (W-lin) in 𝔐^∇ needs LR-grad. (W-loc) (iii)
must match lane A's slice (RW3-4)."

# PART D: Construction BB-bond_k, Theorem BB-mix_k, the corollaries (§9.5 l.1134-1166; §10.8 l.1350-1414)

## D.1 Post-proof corrections and provenance: CONSISTENT; one wording fix

- Order by stat: criteria 06:39:49 < script 06:41:47 < output 06:42:01-03. §9 was pre-stated at 06:37:48 and §10 written
  at 06:49:17 (log). These cannot be split inside one file by stat (single-file birth time = 06:50:41). The logged sizes
  (111780 → 128892 → 164390) are consistent.
- The 7 corrections of §10.9 are all marked in place and agree with §9's text:
  - the χ/η scales;
  - C_M^X;
  - N5-an♭-dens r_ρ and c_ρ;
  - T_W;
  - the ε_W/G_P/R_W/𝔠_W constants;
  - the weighted remark (an added hypothesis);
  - 𝔈_Q, together with W-grad0, (f)-locality in B, and C_E.
- **The last correction is substantive.** With the pre-stated 𝔈_Q, BB-mix_k (ii), the exact decomposition, was *false*
  (it was off by ½⟨𝔑(0; B), A⟩). The repair redefines the construction and strengthens hypothesis (f) to include locality
  in B.
- **RS3-5 (wording):** §10.9's "None changes a theorem's form or status" (l.1421) should read "…form; the hypotheses of
  BB-mix_k ((f) locality in B) and of the weighted remark (localised (W-comm)) are strengthened, and BB-bond_k's 𝔈_Q is
  redefined."
- bb3 cannot distinguish the two 𝔈_Q (𝔑(0) = 0 in the model). §11 says so honestly.

## D.2 Theorem BB-mix_k: CONFIRMED as an implication (constants × t from RW3-1)

- **(i) Fixed point.** I checked:
  - |||Φ_s(0)||| ≤ 𝔎C_M^Y(G_Nε + C_Nε²) ≤ r_s/2;
  - the Lipschitz factor 𝔎C_M^YC_Nσ(2σr_s + ε) = 𝔎C_M^YC_Nσε(8σ𝔎C_M^YG_N + 1) ≤ ½;
  - every fixed point lies in 𝐗_cs;
  - holomorphy, as a uniform limit.

  At s ≡ 1: S_Q𝐀 = A on Q^{(5)} (distance 2R − 7 > 0); (f) is local, so Σ_QM_{η_Q}𝔑(S_Q𝐀) = 𝔑(A); ||A|| ≤ 2^dr_s ≤ r_u
  (×t_X after RW3-1); hence A = x(B). Correct.
- **(ii) Exact decomposition.** 𝔉_D(u) = D(u) − D(0) − ½⟨∇D(u), u⟩ = ½⟨∇D(0), u⟩ + 𝔇_D(u) is an identity. At s ≡ 1,
  Σ_D = E(A) − E(0) − ½⟨∇E(A), A⟩ = E(A) − E(0), since ∇E(A) = 𝓛A + π(g + 𝔑(A)) = 0. Correct.
  - **The trapezoid form is exactly what avoids RW∇-F3.** Quadratic densities have zero defect, so no per-level O(η²)
    sum appears.
  - The splitting, the cluster identity (only connected Γ survive ∂^Γ), constant-gauge invariance by (W-loc) (iv) plus
    uniqueness, and the support X^{(5)} (stated as X^{(8)}, conservative) are correct.
  - **Translation covariance only by multiples of M_c.** The cube partition breaks unit translations. The sum stays
    translation invariant. Non-binding RS3-6: record this, since SF/BB-4♮ use translation invariance of E_k^br only.
- **Lemma W-grad0 (l.1358-1370): CONFIRMED.**
  - At the trivial chain only the top soft densities have a gradient. The Wilson densities have none (Re tr X = 0); the
    lower soft densities are stationary; the Feynman densities are quadratic.
  - ⟨Q^Ta, u_{k−1}⟩ = ⟨a, r_{k−1}(u)⟩ with x_k := 0. The link count 4|Q^{(3)}| gives 5.2ε|Q^{(3)}|·||u||.
  - **RS3-7 (cosmetic):** the holomorphic continuation of Re tr(V_c^{-1}δ) is ½tr((e^{-B} − e^{B})δ) = −tr(sinh(B)δ), not
    Re tr((1 − e^{-B})δ). The bound |sinh B| ≤ e^{|B|} − 1 ≤ 1.3|B| (|B| ≤ ½) is unchanged.
- **(iii) Bounds.**
  - C_E = 2.6ε(M_c + 6)⁴σr_s + C_3(M_c + 6)⁴(σr_s)³. This is O(ε²M_c⁴), the natural per-cube size.
  - Cauchy on radius s̄ − 1 about [0, 1]^Γ. The count ≤ 2^{40|X|} with |X| ≤ 2^{|X|−1} gives C_RK^{|X|−1}, C_R = 2^{40}C_E,
    K = 2^{41}/(s̄ − 1).
  - (80e)^{n−1} animals and 80e·e^{m_0}K ≤ ½ give ||R||_𝒜 ≤ 2e^{m_0}C_R. All correct.
  - All constants are k- and T-uniform given the hypotheses.
- **Mechanism (correcting a reading).** At m = 0 the smallness is K ∝ 1/s̄ with M_c = 2R ≥ 2R_W(s̄) ∝ s̄·C_cG. So
  K ≈ 2^{41}·t_Y·170000·C_cG/M_c: the per-cube smallness comes from **cube size**, polynomially. In BB-mix′_1 it came from
  field size at R = R_* + O(log s̄).
  - Consequence: κ_L = log(1/K)/M_c ~ (log M_c)/M_c → 0 as the constants grow. It is fixed and k-uniform, but tiny.
  - SF's (L-loc)_k remark "κ_L in M-units ≈ κ_5M" (SF l.850) suggests a consumer with a rate threshold.
  - Only the weighted form (R_W = O(m^{-1}log s̄), κ_L ≈ m/c) gives a usable rate. **Record this in §11.**

## D.3 Corollary BFT4-poly_k (l.1146-1151; proof l.1400-1404): CONFIRMED; overclaim narrowed (binding BP3-1)

- E_k^br = S_W + R_k with R_k = (E_∅ − S_W) + ΣR(X). E_∅ = κ_{k−1}Σ_cφ̂_c(V_c; 1) is a sum of single-link functions.
  - They are **not locally gauge invariant**: tr V_c changes under V_c ↦ g_xV_cg_y^{-1}.
  - Each is of size O(κε²), the same order as S_W per cell.
- So R_k is bounded, uniformly in k, but not small relative to S_W, and its pieces are not gauge invariant. Exact gauge
  invariance of E_k^br forces large cancellations between E_∅'s single-link terms and ΣR(X).
- The marginal statement c_k = 1 comes from BB-4♮. Its inputs (I1) and (I2) are lane A's **m > 0** estimates, which are not
  among BB-mix_k's hypotheses. The corollary must list them.
- Fix: "Corollary BFT4-poly_k: on 𝒞_glob, E_k^br = S_W + R_k with R_k a k-uniformly bounded sum of local,
  constant-gauge-invariant polymers (not locally gauge invariant; E_∅ contains single-link non-invariant terms); c_k = 1
  under BB-4♮'s additional m > 0 hypotheses." Apply the same change to the §11 table row and the FOR OTHER FILES line
  (l.1488-1490).

## D.4 Corollary BB-Lloc_k (l.1160-1166; proof l.1405-1411): CONFIRMED-WITH-FIX (binding BL3-1)

- diam_∞X ≤ M_c|X| for *-connected X, so K^{|X|−1} ≤ K^{-1}e^{−κ_Ldiam X}. This is correct.
- But the stated per-piece bound **discards the entropy**. For fixed diameter D the number of X ∋ x grows like
  exp(c(D/M_c)⁴), so Σ_{X∋x}|𝓔_{x,X}| is not controlled by e^{−κ_LD} alone.
- SF's (L-loc)_k is used through sums over regions (CE-exp-𝒞), so the bound must be summable.
- Fix: |𝓔_{x,X}| ≤ C_RK^{−1/2}·K^{(|X|−1)/2}·e^{−(κ_L/2)diam_∞X}. Then
  Σ_{X∋x}K^{(|X|−1)/2}(·) ≤ Σ_n(80e·K^{1/2})^{n−1} converges for s̄ − 1 ≥ 2^{43}(80e)². Alternatively, state the corollary
  as "(L-loc)_k with the polymer-norm bound ||R||_𝒜", which is what CE-exp-𝒞 consumes.
- The polydisc 𝒫_ε is a global sup ball. Each piece depends on B only on X^{(8)}, so the uniform local polydisc of SF holds.
  Correct.
- The remark (SF-∞)_B is ARGUED. The ≥ T/(3R) step count is right: each walk step displaces by ≤ 2R + 5.

# PART E: (BB-gi)_k: verdict and proposed fix

**How serious: SERIOUS (load-bearing outside a narrow use).**
- Witness that RW∇-F2 OCCURS: E_∅ (D.3) is part of the decomposition and is not locally gauge invariant. The R(X) cannot all
  be invariant, because their sum with E_∅ is invariant and E_∅'s non-invariance is local and single-link.
- Root cause: the centring, the trivial chain under B, is not a covariant function of V. 𝓛 is data-independent, so nothing
  transforms under local gauges.

**Does BFT-4 need gauge-invariant polymers, or only a gauge-invariant sum?**

| consumer | needs per-polymer local gauge invariance? |
|---|---|
| BFT-4 as stated (REVIEW_S22 l.414-417): class = every curvature-small V on every torus side ≥ T_0, polydisc "in curvature-adapted coordinates" | **YES.** 𝒞_glob (one global small gauge) is a strict subclass: on large tori, holonomies/torons and the linear growth of axial-gauge links exclude it. Local pieces extend to the full class only if each one is a function of the gauge orbit on its support |
| Cauchy consequences C_♭^{(k)}, (H-G), C_θ level-uniform | **YES**: they evaluate pieces at non-trivial (not globally small) backgrounds |
| EXISTENCE H-Bal-3(3a)-form (l.284-289): E_{K,m}(X) gauge invariant, holomorphic on a neighbourhood containing "in a coarse axial or Landau gauge" all V = exp(iX)V_flat | **YES**, by statement |
| HIST (C) (l.1690-1696): glued main term SU(N)-gauge invariant, local densities assigned on branches over different U | **YES** for the gluing across backgrounds |
| SF (L-loc)_k (l.848-850): pieces on a uniform polydisc max_{b∈R}|A_b| < ρ_k | only if SF's A is not globally small-gauge-fixed. On 𝒞_glob in a global gauge, NO |
| RLARGE (BFT-3 only), FLOW (z = 0, V = 1) | NO |
| value identity E_k^br = E_∅ + ΣR(X), c_k = 1 (BB-4♮), (SF-∞)_B | NO (the sum suffices) |

**Proposed fix (Route GI-A, covariant centring; Balaban's architecture, and what BB-mix′_1 already does at k = 1).**
At k = 1 the pieces are gauge invariant precisely because they are centred at the covariant lift U^(0)(V) (U0 (iii); §6.5
Step 4).

At general k:
- **(GI-1) centre at a covariant smooth background** Z^sm(V), with Z^sm(V^h) = ĥ·Z^sm(V) for every level-k gauge h (ĥ its
  composite extension). Expand Z = e^XZ^sm(V). The cutoff multiplication commutes with Ad_ĥ pointwise (scalars).
- **(GI-2) covariant norms**: 𝔐^∇ with differences covariant relative to Z^sm. Sup norms are already invariant.
- **(GI-3) covariant local inverses, without a transplant ambiguity.** Either:
  - (a) use box-local frames: a canonical gauge on □^{(R+6)}, unique up to a constant at a root, so that (W-loc) (iv)
    absorbs it. Transplant, invert, and conjugate back. NAH1 (b) does exactly this at level 1 with Lemma AX (PROOF
    l.5777). Or:
  - (b) replace the local torus by the covariant **compressed-plus-mass** operator 𝓛_□ := ψ'𝓛(V)ψ' + μ²(1 − ψ'²) on the
    global torus (ψ' = 1 on □^{(R+6)}). It is covariant automatically, depends on V only on supp ψ', and equals 𝓛(V) on
    supp ψ_□'s 3-neighbourhood. So Step 1 holds verbatim with no transplant. It needs the new linear input (W-lin-cmp):
    uniform 𝒴^∇ → 𝔐^∇ bounds for this smoothly compressed operator. With ψ' of scale R there is no sharp boundary layer
    (RW∇-F1 does not apply). This is a variable-coefficient but smooth statement for lane A.
- **(GI-4) conclusion by uniqueness**: 𝐀(s)(V^h) = Ad_ĥ𝐀(s)(V), so 𝔈_Q, ΔE_X and R(X) are locally gauge invariant. E_∅
  becomes 𝔉_k(Z^sm(V); V), a gauge-invariant local sum.
- **Cost on 𝒞_glob:** if ||Z^sm(e^B) ⊖ 1||_𝔐 ≤ C_smε in the global gauge, every hypothesis ((W-lin), (W-comm), (f),
  (E3^∇), (I-id)) at the background Z^sm follows from the trivial-chain one by G-pert. The condition is
  C_sm·G·ε·(1 + C_c) ≪ 1, compatible with ε ≤ ε_mix(s̄). Then (BB-gi)_k on 𝒞_glob ⇐ **(CovLift): existence of Z^sm with
  that bound**. That is lane A's "smooth lift Z^sm", ARGUED (BFT_A l.255-256).
- **Corner lifts do not work.** The composite corner lift (U0-type, TOWER-VAR (b)) is covariant, but its fine-level
  curvature concentrates at block corners. Its 𝔐^∇ size is L^{2(k−j)}ε in coarse units, not O(ε), so it is not a usable
  centring at k ≥ 2. This is why lane A chose C-glob.
- **Off 𝒞_glob (BFT's full class):** route (a) needs frames in which the background is 𝔐^∇-small on each box. HIST's
  **Theorem MSG (PROVEN, l.1213)** gives depth-uniform *sup* smallness of all link logs in an interpolation gauge on a cone
  (the potential half). The gradient/Hölder half is lane A's (UHL)/LR-grad (OPEN). Route (b) needs only (CovLift) on
  patches plus (W-lin-cmp) at MSG-small backgrounds.
- So **(BB-gi)_k is not a new independent wall**. On 𝒞_glob it is (CovLift). Off 𝒞_glob it is the same package lane A
  needs for BFT-0/1/2 outside 𝒞_glob: (UHL)/LR-grad, (SL-cov), Z^sm.

**Route GI-B (Balaban-style gauge-invariant re-localisation after the fact): NOT VIABLE as an exact identity.**
- Defining R̃(X)(V) := R(X)(V^{g_X}) with a canonical local gauge g_X on X^{(8)} gives invariant pieces.
- But ΣR̃(X) ≠ ΣR(X), because the decomposition is not gauge-equivariant.
- Haar-averaging over local gauges is undefined, because V^h leaves 𝒞_glob.
- Covariance must be built into the construction (GI-A), as in Balaban's CMP 99/102 background-covariant propagators
  [second-hand].

# PART F: check bb3

- **Pre-registration: CONFIRMED.** Stat: criteria born 06:39:49, script 06:41:47, output 06:42:01-03. The script matches
  the criteria:
  - the 48² torus;
  - μ² = 2, R = 4, M_c = 8, T_W = 3R + 8;
  - the cutoff profiles, the thresholds and the seeds.
- **Script audit: CONFIRMED.**
  - Comm = 𝓛ψ − ψ𝓛 on the local torus, and Rfull = −Comm·G·χ. So 𝓛P = 1 − R exactly as in Step 1 (ψ = 1 on supp χ).
  - opR and opP implement 𝐑(s) and 𝐏(s): weight s_{Q'Q(□)}, output to every Q' with s ≠ 0, η applied.
  - The energy uses the **pre-stated** 𝔈_Q. It is indistinguishable from the corrected one here (∇E(0) = g), as §11 says.
  - B3-7 replaces per-cube *copies* of g. This is a model device; the theorem's data are shared, so it tests class
    locality only.
- **Limits (stronger than §11 states):**
  - (1) The model is **massive** (μ² ∈ {1, 2}). The informational ||R||_∞ falls exponentially in R (e.g. 0.052 → 0.0098 →
    0.0020). This tests nothing about the m = 0, O(1/R) claim of RW^∇_k, which is the regime the theorem's ε_W is about.
  - (2) T_W = 3R + 8 suffices for a range-1 operator. The theorem's 3R + 14 is not tested.
  - (3) ψ is piecewise linear, not C^{1,1}. This is irrelevant for the algebra.
  - (4) There is no level structure, no (Pl) or (COMM) issue and no slice.
- Recommended (non-binding): add μ² = 0⁺ with a constant-mode penalty, i.e. a massless interior plus a single global
  constraint mimicking the top residual. Check that R·||R|| stays bounded as R grows, which is the O(1/R) law.
- **Re-run (this review): PASS, byte-identical** (record below).

---

# Overclaims
1. l.1470: "now a theorem relative to lane A's linear inputs". The inputs are not known jointly satisfiable (RW3-5).
2. Corollary BFT4-poly_k: "BFT-4's polymer bound at every k … minus local gauge invariance". R_k contains non-invariant
   single-link terms of the size of S_W, and c_k = 1 needs BB-4♮'s extra m > 0 hypotheses (BP3-1).
3. Corollary BB-Lloc_k's per-piece bound is not summable as stated (BL3-1).
4. §10.9 "None changes a theorem's form or status": hypotheses were strengthened (RS3-5).
5. W-ls "up to the order of max and sup, which commute": the norms are sums of sups (RW3-1).

# Tally (lane B session 3; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | RBB2 fixes (residual RS3-1); **C2-3 deviation (justified)**; **Lemma U0-ℂ** (RS3-2/3 cosmetic); **Lemma N5-an♭-dens**; W-cut; W-mult; W-pair; Lemma W-grad0 (RS3-7 cosmetic); (H-RW^∇)_k statement vs BMk-1; bb3 pre-registration, script, reading; re-run byte-identical |
| CONFIRMED-WITH-FIX | **W-ls** (RW3-1, constants ×t); **Theorem RW^∇_k** as an implication (RW3-2 justification, RW3-3 scope, RW3-4 slice/Feynman mismatch); **Theorem BB-mix_k** as an implication (constants ×t; mechanism = cube size at m = 0); Corollary BB-Lloc_k (BL3-1) |
| CONFIRMED, narrowed | Corollary BFT4-poly_k (BP3-1) |
| ARGUED (accepted) | remark (SF-∞)_B; RW∇-F1 |
| OPEN, serious | **(BB-gi)_k**: on 𝒞_glob ⇐ (CovLift); off 𝒞_glob = lane A's (UHL)/LR-grad + (SL-cov) + Z^sm |
| strategic | (W-lin) + (W-comm) have no known common norm pair (GAP 1 versus BL-6 (b); LR-grad OPEN) |

# Required fixes (binding for the next lane-B session)
1. **RW3-1.** W-ls is termwise. Insert the factor t (t_X = 4, t_Y ≤ 6, from the summand count of lane A's norms) into N_P,
   ε_W, R_W, 𝔠_W, σ and the 2^d counts; or work in the equivalent norm sup_zN_z and record the equivalence constants.
2. **RW3-2.** Replace l.1299's justification with the x'' argument (C.3).
3. **RW3-3.** R ≥ 13 (or T ≥ 3R + 14). Replace "T a multiple of M_c" by product partitions with sides in [M_c, 2M_c) and
   [R, 2R).
4. **RW3-4.** State which operator: write the hard-slice Π-variant (gauge-direction annihilation) or require (H-lin^∇) for
   the pure Feynman operator. Flag the mixed (slice + residual-group Feynman) case as open.
5. **RW3-5.** l.1470 and the §11 table: hypotheses not yet jointly satisfiable. Name GAP 1 / BL-6 (b) and LR-grad.
6. **BP3-1.** Narrow Corollary BFT4-poly_k as in D.3 and list BB-4♮'s m > 0 inputs. Update l.1488-1490.
7. **BL3-1.** Keep K^{(|X|−1)/2} in BB-Lloc_k's per-piece bound, or state it in ||·||_𝒜 form.
8. **RS3-1, RS3-5 (wording).** Add a pointer at l.940 to §10.5's c_ρ = 4S_ρ/r_ρ. Correct §10.9's "none changes … status".
9. **(BB-gi)_k.** Restate the OPEN item as (CovLift) on 𝒞_glob plus the off-𝒞_glob package (Part E). Pick route GI-3 (a)
   or (b) and pre-state the needed linear input ((W-lin) at Z^sm, or (W-lin-cmp)).
10. Cosmetic: RS3-2 (S ≤ 0.17), RS3-3 (ε ≤ 0.02 in "Use"), RS3-4 (cutoff scale ℓ ≥ ¼), RS3-6 (translation covariance by
    M_c only), RS3-7 (sinh continuation).

# Strategic verdict

- **What session 3 achieved.**
  - It turned session 2's named wall (H-RW^∇)_k into a correct *implication*: block-diagonal dominance with smooth cutoffs
    and local-sup norms, ε_W = O(C_cG/R), k-uniform.
  - BFT-4's bounded-polymer clause on 𝒞_glob at every k follows (BB-mix_k).
  - The genuine technical insight is twofold: local-sup norms replace solidity; the trapezoid per-cube energy kills the
    k-growing quadratic part.
  - These are sound, modulo RW3-1 (constants) and RW3-4 (slice).
- **What it did not achieve.**
  - Its hypotheses sit exactly on lane A's open core, and the polymers are not gauge invariant.
  - At m = 0 the decay rate κ_L ~ log M_c/M_c is tiny. Only the weighted form, which needs a localised (W-comm), gives a
    usable rate.
- **Current minimal open set for BFT-0..4** (on 𝒞_glob unless marked):
  - **BFT-0/1/2:**
    - (H-lin^∇) at configuration level in 𝔐^∇. Its open pieces: (G♯_0-lev0), (G♯-up), (G♯-rough) + (SB), and LR-grad. The
      gauge-invariant outputs for data and residual sources are PROVEN (BL-5 (a), Theorem W), and so are the potentials
      (Corollary FP).
    - (H-rem^∇): third order, polar, Hölder-Lipschitz ARGUED. The BCH₂ plain row: SPD proven, response via (G♯-rough) +
      (SB).
    - (FP♯').
    - Window α ≤ θ ≤ 1 − α.
    - Off 𝒞_glob: (UHL)/LR-grad, (SL-cov), Z^sm.
  - **BFT-3:** k = 1 PROVEN (BB-3_1 with radius ε_B/16). k ≥ 2 ⇐ (H-lin^∇)_m, m > 0, at configuration level (Theorem W
    proves the gauge-invariant half).
  - **BFT-4:**
    - k = 1 PROVEN with gauge-invariant pieces (BB-mix′_1).
    - k ≥ 2: bounded polymers ⇐ (W-lin) [= (H-lin^∇) configuration level, local tori], (W-comm) [(COMM) incl. GAP 1 plain
      rows, Feynman/slice commutators ARGUED], (W-loc) [slice convention, RW3-4], (f) with locality [ARGUED], (E3^∇)
      [third order ARGUED], (I-id) [Theorem BA]; plus c_k = 1 ⇐ BB-4♮'s m > 0 inputs.
    - Gauge-invariant pieces ⇐ (CovLift) (on 𝒞_glob), then the off-𝒞_glob package.
  - **Ledger:** BR1 (v) and NAH1 (a) complex radius α_*/8 → ε_br/16 (lane B's proposed text is correct, given U0-ℂ).
- **The two levers with the largest fan-out:**
  - **(G♯-rough) + (SB)** [inference: it also closes (COMM)'s GAP 1 if the commutator row splits like CR-1];
  - **a covariant smooth lift with configuration-level gradient control** (LR-grad / (UHL) / Z^sm), which serves BFT-0/1/2
    off 𝒞_glob, BFT-3 at configuration level and (BB-gi)_k at once.
- Recommended next lane-B step: pre-state route GI-3 (b) (compressed-plus-mass covariant local inverses) and its single
  linear input (W-lin-cmp). It removes the transplant, the slice-embedding fuss and the gauge non-covariance in one move.

---

## Re-run record (bb3)
- Runner: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revBB3/run.sh`.
  - It waits with `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, then waits for load1 < 8.
  - Environment: nice 10; OPENBLAS/OMP/MKL/vecLib threads = 1; PYTHONDONTWRITEBYTECODE=1; `/usr/bin/time -l`; python3
    without -I; no `timeout`; no trap.
  - It runs checks/bb3_walk.py unchanged, with outputs in revBB3/.
  - It calls `rmdir` exactly once.
- Lock held 07:03:19-07:03:21 UTC. load1 3.09 (pre-check 3.27); memory free 45%; 2.38 s wall; peak RSS 793 MB; exit 0.
- After the run: the lock directory is gone, no bb3 process is left, and checks/ holds no __pycache__.
- **Result: with the two timing lines removed, revBB3/bb3.out is byte-identical to checks/bb3.out.**
  - B3-1 7.772e-16; B3-2 4.770e-15 (||R||_∞ 0.0524); B3-3 1.295e-15; B3-4 0/0 (control 1.484); B3-5 2.427e-15; B3-6 rel 0;
    B3-7 0/0 (control 3.789e-2).
  - VERDICT ALL PASS. The informational rows are identical.
