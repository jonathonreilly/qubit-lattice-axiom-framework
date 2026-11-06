lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GA2 Y2 referee report (pass 3)

Written 2026-11-06 (UTC) by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). It is pass 3, the referee, of part GA2, bridge Y2, under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**Referee.** This session wrote none of the pass-1 drafts (`GA2_Y2_DRAFT.md`, `Y2W_DRAFT.md`, `Y2WL_DRAFT.md`). It did not write pass 2 (`GA2_Y2.md`). This is one check: one whole-part, line-by-line read. No other review was read. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status. It adopts no law, no reading and no definition. It changes no axiom or working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A "referee closure" (R1-R7) is a short complete argument written here. "[check]" marks a tiny scratch computation; a check guides and never proves.

**Text read.** `GA2_Y2.md` at commit `c96e71cdf`, the commit that adds it and the branch head of `claude/toe-assembly` when read. SHA-256 of the file read: `d1e827ab9b5635e4689d8fd504405d4da2a1bded61397a757b613fc5a764738e`. Line numbers below refer to that file.

**Sources read, with commits.**

| File (this folder) | Content read (last change before the read) | Lines read, numbered at that commit |
|---|---|---|
| `GA2_Y2.md` | `c96e71cdf` | 1-155 (all) |
| `GA2_Y2_DRAFT.md` | `7d2b20d29` | 1-215 (all). SHA-256 equals the hash `GA2_Y2.md` line 11 records. |
| `Y2W_DRAFT.md` | `92e03055c` | 1-208 (all). Hash equal. |
| `Y2WL_DRAFT.md` | `2d0adc0c0` | 1-358 (all). Hash equal. |
| `TOE_ASSEMBLY.md` | `7d2b20d29` | 183 (PS-6r), 201-220 (sections 3.4, 3.5), 385-396 (GA2), 538-562 (section 6) |
| `LW1.md` | `5ff19240c` | 26 (free data), 43-48 (spin-`S` link) |
| `LW1_5.md` | `b05ee6430` | 72-91 (the laws `L5-O` and `L5-U`) |
| `LW1_REFEREE.md` | `5a2a0affe` | 1-80 (format only) |

No other branch was read. `LIT_QLM.md` was not read; `GA2_Y2.md` uses it as context only.

**The branch moved during this pass.** Others committed `ecb2036d9` and `4b65c608f` to `claude/toe-assembly` while this report was written. At `4b65c608f`, `GA2_Y2.md`, the three pass-1 drafts and `TOE_ASSEMBLY.md` are byte-identical to the versions read (hashes rechecked). `LW1.md` gained Amendment 3 (four lines); the cited lines move down by four, with unchanged content. `LW1_5.md` was edited at its freeze. Its cited lines also move down by four. The `L5-U` law and its Gauss generator are unchanged. The `L5-O` line now adds "with \(\eta_a=\eta^y_a\) and \(\eta_{10+b}=\eta^x_b\)", which is the notation `GA2_Y2.md` already uses. No verdict here depends on these edits.

**Working set used, by name.** PS-5 and PS-6r only through the two five-mode laws as written in `LW1_5.md` lines 74-91: their registers, link operators and site Gauss generators. PS-6 and PS-6r through `LW1.md`'s spin-`S` link. PS-7r only through `LW1_5.md` line 89: "the interacting vacuum is VC1's question". The axioms Lattice and Qubit are not used. Rows (a2) and (b) of `GA2_Y2.md` mention them; those rows are checked against pass 1 only.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws, readings and definitions are read plainly.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: spectra of similar operators; Cauchy-Schwarz; the canonical anticommutation relations, including a unitary change of basis among modes; the group algebra of `S_3`; `ℓ^2` of a countable set; the Fejér and Dirichlet kernels. Standard facts cited, not rebuilt, exactly where `GA2_Y2.md` already relies on them: for a compact Lie group `G`, `exp(𝔤)` generates the identity component `G_0`, and `G/G_0` is finite; a continuous one-parameter unitary group in finite dimension is `e^{itL}` with `L` Hermitian. No literature is used.

**Method.** Every proof in `GA2_Y2.md` was re-derived by hand. The face-step table of the cube was recomputed from `ν × n̂`. Each place where `GA2_Y2.md` describes "the draft" or "pass 1" was compared with the pass-1 text. Quotations keep the words of the source exactly; inline LaTeX of the form `\(…\)` is rendered as plain symbols. Verdicts: CORRECT; ERROR (a false or misattributed line, quoted, with the fix); INCOMPLETE (a named missing step, with a referee closure). Section 7 lists the checks.

**Counts.** 75 items: 64 CORRECT, 7 ERROR, 4 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. Seven referee closures, R1-R7, are proved in section 3.

---

## 1. Verdict table

| # | Item (`GA2_Y2.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 "Proved here" list (5) | CORRECT | Each listed result is proved in §§2-4. |
| 2 | §0 GAP, sentence 1: "The pass-1 claim that finite-list SC implies GA2 is unsupported" (7) | CORRECT | Gap real. Pass 1 claims it: `Y2W_DRAFT.md` line 58, "If yes, T0-start and T0-rate give GA2(a)". R2 proves the non-implication and the repaired implication. |
| 3 | §0 GAP, sentence 2 (7) | ERROR | Quoted: "The claimed exclusion of all possible RG-domain or universality descriptions is also too broad". Pass 1 excluded no universality description; it proposed one. `GA2_Y2_DRAFT.md` line 134: Y2's second clause "has to be read as a statement about gauge-invariant correlators: a **universality** statement". The real overreach is narrower. Corollary Y2-0 (line 130) omits the identification its proof assumes. FINISH (line 192) calls `TOE_ASSEMBLY.md`'s sentence "false for every PS-6r law". Fix E1; precise statement R4. |
| 4 | §0 GAP, sentence 3: cube results need the stated loops and readings (7) | CORRECT | Scope statement; true. |
| 5 | §0 "Open" list (9) | CORRECT | Y2-W-L0 is decided under each named reading (Theorem 4.3; line 149 says so). What stays open is the choice of reading. `ε_Θ` reduces to `ε_µ` (R1). |
| 6 | §0 Provenance (11) | ERROR | The three SHA-256 values match the pass-1 files. But two sentences conflict. One gives "reasoning effort high, codex-cli 0.165.0, session `01a1aea0-1f38-7571-834e-c973872cdbe4`". The next says "effort and session ID not visible". Fix E2. |
| 7 | Def. 1, operator link and covariance (15-17) | CORRECT | Matches `GA2_Y2_DRAFT.md` (1.1). |
| 8 | Def. 2, `L5-U` register (18) | CORRECT | Matches `LW1_5.md` line 81. |
| 9 | Def. 3, defect and coherence (19) | ERROR | Quoted: "These are state-dependent and not gauge-invariant diagnostics." `κ` is not gauge invariant. `D_ω(Y)` is unchanged under every gauge unitary that commutes with `Y`. Theorem 4.4's proof uses exactly this: "gauge averaging preserves the defect". Fix E3. |
| 10 | Def. 4, SC (20) | INCOMPLETE | Theorem 3.1 uses `ι(O^†) = conj ι(O)` and `ι(O_1O_2) = ι(O_1)ι(O_2)` for listed products in both orders. Def. 4 states neither. Pass 1 states the second: "both orders mapped to the same commuting product" (`Y2W_DRAFT.md` line 56). Closure R7(a); fix E4. |
| 11 | Def. 5, SC-loop (21) | CORRECT | |
| 12 | Def. 6, boundary cube and readings F, S, B (22) | CORRECT | Outward orientation fixes the step direction `ν × n̂` used in Theorem 4.4 [check: `geom.py`]. |
| 13 | Def. 7, cube skeleton (23) | CORRECT | |
| 14 | Def. 8, thresholds (24) | CORRECT | `η_* = 8ε_Θ + 6δ` silently corrects `Y2W_DRAFT.md` line 159, which used "`η_* = 8ε_μ(g_*) + 6δ`" for the cube family. Theorem 3.1 needs the bound for the listed observable's own image, as `Y2WL_DRAFT.md` Lemma 0′ (line 299) does. Mark the correction (E11). R1 gives `ε_Θ ≤ 36ε_µ`. |
| 15 | Theorem 2.1, statement (28) | CORRECT | |
| 16 | Theorem 2.1, proof (30) | CORRECT | Re-derived. `A = 1⊗L − τ⊗1 = 𝐔B𝐔^{-1}` with `B = 1⊗L`. `spec A = ∪_a(spec L − λ_a)`. Maxima give `min λ_a = 0`; minima give `max λ_a = 0`. |
| 17 | Corollary 2.2, statement (32) | CORRECT | For "`[E,U]=qU`" the text should say `E` Hermitian, as pass 1 does. Or prove it by trace: `U^{-1}EU = E − q` gives `q·dim = 0`. |
| 18 | Corollary 2.2, proof: finite register and norm bound (34) | CORRECT | |
| 19 | Corollary 2.2, proof: compact-Lie step (34) | INCOMPLETE | Quoted: "A compact Lie subgroup of U(N) with infinite image has positive-dimensional identity component, hence nonzero differential." It mixes `G` with `ρ(G)` and does not say why `dρ ≠ 0`. Closure R7(b); fix E5. |
| 20 | Spin-`S` remark: `J\|S⟩=0`, `[E,J]=J`, rank `2S`, approach on finite flux (36) | CORRECT | `LW1.md` lines 46-48. |
| 21 | Spin-`S` remark: "the norm bound excludes uniform operator-norm convergence under a common covariant identification" (36) | INCOMPLETE | "a common covariant identification" is undefined. N3′ alone compares nothing across spaces of different dimension. Closure R7(c); fix E6. |
| 22 | Theorem 2.3, statement and proof (38-40) | CORRECT | Conjugation multiplies by `(ρ(g)^{-1}kρ(h))_{ab}`. `V` is a representation of `G × G`. |
| 23 | Corollary 2.4, statement and proof (42-44) | CORRECT | `π(𝒢_x^T)` is bounded and self-adjoint since `π` is a *-representation. |
| 24 | GAP N5/block: block generators may be sums or emergent; finite sums covered; limits not settled (46) | CORRECT | Gap real, for unbounded generators only. R3 proves the bounded case and gives an unbounded counterexample. |
| 25 | GAP N5/block: no unitary intertwines a bounded site generator with the unbounded Wilson one (46) | CORRECT | |
| 26 | GAP N5/block: "This is the precise content of Y2-0" (46) | ERROR | Y2-0's proof (`GA2_Y2_DRAFT.md` line 132) uses Corollary N5. N5 excludes more than an intertwiner of generators. Pass 1 line 101: "Theorem N says more: it excludes the link variable, whatever the identification of generators." Precise statement: R4. Fix E7. |
| 27 | Theorem 2.5, statement (48) | CORRECT | [check: `link2.py`, `major.py`] |
| 28 | Theorem 2.5, proof (50) | CORRECT | `U^{ca}` is Hermitian, so `(𝐔^†𝐔)^{ab} = Σ_c U^{ca}U^{cb} = Nη^x_aη^x_b`. |
| 29 | Remark: half-spinor 512, link matrix 5120, rank ≤ 512; special representation (52) | CORRECT | |
| 30 | Theorem 3.1, statement (56-58) | CORRECT | Needs E4. The constant 8 can be 4 (R1(a)); optional. |
| 31 | Theorem 3.1, proof (60) | CORRECT | Two quadratic terms give `2δ`; two linear terms with coefficient 2 give `4δ`. |
| 32 | Theorem 3.2, statement (62-64) | CORRECT | `E` must be self-adjoint, as pass 1 says ("E Hermitian"). Every use has a number operator. `K_m = min(m,10−m)+1` checked. |
| 33 | Theorem 3.2, proof (66) | CORRECT | Re-derived edge by edge, with the end edges. "The latter" must mean the total variation, not its square. [check: `corner.py`] |
| 34 | Corollary 3.3 (68-70) | CORRECT | `K_5 = 6` gives 1/18; `K_1 = K_9 = 2` gives 1/2. |
| 35 | Remark on `U(1)`-charged plaquettes and surfaces (72) | CORRECT | |
| 36 | Theorem 3.4, statement (74) | CORRECT | [check: `link2.py`, `link3.py`, `major2.py`] |
| 37 | Theorem 3.4, proof: nilpotence, `M`, `κ ≤ 1/2` (76) | CORRECT | The square-zero bound re-derived: `\|ω(X)\|^2 ≤ min(q‖Xψ‖^2, (1−q)‖X^†ψ‖^2) ≤ (‖Xψ‖^2 + ‖X^†ψ‖^2)/4`. |
| 38 | Theorem 3.4, proof: the Slater state (76) | INCOMPLETE | "`ω(N^xN^y)=5`" is stated without a reason. "yielding `M=15`" should read `ω(M)=15`. Closure R7(d); fix E8. |
| 39 | Theorem 3.4, proof: `L5-O` half-spinor (76) | CORRECT | Rows anticommute; `U^{cc}` anticommutes with `η^x_cη^x_d` and `η^y_cη^y_d`. [check: `major2.py`] |
| 40 | Theorem 3.5, statement and proof (78-80) | CORRECT | With `κ_1 = A/B`: `κ_k = kA/((k−1)A + B)`. |
| 41 | `L5-U[ρ]` paragraph (82) | ERROR | The mathematics is correct: the summed end number takes `0, …, 5k`. Quoted: "For the proposed L5-U[ρ] datum". Pass 1 records it and does not propose it: `Y2W_DRAFT.md` line 179, "(recorded, not proposed)". Fix E9. |
| 42 | GAP classicality (84) | CORRECT | Gap real. R5 gives an example. |
| 43 | Theorem 4.1, statement (88-93) | CORRECT | [check: `link2.py` for the two link identities; `geom.py` for corner types over all 720 orders] |
| 44 | Theorem 4.1, proof (95) | CORRECT | Index bookkeeping re-derived: `E^p_{later,earlier}` at the particle end and `(1−E^h)_{earlier,later}` at the hole end. A fixed-point-free permutation of three ends is a 3-cycle. |
| 45 | Theorem 4.2, statement (97) | CORRECT | [check: `link3.py`, `corner.py`] |
| 46 | Theorem 4.2, proof (99) | CORRECT | The step `(S−Z)^2 = S−Z` also uses that `SZ` and `ZS` are the two transpositions other than `S` (pass 1, `Y2WL_DRAFT.md` Lemma R(iii)). Say so (O6). |
| 47 | Theorem 4.3, statement (101-102) | CORRECT | |
| 48 | Theorem 4.3, proof: F and S (104) | CORRECT | Orders with the same particle ends give the same point operators, hence the same product. |
| 49 | Theorem 4.3, proof: B for `2 ≤ m ≤ 8` (106) | CORRECT | Corners need `s_v + 3 ≤ 5`; inner points need `s_v + 2 ≤ 5`. Both hold. `4^4(−2)^4 = 4096`. |
| 50 | Theorem 4.3, proof: `m = 1, 9` (108) | CORRECT | `Θ^σ = P_σΘ^σP_σ` because `Θ^σ` preserves end numbers and kills an empty particle end. |
| 51 | Theorem 4.4, statement (110) | CORRECT | Links off the block edges carry any fixed vector; say so (O7). |
| 52 | Theorem 4.4, proof (112) | CORRECT | Face table recomputed. Even lowest corner: `e_3`-faces before `e_1`-faces before `e_2`-faces, 8 orders; odd: reversed, 8 orders [check: `geom.py`]. |
| 53 | Theorem 4.5, statement (114) | CORRECT | |
| 54 | Theorem 4.5, proof (116-118) | CORRECT | Re-derived step by step. `225 · 72 = 16200`; `28 · 16200 = 453600`. [check: `corner.py`, largest ratio 0.48 against the proved 18] |
| 55 | Theorem 4.6, statement and proof (120-122) | CORRECT | [check: `geom.py`: no fixed order makes all four cubes agree] |
| 56 | Paragraph: `κ = 0`; the `S∞` state fails SC (124) | CORRECT | "κ=0 on every link" holds on skeleton links; other links as chosen (O7). |
| 57 | §5 four-test preamble (128) | CORRECT | |
| 58 | Row SC (132) | CORRECT | Matches `Y2W_DRAFT.md` section 1.3. |
| 59 | Row SC-loop and `U(1)`-blindness (133) | CORRECT | |
| 60 | Row boundary-loop block faces (134) | CORRECT | Matches `Y2WL_DRAFT.md` section 1.4. |
| 61 | Row F (135) | CORRECT | |
| 62 | Row S (136) | CORRECT | |
| 63 | Row B (137) | CORRECT | |
| 64 | Row (a1) (138) | CORRECT | Matches `GA2_Y2_DRAFT.md` FINISH table. |
| 65 | Row (a2) (139) | CORRECT | |
| 66 | Row (b) (140) | CORRECT | |
| 67 | Row (c) (141) | ERROR | Typo: "Corollator or integration-variable matching needs proof." Read "Correlator". Fix E10. |
| 68 | Row (d) (142) | CORRECT | |
| 69 | Row `L5-U[ρ]` (143) | ERROR | Quoted: "Proposed alternative to the fixed rishon register". Pass 1: "(recorded, not proposed)" (`Y2W_DRAFT.md` line 179). The test results in the row match pass 1. Fix E9. |
| 70 | Laws paragraph (145) | CORRECT | `C(10,5) = 252`; half-spinor of `so(20)` is `2^9 = 512`; matches `LW1_5.md` lines 74 and 81. |
| 71 | Y2-W and its three attacks (147) | CORRECT | Failing steps match `Y2W_DRAFT.md` section 3. The rejected inference is pass 1's "Remark (not used)". |
| 72 | Y2-W-L and Y2-W-L0 (149) | CORRECT | |
| 73 | Y2-W-LB(m), `m = 3, …, 7` (151) | CORRECT (open) | Attacks match `Y2WL_DRAFT.md` section 4.3. |
| 74 | Kernel paragraph and its GAP (153) | CORRECT | Peter-Weyl embedding and the integer/half-integer spin split are right. Gap real; R6. |
| 75 | ZM1-G, T0-start, T0-rate, T0-QLR, T0-D (155) | CORRECT | Requests only; consistent with `GA2_Y2_DRAFT.md` FINISH. |

---

## 2. The distiller's GAPs

`GA2_Y2.md` marks six gaps: three sentences in §0 (line 7) and three at their points of use (lines 46, 84, 153). Each is judged below. Each judgment quotes the GAP first.

**G1. SC does not give GA2 (line 7).** Quoted: "The pass-1 claim that finite-list SC implies GA2 is unsupported: moment agreement for finitely many observables at one scale does not control the other observables, scales, or errors." **Real.** Pass 1 asserts the implication without proof (`Y2W_DRAFT.md` line 58: "If yes, T0-start and T0-rate give GA2(a) on the window"). T0-start and T0-rate speak about `µ` only. SC speaks about `ω` on one finite list. **Closure R2.** R2(a): SC depends only on `ω` restricted to the links of its list. R2(b): every state satisfying SC has a completion outside those links that still satisfies SC, while every flux-raising loop and every boundary cube product outside them has expectation zero, so `D ≥ 2` there. So no argument from SC and `µ` alone gives a comparison at other locations or scales. R2(c), the repaired statement: GA2(a) on a set `𝒪` of correlators follows from ZM1-G on `𝒪` at every scale of the window plus T0-rate, by the triangle inequality.

**G2. The scope of Y2-0 (line 7).** Quoted: "The claimed exclusion of all possible RG-domain or universality descriptions is also too broad: the operator obstruction assumes the specified bounded Gauss generator and an intertwining identification." **Real in a narrower form; misattributed in part.** Pass 1 did not exclude universality descriptions. It proposed one. `GA2_Y2_DRAFT.md` line 134 continues with "Suggested wording for the lead, not made here:" followed by a statement titled "Y2, universality." The overreach in pass 1 is this. Corollary Y2-0 reads "For no PS-6r law, at any finite register size, is the gauge sector Wilson's lattice gauge theory" (line 130), with no identification named. Its proof assumes one: "An identification of the two lattice theories would carry `U_b` to such an operator" (line 132). FINISH then calls `TOE_ASSEMBLY.md`'s sentence "That is T0's theory up to bridges Y1-Y3 below" "false for every PS-6r law" (line 192). That sentence allows bridges, so an operator obstruction does not make it false. **Closure R4** states Y2-0 precisely. It also corrects the distiller: the precise content is wider than "a unitary equivalence intertwining a bounded site generator with an unbounded Wilson Gauss generator" (line 46), because Corollary 2.4 excludes the covariant image of the link whatever the generators are mapped to.

**G3. Cube results need the stated readings (line 7).** Quoted: "The cube results require the explicitly defined boundary loops and ordering readings; they do not select ZM1's block map." **Real as a scope statement.** Theorems 4.1-4.6 are proved for boundary-loop faces and for F, S and B. Nothing needs repair. One addition: R2(b)(iii) shows that boundary-loop cube products of every order vanish in a simple flux state. Theorem 4.4 gives a state where they all meet SC-loop with `η = 0`. So under S both outcomes occur in explicit states, and a decision of Y2-W-L needs the VC1 state.

**G4. GAP N5/block (line 46).** Quoted: "A block transformation may instead be generated by a sum over its sites, or may be an emergent action. The corollary applies to any *specified bounded* coarse generator, including a finite sum, but does not settle a changing-block or singular limit." **Real, and only for unbounded generators.** Pass 1 identified block transformations with fine-site ones: "Those are gauge transformations of the law at fine sites. So Corollary N5 covers block links at every scale" (`GA2_Y2_DRAFT.md` line 99). **Closure R3.** R3(a) proves Corollary 2.4 for every bounded self-adjoint generator, so for every finite block at every fixed scale. R3(b) is a counterexample for an unbounded generator: in a representation of the `L5-U` link algebra, the summed end number over infinitely many links has an exactly covariant unitary raising operator. So the obstruction holds for every bounded coarse generator and fails for this unbounded one.

**G5. GAP classicality (line 84).** Quoted: "Coherence tending to one in a chosen product state is not a proof of a classical phase, a vacuum, a small bare coupling, a continuum limit, or an `O(1/k)` GA2 error." **Real.** Pass 1 wrote "the links can be classical to `O(1/k)`" and "GA2 holds only with an error `O(9/k)` that must fit its budget" (`Y2W_DRAFT.md` line 177). Both are kinematic readings of Theorem 3.5. Neither is a statement about the law's dynamics. **Closure R5** sharpens the gap with an example. Product states with coherence `k/(k+5)` on every link can have a plaquette with `ω(W_p) = 0`, hence `D(cW_p) ≥ 2` for every `c`. Coherence measures each link alone; a loop defect measures the product around the loop.

**G6. GAP band-limited kernel (line 153).** Quoted: "a band-limited kernel is not automatically a positive probability density or outside the hard-core class. Its comparison with that class is open." **Real.** **Partial closure R6.** Band-limitation decides neither positivity nor its failure: the Fejér kernel is band-limited and nonnegative, and the Dirichlet kernel has the same band and takes negative values. Positivity must come from the transfer. The comparison with the hard-core class stays open by name ("the band-limited kernel question"). It is not well posed until Y1 fixes a Euclidean form and the YM branch pins its class.

---

## 3. Referee closures

Each closure is finite linear algebra or elementary analysis. None uses a computation as a step.

### R1. Products of normalized traces

**Lemma R1.** Let `w_1, …, w_k ∈ ℂ` with `|w_f| ≤ 1`, and put `u_f := 1 − Re w_f ≥ 0`. Then
(a) `|1 − w_f|^2 ≤ 2u_f`;
(b) `1 − Re(w_1 ⋯ w_k) ≤ k Σ_f u_f`.

*Proof.* (a) `|1 − w|^2 = 1 − 2Re w + |w|^2 ≤ 2 − 2Re w`. (b) Put `P_j := w_1 ⋯ w_j`; then `|P_j| ≤ 1`. For complex `A, B` the identity `1 − AB = (1 − A) + (1 − B) − (1 − A)(1 − B)` gives `1 − Re(AB) ≤ (1 − Re A) + (1 − Re B) + |1 − A||1 − B|`. For `|A| ≤ 1`, also `|1 − AB| ≤ |1 − A| + |A||1 − B| ≤ |1 − A| + |1 − B|`. Apply both with `A = P_j`, `B = w_{j+1}`, for `j = 1, …, k − 1`. Induction gives `1 − Re P_k ≤ Σ_f u_f + Σ_{f<g} |1 − w_f||1 − w_g|`. By (a), `|1 − w_f||1 − w_g| ≤ 2(u_f u_g)^{1/2} ≤ u_f + u_g`. Each index lies in `k − 1` pairs. So `1 − Re P_k ≤ k Σ_f u_f`. ∎

**Consequences.**
1. In Theorem 3.1, (a) gives `2E|w − 1|^2 ≤ 4ε`, so `D_ω(Ŵ) ≤ 4ε + 6δ`. The stated `8ε + 6δ` is true and weaker.
2. `Y2WL_DRAFT.md` Lemma 0′ (line 299) takes the commuting image of a cube product to be "`Θ_c := Π_f w_f`, each `w_f` a normalised trace". Each `w_f` is the normalized trace around a plaquette of `µ`'s lattice at scale `r = a_{k0}`. If every plaquette satisfies `E_µ(1 − Re w_f) ≤ ε_µ`, then (b) gives `E_µ(1 − Re Θ_c) ≤ 6 · 6ε_µ = 36ε_µ`. So `ε_Θ ≤ 36ε_µ`, and the open bound `ε_Θ` follows from the plaquette bound `ε_µ`.
3. The constant `k` in (b) is sharp as `θ → 0` for `w_f = e^{iθ}`: `1 − cos 6θ ≈ 18θ^2` and `6 Σ_f (1 − cos θ) ≈ 18θ^2` [check: ratio 0.99999 at `θ = 10^{-3}`].

### R2. SC at one scale and GA2

Matter is suppressed, as in Definition 2.

**R2(a) (SC is local).** Let `R` be the finite set of links on which the listed observables act, and `𝔄_R` their algebra. Every listed observable and every product of two of them lies in `𝔄_R`. So whether SC(`r`; `δ`) holds for `ω` with a given `µ` depends only on `ω|𝔄_R`. ∎

**R2(b) (non-implication).** *Proposition.* Let `ω` satisfy SC(`r`; `δ`) with `µ`, and let `R` be as in (a). Let `1 ≤ m ≤ 5`. Let `φ` be the product vector state on the links outside `R` in which every link `ℓ = (x, x + e_i)` holds its `m` rishons at its lower end `x`, in colours `1, …, m`. Put `ω_φ := ω|𝔄_R ⊗ φ`. Then:
(i) `ω_φ` satisfies SC(`r`; `δ`) with the same `µ`;
(ii) `ω_φ(W) = 0` for every loop `W` that uses some link outside `R` exactly once;
(iii) for every block scale `r'`, every boundary block cube `c` whose skeleton lies outside `R`, and every order `σ`: `ω_φ(Θ^σ_c) = ω_φ((Θ^σ_c)^†) = 0`, hence `ω_φ(Θ^S_c) = 0`;
(iv) for each `Y` in (ii) or (iii) and every `c ∈ ℂ`, `D_{ω_φ}(cY) ≥ 2`.
For `6 ≤ m ≤ 9` the same holds with `φ` replaced by its particle-hole image (Theorem 4.2).

*Proof.* (i) By R2(a); `ω_φ` is a state because links are ordinary tensor factors. (ii) Each term of `W` is `A ⊗ B`, with `A` on links of `R` and `B` on links outside `R`. Entries on different links commute, so `B` is a product over links. On the link `ℓ` that `W` uses once, `B` has one entry `U^{jk}_ℓ` or its adjoint. It shifts `N^x_ℓ` by `±1` (proof of Theorem 3.2). `φ` is a product of `N^x_ℓ`-eigenvectors. So `φ(B) = 0` and `ω_φ(A ⊗ B) = ω(A)φ(B) = 0`. (iii) By the proof of Theorem 4.3, `Θ^σ_c` and its adjoint annihilate a product vector unless every `σ`-particle end on the skeleton is occupied. In `φ` the occupied end of every link is its lower end. Take the four block edges of `c` parallel to `e_1`, with lower endpoints `(0,0,0)`, `(0,1,0)`, `(0,0,1)`, `(0,1,1)` relative to the lowest block corner. The particle end is the head of the earlier face's step. So each of these edges needs its earlier face to step along `−e_1`. By the face table (`Y2WL_DRAFT.md` section 4.2, recomputed here [check: `geom.py`]), the face stepping along `−e_1` is `−e_3`, `+e_2`, `−e_2`, `+e_3` respectively; the other face is `−e_2`, `−e_3`, `+e_3`, `+e_2`. Compatibility would need `−e_3 < −e_2`, `+e_2 < −e_3`, `−e_2 < +e_3` and `+e_3 < +e_2` in the order. These close the cycle `−e_3 < −e_2 < +e_3 < +e_2 < −e_3`. No order satisfies them [check: `lower.py`, 0 of 720]. So `Θ^σ_c` and its adjoint vanish on the vector for every `σ`, and `ω_φ` gives zero. (iv) `D_ω(cY) = |c|^2 ω(Y^†Y + YY^†) − 4 Re(c ω(Y)) + 2`, which is at least 2 when `ω(Y) = 0`. For `6 ≤ m ≤ 9`, conjugate by `C` as in Theorem 4.3: `C` maps `N^x`-eigenvectors to `N^x`-eigenvectors, and `CΘ^σC^† = (Θ^{σ^{rev}})^†`. ∎

*Consequence.* SC(`r`; `δ`) holds in `ω_φ` whenever it holds in `ω`. In `ω_φ` every flux-raising loop and every boundary cube product outside `R` has `D ≥ 2` for every normalization. By Theorem 3.1, any SC-type comparison at another location that lists one of these operators, with Theorem 3.1's hypotheses, fails in `ω_φ` once `8ε + 6δ' < 2`. GA2(a), made precise by ZM1-G, compares correlators at every location and every scale of a window. So no argument that uses only SC(`r`; `δ`) for `ω` and properties of `µ` gives GA2(a). An argument from one scale must use further properties of the VC1 state. Pass 1 states none. `ω_φ` is not translation invariant, so this closure does not cover an argument that uses translation invariance.

**R2(c) (repaired implication).** Let `𝒪_r` be a set of gauge-invariant observables at scale `r`, `ι` an identification, `µ` a measure, and `YM_r` the continuum values at scale `r` at the running coupling. Suppose, for every `r` in the window and every `O ∈ 𝒪_r`, `|ω(O) − E_µ(ιO)| ≤ e_1(r)` and `|E_µ(ιO) − YM_r(ιO)| ≤ e_2(r)`. Then `|ω(O) − YM_r(ιO)| ≤ e_1(r) + e_2(r)`. ∎ (Triangle inequality.) So GA2(a) on `𝒪` follows from ZM1-G on `𝒪` at every scale of the window and T0-rate, whenever `e_1 + e_2` fits `O((a/r)^p) + O(g(r)^4)`. SC(`r`; `δ`) is the case of one `r` and one finite list. ZM1-G implies it when the list and its two-fold products lie in `𝒪_r` and `e_1(r) ≤ δ`. This makes precise `GA2_Y2.md` line 20: "It is a necessary component of a suitable stronger comparison, not a sufficient definition of GA2."

### R3. Bounded and unbounded coarse generators

**R3(a).** Let `π` be a representation of the law's quasi-local algebra on `K ≠ 0`, and `L` any bounded self-adjoint operator on `K`. If an operator matrix `𝐕` on `ℂ^n ⊗ K` obeys `[1 ⊗ L, 𝐕] = (τ ⊗ 1)𝐕`, or the right form, with `τ ≠ 0` Hermitian, then `𝐕` has no bounded inverse. *Proof.* Theorem 2.1. ∎ `LW1_5.md` line 84 (at `b05ee6430`) gives the site generator: "`\mathcal G_x^T=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x}`". For a finite set `B` of sites, `π(Σ_{x∈B} 𝒢_x^T)` is bounded. So Corollary 2.4 covers a block transformation generated by a finite sum over the block, at every fixed scale. It also covers one base site per block, which is pass 1's reading.

**R3(b) (an unbounded generator escapes).** Take `L5-U` at `m = 5` and a countably infinite set `S` of links. On each `ℓ ∈ S` fix an occupation basis vector `ξ_ℓ` with `N^x_ℓ ξ_ℓ = 2ξ_ℓ`. Let `Conf` be the set of families `(c_ℓ)_{ℓ∈S}` of occupation labels of `Λ^5ℂ^{10}` that equal the label of `ξ_ℓ` for all but finitely many `ℓ`. `Conf` is countable. On `K := ℓ^2(Conf)` the link algebra of `S` acts factor by factor: for finite `F ⊂ S`, `K ≅ (⊗_{ℓ∈F} Λ^5ℂ^{10}) ⊗ ℓ^2(Conf_{S∖F})`. Put `φ(c) := Σ_ℓ (N^x(c_ℓ) − 2)`, a finite sum, and let `Φ` multiply by `φ`. `Φ` is self-adjoint, unbounded, with integer spectrum. Each level set `Conf_k := φ^{-1}(k)`, `k ∈ ℤ`, is countably infinite. Indeed, one link can shift `N^x − 2` by any of `−2, …, 3`, so finitely many links reach `k`; a further pair of shifts `+1` and `−1` on two unused links gives infinitely many members. Choose bijections `β_k: Conf_k → Conf_{k+1}` and set `Yδ_c := δ_{β_k(c)}` for `c ∈ Conf_k`. `Y` permutes an orthonormal basis, so `Y` is unitary. On finitely supported vectors, `ΦYδ_c = (k+1)δ_{β_k(c)}` and `YΦδ_c = kδ_{β_k(c)}`, so `[Φ, Y] = Y`. ∎

So an invertible operator, exactly covariant with `τ = 1`, exists for this unbounded generator in a representation of the law's own link algebra. Formally, let `S` be the set of links that leave a half-space `H` through their upper end. Then `Φ` is the link part of the `U(1)` generator `Σ_{x∈H} 𝒢_x^1`, minus constants. On a link with both ends in `H` the two end numbers sum to the constant `m`. On a link of `S` only its lower end, which lies in `H`, contributes. The example says nothing about a physical role of `Y`. It shows that boundedness is the hypothesis that carries Theorem 2.1, at every finite block and not in this limit.

### R4. Corollary Y2-0, stated precisely

**Corollary R4.** Let `π` be a representation of the law's quasi-local algebra on `K ≠ 0`, `x` a site, `𝔥 ⊆ 𝔤` a subalgebra, and `T ↦ τ^T` a representation of `𝔥` by Hermitian `n × n` matrices, not identically zero.
(i) No bounded invertible `𝐕` on `ℂ^n ⊗ K` satisfies `[1 ⊗ π(𝒢_x^T), 𝐕] = (τ^T ⊗ 1)𝐕` for all `T ∈ 𝔥`, or the right form.
(ii) Let `H_W := ⊗_b L^2(SU(2))` be T0's slice space over the finitely many links of one time slice, and `𝐔_b` the `2 × 2` matrix of multiplication operators of one link. For every unitary `Φ: H_W → K`, every `𝔥` and every `τ` as above with `n = 2`, the unitary `(1 ⊗ Φ)𝐔_b(1 ⊗ Φ)^*` fails (i)'s covariance.
(iii) No unitary `Φ: H_W → K` carries an unbounded Wilson Gauss generator at a site to `π(𝒢_x^T)`.

*Proof.* (i) Corollary 2.4. (ii) The operator is unitary, hence invertible; apply (i). (iii) Unitary conjugation preserves the norm, and `π(𝒢_x^T)` is bounded. ∎

**Scope.** Y2-0 says (i)-(iii) and no more. It does not exclude an identification of gauge-invariant correlators. It does not exclude group-valued Euclidean integration variables (`GA2_Y2_DRAFT.md` section 4.2). It does not exclude actions with unbounded generators (R3(b)). So `TOE_ASSEMBLY.md` line 552 claims more than is proved when it says "the clause "That is T0's theory up to bridges Y1-Y3" is false for every PS-6r law". What is proved: that clause cannot hold through an identification of the kind in (ii) or (iii).

### R5. Coherence near one does not bound loop defects

**Example R5.** Take the recorded register `L5-U[ρ]`, `ρ = (Λ^5ℂ^{10})^{⊗k}`, with link entries `U^{jk}_ℓ := Σ_{i=1}^{k} U^{jk}_{ℓ,(i)}`. On each link take `φ_{V_ℓ}^{⊗k}`, where `φ_V` is the `m = 5` Slater state of Theorem 3.4. Take the product of these states over links. Then:
- every link has coherence `k/(k+5)` (Theorems 3.4 and 3.5);
- `ω(𝐔_ℓ) = −(k/2)V_ℓ^†` in the operator ordering of Theorem 3.4 [check: `link3.py`, `k = 1`, exact to machine precision]; another ordering convention changes at most an overall sign, which does not affect what follows;
- for a plaquette `p` with links `ℓ_1, …, ℓ_4`, `ω(W_p) = tr Π_i ω(𝐌_i)`, with `𝐌_i = 𝐔_{ℓ_i}` or `𝐔_{ℓ_i}^†` and `ω(𝐔^†) = ω(𝐔)^†`, because the state is a product over links and `W_p` uses each link once.

Choose `V_{ℓ_1} = diag(1, ζ, ζ^2, ζ^3, ζ^4)`, `ζ = e^{2πi/5}`, and `V_ℓ = 1` on every other link. Then `ω(W_p) = (k/2)^4 Σ_{j=0}^{4} ζ^{±j} = 0`. By R2(b)(iv), `D_ω(cW_p) ≥ 2` for every `c`. So coherence `k/(k+5) → 1` on every link is compatible with `D ≥ 2` on a plaquette. A coherence bound is not a small-coupling statement; this is G5's point, now with an example.

### R6. Band-limited kernels

On `U(1)`, the Fejér kernel `F_S(θ) = Σ_{|j|≤S}(1 − |j|/(S+1))e^{ijθ} = (S+1)^{-1}|Σ_{j=0}^{S} e^{ijθ}|^2` has band `|j| ≤ S` and is nonnegative. The Dirichlet kernel `D_S(θ) = Σ_{|j|≤S} e^{ijθ} = sin((S + ½)θ)/sin(θ/2)` has the same band. For `S ≥ 1` it is negative at `θ = 3π/(2S+1)`, where the numerator is `−1` and the denominator is positive. So band-limitation decides neither positivity nor its failure. Positivity of a band-limited transfer kernel must come from the transfer itself.

### R7. Closures of the four INCOMPLETE items

**(a) Definition 4.** Add: "`ι` is multiplicative on the listed products, both orders of a product going to the same commuting product, and `ι(O^†)` is the complex conjugate of `ι(O)`." With this clause the proof of Theorem 3.1 is complete: the commuting image of `D_ω(Ŵ)` is `2E|w|^2 − 2Ew − 2Ew̄ + 2 = 2E|w − 1|^2`. *Four-test check of the added clause.* (1) It names no target: pass. (2) It is two closed conditions: pass. (3) It settles no downstream question; ZM1-G still chooses `ι`: pass. (4) Theorem 3.1 uses both conditions, and pass 1 already states the first: pass. Proposed for the distilled text only; nothing is adopted.

**(b) Corollary 2.2, compact-Lie step.** Let `G` be a compact Lie group, `ρ` a continuous unitary representation on `ℂ^n` with `ρ(G)` infinite, and `V` a continuous unitary representation on a finite-dimensional `R ≠ 0`. Suppose `dρ = 0`. Then `ρ(exp X) = exp(dρ(X)) = 1` for every `X ∈ 𝔤`. `exp(𝔤)` generates `G_0` (cited), so `ρ` is trivial on `G_0`. `G/G_0` is finite (cited), so `ρ(G)` is finite, a contradiction. So some `X` has `τ := −i dρ(X) ≠ 0`, and `τ` is Hermitian. Write `V(e^{tX}) = e^{itL}` with `L` Hermitian (cited). Differentiating `(1 ⊗ V(e^{tX}))𝐔(1 ⊗ V(e^{tX}))^* = (e^{itτ} ⊗ 1)𝐔` at `t = 0` gives `[1 ⊗ L, 𝐔] = (τ ⊗ 1)𝐔`. Theorem 2.1 applies. ∎

**(c) Spin-`S` norm clause.** Let `ι_S` map `|m⟩` to the basis vector `e_m` of `ℓ^2(ℤ)` for integer `S`, or of `ℓ^2(ℤ + ½)` for half-integer `S`. Let `B e_m = e_{m+1}` be the bilateral shift. For every `S` and every `c > 0`, `‖ι_S(J_S/c)ι_S^* − B‖ ≥ ‖(ι_S(J_S/c)ι_S^* − B)e_S‖ = ‖e_{S+1}‖ = 1`, since `J_S|S⟩ = 0`. So no rescaling of `J_S` converges to `B` in operator norm under these embeddings. On each fixed `e_m`, `(S(S+1))^{-1/2} J_S` sends `e_m` to `(1 − m(m+1)/(S(S+1)))^{1/2} e_{m+1} → e_{m+1}`. ∎

**(d) Theorem 3.4, the Slater state.** Rotate the `x`-modes by `V`: `s^†_j := Σ_k V_{kj} r^{x†}_k`. These are five CAR modes, and `N^x = Σ_j s^†_j s_j` because `V` is unitary. The state is `ψ = Π_{j=1}^{5} b^†_j|0⟩` with `b^†_j := (r^{y†}_j + s^†_j)/√2`. Pair `j` consists of the modes `r^y_j` and `s_j`. Expanding the product, each subset `A ⊆ {1, …, 5}` of pairs whose fermion sits at `s` gives one occupation basis vector, with amplitude `±2^{-5/2}` and `N^x = |A|`. So `N^x` is binomial with parameters 5 and ½, and `N^y = 5 − N^x`. Hence `ω(N^xN^y) = 5 · (5/2) − ω((N^x)^2) = 25/2 − (5/4 + 25/4) = 5`, and `ω(M) = 25 − 2 · 5 = 15`. Next, `r^y_j s^†_l` is even, so it commutes with `b^†_i` for `i ∉ {j, l}`. For `l ≠ j` it moves a fermion between two pairs, and its expectation is 0. For `l = j`, a two-mode computation gives `⟨0|b_j r^y_j s^†_j b^†_j|0⟩ = −½`. Since `r^{x†}_k = Σ_l \overline{V_{kl}} s^†_l`, `ω(U^{jk}) = ω(r^y_j r^{x†}_k) = −\overline{V_{kj}}/2`, so `ω(𝐔) = −V^†/2`. Its singular values are all ½, and `2Σ_{jk}|ω(U^{jk})|^2 = 2 · 5/4 = 5/2`. So `κ = (5/2)/15 = 1/6`. ∎ [check: `link3.py`: `ω(𝐔) = −V^†/2` exactly, `⟨N^xN^y⟩ = 5`, `⟨M⟩ = 15`, `κ = 0.166667`]

---

## 4. Required edits to `GA2_Y2.md`

Each edit quotes the text to change. None changes a theorem.

- **E1 (line 7).** Replace "The claimed exclusion of all possible RG-domain or universality descriptions is also too broad: the operator obstruction assumes the specified bounded Gauss generator and an intertwining identification." with: "Pass 1 states Corollary Y2-0 without the identification its proof assumes, and calls `TOE_ASSEMBLY.md`'s sentence 'That is T0's theory up to bridges Y1-Y3' false. The proof covers only identifications that carry the Wilson link to an operator covariant under the law's bounded site generators (`GA2_Y2_REFEREE.md` R4). Pass 1 itself leaves universality descriptions open."
- **E2 (line 11).** Delete "Pass 2 by Codex, model `gpt-6.1-terra` as named in the task; effort and session ID not visible." The lead's run-log sentence before it supersedes it.
- **E3 (line 19).** Replace "These are state-dependent and not gauge-invariant diagnostics." with: "These are state-dependent. `κ` is not gauge invariant. `D_ω(Y)` is unchanged by every gauge unitary that commutes with `Y`."
- **E4 (line 20).** After "an identification ι with commuting Wilson functions", insert: "multiplicative on the listed products, both orders of a product going to the same commuting product, with `ι(O^†)` the complex conjugate of `ι(O)`". Four-test check in R7(a).
- **E5 (line 34).** Replace "A compact Lie subgroup of U(N) with infinite image has positive-dimensional identity component, hence nonzero differential. Differentiate the group covariance." with R7(b).
- **E6 (line 36).** Replace "the norm bound excludes uniform operator-norm convergence under a common covariant identification" with: "under the embeddings `|m⟩ ↦ e_m` into `ℓ^2(ℤ)` or `ℓ^2(ℤ + ½)`, `‖J_S/c − B‖ ≥ 1` for every `c > 0`, since `J_S|S⟩ = 0`; so no rescaling of `J_S` converges in operator norm to the bilateral shift `B`".
- **E7 (line 46).** Replace "This is the precise content of Y2-0;" with the statement of R4 (i)-(iii) and its scope paragraph. Add: "Corollary 2.4 holds for every bounded coarse generator, including a finite sum over a block (`GA2_Y2_REFEREE.md` R3(a)). It fails for an unbounded summed-flux generator (R3(b))."
- **E8 (line 76).** Before "while ω(N^xN^y)=5", insert the computation of R7(d). Replace "yielding M=15" with "yielding ω(M)=15".
- **E9 (lines 82 and 143).** Line 82: replace "For the proposed L5-U[ρ] datum" with "For the L5-U[ρ] datum (recorded in pass 1, not proposed)". Line 143: replace "Proposed alternative to the fixed rishon register" with "Recorded alternative to the fixed rishon register (pass 1: 'recorded, not proposed')".
- **E10 (line 141).** Replace "Corollator" with "Correlator".
- **E11 (line 24).** Add: "This corrects `Y2W_DRAFT.md` line 159, which used `8ε_µ(g_*) + 6δ` for the cube family. Theorem 3.1 needs the small-field bound of the listed observable's own image. By `GA2_Y2_REFEREE.md` R1, `ε_Θ ≤ 36ε_µ`."

**Optional edits** (precision only; the lead decides):
- **O1.** Theorem 3.1, Corollary 3.3 and Definition 8: the constant 8 may become 4, by R1(a). Thresholds then read `4ε + 6δ`.
- **O2.** Line 9: list only `ε_µ` as the open small-field bound, citing R1 for `ε_Θ`.
- **O3.** Line 32: write "`[E,U]=qU`, `E` Hermitian, `q ≠ 0`", or add the trace proof `q · dim = 0`.
- **O4.** Line 62: write "Let `E` be self-adjoint with spectrum in `K` consecutive integers".
- **O5.** Line 66: write "The total variation is at least `2 max p_j ≥ 2/K`."
- **O6.** Line 99: add "`SZ` and `ZS` are the two transpositions other than `S`, so `SZ + ZS = −S` on that sector."
- **O7.** Line 110: add "Links off the block edges carry any fixed vector." Line 124: write "κ = 0 on every skeleton link".
- **O8.** Line 9: write "Y2-W-L0 is decided under each named reading (Theorem 4.3); the choice of reading is open."

---

## 5. Open statements to carry by name

Each is open after this referee pass. The attacks named are those recorded in pass 1; this pass ran none against them.

- **Y1, Y2, Y3, Y4, Y5/GA2-i.** The bridges of `TOE_ASSEMBLY.md` section 6.
- **ZM1-G.** A specified block map and a controlled comparison of gauge-invariant correlators with a reflection-positive group-valued measure, at every scale of GA2's window. R2(c) shows this, with T0-rate, is what gives GA2(a).
- **VC1.** The state. Y2-W-L under reading S, and any argument from one scale (R2(b)), need its properties.
- **GA1-P.** The plaquette class, open law data.
- **Y2-W** (`L5-U`). Pass 1's three attacks failed at "every loop that sees `SU(5)` raises a bounded grading", "the corner is classical" and "the block state is close to a product of aligned coherent states" (`Y2W_DRAFT.md` section 3).
- **Y2-W-L.** Under S: zero defect in an explicit state (Theorem 4.4); a decision needs the VC1 state. Under B: fails for `m ∈ {1, 2, 8, 9}` (Theorem 4.5), given Theorem 3.1's hypotheses.
- **Y2-W-LB(m), `m = 3, …, 7`.** Pass 1's three attacks failed at "the eight octants at `x` keep antisymmetric active parts", "in every sector some end is empty or full" and "the corner operators are polynomials in the permutations of three one-rishon ends" (`Y2WL_DRAFT.md` section 4.3).
- **Y2-W[`L5-O`].** The coupling part, with Y1, Y3 and T0-start for `SO(10)`.
- **The reading of the cube observable** (F, S or B). Owner decision. Y2-W-L0 is decided under each reading (Theorem 4.3).
- **The band-limited kernel question.** Its comparison with the hard-core class (R6 shows band-limitation alone decides nothing).
- **`ε_µ` for the T0-start class.** The plaquette small-field bound. `ε_Θ ≤ 36ε_µ` (R1), so `ε_Θ` is no longer a separate open item.
- **T0, T0-start[G], T0-rate, T0-QLR[G], T0-D[G].** Requests to the YM programme; none is proved.

## 6. Freeze recommendation

**Freeze `GA2_Y2.md` after edits E1-E11.** All sixteen theorems and corollaries (2.1-2.5, 3.1-3.5, 4.1-4.6) are correct as stated, with the notes in section 1. The seven ERROR items are attributions, wording and one typo. The four INCOMPLETE items have complete closures in R7. Optional edits O1-O8 sharpen statements and may be applied at the lead's discretion. R1-R6 may be cited from this file or copied into `GA2_Y2.md` with credit. Before or with the freeze, the lead may wish to correct `TOE_ASSEMBLY.md` line 552 (FINISH, downstream item 2).

## 7. Scratch checks (guides only)

All in `/tmp/toe-ga2ref/` on the Mac mini. Python 3 with numpy 2.4.1 and scipy 1.17.0; floating point. Each started with 62-63 percent of memory free. The sparse and small scripts used a few MB each and ran under one minute. `link.py` held dense `1024 × 1024` real matrices, an estimated 0.7-0.8 GB at peak (not measured), and ran 69 s, over the one-minute limit. Its sparse reruns `link2.py` and `link3.py` (under 1 s each) are the checks reported. `major.py` paired the Majoranas so that `U^{aa}` was not diagonal; its joint-eigenvector test is void, and `major2.py` replaces it.

| Script | What it showed | Time |
|---|---|---|
| `geom.py` | The face-step table of `Y2WL_DRAFT.md` section 4.2 from `ν × n̂`: all 12 rows agree. Corner types: four corners with one particle end and four with two, for all 720 orders. `S∞` parity rule: 8 compatible orders for each lowest-corner parity, `e_3 < e_1 < e_2` faces for even and the reverse for odd. Fixed translated order: no order makes the four cubes at an `e_1`-link agree. | 0.07 s |
| `lower.py` | Every link occupied at its lower end: 0 of 720 orders compatible; 0 already on the four `e_1`-edges. | < 1 s |
| `link.py` | First version of the one-link checks; results as below; 69 s, over the limit. | 69 s |
| `link2.py` | One `L5-U` link (10 modes, 1024 dimensions, sparse): the two identities of Theorem 4.1 and the product formula of Theorem 2.5 exact; `rank 𝐔 ≤ C(10, m+1)` in every sector (25, 100, 200, 250, 210, 120, 45, 10, 1); `M = 5m − 2N^xN^y` exact; `min M ≥ m(10−m)/2`; `(U^{jk})^2 = 0`. | 0.9 s |
| `link3.py` | Random states: largest `κ` 0.1 at `m = 1, 9` and below 0.05 elsewhere (bound 1/2). Slater state, random `V`: singular values all 0.5, `⟨N^xN^y⟩ = 5`, `⟨M⟩ = 15`, `κ = 0.166667`, `ω(𝐔) = −V^†/2` exactly. Particle-hole map: `CrC^† = −r^†`, `CUC^† = −U^†`, `N ↦ 10 − N`, all exact. | 0.25 s |
| `corner.py` | Lemma R operators on `(ℂ^5)^{⊗3}`: zero on symmetric states; 4 (one particle end) and −2 (two) on antisymmetric states, also for adjoints; two-particle operators idempotent on the remaining sector. Theorem 4.5 Step 2 with `R_i = 1`: largest ratio 0.48 over 3000 random `(c, ψ)` against the proved 18. Theorem 3.2: smallest eigenvalue above `2/K^2` for 300 random graded shifts at each `K = 2, …, 6`. R1: largest ratio 0.28 on random draws; at equal small angles the ratio tends to 1. | 2.0 s |
| `major.py` | `L5-O` Majorana links: `rank 𝐔` equals the half-spinor dimension for `N = 2, …, 5`; at `N = 10`, `(U^{ab})^2 = 1`, rows anticommute, `(𝐔^†𝐔)^{ab} = Nη^x_aη^x_b`, all exact. Joint-eigenvector test void (see above). | 0.3 s |
| `major2.py` | With `η^y_a, η^x_a` paired in mode `a`: `U^{aa}` diagonal; joint eigenvectors in both chiralities give `κ = 0.1` and zero end bilinears; random states in one chirality give `κ ≤ 0.003`. | 0.2 s |

File hashes were checked with `shasum -a 256`.

---

## FINISH

**Proved here (pass 3; author check, not independent review of this report).**
- The verdicts of section 1: 75 items, 64 CORRECT, 7 ERROR, 4 INCOMPLETE. Every theorem and corollary of `GA2_Y2.md` (2.1-2.5, 3.1-3.5, 4.1-4.6) was re-derived and holds as stated, with the notes.
- R1: for `|w_f| ≤ 1`, `|1 − w|^2 ≤ 2(1 − Re w)` and `1 − Re Π_{f=1}^{k} w_f ≤ k Σ_f (1 − Re w_f)`. Hence `ε_Θ ≤ 36ε_µ`, and Theorem 3.1 holds with `4ε + 6δ`.
- R2: SC(`r`; `δ`) depends only on `ω` restricted to its list's links. The lower-end flux completion `ω_φ` keeps SC and makes every flux-raising loop and every boundary cube product outside those links vanish, with `D ≥ 2`. GA2(a) on a set `𝒪` follows from ZM1-G on `𝒪` at every scale of the window plus T0-rate.
- R3: Corollary 2.4 holds for every bounded coarse generator, including any finite block sum. In a representation of the `L5-U` link algebra, the summed end number over infinitely many links has an exactly covariant unitary raising operator.
- R4: Corollary Y2-0 stated precisely, with its scope.
- R5: product Slater states with coherence `k/(k+5)` on every link and a plaquette with `ω(W_p) = 0`, so `D(cW_p) ≥ 2` for every `c`.
- R6: band-limited kernels can be nonnegative (Fejér) or not (Dirichlet).
- R7: complete closures of the four INCOMPLETE steps, and the four-test check of the clause added to Definition 4.

**Counterexamples.**
- To the pass-1 argument that SC at one scale gives GA2(a) (`Y2W_DRAFT.md` line 58), as an argument from SC and `µ` alone: R2(b). It does not refute GA2 for the VC1 state. It does not cover an argument that uses translation invariance.
- To extending Corollary 2.4 from bounded generators to an unbounded infinite-block generator: R3(b).
- To reading per-link coherence near one as small coupling: R5.
- To `GA2_Y2.md` line 7's attribution: pass 1 left universality descriptions open (`GA2_Y2_DRAFT.md` line 134).

**Open, by name.** Y1, Y2, Y3, Y4, Y5/GA2-i; ZM1-G; VC1; GA1-P; Y2-W (`L5-U`); Y2-W-L; Y2-W-LB(m) for `m = 3, …, 7`; Y2-W[`L5-O`]; the reading of the cube observable (F, S or B; owner decision); the band-limited kernel question; the plaquette bound `ε_µ` for the T0-start class; T0, T0-start[G], T0-rate, T0-QLR[G], T0-D[G]. The attacks recorded for them are listed in section 5. No law is excluded. Both five-mode laws stay live under `TOE_ASSEMBLY.md` section 3.5: "The owner chose: **keep both live.**"

**What changes downstream.**
1. `GA2_Y2.md`: apply E1-E11, then freeze (section 6).
2. `TOE_ASSEMBLY.md` line 552 reads: "This holds at every scale of the law (Corollary N5). So the clause "That is T0's theory up to bridges Y1-Y3" is false for every PS-6r law, and Y2 can hold only as universality of gauge-invariant correlators." By R3 and R4 this claims more than is proved. Proposed wording for the lead: "This holds for every bounded coarse generator, including any finite block, and not for unbounded limits. So the clause cannot hold through an identification of the Wilson link with an operator covariant under the law's bounded site generators. Y1-Y3 remain open for Euclidean variables, for gauge-invariant correlators and for actions with unbounded generators." This wording only narrows a claim to what R3 and R4 prove. Four-test check: it names no target (1, pass); it is closed (2, pass); it settles no downstream question by premise (3, pass); it adds no structure or constant (4, pass). The lead decides; nothing is adopted here.
3. The request to the YM programme needs only the plaquette bound `ε_µ`, since `ε_Θ ≤ 36ε_µ` (R1).
4. GA2 needs ZM1-G at every scale of its window (R2(c)). SC at one scale is a consequence of ZM1-G, not a route to GA2, unless further properties of the VC1 state are used (R2(b)).
5. Y2-W-L under S: in states that agree with any given state on any finite region, every boundary cube product outside that region can vanish (R2(b)(iii)). So a decision of Y2-W-L under S must use global properties of the VC1 state. This agrees with `GA2_Y2.md` line 149.
6. Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
