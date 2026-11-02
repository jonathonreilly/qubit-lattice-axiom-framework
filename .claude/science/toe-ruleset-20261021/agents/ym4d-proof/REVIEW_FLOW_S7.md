# REVIEW_FLOW_S7: hostile review of lane C session 7 (FLOW.md §50-§56 and the [RFL6-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f10*. This file is the only one I edited.
No commits, PRs or pushes.

Inputs (read-only, by offset):
- REVIEW_FLOW_S6.md (all).
- FLOW.md:
  - l.236-250 (step functional);
  - l.753-862 (§18 with the RFL6 sites);
  - l.1108-1124 (the 𝔊 definition);
  - l.1270-1284;
  - §43-§49 (l.2134-2507), including all 19 [RFL6-fix] sites;
  - §50-§56 (l.2510-2779) in full.
- FLOW_LOG.md l.252-298 (session 7).
- PROOF.md l.2444-2470 (Lemma FP-ab and its application) and l.3031-3085 (NA-crit, NA-inv, Proposition NA-FP, composite
  slice).
- checks: f10_criteria.md (all), f10_fp_vheat.py (Part A in full, Part V structure), f10_out.txt, f10_time.txt.
  - BSD stat (UTC): f10_criteria.md born 06:04:51 (4010 B); f10_fp_vheat.py born 06:07:27 (15456 B, md5 aed08c71…, matches
    FLOW_LOG); f10_out.txt born 06:08:39, last modified 06:08:43; f10_time.txt born 06:08:43.

Numerics:
- **One NUMERIC LOCK acquisition, 06:17:45-06:21:13 UTC, released once with `rmdir` (no trap).**
- Conditions at start: load 2.11, memory free 39%. nice 10, all BLAS threads = 1, PYTHONDONTWRITEBYTECODE=1, plain
  `python3` (no -I), no `timeout`.
- Output is in
  `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow7/`.
- **(R1) f10 re-run.** It ran from a scratchpad copy. The only change was HERE pointed at checks/, as in the author's
  smoke test. The output is **identical to checks/f10_out.txt** apart from the timestamp and timing lines. 19/19 PASS, all
  four controls fail as required. 4.42 s, peak RSS 165 MB.
- **(R2) independent V-heat check (`indep_vheat.py`, my own code).**
  - It imports nothing from f9 or f10, and uses neither FLOW's formula operator nor its symbols.
  - The SU(N) root-sector Wilson Hessian is built from scratch. In the left chart, each plaquette's exact second derivative
    is taken of −Re tr(e^{Y_1}e^{Y_2}e^{Y_3}e^{Y_4}U_p^0), with the Y_k the exactly transported generators.
  - D_Uλ = Ad(U_b)λ(y) − λ(x) and K = H + DD^T, on an open 2D box in Landau gauge.
  - It computes the diagonal heat kernel at the centre with expm_multiply, takes the φ² coefficient by 3-point Richardson,
    and forms R = Θ_2/(t²j_0²).
  - 166 s, peak RSS 540 MB.
- No process was left running, and checks/ has no `__pycache__`.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **[RFL6-fix] S6-1..S6-5: all applied (19 tags, as claimed). Minor leftovers only** (§1).
- **S6-6 was NOT done**, as FLOW says (l.2747-2748, l.2776). S6-6 asked for two things:
  - (R1) and (R2) stated in FLOW on the root-sector maps T_k(B);
  - (V-IR) restated as an operator-level statement on G_⊥: a bound on the f² coefficient of
    ½log det_{ker D_0^*}(H + M^TΠM) + ½log det_⊥(P_⊥𝒞_nP_⊥) against ½log det_{ker D_0^*}(K_F) with a proper-time cutoff at
    t ≈ ℓ², with an n-independent error.
  - It carries over as binding fix S7-2.
- **Lemma FP-exact: CONFIRMED.** Every step checks, including the 2π bookkeeping (d_0 − m_2 − dim S_0 = 0).
  - **The Δ_FP(U_0) of Reading (1) is the correct Faddeev-Popov factor, not an ansatz.** |det χΓ| is the standard FP
    determinant, i.e. the Jacobian of the gauge condition along the orbit, in the Lebesgue-δ convention. det(hh^*)^{-1/2} is
    forced by writing δ(hA)dA as the induced measure on H_0.
  - The target is the Haar quotient ∫_E I/vol(G_res), which is what the tower integrates, and vol(G_res) does not depend
    on U_0.
  - **There is one trap the text does not flag (fix S7-1).** NA-FP's FP_U normalises to ∫_{S_0}I, not to the Haar quotient.
    Reading Δ_FP := FP_U^{-1} would leave a stray U_0-dependent ½log det Δ', which is exactly the size of β[G_gh].
  - **No step uses det(hh^*) background independence.** det(hh^*) sits inside Δ_FP by definition. The post-hoc note is
    correct for d = 2, and for d ≥ 3 its "can depend" is right (§3.3).
- **Theorem V-heat: CONFIRMED.** I re-derived Steps 2-5 and found no error. My independent Wilson-Hessian computation
  matches the closed form to ≤ 1.3e-10 relative for t ∈ [2, 100], for three roots:
  - SU(2), γ = 1/8;
  - SU(3) root (1, 2) of i√(3/2)diag(1, 0, −1), γ = 1/4;
  - SU(3) root (1, 3) of i diag(1, 1, −2)/√2, γ = 5/36.
  - **This includes the SU(N ≥ 3) Wilson structure (i), which f10 did not test.**
  - At t = 100: direct 3.66332704; t(R − 11/3) = −0.33396 → −1/3.
- **R_12 is NOT by itself the transverse coefficient.**
  - R_12 = R_V^{4D} − 2R_S → 11/3 is the BF-Feynman total.
  - The 21/22 needs R_12 + R_S = R_V − R_S → 7/2 (Landau transverse).
  - With the ghost's exact 1/6 (GH-log), the total is 7/2 + 1/6 = 11/3, i.e. β_0^std. FLOW uses this correctly (l.2397-2402,
    l.2548).
- **Lemma F-id-exp: CONFIRMED**, with one wording fix to Step (1) (S7-4).
- **f10: CONFIRMED.** The criteria predate the script, the script predates the run, and the re-run is identical.
  - Part A tests the algebra with a synthetic invariant Q = P_{S_0}BP_{S_0}, not the tower Hessian, and only in 2D at n = 1.
    So it is a consistency check, not evidence for the d = 4 composite case.
- **Corrected tally: 40 PROVEN-HERE (claimed 40)**, with the scope annotations of §8.
- **Minimal remaining list for UNIV (SU(N)) (§6):**
  - (V-IR) on G_⊥, the crux;
  - (L-loc2), proved rather than ARGUED;
  - either G-mag (vi), or (V-IR) and the β bookkeeping stated for limit points.
  - Everything else listed in §55 is either route-internal to a proof of (V-IR) ((R1)-(R3), (a2), (a4'), (b), and the
    level-n ⊥ IR safety) or needed only for the rate ((s1), (s2⊥), and (vi) for exactness).

---

## 1. Priority 1: the [RFL6-fix] edits and S6-6

19 in-text tags (l.786, 833, 847, 1278, 2145, 2192, 2259, 2263, 2269, 2283, 2313, 2334, 2370, 2397, 2414, 2466, 2468,
2477, 2502). This matches the claim (l.2512, l.2747).

| Fix | Where | Verdict |
|---|---|---|
| S6-1, GH (iii) parenthetical | l.2145-2149 | APPLIED. The wording is as asked, and it points to §52. |
| S6-1, old (a3) retired | l.786-789, l.1278-1279, l.2414-2417 | APPLIED. |
| S6-1, scope notes on 1/22 and 21/22 | l.2263-2265, l.2397, l.2468, l.2477-2479, l.2502-2507 | APPLIED. They are now discharged by §52, given S7-1. |
| S6-2, (L-loc) → (L-loc2) | l.2334-2342 | APPLIED. The second-derivative resolvent formula is correct, sign included. |
| S6-2, COV-GI-∞ cites (L-loc2) | l.2370-2371 | APPLIED as an overlay. **Leftover:** the bold line l.2379-2380, "unconditional at each fixed n, given (L-loc)", still reads (L-loc) in place. Edit it to (L-loc2). |
| S6-3 | l.2313-2314 → §51 | APPLIED. |
| S6-4, J_n^⊥ binding definition | l.847-855 | APPLIED. G_gh is outside J. The bracket ½log det O^♯_n − ½log det'Δ_0 is one unit. B_n = −β[G_⊥] − β[G_gh] exactly. Correct. |
| S6-4, old UNIV proof marked superseded | l.833-834 | APPLIED. |
| S6-4, "G_⊥ IR safe because total C²" | l.2283-2290, l.2466-2468 | APPLIED. The Schur-complement argument is stated correctly. |
| S6-5, per-root B-flux | l.2192-2196 | APPLIED. |
| S6-5, "(b) suffices for UNIV" | l.2259-2262 | APPLIED. See S7-3 for the limit-point consequence. |
| S6-5, Landau 1/22 vs Feynman 1/11 | l.2269-2281 | APPLIED, faithfully. |
| **S6-6** | — | **NOT DONE** (honestly declared at l.2747-2748 and l.2776). Content as in the Bottom line. → **S7-2.** |

Further minor leftovers:
- **§48 l.2480-2484** ("Theorem UNIV now: conditional on … (a3), (b), and on (V-heat)") is not tagged. It is now superseded
  by §55 (l.2760-2763). Add a pointer.
- **§52 cites "l.1100-1103"** for the tower's 𝔊 and Δ_FP (l.2621, l.2627). After the RFL edits these lines are
  **l.1114-1117**. Fix the references.

## 2. Priority 2: Lemma FP-exact (§50 (P2), §52)

### 2.1 Line by line

- **(1) Invariance (l.2602-2604): CONFIRMED.**
  - Q = H + M^T𝒞^{-1}M is the Hessian of 𝒯_0 + Ψ(·; 𝔪(U_0)) at U_0. That is exact Gauss-Newton, since Ψ's residual vanishes
    at V = 𝔪(U_0).
  - HD_0ρ = 0 (NA-inv) and MD_0ρ = D ev ρ = 0 for ρ ∈ Λ'. Symmetry then gives I(A + Γρ) = I(A).
  - Γ^TΓ = E'Δ_0E' = Δ'. (ΓΛ')^⊥ = S_0 by S-all.
- **(2) Admissibility (l.2605-2606): CONFIRMED**, given NA-FP (ii) for the composite slice (PROOF l.3078-3083, upstream).
  - The composite onto-ness of M^{(n)} is upstream and was not re-reviewed here.
- **(3) FP-ab (l.2607-2608): CONFIRMED** (PROOF l.2444-2452 verbatim, with Γ = D_0|_{Λ'} and m_1 + m_2 = dim Λ').
- **(4) Coarea (l.2609-2613): CONFIRMED.**
  - The map y ↦ h^*y has Gram matrix hh^*, so dA = det(hh^*)^{1/2}dσ dy.
  - ∫δ(hh^*y)dy = det(hh^*)^{-1}.
  - |P_resD_0^*A|² = ⟨A, D_0P_resD_0^*A⟩, so the exponent on H_0 is ΠOΠ.
  - Positivity: FP-ab is an equality in [0, ∞] (Tonelli), so finiteness of the right side excludes a nonpositive direction
    of ΠOΠ|_{H_0}. ✓
- **(5) Logarithms (l.2614-2616): CONFIRMED.** I redid the bookkeeping:
  - −log LHS = ½log det(ΠOΠ) + ½log det(hh^*) − (d_0/2)log 2π;
  - −log RHS = −(m_2/2)log 2π + log|det χΓ| − ½log det Δ' − (dim S_0/2)log 2π + ½log det_{S_0}Q;
  - d_0 − m_2 − dim S_0 = (dim E − m_1) − m_2 − (dim E − dim Λ') = 0. ✓
- **(6) Factorisation (l.2617-2619): CONFIRMED.**
  - With columns (Λ' ⊖ Λ_res, Λ_res) and rows (su(N)^{N_c}, Λ_res), the matrix is [[M|_⊖, 0], [P_resΔ'|_⊖, P_resΔ'P_res]].
  - It is block lower triangular, and dim(Λ' ⊖ Λ_res) = m_1 because M is onto.
  - Only |det| is basis independent, as used.
- **(7) (a3) ≡ 0 (l.2620-2626): CONFIRMED.**
  - The magnetic-translation/Bloch remark is correct but redundant. The identity holds exactly on every finite torus where
    (N) holds, so it holds between per-site densities.
  - Commuting with magnetic translations holds for the ℓZ⁴ sublattice only (h, M, P_res, Δ' are block structured). That is
    all that is needed.

### 2.2 Is Reading (1)'s Δ_FP the correct FP determinant for the tower's fixing, or an ansatz?

**It is the correct one, and it is forced.**
- The tower's step integrand at fixed coarse V is G_res-invariant: G_res = {g : g(c_X) = 1} at the level-n centres.
  Gauge transformations that move the centres change V, so G_res is the exact symmetry group.
- The physical object is ∫dU F(U)/vol(G_res) with Haar measure. vol(G_res) is U_0-independent, and at the Gaussian level
  Haar measure near 1 is dλ on Λ' with unit Jacobian.
- The FP trick, 1 = Δ(U)∫dg δ(χ_1(g·U))e^{−½|χ_2(g·U)|²}(2π)^{−m_2/2}, has Δ(U) = |det χΓ| in the Lebesgue-δ convention
  (FP-ab's substitution μ = χΓλ).
- So −log[∫_E I/∫_{Λ'}dλ] = ½log det(ΠOΠ|_{H_0}) + ½log det(hh^*) − log|det χΓ| + (U_0-independent).
- That is (P2) with Δ_FP = |det χΓ|·det(hh^*)^{-1/2}. The second factor is the measure conversion δ(hA)dA = det(hh^*)^{-1/2}dσ.
  It is not a choice.
- The Haar quotient equals the δ-slice S_0 form of Lemma GH, ½log det_{S_0}Q − ½log det Δ', which is what Lemma GH and
  GH-log use.

**The trap (binding fix S7-1).**
- PROOF's NA-FP (iii) states ∫Iδ(h)e^{…} = FP_U·∫_{S_0}I with FP_U = (2π)^{m_2/2}|det χΓ|^{-1}det(Γ^TΓ)^{1/2}. This normalises
  to the S_0 slice measure, not to the Haar quotient.
- If Γ^{W0}_n were defined as −log∫_{S_0}I, i.e. with Δ_FP := FP_U^{-1}·(2π)^{…}, it would differ from the S_0 form by
  +½log det Δ'. That term is U_0-dependent, and its f² coefficient per complex root is ≈ +2c_gq_α²log ℓ. It would cancel
  β[G_gh] (REVIEW_FLOW_S6 §3.1).
- Reading (1) (l.2627-2630) names FP_U but does not say that **Δ_FP ≠ FP_U^{-1}**: they differ by the U_0-dependent factor
  det(Γ^TΓ)^{1/2} = det(Δ')^{1/2}. The correct target is the Haar quotient ∫_E/vol(G_res).
- Add one sentence saying this, and annotate FLOW l.244 and l.1114-1117 with "Δ_FP := |det χΓ|·det(hh^*)^{-1/2} (§52);
  NOT FP_U^{-1}".
- This is a statement fix. It does not change the lemma, the proof, or any number.

### 2.3 The post-hoc det(hh^*) note (l.2631-2638)

- **It is labelled correctly and logged (FLOW_LOG 06:09). No statement or proof step changed.**
- **No step of §52 needs det(hh^*) to be background independent.** The factor is part of Δ_FP, so it cancels identically
  in (5).
- It would matter only for a computation that used |det χΓ| alone with the H_0-induced Gaussian. S7-1 excludes that.
- **d = 2 claim: CONFIRMED.**
  - In a block, a 1-link is reached by order (1, 2) only on the centre row, where order (2, 1) with Δ_2 = 0 takes the same
    route. Likewise for 2-links.
  - So every coefficient of h on a link is (count)·Ad(T) for a single transport T.
  - Since blocks are disjoint, hh^* is block diagonal with entries Σ_b n_b²·1, which does not depend on f.
  - f10 A5 agrees: −27.073393 at f and at 0.
- **d ≥ 3 claim ("can depend"): CORRECT.**
  - A μ-link with μ ≥ 3 is reached by the orders (1, 2, 3, …) and (2, 1, 3, …) through routes whose transports differ by a
    plane-12 rectangle holonomy, e^{iq_αfA}.
  - The coefficient is then a sum of distinct orthogonal matrices, and hh^* acquires f-dependent cross terms.
  - It is irrelevant to FP-exact.

### 2.4 Verdict

**Lemma FP-exact: CONFIRMED (PROVEN-HERE)**, given NA-FP (ii) composite (upstream) and (N).
- Its Reading (2), "the 1/22 and 21/22 hold for the tower's own fixing", is correct once S7-1 is written.
- f10 Part A is consistent, but it tests only the linear algebra: a synthetic Q, U(1), d = 2, n = 1.

## 3. Priority 3: Theorem V-heat (§50 (P3), §53)

### 3.1 Re-derivation (Steps 1-5)

- **Step 1 (structure).**
  - The BCH reduction is correct. tr(RU_p^0) = 0. R² gives −ν|r|²(e^{ia} + e^{ib}), hence cos a + cos b. ½Σ[Y_i, Y_j] is
    Cartan-valued, and Re tr(iν'Im(…)(e_ii − e_jj)U_p^0) gives (sin a − sin b).
  - The operator form, c := [1 − εv, u − ε], and cD_0 = (1 − ε)·1 all check.
  - The criticality condition reduces to S_α/(2i) = −iC_αtan(φ/2), and the identity
    (sin a − sin b)/(cos a + cos b) = tan((a − b)/2) gives S_α = 2C_αtan(φ/2).
  - Fixing 2S̃ = 1 *by* criticality is a consistency determination rather than a direct BCH computation of ν'. That is
    legitimate, because U_f is independently critical. **My (R2) confirms the resulting operator directly for SU(2) and
    two SU(3) roots** (|H D λ| = 2e-15 in the interior; the calibration H(0) = c^Tc holds to 4.4e-16).
  - C_α = 1 − γ_αφ² + O(φ⁴), with γ_α = (h_i² + h_j²)/(4q_α²). ✓
- **Step 2 (symbols).**
  - The Weyl product rule, ⋆ to second order (matrix order kept), and τ tr Op(a) = ∫tr a all check.
  - tr σ_1² = sin²k_1 + sin²k_2 + 2(1 + cos k_1)(1 + cos k_2), since |σ_{1,12}|² = ¼|1 + z_1|²|1 + z_2|². σ_1 is Hermitian, and
    σ_1(0) has eigenvalues ±2.
  - tr σ_2 = −2γ_α(2 − cos k_1 − cos k_2). ✓
- **Step 3 (hierarchy).**
  - At order φ²: −ωE^{(2)} − σ_1E^{(1)} − σ_2E^{(0)} + (i/2)({ω, E^{(1)}} + {σ_1, E^{(0)}}) + (1/8)P²(ω, E^{(0)}).
  - {ω, E^{(1)}} = −{σ_1, e^{−tω}}, because the t² parts cancel against ω_1ω_2 symmetry. ✓
  - P²(ω, e^{−tω}) = [t²(ω_{11}ω_2² + ω_{22}ω_1²) − 2tω_{11}ω_{22}]e^{−tω}, using ω_{12} = 0. ✓
  - Integrating: E^{(2)} = e^{−tω}[(t²/2)σ_1² − tσ_2 + (1/8)((t³/3)(…) − t²ω_{11}ω_{22})]. ✓
  - The Banach-algebra justification (weighted ℓ¹, unimodular twist, finite-support σ) suffices.
  - Calibration against G-mag (iii): (1/8)[(8/3)t²j_1² − 4t²j_1²] = −(t²/6)j_1². ✓
- **Step 4.** Using ∫e^{−t(2−2cos k)}sin²k = j_1/(2t):
  - ½·t²·[2(j_0 + j_1)² + j_0j_1/t] = t²(j_0 + j_1)² + (t/2)j_0j_1;
  - −t·∫tr σ_2 = 4γ_αtj_0(j_0 − j_1);
  - orbital −(t²/3)j_1².
  - So Θ_2 matches (ii). SU(2): γ = 1/8 gives (t/2)j_0², hence + 1/(2t). ✓
- **Step 5.** ρ = 1 − 1/(4t) + O(t^{-2}) (from I_1/I_0(z) = 1 − 1/(2z) − …, z = 2t):
  - (1 + ρ)² = 4 − 1/t;
  - ρ²/3 = 1/3 − 1/(6t);
  - ρ/(2t) = 1/(2t);
  - the γ term is O(t^{-2}).
  - Sum: 11/3 + (−1 + 1/6 + 1/2)/t = 11/3 − 1/(3t), independent of γ. ✓
- **Independent continuum check of the limit.**
  - The complex plane-12 vector in Feynman gauge has heat density (4πt)^{-1}(Bt/sinh Bt)·2cosh(2Bt) = (4πt)^{-1}[2 + (4 − 1/3)B²t² + …].
  - With t²j_0² → t/(4π), this gives R_12(∞) = 11/3. ✓

### 3.2 Independent numerics (R2), under the lock

| case | t | R_12 direct (my Wilson builder) | closed form | rel. dev. | t(R − 11/3) |
|---|---|---|---|---|---|
| SU(2), γ = 1/8 | 2 | 3.47415942 | 3.47415942 | 1.3e-10 | −0.38501 |
| | 8 | 3.62393217 | 3.62393217 | 7.5e-11 | −0.34188 |
| | 24 | 3.65266615 | 3.65266615 | 4.6e-11 | −0.33601 |
| | 50 | 3.65997466 | 3.65997466 | 4.1e-11 | −0.33460 |
| | **100** | **3.66332704** | 3.66332704 | 2.8e-11 | **−0.33396** |
| SU(3) (1,2), γ = 1/4 | 2 / 6 / 16 / 24 | 3.50827877 / 3.61270046 / 3.64607067 / 3.65288432 | equal | ≤ 1.3e-10 | → −0.3308 |
| SU(3) (1,3), γ = 5/36 | 2 / 6 / 16 / 24 | 3.47795046 / 3.60954353 / 3.64563314 / 3.65269039 | equal | ≤ 9.1e-11 | → −0.3354 |

- The box size was chosen so that e^{−(B/2)²/(4t)} ≤ e^{−36}. The free normalisation was 1.000000000000 in every case.
- f10 V2's 1.9e-7 at t = 24 is its box edge (B = 101). At B = 123 I get 4.6e-11.
- **Large-t limit:** the direct values at t = 50, 100 sit on 11/3 − 1/(3t) + O(t^{-2}) (−0.33396 at t = 100, which is the
  closed form's own value). With the continuum check above, the limit 11/3 is confirmed independently.
- **γ = 5/36 is a value FLOW never tested**, and it agrees with the closed form.

### 3.3 Does R_12 give the 21/22, and with the ghost the universal β_0?

- **R_12 itself is the BF-Feynman total.** R_12 = R_V^{4D} − 2R_S → 11/3.
- The 4D reduction R_V^{4D} = R_12 + 2R_S needs components 3 and 4 to be decoupled scalars. I checked the argument of
  l.2398-2402 myself:
  - in the Landau gauge θ_1 = θ_3 = θ_4 = 0, the 13, 14, 34 plaquettes are exactly free;
  - the 23 and 24 plaquettes have U_p^0 = 1, hence no spin term, and covariant ∇_2 commutes with flat ∇_3, ∇_4;
  - so the Feynman cross terms cancel exactly against DD^*. ✓
- **The transverse share needs R_12 + R_S = R_V^{4D} − R_S → 7/2 = (21/22)(11/3).** That is the fine piece of G_⊥ in Feynman
  form: ½log det O^♯ (plane-12 block plus two scalars) − ½log det'Δ_0 (once complex per root).
- The ghost's exact share 1/6 (GH-log, from exact scaling, no t-integral) adds to 7/2 + 1/6 = 11/3 = R_12(∞).
  - Summed over roots with Σq_α² = N², and with t²j_0⁴ → 1/(16π²) (lattice corrections O(1/t), integrable), this gives β_0^std.
  - The signs are consistent: β[G_⊥] = −(21/22)β_0 log ℓ and β[G_gh] = −(1/22)β_0 log ℓ, both antiscreening.
- **Caveat (correctly stated at l.2715-2718):** V-heat is about K_F = H + D_0D_0^* without the IR term M^TΠM and without the
  level-n group. Converting ∫(R_12 + R_S)dt/t into exactly (7/2)·2log ℓ + O(1), uniformly in n, is (V-IR).

### 3.4 Verdict

**Theorem V-heat: CONFIRMED (PROVEN-HERE)** for every root of SU(N), including the Wilson structure (i) for N ≥ 3. That
structure is now checked numerically by (R2), for γ = 1/4 and γ = 5/36.
- Pre-statement provenance: FLOW_LOG 05:56 discloses that the SU(2) closed form was found in scratch reasoning and compared
  to f9_out at t = 2 *before* §50. This is honest. It means (P3) is not a blind prediction, but the proof and two
  independent numerics make that immaterial.

## 4. Priority 4: Lemma F-id-exp (§50 (P1), §51)

- **(1) (l.2568-2574): CONFIRMED, with a wording fix (S7-4).**
  - NA-inv at the critical point 1 gives Σ_bh(b, b')(dλ)_b = 0, which licenses the polynomial A'.
  - The truncation step says dλ − dλ_R "is O(R^k) there". That is false as written: far links carry |dλ| ~ (1 + |b|)^k, not R^k.
  - The conclusion holds by the correct bound: Σ_{|b|≥R−1}|h(b, b')|C(1 + |b|)^k(1 + |b'|)^{k'} ≤ C_εe^{−(m−ε)(R−1)}Σ|h|e^{m(|b|+|b'|)} → 0.
  - Replace the sentence with this.
- **(2) Cone homotopy (l.2575-2581): CONFIRMED.**
  - Both axial paths agree through directions 1..μ−1. They then run along μ to x_μ and to x_μ + 1, i.e. they agree up to a
    and a + e_μ.
  - They then run in parallel in μ+1..4, so the loop is the (μ, ν) ladder with |Σ(b)| ≤ |x|_1, and the distances are as stated.
  - A = K̃dA + dλ_A holds for every A.
- **(3) (l.2582-2584): CONFIRMED.** The e^{4m'} prefactor and the linear-factor absorption hold for m' < m.
- **(4) (l.2585-2591): CONFIRMED.**
  - K̃ is the origin cone, not translation covariant. But Σ_xτ_xh_0τ_x^{-1} correctly represents ⟨A, ΠA⟩, since each translate
    is written with its own translated cone.
  - Σ_z|Π_0(z)|e^{m'|z|} is bounded by the weighted sum.
  - ĥ(0)_{12,12} = Σ_{p∈12, p'∈12}h_0(p, p'), the p² extraction, and H_0(𝓛Φ, 𝓛Φ) = h_0(Φ, Φ) = cφ² all check.
- **The MS (iv) hypothesis paragraph (l.2592-2596): CONFIRMED given (L-loc2).**
  - The resolvent second-derivative kernels are O((c + s)^{-2}) and O((c + s)^{-3}), integrable in s.
  - **Add:** differentiating ρ_0(exp(fH_1a^sym)) twice under an infinite link sum needs the second-derivative bounds
    *uniformly on a neighbourhood* (U_f ∈ 𝒦_n), not only at U = 1. (L-loc2) supplies this on 𝒦_n, and Lemma MS (iii)'s
    dominated convergence does the rest. One clause.
- **Verdict: CONFIRMED (PROVEN-HERE). S7-F3 does not occur.**

## 5. Priority 6: f10 provenance and re-run

- **Order of events:**
  - §50 at 06:00:12, with the stat logged; the md5 cannot be re-verified now, because FLOW.md has changed since;
  - proofs §51-§53 at 06:00-06:04;
  - criteria at 06:04:51;
  - script at 06:07:27;
  - smoke run at 06:08:17 under the lock;
  - official run at 06:08:39-43;
  - post-hoc note at 06:09, labelled.
  - BSD stat agrees with FLOW_LOG for all four f10 files.
- **Criteria before script: YES.**
- **Re-run: identical** apart from the timing lines; 19/19; all four controls fail.
- **Evidential weight:**
  - A2 and A3 are near-tautological consequences of FP-ab for any invariant Q. A-ctl usefully shows that Δ_FP(1) is off by
    0.19-0.35.
  - V1 ties the formula to f9's SU(2) Hessian.
  - V2 and V3 use the formula operator, so they are not independent of Step 1. (R2) removes that dependence.
- **Not tested by f10:** d = 4 and the composite slice in Part A; the SU(N ≥ 3) Wilson structure (now covered by R2); (V-IR).

## 6. Priority 5: what remains for UNIV (SU(N)): the minimal list

Theorem UNIV is the O(1) statement |Σ_{k<n}b_k − β_0^std n log L| ≤ R_0. After session 7, with B_n = −β[G_⊥,n] − β[G_gh,n]
(l.847-855, exact), the minimal list of open inputs is:

1. **(V-IR) on G_⊥ (crux, [s-P]).**
   - Statement: c^⊥_{n,α} = −(q_α²/(16π²))∫_1^{ℓ²}(R_12^lat + R_S^lat)dt/t + O(1), uniformly in n, per root.
   - Equivalently, with V-heat: β^fine[G_⊥,n] = −(21/22)β_0^std log ℓ + O(1).
   - Its operator-level form is S6-6/S7-2, still unwritten.
2. **(L-loc2) ([s], ARGUED).** It is needed for COV-GI-∞ (the C² total density, hence the β link via MS (iv) and F-id-exp)
   and, through (L-loc), for N-f. Proving it is routine but is not done.
3. **G-mag (vi), or a limit-point formulation ([s], ARGUED).**
   - S6-5's remark is right that GH-log (b) bounds every limit point of G_gh's coefficient.
   - But without (vi), β[G_gh,n] need not exist as a number. Then β[G_⊥,n] := total − β[G_gh,n] does not exist either, and
     (V-IR) as written is ill-posed.
   - Either prove (vi), or state (V-IR) for the total root-sector f² coefficient (which exists by COV-GI-∞) minus the
     G_gh limit points (fix S7-3).

**Not separately needed for UNIV** (route-internal, or for the rate only):
- (R1), (R2), (R3) on G_⊥, (U-IR)(a2) and (a4') in transverse form, and (U-IR)(b). These are the means of the old
  J_n/U-res route to (V-IR). If (V-IR) is proved directly (e.g. by a proper-time/Duhamel comparison), they are not
  additional hypotheses. FLOW §55 lists (b) as a separate condition; it is one only on the U-res route.
- The IR safety of the root-sector level-n ⊥ group. The total G_⊥ is defined and C² at each n (COV-GI-∞ minus G_gh), so its
  group-wise IR safety is needed only on a proof route that splits G_⊥ into the fine term and the level-n group.
- (s1), (s2⊥), and (vi)'s exactness: for UNIV-rate only.
- (COV-GI) at non-critical backgrounds: β uses critical U_f only.
- FI-1 and HIST's CL^J: cross-lane, for F-flow and beyond, not for UNIV.
- Already discharged: (a3) (FP-exact, given S7-1), (V-heat), the Cartan sector (COV-⊥-C, O(1)), and (U-loc) (§23).

## 7. Per-item verdicts

| Item | Verdict | Fix |
|---|---|---|
| [RFL6-fix] S6-1..S6-5 (19 tags) | **APPLIED** | minor leftovers: l.2380 (L-loc → L-loc2 in place); §48 l.2480 pointer to §55; stale "l.1100-1103" at l.2621, l.2627 → l.1114-1117 |
| S6-6 | **NOT DONE** (declared) | S7-2 |
| (P1) Lemma F-id-exp | **CONFIRMED** | S7-4 (Step (1) truncation bound; uniformity clause) |
| (P2) Lemma FP-exact | **CONFIRMED**; Δ_FP is the correct FP factor (forced, not an ansatz); det(hh^*) independence not used | S7-1 (Δ_FP ≠ FP_U^{-1}; Haar target) |
| Post-hoc det(hh^*) note | **CORRECT** (d = 2 proven above; d ≥ 3 "can depend" right) and correctly labelled | — |
| (P3) Theorem V-heat (i)-(iii) | **CONFIRMED** (re-derived; R2 independent to ≤ 1.3e-10, three roots incl. SU(3) Wilson) | — |
| §46 4D reduction R_V = R_12 + 2R_S | **CONFIRMED** (exact: free 13, 14, 34 plaquettes; flat 23, 24 holonomy) | — |
| "R_12 gives 21/22" | Precisely: R_12 + R_S → 7/2 = 21/22·(11/3); R_12 → 11/3 is the total. FLOW consistent. | — |
| f10 (re-run identical) | **CONFIRMED**; Part A is algebra-only | — |
| §55 UNIV condition list | Over-inclusive (route-internal items listed as hypotheses); misses the (vi)/limit-point well-posedness | S7-3, S7-5 |
| S7-4 target (V-IR model) | NOT ATTEMPTED; the reason (2D has power, not log, proper-time structure) is correct | — |

**Corrected tally: 40 PROVEN-HERE (claimed 40)** = 37 + F-id-exp + FP-exact + V-heat. Scope annotations:
- **FP-exact:** given NA-FP (ii) composite (upstream) and (N); its use requires S7-1's reading of Δ_FP.
- **V-heat:** (iii)'s 4D statement uses §46's exact 3/4 decoupling (confirmed here).
- **F-id-exp:** its MS (iv) application is given (L-loc2).
- **Unchanged from S6:** N-f given (L-loc); COV-GI-∞ given (L-loc2) and (vi); GH-log (c), (d) given (vi).
- **ARGUED, not counted:** G-mag (vi); (L-loc2).
- **RETIRED:** (U-IR)(a3) as a bound against BF-Feynman J_*.
- **GAP:** UNIV-rate. **IMPORTED-AND-REVERIFIED:** L4b. **OPEN:** as in §6.

## 8. Binding fixes for the next lane-C session

1. **S7-1 (Δ_FP normalisation).** In §52 Reading (1), add: "Δ_FP(U_0) := |det χΓ|·det(hh^*)^{-1/2} is NOT FP_U^{-1} of NA-FP
   (iii): FP_U normalises to ∫_{S_0}I and differs by det(Γ^TΓ)^{1/2} = det(Δ')^{1/2}, a U_0-dependent factor of the size of
   β[G_gh]. The tower's object is the Haar quotient ∫_E I/vol(G_res) (vol U_0-independent), which is what (P2) reproduces."
   Annotate l.244 and l.1114-1117 accordingly. Fix the stale "l.1100-1103" (l.2621, l.2627).
2. **S7-2 (= S6-6, carried over).**
   - Write (R1) and (R2) on the root-sector maps T_k(B).
   - Write (V-IR) operator-level: for each root α and n,
     |[f²](½log det_{ker D_0^*}(H + M^TΠM) + ½log det_⊥(P_⊥𝒞_nP_⊥)) − [f²](½log det_{ker D_0^*}K_F)|_{t-cut at ℓ²}| ≤ A,
     with A n-independent and the cutoff made explicit (e.g. as a Duhamel comparison with e^{−tK_F} for t ≤ ℓ²).
3. **S7-3 ((vi) well-posedness).** Either keep G-mag (vi) in UNIV's hypotheses, or restate (V-IR) and S6-5's remark for the
   total root-sector f² coefficient minus the limit points of G_gh's coefficient. Then edit §55 (l.2760-2763) to say which.
4. **S7-4 (F-id-exp wording).**
   - In §51 (1), replace "O(R^k) there" with the bound
     Σ_{|b|≥R−1}|h|(1 + |b|)^k(1 + |b'|)^{k'} ≤ C_εe^{−(m−ε)(R−1)}Σ|h|e^{m(|b|+|b'|)}.
   - In the MS (iv) paragraph, add that the bounds are used uniformly on 𝒦_n (U_f), not only at U = 1.
5. **S7-5 (UNIV condition list).**
   - Rewrite §55's UNIV line as the minimal list: (V-IR); (L-loc2); (vi) or the S7-3 form.
   - Move (R1)-(R3), (a2), (a4'), (b) and the level-n ⊥ IR safety under "means of proof of (V-IR)".
   - Keep (s1), (s2⊥) under UNIV-rate.
   - Edit l.2379-2380 in place to (L-loc2), and add a pointer at §48 l.2480 to §55.

## 9. Next target

1. **S7-2's operator-level (V-IR) statement, then (V-IR) itself in its simplest true instance: a 4D charged scalar at n = 1
   with the real S4' root-sector averaging and IR term.** The scalar heat trace is exact (G-mag (iii)), so this isolates the
   IR-term/level-n mechanism.
   - Concretely: at rational flux with ℓ = 3, use the 4D magnetic Bloch decomposition over ℓZ⁴ (fibre dimension 81·flux
     denominator).
   - Pre-state the f² coefficient of the scalar analogue of G_⊥ as −(q²/16π²)∫_1^{ℓ²}R_S^lat dt/t + O(1).
   - Then test the n = 2 (ℓ = 9) case by fibre sampling, to see whether the error is n-uniform.
   - Criteria first; jobs < 20 min and < 1 GB under the lock.
   - The session-7 objection (2D has a power law, not a log) is valid, so do it in 4D or not at all.
2. **Prove (L-loc2).** It is short and closes COV-GI-∞ and MS (iv) at each n.
3. **S7-1, S7-3, S7-4, S7-5:** wording only, but S7-1 and S7-3 protect the 1/22 and the well-posedness of (V-IR).
