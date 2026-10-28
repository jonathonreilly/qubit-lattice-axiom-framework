# REVIEW_S9_S10: independent hostile review of sessions 9 and 10

Reviewer: an independent agent that did not write the proof.

Inputs:
- PROOF.md, byte-identical to PROOF_session10_snapshot.md (checked with `cmp`).
- `diff PROOF_session8_snapshot.md PROOF_session10_snapshot.md` (hunks at l.1-80, 342-362, 453-463, 903-1001,
  1091-1133, 1142-1217, 1217-1765, 2295, 2741-2786, 2859-2907), with PROOF.md read by offset.
- RTARGET.md §9-15; LOG.md sessions 9-10 (l.467-556); REVIEW_S7_S8.md.
- Checks c19b, c20, c21 and c22: criteria files, scripts and outputs. All four were re-run.
- **Primary source.** Dimock, arXiv:1108.1335. I fetched it myself into the scratchpad `rev910/dl/dimock.pdf`
  (52 pp., sha1 b8b4e855…, identical to the session's copy) and extracted it with pypdf. I read:
  - §3.1 (polymers, l.762-764 of the text: face-connected);
  - (119)-(123), App. A (Lemma 25, Cor. 26);
  - App. B, Thm 27 and (300)-(333), pp.39-44.
- **Provenance.** The session-9 and session-10 agent transcripts (tool-call timestamps, UTC). The directory is
  untracked, so git history is not available.

PROOF.md, LOG.md, RTARGET.md, the snapshots and the checks were not edited. Scratch work is in the scratchpad `rev910/`:
- `scripts/ising_ce.py`: exact Ising H#, 60 digits;
- `scripts/tg.py`: an independent Penrose test;
- `scripts/jstr.py`: an independent two-level J-str test;
- the re-run outputs.

**Bottom line.**
- All 9 REVIEW_S7_S8 binding fixes are applied, and applied correctly.
- The 6 new PROVEN-HERE tally items survive. Session 9: D4-norm, GT-lat with R4D-lat, W1-size' with W1-LD-cond.
  Session 10: Theorem CE, LES, BG-b-lin with CR and J-str. None is WRONG.
- **Proposition CE-κ is mathematically correct.** Dimock's statement does say c0 depends "only on the dimension", with
  κ quantified afterwards. The counterexample is inside the hypotheses. But the wording must change, for three reasons:
  - **Attribution.** The proof's own remark after (306), "(So c0 does depend on κ.)", already corrects the statement.
    What we found is a quantifier misstatement that the author flags himself. It is not an error in Dimock's
    mathematics, and it is harmless in his paper, where κ ≥ 10(κ0 + 1) is fixed.
  - **Rigour.** The Möbius step presumes facts about H# that the bare existence statement does not give. A
    finite-difference argument closes this (fix 1).
  - **Reading.** The counterexample depends on the touching-tree reading of (119). Dimock's own proof of (305) forces
    that reading, but it must be stated.
  - Also, "discrepancy 2" is not a discrepancy in Dimock: his polymers are face-connected.
- 1 GAP: Remark D4-obs is a proof obligation created by decision 4, and it is not in the tally.
- Several CONFIRMED-WITH-FIX items: wording, small constants, edge cases, check reporting.
- All re-runs reproduce the stored outputs exactly; only timing lines differ. c19b Q3 and c22 Q3 are failed criteria,
  and both are honestly recorded.

## [R78-fix] audit (REVIEW_S7_S8 binding fixes 1-9)

| # | Fix | Where | Verdict |
|---|---|---|---|
| 1 | 2D wall cost a ≈ ε_1², window (4π/(N-2))^{1/2}, "a ≤ 2" deleted | PROOF l.903-912; header l.88-90; RTARGET §0 annotated (13:16:33 UTC); LOG l.409 | Applied, correct. |
| 2 | O(3) lattice-dislocation caveat | PROOF l.910-912; RTARGET §0 | Applied. |
| 3 | R2D-iso B = Γ-Γ bonds, b = 2(L-1) | PROOF l.922-927, 961-963 | Applied, correct (re-derived below). |
| 4 | BG-reg OPEN; Consequence tags; W2 "smooth s-family" | l.968-970, 985-986, 1091-1093, header l.69-71 | Applied. |
| 5 | W1-loc restated; cumulant remark; seam; s_0 ≲ δ_0 | l.1142-1145, 1169-1194 | Applied, all five sub-items. |
| 6 | Header wording (weak form; counted as one; smooth s-family) | l.69-80 | Applied. |
| 7 | RTARGET §8 weak-form reading | RTARGET §8 | Applied. |
| 8 | c18c "largest available" removed | l.2295-2296 | Applied. |
| 9 | c19 20 → 5 disclosure; c19b added | l.1114-1133; c19_criteria appendix | Applied. c19b reviewed below. |

**R2D-iso fix 3.** Expand each Γ-Γ bond about its midpoint z: |n(s(z + e/2)) - n(s(z - e/2))|² = s²|∂_μn(sz)|² + O(s⁴).
The central difference has no odd term. The linear term in z cancels over the ι-symmetric bond set. So
A_B = (s²/2)·bΣ_μ|∂_μn(0)|² + O(s⁴) with b = 2(L - 1). CONFIRMED.

## (1) Session-9 PROVEN-HERE items

**Lemma D4-norm (l.1231-1248): CONFIRMED.**
- ∫K dV = Π_c∫k_c dV_c = 1 exactly. Gauge covariance follows from Haar invariance of 𝒩.
- Linearity of the trace gives Σ_t(1 - N^{-1}Re tr V^{-1}T_t) = n_t(1 - N^{-1}Re tr V^{-1}M̄).
- Bound (2):
  - φ(V) ≤ N^{-1}·N||V_0^{-1} - V^{-1}||·||M̄|| ≤ ||V - V_0||;
  - a Haar ball of radius g²/κ gives 𝒩 ≥ e^{-1}c_N(g²/κ)^{N²-1}e^{-(κ/g²)(…)};
  - 𝒩 ≤ 1 only helps the denominator.
- Bound (3) holds: a cumulant expansion of bounded variables.

**Lemma GT-lat (l.1256-1300): CONFIRMED.**
- **Step 1.** The tree-gauge Stokes words have C(R_0)-bounded length. ||U_b - 1|| ≤ Σ||h_{p_i} - 1||, and BCH with
  Ad_{hol(w)} = 1 + O(ε_2) gives E_b = O(ε_2²). S_c = 1 because the complete-axial path to ±Le_μ is straight.
- **Step 2.** The exact lattice curl of 𝓛Φ is ½(Φ_μν - Φ_νμ) = Φ_μν.
- **Step 4, equivariance under reflections, checked.** Let Re_μ = -e_{μ'}. The image of the forward link (x, x + e_μ)
  is the forward link (Rx - e_{μ'}, Rx), carrying -½x^αΦ_αμ. Also (Rx - e_{μ'})^ν(Λ²(R)Φ)_{νμ'} = -x^αΦ_αμ - Φ'_{μ'μ'},
  and Φ'_{μ'μ'} = 0. So R·𝓛Φ = 𝓛(Λ²(R)Φ).
- **Steps 3 and 5.** DF̃(0) = 0 by Ad-invariance. The mean-value bound and the absorption ε_2²(…) ≤ ε_2³ + ε_2(…)
  are right.
- **Pre-statement.** RTARGET §9 was met with one added parameter, ε_V. The data include V, so this is unavoidable, and it
  is disclosed in §11. It is not a weakening.

**Proposition R4D-lat (l.1301-1315): CONFIRMED.**
- ε_* = s_0² is consistent with R4D-iso, since ||D - 1|| ~ s² there.
- K_ρ ≤ C(Λ/g²)³ sup ρ. δβ = c_ρ/c_B is unchanged.
- **The α 2 → 1 question.** The remainder is ε_2(ε_3 + ε_V) + (ε_3 + ε_V)² + ε_2³, which is s⁵ on smooth families. In
  BG-sum the level-n total is w_j[3M_2ō_n + M_2³σ_n²], and ō_n ~ σ_n there. So Σ_nL^{-n} < ∞: **still summable, now
  with one power of margin** (any polylog loss is tolerated, a power loss is not). BG-sum's arithmetic was re-derived:
  - ε_3 ≤ 2ε_2;
  - (ε_3 + ε_V)² ≤ 2M_2σ_n²(ε_3 + ε_V);
  - σ_n⁴L^{4n} = 1.
- **Fix (header l.46, LOG l.505).** "bounded iff (sufficient)" must read "bounded if". BG-sum proves sufficiency only.

**Lemma W1-size' (l.1369-1390) with Corollary W1-LD-cond (l.1409-1420): CONFIRMED (the Corollary is conditional on
(DF1)-(DF3'), and is labelled so).**
- The three-way split is exact.
- The w_ref = sup w choice:
  - sup(Num/w_ref) ≤ 1;
  - at the maximiser U*: g²S(U*) ≤ Bε_*² + O(g² log 1/g) = ε_1²/(4N) + o(1);
  - (B) gives ||1 - U_p||² ≤ 2Ng²S ≤ ε_1²/2 + o(1), which leaves the margin ε_1(1 - 2^{-1/2}) for the rg-ball;
  - U* is a critical point on a compact group, and the Hessian is ≤ C/g², so Den/w_ref ≥ c(rg)^pe^{-Cr²}.
- Chernoff: t = (u - m_0)/((1 + η)C_0²) with η ≤ 1 gives the stated exponent.
- **Note.** (DF3') is used with t ~ 1/g. The (DF3') tilt argument (N9) must therefore hold for |t| ~ 1/g. Its
  min(2, |t||c_x|ρ_W) form handles this, but see (3).

## (2) Session-10 PROVEN-HERE items

### Proposition CE-κ (l.1563-1578): CONFIRMED-WITH-FIX (the mathematics holds; the attribution and the rigour of one step must change)

**What Dimock states (read, p.39).** "Theorem 27. (cluster expansion) There is a constant c0 depending only on the
dimension such that if H(X, Φ) satisfies |H(X, Φ)| ≤ H0e^{-κd_M(X)} on the support of μ with κ > 3κ0 + 3 and H0 ≤ c0
then …".
- The prefactor O(1) in (299) "depends only on the dimension".
- So c0 is chosen before κ, and κ ranges over (3κ0 + 3, ∞). The literal statement does NOT allow κ-dependence.
- The proof, p.40 after (306), says: "we assume c0 is small enough so that 2c0K0κ0e^{κ-κ0} ≤ 1. (So c0 does depend on κ.)"
  The statement and the proof are inconsistent. The proof corrects the statement, in the author's own words.
- In the paper's application (Lemma 21, l.1671-1672 of the text), κ ≥ 10(κ0 + 1) is fixed once, so nothing in Dimock I
  is affected.

**Is the counterexample inside the hypotheses?** Yes:
- σ_x = ±1 uniform is an ultralocal probability measure.
- H({x, y}) = hσ_xσ_y depends on Φ only in X.
- A face-adjacent pair is a polymer in Dimock's face-connected sense (§3.1).
- The κ condition is satisfied for every κ.

**The decisive question is the reading of (119):** "M d_M(X) = the length of the shortest tree in X joining the M-cubes
in X".
- **Touching reading** (a tree meeting every closed cube). Here d(pair) = 0 and d(2 × 3) = 1, and the counterexample
  works. Dimock's own proof forces this reading:
  - (305) "add a line in □ joining the point in τ_i to the point in τ_j. This line has length at most M" presupposes
    that the τ_i meet □ at arbitrary points;
  - the 3^d in (122) is a touching-count constant.
- **Centre-joining reading** (a Steiner tree on the cube centres). Here d(pair) = 1, and the hypothesis forces
  h ≤ c0e^{-κ}. I computed that the counterexample then fails: h⁶ ≤ c0⁵e^{-5κ}h is below the bound
  C h e^{κ}e^{-5(κ-3κ0-3)}. Under this reading the (n - 1) term in (305) is zero, because the trees share the centre
  of □, and the κ-dependence of c0 would not even be needed.
- So the proposition is correct for the reading Dimock's proof uses. It must say so.

**Computation (re-done independently, 60-digit mpmath, `rev910/scripts/ising_ce.py`).**
- H#(Y_6)/h⁶ = 0.99970003, 0.99730254 and 0.97031485 at h = 0.01, 0.03 and 0.1. This is t⁶ - t⁸ + … ; the
  t⁸ coefficient is -1, from -½(2t⁴)² + 2·½t⁸.
- **c21 reports 1.0003 at h = 0.01. The fourth digit is double-precision cancellation noise** (|log Ξ| ~ 3e-4 against
  h⁶ = 1e-12). The criterion still passes, but the printed number is wrong.

**Rigour gap in the proof (l.1568-1571).**
- "Applying the theorem to H restricted to X ⊂ Z gives log Ξ(Z) = Σ_{Y⊆Z}H#(Y) with the same H#(Y), by locality."
  This needs two facts:
  - H#_Z(Y) = 0 for Y ⊄ Z;
  - a branch choice for log.
- Neither follows from the bare existence statement, in which H# is any family that is local in H.
- Both hold for Dimock's constructed H# of (312), since K(Y) = 0 unless Y ⊆ Z. So the proof as written refutes the
  theorem "for the H# of (312)".
- To refute the literal statement, replace the Möbius step by this argument (verified exactly by `ising_ce.py`):
  - Fix a torus T ≥ 3. Turn on only the six outer bonds of Y_6, each with coupling h_b ∈ {0, h}. Every instance obeys
    the hypothesis with H_0 = h, for every κ.
  - For h small (depending on |T|), Σ_Y H#(Y) = log Ξ holds with no 2πi ambiguity, since both sides are O(|T|h).
  - Take the alternating sum Δ over the 2⁶ on/off patterns. Every Y that misses a bond drops out, so
    Δ = Σ_{Y ⊇ Y_6}(alternating sum of H#(Y)) and |Δ| ≤ 64C_1hK_0|T|e^{-(κ-4κ_0-3)} → 0 as κ → ∞.
  - But Δ = log(1 + t⁶) > 0 exactly: 9.998000e-13 at h = 0.01, matching the exact enumeration to 12 digits.
  - So no κ-independent c0 exists, whatever local H# is chosen.

**Fix (binding).**
- Retitle: "Proposition CE-κ (the quantifier in Thm 27's statement must be κ-dependent, as Dimock's proof remarks)".
- Replace "FALSE" in the header (l.12-13), l.1457, l.1592, the tally (l.2745), RTARGET §15 (l.324) and LOG (l.538) by:
  "Thm 27's statement says c0 depends on d only; its proof says (p.40) 'So c0 does depend on κ'. Proposition CE-κ shows
  the κ-dependence is necessary. This corrects the statement's quantifiers, as the author's remark does. Dimock's proof
  and his application (κ fixed) are unaffected."
- State the touching reading of (119), and that Dimock's (305) and (122) presuppose it.
- Add the finite-difference proof.
- Correct the h = 0.01 value to 0.9997.

### Theorem CE with Lemma CE-geo and Remark CE-cx (l.1460-1595): CONFIRMED-WITH-FIX (one misattributed discrepancy)

Every inequality was re-derived.
- **(g1).** Take a maximal sup-½-separated set P. The closed side-1 boxes meet ≤ 3 cubes per axis, which gives 81.
  The ¼-balls are disjoint, and τ has Euclidean length ≥ ¼ inside each, so |P| ≤ max(1, 4ℓ). Right.
- **(g2).** A segment inside a unit 4-cube has length ≤ √4 = 2. Right.
- **(g3).** The closed DFS walk has 80^{2(n-1)}. Right.
- **(g4).** 6400e^{-a} = ½, so the sum = 2e^{-a} = 1/6400. d ≥ |X|/324 - ¼. Right.
- **(g5).** κ_0 ≥ 324. 1 + 4d ≤ 4e^d. Right.
- **Step 1.**
  - |e^z - 1| ≤ |z|/log 2 on |z| ≤ log 2, by convexity.
  - Π e^{-κ'd(X_i)} ≤ e^{-κ'(d(Y)-2(n-1))}.
  - The n-sum is e^{-2κ'}(e^u - 1) ≤ e^{-2κ'}ue^u.
  - The H_0 condition gives u ≤ |Y|/(4A) ≤ ¼ + d.
  - So C_K = 8e^{1/4}AK_0 and κ_1 = κ - κ_0 - 2. Right.
- **Step 3** is sound:
  - finitely many variables on a finite torus;
  - a formal identity in C[[z]];
  - absolute convergence on the closed polydisc;
  - identity of holomorphic functions with equal Taylor series on the connected interior, then continuity.
  This is a genuine improvement on Dimock's "formal series, afterwards convergence".
- **Step 4.**
  - The leaves-inward sum: x^c ≤ c!e^x, |Y| ≤ κ_0(1 + d), so e^{-2κ_0d}e^{|Y|} ≤ e^{κ_0}e^{-κ_0d}.
  - The root has c_1 = d_1.
  - Cayley: Σ_τ d_1Π(d_j - 1)! = (n - 2)!Σ_{seq}d_1 ≤ (n - 1)!·binom(2n-3, n-1) ≤ (n - 1)!4^{n-1}.
  - The n = 1 term is z_Y, and C_K ≤ κ_0B.
  - The third condition gives ratio ≤ ½, so C_1 = 2κ_0B. Right.
  - κ_3 = κ - 3κ_0 - 2 > 1, and the final rate is κ - 3κ_0 - 3. Right.
- **Remark CE-cx.** Right: ||μ_Y|| ≤ e^{δm|Y|} ≤ e^{δmκ_0(1+d)}. State that B, c_0 and C_1 inherit C_K → C_Ke^{δmκ_0},
  and that the κ-condition becomes κ - δmκ_0 > 3κ_0 + 3.
- **Discrepancies vs Dimock, checked against the text.**
  - **1.** (305) "at most M": real (√d·M under the touching reading).
  - **3.** (329) root |Y_1|^{d_1-1}: real. With τ(j) < j the root has d_1 children.
  - **4.** (325) κ_2 = κ - κ0 - 1 vs (310)'s κ - κ0 - 2: real typo. (333) needs κ - κ0 - 2.
  - **5.** (326) drops e^{(κ2-2κ0)(n-1)}: real. It is consistent with c0(κ).
  - **2.** Discrepancy 2 is **NOT a discrepancy**. Dimock's polymers are face-connected (§3.1: "□_j and □_{j+1} have a
    d - 1 = 2 dimensional face in common"), so (2d)^{2(n-1)} is right for his definition. Our Setting CE chose the
    larger *-connected class.
  - **Fix (l.1488, header l.14, LOG l.540, RTARGET l.324).** "Four textual discrepancies (1, 3, 4, 5) and one
    definitional difference (*-connected vs Dimock's face-connected polymers)".
- **For N6.** Theorem CE needs κ > 3κ_0 + 3 ≈ 9.2·10³ in M-units, and H_0 ≤ c_0(κ) ~ e^{-2κ}/(K_0²e^{κ_0}). Node N6 must
  deliver this decay rate, which needs Dimock's reblocking κ' = L(κ - κ_0 - 1). Write it into N6.

**Lemma TG (l.1493-1511): CONFIRMED.**
- (⇒): every non-tree edge is admissible by the minimum rule.
- (⇐): d_G = d_T, because admissible edges change d_T by ≤ 1; the depth-(d-1) neighbours of j are p_T(j) and labels
  > p_T(j).
- The partition into intervals [T, T ∪ R(T)] and the sum give (-1)^{n-1}1[R(T) = ∅].
- An independent implementation (`rev910/scripts/tg.py`) finds 0 violations on 431 random connected graphs with n ≤ 6,
  and ρ^T(K_n) = (-1)^{n-1}(n - 1)! for n ≤ 6.

### Lemma CR (l.1607-1619): CONFIRMED
- (i): composite averages, using max(ŵρ) ≤ maxŵ·colsum ρ.
- (ii): the loop T^σ_y·S_c^{-1} is the boundary of the ribbon swept by the same-order axial path translated by Le_μ.
  This needs S4' pairing, which the setting has. The constant-F flux is L·Σ_νF_νμ(y - c_X)^ν, which is path-independent
  and averages to 0 over the centred block.
- (ii) holds for every B, not only at critical points. "For every critical point" is superfluous; delete it.

### Lemma J-str (l.1620-1638): CONFIRMED
- The EL equations, the induction d*r_i = 0, and ev^T injective are all right.
- Q = Q_str - d∘h is the exact L3g(a)-slice identity (PROVEN, S3), so Q^T = Q_str^T - h^Td*.
- ||Q_str^T||_{∞→∞} = L·L^{-4}, and the κ-ratios telescope.
- **Independent check** (`rev910/scripts/jstr.py`: 2D, two levels, 27² → 9² → 3², random B_2, own S4' implementation,
  dense least squares). The two-order average is the d = 2 instance of the d! = 24 S4' order average in 4D; the proof
  is dimension-independent.
  - |d*r_0|/|r_0| = 6e-14 and |d*r_1|/|r_1| = 1e-14;
  - |r_0 - (κ_1/κ_0)Q_str^Tr_1|/|r_0| = 4e-14;
  - |J_0 + κ_0Q_str^Tr_0|/|J_0| = 2e-13;
  - ||Q_str^T||_∞ = 1/3 = L^{1-d};
  - Q∘d = d∘ev to 3e-15.
- Setting SC assumes κ_- ≤ κ_i ≤ κ_+, but only κ̂ and κ_{k-1} enter. Say so: the c20 model scaling κ_i = κL^{-2i}
  violates the lower bound and is still covered.

### Lemma LES (l.1639-1665): CONFIRMED
- Step 1: componentwise -ΔF = dJ + d*K.
- Step 2: the energy estimate ||∇w|| ≤ ||G||, and Poincaré, give r⁶(J_0 + K_0)².
- Step 3: five Caccioppoli iterations; the tensorised 1D Sobolev bound; sup|∇h| ≤ Cr^{-3}||h - h̄||; hence (ρ/r)⁶.
  For small r (r ≤ ~20), A ≥ 20⁶ makes the one-step inequality trivial, since ρ ≥ 1. Say so: it answers the "integer
  radii" question.
- Step 5: Giaquinta's iteration lemma with a = 6, b = 4 + 2α gives (ρ/R)^α(F_0 + R(J_0 + K_0)).
- Constants were not computed. That is acceptable: §13 did not demand values.

### Proposition BG-b-lin (l.1666-1695): CONFIRMED-WITH-FIX (constants and an edge case)
- **Step 1.**
  - f_{i+1} = 𝔄f_i - ϱ_i;
  - |ϱ_i| ≤ 4κ̂L^{-(k-1-i)}R_top;
  - for i < j, Σ ≤ (3/2)σ_n, so osc ≤ 12κ̂R_topσ_n.
- **Step 2.**
  - ε_V ≤ 2L(L - 1)σ_n² sup|f_j| + sup|r_j|, by CR (ii) with F = 0;
  - sup|r_j| ≤ κ̂L³σ_n³R_top.
- **Step 3.**
  - |𝔄f_0(P) - 𝔄f_0(P')| ≤ **2**L^{-4j}Σ_U|f_0 - c|: the factor 2 is missing at l.1681;
  - CS with #U = ρ_j⁴ gives 625L⁴Osc_2.
- **Step 4.**
  - F = dB_0 on the periodic extension, with R = 20L^k and |J| ≤ κ_{k-1}L^{-3k}R_top (J-str (c));
  - so Osc_2(f_0; U) ≤ C_α(Lσ_n/4)^α(F_0 + 20κ_{k-1}R_top).
- **Edge case.** For n = 0 (j = k):
  - ρ_k = 5L^{k+1} > R/4, so step 4 does not apply;
  - ε_V needs r_k, the residual of the current RG step, which the chain does not contain.
  - Fix: state the proposition for n ≥ 1. Bound the n = 0 term by the sup form (b1), with (H2) extended to the
    current step's residual.
- **Conditionals.** "BG-b ⇐ (H1) + (H2)", with (H1) + (H2) = node N2, OPEN, is labelled honestly everywhere I checked
  (header l.15-21, l.1687-1695, N2/N3).

## (3) Non-item statements

- **GAP: Remark D4-obs (l.1250-1254) is not in the tally.**
  - Under the soft kernel the RG variables V are auxiliary. L7a/L8a use block observables built from S4''(U).
  - A comparison (or an RG with observable sources) is a proof obligation of the main theorem that decision 4 created.
    The session itself says "an extra step that the main theorem will need".
  - Fix: add the OPEN item **D4-obs**: OPEN 23 → 24.
- **B-NA (iii) vs the R3-fix (l.722-724).**
  - L3g(a)-slice records "there is no nonlinear SU(N) analogue" of Q = Q_str - dh.
  - B-NA (iii) uses a perturbative one, "up to Ad-transports 1 + O(|a|) on one block". That is not a contradiction: it
    is a tree-gauge expansion, not an identity.
  - It is argued, not counted, and B-NA (iii) must address the R3-fix explicitly when it is written.
- **(DF3') tilt argument (N9, l.1749-1758; argued, not counted).**
  - "Cauchy estimates on the polydisc of step 3" need a margin: the bound holds on the closed 𝔻 only. Run Theorem CE
    with r_Y → 2r_Y (H_0 → H_0/2) to get a Lipschitz bound on 𝔻.
  - It must hold for |t| ~ 1/g, which the min(2, ·) form handles.
- **Decision 4 governance (l.30-37).** It is labelled "session-9 lead, delegated authority; not an owner ruling". That
  label is honest. REVIEW_S7_S8 (7).5 called it an owner decision. The delegation should be confirmed in the owner's
  own words. This is not a mathematical defect.
- **Session-9 header (l.44-50).** "BG-b is the U_k(ε_0)-membership half of L2" rests on CMP 109 (1.2) "[read,
  second-hand]" for (0.4). It is not load-bearing for any PROVEN item.
- **Imports.** No PROVEN-HERE item of sessions 9-10 uses an IMPORTED-NOT-YET-REVERIFIED lemma as a premise:
  - Theorem CE is self-contained;
  - BG-b-lin uses A1, the L3g(a)-slice identity and LES, all PROVEN;
  - GT-lat/R4D-lat use GT and R4D-iso, both PROVEN.

## (4) Checks re-run

Setup: laptop, nice 10, OPENBLAS/OMP/MKL/vecLib threads = 1, load 2.2-2.4, 43% free memory, sequential runs, no
`timeout`. Outputs are in the scratchpad `rev910/`.

| Check | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c19b | 5/6 (Q3 FAIL) | 16.1 s | 37 MB | byte-identical |
| c20 | VALID, SUMMABLE ×3 | 100 s | 390 MB | identical except runtime lines |
| c21 | 13/13 PASS | 6.0 s | 31 MB | identical except runtime line |
| c22 | VALID; Q1, Q2 PASS, Q3 FAIL | 398 s | 578 MB | identical except runtime lines (load 2.4, 43% free before start) |

**Provenance (UTC, from the transcripts).**
- **Session 9.**
  - RTARGET §9-10 at 13:16:57.
  - c19b: criteria 13:17:19, script 13:17:43, run 13:17:49 (output 13:18:05).
  - c20: criteria 13:20:02, script 13:21:34, a pre-run code edit 13:22:02, run 13:22:27.
  - Derivations inserted at 13:35:15; §11 at 13:36:24.
- **Session 10.**
  - RTARGET §12-14 at 13:54:48.
  - c21: criteria 13:55:51, script 13:56:44, run 13:57:04.
  - c22: criteria 14:03:57, script 14:05:38. Smoke test 1 at 14:06:09. The FastModel evaluator was added at
    14:07:20-14:07:51. Smoke test 2, then the full run 14:08:11-14:14:45.
  - The PROOF block was drafted at 14:12:43 with a literal `C22_RESULT_PLACEHOLDER`. The c22 numbers were inserted at
    14:15:04, after the run finished. So no result was written before it existed.
- The targets were not weakened. §12 already posed the κ question as a "decision to make, not presume". The separations
  are 1-20 minutes, so pre-statement is a file-order fact, as before.

**c19b: CONFIRMED.**
- Q5 is the point of the control, and it holds: c_SD = +2, c_ASD = -2.
- The Q3 FAIL is a criterion-design flaw, not a mathematical one. The window [3, 5] assumes the s⁶ term of f is
  non-zero. For asd, the ratio 17.3 ≈ 16 is the signature of a vanishing s⁶ term, so s⁸ dominates. The PROOF's
  explanation (l.1131-1133) is consistent with this. It is recorded honestly.

**c20: CONFIRMED.**
- The pre-run edit at 13:22:02 (a diagonal-term line) preceded the only run. The disclosure mentions the smoke test but
  not the code edit. Add one line.

**c21: CONFIRMED-WITH-FIX.**
- G and M test the load-bearing identities: (323) via Penrose, and the Mayer grouping.
- S tests step 3 on one instance. Nothing tests the constants chain (g1)-(g5); that is acceptable, since they are
  proven inequalities.
- Correct the I1 value at h = 0.01 (1.0003 → 0.9997), or compute in extended precision.

**c22: CONFIRMED-WITH-FIX.**
- The Q3 FAIL is recorded honestly.
- The second smoke test replaced the evaluator after the criteria were written. That falls outside "one evaluation,
  FD check, timing", but it is disclosed in c22_time.txt and the PROOF, and it is verified to 9e-16. Acceptable.
- Two weaknesses, to state in PROOF l.1709-1722:
  - **(i) Q2 has no power at t ≤ 0.1.** At the minimiser r is nearly co-closed, so even the funnel-carrying
    Q_root^T r_min has R_ax = 1.016 and 1.34, both under the 1.5 threshold. Q2 discriminates only at t = 0.2, where
    Q_root^T r_min = 2.08 and J = 1.04. That is the genuine test of B-NA (iii). V2's control power is against generic
    r, not against this alternative.
  - **(ii) The deviations do not scale like t².** dev_O = 0.022, 0.033, 0.052: from 0.1 to 0.2 they grow by 1.5×, not
    4×. So c22 shows "small", not the O(ε_0²) form claimed in B-NA (i)-(ii).
- "S is a maximum; its nonlinear correction changes sign" (l.1717) is an unverified explanation. Label it so.

## (5) Overclaims in the header and the tally

- **Header l.12-14, l.1457, l.1592, tally l.2745, RTARGET l.324, LOG l.538.** "Thm 27 … FALSE" → the attribution fix
  in (2).
- **"Five smaller discrepancies".** Four, plus one definitional difference.
- **Header l.46, LOG l.505.** "iff (sufficient)" → "if".
- **Header l.22-24.** "No cluster-expansion import and no elliptic-regularity gap remain on these two items" (l.1765).
  This is true for the linearised chain only. The NA elliptic step is B-NA (ii), argued. Add "(linearised)".
- **Tally.** The counts are right as far as they go. D4-obs is missing.

## Verdict counts

**PROVEN-HERE tally items: 6.**
- 4 CONFIRMED: D4-norm, GT-lat (with R4D-lat), W1-size' (with W1-LD-cond), LES.
- 2 CONFIRMED-WITH-FIX:
  - Theorem CE: discrepancy 2 misattributed; the CE-cx constants; the N6 requirement;
  - BG-b-lin: the factor 2, and the n = 0 edge case.
- Theorem CE's components:
  - Proposition CE-κ: CONFIRMED-WITH-FIX (attribution, the reading of (119), the finite-difference proof, the c21
    value);
  - Lemmas TG and CE-geo: CONFIRMED.
- BG-b-lin's components: CR and J-str CONFIRMED (CR with a one-word deletion).
- 0 GAP and 0 WRONG among the tally items.

**Non-items.**
- 1 GAP: D4-obs, missing from the tally.
- Wording fixes: Thm 27 attribution, discrepancy count, BG-sum "iff", the l.1765 scope.
- Check-reporting fixes: c20, c21, c22.

**Corrected tally: 49 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path) + 1
comparison branch.** The added OPEN item is D4-obs. Sessions 9-10 are now reviewed.

## Required fixes (binding for session 11)

1. **CE-κ attribution and rigour (l.12-14, 1457, 1563-1578, 1592-1595, 2745; RTARGET l.324; LOG l.538).**
   - Retitle and reword per (2). Never write "Dimock's Thm 27 is false" without "as literally stated; his proof remarks
     (p.40) that c0 depends on κ; proof and application unaffected".
   - State the touching reading of (119), and why (305) and (122) presuppose it.
   - Replace the Möbius step by the six-bond finite-difference argument, or restrict the claim to the H# of (312).
   - Correct 1.0003 → 0.9997.
2. **Discrepancy 2 (l.1488, l.14, LOG l.540).** Reclassify it as a definitional difference: Dimock's polymers are
   face-connected (§3.1).
3. **Remark CE-cx.** State that B, c_0 and C_1 inherit C_K → C_Ke^{δmκ_0}, and that the condition becomes
   κ - δmκ_0 > 3κ_0 + 3.
4. **N6 (l.1741-1743).** Add the requirement κ > 3κ_0 + 3 ≈ 9.2·10³ (M-units), via reblocking, and H_0 ≤ c_0(κ).
5. **BG-b-lin.**
   - Add the factor 2 at l.1681.
   - State it for n ≥ 1, and treat n = 0 by (b1) with (H2) extended to the current step's residual.
   - Note that only κ̂ and κ_{k-1} enter (Setting SC's κ_- is unneeded).
   - Delete "for every critical point" in CR (ii).
6. **LES.** Add one line: for r below an absolute constant, the one-step inequality holds trivially with large A.
7. **BG-sum wording** (l.46, LOG l.505): "iff (sufficient)" → "if".
8. **D4-obs → OPEN item** in the tally: 49/2/7/24 + 1.
9. **(DF3'), N9.** The Cauchy-estimate margin (r_Y → 2r_Y), and validity for |t| ~ 1/g.
10. **B-NA (iii).** When written, reconcile it with the L3g(a)-slice R3-fix (no exact nonlinear analogue).
11. **Checks.**
    - c20: disclose the 13:22:02 pre-run code edit.
    - c22: state Q2's lack of power at t ≤ 0.1, the non-t² deviations, and label the "S is a maximum" explanation as
      unverified.
12. **Scope (l.1765).** Add "(linearised)" to "no elliptic-regularity gap remains".
13. **Decision 4.** Obtain (or quote) the owner's delegation in the owner's own words. Until then keep the current
    honest label.

## Strategic verdict: the next target in the (DF) sub-DAG

**N2 first, specifically its linear half. N4 (abelian) as the short parallel item. N5 after N2 + N4. N6 last.**
- **N2 (soft L2).** It feeds N3, N5, N6, N8 and N10, so it has the largest fan-out. It is deterministic (tree level,
  no probability), and it has a template (CMP 102).
  - Its linear half would make BG-b-lin unconditional for the linearised chain:
    - existence and uniqueness modulo gauge;
    - Combes-Thomas exponential decay of the linear soft background map;
    - (H1) + (H2) from coarse data.
  - **The first lemma to prove is R_top ≤ C·(gauge-invariant coarse curvature of V)**, not ≤ C·|log V|.
    - c22's informational "mean residual ≈ 1.26t" cannot distinguish the two. On a 3⁴ torus with lowest-mode data,
      the field size and the curvature are the same order.
    - A c22-type control would settle it: V = (large pure gauge) × (small curvature). The residual should stay at the
      curvature scale.
    - If it does not, (H2) is not a small-field condition, and N2 as posed fails.
- **N4 (FP), abelian.** The A-independence of the Faddeev-Popov factor is "plausible, not written" (l.737-740). It is
  short and unblocks N5 together with N2.
- **N5.** Needs N2 (background) and N4.
- **N6** is the CMP 116 analogue. It is the largest, it needs N2 and N5, and it must deliver κ > 3κ_0 + 3 (fix 4). Do
  not start it before N2's linear half is done.
- Keep D4-obs on the list. It is not on the (DF) path, but the main theorem needs it.
