# REVIEW_HW_S1: hostile review of lane H session 1 (HW.md: (H-w), conflicts K5 and K3)

Reviewer: an independent agent that wrote none of HW.md, HW_LOG.md or checks/w1_*. I edited no other file. No commits, PRs
or pushes.

Inputs (read-only):
- HW.md (all, 468 lines; md5 d63b86b8… at review time), HW_LOG.md (all).
- checks/w1_criteria.md, w1_kernel_moments.py, w1_out.txt, w1_time.txt, w1_stderr.txt, and their mtimes.
- HIST.md §7.1-§7.4 (l.452-573), §15.1-§15.4 (l.956-1056), §20.3 (B)-(C) (l.1370-1425), HIST_LOG tail. HIST.md md5 is now
  468e9f03…, not the fd756e0b… that HW recorded at 01:51 UTC. Lane D's session 4 (§24-§29) was appended concurrently.
- RLARGE.md v2 §2-§5 (l.227-487) and §8 (K1-K10, l.558-595); RLARGE_INTEGRATION_LOG.md (all).
- PLD.md §15.2-§15.3 (l.966-1103: per-history measures, (SG^fl), HS-net, INH, PLD-desc).
- REVIEW_HIST_S3.md (format; bottom line; N-4, S3-5).

Scratch work (the w1 re-run) is in the scratchpad directory `rw1/`.

Status words as in PROOF.md. "Line" means a line of HW.md unless another file is named.

---

## Bottom line

- **The core idea is right, and it matters.**
  - Lemma HR writes the history weight in exact indicator form.
  - Proposition PF shows that bounds relative to Z_K cannot feed HIST-sum.
  - Lemma RX supplies the relaxed law μ_{R(𝔥)}.
  - Lemma CH (one pointwise Chernoff inequality under that single law) resolves K5. All four are correct, and K5 is resolved
    as stated: the branch prices did not combine because their moments were taken under three different laws.
  - No hidden independence is used. All dependence between defects sits inside the joint-moment hypotheses (M-i) and (M-f).
- **Lemma KS (SU(2)): CONFIRMED.** I re-derived (a)-(d). The constant 3/2 is sharp and g-independent. KS-chain and H4-red
  are CONFIRMED (H4-red as CONDITIONAL ⇐ (LI)).
- **Theorem HW: CONFIRMED-WITH-FIX.** Two fixes are binding:
  - **(W-1) The θ range is wrong.** (M-f)_{96θ} can hold only for 96θ < 1. HW's own heuristic in §6 gives (1 - λ)^{-dof/2},
    and at λ ≥ 1 one expects a log(1/g) per degree of freedom (HW-F1). So θ ∈ (0, 1/96), not (0, 1/24).
  - **(W-2) The constant is superseded.** It must be HIST's C_cone (RH3-fix N-4), not max{C_loc, 2/η_E}.
- **Proposition FV: CONFIRMED (CONDITIONAL ⇐ (AE)).** It is a two-line corollary of TE, so I recount it as uncounted. Its
  architectural reading is correct. It refutes RLARGE v2 §3.3's claim that the removed-cone normalisation is absorbed at
  e^{B_0} per cube, at a fixed bad coarse field. It does NOT refute PLD-desc, whose law μ^+ is forward and which works only
  on good V. HW's description of PLD-desc as a "fixed coarse field" law is inaccurate.
- **(REL) is not the right residual.** Under (ref-a) it is not an independent node-A, paper-scale item.
  - Sequential conditioning (Lemma REL-seq below, reviewer's proof) reduces (REL) to the same Chernoff machinery, with
    B ≤ 164·ε_♯ → 0.
  - The input needed is (M-i) and (M-f) stated over the family of intermediate relaxed laws.
  - HIST's B_0 list (a)-(d) belongs to the R-operation representation. It does not appear in ∫W·1_𝔥.
- **(M-f) is where the large-field problem now sits. It is not "UV-dominated small-field."** Its exponential moment sees
  the returned finer-level defects in Q's column, and these are allowed under μ_R. The Chernoff loop that would bound them
  loses a factor ≥ 4 in rate per level, so it cannot close by induction. (M-f) should be re-labelled OPEN [P]. Its
  large-field-tail half is new and has no owner.
- **K3: arithmetic CONFIRMED** (K3-a, K3-b), with one small quantifier fix. Both items are moot for HW's own (ref-a) route,
  which has no extraction.
- **w1: re-run reproduced every line** (§7 below). Procedure honest. Both runs were disclosed; the criteria said "one run".
- **Corrected tally: 4 counted** (HW-1 with fix, HW-2 with fix, HW-4, HW-5), not 5. FV is uncounted.

---

## Priority 1. Lemma HR and Proposition PF

### Lemma HR (l.72-83): CONFIRMED (elementary, uncounted)
- **Induction.** 𝒰_j(c) depends on (U_{j-1}, U_j) and on 𝒰_{<j}(c) through Λ^pre_j. On {𝒰_i(c) = 𝒰_i, i < j} the j-th
  factor is exactly 1^𝔥_j. (A1) holds by construction. (A2) holds because 𝒰_j(c) ⊂ Λ^pre_j = complement of Σ(Ω^c_{j-1}).
- **Partition of unity.** Σ_𝔥1_𝔥 ≡ 1, so Z(𝔥) := ∫W1_𝔥 ≥ 0 and Σ_𝔥Z(𝔥) = Z_K. Correct.
- **Remark (1) (l.80-82): overclaim, not load-bearing.** "Z(𝔥) is the history weight of HIST §7.4 once the defect rules are
  fixed" is asserted without proof.
  - HIST's weights come out of the R-operation: the CL^J Mayer step, gas exponentiation and extraction. Whether every
    R-operation term lands in the same 𝔥 as ∫W1_𝔥 is not checked here.
  - Nothing needs it. (H-w) (HIST l.528-532) only asks for SOME decomposition Z_K = Σ_𝔥Z(𝔥) with Z(𝔥) ≥ 0.
  - **Fix H-1:** *define* Z(𝔥) := ∫W1_𝔥 and delete the identity claim, or mark it [inference].

### Lemma RX (l.85-92): CONFIRMED, with one scope fix
- **(i) is correct.** Distinct *-components are not *-adjacent, so the small components miss N_1(𝒰_j).
- **(ii) and (iii) are correct** for a history-independent D_j.
- **The scope note is incomplete.** The text says only that (iii) uses the history-independent convention (l.83). (ii) needs
  it too, and so does the consequence Z(∅) ≤ Z(R(𝔥)). With RLARGE/HIST's two-threshold collar rule (HIST l.466-468),
  D_j(c; 𝒰_{<j}) differs between 𝔥 and ∅, and (ii) can fail.
- **Fix H-2:** "(ii) and (iii) use the history-independent convention of §0." Theorem HW uses only that convention, so no
  result changes.

### Proposition PF (l.97-108): CONFIRMED. Correct and important.
- **The proof is one line and correct.**
- **The reading needs one sentence.** Z_K-relative per-history bounds cannot give any lower bound on P(𝔥 = ∅).
  Counterexample: a law with one large defect component at a uniformly random position has P(𝔥) = 1/|T| ≤ w for every fixed
  w once |T| ≥ 1/w, and P(∅) = 0. **Fix H-3 (recommended):** add this counterexample.
- **The consequence is correct.** RS-joint (HIST l.505-525) is proven under W/Z_K and cannot be multiplied into (H-w) as it
  stands. This is the precise reason the v1/v2 joint pricing was never a proof of (H-w).

### Lemma HS' (l.115-118) and (H-w)³ (l.120-131): CONFIRMED
- HIST-sum's step (2) (HIST l.555) uses Σ_k|Ω^c_k| only through the double shadow sum. So (H-w') suffices.
- (H-w)³ is (H-w') with the constants stated.

## Priority 2. Theorem HW-split and the per-defect weight

### Theorem HW-split (l.133-143): CONFIRMED (one line from RX)
- **Reading of the weight (l.124-130):** energy price e^{-θa_Du_j} × mismatch moment × fine moment. Correct, given Theorem
  HW.
- **(REL) as stated:** under (ref-a) it is the probability statement μ_{R(𝔥)}(R(∅)) ≥ e^{-B·shadow}. Correct.
- **Owner attribution (l.138-140): not accepted.** It says (REL) "is HIST §7.4's B_0 list (a)-(d)". See Priority 5:
  under (ref-a), those items are artifacts of the R-operation representation and do not occur.
- **A stray bracket.** "[inference, not used]" at l.140 sits mid-sentence and does not say what it qualifies. **Fix H-4:**
  attach it to the sentence it qualifies.

## Priority 3. K5: TE, W-bad, W-cb, DJ, CH, Theorem HW

### Lemma TE (l.159-171): CONFIRMED-WITH-FIX
- **(i)** E_𝒞(P) = κΦ_{∂P} + (non-top terms), so the infimum is at most its value at the actual U. Correct.
- **(ii)** CLS-red's strong form holds for every chain (HIST l.1028-1032), so it passes to the infimum. Correct.
  - **The constant is superseded.** HIST l.1030-1031 [RH3-fix N-4] gives C_cone := max{C'_AE/(2N), 2/η_E}. The value
    max{C_loc, 2/η_E} belongs to the superseded (AE) (REVIEW_HIST_S3 N-4).
  - HIST §27 gives C_cone ≈ 10¹⁵. With ε_1 fixed, a_bad ≈ ε_1²·10⁻¹⁶/N, which is the magnitude REVIEW_HIST_S3 flagged.
  - **Fix W-2 (binding):** C'_cl := C_cone throughout (l.162, 176, 191, 232). a_bad stays g-independent, so nothing
    structural changes.
- **(iii)** Checked:
  - A link with both endpoints in Q lies in ≤ 2(d - 1) plaquettes with all vertices in Q (w1 C1 re-confirmed: max 6).
  - Non-top terms of 𝒞(P), P ∈ 𝒫(Q), have their vertices in W_P^{(·)}, which lies under P's corners, which are sites of Q.
    So they are column terms of Q.
  - HIST overlap: each term lies in ≤ 24 cones of one level (HIST l.970-971).
  - Σ inf ≤ inf Σ holds because every term is ≥ 0. Correct.

### Lemma W-bad (l.173-184): CONFIRMED as CONDITIONAL ⇐ (AE) (level 0 unconditional), with fix W-2
- **Lower bound.** (B) gives s ≥ ε_1²/(2N), TE (ii) gives ℰ_P ≥ s/C. Correct.
- **Upper bound.**
  - u_{k+1} ≤ u_k + R comes from the LOWER half of (F_R) at one step: u_k - u_{k+1} ≥ β_- log L - R ≥ -R. HW's §0 attributes
    it correctly.
  - With Rg_k² ≤ 1 this gives ≤ 2u_k, hence 2·6 = 12 and 2·24 = 48. Correct.
- **Level 0.** π_Q = a_bad u_0 ≤ u_0ε_1²/(2N), since C ≥ 1. Correct.

### Lemma W-cb (l.186-198): CONFIRMED as uncounted CONDITIONAL ⇐ (AE), (TC) and the σ_Q reading
- **Algebra re-done.**
  - (TC) t ≥ (16N + 3)δ gives t - 3δ ≥ 16Nδ, and also δ ≤ t/19 ≤ t/6, so x ≥ t/2.
  - KQ with x ≥ 16Nδ gives φ ≥ x²/(4N) ≥ t²/(16N).
- **The σ_Q reading** (C(Q) ⊂ N_1(Q), RLARGE l.238-240) is consistent with RLARGE v2 §2.2. The level assignment of "p ⊂ N_1(Q)"
  is HW's reading and is not checked against PLD §9.1. It is disclosed (HW_LOG choice (b)). Keep it uncounted.
- **Multiplicity (l.269-272): constant missing. Fix W-3.** Collar windows overlap up to 81 + 1 times, and Σ_QF^col_{N_1(Q)}
  can reach about 82 times the column energy of the union. (M-f) for the collar sums at rate 96θ therefore needs
  82·96θ < 1 (heuristically, as in W-1), not 96θ < 1. State θ < 1/(96·82) for the collar extension, or carry the
  multiplicity in the hypothesis explicitly.

### Lemma DJ (l.200-205): CONFIRMED (elementary)
I completed the cross-level step the text compresses.
- Suppose Q' ∈ 𝒰_{k'+1} (k' < k) lay under Q. By H-nest (iii) every ancestor of Q' lies in Ω^c, so the level-k ancestor y
  of Q' is in Ω^c_k.
- Then Q = π(y) ∈ π(Ω^c_k) ⊂ Σ(Ω^c_k), which contradicts Q ∈ Λ^pre_{k+1}.
- Blocks are nested, so otherwise the columns are disjoint.
- **This matters for REVIEW_HIST_S3 S3-5.** Multi-level cone charges are diluted by (24k)⁻¹ "unless the selection makes the
  cones disjoint" (HIST l.1383-1392). DJ is exactly that selection for the bad windows of a history. So Theorem HW is not
  hit by the S3-5 dilution, and HW should say so (Fix H-5, recommended).
- DJ is not consumed by Theorem HW's proof (CH needs no disjointness). It is consumed only through the moment hypotheses'
  multiplicity 1, and that dependence should be stated.

### Lemma CH (l.209-215): CONFIRMED
- The pointwise bound 1{Q ∈ D_j} ≤ e^{θ(X_Q - π_Q)} holds on the event, and the right side is ≥ 0 off it. Multiply, then
  integrate against W ≥ 0. Correct.
- **Hidden dependence: none.** No product structure, conditional independence or greedy subfamily is used. HW-F2 is truly
  avoided.
- The price of this generality is that all correlation between defects at different cubes and levels sits inside
  E_{μ_R}[e^{θΣX}]. Theorem HW therefore delivers exactly what its moment hypotheses contain, and the next points check
  whether those hypotheses are plausible.

### Lemma EQ, Corollary (l.217-228): CONFIRMED
- The identity is exact.
- The K5 diagnosis ("three moments under three laws") is correct, with one inaccuracy. **Fix H-6:** PLD-desc's law μ^+
  (PLD l.973-974) is forward: U is drawn from μ_{𝔥,ω}, then V from the kernel. Only its hypothesis (SG^fl) is conditional on
  V, and only for V ∈ 𝒱^sf (good V). Say "PLD-desc under μ^+_{𝔥,ω} (forward, exterior frozen; (SG^fl) at fixed good V)".

### Theorem HW (l.259-272): CONFIRMED-WITH-FIX (CONDITIONAL; implication proven)
- **Chain re-done.**
  - (F_R) lower half at m = K gives u_k ≥ u_K - R, so g_k² ≤ 2g_K² ≤ 1/R.
  - CH with π_Q = a_bad u_j, then X_Q ≤ Y^mis + Y^fine.
  - Hölder: 2θ·12 = 24θ and 2θ·48 = 96θ.
  - The per-cube factor C_mis^{n_int/2}C_fine^{1/2}. All correct.
- **W-1 (binding): θ range.**
  - (M-i)_{24θ} via KS needs 24θ < 1. The range θ < 1/24 is chosen for that.
  - (M-f)_{96θ} is the moment of e^{λu_kF^col} at λ = 96θ, up to 4 on the stated range. HW's own §6 heuristic
    (l.350-352) evaluates it as ≈ (1 - λ)^{-dof/2}, which is finite only for λ < 1.
  - For λ ≥ 1 the moment is a partition-function ratio at non-positive effective stiffness on the column. One then expects
    a factor ∝ u_k^{dof/2}, i.e. log(1/g) per degree of freedom (HW-F1 itself).
  - As stated, the theorem is vacuous on θ ∈ [1/96, 1/24).
  - **Fix:** θ ∈ (0, 1/96). More precisely, 96θ(1 + O(Rg²)) < 1, because the level-k terms of F^col carry coupling u_{k-1} in
    W. a = θa_bad shrinks by a factor of 4, and nothing structural changes.
- **W-4 (binding, small): HIST-sum under (F_R).**
  - The "Consequently … uniformly in K" clause (l.264-265) applies HIST-sum. HIST-sum's flow hypothesis is the R-free lower
    half (HIST l.549).
  - Under (F_R), RLARGE v2 §5.2 [v2-F] (l.471-472) replaces C'_ℓ by C'_ℓe^{aR}.
  - HW's remark "no e^{aR} factor" (l.263-264) is about the defect price, not about HIST-sum's step (5). State C_H with
    C_ℓe^{aR}.
- **Collar extension (l.269-272):** carries W-3.

## Priority 4. KS, KS-chain, H4-red, FV; consequences for RLARGE v2

### Lemma KS (l.275-299): CONFIRMED (SU(2), unconditional, counted)
Line by line:
- **(a)** A real combination of SU(2) matrices is a quaternion, so M = rŴ with r = ||M||_op. The rest follows:
  - Re tr(V⁻¹M) = 2r cos α.
  - φ = r(1 - cos α), and ||V - Ŵ||²/2 = 2sin²(α/2) = 1 - cos α.
  - The Weyl density is (2/π)sin²α.
  - This needs M̄_c to be a real (convex) combination of transporters. That holds for S4' averages. It fails for SU(N ≥ 3),
    which HW handles honestly as (KS-N).
- **(b)**
  - The substitution sin²α dα = √(w(2 - w))dw is correct.
  - Chebyshev (f = w increasing, h = √(2 - w) decreasing) gives E_b[w] ≤ E_ν[w].
  - The second Chebyshev step, with h = 1{w ≤ 2} under Gamma(3/2, b), gives E_ν[w] ≤ 3/(2b).
  - Laplace's method gives the limit. Correct and sharp.
- **(c)** (log 𝒩)' = -E_s[w], then integrate. Correct, and uniform in M (r = 0 gives Haar and ratio 1).
- **(d)** Correct. Note that the suppression exponent is λκurt²/2 and carries r. For degenerate M̄ (r small) the integrand
  bound is weak. This is irrelevant to Theorem HW, which uses only (c). **Fix H-7 (recommended):** say so at Remark (2).

### Lemma KS-chain (l.301-303): CONFIRMED
- Integrate top-down. Each level's factor is a product of per-link kernel ratios, uniform in the lower field.
- "Special case of H4-red" is slightly loose: H4-red restricts 𝒦_k to links of int(𝒰_{k+1}). Read it as "the proof of
  H4-red with h ≡ 1, 1_R ≡ 1, c_k = 0", which is what is meant.

### Lemma LI-a (l.305-313): CONFIRMED (definition-level)
- **j = k + 1:** cubes at cube distance ≥ 2 have N_1(Q') ∩ Q = ∅.
- **j = k + 2:** Q'' is at distance ≥ 2 from π(Ω^c_{k+1}) ∋ π(Q), so N_1(Q'') ∌ π(Q). The level-(k+1) data read by σ_{Q''}
  and by quietness lie under N_1(Q'') and miss Q.
- Correct for the data-reading listed.

### Hypothesis (LI) (l.315-318) and Lemma H4-red (l.320-329): H4-red CONFIRMED as CONDITIONAL ⇐ (LI) (SU(2), counted)
- **The proof is right.**
  - Peel the top level k_1. By LI-a, 1_{R,k_1+1} is free of V_𝒦.
  - (LI) gives h ≤ e^c·h̲.
  - KS (c) per link applies, since the links are independent given U_{k_1}.
  - h̲ ≤ h, and ∫Π_𝒦k_c = 1.
  - The remainder is the same integral with G_{k_1} := 1. The next level's h is the plain future, because the G's above have
    been removed. Each step is valid.
- **(LI) is OPEN and plausible.** The influence of int(Q) links moves up the projection tower {π^m(Q)}, which stays inside
  the persistent shadow. The kernels of links adjacent to the tower read both endpoint blocks, so the influence leaks by
  distance 1 per level. The width-1 collar of Σ is what contains it [inference]. The sup-ratio form over ALL V, V' is
  strong, since V' can make M̄ degenerate at π(Q).
- **Fix H-8 (wording):** (LI) is "a precise form of H-4 *in the indicator representation*", not "the precise form of H-4"
  (l.250, l.315).
  - HIST's H-4 (l.521-525) concerns the effective-density tilt e^{Σρ}, expected to be 1 + O(e^{-a''_J/g²}).
  - (LI) concerns the exact future probability h and allows e^{c_LI} per shadow cube per level.
  - They are different objects with different expected sizes.

### Proposition FV (l.230-242): CONFIRMED as CONDITIONAL ⇐ (AE); RECOUNTED as uncounted
- The proof is TE (ii) plus (i) plus Φ_{∂P} ≤ Φ_{int Q} plus ℰ^<_P ≤ F^col_Q, which is two lines. It is a corollary of HW-1, not
  a separate counted item.
- **Architectural reading: correct, with the scope fixed by H-6.** At any V with ζ_Q(V) = 1, the conditional moment of
  mismatch plus fine energy is ≥ e^{λa_bad u_k}, for EVERY conditional law. Consequences:
  - **RLARGE v2 §3.3 (l.358-359)** says the removed-cone normalisation is "absorbed by the history bookkeeping (e^{B_0} per
    boundary cube)". At a fixed bad coarse field that is false. The normalisation is ≥ e^{θa_bad u_k} and cancels the price
    exactly (Lemma EQ).
  - **RLARGE v2 §2.1 and §4.3 step 6** ("each bad level-(k+1) cube is priced … before U_k is integrated") cannot be a
    fixed-V integrand bound. The bad-V suppression lives in V's own law.
  - The RS ordering keeps its role in the R-operation (which indicators are inserted where). It has no pricing role.
  - The three-way case split of §3.4 is replaced by one threshold per defect plus a joint moment.
- **What FV does NOT refute:**
  - PLD-desc (forward law, good V only).
  - (SG^fl) (good V only).
  - Branch (iii) read forward, which is Theorem HW.
- **Fix R-1 (for the RLARGE owner; RLARGE not edited):** re-word §3.3's last input bullet and §4.3 step 6 accordingly.

## Priority 5. (M-f), (REL), and whether (REL) is the right residual

### (REL) collapses into the moment hypotheses (reviewer's lemma; PROVEN here at the level of HW's own lemmas, uncounted,
### to be re-checked by the lane)
**Lemma REL-seq.**
*Setup.* For a level-wise cube set S = (S^{(j)})_j, put R_S := ∩_j{every *-component of D_j ∩ S^{(j)} has ≤ n_♯ cubes}.
- R(𝔥) = R_{S(𝔥)} with S^{(j)}(𝔥) = Λ^pre_j(𝔥) ∖ N_1(𝒰_j).
- R(∅) = R_{all}.
- S ⊂ S' implies R_{S'} ⊂ R_S, because a component of D ∩ S lies in a component of D ∩ S'.

*Ordering.* Order the relaxed pairs (j, x) ∉ S(𝔥) by level first, then arbitrarily. Let S_i be S(𝔥) plus the first i
pairs. Then
  Z(∅)/Z(R(𝔥)) = Π_iμ_{R_{S_i}}(R_{S_{i+1}}).

*Bad event at step i.* On R_{S_i} ∖ R_{S_{i+1}}, some *-component of D_j ∩ S^{(j)}_{i+1} has > n_♯ cubes. Every other
component lies in S_i and is small. So that component contains x, and it contains a *-connected 𝒟 ∋ x with |𝒟| = n_♯ + 1,
all of whose cubes are defects.

*Bound.* Apply the union bound over ≤ 6400^{n_♯} shapes ((g3)), then Lemma CH under μ_{R_{S_i}} with the W-bad windows, HÖ,
and the two moments over 𝒟. This gives
  μ_{R_{S_i}}(R_{S_i} ∖ R_{S_{i+1}}) ≤ ε_♯(u_j) := 6400^{n_♯}(C_ℓe^{-au_j})^{n_♯+1}.
- The relaxed set at level j is Σ(Ω^c_{j-1}) ∪ N_1(𝒰_j). It has ≤ |Ω^c_j| + 81|𝒰_j| ≤ 82|Ω^c_j| cubes (H-nest (i)).
- So Z(∅) ≥ Z(R(𝔥))·exp(-164·max_jε_♯(u_j)·Σ_j|Ω^c_j|) once ε_♯ ≤ ½.
- That is **(REL)_B with B = 164 max ε_♯ ≤ 1, indeed B → 0 as g_K → 0**, by Lemma HS'.

*Input needed.* (M-i) and (M-f) for arbitrary cube sets 𝒟, under every intermediate law μ_{R_S} with S ⊇ S(𝔥). Call this
the family 𝔐.
- On cubes that R_S constrains, LI-a fails: R reads their interiors. So (M-i) there is not covered by H4-red and must be
  consumed as stated, as for the collar links (l.271-272).
- Ordering the steps by level means every finer level is fully constrained when level j is relaxed. This is the regime in
  which (M-f) is most natural.

**Consequences.**
- **(REL) is not an independent residual.** Under (ref-a), Theorem HW becomes
  (H-w) ⇐ (F_R) + (AE) + (M-i)^𝔐 + (M-f)^𝔐, with B_0 ≤ 1 + c_LI-terms.
  HIST's B_0 items (a)-(d) belong to the R-operation and effective-density representation and do not occur in ∫W·1_𝔥:
  - top-down ∫K = 1;
  - polymers meeting Ω^c;
  - normalisation mismatch;
  - ℛ^∂ and vacuum/shift near Ω^c.
- **The H-11 fragility moves.** A log(1/g) per cube "in Z(R(𝔥))/Z^sf" (l.365-366) cannot occur in (ref-a) form except
  through the moments.
- **What remains for node A is one torus-wide comparison.** Z(∅) against node A's small-field partition function, for
  (RLF-4). It is a single statement, not a per-history B_0.
- **Fix S-1 (binding for the status line):**
  - l.135-140, l.255, l.364-367 and §10 W2 call (REL) "OPEN [P], node A, (H-w)'s B_0 half unchanged". Replace this with
    "(REL) ⇐ (M-i)^𝔐 + (M-f)^𝔐 (REL-seq); node A owns only Z(∅) ↔ Z^sf (ref-b / RLF-4)".
  - The lane should re-derive REL-seq and adopt it or refute it before the next status change.

### (M-f) (l.252-253, l.345-362): ARGUED status NOT CONFIRMED. Re-label OPEN [P]. Owner incomplete.
- **The reduction to the main term (l.346-352) is correct as an inequality.** The global minimiser's column terms are a
  competitor, and all column terms are assigned to cubes under Q.
  - It is stated with (I_k^E)(a) of HIST §14.1. HIST has since replaced (a) by (a') and then by the analytic main term of
    §25, because of RH3-fix S3-6: the measurable selection is not continuous.
  - It is an upper bound only, so it survives, but it should cite the current form (Fix H-9).
- **The missing half: the large-field tail.**
  - μ_{R(𝔥)} allows returned defects (components ≤ n_♯) at every level ≤ k in Q's column.
  - A single returned bad level-i cube under Q forces F^col_Q ≳ a_bad/24 (TE at level i, with the cone inside the column).
  - The moment E[e^{λu_kF^col_Q}] is therefore finite and g-uniform only if
    μ_R(returned level-i defect at x) ≲ e^{-λ(u_k/u_i)·u_i a_bad/24}.
  - That is a Peierls bound for small finer-level defects, at rate about λ times their energy.
- **The Chernoff loop does not close.** HW's own route proves a rate-θ price from rate-96θ moments at the level below.
  Feeding the price back as a moment needs rate ≥ λ, so θ_{i} ≥ λ_i/24 and λ_{i-1} = 96θ_i give λ_{i-1} ≥ 4λ_i. The admissible
  rate degrades geometrically with depth.
  - [Reviewer's inference; the factor 4 = 96/24 is the loss of Lemma W-bad's 2·24 and Hölder's 2 against the 24-overlap.]
  - So (M-f) is not "UV-dominated small-field" (l.353-356). It contains a non-degrading large-deviation bound on the level-k
    marginal at all finer levels.
  - That is the same kind of content as (H-w) itself, and close to the "(D1-b) at large fields" item HIST §15.4 Remark (3)
    says is still needed.
  - The one-loop argument at l.353-356 addresses only the coherent small-field background.
- **Level 0** (l.360-362) is honestly OPEN even for the plain Wilson measure. This confirms that (M-f) is hard.
- **Fix S-2 (binding, status):** (M-f) is OPEN [P]. Owner: the small-field package for its small-field half; **unowned** for
  its large-field-tail half. Add HW-F5 to §1's failure modes: "rate degradation across levels in a moment ⇒ price ⇒ moment
  loop".

### Circularity (l.373-374): CONFIRMED formally
No hypothesis consumes (H-w) or HIST-sum. In substance, by S-2, (M-f) carries the finer-level large-field content, and HW
should say this in one line.

## Priority 6. K3

### Lemma K3-a (l.381-389): arithmetic CONFIRMED, with fix K-1
- |Ω^c_i ∪ N_1(𝒰_i)| ≤ |Ω^c_i| + 81|𝒰_i| ≤ 82|Ω^c_i|. Correct, since 𝒰_i ⊂ Ω^c_i.
- The factor (2w_* + 1)⁴ inside c_∂ charges each such cube for its extraction-collar neighbours. Correct.
- 82c_∂ ≤ 1 then gives total ≤ Σ_i|Ω^c_i|, i.e. +1 to B_0. Correct.
- The order of constants is B_0 → n_H → n_♯ → w_* → g_0. Non-circular.
- **Fix K-1:** "it suffices for g_K" is short by the R-shift. (F_R) gives only g_i² ≤ g_K²/(1 - Rg_K²) ≤ 2g_K², so require
  82c_∂(g) ≤ 1 for all g² ≤ 2g_K². c_∂ is increasing for g² < a''/3. (P3)'s vacuum correction near Ω^c (≤ C(n_♯)e^{-a''/g²}
  per cube, HIST l.586-588) is not in c_∂. Add it, which changes nothing in kind.

### Lemma K3-b (l.391-405): arithmetic CONFIRMED
- (F_R) upper half gives u_k ≤ u_K + β_+(K - k)log L + R. With m = K - 1 - k, the k-th term is
  ≥ C_1C_2e^{-a(u_K+R)}L^{-aβ_+}L^{(4-aβ_+)m}, exactly as written.
- The sum diverges as K → ∞ at fixed g_K whenever aβ_+ ≤ 4: linearly at equality, geometrically below.
- Dropping polynomial factors ≥ 1 keeps it a lower bound on the bookkeeping bound. Correct.
- It is P4-div's mechanism (HIST l.592-596). The regime claim aβ_+ ≪ 4 holds a fortiori with C_cone ≈ 10¹⁵.
- **Reading (l.403-405):** correct and properly scoped ("about the bound, not the true contribution").

### K3 and HW's own route
- ∫W·1_𝔥 contains no extraction. K3-a and K3-b bear only on representation-based derivations: (ref-b), and the RG-side
  derivation of (M-f) through (I_k^E).
- **Fix H-10:** say this in §7's first paragraph. Otherwise K3-a reads as an input to Theorem HW's B_0, and B_0 = B_2 there
  has no K3 content.

## Priority 7. Check w1

### Procedure and honesty
- **Order.** Criteria mtime is 22:02:25 EDT = 02:02:25 UTC. The script's mtime is 22:03:23 EDT, so the criteria came
  first.
- **Script edit.** The criteria file says it was written after §2-§7 and before the script. The C2 edit before any run is
  disclosed (HW_LOG l.20-21). It replaced a count-by-construction by an enumeration, which is a legitimate pre-run fix.
- **Runs.** The criteria say "One run". Two runs happened (02:49:47, 02:49:55), each with a separate lock acquisition and
  release, and this is disclosed (HW_LOG l.25-28). The script is deterministic, with a fixed seed. The outputs, the
  lock-holding times (22:49:58 EDT) and the record all agree.
- **Log order.** HW_LOG's 02:10 entry sits after the 02:45 entry, so the log is out of order. It is disclosed as
  "(before any run)". Recommended: reorder the entries.
- **One false input claim (header l.17, HW_LOG l.6).** "REVIEW_HIST_S3 is not present" is wrong. Its mtime is 21:38 EDT =
  01:38 UTC, before HW's 01:51 read. As a result HW missed N-4 (fix W-2) and S3-5 (fix H-5). **Fix H-11:** correct the
  sentence.
- **Load-bearing coverage.**
  - A1-A2 test KS (b)-(c), which are fully proven, so they are informational.
  - C1 tests TE (iii)'s 6. C2 tests the 24 plaquettes per corner, which supports HIST's overlap only through HIST's argument.
  - C3 is trivial: the ratio ≤ 81 is the union bound, and it is attained by singletons.
  - The 12/48 constants of W-bad and W-1's θ range are not checked. Nothing numeric could check (M-f).

### Re-run (MANDATORY NUMERIC LOCK; nice 10; BLAS/OMP threads 1; no timeout; python without -I)
- **Lock and conditions.** The lock was acquired at 03:34:15 UTC, after waiting behind other holders, and released once
  (single rmdir, no trap). Load was 3.81 and 42% of memory was free. Exit 0 at 03:34:18 UTC. Wall time 2.76 s, peak RSS 291 MB.
- **Output.** Every result line matches checks/w1_out.txt byte for byte; only the wall-time field was excluded from the
  diff. **OVERALL: PASS** (A1-A4, C1-C3; B I-PASS, max 3.999900).
- **Verdict.** w1 is CONFIRMED as recorded. It is informational: the inequalities it tests are proven analytically (KS) or
  are elementary counts.

## Corrected tally (session 1)

| item | HW claim | verdict |
|---|---|---|
| [HW-1] TE + W-bad | CONDITIONAL ⇐ (AE); level 0, TE (i), (iii) unconditional | **CONFIRMED-WITH-FIX** (W-2: C_cone), counted |
| [HW-2] CH + Theorem HW | CONDITIONAL, implication proven | **CONFIRMED-WITH-FIX** (W-1: θ < 1/96; W-4: e^{aR} in C_H; W-3 for collars), counted |
| [HW-3] FV | CONDITIONAL ⇐ (AE), counted | **CONFIRMED, RECOUNTED as uncounted** (a two-line corollary of TE) |
| [HW-4] KS + KS-chain | PROVEN-HERE, SU(2) | **CONFIRMED**, counted |
| [HW-5] H4-red | CONDITIONAL ⇐ (LI), SU(2) | **CONFIRMED**, counted |
| HR, RX, PF, HS', HW-split, DJ, EQ, HÖ, LI-a | uncounted elementary | CONFIRMED (RX with H-2; HR Remark (1) to [inference], H-1) |
| W-cb | uncounted CONDITIONAL ⇐ (AE), (TC) | CONFIRMED as such (σ_Q level reading unchecked; W-3) |
| K3-a, K3-b | uncounted arithmetic | CONFIRMED (K-1); moot for the (ref-a) route (H-10) |
| (M-f) | ARGUED | **NOT CONFIRMED as ARGUED → OPEN [P]**; large-field-tail half unowned (S-2) |
| (REL) | OPEN [P], node A | **status line WRONG under (ref-a)**: ⇐ (M-i)^𝔐 + (M-f)^𝔐 by REL-seq (S-1); node A keeps only Z(∅) ↔ Z^sf |
| (LI) | OPEN | OPEN, plausible; wording H-8 |
| (KS-N) | HYPOTHESIS | HYPOTHESIS (scalar polar part numerically consistent, c_3 → 4) |

**Counted: 4 (was 5).** Targets: W1 MET; W2 MET as CONDITIONAL, with the residual re-identified (S-1, S-2); W3 MET (K-1).

## Binding fixes (next lane-H session)

1. **W-1** Theorem HW: θ ∈ (0, 1/96), more precisely 96θ(1 + O(Rg²)) < 1. State why: (M-f)_λ needs λ < 1.
2. **W-2** C'_cl := C_cone (HIST RH3-fix N-4) at l.162, 176, 191, 232. Record a_bad's size (≈ ε_1²·10⁻¹⁶/N with h7's
   C_cone).
3. **W-3** Collar extension: θ divided by the window multiplicity (≤ 82), or the multiplicity stated in the hypothesis.
4. **W-4** HIST-sum consequence under (F_R): C_ℓ → C_ℓe^{aR} (RLARGE v2-F).
5. **S-1** (REL) status: replace "OPEN [P], node A, B_0 list" by the REL-seq reduction (adopt after re-derivation). Node A
   keeps the single comparison Z(∅) ↔ Z^sf.
6. **S-2** (M-f): OPEN [P]; split it into its small-field half (package) and its large-field-tail half (unowned). Add HW-F5,
   rate degradation.
7. **H-2** RX: (ii) and (iii) need history-independent D_j.
8. **H-6** PLD-desc's law is forward μ^+ (good V only); FV does not refute it.
9. **H-8** (LI) is a form of H-4 in the indicator representation, not "the precise form".
10. **H-11** Correct "REVIEW_HIST_S3 is not present".
11. **K-1** K3-a: require 82c_∂(g) ≤ 1 for all g² ≤ 2g_K², and include (P3)'s vacuum term.
Recommended: H-1 (HR Remark (1) to [inference] or delete it), H-3 (PF counterexample), H-4 (stray bracket), H-5 (DJ
answers S3-5), H-7 (KS (d) carries r), H-9 ((I_k^E) current form), H-10 (K3 moot for ref-a), FV recounted.
For the RLARGE owner (not edited): **R-1**, FV's consequence for §3.3's last bullet and §4.3 step 6.

## Strategic verdict

- **What HW achieved.** HW turned K5 from a bookkeeping conflict into one precise inequality, and that conversion is
  correct.
  - The exact indicator representation, the relaxed law, Chernoff under one law, and the threshold given by the tower
    energy together replace RS-joint, PLD-desc, the case split, the greedy factors and E10 for bad cubes.
  - KS gives the mismatch moments exactly and sharply for SU(2), and H4-red reduces their in-history form to (LI).
  - FV shows the fixed-coarse-field reading of branch (iii) is false. RLARGE v2 §3 should be re-worded around joint
    moments.
- **(REL) is the wrong residual.** Under (ref-a) it reduces by REL-seq to the same moment hypotheses over a family of
  relaxed laws, with B → 0. It is neither paper-scale nor node A's. Node A's remaining interface is a single torus-wide
  comparison of Z(∅) with its small-field partition function.
- **The real residual is (M-f)^𝔐** (with (AE) and (M-i)^𝔐/(LI)). It is not a small-field object. Its exponential moment
  contains the large-deviation tail of returned defects at every finer level, and the moment → price → moment loop
  degrades by a factor ≥ 4 per level, so it cannot be closed inside HW's own machinery.
- **Recommended next targets, in order:**
  1. Re-derive or refute REL-seq.
  2. Prove (M-f) at level 0 for the plain Wilson measure under μ_{R_S} at some fixed λ < 1. HW marks this OPEN even without
     conditioning. It is the cleanest test of whether (M-f) is reachable.
  3. Look for a non-degrading moment source: a direct upper bound on the level-k marginal density of the form
     C^{dof}u_k^{dof/2}e^{-(1-δ)u_kF^col}, which is the large-field (D1-b)-type bound. Avoid the Chernoff loop.
  4. Only then attempt (LI).
