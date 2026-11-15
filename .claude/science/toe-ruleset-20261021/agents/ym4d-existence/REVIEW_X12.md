# REVIEW_X12: independent hostile review of session 12 of the YM4D existence lane (§21 and the [RX11-fix] changes)

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session12_snapshot.md (`cmp` clean).
  - `diff session11 session12` read in full: 26 fix hunks plus all of §21 (l.4607-4858).
  - §20.2-§20.4 re-read in context (l.4376-4500).
  - §15.6 ASSEMBLY and its hypothesis table (l.2513-2575).
- LOG.md, session 11 tail and session 12 (l.695-780). REVIEW_X11.md (all).
- checks: x11_criteria.md, x11_vertex.py (read line by line), x11_out.txt, x11_time.txt, x11b_criteria.md, x11b_axial.py
  (read line by line), x11b_out.txt, x11b_time.txt.
- Layer 1 (agents/ym4d-proof/), read-only, as of 05:18-05:35 UTC 2026-10-28:
  - files: RLARGE.md v2 (§1.2, §3.2-§3.4, §4.2, K3/K5/K8/K9); FLOW.md (§4, §18, §23, §36, §41-§45 headers, the status block
    l.2020-2045) with FLOW_LOG and REVIEW_FLOW_S3/S4/S5; HIST.md (§7.4, §15, §20, §25-§26, session-4 status l.1880-1896) with
    REVIEW_HIST_S4; HW.md (§0-§1, §5.3, §13-§18, interface table l.997-1013) with REVIEW_HW_S2; SQ.md (§0, §T, §9, §12) with
    REVIEW_SQ_S2; SF.md (§6.2, §7.1, §10, §11 incl. the 05:16 [RSF3-fix] edits) with REVIEW_SF_S3; BFT_A.md (§3.9, §5) with
    REVIEW_BFT_A_S1; BFT_B.md (summary table l.468-516); REVIEW_S22.md Part 5 (l.400-432); LINEAR_PACKAGE.md header.
  - Three read-only digest sub-agents gathered the layer-1 labels with file:line quotes. Every label used in (6) was re-read
    by the reviewer at the quoted line (HW l.966-971, SQ l.72-93, SF l.1209-1213 and l.1308-1335, BFT_B l.470-516,
    REVIEW_S22 l.405-430, HIST l.1891-1896, REVIEW_BFT_A_S1 l.29-34, BFT_A l.205, FLOW l.831-832/1755-1756/1851-1853/1876-1879).
- The reviewer's own computation (§(4c), §(7)): scratchpad `rerun_x12/rev_kappa.py` and `rev_kappa2.py`. They were written by
  the reviewer **after reading x11/x11b and their outputs**, and share no code with them.
- No web access. Literature remarks are marked [reviewer knowledge] and are not load-bearing.

Line numbers are EXISTENCE.md lines unless marked. No file other than this one was edited.

**Bottom line.**
- **RX11 fixes 1-11: all applied, all correct as of 05:01 UTC.** Two residues:
  - Fix 2's "CONDITIONAL ⇐ (FP-loc)_0 alone" and the "(CE-Q^∞) priced in U-variables, RLARGE branch (ii)" handoff went stale
    at 05:16 UTC. SF's [RSF3-fix SN-2, C-2] added (BGC) and withdrew the handoff. This is not a session-12 error, but it must
    be propagated.
  - Fix 9 calls the chain's C-covariance "ARGUED". ASSEMBLY (I) records it (C-invariance of the kernels and of μ_K, proof of
    NA-3, l.2527). Cosmetic.
- **Lemma AX: CORRECT.** Every combinatorial step re-derived: the 8 trees, the 7-site / 6-edge tree, the holonomy formula,
  the comb containment rule, and the torus removed links. One precision: the null class does not depend on 𝔗 at all.
- **Lemma NG-ax and the correction to REVIEW_X11 (4b): CORRECT.** REVIEW_X11's "strawman" remark was too strong, and is
  withdrawn. A new hostile qualification replaces it: the axial-Gaussian shadow is **not translation invariant** (reviewer
  computation). So "no limit point is such a shadow" is mostly implied by translation invariance. The real content is the
  per-site marginal separation (the TV bound).
- **Theorem NG-ax: CORRECT as an implication, but it is a corollary** of NG-red plus Lemma AX. Count Lemma AX instead; the
  tally is unchanged.
- **Tree-level value E_W[O] = 0.012827·N(N² - 1)g⁴: CONFIRMED independently.**
  - The reviewer re-derived the cubic action, the two-cubic Wick determinant and the absence of ghost/Jacobian terms by hand.
  - Checked numerically: an exact Isserlis check, and a numerical odd-part extraction of S_3.
  - Recomputed in **four** gauges with new code. Two of them (an off-root comb with all 9 corner links non-tree, so κ_PO ≠ 0,
    and random spanning trees) are genuinely discriminating. They agree with Feynman gauge to ≤ 5·10⁻⁷ at T = 8, 12.
  - x11b's root-comb residual is a finite-T effect concentrated on the comb's root line, and scales cleanly as T⁻³.
  - (c3-nz) is plausible to prove but is not touched by this number. It consumes a further layer-1 input (the k-uniform cubic
    data of the branch action), which the consumer list omits.
- **x11/x11b: honest.**
  - D FAIL is correctly reported.
  - A1 is correctly disclosed as vacuous. Note what this means: x11 had **no** pre-registered discriminating test of κ_V, and
    x11b F2 (post-hoc, disclosed) is the only one.
  - x11b re-run: byte-identical except the wall/RSS line.
- **CONSUMER LIST §21.3: materially incomplete and partly stale.**
  - It never cites HW.md, SQ.md, BFT_A.md or BFT_B.md.
  - (H-w) is no longer bare OPEN: HW reduces (H-w') to named hypotheses, and **for SU(2) and bad-only defects only**.
  - Branch (iii) no longer routes through (AE): SQ routes it through (REG-min), and (AE) is CONDITIONAL ⇐ (MS-Sob).
  - (U-loc) is reviewed. (U-IR) is split into sub-items, and FLOW's session 6 now consumes (L-loc) too.
  - The (CE-Q^∞) → RLARGE (ii) handoff is withdrawn.
  - (BG-reg) ⇐ BFT-1 + BFT-3 is this lane's routing, not a layer-1 statement. BFT-3 at k = 1 is now PROVEN.
  - The "(N5-unif) without (H-K)" route is contradicted by BFT_B's BB-4c.
  - The corrected list is (6).
- **Corrected tally: 58 / 1 / 3 / 9 / 12; ARGUED 39** (claimed 38; +1 for the (BG-reg) routing inference).

---

## (1) RX11 fixes (priority 1)

| Fix | Where (session-12 lines) | Verdict |
|---|---|---|
| 1 "not vacuum-only" deleted | l.4501-4506; §0 l.193; LOG l.713-714 | CONFIRMED. The constant-link example is copied correctly |
| 2 (M1) reason updated to SF session 3 | l.4334-4348, l.4553-4557, l.4600-4602; §0 l.182-185; LOG l.703-705 | CONFIRMED as of 05:01. **Residue (binding, post-hoc):** SF.md 05:16 [RSF3-fix SN-2] makes CE-exp^0 / CE-Q-as-integral ⇐ (FP-loc)_0 **+ (BGC)** (SF l.1313, l.1334). [RSF3-fix C-2] withdraws "pricing in U-variables, RLARGE §3.2 branch (ii)" as circular (SF l.1211-1212); it is to be restated in an SF §12.2/§13.2 that does not yet exist. Theorem CE-Q (band) is now "counted only with Fix Q1" and "superseded by CE-Q-col §13.1" (SF l.1310). Propagate to l.183-184, l.4336-4345, l.4353-4357, l.4553-4556, l.4600-4602 and §21.3 D |
| 3 (M2): (L-loc)_k, co-binding | l.4361-4368, l.4557, l.4582-4583 | CONFIRMED. SF l.857-859 and l.1318 match the text verbatim |
| 4 RLARGE branch (iii) as owner | l.4330-4332 | CONFIRMED |
| 5 B_N Z-event is a ν-bound | l.4350-4355 | CONFIRMED. "B_N in U-variables only" is the right repair |
| 6 ε := ε_1 | l.4190-4192, l.4200-4201, l.4573-4574 | CONFIRMED. χ in §20.4 uses the same ε; consistent |
| 7 tally 57/1/3/9/12, ARGUED 36 | §0 l.174-175, l.4575-4588 | CONFIRMED |
| 8 NG-wit nearly vacuous; (NG-conn) re-posed | l.4400-4406, l.4507-4514, l.4562-4567 | CONFIRMED. The parenthetical at l.4404-4406 should say "**at the site y** where the tree contains a star corner tree" (see (2)) |
| 9 d-type members, max_{t'}, r_2 | l.4461-4466, l.4468-4470, l.4490 | CONFIRMED. Cosmetic: l.4463-4464 labels C-covariance "ARGUED", but ASSEMBLY (I) records C-invariance of the kernels and of μ_K (l.2523, l.2527). So the joint chain law is C-invariant, and its conditional laws are C-covariant. The d-type members are harmless (their x_k vanish), but the label should read "recorded in ASSEMBLY (I)" |
| 10 A_*(n); x9 h = 1; (b^q) uniform | l.4215-4218, l.4266-4268, l.4372-4374 | CONFIRMED |
| 11 x10 record | l.4530-4542, l.4566-4567 | CONFIRMED. The appended-correction form is correct pre-registration practice |

---

## (2) Lemma AX and the star corner trees (priority 2): CORRECT

**Combinatorics, re-derived.**
- The corner at y uses 9 links: the star links U_μ(y), μ = 1, 2, 3, each in two corner plaquettes, and six outer links
  U_ν(y + e_μ), U_μ(y + e_ν). The plaquettes span 7 sites: y, three y + e_μ, three y + e_μ + e_ν.
- A star corner tree is the 3 star links plus one outer link per plaquette, so there are 2³ = **8**. It has 6 edges on 7
  sites. The star connects y to the three y + e_μ, and each far site y + e_μ + e_ν lies in exactly one plaquette and gets
  exactly one edge. So it is connected, hence a tree.
- In 𝔗-gauge with h(y) = 1, take P_μν = U_μ(y)U_ν(y + e_μ)U_μ(y + e_ν)⁻¹U_ν(y)⁻¹ with the two star links equal to 1.
  - If U_ν(y + e_μ) ∈ T_0, then P = U_μ(y + e_ν)⁻¹.
  - Otherwise P = U_ν(y + e_μ).
  - Plaquettes based at y transform by h(y), so gauge fixing leaves them unchanged.
- log(V⁻¹) = -log V off the eigenvalue -1 set, and χ is even. So O = σ_12σ_23σ_31·χ·tr(v_1[v_2, v_3]), which is odd under
  the joint inversion. **Correct.**

**Comb rule (l.4687-4691), re-derived.** Take direction order (d_1, …, d_4): d_1-links everywhere, and d_i-links on
{x_{d_1} = … = x_{d_{i-1}} = 0}, with the link leaving x_{d_i} = T - 1 removed.
- For corner directions μ before ν:
  - U_μ(e_ν) sits at a point whose only non-zero coordinate is ν, which comes later. All coordinates earlier than μ are 0, so
    U_μ(e_ν) ∈ 𝔗.
  - U_ν(e_μ) needs x_μ = 0, but e_μ has x_μ = 1, so it is ∉ 𝔗.
- The removed links leave coordinate T - 1 ∉ {0, 1} for T ≥ 3, so they never touch the corner.
- Edge count: (T - 1)(T³ + T² + T + 1) = T⁴ - 1.
- **Correct.** x11b's code (indices 3, 2, 1, 0 = order (4, 3, 2, 1)) matches. In the reviewer's code, the root comb has 6
  distinct corner links (9 with multiplicity) in the tree, and κ_PO ≡ 0.

**Precisions (non-binding).**
- (a) Star corner trees exist at **every root-line site** y = (a, 0, 0, 0), a ≠ T - 1, not only at the root. The reviewer
  found κ_PO ≡ 0 at (1, 0, 0, 0) and (T/2, 0, 0, 0).
- (b) **The null class is 𝔗-independent.** By Lemma AX the three plaquettes are V_P^{±1}. So "the law of (V_12, V_23, V_31) is
  inversion-symmetric" is the same as "the law of the three corner plaquettes at y is jointly inversion-symmetric". That is a
  gauge-invariant condition and exactly NG-wit's class. The quantifier "for every spanning tree containing a star corner
  tree" therefore only serves to name members of the class; it does not enlarge the class.

---

## (3) Lemma NG-ax and the correction to REVIEW_X11 (4b) (priority 3)

**Lemma NG-ax (l.4679-4686): CORRECT.**
- A centred Gaussian A on the non-tree links is invariant under A ↦ -A, which is V ↦ V⁻¹ on the three corner variables. O is
  odd and bounded, so E[O(y)] = 0 for any covariance and any coupling.
- The centring remark is right: the only Ad-invariant vector of su(N) is 0.
- One precision: on a torus the axial-gauge Maxwell "Gaussian" is improper along the toron directions. So "Gaussian" must
  mean a proper Gaussian law, with torons excluded or compactified.

**Correction to REVIEW_X11 (4b): CORRECT; this reviewer accepts it.** NG-wit's sign-symmetric class is the class of (2)(b). It
contains the exponentiated centred Gaussian connections of any complete gauge, at any site where the tree contains a star
corner tree. REVIEW_X11's "the only sign-symmetric competitor is an exactly abelianised / Lie-linear law (a strawman)" is
withdrawn. REVIEW_X11's other point stands: no finite-lattice Wilson-type measure is sign-symmetric, so NG-red's content is
the uniformity of its bound.

**New hostile qualification (binding wording).** The excluded objects are the **gauge-invariant shadows** of axial Gaussians,
and these are not translation invariant.
- For the Maxwell covariance in the comb gauge the reviewer computed the Gaussian value of the witness, κ_PO^comb(y), at
  T = 12 (`rev_kappa2_out.txt`; order (4, 3, 2, 1), coordinates (x_1, x_2, x_3, x_4)):

  | site y | κ_PO^comb(y) |
  |---|---|
  | (0, 0, 0, 0), (1, 0, 0, 0), (6, 0, 0, 0) | 0 |
  | (0, 1, 0, 0) | 0.00476 |
  | (0, 0, 1, 0) | 0.00845 |
  | (0, 0, 0, 1) | 0.00871 |
  | (1, 1, 1, 1) | 0.00863 |
  | (0, 0, 0, 6) | 0.00827 |

- So the shadow ν has ν(O(y)) = 0 only on the comb's root line and a positive value elsewhere. A translation-invariant limit
  point ω could never equal such a ν: ω(O(y)) is constant in y.
- Hence "no limit point is the gauge-invariant shadow of a centred Gaussian connection in any complete axial gauge"
  (l.4742-4743) is true but, for the Maxwell covariance, already follows from translation invariance.
- What Theorem NG-ax adds is the quantitative **marginal** statement: the corner-triple law of ω at any site is at TV
  distance ≥ u_+⁻²|c(t_0)|/(4||O||_∞) from the corner-triple law of ν at its root. Rewrite l.4742-4743 and l.4752-4755 in that
  form.

---

## (4) Theorem NG-ax, the exclusion list, the tree-level value, (c3-nz) (priority 4)

### (4a) Theorem NG-ax (l.4730-4749): CORRECT as an implication; a corollary

- The proof is NG-red's bound, plus translation invariance at level j, plus Lemma NG-ax at the site with a star tree.
- The TV step: |∫O d(ω_3 - ν_3)| ≤ 2||O||_∞·||ω_3 - ν_3||_TV, with TV = sup_A|ω_3(A) - ν_3(A)|. So the constant /(4||O||_∞) is
  right for that convention. **State the convention.**
- The hypotheses are exactly NG-red's (l.4731-4734). The v2 names are right, up to the stale items in (6).
- **Count:** by (2)(b) the conclusion is NG-red's "not sign-symmetric", read through Lemma AX. Relabel it **Corollary NG-ax**
  (uncounted), and count **Lemma AX** in its place (the new, checked statement that decides T35 (i), as Lemma PO decided T33).
  PROVEN-HERE stays 58.

### (4b) The exclusion list (l.4751-4764)

- **Excluded:** correct, with the (3) rewording (root-site marginal).
- **Not excluded (ii)** ("maximal-tree gauges with no star corner tree: undecided") **can be partly decided.** At any site where
  𝔗 has no star corner tree, the Maxwell-covariance Gaussian gives E[O] ≠ 0 at tree level.
  - Reviewer computation: random spanning trees at the origin give κ_PO^tree = 0.0084, 0.0054, 0.0101 at T = 6, 8, 12.
  - The off-root comb sites give κ_PO^tree between 0.0048 and 0.0087.
  - So these Gaussians are not excluded **through those sites**, by the same mechanism as covariant gauges. "Undecided"
    remains right only for arbitrary covariances.
- **Add (v):** the exclusion is at the g-dependent resolution m_* ≍ log(1/g) only, and is conditional on (CE-cond^3), which
  includes c(t_0) ≠ 0 [(c3-nz) ARGUED].

### (4c) The tree-level Wilson value: CONFIRMED independently

**By hand.**
- Write U_b = e^{ga_b}, tr(T^aT^b) = -½δ. For anti-Hermitian Y, Re tr Y³ = 0, so Re tr(1 - e^Y) = -½tr Y² - (1/24)tr Y⁴ + ….
- With Y_P = gL + g²B + O(g³), B = ½Σ_{i<j}[X_i, X_j] (BCH for four exponentials):
  (2/g²)Re tr(1 - U_P) = ½|L|² - 2g tr(LB) + O(g²) = ½|L|² - gΣ_{i<j}tr(L[X_i, X_j]) + O(g²). This matches l.4707 and the sign
  is right.
- O = g³O_3 + g⁴O_4 + O(g⁵) with O_3 = tr(L_12[L_23, L_31]) and O_4 = Σ_cyc tr(B_P[L_Q, L_R]) (cyclicity). The order-g⁴ terms of
  E[O] are E_0[O_4] and -g⁴E_0[O_3S_3'] = +g⁴Σ_{P'}Σ_{i<j}E_0[O_3 tr(L'[X'_i, X'_j])].
  - With tr(A[B, C]) = -½f^{abc}A^aB^bC^c, pairings inside one f-cubic vanish. Each cross pairing σ gives
    f^{abc}f^{σ(abc)} = sgn(σ)N(N² - 1). Hence E[tr(A[B, C])tr(D[E, F])] = ¼N(N² - 1)det γ_{(ABC),(DEF)}. This is l.4710's κ_V.
- The Haar Jacobian is even (degree-2 correction × odd O_3 gives degree 5 → 0). The covariant-gauge ghost loop with one gluon
  is ∝ f^{abb} = 0. A complete tree gauge has no Faddeev-Popov factor at all.
- So **κ = κ_PO + κ_V is the complete order-g⁴ coefficient. Correct.** The formal-expansion caveat (ARGUED, l.4727-4728) is
  right.

**By computer (reviewer's code, written from scratch).** Site-major indexing; own FFT Feynman propagator; own sparse
incidence and CG; numpy determinants.

| Check | Result |
|---|---|
| (S3) odd part (S(h) - S(-h))/(2h) of exact SU(2)/SU(3) plaquettes vs -Σtr(L[X_i, X_j]), 80 random plaquettes | max rel. error 4.5·10⁻⁶ at h = 10⁻³ (O(h²), as expected). This confirms S_3's sign and normalisation independently of BCH |
| (W) the two-cubic Wick formula, SU(2), random 6×6 Γ, exact brute-force Isserlis (15 pairings × 3⁶ colour sums) | -67.265433026028 both sides, difference 0 |
| Feynman, own code | κ = 0.0127993 / 0.0128190 / 0.0128255 / **0.0128266** at T = 6 / 8 / 12 / 16. This reproduces x11 to 7 digits |
| comb at root (C0) | 0.0126793 / 0.0127670 / 0.0128101 / 0.0128201, κ_PO ≡ 0. This reproduces x11b |
| **comb, corner at (0, 0, 0, T/2), all 9 corner links non-tree (C1)** | κ_PO = 0.008313 / 0.008282 / 0.008270 / 0.008269 and κ_V = 0.004486 / 0.004538 / 0.004555 / 0.004558; **sum equals Feynman** (k - k_F = +2·10⁻⁹ at T = 8, +3·10⁻¹¹ at T = 12) |
| **random spanning trees (random-weight MST), corner at origin** | κ_PO ranges over 0.0054-0.0101 by seed; **\|sum - Feynman\| ≤ 4.4·10⁻⁷ at T = 8, 12** (4 trees) and 7·10⁻⁷ at T = 6 (1 tree) |
| comb order (1, 2, 3, 4) at its root | k - k_F = -1.5·10⁻⁶ (T = 8), -2.1·10⁻⁷ (T = 12) |

- **Finding: the residual is localised, not generic.** The root-comb deviation from Feynman is -1.2·10⁻⁴, -5.2·10⁻⁵, -1.55·10⁻⁵ and
  -6.5·10⁻⁶ at T = 6, 8, 12, 16. That is **exactly ∝ T⁻³** (coefficient 0.0266), and the root-line sites carry the same
  deviation. Off the comb's skeleton the deviation falls to 10⁻⁹-10⁻¹¹.
- It is a finite-T inequivalence of zero-mode-dropped perturbation theory between gauges, concentrated where the comb's
  lower-dimensional tree structure sits. It is **not** the toron minimum-norm choice: every contraction has a corner curl on
  one side, so the null-space component never enters, in either gauge.
- T⁻³ extrapolation of the root comb gives 0.012827, in agreement with the covariant T = 32 value 0.0128271.
- **Verdict:** κ = 0.012827 (5 digits) is gauge-invariant across four gauge families. Within 1·10⁻⁶ at T ≥ 12 it agrees off the
  comb skeleton. E_W[O] = 0.012827·N(N² - 1)g⁴: SU(2) 0.0770g⁴, SU(3) 0.3078g⁴. **CONFIRMED.** The 64% path-ordering share in
  covariant gauge (0.008268/0.012827 = 0.645) is right. "Entirely the vertex in axial gauge" holds at the root (and the root
  line) only. Off the root the comb split is ≈ the covariant split (C1).
- Correction (non-binding) for l.4715 and §21.4: describe the comb residual as "T⁻³, localised on the comb's root line;
  off-skeleton comb sites and random trees agree to ≤ 5·10⁻⁷". Record the reviewer's confirmation.

### (4d) Is c(t_0) ≠ 0 plausible to prove?

- **Plausible, but it is a different computation from x11.** c(t_0) is the order-g⁴ value of the n-step conditional law at a
  trivial level-(k + n) background. Its ingredients are:
  - the fluctuation (blocked, coarse-pinned) propagator at level k;
  - the **cubic vertex of the level-k tree-level action**, which for k = j + in → ∞ is the classical blocked (perfect) action
    E_k^br of BFT, not Wilson's;
  - the kernel φ's cubic terms.
- At k = 0 (Wilson plus one kernel step) it is a finite, exponentially localised lattice sum. A computer-assisted enclosure
  of it is realistic.
- For the level-uniform c(t_0) that (CE-cond^3) needs, the cubic Taylor data of E_k^br at V = 1 must converge in k. That is
  BFT-3 at n = 3, V = 1, k-uniform, which BFT_B l.477 records as "n = 3, 4 k-uniform: OPEN ⊂ BFT-4".
- So (c3-nz) consumes a layer-1 output that §21.3 omits (added in (6)). The Wilson value 0.0128 is evidence at level 0 only.
- The session's "Next" (c(t_0) at n = 1 in a complete axial gauge) is the right first computation. Its axial-gauge advantage
  (pure vertex) holds only for a corner at the tree root, and the reviewer's T⁻³ finding says to place the tree root at the
  corner and extrapolate in T.

---

## (5) x11 and x11b (priority 5)

- **Order.**
  - §21.0 05:02 < x11 criteria ~05:04 < x11 run 05:04:36-05:04:41.
  - x11b criteria ~05:07, **written after reading x11** (disclosed in the file, §21.4 and the LOG), < x11b run 05:07:46-51.
  - §21.1-§21.5 written from 05:09. Consistent.
- **x11 D FAIL: honestly reported, correctly diagnosed.**
  - The pre-registered absolute threshold 10⁻² ignored the |X|⁴ size of unit Gaussian SU(3) logs, and the two g values used
    fresh samples (x11_vertex.py draws inside the g-loop).
  - The ratio 0.187 passed. D' (same samples, three g values, ratios 0.100, 0.100) is a legitimate post-hoc re-test.
  - The reviewer's (S3) is an independent pass.
- **x11 A1: correctly disclosed as structurally vacuous.** Covariant-gauge changes add k̂_μk̂_ν/k̂⁴ (pure gradient) terms, and
  every Wick contraction has a corner curl, which annihilates gradients. Hence each part is ξ-independent to 10⁻¹⁶.
  - Consequence, stated plainly: the pre-registered load-bearing check of x11 tested nothing. The only discriminating test
    of κ_V's sign and normalisation was x11b F2, written post hoc.
  - That is disclosed. It also makes the reviewer's independent C1 / random-tree agreement load-bearing for the value.
- **x11b F2: an honest real test.**
  - The 5% tolerance is loose. Equality λκ_V^tree = κ_PO^cov + λκ_V^cov solves to λ = 1.0018 at T = 12, so the overall vertex
    factor is fixed to 2·10⁻³.
  - "Agreement 1.2·10⁻³ at T = 12" is accurately reported.
  - The implicit attribution of the residual to generic finite size (the criteria's toron remark) is imprecise; see (4c).
- **x11 B, C, E:** correct as stated. B tests κ_PO only. C is a genuine test (MC against the determinant formula, 0.92 and
  0.49 SE). E's 8 × 2 × 50 identification is correct.
- **Re-run of x11b (mandatory lock):** see (7). Output **byte-identical to checks/x11b_out.txt except the wall/RSS line**
  (4.3 s / 123 MB against 4.2 s / 122 MB).

---

## (6) The consumer list §21.3 (priority 6): corrected

**Defects of §21.3 as written (05:10 UTC), against layer 1 as read 05:18-05:35 UTC.**
1. **Omitted owners.**
   - HW.md (lane H, (H-w)) is not cited. Its net statement (HW l.968-971, CONDITIONAL): **(H-w') ⇐ (F_R) [g_K² ≤ 1/(2R)] +
     (CLS-min) + (LI^F) + (M-f^A)_θ**, "Scope: SU(2) (SU(N ≥ 3) needs (KS-N)), bad-only defects (the collar extension is not
     covered by HW^cap)".
   - HIST-sum consumes (H-w') unchanged (HW l.127-130). K5 is resolved (HW §5.3) and K3 is settled for B_0 (HW l.433-434,
     l.461-462). REVIEW_HW_S2 confirmed this with fixes, all applied (HW §18).
   - **This is a scope gap for an SU(N) existence statement:** (KS-N) and the collar-bad extension ((TC), (M-i), (M-f)_{96θ},
     HW l.1012-1013) must be listed.
2. **Branch (iii) is mis-routed.**
   - SQ.md (lane G) verdict (SQ l.72-74): branch (iii) "does NOT consume the energy form (AE) for general chains". It
     consumes a lower bound on the cone-local infimum. Its price is Corollary PRICE-iii ⇐ **(REG-min) [OPEN, B-NA class]**
     plus proven pieces (SQ l.380-381).
   - (AE) itself is CONDITIONAL ⇐ (MS-Sob) (HIST l.1894; REVIEW_HIST_S4 confirms AE-red). It is not "ARGUED, (AE) OPEN".
   - REVIEW_SQ_S2 (05:03; fixes not yet applied in SQ): "(REG-min) OPEN; its wall = (MIN-reg)_cone", and the route via
     (BFT-cone) + (MIN-reg)_cone is "close to circular".
3. **FLOW is stale.**
   - (U-loc) is CONFIRMED (REVIEW_FLOW_S3 l.39; REVIEW_FLOW_S4 l.262-266), not "unreviewed". RLARGE l.401's own label is the
     stale source.
   - (U-IR) is OPEN but split (FLOW l.2039-2045): (a2) transverse, (a3), (a4'), (b), (c⊥) root sectors, (COV-GI) remainder,
     (U-IR-s)(s1), (s2⊥), **(COV-GI-∞)**, and the IR-safe root-sector grouping. REVIEW_FLOW_S5 §7 calls the root-sector
     programme (R1)-(R4) "the crux".
   - FLOW session 6 (in progress at 05:18-05:35) claims §45 proves (COV-GI-∞) at fixed n **given (L-loc)** (FLOW l.832,
     l.1756, l.1853). So **(L-loc) now enters the (F_R) chain as well as (M2)**.
   - FLOW imports GS-1 and GS-2 (e) from this lane's §14 (FLOW l.1876-1877). They rest on layer-1 (R) and Lemma 2.4 only
     (l.737-738), so there is no circularity.
4. **SF is stale (05:16 edits).** CE-Q (band) is now ⇐ (FP-loc)_0 + **(BGC)**, counted only with Fix Q1, and "superseded by
   CE-Q-col §13.1" (not yet written). The (CE-Q^∞) → RLARGE branch (ii) handoff is **withdrawn** (SF l.1211-1212, l.1311;
   REVIEW_SF_S3 l.197). REVIEW_SF_S3 also names a new OPEN item, CE-Q-col.
5. **BFT status is stale.** BFT_A and BFT_B (session 1, 04:56 / 05:10) exist.
   - **BFT-0/1/2:** Theorem BA is "PROVEN as an implication" on 𝒞_glob ⇐ (H-lin^∇) [OPEN], (H-rem^∇) [ARGUED], (FP♯') (BFT_A
     l.205). It gives θ_w = 2.
     - REVIEW_BFT_A_S1 l.31-33: "CONFIRMED as an implication on 𝒞_glob. It is B-NA-red re-instantiated in 𝔐^∇ plus BA-9, not
       BFT-0/1/2 on BFT's class".
     - (H-lin^∇) "as stated … is therefore false for α > θ" (GAP F3/F4). Z^lift lies outside every BFT-admissible ball.
   - **BFT-3:** Theorem BB-3_1 is PROVEN-HERE at k = 1, all n, rate Lμ_1/n (BFT_B l.474). General k (n ≤ 4) ⇐ BFT-0/2 +
     (H-𝔊_w), with (H-𝔊_w) ⇐ (LEG_w) [ARGUED] + (LOC-ζ) + BFT-1 (θ_w > 0) (l.476). Unreviewed.
   - **BFT-4:** BB-loc PROVEN at k = 1; the bound (BB-mix) is OPEN (l.479-482); B4-F1 "(O3) FAILS in ||·||_𝒜". Unreviewed.
   - **BFT-5:** no lane file states or owns it (stated only in REVIEW_S22 l.419-421).
6. **(L-loc)_k's ARGUED item (l.4803, l.4850) is mis-aimed.** BFT-3 as stated is n ≤ 4 (REVIEW_S22 l.412), but BFT_B proves
   all-order decay at k = 1 (Theorem BB-3_1, rate μ/n). BFT_B identifies (L-loc)'s missing input as **BFT-4's (BB-mix)**, "with
   the addition that per-cube smallness (not only decay) is required" (l.510-512). Restate: "(L-loc)_k ⊂ (BB-mix) (BFT-4), not
   supplied by BFT-3; all-order decay alone is insufficient".
7. **(BG-reg) ⇐ BFT-1 + BFT-3 is this lane's own inference.** No layer-1 file names (BG-reg); "owner REVIEW_S22 Part 5" is
   wrong. Mark it [inference, this lane] and count it ARGUED. Its inputs as of now: one-step locality at k = 1 PROVEN
   (BB-3_1); general k ⇐ (H-𝔊_w) OPEN; BFT-1 only as BA's implication on 𝒞_glob.
8. **(N5-unif) "⇐ BFT-0,1,2,4 without (H-K)"** is REVIEW_S22 l.426's routing. BFT_B's Corollary BB-4c (l.486) keeps (H-K):
   "NAH-unif′ ⇐ (H-K) + BFT-2 + BFT-4". List the BFT route as "REVIEW_S22 routing, not confirmed by BFT_B".
9. **Mis-attributions.**
   - "(a5-G♯)" is SF's name (SF l.680) and REVIEW_HIST_S4's fix S4-1. HIST still says (a5-G) (HIST l.1660).
   - The BFT-5/BFT-0 wiring of (a5-G♯), (a5-U), (MIN-reg) is REVIEW_S22's (l.427). BFT_A does not discharge (a5-U) or
     (MIN-reg).
   - (BG-unif)'s owner is PROOF (B-NA) and RLARGE #3a ("named, not precisely stated in PROOF"), not HIST §6/§8 (HIST has no
     (BG-unif)).
   - "v2 §0, #1": the #-numbering is RLARGE §4.2 (l.397-425); §0 only states (F_R).
   - LINEAR_PACKAGE is now FROZEN v1.1 (errata only), not v1.
10. **Omitted input of a counted theorem:** (c3-nz)'s level-uniform constant needs BFT-3 at n = 3, V = 1, k-uniform (see (4d)).
    It is ARGUED, so this is not a counted hypothesis, but the interface must show it.

**Completeness check against ASSEMBLY (I)-(IV) and §13-§21.** Every row of the ASSEMBLY table (l.2556-2566) maps to A, B, C or E
below, including (H-cont^S_sp) ⇐ (H-corr^S) (→ (SF)_k / N5) + (H-lin^S) and (PLD^mod_dis). With items 1-10, no counted
hypothesis is unmapped.

### Corrected §21.3 (statuses as read 05:18-05:35 UTC 2026-10-28; owners' labels; "this lane" = EXISTENCE's own)

**A. Unconditional soft structure (ASSEMBLY (I)).**
- X-LRP (PROOF L9a; IMPORTED-AND-REVERIFIED here).
- L9a′ (PROOF; PROVEN there).
- D4-norm (PROOF [S9]; PROVEN there).
- A1 = LINEAR_PACKAGE Lemma 2.2 (**FROZEN v1.1**; PROVEN there).
- (R) (LINEAR_PACKAGE §1.2).
- C-invariance of kernels and μ_K (this lane, proof of NA-3).
- No open layer-1 input.

**B. Flow and large fields.**

| Consumed as | Layer-1 output | Owner | Status (owner's, as read) |
|---|---|---|---|
| (O1), (F) | **(F_R)** on the chain's own sequence, with tuning (RLARGE §0; §4.2 #1) ⇐ F-flow/F-tune ⇐ (UNIV-1L) ⇐ Theorem UNIV ⇐ (U-loc), (U-IR); + (SF-g), (RLF-δ)_k (#2), (SF-cont), (SF-∞) | FLOW §4, §7, §18, §23, §36-§45; RLARGE §0, §4.2 | F-flow, F-tune PROVEN-HERE given the listed items (CONFIRMED conditional). **(U-loc) PROVEN-HERE, CONFIRMED** (REVIEW_FLOW_S3/S4). **(U-IR) OPEN, split:** (a2) transverse, (a3), (a4'), (b), (c⊥) root sectors, (COV-GI) remainder, (U-IR-s)(s1), (s2⊥), **(COV-GI-∞)** (session 6 in progress: ⇐ (L-loc) at fixed n), root-sector (R1)-(R4) = the crux (REVIEW_FLOW_S5 §7). UNIV's proof is being re-split ([RFL5-fix S5-1]) |
| (RLF-3^dis) → Theorem CB → (LF-loc), (LF-loc)^{ε_1}, (MOM_4) | (RLF-3) per history + **Theorem HIST-sum**, consuming **(H-w')** (HW l.130); with (RLF-1), (RLF-4), the K8 reading (§17.8) | RLARGE §1.2, §5.2; HIST §7.4; **HW.md** | HIST-sum CONDITIONAL ⇐ (H-w) (CONFIRMED). **(H-w') CONDITIONAL ⇐ (F_R) [g_K² ≤ 1/(2R)] + (CLS-min) + (LI^F) + (M-f^A)_θ** (HW l.968-971; REVIEW_HW_S2 CONFIRMED-WITH-FIX, applied). **Scope: SU(2), bad-only defects.** SU(N ≥ 3) ⇐ **(KS-N)** [HYPOTHESIS]; collar-bad ⇐ (TC), (M-i), (M-f)_{96θ}. Open inputs: (CLS-min) ⇐ (REG-min) [OPEN]; (LI), (LI^F) [OPEN, HW]; (M-f^A)_θ ⇐ (SF-cap)^A_θ + (SDP)^A_θ [OPEN, node A]; (NA-∅) [OPEN, node A]. Theorem RLF itself OPEN (RLARGE l.165, l.517) |
| (RLF-0) one shift per level | (RLF-0); **K9** | RLARGE §1.2, K9 | clause of the OPEN target; K9 "Not reconciled" (anisotropic tori need two shifts) |
| (PLD^mod_dis) | no v2 input ((PLD)_k withdrawn, [v2-A]); target T1 (PLD-mod) | PLD.md | this lane's HYPOTHESIS-NEW, layer-1-native |
| (O3) large fields o(g⁴) | three-way price: (i); (ii) ⇐ **(SG^fl)_k** (#7); (iii) ⇐ **Corollary PRICE-iii ⇐ (REG-min)** (SQ), alternative CLS-sf cone ⇐ CLS-red ⇐ (AE) ⇐ (MS-Sob) | RLARGE §3; **SQ.md §0, §9**; HIST §15, §26 | (i) PROVEN; (ii) PROVEN given (SG^fl)_k [HYPOTHESIS, clause of #3]; (iii) RLARGE "ARGUED". **SQ: PRICE-iii CONDITIONAL ⇐ (REG-min) [OPEN, B-NA class; wall = (MIN-reg)_cone, REVIEW_SQ_S2]**; (AE) **CONDITIONAL ⇐ (MS-Sob)** [(MS-Sob) OPEN] |
| (MOM_4) | CB + a prefactor-free (RLF-3^dis) at g-scaled thresholds | this lane (§20.2) | HYPOTHESIS-NEW; not stated by layer 1 |

**C. Small-field output at the observation level ((O2), NT-red, NT-pol, H-cont^S).**

| Consumed as | Layer-1 output | Owner | Status |
|---|---|---|---|
| (O2) | **(I_k^E)''** (RLARGE #4: "(I_k^E) HYPOTHESIS with GAPs S2-1..S2-3"), items (a3-q), (a4), (a5) = (a5-G) + (a5-U) | HIST §25; SF §6.2 | (I_k^E)'' HYPOTHESIS [P] (HIST l.1720). (a5-G) OPEN in HIST, restated as **(a5-G♯)** OPEN in SF l.680 (REVIEW_HIST_S4 S4-1: A5 ARGUED until restated). (a5-U), (a3-q) OPEN (lane D). **(G♯-patch)** OPEN = the B-NA wall (SF l.1320), reduced by BFT_A to (H-lin^∇) + G-pert + (COMM) + (UHL) + (SL-cov) [(COMM) GAP, REVIEW_BFT_A_S1]. BFT-5 ⇒ (a5-G♯): REVIEW_S22 routing; **no lane owns BFT-5** |
| (SF^J)_k (via (H-corr^S), (SG^fl)_k, (SF-irr)_{k+1}) | **(SF^J)_k** level-uniform (#3), **(BG-unif)** (#3a) | HIST §6, §8; PROOF N2, N4-N6; RLARGE §4.2 | (SF^J)_k OPEN, P×3-4. (BG-unif) HYPOTHESIS, owner PROOF (B-NA) (SF l.81), "named, not precisely stated in PROOF" (RLARGE #3a). BFT-0, 1 (θ_w = 0), 2, 4 route: REVIEW_S22 l.426; BFT-0/1/2 only as BA's implication on 𝒞_glob (not BFT's class, REVIEW_BFT_A_S1); BFT-4 (BB-mix) OPEN |
| (SF-bg^tor), torus term set of (a3-q) | (I_k^E)'' items at flat non-trivial backgrounds on wrapping polymers | HIST / SF | not stated in any layer-1 file |
| NT-pol | (O1)-(O3) + CLS-cone + (a3-q) | as above | CLS-cone CONDITIONAL ⇐ (AE) (HIST l.1372), hence ⇐ (MS-Sob) |

**D. Conditional weak-coupling input of SPEC-red^ms, NG-red, Corollary NG-ax** ((CE-cond^ms), (CE-cond^3) are this lane's
HYPOTHESIS-NEW; (M1), (M2) co-binding).

| Item | Layer-1 output | Owner | Status |
|---|---|---|---|
| (M1) band | **Theorem CE-Q (band)** | SF §10.1 | analytic part PROVEN-HERE (counted, **with Fix Q1**); as an integral statement CONDITIONAL ⇐ (FP-loc)_0 **+ (BGC)**; "superseded by CE-Q-col §13.1" (not yet written; REVIEW_SF_S3 names **CE-Q-col** OPEN) |
| (M1) deep set, localised | **(CE-Q^∞)** localised | SF §10.1 (§12.2/§13.2 announced) | **OPEN.** The RLARGE branch (ii) handoff is **withdrawn** (circular; SF l.1211-1212, REVIEW_SF_S3 l.197). There is no current owner of the U-variable pricing |
| (M1) coarse large-V away from N_R | RLARGE §3.2 branch (iii) | RLARGE §3.3; **SQ** | ⇐ PRICE-iii ⇐ (REG-min) [OPEN] (or ⇐ (AE) ⇐ (MS-Sob)) |
| (M1) the localised expansion, P_K-price of Z-events in Ω | **(CE-loc)** | this lane's name; SF | not stated by layer 1 |
| (M2) level-uniform stage-j | **CE-exp^k**, k = j → ∞ ⇐ (i) N_μ(\|𝒞_k\|) < ∞ ⇐ (N5-unif); (ii) **(L-loc)_k**; (iii) (FP-loc)_k, (N5-reg)_k, criticality; (iv) inherited activities of (I_k^E)'; (v) CE-exp-col | SF §7.1, §10.3, l.857-859, l.1318 | CE-exp^k CONDITIONAL. (N5-unif) CONDITIONAL ⇐ (H-K) + (H-C⁺) + (H-ℂ) (the BFT route without (H-K) is REVIEW_S22's; BFT_B BB-4c keeps (H-K)). **(L-loc)_k OPEN, B-NA wall; its missing input is BFT-4's (BB-mix) with per-cube smallness (BFT_B l.510-512); BFT-3 (n ≤ 4) does not supply it; all-order decay at k = 1 is PROVEN (BB-3_1) and insufficient.** (FP-loc)_k [OPEN; s to P], (N5-reg)_k [OPEN; s]. CE-col PROVEN-HERE (counted; rate sense), CE-exp-col PROVEN-HERE (uncounted), CONFIRMED (REVIEW_SF_S3) |
| (M2) source step | Lemma CE-cov over Theorem CE-exp | here; SF §7.1 | PROVEN |
| (M3) reference values | (A-cond); c(t_0) ≠ 0 ((c3-nz)) | this lane; **+ BFT-3 at n = 3, V = 1, k-uniform** (cubic data of E_k^br) | (A-cond) inside (CE-cond^ms); (c3-nz) ARGUED (Wilson level-0 value 0.012827·N(N² - 1), confirmed by REVIEW_X12); BFT-3 n = 3 k-uniform "OPEN ⊂ BFT-4" (BFT_B l.477) |
| (M4) | **(BG-reg)**: \|B_D(V)\|² ≤ c_BL⁻⁴ⁿQ_w(V) | **this lane's routing [inference, ARGUED]:** ⇐ BFT-1 (θ_w > 0) + BFT-3 (n = 1) | (BG-reg) not stated by layer 1. Level-1 locality PROVEN (BB-3_1, unreviewed); general k ⇐ (H-𝔊_w) [OPEN]; BFT-1 only as BA's implication on 𝒞_glob |
| (M5) | (MOM_4) (row B) | | |
| RP of the soft chain | X-RP^S (from L9a′) | here | PROVEN-HERE |

**E. This lane's own open items.**
- (H-sig^S_loc), (WC_∞)/(WC_∞^sp).
- (H-cont^S_sp) ⇐ (H-corr^S) [→ C] + (H-lin^S) ⇐ (NA-R2^bg).
- (NA-R2), X-ROT, X-IR, X-SRC-GAP.
- HYPOTHESIS-NEW: (CE-cond), (CE-cond^ms), (CE-cond^3), (MOM_4), (RLF-3^dis), (PLD^mod_dis), H-loc-LF, H-sg, H-Bal-loc.
- (CE-loc) as named here.

**Not consumed by any counted theorem.** Theorem CE directly; v2 (SF-last), except through RLF-4; PLD-AF; (TRACK); Theorem TS;
H-Bal-2.

**The interface in one line (corrected).** Layer 1 must supply:
- **(F_R)** [(U-IR) sub-items; root sectors R1-R4; (COV-GI-∞) ⇐ (L-loc)];
- **HIST-sum with (H-w')** [(CLS-min) ⇐ (REG-min), (LI^F), (M-f^A)_θ; **(KS-N) for SU(N ≥ 3)**; the collar extension];
- **(I_k^E)''** [(a5-G♯)/(G♯-patch) = B-NA; (a5-U), (a3-q) lane D];
- **(SF^J)_k** with (SG^fl)_k and (BG-unif);
- branch (iii) via **(REG-min)** (or (AE) ⇐ (MS-Sob));
- for the weak-coupling input: **(CE-Q^∞) localised (no owner since the handoff was withdrawn) + (CE-loc)** and **CE-exp^j
  level-uniform** ⇐ **(L-loc)_j ⊂ (BB-mix) (BFT-4)**, (FP-loc)_j + (BGC), (N5-reg)_j, (N5-unif); plus BFT-3 at n = 3 k-uniform
  for (c3-nz).
- **Walls touched twice:** (L-loc) (by (M2) and by FLOW's (COV-GI-∞)) and (REG-min) (by (H-w') and by branch (iii)). These are
  the two highest-leverage layer-1 items for this lane.

---

## (7) Re-run under the mandatory numeric lock (priority 7)

- **Acquisition 1.**
  - `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`; acquired 05:22:46 UTC after waiting (another
    holder had it at 05:20).
  - Load 2.77 (< 8); 44% memory free. nice 10; OMP/OpenBLAS/MKL/vecLib threads 1; `python3` without -I; no `timeout`; no
    trap.
  - Ran x11b (4.6 s, 128 MB) and the reviewer's rev_kappa.py (58.5 s, 216 MB). A single `rmdir` at 05:23:49.
- **Acquisition 2.** Same rules, for the site-dependence diagnostic rev_kappa2.py: 05:26:07-05:27:15, load 5.58, 40% free, 67.9 s,
  118 MB, a single `rmdir`.
- After both: the locks directory is empty and no process is left running (checked with `pgrep`).
- **x11b output: byte-identical to checks/x11b_out.txt except "wall 4.3 s; peak RSS 123 MB"** (recorded: 4.2 s / 122 MB).
- Files (scratchpad `rerun_x12/`): x11b_out_rerun.txt, rev_kappa.py, rev_kappa_out.txt, rev_kappa2.py, rev_kappa2_out.txt,
  time.txt, run_locked.sh, run2.sh.

---

## (8) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| RX11 fixes 1-11 | CONFIRMED. Fix 2 went stale at 05:16 (SF: + (BGC); branch-(ii) handoff withdrawn). Fix 9: C-covariance is recorded in ASSEMBLY (I), not ARGUED |
| Lemma AX (8 star corner trees; comb rule) | CORRECT; the null class is 𝔗-independent; star trees exist along the whole root line |
| Lemma NG-ax | CORRECT (proper Gaussians; torons excluded) |
| Correction to REVIEW_X11 (4b) | CORRECT; REVIEW_X11's "strawman" remark withdrawn |
| Theorem NG-ax | CORRECT as an implication; a corollary of NG-red + AX: relabel, count AX instead; reword as a root-site marginal statement (axial-Gaussian shadows are not translation invariant) |
| Exclusion list | correct; (ii) partly decidable (Maxwell-covariance Gaussians at non-star sites give E[O] ≠ 0); add the m_* and (c3-nz) qualifiers |
| Tree-level E_W[O] = 0.012827·N(N² - 1)g⁴ | CONFIRMED by hand and by independent code in four gauge families; the comb residual is a T⁻³ effect localised on the root line |
| c(t_0) ≠ 0 | plausible (finite tree-level sum at k = 0); level-uniformly it needs BFT-3 at n = 3 k-uniform (OPEN ⊂ BFT-4); stays ARGUED |
| x11 / x11b | honest. D FAIL correct; A1 vacuous, so x11b F2 (post hoc) was the only discriminating test; re-run byte-identical |
| Consumer list §21.3 | INCOMPLETE and partly STALE (items 1-10 of (6)); replace with the corrected list |

**Tally.**
- **Claimed:** PROVEN-HERE 58 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 9 / OPEN 12;
  ARGUED 38.
- **Corrected: 58 / 1 / 3 / 9 / 12; ARGUED 39.**
- PROVEN-HERE +1 is kept, relabelled: **Lemma AX** is counted. Theorem NG-ax becomes Corollary NG-ax (uncounted), with Lemma
  NG-ax uncounted.
- ARGUED +3 (not +2):
  - (L-loc)_k, restated as "⊂ (BB-mix) (BFT-4); not supplied by BFT-3; all-order decay insufficient";
  - the formal coefficient (l.4727-4728);
  - **+1: (BG-reg) ⇐ BFT-1 + BFT-3**, an inference not stated by any layer-1 file.
- HYPOTHESIS-NEW and OPEN are unchanged. (NG-conn), re-posed, is answered conditionally by Corollary NG-ax and is not counted.
  Nothing new is counted for (KS-N), (REG-min) or (BB-mix): they are layer-1 items.
- The reviewer's computations are not counted.

---

## Binding fixes for session 13

1. **§21.3** (l.4766-4821): replace it with the corrected list of (6), including the SU(2) / bad-only scope of (H-w') with (KS-N)
   and the collar extension, branch (iii) via (REG-min), (AE) ⇐ (MS-Sob), (U-loc) CONFIRMED, (U-IR) split, (COV-GI-∞) ⇐ (L-loc),
   the BFT_A/BFT_B statuses and the BFT-5 non-ownership. Also LOG finding 4 and §0 l.199.
2. **Fix-2 residue** (l.183-184, l.4336-4345, l.4353-4357, l.4553-4556, l.4600-4602, LOG l.703-705):
   - "⇐ (FP-loc)_0 alone" → "⇐ (FP-loc)_0 + (BGC)" (SF [RSF3-fix SN-2]);
   - "(CE-Q^∞) priced in U-variables, RLARGE §3.2 branch (ii)" → "the branch-(ii) handoff is withdrawn by SF [RSF3-fix C-2];
     no current owner";
   - note CE-Q-col (OPEN).
3. **(L-loc) ARGUED item** (l.4803, l.4850): "beyond BFT-3's orders ≤ 4" → "⊂ BFT-4's (BB-mix) with per-cube smallness (BFT_B
   l.510-512); BFT-3 does not supply it, and all-order decay at k = 1 (BB-3_1) is proven but insufficient".
4. **(BG-reg) row** (l.4806): owner "this lane [inference]", ARGUED (+1 → 39). Update its inputs: BB-3_1 (k = 1) PROVEN; general
   k ⇐ (H-𝔊_w) OPEN; BFT-1 only on 𝒞_glob as an implication.
5. **(N5-unif) row** (l.4803): "or ⇐ BFT-0,1,2,4 without (H-K)" → "REVIEW_S22 routing; BFT_B BB-4c keeps (H-K)".
6. **Theorem NG-ax → Corollary NG-ax** (l.4730, l.4848-4849). Count Lemma AX instead (58 unchanged). Add after Lemma AX that the
   null class is 𝔗-independent (= joint-inversion symmetry of the corner triple at y).
7. **Reading of NG-ax** (l.4742-4743, l.4752-4755, §0 l.191-195, LOG finding 2):
   - The excluded object is the **root-site corner-triple marginal** of an axial-Gaussian shadow.
   - For the Maxwell covariance the shadow is not translation invariant (0 on the root line, 0.0048-0.0087·N(N² - 1)σ⁴
     elsewhere; REVIEW_X12 (3)), so the whole-law exclusion is largely implied by translation invariance.
   - The content is the TV bound. State the TV convention (sup over events).
8. **Exclusion list (ii)** (l.4702-4703, l.4759): for the Maxwell covariance, Gaussians in tree gauges at sites without a star
   corner tree give E[O] ≠ 0 at tree level (REVIEW_X12 (4b)): not excluded through those sites. "Undecided" stays only for
   arbitrary covariances. Add (v): only at resolution m_*, and conditional on (c3-nz).
9. **(c3-nz)** (l.4723-4728, l.4805): add that the level-uniform c(t_0) consumes the cubic Taylor data of E_k^br at V = 1,
   k-uniform (BFT-3 at n = 3, OPEN ⊂ BFT-4), and that the Wilson value is level-0 evidence only.
10. **x11/x11b record** (§21.4, l.4714-4719):
    - A1's vacuity means x11 had no pre-registered discriminating test of κ_V. Say so.
    - Replace the generic finite-size description of the comb residual by "∝ T⁻³, localised on the comb's root line;
      off-skeleton comb sites and random spanning trees agree with Feynman to ≤ 5·10⁻⁷ (REVIEW_X12 (4c))".
    - Credit the reviewer's independent confirmation, and record the x11b re-run (byte-identical except wall/RSS).
11. **Fix 9 cosmetic** (l.4463-4464): C-covariance "ARGUED" → "recorded in ASSEMBLY (I) (C-invariance of the kernels and of
    μ_K)"; the d-type members remain admissible.
12. **Tally** (§0 l.188-189, l.4846-4854, LOG): 58 / 1 / 3 / 9 / 12; ARGUED 39; Lemma AX counted, NG-ax a corollary.

---

## Strategic verdict

- **What session 12 established (correctly).**
  - Lemma AX is a clean, correct observation. It corrects REVIEW_X11: the sign-symmetric null class contains genuine
    non-abelian, path-ordered Gaussian connections (axial-gauge shadows), not only abelianised strawmen.
  - The tree-level Wilson value 0.012827·N(N² - 1)g⁴ is right. The reviewer confirms it independently in four gauge families,
    and it is gauge-invariant to ≤ 5·10⁻⁷ off the comb skeleton.
  - The RX11 fixes were applied faithfully.
- **What it is worth, honestly.**
  - (i) "Non-Gaussianity with the gauge named" is narrow.
    - It is NG-red's conditional "not sign-symmetric", now known to exclude the root-site marginal of axial-Gaussian shadows.
    - Those shadows are not even translation invariant, so the whole-law exclusion is mostly free.
    - Covariant-gauge Gaussians, the physically natural free-theory null model, are still not excluded.
    - Everything rests on (CE-cond^3), with c(t_0) ≠ 0 ARGUED. The level-uniform c(t_0) itself needs a BFT-4-class input.
  - (ii) The consumer list was the session's most useful deliverable, but it was written against a moving layer 1.
    - Within 10 minutes SF, FLOW and BFT_B changed it.
    - It never read HW, SQ, BFT_A or BFT_B, which carry the current (H-w') reduction (with an SU(2)-only scope), the branch-(iii)
      re-routing through (REG-min), and the actual BFT statuses.
- **Recommendation, in order.**
  1. Apply binding fix 1 first. The corrected list shows two walls that this lane's statement consumes twice: (L-loc) ⊂ (BB-mix)
     and (REG-min). Name them to layer 1 as this lane's priority requests. Flag the **SU(N ≥ 3) gap** ((KS-N)) in (H-w'): the
     existence statement is stated for SU(N).
  2. Re-date the consumer list against file mtimes, and re-read SF §12-§13 and FLOW §45 once they are written: both touch
     (M1)/(M2) and (F_R).
  3. For non-Gaussianity: stop extending the one-point witness. If the thread continues, compute c(t_0) at k = 0, n = 1, with
     the tree root at the corner and T⁻³ extrapolation. A covariant-gauge exclusion needs two-sided relative-g² control (REVIEW_X11
     (4c) items 2-3), which no hypothesis here supplies.
  4. Leave §12.1 unchanged. §21 is conditional on new, unadopted hypotheses.
