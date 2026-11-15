# REVIEW_FLOW_S12: hostile review of lane C session 12 (FLOW.md §94-§102 and the [RFL11-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f15*. This file is the only file I edited in
the repo. No commits, PRs or pushes.

Inputs (read-only):
- REVIEW_FLOW_S11.md (all).
- FLOW.md §94-§102 (l.4238-4520) in full; every [RFL11-fix] site (l.4036-4232); §84 (U6) (l.3969-3977); the l.836-841
  re-split; the U_f definition (l.2075, 3835).
- PROOF.md S4' (l.595-600); LINEAR_PACKAGE.md l.70-72, 138.
- FLOW_LOG.md l.507-560 (session 12).
- checks: f15_criteria.md (all), f15_cl_vct.py (all, line by line), f15_out.txt, f15_time.txt.
- The author's scratchpad flow12/ (inplace.py, fix_s11.py, fix95.py, fix97.py, run.sh, f15_conditions.txt, dev.py).

Line numbers below are FLOW.md lines as of this review (FLOW.md md5 002b7b2d…, 506795 B).

---

## Bottom line

- **Provenance: CLEAN, and stronger than the log claims.**
  - I reverse-applied the author's 25 [RFL11-fix] replacement pairs (flow12/fix_s11.py) to the current FLOW.md. The first
    473627 bytes of the result have md5 **4f2fddc9…**, which is exactly the md5 FLOW_LOG records for 10:44:05.
  - So §94 is byte-identical to its pre-statement, and the [RFL11-fix] edits are the ONLY changes made before §95.
  - Two forward references are minor blemishes (S12-8).
- **[RFL11-fix] S11-1..S11-8: all APPLIED and correct.** There are 25 replacements, at the sites the log names.
- **Lemma CL-V: CONFIRMED.** I re-derived (a)-(c) line by line: BCH, the diagonal traces, cross terms, D_U, the Weitzenböck
  step and the spin coefficient 2.
  - The heat-trace ratio is independently re-derived: (−1/3 + 2)/(−1/12) = −20.
  - **Corollary VFINE-K-val: CONFIRMED** (a corollary; strict tally folds it).
  - One wording point: the q → −q equivalence (S12-6).
- **Proposition LONG-n: CONFIRMED for Y_n.** The proof is Cauchy-Schwarz against the gradient of ev^†, with |d_jψ|² = 8.
  - **Overreach:** "hence of W_n" (and of D_ℓ^*Y^{-1}D_ℓ) does NOT follow from §97. Cauchy-Schwarz gives
    ⟨V, Y^{-1}V⟩ ≥ 1/⟨V, YV⟩, which is a lower bound, not an upper one (S12-2).
  - The growth is **not physical**. It lives in the coarse gauge (level-longitudinal) directions, as a D_n(·)D_n^* term.
- **Lemma T-tel: CONFIRMED (THE decisive step).**
  - Re-derived by hand.
  - Independently checked on a generic random complex finite-dimensional model with exact one-step covariance and critical
    structure: (i) to 1.9e-15, the closed recursion to 3.5e-12, the total identity to 7.1e-15, and the (iii) Sylvester
    identity to all printed digits.
  - **The longitudinal growth drops out of c^tot_n EXACTLY, at every n.** The V-block of Y_n enters the total only through
    ½log det Y_n + ½log det(D_ℓ^*Y_n^{-1}D_ℓ), and that equals ½log det(D_ℓ^*D_ℓ) + ½log det_⊥Ỹ_n by Jacobi.
  - **One sign error:** §96 Reading (2) (S12-1, numerically confirmed).
- **Proposition VC-T0: CONFIRMED at U = 1** (closed form, composite recursion, the exact drop-out of d∘h, and the L^{-2n}
  rate re-derived).
  - **Scope:** the exact drop-out (b) is a U = 1 identity. At U ≠ 1 it holds only through a covariant decomposition at U.
    This gives the precise form of what (T-a) must prove (S12-4, the main new point of this review).
  - Also, "uniformly down to K = 0" refers to the difference; the symbol itself is ~|K|^{-2} (S12-5).
- **f15: re-run IDENTICAL, 25/25.**
- **Remaining UNIV list (§99): correct, but not minimal, and (T-a) is imprecise.**
  - The plane-wave form factor of 𝔪_n at Cartan backgrounds is exact and explicit (abelian logs). It is a one-line lemma, not
    an open wall.
  - The hard part of (T-a) is the background linearisation T_k(U) in covariant-decomposition form, together with the poles of
    P_k(U).
  - These are **not** transverse transcriptions of the scalar items (§5).
- **Corrected tally: 70 PROVEN-HERE (claimed 70); strict 66 (claimed 66). CONFIRMED.**

---

## 0. Numerics (reviewer)

Scratchpad: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow12/`.

Lock and run conditions:
- ONE NUMERIC LOCK acquisition, 11:12:52-11:13:29 UTC, released once with `rmdir` (no trap).
- The wrapper waited before the lock for load < 8 and memory free ≥ 35%. At about 11:11 memory free was 33%, so the wrapper waited.
- Inside the lock: load 3.22, memory free 35%.
- nice 10, all BLAS threads 1, plain `python3`, no `timeout`, PYTHONDONTWRITEBYTECODE=1.
- Afterwards: no process left, the lock directory is empty, nothing written to checks/, and no __pycache__ there.

Runs:
- **f15 re-run** from a byte-identical copy (md5 e06c0c38…, matching FLOW_LOG and checks/): 37.2 s, peak RSS 101 MB.
  **25/25 PASS. Output IDENTICAL to checks/f15_out.txt** apart from the timing lines (strict `diff`).
- **`ttel_check.py`** (reviewer; generic model): complex level spaces of dimension 14/11/9/7/6 and ghost spaces 4/3/3/2/2.
  - D^{(k)} random and injective. T_k = D^{(k+1)}ι_k^*D^{(k)+} + R_k(1 − D^{(k)}D^{(k)+}), which gives exact covariance.
  - H_⊥ = P_0AP_0 with A > 0 (critical structure). Π_k random > 0. Y^{(0)} := K_F^{-1} − DΔ^{-2}D^*.
  - Results:
    - Y^{(0)} = H_⊥^+ to 3.4e-16.
    - P_{k+1}T_k = P_{k+1}T_kP_k to 1.9e-15; the closed T-recursion to 3.5e-12.
    - L-tel total = ½ΣΦ^T_k + G_gh,n to 7.1e-15; log det_⊥Ỹ^{(0)} = −log det_⊥H_⊥ to 7.1e-15.
    - (iii) Sylvester form: both sides 28.350627841459563.
    - Reading (2): Φ^T_k − Φ^L_k = **+**[log det(V_{k+1}^*Y^{(k+1)-1}V_{k+1}) − log det(V_k^*Y^{(k)-1}V_k)], with values −7.0022, −3.4647, −5.2203
      on both sides.
  - Disclosure: one extra 0.1 s, 34 MB re-run of this linear-algebra script, to print both sides of (iii), was made outside
    the lock, after it had been released.

## 1. Priority 1: provenance, [RFL11-fix], the minimal list of §99

### 1.1 Provenance

| Event | Time (UTC) | Evidence | Verdict |
|---|---|---|---|
| §94 pre-statement | 10:44:05, 473627 B, md5 4f2fddc9… | **re-verified**: reverse-applying fix_s11.py's 25 pairs to the current file reproduces this md5 on the first 473627 B | ✓ §94 unchanged |
| [RFL11-fix] | 10:44-10:47 | the reconstruction above: these 25 pairs are the only pre-§95 changes | ✓ |
| f15_criteria.md | born = mtime 10:51:15, 4829 B | BSD stat | ✓ before any script |
| dev.py / f15_cl_vct.py | dev 10:52-10:55; checks copy born = mtime 10:57:07, 24239 B, md5 e06c0c38… | stat, md5, `cmp` dev.py = checks copy | ✓ |
| not-run attempt | 10:55:57 (memory 34%) | FLOW_LOG | honest ✓ |
| smoke | 10:56:36-40 | FLOW_LOG; dev_out1 | ✓ |
| official run | 10:58:16-10:58:55 | f15_out born/mtime, f15_conditions.txt (load 4.50, 38%) | ✓ |
| §95-§102 | 11:01-11:03:42 | FLOW.md mtime 11:03:42; birth still 10:13:14 (in-place writes, S11-8 honoured) | ✓ |
| post-proof corrections | 11:01, 11:03 | fix95.py (3 pairs), fix97.py (1 pair) | logged ✓ |

- **fix95.py note.** The draft §95 had "−2q_αF_{12}·**2**Im(φ_1φ̄_2)", an extra factor 2 in the load-bearing spin line. It
  was corrected in place at 11:01 and logged as a "wording correction".
  - The correction is right; the final text is correct (§2).
  - It was a mathematical slip in the proof, not just wording. "Statement changes: none" is still accurate, since (W2) was
    unchanged.
- **Statement changes after §94: none.** This is confirmed by the md5 reconstruction (§94 byte-identical).

### 1.2 [RFL11-fix] S11-1..S11-8

| Fix | Sites | Verdict |
|---|---|---|
| S11-1 (log log ℓ not in c^tot_n; retitle) | l.4036, 4062, 4082, 4178, 4216, 4230 | APPLIED, correct |
| S11-2 (X vs Y; row S_μ; Y_11 ratios) | l.4148, 4153, 4194; FLOW_LOG | APPLIED |
| S11-3 ((G1′), (G4) automatic; C_{K_F} derivation) | l.4122, 4136, 4144, 4172, 4218, 4231 | APPLIED; derivation as in REVIEW_FLOW_S11 §4.4 |
| S11-4 (offset Riemann sum; boundary aliases) | l.4044, 4051 | APPLIED |
| S11-5 (K_a-specific; K_b; K-free form) | l.4075, 4203 | APPLIED (0.538, 0.927, 0.984 present) |
| S11-6 (c_1\|q\|^{-3}) | l.4133 | APPLIED |
| S11-7 (S4' averages transversely; (GP-L) ⊂ (VC-L); 𝔪_n form factor re-listed) | l.4156, 4165, 4174, 4176, 4180 | APPLIED |
| S11-8 (FLOW.md birth reset) | FLOW_LOG | APPLIED; session 12 kept the birth at 10:13:14 ✓ |

### 1.3 Step-1 list (§99, first paragraph)

The list matches REVIEW_FLOW_S11 §5's minimal list verbatim in substance. ✓ It is superseded by the session-12 revision (§4
below).

## 2. Priority 2: Lemma CL-V (§95)

Re-derivation, step by step.

**(a), (b): Ad bookkeeping.**
- U_3^{-1} = e^{−tX_3}B_3^{-1}. Moving B_2B_3^{-1}B_4^{-1} past e^{tX_1} gives Ad(B_4B_3B_2^{-1}); moving B_3^{-1}B_4^{-1} past e^{tX_2} and
  e^{−tX_3} gives Ad(B_4B_3); and Ad(B_4) for X_4. ✓
- With Ad(e^{cH_1})e_{ij} = e^{iq_αc}e_{ij}, this gives y = e^{iq(a_3+a_4)}(e^{−iqa_2}φ_1, φ_2, φ_3, e^{−iqa_3}φ_4). ✓

**BCH.** The t² coefficient of tr B_P(·) is ½W² + ½Σ_{a<b}[s_aY_a, s_bY_b]. ✓

**Diagonal parts.**
- W² = −|w|²(e_{ii} + e_{jj}), so Re tr(B_P½W²) = −|w|²cos(h̄F)cos(qF/2). ✓
- [y_ae_{ij} − ȳ_ae_{ji}, y_be_{ij} − ȳ_be_{ji}] = −2iIm(y_aȳ_b)(e_{ii} − e_{jj}), so Re[−i(e^{ih_iF} − e^{ih_jF})] = 2cos(h̄F)sin(qF/2). ✓
- d²S_W/dt² = −(β/N)Σ2·(t² coefficient), which is (2β/N)·[(W2) (b) summand]. ✓

**Cross terms.**
- Products and commutators of e_{ij}-type matrices from different root pairs are off-diagonal: e_{ij}e_{jk} = e_{ik} with i ≠ k.
- The same holds for root × Cartan.
- So the trace against diagonal B_P vanishes, and the sectors decouple at every abelian background. ✓

**D_U.** The orbit derivative is Ad(U^{-1})ω(x) − ω(x + e_μ), whose e_{ij}-coefficient is e^{−iqa}ω(x) − ω(x + e_μ). ✓
- D_U^* as written. ✓

**(c) At the plane wave.**
- F_P = a(x) − a(x + e_ν) is nonzero only for ν = 2. ✓
- w_P → (∂_1 + iqa)φ_ν − ∂_νφ_1. ✓
- J^0 with y = (φ_1, φ_2, φ_1, φ_2): the pairs (12), (14), (23), (34) give +1, −1, +1, +1 times Im(φ_1φ̄_2), so J^0 = 2Im(φ_1φ̄_2). ✓
- F_P → −∂_2a_1 = F_{12}. ✓

**Weitzenböck (signs checked).**
- ½Σ|D_μφ_ν − D_νφ_μ|² + |D·φ|² = ⟨φ, −D²φ⟩ + Σ_{μν}⟨φ_ν, [D_μ, D_ν]φ_μ⟩ = ⟨φ, (−D² − iqF)φ⟩, with (Fφ)_ν = F_{νμ}φ_μ. ✓
- −2qF_{12}Im(φ_1φ̄_2) = iqF_{12}(φ_1φ̄_2 − φ̄_1φ_2) = ⟨φ, −iqFφ⟩. ✓
- So O^c = −D²δ − 2iqF: **spin coefficient 2** (g = 2 of the background-field vector). ✓

**Vertex.**
- Ṽ_+^c = 2qk_1·1 − 2qp(E_{12} − E_{21}) (from F_{12} = −ip(ε/2)e^{iϑ}e^{ipx_2}). ✓
- Degree-0 part of O_2: only |iqaφ_ν|² (ν ≥ 2) and |iqaφ_1|² (from D^*), giving (q²/2)ε²·1. ✓
- cos(h̄F) and cos(qF/2) enter at F², two degrees up. ✓

**(G2).**
- The ¼q²·4 = q² arithmetic is right. ✓
- The integral of ∂_1(∂_1λ/λ) vanishes by Fubini: for each k_⊥ ≠ 0 the integrand is a smooth periodic total derivative in k_1. ✓

**Independent cross-check of −20.**
- Heat kernel: a_2 ∝ tr(Ω²/12 + E²/2).
- Vector: 4·(−q²F²)/12 + ½·4q²F² = (−1/3 + 2)q²F². Scalar: −q²F²/12.
- Ratio −20 (orbital 4, spin −24). ✓

**f15 A (script read line by line).**
- hess_exact is the exact matrix product rule: f2 = B X X and X X B^{-1}, and the cross terms are doubled. ✓
- The polarisation B(·) recovers ⟨f_1, Of_2⟩ (checked: ¼Σi^{-r}Q(f_1 + i^rf_2) = ⟨f_1, Of_2⟩). ✓
- Vp = 2∂_ε⟨k+p|O|k⟩/N_2 equals Ṽ_+ (ϑ = 0). ✓
- A3 tests the sign as well as the magnitude.
- **Weak control:** A1c fails at only 1.0e-2. At this background the spin term is ≈1% of the Hessian. The decisive spin test is
  A3c (E1 ≥ 0.496), so A1c is a weak but pre-stated control. Say so.
- A1 uses a single background family (direction-1 wave). The formula is proven for every abelian background, so this is
  acceptable.

**Verdict.** **Lemma CL-V and Corollary VFINE-K-val: CONFIRMED.** The N ≥ 3 reading (cos(h̄F) appears only at F²) is correct.

## 3. Priority 3: Proposition LONG-n (§97) and the T-tel verdict (§96)

### 3.1 LONG-n: CONFIRMED for Y_n; the W_n clause is an overreach (S12-2)

**Proof check.**
- ψ = ev^† and A_jd_jψ = D̂_ℓ ev ev^† = D̂_ℓ, so |⟨A_j^†V, d_jψ⟩| = |D̂_ℓ|.
- |d_jψ|² = L^{-4i}Σ_mλ(κ_m) = Σ_μ(2 − 2avg cos) = 8 for L^i ≥ 2. ✓
- Adding the j = n term 1 gives the bound. ✓
- f15 B4 checks it. Increments → 0.1225 (K_a), 1.4743 (K_b), 1.07e-3 (K_c), i.e. ≈ 0.162|D̂_ℓ|²/level, above 1/8. ✓
- **Precondition to name:** the bound uses the soft-chain form 𝒞_n = κ^{-1}ΣA_jA_j^T (COV-str (ii), Π_j = 1), not just "every block
  map". (W4) should say "every block map, in the soft chain of COV-str".

**Where the growth sits.**
- Write A_j = Q_str^{(L^i)} − d_n∘h^{(i)}. Then A_jA_j^T = QQ^T − Qh^Td_n^T − d_nhQ^T + d_nhh^Td_n^T.
- ⟨V, QQ^TV⟩ ≤ L^{-2i} is summable, and the cross terms are summable (‖Q‖ ≤ L^{-i}).
- So the linear growth is the d_n(hh^T)d_n^T term: noise in the coarse GAUGE directions, one O(1) slice per scale, undamped.
- (W6) is the same mechanism in the M-part.
- Physically this is the level-gauge Jacobian bookkeeping. It is the object a per-level gauge fixing (Balaban) removes by hand,
  and here it is removed by P_n. It is **not physical**: it cannot affect β (§3.2).

**The W_n clause (S12-2).**
- §97 Reading (1) and (W4) say "(VC-L) … of Y_n, hence of W_n … FALSE". Only the Y_n half is proven.
- For W_n = V^*Y_n^{-1}V, Cauchy-Schwarz gives W_n ≥ 1/⟨V, Y_nV⟩, a LOWER bound.
- The Schur form W_n = 1/(Y_VV − Y_VTỸ^{-1}Y_TV) shows that W_n ~ 1/(cn) → 0 (non-geometric, with log det W_n ~ −log n) **if** Y_VT stays
  bounded. Y_VT does stay bounded by the decomposition above (the cross terms are summable), but §97 does not say so.
- Fix: either add these two lines, or restrict the FALSE verdict to Y_n.
- The consequence (the Landau split is not n-uniform) is unaffected, because T-tel makes it moot.

### 3.2 T-tel: CONFIRMED; the longitudinal growth drops out of c^tot_n exactly

**(i).**
- T_kD^{(k)} = D^{(k+1)}ι_k^* means T_k(Ran D^{(k)}) ⊂ Ran D^{(k+1)}, so P_{k+1}T_k(1 − P_k) = 0. ✓
- Compressing the L-tel Y-recursion (valid at every U) gives the closed transverse recursion. ✓

**(ii), re-derived.**
1. Start from the L-tel total: ½log det K_F − log det Δ + ½log det Y + ½log det(D_ℓ^*Y^{-1}D_ℓ).
2. D_ℓ = VR gives log det(D^*Y^{-1}D) = log det(D^*D) + log det(V^*Y^{-1}V).
3. Jacobi: det(Y^{-1})_{VV} = det Y_{⊥⊥}/det Y. ✓
4. Hence ½log det Y + ½log det(D^*Y^{-1}D) = ½log det(D^*D) + ½log det_⊥Ỹ. **This is the line in which the whole V-block of Y (where the
   growth lives) cancels identically.**
5. log det K_F = log det_⊥H_⊥ + log det Δ (§85 (a)).
6. Ỹ^{(0)} = H_⊥^{-1}P_⊥. Exactly at critical U, the longitudinal part of Y^{(0)} = K_F^{-1} − DΔ^{-2}D^* vanishes, because (DD^*)^{-1}|_{Ran D}
   = DΔ^{-2}D^*. ✓
7. Telescoping. ✓

**Reviewer's generic numerics.** The identity holds to 7e-15 with no structure beyond covariance and criticality.

**Is the cancellation genuine?** YES.
- c^tot_n is a gauge-invariant total. The T-split writes it with NO object that sees the V-block: Ỹ^{(k)} lives on ker D^{(k)*}, and
  G_gh,n is exact (GH-log (c), at U_f).
- The growth of LONG-n and (W6) enters the L-split pieces Φ^L_k and log det W_n with opposite signs, and cancels in pairs
  (Reading (2), with corrected sign).
- So it is not a contribution to β. It is the same structural fact as S11's G2 cancellation, one level down.

**What T-tel does NOT settle.** n-uniformity of φ^T_k at U_f, which is (T-a)-(T-c). In particular, T-tel alone does not show that the
growth cannot re-enter Ỹ through the U-dependence of P_k. §4 (S12-4) shows that it cannot, PROVIDED a covariant
decomposition exists at U.

**Remaining checks.**
- (iii) Sylvester. ✓
- Reading (3), Woodbury one-step form: re-derived. ✓
- **Reading (2) sign error (S12-1).** By Jacobi, log det_⊥Ỹ = log det Y + log det(V^*Y^{-1}V). So Φ^T_k − Φ^L_k =
  **+**log det(V_{k+1}^*Y^{(k+1)-1}V_{k+1}) **−** log det(V_k^*Y^{(k)-1}V_k). The text has both signs reversed (numerically confirmed, §0).
- **Reading (4).** The identification with l.839 needs l.839's Π to be read as P_n(P_n𝒞_nP_n)^{-1}P_n, and its "P_⊥" as the LEVEL
  transverse projector P_n. §94 uses P_⊥ = P_0, the FINE projector, so this is a notation clash. State it explicitly.

**T-tel VERDICT: CONFIRMED, exact.** W_n, G2, (GP-L) and (GP) are genuinely not needed for the total, and the longitudinal growth
genuinely drops out of c^tot_n.

## 4. Priority 4: Proposition VC-T0 (§98)

**(a) The one-step closed form.**
- Axial legs: (e^{ik_αy_α} − e^{ik_αc_α})/(e^{ik_α} − 1). Averaging over y gives D_L. The order-average weight is ¼Σ_sC(3, s)^{-1}e_s(other D's), and
  the script implements exactly this.
- The script's contour sums use PROOF.md's T^σ_y = P^σ(c_X → y)S_yP^σ(c_Y → y + Le_μ)^†. ✓ B0(i) 6e-15.

**Composite.** (Q_str,k − dh_k)(Q_str^{(k)} − dh^{(k)}) = Q_str^{(k+1)} − d[ev h^{(k)} + h_kQ_str^{(k)}], using Q_str∘d = d∘(ev + h∘d) and IT-str. ✓
- Covariance telescoping: Σ_j[ΠD_L(L^jk) − 1]ΠD_{L^j}(k) = ΠD_ℓ − 1. ✓ B0(ii), (iii).

**(b), (c).**
- P_{T,ℓ}D̂_ℓ = 0 removes d∘h. Q̂_strŝ = D̂_ℓΠD removes the fine longitudinal part. Q̂_str is diagonal. ✓
- P_nA_j = P_nQ_str^{(L^i)}. ✓
- ‖s_i‖ ≤ L^{-2i}: the Schur test is right, and directly Σ_m|D_r|² = 1 and Σ_m|S_rD_r|² = O(r²). ✓

**Rate.**
- The relative-error factors are 1 + O(|x|²/ℓ²) on |x_α| ≤ πℓ. The arguments are ≤ π/2, so the ratios stay bounded. ✓
- The difference bound Cℓ^{-2}Π_αmin(1, π²/x_α²) is a product of summable 1D sums. ✓
- **Wording (S12-5).** The m = 0 term makes x^{blk}_n itself ~1/|K|² as K → 0. Only the DIFFERENCE is uniform. "Uniformly down to K = 0
  with no normalisation needed" (Reading (1)) should say so.

**Scope (S12-4, the main new point of this review).**
- (b) is exact at U = 1 only.
- At U ≠ 1, for ANY decomposition A_j(U) = Q_j(U) − D_n(U)h_j(U) (h_j(U) free; Q_j(U) defined by this), one has
  P_n(U)A_j(U)A_j(U)^*P_n(U) = P_n(U)Q_jQ_j^*P_n(U) EXACTLY. The DhQ^*, Qh^*D^* and Dhh^*D^* terms are all killed by P_n(U)D_n(U) = 0, and
  the same holds for the M-part.
- So the LONG-n/(W6) growth, which is a D_n(·)D_n^* term, can never leak into the T-split at any order in ε, **provided** h_j(U) can be
  chosen (for instance by background-transported radial slices) so that Q_j(U) has n-uniform, L^{-i}-summable ε-data.
- With the U = 1 choice h_j(1), the ε-expansion of P_n(U) instead produces, at second order, a term [ε]P·(d hh^Td^T)·[ε]P ~ n|D̂|² from
  the growing block. So the choice of h_j(U) is load-bearing.
- This is the precise form of (T-a)'s "ε-expansion of T_k(U)", and it should replace the vague wording.

**(W6).** ARGUED, constant c_h = 2.2594e-4 at both K. ✓ It is not counted. ✓

**Verdict.** **VC-T0: CONFIRMED (U = 1, zeroth order).**

## 5. Priority 5: the remaining UNIV list (§99)

§99's list is (L-loc2), (T-a), (T-b), (T-c), plus the unchanged rate and cross-lane items. Corrections:

1. **The plane-wave form factor of 𝔪_n is EASY and should leave the wall list.**
   - At a Cartan configuration inside D′, every S^{-1}T^σ_y is diagonal with eigen-angles < π/3. The principal logs are linear in a,
     so the average is linear.
   - Hence 𝔪(U) = exp((Q_root a)H_1) EXACTLY, and composites stay Cartan, so 𝔪_n(U_pw) = exp((Q_root^{(n)}a)H_1).
   - Q_root a = Q_str a − d(ha) is a level gauge transform of the plane wave with amplitude ε̃·D_ℓ(p)/(…). This is explicit, with an
     ℓ^{-2} rate (ℓsin(p/2) → P/2).
   - Write it as a lemma, a few lines (W_♮ for N ≥ 3 is the same statement, with weights h_k).
2. **(T-a) must be restated** in the covariant-decomposition form of S12-4:
   - (T-a1) choose h_k(U) so that the first- and second-order plane-wave symbols of Q_k(U) := T_k(U) + D^{(k+1)}(U)h_k(U) (one-step and
     composite) are n-uniform and L^{-i}-summable;
   - (T-a2) the ε-expansion of P_k(U) = 1 − D^{(k)}Δ_k^{-1}D^{(k)*}. Its first-order term carries the massless level poles at K and K + P, so the
     normalisation is λ̃(K)λ̃(K + P) (twice the λ̃ of the scalar template). P_{T,ℓ} itself is non-analytic at K = 0; analyticity
     is only for λ̃P_T = λ̃ − D̂D̂^†.
   - Then the degree-4 numerator statement as in Lemma VC.
3. **(T-b)** is precise as stated: the plane-wave density of H_⊥ + M̃^T(P_n𝒞_nP_n)^{-1}M̃ to the polarisation form. Its operator
   contains two nonlocal projectors (P_⊥ fine, P_n level). The fine one is already handled (VFINE-L, PROVEN). The level one
   brings the same poles as (T-a2).
4. **(T-c)** is precise. The NO mode sits in Ỹ^{(0)} = H_⊥^{-1}P_⊥ (Woodbury, Reading (3)).

**Minimal list for the vector (UIR)/(V-IR):** (L-loc2); (T-a1); (T-a2); (T-b); (T-c). The rate and cross-lane items are unchanged.

**How hard, compared with the proven scalar items (S-2pt, S-tel, S-fix, FINE-IR, IR-id, UIR-S)?**
- **They are NOT transverse transcriptions.** All the scalar objects are local with analytic symbols.
- (T-a1) is new: it has no scalar counterpart (in the scalar proxy the covariance is trivial). It is a contour computation at a
  Cartan background, explicit but tensor-valued, and it is the crux. Estimate: hard.
- (T-a2) and the level projector in (T-b) bring nonlocal massless P_k(U). The scalar template never had poles in the vertex
  (only 1/λ̃ at zeroth order). Estimate: moderate-hard, with the λ̃(K)λ̃(K+P) normalisation and the K ↔ K + P symmetric pole
  handling as in §65 (b).
- (T-b) is otherwise S-red (ii) / §75 (b) in vector form: moderate.
- (T-c) is moderate. There is an alternative to the steps-only route: the local Jacobi form log det_⊥Ỹ = log det Y +
  log det(D^*Y^{-1}D) − log det(D^*D) trades the poles for a cancellation between two non-uniform local pieces. It is not
  recommended.

## 6. Priority 6: f15

- **Re-run: 25/25, identical** (§0).
- **Part A:** read line by line (§2).
  - A1: 1.3e-16 (SU(2), SU(3), 3 roots with h̄ ≠ 0).
  - A1x: 2.3e-16.
  - A2: 4.9e-11.
  - A3: E1 = 3.2e-3, 6.1e-3, 5.0e-3 at s = 0.01, halving with s. The spin-1 control has E1 ≥ 0.496.
  - E2 ≤ 3.8e-5.
  - All ✓. A1c (control) is weak (S12-7).
- **Part B:**
  - B0 6.0e-15 / 2.3e-14 / 9.5e-16.
  - B1 Δ-ratios 0.1111-0.1114 (K_a, K_b, K_c), s_i ratios 0.111, step control 1.2e-13.
  - B2 (the (W6) d∘h longitudinal increments): δ_n/|D̂|² = 2.2245, 2.2531, 2.2588, 2.2594e-4 (K_a), constant and K-independent.
  - B3: the straight path diverges (ratios 3.00).
  - B4 bound ✓.
  - What B1 tests: only the M-part P_T diag(x^blk)P_T, and the 𝒞-part via ‖s_i‖. This matches (W5) (c). ✓
- **The criteria were followed exactly**, with no post-run threshold change.

## 7. Per-item verdicts

| Item | Verdict | Fix |
|---|---|---|
| Provenance | **CLEAN**; §94 byte-identity re-verified by md5 reconstruction | S12-8 |
| [RFL11-fix] S11-1..S11-8 (25 pairs) | **APPLIED**, correct | S12-8 (forward refs) |
| Step-1 minimal list | correct | — |
| Lemma CL-V (W2) | **CONFIRMED** | S12-6, S12-7 |
| Corollary VFINE-K-val | **CONFIRMED** (corollary) | — |
| Lemma T-tel (W3) | **CONFIRMED**, exact (+ generic numerics) | S12-1 (sign), S12-3 (notation) |
| Prop LONG-n (W4) | **CONFIRMED for Y_n**; W_n clause unproven | S12-2 |
| Prop VC-T0 (W5) | **CONFIRMED at U = 1** | S12-4, S12-5 |
| (W6) | ARGUED, consistent with f15 B2 | — |
| (W7) / §99 list | correct verdict (UNIV not yet on (L-loc2) alone); list imprecise, not minimal | S12-4, S12-9 |
| f15 | **CONFIRMED**; re-run identical 25/25 | S12-7 |

## 8. Corrected tally

**70 PROVEN-HERE (claimed 70)** = 65 + CL-V + VFINE-K-val + T-tel + LONG-n + VC-T0.
- **Strict: 66 (claimed 66)**, with VFINE-K-val folded into CL-V.
- Under the strict reading, T-tel (iii) duplicates the l.839 re-split. The new content, the closed recursion (i) and the exact
  telescoping (ii), justifies counting it.
- Scope notes:
  - LONG-n covers Y_n only (S12-2).
  - VC-T0 is U = 1, zeroth order.
- IMPORTED-AND-REVERIFIED: unchanged (L4b; the Lévy functional CLT). No new import. ✓
- ARGUED, not counted:
  - (L-loc2);
  - (W6);
  - the (GP) mechanism;
  - DEF-red;
  - the Cartan 𝔪_n form-factor lemma of §5 (1) (reviewer, not yet written).
- OPEN:
  - (T-a1);
  - (T-a2);
  - (T-b);
  - (T-c);
  - (L-loc2);
  - the rate and cross-lane items.

## 9. Binding fixes for the next lane-C session

1. **S12-1 (§96 Reading (2), l.4387-4388).** Correct the sign: Φ^T_k − Φ^L_k = +log det(V_{k+1}^*Y^{(k+1)-1}V_{k+1}) − log det(V_k^*Y^{(k)-1}V_k).
2. **S12-2 (§94 (W4) l.4276-4279; §97 Reading (1); §99; §101; §102).**
   - Restrict "FALSE" to Y_n.
   - Or add the Schur argument: Y_VT is bounded by the A_j = Q − dh decomposition, so W_n ~ 1/(cn) and log det W_n ~ −log n.
   - Name the COV-str (ii) soft-chain hypothesis.
3. **S12-3 (§96 Reading (4)).** Define l.839's Π := P_n(P_n𝒞_nP_n)^{-1}P_n, and note that l.839's "P_⊥" is the level projector P_n (§94's P_⊥ is fine).
4. **S12-4 (§98 Reading (1), §99 (T-a)).**
   - Add that (b) is a U = 1 identity.
   - At U, P_n(U)A_jA_j^*P_n(U) = P_n(U)Q_jQ_j^*P_n(U) holds for every decomposition A_j = Q_j − D_n(U)h_j, so the D(·)D^* growth never
     leaks, provided (T-a1).
   - Replace (T-a) by (T-a1) + (T-a2) as in §5 (2), including the λ̃(K)λ̃(K+P) normalisation and the non-analyticity of P_{T,ℓ}.
5. **S12-5 (§98 Reading (1), l.4434-4436).** "Uniformly down to K = 0" applies to Ỹ̂_n − Ỹ̂_∞. The symbol itself is ~|K|^{-2}.
6. **S12-6 (§94 (W2) (c), §95 Corollary).**
   - "Equivalently §84's form with q → −q" holds with D and F both flipping. Equivalently, §84 (U6) l.3976's "+2iqF" should
     be tagged as superseded by −2iqF (D = ∂ + iqa).
   - The relative sign does not enter C_{K_F} (tr A = 0). f15 A3 fixes it anyway.
7. **S12-7 (§95 Reading (2), §100).** Say that A1c is a weak control: the spin term is ≈1% of the Hessian at this background. The
   spin test is A3c.
8. **S12-8 (FLOW_LOG; l.4082, l.4156).**
   - The S11-1 and S11-7 [RFL11-fix] tags, written 10:44-10:47, cite "session 12, Lemma T-tel / VC-T0" as results, before those
     proofs existed (11:01). Re-tag them as forward references ("see §96, §98").
   - Log the fix95 extra factor 2 as a proof slip (not wording).
9. **S12-9 (§99).** Move the plane-wave form factor of 𝔪_n at Cartan backgrounds off the wall list, as a short lemma (§5 (1)). The
   substantive item is the background linearisation T_k(U) (T-a1).

## 10. Next target

1. Apply S12-1..S12-9. The only status-relevant changes are S12-2 (scope of LONG-n) and S12-4/S12-9 (the restated (T-a)).
2. **Lemma Cartan-𝔪 (easy):** 𝔪_n(U) = exp((Q_root^{(n)}a)H_1) on D′ for Cartan U, with the explicit plane-wave amplitude and its ℓ^{-2} rate.
3. **(T-a1), the crux.**
   - Compute T_k(U) at the Cartan plane wave and at U_f, to first and second order in ε: the S4' contour linearisation with
     background phases, root sector.
   - Define h_k(U) by background-transported radial slices, and show that Q_k(U) = T_k(U) + D(U)h_k(U) has n-uniform,
     L^{-i}-summable symbols, with a residual ∝ the enclosed level flux.
   - Suggested check f16, pre-stated:
     - (i) the closed-form ε-vertices of Q_k(U) against finite differences of direct contour sums (≤ 1e-9);
     - (ii) L^{-2} convergence of the first- and second-order T-split vertex symbols of P_nQQ^*P_n, λ̃(K)λ̃(K+P)-normalised, at
       three K including a small one;
     - (iii) control: with h(1) in place of h(U), the second-order transverse vertex must grow ∝ n.
     - Jobs < 20 min and < 1 GB, under the lock.
4. Then (T-a2) (pole bookkeeping of P_k(U), as in §65 (b)), (T-b), (T-c), and (L-loc2).
