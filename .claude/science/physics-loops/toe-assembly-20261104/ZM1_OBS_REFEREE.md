lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# ZM1-OBS referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as the pass-3 referee under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. The lane ran under the pass-1 lane rules. This session wrote neither pass 1 (`ZM1_OBS_DRAFT.md`) nor pass 2 (`ZM1_OBS.md`). This is one check: one line-by-line read of the whole part. It reviews no other review.

**What this file is.** A referee report. It grants no status. It adopts no law, reading, class or ranking, and it changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Referee closure" marks a complete argument written here for a missing step or a correction; such closures are themselves unrefereed. Proposed repairs of class specifications are four-tested in §4 and left to the owner. No `[check]` was run: every argument below is by hand, and every one is short enough to formalize.

**Sources read, with commits.** Checkout `/Users/jonBridger/toe-worker/repo`, branch `claude/toe-assembly`. HEAD was `cf42edcedb66a365b18d7fef1b8cd7ae4d45ea26` when the lane began and `f96fccb42` when this file was finished. The three commits in between record owner decision GA1-P-NN = NN-a (`TOE_ASSEMBLY.md` §3.7, `GA1_5.md` Amendment 1), add `RCS1.md` Amendment 1 (prior work), and add prior-work digests for nine other parts. They do not touch `ZM1_OBS.md`, its draft, its digest, `ZM1.md`, `GA2_Y2.md`, `LZ1.md` or `VC1_5.md`. This report uses the new texts; §2 (G1) and §3.7 use the NN-a decision. Folder `.claude/science/physics-loops/toe-assembly-20261104/`. Line numbers below refer to `ZM1_OBS.md` unless a file is named, and to the files at `f96fccb42`.

| File | Last commit touching it | SHA-256 (prefix) | Lines read |
|---|---|---|---|
| `ZM1_OBS.md` (refereed text) | `cf42edced` | `2da8a7fdec2a9c59675708a2106c3261a96d2bf96802071c132d06e0e95ae11c` (full) | 1-190, all |
| `ZM1_OBS_DRAFT.md` (pass 1) | `8d0d4b4db` | `fcf9b7f24eebfa20` (equals the hash `ZM1_OBS.md` line 13 records) | 1-460, all |
| `prior/ZM1_OBS.md` (digest) | `4844be653` | `ae1e64b52512b03d` | 1-95, all |
| `ZM1.md` (frozen, Amendment 1) | `068681e30` | `61b6ac086000ab6c` (the draft read `123684581f2023f4`, before Amendment 1) | 1-30, 40-80, 225-300, 340-396 |
| `RCS1.md` (frozen, Amendment 1) | `8ca361b0c` | `0b2addf9efb30ce3` (read in full at `f9694bb35`, `defe632b1eb5136e`, which equals the draft's; Amendment 1 adds lines 7-10 and shifts later lines by 5) | 1-224 at `f9694bb35`; 7-10 and grep hits at `8ca361b0c` |
| `GA2_Y2.md` (frozen) | `bf403a16a` | `25db8a18aff1d30f` (equals the draft's) | 1-169, all |
| `LZ1.md` (frozen, Amendments 1-2) | `cf42edced` | `e5e18302fd535f6d` (the draft read `f6171c950bc65c7c`, before Amendment 2) | 1-60 |
| `VC1_5.md` (frozen, Amendment 1) | `eb667e2ff` | `d353e995e8c20396` (the draft read `7461113c411eeda4`, before Amendment 1) | 1-70; grep hits 117, 181 |
| `GA1_5.md` (frozen, Amendment 1) | `2d48e6bdc` | `c53418ca516e84a2` | 7 (Amendment 1); grep hits 5, 11, 13, 50, 262, 321 |
| `TOE_ASSEMBLY.md` | `2d48e6bdc` | `1f4866e908262ee2` (read first at `8e442c884`, `a69284d6505b837b`; the new §3.7 adds lines 231-238 and shifts later lines by 8) | 220-232, 270-290, 393-400, 546-563 at `8e442c884`; 225-238, 281, 405 at `2d48e6bdc` |
| `LW1.md`, `FL1.md` | `4b65c608f`, `c98189c13` | `78280bd620800eac`, `6cc65f50cc52ed77` | grep hits only (GA1-P; a search of the folder for prior treatment of the twist) |
| `LW1_REFEREE.md`, `GA1_5_REFEREE.md`, `Y2W_DRAFT.md` | | | 1-80 and headings; 1-50, 105-125, 297-400; 1-30 (format only) |

Also read: `AGENTS.md`, `CLAUDE.md`, `docs/ai_methodology/SCIENCE_WORKFLOW.md`. Branch `origin/main` at `f5af11cd0` (after `git fetch -q origin main`; read with `git show` only): the five notes `ZM1_OBS.md` cites, at the quoted lines (`MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 230-240; `FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 1-6 and 542-551; `CONFINEMENT_STRING_TENSION_NOTE.md` lines 4-8 and 139-143; grep hits in `GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md` and `GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md`). Branch `origin/claude/ym4d-hard-route` at `83eccbb94` (after `git fetch -q`; `git show` only): `.claude/science/physics-loops/ym4d-hard-route-20261030/library/port/p8b-limits.md` (last changed `8c60cc97b`), lines 55-58. Nothing was checked out.

**Working-set entries used, by name.** PS-5 (five modes per site) and PS-6r (finite link registers), through the two live laws `L5-U[m]` and `L5-O[S_+]` as the sources state them. PS-7r only through ZM1-I1's phrase "a vacuum that VC1 supplies" (`ZM1.md` line 361). Owner decisions of `TOE_ASSEMBLY.md` §§3.6-3.7, as recorded: the ZM1-I1 instruction (line 227), R-CS^str as a named working candidate (line 225), LZ1-SC (line 229, used once in §3.7), and GA1-P-NN = NN-a (line 235, used in G1 and §3.7). Not used: PS-1c beyond what the cited theorems already use, PS-2, PS-3, PS-4, PS-11c, PS-Ar.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws, PS-6r and the VC1 conditions are read plainly. Where a class specification leaves a choice that decides a verdict, this report states the repair, four-tests it, and leaves the choice to the owner.

**Method.** Every proof in `ZM1_OBS.md` was re-derived by hand and checked against the draft where the distillation shortens it. Every citation of another file was checked against that file's text. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step, closed here where possible). §2 judges the six GAPs the distiller marked. §3 holds the referee closures. §4 checks every four-test verdict and the ranking.

**Counts.** 67 items: 54 CORRECT, 5 ERROR, 8 INCOMPLETE. No ERROR changes the content of a numbered theorem. One ERROR (row 52) and five INCOMPLETE items (rows 49, 53, 57, 60, 64) change a class specification, a four-test verdict or the ranking text, and so bear on the owner's choice. Six distiller GAPs: five are real; GAP S′ is real only in its `p>0` clause. GAP b-zero is repaired. GAPs C-law, d-domain and c′ are partly repaired. GAP e-dynamics stays open.

---

## 0. Outcome

**The theorems hold.** Theorems 1-12 and the compactness proof are correct under their stated hypotheses. Three statements lost a hypothesis or a convention in distillation: the Fourier convention of §3, and the summability hypothesis of Theorems 8 and 9 (draft Lemmas S and S′, lines 231 and 239). With summability restored, Theorem 9's added bound `S` is automatic (Lemma S0). So most of GAP S′ is not a gap.

**Two extensions bear on what class (c) supplies.** Theorem 8 does not need `w₁(0)>0`: positive weights off `θ=0` suffice (Theorem 8′). Under the relative budget, Theorem 9 holds for weights comparable to one positive function (Theorem 9′). So speed transfer covers composites whose weight vanishes at zero momentum, such as conserved densities.

**Class (a) forces exact tail matching.** Its envelope bound makes the two sides' tail envelopes agree to relative order `r^{-p}` at every tick (Lemma ER). In a gapped vacuum this is exact equality of every invariant channel's correlation length and tail amplitude, in coarse units. That is long-distance content, so (a)'s four tests stay P P P P.

**Class (d)'s string data do not carry three-dimensional speeds through Theorems 8-9.** A limit of the normalized same-far-end amplitudes, if it exists, is a positive-definite function with a covariant cyclic representation (Lemma DL). But when the charge propagates in three dimensions, the on-axis amplitude is a transverse average. In the free massless walk it has, for some residue, no finite branch decomposition at any small axial momentum (Lemma AX). So (d)'s claimed supply to LZ1-i fails in the basic propagating case.

**The twist.** GAP C-law is real as a scope gap. Under the owner's decision NN-a the twisted update is a PS-1 update with the same invariant data and the same VC1 vacua as the untwisted one, but it is not of the `L5-U` form that ZM1-I1 states (Proposition T). Whether the law should contain it is a law-specification choice.

**Four tests.** (a) P P P P, (c) P C P C, (d) P C C C and (e) C P P P are confirmed. Class (b) has an ERROR: its area form (b-A) gets C on test 3 and its Creutz form (b-Cr) gets P, but both compare only `σ` (Theorem 11), so the two verdicts must agree. The area form is blind to perimeter coefficients only at `p=1`. Every budget weakens as `p` decreases, so each existential ZM1-I1[O] is its `p=1` case (Lemma P1). Rule R-b repairs (b)'s zero rule and Creutz domain; with it, (b)'s test 2 passes. Class (c)'s summability domain and class (d)'s positivity domain depend on the candidate; repairs R-c and R-d remove that.

**Ranking.** The stated criteria do not determine pass 1's order (a), (c), (e), (d), (b). Under a stated weighting (prefer the least demanding class whose added data a named consumer uses), the corrected verdicts give (a), (c), (e), (b), (d). Only the last two places change.

**Recommendation.** Freeze `ZM1_OBS.md` after the required edits R1-R21 of §5. Put the class choice to the owner with §4's table, routed first through the check that `TOE_ASSEMBLY.md` line 229 records.

---

## 1. Verdict table

Each row is one statement or proof step of `ZM1_OBS.md`, with its line numbers. The six GAPs are judged separately in §2. "R*n*" points to a required edit in §5.

| # | Item (`ZM1_OBS.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status and scope (5) | CORRECT | |
| 2 | §0 "Proved" list (7) | CORRECT | Each listed item is proved below. R21 adds the referee closures. |
| 3 | §0 GAP list (9) | ERROR | Item 2 says the several-branch proof "needs uniform weight bounds, circular phase separation and `p>0`". With the draft's summability hypothesis the upper weight bound is automatic (Lemma S0), and near `θ=0` plain and circular distances agree. Only `p>0` is a real condition. Item 1 overstates the draft: it never called the twist a base law; its Theorem C(4) treats `K_φU₀` as an admissible ZM1-I1 fine update. R4, R8. |
| 4 | §0 open list (11) | CORRECT | Matches `ZM1.md` line 16 and `RCS1.md` line 18. |
| 5 | §0 provenance (13) | CORRECT | The draft's SHA-256 was recomputed and matches. |
| 6 | §1 conventions and block maps (17) | CORRECT | |
| 7 | §1 data, values, linear extension, truncation (19-25) | CORRECT | |
| 8 | §1 ZM1-I1[O] and the original ZM1-I1 (25) | CORRECT | Every budget weakens as `p` decreases, so "there exist ... `p≥1`" is the `p=1` case (Lemma P1, §3.3). R19. |
| 9 | §1 "determine", "cannot detect", four-test legend (27) | CORRECT | The correction of the draft's "carries them approximately" is right. |
| 10 | Theorem 1 (31) | CORRECT | |
| 11 | Theorem 1 proof (33) | CORRECT | |
| 12 | Theorem 2 (35) | CORRECT | |
| 13 | Theorem 2 proof (37) | CORRECT | Connectedness of `U(5)` and `Spin(10)` gives products of exponentials. (G2) and singletons are not used. |
| 14 | Remark on one charged entry (39) | CORRECT | "Charged at X" must mean that the entry's span carries a representation of the local group at X with no invariant vector, all other entries being invariant there. R20. |
| 15 | Theorem 3 (41) | CORRECT | |
| 16 | Theorem 3 proof (43) | CORRECT | Singletons are needed for the image claim: for a site of a larger `S_X` the single-site gauge action is not an image under `Φ`. |
| 17 | Theorem 4 (45) | CORRECT | |
| 18 | Theorem 4 proof (47) | CORRECT | |
| 19 | Remark after Theorem 4 (49) | CORRECT | Any `β` of sup-norm 1 already works, with radius `R₀+1`; "sufficiently large" is not needed. |
| 20 | Theorem 5 (51) | CORRECT | Signs checked: `γ_φ(c)=K_φ*cK_φ=e^{iφ}c`, so `α_φ=α∘γ_φ`, and a node appears at `K₀` exactly when `e^{iqφ}=λ`. |
| 21 | Theorem 5 proof (53) | CORRECT | |
| 22 | GAP C-law (55) | CORRECT | Real, as a scope gap; G1 and §3.7. R8. |
| 23 | Theorem 6 (59) | CORRECT | The hypothesis on the coarse value must hold for every candidate, as the draft's Lemma V says. R6. |
| 24 | Theorem 6 proof (61) | CORRECT | |
| 25 | Remark after Theorem 6 (63) | CORRECT | |
| 26 | Setting of Theorems 7-9 (65) | INCOMPLETE | The Fourier convention `f̂(θ)=Σ_βf(β)e^{iθ·β}` (draft line 211) is missing, and `c_i` lacks "when the sum converges absolutely". The formula of Theorem 7 depends on both. R1. |
| 27 | Theorem 7 (67-71) | CORRECT | |
| 28 | Theorem 7 proof (73) | CORRECT | Moment step checked: a polynomial of degree at most `n` that is `o(s^n)` vanishes. |
| 29 | Charged fields and composites (75) | CORRECT | The main-branch quote ("not absolutely summable", MASSIVE_WILSON note line 238) checked. |
| 30 | Theorem 8 (77) | INCOMPLETE | Summability `Σ_β‖C_i(β,0)‖<∞` (draft line 231) was dropped; it is needed to define `ξ_i` on band-limited profiles. `w₁(0)>0` is not needed (Theorem 8′). R2, R5. |
| 31 | Theorem 8 proof (79) | CORRECT | The draft's constant `C₁=12C` can be `4C`. |
| 32 | Theorem 9 hypotheses (81-85) | INCOMPLETE | Summability (draft line 239) was dropped; with it the bound `S` is automatic (Lemma S0). R2. |
| 33 | Theorem 9, last sentence (85) | ERROR | "A cone `±v\|θ\|`, `v>0`, satisfies the gap condition, but only if the observables have the stipulated nonvanishing branch weights." The gap condition holds with `g=2v` whatever the weights; the weights are a separate hypothesis. R3. |
| 34 | Theorem 9 proof (87) | CORRECT | The leakage term `πSs^p/(ηg)` is where `p>0` is used. |
| 35 | GAP S′ (89) | ERROR | "Continuity on the punctured ball plus a lower bound on `‖W‖` does not supply its proof's finite `sup Σ‖W‖`." The draft's hypotheses also include summability and `W≥0`, and these supply it (Lemma S0). The `p>0` and common-speed sentences are right. G2, R4. |
| 36 | Theorem 10 (93) | CORRECT | The hypothesis forces `n` to be an eigenvalue. |
| 37 | Theorem 10 proof (95) | CORRECT | |
| 38 | Loop application (97) | CORRECT | The witnesses have sharp end numbers: `VC1_5.md` line 117, `RCS1.md` lines 97 and 101. The traversal correction of the draft is right. |
| 39 | Theorem 11 (99) | CORRECT | |
| 40 | Theorem 11 proof (101) | CORRECT | |
| 41 | Theorem N paragraph (103) | ERROR | "an invertible covariant operator link with nontrivial continuous representation is impossible on a finite register" is false for a representation with finite image: `GA2_Y2.md` Theorem 2.3 (line 40) builds such a link on `L²(K)`. Corollary 2.2 (line 34) needs infinite image, which every nontrivial continuous representation of the connected groups `U(5)` and `Spin(10)` has. The conclusions drawn for the two laws stand. R7. |
| 42 | Theorem 12 (105) | CORRECT | It also holds on the fine side for block images, by Theorem 2 at the far coarse site. |
| 43 | Theorem 12 proof (107) | CORRECT | Checked on both laws: fundamental rishon creator at the far end on U; vector Majorana `η^y_b` on O, with a one-dimensional invariant space in `V⊗V`. |
| 44 | Remark after Theorem 12 (109) | CORRECT | |
| 45 | §5 preamble (113) | CORRECT | |
| 46 | (a) definition and ZM1-I1[a] (117-122) | CORRECT | |
| 47 | (a) commentary (124) | CORRECT | The correction of the draft's "the two comparisons compose" is right. |
| 48 | (a) four tests (126) | CORRECT | P P P P agreed. Lemma ER (§3.2) states what the envelope forces. At fixed `r` the budget is vacuous once `C_{R₀}(r^{-p}+tr^{-p-1})≥2`, as is every budget with a `t`-linear term. R18. |
| 49 | (b) definition and zero rule (130-136) | INCOMPLETE | The zero rule does not define `χ` when one of its four values vanishes, does not cover `R=1` or `T=1` for `χ`, and gives no budget for `W_C*W_C`. Rule R-b (§3.3). R9. |
| 50 | GAP b-zero (138) | CORRECT | Real; G3. |
| 51 | (b) commentary (140) | CORRECT | Main-branch quotes (finite-clock note lines 542-551; confinement note lines 141-142) checked. |
| 52 | (b) four tests (142) | ERROR | "(b-A) P C C P; (b-Cr) P C P P", with the reason "The area form can discard perimeter distinctions". By Theorem 11 the Creutz form also cancels every `f(R)+g(T)`, so it discards them too. Both forms compare only `σ`; the test-3 verdicts must agree. The area form discards perimeter coefficients only at `p=1` (§3.3). §4, R10. |
| 53 | (c) definition and ZM1-I1[c] (146-151) | INCOMPLETE | The summability domain is stated for the states, and the coarse state and `Φ` belong to the candidate. The translation unitaries `T^{(1)}` also need a coarse state invariant under coarse cell translations, which ZM1-I1[O] does not require. Repair R-c (§3.4). R11. |
| 54 | (c) commentary (153) | CORRECT | Theorems 8′ and 9′ widen the species covered. R5. |
| 55 | (c′) and GAP c′ (155) | CORRECT | Real; the free part is closed in trace norm (Lemma C′-free, §3.5). G5, R14. |
| 56 | (c) four tests (157) | CORRECT | P C P C agreed, as written. |
| 57 | (d) definition (161-166) | INCOMPLETE | The positivity domain depends on the candidate; coarse translation invariance is missing; the letter `r` means separation in (a) and string length in (d). Repair R-d (§3.6). R12. |
| 58 | GAP d-domain and speed (168) | CORRECT | Real. Lemma DL supplies the limit structure from pointwise convergence; Lemma AX shows the remaining hypotheses fail for three-dimensional propagation. G4, R13. |
| 59 | (d) four tests (170) | CORRECT | P C C C agreed. |
| 60 | (e) definition (174) | INCOMPLETE | The one-step maps' properties are omitted. The draft (line 398) has "a tower of block maps `Φ_k : 𝔄_k → 𝔄` of factor `2^k`". R15. |
| 61 | (e) compactness proof (176) | CORRECT | |
| 62 | GAP e-dynamics (178) | CORRECT | Real; G6. The H-BLOCK quote (YM branch, `p8b-limits.md` line 57) checked. |
| 63 | (e) four tests (180) | CORRECT | C P P P agreed. |
| 64 | §6 ranking (184) | INCOMPLETE | The stated criteria do not determine the order. Two of pass 1's reasons for placing (b) last fail, and Lemma AX removes (d)'s distinctive supply. §4, R17. |
| 65 | §6 four-test retention (186) | CORRECT | Its caveat on (e) is broader than needed: ZM1-I1[e] quantifies the tower existentially, and the common algebra enters only the optional limit-point clause. R16. |
| 66 | §6 prior-work paragraph (188) | CORRECT | |
| 67 | §6 toy-check paragraph (190) | CORRECT | Matches draft line 433. |

---

## 2. The distiller's GAPs

**G1 = GAP C-law (line 55; §0 item 1). Real, as a scope gap; partly repaired.** The draft's Theorem C(4) (draft line 191) says: "For every class whose entries lie in `𝔄_1^G`, ZM1-I1[O] for the fine update `U_0` and for `K_φU_0` (or `∏P_x U_0`) is the same statement, with the same `ω_0`." Two of its three ingredients hold. The invariant data agree (Theorem 5). The vacuum reading is closed under the twist: the draft's proof is right, because `VC1_5.md` line 29 defines E as "extremality among states satisfying (i)–(iii)" and P as "purity of the restriction to `A^{gauge}`", and for a locally gauge-invariant state stationarity under `α` and under `α_φ` coincide. The third ingredient fails as stated. ZM1-I1 admits the fine update "base tick, or with a plaquette class that GA1-P-5 supplies" (`ZM1.md` line 361). GA1-P-5's gates are link-only: "each `g_X` is a link-only gauge-invariant unitary" (`GA1_5.md` line 50). `K_φ` acts on matter, since `γ_φ(c)=e^{iφ}c`. So `K_φU₀` is in LZ1's class (`LZ1.md` line 28) but is not one of ZM1-I1's stated fine updates. Under the owner's decision NN-a (`TOE_ASSEMBLY.md` line 235), `K_φU` is a PS-1 update whenever `U` is, because `K_φ` acts as one layer of even nearest-neighbour gates (Proposition T(5)). So the twist relates two PS-1 updates with the same invariant data and the same VC1 vacua, and only one of them has the `L5-U` form that ZM1-I1 states. The repaired statement is Proposition T (§3.7). Whether the five-mode law's update class should contain the matter-phase layer is a law-specification choice for the owner; it is not decided here. The distiller's "conditional on a charged band" is also right: the draft's FINISH counterexample assumes a charge-`q` band with scalar `V(K₀)` and exhibits none.

**G2 = GAP S′ (line 89; §0 item 2). Real only in its `p>0` clause.** (i) The finite bound `S` is supplied. The draft's Lemma S′ assumes `Σ_β‖C_i(β,0)‖<∞` and `W_{i,k}≥0` (draft line 239). Lemma S0 (§3.1) then gives `‖W_{i,k}(θ)‖≤Σ_β‖C_i(β,0)‖`. The distilled Theorem 9 dropped summability and so had to add `S`. Restoring summability removes the added hypothesis. (ii) Circular distance needs no change of proof. All phases tend to `0` with `θ`, so for small `|θ|` every phase difference lies in `(−π,π)`, where plain and circular distances agree. (iii) `p>0` is used in the leakage term `πSs^p/(ηg)`. The draft did not state it. Every class has `p≥1`, so the condition is met. Repaired statement: Theorem 9 with summability and without `S` (R2).

**G3 = GAP b-zero (line 138). Real; repaired.** The draft's rule ("A loop with `F_0 = F_1 = 0` passes; one with exactly one zero fails", draft line 315) concerns single loops. `χ(R,T)` needs four nonzero values and four nondegenerate rectangles, so `R,T≥2`. The rule also gives no budget for `W_C*W_C`. Rule R-b (§3.3) assigns every case. Four tests P P P P (§4).

**G4 = GAP d-domain and speed (line 168). Real; partly repaired, and the corrected claim is shown to fail in the basic propagating case.** At finite string length the vectors `π(B_{n−k}(X+2ke))Ω` are not translates of one vector, so the amplitudes are not of Setting F's form. Lemma DL (§3.6) supplies the missing construction from one hypothesis: if the normalized amplitudes converge as the string length grows, for every axial displacement and tick, the limits form a positive-definite function on `Z²` with a covariant cyclic representation. Theorems 8-9 then apply to the fine and coarse limits under their remaining hypotheses. Lemma AX (§3.6) shows those hypotheses fail when the charge propagates in three dimensions: in the free massless walk the on-axis amplitude has, for some residue and at every small axial momentum, a nonzero phase spectrum with no atoms. So the distiller's corrected claim ("axial speed transfer *if* a specified limiting translation-covariant kernel satisfies all hypotheses of either theorem") is right, and its hypothesis is false in that case.

**G5 = GAP c′ (line 155). Real; free part closed.** The draft asserts that with c-number links the bilocals "become bilinears of band-limited fields, and `ZM1.md` line 272 (normally ordered `2n`-point functions) proves the comparison with `p = 2`" (draft line 347). Lemma C′-free (§3.5) proves this for trace-class kernels whose Fourier support lies in `|θ|≤κ` in both variables, with an absolute error `8β(t)‖K‖₁‖K′‖₁`. The relative form `C(κ^p+tκ^{p+1})N(f)N(g)` is not proved for bilocals. The quantum-link form needs the c-number reduction that `ZM1.md` Attack 2 (line 382) does not supply.

**G6 = GAP e-dynamics (line 178). Real; open.** Nothing in the draft constructs a tower, convergence of updates, a unique limit, or a charged sector. The compactness proof is right and gives only subsequential limit points of states. This is the content of ZM1-i. No repair is attempted here.

---

## 3. Referee closures

All closures below are unrefereed. Notation is that of `ZM1_OBS.md` §3: `C_i(β,t)_{ab}=⟨v_{i,a},U_i^tT^{(i)}_βv_{i,b}⟩`, `f̂(θ)=Σ_βf(β)e^{iθ·β}`, `‖f‖²=(2π)^{-3}∫|f̂|²`, `N(f)=max_i‖ξ_i(f)‖`, `s=|θ₀|`.

### 3.1 Theorems 8 and 9: summability and vanishing weights

**Lemma S0 (the bound `S` is automatic).** Assume the hypotheses of Theorem 9 together with `Σ_β‖C_i(β,0)‖<∞`, as the draft's Lemma S′ does (draft line 239). Then for `0<|θ|<κ₀`,
\[
 \|W_{i,k}(\theta)\|\le\|c_i(\theta,0)\|\le\textstyle\sum_\beta\|C_i(\beta,0)\| ,
\]
so `S:=max_i sup_θΣ_k‖W_{i,k}(θ)‖≤max_i n_iΣ_β‖C_i(β,0)‖<∞`.

*Proof.* At `t=0` the branch form gives `c_i(θ,0)=Σ_kW_{i,k}(θ)`. If the hypothesis is stated as a form identity for profiles with Fourier support in `B_{κ₀}` (the draft's wording), the same pointwise identity follows from Theorem 7's proof: normalized profiles concentrated at `θ` and continuity of both densities at `θ≠0`. Each `W_{i,k}(θ)` is positive semidefinite, so `0≤W_{i,k}(θ)≤c_i(θ,0)`, and the operator norm is monotone on positive semidefinite matrices. The last inequality bounds an absolutely convergent Fourier series. □

**Theorem 8′ (positive weights off zero suffice).** In Theorem 8, replace "`w₁(0)>0`" by "`w₁(θ)>0` for `0<|θ|<κ₀`". Then there is `s_*>0`, depending on `C`, `p`, `κ₀` and the continuity of `λ₀−λ₁` at `0`, with
\[
 |\lambda_0(\theta)-\lambda_1(\theta)|\le 8\pi C\,|\theta|^{p+1}\qquad(0<|\theta|\le s_*).
\]

*Proof.* Fix `θ₀`. As in Theorem 8's proof (relative budget, normalized profiles concentrated at `θ₀`, then `κ↓s`), for every `t∈N₀`
\[
 |w_0e^{-it\lambda_0}-w_1e^{-it\lambda_1}|\le C(s^p+ts^{p+1})\max_iw_i\qquad\text{at }\theta_0 .
\]
At `t=0` this gives `|w₀−w₁|≤Cs^p max_iw_i`. If `Cs^p≤1/2`, then `max_iw_i≤2w₁(θ₀)`. Write `δλ=λ₀(θ₀)−λ₁(θ₀)`. Since `w₁e^{−itλ₀}−w₁e^{−itλ₁}=(w₁−w₀)e^{−itλ₀}+(w₀e^{−itλ₀}−w₁e^{−itλ₁})`,
\[
 w_1|e^{-it\delta\lambda}-1|\le 2Cs^p\,w_1+2C(s^p+ts^{p+1})\,w_1\le 4C(s^p+ts^{p+1})\,w_1 .
\]
Divide by `w₁(θ₀)>0`: `|e^{−itδλ}−1|≤C₁(s^p+ts^{p+1})` with `C₁=4C`. Choose `s₁` so that `|δλ|≤π/2` for `|θ₀|≤s₁`. The draft's step (draft line 237: `t_*=⌈π/(2|δλ|)⌉`, `|e^{−iδλt_*}−1|≥√2`) gives `|δλ|≤2πC₁s^{p+1}=8πCs^{p+1}` once `C₁s^p≤1/2` and `s^{p+1}≤1/(4C₁)`. The value `w₁(0)` is never used. □

So Theorem 8 applies to composites whose weight vanishes at `θ=0`, such as a conserved density (draft line 353: "a conserved density has `c(0) = 0` and signal `O(κ^2)`").

**Theorem 9′ (relative budget, comparable weights).** In Theorem 9, replace the absolute error by the relative error `C(κ^p+tκ^{p+1})N(f)N(g)`, and the weight bounds by
\[
 w\,\rho(\theta)\le\|W_{i,k}(\theta)\|,\qquad \textstyle\sum_k\|W_{i,k}(\theta)\|\le S\rho(\theta)\qquad(0<|\theta|<\kappa_0)
\]
for one function `ρ>0`. Keep `p>0`, summability and the gap condition. Then the conclusions of Theorem 9 hold, with a matching distance at most `(8πCS²/w²)|θ|^{p+1}` for small `|θ|`.

*Proof.* Use normalized profiles concentrated at `θ₀` with unit vectors `u,u′`. The relative budget gives, after `κ↓s`, `|⟨u,(c₀−c₁)(θ₀,t)u′⟩|≤C(s^p+ts^{p+1})max_i‖c_i(θ₀,0)‖`. Since `c_i(θ₀,0)=Σ_kW_{i,k}(θ₀)`, the right side is at most `CSρ(θ₀)(s^p+ts^{p+1})`. Divide every symbol and weight at `θ₀` by `ρ(θ₀)`. The rescaled data obey Theorem 9's pointwise bound with constant `CS`, and its weight bounds `w` and `S`. Theorem 9's proof works at one `θ₀` at a time (the average is over `t`), so it gives `δ≤2πS/(Tw)` with `T=⌈ηs^{−p−1}⌉`, `η=w/(4CS)`, that is `δ≤(8πCS²/w²)s^{p+1}`, with constants independent of `θ₀`. The matching along rays is unchanged. □

With `ρ≡1` the relative budget implies the absolute one used in Theorem 9, so Theorem 9′ contains it.

### 3.2 Lemma ER: class (a) forces exact tail matching

**Lemma ER.** Fix `A,B∈𝔄₁^G(R₀)` and `t∈N`. Put `m_i(r)=sup_{|β|_∞≥r}|F_i^T(A^*,τ_βB;t)|`, so that `M(r,t)=max_im_i(r)`, and `ε(r)=C_{R₀}(r^{-p}+tr^{-p-1})`. If (a)'s bound (line 120) holds, then for every `r≥1`
\[
 |m_0(r)-m_1(r)|\le\varepsilon(r)\,M(r,t).
\]
So if `ε(r)<1` and `M(r,t)>0`, both `m_i(r)>0` and `m_0(r)/m_1(r)∈[1−ε(r),(1−ε(r))^{-1}]`.

*Proof.* Let `|β|_∞=r′≥r`. Then `r′^{-p}+tr′^{-p-1}≤r^{-p}+tr^{-p-1}` and `M(r′,t)≤M(r,t)`, so the bound at `β` gives `|F_0^T(β)|≤|F_1^T(β)|+ε(r)M(r,t)≤m_1(r)+ε(r)M(r,t)`. Take the supremum over `β`, then exchange the sides. The ratio bounds follow from the two one-sided inequalities. □

*Consequence.* At every fixed tick the tail envelopes of the two sides agree to relative order `r^{-p}`. If `m_i(r)=a_ie^{−r/ξ_i}(1+o(1))` with `a_i>0`, then `ξ₀=ξ₁` and `a₀=a₁`. If `m_i(r)=a_ir^{−η_i}(1+o(1))`, then `η₀=η₁` and `a₀=a₁`. Definition Z compares `Φ(A)` with `A` directly (`ZM1.md` line 56, "the **correlation error**"), so no renormalization factor can absorb a difference of amplitudes. So ZM1-I1[a] asks a coarse law of the `L5-U` form to reproduce, in coarse units, every invariant channel's correlation length and tail amplitude exactly. This is long-distance content, and it is what the vanishing rate of `ZM1(a)1` asks; it does not change (a)'s test 4. It is a strong demand on a law with finitely many constants. The (c) budget, through Theorem 7, and the (b-Cr) budget, through Theorem 11, force exact equalities of the same kind. So for any chosen class, a counterexample is the natural first attack on ZM1-I1[O].

### 3.3 Loops: rule R-b, the area form, and the exponent `p`

**Rule R-b (proposed repair of the zero rule; not adopted).** In this subsection `Γ` denotes a rectangle and `C` a constant; `ZM1_OBS.md` line 132 writes `C` for both. Let `Γ` range over coordinate-plane rectangles with sides `R,T≥1`, in every position, with their cell-group images. Let `Y` range over `W_Γ` on both laws and, on `L5-U`, also `W_Γ^*W_Γ`. Write `F_0(Y)=ω₀(Φ(Y))` and `F_1(Y)=ω₁(Y)`.
- (z) `F_0(Y)=0` if and only if `F_1(Y)=0`. A violation fails the bound.
- Where both values are nonzero, put `w_i(Y)=−log|F_i(Y)|`. Budgets (b-P) and (b-A) apply to every such `Y`.
- (b-Cr): for `Γ` with `R,T≥2`, let `Γ′,Γ″,Γ‴` share the corner of `Γ` with least coordinates and have sides `(R−1,T−1)`, `(R,T−1)`, `(R−1,T)`. If the four values of the same type (`W` or `W^*W`) are nonzero, put `χ_i(Γ)=w_i(Γ)+w_i(Γ′)−w_i(Γ″)−w_i(Γ‴)` and impose `|χ_0(Γ)−χ_1(Γ)|≤C min(R,T)^{-p}`. If one of the four vanishes, (z) already compares the zero pattern and no `χ` comparison is made.

The per-position definition matters because ZM1-I1[O] does not require `ω₁` to be translation invariant. Four tests: §4.

**Proposition A (the area form at fixed `p>1`).** Let `w_i(R,T)=2μ_i(R+T)+c_i+o(R+T)` with `μ₀≠μ₁`. For every `p>1` and every constant `C`, (b-A) fails on the squares `R=T=n` for all large `n`.

*Proof.* `|w₀−w₁|=4|μ₀−μ₁|n+O(1)+o(n)`, while `C·RT·min(R,T)^{-p}=Cn^{2−p}=o(n)`. □

At `p=1` the right side is `C·max(R,T)`, while `|w₀−w₁|≤4|μ₀−μ₁|max(R,T)+O(1)+o(R+T)`. So (b-A) holds for a large enough `C`, and the area form is blind to perimeter coefficients at `p=1` only. At a fixed `p>1` it compares them, like (b-P).

**Lemma P1 (the existential exponent is `p=1`).** In the ranges `r≥1`, perimeter `|Γ|≥1`, `min(R,T)≥1` and `0<κ≤1`, every budget of `ZM1_OBS.md` §5 is nonincreasing in `p`. So a candidate that meets a budget with some `p≥1` (and some `κ₀` in (c) and (d2)) meets it with `p=1` and `κ₀′=min(κ₀,1)`, with the same constants. Hence every ZM1-I1[O] that reads "there exist ... `p≥1`" is equivalent to its `p=1` case.

*Proof.* In these ranges `r^{-p}≤r^{-1}`, `tr^{-p-1}≤tr^{-2}`, `|Γ|^{1-p}≤1`, `min(R,T)^{-p}≤min(R,T)^{-1}`, `κ^p≤κ` and `tκ^{p+1}≤tκ²`. □

The original ZM1-I1 (`ZM1.md` line 361) has the same form. So the rate exponent carries content only if the owner fixes it. `TOE_ASSEMBLY.md` line 281 asks `ZM1(a)1` for "an explicit `p >= 2`". In the existential reading, Theorem 7's moment clause reduces to `n=0`, which its first clause already gives, and Proposition A does not apply.

### 3.4 Class (c) without a candidate-dependent domain

*The problem.* Line 146 reads: "Fix a finite local invariant list `O_a` and states for which the `t=0` correlation matrices are absolutely summable." `Φ` and `ω₁` belong to the candidate. Read as a domain, the condition lets a candidate whose correlations are not summable escape the comparison. Read as a requirement, it presumes enough decay; the main-branch comparator note records plaquette covariance that is "not absolutely summable" in its `d≥3` setting (MASSIVE_WILSON note line 238). Also, `T^{(1)}_β` exists as a unitary group commuting with `U₁` only if `ω₁` is invariant under coarse cell translations, and ZM1-I1[O] asks only for "a stationary coarse state" (line 25).

**Lemma SP (summable profiles).** Let `T` be a unitary representation of `Z³` on `H`, let `U` commute with it, and let `v₁,…,v_d∈H`. For `f∈ℓ¹(Z³)^d` put `ξ(f)=Σ_{a,β}f_a(β)T_βv_a`.
1. The series converges in norm, and `‖ξ(f)‖≤‖f‖₁max_a‖v_a‖`.
2. If `f̂` is `C⁴` on `T³`, then `f∈ℓ¹`.
3. If `Σ_β‖C(β,0)‖<∞`, then `ξ` agrees on `ℓ¹` with Theorem 7's bounded extension.
4. Let `ρ` be smooth, supported in the unit ball, with `∫|ρ|²=1`. For unit `u` put `f̂_δ(θ)=(2π)^{3/2}δ^{-3/2}ρ((θ−θ₀)/δ)u`, and define `g_δ` from `u′` in the same way. Then `‖f_δ‖=1`, `f_δ∈ℓ¹`, and for every density `c(θ,t)` that represents the form `⟨ξ(f),U^tξ(g)⟩` and is continuous at `θ₀`, `⟨ξ(f_δ),U^tξ(g_δ)⟩→⟨u,c(θ₀,t)u′⟩` as `δ→0`.

*Proof.* (1) `‖T_βv_a‖=‖v_a‖`. (2) `f(β)=(2π)^{-3}∫f̂(θ)e^{−iθ·β}dθ`; four integrations by parts in the coordinate with the largest `|β_j|` give `|f(β)|≤C(1+|β|)^{-4}`, which is summable on `Z³`. (3) `ℓ¹⊂ℓ²`; both maps are bounded and agree on finitely supported `f`. (4) Parseval gives `‖f_δ‖²=∫|ρ|²=1`; (2) gives `f_δ∈ℓ¹`; the form equals `∫|ρ(y)|²⟨u,c(θ₀+δy,t)u′⟩dy`, which converges by continuity at `θ₀`. □

The proofs of Theorems 7-9, 8′ and 9′ use normalized profiles only through the limits in (4). So they hold verbatim with smooth profiles in `ℓ¹`.

**Repair R-c (proposed; not adopted).** Class (c) as on lines 146-151, with three changes.
- Profiles: `f,g∈ℓ¹(Z³)^d` with `f̂,ĝ` supported in `|θ|≤κ`, and `ξ_i(f)=Σ_{a,β}f_a(β)T^{(i)}_βv_{i,a}` (norm-convergent, Lemma SP). No summability domain.
- The coarse state is invariant under the coarse cell translations, as in `ZM1.md`'s Consequence (line 372). Replacing `ω₁` by `ω₁∘E₁` keeps this invariance, since `E₁` commutes with the cell lifts (`VC1_5.md` Theorem 2.1 for the coarse law).
- The list is either fixed by the owner now, or it is every finite list of local elements of `𝔄₁^G`, with list-dependent constants.

Theorem 7's rigidity then applies where its summability holds, and Theorems 8-9, 8′, 9′ where their band forms hold. Four tests: §4.

### 3.5 Lemma C′-free: bilocals in the free comparison

**Lemma C′-free.** Assume the hypotheses of `ZM1.md` Theorem Z2 (line 240: `F=1` or `5`, `0<ε<π/2`, `μ=0`, `L≥2`), with `Φ=Γ(J̃_L)`, fine sea `P`, coarse sea `P_c` and the free walk as coarse law. Let `0<κ≤√v/2`, `t∈N` and `β(t)=(3.5/v+2.66)κ²+1.5tκ³`. Let `K,K′` be trace-class operators on the coarse one-body space with `K=P_κKP_κ` and `K′=P_κK′P_κ`, where `P_κ` projects onto momentum support `|θ|≤κ`. For a singular value decomposition `K=Σ_nσ_n|w_n⟩⟨u_n|` put `B_K=Σ_nσ_nc₁^†(w_n)c₁(u_n)`, the coarse bilinear `Σ_{X,Y}K_{XY}c₁^†_Xc_{1,Y}`. Then `B_K` converges in norm, and
\[
 \big|\omega_P\big(\Phi(B_K)^*\alpha^{Lt}(\Phi(B_{K'}))\big)-\omega_{P_c}\big(B_K^*\alpha_1^{t}(B_{K'})\big)\big|\le 6\,\beta(t)\,\|K\|_1\|K'\|_1 .
\]
The truncated values differ by at most `8β(t)‖K‖₁‖K′‖₁`.

*Proof.* For `σ_n>0`, `u_n` and `w_n` lie in `ran P_κ`, because `K^*K` and `KK^*` have their ranges there. For unit vectors `‖c^†(w)c(u)‖≤1`, so both series converge in norm, with norms at most `‖K‖₁` and `‖K′‖₁`. Expand both expectations in the two decompositions. By `Φ(c₁(h))=c(J̃h)` and `α^{Ls}(c(h))=c(V^{-Ls}h)` (`ZM1.md` line 279), a fine term is
\[
 \omega_P\big(c^\dagger(\tilde Ju)\,c(\tilde Jw)\,c^\dagger(V^{-Lt}\tilde Jw')\,c(V^{-Lt}\tilde Ju')\big),
\]
and the coarse term drops `J̃` and has `V^{-t}`. The CAR give `c(a)c^†(b)=⟨a,b⟩−c^†(b)c(a)`. So each term is a scalar `⟨J̃w,V^{-Lt}J̃w′⟩` times a normally ordered two-point function, minus a normally ordered four-point function.
1. The scalars differ by at most `2.66κ²+1.5tκ³≤β(t)`. Indeed `J̃^*J̃=1` gives `⟨J̃w,V^{-Lt}J̃w′⟩−⟨w,V^{-t}w′⟩=−⟨J̃w,V^{-Lt}(V^{Lt}J̃−J̃V^t)V^{-t}w′⟩`, and Theorem Z2(3) (line 243) applies to `V^{-t}w′`, which has the same momentum support.
2. The two-point functions differ by at most `β(t)`, and the four-point functions by at most `4β(t)`. These are the cases `n=1` and `n=2` of the normally ordered bound `n^{(n+2)/2}β` (`ZM1.md` line 277), with times in `{0,t}`. Reordering the annihilators changes both sides by the same sign.

Every scalar and every function has modulus at most `1`, so a term differs by at most `β+β+4β=6β(t)`. Sum with weights `σ_nσ′_m`. For the truncation, each one-point value differs by at most `β(0)‖K‖₁` (the case `n=1` at `T=0`) and has modulus at most `‖K‖₁`, so the products differ by at most `2β(0)‖K‖₁‖K′‖₁≤2β(t)‖K‖₁‖K′‖₁`. □

So with c-number links the bilocals of (c′) obey `p=2` for times `t≤1/κ`, in an absolute trace-norm budget. The relative form of line 149 is not proved for them. The quantum-link form needs the c-number reduction that `ZM1.md` Attack 2 (line 382) does not supply.

### 3.6 Class (d): limit amplitudes and axial averaging

**Lemma DL (limit amplitudes).** Fix `i∈{0,1}`, an axis `e` and a coarse site `X`. Write `Φ₀=Φ`, `Φ₁=id`, `U_{(0)}=Ũ^L` and `U_{(1)}=Ũ₁`. Let `ω_i` be locally gauge invariant, stationary, and invariant under the coarse cell translation along `e` (for `i=0`, its fine lift). Write `B_n(Y)=B^{(1)}_{n,1}(Y)` for the coarse straight string with `2n` links from `Y` along `e`; its far end is `Y+2ne`. Assume `‖π_i(Φ_i(B_n(Y)))Ω_i‖>0` for all `Y∈X+2Ze` and `n≥n₀`. For `k<n−n₀` put
\[
 u^{(n)}_k=\frac{\pi_i(\Phi_i(B_{n-k}(X+2ke)))\Omega_i}{\|\pi_i(\Phi_i(B_{n-k}(X+2ke)))\Omega_i\|},\qquad a_n(k,t)=\langle u^{(n)}_0,\,U_{(i)}^t\,u^{(n)}_k\rangle .
\]
1. `a_n(k,t)` is the normalized (d2) amplitude of line 164 at string length `n` and displacement `k`.
2. `⟨U_{(i)}^su^{(n)}_j,U_{(i)}^tu^{(n)}_{j′}⟩=a_{n−j}(j′−j,t−s)`.
3. If `A(k,t)=lim_{n→∞}a_n(k,t)` exists for every `(k,t)∈Z²`, then `A` is a positive-definite function on `Z²` with `A(0,0)=1`.
4. Then there are a Hilbert space, commuting unitaries `T` and `U` on it, and a cyclic unit vector `v` with `A(k,t)=⟨v,U^tT^kv⟩`. So Setting F holds in one dimension for the limits, and Theorems 7-9, 8′ and 9′ apply to `(A₀,A₁)` under their remaining hypotheses.

*Proof.* (1) Both strings end at `X+2ne`. By Theorem 12 (on the fine side, through Theorem 2 at the far coarse site), `ω_i(Φ_i(B_{n,b}(X))^*α_{(i)}^t(Φ_i(B_{n−k,b′}(X+2ke))))` is `δ_{bb′}` times a value independent of `b`. Likewise `N_i(Y,m)=D‖π_i(Φ_i(B_m(Y)))Ω_i‖²`, with `D` free indices (5 on U, 10 on O). The `D` equal terms divided by `[D‖·‖²·D‖·‖²]^{1/2}` give `a_n(k,t)`. (2) The unitary implementing the translation by `−j` cells maps the two strings to `B_{n−j}(X)` and `B_{n−j′}(X+2(j′−j)e)` and commutes with `U_{(i)}`. On the fine side, (Z-b) intertwines `Φ` with the lift up to a global phase or global parity. Both strings carry the same charge, so the factor is common and cancels in the inner product. (3) For finitely many `(j_a,s_a)` and `c_a∈C`, (2) gives `Σ_{a,b}c̄_ac_bA(j_b−j_a,s_b−s_a)=lim_n‖Σ_bc_bU_{(i)}^{s_b}u^{(n)}_{j_b}‖²≥0`. (4) Complete the finitely supported functions on `Z²` in the form `⟨δ_{(j,s)},δ_{(j′,t)}⟩=A(j′−j,t−s)`, after dividing out null vectors. The two shifts preserve the form, so they act as commuting unitaries; take `v=δ_{(0,0)}`. □

**Lemma AX (axial averaging).** Let `T` be a unitary representation of `Z³`, `U` a unitary commuting with it, and `v` a vector with
\[
 \langle\xi(f),U^t\xi(g)\rangle=(2\pi)^{-3}\!\int\overline{\hat f}\,\hat g\;W(\theta)\,e^{-itw(\theta)}\,d\theta\qquad(f,g\in\ell^1(\mathbb Z^3),\ t\in\mathbb N_0),
\]
where `W≥0` is bounded, `w` is real, and both are continuous off `θ=0`. Fix an axis `e`, write `θ=(θ_e,θ_⊥)`, and let `ν_{θ_e}` be the image of the measure `(2π)^{-2}W(θ_e,θ_⊥)dθ_⊥` under `θ_⊥↦w(θ_e,θ_⊥)` mod `2π`. Then the axial amplitudes `⟨v,U^tT_{ke}v⟩` have the axial density `c_e(θ_e,t)=∫e^{−itμ}dν_{θ_e}(μ)`, continuous in `θ_e`. If near some `θ_e⁰` they also have a finite branch form `Σ_kW_k(θ_e)e^{−itλ_k(θ_e)}` with continuous data, then `ν_{θ_e}=Σ_kW_k(θ_e)δ_{λ_k(θ_e)}` there. So if `ν_{θ_e}` is nonzero and has no atoms, no finite branch form exists near `θ_e`.

*Proof.* A profile supported on the axis has `f̂` depending on `θ_e` alone. Fubini turns the three-dimensional form into the axial form with density `c_e`. Dominated convergence makes `c_e` continuous, since the point `θ=0` meets each slice in a null set. Two densities that represent the same form on band-limited axial profiles and are continuous agree pointwise (Lemma SP(4) in one dimension). At fixed `θ_e` both sides are then the Fourier coefficients, for `t≥0`, of finite positive measures on the circle. For `t<0` the coefficients are the complex conjugates. A finite measure on the circle is determined by its Fourier coefficients. □

*Application: the free massless walk.* In the free analogue of (d) the links are c-numbers, so the strings reduce to creators `ψ^†_{X,b}`. The coarse (d2) amplitude is then the on-axis particle propagator `ω_{P_c}(ψ_{X,b}α₁^t(ψ^†_{X+2ke,b}))`. Its three-dimensional density is `W(θ)e^{∓itw(θ)}`, where `W` is a diagonal entry of the positive-band projection `1−P_c(θ)` and `±w(θ)` are the eigenvalues of `h(θ)` (`ZM1.md` line 265). The same line gives `1 − cos w = s^2 (1 − chi)` with `1 − chi = (2/3) sum_j sin^2(theta_j/2)`. So at fixed `θ_e` the function `w(θ_e,·)` is a strictly increasing function of `ζ(θ_⊥)=Σ_{j⊥e}sin²(θ_j/2)`, a nonconstant real-analytic function on `T²` (here `s=sin ε>0`, and `w∈[0,π)`). Its level sets are null, so `ν_{θ_e}` has no atoms. For `θ≠0`, `h(θ)` has the positive eigenvalue `w(θ)≥2v|θ|/π>0` (line 265), so `tr(1−P_c(θ))>0`. Hence for some residue and flavour the diagonal entry has `∫W(0,θ_⊥)dθ_⊥>0`, and by continuity `ν_{θ_e}≠0` for all `θ_e` near `0`. By Lemma AX, for that residue the axial data have no finite branch form at any small `θ_e`. Theorems 8-9, 8′ and 9′ do not apply to them.

So the draft's supply for (d), "the fermion's speeds along `e` (Lemmas S, S′ on (d2)), if its axial data form gapped branches" (draft line 383), fails in the free analogue: a charge that propagates in three dimensions gives an axial phase continuum, not branches. The same holds in the interacting case whenever the limit of Lemma DL is the on-axis amplitude of a three-dimensional covariant structure whose bands have null level sets in `θ_⊥`. Theorem 12 does not change this. It forbids amplitudes between strings with different far ends; it does not forbid transverse motion of the charge between them. The axial data can form branches when the charge does not move transversely, as in the transversely flat setting of `RCS1.md` Corollary 9.

**Repair R-d (proposed; not adopted).** Class (d) as on lines 161-166, with four changes.
1. Write `n` for the string half-length and keep `r` for (a)'s separation.
2. Zero rule: `N₀(X,n)=0` if and only if `N₁(X,n)=0`, for every coarse site `X` and `n≥n₀`. (d1) and (d2) are compared where both are positive.
3. The coarse state is invariant under the coarse cell translation along `e` (Lemma DL(2) needs it).
4. The (d2) budget is stated for the limits `A₀,A₁` of Lemma DL.

Four tests: §4. Two limits remain. A candidate whose block strings all have `N₀=0` meets the string part trivially; whether such a `Φ` exists with the other requirements is not decided. And requiring the limits of Lemma DL to exist presumes convergence, while not requiring them lets the (d2) part lapse.

### 3.7 The twist and ZM1-I1's fine updates

**Proposition T.** Let `U` be an update in LZ1's class (`LZ1.md` line 28). Use `K_φ` and `γ_φ` as in Theorem 5; on `L5-O`, `K_π=∏_xP_x` and `γ_π=θ`.
1. `K_φU` is in LZ1's class, and `α_{K_φU}=α_U∘γ_φ` equals `α_U` on `𝔄^G` (Theorem 5).
2. A locally gauge-invariant state is `α_U`-invariant if and only if it is `α_{K_φU}`-invariant. So VC1's conditions (i)-(iii) select the same states for `U` and `K_φU`, and so do readings E and P (`VC1_5.md` line 29).
3. For every class whose entries lie in `𝔄₁^G` and every candidate `(Φ,α₁,ω₁)`, the data and budgets are the same for `(ω₀,U)` and `(ω₀,K_φU)`.
4. On `L5-U` with `φ∉2πZ`, and on `L5-O` with `φ=π`, `α_{K_φU₀}` equals neither `α_{WU₀}` nor `α_{U₀W}` for any member `W` of GA1-P-5.
5. If `U` is an update of PS-1's nearest-neighbour class under NN-a (`TOE_ASSEMBLY.md` line 235), so is `K_φU`. On `L5-U`, `γ_φ` is implemented by the layer `∏_{x:x₁ even}e^{iφ(N_x+N_{x+e₁})}`; on `L5-O`, `γ_π=θ` by `∏_{x:x₁ even}P_xP_{x+e₁}`.

*Proof.* (1) is Theorem 5. (2) For such a state `ω∘γ_φ=ω` on local elements, and `γ_φ` commutes with `α_U`; so `ω∘α_{K_φU}=ω∘γ_φ∘α_U=ω∘α_U`. Condition (ii), condition (iii) and reading P do not involve the update, and E is extremality within the set that (i)-(iii) fix. (3) follows from (1) and Theorem 2's last clause. (4) GA1-P-5's gates are link-only (`GA1_5.md` line 50: "each `g_X` is a link-only gauge-invariant unitary"), so every member fixes every matter operator. With `α(A)=U^*AU` one has `α_{WU₀}=α_{U₀}∘γ_W` and `α_{U₀W}=γ_W∘α_{U₀}`, where `γ_W(A)=W^*AW`. Since `γ_φ` commutes with `α_{U₀}`, either equality gives `γ_φ=γ_W` on `𝔄`. Apply both sides to `c_{x,j}`: `e^{iφ}c_{x,j}=c_{x,j}`, false for `φ∉2πZ`. On `L5-O`, `γ_π(γ_{x,a})=−γ_{x,a}` gives the same contradiction. (5) On `L5-U` each link has `p_{ℓ,x}+p_{ℓ,y}=m` (`VC1_5.md` §2), so `∏_xe^{iφQ_x}` differs from `∏_xe^{iφN_x}` by the link factors `e^{iφm}`, which are scalars; both give the automorphism `γ_φ`. Each gate `e^{iφ(N_x+N_{x+e₁})}`, or `P_xP_{x+e₁}` on `L5-O`, is a unitary supported in `F_x` and `F_{x+e₁}` that commutes with `P_xP_{x+e₁}`. The edge triples `(x,x+e₁,ℓ)` with `x₁` even are pairwise disjoint and cover every site, so the product is one nearest-neighbour layer. Composing with `U` adds one layer, so the depth stays finite and independent of volume. `α_{K_φU}=α_U∘γ_φ` fixes every local gauge generator, because `γ_φ` fixes the number-conserving bilinears `G^T_x` (on `L5-O`, the even bilinears `G^{cd}_x`) and `α_U` fixes them. `γ_φ` commutes with every cell lift, because each lift sends a matter mode to a signed matter mode (`VC1_5.md` Theorem 2.2) and `γ_φ` multiplies every matter annihilator by the same phase. □

So, for classes with invariant entries, ZM1-I1[O] posed for fine updates in LZ1's class does not distinguish `U` from `K_φU`. Under NN-a both are PS-1 updates (5). ZM1-I1 as stated admits "base tick, or with a plaquette class that GA1-P-5 supplies" (`ZM1.md` line 361), and (4) shows that `K_φU₀` is not of that form with the base tick `U₀`. Whether `α_{K_φU₀}` equals the tick of a base law with other constants is not decided here. Whether the five-mode law's update class should contain the matter-phase layer, as a chemical-potential-like free constant, is a law-specification choice for the owner.

*Bearing on LZ1's census.* `K_φU` is in LZ1's class, so `LZ1.md` Theorem 2.2 (line 56) applies to it: "Every band in `H_nt` is identically `1` on any connected `C¹` neighbourhood of a node." So on odd bands the twist removes and creates only flat nodes. Under LZ1-SC the dispersion clause applies only to bands with image in `ker(Ũ−1)^⊥` (`TOE_ASSEMBLY.md` line 229), and a band equal to `1` near a node does not have such an image. So the twist does not affect that clause on odd bands. On charged even bands, such as charge `±2` composites in the trivial pattern, Theorem 2.2 does not apply, and Theorem 5 lets the twist move a propagating node.

---

## 4. Four-test verdicts and the ranking

The four tests: a proposed reading or specification fails if it (1) states or fixes a part's target, (2) is open-ended so a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. P means pass, C conditional.

### 4.1 The classes

Pass 2 retains pass 1's verdicts (line 186), so one column shows both.

| Class | Passes 1-2 | Referee, as written | Referee, after the repairs | Reasons for the referee verdicts |
|---|---|---|---|---|
| (a) | P P P P | P P P P | P P P P | (1) No target, no existence, no fixed `p`. (2) Every support radius is quantified, and the constants `C_{R₀}` are existential. (3) Dropping charged data settles nothing: in locally gauge-invariant vacua charged two-point data are on-site (Theorem 2 and the paragraph on line 75), and (a) asserts no MT1-S or GA2 conclusion. (4) The relative form is needed by Theorem 6 and the vanishing rate by ZM1(a)1. Lemma ER shows what the envelope then forces, exact tail matching, which is long-distance content. Test 4 stays a judgment, as line 126 says. |
| (b-P) | P C P C | P C P C | P P P C | (2) Rule R-b assigns every zero case. (4) It demands equality of the perimeter coefficient, a local self-energy quantity that a long-distance comparison does not need; the draft's item 23 is context for this, not a premise. |
| (b-A) | P C C P | P C P P | P P P P at `p=1`; P P P C at a fixed `p>1` | (3) As for (b-Cr): the form compares `σ` and assumes no value of it. Blindness to the perimeter coefficient leaves a question open; it does not settle it. If the owner keeps pass 1's stricter reading of test 3, then (b-A) and (b-Cr) both get C. (2) Rule R-b. At a fixed `p>1` the form compares perimeter coefficients (Proposition A) and gets (b-P)'s test-4 C. By Lemma P1 the existential statement is the `p=1` case. |
| (b-Cr) | P C P P | P C P P | P P P P | (2) Rule R-b. (3) As for (b-A). (4) Theorem 11's cancellation is what the form is for. |
| (c) | P C P C | P C P C | P P P C, if the list is fixed now or quantified universally | (2) As written, the list, the profiles and the summability domain are open, and the domain depends on the candidate (§3.4). R-c fixes the profiles and removes the domain. (4) Theorem 7 forces exact zero-momentum sums, contact terms included, which speed transfer does not need. |
| (d) | P C C C | P C C C | P C C C | (2) The axis, the limits and the odd label beyond parity-sharp backgrounds need fixing, and (d2) either presumes the limits of Lemma DL or lapses (§3.6). (3) It builds the working candidate R-CS^str into ZM1-I1 before RCS-P and MT1-S settle (`TOE_ASSEMBLY.md` line 225). (4) The axis decides which motion the data can show (Theorem 12). R-d adds only what the data need, so it changes no verdict. |
| (e) | C P P P | C P P P | C P P P | (1) It moves ZM1-I1 from one interacting step to ZM1(a)1 along the tower. (2) ZM1-I1[e] quantifies the tower existentially, so it is closed once each `Φ_k` is a Definition-Z map as §1 requires (R-e makes this explicit). The limit-point clause is a use of the class, not part of its statement. |

### 4.2 The proposed repairs

| Repair | 1 | 2 | 3 | 4 | Check |
|---|---|---|---|---|---|
| R-b (§3.3) | P | P | P | P | It fixes no loop value. Every case is assigned. Zeros are compared, not excluded, and two zeros pass, as the data allow (Theorem 10). It adds only what the logarithm and `χ` need: nonzero values and `R,T≥2`. |
| R-c (§3.4) | P | P | P | P | It removes a condition. Summable profiles are standard and define the data for every candidate. Translation invariance of `ω₁` is what Setting F needs; `ZM1.md`'s Consequence (line 372) already assumes it. |
| R-d (§3.6) | P | P | P | P | Each clause is needed for the data to be defined (zero rule), covariant (translation invariance) or of Setting F's form (limits). Class (d) keeps P C C C. |
| R-e (R15) | P | P | P | P | It restores the draft's specification (draft line 398) with ZM1-I1's own conditions. |

These are proposed specifications, not adoptions. The owner chooses.

### 4.3 The ranking

Pass 1 lists its criteria with the words "The criteria, in order." (draft line 419): content in VC1 vacua, well-posedness on finite quantum links, the four tests, fit to ZM1-I1 as one interacting step, and downstream supply. Read in that order, they do not give pass 1's ranking. Criterion (i) does not separate the classes. After R-b, criterion (ii) does not separate (b) either: its loops are well-defined quantum-link observables, and Theorem 10 concerns their content, not their definition. With the referee's test-3 verdict, criterion (iii) then puts (b-Cr) level with (a), and (e) level with repaired (c). So pass 1's order uses a further weighting. Two of its stated reasons for (b)'s place also fail. "Creutz ratios avoid both" (draft line 425) is false for the first defect it names: by Theorem 11 the Creutz form cancels every `f(R)+g(T)`, so it is as blind to perimeter-law differences as the area form. "It supplies nothing to LZ1-i" holds for the loop data only, since (a)⊂(b).

The weighting can be stated: *prefer the least demanding class whose added data a named consumer uses.* With the corrected verdicts it gives:
1. **(a).** The least demanding P P P P class. Its data are the physical-sector data that GA2's and T0's gauge-invariant interface and LZ1-i read; the dictionary to the continuum is still to be supplied.
2. **(c).** It adds the spectral data that LZ1-i uses: speed transfer for even species (Theorems 8-9, 8′, 9′). Its cost is the zero-momentum rigidity of test 4.
3. **(e).** Class (a) along the tower. ZM1-i needs this form. It is not one step (test 1 C).
4. **(b).** P P P P in its Creutz form after R-b, but no named consumer uses `σ` as stated. GA2(a)'s window "`a << r << Lambda_i^{-1}`" (`TOE_ASSEMBLY.md` line 405) excludes the string-tension scale, T0 asserts no area law, and LZ1-i reads no loops. In sharp-flux states its fundamental loops vanish (Theorem 10).
5. **(d).** P C C C, and it depends on R-CS^str. Its one distinctive consumer is the fermion of MT1-S and LZ1-i. Lemma AX shows that Theorems 8-9 do not deliver that fermion's speeds from (d2) when it propagates in three dimensions: in the free analogue, and in the interacting case under the lemma's hypothesis.

This order differs from pass 1's only in the last two places. It is a judgment under a stated weighting, not a theorem. The classes nest, (a)⊂(b) and (a)⊂(d), and combinations are possible, as line 184 says.

---

## 5. Required edits

Each edit marks imported text "(referee closure, ZM1_OBS_REFEREE.md)" or, for a class specification, "(proposed repair, ZM1_OBS_REFEREE.md; not adopted)". R2-R4 and R6-R8 fix statements. R9, R11, R12 and R15 change class specifications. R10 and R17 change four-test verdicts and the ranking text. The rest add a missing convention, step or import.

- **R1 (line 65; row 26).** After the definition of `ξ_i(f)` add: "Here `f̂(θ)=Σ_βf(β)e^{iθ·β}`, so `‖f‖²=(2π)^{-3}∫|f̂|²`, and `c_i(θ,t)` is defined when the sum converges absolutely."
- **R2 (lines 77, 81-85; rows 30, 32).** In Theorem 8 add the hypothesis `Σ_β|C_i(β,0)|<∞` and state the band hypothesis as in the draft (line 231): `⟨ξ_i(f),U_i^tξ_i(g)⟩=(2π)^{-3}∫\bar{f̂}ĝ\,w_ie^{-itλ_i}dθ` for all `t∈N₀` and all `f,g` with Fourier support in `B_{κ₀}`. In Theorem 9 add `Σ_β‖C_i(β,0)‖<∞`, state the branch form in the same way, and replace "`Σ_k‖W_{i,k}‖≤S<∞`" by: "Then `Σ_k‖W_{i,k}(θ)‖≤n_iΣ_β‖C_i(β,0)‖` (referee closure, ZM1_OBS_REFEREE.md, Lemma S0)."
- **R3 (line 85; row 33).** Replace the last sentence of Theorem 9 by: "A cone `±v|θ|`, `v>0`, satisfies the gap condition with `g=2v`. The theorem applies to it only if both branches carry weights at least `w`."
- **R4 (lines 9, 89; rows 3, 35).** Replace the first two sentences of GAP S′ by: "With the draft's summability hypothesis the weight bound `S` is automatic (referee closure, ZM1_OBS_REFEREE.md, Lemma S0). Near `θ=0` all phases are small, so plain and circular distances agree. The conclusion needs `p>0`, which every class meets." In line 9 replace "Its several-branch proof needs uniform weight bounds, circular phase separation and `p>0`." by "Its several-branch lemma needs `p>0`, which every class meets."
- **R5 (after line 87, and line 153; rows 30, 54).** Insert Theorems 8′ and 9′ of §3.1 after Theorem 9, each marked as a referee closure. In line 153 add: "By Theorems 8′ and 9′ this includes species whose composite weight vanishes at zero momentum, provided it is positive off zero, or comparable across branches."
- **R6 (line 59; row 23).** Replace "if `|F_i(d)|≤s(d)` for both sides" by "if `|F_0(d)|≤s(d)` and every candidate has `|F_1(d)|≤s(d)`".
- **R7 (line 103; row 41).** Replace "with nontrivial continuous representation" by "covariant under a group whose continuous finite-dimensional image is infinite (`GA2_Y2.md` Corollary 2.2). For the connected groups `U(5)` and `Spin(10)` this is every nontrivial continuous representation; for a finite image, Theorem 2.3 there gives an invertible link".
- **R8 (lines 9, 55; rows 3, 22).** Append to GAP C-law: "The vacuum reading is closed under the twist. `K_φU₀` differs from the base tick composed with any GA1-P-5 member, whose gates are link-only (`GA1_5.md` line 50). Under NN-a, `K_φU` is a PS-1 update whenever `U` is (referee closure, ZM1_OBS_REFEREE.md, Proposition T). So the twist relates two PS-1 updates with the same invariant data; only one has the `L5-U` form that ZM1-I1 states." In line 9 replace "The draft's unconditional identification of the twist with another admissible *base five-mode law* is not established." by "The draft's Theorem C(4) treats `K_φU₀` as an admissible ZM1-I1 fine update; it is a PS-1 update under NN-a but not of the stated `L5-U` form."
- **R9 (lines 136, 138; row 49).** Replace "Pass 1 proposes that two zero expectations pass and exactly one zero fails." and GAP b-zero by rule R-b of §3.3, marked as a proposed repair.
- **R10 (line 142; row 52).** Replace the first sentence by: "**Four tests, proposed:** (b-P) P C P C; (b-A) P C P P; (b-Cr) P C P P. With rule R-b, test 2 passes for all three. (b-A) and (b-Cr) compare only `σ` (Theorem 11) and assume no value of it; in perimeter-law vacua they add no loop content beyond (a)." In the third sentence replace "The area form can discard perimeter distinctions" by "At `p=1` the area and Creutz forms discard perimeter distinctions; at a fixed `p>1` the area form compares them and gets (b-P)'s test-4 C (referee closure, ZM1_OBS_REFEREE.md, Proposition A)". Keep the other sentences.
- **R11 (lines 146-151; row 53).** Replace "and states for which the `t=0` correlation matrices are absolutely summable" by repair R-c (§3.4), marked as a proposed repair, and add Lemma SP as a referee closure.
- **R12 (lines 161-166; row 57).** Apply repair R-d (§3.6): write `n` for the string half-length, add the zero rule and the translation invariance of `ω₁`, and state the (d2) budget for the limits of Lemma DL.
- **R13 (line 168; row 58).** Append: "If the normalized (d2) amplitudes converge as the string length grows, for every displacement and tick, the limits form a positive-definite function on `Z²` with a covariant cyclic representation (referee closure, ZM1_OBS_REFEREE.md, Lemma DL). Theorems 8-9 then apply under their remaining hypotheses. Those hypotheses fail when the charge propagates in three dimensions: in the free massless walk the on-axis amplitude, for some residue, has no finite branch form at any small axial momentum (Lemma AX)."
- **R14 (line 155; row 55).** After "no such proof is supplied" add: "For trace-class kernels with Fourier support in `|θ|≤κ` in both variables, the free comparison holds with absolute error `8β(t)‖K‖₁‖K′‖₁`, so `p=2` (referee closure, ZM1_OBS_REFEREE.md, Lemma C′-free). The relative form of line 149 is not proved for bilocals."
- **R15 (line 174; row 60).** Replace "Take compatible one-step maps `ι_j:𝔄_j→𝔄_{j-1}`, compositions `Φ_k=ι₁⋯ι_k`, coarse laws and states." by "Take block maps `Φ_k:𝔄_k→𝔄` of factor `2^k` (Definition Z with (Z-a), (Z-b), (G1)-(G2) and singleton sets), each a composite `Φ_k=ι₁∘⋯∘ι_k` of one-step maps `ι_j:𝔄_j→𝔄_{j−1}`, with coarse laws `α_k` and `α_k`-invariant states `ω_k` (draft line 398)."
- **R16 (line 186; row 65).** Replace "its P for (e)'s closedness presumes the common algebra and tower have actually been fixed" by "its P for (e)'s closedness holds for ZM1-I1[e], which quantifies the tower existentially; the common algebra enters only the optional limit-point clause".
- **R17 (line 184; row 64).** Add: "The stated criteria do not determine this order (ZM1_OBS_REFEREE.md §4.3). Under the weighting 'prefer the least demanding class whose added data a named consumer uses', the corrected verdicts give (a), (c), (e), (b), (d). The order is a judgment, not an owner selection."
- **R18 (line 126; row 48).** After "Thus test 4 is a judgment, not a theorem that no extra structure was introduced." add: "The bound forces `|m₀(r)−m₁(r)|≤C_{R₀}(r^{-p}+tr^{-p-1})max_im_i(r)` for the tail envelopes `m_i(r)=sup_{|β|_∞≥r}|F_i^T|`, hence exact asymptotic equality of every invariant channel's correlation length and tail amplitude (referee closure, ZM1_OBS_REFEREE.md, Lemma ER)."
- **R19 (line 25; row 8).** After "Constants may depend on an explicitly quantified support radius or composite list." add: "Every budget in §5 weakens as `p` decreases, so 'there exist ... `p≥1`' is equivalent to `p=1` (referee closure, ZM1_OBS_REFEREE.md, Lemma P1). A fixed `p`, such as ZM1(a)1's 'explicit `p >= 2`' (`TOE_ASSEMBLY.md` line 281), must be stated to carry content."
- **R20 (line 39; row 14).** Replace "a single charged entry at `X` and no other entry charged at `X`" by "one entry whose span carries a representation of the local group at `X` with no invariant vector, all other entries being invariant at `X`,".
- **R21 (lines 7, 9, 11, 188).** Add to "Proved": "Referee closures, unrefereed: Lemma S0, Theorems 8′ and 9′, Lemma ER, Proposition A, Lemma P1, Lemma SP, Lemma C′-free, Lemmas DL and AX, Proposition T (each ZM1_OBS_REFEREE.md)." In line 9 record GAP b-zero as repaired by R-b and apply R4 and R8. In line 11 add the open statements of §6 below. In line 188 add: "`GA1_5.md` line 50 (GA1-P-5's gates are link-only), `VC1_5.md` line 29 (readings E and P) and `TOE_ASSEMBLY.md` line 235 (NN-a) bear on the twist (Proposition T)."

---

## 6. Open statements to carry by name

None of these was attacked in this lane; each is inherited or left open by the closures above.
- **ZM1-I1[a], ZM1-I1[b], ZM1-I1[c], ZM1-I1[d], ZM1-I1[e].** Specifications, not worked, as `TOE_ASSEMBLY.md` line 227 directs. For any chosen class, Lemma ER, Theorem 7 and Theorem 11 make a counterexample the natural first attack.
- **ZM1-I1, the owner's selection**, with §4's table and the R-b, R-c, R-d and R-e repairs.
- **ZM1-OBS-twist.** Whether the five-mode law's update class should contain the matter-phase layer `∏_xe^{iφN_x}` (a PS-1 update under NN-a, Proposition T(5)), and whether `α∘γ_φ` equals the tick of a base law with other constants. The first is a law-specification choice for the owner.
- **ZM1-OBS-d-lim.** Whether the normalized (d2) amplitudes converge in the VC1 vacuum (the hypothesis of Lemma DL). By Lemma AX, convergent limits give branch data only when the charge does not move transversely.
- **The relative and quantum-link forms of (c′).** The quantum-link form needs the c-number reduction of `ZM1.md` Attack 2 (line 382).
- **ZM1-i**, with GAP e-dynamics: the tower, convergence of its updates, and its charged sectors.
- Inherited, unchanged: Z2-spatial, ZM1-ii, ZM1-G, Y1, VC1, GA1-P, GA1-P-5 and the rung rule (`ZM1.md` line 16); RCS-P, MT1-S[R-CS^str] and R-CS (`RCS1.md` line 18).

## 7. Freeze recommendation

**Freeze `ZM1_OBS.md` after R1-R21.** No ERROR changes a numbered theorem. R2 restores hypotheses the draft had. The referee closures enter marked as such and stay unrefereed. R9, R11, R12 and R15 change class specifications, and R10 and R17 change four-test verdicts and the ranking text; these bear on the owner's choice, so the lead should apply them before the class question goes to the owner. `TOE_ASSEMBLY.md` line 229 records the owner's request "that every owner question be checked by Codex `gpt-6-astra` at max effort before it is put to them", so the class choice goes through that check first, with §4's table.

---

## Prior work used

- `prior/ZM1_OBS.md` (the digest; the file does not name its author model): its overlap verdicts place each result (for example, Theorem 3 duplicates `RCS1.md` Theorem 4). Its five main-branch citations and its YM-branch citation were checked by line (rows 29, 51, 62).
- `ZM1.md`: Definition Z and its correlation error (line 56); Theorem Z2 (line 240) and its bound (3) (line 243); the eigenvalue relation of `h(θ)` in the proof of Z2(4) (line 265); the normally ordered `2n`-point bound (line 277, a referee closure there) and its conventions (line 279); the precise ZM1-I1 (line 361); R-GI and its Consequence (lines 368-374); Attack 2 (line 382); the open list (line 16). Extended in Lemma C′-free, Lemma AX, Lemma P1 and Proposition T.
- `RCS1.md`: definition 5 (line 30), Theorem 4 (line 64), the straight strings of §5 (line 82), Theorems 7-8 (lines 97, 101), Corollary 9 (line 125), the open list (line 18). Used in rows 15-21, 38 and 42-44 and in Lemma DL.
- `GA2_Y2.md`: Theorem 2.1 (N), Corollary 2.2 (line 34), Theorem 2.3 (line 40), Theorems 2.5 and 3.4. Used in row 41.
- `LZ1.md`: the update class (line 28), bands (line 36), Theorem 2.2 (line 56). Used in Proposition T.
- `VC1_5.md`: definition 5 (line 29), §2 (fixed link number `m`), Theorems 2.1, 2.2 and 5.5 (line 117). Used in Proposition T, repair R-c and row 38.
- `GA1_5.md`: the proposed class GA1-P-5 (line 50) and Amendment 1 (line 7). Used in Proposition T(4).
- `TOE_ASSEMBLY.md`: lines 225, 227 and 229 (§3.6), 235 (§3.7, NN-a), 281 (ZM1(a)1) and 405 (GA2(a)). Used in G1, Proposition T, Lemma P1 and §4.3.
- Main branch, context only (checked by line, not used as proof): the MASSIVE_WILSON note's non-summability statement (line 238), cited in §3.4.

**Prior work the digest missed, found here.** `GA1_5.md` line 50 (link-only gates) and `TOE_ASSEMBLY.md` §3.7 (NN-a, recorded after the digest), both bearing on the twist. `VC1_5.md` line 29 (readings E and P), which the draft used and the digest does not list. `LZ1.md` Theorem 2.2, as it bears on what the twist does to LZ1's census. `ZM1.md` line 277, the input for (c′). The new `RCS1.md` Amendment 1 lists `docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md` and `docs/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md` as inputs for RCS-P and R-CS^Dirac; they bear on class (d)'s charged data. This report read only the first one's header and used neither.

---

## FINISH

**Proved here (referee closures; unrefereed).**
- Lemma S0: under summability and `W≥0`, Theorem 9's weight bound `S` is automatic.
- Theorem 8′: one-branch speed transfer needs only `w₁>0` off `θ=0`, and gives `|λ₀−λ₁|≤8πC|θ|^{p+1}`.
- Theorem 9′: several-branch transfer holds under the relative budget, with weights comparable to one positive function.
- Lemma ER: class (a)'s bound makes the two tail envelopes agree to relative order `r^{-p}` at each tick; exponential or power tails then have equal rates and amplitudes.
- Proposition A: at a fixed `p>1`, the area form (b-A) detects perimeter-coefficient differences on square loops.
- Lemma P1: every budget weakens as `p` decreases, so each existential ZM1-I1[O], and the original ZM1-I1, is its `p=1` case.
- Lemma SP: summable profiles define the smeared vectors for every candidate, and Theorems 7-9 keep their localized-profile limits with smooth summable profiles.
- Lemma C′-free: with c-number links, bilocals with trace-class band-limited kernels obey the free comparison with absolute error `8β(t)‖K‖₁‖K′‖₁`.
- Lemma DL: pointwise limits of the normalized (d2) amplitudes form a positive-definite function on `Z²` with a covariant cyclic representation.
- Lemma AX: on-axis amplitudes of a three-dimensional band with null transverse level sets have no finite branch form; in the free massless walk this holds at every small axial momentum, for some residue.
- Proposition T: the twist preserves every invariant datum, VC1's conditions (i)-(iii) and readings E and P. `K_φU₀` is not the base tick composed with a GA1-P-5 member. Under NN-a, `K_φU` is a PS-1 update whenever `U` is.
- Re-derived and found correct: Theorems 1-12 and the compactness proof of `ZM1_OBS.md`.
- Proposed and four-tested, not adopted: repairs R-b, R-c, R-d and R-e, each P P P P.

**Counterexamples.**
- To line 103's "an invertible covariant operator link with nontrivial continuous representation is impossible on a finite register": the invertible covariant link on `L²(K)` for a finite image `K` (`GA2_Y2.md` Theorem 2.3).
- To GAP S′'s claim that the draft's hypotheses do not supply the finite `sup Σ‖W‖`: Lemma S0 derives it from them.
- To "the area form can discard perimeter distinctions" at a fixed `p>1`: two perimeter laws with `μ₀≠μ₁` (Proposition A).
- To pass 1's "Creutz ratios avoid both" (draft line 425): two perimeter laws with `μ₀≠μ₁` have the same Creutz ratio `0` (Theorem 11).
- To the expectation that (d2) supplies the fermion's axial speeds through Lemmas S and S′ (draft line 383, conditional on gapped axial branches): the condition fails in the free massless walk, where the on-axis amplitude has, for some residue, no finite branch form (Lemma AX).
- The twist stays a counterexample, conditional on a charged band with scalar `V(K₀)`, to "invariant data fix whether `K₀` is a node". Under NN-a it relates two PS-1 updates; only one of them has the `L5-U` form that ZM1-I1 states (Proposition T).

**Open by name.** ZM1-I1[a], ZM1-I1[b], ZM1-I1[c], ZM1-I1[d], ZM1-I1[e] and the owner's selection; ZM1-OBS-twist; ZM1-OBS-d-lim; the relative and quantum-link forms of (c′); ZM1-i with GAP e-dynamics. Inherited and unchanged: Z2-spatial, ZM1-ii, ZM1-G, Y1, VC1, GA1-P, GA1-P-5, the rung rule, RCS-P, MT1-S[R-CS^str], R-CS. None was attacked here.

**What changes downstream.**
- The owner's ZM1-I1 choice: use §4's table. (a), (c), (d) and (e) keep their verdicts as written. (b)'s area and Creutz forms get the same test-3 verdict, and (b) passes test 2 with R-b; (c) passes test 2 with R-c and a fixed or universal list. The suggested order is (a), (c), (e), (b), (d), a judgment under a stated weighting.
- ZM1: every existential ZM1-I1[O], and the original ZM1-I1, is its `p=1` case. ZM1(a)1's "explicit `p >= 2`" needs a fixed `p`.
- LZ1-i: class (c) transfers speeds also for species whose composite weight vanishes at zero momentum (Theorems 8′, 9′). Class (d) does not supply a three-dimensional fermion cone through Theorems 8-9 in the free analogue, nor in the interacting case under Lemma AX's hypothesis. On odd bands the twist moves only flat nodes, which LZ1-SC's dispersion clause does not reach (§3.7).
- MT1-S[R-CS^str] and RCS-P: Theorem 12 forbids amplitudes between strings with different far ends. If a Lemma DL limit is the on-axis amplitude of a three-dimensional band with null transverse level sets, it has no finite branch form (Lemma AX), so Theorems 8-9 give no axial speed from it. Testing a three-direction cone with string data needs other data or a transfer theorem for phase continua.
- GA2, T0-start, T0-rate: unchanged. Class (a) stays a candidate operator-side interface; composing it with a continuum comparison still needs a dictionary and propagated errors.
- The law: under NN-a the matter-phase layer gives a PS-1 update with the same invariant data as the untwisted law (Proposition T(5)). Whether the five-mode law includes it is a law-specification choice for the owner.
- No law is eliminated. Both five-mode laws remain live. No axiom, working-set entry, reading, class or ranking is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
