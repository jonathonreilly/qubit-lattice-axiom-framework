# REVIEW_S18_S19: hostile review of sessions 18 and 19 (R1617 fixes, RLARGE repair, LINEAR_PACKAGE v1; N5-triv; RW, N5-sf0)

Reviewer: an independent agent that wrote none of the proof. I edited no other file. No commits, PRs or pushes.

Inputs:
- REVIEW_S16_S17.md (format; its 12 binding fixes).
- `diff PROOF_session17_snapshot.md PROOF_session19_snapshot.md` (445 lines). PROOF.md is byte-identical to the session-19
  snapshot (`cmp` empty). Read by offset: headers l.1-40; N5 node l.2135-2137; tally l.4498-4529; [S17] pointer
  l.5033-5041; the [S18] block l.5046-5136; the [S19] block l.5140-5393; N2-exp l.2777-2790; NA-alg l.2914-2945;
  NA-lev (c)-(d) l.3395-3420.
- `diff RLARGE_session17_snapshot.md RLARGE.md`; RLARGE.md §0 header, §1, §1A, §5 (d), §7.1-§7.4, §8, §9A, §10-§12 read in full.
- LINEAR_PACKAGE.md (all 500 lines; pointers spot-checked against PROOF_session16_snapshot.md).
- RTARGET.md §40-§43; LOG.md sessions 18-19 (l.812-905).
- checks/c33_*, c34_*, c35_* (criteria, scripts, records, stored outputs); all re-run (below).

Scratch work (re-runs, lock wrapper) is in the scratchpad directory `rev1819/`.

---

## Bottom line

- **The R1617 fixes are applied correctly.** The B_4 step of R1 (iii) is now right: I re-derived the bijection
  τ ↦ Rτ on unfattened tuple supports, and c33 B (all 384 elements of B_4) re-runs identically. R-3a, R-4, R-5, R-6, the
  two-threshold R-operation, Z_ref, (SF-last), (RLF-5), CL-1, (P4) → ARGUED and the four new named hypotheses are all
  present and stated precisely. **Theorem TS + Theorem R1: CONFIRMED-WITH-FIX** (constants-level). The 67 → 68 restoration
  is justified.
- **Theorem N5-triv (S18): CONFIRMED.** I re-derived Lemma CT, N5-sl, N5-coer, N5-loc, the product-rule bound 𝔇 and the
  three conclusions. Two optional sharpenings (a factor 2 in N5-coer, the torus constant M').
- **Theorem RW (S19), with CT♯ and RW-triv: CONFIRMED-WITH-FIX.** The walk identity, the walk bounds, the square root, the
  decoupling and the locality are all right. One statement is too broad: (iv) says 𝒞(s) "has the same properties". For
  s ≠ 1 it is neither a square root of K^{-1}(s) nor symmetric; only the bounds and the decoupling carry over.
- **Theorem N5-sf0 (S19): CONFIRMED-WITH-FIX**, as an existence theorem.
  - r_*, S_* are not computed, so ε_* is not explicit. RTARGET §42's pre-registered "explicitly stated ε threshold" is
    therefore only partly met.
  - The proven "gap" is ≈ 10⁻⁸¹ (product rule) or ≈ 4·10⁻⁵¹ (with N5-w0). That should be said wherever "gap" is claimed.
  - Two R_g-orientation typos.
- **Proposition N5-sf_i is correctly NOT counted.** Its hypothesis (NA-H_loc) also presupposes the level-i SU(N) background
  minimiser (B-NA/N2), which should be said.
- **Lemma N5-w0 (not counted): CONFIRMED-WITH-FIX.**
  - The exact part (ν_w = 30/13) is exact, rational and reproduced.
  - The rate m_cov^num = 1.93·10⁻¹⁰ rests on floating-point entries and sums with a heuristic (1 + 10⁻⁹) factor and no
    rounding control. It is a numerical verification, not a rigorous computer-assisted proof, until C2 is redone in
    exact rationals or interval arithmetic. Everything that uses it (the second ε_* value) inherits that label.
- **LINEAR_PACKAGE v1: NOT YET public-ready, but close.**
  - Every R1617 item landed.
  - Two sentences are misleading (§9 "fluctuation covariance … OPEN", stale since S18-S19; §9's partial list of unread
    Balaban papers).
  - Four symbols are undefined (ε_1/B in the BG-b row, which clashes with Theorem 5.1's B; ||·||_B; Phys^{(k)}; Z_ref).
  - Two bibliography entries are incomplete.
  - A v1.1 errata (no mathematics) fixes all of it.
- **Checks re-run.** c33 A/B, c33 diag, c34 A/B/C and c35 A/B/C re-run identically, except timing (c33 A again FAIL as
  pre-registered, the same float artefact; the 40-digit diagnostic is reproduced).
- **No IMPORTED-NOT-YET-REVERIFIED item is load-bearing** for any S18/S19 PROVEN claim.
- **Corrected tally: 71 / 2 / 7 / 24 + 1, as claimed.**

---

# PART 1: session 18

## [R1617-fix] audit (REVIEW_S16_S17 binding fixes 1-12)

| # | Fix | Where now | Verdict |
|---|---|---|---|
| 1 | R-3b: tuple localisation, c33 | RLARGE §7.2 (i) tuple form, (iii); §9A | **Applied correctly** (see below) |
| 2 | R-3a / R-4 / R-5, g² < a''/3 | Lemma 7.2-0; §7.2 (iv); §7.3 | Applied. Two constants-level fixes (F1, F2 below) |
| 3 | R-6 narrowing | RLARGE l.14, 200, §7.2 Reading, §7.4; PROOF l.5033-5036; LOG l.793-796 | Applied. The [S17] pointer text l.5032 is kept and annotated, which is fine |
| 4 | R-1 / R-8: two thresholds, one exponent | §1A items 1-2, §7.1, §8.2 (W1-ret'), §8.3 steps 3-4, (P1) | Applied. a_♯ uses c_RS = 5⁴, which is ARGUED; n_♯ is a definition, and no counted item depends on it (R1 holds for every n_c ≥ n_*). Say so where n_♯ is defined |
| 5 | R-7a / R-7b | (H-Mayer), (H-pos) [P] in §8.2, §11 items 6, 6a | Applied |
| 6 | R-2, R-9 | (RLF-4) Z_ref; (SF-last); (HIST) ordering; §8.3 step 6 | Applied. Z_K^{sf,ref} is defined by pointer to node A's (unwritten) normalisation, so "L6-soft for this normalisation" is a statement about an object that node A must still define. That is acceptable for a target, and it is labelled [inference] |
| 7 | (P4) ARGUED; (P1) count; §8.5; complex fields | §8.4, §8.5, (RLF-5) | Applied. (P1) now uses 80^{2(n-1)} with 6400C_ℓe^{-a_♯/g_K²} ≤ ½, which is consistent |
| 8 | R-10 | §7.1 [inference] | Applied |
| 9 | CL-1 | §5 (d) | Applied, and derived: Λ_1 = 6 + 8κ(2 + C_𝒩) (multiplicity 8, two occurrences per contour from the back-tracking). This is the same multiplicity that N5-loc reuses (Σ_c|Q(c, b)| ≤ 16), so the two are consistent |
| 10 | PROOF title, header, §3 tally | l.1, l.22-40, l.4498-4529 | Applied |
| 11 | LINEAR_PACKAGE | v1 | Applied item by item (Part 3). Remaining issues are listed there |
| 12 | LOG source of the S17 direction | LOG l.813-819 | Recorded, second-hand ("as relayed by the session-18 brief"). I take no position on governance |

## Theorem R1 (iii), the repaired B_4 step: CONFIRMED (RLARGE l.370-492, step at l.446-458)

- **Action.**
  - R ∈ B_4 acts about the block centre c_x by z ↦ c_x + R(z - c_x).
  - Block centres are c_y = Ly + o with L odd, so c_x + RL(y - x) = c_{x+R(y-x)}. The block {-(L-1)/2, …}⁴ is B_4-invariant
    about its centre, so blocks map to blocks and sites to sites.
- **The family is permuted.** I checked each of the four ingredients:
  - (a) r_{RY}(R·D) = r_Y(D), by CL (e): the S4' family and the cuts are B_4-symmetric;
  - (b) R preserves the cube sup-distance, so the touching graph satisfies G(Rτ) = G(τ) and φ^T is unchanged;
  - (c) N, |S| and supp transform correctly;
  - (d) R fixes x, so x ∈ RS ⇔ x ∈ S.
  - Hence τ ↦ Rτ is a bijection {supp = S, N} → {supp = RS, N}, term by term, and F_S(R·D) = F_{R^{-1}S}(D). This is
    exactly GT-lat' (ii)'s hypothesis. The 384-element group order is right (2⁴·4!).
- **Tuple form = X-majorant.** The overlap graph of (Ŷ_i) equals the touching graph G(τ) (the hard-core equivalence of (i)),
  so ρ^T(g(X)) = φ^T(G(τ)) termwise. With r' ≥ 0 the τ-majorant sums to the X-majorant exactly, and supp τ ∋ x ⇒ ∪Ŷ_i ∋ x.
  So the bound 2κ_0Bc_0K_0 is right.
- **Locality.** S is *-connected with |S| ≤ n_c, so it lies within n_c - 1 cubes of x. The r_Y see blocks of Y and their
  *-neighbours, at fine sup-distance ≤ n_cL + (L-1)/2 < R_* = (n_c + 2)L. Correct.
- **Torus.** For T_j ≥ W = 2n_c + 5, the relevant box spans ≤ 2n_c + 1 < T_j - 1 cubes, so touching is the Z⁴ relation, and
  2R_* + 1 ≤ T_jL - 2 for L ≥ 3. Correct.
- **Wrap levels (iv).** |ℛ^w_x| ≤ 2κ_0Bc_0K_0e^{-a''/g²}, from (i) with N ≥ 1 and 1/|S| ≤ 1. The number of cubes is
  ≤ (L⁴/(L⁴ - 1))W⁴, and g_j ≤ g_K. Correct.
  - Note that W⁴ ≈ (2·10¹³)⁴ is absorbed into the g-independent C of (RLF-4). That is legitimate, and worth one sentence.
- **Remark 7.2-B (ARGUED, not counted): accepted as ARGUED.** Centre independence of the Hessian on reference data uses
  DF̃(0) = 0 and the linearised gauge invariance, which is fine. c33 A5/B4 are consistent with it.

**F1 (Lemma 7.2-0 / C_♮, constants).** The S18 note correctly observes that C_♮ = 3 covers the data but not the chart ball
over which K_F is a supremum. "C_♮(R_*) chosen so that …" asserts a constant without saying why one exists. Add one line:
ε_♭(·; Y) is Lipschitz in the tree coordinates on the chart ball, with constant C'(R_*) (finitely many links, smooth
functions), so C_♮ := max(3, C'(R_*)C(R_*)) works.

**F2 (notation).** §7.2 (iv) writes T_j = T·L^{K-1-j} with T the level-K side, while §1A writes T_k for the level-k side in
level-k cubes. Use one convention.

## Theorem TS (repaired; RLARGE l.494-540): CONFIRMED

- (R1)_i is now global on each inner level, which is the honest reading of R1's gas identity.
- (b1)-(b2) are on Δ_{*,n} (the R_*/L + 1 neighbourhood), with the box-overlap factor (2R_*/L + 3)⁴ in C_TS.
- The coupling window g² < a''/3 is stated, and d log w/dg = -6/g + 2a''/g³ is right.
- I re-derived the two level-n totals, 3M_2ō_n·overlap (via L^{4n}σ_n⁴ = 1) and M_2³σ_n²·(2R_*/L + 3)⁴·overlap (via
  |Δ_{*,n}|σ_n⁴ ≤ (2R_*/L + 3)⁴). Both are right.
- The "box merging" step (ε_3 on B̂_* from a chain of cube boxes) is written at constants level, which is adequate.
- Role: TS is the frozen shadow and is not used by RLF-step. Stated (§7.3 "Role").

## The inductive step (§8): still CONDITIONAL, with one further unnamed point (not counted, no tally effect)

- **G5 (new).**
  - Step 2 applies Theorem R1 "on the locally small part r^s, pointwise in the sample". But Theorem R1's hypothesis (H-ch)
    is global on the level (§7.2 Setting; TS states it globally on purpose).
  - In a sea sample (H-ch) fails with density e^{-c/g²}, so R1 is not applicable as stated. What is needed is a version of
    R1 for the gas of r^s = r·1{local smallness}, with (H-ch) required only on the boxes B̂_*(x) of the supports used.
  - The proof of (ii) appears to localise (it uses B̂_*(x) only). But two things have to be said:
    - The Taylor step is applied to the smooth r_Y, not to r^s.
    - The indicator is constant on the chart ball, which is the same C_♮ argument as F1.
  - Name this as part of (H-pos)/(W1-ret'), or state R1-loc.
- **Interface remark (N5 ↔ RLARGE).**
  - N5-sf0's background class requires plaquette curvature and soft fluctuation ≤ ε_* ≈ 10⁻²⁴/C_Δ. RLARGE's small-field
    cubes are defined with ε_1 ≤ 2 and ε_loc ≈ 3.5·10⁻³.
  - For the small-field package to cover RLARGE's small-field region, the R-operation's thresholds must be ≤ the N5
    threshold in matching units. Then a'' ∝ ε_1² and n_♯ become astronomically larger, still g- and K-independent.
  - This is not a gap, because only finiteness is used. Record it as a compatibility condition in RLARGE §1A item 1, or in
    the (SF) hypothesis.

## Theorem N5-triv (PROOF l.5046-5136): CONFIRMED

- **Lemma CT (l.5061-5068).**
  - The commutator kernel is |K|(e^{m|f(x)-f(y)|} - 1) ≤ |K|(e^{md} - 1). The Schur test on the symmetric majorant gives
    ≤ γ/2 ≤ (γ + t)/2. So the inverse norm is ≤ 2/(γ + t), and entry ≤ norm.
  - The square root comes from π^{-1}∫t^{-1/2}(K + t)^{-1}, using ∫t^{-1/2}(γ + t)^{-1} = π/√γ.
  - Correct, and the rate is uniform in t.
- **Lemma N5-sl (l.5070-5079).**
  - w(b_0) ≥ (L - 1)/(8L): 6 of the 24 orders start in direction 1, and y_1 > c_1 for ((L - 1)/2)L³ sites. Monotone axial
    paths never use b_0 backwards. Correct.
  - Σ|w| ≤ the maximal path length 2(L - 1). The bounds n_Π ≤ 1 + 128L²/(L - 1) and D_m(|Π|) are right.
  - c34 A gives w(b_0) = 10/81 ≥ 1/12 and ||w||² = 104/729.
- **Lemma N5-coer (l.5081-5091).** I re-derived all four steps:
  - T = P_resΔ_0|_{Λ_res} ≥ ν_N, from the per-block Neumann gap on zero-mean λ (2(1 - cos(π/L)) is the product-graph gap);
  - h(dλ) = avg λ - λ(c) = 0;
  - P_resd*A_P = 0;
  - Q(dλ) = d(ev λ) = 0;
  - ||Tλ||² ≥ ν_N⟨λ, Tλ⟩;
  - the use of NA-lev (c) (l.3405-3412) in PG normalisation, which gives the factor 2min(c_E, κ_i/2)c_1L^{-2}. Correct.
  - **Optional sharpening:** A_P ⊥ dλ, since ⟨A_P, dλ⟩ = ⟨d*A_P, λ⟩ = 0 (d*A_P ∈ Λ_res^⊥, λ ∈ Λ_res). So
    ||A||² = ||A_P||² + ||dλ||², and the ½ in γ_i is unnecessary. γ_i doubles, which also matches PG's "O_FP ≥ min(c_PG, 4)
    on H_0" with no ½.
- **Lemma N5-loc (l.5093-5106).**
  - H_i = -κ_{i-1}(𝓡_i + 𝓡_i^T)/2 follows from E_i = -(κ_{i-1}/2)⟨𝓡B, B⟩ (stationarity). Correct.
  - Row sums: 4κ_+M coth⁴; 24 for d*d (6 + 6·3); 16p_L for Q^TQ (≤ 8 coarse links, ≤ 2 uses each; contour length p_L); 32
    for dP_resd* (2·2·8; P_res rows ≤ 2 via the orthonormalised span(δ_c, 1_B)).
  - Ranges: p_L = 5L - 4 (the ℓ¹ diameter of two adjacent blocks) and 4L - 2. All correct.
  - **Optional:** N2-exp (ii) (l.2784) writes the torus bound with M', not M. N5-loc's "no larger" is right for the
    periodisation, but with N2-exp's constant. Write M' (or note M' = M).
- **Theorem (l.5108-5130).**
  - Π commutes with Õ, and Õ ≥ min(γ_i, 1).
  - 𝔇(m) is exactly the three-factor product rule with N_m(|Π|) ≤ p_m, N_m(|O_i|) ≤ S_O + E_O, plus D_m(|1 - Π|) ≤ δ_Π.
    𝔇(0) = 0 and it is continuous.
  - (i)-(ii): Lemma CT plus the block-local (1 - Π) term.
  - (iii): Σ_{b'}𝒞_i(b, b')² = C_i(b, b) ≤ 1/γ_i, and the ℓ¹ bound via coth⁴.
  - Uniform in i, k, T: every constant is from (L, κ_±, c_E^-, M, m'). Correct.
- **Inputs.** NA-lev (c), E-low, PG, N2-exp', LED-dual and FP-ab are all PROVEN-HERE and reviewed. No imported item is used.
- **c34 re-run:** A, B, C identical (Part 4).

---

# PART 2: session 19

## Setting N5-bg, Lemma N5-cov (l.5149-5181): CONFIRMED

- The entry ranges are right:
  - Õ(b, b') ≠ 0 only for blocks at ℓ^∞ distance ≤ 1, so d ≤ r_1 = 8L - 4;
  - the variables lie within ℓ^∞ distance 2 (3 for the coarse links' far blocks);
  - Π_U is block-diagonal because w_X^U lives on links with both ends in B(X).
- The trivial-background identity Õ(1, 1) = Õ_0 ⊗ 1 holds. Re tr(1 - e^F) = ½|F|²_HS, and φ̂ = Nφ has zero gradient at the
  minimum, so the second-order part of log W_0 does not enter. c35 A2 confirms it to 2.6e-15.
- **N5-cov.** e^{Ad(g(x))A}g(x)U_bg(y)^{-1} = g(x)e^{A}U_bg(y)^{-1}. M̄ covariance, W_0 covariance (unique maximiser),
  φ(gV; gM) = φ(V; M), and the slice/residual covariances h_{gU}R_g = A_gh_U and P_res^{gU} = Ad_gP_res^UAd_g^{-1} all hold.
  The complex extension (identity theorem on a totally real set) is right. c35 A1: 2.4e-14.

## Lemma AX (l.5183-5200): CONFIRMED

- The plaquette-move count is Σ_{ν>μ}(x_ν - o_ν) ≤ 3(ℓ - 1), inside the box.
- The bi-invariant distance has the triangle inequality, and d(W, 1) ≤ |log W| when log W ∈ su(N).
- The principal-log argument holds: |X|² ≥ Σθ_j² for every log, no eigenvalue -1, and |Σθ_j| < 2π ⇒ Σθ_j = 0. It needs
  3(ℓ - 1)ε < min(π, 2π/√N), which is stated.
- Coarse links: y + 9.2y² ≤ 3y for y ≤ 1/20, and (gV)_c = W_0e^{-ρ}. So 3y + ε ≤ α. Correct.

## Lemma N5-an (l.5202-5221): CONFIRMED as an existence statement

- The composition argument is sound:
  - the Wilson part and h_U, M_U, D_U are polynomial in Ad entries;
  - the block-diagonal inverses are nonsingular at U = 1, where M_1 is onto by NA-FP (ii);
  - X_0(M) is real-analytic by the analytic IFT, with Lip ≤ 0.23 from NA-alg (a);
  - φ is a polynomial in (V, M, W_0) (NA-alg (b));
  - real-analytic ⇒ holomorphic on a polydisc with finite sup.
- Finitely many entry types modulo L-translations, so r_*, S_* are uniform, with no T-dependence once T ≥ 5. The Schwarz
  step (2S_*/r_*)α and the row count n_1 = 4(3L)⁴ are right.
- What it does not give: numbers. It is honestly labelled "existence; not computed".

## Lemma CT♯ (l.5223-5238): CONFIRMED

- The bounds are right:
  - ||(K + t)^{-1}|| ≤ 1/(γ - δ + t) by the Neumann series around K_0 + t;
  - the spectrum lies in Re z ≥ γ - δ, since dist(z, [γ, ∞)) > δ;
  - the block Schur test on the symmetric majorant |K_0| + |Δ| holds. |K_0| is symmetric because K_0(y, x) = K_0(x, y)^T has
    the same operator norm.
- The square root by Riesz-Dunford is right: it squares to K^{-1}, and it is the spectral root when K is real symmetric.
- Holomorphy in parameters is right.

## Theorem RW (l.5240-5287): CONFIRMED-WITH-FIX

- **(i).** I re-derived each step:
  - (K + t)G_□ = 1_Ω + 1_{Ω^c}KG_□, because G_□ is supported in Ω, so the t-term vanishes off Ω;
  - multiplying by 1_□ and summing gives 1 - R;
  - the bound |R_□|(x, y) ≤ (2S_m/(γ' + t))e^{-md(x,y)}1[d > RL];
  - the weight e^{m_1d} with e^{-ad} ≤ e^{-aRL/2}e^{-ad/2}, and Σ ≤ 4coth⁴(a/4). This gives ε_R(t) exactly as stated.
  - N_0 < 1 is the ℓ^∞ operator norm, and in finite dimensions the right inverse is the inverse. Correct.
- **(ii).** Σ_{|ω|=n}|T_ω| ≤ |P|(Σ|R_□|)^n entrywise. N_{m_1}(|P|) ≤ 8coth⁴(a/2)/(γ' + t), and
  M(AB^n) ≤ N(A)N(B)^{n-1}M(B). Correct.
- **(iii).**
  - K + t is invertible for all t ≥ 0, so σ(K) ∩ (-∞, 0] = ∅ and the functional calculus applies.
  - The real symmetric case gives μ > 0.
  - λ_min ≥ γ'(1 - ε_R)/(8coth⁴(m/2)) via (ii) at m_1 = 0. The m_1 = 0 value of ε_R is smaller than the stated one
    (e^{-aRL/2}coth⁴(a/4) decreases in a), so the stated ε_R may be used. Correct.
- **(iv).** R_□1_{□'} = 0 for □ ≠ □', and s_{□'}R_{□'} = 0 ⇒ R(s)1_{□'} = 0 ⇒ K^{-1}(s)1_{□'} = G_{□'}1_{□'}. Correct, and exact
  (c35 B5: 0.0).
- **(v).** The variable count and the 7⁴ neighbour count are right (□_{j-1} must contain a block at ℓ^∞ distance R + 1 from □_j).
- **Fix RW-1 (statement (iv), l.5261-5262).**
  - "𝒞(s) … has the same properties with the (iii) bounds" is too broad. For s ∉ {0, 1}^𝒫, K^{-1}(s; t) is not a resolvent
    (P(t), R(t) depend on t). So 𝒞(s)² ≠ K^{-1}(s; 0) in general. 𝒞(s) is not symmetric, and not positive for real
    s ∈ (0, 1).
  - What carries over is: holomorphy, the M/N bounds with s̄ε_R, 𝒞(1) = K^{-1/2}, and the column decoupling.
  - That is exactly what Balaban-style use needs, with the field written A = 𝒞(s)Z, Z white noise. Say so; do not imply
    that 𝒞(s)² is a covariance.
- **Remark RW-2 (not a defect).** Theorem N5-sf0 fixes R_* by ε_R ≤ ½, so only s̄ < 2 is available. A cluster expansion
  in s needs s̄ ≫ 1 (Cauchy gains). The R in (iv)'s use must be chosen larger, with s̄ ~ ε_R^{-1/2}. The theorem allows
  this; N5-sf0's stated R_* does not.
- **Corollary RW-triv (l.5288-5295): CONFIRMED.**
  - S_m = p_m²(S_O + E_O) + (n_Π - 1)e^{4m(L-1)} is N_m(|Π||O||Π|) + N_m(|1 - Π|).
  - Compressions keep the gap (Rayleigh) and D_m (monotone).
  - R_triv solves ε_R ≤ ½ with a = m_cov/2.
  - The no-wrap remark is right: T < 2R + 1 ⇒ Ω_□ = the torus ⇒ R = 0.

## Theorem N5-sf0 (l.5297-5349): CONFIRMED-WITH-FIX (existence theorem)

- **Constants.**
  - γ_0 = c_1min(½, κ_-/2)/L², with c_E = ½ trivially at i = 0. Note that "ν_N ≥ 1" holds only at L = 3; elsewhere the
    min is still the c_1 term.
  - α_* gives CT♯'s condition: 𝔇_0 + (e^{mr_1} - 1)C_Δα ≤ (γ_0 - C_Δα)/2 ⇐ C_Δαe^{mr_1} ≤ γ_0/2 - 𝔇_0.
  - γ' ≥ γ_0/2. Correct.
- **(a).**
  - Ω^+_□ spans ≤ 4R_* + 5 < T_0 blocks, so there is no wrap.
  - AX's hypotheses follow from 10p_Lℓε ≤ α_* ≤ r_* ≤ 1/(20p_L).
  - The complex neighbourhood: |log(e^Xe^Y)| ≤ 2(|X| + |Y|) for |X| + |Y| ≤ ¼ (HS submultiplicative), and real g preserves
    |z|. Correct.
- **(b).** (RW1): CT♯ on each compression in the gauge g_□. Δ_□'s variables lie in Ω^+_□ (R + 2 for links, R + 3 for the
  far blocks of coarse links). Its block norm is ≤ N_0 (symmetric majorant). (RW2) is row-wise in g_□. The bounds, the ℓ¹/ℓ²
  forms, positivity, holomorphy (uniform limits) and locality all follow. Correct.
- **Fix SF-1 (typo, l.5324).** By N5-cov, Õ(U, V) = R_g^{-1}Õ(gU, gV)R_g, not R_g(·)R_g^{-1}. It is harmless, because R_g
  is block-diagonal orthogonal. The same applies in Proposition N5-sf_i (l.5355): R_g^{-1}Õ_iR_g should be R_gÕ_iR_g^{-1}
  (= Õ_i(g_□U, g_□V)).
- **Fix SF-2 (the "gap", l.5316, header l.10-13, RTARGET §43, N5 node l.2135-2137).**
  - The proven lower bound is λ_min ≥ γ'(1 - ε_R)/(8coth⁴(m/2)):
    - ≈ 7·10⁻⁸² at the product-rule m = 1.97·10⁻¹⁸;
    - ≈ 4·10⁻⁵¹ at N5-w0's m = 9.66·10⁻¹¹ (with γ' ≈ 1.19·10⁻⁸, ε_R ≤ ½).
  - It is positive and T-uniform, but it is 43-73 orders of magnitude below γ_0. State the number next to the word "gap".
- **Fix SF-3 (pre-registration).**
  - RTARGET §42 A required "an explicitly stated ε threshold". ε_* is explicit only up to the uncomputed r_*, S_* (through
    C_Δ, and through α_* when α_* = r_*).
  - RTARGET §43 "met for level 0" should read "met, except that ε_* is an existence constant (r_*, S_* not computed)".
  - The header l.11 says this correctly ("explicit up to …"). The §43 line does not.
- **Fix SF-4.** ν_w = 30/13 (l.5313) is the L = 3 value from N5-w0. The theorem is stated for general L, so write
  "(n_Π - 1, or ν_w = 30/13 at L = 3)".
- **Fix SF-5 (wording).** "Holomorphic on 𝔑(α_*)": 𝔑(α_*) is defined by closed conditions plus the existence of gauges.
  Say "holomorphic on a neighbourhood of each point of 𝔑(α_*) (N5-an's polydisc is closed with slack)", or state it on
  (a)'s parametrised neighbourhood z ↦ (e^zU, e^{z'}V), which is the form N10/RLF-5 uses.
- **Scope.** This is the level-0 (first RG step) operator only, at T ≥ T_0 ≈ 7·10¹². It is correctly scoped in "What it
  is and is not".

## Proposition N5-sf_i (l.5351-5359): correctly NOT counted

- It is a valid implication: CT♯ needs 𝔇 + 1.5δ_H ≤ γ_i/2, which the stated 2δ_H covers. The locality exception is
  correctly made.
- **Add:** (NA-H_loc) is a statement about Hess E_i^{NA} at (U, V). E_i^{NA} is defined by minimising the lower levels, so
  (NA-H_loc) presupposes the level-i SU(N) background minimiser and its regularity (B-NA / N2 / L2). It is not only a
  Hessian estimate. This places it inside B-NA, not next to it.

## Lemma N5-w0 (l.5361-5371; not counted): CONFIRMED-WITH-FIX

- **C1 is exact and reproducible.**
  - ||w||² = 104/729, Σ|w| = 8/3, max|w| = 10/81, so ν_w = (10/81)(8/3)(729/104) = 30/13. I checked the arithmetic.
  - The float rows of 1 - Π reproduce it to 1e-12.
- **C2 is not a rigorous computer-assisted computation.**
  - The 324 rows of Õ_0 come from floating-point matvecs (Π, P_res, Q in double precision).
  - N_0 and the first moment Σ|Õ_0|d are float sums with a (1 + 10⁻⁹) safety factor. That factor is heuristic: there is
    no rounding-error analysis, the zero test is |·| > 0, and float noise entries are counted.
  - The bound itself (41.077·m·e^{20m}, via e^x - 1 ≤ xe^x) is the right closed form. It avoids the exp - 1 cancellation
    that, as disclosed, corrupted the printed product-rule value.
  - Every entry is rational: d*d is integer, the S4' averages are rational, Π has denominator ||w||² = 104/729, and P_res
    is a rational projector. So C2 can be redone in exact rationals (≈ 324 × 26 244 entries), or with interval arithmetic.
- **Fix W0-1.** Until then, label N5-w0's rate "numerically verified (double precision, heuristic margin)", not
  "computer-assisted lemma". N5-sf0's second threshold (1.7·10⁻²⁴/C_Δ) inherits the label. The product-rule threshold
  (2.1·10⁻³²/C_Δ) is the proven one.
- **Measured γ values.** These are correctly labelled measurements. "Suggests that the loss is entirely in c_1" is
  correctly worded as a suggestion.

---

# PART 3: LINEAR_PACKAGE.md (FROZEN v1)

## Did every REVIEW_S16_S17 fix land? Yes

- **Statement table.**
  - P-2: Theorems 4.2 and 4.2' are separated (l.207-223).
  - P-3: Prop 3.3 has "provided M_2 ≤ ε_*" (l.178-180).
  - P-4: two κ̂'s (l.94-97).
  - P-5: "linearised abelian" (l.123).
  - P-6: O_FP "on H_0" (l.329).
  - "m_*' ≤ 0.1" (l.255).
- **The 13 sentences.**
  1. Pairing (l.70-75).
  2. = P-5.
  3. = P-2.
  4. Dimock differences listed and classified (l.290-307).
  5. Bibliography (§11).
  6. "observation … interpretation" (l.234-235).
  7. "If … ARGUED" (l.238-242).
  8. Double-fixing history replaced by the admissibility condition (l.324-325).
  9. OpenAI text removed: `grep` finds no "OpenAI", "owner", "lead" or "memory".
  10. [inference] label (l.467-468).
  11. Review status (l.12-15).
  12. §10 frozen as prose.
  13. Governance removed.
- **Other fixes.** P-1 (c28 C3/C4 separated, l.399). §9 (a)-(d) added. Lemma 4.4 renamed. A glossary §0. The companion
  snapshot is named.
- **Bibliography check.**
  - The seven Dimock arXiv ids match the downloaded sources (1108.1335, 1212.5562, 1304.0705, 1512.04373, 1712.10029,
    2009.01156, 2204.07201).
  - The Balaban volume, year and page data agree with the standard citations (CMP 95 17-40; 96 223-250; 98 17-51;
    99 75-102 and 389-434; 102 255-275 and 277-309; 109 249-301; 116 1-22; 119 243-285; 122 175-202 and 355-392).

## Remaining sentences / items (each blocks public release; none needs mathematics)

1. **§9 l.433-435** "The covariance of the gauge-fixed soft Hessian (ℓ¹ bound, random-walk expansion) is a different
   object and is OPEN."
   - This was true at the freeze (18:09; the N5-triv target was pre-stated after it). It is now misleading, because the
     trivial-background covariance, its random-walk expansion and the level-0 small-field case are proven in the ledger
     (S18-S19, now reviewed here).
   - The document is frozen, so issue a dated v1.1 note: "after this version: N5-triv, RW, N5-sf0 (ledger [S18]-[S19])".
2. **§9 l.429** "Balaban's CMP 102, 116, 119, 122 I-II were not read (CMP 109 was)."
   - This omits CMP 95, 96, 98, 99, which were not read either (§11: "bodies not read except CMP 109"). As written it
     implies they were.
   - Replace with "Of Balaban's papers only CMP 109 was read."
3. **§0 BG-b row (l.33).** "ε_* := (ε_1²/(4NB))^{1/2}": ε_1 and B are undefined in the package. B collides with Theorem
   5.1's B = C_Ke^{κ_0}K_0. Define both, or rename (e.g. B_LF).
4. **Prop 6.4 (l.339).** ||A||²_B is undefined; it means L^{-2}Σ_ba_b² in PG's normalisation. "One-level Phys" should be
   "Phys at n = L".
5. **Prop 6.3 (l.335).** Phys^{(k)} is undefined (the composite slice h^{(k)} = 0 with the residual fixing).
6. **§9 l.424.** Z_ref is undefined in the package. Say "a reference normalisation (RLARGE §1A (RLF-4))", or drop the
   symbol.
7. **§11.**
   - [D-II] and [D-III] lack journal names (their DOIs are J. Math. Phys. and Ann. Henri Poincaré). Add volume, year and
     pages.
   - [B95], [B96], [B102a], [B119] lack titles.
   - [D-QED*] are listed but never cited: cite them or drop them.
8. **Theorems 4.2/4.2' (l.207-217).** m_*, m_*' are defined through the strip conditions (P1)-(P7) and (S1)-(S7), which
   appear only in the snapshot. Since the snapshot "must accompany", this is acceptable. A one-line summary of what the
   conditions bound (ρ_β, e_Ψ, br_V, the f_0 condition) would make the main theorem self-contained.

**Verdict: NO, not yet.** The mathematics is faithful, and every R1617 item landed. Items 1-2 would mislead an expert,
3-6 are undefined symbols, and 7 is bibliographic. All of it fits a v1.1 errata with a change log, about one hour, no
mathematics. After that: **yes**.

---

# PART 4: checks (re-run)

Setup:
- Copies of the scripts in scratchpad `rev1819/`, so nothing was written into `checks/`.
- Each job behind the machine-wide lock (`mkdir …/locks/numeric`, `rmdir` after, on failure too); nice 10;
  OPENBLAS/OMP/MKL/vecLib threads 1; PYTHONDONTWRITEBYTECODE = 1; no `timeout`.
- Load (1-min) 2.4-3.7 before each job (< 8). Memory checked before each job; c35 only at ≥ 40% free (B/C were deferred once at 34% and run later at 41-42%).

| Part | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c34 A | PASS | 0.14 s | 28 MB | identical |
| c34 B | PASS | 0.29 s | 152 MB | identical |
| c34 C | PASS (24/24, ratios ≤ 0.488) | 0.19 s | 37 MB | identical |
| c33 A | **FAIL as pre-registered** (A1, A4, A5 on the constant seed, 2.9e-9) | 11.8 s | 75 MB | identical |
| c33 B | PASS (384 elements; tuple ≤ 1.2e-15; fattened 0.68-3.94) | 142 s | 63 MB | identical |
| c33 diag (40 digits) | 0, 1.08e-37, 2.97e-34 | 8.1 s | 77 MB | as recorded |
| c35 A | PASS | 83 s | 303 MB | identical (timing only) |
| c35 B | PASS (B0-B6; q = 1.39/0.377/0.106; decoupling 0.0; walk-root 7.2e-14) | 241 s | 1183 MiB (/usr/bin/time; script's own figure 1165 MB, at the 1.2 GB cap) | identical (timing only) |
| c35 C | PASS (C1-C4; ν_w = 30/13; m_cov^num = 1.9321e-10; γ_meas 0.039849, γ^LB 8.138e-3; m_meas 0.4328) | 67 s | 1088 MiB | identical (timing only; the printed 1.0093e-17 artefact is reproduced) |

Procedure and scope:
- **Order.**
  - c33: RLARGE §13 at 21:47 UTC, then the criteria, then the script.
  - c34: the criteria and the script were written in one command, criteria first, after the N5-triv text. This is
    disclosed. It is weaker pre-registration, but the criteria are bounds a lemma must satisfy, so it does not matter here.
  - c35: criteria before the script; a batch of pre-run script-only edits is disclosed.
- **No criterion edited.** c33 A's FAIL stands.
- **The c35 C2 printed product-rule m_cov is wrong** (1.0093e-17; expm1 gives 3.9457e-18). This is disclosed in
  c35_time.txt and the ledger uses the corrected value. The criterion margin (≥ 10⁷) is unaffected.
- **Scope.**
  - c35 A is a MODEL operator (κ|Q_UA|² for the soft Hessian), SU(2), on (Z/6)⁴, T = 2. That is below T_0 by 12 orders, so
    it tests the covariance identity and the analytic response, not N5-sf0's regime.
  - c35 B is d = 2 abelian. Its B7 shows the proven ε_R is ≥ 10⁵ at the tested R (the constants, not the mechanism).
- **No check would catch** an error in N5-an's existence argument or in RW (v)'s locality count. Neither is instantiable
  at these sizes, and I checked both by hand.

---

# Overclaims

1. **PROOF header l.10-13, RTARGET §43, N5 node l.2135-2137:** "gap" without its size (SF-2). "Met for level 0" without
   "ε_* is an existence constant" (SF-3).
2. **PROOF l.5361 / LOG l.886 / RTARGET §43:** "computer-assisted" for N5-w0's rate (W0-1). Only C1 is exact.
3. **PROOF l.5261:** 𝒞(s) "has the same properties" (RW-1).
4. **RLARGE §8.3 step 2:** "Theorem R1 (pointwise in the sample)" without a local-hypothesis R1 (G5).
5. **LINEAR_PACKAGE §9 l.433-435** (stale OPEN) and **l.429** (partial unread list): Part 3.
6. **Imported items.** None is load-bearing for an S18/S19 PROVEN claim. The literature notes on Dimock's random-walk
   statements are cited as context only, and RW is derived in full.

# Verdict counts and tally

**Counted items.**
- **S18, 2 items.**
  - Theorem TS + Theorem R1 (repaired): CONFIRMED-WITH-FIX (F1, F2: constants and notation).
  - Theorem N5-triv: CONFIRMED.
- **S19, 2 items.**
  - Theorem RW (with CT♯, RW-triv): CONFIRMED-WITH-FIX (RW-1, wording).
  - Theorem N5-sf0 (with N5-cov, AX, N5-an): CONFIRMED-WITH-FIX (SF-1 to SF-5; none affects validity).
- **0 GAP, 0 WRONG.**

**Uncounted items.**
- Proposition N5-sf_i: a correct implication; correctly not counted.
- Lemma N5-w0: CONFIRMED-WITH-FIX (W0-1, "numerically verified").
- Remark 7.2-B: ARGUED, accepted.
- RLF-step: CONDITIONAL, plus G5.
- (P1)-(P3), (P5): arithmetic CONFIRMED. (P4): ARGUED.
- c33, c34, c35: re-run as tabulated.

**Corrected tally: 71 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path)
+ 1 comparison branch, as claimed.**
- 67 after REVIEW_S16_S17.
- +1 TS/R1 restored (the review's own condition met and now confirmed): 68.
- +1 N5-triv: 69.
- +1 RW: 70.
- +1 N5-sf0: 71.

# Required fixes (binding for the next session)

1. **SF-1:** R_g orientation at PROOF l.5324 and l.5355.
2. **SF-2:** state the proven gap's size (≈ 10⁻⁸¹; ≈ 4·10⁻⁵¹ with N5-w0) wherever N5-sf0's "gap" is claimed.
3. **SF-3:** RTARGET §43 A: "met, except ε_* is an existence constant". Add an annotation; do not edit §43's text in place.
4. **SF-4, SF-5:** ν_w for general L; the holomorphy domain.
5. **RW-1:** narrow (iv) to the bounds, holomorphy, 𝒞(1) = K^{-1/2} and decoupling. Add the A = 𝒞(s)Z usage note. Record
   RW-2: choose R so that s̄ε_R ≪ 1 for the cluster-expansion use.
6. **W0-1:** relabel N5-w0's rate as numerically verified, or redo c35 C2 in exact rationals or interval arithmetic (a new
   check, criteria first), and only then call it computer-assisted.
7. **N5-sf_i:** state that (NA-H_loc) presupposes the level-i SU(N) background minimiser (B-NA/N2).
8. **RLARGE:**
   - F1 (why C_♮ exists); F2 (one T_k convention);
   - G5 (R1 with local (H-ch) for the r^s gas, or name it inside (H-pos)/(W1-ret'));
   - the N5 ↔ RLARGE threshold compatibility in §1A item 1;
   - say where n_♯ is defined that it depends on the ARGUED c_RS.
9. **Optional (N5-triv):** the orthogonality A_P ⊥ dλ doubles γ_i; M' vs M in N5-loc.
10. **LINEAR_PACKAGE v1.1 errata:** Part 3 items 1-8, with a change log; then it is public-ready.

---

## Strategic verdict: (NA-H_loc) for i ≥ 1 vs the c_1 lever vs others

- **The c_1 lever (a sharper PG constant): do not make it the next target.**
  - It would raise γ by up to the measured 2.5·10⁶, m_cov by the same factor, and ε_* ∝ γ·m/log by ~10¹².
  - But no node's status changes. Every downstream use needs only *some* g-independent threshold, and the thresholds are
    already uniform.
  - It is also not cheap rigorously. PG must be uniform in n and T, so a finite-dimensional computer-assisted bound does
    not obviously suffice, and the measured equality γ^LB = 2c_E is a single-grid measurement.
  - Keep it as an optional constants item. W0-1 (exact rationals for C2) is the cheap constants task, if one is wanted.
- **(NA-H_loc) for general i: do not attack head-on.** It is inside B-NA. It needs the SU(N) background minimiser at
  level i, its exponential locality, and the Hessian's local background dependence. That is paper-scale (CMP 95/96/99/102
  territory).
- **Recommended next target: (NA-H_loc) at level 1, by the Schur complement of N5-sf0.**
  - E_1^{NA}(V) = min_U[S_W(U) + κ_0Σφ̂(V; M̄(U))]. At a critical U, Hess E_1^{NA} is the Schur complement of exactly the
    level-0 operator that N5-sf0 controls (in the slice).
  - So:
    - (1) Existence and local regularity of the level-0 minimiser at curvature-small V, by a Newton/IFT iteration with
      N5-sf0's covariance as the inverse. This is the one-level case of B-NA; the curvature-only form needs the walk
      expansion again.
    - (2) The background dependence of H_1^{NA} is local, from RW (v), and the deviation from the abelian Hessian is from
      N5-an.
    - (3) Hence (NA-H_loc)_1 and N5 at level 1 (Proposition N5-sf_1).
  - It reuses everything just built, and it is the first genuinely multi-level non-abelian datum. Most importantly, it
    answers the uniformity question that decides B-NA's size: does the threshold or constant shrink by a fixed factor per
    level (fatal for i ~ k), or not?
  - Pre-state one failure mode: the Schur complement's slice/residual-fixing bookkeeping (level-0 gauge modes against the
    level-1 coarse gauge) is not uniformly inf-sup.
- **Alternatives, in order.**
  - The linear-side inputs of B-NA-red that are session-scale: (LED-src) and G♯_0-plain (LINEAR_PACKAGE §10's first block).
    They are needed for (G♯) whatever happens to N5.
  - The binding fixes above, which are under one session.
  - Everything large-field ((H-pos), (HIST)) stays behind CMP 122.
