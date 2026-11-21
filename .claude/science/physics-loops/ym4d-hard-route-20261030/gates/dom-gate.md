# DOM gate (pass-3 referee of library/dom.md)

First failing step: L207, proof of Theorem 7. The step "its recorded witness gives Definition 2(3)" needs a recorded witness on every box of B_I(Z). Definition 1(2) (L34) does not name those boxes among the recorded core gauge boxes. Repairable.

Text read: `library/dom.md` (385 lines), once, line by line. The draft `dom-draft.md` was read only where dom.md points to it, and for the Theorem 7 comparison (draft L98, L204, L222-223). Imports read at the cited lines: st1-r4 (L85-171, 539-780, 900-915, 1455-1592), pr-lay (L215-275, 305-312), hm (L11-153, 154-316), descent (L101-126, 184-250, 285), in1 (L12-30, 44, 143, 221-245, 666-699), cp12 (L462-575), geoh (L9-75, 192-203), dr (L170-180, 594, 627), ci-form (L30-38, 403), layered-a3 (L25-40), assembly-status (L45-61, 127, 180-192). Source lines read myself: SA 6005-6035 (R19), 8165-8172, 9767-9772, 9783-9789, 9913, 17334, 17575-17583, 17656, and CA-I 53765-53774.

## Findings

1. **L207 (Theorem 7 proof), with Definition 1(2), L34. Repairable. First failing step.**
   - The step: each box of B_I(Z) lies inside Ω_k, so "its recorded witness gives Definition 2(3)".
   - The problem: Definition 1(2) records a witness only on "every required core gauge box". It does not say which boxes are required. Definition 2(3) and hm Lemma 4 need one real gauge on each **whole** rounded IMS box. Such a box has side up to 2ℓ_IMS+2b_gap. It is not one M-cube, and witnesses on its M-cubes one at a time do not give one gauge on their union. The draft did state this: R♮-c, draft L98, took the prescribed core cubes to be "**every** cube of side at most C_box LM contained in Ω_k^σ". The distilled text dropped that clause. So the step does not follow from Definition 1 as written.
   - Repair: add to Definition 1(2), at core level k, that the prescribed core gauge boxes include every box of B_I(Z) (or every box of side ≤ C_box LM in Ω_k), each with its formation carrier. Formation then follows from ST1 (60): the side satisfies s ≤ 2ℓ_IMS+2b_gap ≤ C_box LM by hm (23), so the quotient (s+2)/M is bounded independently of M. The distance count in L207 is correct: 1 + b_gap + e_c + M ≤ 2M − 2 < LM under (11).
   - This is also the answer to "is each coverage obligation stated so that a later text can discharge it": items 1 and 3 of Definition 1 are (item 1 uses PR-lay D's own wording "every required bond and derivative stencil"; item 3 names PR-lay/hm's natural cubes). Item 2's "required core gauge box" and "every consumer core level" are not, until the consumer list is written out as above.

2. **L258-267 (Lemma 11), with L55. Repairable.**
   - The conclusion "F6's two smallness conclusions hold" uses R_♯ ≥ c_Nℓ_t^r/4 (L273). That needs R_♯ ≥ MR_t/4, ST1 LOC(decay)'s condition (st1-r4 L157).
   - Lemma 11's hypotheses use R_♯ only through "rows constant within distance R_♯/2". They never state R_♯ ≥ MR_t/4. Definition 3 mentions it, but only as part of the consumer.
   - Repair: add "with R_♯ ≥ MR_t/4" to Lemma 11's hypotheses. (15) then has exactly LOC(decay)'s form, with c_loc = a/2.
   - The rest checks: aρ_0 ≥ 32 log L follows from ST1 row 3; the right-trivialized velocity is integrated; d_G is at most the integrated speed; the window ratio θ_j/θ_t ∈ [1/2,2] needs only a final ceiling; and e^{-cℓ^r}/δ'_j → 0 because r > 1.

3. **L62-64 (Order of choice). Repairable, no consequence.**
   - The table puts "the numerical frame-increment bound B̄" in rows 6-8.
   - IN1 fixes B̄ = C_β+1 with c_0, c_2 at row 2 (in1.md L18 and L228: "the weak triple (1)"). IN1 row 8 then makes d_0 follow B̄. Row 6-8 placement is ST1's own permission (st1-r4 L163, L170); it is not IN1's table.
   - Nothing in dom fixed before row 9 reads B̄. Theorem 1's floor (4) is a row-9 floor. So nothing breaks.
   - Repair: say that B̄ is IN1's row-2 constant and that (4) is imposed at row 9.

4. **L310 (Lemma 14 proof). Minor order note.**
   - r_hol is chosen below δ_B/[4(1+C_R)]. δ_B is ST1 row 4, but ST1 lists r_hol at row 2 (st1-r4 L163).
   - I found no constant in ST1 rows 2-4 that reads r_hol, so there is no cycle. All of these are fixed before κ, as dom's row "3, then 4" says.
   - Repair: state that r_hol (and M_*) now follow δ_B and the row-3 chart shrinkage.

5. **L103 (Theorem 1 proof). Minor.**
   - "For t ≤ ρ_1, no solution with N ≤ t exists" is stated without proof.
   - It is true: unit steps give ρ_{t-N+1} ≥ ρ_1 − (t−N), so g(N) ≤ t−1−ρ_1 < 0.
   - Repair: add that line. The claim is not load-bearing.

6. **L287 (LOC-flat, second route). Locator only.**
   - SA 17578 is the formula Ω_i^c∩X = H_i^{[8]}. The quiet clause is at SA 17575, and the box nest at 17577-17582.
   - The reading itself is fair: those nested boxes give margins inside X, not for the cut Ω_q∩X^♯.
   - Repair: cite SA 17575-17582.

7. **L353, L359 (source record and status sentence). Non-mathematical.**
   - The linked `../checks/dom-pass2/source-checks.md` and both sha256 files are not in this clone (F/checks has no dom entry). I re-read every load-bearing SA/CA-I quotation myself (list above); all are correct apart from item 6.
   - The text says "Distilled DR ... not treated as refereed supply". DR was frozen (commit 8521ff989) after dom's stated checkout 1d6a3a0af, and pw.md was frozen later still. The DR quantities dom uses are unchanged in the frozen text: E_κ̄ = e^{48κ̄} and s_D = ε_D e^{-64κ̄} (dr.md (9)), and Theorem 4's retained hypotheses (dr.md L170, L594).
   - Repair: update the sentence and the provenance checkout, and add the record or drop the link.

8. **L355-359 (Result). Repairable wording.**
   - The open list omits two items:
     - the ST-test residue that L300 itself leaves open: "selection and compatibility of the actual passing factor, including its older densities";
     - the fact that Theorem 13 assumes "the local rule's agreement/admission clauses". These are LOC-flat clauses 2-3, which are open for curved data (L285).
   - So the pivot clause is proved only relative to LOC-flat 2-3. "Conditional pivot estimate" (L357) is accurate, but item 5 needs this stated.
   - Repair: add both to the Outstanding list in the Result.

9. **Application of Theorem 1 to the actual history (L71, against assembly item 5). Note, not an error.**
   - R19 includes R_j ≤ LR_{j+1}. IN1's frame (1) (in1.md L22) does not list it.
   - For IN1 frames it is supplied by frozen geoh Lemma 1 ("adjacent R's have ratio 1 or L", after a floor on X_0 depending on L, r, B̄).
   - With that citation, Theorem 1 discharges RUN-low on the actual IN1 frames (IN1 has r ≥ 2 > 1).
   - Repair: add one sentence citing geoh Lemma 1.

## Checks that passed (summary)

- **Theorem 1 (L71-103).** I read SA R19 at 6017-6026 myself. Every step checks:
  - min_{u≤j}θ_u ≥ θ_j − c_5 ≥ θ_j/2 for θ_j ≥ 2c_5.
  - ρ_j ≥ 1, because every θ_u ≥ X_0 ≥ 4 > e.
  - The unit steps of ρ and g; g(1) < 0; g(t) ≥ 0 when t ≥ 1+ρ_1.
  - ρ+3 ≤ L^ρ, so N_* ≤ R_t − 1 ≤ t − 1.
  - θ_u ≤ θ_t + B̄(ρ+1) ≤ y + c_5 + B̄(ρ+1) ≤ 2y by (4).
  - (log 2y)^r ≤ L(log y)^r ≤ LR_t, so R_u ≤ LR_t and g(N_*) ≥ 0.
  - (4) holds for every fixed finite B̄ after a row-9 floor.
  - SA 17582 ("As long as k ≤ N_k the class is empty") supports L103.
  - CA-I 53765-53774 (smallest positive N_0; "N_0 ≥ 2 and N_0 ≤ R_k − 1") supports the Result-table entry.
  - RUN-low's clauses (st1-r4 L147) are all supplied, with c_N = 2^{-r}.
- **Theorem 3.** l ≤ Lξ_m holds, since a stencil cannot cross a full layer. (5) follows from (1) with room to spare. D (19) holds with λ_σ = L^3 ≤ C'_λ(log θ_ν)^{2r_R}. F_Q is the supremum for γ < e^{-Q} (PR-lay Lemma 7).
- **Lemma 4.** A sketch, but correct in structure. T2 gives L^{-av}r_0(m+v) ≤ (2/L)^v r_0(m); this also converts (7) into Lemma 9′'s level-i condition (55). The margins are the B4 half-radius, not the gap d_*, so c_room is early.
- **Lemma 5 (the R4 counterexample).**
  - Tent bounds: ξ|A_s| ≤ s and ξ²|∇A_s| ≤ s. Commuting links give normalized curvature ≤ s ≤ 2s.
  - Ordinary towers: E_U = 0, E_{A_s} ≤ s. The L^{p−i} factor against (14) is ≤ 1.
  - R1 towers: (R2) carries the extra L^{−(i−p)}. Lemma 9′'s displayed Lipschitz bound gives K^♯ s λ_p < c_min r_min λ_p ≤ b_0(e)λ_p. The full-carrier hypothesis i ≤ m is exactly what gives ξ_i|A_s| ≤ s. Core simple elements at levels i > m cannot read the support, by the >3ξ_m layer distance.
  - The violation: |A_s(b)| = sL^{k−m} > (s_0/2)L^{n_0} ≥ La_1 > a_1.
  - Scope: the Outstanding at L164 (the draft's full-carrier and actual-history claims are not established) is correct, as is the remark that (I,0,0) lies in both classes.
- **Theorem 6, checked against hm Theorems 5, 7, 8 and Lemmas 1-4, and descent Lemmas 1, 4 and Theorem 5.**
  - K^♭ ⊂ R_loc(Z; h/4).
  - Lemma 2's line disc uses only the real bound < h/2 and r_Z.
  - Lemma 3/4 boxes: α < C_pot M a_0 < h/(16L²) by (9) = hm (10).
  - Root compressions: a tent box lies within 2ℓ_IMS + b_tail + r_av + 3L ≤ b_gap of its coordinate ball, hence inside the readable hull (R_* ≥ nr_c + b_gap). So B_I(Z) is exactly the needed family, and K4 was too narrow.
  - (10) is hm (26) with r_Z < ϱ. (9) gives H_0 r ≤ 1/2 and r < r_loc/2.
  - Real-gauge invariance of Definition 2 (witness h ↦ hg^{-1}) gives descent Lemma 1's Rep representative.
- **Theorem 7.** Apart from finding 1, it checks: (12) gives Definition 2(1); Definition 1(3) gives 2(2); r_0(k) ≤ C_0F_q(γ) = a_0^γ; the top gap ≥ LM matches PR-lay G.
- **Theorem 8.** Exactly ST1 Theorem 14 / Lemmas 11, 13 on D^♭. Membership of P stays a hypothesis; the Outstanding at L221 is correct.
- **Corollary 9.**
  - (71) with δ_src = 2c_ct r_0(k) and Q_X ≤ C/(a r_0(k)): the r_0(k) cancels in the first term, which gives c_ct E_κ̄ K_main. The second term → 0. So a_X < 1/2 under (14).
  - K_main is early.
  - The ball matches cp12 D8: r_k^ct = c_ct α_{0,k}, and 𝔅_k(2r^ct) is sup|g_kB| < 2c_ct r_0(k).
  - c_ct at IN1 row 6 matches cp12 L544. The Hessian factor matches cp12 L547. The κ̄-dependent (c_ct C_0)^{-2} is paid at X_0, which cp12 L551 already places last.
  - SA 9767-9772 does assume enlarged simple **and** tower conditions.
- **Lemma 10.**
  - D_1(c) = e^{3ir_Bσ_3} against D_0(c) = I gives d_G = 3r_B < π. Both data are exactly flat and gauge-equivalent. The local rule cannot tell them apart, so LOC-form would force 3r_B ≤ 2r_B.
  - Scope: this refutes LOC-form universally on the non-gauge-fixed admitted class, which is the class the lemma states. It does not touch LOC-decay: the background moves only near v.
- **Lemma 12 (pure-gauge construction).** On a local component q_v = g_v g_root^{-1}. A common right factor keeps local rows constant. Outside, g_v goes to I. Row speed ≤ 2π. Local rows agree exactly and the output is flat.
  - What remains for curved data is stated precisely (L285-289), and I agree with it:
    - agreement fails on non-tree edges that close nontrivial plaquettes;
    - the restricted system loses A1/P82's separation margin at the artificial boundary;
    - the single-gauge cutoff route has no small gauge over a cell-sized X^♯ and no commutator control.
  - So clauses 2-4 (agreement, admission, path) and 5's quantitative chart are open. No nonexistence claim is made.
- **Theorem 13.**
  - SA 8167 puts the pivot at (y+he_μ, y+(h+1)e_μ), crossing B(y) → B(y'). The opposite edge and the transverse edges cannot be pivots, by coordinates mod L, so the plaquette has exactly one pivot.
  - Bi-invariant triangle bound: 3δ'_j + two curvatures, with d_G(W,I) ≤ 2|W−I|.
  - (58) with (56) gives C_te C_R² A_0 g ℓ^{p_0+2r_R} ≤ C·A_0 F_{p_0+2r_R}(γ).
- **Lemma 14.** The composition argument is sound: with ‖X‖, ‖Y‖ ≤ ‖B‖, the Lipschitz bound plus a centre discrepancy below a quarter of the log radius keeps the relative logarithm holomorphic and bounded. The Outstanding at L312 is correct; ε sin(Nz) is a valid illustration.
- **Theorem 15.** Matches ST1 BOX, B1, B2 and geoh Theorem 2's exponent N_t^0 − 1 under its stated qualification.
- **Lemma 16.** Matches st1-r4 Lemma 8: ‖B(w)‖ < δ_B/4, tube room δ_B/8. The literal layered-a3 (1) (L33-35) is not proved, and the text says so.

## Codex's verdicts on the draft's corrections to frozen texts (L373-383)

I checked each verdict against the frozen text. All are correct.
- **hm L33 / descent (2):** the flat point (I,0,0) satisfies R4, so "never met" is false.
- **IN1 L44:** no defect is shown.
- **PR-lay L254:** the mark stands.
- **ST1 L154:** C_QL(1+β_s) holds for the same index, and adjacent indices pay a T2 factor ≤ 2.
- **ST1 L1542 hypothesis 2:** the proposed deletion is rightly rejected. B4 is real admission only (st1-r4 L1531).
- **cp12 (27):** (14) is valid for its ball, but C1-C3/D7 coverage stays open.
- **assembly-status L127 and L51:** both are properly narrowed.
- **CA-I 53773:** verified in ca_I.tex.

## Unchecked (unfrozen) notes and what depends on them

- **ci-form.md:** used only to state obligations (L111, L222, L334). No result depends on it.
- **layered-a3.md:** used only for the PR1(5b) remark (L330-336). That remark rests on what layered-a3 (1) says (checked: L33-35) and on ST1 importing none of it.
- **td.md:** IN1 Amendment 1's floors are conditional on td.md. No dom constant reads them.
- **Through S and M:** a3-derivative, a1-balaban (A1/F0), h-walk and the SA FG/UM and AV imports enter as hypotheses that the frozen ST1, hm and cp12 texts already carry.
- **dr.md and pw.md:** now frozen (finding 7).

## Constants (IN1 rows 1-10 with Amendment 1)

- Early, before κ, independent of M and κ̄: c_N = 2^{-r} (row 1), L ≥ 27 with Amendment 1's L_0^♮ (row 2), a_♭ < h/4, c_room, K_main, C_path, r_R, C_R, C_raw, C_V, r_hol, M_*.
- After κ̄: c_ct (row 6, through E_κ̄), M floor (11) (row 5).
- Final (row 9): (4), (12), (9) with ϱ_γ, a_0^γ, the γ ceilings of Corollary 9, Lemma 11, Theorems 13 and 15.
- No early constant is rescued by a later choice. The only mismatches are B̄'s row (finding 3) and r_hol's position (finding 4).

## Verdict

dom.md is a sound conditional text, with one repairable gap at L207 (finding 1) and minor wording, locator and order repairs (findings 2-9).
- **Proved:** Theorem 1 (RUN-low with N_t^0 ≤ R_t − 1 for any fixed finite B̄).
- **Exact in its stated class:** the LOC-form counterexample (Lemma 10).
- **Correctly restricted:** the R4 counterexample (Lemma 5), to the full-carrier hypothesis and the core-tower factor λ_p = L^{-(i−p)}.
- **Correct conditional implications:** Theorems 3, 6, 8, 13 and 15, Corollary 9, and Lemmas 11, 14 and 16.
- **Theorem 7:** correct once Definition 1(2) names the B_I(Z) boxes.

The Outstanding marks are correctly placed: L111 (roster realization and local coverage), L164 (full-carrier claim of the original counterexample), L221 (actual input membership), Lemma 12 (curved LOC-flat), L312 (quantitative localized charts), L328 (actual BOX), and the Result's "Full DOM ... Outstanding". Finding 8 asks that the Result also list the ST-test passing-factor residue and Theorem 13's dependence on LOC-flat 2-3.

What changes for item 5 (assembly-status L186):
- **RUN-low** can leave item 5. It follows from Theorem 1, IN1's frame (1) and geoh Lemma 1.
- **ST-test:** its pivot clause is proved relative to LOC-flat 2-3. Selection and compatibility remain a design input.
- **LOC:** LOC-form is refuted universally. LOC-decay reduces to LOC-flat's extension and path, which remain open for curved data.
- **ST-test^hol** reduces to Lemma 14's quantitative chart, which is open.
- **"Every ST1 chain domain inside R4":** the literal inclusion fails on qualifying geometries (Lemma 5). It is replaced by the weighted K^♭ interface (Theorems 6-7, after the finding-1 repair). Its adoption is open.
- **PR-lay D:** holds on the proposed roster. Actual roster realization is open.
- **Complex input membership:** open.
- **BOX:** straddling loops and source identification are open.
- **PR1(5b):** not needed on the conditional ST1 route.

Item 5 stays open. Its content narrows to: roster realization and local coverage, input membership, curved LOC-flat with its quantitative chart, ST-test passing-factor compatibility, and actual BOX.

Checked line by line by Claude (fresh session).
