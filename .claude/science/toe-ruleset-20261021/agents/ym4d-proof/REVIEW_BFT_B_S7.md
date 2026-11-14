# REVIEW_BFT_B_S7: hostile review of BFT lane B session 7 (BFT_B.md [RBB6-fix] edits, §21-§23; checks bb7g, bb7c, bb7n, bb7k)

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md or the checks. This file is the only one I edited. No
commits, PRs or pushes. One disclosure: REVIEW_BFT_B_S6 D.4 (the (N1-G) proof that lane B imports) was written by an earlier
reviewer instance. I re-checked it here as if it were someone else's work, and it has a gap (B.2).

Inputs (read 2026-10-28 ≈10:40-11:00 UTC). `TZ=UTC stat`: BFT_B.md born 09:21:46, modified 10:39:24, 365788 bytes;
BFT_B_LOG.md modified 10:39:42, 38915 bytes. checks/: bb7*_criteria.md born = modified 10:28:08; scripts 10:28:43-10:32:39;
outputs 10:34:18-10:35:23. BFT_A.md modified 10:26:38 (lane A session 7 finished; unreviewed; read only).
- BFT_B.md: §21-§23 and the session-7 FOR OTHER FILES (l.2854-3252), in full.
- Every [RBB6-fix] tag in context (l.1881, 1899, 1975, 2426, 2473, 2512-2519, 2631, 2651, 2665, 2683, 2710, 2716, 2745, 2773,
  2777, 2816-2846).
- §12.2 (CovLift) (l.1636-1660); §16 σ_5 (l.2024, 2146-2150); §19.7.
- BFT_B_LOG.md: session 7 (l.317-370).
- REVIEW_BFT_B_S6.md (all) and REVIEW_BFT_A_S6.md (bottom line, Part 7, binding fixes, strategic verdict).
- BFT_A.md: LRL (b) (l.1345-1350), the norm definitions (l.883), the S4' average (l.1112), and BFT_A_LOG session 7.
- HIST.md: S4' reflection L1 (l.385-402, l.1036-1044).
- checks: all four criteria files, and bb7c_resid.py, bb7n_chain.py and bb7k_off.py line by line.

Re-runs: bb7g, bb7c, bb7n and bb7k under the numeric lock, plus two reviewer probes:
- the amplitude-corrected bb7n;
- near-antipodal Karcher data, the control K10 should have used.

The record is at the end.

---

## Bottom line

- **Provenance: CONSISTENT. One provenance defect (RS7-1).**
  - §21 plus its "# Session 7" header is **11674 bytes = 324833 − 313159**, exactly the growth logged at 10:21:15. The prefix
    l.1-2853 is 319782 = 313159 + 6623, which is the Step-1 growth (331455 − 324833 = 6622) plus the usual 1-byte line
    boundary. So every Step-1 edit lies before §21, and §21 has the same byte count as when it was appended.
  - l.1-2962 is 331456 bytes, against 331455 after Step 1. So nothing before §22 changed after Step 1.
  - **Tags inside pre-stated §18 are purely additive.** §18 (l.2451-2580) is 13746 bytes. Removing its two [RBB6-fix]
    insertions (296 B at l.2473 and 945 B at l.2512-2519) leaves **exactly 12505 B**, the size §18 had when it was appended
    in session 6. The RHT rename sits only inside a tag.
  - Order: §21 (10:21:15) < Step 1 (10:23:36) < criteria (10:28:08) < scripts < runs (10:34:18-10:35:23) < §22 (10:38:24) < §23
    (10:39:24). This matches the log.
  - **RS7-1 (provenance, binding-cosmetic).** Several Step-1 tags written at 10:22-10:23 state session-7 outcomes as already
    established, about 15 minutes before §22 existed. Examples:
    - l.2473-2475: "IMPORTED-AND-REVERIFIED … re-verified line by line in §22.2; reproduced in checks/bb7g";
    - l.2710-2711: "this is PROVEN-HERE with no import";
    - l.1901 and l.1975: "§22 gives / addressed in §22 by Z^off";
    - l.2774: "proof §22 (Theorem N2)";
    - l.2666: "proof in §22".

    Unlike session 6 (RS5-10), these forward references are **not disclosed** as planned. Append "(planned at the time of this
    tag, 10:23; written 10:38)" to each. Do not rewrite them.
- **[RBB6-fix] edits: all nine applied, with the content asked for** (Part A). There is one consequential slip: RS6-3's
  constant was later "corrected" wrongly (RS7-2).
- **Remark PL: CONFIRMED.** Its pre-stated constant **e^{20m} was right, and post-proof correction (1) is a misreading.**
  - In LRL (b), m is the weight on **both** sides (BFT_A l.1347-1349: ||·||_{∞,m} on the left, ||B_k||_{D,m} := ||B_k||_{∞,m}
    on the right).
  - m' is the kernel-decay exponent (0 ≤ m < m' < m_*'). It is not an output weight.
  - The correct constant is C_b(T) ≤ e^{(4T+4)m}C_b(2T) ≤ e^{20m}C_b(2T) (RS7-2).
- **Lemma N1G: the result is CONFIRMED; the step-(2) proof is NOT valid as written (RS7-3).**
  - The "reflect the path after the first crossing" map deletes the crossing jump. In continuous time this is neither
    rate-preserving nor a bijection of path spaces.
  - The S6 D.4 text has the same gap.
  - A two-line replacement proof (maximum principle for u = q(x) − q(x + 1)) is in B.2. With it, N1G is PROVEN, C_G = ¼
    exactly.
  - bb7g re-run: byte-identical.
- **Theorem N2: CONFIRMED** (constants not evaluated, as stated).
  - Lemma S2K and Lemma N2-step are also CONFIRMED.
  - The telescoping, the frame-change bracket, the downward induction, the absorption constant ε_1 and (N2-lip) without the
    factor k − j were all re-derived (C.1-C.3).
  - It is curvature-only, so it holds on 𝒦(ε_1) with no global gauge. **N2-F1 does not occur.**
- **(C_g-θ): Lemma Γ0 CONFIRMED given L1.**
  - L1 must hold for each transverse direction separately (C.4).
  - Lane A's Q is the uniform S4' average (BFT_A l.1112), so the uniform-weight assumption holds.
- **Proposition Cg-lin: CONFIRMED** (units re-derived).
- **Proposition Cg-NL:** the first-order term is CONFIRMED as an implication; the BCH remainder is ARGUED (correctly marked).
- **C_g design decision: justified** for the residual component. The non-residual components of g_Z at θ > 0 stay OPEN.
- **Theorem KΠ-off (the headline): CONFIRMED-WITH-FIX for (CovLift) (i)-(iii) on 𝒦(ε), every level-k gauge, including
  holonomies, torons and Q ≠ 0** (Part D). The cut-off is doing exactly the right thing: no logarithm is evaluated outside
  d < r_2 < r_inj. Covariance holds for all gauges, by NF-cov and bi-equivariance of m_w alone. Three fixes are needed:
  - **RS7-4.** For N ≥ 3 the eigenvalue-principal logarithm is not the geodesic logarithm on the whole injectivity ball. It
    can leave su(N), for example at angles (1.1π, −0.55π, −0.55π), which lie inside the ball of radius √2π. Require
    r_2 < π (HS-angle normalisation), or define "log" as the inverse of exp on the ball.
  - **RS7-5.** The reduction "(iv), (v) = the 𝒞_glob walls" is literal only if (N1-int) and (N2-bd) are stated **locally**
    (on Ω^{(−r)}, given V^h = e^b on Ω). As written in §19.16 they are global 𝒞_glob statements.
  - **RS7-6.** Scope. Z^off needs boxes Ñ_X that embed: coarse side ≥ 5, as in bb7k. "Every torus" in (CovLift) is to be read
    as T ≥ 5 (consumers use T ≥ 86). Also, the fixed axis order breaks hypercubic covariance, and so does R^{ax} itself.
    (CovLift) does not ask for it, but the marginal-coupling extraction must symmetrise (note, D.6).
- **Lemma CUT: CONFIRMED.** Face consistency and root values were checked against σ_5(0) = 1, so w = p(t).
- **Lemma CL-clu: CONFIRMED** (constants not evaluated). It correctly repairs a gap that REVIEW_BFT_B_S6 C.6 missed: chain(V)
  is not small in coarse units in any level-0 gauge, because face links carry coarse links. State the needed smallness
  C_clε ≤ r_1/2 explicitly in the hypotheses of Theorem KΠ-off (RS7-7).
- **Proposition TOP: CONFIRMED**, and the distinction it draws is correct.
  - (a) is the classical fact: a continuous path-selection on X × X forces X to be contractible.
  - (b)-(c) are right.
  - The deeper reason (D.5): on a lattice, *existence* of a continuous covariant section is always cheap (a maximal-tree
    gauge already is one). The Gribov/Singer obstruction is a continuum phenomenon. So KΠ-off's real content is "covariant
    everywhere **and** the 𝔪^geo construction in every frame". That is proven.
  - (d) (Lüscher) is cited, not opened. The topological sector is carried entirely by chain(V); Π^off is a gauge transform
    and changes no holonomy.
- **Remark HOL: ARGUED, plausible.**
- **bb7k K10 (the control): FAILED for the reason lane B gives.** My near-antipodal probe makes the predicted failure occur
  (E.2): non-unique Karcher limits on exactly antipodal pairs, and an O(1) jump of the Karcher mean across the cut locus. The
  cut-off m_w stays continuous there.
- **bb7n at the amplitudes its criteria named: ALL PASS** (E.3). The f_k = 0.26 / 0.52 deviation has no adverse consequence.
  It tested a less-small regime than promised; the corrected amplitudes agree with the linear chain even better.
- **Re-runs:** bb7g and bb7n are byte-identical. bb7c and bb7k differ only in their timing lines, and K10 still FAILs.

---

# PART A: the [RBB6-fix] edits (Step 1)

All of REVIEW_BFT_B_S6's binding and cosmetic fixes were applied in place, with the content asked for.

**RS6-1** (l.2512-2519, l.2631, l.2817, l.2846): applied. It has the co-closed scope, names V_l OPEN, and states the candidate
route.

**RS6-2:** the commutator rows are named at l.2514.

**RS6-3** (l.2665, l.2820): applied. The tag's constant e^{20m} is the correct one. The later "post-proof correction (1)" to
e^{16m+4m'} (l.2965-2966, 2986, table l.3217) should be reverted (RS7-2).

**RS6-4** (a)-(d):
- l.2777 and l.2829: small gauges.
- l.2745 and l.2830: CL-F4 OCCURS off 𝒞_glob.
- l.1881: the saturation-by-invariance sentence.
- l.1899 and l.1975: (KΠ-off) named.
- All correct. l.1899-1901 and l.1975 carry undisclosed forward references to §22 (RS7-1).

**RS6-5** (l.2773-2774): points to §21.0's (N2-0)_j, which has the asked-for quantifiers and per-level clauses.

**RS6-6** (l.2473, 2710, 2824-2825, 2838, 2846): applied, with the forward-reference caveat RS7-1.

**RS6-8:**
- RHT and RHT_m appear only inside tags. The pre-stated §18 keeps "Theorem RH", which is acceptable.
- t, C_ℓ, Φ_0 and C_bch were checked.

**RS6-9:**
- The 19.4 correction is marked (l.2631).
- l.2426's clause is struck.
- 19.12's "… more precisely" is annotated in §19 (l.2716). §18 is untouched (verified by bytes).
- 𝒟(ε) is stated (l.2825).
- The bb6_criteria.md time is fixed (the log names it; not re-checked byte-wise).

---

# PART B: Step-1 results (Remark PL, Lemma N1G)

## B.1 Remark PL (§21.1 l.2891; proof 22.1 l.2974-2987): CONFIRMED; constant e^{20m} (RS7-2)

**(a)-(b) are correct.**
- Periodisation commutes with every translation-invariant local operator given by one formula.
- Π_E^{(2T)} commutes with translation by Te_μ (EP-alg), so the image of a T-periodic configuration is T-periodic.
- P_♯ ∘ P_♯ = P_♯ follows from lift ∘ descend = 1 on periodic configurations and Π_E² = Π_E.
- P_♯x − x is the descent of the periodic composite gauge direction.
- The lifted minimiser is the 2T-minimiser: by uniqueness of the gauge-invariant outputs, as accepted in S6 B.7.

**(c) Weights.**
- Input: a coordinate distance on 𝕋_{2T} exceeds the 𝕋_T one by at most T, so the ℓ¹ excess is ≤ 4T ≤ 16 and the input
  costs e^{4Tm} ≤ e^{16m}. Correct.
- Output: the minimal representative has d_{2T}(z̃, X̃_0) = d_T(z, X_0). This holds because each coordinate offset is
  ≤ T/2 < T. The difference and Campanato terms read points within ℓ¹ distance 4, which costs e^{4·(weight)}.
- **The output weight in LRL (b) is m, not m'** (BFT_A l.1348-1349; ||B_k||_{D,m} := ||B_k||_{∞,m}, l.883). So the bound is
  C_b(T) ≤ e^{(4T+4)m}C_b(2T) ≤ e^{20m}C_b(2T), which is exactly the pre-stated value.
- Correction (1)'s "input weight m, output weight m'" misidentifies m'. The kernel exponent m' only enters C_b(2T). Its
  bound e^{16m+4m'} is still a true upper bound, since m < m', but it is wrongly motivated and weaker. Revert it.

**Extension (reviewer, routine).** The same lift with T' := qT ≥ 5 (q = 5 for T = 1, q = 3 for T = 2) gives LRL (b) for
T = 1, 2 as well:
- the per-coordinate excess is ≤ qT/2, so the cost is e^{2qTm + 4m};
- this answers REVIEW_BFT_A_S6's "T = 1-4 for the configuration half" (Part 7 (ii));
- it may also serve lane A's P6-4 no-wrap issue (push the construction forward from a lifted cover).

Mark the extension ARGUED-routine.

## B.2 Lemma N1G (§21.1 l.2894; 22.2 l.2989-3003): result CONFIRMED; step (2) INVALID as written (RS7-3)

**Steps (1), (3), (4) and (5) re-checked.** At M/2:
- −Δg = 2g(M/2) − 2g(M/2 − 1);
- this equals 2[−M/8 + (M/2 − 1)/2 − (M/2 − 1)²/(2M)] = −1/M.

So g(0) − g(M/2) = M/8 and Σ|∇_1G_M| = M/4. For M odd it is (M² − 1)/(4M). bb7g agrees to 3.6e-14.

**Step (2), the reflection lemma.** The text: "reflecting the path after that time is an injective, rate-preserving map onto
paths from 0 to x".
- At the first entry time τ into x + 1's arc, the path jumps across a mirror bond, x → x + 1 (or x + M/2 + 1 → x + M/2).
- The reflection r swaps the two endpoints of each mirror bond. So r(ω(τ)) = ω(τ−), and the reflected path has **no jump
  at τ**.
- The image path has one jump fewer. The continuous-time path density (e^{-2t}dt_1…dt_n per n-jump path) is not
  preserved, and the map is not onto a path space of the same dimension.
- The same gap is in REVIEW_BFT_B_S6 D.4 (2).

**Replacement proof (reviewer, PROVEN here).**
- Let u_t(x) := q_t(x) − q_t(x + 1) for x = 0, …, M/2 − 1 (M even).
- The differences satisfy the same heat equation du/dt = u(x − 1) + u(x + 1) − 2u(x). Symmetry of q_t gives the boundary
  values:
  - u(−1) = q(1) − q(0) = −u(0);
  - u(M/2) = q(M/2) − q(M/2 + 1) = q(M/2) − q(M/2 − 1) = −u(M/2 − 1).
- So u' = Au, where A is the discrete Laplacian with antisymmetric ghost cells. A has non-negative off-diagonal entries (it
  is Metzler), so e^{tA} is entrywise ≥ 0.
- Since u_0 = δ_{x,0} ≥ 0, u_t ≥ 0 for all t. That is, q_t is non-increasing on [0, M/2]. For M odd use x ≤ (M − 3)/2, with
  ghost u((M − 1)/2) = 0.
- Insert this in place of the path reflection in 22.2 (2) and in the §18.0 tag's description. bb7g G3 and G4 confirm it
  numerically (1.5e-15, 4.5e-17).

**Status.** With the replacement, N1G is PROVEN-HERE (the first-crossing argument is not needed).

---

# PART C: Theorem N2 and the C_g clause

## C.1 Lemma S2K (22.3): CONFIRMED
- DD8 is interpolatory. So level-t values of s^tc are exact samples of the limit function Σc_iφ(· − i), and the derived
  scheme is integrated by ψ = Σ_{i≥1}φ'(· − i).
- Hence S_2^{(t)} is the t-fold composition, and its entries are products of averaged ψ and point values of φ.
- The ℓ¹ sup is bounded uniformly in t; averaging over an interval does not increase it.
- The Lipschitz constant Λ_2' needs ψ' = Σφ''. This is available since φ ∈ C^{2,β}: β ≥ 0.473, PROVEN by exact computation
  (S5 Part D, bb6m).
- The composition identity W^{(t+1)}(q, P) = Σ_pW^{(t)}(q, p)w_{pP}, used in 22.5, holds because the scheme is stationary.

## C.2 Lemma N2-step (22.4): CONFIRMED
**(0) Stencil.**
- An axial link value is a ladder holonomy, and its lasso bound is 1.011·D_ax·own plaquette size.
- bb7n's stencil has D_ax = 5 (offsets q_1 ∈ [−4, 5]; the axis-0-then-axis-1 tree encloses |q_1| plaquettes).
- The measured ratio 4.90 < 5.06 approaches the bound from below, as it must.

**(1) The X'-interior values against R(A^X).**
- In X's frame, the neighbour's frame field is (A^X)^H with own|log H| = O(D_axρ²f).
- (A^X)^H = A^X + dη + O(own|η|·own|A^X|), where η is the axial potential to X'.
- S_1(A^X + dη) = S_1A^X + dS_0ψ^X_{X'} = R(A^X) on X''s sites, since μ(A^X) = S_0ψ^X_{X'} there.
- So the level-j field near X is exp(R(A^X)) up to own O(ρ_{j+1}⁴f²). Correct; this was the "check first" item.

**(2) Curvature.**
- dRA^X = dS_1A^X = S_2dA^X.
- E_1 (the BCH of four links of own size σ) and E_2 (the log of the frame holonomy minus dA^X) are both O(ρ_{j+1}⁴f²) own.
- Dividing by ρ_j² = ρ_{j+1}²/L² gives |e_j| ≤ C_eρ_{j+1}²f², with C_e ∝ L². Correct.

## C.3 Theorem N2 (22.5): CONFIRMED
**Telescope.**
- Φ_{j_0} = F_{j_0}(q) because W^{(0)} = 1 and τ(q, q) = 1.
- |Φ_k| ≤ Λ_2f_k because Ad is an isometry.
- The increment has two parts:
  - the error part ≤ Λ_2C_eρ_{j+1}²f_{j+1}²;
  - the frame-change bracket ≤ Λ_2Λ_2^{(1)}·2|log hol(loop)|·f_{j+1}.
- The loop x_j(q) → p → X → P → x_{j+1}(q) → x_j(q) has coarse diameter ≤ C_rρ_{j+1}. Its level-(j+1) segments are replaced
  by root rows, with own error O(σ²) because the linear row sum vanishes (Q_axR = 1). It is spanned by C_A(L, d, r_s) level-j
  plaquettes, so |log hol| ≤ c_hρ_{j+1}²max(f_j, f_{j+1}).
- Every increment is therefore quadratic in f, times ρ_{j+1}². Σ_{j≥j_0}ρ_{j+1}² ≤ L²/(L² − 1).

**Induction.**
- The a priori one-step bound f_{j_0} ≤ 3Λ_2^{(1)}Λ_2f_k (using Λ_2^{(1)} ≥ 1) controls the j = j_0 bracket term.
- The absorption condition is f_k ≤ [(L²/(L² − 1))(4C_eΛ_2² + 12c_h(Λ_2^{(1)})²Λ_2²)]^{-1}. I re-derived it, and it equals the
  displayed ε_1 (l.3051).
- Only f_k enters, so the result is k-, T- and j-uniform and gauge-free.
- (b) and (c) are correct. For (c), (d − 1)·4n plaquettes of own size f_0/n² give n|A| ≤ 12.2f_0 in d = 4. This is
  conservative: the box half-width is 2n.

**(N2-lip) without the factor k − j: correct.**
- The level-j' error terms contribute ≤ min(2Λ_2, 2Λ_2'ρ_{j+1}/ρ_{j'})C_eρ_{j'+1}²f².
- Using the second branch, the sum over j' ≥ j is ≤ 2Λ_2'Lρ_{j+1}Σρ_{j'+1} ≤ Cρ_{j+1}. It is dominated by the top levels,
  where ρ ≈ 1, and needs no factor k − j.
- The top term is Λ_2'·2ρ_{j+1}f_k plus the parallel-path loop holonomy (area O(ρ_{j+1}) × C_Nf_k).
- So the pre-stated (k − j) was over-cautious, and correction (2) is right.

**Off 𝒞_glob.** The proof never uses a global gauge or a small coarse link. It holds on 𝒦(ε_1), including nontrivial
holonomy and Q ≠ 0. **N2-F1 does not occur: CONFIRMED.**

**Corollary N2-cons (22.6): CONFIRMED.**

## C.4 Lemma Γ0 (22.7): CONFIRMED given L1, read per transverse direction
- Q − Q_ax kills exact forms (root covariance). Contour minus straight leg bounds a ribbon in c's endpoint blocks, so
  Q − Q_ax = Γ∘d with Γ local.
- For constant H, Γ(H) = avg_{σ,y}Σ_{κ<λ}H_{κλ}A_{κλ}.
  - Every plane κλ contains some ν ≠ μ: either κ or λ if both differ from μ, or ν if the plane is μν.
  - The reflection in x_ν about c's ν-coordinate fixes c and the straight leg, maps the S4' family to itself, and reverses
    the orientation of every plane containing ν. So A_{κλ} averages to 0.
- What is used is L1 **for each transverse direction ν ≠ μ separately**. HIST l.1036-1044 spells it out for x_2 with c along
  e_1. The family's construction (all orders σ, offsets y symmetric in each transverse coordinate) makes the general case
  the same argument.
- Lane A's linearised Q is the **uniform** average avg_{σ,y} (BFT_A l.1112, Lemma BA-4's avg_y d_νd_ν' = 0), so 22.7's
  uniform-weight assumption holds. Cosmetic: cite BFT_A l.1112, and answer §23's question to lane A here.
- bb7c's Q_sym (y ∈ {−1, 0, 1}, d = 2) is a model of the mechanism, not lane A's S4' family. Its C1 = 0.0 tests Γ0's
  mechanism only.

## C.5 Proposition Cg-lin (22.8): CONFIRMED
- Residuals of the R-chain and the S_1-chain agree: R − S_1 = dμ with ev μ = 0, and Q is root-covariant.
- Π_E does not change residuals.
- Q_axS_1 = 1, so r_l = (Q − Q_ax)Z_l = Γ(dZ_l) = Γ(S_2^{(k−l)}db).
- Units: own |r_l| ≤ 2L(L − 1)·ρ_l²·osc_coarse(H) and osc ≤ 2Λ_2'ρ_{l+1}·4||b||, giving
  ρ_{l+1}^{-2}|r_l|_own ≤ 16Λ_2'ρ_{l+1}||b||.
- Weighting by κL^{θ(k−l)} = κL^θρ_{l+1}^{-θ} gives 16κ_+L^θΛ_2'ρ_{l+1}^{1−θ}||b||, bounded for θ ≤ 1. Correct.
- bb7c's profiles show the predicted rates: θ = 0 decays ≈ ×L^{-1}; θ = ½ decays; θ = 1 is bounded with halving increments.
  The asymmetric control grows ×L^{θ}.
- Note: C3's threshold (max ≤ 2·top, measured 1.948) is tight. The θ = 1 profile converges to ≈ 4.3 against 4.32, so a
  depth-6 run could fail C3 without contradicting the theorem. Informational.

## C.6 Proposition Cg-NL (22.9): first-order term CONFIRMED as an implication; BCH remainder ARGUED
- The residuals are composite-gauge covariant, so the statement concerns the R^{ax} chain only. Z^{KΠ} and Z^off give the
  same residuals, which is correct and worth stating.
- The first-order term uses (N2-lip) localised to Ω. The telescope reads V only on Ω^{(+r)}, and that is correct given
  finite DD8 support.
- The remainder O(ρ^{2−θ}ε²) is ARGUED, honestly marked. It needs lane A's nonlinear W_0∘M̄.
- The design decision (C_g) is justified for the residual component. The non-residual components of g_Z at θ > 0 remain as
  in RS5-5 (OPEN).

---

# PART D: Theorem KΠ-off (the headline)

## D.1 Is the gluing well defined? Yes; the cut-off does exactly this (with RS7-4)
**m_w is defined, and indeed C^∞, on all of SU(N)²:**
- on {d < r_inj}, ψ∘d is smooth: ψ = 1 near 0, where d is not smooth, and d is smooth on 0 < d < r_inj;
- the logarithm is analytic there;
- on {d > r_2}, m_w = a;
- the two open sets cover SU(N)², and the formulas agree on the overlap.

**The iteration.** Each step is applied to the *intermediate* pair, so no logarithm is ever evaluated at d ≥ r_2.

**RS7-4 (binding).** §21.0 says "principal log analytic on d(1, c) < r_inj".
- For SU(2) (bb7k's normalisation, d(1, −1) = π = r_inj) this is fine.
- For N ≥ 3 the eigenvalue-principal log can leave su(N) inside the injectivity ball. In HS-angle normalisation
  (|X|² = Σθ_i², r_inj = √2π), the angles (1.1π, −0.55π, −0.55π) have |X|² = 1.815π² < 2π², but the principal branch maps
  1.1π to −0.9π, and then the trace is −2πi ≠ 0.
- Fix either way:
  - define log := (exp|_{B(0, r_inj)})^{-1} into su(N), which is analytic on the injectivity ball; or
  - require r_2 < π, since |θ_i| ≤ |X| < π makes the principal log traceless and equal to the geodesic log.
- The conjugation-equivariance used in Lemma CUT holds for either definition.

## D.2 Covariance under ALL gauges: CONFIRMED (no smallness anywhere)
**The two equivariances used.**
- Right: m_w(ag, bg) = m_w(a, b)g. Here d is right-invariant and log(g^{-1}xg) = g^{-1}log(x)g.
- Left by a common constant: m_w(ca, cb) = c·m_w(a, b).

**(b) root-value formula.**
- NF-cov gives g_X(U^k) = k(c_X)g_X(U)k^{-1} with no smallness, so corner points transform as p_X ↦ k(c_X)p_Xk(z)^{-1}.
- The right factor is common to all corners at z. So G^off(U^k) = 𝔤[{k(c_X)g_X(U)}]k^{-1}, and with (U^a)^b = U^{ba},
  Π^off(U^k) = Π^off(U)^{ĥ}, where ĥ = 𝔤[{k(c_X)g_X}]𝔤[{g_X}]^{-1}.
- The left factors k(c_X) differ between corners, which is why ĥ is a ratio and not k itself. It depends on k only through
  root values.
- ĥ(c_Y) = k(c_Y) because σ_5(0) = 1 ⇒ w = p(0) = 0 ⇒ the lower corner is selected at c_Y, and g_Y(U)(c_Y) = 1. Constant k
  gives ĥ = c.

**(c) idempotence.** Re-derived: G^off(U^G) = 𝔤[{G(c_X)g_X}]G^{-1} = 𝔤[{g_X}]G^{-1} = 1, using G(c_X) = 1.

**Chain covariance for every h (AX-cov + Theorem N2 (b)).**
- The axial-frame logs are defined by a gauge-invariant condition (ladder holonomies). So chain(V^h) = chain(V)^K with K
  block-constant at every level, for every h.
- This is the step where Theorem N2 makes "all gauges" legitimate.

**(CovLift) (i) cocycle (cosmetic, RS7-8).**
- With ĥ explicit, I get ĥ(h_2h_1, V) = ĥ(h_2, V^{h_1})ĥ(h_1, V). This is the form that matches the (U^a)^b = U^{ba}
  convention.
- §12.2 writes ĥ(h_1h_2, V) = ĥ(h_1, V)ĥ(h_2, V^{h_1}), which is the other convention.
- CL-uniq makes the cocycle automatic in either convention. Fix the convention once in §12.2.

**(ii), (iii).** ĥ(z) and Z^off(V)(z) read V within the chain's range (geometric in the DD8 support, k-uniform) plus the
cell's corner boxes. Coarse translations act covariantly. CONFIRMED.

## D.3 Continuity: CONFIRMED where it is needed
- The normal forms are continuous, indeed real-analytic, in U on chain(𝒦(ε)): IFT locally, and NF-uniq for global
  well-definedness. m_w is C^∞, so G^off is continuous (C^∞) in U.
- G^off is real-analytic where all corner data are r_1/2-clustered.
- Discontinuities exist only in the discrete cell variable on spread data. They are lattice jumps between neighbouring
  sites, which no clause of (CovLift) constrains.
- bb7k K7 (output step ≤ 8.2× root step along a path from 0% to 100% spread) agrees.
- Note: m_w's Lipschitz constant in the data involves ψ' ~ 1/(r_2 − r_1) and compounds over d iterated steps. It is bounded
  but not small in d = 4. Nothing uses it.

## D.4 Lemma CL-clu (22.12) and the repair of S6's KΠ domain argument: CONFIRMED (RS7-7)
**What lane B caught.**
- 19.13 (and my S6 C.6, which accepted it) argued from "U = e^A small in one level-0 gauge".
- For U = chain(V) with V ∈ 𝒞_glob(ε), the face links carry the coarse links V(X, X'), of own size O(ε). In level-0 coarse
  units (×n) that is not small, so the hypothesis of 19.13 never held literally.

**The proof.**
- On Ñ_X, U = (e^{A_X})^{k_X} with the complete axial gauge k_X.
- p_Xp_Y^{-1} is a product of three near-1 factors: g_X(e^{A_X}), k_X^{-1}k_Y (conjugate to τ = k_Yk_X^{-1}, which is nearly
  constant) and g_Y(e^{A_Y})^{-1}. The distance is conjugation invariant.
- The constant value of τ is the level-0 axial transport c_X → c_Y. That is the product of root rows, and it equals the
  coarse link(s) up to Σ_jO(σ_j²) = O(ε²): the linear row sum vanishes because the positive-neighbour link is 1 in X's axial
  gauge.
- So d(p_X, p_Y) ≤ C_clε in a frame. Correct.

**RS7-7.**
- Theorem KΠ-off (iv)'s reduction needs C_clε ≤ r_1/2 and r_1/2 ≤ the convexity radius. State both in the hypothesis
  defining ε. C_cl contains the factor 16·25·4C_N (≈ 1600Λ_2), so ε is small.
- The frame region Ω must contain the corner boxes of Ω^{(−r)}. With Lemma GI-frame, C_F(Ω) depends on Ω's side, so ε must
  be small relative to 1/C_F(Ω_□). This is consistent with BB-bond's boxes of fixed side.

## D.5 Proposition TOP: CONFIRMED; the distinction is correct, and the reason is sharper than stated
**(a)** m(c, 1, s) is a homotopy from id to the constant map, so SU(N) would be contractible. π_3(SU(N)) = ℤ, so it is not.
This is the standard fact that a continuous path-selection exists only on contractible spaces. The application to pure-gauge
fields 1^k is correct: G_0-invariance gives that Ĝ = G(1^k)k depends only on root values (I re-derived it).

**(b), (c)** are correct.

**Why the lattice evades it (reviewer).**
- Existence of a continuous G_0-equivariant section is trivial on any lattice. A maximal-tree gauge rooted at the level-k
  roots is continuous and covariant. The Gribov/Singer obstruction lives in the continuum, where no tree gauge exists.
- So the topological question is not whether a covariant section exists. It is whether **one exists that is the smooth
  𝔪^geo/normal-form construction in every frame**. Z^off is exactly that: tree-like, with jumps, on spread data, and smooth
  on clustered data. CL-clu guarantees that frames are clustered.
- That is the right content, and it is proven.

**(d)** is cited (Lüscher 1982, not opened), as stated. One addition:
- Π^off is a gauge transform, so plaquette conjugacy classes and Lüscher's charge of the lifted field equal those of
  chain(V).
- The topological sector is carried entirely by R^{ax}, which is covariant under all gauges.
- Whether Q(chain V) = Q(V) holds is not proven, and is not needed by (CovLift). Record it as an informational OPEN.

## D.6 KΠ-off verdict
**CONFIRMED-WITH-FIX (RS7-4, RS7-5, RS7-6, RS7-7).**
- Z^off gives (CovLift) (i)-(iii) on the locally-small class 𝒦(ε), for every level-k gauge. This includes nontrivial
  holonomy, torons and nonzero topological charge.
- (iv) and (v) reduce to frame representatives, where Z^off is the clustered 𝔪^geo construction.

**RS7-5 (binding).**
- "(iv) is the same open items (N1-int) and (N2-bd) as on 𝒞_glob" is literal only if those are stated locally. The form
  needed is: if V^h = e^b on Ω with ||b|| ≤ ε, then the bounds hold on Ω^{(−r)}, with constants independent of V outside Ω.
- The mechanism is local: finite range, geometric sums. So this is a restatement, not new mathematics. But §19.16 and §23's
  "(N2-bd) (moderate; Theorem N2 is its zeroth order)" must carry the local form.

**RS7-6 (scope, binding-cosmetic).**
- (a) Z^off needs the boxes Ñ_X (coarse side 4 + 1/n) to embed, so coarse side T ≥ 5. "Every torus" in (CovLift) is to be
  read as every torus with T ≥ 5. Every consumer uses T ≥ 86.
- (b) Note, not a defect of (CovLift). The fixed axis order in 𝔪^geo and in R^{ax} breaks hypercubic covariance. (CovLift)
  only asks for translations.
  - The exact RG integral does not depend on the background, so the effective density keeps the lattice symmetry.
  - But the split of the polymer activities into a local part and a remainder is not automatically symmetric. A
    symmetrisation over the hypercubic group must be part of the marginal-coupling extraction ((I-id)), or anisotropic
    dimension-4 terms Σc_{μν}tr F_{μν}² must be shown not to be generated.
  - Add a sentence; it is not a new wall.

**How much it bought.**
- Off 𝒞_glob, the wall (KΠ-off) as I named it in S6 is closed for (i)-(iii).
- Its depth is modest. CL-F4 was an artefact of choosing the Karcher mean (no continuous extension past the cut locus), not
  of the problem.
- GI-off still needs (Mult-Y), (SL-cov) and (I-id) off 𝒞_glob, as §23 says.

---

# PART E: checks

## E.1 bb7k: K1-K8 CONFIRMED; K10 fails, as disclosed
Line by line:
- quaternion algebra, qlog (principal, angle ∈ [0, π]), the Neumann normal-form descent (from bb6n);
- the NF-cov transports used in K4, K6 and K7;
- σ_5, w = 1 − σ_5(t);
- ψ, a C^∞ step on [1, 2] with r_2 = 2 < π;
- m_w with explicit w = 0, 1 branches;
- the iterated gluing, axis 0 then axis 1.

All are correct.

**Scope.**
- d = 2, coarse side 5, n = 3.
- K3 and K5 use descents from perturbed starts, so they test G_0-invariance and idempotence up to descent precision (7e-11).
- K6's ĥ check is exact by construction, given NF-cov transport. It tests the algebra, not NF-cov itself, which was tested
  in bb6n.
- **K10 FAILS for the reason lane B gives.** The Haar spreads (≤ 2.76 < π) never reach the antipodal regime. On S³ = SU(2),
  for weights dominated by one corner, the weighted Karcher functional has a unique attracting minimiser below the cut
  locus, so start-independence there is expected.
- The control was mis-designed, and lane B disclosed the failure rather than retuning. That is the right handling.

## E.2 Reviewer probe: near-antipodal Karcher data (the K10 that should have been run)
The probe (revBB7/antipodal_probe.py) uses bb7k's conventions: quaternions, d(1, −1) = π, r_1 = 1, r_2 = 2, σ_5 weights, and
bb7k's Karcher iteration.

- **P1: exactly antipodal pair (1, −1), weights (0.7, 0.3).** I ran 6 random starts. All converge, all to d(limit, 1) = 0.9425
  = 0.3π (the predicted minimiser radius), with the same F = 2.072617. The limits are **pairwise up to 1.592 apart**. This is
  the 2-sphere of minimisers: non-unique.
- **P2: path b_s = exp(s e_1), s ∈ [π − 0.05, π + 0.05].** The Karcher mean moves from ≈ exp(+0.3π e_1) to ≈ exp(−0.3π e_1),
  a total of 2wπ = 1.885, over a data change of 0.01 on either side of s = π.
  - It does this in two steps of 0.939 through the degenerate point s = π, where qlog(−1) = 0 and the iteration stalls at
    the start.
  - So it is **discontinuous in the data**. The cut-off m_w is constant (= a, step 3.7e-17).
- **P3: one hand-built cell with two near-antipodal pairs (δ = 1e-3, t = (½, ½)).** The Karcher mean is start-independent
  there, because the weights are not balanced on the antipodal pairs. So near-antipodality alone does not force failure.
- **P4: 200 random 4-corner configurations near {+p, −p}.** Spread 1e-4 to 1e-1, t ∈ [0.2, 0.8]², 8 starts each.
  - Among the 172 mixed-sign cases, the starts disagree by ≥ 0.1 in **74**, and some runs fail to converge in 500
    iterations in **128**.
  - In the same-sign cases there is no disagreement.

So **CL-F4 for the Karcher gluing OCCURS on near-antipodal data, as non-uniqueness, non-convergence and discontinuity, and the
cut-off gluing is continuous there.** This confirms 22.13's last remark and the motivation for Z^off. It also confirms lane
B's diagnosis of why K10 failed on Haar-spread data.

## E.3 bb7n and the amplitude deviation
**The code.**
- R^{ax} matches Construction GC, d = 2: the axial tree axis 0 then axis 1, D_ax = 5, μ on face links via the transverse
  potentials, and the coarse link multiplied in.
- The curvature profile |log hol| is gauge-invariant.
- N-c (3.4e-16) is a genuine test of exact covariance for a Haar level-k gauge.

**The deviation.** s := target/f_raw was computed from qexp(b) with b ~ N(0, 1), whose plaquettes are near the wrap. So the
runs had f_k = 0.26 and 0.52.

**Consequences.** None adverse.
- The thresholds are relative.
- Running at a larger amplitude is a *harder* test of the nonlinear regime.
- But nothing was measured at the f_k ≤ 0.10 promised, and the "2a" label is really 0.52. That is outside any plausible ε_1
  of Theorem N2, whose absorption ε_1 involves C_eΛ_2² and is ≪ 0.5. So bb7n illustrates rather than tests N2 at 2a.

**My amplitude-corrected run: ALL PASS.**
- Method: a copy with the scale found by bisection so that f_k is exactly 0.1000 and 0.2000 (revBB7/bb7n_amp.py); otherwise
  identical.
- At f_k = 0.10:
  - R_1, R_2, R_3 = 1.2769, 1.3100, 1.3272;
  - deviation from the linear chain 0.0006·f_k (against 0.0026 at 0.26);
  - N-c 4.3e-16;
  - stencil ratios 1.468, 2.859, 4.905 (< 5.06).
- At f_k = 0.20: 1.2768, 1.3100, 1.3261.
- The deviation from the linear profile (1.2771, 1.3102, 1.3278) shrinks roughly linearly with f_k, as Theorem N2's O(f)
  correction predicts.

**N-d's ungauged informational number** (5.33·f_k at f_k = 0.26; 1.89·f_k at f_k = 0.10).
- This is not noise. exp(linear refinement) treats the coarse links that face links carry additively, so it misses the
  commutators [b_x, b_y] at block corners, which are O(|b|²) own.
- Relative to f_k it scales like |b|, i.e. ∝ f_k: the ratio 2.8 matches the amplitude ratio 2.6.
- So the frame-free construction already fails without a large gauge. The control's 876 (2340 at f_k = 0.10) includes this,
  together with the gauge effect.
- It is still a valid control. State it so.

**N-a (R_3 ≤ 1.15·max(R_1, R_2)).** This is weak evidence over depths 1-3. The ratios 1.277, 1.310, 1.325 track the linear
chain 1.277, 1.310, 1.328, which is bounded by Λ_2. Fine as an illustration.

## E.4 bb7c, bb7g
- bb7c: the code matches its criteria. The Q_sym and Q_asym contours are correctly built (C0 1.3e-16). The re-run differs
  only in the timing line. Scope note in C.4: it is a model of the S4' family.
- bb7g: exact FFT; the transverse-sum and unimodality checks. The re-run is byte-identical.

---

# Overclaims and underclaims
1. **RS7-1.** Step-1 tags (l.1901, 1975, 2473-2475, 2666, 2710-2711, 2774) assert §22 results before §22 existed, and are not
   disclosed as planned.
2. **RS7-2.** "Post-proof correction (1)" (l.2965-2966, 2986, l.3217) replaces a correct constant with a misreading of m'.
3. **RS7-3.** "injective, rate-preserving" (l.2994) is false for continuous-time paths; the result is true by B.2.
4. **RS7-5.** §23 l.3237-3239 "off 𝒞_glob no wall is added": true only with (N1-int) and (N2-bd) in local form.
5. **RS7-6.** "(CovLift) … on every torus" (§12.2) versus Z^off's need T ≥ 5.
6. **Underclaim.** Remark PL extends to T = 1, 2 (B.1). Theorem KΠ-off's "PROVEN modulo the cited Karcher-free facts (none)"
   (l.3236) is accurate: no Karcher fact remains in Z^off.

# Tally (lane B session 7; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | provenance by byte accounting (§21 = 11674 B; §18 minus tags = 12505 B); RBB6 fixes (all nine); **Remark PL** (constant e^{20m}); Lemma S2K; **Lemma N2-step**; **Theorem N2** ((N2-0) per level, k-uniform, curvature-only; (N2-lip) without k − j); Corollary N2-cons; **Lemma Γ0** (given L1 per transverse direction; lane A's Q uniform); **Proposition Cg-lin**; C_g design decision (residual component); **Lemma CUT**; **Lemma CL-clu** (repairs a gap REVIEW_BFT_B_S6 missed); **Proposition TOP** (a)-(c); bb7g, bb7c, bb7n (re-runs identical); bb7k K1-K8 |
| CONFIRMED-WITH-FIX | **Theorem KΠ-off** ((CovLift) (i)-(iii) on 𝒦(ε) for every gauge; RS7-4 log branch for N ≥ 3, RS7-5 local walls, RS7-6 T ≥ 5 and symmetry note, RS7-7 explicit smallness); **Lemma N1G** (result CONFIRMED; reflection step replaced, RS7-3) |
| PROVEN HERE (reviewer) | monotonicity of the cycle heat kernel by the Metzler/maximum-principle argument (B.2) |
| ARGUED (reviewer) | LRL (b) for T = 1, 2 by the q-fold lift (B.1) |
| AS MARKED | Cg-NL's BCH remainder ARGUED; Remark HOL ARGUED; TOP (d) cited |
| NEW (reviewer probes) | near-antipodal CL-F4 for the Karcher gluing OCCURS, and the cut-off gluing is continuous there (E.2); bb7n at the promised amplitudes ALL PASS (E.3) |
| OPEN | (N1-int), (N2-bd) (now to be stated locally); non-residual components of g_Z at θ > 0; V_l's (Res-Hölder) = (NC-Γ); Q(chain V) = Q(V) (informational); hypercubic symmetrisation in (I-id) (note) |

# Required fixes (binding for the next lane-B session unless marked cosmetic)
1. **RS7-1 (provenance).** Append "(planned at the time of this tag, Step 1 10:23; proof written 10:38)" to the Step-1 tags
   at l.1901, 1975, 2473-2475, 2666, 2710-2711 and 2774. Do not rewrite them.
2. **RS7-2.**
   - Revert post-proof correction (1). LRL (b) uses weight m on both sides, so C_b(T) ≤ e^{(4T+4)m}C_b(2T) ≤ e^{20m}C_b(2T).
   - Fix l.2965-2966, l.2984-2986 and table l.3217.
   - Optionally add the q-fold lift for T = 1, 2 (B.1) as an ARGUED remark.
3. **RS7-3.**
   - Replace 22.2 step (2) by the Metzler/maximum-principle proof of B.2.
   - Annotate the §18.0 tag l.2473-2475 and the §21.1 description ("reflection lemma"), adding "(proof replaced:
     REVIEW_BFT_B_S7 B.2)".
4. **RS7-4.** In §21.0's cut-off definition (annotated in §22, not edited in §21), define log as the inverse of exp on the
   injectivity ball into su(N), or require r_2 < π (HS-angle normalisation). Note that bb7k's SU(2) normalisation is
   unaffected.
5. **RS7-5.** Restate (N1-int) and (N2-bd) in local form (on Ω^{(−r)} given V^h = e^b on Ω). Change §23 l.3237-3239 to
   "no wall is added, given the local forms".
6. **RS7-6.**
   - (a) Read (CovLift)'s "every torus" as T ≥ 5 for Z^off.
   - (b) Add a sentence: the axis-ordered constructions break hypercubic covariance, so the marginal-coupling extraction
     symmetrises.
7. **RS7-7.** State C_clε ≤ r_1/2 ≤ (convexity radius) and Ω ⊇ the corner boxes of Ω^{(−r)} as explicit hypotheses of
   Theorem KΠ-off (iv)-(v) and Lemma CL-clu.
8. **RS7-8 (cosmetic).**
   - Fix the cocycle convention in §12.2 (i): with (U^a)^b = U^{ba} it reads ĥ(h_2h_1, V) = ĥ(h_2, V^{h_1})ĥ(h_1, V).
   - bb7k_criteria K10: record that the control was mis-designed. Cite this review's E.2 probe as the control actually
     demonstrating CL-F4.
   - bb7n: record the corrected-amplitude reviewer run.
   - C.4: cite BFT_A l.1112 for the uniform S4' average, and remove the question to lane A in §23.
   - bb7c C3's threshold is tight (C.5).

# Strategic verdict
- **Session 7 is a correct and useful session.** The two walls REVIEW_BFT_B_S6 ranked highest for lane B both moved:
  - **(N2-0)** is now a theorem: per level, k-, T- and j-uniform, curvature-only. The proof is the manifold-subdivision
    proximity mechanism, made explicit with axial frames.
  - **The C_g clause** is stated and proven linearly for all 0 ≤ θ ≤ 1, by a symmetry (Γ0) rather than a redesign. No lane-A
    change is needed.
- **(KΠ-off) for (i)-(iii) is closed**, on the whole locally-small class, by a construction that is honest about where
  continuity is and is not needed.
  - The Karcher route's CL-F4 was a self-inflicted obstruction.
  - The genuine topological fact (Proposition TOP) constrains only continuum smoothness on spread data.
- **What remains for (CovLift):**
  - (iv): (N1-int) (routine) and (N2-bd) (moderate; Theorem N2 is its sup-level zeroth order, and the Hölder version follows
    the same telescope with α < 1), both in local form;
  - the non-residual components of g_Z at θ > 0;
  - Cg-NL's BCH remainder;
  - (v) in frames (ARGUED).
- **Recommended order for session 8:**
  1. RS7-1..RS7-7 (short);
  2. (N2-bd) in local form, the Hölder telescope on (N2-lip);
  3. (N1-int);
  4. the non-residual g_Z components at θ > 0;
  5. Cg-NL's remainder, which needs lane A's nonlinear root map;
  6. help lane A on (NC-Γ) with Lemma RT for composite-co-closed sources (S6 B.4 lever).

# Current minimal open set for BFT-0..4 (merged with lane A's latest: REVIEW_BFT_A_S6, plus lane A session 7 unreviewed)
- **BFT-0/1/2 (m = 0, trivial background):**
  - (H-lin^∇): the gauge-invariant half holds for all level-wise co-closed sources and all T ≥ 1 (lane A S5-S6, reviewed).
  - The residual-gradient part (Theorem RHT) and the configuration half in S_E (Corollary LRL(b)-E) hold for T ≥ 5, and now
    for **T ≥ 3** by Remark PL, with T = 1, 2 by the q-fold lift (ARGUED).
  - **Open:**
    - **(NC-Γ)** for Γ = Γ_E: the composite-divergence content of the non-co-closed BCH₂ and Wilson rows. Lane A session 7
      claims Proposition SR ((NC-Γ) sup of f_0 ⇐ (PW-ℓ¹) + SPD), unreviewed; its named wall is (PW-ℓ¹).
    - the endpoint α = θ;
    - explicit constants.
  - (H-rem^∇) third order: ARGUED. (FP♯').
- **BFT-3:**
  - k = 1 PROVEN.
  - k ≥ 2 ⇐ weighted (H-inv)_m on the co-closed classes. Lane A's S6 m-part is CONFIRMED for 0 ≤ m ≤ m_Y (astronomically
    small). Lane A S7 (unreviewed) claims Theorem W0_m; DX_m and DB_m are OPEN.
  - The weighted (Res-Hölder)_m is CONFIRMED (RHT_m).
  - Plus V_l at m > 0.
- **BFT-4:**
  - k = 1 PROVEN.
  - k ≥ 2 bounded polymers ⇐ RW^∇_k-Π(E) [(W-Π) PROVEN; (W-lin-Π) ⇐ (H-inv) + (NC-Γ)] + (W-comm) [GAP 1 plain rows] + (W-loc) +
    (f) + (E3^∇) [ARGUED] + (I-id).
  - Gauge-invariant pieces ⇐ (CovLift) = Z^off (on 𝒞_glob it coincides with the clustered construction):
    - (i)-(iii): **PROVEN on 𝒦(ε) for every gauge** (with RS7-4, RS7-6, RS7-7);
    - (iv): (N1-int) [routine] + (N2-bd) [moderate], both in local form, plus (C_g-θ) [linear PROVEN; BCH remainder ARGUED;
      non-residual components at θ > 0 OPEN];
    - (v): ARGUED (frames).
  - Plus (Mult-Y) [GAP-1 family] + (Pair-loc) [ARGUED] + (I-id)_Z [ARGUED, plus the hypercubic symmetrisation note].
  - **Off 𝒞_glob:** GI-off [ARGUED] needs (Mult-Y), (SL-cov) and (I-id) off 𝒞_glob (lane A's BFT-0 there). It **no longer
    needs (KΠ-off)** for (i)-(iii).
- **Rate:** κ_L ≥ m/8 under weighted (H-inv+)_m = weighted (H-inv)_m (RHT_m) + localised (W-comm) (RATE-m).
- **Largest levers:**
  - (a) (NC-Γ), with lane A's (PW-ℓ¹), plus Lemma RT for composite-co-closed sources (lane B can help);
  - (b) the (Pl)-free plain-row theory (GAP 1 + (Mult-Y));
  - (c) (N2-bd) + (N1-int) in local form, which would complete (CovLift) (iv) on the whole of 𝒦(ε);
  - (d) the non-residual g_Z components at θ > 0.

---

## Re-run record and reviewer probes
**Runner.** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revBB7/run_bb7rev.sh`.
- It waits with `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, then waits for load1 < 8.
- Environment: nice 10; OMP/OPENBLAS/MKL/VECLIB/NUMEXPR threads = 1; PYTHONDONTWRITEBYTECODE=1; `/usr/bin/time -l`; python3
  without -I; no `timeout`; no trap; `rmdir` exactly once at the end.

**One acquisition, 10:52:37-10:54:24 UTC.** Load1 3.78; memory free 39% at the start, 38% at the end.
- bb7g_n1g: byte-identical, including its timing line; 0.28 s; 279 MB. stderr carries a NumPy 2 DeprecationWarning
  (`irfftn` with `s` but no `axes`, l.25), which will become an error in a future NumPy (cosmetic).
- bb7c_resid: identical apart from `[t = …]`; 0.42 s; 264 MB.
- bb7n_chain: byte-identical; 0.81 s; 178 MB.
- bb7k_off: identical apart from `[t = …]`, including K10 FAIL; 63.3 s; 35 MB.
- Reviewer probes:
  - revBB7/bb7n_amp.py (bisection amplitudes): ALL PASS, numbers in E.3; 0.9 s; 178 MB.
  - revBB7/antipodal_probe.py: P1-P4 in E.2; 40.6 s; 34 MB.

**Afterwards.**
- The lock directory is absent.
- `pgrep -fl 'bb7|antipodal'` is empty.
- There is no __pycache__ in checks/.
- Outputs are in scratchpad/revBB7/ (*.rerun.out, *.rerun.time, bb7n_amp.out, antipodal_probe.out, lock.log).
- No repository file other than this review was written.
