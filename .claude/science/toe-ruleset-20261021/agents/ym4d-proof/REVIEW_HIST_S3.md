# REVIEW_HIST_S3: hostile review of lane D session 3 (HIST.md §19-§23 and the [RH2-fix] changes)

Reviewer: an independent agent that wrote none of HIST.md or its checks. I edited no other file. No commits, PRs or pushes.

Inputs (read-only):
- REVIEW_HIST_S2.md (all; the format and fixes 1-13).
- HIST.md §14 (l.832-955), §15 (l.956-1079), §17-§18 (l.1105-1138), §19-§23 (l.1140-1434); the [RH2-fix] lines (grep).
- HIST_LOG.md session 3-D (l.68-105), including the h5 disclosures (l.77-80).
- LINEAR_PACKAGE.md §1.2 (S4', roots = block centres); RLARGE.md Lemma RS (l.740-773: A_d, (R1)-(R5), η_1).
- checks/h6_criteria.md, h6_msg_cone.py, h6_out.txt, h6_time.txt, h6b_diag.py, h6b_out.txt, h6b_time.txt; mtimes. Both
  scripts re-run (below).
- literature/balaban_cmp109_text.txt l.183-256, l.480-590, l.684-710 (read-skim, for the gauge-fixing comparison).

Scratch work (wrapper, re-run outputs) is in the scratchpad directory `revhist3/`.

---

## Bottom line

- **All thirteen RH2 fixes are applied correctly.** Two leftovers need the same edit: the CLS-red display at l.1027-1028
  still shows the old constant, and η_E's dependence still names C_AE (N-4 below).
- **Theorem MSG: CONFIRMED-WITH-FIX.** I re-derived steps (1)-(7) and every constant.
  - The construction is sound: one bounded axial box at the top, then a block-internal gauge to a Whitney reference field at
    each level.
  - The interpolation does not need to satisfy the S4' averaging relation. V is only a comparison field, and the actual
    fields are changed by a gauge transformation alone. The averaging relation enters through hypothesis (ii) and the
    exact identity hol_V(S_c) = e^{a_c} (W2), and both are used correctly.
  - In sup norm the BCH terms do not accumulate. Each level's term is absorbed into ε by (S3), and inherited sizes contract
    by exactly 1/L. So C_M = 66.1 is depth-independent.
  - One count is wrong. A_ax = 9 needs the axial order to start with one of P's plane directions. With the fixed order
    0, …, d - 1 and P in a plane not containing axis 0, the ladder reaches 2(2L - 1) + (d - 3)(L - 1) = 12. C_M is unchanged
    (fix S3-1).
- **Corollary MSG-loc: GAP (not "the same proof").** Step (5)'s quadratic BCH term 33α²e^{4α} is absorbed by the GLOBAL ε
  through (S3). In the local form it survives as a per-level source c·α_{cell}² that is not bounded by the local ε̂_j.
  Absorbing it instead gives a contraction of (1 + O(ε))/L per level. Either version breaks the exact scale invariance that
  MS-HLS needs (fix S3-2). **This is where the non-abelian corrections DO accumulate over levels: in ℓ⁴, not in sup.**
- **Lemma MS-HLS: CONFIRMED** (constant 432 = 24·4·4.5, re-derived). It needs d = 4, which it never states (fix S3-3).
- **MS-Sob ⇐ (SQ): the implication is valid, but its premise is false. Not a usable CONDITIONAL.** The (SQ) it consumes has
  x̂_j equal to MSG-loc's sources: curvature and residual sizes. HIST's own k-fold example refutes that version, and I
  confirm the example. The deviation-source (SQ) needs a deviation-source MSG-loc, which nobody has proven. Recount the item
  as ARGUED (fix S3-4).
- **(AE) ⇐ MSG + (MS-Sob): CONFIRMED as ARGUED.** Writing it out fully is session-scale bookkeeping.
- **Corollary CLS-cone: CONFIRMED as CONDITIONAL ⇐ (AE)**, with RLARGE's actual η_1. The conversions (a)-(c) are right.
  - (c) covers only level-k defects.
  - Mixed-level defect sets pay 24 per level, so k-fold overall, unless the selection uses disjoint cones (fix S3-5).
- **(I_k^E)': HYPOTHESIS. S2-3 repaired; S2-1 repaired with one new hole; S2-2 repaired with one notational error.**
  - (a'): an inf over real chains has no analytic continuation, but (b') needs one (fix S3-6, new item (a5)).
  - (b'): "Ve^{iZ}, Z Hermitian" is unitary, so the domain as written has no complex points (fix S3-7).
- **h6: honest.** The criteria predate the script, A2/A3 FAIL is recorded and stands, h6b is labelled post hoc, and the
  re-run reproduces every stored line.
- **Corrected session-3 tally: 2 PROVEN-HERE / 1 CONDITIONAL / 2 ARGUED / 1 OPEN + HYPOTHESIS (replaced).** The claim was
  2/2/1/1. **Whole file: 9 / 4 / 8 / 4 + 1 HYPOTHESIS** (claimed 9/5/7/4 + 1).

---

## Priority 1. The RH2 fixes

| Fix | Where | Verdict |
|---|---|---|
| 1-3 (S2-1, S2-2, S2-3) | marked GAP in §14.1 l.842, l.852-854, l.858-859, l.870-872; repaired in §20.3 (C) | CONFIRMED as marking (the repairs are Priority 5) |
| 4 (S2-4, side ≥ 3) | §15.1 l.968-969; E-loc l.979 | CONFIRMED |
| 5 (S2-5, C'_AE) | §15.3 l.1006-1010; CLS-red bracket l.1021-1022 | CONFIRMED-WITH-FIX (N-4) |
| 6 (S2-6, ribbons in cone) | l.1038-1041 | CONFIRMED |
| 7 (S2-7, U_k(P) = e^X) | l.1007-1009 | CONFIRMED |
| 8 (HF, N = 2 wording) | l.885 | CONFIRMED |
| 9 ((c4) sign) | l.937-938 | CONFIRMED |
| 10 (FLOW strengthening) | l.911-920 | CONFIRMED |
| 11 (§17-§18 wording) | l.1118-1120, l.1126-1127 | CONFIRMED |
| 12 (N-1, N-2, N-3) | l.341, l.580; l.168; l.421 | CONFIRMED |
| 13 (h5 disclosures) | HIST_LOG l.77-80 | CONFIRMED (both mismatches disclosed as I stated them) |

**N-4 (binding, wording/constants).**
- CLS-red's displayed strong form (l.1027-1028) still reads s ≤ max{C_loc, 2/η_E}·E and c_cl = 1/(24·max{C_loc, 2/η_E}).
  With the restated (AE) these are max{C'_AE/(2N), 2/η_E} (= C_cone of §20.3 (B)).
- η_E "depending only on N, L, κ, C_AE, ε_AE" (l.1023) should name C'_AE.
- Since §20.3 adds the energy cap (iii) E_𝒞 ≤ η_AE to (AE), CLS-red must also choose η_E ≤ η_AE. Say so where η_E is
  chosen.
- The bracket at l.1021-1022 fixes the proof but not the statement.

---

## Priority 2. Theorem MSG (§20.2, l.1211-1269) and MSG-loc (l.1271-1278)

### MSG, step by step

**§20.0 facts (l.1182-1194): CONFIRMED.**
- (F1): 2arcsin(x/2)/x at x = ½ is 4arcsin(¼) = 1.0107.
- (F3): the log series on ||Z|| ≤ ½, with ||Z_1^n - Z_2^n|| ≤ n2^{1-n}||Z_1 - Z_2||, sums to 2. The principal log of a unitary
  agrees with the series eigenvalue-wise.
- (F5): the two series agree in orders 0 and 1, and every order-n part is ≤ s^n/n!.
- (F6): LINEAR_PACKAGE l.65-69 states that S4' is root-covariant, with roots = block centres (LINEAR_PACKAGE l.55). So a
  level-0 gauge acting on U_i at the iterated centres is a symmetry of every s, φ and normalisation. The top-down
  extension (keep g at the centres, choose it at the new sites) is consistent: changing g at level-i non-centre sites
  leaves U_{i+1} untouched.

**§20.1 Whitney (l.1196-1209): CONFIRMED.**
- (W1) holds because W(a)_μ is a convex combination of the cell's μ-edges, and b has length 1/L. In a clamped direction the
  component is zero.
- (W2) is exact: on a coarse edge the transverse hats are 1/0. A coarse edge spans L fine links because centres are
  level-i sites.
- (W3): d commutes with W and with the coordinatewise-clamping pull-back (piecewise linear, tangential continuity at the
  hull). W_2 is a convex combination of plaquette values, and a fine plaquette has area L⁻².
- The script's `whitney()` implements exactly this: zero outside the hull in the link direction, clipped linear weights
  transversally, /L.

**(1) Top level: CONFIRMED-WITH-FIX S3-1.**
- In complete axial gauge, link (x, x + e_μ) carries a ladder of Σ_{ν>μ}x_ν plaquettes. The box W_P^{(k-1)} has sides 2L in
  P's two plane directions and L in the others.
- A_ax = (2L - 1) + (d - 2)(L - 1) = 9 holds iff at most one 2L side follows μ in the axial order. That is the case when the
  order starts with one of P's plane axes, as in h6 (P in the (0, 1) plane, order 0, …, 3).
- As stated ("order 0, 1, …, d - 1", P arbitrary), a P in the (1, 2) plane gives, for μ = 0,
  (2L - 1) + (2L - 1) + (L - 1) = 12.
- **Fix S3-1:** "order the axes with P's two plane directions first", or put A_ax := 2(2L - 1) + (d - 3)(L - 1) (= 12).
  - Consequences: C_* = max{1.011A_ax, 2BL/(L - 1)} = 66.1 either way.
  - The second entry of C_M becomes 1.011(1.011·3·12 + 19) = 56.0 < 66.1, so C_M = 66.1 is unchanged.
  - (S1) becomes 12ε ≤ ½.

**(2) Algebra: CONFIRMED.**
- With g(x) = hol_U(γ_x)^†g(c_X)hol_V(γ_x), I recomputed U^g(b) = hol_V(γ_x)^†·[g(c_X)^†hol_U(π)g(c_{X'})]·hol_V(γ_y), and
  V(b) = hol_V(γ_x)^†hol_V(π)hol_V(γ_y) trivially.
- Also hol_{U^g}(γ_x) = hol_V(γ_x).

**(3) Intra-block: CONFIRMED.**
- γ_x and γ_y share the moves along axes < μ. π is a width-1 ladder of Σ_{ν>μ}|x_ν - c_ν| ≤ (d - 1)h = 3 plaquettes, inside
  the block.
- Bounding this by A_d = 9 is generous by a factor 3.

**(4) Inter-block: CONFIRMED.**
- The path word π = P_<μ^hP_>μP_>⁻¹μ^hP_<⁻¹ is right. The far end uses γ_y from c_Y = c_X + Le_μ, which has the same transverse
  offsets, and y is on the -μ face, so the path is μ^{-h} reversed.
- The two deformations cost Σ_{ν>μ}|t_ν| + LΣ_{ν<μ}|t_ν| ≤ (d - 1)hL = A_d plaquettes, in X ∪ Y.
- hol(S_c) - M̄_c ≤ A_dε is RS (R1) (RLARGE l.747: the ribbons lie in B(X) ∪ B(X + e_μ)).
- ||M̄_c - W_0(M̄_c)|| = ||G - 1|| ≤ 18.4y² follows from NA-alg's G-bound and left covariance. y = 1.011√N·A_dε. (S2) gives
  18.4y² ≤ ε and y ≤ 1/20.
- Total: (2A_d + 2)ε + A_d·max||1 - V(p)||.

**(5) Curvature of V: CONFIRMED (in its global form).**
- ||1 - hol_V(p)|| ≤ |dIa(p)| + 16α²L⁻²e^{4α/L}.
- |dIa| ≤ L⁻²max|da(P')|, and |da(P')| ≤ 1.011(ε + 16α²e^{4α}) via (F5) against U^g_{i+1}(P') and (F1) (|da| ≤ 4α < π).
- 1.011·16 + 16 = 32.2 ≤ 33.
- (S3): 33C_*²εe^{4C_*ε} ≤ 1 gives ε_M ≈ 6.9·10⁻⁶ at C_* = 66.1, as stated.
- The coarse plaquettes P' are at level i + 1 ≤ k - 1, so hypothesis (i) applies. Every cell corner is a cone site, because
  W_P^{(i)} is the union of the level-i blocks of W_P^{(i+1)}.

**(6) Recursion: CONFIRMED.**
- B = 2A_d + 2 + 2.02A_d/L² = 22.02.
- (F3) needs both U^g(b) and V(b) within ½ of 1, which (S4) guarantees.
- |a_i| ≤ α_{i+1}/L + 2Bε, and C_*(1 - 1/L) ≥ 2B closes with C_* = 2BL/(L - 1) = 66.06. The same constant holds at every
  level.

**(7) Level k: CONFIRMED.** The bound (2A_d + 1)ε is loose but valid. 1.011(1.011·3·9 + 19) = 46.8 ≤ 66.1.

### The brief's four questions
- **Does the interpolation respect S4' block averaging?** It does not have to, and the proof never assumes it.
  - V is a reference field, and the chain is changed only by the chain gauge (F6).
  - The S4' relation enters through (ii) and RS (R1) on U, and through the one exact property of V that is needed:
    hol_V(S_c) = e^{a_c} (W2).
  - h6 B2 confirms this to 3.3·10⁻¹⁶, and B1 confirms gauge invariance of all s and φ to 9.2·10⁻¹⁵.
  - M̄_c(V) ≠ e^{a_c} in general, and nothing uses it.
- **Do BCH corrections accumulate over levels?** In sup norm, no. The level-i BCH term is ≤ 33α²e^{4α}·A_d/L². By (S3) it is
  ≤ 1.01ε·A_d/L², so it sits inside the per-level cost 2Bε. That cost is multiplied by L^{-(j-i)} on the way down, which
  gives a geometric series. In ℓ⁴ they do accumulate (MSG-loc below).
- **Is C_M depth-independent?** Yes.
  - (S1)-(S4) involve only (N, L, d) and C_*.
  - No gauge is chosen on a region that grows with depth. The top box is bounded in level-(k-1) units, and the γ_x lie in
    single blocks.
  - h6 C (d = 2, depths 1-5; noise family, which exercises the downward steps) gives 1.51, 1.39, 1.51, 1.79, 1.64.
- **Is the theorem a "global small gauge on the cone"?** Yes in output, but Stokes is not violated, because hypothesis (i)
  bounds the plaquettes at EVERY level. The flux through a level-j square is then ≤ ε plus residuals, which is consistent
  with links of size C_Mε·L^{-j}-scaled sums. The target's "not success" clause (a small gauge from level-0 data alone) is
  not triggered. **Target S4: MET** (with S3-1).

### MSG-loc (l.1271-1278): GAP
- The local proof would iterate (6) as |a_i(b)| ≤ L⁻¹max_{nearby c}|a_{i+1}(c)| + 2Bε̂_i(b). But (6)'s 2Bε contains
  A_d·L⁻²·33α²e^{4α}, which (5) converted into ≤ 1.009ε **using α ≤ C_*ε and (S3) with the GLOBAL ε**.
- With local sources the term is 33α_{cell}²e^{4α}, where α_cell is the level-(i+1) link size on b's cell. That is an
  INHERITED size, not a local source. It is not ≤ ε̂_i when the local sources are small and the inherited sizes are not.
- **The correct local recursion is |a_i(b)| ≤ L⁻¹max_{nearby}|a_{i+1}| + 2B'ε̂_i(b) + c_q·α_{cell}(b)²**, with
  c_q := 2·33A_de^{4C_*ε}/L² (≈ 66 at d = 4, L = 3) and B' = 2A_d + 2 + 1.011A_d/L². The step (4) term 18.4y² ≤ ε̂ is
  genuinely local, since y ∝ ε̂.
- There are two ways to close it. Both cost depth-uniformity in the use HIST makes of it:
  - (a) Absorb α² ≤ C_*ε·α. The contraction becomes λ = L⁻¹ + c_qC_*ε (≈ L⁻¹·1.18 at ε = ε_M). In MS-HLS the weights become
    λ^j instead of L^{-j}. The product bound acquires (Lλ)^{j_1+j_2+j_3+j_4}, which reaches (1.18)^{4k} for top-level
    sources. That is not depth-uniform.
  - (b) Keep c_qα_{j+1}² as a source. In (SQ) it contributes Σ_jΣ_{level-j}α_j⁴. This is scale-invariant at each level (the
    same L^{-j}-versus-L^{4j} count as MS-HLS), so it sums to ≈ k·(MS-Sob size) = k·C_SE². A smooth top-scale field
    realises this: α_j ≍ θL^{-(k-j)} on L^{4(k-j)} blocks, so θ⁴ per level.
- **Fix S3-2 (binding):**
  - Restate MSG-loc with the c_qα_{cell}² term (proven by the same proof).
  - Record that the quadratic BCH term is the non-abelian, d = 4-marginal part of the multi-scale problem. Its control is
    part of (SQ) (deviation form, below), not a consequence of MSG.
  - Status: MSG-loc' (with the term) PROVEN-HERE, counted with MSG. MSG-loc as stated is not proven.
- Minor: the radius claim "(r_j + 2)/L + 1 ≤ 2" holds for r_j ≤ 2 and L ≥ 3. Fine.

---

## Priority 3. MS-HLS, the (AE) chain, and (SQ) (§20.3 (A), l.1281-1325)

### Lemma MS-HLS (l.1282-1290): CONFIRMED (PROVEN-HERE, counted); one hypothesis to add
- Expanding over sorted quadruples gives multiplicity ≤ 24.
- The Hölder split is ||g_1||_2||g_2||_2||g_3||_∞||g_4||_∞.
- ||g_j||²_2 = dL^{4j}L^{-2j}h_j, and ||g_j||_∞ ≤ L^{-j}√h_j. The product is dL^{j_1+j_2-j_3-j_4}√(…) ≤ dL^{-m}√(h_{j_1}h_{j_4})·H,
  using L^{j_2-j_3} ≤ 1 and √(h_{j_2}h_{j_3}) ≤ H.
- There are ≤ (m + 1)(m + 2)/2 ≤ (m + 1)² middle pairs, and Σ_j√(h_jh_{j+m}) ≤ H by Cauchy-Schwarz.
- S_L = (1 + x)/(1 - x)³ at x = 1/3 is 4.5, so 24·4·4.5 = 432. Correct.
- **Fix S3-3:** the count "L^{4j} sites per block" is d = 4. In general d it is L^{dj}, and the product acquires
  L^{(d-4)(j_1+j_2)/2}. So the lemma is scale-invariant only at d = 4, which is the critical case it is for. State d = 4.
- **Application constants (nit):**
  - MSG-loc's ε̂_j is a maximum over a radius-2 neighbourhood of b's level-(j+1) ancestor. Converting Σ(max over
    neighbourhood)² to Σ(local)² costs 5^d = 625.
  - Indexing x_j on level-(j+1) blocks costs a factor L^d in ||g_j||²_2.
  - Both are depth-uniform and belong in C_Q. The formula C_S = 24dS_L(2B)⁴C_Q² omits them.

### MS-Sob ⇐ MSG-loc + MS-HLS + (SQ) (l.1291-1297): the implication is valid, but it is a CONDITIONAL on a false premise
- As written, x̂_j are "the local SOURCE sizes of MSG-loc", i.e. ε̂_j: plaquette sizes at levels j, j + 1 and residuals.
- HIST's next paragraph (l.1298-1301) shows that this (SQ) is false by a factor k.
- **I confirm the counterexample.** In the linear abelian case it is exact: r ≡ 0, and d∘Q^m = d∘Q_str^{(L^m)} makes every
  level-j plaquette exactly the flux through its L^j-square, so Σ_{level j}|dB_j|² is the same at every level. Non-abelian
  embeddings change this only by O(y²).
  - With x̂_j ≥ local plaquette sizes, Σ_jh_j ≥ c·k·θ², while E_𝒞 ≍ θ² (only level-0 plaquettes and residuals enter E).
  - So no depth-uniform C_Q exists.
- Add one observation: on the same example (MS-Sob) itself HOLDS.
  - In the MSG gauge, |a_0| ≍ θL^{-k} on ≍ L^{4k} links, so Σ|a_0|⁴ ≍ θ⁴ ≍ E².
  - MSG-loc's pointwise bound is also fine there: Σ_jL^{-j}·θL^{-2(k-j)} ≍ θL^{-k}.
  - The loss is in the ℓ²-over-blocks conversion of MS-HLS with curvature sources, not in MS-Sob.
- Hence:
  - The counted CONDITIONAL "MS-Sob ⇐ (SQ)" rests on a premise refuted in the next paragraph. It carries no weight on the
    path.
  - With S3-2 the premise also has to include the quadratic sources, which are k-fold for the same example.
  - The deviation-source version that HIST proposes as "the correct (SQ)" (l.1302-1307) is a different statement. Its
    reduction to MS-Sob needs a **deviation-source MSG-loc**: |a_i(b) - (Ia_{i+1})(b)| ≤ local deviation sizes +
    residuals + (deviation × size) terms. Nobody has proven it. MSG's steps (3)-(4) bound hol_U(π) - hol_V(π) through
    plaquette SIZES (lasso), not deviations, and the RS ribbons in step (4) are curvature-sized, not deviation-sized.
- **Fix S3-4 (binding):**
  - Re-label: "MS-Sob ⇐ MSG-loc-dev [OPEN] + MS-HLS [PROVEN] + (SQ-dev) [OPEN]: ARGUED (the HLS step proven; the
    deviation localisation sketched at l.1302-1305)."
  - Keep the curvature-source implication only as a remark ("valid but vacuous: its premise is false, §20.3").
  - Name the two OPEN pieces separately, or fold them into one OPEN item, "(SQ-dev) incl. MSG-loc-dev".

### Is (SQ) with deviation sources plausible or known?
- **Linear case: plausible, and known in kind.**
  - The statement Σ_j‖(1 - I_2Q_2)F_j‖² ≤ C(‖F_0‖² + Σ‖dr_j‖²), with F_{j+1} = Q_2F_j - dr_j, is the upper half of a discrete
    Littlewood-Paley / multilevel norm equivalence at smoothness 0.
  - In the Haar case (I = piecewise constant), (1 - IQ)Q^jF are orthogonal wavelet details and the bound holds with C = 1.
  - With Whitney I, (1 - I_2Q_2) annihilates constants. Near-orthogonality across levels then follows from the decay of the
    commutator kernels (an almost-orthogonality/Cotlar argument).
  - These are standard tools of the multilevel-splitting literature (BPX-type norm equivalences; Oswald; Dahmen)
    [inference; not read for this review]. On the lattice, the sampling (decimation) rules out a pure symbol proof.
    HIST's "Σ_j|ψ(L^jξ)|² ≤ C on the symbol side" is the heuristic, not the proof: aliasing terms must be bounded too.
  - Writing the linear proof is plausibly session-scale.
- **Non-abelian case: open, and the d = 4-critical core.**
  - The BCH sources (S3-2's c_qα²) must be shown to be deviation-sized (|a|·|Δa|, where Δa is the cell-to-cell variation),
    so that they decay across levels for fields smooth above some scale.
  - For a smooth non-abelian field the coarse commutator [a_{j+1}, a_{j+1}] interpolated by W_2 and the fine commutators
    [Ia, Ia] agree to leading order (both scale as L⁻²[a, a]). The mismatch is ≍ |a||∇a|, which is summable.
  - Making that a theorem for arbitrary every-level-ε-small chains is the multiscale analogue of Uhlenbeck's ‖A‖_{L⁴} ≲ ‖F‖_{L²}
    in Coulomb gauge. It is not session-scale.

### (AE) ⇐ MSG + (MS-Sob) (l.1310-1322): CONFIRMED as ARGUED
- (1)-(3) are right: the exact recursion with the residual log; e_i quadratic, from F5 + F3 on contours of ≤ p_L = 5L - 4
  links; E-loc's linear identities.
- (4) is right, and it is the scale-invariant heart of the argument:
  - n⁻⁴Σ_yΣ_{p∈sq_y}|R_p| ≤ n⁻²Σ_{R_0}|R_p|.
  - Σ_{R_0}m² ≤ |R_0|^{1/2}(Σm⁴)^{1/2} = 2n²(…)^{1/2}.
  - Hence 2C√C_S·E = 2C√(C_Sη_AE)·√E. The energy cap (iii) is exactly what turns E into ε·√E. Correct.
- (5): the √8L^{-m} weights from E-loc step (4) are right. They need (MS-Sob) at every level i < k (as stated).
- (7): the induction on depth is sound. The top-level m_k ≤ C√E uses MSG-loc only on the bounded level-(k-1) box, where the
  S3-2 quadratic term is harmless (a bounded number of links). The inherited constant enters multiplied by ε, as stated.
- Two things to write when promoting it:
  - (i) The constant C in (7) depends on C'_AE at depth k - 1. Make the closing inequality explicit:
    √(C_locN)(1 + Cε) + Cε√C'_AE + C√(C_Sη_AE) ≤ √C'_AE with C'_AE = 2C_locN.
  - (ii) ε_AE ≤ ε_M ≈ 7·10⁻⁶, so η_E ≲ ε_M²/C_* ≈ 10⁻¹². Hence C_cone ≥ 2/η_E ≳ 10¹² (see Priority 4).
- **Is the ARGUED step session-scale? Yes.** It is bookkeeping on proven pieces: E-loc identities, F-facts, NA-alg, KQ, and
  the depth induction. **(MS-Sob) itself is not**, because it carries the whole d = 4-marginal non-abelian content.

**Net status of (AE) (corrected):** OPEN. (AE) ⇐[ARGUED] MSG [PROVEN] + (MS-Sob). (MS-Sob) ⇐[ARGUED] MSG-loc-dev [OPEN] +
MS-HLS [PROVEN] + (SQ-dev) [OPEN]. HIST's statement that the wall has moved to "the square function of the deviations" is
right. It does not include the deviation localisation of the gauge, which is part of the same wall.

---

## Priority 4. Corollary CLS-cone (§20.3 (B), l.1327-1341): CONFIRMED as CONDITIONAL ⇐ (AE), one scope fix

- **Displayed inequality.** s ≤ |X|²_HS/(2N) ≤ (C'_AE/(2N))E when E_𝒞 < η_E, and s ≤ 2 ≤ (2/η_E)E otherwise. So
  C_cone = max{C'_AE/(2N), 2/η_E}. Correct, and depth-uniform given (AE).
- **(a): CONFIRMED.**
  - s(V) = ‖1 - V‖²_HS/(2N), because ‖1 - e^{iθ}‖² = 2(1 - cos θ).
  - It is ≥ ‖1 - V‖²_op/(2N), so E_𝒞(P) ≥ ε_1²/(2NC_cone).
- **(b): CONFIRMED with RLARGE's actual η_1.**
  - RLARGE l.750 gives η_1 = min{ε_1/(2L²), ε_1²/(512N·A_d)}, i.e. min{ε_1/18, ε_1²/(4608N)} at d = 4, L = 3. Correct.
  - The level-i statement uses CLS-cone at depth i for the sub-chain, which is covered by "every k ≤ K", together with
    nesting.
  - At i = 0, E_𝒞(p) = s(U_0(p)) directly.
- **(c): CONFIRMED for level-k defect sets.** Overlap ≤ 24 gives Σ_{P∈D}E_𝒞(P) ≤ 24E(T), hence ≥ |D|ε_1²/(48NC_cone).
- **Fix S3-5 (binding, scope).** "Usable defect by defect" is proven only for defects at ONE level.
  - Cones of plaquettes at different levels nest: a term lies in ≤ 24 cones at EACH level. So a defect set spread over k
    levels gets only (24k)⁻¹, unless the selection makes cones disjoint (e.g. one price per footprint, as §7.2's disjoint
    shadows do).
  - RLARGE (R3)'s branch "a level-(k-1) plaquette p ⊂ U_4(P) with ‖1 - U_p‖ ≥ η_1" charges P to a finer cone. The map P ↦ p
    is ≤ 24-to-1 (P must have p's block among its corners). So a one-step version holds with 24·24 = 576.
  - State both:
    - (c1) single level: 1/24;
    - (c2) one-step re-seeding (R3): 1/576;
    - (c3) multi-level: needs the history's disjoint-footprint selection, else k-fold.
- **Size of the price (remark, not a fix).**
  - With ε_AE ≤ ε_M ≈ 7·10⁻⁶, C_cone ≳ 10¹². The defect price is u_kε_1²/(2NC_cone) ≳ u_kε_1²·10⁻¹³.
  - That is depth-uniform, so it is enough for a proof. But it forces g² ≪ ε_1²·10⁻¹³ wherever RLARGE needs the price to
    beat per-defect entropy.
  - RLARGE should record this requirement when it consumes CLS-cone.

---

## Priority 5. (I_k^E)' (§20.3 (C), l.1343-1381)

**(a') localised main term: S2-1 REPAIRED, with one new hole (S3-6).**
- (1) Defined and attained: continuous (φ uses the max over SU(N), which is continuous in M), on a compact group power.
  - "Depends only on U on the links of Λ_k" needs a "term's vertices" convention that includes every site a kernel term
    reads (both endpoint blocks of c). §15.1 l.965-966 gives exactly this for cones. Say so.
- (2) Superadditivity: CONFIRMED. The term sets are disjoint, 𝒞(Λ) ∪ 𝒞(Λ') ⊂ 𝒞(Λ ∪ Λ'), straddling terms are ≥ 0, and a
  chain restricted to desc(Λ) is admissible for Λ.
- (4) Localised (c5): CONFIRMED. 𝒞(Λ_{k+1}) ⊂ 𝒞(Λ_k) ∪ {level-(k+1) kernel terms over Λ_{k+1}} when desc(Λ_{k+1}) ⊂ Λ_k. Drop
  the rest (it is ≥ 0).
- Assignment rule and measurable selection: CONFIRMED. The argmin correspondence is compact-valued and upper hemicontinuous
  (Berge), and Kuratowski-Ryll-Nardzewski applies.
- **S3-6 (binding, new): the main term must be analytic where the polymers are.**
  - (b') requires E_k(X; ·) = (log density − main term)'s polymer pieces to be analytic on the complex domain 𝔇_α(X).
  - 𝓔^Λ_k is an infimum over REAL chains, so it has no complex extension. Its measurable per-cube selection 𝓔^Λ_{k,x} is not
    even continuous where minimisers are non-unique.
  - So in (I_k^E)' as written, the polymers cannot be analytic unless the main term is.
  - Balaban defines the action through the minimal configuration U_k(V) and its analytic continuation to regular
    G^c-configurations (CMP 109 text l.490-500, l.523-530 [read-skim]).
  - **Add hypothesis item (a5):** on the small-field part of Λ_k, the localised minimiser chain is unique and nondegenerate,
    and real-analytic in U. 𝓔^Λ_k there is its critical value, continued analytically to 𝔇_α(X). The decomposition into
    𝓔^Λ_{k,x} is by a fixed (analytic) local rule on that region, and the measurable selection is used only off it.
  - (a5) is where (SF-bg)-local enters. It is consumed by (b'), and not only by (a4).

**(b') domain: S2-2 REPAIRED in substance, one notational error (S3-7).**
- The idea is right and solves S2-2: a chart-free, gauge-covariant thickening whose real points contain the ε_1-domain on
  every polymer.
- **S3-7 (binding, notation).** "U = V_be^{iZ_b}, Z_b ∈ i·su(N) (Hermitian traceless)": e^{iZ} with Z Hermitian is UNITARY,
  so as written 𝔇_α(X) ⊂ SU(N)^X has no complex points. The polar decomposition is Ve^{H}, H Hermitian traceless.
  - Write U = V_be^{Z_b} with Z_b ∈ i·su(N), or keep e^{iZ} with Z ∈ su(N).
  - Fact (4) already uses the correct form: U e^{(s+it)Y} = (Ue^{sY})·e^{itY}, where itY is Hermitian for Y ∈ su(N).
  - Fact (2) is unchanged.
- Facts (1)-(4) are otherwise CONFIRMED.
  - Polar decomposition is a real-analytic diffeomorphism SU(N) × (Hermitian traceless) → SL(N, ℂ).
  - Gauge covariance: g_xVe^{H}g_y⁻¹ = (g_xVg_y⁻¹)e^{g_yHg_y⁻¹}.
  - The real points contain the ε_1-domain (‖1 − V_p‖ ≤ 2ε_1 ⊃ ≤ ε_1) for any size of X.
  - Cauchy polydisc: a real change ≤ r|Y| per link moves a plaquette by ≤ 4r|Y| ≤ ε_1, and |H| = |tY| ≤ α_E.
- "MSG is NOT needed for (b')": CONFIRMED for the statement. Proving the per-cube bound will need charts (MSG or Balaban-type
  axial charts) together with S3-6's (a5).

**(d'): S2-3 REPAIRED.** The normalisation term is listed, with the right class and its feed into Γ_k / u_{k+1}. (Its
field-independent part, -((N²-1)/2)log(κu_k) per link, is a c-number for 𝒱_k. Say so, to keep E_0 g-independent.)

**(a3), (a4): CONFIRMED as honest new hypothesis items.**
- (a3), a per-cube upper bound on a minimiser's local density, is not implied by a global upper bound. It is genuinely a
  locality statement.
- (a4) is correctly labelled ARGUED. Its routing of the boundary defect to ℒ_𝔥/B_0 rather than to the polymers follows
  (c3), and it is consistent with S2-1's demand.
- (c4) with 𝓔^Λ is CONFIRMED (arithmetic).
- **Target S5: MET in the reduction form, with fixes S3-2, S3-4, S3-6, S3-7.**

---

## Priority 6. h6, h6b (re-run)

### Procedure and honesty
- **Criteria predate the script.** mtimes (EDT): h6_criteria.md 21:01:44; h6_msg_cone.py 21:10:55 (its final pre-run fix;
  HIST_LOG l.85-87: written 01:02-01:10 UTC, crash at 01:10:21); smoke run 21:13:01; h6_out/h6_time 21:16:21. The script
  was not touched after the run.
- **h6b is post hoc.** h6b_diag.py (21:16:49) postdates h6_out (21:16:21). It is labelled post hoc in its docstring, HIST §21
  l.1402-1407 and HIST_LOG l.91-93. The A2/A3 FAIL stands everywhere (§21, §22 l.1419, HIST_LOG l.88-90).
- **Criteria against script: I found no undisclosed mismatch.**
  - ε (i: levels 0-1; ii: levels 1-2; op norm via 2sin(θ/2)), E_𝒞, E^lin normalisation (|X|²_HS = |a|²/2), the A3 floor and
    fit range, the B2 tolerances, and C3's level-0 axial gauge all match.
  - The pre-run crash fixes and the smoke run are disclosed.
- **Are A2/A3 really an artefact? Yes.**
  - Seed 2's R_lin = 6.6·10⁻⁴, and h6b's additive error is 1.344t·√E at every t from 10⁻⁴ to 10⁻².
  - So D_rel ≈ 2·1.344t/√R_lin·(…) ≈ 100t. That predicts 0.25 at t = 0.0025 against the measured 0.216, and h6b's D_rel →
    9.3·10⁻³ at t = 10⁻⁴.
  - The additive form is what (AE)'s proof uses. In units of ε (≈ 3.1t for seed 2) the additive constant is ≈ 0.43.
- **Scope notes (for the reader, not defects).**
  - (i) h6 A is depth 2. It cannot see the k-fold marginality, which is the whole issue for (SQ)/(MS-Sob). No d = 4 check
    of depth-uniformity of the ADDITIVE constant exists.
  - (ii) C2's maximum (8.4 → 8.7) is set by the smooth family's TOP-level axial links, which are depth-independent by
    construction. Depth-uniformity of the downward steps is shown by the noise family alone (1.0-1.8).
  - (iii) For C-smooth, complete axial gauge on the level-0 box is far better than MSG (C_ax = 0.045-0.060 against 5.3-8.7
    at k = 5). C3's contrast is a noise-family statement, as HIST says (l.1399-1401).
  - (iv) The chains are generated bottom-up (U_{i+1} = W_0(M̄)e^{tr}), not minimiser chains. That is fine, because MSG and
    (AE) are for every chain.

### Re-run
Setup:
- The numeric lock was taken by `until mkdir …/locks/numeric; do sleep 20; done`, after waiting for another holder. It was
  taken at 01:35:12 UTC and released by a single `rmdir` at the end of the wrapper at 01:37:49 UTC (no trap, no second
  release, exit 0). The lock directory present afterwards belongs to a later holder.
- Load 2.87 (< 8, checked inside the lock), 38% free memory, nice 10, OMP/OPENBLAS/MKL/vecLib threads 1,
  PYTHONDONTWRITEBYTECODE = 1, python3 without -I, no `timeout`, sequential. Outputs went to the scratchpad only.

| Run | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| h6_msg_cone.py | OVERALL FAIL (A2, A3); A1, B1-B3, C1-C3 PASS; max C_meas 3.534; C(5) 8.655 | 139.1 s | 706 MB | identical except runtime lines (`diff`) |
| h6b_diag.py | additive-error slopes 1.017 / 0.998 / 1.005; seed 2 D_rel(10⁻⁴) = 9.279·10⁻³ | 17.8 s | 642 MB | identical except runtime |

---

## Corrected tally (session 3)

| Item | Claimed | Verdict |
|---|---|---|
| Theorem MSG | PROVEN-HERE, counted | CONFIRMED-WITH-FIX (S3-1: axis order or A_ax = 12; C_M = 66.1 unchanged) |
| Corollary MSG-loc | PROVEN-HERE (with MSG) | GAP as stated; MSG-loc' with the c_qα² term PROVEN (S3-2) |
| Lemma MS-HLS | PROVEN-HERE, counted | CONFIRMED (state d = 4; S3-3) |
| MS-Sob ⇐ (SQ) | CONDITIONAL | valid implication from a FALSE premise; re-label ARGUED (deviation chain) (S3-4) |
| (AE) ⇐ MSG + MS-Sob | ARGUED | CONFIRMED as ARGUED; session-scale to promote |
| (SQ) | OPEN | OPEN, in the deviation form, together with MSG-loc-dev |
| k-fold example | PROVEN-HERE, uncounted | CONFIRMED (exact in the linear abelian case); MS-Sob holds on it |
| Corollary CLS-cone | CONDITIONAL ⇐ (AE) | CONFIRMED (scope S3-5: one level / one step) |
| (I_k^E)' | HYPOTHESIS | S2-1, S2-3 repaired; S2-2 repaired up to S3-7; new item (a5) needed (S3-6) |
| §20.0, W1-W3, (a') (1)(2)(4), (b') (1)-(4) | PROVEN, uncounted | CONFIRMED ((b') after S3-7) |
| h6 / h6b | FAIL as pre-registered / post hoc | honest; reproduced |

- **Session 3: 2 PROVEN-HERE (MSG, MS-HLS) / 1 CONDITIONAL (CLS-cone) / 2 ARGUED ((AE) ⇐ MSG + MS-Sob; MS-Sob ⇐
  MSG-loc-dev + MS-HLS + SQ-dev) / 1 OPEN ((SQ-dev), incl. MSG-loc-dev) + HYPOTHESIS (I_k^E)' (replaces).** Claimed 2/2/1/1.
- **Whole file: 9 PROVEN-HERE / 4 CONDITIONAL / 8 ARGUED / 4 OPEN + 1 HYPOTHESIS.** Claimed 9/5/7/4 + 1.
  - CONDITIONAL: RS-joint, HIST-sum, CLS-red, CLS-cone.
  - OPEN: (AE), (SQ-dev), (D1-b), (H-w).
- Targets: S4 **MET** (with S3-1). S5 **MET in reduction form, with fixes**, as claimed except that the chain to (SQ) is
  ARGUED, not proven.
- Main-path count if placed in PROOF.md: +2 (MSG, MS-HLS). Neither closes a wall by itself.

## Binding fixes (next lane-D session)
1. **S3-1.** In MSG's construction, take the axial order with P's two plane directions first (or put A_ax := 2(2L - 1) +
   (d - 3)(L - 1)). Update (S1). C_M = 66.1 is unchanged.
2. **S3-2.** Restate MSG-loc with the per-level term c_qα_{cell}², c_q = 66A_de^{4C_*ε}/L². Say that the global ε absorbs it
   only in sup form, and that in ℓ⁴ it is the d = 4-marginal non-abelian term.
3. **S3-3.** MS-HLS: state d = 4. Put the neighbourhood (5^d) and indexing (L^d) constants into C_Q.
4. **S3-4.** Re-label "MS-Sob ⇐ (SQ)" as ARGUED via MSG-loc-dev + MS-HLS + SQ-dev. Keep the curvature-source implication as a
   vacuous remark. Name MSG-loc-dev (the deviation-source localisation of the gauge) as part of the OPEN wall. Correct §22,
   §23 and HIST_LOG's tally to 9/4/8/4 + 1.
5. **S3-5.** CLS-cone (c): state the single-level (1/24) and one-step re-seeding (1/576) forms. Say that mixed-level defect
   sets need disjoint footprints (else k-fold). Remark on C_cone ≳ 10¹² and the g² requirement it puts on RLARGE.
6. **S3-6.** (I_k^E)': add item (a5), analyticity of the localised main term on 𝔇_α (unique nondegenerate localised minimiser,
   analytic continuation of its critical value). The inf/measurable-selection definition is used only off the small-field
   region.
7. **S3-7.** (b'): U = V_be^{Z_b} with Z_b Hermitian traceless (not e^{iZ}).
8. **N-4.** CLS-red display (l.1027-1028), η_E's dependence on C'_AE, and η_E ≤ η_AE.
9. **Literature pointer (optional).** In the MSG comparison, cite CMP 109 (1.15)-(1.16) (text l.574-590): Balaban builds U_n(V)
   in axial gauges on nested domains Ω_n with per-scale plaquette bounds |dU_n - 1| < α_0ξ². This is structurally the closest
   analogue of MSG. His regularity (|J| < ε_0, J = η⁻²Im dU) is a sup smoothness condition in coarse units, stronger than
   MSG's per-level-ε hypothesis [read-skim].

---

## Strategic verdict

- **MSG is a real, correct, depth-uniform theorem. It retires (CS-F2) for sup norms.** It is cheap in hindsight: given
  ε-smallness at every level, spreading coarse links over the centre segment contracts inherited sizes by exactly 1/L.
- **(SQ) is the right d = 4-critical wall, provided the main path really needs the ENERGY form (AE).** The session-3 chain
  shows precisely where the marginality sits:
  - The sup bounds are fine (MSG).
  - The scale-invariant HLS step is fine (MS-HLS).
  - What remains is to show that the per-level sources, both linear (curvature deviations) and quadratic (BCH, S3-2), are
    ℓ²-summable across levels by an energy.
  - Its linear part is a discrete Littlewood-Paley / multilevel norm-equivalence bound, known in kind and plausibly a
    session.
  - Its non-abelian part is the multiscale analogue of Uhlenbeck's L⁴ gauge estimate. That is multi-session, and should not
    be scheduled as one step.
- **MS-Sob's ARGUED neighbour ((AE) ⇐ MSG + MS-Sob) is session-scale.** Promote it only after (SQ-dev)'s linear case is
  written, because its constant bookkeeping (C_S, η_AE, ε_M ≈ 7·10⁻⁶) fixes how small η_E and 1/C_cone become.
- **Recommended order.**
  1. Fixes 1-8 (short).
  2. **Before attacking the non-abelian (SQ), have the lead check what the main path consumes.**
     - RLARGE/PLD consume CLS-cone only as a per-defect energy PRICE.
     - Balaban's scheme prices large fields scale by scale under SUP regularity conditions at each scale (CMP 109 §1
       [read-skim]), and those conditions are what MSG handles.
     - If a per-scale price (a defect at level j paid at the level-j integration, as §7's history bookkeeping already
       organises) suffices, then the energy-based (AE) and (SQ) leave the critical path, and CLS-red/CLS-cone remain
       off-path classical results.
     - If the energy form is genuinely consumed (for example by (a3)/(a4) of (I_k^E)'), keep (SQ-dev).
     - [inference; this needs the lead's reading of RLARGE §8 and PLD.]
  3. If (SQ-dev) stays on the path: write its linear case (LP for (Q_2, I_2) with residual sources). Then add an h7 check of
     the ADDITIVE (AE) constant's depth dependence on smooth fields, in d = 2 at depths 1-5 (d = 4 depth 3 is ≈ 2·10⁶ sites
     and needs the memory cap checked first). Only then attempt MSG-loc-dev.
- **Do not:** count the curvature-source MS-Sob ⇐ (SQ) as progress, or treat MSG-loc's sources as the (SQ) sources.
