lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T07:56Z

# support-physical: (D-F) on the physical label datum (queue row 96)

Provenance: Anthropic claude-opus-5-5, effort max, Mac mini worker, checkout `d4226aaf7`. Section 1 gates a Codex section (cross-provider read, one reader, not an audit, no status); Sections 2-7 are new proofs by the same model, **ungated**. Sources: Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), `YM4_sketch_500.tex` ("SA n") and `theorem_0_complete_account_raw_I.tex` ("raw I n") at `31a47c543775`, fetched once into a private scratch folder; T. Balaban, CMP 119 (1988) 243-285, OCR in `~/ym4d-papers/` (read in place, not copied). Balaban CMP 122 (1989) is not in hand. No numeric job was run (memory 64 percent free; none was needed).

**Moves:** `library/route-decisions.md` position H (Package C rank 1, floor screening): the support input (D-F) of `library/floor-screen.md` Theorem R, on the physical label datum V_l on Γ_l of the old core (SA 17709).

## 0. Result

| Item | Verdict or status |
|---|---|
| `support-envelope.md` §15, initial strip (15.1) | ADVANCE |
| §15, positive-level ordinary read and ordinary seams | ADVANCE |
| §15, its read sets against CMP 119 | confirmed; one non-breaking difference at the first step (D1) |
| Healed draws of older operations (§4 here) | proved, bound 2ε_s; **Proposition 2.4 is not used** |
| Islands, the second-class draws (§5) | proved given Proposition 2.4 (cited-pending) and reading R1 of the cut-off; under the other reading, (D-F) fails |
| Inherited raised cells and drop-out bare integrals (§6) | proved from the arrested attempt's own passed stage tests |
| (D-F) on the physical label datum, every case (§7) | proved, conditional on Proposition 2.4 (islands only), R1, and the outline's read sets (CMP 119 (3.1)-(3.5); SA 17624) |

The case list is complete by raw I's list of level-assigning operations (§2). Healed draws need no Proposition 2.4, so the gate's statement that older draws read Proposition 2.4 narrows to islands. Raw I's inherited-datum hypothesis concerns a different quantity, the near-group total, and is not needed here.

## 1. Gate of `support-envelope.md` Section 15

**Read sets, checked against the CMP 119 OCR.** First step (pp. 246-248): (1.4) is χ_1(□') = 1{sup over p ⊂ □'^~ of |U_{1,□'}(V,∂p) − 1| ≤ ε_1 L^{−2}}, with U_{1,□'} = U(B_1(□'^{~4}), M^·(Q_1^* V)) from (1.2). (1.8)-(1.9) give χ'_0(□') = 1{|U(b)U_{1,□'}(b)^{−1} − 1| < 2δ_0 on (□'^{~2})^*}, where * keeps every bond with an end point in □'^{~2} except the pivots b_0(c) of coarse bonds c touching □'^{~2}, and δ_0 = (A_1/A_0)ε_0. Ordinary step (pp. 264-265, (3.2)-(3.5)): plaquette tests on the cubes of (Z_k^{~4})^c; gauge fixing outside P'^~ ∪ Z^{~5}; approximate tests (3.3)-(3.4) on (P'^{~2} ∪ Z^{~6})^c with reference V_k^{(□)} = M^k U_{k+1,□}; and Ω_{k+1}^c = Q'^{~2} ∪ P'^{~4} ∪ Z^{~8}. These are the read sets of the note's 14.1 and the layer numbers of SA 17320.

**(15.1), initial strip: ADVANCE.** I redid each step:

- The clearances (10.1).
- The approximate test at D was made, since C misses P'^{~2} and there is no older region.
- Both tests passed, since C is in neither Q'_1 nor P'_1.
- The footprint inclusion: the bonds of p and the double blocks of its at most four pivot rows lie within 4L of the corner, which is inside D^~ once the test side exceeds 8L.
- The top member of D's tower contains D^~ (14.1; gate of row 94, §1(c)), so M(W)(c) = V_1(c) = M(V_0)(c).
- The pivot lemma, then (3.3).

The rows read only their own pivot (SA 8167-8175), and * removes exactly the pivots. The pivot lemma and (5.1)/(5.3) are inputs, so I re-derived them:

- In a row, L of the L^4 parallel segments cross the pivot, so w = L^{−3}.
- (4.2) and the choice wE + La + b ≤ πw/4 keep P and the off-pivot closed transports a fixed distance from −1.
- d/dt[e^{(1−t)X}e^{tY}] = e^{(1−t)X}(Y − X)e^{tY} gives ‖e^X − e^Y‖ ≤ ‖X − Y‖.
- At the flat field the pivot derivative of the row logarithm is wI: +I from the central transport, and −(1 − w)I from the off-central closed transports.
- (5.2) is the Stokes sum over the L×L squares of the L^4 segments, with total weight L².
- The iteration (5.3) closes under exp(2K_L ε/(L²(L²−1))) ≤ 2.

No defect in either.

**Positive-level ordinary read and ordinary seams: ADVANCE.**

- A test loop with a bond in Γ_t has an end point in Ω_t (SA 9607).
- The chosen cell avoids Ŷ^{~8} and P'^{~4}, so χ_t(D) was made outside the four-cell margin and passed.
- At step t the delta function gives V_t = M(V_{t−1}) on every coarse bond, so a mixed test equals ∂V_t(p') of the step-t field, and (5.3) gives 2ε_t.

The note uses (3.1). The value is the same, fixed at the coarse side's birth (§3 here).

**Defects (none breaks the section):**

- **D1 (non-breaking).** CMP 119's own first step has a level-0 large-field set P_0 with one-layer margins ((1.2) tests on (P'_0^~)^c; (1.10)). The outline has none: ρ_0 is the bare Wilson density, and SA 23265 starts the determining set at Ω_0 = Ω_1^~. So Y = ∅ at step 1, as the note says. With P_0 present the clearances would be dist(C, Q'_1) ≥ 2, dist(C, P'_1) ≥ 3 and dist(C, P'_0) ≥ 4, and the proof is unchanged.
- **D2 (scope).** "Ordinary" must mean that the coarse bonds received their values and level at T_t, with an end point in Ω_t as set by step t. Parts of the current Ω_t added later by a completed decision or a preparation raise are the cases of §§4-6 here.
- **D3 (support).** §15 carries (15.1) forward by §4's persistence of values. Persistence **on supports** also needs the passed indicators to stay in force after the factors are reorganised. Lemma P (§2) supplies this.

Section 15 does not treat draws, raises or collar lifts, and says so.

## 2. Persistence on supports, and the birth inventory

**Setting.** R acts at level m on a class component X with bottom m_b. O = Ω_{m_b}^c ∩ X is the old core, and its label datum is V_l on Γ_l with l ≤ m_b − 1 (SA 17709). By the repaired Lemma G and gate row 94 §3(i), every floor test of Theorem R is a test loop of this datum.

**Lemma P (persistence on supports).** Fix a history h and its kernel K_h, a composition of positive outcome kernels (SA 7462-7469, Proposition 1a.2.3). The *support* is the set of bare fields, stored and integrated variables and draws at which the integrand of K_h is nonzero.

- **(a)** If h records an indicator as passed, it equals 1 on the support, at the values its arguments had when it was evaluated.
- **(b)** A stored bond variable keeps its value, up to a simultaneous gauge transformation, until an operation takes it out of the determining set. New values arise only at three kinds of birth:
  - a step T_t, whose delta function makes V_t = M(V_{t−1});
  - a preparation raise, which makes V_i = M(V_{i−1}) and keeps the bare integral (SA 17654);
  - the draw of R, which changes V_k on b_X, the level-k bonds with an end point in Λ^pr (SA 22749, 17604), and nothing else.
- **(c)** Hence the following holds at every later point of every support, for as long as a test loop's bonds stay determining: any gauge-invariant bound on the test loop that follows from (a) and from the reference law's support, at the last birth of its bonds.

*Proof.*

- **(a)** A history records every outcome (SA 17407). Each decomposition of unity puts into the kernel of the recorded outcome the product of its passed indicators and failed complements. Later kernels multiply nonnegative factors and integrate. A factor the outline later drops is dropped because it equals 1 on the support of the others (Lemma 2.2 (a), SA 17369), so the integrand does not change. Proposition 1a.2.3 says the outline's terms are these kernels exactly. If a dropping claim failed, the term would differ from the kernel, and that would be a defect of the claim. The support defined here would not change.
- **(b)** Steps store the level-k variables on Ω_k \ Ω_{k+1} unchanged (CMP 119 (3.1)). The linearising changes of coordinates (CMP 119 p. 249; SA 17523) are invertible, and the physical value is read through the inverse. Gauge fixing, trees and the frame sum act by gauge transformations, which conjugate plaquette holonomies. A completed decision removes the old determining layers of its component (SA 17416-17420). The main step of R integrates V_k on b_X only, and the reference law redraws it there (SA 17585, 17604).

Part (c) follows from (a) and (b). ∎

**Birth inventory.** Raw I (lemma on the base below the level, Step 1, raw I 64643-64660) lists the only operations that assign a level to a cell:

- (i) T_t on Ω^T_t;
- (ii) a completed first-class decision of R_t on its component;
- (iii) a completed second-class decision;
- (iv) a preparation raise of R_t, which persists while its attempt is arrested and live.

A completed decision re-levels its whole component and supersedes (iv) of the same attempt. The present operation does not touch O: O ⊂ X ∩ Z_{m_b} = C_{m_b}, because Λ_{m_b} ⊂ Ω_{m_b} (SA 17709), and the core is never unfolded (SA 17598). Quarantine (SA 17575) and "marks wait" (SA 17440) put every earlier operation that acted in X at a level below m_b. So each bond of the datum in O at level l last received its value and its level at exactly one of the following:

| Case | Birth | Certificate |
|---|---|---|
| T | step T_l | `support-envelope.md` §15, gated above |
| H | first-class decision of R_l (healed) | §4: the decision test and the quiet step-l tests |
| I | second-class decision of R_l (island) | §5: stage tests, reference-law cut-off, Proposition 2.4 |
| A | raise to level l by a live arrested attempt (drop-out) | §6: the attempt's own passed stage tests |

Artificial collar lifts are not physical label data, and Theorem R does not read them (gate row 94 §3(i)).

## 3. Seams across origins

A mixed test τ of level t uses M(V_{t−1}) on its finer-layer bonds (SA 9616). It is certified at the birth of its coarse side, whatever the origin of the finer side:

- **T.** At step t the delta function gives V_t = M(V_{t−1}) on every coarse bond, so τ = ∂V_t(p') of the step-t field, which is §15's case.
- **H, I.** After the decision, the component X' and its surroundings lie in Ω_t, since outside X' lies Λ_t ⊂ Ω_t. So no level-t seam meets X' at that moment. A seam made later near X' is born at a later step, as case T at the higher level.
- **A.** Inside a raised region, τ = ∂(M^t U')(p') exactly (§6).

Afterwards Lemma P(b) keeps every value τ reads until one of its bonds is reborn. A raise keeps the value: M(V_{t−1})(b) becomes the stored V_t(b). A redraw happens only inside a component whose decision re-levels it. Then τ is no longer a test of the datum, or it is a new test with its own birth.

## 4. Case H: healed draws, without Proposition 2.4

**Proposition H.** Let R_s act on a class component X' with a first-class decision, and let V_s be the field after the decision: drawn on b_{X'}, unchanged elsewhere. Then on the support every level-s plaquette p' with a corner in X' satisfies |∂V_s(p') − 1| ≤ 2ε_s.

*Proof.* Quiet free evolution gives X' = H^{[10]} and X' ∩ Ω_s^c = H^{[8]}, where H is the cell hull of X' ∩ Z_{s−1}. Step s creates nothing in X' (SA 17575-17583; the quiet condition includes i = s). The decision is χ_s(X'^{~−6}), the step test χ_s of the new field (raw I 51742-51748; SA 17838 (v)). A layer of ~ is at most one cell, so X'^{~−6} ⊃ H^{[4]}.

Two inclusions are needed.

- **(α) Λ^pr ⊂ H^{[1]}.** Λ^pr has side at most CM level-s spacings. It contains the core C_{s_b} ⊂ X' ∩ Z_{s−1} ⊂ H (SA 17585; the Z_i ∩ X' are nested under quiet evolution). A cell has side MR_s > 2CM under the ceiling.
- **(β) Ŷ^{~4} ∩ X' = H^{[4]}, with Y = Z_{s−1}.** X' ∩ Z_{s−1} is a single box (single boxes, SA 17575). Any other cell of Ŷ within ten cells of X' would lie in the component X' of Z_s ⊃ Ŷ^{~10} (SA 17320: Ω_s^c ⊃ Ŷ^{~8} and Z^{[0]} ⊃ (Ω_s^c)^{~2}).

Fix a corner y ∈ X' of p', a level-s cell C ∋ y in X', and a test cube D ∋ y in C, taking closures at partition faces. There are two cases.

- **(i) C ⊂ H^{[4]}.** Then D ⊂ X'^{~−6}, so χ_s(D) is a factor of the passed decision, evaluated at V_s. It equals 1 on the support by Lemma P(a).
- **(ii) C ⊄ H^{[4]}.**
  - H^{[4]} is a union of cells, so C misses it, and by (β) C also misses Ŷ^{~4}.
  - The step-s plaquette test is made on every test cube outside Ŷ^{~4} (CMP 119 (3.2); SA 17317). So χ_s(D) was made at step s, and it passed, because step s creates nothing in X'.
  - Its read set D^{~4} lies within five test-cube sides of C, at most 5MR_s/L² < MR_s. C is a full cell away from H^{[3]}, which contains Λ^pr by (α). So D^{~4} misses b_{X'}, the draw leaves its field unchanged, and χ_s(D)(V_s) = 1 on the support.

In both cases W = U_{s,D}(V_s) has curvature below ε_s, in level-s units, on D^~ (the form of CMP 119 (1.4)). D^~ contains the s-fold footprint of p', which lies within 3ξ_s of y. The top member of D's tower contains D^~ (14.1), so M^s W = V_s on the four bonds of p'. Then (5.3) gives |∂V_s(p') − 1| ≤ 2ε_s. ∎

The cut-off, the centre V_Λ and Proposition 2.4 do not enter: the healed field is certified by tests of the field itself. After the decision X' and its surroundings lie in Ω_s, so every level-s test loop meeting X' is a plain plaquette (§3).

## 5. Case I: islands (second-class draws)

**Proposition 2.4, exactly as the outline states it (SA 17656). Cited-pending: Balaban, CMP 122 (1989) 175, Proposition 1, not in hand. The outline says Balaban states it on fields of mild regularity, for ε sufficiently small, with the bound CM^5 ε.**

There are a radius a_Λ > 0 and a constant C(M), both chosen after M and before γ, with the following property. Let R act at level k on X with box Λ^pr.

- *Hypothesis.* The exterior data satisfy |∂V_k − 1| < ε, with C(M)ε ≤ a_Λ.
- *Class.* Let 𝒞 be the class of continuations with |∂V_k − 1| < a_Λ at every level-k plaquette whose corners all lie within distance 1 of Λ^pr.
- *Conclusion.* On 𝒞 the localised background U_{k,X}(V_k) exists. The map V_k|_{Λ^pr} ↦ A(U_{k,X}(V_k)) is a function of V_k on b_X, the level-k bonds with an end point in Λ^pr. In 𝒞 it has exactly one critical gauge orbit V_Λ. This orbit is the set of its minima in 𝒞, is analytic in the data, and satisfies |∂V_Λ − 1| ≤ C(M)ε. Moreover J(U_{k,X}(V_Λ)) = 0 in Λ^pr.

*Readings used:*

- The bound |∂V_Λ − 1| ≤ C(M)ε holds at the plaquettes of the class, with distance taken as lattice ℓ^∞ distance. These include every plaquette with a bond in b_X.
- "Exterior data" are the level-k plaquettes with no bond in b_X, in the region the localised background reads: X, with its lifted collar. A lifted plaquette is 1 or an exterior plaquette (`support-envelope.md` §6), so it obeys the same bound.

**Reading R1.** "The bonds of the box" in the cut-off χ(Λ^pr) of SA 17604 are the law's variables, b_X. This is the set Proposition 2.4 names and the set SA 22749 changes. `support-envelope.md` §10.2 raised the point. The next paragraph shows that R1 is necessary.

**Counterexample under the other reading.** Suppose the cut-off reads only bonds with both end points in Λ^pr.

- *The draw.* Take a crossing bond b ∈ b_Y off the tree of δ_ax; all crossing bonds but one are off it. Put V' = 1 except V'(b) = exp(iθσ_3). By (3.3), every plaquette p' through b has |∂(V'V_Λ)(p') − 1| within C(M)ε of ‖e^{iθσ_3} − 1‖ = 2 sin(θ/2). Choose 2 sin(θ/2) ∈ (a_Λ/2 + C(M)ε, a_Λ − C(M)ε), which is a non-empty interval once C(M)ε < a_Λ/4. Then a_Λ/2 < |∂(V'V_Λ)(p') − 1| < a_Λ. So V'V_Λ ∈ 𝒞, the Wilson weight of the law is positive and continuous there, and an open set of such draws lies in the support.
- *The test fails.* Let D be the test cube at p'. If χ_s(D) were 1, (5.3) would give |∂V_s(p') − 1| ≤ 2ε_s < a_Λ/2. So χ_s(D) = 0.
- *The decision is second class.* D ⊂ H^{[1]} ⊂ Y^{~−6}, and the earlier tests are evaluated before the draw. Admitted histories that reach the draw with positive mass exist: the flat histories of `support-envelope.md` §§16, 20-22, admitted by gate row 94 §1.
- *The island datum.* The island keeps V_s on Y as its datum (raw I, Remark 4.21 (c): the single domain Y^{(s)}), with a plaquette above a_Λ/2. a_Λ is fixed, while C R_s² ε_s → 0 under the ceiling, so (D-F) fails at level s on an open part of the support.
- *It reaches a floor.* Y is a mark (SA 17440). In a later class component containing it, Y ⊂ Z_{t'} for s ≤ t' < m (raw I, lemma on the base below the level), so Y lies at least eight level-m_b cells from Ω_{m_b} and its cells are floor cells.

Not constructed: the full admitted later history. The template is the late quiet components of `support-envelope.md` §§16, 18. Balaban's (1.102) also lacks the cut-off (SA 17642), so the same remark applies to his version.

**Proposition I.** Assume R1 and Proposition 2.4. Let R_s act on Y with a second-class decision, and let V_s be the island datum: drawn on b_Y, unchanged elsewhere. Put ε := 7L²R_s²ε_s, and let the ceiling give C(M)ε ≤ a_Λ. Then on the support every level-s plaquette p' with a corner in Y satisfies

  |∂V_s(p') − 1| ≤ C_I R_s² ε_s,  C_I := 7L²(C(M) + 1) + 4M_0.

*Proof.* As in §4, Y = H^{[10]}, step s is quiet in Y, and Λ^pr ⊂ H^{[1]}. An island's decision is the only test that fails (SA 17418), so h records every earlier test of R_s on Y as passed. That includes the curvature test of the final stage background U^{(N)}, under either reading of when stage tests are made (§6). By Lemma P(a) all of them hold on the support. There are three kinds of plaquette.

- **(i) p' has a corner in a cell C ⊄ H^{[4]}.** Then p' misses b_Y. As in §4 (ii), χ_s(D) passed at step s on a read set that misses b_Y, so |∂V_s(p') − 1| ≤ 2ε_s.
- **(ii) p' misses b_Y and has a corner in H^{[4]}.**
  - Outside Λ^pr every layer has been raised to level s (SA 17585: Λ^pr holds the stacked shells). So M^s U^{(N)} = V_s on the bonds of p'.
  - The footprint of p' misses Λ^pr, which is a union of level-s blocks, and lies at least five cells inside ∂Y.
  - There the passed test bounds U^{(N)}, in the region not covered by the shells, by (1 − β_s/2) c_l L_♭^{2e} ε_s η_s², with c_l ≤ 3 and e ≤ (s − j_0)_+ (SA 17624; j_0 = s_♯ + 1).
  - By (11.4), L_♭^{2e} ≤ L^{2(s−j_0)} = R_{j_0}² ≤ L² R_s². So in bare units the curvature is below 3L²R_s²ε_s L^{−2s}, and (5.3) gives |∂V_s(p') − 1| ≤ 6L²R_s²ε_s.
  - The draw does not change these values (Lemma P(b)).
- **(iii) p' meets b_Y.**
  - By (i) and (ii), the exterior data are below ε at the draw. Just outside Y they are bounded by the step-s tests, case T, at 2ε_s. Lifted plaquettes obey the same bounds. None of these values changes afterwards.
  - The centre V_Λ, in every frame r (SA 17585: the frame sum keeps a cut-off and a tree per summand), is Proposition 2.4's orbit element for these data. So |∂V_Λ − 1| ≤ C(M)ε at every plaquette meeting b_Y.
  - Under R1 the law's support gives |log V'(b)| < M_0 ε_s on all of b_Y. Then (10.3), proved from (3.3) and ‖e^{iA} − 1‖ ≤ ‖A‖ and rechecked, gives |∂V_s(p') − 1| ≤ C(M)ε + 4M_0 ε_s ≤ (7L²C(M) + 4M_0) R_s² ε_s.

All three bounds are gauge invariant, so the tree representative and the frame do not matter. ∎

This is the only case of (D-F) that reads Proposition 2.4. It reads it with ε of order R_s²ε_s, not ε_s, which the proposition allows, since its only condition is C(M)ε ≤ a_Λ.

## 6. Case A: inherited raised cells and drop-out bare integrals

**Setting** (SA 17419, 17440, 17642; raw I 64796-64870, the definition of raised cells and arrested attempts). An attempt a of R_t on X_a, with t = k_a < m_b, is arrested. Either it is a drop-out after n stages (some test of (1)-(3) failed), or it was excluded after all N_t stages. An attempt excluded before any stage raises nothing. Its preparation raised the cells of X_a \ Z''_i(X_a) to the levels i ∈ (t_b, t_b + n^+] (raw I 64817). While a is live:

- the raises persist, and no cell is raised twice (raw I 64865);
- no later step re-levels X_a, since no point of X_a lies in Ω^T_{t'} for t < t' ≤ m (raw I, lemma on the base below the level);
- the drop-out keeps the bare integrals ∫dV_{i−1} δ(M(V_{i−1})V_i^{−1}) of the levels already treated (SA 17642), so on the support V_i = M(V_{i−1}) on every raised bond. Its determining sequence is ν = n (SA 17440).

**Proposition A.** On the support, every test loop τ of level i of the datum on cells raised by a live arrested attempt satisfies

  |∂V(τ) − 1| ≤ C_A R_i² ε_i,  C_A := 6L⁶K,  with K = 2^{p_0+1} as in (11.2).

*Proof.* Let q be the stage whose integration gave τ's coarse bonds the level i = t_b + q. The tests of a stage are made before its integration (SA 17585), and SA 17612-17624 calls the curvature test of U^{(n)} the test "after n stages". So before the q-th integration, h records a passed curvature test of U' := U^{(q)} or of U' := U^{(q−1)}, according to whether the test after q stages precedes the q-th integration or follows the (q−1)-th. The proof covers both readings.

**(a) Identity: τ = ∂(M^i U')(p') exactly.** On the determining bonds of U''s sequence, M^l U' = V_l, which is the constraint of the background (SA 9616).

- If U' = U^{(q)}, this is the claim for τ's coarse bonds, and finer-side factors are M(V_{i−1}) = M^i U'.
- If U' = U^{(q−1)}, τ's bonds lie in that sequence's level-(i−1) territory. The raise sets V_i = M(V_{i−1}) = M(M^{i−1}U') = M^i U' by the semigroup.

Later stages do not change level-i values in the stratum Z''_{i+1} \ Z''_i (no cell is raised twice; Lemma P(b)).

**(b) Bound.** The passed test bounds the bare curvature of U' on τ's footprint. The footprint lies within 3ξ_i of a corner of p'. It misses Z''_{i−1}, and so the attempt's core: a stratum of width at least Mξ_i or two level-i cells separates them (`support-envelope.md` §17).

- By SA 17624 the thresholds are:
  - (1 − β_s(1 − 2^{−(j−i'+1)})) L_♭^{2(i'−j_0)_+} ε_{i'} η_{i'}² on a shell of level i' ≤ j;
  - (1 − β_s/2) c_l L_♭^{2e} ε_j η_j², with c_l ≤ 3 and e ≤ (j − j_0)_+, in the region not covered by the shells at stage j.
- By (11.4) these are at most 3L²R_{i'}²ε_{i'} L^{−2i'} and 3L²R_j²ε_j L^{−2j} respectively.
- The footprint meets only levels i' ∈ {i − 1, i}. With U' = U^{(q−1)} it lies in level-(i−1) territory outside the shells, at the stage scale j = i − 1.
- Use R_{i−1} ≤ LR_i (11.3), ε_{i−1} ≤ Kε_i (11.2) and L^{−2(i−1)} = L²L^{−2i}. Then the bare curvature is below 3L⁶KR_i²ε_i L^{−2i} on the whole footprint.
- (5.3) with ε := 3L⁶KR_i²ε_i, admissible under the ceiling (7.1), gives |∂(M^i U')(p') − 1| ≤ 6L⁶KR_i²ε_i.

**(c) Persistence.** By Lemma P(a) the recorded test holds on the support, and by (b) of that lemma and raw I 64865 the values persist while a is live. ∎

**What this uses.** Neither Proposition 2.4 nor raw I's inherited-datum hypothesis is used. That hypothesis (raw I 68420-68437) bounds a near-group total, an analytic data constant; raw I marks it "Proof outstanding", and it is a different statement. Raw I's Remark 4.21 (b) is right that the present preparation's bound, CMP 122a (1.24), says nothing on the inherited cells W. The bound comes instead from the earlier attempt's own test, by persistence.

**Readings, and what is out of scope.**

- Excluded attempts after all stages (raw I's branches B5-B7) are covered with q ≤ N.
- The branch-(B4) stored collar terms are functions, not datum, so they are out of scope.
- The domain reading: SA 17624's "on that shell" and "in the region not covered by the shells" cover every raised cell's footprint. Raw I's row list for CMP 122a (1.24) (raw I 68302-68310: thin strata, Ω^c_{k_0+1} \ Z''_j, original shells, and Ω_{j−1} \ Ω_{j+1}) agrees. If the formation data test less, the inclusion must be restated, the same caveat as 14.1.

## 7. Theorem: (D-F) on the physical label datum

**Theorem.** Let R act at level m on a class component X with bottom m_b, and put O = Ω_{m_b}^c ∩ X. Assume:

- **(H1)** the outline's step rule, with CMP 119's read sets (`support-envelope.md` 14.1; SA 17317-17341);
- **(H2)** the stage tests of SA 17612-17624, with the domains read in §6, as recorded outcomes of R;
- **(H3)** reading R1 of the reference-law cut-off;
- **(H4)** Proposition 2.4, cited-pending and used only in §5;
- the ceiling (7.1).

Then on the support of every history, every test loop τ of level l of the label's datum in O satisfies

  |∂V(τ) − 1| ≤ C_F R_l² ε_l,  C_F := max{C'_L, 6L⁶K, 7L²(C(M) + 1) + 4M_0},

where C'_L is the constant of (15.1). C_F is fixed after M and before γ.

*Proof.* By §2, each bond of τ last received its value and its level at a birth of kind T, H, I or A. By §3, a mixed test is certified at the birth of its coarse side. The bounds at birth are:

- T: (15.1), and 2ε_t from §15 (using R_l ≥ 1);
- H: 2ε_s (Proposition H);
- I: C_I R_s² ε_s (Proposition I);
- A: C_A R_i² ε_i (Proposition A).

Lemma P carries each of them to every later support while τ's bonds stay determining. ∎

**Ceiling (7.1).** Choose γ so small that, at every level l:

- ε_1 L^{−2} ≤ κ_L and 2δ_0 ≤ h_L (the pivot lemma);
- 2ε/L² ≤ a_L and exp(2K_L ε/(L²(L²−1))) ≤ 2 at ε = 3L⁶KR_l²ε_l ((5.3));
- 7C(M)L²R_l²ε_l ≤ a_Λ (Proposition 2.4);
- R_l > 2C, so that Λ^pr ⊂ H^{[1]}, and test sides exceed 8ξ (the footprints).

All of these hold for small γ. Every frame value is at least γ^{−2} (SA 7470), so R_l ≥ (log γ^{−2})^r. Also R_l²ε_l ≤ L²A_0 sup over θ ≥ γ^{−2} of θ^{−1/2}(log θ)^{2r+p_0}, and that function decreases for θ ≥ e^{2(2r+p_0)}, so this tends to 0. No step uses a computed value.

**Consumer.** `floor-screen.md` Theorem R, as repaired in `gates/floor-screen-gate.md`, reads (D-F) only at floor tests, and these are tests of this datum (gate row 94 §3(i)). With this C_F, Lemma T gives A_F = 4L²C_F R_m² ε_m. C_F depends on M, and Theorem R needs it fixed before γ (its Step 4 limit), which holds. So (D-F) leaves Theorem R's list of open inputs; (H1)-(H4) take its place.

## 8. Counterexample attempts, what changes, what stays open

**Attempts to kill (D-F), made first:**

- **Healed draws.** I looked for a gap between the decision domain X'^{~−6} and the step-s test domain. There is none: X'^{~−6} ⊃ H^{[4]}, and the step tests cover X' \ H^{[4]} (§4 (β)).
- **Islands.** Under the narrow reading of "bonds of the box", an admitted island has a crossing plaquette above a_Λ/2 on an open part of its support (§5). That attack succeeds, so R1 is necessary.
- **Drop-outs.** The test that failed may be the curvature test of the drop-out's own sequence. The proof then reads the previous stage's test, at an extra cost of L⁴ (§6, both readings).
- **Seams across origins.** Every seam is certified at its coarse side's birth (§3).

None gives an admitted violation under R1.

**For the lead:**

- (a) The open list of gate row 94 §3 changes. Older healed draws, inherited cells and drop-out bare integrals are proved here (ungated). Older island draws are proved given Proposition 2.4.
- (b) R1 should be recorded as the reading of SA 17604.
- (c) Theorem R's other inputs are unchanged: (D-far)/(EA), (A1-S), (A3-P) or the repaired (OS-loc), and the rest of (S1).
- Reversal test 4.3 is not affected.

**Hardest remaining input of (D-F): Proposition 2.4** (CMP 122, Proposition 1, not in hand), needed for islands only. If it fails, island data are regular only at the fixed radius a_Λ, and (D-F) fails on every floor that contains an island. Theorem R would then need islands kept out of floors, or their datum tested again. That is the evidence that would reopen position H's support input.

**Unverified readings.** (H1) rests on the outline's statement that its layer numbers are Balaban's (SA 17320). (H2)'s domains rest on the words of SA 17624 and raw I's row list for CMP 122a (1.24), which is not in hand.

**Not addressed** (Theorem R does not read them): artificial collar lifts of retained old functions, and raw I's inherited-datum hypothesis on the near-group total.

**Gate needed.** §§2-7 are one model's work. A cross-provider gate should check Lemma P(a) on dropped factors, §4 (β), Proposition I (ii) (the domain of the last stage's test), and the level bookkeeping of Proposition A (b) under both readings.

RESULT: Section 15 of `support-envelope.md` gated ADVANCE: the initial strip (15.1), the positive-level ordinary read and the ordinary seams, with read sets confirmed against CMP 119 (1.4), (1.8), (3.2)-(3.5) and one non-breaking first-step difference. (D-F) on the physical label datum is proved (ungated) for every case on the support: healed draws at 2ε_s without Proposition 2.4; inherited raised cells and drop-out bare integrals at 6L⁶K R²ε from the arrested attempt's own passed stage tests; islands at (7L²(C(M)+1)+4M_0) R²ε, given Proposition 2.4 (stated exactly, cited-pending) and reading R1 (the cut-off covers every changed bond b_X, without which an admitted island violates (D-F)). Hence C_F in Theorem R is fixed after M, before γ. Open: Proposition 2.4 (CMP 122 Proposition 1, islands only), the CMP 122a stage domains behind SA 17624, a cross-provider gate of §§2-7, and Theorem R's other inputs ((D-far)/(EA), (A1-S), (A3-P)/(OS-loc), (S1)).
