lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SGAP referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 (referee) under PR #10138's method: Claude drafts at length and runs to closure (`SGAP_DRAFT.md`), Codex distils (`SGAP.md`, by Codex gpt-6.1-terra), a fresh session referees, then the owner freezes. This session wrote neither pass 1 nor pass 2. This is one check: one line-by-line read of `SGAP.md`. It reviews no other review.

**What this file is.** A referee report. It grants no status, adopts no law, reading or definition, and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "[check]" marks a tiny scratch computation in `/tmp/toe-SGAPref/`; a check guides or refutes and never proves.

**Text read.** `SGAP.md` as of commit `e6c5cab1f` (the last commit that touches it; branch `claude/toe-assembly` head). SHA-256 of the file read: `da3aa200cfe0479017e1693db48c81c871c6c71c778dca9a4b0a554be920f17d`. Line numbers below refer to that file.

**Sources read, with commits.** All at `claude/toe-assembly` commit `e6c5cab1f` unless named.

| File | Last commit touching it | Lines read |
|---|---|---|
| `SGAP.md` | `e6c5cab1f` | 1-135 (all) |
| `SGAP_DRAFT.md` (SHA-256 `c2715daa…6122dab8`) | `b21cbe0fc` | 1-25, 36-38, 59-79, 189-251 |
| `prior/SGAP.md` | `6e22793b6` | 1-92 (all) |
| `SMG15.md` | `373e01725` | 11-26, 30-66, 130-162; lines 1-217 scanned by grep for headings and names |
| `SMG1.md` | `373e01725` | grep hits only: lines 41, 43, 49, 53, 69, 132, 134, 139 |
| `SMG15_REFEREE.md` | `7a7a141af` | 241-249 |
| `TOE_ASSEMBLY.md` | `47e819786` | 257-266 (§3.10) |
| `CH1.md` | `777e071c3` | names of open items only (grep, line 24) |
| `LW1_REFEREE.md`, `Y2W_DRAFT.md` | `5a2a0affe`, `92e03055c` | 1-80 and 1-30, for the format only |
| `origin/main` (`f5af11cd0`, `git fetch -q origin main`, `git show` only) | per file, section 4.5 | the digest's quoted lines of three notes (section 4.5) |

**Working-set entries used.** SMG1-GAP (bounded R-GEN, `TOE_ASSEMBLY.md` §3.10), only as the owner's frame against which this report judges. PS-5 and PS-6r enter only through the rung-1 carrier of `SMG1.md` that `SGAP.md` uses. No other entry is used.

**Counts.** 48 items: 47 CORRECT, 1 ERROR, 0 INCOMPLETE. No ERROR changes the content of a theorem. Referee closures: R-w (section 3.1) and the A5 window identity in full (section 3.2). Sharpened hypotheses: (G1′) and (HF-alt) (section 3.3). Every distiller GAP is real; the `w>0` GAP is closed by R-w. No `[check]` was run.

**Method.** Every proof step was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. Owner guidance applied, verbatim: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The owner chose bounded R-GEN for SMG1 rungs (`TOE_ASSEMBLY.md` 3.10); this report judges against that choice.

---

## 1. Verdict table

Item numbers are fixed. Line numbers refer to `SGAP.md` at `e6c5cab1f`. Notes marked "N" are in section 2.

| # | Item (SGAP line) | Verdict | Note |
|---|---|---|---|
| 1 | Status paragraph (3) | CORRECT | Each claim is proved below; S-GAP and S-GAP⁰ are correctly OPEN. |
| 2 | GAP summary (5) | CORRECT | Matches lines 105, 125, 127, 129. "positive weight … not proved" should note that the bound implies it (R-w, section 3.1; edit E6). |
| 3 | Provenance (7) | CORRECT | All seven SHA-256 values verified (section 4 head). |
| 4 | Definition 1 (13) | CORRECT | Matches `SMG15.md` line 15; keep its "a restriction, not a derivation" clause (edit E5). |
| 5 | Definition 2 (14) | CORRECT | Matches `SMG1.md` lines 49, 53. `P^χ_x`, `ρ_a` are defined in `SMG15.md` §1 item 5, not §2 (edit E7). |
| 6 | Definition 3 (15) | CORRECT | `H_ε` equals `SMG15.md` line 150; `E_L` checked (N15). |
| 7 | Definition 4 (16) | CORRECT | Matches `SMG15.md` lines 148-152. |
| 8 | Definition 5 (17) | CORRECT | `n_x(χ)` solves `m(χ)(−1)^{n_x}=p_x`. |
| 9 | Definition 6 (18) | CORRECT | |
| 10 | Proposed readings paragraph (20) | CORRECT | Matches `SMG15.md` lines 24, 26 and the draft's FINISH (section 4.4). |
| 11 | Theorem 1, statement (24) | CORRECT | Symmetries, sign flip `ε→−ε`, eight even charges, bijection `b↦ρ_aρ_b`. |
| 12 | Theorem 1 proof, symmetry part (26) | CORRECT | N12: `R` flips exactly one endpoint of every bond, the wrap bond included, because `L` is even. |
| 13 | Theorem 1 proof, charge part (28) | CORRECT | `U_{g₁g₂}=∏_xP_x(−1)^{n_x}=(−1)^{L/2}=1` since `4∣L`. |
| 14 | Theorem 2 (Proposition Z), statement (30) | CORRECT | Exact for every real `t`; `Δ≤16` on the slice. |
| 15 | Theorem 2 proof (32) | CORRECT | N15: `E_L` checked (antiperiodic filling; periodic gives `−2|t|cot(π/L)`). The cited `SMG15.md` Theorem 3 covers `t≠0` only; `t=0` is immediate (section 4.2, edit E4). |
| 16 | Credit paragraph (34) | CORRECT | Citations checked (sections 4.1, 4.2). |
| 17 | Theorem 3 (Theorem A), statement (38-42) | CORRECT | Exact operator identity `YH_εY=H_ε+B`. |
| 18 | Theorem 3 proof (44) | CORRECT | N18: on-site difference `W(χσ)−W(χ)` is `16, −16, 0` as stated. |
| 19 | Corollary 3.1, statement (46-48) | CORRECT | |
| 20 | Corollary 3.1 proof (50) | CORRECT | Both variational steps and `‖B‖≤16τ+8|ε|` checked. |
| 21 | Equivalence sentence (52) | ERROR | Reasons are swapped. N21 gives the fix. The equivalence itself is true. |
| 22 | `Δ≤16+8c₀`, `Δ≤16` (52) | CORRECT | |
| 23 | Translation remark (52) | CORRECT | A remark; no claim is used later. |
| 24 | Reported pass-1 check (54) | CORRECT | Correctly labelled as reported, not reproduced. |
| 25 | Theorem 4 (Theorem C, Corollary C1), statement (58-62) | CORRECT | `2^{L−1}` sectors; 16-level chains; on-site gap `14τ`; hop rule `m(χ_x)m(χ_{x+1})=−p_xp_{x+1}`. |
| 26 | Theorem 4 proof (64) | CORRECT | N26: site-even factorization of `T`, wrap bond included. |
| 27 | Remark on Fröhlich-Pizzo and `|z|⁻²` tails (66) | CORRECT | Correctly says it verifies no stability hypothesis. |
| 28 | Proposition 4.1 (C2), statement (68) | CORRECT | The per-sector form is false at `t=ε=0`. |
| 29 | Proposition 4.1 proof (70) | CORRECT | Identity `N=k(p)+Σ_{odd sites}p_x` checked. |
| 30 | Proposition 4.2 (C3), statement (72-76) | CORRECT | Coefficient `8/(28τ)=2/(7τ)` per wall. |
| 31 | Proposition 4.2 proof (78) | CORRECT | `(hop⁰_x)²=n_x+n_{x+1}−2n_xn_{x+1}` checked. |
| 32 | Proposition 4.3 (C5), statement (80-85) | CORRECT | A valid conditional. |
| 33 | Proposition 4.3 proof (87) | CORRECT | N33: continuity of the rank-one projector and of `tr(U_gΠ)`. |
| 34 | Corollary 4.4 (C6), statement (89) | CORRECT | Holds at `t=0` and zero electric coupling only, as stated. |
| 35 | Corollary 4.4 proof (91) | CORRECT | |
| 36 | Theorem 5 (Lemma R), statement (95-101) | CORRECT | N36: the sum `Σ_c` in `H_4^{(y)}` must run over all eight flavours; required edit E2. |
| 37 | Theorem 5 proof (103) | CORRECT | N37: the commutator step is short but valid; `2√8=4√2`. |
| 38 | Consequence and distiller GAP `w>0` (105) | CORRECT | Omission real in the text; closed by referee closure R-w (section 3.1). The A4 hypothesis `W_odd≤Kw` alone suffices. |
| 39 | Proposition 5.1 (R2), statement (107-111) | CORRECT | `448²=200704`. |
| 40 | Proposition 5.1 proof, trial state (113-117) | CORRECT | N40: bond `(0,1)` is covered only if sites 0 and 1 are read as two factors; restore the draft's clause (required edit E3). |
| 41 | Proposition 5.1 proof, concavity step (119) | CORRECT | N41: secant step and Hellmann-Feynman at a differentiability point. |
| 42 | S-GAP⁰ OPEN, equivalent form (123) | CORRECT | |
| 43 | A4, removal (125) | CORRECT | GAP real. Sections 3.1, 5. |
| 44 | A5, local window (127) | CORRECT | GAP real; the needed strict increase is false. Sections 3.2, 5. |
| 45 | A6, parity-sector stability (129) | CORRECT | GAP real. Sections 3.3, 5. |
| 46 | Prior failed routes (131) | CORRECT | Matches `SMG15.md` lines 156-158; omits route 3's twist-theorem clause, harmlessly (section 4.2). |
| 47 | Other open items and the S3 remark (133) | CORRECT | Names match `SMG15.md` lines 7, 160, 162; the S3 remark is correct and correctly scoped (section 4.2). |
| 48 | Prior sources and limits (135) | CORRECT | The literature caveat is right (section 6); the digest's quotes from `origin/main` checked in section 4.5. |

## 2. Notes on items (referee re-derivations)

**N12.** Put `R=∏_{x even}(g₁g₂)_x`. Each `(g₁g₂)_x` reverses all eight `γ_{x,a}`, because `ρ_a(g₁g₂)=−1` for every `a`. It is even, so it commutes with light, link and other-site operators, with `W_x`, `N`, `P_y`, `G_y` and `U_g`. Every bond `{x,x+1}` has exactly one even endpoint; for the wrap bond `{L−1,0}` this uses `L` even. So `RT_{x,a}R*=−T_{x,a}`, `R` fixes `H_M` and `H_L`, and `R` maps each `H^χ_{1/2}` onto itself. Hence `E_χ(ε)=E_χ(−ε)`.

**N15.** At `N=L/2` (even), the two holonomies give the two boundary conditions of the free ring. Antiperiodic momenta `(2j+1)π/L` fill symmetrically and give `−2|t|Σ_{j=0}^{L/4−1}2cos((2j+1)π/L)=−2|t|/sin(π/L)`. Periodic momenta give `−2|t|cot(π/L)`, which is higher. The sign of `t` is absorbed by `k↦k+π`, which preserves both momentum sets because `L` is even. So `E_L` is the half-filled minimum.

**N18.** `Y` maps the one-dimensional `χ` line at `x₀` onto the `χσ` line, and `Y²=1`, so `YP^χ_{x₀}Y=P^{χσ}_{x₀}`. Hence `YW_{x₀}Y−W_{x₀}=Σ_χ(W(χσ)−W(χ))P^χ_{x₀}`. The coefficient is `2−(−14)=16` at `χ=1`, `−16` at `χ=σ`, `2−2=0` at the other even `χ` (then `χσ≠1`), and `0−0=0` at odd `χ`. `Y` reverses `γ_{x₀,a}`, `γ_{x₀,b}` and commutes with every other mode, so exactly the four bond terms `T_{x₀−1,c}`, `T_{x₀,c}`, `c∈{a,b}`, change sign.

**N21 (ERROR, item 21).** Line 52 reads: "such a bound forces `E_0=E_1`; the converse follows from `E_1≥E_0`." The reasons are attached to the wrong directions. The fix: "A bound `E_σ−E_1≥Δτ` for all seven `σ` gives S-GAP, because `E_1≥E_0`. Conversely, S-GAP makes every charged `E_σ` exceed `E_0`, so the minimum `E_0` is attained at `χ=1`; hence `E_1=E_0` and `E_σ−E_1≥Δτ`." The equivalence is true. Nothing downstream changes.

**N26.** Moving `c^{(†)}_x` past `γ_{x+1,a}` gives `T_{x,a}=−i(γ_{x,a}c_x†)(γ_{x+1,a}c_{x+1})+i(γ_{x,a}c_x)(γ_{x+1,a}c_{x+1}†)`. Each factor is site-even. Site-even operators at different sites commute, and on the subspace of fixed site parities they act as ordinary tensor factors. No Jordan-Wigner string appears, so the wrap bond needs no sign. Each factor maps one one-dimensional character line, times one light occupation, to another; it is a partial isometry there, so the amplitude has modulus one.

**N33.** For `|s|≤|ε|`, (G1) gives a simple lowest eigenvalue of `H_p(s)` with gap at least `Δ_Gτ`. The rank-one spectral projector `Π(s)` is then Lipschitz in `s`: the elementary finite-dimensional bound `‖Π(s)−Π(s′)‖≤2‖H_p(s)−H_p(s′)‖/(Δ_Gτ)` suffices. Each `U_g` commutes with `H_p(s)`, so `U_gΠ(s)=χ_s(g)Π(s)` with `χ_s(g)=tr(U_gΠ(s))∈{±1}`. A continuous function into `{±1}` on an interval is constant, and `χ_0=1`.

**N36 (item 36).** Line 95 writes `H_4^{(y)}=Σ_c(T_{y−1,c}+T_{y,c})` with no range, two lines after Theorem 3 used `Σ_{c∈{a,b}}`. The identity on line 97 holds when `c` runs over all eight flavours: `H_εP^σ_yΨ=E_σP^σ_yΨ+ε[H_4^{(y)},P^σ_y]Ψ`, because every other term commutes with `P^σ_y`, and `P^σ_yH_4^{(y)}P^σ_y=0`, because each term changes the character at `y` by some `ρ_c≠1`. With `c∈{a,b}` only, six flavours' commutator terms would be dropped and the identity would fail. The proof's "eight distinct lines" shows that all eight are meant. Required edit E2.

**N37.** `⟨D_yΨ,H_εD_yΨ⟩=⟨P^σ_yΨ,(H_ε+B_y)P^σ_yΨ⟩`. The atomic part of `B_y` gives `−16τ‖P^σ_yΨ‖²`. Its bond part has `P^σ_yT_{y−1,c}P^σ_y=P^σ_yT_{y,c}P^σ_y=0`. N36 gives the rest. For the bound, `P^σ_yT_{y,c}=T_{y,c}P^{σρ_c}_y`, the eight lines `σρ_c` are the eight odd lines, and Cauchy-Schwarz over `c` and then over `y` gives `X≤2√8√(wW_odd)=4√2√(wW_odd)`.

**N38 (distiller GAP `w>0`).** The omission is real in the text. If `w=0`, the summed inequality reads `0≥0`. A `σ` configuration with no `σ` line exists: put `ρ_aρ_c` at one site and `ρ_cρ_b` at another, `c∉{a,b}`. But referee closure R-w (section 3.1) shows that a `σ`-ground vector with `W_odd=0` has `w>0` when `|ε|<2τ`. So the hypothesis `W_odd≤Kw` already forces `w>0`, and the draft's sufficiency claim holds with `c₀<2`.

**N40.** The pair `(0,1)` carries `|σ⟩_0|1⟩_1`, with on-site energy `16τ`. Its internal bond terms map it to `|σρ_c,ρ_c⟩`, which is orthogonal to it, so their expectation is zero. Line 117's sentence covers this bond only if sites 0 and 1 are read as two single-site factors, as the draft says ("every bond at sites `0` and `1`"). Restore that clause (required edit E3). Inside a dressed pair, `T_{2j,c′}` maps `|ρ_c,ρ_c⟩` to `|ρ_cρ_{c′},ρ_cρ_{c′}⟩`, outside the support unless `c′=c`. With `κ=ε/(28τ)`: `8κ²·28τ=2ε²/(7τ)`, `16εκ=4ε²/(7τ)`, `1+8κ²=1+ε²/(98τ²)`. So the pair energy is `−g(ε)`, as stated.

**N41.** Let `f(s)` be the lowest eigenvalue of `H_M+sH_4` on `H^σ_{1/2}` at `t=0`. It is a minimum of affine functions, hence concave on `R`, Lipschitz on `[0,ε]`, and differentiable outside a countable set. The claim "differentiable except at finitely many points" is true by analytic perturbation theory, but concavity alone suffices. Let `S=(f(ε)−f(0))/ε`. If `f′>S` at every differentiability point of `(0,ε]`, then `f(ε)−f(0)=∫_0^εf′>Sε`, a contradiction. So some differentiability point `ε′` has `f′(ε′)≤S≤−(L/2−1)g(ε)/ε≤−(L/4)·ε/(7τ)=−Lε/(28τ)`, using `L≥8` and `1+ε²/(98τ²)≤2` for `ε≤τ`. Each `σ`-ground vector `Ψ` at `ε′` gives the affine majorant `s↦⟨Ψ,(H_M+sH_4)Ψ⟩` of `f`, touching at `ε′`; differentiability forces `⟨Ψ,H_4Ψ⟩=f′(ε′)`. `T_{y,c}` maps even lines at `y` to odd ones and back, so `|⟨T_{y,c}⟩|≤2‖O_yΨ‖‖(1−O_y)Ψ‖≤2‖O_yΨ‖`. Summing over 8 flavours and `L` bonds, `|⟨H_4⟩|≤16√(LW_odd)`. Hence `W_odd≥Lε²/(448²τ²)`, and `448²=200704`.

## 3. Rulings on the distiller's GAPs

**3.1 GAP `w>0` (line 105): real as an omission, closed here. GAP A4 (line 125): real.** Theorem 5 gives no gap when `w=0` (N38), and no proof of `W_odd≤Kw` exists. But the hypothesis `W_odd≤Kw` already forces `w>0` on ground vectors once `|ε|<2τ`:

*Referee closure R-w.* Let `|ε|<2τ`, any `t`, and `Ψ` a normalized `σ`-ground vector, `σ≠1`. If `W_odd=0`, then `w>0`. Proof. At `ε=0`, Theorem 2's minimizers have exactly one `σ` site, so `w=1`. Let `ε≠0`. `H_M` and `H_L` preserve mirror configurations; each `T_{x,a}` reverses mirror parity at `x` and `x+1`. If `W_odd=0`, `Ψ` lies in all-even configurations and `H_4Ψ` lies in configurations with two odd sites. Projecting `H_εΨ=E_σΨ` onto those gives `H_4Ψ=0`, so `(H_M+H_L)Ψ=E_σΨ`. If also `w=0`, every configuration in `Ψ` has charge `σ` and no `σ` line, hence at least two nontrivial even lines, so `E_σ≥E_L+32τ`. The neutral trial vector (all lines trivial, light ground state in the best holonomy) has `⟨H_4⟩=0`, so `E_1≤E_L`. Corollary 3.1 gives `E_σ≤E_1+16τ+8|ε|<E_L+32τ`. Contradiction. `□`

So under `W_odd≤Kw`, `w=0` would force `W_odd=0` and contradict R-w. The draft's sufficiency claim (`SGAP_DRAFT.md` line 201) is therefore true as stated once `c₀<2`, which costs nothing: S-GAP for some `c₀` follows from S-GAP for a smaller `c₀`. The repaired statement is: *Suppose `K≥0`, `0<c₀<2`, `4√2c₀√K<16`, and for every allowed `L`, `τ>0`, `|t|,|ε|≤c₀τ` and `σ≠1` some normalized `σ`-ground vector has `W_odd≤Kw`. Then S-GAP holds with `Δ=16−4√2c₀√K`.* Proof: R-w gives `w>0`; Theorem 5, an inequality for each `σ`-ground vector separately, gives `E_σ−E_1≥16τ−4√2|ε|√K≥Δτ`; item 21's equivalence (with N21's fix) gives S-GAP. `K` must not depend on `ε` or `L`. The missing step of A4 is therefore `W_odd≤Kw` alone. Line 5's "positive weight on a specified charged line … neither is proved" should change accordingly (required edit E6).

*Referee closure (conditional, rigorous).* If `w≤w_max` at the parameters `ε′_L` of Proposition 5.1, with `w_max` independent of `L`, then no `L`-uniform `K` exists: Proposition 5.1 gives `W_odd/w≥Lε²/(200704 w_max τ²)`, which is unbounded in `L`.

*Referee remark (heuristic; not a proof and not a [check]).* If instead `w` grows with `L`, the growth comes from `σ` lines created in neutral pairs far from the charged line. For such a line at `y`, `D_yΨ` is a neutral vector with two separated nontrivial even lines, of energy about `E_1+32τ`. The variational step `⟨D_yΨ,H_εD_yΨ⟩≥E_1‖D_yΨ‖²` then discards about `32τ` per such line, more than the `16τ` it must protect. So the summed form of A4 is not expected to work at large `L` in either case. A repair must restrict the sum over `y` to the charged line's neighbourhood, which needs the localization estimate line 125 names.

**3.2 GAP A5 (line 127): real, and the needed step is false.** Referee closure: for every window `Λ` containing `x₀` and its two incident bonds, every `t`, `ε`, and every window space preserved by `Y`, line 127's identity `Y(K+B)Y=K` holds (it uses `YH_outY=H_out`, `YKY=K+B` and `YBY=−B`). So `K+B` and `K` are unitarily equivalent on the window, and `λ_min(K+B)=λ_min(K)` exactly. No argument of the form "`B` raises the lowest window energy" can succeed. A5 is refuted as an attack; S-GAP is not refuted.

**3.3 GAP A6 (line 129): real.** Proposition 4.1 refutes the per-sector half-filled form at `t=ε=0`, a point inside S-GAP's quantifiers. Proposition 4.3 gives a valid sufficient pair. Two referee additions follow.

*(a) A weaker first hypothesis suffices.* Let `e_p=min spec(H_ε|K_p)`. Put **(G1′)**: there are `c₀,Δ_G>0` such that for every allowed `L`, `τ>0`, `|ε|≤c₀τ` at `t=0` and every `p`, every `S`-charged vector of `K_p`, of any `N`, has energy at least `e_p+Δ_Gτ`. Then (G1′) and (HF′) give `E_σ≥min_pe_p+Δ_Gτ=E_*+Δ_Gτ≥E_0+(Δ_G−δ)τ` in one line, because `H_ε` is block diagonal in `p`. (G1) implies (G1′) by N33. Four-test check of (G1′) as a named hypothesis: (1) it fixes no part's target: it is a per-sector statement with unrestricted `N`, and S-GAP⁰ follows from it only together with a comparison across sectors such as (HF′); (2) its quantifiers are closed; (3) it is a hypothesis of a conditional and settles no downstream question; (4) it adds no structure or constant beyond (G1)'s `c₀, Δ_G`. Passes. Adopted: nothing.

*(b) Under (G1), (HF′) reduces to a comparison with the alternating sector.* Let `p_alt` be alternating. `N` and `U_g` commute with `H_{p_alt}(s)`; under (G1), the simple ground projector `Π(s)` is continuous for `|s|≤|ε|` (N33), so `tr(NΠ(s))` and `tr(U_gΠ(s))` are continuous and take values in a discrete set. At `s=0` they equal `k(p_alt)=L/2` and `1`. So the ground vector of `H_{p_alt}` is neutral and half filled, and `E_0≤e_{p_alt}`. Hence (HF′) follows from **(HF-alt)**: `e_{p_alt}−min_pe_p≤δτ`. (HF-alt) is the "classical comparison" of line 129. Proposition 4.2 suggests it holds with `δ=0` at second order; no bound on higher orders exists here. Four-test check: (1) no target fixed (it is a sufficient condition, not S-GAP⁰); (2) closed; (3) settles nothing by premise; (4) no new constant beyond `δ`. Passes. Adopted: nothing.

*(c) Status of (G1′).* At fixed `p`, `H_p` is an ordinary tensor-product chain of 16-level sites with a unique on-site ground vector, on-site gap `14τ`, and nearest-neighbour terms of norm at most `8|ε|` per bond (N26). Published stability theorems for weakly perturbed non-interacting gapped chains treat this setting (from memory, context only, never load-bearing: Kennedy-Tasaki 1992; Yarotsky 2005 and 2006, the latter fetched by pass 1 as L3; Bravyi-Hastings-Michalakis 2010 and Michalakis-Pytel 2013, arXiv:1109.1588 as pass 1 fetched it, for periodic boundary conditions; Fröhlich-Pizzo 2020 for open chains). None is rebuilt here, so (G1) and (G1′) remain unproved hypotheses in this repository. (HF-alt) is not covered by those theorems: it compares ground energies of different chains to `O(τ)` accuracy while each energy is extensive.

**3.4 Labels on (G1) and (HF′) (line 5).** Correct: both are unproved hypotheses. Line 5's three GAP summaries match the bodies at lines 125, 127, 129.

## 4. Source check

Each cited source was read at `e6c5cab1f`; all six SHA-256 values on line 7 of `SGAP.md` match the files read (`prior/SGAP.md`, `SMG15.md`, `SMG1.md`, `CH1.md`, `LW1.md`, `TOE_ASSEMBLY.md`), and so does the `SGAP_DRAFT.md` value.

**4.1 `SMG15.md` §1-§2 (lines 11-44).**

- Definition 1 (SGAP line 13) matches `SMG15.md` line 15: "Take `L ∈ 4N`, `L ≥ 8`, sites `Z_L`, five CAR modes `c_{x,j}=(γ_{x,2j−1}+iγ_{x,2j})/2` and eight mirror Majoranas `γ_{x,a}`, `a≤8`. Write `c_x=c_{x,5}`". So a site carries five CAR modes: four mirror modes and the light mode. `G_x`, `H_G`, `H_{1/2}`, `hop_x` and `hop⁰_x` match lines 15 and 20. Zero electric coupling matches line 17: "All models below set the electric coupling `τ_E=0`; this is a restriction, not a derivation from the working set." SGAP should keep that last clause (required edit E5).
- Definition 2 (SGAP line 14) matches line 16: "`W=−Σ_{g∈S, deg(g)=4}g`. Its unique `S`-fixed even ground vector is `ψ`, with eigenvalue `−14`; the eight odd character lines have eigenvalue `0`, and the seven other even lines have eigenvalue `2`." `P^χ_x` and `ρ_a` are defined at line 20 (`SMG15.md` §1, item 5), not in §2; §2's Theorem 1 proves their properties. A citation slip only.
- Line 20 (proposed readings) matches line 24: "After SMG1-GAP the referee marks `C, P, P, C`", and line 26: "After SMG1-GAP, R-COR fails test 3 as a reading of 'gapped'".
- Theorem 4's use of the Gauss reduction matches `SMG15.md` Theorem 2 (line 34ff.): "A matter operator preserving all site parities maps to itself tensored with `1`." The same theorem gives the wrap-bond `σˣ` for the light hop, which is the holonomy that Theorem 2 of SGAP minimizes over.
- `SMG15.md` Theorem 1 (line 30) gives the facts SGAP uses without restating: each `P^χ` has rank one, `γ_{x,a}P_x^χ=P_x^{χρ_a}γ_{x,a}`, the configuration projectors commute with light and link operators, and a genuine degree-four monomial `γ_{x,a}γ_{y,a}…` is off-diagonal in configurations.

**4.2 `SMG15.md` §3, §7, §8 and `SMG1.md` §2.**

- Definition 2's `m(χ)=χ(g₁g₂)` is mirror parity. `SMG1.md` line 49 (Lemma 2.1) reads: "`g₁g₂=c₁⋯c₈=P^(4)` and `g c_a g⁻¹=(−1)^{u_a}c_a` for the support `u` of `g`." Line 53 (Theorem 2.2) reads: "`W` has spectrum `−14` once, `0` eight times in odd parity, and `2` seven times in even parity. Its unique ground vector `ψ` is `S`-fixed and even; the eight vectors `c_aψ` form an orthonormal basis of the odd sector." This supports Definition 2 in full.
- Theorem 2 (item 15) cites "`SMG15.md`, Theorems 1–3" for the light reduction. `SMG15.md` Theorem 3 (line 60) covers SGAP's `ε=0` model as the case `t(χ,χ′)≡t`, `μ≡0`, `δ=0`, and gives "`E₀=−2|t₀|/sin(π/L)`, attained uniquely in `w=−1`". Its data line 52 requires "`t₀=t(1,1)≠0`". So the citation covers `t≠0` only. The case `t=0` is immediate (`H_ε=H_M`, `E_1=0`, `E_σ=16τ`), so Theorem 2 stands; one clause is needed (required edit E4). The step from `14τ` per nontrivial site (Theorem 3's bound with `δ=0`) to `16τ` for one even site is SGAP's own and is correct.
- Proposition 4.2 (item 31) is `SMG15.md` Theorem 7, case I, line 136: "`PH_4P=0`, and `PH_4Q(QH_MQ)⁻¹QH_4P=(2/(7τ))Σ_xΛ_x² P`", with "`Λ_x²=n_x+n_{x+1}−2n_xn_{x+1}`". The restriction to `K_p` is direct. Line 142's limit, "higher orders not bounded here … It does not yield volume-uniform decoupling", is kept on SGAP line 76.
- Definition 4 (S-GAP) matches `SMG15.md` lines 148-152 word for word in content: "Do there exist `c₀,Δ>0` such that, for every `τ>0`, `|t|,|ε|≤c₀τ` and every allowed `L`, the `S`-charged spectrum of `H_ε=…` lies at least `Δτ` above its ground energy on `H_{1/2}`? This includes `t=0`. A unique ground state is a separate question." The Hamiltonian on line 150 equals Definition 3's `H_ε`.
- Line 131 (prior failed routes) matches `SMG15.md` lines 156-158: route 1, "bounding the total remainder by the sum of local norms gives a bound growing with `L`"; route 2, "a potential long-distance `|z|⁻²` contribution … diverges logarithmically … The draft does not … exclude cancellations"; route 3, "With the fifth mode unsplit, the reference on-site kernel is two-dimensional. Splitting it with `τ₅n_x` gives an empty, rather than half-filled, reference chain." Line 158 adds one point SGAP omits: the global-gap conclusion "cannot be applied unchanged to the one-site-invariant half-filled family in the presence of Theorem 5". This does not affect A6: each `H_p` has a fixed `p`, and Corollary 4.4 already shows the half-filled ground space is degenerate at `t=0`.
- Line 133 (other open items) matches `SMG15.md` lines 7, 160 and 162 by name: S-GAP, R1.5-U, R1.5-D, P3, R15-GNS, the tick/generator state comparison, Q-R15, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D, W2/R4. `SMG15.md` line 162 confirms the owner's choice: "`TOE_ASSEMBLY.md` §3.10: SMG1-GAP adopts bounded R-GEN for SMG1's rungs".
- Line 133's claim "Corollary 4.4 rules out R15-SPEC's finite-ring uniqueness S3 at `t=0` for this zero-electric-coupling model" is correct against `SMG15.md` line 24: "(S3) the ground vector in `H_{1/2}` is unique for all sufficiently large `L`". At `t=0` every level of `H_{1/2}` has even multiplicity. The scope is S-GAP's own model at `t=0`, `τ_E=0`; S3 is a clause of a proposed reading, not an adopted one.

**4.3 `SGAP_DRAFT.md` (pass 1), head, outcome and literature.**

- Provenance (SGAP line 7) matches the draft head: "Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini", lead line `anthropic/claude-opus-5-5/max`. The draft read `SMG15.md` at `373e01725`; SGAP checked the same file by hash. The hashes agree with the files at `e6c5cab1f` (section 4 head).
- The draft's outcome paragraph (draft line 38) names exactly the results SGAP keeps: Lemma E and Proposition Z (SGAP Theorems 1, 2), Theorem A and Corollary A1 (Theorem 3, Corollary 3.1), Theorem C, Corollary C1, Propositions C2, C3, C5, Remark C6 (Theorem 4, Propositions 4.1-4.3, Corollary 4.4), Lemma R and Proposition R2 (Theorem 5, Proposition 5.1). The distillation drops no proved result. It renames Remark C6 as Corollary 4.4; the content is a corollary, so the change is right.
- The literature sentence. Draft line 79 reads: "A search for a rigorous ground-energy bound for a mobile impurity in a Luttinger liquid found none. … So no fetched work states a uniform energy gap for a gapped excitation coupled to a gapless one-dimensional chain." Section 5 rules on it.

**4.4 `SGAP_DRAFT.md` §4.4, §5 and FINISH against SGAP §5-§6.**

- Lemma R. The draft (§4.4) has the same unranged `Σ_c`, and its proof says "As `c` runs over `1,…,8`". So all eight flavours are meant in both texts (N36). The draft's step "`P^σ_yH_ε(1−P^σ_y)=εP^σ_yH_4^{(y)}`" is the commutator step of N36, written out; SGAP line 103 compresses it to "the eigenvalue equation yields the displayed identity". Correct, but the draft's line should be kept (required edit E2).
- The `w>0` sentence. The draft (after Lemma R) reads: "So `E_σ−E_1≥16τ−4√2|ε|√(W_odd/w)` whenever `w>0`. … It proves S-GAP for any family of charged ground vectors with `W_odd≤Kw`, `K` independent of `L`, once `4√2c₀√K<16`." SGAP's GAP note says "the draft omits the `w>0` requirement in its unqualified sufficiency claim". That is accurate about the text. Referee closure R-w (section 3.1) shows that the claim is nevertheless true: `W_odd≤Kw` forces `w>0` for `|ε|<2τ`, and S-GAP needs only some `c₀`.
- Proposition R2. The draft's proof says "Every bond between blocks, and every bond at sites `0` and `1`, changes the line at one site of each of two different factors". So the draft treats sites 0 and 1 as two single-site factors, and the bond `(0,1)` is covered. SGAP line 117 drops "and every bond at sites `0` and `1`"; under the same reading its sentence still covers that bond. The clause should be restored for clarity (required edit E3; N40). The draft's "one-sided derivatives of a lowest eigenvalue are the extreme values of `⟨H_4⟩` on the ground space" is a correct alternative to N41's majorant argument.
- A4, A5, A6 match the draft's attacks in plan and failing step. The draft adds one `[check]` to A6, "`‖[H,P_x]‖=0.6` at `t=0.3`, against `0` at `t=0`". SGAP drops it; this is harmless, since Theorem 4 proves `[H_ε,P_x]=0` at `t=0` and `hop_x` visibly changes `P_x` at `t≠0`.
- Four tests. The draft's FINISH reads: "S-GAP⁰ as a named sub-lemma passes the four tests: (1) it fixes no part's target, being a case of an existing open statement; (2) its quantifiers are closed; (3) it settles no downstream question by premise; (4) it adds no structure or constant." SGAP line 20 reports this faithfully. The referee agrees: S-GAP⁰ is `SMG15.md` line 148's statement with `t=0`, which line 152 already includes.
- Downstream. The draft's FINISH says "on `H_{1/2}`, S-GAP's best constant at `ε=0` is `16`, not `14`", and "at `t=0` (with `τ_E=0`) every level of `H_ε` on `H_{1/2}` has even multiplicity (Remark C6), so uniqueness needs `t≠0` or `τ_E>0`". SGAP keeps both (Theorem 2; line 133). The draft's remark on SMG1's later rungs ("This is a remark, not a theorem about those rungs") is not carried into SGAP; it carries no claim, so nothing is lost.

**4.5 The digest's reports from `origin/main` (SGAP lines 131, 135).** SGAP repeats these only as digest reports. The quotes were checked at `origin/main` `f5af11cd0` (after `git fetch -q origin main`; read with `git show` only). Spin(10) note (`docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md`, last changed `4d0cd77bd`): line 235 "the bound retains v's volume dependence", line 239 "This is not a volume-uniform expansion", line 256 "At this order the induced term is a constant", line 272 "function therefore cannot follow by applying Wick's rule", line 293 "a nonzero attractive density interaction", line 297 "not imported unchanged into the refined Spin(10) atom". Ring comparator (`docs/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_…_2026-09-24.md`, last changed `ef918c191`): line 90 "one spinless band whose wrap bond carries `R`", line 112 "the lowest state over all `N` is half filled", line 23 "unaudited". KMS note (`docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`, last changed `e92061999`): line 14 "This row proves only scalar ODE consequences", line 89 "Any future framework use must separately supply the BBF/Polchinski inequality". All match `prior/SGAP.md`. None enters a proof in SGAP. The ring comparator's line 112 is the free-band analogue of (HF′); it does not transfer to the interacting `t=0` chains.

## 5. Attacks A4, A5, A6 against the three on file

The three attacks on file are in `SMG15.md` lines 156-158 and `SMG15_REFEREE.md` §2.9 (lines 241-249). Their failing steps, quoted from the referee: (1) local Schrieffer-Wolff, "a norm bound by the sum of local norms grows with `L`, and Weyl's inequality then gives no `L`-uniform sector gap"; (2) absolute polymer expansion, "Such correlations have nonzero `|z|⁻²` tails … The absolute sum … diverges logarithmically"; (3) Fröhlich-Pizzo, "(1.4) needs a one-dimensional on-site kernel. At `τ₅=τ_E=0` the on-site kernel, with its link, is `ψ⊗{|0⟩,|1⟩}⊗{|+⟩,|−⟩}`, four-dimensional."

| Attack | New step | Failing step | Kind of failure | Same as a route on file? |
|---|---|---|---|---|
| A4, charge removal | exact identity of Theorem 5 (`D_y=Y_yP^σ_y`), variational bound in the neutral block | `W_odd≤Kw`, `K` independent of `L` and `ε` | unproved; R-w removes the separate `w>0` condition; section 3.1 gives a conditional obstruction and a heuristic one | No. No expansion, no remainder, no stability theorem. |
| A5, shifted window | Theorem 3 localized to a window with an Anderson bound | `λ(K+B)>λ(K)` | false: `Y(K+B)Y=K` exactly (section 3.2) | No. |
| A6, parity sectors | Theorem 4: `2^{L−1}` chains with one-dimensional on-site kernels | comparison across sectors; the per-sector half-filled form is false (Proposition 4.1), (HF′) open | per-sector target false; sufficient pair unproved | No. It removes route 3's obstacle at `t=0` (Theorem 4 puts the link into the global `C²` and fixes `n_x` by `p_x` and the line), and fails at a different step. Route 2's obstacle is absent at `t=0` (no light hopping). It never uses a norm-Weyl bound, so route 1's step does not arise. |

**Ruling.** A4, A5 and A6 are distinct from each other and from the three on file. A4 and A5 share Theorem 3 but fail at different steps of different kinds. Each failing step is named. S-GAP⁰ therefore meets the stopping rule (a lemma on which three distinct attacks failed), as pass 1 and pass 2 say. The ruling is about attacks only; it does not say that S-GAP⁰ is hard or that other routes are excluded. Section 3.3 names the route A6 points to; it is not attempted here.

**Owner frame.** `TOE_ASSEMBLY.md` §3.10 (line 257, "Owner decisions on the chirality wall, SMG1 (2026-11-07)") records at line 261 "**SMG1-GAP = R-GEN, bounded (owner 2026-11-07).**", with "A ground state satisfies \(\omega(A^*[H_U,A])\ge0\) for every local \(A\)" and "Tick stationarity remains a separate requirement."  SGAP's statements are finite-ring spectral statements about one operator `H_ε` (Definition 4: "These are finite-ring questions, not GNS or tick statements"). They neither use nor contradict SMG1-GAP. Their bearing on SMG1-GAP passes through R15-SPEC (S1), a proposed reading, and R15-GNS, open. SGAP says both (line 20, line 133). Judged against SMG1-GAP, SGAP claims nothing it does not prove.

## 6. The literature claim

`SGAP_DRAFT.md` line 79 reads: "A search for a rigorous ground-energy bound for a mobile impurity in a Luttinger liquid found none. … A search for Mastropietro's work on an impurity in a Luttinger liquid found no rigorous paper on that problem. So no fetched work states a uniform energy gap for a gapped excitation coupled to a gapless one-dimensional chain." `SGAP.md` line 135 reads: "its cited abstracts were not independently re-fetched here. In particular no claim of an exhaustive literature absence follows from its search."

**Ruling.**

1. Pass 1 makes two claims: a search report ("found none") and a statement about the works it fetched. Both are worded within what a search shows. Neither is the claim "no rigorous mobile-impurity bound in a Luttinger liquid is known".
2. That absence claim is not established. A search cannot establish it. It must not be written in SGAP or downstream. SGAP line 135 says so, correctly.
3. No proof step in SGAP or in the draft depends on it. It is context for S-GAP at `t≠0` only. At `t=0` there is no light hopping and no Luttinger liquid: the light occupations are frozen classical data `p`, and S-GAP⁰ is a stability-and-comparison problem for gapped 16-level chains (Theorem 4).
4. Context from memory, not verified and never load-bearing: McGuire (J. Math. Phys. 6, 432 (1965); 7, 123 (1966)) solved by Bethe ansatz one distinguishable particle with a contact interaction in a one-dimensional free Fermi gas. A free Fermi gas is the non-interacting case of a Luttinger liquid. So the unqualified absence claim would already be doubtful in that special case. For an interacting Luttinger liquid this referee knows of no rigorous mobile-impurity energy bound; that is not evidence of absence. This referee ran no literature search.

## 7. Required edits to `SGAP.md`

No edit changes the content of a theorem. E1 corrects a false line. E2-E7 are clarity or citation edits. E8 is optional.

- **E1 (item 21, line 52).** Replace "such a bound forces `E_0=E_1`; the converse follows from `E_1≥E_0`" by: "such a bound gives S-GAP because `E_1≥E_0`; conversely, S-GAP makes every charged `E_σ` exceed `E_0`, so the minimum `E_0` is attained at `χ=1` and `E_1=E_0`."
- **E2 (items 36-37, lines 95, 103).** Write `H_4^{(y)}=Σ_{c=1}^{8}(T_{y−1,c}+T_{y,c})`, all eight flavours, to separate it from Theorem 3's `Σ_{c∈{a,b}}`. Restore the draft's step "`P^σ_yH_ε(1−P^σ_y)=εP^σ_yH_4^{(y)}`" in the proof.
- **E3 (item 40, lines 113, 117).** Say that sites 0 and 1 are two single-site factors, and restore the draft's "and every bond at sites `0` and `1`".
- **E4 (item 15, line 32).** Add: "`SMG15.md` Theorem 3 assumes `t₀≠0`; at `t=0`, `H_ε=H_M` on this slice, so `E_1=0` and `E_σ=16τ` directly."
- **E5 (item 4, line 13).** After "The electric coupling is zero", add `SMG15.md` line 17's clause: "this is a restriction, not a derivation from the working set".
- **E6 (items 2, 38, 43; lines 5, 105, 125).** Add referee closure R-w (section 3.1). Line 5: "A4 requires a bound `W_odd≤Kw` uniform in `L` and `ε`; by R-w it implies `w>0` when `|ε|<2τ`; the bound is not proved." Line 105: "the draft's sufficiency claim omits the `w>0` step; referee closure R-w supplies it for `|ε|<2τ`." Line 125: "The missing step is `W_odd≤Kw`."
- **E7 (item 5, line 14).** Cite "`SMG15.md` §1 item 5 and §2" for `P_x^χ` and `ρ_a`.
- **E8 (optional).** Add, labelled as referee closures and remarks: the conditional A4 obstruction and the heuristic remark (section 3.1); (G1′) and the reduction of (HF′) to (HF-alt) under (G1) (section 3.3).

## 8. Open statements to carry by name

- **S-GAP⁰ (OPEN).** Definition 4 with `t=0`. It is the stopping lemma. Three distinct attacks failed at named steps: A4 at `W_odd≤Kw`; A5 at `λ(K+B)>λ(K)`, which is false; A6 at the comparison across sectors (section 5).
- **S-GAP at `t≠0` (OPEN).** Routes 1-3 on file and A4, A5 fail; A6 does not apply, because `hop_x` changes `P_x`.
- **(G1′) (unproved hypothesis, not adopted).** Section 3.3(a). (G1) implies it. It lies in the setting of published stability theorems for weakly perturbed non-interacting gapped chains; none is rebuilt in this repository.
- **(HF-alt) (unproved hypothesis, not adopted).** Section 3.3(b): `e_{p_alt}−min_pe_p≤δτ`. Under (G1) it implies (HF′). With (G1′) and `δ<Δ_G` it gives S-GAP⁰. It is the step A6 is missing.
- **Downstream, unchanged.** R1.5-U, R1.5-D, R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D and W2/R4, as `SMG15.md` lines 7, 160 and 162 state them.

## 9. Freeze recommendation

**Freeze `SGAP.md` after edits E1-E7.** E8 is optional. No further referee pass is needed: no edit changes a theorem's content, and every proof was re-derived here.

Status at freeze: S-GAP and S-GAP⁰ OPEN. Proved, conditional on the frozen atom of `SMG1.md` and the Gauss reduction of `SMG15.md` (as line 3 says): Theorems 1-5, Corollaries 3.1 and 4.4, Propositions 4.1-4.3 and 5.1. On the points the brief names:

- the exact `ε=0` charged gap `16τ`, for every real `t`: CORRECT (items 14-15; citation clause E4);
- the charge-shift identity (Theorem 3) and the reduction of S-GAP to the energy cost of one local operator (Corollary 3.1, line 52): CORRECT; one ERROR in the reasons on line 52 (E1);
- Lemma R (Theorem 5): CORRECT, with the flavour range written out (E2); Proposition R2 (5.1): CORRECT;
- the `t=0` decomposition into `2^{L−1}` chains of 16-level sites with on-site gap `14τ` (Theorem 4): CORRECT;
- Proposition C2 (4.1), the per-sector form is false at `ε=0`: CORRECT; Proposition C5 (4.3), the sufficient pair: CORRECT, and (G1′) may replace (G1); Remark C6 (Corollary 4.4), even multiplicity at `t=0`: CORRECT;
- A4, A5, A6: real failed attacks, distinct from each other and from the three on file (section 5);
- the literature claim: pass 1 reports a search, correctly worded; the absence claim "no rigorous mobile-impurity bound in a Luttinger liquid is known" is not established and must not be written (section 6).

## 10. Prior work used

| Prior result | Path | Use here |
|---|---|---|
| Prior-work digest for SGAP | `.claude/science/physics-loops/toe-assembly-20261104/prior/SGAP.md` (all) | Routes on file; main-branch reports, re-checked in section 4.5 |
| Lemma 2.1 (`g₁g₂=c₁⋯c₈=P^(4)`) and Theorem 2.2 (the atom: `−14`, `0` ×8 odd, `2` ×7 even) | `SMG1.md` lines 49, 53 | Items 5, 13, 18, N18 |
| Theorem 1 (rank-one character lines, shift rule) and Theorem 2 (Gauss reduction `J`, wrap-bond `σˣ`) | `SMG15.md` lines 30, 34-44 | Items 5, 12, 15, 25-26, N26 |
| Theorem 3 (finite-ring spectrum of the configuration-conserving family, `t₀≠0`) | `SMG15.md` lines 46-66 | Item 15, edit E4 |
| Theorem 7 (atomic resolvent `2/(7τ)`) | `SMG15.md` lines 130-142 | Items 30-31 |
| S-GAP statement and the three routes on file | `SMG15.md` lines 148-158; `SMG15_REFEREE.md` §2.9, lines 241-249 | Item 7; section 5 |
| R15-SPEC (S1-S3), R-COR, owner frame | `SMG15.md` lines 24, 26, 162; `TOE_ASSEMBLY.md` §3.10, lines 257-266 | Items 10, 47; section 5 |
| Pass-1 draft | `SGAP_DRAFT.md` (lines 1-38, 59-79, 189-251) | Sections 4.3-4.4 |

**Extended here.** Theorem 5 by referee closure R-w (section 3.1). Proposition 4.3 by (G1′) and the reduction of (HF′) to (HF-alt) under (G1) (section 3.3).

**Prior work the digest missed.** None found in the files read. The digest names further files that `SGAP.md` does not cite and no verdict here needs: the consolidated chirality note (`ref/pr10131/…`), the retained-Grassmann polymer note and the PR #10135 gauge-gap note. They were not read.

---

## FINISH

**Proved (this report, by hand; no computer-assisted step; no [check] was run).**
- All 48 items of `SGAP.md` were re-derived: 47 CORRECT, 1 ERROR (item 21, the reasons on line 52; the equivalence itself is true), 0 INCOMPLETE.
- Referee closure R-w: for `|ε|<2τ` and every `t`, a `σ`-ground vector with `W_odd=0` has `w>0`. Hence the A4 hypothesis `W_odd≤Kw` alone gives S-GAP (with `c₀<2`, `4√2c₀√K<16`), and the draft's sufficiency claim is true.
- Conditional obstruction to A4: if `w` stays bounded at the parameters `ε′_L` of Proposition 5.1, no `L`-uniform `K` exists.
- (G1′) and (HF′) give `E_σ≥E_0+(Δ_G−δ)τ`. (G1) implies (G1′). Under (G1), (HF-alt) implies (HF′).
- A5's identity: `K+B` and `K` are unitarily equivalent on every `Y`-invariant window space, for every `t`, `ε`.

**Counterexamples.** None new. Confirmed: Proposition 4.1 (the per-sector half-filled form is false at `t=ε=0`) and A5's identity `λ(K+B)=λ(K)`. No counterexample to S-GAP or S-GAP⁰ is known.

**Open by name.** S-GAP⁰, the stopping lemma: three distinct attacks failed, A4 (charge removal, at `W_odd≤Kw`), A5 (shifted window, at `λ(K+B)>λ(K)`, false), A6 (parity sectors, at the comparison across sectors). S-GAP at `t≠0`. The hypotheses (G1′) and (HF-alt), not adopted.

**What changes downstream.**
- `SGAP.md` can freeze after E1-E7. Its proved results stand as stated.
- A `t=0` lane should target (HF-alt), with (G1′) from a rebuilt stability argument. A4 needs a form localized at the charged line; its summed form is not expected to work at large `L` (heuristic, section 3.1).
- The absence claim "no rigorous mobile-impurity bound in a Luttinger liquid is known" must not be cited anywhere.
- No axiom, law, frozen part, reading or working-set entry changes. Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
