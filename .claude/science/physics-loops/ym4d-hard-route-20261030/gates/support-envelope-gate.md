lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T07:22Z

# Gate: `library/support-envelope.md` Sections 16-23 (queue row 94)

Provenance: Anthropic claude-opus-5-5, effort max, Mac mini worker, checkout `5dc2520b9`; gate of a Codex note (cross-provider read, one reader, not an audit, no status). Sources: Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), `YM4_sketch_500.tex` and `theorem_0_complete_account_raw_I.tex` at `31a47c543775`, fetched once into a private scratch folder ("SA n" and "raw I n" are their line numbers); T. Balaban, CMP 119 (1988) 243-285, read from `~/ym4d-papers/` (OCR checked against the rendered scan of journal pp. 246, 256, 257; not copied). No numeric job was run (memory 62 percent free; none was needed).

**Moves:** `library/route-decisions.md` position H (Package C rank 1, floor screening) and its first reversal test (4.3, first bullet).

## Verdicts

| Section | Verdict | Note |
|---|---|---|
| 16 late flat creation | CORRECT-NO-ADVANCE | geometry only; checked against SA 17317 (raw V_k compared with the block-axial average) |
| 17 prepared-shell geometry | CORRECT-NO-ADVANCE | only the containment core ⊂ Λ^pr with one level-s M-cube layer is used later (SA 17598) |
| 18 old collar in a later floor | CORRECT-NO-ADVANCE | not used by 22 |
| 19 | superseded | not gated |
| 20 reference-law support | ADVANCE | cutoff SA 17604, centre 1, positive mass at each fixed s |
| 21 cube test across the old floor, (21.2)-(21.3) | ADVANCE | CMP 119 (1.3), (2.13), (2.16); SA 9783 (c); SA 17838 (v); raw I 51737-51753 |
| 22 admitted history, (22.4)-(22.7) | ADVANCE | the history is admitted and (22.7) holds; one non-breaking frame remark (D3) |
| 23 scope; source-level indexing | CORRECT-NO-ADVANCE | the implication to the common floor amplitude is Lemma T |
| 23 admission gate (23.1) | WRONG as a repair | its rejection branch contains fields of typical size and carries no gain (D1) |

**First failing step:** none in the refutation (Sections 16-22). The first failure in Sections 16-23 is the proposed repair (23.1).

**Route question:** `library/floor-screen.md` Theorem R, as repaired in `gates/floor-screen-gate.md`, goes through unchanged with source-level indexing; the counterexample is not in its scope (Section 3 below). **The reversal test of `route-decisions.md` 4.3 has not fired** (Section 4).

## 1. Is the history of Section 22 admitted? Yes

Each rule named in row 94 was checked against its source text.

**(a) Reference-law cutoff (SA 17604).** The law is δ_ax(V′) χ(Λ^pr)(V′) e^{−x_k A(φ_X, U_{k,X}(V′V_Λ))} over its normaliser. Here V′ = V_k V_Λ^{−1}, and χ(Λ^pr) = 1{|(1/i) log V′(b)| < M_0 ε_k on the bonds of the box}, with M_0 "chosen large after M". The threshold is ε_k = ḡ_k p_0(ḡ_k) of the frame (SA 6031), so ε_s = ε(T) when θ_s = T. At a flat exterior, V_Λ = 1. The weighted Wilson function is ≥ 0 and vanishes at V = 1. Proposition 2.4 (SA 17656) makes the critical orbit the set of minima, and its tree representative is 1. The draw (22.3) puts exp(8iε_s σ_3) on one non-tree edge of P and 1 everywhere else. It lies on the tree slice, it has |(1/i) log V′| = 8ε_s < M_0 ε_s once M_0 > 8, and its curvature 2 sin(4ε_s) is inside Proposition 2.4's fixed class. Near the draw, the numerator is a positive continuous density in the non-tree coordinates. The normaliser is finite and positive.

The incoming mass is positive at each fixed s. All passing inequalities of the flat history are strict, and so is its single failure (3δ_b > 2δ_b). The constraints have full rank there, so the term is positive on a relatively open set. No uniformity in s is used.

One point the note leaves implicit: the frame sum (SA 17598, item (0)) forms δ_ax and the cutoff in each frame r. P is a 4-cycle, so in every frame some edge of P is a non-tree edge, and the example works summand by summand.

The creation of Section 16 rests on the approximate test of SA 17317, χ′_k(□) = 1{|V_k(M^k U_{t,□}(V_t))^{−1} − 1| < 2δ_k}. This test compares the raw variable V_k with the block-axial average, and a gauge move at a non-top site changes V_k at no cost in action (SA 17709, item (3)). So the pure gauge of (16.1) fails it strictly while every curvature test passes. The quarantine arithmetic i − R_i < k − R_k (i < k) is right.

**(b) Final decision (raw I 51737–51753; SA 17648; SA 17838 (v)).** First-class components carry χ_k(X^{∼−6}). Islands carry χ^c_k(Y^{∼−6}) together with χ_{k,Λ}, χ and δ. SA 17838 (v) calls the failing cube test "the test χ_m of a step, and not one of the sharper tests of the stages". (The note cites SA 17831 for this sentence; it is at SA 17838.) So the decision is a product of ordinary cube tests. By CMP 119 (2.16)–(2.17), each is built from U_{s,□}(V_s) = U(B_s(□^{∼4}), M^·(Q^*_s V_s)).

Take E, a test cube containing a corner of P. If χ_s(E) = 1, the bare curvature of U_{s,E} is below ε_s η² on E^∼. That region contains P's whole averaging footprint, inside the top member of E's tower (CMP 119 (2.13): the top member contains □^{∼4} less two M_1-cubes). Then (5.3) gives |∂V_s(P) − 1| ≤ 2ε_s, which contradicts 2 sin(4ε_s) ≥ (16/π)ε_s. Hence χ_s(E) = 0, and the island factor 1 − ∏χ_s(□) equals 1.

**(c) Exact lift (CMP 119 (1.2)–(1.3), (2.13), (2.16); SA 9783 (c); SA 9646).** By (1.3), (Q^*V)(b) is 1 inside a block and V(c) on a bond from B(c_−) to B(c_+). By (2.13) on p. 256, B_j(Ω) is built on the maximal sequence Ω = Ω_0 ⊃ Ω_1 ⊃ … with dist(Ω_n, Ω_{n−1}^c) ≥ L^n ξ M_1. So the level-0 member of the tower of W = D^{∼4} is W itself, and it is eroded to Ω_1 by at least LM_1 bare spacings. The outline's two tower rules (SA 9646) erode by more than ρ bare spacings or by at least LM′_1. Either way, a bare plaquette half a spacing inside a face of W has all four bonds in the tower's Γ_0, carrying Q^*V_s.

The plaquette p of (21.1) is tangential to the face and straddles two level-s block faces. Its four bonds therefore carry the four coarse bonds of P in order, so (21.2), ∂(Q^*V_s)(p) = ∂V_s(P), is exact. This gives (21.3) with ‖·‖ = 2 sin(4ε_s).

**(d) Geometry, redone.** The face x_1 = qξ/2 of W is a level-s block face, since q and ξ are odd. The creation cell J_a gives Ω_a^c = Q′^{∼2} = J_a^{[2]} (SA 17320, with P′ = Ŷ = ∅), so the floor is J_a^{[1]}, which contains the corners of p. W spans 9qξ ≤ 9MR_s ξ/L², which is less than one cell (SA 17334: L²M_2 ≤ M, and L ≥ 5). W contains p, which lies in the core inside H_s, so D ⊂ W ⊂ H_s^{[1]} ⊂ H_s^{[4]} = X^{∼−6}. The edges of P lie within 2ξ of the core, so inside Λ^pr, which is Z″_s ⊃ core plus one layer of level-s M-cubes (SA 17598; raw I (4.15)).

## 2. Does (22.7) hold? Yes, and generically

By (21.3), h = 2 sin(4ε(T)) depends only on T. Since R_0 ≤ L(log θ_0)^r, we have R_0²ε_0 ≤ L²A_0 θ_0^{−1/2}(log θ_0)^{2r+p_0} → 0. The lower flow bound θ_0 − θ_s ≥ λ̲s − c_5 (SA 6017) sends θ_0 → ∞ at fixed θ_s = T. So for every C there is an s with h > C R_0² ε_0. **The every-joined-read envelope indexed by geometric level is refuted.**

The failure does not depend on this construction. The identity (21.2) holds at every block corner on every face of every cube tower, at every ordinary step as well as inside R. At depth ε_t/(R_0²ε_0) → ∞, so any regular datum with one face-corner coarse plaquette of a read cube above C R_0²ε_0 violates the geometric bound. Section 22's contribution is an admitted instance inside R and inside the old floor.

Row 88's target, read literally, was never satisfiable on lift bonds. The outline never asserts it:

- SA 17709 bounds the label's V_l on Γ_l, which are physical bonds.
- SA 17831 (ii) and (iv) bound the term's background and its evaluations layer by layer of the label's sequence.
- The tower clauses (SA 9654) hold only on Z less two M-cube layers.
- SA 9783 (c) uses a single radius ε_1 for the joined datum.

## 3. Route question: Theorem R with source-level indexing goes through unchanged

Two independent reasons.

**(i) The counterexample is outside Theorem R's hypothesis.** In `library/floor-screen.md`, (D-F) is a hypothesis on the datum V of a stage or prepared sequence S localized in X, at the tests T_F whose bare support meets the floor F. The read of Section 22 is a final-decision cube test, made after the main step on the new V_s. It is not a stage background, and (FS) claims nothing about it.

The stage datum's own lift bonds are the collar bonds of the X-localization: O(1) layers of μ-cubes at the part's boundary (SA 9783 (c)), where the component collar X^∼ is X plus one layer of M-cubes (SA 17356). Section 12's argument, rechecked here, places the part inside X in Ω_m:

- X = H_m^{[10]} and Ω_m^c ∩ X = H_m^{[8]} (SA 17578), so the two outer cell layers of X lie in Ω_m.
- O(1)·μξ_m + 3ξ_m is less than one cell MR_mξ_m once R_m is large.
- Ω_m ⊂ Ω_{m_b}, and F ⊂ Ω_{m_b}^c.

The part outside X misses F, because F ⊂ X. So T_F contains only physical label tests (V_l on Γ_l, SA 17709), and for those the source level is the geometric level. This also supplies the inside half of the collar clause of (S1b), which `gates/floor-screen-gate.md` Section 4 left open, given that the O(1) and μ of SA 9783 (c) are fixed numbers.

**(ii) If lifted tests did meet F, source-level indexing would cost nothing.** Theorem R reads (D-F) in two places only: through max_{τ∈T_F}|∂V(τ) − 1| ≤ A_F = 4L²C_F R_m²ε_m (Steps 1 and 3), and through actual supports in the repaired Lemma G. Under (6.1), |∂V(τ) − 1| ≤ C_*R_{b(τ)}²ε_{b(τ)} with b(τ) ≤ m. Lemma T bounds this by 4L²C_*R_m²ε_m for every b ≤ m, which is the same A_F. (Lemma T was gated CORRECT-NO-ADVANCE, and (6.2) is the same statement.) A lifted test in T_far inherits the level-free bound ς of (D-far) from its source plaquette by (21.2).

Theorem R's open inputs are therefore unchanged:

- (D-F) on the physical label datum of the old core. The note's Section 15 argues the initial strip and the ordinary seams under the CMP 119 rule, but that section is not gated here. Still open: draws of older R operations (they read Proposition 2.4's uniform C(M)ε_k, not rebuilt), inherited cells (raw I, Remark 4.21), and drop-out bare integrals.
- (D-far), through (EA).
- (A1-S).
- (A3-P), or the repaired (OS-loc).
- The rest of (S1).

## 4. Reversal test 4.3: not fired

The test asks for a history whose energy outside the old floor is below c l_m^{2p_1−8r} but whose localized background fails a test outside the floor; the stated example is a heavy wall in the floor that is screened by less than R_m²ε_m e^{−δ_0MR_m}. Section 22 is not such a history:

- **(a)** Its read is not a stage background. At the stages the example is exactly flat, so every stage background is flat and no stage test fails.
- **(b)** The floor datum is a lift of size 2 sin(4ε_m) ≤ 8ε_m ≤ A_F, at source level m. It is not a heavy wall.
- **(c)** The only failed test, χ_m(E), is a final-decision test. The drawn level-m datum fails it by itself (|∂V_m(P) − 1| > 2ε_m); no screening of floor data is involved. Islands are paid by the Wilson gain of that failed test (SA 17838 (v)).

Package C rank 1 keeps its reversal test, untested in its stated form.

## 5. Defects, ranked by what they break

**D1 (breaks the second repair of Section 23).** With ℓ(τ) the geometric level, (23.1) is a valid Borel identity. By (21.2), however, its rejection branch I_join = 0 contains every datum with a face-corner coarse plaquette P of a read cube satisfying |∂V_s(P) − 1| > C R_0²ε_0.

An explicit case is (20.1) with any t in ((π/2)C R_0²ε_0, g_s). This interval is non-empty at depth, because g_s = T^{−1/2} is fixed while R_0²ε_0 → 0. The cutoff admits these draws. Their only non-flat datum is one coarse plaquette smaller than g_s, which is below every threshold of level s (ε_s, δ_s and δ′_s all carry log factors above g_s). The old core is a pure gauge.

The outline pays each failure outcome through the dichotomy "failure ⇒ a field above a threshold ⇒ small factor" (Lemma 2.5, SA 17709; SA 17838 (v)). This branch has no such field, so it has no payer. Inside R it rejects these draws whatever the other tests give. Applied to all background reads, it would gate ordinary steps too, since (21.2) holds there as well. The note leaves this cost unproved; the example shows that the cost is not a question of smallness. So (23.1) is not a repair. With ℓ(τ) the source level, (23.1) reduces to (6.1) and is unnecessary.

**D2 (scope, for the lead; not a defect of the note).** Row 88's target, every actual joined datum regular at C R_l²ε_l, should be replaced by the outline's own sentence (SA 17709: the label datum V_l on Γ_l in the old core), with any lifted read bounded at its source level. The refutation then removes nothing the route uses.

**D3 (non-breaking).** A frame must satisfy λ̲(j−i) − c_5 ≤ θ_i − θ_j ≤ B̄(j−i), and it must stay within the tube (R20) around the actual x_j = x_{j−1} − b_j (SA 6017). So the slope in (22.2) must lie in [λ̲, B̄] and match the b_j up to the tube. The argument uses only θ_0 − θ_s → ∞ and the top plateau R(θ_i) = R for i ∈ [s−R−1, s]. Both hold for any legal frame with θ_s = T inside a plateau of length at least B̄(R+1); choose the bare coupling so that θ_s = T.

**D4 (non-breaking).** In the island record the value of χ_s(D) is inert, because E alone fixes the factor. D's joined datum is still formed: the factor is a function of V_s built from U_{s,D}. So row 88's literal quantifier is met, though no consumer reads the value here. The generic form in Section 2 does not depend on this point.

## 6. What stays open and what changes

- **Unchanged:** Package C rank 1 remains conditional floor screening (Theorem R, as repaired), and the reversal test of 4.3 stands.
- **Change, for the lead:** restate row 88's target as in D2, and do not adopt (23.1).
- **Next decisive item** for (D-F) on the physical label datum: gate the note's Section 15 (initial strip and ordinary seams under CMP 119 (3.1)–(3.5)). Then take the older-R-draw case, which reads Proposition 2.4's uniform C(M)ε_k (CMP 122, Proposition 1, not rebuilt here).
- **Method:** no numeric or computer-assisted step entered. One reader, Claude, read every section, as a cross-provider read of a Codex note.

RESULT: The history of Section 22 is admitted under the outline's rules (SA 17604 cutoff with M_0 > 8; the final decision of raw I 51737-51753 and SA 17838 (v) uses ordinary cube tests; CMP 119 (1.3), (2.13), (2.16) give exact lifts on a level-0 strip at least LM_1 wide). (22.7) holds, and the geometric-level every-joined-read envelope fails generically on lift bonds. Theorem R goes through unchanged: it reads only physical label tests in the floor, and in any case Lemma T bounds source-level amplitudes by A_F. The reversal test of 4.3 has not fired. (23.1) is WRONG as a repair. Open: (D-F) on the physical label datum (gate Section 15; older-R draws need Proposition 2.4), plus (D-far)/(EA), (A1-S), (A3-P) and (S1).
