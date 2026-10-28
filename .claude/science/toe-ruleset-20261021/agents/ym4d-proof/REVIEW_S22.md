# REVIEW_S22: hostile review of session 22 (R21 fixes; Lemmas ENV, HG1, LOC_1, HG-ind; Corollaries H-fac, CURV1_1; TOWER-VAR; COMP; c38)

Reviewer: an independent agent that wrote none of the proof. I edited no other file. No commits, PRs or pushes.

Inputs:
- REVIEW_S21.md (format; its 7 binding fixes and recommendations).
- `diff PROOF_session21_snapshot.md PROOF_session22_snapshot.md`, all hunks. PROOF.md is byte-identical to the S22
  snapshot (`cmp`). The [S22] block (l.6137-6368) was read in full, together with Lemma CURV1 (l.5990-6050), Lemma LOC and
  Theorem NAH1 (l.5728-5820) and the (BG-unif) statement (l.5871-5895).
- RTARGET §47-49; LOG session 22 (l.982-1039, including "FOR OTHER FILES").
- checks/c38_criteria.md, c38_cubic.py (all 580 lines), c38{A,B,C,D}.out, c38_time.txt, and the file mtimes.
- Read-only: SQ.md ((REG-min) l.177-193; Σ_dec l.89-93), SF.md ((N5-unif) chain l.244-257; (a5-G♯), G-pert, (MIN-reg)
  l.650-680, l.795-822), FLOW.md ((SF-bg) l.189-192), RLARGE.md ((BG)_k l.324-326).

Re-runs and diagnostics (scratchpad `rev22/`, copies of c38_cubic.py, c37_kcurv.py and c35_n5bg.py; my diagnostic
`rdiag22.py`; runner `run.sh`):
- Every job ran under the mandatory lock (`until mkdir …/locks/numeric; do sleep 20; done`, then load1 < 8 and memory free
  ≥ 25%, the jobs, then `rmdir` exactly once, no trap). There were two acquisitions: 04:20:28-04:29:51 UTC, and
  04:33:36-04:33:41 UTC (A only).
- nice 10, all BLAS threads 1, no `timeout`, python without -I. load1 was 2.6-4.5 and free memory 35-44%.
- No process of mine is left running. The lock directory is empty. The orphaned `rdiag.py` noted in LOG session 22 is no
  longer running.

---

## Bottom line

- **R21 fixes:** all 7 are applied correctly. One stale quotation remains in SF.md l.252 ("margin ≈ 10 … K_p^♯ = 0.062,
  0.103"). That file belongs to another owner, so it goes under FOR OTHER FILES.
- **c38 is honestly recorded.**
  - The criteria (23:45:12 EDT) predate the first output (23:52:24).
  - The script mtime (23:56:52) is after B's output (23:55:04). That is the disclosed addition of Part D.
  - My re-runs of A, B, C and D are byte-identical in every number. So the A-C code that produced the stored outputs is
    the code now on disk.
  - B FAIL is recorded as a FAIL, and D is labelled post-hoc. **Accepted.**
- **"Far below E3's 1267": the conclusion is safe, but not for the reason given.**
  - The torus values R_3 = 1.13 and 1.40 are *lower* bounds for the ℤ⁴ value. The torus kernel is the periodisation of the
    ℤ⁴ kernel, so its ℓ¹ mass is ≤ the ℤ⁴ mass. They are not estimates, and they could be much smaller than the true value.
  - What makes the conclusion safe is my diagnostic L. It gives an *upper* bound, the absolute-leg N3^abs: 73.2, 90.8,
    111.1 and 131.9 at T = 4, 5, 6, 8. That is still growing, but the leg mass decays by a factor ≈ 2-2.5 per coarse shell.
  - Extrapolated, N3^abs(ℤ⁴) ≲ 170, so R_3(ℤ⁴) ≤ N3^abs/3 ≲ 60. That is ≥ 20 times below 1267, and it does not rely on any
    signed cancellation.
  - The signed ratio on ℤ⁴ is bracketed only as **1.40 ≤ R_3(ℤ⁴) ≲ 60**. "Signed ratio 1.1-1.4" must not be quoted as the
    value.
- **c38 C: the prediction is met and robust.** Three more random configurations give c_3 - c_2 ∝ s² with coefficients
  -2.3 to -3.2. But this is close to a gauge-invariance consistency check, and it is silent on the lattice-scale part that
  dominates N3. In B, the soft part carries 3.1-3.9 of N3, against 0.5-0.8 for the Wilson part.
- **ENV, H-fac, LOC_1, TOWER-VAR: CONFIRMED.**
- **HG1 and CURV1_1: CONFIRMED-WITH-FIX.** The "no near/far split is needed" claim is false *in the use*. HG1 (iii) holds in
  each link's own box gauge, but CURV1_1's assembly needs it in the single gauge of p's box. For links outside that box the
  error is first-order (≤ 30κ_0p_L𝔠_∞ε), and the decay of C_1 must absorb it, exactly as at level 0. There is also a missing
  Ad-conjugation term. Both are fixable.
- **HG-ind: the induction is genuinely closed. It is not circular.**
  - (H-G)_{i+1} needs CURV1_i (ρ part), which needs (H-G)_i, down to U0 (iv) at level 0. No step uses a statement at its own
    level or above.
  - **But it compounds at first order in two ways that the session does not record:**
    - (a) **r-compounding, avoidable.** HG-ind's sup bound |g_{i+1}| ≤ 2κ_ip_Lr^{(i)} feeds BR1_{i+1}'s radius, so r^{(i+1)}
      = 4κ_ip_L𝔠_∞^{(i+1)}r^{(i)}, which grows by ≥ 10³ per level. The cure is to use HG1 (iii) instead of (iv).
    - (b) **θ-compounding, not avoidable in sup norms.** CURV1_{i+1} at θ needs CURV1_i at θ' = θ/(16κ_i𝔠_∞^{(i+1)}). So
      level 0 runs at θ(16κ𝔠_∞)^{-k}, its box ℓ_θ grows linearly in the depth k, and ε_θ ∝ 1/ℓ_θ → 0 like 1/k.
  - So Proposition NAH-unif′'s proof is **GAP as written**: it uses one θ at every level. Its hypothesis (H-C⁺) must
    include the θ-cascade.
  - CURV-F2′ is the same phenomenon as CURV-F2 (E3's recursion): C_G is the localised second derivative of ∇E^br, the
    object c38 measures. "(H-G) is not an independent hypothesis" is correct only as "derivable at each fixed level".
- **COMP: GAP as an implication.** The identification "fixed point = tower" needs an unnamed hypothesis (per-level
  existence and uniqueness in balls that contain the composite fixed point's components, i.e. (CL-4)). Without it COMP
  delivers (BG-unif)-type bounds for the *composite* critical point, not for the per-level tower.
- **COMP-F1:** the mechanism is correct, and it is independently corroborated: SF/HIST found that the sup-norm (a5-G) is
  FALSE, with ||𝓛⁻¹||_{∞→∞} ≳ L^{2(k-1)}. But the stated growth rates are inferences, so "OCCURS" should read "occurs
  [inference, no lower-bound input exhibited]".
- **(CL-cl): the right object, misstated.**
  - The irrelevant part is bounded (it tends to the classical perfect action's part), not shrinking. c38 B shows it
    dominates N3 at level 1.
  - At tree level the marginal coefficient is fixed (c_i → 1), not a flowing c_i.
  - It is an *output* of the composite route and the *input* of the per-level route.
- **Yes, five lanes are converging on one background-field theorem.** The PROOF lane (BG-unif)/(H-C⁺)/(H-ℂ)/(CL-cl), FLOW
  (SF-bg), RLARGE (BG)_k, SF (a5-G♯)/(a5-U)/(MIN-reg) and, in a cone-local sibling form, SQ (REG-min) all ask for parts of
  one statement, **BFT** (Part 5).
- **Tally: 72 / 2 / 7 / 24 + 1, as claimed.** Nothing new is counted, and nothing should be.

---

# PART 1: the R21 fixes (REVIEW_S21 binding fixes 1-7)

| # | Fix | Where (PROOF) | Verdict |
|---|---|---|---|
| S21-1 | one torus for all ε ≤ ε_H | NAH1 l.5766; N5-sf1 l.5822 | **Applied correctly.** It freezes at an admissible ε_♯ ≤ ε_H rather than at ε_H itself, which is necessary because the conditions are not monotone. The monotonicity of δ_H in α' and α decreasing with ε are checked |
| S21-2 | K_p^♯ quotations | l.10, 39, 68, 5869, 5993-5994, 6049, 6096, 6106, 6127, 6133; RTARGET l.833; LOG l.966 | **Applied** everywhere in this lane's files (grep-verified). The old bold text is kept with an inline correction, which is acceptable. **Residue:** SF.md l.252 still says "margin ≈ 10 … 0.062, 0.103" (another owner; FOR OTHER FILES) |
| S21-3 | 14ε_V; 56; 104 | l.5998, 6025, 6036, 6040 | **Applied correctly** |
| S21-4 | E3 coefficient | l.6102 | **Applied** (157.08 × 14.81 ≈ 2.3·10³) |
| S21-5 | NAH-unif GAP; (H-G), (H-ℂ) | l.6070, 6083-6091 | **Applied verbatim in substance.** The false sentence is withdrawn |
| S21-6 | η_*, C_θ^ρ | l.6077, 6081-6084 | **Applied correctly** |
| S21-7 | stale LOG/RLARGE items | LOG l.944; LOG session 22 FOR OTHER FILES 1 | **Applied** |

Minor: TOWER-VAR (b) (l.6303) says "≤ 6ε_k per link". This agrees with U0 (iv)'s stated bound. But U0 (iv) and CURV1 step (3)
(|π(e^F)| ≤ 1.2|F| ⇒ 7.2ε) disagree about the same quantity. Reconcile U0 (iv) once: either |Re tr(XW)| ≤ |X||log W|
gives 6ε exactly, or it is 7.2ε. This is cosmetic.

---

# PART 2: c38

## Pre-registration and honesty: CONFIRMED

- **Mtimes (EDT):** criteria 23:45:12 (4649 B, as stat'ed into LOG); A out 23:52:24; C 23:52:57; B 23:55:04; script
  23:56:52; D 23:59:06; record 00:02:26.
- **The script is newer than A-C's outputs.** This is the disclosed addition of Part D. My byte-for-byte re-run of A-C
  (below) shows that the A-C code paths are unchanged in effect.
- **B FAIL:** the stability clause (|R_3(5) - R_3(4)| = 0.269 > 0.140) is recorded as FAIL in PROOF l.6273, RTARGET §49 and
  LOG, with no criterion edited.
- **D (post-hoc)** is labelled post-hoc and does not rewrite B.
- **Pre-run edit:** the fibre dictionaries were slimmed before the first run. This is disclosed.

## Re-run (identical)

| Part | Result | Peak | vs stored |
|---|---|---|---|
| A | PASS (A1 6.0e-15 … Hfac 1.3e-14; A2 0.9999999709; A3 0.9999999690) | 607 MB | identical |
| C | c_3 0.974468, 0.997664, 0.999740, 0.999977; c_2 0.991216 … 0.999992 | 81 MB | identical |
| B | N3(T_E) 3.380437 / 4.186756; R_3 1.126812 / 1.395584; N3^abs 73.2067 / 90.8260; FAIL | 935 MB | identical |
| D | shells 0, 1.4734, 1.9071 (T = 4); 0, 1.4103, 2.7765 (T = 5) | 892 MB | identical |

(The first A attempt failed on a missing import of c35_n5bg in my copy, not in the lane's code. I copied the module and
re-ran A under its own lock acquisition.)

## Script audit (line level)

- Û = κM⁺Q† (pseudo-inverse with a relative cut of 1e-9). The fine-gauge ambiguity drops out at cubic order because
  ∇_uG_2(ÛB, B) = 0 (A1: 6e-15). I checked this against Lemma E3's identity: the D²F[(w, 0), ζ] terms vanish for fine w.
  Correct.
- `vertex_batch`: slot 1 is the differentiated leg (dÛ for Wilson, QÛ - 1 for soft), slots 2 and 3 are potential legs.
  `antisym_torus` antisymmetrises over simultaneous (momentum, index) permutations with the right signs. The kernel is
  unique (only the totally antisymmetric part couples to ε_abc).
- `n3_from_VA`: N3 = max over the slot-1 direction of the ℓ¹ sum over (R2, R3, ν, λ). This is the right comparator for
  C_♭ at the trivial background: N_0(D Hess[δV]) ≤ N3·|δV|_∞ up to the common colour factor.
- `abs_bound`: the slot average (N1 + N2 + N3)/3 is a valid upper bound for the antisymmetrised kernel (max of an average ≤
  the average of maxima).
- **Key structural fact not stated in the record.** On a torus the kernel is the periodisation of the ℤ⁴ kernel (Poisson
  summation over the momentum grid). Hence:
  - Σ|t_T| ≤ Σ|t_ℤ⁴|: **every torus N3 is a lower bound for N3(ℤ⁴)**;
  - N3^abs_T is an upper bound for N3_T, and it converges to N3^abs(ℤ⁴) as T grows.
  - On T = 4 and T = 5 the largest torus distance is 2 in both cases, so "shell 2" also collects every wrapped image.

## Diagnostic L (mine; not a c38 criterion): the absolute-leg bound and the leg kernel on larger tori

| T | N3^abs(T_E) | max row ℓ¹: Û / dÛ / QÛ - 1 | max col ℓ¹ Û | Û mass by coarse shell 0, 1, 2, 3, 4 |
|---|---|---|---|---|
| 4 | 73.21 | 2.668 / 0.171 / 4.576 | 39.25 | 12.6, 84.4, 60.0 |
| 5 | 90.83 | 2.950 / 0.186 / 4.805 | 41.07 | 12.5, 76.5, 75.2 |
| 6 | 111.09 | 3.247 / 0.204 / 5.068 | 43.08 | 12.5, 74.8, 58.7, 26.4 |
| 8 | 131.86 | 3.525 / 0.216 / 5.227 | 45.30 | 12.5, 74.3, 53.7, 29.6, 11.1 |

Readings:
- The leg mass decays by ≈ 2-2.7 per coarse shell beyond shell 2.
- The increments of N3^abs are slowing (+17.6, +20.3, +20.8 over two units of T). A geometric tail with ratio ≈ 0.4-0.5
  gives **N3^abs(ℤ⁴) ≈ 150-170** (extrapolation, not converged, float).
- **So 4.19 ≤ N3(T_E; ℤ⁴) ≤ N3^abs(ℤ⁴) ≲ 170, i.e. 1.40 ≤ R_3(ℤ⁴) ≲ 60.**
- The conclusion "C38-F1 does not occur, far below E3's 1267" is **safe** at the level of a ≥ 20 times margin, by the
  absolute bound alone. The "three orders" figure and the quoted signed 1.1-1.4 are **not** safe: they are periodised lower
  bounds.
- Also notable: the column ℓ¹ of the pseudo-inverse-gauge leg is ≈ 45, against E3's Z_col = 156 in BR1's slice. Part of
  E3's 1267 is a slice artefact, which REVIEW_S21 anticipated.

## C and diagnostic C2

| config | s = 0.1 | 0.03 | 0.01 | c_3 - c_2 coefficient |
|---|---|---|---|---|
| c38 C | -1.67e-2 | -1.54e-3 | -1.71e-4 | -1.7 |
| C2 trial 0 | -3.14e-2 | -2.91e-3 | -3.25e-4 | -3.2 |
| C2 trial 1 | -2.22e-2 | -2.06e-3 | -2.29e-4 | -2.3 |
| C2 trial 2 | -2.62e-2 | -2.42e-3 | -2.69e-4 | -2.7 |

(These are c_3 - c_2 values; c_2 → 1 in every case.)

- The prediction is met robustly, and the coefficient is configuration-dependent, as an O(K²) remainder should be.
- **Reading (binding: fix S22-2).** The result is what gauge invariance plus locality of E_1^br force: the leading
  small-momentum gauge-invariant cubic is tied to the quadratic coefficient. c_2 → 1 is tree-level preservation of the
  marginal coefficient.
- It says nothing about the lattice-scale structure, which carries N3 and hence C_♭. In B the soft part is 3.14 / 3.90 of
  N3 and the Wilson part 0.52 / 0.76. "C supports the artefact reading" holds only for the marginal direction.

## Verdict on c38's reading (PROOF l.6288-6293, RTARGET §49, LOG)

The sentence "the signed ratio is 1.1-1.4, three orders below E3's … 1267" must be replaced by:

> "R_3(ℤ⁴) ∈ [1.40, ≈ 60] (periodised lower bound; absolute-leg upper bound N3^abs ≈ 73-132 on T = 4-8, extrapolated
> ≲ 170, REVIEW_S22 L): at least ≈ 20 times below E3's 1267. The signed value on ℤ⁴ is not measured."

The rest of the "Not shown" list is accurate.

---

# PART 3: the (H-G) chain

## Lemma ENV (l.6164-6171): CONFIRMED

- The envelope step needs criticality in *every* fine direction, because the slice may depend on V. This is stated
  ("without fixing", BR1 (ii)).
- The derivative is right. Re tr(XW) = Re tr(X·(W - W†)/2), the Hermitian part gives an imaginary trace, and the trace part
  vanishes because tr X = 0. So ⟨X, ∇E⟩ = -κ⟨X, π(M̄V⁻¹)⟩.
- The W_0-term does not depend on V.

## Corollary H-fac (l.6172-6176): CONFIRMED

- ∇E^br = -κπ(M̄V⁻¹) linearises to -κ(QÛ - 1)B = -κ𝒦_ρd_1B.
- c38 A1 verifies H = -κR = -κ𝒦_ρd_1 to 1.3e-14, and I reproduced it.
- The resulting 𝒦^{(1)} = (1 + κ_0dC^{(1)}𝒦_ρ)ι^{(1)} has the right signs (-C^{(1)}H_1J = +κ_0C^{(1)}𝒦_ριd).
- Notation: ι and ι^{(1)} are used for the same map in l.6176 and l.6184. Unify them.

## Lemma HG1 (l.6177-6195): CONFIRMED-WITH-FIX

- **(i), (ii), (iv): correct.** (ii): φ̂ ≥ 0, with equality at W_0(M̄) = W, so it is stationary at the lift. (iv):
  |π(M̄V⁻¹)| ≤ avg|Y_j| + c_π(p_Lr)³ ≤ 2p_Lr = 24p_L𝔠_∞ε.
- **(iii): correct as a per-link statement in c's own box gauge,** given CURV1's ρ-proof. That proof does produce the
  vector statement avg_jY_j = (QA*)_c + O(αr + (p_Lr)²), with QA* = 𝒦_ρF^G + (θ-terms) + O(ε²) before X_0. The Z' tail
  term is not needed for the vector form, so it is only an overestimate.
- **Fix S22-3a (conjugation).** M̄_c = h(avg e^{Y_j})h⁻¹V_c "up to conjugation". The vector comparison needs
  ||Ad(h) - 1|| ≤ 9α, which adds ≤ 9α·2p_Lr = 648ℓ_{θ'}p_L𝔠_∞ε² to C_G. In the norm statements of CURV1 this was invisible.
  Here it is a constants change.
- **Fix S22-3b (the overclaim at l.6185-6186).** "No near/far split is needed" is false for the use in CURV1_1.
  - The identity g_1(c) ≈ -κ_0(𝒦_ρF^G)(c) mixes curvature frames at the plaquettes P near c. It holds in a gauge that is
    AX-small around c.
  - CURV1_1 sums dC_1(p, c)e_{g,1}(c) over all c in the one gauge of p's box. Outside that box the gauge is arbitrary
    ("extended arbitrarily", CURV1 proof), and the frames differ by O(1).
  - So e_{g,1}(c) is only bounded by |g_1| + |𝒦_ρF| ≤ (24 + 6)κ_0p_L𝔠_∞ε there: *first order*.
  - Restore the level-0 structure. Near part (c within D_g of p, and c's ℓ_{θ'}-box inside p's box): HG1's bound. Here
    p's gauge is AX-small on c's box, which is all CURV1's proof uses. This needs the nesting condition ℓ_θ^{(1)} ≥
    2(D_g^{(1)} + ⌈ℓ_{θ'}/L⌉) + O(1). Far part: 30κ_0p_L𝔠_∞ε times the decay c_K^{(1)}τ^{(1)}(D_g). This adds
    4·30κ_0p_L𝔠_∞c_K^{(1)}τ^{(1)}(D_g) to D_g's defining condition.
  - The result: still a correct lemma, and still exponentially small first-order error, but **with** a near/far split.

## Lemma LOC_1 (l.6196-6209): CONFIRMED

- Change (a): δ_box in place of C_Δα' is legitimate, and CT♯ needs δ_box ≤ γ_1/4.
- Change (b): with K - K^♮ exponentially decaying instead of finite range, the triple sum Σ|K⁻¹||K - K^♮||(K^♮)⁻¹| has two
  internal sums. Splitting the weight along b → z → z' → b' costs one more coth⁴(m/4). This is right *provided* the decay
  rate of the entries of Õ_1(V, W) (NAH1 (c): m ≤ μ_1/2) is ≥ m^{(1)}. Make "m^{(1)} ≤ m" explicit.
- The δ_box bound "by NAH1 (b)'s proof on Λ'' with ρ := its diameter" requires the gauge box to have side ℓ_1(diam Λ'', D).
  That is what NAH1's proof needs; fine with constants.

## Corollary CURV1_1 (l.6210-6229): CONFIRMED-WITH-FIX

- Steps (1), (2), (4), (5) and the ρ statement are right.
- Thresholds: the BCH step needs s = 4r^{(1)} + ε ≤ 1/53, i.e. ε ≲ 1/(10⁴κ_0p_L𝔠_∞𝔠_∞^{(1)}). This is part of "the level-1
  ε_θ". Write it explicitly.
- Step (3) and l.6224 need fix S22-3b: the uniform bound 4𝔠_∞^{(1)}κ_0(θ' + C_Gε)ε holds only for the near part.
- The log factor (1 + log(1/ε)) from δ_box = O(ε log 1/ε) is correct.

## Lemma HG-ind (l.6230-6237): the induction is NON-CIRCULAR; GAP in level-uniformity, with two compounding mechanisms not recorded

- **Is it circular? No.**
  - CURV1_{i+1} uses (H-G)_{i+1} (gradient of E_{i+1}^br at level-(i+1) lifts), LOC_{i+1} and BR1_{i+1}.
  - (H-G)_{i+1} uses CURV1_i (ρ part) applied to the level-(i+1) lift V = U^{(i+1)}(W) of the level-(i+2) field. That is an
    auxiliary application on lifts, not on the tower.
  - CURV1_i uses (H-G)_i, and so on down to U0 (iv). It is a well-founded upward induction.
  - For i ≥ 2 it is conditional on NAH-ind's (I_i) (LOC_{i+1} "as LOC_1" needs NAH1 at level i + 1, which is only an
    implication). The label "PROVEN-HERE (as an implication)" is accurate.
- **(a) r-compounding (avoidable): fix S22-4.**
  - |g_{i+1}|_∞ ≤ 2κ_ip_Lr^{(i)} feeds BR1_{i+1}: r^{(i+1)} = 2𝔠_∞^{(i+1)}|g_{i+1}| = 4κ_ip_L𝔠_∞^{(i+1)}r^{(i)}.
  - At L = 3 (p_L = 11) and 𝔠_∞ ≥ 25 that is ≥ 1.1·10³ per level.
  - Both |Y_j| ≤ p_Lr^{(i)} ≤ 1/20 and C_G^{(i)} ∋ c_π(p_Lr^{(i)}/ε)³ then force ε ≲ (10³)^{-i}.
  - This is not in CURV-F2′, and it is not needed. Bound g_{i+1} through HG1 (iii) (curvature form) instead:
    |g_{i+1}|_∞ ≤ κ_i(N_0(|𝒦_ρ^{(i)}|) + θ' + C_G^{(i)}ε)ε. Then r^{(i+1)} ≤ 2𝔠_∞^{(i+1)}κ_i(N_0(|𝒦_ρ^{(i)}|) + 1)ε, which
    depends on two consecutive levels' constants only.
  - The same correction applies to l.6191-6194 (r^{(1)}): 24p_L𝔠_∞ there is the same order as N_0(|𝒦_ρ|) ≤ 6p_L𝔠_∞ at level
    1, but only the curvature form is non-recursive.
- **(b) θ-compounding (unavoidable in sup norms): fix S22-5, new failure mode CURV-F2″, OCCURS.**
  - CURV1_1 takes θ' := θ/(16κ_0𝔠_∞^{(1)}) at level 0 (l.6212). Iterated, CURV1_k at θ needs CURV1_0 at θ_0 =
    θ·Π_j(16κ_j𝔠_∞^{(j+1)})⁻¹.
  - θ is the first-order localisation error: exponentially small in the box size, θ ~ e^{-m_1D_g/2}. So D_g^{(0)}, and
    with it ℓ_θ^{(0)}, grow **linearly in the depth k**.
  - Since ε_θ ∝ 1/ℓ_θ (α_*/(12ℓ_θ), 1/(60ℓ_θ)) and C_θ ∝ ℓ_θ, this gives ε_unif = O(1/k) even if every 𝔠_∞^{(i)}, κ_i and
    C_♭^{(i)} were level-uniform.
  - The mechanism is the same absolute step |dC e|_∞ ≤ 4𝔠_∞|e|_∞, now acting on the first-order error.
- **CURV-F2′ (l.6238-6249): CONFIRMED as a route failure, with a wording fix.**
  - "C_θ^{(i)} ≥ Π(4κ𝔠_∞)" is a statement about the *bound produced by this route*, not about the true constant. Say so.
  - Also note what C_G^{(i)} is: the localised second-order coefficient of ∇E_{i+1}^br at the lift, i.e. a localised
    D³E_{i+1}^br, the object c38 measures at the trivial background.
  - **CURV-F2′ is CURV-F2 in another coordinate**, not an independent wall.

## Proposition NAH-unif′ (l.6250-6254): GAP as written (fix S22-5)

- Its proof runs CURV1_j at one θ at every level, with HG-ind supplying step (3). HG-ind requires CURV1_{j-1} at θ', and
  so on.
- The implication is valid only if (H-C⁺) is extended to the cascade: *level-uniform ε_θ^{(i)}, ℓ_θ^{(i)}, C_θ^{(i)},
  C_θ^{ρ,(i)} at θ_i = θ·Π_{j≥i}(16κ_j𝔠_∞^{(j+1)})⁻¹*. Equivalently, it needs a non-recursive (H-G).
- HG-ind's own mechanism makes that extended (H-C⁺) false *as produced by this route*. So NAH-unif′ is a correct but
  empty-by-route implication. The per-level route needs (H-G) from (CL-cl)/BFT, not from HG-ind.
- "(H-G) is derived (HG-ind)" (l.6253) must read: "(H-G) is derived at each fixed level. Its level-uniform form is not, and
  is ⊂ (H-C⁺)/BFT-4".

## (H-ℂ) (l.6255-6259): status OPEN, correctly labelled; the ARGUED route is plausible

- The holomorphic π_ℂ and the complex covariance bounds of N5-sf0 (b) are the right ingredients.
- The radius r_ℂε with (1 + 4r_ℂ)ε is unverified and unwritten. Keep it ARGUED.

---

# PART 4: the composite route

## Lemma TOWER-VAR (l.6295-6318): CONFIRMED (algebraic)

- (a) ∂_{U_j}𝔉_k = ∂_{U_j}[κ_{j-1}φ̂^{(j-1)}] + ∂_{U_j}[κ_jφ̂^{(j)}]. ENV converts the first term to ∇E_j^br(U_j), since
  U_{j-1} = U_{j-1}(U_j) on the tower. The sum is ∇F_j = 0. The value telescopes. Correct.
- (b) Iterated U0, and π(1) = 0 in the coarse slot. Correct.
- (c) A pointer to Setting SC / N2-lin. Accepted.
- (d) D³E = D³𝔉[ζ, ζ, ζ] + 3D²𝔉[(D²Z, 0), ζ] + D𝔉[D³Z]. The last term vanishes by criticality. The middle term vanishes
  *at the trivial background*, where ζ is critical for the quadratic part in every fine direction. Correct as stated, at 1
  only.
- Note: (a) is one-directional, tower ⇒ critical point. The converse is what COMP needs.

## Proposition COMP (l.6319-6331): GAP as an implication (fix S22-6)

- **The Banach part is right.**
  - ||Φ(0)|| ≤ C_1ε, Lip ≤ 4C_1C_2ε ≤ ½, and the self-map of the 2C_1ε ball given ε ≤ r_0/(2C_1).
  - Implicit and required: 𝔊_k maps into S_k (so Φ(S_k) ⊂ S_k), and 𝔊_kHess𝔉_k = 1 on S_k, with the fixing annihilating
    S_k. Without the latter, (1 - 𝔊Hess)(X - X') is not 0, and (CL-2)'s remainder form does not give the Lipschitz bound.
    Add both as part of (CL-0).
- **The gap: "when it is the tower (TOWER-VAR (a) and per-level uniqueness)".**
  - Identifying the composite fixed point with the per-level tower (the object E_k^br, N5 and the RG use) needs: each U_j of
    the composite fixed point is the per-level branch U_j(U_{j+1}).
  - ∂_{U_j}𝔉 = 0 gives "U_j is *a* critical point of F_j(·, U_{j+1})" only once E_j^br is known to exist along the composite
    components, and "*the* branch" only with per-level uniqueness in a ball containing it.
  - BR1's level-j uniqueness ball is centred at the lift U^{(j)}(U_{j+1}), not at the composite lift's component. Its
    radius is the non-uniform r^{(j)}.
  - Name it **(CL-4)** (per-level existence and uniqueness of the branches in balls that contain the composite fixed point's
    components, with the composite fixed point's displacement relative to U^{(j)}(U_{j+1}) controlled).
  - Or adopt Balaban's convention: *define* the background as the composite critical point and re-derive the per-level
    recursion E_{k+1}^br = F_k-value from composite uniqueness.
  - Without one of these, COMP proves (BG-unif) (i)-(ii) for the composite critical point only.
- The holomorphy is standard.

## COMP-F1 (l.6332-6350): mechanism CONFIRMED; label to be softened (fix S22-7)

- The non-closed second-order remainder against Π_ex's |x|^{-4} kernel (log growth over a block of side L^k) is the right
  mechanism. So is the |x|^{-3} response to non-divergence-form sources (linear growth).
- The (W1) power count (an ε²L^{-3k} source over side L^k gives relative ε) is right.
- **Independent corroboration (not cited in [S22]).** SF §6.2 / REVIEW_HIST_S4 S4-1: the sup-norm (a5-G) is FALSE at the
  trivial chain, with ||𝓛⁻¹||_{ℓ^∞→ℓ^∞} ≳ L^{2(k-1)}. That is the same phenomenon at the potential level (one derivative
  more), and its cure was SF's §33 pair (Hölder X_c, a divergence-form Y with level weights ω_l = L^{θ(k-l)}). That pair is
  a concrete candidate for 𝔐, in which (CL-2) should be tested. It is (W1) + (W2) in one norm.
- The growth rates in COMP-F1 are "[inference from the tails]" and no lower-bound input is exhibited. Write "COMP-F1 occurs
  [inference]".

## (CL-cl) (l.6351-6356): the right OBJECT, misstated; it is not by itself the target (fix S22-8)

- **"Shrinking irrelevant part" is wrong.**
  - Iterating the classical block step converges (if at all) to the classical perfect action S_*, whose irrelevant part
    relative to S_W is O(1) at the cutoff scale.
  - c38 B already shows this at level 1: the non-Wilson (soft) part of the cubic vertex carries 3.1-3.9 of N3, against
    0.5-0.8 for the Wilson part.
  - What is needed, and what suffices, is **boundedness** in a fixed analytic class, with contraction *toward S_*'s
    irrelevant part* optional.
- **"c_i S_W" is not right either.** At tree level the marginal coefficient is preserved (c_2 → 1 exactly as K → 0; d = 4
  classical scale invariance, with β factoring out of the classical step). There is no flowing c_i. Write E_i^br = S_W +
  R_i with sup_i||R_i||_𝒜 < ∞.
- **"⊂ (BG-unif) (iv)" is the wrong direction.** (CL-cl) on a level-uniform polydisc implies (iv) (and (H-C⁺), (H-G)
  level-uniformly) by Cauchy estimates. It is stronger than (iv).
- **Routes.**
  - The composite route never needs (CL-cl) as input: 𝔉_k is explicit and local. Its wall is the norm 𝔐 ((CL-2)), and
    (CL-cl) is its output (via TOWER-VAR (a) and Cauchy).
  - The per-level route *can* use (CL-cl) as an induction hypothesis without compounding: if every per-level constant
    depends only on ||E_i^br - S_W||_𝒜, an inductive bound in a fixed ball replaces the Lipschitz recursion. Proving that
    the classical step maps the ball into itself is the analytic classical-RG problem, which is legitimate. But that
    self-map needs the same composite (multi-level) linear estimate in the analytic norm, since the classical step is
    marginal in d = 4.
  - So both routes meet at one theorem (BFT below), with (CL-cl) as its clause BFT-4. Is (CL-cl) the right target? Yes as
    a clause; the target is BFT.

---

# PART 5: one background-field theorem (BFT)

**Are several lanes converging on one theorem? Yes.**

| Lane item | What it asks | BFT clause |
|---|---|---|
| PROOF (BG-unif) (i)-(iv) [R20-fix 12] | composite-unique tower; own-units curvature ≤ Cε; holomorphy; derivative decay; Hess-Lipschitz | 0, 1 (undecayed suffices), 2, 3, 4 |
| PROOF (H-C⁺), (H-G) uniform, (H-ℂ), (CL-cl) | level-uniform derivative and gradient constants of E_i^br; complex radius; branch-action class | 4, 2 |
| PROOF COMP (CL-0)-(CL-4) | the composite contraction in a norm 𝔐 | the proof route of 0-2, in the norm 𝔐 below |
| FLOW (SF-bg) | the tree tower and 𝒯_k analytic on a k-uniform complex neighbourhood; derivatives ≤ 4 exponentially local at 1 | 2, 3 at the trivial field (TOWER-VAR (d) gives D³ explicitly) |
| RLARGE (BG)_k | locality radius R_bg of 𝔟(V) (load-bearing); one-step curvature C_IL^{-2} | 3; 1 (one-step form) |
| SF (a5-G♯), (a5-U), (MIN-reg) | (G♯) for the slice Hessian at non-trivial critical chains of E^♭ in the §33 pair; uniqueness of the chain minimiser | 5, 0 (E^♭'s critical chains are 𝔉_k's critical points) |
| SF (N5-unif) | level-uniform N5 thresholds | ⇐ 0, 1, 2, 4 (via NAH-ind/N5-sf_i, with (H-K) not needed) |
| SQ (REG-min) | cone-local, free-boundary *minimisers* in Σ_dec (decay L^{-2(k-i)}) | **a sibling, not a corollary**: the same weighted-sup absorption estimate as 1, on a cone with free boundary, without uniqueness |

**Statement (BFT).**

*Data:* N ≥ 2; L ≥ 3 odd; soft couplings κ_j ∈ [κ_-, κ_+]; F_j = E_j^br + κ_jΣ_cφ̂_c and 𝔉_k as in PROOF [S20]-[S22]
(TOWER-VAR); S_k a composite slice at the composite lift Z^lift(V_k).

*The norm 𝔐 (on composite displacements X, Z = e^XZ^lift):*
- level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)};
- curvature is measured in a Hölder (X_c-type) norm, and nonlinear sources in a divergence-form norm Y (SF/RTARGET §33's
  pair with ω_l = L^{θ_w(k-l)});
- exponential weights e^{±m d} are in level-k ancestor distance.
- The plain sup-curvature norm is excluded (COMP-F1; SF S4-1).

*Claim:* there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0, **depending only on (N, L, κ_±)**, such
that for **every** k ≥ 1, **every** torus whose level-k side is ≥ T_0 (and every non-wrapping box with the boundary
convention of N5-sf0), and **every** level-k field V_k = e^zV_k^r with V_k^r real, max_P|log V^r_{k,P}| ≤ ε ≤ ε_0 and
|z|_∞ ≤ r_ℂε:

- **BFT-0 (existence, uniqueness, identification).**
  - 𝔉_k(·; V_k) has a critical point Z(V_k) = (U_0, …, U_{k-1}) in {e^XZ^lift : X ∈ S_k, ||X||_𝔐 ≤ C_0ε}, unique there
    modulo composite gauges trivial at level k.
  - For real V_k, each U_j is the unique critical point of F_j(·, U_{j+1}) in its level-j ball (so Z(V_k) is the per-level
    tower), and E_k^br(V_k) = 𝔉_k(Z(V_k); V_k).
- **BFT-1 (scale-weighted regularity).** For every j < k: the own-units plaquette logs of U_j and the soft fluctuations
  ρ(U_j, U_{j+1}) are ≤ C_0L^{-θ_w(k-j)}ε, in Hölder form within each level-k block.
- **BFT-2 (analyticity).** Z(V_k) and E_k^br are holomorphic in z on |z|_∞ ≤ r_ℂε, and BFT-1 holds there.
- **BFT-3 (locality).** For n ≤ 4: |∂^nU_j(x)/∂V_k(y_1)⋯∂V_k(y_n)| ≤ C_0e^{-m_0 tree(x, y_1, …, y_n)} (block norms;
  level-k units; "tree" is the minimal spanning-tree length). The same holds for ∂^n E_k^br.
- **BFT-4 (branch-action class).** E_k^br = S_W + R_k with R_k = Σ_X R_k(X) a sum of gauge-invariant local polymers, and
  ||R_k||_𝒜 := Σ_{X∋0} sup_{polydisc}|R_k(X)|e^{m_0|X|} ≤ C_0.
  - The polydisc is the BFT-2 one in curvature-adapted coordinates.
  - Consequently, by Cauchy: C_♭^{(k)}, (H-G) and the C_θ, C_θ^ρ, ε_θ constants are level-uniform.
  - Optional strengthening: ||R_{k+1} - R_k||_𝒜 ≤ C_0λ^k (convergence to the classical perfect action).
- **BFT-5 (linear stability at the background).** The composite slice Hessian at Z(V_k) satisfies (G♯) in the 𝔐-pair with
  constants ≤ C_0. This follows from BFT-1/2 plus (G♯_0-field) + (R♯_ω) by SF's Lemma G-pert on X_c-small patches, and
  (G♯-patch) globally.
- **Anti-circularity:** the proof may not use the per-level covariances C^{(j)} as Newton inverses. It is one contraction
  for 𝔉_k in 𝔐 (COMP with (CL-0)-(CL-4) verified in 𝔐).

**Who needs which part.**
- PROOF/N5: BFT-0, 1 (θ_w = 0 suffices), 2 and 4. NAH-unif′, HG-ind's uniform form and (H-K) all become unnecessary.
- SF: BFT-1 (θ_w > 0), 2 (complex ball for (R♯)) and 5, giving (a5-G♯), (a5-U) and (MIN-reg). Also (N5-unif) from PROOF.
- FLOW: BFT-2 and 3 at z = 0, V_k = 1 (orders ≤ 4).
- RLARGE: BFT-3 (R_bg; load-bearing under v2) and BFT-1 one-step (C_I; not load-bearing).
- SQ: the cone-local analogue of BFT-1 for minimisers (REG-min). Its proof architecture (absorption in the weighted norm)
  is the same as BFT-1's, but it is not implied by BFT as stated.

**Smallest measurable piece:** c39 should measure the level-2 smooth-limit vertex and N3 on ℤ⁴ (a real-space truncation;
diagnostic L shows the legs decay by ≈ 2.5 per coarse shell, so a radius-6 truncation suffices). It should also test
(CL-2) for the linear package in SF's §33 pair, rather than in a newly invented 𝔐.

---

# Overclaims

1. **PROOF l.27-28, 6288-6290; RTARGET §49; LOG l.998-1001.** "Signed ratio 1.1-1.4 … three orders below 1267". These are
   periodised lower bounds. The defensible statement is R_3(ℤ⁴) ∈ [1.40, ≲ 60], ≥ 20 times below.
2. **PROOF l.6185-6186.** "No near/far split is needed". It is needed in CURV1_1's single gauge.
3. **PROOF l.6236-6237; LOG l.1009.** "(H-G) is not an independent hypothesis". True per fixed level. Its level-uniform form
   is not derived, and HG-ind compounds (r and θ).
4. **PROOF l.6250-6254.** NAH-unif′ "PROVEN as an implication": its proof uses one θ at every level, which HG-ind does not
   provide.
5. **PROOF l.6329.** COMP's "(BG-unif) (i)-(ii) hold": for the composite critical point only, without (CL-4).
6. **PROOF l.6332.** COMP-F1 "OCCURS": an inference.
7. **PROOF l.6352-6356.** (CL-cl): "shrinking", "c_iS_W", and "⊂ (BG-unif) (iv)".

# Tally

**72 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path) + 1 comparison
branch: as claimed, unchanged.**
- ENV, H-fac, LOC_1, TOWER-VAR: CONFIRMED.
- HG1, CURV1_1: CONFIRMED-WITH-FIX.
- HG-ind: CONFIRMED as a per-level implication (non-circular). Not level-uniform.
- NAH-unif′: GAP as written.
- COMP: GAP (CL-4).
- None is counted, and none should be. N5 stays OPEN.

# Required fixes (binding for the next session)

1. **S22-1 (c38 reading).** Replace every "signed ratio 1.1-1.4 … three orders below" with "R_3(ℤ⁴) ∈ [1.40, ≲ 60]
   (periodised lower bound / absolute-leg upper bound N3^abs = 73.2, 90.8, 111.1, 131.9 at T = 4, 5, 6, 8, extrapolated
   ≲ 170; REVIEW_S22 L), ≥ 20 times below 1267; the signed ℤ⁴ value is unmeasured". State in the c38 record that torus N3
   is a lower bound.
2. **S22-2 (c38 C reading).** C confirms the marginal (K → 0) direction only, as gauge invariance requires. It is silent on
   the lattice-scale part (soft 3.1-3.9 of N3). Record C2's coefficients (-2.3 to -3.2).
3. **S22-3 (HG1/CURV1_1).**
   - (a) Add the Ad(h) - 1 term (≤ 648ℓ_{θ'}p_L𝔠_∞ε²) to C_G.
   - (b) Withdraw "no near/far split". In CURV1_1, split near/far: far |e_{g,1}| ≤ 30κ_0p_L𝔠_∞ε, absorbed by
     c_K^{(1)}τ^{(1)}(D_g) in D_g's condition; add the box-nesting condition for the near part.
   - (c) Make m^{(1)} ≤ m explicit in LOC_1.
   - (d) Make CURV1_1's BCH threshold in r^{(1)} explicit.
4. **S22-4 (r-compounding).** In HG-ind and in BR1-at-level-i, bound |g_{i+1}| by HG1 (iii)'s curvature form, not by (iv).
   r^{(i+1)} := 2𝔠_∞^{(i+1)}κ_i(N_0(|𝒦_ρ^{(i)}|) + 1)ε. Record that the (iv)-based version compounds by ≥ 10³ per level.
5. **S22-5 (θ-cascade).** Record the new failure mode CURV-F2″ (first-order θ compounds as θ(16κ𝔠_∞)^{-k}, ℓ_θ^{(0)} ∝ k,
   ε_unif = O(1/k)). Restate NAH-unif′ with (H-C⁺) extended to the cascade, or with a non-recursive (H-G) hypothesis (from
   BFT-4). Reword "(H-G) derived" as "derived at each fixed level". Note that CURV-F2′ ≡ CURV-F2 (C_G is a localised
   D³E^br), and that "C_θ^{(i)} ≥ Π" refers to the route's bound.
6. **S22-6 (COMP).** Add (CL-4) (or Balaban's convention, with the per-level recursion re-derived). Add to (CL-0) that
   𝔊_k maps into S_k and 𝔊_kHess = 1 on S_k.
7. **S22-7 (COMP-F1).** "occurs [inference]". Cite SF §6.2 / REVIEW_HIST_S4 S4-1 (sup-norm (a5-G) FALSE) as independent
   corroboration. Name SF's §33 pair as the candidate 𝔐.
8. **S22-8 (CL-cl).** Restate it as BFT-4: E_k^br = S_W + R_k, sup_k||R_k||_𝒜 < ∞, the marginal coefficient fixed. Write
   "⇒ (BG-unif) (iv)", not "⊂". Present it as a clause of BFT, which is the target.
9. **S22-9 (BFT).** Adopt BFT (Part 5) as the single named target. Re-point (BG-unif), (H-C⁺), (H-ℂ), (CL-cl) and
   COMP's (CL) to its clauses.
10. **Cosmetic.** Unify ι vs ι^{(1)} (l.6176, 6184). Reconcile U0 (iv)'s 6ε with CURV1's 7.2ε.

## FOR OTHER FILES (for their owners; not edited)

- SF.md l.252: "margin ≈ 10 … K_p^♯ = 0.062, 0.103" is stale (S21-2). The chain should cite NAH-unif′'s GAP (S22-5) and
  BFT.
- RLARGE row 3a: as LOG session 22 item 1, plus re-point (BG)_k to BFT-3 / BFT-1.
- FLOW (SF-bg), SQ (REG-min), SF (a5-G♯)/(a5-U)/(MIN-reg): add a cross-reference to BFT (Part 5) and the clause each one
  uses. SQ should note that (REG-min) is the cone-local sibling of BFT-1, not a corollary.
