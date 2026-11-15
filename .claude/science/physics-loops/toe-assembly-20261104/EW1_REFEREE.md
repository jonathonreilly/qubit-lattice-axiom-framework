lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# EW1 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (the referee) of part EW1 under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the lead freezes the part.

**What this file is.** One check of `EW1.md`: a whole-part, line-by-line read by a fresh session. It grants no status, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. This session wrote neither pass 1 (`EW1_DRAFT.md`) nor pass 2 (`EW1.md`). No review of this review was commissioned, and no other review was read.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max effort, headless, no subagents.

**Text read.** `EW1.md` at commit `e9e8234c1` on branch `claude/toe-assembly` (clean checkout; the last commit that touches the file). SHA-256 of the file read: `57a8bea50f7f0ea85712f487fb8ef2c4b0e6cff97b26fef3a24d8a57910d4cf3`. Line numbers below refer to that file.

**Sources read, with commits.** All at `e9e8234c1`, in `.claude/science/physics-loops/toe-assembly-20261104/` unless marked. No other branch was fetched or read.

| File | Lines read |
|---|---|
| `EW1.md` | 1-358 (all) |
| `EW1_DRAFT.md`, SHA-256 `4b79723b52842828130b016c085b7525ba6e89363e1b696423e357cbd0046555` (the hash `EW1.md` records) | 1-486 (all) |
| `LW1_REFEREE.md` | 1-80 (format only) |
| `Y2W_DRAFT.md` | 1-40 (head format only) |
| `TOE_ASSEMBLY.md` | 167-185 (§3.2, the four tests), 447-460 (EW1) |
| `CH1_5O.md` | 11-27, 34-40, 84-92, 132-151, 160-175 |
| `LW1_5.md` | 25-36, 76-98, 105, 123-131, 136, 142-148, 160-166, 217-233, 255-259, 295; heading list |
| `CH1_5OEP.md` | 17-66, 132-138, 191-201; heading list |
| `VC1_5.md` | 17-44, 59-80, 185-197; heading list |
| `GA2_Y2.md` | 62-66, 76-91, 115-128, 161 |
| `CH1_5OE.md` | 19 (inferred definition 3), with grep hits up to line 82 |
| `CH1.md` | 133 |
| repo root: `AGENTS.md`, `CLAUDE.md`, `docs/ai_methodology/SCIENCE_WORKFLOW.md` | all |

**Working set used, by name.** PS-5 (five modes per site), PS-6 and PS-6r (finite link registers), and PS-1 read by PS-1c (cell lifts), only through the two laws of frozen `LW1_5.md` §2 that `EW1.md` uses. No other entry is used. No axiom reading is attacked.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and the working set are read plainly. Readings proposed by `EW1.md` are checked for errors in their reasons, not attacked.

**Method.** Every proof step was re-derived by hand. Verdicts: CORRECT; ERROR (a false or inexact line, quoted or located, with the fix); INCOMPLETE (a named missing step, with its closure where one is given). A referee closure (R1-R8, §3) is a short complete argument written here; it is itself unrefereed. A `[check]` is a scratch computation in `/tmp/toe-ew1ref/` (`check_ref.py`, output `out2.txt`; about 15 s and 0.5 GB peak; 66 percent of memory free before each run). It guides and never proves. A first run scanned too narrow a range of normalizations and reported a one-link Λ² floor of 41.6; the optimum lay outside the range. The rerun on a log grid gives the values quoted below.

**Counts.** 116 items: 98 CORRECT, 16 ERROR, 2 INCOMPLETE. Two ERROR items change a statement: Theorem 6.3 and Lemma 6.4(3) are false as written and need the hypothesis (C). Every later use of them is in R-FMS states, which satisfy (C), so no conclusion of `EW1.md` changes except a constant. The other ERROR items are wording, convention or citation fixes.

**Decisions in one paragraph.** *Reverse transport ordering:* the distiller's counterexample is valid; the draft's general claim fails on `L5-U`. Theorem 5.3 never depended on it: for its data the draft's own reversal was exact (R1). The distiller's adjoint convention is correct. *Fixed-register quantifier:* the gap is real. The register is a free datum of one law (`LW1_5.md` line 97), and Theorem 5.3 picks `k` after `δ`. `EW1.md`'s restated Theorem 5.3 is the correct repair. The fixed-law question is open; §5 names it EW1-O[R] and records three failed attacks. *New:* Theorem 6.3 and Lemma 6.4(3) have a counterexample as stated (R4); adding (C) repairs both. Definition 2.4's general claim "`−1 ∉ H`" fails at `(a, b) = (4, 1)` (R7); nothing uses it outside the standard ratio. The vector-link GAP is repaired for every representation by Lemma 5.4′ (R2), still for one link only.

---

## 1. Verdict table

| # | Item (EW1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 "Proved" list (5) | ERROR | It lists Theorem 6.3 and Lemma 6.4 as proved. Theorem 6.3 and Lemma 6.4(3) are false as stated (items 83, 89; R4). Fix: edit E1. |
| 2 | GAP reverse transport ordering (7) | CORRECT | Real in general. Theorem 5.3 is untouched even under the draft's convention (§2 G1, R1). |
| 3 | GAP fixed law (7) | CORRECT | Real (§2 G2). |
| 4 | GAP vector-link scope (7) | CORRECT | Real. Repaired for every representation by Lemma 5.4′ (§2 G3, R2). |
| 5 | GAP thin-transport interpretation (7) | CORRECT | Real (§2 G4). |
| 6 | GAP neutral data (7) | CORRECT | Real for EW. The draft's sentence was about the full pattern; repaired statement R3 (§2 G5). |
| 7 | §0 "Open" list (9) | INCOMPLETE | The fixed-register question that the GAP paragraph calls open has no name. Carry it as EW1-O[R] (§5). |
| 8 | Provenance (11) | CORRECT | The recorded draft hash matches the file. |
| 9 | Literature scope (13) | CORRECT | The L-numbering matches `EW1_DRAFT.md` §1. No proof uses a citation. |
| 10 | Section numbering and heading (15-17, 19, 76, 101) | ERROR | "## 1" holds "### 2.1"-"### 2.5"; "## 2" follows; there is no "## 3". The definitions are the draft's §2 with one correction (Definition 2.3), not distiller inferences. Fix: edit E12. |
| 11 | §2.1 laws (21) | CORRECT | |
| 12 | Update of the law (23) | CORRECT | Matches `CH1_5OEP.md` inferred definition 5. |
| 13 | Definition 2.1 (25) | CORRECT | |
| 14 | Definition 2.2 (29) | CORRECT | |
| 15 | `p_sym` and its gauge invariance (31) | CORRECT | Read "G-invariant" for the action by which the coordinates `Φ^i` move, `w ↦ σ(g)^T w` (item 18, R8). All proofs use `\|w\|^2`, `\|w_r\|^2` or a real orthogonal `σ`, where both readings agree. |
| 16 | `σ(𝐔)` and central charge (35) | ERROR | On `L5-U` the rows of `𝐔` carry the dual of the creator representation `C^5`: `CH1_5OEP.md` R-U, "`c` conjugates `U^{jk}_ℓ = r^y_jr^{x†}_k` to `e^{−iθ}U^{jk}_ℓ`". With `V = C^5` the labels `V`, `V̄` are swapped and `q_r = p − p′` has the wrong sign. Only `\|q_r\|` and `q_r ≠ 0` are used. Fix: edit E4. |
| 17 | Definition 2.3, repaired (37) | CORRECT | Covariance and exact reversal re-derived (§2 G1). |
| 18 | Covariance paragraph (39) | ERROR | In Definition 2.2's index convention the row action is `σ(g)^T`, not `σ(g)`: on `L5-O`, `a_{y,g}(U^{ab}) = Σ_{a′}R(g)_{a′a}U^{a′b}` (from `LW1_5.md` "Q and G", lines 125-126, and the rule `a_{x,g}(γ_{x,a}) = Σ_bR(g)_{ba}γ_{x,b}` of EW1 line 151). The conclusions (fixed at interior sites, `𝒯Q_x` fixed at `x`) hold. Fix: edit E4. |
| 19 | `‖M‖_HS`, `M^†` (41) | CORRECT | |
| 20 | Definition 2.4, "`π\|_H` is injective because `−1 ∉ H`" (45) | ERROR | `CH1_5O.md` R4 proves `−1 ∉ H` for the standard embedding only. For `(a, b) = (4, 1)` (coprime, `a` even) `−1 ∈ H` (R7). Not load-bearing: every use is at the standard ratio. Fix: edit E3. |
| 21 | `K_em` and its computation (47) | CORRECT | |
| 22 | `c_F`, `Z_F` (49) | CORRECT | |
| 23 | Definition 2.5, R-FMS (53-66) | CORRECT | |
| 24 | Definition 2.6 and Q-EW (68-72) | CORRECT | With the identity update of `CH1_5OEP.md` Theorem 3, "stationary for an update" is vacuous; §5 records this. |
| 25 | Four-test quotation (78) | ERROR | Set in quotation marks but reworded. `TOE_ASSEMBLY.md` lines 173-176 read "1. It states or fixes something that a part lists as its target." and so on. `CH1_5O.md` line 164 quotes them exactly. Fix: edit E13. |
| 26 | R-VEV (80) | CORRECT | Quote matches `CH1_5O.md` line 38. |
| 27 | R-A and R-L (82) | ERROR | "Already rejected for EW1" is exact for R-A only. `CH1_5O.md` line 169 records R-L's tests 2 and 3 as failed by pass 1 and says "Rejecting this as a physical definition remains a proposed interpretation." Fix: edit E13. |
| 28 | R-ST (84) | CORRECT | An assessment; its literature context is not load-bearing. |
| 29 | R-SPEC (86) | CORRECT | |
| 30 | R-FMS tests 1-3 (89-91) | CORRECT | Assessments; no error in their reasons. |
| 31 | R-FMS test 4 (92) | CORRECT | Checked: for odd block averages `[Φ^i, Φ^j] = 2Φ^iΦ^j − \|X\|^{−2}Σ_x{ψ^i_x, ψ^j_x}`; the link-only `T := Φ_XΦ_Y^†/\|v\|^2` gives `TΦ_Y = Φ_X\|Φ_Y\|^2/\|v\|^2`. |
| 32 | Relation to R-E (93) | CORRECT | `CH1_5OE.md` line 19 defines the frozen relation `σ(U_{xy})φ_y = φ_x`. |
| 33 | EW instance (95) | CORRECT | |
| 34 | EW⁺ reading (97) | CORRECT | |
| 35 | Theorem 4.1 statement (105-108) | CORRECT | |
| 36 | Proof (1) on `L5-O` (110) | CORRECT | Uses only `κ_{−1} = id`, `κ_ϖ = Θ` (`CH1_5O.md` line 34) and carriage at `x`. The remark on `S_±^{⊗k}` is true and unused. |
| 37 | Proof (1) on `L5-U` (112) | CORRECT | Z-U quote matches `LW1_5.md` line 233; charge components keep commuting with every `Q_y`. |
| 38 | Proof (2) (114) | CORRECT | Quote matches `CH1_5O.md` line 132. |
| 39 | Proof (3) (116) | CORRECT | |
| 40 | Reading of Theorem 4.1 (118) | CORRECT | `3(B−L)` is odd on every Standard Model fermion with `ν^c` and even on bosons. |
| 41 | Lemma 4.2 statement (122) | CORRECT | |
| 42 | Lemma 4.2 proof on `L5-O` (124-126) | CORRECT | Commutant and its antisymmetric part re-derived. |
| 43 | Lemma 4.2 proof on `L5-U` (128) | CORRECT | |
| 44 | Lemma 4.2, dimension 10 (130) | CORRECT | The proof shows `⊇`; equality holds because `𝔥` meets the block-diagonal matrices on `C^3 ⊕ Ce_4 ⊕ Ce_5` in dimension 10. Only `≥ 10 > 9` is used. |
| 45 | Lemma 4.2, meaning (134) | CORRECT | |
| 46 | Proposition 4.3 setup (138-142) | CORRECT | |
| 47 | 4.3(1) and proof (145, 151) | CORRECT | `Γ^{abcd}` is Hermitian: reversal sign `(−1)^6`. |
| 48 | 4.3(2) and proof (146, 153) | CORRECT | Quote matches `LW1_5.md` line 148; the 256 monomials of degree 0, 2, 4 form a basis of `End(H_+)`; equivariance re-derived. |
| 49 | 4.3(3) and proof (147, 155-159) | CORRECT | Standard ratio; R4 of `CH1_5O.md` applies. |
| 50 | 4.3(4) and proof (148, 161) | CORRECT | `𝔭`-part and `u(5)`-part conditions re-derived. |
| 51 | 4.3(5) and proof (149, 163) | CORRECT | |
| 52 | Proposition 4.4 statement (169-171) | CORRECT | |
| 53 | 4.4 proof, weights (173-177) | CORRECT | Case analysis re-derived; monomials `c^†_Ic_J` are joint weight vectors. |
| 54 | 4.4 proof, `U(1)_λ ∩ H` (179) | CORRECT | At the standard ratio the intersection is `{1}`; `−1 ∈ U(1)_λ` but `−1 ∉ H`. |
| 55 | 4.4, meaning (183) | CORRECT | Proposition 4.4 constrains the representation that contains `v`, not how `Φ` is built (compare item 73). |
| 56 | Pass-1 `[check]` reports (132, 165, 181, 262) | CORRECT | Labelled as historical; not rerun here. |
| 57 | Register `R_k^-`, `c = k` (189) | CORRECT | `CH1_5OEP.md` O1 is a proposed normalization; using `c = k` as R-FMS data adopts nothing. |
| 58 | Lemma 5.1 and proof (191-193) | CORRECT | Counting re-derived: deviation `≤ 2C(d,2)/k`. |
| 59 | `Φ_prod` and `ω` (195) | CORRECT | |
| 60 | Lemma 5.2 statement (197) | CORRECT | |
| 61 | Lemma 5.2 proof: gauge invariance, stationarity (199) | CORRECT | Quotes match `CH1_5OEP.md` line 62. |
| 62 | Lemma 5.2 proof: cell lifts (201) | CORRECT | Quotes match `CH1_5OEP.md` lines 20, 39 and 60, `LW1_5.md` lines 162 and 257. The sign `σ_xσ_y` and its removal by `∏_{σ_x=−1}a_{x,ϖ}` re-derived. |
| 63 | Theorem 5.3 statement (203-208) | CORRECT | As restated by the distiller: varying register, not Q-EW for one law (§2 G2). |
| 64 | Step 0 (210) | INCOMPLETE | Linear independence must also exclude a cancelling scalar; closure R6. The reversal claim is exact under the repaired Definition 2.3, and was already exact under the draft's convention for these data (R1). |
| 65 | Step 1 (212-215) | CORRECT | Factorization over links and telescoping re-derived. |
| 66 | Step 2 setup, `Var ≤ 885/4` (217) | CORRECT | |
| 67 | Step 2 (A) (218) | CORRECT | `F^{cl} = 2Var/L^3`. |
| 68 | Step 2 (T) (219) | CORRECT | |
| 69 | Step 2 (C) (220) | CORRECT | `ρ^⊗(\|Σ_xC_x\|^2) ≤ 4L^3 + 4L^6 ≤ 8L^6`. |
| 70 | Step 2 (O) (221) | CORRECT | The commutator split `PΩ = ABΔ^iΩ + A[Δ^i, B]Ω` re-derived. |
| 71 | Step 3 (223) | CORRECT | `L` even gives `LZ^3 ⊆ 2Z^3`; finitely many conditions. |
| 72 | "Does not give": dynamics (226) | CORRECT | |
| 73 | "Does not give": the full pattern (227) | ERROR | "By Proposition 4.4 no state built from identical even site states and adjoint link values reaches EW⁺" misstates Proposition 4.4, which constrains the representation that contains `v`. Fix: edit E9. |
| 74 | "Does not give": the register (228) | ERROR | "Large `k` is not decoration (Lemma 5.4)" rests on vector transport, which Theorem 4.1 excludes from R-FMS data. Lemma 5.4′ (R2) bounds every representation, still for one link only. Fix: edit E9. |
| 75 | Lemma 5.4 and proof (230-232) | CORRECT | Quote matches `GA2_Y2.md` line 62. `10(s−1)^2 + 90s^2 = (10s − 1)^2 + 9`. |
| 76 | Lemma 5.4 scope (234) | CORRECT | Strengthened by R2. |
| 77 | `K_m` and end numbers (240) | CORRECT | |
| 78 | Lemma 6.1 and proof (242-244) | CORRECT | Square-zero bound rebuilt (R5). The attaining Slater state is at `m = 5` (`GA2_Y2.md` line 88); say so (edit E14). |
| 79 | Lemma 6.2 statement (246-250) | CORRECT | |
| 80 | Lemma 6.2 proof (252-260) | CORRECT | `⟨Y, T_adj(X)⟩ = −X̂_xŶ_y`, the Casimir values `24C(3,p−1)/C(5,p)` and the singlet attainment re-derived. |
| 81 | Remark after Lemma 6.2 (264) | CORRECT | |
| 82 | Lemma 6.3a and proof (266-271) | CORRECT | Quote matches `GA2_Y2.md` line 76. Its proof is rebuilt in R5. |
| 83 | Theorem 6.3 statement (273-276) | ERROR | False as stated: R4 gives a state and data with (O) and (A) at every `δ > 0` and no floor. Fix: add (C) for `X` and `Y`; the constant becomes `1 + √(dim W)/2 + c_Φ\|v\|` (R4, edit E2). |
| 84 | Theorem 6.3 proof, upper bound (278-283) | ERROR | "using (O) with `p_1 = \|·\|^2`" bounds `p_{1,sym}(Φ_X) = Σ_i(Φ^{i†}Φ^i + Φ^iΦ^{i†})/2`, not `\|Φ_X\|^2 = Σ_iΦ^{i†}Φ^i`. They differ by `½Σ_i[Φ^{i†}, Φ^i]`, which (C) controls. Fix: R4. |
| 85 | Theorem 6.3 proof, lower bound (285) | CORRECT | `[E_S, T_{XY}] = ±qT_{XY}` holds under either reversal convention. |
| 86 | Examples (287) | CORRECT | With the corrected constant: at `m = 5`, `n = 1`, `δ ≥ \|v\|^4/(4(1 + √5/2 + c_Φ\|v\|)^2)` for the `Λ^4C^5` datum. |
| 87 | Lemma 6.4(1) and proof (290, 294) | CORRECT | Quote matches `VC1_5.md` line 187. |
| 88 | Lemma 6.4(2) and proof (291, 294) | CORRECT | |
| 89 | Lemma 6.4(3) statement (292) | ERROR | False as stated: the R4 example has sharp `N_X = 0`, (O) and (A) at every `δ`, and `\|v\|^2 = 5/2`. Fix: add (C); the bound becomes `(s + √(dim W)/2)√δ + δ\|v\|^2` (R4, edit E2). |
| 90 | Lemma 6.4(3) proof (296) | ERROR | The cross-term argument is correct. The step "`ω(\|Φ_{X,r}\|^2) ≥ \|v_r\|^2 − √δ`, by (O)" needs (C), as in item 84. |
| 91 | Remark after Lemma 6.4 (298) | CORRECT | |
| 92 | Proposition 6.5(1) and proof (301, 304) | CORRECT | Given R4's corrected Lemma 6.4(3); "realized" means R-FMS, which includes (C). |
| 93 | Proposition 6.5(2) and proof (302, 306) | CORRECT | `Stab(w_n) = {diag(A, λ) : det A = λ^4}` and `Lie(K_n) ∩ 𝔥 = 𝔨_em` re-derived. |
| 94 | Paragraph after 6.5 (308) | CORRECT | The positive form for EW_grp and EW⁺ (R3) may be added (edit E8). |
| 95 | EW1-U statement (312) | CORRECT | |
| 96 | "Why stationarity is dropped" (314) | CORRECT | The quoted condition holds on `L5-U`: every gate commutes with every `𝒢^T_x` (`LW1_5.md` line 136, "U"), and B1-U (line 259) makes the tick cell covariant, so Theorem 3's proof applies verbatim. |
| 97 | EW1-U Attack A1 (316) | ERROR | "at most `2^{−N}`" holds for `c = 1`; for normalization `c` it is `(2c)^{−N}`. Fundamental transport is also excluded from R-FMS data by Theorem 4.1 (`σ(−1_5) = −1`). The failing step stands. Fix: edit E14. |
| 98 | EW1-U Attack A2 (318) | CORRECT | `GA2_Y2.md` line 161 states the same stopping point. |
| 99 | EW1-U Attack A3 (320) | ERROR | "they have definite end numbers on every link" is false for the family of `GA2_Y2.md` Theorem 4.3 with `2 ≤ m ≤ 6`, which antisymmetrizes an active rishon across three ends (line 120). The failing step stands. Fix: edit E14. |
| 100 | EW1-U closing (322) | CORRECT | |
| 101 | Remark 7.1 (328) | CORRECT | Quote matches `CH1_5OEP.md` line 136. |
| 102 | Lemma 7.2 statement (330) | CORRECT | |
| 103 | Lemma 7.2 proof (332) | CORRECT | Factorization and `M = σ_r(g)M` re-derived. The step "`≥ \|v_r\|^2 − √δ`" is valid because `τ` is tracial: `τ(\|Φ_{X,r}\|^2) = τ(p_{r,sym}(Φ_X))`. Cite that, not Lemma 6.4(3) (edit E11). |
| 104 | EW1-O[U_0] statement (334) | CORRECT | |
| 105 | Paragraph (336) | CORRECT | |
| 106 | EW1-O[U_0] Attack A1 (338) | CORRECT | With R2, one `S_+` link fails (T) in every admissible representation; the attack's last sentences stay true. |
| 107 | EW1-O[U_0] Attack A2 (340) | ERROR | E2b-5 (`LW1_5.md` line 295) gives "cell-translation and gauge-invariant" limit points, not "cell-symmetric". Full cell symmetry follows because the tick commutes with every lift (`CH1_5OEP.md` line 20), so each Cesàro mean is cell symmetric. The failing step stands. Fix: edit E14. |
| 108 | EW1-O[U_0] Attack A3 (342) | CORRECT | Quote of C4 matches `CH1_5OEP.md` line 132 in substance. |
| 109 | Closing (344) | CORRECT | |
| 110 | §8 item 1 (351) | CORRECT | Re-derived: `F = N_x(5−N_y)/5`, same-order reverse `N_y(5−N_x)/5`. `[check]` Part 4: they differ on the `m = 1` sector. |
| 111 | §8 item 2 (352) | CORRECT | |
| 112 | §8 item 3 (353) | CORRECT | |
| 113 | §8 item 4 (354) | CORRECT | |
| 114 | §8 item 5 (355) | CORRECT | |
| 115 | §8 item 6 (356) | CORRECT | |
| 116 | Closing statement (358) | CORRECT | |

---

## 2. The distiller's GAPs

### G1. Reverse transport ordering: real; Theorem 5.3 untouched

The draft's Definition 2.3 (`EW1_DRAFT.md` line 121) builds a reversed factor as a fresh evaluation at "its transpose-adjoint", and then says "Its reverse is `T^†`, the same combination over the reversed paths." That identity is false in general.

*The counterexample checks.* Take the trivial summand of `V ⊗ V̄` on an `L5-U` link, with unit invariant vector `Σ_je_j ⊗ e_j/√5`. The forward factor is `(1/5)Σ_{jk}U^{jk}(U^{jk})^† = (1/5)Σ_{jk}n^x_k(1 − n^y_j) = N_x(5 − N_y)/5`. The same-order evaluation at `𝐔^†` is `(1/5)Σ_{jk}(U^{kj})^†U^{kj} = N_y(5 − N_x)/5`. The forward factor is Hermitian, so it is its own adjoint. At `m = 1` and `(N_x, N_y) = (1, 0)` the two factors are `1` and `0`. `[check]` Part 4 agrees.

*The repair is correct.* The end actions act on entries by linear substitutions and commute with `†`. For an operator matrix `M` and a scalar matrix `S`, `(MS)^† = S^†M^†`. So if the forward factor obeys `a_{t,g}(σ(𝐔)) = ρ(g)σ(𝐔)` at its row end `t` and `a_{s,g}(σ(𝐔)) = σ(𝐔)ρ(g)^{−1}` at `s`, with `ρ(g)` unitary, then `a_{s,g}(σ(𝐔)^†) = ρ(g)σ(𝐔)^†` and `a_{t,g}(σ(𝐔)^†) = σ(𝐔)^†ρ(g)^{−1}`. The adjoint has its rows at the source end, as a reversed traversal needs. For operator matrices `((AB)^†)_{ij} = Σ_kB_{ki}^†A_{jk}^† = (B^†A^†)_{ij}`. So a reversed path transports by exactly `𝒯_π^†`, and with real weights `c_π` the reversed combination is `T^†`.

*Theorem 5.3 never used the false identity.* R1 (§3) proves that on `L5-O`, for the antisymmetrized bases of `Λ^2` and `Λ^4`, the same-order evaluation at `𝐔^T` equals the adjoint. So the draft's Step 0 sentence "for a reversed path `𝒯^† = 𝒯^T`, which is the transport of Definition 2.3 for the reversed path" (`EW1_DRAFT.md` line 294) was exact for its own data.

### G2. Fixed law: real

`LW1_5.md` line 97: "Free data are \(\varepsilon,\mu,\tau_E,\omega_0\), and \(R\) or \(m\), plus any future plaquette data." So `L5-O[R]` with one register `R` is one law. Q-EW (line 72) asks for states "stationary for an update of the law". Step 3 of Theorem 5.3 chooses `L` from `δ` ("Choose `L` even with every classical value at most `δ/2`") and then `k` from `L` ("Then choose `k` with every `C_F(L)/k ≤ δ/2`"). It proves `∀δ ∃L, k`. The draft's line 292 ("this answers Q-EW positively on `L5-O`") needs `∃R ∀δ`, which is not proved.

*Repaired statement.* `EW1.md` line 208, as written: the triple is fixed, the register may depend on `δ`, and the result holds across the family of laws `L5-O[R_k^-]`.

*The fixed-law question.* For every irreducible register and allowed constants, `CH1_5OEP.md` Theorem 3 makes the identity an allowed update ("The tick followed by \(W_E^{-1}\), \(M_o^{-1}\), then \(M_e^{-1}\) is an allowed update and is the identity"). Every state is stationary for it. So Q-EW for one fixed law is a kinematic question. It is open; §5 names it EW1-O[R] and records three failed attacks.

### G3. Vector-link scope: real; repaired for every representation

Theorem 4.1 gives `σ(ϖ) = 1` for every R-FMS representation, while `ϖ` acts on `V` by `−1`. So `V` is never an R-FMS representation, and Lemma 5.4 bounds no R-FMS transporter. R2 (§3, Lemma 5.4′) proves the one-link floor for every representation: `ω(‖σ(𝐔/c)^†σ(𝐔/c) − 1‖^2_HS) ≥ dim σ − 1` for each irreducible summand, every state and every `c > 0`. For `σ_Q = Λ^2 ⊕ Λ^4` the floor is `44 + 209 = 253`. The repair keeps the one-link scope. R-FMS transporters join block sites at distance `L ≥ 2`, and no floor for a product of two or more `S_+` links is on file.

### G4. Thin-transport interpretation: real

Theorem 6.3's floor contains `c_Φ = max(‖|Φ_X|^2‖, ‖|Φ_Y|^2‖)^{1/2}`, an operator norm. R-FMS controls second moments in the state, not operator norms. Along a family with `δ → 0`, `c_Φ` may grow, and the displayed floor may tend to zero. *Repaired statement* (with R4): a family of R-FMS states and data with a fixed cut size `n`, fixed `|q|`, fixed `|v|`, fixed `dim W` and `sup c_Φ < ∞` has
\[
\delta\ \ge\ \frac{|v|^4}{\big(1+\sqrt{\dim W}/2+\sup c_\Phi\,|v|\big)^2\,\lceil (n(K_m-1)+1)/|q|\rceil^2}
\]
for every member. `EW1.md` lines 287 and 354 say this in words, with the old constant.

### G5. Neutral data: real for EW; the draft meant the full pattern

The draft's sentence (`EW1_DRAFT.md` line 392) reads: "Full EW1 on `L5-U` needs a charged datum aligned through fat transporters (Theorem 6.3), in a state whose block matter numbers fluctuate." The draft uses "full EW1" for the full pattern: its line 451 says "Full EW1 on `L5-U` needs `U(1)_N` broken." Read as a claim about EW, the GAP is real: Proposition 6.5(2) gives a neutral orbit point with `Lie(K_n) ∩ 𝔥 = 𝔨_em`. Read as a claim about EW_grp or EW⁺, it is true in the form R3 (§3), except "fat transporters", which holds only in G4's sense.

---

## 3. Referee closures

Each closure below is written here in full. It is unrefereed.

### R1. Same-order reversal equals the adjoint on `L5-O` for reversal-symmetric bases

*Statement.* Let the entries `U^{ab}` be Hermitian (`L5-O`). Realize `σ ⊆ V^{⊗p}` by an orthonormal basis `(f_i)` of an invariant subspace. Let `R` reverse tensor factors: `(Rf)(k_1, …, k_p) := f(k_p, …, k_1)`. If `Rf_i = ζf_i` for every `i`, with `|ζ| = 1`, then the same-order evaluation `σ(𝐔^T)` equals `σ(𝐔)^†`.

*Proof.* Write `U^{KL} := U^{k_1l_1}⋯U^{k_pl_p}` in the fixed order. Hermitian entries give `(U^{KL})^† = U^{(RK)(RL)}`. Then
\[
(\sigma(\mathbf U)^\dagger)_{ij}=(\sigma(\mathbf U)_{ji})^\dagger=\sum_{K,L}f_j(K)\,\overline{f_i(L)}\,U^{(RK)(RL)}=\sum_{K,L}(Rf_j)(K)\,\overline{(Rf_i)(L)}\,U^{KL}=\sum_{K,L}f_j(K)\,\overline{f_i(L)}\,U^{KL},
\]
using the substitution `K → RK`, `L → RL` and `ζζ̄ = 1`. Since `((𝐔^T)^{⊗p})_{KL} = U^{l_1k_1}⋯U^{l_pk_p}`, renaming `K ↔ L` gives `σ(𝐔^T)_{ij} = Σ_{K,L}\overline{f_i(K)}U^{LK}f_j(L) = Σ_{K,L}f_j(K)\overline{f_i(L)}U^{KL}`. □

*Application.* The antisymmetrized basis `f_I := (p!)^{−1/2}Σ_{π∈S_p}sgn(π)e_{I∘π}` of `Λ^p` has `Rf_I = (−1)^{p(p−1)/2}f_I`. So for `σ_Q = Λ^2 ⊕ Λ^4` the draft's reversed factor `σ_Q(𝐔^T/k)` equals `σ_Q(𝐔/k)^†`, and Theorem 5.3's reversed transport is exactly `𝒯^†` under either convention. The hypothesis also holds whenever `σ` has multiplicity one in `V^{⊗p}`: the isotypic projection commutes with `R`, and `R` acts on its range as a scalar by Schur's lemma. On `L5-U` the entries are not Hermitian, and G1's example shows the identity fails. `[check]` Part 3 (an `so(6) ⊕ so(6)` analog on the half-spinor): zero difference for `V`, `Λ^2` and `Sym^2_0`.

### R2. Lemma 5.4′: one `S_+` link, every representation

*Statement.* On one `L5-O[S_+]` link, let `σ ⊆ V^{⊗p}` be irreducible of dimension `d`, realized by any orthonormal basis `(f_i)` of an invariant subspace, and put `T := σ(𝐔/c)` with `c > 0`. Then `‖T^†T − 1‖^2_HS ≥ (d − 1)·1` as an operator. Hence `ω(‖T^†T − 1‖^2_HS) ≥ d − 1` in every state. For `σ = ⊕_rσ_r` with one `c` the floor is `Σ_r(d_r − 1)`. The same floors hold for `‖TT^† − 1‖^2_HS`, by exchanging the ends.

*Proof.* (a) *Product form.* `U^{ab} = iη^y_aη^x_b`. Moving each `η^x` past the later `η^y` gives `U^{KL} = φ_pη^y_Kη^x_L`, with `η_K := η_{k_1}⋯η_{k_p}` and `φ_p := i^p(−1)^{p(p−1)/2}`. So `σ(𝐔)_{ij} = φ_pA_iB_j`, with `A_i := Σ_K\overline{f_i(K)}η^y_K` and `B_j := Σ_Lf_j(L)η^x_L`.

(b) *Invariants.* `𝒜 := Σ_iA_i^†A_i = Σ_{K,K′}(P_σ)_{KK′}(η^y_K)^†η^y_{K′}`, with `P_σ = Σ_if_if_i^*`. `P_σ` commutes with `R(g)^{⊗p}`, so `𝒜` is invariant under the `y`-end `Spin(10)`. `𝒜` is even in the `y`-Majoranas, so it preserves `y`-chirality. The two half-spin representations are irreducible and inequivalent, so by Schur's lemma `𝒜` acts as a scalar `λ_ε ≥ 0` on `y`-chirality `ε`. Likewise `ℬ := Σ_jB_jB_j^†` and `ℬ′ := Σ_jB_j^†B_j` act as scalars `μ_ε`, `μ′_ε` on `x`-chirality `ε`. (For odd `p` the `x`-words carry the sign of the `y`-chirality in the graded product; it cancels in every product used below.)

(c) *Computation.* `𝒜` is even in the `y`-Majoranas and commutes with every `B_j`, and no `B_j` changes `y`-chirality. So on `y`-chirality `ε`, `(T^†T)_{jj′} = c^{−2p}B_j^†𝒜B_{j′} = sB_j^†B_{j′}` with `s := c^{−2p}λ_ε`. Expanding,
\[
\|T^\dagger T-1\|^2_{HS}=\sum_{j,j'}\big(sB_{j'}^\dagger B_j-\delta_{jj'}\big)\big(sB_j^\dagger B_{j'}-\delta_{jj'}\big)=s^2\sum_{j'}B_{j'}^\dagger\mathcal B B_{j'}-2s\,\mathcal B'+d .
\]
Each `B_{j′}` maps `x`-chirality `ε′` to `ε′(−1)^p`. So on `S^y_ε ⊗ S^x_{ε′}` the operator is the scalar `s^2μ_{ε′(−1)^p}μ′_{ε′} − 2sμ′_{ε′} + d`.

(d) *Trace identity.* `B_j` maps the 16-dimensional `S^x_{ε′}` into the 16-dimensional `S^x_{ε′(−1)^p}`, so `tr_{S_{ε′}}(B_j^†B_j) = tr_{S_{ε′(−1)^p}}(B_jB_j^†)`. Summing over `j` gives `μ′_{ε′} = μ_{ε′(−1)^p} =: μ`. The operator is `(sμ − 1)^2 + d − 1 ≥ d − 1` on every summand. □

*Consequences.* For `p = 1` this is Lemma 5.4 (`d = 10`, floor 9). For `σ_Q` the floor is `44 + 209 = 253`. `Spin(10)` is connected and perfect, so it has no nontrivial one-dimensional representation; every nontrivial summand has `d_r ≥ 2`, and every R-FMS representation with a nontrivial summand has one-link floor at least 1. `[check]` Part 3 (`so(6) ⊕ so(6)` analog, log grid of `c`): minima 5.0004 for `V` (`d = 6`), 14.001 for `Λ^2` (`d = 15`), 20.000 for `Sym^2_0` (`d = 20`; there `T = 0` on spinors, since symmetric products of anticommuting Majoranas reduce to the trace), and 5.0002 for a multiplicity-two vector copy in `V^{⊗3}`. *Scope.* One link only.

### R3. What EW_grp and EW⁺ need on `L5-U` (repairs G5)

*Statement.* Take `L5-U[m]`, the standard ratio and R-FMS data with orbit point `v` and `K := Stab(v)`. (i) If `K ∩ H = K_em` (EW_grp) or `K = K_em·Z_F` (EW⁺), then `v_r ≠ 0` for some summand with `q_r ≠ 0`. (ii) If a fixed triple realizes EW_grp or EW⁺ for every `δ > 0`, then for all small `δ` no realizing state has sharp block matter numbers.

*Proof.* (i) Suppose every charged component vanishes. The centre acts on `σ_r` by `e^{iq_rθ}`, so the central `U(1)` fixes `v` and lies in `K`. Under EW_grp, `K ⊇ K ∩ H = K_em`, and Proposition 6.5(1) gives `K ∩ H ⊇ K_em·Z_5 ≠ K_em`, a contradiction. Under EW⁺, `i·1_5 ∈ K`, but every element of `K_em·{±1_5}` acts on `e_5` by `±1`, a contradiction. (ii) By (i), `Σ_{q_r≠0}|v_r|^2 > 0` for the fixed `v`. Lemma 6.4(3)′ (R4) bounds this sum by `(s + √(dim W)/2)√δ + δ|v|^2` in every state with sharp block matter numbers that satisfies (O), (C) and (A). The bound fails for small `δ`. □

EW at the Lie level is not covered: Proposition 6.5(2) gives a neutral orbit point. Whether alignment needs "fat" transport is decided only in G4's sense.

### R4. Counterexample to Theorem 6.3 and Lemma 6.4(3) as stated, and the corrected statements

*Counterexample.* Take `L5-U[m]`, any `m` and any constants. At each site `x` put `Φ^I_x := c_{x,i_1}c_{x,i_2}c_{x,i_3}c_{x,i_4}` for the five sets `I = {i_1 < i_2 < i_3 < i_4} ⊂ {1, …, 5}`. The entries are local, even and linearly independent. `U(5)_x` acts on them by `Λ^4` of the annihilator representation, which is irreducible and unitary in this basis, and the other local groups fix them. So `Φ_x` is a bosonic composite carried at `x`, with `|q| = 4` and `σ(−1_5) = 1`. `SU(5)` acts transitively on the spheres of this five-dimensional representation, so `{|w|^2}` generates the invariant polynomials. Fix `v` with `|v|^2 = 5/2`. Take any even `L`, `Φ_X := Φ_{x_X}`, transporters along straight paths in the four-fold tensor power, and `S` the one link that crosses the face, so `n = 1`. Let `φ` be the product state with empty matter at every site and the normalized trace on every link, and `ω := φ∘E`. It is gauge invariant (`E`), cell symmetric (the lifts of `VC1_5.md` Theorem 2.2 fix the matter vacuum and the trace), and stationary under the base tick (Lemma 6.4(1)-(2)). Every `N_X` is sharp at 0.
- (O): `p_{1,sym}(Φ_X) = ½Σ_I(Φ^{I†}Φ^I + Φ^IΦ^{I†})`. On the empty site `Φ^I|∅⟩ = 0` and `Φ^IΦ^{I†}|∅⟩ = |∅⟩`. So `p_{1,sym}(Φ_X)` acts as `5/2` on the support of `φ`, and `ω(|p_{1,sym}(Φ_X) − 5/2|^2) = 0`.
- (A): `Φ^I_X` and `Φ^J_Y` kill the empty sites, and link operators commute with matter. So every `(Φ_X − T_{XY}Φ_Y)^I` kills every vector in the support of `φ`, and `ω(|Φ_X − T_{XY}Φ_Y|^2) = 0` for both orders.

So (O) and (A) hold with every `δ > 0`. Lemma 6.4(3) as stated gives `5/2 ≤ √δ + (5/2)δ`, false for `δ ≤ 1/4`. Theorem 6.3 as stated gives `δ ≥ (25/4)/((1 + √5·√(5/2))^2⌈K_m/4⌉^2) > 0` (here `c_Φ = ‖Σ_IΦ^{I†}Φ^I‖^{1/2} = √5`), false for small `δ`. The state fails (C): `Σ_{I,J}ω(|[Φ^I, Φ^{J†}]|^2) ≥ Σ_I‖Φ^IΦ^{I†}|∅⟩‖^2 = 5`. `[check]` Part 1: `p_{1,sym}|∅⟩ = (5/2)|∅⟩`, `|Φ|^2|∅⟩ = 0`, (C) sum `= 5`, `‖Σ_IΦ^{I†}Φ^I‖ = 5`. The same example refutes the draft's versions, which have the same hypotheses.

*Theorem 6.3′ (corrected).* Keep the hypotheses of Theorem 6.3, and suppose `ω` satisfies (O), (C) and (A) for `(X, Y)` and `(Y, X)` with tolerance `δ`, with (C) for both `X` and `Y`. Then
\[
\delta\ \ge\ \frac{|v|^4}{\big(1+\sqrt{\dim W}/2+c_\Phi|v|\big)^2\,\lceil K_S/|q|\rceil^2}.
\]
*Proof.* Only the upper bound changes. `|Φ_X|^2 = p_{1,sym}(Φ_X) − ½Σ_i[Φ^i_X, Φ^{i†}_X]`, and `‖[Φ^i_X, Φ^{i†}_X]Ω‖^2 = ω(|[Φ^i_X, Φ^{i†}_X]|^2)` is a term of (C). Cauchy-Schwarz over the `dim W` indices gives `‖(|Φ_X|^2 − |v|^2)Ω‖ ≤ √δ + ½√(dim W)·√δ`. The same holds for `Y`. The rest of the proof is unchanged: `D ≤ 2δ(1 + √(dim W)/2 + c_Φ|v|)^2/|v|^4` and `D ≥ 2/⌈K_S/|q|⌉^2`. □

*Lemma 6.4(3)′ (corrected).* Let `ω` have sharp `N_X` for every block and satisfy (O), (C) and (A) with tolerance `δ`. Then `Σ_{r: q_r≠0}|v_r|^2 ≤ (s + √(dim W)/2)√δ + δ|v|^2`. Hence a fixed triple realized in such states for every `δ > 0` has `v_r = 0` whenever `q_r ≠ 0`.

*Proof.* The cross-term argument of `EW1.md` line 296 stands, so `Σ_{q_r≠0}ω(|Φ_{X,r}|^2) ≤ ω(|Φ_X − T_{XY}Φ_Y|^2) ≤ δ|v|^2`. For each charged `r`, `ω(|Φ_{X,r}|^2) = ω(p_{r,sym}(Φ_X)) − ½Σ_{i∈r}ω([Φ^i, Φ^{i†}])`. (O) and Cauchy-Schwarz give `ω(p_{r,sym}(Φ_X)) ≥ |v_r|^2 − √δ`. `|ω([Φ^i, Φ^{i†}])| ≤ ω(|[Φ^i, Φ^{i†}]|^2)^{1/2}`, and Cauchy-Schwarz with (C) bounds the sum of these over all charged indices by `√(dim W)·√δ`. Sum over the charged summands. □

Every use of Theorem 6.3 and Lemma 6.4(3) in `EW1.md` (Proposition 6.5(1), the paragraph at line 308, §6.6 Attack A2, Remark 7.1) concerns R-FMS states, which satisfy (C). Those conclusions stand; only the constants change.

### R5. Rebuilt inputs of Lemmas 6.1 and 6.3a

*(a) `GA2_Y2.md` Theorem 3.2* (line 76): "Let E be self-adjoint with spectrum in K consecutive integers and \([E,Y]=Y\). For every state and complex z, \[\omega((Y-z)^\dagger(Y-z)+(Y-z)(Y-z)^\dagger)\ge 2|z|^2/K^2.\]"

*Proof, rebuilt.* Shift `E` so its spectrum lies in `{0, …, K−1}`. By affinity in `ω` it suffices to take a vector state `ψ`. Let `P_j` be the spectral projections, `ψ_j := P_jψ`, `p_j := ‖ψ_j‖^2` and `B_j := P_{j+1}YP_j`; then `Y = Σ_jB_j`. The level-`(j+1)` component of `(Y − z)ψ` is `B_jψ_j − zψ_{j+1}`, and the level-`j` component of `(Y − z)^†ψ` is `B_j^†ψ_{j+1} − z̄ψ_j`, with `ψ_{−1} = ψ_K = 0`. Group the defect `D` by pairs `(j, j+1)`, `j = −1, …, K−1`. For one pair put `a := ‖ψ_j‖`, `b := ‖ψ_{j+1}‖` and `β := ⟨ψ̂_{j+1}, B_jψ̂_j⟩`. Projecting onto the unit vectors, the pair contributes at least `|aβ − zb|^2 + |bβ − za|^2`, which is at least `|z|^2(a^2 − b^2)^2/(a^2 + b^2)` (the squared distance in `C^2` from `z(b, a)` to the line `C(a, b)`). The bound also holds when `a` or `b` vanishes. Cauchy-Schwarz with `Σ_j(p_j + p_{j+1}) = 2` gives `D ≥ |z|^2 TV^2/2`, where `TV := Σ_j|p_{j+1} − p_j| ≥ 2max_jp_j ≥ 2/K`. So `D ≥ 2|z|^2/K^2`. □

*(b) The square-zero bound* (`GA2_Y2.md` line 90): for `X^2 = 0` and every state, `|ω(X)|^2 ≤ ω(X^†X + XX^†)/4`.

*Proof, rebuilt.* Take a vector state `ψ` and let `P` project onto the closure of `ran X`. `X^2 = 0` gives `XP = 0` and `(1 − P)X = 0`, so `X = PX(1 − P)` and `X^† = X^†P`. Hence `|⟨ψ, Xψ⟩| = |⟨Pψ, Xψ⟩| ≤ ‖Pψ‖‖Xψ‖` and `|⟨ψ, Xψ⟩| = |⟨X^†ψ, (1 − P)ψ⟩| ≤ ‖X^†ψ‖‖(1 − P)ψ‖`. With `x := |⟨ψ, Xψ⟩|`, `a := ‖Xψ‖`, `b := ‖X^†ψ‖` and `t := ‖Pψ‖^2`, this says `x^2 ≤ ta^2` and `x^2 ≤ (1 − t)b^2`. So `x^2 ≤ a^2b^2/(a^2 + b^2) ≤ (a^2 + b^2)/4`. Mixed states follow by convexity of `|ω(X)|^2` and affinity of the right side. □

### R6. Theorem 5.3, Step 0: linear independence

Suppose `Σ_iλ_iΦ^i_X = 0`. The term `x = x_X` has the empty path, so it is `L^{−3}A` with `A := Σ_iλ_iQ^i_{x_X}`, acting on the matter of `x_X`. Every other term is even and acts as the identity on the matter of `x_X`. So `A ⊗ 1 = −1 ⊗ B` for some `B`. Applying the normalized trace on the site `x_X` gives `B = −tr(A)·1`, so `A` is a scalar. The monomials of degree 0, 2 and 4 are linearly independent (`LW1_5.md` line 166: "all such monomials form a basis"), so `A = 0` and every `λ_i = 0`. □

### R7. `−1 ∈ H` at `(a, b) = (4, 1)`

`H` is generated by the images of `su(3)`, `su(2)` and `R·i diag(a,a,a,b,b)` (`CH1_5O.md` R3's proof, line 134). Take `(a, b) = (4, 1)`, coprime with `a` even. Let `h` be the product of the image of `−1_2 ∈ SU(2)` and `exp(πŶ)`, with `Ŷ` the image of `i diag(4,4,4,1,1)`. Then `π(h) = (1_3 ⊕ −1_2)(e^{4πi}1_3 ⊕ e^{iπ}1_2) = 1_5`, so `h = ±1`. Both factors are exponentials in the image of the diagonal torus, so `h` is the exponential of the image of `i diag(4π, 4π, 4π, 2π, 0)`. The site spin representation sends the image of `i diag(φ_1, …, φ_5)` to `∏_je^{iφ_j(n_j − 1/2)}`, because `n_j − 1/2 = M^{2j−1,2j}` (`LW1_5.md` line 31). Here this is `e^{−i(14π)/2} = −1`. The site representation sends `−1 ∈ Spin(10)` to `−1` (`LW1_5.md` line 162) and `+1` to `+1`. So `h = −1 ∈ H`, and `π|_H` is not injective. At the standard ratio the only such element is `+1` (`CH1_5O.md` R4). `[check]` Part 2 agrees on both counts. `EW1.md` uses injectivity only at the standard ratio (Proposition 4.3(3)), so no result changes.

### R8. Two conventions in §2.3

*(a) Transpose.* Definition 2.2 writes `a_{x,g}(Φ^i) = Σ_jσ(g)_{ji}Φ^j`: the column `(Φ^i)` is multiplied by `σ(g)^T`. On `L5-O` the row end of a link acts the same way: `a_{y,g}(U^{ab}) = Σ_{a′}R(g)_{a′a}U^{a′b}`, so `𝐔 ↦ R(g)^T𝐔`, and at the column end `𝐔 ↦ 𝐔R(g)`. Line 39 should read `a_{z_0,g}(𝒯_π) = σ(g)^T𝒯_π` and `a_{z_N,g}(𝒯_π) = 𝒯_π(σ(g)^T)^{−1}`. Then `𝒯Q_x` is fixed at `x` because `(σ(g)^T)^{−1}σ(g)^T = 1`. "G-invariant polynomials" (line 31) should be read for the action `w ↦ σ(g)^Tw` by which the coordinates move. For real orthogonal `σ`, and for `|w|^2` and `|w_r|^2`, the two readings agree; every proof in `EW1.md` uses only these cases.

*(b) Dual on `L5-U`.* `CH1_5OEP.md` R-U (line 201): "`c` conjugates `U^{jk}_ℓ = r^y_jr^{x†}_k` to `e^{−iθ}U^{jk}_ℓ`". Creators carry `e^{iθ}`. So the rows of `𝐔` carry the dual of the creator representation `V = C^5`, and `P_σ(𝐔^{⊗p} ⊗ 𝐔̄^{⊗p′})P_σ` transports data of central charge `p′ − p` in Definition 2.2's sense. Either define `V` as the representation on the rows of `𝐔`, or set `q_r := p′ − p`. Theorem 6.3, Lemma 6.4(3), Proposition 6.5 and Remark 7.1 use only `|q_r|` or `q_r ≠ 0`, so nothing changes.

---

## 4. Required edits

Each edit names the `EW1.md` lines it changes. None changes the statement of Theorem 4.1, Lemma 4.2, Propositions 4.3-4.4, Lemmas 5.1-5.2, Theorem 5.3's statement, Lemmas 5.4, 6.1, 6.2, 6.3a, 6.4(1)-(2), Proposition 6.5 or Lemma 7.2.

- **E1 (status; lines 5, 9).** In "Proved", replace "the graded floor and its conditional application (6.3a and 6.3), the sharp-matter and empty-sector results (6.4–6.5)" by "the graded floor (6.3a), the thin-transport floor with (C) (6.3′), the empty-sector and sharp-matter results (6.4(1)-(2), 6.4(3)′ with (C)) and the neutral-data result (6.5)". Add a GAP entry: "Theorem 6.3 and Lemma 6.4(3) as drafted omit (C); counterexample and correction in `EW1_REFEREE.md` R4." In "Open", add EW1-O[R] (§5 below).
- **E2 (Theorem 6.3 and Lemma 6.4(3); lines 273-287, 292, 296).** Replace both statements by Theorem 6.3′ and Lemma 6.4(3)′ of R4, insert R4's upper-bound step in place of "using (O) with `p_1 = |·|^2`", and use the constant `1 + √(dim W)/2 + c_Φ|v|` in the Examples paragraph.
- **E3 (Definition 2.4; line 45).** Replace "and `π|_H` is injective because `−1 ∉ H` (`CH1_5O.md` R4)" by "for the standard ratio `π|_H` is injective because `−1 ∉ H` (`CH1_5O.md` R4); at other ratios this can fail: `−1 ∈ H` at `(a, b) = (4, 1)` (`EW1_REFEREE.md` R7)".
- **E4 (§2.3; lines 31, 35, 39).** Add R8(a) and R8(b) as two short paragraphs, and write `σ(g)^T` in the covariance line.
- **E5 (Theorem 5.3, Step 0; line 210).** Add R6's argument for linear independence. Add: "Under the draft's convention the reversed factor was already `σ_Q(𝐔^T/k) = σ_Q(𝐔/k)^†` (`EW1_REFEREE.md` R1)."
- **E6 (fixed law; lines 7, 352).** Name the open fixed-register question EW1-O[R] and state it as in §5. Add: "For every irreducible register and allowed constants the identity update of `CH1_5OEP.md` Theorem 3 is allowed, so the question is kinematic."
- **E7 (vector-link scope; after line 234, and line 353).** Insert Lemma 5.4′ (R2) as a referee closure, with its one-link scope.
- **E8 (neutral data; after line 308, and line 7).** Insert R3 as the repaired form of the draft's sentence about the full pattern.
- **E9 (lines 227-228).** Replace "By Proposition 4.4 no state built from identical even site states and adjoint link values reaches EW⁺" by "By Proposition 4.4 no R-FMS datum whose orbit point lies in sums of even site-operator representations and `so(10)` satisfies EW⁺". Replace "Large `k` is not decoration (Lemma 5.4)" by "On `S_+` one link fails (T) in every representation with a nontrivial summand (Lemma 5.4′); transport over several `S_+` links is not bounded here."
- **E10 (thin transport; lines 287, 354).** State G4's repaired statement with the constant of Theorem 6.3′.
- **E11 (Lemma 7.2 proof; line 332).** Replace "As in Lemma 6.4(3), `τ(|Φ_{X,r} − T_rΦ_{Y,r}|^2) ≥ |v_r|^2 − √δ`" by "The cross term vanishes, and `τ` is tracial, so `τ(|Φ_{X,r} − T_rΦ_{Y,r}|^2) ≥ τ(|Φ_{X,r}|^2) = τ(p_{r,sym}(Φ_X)) ≥ |v_r|^2 − √δ` by (O)".
- **E12 (numbering; lines 15-19, 76, 101).** Rename "## 1. Definitions inferred by the distiller" to "## 2. Setting and definitions" and add: "These are the draft's §2 definitions; the distiller corrected Definition 2.3." Rename "## 2. Proposed readings ..." to "## 3. Proposed readings ...". The subsection and definition numbers 2.1-2.6 and §§4-8 then match.
- **E13 (quotations; lines 78, 82).** Quote `TOE_ASSEMBLY.md` lines 173-176 verbatim, as `CH1_5O.md` line 164 does. Replace the R-A and R-L sentence by: "Frozen `CH1_5O.md` (table, lines 166-171) records pass-1 assessments: R-A fails test 3 for EW1 and is rejected there; R-L fails tests 2 and 3, and 'Rejecting this as a physical definition remains a proposed interpretation.' Not revisited."
- **E14 (wording; lines 244, 316, 320, 340).** Line 244: "so the bound is attained" becomes "so the bound is attained at `m = 5`". Line 316: "at most `2^{−N}`" becomes "at most `(2c)^{−N}`", and add that fundamental transport is not admissible R-FMS data (Theorem 4.1), so the remark concerns one-link quality only. Line 320: "but they have definite end numbers on every link, so" becomes "but those of Theorem 4.4 and of the first family of Theorem 4.3 have definite end numbers on every link, so in them". Line 340: after the E2b-5 quote add "cell symmetry of the limit points follows because the tick commutes with every lift, so each Cesàro mean is cell symmetric".

---

## 5. Open statements to carry by name

- **EW1-U** (`EW1.md` line 312), unchanged. Its three attacks stand. A1 fails at "one `L5-U` link can be prepared with transport near a group element" (false by Lemmas 6.1-6.2). A2 fails at "every R-FMS alignment operator raises a bounded grading through a bounded cut" (false for neutral data; for charged data the floor of Theorem 6.3′ decays with the cut size). A3 fails at "such a state of `L5-U` is exhibited". E14 corrects two side remarks.
- **EW1-O[U_0]** (`EW1.md` line 334), unchanged. Its three attacks stand: A1 at "a known own-tick witness carries electroweak FMS data" (false for `τ` by Lemma 7.2, undecided for `ω_0` and `ω_F`), A2 at "time averaging preserves (O), (A) and (T)", A3 at HEAT and at the parity of FMS transport (Remark 7.1).
- **EW1-O[R]** (new name for the question G2 leaves open). Take the standard ratio. Are there an irreducible register `R` and a fixed triple `(W, σ, v)` with `Lie(Stab v) ∩ 𝔥 = 𝔨_em` such that for every `δ > 0` some symmetric state of `L5-O[R]` and some data `D` with this triple satisfy R-FMS(`Stab v; D, δ`)? Stationarity is omitted on purpose: for every irreducible register and allowed constants the identity update of `CH1_5OEP.md` Theorem 3 is allowed, and every state is stationary for it. So EW1-O[R] is Q-EW for one fixed law. A positive answer to EW1-O[U_0] with register `R` gives one here.
  - *Attack 1: Theorem 5.3 with `k` frozen.* Failing step: Step 3, "Then choose `k` with every `C_F(L)/k ≤ δ/2`". At a fixed `k` the bound `C_F(L)/k` is not shown small for the `L` that Step 2 needs, and no other bound on the link error is on file.
  - *Attack 2: refute on `S_+` by one-link floors.* R2 gives (T) at least 44 for one `S_+` link carrying any nontrivial admissible summand. Failing step: "an R-FMS block transporter is one link". `T_{XY}` joins block sites at distance `L ≥ 2` and may average many paths, and no floor for a product of two or more `S_+` links is on file.
  - *Attack 3: refute at fixed block size by finite dimension.* With `L` and `R` fixed, the block algebra is finite dimensional, and frozen `CH1_5O.md` Theorem 9 (line 92) says that "A nontrivial covariant multiplet cannot have all its entries and their adjoints mutually commuting." Failing step: "(C) at most `δ` for every `δ` forces commuting entries". (C) is a second moment in the state, not an operator identity, and nothing bounds `L` or the composites as `δ → 0`.
- **Inherited, unchanged:** EW1-i and the hierarchy `va`; CG1K-H; CG1-i; VC1; GA1-P-5; Y2-W; HEAT; the spectrum and the scalar channel.

## 6. Freeze recommendation

Freeze `EW1.md` after edits E1-E14. The edits are local. Only E2 changes statements: Theorem 6.3 and Lemma 6.4(3) gain the hypothesis (C) and a new constant. Every later use is in R-FMS states, which satisfy (C), so no conclusion of `EW1.md` changes except that constant. Theorem 5.3 stands as the distiller restated it: a varying-register construction in the update class. Closures R1-R8 are written in full above and may be imported as "referee closure, `EW1_REFEREE.md`", as earlier parts did. A second referee pass is not needed for the edits as written. Whether R2 and R4 get their own research gate is the lead's call.

---

## FINISH

**Proved** (referee closures, written in full in §3; unrefereed).
- R1: on `L5-O`, for a reversal-symmetric basis (the antisymmetrized basis of `Λ^p`, or any multiplicity-one `σ`), the same-order evaluation at `𝐔^T` equals the adjoint. Theorem 5.3's reversed transport was exact under both conventions.
- R2 (Lemma 5.4′): on one `L5-O[S_+]` link, for every irreducible `σ ⊆ V^{⊗p}` and every `c > 0`, `‖σ(𝐔/c)^†σ(𝐔/c) − 1‖^2_HS ≥ dim σ − 1` as an operator.
- R3: on `L5-U` at the standard ratio, EW_grp and EW⁺ need a charged component of the orbit point; for a fixed triple and every `δ`, the realizing states cannot have sharp block matter numbers.
- R4: Theorem 6.3′ and Lemma 6.4(3)′, the forms with (C).
- R5: `GA2_Y2.md` Theorem 3.2 and the square-zero bound, rebuilt.
- R6: linear independence in Theorem 5.3, Step 0.
- R7: `−1 ∈ H` at `(a, b) = (4, 1)`.
- Decisions: the distiller's counterexample to the draft's reverse ordering is valid, and the adjoint repair is correct. The fixed-register quantifier gap is real, and `EW1.md`'s restated Theorem 5.3 is the correct repair.

**Counterexamples.**
- Theorem 6.3 and Lemma 6.4(3) as stated in `EW1.md` and `EW1_DRAFT.md`: the empty-matter `Λ^4`-annihilator datum on `L5-U` satisfies (O) and (A) at every `δ > 0` and violates both conclusions. It fails (C) (R4).
- Definition 2.4's general clause "`π|_H` is injective because `−1 ∉ H`": false at `(a, b) = (4, 1)` (R7).
- The draft's same-order reverse convention on `L5-U`: the distiller's trivial-summand example, confirmed (G1).

**Open, by name.** EW1-U and EW1-O[U_0], each with the three named attacks of `EW1.md`. EW1-O[R], the fixed-register form of Q-EW, after three named attacks (§5): Theorem 5.3 with `k` frozen fails at Step 3's choice of `k` after `L`; one-link floors fail at "a block transporter is one link"; finite dimension fails at "(C) at most `δ` for every `δ` forces commuting entries". Inherited, unchanged: EW1-i and `va`; CG1K-H; CG1-i; VC1; GA1-P-5; Y2-W; HEAT; the spectrum and the scalar channel.

**What changes downstream.** Theorem 6.3 and Lemma 6.4(3) need (C); each use in R-FMS states stands with a new constant. The `L5-O` construction is a result across the family `L5-O[R_k^-]`; the fixed-law question is EW1-O[R]. On `S_+`, one link fails (T) in every representation with a nontrivial summand; transport over several links is still unbounded. On `L5-U`, EW_grp and EW⁺ need charged data and, for a fixed triple, fluctuating block matter. EW at the Lie level admits a neutral orbit point (Proposition 6.5(2)); whether it needs fluctuating block matter is not decided. No law is eliminated and no reading is adopted. The owner's decision to keep both laws live is untouched.
