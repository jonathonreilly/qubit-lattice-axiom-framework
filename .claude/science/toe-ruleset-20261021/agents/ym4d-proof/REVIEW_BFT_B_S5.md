# REVIEW_BFT_B_S5: hostile review of BFT lane B session 5 (BFT_B.md [RBB4-fix] edits, §15-§17; check bb5)

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md, HIST.md, PROOF.md or the checks. This is the only
file I edited. No commits, PRs or pushes.

Inputs (read 2026-10-28 ≈08:40-09:00 UTC). `TZ=UTC stat`: BFT_B.md born 08:36:05, modified 08:36:46, 268561 bytes;
BFT_B_LOG.md modified 08:37:08, 26449 bytes; bb5_criteria.md born = modified 08:27:06; bb5_lift.py born 08:28:06, modified
08:28:21; bb5.out and bb5.out.time 08:28:31-08:28:34.
- BFT_B.md:
  - §12.0-§12.3 (l.1586-1697): Setting Π, (W-Π), (W-lin-Π), (CovLift), GI-F2.
  - §13.6 Step 2 (l.1836-1850).
  - Every [RBB4-fix] tag in context (26 tag strings, l.1609-2065).
  - §15-§17 and the session-5 FOR OTHER FILES (l.2003-2430), in full.
- BFT_B_LOG.md: session 5 in full.
- REVIEW_BFT_B_S4.md: bottom line, Parts A, C.4, E, F, and the fix list.
- BFT_A.md: §1.3-§1.4 (coarse units; 𝔐^∇), ||·||_inv (l.462), LRL (b) (l.1340-1356), §21.2 (b1)/(b2) (l.1743-1748).
- REVIEW_BFT_A_S4 Part 6.
- PROOF.md Lemma LES-div (l.3394-3407).
- checks/bb5_criteria.md, bb5_lift.py (line by line), bb5.out, bb5.out.time.

Re-run: bb5 under the numeric lock, plus two reviewer probes (exact mask-regularity computations). Record at the end.

---

## Bottom line

- **Provenance: CONSISTENT.**
  - File order: §15 (08:25:04) < Step 1 (08:26:44) < criteria (08:27:06) < script (08:28:06; last byte 08:28:21) < output
    (08:28:31-34) < §16 (08:35:44) < §17 (08:36:40). This matches the log.
  - Byte accounting confirms the log's sizes:
    - §15 as it stands (l.2003-2110) is 11283 bytes. Adding the 30-byte "# Session 5" header gives 11313, exactly the
      growth logged at 08:25:04 (217135 → 228448).
    - l.1-2110 now total 233687 bytes, against 233686 logged after Step 1. The 1-byte difference is the line boundary.
    - So nothing before §16 changed size after Step 1. The born time 08:36:05 is the logged 16.6 clarification (an atomic
      rewrite).
  - Two forward references:
    - §15's "[RBB4-fix RS4-1]" (l.2065) is disclosed.
    - Step 1's item-8 tag (l.1920-1925, written 08:26) says CL-blk was "tested and corrected in §16" before bb5 and §16
      existed. This one is **not disclosed** (cosmetic RS5-9). CL-blk itself was pre-stated in §15 at 08:25:04.
  - All five post-proof corrections are marked in §16's header (l.2113-2118). I checked them against §15; they are accurate.
- **[RBB4-fix] edits: all applied, correctly.**
  - Checked: RS4-1 (l.1619, 1658, 1741, 1781, 1837, 1956), RS4-2 (l.1627, 1754), RS4-3 (l.1808, 1817), RS4-4 (l.1692,
    1766-1772, 1895, 1958, 1982), RS4-5 (l.1791), RS4-6 (l.1609), RS4-7 (l.1879, 1963, 1996-1998), item 8 (l.1920).
  - One carry-over: GI-F2's status in §12.3, §13.6 and the §14 table must now follow Lemma CL-uniq (RS5-1).
- **Lemma CL-uniq: CONFIRMED. GI-F2 cannot occur for an orbit-covariant lift: CONFIRMED.** This retracts my S4 review's
  C.4 sentence that GI-F2 is "a genuine requirement near reducible or flat backgrounds".
- **Elliptic slice:**
  - Lemma EP-alg: **CONFIRMED**.
  - Lemma EP-int (given LES-div): **CONFIRMED**. This is the genuine "no Gaffney, no boundary regularity" mechanism.
  - Lemma Q-hold: **CONFIRMED**.
  - **Theorem EP-bd: CONFIRMED**, k- and T-uniform, reach 4, at the trivial chain (linear model).
  - **Theorem EP-opt: CONFIRMED** (one typo, RS5-2).
  - **Theorem EP-rec: CONFIRMED** (given LES-div, Lemma Λ, LR-pot). Its weighted constant c_r = 24 is ARGUED-level
    bookkeeping (RS5-4).
- **Corollaries:**
  - Corollary EP-lin: **CONFIRMED** as an implication.
  - **Corollary EP-LRL(b): CONFIRMED-WITH-FIX.** LRL (b) ⇐ (Res-Hölder)_m holds, but only for **T ≥ 5**, not LRL (b)'s
    T ≥ 3. N_res,m must also be defined (RS5-3).
- **Theorem RW^∇_k-Π(E): CONFIRMED as an implication.** The hard-slice RW^∇_k now has an admissible slice: (W-Π) is
  PROVEN for S_E. (W-lin-Π) for S_E is equivalent to the gauge-invariant (H-inv+), up to the sum-versus-max gap.
- **Proposition RATE-m: CONFIRMED as an implication.** κ_L → m/4 as R → ∞, so κ_L ≥ m/8 for R ≥ R_0. One constant is off
  by a factor 2 inside a logarithm (cosmetic, RS5-6).
- **Lemma CL-blk: CONFIRMED.** It corrects my S4 review's (R1) ("Φ commutes with all level-j gauges" must go). The
  threshold can be sharpened: the sup term already fails once L^{k-j} > C_sm (RS5-7).
- **Proposition CL-lin: CONFIRMED given φ ∈ C^{2,α}. The table's "(i)-(v)" is an overclaim:** CL-lin says nothing about
  (CovLift) (iv)'s second clause ||g_Z||_Y ≤ C_g||b|| (RS5-5).
- **Proposition CL-Φ: CONFIRMED as an implication.** The measured failure of its curvature hypothesis is real and has the
  expected size (×3^{1/4} per level, identical to Q1).
- **Mask regularity: settled here by exact computation.** Details and the choice of mask are in Part D.
  - **DD8 ternary: φ ∈ C^{2,β} with β ≥ 0.473. PROVEN** (exact rational arithmetic; standard m-ary difference-scheme
    theorem).
  - **DD6 ternary: φ ∈ C^{2,β} with 0.267 ≤ β ≤ 0.320.** The upper bound is from a spurious eigenvalue. So DD6 is PROVEN
    admissible at lane A's α = ¼, with little margin.
  - **DD4: NOT C²** (spurious eigenvalue 0.1358 > 1/9, smoothness ≤ 1.817).
  - Cubic spline: C^{2,1} (classical), but only exponentially local.
- **bb5: CONFIRMED.**
  - The script is correct line by line.
  - The re-run is **byte-identical** (timing line excluded).
  - DD6's pass is marginal on the 1.25 threshold (1.193/1.200). My exact computation, not the proxy, is what makes DD6
    admissible.
- **(CovLift): OPEN. The route has moved:** the linear level is now unconditional for DD6/DD8. What remains is nonabelian
  (Part E).

---

# PART A: provenance and the [RBB4-fix] edits

**A.1 Provenance: CONSISTENT.**
- Stat values are as listed in the header. They match the log line by line.
- bb5_lift.py's logged pre-run edit (08:28:21: the corner0 index offset, a no-op conditional, an unused line) touches no
  criterion. The criteria file mentions no session-5 constant. Its thresholds (×10, [0.8, 1.25]) are generic predictions.
- Pre-stated (§15) versus proven (§16), item by item:
  - EP-int: N_X → N'_X (half-width 3/2). Marked. It is what EP-bd and EP-rec need: the products χλ need λ just outside N_X
    for discrete Leibniz, and the 16.6 Hölder comparisons use N'_X.
  - EP-lin: converse constant (C_Q + 1). Marked.
  - CL-blk: "fails at depth ≥ 1" → "fails k-uniformly". Marked. The pre-statement's own bound cL^{k-j} contradicted
    "every depth ≥ 1" for C_sm > L.
  - CL-lin: residual constant 2 (not 2L²); finite range only for finite masks. Marked; both correct (B.10).
  - CL-uniq's GI-F2 consequence: new, marked, and flagged for review.
  - RATE-m: "κ_L ≥ m/c, c absolute" → c = 8. Consistent.
  - Nothing proven in §16 was absent from §15.
- §15's opening disclaimer ("exploratory reasoning … preceded this append; its only claim is file order") is honest and
  appropriate.

**A.2 [RBB4-fix] edits: CONFIRMED.** Each binding fix of REVIEW_BFT_B_S4 is applied in place, with the content I asked for:
- RS4-1: 4R + 14 + 2r_Π / 2r_Z; ℓ_Ω ≤ 4R + 12 + 2r_Z; 4R + 2r_Π + 6 in Step 3.
- RS4-2: full X-gradient; ΔE(1) uses A ∈ S.
- RS4-3: the residual part is ARGUED; the Feynman difference goes under (Mult-Y), at both sites.
- RS4-4: C^{2,α} tents; S_tent fails (W-lin-Π); elliptic slice; "kept" clause.
- RS4-5, RS4-6: applied.
- RS4-7: (Pair-loc), (I-id)_Z; unweighted versus weighted rate, in the SF line.
- Item 8: seventh candidate; MSG in own units.

Carry-over **RS5-1**: §12.3 GI-F2 (l.1686), §13.6 Step 2's last sentence (l.1844-1846) and the §14 rows (l.1962, l.1967)
still say "GI-F2 occurs without the cocycle". After CL-uniq they should read: "GI-F2 cannot occur for any lift that is
orbit-covariant at level 0 (Lemma CL-uniq). The cocycle is automatic."

---

# PART B: elliptic slice (§15.1; §16.1-§16.10)

## B.1 Lemma EP-alg (l.2038; proof l.2128-2142): CONFIRMED
- (a) Gauge shift. Correct: Ñ_X is connected, Neumann, so the kernel is the constants, fixed by λ(c_X) = 0.
  - The constrained first variation at c_X is not needed: the unconstrained minimiser modulo constants gives d*a = 0 at
    every interior site, including c_X.
- (b) Tents. I checked:
  - σ_5(t) + σ_5(1 − t) = 1;
  - σ_5' = −30t²(1 − t)²;
  - σ_5'' = −60t(1 − t)(1 − 2t), which vanishes at 0, ½ and 1;
  - |σ_5'| ≤ 15/8 at t = ½; |σ_5''| ≤ 10/√3 at t = ½ ± 1/(2√3).
  - So t ↦ σ_5(|t|) is C^{2,1}. Σ_Xχ^5_X = 1 and χ^5_X(c_Y) = δ_XY follow.
- (c), (d): Λ(x + DΛ) = Λ − Σχ_XΛ + Σχ_XΛ(c_X) = 0, because Λ(c_X) = 0. Projection, correct.
- (e): with 𝒢_0 = {Dμ : μ = 0 at level-k sites} (Setting Π, l.1590), Λ(Dμ) = −μ. So S_E ∩ 𝒢_0 = {0}. Correct.
  - This uses exactly 𝒢_0's level-k triviality. Without it, Dμ with μ = I_χ(root values) would lie in S_E.
- (g) Radius: Λ(z) reads boxes Ñ_X with |z − c_X| < 1, i.e. within 3; one more for links. r_Π = 4 is correct with slack.
- T ≥ 5 is needed for Ñ_X (side 4 coarse plus one site) to embed.

## B.2 Lemma EP-int (l.2041; proof l.2144-2170): CONFIRMED given LES-div. The "no Gaffney, no boundary regularity" claim is right
**How the argument avoids the box boundary (verified).**
- Step 0 is the L² projection property of the Neumann minimiser: a ⊥ d(ℓ²(Ñ)), so ||a||_{ℓ²(Ñ)} ≤ ||v + dμ||_{ℓ²(Ñ)} for
  every μ. That is the only global information used.
- Everything else is **interior**:
  - at interior sites, d*a = 0 and da = dv, so −Δa_μ = Σ∂^-_ν(±(dv)_{νμ}) componentwise (the lattice identity
    −Δ = d*d + dd* on Z⁴);
  - −Δλ = div(∓v), and differences commute with Δ.
- The interior Campanato step (LES-div) needs only the equation on Q_R(z) ⊂ interior. The Caccioppoli step brings the L²
  energy from Q_{R/2} down to Q_{R/4}. Step 0 bounds the L² energy on Q_{R/2} by the box's.
- So boundary corners and edges never enter: margin ½ coarse, with R = n/4 and box Q_R(z) ⊂ Ñ_X for z ∈ N'_X.
- A box Gaffney inequality would be needed only to control ∇a up to ∂Ñ_X. Nothing uses that.
- **EP-F1 and EP-F2 do not occur: CONFIRMED.**

**Checks of the details.**
- LES-div (PROOF l.3394-3407) is stated for −Δu = Σ∂^-_ag_a + h on Q_R, R ≥ 16, for Campanato of ∇u at 1 ≤ ρ ≤ R/4 on
  Q_{R/2}. It uses [g]_{α;Q_R} in L²-Campanato form.
  - Applied with u = ∂_bλ, g = ∓∂_bv, h = 0. The coarse-unit rescaling (H = n²∇u, g^c = n²∂v) is homogeneous of degree
    2 + α. The bound needs n ≥ 64.
- The small-k finite-dimensional argument is fine:
  - n_Ñ is a norm on x_0|_Ñ (it contains sup|x^c_0|);
  - the box is T-independent;
  - only finitely many k have L^k < 64.
- Caccioppoli (Step 2) is standard. The constant ḡ drops out against a compactly supported test function.
- Step 4's sup bounds by telescoping are correct; so is |λ| ≤ 4 sup|∇^cλ| (resp. 6) on N_X (resp. N'_X).
- (b) is gauge invariant, since a_X(x + dμ) = a_X(x). The right-hand side's free μ is legitimate.

## B.3 Lemma Q-hold (l.2048; proof l.2172-2184): CONFIRMED
- I re-derived the two gauge-part bounds with ρ_b = sρ_a:
  - |(dhv)^c| ≤ ρ_b^{-1}·2s·sρ_a²||∇^cv^c|| = 2ρ_b||∇^cv^c||;
  - its coarse gradient is ≤ ρ_b^{-2}·2s·sρ_a²ρ_b^α[∇^cv^c]^∞_α = 2ρ_b^α[·].
- The straight part is an average of translates of v^c, so it preserves sup, gradient and Hölder.
- BL-2 (b)'s formula h^{(a→b)} = Σ_iev∘h_i∘Q_str is exactly the composite of the one-level Q_i. Hence the composite
  Q^{(i+1→j)} in EP-rec's telescoping is the map Q-hold bounds, and C_Q is independent of b − a.

## B.4 Theorem EP-bd (l.2051; proof l.2186-2200): CONFIRMED (linear model, trivial chain)
- **Across box interfaces with quintic tents** there is no interface term at all:
  - Λ = Σ_Xχ^5_Xλ^E_X is a finite (≤ 16) sum of terms, each globally C^{2,α} after extension by 0.
  - The reason: σ_5, σ_5' and σ_5'' all vanish at t = 1. So second differences of χλ vanish at ∂N_X, and their Hölder
    modulus across ∂N_X is bounded by the one-sided modulus (×2).
  - The discrete Leibniz rule reads λ at shifted points just outside N_X. That is why EP-int is needed on N'_X; it is so
    proven.
- Level j:
  - (d ev^{(j)}Λ)^c is an average of fine ∇^cΛ along the link;
  - its level-j gradient is an average of fine ∇^c∇^cΛ over a ρ_j × ρ_j grid;
  - its Hölder seminorm is bounded by that of translates.
  - So the C^{1,α} norm at every level is ≤ 2||Λ||_{C^{2,α}}. I checked the averaging identity.
- Residuals are untouched, because both Q and Q_ax are root-covariant and ev^{(k)}Λ = 0. Correct.
- Weighted e^{4m}: correct (output reads input within 4).
- "C_Π for every v, u ∈ S not needed" is right.
- **Contrast with S_tent:** the box-Coulomb gauge gains one derivative over x_0 (Schauder), where the axial gauge integrates
  along lines and loses one. This is correct, and it is the real reason S_E works.
- **Scope (state explicitly, RS5-4 (c)).** EP-bd is a theorem about the linear slice at the trivial chain. The background
  (Z-covariant, nonlinear) version needed by 13.8 / GI-off is (N1) of CovLift-route, still OPEN.

## B.5 Theorem EP-opt (l.2054; proof l.2202-2212): CONFIRMED (typo RS5-2)
- The kernel computation is correct:
  - dx_0 = 0 on the torus gives exact plus a constant h;
  - r = 0 forces x_k = Q^{(0→k)}x_0, and with x_k = 0, L^kh = −mean(d ev λ) = 0;
  - so ker 𝓑 = 𝒢_0.
- Identification: π_S is the restriction of π (l.1589), so the slice problem's right-hand side is (πy)|_S. Then
  𝓑(Π_Ex, w) = ⟨πy, w⟩ for all w, and the identity holds for every y.
  - l.2208 writes ⟨y, w⟩. That is correct only because lane A's sources already annihilate 𝒢_0. Write ⟨πy, w⟩ (RS5-2).
- G_opt ≤ ||𝓛_{S_E}^{-1}π_{S_E}|| ≤ C_ΠG_opt: correct.

## B.6 Theorem EP-rec (l.2057; proof l.2214-2238): CONFIRMED (given LES-div, Lemma Λ, LR-pot)
**Level 0.**
- I re-derived (Π_Ex)_0 = Σχ_X(z + e)a_X + Σ(λ_X − λ_*)dχ_X from the discrete product rule, Σχ = 1 and Σdχ = 0.
- Common corner: two points at ∞-distance ≤ 1 lie in cells that share a corner. So X_* can be common, and every X used
  satisfies |c_X − c_*|_∞ ≤ 1.
- The 08:36:05 clarification handles a term whose tent vanishes at one of the two points. The comparison point on
  ∂supp χ_X has the term and its first differences equal to 0, because σ_5' = σ_5'' = 0 at 1. It is correct, and **this is
  exactly where C^{2,α} tents are needed.** With C^{1,1} tents, ∇(dχ) jumps at ∂supp and the Hölder term costs L^{αk}.
- a_X via EP-int (b) with μ = the tent-axial gauge: legitimate, since (b) holds for any μ. It turns a gauge-variant sup into
  LR-pot's gauge-invariant bound.
- λ_X(c_*) = Σ_π(a_X − x_0) along ≤ 4 root-to-root segments. The x_0 line sums are lane A's root-to-root holonomies,
  bounded by Lemma Λ. EP-F3 does not occur: correct.

**Levels j ≥ 1.**
- Telescoping x_{i+1} = Qx_i − r_i (lane A's convention r = Qx − x_{+}) plus Q-hold: correct.
- **N_res is genuinely a sum.** The telescoped residuals add without decay in the level-j norm. Corollary EP-lin's remark on
  sum versus max is accurate.
- The B5' counterexample is consistent with EP-rec: N_res ∼ L^{(2+α)(k-j)}a matches its lower bound.

**Weights (RS5-4 (a)).** c_r = 24 assumes LR-pot and Lemma Λ are local with reach 12 and 8 per output point. That is
plausible from their constructions (tent-axial paths inside one coarse cell, root-to-root contours), but I did not see it
proven in the cited lane-A text. Mark the weighted form "with LR-pot's and Lemma Λ's reach ARGUED".

## B.7 Corollary EP-lin (l.2060; proof l.2240-2245): CONFIRMED as an implication
- (H-inv+) is gauge invariant, because ||·||_inv and N_res are 𝒢_0-invariant. So "any representative" is harmless.
- Converse: correct with (C_Q + 1).
- Net effect: (W-lin-Π) for S_E ⟺ (H-inv+), up to the sum-versus-max gap. This moves (H-lin^∇)'s gauge-variant half
  entirely into gauge-invariant terms. **EP-F4 = (Res-Hölder) is the remaining content.** That is not progress on the wall
  itself, and §16.6's "Reading" says so honestly.

## B.8 Corollary EP-LRL(b) (l.2063; proof l.2247-2253): CONFIRMED-WITH-FIX (RS5-3)
- REVIEW_BFT_A_S4 Part 6's needs:
  - item 1 (slice): EP-alg;
  - item 2 (interior C^{1,α}): EP-int + EP-rec, by a different and better route. It telescopes through Q-hold instead of
    per-level box estimates, so no box Gaffney is needed at any level;
  - item 3 (patching): 16.6 plus Lemma Λ;
  - item 5 (weights): Prop W plus weighted EP-rec.
  - These four are discharged. Item 4 is (Res-Hölder)_m plus Q-hold. **Confirmed: LRL (b) ⇐ (Res-Hölder)_m.**
- Fixes (binding):
  - (a) LRL (b) is quantified over T ≥ 3 (BFT_A l.1348). S_E needs T ≥ 5. State EP-LRL(b) for T ≥ 5. The cases T = 3, 4 are
    not finite-dimensional uniformly in k, so they need a separate argument (or LRL (b) restated for T ≥ 5).
  - (b) Define N_res,m: weights e^{mf} inside the sup, gradient and Hölder terms of each ||r^c_i||_{C^{1,α}}, with the same
    f as in ||·||_{D,m}.
  - (c) The pre-registered weighted reach of LR-pot and Lemma Λ is ARGUED (B.6).
- No ||x||_{inv,m} of the response appears on the right: Prop W converts it to ||B_k||_{D,m}. This complies with LRL (b)'s
  "no ||x||_{inv,m} on the right".

## B.9 Theorem RW^∇_k-Π(E) (l.2065; proof l.2255-2264): CONFIRMED as an implication
- §13.2 uses (W-Π) only at the four places listed. EP-alg and EP-bd supply each. Local-torus embeddings are
  coarse-lattice translations (RS4-6), which carry roots, Neumann boxes and tents to themselves.
- Arithmetic: R ≥ 2·4 + 8 = 16; T^Π_W = 4R + 14 + 8 = 4R + 22; 3R + 22 for T a multiple of M_c. Correct.
- Weighted gain: e^{−m(R/2 − 7)} is derived and e^{−m(R/2 − 9)} is claimed (conservative). Correct.
- **Verdict on what the hard-slice RW^∇_k rests on now:**
  - (W-Π): PROVEN (S_E).
  - (W-lin-Π): ⟺ (H-inv+) [OPEN: (CO-0), (CO-up), (Res-Hölder)].
  - (W-comm): GAP 1 plain rows.
  - (W-loc) (i), (ii), (iv): as before.
  - The §17 paragraph (l.2398-2402) states this accurately.

## B.10 Proposition RATE-m (l.2069; proof l.2266-2274): CONFIRMED as an implication (cosmetic RS5-6)
- s̄(R)ε^Π_W = ¼ by construction.
- log(1/K) = log(s̄ − 1) − 41 log 2 ≥ m(R/2 − 9) + log(R/(2^{44}C_W')), using s̄ − 1 ≥ s̄/2. The text has 2^{43}: a factor 2
  inside the log, harmless.
- κ_L → m/4 as R → ∞, so κ_L ≥ m/8 for R ≥ R_0(m, C_W'). Correct.
- The price is stated honestly: s̄(R) is exponentially large, so ε_mix(s̄(R)) is tiny but fixed before ε.
- Check that ε_mix is k-uniform in Theorem BB-mix_k (the subscript k in "ε_mix,k" suggests a per-k threshold). If it is
  k-uniform, write ε_mix. If not, the "k-uniform rate" claim needs it.
- RW∇-F5 reading: the top residual is the coarse mass, as in my S4 Part F. Consistent.

---

# PART C: (CovLift) (§15.2; §16.11-§16.15)

## C.1 Lemma CL-uniq (l.2074; proof l.2276-2288): CONFIRMED. **GI-F2 cannot occur: CONFIRMED.** (Reviewed first, as asked.)
- **The lemma.**
  - Z^G = Z at level 0 means G(y) = Z_0(b)^{-1}G(x)Z_0(b) on every link b = (x, y). With G(x_0) = 1, induction along paths
    gives G ≡ 1 on the connected region.
  - This is the elementary fact that a connection's stabiliser is the centraliser of its holonomy, embedded by evaluation
    at one point. Fixing that value to 1 kills it.
  - It holds for every background, flat or reducible included, and verbatim for complexified gauges in GL(N, ℂ).
  - Only level 0 is used. Every level-k site is a level-0 site, so "G = 1 at the level-k sites" suffices.
- **The cocycle.**
  - Both ĥ(h_1, V)ĥ(h_2, V^{h_1}) and ĥ(h_1h_2, V) map Z^sm(V) to Z^sm(V^{h_1h_2}) and restrict to h_1h_2 at level k. So
    they are equal.
  - ĥ(c, V) = c follows from constant covariance.
  - I re-did this with explicit right-action conventions (as in my S4 C.4); the orders match.
- **GI-F2.**
  - In §13.6 Step 2 both ĥ·ĝ_□(V^h) and ĝ_□(V)c map Z^sm(V) to Z^sm(V^{g_□(V)c}) on the frame region.
  - Both restrict at level k to h·g_□(V^h) = g_□(V)c (Lemma GI-frame (a)).
  - So their quotient stabilises Z^sm(V) **and is trivial at level-k sites**, hence trivial.
  - **My S4 C.4 sentence ("near reducible or flat backgrounds it is a genuine requirement") was wrong.** I conflated the
    full stabiliser of Z^sm(V) (constants at flat backgrounds) with the stabiliser at fixed level-k values, which is always
    trivial. Retracted.
- **Conditions (state them in the lemma, cosmetic RS5-8).**
  - Orbit covariance must be exact at level 0 on the region where the identity is used (the r_Z-interior of Ω_□).
  - That region must be connected via level-0 links and contain a level-k site.
  - Both hold for box regions.
- **Consequence for (CovLift):** (i) reduces to exact orbit covariance (with some level-0 chain gauge restricting to h)
  plus constant covariance.

## C.2 Lemma CL-blk (l.2078; proof l.2290-2303): CONFIRMED; the correction of REVIEW_BFT_B_S4 (R1) is CONFIRMED
- (iv) applies "in some level-k gauge" (l.1640-1641). So V = 1^h = e^b in the identity gauge must satisfy
  ||log Z^sm(1^h)||_X ≤ C_sm||b||_∞.
- By (i) and CL-uniq, Z^sm(1^h) = 1^{ĥ(h,1)}. A block-constant ĥ concentrates b on face-crossing links:
  - coarse level-j value L^{k-j}b;
  - gradient L^{2(k-j)}b.
- **Sharpening (RS5-7):** the sup term already gives ≥ L^{k-j}||b||. So (iv) fails once L^{k-j} > C_sm, not just
  L^{2(k-j)} > C_sm. The conclusion (no k-uniform C_sm) is unchanged.
- Corner lift + gauge-commuting Φ: U^(0)(V^h) = U^(0)(V)^{Ĝ}, Ĝ block-constant. Φ commuting with all chain gauges keeps Ĝ.
  CL-uniq then identifies Ĝ as the extension. Correct.
- **So my S4 (R1) ("exact covariance and the cocycle come from the corner lift's homomorphic ĥ; Φ commutes with all
  level-j gauges") yields covariance but provably fails (iv).** Retracted.
  - The refinement must move pure-gauge inputs: Φ(1^Ĝ) = 1^{G'} with G' a smooth interpolation.
  - Equivalently, compose with a gauge normal form (CL-Φ), or use an interpolatory S_0 with a C^{2,α} limit (CL-lin).
- bb5 B5-5 shows this exactly: identity to 9.7e-17; P1 ×9 = L² per level; P0 ×3 = L per level (the sup mechanism of RS5-7).

## C.3 Proposition CL-lin (l.2082; proof l.2305-2330): CONFIRMED given φ ∈ C^{2,α}; one overclaim (RS5-5)
- (a) Identities.
  - The derived scheme exists because s reproduces constants.
  - Telescoping over the L fine links between roots gives Q_axS_1 = 1, because interpolation makes the transverse factor
    the identity on the root row.
  - Constants: s^{[1]}c = c/L per fine link. bb5's s1_matrix does exactly this.
  - Correct.
- (b) ev^{(j)}S_0^k = S_0^{k-j} (interpolatory). The extension ĥ^lin_j = S_0^{k-j}μ is smooth exactly when φ is: this is
  the CL-blk escape. Correct.
- (d) For interpolatory schemes, S_0^mc = f(L^{-m}·) exactly. I re-did the Abel summation Σc_iφ'(t − i) = Σd_iψ(t − i)
  with ψ := Σ_{l≥1}φ'(· − l); compact support follows from Σφ'(· − l) = 0. Lattice values are exact averages of a C^{1,α}
  function, so the bound is uniform in ρ. Correct.
- (e) |r_j| ≤ 2L(L − 1)ρ_j²||f_j||. Residual term ≤ 2((L − 1)/L)||f_j||. Correct (2, not 2L²).
- **Overclaim (RS5-5, binding).** The §17 table (l.2394) says "linearised (CovLift) (i)-(v)". CL-lin does not address
  (iv)'s second clause ||g_{Z^sm(V)}||_Y ≤ C_g||b||_∞ (l.1641).
  - With lane A's Q, Z^lin has residuals ∼ 2||f_j|| at every level.
  - In 𝒴^∇ the residual-type source carries ω_l = L^{θ(k-l)}. So the C_g clause holds k-uniformly only at θ = 0, or with
    Q_ax as the functional's Q.
  - At θ = 0, ||g_{Z^lin}||_Y ≲ ||f_0||_∞ + [f_0]_α + Σκ_l·2||f_l||, which is fine.
  - Fix: restrict the table entry to "(i)-(iv) first clause, (v) trivially (linear)". Add "C_g clause: holds at θ = 0;
    θ > 0 OPEN".

## C.4 Proposition CL-Φ (l.2088; proof l.2332-2341): CONFIRMED as an implication
- d*d∘d = 0 and C∘d = d∘C_0 give linear covariance with block-constant C_0.
- With Π_E as a gauge normal form, for λ_0 not vanishing at level k: Λ(x + Dλ_0) = Λ(x) − λ_0 + I_χλ_0. So the extension
  becomes the quintic-tent interpolation of μ, smooth. Correct.
- This is a useful general principle: **Π_E ∘ (any gauge-commuting refinement) has a smooth extension.** (iv) then reduces
  by EP-rec to gauge-invariant bounds (curvature C^α, N_res).
- Measured: Φ-chain(I) F1 = 5.53, 7.27, 9.55, 12.6, 16.5, a ratio of 1.315 per level = 3^{1/4} = L^α. This is the
  signature of block-piecewise-constant curvature, identical to Q1/W.
  - The pre-stated guess failed (1.73 > 1.5), recorded and not repaired. Honest.
  - The diagnosis "the refinement must read neighbouring coarse cells" is right. Note the scope: the measured Φ is N = 18
    steps of τ = 0.1, not the converged constrained minimiser. Nothing was measured about the converged version.

## C.5 Proposition CovLift-route (l.2091; proof l.2343-2354): ARGUED, accepted; sharpened in Part E

---

# PART D: mask choice and mask regularity (decisive; reviewer computation)

Theory used (standard; Dyn-Levin / Hassan-Dodgson m-ary form):
- Arity m = 3, σ(z) := 1 + z + z².
- The 2nd-divided-difference scheme of S_a is a^{[2]} = 9a/σ², and e := a^{[2]}/σ = 9a/σ³ is its difference scheme.
- If ||S_e^n||_∞ < 1, then φ ∈ C^{2,β} with β ≥ −log_3(||S_e^n||_∞^{1/n}).
- A non-polynomial eigenvalue λ of the local subdivision matrix bounds the total smoothness from above by −log_3|λ|.
- Computed in exact rational/integer arithmetic (probes in the scratchpad; record below).

| ternary mask | range (coarse) | lower bound β (n = 10, exact) | upper bound (spurious eigenvalue) | verdict at α = ¼ |
|---|---|---|---|---|
| DD4 (Lagrange 4-pt) | 2 | none (ρ_n = 1.222 > 1) | λ = 0.1358 > 1/9 ⇒ smoothness ≤ **1.817** | **NOT C²** (CL-F2 OCCURS: PROVEN) |
| DD6 (Lagrange 6-pt) | 3 | **β ≥ 0.2677** (n = 7: 0.2454; n = 8: 0.2547) | λ = 0.0782 ⇒ ≤ 2.320 | **C^{2,¼}: PROVEN**, margin ≤ 0.07 |
| DD8 (Lagrange 8-pt) | 4 | **β ≥ 0.4732** | λ = 0.0581 ⇒ ≤ 2.590 | **C^{2,¼}: PROVEN**, comfortable |
| cubic spline (cardinal) | ∞ (decay (2 − √3)^{|x|} ≈ 0.27^{|x|}) | C^{2,1} (classical: Schoenberg's cardinal spline; refinement = resampling the same spline) | — | C^{2,1}, but exponentially local only |

**Cross-check with the literature.**
- The ternary Lagrange 4-point weights at offset ⅓ are (−5, 60, 30, −4)/81. These are the Hassan-Ivrissimtzis-Dodgson-Sabin
  4-point ternary family a_0 = −1/18 − μ/6, a_1 = 13/18 + μ/2, …, at **μ = 1/27**.
- The C² range reported for that family is **1/15 < μ < 1/9** (Hassan et al., CAGD 19 (2002) 1-18; the range is as quoted
  by Zheng et al., IJAM 36:1). 1/27 lies outside it, consistent with my eigenvalue bound.
- So DD4's failure is classical, not a numerical artefact.

**Which mask (verdict).**
- **DD8 is the right default for (CovLift):**
  - finite range (r_s = 4 coarse steps, so r_Z ≤ 4L/(L − 1) ≤ 6);
  - PROVEN C^{2,0.47}, so α = ¼ has room and lane A could raise α toward 0.4;
  - interpolatory, so ev∘S_0 = 1 is exact.
- **DD6** is admissible at α = ¼ (PROVEN, β ∈ [0.268, 0.320]). But any later increase of α above ≈ 0.26 breaks it.
- **The cubic spline** has the cleanest regularity but infinite range. It needs (CovLift) (ii) relaxed to exponential
  locality, booked as e^{−cR} errors in R_□ (my S4 Part E.2). Its nonabelian analogue would need a global (circulant) solve
  per level. Not recommended as primary.
- **Binding (RS5-10):** replace "mask regularity of DD6/DD8 as a proof: OPEN" (l.2397, log) with "PROVEN by an exact
  finite computation (REVIEW_BFT_B_S5 Part D)". Lane B should add a checks/ file reproducing it (its own exact-arithmetic
  script; the reviewer's probes are in the scratchpad, not in checks/). The bb5 DD6 pass (1.193/1.200 against 1.25) should
  be described as marginal on the proxy and settled by the exact bound.
- In d dimensions the tensor-product limit φ^{⊗d} and ψ⊗φ^{⊗(d−1)} inherit C^{1,α} for x^c when φ ∈ C^{2,α}. That is what
  CL-lin (d) uses. No extra multivariate (joint spectral radius) argument is needed for tensor pairs.

---

# PART E: (CovLift) route verdict

- **Linear level: now unconditional.**
  - CL-lin with DD8 (or DD6) holds with PROVEN mask regularity.
  - It gives an exactly linearly orbit-covariant, finite-range, translation-covariant lift with a smooth extension and
    ||Z^lin||_X ≤ C||B||_∞, k-uniformly.
  - Minus the C_g clause at θ > 0 (RS5-5).
- **The cocycle is no longer an issue** (CL-uniq). GI-F2 is gone.
- **Two viable nonabelian constructions.** Both need (N1) and (R3).
  - **(a) Covariant DD8 refinement in a local normal form.** On each block neighbourhood, gauge-fix Z_{j+1} by the
    nonabelian box-Coulomb normal form (N1), apply the DD8 pair to the logs, then transform back.
    - Covariance is exact by CL-uniq, if the normal form is unique (implicit function theorem near small fields around
      EP-int).
    - Patches must be glued; GI-F3 is the danger. Gluing gauge-fixed patches by tents is covariant only to first order.
      Unlike for the slice, gluing a *lift* needs a consistency that tents do not give, unless the normal form is global
      on the relevant region.
  - **(b) Π_E-normalised gauge-invariant curvature subdivision (CL-Φ route).**
    - The refinement acts on gauge-invariant data (curvatures and root holonomies) by the DD8 curvature map, then is
      realised in the elliptic normal form.
    - Smooth extension is automatic (CL-Φ). (iv) reduces by EP-rec to C^α curvature plus N_res, which the DD8 linear model
      supplies.
    - **I rank (b) higher.** It avoids GI-F3, and its nonlinear content is (N1) + (N2) + (R3), with (N2) now having an
      explicit linear target.
- **Not the route:**
  - corner lift + gauge-commuting smoothing (CL-blk);
  - Q1/Whitney (CL-F3: P1 ×3 per level);
  - DD4 (not C²);
  - MSG plus smoothing (S4 Part E).
- **Most robust alternative (unchanged):** Balaban's variational lift with exponential locality. It shares lane A's linear
  inputs.
- **(CovLift): OPEN.** Its open content is now purely nonabelian: (N1) the nonlinear EP-int / normal-form uniqueness;
  (N2) covariant curvature subdivision; (R3) BCH absorption in C^{1,α}; plus the C_g clause at θ > 0.

---

# Overclaims
1. l.2394 (table) "linearised (CovLift) (i)-(v)": the C_g clause of (iv) is not addressed (RS5-5).
2. l.2397 / log "mask regularity … OPEN": now PROVEN by this review's computation (RS5-10). This is an underclaim, but the
   record should be corrected.
3. l.1920-1925 (item-8 tag, written at Step 1): "tested and corrected in §16" predates bb5 and §16 (RS5-9).
4. Corollary EP-LRL(b): stated without the T ≥ 5 restriction; LRL (b) quantifies T ≥ 3 (RS5-3).
5. 16.6 weights "c_r := 24 [crude]": it rests on unproven reach statements for LR-pot and Lemma Λ (RS5-4).
6. My own S4 review: C.4's "genuine requirement near reducible or flat backgrounds" (retracted, C.1) and Part E (R1) "Φ
   commutes with all level-j gauges" (retracted, C.2).

# Tally (lane B session 5; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | provenance (byte accounting); RBB4 fixes; **Lemma EP-alg**; **Lemma EP-int** (given LES-div; no Gaffney, no boundary regularity: verified); **Lemma Q-hold**; **Theorem EP-bd** (linear, trivial chain); **Theorem EP-rec**; Corollary EP-lin; **Theorem RW^∇_k-Π(E)**; Proposition RATE-m; **Lemma CL-uniq + GI-F2 cannot occur**; **Lemma CL-blk** (+ correction of S4 (R1)); Proposition CL-Φ; bb5 reading and re-run (byte-identical) |
| CONFIRMED-WITH-FIX | Theorem EP-opt (RS5-2); Corollary EP-LRL(b) (RS5-3: T ≥ 5, N_res,m defined); EP-rec weights (RS5-4); **Proposition CL-lin** (RS5-5: C_g clause) |
| PROVEN HERE (reviewer, exact computation) | DD8 ternary φ ∈ C^{2,0.473}; DD6 ternary φ ∈ C^{2,0.267}; DD4 not C² (smoothness ≤ 1.817) |
| ARGUED (accepted) | Proposition CovLift-route; weighted reach of LR-pot / Lemma Λ |
| OPEN | **(Res-Hölder)** (= EP-F4); (CO-0), (CO-up) for (H-inv+); **(CovLift)** nonabelian: (N1), (N2), (R3), C_g at θ > 0; (Mult-Y); (Pair-loc) for (G), (P0), (Pl); background (Z-covariant) S_E |

# Required fixes (binding for the next lane-B session unless marked cosmetic)
1. **RS5-1.** GI-F2: §12.3 (l.1686), §13.6 Step 2 (l.1844-1846) and the §14 rows (l.1962, l.1967) should read "cannot
   occur for any lift orbit-covariant at level 0 (Lemma CL-uniq); the cocycle is automatic".
2. **RS5-2 (cosmetic).** l.2208: ⟨y, w⟩ → ⟨πy, w⟩.
3. **RS5-3.** Corollary EP-LRL(b): add "T ≥ 5" (LRL (b)'s T = 3, 4 need a separate argument), and define N_res,m.
4. **RS5-4.**
   - (a) Mark 16.6's weighted constant as resting on the reach of LR-pot (≤ 12) and Lemma Λ (≤ 8), ARGUED.
   - (b) The same caveat applies in EP-LRL(b).
   - (c) State in EP-bd and EP-rec that they concern the linear slice at the trivial chain. The Z-covariant version is (N1).
5. **RS5-5.** CL-lin / §17 table: "(i), (ii), (iii), (iv) first clause, (v) (linear)". Add the C_g clause: it holds at
   θ = 0 (or with Q_ax in the functional); θ > 0 OPEN.
6. **RS5-6 (cosmetic).** 16.10: 2^{43} → 2^{44}. Check that ε_mix in BB-mix_k is k-uniform, and write ε_mix if so.
7. **RS5-7 (cosmetic).** CL-blk: (iv) already fails once L^{k-j} > C_sm (sup term).
8. **RS5-8 (cosmetic).** CL-uniq: state its conditions (exact level-0 orbit covariance on a level-0-connected region
   containing a level-k site).
9. **RS5-9 (cosmetic).** Log: disclose the item-8 tag's forward reference to §16/bb5 (written at Step 1, 08:26).
10. **RS5-10.**
    - Record the mask regularity as PROVEN (Part D): DD8 β ≥ 0.473, DD6 β ≥ 0.267, DD4 not C².
    - Add a checks/ exact-arithmetic reproduction.
    - Adopt DD8 as the default mask for CL-lin and (N2).
    - Call bb5's DD6 proxy pass marginal.

# Current minimal open set for BFT-0..4 (on 𝒞_glob unless marked)
- **BFT-0/1/2:**
  - (H-lin^∇) at configuration level. By EP-opt and EP-lin this is now **gauge invariant**: (H-inv+) = ||x||_inv bounds
    [(CO-0) = (G♯_0-lev0), (CO-up), (G♯-rough) curvature half, (SB); the X_s halves (XR, XB, HX) and the data/residual
    sources (Theorem W) PROVEN] + **(Res-Hölder)** (N_res of responses; the B5' obstruction shows it cannot be dropped).
  - LRL (b) ⇐ (Res-Hölder)_m (T ≥ 5).
  - (H-rem^∇) third order ARGUED. (FP♯').
  - The slice is no longer open at the linear level (S_E). The background-covariant slice is (N1).
  - Off 𝒞_glob: (UHL), (SL-cov), Z^sm.
- **BFT-3:** k = 1 PROVEN. k ≥ 2 ⇐ (H-lin^∇)_m, m > 0, which is now ⟺ weighted (H-inv+)_m. Theorem W supplies the
  gauge-invariant data part.
- **BFT-4:**
  - k = 1 PROVEN.
  - k ≥ 2 bounded polymers on 𝒞_glob ⇐ Theorem RW^∇_k-Π(E) [(W-Π) PROVEN; (W-lin-Π) ⟺ (H-inv+)] + (W-comm) [GAP 1 plain
    rows] + (W-loc) + (f) + (E3^∇) [ARGUED] + (I-id).
  - Gauge-invariant pieces ⇐ + (CovLift) [OPEN, nonabelian only: (N1), (N2), (R3), C_g at θ > 0; linear level PROVEN with
    DD8] + (Mult-Y) [GAP-1 family] + (Pair-loc) [ARGUED] + (I-id)_Z [ARGUED].
  - The slice + Feynman mixed form (Theorem BA's hypothesis form) is still OPEN.
  - Off 𝒞_glob: GI-off (ARGUED).
- **Rate:** κ_L ≥ m/8 under weighted (H-inv+)_m + localised (W-comm) (RATE-m). Unweighted: κ_L ∼ log M_c/M_c.
- **Levers with the largest fan-out:**
  - (a) the (Pl)-free plain-row theory (GAP 1 + (Mult-Y));
  - (b) **(Res-Hölder)**: it is now the single gauge-variant-free input behind (W-lin-Π), LRL (b) and the slice route;
  - (c) the nonabelian normal-form uniqueness (N1), shared by the covariant slice and (CovLift) route (b).

---

## Re-run record (bb5) and reviewer probes
- Runner: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revBB5/run.sh`.
  - It waits with `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, then waits for load1 < 8.
  - Environment: nice 10; OMP/OPENBLAS/MKL/VECLIB threads = 1; PYTHONDONTWRITEBYTECODE=1; `/usr/bin/time -l`; python3
    without -I; no `timeout`; no trap.
- Acquisition 1 (08:56:49-08:56:53 UTC; load1 2.43; memory free 43%; `rmdir` once):
  - bb5_lift.py re-run: **byte-identical to checks/bb5.out** (the `[t = …]` line excluded); 2.75 s; RSS 517 MB.
  - Reviewer probe `revBB5/mask_reg.py`: exact Fractions, n ≤ 7, plus local subdivision-matrix eigenvalues; 0.49 s.
- Acquisition 2 (08:57:31-08:57:32; load1 2.51; memory free 46%; `rmdir` once): reviewer probe `revBB5/mask_reg2.py`, exact
  integers, n ≤ 10, for DD6 and DD8; 1.09 s; 67 MB.
- Outputs are in the scratchpad: revBB5/bb5.rerun.out, mask_reg.out, mask_reg2.out, *.time.
- Afterwards: lock directory absent; no __pycache__ in checks/; no process left. No file other than this review was
  written in the repository.

Sources consulted for Part D:
- Hassan, Ivrissimtzis, Dodgson, Sabin, "An interpolating 4-point C² ternary stationary subdivision scheme", CAGD 19 (2002):
  https://durham-repository.worktribe.com/output/1549906/an-interpolating-4-point-c2-ternary-stationary-subdivision-scheme
- The C² range 1/15 < μ < 1/9 as quoted in https://www.iaeng.org/IJAM/issues_v36/issue_1/IJAM_36_1_4.pdf
- Beccari-Casciola-Romani (μ = 1/10 is C²): https://boa.unimib.it/bitstream/10281/7672/1/BCR_ternary_cagd07.pdf
