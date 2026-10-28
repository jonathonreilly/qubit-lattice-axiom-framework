# REVIEW_SQ_S1: hostile review of lane G session 1 (SQ.md, SQ_LOG.md, checks q1, q2)

Reviewer: an independent agent. I wrote none of SQ.md, SQ_LOG.md or the checks. I edited no other file. No commits, PRs or
pushes.

Inputs (read-only):
- SQ.md (all, l.1-452) and SQ_LOG.md (all, including the disclosed 1052 MB breach).
- checks/q1_criteria.md, q1_sq_lin.py, q1_out.txt, q1_out_firstrun_crash.txt, q1_time.txt.
- checks/q2_criteria.md, q2_decay_min.py, q2_out.txt, q2_time.txt, with UTC mtimes.
- RLARGE.md v2 §3 (l.287-380).
- HW.md §4-§5 (l.157-300), the consumer of the windows and of the joint moment.
- HIST.md §15.4 (CLS-red), §20.0-§20.3 (MSG, MSG-loc', CLS-cone, (I_k^E)'), §25.5-§25.7 (Theorem A5) and §26 (AE-red).
- REVIEW_HIST_S4.md: format, S4-1 and the strategic verdict.
- PROOF.md: NA-alg (a)-(b) (l.2967-2975) and BNA-F1/F2/F3 (l.3176-3192).
- FLOW.md (SF-bg) (l.189-192); LINEAR_PACKAGE.md Theorem 3.8 (l.196-201); SF.md l.94-99 and l.826-840 (consumers of AE-red).

Scratch work is in the scratchpad directory `rsq/`:
- rq1.py: an independent construction of the three 1D frames, giving λ(J) and the max |Gram| row sums;
- consts.py: the constants of §0.3;
- re-run outputs.

Line numbers below are SQ.md's unless another file is named.

---

## Bottom line

- **Lemma INF and the descent architecture are right, and they are the session's real gain. Two statements about them are wrong.**
  - Branch (iii), HW's windows and HW's Proposition FV consume only the cone-local infimum 𝓔^{𝒞(P)}(V). That is HW's ℰ_P(V),
    literally. MSG-dec, E2, SUP-price, FORCE and DESC are correct as written; I re-derived every step and constant, with two
    small slips (the BCH-p constant and FORCE's strictness).
  - l.70 is false: "(AE) for every chain is strictly stronger than what is consumed". A lower bound on the infimum over chains
    with top V is *equivalent* to the same lower bound for every chain with top V. What the infimum form buys is a proof
    method (one may assume minimality), not a weaker statement.
  - It follows that DESC + (REG-min) *proves* the general-chain energy form, and also AE-red's size clause (S1-2 below).
    That is what lets (MS-Sob) leave the path. §0.5's justification is incomplete: Theorem A5 (A), (I_k^E)' (a4) and SF's
    (BG-loc) consume AE-red's size clause, i.e. (MS-Sob). They were not read.
- **The plain-sup failure (§0.2) is a correctly labelled method limit.**
- **(REG-min) is precisely stated, up to small fixes. It is not "the cone-local sup form of (BG)_k / (SF-bg)", it is not
  subcritical as argued, and its proof plan has a GAP.**
  - It is stronger than both (BG)_k and (SF-bg): it asks for one depth-uniform constant for the multi-level decay.
  - Ingredient (β) of the plan, the product rule, is false in the MSG gauge for link × link sources (it loses L^{k-i}).
  - Ingredient (α), a weighted-sup linear estimate with sources at every level, meets PROOF's BNA-F2: the Calderón-Zygmund
    failure of sup norms, i.e. a log, which here is the depth.
  - Its natural home is the B-NA multi-scale Schauder wall, the same wall to which REVIEW_HIST_S4 S4-1 sent A5, next to SF's
    (MIN-reg).
- **Linear (SQ): the D_j part is CONFIRMED with the stated constants 34203 / 1010.**
  - B-box is re-derived: entries (1, 2, 1)·L^{-m/2}, Schur row sums ≤ 14.93.
  - My independent max |Gram| row sums are 4.000, 6.309, 8.619, 9.952, 11.285, 12.055, 12.825, 13.270 (J = 1-8). They match
    the proof's entry formula exactly and rise to 14.93 only as the number of levels goes to infinity.
  - So q1's rising λ_box (9.29 at J = 9) is bounded by a rigorous uniform bound. It is not a threat.
  - The G_{j+1} part is in kind only (the counts are missing), so "explicit C_Q^lin" (l.340) and the counted status of §5 are
    overclaims.
- **Constants.** The sup route is a net LOSS, not "no net improvement" (l.162). Its per-defect price is c_♭τ_♭² ≈ 3·10⁻²³ at
  C_D = 2, against ε_1²/(2NC_cone) ≈ 6·10⁻¹⁴ to 6·10⁻¹⁷ for CLS-cone at ε_1 = 0.5. Both are depth-uniform and g-independent.
- **Checks: the FAILs are honestly recorded, and the criteria predate the scripts.**
  - Both re-runs reproduce to every printed digit.
  - One undisclosed pre-run edit of q2's script (mtime 02:19:28 against the logged 02:09). It is harmless.

---

## Priority 1. §0 "Is (SQ) needed?" and Lemma INF (l.45-72, 222-232)

### What is consumed (checked against the consumers)
- **RLARGE §3.3 (l.333-347)** needs the restricted joint main term ≥ u_kc_sf·min{||1 - V_P||², ε_1²}.
  - Under (I_k^E)'' the real-point main term is 𝓔^♭_k(U) = inf_ψE^♭(ψ; U) (HIST l.1655, 1690).
  - Its cone restriction is a sum of nonnegative 𝒞(P)-terms of one chain, completed by κΦ_{∂P}(U, V).
  - So it is ≥ 𝓔^{𝒞(P)}(V), where the infimum also runs over U. **INF holds.**
  - **Fix S1-1a (definitional).** "Restricted to the cone" must mean the sum of the 𝒞(P)-terms (or a superset). It must not mean
    Σ_x𝓔_{k,x} over the cone's sites: the lexicographic assignment (HIST l.1406-1408) can send a 𝒞(P)-term to a site outside.
  - INF also needs 𝒞(P) ⊂ 𝒞^♭(Λ_k), i.e. a full cone. Boundary-adjacent defects stay in E10.
- **HW §4-§5** uses ℰ_P(V) := inf E_𝒞(P)(·, V) (HW l.160), which is exactly 𝓔^{𝒞(P)}(V). (AE) enters only through TE (ii)
  (HW l.266), in infimum form:
  - W-bad and W-cb are lower bounds on ℰ_P and ℰ_p;
  - Proposition FV uses the same inequality;
  - the upper windows (TE (i), (iii)) and the joint moment (M-i), (M-f), Lemma CH and Lemma HÖ use no (AE).
  - So the per-defect windows and the joint-moment combination consume only the infimum form. Confirmed.
- **The min-form output** 𝓔^{𝒞(P)} ≥ (c_♭/C'²)min{θ², (C'τ_♭)²} (l.211) feeds TE (ii) with
  C'_cl = max{2/(c_♭τ_♭²), C'²/(2c_♭)} (s ≤ 2 above, s ≤ θ²/2 below). It is the same structure as CLS-red's
  max{C'_AE/(2N), 2/η_E}. W-cb's level-k use at thresholds η_q < C'τ_♭ works through DESC (b), at the cost C'² = 2809.

### S1-1 (binding): the "strictly stronger" claim is false (l.70; also l.47-48, 54-55, 231-232)
- If E(ψ) ≥ f(θ) for every chain ψ with top V, the infimum obeys it; conversely inf ≤ E(ψ).
- So (CLS-min) ⟺ "(AE)-type lower bound for every chain", for each regime.
- **Fix.** Replace l.70 by: "the consumed statement may be PROVEN by examining minimisers only (the infimum is attained), so
  regularity properties of minimisers become available". Replace "general-chain (AE) is not consumed" (l.55, 231) by: "its
  (MS-Sob) proof route is not needed; the statement itself follows from DESC + (REG-min)".

### S1-2 (binding): §0.5 missed consumers of AE-red's size clause, but DESC already covers them
- **Consumers not read.** SQ's inputs stop at HIST §23; §25-§26 may not have existed at 01:57 UTC (not negligent).
  - **HIST Theorem A5 (A)** (l.1687-1691): via AE-red's size clause, small-energy minimisers are ε_R-regular. It is listed
    "⇐ … (MS-Sob)" (l.1676).
  - **(I_k^E)' (a4)** (HIST l.1413-1415): "ε-regularity, CLS-red steps α-β, ⇐ (AE)".
  - **SF.md** l.97-99 and l.838: (BG-loc)'s content is A5 (A)-(C), with (MS-Sob) in the hypothesis list.
  - So "(SQ)/(MS-Sob) leave the critical path" does not follow from branch (iii) alone.
- **The repair is short (reviewer-derived; I checked each step).**
  - Corollary DESC-ε, given (REG-min) and τ ≤ τ_♭: for EVERY chain on 𝒞(P) with E := E_𝒞(P) < c_♭τ²/C'², every object below the
    top has size < τ, and ||1 - U(P)|| ≤ C'√(E/c_♭).
  - *Proof.* Take a violating object of minimal height. Cases (i) and (ii) give E ≥ c_♭τ², a contradiction. In case (iii),
    q at level i ≥ 1: FORCE gives θ_q ∈ [τ, C'τ), and E ≥ E_𝒞(q) ≥ 𝓔^{𝒞(q)} ≥ c_♭min{θ_q/C', τ}² ≥ c_♭τ²/C'² by DESC (b), again a
    contradiction. The top bound is DESC (b) applied to the chain's own top. ∎
  - Taking τ := C'√(E/c_♭)(1 + δ), δ ↓ 0, gives AE-red's two conclusions for all chains with E ≤ η_♭ := c_♭τ_♭²/C'²:
    - |log U(P)|²_HS ≤ (1.011²NC'²/c_♭)·E;
    - the size clause, with constant C'/√c_♭ (≈ 1.3·10³ at N = 2) in place of √C'' and C_♮.
  - A5 (A), (a4) and SF's list can then cite DESC-ε instead of AE-red, and (MS-Sob) leaves the path *conditionally on
    (REG-min)*.
  - The SQ owner should write this corollary; it is one paragraph.

### Verdict on Priority 1
- Lemma INF: **CONFIRMED-WITH-FIX** (S1-1, S1-1a).
- §0 verdict: **CONFIRMED in substance, with corrected reasons** (S1-1, S1-2).
- §0.5: **INCOMPLETE** (S1-2).
- The PLD question (l.225): grep finds no (AE), AE-red, CLS or MS-Sob in PLD.md, FLOW.md, RTARGET.md or PROOF.md.

## Priority 2. The plain-sup failure (§0.2, l.74-86): CONFIRMED as a method limit
- The bounds are correct for the tool used:
  - |d(Q^me)(P)| ≤ 4L^m·sup|e| (4n_m links per circulation, unit total weight);
  - the level-0 R-part ≤ n²C_p(C_Mε)² (the weights sum to n²).
- Sup data give no cancellation, so no depth-uniform bound follows. It is correctly called a method limit. The withdrawal of
  "attained by a circulating field" (SQ_LOG 02:21) was right.
- Two wording fixes:
  - "|log U_k(P)| ≤ C'ε (Lemma FORCE)": FORCE bounds ||1 - U||, so add (F1).
  - "per-scale pricing is (CLS-min)" (l.86) also answers REVIEW_HIST_S4 strategic 4. Its note there should be cross-referenced:
    the per-scale route avoids (MS-Sob), but not the constants (Priority 5).

## Priority 3. The minimiser-only sup route

### Lemma MSG-dec (l.99-115): CONFIRMED
- Re-derived against HIST MSG steps (1)-(7):
  - steps (3)-(4) with level-dependent maxima give (2A_d + 1)ε^p_i + ε^r_i + A_dκ_V (18.4y² ≤ ε^p_i by (S2) at the smaller size);
  - step (5) gives κ_V ≤ L⁻²(1.011ε^p_{i+1} + 32.2α²e^{4α}), within the stated 33;
  - doubling by (F3), the recursion's coefficient is 2C_Dθ L^{-2(k-i)}B_1 + 66A_dL⁻²α²e^{4α} with B_1 = 3.011A_d + 1 + L² = 37.1.
- Division by θL^{-(k-i)} gives K_i ≤ K_{i+1} + (2C_DB_1 + 66A_de^{4α}K²θ)L^{-(k-i)}, as stated.
  - The quadratic term is kept, so S3-2 is avoided.
  - The sum starts at m = 2, so using Σ_{m≥1} is conservative.
  - K = C_D(4.04 + 74.2) = 78.2C_D, K_top = 81.2C_D, matching l.97.
- Level k: ||1 - U^g_k(c)|| ≤ Lα_{k-1} + C_Dθ(1 + (A_d + 1)/L²), as stated.
- A_ax = 12 is the safe choice.

### Lemma E2 (l.117-129): CONFIRMED; sharper than HIST §26 step (4)
- The mixed-word bound ||e^Ae^B - e^{A+B}|| ≤ 2|A||B|e^{2σ} is correct:
  - σ^n - a^n - b^n ≤ ab·2^nσ^{n-2};
  - Σ_{n≥2}(2σ)^n/(n!σ²) ≤ 2e^{2σ}.
- It gives the m|ρ̃| term in place of HIST's |ρ̃|². Every constant is conservative:
  - bracket (ii) is 9.2·1.22 = 11.2Np_L² against the stated 13.3;
  - |X_0| ≤ 1.46y_c;
  - the cross term is 8.86Np_L.
- C_e = 3791 confirmed. NA-alg (a) is applied to M̄_c = avg e^{Z_T} with |Z_T|_HS ≤ y_c, which is legitimate: the lemma has no
  base-frame condition.

### Lemma BCH-p (l.131-132): minor slip (M-1)
- With 4m = 1/10: 2·2(e^s - 1 - s) = 33.09m² (op), so C_p = 33√N is 0.3% too small at the end of the range m ≤ 1/40.
- **Fix:** C_p := 34√N, or m ≤ 1/80. In use m ≤ K_topθ ≈ 10⁻⁶, so nothing downstream moves.

### Theorem SUP-price (l.134-164): CONFIRMED given its inputs
- Steps checked:
  - (1)-(2): unrolling, valid on cone links;
  - (3): the n^{-4}#{y} weights sum to n²;
  - (5): 4L^m·max|e_i| with k - i = m + 1, sums K²/(L(L - 1)) and 1.011KC_DL/(L² - 1);
  - (8): t² ≤ 1.03·2(1 - cos t) for |t| ≤ 0.506 (actually 1.022);
  - NA-alg (b) with ρ = ρ̃ (V⁻¹W_0 = e^{ρ̃}), and 9.2y² + (√N/3)e^{|ρ|}|ρ| ≤ ¼ gives φ ≥ |ρ̃|²/(4N);
  - (9): θ ≤ |log|_op ≤ |log|_HS, and θ ≤ θ_0 gives θ² ≤ 4C_1E.
- C_1 = 160. Step (5) is the genuine new point: decay beats the L^m circulation gain.
- θ_♯ is described, not written as a list. **Fix (M-2):** list it as the minimum of:
  - MSG-dec's two conditions;
  - y_c ≤ 1/20 with m ≤ K_topθ;
  - 9.2y_c² ≤ 1/8;
  - e^{|ρ̃|}|ρ̃| ≤ 3/(8√N) with |ρ̃|_HS ≤ 1.011√NC_Dθ;
  - BCH-p's m ≤ 1/40 at K_topθ.
  - Numerically it is ≈ 3.5·10⁻⁶ at C_D = 2. MSG-dec's quadratic condition and ε_M/C_D bind.

### Lemma FORCE (l.166-175): CONFIRMED; wording (M-3)
- C' = L² + 4A_d + 8 = 53. The L × L centre square lies in the four endpoint blocks.
- DESC (a) needs the contrapositive with ≥ C'τ. Restate FORCE with the actual maximum μ < τ of the listed sizes: the proof
  gives ≤ C'μ < C'τ, strictly.
- The tally is inconsistent: l.166 says "not counted" and l.441 says "[FORCE counted with DESC]". Pick one.

### Lemma DESC and Corollary PRICE-iii (l.192-213): CONFIRMED (DESC); CONFIRMED as CONDITIONAL ⇐ (REG-min) (PRICE-iii)
- Case (i): s ≥ ||1 - U||²_op/(2N).
- Case (ii): KQ (lower) with ||M̄ - W_0|| ≤ 18.4y², y ≤ c'A'τ, and x ≥ 73.6Ny² gives φ ≥ x²/(4N).
- Case (iii):
  - the nesting is used;
  - U¹ is used only as a competitor;
  - U² keeps q's links, so θ_q ∈ [τ, C'τ];
  - (REG-min)'s τ_R-smallness is implied by non-violation since τ ≤ τ_R;
  - SUP-price's ranges come from τ ≤ θ_0/C', θ_♯/C', ε_M/(C_DC').
  - The height strictly decreases, so the descent terminates.
- (b) and the min-form (l.211) check out.
- PRICE-iii is one level only (overlap 1/24, as CLS-cone (c1)); multi-level needs disjoint footprints (S3-5 (c3)). Stated
  correctly.
- c_sf in RLARGE's form is c_♭τ_♭²/ε_1², given ε_1 ≥ C'τ_♭.

### Hypothesis (REG-min) (l.177-190)
**Precision (fixes M-4).**
- "Residuals in 𝒞(q)" must include the top residuals of q's own links: (D2) at i = k - 1 bounds them by C_Dθ. Say so.
- Fix the cone-box and torus conventions as in SUP-price (level-k side ≥ 3).
- "For every τ_R-small minimiser" is what DESC uses, and it is correctly chosen: "some minimiser" would not suffice in case
  (iii).
- θ = 0 is consistent: the minimiser is flat.

**It is not the cone-local form of (BG)_k / (SF-bg) (S1-3, binding wording).**
- (BG)_k (RLARGE l.326-328) is ONE level: curvature ≤ C_IL⁻²·(coarse) + quadratic. Iterating it gives C_I^{k-i}L^{-2(k-i)}.
  (REG-min) asks for a single C_D, i.e. effectively C_I = 1 plus summable corrections, uniformly in depth, on a free-boundary
  cone box.
- (SF-bg) (FLOW l.189-192) is analyticity with exponentially local derivatives at the trivial field. It is not a decay
  statement.
- The closest existing items:
  - PROOF's (G♯) (BNA-F1: the proven linear kernels, e.g. LINEAR_PACKAGE Theorem 3.8, are DATA kernels; a source at every
    level needs a new estimate);
  - SF.md's (MIN-reg) (l.832-838: coarse-unit a-priori closeness of minimisers, which AE-red's own-unit bounds do not give).
  - The decay class is a coarse-unit sup bound, the sup shadow of (MIN-reg)'s X_c norm.
- Replace "on the main path anyway (node A)" (l.53) by "B-NA-class (multi-scale Schauder), adjacent to SF's (MIN-reg) and
  PROOF's (G♯)".

**It is not subcritical as argued, and the plan has a GAP (S1-4, binding).**
- **(β) is false in the MSG gauge.** Links in the decay class are only ≍ KθL^{-(k-i)} (MSG-dec), one power of L per level.
  - A link × link source (the BCH [a, a] of every plaquette, and the e_i of E2) bounded as "unweighted (C_Mτ_R) × weighted"
    is C_Mτ_R·KθL^{-(k-i)} against the curvature weight θL^{-2(k-i)}. It loses L^{k-i}.
  - The correct bound uses both factors' decay: K²θ²L^{-2(k-i)}, i.e. θ𝔑², quadratic in 𝔑.
  - The inequality 𝔑 ≤ C_lin + Cθ𝔑² has a large branch, which absorption cannot exclude. The a priori finiteness of 𝔑 is
    ≍ τ_RL^{2k}/θ, useless.
  - Excluding the large branch needs a continuity (bootstrap) argument along a continuous family of minimisers, i.e.
    uniqueness or a selection. The plan disclaims exactly that (l.186).
  - (In a smooth multi-level gauge the quadratic terms are a·∇a, and (β) would hold; that gauge is BNA-F3's open item.)
- **(α) meets BNA-F2.**
  - Plaquette-type sources q (same derivative order as F) enter the response as F = q - dΔ⁻¹d*q-type, a Calderón-Zygmund
    operator.
  - Between weighted sup norms it is bounded only up to a log. In the multi-level lattice form that log is the number of
    coarser levels whose sources, each of unit weighted size, add at a fine site.
  - So a weighted-sup (α) with general sources at every level is expected to lose ≍ (k - i), and 𝔑 ≤ C_lin + C·k·θ𝔑² is not
    depth-uniform.
  - SUP-price escapes this because it evaluates only an UPWARD (averaging) observable, the top circulation. (REG-min) needs
    pointwise decay at every level, i.e. the downward direction.
  - [Reviewer ARGUED; it is the repo's own BNA-F2 scaling count transposed to the decay class.]
- **What would work [inference].**
  - State (α) in RTARGET §33's coarse-unit Hölder (Schauder) pair, where the CZ log is absent.
  - Prove the product rule there (an algebra estimate).
  - Run a contraction in a smooth gauge, which gives uniqueness (and (a5-U)) at the same time.
  - This is the B-NA wall's proof shape, cone-local with free boundary.
- **q2 does not test this.** It has data only and no sources, so it is the BNA-F1 "data kernel" case. In d = 4 it covers only
  two depths, and C_D doubles (0.22 → 0.45). The d = 2 half is depth-flat (1.06 → 2.25), but d = 2 is not scale-invariant
  (C3).
- **Proposed q3 (for the owner, criteria first).** The linear chain in d = 3, with prescribed plaquette-type sources of unit
  weighted size and aligned sign at every level. Measure the weighted curvature response against k. The reviewer predicts
  linear growth in k.

## Priority 4. Linear (SQ) (§2-§5)
- **B-box: CONFIRMED (re-derived).**
  - Same level: diagonal 2, neighbours -1.
  - Finer level: only the three X' whose midpoint is a breakpoint; |G| = n'^{1/2}·jump = L^{-m/2}(1, 2, 1).
  - Coarser level: the support's only interior multiple of n is n(X + 1), and ≤ 3 coarse functionals jump there.
  - β_M = 4 + 8/(√L - 1) = 14.93.
  - Numerically, my independent max |Gram| row sums equal 4 + 4Σ_{m≤j}L^{-m/2} + 4Σ_{m≤J-1-j}L^{-m/2} at the best row (13.270
    at J = 8). Since λ ≤ row sum, **λ_box(J) < 14.93 for every J, rigorously.**
  - q1's 9.29, still rising at J = 9, is consistent with this. My λ_box(J), J = 1-8, reproduce q1's to 4 digits.
  - The post hoc mechanism sentence (l.400, "L^{-1/2} saturation") does not match its own data: the increments shrink by ≈ 0.7-0.83
    per depth, not 0.577. Drop it or say "slow".
- **B-tri: CONFIRMED.**
  - Summation by parts gives entries ≤ 2L^{-3m/2}; ||ψ||² = 1 + n⁻² exactly.
  - Counts 5, 3L^m + 3, ≤ 4.
  - β_A = 21.53 is crude: the max row sum is 7.41 at J = 7 and λ = 4.105.
- **B-edge: CONFIRMED.** ⟨χ_{j,0}, χ_{j',s'}⟩ = (n'/n)^{3/2}(s' + 1); β_E = 1.477 is an upper bound on every row. The measured row
  sum is 1.238 and λ = 1.157 for both layers, against 2.953.
- **§3.0, §4.1-§4.3: CONFIRMED.**
  - The Schur norms check out.
  - ||I_2|| ≤ ν² holds for the normalised factors J̃_0 = L^{1/2}J_0 and J̃_1 = L^{-1/2}J_1 (the unnormalised product has the same
    norm because the L-powers cancel). Say so (M-5).
  - Distances 3h and 3h + 1; window multiplicities 2 and 3.
  - (3 + ν²) is Cauchy-Schwarz with weights (1, 1, 1, ν).
  - Residual Schur: row 4n, column 2n·n⁻⁴, so 8n⁻².
  - C_main = 3·11401 = 34203 and C_res = 72(1 + ν²)²(L/(L - 1))² + 72ν⁴ = 1010.
- **§4.4 G_{j+1} (the link source): in kind only (S1-5, binding status fix).**
  - The reduction to coarse gradients plus an edge term via LINEAR_PACKAGE Lemma 2.3 (ii) is right in kind.
  - What is missing: the neighbourhood counts (how many G-links read one coarse plaquette difference), and whether the clamped
    layer's coarse positions beyond s < h are covered (f(1) = f(0) + ∇f(0) handles them).
  - So **l.340 "explicit, depth-independent C_Q^lin" is an overclaim**: it is depth-independent in kind, not explicit.
  - §5's linear MS-Sob is counted PROVEN-HERE (l.441), but its constant C_S^lin = 24d·S_L·C_nb·(C_Q^lin)² contains the
    uncomputed G part. **Downgrade §5 to CONDITIONAL ⇐ §4.4 bookkeeping** (uncounted until the counts are written).
  - The algebra of §5 is correct as an identity: intra-block δ = Σ±D_j; inter-block (S_c - Q)δ + G + r with G = ((1 - QI)a)(c) by
    (W2); no quadratic term.
- **§0.4 (Q_str ↔ Q_root): CONFIRMED** (Q_strB'_i - B'_{i+1} = Q_rootB_i - B_{i+1}; avg is onto). q2's use is legitimate.

## Priority 5. Constants and their consequences
Recomputed (N = 2, L = 3, κ = 1; consts.py):

| C_D | K | C_err | θ_0 | τ_♭ (binding θ_0/C') | price c_♭τ_♭² |
|---|---|---|---|---|---|
| 0.45 | 35.2 | 3.3·10⁶ | 1.5·10⁻⁷ | 2.8·10⁻⁹ | 1.2·10⁻²⁰ |
| 2 | 156 | 6.6·10⁷ | 7.6·10⁻⁹ | 1.4·10⁻¹⁰ | 3.2·10⁻²³ |
| 2.25 | 176 | 8.4·10⁷ | 6.0·10⁻⁹ | 1.1·10⁻¹⁰ | 2.0·10⁻²³ |

- The θ²-coefficient 1/(4C_1) = 1/640 is correct.
- θ_0 ≈ 3.0·10⁻⁸/C_D² (l.161 says ≈ 10⁻⁸/C_D², which is 3× low; fix M-6).
- τ_R (unknown) can only lower τ_♭.
- **Consequences (S1-6, binding wording at l.162).**
  - Against CLS-cone at ε_1 = 0.5 (ε_1²/(2NC_cone), C_cone ≳ 10¹²-10¹⁵: 6·10⁻¹⁴ to 6·10⁻¹⁷), the sup route is 6-9 orders WORSE.
    The C_cone-equivalent at ε_1 = 0.5 is ≈ 2·10²¹ at C_D = 2. Write "net loss", not "no net improvement".
  - Under A5's own ε_1 restriction (REVIEW_HIST_S4 strategic 4: CLS-cone price ≈ u_k·10⁻³¹/C_3), the two routes are of the
    same order. DESC-ε's threshold η_♭ = c_♭τ_♭²/C'² ≈ 10⁻²⁶ would give ε_1 ≲ 5·10⁻¹⁴/√C_3 and a price ≈ 10⁻³³/C_3.
  - Either way the price is depth-uniform and g-independent: valid for a proof, with g² below it.
  - a_coh becomes the binding entry of RLARGE §3.4's a_♯. The "defect size ~10⁻⁸" means SUP-price itself acts only below
    θ_0; larger defects are priced through the descent at τ_♭. That is consistent, but it caps the price at τ_♭².
  - C_e and K dominate C_err (h6 measured MSG at 3.5 against 66), so optimisation could gain several orders. Unclaimed, as
    stated.

## Priority 6. Checks q1, q2
- **Order and honesty.**
  - q1_criteria (02:00:56) and q2_criteria (02:01:15, its one pre-script C3 edit disclosed) predate both scripts (logged
    02:07, 02:09).
  - q1's later mtime (03:45:25) is the disclosed crash fix (dense ≤ 2500, ncv = 96), not a criterion change.
  - q2_decay_min.py's mtime is 02:19:28, against the logged creation at 02:09: an undisclosed edit, before any run (first smoke
    03:34). Harmless; disclose it (M-7).
  - The criteria quote β-values derived at 02:02-02:07 in the written text. They come from the pre-§T exploratory reasoning,
    which the protocol allows.
  - Both OVERALL FAILs (A2; C3 d = 2) stand as recorded, and are correctly read as criterion design errors, not as defects of
    the mathematics. A2 is the slow saturation of a rigorously bounded quantity (Priority 4). C3 is d = 2 non-scale-invariance.
- **Resources.**
  - q1 run 2's peak footprint of 1052 MB > 1 GB is disclosed. Part A alone needs ≈ 120 MB (my run), so the breach was Part B
    at k = 3.
  - Future runs should split Part B into its own lock hold, or skip k = 3.
- **Re-runs (reviewer, lock held 04:05:27-04:05:37 UTC, one rmdir; load 5.65 at start, 43% free, nice 10, threads 1).**
  - rq1 (independent frames, box J ≤ 8, tri and edge J ≤ 7): 2.0 s, peak footprint 118 MB. The λ values reproduce q1's.
    The Gram row sums are as quoted in Priority 4.
  - q2 re-run verbatim: 8.4 s, 230 MB. Identical output (C1, C2, C4 PASS; C3 FAIL).
  - consts.py ran under a second lock hold (one rmdir).
- q2 faithfulness:
  - the level-k box is exactly P's four links;
  - free boundary;
  - Q_str triangle/block weights;
  - κ ≡ 1;
  - LSQR minimal-norm solutions are fine, because the outputs are gauge invariant.

---

## Corrected tally (session 1)

| Item | SQ's status | Reviewer |
|---|---|---|
| Lemma INF | PROVEN, not counted | CONFIRMED-WITH-FIX (S1-1, S1-1a) |
| MSG-dec | PROVEN, counted | CONFIRMED |
| E2 | PROVEN, counted | CONFIRMED |
| BCH-p | PROVEN, not counted | CONFIRMED-WITH-FIX (M-1, C_p := 34√N) |
| SUP-price | PROVEN, counted | CONFIRMED (M-2, list θ_♯) |
| FORCE | inconsistent | CONFIRMED, not counted (M-3) |
| DESC | PROVEN, counted | CONFIRMED |
| PRICE-iii | CONDITIONAL ⇐ (REG-min) | CONFIRMED as CONDITIONAL |
| (REG-min) | OPEN | OPEN; statement fixes M-4; NOT node-A-adjacent-cheap (S1-3) |
| (REG-min) plan | ARGUED | GAP (S1-4: (β) false in the MSG gauge; (α) meets BNA-F2) |
| §0.2 | method limit | CONFIRMED |
| §0.4 | PROVEN, not counted | CONFIRMED |
| B1D (B-box, B-tri, B-edge) | PROVEN, counted | CONFIRMED |
| SQ-lin, D_j part | PROVEN, counted | CONFIRMED (34203 / 1010) |
| §4.4 G reduction | PROVEN, not counted | in kind only (S1-5) |
| §5 linear MSG-loc-dev + MS-Sob | PROVEN, counted | CONDITIONAL ⇐ §4.4 counts; identities CONFIRMED |
| §6 non-abelian | OPEN/ARGUED | unchanged (off-path, not reviewed in depth) |
| §7 proposal | ARGUED (AE) ⇐ MSG + MS-Sob | STALE: HIST §26 AE-red is now PROVEN as an implication (REVIEW_HIST_S4 P6) |

- **Counted PROVEN-HERE: 6** (MSG-dec, E2, SUP-price, DESC, B1D, SQ-lin D_j). SQ claimed 8; its own list had 7.
- **CONDITIONAL: 2** (PRICE-iii ⇐ (REG-min); linear MS-Sob ⇐ §4.4 counts).
- **OPEN: 2** ((REG-min); non-abelian (SQ)).
- **New reviewer-derived item for the owner:** Corollary DESC-ε (S1-2), CONDITIONAL ⇐ (REG-min), proof sketch above.

## Binding fixes (next lane-G session)
1. **S1-1.** l.70, 47-48, 55, 231-232: infimum form ⟺ every-chain form. The gain is the proof method; reword.
2. **S1-1a.** Define the "restricted main term" in INF as the 𝒞(P)-term sum, and require a full cone in 𝒞^♭(Λ_k).
3. **S1-2.** Add Corollary DESC-ε (the size clause and the every-chain bound from DESC + (REG-min)). Rewrite §0.5 to list:
   - A5 (A) (HIST l.1687-1691);
   - (I_k^E)' (a4) (HIST l.1413-1415);
   - SF.md l.97-99, 838;
   - HW TE (ii).
   All are discharged by DESC-ε ⇐ (REG-min).
4. **S1-3.** l.51-53, 177, 230: (REG-min) is B-NA-class (multi-scale Schauder, cone-local, free boundary). It is adjacent to
   PROOF (G♯) and SF (MIN-reg), not "the cone-local form of (BG)_k / (SF-bg)".
5. **S1-4.** l.181-189: withdraw "subcritical", "absorption … no uniqueness and no contraction mapping needed" and the product
   rule (β) as stated. Record both obstructions ((β) in the MSG gauge; (α) and the BNA-F2 log). Re-plan in the §33 Hölder pair
   with a smooth gauge and a contraction. Run q3 (criteria first) before further architecture.
6. **S1-5.** l.340, 441: "explicit C_Q^lin" → "depth-independent in kind; counts open". §5 → CONDITIONAL, uncounted.
7. **S1-6.** l.161-162: θ_0 ≈ 3·10⁻⁸/C_D²; "no net improvement" → "a net loss of 6-9 orders against CLS-cone at ε_1 = 0.5;
   comparable under A5's ε_1 restriction".
8. **§7.** Rewrite against HIST §26: SUP-price is the decay-class instance of AE-red's conclusion, without (MS-Sob). The proposal
   for HIST's owner is a citation of DESC-ε as an alternative to AE-red, CONDITIONAL ⇐ (REG-min).
9. **Minor.** M-1 (C_p), M-2 (θ_♯ list), M-3 (FORCE strictness; tally consistency), M-4 ((REG-min) top residuals and
   conventions), M-5 (normalised I_2), M-6 (θ_0 figure), M-7 (q2 script edit at 02:19). Also drop the "L^{-1/2} saturation"
   reading (l.400).

## Strategic verdict
1. **The structural insight is right and should be kept.**
   - Every consumer of (AE), (MS-Sob) or (SQ) on the main path needs only two statements about cone-local minimisers:
     - the infimum bound (branch (iii), HW);
     - small energy ⇒ every-level small, the size clause (A5 (A), (a4), SF).
   - DESC proves both from one hypothesis about small minimisers.
   - SUP-price shows that decay makes every transported quadratic source geometric, with no ℓ⁴ step. This is the right
     replacement for AE-red's ℓ⁴ steps (4)-(5).
2. **(REG-min) is not a cheap substitute for (SQ).**
   - In sup norms it is log-critical (BNA-F2), not subcritical.
   - Its proof needs the multi-scale Schauder machinery (PROOF (G♯) + (R♯), a smooth multi-level gauge), which is the B-NA
     wall.
   - Taking (SQ)/(MS-Sob) off the critical path is therefore justified **only as a merger**: if (REG-min) is derived from the
     B-NA items that A5 needs anyway (REVIEW_HIST_S4 S4-1; SF (MIN-reg)), the open-wall count drops by one ((SQ-dev) and
     (MS-Sob) go).
   - Until that derivation exists, (REG-min) is a second wall of B-NA difficulty. Keep (SQ-dev) as a parallel route: off the
     DAG's critical path only conditionally. Do not delete it, and do not mark it "not consumed".
3. **Recommended next target for lane G.**
   - First, linear (REG-min) with sources in the §33 Hölder pair (cone-local, free boundary): the analogue of (G♯_0) at the
     trivial chain. q3 should come first to confirm the sup-norm log.
   - Then the product rule and a contraction in a smooth gauge. This also yields (a5-U)-type uniqueness and (MIN-reg) near the
     trivial chain, so one proof would serve DESC, A5 and SF.
4. **The constants are now the cost of the whole small-field classical chain (10⁻²³ to 10⁻³³ per defect).**
   - They are depth-uniform and g-independent, so they are acceptable for an existence proof.
   - The lead should record in RLARGE §3.4 that a_coh is the binding exponent, at g² ≪ 10⁻²³ (sup route) or ≪ 10⁻³¹ (energy
     route under A5).
5. **Do not:**
   - count §5 or the G part as PROVEN;
   - read q2 as evidence for (REG-min) with sources;
   - cite "(REG-min) is on the main path anyway";
   - propose §7's text before rewriting it against HIST §26.
