# Check of library/hcm-repair.md (HCM-SC)

Checker: Claude (Opus 5.5), one line-by-line reading, 2026-11-08.
Clone at `7338d0bb6` on `claude/ym4d-hard-route`.
Research text. Not an audit. Grants no status.

## Verdict: FIX

The proved steps are correct. Section 3's payment matches IN1 (31)-(32) exactly.
The hand checks (9), (11), (12) are correct.
Three things need repair.
First, HCM-SC asks for more than the repair needs. It keeps the artificial lower collar rows.
A repair may delete them. That gives a fourth route the note does not try (finding 9).
Second, Route 1 is the old obstruction, not a route to HCM-SC. So only two real routes fail.
Third, the consumer list in section 6 misses three Y ranges (finding 8).

## Findings

**1. Note 36-57 (source table, (1)). I 42988-43004, 43128-43150. CONFIRMED.**
(1) is I's display (4.12:eq-constrained-minimisers-b).
ℓ_B(p) is the smallest block side next to p (I 43007-43011).
At a bare determining block η²ℓ_B⁻² = 1. At a level-m block it is L^{-2m} (I 42952-42954: η=L^{-k}, ℓ_m=L^{m-k}).
So "homogeneous top set gives the factor, bare joined set does not" is right.

**2. Note 61-91 (§2, the changed test). Y 72313-72338, Y 61905, SA 5672-5676. CONFIRMED.**
The guard is Y's final-stage test, threshold 3(1-β_s/2)ε_m L^{-2m} (Y 72324-72327).
The four bonds are face-lifted determining bonds (Y 72328-72334).
Line 89-90 (joined-level units would weaken the hypothesis) has a stronger support than Y 61905: SA R4 (SA 5672-5676) needs |∂U-1| < a_0η_j² on all of X.
Repair: cite R4 there.

**3. Note 98-157 (§3, from (3) to the witness). Y 71745-71760, 76885-76895. CONFIRMED.**
With d=a_s/(4C_s) and D<dε_m, (3) gives η²(a_s/4+a_s/4)ε_m. That is half of (2). Correct.
(5) is Y's certificate (eq:small-energy-min-certificate): min{¼Σ‖1-∂M^tU(C)‖², e_*/2}. Correct for a singleton.
θ_mε_m² = P_m², since ε_j = g_jP_j and g_j = θ_j^{-1/2} (in1.md 28). Correct.
The same logic is Y's island argument (Y 76885-76895). The note says it is not substituting the island event. Correct.

**4. Note 159-186 (§3, the payment q_t). in1.md 25-33, 155, 227, 484-527. CONFIRMED.**
(6): T_t = C_TR_t (in1.md 155). r̂_t = 4c_1M⁴R_t⁵+κ_1 (in1.md 511). q_t = C_cnt T_t r̂_t is the per-mark charge in (31) (in1.md 489).
R_t ≤ L(log m_t)^r ≤ Lx^r, since m_t ≤ θ_t. With x ≥ 1, q_t ≤ Kx^{6r} and K is right.
P_t = A_0x^{p_0} (in1.md 28). c_*A_0²x^{2p_0} ≥ Kx^{6r} needs only 2p_0 > 6r. IN1 has p_0 > 6r (in1.md 227, 484).
X_0 is chosen after c_1, κ_1, C_T, C_cnt (in1.md 233 then the coupling ceiling). So the order is valid.
IN1 itself uses P_n/2 ≥ C_cnt T_n r̂_n (in1.md 518-520). q_t is exactly what a mark needs.

**5. Note 152-157, 202-205 (ownership). Y 76813-76822, 76848-76866. UNCLEAR.**
The mark halo C(u)^+ adds only two layers of level-m unit cubes (Y 76817-76820).
The final-stage rim is at the outer boundary of X. Y 63866 says the stages end at a box of side O(M).
So the rim top rows very likely lie outside C(u)^+. Then "fit those carriers" fails, and the enlarged-carrier allocation is the real input.
The note states both options. Repair: say which one applies, after checking the size of the final X against C(u)^+.

**6. Note 246-262 (Route 1). Y 72328-72334. CONFIRMED as a proof; MISMATCH as a route.**
Four prescribed bonds fix the plaquette. Minimizing cannot change it. Correct.
But HCM-SC replaces those four data by definition (§4, line 207-213). Route 1 keeps them.
So Route 1 does not attempt HCM-SC. The note itself calls it "a reuse of their face-lift obstruction" (line 258).
Only Routes 2 and 3 are real attempts. Stop (c) needs three.

**7. Note 264-347 (Route 2) and 349-433 (Route 3). CONFIRMED.**
(9): S_1 is a pure gauge of 1 with g=1 at top sites, so equal top data (SA 8090-8104 covariance).
The crossing angle is a·sin(2πη) ≥ 4aη for η ≤ 1/4 (sin y ≥ 2y/π). The matrix defect is ≥ 8aη/π. Correct.
Y 13405-13410 gives the factor L^{-2λ^W(p)}, and λ^W = 0 at a bare joined row. Correct.
Route 2 fails where stated: the auxiliary minimizer is not the stage minimizer.
(10) is SA (WI20), 16/n² (SA 9030-9033). Scope limit at SA 9049-9055. Correct.
(11): a_0+2a_1 = 1. The end-index argument and the tail argument are both correct.
(QC16) J_c = L^{-3}I_3 (SA 8193-8195). So a row error r needs pivot angle L³r. (12) follows. Correct.

**8. Note 435-471 (§6, consumers). rg -n -i "face.?lift" on Y: 37 hits; on I: 0 hits. MISMATCH (incomplete).**
The table covers every hit except these:
- Y 64088-64107. Prefinal reads: "At the exterior tower a tested holonomy is either the identity or the lifted top holonomy." Same obstruction at prefinal stages. The note's range stops at 64087.
- Y 71368-71382. Stage curvature estimate: "The remaining tests at the artificial join are the identity or lifted top plaquette holonomies." A direct consumer of the collar lift.
- Y 134088-134131. Cutoff comparison: the test-cube tower "admits the lifted datum at the test radius". Like Y 98111, it is unchanged by a collar-only change. It should still be listed.
I has no face-lift text. Add I 45115-45160 (tower localisation; coarse constraints across ∂X''' against finer ones; "a lemma on the boundary towers"). Any change of the collar tower reads it.

**9. A route the note did not try: no artificial descent at the outer boundary. I 43000-43004, 43128-43133; Y 12993-13016, 13063-13071, 72280-72306. UNCLEAR (proposed, concrete).**
Why the rim is bare. The joined sequence erodes each tower A_{a,q} from A_a^c, with gap μξ_{q+1} (Y 12993-12996, 13008-13016).
So the stage tower drops to level 0 at the artificial boundary ∂W. The new low rows get the face lift (Y 13058-13071).
I's determining-set hypothesis does not force this. The boundary tower t_X has only a lower bound: t_X(x) ≥ m when dist(x,∂X) ≥ 2M_1ℓ_m (I 43000-43004).

Statement (HCM-TB). On the outer joining collar, inside Ω_{j_a}, take Θ^a_q = A_a for q ≤ j_a toward the artificial boundary. Keep the erosion toward the old core.
Then the collar has only the ambient level-j_a rows. These are physical rows. There are no new rows and no face lift.
Define U^{pr}_{m,X} as Bałaban's constrained minimizer U(B,D) on this determining set (I 43128-43150).
- Exact averages: the collar rows are constraints of C(B,D). There are no lower artificial rows, so HCM-SC(1) is empty.
- Mesh factor: on rim plaquettes ℓ_B(p) = ℓ_m at the final stage. (1) then gives η²ℓ_B⁻² = L^{-2m}.
  The local form is Y's interior estimate (Y 72298-72306) with λ(p) = m. The rim joins the inset of Y 72311.
- Read set: the face lift is a function of the same top rows (Y 13063-13071). So the read set does not change. Y 72280-72281 still puts it outside the old floor.
- Locality: the minimizer on X reads only X. No padding and no restriction step, unlike Route 2.
This is Bałaban's minimizer with fixed averages on the rim layer. It keeps the averages exact by construction.

First open input of this route:
(a) The joined sequence loses its gap to W^c at the artificial boundary. Every user of that gap must be rechecked: the separation check (Y 13019-13034), R5-R6 erosions (SA 5694-5724), the collar comparison (Y 13315-13414), consecutive stages (Y 63864-63883), the prefinal reads (Y 64050-64107), and I 45115-45160.
(b) The minimizer and stage theorems are cited for Bałaban's own sets, which descend at ∂X: B_p(X) of CMP 122a and the maximal domains of CMP 109 (I 43059-43063). I states the minimizer theorem for every set of its definition (I 43128-43133), which includes this one. Whether Bałaban's proof covers a free boundary with top blocks must be read in CMP 102b and CMP 109 themselves.
(c) b_{m,X} ≤ a_sε_m/4 in (3) needs the rim far enough from the old carriers in weighted distance. With a final box of side O(M) (Y 63866), that comes from the compressed-shell factor Ř^{-c}, not from distance alone. Check it.

**10. The padded-layer idea (rim not tested at bare scale). Y 98117-98146, I 54985-55024 (b). CONFIRMED that it reduces to finding 9.**
Y 98117-98146 is the source's good case: the tested plaquettes sit in the top member, and the descent is outside them.
For the stage background, the rim is ∂X itself. Padding X to X' moves the bare layer outward. Then either R4 fails on X' (SA 5672), or the term reads outside X. The latter breaks I 54985-55024 (b), "only inside X".
So padding does not help unless the tower does not descend at ∂X. That is finding 9.

## Repairs

1. §4: state the supplier without fixing the joined geometry. HCM-SC is sufficient, not necessary.
2. §5: drop Route 1 as a route (keep it as the obstruction). Add finding 9 as a route, or name HCM-TB (a)-(c) as the first open input.
3. §6: add Y 64088-64107, 71368-71382, 134088-134131 and I 45115-45160.
4. §2 line 89-90: cite SA R4 (SA 5672-5676).
5. §3 line 152-157: check the final X against C(u)^+. Say which allocation is needed.
