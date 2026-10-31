# REVIEW_BFT_B_S8: hostile review of BFT lane B session 8 (BFT_B.md [RBB7-fix] edits, §24-§26; checks bb8t, bb8n, bb8w, bb8n_defect), with the cross-lane (GE-T) adjudication against BFT_A §36-§40

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md or the checks. This file is the only repository file I
edited. No commits, PRs or pushes.

**Inputs** (read 2026-10-28, about 11:30-11:50 UTC; `TZ=UTC stat`):
- BFT_B.md: born 10:22:44, modified 11:28:44, 409782 B.
- BFT_B_LOG.md: modified 11:29:03.
- BFT_A.md: modified 11:39:34, 351969 B (lane A session 8 finished).
- checks/bb8*_criteria.md: born = modified 11:17:28.
- Scripts: 11:18:52-11:20:37, plus bb8n_defect 11:25:00.
- Outputs: 11:21:05-11:21:12, plus bb8n_defect 11:25:12-11:25:13.

**What I read:**
- BFT_B: §24-§26 and FOR OTHER FILES (l.3260-3570) in full; every [RBB7-fix] tag in context; 22.2 (l.2989-3011).
- BFT_B_LOG: session 8 (l.372-420).
- REVIEW_BFT_B_S7 (all) and REVIEW_BFT_A_S7 Parts 1-4.
- BFT_A: §36 (statements), §38 (proofs), §39 (ba8), §40 (outcome); checks/ba8_out_E2.txt.
- REVIEW_S22: the BFT-0..5 definitions.
- Line by line: checks bb8t_get.py, bb8n_lip.py, bb8n_defect.py and bb7n_chain.py's `refine`.

**Re-runs and probes.** All of them ran under the numeric lock in **one acquisition, 11:40:58-11:44:22 UTC** (load1 2.39;
memory free 43% before, 42% after). Runner: scratchpad `revBB8/run_bb8rev.sh`.
- It waits with `until mkdir …/locks/numeric`, then waits for load1 < 8.
- Environment: nice 10; thread variables 1; PYTHONDONTWRITEBYTECODE=1; `/usr/bin/time -l`; python3 without -I; no
  `timeout`; no trap; one `rmdir`.
- Afterwards: the lock directory is empty, `pgrep` finds no process, and there is no `checks/__pycache__`.

The record is at the end.

---

## Bottom line

- **Provenance: CONSISTENT** (Part A). There are two cosmetic notes. One is a birth-time discrepancy against the S7 review's
  record; byte accounting is unaffected.
- **[RBB7-fix]: all of RS7-1..RS7-8 applied, with the content asked for.** One stale header remains (RS8-1).
- **Lemma GE-T (a)-(f): CONFIRMED.** The sharper bulk bound is ARGUED, as marked.
  - The exact tent sum Σ|d ev χ^5_X| = 2d(n/s)^{d-1} is re-derived. A reviewer probe confirms it in d = 2, 3, 4 and for
    L = 3, 5 to 1.3e-15.
  - **Adequacy for lane A: NOT ADEQUATE for lane A's named hypothesis (GE-T) of BFT_A §36.0.** That is a different and
    strictly stronger statement, and it is expected FALSE (Cross-lane section).
  - GE-T is adequate, and was what REVIEW_BFT_A_S7 Part 4 literally asked for, as an operator lemma. Its exact root-charge
    count is the dual of lane A's Proposition TE tents. It fixes TE's size constant to exactly 8 = 2d.
  - The sentence "the correction is of the same order as the target" (l.3415-3417) compares the sup of a source with the
    size of a response. It must be reworded (RS8-2).
- **Theorem N2-loc: CONFIRMED** (constants not evaluated).
  - (c), the root-row defect ≡ 0, is CONFIRMED exactly, both by the proof and by reading the code.
  - A reviewer non-vacuity probe gives: root-row interior links |log| ≤ 1.3e-18, against off-row links 2.5e-2 / 3.2e-3 /
    3.8e-4 at depths 1-3.
- **Theorem N1-loc: CONFIRMED as an implication of LES-div.** One last-scale constant is off by a factor 2, which is harmless
  (RS8-6).
- **Corollary CL-iv: CONFIRMED as an implication** for the C^{1,α} terms. The residual term is at Cg-NL's status, as stated.
  - The exact row recursion at levels j ≥ 1 is the real gain of (c).
- **bb8n's L-c FAIL and the post-hoc probe: HONEST.**
  - The criterion was not retuned, and bb8n.out remains the record.
  - The probe's "prediction" was written after the 0.0000 had been seen. It carries no pre-registration weight. It is a
    resolution check that the 0.0000 was round-off (1e-18-9e-17) and not a value hidden by 4-decimal printing.
  - Theorem N2-loc (c) rests on the proof, which I re-derived.
- **Re-runs:** bb8t, bb8n, bb8w and bb8n_defect are **identical to the stored outputs apart from the timing lines**,
  including the L-c FAIL.
- **Cross-lane:** lane A's "funnel spikes" and lane B's root charges are **different objects**.
  - The spikes sit at roots of top level < k and come from Q's funnel.
  - The root charges sit at level-k roots and come from Λ's χ-interpolation; they are the dual of lane A's tents.
  - The two lanes do **not** contradict each other. They proved and refuted two different statements that share one name.
  - I **concur, at the ARGUED level, that (PW-i)_{Γ_E} and lane A's (GE-T) fail for large k.** I add an exact identity
    showing that S_E is in the level-0-Coulomb class at non-level-k roots, so the S_C0 stand-in is representative (C.3).
  - **Recommendation: one slice (S_E) for the program. Do not adopt the top-anchored representative as a second slice now.**
    Details are in the Cross-lane section.
- **BFT-5: recommend lane B as owner**, with a composite-co-closed statement that does not depend on the slice decision
  (Part F).

---

# PART A: provenance

**Byte accounting.** Measured with `sed -n | wc -c`.

| quantity | measured | expected | result |
|---|---|---|---|
| "# Session 8" header (30 B, l.3260-3262) + §24 (l.3263-3349, 10151 B) | 10181 B | 10181 B, the logged growth 375969 − 365788 at 11:12:37 | exact |
| prefix l.1-3260 | 372007 B | 365788 (session-7 state) + 6218 (Step-1 growth 382187 − 375969) | +1 B, the usual line boundary |
| l.1-3349 | 382188 B | 382187 B after Step 1 | +1 B, line boundary |
| §25 + §26 | 21434 + 6160 = 27594 B | 409782 − 382188 | exact |

So every Step-1 edit lies before §24, §24 is byte-for-byte the size it had when appended, and §25-§26 are pure appends.

**Order:** §24 (11:12:37) < Step 1 (11:13-11:15:04) < criteria (11:17:28) < scripts < runs (11:21:05-12) < bb8n_defect
criteria and script (11:25:00) < its run < §25 (11:27:31) < one in-place §25.4 constant fix (11:27:56, logged) < §26 (11:28:30,
plus a logged clean-up at 11:28:44). This matches the log.

**Disclosure.** §24's header says, honestly, that lane A's request did not yet exist (BFT_A.md mod 10:26:38 at 11:10). That
is confirmed: lane A's §36, which carries its own (GE-T), was appended at 11:23:19, after lane B's §24 and before §25.

**Birth-time note (informational).** BFT_B.md is now `born 10:22:44`. REVIEW_BFT_B_S7 recorded `born 09:21:46` at ≈10:40.
- A file's birth time cannot move later without the file being replaced.
- So either S7 misrecorded it, or the file was rewritten whole at 10:22:44 (session 7 Step 1).
- Byte accounting is unaffected. Future sessions should log `born` together with `mod` at their first stat (cosmetic).

**[RBB7-fix] audit** (26 tag strings; 25 in the text plus the §26 table).

| fix | lines | status |
|---|---|---|
| RS7-1 | 1901, 1975, 2475, 2667, 2712, 2774 | planned-at-the-time notes appended, wording kept: CONFIRMED |
| RS7-2 | 2966, 2985, 2986, 3224 (and the 2665 tag) | e^{20m} restored, correction withdrawn, q-fold lift ARGUED-routine: CONFIRMED |
| RS7-3 | 2995 | Metzler replacement written out correctly (ghost values re-checked); 2896 annotated: CONFIRMED. Cosmetic: the 22.2 heading still reads "IMPORTED-AND-REVERIFIED" (RS8-1) |
| RS7-4 | 3124 | CONFIRMED |
| RS7-5 | 2781, 3163, 3246 | pointing to §24.2, which existed before Step 1: CONFIRMED |
| RS7-6 | 1638, 3138 | CONFIRMED |
| RS7-7 | 3149 | CONFIRMED |
| RS7-8 | 1638 cocycle; 3088; 3205/3207/3209; 3253; the dated note in checks/bb7k_criteria.md (logged 11:15:11) | CONFIRMED |

---

# PART B: Lemma GE-T (§24.1; proof 25.1, l.3362-3417)

**(a) Representation: CONFIRMED.**
- The first variation gives d*_X(x_0 + d_Xλ) = 0, and the projector 1 − 1δ_c^T fixes the constant.
- ⟨ψ, λ⟩ = −⟨d_XG_Xρ, x_0⟩ with ρ neutral. Transposing gives (λ^E_X)^Tψ = −d_XG_Xρ.
- The reflection to 𝕋_R of side 2S (y ↦ 2S − 1 − y): box-boundary neighbours are mirror images, so u|_box solves the
  Neumann problem.
- The code's `fold_idx` implements exactly this map. bb8t T0 and T4 give an independent CG check of adjointness (1.7e-14).

**(b) Locality (range 3): CONFIRMED.**

**(c) ℓ¹ bound: CONFIRMED.**
- 16 images per box link; crossing links carry du = 0.
- Lemma N1G per direction gives Σ_{𝕋_R}|du_μ| ≤ 16||ρ||_1·M/4. So the box sum is ≤ M_n||ρ||_1 ≤ 2M_n||ψ||_1, and summing
  over X gives 2M_n||φ||_1 = 4(4n + 1)||φ||_1.
- The scalar kernel acts componentwise, so there is no loss for su(N)-valued fields.
- Precision (cosmetic, RS8-4): N1G's transverse-sum + monotonicity proof is d-independent. (c) and (e) hold in every d with
  2^d images. Restricting to d = 4 is harmless.

**(d) Dual sup-data bound: CONFIRMED.** 2M_n/n = 16 + 4/n ≤ 20 in coarse units. This is a clean, useful sup-only bound for Λ.

**(e) ℓ^∞ bound: CONFIRMED.**
- Monotonicity along coordinate lines follows from the factorised kernel and REVIEW_BFT_B_S7 B.2.
- Then |∇_μG(y)| ≤ max(G(0) − G(·)) ≤ 1.71: the Fourier sum and the shell count were re-done, and at M = 4 it is
  1.5 + 0.21 = 1.71.
- Cosmetic (RS8-5): the telescoping sum at l.3387 should run from t = y_μ, not from t = 0. The bound is unchanged.
- The overlap count 5^4 is correct.
- The measured C_∞ = (1 − M^{-4})/8 is exact: −ΔG(0) = 2d(G(0) − G(e_1)) = 1 − M^{-4} by symmetry. It could be stated as a
  remark.

**(f) Root charges: CONFIRMED, and the constant is exact.**
- Q_X(D(j)) = ⟨d ev χ^5_X, j⟩, where d ev χ^5_X is the level-l gradient of the sampled bump.
- In each coordinate the 1D sum Σ_{y∈sℤ}σ_5(|y|/n) = n/s is exact. Pair y with n − y using σ_5(t) + σ_5(1 − t) = 1; the
  y = 0 term is 1 and there are n/s − 1 paired terms.
- The total variation of σ_5(|·|/n) is exactly 2.
- So Σ = 2d(n/s)^{d-1}. In d = 4 this gives |Q_X| ≤ 8L^{3(k−l)}||j||_∞, sharp for j = sign(d ev χ^5_X).
- Reviewer probe R2: ratio = 1 to 1.3e-15 for d = 2, 3, 4, L = 3, 5, k ≤ 3 and all l < k.
- **The same number is lane A's tent size.** ||(Ξχ^5_X)_l||_1 = ||d ev^{(l)}χ^5_X||_1 = 8L^{3(k−l)} exactly. BFT_A 38.4
  writes this as "≈ 8L^{3(k−l)}" from a Riemann-sum estimate, and it should cite (f) for the exact value.

**Sharper bulk bound: ARGUED, as marked.** It needs BA-7's pointwise decay. The arithmetic n/s⁴ = L^{k−4l} ≤ L^{3(k−l)} is
right.

**Remark GE-T' (log n): CONFIRMED as ARGUED.** bb8t C2 shows the log growth. The row of P_grad is an adjacent dipole field.

**The reading paragraph l.3411-3417 (RS8-2, binding).**
- "In the dual form of (PW-i) … the correction is therefore of the same order as the target." This compares the **sup of a
  level-0 source** (own units) with the **sup of a response** f = n²⟨·, Y⟩. These are different quantities.
- By (PW-i) itself at l = 0, a level-0 source of sup V can produce a response up to C_PL^{3k}V. A source of size L^{3(k−l)}
  is therefore not "of the order of the target" in any operational sense.
- The correct and useful content is this. Q_X = ⟨j, (Ξχ^5_X)_l⟩ is the pairing of j with the level-l trace of the tent
  Ξχ^5_X. So the root-charge part of S^E_0(j) is exactly the dual of lane A's Proposition TE. (PW-i)_{Γ_E} at level l
  requires every level-k-root tent coefficient a to obey 8|a|L^{3(k−l)} ≲ C_PL^{k−3l}, i.e. |a| ≲ C_PL^{−2k}/8.
- So the root charges do **not** add a new requirement to the dual target: the identity 𝒟_l = ||(Π_EY)_l||_1, BFT_A 38.1,
  is exact. But they **are** one of the two mechanisms by which (PW-i)_{Γ_E} fails (Cross-lane section).
- Replace l.3415-3417 (in a later dated note; §25 is not to be rewritten) by the tent reading above.

**Is the open ℓ¹ comparison of S_E with the 𝒩-optimal representative needed?** **No.**
- Lane A's route (BFT_A §36.1 and §38: Lemma DF + Theorem PW-cc + its (GE-T)) never uses a general comparison.
  - PW-cc bounds co-closed pairings through 𝒩_l, which is representative-independent.
  - The non-co-closed part is (GE-T)'s job.
- Remark GE-T' shows that the comparison is unavailable in operator form at k-uniform level (1 + log n = O(k)).
- Its structured special case is lane A's (GE-T), which is expected false.
- Remove "S_E vs 𝒩-optimal in ℓ¹" from the open set (RS8-8).

**Verdict on GE-T for lane A.**
- As an operator lemma (what REVIEW_BFT_A_S7 Part 4 asked, and what lane B could state before lane A's request existed):
  **CONFIRMED and correct.**
- As lane A's named (GE-T) (BFT_A §36.0: ||(Π_Eu⃗^♮)_l||_1 ≤ C_GTL^{−3l}R): **NOT ADEQUATE.** GE-T does not imply it.
  Plugging (c), (e) or (f) into the pairing loses factors of n up to n³. Moreover the hypothesis is expected false, so no
  correct lemma on Γ_E^T can supply it.
- RS8-3 (binding): rename lane B's lemma (for example **Lemma ΓT-op**) to end the name collision with lane A's hypothesis.

---

# PART C: Theorem N2-loc, Theorem N1-loc, Corollary CL-iv

## C.1 Theorem N2-loc (25.3): CONFIRMED (constants not evaluated)

**Gauge invariance of the three quantities: correct** (AX-cov; each one rotates by Ad at one point).

**(a): CONFIRMED.** The telescope is pointwise with finite reach. The nested regions shrink by Σ_jLρ_{j+1}(r_s + C_r + 2),
which is geometric.

**(b): CONFIRMED.**
- *The one-frame identity.* Using τ'(p', ·) = τ(p, p')^{-1}τ(p, ·) gives Ad_{τ(p,p')}Ad_{τ'(p',p'')} = Ad_{τ(p,p'')}. So both
  telescopes carry the same β_{j'}. The identity of 22.5 uses no property of τ beyond τ(q, q) = 1. That is correct (I
  re-checked the increment formula).
- *Case ρ_{j'+1} ≥ δ.* ||W(p, ·) − W(p', ·)||_1 ≤ Λ_2'δ/ρ_{j'} = Λ_2'Lδ/ρ_{j'+1}, times |β| = O(ρ_{j'+1}²f²), gives
  O(δρ_{j'+1}f²). Correct.
- *Case ρ_{j'+1} < δ.* Two axial paths in a fixed coordinate order whose start and end points lie within C_rρ_{j'+1} of each
  other bound a union of d ladders of width O(ρ_{j'+1}) and length ≤ δ + O(ρ), plus corner pieces. So the area is
  ≤ C'ρ_{j'+1}δ. Re-checked.
  - The level-(j'+1) legs are converted to level-j' root rows exactly, by (c).
  - The lasso needs area·f ≤ ½, which holds since area ≤ C' and f ≤ C_N'ε.
- The sum over j' is geometric. So [F_j]_{Lip} ≤ (Λ_2'f_k + C_2f²) is k-uniform. Correct.

**(c) d_j ≡ 0: CONFIRMED exactly.**
- *Proof.* In X's axial frame, a coarse site X + te_μ is reached along e_μ only (fixed order). So A^X = 0 on the line's
  coarse μ-links.
  - The fine row at transverse offset 0 reads only that line, because DD8 is interpolatory: the transverse weights at offset 0
    are δ.
  - μ(A^X) vanishes on the row: the interpolatory Φ_0 reads only line sites, whose tree paths carry A^X = 0.
  - So the interior row links are 1 and the face link is Z_{j+1}(X, X').
- *Code (bb7n_chain.py `refine`).* W0[0] is the Lagrange weight at t = 0, i.e. δ_{q,0}. A0[(l, 0)] = log(g Z0 g^{-1}) = 0
  along the axis-0 tree. The face-link μ for r1 = 0 uses W0[0], so ψ = 0 there. The same holds on the axis-1 row.
- *Reviewer probe R1* (non-vacuity). Root-row interior links have own |log| ≤ 1.3e-18. Off-row interior x-links carry
  2.5e-2, 3.2e-3 and 3.8e-4 at m = 1, 2, 3. So the zero is structural, not a property of a trivial field.
- *Note.* bb7n/bb8n use roots at block **corners** (fine site 3X); §15.0 uses block centres. The mechanism needs only
  "root = subdivision node", so the theorem holds in both conventions. Say so in §26 (cosmetic).
- *Scope of the sharpening.* It holds for straight root rows, nested on the same line. With nested roots it gives the exact
  identity "level-0 root line c_X → c_{X'} = Z_k(X, X')". This is what upgrades CL-clu's O(ε²) and 22.5's O(σ²) to 0.
  The other factors of CL-clu (g_X, g_Y, the conjugation) are unchanged.

**(d): CONFIRMED.**

## C.2 Theorem N1-loc (25.4): CONFIRMED as an implication of LES-div

**The equations.**
- NF-crit gives d*_Xw = 0 exactly. The gradient of ½d(1, ·)² is the geodesic log, so the box normal-form condition is linear
  in w.
- Divergence form: g = ±dw with h = 0.
- dw = F^N − B. The BCH bounds and Lip(B^c) ≤ C_3'η|∇^cw^c| are correct, including the n-counting.
- Lip(F^N) ≤ [F_0]_{Lip} + 8ηf_0, using |log τ^N| ≤ 4δη.

**The one-scale estimate** has the homogeneity of LES-div. The B-term costs R_c·Lip, hence the factor A_1ηrM(r/2).

**The distance iteration.**
- The sum is ≤ 16A_0(4η + B). Re-done: Σ2^{i−i(i−1)/2} ≈ 6.3 and Σ2^{−i(i−1)/2} ≈ 2.64.
- **RS8-6 (cosmetic).** With the stopping rule "iterate while nr_{i+1} ≥ 32", the last scale satisfies
  n < 64·2^m/r_0 ≤ 256·2^m, not 32·2^m/r_0. The last term is then ≤ 1024η, not 512η. Constants only.

**The small-n branch** and the interior Hölder from Campanato telescoping with margin ¼ are correct.

**Reliance.** The theorem uses LES-div "in the form of 16.2 Step 3/5". I did not re-open PROOF [S15].

**bb8w:** d = 2, SU(2), one profile. The interior proxies are flat in n (W1) and the boundary layer grows. Supportive,
informational.

## C.3 Corollary CL-iv (25.5): CONFIRMED as an implication (C^{1,α} terms)

**Level 0.**
- The transition relation κ_X(y') = e^{−w_X}κ_X(y)e^{w_*} is re-derived from U^{g}(b) = e^{w(b)}.
- ϕ_n's expansion, uniform in n, is correct.
- The C^{2,α} of k comes from bootstrapping ∇k = ϕ(k, w_X, w_*).
- 𝔪^geo weights: σ_5 is C^{2,1} with σ_5', σ_5'' vanishing at 0 and 1, so it is C^{2,1} across faces.
- Z^off_0 = N_*^K and log Z^off_0 = log(Ke^{w_*}K'^{-1}). Correct.

**Levels j ≥ 1: CONFIRMED, and this is the real gain of (c).**
- Z^off_{j+1}(X, X') = the row product of Z^off_j, exactly.
- In level-(j+1) coarse units, Σ_iv_j(b_i) is an average of L translates. Sup, gradient and Hölder do not increase.
- β_j = O(L²ρ_j²|v||∇v|). The inverse estimate gives ρ_j^{1−α}.
- The product Π(1 + Cρ_j^{1−α}ε) is bounded, so C_1ε is k-uniform.

**Disclosed and accepted:** the chain-rule constants are not written out; the residual term is at Cg-NL's status; the
non-residual g_Z components at θ > 0 are OPEN; (v) is ARGUED.

---

# PART D: checks

**bb8t:** the code matches its criteria (read in full).
- T4 is a genuinely independent path (CG solve of the pinned normal equation).
- T5 is the combinatorial identity.
- C1 confirms that the pinned compensation sup grows like n^d. Reviewer probe R3 shows the same thing: δ_b at a level-k
  root has ||dΛ||_1/||u||_1 = 10.1, 30.4, 67.8 for n = 2, 3, 4, which is ∝ n².
- Re-run identical apart from timing; 5.9 s, 564 MB.

**bb8n:** the code matches its criteria.
- L-a and L-b PASS. The control C PASS has the correct 1/|p − p'| signature.
- L-c FAILS as recorded.
- The VERDICT line prints "(L-a, L-b, L-c, C)", listing all tests rather than the failing one (cosmetic; §26 states it
  correctly).
- Re-run identical apart from timing; 1.8 s, 190 MB.

**bb8n_defect:** an informational probe with a post-hoc prediction, disclosed as such. Identical on re-run; 1.1 s.
- **Honesty verdict: HONEST.**
  - The FAIL is kept.
  - The criteria file states it was written after bb8n ran.
  - §25's correction (3) carries the proof.
  - The theorem's pre-stated bound (|d_j| ≤ C_dρ⁴ε²) is true with C_d = 0. Only the criterion's "second-order scaling"
    clause was wrong.

**bb8w:** identical on re-run; 0.5 s, 83 MB.

---

# Cross-lane GE-T adjudication

**Objects.**
- **Lane B, Lemma GE-T (§24.1, PROVEN).** Operator bounds on Γ_E^T: ℓ¹ ≤ 2M_n, locality 3, exact divergence
  d*Γ_E^TD(j) = −D(j) + Σ_XQ_Xδ_{c_X}, |Q_X| ≤ 8L^{3(k−l)}||j||_∞ (exact sum), sup ≤ C(n + L^{3(k−l)})||j||_∞.
- **Lane A, hypothesis (GE-T) (BFT_A §36.0, with §38 precision 2).** For co-closed u with |u(b)| ≤ (1 + |b − z_0|)^{−3},
  support within R of z_0 (1 ≤ R ≤ Tn/2):
  - **||(Π_Eu⃗^♮)_l||_1 ≤ C_GTL^{−3l}R** for every l < k;
  - dual form: |⟨S^E_0(j), u⃗^♮⟩| ≤ C_GTL^{−3l}R||j||_∞.

**Reviewer decomposition (exact).** It uses 16.1 (a) (Λ(x_0 + dμ) = Λ(x_0) − μ + I_χμ), BL-2 (b)
(Q^{(0→l)} = Q_str^{(0→l)} − d∘h^{(0→l)}) and Proposition TE:

  (Π_Eu⃗^♮)_l = Q_str^{(0→l)}u  −  dΦ_l(u)  +  d ev^{(l)}Λ(u)  +  d ev^{(l)}I_χψ_u,   ψ_u = h^{(0→k)}u.

The four terms behave as follows.
1. **Straight term.** ||Q_str^{(0→l)}u||_1 ≤ L^{−3l}||u||_1 ≲ L^{−3l}R (||Q_str||_{1→1} = ||Q_str^T||_{∞→∞} ≤ L^{−3}).
   Harmless.
2. **Funnel term −dΦ_l(u).** A point value Φ_l(u)(Z) at a root Z of top level l(Z) costs ≈ 8|Φ_l(Z)| per level, which is
   level-independent. This is lane A's spike. Lane B's lemma plays no part in it.
3. **Bulk Λ(u).** For co-closed u, λ_X(u) is the box-Neumann potential of the **boundary flux** of u: d*_Xu vanishes at
   interior sites. It is discrete-harmonic on N_X ⊃ supp χ^5_X, at distance n from the charges. So it is smooth on scale n,
   and level-l sampling loses nothing (ARGUED, reviewer).
   - Reviewer probe R3 (d = 4, abelian, coarse side 5): ||dΛ(u)||_1/||u||_1 for u = (1 − P_grad)δ_b is **0.078, 0.133, 0.147**
     (b at a root) and **0.061, 0.091, 0.097** (generic) for n = 2, 3, 4. This is small and saturating.
   - Against it, δ_b gives 5.6 → 7.9 (generic, log n) and 10 → 68 (root, n²).
   - So the bulk part of (GE-T) is not the obstruction.
4. **Tents d ev^{(l)}I_χψ_u.** Since Σχ_X = 1, these depend only on the level-k differences of ψ_u.
   - For a ψ_u concentrated at one root X, the size is 8|ψ_u(X)|L^{3(k−l)} **exactly**, by lane B's (f).
   - Precision for lane A (P8-a, cosmetic): 38.8's "(GE-T) needs |ψ_u(X)| ≲ C_GTL^{c−2k}" should read "needs the level-k
     differences of ψ_u near X to be ≲ …". The two coincide for the single-root spike that lane A identifies.

## 1. Are lane A's "funnel spikes" exactly lane B's root charges Q_Xδ_{c_X}?

**No.** There are two distinct mechanisms.

**Funnel spikes** (term 2):
- They sit at roots Z with 1 ≤ l(Z) < k.
- They come from the funnel h of lane A's root-covariant S4' contour average Q (Proposition RF, exact).
- They are nonzero only at asymmetric placements of p next to Z (ba8 E3: ε = −0.00262 at offset (1,0,0,0), and 0 at the
  four symmetric offsets).

**Root charges / tents** (term 4):
- They sit at level-k roots only.
- They come from Λ's χ^5-interpolation of the pinned level-k gauge values (Proposition TE, exact).
- Lane B's Q_X = ⟨j, (Ξχ^5_X)_l⟩ is exactly their dual. With lane B's exact count, lane A's ≈ 8L^{3(k−l)} becomes the
  identity ||(Ξχ^5_X)_l||_1 = 8L^{3(k−l)}.

So the **tents ↔ root charges** correspondence is exact, and the **spikes are a separate, Q-specific effect**.

## 2. Is lane B's proven form, with the root-charge correction, sufficient for PW-E? Is PW-E false as stated?

**Not sufficient.**
- Lane A's (GE-T) is strictly stronger than, and not implied by, lane B's GE-T.
- Using GE-T's operator bounds in the pairing ⟨Γ_E^TD(j), u⃗^♮_0⟩ loses n up to n³.
- Terms 2 and 4 above are real and are not controlled by any Γ_E^T operator norm.

**PW-E is not false as stated.** It is an implication. I checked its structure:
- the data split Z' = Z'' + Ξ_fullψ̃ (Theorem Y step 2);
- 𝒮_l's 𝒢_0-invariance (Lemma RC's Λ(y + Ξν) = Λ(y) − ν);
- the EP-rec sup terms;
- the periodisation for T ≤ 4.

I did not re-derive Case A's constants.

Since its hypothesis is expected false for S_E, **PW-E is vacuous for Γ_E**. Its value is as a template: the same bootstrap
with Π_E replaced by any 𝒢_0-invariant linear representative map P satisfies (GE-T)_P ⇒ (PW-i)_P.

**There is no contradiction between the lanes.** "GE-T PROVEN" (lane B) and "(GE-T) expected FALSE" (lane A) are statements
about two different objects that share one name (RS8-3).

## 3. Is the spike artefact-free in S_E itself, as opposed to the Coulomb stand-in S_C0?

**Intermediate roots: yes (reviewer ARGUED, with an exact identity).**

For every chain x and every level-0 site z that is **not** a level-k root, take Leibniz on Λ = Σ_Xχ^5_Xλ_X with
−Δ_Xλ_X = −d*_Xx_0 on the interior of Ñ_X ⊃ N_X ∋ z, and Σχ_X = 1:

  d*(Π_Ex)_0(z) = R_x(z),   R_x := Σ_X[(λ_X − λ_{X_0})Δχ^5_X − 2∇χ^5_X·∇(λ_X − λ_{X_0})] (shift-corrected).

R_x depends on x only through the differences λ_X − λ_{X'}. These are discrete-harmonic on the box overlaps away from the
level-k roots, where the pins sit. So R_x has **no point divergence**: it is O(n^{−1}) and smooth.

Hence:
- S_E belongs to the same class as S_C0 (level-0 field divergence-free at non-level-k sites, up to a smooth term).
- The gauge ξ connecting S_C0 to S_E solves Δ_0ξ = R off the level-k roots, with ξ = 0 at them. It is smooth near Z.
- It changes sp_l(Z) by O(s²·sup|R|) → 0.
- The orbit content is visible in the three ba8 representatives at offset (1,0,0,0), k = 3 (own units):
  - CG (−0.0017, +0.0009, +0.0008);
  - S_C0 (0, +0.0032, +0.0028);
  - C0# (−0.0028, ≈0, 0).

  The total spike ≈ 0.003 is a property of the orbit. A slice chooses only **where** it sits. Any level-0-Coulomb slice,
  S_E included, must put it on levels ≥ 1.

So the S_C0 measurement transfers to S_E up to o(1). The spike is **not an artefact of the stand-in**.

**Level-k roots: the tent identity is exact (TE plus (f)).** Its size needs the level-0 spike a at the level-k root to be
k-independent. It was measured only at k = 2 (a = −0.0022). k-independence is structural: a is set by the local fine-scale
field of Y^p, which is k-independent. But it is not measured. ARGUED.

**Verdict.** I **concur, at the ARGUED level, that (PW-i)_{Γ_E} and lane A's (GE-T) fail for large k.**
- The onset is l > k/3 + O(1) (spikes) and an n² factor (tents).
- At k ≤ 3 the effect is only a factor ≈ 2 (ba8: 0.866 against 0.445).
- **Unaffected:** Theorem PW-cc, every composite-co-closed response, gauge-invariant outputs, and responses at critical
  points (Lemma CD (i)).
- **Scope of the evidence:** abelian, L = 3, κ ≡ 1, k ≤ 3, one asymmetric offset family, S_E not computed directly.
- A direct S_E run (T = 5, k = 2, fine side 45 in d = 4) is the one check that would upgrade this verdict. It is above the
  per-job budget. It is worth scheduling as a single long locked job if the lead wants proof-grade evidence.

## 4. Should the program adopt the top-anchored representative? One slice or two

**Recommendation: ONE gauge fixing, S_E, for the program.** Do **not** adopt the top-anchored representative as a second
slice for the dynamics now. Reasons:

1. **The tension is structural, not a defect of S_E.**
   - 𝔐^∇ for configurations needs smooth placement of the root gauge values: tents at level-k roots, and a Coulomb-smooth
     level 0 at the other roots.
   - (PW-ℓ¹) for Y^p needs point-like placement: spikes at level 0, points at level-k roots.
   - Π^♯ = Π_E + Ξσ∘Π_E moves Φ_{l(Z)} of a smooth configuration to a level-0 point gradient of coarse size ≈ L^{2l(Z)}η,
     which 𝔐^∇ forbids (BFT_A 38.8).
   - At level-k roots, removing the tents would need point gauges there, which conflicts with the configurations in the same
     way.
   - No single linear slice is known to serve both.
2. **A two-slice program adds a wall.** Each RG step would need a gauge transfer between slices with (CovLift)-compatible
   bounds (C^{1,α} in frames, translation covariance, locality). BFT-5's (G♯) for "the composite slice Hessian" would then
   have to be proven in both slices.
3. **The top-anchored representative is already usable, with no decision needed, for slice-independent quantities.**
   - Pairings with composite-co-closed sources are representative-independent, so any element of the orbit may be used to
     estimate them, including C0#. This applies at critical points and to Proposition SR's scope (BFT_A 38.8).
   - This is an evaluation device, not a gauge fixing.
4. **Route (i), to pursue first (owner: lane A).**
   - Reformulate (NC-Γ) as **(NC-Γ)_cc**: k-uniform Γ_E-response bounds for composite-co-closed sources, plus an explicit
     remainder for the non-co-closed part of the contraction's source.
   - That part is (K_x − Ξ)^T∇(𝔉_k∘exp), where K_x is the gauge-orbit tangent at x. It is O(|x|·|∇𝔉|), vanishes at critical
     points and is quadratically small along the iteration.
   - **The exact risk:** the remainder is multiplied by a Γ_E-response that can grow like L^{2k} at roots next to p. So route
     (i) needs the remainder's composite divergence at those roots to carry a compensating L^{−2k}, or to be supported away
     from p's roots. This is a precise, checkable lemma.
5. **Fallback, and the trigger for the lead.** If route (i)'s lemma fails, adopt a **restricted two-slice scheme**:
   - S_E for configurations and the nonlinear map;
   - the funnel-corrected Π^♯ only inside the linear solve, with the transfer n²⟨D(S), σ(Π_EY^p)⟩ (Lemma RC) and the tents
     (TE) carried as explicit correction terms;
   - plus a proof that the transfer is a gauge transform whose 𝔐^∇ cost is bounded on the sources that occur.
   - The decision is the lead's after route (i)'s lemma is settled. Until then the LEAD DECISION "one gauge fixing Γ_E" stands,
     qualified as BFT_A 38.8 says.
6. **Lever (note, not a recommendation).** The spikes are specific to lane A's S4' contour-average Q: ε ≠ 0 only at
   asymmetric near-root placements. A root-covariant Q with a smaller near-root funnel would shrink them. Q is constrained by
   Lemma Γ0's reflection symmetry (C_g-θ), so any change must keep L1.

---

# Required fixes

Binding unless marked cosmetic.

**Lane B**
1. **RS8-1 (cosmetic).** Add a dated note to the 22.2 heading (l.2989): "IMPORTED-AND-REVERIFIED" now reads PROVEN-HERE, per
   the RS7-3 tag.
2. **RS8-2 (binding).** In a dated note after §26, replace the reading at l.3415-3417 ("same order as the target … cannot be
   dropped") by:
   - "Q_X = ⟨j, (Ξχ^5_X)_l⟩: the root charges are the dual of lane A's tents (Proposition TE);
     ||(Ξχ^5_X)_l||_1 = 8L^{3(k−l)} exactly; (PW-i)_{Γ_E} at level l requires the tent coefficients to be ≲ C_PL^{−2k}/8.
     Sup bounds on Γ_E^TD(j) do not control the response."
   - Make the same correction in §26 FOR OTHER FILES.
3. **RS8-3 (binding).**
   - Rename lane B's lemma (for example Lemma ΓT-op), and state in one line that it does **not** imply BFT_A §36.0's (GE-T).
   - Record lane A's (GE-T) as "expected FALSE for S_E (ARGUED, BFT_A 38.8, REVIEW_BFT_B_S8 Cross-lane)".
4. **RS8-4 (cosmetic).** Correction (2) of §25: Lemma N1G and GE-T (c), (e) hold in every d (with 2^d). d = 4 is the case
   needed.
5. **RS8-5 (cosmetic).** 25.1 (e), l.3387: start the telescoping sum at t = y_μ. Optionally record
   C_∞ = (1 − M^{−4})/8 exactly (the symmetry argument).
6. **RS8-6 (cosmetic).** 25.4: with the stated stopping rule the last-scale constant is ≤ 1024η.
7. **RS8-7 (cosmetic).**
   - §26: bb8n's model has corner roots (3X). N2-loc (c) needs only "root = subdivision node".
   - bb8n_defect's prediction post-dates the observed 0.0000. It is a resolution check with no pre-registration weight.
   - bb8n's VERDICT line lists all tests.
8. **RS8-8 (binding).** Remove "S_E against the 𝒩-optimal representative in ℓ¹" from the open lists (§24.1 Remark GE-T'
   planned clause, §26 table, FOR OTHER FILES). It is not needed (Part B).
9. **RS8-9 (binding).** In a dated note on §26's "What (CovLift) rests on now": (CovLift) is unaffected by the cross-lane
   finding. The (PW-ℓ¹)/(NC-Γ) consequence belongs to lane A's linear package and to BFT-5's statement (Part F).

**Lane A** (for its owner; not edited)
- **P8-a (cosmetic).** In 38.4 and 38.8: the tent size is exact, 8L^{3(k−l)} (lane B (f)). The (GE-T) requirement concerns the
  level-k differences of ψ_u.
- **P8-b.** In 38.5 and 38.8: cite the S_E level-0 divergence identity above (C.3) for the S_E ≈ S_C0 inference, in place of
  "ARGUED by analogy".

---

# Tally (lane B session 8; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | provenance (byte accounting exact); RBB7 fixes (all eight); **Lemma GE-T (a)-(f)** (exact tent sum 2d(n/s)^{d-1}); Remark GE-T' as ARGUED; **Theorem N2-loc** (a)-(d), including **(c) d_j ≡ 0** (proof and code); bb8t, bb8n (L-c FAIL honest), bb8w, bb8n_defect (re-runs identical apart from timing) |
| CONFIRMED as an implication | **Theorem N1-loc** (given LES-div); **Corollary CL-iv** (C^{1,α} terms; residual at Cg-NL's status) |
| NOT ADEQUATE | GE-T as a proof of lane A's (GE-T) (different, stronger statement; expected false) |
| CORRECTION | l.3415-3417 reading (RS8-2); name collision (RS8-3) |
| NEW (reviewer) | the exact decomposition of Π_Eu⃗^♮ into straight / funnel / bulk / tent terms; the S_E level-0 divergence identity (no point divergence at non-level-k roots); probes R1 (non-vacuity of d_j = 0), R2 (tent sum, d = 2-4, L = 3, 5), R3 (bulk Λ of co-closed fields bounded ≈ 0.1, against log n / n² for δ_b) |
| ARGUED (concurring with lane A) | (PW-i)_{Γ_E} and lane A's (GE-T) fail for large k (spikes at l > k/3 + O(1), tents with factor n²) |

---

# Current minimal open set for BFT-0..5 (both lanes, after session 8)

## BFT-0/1/2 (m = 0, trivial background)

**Holds:**
- (H-lin^∇), the gauge-invariant half: holds for co-closed sources and all T.
- Residual-gradient / configuration half in S_E: holds for T ≥ 3, and T = 1, 2 by the q-fold lift (ARGUED).
- **Theorem PW-cc** (new, lane A, unreviewed by me except its role): the co-closed half of the dual (PW-i), at every level,
  k- and T-uniform.

**Open:**
- **(NC-Γ) for Γ_E: expected FALSE as stated** away from the critical set. Replace it by **(NC-Γ)_cc plus the
  contraction-remainder lemma** (Cross-lane 4, route (i); owner lane A). The restricted two-slice fallback is a lead decision
  conditional on it.
- **(PW-ii)**, needed by Proposition SR's t ≥ 2 terms. In S_E its symmetric part fails for the same reason as (PW-i).
- The endpoint α = θ.
- Explicit constants.
- (H-rem^∇) third order: ARGUED.
- (FP♯').

## BFT-3

- k = 1 PROVEN.
- k ≥ 2 ⇐ weighted (H-inv)_m on the co-closed classes. Theorem W0_m is CONFIRMED for 0 ≤ m ≤ m_Y; DX_m and DB_m are OPEN.
- The weighted (NC-E) behind (H-𝔊_w)_k.
- V_l at m > 0.
- Lane A's table MR: m_Y meets the consumers' rates read, with two rows NOT DETERMINED.

## BFT-4

- k = 1 PROVEN.
- k ≥ 2 ⇐ RW^∇_k-Π(E):
  - (W-lin-Π) ⇐ (H-inv) + (NC-Γ), with (NC-Γ) as reformulated above;
  - (W-comm), GAP 1 (plain rows);
  - (W-loc), (f), (E3^∇) [ARGUED], (I-id) with the hypercubic symmetrisation.
- **(CovLift) = Z^off:**
  - (i)-(iii) PROVEN on 𝒦(ε), every gauge, T ≥ 5;
  - **(iv) first clause PROVEN as an implication in frames** (N2-loc, N1-loc given LES-div, NF-ex, CL-clu, CUT);
  - residual term at Cg-NL's status (BCH remainder ARGUED);
  - non-residual g_Z components at θ > 0 OPEN;
  - (v) ARGUED (Remark HOL).
- (Mult-Y) (GAP-1 family; not attempted in session 8).
- (Pair-loc) [ARGUED].
- GI-off off 𝒞_glob [ARGUED] needs (Mult-Y), (SL-cov) and (I-id) there.

## BFT-5 (linear stability at the background): no status yet; owner recommended below

Inputs: (G♯_0-field) [lane A's U = 1 package; needs the abelian multi-level physical gap], (R♯_ω) [stated, not proven;
needs C^{1,α} field control, which CL-iv now supplies in frames], SF's Lemma G-pert on X_c-small patches, (G♯-patch)
globally.

## Largest levers now

- (a) route (i)'s contraction-remainder lemma (it decides one slice against two);
- (b) (PW-ii);
- (c) (Mult-Y) / GAP 1;
- (d) BFT-5 via G-pert in frames;
- (e) the non-residual g_Z components at θ > 0;
- (f) one direct S_E run (T = 5, k = 2) to upgrade the cross-lane verdict from ARGUED.

---

# PART F: BFT-5 owner and statement

**Owner: lane B**, with lane A supplying (G♯_0-field). Reasons:
- BFT-5 is a statement about the slice Hessian, and lane B owns S_E, Π_E and the frames.
- G-pert from U = 1 to Z(V_k) needs exactly what lane B has just proven: C^{1,α} control of the background in frames
  (CL-iv) and covariance on 𝒦(ε) ((CovLift) (i)-(iii)). PROOF l.3473 says (R♯) needs C^{1,α} control of the field.
- Lane A is loaded with (NC-Γ)_cc and (PW-ii).

**Statement (recommended; written so that it does not depend on the one-slice / two-slice decision).**

> **(BFT-5_E).** There are ε_5 > 0 and C_5 < ∞, independent of k and T (T ≥ 5), such that for every V_k ∈ 𝒦(ε_5) the
> S_E-slice Hessian H_E := ∇²𝔉_k(Z(V_k)) restricted to S_E is invertible. For every source S that is composite-co-closed
> relative to Λ_* (⟨D(S), ξ⟩ = 0 for ξ ∈ Λ_*), the response x = H_E^{-1}S obeys the (G♯) bounds in SF's 𝔐-pair:
> ||x||_𝔐 ≤ C_5||S||_{𝔐*}, together with the weighted locality of BFT-3 at rate ≥ m_Y. For a general source, the bound holds
> for the gauge-invariant part, and the slice-dependent root terms (Lemma RC's n²⟨D(S), σ⟩ and Proposition TE's tents) are
> stated separately with their explicit sizes.

**Proof route.**
1. (G♯_0-field) at U = 1 (lane A).
2. (R♯_ω) on frames Ω, using Z^off and CL-iv for ||log Z^off||_{C^{1,α}} ≤ C_1ε.
3. SF's Lemma G-pert on X_c-small patches.
4. (G♯-patch) by the (CovLift)-covariant gluing.

**First narrow lemma:** (R♯_ω) in local frame form, given CL-iv.

---

## Re-run record and reviewer probes

All outputs are in scratchpad `revBB8/`: `*.rerun.out`, `*.rerun.time`, `probe_rows.out`, `probe_tent.out`, `probe_cc.out`,
`lock.log`. Scripts: `probe_rows.py`, `probe_tent.py`, `probe_cc.py`.

| job | result | wall | peak |
|---|---|---|---|
| bb8t_get | identical apart from `[t = …]` | 5.9 s | 564 MB |
| bb8n_lip | identical apart from `[t = …]`, including the L-c FAIL | 1.8 s | 190 MB |
| bb8w_nf | identical apart from `[t = …]` | 0.5 s | 83 MB |
| bb8n_defect | identical apart from `[t = …]` | 1.1 s | 167 MB |
| R1 probe_rows (bb8n's code, unchanged by exec) | root-row interior links ≤ 1.3e-18; off-row 2.5e-2 / 3.2e-3 / 3.8e-4 | 0.3 s | 156 MB |
| R2 probe_tent | deviation from 2d(n/s)^{d-1} ≤ 1.3e-15 | 0.05 s | 27 MB |
| R3 probe_cc (d = 4, coarse side 5, n = 2, 3, 4; 625 box solves each) | numbers in the Cross-lane section | 194 s | 145 MB |

- One lock acquisition, 11:40:58-11:44:22 UTC (load1 2.39; memory free 43% → 42%). `rmdir` was called once, by the runner.
- After the coordinator's handoff no further run was needed. The lock directory was found empty and no process was running
  (`pgrep -fl 'bb8|probe_|run_bb8rev'` empty).
- No `checks/__pycache__`. No repository file other than this review was written.
