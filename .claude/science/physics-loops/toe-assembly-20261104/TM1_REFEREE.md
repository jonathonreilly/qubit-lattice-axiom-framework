lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# TM1 referee report (pass 3)

Written 2026-11-06 (UTC) by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). The lane runs in a pass-1 lane slot of the TOE assembly. Its task is pass 3, the referee, of part TM1 under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. This session wrote neither pass 1 (`TM1_DRAFT.md`) nor pass 2 (`TM1.md`). This is one check: one whole-part, line-by-line read. It reviews no other review.

**What this file is.** A referee report. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is not edited. No other file is edited. The lead copies, checks and commits this file.

**Text read.** `TM1.md` as of commit `c96e71cdf` (the last commit that touches it; it is the branch head when read). SHA-256 of the file read: `320672a2a44d9ba21e502c1089e732834bf28d6e094c813520952101428b357e`. It has 134 lines. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), HEAD | `c96e71cdf` |
| `origin/main` (ref recorded; no file read from it) | `f5af11cd01` |

Files read at HEAD, by line, with the commit that last changed each. All are in `.claude/science/physics-loops/toe-assembly-20261104/`.
- `TM1.md` (`c96e71cdf`): lines 1-134, all of it.
- `TM1_DRAFT.md` (`b05ee6430`; SHA-256 `54c2c8ea444b7303c22e7ebabb758a302bf219baad673c46765ebe1e53a5e70f`): lines 1-422, all of it.
- `LW1.md` (`5ff19240c`, frozen): lines 1-330 and 380-508.
- `VC1_5_DRAFT.md` (`2d0adc0c0`): lines 36-262.
- `LW1_5_DRAFT.md` (`e648fa3e0`): lines 296-345 and 370-425.
- `LW1U_SEA_DRAFT.md` (`2d0adc0c0`): lines 180-186 and 369-373, and the grep hits for `Σ_π` (lines 177, 183, 189, 195, 211, 215, 217, 221).
- `TOE_ASSEMBLY.md` (`7d2b20d29`): lines 1-60, 95-232, 275-300 and 472-490.
- For the format only: `LW1_REFEREE.md` lines 1-80 and its headings; `Y2W_DRAFT.md` lines 1-40.
- Rules: `AGENTS.md`, `CLAUDE.md`, `docs/ai_methodology/SCIENCE_WORKFLOW.md`.

Not read: the distilled `VC1_5.md`, `LW1U_SEA.md` and `LW1_5.md` (TM1.md cites the drafts), every other referee file, and every other branch.

**Method.** Every proof was re-derived by hand. Each citation of a pass-1 source was checked against the source line. Verdicts: CORRECT; ERROR (a false, contradictory or wrongly cited line, quoted, with a fix); INCOMPLETE (a step or hypothesis that the text needs and does not state, or states only by pointing to the draft; the missing piece is named). Terse wording that is exact in context is CORRECT, with a note. A "referee closure" is a short complete argument written here for a missing step. A "[check]" is the scratch computation `/tmp/toe-tm1ref/check_tm1ref.py` (output `out.txt` there). It ran after `memory_pressure` showed 60 percent free, took 0.07 s and 16 MB, and uses floating point. It is an independent implementation, not the draft's script: dressed cube generators of `L_cube` act on single Fock basis vectors of the infinite lattice, with Jordan-Wigner signs from the lexicographic order. `scripts/lab_ops.py preflight` could not run, because the script is not in this sparse checkout. A check guides and never proves.

**Counts.** 97 items: 90 CORRECT, 2 ERROR, 5 INCOMPLETE. Each theorem's statement and each step of its proof is an item. No ERROR or INCOMPLETE item overturns a proved conclusion. Corollary 14 needs one added hypothesis, which its proof already uses. One sentence of section 5 needs an exact form.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The Record axiom, PS-3c, PS-4 and PS-3h5 are read plainly. This report proposes no reading. Its one new notion, a "monotone reading of saturation" (section 3.2), is notation for a quantifier in a proved statement. It gets the four-test check there.

**Working set used, by name.** PS-3 read by PS-3c and PS-3h, through LW1's formalization (`LW1.md` lines 72-82 and E3). PS-4. PS-1c, only through the lifts. PS-5 and PS-6r, only through `L5-O[S_+]` and `L5-U[m]` as stated in `LW1_5_DRAFT.md` section 8.1. PS-3h5 and PS-3g (proposed only, not in the working set) where TM1.md uses them. PS-2, PS-7r, PS-11c and PS-Ar are not used.

**Inputs from outside the working set.** The joint Born identification (`LW1.md` inferred definition 26), which TM1.md names as an external premise. Standard mathematics, rebuilt where used: spectral projections of commuting self-adjoint elements, positivity of states, the normal form of a two-by-two unitary, and Kolmogorov's extension theorem for a product of probability measures on compact metrizable spaces. No literature is used. No new search was run. The draft's search record (`TM1_DRAFT.md` line 35) was read, and no step here rests on a citation.

---

## 1. Verdict table

| # | Item (TM1 line) | Verdict | Note |
|---|---|---|---|
| 1 | Status paragraph (3) | CORRECT | Matches Theorems 1-4 and 11-14. |
| 2 | GAP (a): transport for non-factor states (5) | CORRECT | Gap real as a limit on "PS-3 history"; no theorem depends on it. Referee closure R2, section 3.1. |
| 3 | GAP (b): saturation (5) | CORRECT | Gap real against the draft's "under any reading" (draft lines 378, 413), not against draft Corollary 2.9. Repaired statement R1, section 3.2. |
| 4 | Open paragraph (7) | CORRECT | The free-sea excitation question has no label; see section 6. |
| 5 | Provenance (9) | ERROR | "reasoning effort high ... session `01a1aea0-...`" contradicts "effort: not visible; session id: not visible". |
| 6 | Preamble of section 1 (13) | CORRECT | |
| 7 | Definition 1: sites, tilings, `G` (15) | CORRECT | |
| 8 | Definition 2: tick, base tick, law data (16) | INCOMPLETE | `L5-O`'s register is never fixed to `S_+`; Lemma 10, Theorem 11 and Theorem 6 need it. |
| 9 | Definition 3: actual values, lifts, symmetric states (17) | ERROR | Cites "LW1 B4" for the lifts; B4 is Gauss conservation. |
| 10 | Definition 4: `n_x`, `P_x`, `N_x`; PS-3h5 (18) | CORRECT | Matches `LW1_5_DRAFT.md` line 324. |
| 11 | Definition 5: `Π_x(v)`, `D_xy`, joint Born (19) | CORRECT | |
| 12 | Definition 6: `F_n`, `R_n`, `t_x`, `r_x` (20) | CORRECT | Same as `LW1.md` lines 77-82 with the general `D`. |
| 13 | Definition 7: history assertions (21) | CORRECT | Note: add that such measures exist for every state (R2). |
| 14 | Definition 8: `B^{+r}`, `A(Λ)`, full saturation (22) | CORRECT | |
| 15 | Theorem 1, statement (26) | CORRECT | |
| 16 | Theorem 1, proof: determinism (28) | CORRECT | |
| 17 | Theorem 1, proof: content law (28) | CORRECT | Uses only the one-time marginal at tick `t_x`. |
| 18 | Theorem 1, proof: mixtures (28) | CORRECT | |
| 19 | Remark on a dark state mixed with the trace (30) | CORRECT | |
| 20 | Theorem 2, statement (32) | CORRECT | |
| 21 | Theorem 2, proof, with the periodic case (34) | CORRECT | |
| 22 | Theorem 3, statement (36) | CORRECT | "lifts" carries Definition 3's condition `β_g(a_x)=a_{gx}`. |
| 23 | Theorem 3, proof: `ρ_n∘β_h=ρ_n` (38) | CORRECT | |
| 24 | Theorem 3, proof: `β_h(D_xy)=D_{hx,hy}` (38) | CORRECT | |
| 25 | Theorem 3, proof: witnesses move, transitivity, recursion (38) | CORRECT | |
| 26 | Theorem 4 (TM1-D), statement (40) | CORRECT | Wording: restore the draft's `ω_0(D_{x_0y})=ω_0(D_{x_0z})=0`. |
| 27 | Theorem 4, proof (42) | CORRECT | |
| 28 | Theorem 5, statement (44) | CORRECT | |
| 29 | Theorem 5, proof: one link orbit per tiling (46) | CORRECT | |
| 30 | Theorem 5, proof: two witnesses and the converse (46) | CORRECT | |
| 31 | Theorem 5, proof: cube edge graphs, countable union (46) | CORRECT | |
| 32 | Theorem 5, proof: content in case (E) (46) | CORRECT | |
| 33 | Mixture of the two dark `L_cube` states (48) | CORRECT | |
| 34 | Theorem 6, statement (50) | CORRECT | Conditional on provisional VC1 and LW1-5 results, as stated; `L5-O` means `L5-O[S_+]` (item 8). |
| 35 | Theorem 6, proof: sharp values in the dark witnesses (52) | CORRECT | |
| 36 | Theorem 6, proof: `L_cube` dark states (52) | CORRECT | |
| 37 | Theorem 6, proof: cited VC1 results (52) | CORRECT | Checked against `VC1_5_DRAFT.md` O2, O2.1, U1, U3. |
| 38 | Theorem 6, proof: free seas (52) | CORRECT | Note: cite `LW1.md` B10(3) and `LW1_5_DRAFT.md` A2-5 for stationarity and symmetry. |
| 39 | Theorem 6, proof: traces, `1/2` and `772/1024` (52) | CORRECT | `[check]`: `1 − Σ_k C(5,k)^2/1024 = 193/256`. |
| 40 | Theorem 6, proof: `ω_t`, finite `t` (52) | CORRECT | |
| 41 | Remark: limit `t → +∞`, formation not continuous (54) | CORRECT | |
| 42 | Remark: `LW1U_SEA_DRAFT.md` Corollary 3.3 (54) | CORRECT | Quotation checked (source line 183). |
| 43 | Preamble of section 3 (58) | CORRECT | |
| 44 | Lemma 7, statement (60) | CORRECT | Note: the coefficient is `±j(e)` or `±j(e−1)`. |
| 45 | Lemma 7, proof (62) | CORRECT | |
| 46 | Lemma 8, statement (64) | CORRECT | |
| 47 | Lemma 8, proof (66) | CORRECT | |
| 48 | Lemma 9, statement (68) | CORRECT | Note: "sector product vector" is not defined in TM1.md. |
| 49 | Lemma 9, proof (70) | CORRECT | |
| 50 | Lemma 10, statement (72) | CORRECT | Needs the rishon vacuum in the register, so `R = S_+` (item 8). |
| 51 | Lemma 10, proof: the four register coefficients (74) | CORRECT | All four expansions re-derived. |
| 52 | Lemma 10, proof: three kill the vacuum, `c_yc_x` kills an empty end (74) | CORRECT | |
| 53 | Lemma 10, proof: electric phase (74) | CORRECT | |
| 54 | Theorem 11, statement (76) | CORRECT | Note: state also that no site of `2Z^3` ever records (section 5 uses it). |
| 55 | Theorem 11, proof: `L_cube` configuration (78) | CORRECT | |
| 56 | Theorem 11, proof: `L5-U` configuration (78) | CORRECT | Note: name the flavours, as the draft does. |
| 57 | Theorem 11, proof: `L5-O` configuration (78) | CORRECT | |
| 58 | Theorem 11, proof: stationarity and gauge average (78) | INCOMPLETE | The electric phase on `L5-U` and the five-mode form of Lemma 8 are not stated. |
| 59 | Theorem 11, proof: translation invariance (78) | CORRECT | |
| 60 | Theorem 11, proof: neighbour count and Theorem 2 (78) | CORRECT | |
| 61 | Theorem 12, statement (80) | CORRECT | |
| 62 | Theorem 12, proof: `ψ` symmetric and gauge invariant, carried by `α^{-2}` (82) | CORRECT | |
| 63 | Theorem 12, proof: tick 2 (82) | CORRECT | |
| 64 | Theorem 12, proof: reduction to `x=(1,1,1)`, positive weights (84) | CORRECT | |
| 65 | Theorem 12, proof: odd neighbours, frozen configuration (84) | CORRECT | `[check]`. |
| 66 | Theorem 12, proof: even neighbours, the two-configuration hop (86) | INCOMPLETE | Load-bearing link values are left to "the draft's blocked construction". `[check]`: with `−S` there, even cubes act on the moved configuration. |
| 67 | Theorem 12, proof: `F_1=∅`, `F_2=Z^3`, not stationary (86) | CORRECT | |
| 68 | Theorem 12, proof: the window clause (86) | CORRECT | |
| 69 | Theorem 13, statement (88-92) | CORRECT | Note: for finite `q`, `y` may record (section 2.3). |
| 70 | Theorem 13, proof: the two vectors and their blocked links (94) | CORRECT | `[check]` for `S = 1/2, 1, 3/2, 2`, every `m`. |
| 71 | Theorem 13, proof: the tick acts as `U` up to phase (94) | CORRECT | `[check]`: only the even cube `C_0` acts, as `+(j(m)/√3)σ_x`. |
| 72 | Theorem 13, proof: equal Gauss eigenvalues (94) | CORRECT | |
| 73 | Theorem 13, proof: sites outside `{x,y}`; `x∈F_n` iff `p_n=0` (96) | CORRECT | |
| 74 | Theorem 13, proof: `U^r` fixes the line of `y` iff `U^r` is scalar (96) | CORRECT | |
| 75 | Theorem 13, proof: `t_x=k` (96) | CORRECT | |
| 76 | Theorem 13, proof: `k=3` (98) | CORRECT | |
| 77 | Theorem 13, proof: `S=1/2` (98) | CORRECT | |
| 78 | Corollary 14, statement (100) | INCOMPLETE | Missing hypothesis `sin θ ≠ 0`, which the proof uses and `q = ∞` does not imply. |
| 79 | Corollary 14, proof (102) | CORRECT | Given `sin θ ≠ 0`. |
| 80 | Remark on boxes, `y_k` and contents (104) | CORRECT | |
| 81 | Check record (106) | CORRECT | Note: the draft's items (3)-(4) are `v_1` and the pair `v_2, b_2`. |
| 82 | Lemma 15, statement (110) | CORRECT | |
| 83 | Lemma 15, proof (112) | CORRECT | |
| 84 | Theorem 16, statement (114) | CORRECT | |
| 85 | Theorem 16, proof (116) | CORRECT | |
| 86 | Corollary 17, statement (118) | CORRECT | Note: the count bound needs `F_1(ω_v)=Z^3`; say "in that case". |
| 87 | Corollary 17, proof (120) | CORRECT | |
| 88 | Local unitary excitations (122) | CORRECT | |
| 89 | Product states and the gauge average (122) | CORRECT | |
| 90 | Unitary excitations of the trace (122) | CORRECT | |
| 91 | Section 5, case (E) and (N) counts (126) | CORRECT | |
| 92 | Section 5, the trace and Theorem 11 (128) | CORRECT | |
| 93 | Section 5, the flat tick of Theorem 13 (128) | INCOMPLETE | The conclusion holds for readings of saturation under which a saturated count never rises later; the sentence does not state this condition. |
| 94 | Section 5, transport disclaimer (128) | CORRECT | |
| 95 | Section 5, growth on more than one tick (130) | CORRECT | |
| 96 | Section 5, VC1 witnesses, U2 and U2′ (132) | CORRECT | |
| 97 | Section 5, readings and checks (134) | CORRECT | Checked against `LW1_5_DRAFT.md` lines 322-341. |

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 5 (provenance, line 9).** The line says: "Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1aea0-1f36-78b0-ab6c-1a5894599987`." Later the same line says: "Model: gpt-6.1-terra; effort: not visible; session id: not visible." The two clauses disagree on the effort and on the session. The commits in the line are right: `5ff19240c` is in the branch log, the local `origin/main` ref is `f5af11cd0102cfd0b51aef0911f600130bf5beb1`, and the draft's HEAD `2d0adc0c02` matches `TM1_DRAFT.md` line 13. **Fix.** Replace the second clause with: "The distiller could not see its own effort or session id; the values above come from the run log."

**Item 9 (Definition 3, line 17).** The line says: "Existence of these lifts for the three base laws and the choices below is an imported LW1 B4/VC1 Lemma C result." `LW1.md` B4 (line 237) is Gauss conservation: "Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\)." It says nothing about lifts. The lift result is the proof after it, "Gauged covariance and B1/B1q" (line 243): "Thus each cube Hamiltonian is sent to the Hamiltonian of the image cube. ... This proves covariance of \(U_0\)." It uses A2's site sign correction (line 209), and that correction gives `n_x ↦ n_{gx}`. **Fix.** "Existence of these lifts is imported: for `L_cube` from LW1 A2 and its gauged-covariance proof (`LW1.md` lines 209 and 243), for the five-mode laws from VC1 Lemma C. The covariance of `P_x` and `N_x` is shown in Definition 4."

### 2.2 INCOMPLETE

**Item 8 (Definition 2, line 16): the register of `L5-O`.** `LW1_5_DRAFT.md` line 305 makes the register a free datum: "carries a register `R_ℓ = R` ... Free datum. Proposed value: `R = S_+`". TM1.md line 16 lists "`S` or `m` and `τ_E`" as law data and never names `R`. Four places need `R = S_+`. Lemma 10 assumes "the rishon vacuum on a link", and `VC1_5_DRAFT.md` line 205 says: "With `S_−` the rishon vacuum is not in the register". Theorem 11 builds its `L5-O` state on that vacuum. Theorem 6's `L5-O` witnesses are VC1 O2's, stated for `S_+`. PS-3h5 itself reads "under `L5-O[S_+]` the site parities" (`LW1_5_DRAFT.md` line 324). **Missing piece and fix.** Add to Definition 2: "`L5-O` means `L5-O[S_+]`, the proposed register; it contains the rishon vacuum." Theorems 1-5 hold for any register and may say so. Also write `C ∈ T_e` under `M_e` and `C ∈ T_o` under `M_o` (`LW1.md` line 68).

**Item 58 (Theorem 11, line 78): stationarity on the five-mode laws.** The proof says: "Lemmas 8–10 give stationarity; gauge-average the five-mode states." Lemma 8 is stated for `L_cube` only. On `L5-U`, Lemma 9 kills every hop, but the electric layer `W_E = ∏_ℓ e^{−iτ_E(p_{ℓ,x} − m/2)^2}` (`VC1_5_DRAFT.md` line 58) is not discussed. **Referee closure.** `W_E` is a function of the end numbers. Every vector in the construction has definite end numbers on every link, so `W_E` multiplies it by a phase. On `L5-O`, Lemma 10's last sentence gives the phase. So on every finite region that contains the supports of the gates in `α(A)`, `U_0` multiplies the product vector by a phase. The argument of Lemma 8 ("Finite gate support proves stationarity on local observables") then gives `Φ∘α = Φ` on both five-mode laws. **Fix.** Add these sentences. Also name the vectors, as the draft does (`TM1_DRAFT.md` line 260): at a marked end, flavours `1, …, min(m,5)`; at the other end, flavours `1, …, max(m−5,0)`; on a link with no marked end, `min(m,5)` rishons at the source end and the rest at the target end. "Choose a fixed configuration" must mean one definite vector with definite end numbers, the same on every link of its kind (or at least a `2Z^3`-periodic choice), or translation invariance is not shown.

**Item 66 (Theorem 12, lines 84-86): the labels of the non-mixed links.** The proof says: "For even neighbours, change the odd link `(x,x+e_1)` to `m<S`, and set the two even links entering `x+e_1` in directions 2 and 3 to `-S`, leaving the other labels as in the draft's blocked construction." It then says: "After the hop all other links at the two endpoints are blocked". TM1.md's own configuration (line 84) fixes only "all mixed links blocked". It leaves the labels of the other links free. Those labels are load-bearing. After the hop, `x = (1,1,1)` is empty and its three neighbours in `C_0 = {0,1}^3` are full. The even link `(x − e_i, x)` then joins a full source to an empty target, and Lemma 7 blocks it only at label `S`. The links leaving `x + e_1 = (2,1,1)` along `+e_1, +e_2, +e_3` now have a full source, and they too are blocked only at `S`. In TM1.md's configuration these six links join equal occupations, so "mixed links blocked" does not fix them. The draft does: "Set every other link to `ε = S`" (`TM1_DRAFT.md` line 283). `[check]`: with `S` on every non-mixed link, only the odd cube `{1,2}^3` acts on `v_2` and `b_2`, with amplitude `+j(m)/√3` both ways, for `S = 1/2, 1, 3/2, 2` and every `m`. With `−S` there instead, the even cubes with base points `(0,0,0)` and `(2,0,0)` also act on `b_2`. The theorem stands; the proof needs the labels. **Fix.** In line 84 write: "Choose one with the even cube of `x` full, all other even cubes empty, every mixed link at its blocking value and every other link at `S`." Drop "as in the draft's blocked construction" in line 86. Optionally add that "acts as `(j(m)/√3)σ_x`" holds up to a sign fixed by the fermion order, and that the squared amplitude does not depend on it.

**Item 78 (Corollary 14, line 100): a missing hypothesis.** The statement says: "If the data in Theorem 13 have `q=∞`, there is a gauge-invariant state forming at least one new record at every tick." The proof runs Theorem 13's construction, which needs `sin θ ≠ 0`. `q = ∞` does not imply it. **Counterexample to the proof as written.** Take `S = 7/2`, `m = 1/2`, `a_e = π/√5` (inside the window, since `π/√5 < π/2`) and `τ_E` with `τ_E/π` irrational. Then `j(1/2) = √15`, `θ = a_e√15/√3 = π`, `sin θ = 0`, `φ = τ_E(2m+1) = 2τ_E`, and `U = −diag(e^{iτ_E}, e^{−iτ_E})`. `U^r` is scalar exactly when `rτ_E ∈ πZ`, which never holds for `r ≥ 1`, so `q = ∞`. But `U` is diagonal, so `U^{−k}|y⟩ ∈ C|y⟩`, `p_n = 0` for every `n`, and every `x_k` records at tick 1. `[check]` gives `p_n = 0`. The statement itself is not refuted at this law point: `m' = −1/2` gives `j = 4`, `θ' = 4π/√15`, `sin θ' ≠ 0`, `φ' = 0`, and `θ'/π = 4/√15` is irrational, so `q' = ∞` and the construction works with `m'`. **Fix.** "If the data in Theorem 13 have `sin θ ≠ 0` and `q = ∞`". The draft's Corollary 3.8 (line 325) has both.

**Item 93 (section 5, line 128): the condition on saturation.** The text says: "Its count increases at tick 1, is flat at tick 2, and increases at tick 3. Thus a definition of saturation consistent with a later increase cannot make the earlier flat step satisfy strict increase until saturation." The three facts are right (Theorem 13 with `k = 3`). The conclusion needs a condition the sentence does not state clearly. If a reading lets a box be "saturated" and still gain records later, the flat step may come after saturation, and TM1(a)(2) is not violated. **Fix.** Replace the second sentence with Proposition R1(i) of section 3.2: "Under every reading of saturation under which a saturated box never gains a record later (full occupancy is one), this box is not saturated at ticks 0, 1 or 2, because it gains a record at tick 3; its count does not rise from tick 1 to tick 2; so TM1(a)(2) fails for it."

### 2.3 Notes on CORRECT items that bear on the freeze

- **Item 26 (Theorem 4).** "The first case holds exactly when two neighbours of one site have zero disagreement expectation in `ω_0`." Read as "zero disagreement with that site", it is right. Read as "with each other", it is wrong. Restore the draft's exact form (`TM1_DRAFT.md` line 165): "exactly when, at one site `x_0`, two neighbours `y ≠ z` have `ω_0(D_{x_0y}) = ω_0(D_{x_0z}) = 0`."
- **Item 13 (Definition 7).** Add: "Such measures exist for every initial state: the product of the one-time Born laws is one (R2), and LW1 E5 gives supported Markov ones." E5 is stated for `L_cube`. `LW1_5_DRAFT.md` line 376 carries it to `L5-O` ("E3-E6 | unchanged | finite alphabets `{±1}` per site"); the same proof runs on `L5-U` with the alphabet `{0, …, 5}`. TM1 needs none of this beyond the one-time marginals.
- **Item 38 (Theorem 6, free seas).** The stationarity and symmetry of the free seas are `LW1.md` B10(3) (line 324: "\(\omega_P\) is a pure, stationary, \(\mathscr G\)-invariant, half-filled state") and, for five modes, A2-5 with five copies (`LW1_5_DRAFT.md` lines 382, 402). The proof's sentence "The other stationarity and invariance claims are the cited VC1 results" does not cover them. Add the citation.
- **Item 44 (Lemma 7).** "the one allowed hop has coefficient `j(e)` ... or `j(e-1)`": the coefficient carries a sign `±1` from `η_i(x)` and the fermion order (`TM1_DRAFT.md` line 224). No later step depends on the sign.
- **Item 48 (Lemma 9).** "Sector product vector" means a product vector with definite site numbers `N_x` and definite end numbers `p_{ℓ,z}` (`TM1_DRAFT.md` line 234). Say so.
- **Item 54 (Theorem 11).** The statement gives "precisely the sites outside `2Z^3` first record at tick 1". With Theorem 2 (`t_x ∈ {1, ∞}`) this means the sites of `2Z^3` never record, and line 128 uses that. Say it in the statement, as the draft does.
- **Item 69 (Theorem 13): `y` can record when `q` is finite.** Take `S = 1/2` and `a_e = √3π/4`, a window point. Then `θ = π/4`, `φ = 0`, `U = e^{−iπσ_x/4}` and `q = 4`. With `k = 3` the tick-1 vector is `U^{−2}|y⟩ = iσ_x|y⟩ = i|x⟩`, so `p_1 = 1`. Then `y` is empty with probability one, agrees with its five empty neighbours other than `x`, and records at tick 1. `[check]`: `p_1, …, p_5 = 1, 1/2, 0, 1/2, 1`. Theorem 13 claims nothing about `y`, and line 128 does not need it: no new record forms at tick 2 (`p_2 = 1/2 < 1`), and `x` records at tick 3. No edit is required; one sentence would help readers.
- **Item 81 (check record).** "the two configurations in Theorem 12" are the draft's items (3) and (4): `v_1`, and the pair `v_2, b_2` (`TM1_DRAFT.md` line 333).
- **Item 86 (Corollary 17).** "If `B` is finite, at most `|B^{+3}|` records form after tick 1" holds under the first sentence's hypothesis `F_1(ω_v) = Z^3`. Without it the bound is false: take `ω_0 = ω_v` equal to the state of Theorem 12 and `B = ∅`; every site first records at tick 2. Write "In that case, if `B` is finite, ...".
- **Notation.** Definition 3 and Theorem 3 write `β_g`, `β_h` for lifts. `LW1.md` line 70 writes `β_h` for the half-step automorphism. Inside TM1.md, Definition 3 fixes the meaning, so nothing is wrong. Another letter would help a reader who has both files open.
- **Definition 8's "full saturation".** TM1.md uses it only inside conditional statements ("Under the explicitly inferred full-occupancy definition of saturation"). It fixes no reading of TM1(a)(2). As notation it passes the four tests, in the same way as the notion of section 3.2.

## 3. The distiller's GAPs

TM1.md marks one GAP paragraph (line 5). It has two parts.

### 3.1 GAP (a): no selected transport for non-factor states

**The text.** "PS-3 does not select a transport for every non-factor state. The formation-set statements still follow from the prescribed one-time Born marginals, but statements about a PS-3 history require an available history measure with those marginals."

**Is it real?** Yes, as a fact about the working set. The owner held non-factor states: "PS-3 selects one transport at factor states only" (`TOE_ASSEMBLY.md` line 197). For states that are not cell invariant, no infinite-volume rule exists (LW1-N, `LW1.md` line 504). The states of Theorem 13 and Corollary 14 are not cell invariant, so no PS-3 rule on file applies to them.

**Is it load-bearing?** No. `F_n`, `R_n` and `t_x` are functions of the state sequence (Theorem 1). Every probability statement in TM1.md is about contents `r_x = ξ_{2t_x}(x)` and uses the Born law at one tick. So each holds for every measure on histories with the prescribed one-time marginals. Lemma R2 shows that such measures exist for every initial state.

**Lemma R2 (history measures with the prescribed marginals exist; referee closure).** Take a live law and an initial state `ω_0`. For each half-tick `h` let `ν_h` be the Born law of `ω_h` on `Ω = ∏_x V_x` (`LW1.md` line 77; for `h = 2n`, `ω_h = ρ_n`). Then there is a probability measure `Q` on `Ω^{N_0}` whose time-`h` marginal is `ν_h` for every `h`. Every statement of TM1.md about record contents holds under `Q`.

*Proof.* `Ω` is a countable product of finite sets, hence compact metrizable. The finite products `⊗_{h∈H}ν_h`, `H ⊂ N_0` finite, are consistent. Kolmogorov's extension theorem gives `Q = ⊗_hν_h`, with time-`h` marginal `ν_h`. Theorem 1's content law uses only `Q(ξ_{2n}(x) ≠ ξ_{2n}(y)) = ν_{2n}(ξ_x ≠ ξ_y) = ρ_n(D_xy)` and `Q(ξ_{2n}(y) = v) = ρ_n(Π_y(v))`. Theorem 5's content clause and line 48 use the joint law of `ξ_2` at the single tick 1. All are one-time quantities. ∎

`Q` respects no transport support. `LW1.md` E5 gives supported Markov measures on `L_cube`, with steps from `𝒪_h` on cell-invariant sequences. TM1 needs neither property. So TM1's "history" statements hold for every PS-3 history, once one is selected, and for every other measure with these marginals. The owner's held decision on non-factor states is untouched. **Repair.** Add R2's first two sentences to Definition 7 (section 2.3, item 13). The GAP can then read "not load-bearing; see Definition 7".

### 3.2 GAP (b): the reading of saturation

**The text.** "Also, the draft's assertion that TM1(a)(2) holds *exactly* in case (E) requires a definition of saturation: if a count that never grows is called saturated at zero, case (N) is vacuous. The statements below use full occupancy as saturation. A counterexample with an intermediate flat tick is given for boxes containing the specified sites."

**Against the draft.** The draft's Corollary 2.9 states its reading (`TM1_DRAFT.md` line 205): "Read "saturation" as "every site of the box carries a record". Then TM1(a)(2) holds for `ω_0` exactly in case (E)". So Corollary 2.9 itself is not affected. Section 5.2 (line 376) repeats the result and points to Corollary 2.9; the FINISH (line 403) repeats it without the reading. Section 5.2 (line 378) and the FINISH counterexample (line 413) claim more: "Under any reading of "saturation", the state of Proposition 3.7 on `L_cube` with `k = 3` is a counterexample". R1(ii) below shows that claim false. So the gap is real against lines 378, 403 and 413. The distiller's repair (full occupancy, stated as a condition) is correct.

**Notation.** A reading of saturation says, for each finite box `Λ`, state and tick `s`, whether `Λ` is saturated at tick `s`. Let `s*` be the least such `s` (`∞` if none) and `c_n = |R_n ∩ Λ|`. TM1(a)(2) at `Λ` under the reading means `c_{n+1} > c_n` for every `0 ≤ n < s*`. Call a reading *monotone* if `c_n = c_s` for every `n ≥ s` whenever `Λ` is saturated at tick `s`.

**Four-test check of "monotone reading".** It is notation for a quantifier in R1, not a proposal. (1) It states or fixes no part's target and no reading: pass. (2) It is one closed condition: pass. (3) It settles no physics question by premise; R1's conclusion is proved: pass. (4) It adds no structure or constant: pass.

**Proposition R1 (referee closure).** On `L_cube` take `S = 1/2`, any window point, `k = 3`, and the state of Theorem 13. Let `Λ` be a finite box that contains `x = 0` and a site `z ∉ {x, y}`.
- (i) Under every monotone reading of saturation, TM1(a)(2) fails at `Λ`. Full occupancy is monotone.
- (ii) Under the reading "`Λ` is saturated at tick `s` when `c_{s+1} = c_s`", TM1(a)(2) holds at every finite box for every state of the three laws.

*Proof.* (i) Theorem 13 gives: `z` records at tick 1, no site records at tick 2, and `x` records at tick 3. So `c_0 = 0 < c_1`, `c_2 = c_1` and `c_3 = c_2 + 1`. Suppose `s* ≤ 2`. Monotonicity gives `c_2 = c_{s*} = c_3`, a contradiction. So `s* ≥ 3`, and TM1(a)(2) requires `c_2 > c_1`, which fails. Full occupancy is monotone: once every site of `Λ` carries a record, `c_n = |Λ|` for all later `n`, since `R_n ⊆ R_{n+1}` and `c_n ≤ |Λ|`. (ii) Under this reading `s*` is the least `s` with `c_{s+1} = c_s`. For `n < s*`, `c_{n+1} ≠ c_n`, and `c_{n+1} ≥ c_n` because `R_n ⊆ R_{n+1}`. So `c_{n+1} > c_n`. ∎

R1(ii) is the distiller's remark made exact: under that reading no state is a counterexample, so "under any reading" is false. R1(i) is the exact form of TM1.md line 128 (item 93).

## 4. Checks behind the verdicts, section by section

### 4.A Head and section 1 (items 1-14)

- **Definition 1.** TM1's cubes `2b+{0,1}^3` and `2b+1+{0,1}^3`, `b ∈ Z^3`, are LW1's `b+{0,1}^3` and `b+1+{0,1}^3`, `b ∈ 2Z^3` (`LW1.md` lines 36-37). A1 (line 182): "Each positive edge belongs to exactly one cube in exactly one of the two tilings." A2 (line 205): "The action on sites is transitive". A2's proof (line 207) shows that both tilings are preserved.
- **Definition 2.** The base tick, angles and window match `LW1.md` lines 26, 55 and 68. The infinite products are E1's automorphisms (line 397). The register gap is item 8.
- **Definition 4.** PS-3h5 (`LW1_5_DRAFT.md` line 324): "under `L5-O[S_+]` the site parities `P_x = ±1`; under `L5-U` the site numbers `N_x ∈ {0, …, 5}`". Covariance of `P_x`, rebuilt. From `c_j = (γ_{2j−1} + iγ_{2j})/2`, `n_j = (1 + iγ_{2j−1}γ_{2j})/2`, so `1 − 2n_{x,j} = −iγ_{x,2j−1}γ_{x,2j}`. The lift maps `γ_{x,a}` to `sγ_{gx,a}` with one sign `s` for all ten `a` at `x`: `VC1_5_DRAFT.md` line 178 ("`β_g` maps each `γ_{x,a}` to `±γ_{gx,a}`") and `LW1_5_DRAFT.md` line 394 ("A2's sign correction `d(x)` is implemented on matter by `Ad P_x` (`P_xγ_{x,a}P_x = −γ_{x,a}`)"). Then `β_g(1 − 2n_{x,j}) = −is^2γ_{gx,2j−1}γ_{gx,2j} = 1 − 2n_{gx,j}`, and `β_g(P_x) = P_{gx}`. For `N_x`: VC1 Lemma C(iii), line 83.
- **Definition 5.** Even elements at distinct sites commute, so the `Π_x(v)` and `Π_y(w)` commute. `Σ_vΠ_x(v)Π_y(v)` is a sum of mutually orthogonal projections, hence a projection, and `D_xy` is its complement. For `L_cube`, `D_xy = (n_x − n_y)^2` (`LW1.md` line 77); for `L5-O`, `D_xy = (1 − P_xP_y)/2`.
- **Definitions 6-8.** Definition 6 is `LW1.md` lines 77-82 with the general `D`. Definition 7 is discussed in sections 2.3 and 3.1. Definition 8 is used only conditionally.

### 4.B Section 2 (items 15-42)

- **Theorem 1.** `ρ_n(D_xy + D_xz)` is a number fixed by `ω_0` and the law. `N(x)` has six elements, so finitely many numbers decide `x ∈ F_n`, and `R_n`, `t_x` follow by recursion. No configuration enters. At `n = t_x` with a copy neighbour `y`, any `Q` with the prescribed marginal at tick `n` has `Q(ξ_{2n}(x) ≠ ξ_{2n}(y)) = ρ_n(D_xy) = 0`, so `r_x = ξ_{2n}(y)` almost surely and `Q(r_x = v) = ρ_n(Π_y(v))`. For mixtures, `ρ_n = λρ'_n + (1−λ)ρ''_n` because `α^n` is linear, and a positive combination of two nonnegative numbers vanishes exactly when both do.
- **Line 30.** The trace is invariant under `α` and has `τ(D) > 0` on every link (Theorem 6). So for `λ < 1` the mixture has `ρ_n(D) ≥ (1−λ)τ(D) > 0` on every link at every tick, and no record ever forms.
- **Theorem 2.** Stationarity gives `ρ_n = ω_0` by induction. If `ω_0∘α^p = ω_0`, then `ρ_{n+p} = ω_0∘α^p∘α^n = ρ_n`, so `F_{n+p} = F_n`. A site in some `F_n` lies in some `F_j` with `1 ≤ j ≤ p`.
- **Theorem 3.** `ρ_n∘β_h = ω_0∘α^n∘β_h = ω_0∘β_h∘α^n = ρ_n`. Each `Π_x(v)` is a polynomial in `a_x` (finite spectrum), so `β_h(Π_x(v))` is the same polynomial in `a_{hx}`, which is `Π_{hx}(v)`; hence `β_h(D_xy) = D_{hx,hy}`. `h` is a lattice isometry (`LW1.md` line 211: "a cube-centred rotation followed by an integer translation"), so `hy ≠ hz` lie in `N(hx)`. `F_n` is `H`-invariant, and transitivity leaves `∅` or `Z^3`.
- **Theorem 4.** Theorem 2 gives `R_n = F_1` and `ρ_1 = ω_0`; Theorem 3 gives `F_1 ∈ {∅, Z^3}`; one site decides.
- **Theorem 5.** `LW1.md` A2 (line 211): "A rotation about a site must fix the centre of its even cube; its stabilizer consists of the identity and the two turns about that body diagonal." Put `s_i = +1` for even `x_i` and `−1` for odd. The even cube of `x` has centre `x + s/2`, and its odd cube has centre `x − s/2`. Both lie on the line `x + Rs`. The order-3 turn about that line permutes the three edges at the corner `x` of each cube cyclically. By A1 each link at `x` lies in one of these two cubes. So the stabilizer has one orbit on the even links at `x` and one on the odd links. With site transitivity, `𝒢` is transitive on even links and on odd links (`VC1_5_DRAFT.md` Lemma S2′(b), line 94, says the same). `D_xy = D_yx`, so `ρ_n(D_ℓ)` is defined on unoriented links and constant on each orbit. The cube edge graph is connected, and a countable union of null events is null.
- **Line 48.** Both components are stationary and symmetric (Theorem 6), and `D = 0` in both, so every site is in `F_1`. Born laws are affine in the state, so the tick-1 law is `(δ_0 + δ_1)/2` on the all-0 and all-1 configurations.
- **Theorem 6.** Checked against `VC1_5_DRAFT.md`. O2 (lines 162-167) and Remark O2.1 (line 195): "In `ω_0` every `P_x = +1`; in `ω'_0` every `P_x = −1`; and `P_x ∈ 𝔄^G`." U3 (line 244): filling `0`, and "With full matter in place of the vacuum the same holds with `Q_x = 5 + 3m` and filling `5`"; since `0 ≤ N_x ≤ 5`, both fillings make `N_x` sharp. U1 (line 222): "the product state with density `e^{−tN_x}/Z_t` on each site ... and the normalized trace on each register", for `t ∈ [−∞, ∞]`. So under `ω_t`, `N_x` has law `p_k = C(5,k)e^{−tk}/(1+e^{−t})^5`, independent across sites, and `Σ_kp_k^2 < 1` as soon as two `p_k` are positive. For the `L_cube` dark states: each `H_C` kills (empty matter) ⊗ (any link vector) and (full matter) ⊗ (any link vector); `W_E` acts on links only and fixes the trace; lifts map `n_x` to `n_{gx}` and act on links by unitaries (`LW1.md` line 243); `e^{it𝒢_x}` is `e^{itn_x}` times a link unitary. Traces: VC1 Lemma 2.4(a) (line 141), "`τ∘β = τ` for every automorphism `β` that maps each local algebra into a local algebra". Under `τ` the modes are independent fair bits, so the disagreements are `1/2`, `1/2` and `1 − C(10,5)/1024 = 772/1024` (Vandermonde: `Σ_kC(5,k)^2 = C(10,5) = 252`). Free seas: `LW1.md` B8a (line 291): "Under the free tick and PS-3c, starting from the free sea, no record forms." `LW1_5_DRAFT.md` B8a-5 (line 400): "Under the free tick and PS-3c read with PS-3h5, from the free sea, no record forms", and the same for `N_x`.
- **Line 54.** U1 includes `t = +∞` (matter vacuum), where `N_x = 0` is sharp. Each site density `e^{−tN_x}/Z_t` converges in norm to the vacuum projection, so the product states converge on every local element. `LW1U_SEA_DRAFT.md` line 183: "Let `(eps, mu)` lie in the window and off `Σ_π`. Build a history measure from `ω_P` as in `LW1.md` E5, with each step selected from `O_h`. Then `ξ_h = ξ_0` for every `h`, almost surely". Line 177 defines `Σ_π = {2 eps + mu = pi, 0 < mu < pi/2}`. TM1.md's summary and its conditional label are right.

### 4.C Section 3 (items 43-81)

- **Preamble.** VC1 Lemma 1.1 (lines 71-74): `E` is the identity on `𝔄^G`, commutes with `α` and the lifts, and `ω∘E` is gauge invariant. `P_x ∈ 𝔄^G` (line 195) and "`N_x` and `Q_x` are gauge invariant" (line 250), so each `D_xy ∈ 𝔄^G`.
- **Lemma 7.** The forward term `c_y^†Jc_x` is nonzero exactly at `(n_x,n_y) = (1,0)` and `e < S`, the reverse term exactly at `(0,1)` and `e > −S`. For `−S ≤ e ≤ S−1`, `S(S+1) − e(e+1) = (S−e)(S+e+1) > 0`, so `j(e) > 0`. The two conditions exclude each other.
- **Lemma 8.** Every `H_C` kills the vector, so each matter gate fixes it. `W_E` is diagonal in `E_ℓ`. Each `𝒢_x` is diagonal in the labels. `α(A)` uses finitely many gates (E1).
- **Lemma 9.** `h^U_ℓ = Σc^†_{y,j}U^{jk}_ℓc_{x,k} + Σc^†_{x,k}U^{jk†}_ℓc_{y,j}`, `U^{jk}_ℓ = r^{ℓ,y}_jr^{ℓ,x†}_k` (`VC1_5_DRAFT.md` line 58). Take `x` full and `y` empty. The second sum has `c_{y,j}` on an empty site. In the first, `r^{ℓ,x†}_k` kills a full `x`-end when `m ≥ 5`, and `r^{ℓ,y}_j` kills the `y`-end, which holds `m − min(m,5) = 0` rishons, when `m ≤ 5`. The case `y` full is symmetric, and the equal cases are immediate.
- **Lemma 10.** With `γ_{2k−1} = c_k + c_k^†`, `γ_{2k} = −i(c_k − c_k^†)` and `U^{ab} = iη^y_aη^x_b`, the coefficients of `c^†_{y,k}c^†_{x,j}`, `c^†_{y,k}c_{x,j}`, `c_{y,k}c^†_{x,j}` and `c_{y,k}c_{x,j}` are `4id^y_kd^x_j`, `4id^y_kd^{x†}_j`, `4id^{y†}_kd^x_j` and `4id^{y†}_kd^{x†}_j`. The first matches `𝒰^{++}` (`VC1_5_DRAFT.md` line 174); the others follow from the same expansion. `d^x_j|0⟩ = 0`, and `d^y_kd^{x†}_j|0⟩ = −d^{x†}_jd^y_k|0⟩ = 0`. The fourth multiplies `c_{y,k}c_{x,j}`, which is zero when `x` or `y` is empty. `Γ^x_ℓ = ∏_k(iη^x_{2k−1}η^x_{2k}) = ∏_k(2n^x_k − 1) = −1` on `|0⟩` (line 176).
- **Theorem 11.** No two sites of `2Z^3` are neighbours. A site `x ∉ 2Z^3` has `x ± e_i ∈ 2Z^3` exactly when `x_i` is its only odd coordinate, so it has at most two marked neighbours. Even translations need no sign correction (`LW1.md` line 205: "Even translations preserve its phases exactly"; VC1 Lemma C's proof, line 86: "Even translations need `d = 1`"), and `E∘β_t = β_t∘E` (Lemma 1.1(d)). The actual values are sharp: `1, 5, −1` at marked sites and `0, 0, +1` elsewhere. The stationarity step is item 58.
- **Theorem 12.** `ψ` is an even product over disjoint regions. Lifts map even cubes to even cubes and `n_x` to `n_{gx}`; gauge transformations act as above. `α^{−2}` commutes with lifts and gauge transformations because `α` does. At tick 2 the state is `ψ`, constant on even cubes. At tick 1, `ρ_1(D) = ψ(U_0DU_0^*) = Σ_vp_v‖DU_0^*v‖^2`, with `p_v > 0` for every configuration that is constant on even cubes; this needs a finite union of even cubes containing all gates used, and `ψ` restricted there is diagonal. For odd neighbours of `x = (1,1,1)`: `v_1` is frozen, `x` is full and `x + e_i` empty. For even neighbours: `U_0^*v_2 = ζ[cos(a_oh)v_2 − iσ sin(a_oh)b_2]` with `h = j(m)/√3`, `|ζ| = 1`, `σ = ±1`; `W_E^*` acts first and gives a phase, `M_o^*` acts through the cube `{1,2}^3`, and `M_e^*` fixes both vectors. Then `D_{xy}v_2 = 0` and `D_{xy}b_2 = b_2` for `y ∈ C_0`, so `ρ_1(D_{xy}) ≥ p_{v_2}sin^2(a_oh) > 0`. Window clause: `j(−S) = (2S)^{1/2} ≤ √3` for `S ≤ 3/2`, and `0 < a_o < 2ε < π`. For fixed `S` and `m`, `a_oj(m)/√3 ∈ πZ` holds for finitely many `a_o ∈ (0, π)`. The labels issue is item 66.
- **Theorem 13.** `ℓ = (0, e_1)` is an even link of `C_0`. On `|x⟩` and `|y⟩` every other link is blocked. With one particle no fermion sign enters, and `η_1(0) = 1`, so `H_{C_0}` acts as `+(j(m)/√3)σ_x` (`[check]`). `M_e` acts as `cos θ − i sin θ σ_x`. `W_E` gives `diag(e^{−iτ_Em^2}, e^{−iτ_E(m+1)^2})`, which is a phase times `diag(e^{iφ/2}, e^{−iφ/2})` with `φ = τ_E(2m+1)`. Gauss: at `x`, `1 + m` against `0 + (m+1)`; at `y`, `0 − m` against `1 − (m+1)`. A site `z ∉ {x, y}` is adjacent to at most one of `x, y` (no site is adjacent to both `0` and `e_1`), so it has at least five empty neighbours. `x` has five neighbours other than `y`, all empty; it disagrees with `y` with probability one. Write `U = e^{iχ}(cos β + i sin β u·σ)`. The off-diagonal entries of `U` have modulus `|sin θ|`, so `sin β ≠ 0` and `(u_1, u_2) ≠ 0`. `⟨x|U^r|y⟩` is `e^{irχ} i sin(rβ)(u_1 − iu_2)`, zero exactly when `U^r` is scalar. For `1 ≤ n < k ≤ q`, `U^{k−n}` is not scalar, so `p_n > 0`; `p_k = 0`. For `k = 3`, `y ∈ F_2` needs `U^{−1}` anti-diagonal, and an anti-diagonal unitary has a scalar square. For `S = 1/2`: `a_e = ε − μ/2 ∈ (0, π/2)`, so `θ = a_e/√3 ∈ (0, π/(2√3))`; `rθ ∈ πZ` needs `r > 2√3`, so `q ≥ 4`.
- **Corollary 14.** Copies at `x_k = (8k,0,0)` are at least 7 apart, so their cubes, links and copy neighbourhoods are disjoint, and every link other than the `ℓ_k` is blocked in every branch. The local vector states are even, so their infinite product is a state. Item 78 records the missing hypothesis.
- **Line 104.** A site outside all copies is adjacent to at most one copy site, so it records at tick 1. `y_k` would need `U^{n−k}` anti-diagonal, hence `U^{2(n−k)}` scalar, which `q = ∞` forbids unless `n = k`, where `U^0 = 1` is not anti-diagonal. At `t_{x_k}`, `p = 0`, so the content is `0`.
- **Line 106.** It matches the draft's section 3.5 (line 333) and the draft's own label "it proves nothing". The script was not looked for: this lane's rules keep it inside its own scratch folder.

### 4.D Section 4 (items 82-90)

- **Lemma 15.** `α(A) = M_e^*M_o^*W_E^*AW_EM_oM_e` (`LW1.md` line 70). Conjugation by single-link gates keeps `𝔄(Λ)`. An odd cube that meets `Λ` lies in `Λ^{+1}`, since a cube has sup-diameter 1, and its links have both ends in it. A gate disjoint from the support of `A` commutes with `A` (E1, line 405: "A further gate disjoint from \(F\) commutes with \(A\), by evenness"); registers are ordinary tensor factors (`LW1.md` line 48; `LW1_5_DRAFT.md` line 305; `VC1_5_DRAFT.md` line 58). Then `(Λ^{+a})^{+b} ⊆ Λ^{+(a+b)}` and induction.
- **Theorem 16.** `D_xy + D_xz ∈ 𝔄(B_∞(x,1))`, so `α^n(D_xy + D_xz) ∈ 𝔄(B_∞(x, 2n+1)) ⊆ 𝔄(Z^3∖B)` and is even. Earlier ticks have smaller cones.
- **Corollary 17.** `n = 1` gives sites at sup-distance at least 4; a site carries one record; `R_n(ω_v) = ∅` gives `R_n(ω_0) ⊆ B^{+(2n+1)}`.
- **Line 122.** A link that meets `B` lies in neither `𝔄(B)` nor `𝔄(Z^3∖B)`, so the two algebras have disjoint supports, and an even `A` commutes with `W`. `(c_x + c_x^†)^2 = c_xc_x^† + c_x^†c_x = 1`. The gauge unitary `V_x(g)` is a product of a site factor and one factor per link end (its generator, `VC1_5_DRAFT.md` lines 56 and 58, is a sum of commuting terms of that form). Conjugating `A` by it uses only the factors on `A`'s support, so `E(A) ∈ 𝔄(Z^3∖B)`, and `E(A)` is even. For the trace, `τ(W^*AW) = τ(AWW^*) = τ(A)`.

### 4.E Section 5 (items 91-97)

- **Line 126.** The count is a number (Theorem 1). In case (E) it is `0, |Λ|, |Λ|, …`; under full occupancy this rises once and saturates. In case (N) it is `0, 0, …` and never saturates.
- **Line 128.** The trace count stays `0`. A box with a marked site in Theorem 11's state has a count that is constant after tick 1 and below `|Λ|`. The flat-tick sentence is item 93.
- **Line 130.** Theorem 2 allows growth at tick 1 only, and Theorem 3 at one tick `n*` only. So growth at two ticks needs both hypotheses to fail.
- **Line 132.** `VC1_5_DRAFT.md` O2 (line 167): "`ω_0(N_x) = 5/2`". U2 (line 228): "So no state of `L5-U` with (iii) and (iv-P) is half filled." U2′ (line 234): "no state of `L_cube` that is invariant under `𝒢` and pure on its gauge-invariant algebra is half filled". `τ(N_x) = 5/2`.
- **Line 134.** `LW1_5_DRAFT.md` table rows c8 and c9 (lines 340-341): PS-3g passes tests 1, 2 and 4, and test 3 is "conditional: with PS-6r's "no actual configuration" on links, it excludes registers with `R ≅ R^σ` (no frame-invariant site value), so it decides the component group in GA1-i's answer"; PS-3h5 is "as c8" on test 3 and "pass: it removes structure" on test 4. TM1's "affects" is weaker than the source's "decides"; that is acceptable.

### 4.F The [check]

`/tmp/toe-tm1ref/check_tm1ref.py`, output `/tmp/toe-tm1ref/out.txt`. It reports:
- Theorem 12, for `S = 1/2, 1, 3/2, 2` and every `m`: `v_1` is killed by every cube generator that touches an occupied site. With `S` on the non-mixed links, only the odd cube with base point `(1,1,1)` acts on `v_2` and on `b_2`, with amplitude `+j(m)/√3` both ways. With `−S` on the non-mixed links, the even cubes with base points `(0,0,0)` and `(2,0,0)` also act on `b_2`.
- Theorem 13, the same `S` and `m`: only the even cube `C_0` acts on `|x⟩` and `|y⟩`, with amplitude `+j(m)/√3` both ways.
- Theorem 13 with `S = 1/2`, `k = 3`: `p_3 = 0` and `p_2 > 0` at `a_e = 0.4, 1.0, √3π/4, 1.5`; at `a_e = √3π/4`, `p_1 = 1`.
- Corollary 14's data `S = 7/2`, `m = 1/2`, `a_e = π/√5`, `τ_E = √2`: `θ/π = 1` to twelve digits, `U` diagonal, `p_n = 0` for `n ≤ 6` and `k = 1, 2, 5`.
- Theorem 6: `1 − Σ_kC(5,k)^2/1024 = 193/256 = 772/1024`.

## 5. Required edits

Required before the freeze (one per non-CORRECT item):
- **E1 (line 9, item 5).** Replace "Model: gpt-6.1-terra; effort: not visible; session id: not visible." with "The distiller could not see its own effort or session id; the values above come from the run log."
- **E2 (line 17, item 9).** Replace "an imported LW1 B4/VC1 Lemma C result" with "imported: for `L_cube` from LW1 A2 and its gauged-covariance proof (`LW1.md` lines 209 and 243), for the five-mode laws from VC1 Lemma C; the covariance of `P_x` and `N_x` is shown in Definition 4."
- **E3 (line 16, item 8).** Add "`L5-O` means `L5-O[S_+]`, the proposed register; it contains the rishon vacuum." Write `C ∈ T_e` under `M_e` and `C ∈ T_o` under `M_o`.
- **E4 (line 78, item 58).** Add: "On `L5-U`, `W_E` is a function of the end numbers, so it multiplies each vector with definite end numbers by a phase; on `L5-O`, Lemma 10 gives the phase. The argument of Lemma 8 then gives stationarity on both five-mode laws." Name the `L5-U` vectors as in `TM1_DRAFT.md` line 260.
- **E5 (lines 84-86, item 66).** In line 84 write "every mixed link at its blocking value and every other link at `S`". In line 86 drop "as in the draft's blocked construction".
- **E6 (line 100, item 78).** "If the data in Theorem 13 have `sin θ ≠ 0` and `q = ∞`".
- **E7 (line 128, item 93).** Replace "Thus a definition of saturation consistent with a later increase cannot make the earlier flat step satisfy strict increase until saturation." with Proposition R1(i) (section 2.2 gives the wording).

Recommended precision edits (no content changes):
- **P1 (line 40).** Theorem 4: "exactly when, at one site `x_0`, two neighbours `y ≠ z` have `ω_0(D_{x_0y}) = ω_0(D_{x_0z}) = 0`."
- **P2 (lines 5 and 21).** Definition 7: add R2's existence sentence. The GAP line can then say that GAP (a) is not load-bearing, and that the draft's Corollary 2.9 already states full occupancy; the overstatement was the draft's "under any reading".
- **P3 (line 52).** Cite `LW1.md` B10(3) and `LW1_5_DRAFT.md` A2-5 for the free seas' stationarity and symmetry.
- **P4 (line 60).** "coefficient `±j(e)` or `±j(e−1)`".
- **P5 (line 68).** Define a sector product vector: definite site numbers and definite end numbers.
- **P6 (line 76).** Add "and no site of `2Z^3` ever records".
- **P7 (line 118).** "In that case, if `B` is finite, ...".
- **P8 (line 106).** "the configuration `v_1` and the pair `v_2, b_2` in Theorem 12".
- **P9 (after line 98, optional).** "For finite `q`, `y` may record; for example `S = 1/2`, `a_e = √3π/4`, `k = 3` gives `p_1 = 1`. Nothing below uses `y`."

## 6. Open statements to carry by name

- **TM1-i, remaining parts** (`TOE_ASSEMBLY.md` line 297; TM1.md line 7). Which state VC1 selects, and so whether its vacuum is in case (E) or (N). For a stationary `𝒢`-symmetric candidate, Theorem 5 reduces this to one even and one odd link of that state. The formation rate outside the stated cases. PS-4 stays a premise.
- **The domain or form of TM1(a)(2)** (LW1-R, moved into TM1-i by `LW1.md` Amendment 1). This is a choice for the owner and the lead, not a proof obligation. What holds is on record: under full occupancy, TM1(a)(2) holds in case (E) with one rise at tick 1 and fails in case (N) (line 126); it fails for the trace, for Theorem 11's state and, under every monotone reading, for Theorem 13's state (R1(i)); and under one non-monotone reading it holds for every state (R1(ii)).
- **The free-sea excitation question** (TM1.md line 7, unlabelled): whether some local excitation of the free sea forms records at infinitely many ticks. Corollary 17 confines its records at tick `n` to `B^{+(2n+1)}`. Neither TM1 pass nor this report attacks it. A short label (for example TM1-FS) would make it citable.
- **Inherited, not TM1's own:** VC1 (the gauged vacuum), LW1-U_f with LW1-U_hop, LW1-N and GA1-P. Only line 54's remark touches them, and it is labelled conditional.

## 7. Freeze recommendation

**Freeze TM1.md after edits E1-E7.** The P edits are recommended and change no content. No proved conclusion is overturned. The dichotomy (Theorems 1-5) is correct as stated: for any site-covariant actual values and any tick automorphism whose lifts commute with it, a stationary state invariant under lifts of a site-transitive subgroup records everywhere at tick 1 or never, and under `𝒢` the case is read from one link of each tiling. Theorem 6 is correct as a conditional on the provisional `VC1_5_DRAFT.md` and `LW1_5_DRAFT.md` results, and TM1.md labels it so. The examples of section 3 are correct with E3-E6. Section 4 is correct. Section 5 is correct with E7. After the freeze, TM1 reopens only on a `wrong` signal, or if an input it reads changes: VC1 O2, O2.1, U1, U3, U2 or U2′, LW1-5's PS-3h5 or B8a-5, or `LW1U_SEA_DRAFT.md` Corollary 3.3 (context only).

---

## FINISH

**Proved here (referee closures).**
- Lemma R2: for every live law and every initial state, a measure on histories with the prescribed one-time Born marginals exists (the product of the marginals). Every record-content statement of TM1.md holds for every such measure. GAP (a) is real as a limit on "PS-3 history" and is not load-bearing.
- Proposition R1: (i) under every monotone reading of saturation (full occupancy is one), the box of Theorem 13 with `S = 1/2`, `k = 3` violates TM1(a)(2); (ii) under the reading "saturated at the first tick at which the count does not rise", TM1(a)(2) holds for every state. GAP (b) is real against the draft's "under any reading" and is repaired by R1.
- The closure of item 58: on `L5-U`, `W_E` multiplies vectors with definite end numbers by a phase, so Theorem 11's five-mode states are stationary.
- The verdicts: 97 items, 90 CORRECT, 2 ERROR, 5 INCOMPLETE. Every proof in TM1.md was re-derived, and every cited pass-1 line was checked.

**Counterexamples.**
- To the draft's "Under any reading of "saturation", the state of Proposition 3.7 on `L_cube` with `k = 3` is a counterexample" (`TM1_DRAFT.md` lines 378 and 413): R1(ii).
- To the proof of Corollary 14 without `sin θ ≠ 0`: `S = 7/2`, `m = 1/2`, `a_e = π/√5`, `τ_E/π` irrational. Then `q = ∞` and `sin θ = 0`, and every `x_k` records at tick 1. The statement survives at this point through `m = −1/2`.
- To the step "After the hop all other links at the two endpoints are blocked" of Theorem 12, read with TM1.md's own configuration: the label `−S` on `(x − e_1, x)` leaves that link unblocked after the hop (Lemma 7), and `[check]` shows two even cubes acting on `b_2`. The draft's labels repair it (E5).
- To Corollary 17's count bound read without `F_1(ω_v) = Z^3`: `ω_0 = ω_v` equal to Theorem 12's state and `B = ∅`.

**Open by name.** TM1-i, remaining parts: the VC1 state's case, the formation rate, PS-4. The domain or form of TM1(a)(2) (LW1-R): an owner and lead decision. The free-sea excitation question (TM1.md line 7). Inherited and not TM1's own: VC1, LW1-U_f with LW1-U_hop, LW1-N, GA1-P.

**What changes downstream.**
- TM1: freeze after E1-E7. The dichotomy stands as TM1-i's answer for stationary symmetric states.
- VC1: unchanged. (a)(4) is one bit for each stationary symmetric candidate, read from one even and one odd link.
- The assembly: under full occupancy TM1(a)(2) holds exactly in case (E) and fails for some initial states; "under any reading" is false. The choice of domain or restatement stays with the owner and the lead.
- `L5-O` results that use the rishon vacuum are for `L5-O[S_+]` (E3).
- No proved result of `LW1.md`, `VC1_5_DRAFT.md` or `LW1_5_DRAFT.md` changes.
