# REVIEW_BFT_A_S7: hostile line-by-line review of BFT lane A, session 7 (BFT_A.md §31-§35, BFT_A_LOG session 7, checks/ba7*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: REVIEW_BFT_A_S6.md (all);
BFT_A.md l.38, l.222-226, l.445, l.465, l.606, l.830, l.916-919, l.1024-1048, l.2729-3266 (§31-§35 in full); BFT_A_LOG.md
sessions 6-7; BFT_B.md §15.0-15.1 (l.2014-2060), §16.1-16.2 (l.2143-2165), l.2492-2501, l.2517, l.2601-2602, l.2631;
REVIEW_BFT_B_S6.md l.39-56, l.160-180, l.210-225; REVIEW_BFT_A_S3.md l.25-31, l.240-248; checks/ba7_criteria.md,
ba7_s7.py (all), ba7_out_K.txt, ba7_time.txt, ba6_w0.py run_k, ba5_y.py (Qop/QTop, coulomb, Chain). Only this file was
written in the repo. Reviewer scripts and outputs:
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revbftA7/`
(run.sh, rev7_diag.py, time.log, out_{A,K,D1,D2}.txt, err_{A,K,D1,D2}.txt).

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / GAP / WRONG. ARGUED marks reasoning of mine that is not a written
proof. Nothing below counts in PROOF's tally.

## Bottom line

- **Provenance: CONFIRMED.** The byte boundaries are exact (256215 B ends §30 at l.2728; 268696 B ends §31.5 at l.2857), the
  file was never rewritten, the criteria hold no session-7 constant, and every §33 heading postdates the runs. One minor
  disclosure item (fix P7-1): §32, appended at 10:17:18Z, refers forward to "proof §33.1" and to §35.
- **[RBA6-fix] P6-1..P6-7: all applied faithfully.** P6-4 (cover construction plus periodisation) is CONFIRMED, and the
  factor (1 + q)⁴ is conservative: the overlap count already absorbs the wrap. One precision is needed (P7-2). P6-2's
  line-number correction (§33 item 4) is **right**: the 𝔐^∇ clause is l.38 and the Wilson-BCH table row is l.226. My S6
  numbers l.222/l.224 were wrong.
- **Lemma GE: CONFIRMED.** **Lemma TD: CONFIRMED** (exact; precision 1 is right and needed). **Lemma CD: CONFIRMED-WITH-FIX.**
  - Part (i) is trivial: it holds at any critical point and does not need (GI).
  - In (ii), "Λ_0/const" must read Λ_* = {ξ = 0 at level-k roots}. In the nonabelian case K'_x does not annihilate
    constants.
  - The content of CD is (ii): the Γ_E-Feynman fixed point is critical. That is the standard Faddeev-Popov statement, proven
    correctly given (GI) and the invertibility of Γ_EK_x (ARGUED).
- **Proposition CD2: ARGUED, correctly labelled.** **Proposition OB: identity CONFIRMED given CD2; the quantitative
  obstruction is WRONG as written.**
  - Lemma TD's own solution b_m = T_m(R) is admissible, with sup|T_m| ≤ (k - m)N_Bσ_m.
  - So by the flux bound, (ND) cannot hold on boxes larger than ≈ 8(k - m)N_BL³/c_0. The "ρ_1 = L^{k-m}, (R)-size
    L^{θ(k-m)}, grows with the box" reading of 33.5 and §35 is impossible.
  - The correct conclusion is weaker: under a finite-scale (ND), no b_m is better than T_m by more than a constant. So the
    telescoping route cannot remove the factor (k - m) (fix P7-4).
- **Lemma IP: CONFIRMED** (constant 12 re-derived).
- **Proposition SR: CONFIRMED as an implication of (PW-ℓ¹) + SPD** (every exponent re-done). The s-balancing idea is right.
- **(PW-ℓ¹): stated precisely in Part 4. It is plausible, it is OPEN, and it is not provable from lane B's machinery as it
  stands.**
  - Dual form (PROVEN here): (PW-ℓ¹) is equivalent to O(1) Γ_E-responses to *arbitrary*, non-co-closed single-level sources
    (and a log-loss version for divergence-form sources). So it is a per-level (NC-E), not a slice-regularity fact.
  - I raised a specific threat: lane A's Q = Q_str + d∘h (the root funnel) could put O(1) gradients at root links. I tested
    it (diagnostic D2, k = 3) and **found no blow-up**. The PW ratios stay 0.25-0.50 (ℓ¹) and 1.5-5.0 (gradient) at every
    level, for p at a level-3 root and for p far from the level-2 roots. The contour average's symmetry cancels the
    plaquette dipole at the root.
  - **Owner recommendation: lane A**, in the dual form, with one supporting lemma from lane B on Γ_E^T (Part 4).
- **m > 0: Lemma LES-dd, Theorem W0-loc, Lemma WT, Lemma QH_m, Theorem W0_m: CONFIRMED** (0 ≤ m ≤ m_Y), with two
  precisions: the Hölder-separation range in QH_m's multiplier, and the notation of [G^c_0]_{α,m} (P7-6). LES-dd is the
  right replacement for Lemma LE at m > 0. DX_m and DB_m are not attempted, as stated.
- **Proposition SM: (a) CONFIRMED, (b) CONFIRMED-WITH-FIX, (c) CONFIRMED as an implication.**
  - (b): the constants are the same only at m = 0. Weighted bounds pick up e^{20m} (REVIEW_BFT_B_S6 RS6-3).
  - (c): its inputs are now reviewed. REVIEW_BFT_B_S6 (born 09:55:38Z, not read by session 7) CONFIRMS Theorem RH and
    LRL(b)-E for T ≥ 5, and RH-inv only for level-wise co-closed classes.
  - SM is the written form of REVIEW_BFT_B_S6's ARGUED periodic lift.
- **ba7 re-run under the lock:** A and K are **identical** to the stored outputs apart from timing/RSS (diff). All PASS
  verdicts are reproduced.
- **k-uniformity verdict.**
  - The T = 1 series (2.68, 5.34, 6.97; increments 2.66, 1.63) cannot separate saturation from ln k growth. ln k fits
    3 points to 1% (predicted 6.90), and each T = 1 torus is a single coarse site. Clean linear-in-k growth (constant
    increments) is disfavoured at face value, but the series is confounded by fine-torus growth (sides 3, 9, 27).
  - **The informative comparison is at a fixed fine torus.** There, adding levels *lowers* U_H in all four cases
    available: side 9: 7.49 (k = 1) > 5.34 (k = 2); side 18: 10.14 > 7.59; side 27: 10.61 > 9.74 > 6.97.
  - k = 1 saturates in T at ≈ 10.7 (S6). So the data are consistent with **sup_{k,T}U_H ≤ U_H(1, ∞) ≈ 10.7**, i.e.
    k-uniform, and give no sign of log growth.
  - This is post-hoc, three depths, abelian, L = 3, κ ≡ 1: evidence, not proof.
  - k = 3 at T = 2 (side 54) or k = 4 at T = 1 (side 81) would need ~5 GB and ~25 GB. Not cheap, not run.

---

# Part 1. Provenance (priority 1)

**Filesystem record** (stat in local EDT, quoted in UTC):
- BFT_A.md: born 05:39:32, modified 10:26:38, size 305985.
- ba7_criteria.md: 10:15:19. ba7_s7.py: born = modified 10:16:13, so no fix before the run.
- ba7_out_A: 10:16:53-10:17:07. ba7_out_K: 10:17:07-10:17:37. ba7_time.txt: 10:17:37.

**Confirmed.**
1. **Byte boundaries.** The first 256215 bytes end at §30's last line (l.2728). The first 268696 bytes end exactly at
   §31.5's last line ("…No constant derived in this session appears in them.", l.2857). The birth time is unchanged, so
   every edit was an append.
2. **Criteria.** `grep -cE '1296|0\.51|C_SR|52|48N|e\^\{8m\}|K_L|6952' ba7_criteria.md` = 0. The only number with session
   content is Lemma IP's 12, and that is pre-stated in §31.1 (l.2803-2804).
3. **Order.** §31 < criteria < script < runs < §33, and §32 was appended during part K. §32 is pure transcription of the
   S6 fixes plus the P6-4 decision; it does not use ba7.
4. **Disclosure.** §31's list (l.2741-2744) names every session-7 idea that later carries a proof, including "an
   interpolation-Poincaré gain against SPD" (Proposition SR) and the periodic lift (SM). The (c) marks are honest.
5. **Run protocol.** One acquisition, one rmdir, no pkill, and a post-run pgrep/pycache/lock check logged with commands
   (BFT_A_LOG l.200-202). It matches U9.

**Fix P7-1 (disclosure, minor).**
- §32 (10:17:18Z) cites "Lemma GE (§31.1, proof §33.1)" (l.2901-2902) and "Session 7's status of these items is in §35"
  (l.2907). §33 and §35 did not exist yet.
- These are forward references to planned sections, not results. Add one dated line saying so. Nothing is invalidated.

# Part 2. [RBA6-fix] items (§32)

- **P6-1, P6-3, P6-5, P6-6, P6-7: CONFIRMED** (faithful transcriptions).
  - P6-6's reformulation for Γ_E, S^E_0(V) = V + Γ_E^TΞ^TV, is Lemma GE (c). It is correct (Part 3).
- **P6-2: CONFIRMED, with the line correction of §33 item 4.**
  - l.38 is the 𝔐^∇ clause (it contains ||∇^cx^c_j||_{∞,m}). l.226 is the "Wilson BCH q_p" row.
  - REVIEW_BFT_A_S6's l.222/l.224 were wrong (l.222 is prose, l.224 is the table header).
  - The bold text of §32 P6-2 still says "l.222"; §33 item 4 overrides it. That is acceptable.
- **P6-4 (l.2880-2888): CONFIRMED, with a precision (P7-2).**
  - Per commutes with d and d* (it is a sum of translates) ✓. Lemma BOG, the moment identity and Lemma PC are used only on
    compactly supported lifts in Z⁴ ✓.
  - The factor (1 + q/M_l)⁴ is an over-estimate. A torus point z receives Σ_c Σ_γ|W̃_c(z + γ)|.
    - The pairs (c, γ), with c in a fundamental domain and z + γ ∈ cube(c̃), are in bijection with the cover pieces whose
      cube contains a fixed lift z̃.
    - So the sup bound is the cover bound 4N_R(2q + 1)⁴·(piece sup), with no extra factor.
    - Harmless either way.
  - **Precision P7-2.** The identity d*W_c = R_c - v_c needs **Per R̃_c = R_c**, i.e. the torus piece must be the descent
    of the cover piece built from the periodic lift of the configuration.
    - This holds for every row of 28.6 (b) and 28.12: they are local polynomial formulas in x and r(x), evaluated on the
      periodic lift.
    - Say it once, because on tori with M_l ≤ q a "local formula on the torus" could otherwise be read as the wrapped sum
      evaluated on the torus. The two agree only by this remark.

# Part 3. Step 2: Lemmas GE, TD, CD, CD2, OB (priority 2)

**Lemma GE (33.1, l.2936-2952): CONFIRMED.**
- (a) Inputs: BFT_B 16.1 (a), (c), (e) (l.2144-2160, read). Λ is linear (λ^E_X minimises a quadratic). Σ_Xχ^5_X = 1, so
  I_χλ = c for λ with constant root value c ✓.
  - Γ_EΞλ = -(λ - c) ✓. Ran Γ_E = Λ_* ✓.
  - 𝓛_E invertible: Ker H ∩ S_E = Ran Ξ ∩ S_E = 𝒢_0 ∩ S_E = {0}. Ran Ξ over Λ_0 equals 𝒢_0 because constants give 0 ✓.
- (b) Feynman: FG (ii) with Ker Γ_E = S_E; the representative of Y^p in S_E is Π_EY^p (Π_E moves along 𝒢_0 only) ✓.
  - Hard slice ✓. Both give n²⟨S, Π_EY^p⟩ ✓.
- (c) ⟨μ + D, ν⟩ = 0 on Λ_* with μ ∈ Λ_* ⇒ μ = -P_*D ✓. Γ_E^Tδ_{c_Y} = 0 because Λ(x)(c_Y) = 0 for every x ✓.
  - D(S^E_0) = D + (Γ_EΞ)^TD, and (Γ_EΞ)^T = -1 + I_χ^T on all level-0 functions, so D(S^E_0) = I_χ^TD, supported on the
    level-k roots ✓.
- *Reading (no fix).* GE says nothing about the **size** of Γ_E^TD.
  - (λ^E_X)^T is the gradient of a box Neumann potential, so on a point charge it gives a |z|^{-3} field. Its sup can exceed
    the source's sup by a factor up to n.
  - So the "box-local correction" is not small termwise. SR rightly avoids splitting S^E_0 into its pieces (it pairs the raw
    rows with Π_EY^p).

**Lemma TD (33.2, l.2954-2971): CONFIRMED.** Every step was re-done.
- T_m = S_m + Q_m^TT_{m+1} ⇒ u_m = d*S_m + ev^Tu_{m+1} (BL-2 (c)) ✓. d*c_m = 0 for 1 ≤ m ≤ k - 1 ✓. d*c_0 = D(S) ✓.
- The identity: index shift with b_0 = b_k = 0 ✓. The source functional of (c, -b_{·+1}) equals that of S ✓.
- The general solution ✓.
- The restriction formula needs nested roots: a level-l root is a root at every lower level. This holds for block-centre
  roots with L odd (BFT_B §15.0 "roots at block centres"; ba7 E1 (d): the code's roots are at offset 1) ✓.
- **Precision 1: CONFIRMED and necessary.** The b_k extension works.
  - The extra term is ⟨b_k, Q_{k-1}v_{k-1}⟩. It equals ⟨b_k, r_{k-1}(v)⟩ only because chains have v_k = 0 in Setting LIN
    (x_k = B_k is data, so the source functional is unchanged up to a constant). State "v_k = 0" (P7-3).
  - b_k is a solution of d*b = f on the coarse torus. It is generally nonlocal, with sup up to ~T·sup|f|. That is fine for
    exactness, but not for bounds (it does not matter where D vanishes at the roots, e.g. after GE (c)).
- ba7 E1 tests only k = 2 (a single b_1). The recursion for k ≥ 3 is algebra only. It is checked above.

**Lemma CD (33.3, l.2973-2984): CONFIRMED-WITH-FIX.**
- The identity Ξ^T𝔑^0 = -K'^T_x∇(𝔉_k∘exp) on Λ_* ✓. Ξ^TH = 0 and Ξ^TNB = 0, because r_{k-1}(Ξξ) = d(ev λ_{k-1} - λ_k) = 0 ✓.
- **(i) is trivial and does not need (GI).** At a critical point 𝔑^0 = Hx - NB, and Ξ^T(Hx - NB) = 0 identically. Say so,
  so that (i) is not cited as a consequence of gauge invariance.
- **(ii): CONFIRMED** (the Faddeev-Popov argument) on Λ_*. **Fix P7-3 (part):** "Γ_EK_x a bijection of Λ_0/const" must
  read "of Λ_* onto Ran Γ_E = Λ_*".
  - In the nonabelian case K'_x(const) = [const, x]-type terms ≠ 0, so K_x does not descend to Λ_0/const.
  - (GI) is assumed only for gauges trivial at level k. Λ_* is exactly what the proof uses.
- Remark (ARGUED, invertibility of 1 + Γ_EK'_x): correctly labelled.
  - Note: the operator norm needed is Λ_* → Λ_* in a norm in which Γ_E is bounded. With Γ_E ~ box-Coulomb of size up to n,
    this is a real (unwritten) estimate, not a formality.

**Proposition CD2 (33.4): ARGUED, correctly labelled.**
- The algebra after the covariance expansion is right: Q_lx_l = x_{l+1} + r_l, w(r, r) = 0, and w linear in its first slot
  gives α_j - β_j = w(E_j, x_j) ✓.
- The two un-re-derived inputs (that R^B_l = κ_l(∂B_l)^Tr_l for the S4' average, and the endpoint convention ♯) are named.

**Proposition OB (33.5, l.2995-3014): identity CONFIRMED given CD2; piece totals CONFIRMED; the quantitative obstruction
is WRONG as written.**
- The identity u_m = -β_m + Σ_{m<j≤k}ev^{(m→j)T}w(E_j, x_j) (with precision 2) ✓.
- Piece totals [r_m(c), (Q_mx_m)(c)] = [r_m(c), x_{m+1}(c)] ✓.
- Flux bound ✓, and the arithmetic of the contradiction at ρ > 8N_BCL³/c_0 ✓.
- **The error.** Lemma TD itself supplies an admissible b_m: b_m = T_m(R^B), with d*T_m = u_m.
  - Write Q_m^T = Q_str^T + h_m^Td* (the funnel; Part 4 item 1). Then T_m = R_m + Q_str^TT_{m+1} + h_m^Tu_{m+1}.
  - Three bounds: |Q_str^Tv| ≤ L^{-3}sup|v| (I_L = L³Q_str^T is a convex combination); |h^Tf| ≤ 2(L - 1)sup|f| (REVIEW_BFT_B_S6
    l.177); and, at OB's configuration (D = 0 off the level-k roots), the restriction formula gives
    |u_{m+1}| ≤ Σ_{l≤m}8N_Bσ_l ≤ 9N_Bσ_m.
  - With σ_{m+1} = L³σ_m, A_m := sup|T_m|/σ_m obeys A_m ≤ (1 + 18(L - 1))N_B + A_{m+1}. So
    **sup|T_m| ≤ C_L(k - m)N_Bσ_m**, with C_L := 1 + 18(L - 1).
  - Applied to T_m, the flux bound gives |Σ_Qu_m| ≤ 8ρ³C_L(k - m)N_Bσ_m for every box.
  - Hence (ND) (|Σ_Qu_m| ≥ c_0ρ⁴L^{-3}σ_m) **cannot hold for ρ > 8C_L(k - m)N_BL³/c_0**.
  - The sentence "If ρ_1 is the coarse scale L^{k-m}, the residual sources … ≳ L^{θ(k-m)}c_0L^{-1}η² per level" (l.3010-3011)
    assumes an impossible ρ_1. So does §35's "forces the residual sources to grow with the box" (l.3221).
- **What survives (fix P7-4).** Under (ND) on [ρ_0, ρ_1] with 8N_bCL³/c_0 < ρ_1 ≤ 8C_L(k - m)N_BL³/c_0, no b_m of sup ≤ Cσ_m
  uniform in k - m exists, and sup|b_m| ≥ c_0ρ_1L^{-3}σ_m/8.
  - So the TD push-down's (k - m) is sharp up to constants. That is the real obstruction. The factor k sits in
    c_0 = T_0(R) (level-0 plain current of coarse size ~kη²), as in [RBA2-fix] B3.
  - BA7-F2 "does not occur (ARGUED)" stands in this weaker form.

# Part 4. Lemma IP, Proposition SR and the wall (PW-ℓ¹) (priority 3)

**Lemma IP (33.6, l.3016-3025): CONFIRMED.**
- I_su(z, ν) = s^{-1}Σ_{t<s}u(Y'(z - te_ν), ν) uses exactly the blocks Y'(z) and Y'(z) - e_ν ✓. z ∈ D(Y') for both ✓.
- Σ_D|Y - m_B| ≤ (1 + |D|/|B|)Σ_D|Y - m_D| ✓. The path count ≤ |D|ℓ_a and max ℓ_a = 2s ✓. Each point lies in two
  rectangles ✓ ⇒ 12s ✓.
- The torus needs s | M_l, and s = L^{⌊t/2⌋} divides TL^t ✓.

**Proposition SR (33.7, l.3027-3047): CONFIRMED as an implication of (PW-ℓ¹) + SPD.**

*Arithmetic (re-done).* SPD as used is exactly l.917/l.1044: |Q_str^{(l→m)}R^B_l| ≤ C_SPDκ_lL^{-3(k-l)}η², own units of
level m, for every m ∈ (l, k] ✓. With σ_l = 4κ_+p_LL²L^{-3t}η² and n² = L^{2l}L^{2t}:
- level 0 ✓; t = 1: the powers cancel exactly, O(1) per level ✓;
- t ≥ 2, smooth term: n²s³·C_SPDκL^{-3t}η²·s^{-4}C_PL^{-2l}L^t = C_SPDκC_Pη²s^{-1} ≤ C·L^{1/2}L^{-t/2}η² ✓;
- interpolation term: n²N_Bσ_l·12s·C_PL^{-2l}(t + 1) = 48N_Bκp_LL²C_P·sL^{-t}(t + 1)η² ≤ …(t + 1)L^{-t/2}η² ✓.
- The level sum is geometric ✓. **So SR is a valid implication.** The balancing (s^{-1} against s) is a genuine and correct
  idea.

***(PW-ℓ¹), precisely (as lane A states it, l.2805-2807).*** Let Y := Π_EY^p (lane B's S_E representative of the fine
plaquette response, a chain of level-l 1-forms, 0 ≤ l < k). There is C_P, independent of k, T and p, such that for every
0 ≤ l < k:
- **(PW-i)** Σ_{level-l links}|Y_l| ≤ C_PL^{-2l}L^{k-l};
- **(PW-ii)** Σ_{level-l links}Σ_a|∂_aY_l| ≤ C_PL^{-2l}(k - l + 1);

in level-l own units. SR uses (PW-i) at l = 0 and t = 1, and both (PW-i) and (PW-ii) at t ≥ 2.

**Dual form (reviewer; PROVEN, by Lemma GE (b) and ℓ¹-ℓ^∞ duality).**
- Σ|Y_l| = sup{|⟨j, Y_l⟩| : ||j||_∞ ≤ 1}, and ⟨j, Y_l⟩ = n^{-2}f^E_0[j](p), where f^E_0[j] is the Γ_E-response to the
  single-level source j placed at level l.
- So **(PW-i) ⟺ ||f^E_0[j]||_∞ ≤ C_PL^{3(k-l)}||j||_∞** for **every** level-l current j, co-closed or not. That is an O(1)
  response to a coarse-size-1 level-l source with no cancellation.
- **(PW-ii) ⟺ ||f^E_0[∂^Tg]||_∞ ≤ C_PL^{2(k-l)}(k - l + 1)||g||_∞** for divergence-form level-l sources.
- By Lemma GE (c), f^E_0[j] is the gauge-invariant response to the composite-co-closed source j + Γ_E^TD(j).
- So (PW-ℓ¹) is a **per-level (NC-E) for arbitrary single-level sources**. It is the same kind of object as (NC-Γ), one level
  at a time, not a configuration-side regularity fact.

**A threat to (PW-ℓ¹) that I tested and did not confirm (reviewer; diagnostic D2).**
1. Lane A's Q (S4' contour average) is root-covariant: Q d = d ev, and every contour runs root to root (l.606). On
   co-closed forms Q^T = Q_str^T (REVIEW_BFT_A_S3 l.245; lane B's funnel h_l, REVIEW_BFT_B_S6 l.167-177).
   - So **Q = Q_str + d∘h**: Q is the straight average plus a level-(l+1) gradient of a local function (the funnel).
   - Iterating, Y_l = Q_str^{(0→l)}Y_0 + dφ_l + (residual and Λ terms), with φ_l = Σ_{1≤j≤l}ev^{(j→l)}h_{j-1}(Q_str^{(0→j-1)}Y_0).
   - The straight part has PW's amplitude L^{-2l}. The funnel part could be O(1) on the links of a level-l root next to p,
     if the root-link weights did not cancel the plaquette dipole field. That would break (PW-ii) once L^{2l} ≫ C_P(k - l + 1).
2. **D2 (k = 3, T = 1, side 27; CG representative of ba5_y.Chain, i.e. orthogonal to the composite gauge directions, not
   S_E).** For the (0,1)-plaquette:

| p | l | max\|Y_l\|·L^{2l} | Σ\|Y_l\| / (L^{-2l}L^{k-l}) | Σ\|∇Y_l\| / (L^{-2l}(k - l + 1)) |
|---|---|---|---|---|
| level-3 root (13,13,13,13) | 0 | 0.125 | 0.500 | 4.95 |
| | 1 | 0.055 | 0.435 | 3.38 |
| | 2 | 0.033 | 0.250 | 1.45 |
| far from level-2 roots (8,8,8,8) | 0 | 0.125 | 0.501 | 4.96 |
| | 1 | 0.114 | 0.500 | 4.53 |
| | 2 | 0.082 | 0.444 | 3.26 |

   - **No blow-up.** If the funnel effect were there, the root row would grow like L^{2l} (×81 at l = 2). Instead it is
     *smaller* than the generic row. The contour average is symmetric over the 24 orders, and that cancels the
     antisymmetric plaquette dipole at the root.
   - Both rows are flat or decreasing in l at PW's scaling. So **the data support (PW-ℓ¹)'s exponents** (C_P ≈ 5 suffices
     here).
   - Caveats: one depth (k = 3), abelian, κ ≡ 1, a composite-Coulomb rather than S_E representative, and no sup over all p.
3. **Consequence for a proof.** The funnel decomposition is still the right bookkeeping. A proof of (PW-ii) must show the
   root cancellation, or bound the funnel part by pairing it through Lemma TD:
   Σ_l⟨R_l, dφ_l⟩ = Σ_j⟨u_j(R), g_j⟩ = Σ_j⟨T_j(R), dg_j⟩, g_j := h_{j-1}(Q_str^{(0→j-1)}Y_0). With
   sup|T_j| ≤ C_L(k - j)N_Bσ_j (Part 3) this is geometric in k - j (ARGUED).
   - So TD, blocked as a *bounding* route by OB, is useful as a pairing device here.

**Is (PW-ℓ¹) plausible?** Yes (ARGUED, and supported by D2).
- The straight part is the block average of a near-Coulomb fine field (|z - p|^{-3} near p). It is screened beyond the
  coarse scale: ba6's T-saturation and the coarse-shell decay ≈ 0.33 per shell in REVIEW_BFT_A_S6.
- Its ℓ¹ norm then sums |z|^{-3} up to L^{k-l} (level-l units), and its gradient sums |z|^{-4}, which gives the log
  (k - l + 1). Both are exactly PW's scalings.
- The tail beyond the coarse scale needs the slice potential, not only the curvature, to be screened. In S_E that follows
  from Λ's locality (EP-alg (g)) plus the pinned top level (x_k = 0). That is plausible, but it is an estimate, not an
  identity.

**Who should own it.**
- **Not lane B's existing machinery.** EP-bd, EP-int and EP-rec bound ||Π_Ex||_X (sup/Hölder) by gauge-invariant
  sup/Hölder data, for Hölder-class sources. They do not dualise to ℓ¹ point-source bounds.
- Theorem RH (CONFIRMED in REVIEW_BFT_B_S6) assumes level-wise co-closed sources. By the dual form above, PW concerns
  exactly the non-co-closed ones.
- **Recommendation: lane A owns (PW-ℓ¹), in the dual form,** as a gauge-invariant response bound for single-level sources plus
  the TD pairing of the funnel part. Lane A's Theorem YH / LD bootstrap machinery is the natural ℓ¹ tool (YH already gives
  𝒩(Y^p) ≤ C_YNn, i.e. (PW-i) at l = 0 in the *optimal* representative).
- **Lane B supplies one lemma:** an ℓ¹ → ℓ¹ (or ℓ^∞ → ℓ^∞ with explicit n-power) bound and locality for Γ_E^T = Σ_X(λ^E_X)^Tχ^5_X
  (box-Neumann adjoint), and the ℓ¹ comparison of the S_E representative with the 𝒩-optimal one ("S_E is ℓ¹-near-optimal",
  33.7 last paragraph, not proven).

# Part 5. Step 3: m > 0 (priority 4)

**Lemma LES-dd (33.8, l.3049-3064): CONFIRMED.**
- The symbol bound: |ν_aν_b| ≤ (|ν_a|² + |ν_b|²)/2 ≤ ψ, so |ν_aν_b|/ψ ≤ 1 ✓. Forward vs backward choices only change phases ✓.
- The whole-lattice w_2 avoids any boundary H² estimate ✓. -Δw_2 = Σ∂∂g on Q_{r-2} (two stencil steps) ✓.
- The Dirichlet w_1: energy ≤ r⁴H_0², Poincaré r² ⇒ r⁶H_0² ✓.
- Harmonic decay exponent 6 in d = 4 ✓. Iteration with a = 6, b = 4 + 2α ✓. The H-term R^{2-2α}H_0² ⇒ R·H_0 after the square
  root ✓.
- The constant 16 in the w_2 bound absorbs the ℓ^∞-diameter factor of the Hölder step. Harmless.
- **BA7-F4 does not occur ✓.** This is the "local Campanato for the curvature" of REVIEW_BFT_A_S6 Part 5 item 3, written
  correctly.

**Theorem W0-loc (33.9): CONFIRMED.**
- F closed ⇒ -ΔF = dd*F componentwise ✓. d*F = d*G_0 + h (W0 step 4, CONFIRMED in S6) ✓. The double-divergence form ✓.
- The coarse conversion: n²·(ρ/n)^{-α}·(…) ⇒ sup f_0 + [G^c_0]_α + n³H_0 ✓. n³H_0 ≤ sup|j^c_0| + κ_+sup|r_{k-1}| locally ✓.
- The periodic lift for small n and T ✓.
- **This closes PROOF's (LED-src) without Lemma LE or any Coulomb potential.** It is the better proof of W0 step 4.

**Lemma WT (33.10): CONFIRMED.** All inputs lie within ℓ^∞ cell distance 2, hence ℓ¹ ≤ 8 ✓. So
w_m(z_B) ≤ e^{8m}w_m(y) ✓. For CO-0R, CO-B and GU, LES holds with local sups (Lemma 3.2 is local) ✓.
- R = 4max(4, L^l) ≤ 4n/3 needs n ≥ 12 when L^l < 4. The small-n branch is the crude sup bound. Fine.
- **Notation (P7-6 part).** [·]_{α,m} is defined (l.2774) for outputs as a box-weighted Campanato. W0_m step 3 applies it to
  the source G^c_0. Either a box-weighted Campanato or a weighted pointwise Hölder of G works, since LES-dd only needs
  ||(g - ḡ)1_{Q_r}||_2 ≤ Cr^{2+α}[g]. Say which.

**Lemma QH_m (33.11): CONFIRMED** (constants modulo the shell combinatorics, which I did not re-count).
- ψ_q ≤ 1 by the triangle inequality ✓. E = φ_p - φ_q is 2-Lipschitz in coarse ℓ¹, hence 8-Lipschitz in ℓ^∞ ✓.
- |e^a - e^b| ≤ |a - b| on a, b ≤ 0 ✓.
- **Precision (P7-6).** [ψ_q]_α ≤ 8m holds for separations ≤ 1. If [·]^∞_α ranges over all separations, use
  |ψ(z) - ψ(z')| ≤ 1 ≤ d^α beyond 1. Then the multiplier factor is ≤ 2 rather than 1 + 8m.
  - Either way it is a constant. With 2, the bootstrap coefficient is ¼·2·e^{4.1mL^c} ≤ ¼·2·1.19 ≈ 0.60 < 1. The proof's
    "e^{4.1mL^c} ≤ 2" is loose (e^{4.1 ln 2/16} = 1.19). So the result stands under either convention, but the stated
    "< 0.51" needs the local convention: state it.
- Case A: e^{4.1mL^c} ≤ 2 and 1 + 8m ≤ 1.01 on [0, m_Y] ✓ (m_Y ≤ ln 2/(16·260) ≈ 1.7·10^{-4}). Coefficient < 0.51 ✓.
- The second-part term ~ m·L^c·C_d ≤ C_d ln 2 ✓. This is the term the S6 reviewer predicted.
- Case B: the torus ℓ¹ diameter ≤ 2T < 16L^c ⇒ e^{16mL^c} ≤ 2 ✓. **BA7-F5 does not occur ✓.**

**Theorem W0_m (33.12): CONFIRMED** for 0 ≤ m ≤ m_Y, uniform in k, T, X_0.
- The step 1 multiplier e^{m(φ_{X_0}(z_p) - φ_p - φ_{X_0})} ≤ 1 by the triangle inequality ✓. w_m ≤ e^{4m}e^{mφ_{X_0}} ✓.
- Step 2 (the top residual written out, closing S6's "by the same argument") ✓. Lower residuals from the top one within one
  cell ✓.
- Steps 3-4 ✓, given WT and §18.7.
- **This upgrades REVIEW_BFT_A_S6 fix P6-7:** the G_0 part of W0's sup and all Hölder parts of W0 are now proven at m > 0.
- Still OPEN, as §35 says: DX_m and DB_m, hence the weighted sups of GU, CO-0R and CO-B.
- §35's concern (is m_Y ~ ln 2/(16L^c) enough downstream?) is right and is now the gating question for m > 0.

# Part 6. Step 4: Proposition SM (priority 5)

- **(a): CONFIRMED.**
  - EP-alg (f) (translations), (c) (Λ = 0 at roots), (e) (S_E ∩ 𝒢_0 = {0}) and (g) (locality; Ñ_X embeds for T' ≥ 5,
    side 4n + 1 < 5n) are all in BFT_B l.2144-2160, read ✓.
  - Independence of c: Λ_{T'}(x̃)(z) is computed from box problems on copies of the same Z⁴ box ✓. For T ≥ 5, c = 1 ✓.
- **(b): CONFIRMED-WITH-FIX (P7-7).**
  - "Same constants" is right at m = 0 for translation-invariant sup and Campanato norms.
  - For the weighted (m > 0) versions the lift costs e^{16m} on the source and the output point must be chosen in the
    fundamental cell nearest X̃_0 (REVIEW_BFT_B_S6 RS6-3: C_b(T) ≤ e^{20m}C_b(T')). Add this.
  - EP-opt's lift argument: the average of the translates of a T'-solution is a periodic solution (linear problem,
    periodic source); uniqueness modulo 𝒢_0 then identifies it ✓.
- **(c): CONFIRMED as an implication, and its inputs are now reviewed.**
  - REVIEW_BFT_B_S6 (09:55:38Z; BFT_A_LOG does not list it as read) CONFIRMS Lemma RT, Theorem RH (k ≥ 2, T ≥ 1) and LRL(b)-E
    for T ≥ 5. It CONFIRMS RH-inv only for **level-wise co-closed** classes (RS6-1). EP-rec is CONFIRMED in REVIEW_BFT_B_S5.
  - So (c) holds for the level-wise co-closed source class of LIN0, all T ≥ 1, m = 0. Replace "session 6, unreviewed"
    (l.3143, l.3208) by these verdicts.
  - It does **not** extend to the non-co-closed rows ((NC-E)), which is consistent with §35.
- Priority note: the construction is REVIEW_BFT_B_S6's ARGUED RS6-3 (lift T' = 2T). §33.13 is its written proof, with any
  admissible c. No conflict.

# Part 7. ba7 and its re-run under the lock (priority 6)

**Script review (ba7_s7.py).**
- E1:
  - The source is made composite-co-closed **as a function** (Coulomb projection of T'_0), so precision 1's root case is
    not exercised;
  - b_1 = S_1 + ζ_1 is TD's general solution at k = 2 ✓;
  - (d)'s "PASS iff for one offset" is lenient, but offset 1 is the block-centre convention of BFT_B §15.0 ✓.
- E2 tests IP's elementary inequality on four field types. The ratios ≤ 0.26 show that 12 is loose, as §34 says.
- E3 calls ba6 run_k (reviewed in S6) ✓.
  - **All T = 1 tori are a single coarse site.** k = 1, T = 1 is a 3⁴ torus. These points sit deep in YH's Case B and in the
    regime where U_H is torus-limited: U_H(1, T) rises 2.68 → 10.65 from T = 1 to T = 10 in S6's extension.
  - So the T = 1 depth sequence mixes depth with fine-torus growth (side 3, 9, 27).

**Re-run.**
- One acquisition: lock 10:50:44Z (load 4.31, 31% free), released by one rmdir at 10:52:21Z.
- Settings: nice 10, OMP/OPENBLAS/MKL/VECLIB threads 1, PYTHONDONTWRITEBYTECODE=1, python3 without -I, no timeout, no
  trap, no pkill.
- Afterwards: `pgrep -fl 'ba7_s7|rev7_diag'` → none; no checks/__pycache__.
  - The lock directory present afterwards belongs to another session's later acquisition: mine was released at 10:52:21Z.
- Outputs went to the scratchpad only.

| job | peak RSS | result |
|---|---|---|
| ba7 A | 118 MB | **identical** to checks/ba7_out_A.txt after stripping timing/RSS (diff) |
| ba7 K | 304 MB | **identical** to checks/ba7_out_K.txt; H3a, H3b, N3 PASS reproduced |
| D1 (U_H at (1, 2), (2, 2), (1, 3), (1, 9)) | 270 MB | below |
| D2 (level profile of Y^p, k = 3) | 238 MB | Part 4 table |

**U_H table (ba7 + S6 extension + D1; post-hoc, no pre-registration weight).**

| fine side | k = 1 | k = 2 | k = 3 |
|---|---|---|---|
| 3 | 2.683 (T = 1) | - | - |
| 6 | 5.511 (T = 2) | - | - |
| 9 | 7.494 (T = 3) | 5.344 (T = 1) | - |
| 18 | 10.137 (T = 6, S6) | 7.586 (T = 2) | - |
| 27 | 10.605 (T = 9) | 9.740 (T = 3) | 6.973 (T = 1) |
| 30 | 10.654 (T = 10, S6) | - | - |

**Reading.**
1. At a fixed fine torus, every added level lowers U_H (four comparisons). The coarse pinning screens the response
   further, so depth does not feed the far field.
2. At fixed T, U_H rises with k (T = 1: +2.66, +1.63; T = 2: +2.08). That is the fine torus growing towards the k = 1
   saturation value, not log n: the k-series at fixed T stays below the k = 1 value on the same fine torus.
3. Hence the data are consistent with sup_{k,T}U_H ≤ U_H(1, ∞) ≈ 10.7, which is **k-uniformity, and show no log growth**.
   A ln k fit to T = 1 alone (6.90 predicted vs 6.97) is equally good, so T = 1 alone decides nothing. The fixed-fine-torus
   ordering is what carries the verdict.
4. Limits: depth ≤ 3, abelian Setting LIN, L = 3, κ ≡ 1, m = 0. The domination "U_H(k, T) ≤ U_H(1, TL^{k-1})" is an
   observed pattern, not a theorem. If it were proven (a monotonicity of the plaquette response under adding a pinned coarse
   level), it would give 𝒬_H k-uniformity from the k = 1 case. That is a cheap target worth one attempt (ARGUED).

# Binding fixes

- **P7-1** §32 (l.2901-2902, l.2907): one dated line saying that "proof §33.1" and "§35" were forward references to planned
  sections at 10:17:18Z.
- **P7-2** §32 P6-4: add "the torus piece R_c is the descent Per R̃_c of the cover piece built on the periodic lift (true for
  the rows of 28.6 (b), 28.12)". Optionally drop (1 + q)⁴ (the overlap count already absorbs the wrap).
- **P7-3** 33.2: state v_k = 0 for chains in the identity (precision 1's top term). 33.3 / §31.1 Lemma CD (ii): replace
  "Λ_0/const" by Λ_* (nonabelian K'_x does not kill constants). Record that (i) is trivial and does not use (GI).
- **P7-4** 33.5 l.3009-3011 and §35 l.3220-3221: (ND) cannot hold beyond ρ ≈ 8C_L(k - m)N_BL³/c_0, because T_m(R) is an
  admissible b_m with sup ≤ C_L(k - m)N_Bσ_m (C_L = 1 + 18(L - 1); recursion of Part 3). Replace the ρ_1 = L^{k-m} sentence and "grow with the box" by: "under a
  finite-scale (ND), the TD push-down's factor (k - m) cannot be improved by more than a constant".
- **P7-5** 33.7, §31.1 and §35 FOR OTHER FILES (2): record the dual form of (PW-ℓ¹): (PW-i) ⟺ O(1) Γ_E-response to
  coarse-size-1 single-level sources, co-closed or not, and (PW-ii) similarly for divergence-form sources. §35's
  "configuration-side input … Lane B owns the slice estimates" is replaced by: "(PW-ℓ¹) is a per-level (NC-E); lane A owns
  it in dual form; lane B supplies the Γ_E^T lemma". Note the funnel split Q = Q_str + d∘h as the bookkeeping a proof must
  handle (Part 4).
- **P7-6** 33.11: state whether [·]^∞_α ranges over separations ≤ 1 (needed for "1 + 8m" and "< 0.51"; with all separations
  the factor is 2 and the coefficient ≈ 0.60, still < 1). 33.12 step 3: say which
  seminorm [G^c_0]_{α,m} denotes.
- **P7-7** 33.13 (b): the same constants only at m = 0; weighted bounds pick up e^{20m} (lift and output-cell choice).
  33.13 (c) and §35 l.3208: cite REVIEW_BFT_B_S6's verdicts (RH CONFIRMED; RH-inv for level-wise co-closed classes;
  LRL(b)-E for T ≥ 5) instead of "unreviewed".
- **P7-8** §34 Reading (l.3179-3181): the T = 1 series is one coarse site per torus, and its increments conflate depth with
  fine-torus growth. The evidence for k-uniformity is the fixed-fine-torus ordering (Part 7), not the shrinking increments.

# Strategic verdict

- **Session 7 is correct where it proves things, and it moves three fronts.**
  - m > 0 for W0 is done properly: LES-dd + W0-loc + WT + QH_m. LES-dd is the right local tool and also gives the cleaner
    m = 0 proof of W0 step 4.
  - Small tori are done (SM, completing REVIEW_BFT_B_S6's RS6-3).
  - (NC-Γ) for Γ_E is pinned down structurally: GE (where Γ_E enters), TD (exact), CD (fixed points are critical).
- **The one genuinely new analytic idea is SR's s-balancing.** It is correct. It converts (NC-E)'s sup into one wall,
  (PW-ℓ¹).
  - By the dual form, (PW-ℓ¹) is itself a per-level (NC-E) for arbitrary single-level sources. So the reduction relocates
    the problem: it does not shrink it to a slice-regularity fact.
  - It is nevertheless a cleaner, scale-by-scale target. The data (D2) support its exponents.
- **What is wrong:** OB's quantitative obstruction (P7-4). The correct, weaker form still blocks the telescoping route.
- **Live walls, in order:**
  1. **(PW-ℓ¹)**, owned by lane A in the dual form. Lane B supplies a Γ_E^T (box-Neumann adjoint) ℓ¹/ℓ^∞ lemma.
     - First check whether YH's LD bootstrap runs for the Γ_E-response to a single non-co-closed level-l source. Its l = 0
       case is YH's 𝒩* in the optimal representative.
     - Track the funnel part (Q = Q_str + d∘h) explicitly; D2 suggests it cancels by contour symmetry.
  2. **The rest of (NC-E):** the top residual (the analogue of PW for Π_EY^{(b)}), the Hölder parts (W0-loc with the
     non-co-closed level-0 source), and the residual gradients.
  3. **m > 0:** DX_m, DB_m. But first settle whether m_Y ~ ln 2/(16L^c) suffices downstream. That is now the gating
     question, not the analysis.
  4. Nontrivial backgrounds, the endpoint α = θ, explicit constants.
- **Recommended next session (lane A):**
  - (a) Binding fixes P7-1..P7-8 (short).
  - (b) A proof attempt of (PW-i) at all levels via the dual form and the YH bootstrap.
  - (c) A cheap numeric of the dual form: the Γ_E-response to a random non-co-closed level-l source at k = 3. This needs
    Γ_E^T in code; lane B's bb scripts may have Λ.
  - (d) One attempt at the monotonicity "U_H(k, T) ≤ U_H(1, TL^{k-1})" suggested by the U_H table.
- **PROOF tally (candidates after this review):** Lemma GE, Lemma TD, Lemma IP, Lemma LES-dd, Theorem W0-loc, Lemma WT,
  Lemma QH_m, Theorem W0_m, Proposition SM (a)-(b), each with the fixes above.
  - Proposition SR is an implication only.
  - CD (ii) is conditional on the Γ_EK_x invertibility (ARGUED). CD2 and OB's (ND) are ARGUED.
