# REVIEW_FLOW_S9: hostile review of lane C session 9 (FLOW.md §64-§72 and the [RFL8-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f12*. This file is the only one I edited.
No commits, PRs or pushes.

Inputs (read-only, by offset):
- REVIEW_FLOW_S8.md (all).
- FLOW.md §57 (l.2803-2835), every [RFL8-fix] site (l.856, 2206, 2216, 2247, 2252, 2264, 2286, 2372, 2821, 2850, 2874,
  2921, 2934, 2950, 2979, 2983, 2985, 2988, 3003, 3010, 3020, 3044, 3067, 3113, 3120), §41 setting (l.2100-2117), (L-loc)
  (l.2325-2340), FP-exact (l.2606-2630), the vector 𝒞_n (l.1461), §64-§72 (l.3137-3430) in full.
- FLOW_LOG.md l.352-398 (session 9).
- checks: f12_criteria.md, f12_proxy_2pt.py (all), f12_out.txt, f12_time.txt; f11_out.txt l.32, 43.
  - BSD stat (UTC; local EDT +4 h): f12_criteria.md born 07:45:18 (3764 B); f12_proxy_2pt.py born 07:49:15, modified
    07:49:54 (17869 B, md5 fea3107e…, matches FLOW_LOG l.375); f12_out.txt born 07:54:08, modified 07:54:12 (3628 B);
    f12_time.txt 07:54:12 (101 B). All agree with FLOW_LOG l.370-388.
  - The §64 pre-statement (FLOW_LOG l.361: 07:36:41, 343953 B, md5 64e275…) cannot be re-verified, because FLOW.md has
    changed since (now 374195 B, mtime 08:00:46). The order criteria → script → smoke → run is confirmed by the stats.

Numerics (scratchpad `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow9/`):
- All runs: nice 10, all BLAS threads = 1, plain `python3` (no -I), no `timeout`, no trap. Nothing was written to checks/
  (no `__pycache__` there). No process was left running, and the lock directory is empty.
- At 08:02 UTC the lock was held by another job and memory was 34% free. My runner waited, and checked load and memory
  inside the lock before starting anything.
- **Lock acquisition 1: 08:10:48-08:11:32 UTC, released once with `rmdir`.** Load 4.35, memory free 49%.
  - f12 re-run from a byte-identical scratchpad copy (md5 fea3107e…): 3.87 s, 398 MB.
  - `i1.py`: 0.7 s.
  - `ratio.py`: 39 s, **peak RSS 1.12 GB**. Memory was 51% free at its start.
- **Lock acquisition 2: 08:14:05-08:14:08 UTC, released once with `rmdir`.** Load 3.66, memory free 49%.
  - `i1b.py`: 2.8 s, 113 MB.
- `i1*.py` and `ratio.py` import an unchanged copy of the f12 functions (`f12mod.py`). I changed only the parameters:
  ε sets, fit degrees, h_u, N_K, n.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **[RFL8-fix] S8-1..S8-6 and the tally correction: all applied, 25 tag occurrences as claimed (l.3404).** Each one
  matches REVIEW_FLOW_S8 §9. No content error was introduced.
  - Also correct: the extra Duhamel sentence for j = 2 (l.2979-2980), and the K-L one-liner (G'' = 1 − δ, mean zero).
- **Provenance: CLEAN with one disclosure point.**
  - The pre-statement, criteria, script, smoke run, void run and valid run are in the stated order.
  - The void run (load 8.53) was correctly discarded and disclosed.
  - The explicit vertex formulas of §65 (b) (u, m_2, c_2) were written at 07:57-08:00, i.e. **after** the script
    (07:49) and the run (07:54). §64 (S1) fixed only their structure.
  - I re-derived c_2, the ϑ-selection and the ¼(T − I) normalisation by hand. u and m_2 rest on f12's n = 2 real-space
    check (2.3e-11, 2.1e-9).
  - c_2 vanishes at n = 1, so I1 does not test it. Only P-a at n = 2 tests it numerically (S9-7).
- **Lemma S-2pt: CONFIRMED.**
  - (a) is correct: one ancestor per site, so the matrix product has a single term, and d|w|² = 2Re(i·avg dθ) = 0.
  - (b) is correct: the block inverse, the ϑ-selection for 0 < |p| < π/ℓ, and the vertex normalisations. I checked c_2
    analytically.
  - (c) is correct: F = 2ε sin(p/2)sin(px_2 + p/2 + ϑ), so h_n = ĥ(pe_2)sin²(p/2).
  - **f12 re-run: IDENTICAL** (14/14).
  - I1's 8.5e-8 (threshold 1e-7) is ε-fit truncation, not a formula error. Higher-degree fits bring it to **9e-9**, and the
    momentum side is stable to 4e-15 under h_u → h_u/3 (§4.2).
- **Proposition S-tel: CONFIRMED.** The unrolling, the Sylvester step, the inverse-form Woodbury, the induction on the kernel
  of Γ_k^{-1}, and the level-unit recursion Γ̃_{k+1} = L²QΓ̃_kQ^† + s^{-1} all check. One wording fix (S9-6).
- **Lemma S-fix: CONFIRMED.**
  - I checked: the closed form of γ_k, the s_ℓ bound x²/(24ℓ²), the dominator Π_μmin(1, 4π²/x_μ²) and its 4D
    summability, the O(ℓ^{-3}) tail, the O(ℓ^{-2}) error of the m = 0 term, and the uniform gap of L^{-2k}H_k(1).
- **Priority-2 answer. Yes: if |φ_k − 2c_g log L| ≤ Cθ^k, then sup|ρ_n| ≤ C/(1 − θ) immediately (geometric sum).** But
  S-fix alone does not give that rate. φ_k also depends on the plane-wave vertices of Γ̃_k.
- **(VC) + (IRR*) is sufficient for (S4), not "exactly" equivalent to it. Moreover, (IRR*) is redundant (S9-1).**
  - There is an exact identity **ρ_n = a_0 − a_n**, where a_n := lim_{P→0}[x_n(P) − 2c_g log(1/P)] is the IR finite part
    of the level-n polarisation. a_n exists for every n by S-red (i), given the standard fine-lattice expansion of x_0.
  - Hence **φ_k − 2c_g log L = a_k − a_{k+1} exactly.** The log coefficient 2c_g is forced at every level, and no fixed-point
    universality theorem is needed.
  - **(V-IR-S) ⟺ sup_n|a_n| < ∞.** That needs only n-uniform bounds on the level-unit vertex data with uniform IR control,
    not geometric convergence. The rate is a bonus.
- **(VC) is not an RG-contraction problem (S9-2).**
  - Γ̃_k = L^{2k}𝒦_k is in closed form (S-tel (a)). Its U = 1 vertices are the explicit separable alias sums of §65 (b) at
    level k, so (VC) is S-fix's dominated-convergence argument applied to them, on Γ̃_k^{-1}, which is regular at K = 0.
  - Difficulty: moderate and explicit. The real work is the slower alias decay of the first-order vertex form factors
    (G_κ, one derivative of the block form factor) and the uniformity of the IR expansion. The ratio → L^{-2} is the
    midpoint-rule rate this predicts.
- **f12: CONFIRMED.**
  - **Reviewer extension, refined:**
    - The increment ratio 4→5 is 0.11103-0.11109 across N_K ∈ {16, 20} and h_u ∈ {0.15, 0.2, 0.3}. That is L^{-2} = 0.11111
      to 5e-4 relative.
    - **The 5→6 ratio 0.115 quoted in §70 is NOT converged.** It ranges 0.112-0.116 with h_u.
    - c^S_6 moves by 6.0e-10 under halving h_u, which fails f12's own I3 threshold of 1e-10. n = 5 is at the edge (9.7e-11).
    - Fix: S9-3.
- **Lemma V-2pt (a)-(c), given (L-loc2): CONFIRMED (conditional), with two wording fixes (S9-5).**
  - "Explicit kernel" overclaims: the kernel is defined, not written.
  - Δ'(1) is strictly positive, but its gap is ~ℓ^{-4} in fine units (4D capacity). It is therefore not uniform in level
    units, and the vector route must remove the ghost exactly rather than bound Δ'^{-1}.
- **(S5) (d): CORRECT as a kernel statement** (exactly one zero mode dΔ^{-1}ν_K per level momentum K ≠ 0 and colour).
  - **The consequence "the reference must carry a mass" is too strong (S9-4).**
  - K̃ = K_F − DP_nD^* differs from the massless Feynman operator K_F(1) by a rank-one-per-fibre term.
  - At U = 1, D^*K_F^{-1}D = 1. So the bordered Woodbury about K_F(1) is exact with no mass: its level-site block is
    −1 + 1 = 0, and the residual mode is lifted through the border b = D_ℓg.
- **(S6) NO: CORRECT, but only for the stated form (Γ_0^{-1} = K̃_n). It is not structural.**
  - The ghost −log det Δ'_n telescopes exactly by Jacobi decimation, with n-independent steps, for every U.
  - At U = 1 and at critical backgrounds, E'_n can be removed: the total = fine Feynman + level-n transverse Feynman block
    covariance X_n = 𝒞_n + MK_F^{-1}M^† + a level ghost. X_n obeys the n-independent recursion X_{k+1} = T_kX_kT_k^† + κ^{-1}Π^{-1}
    (l.1461).
  - What remains OPEN: the off-shell defect HD_U = O(D_U^*F) along plane waves, at order ε²p² (§6).
- **Corrected tally: 50 PROVEN-HERE, as claimed.** V-2pt is counted conditional on (L-loc2), following the COV-GI-∞
  precedent. Scope annotations are in §7.

---

## 1. Priority 1: the [RFL8-fix] edits and provenance

| Fix | Where | Verdict |
|---|---|---|
| S8-6, (vi) pointers | l.856, 2206, 2216, 2247, 2252, 2264, 2286, 2372 | APPLIED (8 sites, as asked) |
| S8-2, A_0 | l.2821 (statement, "read as" annotation), l.2985-2986 (proof) | APPLIED |
| S8-2, Duhamel factor t | l.2979-2980 (with the j = 2 count t² + t ≤ t(1 + t)), l.2983 (replaced sentence) | APPLIED, correct |
| S8-3, max_i\|h_iF\| | l.2850 (Q2), l.3003 (R1), l.3020 (R-damp) | APPLIED |
| S8-3, maximiser | l.3010 | APPLIED |
| S8-4, "IR safe" | l.2874 | APPLIED |
| S8-4, Harper import | l.3044 (struck; fibrewise covariant-constant argument) | APPLIED, correct |
| S8-1, Billingsley sentence | l.2921 | APPLIED |
| S8-1, K-L one-liner | l.2934 | APPLIED, correct (G'' = 1 − δ, ∫G = 0, eigenvalues (2πk)^{-2}, ×2) |
| S8-1, import list | l.2950 | APPLIED |
| S8-5, Nielsen-Olesen scope | l.3067, l.3113 | APPLIED |
| tally, 46; (Q1)(c) a remark | l.2988, l.3120 | APPLIED |

25 occurrences at fix sites, plus mentions at l.3137, 3140, 3205, 3404, 3424. That matches l.3404.

**Provenance.**
- §64 was the first edit (07:36:41). The criteria came at 07:45:18, the script at 07:49:15/07:49:54 (one pre-run edit,
  disclosed), the smoke test at 07:50, the void run at 07:51 (load 8.53, correctly voided, output set aside) and the valid
  run at 07:54:08. The extension ran at 07:55. §65-§72 were written at 07:57-08:00.
- **One point to disclose (S9-7).** §65 (b)'s explicit vertex formulas post-date the code that implements them. The
  statement (S1) (b) pre-fixed only the structure: traces over the alias fibre, diagonal plus rank one. So for u and m_2 the
  "derivation" is partly a description of the implementation.
- Independent support for them:
  - my hand derivation of c_2 (§2);
  - f12's n = 2 real-space form-factor check;
  - P-a against f11's constant-field computation, which is a different method.
- Not a defect, but §70 should say it.

## 2. Priority 2a: Lemma S-2pt (§64 (S1), §65)

- **(a) (l.3213-3216): CORRECT.**
  - A_j(Y, y) is a single product of Q-entries, because each level site has one parent. So A_jA_j^† is diagonal, and its
    entries are Σ_yΠ_kL^{-8}|w_k|².
  - d|w|² = 2Re(w̄dw) = 2Re(i·avg dθ) = 0 at A = 0. ✓
- **(b) (l.3217-3248): CORRECT.**
  - Schur: det 𝔐 = det(−𝒞)det(Δ + M^†𝒞^{-1}M). ✓
  - The block inverse equals (Λ^{-1} ⊕ 0) − αξξ^† with ξ = (Λ^{-1}v, −1) and α = (C + Ĝ)^{-1}. I multiplied it out. ✓
  - Invertibility at K = 0, m = 0: Λx + vy = 0 forces y = 0 (v_0 ≠ 0), then x = x_0e_0, then v_0x_0 = 0. ✓
  - Second order:
    - the ϑ-free part of −½tr(𝔐_0^{-1}𝔐_1)² is −¼I;
    - tr𝔐_0^{-1}·¼𝔚 = ¼T;
    - the ±2p parts vanish iff 2p ∉ (2π/ℓ)Z, i.e. |p| < π/ℓ.
    So h = ¼∫ℓ^{-4}(T − I). ✓
  - Δ_U vertices: the direction-1 hop with a = a(x_2) gives 2a sin k_1 at first order and a²cos k_1 at second, so W = 2cos k_1
    with ¼ε²·2cos k_1 = ½ε²cos k_1. ✓
  - **c_2, re-derived:**
    - |w_κ|² = cos²(Δ_κ(a − a')/2), and the ϑ-average of (a − a')² is ε²(1 − cos(pΔx_2)).
    - The digit averages E d_1² = 2/3 and E(1 − cos pL^κd_2) = (2/3)(1 − cos pL^κ) give −(1/9)L^{2κ}(1 − cos pL^κ) per ε². That is
      −(4/9)L^{2κ}(1 − cos pL^κ) per ε²/4, summed over the steps κ = j..n−1 of A_j, with weight κ_j^{-1}L^{-4(n−j)}.
    - First-order cross terms vanish by (a). **Matches l.3241.**
  - The Woodbury expansions of T_n and I_n (l.3244-3247) are the standard rank-one algebra. ✓
- **(c) (l.3249-3262): CORRECT.**
  - F_x = 2ε sin(p/2)sin(px_2 + p/2 + ϑ), avg F² = 2ε²sin²(p/2), so ½H_0/V = ε²ĥ(pe_2)sin²(p/2).
  - The F-id normalisation 2c^S_n = ĥ(0) matches. Evenness follows from the x_2 reflection about a level site (odd L). ✓
  - Small points, not load-bearing:
    - "Dρ_0(1) = 0" is irrelevant: a = ε cos(…) is exactly linear in ε, so the ε² coefficient is ½D²G alone.
    - "the background is a constant pure gauge" at p = 0 is true only for the infinite-volume density (on a torus it is a
      holonomy).
  - **Verdict: CONFIRMED.** f12 P-a is independent evidence (U = 1 plane wave against constant-field Bloch):
    - n = 1: 6.5e-11, within f11's 7-digit rounding;
    - n = 2: 5.1e-9 (1.8e-6 relative). This is above the rounding, so it is the joint error of f11 and f12, mostly f11's.

## 3. Priority 2b: Proposition S-tel, Lemma S-fix, and (VC)/(IRR*)

### 3.1 S-tel (§66): CONFIRMED

- (a): the unrolling Γ_2 = Q_1Q_0Δ^{-1}Q_0^†Q_1^† + κ_1^{-1}Q_1Q_1^† + κ_2^{-1} is 𝒦_2. ✓
  - Sylvester: det(QΓQ^† + κ^{-1}) = κ^{-N_{k+1}}det Γ det(Γ^{-1} + κQ^†Q). ✓
  - With S-red (ii), the τ log Δ cancels against −log det Γ_0, so G_S,n = Σ_kΦ_k exactly. ✓
- (b): the variational form, ker Γ_k^{-1} = constants (induction), and the gap by compactness are correct.
  - The locality induction is correct as stated. It is provable in the proxy, unlike the vector (L-loc2).
- (c): Γ̃_{k+1} = L²QΓ̃_kQ^† + s^{-1}, since κ_{k+1}^{-1}L^{2(k+1)} = s^{-1}. ✓
  - φ_k is the F² coefficient per level-k site. The L^{2k} rescaling drops out of [F²]. ✓
- (d): the equivalence is with bounded partial sums.
  - **Reading (1) (l.3299) says "summable"**, which is the stronger (S4)-type statement (S9-6).

### 3.2 S-fix (§67): CONFIRMED

- γ_k = ℓ^{-2}Σ_mΠD_1²/λ + s^{-1}(1 − L^{-2k})/(1 − L^{-2}). ✓
- D_1(k_m) = ±sin(K/2)/s_ℓ(x) and λ = Σ(2s_ℓ/ℓ)², so the m-th term is Π[sin(K_μ/2)/s_ℓ]²/Σ(2s_ℓ)². ✓
- Rate: |s_ℓ/(x/2) − 1| ≤ x²/(24ℓ²) (sin y/y ≥ 1 − y²/6), and max_μx_μ²/|x|² ≤ 1.
  - So the error is ≤ Cℓ^{-2}Σ_mΠmin(1, 4π²/x_μ²) < ∞. ✓
  - The tail beyond |x_μ| > πℓ is O(ℓ^{-3}). ✓
  - The m = 0 term has absolute error O(ℓ^{-2}). ✓
- The gap of L^{-2k}H_k(1): γ_k ≥ s^{-1} gives Γ̃_k^{-1} ≤ s. The uniform convergence of the fibres to H̃_*, and H̃_* ≥ c_*
  by the §66 (b) argument with continuity on the compact zone, are both fine. ✓

### 3.3 Is boundedness of ρ_n immediate? Is it exactly (VC) + (IRR*)?

1. **Immediate:** |φ_k − 2c_g log L| ≤ CL^{-2k} ⟹ |ρ_n| ≤ C/(1 − L^{-2}), and ρ_n converges. Yes, trivially.
   - **S-fix does not supply this rate.** φ_k is the P² coefficient of a step kernel. That kernel uses the first- and
     second-order plane-wave vertices of Γ̃_k^{-1} and Q, not only the symbol γ_k.
2. **(VC) + (IRR*) ⟹ (S4) (l.3334-3342): correct.**
   - (VC) ⟹ |φ_k − φ_*| ≤ C'θ^k. The step kernel is analytic in the data on the uniformly gapped region, and the P²
     coefficient is a Cauchy integral.
   - In the inverse variables Γ̃_k^{-1} (symbol 1/γ_k ~ |K|²), no IR weight is needed at all: H_k is gapped (§67).
   - **(VC) should be stated on Γ̃_k^{-1}.**
3. **(IRR*) is redundant (S9-1).**
   - For P > 0 put x_k(P) := [ε̃²]τ_k log Γ̃_k^{-1}/(P²/2). It is finite: in 4D, massless bubbles are IR-finite at nonzero
     external momentum.
   - S-red (ii) holds along the plane-wave family (a determinant identity, Δ_U invertible). So
     **c^S_n = lim_{p→0}[x_0(p) − x_n(ℓp)]**: the fine minus the level-n polarisation, each finite at p > 0.
   - Let x_0(p) = 2c_g log(1/p) + a_0 + o(1). This is the IR expansion of the massless fine-lattice scalar vacuum
     polarisation, a standard one-loop fact to be proved or imported-and-reverified.
   - Then finiteness of c^S_n (S-red (i)) forces x_n(P) = 2c_g log(1/P) + a_n + o_n(1) **for every n**, with
     **a_n = a_0 − ρ_n.**
   - So **ρ_n = a_0 − a_n** and **φ_k − 2c_g log L = a_k − a_{k+1}** exactly. I checked this against the step identity
     φ_k = lim[x_k(P) − x_{k+1}(LP)] of l.3340.
   - The log coefficient is 2c_g at every level, because each finite φ_k forces equal log coefficients at k and k + 1.
     So "φ_* = 2c_g log L" holds automatically once a_k converges, and no universality theorem for Γ̃_*^{-1} is needed.
   - **(V-IR-S) ⟺ (UIR): sup_n|a_n| < ∞.** This is a single-level statement about the IR finite part of the level-n
     block-spin covariance's polarisation. It needs only n-uniform bounds plus a uniform IR expansion of x_n, not a rate.
     The rate form is a_n → a_* at θ^n.
   - Numerically, a_n − a_0 = −ρ_n → +1.76805e-3.
4. **How hard is (VC)? Not an RG contraction (S9-2).**
   - l.3343 says "(VC) is an RG contraction for the affine recursion … not written here". But S-tel (a) has already solved
     the recursion: Γ̃_k = L^{2k}(M_UΔ_U^{-1}M_U^† + 𝒞_k(U)).
   - So the U = 1 plane-wave vertices of Γ̃_k are exactly the separable alias sums of §65 (b) at level k (D_1, u, m_2, c_2, Σ,
     W, over 1/λ^a λ'^b, a + b ≤ 3), and those of Γ̃_k^{-1} follow by the resolvent identity.
   - (VC) is S-fix's method, Taylor in s_ℓ plus a dominated alias sum, applied to these explicit sums.
   - What actually needs checking:
     - (i) **summability of the alias sums with the first-order vertex form factors.** G_κ = −(2/3)L^κsin(qL^κ)Π_{r≠κ}δ_r is a
       derivative of a block product and decays one power of x_μ slower than D_1. The direction-1 sums carry
       G_κ·G_{κ'}/λ², so the 4D dominator must be redone direction by direction;
     - (ii) **the Riemann-sum rate.** The balanced-digit (centred) blocks give midpoint-type sums, hence ℓ^{-2}. This matches
       f12's ratio → 1/9;
     - (iii) **uniformity of the IR expansion of x_k(P) in k.** This comes from the leading small-K form |K̂|²(1 + O(K²)) of
       Γ̃_k^{-1} (S-fix) and the Ward structure (D(0) = 1, gauge covariance) of the vertices.
   - Rating: explicit, moderate (a long but elementary lemma), well within the session's methods. **f12 shows the
     increments shrinking with ratio 0.0946, 0.1099, 0.1111 (reviewer, robust).** That is the predicted L^{-2k} =
     ℓ^{-2} midpoint rate, with a faster correction at small k.

## 4. Priority 4: f12

### 4.1 Re-run

- Lock acquisition 1 (08:10:48 UTC; load 4.35, memory free 49%). Scratchpad copy, md5 identical.
- **Output identical to checks/f12_out.txt** apart from the start-time and timing lines. 14/14 PASS, 3.87 s, 398 MB.

### 4.2 I1 margin: 8.5e-8 against a 1e-7 threshold

The momentum formula is stable: −7.8281482457{164, 479, 476}e-5 at h_u = 0.3, 0.15, 0.1.

| Direct torus fit (ε-polynomial) | h direct | rel. diff |
|---|---|---|
| f12: ε 0.02-0.08, deg 3 | −7.82814758e-5 | 8.5e-8 |
| ε 0.01-0.04, deg 3 | −7.82814890e-5 | 8.3e-8 |
| ε 0.01-0.08 (8 points), deg 3 / 4 / 5 | −7.8281473e-5 / −7.8281481e-5 / −7.82814817e-5 | 1.2e-7 / 1.8e-8 / **9.2e-9** |
| ϑ-averaged (4 ϑ), deg 4 | −7.8281479e-5 | 4.3e-8 |
| ε ≤ 0.02, deg 2-3 | roundoff-limited | 5e-7 to 8e-7 |

- The residual is ε-fit truncation, not a formula error: it falls with the fit degree, to 9e-9.
- The direct value depends on ϑ at relative 2.3e-6 at ε = 0.02. This is an ε⁴ effect: on this torus 4p = 2π/3 is an
  umklapp momentum for ℓ = 3. The ε² coefficient is ϑ-free, as (b) says.

### 4.3 Increments and the n = 5, 6 extension (reviewer, `ratio.py`; the f12 functions unchanged)

| setting | c^S_6 | inc 4→5 | inc 5→6 | ratio 4→5 | ratio 5→6 |
|---|---|---|---|---|---|
| N_K 16, h_u 0.3 | 1.21460432789e-2 | −1.684775e-7 | −1.936067e-8 | 0.11109 | 0.11492 |
| N_K 20, h_u 0.3 (= FLOW's extension) | 1.21460432331e-2 | −1.684620e-7 | −1.942408e-8 | 0.11108 | 0.11530 |
| N_K 16, h_u 0.2 | 1.21460431191e-2 | −1.684328e-7 | −1.957102e-8 | 0.11106 | 0.11619 |
| N_K 16, h_u 0.15 | 1.21460438797e-2 | −1.683890e-7 | −1.885638e-8 | 0.11103 | 0.11198 |

- n = 3, 4 reproduce f12 to ≤ 2e-12 (N_K) and ≤ 8e-12 (h_u).
- The h_u change is 9.7e-11 at n = 5 and **6.0e-10 at n = 6**. f12's I3 threshold is 1e-10.
- **So ρ_6 and the ratio 0.115 (l.3396-3397) are not converged under f12's own criterion.** The ratio 4→5 = 0.1111 is
  robust to 6e-5.
- ρ_∞ ≈ ρ_5 + inc_{4→5}·(1/8) = −1.768046e-3. This agrees with §70's −1.76805e-3.

### 4.4 Criteria compliance

- **I2.** The criteria (l.18 of f12_criteria.md) ask for "the fitted constant term of h_n(p) in a fit with a free
  constant". The script instead tests the unsubtracted p = 0 value h_n(0) directly.
  - This is a stronger and simpler test, and §70 reports what was computed. But it is a wording deviation from the
    criteria (S9-7).
- **I3 and I4:** as pre-stated.
- **P-a and P-b:** thresholds as pre-stated, and pass with large margins (P-b: 1.38e-5 against 4.9e-5).
- **S9-F3 (geometric decrease):** reported only, and supported through n = 5.

## 5. Priority 3a: Lemma V-2pt (§64 (S5), §69)

- **(a) (l.3349-3355): CORRECT given (L-loc2).**
  - The Cartan plane wave H_1ε cos(px_2 + ϑ) commutes with the torus, so the root sectors stay decoupled.
  - The S-2pt (c) argument applies verbatim to the root block, with MS (iv) and F-id-exp under (L-loc2).
  - GH-log (c) is unconditional since §58.
- **(b) (l.3355-3357): CORRECT.**
  - K_F + μ and Δ_0 + μ are finite range and covariant, gapped by μ − C|f|^{2/3}. The normalisation 2𝔪_α(μ) ↔ the p²
    coefficient matches §57 (Q1)'s 𝔪_α := [f²]{log det_C(K_F + μ) − log det_C(Δ_0 + μ)}.
- **(c) (l.3357-3362): CORRECT as an equivalence**, via VIR-eq (|𝔪_α(ℓ^{-2}) − 𝔠_α(ℓ²)| ≤ A_0q²). Two wording points (S9-5):
  1. "an **explicit** U = 1 one-loop kernel" (l.3183): the kernel is *defined* by the U = 1 Hessians. No fibre formula is
     written, unlike S-2pt (b). Say "defined"; the explicit form is the next target.
  2. "every propagator is the inverse of an operator ≥ c > 0" is true at each n, but the constants are n-dependent and
     not level-uniform.
     - **Δ'(1) = E'Δ_0E' has gap ≍ ℓ^{-4}** in fine units, i.e. ≍ ℓ^{-2} → 0 in level units.
     - Rayleigh quotient with ρ = (g(0) − g)/g(0), where g is the cell Green's function: ⟨ρ, Δρ⟩/||ρ||² ≈ 1/(g(0)ℓ⁴) and
       g(0) → G_{Z⁴}(0) ≈ 0.155. This is the 4D capacity of a point.
     - So no n-uniform vector bound may pass through Δ'(1)^{-1}. The ghost must be removed exactly: GH-log (c), or the
       Jacobi telescoping of §6.
     - Ã(1) ≥ c_n (N-f (ii)) is likewise not shown to be level-uniform.
- **(d) (l.3363-3369): the kernel statement is CORRECT; the conclusion is too strong (S9-4).**
  - K̃(1)A = 0 ⟺ dA = 0 and E'd^*A = 0. Every alias is ≠ 0 at K ≠ 0, so A = dλ and Δλ is supported on the level sites (one
    dimension per fibre per colour). Hence the kernel is span{dΔ^{-1}ν_K}. ✓
  - Equivalently, K̃ = K_F^{1/2}(1 − ww^†)K_F^{1/2} with w = K_F^{-1/2}Dν and ||w||² = ν^†D^*K_F^{-1}Dν = 1, because K_FD = DΔ_0
    at U = 1. So there is exactly one zero eigenvalue. ✓
  - **"So the Woodbury reference must be K_F(1) + μ … with μ carried explicitly" (l.3364) does not follow.** A massless
    reference works: see §6 (1).

## 6. Priority 3b: (S6) and a reformulation that restores the step structure

**(S6) NO (l.3370-3376): CORRECT, but only in the stated form**, where the decomposition starts from Γ_0^{-1} = K̃_n with
E'_n inside. Both terms named (E'_n in DE'_nD^* and in Δ'_n) can be removed:

1. **Gauge-fixing term, exact at U = 1 (and at critical backgrounds where K_F is invertible).**
   - Write DE'_nD^* = DD^* − DP_nD^*, with P_n = 1 − E' of rank 1 per fibre and colour. Then Ã = K_F + B^†JB, with
     B = (M; P_nD^*) and J = diag(𝒞_n^{-1}, −1).
   - Use K_FD = DΔ_0, so D^*K_F^{-1}D = 1. Use MD = D_ℓ∘ev (COV-GI proof (1), FP-exact (1)), so MK_F^{-1}DP_n = D_ℓg with
     g := (Δ_0^{-1})|_{level sites}.
   - The capacitance is the bordered matrix [[X_n, b], [b^†, 0]], with X_n := 𝒞_n + MK_F^{-1}M^† and b = D_ℓg. Its level-site
     block is −1 + 1 = 0.
   - Hence det Ã = det K_F·det𝒞_n^{-1}·det X_n·(b^†X_n^{-1}b).
   - **Ghost (Jacobi):** det Δ'_n = det Δ_0·det(Δ_0^{-1}|_{level}) = det Δ_0·g. g cancels between the two, leaving
     **total_n = [½log det K_F − log det Δ_0]_fine + ℓ^{-4}τ_n[½log det_⊥(P_⊥X_nP_⊥) + ½log Δ_ℓ]**,
     with Δ_ℓ the level Laplacian symbol (Jacobi again: det X·D_ℓ^†X^{-1}D_ℓ = det_⊥X·D_ℓ^†D_ℓ).
   - **E'_n has disappeared.** The level piece is the transverse part of the Feynman-gauge level-n block covariance, which is
     exactly the "level-n ⊥ group" of (Q1)(d). The vector analogue of S-red (ii) needs no mass.
2. **Steps.** l.1461 gives 𝒞_n = κ^{-1}Σ_jA_jΠ_j^{-1}A_j^T with A_j = T_{n−1}⋯T_j. So X_{k+1} = T_kX_kT_k^† + κ^{-1}Π_{k+1}^{-1} with
   X_0 = K_F^{-1}: an n-independent recursion.
   - Sylvester as in S-tel cancels ½log det K_F, and the step operators are H^V_k = X_k^{-1} + κT_k^†ΠT_k.
   - In inverse form, X_{k+1}^{-1} = κΠ − κ²ΠT_k(H^V_k)^{-1}T_k^†Π never needs K_F^{-1}.
   - H^V_0 = K_F + κT^†ΠT is gapped at U = 1, and at U_f for small f by IMS: the step IR term lifts the Nielsen-Olesen band,
     as in Ã.
   - The level ghost ½log Δ_ℓ (or ½log D_ℓ^†X_n^{-1}D_ℓ) telescopes by differences between consecutive levels, and the fine ghost
     by Jacobi decimation: log det Δ'_n = Σ_{k<n}log det(Δ^{(k)} restricted to Λ_k∖Λ_{k+1}), with Δ^{(k)} := (Δ_0^{-1}|_{Λ_k})^{-1}.
     That is an exact identity for every U, with n-independent steps, gapped O(1) in level-k units.
3. **What is OPEN in this route** (it is a route, not a claim):
   - (a) **The off-shell defect.** HD_U = 0 holds only at critical backgrounds. Along the plane wave, H(U)D_U = O(D_U^*F) =
     O(εp²). Its contribution to the ε²p² coefficient, via a defect at O(ε) times a vertex at O(ε) with IR propagators,
     must be shown to vanish or be computed.
     - At U_f the identity is exact, but the fine Feynman piece then meets the Nielsen-Olesen obstruction. So this is the
       crux of the reformulation.
   - (b) MD = D_ℓ∘ev must be checked at U ≠ 1 at the needed order. It holds at critical U_0 (FP-exact (1)).
   - (c) The bordered identity at U = 1 is a finite-dimensional statement. It can be checked to machine precision on a small
     torus before any proof.
   - A gauge-fixing-independence variant uses FP-exact: the total is the orbit-space Gaussian of the Λ'-invariant weight,
     and one fixes per step on Λ_k∖Λ_{k+1}. It needs the same criticality, so it adds nothing beyond (1)-(2).

## 7. Per-item verdicts

| Item | Verdict | Fix |
|---|---|---|
| [RFL8-fix] S8-1..S8-6, tally (25 tags) | **APPLIED**, correct | — |
| Provenance | **CLEAN**; void run handled correctly | S9-7 (§65 (b) formulas post-date the code; I2 wording) |
| (S1) Lemma S-2pt | **CONFIRMED** (c_2 re-derived; I1 true agreement ≤ 9e-9) | — |
| (S2) Proposition S-tel | **CONFIRMED** | S9-6 ("summable" → "bounded partial sums", l.3299) |
| (S3) Lemma S-fix | **CONFIRMED** | — |
| (S4) and its reduction (§68) | reduction **CORRECT but not sharp**: (IRR*) is redundant; (VC) is explicit, not an RG contraction; (V-IR-S) ⟺ sup\|a_n\| < ∞ | S9-1, S9-2 |
| (S5) (a)-(c) Lemma V-2pt | **CONFIRMED given (L-loc2)** | S9-5 ("explicit" → "defined"; Δ'(1) gap ≍ ℓ^{-4}, not level-uniform) |
| (S5) (d) | **kernel CORRECT; "must carry a mass" WRONG** (the bordered Woodbury about massless K_F(1) is exact) | S9-4 |
| (S6) | **NO CORRECT only in the stated form**; E'_n removable (bordered Woodbury + Jacobi); off-shell defect OPEN | S9-4 |
| f12 | **CONFIRMED**; re-run identical; P-a, P-b strong | S9-3 (n = 6 not converged; ratio 4→5 = 0.1111 robust) |

**Corrected tally: 50 PROVEN-HERE (claimed 50)** = 46 + S-2pt + S-tel + S-fix + V-2pt (given (L-loc2)).
- **Scope annotations:**
  - V-2pt (a)-(c) conditional on (L-loc2). (d)'s consequence is narrowed by S9-4.
  - S-2pt (b)'s u and m_2 are verified numerically (n = 2 real-space check), not by an independent derivation.
- **IMPORTED-AND-REVERIFIED:** L4b; the Lévy-process functional CLT.
- **To be added as a standard input (S9-1):** the IR expansion x_0(p) = 2c_g log(1/p) + a_0 + o(1) of the massless
  fine-lattice scalar polarisation. Prove it, or import and reverify it.
- **ARGUED, not counted:** (L-loc2).
- **OPEN:**
  - (V-IR) in the form (Q1)(d), i.e. sup|ρ^V|/q² < ∞;
  - (V-IR-S), now (UIR): sup_n|a_n| < ∞;
  - the vector off-shell defect (§6 (3a));
  - (L-loc2);
  - the rest of §72's list.

## 8. Binding fixes for the next lane-C session

1. **S9-1 (§68, l.3339-3342).** Replace (IRR*) with the exact identity:
   - ρ_n = a_0 − a_n, with a_n := lim_{P→0}[x_n(P) − 2c_g log(1/P)];
   - a_n exists for every n by S-red (i) plus the fine expansion of x_0 (name it as an input);
   - φ_k − 2c_g log L = a_k − a_{k+1}.
   Restate (S4) as (UIR): sup_n|a_n| < ∞, with the rate form a_n → a_* at θ^n.
2. **S9-2 (§68, l.3343-3344).** Strike "RG contraction for the affine recursion". State (VC) on the vertex functions of
   Γ̃_k^{-1}, which are explicit by S-tel (a) and §65 (b) at level k. Name the three real tasks of §3.3 (4): alias
   summability with the G_κ factors, the midpoint ℓ^{-2} rate, and IR uniformity.
3. **S9-3 (§70, l.3395-3400).** Mark ρ_6 and the ratio 0.115 as not converged: the h_u change is 6.0e-10 > 1e-10, and the
   ratio spans 0.112-0.116 (REVIEW_FLOW_S9 §4.3). Quote the 4→5 ratio as 0.1111 (robust). Add that I1's 8.5e-8 is ε-fit
   truncation (degree-5 fit: 9e-9).
4. **S9-4 (§69, l.3363-3364, l.3370-3376; §71 l.3413-3416).**
   - In (d), replace "so the Woodbury reference must be K_F(1) + μ … with μ carried explicitly" with: "…for the plain
     Woodbury about K̃; the bordered Woodbury about the massless K_F(1) is exact (D^*K_F^{-1}D = 1; REVIEW_FLOW_S9 §6 (1))".
   - Narrow (S6) to "NO for the decomposition starting from K̃_n". Record the route of §6 (bordered Woodbury, Jacobi ghost
     decimation, X_k recursion), with the off-shell defect as its OPEN crux.
5. **S9-5 (§64 l.3183, §69 l.3358-3361).** Change "explicit" to "defined by the U = 1 Hessians". Add that Δ'(1)'s gap is
   ≍ ℓ^{-4} (fine units), so the ghost must be removed exactly and never bounded in the n-uniform route.
6. **S9-6 (§66 Reading (1), l.3299).** "is summable" → "has bounded partial sums ((S2) (d)); summability is (S4)".
7. **S9-7 (§70).**
   - Disclose that §65 (b)'s explicit vertex formulas were written after f12 ran.
   - State that c_2 and the multi-κ structure are untested by I1 (c_2 = 0 at n = 1) and are covered by P-a at n = 2 and by
     REVIEW_FLOW_S9 §2.
   - Note that I2 was implemented as the direct h_n(0) test, not the free-constant fit of the criteria.

## 9. Next target

1. **(UIR) for the scalar proxy (analytic).** Prove level-unit convergence of the explicit vertex data of Γ̃_k^{-1}, by S-fix's
   method applied to the §65 (b) alias sums at level k, with the IR uniformity of x_k. This gives sup|a_n| < ∞, and the rate
   L^{-2n} as a bonus.
   - **Check f13 (pre-state):** compute x_n(P) − 2c_g log(1/P) on a P-grid for n = 1..5.
     - Prediction: n-convergence uniformly in P ∈ [P_min, π] at rate ≈ L^{-2n}.
     - Its P → 0 limit must reproduce a_0 − ρ_n from f12 to 1e-9.
   - This tests (VC) directly, not only its consequence.
   - Use h_u ≤ 0.15 for n ≥ 5. Jobs < 20 min and < 1 GB under the lock. My n = 6 run peaked at 1.12 GB, so keep N_K ≤ 16
     there.
2. **Vector (the crux).**
   - (i) State and prove the bordered identity of §6 (1) at U = 1. Check it first to machine precision on a small torus
     (finite-dimensional).
   - (ii) Prove the Jacobi ghost telescoping and the X_k recursion.
   - (iii) Settle the off-shell defect: is the ε²p² contribution of H(U)D_U = O(D_U^*F) zero, or computable? If it is zero, the
     vector total telescopes into n-independent gapped steps, and (V-IR) reduces to the vector (UIR).
3. **(L-loc2)**, which closes V-2pt's hypothesis.
4. Wording fixes S9-1..S9-7.
