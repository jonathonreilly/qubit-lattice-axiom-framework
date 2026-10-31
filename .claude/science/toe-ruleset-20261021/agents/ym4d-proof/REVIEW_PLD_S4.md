# REVIEW_PLD_S4: hostile review of lane E session 4 (PLD.md §16: Theorem NA-PRICE, the wall (J-NS^dir), a_ret, K12, check p4)

Reviewer: an independent agent. I wrote none of PLD.md and edited no file except this one. No commits, PRs or pushes.

Inputs. Line numbers are PLD.md's at mtime 2026-10-28 06:35:23 local (10:35:23 UTC): 1606 lines, md5 def1982d61cccacf3fb1d3df7e86d446.
- PLD.md §16 in full (l.1291-1606).
- PLD_LOG.md, session-4 block (l.53-68).
- REVIEW_PLD_S3.md (format).
- REVIEW_RLARGE_V3.md: S-1 to S-6 (l.95-170), §3.4 K12 (l.246-262), top 3 and required fixes (l.380-420).
- RLARGE.md: §3 row (SDP)^A (l.392-404); App. A §6 Lemma RS (l.964-990).
- HW.md:
  - tower energies and Lemma TE (l.160-200);
  - §13.1 relaxed family, (m1), Lemma DECL (l.600-632);
  - §15 SAT, CAP-dec, LOOP-div, LOOP-const (l.767-850);
  - §18.1 (SDP)^A re-ownership (l.926-1000).
- REVIEW_HW_S2.md §5 (l.280-385): extraction, not cross-level pricing.
- checks/p4_criteria.md, p4_pld.py, p4_out.txt, p4_time.txt. I re-ran p4 (Part 5).

Scratch files are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/rerun4/`.

---

## Bottom line

1. **The four lemmas are right.**
   - Lemma FT: CONFIRMED. The proof actually gives e^{2c_T}; the stated e^{4c_T} is a safe overstatement.
   - Lemma FV-law: CONFIRMED, with a scope fix (S-4).
   - Lemma KD: CONFIRMED. I re-derived the KS (c) Chernoff from monotonicity of b^{3/2}𝒩(b).
   - Lemma CW: CONFIRMED as CONDITIONAL ⇐ (CLS-min), with one wrong sentence in its "Reading".
   - The implication NA-PRICE (i) ⇐ (LI^U) + (CLS-min) + (SF-cap)^{A,+} + (J-NS^dir) is valid as a piece of logic.
2. **The architecture is the one REVIEW_HW_S2 ruled out. It is not a new route.**
   - NA-PRICE (i) never uses node A's R-operated representation. It uses neither (I_{k-1}^E)′ (two-field form), nor
     (W1-ret′^J)_{k-1} (c), nor (SC)_{k-1}, nor R1^J's gas. RLARGE v3 l.398-404 and HW §18.1 list all four as the inputs of
     (SDP)^A.
   - Instead it splits the raw relaxed law μ_R along the raw finer-defect indicator G^c_Q. It then hands the coarse cube on
     a column with a returned defect to a hypothesis, (J-NS^dir).
   - That is the cross-level price of a coarse defect against a returned finer defect in its column. Its trivial bound is
     LOOP-const, as Proposition WALL (a) itself shows. "LOOP-const respected" (l.1428) holds only because the cross-level
     content has been moved into the hypothesis.
   - The cause sits in the pre-statement. §16.0's list of allowed inputs (l.1314-1315) leaves out the R-operated
     representation. With those inputs, NP-F1 ("LOOP-const in a new guise") is the outcome actually met.
3. **"PARTIAL SUCCESS" does not meet the pre-stated bar (binding).**
   - The bar (l.1317-1319) asks for a hypothesis that is shown strictly weaker than (SDP)^A, or of a different kind
     (single-level, deterministic or small-field).
   - (J-NS^dir) is two-level, probabilistic and large-field. The file concedes it is "not shown to be strictly weaker"
     (l.1567).
   - Reclassify T9 (i) as **NP-F1 MET, plus a valid conditional implication**.
4. **"K12 decided: the requirement is not needed" (l.1523-1527, 1585-1586) is not established.** The requirement has moved
   into (J-NS^dir)'s hypothesis a_ns ≥ θa_bad.
   - Proposition CC shows a returned cluster has no exponential price of its own on the cut-good domain.
   - So the price of the event 𝒞 ∩ G^c has two possible sources. Either it comes from the coarse centre, which needs the
     extracted-completion argument of Part 3. Or it comes from the cluster, and then a_ns is bounded by an in-step
     returned price of a_ret type, ≈ 8·10⁻⁷a_bad. In the second case K12's requirement returns.
5. **A wrong constant placement (binding).**
   - In §16.7, c_f := 2c_U(1 + Δ_sh) multiplies the union-form depth term by Δ_sh ≈ 3.07·10⁶ (l.1469, hence c_A at l.1409).
   - Δ_sh is a depth-free per-cube excess. It belongs in c_sf: c_sf = e^{2c_U(81+Δ_sh)}c_lcr and c_f = 2c_U.
   - Separately, the delivered shadow coefficient c_A ≥ 6c_U is not the target's 2c_U (l.1306). This deviation is not
     disclosed.
6. **(iii) a_ret.**
   - The formula and the numbers are right. I re-derived 4.465·10⁻¹³ε_1², 8.03·10⁻⁷a_bad, 2.00·10⁻⁹¹ and the 10⁻⁹⁴ ceiling.
   - Proposition CC (a) is CONFIRMED.
   - "(NP-F2) MET" is mislabelled. CC does not touch (SC)_k's own domain, which is stated sup over the chart; the file says
     so at l.1507. The sea-averaged counterexample is ARGUED only.
   - Relabel: "frozen counterexample to (SF-irr)'s off-chart clause PROVEN; sea-averaged ARGUED; (SC)_k unaffected".
7. **p4.**
   - My re-run is byte-identical to p4_out.txt.
   - The E1 criterion defect (exact vs rounded c_pr) is honestly disclosed in three places.
   - One residue: §16.10's "nothing was re-run or edited" (l.1549) omits the post-run phrase edit at l.1411-1412, which
     PLD_LOG l.67 does record.

---

# PART 1: Lemmas FT, FV-law, KD, CW (priority 1)

## FT (l.1344-1361): CONFIRMED (the constant can be sharpened to e^{2c_T})
- **Step (1).** On {T ⊂ D_k} the indicators agree, 1_R = 1_{R′}: declared cubes count as defects, D ∪ E = D ∪ E′.
  - (m1) gives R′ ⊂ R, so Z(R′) ≤ Z(R).
  - Together: E_μ[1F] ≤ E_{μ′}[1F]. This is DECL with F riding along. Correct (HW l.620-627).
- **Step (2).** μ′ restricted to U_{≤k} equals ν′ tilted by H′.
  - Integrating U_{>k} out of e^{-S_0}ΠK_iΠ1_{R′,j} leaves exactly ∫K_k·1_{R′,k+1}·h_{k+1}.
  - This needs every 1_{R,j} to read U_j only, which holds for bad-only defects (R_{S,E} is a per-level *-component
    condition).
  - ℓ(T) is read by T's windows, so (LI^U) applies with S = T. Correct.
- **Step (3).**
  - Given U_{≤k-1}, the level-k links have density ∝ ΠK_{k-1}·1_{R′,k}.
  - DECL's second claim says 1_{R′,k} reads no link of int Q, Q ∈ T. The interior plaquettes of the other cubes use links
    disjoint from int Q.
  - So the ℓ(T) links are conditionally independent with the normalised kernels k_c.
  - Neither ζ_Q nor H′(U^ref) nor F reads anything else. The factorisation into Πp_K is Lemma TD. Correct.
- **Step (4).** The chain is e^{c_T} (μ → ref), then the factorisation, then e^{c_T} (ref → μ), then division by
  E_{ν′}[H′] = the normalisation of μ′. Correct.
- **Constant.** Two applications of (LI^U) give e^{2c_T}. Step (1) costs nothing. "e^{4c_T} is kept" is harmless.
  - The proposals to HW (l.1602) and the tally (l.1579) say "ONE application". That is wrong: the bound uses (LI^U) twice,
    on the same set T.
  - **Fix FT-1:** write "(LI^U) on the set T, used twice (e^{2c_T})".
- **Scope.** k ≥ 1 is needed because a kernel must exist. Level 0 is l.1423-1425 and is not proven (see NA-1).

## FV-law (l.1363-1369): CONFIRMED (proof); the Consequence needs a scope fix
- The proof is right. Given U_{≥k+1}, the factors K_i with i ≥ k + 1 and the factors 1_{R,j} with j ≥ k + 2 are constants.
  K_k and 1_{R,k+1} are kept.
- **Fix FV-1 (medium).** "Every fixed-V statement … is the same under μ ∈ ℛ^A_𝔥" (l.1367) needs an extra condition. The
  past constraint factors 1_{R,j}, j ≤ k, of a relaxed or declared pattern R_{S,E} are not those of PLD's per-history
  measures μ_{𝔥,ω}/μ^+.
  - FV-law removes the tilt. It does not remove the pattern dependence.
  - Add: "provided (SG^{fl}), PLD-desc and the sea law hold uniformly over the past constraint patterns of ℛ^A_𝔥
    (REVIEW_RLARGE_V3 S-4)".

## KD (l.1371-1379): CONFIRMED
- **Telescoping.** For unitaries, ||1 - V_P|| ≤ ||1 - V^0_P|| + Σ_{c∈∂P}||V_c - V^0_c||. With ||1 - V^0_P|| < ε_1/2 and
  ||1 - V_P|| ≥ ε_1, some c has ||V_c - V^0_c|| > ε_1/8.
- **φ identity.** For SU(2) with VŴ^{-1} = e^{iα n·σ}: ||V - Ŵ||²_op/2 = 2sin²(α/2) = 1 - cos α. With r_c ≥ ½ this gives
  φ_c ≥ ε_1²/256. p4 A2 confirms it at 1.6e-15.
- **KS (c), independent proof.**
  - The kernel angle law is ∝ e^{-bw}√(w(2-w)) on [0, 2] (b = κu r_c), with normaliser 𝒩(b).
  - The Chernoff ratio is 𝒩((1-λ)b)/𝒩(b).
  - After the substitution w = t/b, b^{3/2}𝒩(b) = ∫_0^{2b}e^{-t}√(t(2 - t/b))dt. This is nondecreasing in b.
  - Hence the ratio is ≤ (1-λ)^{-3/2}, for every b > 0 and so uniformly in M̄_c. p4 A1 agrees: the maximum of
    exact/bound is 0.65.
- **Placing degenerate M̄ in 𝒞 is sound.** The union bound over n_int links is correct.

## CW (l.1381-1394): CONFIRMED as CONDITIONAL ⇐ (CLS-min); the Reading is wrong
- **(a)** RS (R1) gives ||M̄_c - S_c|| ≤ A_dη (RLARGE l.973).
  - With r_c < ½, ||M̄_c - S_c|| ≥ 1 - r_c > ½, so η > 1/(2A_d). This is stronger than the file's 1/(4A_d), and simpler
    than the T_1 route.
  - The ribbon of a single link c lies in c's two endpoint blocks (the axial path, the leg and its translate). Both
    blocks are level-(k-1) cubes under Q.
  - Every term of 𝒞(p) is a column term of Q. F^col is the infimum of a larger sum of nonnegative terms, so
    F^col_Q ≥ ℰ_p.
  - TE (ii) (HW l.183) plus ε_1 ≤ min{1/(4A_d), t_pr} give the bound ≥ c_prε_1² = a_bad.
  - The level-0 case via (B) and c_pr ≤ 1/(2N) is correct.
- **(b)** TE (i) at U = U_{k-1} and V = V^0 gives ℰ_P(V^0) ≤ κΦ_{∂P}(U_{k-1}, V^0) + ℰ^<_P(U_{k-1}). The Φ term is 0 at
  V^0 = W_0(M̄).
  - ℰ^<_P is an infimum of non-top terms of 𝒞(P). These are column terms of Q (TE (iii)'s proof), so ℰ^<_P ≤ F^col_Q.
  - ℰ_P depends on V only through ∂P, so evaluating it at V^0, which need not be a realised field, is legitimate.
  - Correct. Y^f_Q ≥ 24u_k·a_bad/4 = 6a_badu_k.
- **Fix CW-1 (binding wording).** l.1393-1394 says "A returned finer defect in Q's column lands in (a) or (b) as well,
  because it raises F^col_Q (SAT)". That is false.
  - The split (a)/(b) is on Q ∈ 𝒞, a property of the kernel centre, not of F^col.
  - By HW's SAT-1 (HW l.778-781), a returned finer defect at threshold moves the coarse holonomy only by dilution
    (~ε_1/L²). It does not put Q in 𝒞.
  - Replace with: "A column with a returned finer defect is in 𝒞 or not. If not, KD prices Q by the kernel mismatch,
    whatever the finer defect. If so, CW still gives F^col_Q ≥ a_bad/4, but (SF-cap)'s factor 1_{G_Q} excludes the column.
    This is the only place a returned finer defect enters (§16.6)."

---

# PART 2: NA-PRICE (i) (priority 2)

## The implication (l.1396-1428): CONFIRMED as logic, with fixes NA-1 to NA-4
- **Decomposition.** {S ⊂ D_k} ⊂ ∪_{S′}E(S′). Dropping "Q bad" for Q ∈ S′ is an upper bound. The 3^{|S|} triples
  (T, S_0, S_1) are right.
- **FT with F.** F = the 𝒞/G-indicators on the columns of S′, a function of U_{≤k-1}. The factor 1{Q ∉ 𝒞} for Q ∈ T can
  be folded into F, and KD then bounds p_K·1{Q∉𝒞} by p_mis.
- **(SF-cap)^{A,+}.**
  - It is applied with A = S′ and A′ = S_1 under μ′, which lies in ℛ^A_𝔥 (closure under DECL).
  - F_1 is column-measurable: 1{Q ∈ 𝒞} reads M̄_c, c ∈ ℓ(Q), whose contours stay in the endpoint blocks under Q.
  - On 𝒞 the bound 1 ≤ e^{θY^f}e^{-6θa_badu_k} is CW.
- **Kernel exponent.** It uses u_{k-1} ≥ u_k - R (finer levels are weaker coupled).
- **Exponents.**
  - λκε_1²/256 ≥ θa_bad ⟺ c_pr ≤ 24λκ/256. At λ = ½ this is κ ≥ 256c_pr/12 = 1.18666·10⁻⁵. My arithmetic, with exact
    c_pr = 1/1797760, matches p4.
  - 6θa_bad ≥ θa_bad.
  - So a_A ≥ θa_bad, given a_ns ≥ θa_bad. a_A/a_bad = 6θ → 0.25 as θ ↑ 1/24 (p4 E5).
- **k-uniformity.** C_A is built from p_mis's prefactor, c_sf and C_ns, so it is uniform exactly when those constants are.
  No recursion is used. This is true as written.

**Fixes.**
- **NA-1 (scope).** T9 asks for "every level k ≥ 0" (l.1305). The theorem is for k ≥ 1, and level 0 is a sketch
  ("Not written further", l.1425). Say so in the status line and in the tally.
- **NA-2 (binding; see Part 4).** The delivered shadow coefficient is c_A = 4c_U + c_f + c_ns.
  - With §16.7's c_f this is ≈ 6·10⁶c_U. With the fix it is ≥ 6c_U + c_ns.
  - Either way it is not the 2c_U pre-stated at l.1306.
  - REL-seq absorbs the depth term 38416c_A(K-1-j) at n_H. Record the deviation and the factor by which n_H moves, or
    state the target as e^{c_A‖S‖_sh}.
- **NA-3.** The status line "not derived from (SDP)^A at level k - 1 (LOOP-const respected)" (l.1428) is literally true,
  but it misleads. See Part 3: the cross-level content is inside (J-NS^dir).
- **NA-4.** "In particular a_A ≥ θa_bad … a_ns ≥ θa_bad by hypothesis" (l.1410-1413) puts the whole K12 content into a
  hypothesis. See Part 4.

---

# PART 3: THE WALL (J-NS^dir) and the architecture verdict (priority 3)

## Proposition WALL (l.1430-1459): arithmetic CONFIRMED; one definitional slip; the reading needs correcting
- **(a) CONFIRMED.** μ(G^c_Q) ≤ Σ_{x}μ(x ∈ D_{k-1}). Feeding it with (SDP)^A at level k - 1, and using the upper half of
  (F_R), u_{k-1} - u_k ≤ β_+log L + R, gives G = 81L^{-a_Aβ_+}e^{-a_AR} > 1. That is HW's LOOP-const with θa_bad → a_A
  (HW l.814-821). With C_A's factor 3, the per-level factor is 243.
- **(b) The constants arithmetic is CONFIRMED.** The bounded case is 243ηe^{aR} ≤ 1; equality is also bounded (p4 D1).
- **Fix W-1 (definitional).** (J-NS^rec_η) at l.1436 is written with max over choice functions of μ(x_Q ∈ D ∀Q). With a
  max, no factor 81 appears, and the closing condition would be 3ηe^{aR} < 1.
  - The 81 in b_3 needs the per-choice form: μ(∩_{S_1}{Q ∈ 𝒞} ∩ {x_Q ∈ D_{k-1}}) ≤ η^{|S_1|}μ(x_Q ∈ D_{k-1} ∀Q) for every
    choice function, summed over the 81^{|S_1|} choices.
  - Fix the statement so that it matches 243ηe^{aR} < 1.
- **(b) The shadow compounding is CONFIRMED as arithmetic about this bound.**
  - When T ≠ ∅ and S_1 ≠ ∅, the common union-form depth term D carries 4c_U + c(k-1). The recursion gives
    c(k) ≥ c(k-1) + 4c_U.
  - Its consequence for REL-seq follows HW l.664-667.
  - p4's D2c evidence for "deep shadows coincide" is degenerate: the tested pair has the same parent (p4_time.txt says
    so). It is evidence for that pair only. The claim rests on H-geo (iii), not on D2c.
- **(c) DIL-1 is CONFIRMED as stated, but its use is gauge-dependent (Fix W-2, medium).**
  - The bound ||M̄ - M̄°|| ≤ fℓ·max||U_e - U°_e|| is true. The polar bound with factor 2 is true (p4 B1/B1n). It also needs
    r > 0 for Ŵ_c(U) to be defined.
  - But the "thin cluster, raised threshold" reading (l.1454-1459) reads the link deviation δ of a gauge-variant field.
  - Take a defect whose only feature is one plaquette at curvature ε_1. In axial gauge it shows up as an O(ε_1) deviation
    on a whole line of links, so f is not small. Through the endpoint blocks, every S4′ contour of c meets it.
  - The gauge-covariant statement is the lasso form of RS (R1)'s proof: ||T^σ_y(U) - T^σ_y(U°)|| ≤ Σ of the curvature
    changes on the plaquettes of the contour's ribbon. That is what gives the ε_1/L² dilution of SAT-1.
  - Restate DIL-1 in lasso form before using it as the "deterministic half" of (J-NS).

## Architecture verdict (the critical question)

**Verdict: YES. NA-PRICE still prices a coarse defect against the returned finer defects in its column, inside the
unrenormalised law. That re-creates LOOP-const in the form "a hypothesis that hides it".**

The evidence, line by line:
- **The inputs.** §16.5 reads only levels k-1 and k of the raw μ_R (l.1427-1428). None of RLARGE v3's listed sources of
  (SDP)^A is used: (I_{k-1}^E)′ two-field, (W1-ret′^J)_{k-1} (c), (SC)_{k-1}, R1^J gas (RLARGE l.398-404, HW §18.1). §16.0
  did not allow them (l.1314-1315).
- **Where the finer defect enters.** It enters as the raw indicator G^c_Q under μ ∈ ℛ^A_𝔥. Bounding μ(𝒞 ∩ G^c) through
  μ(G^c) is LOOP-const (WALL (a)). Through a conditional factor η it is a column recursion (WALL (b)).
  - Both are the column-window Chernoff with a finer defect read through the actual finer field. REVIEW_HW_S2 §5.4 (l.369-372)
    predicted exactly this: "If node A's in-step price of returned level-k clusters were itself derived by the column-window
    Chernoff …, LOOP-const would reappear there verbatim".
- **The direct form.** (J-NS^dir) is exactly HW §15.3's open "non-saturating window split" (HW l.861). It has been
  restated, but no mechanism has been supplied.

**The correct architecture.** It removes (J-NS^dir) as a two-level probability. What remains is two single-level
statements.

Work at level k under the stage-(k-1) R-operated representation, uniform over ℛ^A_𝔥 (S-4), with the tilt handled by FT
exactly as now. In that representation:
- returned level-(k-1) clusters Y in Q's column appear only through their extracted activities ρ_Y, with
  |ρ_Y| ≤ E_0^{|Y|};
- E_0 is level-uniform by the representation's own contraction. It is never taken from (SDP)^A at level k - 1;
- the c-numbers and the coupling shift have been extracted already.

Then on 𝒞 ∩ G^c_Q:
1. **Thin/diluted clusters.** The cluster moves the centre by ≤ γε_1 with γ < ½ (lasso DIL-1). Then
   Q ∈ 𝒞(U) ⇒ Q ∈ 𝒞_{(½-γ)ε_1}(U°), where U° is the extracted small-field completion on the punctured column (column ∖ Y).
   - CW at the reduced threshold gives F^col_{Q∖Y}(U°) ≥ (1 - 2γ)²a_bad/4.
   - The price comes from the coarse centre's main term. A moment of (SF-cap) type on the punctured column, with the
     extracted ρ_Y as a bounded perturbation, gives b_3 ≤ C(E_0, c_lcr)·e^{-6θ(1-2γ)²a_badu_k}.
   - No level-(k-1) defect probability is used: μ(x ∈ D_{k-1}) ≤ 1 is enough. So there is no recursion, (LI^U) is used
     once (on T, as in FT) with no compounding, and LOOP-const does not arise.
2. **Centre-moving clusters.** These are clusters with no dilution gain: γ ≥ ½, a large gauge-invariant deviation.
   - Here the price must come from the cluster itself. Proposition CC (a) shows that the threshold activity has no
     exponential price in a coherent background.
   - So what is needed is an **energy-graded** in-step activity |ρ_Y| ≤ C^{|Y|}e^{-a_eg u_{k-1}·ℰ_+(Y)/ε_1²}. Here ℰ_+(Y) is
     Y's energy above its completion; it is not the background's.
   - A cluster that moves the centre by ≥ ε_1/2 has ℰ_+(Y) ≳ ε_1² times a geometric constant.

**Restated wall.** Replace (J-NS^dir) by:
- **(LCR^punct)_{k-1}** [node A; small-field]. (LCR)_{k-1} of §16.7 on punctured columns, conditional on the extracted
  returned clusters Y in the column with |ρ_Y| ≤ E_0^{|Y|}. Same rate λ_f, constant c_lcr·(1 + E_0)^{81}.
- **(EG)_{k-1}** [node A; large-field, single-level]. An energy-graded in-step returned-cluster activity at level k - 1,
  with a_eg·(geometric constant) ≥ θa_bad.
  - (EG) is where K12 lives now. A threshold-only price (a_J, or a_ret's (β) at ≈ 8·10⁻⁷a_bad) does not suffice.
  - Its natural source is CL^J (c)'s proof with the kernel factors kept energy-graded. It must be consistent with CC: in
    CC's coherent background, ℰ_+(Y) ~ δ² is small, so CC does not refute (EG).
- **Plus** DIL-1 in lasso form (deterministic, provable now).

**Exponent.** a_A = min{λκε_1²/256, 6θ(1-2γ)²a_bad, a_eg·c_geo}. No 81^k and no c(k) growth.

**Is (J-NS^dir) unnecessary?** Not unnecessary. It is replaced: (LCR^punct) is of the "small-field" kind that the
partial-success bar allows. (EG) is single-level but large-field, and it is the honest K12 residue.

---

# PART 4: NA-PRICE (ii), (iii), Proposition CC, K12 (priority 4)

## (ii) ⇐ (LI^U) + (LCR)_{k-1} (l.1461-1479): reduction CONFIRMED-WITH-FIX (binding constant)
- **λ_f.** u_k ≤ u_{k-1} + R ≤ u_{k-1}(1 + 2Rg_K²), so θY^f ≤ λ_fu_{k-1}F^col_Q. Correct.
- **The tilt.** It is used twice, at level k - 1, and the replaced tilt is a G that does not read the column links.
  Correct.
- **Fix C-1 (binding).** S = the 81|A∖A′| column cubes at level k - 1. The (LI^U) allowance is
  c_U(81|A∖A′| + sh(S)) with sh(S) ≤ sh(A∖A′) + Δ_sh|A∖A′|, because the excess is additive and depth-free (p4 D2b;
  Δ_sh = 3073361, E4).
  - Hence c_sf = e^{2c_U(81+Δ_sh)}c_lcr and c_f = 2c_U.
  - l.1469 instead has c_sf = e^{162c_U}c_lcr and c_f = 2c_U(1 + Δ_sh). That multiplies the depth term by ≈ 3·10⁶ and
    enters c_A (l.1409, l.1563).
  - Correct l.1469, l.1573, and c_A in l.1409/l.1564.
- **(LCR)'s status.** "c_lcr not certified" is honest. HW §6's F^col ≤ Σ𝓔^{an} is uncounted and HW's; that is noted.
- **Fix C-2 (minor).** l.1402: HW's form "with c_f = 0" is not deliverable through (LI^U). HW's CAP-dec must carry
  e^{c_f‖·‖_sh} (S-1). Say so in §16.12's HW bullet.

## (iii) a_ret formula (l.1510-1522): CONFIRMED (arithmetic and citation)
- η_q = min{ε_1/18, ε_1/4608, δ_0/A_d} = ε_1/4608.
- a_fl = 49η_q²/(1024σ_fl²). This is HS-net's a(τ) = 49τ²/(256σ²) at τ = η_q/2.
- With σ_fl² = 16/3.17·10⁻³ = 5047.3: a_fl/ε_1² = 4.465·10⁻¹³ and a_fl/a_bad = 8.03·10⁻⁷ (exact c_pr).
- a_J/ε_1² = 2.441·10⁻⁴ (κ = 1). a_KN uses ε_loc = 35ε_1/256.
- a_ret(6.7·10⁻⁴⁰) = 2.00·10⁻⁹¹.
- **Ceiling.** a/g² = (12+p)ln(1/g): with p = 6, ln(1/g) ≈ 108.5, g² ≈ 1.03·10⁻⁹⁴. Correct. This is below the n_H ceiling,
  and DX′ (2.5·10⁻¹⁵²) still binds.
- **Disclosed and correct:** the Gaussian part of σ_fl only; levels ≥ 1 need N5 level-uniformity; the chart domain depends
  on C_I through r_ch, so the V-domain is conditional on restricted (BG)_k.
- **Fix A-1 (minor).** Call a_ret "the per-cube price entering (SC)_k's expansion, conditional on (SC)_k". "PROVEN as
  cited" (l.1510) applies only to the three component prices.

## Proposition CC (l.1482-1508)
**(a) CONFIRMED.** I checked each step:
- P_w(ζ = 1) ≤ r^J.
- The sup bounds use 1/𝒩 increasing and r ≤ 1.
- The int Q factors are ≥ e^{-κu_kδ²/2}, since x^0 maximises every kernel factor (CF (1)).
- C(Q):
  - r ≥ 0.7 - ℓ_Qδ by DIL-1. This is legitimate here, because x^0 fixes the gauge.
  - 1/𝒩(br) ≥ r^{3/2}/𝒩(b), the same monotonicity as in KD.
  - φ ≤ (2ℓδ/0.7)²/2. The exponent 4·8u_{k+1}ℓ²/0.49·δ²/2 is right.
- The Haar ball:
  - the rotation raises ||1 - V_{P_*}|| by ≥ 0.45δ;
  - four δ/16 balls lower it by ≤ δ/4, which gives ε_1 + 0.075δ;
  - each link stays within δ/2 + δ/16 < δ.
- At δ = g_k (admissible, since g_k ≪ ε_1/8) the bound is c·g^{3n_int} with c independent of g.

Two remarks on (a):
- **Remark CC-1 (precision, not a defect).** The lower bound is polynomial, g^{648} at n_int = 216. So it beats
  C g^{-p}e^{-a/g²} only when g² ≲ a/((648 + p)ln(1/g)): about 3·10⁻⁹⁶ for a = a_ret. At the operating point
  (g² ≤ 2.5·10⁻¹⁵² from DX′) it does bite. State this threshold, because at g² = 10⁻⁹⁴ it would not.
- **(b) ARGUED.** Disclosed.
- **Fix CC-2 (binding label).** NP-F2 was pre-stated as "no uniform a_ret on the V-domain (SC)_k is stated on"
  (l.1322). (SC)_k is stated sup over the chart, and CC concedes it does not contradict it (l.1507).
  - What is met is: frozen counterexample to (SF-irr)'s off-chart clause and (RLF-2)'s off-chart reading, PROVEN;
    sea-averaged, ARGUED.
  - Replace "(NP-F2) MET" at l.1506, 1561 and 1577 with that sentence.

## K12 (l.1523-1527, §16.9, l.1583-1586): NOT DECIDED as claimed
- **Correct.** On §16.5's route, a_A does not pass through the sea activities.
- **But** §16.5's route is conditional on (J-NS^dir) with a_ns ≥ θa_bad. That hypothesis is the price of a coarse centre
  over a returned defect. CC shows the returned defect carries no exponential price of its own on cut-good data.
  - If (J-NS) is proven through the coarse centre (Part 3, branch 1), K12 is not needed for diluted clusters.
  - For centre-moving clusters (branch 2), the price is the cluster's own. With threshold prices only, it is a_ret-type,
    ≈ 8·10⁻⁷a_bad, and K12's requirement (θ ≲ 8·10⁻⁷, n_H × 5·10⁴) returns.
- **Fix K-1 (binding).** Replace "K12 … not needed" with: "K12 is reduced to (EG): an energy-graded in-step price of
  centre-moving returned clusters. Without (EG), θ ≤ a_ret/a_bad ≈ 8·10⁻⁷".
  - Strike the RLARGE proposal "strike the requirement" (l.1597-1598).
- **T10's restricted (BG)_k.** It is load-bearing only for a_ret's (β) on the chart. This is CONFIRMED as a reading, and
  the [inference] about the trivial-background operator is labelled.

---

# PART 5: check p4 (priority 5)

- **Re-run under the mandatory lock.**
  - The `until mkdir …/locks/numeric` loop acquired the lock at 10:50:21 UTC, immediately; load 5.17 / 3.78 / 3.48; 34%
    memory free.
  - Run: nice 10; OPENBLAS/OMP/MKL/VECLIB threads 1; PYTHONDONTWRITEBYTECODE=1; python3 without -I; no timeout. 17.1 s,
    70 MB, exit 0.
  - One `rmdir` at 10:50:38. No trap, no pkill, no process left.
  - The output is **byte-identical** to checks/p4_out.txt, including SUMMARY "FAIL: E1".
- **The E1 defect is honestly disclosed** in §16.10 (l.1547-1549), in p4_time.txt and in PLD_LOG l.66-67.
  - The criterion compared the exact 1/1797760 = 5.562477·10⁻⁷ with REVIEW_RLARGE_V3's 5-figure rounding at a relative
    tolerance of 1e-10. The difference is 4.1·10⁻⁶ relative.
  - The κ_min half holds: 1.18666·10⁻⁵ < 1.2·10⁻⁵.
  - No criterion was edited and the script was not re-run. Downstream numbers use the exact value.
  - Verdict: a criterion defect, not a mathematical failure. It is disclosed.
- **Fix P-1 (minor).** §16.10's "nothing was re-run or edited" (l.1549) should add: "PLD.md l.1411-1412 was edited after
  the run to quote the exact c_pr (PLD_LOG l.67)".
- **Scope of p4 (as its criteria say).** It tests no hypothesis ((LI^U), (SF-cap), (LCR), (J-NS), (SC)_k).
  - C1/C2 are a 4-link toy at ε_1 = 0.02. C2's "proven toy lower bound 9.75·10⁻⁵⁵" is far below the sampled 0.516, so C2
    passes trivially.
  - D2c is degenerate (same parent).
  - None of this is load-bearing for a counted item.

---

## Binding fixes (for the PLD owner)
1. **ARCH-1.** Reclassify T9 (i): **NP-F1 MET** (raw-law column pricing = LOOP-const in a new guise, Proposition WALL),
   with NA-PRICE (i) kept as a valid conditional implication. Withdraw "PARTIAL SUCCESS" at l.1561-1567: (J-NS^dir) fails
   the pre-stated bar of l.1317-1319. Record Part 3's restated wall, (LCR^punct)_{k-1} + (EG)_{k-1} + lasso DIL-1, as the
   proposed node-A route. Record that §16.0's allowed-input list (l.1314-1315) omitted the R-operated representation.
2. **NA-3.** Rewrite l.1427-1428: "not derived from (SDP)^A_{k-1}; the cross-level content is the hypothesis (J-NS^dir),
   whose trivial and recursive proofs are LOOP-const (§16.6)".
3. **CW-1.** Correct the Reading (l.1393-1394) per Part 1.
4. **C-1 / NA-2.** Set c_sf = e^{2c_U(81+Δ_sh)}c_lcr and c_f = 2c_U. Recompute c_A, and disclose c_A ≠ 2c_U against
   l.1306, with its n_H consequence via REL-seq.
5. **W-1.** Restate (J-NS^rec_η) per choice function so that it matches 243ηe^{aR} < 1.
6. **K-1.** "K12 decided / not needed" → "reduced to (EG)". Fix §16.8 l.1523-1527, §16.11 l.1583-1586, §16.12 l.1597-1598.
7. **CC-2.** Relabel NP-F2 (l.1506, 1561, 1577).
8. **FT-1.** "(LI^U) used once" → "used twice on the set T (e^{2c_T})" (l.1579, 1602).

## Recommended (non-binding)
- W-2: DIL-1 in lasso, gauge-covariant form.
- FV-1: the S-4 uniformity clause.
- NA-1: k = 0 is not covered.
- A-1, CC-1, C-2, P-1.

## Tally
- **[E4] (1) FT + KD: CONFIRMED** (FT-1 cosmetic).
- **[E4] (2) NA-PRICE (i) as an implication, with CW: CONFIRMED-WITH-FIX** (NA-2/C-1 constant; CW-1 wording; NA-3).
- 0 GAP and 0 WRONG among the counted items.
- The outcome labels are WRONG: "PARTIAL SUCCESS", "K12 DECIDED" and "NP-F2 MET" (ARCH-1, K-1, CC-2).
- Uncounted items:
  - FV-law: CONFIRMED (scope FV-1).
  - DIL-1: CONFIRMED as stated, use gauge-dependent (W-2).
  - WALL: CONFIRMED as arithmetic (W-1).
  - CC (a): CONFIRMED.
  - §16.7 reduction: CONFIRMED-WITH-FIX (C-1).

## Strategic verdict
- Session 4's genuine gains are three. The law conversion (FT/FV-law) is clean and settles S-1's mechanism: the tilt is
  converted once per kernel event, with no fixed-V law. The kernel/centre dichotomy (KD/CW) disposes of the mismatch and of
  the clean-column coherent background without a background map. And Proposition CC is a real negative for (SF-irr)'s
  off-chart clause.
- The wall did **not** move. (J-NS^dir) is HW §15.3's non-saturating split under a new name, posed in the raw law.
- The next session should re-pose T9 with the R-operated representation as an allowed input. Then prove (LCR^punct) (with
  (LCR), the same small-field object) and (EG) (energy-graded CL^J (c)) at a single level. That is the only form in which
  (SDP)^A is a per-level output with no column induction.
- Until (EG) is in hand, plan the constants with θ ≈ a_ret/a_bad ≈ 8·10⁻⁷, i.e. n_H × ≈ 5·10⁴. Do not plan with θ ↑ 1/24.
