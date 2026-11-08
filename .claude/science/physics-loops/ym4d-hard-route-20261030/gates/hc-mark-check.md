# Check of library/hc-mark.md (H-C-MARK)

Checker: Claude (Opus 5.5), one line-by-line reading, 2026-11-08.
Clone at `2bed22991` on `claude/ym4d-hard-route`.
Research text. Not an audit. Grants no status.

## Verdict: FIX

The proved steps are correct. The ported citations say what the note uses.
The scale example is stated faithfully.
The three routes are distinct, and each fails where the note says.

One gap changes the result. The note treats the source example as a rare worst case.
It is not rare. Under the literal rim test, failure is the typical branch (finding 9).
Then HCM-R (4) is very probably false, not open.
No unused payer or weighted accounting can save it.
The repair belongs in the construction of the rim layer, not in the ledger (finding 10).
The note should say this and redirect the next step.

## Findings

**1. Note 32-40 (scale example). Y 72324-72439. CONFIRMED.**
Birth at h=m-N_m by a pure gauge. Disjoint commuting rim field with top angle a=8ε_m L^{-2m}.
Wilson exponent Cθ_mε_m²L^{-4m} (Y 72370-72373). Fresh gauge and Gaussian payments O(|a|²) (Y 72421-72423).
The birth gauge payment is owned below the window (Y 72424).
The source calls it the first operation after the birth, not a renewal. The note's "renewed failure" is loose but harmless.
The note leaves out one source word: the mismatch occurs "even" for an averaged low-action field (Y 72340). See finding 9.

**2. Note 42-48. Y 72243-72323, 72470-72740; I 4209-4246, 49495-49546. CONFIRMED.**
The interior estimate works on the inset and uses λ(p) (Y 72296-72306).
I 4209-4246 cites Bałaban's ultraviolet theorem and says the large-field operation is "constructed in" CMP 122a/b.
I 49495-49546 lists application conditions outside the operator implication. Neither names a payer.

**3. Note 52-89 (§2, the smaller mark payment). IN1 (31), (32), Lemma 8 proof (in1.md 484-527). CONFIRMED.**
(2) is IN1 (31) with q_t=C_cnt T_t r̂_t. The chain of inequalities at 79-86 is correct.
IN1 itself only uses P_n/2 ≥ C_cnt T_n r̂_n (in1.md 520). So q_t per mark is exactly what the consumer needs.
This also matches SA's own ledger condition p_n ≥ C T_n r̂_n (SA 17719-17790, "the ledger").
q_t=O((log θ_t)^{6r}) is right: T_t~R_t, r̂_t~R_t^5.
Remark: HCM-R keeps 2P_h for every birth (note 213). (32) needs the leaf mass at one leaf only. This is slightly more than needed, but c_G P_h² ≫ 2P_h, so it does not matter.

**4. Note 95-133 (§3, retained payers). CONFIRMED.**
Y 76758-76777: stopped weight υ(p) ≥ cθ_t on the owned support. Y 76813-76816: mark halos have no corner in the floor. Y 76848-76855: gauge and Gaussian shares by original level and slot. Y 76933-76935: unused halves stay for the reference integral.
I 55379-55420: the older T_h is carried unchanged; retained Y_i keep their factors (CMP 122a (1.2), (1.11); 122b p. 390).
I 64835-64850: inherited raised cells stay live until the next completed R-operation. Stored data, not a lifetime estimate.
The conclusion "a retained share is available once" is correct.
Small mismatch: note 118 says Bałaban's credit "pays until the next event". SA 17719-17790 says SA's credit pays the whole wait up to k levels, and that Bałaban's (1.80) runs to K with summand O(1)M^dR_n^{d+1}d'_n. The note should quote that. It does not change the result (finding 10).

**5. Note 137-253 (§4, HCM-R and (5)). CONFIRMED as an implication.**
The weights in (3a) match the price in IN1 Theorem 10: (c+C_env+C_int)V° from (16), c_ent V° against (33), κ_1 per cell.
Backward induction is valid. Time strictly increases and the terminal level is finite.
(5): e^{-E}e^{q}e^{E-q-2P}=e^{-2P}. Correct.
HCM-R is the right shape for the consumer, and not stronger, apart from the remark in finding 3.

**6. Note 255-288 (§5, route one). CONFIRMED.**
Order of quantifiers is right: floor first, then unrestricted level. λ(p)=0 is in the source (Y 72426).
The restored-field island test has threshold cε_m on the restored field (Y 76878-76895). The rim defect is far below it. Correct.

**7. Note 290-405 (§6, route two). CONFIRMED.**
Plateau (L^{(j-1)/r},L^{j/r}] in log θ is right for R=⌈(log m)^r⌉ rounded to a power of L.
(9) obeys frame (1) for λ in [λ_low, B̄]. (10) uses x=θ ≥ Θ/2. (11) ratio ≥ c Θ/(log Θ)^{2p_0-4r-1}. Correct.
Order D/R marks with q~R^6 gives DR^5. Correct.
The note is honest that §6.1 is a symbolic schedule, not a field history. Finding 9 supplies the field.

**8. Note 407-506 (§7, route three). CONFIRMED.**
(13)-(14) are trivial and correct. (15): d=0 gives W_n=1; r=(1+e^{-d})/2 gives re^d=(1+e^d)/2>1. Correct.
Note 498-502: for fixed exterior top datum the four determining bonds fix the rim plaquette. This matches Y 72329-72334.

**9. The missed fact: the rim failure is generic. Y 72326-72340, Y 61905. UNCLEAR (strong; needs one check by the lead).**
The tested bare plaquette carries the face lift of V_m. Its defect is the level-m plaquette defect of V_m (Y 72332-72334).
The threshold is 3(1-β_s/2)ε_m L^{-2m}, with ε_m=g_mP_m.
In the small-field region a typical level-m plaquette defect of V_m is of size g_m=θ_m^{-1/2}.
The ratio of threshold to typical size is about 3P_m L^{-2m}. It tends to zero for large m.
So the test fails with conditional probability tending to one.
In the mass norm the exterior datum is a supremum. Any exterior defect between 3ε_mL^{-2m} and ε_m passes the ordinary tests and fails the rim test. Then failure is certain at that evaluation.
The Wilson energy of a typical failing datum is θ_m g_m² = O(1). There is no gain to extract.
At each later attempt m' the same holds at level m'.
Ordinary tests fail with probability about e^{-cP²} per cell, so a chain of D levels has no funded event with probability near one.
Consequence. In (3a), each renewal has continuation mass near one and price e^{(c+c_ent)ΔV}>1.
This is the toy (15) with r→1. F(s_first rim) must grow without bound in the terminal level, while e^{B_h} is fixed.
H_ρ is a majorant, so a lower bound on the actual integrand bounds every admissible H_ρ.
The free reserve c=C_vc_r can be taken large, so a bounded per-node normalized stage mass does not save (4).
What needs checking: that the face-lifted rim plaquette is tested at every final stage of every renewal, and that no earlier passed test bounds the rim plaquettes of V_m by ε_mL^{-2m}. The source example passes all earlier tests with a ≫ that bound only by a factor 8, so I see no such test.
If this holds, H-C-MARK stops at (b), with this history family. Note 518 and 520 then say too little.

**10. Concrete route: repair the rim layer, not the ledger. Y 61905, 72313-72321, I 55379-55420. UNCLEAR (proposed).**
Y 61905: the regular expansion needs background plaquettes within ε_kη_k² of 1. So the positive branch does need bare-scale smoothness.
The face lift does not give it: a bare plaquette with four lifted bonds carries the whole level-m holonomy.
Y 72318-72321 says a local-units bound gives the top threshold "only with an additional bound on the lifted top datum".
Proposed statement. On the final-stage rim, the bare determining bonds carry a smooth background of V_m (Bałaban's minimizer, or an interpolation with |∂U(p)-1| ≤ C L^{-2m} max|∂V_m-1|), not its face lift. Equivalently, test those plaquettes in the units of their joined level, after this interpolation.
Then a failure of the rim test forces a level-m plaquette defect ≥ cε_m of V_m.
The four-block certificate gives Wilson energy cθ_mε_m²=cP_m² (as in Y 76887-76895).
The rim top data lie outside the old floor (Y 72280-72281). So this is a fresh witness, and cP_m² ≥ q_m.
This is the ordinary plaquette certificate. HCM-R is then not needed.
Support from Bałaban: his R-operation on a component in the class has only geometric conditions (I 55379-55392). Retained regions keep their factors (I 55409-55420). There is no analytic rim test that can fail there.
Open in this route: the smooth interpolation must keep the averaging constraints exact on the determining set, and the stage domains R4-R6 must hold for it. This is a construction change. It needs owner approval as a change to a ported test.

**11. Note 130-133, 520-523 (scope). CONFIRMED, with one repair.**
The note says plainly that the Bałaban readings are mediated by SA and I. It claims no closure.
Repair: replace "HCM-R remains open" by "HCM-R is expected false under the literal rim convention (finding 9)". Point the next step at finding 10. Keep §2 and §4 as proved.

## Repairs

1. Add finding 9 as §7.3, with its check items. If confirmed, change the stopping condition to (b).
2. Add finding 10 as the next step in §8. Drop "an integrated estimate" as the main hope.
3. Note 118: quote SA's statement on Bałaban's (1.80) with K and d'_n.
4. Note 32: say "first operation after the birth", and quote "even" from Y 72340.
