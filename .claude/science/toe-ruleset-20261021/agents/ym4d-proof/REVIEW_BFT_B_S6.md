# REVIEW_BFT_B_S6: hostile review of BFT lane B session 6 (BFT_B.md [RBB5-fix] edits, §18-§20; checks bb6, bb6m, bb6n)

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md or the checks. This is the only file I edited. No
commits, PRs or pushes.

Inputs (read 2026-10-28 ≈09:37-09:55 UTC). `TZ=UTC stat`: BFT_B.md born 09:21:46, modified 09:35:12, 313159 bytes;
BFT_B_LOG.md modified 09:35:32, 32864 bytes (both unchanged during the review). checks/: bb6_criteria.md born 09:23:17, modified
09:25:02; bb6m_criteria.md and bb6n_criteria.md born = modified 09:23:17; bb6m_mask.py 09:25:33; bb6_transport.py 09:26:41;
bb6n_nf.py born 09:27:26, modified 09:27:59; outputs 09:28:23-09:29:14. BFT_A.md modified 09:33:01 (lane A active; read only).
- BFT_B.md: §18-§20 and the session-6 FOR OTHER FILES (l.2446-2816) in full; every [RBB5-fix] tag in context (22 tag strings:
  20 Step-1 tags at l.1688-2425, plus the mentions at l.2448 and l.2644); §12.2 (CovLift) and GI-cov / BB-gi_k / GI-off
  (l.1636-1675, 13.7-13.8, l.1869-1900); §15.0 N_res and §15.1 EP-rec / EP-lin / EP-LRL(b) (l.2026-2075); 16.8 (l.2262-2270).
- BFT_B_LOG.md: session 6 in full (l.258-315).
- REVIEW_BFT_B_S5.md (all; format, fixes, mask verdict).
- BFT_A.md: §7.1-§7.2 (Setting LIN, norms), §8.2 BL-2, §8.6 BL-5, §12.0, LRL (b) (l.1338-1356), §23.8 (lane A's own "Lemma
  RH"), §26.0-§26.2 (Lemma FG, Proposition/Corollary NC, the non-co-closed BCH₂ remainder), §27 [RBA5-fix] U7.
- checks/bb6_criteria.md, bb6m_criteria.md, bb6n_criteria.md; bb6_transport.py and bb6n_nf.py line by line; all three outputs.

Re-run: bb6m, bb6, bb6n under the numeric lock, plus one reviewer probe ((N1-G) on 4D tori). Record at the end.

---

## Bottom line

- **Provenance: CONSISTENT.**
  - §18 as it stands (l.2446-2565, including the "# Session 6" header) is **12505 bytes = 281066 − 268561**, exactly the
    growth logged at 09:20:07. So §18 has not changed since its append.
  - l.1-2565 total 285414 bytes against 285413 logged after Step 1 (the 1-byte line boundary, as in S5). Nothing before §19
    changed after Step 1.
  - Order: §18 (09:20:07) < Step 1 (09:22:01) < criteria (09:23:17) < A5 replaced (09:25:02) < scripts (09:25:33-09:27:59) <
    runs (09:28:23-09:29:14) < §19-§20 (09:34:46) < one 19.4 correction (09:35:12). This matches the log.
  - The A5 replacement predates bb6_transport.py and is disclosed, with a correct reason: a non-co-closed j_1 pairs with
    composite gauge directions, so E_src has no critical point. The criteria's "[edited 09:2x …]" should give the exact
    time, 09:25:02 (cosmetic).
  - Forward references: the two RS5-10 tags that name checks/bb6m before it existed are disclosed ("planned at the time of
    this tag"). I found no undisclosed one.
  - The 09:35:12 in-place correction in 19.4 (the BCH₂-row size) is in the log but not marked in the text (cosmetic RS6-9).
- **[RBB5-fix] edits: all ten applied, correctly** (Part A).
- **Lemma RT: CONFIRMED.** **Lemma TC: CONFIRMED.** **Theorem RH: CONFIRMED.** It is short, correct, and needs no elliptic
  step. The claim "carry-down gains L^{-2} per level, the inverse estimate loses L^{1+α}" is right. So is "d = 4": in d dimensions
  the gain is L^{-(d-2)}.
- **Theorem RH_m: CONFIRMED** (c_w = 12; 10 for the data map). **Corollary RH-D: CONFIRMED.**
- **Corollary RH-inv: CONFIRMED-WITH-FIX (scope).** It holds for every *level-wise co-closed* Setting-LIN class: (G), (R),
  commutator rows (residual type by lane A's CR-1), BA-6's residual part, (P0), (Pl-c), rough currents, and **co-closed** BCH₂
  rows.
  - It does **not** hold for lane A's non-co-closed BCH₂ remainder V_l (BFT_A §26.2): Lemma RT (a) uses d*j_l = 0 at every
    level. "Every source class of 𝒴^∇" must be narrowed (RS6-1).
  - The α = θ example is **CONFIRMED**.
- **Corollary LRL(b)-E: CONFIRMED for T ≥ 5.** Excluding T = 3, 4 is **harmless**, and a periodic lift removes the gap
  (C.4, RS6-3).
- **Nonabelian (CovLift):**
  - **Lemma NF-crit, Lemma NF-uniq, Lemma NF-cov: CONFIRMED.** NF-uniq's n-independence (the δ/n sup bound against the n
    Poincaré factor) is verified.
  - **Lemma REF / (N1-bd): CONFIRMED given (N1-G).**
  - **(N1-G) is TRUE with the sharp constant C_G = ¼, by an elementary argument** (Part D.4). I checked it numerically:
    Σ|∇G_M| = M/4 to all printed digits, for M = 8 to 64. So **(N1-G) can be PROVEN on the framework** without lane A's
    pointwise BA-7 import.
  - **Theorem NF-ex: CONFIRMED** (with its post-proof hypothesis). **Proposition KΠ: CONFIRMED** on its stated domain.
  - **Lemma GC-lin: CONFIRMED. Proposition AX-cov: CONFIRMED.** I re-derived the face-link linearisation signs.
  - **Theorem CovLift-KΠ (i)-(iii): CONFIRMED-WITH-FIX, given (N2-0).**
    - (a) Covariance holds only for **small gauges**: neighbouring root values within O(ε), i.e. V and V^h both in
      𝒞_glob(ε). (CovLift) (i) is quantified over every level-k gauge.
    - (b) **CL-F4 OCCURS off 𝒞_glob.** On GI-off's class (small plaquettes, large coarse links), the corner points g_X(U)(z)
      differ by coarse transports, so the Karcher gluing is undefined (D.7).
    - (c) (N2-0) must be stated at every level, with its quantifiers (RS6-5).
  - Walls: (N1-int) is routine; (N2-0)/(N2-bd) is tractable (I sketch why the axial frame gives geometrically decaying BCH
    defects); C_g at θ > 0 is **not precisely stated** and is a design question (Part E).
- **bb6m, bb6, bb6n: CONFIRMED; the re-runs are byte-identical** (timing strings excluded).
  - bb6m reproduces REVIEW_BFT_B_S5 Part D exactly.
  - bb6n's inputs lie outside NF-ex's hypotheses (ε_f = 2.02), so it illustrates rather than tests the theorem.

---

# PART A: the [RBB5-fix] edits

All binding and cosmetic fixes of REVIEW_BFT_B_S5 are applied in place, with the content I asked for:
- RS5-1: GI-F2 text at l.1688, l.1848 and the §14 row l.1973 now reads "cannot occur for any lift orbit-covariant at level 0
  (Lemma CL-uniq); the cocycle is automatic".
- RS5-2: l.2220 now reads ⟨πy, w⟩.
- RS5-3: T ≥ 5 and N_res,m, at l.2071, l.2268 and l.2416. N_res,m is defined in §18.0 (l.2459-2461) as asked.
- RS5-4: (a) l.2247; (b) inside l.2071; (c) l.2208.
- RS5-5: l.2421.
- RS5-6: l.2289, l.2291. I checked BB-mix_k's ε_mix,k (l.1149-1150): every entry is k-uniform under the hypotheses, so
  writing ε_mix is correct.
- RS5-7: l.2319. RS5-8: l.2303. RS5-9: l.1931 plus the log. RS5-10: l.2354, l.2421, l.2424, l.2425.
- One leftover: the §17 table row l.2421 keeps "mask regularity measured (bb5), not proven" ahead of its own [RBB5-fix]
  tag. Strike the old clause (cosmetic RS6-9).

---

# PART B: (Res-Hölder) (§18.1; §19.1-§19.7)

## B.1 Lemma RT (l.2486; proof l.2576-2587): CONFIRMED
- **Euler-Lagrange.** With E_src of BFT_A §7.1:
  ∂E/∂x_l = Q_l^T(κ_lr_l − s_l) − (κ_{l−1}r_{l−1} − s_{l−1}) − d*G_l − j_l.
  This gives ρ_{l−1} = Q_l^Tρ_l − d*G_l − j_l. The level-0 equation is d*dx_0 + Q_0^Tρ_0 − d*G_0 − j_0 = 0. bb6's normal
  equations (b0, b1 and Hmv) are exactly these; I checked them term by term.
- **(a) Co-closedness.**
  - Q_ld = d ev transposes to d*Q_l^T = ev^Td*.
  - d* of the level-0 equation gives ev^T d*ρ_0 = 0. This uses d*d* = 0 on the 2-form dx_0 and on G_0, and d*j_0 = 0.
  - ev^T is injective (it places level-1 values on distinct level-0 sites), so d*ρ_0 = 0.
  - Induction gives the rest, using d*j_l = 0 at **every** level. Setting LIN (BFT_A l.451) assumes exactly this.
- **(b)** Q^T = Q_str^T − h^Td* (BL-2 (c)), so Q^Tρ = Q_str^Tρ on co-closed ρ.
- **(c)** Iteration. Each source d*G_l + j_l is co-closed, and co-closedness is preserved by Q^T, so every composite
  transpose is the straight one (IT-str). Then r_i = (ρ_i + s_i)/κ_i.
- **s_i need not be co-closed** (the r_l are composite-gauge invariant), so a checkerboard s is legitimate (used in B.4).
- **Prior art.** The transport inequality already appears in lane A (BFT_A §18.4 Step 1 and BL-5; quoted in §23.8). Lane B's
  FOR OTHER FILES says so (l.2810). Lemma RT adds the exact identity with every co-closed source class.
- **Scope.** RT fails as soon as one level-l plain source has d*j_l ≠ 0, even if the whole source is composite-co-closed
  (Ξ^TS = 0, BFT_A §26.0). Then ev^Td*ρ_0 = d*j_0 ≠ 0, and the funnel terms h^Td*ρ_l appear (bb6 A5: of size 0.87·max|v|).
  This matters for RH-inv (B.4).

## B.2 Lemma TC (l.2490; proof l.2589-2596): CONFIRMED
- **Sup.** BL-2 (c): (Q_str^Tj)(b) = L^{-4}Σ_{i<L}j(X(b − ie_μ)). That is L^{-3}||j|| in own units, for any j (co-closedness
  is not needed for the size).
  - Composite: L^{-3m}.
  - Level-(i+1) 1-form coarse units multiply by L^m. Net: **L^{-2m}**.
  - For a level-l current: L^{-3(l−1−i)}·L^{-3(k−l)}π_l = L^{-3m}π_l. Correct.
- **d*G.** A link lies in 2(d − 1) = 6 plaquettes, so π_l(d*G_l) ≤ 6L^{k−l}||G^c_l||. Correct.
- **Inverse estimate.** On the level-(i+1) lattice (spacing ρ = L^{-m}):
  - ||∇^cH^c|| ≤ 2L^m||H^c||;
  - Campanato [∇^cH^c]_α ≤ ρ^{-α}||∇^cH^c||, since Osc_2 ≤ sup and boxes have side ≥ ρ;
  - so ||H||_{C^{1,α}} ≤ (1 + 2L^m + 2L^{(1+α)m})||H^c|| ≤ 5L^{(1+α)m}||H^c||;
  - pointwise, [·]^∞_α ≤ 2ρ^{-α}sup, which gives 7.
  - All correct.

## B.3 Theorem RH (l.2494; proof l.2598-2610): CONFIRMED. "No elliptic step is needed" is correct
**The three geometric sums (m = k − 1 − i ≥ 1).**
- s-term:
  - ||s||_R = max_lω^R_lL^{k−1−l}||s^c_l|| (BFT_A l.462), so ||s^c_i|| ≤ L^{-θ(m+1)}L^{-m}||s||_R.
  - Times 5L^{(1+α)m}/κ_- this is (5/κ_-)L^{-θ}L^{(α−θ)m}. The sum over m ≥ 1 is 1/(L^{θ−α} − 1).
- Top term: (5/κ_-)L^{-(1−α)m}||ρ_{k−1}||, summing to 1/(L^{1−α} − 1).
- Level-l sources: they enter r_i iff i + 1 ≤ l, i.e. m ≥ k − l. Σ_{m≥k−l}L^{-(1−α)m} = L^{-(1−α)(k−l)}/(1 − L^{-(1−α)}).
- All three match the displayed bound (l.2495-2496). Nothing depends on T.

**Units cross-check.** N_res uses r_i in level-(i+1) coarse 1-form units with no extra weight (§15.0 l.2026). ||x||_inv carries
L^{k−1−j}||r^c_j||. The top component (j = k − 1) has factor 1, so ||r^c_{k−1}|| ≤ ||x||_inv as used.
- Note: ||x||_inv alone gives only ||r^c_i|| ≤ L^{-m}||x||_inv. After the inverse estimate that is L^{αm}, which is **not**
  summable.
- So the content of Theorem RH is exactly the extra L^{-m} from criticality (transport). That is also why B5' (a
  non-critical configuration) is no counterexample.

**Remark.** (Res-Hölder) was carried as a wall for two sessions. It falls to a transport identity plus an inverse estimate.
The proof is a few lines and I find no gap. The B5' obstruction (BFT_A l.1344-1346) concerns general configurations, not
critical points. Consistent.

**Cosmetic.**
- Lane A already has a **"Lemma RH"** (BFT_A §23.8, residual Hölder of the curvature-side composite R_j). Rename lane B's
  Theorem RH (for example Theorem RHT, "residual Hölder by transport") before any cross-file citation (RS6-8).

## B.4 Corollary RH-inv (l.2500; proof l.2612-2625): CONFIRMED-WITH-FIX
**Term-by-term bounds: correct.**
- (G): 6L^{(α−θ)(k−l)}||G||_Y.
- (Pl-c): L^{-θ(k−l)}||j||_{Pc}.
- Rough currents: L^{-(1−α)(k−l)}π_l(w) = ω_l^{-1}N_l(w), with N_l from BFT_A l.894.
- (P0) does not enter the formula for r_i (it enters only through ||r_{k−1}||, which is bounded by ||x||_inv). Correct.
- Commutator rows are not listed, but they are exactly residual type (lane A CR-1, ||s^C||_R ≤ κ_+L^θη²). Add them to the
  list.
- BCH₂ size:
  - the residual scaling of ||x||_𝔐 gives own |r_l| ≤ L^{-2(k−1−l)}η and |x_l| ≤ L^{-(k−l)}η;
  - so π_l ≤ 2C_B'κ_+L²η², uniform in l;
  - this is consistent in order with lane A's Corollary NC (ω_l||W^c_l|| ≤ CL^{-(1−θ)(k−l)}η², so π_l(d*W_l) = O(η²)).

**Scope error (binding, RS6-1).** l.2615-2616 apply Theorem RH to "the BCH₂ rows R^B_l" as plain currents.
- R^B_l is **not** co-closed in general. Lane A splits it as R^B_l = d*W_l + V_l: a co-closed completion in the (G) slot,
  plus a remainder V_l with d*V_l = d*R^B_l (BFT_A §26.2, Proposition NC).
- Lemma RT (a) fails for V_l. With only composite co-closedness, d*ρ_0 = (ev^T)^{-1}d*j_0-type terms appear, and the funnel
  terms −h_l^Td*ρ_l are O(1) (bb6 A5: 0.87). Without even that, there is no critical point.
- Read instead:
  - "co-closed BCH₂ rows (lane A's scope, [RBA5-fix] U7), and the co-closed completions d*W_l as (G)-slot sources";
  - "the non-co-closed remainder V_l is outside Setting LIN; Lemma RT does not apply to it; (Res-Hölder) for its responses is
    part of lane A's (NC-Γ) target, OPEN";
  - in the statement (l.2500), "every source class of 𝒴^∇" becomes "every level-wise co-closed Setting-LIN source class".

**Lever (reviewer, ARGUED).** Lemma RT extends to composite-co-closed sources.
- d*ρ_l is then determined explicitly by the d*j_{l'} (l' ≤ l), through the injectivity of ev^T.
- The funnel term h_l^Td*ρ_l becomes one more explicit level-l plain source, of own size ≤ 2(L − 1)|d*ρ_l|.
- So Theorem RH would carry over with π_l replaced by π_l + C·(coarse size of d*ρ_l). For local rows, d*ρ_l is of the order
  of π_l.
- This is the natural route to (Res-Hölder) for V_l (RS6-1 (b)).

**The α = θ example (l.2620-2625): CONFIRMED.**
- On level-(i+1) sites (T even, L odd: the side TL^m is even), s^c_i = a_i(−1)^{Σz}e_μ has coarse gradient ±2L^ma_i.
- On a box of own side 2 (coarse side 2ρ), Osc_2 = 2L^ma_i, so [∇^cs^c_i]_α ≥ 2^{1−α}L^{(1+α)m}a_i = 2^{1−α}L^{-θ}L^{(α−θ)m}.
- At α = θ this is L-uniform per level. The other terms decay like L^{-(1−α)m}. The bound ||x||_inv ≤ G_R||s||_R is BL-5 (a),
  valid for α ≤ θ (BFT_A l.666), so it is legitimate at α = θ.
- Hence N_res ≥ c(k − m_0) while N^max_res stays bounded. RH-F2 occurs exactly at α = θ.
- This is lane A's BL-5 (c) mechanism transposed to residual gradients. Lane A's χ was co-closed; lane B's is not, which is
  harmless for a residual source.

**Consequence.** (H-inv+) ⟺ (H-inv) for α < θ, and (W-lin-Π) for S_E ⇐ (H-inv) alone, with G_Π = C_rec((1 + C_1)G + C_2).
Correct within the co-closed scope.

## B.5 Corollary RH-D (l.2505; l.2627-2629): CONFIRMED
5κ̂/(3^{3/4} − 1) = 3.91κ̂ (I get 3.906). ||r_{k−1}|| ≤ 4C_R||B_k||_D is cited from LINEAR_PACKAGE Theorem 3.8 / N2-lin; the
citation is consistent with the S5-era usage.

## B.6 Theorem RH_m (l.2507; proof l.2631-2641): CONFIRMED (c_w = 12; 10 for the data map)
- The transported sup reads within ℓ¹ distance ≤ 5 coarse: crude, but enough.
- Weighted differences: a factor 1 + e^m ≤ 2e^m. The weighted Campanato term over boxes of side ≤ 1 (ℓ¹ diameter ≤ 4) gives
  e^{4m}. So the inverse estimate costs 5e^{5m}L^{(1+α)m}.
- d*G reads within 2, adding e^{2m}.
- Totals: e^{10m} for the top and plain terms, e^{12m} for the G-terms, e^{5m} for the s-terms. The correction from 8 to 12
  is right.
- For the data map: ||r_{k−1}||_{∞,m} ≤ G_D(m)||B_k||_{D,m} by Proposition W (the j = k − 1 residual component of
  ||y||_{inv,m}). Correct. **(Res-Hölder)_m for the data map: CONFIRMED.**
- Cosmetic (RS6-8): in 19.6, m denotes both the weight and the depth k − 1 − i (as in "e^{5m}L^{(1+α)m}"). Rename the depth
  t.

## B.7 Corollary LRL(b)-E (l.2510; l.2643-2648): CONFIRMED for T ≥ 5; T = 3, 4 HARMLESS and closable (RS6-3)
- The chain is EP-LRL(b) (CONFIRMED-WITH-FIX in S5, fix applied) + RH_m. The constant C_b is as displayed.
- At m = 0 no reach statement is used. Correct.
- **Is excluding T = 3, 4 harmless?** Yes, for two reasons.
  - (1) Every consumer in lane B uses local tori of side ≥ T^Π_W = 4R + 22 ≥ 86 (R ≥ 16). In lane A, LRL (b) feeds only the
    gradient half of (G♯_0-field^∇), on the same local or global tori.
  - (2) The gap closes by a **periodic lift**, the device lane A itself uses for T ≤ 2 (BFT_A l.2458). For T ∈ {3, 4} put
    T' := 2T ∈ {6, 8} and P_♯^{(T)} := descend ∘ Π_E^{(T')} ∘ lift.
    - Π_E commutes with coarse translations (EP-alg), so it preserves T-periodicity. lift∘descend = 1 on periodic
      configurations, so P_♯^{(T)} is a projection.
    - P_♯x − x is the descent of a periodic composite gauge direction trivial at level k.
    - The lift of the T-minimiser is the T'-minimiser for the lifted data: the gauge-invariant outputs are unique, and the
      Euler-Lagrange equations are local.
    - Weights: d_{T'}(z̃, X̃_0) ≤ d_T(z, X_0) + 4T, so ||lift B||_{D,m} ≤ e^{16m}||B||_{D,m}. On the output side, choose z̃ in the
      fundamental cell nearest X̃_0, so the weight does not grow.
    - Result: C_b(T = 3, 4) ≤ e^{(16+4)m}C_b(T'). ARGUED-routine; write it as a remark.
  - With this remark, LRL (b) holds for **all T ≥ 3** as lane A states it.

---

# PART C: nonabelian normal forms and the Karcher-glued slice (§18.0, §18.2; §19.8-§19.16)

## C.1 Lemma NF-crit (l.2515; l.2650-2656): CONFIRMED
- ad_w is skew for the Ad-invariant inner product, so φ(ad_w)^T = φ(−ad_w).
- φ(−ad_w)w = φ(0)w = w, because ad_ww = 0.
- Hence dΦ/ds = 2Σ⟨w(b), ξ(x) − ξ(y)⟩ = −2Σ⟨ξ, d*w⟩.
- With the constraint ξ(c_X) = 0, the identity Σ_z(d*w)(z) = 0 (each link counted once at each end) gives d*w = 0 also at
  c_X. Correct. This is the standard fact that the Σ|log|² gauge functional's critical condition is the *linear* Neumann
  condition on w = log U^g.

## C.2 Lemma NF-uniq (l.2517; l.2658-2672): CONFIRMED (checked first, as asked)
**The shift.**
- κ = g_2g_1^{-1} and d(κ(x), κ(y)) ≤ 2δ/n by bi-invariance. Paths from c_X have length ≤ 8n (box side 4n + 1), so
  |log κ| ≤ 16δ.
- The fixed-point map ζ ↦ −avg log κ − R(ζ) has R = O(|ζ||log κ|) = O((|ζ| + 16δ)²). It maps {|ζ| ≤ 40δ} into itself and
  contracts for δ small.
- At the fixed point, avg log(e^ζκ) = ζ + avg log κ + R(ζ) = 0. Verified.
- g_2' = ag_2 is critical on the whole group, because U^{ag} = Ad_aU^g and Φ is Ad-invariant.
- ξ := log(g_2'g_1^{-1}) is mean-zero, with |ξ| ≤ 60δ and |dξ| ≤ C·2δ/n (log is Lipschitz near 1).

**Smallness along the curve.** I checked that max|log W_t| ≤ Cδ/n although |ξ| is only O(δ):
- e^{tξ_x}e^{w}e^{−tξ_y} = e^{Ad w}·e^{tξ_x}e^{−tξ_y};
- |log(e^{tξ_x}e^{−tξ_y})| ≤ t|ξ_x − ξ_y| + |[ξ_x, ξ_x − ξ_y]|/2 + … = O(δ/n).

**Convexity.**
- f'(0) = f'(1) = 0.
- D_b is linear in ξ, and |D_b − dξ(b)| ≤ C|w||ξ|. E_b = [ξ_x, dξ(b)] + O(|w||ξ|²).
- Σ_b|w|²|ξ_x|² ≤ (Cδ/n)²·8||ξ||².
- Σ_b|w||ξ_x||dξ_b| ≤ (Cδ/n)√8||ξ||·||dξ||.
- With the Neumann Poincaré inequality ||ξ|| ≤ ((4n + 1)/2)||dξ||, both are ≤ Cδ||dξ||². So **n cancels, and δ_0 = δ_0(N, d)**.
- The Poincaré constant is right: path-graph gap 4sin²(π/2S) ≥ 4/S² (sin x ≥ 2x/π); product graphs have the minimal factor
  gap.
- Then ∫_0^1f'' = 0 gives dξ = 0, so ξ = 0.
- **NF-F1 does not occur: CONFIRMED.**

## C.3 Lemma NF-cov (l.2520; l.2674-2678): CONFIRMED
Φ_{U^h}(g') = Φ_U(g'h). Left-constant invariance makes h(c_X)gh^{-1} critical. It lies in 𝒲_δ(U^h), since
(U^h)^{g'} = Ad_{h(c_X)}U^g. Uniqueness comes from NF-uniq. No smallness of h is used. Correct.

## C.4 Lemma REF and (N1-bd) (l.2523; l.2680-2690): CONFIRMED given (N1-G)
**The reflected form.**
- On the doubled torus 𝕋_R, the reversed-image rule w^R_μ(ϱ_Az) = −w_μ(z − e_μ) (for μ ∈ A) is the correct odd extension:
  ϱ_A(z)_μ + 1 = −z_μ = ϱ_A(z − e_μ)_μ.
- Under the μ-reflection the divergence term w^R_μ(ϱz) − w^R_μ(ϱz − e_μ) equals w_μ(z) − w_μ(z − e_μ). Crossing links carry 0,
  matching the Neumann omission. So d*w^R = 0.
- Mean zero: the μ-components are odd under ϱ_μ, and crossing links carry 0.
- A plaquette straddling a μ-plane has its two μ-links equal to 0 and two equal transverse links, so its curl is 0. Hence
  sup|dw^R| = sup|dw|.

**The bound.**
- w^R = Δ^{-1}d*dw^R (componentwise; harmonic 1-forms are constants, removed by mean zero). Each component involves ≤ 3
  first differences of G_M.
- So sup|w| ≤ 3C_GM sup|dw|. With M = 2(4n + 1) ≤ 10n and coarse units (w^c = nw, (dw)^c = n²dw), C_B = 30C_G suffices. 60C_G
  is fine.
- **NF-F2 does not occur:** the operator d*Δ^{-1} has degree −1, so Σ|∇G| is O(M) with no logarithm. Correct.

## C.5 Theorem NF-ex (l.2527; l.2692-2703): CONFIRMED (with the post-proof hypothesis)
- **A priori bound.** dw = log W(∂p) − B_p, with |B_p| ≤ C_3(max|w|)². In coarse units this gives
  n max|w| ≤ C_B(ε_* + C_3δ·n max|w|), hence ≤ 2C_Bε_*. Correct.
- **Continuation.**
  - Closed: by compactness, and because the a priori bound lands in 𝒲_{δ/2}.
  - Open: the Hessian on {ξ(c_X) = 0}. At a critical point the constants are in the kernel of the (intrinsic) Hessian, so
    H(ξ) = H(ξ − ξ̄) ≥ ||dξ||². The C.2 estimate is a quadratic-form bound, homogeneous in ξ, so no size restriction is
    needed.
  - Correct.
- The added hypothesis max_tε_f(e^{tA}, X) ≤ ε_0 is genuinely needed: sup-smallness n|A| ≤ ε_0 gives only
  n²|dA| ≤ 4nε_0. It is marked.
- **Cosmetic (RS6-9).** §18.2's NF-ex pre-statement contains a dangling "… more precisely". The 𝒟(ε) of KΠ (l.2531) must
  carry both NF-ex hypotheses. 19.13 does this implicitly ("e^A as in NF-ex"); state it in the §20 table.

## C.6 Proposition KΠ (l.2531; l.2705-2720): CONFIRMED on its domain
- **Root-value formula.**
  - The convention (U^a)^b = U^{ba} gives Π(U^k) = U^{G(U^k)k}.
  - G(U^k)(z) = M[k(c_X)g_X(U)(z)k(z)^{-1}] = M[k(c_X)g_X(U)(z)]k(z)^{-1}, by NF-cov and right-equivariance of the
    bi-invariant Karcher mean.
  - Hence ĥ = M[k(c_X)g_X]·M[g_X]^{-1}. It depends on k **only through its root values**. Verified.
  - Post-proof correction (4) is right: the covariance identity itself is automatic for any root-normalised G. The content
    is the root-value dependence, which bb6n N5 shows fails for exponential-coordinate gluing.
- **Idempotence:** G(U^G) = M[g_X(U)]G^{-1} = 1, using G(c_X) = 1. Correct.
- **Smoothness of ĥ at U = 1** (M_{χ^5}[k(c_X)]): C^{2,1}.
  - Across cell faces the corner set changes. A corner whose weight vanishes does not move the Karcher mean, and χ^5 vanishes
    to second order there, so the pieces match to order 2.
  - The Karcher mean is analytic in the weights near the simplex (IFT on Σw_ilog(M^{-1}p_i) = 0).
  - Correct.
- **Linearisation to Π_E:** correct. U^g ≈ a − dλ, d*(a − dλ) = 0 with λ(c_X) = 0, and M linearises to the tent average.
- **Domain (see D.7):** the ≤ 16 corner points must lie in one Karcher ball. 19.13 checks this for U small in one global
  gauge. Its "CL-F4 does not occur on 𝒞_glob" is correct **as stated**: if V and V^h are both in 𝒞_glob(ε), neighbouring root
  values differ by ≤ 2ε, hence by ≤ 8ε across a cell.

## C.7 Lemma GC-lin and Proposition AX-cov (l.2538, l.2541; l.2722-2739): CONFIRMED
**GC-lin.**
- μ(dν) = C_0ν − S_0ν and S_1d = dS_0, so R(dν) = dC_0ν.
- Q_axRB = B: μ(c_Y) = ψ_Y(Y) = 0 by interpolation.
- The R-chain and the S_1-chain differ by a composite gauge trivial at level k: λ_j = S_0λ_{j+1} + μ_j, ev λ_j = λ_{j+1}
  (μ_j = 0 at level-(j+1) roots), λ_k = 0. So Π_E∘(R-chain) = Π_E∘Z^lin. Correct.

**AX-cov covariance.**
- P_{X←i} ↦ h(X)P h(i)^{-1}, so A^X ↦ Ad_{h(X)}A^X (the principal log is conjugation-equivariant).
- Then R^{ax}(Z^h)(b) = h(X)R^{ax}(Z)(b)h(X')^{-1}. Correct.

**AX-cov linearisation (signs re-derived).**
- Fixed-order axial paths have the tail property, so the axial condition ∫_{a(i→X)}A^X = 0 forces A^X = B + dψ_X with
  ψ_X(i) = ∫_{a(i→X)}B.
- Inside block X: μ(A^X) = 0, so s^X = S_1B + dS_0ψ_X = RB.
- On a face link:
  - μ(A^X)(z') = S_0ψ_{X'}(z') − S_0ψ_X(z') + ψ_X(X');
  - so s^X(b) = S_1B(b) + S_0ψ_{X'}(z') − S_0ψ_X(z) + ψ_X(X');
  - ψ_X(X') = −B(X, X'), so s^X(b) + B(X, X') = RB(b).
- All signs agree with l.2735-2738. **The upgrade from ARGUED to PROVEN is justified.**

## C.8 Theorem CovLift-KΠ (l.2544; l.2741-2752): (i)-(iii) CONFIRMED-WITH-FIX given (N2-0); (iv), (v) OPEN
- **(i)** AX-cov gives chain(V^h) = chain(V)^K with K = h∘X_k block-constant. KΠ then gives Z^{KΠ}(V^h) = Z^{KΠ}(V)^{ĥ}, with
  ĥ = M[h(X)g_X]M[g_X]^{-1} restricting to h at level k. The cocycle follows by CL-uniq.
  - Z^{KΠ}(1^h) = 1^{ĥ}, with ĥ the Karcher-tent interpolation, so the CL-blk obstruction is avoided: correct.
  - **Scope (binding RS6-4):** this holds for gauges h whose neighbouring root values are within O(ε) (V, V^h ∈ 𝒞_glob(ε)).
    (CovLift) (i) (l.1637) is quantified over every level-k gauge; see D.7.
- **(ii), (iii):** correct. The range is a geometric sum, as in GC-lin (4).
- **Level-k field unchanged:** G = 1 at the roots, so the level-k field is V. Correct.

---

# PART D: walls, (N1-G) and the domain of the Karcher gluing

## D.1 (N2-0) (l.2742): precisely stated? NO (binding RS6-5)
**Two defects in the statement.**
- (a) The quantifiers are missing. It should read: "there is ε_1 = ε_1(ε_0, L, φ, N), independent of k and T, such that for
  V ∈ 𝒞_glob(ε_1) …".
- (b) It is stated at level 0 only. But R^{ax}_j is defined only when the axial-frame logs at level j + 1 are in the
  principal domain. The chain needs, at **every** level j, coarse-unit field and curvature ≤ ε_0 in the axial frames.
- Restate (N2-0) as an inductive per-level statement. The level-0 clause used by NF-ex is then its j = 0 case.

**How hard (reviewer sketch, ARGUED; this is a positive signal).**
- In the axial frame at X, the coarse-unit connection on the DD8 stencil (≤ 4 level-(j+1) links) is
  |A^{X,c}| ≲ 4ρ_{j+1}·sup|F^c_{j+1}|. Axial-gauge transverse components are bounded by distance × curvature.
- So the BCH defects of R^{ax}_j are O(ε²ρ_{j+1}²) in coarse curvature units inside blocks, and O(ε²Lρ_{j+1}) on face links
  (from [s^X, B(X, X')]). Both decay geometrically with depth.
- Writing F_j = S^{(2)}F_{j+1} + E_j, with ||(S^{(2)})^t||_∞ ≤ C_φ uniformly in t (DD8, β ≥ 0.473), gives
  ||F_0|| ≤ C_φ(ε + CΣ_tL^{-t}ε²) by induction. This is **k-uniform**.
- This is the proximity / smoothness-equivalence mechanism of manifold-valued subdivision (Wallner-Dyn proximity
  conditions; Grohs's analyses of Lie-group and interpolatory schemes). I cite these from memory; they were not opened in this
  review.
- The axial frame is what supplies the geometric decay. **(N2-0) looks tractable**, about a lemma's worth.

## D.2 (N2-bd) = (R3): precisely stated? Partly
- 19.16 states "k-uniform C^{1,α} bounds and residual sizes of the iterated R^{ax}". The Hölder version of D.1 follows the same
  route: the defect's coarse Hölder-gradient is O(ε²ρ^{1−α}), still summable for α < 1.
- The derived DD8 scheme's C^{0,β} contractivity (β ≥ 0.47 > α = ¼) is available.
- The **residual sizes** are a separate matter (D.4, the C_g clause).
- Estimate: moderate. Several pages of bookkeeping with no conceptual obstruction found.

## D.3 (N1-int) (l.2749-2750): precisely stated: yes. Difficulty: routine
- The system is d*w = 0, dw = F − B(w, w) on the box, with B the local BCH polynomial. In coarse units,
  [B^c]_α ≤ C||w^c||_∞[w^c]_α.
- A small-data bootstrap of EP-int (LES-div is n-uniform; margin N'_X) gives interior C^{1,α} of w. With the C^{1,α} input from
  (N2-bd), this gives C^{2,α} of g_X in coarse units.
- Standard. The one care point: the bootstrap needs [w^c]_α on N'_X, which comes from Campanato iteration starting at (N1-bd)'s
  sup bound.

## D.4 (N1-G) (l.2466): named import; TRUE with C_G = ¼; elementary proof (reviewer, PROVEN-HERE modulo one classical lemma)
- **What it is.** The ℓ¹ bound Σ_y|∇G_M(y)| ≤ C_GM for the mean-zero Green function of −Δ on the 4D torus of side M.
  - This is weaker than lane A's pointwise import |∂G(y)| ≤ C|y|^{-3} (BA-7, IMPORTED-NOT-YET-REVERIFIED), and implied by it.
  - It is standard lattice potential theory.
- **Proof (M even).**
  - (1) G_M = ∫_0^∞(p_t − M^{-4})dt, with p_t(y) = Π_iq_t(y_i), where q_t is the continuous-time simple-random-walk kernel on
    the M-cycle. The integral converges absolutely for ∇G, with exponential decay for t ≫ M².
  - (2) **Lemma (classical; reflection principle):** q_t(x) is non-increasing in x ∈ [0, M/2].
    - Reflect about the bond (x, x + 1) and its antipode.
    - A path from 0 to x + 1 must cross a mirror. Reflecting after the first crossing maps it injectively onto the paths
      from 0 to x.
  - (3) Hence p_t(·, y') is symmetric-decreasing in y_1 for every y', and so is G_M(·, y'). So
    Σ_{y_1}|∂_1G_M(y_1, y')| = 2(G_M(0, y') − G_M(M/2, y')).
  - (4) Sum over y'. g(y_1) := Σ_{y'}G_M(y_1, y') is the 1D mean-zero Green function, g(y) = −|y|/2 + y²/(2M) + c. I checked
    −Δg = δ_0 − 1/M. So g(0) − g(M/2) = M/8.
  - (5) Therefore **Σ_y|∇_1G_M(y)| = M/4 exactly**: C_G = ¼, sharp. (M odd: ≤ (M² − 1)/(4M) < M/4.)
- **Numerical check (reviewer probe, exact FFT):**
  - Σ|∇G_M| = 2.0000, 4.0000, 6.0000, 8.0000, 12.0000, 16.0000 for M = 8, 16, 24, 32, 48, 64. That is M/4 to every printed
    digit.
  - The 1D cycle kernel is unimodal at every (M, t) tested.
  - max|y|³|∇G_M| = 0.1735, flat in M, consistent with BA-7's pointwise form.
- **Consequences.**
  - (N1-bd) holds with C_B ≤ 60·¼ = 15 (in fact ≤ 7.5).
  - NF-ex, KΠ and CovLift-KΠ no longer depend on an import.
  - Lane B should write this into §19.11 as a PROVEN-HERE lemma with its own check (RS6-6).
  - The reflection lemma is the one classical ingredient. Its proof is one paragraph.

## D.5 The C_g clause at θ > 0: NOT precisely stated (binding RS6-7). A design question, not only analysis
- 19.16 and the table say "C_g clause at θ > 0 (RS5-5)" with no formula.
- The clause is (CovLift) (iv)'s ||g_{Z^sm(V)}||_Y ≤ C_g||b||_∞ (l.1641). Here g_Z is the source the functional generates at
  the background Z. Its residual-type part is κ_lr_l(Z) at each level, in ||·||_R with weights ω^R_lL^{k−1−l} = L^{θ(k−l)}L^{k−1−l}.
- So the clause requires the lift's **lane-A-Q residuals** r_l(Z) = Q_lZ_l − Z_{l+1} to be small enough that
  max_lL^{θ(k−l)}L^{k−1−l}||r^c_l(Z)|| ≤ C_g||b||. This is a consistency requirement between the lift and the functional's
  blocking map.
- For R^{ax}/GC: Q_axR = 1, but Q_l ≠ Q_ax. With lane A's Q, CL-lin (e) gives residuals ∼ 2||f_l|| at every level (S5 C.3).
- Options:
  - (a) Q_ax as the functional's Q. This is lane A's choice; it changes BL-2 constants, not the structure.
  - (b) A Q-consistent lift R' := R∘(Q∘R)^{-1}.
    - It keeps linear covariance, since Q∘R(dν) = d ev C_0ν = dν. It makes the residual part of g_Z vanish identically.
    - But (Q∘R)^{-1} is at best exponentially local, so (CovLift) (ii) must be relaxed to exponential locality (S4 E.2).
    - The invertibility of Q∘R on one level (a k-independent, finite-range operator: check its symbol) is NOT verified.
  - (c) θ = 0 for the residual-type slot only. This is a lane-A weighting decision.
- Rank: (a) or (b). Each is a few-line linear check before any nonlinear work.

## D.6 Difficulty ranking of the named walls
| wall | precisely stated? | difficulty | note |
|---|---|---|---|
| (N1-G) | yes | **done** (D.4) | C_G = ¼ exactly; write up |
| (N1-int) | yes | routine | small-data Campanato bootstrap of EP-int |
| (N2-0) | **no** (per-level, quantifiers) | moderate | axial-frame BCH defects O(ε²ρ_{j+1}²): k-uniform (D.1, ARGUED) |
| (N2-bd) = (R3) | partly | moderate-hard | Hölder version of D.1 plus residual sizes; manifold-subdivision proximity is the template |
| C_g at θ > 0 | **no** | design + linear check | Q-consistency of lift versus functional (D.5) |
| CL-F4 off 𝒞_glob | not named | **hard** | D.7 |

## D.7 The domain of the Karcher gluing: CL-F4 OCCURS off 𝒞_glob (new finding; binding RS6-4)
**The obstruction.**
- Let U = chain(V) with V having small plaquettes but coarse links V(X, Y) not near 1. This is GI-off's class (13.8:
  holonomies and torons allowed), or V^h with V ∈ 𝒞_glob and h large.
- Each box normal form puts N_X(U) small. On box overlaps, N_X = N_Y^{g_Xg_Y^{-1}} with both small, so g_Xg_Y^{-1} is nearly
  constant there, and g_X(c_Y) ≈ V(X, Y)^{±1}·(1 + O(ε)).
- So the ≤ 16 corner points {g_X(U)(z)} differ by the coarse transports. They lie in no common small ball, and
  G(U) = M[g_X(U)(z)] is undefined.
- Any "aligned" variant (left-multiplying by coarse transports to a base corner) breaks G(c_Y) = 1 at the roots, or is
  discontinuous across cells.

**What survives.**
- Theorem BB-gi_k on 𝒞_glob(ε) uses only small gauges: for V ∈ 𝒞_glob, the box frames g_□ and ĝ_□ are near 1. So BB-gi_k holds
  with Z^{KΠ}.
- On the gauge saturation of 𝒞_glob, the activities can be *defined* by invariance. Two 𝒞_glob representatives of one orbit
  differ by a gauge with O(ε) neighbouring root differences, where KΠ covariance applies. Locality is inherited by the same
  argument.
- So "(BB-gi)_k on 𝒞_glob and its gauge saturation" survives, with this sentence added to 13.7.
- **Proposition GI-off needs (CovLift) on locally-small fields. Z^{KΠ} as constructed does not supply it:** CL-F4 OCCURS
  there.
- Note that R^{ax} itself is fine on GI-off's class: it is covariant under all gauges, with a block-constant extension. Only
  Π^{NA} fails.

**Fix.**
- 19.13's "CL-F4 does not occur on 𝒞_glob" stays.
- Add "CL-F4 OCCURS on GI-off's class and for large gauges: Π^{NA} is defined only where neighbouring box normal forms agree to
  O(ε) at the shared points".
- Restate CovLift-KΠ (i) as "for every level-k gauge h with max_{X∼Y}d(h(X), h(Y)) ≤ c·ε".
- Name the new wall **(KΠ-off)**: a root-normalised, gauge-covariant gluing of box normal forms for locally-small fields.
- (KΠ-off) is the genuinely nonabelian part of the old (UHL)/(SL-cov) frame problem. Balaban avoids it by never forming a global
  lift (local axial frames per block plus covariance under local gauges). That remains the robust alternative off 𝒞_glob.

---

# PART E: checks (bb6m, bb6, bb6n)

**bb6m: CONFIRMED.**
- Byte-identical re-run.
- It reproduces my S5 Part D numbers exactly: DD8 β_10 = 0.4732; DD6 β_10 = 0.2677 (n = 7, 8: 0.2454, 0.2547); DD4 ρ_n = 1.2222
  for all n ≤ 10; DD4 weights (−5, 60, 30, −4)/81.
- This is independent code agreeing with my independent exact computation. RS5-10's checks/ request is satisfied.

**bb6 (bb6_transport.py, read line by line): CONFIRMED.**
- The normal equations match E_src (B.1). Q := Q_str − d∘h with an averaged axial h is root-covariant (A0: 1.5e-15).
- CG converges to a relative residual of 8.7e-14 on the singular, consistent system. The right-hand side annihilates the
  composite gauge kernel, since j_0 and j_1 are d* of 2-forms.
- A2-A4 test exactly Lemma RT (a)-(c) at a critical point with every co-closed source class. A6 is BL-2 (c), with ratio 1.000.
- Part B: H_m = s^{-2}·avg_{j<s}ρ(· − je_μ) is (Q_str^{(L^m)})^Tρ in coarse units. The centred block assignment matches OFFS.
- Scope:
  - Part A has k = 2 (one transport step) and T = 2.
  - Part B is a property of Q_str^T alone (no critical point). B1's ratio 1.000 is attained trivially by line-constant ρ.
  - So bb6 confirms the identities, not the depth uniformity. That uniformity is the proof's geometric sums, which I checked
    by hand.

**bb6n (bb6n_nf.py, read line by line): CONFIRMED, informational only.**
- Quaternion algebra, principal log, the Neumann divergence (invalid links zeroed) and the χ^5 product tents (a partition of
  unity; normalising by Σ is harmless) are correct. The Karcher iteration is correct.
- **The input has ε_f(U) = 2.02.** It is outside NF-ex's hypothesis (ε_0 small), and the theorem is d = 4 while bb6n is d = 2.
- N3 and N4 (c) start the descents within 0.3 of the predicted normal form. They confirm that the predicted point is critical
  and attracting, not that it is unique; only N2 (four starts, on U) addresses uniqueness.
- The N4 (c) gauge has root values within 0.2. That is the small-gauge regime of D.7. The large-gauge regime is not tested, and
  by D.7 Π^{NA} is not defined there.
- N5 is a good control: exponential gluing violates the root-value formula by 0.336.

---

# Overclaims
1. l.2500-2502, l.2615-2616, table l.2785, FOR OTHER FILES l.2808-2810: "every source class of 𝒴^∇", including BCH₂ rows. It
   holds for co-closed classes only; the non-co-closed BCH₂ remainder is outside Lemma RT (RS6-1).
2. l.2744-2747, table l.2797, l.2803: "(CovLift) (i) exact orbit covariance". It is proven for small gauges only, and CL-F4
   OCCURS off 𝒞_glob (RS6-4).
3. l.2742: (N2-0) is stated at level 0 without quantifiers, but the chain needs it at every level (RS6-5).
4. l.2751, l.2797: "C_g clause at θ > 0" is listed as a wall without a statement (RS6-7).
5. l.2805, l.2811: "a proof of (N1-G) on the framework" is listed as a lever. It is now a two-paragraph lemma (D.4). This
   is an underclaim to be corrected.
6. l.2788 "T = 3, 4 not covered": an underclaim. The periodic lift covers them (RS6-3).

# Tally (lane B session 6; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | provenance (byte accounting: §18 = 12505 B exactly); RBB5 fixes (all 10); **Lemma RT**; **Lemma TC**; **Theorem RH** ((Res-Hölder), m = 0, co-closed Setting LIN; no elliptic step); **Theorem RH_m** (c_w = 12; data map (Res-Hölder)_m); Corollary RH-D; the α = θ example (RH-F2 exactly at α = θ); Lemma NF-crit; **Lemma NF-uniq** (δ_0 n-independent); Lemma NF-cov; Lemma REF / (N1-bd) given (N1-G); Theorem NF-ex (with its post-proof hypothesis); **Proposition KΠ** (on its domain); Lemma GC-lin; **Proposition AX-cov** (linearisation signs re-derived); bb6m, bb6, bb6n (re-runs byte-identical) |
| CONFIRMED-WITH-FIX | **Corollary RH-inv** (RS6-1: co-closed scope); **Corollary LRL(b)-E** (T ≥ 5; T = 3, 4 by lift, RS6-3); **Theorem CovLift-KΠ (i)-(iii)** (RS6-4: small gauges; RS6-5: (N2-0) per level) |
| PROVEN HERE (reviewer) | **(N1-G) with C_G = ¼ exactly** (D.4; classical reflection lemma; exact-FFT check M ≤ 64) |
| ARGUED (reviewer) | LRL (b) at T = 3, 4 via a periodic lift; (N2-0) k-uniform via axial-frame BCH decay O(ε²ρ_{j+1}²); Lemma RT for composite-co-closed sources with explicit funnel terms |
| NEW FINDING | **CL-F4 OCCURS off 𝒞_glob** (Karcher gluing undefined for large coarse links or large gauges): GI-off is not supplied by Z^{KΠ} |
| OPEN | (N2-0) (per level), (N2-bd) = (R3), (N1-int); C_g at θ > 0 (to be stated); **(KΠ-off)**; (Res-Hölder) for the non-co-closed BCH₂ remainder; (H-inv) for the remaining classes (lane A); (Mult-Y); (Pair-loc) |

# Required fixes (binding for the next lane-B session unless marked cosmetic)
1. **RS6-1.**
   - (a) In RH-inv (l.2500-2504, l.2615-2616), the table and FOR OTHER FILES, replace "every source class of 𝒴^∇" with
     "every level-wise co-closed Setting-LIN class (G), (R), commutator rows (CR-1), BA-6's residual part, (P0), (Pl-c),
     rough currents, co-closed BCH₂ rows and the completions d*W_l".
   - (b) Add: "the non-co-closed BCH₂ remainder V_l (BFT_A §26.2) is outside Lemma RT; its (Res-Hölder) is OPEN; candidate
     route: RT with explicit funnel terms h_l^Td*ρ_l for composite-co-closed sources".
2. **RS6-2 (cosmetic).** In RH-inv's source list, name the commutator rows (residual type by CR-1).
3. **RS6-3.** In LRL(b)-E and its table row, add the periodic-lift remark (B.7). Then LRL (b) holds for all T ≥ 3, with
   C_b(T = 3, 4) ≤ e^{20m}C_b(2T). Mark it ARGUED-routine or prove it.
4. **RS6-4.**
   - (a) In CovLift-KΠ (i) (l.2744-2747) and the table, read "for every level-k gauge h with max_{X∼Y}d(h(X), h(Y)) ≤ cε
     (V, V^h ∈ 𝒞_glob(ε))".
   - (b) Add "CL-F4 OCCURS off 𝒞_glob (GI-off's class) and for large gauges" (D.7).
   - (c) In 13.7, add the sentence extending BB-gi_k to the gauge saturation by invariance.
   - (d) In GI-off's row, record that Z^{KΠ} does not supply (CovLift) there. Name the wall (KΠ-off).
5. **RS6-5.** Restate (N2-0) per level with quantifiers (D.1).
6. **RS6-6.** Replace the (N1-G) import by the D.4 lemma (C_G = ¼). Add a checks/ reproduction (exact FFT; unimodality of the
   cycle kernel). Update l.2466-2468, 19.11, the table, l.2805 and l.2811.
7. **RS6-7.** State the C_g clause at θ > 0 as a formula (D.5). Check options (a) Q_ax in the functional, or (b) R∘(Q∘R)^{-1}
   (the symbol of Q∘R on one level), before any nonlinear work.
8. **RS6-8 (cosmetic).**
   - Rename lane B's Theorem RH (lane A has a Lemma RH, §23.8).
   - In 19.6, rename the depth m → t.
   - Φ is used both for the box functional and for the S_0 kernel; C_1 and C_B collide between 19.4, 19.9 and 19.11.
9. **RS6-9 (cosmetic).**
   - Mark the 09:35:12 in-place correction inside 19.4.
   - Strike "mask regularity measured (bb5), not proven" at l.2421.
   - Remove the dangling "… more precisely" in §18.2 NF-ex. That is pre-stated text: annotate it in §19, do not edit §18.
   - Give the exact A5 edit time (09:25:02) in bb6_criteria.md.
   - In 19.13, state that 𝒟(ε) carries both NF-ex hypotheses.

# Strategic verdict
- **(Res-Hölder) is closed** at the linear level, trivial chain, co-closed classes, k-, T- and level-uniformly, both
  unweighted and weighted (data map). It took a transport identity, not an elliptic estimate, so the lane-B elliptic
  machinery (EP-rec) now runs on gauge-invariant inputs only.
- With lane A's (H-inv) this gives (W-lin-Π) for S_E. With Proposition W it gives LRL (b) for all T ≥ 3 (lift).
- The gauge-variant half of (H-lin^∇) is no longer a wall on the co-closed classes. What remains there is the non-co-closed BCH₂
  remainder, which is also lane A's open item.
- **Nonabelian (CovLift) on 𝒞_glob has moved from "not constructed" to "constructed with exact covariance (small gauges) and
  smooth extension".**
  - The normal-form uniqueness and covariance are genuine theorems.
  - (N1-G) is now proven (D.4).
  - (i)-(iii) rest only on (N2-0) and the cited Karcher facts.
  - (iv), (v) need (N1-int) (routine), (N2-bd) (moderate, with a plausible k-uniform mechanism) and a decision on the C_g
    clause.
- **Off 𝒞_glob the Karcher route stops** (CL-F4 occurs). GI-off is therefore not advanced by this session.
  - That is the place where Balaban's local-frame method, rather than a global lift, remains the reference.
  - It should not be attempted before the 𝒞_glob chain BFT-4 ⇐ … is closed.
- **Recommended order for session 7:**
  1. the C_g formula, plus the linear Q-consistency check;
  2. (N2-0) per level (D.1);
  3. RT for composite-co-closed sources;
  4. (N1-int);
  5. the write-up of (N1-G).

# Current minimal open set for BFT-0..4 (on 𝒞_glob unless marked)
- **BFT-0/1/2:**
  - (H-lin^∇) at configuration level, m = 0, trivial background ⟸ (H-inv) on the co-closed Setting-LIN classes, plus
    (Res-Hölder) for the non-co-closed BCH₂ remainder V_l. The first part of (Res-Hölder) is now CONFIRMED (Theorem RH +
    RH-inv).
  - (H-inv): lane A's Theorems W0, GU, YH and Corollary LIN0 (§26, unreviewed; pending REVIEW_BFT_A_S6) would supply all
    co-closed classes at m = 0 for α < θ. The X_s halves, Theorem W and (G♯-rough) for α < θ are CONFIRMED earlier.
  - (H-rem^∇) third order: ARGUED. (FP♯').
  - The background-covariant slice is (N1-int) + KΠ (𝒞_glob).
  - Off 𝒞_glob: (UHL), (SL-cov), (KΠ-off).
- **BFT-3:**
  - k = 1 PROVEN.
  - k ≥ 2 ⇐ weighted (H-inv)_m on the co-closed classes. The weighted (Res-Hölder)_m is CONFIRMED (RH_m, all co-closed
    classes). Plus V_l at m > 0.
- **BFT-4:**
  - k = 1 PROVEN.
  - k ≥ 2 bounded polymers ⇐ RW^∇_k-Π(E) [(W-Π) PROVEN; (W-lin-Π) ⇐ (H-inv) + V_l] + (W-comm) [GAP 1 plain rows] + (W-loc) +
    (f) + (E3^∇) [ARGUED] + (I-id).
  - Gauge-invariant pieces ⇐ + (CovLift) on 𝒞_glob = Z^{KΠ}. Its inputs: (i)-(iii) ⇐ (N2-0) [OPEN, tractable]; (iv)
    ⇐ (N1-int) [routine] + (N2-bd) [moderate] + C_g at θ > 0 [to be stated; linear check]; (v) holomorphy [ARGUED via IFT].
  - Plus (Mult-Y) [GAP-1 family] + (Pair-loc) [ARGUED] + (I-id)_Z [ARGUED].
  - Off 𝒞_glob: GI-off [ARGUED] now also needs (KΠ-off).
- **Rate:** κ_L ≥ m/8 under weighted (H-inv+)_m = weighted (H-inv)_m (RH_m) + localised (W-comm) (RATE-m).
- **Largest levers:**
  - (a) lane A's (H-inv) review (LIN0) together with the V_l remainder;
  - (b) the (Pl)-free plain-row theory (GAP 1 + (Mult-Y));
  - (c) (N2-0)/(N2-bd) with the C_g decision;
  - (d) (KΠ-off), only after the 𝒞_glob chain closes.

---

## Re-run record and reviewer probe
- Runner: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revBB6/run.sh`.
  - It waits with `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, then waits for load1 < 8.
  - Environment: nice 10; OMP/OPENBLAS/MKL/VECLIB/NUMEXPR threads = 1; PYTHONDONTWRITEBYTECODE=1; `/usr/bin/time -l`; python3
    without -I; no `timeout`; no trap; `rmdir` exactly once at the end.
- One acquisition, 09:46:15-09:47:09 UTC: load1 2.57; memory free 32% (38% before the run).
  - bb6m_mask: byte-identical; 0.38 s; 96 MB.
  - bb6_transport: byte-identical apart from the `[t = …]` line; 5.92 s; 549 MB.
  - bb6n_nf: identical except the embedded timing in the N4 header (41.7 s → 42.7 s); 46.1 s; 35 MB.
  - Reviewer probe revBB6/n1g_probe.py (exact FFT on 4D tori, M ≤ 64; 1D cycle kernel unimodality): 1.0 s; 680 MB.
    Results in D.4.
- Afterwards: lock directory absent; no bb6/n1g process left (pgrep empty); no __pycache__ in checks/. Outputs are in
  scratchpad/revBB6/ (*.rerun.out, *.rerun.time, n1g_probe.out, lock.log). No repository file other than this review was
  written.
