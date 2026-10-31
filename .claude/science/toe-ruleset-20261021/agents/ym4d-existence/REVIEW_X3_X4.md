# REVIEW_X3_X4: independent hostile review of sessions 3 and 4 of the YM4D existence lane

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session4_snapshot.md (`cmp` empty). §0-§3, §6, §10-§13 were read by offset.
  `diff session2 session4` and `diff session3 session4` were also read: session 4 changed only the title, the header, the
  tally lines in §0 and §6, §12.1 and §13, as it says.
- LOG.md sessions 2-4, NOTES.md sessions 2-4, REVIEW_X1_X2.md (all).
- checks/x3_criteria.md, x3_soft_rp.py, x3_out.txt, x3_time.txt.
- P = ../ym4d-proof/ (read-only):
  - RLARGE.md §0, §1, §1A, §6 (Lemma RS), §8.1-8.3 ((I_k), (PLD), RLF-step) and §11. The md5 is d41ec7fb…, matching
    EXISTENCE §13.9.
  - LINEAR_PACKAGE.md (frozen v1): header, §1.3, Proposition 6.4, Proposition 7.1.

Line numbers below are EXISTENCE.md lines unless marked.

No web access was used. Re-run conditions:
- nice 10, with OMP/OpenBLAS/MKL/vecLib threads set to 1.
- `uptime` load 2.2 (below 8); 35% of memory free.
- No `timeout` was used.
- Output: scratchpad `rerun_x3/`.

No file was edited other than this one.

**Bottom line.**
- **All 12 RX12 fixes are applied correctly, and the provenance labels match REVIEW_X1_X2's table.** Two §0 lines still
  name H-Bal-3T where the tally names H-sg.
- **The session-3 reduction is correct.**
  - H-Bal-3L ⇐ H-Bal-1 + H-loc-LF is right. One constant needs a factor of 2.
  - The full-law packaging and X-ND without (3b) are right.
  - H-Bal-3T needs H-sg, as stated. That "reduction" is nominal: H-sg is H-Bal-3T restricted to the small-field window.
- **The session-4 mathematics survives. No counted item is WRONG.**
  - **X-RP^S as worded is too broad.** "All sites of B(X) ∪ B(X + e_μ) strictly on the positive side" does **not** keep the
    ancestors on the positive side. A counterexample is given below. The fix is a continuum-support condition, and every
    downstream use already satisfies it.
  - Chessboard (CBE, CB, CB-sg) is correct. It needs RP through every plane between blocks, and X-RP^S supplies exactly
    those planes.
  - Lemma KN is correct. It does remove RS's linear δ_c loss, but only together with KN-step's re-centred dichotomy.
- **The merge claim is overstated in four places:**
  - (RLF-3^dis) is not yet "an instance" of RLF-3.
  - "Not Haar" also needs (F).
  - The Gaussian evidence offered for (PLD^mod_dis) comes from the other (deterministic) branch.
  - For the soft branch, (F) is not something Balaban states.
- **New structural finding.** For soft variables, the L² form of H-cont is **false**, and so is H-bl in L² form. Shifted
  grids carry independent kernel noise. So the soft branch's route to ker T = 0 must change.
- **§12.1 overclaims.** A rewrite is given word for word below.

---

## (1) The 12 RX12 fixes and the provenance labels

| Fix | Where | Verdict |
|---|---|---|
| 1 status HYPOTHESIS (new); labels | l.14-28; l.102-170, 688, 706, 922 | CONFIRMED. The labels match REVIEW_X1_X2 §1 row by row: H-Bal-1 SU(2) / SU(N) and M-uniform; H-Bal-2; (3a)-form; full-law packaging; (3b); 3G, 3L, 3T, loc. |
| 2 H-Bal-1 SU(N), M-uniformity | l.104-109, 359, 957-960 | CONFIRMED |
| 3 H-Bal-3: (0.28)-(0.30), regrouping, e^{±C_R}, η_0(m, ℓ), diagonal-pairing | l.79-80, 141-163, 193 | CONFIRMED |
| 4 X-ND constants; strike the q ∈ [1/3, 3] remark | l.368-383, 696-702 | CONFIRMED. q ∈ [1/3, 3] survives only as a hypothesis parameter of H-Bal-3L (l.694), which is legitimate. |
| 5 𝔄_∞ quotient, gauge lift | l.229-253 | CONFIRMED |
| 6 X-KER reverse inclusion | l.805-808 | CONFIRMED |
| 7 H-cont in L² two-grid form | l.507-515 | CONFIRMED (deterministic branch; see §5 for the soft branch) |
| 8 X-FLOW-NL torus zero; "X-RP does not apply" | l.301-303, 315 | CONFIRMED |
| 9 X-IVND gauge invariance and η_0; α ≤ ε_0/3 | l.430-438, 703 | CONFIRMED |
| 10 narrow l.714-718; 𝒦^⊥ = CΩ | l.868-876, 43, 345-348 | CONFIRMED |
| 11 §0 / §10.4 wording; LOG finding 1 | l.34-49, 949-975; LOG l.65 | CONFIRMED-WITH-FIX: l.35 and l.46 list "H-Bal-3T" as a session-3 hypothesis, but the tally (l.574) has H-sg; replace with "H-sg" in both places. l.48: X-IVND' also needs H-Bal-1 (M-uniform); add it. l.35 should also name session 4's (RLF-3^dis) and (PLD^mod_dis). LOG l.98 (session-2 tally "7") is unannotated (cosmetic). |
| 12 X-WIL novelty unverified; literature | l.764-765, 1177-1200 | CONFIRMED. The convexity remark re-derived: -E[S] = (log Z)′ ≤ (log Z(2β) - log Z(β))/β; it is correctly ARGUED. |

---

## (2) Session 3 (§11)

### Fact Ω (l.1012-1015): CONFIRMED
Only the plaquettes in N(b) move, by less than |s| + ε_0/3 < ε_0. Nothing else changes.

### BG-1L-lin (l.1049-1067): CONFIRMED
- **The argument.** It is an envelope argument: q ≥ 0 and q(0) = 0 give q′(0) = 0. The field B_k enters only through the
  top coupling.
- **Its place in the DAG.** It is a side lemma. No counted conclusion depends on it, since LF⇒3L uses BG-1L-B.

### BG-1L-B (l.1069-1075), POL-1L (l.1077-1085): CONFIRMED
- **The slice estimate.** It is right: a direction-v disc of radius α_1/2 around a point of the α_1/2-polydisc stays in the
  α_1-polydisc, so |∂_v f| ≤ 2S/α_1.
- **The counts.**
  - Scale-j cells at coarse distance r number ≲ (r + 1)^{d-1}(ML^jη)^{-4}.
  - The geometric j-sum is right.

### Theorem LF⇒3L (l.1087-1101): CONFIRMED-WITH-FIX
- **The probability step is right:** η_L ≤ 1/4 ⇔ g² ≤ a_P / log(8(d - 1)C_P).
- **The ratio step is right:**
  - the regular region, the polymer index set and 𝒵 are frozen;
  - the Y ∌ b terms cancel;
  - holomorphy and reality hold.
- **Fix (constant, l.1089, 1099).** "Y ∋ b" includes polymers that contain either endpoint cell of b. If b crosses
  between cells, Σ_{Y∋b} e^{-κd(Y)} ≤ 2K_0, not K_0. Put E_1 := E_bg + 2H_0K_0.
- **Wording (l.1101, 1121).** The text reads "γ ≤ min(α/2, e^{-p_*}, g_LF)". Since H-Bal-1 gives g_{m,K} ≤ g, the operative
  condition is g ≤ min(α/2, e^{-p_*}, g_LF). Write it that way, because γ is H-Bal-1's constant and not a free choice.
- **Substance caveat** (not an error). H-loc-LF's (P2) and (LF-b1) are themselves one-link *increment* bounds on each
  component.
  - "Nothing in H-loc-LF is a one-link density-ratio statement" (l.1044) is true, but most of H-Bal-3L's content has moved
    into (P2) and (b1).
  - What is genuinely derived is the local event G_b with its probability, and the assembly.
  - "One hypothesis instead of three" counts names. H-loc-LF has nine parts: (P1)-(P4), (b1)-(b3) and (LF-P).

### Corollary LF⇒3 (l.1105-1118): CONFIRMED
- **(ii)** 𝒵 ≤ e^{(E_+ + C_+)|Λ_m|} follows from A ≥ 0, (P4) and (b2), and needs no ν(R) bound. X-ND is correctly re-proven
  without (3b).
- **(iii)** The split is right, given the monotonicity condition on g_T.
- **H-Bal-3T needs H-sg: CONFIRMED.**
  - H-sg (window bound g²/2) is H-Bal-3T on the window {g p(g) ≤ |V_p - 1| < ε_0/3} with a factor of 2. So "3T ⇐ LF + H-sg"
    trades a hypothesis for a slightly sharper restriction of itself.
  - §11.7 says "not reduced", which is honest. The tally line "replaces 4 new hypotheses by H-loc-LF + H-sg" should add
    "(H-sg is H-Bal-3T on the small-field window)".

### X-IVND' (l.1120-1127): CONFIRMED
Portmanteau for the open set and the gauge invariance of |V_p - 1| are both right.

### §11.5 (D1-D6), §11.6: CONFIRMED (accurate comparison; literature correctly tagged).

---

## (3) Session 4 (§13)

### Setting S, (L), (C) (l.1310-1335): CONFIRMED
- **The class tree.** Its parent structure is right. θa = 2c - a ∈ L^{-K}Z^4 for K ≥ m_0.
- **The kernel reflection identities.** I re-derived them:
  - Re tr(V M̄^†) = Re tr(V^{-1}M̄) for unitary V;
  - 𝒩(M̄^†) = 𝒩(M̄), by V ↦ V^{-1} and inversion invariance of Haar measure.
- **Contour-set covariance** is P's L9a′, which is imported and reviewed in P.

### Theorem X-RP^S (l.1339-1352): CONFIRMED-WITH-FIX (the statement is too broad)
- **What survives.** The integrate-out argument is correct:
  - A_+ is closed under ancestry, so a variable outside A_+ ∪ A_- has no child in it, and coarsest-first integration with
    ∫k = 1 is exact;
  - (C), together with Haar invariance under inversion, turns the A_- integral into θ(F̃)^*;
  - X-LRP finishes.
  - **The normalisation 1/𝒩(M̄_c) is harmless here.** It is a function of A_+ ∪ {positive fine links} only, so it travels
    with F̃.
- **The gap: the proof's step "By (L), every variable in A_+ has its cells on the positive side" (l.1345) is false for
  the class defined at l.1341-1342.**
  - **Counterexample** (L = 3, time coordinate):
    - Take Π: x_0 = 5.5/9 ∈ P_2.
    - Take a resolution-0 link (X, X + e_ν), with X_0 = 1 and ν spatial. Its cells consist of resolution-1 sites with
      x_0 ∈ {2/3, 1, 4/3}, all > Π. So it qualifies for 𝔉^S_+.
    - Its parent link at x_0 = 2/3 has a kernel that depends on resolution-2 sites at x_0 ∈ {5/9, 6/9, 7/9}, and
      5/9 < Π.
    - So the ancestors cross Π, and the proof does not apply.
  - The same happens for every shifted class, since the shifted block boundaries are not in P_{m_0}.
  - Whether RP actually fails for such F is not decided here. The theorem as stated is unproven.
- **Fix (binding).** Replace "whose cells (all sites of B(X) ∪ B(X + e_μ)) lie strictly on the positive side" with
  **"whose continuum supports supp(c) := the closed union of the continuum cubes of B(X) and B(X + e_μ) (side L^{-n}, centred
  at X, X + e_μ) lie in the open positive half-space"**.
  - Nesting (L odd) maps parent supports into child supports, so ancestors then stay positive down to fine links. Fine sites
    never lie on Π.
  - Define 𝔄_+ for X-OS^S/X-KER with the same condition. It is translation-stable.
  - All downstream uses satisfy it: level-k links interior to a level-k cube (CBE, CB, CB-sg), and τ_s of such generators
    (X-OS^S).

### Site planes and x3 B1 (l.1353-1359): CONFIRMED
- **Why the proof fails.** The cell of an in-plane link straddles Π, and 1/𝒩 does not factor as G·θ(G).
- **Why B1's -0.195 is a genuine RP violation in the toy.**
  - The Gram matrix runs over *all* functions of (σ_0..σ_3, φ_A, φ_B), where the plane spins are θ-fixed.
  - The fine marginal is unchanged by the normalised kernel.
  - B2's PSD result isolates 𝒩 as the cause.
- The licensed wording ("fails for the normalised kernel in that toy") is respected.

### Soft-layer transfer (l.1360-1369): CONFIRMED-WITH-FIX
- **What checks out.**
  - X-CONS^S is Markov-projective in the correct direction: ν_m = ν_{m+1}K. The limit uses a diagonal subsequence in g′_m
    and joint continuity.
  - Gauge covariance at the roots holds, because nested sites are block centres.
  - X-SYM^S, X-IV^S and X-2GRID^S hold.
- **Fix: the class definition.** Use the corrected class.
- **Fix: what "X-OS^S and X-KER hold verbatim" leaves out.** The statement is true as implications, but see §5: for soft
  generators, the sufficient conditions X-KER (ii) and (iii) are unsatisfiable in their L²(ω) form. Say so here.

### Proposition KB (l.1373-1384): CONFIRMED (kernel only)
- The bracket lies in [0, 2], so 𝒩 ≤ 1 and k ≥ e^{-2κ/g′²}.
- The upper bound uses P's D4-norm (2): with V_0 the maximiser, k ≤ e c_N^{-1}(κ/g²)^{N²-1}. The bound is imported from P;
  name it in the dependency list.
- The entire extension is right.
- c_- is volume-dependent; the text says so (finite volume).

### Proposition LAP^S (l.1386-1403): CONFIRMED (kernel only)
- **The derivation.**
  - I re-derived a(s) = (κ/2N)[tr(V^{-1}(1 - e^{-sX})M̄) + tr(M̄^†(1 - e^{sX})V)], with
    |a| ≤ κ||1 - e^{±sX}||_HS/√N ≤ κ(e - 1)/√N.
  - The rest follows: H-Bal-3L holds exactly for ρ_U; LAP-1; δ^S_* = r_*²/(2N).
- **The "no Wilson-measure information" label is correct and adequate** (l.1398-1403). See §4 for three places where it
  leaks.

### Lemma CBE (l.1407-1434): CONFIRMED (proof checked); label fix
- **Step (0).** Composites of reflections mapping 0 to i are unique, so f^{[s]} is well defined and θ(G^{[i]}) = G^{[θi]}.
- **Step (1).** The Schwarz inequality gives Z(G)² ≤ Z(G′)Z(G″). The denominators factor exactly. Maximisers are closed
  under the operation.
- **The run-doubling argument is right.**
  - If ℓ ≥ n, the kept half is all run, so mirroring gives the constant tuple.
  - If ℓ < n, the run doubles.
  - The ε-shift is legitimate because 1 ∈ 𝔅_t.
- **Step (2).** It is standard.
- **RP availability.** CBE needs RP through every plane between block layers in every direction, plus the antipodes.
  - For level-k cubes these are the planes P_{K-k-1}, plus P_{K-k} after a level-k shift.
  - All lie in P, so corrected X-RP^S supplies them. Blocks per direction: 4L^{M+K-k-1}, which is even.
  - Reflections in P_{K-k-1} fix the main class at resolutions ≥ K - k - 1, which is all that 𝔅_t uses.
  - P_K is θ-invariant (all classes included).
- **Label fix.** IMPORTED-AND-REVERIFIED requires an "exact source" (l.17). FILS and Shlosman were not read, and Biskup was
  read only at the abstract. Relabel as **PROVEN-HERE (standard result; proof written out and checked; sources not
  read)**.

### Theorem CB (l.1436-1447): CONFIRMED
- **Interior plaquettes.** For interior plaquettes, 1{Q bad}^{[s]} = 1{s bad}. ||1 - W||_op is invariant under inversion
  and conjugation.
- **Non-interior plaquettes.** The level-k shift preserves the law of (U_0, …, U_k). The shifted cube boundaries
  b + (j + ½)L^{-(K-k-1)} lie in P_{K-k}, as checked.
- **Deterministic branch.** The remark at l.1446 is right: X-RP covers bounded measurable indicators at finite K via
  X-LRP.

### Corollary X-IVND^S (l.1452-1456): CONFIRMED-WITH-FIX
- **The bound is correct:** Portmanteau for the open set, and CB at k = K - m.
- **Fix (l.1455-1456).** The sentence "Together with Proposition KB (not flat), the soft limit is neither flat nor Haar …
  given (RLF-3^dis) alone" pairs a kernel artefact with the informative half.
  - Write instead: "not Haar, given (RLF-3^dis) and (F); not flat for every law of the fine field (kernel, no Yang-Mills
    content)".
  - (F) is needed because (RLF-3^dis) is quantified "within (F)" and the bound needs g^S_m small.

### Lemma MIX (l.1478-1484): CONFIRMED (lemma); application GAP
- **The lemma.** Cauchy-Schwarz is correct.
- **The claim "D3 is not needed" (l.1478) and "D3 dissolved" (l.1595) overclaim.** MIX replaces D3 with a weaker but
  still unsupplied input:
  - a **nonnegative** history mixture, ρ = Σw_hρ_h with w_h ≥ 0;
  - with **per-history** pair inequalities on a **common** G_b.
  - RLF's (I_k) supplies neither: ℒ_𝔥 is bounded in modulus only, and no per-history one-link bound is stated.
- **Fix.** Write: "D3 is reduced to: a nonnegative history representation with per-history pair inequalities (not
  supplied by RLF); for the soft branch D3 does not arise."

### Lemma KN (l.1502-1514): CONFIRMED-WITH-FIX (precision)
- **I re-derived it.**
  - R = Σw(e^{-X̄} - 1)(e^{X_i} - 1) + (e^{-X̄} - 1 + X̄) + Σw(e^{X_i} - 1 - X_i).
  - ||R|| ≤ δ²(e^{2δ} + e^δ) ≤ 2.93δ² at δ = 1/4.
  - Re tr(1 - Z^{-1}) = ½x², and the HS cross bound holds.
  - D4-norm (2) at the maximiser V_0 holds, with Re tr V_0^{-1}M̄ ≥ Re tr W′^{-1}M̄.
- **The claim at l.1513 is true, with a qualification.** It removes RS's linear δ_c loss only together with KN-step's
  re-centred dichotomy:
  - (R4) bounds ||V_c - S_c||, and KN bounds ||V - W′||;
  - re-centring at W′ re-introduces a linear term ||W′_c - S_c|| ≤ e^δ - 1 into the plaquette bound;
  - so the gain is η_1: from min{ε_1/(2L²), ε_1²/(512NA_d)} (quadratic in ε_1) to c_1ε_1, with c_1 = 1/(2(L² + 5.5A_d))
    (linear).
  - This is slightly worse than RLARGE §11 item 7's hoped-for O(ε_1/L²).
  - The step δ ≤ (π/3)A_dη also needs A_dη ≤ 1.
- **Fix.** State this at l.1513-1514.

### Corollary KN-step (l.1516-1526): CONFIRMED
- **Constants re-derived.**
  - 4(e^δ - 1) ≤ 4.76A_dη ≤ 5.5A_dη.
  - t/8 ≥ 12√Nδ² ⇐ t ≤ 1/(105.3√NA_d²c_1²); the text's 106 is conservative.
  - c_1 = 1/117.
- **The final claim** needs g_k ≍ g_{k+1}, which (F) gives.

### Theorem CB-sg (l.1528-1538): CONFIRMED-WITH-FIX
- **The geometry is right.**
  - Super-block boundaries are cube planes, and become P_{K-k} planes after the shift.
  - There are 2L^{M+K-k-1} super-blocks per direction, which is even.
  - A plaquette at distance ≥ 2 from the boundary has disjoint 1-neighbourhoods across copies.
  - The term 16·P(E_all)^{1/N_k} comes from CB on the shifted cubes.
- **Fix 1 (l.1534).** "P_cut … (RLARGE's all-cut measure)" is a misidentification.
  - Here P_cut is the true law conditioned on all *shifted* cubes being good. It equals the shift of the law conditioned on
    the standard cubes, by translation invariance; say so.
  - RLARGE's all-cut measure (§8.2 (PLD)) is the per-history small-field measure of (I_k) on Λ(𝔥).
  - Passing from one to the other is the ARGUED "mixtures over histories" step. It needs nonnegative history weights, and
    p′ ∈ A_p inside the large-field regions of 𝔥 is not covered.
  - Replace the parenthesis with "(the true conditional law; RLARGE's (PLD) concerns the per-history all-cut measure of
    (I_k), and the passage is ARGUED)".

### (PLD^mod_dis) and Corollary H-Bal-3T^S (l.1540-1551): CONFIRMED (implication); evidence GAP
- **The implication is right:** τ = g p(g)/√N; C_m e^{-a_m p²/N} ≤ g²/2 ⇔ 2p_* > 1; |·|_HS ≤ √N||·||_op; φ(g^S_m) ≤ φ(G_m).
- **GAP in the supporting evidence (l.1557, 1576; LOG l.206).** "The Gaussian instance holds by layer 1's A2" is a
  statement about **deterministic** averaging (LINEAR_PACKAGE Prop. 7.1: "linearised S4′ levels"). It is not about the
  soft chain that this branch uses.
- **For the soft chain the free instance is open, and the text itself notes the danger** (l.1558-1560). The crude
  recursion accumulates Σ_j g_j²/κ ≈ log(K/m)/(κβ_- log L) at fixed resolution m, which diverges as K → ∞.
- **What would rescue it.** If the symbol-level cancellation (injected link noise has curvature symbol O(p²)) fails, then
  soft block plaquettes drift toward Haar as K → ∞. In that case (RLF-3^dis) and (PLD^mod_dis) are **false** for the soft
  chain, and the soft branch collapses.
- **Fix.** Say "no instance of (PLD^mod_dis) is established for the soft chain, even in the free Gaussian case". This is
  the cheapest decisive next check.

---

## (4) The merge table (l.1489-1498) and (RLF-3^dis)

**Does the soft existence theorem rest only on (RLF-3^dis), (PLD^mod_dis), (F)?** CONFIRMED-WITH-FIX.
- **Hidden inputs to list:**
  - X-LRP (Osterwalder-Seiler);
  - P's L9a′ contour covariance (for (C));
  - P's D4-norm (2) (for KB, KN, KN-step);
  - smallness: g ≤ g_T, g′_m ≤ 1/2, g² ≤ κ.
- **The "not Haar" row omits (F).**
- **Neither layer-1 inductive hypotheses nor H-loc-LF is used silently.** I found no use of (SF), (PLD), (W1-ret′) or
  (HIST) treated as RLF. (PLD^mod_dis) is a separately named hypothesis, which is correct per T8's "Not success" rule.
- **(F) is not Balaban's for this branch.** In the soft branch, (F) is a property of the soft scheme's effective couplings:
  RLARGE §0, "OPEN as A5". As an inequality on a chosen sequence it is satisfiable by fiat; its content enters only through
  the other hypotheses holding for that sequence.
  - Label: **plausible extension of H-Bal-1 (different RG scheme; layer-1 node A5, OPEN)**.
  - It is not "Balaban states it" (see §12.1).
- **"Rests on RLF" (l.1496) means it rests on an OPEN layer-1 target.**

**Is (RLF-3^dis) honestly an instance of RLF-3 (§1A)? Not as stated: GAP (wording).**
- **What §1A says.** Its (RLF-3) bounds "weights" of unreturned defect configurations in a representation of Z_K^{ren}.
  It says nothing about:
  - (i) what the weights are normalised against;
  - (ii) whether they are nonnegative;
  - (iii) whether the bound holds for the sum over all finer- and coarser-level histories compatible with E_all.
- **Assessment of the reading.** It is natural: E_all is the single term Πζ_Q of the χ/ζ partition, n = N_k > n_♯, and
  session 18's Z_K^{ref} with |T| ≤ L⁴N_k absorbs e^{E′_-|T|}.
- **But the route uses more than RLF-3.** It also uses (RLF-1), (RLF-4) and node A's lower bulk bound Z_K/Z_K^{ref} ≥
  e^{-E′_-|T|} (l.1616 says so). Those are also OPEN.
- **§13.5 and §13.9 are honest.** The overclaims are elsewhere:
  - §0 l.60: "an instance … under a normalisation reading". This is acceptable only if "(reading not adopted by layer 1)"
    is added.
  - l.1494, l.1496: "= RLF-3", "one instance of RLF-3".
  - §12.1: "this is one instance of a large-field bound targeted by our sister lane".
- **Fix.** "Would follow from layer 1's (OPEN) RLF-3, together with (RLF-1), (RLF-4) and node A's bulk bound, **if** RLF-3's
  weights are read as nonnegative ratios Z_K[𝔥]/Z_K^{ref}, which RLF does not state." Also note the notation clash: in
  l.1450, "g_K ≤ g_0" means RLF's threshold g_0, not the bare coupling of ES3.

**Kernel-only bounds labelled as having no Yang-Mills content.** The labelling is correct and adequate at l.1398-1403,
l.1493 and §0 l.60. It leaks in three places:
- l.1455 and LOG l.198: "neither flat nor Haar", with "not flat" from the kernel.
- l.1496: "non-triviality statements 'neither flat nor Haar'".
- §12.1: "so the limit is not scale invariant".
  - For the soft variables, this uses the kernel's lower bound at m = 0, and the kernel couplings are a scheme choice.
  - Even a frozen fine field (U_0 ≡ 1) would give ⟨1 - P⟩_m ≍ g′_m² ~ 1/m from injected noise alone. So non-scale-invariance
    of the soft family carries no Yang-Mills information.
  - The informative statements are "not Haar" and the upper bound (approach to flat at fine resolution, at least
    logarithmically fast).

---

## (5) New finding: H-cont and H-bl in L² form fail for soft variables (GAP; strategic)

- **The mechanism.** For a ∈ L^{-n}Z^4 \ L^{-m}Z^4 (n > m), the shifted and unshifted resolution-m soft variables
  V^{(m),S}_a and V^{(m),S}_0 lie on different branches of the class tree. Given their parents, they are drawn
  independently.
- **The consequence.** E|F(V_a) - F(V_0)|² ≥ 2E[Var(F(V_0) | parents)]. For F a block plaquette, this is ≥ c g′_m²
  (LAP^S-type anti-concentration), uniformly as |a| → 0.
- **So H-cont (l.507-509) is false in the soft branch.**
- **H-bl in L²(ω) form fails for the same reason.** A soft generator touching Π_0 carries its own kernel noise, which no
  element of 𝔄_{++} can approximate in L².
- **What survives.** X-KER (i) holds, and (ii)-(iii) hold as implications, but their hypotheses are unsatisfiable here.
- **What should replace them.** By the X-RP^S computation, OS inner products see only F̃ = E[F | fine field]:
  ⟨F, G⟩_OS = E[θ(F̃)^*G̃].
  - So 𝒦 = {0} for soft variables must be sought in the **OS seminorm** (via F̃), not in L²(ω).
  - Alternatively, take the time-continuity statement from the deterministic branch.
- **Where to record it.** §13.2 and the T8a outcome should state this; X-2GRID^S's "exact by construction" is true but
  useless for H-cont.

---

## (6) Check x3: re-run and audit

- **Re-run** (nice 10, threads 1, load 2.2, 35% free memory, no `timeout`).
  - **Output is byte-identical** to x3_out.txt (`diff` empty).
  - 3.70 s wall; peak 91.9 MB.
- **Pre-registration order** (mtimes): criteria 18:18:30 < script 18:18:58 < out 18:19:14 < time 18:19:23. §13.0 is stamped
  22:15 UTC (18:15 local). Consistent.
- **A (block-boundary RP).**
  - The Gram matrix correctly realises ω(θ(F)F) over all functions of the positive variables (θx = 5 - x; blocks map to
    blocks).
  - PASS, -9e-16.
  - It is a one-level toy, so it **cannot probe the X-RP^S ancestor gap** of §3, which needs two levels or shifted
    classes.
- **B.**
  - Construction: the row index (s0, s5, s4, s3, φ_A, φ_B) is θ of the column index (θx = -x).
  - B2's factorisation over the θ-fixed (σ, φ) is the pre-stated reason for B2 being PSD.
  - B1's -0.195 is valid.
- **C.**
  - **Weakness of the test.** The script tests ||R|| ≤ 3δ² with δ the sampling bound, not δ := max||X_i||. Since
    max||X_i|| ≤ δ, this is a weaker test than the lemma.
  - **The discrimination claim stands.** Measured against the true δ, the ratio would be larger.
  - PASS stands.
  - Minor fix for the record: compute δ as max||X_i||_op.
- **Verdict.** PASS as reported. No counted claim rests on x3 beyond what the written proofs carry.

---

## (7) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| Fact Ω, BG-1L-lin, BG-1L-B, POL-1L, Corollary LF⇒3, X-IVND′, Prop. KB, Prop. LAP^S, Lemma CBE (proof), Theorem CB, Corollary KN-step | CONFIRMED |
| Theorem LF⇒3L (constant 2H_0K_0; g-condition wording) | CONFIRMED-WITH-FIX |
| Theorem X-RP^S + soft-layer transfer (class too broad; counterexample; continuum-support fix) | CONFIRMED-WITH-FIX |
| Corollary X-IVND^S (add (F); separate kernel-only "not flat") | CONFIRMED-WITH-FIX |
| Lemma KN (re-centring precision on the RS claim) | CONFIRMED-WITH-FIX |
| Theorem CB-sg / Corollary H-Bal-3T^S (P_cut identification) | CONFIRMED-WITH-FIX |
| Lemma MIX | CONFIRMED (lemma); "D3 dissolved" = GAP (overclaim) |
| (RLF-3^dis) "an instance of RLF-3" | GAP (wording; ARGUED reading only) |
| (PLD^mod_dis) "Gaussian instance holds" | GAP (wrong branch; soft free case open) |
| Soft H-cont / H-bl in L² form | GAP (new: false for soft variables) |
| §0 l.35, l.46 (H-Bal-3T vs H-sg) | WRONG label (cosmetic) |
| §12.1 public statement | GAP (overclaim; rewrite below) |

**Tally.**
- **Claimed:** 36 / 2 / 3 / 5 / 10.
- **Corrected:** **PROVEN-HERE 37 / IMPORTED-AND-REVERIFIED 1 (X-LRP) / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5
  / OPEN 10.**
  - Lemma CBE is relabelled to PROVEN-HERE (standard; sources not read).
  - All 37 survive as implications; 6 of the 12 session-3/4 counted items need local fixes.
  - The H-Bal-1 entry must carry the soft-scheme (F) as a *plausible extension (layer-1 A5, OPEN)*.
  - ARGUED stays 10. "D3 dissolved" becomes ARGUED-reduced, and is not counted.
- **Substance.** Of the 12 new counted items, 2 are kernel-only: KB and LAP^S, with no Yang-Mills content. One, BG-1L-lin,
  is off the main DAG. The substantive new items are LF⇒3L (with BG-1L-B and POL-1L), X-RP^S, CB/CBE, CB-sg and KN.

---

## Binding fixes for session 5

1. **X-RP^S** (l.1341-1342, 1345): define 𝔉^S_+ and 𝔄_+ by continuum supports, as in §3. Add the L = 3 counterexample to
   the old wording as a remark.
2. **§13.2** (l.1367-1368): add that X-KER (ii)-(iii) cannot be met in L² form for soft generators (§5). The soft route to
   𝒦 = {0} is the OS seminorm via F̃.
3. **Lemma CBE**: relabel as PROVEN-HERE (standard; FILS/Shlosman not read; Biskup abstract only). Update the tallies in
   §0, §6 and LOG.
4. **l.1455-1456, 1494-1496, LOG l.198**: give the soft "not flat" as kernel-only. Write "not Haar | (RLF-3^dis), (F)".
   Add X-LRP, L9a′ and D4-norm (2) to the merge table.
5. **(RLF-3^dis) wording** at l.60, 1494, 1496, 1544, §12.1: "would follow from the OPEN RLF-3 (+ RLF-1, RLF-4, node A)
   under the nonnegative-ratio reading, which layer 1 has not adopted". Rename RLF's threshold in l.1450 (e.g. g_RLF) to
   avoid the clash with the bare coupling g_0.
6. **l.1534**: correct the P_cut identification (true conditional law, shifted grid; the per-history passage is ARGUED).
7. **l.1557, 1576; LOG l.206**: say that the A2 Gaussian instance is for deterministic averaging. For the soft chain the
   free instance is open, and the log-divergent crude bound is a falsification risk.
8. **l.1478, 1595**: "D3 reduced to a nonnegative history mixture with per-history pair inequalities (not supplied by
   RLF)", not "dissolved".
9. **l.1513-1514**: qualify the Lemma RS claim (re-centred dichotomy needed; η_1 becomes c_1ε_1; A_dη ≤ 1).
10. **l.1089, 1099**: E_1 := E_bg + 2H_0K_0. **l.1101, 1121**: state the conditions on g, not γ.
11. **§0 l.35, l.46**: H-Bal-3T → H-sg. **l.48**: add H-Bal-1 (M-uniform) to X-IVND′. Label the soft (F) as a plausible
    extension (layer-1 A5).
12. **Replace §12.1 by the statement below.**

---

## Public-statement verdict: GAP. Replace §12.1 with this text, word for word

> For four-dimensional SU(N) lattice Yang-Mills theory with the Wilson action, we give a conditional argument, checked
> only by internal reviews and not peer reviewed, with the following content. Unconditionally, by compactness and
> Osterwalder-Seiler reflection positivity (standard arguments), along subsequences of lattice spacings L^{-K} → 0 the
> lattice measures define limit states on a separable algebra of block variables at every L-adic resolution and shift
> and of gradient-flowed lattice Wilson loops. Two kinds of block variables are treated: a continuous, gauge-covariant
> block average, and the variables of a soft renormalisation-group Markov chain with normalised Gaussian-type kernels.
> For both, the limit states are consistent across resolutions, reflection positive for every L-adic block-boundary
> hyperplane (for observables supported on one side), invariant under L-adic translations and the hypercubic group, and
> yield an Osterwalder-Schrader Hilbert space with a positive self-adjoint generator H on the orthogonal complement of
> the kernel of the transfer operator; that complement may be one-dimensional, in which case H is trivial. For the soft
> variables, the limit block laws have analytic densities and fluctuate at least at the scale of the kernel coupling;
> this is a property of the kernel alone and says nothing about the Yang-Mills measure. For the continuous block average,
> under a coupling-flow hypothesis 1/g_m² ≈ 1/g² + O(m log L), uniform in the volume, which Balaban states for SU(2)
> for his renormalisation group with its proof deferred and not seen by us, and a large-field localisation hypothesis on
> the block laws that no published work states, the limit block plaquette satisfies ⟨1 - P⟩_m ≥ c/(1/g² + β' m log L),
> uniformly in the volume, and the limit is neither flat nor Haar at any resolution. For the soft variables, under the
> analogous coupling-flow hypothesis for the soft scheme (open) and an unpublished, volume-uniform bound of order
> e^{-a/g_k²} per block on the probability that every block at a given scale is a large-field block (a bound that would
> follow from a large-field theorem our sister lane is attempting, under a normalisation that lane has not yet adopted),
> the soft limit is not Haar at any resolution, uniformly in the volume; the local bound is derived from the extensive
> one by chessboard estimates. With a second unpublished hypothesis of the same extensive kind (a moderate-deviation
> bound for the small-field measure, for which no instance is established for the soft chain, even for free fields),
> also ⟨1 - P⟩_m ≤ C (log m)^{2p}/m for the soft block plaquette. Time continuity (kernel of the transfer operator = 0),
> Euclidean invariance, the OS regularity axiom for local fields, uniqueness, clustering and a mass gap are not
> established. This is not a construction of Yang-Mills theory, and it does not rest on any published large-field
> theorem.

Changes from the lane's §12.1:
- "unreviewed" becomes "internal reviews only".
- "one sided" is added for RP.
- "bounded" is dropped (the bound is volume-dependent).
- The deterministic statements are spelled out, with the flow attributed to Balaban's own RG.
- For the soft branch, the flow is labelled open.
- (RLF-3^dis) is described as conditional on a reading layer 1 has not adopted.
- The missing free-field instance of (PLD^mod_dis) is stated.
- "so the limit is not scale invariant" is deleted, because for soft variables it rests on the kernel lower bound.

---

## Strategic verdict

- **What is real.** Session 4's chessboard bridge is real and portable.
  - RP for every block-boundary plane, plus an even torus, turns one extensive (disseminated) large-field bound into local
    probability bounds.
  - It also removes the localisation problem of H-sg. That idea is standard in statistical mechanics (FILS), but its use
    on RG block variables is the lane's best new mechanism.
  - X-RP^S, with the support fix, is the correct merge point with layer 1.
- **Three risks dominate, in order:**
  1. **Viability of the soft variables.** Accumulated kernel noise may diverge logarithmically at fixed resolution
     (l.1558-1560). If so, (RLF-3^dis) and (PLD^mod_dis) are false and the soft branch's informative half collapses.
     - **Next session's first target:** the free Gaussian soft linear chain. Prove (or refute) the uniform operator-norm
       bound on the resolution-m curvature covariance by symbols: injected link noise has curvature symbol O(p²). Then
       prove (PLD^mod_dis) there by the Gaussian argument of l.1554-1556.
     - This is cheap, exact and decisive. It is also checkable numerically (pre-registered x4).
  2. **Layer-1 alignment.** Ask layer 1 to adopt RLF-3 in the ratio form Z_K[𝔥]/Z_K^{ref} ≤ Π(Ce^{-a/g²})^{n} (one sentence
     in §1A). Until then, the soft "not Haar" rests on a reading.
  3. **𝒦 = {0}.** For soft variables the L² route is dead (§5). Restate H-bl in the OS seminorm via F̃ = E[F | fine field],
     or take time continuity from the deterministic branch.
     - Either way, this is still the lane's largest gap toward an OS reconstruction that is not vacuous.
- **What not to do.** Do not spend effort on (W-lc) / log-concavity before risk 1 is settled. Do not headline X-WIL, KB or
  LAP^S.
