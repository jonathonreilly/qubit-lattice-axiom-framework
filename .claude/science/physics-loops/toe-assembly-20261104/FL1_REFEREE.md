lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# FL1 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 of part FL1 of the TOE assembly, under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the item is frozen. This session wrote neither pass 1 (`FL1_DRAFT.md`) nor pass 2 (`FL1.md`). It is one check: a single line-by-line read of `FL1.md`. It reviews no other review.

**What this file is.** A referee report. It grants no status. It adopts no law, reading or specification. It changes no axiom and no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. `FL1.md` is not edited. "[check]" marks a tiny scratch computation: `check_ref.py`, `check_grp.py` and `check_d3.py` in `/tmp/toe-fl1ref/scripts/`. They use floating point on a periodic `8^3` torus, exact integer enumeration in `O`, and `2×2` matrices. Each runs in under 1 s with peak memory under 90 MB. A check guides and never proves.

**Text read.** `FL1.md` at commit `cb26a5345`, the commit that adds it and the branch head when read. The lead's later commits (branch head `c2bfcd143` when this report was finished) leave `FL1.md`, `FL1_DRAFT.md` and every source file cited below from this folder unchanged. SHA-256 `611b593b4f8eac7df60f74c79e24dacd9dbf673c44901568abd17b05b699c011`. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| this checkout, branch `claude/toe-assembly` | `cb26a5345` |
| `origin/claude/toe-family-count-5mode-20261021`, the #10022 note (read with `git show`) | `8b8db34725` |
| `origin/claude/toe-families-from-tastes-20261021`, the #10016 note (read with `git show`) | `f2bc19c248` |
| `origin/docs/consolidate-families-flavour`, the #10129 synthesis (read with `git show`) | `d78b2ebed5` |

Files read, by line. This folder: `FL1.md` lines 1-116 (all); `FL1_DRAFT.md` lines 1-308 (all; its SHA-256 `bcc9761649e8ebca5e7d49551521b28be19ecaf5ab3ac934829844d9d9eaa837` equals the hash `FL1.md` records); `LW1_REFEREE.md` lines 1-238 (for the format only); `Y2W_DRAFT.md` lines 1-30 (the head format); `LW1.md` lines 40-46, 186, 209-216 (A1, A2), 322-350 (B10), 371-390 (C1); `LW1_5.md` lines 205 and 253-269 (A2-5, B1-5, B1-U) and 322 (section 7.1), with grep hits at lines 7, 11, 39, 46, 72, 80, 85, 97 and 132-211 read in passing; `CH1.md` lines 7-17, 26-34, 127-135, 169-181 and 215-237; `CH1_5U.md` lines 3-11, 59-62 and 89-127; `TOE_ASSEMBLY.md` lines 180, 214, 431 and 445. The #10022 note (`docs/THE_LIGHT_COPY_CARRIES_A_NONZERO_TURN_CHARGE_SO_A_SYMMETRICALLY_GAPPED_MIRROR_NEEDS_FAMILY_COUNT_ZERO_MOD_THREE_BOUNDED_THEOREM_NOTE_2026-10-22.md`) lines 1-90. The #10016 note line 29. The #10129 note lines 19 and 392-396. `AGENTS.md` (all) and `docs/ai_methodology/SCIENCE_WORKFLOW.md` lines 170-200. Pass 1's scratch folder `/tmp/toe-fl1` was not read; the checks it reports were redone in `/tmp/toe-fl1ref`.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The two laws, PS-1c and the conditional premises IR-P, V0 and AM-turn are read plainly. No hostile meaning is read into them.

**Working-set entries used, by name.** PS-1 read by PS-1c, only to judge Corollary 4.2 and GAP A2. PS-5 (five modes per site), for the five complex flavours. PS-6 and PS-6r, only through the laws `L5-O` and `L5-U` of `LW1_5.md` section 2; both are live (`TOE_ASSEMBLY.md` line 214: "The owner chose: **keep both live.**"). No other entry is used.

**Results used, by name.** Frozen `LW1.md` A1, A2, B10 and C1. Frozen `LW1_5.md` A2-5, B1-5, B1-U and section 7.1. Frozen `CH1.md`: the domain sentence of Amendment 2 (line 9), definition 4, the family `F_t`, the arithmetic paragraph at line 179, CH1-5U-i and CH1-5O-i. Frozen `CH1_5U.md` Theorems 3.2-3.4. Each use is quoted where it occurs. Standard mathematics used and rebuilt where it is used: Lagrange's theorem; normal forms in groups given by generators and relations; the sign rule for reordering anticommuting factors; that a rotation by an angle in `(0, π)` determines its oriented axis (item 24); that an element of `SU(2)` over a quarter-turn has fourth power `−1` (section 4.4). Standard mathematics cited, not rebuilt, in one remark only (section 4.4): the presentation `⟨s,t | s^2=t^3=(st)^4=1⟩` of `O`. No theorem below depends on it.

**Method.** Every proof in `FL1.md` was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix); INCOMPLETE (a named missing step, with the step supplied). A "referee closure" is a complete short argument written here. Quotes from other files are exact.

**Counts.** 72 items: 66 CORRECT, 2 ERROR, 4 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. All seven GAPs the distiller marked are real. Section 3 gives a proof or a counterexample for four of them. It confirms that the other three need nothing further before a freeze.

---

## 1. Verdict table

| # | Item (FL1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status sentence (5) | CORRECT | Both laws are live, as quoted in the head. |
| 2 | §0 "Proved" list (7) | CORRECT | Each listed result is proved below, within its hypotheses. Optional: "two Weyl tastes of each handedness" should say "per complex flavour", as Theorem 7 does. |
| 3 | §0 GAP summary (9) | CORRECT | Each listed gap is real (section 3). One entry names no pass-1 claim: the draft says "It is data, not a phase" (draft Corollary D). So "that abstract data are phases" is not a pass-1 gap. |
| 4 | §0 "Open by name" (11) | CORRECT | FL1's target is `N_f = 3` (`TOE_ASSEMBLY.md` line 431), so "exactly three" is right. |
| 5 | §0 Provenance (13) | CORRECT | The recorded draft hash matches. `58586b850` is the parent of `cb26a5345`. Optional: merge the lead's run-log sentence with the distiller's "not exposed" sentence. |
| 6 | Def 1: cell group, turn, inverter (17) | CORRECT | Matches `LW1.md` line 43. |
| 7 | Def 2: canonical sign lift (18) | CORRECT | Matches `LW1_5.md` line 255, "with the lifts conjugated by \(W\) for \(L5\)-O", and line 257, "Site parity implements LW1's sign lift." [check]: `Wβ_{η_0}W^*` has purely imaginary entries, and `Wβ_{γ_0}W^* = β_{γ_0}`. |
| 8 | Def 3: light content and count (19) | CORRECT | Matches `CH1.md` lines 233 and 235. |
| 9 | Def 4: IR-P (20) | CORRECT | `U(z) = −1` presumes that `z` lies in the represented group. Read that group as generated by the lifts and `z`. |
| 10 | Def 5: turn charges (21) | CORRECT | The order-3 choice removes the sign freedom, since `−Λ_γ` has order 6. |
| 11 | Def 6: V0 and AM-turn (22) | CORRECT | Matches #10022 lines 73-74: "the light 't Hooft vertex (4N left-handed zero modes) must be invariant under the kept turn." |
| 12 | Def 7: realizing `N` families (23) | CORRECT | |
| 13 | Def 8: light at the free tick (24) | CORRECT | B10 gives a gap at `π`, so zero is the only light quasienergy. |
| 14 | Four-test record (26) | CORRECT | It reports the draft's tables (draft sections 1.3, 5, 6 and 7) accurately. |
| 15 | Theorem 1, statement (30) | CORRECT | |
| 16 | Theorem 1, proof: form of `Q` (32) | INCOMPLETE | Missing: why `Q` has order three, and why it equals `DP^{±1}D^{-1}`. Supplied in section 2.2. |
| 17 | Theorem 1, proof: translation condition and fixed point (32) | CORRECT | `(I−P)(0, t'_2, −t'_1) = (t'_1, t'_2, t'_3)` when `t'_1 + t'_2 + t'_3 = 0`. |
| 18 | Theorem 1, proof: the `D` and `P^{-1}` cases (32) | CORRECT | `I − P^{-1} = −P^{-1}(I − P)`, and `D`, `P^{-1}` preserve the integer vectors of coordinate sum zero. |
| 19 | Theorem 1, proof: the inverter `η` (32) | CORRECT | Implicit last step: `ηγη^{-1}` and `γ^{-1}` both fix `p` and have linear part `Q^{-1}`, so they are equal. |
| 20 | Theorem 2, statement (34) | CORRECT | [check]: `O` has 30 subgroups; 4 contain `P`; the two with no inverter of `P` have orders 3 and 12. |
| 21 | Theorem 2, proof: possible orders; order 24 (36) | CORRECT | |
| 22 | Theorem 2, proof: order 6 (36) | CORRECT | Implicit step: index two makes `⟨Q⟩` normal, so `hQh^{-1} ∈ {Q, Q^{-1}}`. |
| 23 | Theorem 2, proof: order 12 (36) | CORRECT | `R = (R^{-1})^2` for `R` of order 3; a coordinate half-turn is the square of a quarter-turn. |
| 24 | Theorem 2, proof: `T` has no inverter (36) | INCOMPLETE | Missing: an inverter must map the axis line of `Q` onto itself. Supplied in section 2.2. |
| 25 | Theorem 3, statement (38) | CORRECT | |
| 26 | Theorem 3, proof (40) | CORRECT | The face products agree because both sign fields have product `−1` on every face (`LW1.md` line 186: "Every unit face has sign product \(-1\)."). |
| 27 | GAP S1 / covariance (42) | CORRECT | Real for the dressed tick. Referee closure for both free walks in section 3.1. |
| 28 | Example: turn sign (44) | CORRECT | Hand check of the three edge ratios and of the cube; [check]. |
| 29 | Example: inverter sign and its square (44) | CORRECT | Hand check; [check]. |
| 30 | Reported half-turn checks (44) | CORRECT | Hand check; [check]. `FL1.md` does not display these maps, though Theorem 8 needs the edge half-turn (item 53). |
| 31 | Theorem 4, statement (48) | CORRECT | |
| 32 | Theorem 4, proof (50) | CORRECT | `S^{-1}TS = T^{-1}` follows from `STS^{-1} = T^{-1}`, so both inclusions hold. |
| 33 | Corollary 4.1, statement (52) | CORRECT | "the indicated ... sums" points to nothing in `FL1.md`. Optional: name them (`w = dim r`, `w = 2T_i(r)`, and the signed count of García-Etxebarria–Montero eq. (4.10)). |
| 34 | Corollary 4.1, proof (54) | CORRECT | Its instanton input stays cited, as the text says. |
| 35 | Normalizing-inverter extension (56) | CORRECT | `(Sφ)∘r(σ^{-1}(h)) = ρ(h)∘(Sφ)`, so `Sφ ∈ M_{r∘σ^{-1}}`; reindexing is a bijection of irreducibles. |
| 36 | Corollary 4.2, statement (58) | CORRECT | |
| 37 | Corollary 4.2, proof (60) | CORRECT | |
| 38 | GAP A2 scope (62) | CORRECT | Real. Referee counterexample in section 3.2. #10022 line 52, retrieved here: "The copy mass keeps exactly the 12 tetrahedral rotations, including all 8 three-fold turns." |
| 39 | Theorem 5, statement (64) | CORRECT | |
| 40 | Theorem 5, proof (66) | CORRECT | `CH1.md` line 179: "It contains four weak doublets." |
| 41 | GAP in FL1-i(3) (68) | CORRECT | Real. Repaired statement in section 3.3. |
| 42 | Theorem 6, statement (70) | CORRECT | |
| 43 | Theorem 6, proof (72) | INCOMPLETE | Missing: the listed relations present the lift group. Without that step, "satisfy the relations" does not define a homomorphism. Supplied in section 2.2. |
| 44 | Paragraph after Theorem 6, with GAP D (74) | CORRECT | Quotes checked: `CH1_5U.md` lines 89, 95-96 and 101; `CH1.md` line 179. GAP D is real (section 3.4). |
| 45 | Theorem 7, statement (78) | CORRECT | |
| 46 | Theorem 7, proof: band formula and bounds (80) | CORRECT | `LW1.md` lines 324-325 and 344. |
| 47 | Theorem 7, proof: `V(0) = I`, logarithm, `h^2 = w^2 I` (80) | CORRECT | `h^2 = w^2 I` uses B10 (1), "The Bloch eigenvalues are \(e^{\pm iw(K)}\)". Cite it. |
| 48 | Theorem 7, proof: Clifford relations (80) | CORRECT | `LW1.md` line 383 gives `w^2 = s_ε^2 k^2/3 + O(k^4)`, with `k` the cell momentum. [check]: anticommutator error `6·10^{-9}`. |
| 49 | Theorem 7, proof: `χ_c` and `Θ` (80) | CORRECT | `LW1.md` line 348: "Hence \(\Theta V\Theta^{-1}=V\)." `Θ` maps the fibre at `K` to the fibre at `−K`. |
| 50 | Theorem 7, proof: block forms and handedness (80) | CORRECT | [check]: chirality eigenvalues `4 + 4`. The four nodes share one 8-dimensional eigenspace. So they are not regular nodes in the sense of `CH1.md` definition 4, which needs "an isolated two-dimensional eigenspace". The text uses only the linearized blocks and their velocity determinants, as it says. |
| 51 | Theorem 7, proof: transfer to O (80) | CORRECT | `LW1_5.md` line 322: "so it shifts cell momentum by \((\pi,\pi,\pi)\) as well as changing the residue basis." |
| 52 | Theorem 8, statement (82) | CORRECT | The proof treats `γ_0` and `η_0`. Every turn is conjugate to `γ_0` in `𝒢` (section 2.2), so the statement holds for every turn. Add that sentence. |
| 53 | Theorem 8, proof: covariance and period two (84) | INCOMPLETE | The edge half-turn and its sign are not displayed. That it generates `O` together with `γ̄_0` is asserted, not shown. Supplied in section 2.2. |
| 54 | Theorem 8, proof: spin generators and factorization (84) | CORRECT | `−(i/4) Σ ε_{kij} γ_i γ_j = σ_k/2` on both blocks. The commutant of `(M_2⊗1) ⊕ (M_2⊗1)` is `(1⊗M_2) ⊕ (1⊗M_2)`. |
| 55 | Theorem 8, proof: trace (84) | CORRECT | The signs have period two, so the signs at residues `000` and `111` equal those at the fixed sites `(0,0,0)` and `(1,1,1)`. [check]: trace 2. |
| 56 | Theorem 8, proof: pairing and spectrum (84) | CORRECT | [check]: on each block `U(β̂_{γ_0})` has eigenvalues `{1, 1, ω, ω̄}`. That is `Λ_3 ⊗ τ` with `τ` of spectrum `{ω, ω̄}`. |
| 57 | Theorem 8, proof: transfer to O (84) | CORRECT | [check]: `Wβ_{γ_0}W^* = β_{γ_0}`, and `Wβ_{η_0}W^*` is `i` times a real signed permutation. A global phase leaves the pairing intact. |
| 58 | Paragraph after Theorem 8, with GAP B5 (86) | CORRECT | Real (section 3.6). |
| 59 | Theorem 9, statement (90) | CORRECT | |
| 60 | Theorem 9, proof (92) | CORRECT | `LW1.md` line 215: "A rotation about a site must fix the centre of its even cube; its stabilizer consists of the identity and the two turns about that body diagonal." |
| 61 | Corollary 9.1 and proof (94-96) | CORRECT | |
| 62 | GAP C4 (98) | CORRECT | Real. Draft (C4) says "None of these structures is light", but its proof treats only the momentum triples. |
| 63 | GAP FL1-i (100) | CORRECT | Real. Repaired statement in section 3.5, with the #10129 text on the slab notes. |
| 64 | FL1-V (104) | CORRECT | |
| 65 | Attack 1 (108) | CORRECT | |
| 66 | Attack 2 (109) | CORRECT | |
| 67 | Attack 3 (110) | CORRECT | It rightly replaces the draft's "no family-realizing phase exists" (draft FINISH) by "has been constructed". |
| 68 | Proposed route: use of Theorem 5 (112) | CORRECT | |
| 69 | Proposed route: the staggered density (112) | ERROR | On `L5-O`, `n_x` is not `Spin(10)`-invariant, and every gauge-invariant state has `ω(n_x) = 5/2`. The proposed density then vanishes identically. Fix in section 2.1. |
| 70 | Proposed route: infinite-lattice reading (112) | CORRECT | |
| 71 | Proposed readings: the octahedral extension (114) | ERROR | The relations the draft states do present the point-group lift group, once the presentation of `O` is granted. Fix in section 2.1. |
| 72 | Source and search limits (116) | CORRECT | No mathematical claim. |

---

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 69 (line 112, the staggered density).** FL1: "The staggered density \(\sum_x(-1)^{x_1+x_2+x_3}n_x\) is a candidate order parameter". The sentence names no law. On `L5-O` it fails.

*Referee closure.* `CH1.md` line 9 states the domain: "for every gauge-invariant state of `L5-O`". Fix a site `x` of `L5-O` and write `n_{x,j} = c^†_{x,j}c_{x,j} = (1 + iγ_{x,2j−1}γ_{x,2j})/2`. For `j ≠ k`, let `R_{jk}` reverse the Majorana axes `2j` and `2k` and fix the other eight. It has determinant `+1`, so it lies in `SO(10)` and lifts to `Spin(10)`. The local gauge automorphism at `x` by that lift acts on matter at `x` by `γ_{x,a} ↦ Σ_b (R_{jk})_{ab} γ_{x,b}`. It sends `n_{x,j} ↦ 1 − n_{x,j}` and `n_{x,k} ↦ 1 − n_{x,k}`, and it fixes the other three. Let `ω` be invariant under the local gauge automorphisms at `x`, and put `a_l = ω(n_{x,l})`. Invariance gives `a_j + a_k = 2 − a_j − a_k`, so `a_j + a_k = 1` for every pair `j ≠ k`. The pairs `(1,2)`, `(1,3)`, `(2,3)` give `a_1 = a_2 = a_3 = 1/2`, and then every `a_l = 1/2`. So `ω(n_x) = 5/2` at every site. Over a finite region `F` the staggered sum has expectation `(5/2) Σ_{x∈F} (−1)^{x_1+x_2+x_3}`, which is `0` on every union of `2×2×2` cells. So on `L5-O` the density takes the same value in every gauge-invariant state and cannot detect a broken inverter. On `L5-U`, `n_x` is `U(5)`-invariant and the sentence stands.

*Fix.* "On `L5-U`, the staggered density \(\sum_x(-1)^{x_1+x_2+x_3}n_x\) is a candidate order parameter. On `L5-O`, use the staggered site parity \(\sum_x(-1)^{x_1+x_2+x_3}P_x\), \(P_x=\prod_j(1-2n_{x,j})\)." Reason: `1 − 2n_{x,j} = −iγ_{x,2j−1}γ_{x,2j}`, so `P_x = (−i)^5 γ_{x,1}⋯γ_{x,10}`. It commutes with every `γ_{x,a}γ_{x,b}`, hence with the matter action of `Spin(10)` at `x`. A canonical lift sends `γ_{x,a}` to `d(gx)γ_{gx,a}`, so `P_x ↦ d(gx)^{10}P_{gx} = P_{gx}`. The staggered parity therefore has the same behaviour as the density: `T` fixes it and every element of `O∖T` reverses it. [check]: a rotation about `c_0` preserves the parity of the coordinate sum exactly when its linear part lies in `T`. *Four-test check of the replacement* (recorded, not adopted): (1) pass, it fixes no part's target and no value of `N`; (2) pass, it is one specified operator; (3) pass, whether its expectation is nonzero stays VC1's question; (4) pass, `P_x` is already an operator of the law, and nothing new is added.

**Item 71 (line 114, the octahedral extension).** FL1: "Pass 1 reports \(\pi^4=z\) for the displayed quarter-turn and cites \(O=\langle s,t\mid s^2=t^3=(st)^4=1\rangle\); these facts alone do not establish the extension without checking all lift-group relations." No further relation needs checking. Pass 1 states `a^3 = 1` (its (S3)), `β_ε^2 = 1` and `π^4 = α_P` with `π = β_ε a`. Section 4.4 shows that these relations, with `z` central of order two, present the lift group of `O_{c_0}`, given the cited presentation of `O`. Pass 1 lacks only that counting step. *Fix:* "With the counting step of `FL1_REFEREE.md` section 4.4, these relations present the lift group; the extension is then conditional only on the cited presentation of \(O\). Nothing uses it."

### 2.2 INCOMPLETE

**Item 16 (Theorem 1, the form of \(Q\)).** Supply, as in draft (G1). `γ^3 = (Q^3, (I+Q+Q^2)t) = id` gives `Q^3 = I`. If `Q = I`, then `γ^3` is the translation by `3t`, so `t = 0` and `γ = id`, against order three. So `Q` has order three. If `Q` fixed an axis line, `Qe_i = ±e_i`, and `Q` would act on the other two axes as a signed permutation of a plane, of order 1, 2 or 4. With `Q^3 = I` that forces `Q = I`. So `Q` permutes the axes by a 3-cycle: `Q = D_1P^{±1}` with `D_1 = diag(s_1, s_2, s_3)` and `s_1s_2s_3 = 1`, since `det Q = det P = 1`. For `D = diag(d_1, d_2, d_3)`, `DPD^{-1} = diag(d_1d_3, d_2d_1, d_3d_2)P`; take `(d_1, d_2, d_3) = (1, s_2, s_1)`. Also `DP^{-1}D^{-1} = diag(d_1d_2, d_2d_3, d_3d_1)P^{-1}`; take `(1, s_1, s_1s_2)`. Both give `D_1P^{±1}`.

**Item 24 (Theorem 2, \(T\) has no inverter).** Supply. Write `Q = R(2π/3, n)`, the rotation by `2π/3` about the unit vector `n`. For `h ∈ O`, `hQh^{-1} = R(2π/3, hn)`, and `Q^{-1} = R(2π/3, −n)`. A rotation by an angle in `(0, π)` determines its oriented axis: its fixed vectors span its axis line, and `R(θ, −n) = R(−θ, n) ≠ R(θ, n)`, since `R(θ, n)^2 = R(2θ, n) ≠ I`. So `hQh^{-1} = Q^{-1}` forces `hn = −n`: an inverter maps the axis line of `Q` onto itself. In `T`, the elements of `⟨Q⟩` fix `n`. A coordinate half-turn moves every body diagonal to another one; for example `diag(1,−1,−1)(1,1,1) = (1,−1,−1)`. A turn about another body diagonal permutes the remaining three diagonals cyclically, so it moves the axis of `Q`. Hence `T` contains no inverter of `Q`.

**Item 43 (Theorem 6, the presentation).** Supply, as in draft Corollary D (1). Every element of `𝒦` is uniquely `τ_t γ_0^i η_0^j` with `t ∈ 2Z^3`, `i ∈ Z_3`, `j ∈ Z_2`: the six linear parts `P^iH_0^j` are distinct, and the translation part then fixes `t`. So the canonical lifts of `𝒦` are the elements `T_t a^i b^j z^k`, each listed once. Let `G̃` be the group with generators `T_t`, `a`, `b`, `z` and relations `T_tT_s = T_{t+s}`, `aT_ta^{-1} = T_{Pt}`, `bT_tb^{-1} = T_{H_0t}`, `a^3 = b^2 = z^2 = 1`, `bab^{-1} = a^{-1}`, and `z` central. These relations hold among the lifts; the second and third use the period-two signs. They also move every word of `G̃` to a normal form `T_t a^i b^j z^k`. Distinct normal forms map to distinct lifts. So `G̃` maps isomorphically onto the lift group. A homomorphism out of the lift group is therefore fixed by images that satisfy these relations, and the proof checks exactly those.

**Item 53 (Theorem 8, the edge half-turn and generation).** Supply, as in draft (B4). The edge half-turn about `(1,1,0)` through `c_0` is `ε: x ↦ (x_2, x_1, 1 − x_3)`, with linear part `E(v) = (v_2, v_1, −v_3)` and `det E = 1`. Its sign `(−1)^{y_1y_2}` at the image passes the edge test. The edges along `e_1`, `e_2`, `e_3` at `x` have ratios `(−1)^{x_2}`, `(−1)^{x_1}`, `1`. With `y = εx`: `d(y)d(y + e_2) = (−1)^{y_1} = (−1)^{x_2}`, `d(y)d(y + e_1) = (−1)^{y_2} = (−1)^{x_1}`, `d(y)d(y − e_3) = 1`. [check]. Generation: `P` fixes the diagonal `(1,1,1)` and cycles `(1,1,−1) → (−1,1,1) → (1,−1,1)`, while `E(1,1,1) = (1,1,−1)`. So `⟨P, E⟩` is transitive on the four body diagonals, and its order is divisible by 4 and by 3. By the proof of Theorem 2, the only subgroup of order 12 is `T`. `E ∉ T`, since it has order two and is not a coordinate half-turn. So `⟨P, E⟩ = O` [check]. Each canonical lift of a rotation about `c_0` is then `±` a word in `a` and `β_ε`. Such words have period-two signs, because `g(x + 2t) = gx + 2Qt`.

**Item 52 (one sentence to add).** Every turn is conjugate in `𝒢` to `γ_0`. Item 16 gives `Q = DP^{±1}D^{-1}`; replacing `D` by `−D` when `det D = −1` keeps the conjugation inside `O`; and `P^{-1} = H_0PH_0^{-1}`. A turn about `p = c_0 + 2v` is `τ_{2v}(Q, 0)τ_{2v}^{-1}`. If `γ = gγ_0g^{-1}`, the cube-one lifts satisfy `β̂_γ = β_gβ̂_{γ_0}β_g^{-1}`. On the zero fibre an even translation acts by a scalar (`1` at `K = 0`, `±1` at `K_*`), and a proper rotation keeps both chirality blocks. So each `τ_±(β̂_γ)` is conjugate to `τ_±(β̂_{γ_0})` and has the spectrum `{ω, ω̄}`.

---

## 3. The distiller's GAPs: real or not, with repairs

### 3.1 GAP S1 / covariance (line 42): real

FL1: "Pass 1 defines *all* lifts merely as signed geometric maps commuting with the full tick, then proves uniqueness from preservation of the individual edge signs. The latter does not follow from the former". The draft's (S1) says: "Uniqueness: a site sign `d` with the required edge ratios is fixed by its value at one site". It never shows that commuting with the tick forces those edge ratios. So the gap is real. FL1 repairs it by restricting every claim to the canonical family, where uniqueness holds (Theorem 3). That restriction is enough for every theorem in FL1. For the free walks the referee closes the gap outright.

*Referee closure (free walks).* Let `0 ≤ μ < 2ε < π`, `a_e = ε − μ/2`, `a_o = ε + μ/2`. Then `0 < a_e < π/2` and `0 < a_o < π`. `LW1.md` line 186: "Both \(R_e^2\) and \(R_o^2\) equal the identity." So `V = (cos a_o + i sin a_o R_o)(cos a_e − i sin a_e R_e)`. Let `D = diag(e(x))` be a diagonal unitary with `DV = VD`. Then `(e(y) − e(x))V_{yx} = 0` for all sites `x, y`.
1. *Odd edges.* Let `(x, y)` be an edge of the odd tiling. `R_e` has no `(y, x)` entry. `R_oR_e` has none either, because two unit steps cannot give a unit displacement. So `V_{yx} = i sin a_o cos a_e (R_o)_{yx}`, of modulus `sin a_o cos a_e/√3 > 0`. Hence `e` is constant on each odd cube.
2. *Steps by `2e_i`.* Let `x_i` be even. Then `(x, x+e_i)` is an even edge and `(x+e_i, x+2e_i)` is an odd edge. `LW1.md` line 215: "From \(0\) to \(2e_i\), the sole two-step path uses an even edge then an odd edge, giving modulus \(\sin a_e\sin a_o/3>0\)." The same holds from every such `x`, since the edge signs have period two. `R_e` and `R_o` have no `(x+2e_i, x)` entry. So `V_{x+2e_i,x} ≠ 0`.
3. *Connection.* The odd cubes are `1 + 2b + {0,1}^3`. A site with `x_i` even in cube `b` has `x_i = 2b_i + 2`, and `x + 2e_i` lies in cube `b + e_i`. Each odd cube contains such a site for each `i`. So `e` is one constant on all sites.

Two lifts `D_dP_g` and `D_{d'}P_g` that commute with `V` differ by `D_{d'/d}`, which commutes with `V`. So `d' = ±d`. A Bogoliubov automorphism `c(f) ↦ c(Uf)` determines the one-body unitary `U`, so commuting at the CAR level is the same as commuting at the one-body level. For the O free walk, apply the argument to `W^*(·)W`. Hence on both free walks, every sign lift in the draft's sense is unique up to `z`, at every admissible `(ε, μ)`. This includes `a_o = π/2`, where the even-edge entries of `V` vanish. FL1's phrase "especially at exceptional parameters" therefore has no force for the free walks. [check]: the graph of nonzero entries of `V` is connected at `(ε, μ) = (0.7, 0.3)`, `(0.6, 0)` and `(1, π − 2)`. For the dressed ticks the same question is not settled here. FL1 does not need it.

*The plaquette clause.* FL1: "Nor does covariance of an unspecified plaquette layer show it preserves the same lifts without a compatibility condition." This is real. A layer can be covariant under lifts that differ from the canonical ones by gauge transformations. FL1's definition 2 states the compatibility as a separate hypothesis. That is the right repair.

*The O free walk.* FL1's GAP summary says the draft's "sign-lift definition also needs correction for the O free walk". This is real. The draft's (S1) proof says: "The construction is purely about the signs `η_i`, which are the same in `L_cube`, `L5-U` and `L5-O`." On the dressed `L5-O` law this holds: `LW1_5.md` line 257, "it sends \(U^{ab}\) to \(-U^{ba}\), while reversing the two matter Majoranas gives the other minus sign. Site parity implements LW1's sign lift." On the O free walk the link registers are c-numbers. The sign from reversing the two matter Majoranas then has nothing to cancel it. [check]: the real lift `β_{η_0}` with LW1's signs does not commute with `WVW^*`, while `Wβ_{η_0}W^*` does. Its entries are purely imaginary. So the real sign lift of `η_0` on the O free walk is `±iWβ_{η_0}W^*`, and its square is `−W β_{η_0}^2 W^* = z`. The W-conjugated lift squares to `1`. Theorem 8 is unaffected: a global phase on the inverter's lift leaves `STS^{-1} = T^{-1}`, and the turn's lift is real either way (`Wβ_{γ_0}W^* = β_{γ_0}`). FL1's definition 2 follows `LW1_5.md` line 255, "with the lifts conjugated by \(W\) for \(L5\)-O", and is consistent.

### 3.2 GAP A2 scope (line 62): real, with a counterexample

FL1: "Pass 1's assertion that a count can survive *only* in a phase whose entire kept point group is \(C_3\) or \(T\) is stronger than its proof." The draft's section 0.1 says: "A count can survive only in a phase whose kept point group is `C_3` or `T` (Corollary A2)." The implication is false, even at the level of IR-P data. Corollary 4.2 as FL1 states it, about the elements fixing `p`, is correct.

*Counterexample.* Let `g = (H_0, (2,0,0))`, the half-turn `H_0` about `c_0` followed by the translation by `(2,0,0)`. Let `𝒦 = ⟨γ_0, g⟩ ⊂ 𝒢`. Then:
1. the linear parts of `𝒦` form `D_3 = ⟨P, H_0⟩`, of order 6;
2. `𝒦` contains no inverter of `γ_0`;
3. the elements of `𝒦` that fix `c_0` have linear parts `⟨P⟩ ≅ C_3`;
4. there is IR-P data for `𝒦` in which every turn charge of `γ_0` equals `1`.

*Proof of 1-3.* Let `D_3 = {Q ∈ O : Q(1,1,1) = ε(Q)(1,1,1), ε(Q) = ±1}`. It contains `P` (`ε = 1`) and `H_0` (`ε = −1`), and it has six elements. Put `S(t) = t_1 + t_2 + t_3`. For `Q ∈ D_3`, `Q` is orthogonal, so `S(Qt) = (Q^{-1}(1,1,1))·t = ε(Q)S(t)`. On `𝒢_ℓ = {(Q, t) ∈ 𝒢 : Q ∈ D_3}` the map `Ψ(Q, t) = (ε(Q), S(t))` is therefore a homomorphism to `Z_2 ⋉ Z`, with product `(ε_1, s_1)(ε_2, s_2) = (ε_1ε_2, s_1 + ε_1s_2)`. `Ψ(γ_0) = (1, 0)`, `Ψ(g) = (−1, 2)` and `(−1, 2)^2 = (1, 0)`. So `Ψ(𝒦) = {(1, 0), (−1, 2)}`. Let `η` invert `γ_0`. The fixed line of `ηγ_0η^{-1}` is the image under `η` of the fixed line `c_0 + ℝ(1,1,1)` of `γ_0`, and `γ_0^{-1}` has the same fixed line as `γ_0`. So `η` maps that line onto itself, and (item 24) its linear part `H'` reverses its direction: `ε(H') = −1`. Write `η = (H', s)`. Then `η(c_0) = c_0 + s` lies on the line, so `s ∈ 2Z^3 ∩ ℝ(1,1,1)`. So `η` is `(H', (2k, 2k, 2k))` with `ε(H') = −1`, and `Ψ` sends it to `(−1, 6k)`. Since `6k ≠ 2`, `𝒦` has no inverter of `γ_0`. The linear parts contain `P` and `H_0` and lie in `D_3`, which gives 1. An element of `𝒦` fixing `c_0` has translation part `0`, so `Ψ = (ε(Q), 0)`, which forces `ε(Q) = 1`. That gives 3. [check]: 528 elements enumerated; point-group image of size 6; no inverter; stabilizer of `c_0` of order 3.

*Proof of 4.* The translations of `𝒦` form `Λ_𝒦 = Zα_1 + Zα_2`, `α_1 = (2,−2,0)`, `α_2 = (0,2,−2)`. Indeed `Ψ` forces `S(t) = 0` for each translation `(I, t) ∈ 𝒦`, and every `t = 2(m_1, m_2, m_3)` with `S(t) = 0` equals `m_1α_1 + (m_1 + m_2)α_2`. Conversely `g^2 = (I, (2,0,0) + H_0(2,0,0)) = (I, α_1)` and `γ_0(I, α_1)γ_0^{-1} = (I, Pα_1) = (I, α_2)`. Every element of `𝒦` is uniquely `τ_tγ_0^ig^j` with `t ∈ Λ_𝒦`, since the six linear parts `P^iH_0^j` are distinct. Take the lifts `a = β̂_{γ_0}`, `g̃ = T_{(2,0,0)}b` with `b` the inverter lift of FL1 line 44, and `z`. Then `a^3 = 1`, `g̃^2 = T_{(2,0,0)}T_{H_0(2,0,0)}b^2 = T_{α_1}`, `aT_ta^{-1} = T_{Pt}` and `g̃T_tg̃^{-1} = T_{H_0t}`. Also `gγ_0g^{-1} = (P^{-1}, (I − P^{-1})(2,0,0)) = τ_vγ_0^{-1}` with `v = (2,0,−2) = α_1 + α_2`. Both `g̃ag̃^{-1}` and `T_va^{-1}` lift this turn and have cube `1`, since `(I + P^{-1} + P^{-2})v = S(v)(1,1,1) = 0`. So `g̃ag̃^{-1} = T_va^{-1}` by Theorem 3. With `z` central of order two, these relations give the normal form `T_ta^ig̃^jz^k` and present the lift group, as in item 43.

Let `χ` be the character of `Λ_𝒦` with `χ(α_1) = χ(α_2) = ω`. It is invariant under `P` and `H_0`: `Pα_1 = α_2`, `Pα_2 = −α_1 − α_2`, `H_0α_1 = α_1`, `H_0α_2 = −α_1 − α_2`, and `ω^{-2} = ω`. Pick `Λ_3` of order three over `P`, `λ ∈ SU(2)` over `H_0` (so `λ^2 = −1`), and `s = iω̄` (so `s^2 = −ω`). Put `U(a) = Λ_3 ⊗ ω`, `U(g̃) = λ ⊗ s`, `U(T_t) = 1 ⊗ χ(t)`, `U(z) = −1`, with the scalars acting on any light content `W`. The relations hold: `U(a)^3 = 1`; `U(g̃)^2 = λ^2 ⊗ s^2 = 1 ⊗ ω = U(T_{α_1})`; `U(g̃)U(a)U(g̃)^{-1} = λΛ_3λ^{-1} ⊗ ω = Λ_3^{-1} ⊗ ω`, while `U(T_v)U(a)^{-1} = Λ_3^{-1} ⊗ χ(v)ω̄ = Λ_3^{-1} ⊗ ω`, because `χ(v) = ω^2 = ω̄`; the translation conjugations hold because `χ` is invariant; `−1` is central. Here `λΛ_3λ^{-1} = Λ_3^{-1}` because both have order three over `P^{-1}`. The internal factors are scalars, so they commute with `ρ(G_∞)`. So IR-P (a)-(c) hold, and `τ(β̂_{γ_0}) = ω`: `n_r(1) = dim M_r` and `n_r(2) = 0` for every `r`. [check] (`check_d3.py`): explicit `Λ_3` and `λ` lie over `P` and `H_0`, and the three relations hold. It is data, not a phase. Under V0, with `W = F ⊗ C^N`, Theorem 5 then gives `N ≡ 0 (mod 3)` with kept point group `D_3`.

*Repair.* Keep Corollary 4.2 as written. In GAP A2, replace "is stronger than its proof" by "is false: `FL1_REFEREE.md` section 3.2 gives a kept group with point group `D_3`, no inverter, and IR-P data with all turn charges `1`." Replace "Pass 1 reports #10022's copy mass preserves exactly \(T\); that source was not independently retrieved here" by the quote from #10022 line 52 given in item 38.

### 3.3 GAP in FL1-i(3) (line 68): real, repaired

The draft's Theorem FL1-i item 3 says: "Under V0 it selects `N ≡ 0 (mod 3)` exactly when the phase's kept point group at the turn's centre is `C_3` or `T` and all copies carry one common nonzero charge". The "only if" half is false. On `L5-U`, give every copy of `R_u` the charges `(q_{10}, q_{\bar5}, q_1) = (0, 1, 0)`. Under the weak `SU(2)` the `10` has `2T = 3` and the `\bar5` has `2T = 1`. So `v(F) = 3·0 + 1·1 = 1 ≢ 0`, and V0 forces `N ≡ 0 (mod 3)` with no common charge on the family. The repaired statement follows.

*Proposition (repaired FL1-i(3)).* Assume IR-P for a kept turn `γ`, `W = F ⊗ C^N`, and a copy-blind turn, `T = T_F ⊗ 1_N`, with `T_F` commuting with `G_∞` and `T_F^3 = 1`. Put `v(F) = Σ_r 2T(r)(n^F_r(1) − n^F_r(2)) mod 3`. Then V0's congruence holds exactly when `N·v(F) ≡ 0 (mod 3)`. So V0 forces `N ≡ 0 (mod 3)` exactly when `v(F) ≢ 0 (mod 3)`. In that case `𝒦` contains no inverter of `γ`, and the linear parts of the kept elements fixing any even-cube centre fixed by `γ` form `C_3` or `T`. One common nonzero charge `q` gives `v(F) ≡ 4q̂ ≢ 0`, which is Theorem 5.

*Proof.* `M_r(W) = M_r(F) ⊗ C^N`, and `T` acts there as `T_F ⊗ 1`. So `n^W_r(q) = N n^F_r(q)` and `v(W) = N v(F)`. If `v(F) ≢ 0`, it is invertible mod 3, and `N v(F) ≡ 0` exactly when `N ≡ 0`. If `v(F) ≡ 0`, the congruence holds for every `N`. If `v(F) ≢ 0`, some `r` has `n_r(1) ≠ n_r(2)`. Theorem 4 then excludes an inverter, and Corollary 4.2 gives the stabilizer. ∎

Copy-dependent turns are covered by Theorem 5's second clause. The sentence of FL1 line 68 then becomes a proved statement: "`C_3` or `T` at the fixed centre is necessary; under V0 with a copy-blind turn the count is forced exactly when `v(F) ≢ 0`."

### 3.4 GAP D (line 74): real; carried open

The draft's Corollary D says the data make "every anomaly condition on file vanish", and its section 0.1 says "anomaly matching on the laws' exact symmetries does not fix `N_f`". Neither is proved. Mixed anomalies of the inverter's lift, of the translations or of the whole crystalline group with the gauge group are not computed. The matching of light data to the lattice is a premise (V0, AM-turn), not a theorem. What is proved is Theorem 6 together with the per-family checks quoted in item 44. FL1 already states only that. No repair is needed for the freeze. If FL1 later wants the stronger sentence, it is the open statement GAP D.

### 3.5 GAP FL1-i (line 100): real, repaired

The draft's Theorem FL1-i concludes: "So none of the three candidates on file ... fixes `N_f` on either law." The draft never defines "a carrier fixes `N_f`". Its proof establishes the free and conditional facts only. No family-realizing phase is known, so a statement quantified over such phases cannot rest on those facts. The gap is real. The proved content is the following.

*Theorem (repaired FL1-i).* On `L5-O` and on `L5-U`:
1. per complex flavour, the free walk has two linearized Weyl nodes of each handedness at `μ = 0` and no zero node at `μ > 0`; in each handedness the two tastes carry turn charges `1` and `2`, and no line of the taste space is kept by both `γ_0` and `η_0`;
2. in every phase satisfying IR-P whose kept group contains a turn and an inverter of it, every turn-odd weighted sum vanishes, for every `N`;
3. for every `N ≥ 1` the following hold together with family count `N`: IR-P (a)-(c) for `𝒦 = 2Z^3 ⋊ ⟨γ_0, η_0⟩`, all turn charges zero, V0's congruence `v(W) ≡ 0`, and the per-family checks of `CH1_5U.md` Theorems 3.2-3.4 (`L5-U`) and of `CH1.md` line 179 (`L5-O`).

Hence the conditions in item 3 imply no value of `N` and no congruence on `N`.

*Proof.* Item 1 is Theorems 7 and 8. Item 2 is Theorem 4 with Corollary 4.1. Item 3 is Theorem 6. Zero charges give `v(W) = 0`. The listed per-family coefficients add over the `N` copies. The conditions hold for `N = 1` and `N = 2`, so they imply neither `N = 3` nor `N ≡ 0 (mod 3)`. ∎

What stays open is FL1-i itself: whether some structure of either law fixes the family count of an interacting family-realizing phase. That needs such a phase first (FL1-V, CH1-5U-i, CH1-5O-i).

*The slab notes.* The draft says #10022 and the slab notes "differ by one premise, the `T`-only copy mass". The #10129 synthesis, line 392, locates the difference elsewhere: "Later notes outside this theme apply an index N_f (q_l - q_m) = 0 mod 3 with twist k = -q_mirror. It allows every N_f when the mirror carries the light copy's turn charge." The same line adds: "#10022 excludes a fermion-number Z3 twist unless 3 divides N, so it and these notes differ on whether that twist is available." In that case the index `N_f(q_l − q_m)` vanishes because the mirror's charge equals the light copy's charge. That is not the pairing of Theorem 4, where the light charges cancel among themselves. So the draft's account is one candidate premise difference, not a reconciliation. FL1's sentence on line 100 is right. The reconciliation stays open by name.

### 3.6 GAP B5 (line 86): real; part of FL1-V

The draft's section 4 says: "Under any symmetry group that keeps a turn and its inverter, a symmetric gap of the free tastes removes them in pairs." Its (B5) proves only that no line of the free taste space is invariant under `γ_0` and `η_0`. An interacting gap need not act by choosing an invariant subspace of the free taste space. FL1 states the narrow result, which is correct. The interacting question belongs to FL1-V and CH1-i. No repair is needed here.

### 3.7 GAP C4 (line 98): real; repaired by Corollary 9.1

The draft's (C4) says: "None of these structures is light in the free tick: at `μ = 0` the only light momentum is `K_*`, and at `μ > 0` nothing is light." Its proof treats the six momenta of (C2) only. The three links at a site are operators, not momentum fibres. FL1's Corollary 9.1 states what the proof gives, and it is correct (item 61). Nothing further is needed.

---

## 4. Checks behind the verdicts

### 4.1 The example lifts, by hand

A sign lift sends the mode at `x` to `d(gx)` times the mode at `gx`. The edge test asks that `d(y)d(y')` equal the ratio of the image edge's sign to the original edge's sign, with `η_1 = 1`, `η_2(x) = (−1)^{x_1}`, `η_3(x) = (−1)^{x_1+x_2}`.

- *Turn* `γ_0x = (x_3, x_1, x_2)`, `d(y) = (−1)^{y_1(y_2+y_3)}`, `y = γ_0x`. Edge `e_1 ↦ e_2`: ratio `(−1)^{y_1}`, and `d(y)d(y+e_2) = (−1)^{y_1}`. Edge `e_2 ↦ e_3`: ratio `(−1)^{y_1+y_2+x_1} = (−1)^{x_3}`, and `d(y)d(y+e_3) = (−1)^{y_1} = (−1)^{x_3}`. Edge `e_3 ↦ e_1`: ratio `(−1)^{x_1+x_2}`, and `d(y)d(y+e_1) = (−1)^{y_2+y_3} = (−1)^{x_1+x_2}`. Cube: the exponents along the orbit sum to `2(x_1x_2 + x_2x_3 + x_3x_1)`, which is even.
- *Inverter* `η_0x = (1−x_2, 1−x_1, 1−x_3)`, `d(y) = (−1)^{y_1(y_2+1)}`. Edge `e_1 ↦ −e_2`: ratio `(−1)^{y_1}`, and `d(y)d(y−e_2) = (−1)^{y_1}`. Edge `e_2 ↦ −e_1`: ratio `(−1)^{x_1}`, and `d(y)d(y−e_1) = (−1)^{y_2+1} = (−1)^{x_1}`. Edge `e_3 ↦ −e_3`: ratio `(−1)^{y_1+y_2+x_1+x_2} = 1`, and `d(y)d(y−e_3) = 1`. Square: `(1−x_2)(2−x_1) + x_1(x_2+1) ≡ 2x_1(x_2+1) ≡ 0 (mod 2)`.
- *Face half-turns* `f_1x = (1−x_1, 1−x_2, x_3)` with `(−1)^{y_2}`, and `f_2x = (x_1, 1−x_2, 1−x_3)` with `(−1)^{y_3}`. Edge ratios for `f_1`: `1, −1, 1`; for `f_2`: `1, 1, −1`. The signs match them. Squares: `(−1)^{(1−x_2)+x_2} = −1` and `(−1)^{(1−x_3)+x_3} = −1`. The products `f_1f_2` and `f_2f_1` have the same map and signs `(−1)^{(1−x_3)+x_2}` and `(−1)^{(1−x_2)+(1−x_3)}`, whose ratio is `(−1)^{2x_2−1} = −1`. So the two lifts anticommute.
- *Edge half-turn* `ε`: item 53. Square: `(−1)^{2x_1x_2} = 1`.
- *Quarter-turn* `π = β_εa`, `x ↦ (x_1, x_3, 1−x_2)`. Its sign at the image `y = πx` is `d_{γ_0}(γ_0x)d_ε(y)`. Since `γ_0x = εy = (y_2, y_1, 1−y_3)`, the exponent is `y_2(y_1 + 1 − y_3) + y_1y_2 ≡ y_2(1 + y_3)`. Write `(u, v) = (x_2, x_3)`. The orbit `(u,v) → (v, 1−u) → (1−u, 1−v) → (1−v, u)` has sign exponents `uv`, `v + uv`, `1 + u + v + uv`, `u + uv` mod 2. Their sum is odd, so `π^4 = z`.

### 4.2 Numerical checks ([check]; they guide and prove nothing)

`check_ref.py` (an `8^3` torus, one mode per site, `(ε, μ) = (0.7, 0.3)`, `(0.6, 0)` and `(1, π − 2)`): `V` is unitary; the lifts of `γ_0`, `η_0`, `ε`, `f_1`, `f_2` commute with `V` at all three points; the graph of nonzero entries of `V` is connected at all three points; `a^3 = 1`, `b^2 = 1`, `bab^{-1} = a^{-1}`, `β_ε^2 = 1`, `f_1^2 = f_2^2 = −1`, `f_1f_2 = −f_2f_1`, `π^4 = −1`; `aT_{(2,0,0)}a^{-1} = T_{(0,2,0)}` and `bT_{(2,0,0)}b^{-1} = T_{(0,−2,0)}`; on the O walk `b` does not commute with `WVW^*`, `WbW^*` does and is purely imaginary, and `WaW^* = a`. At `μ = 0`: `V(0) = I` on the fibre; fibre trace of `a` equal to `2`; Clifford relations from central differences of `i log V(K)` to `6·10^{-9}`; chirality eigenvalues `−1` and `+1`, four each; on each block `a` has eigenvalues `{1, 1, ω, ω̄}`. `check_grp.py` (exact integers): `O` has 30 subgroups; 4 contain `P`; the two with no inverter have orders 3 and 12, and the one of order 12 is `T`; `⟨P, E⟩ = O` and `E ∉ T`; a rotation about `c_0` keeps the parity of the coordinate sum exactly when its linear part is in `T`; the group of section 3.2 has point-group image of size 6, no inverter among 528 enumerated elements, and stabilizer of `c_0` of order 3. `check_d3.py` (`2×2` matrices): `Λ_3 = −exp(−i(π/3)n·σ)` with `n ∝ (1,1,1)` lies over `P` and has order three; `λ = exp(−i(π/2)m·σ)` with `m ∝ (1,−1,0)` lies over `H_0`; the data of section 3.2 satisfy `U(a)^3 = 1`, `U(g̃)^2 = U(T_{α_1})` and `U(g̃)U(a)U(g̃)^{-1} = U(T_v)U(a)^{-1}`.

### 4.3 Citations checked against the sources

| FL1 use | Source text, quoted | Agrees |
|---|---|---|
| Def 1 and the lifts | `LW1.md` line 43: "Statements about the exact spatial symmetry group refer to orientation-preserving lattice isometries lifted by diagonal phases." | yes |
| Theorem 3 (face products) | `LW1.md` line 186: "Every unit face has sign product \(-1\). Both \(R_e^2\) and \(R_o^2\) equal the identity." | yes |
| Theorem 3 (potential) | `LW1.md` line 213: "Their ratio has product one on every face. Fix its value at one site and define a site sign by multiplying the ratios along an edge path to that site." | yes |
| Def 2, O walk | `LW1_5.md` line 255: "with the lifts conjugated by \(W\) for \(L5\)-O" | yes |
| Def 2, dressed O | `LW1_5.md` line 257: "Site parity implements LW1's sign lift." | yes |
| Def 2, dressed U | `LW1_5.md` line 261: "LW1 A2 constructs signs \(d_g(gx)\in\{\pm1\}\) whose product at the endpoints converts each transformed edge sign into the sign of the image edge, including reversed edges." | yes |
| Theorem 7 (band) | `LW1.md` line 325: "\(\cos w(K)=a_{\rm band}\chi(K)-b_{\rm band}\) and \(\mu\leq w(K)\leq2\varepsilon\)"; line 344: "When \(\mu=0\), zero occurs only at \(K=0\)." | yes |
| Theorem 7 (`Θ`) | `LW1.md` line 348: "Hence \(\Theta V\Theta^{-1}=V\)." | yes |
| Theorem 7 (dispersion) | `LW1.md` line 383: "\(w^2=s_\varepsilon^2k^2/3+O(k^4)\)" | yes |
| Theorem 7, O | `LW1_5.md` line 322: "\(W_{2b+r}=(-1)^{b_1+b_2+b_3}i^{r_1+r_2+r_3}\), so it shifts cell momentum by \((\pi,\pi,\pi)\)" | yes |
| Theorem 9 | `LW1.md` line 215: "its stabilizer consists of the identity and the two turns about that body diagonal." | yes |
| Def 3, Theorem 6, O | `CH1.md` line 235: "an operational proper long-distance subgroup \(H\subseteq G_\infty\subsetneq Spin(10)\)" | yes |
| Theorem 5, Theorem 6, O | `CH1.md` line 179: "It contains four weak doublets. This is arithmetic, not a full global-anomaly proof." | yes |
| Theorem 6, U | `CH1_5U.md` line 89: "For every `X∈u(5)`, `Tr_{R_u}X=Tr_{R_u}X³=0`"; line 96: "\[n(\sigma^*R_u)=4n(\sigma^*5)\in4\mathbb Z.\]"; line 101: "Then `ν∈{16,0,−16}`." | yes |
| A5-glob conditional | `CH1_5U.md` line 127: "**A5-glob (open, conditional).**" | yes |
| GAP A2 | #10022 line 52: "The copy mass keeps exactly the 12 tetrahedral rotations, including all 8 three-fold turns." | yes |
| Def 6 (V0) | #10022 lines 73-74: "With the mirror gapped symmetrically, the light 't Hooft vertex (4N left-handed zero modes) must be invariant under the kept turn." | yes |
| Theorem 5 (D7) | #10022 lines 86-87: "family-dependent copy-sign projectors (q_f = 1 for some families, 2 for others) allow every N >= 2." | yes |
| Theorem 8 vs #10022 | #10022 line 64: "Without the copy mass both tastes are light, with q = {1, 2}, which sum to 0." | yes |
| Open list | `TOE_ASSEMBLY.md` line 445: "reconciling #10022 with the later slab notes #10063, #10065" | yes |

Two pass-1 line numbers are off by one; `FL1.md` does not repeat them. The draft cites #10022 "its lines 57-58" for the factorization; the quoted sentence begins on line 56. It cites "its line 74" for V0; the sentence begins on line 73.

### 4.4 The octahedral extension (referee closure, conditional on one cited presentation)

*Claim.* Let `L_O` be the group of canonical lifts of the rotations about `c_0`. Grant the presentation `⟨s, t | s^2 = t^3 = (st)^4 = 1⟩` of `O`, with `s = ε̄` and `t = γ̄_0` (cited, not rebuilt). Then `L_O` is presented by generators `a`, `e = β_ε`, `z` and relations `a^3 = e^2 = z^2 = 1`, `(ea)^4 = z`, `z` central. The map `a ↦ Λ_3`, `e ↦ iλ_ε`, `z ↦ −1`, with `λ_ε ∈ SU(2)` over `ε̄`, extends to a homomorphism `φ: L_O → U(2)` of the form `φ(β) = Λ(β)·i^k`, `Λ(β) ∈ SU(2)` over `β̄`. With `φ(T_t) = 1` it extends to the lift group of `𝒢`, and every turn charge is `0`.

*Proof.* The relations hold in `L_O`: `a^3 = 1` by Theorem 3, and `e^2 = 1` and `(ea)^4 = z` by section 4.1. `ε̄` and `γ̄_0` generate `O` (item 53), and each element of `O` has exactly two canonical lifts. So `a`, `e`, `z` generate `L_O`, and `L_O` has 48 elements. Let `G̃` be the group defined by these generators and relations. Setting `z = 1` gives the cited presentation of `O`, so `G̃/⟨z⟩` has at most 24 elements. `z` is central of order at most two, so `G̃` has at most 48 elements. The map `G̃ → L_O` is onto, hence an isomorphism. In `U(2)`: `Λ_3^3 = 1`; `(iλ_ε)^2 = −λ_ε^2 = 1`; `λ_εΛ_3 ∈ SU(2)` lies over the quarter-turn `ε̄γ̄_0`, so it is `±exp(−i(π/4)n·σ)` for a unit axis `n` and its fourth power is `exp(−iπn·σ) = −1`, and `(iλ_εΛ_3)^4 = −1`; `−1` is central. So `φ` is defined. The generator images have the form `i^k` times an element of `SU(2)` over their rotation, and products keep that form. The signs of `a` and `e` have period two, so every element of `L_O` satisfies `βT_tβ^{-1} = T_{Qt}`, and `φ(T_t) = 1` is consistent. For a turn, its cube-one lift `β̂` has `φ(β̂) = i^kμ` with `φ(β̂)^3 = 1` and `μ` of order 3 or 6. If `μ` has order 3, then `i^{3k} = 1` and `i^k = 1`. If `μ` has order 6, then `i^{3k} = −1`, `i^k = −1`, and `φ(β̂) = (−μ)·1` with `−μ` of order 3. In both cases the internal factor is `1`. ∎

The images agree with the hand facts of section 4.1: a face half-turn lies in `T`, so its image is in `SU(2)` over a half-turn and squares to `−1`; an edge half-turn maps to `i` times such an element and squares to `1`. The extension stays conditional on the cited presentation of `O`. Nothing in FL1 uses it.

---

## 5. Required edits

These change a false line or supply a missing step. Each cites the section of this report that gives the text.

1. Line 112 (item 69). Restrict the staggered density to `L5-U`, and use the staggered site parity on `L5-O` (section 2.1).
2. Line 114 (item 71). Replace the sentence on the octahedral extension (section 2.1). The extension stays conditional on the cited presentation of `O` and unused.
3. Line 32 (item 16). Insert the steps that make `Q` of order three and of the form `DP^{±1}D^{-1}` (section 2.2).
4. Line 36 (item 24). Insert the step that an inverter maps the axis line of `Q` onto itself (section 2.2).
5. Line 72 (item 43). Insert the presentation of the lift group of `𝒦` by normal forms (section 2.2).
6. Line 84 (item 53). Display `ε: x ↦ (x_2, x_1, 1 − x_3)` with sign `(−1)^{y_1y_2}`, and insert the proof that `γ̄_0` and `ε̄` generate `O` (section 2.2).
7. Line 82 (item 52). Name `γ_0` and `η_0` in Theorem 8, or add the conjugacy sentence (section 2.2).
8. Line 42 (GAP S1). Add the free-walk closure (section 3.1). Restrict "especially at exceptional parameters" to the dressed ticks. Record that on the O free walk the real sign lift of `η_0` is `±iWβ_{η_0}W^*` and squares to `z`.
9. Line 62 (GAP A2). State the counterexample (section 3.2). Replace "that source was not independently retrieved here" by the quote of #10022 line 52.
10. Line 68 (GAP in FL1-i(3)). Replace it by the proposition of section 3.3.
11. Line 100 (GAP FL1-i). Add the theorem of section 3.5 as the proved content. Add the two quotes of #10129 line 392.

Optional before freeze: line 7, "per complex flavour"; line 9, drop "that abstract data are phases"; line 13, merge the two pass-2 provenance sentences; line 20, say that the represented group contains `z`; line 32, the last step of item 19; line 36, the normality step of item 22; line 52, name the weights of item 33; line 80, cite B10 (1) for the eigenvalues and note that the four nodes are degenerate (items 47 and 50).

## 6. Open statements to carry, by name

- **FL1-i**: whether some structure of either law fixes the family count of an interacting family-realizing phase. Section 3.5 states what is proved about the candidates on file.
- **FL1-V**: whether all admissible family-realizing phases of a law have one family count, and whether it is three.
- **FL1-ii** (= CH1-i), **CH1-5U-i**, **CH1-5O-i**, **CH1-ii**.
- **AM-5** and **A5-glob**, as stated in `CH1.md` and `CH1_5U.md`.
- **GAP D**: the full crystalline and mixed anomaly of the kept symmetries. FL1 needs it only for the stronger anomaly sentence it already withholds.
- **VC1**, including whether either vacuum breaks the inverters, for example by the staggered order of section 2.1.
- **LZ1**, for the Lorentz form that IR-P presumes.
- **The reconciliation of #10022 with #10063 and #10065** (`TOE_ASSEMBLY.md` line 445).

FL2 and CS1 stay downstream open questions, as FL1 says. Two items need not be carried. The uniqueness of sign lifts for the dressed ticks is not needed by any theorem. The octahedral extension is conditional on a cited presentation and unused.

## 7. Freeze recommendation

FL1 can be frozen with its open statements named, after the eleven required edits. Every result FL1 marks as proved holds within its hypotheses: Theorems 1-9 and Corollaries 4.1, 4.2 and 9.1, with the four missing steps supplied in section 2.2. The two ERRORs sit in the proposed-route paragraph and in a remark. Neither changes a theorem. All seven GAPs are real. This report repairs four of them: S1 for the free walks, A2, FL1-i(3) and FL1-i. FL1 itself repairs C4 by Corollary 9.1. D and B5 stay open, and FL1 does not claim them. The frozen FL1 does not establish its target `N_f = 3`. It records what is proved toward that target and names what is open.

---

## FINISH

**Proved here (referee, pass 3).**
- Verdicts on all 72 items of `FL1.md`: 66 CORRECT, 2 ERROR, 4 INCOMPLETE, each with its fix or missing step (sections 1 and 2).
- The missing steps of Theorems 1, 2, 6 and 8, and the extension of Theorem 8 to every turn by conjugacy (section 2.2).
- On both free walks, every sign lift that commutes with the free tick is canonical and unique up to `z`, at every admissible `(ε, μ)` (section 3.1).
- On the O free walk, the real sign lift of `η_0` is `±iWβ_{η_0}W^*` and squares to `z`; Theorem 8 does not depend on this choice (section 3.1).
- On `L5-O`, every state invariant under the local gauge automorphisms has `ω(n_x) = 5/2`; the site parity `P_x` is gauge invariant and transforms as `P_x ↦ P_{gx}` under canonical lifts (section 2.1).
- Repaired FL1-i(3): with a copy-blind turn, V0 forces `N ≡ 0 (mod 3)` exactly when `v(F) ≢ 0 (mod 3)`, and then no inverter is kept (section 3.3).
- Repaired FL1-i: the free node count, the vanishing of turn-odd sums when an inverter is kept, and data with family count `N` for every `N ≥ 1` meeting IR-P (a)-(c), V0's congruence, zero turn charges and the per-family checks. Hence those conditions imply no value and no congruence of `N` (section 3.5).
- Conditional on the cited presentation of `O`: the representation of Theorem 6 extends to the lift group of `𝒢` with all turn charges `0` (section 4.4).

**Counterexamples.**
- To the draft's "A count can survive only in a phase whose kept point group is `C_3` or `T`": the kept group `⟨γ_0, (H_0, (2,0,0))⟩` has point group `D_3`, no inverter of `γ_0`, and IR-P data with every turn charge `1` (section 3.2).
- To the "only if" half of the draft's FL1-i item 3: charges `(0, 1, 0)` on `(10, \bar5, 1)` in every copy force `N ≡ 0 (mod 3)` under V0 without a common charge (section 3.3).
- To FL1 line 112 on `L5-O`: the staggered density has the same expectation in every gauge-invariant state (section 2.1).
- To FL1 line 114, "these facts alone do not establish the extension": the counting argument of section 4.4.
- To the draft's "The construction is purely about the signs `η_i`, which are the same in `L_cube`, `L5-U` and `L5-O`", on the O free walk: section 3.1.

**Open, by name.** FL1-i; FL1-V; FL1-ii (= CH1-i); CH1-5U-i; CH1-5O-i; CH1-ii; AM-5; A5-glob; GAP D; VC1; LZ1; the reconciliation of #10022 with #10063 and #10065. All are carried from FL1 and its inputs. This report leaves no new open lemma: each of its own claims ends in a proof or a counterexample. The octahedral extension remains conditional on one cited presentation and is unused.

**What changes downstream.**
- *FL1.* It can be frozen after the eleven required edits of section 5. FL1-i and FL1-V stay open.
- *Corollary 4.2, VC1 and any state-breaking route.* The correct reading is the stabilizer of the turn's fixed centre, not the whole point group. A route needs a kept group with no inverter. Kept groups with point group `D_3` also admit unpaired charges, at least as IR-P data.
- *VC1 on `L5-O`.* An order parameter for a broken inverter must be gauge invariant. The staggered site parity is a candidate; the staggered density is not.
- *#10022 and the slab notes.* The #10129 synthesis locates their difference in the availability of the fermion-number `Z_3` twist. The draft's account by the `T`-only copy mass is one candidate. The reconciliation stays open.
- *CH1-5U-i and CH1-5O-i.* Unchanged.
