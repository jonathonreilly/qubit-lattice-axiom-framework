# REVIEW_S21: hostile review of session 21 (R20 fixes; Lemmas CURV-lin, CURV1, E3; Proposition NAH-unif; c37)

Reviewer: an independent agent that wrote none of the proof. I edited no other file. No commits, PRs or pushes.

Inputs:
- REVIEW_S20.md (format; its 13 binding fixes).
- `diff PROOF_session20_snapshot.md PROOF_session21_snapshot.md`, all hunks. PROOF.md is byte-identical to the S21
  snapshot (`cmp`).
- PROOF l.5575-5596 (Lemma U0) and l.5797-5830 (NAH-ind). The [S21] block l.5902-6099, read in full.
- RTARGET §46-47; LOG session 21 (l.930-979, including "FOR RLARGE v2").
- RLARGE.md: grep for the fix-9 text.
- checks/c37_criteria.md, c37_kcurv.py (all 483 lines), c37{A..E}.out, c37_time.txt and the file mtimes.

Re-runs and diagnostics:
- Copies of c37_kcurv.py and c35_n5bg.py are in the scratchpad `rev21/`, together with my diagnostic `rdiag.py` (P: the
  plane-wave smooth limit; T: the torus dependence of the LP, and a closed-input LP).
- Every job ran under the mandatory lock (`until mkdir …/locks/numeric; do sleep 20; done`, then load1 < 8 and memory
  free ≥ 25%, then the job, then `rmdir` exactly once, no trap).
- nice 10, all BLAS threads 1, no `timeout`, python without -I.
- The lock was held by another worker (f6_iter_chain.py) from 21:56 to 02:50 UTC. My jobs waited for it.

---

## Bottom line

- **R20 fixes:** all 13 are applied correctly. Fix 9 was deferred to RLARGE, and RLARGE v2 has in fact already applied it
  ([v2-C], RLARGE l.13, l.72-74). So LOG's "FOR RLARGE v2" item 1 is stale.
- **The new ε-dependent torus condition T_0^(1)(ε):** the observation is correct. It is avoidable, though (fix S21-1).
- **c37 is honestly recorded:**
  - The criteria (01:26:13) predate the script (01:30:06), and the script predates the outputs (01:34-01:56).
  - B FAIL is recorded as FAIL, and the pre-run edits are disclosed.
  - My re-runs of A, B, D and E are identical to the stored outputs. C was not re-run (see Part 4).
- **The headline reading of c37 is wrong in two independent ways.** In both, the quoted K_p^♯ ≈ 0.06-0.10 understates the
  quantity the induction uses:
  - **(a) Finite torus.** The exact-input norm grows with the torus side. It is ≥ 1/L² = 0.1111 in the large-torus limit:
    the smooth plane-wave limit gives exactly 0.11111 (diagnostic P). For row 252 (E2's arg-max) the LP gives 0.062 at
    T = 4 and 0.090 at T = 6. "Below 1/L² = 0.11" and "margin ≈ 10" are therefore small-torus artefacts.
  - **(b) Wrong dual.** The LP of C2/E2 is over *exact* inputs (F = d_1a). CURV1's min_Z K_p(Z) is, by LP duality, the norm
    on *closed* inputs (d_2F = 0), and on a torus that space includes the harmonic 2-forms. That is the correct object for
    CURV1, because a non-linear F^G is only approximately closed and need not be exact. The closed-input LP gives:
    - row 252: 0.120 (T = 4) and 0.124 (T = 6), against the exact-input 0.062 and 0.090;
    - corner row 482: 0.114 and 0.115, against 0.056 and 0.082.
  - **The defensible measured statement is K_p^♯ ≈ 0.11-0.13 (level 0). That is still < 1, with margin ≈ 8.** (H-K) survives,
    but the numbers and the "below 1/L²" sentence must be corrected (fix S21-2).
- **K_ρ ≈ 2.1-2.6 (> 1) is not an obstruction.** In NAH-unif, ρ is an output only: U_{j-1} depends on U_j alone. I checked
  this against the class 𝔅_j. One threshold slip is noted below.
- **Lemma CURV-lin: CONFIRMED.**
- **Lemma CURV1: CONFIRMED-WITH-FIX at level 0** (a constants slip in step (3); the dual/representative wording; the Z
  tails).
- **Lemma E3: CONFIRMED.** The identity is exact. Its Lipschitz corollary is right as an absolute-value bound.
- **Proposition NAH-unif: GAP as an implication.** "Lemma CURV1 at level i ≥ 1 is part of the implication; its proof uses
  only (I_i) (a)-(c), U0, Bianchi, LOC" is not true:
  - CURV1 step (3) uses U0 (iv), which is specific to the Wilson action (the gradient at the lift comes from corner
    plaquettes only).
  - At level i ≥ 1, E_i^br is not a plaquette action and H_i is not finite range. The gradient at the lift needs a localised
    second-order expansion of ∇E_i^br, and that is not in (I_i).
  - The complex neighbourhood is also not propagated through the tower.
  - Two named hypotheses must be added (fix S21-5).
- **(H-C): mostly a norm artefact, but not cheaply curable.**
  - The factor 1.3·10³ is Z_colZ_row² of the absolute-value branch tangent. Z_col ≥ 27 counts the full lift on every
    crossing link at sup size, where the true pulled-back cubic vertex is scale invariant in d = 4 (Part 3).
  - The true per-level factor of the classical branch-action's third derivative is expected to be 1 + (irrelevant terms).
  - No per-level Lipschitz recursion in absolute N_0 norms can show this. The recommended norm is analytic (Cauchy) bounds
    on a level-uniform complex polydisc in curvature-adapted coordinates, which is (BG-unif) (ii)/(iv) by the composite
    contraction. A measurable intermediate step is recommended (c38).
- **Tally: 72 / 2 / 7 / 24 + 1, as claimed.** Nothing new is counted, and I confirm that nothing should be.

---

# PART 1: the R20 fixes (REVIEW_S20 binding fixes 1-13)

| # | Fix | Where (PROOF) | Verdict |
|---|---|---|---|
| 1 | NAH1-1 (polydisc) | after ε_H, l.5729-5740 | **Applied correctly.** α' ≤ r_♭/2 is in ε_H, and the chart alternative is stated |
| 2 | LOC-1 / NAH1-2 | ℓ_1 l.5718; NAH1 (b) l.5749-5760 | **Applied correctly.** The collar r_1 + 3L is in level-0 units and divided by L in ℓ_1. The central part is enlarged consistently |
| 3 | NAH1-3 (units) | l.5729-5740, l.5788-5789 | **Applied.** T_1 is the level-1 side, T_2 = T_1/L. The three hypotheses are in consistent units |
| 4 | NAH1-4 (suprema) | l.5729ff., l.5788 | **Applied correctly.** The new ε-dependent torus condition is discussed below |
| 5 | RW2-1 | l.5315-5318, l.5528-5531 | **Applied correctly**, including the ⌊T/R⌋ - 1 typo |
| 6 | RW2-2 | l.5543-5549 | **Applied correctly.** The Neumann bound 1/(γ_0 + t - C_Δα_*) needs C_Δα_* < γ_0, which γ' > 0 already presupposes |
| 7 | locality exception | header l.35-36, node l.2189-2191, tally l.4559-4560, [S20] status l.5896-5898 | **Applied in all four places** |
| 8 | NAH-ind reading | header l.40-44, l.5831-5837, l.5884-5886, LOG l.911 | **Applied**, but the numbers it now quotes ("d = 4: ≈ 0.06-0.10") inherit the S21 misreading. Fix S21-2 |
| 9 | RLARGE compatibility | deferred, LOG "FOR RLARGE v2" | **Applied elsewhere already.** RLARGE v2 [v2-C] (l.13, l.72-74, rows 3/3a) carries it. LOG item 1 is stale; item 3 is new and valid. Also stale: RLARGE row 3a says "(BG-unif) named, not precisely stated in PROOF". After S21 fix 12 it is stated (for the next RLARGE pass) |
| 10 | W0-2 scope | l.5473-5475 | **Applied** |
| 11 | c36 record | l.5599, l.5668-5675, l.5888-5891 | **Applied.** I verified B4's numbers (0.348184, -0.003808, rank 12) in c36B.out l.10 |
| 12 | (BG-unif) precise | l.5845-5866 | **Applied verbatim from the template**, with the anti-circularity clause. Accepted |
| 13 | optional items | l.5651-5652, l.5867-5871, l.5879 | **Applied.** The γ_1/36 floor is correct |

**The ε-dependent torus condition T_0^(1)(ε) (l.5732-5735): CONFIRMED as an observation. Make it avoidable (fix S21-1).**
- ρ(ε) and D(ε) = O(log 1/ε) grow as ε ↓ 0, so ℓ_1 grows. The session-20 T_0^(1)(ε_H) is the smallest torus and covers
  only ε near ε_H. That is right.
- But it is an artefact of insisting on δ_H = O(ε log 1/ε) for every ε. N5-sf1 needs only 𝔇_1 + 2δ_H ≤ γ_1/2, not δ_H = O(ε).
- Freezing ρ := ρ(ε_H) and D := D(ε_H) for all ε ≤ ε_H keeps every exponential term at its ε_H value. That value already
  satisfies the gap condition, and the ε-proportional terms only decrease. So **(a) the gap/N5-sf1 statement holds on
  T_2 ≥ T_0^(1)(ε_H) for every ε ≤ ε_H** (one fixed torus). **(b) The asymptotic δ_H = O(ε log 1/ε) holds on
  T_2 ≥ T_0^(1)(ε)**.
- Without this split, the theorem reads as if smaller backgrounds needed larger tori. NAH-unif inherits the issue through
  "T_j ≥ the level-j sizes".

---

# PART 2: c37 (criteria, honesty, re-run, and what the LP measures)

**Pre-registration and honesty: CONFIRMED.**
- Mtimes (EDT): criteria 21:26:13, script 21:30:06, outputs 21:34:51 to 21:56:05, record 21:57:18.
- The criterion "K_curv < 1 with plain row sums" FAILS and is recorded as FAIL in PROOF, RTARGET §47 and LOG, with no
  criterion edited.
- The post-run commentary ("stricter than the induction needs … blind to Bianchi") is labelled as commentary and does not
  rewrite the FAIL. Accepted.
- C2/E2 (the LP norms) were pre-registered as informational, so quoting them is not a post-hoc pivot. **But their reading
  is overstated (below).**

**Re-run (identical modulo timing).**

| Part | Result | Peak footprint | vs stored |
|---|---|---|---|
| A | PASS (1.3e-15, 8.9e-16; A2 1.3e-14 / 3.2e-15; A3 [-3.1e-15, 1 - 1.2e-14]) | 568 MB | identical |
| B | FAIL: K_p 2.2443 / 2.2619 / 2.2678; K_ρ 2.7364 / 2.9069 / 2.9690 | 585 MB | identical |
| D | κ-dependence; K_A 1.388; Z_row 2.849, Z_col 156.08, Z_colZ_row² 1266.8 | 590 MB | identical |
| E | E1 holds; level 0 K_p^♯(4) 0.06188, K_ρ^♯ 2.21918; level 1 0.10323 / 2.07397 | 563 MB | identical |
| C | not re-run (cancelled to free the lock); stored output audited; C2 row 482 reproduced by diagnostic T | n/a | n/a |

**Script audit (line-level).**
- `level0_hats` solves Õ_0x = rhs and subtracts (1 - Π)rhs, so C^0 = Õ^{-1} - (1 - Π) as defined.
- 𝒦 = ι + d·x with x = -C^0d^*ι. The ρ map is Q·x, which is right since QJa - a = 0.
- `kernel` maps row p at cell 0 to source cell S as k[S, p, ·]. This is consistent with A2's direct comparison.
- `lp_norm` maximises obj·a under |d_1a|_∞ ≤ 1, with |a| ≤ B for the gauge recession directions (B = 50 and 100 agree).
- Kernels in B, C and E are float32. That is fine for measurement, not for certification.
- **D2's second product (1 + Z_col)·max(1, Z_row)² ≠ E3's (1 + Z_col)(1 + Z_row)²** (= 157.1 × 14.8 = 2.32·10³, not 1274.9).
  This is cosmetic (informational, and the soft-term coefficient), but the ledger should quote E3's form.

**What C2/E2 measure, and why it is not K_p(Z) (my diagnostic, scratchpad `rev21/rdiag.py`, outputs `rdiagP.out` and
`rdiagT.out`; not a c37 criterion).**

1. **The smooth limit (P).**
   - For a plane wave a = e_μe^{iK·X} with |K| → 0, the response is a single Bloch fibre, so sup|F_1|/sup|F_V| =
     max_r|(𝒦(K)F̂)_r|/max_j|F̂_j| exactly.
   - n = 2π/|K| = 10, 20, 50, 200, 2000 gives **0.0838, 0.1026, 0.1096, 0.1110, 0.11111** (two polarisations agree).
   - The n = 10 value reproduces C1's "smooth sin" 0.0838.
   - So the exact-input norm on large tori is **≥ 1/L² = 1/9**: a smooth coarse curvature F spreads to F/L² on each of the
     L² fine plaquettes of the coarse face.
   - The smooth ρ ratio → 0 (0.466 at n = 10, 0.0031 at n = 2000), so K_ρ's O(1) size is a short-wavelength effect.
2. **Torus dependence (T).** The exact-input LP is C2/E2's LP; the closed-input LP is max k·F subject to d_2F = 0 and
   |F|_∞ ≤ 1. I verified d_2d_1 = 0 exactly.

| row | T | row sum | exact-input LP (c37's) | closed-input LP (= min_Z K_p(Z) row value) |
|---|---|---|---|---|
| 252 (site (0,2,1,1), plane (0,1); E2's arg-max) | 4 | 0.584 | 0.0619 (= E2) | **0.1202** |
| 252 | 6 | 0.642 | 0.0900 | **0.1236** |
| 482 (corner (2,2,2,2), plane (0,3); C2's rows) | 4 | 2.190 | 0.0560 | **0.1138** |
| 482 | 6 | 2.244 | 0.0822 (= C2) | **0.1154** |

Readings:
- The exact-input LP grows with T (0.062 → 0.090 for row 252), towards the smooth bound 1/9.
- C2's "16 largest-row-sum rows" are all corner rows. They are *not* the arg-max rows on exact inputs: row 252 at T = 6
  gives 0.090 > 0.0822. So "0.0822 at side 6" is not the side-6 K_p^♯.
- **The closed-input value is about 0.12 at both T and nearly T-stable.** LP duality gives sup{k·F : d_2F = 0, |F| ≤ 1} =
  min_Z||k - d_2^Tz||_1. **This, not the exact-input LP, is min_Z K_p(Z) on the torus.** CURV1's representative
  statement (l.5960-5961) "min_Z K_p(Z) (per row) is the exact sup-norm of the row on exact inputs" is false on a torus.
  - Exact = closed ∩ (harmonic)^⊥, and on the side-4/6 tori the harmonic (constant) 2-forms carry about half the value.
  - On ℤ⁴ (no harmonic forms) the two coincide in the limit. The closed-input numbers are then the better estimate of the
    infinite-volume K_p^♯. They lie above 1/9, consistently with the smooth-limit bound.
- CURV1 needs the closed-input dual on whatever torus it works on: F^G is only approximately closed, and need not be exact.
- **Corrected measured statement: K_p^♯ ≈ 0.11-0.13 at level 0 (rows 252/482, T = 4, 6). It is not
  certified, and the max over all 486 rows of the closed LP is not computed.** Margin to 1: ≈ 8, not ≈ 10.
- The level-1 value 0.103 (E2, exact inputs, side 4) is subject to the same two corrections. Its closed-input value is
  unmeasured. "Does not grow beyond ×1.7" compares two equally truncated numbers.

**K_ρ ~ 2.1-2.6: does the induction need K_ρ < 1? No (checked).**
- In NAH-unif the branch U_{j-1}(U_j) depends on U_j only (BR1 is a functional of the coarse field). ρ(U_j, U_{j+1}) is
  needed only for membership of 𝔅_j(ε), with ε := (1 + K̄_ρ + θ)ε_unif. So K̄_ρ < ∞ suffices.
- **Slip (fix S21-6):** η_* contains θ/C_θ^{(i)} but not θ/C_θ^{ρ,(i)}, and the ρ bound "(K̄_ρ + θ + C_θη)η" uses the
  wrong C. Add θ/C_θ^{ρ,(i)} and CURV1's extra ρ-threshold 1/(636p_L𝔠_∞) to η_*.
- Also: K_ρ's size is κ-driven (D1: 4.70 at κ = 0.25, 0.65 at κ = 16), and K_ρ → 0 in the smooth limit (P). So it is not
  a structural danger. Not an obstruction.

---

# PART 3: the S21 lemmas

## Lemma CURV-lin (l.5933-5956): CONFIRMED

- (i): U0 (i)-(ii) at first order give QJ = 1 and dJ = ιd_1, and the soft gradient vanishes at the lift. The linearised BR1
  equation gives x = -C^0d^*ιF_V. Invariance under the slice, the fixing and coarse gauge holds: ddλ = 0, QD_0λ = 0 when λ
  vanishes at the centres, and JD_0Λ = dΛ̂.
- (ii): X ≥ B^*B gives 0 ≤ BX^{-1}B^* ≤ 1, and QC^0d^* factorises with norms ≤ κ^{-1/2}·1. ||ι||² = L^{d-2} is right.
  c37 A3 confirms 0 ≤ dCd^* ≤ 1.
- (iii): the reduction to the scalar ⊗ 1 also holds for the exact-input norm. Project onto a unit direction e: ⟨e, F⟩ is a
  scalar exact input with |·| ≤ 1.
- The heuristic "‖F_1‖_2² ≈ L^{d-4}‖F_V‖_2²" is consistent with diagnostic P (F/L² on L^d·L^{-2}·… plaquettes) and is
  correctly labelled heuristic.

## Lemma CURV1 (l.5957-6019): CONFIRMED-WITH-FIX (level 0)

Step by step:
- (1) The fixed-point identity A* = -C_0(g + R_2) is right (C_0Π_0O_0 = 1 on ker h_0; ||R_2|| ≤ ½C_♭r²).
- (2) The BCH constant: (e^t - 1 - t)/t² ≤ 0.544 at t = ¼, and |W|²/(2(1 - |W|)) ≤ 0.90t² with |W| ≤ 1.136t, total 1.45.
  The four applications with s ≤ 1/80 are covered by "53". The Ad-error 4·9α·r = 36αr is right, and so is 1296𝔠_∞ℓ_θ.
- **(3) The constants slip (fix S21-3).** "|e_g(b)| ≤ 12ε_V for every b": |g(b)| ≤ 6·1.2ε_V = 7.2ε_V and |d^*ιF^G| ≤ 6ε_V, so
  |e_g| ≤ 13.2ε_V. Replace 12 by 14. Then 48c_Kτ becomes 56c_Kτ and D_g's condition 96c_Kτ becomes 104c_Kτ. This is
  constants only.
- (4) Π_{U^(0)} = Π is right (interior links are 1). The LOC application with the collar is consistent with fix LOC-1.
  The near/far split 24ε[…] is right (4 entries of d × |d^*ιF| ≤ 6ε).
- (5) Bianchi: 54αε from six transports of ≤ 3 links. The BCH part is ≤ 5·1.45·36ε² ≈ 261ε², so 2880 is generous. Correct.
- (6) The assembly sums are re-derived. The linear parts are 96c_Kτ + 6t_Z + 24A_out n e^{-m_1D_L/2} (104 after the slip),
  and the ε² coefficients match C_θ.
- **Representative/dual wording (fix S21-2b).** l.5960-5961 must read "min_Z K_p(Z) per row equals the sup-norm of the
  row on **closed** inputs (d_2F = 0), harmonic forms included on a torus". C2/E2's exact-input LP is a lower bound for it,
  not the value.
- **Z tails (stated as "what it is not"; keep).**
  - C_θ contains N_0(|Z|), so Z itself must be summable, not only k - d_2^Tz.
  - A torus LP dual gives a torus Z. A ℤ⁴ representative needs truncation, with its error added to K_p(Z).
  - Certification route: take finite-support Z_p for the 486 reference rows (from translation-averaged torus duals),
    truncate to a ball, and bound K_p(Z) = max_pΣ_P|𝒦(p, P) - (Zd_2)(p, P)| *primally*. Any finite-support Z gives a
    rigorous upper bound, and no duality is needed. This also needs a rigorous enclosure of 𝒦 (computer-assisted ℓ¹ bound
    on C^0 with an explicit decay rate ≈ 0.4, interval arithmetic, float64 or better).
- **Scope.** Level 0 only (U0 (iv) is Wilson-specific), real V only. Thresholds: ε_θ ≲ 1/(80(48𝔠_∞ + 1)) ≈ 10⁻⁴⁰ and θ/C_θ
  with C_θ ∋ 288𝔠_∞³C_♭ (≈ 10¹¹⁴C_♭). These are astronomical, but level-independent only under (H-C). Correctly stated.
- Status PROVEN-HERE (uncounted, strengthens BR1 (iii)): accepted after fix S21-3.

## Lemma E3 (l.6020-6035): CONFIRMED

- The identity: Hess_BE^br = ζ^TF_zzζ uses F_aaa' = -F_aB. Its δB-derivative is ζ^TD³F[ζδB]ζ + 2δζ^TF_zzζ, and the
  A-component of F_zzζ vanishes, so the second term is 0. Gauge freedom in a' does not matter. This is exact.
- The Lipschitz corollary C_♭^{(i+1)} ≤ Z_colZ_row²C_♭^{(i)} + (1 + Z_col)(1 + Z_row)²C_soft is right as an
  absolute-value N_0 bound (N_0(ζ^T) ≤ 1 + Z_col, N_0(ζ) ≤ 1 + Z_row, |w|_∞ ≤ Z_row|δV|_∞; E_i depends on A only).
- Its replacement of NAH-ind's 𝔠_∞³ form (≈ 10¹¹⁴ → 1.3·10³) is a genuine improvement.
- Note: Z_row and Z_col are measured in BR1's slice. The gauge freedom a' → a' + D_0λ could lower Z_col somewhat, but not
  below the 27 crossing links of J. So the product stays ≫ 1.

## Proposition NAH-unif (l.6036-6072): the induction algebra is CONFIRMED; as an implication, GAP

- **Algebra: correct.** (K̄ + θ)c + C_θc² ≤ (K̄ + 2θ)η = η for c ≤ η ≤ θ/C_θ. Only the curvature is fed down, so ρ enters
  once. ε_unif is depth-independent given the hypotheses.
- **GAP 1: CURV1 at level i ≥ 1 is not implied by the listed ingredients** (l.6050-6052).
  - Step (3) uses U0 (iv): the gradient of the Wilson action at the lift comes from corner plaquettes only, with
    |g| ≤ 6ε_V and g = d^*ιF + O(αε + ε³).
  - At level i ≥ 1 the "fine" functional is E_i^br + soft, a non-local functional (H_i not finite range, fix 7). Its
    gradient at the lift is H_iJa + (second order), where a is a potential of F^G that is small only inside the AX box.
  - Controlling the far contributions needs (α) gauge invariance of E_i^br plus a localisation of ∇E_i^br (exponential decay
    of its dependence, with Lemma-LOC-type constants for the *gradient*, not the Hessian entries), and (β) a second-order
    Taylor bound of ∇E_i^br in the AX gauge (C_♭^{(i)} and the decay of D²E_i^br).
  - (I_i) (b) gives region bounds for the entries of Õ_i only. Name **(H-G)**: *at every level i, ∇E_i^br at the lift of any
    V in the class satisfies g_i = H_iJa + e_{g,i}, with e_{g,i} obeying step (3)'s near/far bounds with level-uniform
    constants*. It is ⊂ (BG-unif); measurable at trivial background (the linear part is E's 𝒜_i), OPEN.
  - Note also that the linear kernel at level i is d(J - C^{(i)}H_iJ) acting on potentials. Its representative form on
    closed inputs needs the same Z-construction at level i.
- **GAP 2: the complex neighbourhood.**
  - N5-sf_j and NAH1 (a) use V in a complex neighbourhood (radius α_*/8 in 𝔅_i). CURV1 is proven for real V.
  - The tower's complex extension must have a level-uniform radius. Otherwise holomorphy (I_i) (c) degrades per level, and
    the complex displacement is bounded only through 12𝔠_∞, i.e. the old displacement loss.
  - Add it to the hypotheses (it is (BG-unif) (ii)), or prove CURV1 for complex V with the imaginary part tracked as a
    curvature.
- **Small tori.** "T_j ≥ the level-j sizes" excludes the top ≈ log_L ℓ_θ levels of an L^K torus. This is correctly listed
  under "Still needed".
- Verdict: **a correct implication from (H-K), (H-C), (H-G), and the complex-radius clause.** As stated, with two
  hypotheses, it is GAP. Uncounted either way.

## (H-C) and the failure mode CURV-F2: genuinely hard, or a norm artefact? **Mostly a norm artefact. Its cure is (BG-unif)-scale.**

- **Why the true quantity should be level-uniform.**
  - E_i^br is the classical branch action, i.e. tree level: the minimum of the fine action at fixed coarse field.
  - For smooth V it is ≈ the coarse Wilson-type action plus irrelevant corrections. Classical d = 4 YM is scale invariant:
    a smooth fine field has curvature F/L² on L⁴ fine plaquettes per block-plane, and potential ~v/L per fine link. So
    the pulled-back cubic vertex ⟨dA, [A∧A]⟩ sums to L⁴·(F/L²)(v/L)² = O(Fv²), the coarse vertex in own units.
  - The measured pieces agree: K_p → 1/L² in the smooth limit (P), and the trivial-background gap is flat from level 0 to
    level 1 (c36 D, 0.9966).
- **Why the absolute-value recursion cannot see it.** N_0(ζ^T) ≥ Z_col ≥ 27 counts the full lift on every crossing link
  at sup size, and Z_row² does so twice more. The signed sum over the 27 crossing links, and the differentiated leg
  (d(ζδV) = 𝒦-sized), are discarded. This is the same mechanism as K_p(0) = 2.27 against K_p^♯ ≈ 0.12. So 1.3·10³ is a
  bound artefact, not a property of E_i^br.
- **But no per-level Lipschitz recursion in a sup-type norm closes.** Even with a sharp signed per-level factor κ_3 ≈ 1, a
  recursion C^{(i+1)} ≤ κ_3C^{(i)} + c compounds unless κ_3 < 1 strictly, and marginality means κ_3 ≈ 1, not < 1. So a
  "curvature-adapted Lipschitz recursion" is unlikely to be enough on its own.
- **Recommended norm.** Analytic (Cauchy) bounds: |E_i^br(V) - S_i^{loc}(V)| ≤ C uniformly on a level-uniform complex
  polydisc defined in curvature-adapted coordinates. The polydisc is {V : own-units |log V_P| ≤ ε, AX-gauge links ≤ ℓε on
  boxes, |Im| ≤ r}, and S_i^{loc} is an explicit local (Wilson-type) action. All derivatives, including C_♭^{(i)}, then
  follow by Cauchy estimates with level-independent constants. This is (BG-unif) (ii)/(iv), by the composite contraction
  of the anti-circularity clause: Balaban's route.
- **Measurable step first (c38, criteria first).** At the trivial background E3 gives D³E_1^br(1) = ζ^TD³F(1)[ζ·]ζ
  *exactly*, with ζ = (κC^0Q^T, 1): a computable translation-invariant trilinear kernel (Bloch, two momenta). Pre-register:
  - (i) its signed N_0-type norm against that of D³S_W(1) on the coarse lattice (prediction ≈ 1, not 10³);
  - (ii) the closed-input analogue (one leg through d).
  If (i) ≈ 1, (H-C) is shown to be a norm artefact. The proof still needs the analytic norm above.
- **Verdict:** (H-C) is not a real obstruction to uniformity (a norm artefact, with high confidence on physical grounds;
  measured support only indirect). It is genuinely hard to *prove*, at (BG-unif) scale, and not at the per-level scale.

## The (H-K) certification path: VIABLE, with corrected targets

- Target: K_p(Z) ≤ ~0.2 (true ≈ 0.12) at level 0 for a finite-support Z, then levels i ≥ 1 (or level-uniformly, via the
  smooth limit plus decay).
- Steps:
  1. Closed-input LP duals on T = 6, 8 for all 486 rows (reduce by the cubic symmetry first).
  2. Translation-average and truncate Z; bound K_p(Z) primally on ℤ⁴.
  3. A rigorous ℓ¹ enclosure of 𝒦 via a truncated approximate inverse of Õ_0 with a Neumann residual in N_m (m ≈ 0.4),
     in interval arithmetic.
- This is finite-dimensional, computer-assisted work (harder than c36 C, but the same kind).
- The margin ≈ 8 is comfortable. The level-uniform statement (H-K) for all i is *not* reached this way; it needs (BG-unif)
  or a level-i computation at each level. Note: if (BG-unif) is proven, (H-K) is not needed at all.

---

# PART 4: re-run record

- A, B, D, E: identical to the stored outputs (timing aside). Peaks 563-590 MB; load1 2.5-4.0; free memory 36-45%.
- Diagnostic P: 2 s. Diagnostic T: T = 4 and 6 done. I stopped the T = 8 LP after 33 min with no row finished. The
  runner then released the lock with its single rmdir (verified).
- c37 C was not re-run: it was the last job in the queue, and I cancelled it with the T = 8 LP rather than hold the
  machine-wide lock for a further 13 min. Its stored output was audited line by line instead.
  C2's row 482 value 0.08218 is independently reproduced by my diagnostic T, with the same LP and the same kernel.

---

# Overclaims

1. **PROOF l.16-17, 6056-6059, 6083-6087; header l.31-33 (fix-8 text); LOG l.960-962; RTARGET §47.** "K_p^♯ ≈ 0.06-0.08
   (level 0), 0.10 (level 1)", "margin ≈ 10", "below … 1/L² = 0.11". These are small-torus, exact-input values. The CURV1
   quantity (closed inputs) is ≈ 0.11-0.13 and ≥ 1/9 in the limit.
2. **PROOF l.5960-5961.** "min_Z K_p(Z) … is the exact sup-norm of the row on exact inputs": false on a torus (closed ≠
   exact).
3. **PROOF l.6050-6052.** "Lemma CURV1 at level i ≥ 1 is part of the implication; its proof uses only …": it also needs
   (H-G) and the complex radius.
4. **PROOF l.6069-6072, LOG.** The "(1 + Z_col)max(1, Z_row)²" printed by D2 is not E3's coefficient (cosmetic).
5. **LOG "FOR RLARGE v2" item 1.** Already done in RLARGE v2.

# Tally

**72 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path) + 1 comparison
branch: as claimed, unchanged.**
- CURV-lin: CONFIRMED.
- CURV1: CONFIRMED-WITH-FIX (level 0).
- E3: CONFIRMED.
- NAH-unif: GAP as stated (uncounted).
- No count changes. N5 stays OPEN.

# Required fixes (binding for the next session)

1. **S21-1:** split NAH1's ε-dependence. (a) Gap/N5-sf1 with ρ, D frozen at ε_H on T_2 ≥ T_0^(1)(ε_H) for all ε ≤ ε_H.
   (b) δ_H = O(ε log 1/ε) on T_2 ≥ T_0^(1)(ε).
2. **S21-2:** correct every K_p^♯ quotation.
   - (a) Record: exact-input LP values grow with T (row 252: 0.062 at T = 4, 0.090 at T = 6); the smooth limit gives
     ≥ 1/9 (REVIEW_S21 P).
   - (b) The CURV1 constant is the closed-input dual: ≈ 0.120/0.124 (row 252) and 0.114/0.115 (row 482) at T = 4/6.
   - (c) Withdraw "below 1/L²" and "margin ≈ 10". Write "≈ 0.11-0.13, margin ≈ 8, measured on two rows, not certified".
   - (d) Fix l.5960-5961 to "closed inputs".
   - (e) Level-1 0.103 is exact-input, side 4: requalify it.
3. **S21-3:** CURV1 step (3): |e_g| ≤ 14ε_V (not 12). Propagate 96 → 104 in D_g.
4. **S21-4:** the D2 coefficient: quote E3's (1 + Z_col)(1 + Z_row)² ≈ 2.3·10³.
5. **S21-5:** NAH-unif: add (H-G) (level-i localised gradient expansion at the lift) and the level-uniform complex radius
   (or CURV1 for complex V). Restate it as an implication from (H-K), (H-C), (H-G) and (H-ℂ).
6. **S21-6:** η_* must include θ/C_θ^{ρ,(i)} and 1/(636p_L𝔠_∞^{(i)}). The ρ bound uses C_θ^ρ.
7. **S21-7:** LOG "FOR RLARGE v2" item 1 is already applied (RLARGE [v2-C]). RLARGE row 3a's "not precisely stated" is
   stale after fix 12. Both are for the next RLARGE pass.
8. **Recommended next.**
   - c38 (criteria first): D³E_1^br(1) by E3, signed, against D³S_W(1) (the (H-C) artefact test).
   - Closed-input LP for all rows at T = 6, 8 (symmetry-reduced), and at level 1.
   - Then the (H-K) certification path above. Then (BG-unif) by the composite contraction, as the only route that
     discharges (H-C), (H-G) and the complex radius together.
