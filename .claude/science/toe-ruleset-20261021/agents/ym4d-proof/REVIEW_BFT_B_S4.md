# REVIEW_BFT_B_S4: hostile review of BFT lane B session 4 (BFT_B.md [RBB3-fix] edits, §12-§14; checks bb4, bb4_diag)

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md, HIST.md or the checks. This is the only file I
edited. No commits, PRs or pushes.

Inputs (read 2026-10-28 ≈07:55-08:10 UTC; `TZ=UTC stat` BFT_B.md born = modified 07:49:58, 217135 bytes; BFT_B_LOG.md
modified 07:50:13, 20499 bytes):
- BFT_B.md: every [RBB3-fix] tag in context (33 tag strings, l.942-1957); §12-§14 and the session-4 FOR OTHER FILES
  (l.1584-1957) in full; §10.1-§10.3 (W-ls, W-cut, W-mult; l.1216-1278) for the norms and cutoffs.
- BFT_B_LOG.md session 4 in full. REVIEW_BFT_B_S3.md (format; Part E; required fixes).
- BFT_A.md: §12.0-§12.2 (S_tent, LR-pot, LR-grad; l.879-950), §13.12-§13.13 (LR-pot proof, LR-grad; l.1123-1166), §16
  (LRL (a), Lemma FC, Theorems XR/XB, Corollary HX, Proposition CO; l.1226-1300).
- HIST.md §20.0-§20.2 (F1-F6, Whitney interpolation, Theorem MSG, MSG-loc' and the superseded MSG-loc; l.1184-1306).
- checks/bb4_criteria.md, bb4_models.py (parts A and C line by line; B in outline), bb4.out, bb4_diag.py, bb4diag.out,
  their .time files; `TZ=UTC stat` of all.

Re-run: bb4 and bb4_diag under the numeric lock. Record at the end.

---

## Bottom line

- **Provenance: CONSISTENT.** File order criteria (07:36:13) < script (07:39:19, last byte 07:40:55) < output
  (07:41:10-22) < post-hoc diagnostic (07:44:49; output 07:45:28-07:46:08) < §13/§14 (final 07:49:58, 217135 bytes) matches
  the log. §12's 07:30:46 write is self-reported only (the file has been rewritten since), but nothing in §12 cites a
  session-4 result. Its one forward pointer "[RBB3-fix RW3-3]" (l.1617) is disclosed in the log. All four post-proof
  corrections are marked in §13's header (l.1704-1708). §12 itself already anticipated part of (Mult-Y) (l.1647-1648, "needs
  covector multiplication (a GAP-1-type plain row)"), so §12's "the one new input is (CovLift)" (l.1667) was inconsistent
  within §12 already. The correction in 13.7 is right.
- **RBB3 fixes: all applied, correctly.** I checked RW3-1..RW3-5, BP3-1, BL3-1, item 9, RS3-1..RS3-7 and the m = 0
  mechanism note in place. One fix does not reach §12/§13: RW3-3's product-partition local-torus side **4R + 14** is not
  carried into T^Π_W and T^cov_W (binding **RS4-1**).
- **Lemma W-gauge0: CONFIRMED** (even simpler: 0 is the global minimum of 𝔉_k(·; 0)).
- **Theorem RW^∇_k-Π: CONFIRMED as an implication**, with fix RS4-1 and a wording fix on "∇ the S-gradient" (RS4-2).
- **Corollary BB-mix_k-Π: CONFIRMED.**
- **RWΠ-F1: the diagnosis is CONFIRMED, but the repair is INSUFFICIENT and the failure is not the main one.**
  - 𝔐^∇ contains the Hölder seminorm of the gradient, [∇^cx^c]_α. In Π(φu) − φu the tents enter through dχ, so ∇^c of the
    correction contains χ''. C^{1,1} tents have jumps in χ'', and those jumps cost ρ_0^{-α} = L^{αk} in [∇^cx^c]_α.
    **C^{2,α} tents are needed** (e.g. the quintic smoothstep).
  - More important: **(W-lin-Π) already fails for S_tent** by lane A's own LR-grad diagnosis: S_tent does not control
    gradients, a loss of L^{k(1−α)} [ARGUED in BFT_A]. A second mechanism of the same kind threatens (W-Π) itself.
  - So Theorem RW^∇_k-Π currently has no slice that satisfies it. The slice must be lane A's proposed elliptic
    (box-Coulomb, tent-patched) slice, with smooth tents.
- **Lemma GI-frame: CONFIRMED** (unitary). **Lemma GI-norm: CONFIRMED-WITH-FIX**: a numerical slip, ||Ad_{e^a} − 1|| ≤ 3|a|
  is false at |a| = ½ (RS4-5); the residual term is ARGUED, as stated.
- **Lemma GI-pert: CONFIRMED as an implication given (Mult-Y), with two overclaims.**
  - The residual component of the X-multiplier bound is the same ARGUED BCH/residual issue as in GI-norm (b), not
    "PROVEN-HERE in the same way".
  - The Feynman-difference term is a differential operator, not a "pointwise multiplier"; it too lands in (Mult-Y).
  - Fix: RS4-3.
- **Theorem GI-cov: CONFIRMED as an implication.** I re-derived the cocycle step with explicit Ad-composition conventions.
  The cocycle does remove GI-F2 exactly.
- **Theorem BB-gi_k (on 𝒞_glob, given (CovLift) + (Mult-Y)): CONFIRMED as an implication**, with RS4-1 (the torus side)
  and with the ARGUED local pairing bound for non-residual components named as a third soft input.
- **Corollary BFT4-poly^gi_k: CONFIRMED.**
- **Proposition GI-off: ARGUED, accepted.**
- **(Mult-Y) is NOT closed by lane A's LRL/XR/XB.** Those give only the X_s (residual-output) half of the response to
  co-closed rough or carrier-decaying currents. (Mult-Y)'s currents are general plain currents. Their curvature outputs
  ((CO-0), (CO-up)) and configuration-level gradients (LR-grad) are OPEN, and the (Pl) slot is refuted as written (BL-6 (b)).
- **(CovLift): OPEN. Proposition CovLift-status's table is sound.**
  - **It is NOT a corollary of Theorem MSG plus smoothing.** MSG gauges a *given* chain. Its bound is in **own** units
    (coarse-unit size up to L^{k−j}C_Mε). It is frame-dependent, and its Q1-Whitney reference field is only Lipschitz across
    faces.
  - **Shortest route:** an inductive one-level covariant refinement (corner lift + constrained covariant smoothing), whose
    linearisation is a C^{1,α}-convergent commuting subdivision scheme, with MSG-type BCH absorption. Details in Part E.
  - **Most robust route:** Balaban's variational lift, with the walk expansion as the localiser.
- **RW∇-F5: CONFIRMED in the model, and harmless.**
  - The coarse mass is the top residual κ_{k−1}|r_{k−1}|², which is part of the soft functional at every RG step, so it is
    legitimately available k-uniformly.
  - It is not a physical mass and does not conflict with m = 0.
  - bb4 A-1 shows exponential (not 1/R) decay. That supports the weighted route to an O(1) cluster rate.
- **bb4: reading CONFIRMED.**
  - C-5 and B-6 are honestly recorded as failed predictions, not repaired, and the diagnostic is labelled post hoc.
  - **Re-run: byte-identical** (bb4 and bb4_diag, timing lines excluded).

---

# PART A: provenance and the [RBB3-fix] edits

**A.1 Provenance: CONSISTENT.**
- Stat of the checks: bb4_criteria.md born = modified 07:36:13; bb4_models.py born 07:39:19, modified 07:40:55 (the logged
  pre-run edit: tolerance 1e-15 → 1e-14, an unused helper removed). Neither edit touches a criterion.
- bb4.out and .time: 07:41:10-07:41:22. bb4_diag.py 07:44:49. bb4diag.out 07:45:28-07:46:08. BFT_B.md final
  07:49:58 / 217135 bytes and the log's final line agree.
- bb4_diag.py's docstring says "POST-HOC diagnostic … does not change bb4's verdict". It imports bb4_models unchanged.
- §12 cannot be re-statted to 07:30:46 (rewritten since), so that time rests on the log. Internal evidence supports it:
  - §12 lists failure modes with "Expected" outcomes, including RWΠ-F1, which §13 then argues.
  - The bb4 criteria's thresholds (C-5 plateau 2; B-6 thresholds 1e-6/1e-8) are ones that later FAILED. A writer with the
    results would not have chosen them.
- Pre-stated (§12) versus proven (§13), checked item by item:
  - GI-pert: §12 pre-stated "(W-lin)_Z … PROVEN as an implication". §13 adds (Mult-Y) as an input; marked.
  - BB-gi_k: §12 "one new input". §13 "two"; marked.
  - GI-frame: §12 unrestricted. §13 unitary only; marked.
  - Theorem RW^∇_k-Π: unchanged.
  - Nothing proven in §13 was absent from §12 except the (Mult-Y) label and C_eq/C_F constants.

**A.2 [RBB3-fix] edits: CONFIRMED (one carry-over missing).**
- RW3-1 (l.1227): t_X = 4, t_Y = 6 are inserted into N_P, ε_W, R_W, 𝔠_W, σ and the BB-mix bound. Correct; it matches my
  summand count (𝔐^∇ four terms; Y six).
- RW3-2 (l.1334): x''-argument as I gave it.
- RW3-3 (l.1340): R ≥ 13 or T ≥ 3R + 14; product partitions with local tori 4R + 14 and (2M_c + 6)⁴. Correct.
  **Not carried into §12/§13: T^Π_W := 3R + 14 + 2r_Π (l.1616) and T^cov_W := 3R + 14 + 2r_Z (l.1652, l.1813) are the
  box-side-R values. For product partitions they must be 4R + 14 + 2r_Π and 4R + 14 + 2r_Z. ℓ_Ω in Lemma GI-frame's C_F
  (l.1765) becomes ≤ 4R + 12 + 2r_Z** (RS4-1).
- RW3-4 (l.1347): the operator mismatch is stated. The hard-slice form is in §12/§13 and the mixed form is flagged OPEN.
  Correct.
- RW3-5 (l.1532): the overclaim is struck. GAP 1 / BL-6 (b), LR-grad and the slice are named. Correct.
- BP3-1 (l.1171, 1460, 1519, 1575), BL3-1 (l.1183, 1468, 1569): correct.
- Item 9 (l.1161): correct.
- RS3-1..RS3-7: correct. RS3-1 at l.942 now points to §10.5's c_ρ = 4S_ρ/r_ρ.
- m = 0 mechanism note (l.1543): correct. It already names the weighted route via Theorem W, which Part F supports.

---

# PART B: hard slice (§12.1; §13.1-§13.2)

## B.1 Lemma W-gauge0 (l.1612; proof l.1710-1719): CONFIRMED
- F6: one level-0 gauge acts on the chain through its values at the level-j sites. If it vanishes at the level-k sites, the
  data V = 1 are untouched, so F(Ψ_t x) = F(x) exactly.
- ξ(0) = Dλ is correct (left-trivialised).
- ∇F(0) = 0 needs nothing beyond F ≥ 0 = F(0): the trivial chain with trivial data is a global minimum of the soft
  functional. Citing W-grad0 is fine but unnecessary.
- The remark that a Feynman term breaks the lemma is correct, which is why the Feynman form used (W-loc) (iii).

## B.2 Theorem RW^∇_k-Π (statement l.1615-1620; proof l.1720-1750): CONFIRMED as an implication; fixes RS4-1, RS4-2

I re-derived each step.

- **(a)** It needs Πx − x ∈ 𝒢_0 for x ∉ S. (W-Π) states it for every x. Correct.
- **(b)-(c)** Locality and the definition of C_ψ. Correct.
- **(d)** W-gauge0 in the second slot (𝓑 symmetric), then the slice equation tested against Π_□(ψιv') ∈ S(𝕋_□). Correct.
- **(e)** Only Π_□(ψιv') on ι□^{(4)} is read. Π's reach r_Π puts the inputs in □^{(4+r_Π)} ⊂ □^{(R/2)} (R ≥ 2r_Π + 8),
  where ψ = 1 (Lemma W-cut: ψ = 1 on □^{(R/2)}) and v' = v. So the value is ι(Πv) = ιv. Correct.
  - Tacit requirement: ι must carry the tent/root lattice to itself, i.e. translation by a coarse-lattice vector. Boxes sit
    at integer coarse positions, so this holds. The model uses an even shift (sh = 22).
  - State this in (W-Π)'s "one local formula" clause (cosmetic, RS4-6).
- **(f)** x''-argument. Correct.
- **Step 3** Transport region □^{(R+r_Π+3)} (side 3R + 2r_Π + 6 < T^Π_W for box side R). The count ≤ 4 boxes per axis holds
  for R > 2r_Π + 6. The 5^d in ε^Π_W is inherited from §10.7 (R_□'s support), as before. Correct.
  - **RS4-1:** with product partitions the box side is up to 2R, the side is 4R + 2r_Π + 6, and T^Π_W must be
    4R + 14 + 2r_Π.
- **Step 4** Onto ⇒ invertible (finite dimension), with values in S. Correct.
- **Step 5** Distance (γ) > 0 for R > r_Π + 2. Correct.
- **RS4-2 (wording).**
  - The corollary's reading "(f), (E3^∇), (I-id) read with ∇ the S-gradient" (l.1623) is ambiguous.
  - 𝔈_Q (l.1408) pairs per-density full gradients ∇D with S_Q𝐀, whose cube components are not in S. A pairing of an
    S*-element with them is undefined.
  - What the proof needs: ∇ is the full X-gradient represented in Y; π_S enters only through 𝓛_S^{-1}π_S; and ΔE(1)'s
    ⟨∇E(A), A⟩ = ⟨π_S∇E(A), A⟩ = 0 because A ∈ S.
  - With that reading the corollary's two steps are correct.

## B.3 Corollary BB-mix_k-Π: CONFIRMED (given RS4-2)
- s ≡ 1 gives the slice-critical equation.
- (I-id) in slice form identifies A = x(B).
- The trapezoid sum at s ≡ 1 telescopes to E(A) − E(0) − ½⟨∇E(A), A⟩ with the full gradient, and that last term is 0.
- No other step uses the operator's form.

## B.4 RWΠ-F1 (l.1684-1687; remark l.1751-1757): diagnosis CONFIRMED; repair INSUFFICIENT; the main failure lies elsewhere

**What I verified.**
- Since u ∈ S, Pλ(u) ≡ 0, so Π(φu) − φu = d(Pλ(φu)) = d(Σ_Xχ_Xμ_X) with μ_X = λ_X(φu) − φλ_X(u). The φ(z)-terms cancel
  under Σχ_X (this is why φ itself needs no extra smoothness).
- Writing x := Π(φu) − φu = Σ_X(dχ_X)μ_X + Σ_Xχ_X[dλ_X(φu) − φ dλ_X(u)]:
  - **First term (tent mechanism).** In coarse units x^c ∋ Σχ_X'μ_X and ∇^cx^c ∋ Σχ_X''μ_X. With Σχ_X'' = 0 the
    coefficient is μ_X − μ_*, generically of size ||u||/ℓ. That difference is ∫(φ(w) − φ(z))u along the root-to-root
    path, which is ≠ 0 for ∇φ ~ 1/ℓ.
    - Piecewise-linear tents: χ' jumps, so ||∇^cx^c||_∞ ~ L^k||u||/ℓ. **B's claim is CONFIRMED.**
    - **C^{1,1} tents: χ'' jumps** (σ'' = −4 → +4 at t = ½; 0 → ∓4 at t = 0, 1). 𝔐^∇ contains [∇^cx^c_j]_α over boxes of
      side ρ ∈ [ρ_j, 1] (W-ls fix, l.1227; W-mult (3)). A jump J in ∇^cx^c gives ρ_0^{-α}·J/2 = **L^{αk}·O(||u||/ℓ)**.
      **The proposed repair fails the Hölder-gradient term.**
    - The contrast with Lemma W-cut is exact: there cutoffs multiply x undifferentiated, so C^{1,1} suffices. Here tents
      enter differentiated once, so they need one more derivative: **C^{2,α}**.
    - A concrete choice: σ_5(t) := 1 − (10t³ − 15t⁴ + 6t⁵). It has σ_5(t) + σ_5(1 − t) = 1, σ_5' = σ_5'' = 0 at 0 and 1,
      so χ = Πσ_5(|·|/n) is C^{2,1}; and |σ_5'| ≤ 15/8.
  - **Second term (axial mechanism; not addressed in §13).**
    - dλ_X(φu) − φdλ_X(u) contains the axial strip flux of (φ(w) − φ(z))f, with f = du ∈ C^α only. Its transverse coarse
      gradient involves ∫∂_⊥f along an axial segment, which costs ρ_0^{α−1} = n^{1−α}. This is exactly lane A's LR-grad
      mechanism (BFT_A l.1153-1156).
    - u ∈ S ∩ 𝔐^∇ controls only the tent-weighted, order-averaged, unweighted fluxes. Those are what u is built from, via
      u = Πu. It does not control the individual (X, σ) fluxes with the weight φ(w) − φ(z).
    - Integration by parts along the path would work if each single (X, σ) flux were C^1 in z. That is not known.
    - **Status: a plausible second failure of (W-Π) for S_tent, independent of tent smoothness [ARGUED here].**
- **(W-lin-Π) already fails for S_tent.** Lane A records (BFT_A l.1153-1156, ARGUED) that minimisers in S_tent lose up to
  L^{k(1−α)} in ∇^c. That is the negation of (W-lin-Π) in 𝔐^∇. So the hard-slice theorem's slice inputs are expected false
  for S_tent whatever the tents.
  - §13.2's remark and the §14 table (l.1921) say only "C^{1,1} tents would be needed". They miss this, and they miss the
    C^{2,α} point.

**Would smooth tents keep the projection algebra and lane A's results?**
- **Projection algebra: YES.** It uses only Σ_Xχ_X = 1 and χ_X(c_Y) = δ_{XY}, both of which hold for Πσ(|·|/n) with
  σ(t) + σ(1 − t) = 1, σ(0) = 1, σ(1) = 0. Then λ(c_Y) = 0, P∘P = P (BFT_A l.1124-1128 verbatim), and P − 1 ∈ 𝒢_0.
- **LR-pot: YES, with constants × sup|σ'|.** The proof uses Σ_X dχ_X(b) = 0 (still true), Σ_X|dχ_X(b)| ≤ 2/n (becomes
  ≤ 2 sup|σ'|/n: ×2 for σ of W-cut, ×15/8 for σ_5), "the transverse factors sum to 1" (true), and the same supports N_X
  (true). So C_1, C_2, C_3 scale by ≤ 2, and c_0 is unchanged.
- **Corollary FP: YES** (same constants scaling).
- **XR/XB/LRL (a): not affected.** They are about Coulomb potentials and flux coarse-grainings, not S_tent.
  - Where lane A's §18 uses "tent" formulas (BFT_A l.1461, 1531-1535), those are level-l block tents of Q^T structure, not
    χ_X. I did not re-derive them; lane A to confirm.
- **Recommended slice (for lane A; also its own LR-grad plan):** box-local Coulomb gauge patched with **C^{2,α}** tents.
  Then Π is local with r_Π ~ box size, and (W-Π)'s C_Π comes from interior Schauder (LES-div) plus a box Gaffney inequality.
  (W-lin-Π) for that slice = LR-grad.

**Fix RS4-4 (binding).** Rewrite RWΠ-F1's repair as: "C^{2,α} tents (C^{1,1} fails the [∇^c·]_α term by L^{αk}); and S_tent
fails (W-lin-Π) by lane A's LR-grad diagnosis and plausibly (W-Π) by the axial-flux mechanism. Theorem RW^∇_k-Π awaits an
elliptic slice." Apply at l.1754-1757, at the §14 table row (l.1921), and in FOR OTHER FILES (2) (l.1943-1945).

## B.5 bb4 C (hard-slice model): CONFIRMED as model algebra
I read the code line by line.
- SliceModel: Π = 1 + D·Pλ, with λ_X = −½Σ_orders (line integral) and linear tents of half-width b = 2.
- The slice solve u = Πw with (B + (1 − Π)^T(1 − Π))w = Π^Ty. I verified that this gives w ∈ S and Π^TBu = Π^Ty, because
  BΠ = B, Π^TB = B and Π^T(1 − Π)^T = 0. So it is 𝓛_S^{-1}π_S exactly.
- C-3 tests Π^T(BPy − (1 − R)y), i.e. 𝓛_SP^Π = π_S(1 − R^Π).
- C-2 is trivially true in this model (curl ∘ d = 0, and Λ(dλ) = λ(c + be_μ) − λ(c) = 0 at roots). That is fine: it is
  W-gauge0's content.
- Not tested (correctly disclosed): 𝔐^∇ norms, so RWΠ-F1 is untested.

---

# PART C: covariant centring (§12.2; §13.3-§13.9)

## C.1 Lemma GI-frame (l.1638-1640; proof l.1758-1768): CONFIRMED (unitary)
- (a) g_Ω(V)(x) = hol_V(γ_x)^{-1}. hol_{V^h}(γ_x) = h(root)^{-1}hol_V(γ_x)h(x), which gives g_Ω(V^h) = h^{-1}g_Ω(V)h(root),
  and the principal log commutes with conjugation. Correct.
- (b) Ladder ≤ Σ_{ν>μ}|x_ν − root_ν| ≤ (d − 1)ℓ_Ω.
  - The root is the lowest corner of □, but Ω extends below it. The bound still holds with ℓ_Ω.
  - Lasso (F4) and (F1) (valid for ||1 − U|| ≤ ½ with 1.0107). On 𝒞_glob ||1 − V_p|| ≤ 4ε by (F2) plus subadditivity.
    Correct.
- C_F(Ω) ≈ 1.011·3·(3R + 12 + 2r_Z) ≈ 9R: an O(R) loss absorbed by ε_gi(R) (R is fixed before ε). Accepted.
  - RS4-1: ℓ_Ω ≤ 4R + 12 + 2r_Z with product partitions.
- Complex data ARGUED: acceptable (as in U0-ℂ).

## C.2 Lemma GI-norm (l.1641-1644; proof l.1769-1781): (a) CONFIRMED; (b) CONFIRMED-WITH-FIX (RS4-5)
- (a) ∇^{Z^ĥ}(Ad_ĥx) = Ad_{ĥ(y)^{-1}}∇^Zx. Transported box values pick up a common Ad (oscillations unchanged). The residual
  is root-covariant (F6). Correct; exact invariance.
- (b) **Slip:** "||Ad_{e^a} − 1|| ≤ e^{2|a|} − 1 ≤ 3|a| (|a| ≤ ½)" is false at |a| = ½ (e^1 − 1 = 1.718 > 1.5). It holds for
  |a| ≤ ⅓ (e^{2/3} − 1 = 0.948 ≤ 1). Since the own-unit |a| = ρ_j|z^c| ≤ δ ≤ δ_0 is small, nothing downstream changes.
  **RS4-5 (cosmetic):** read |a| ≤ ⅓.
- The rest of (b): multiplier M = (Ad_{e^z} − 1)/ρ_j with ||M|| ≤ 3δ and osc ≤ 3dρδ; W-mult's product rule; C_eq ≤ 12d + 6
  (crude). I accept it.
- The residual term (Dρ(Z) − Q) with k-uniform weight L^{k−1−j}: ARGUED, BA-6 type, as stated.

## C.3 Lemma GI-pert (l.1645-1649; proof l.1782-1805): CONFIRMED as an implication given (Mult-Y); overclaims (RS4-3)
- The formula for 𝓛_Z and g_Z = J_z^T∇E(z) is correct. Note the extra O(δ²) term ⟨Γz, ΓD²β_z(0)[·,·]⟩ inside Hess F_Z(0),
  since Γβ_z(0) = Γz ≠ 0. It is harmless.
- **Overclaim 1 (l.1788-1789).** "On X such multipliers are bounded (1 + C_Xδ) … PROVEN-HERE in the same way":
  - The sup, gradient and Hölder parts: yes. W-mult's (1)-(3) need only Hölder ∇M, which the 𝔐^∇-size of z supplies.
  - **The residual part: no.** J_z acts levelwise (J_{z_j} on x_j, J_{z_{j+1}} on x_{j+1}). The residual commutator
    contains (J_{z_{j+1}} − Q_jJ_{z_j}Q_j-type) × x_{j+1}. This is a nonlinear-BCH comparison of J at z_{j+1} with the block
    average of J at z_j, controlled only through r_j(z) and gradients at the k-uniform weight L^{k−1−j}. That is the same
    ARGUED item as GI-norm (b)'s residual term.
  - Mark it ARGUED.
- **Overclaim 2 (l.1787).** "the Feynman difference [is a] pointwise multiplier of 𝔐^∇-size O(δ)": D_ZD_Z^* − J^TΓ^TΓJ is a
  second-order differential operator X → Y. Its source is "δ-coefficient × derivative of x", i.e. (G)/(Pl)-type sources:
  inside (Mult-Y), not a multiplier on X.
- The **(Mult-Y)** isolation is correct and honest: transposes of multipliers generate plain currents (dJ^{-1})∧x and
  [r, J^{-1}]x. Same family as GAP 1.
- (I-id)_Z ARGUED: correct as flagged. The two Feynman conditions select different orbit representatives; local uniqueness
  modulo gauge is (FP♯')-type.
- **RS4-3 (binding):** in 13.5, mark the residual component of the X-multiplier bound ARGUED, and move the Feynman
  difference into (Mult-Y).

## C.4 Theorem GI-cov (l.1659-1663; proof l.1806-1839): CONFIRMED as an implication

**Step 1.** The frame transplant identifies the global operator at Z^sm(V), read in ĝ_□, with 𝓛_□ on □^{(R+6)}. This uses
(CovLift) (ii) with Ω_□ = □^{(R+6+r_Z)} and the reading radius 3. The arbitrary extension of g_□ outside Ω is irrelevant by
(ii). Correct (with RS4-1 for product partitions).

**Step 2 (re-derived with explicit conventions).** For the right action, Ad_{g_1g_2} = Ad_{g_2}∘Ad_{g_1}.
- The cocycle gives ĥ·ĝ_□(V^h) = ĝ_□(V)c on the r_Z-interior, so Ad_{ĝ(V^h)} = Ad_c∘Ad_{ĝ(V)}∘Ad_ĥ^{-1}.
- With 𝓖(V^h) = Ad_c𝓖(V)Ad_c^{-1} (constant-gauge covariance, (CovLift) (i) with ĥ(c, ·) = c), we get
  P_□(V^h) = ψAd_ĥAd_{ĝ(V)}^{-1}Ad_c^{-1}ι^*Ad_c𝓖(V)Ad_c^{-1}ι_*Ad_cAd_{ĝ(V)}Ad_ĥ^{-1}χ = Ad_ĥP_□(V)Ad_ĥ^{-1}.
- The cocycle identity is needed, and used, only on the region where the frame objects are read. Correct.

**GI-F2 analysis: CORRECT.** A stabiliser element s of Z^sm(V) on Ω commutes with the global operator there, but not with
the local-torus inverse, whose background is 1 off the embedded Ω. The cocycle pins ĝ.
- Where stabilisers are trivial (irreducible local holonomy), ĥ is unique and the cocycle is automatic.
- Near reducible or flat backgrounds it is a genuine requirement. It holds automatically for lifts defined in a
  gauge-normal form relative to the level-k sites (Part E).

**Step 3.** Covariance of 𝐊(s) (scalar weights), of g_Z and 𝔑_Z (joint invariance of the background-Feynman density), the
ball (GI-norm (a)), uniqueness, and invariance of the densities. Correct. The class is gauge invariant. Correct.

**Model check.** bb4 B-1..B-5 PASS with the background given. They test exactly Steps 1-3 (no lift).

## C.5 Theorem BB-gi_k (l.1664-1669; proof l.1840-1856): CONFIRMED as an implication
- The chain composes correctly: GI-frame + (CovLift) (iv) → 𝔐^∇-small backgrounds on 𝕋 and every 𝕋_□ (b̃_□ is globally
  sup-small on 𝕋_□) → GI-pert with (Mult-Y) → (H-RW^∇)_k for the covariant construction (Steps 2-5 of §10.7 unchanged,
  constants ×2) → §10.8 verbatim at Z → GI-cov.
- The threshold ε_gi ~ 1/(C_smC_F(R)·…) with R ∝ s̄ is k- and T-uniform. Correct.
- Replacing W-grad0 by ||g_Z||_Y ≤ C_gC_Fε plus a local pairing bound is correct.
  - The pairing bound is PROVEN for residual components (W-pair) and ARGUED for (G), (P0), (Pl). State it in the theorem's
    input list as **(Pair-loc) [ARGUED]**: it is a third soft input next to (CovLift) and (Mult-Y).
  - The C^cov_E product-partition factor (2M_c + 6)⁴/(M_c + 6)⁴ < 2⁴ is correct.
- Gauge saturation follows by invariance. Correct.
- Verdict line, to use: **(BB-gi)_k on 𝒞_glob ⇐ BB-mix_k's hypotheses (pure background-Feynman form) + (CovLift) [OPEN] +
  (Mult-Y) [GAP-1 family, OPEN] + (Pair-loc) [ARGUED] + (I-id)_Z [ARGUED].**

## C.6 Corollary BFT4-poly^gi_k (l.1871-1878): CONFIRMED
- E^cov_∅ is a gauge-invariant local sum (densities at Z^sm(V), reading V within 3 + r_Z, the same locality convention as
  R(X)'s X^{(8+r_Z)}).
- The bound C^cov_∅ is finite by holomorphy.
- "Bounded, not small relative to S_W" and "c_k = 1 needs BB-4♮'s m > 0 inputs" are honest.

## C.7 Proposition GI-off (l.1857-1870): ARGUED, accepted. Points I checked
- (4) is right and worth keeping. Global invertibility on any torus side follows from the right inverse
  P(1 − R)^{-1} built from local tori alone (π onto ⇒ 𝓛 onto). Global holonomies and torons enter only through the local
  tori, where the top residual removes the zero modes.
- The missing items are listed correctly: (I-id) off 𝒞_glob (lane A's BFT-0 there), (SL-cov) or a background-covariant
  local slice, (CovLift), (Mult-Y). The slice variant inherits B.4: a covariant elliptic slice with C^{2,α} tents, not C^{1,1}.

## C.8 Is (Mult-Y) closed by lane A's LRL/XR results? **NO.**
- (Mult-Y) needs, for a plain level-l current J = c·G (c a coefficient field of 𝔐^∇-size δ, G a Y-source):
  - (i) representability in Y with norm ≤ C_Yδ||G||;
  - (ii) (W-lin) on J, i.e. a configuration-level 𝔐^∇ response bound.
- (i) for the "c × (Y-source)" part is the product rule of W-mult with Hölder coefficients: fine. The transposition
  currents (dJ^{-1})∧x and [r, J^{-1}]x are *plain* currents, so (i) needs the (Pl) slot, which BL-6 (b) refutes as written.
- (ii), measured against what lane A has:
  - **Theorem XR**: X_s outputs only (residuals) for **co-closed rough** currents w ∈ R_l, with gain:
    ||r||_{X_s,Σ} ≤ C_XR L^{2(k−l)}sup|w|_own = C L^{−(k−l)}||w^c||_∞.
  - **Theorem XB**: X_s outputs for carrier-decaying (SPD-H) families only.
  - **Corollary HX**: X_s only.
  - **LRL (a)**: single-level Coulomb-potential C^{1,α} bounds for exact 2-forms. This is an *ingredient* of LR-grad, not
    LR-grad.
  - **Missing:**
    - the gradient (non-co-closed) part of J, which pairs with gauge directions (in the Feynman or slice form it is not
      zero);
    - the smooth part S_l = Q^T(C_{l+1});
    - the curvature outputs ((CO-0), (CO-up), OPEN, Proposition CO);
    - the configuration-level gradients (LR-grad, OPEN).
- **Status: (Mult-Y) OPEN.** Its co-closed-rough X_s part is covered by XR. It closes together with GAP 1's plain rows,
  provided lane A's eventual (Pl)-free repair (the CR-1-type split) treats "smooth coefficient × source" currents
  generally, as FOR OTHER FILES (3) says.
- Alternative that avoids (Mult-Y): assume the background hypotheses (W-lin)_Z etc. directly, as (SL-cov) on 𝒞_glob, i.e.
  lane A's estimates at smooth backgrounds. This is needed off 𝒞_glob anyway, so (Mult-Y) is a convenience cost of GI-pert,
  not an independent wall.

---

# PART D: failure modes, the check bb4, and its honesty

- **GI-F1** does not occur (constant c commutes through 𝓖_□). Correct.
- **GI-F2** occurs without the cocycle. Correct.
- **GI-F3** [argued]: the BCH mismatch between frames is O(ε²) in coarse units, a jump across faces. Its coarse gradient is
  ~ L^{k−j}ε². I accept it.
- **RWΠ-F1**: Part B.4.
- **RW∇-F5**: Part F.
- **C-5 FAIL.** The criterion assumed r_Π ≈ 3 (T^Π_W = 3R + 14 + 2·3). The measured reach is 1.5, so the plateau 2 already
  covers it.
  - D1: the identity fails at plateau 0.5 only (6.9e-4), consistent with Step (e)'s requirement. The theorem's
    R ≥ 2r_Π + 8 is sufficient, not sharp.
  - Recorded as a failed prediction; not repaired. **Honest.**
- **B-6 FAIL.** At μ² = 1 the frame-free defect, transmitted from the transplant cut at distance R + 6 = 10, is
  exponentially small (2e-10).
  - D2's mass scan (1.9e-5, 1.3e-2 at μ² = 0.25, 0.05; frame ≤ 2e-14) confirms the mechanism.
  - Recorded as a failed prediction; the diagnostic is labelled post hoc; the verdict stays 12/14. **Honest.**
- **A-1/A-2**: Part F.
- **Limits** (as disclosed, plus one): B uses a given background, so (CovLift) is untested; C uses sup norms, so RWΠ-F1 is
  untested; there is no k-uniformity.
  - Added: A's coarse mass acts at block scale 3 with R = 6-30. This is a faithful ratio to "coarse mass at scale 1, R ≥ 13
    coarse units". The decay it shows is exponential, so A-1 does not test the 1/R law; it tests something stronger.

---

# PART E: (CovLift): route verdict

**The six candidates (l.1880-1888): verdicts accepted**, with three sharpenings.
1. **Corner lift.** Covariant, with a block-constant ĥ that is a homomorphism, so the cocycle is trivial; finite range;
   holomorphic. It fails 𝔐^∇ smallness only through fine-scale curvature concentration. **It is the natural covariant seed.**
2. **Variational lift.** Exponential, not finite, locality. That is acceptable if (CovLift) (ii) is relaxed to exponential
   locality: GI-cov Step 1 then holds up to e^{−cR} terms, which can be booked into R_□ (a walk-expansion-type error).
3. **Cocycle.** For any lift defined as a gauge-normal form relative to the level-k sites (or block centres), ĥ is
   determined uniquely by the normal form, so the cocycle and ĥ(c, ·) = c are automatic. GI-F2 is then a non-issue by
   construction.

**Is (CovLift) a corollary of Theorem MSG plus smoothing? NO.** Four reasons, from HIST l.1213-1306:
- (1) MSG *gauges a given chain*. It does not construct a chain from level-k data.
- (2) MSG's bound |log U_i^g(b)| ≤ C_Mε is in **own units**. In coarse units (the 𝔐^∇ units, x^c_j = L^{k−j}x_j) it allows
  L^{k−j}C_Mε. Only the local form MSG-loc', iterated with smooth-scale sources (ε̂_j ~ L^{−2(k−j)}ε), gives coarse-unit sup
  smallness. Even then the c_qα_cell² term is the non-local quadratic piece.
  - The S3 review's phrase "MSG gives depth-uniform sup smallness (the potential half)" must be read in own units.
    **Correction to REVIEW_BFT_B_S3 Part E.**
- (3) MSG's reference field V = exp(Ia) uses Q1-Whitney forms. They are tangentially continuous but only Lipschitz across
  cell faces, so the [∇^c·]_α term fails by L^{α(k−j)} (the same mechanism as B.4).
- (4) MSG is built from one box axial frame (root at a corner), so it is covariant only up to that frame. A global lift by
  gluing box frames is GI-F3.

**Shortest route (proposal; ARGUED):** (CovLift) ⇐ (R1) + (R2) + (R3).
- **(R1) One-level covariant refinement.** For each level-(j+1) configuration, Z_j := Φ(corner lift of Z_{j+1}). Φ is a
  finite number O(L²) of steps of a gauge-covariant smoothing descent at level j, constrained to the root-map consistency
  M̄_c(Z_j) = Z_{j+1} (S4'; the constraint manifold is invariant under the block-constant extensions).
  - Exact covariance and the cocycle come from the corner lift's homomorphic ĥ. Φ commutes with all level-j gauges.
  - Finite range O(L²) per level gives r_Z = O(1) in coarse units.
  - Holomorphic.
- **(R2) Linearised C^{1,α} subdivision.** In a small gauge, the linearisation of the iterated refinement is a stationary
  linear subdivision scheme on Lie-algebra-valued 1-forms that commutes with d (a spline de Rham pair of degree ≥ 3 in place
  of Q1 Whitney).
  - Its iterates converge in C^{1,α} with level-uniform constants (classical stationary-subdivision theory) [IMPORTED-NOT-
    YET-REVERIFIED; this is a finite, abelian, checkable statement about one mask: a joint spectral radius below L^{−(1+α)}
    on second differences].
  - This replaces MSG's contraction L^{−1} in sup by the same contraction in C^{1,α}.
- **(R3) Non-abelian absorption.** MSG-type BCH absorption per level, in C^{1,α} instead of sup.
  - Here MSG enters genuinely: MSG-loc' supplies the depth-uniform small gauges in which (R2)'s linearisation is valid. Its
    quadratic c_qα² term is a C^{1,α} source of size ε², contracting by L^{−1}.
  - New lemma: the C^{1,α} version of MSG step (6).
- The decisive new statement is (R2). It is numerically testable on a d = 2 abelian model before any proof.
  **Recommended next check (lane B): measure the C^{1,α} norm of the iterated refinement of a smooth coarse field over
  depths 1-5 for Q1 Whitney versus a cubic-spline commuting pair.** Prediction: Q1 grows like L^{αj}; the spline stays
  bounded.

**Most robust route (longer):** the variational lift Z^sm(V) := argmin of a covariant smoothing functional at fixed Z_k = V.
- Covariance comes from uniqueness, so the cocycle is automatic.
- 𝔐^∇-smallness = BFT-1 regularity (lane A's LRL/LR-grad).
- Exponential locality comes from Theorem RW^∇_k applied to the lift functional's Hessian. That is Balaban's architecture,
  with the lift's localisation inside the induction.
- It shares all of lane A's open linear inputs, so it adds no independent wall, but it closes only when they do.

---

# PART F: RW∇-F5 and the m = 0 theory

- **Measured (re-run identical):**
  - A1 (−Δ + (1/9)P_blk): G_□ 5.38 → 8.93 bounded; R·r_□ 3.11 → 0.0106. This is exponential: e^{−≈0.23R} between R = 12
    and 30, not 1/R.
  - A0 (−Δ + global mean penalty): G_□ ×13 (≈ R^{1.6}, the 2D log-weighted volume sum); r_□ ≈ 1.2-1.3 with no decay.
- **Verdict: RW∇-F5 CONFIRMED in the model, and harmless for the YM RG.**
  - **Is a coarse mass legitimately available? YES.** It is the top residual term κ_{k−1}|r_{k−1}(x)|² of the soft
    functional, with x_k := 0: displacements are taken at fixed data V. It is the RG's soft block-spin kernel, present at
    every step with κ_j ∈ [κ_−, κ_+], hence k-uniform.
    - It is not a physical mass. The fluctuation covariance at fixed coarse data is massive at the block scale. That is
      standard in Balaban/Gawędzki-Kupiainen: G_k(Ω) decays at rate O(1) in block units. It is compatible with massless YM,
      whose masslessness concerns the data V across steps.
    - Lane A's Proposition W / Theorem W (PROVEN-HERE; weights e^{m d}, 0 ≤ m < m'_*) is the gauge-invariant statement of
      this coarse mass.
  - **Gauge directions.** In the Feynman form, 𝒢_0's λ vanishes at level-j sites level by level. The Feynman term then gives
    scale-by-scale Dirichlet-point masses (lane A's uniform-G statement covers this). In the hard slice they are absent.
  - **Implications:**
    - (i) (W-lin) must be (and is) stated for the operator including the top residual, on the local tori too (copies of the
      same functional). So RW∇-F5 does not apply.
    - (ii) A purely massless local inverse would break RW^∇_k. Any variant that drops the top residual on local tori, e.g.
      a "compressed" operator without the mass term, is excluded.
    - (iii) **Positive consequence:** with the coarse mass, the weighted route [RBB3-fix m = 0 note, l.1543] gives
      ε_W(R) ≲ e^{−mR}·poly(R). Then M_c ~ m^{-1}log s̄ and κ_L = O(m), replacing the tiny κ_L ~ log M_c/M_c.
      Its inputs are the configuration-level (W-lin)_m (Theorem W's gauge-invariant half PROVEN; LR-grad weighted OPEN) and
      a localised (W-comm).
    - FOR OTHER FILES' SF line (l.1957, "the rate remark … stands") should add "for the unweighted form; the weighted form
      would give κ_L = O(m'_*)" (RS4-7).

---

# Overclaims
1. l.1754-1757, l.1921, l.1943: "C^{1,1} tents" as the repair. It is insufficient (C^{2,α} needed), and S_tent fails
   (W-lin-Π) independently (RS4-4).
2. l.1788-1789: GI-pert's X-multiplier bound "PROVEN-HERE in the same way". The residual component is ARGUED (RS4-3).
3. l.1787: the Feynman difference is called a "pointwise multiplier". It is a differential operator, inside (Mult-Y) (RS4-3).
4. l.1667 (pre-stated) "the one new input is (CovLift)". Already corrected in 13.7. Also add (Pair-loc) [ARGUED] (C.5).
5. Session-3 review (mine to correct): "MSG gives depth-uniform sup smallness" holds in own units only (Part E (2)).

# Tally (lane B session 4; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | provenance; RBB3 fixes (except the RS4-1 carry-over); **Lemma W-gauge0**; **Corollary BB-mix_k-Π** (RS4-2 wording); **Lemma GI-frame** (unitary); GI-norm (a); **Theorem GI-cov** (cocycle step re-derived); Corollary BFT4-poly^gi_k; bb4 reading, honesty of C-5/B-6, D1/D2; re-run byte-identical |
| CONFIRMED-WITH-FIX | **Theorem RW^∇_k-Π** (RS4-1 torus side, RS4-2 gradient wording, RS4-6 lattice-compatible embedding); GI-norm (b) (RS4-5); **Lemma GI-pert** given (Mult-Y) (RS4-3); **Theorem BB-gi_k** (RS4-1; (Pair-loc) named) |
| CONFIRMED diagnosis, REJECTED repair | **RWΠ-F1** (C^{2,α} tents; S_tent fails (W-lin-Π) by LR-grad; axial-flux mechanism for (W-Π) ARGUED) |
| ARGUED (accepted) | Proposition GI-off; Proposition CovLift-status; GI-F3; (I-id)_Z; complex GI-frame |
| OPEN | **(CovLift)** (not an MSG corollary; route R1-R3 proposed); **(Mult-Y)** (not closed by LRL/XR/XB); (Pair-loc) for (G), (P0), (Pl); the mixed slice + Feynman form; an elliptic slice satisfying (W-Π) + (W-lin-Π) |
| model-confirmed | RW∇-F5 (harmless: the top residual is the coarse mass) |

# Required fixes (binding for the next lane-B session)
1. **RS4-1.** With product partitions (RW3-3), read T^Π_W = 4R + 14 + 2r_Π (l.1616), T^cov_W = 4R + 14 + 2r_Z (l.1652,
   l.1813), and ℓ_Ω ≤ 4R + 12 + 2r_Z in C_F (l.1765). Box-side-R values stand for T a multiple of M_c.
2. **RS4-2.** In Corollary BB-mix_k-Π (l.1622-1623 and the 13.2 corollary), ∇ is the full X-gradient represented in Y;
   π_S enters only via 𝓛_S^{-1}π_S; the ΔE(1) identity uses A ∈ S.
3. **RS4-3.** In 13.5, mark the residual component of the X-multiplier bound ARGUED (same item as GI-norm (b)), and list the
   Feynman difference D_ZD_Z^* − J^TΓ^TΓJ under (Mult-Y).
4. **RS4-4.** Rewrite RWΠ-F1's repair (l.1754-1757, the l.1921 table row, FOR OTHER FILES (2)):
   - C^{2,α} tents (e.g. σ_5) are required (C^{1,1} fails [∇^c·]_α by L^{αk});
   - S_tent fails (W-lin-Π) by lane A's LR-grad diagnosis, and plausibly (W-Π) by the axial-strip-flux mechanism (B.4);
   - Theorem RW^∇_k-Π awaits an elliptic (box-Coulomb, smooth-tent) slice.
   - Keep: the projection algebra and LR-pot survive smooth tents, with constants × sup|σ'|.
5. **RS4-5 (cosmetic).** GI-norm (b): |a| ≤ ⅓ for ||Ad_{e^a} − 1|| ≤ 3|a|.
6. **RS4-6 (cosmetic).** (W-Π)'s "one local formula": the local-torus embedding is a translation by a coarse-lattice
   vector, so roots map to roots.
7. **RS4-7.** Theorem BB-gi_k's input list: add (Pair-loc) [ARGUED for (G), (P0), (Pl)] and (I-id)_Z [ARGUED]. SF line
   (l.1957): "stands for the unweighted form" plus the weighted κ_L = O(m'_*) remark (Part F (iii)).
8. Proposition CovLift-status: add the corner-lift + constrained-covariant-smoothing refinement as a seventh candidate, with
   (R1)-(R3), and note the own-units reading of MSG (Part E).

# Strategic verdict

- **What session 4 achieved.**
  - A correct hard-slice RW^∇_k.
  - A clean and genuinely correct covariance mechanism: frames + cocycle ⇒ exactly gauge-invariant polymers.
  - This reduces (BB-gi)_k on 𝒞_glob to a lift statement plus a GAP-1-family representability.
  - bb4 B shows the mechanism exactly, and D2 shows why frame-free transplants fail at small mass.
- **What it did not achieve.**
  - The hard slice has no admissible slice yet: S_tent fails (W-lin-Π), and C^{1,1} tents do not repair (W-Π).
  - (CovLift) is untouched beyond triage.
- **Current minimal open set for BFT-0..4** (on 𝒞_glob unless marked):
  - **BFT-0/1/2:**
    - (H-lin^∇) at configuration level in 𝔐^∇: (G♯_0-lev0) = (CO-0); (G♯-up) = (CO-up); (G♯-rough) curvature half; (SB);
      **LR-grad**. The X_s halves are PROVEN (XR, XB, HX), and so are the potentials (FP).
    - (H-rem^∇) third order ARGUED.
    - (FP♯').
    - **An elliptic slice with C^{2,α} tents**, or the Feynman/mixed form matched to Theorem BA.
    - Off 𝒞_glob: (UHL)/LR-grad, (SL-cov), Z^sm.
  - **BFT-3:** k = 1 PROVEN. k ≥ 2 ⇐ (H-lin^∇)_m, m > 0, at configuration level. The gauge-invariant half is PROVEN
    (Theorem W).
  - **BFT-4:**
    - k = 1 PROVEN (gauge-invariant pieces).
    - k ≥ 2 bounded polymers on 𝒞_glob ⇐ (W-lin) + (W-comm) [GAP 1 plain rows] + (W-loc) [slice/Feynman form] + (f) +
      (E3^∇) [ARGUED] + (I-id). Not yet jointly satisfiable in one norm pair.
    - **Gauge-invariant pieces ⇐ + (CovLift) [OPEN] + (Mult-Y) [GAP-1 family, OPEN] + (Pair-loc) [ARGUED] + (I-id)_Z
      [ARGUED].**
    - c_k = 1 ⇐ BB-4♮'s m > 0 inputs.
    - Off 𝒞_glob: GI-off (ARGUED).
  - **Rate:** the weighted (W-lin)_m + localised (W-comm) give κ_L = O(m'_*). The coarse mass is legitimately the top
    residual.
- **The two levers with the largest fan-out (unchanged in kind, sharpened):**
  - (a) **the (Pl)-free plain-row theory** ((G♯-rough) + (SB), CR-1-type split for "smooth coefficient × source"). It
    closes GAP 1 and (Mult-Y) together.
  - (b) **a covariant C^{1,α} lift / elliptic gauge.** LR-grad, the elliptic slice for RW^∇_k-Π and (CovLift) via (R1)-(R3)
    all need the same C^{1,α}-uniform multilevel interpolation estimate. Test (R2) numerically first.

---

## Re-run record (bb4 and bb4_diag)
- Runner: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revBB4/run.sh`.
  - It waits with `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, then waits for load1 < 8.
  - Environment: nice 10; OPENBLAS/OMP/MKL/VECLIB threads = 1; PYTHONDONTWRITEBYTECODE=1; `/usr/bin/time -l`; python3
    without -I; no `timeout`; no trap.
  - It runs checks/bb4_models.py and then checks/bb4_diag.py, both unchanged, with outputs in revBB4/.
  - It calls `rmdir` exactly once.
- Lock held 08:03:51-08:04:43 UTC (one acquisition, free on arrival). load1 4.93; memory free 44%.
  - bb4: 11.0 s wall, peak RSS 835 MB, exit 0.
  - bb4_diag: 40.7 s, 154 MB, exit 0.
- After the run: the lock directory is gone, no bb4 process is left, and checks/ holds no __pycache__.
- **Result:** with the `[t = …]` and `setup` timing lines removed, revBB4/bb4.out is **byte-identical** to checks/bb4.out
  (VERDICT NOT ALL PASS (12/14); C-5, B-6 FAIL as recorded). revBB4/bb4diag.out is **byte-identical** to
  checks/bb4diag.out (D1 6.862e-04 at plateau 0.5, measured r_Π = 1.50; D2 2.130e-10 / 1.910e-05 / 1.344e-02).
