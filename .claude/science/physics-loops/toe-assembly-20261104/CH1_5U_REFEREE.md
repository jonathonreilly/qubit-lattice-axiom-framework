lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1-5U-i referee report on `CH1_5U.md` (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (the referee) of `CH1_5U.md` under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen). This session wrote neither pass 1 (`CH1_5U_DRAFT.md`) nor pass 2 (`CH1_5U.md`). The session reports model id `claude-opus-5-5`; the effort is the one line 1 records. This is one check: one line-by-line read of `CH1_5U.md`. No other review was read for content, and no review of this review was commissioned.

**What this file is.** A referee report. It grants no status. It adopts no law, reading or definition, and it changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. No other file was edited. "[check]" marks a scratch computation in `/tmp/toe-ch15uref/` (`check_ref.py`, output `out.txt`; exact integer arithmetic except check (7), which is floating point; 0.45 s; 172 MB peak; started after `memory_pressure` showed 63 percent free). `scripts/lab_ops.py` is not in this sparse checkout, so its preflight did not run. A check guides and never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with its fix); INCOMPLETE (a named missing step, with what is missing). A referee closure (R0-R5, section 3) is a complete short argument written here. It is pass-3 work and is not itself refereed.

**Text refereed.** `CH1_5U.md` at commit `a5ddff4b0` (its only commit), 122 lines, SHA-256 `28e0c94570da35af4de6c15b78c97d482f2fba84e2f487c666ff2358aa485535`. Line numbers below refer to it. Its draft, `CH1_5U_DRAFT.md`, last changed at `ecb2036d9`, has SHA-256 `91430000d948742a9e833b1855ca02634fdcb7722dc9ae49df3c039a30bc07ae`, the hash `CH1_5U.md` line 11 records.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse) | `a5ddff4b0` |

No other branch was read. The draft's own source revision, `2d0adc0c0`, differs from `a5ddff4b0` only in files the draft did not read: `git diff 2d0adc0c0 a5ddff4b0` is empty on all eight folder files the draft cites. Files read at `a5ddff4b0`, by line. This folder: `CH1_5U.md` lines 1-122 (all); `CH1_5U_DRAFT.md` lines 1-289 (all); `LW1_REFEREE.md` lines 1-80 and its headings (format only); `CH1.md` (frozen; last changed `5ff19240c`; SHA-256 `7c71b87187c17d421bf27164452b18c3edecd6285929894c55de9599c7cd23a1`) lines 1-30 and 100-229; `GA2_Y2.md` (frozen; last changed `bf403a16a`) lines 1-12 (each cut at 600 characters) and 88 (Theorem 3.4); `CH1_5_DRAFT.md` lines 1-60 and 90-311; `LW1_5U_DRAFT.md` lines 1-130; `CG1_KILL_DRAFT.md` lines 178-200; `Y2W_DRAFT.md` lines 1-40, 100-132, 185-208; `LW1.md` lines 9-30 (the amendment format). By grep only, for names and the bridge Y2: `VC1_5.md` lines 11, 142, 221; `LW1_5X.md` lines 1, 5, 11, 104, 110; `TOE_ASSEMBLY.md` lines 136, 137, 305, 387, 389, 391, 395, 399, 410, 431, 540, 544-546, 548-556; `LIT_SMG.md` lines 3, 7, 9, 26, 30, 32, 34, 56, 62, 71, 86, 88, 90, 92, 97-99, 104, 106, 110, 124, 126, 134, 142, 166, 206, 210, 211, 213. Outside the folder: `AGENTS.md`, `CLAUDE.md`, `docs/ai_methodology/SCIENCE_WORKFLOW.md` (all). Greps for names and headings also printed the headings or single lines of `GA2_Y2_REFEREE.md`, `VC1_5_REFEREE.md`, `LW1U_SEA_REFEREE.md` and `TM1_REFEREE.md`; none of them was read further or used.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U`, CH1-5U-i and hypothesis IR are read plainly. One clause gets a named plain reading, in R2, and passes the four-test check there. R4's restatement of CH1-5U-q passes it too. Nothing is adopted.

**Working set used, by name.** PS-5 and PS-6 with PS-6r, only through the law `L5-U` as frozen `CH1.md` and `GA2_Y2.md` state it. PS-8, only as the gate kind CH1-5U-i (a) names. Results used, cited by line at the point of use: from frozen `CH1.md`, inferred definitions 6-9 (line 26 is IR), Lemma C2-5 (line 109), Lemma V (line 113), Theorem U-M (line 143), Theorem U-A (line 161), Corollary U-T″ (line 197), AM-5 (line 207) and the CH1-5U-i paragraph (line 225); from frozen `GA2_Y2.md`, Theorem 3.4 (W2, line 88); from `LW1_5U_DRAFT.md`, Lemma E (E1) and Lemma Z-U, as provisional inputs, as `CH1.md` uses them; from `CH1_5_DRAFT.md`, hypothesis IR (line 49) and section 5.1. PS-1 to PS-4, PS-7 and PS-9 to PS-11 are not used.

**Inputs from outside the working set.** *Standard mathematics, rebuilt in the text:* Schur's lemma for unitary representations; the continuous characters of `U(1)`; triviality of a continuous character of a connected Lie group with perfect Lie algebra; Wick's rule, taken as the definition of a quasi-free state; orthogonality of the ordered CAR product basis. *Standard mathematics cited, not rebuilt (only in R3, whose conclusion stays conditional):* S1 Pontryagin-Thom (Thom 1954); S2 the Thom isomorphism; S3 the Serre spectral sequence (Serre 1951); S4 the Hurewicz theorem modulo a Serre class (Serre 1953); S5 the Atiyah-Hirzebruch spectral sequence (Atiyah and Hirzebruch 1961); S6 `Ω^{Spin^c}_1 = Ω^{Spin^c}_5 = 0` (Stong 1968; Bahri and Gilkey 1987); S7 `Ω^{SO}_1 = Ω^{SO}_2 = Ω^{SO}_3 = 0`, `Ω^{SO}_5 = Z_2` (Thom 1954; Wall 1960); S8 `H^*(BU(5); Z) = Z[c_1, …, c_5]` and `H^*(BSU(5); Z) = Z[c_2, …, c_5]` (Borel 1953); S9 finite generation of `Ω_n` for a compact structure group; Wu's formula `w_3 = Sq^1w_2` on oriented manifolds. *Physics framework cited, never load-bearing:* the η-invariant form of the anomaly with its Atiyah-Patodi-Singer bordism invariance (Atiyah, Patodi and Singer 1975; Dai and Freed 1994; Witten 2016; Witten and Yonekura 2019); Witten's `SU(2)` anomaly (1982); the mod-16 anomaly (Tachikawa and Yonekura 2018; García-Etxebarria and Montero 2018; Hsieh 2018); the new `SU(2)` anomaly (Wang, Wen and Witten 2018); Wan and Wang's table for `Spin ×_{Z_2} Spin(10)`, only as `LIT_SMG.md` line 92 records it. No outside source was opened in this pass.

**Credits.** Pass 1 (Claude Opus 5.5, `CH1_5U_DRAFT.md`) found the covering description, the five anomaly computations, Lemma K, Lemma Q3 and the AHSS sketch that R3 completes. Pass 2 (Codex `gpt-6.1-terra`, `CH1_5U.md`) found the GAPs this report assesses. R1 extends pass 1's determinant argument of Lemma A4.

**Counts.** 57 items: 49 CORRECT, 2 ERROR, 6 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. Section 3 gives six referee closures, R0-R5.

---

## 1. Verdict table

| # | Item (`CH1_5U.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 "Proved in this item" (5) | CORRECT | Each listed result is proved in §§2-5 within its stated scope. R1 removes the restriction on the new-`SU(2)` result. |
| 2 | §0 GAP paragraph (7) | ERROR | Its sentence on CH1-5U-i ⇒ CH1-5U-q is false as written (2.1). Its other six sentences are accurate against the draft (section 4). |
| 3 | §0 Open by name (9) | INCOMPLETE | "The full global-anomaly calculation remains open here" carries no name (2.2). |
| 4 | §0 Provenance (11) | CORRECT | The draft hash matches. Two model reports (the lead's run log; the session) should be labelled as such (2.3). |
| 5 | Definition 1, centre and charges (15) | CORRECT | |
| 6 | Definition 2, `R_u`, `k`, `k'` (16-17) | CORRECT | `u − 2` odd gives `k` odd; `k' = −3k − 1` is even; charges `5k + 2 = u`, `5k' − 1 = −3u`, `5u`; smallest `|u|` is 3 at `k = −1` [check (0), (1)]. |
| 7 | Definition 2, `B_k` and the mirror (18) | CORRECT | `CH1.md` line 145, Theorem U-M (B): "`k'=-(1+3k),\quad k''=2+5k`". These are the line's twists, so the representation is `R_u`. The right-handed copy of `R_u` is the left-handed `R_u^*`. |
| 8 | Definition 3, `Ũ(5)`, `−1̃`, `S` (19) | CORRECT | `z^{−1}Γ(g)` is a representation; `−1̃` acts as `−1`. The naming is not used. |
| 9 | Definition 4, `K_d` (20) | CORRECT | `R_u` is a `K_d`-representation: `−1_5` acts as `(−1)^{charge} = −1`, all charges being odd. The caution is accurate. |
| 10 | Definition 5, the tests (21) | CORRECT | The degree-6 Weyl polynomial involves only `tr F^3` and `p_1 tr F`. |
| 11 | Definition 6, CH1-5U-i (22) | INCOMPLETE | Omits the update's `G_U` covariance and the state's `G_U` and gauge invariance (2.2). |
| 12 | Theorem 2.1: `Ũ(5)`, `σ`, `C` (26) | CORRECT | Kernel: `w^5 = 1`, `A = w^{−2}1_5`, `det A = w^{−10} = 1`. `C ≅ U(1)`: `w^2 = w^5 = 1` gives `w = w^5(w^2)^{−2} = 1`. |
| 13 | Theorem 2.1: every `ψ` is some `ψ_{a,b}` (28-29) | CORRECT | |
| 14 | Theorem 2.1: `a` odd, `b ≡ 3 mod 5`, onto, kernel `μ_{|b|}` (30) | CORRECT | `1 + 5a = 2b` even forces `a` odd; `2b ≡ 1` gives `b ≡ 3`; `gcd(2b, 5b) = |b|`, and `b ≠ 0`. |
| 15 | Theorem 2.1: `ψ_{a,b}^*S` and `ψ_{a,b}(−1_5)` (31) | CORRECT | Charges `2 + 5(2a − b) = −b`, `4 + 5(4a − b) = 3b`, `−5b`; `ψ(−1_5) = ((−1)^{1+5a}1_5, (−1)^{5b}) = (1_5, (−1)^b)` [check (1)]. |
| 16 | Theorem 2.1: `φ_u`, the line, no isomorphism, scalars (32) | CORRECT | `2u + 1 ≡ 0 mod 5`, so `a ∈ Z`; `b = −u` is odd. See 2.3 on `u = 1`. |
| 17 | Proof, first paragraph (34) | CORRECT | Sign flip `w ↦ −w` keeps `w^2` and changes `w^5`. |
| 18 | Proof, second paragraph (36) | INCOMPLETE | Two steps are compressed (2.2). R0 supplies both. |
| 19 | Proof, third paragraph (38) | CORRECT | The pieces equal those of `R_u`, not only up to isomorphism: `2a − b = k` and `4a − b + 1 = k'`. |
| 20 | Complex-conjugation remark (40) | CORRECT | `R_u^*` contains a `10bar`, so it is no `R_{u'}`. |
| 21 | Theorem 2.2 (42) | CORRECT | Scope: one-body modes of a number-conserving tick at a c-number background. |
| 22 | Proof of 2.2 (44) | CORRECT | |
| 23 | GAP Q1′ (46) | CORRECT | The gap is real. Its first clause, read as a target, is false: three particles of a quasi-free sea carry charge 3. R2 proves the form Attack 4 needs. |
| 24 | Theorem 3.1, statement (50) | CORRECT | `F_u[−s, −g] = [−s, −1̃φ_u(g)] = [s, φ_u(g)]`, so `F_u` is well defined; it lies over `SO(d)`. |
| 25 | Proof of 3.1 (52) | INCOMPLETE | "the same equivalence relation" is inexact; the map is missing (2.2). |
| 26 | Theorem 3.2, statement (54) | CORRECT | |
| 27 | Proof of 3.2 (56) | CORRECT | On `e_T ⊗ z^{−1}` the weight is `(i/2)Σ_lε_lx'_l` with `x'_l = x_l + aΣx`; a two-sign flip preserves `E` and negates each linear or cubic coefficient [check (2)]. |
| 28 | Second-derivation remark (58) | CORRECT | The cited indices are those of frozen `CH1.md` Theorem U-A's proof (line 167). |
| 29 | Theorem 3.3, statement (60-62) | CORRECT | |
| 30 | Proof of 3.3 (64) | CORRECT | `Σ_{i<j}(y_i + y_j)^2 = 4Σy^2 + 2Σ_{i<j}y_iy_j = 3Σy^2`. The twists `det^k` act trivially on `σ`'s image because `det∘σ = 1`; the proof uses this tacitly [check (4)]. |
| 31 | Theorem 3.4, statement (66) | CORRECT | |
| 32 | Proof of 3.4 (68-70) | CORRECT | `χ = (−1)^re_2 + e_1 + (−1)^r`, `e_2 = (t^2 − 5)/2`; the six values are `16, 0, 0, 0, 0, −16` [check (3)]. |
| 33 | Theorem 3.5, statement (72-74) | CORRECT | |
| 34 | Proof of 3.5 (76) | CORRECT | The kernel of `(A, λ) ↦ λA` is `{(ζ1_5, ζ^{−1}) : ζ^5 = 1}`; the two generators commute and the staged quotient is valid. |
| 35 | GAP A4 (78) | CORRECT | Real for the proof as written. R1 proves the first clause in full; the second clause is part of A5-glob. |
| 36 | Conditional Proposition 3.6, statement (80) | CORRECT | As a conditional. |
| 37 | Proof of 3.6 (82) | CORRECT | |
| 38 | GAP A5 (84) | ERROR | It quotes "all anomalies absent", a phrase the draft does not contain (2.1). The gap itself is real; R3 reduces it. |
| 39 | Theorem 4.1, statement (88-90) | CORRECT | |
| 40 | Proof of 4.1 (92) | CORRECT | The system `{α + 2β + γ, 2α − β − γ}` is unimodularly equivalent to `{3α + β, α + 2β + γ}`, so its kernel on the 3-torus is the connected circle `t(1, −3, 5)` [check (5), (6)]. |
| 41 | Scope remark and its GAP (94) | CORRECT | R5 states the restricted form that is proved. |
| 42 | Attacks 1-3 (96) | INCOMPLETE | Attack 3 fails "with AM-5"; "one-site composites" must name `c`, `ccc`, `c^5`; both points are frozen in `CH1.md` (2.2). |
| 43 | Attack 4 (98) | CORRECT | R2 sharpens its step (1). |
| 44 | Attack 5 (100) | CORRECT | Both of its "not checked here" inputs are frozen (2.3). |
| 45 | Attack 6 (102) | CORRECT | |
| 46 | CH1-5U-q (106) | INCOMPLETE | Missing the form clause and IR's charged-correlator prescription (2.2); R4 gives the statement. |
| 47 | GAP in the claimed implication (108) | CORRECT | Real only at the level of the statement; R4. |
| 48 | Theorem 5.1 (110) | CORRECT | [check (7)]. |
| 49 | Proof of 5.1 (112) | CORRECT | Irreducibility of each `Λ^k` is `LW1_5U_DRAFT.md` Lemma E (E1), a provisional input; its proof there is complete. |
| 50 | `V(N_x)` remark and the chain test (114) | CORRECT | |
| 51 | Reading (a), `K` (116) | CORRECT | |
| 52 | Reading (b), "type" (116) | CORRECT | |
| 53 | Reading (c), a second gauge group (116) | CORRECT | See 2.3 on test 3. |
| 54 | Reading (d), c-number links (116) | CORRECT | See 2.3 on test 3. |
| 55 | Reading (e), CH1-5U-q (116) | CORRECT | In R4's form it passes all four tests. |
| 56 | Check record (120) | CORRECT | The eight line values with `|u| ≤ 40` are `−33, −23, −13, −3, 7, 17, 27, 37`; `5` has seven `SU(2)` splittings. The referee's independent checks (1)-(7) agree. |
| 57 | Outside inputs and literature (122) | CORRECT | The two links were not opened here. `LIT_SMG.md` line 92 records Wan and Wang's `Z_2` (detected by `w_2w_3`) for `Spin ×_{Z_2} Spin(10)`; that supports the caution about the `Spin(10)` route (R3(d)). |

---

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 2 (line 7).** The line: "The draft's claimed implication CH1-5U-i ⇒ CH1-5U-q needs an extra local-operator and correlation hypothesis." It is false as written. Hypothesis IR of CH1-5U-i already supplies the operator and the correlations. `CH1_5_DRAFT.md` line 49: "quasi-local fermion-odd operators `ψ_i` whose large-separation correlations in `ω` agree with free Weyl fields of chiralities `χ_i`, all other connected correlations decaying exponentially. Here `ψ_i` spans an irreducible representation `R_i` of the group named." Frozen `CH1.md` line 26 states the same IR. A component of the light `10_u` is such an operator, of charge `u`. What CH1-5U-q lacks is IR's charged-correlator clause, which `CH1.md` line 26 names: "Charged correlators require a gauge-covariant dressing or a charge-sector prescription." That is a clause of the statement, not an extra hypothesis. `CH1_5U.md` line 108 itself says that IR "supports the intended implication". *Fix:* "The draft's implication CH1-5U-i ⇒ CH1-5U-q holds once CH1-5U-q is stated with IR's clause and the same charged-correlator prescription (`CH1_5U_REFEREE.md` R4)."

**Item 38 (line 84).** The line: 'The draft's unconditional verdict "all anomalies absent" is therefore not proved.' The quoted phrase does not occur in `CH1_5U_DRAFT.md`. The draft's unconditional lines are line 37, "The smallest statement that could refute CH1-5U-i outright, its anomaly, is decided: absent.", and line 278, "anomaly obstruction absent (section 3.7)". Its line 173 is conditional: "With the cited bordism fact, it carries none at all (Proposition A5)." *Fix:* 'The draft's unconditional lines 37 ("its anomaly, is decided: absent") and 278 ("anomaly obstruction absent") are therefore not proved. Its line 173 states the conclusion only "With the cited bordism fact".' The last sentence of the same paragraph should cite the frozen ledger. Frozen `CH1.md` Theorem U-M (line 143) classifies the small `U(5)` family multiplets under R-M, and Theorem U-A (line 165) says of its three `U(1)_N` coefficients: "They all vanish exactly on \((n_{10},n_{\bar5},n_1)=u(1,-3,5)\)." So the off-line anomaly is frozen within R-M, and "whose hypotheses are not re-proved here" can go.

### 2.2 INCOMPLETE

**Item 3 (line 9).** The open global-anomaly statement needs a name, so the frozen part can carry it. *Fix:* carry it as **A5-glob** (section 6), with R3's reduction.

**Item 11 (line 22).** Definition 6 omits two clauses of CH1-5U-i. The update is "covariant under `G_U`", and the state is "invariant under `G_U` and gauge transformations" (`CH1_5_DRAFT.md` lines 236-239, quoted at `CH1_5U_DRAFT.md` line 27). *Fix:* the amendment enters `CH1.md`, so quote its line 225 verbatim: "Find a covariant finite-depth \(L5\text{-U}\)-form gauge update and invariant stationary state whose IR is exactly one left-handed \(10_u\oplus\bar5_{-3u}\oplus1_{5u}\), with \(u=5k+2\), \(k\) odd, or its flipped assignment; keep \(U(5)\) as an operational massless long-distance group and gap the other odd excitations."

**Item 18 (line 36).** Two steps are compressed. (a) "Schur's lemma puts the image of scalars in `C`." Schur gives `ψ(λ1_5) = (μ1_5, z)` with `z^2 = μ^5`. One must still show that such a pair lies in `C`. (b) "Its differential is an isomorphism between 25-dimensional groups." One must say that a finite kernel makes the differential injective, and that `(g, z) ↦ g` is two-to-one, so `dim Ũ(5) = 25`. *Fix:* R0. It proves (a) and replaces (b) by a direct argument.

**Item 25 (line 52).** The line: "Both bundles are the quotient of P'×R by the same equivalence relation." The second bundle is a quotient of `(P' × K) × R`, not of `P' × R`. *Fix* (the draft's Lemma N proof, `CH1_5U_DRAFT.md` line 112): the map `[p', v] ↦ [[p', 1], v]` is well defined, because `(p'k', v)` and `(p', f(k')v)` both go to `[[p', f(k')], v] = [[p', 1], f(k')v]`. It is a linear bijection on each fibre. It intertwines the induced connections and Clifford actions, which come from the same frame bundle.

**Item 42 (line 96).** Three omissions. (a) Attack 3 fails at "Theorem U-A(iii) with AM-5" (`CH1_5U_DRAFT.md` line 179), not at U-A(iii) alone. (b) "one-site composites" must read "the one-site carriers `c`, `ccc`, `c^5`". Frozen `CH1.md` lines 197-201, Corollary U-T″, carry an anomaly-free line family at one site: "So an anomaly-free `U(5)` family is carried at one site exactly when `2 ≤ m ≤ 8`." U-A does not exclude that family. (c) The three failures are frozen. `CH1.md` line 225: "A free construction fails V; an elementary chiral \(5\) fails K1 at its endpoints and, conditionally, AM-5; the one-site family fails the U-A ledger under AM-5." *Fix:* cite that sentence in place of "These source-dependent findings are not re-established here", and add (a) and (b).

**Item 46 (line 106).** Two clauses are missing. The update must be "of `L5-U` form" as in CH1-5U-i (a), covariant under `G_U`, so that the implication from CH1-5U-i is literal. The correlation clause must be IR's, with its charged-correlator prescription (`CH1.md` line 26). *Fix:* R4's statement.

### 2.3 Notes on CORRECT items that bear on the freeze

- *Item 4.* The provenance gives the model twice: "Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high" and "actual model and reasoning effort are not exposed in this session". Both can stay if each is labelled by its source. The session id appears twice.
- *Item 16.* "in particular `u=1` cannot arise from such an isomorphism" is true and weaker than what holds. No `ψ_{a,b}` gives `u = 1`, since `b = −1 ≢ 3 mod 5`. And `R_1` is not a `U(5)`-representation, since `k = −1/5`.
- *Item 44.* Attack 5's two inputs are frozen. `GA2_Y2.md` line 88, Theorem 3.4 (W2): "On L5-U, \((U^{jk})^2=0\)". It takes one line: `(r^y_jr^{x†}_k)^2 = −(r^y_j)^2(r^{x†}_k)^2 = 0`, since distinct rishon modes anticommute and each squares to zero. `CH1.md` line 109, Lemma C2-5: "The ten distinct triple products cannot be ten independent CAR modes on a nonzero invariant subspace of the 32-dimensional matter site." So "the cited one-site composite CAR obstruction is not checked here" can cite C2-5.
- *Items 53-54.* The passes disagree on test 3 for readings (c) and (d). For (c), the distiller is right: adding a gauge group does not by itself gap the mirror. For (d), the distiller's doubt is also fair. `TOE_ASSEMBLY.md` line 556 states Y2 as "`S_fw` lies in the domain of the hard-core block RG (Balaban's class as rebuilt on the branch), or the hard core's bounds extend to `S_fw`. T0 is stated for the Wilson action." Group-valued links alone do not place an action in that class. Both rows stay rejected on tests 1 and 4, so no verdict depends on test 3. The disagreement is recorded, not resolved by vote.
- *Notation.* `σ` names the covering `SU(5) × U(1) → Ũ(5)` (Theorem 2.1) and also the maps `SU(2) → U(5)` (Theorems 3.3, 3.5). One of them should be renamed.

---

## 3. The distiller's GAPs, and referee closures

### 3.1 Is each GAP real?

| GAP (`CH1_5U.md` line) | Real? | Repair |
|---|---|---|
| §0: the all-anomaly claim rests on an unverified bordism computation and an anomaly-theory input (7) | Real | R3 reduces the bordism part to the cited standard theorems S1-S9. The anomaly-theory part is the η-invariant framework, cited. The conclusion stays conditional, as A5-glob. |
| §0: the sketch does not establish the localization equivalences (7) | Real | R3 (a) and (b) prove both, given S1-S9. |
| §0: the `Spin(10)` route needs a precise theorem (7) | Real | Not needed after R3. R3 (d) shows why the `w_2w_3` class of `Spin ×_{Z_2} Spin(10)` cannot reach `K`-manifolds. |
| §0: the named tests are not all anomalies (7) | Real | A5-glob, through R3. |
| §0: spacetime-symmetry anomalies are not analysed (7) | Real | Outside this item's question, which is the `U(5)` ledger. None here. |
| §0 and §5: CH1-5U-i ⇒ CH1-5U-q (7, 108) | Real only in the statement of CH1-5U-q | R4. |
| §0: the attacks fail in a narrower scope (7) | Real | Stated in §4 of `CH1_5U.md`. R2 and R5 sharpen Attacks 4 and 6. |
| Q1′ (46) | Real. Its first clause is false as a target. | R2 proves the quasi-free half in the form Attack 4 needs. The interacting half lies inside CH1-5U-q. |
| A4 (78) | Real for the proof as written | R1 excludes every structure map over `SO(d)`, `d ≥ 3`, so the first clause is proved. The second clause is part of A5-glob. |
| A5 (84) | Real | R3. |
| "no surviving symmetry has an anomaly" (94) | Real as the draft states it | R5 proves the restricted form. |

### 3.2 Referee closures

**R0 (Theorem 2.1: the scalar step and surjectivity, without Lie theory).** *Scalar step.* Let `ψ(λ1_5) = (μ1_5, z)` with `z^2 = μ^5`. Choose `w` with `w^2 = μ`. Then `(w^5)^2 = μ^5 = z^2`, so `w^5 = ±z`. Replacing `w` by `−w` keeps `w^2` and changes the sign of `w^5`. So `(μ1_5, z) = (w^21_5, w^5) ∈ C`. *Surjectivity.* Let `(g, z) ∈ Ũ(5)`. By the first part of Theorem 2.1, `(g, z) = (w^2A, w^5)` with `A ∈ SU(5)`, `w ∈ U(1)`. Since `b ≠ 0`, choose `λ ∈ U(1)` with `λ^b = w`. Then
\[
\psi_{a,b}(\lambda A)=\big(\lambda^{1+5a}A,\ \lambda^{5b}\big)=\big(\lambda^{2b}A,\ \lambda^{5b}\big)=(w^2A,\ w^5)=(g,z).
\]
∎ This uses only `det(λA) = λ^5` and `1 + 5a = 2b`.

**R1 (GAP A4: no structure map at all).** *Statement.* Let `d ≥ 3`. No continuous homomorphism `f: Spin(d) ×_{Z_2} SU(2) → K_d` satisfies `π_K∘f = π'`, where `π'[s, h] = π(s)` and `π_K[s, g] = π(s)` are the maps to `SO(d)`.

*Proof.* (1) `ker π_K = {[1, g] : g ∈ U(5)}`, because `[−1, g] = [1, −g]`. The map `j: g ↦ [1, g]` is an injective continuous homomorphism onto it: `[1, g] = [1, g']` forces `(1, g') = (1, g)`, since `(1, g') = (−1, −g)` is impossible. As `U(5)` is compact, `j` is a homeomorphism onto `ker π_K`. (2) `f[1, h]` lies in `ker π_K`, so `σ := j^{−1}∘f∘(h ↦ [1, h])` is a continuous homomorphism `SU(2) → U(5)`. (3) For `s ∈ Spin(d)`, `π_K(f[s, 1]) = π(s)`, so `f[s, 1] = [s', g]` with `s' = ±s`. As `[−s, g] = [s, −g]`, write `f[s, 1] = [s, τ(s)]`, with `τ(s)` unique, since `[s, g] = [s, g']` forces `g = g'`. `τ` is a homomorphism: `[ss', τ(ss')] = f[ss', 1] = [s, τ(s)][s', τ(s')] = [ss', τ(s)τ(s')]`. It is continuous, because `[1, τ(s)] = [s, 1]^{−1}f[s, 1]`. (4) In `Spin(d) ×_{Z_2} SU(2)`, `[−1, 1] = [1, −1]`. Applying `f`: `[−1, τ(−1)] = [1, σ(−1)]`, that is `[1, −τ(−1)] = [1, σ(−1)]`, so `σ(−1) = −τ(−1)`. (5) `det∘σ` and `det∘τ` are continuous characters of connected groups whose Lie algebras `su(2)` and `so(d)` are perfect for `d ≥ 3`. Their differentials vanish on `[𝔤, 𝔤] = 𝔤`, so both characters are trivial. Hence `1 = det σ(−1) = det(−τ(−1)) = (−1)^5 det τ(−1) = −1`, a contradiction. ∎

So no pullback test of the new-`SU(2)` type exists for `K_d`, with or without a spin component in the map. This is the proof of Theorem 3.5 with the Lorentz part allowed to twist.

**R2 (GAP Q1′: at a quasi-free point, a light field forces a light elementary field).** *Setting.* The matter CAR algebra of the modes `c_{x,j}`, `x ∈ Z^3`, `j = 1, …, 5`, at a c-number background, as in Theorem 2.2. A state `ω` is *number-conserving quasi-free* when, for `b_1, …, b_n ∈ {c_{x,j}, c^†_{x,j}}`, `ω(b_1⋯b_n) = 0` for odd `n` and, for even `n`, `ω(b_1⋯b_n) = Σ_π sgn(π)∏_{(i<j)∈π}ω(b_ib_j)` over the perfect matchings `π` of `{1, …, n}`, with `ω(cc) = ω(c^†c^†) = 0`. Put `G_{xi,yj} = ω(c^†_{x,i}c_{y,j})`.

*(i) Statement.* Let `A = b_1⋯b_{n_A}` have all factors at sites of a finite set `X`, and `B = b_{n_A+1}⋯b_n` all factors at sites of a finite set `Y`, with `X ∩ Y = ∅`. If `|G_{xi,yj}| ≤ Ce^{−μ|x−y|}` for all `x ≠ y`, then
\[
|\omega(AB)-\omega(A)\omega(B)|\le (n-1)!!\;C\,e^{-\mu\,d(X,Y)} .
\]
*Proof.* Expand `ω(AB)` by the matching rule. A matching with no chord between `{1, …, n_A}` and `{n_A + 1, …, n}` is a pair `(π_A, π_B)`, and `sgn π = sgn π_A · sgn π_B`, because no chord inside the first block crosses a chord inside the second. These terms sum to `ω(A)ω(B)`. Every other matching has a chord `(i, j)` with `b_i` at `x ∈ X` and `b_j` at `y ∈ Y`. Since `x ≠ y`, `ω(b_ib_j)` is `0`, `G_{xi,yj}` or `−G_{yj,xi}` (from `ω(c_{x,i}c^†_{y,j}) = −ω(c^†_{y,j}c_{x,i})`). So its modulus is at most `Ce^{−μd(X,Y)}`. Every two-point value has modulus at most 1, since `‖b‖ = 1`. There are `(n − 1)!!` matchings. ∎

*(ii) Statement.* Let `ψ` be fermion odd, of `U(1)_N` charge `q ≠ 0`, and quasi-local in the usual exponential sense (IR fixes no rate): `‖ψ − ψ_R‖ ≤ C'e^{−κR}`, with `ψ_R` in the algebra of the modes within distance `R` of the origin. Let `ψ_x` be its translate. If `G` obeys the bound of (i), then `ω(ψ_xψ_y^†)` decays faster than every power of `|x − y|`.

*Proof.* Replacing `ψ_R` by its charge-`q` part, `(2π)^{−1}∫e^{−iqθ}e^{iθN}ψ_Re^{−iθN}dθ`, keeps it in the same algebra and does not increase `‖ψ − ψ_R‖`. So take `ψ_R` of charge `q`. Then `ω(ψ_{R,x}) = 0`, because a number-conserving quasi-free state is `U(1)_N` invariant. Put `d = |x − y|` and `R = d^{1/4}`, and take `d` so large that `‖ψ_R‖ ≤ 2‖ψ‖`. The truncation changes `ω(ψ_xψ_y^†)` by at most `‖ψ − ψ_R‖(‖ψ‖ + ‖ψ_R‖) ≤ 3‖ψ‖C'e^{−κR}`. `ψ_R` lies in the algebra of `M ≤ 5(2R + 1)^3` modes. The ordered products of `{1, c_k, c^†_k, 2c^†_kc_k − 1}` form a basis of that algebra. It is orthogonal for `⟨X, Y⟩ = 2^{−M}tr(X^†Y)`, with squared norms at least `2^{−M}`: in Majorana form the four factors are `1`, `(γ ± iγ')/2` and `±iγγ'`, and Majorana monomials are orthonormal. So each coefficient of `ψ_R` has modulus at most `2^{M/2}‖ψ_R‖`, since `‖X‖_2 ≤ ‖X‖`. Expanding each `2c^†c − 1` writes `ψ_R` as at most `8^M` products of at most `2M` operators `b`, with coefficients of modulus at most `2^{3M/2}‖ψ_R‖`. By (i), applied to each pair of products, whose supports lie at distance at least `d − 2R`,
\[
|\omega(\psi_{R,x}\psi_{R,y}^\dagger)|\le 64^M\,2^{3M}\,(2\|\psi\|)^2\,(4M-1)!!\;C\,e^{-\mu(d-2R)}=\exp\!\big(O(d^{3/4}\log d)-\mu d\big).
\]
Both contributions decay faster than every power of `d`. ∎

*(iii) Consequences.* The equal-time two-point function of a free Weyl field decays as a power of the separation. So, at a number-conserving quasi-free point:
- if `G` decays exponentially, no quasi-local fermion-odd operator of any charge has free-Weyl large-separation correlations;
- hence, if some field of charge `|q| ≥ 3` has free-Weyl correlations there, `G` does not decay exponentially. Then the elementary field of charge `±1` is not gapped, and the light content is never exactly `R_u ⊕ R_u^*`. This is the step Attack 4 (line 98) needs, now with composites included.

*A reading, used only here.* CH1-5U-i asks that "every other fermion-odd excitation" be gapped. At a quasi-free point, read this to include the elementary `c_{x,j}`: their connected correlations decay exponentially, as IR's clause "all other connected correlations decaying exponentially" (`CH1_5_DRAFT.md` line 49) says for operators outside the family fields. Under this reading, (iii) shows that no number-conserving quasi-free state at a c-number background has the light content CH1-5U-i asks for. Four-test check. (1) It fixes no part's target; it reads a clause of CH1-5U-i as worded. (2) It is closed: one clause, one class of operators. (3) It settles nothing by premise: the quasi-free conclusion is derived, and frozen Lemma V (`CH1.md` line 113) already excludes the free route by another argument. (4) It adds no structure or constant. Pass. Not adopted.

*What R2 does not reach.* An interacting law can have light composites of charge `|q| ≥ 3` without a light elementary field. That case is CH1-5U-q.

**R3 (GAP A5: `Ω_5^{K} = 0` from named standard theorems).** Write `K` for the stable form of `K_d`. The inputs S1-S9 are listed in the head; they are cited, not rebuilt. R3 completes pass 1's sketch (`CH1_5U_DRAFT.md` line 167).

*(a) At the prime 2.* The homomorphism `q: Spin^c(d) × SU(5) → K_d`, `([s, λ], A) ↦ [s, λA]`, is well defined (`([−s, −λ], A) ↦ [−s, −λA] = [s, λA]`), lies over `SO(d)`, is onto, and has kernel `{([1, ζ], ζ^{−1}1_5) : ζ^5 = 1} ≅ Z_5`. That is Theorem 3.5's isomorphism. `Bq` is a fibration with fibre `BZ_5`, over the simply connected `BK` (`K` is connected). The reduced homology of `BZ_5` with `Z_{(2)}` coefficients vanishes, so the Serre spectral sequence (S3) makes `Bq` a `Z_{(2)}`-homology isomorphism. Both Thom spectra are built from the same oriented bundle pulled back from `BSO`. The Thom isomorphism (S2) and S4 then give `Ω_5^K ⊗ Z_{(2)} ≅ Ω_5^{Spin^c × SU(5)} ⊗ Z_{(2)} = Ω_5^{Spin^c}(BSU(5)) ⊗ Z_{(2)}`, by S1. In the AHSS (S5), `E^2_{p,5−p} = H_p(BSU(5); Ω^{Spin^c}_{5−p})`. `SU(5)` is 2-connected, so `BSU(5)` is 3-connected and `H_p(BSU(5); A) = 0` for `p = 1, 2, 3` and every `A`. `H_5(BSU(5); Z) = 0` by S8 and universal coefficients (`H^5 = 0`, and `H^6 = Z c_3` is torsion free). The two remaining entries carry `Ω^{Spin^c}_1 = 0` (at `p = 4`) and `Ω^{Spin^c}_5 = 0` (at `p = 0`), by S6. So the whole line `p + q = 5` vanishes at `E^2`, and `Ω_5^K ⊗ Z_{(2)} = 0`.

*(b) At an odd prime p.* Put `P = U(5)/{±1_5}`. The maps `K_d → SO(d) × P`, `[s, g] ↦ (π(s), [g])`, and `SO(d) × U(5) → SO(d) × P` are onto, lie over `SO(d)`, and have kernel `Z_2`. Their fibres `BZ_2` have vanishing reduced `Z_{(p)}`-homology, and the base is simply connected. So, as in (a), `Ω_5^K ⊗ Z_{(p)} ≅ Ω_5^{SO}(BU(5)) ⊗ Z_{(p)}`. In its AHSS, `H_{odd}(BU(5); A) = 0` for every `A` by S8 (cohomology free and in even degrees), so the entries at `p' = 1, 3, 5` vanish. The entries at `p' = 4, 2` carry `Ω^{SO}_1 = 0` and `Ω^{SO}_3 = 0`, and the entry at `p' = 0` is `Ω^{SO}_5 ⊗ Z_{(p)} = Z_2 ⊗ Z_{(p)} = 0` (S7). So `Ω_5^K ⊗ Z_{(p)} = 0`.

*(c) Conclusion.* `Ω_5^K` is finitely generated (S9). A finitely generated abelian group that vanishes after tensoring with `Z_{(p)}` for every prime `p` is zero. So `Ω_5^K = 0`, given S1-S9.

*(d) Why the `Spin(10)` class does not reach `K`.* `LIT_SMG.md` line 92 records Wan and Wang: "Table 25 gives `Z2`, detected by `w2 w3`, for `Spin ×_{Z2} Spin(10)`." The homomorphism `K_d → Spin^c(d)`, `[s, g] ↦ [s, det g]`, is well defined, since `det(−1_5) = −1`. So every `K`-manifold is `Spin^c`: `w_2` is the reduction of an integral class, `W_3 = 0`, and `w_3 = Sq^1w_2 = 0` on an oriented manifold (Wu). Hence `w_2w_3 = 0` on every `K`-manifold. Any anomaly of the 16 on that `Z_2` pulls back along `F_u` (composed with `Ũ(5) ⊂ Spin(10)`) to zero. This agrees with (c). The vanishing of `w_2w_3` on `K`-manifolds does not depend on Wan and Wang.

*(e) What stays conditional.* Proposition 3.6 also needs its second hypothesis: once the degree-6 polynomial vanishes, the anomaly of a `K`-Weyl content is a homomorphism `Ω_5^K → U(1)`. Under the η-invariant definition of the anomaly, this follows from the Atiyah-Patodi-Singer theorem: on `Y = ∂Z`, `exp(2πiη(Y)) = exp(2πi∫_ZI_6) = 1`. That framework is cited. So A5-glob holds given S1-S9 and the framework, and neither is rebuilt here.

**R4 (the implication CH1-5U-i ⇒ CH1-5U-q).** *Statement of CH1-5U-q.* Fix a charged-correlator prescription `𝒫` in the sense of `CH1.md` line 26. CH1-5U-q[`𝒫`]: there exist (a) an update `U` of `L5-U` form as in CH1-5U-i (a), covariant under `G_U`, and (b) a state `ω`, stationary under `U` and invariant under `G_U` and gauge transformations, such that hypothesis IR, with prescription `𝒫`, holds for at least one quasi-local fermion-odd operator `ψ` of definite `U(1)_N` charge `q`, `|q| ≥ 3`: its large-separation correlations in `ω` agree with those of a free Weyl field.

*Claim.* For every `𝒫`, CH1-5U-i[`𝒫`] implies CH1-5U-q[`𝒫`].

*Proof.* CH1-5U-i[`𝒫`] supplies `U` and `ω` with clauses (a) and (b), and IR fields spanning the `10_u`. Each component has fermion parity odd and `U(1)_N` charge `u`, with `|u| ≥ 3` (Theorem 2.2). Its correlations are free-Weyl under `𝒫`. ∎ So a proof of ¬CH1-5U-q[`𝒫`] refutes CH1-5U-i[`𝒫`].

*Four-test check.* (1) It fixes no part's target: it is a consequence of CH1-5U-i, posed as an open question. (2) It is closed: every clause is quoted from CH1-5U-i and IR, and `𝒫` is a parameter left open, not filled. (3) No downstream question is assumed. (4) It removes clauses and adds none. Pass. Not adopted.

**R5 (GAP on line 94: the restricted statement that is proved).** Let `Φ` be a unitary linear map of the mirror's left-handed fields `(A, B, C)` that commutes with `U(5)` and fixes `O_2` and `O_3`. By Theorem 4.1, `Φ` lies in the image of `U(1)_N ⊂ U(5)`. On that image, every perturbative anomaly vanishes (Theorem 3.2), the Witten and mod-16 tests vanish (Theorems 3.3, 3.4), and no new-`SU(2)` test exists (R1). So no symmetry of this class carries an anomaly of these types; with A5-glob, none of any type. Antiunitary, spacetime, nonlinear and higher-form symmetries stay outside, as line 94 says.

---

## 4. `CH1_5U.md` checked against `CH1_5U_DRAFT.md` where it cites it

| `CH1_5U.md` line | What it reports of the draft | Draft line | Verdict |
|---|---|---|---|
| 7 | The all-anomaly claim uses a cited bordism fact and a cited anomaly framework | 159-169, 173 | Accurate |
| 7 | The sketch does not prove the localization steps | 167 | Accurate |
| 7 | The `Spin(10)` route needs a precise theorem | 169 | Accurate |
| 7 | The implication needs an extra hypothesis | 232 | Inaccurate (item 2) |
| 11 | Draft SHA-256; draft source revision `2d0adc0c0` | 13 | Accurate; hash recomputed |
| 20 | The draft cites Lemma Z-U for `−1_5` as fermion parity | 58 | Accurate |
| 22 | `L5-U`, `G_U`, IR and PS-8 as in pass 1's sources | 19, 27 | Accurate; two clauses omitted (item 11) |
| 58 | The inputs of the second derivation | 121 | Accurate |
| 84 | The AHSS sketch asserts the 2-local and odd-local steps without proof | 167 | Accurate |
| 84 | 'unconditional verdict "all anomalies absent"' | 37, 173, 278 | Inexact quotation (item 38) |
| 94 | '"no surviving symmetry has an anomaly"' | 216 | Accurate; the draft's sentence ends "to match" |
| 96 | Attacks 1-3 fail at V, K1-5/K2-5 with AM-5, and U-A(iii) | 179, 224 | Omits "with AM-5" for Attack 3 (item 42) |
| 98 | Attack 4: pullback of interactions, quasi-free start, added gauge group | 200-204 | Accurate; the narrower scope is right |
| 100 | Attack 5: W2, multiplicative state, Euclidean kernel, CAR obstruction, c-number links | 208-210 | Accurate |
| 102 | Attack 6: Lemma K, Lemma Q1, the dressed propagator | 214-220 | Accurate; the narrower scope is right |
| 108 | Pass 1 gives no charged-correlator prescription in CH1-5U-q | 230-232 | Accurate |
| 114 | The draft's claims on the chain test | 240 | Accurate |
| 116 | Pass 1's four-test results for rows (a)-(e) | 248-254 | Accurate, test by test |
| 120 | Check list (1)-(8) | 92, 123, 133, 147, 196 | Accurate |
| 122 | Outside results the draft credits | 21 | Accurate. The draft also credits Dai and Freed, Freed and Hopkins, Witten and Yonekura, and Wang, Wen and Witten. |

---

## 5. Required edits to `CH1_5U.md`

The distiller or the lead applies these at the freeze. None changes a theorem.

1. Line 7: replace the sentence on the implication by item 2's fix.
2. Line 84: replace the quotation "all anomalies absent" by item 38's fix. In its last sentence, cite frozen `CH1.md` Theorems U-M (line 143) and U-A (line 165) for the off-line anomaly.
3. Line 9: name the open global-anomaly statement **A5-glob** and add **CH1-5U-q[𝒫]** in R4's form (section 6).
4. Line 11: label the two model reports by their sources; give the session id once.
5. Line 22: replace Definition 6's summary of CH1-5U-i by `CH1.md` line 225 verbatim (item 11).
6. Line 36: insert R0's scalar step and its direct surjectivity proof (item 18).
7. Line 52: replace "Both bundles are the quotient of P'×R by the same equivalence relation" by the explicit map of item 25.
8. Lines 72 and 78: state Theorem 3.5's first clause without the restriction, as R1 (labelled a referee closure), and mark GAP A4's first clause as closed by R1. Its second clause moves into A5-glob.
9. Line 84: state R3's reduction: `Ω_5^K = 0` given S1-S9 (cited, not rebuilt), and A5-glob given that and the η-invariant framework. Keep the conclusion conditional.
10. Line 46: add R2 (labelled a referee closure) as the quasi-free half of Q1′. Keep the interacting half as part of CH1-5U-q[𝒫].
11. Line 94: add R5's restricted statement.
12. Line 96: Attack 3 fails "with AM-5"; name its carriers `c`, `ccc`, `c^5`; cite `CH1.md` line 225 and Corollary U-T″ (lines 197-201) (item 42).
13. Line 100: cite frozen W2 (`GA2_Y2.md` line 88, Theorem 3.4) and frozen Lemma C2-5 (`CH1.md` line 109) in place of "assuming pass 1's cited W2" and "not checked here".
14. Lines 106-108: replace CH1-5U-q by R4's statement and proof. The GAP of line 108 is then closed.

Optional: strengthen the `u = 1` remark of line 32 (2.3, item 16), and rename one of the two maps called `σ`.

---

## 6. Open statements to carry, by name

- **CH1-5U-i** (frozen `CH1.md` line 225). On the line its anomaly ledger now reads: every perturbative `U(5)` anomaly of `R_u` and `R_u^*` vanishes (Theorem 3.2); the Witten and mod-16 tests vanish (Theorems 3.3, 3.4); no new-`SU(2)` test exists (R1); the full global statement is A5-glob, below, which is conditional. Six attacks are on file, in the narrower scopes of `CH1_5U.md` §4.
- **CH1-5U-q[𝒫]** (R4). It is implied by CH1-5U-i[𝒫] for every prescription `𝒫`. It fails at every number-conserving quasi-free point whose elementary two-point function decays exponentially (R2). Its interacting case is open.
- **A5-glob.** Every anomaly of `R_u` and of `R_u^*` on `K_d`-manifolds, and hence on `Spin(d) × U(5)`-manifolds, vanishes. It holds given `Ω_5^K = 0`, which R3 derives from the cited standard theorems S1-S9, and given the η-invariant framework. It becomes a closure when S1-S9, or a direct computation of `Ω_5^K`, are rebuilt as library entries and gated.
- Inherited, unchanged: CH1-i; CH1-ii; AM-5; CH1-5O-i; reflection positivity; CG1K-H; LW1-5-X; VC1-5U-odd; GA2's bridge Y2.

---

## 7. Freeze recommendation

**`CH1_5U.md` can enter the frozen part `CH1.md` by a dated amendment once edits 1-14 are applied.** Every theorem of `CH1_5U.md` is correct as stated. The two ERRORs are a misstated status sentence and an inexact quotation. The six INCOMPLETE items are omitted clauses or compressed steps, and each has its fix. The amendment should list what is proved (Theorems 2.1, 2.2, 3.1-3.5, 4.1, 5.1; R0, R1, R2, R4, R5 as referee closures not themselves refereed), what is conditional (A5-glob, with S1-S9 and the η-invariant framework named), and what is open (CH1-5U-i, CH1-5U-q[𝒫]). It should not state that every `U(5)` anomaly vanishes without that condition. No law fails at a named step here, so both five-mode laws stay live under `TOE_ASSEMBLY.md` section 3.5.

---

## 8. Scratch checks (guides only)

`/tmp/toe-ch15uref/check_ref.py`, output `/tmp/toe-ch15uref/out.txt`. Exact integer arithmetic except (7). 0.45 s, 172 MB peak.

- (0) The line values with `|u| ≤ 40` are `−33, −23, −13, −3, 7, 17, 27, 37`.
- (1) For each, the 16 weights of `φ_u^*S` equal those of `R_u`; `a` is odd, `b ≡ 3 mod 5`, `k` odd, `k'` even; the charges are `u` (10 times), `−3u` (5 times), `5u` (once).
- (2) For each, every coefficient of `Σ_w(w·x)` and `Σ_w(w·x)^3` is zero, for `R_u` and for `R_u^*`. Control: the one-site carriers `ccc`, `c`, `c^5` give nonzero cubic coefficients and linear sum `−40`.
- (3) For each, `ν(i·h_T)` over all 32 subsets `T` depends only on `r = |T|` and equals `ε·(16, 0, 0, 0, 0, −16)`; without the singlet, `ν(i·1_5) = 15ε`.
- (4) The seven `SU(2)` splittings of `5` give `n(5) ∈ {20, 10, 5, 4, 2, 1, 0}`, and `n(R_u) = 4n(5)` in each.
- (5) For `n = 2, …, 40`, the solutions of `α + 2β + γ ≡ 0`, `2α − β − γ ≡ 0 mod n` are exactly the multiples of `(1, −3, 5)`.
- (6) Grassmann expansion: `O_2` has 60 monomials, and `A_{12;1}B^2_{;2}B^1_{;1}C_{;2}` has coefficient 1. `O_3` has 60 monomials, and `A_{23;1}A_{45;2}\bar B_{1;1}\bar C_{;2}` has coefficient 8, the eight orderings of line 92. All 24 generators of `su(5)` annihilate both. Control: the identity of `gl(5)`, acting through indices only, annihilates `O_2` but not `O_3`, whose `ε` scales by `det`; the twist charges cancel that, as `−2u − 3u + 5u = 0`.
- (7) On the 32-dimensional site space, `Γ` is a homomorphism, and the commutant of two random `Γ(g)` has dimension 6, the dimension of the functions of `N_x`.

---

## FINISH

**Proved here (pass 3; referee closures, not themselves refereed).**
- The verdicts: 57 items, 49 CORRECT, 2 ERROR, 6 INCOMPLETE. No theorem of `CH1_5U.md` is false, and no fix changes a theorem's content.
- R0: the scalar step of Theorem 2.1 and a direct proof that each `ψ_{a,b}` is onto.
- R1: for `d ≥ 3` there is no continuous homomorphism `Spin(d) ×_{Z_2} SU(2) → K_d` over `SO(d)`, with or without a spin component.
- R2: in a number-conserving quasi-free state whose elementary two-point function decays exponentially, every quasi-local fermion-odd operator of nonzero charge has correlations that decay faster than every power. So no quasi-free point has light content exactly `R_u ⊕ R_u^*`. Under a plain reading of CH1-5U-i's gap clause that passes the four tests, no number-conserving quasi-free state at a c-number background has the light content CH1-5U-i asks for.
- R4: CH1-5U-i[𝒫] implies CH1-5U-q[𝒫] for every charged-correlator prescription `𝒫`.
- R5: no unitary linear symmetry of the mirror that commutes with `U(5)` and fixes `O_2` and `O_3` carries a perturbative, Witten, mod-16 or new-`SU(2)`-type anomaly.
- R3, conditional: `Ω_5^{Spin ×_{Z_2} U(5)} = 0` given the cited standard theorems S1-S9. Also, every `K`-manifold is `Spin^c` through `[s, g] ↦ [s, det g]`; with Wu's formula, `w_2w_3 = 0` on it.

**Counterexamples.** None to a theorem of `CH1_5U.md`. One to the first clause of GAP Q1′ read as a target ("every … multiparticle excitation in every quasi-free system has charge ±1"): three particles above a quasi-free sea carry charge 3. `CH1_5U.md` does not assert that clause; it says the clause is not shown.

**Open, by name.**
- **CH1-5U-i**, with the anomaly ledger of section 6.
- **CH1-5U-q[𝒫]** (R4), implied by CH1-5U-i[𝒫]; false at quasi-free points with a gapped elementary field (R2); open for interacting laws.
- **A5-glob**, conditional on S1-S9 and the η-invariant framework, neither rebuilt here.
- Inherited, unchanged: CH1-i, CH1-ii, AM-5, CH1-5O-i, reflection positivity, CG1K-H, LW1-5-X, VC1-5U-odd, GA2's bridge Y2.

**What changes downstream.**
- `CH1.md`, by amendment: its CH1-5U-i paragraph (line 225) can add the anomaly ledger of section 6, and its open list gains CH1-5U-q[𝒫] and A5-glob. AM-5's sentence "Global anomalies are not settled" (line 207) stays true of AM-5. For the `U(5)` ledger of the line family, the global part reduces to A5-glob.
- Attack 4 (an imported `Spin(10)` gapping) has no quasi-free starting point, now with composites included (R2).
- Attack 3 concerns the one-site carriers `c`, `ccc`, `c^5`. No attack on file excludes, as the light content of an interacting state, the line family that frozen Corollary U-T″ carries at one site for `2 ≤ m ≤ 8`.
- GA2 and Y2: nothing new; W2 is already frozen in `GA2_Y2.md`.
- No law fails at a named step. Both five-mode laws stay live under `TOE_ASSEMBLY.md` section 3.5.
