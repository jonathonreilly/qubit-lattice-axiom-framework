# REVIEW_BFT_A_S2: hostile line-by-line review of BFT lane A, session 2 (BFT_A.md §6-§10, BFT_A_LOG session 2, checks/ba2_*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: BFT_A.md l.18-47, l.258-275, l.332-794
(§6-§10 in full); BFT_A_LOG.md (all); REVIEW_BFT_A_S1.md (all); LINEAR_PACKAGE.md l.80-204, l.356-384 (Setting SC,
norms, Lemma 2.2-2.5, J-str, LES, N2-lin, Lemma 6.5-6.8); REVIEW_BFT_B_S1.md (the (G♯-res)/m > 0 rows, l.222-237, 492-519);
checks/ba2_criteria.md, ba2_lin.py (all), ba2_outV.txt, ba2_outM.txt, ba2_time.txt. Only this file was written in the repo;
my rerun outputs are in the session scratchpad
(`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revbftA2/`).

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / GAP / WRONG. Nothing below is counted in PROOF's tally.

## Bottom line

- **Provenance: file-order pre-statement of §7 CONFIRMED; epistemic pre-statement NOT established.** The first 56805 bytes
  of BFT_A.md end exactly at the end of §7 (the "Check ba2" paragraph), and §8 starts at byte 56806. That matches the
  logged post-append size, and the birth time is still 05:39:32Z. But §6 was in the file before §7, and it already reports
  the session-2 outcomes (l.393 "proven in session 2, BL-5(c) below"; l.401 "finds both in need of correction (BL-5(c),
  BL-6(b))"). §7 also carries final constants (G_R, C_P, C_C). So §7 records results that had already been derived; it is
  not a prediction, and BA2-F1..F5 carry no pre-registration weight. The ba2 criteria predate the script and the outputs
  (birth times), and the §8 proofs (05:49:40) predate the ba2 output (05:51:36).
- **BL-1 (i)-(iii): CONFIRMED, exact.** **BL-2, BL-3, BL-C: CONFIRMED.** **BL-4: CONFIRMED given the package**
  (N2-lin, J-str, LES), with one constant to fix (the LES box convention). **BL-5 (a): CONFIRMED** for gauge-invariant
  outputs at m = 0. **BL-5 (c): CONFIRMED**: the checkerboard counterexample is correct, and so is the l = 0 weight
  correction ω^R_0 = L^{θk}. "Necessary and sufficient" is overstated: α ≤ θ is necessary only for the sup-only (R) slot.
- **BL-6 (a): CONFIRMED.** **BL-6 (b): CONFIRMED on the linear side.** Its remainder-side half ("unbounded for θ > 1 - α")
  is a power-count upper bound, ARGUED, not PROVEN. **8.7's step example: vacuous.** G_l is co-closed already at level l,
  so the source is zero. The "PROVEN" label must go.
- **(α, θ) window: NOT empty.** The (Pl-F3) *slot* is dead for every (α, θ). The *window* 0 < α ≤ θ ≤ 1 - α (α ≤ ½) is
  not: BL-6 (b)'s currents lie entirely in Ran Q_l^T ("smooth"), so they do not touch the rough part of a rough/smooth
  split. The window survives conditional on two OPEN lemmas, (G♯-rough) and a smooth-part decay lemma (SPD, named below).
  Both are consistent with power counts. Recommended working point: α = ¼, θ ∈ [¼, ¾].
- **Lane B (m > 0): one exact reduction shortens the path.** For lane B's top source s_{k-1} alone, BL-1 (i) gives
  τ_j = 0 for j < k, so **x(s_{k-1}; B_k) = x(0; B_k + s_{k-1}/κ_{k-1}) exactly, at configuration level, in every gauge.**
  Lane B's (G♯-res)_m and (LEG_w) are one object: the weighted data map. Its gauge-invariant half is already Theorem 6.8 +
  Lemma 6.7 (m > 0). What remains is the configuration-level half, (G♯_0-field^∇)'s data part at m > 0.
- **ba2 rerun: byte-identical** to the logged outputs apart from timing lines. **H_f is saturating, not growing like log:**
  the increments shrink geometrically, ratio ≈ 0.33-0.38 ≈ 1/L. The extrapolated limit is ≈ 2.339 for both α. A log law would
  give constant increments.

---

# Part 1. Provenance audit

**Filesystem record (TZ=UTC stat, APFS birth | modification | size), taken 2026-10-28 ≈06:00Z:**

| file | born | modified | size |
|---|---|---|---|
| REVIEW_BFT_A_S1.md | 05:12:27 | 05:12:27 | 31642 |
| REVIEW_BFT_B_S1.md | 05:25:02 | 05:25:02 | 42830 |
| BFT_A.md | 05:39:32 | 05:54:34 | 79088 |
| checks/ba2_criteria.md | 05:42:40 | 05:42:40 | 4405 |
| checks/ba2_lin.py | 05:44:54 | 05:44:54 | 12943 |
| checks/ba2_outV.txt | 05:51:36 | 05:51:45 | 789 |
| checks/ba2_outM.txt | 05:51:45 | 05:53:33 | 3046 |
| checks/ba2_time.txt | 05:51:36 | 05:53:33 | 1742 |
| BFT_A_LOG.md | 04:56:48 | 05:54:43 | 5490 |

**What is confirmed.**
1. **The §7/§8 byte boundary.** `head -c 56805 BFT_A.md` ends with the last sentence of §7's "Check ba2" paragraph
   ("... for k = 1..4 from the exact symbols."). Byte 56806 begins "\n---\n\n# 8. Proofs of §7". This is the size the log
   records for the post-§7 stat (56805 bytes, both the mislabelled-EDT and the TZ=UTC copy). The birth time is still
   05:39:32Z, the F6 Edit-tool rewrite the log discloses, so no Edit/Write-tool rewrite happened after it. Everything after
   05:39:32 was added in a way that kept the inode, consistent with the log's "shell >> only".
2. **The disclosed birth-time reset.** Session 1's birth (04:55:24Z) appears in REVIEW_BFT_A_S1 Part 1. The current birth
   (05:39:32Z) equals the log's F6 correction time. The disclosure is accurate.
3. **ba2 ordering.** Criteria (05:42:40) < script (05:44:54) < outputs (05:51:36). The criteria file was not modified after
   birth. The script's birth equals its modification time. The log reports a Write followed by one `sed` fix, and `sed -i`
   replaces the file, so the Write-tool version's birth is lost. The surviving version is still after the criteria. The
   §8 proofs (log: 05:49:40) were appended while ba2 waited for the lock, before its output existed, so §8 was not fitted to
   ba2.
4. **REVIEW_BFT_B_S1 was born 05:25:02**, after the log's "did not exist at 05:13" check and before §7. The log says it was
   read only at ≈05:52. That cannot be tested; it is immaterial to §7-§8's mathematics.

**What is not established.**
1. **§7 is a statement of results already derived, not a prediction.** §6 sits before byte 56805 and was in the file by
   05:39:32. It already says "with sup-only residual sources (H-lin^∇) is false for α > θ (... proven in session 2, BL-5(c)
   below)" (l.392-393) and "Session 2 (§7-§8) tests the (R) weight at l = 0 and the (Pl) slot and finds both in need of
   correction (BL-5(c), BL-6(b))" (l.401). §7 then states BL-5 (c) with its exact lower-bound constant
   (2^{1-α}L^{-θ}/κ_+, 5G_D/κ_-), BL-6 (a) with C_P = L/(e(1-θ)ln L), and BL-C's C_C. These are constants of finished proofs.
   §7's own l.441 discloses "Exploratory reasoning in this session preceded it (not recorded)".
   - **Reading:** "PRE-STATED" (l.437, log 05:40:30) is a file-order fact only. "Failure modes (pre-stated, session 2)"
     BA2-F1..F5 (l.563-566) were written after their outcomes were known (§6 l.401). They carry no pre-registration weight,
     the same verdict as session 1's l.93.
2. **The stat lines are transcriptions.** The log was last modified at 05:54:43, so the session-2 log block was written
   (or rewritten) at the end. The byte-size match in item 1 is the independent corroboration, and it holds.
3. **A truncating rewrite** (`cat > file`) keeps the inode and the birth time. It cannot be excluded by filesystem evidence.
   Nothing in the content suggests one.

**Provenance verdict: ACCEPTABLE WITH RELABELLING (binding fix P1).** The ba2 pre-registration is real, and so is §7's
file-order priority over §8. §7's "pre-stated" label and BA2-F1..F5 must be read as post-derivation statements.

---

# Part 2. §6 [RBA1-fix] (l.332-433): CONFIRMED, with two supersessions to make explicit

- F1, F2, F5, F7, F8: applied as REVIEW_BFT_A_S1 asked. The l.18/l.93/l.292 relabels are correct.
- **F6 Lipschitz form (l.373-381): CONFIRMED.** BCH₂ is a symmetric quadratic form, so BCH₂(x) - BCH₂(x') = B(x - x', x + x').
  B(ū, v̄) = 0 on direction-constant pairs follows from BA-4 applied to ū, v̄ and ū + v̄. The three-term bound with
  |ū| ≤ L^{-(k-l)}||·||, δ ≤ 5L·L^{-2(k-l)}||·|| gives (10L + 25L²L^{-(k-l)})L^{-3(k-l)} ≤ 35L·L^{-3(k-l)} for k - l ≥ 1.
- **The "corrected pair" (l.396-401) is superseded twice by §7-§8 and should say so in place of "finds both in need of
  correction":**
  - (R)'s ω_0 = 1 is replaced by ω^R_0 = L^{θk} (BL-5 (c));
  - the (Pl, F3) slot is unusable as a slot for all currents (BL-6 (b)).
  §10 records both, but a reader of §6 alone gets the wrong pair (fix B6).

---

# Part 3. BL-1 (exact reductions; l.476-486, proof l.588-596): CONFIRMED

- **(i)** (κ/2)|r|² - ⟨s, r⟩ = (κ/2)|r - σ|² - |s|²/(2κ). With y = x + τ and τ_{l+1} = Q_lτ_l + σ_l, τ_0 = 0, I re-derived
  r_l(y) = r_l(x) + Q_lτ_l - τ_{l+1} = r_l(x) - σ_l, so r_l(x) = r_l(y) + σ_l, and dx_0 = dy_0.
  - The G and j terms change by x-independent constants.
  - y_k = B_k + τ_k is fixed data.
  - x ↦ y is an affine bijection of the unknowns.
  - **Exact.** ba2 V1 (rel ≤ 2.0e-11) confirms it against an independent CG solve with the explicit source gradient. I read
    the code: `grad_src` adds Q_l^Ts_l at level l and -s_l at level l + 1, the correct gradient of ⟨s_l, Q_lx_l - x_{l+1}⟩.
- **(ii)** x_m = Q_{m-1}x_{m-1} - r_{m-1} gives ⟨v, x_m⟩ = ⟨Q^Tv, x_{m-1}⟩ - ⟨v, r_{m-1}⟩. Iterating, with
  Q_{m-1}^T(Q^{(m→l)})^T = (Q^{(m-1→l)})^T, gives the stated identity. The energy's -⟨j, x⟩ then produces residual sources
  s_i = -(Q^{(i+1→l)})^Tj_l. Signs check. The identity needs no co-closedness of j_l. Q^Td* = d*𝒬^T is the transpose of
  dQ = 𝒬d. **Exact.** (V2: 2.0e-12.)
- **(iii)** Telescoping Q^{(l→k)}x_l - x_k = Σ_iQ^{(i+1→k)}r_i is correct. The induced sources s_i = +(Q^{(i+1→k)})^TJ have
  the opposite sign to (ii), consistent with 8.7 (b). **Exact.**
- **8.0 existence: CONFIRMED.** On the torus a closed x_0 is dλ + const. Q^{(0→k)} maps the constant to L^k·const, and a
  gradient plus a constant vanishes only if both do. Every source vanishes on the composite-gauge kernel, so the minimum is
  attained.

# Part 4. BL-2 (l.488-498, proof l.598-618): CONFIRMED

- (a) The one-step bound L||v||_own, converted to coarse units, gives a contraction.
- (b) The induction h^{(a→b+1)} = h_bQ_str^{(a→b)} + ev∘h^{(a→b)} is right; it uses root covariance and IT-str. Path length:
  |y - c_X|_1 ≤ 4·(L-1)/2 = 2(L-1). The geometric sum gives 2(L^{b-a} - 1). |dλ| ≤ 2 sup|λ|, so dh ≤ 4L^{b-a}, i.e.
  ≤ 4 in coarse units, total ≤ 5. ba2 V4 measures 2.53/2.77.
  - h_l(const) = 0 needs L odd and c_X the block centre (§1.1 has L ≥ 3 odd).
- (c) Q^T = Q_str^T - h^Td*. Co-closedness is preserved via d*Q^T = ev^Td*. A fine μ-link meets exactly L coarse
  averages, so the factor is L^{-3}, attained on constants (V4: 1.000000).
- (d) The probability-average form and the 3ρ_b support are right for L ≥ 3 (2L/(L-1) ≤ 3). The transpose formula is
  right: L^{2(k-l)}·L^{-4}·L² = L^{2(k-l-1)}.
- (e) Correct. Osc_2 ≤ ||H||_∞ (take c = 0).

# Part 5. BL-3 (l.500-505, proof l.620-626): CONFIRMED

- τ_j = Σ_{i<j}Q^{(i+1→j)}σ_i, with one factor 5 per composite (no compounding).
- ||σ^c_i|| ≤ L^{-θ(k-i)}L^{-(k-1-i)}||s||_R/κ_-. Substituting m = j - 1 - i gives L^{-θ}L^{-(1+θ)(k-j+m)}, so the sum is
  ≤ L^{-θ}L^{-(1+θ)(k-j)}L/(L-1).
- Gradient/curvature factors 2L^{k-j}, 4L^{k-j}; Campanato factor ρ_j^{-α}.
- 𝔐^∇ total: c_1 + 2c_1 + 2c_1 + 1/κ_- = 5c_1 + 1/κ_- (𝔐^∇ includes ||x^c_j||, §1.4). ||·||_inv total: 8c_1 + 1/κ_-.
- Uniform in k, T for α ≤ θ. **BA2-F1 does not occur** (and was known not to; Part 1).

# Part 6. BL-C (l.507-508, proof l.628-635): CONFIRMED

I re-derived each step:
- the nested dyadic chain;
- the factor (|B|/|D|)^{1/2} = 4 per dyadic step (16 = 2⁴ in d = 4);
- the telescoping sum 4[H]_α(2^Iε)^α·2^α/(2^α - 1);
- the common box B* of side 2^{I+2}ε ≤ 1, in both cases I = 0 (then δ = ε) and I ≥ 1 (then 2^Iε < 2δ ≤ ¼), with factor
  2·(4⁴)^{1/2} = 32;
- (2^Iε)^α ≤ (2δ)^α;
- the trivial range δ > 1/8.

When ρ_j ≥ 1/8 (j ≥ k - 1 at L = 3) only the trivial range occurs, which is consistent. C_C is as stated.

# Part 7. BL-4 (l.510-515, proof l.637-660): CONFIRMED given the package; one constant to fix

- **Package inputs checked against LINEAR_PACKAGE:**
  - J-str (c), l.166-169: sup|r_i| ≤ (κ_{k-1}/κ_i)L^{-3(k-1-i)}sup|r_{k-1}| and sup|J^c_0| ≤ κ_{k-1}sup|r_{k-1}|, uniform
    in k;
  - N2-lin, l.196-198: C_R, C_f uniform in k and T;
  - LES, l.173-175.
  The unit conversions L^{k-1-i}||r^c_i|| = L^{2(k-1-i)}||r_i||, F_0 = n^{-2}||f_0|| and RJ_0 = n^{-2}||J^c_0|| are
  correct.
- **LES box convention (fix B7, constant only).** "B of fine side s lies in Q_{2s}(c)" and Osc_2(F; B) ≤ 4·Osc_2(F; Q_{2s}(c))
  hold if Q_ρ(x) is the box of *side* ρ centred at x. If LINEAR_PACKAGE's Q_ρ is the radius-ρ box (side 2ρ + 1), the factor
  is ((4s+1)/s)² ≤ 25 instead of 4, and C_L changes accordingly. Also check LES's admissibility (x ∈ Q_{R/2}(x_0),
  ρ ≤ R/4) in that convention: with R = n on the periodic extension it holds for 2s ≤ n/4. The conclusion is unchanged.
- **Upper levels: CONFIRMED.** f_j = 𝒜^{(0→j)}f_0 - R_j follows from dx_{j+1} = 𝒬dx_j - dr_j. The sup bound
  6κ̂L^{-(k-j)}||r_{k-1}|| is right.
  - The pointwise-Hölder step is valid with any coupling. The supports of the two averages lie within δ + 3ρ_j ≤ 4δ of each
    other, so a product coupling suffices. Translation covariance at the trivial background would give δ instead of 4δ
    (a sharper constant; optional).
  - The R_j Hölder term 12κ̂δ^αL^{-(1-α)(k-j)} and Osc_2 ≤ [H]^∞_αρ^α are right.
- **G_D:** I recomputed the j = 0 and j ≥ 1 sums. The stated G_D dominates both (the "(1 + 4^αC_C)C_L" term covers j = 0's
  C_L and j ≥ 1's 4^αC_CC_L). **BA2-F2 does not occur.**
- **Remark m > 0 (l.658-660): ARGUED, and fine as such.** Everything except the two data kernels is local within ≤ 3
  coarse units.

# Part 8. BL-5 (l.517-528, proof l.662-682)

**(a) CONFIRMED.**
- x = y - τ; each ||·||_inv component is subadditive; ||τ_k||_D ≤ c_1L^{-θ}||s||_R.
- G_R = c_1G_D + 8c_1 + 1/κ_- (the L^{-θ} is dropped, which is legitimate).
- The X_s line uses only BL-4's residual bound and σ.
- **Scope:** gauge-invariant outputs, m = 0, sup-only residual sources. The proof is three lines on top of BL-1/BL-3/BL-4.
  §10's "no new symbol analysis was needed" is accurate.

**(c) CONFIRMED (the counterexample).**
- χ_1(b) = (-1)^{b_2} gives (dχ)_{12} = 2(-1)^{b_2}; the χ_2 terms vanish. Level-(l+1) curvature coarse factor:
  L^{2(k-l-1)}.
- On a box of side 2ρ_{l+1} (2 points per side, admissible because 2ρ_{l+1} ≤ 2/3 for l ≤ k - 2), Osc_2 = 2aL^{2(k-l-1)}
  exactly.
- The seminorm subtraction and [f_{l+1}(y)]_α ≤ G_D||τ_k||_D ≤ 5G_DL^{k-l-1}a are right.
- ||s||_R = κ_lL^{θ(k-l)}L^{2(k-1-l)}a: I recomputed the quotient and get the stated bound. At l = 0 with ω_0 = 1 the
  first term is (2^{1-α}/κ_0)L^{α(k-1)}.
- T even with L odd makes every level side even.
- **Both claims hold:** α ≤ θ is necessary for this pair, and ω^R_0 must be L^{θk}.
- The l = 0 correction is new and real: session 1 (BFT_A §1.4) and REVIEW_BFT_A_S1 F4 both carried ω_0 = 1 on the (R)
  slot. The nonlinear remainder survives the stronger weight: BA-6 at l = 0 gives
  ω^R_0L^{k-1}||s^c_0|| ≤ κC_6L^{-2}L^{-(1-θ)k}η². I checked this against BA-6's own-unit bound, using 𝔐^∇'s j = 0 gradient
  control.

**Overstatement (fix B1).** §10 l.778 says "α ≤ θ, which is both necessary and sufficient", and BL-7 (f) says the same.
Necessity is proven only for **sup-only** residual sources measured against a configuration norm with own-scale Campanato
curvature at every soft level. REVIEW_BFT_A_S1 F4's alternative (Hölder/∇ components of s_l in 𝒴^∇) is not excluded.
The actual s_l = κρ^{(2)}_l has level-(l+1) differences smaller by L^{-α(k-l)}. Read: "necessary for the sup-only (R) slot".
This does not affect the window verdict, since α ≤ θ is satisfiable.

**8.6 "Consequence for (H-rem^∇)" (l.678-682): CONFIRMED as scoped.** (R) is a max-norm and BL-3's geometric sum
absorbs the level count, so the soft-BCH₂ remainders give a response ≤ G_RκC_6L^{-2}η² in value and (by F6) in Lipschitz
form. It covers **gauge-invariant outputs only**. The contraction runs in 𝔐^∇ (BA-6's δ and x̄ are gauge-variant), so
BFT-A-F2 is disposed of for the outputs, not yet for the fixed-point map.

# Part 9. BL-6 (l.530-548, proof l.684-728)

**(a) CONFIRMED.**
- |s_i| ≤ L^{-3(k-1-i)}||j^c_l||, and the (R) weight gives L^{θ(k-i)}L^{-(k-1-i)}||j^c_l||.
- With the (Pl-c) weight this becomes L·L^{-(1-θ)(l-i)}L^{-(k-l)} ≤ L·L^{-(1-θ)(k-i)}. Summing ≤ k - 1 - i copies gives
  C_P. A sharper geometric sum gives L/(1 - L^{-θ}) and avoids the 1/(1 - θ); optional.
- Divergence form: |d*G| ≤ 6|G| (six plaquettes per link in d = 4), exponent 1 + i - l. Correct.

**Missing scope sentence (fix B3): the F3 rows are not in (Pl-c).** The remainder rows (∂ρ^{(2)})^Tr_l and [A^T, χ]A are
O(η²) per level in plain coarse units with **no** level decay (REVIEW_BFT_A_S1 Part 5). So ||rows||_{Pc} ≍ L^{θ(k-1)}η² is
unbounded for θ > 0. BL-7's pair (R ⊕ G ⊕ P0 ⊕ Pl-c) is a correct linear statement for a source class the remainders do
not occupy.

The exact location of the k-loss is worth recording. Reduce an **unweighted** plain-current family (||j^c_l|| ≤ η² for all
l) by BL-1 (ii):
- the residual part stays bounded for every θ < 1: Σ_{l>i}L·L^{-(1-θ)(k-i)}η² ≤ C_Pη²;
- the level-0 images add up to Σ_l||j^c_l|| ≤ (k - 1)η².

**All of the level-count loss sits in the level-0 image** (equivalently, after pushing up, in the top-step stacking). That
is exactly BL-6 (b)'s factor k - 1.

**(b) CONFIRMED on the linear side.**
- j_l = (Q^{(l→k)})^TJ, with J constant. By BL-1 (iii) it is equivalent to constant residual sources s_i = L^{-3(k-1-i)}ce_μ.
- τ_k is constant (Q multiplies constants by L), so dτ_k = 0.
- y has data τ_k, a constant flat datum: x_0 = τ_k/L^k realises r = 0, dx_0 = 0, and Lemma 2.5 gives uniqueness of the
  outputs.
- So r_{k-1}(x) = σ_{k-1} = (c/κ_{k-1})e_μ, independent of l, with ||j||_{F3} = L^{(θ+α-1)(k-l)}|c|.
- Single current: ratio L^{(1-α-θ)(k-l)}/κ, unbounded for θ < 1 - α. All levels: (k - 1)L^{1-α-θ}/κ_+, unbounded for
  θ = 1 - α.
- ba2 V3 confirms the identity at k = 2 (≤ 1.4e-14).
- The zero-mean variant (l.713-714) is ARGUED. My power count agrees: dτ_k = O((k-1)c/(κT)) perturbs r by O(kc/T) only.

**The remainder-side half is ARGUED, not PROVEN (fix B2).** l.542-543: "the F3 rows have ||·||_{F3} ≍
L^{(θ+α-1)(k-l)}η² ..., unbounded for θ > 1 - α". REVIEW_BFT_A_S1 Part 5 proved the *upper* bound (≲) only, and no lower
bound on the rows exists. So the conclusion is:
- PROVEN: "the F3 slot gives no k-uniform linear bound for θ ≤ 1 - α";
- ARGUED: "and for θ > 1 - α the remainder rows are not bounded in it".

The bold "no θ makes the F3 slot serve both" is ARGUED on its second half.

**8.7 step example (l.692-705, correction l.724-728): vacuous; drop "PROVEN" (fix B5).** G^c_l(X; 1, 2) = g(X_3) is
co-closed **already at level l**: d*G_l involves only differences of G_{12} in directions 1 and 2. So the source
⟨G_l, dx_l⟩ = ⟨d*G_l, x_l⟩ is zero at level l. Its level-0 image is then irrelevant, and the step-height correction
(l.724-728) corrects an irrelevant constant. What survives is the *representative* point: (G) norms representatives, not
sources. "(G♯-up) is not implied by (G♯_0-lev0)" is therefore **OPEN in full**, not "not implied via the image
representative".

**(c) Repair: correctly diagnosed. Analysis of the window in Part 10.**

# Part 10. The (α, θ) window: VERDICT — NOT EMPTY (conditional); the F3 *slot*, not the window, is dead

**Constraints actually proven:**
- θ > 0: Theorem 6.8, Ω < ∞;
- θ < 1: BL-6 (a)'s C_P, and BA-6's decay L^{-(1-θ)(k-l)};
- α ≤ θ: only for the sup-only (R) slot (BL-5 (c)).

**What BL-6 (b) kills.** It kills the use of one F3 weight on **all** plain currents. Its currents are by construction in
Ran Q_l^T: j_l = (Q^{(l→k)})^TJ, which climbs all the way to the top. They are residual sources in disguise (BL-1 (iii)),
and they stack at the top step. The earlier window α ≤ θ ≤ 1 - α (REVIEW_BFT_A_S1 F3/F4) came from the remainder-side power
count of the rows in the F3 weight. BL-6 (b) shows that the same weight is wrong on the linear side for **smooth** currents.
It says nothing about **rough** currents (Q_lw_l = 0).

**The split resolves the conflict in principle.** Write j_l = w_l + Q_l^Tv_{l+1} (BL-6 (c)).
- *Rough parts, linear side (G♯-rough), power count (mine, ARGUED):*
  - a rough w_l leaves r_l unchanged, so x_l responds by the mass term: u ≈ w_l/κ_{l-1}. Then
    [f_l]_α ≈ L^{(2+α)(k-l)}|w_l|_own = ω_l^{-1}||w||_{F3}, and L^{2(k-l)}|r_{l-1}| ≈ L^{2(k-l)}|w_l|/κ. Both are bounded
    by the F3 weight;
  - pushing w_l down (BL-1 (ii)) gives a residual source s_{l-1} = -w_l, whose (R) weight is ≤ L^θL^{-α(k-l)} times its
    F3 weight (bounded), and a level-0 current that is rough at scale ρ_l. The level-0 stiffness smooths the latter: the
    curvature response is ~ ρ_l × (coarse size) ≤ L^{-(α+θ)(k-l)}||w||_{F3}, and its Hölder part at scale ρ_l is
    ≤ L^{-θ(k-l)}||w||_{F3};
  - so BL-6 (b)'s mechanism is absent. No restriction on θ arises from the linear side of rough currents.
- *Rough parts, remainder side:* the rows' rough parts are at most the full rows, so they are bounded in the F3 weight iff
  θ + α ≤ 1 (REVIEW_BFT_A_S1's power count; ARGUED).
- *Smooth parts, remainder side, a new named lemma **(SPD) smooth-part decay**:* the Ran(Q^T) component of the row at level
  l, carried up to level m, must have plain coarse size ≲ L^{-(m-l)}η². Then the top-step stacking Σ_l is geometric, and the
  k - 1 of BL-6 (b) does not arise.
  - Route (ARGUED) for the soft row: ⟨(∂ρ^{(2)})^Tr_l, Q^Tv⟩ = 2⟨r_l, B(x, Q^Tv)⟩, and B vanishes on pairs of
    direction-constant fields (BA-4 polarisation, F6). Q^{(l→m)T}w is a moving average along μ and piecewise constant
    transversally, so on N(X, μ) it is direction-constant up to interpolation gradients O(L^{-(m-l)}), except in a boundary
    layer of relative volume O(L^{-(m-l)}). The pushed-up component is a block sum, so it sees only that layer. The
    δ_x-term carries an extra L^{-(k-l)} besides.
  - For [A^T, χ]A (outside 𝒞_glob only) the analogous factor is ρ_l/ℓ.
- *Smooth parts, linear side:* exactly (R), by BL-1 (iii) (BL-5 (a)).

**Window after the split: 0 < α ≤ θ ≤ 1 - α (so α ≤ ½)**, e.g. α = ¼, θ ∈ [¼, ¾]. It is conditional on (G♯-rough)
(OPEN, power count consistent) and (SPD) (OPEN, ARGUED route above). If the Hölder-source (R) variant is used, α ≤ θ can
be dropped and the window becomes θ ≤ 1 - α. If (SPD)'s mechanism also shrinks the rough parts, θ + α ≤ 1 relaxes. **Nothing
proven so far makes the window empty.** BFT_A §10's "F3's plain-current slot (unusable as written; needs the split)" is the
correct reading, and BL-7 (f) "θ ≤ 1 - α enters only through the repaired plain slot, ARGUED" is correct.

# Part 11. Status of the open items and the shortest path to m > 0 for lane B

| item | status after session 2 | note |
|---|---|---|
| (G♯-res), gauge-invariant outputs, m = 0 | PROVEN (BL-5 (a)) | review CONFIRMED |
| (G♯-res), m > 0 | ARGUED (§10) | for lane B's case, exact reduction below |
| (G♯_0-lev0) (LED-src, G♯_0-plain) | OPEN | global part needs screening (G0-F3); the k-loss of plain currents sits here (Part 9) |
| (G♯-up) | OPEN in full | 8.7's obstruction is vacuous (Part 9) |
| (G♯-rough), (SPD) | OPEN | power counts consistent; window survives (Part 10) |
| (G♯_0-field^∇) (gauge-variant 𝔐^∇ components) | OPEN | the slice; also lane B's (LEG_w) |

**Exact reduction for lane B (new; PROVEN here from BL-1 (i)).** Lane B's top source s_y = s_{k-1} is residual-type at
step k - 1 only (REVIEW_BFT_B_S1 l.222). Then:
- τ_0 = … = τ_{k-1} = 0 and τ_k = σ_{k-1} = s_{k-1}/κ_{k-1};
- the unknowns x_0..x_{k-1} are unshifted, so **x(s_{k-1}; B_k) = x(0; B_k + s_{k-1}/κ_{k-1}) at configuration level, in
  every gauge**;
- r_{k-1}(x) = r_{k-1}(y) + σ_{k-1}, and all other outputs equal y's.

Consequences:
1. The gauge-invariant half of (G♯-res)_m for lane B is **Theorem 6.8 (a)-(b)** (weighted r) plus **Lemma 6.7/Lemma 4.4**
   (exponential f_0 kernel), applied to the datum σ_{k-1}, with ||σ_{k-1}||_{D,m} = ||s_{k-1}||_{∞,m}/κ_{k-1}. No
   composite-map locality is needed, because τ has no intermediate levels. The weighted Campanato components need only a
   weighted LES. LES is local (one coarse unit), so weights cost e^{O(m)}. ARGUED, short to write.
2. The configuration-level half of (G♯-res)_m **is** lane B's (LEG_w): REVIEW_BFT_B_S1's two OPEN rows (l.222, l.223)
   collapse to one, the **weighted data map into 𝔐^∇**, i.e. (G♯_0-field^∇)'s data part at m > 0.

**Shortest path to what lane B needs:**
- (i) write the top-source reduction above (½ page);
- (ii) write weighted LES + BL-4 at m > 0, giving gauge-invariant outputs;
- (iii) fix a translation-invariant per-level slice (REVIEW_BFT_A_S1 Part 8 step 1) and prove a local reconstruction
  lemma: in that slice, ||x^c_j|| + ||∇^cx^c_j|| + [∇^cx^c_j]_α are bounded by the gauge-invariant outputs (f_j, r_j) plus
  the flat-holonomy zero mode, with e^{O(m)} weights. This is a per-level lattice Schauder/Hodge statement: the
  degree-0 CZ part is Hölder→Hölder bounded by (G1)-(G3). BL-4 now supplies Campanato control of f_j at every level,
  which is exactly the input it needs.
- (iv) the m = 0 → m > 0 Combes-Thomas step (lane B's (H-op)) is then needed only for the nonlinear Neumann series, not for
  the linear response to s_y.

---

# Part 12. ba2 rerun and H_f

**Rerun (numeric lock).**
- Lock acquired 06:03:33Z (load 2.77, 39% free at acquisition; 44% at the pre-check), released 06:05:30Z by one rmdir.
- nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; PYTHONDONTWRITEBYTECODE=1, so no __pycache__ appeared in
  checks/ (verified); no timeout; no process left (verified).
- Part V 8.4 s, peak RSS 0.65 GB; Part M 108.8 s, peak RSS 0.23 GB.
- **Both outputs are byte-identical to checks/ba2_outV.txt and ba2_outM.txt** after stripping timing/RSS fields. All of V0-V4
  and Q1-Q3 PASS reproduced.

**Code review of ba2_lin.py.**
- V1/V2 use an independent CG on the normal equations with the explicit source gradient. That is a genuine test of BL-1,
  not of the formula against itself.
- V4's coarse row norm L^{-(b-a)}·max-row-ℓ¹ is the right coarse-unit ∞→∞ bound.
- The script writes no files.
- Q3's pre-registered window (H_f(4) ≤ 1.25·max(H_f(2), H_f(3))) is **too loose to distinguish saturation from log growth**:
  a log law with increment 0.11 per level would also pass.

**H_f: saturation, not log growth (my analysis of the reproduced numbers, not pre-registered):**

| α | H_f(k = 1..4) | increments | increment ratios | geometric extrapolation |
|---|---|---|---|---|
| 0.25 | 1.86916, 2.17609, 2.28424, 2.32040 | 0.307, 0.108, 0.0362 | 0.352, 0.334 | 2.338 |
| 0.5 | 2.06857, 2.24112, 2.30590, 2.32762 | 0.173, 0.0648, 0.0217 | 0.375, 0.335 | 2.339 |

The increment ratio converges to ≈ 1/3 = 1/L: each new finest level adds a contribution L^{-1} times the previous one.
That is the signature of a convergent level sum, and log growth would give constant increments. With only three increments
this is a diagnostic, not a proof. It agrees with BL-4's uniform G_D, and the two α values extrapolate to the same limit.
H_f is a lower bound (pairs within one coarse cell, along e_1 only).

---

# Binding fixes for the next lane-A session

- **P1 (provenance).** §7 l.437-442 and the log's "05:40:30 §7 PRE-STATED": add "file-order only; §6 l.393 and l.401 (in the
  file before §7) already report BL-5 (c)/BL-6 (b)'s outcomes, so §7 states results already derived". Relabel l.563
  "Failure modes (pre-stated, session 2)" to "stated after the outcomes were known; not pre-registered".
- **B1 (BL-5 (c) scope).** §10 l.778 and BL-7 (f): "necessary and sufficient" becomes "necessary for the sup-only (R) slot
  (BL-5 (c)); a Hölder-source (R) variant is not excluded".
- **B2 (BL-6 (b)).** l.542-543: "≍" becomes "≲ (REVIEW_BFT_A_S1 upper bound)". "No θ makes the F3 slot serve both" becomes
  "PROVEN: no k-uniform linear bound for θ ≤ 1 - α; ARGUED: remainder rows unbounded in it for θ > 1 - α".
- **B3 (BL-7 scope).** Add that the F3 rows have ||·||_{Pc} ≍ L^{θ(k-1)}η², so (Pl-c) does not contain them. Under the
  unweighted plain norm the residual part is bounded (C_P) and the level count sits entirely in the level-0 image
  (Σ_l ≤ (k - 1)η²).
- **B4 (window).** State the window as 0 < α ≤ θ ≤ 1 - α, conditional on (G♯-rough) and (SPD) (Part 10). Record that
  BL-6 (b)'s currents are in Ran Q^T, so the split is not touched by it.
- **B5 (8.7).** Delete "PROVEN for the image itself" and the step-height correction's role. G_l is co-closed at level l, so
  the source is zero. "(G♯-up) not implied" becomes "OPEN".
- **B6 (§6 corrected pair).** Replace l.401's forward reference with the two supersessions (ω^R_0 = L^{θk}; F3 slot replaced
  by the split).
- **B7 (BL-4 constant).** Fix the LES box convention (side vs radius) and the factor 4 (≤ 25 under the radius convention).
- **B8 (lane B).** Write the top-source reduction x(s_{k-1}; B_k) = x(0; B_k + s_{k-1}/κ_{k-1}) and pass it to BFT_B: (G♯-res)_m
  ≡ (LEG_w) at configuration level.
- **B9 (checks).** Any future depth-trend criterion should test the increment ratio (saturation: ratio < 1 bounded away from
  1), not a 25% window.

# Strategic verdict

Lane A is **not** blocked. Session 2's real content:
- an exact and correct algebraic reduction (completing the square) that proves (G♯-res) for the gauge-invariant outputs
  at m = 0;
- a correct necessity theorem that fixes the (R) weight at l = 0;
- a correct proof that one F3 weight cannot serve all plain currents.

The apparent window conflict (α ≤ θ from BL-5 (c), θ > 1 - α from BL-6 (b), θ ≤ 1 - α from F3's remainder power count) is
an artefact of applying the F3 weight to smooth currents. With the rough/smooth split, the window α ≤ θ ≤ 1 - α survives,
conditional on (G♯-rough) and (SPD). **Highest-value next step:** for lane B, write the top-source reduction plus the weighted
gauge-invariant bounds (steps (i)-(ii) of Part 11, essentially already proven). Then put the lane's effort into the one shared
object, the weighted configuration-level data map ((G♯_0-field^∇)_m via a per-level slice and a local reconstruction
lemma). That single estimate feeds both BFT-0/1/2 and BFT-3. (G♯-rough)/(SPD) are lane A's second target, needed for
(H-rem^∇) in 𝔐^∇, not for lane B's linear response.

## Tally

- CONFIRMED: §6 F1/F2/F5/F6/F7/F8; BL-1 (i)-(iii); 8.0; BL-2; BL-3; BL-C; BL-5 (a); BL-5 (c) (counterexample and l = 0
  weight); BL-6 (a); BL-6 (b) linear side; 8.6 consequence (gauge-invariant scope).
- CONFIRMED-WITH-FIX: BL-4 (LES box constant); BL-7 (scope: (Pl-c) does not contain the rows).
- ARGUED (mislabelled as proven): BL-6 (b) remainder side; BL-5/BL-7 "sufficient" in the necessity sense.
- WRONG / vacuous: 8.7 step example ("PROVEN for the image itself"; the source is zero).
- Provenance: file-order pre-statement CONFIRMED (byte boundary 56805); epistemic pre-statement NOT established (§6
  l.393/l.401).
- Checks: ba2 rerun byte-identical (V0-V4, Q1-Q3 PASS); H_f saturating (increment ratio ≈ 1/L, limit ≈ 2.339).
