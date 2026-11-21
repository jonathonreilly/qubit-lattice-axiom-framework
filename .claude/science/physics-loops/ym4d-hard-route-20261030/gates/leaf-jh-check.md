# Check of library/leaf-jh.md

Checked line by line by Claude (Opus 5.5), 2026-11-08, one reading.
Clone at `08462835c` on `claude/ym4d-hard-route`.
Sources: Y = YM4_1400.tex (pin 2bc0658f), SA = YM4_sketch_500.tex, I = CA-I (pin 31a47c543775).

## Verdict: FIX (minor, in place)

I found no mathematical error.
Both kill tests pass when checked by hand.
Every inequality in (12)–(15) checks.
The ported diagram, the inverse and the one-step factor say what the source says.
The proved statements are the ones J-ENTRY (D1) and H-ROWS (D3) ask for, on one two-part join.
Six repairs are wording and citations only.
Three of them name inputs that the note uses but does not cite (findings 9, 12, 14).
No result changes. No new lane is needed.

## Findings

1. **Outward kill test (1)–(2).** Note 55–91. Y 3575 (Federbush mean, axis-ordered path family G(y,x)), Y 42131–42143 (u_W is the exponential of averaged relative logs, weight L^{-4}).
   With commuting data the mean of e^{itT} over the paths that use e gives e^{itp_xT}.
   Only paths that leave z in direction +1 use e, and they use it positively.
   The single path to z+e_1 is e, so p_{z+e_1}=1 and ν ≥ L^{-4}.
   (9) with V_0=1 and B_raw(c)=0 gives b(c)=tνT ≠ 0. ST1 (7) (st1-r4 47–52) feeds this value to the response.
   **CONFIRMED.** Raw-row substitution fails, as stated.

2. **Radius kill test.** Note 93–97. **CONFIRMED.** With S=tE_c and t→s_D, the strict-room remark is correct.

3. **Noncommuting test (3).** Note 99–130. Y 42136: each factor is log{T(e^{ia}W)T(W)^{-1}}. With zero relative increments this is log I = 0 for any W, commuting or not.
   The commutator example is correct: XY−YX = −2i sinα sinβ σ_3.
   The split between the one-step factor and the accumulated node gauge matches Y 34157–34160 and ST1 (34) (st1-r4 374).
   **CONFIRMED.**

4. **Cut-action test (4).** Note 132–144. **CONFIRMED as stated, but it is a stipulation.** Both sides are *defined* with A_J. The test does not compute anything.
   Y 16129 (end of the paragraph) records two conventions. Statements 3–8 use the inner-plaquette action. Statements 1–2 use the compressed ambient Hessian.
   SA 9783 defines the localized background as "the background attached to this problem". It does not name the action.
   *Repair:* at note 479, cite Y 16129 (statements 3–8) for the inner-plaquette convention. Say that the regional PH1 chart is granted with A_J. Note 143 already says that the ambient choice would fail.

5. **Node diagram port (8)–(9).** Note 211–234. Y 34174–34189.
   Endpoint order, inverse and orientation formulas match. The c_- case (note 230) also checks: with u_+=1, e^{iS}=u_-^{-1}e^{iB}.
   **MISMATCH (notation only).** Y writes e^{iξ_c b_c} and e^{iξ_c B_c} (ξ_c is the row length, Y 16108, 16129). The note writes e^{iS}, with no ξ_c.
   This is consistent with the note's raw-angle convention (note 251) and with K^J=m_JQ^J (leaf-d1 (4)). But the conversion is not stated at the port.
   *Repair:* at note 211, add "S(c)=ξ_c b_c in Y's notation; all rows are raw angles."

6. **Inverse and nilpotence.** Note 236–240. Y 10719–10723 (the factor reads interior rows only) and Y 10763–10766 (Db=D+T, TD^{-1}T=0). **CONFIRMED.**

7. **Complex reference in the inverse chart.** Note 194, 246–248, 285.
   Y 10710 and 10731–10733 prove the inverse for a **real** U_0. They use the fact that conjugation by a real V_0 has norm one. Y 34190 likewise says "at the real reference".
   The note applies the inverse at complex V_0^J(P) and assigns this to "the granted complete-read admission". The tree grants leaf-d1 §6's D2 admission, which "must supply the reference gauges on these full reads" (leaf-d1 427). That grant does not explicitly name a uniform complex-reference inverse radius r_red.
   **UNCLEAR.** This is not a source port.
   *Repair:* state that r_red, uniform over the pair domain, is part of the grant. Alternatively derive it from ST1 F4's complex Ad V bound (st1-r4 898) on Lemma 5's tube (32) (st1-r4 350–353).
   Note: J0 itself only needs the S-ball, so r_red is needed only for the raw-coordinate inverse.

8. **Norm identity (10) and units.** Note 251–262. TD R (td 31: maximum of row norms) and leaf-d1 (7) (‖b‖_{Y,w}=sup w|b|). **CONFIRMED.** The weight is w=1 on the ball, as in DR 194.

9. **Constant choice (12).** Note 285–301. DR (9) (dr 172–178): c_* ≤ min{r_0/4, (16C_W)^{-1}, (16C_C)^{-1}} and ε_D = min{c_*b_0^{-4}, (32C_Rt_0b_0)^{-1}, r_R/(4b_0)}.
   With b_0=t_0=C and c_*=c/4, (12) is DR's choice. Adding r_red to the minimum only shrinks c, which is allowed. **CONFIRMED.**
   **UNCLEAR:** the note says C_op is "early" (note 271). DR 73 makes b_0 early. But the native joined C_op must be fixed at or before TD step 2 (td 428; td2 172), and the note gives no citation for this. The hull radius R_*=C_LM_1 (leaf-d1 446) suggests C_op may depend on M_1.
   *Repair:* cite where the granted native C_op is fixed relative to TD step 2, or list "C_op fixed before ε_D" as part of the grant.

10. **Inequalities (13)–(14).** Note 303–330. I checked each step by hand.
    s_D ≤ (c/4)C^{-4}e^{-64κ̄} = r_DF/4. With b_*=2s_D, s_D<b_*<r_DF. s_D ≤ r_red/4.
    2R_* = 8Bs_D ≤ 2r_Re^{-48κ̄} < r_R.
    BC_der(2R_*) ≤ 8C_RB²b_* = 16C_RC²ε_De^{-32κ̄} ≤ 1/2.
    DR's own contraction constants also hold at b_*: they are at most 1/16, 1/8 and r_0/2. **CONFIRMED.** (11) matches dr 200.

11. **Order and Cauchy budget (15).** Note 332–362. TD 428–430 and TD2 172–178 fix c_D and ε_D before κ, and s_D after κ̄. The ϱ, A_V, K_1 and ϑ formulas match td 36–46.
    I derived both alternatives by hand: ϑ ≍ gℓ^{p_0} when K_1=1, and ϑ ≍ ℓ^{p_0−q} otherwise. Both tend to 0. **CONFIRMED.** I found no lower bound on ε_D in TD or TD2.

12. **Next map (16)–(17) and fibre (19).** Note 386–441. ST1 Lemma 12 (67) and its proof (st1-r4 781–800). Its double-block separation argument is the one used. **CONFIRMED** on (5), given the separation hypotheses of a3-close Lemma J.

13. **Reduced datum on the fibre (20).** Note 455–467. **CONFIRMED.** This is already HMA Lemma 7 (hma 346): b(ιB)=ιB, v_z(0)=1.
    *Repair:* credit HMA Lemma 7 at note 462.

14. **Criticality transfer.** Note 485–489. This matches ST1 Lemma 12's "critical for the old fibre by (67)". **CONFIRMED.**
    **UNCLEAR:** "The base lies strictly inside the supplied regular uniqueness class" (note 494) is asserted without a source. The tree lists class membership as part of H-ROWS.
    The margin exists: Y 35634–35649 gives R ≤ C_Bε ≤ C_Ba_1 < a_0. ST1 Lemma 12's proof uses "the real background bounds" for the same step.
    *Repair:* cite these at note 494.

15. **Real uniqueness, holomorphic continuation and gauge transport.** Note 498–528. The argument is standard and correct on the granted connected common chart: a real ball is a uniqueness set, and the action is gauge invariant. **CONFIRMED.**

16. **Scope versus D1 and D3.** Note 534–567. For D1, the note gives J0 and the Neumann condition on TD's full completed ball. It leaves the anchor and the tags unchanged. This is what J-ENTRY asks for (tree 209–231), conditional on findings 7 and 9.
    For D3, the note gives PH3 on one regional join. Leaf-d3 236 needs PH3 "on the regional problems used by this birth". The note correctly says that other births and HMA-DOM remain open.
    **MISMATCH (wording):** status-table row "Physical Hessian … can consume" (note 561) and note 543. HMA Theorem 8 assumes D6, which fixes Ω_0 as the torus (hma 281). Theorem 8 therefore cannot take a proper-region identity without a regional version of D6. Note 544–546 says this, but the table does not.
    *Repair:* reword the row: "Consumable only after a regional D6/Theorem 8; this is not supplied here."

17. **Source locators.** Note 46–49. Y 10707–10782, 34153–34208 and 42131–42157 are the correct passages. I 45162–45201 is labelled "Proof outstanding", as the note says. **CONFIRMED.**

## Grants actually used

- Leaf-d1 §6: the native operator implication (B=C_op e^{16κ̄}) and the D2 complete-read admission.
- HMA PH1, PH2 and PH4 on the regional join, with their connected common chart.
- a3-close Lemma J: geometry and separation.
- Not granted but used (findings 7, 9 and 14): the uniform complex-reference inverse radius r_red, C_op fixed early, and the base-class margin. The source supports the margin. The other two must be stated as grants or cited.
