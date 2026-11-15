lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SMG1 referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 (the referee) of part SMG1 under PR #10138's method. Claude drafted the part (`SMG1_OUTLINE.md`). Codex gpt-6.1-terra distilled it (`SMG1.md`). This session wrote neither. This is one check: one line-by-line read of `SMG1.md`, with its pass-1 sources checked where it cites them. No review of other reviews was made.

**What this file is.** A referee report. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. Only the owner adopts. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A `[check]` is a tiny scratch computation in `/tmp/toe-SMG1ref/`; it guides or refutes and never proves.

**Text refereed.** `SMG1.md` as of commit `a7fa25536` (the last commit that touches it, equal to branch head `claude/toe-assembly` when read). SHA-256 of the file read: `03b17522f1a5699baa4244589273027fdadf2dfd07b4df2157860bb1da1e44cc`. Line numbers below refer to that file, written `L<n>`.

**Pass-1 source checked.** `SMG1_OUTLINE.md` as of commit `494ffe935`, SHA-256 `e1e206f739b10a560f2b1289a415ea60405323f03e117796148fdc2fe7212b85`, all 417 lines. Outline line numbers are written `O<n>`.

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step, written here so the owner can see it; it is a proposal, not an edit of `SMG1.md`.

**Sources read, with commits.**

| Ref | Commit | Read with |
|---|---|---|
| `claude/toe-assembly` (this checkout) | `a7fa25536` | working tree |
| `origin/docs/consolidate-chirality-doublers` (PR #10131) | `a1bced899` | `git show` |
| `origin/claude/toe-cayley-mirror-gap-20261021` (#10078) | `d2b189516` | `git show` |

Files read, by line. This folder: `SMG1.md` (all); `SMG1_OUTLINE.md` (all); `prior/SMG1.md` (all); `LW1_REFEREE.md` lines 1-80, its headings and section 4 (format); `Y2W_DRAFT.md` lines 1-30 (format); `TOE_ASSEMBLY.md` lines 171-177, 180, 183, 184, 205, 235, 718; `VC1_5.md` lines 20, 36, 48, 50 and its headings; `GA2_Y2.md` lines 37-43; `RCS1.md` lines 8, 16, 66, 68; `CH1.md` lines 24, 62, 72, 122, 126 (grep hits); `CG16S.md` lines 5, 9, 11, 116, 120, 138 (grep hits); `LIT_SMG.md` lines 200-202; `CH1_5UQ.md` lines 1-12, 26 and grep hits for "gap". PR #10131 consolidation note: line 2341. #10078 note (`docs/THE_CAYLEY_COMPLETION_OF_THE_CHARGE_FOUR_TERM_HALVES_THE_GAPPING_COUPLING_OF_THE_EIGHT_MAJORANA_PROXY_CHAIN_BUT_BOTH_FORMS_PERSIST_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-24.md`): grep hits at lines 4, 34, 37. Literature, downloaded on 2026-11-07 into `/tmp/toe-SMG1ref/dl_fk/` and `/tmp/toe-SMG1ref/dl_fp/` and read as extracted text: arXiv:0904.2197v3 (Fidkowski–Kitaev), Section II, Eqs. (8)-(11), (18); arXiv:1812.02457v2 (Fröhlich–Pizzo), Sections 1.1-1.2 and Theorem 3.5.

**[check] runs.** `check.py` in `/tmp/toe-SMG1ref/`, output `out.txt`; numpy and scipy, under one second, 0.27 GB peak; started at 58 percent free memory. It confirms the fourteen signs of `W`, the atom spectrum and parities, the one-dimensional `S`-fixed space, eight zero modes for a random admissible form on `Z_5`, the gaplessness of the alternating-sign chain against a gapped dimerised one, `‖b_ℓ‖ = 4`, and the non-stationarity of `Ψ` under the conjugated tick. A check guides and never proves.

**Working-set entries used.** NN-a (GA1-P-NN, `TOE_ASSEMBLY.md` line 235): items 7 and 16, and hypothesis (H1) of Lemma F. PS-1c (line 180): the cell translations of (H2). PS-5 (line 205) and PS-6r (line 183): only through the carrier of `SMG1.md`. The four smuggle tests (lines 173-176). No other entry is used. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The working set and the two live laws are read plainly. Where a meaning is open, this report proposes a specification (W2.4′) and four-tests it; nothing is adopted.

---

## 1. Verdict table

Items follow `SMG1.md` in order. Section 2 below gives the long notes, proofs and referee closures that the table points to.

### 1.1 Status lines and section 1 (definitions, target)

| # | Item (`SMG1.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Status paragraph (L3) | CORRECT | Each listed result is proved below in its section, for the stated model. The Fröhlich–Pizzo hypotheses that L3 calls unchecked are checked in §2.5 here. |
| 2 | GAPs paragraph (L5) | CORRECT | A faithful summary. Each GAP is judged at its own row: items 13, 22, 34 with 51, 39, 45. |
| 3 | Open list (L7) | CORRECT | All eight names appear in §6 of `SMG1.md`. Item 13 adds one name, W2-LIGHT (§4). |
| 4 | Provenance (L9) | CORRECT | It records what pass 2 did not run. No mathematical claim. |
| 5 | Preface to section 1 (L13) | CORRECT | |
| 6 | Definition 1, carrier (L15) | CORRECT | Matches `O115` and `O247`. Even ring length is needed for the two hop layers and for the sign `(−1)^x` of the reflection. |
| 7 | Definition 2, NN-a (L16) | ERROR | The last sentence is not NN-a's text. See §2.1. |
| 8 | Definition 3, R-GEN (L17) | CORRECT | A proposal, not adopted. The sign convention is right: for a finite ground vector `Ψ` with energy `E₀`, `⟨Ψ, A*[H,A]Ψ⟩ = ⟨AΨ,(H−E₀)AΨ⟩ ≥ 0`. |
| 9 | Definition 4, symmetry and vacuum (L18) | CORRECT | Matches `O121-O123`. Purity on `𝔄` with gauge invariance implies purity on `𝔄^K` (`VC1_5.md` Theorem 2.1; item 31). |
| 10 | Definition 5, light fields (L19) | CORRECT | `RCS1.md` line 68, Theorem 4: "Every `A∈𝔄^G` is matter-even." The outline cites line 66; the theorem is at line 68. |
| 11 | Definition 6, scaling map (L20) | INCOMPLETE | The tie convention for `[λx]` is named but not fixed. The map has no channel for quasi-energy `π`; see item 13. |
| 12 | Definition 7, target W2 (L21) | ERROR | It renders W2.4 as "**every** choice of rescaling powers". The outline (`O138`) says "each rescaled by a power of `λ`", and its test 2 (`O387`) says "the rescaling powers are existential per operator". Fix: report the outline's wording and that both readings fail (item 13). |
| 13 | GAP W2.4 (L23) | CORRECT (gap real) | The universal reading is inconsistent, as L23 shows. The existential reading is vacuous (§2.2). The `π` sentence is right, and `O142` "so it is excluded too" is an ERROR (§2.2). A repaired statement W2.4′ is proposed and four-tested in §2.2. It is not adopted. Open by name: W2-LIGHT, the owner's choice of a light-sector criterion. |
| 14 | W2.1 and the free no-go results (L25) | CORRECT | Under `G_SM` the singlet `ν^c` has `ν^cν^c` invariant. CH1 F3a is at `CH1.md` line 62; RC-W is at `CG16S.md` line 120. |

### 1.2 Section 2 (construction and atom) and section 3 (obstruction and minimality)

| # | Item (`SMG1.md` line) | Verdict | Note |
|---|---|---|---|
| 15 | `S`, `W` and the global `S` action (L29-L33) | CORRECT | Each `g ∈ S` is an even site element, so the product of site adjoint actions is well defined and fixes mode 5 and the links. |
| 16 | Chain terms, constants, tick, `H(θ)`, `Δ₀` (L33-L37) | CORRECT | The constants give `‖X_g‖ < π` for every gate: the on-site generator has norm `16τ+τ₅` (attained at `W=2`, `n₅=1`), the link generator `τ_E`, the hop generator `4|θ|`. Under NN-a's "pairwise disjoint edge triples" (`TOE_ASSEMBLY.md` line 235), `L₂` is two NN-a layers (even and odd links); the tick is unchanged. |
| 17 | Lemma 2.1, statement (L39) | CORRECT | |
| 18 | Lemma 2.1, proof (L41) | CORRECT | Rebuilt in §2.3. The outline's list of the sixteen words (`O277`) swaps two labels: `u₁+u₃+u₄ = {1467}` and `u₁+u₂+u₃+u₄ = {1458}`. The set of fourteen words is right. |
| 19 | Theorem 2.2, statement (L43) | CORRECT | |
| 20 | Theorem 2.2, proof (L45) | CORRECT | Rebuilt in §2.3. `[check]` gives `−14` (1, even), `0` (8, odd), `2` (7, even) and a one-dimensional `S`-fixed space. |
| 21 | Precursor paragraph (L47) | CORRECT | The `ref/pr10131/` path is the digest's retrieval folder. In this repository the source is `origin/docs/consolidate-chirality-doublers`, file `docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`, line 2341, which reads "the Cayley form, has stabiliser 21 (Spin(7)) and spectrum -14 (1), 0 (8, odd), +2 (7, even)", status "logged". |
| 22 | GAP FK identification (L49) | CORRECT (gap real in `SMG1.md`); CLOSED here | All fourteen signs are computed by hand in §2.3 and agree term by term with Eq. (8) of arXiv:0904.2197v3 as printed. FK's Eqs. (9)-(10) give `a_j = (ĉ_{2j−1}+iĉ_{2j})/2`, the convention of Definition 1. The identification is credit only; no proof uses it. |
| 23 | Theorem 3.1, statement (L53) | CORRECT | |
| 24 | Theorem 3.1, proof (L55) | CORRECT | "generate `Cl₈(C)`" should read "generate a nonzero quotient of `Cl₈(C)≅M₁₆(C)`, which is `M₁₆(C)` because that algebra is simple"; `O302` gives this. On a ring, `Σ_r A^a_{0r} = 0` because `r ↦ −r` is a bijection of `Z_L` and `A^a_{0,−r} = −A^a_{0r}`. `[check]`: a random admissible form on `Z_5` has exactly 8 zero one-body eigenvalues. |
| 25 | Remark on translation (L57) | CORRECT | True with "dimerized" meaning alternating strengths. The outline's displayed example (`O304`) is gapless: ERROR in the outline, see §2.3. |
| 26 | Theorem 3.2, statement (L59) | CORRECT | |
| 27 | Theorem 3.2, proof (L61) | CORRECT | Distinctness of the `ν` functionals gives `ν ≤ 2^k`; with `k ≤ ν/2` this fixes `k = 1, 2, 3` for `ν = 2, 4, 6`. L61 uses this ("they fill `F₂²`"); the outline states it. |
| 28 | Remark on scope (L63) | CORRECT | |

### 1.3 Section 4 (product tick and Floquet spectrum)

| # | Item (`SMG1.md` line) | Verdict | Note |
|---|---|---|---|
| 29 | Theorem 4.1, statement (L67) | CORRECT | |
| 30 | Theorem 4.1, finite-volume proof (L69) | CORRECT | `Σ_j(1−p_j) ≥ 1−∏_j p_j` holds for commuting projections in their joint eigenbasis. |
| 31 | Theorem 4.1, infinite-volume proof (L71) | ERROR (citation only) | "the gauge-invariant extremality equivalence in `VC1_5.md`, section 1": the equivalence is `VC1_5.md` Theorem 2.1 (line 48, section 2): "For a gauge-invariant state, P is equivalent to extremality among all gauge-invariant states." The mathematics is right. When `e` is odd, `A=|κ⟩⟨e|` is odd; it still commutes with every other term, since all terms are even. |
| 32 | Theorem 4.2, statement (L73) | CORRECT | Infinite chain, GNS of `ω₀`. |
| 33 | Theorem 4.2, proof (L75) | CORRECT | `α(K_x) = e^{16iτ}K_x` with `α = Ad U*`; the vectors are unit, vacuum-orthogonal and in the invariant sector. |
| 34 | GAP general Floquet claim (L77) | CORRECT (gap real); first half CLOSED here | The outline's general sentences (`O332`, `O378` "never available", `O415`) rest on one example. Referee closure, Lemma F (§2.4): for every NN-a tick that commutes with an infinite group of cell translations, and every stationary, cell-invariant, gauge-invariant state that clusters along them, `1` lies in the spectrum of the GNS unitary on `Ω^⊥` in the invariant-algebra sector. The second half, that a generator is the only meaningful notion of gap, is a choice, not a theorem; it is owner question Q1. FLQ stays open. |

### 1.4 Section 5 (weak hopping and finite gauging)

| # | Item (`SMG1.md` line) | Verdict | Note |
|---|---|---|---|
| 35 | Lemma 5.1, statement (L81) | CORRECT | Fröhlich–Pizzo use one on-site matrix `H` at every site ((1.2) of the source). The dummy link at `x=N` makes all `N` factors identical, so this holds; `SMG1.md` should say so (§3, edit E5). |
| 36 | Lemma 5.1, proof (L83) | CORRECT | Each of the eight hop summands is Hermitian with square `1/4`, and they commute, so `‖b_ℓ‖ = 4`. `[check]` gives `4.0`. |
| 37 | Theorem 5.2, statement (L85) | CORRECT (as a conditional) | The hypotheses (1.4), (1.6), (1.7) of the printed Theorem 3.5 hold for Lemma 5.1's chain with `M = 64`, `k̄ = 1` (§2.5). The theorem stays cited, not rebuilt; R1-H stays open. |
| 38 | Theorem 5.2, proof (L87) | CORRECT | The Riesz projection is norm-continuous while the gap stays at least `Δ₀/2`; `tr(P(θ)g)` is continuous with values in `{±1}`, hence constant. |
| 39 | Remark after Theorem 5.2 (L89) | CORRECT | The `≤` of `O168` against the `<` of `O344` is a real inconsistency; the strict form is right. The source's own statement is strict: "for any t ∈ R with \|t\| < t0". No stationarity at `θ ≠ 0` follows: also right. |
| 40 | Proposition 5.3, statement (L91) | CORRECT | With `K = S`, local fermion parity `P_x` is no longer a gauge generator (`S` acts trivially on mode 5). The gates stay even, as NN-a requires. |
| 41 | Proposition 5.3, proof (L93) | CORRECT | Each `M_ρ` is a permutation matrix with `M_ρ² = 1`, so it is a Hermitian unitary; `Ad` of the link character operator multiplies `M_{ρ_a}` by `ρ_a(g)`; the product with `γ_{x,a}` is invariant. |

### 1.5 Section 6 (ladder) and section 7 (readings)

| # | Item (`SMG1.md` line) | Verdict | Note |
|---|---|---|---|
| 42 | Ladder preface (L97) | CORRECT | |
| 43 | R0 (L99) | CORRECT | One site cannot carry sixteen independent complex modes in any case: `dim ΛC⁵ = 32 < 2^16`. `CH1.md` C2-5 (line 126) is the sharper statement. |
| 44 | R1 (L100) | CORRECT | |
| 45 | R1.5-D and its GAP (L101) | CORRECT (gap real, a precision gap); CLOSED here | Referee closure (§2.6): every `S × U(1)₅`-invariant operator is a sum of products `M·L`, with `M` an `S`-invariant mirror operator and `L` a `U(1)₅`-invariant light operator, and genuine mixing starts at degree four. So the outline's "starts at quartic order" is true; its gloss names only the leading terms. No Luttinger limit follows: right. |
| 46 | R2 (L102) | CORRECT | Status words follow the digest. |
| 47 | R3-H and R3-D (L103) | CORRECT | The zeros at `{0,π}²` follow by the proof of Theorem 3.1: the symbol is `−2Σ_{r∈half-plane} f(r) sin(k·r)`. |
| 48 | W2 / R4 (L104) | CORRECT | |
| 49 | Seven tasks (L106) | CORRECT | Matches the outline's tricks A-G (`O220-O228`). |
| 50 | Four-test preface (L110) | CORRECT | `TOE_ASSEMBLY.md` lines 173-176: "1. It states or fixes something that a part lists as its target. 2. It is open-ended, so a part can add to it to get a result. 3. It settles a downstream physics question by premise. 4. It adds a structure or a constant that its own reasons do not need." |
| 51 | R-GEN check (L112) | CORRECT | Two additions (§2.7). Decomposition dependence does hold within the bound `‖X_g‖ < π`, by a conjugation identity. The conjugated-tick example is verified: `Ψ` is not stationary for `0 < \|θ\|` small when `28τ+τ_E ∉ 2πZ`. |
| 52 | R-LIGHT check (L113) | CORRECT | Add: the existential reading of W2.4 is vacuous (§2.2). The repair W2.4′ is in §2.2. |
| 53 | R1-LAW check (L114) | CORRECT | |
| 54 | Closing line (L116) | CORRECT | Both checks it asks for are done here: the fourteen signs (§2.3) and Theorem 5.2's hypotheses (§2.5). |

**Counts.** 54 items: 50 CORRECT, 3 ERROR (items 7, 12, 31), 1 INCOMPLETE (item 11). No ERROR or INCOMPLETE item changes a proved theorem. L5 lists five GAPs, and all five are real. Three are closed here: the FK identification (item 22); the form of the mixing terms (item 45); and the general tick-gap claim, proved under clustering, with a valid example of decomposition dependence (items 34, 51). Two stay open by name: W2-LIGHT (item 13; a repair is proposed) and FLQ (stationarity at `θ ≠ 0`, item 39). The Fröhlich–Pizzo hypotheses that L3 and L89 leave unchecked are checked here (item 37).

### 1.6 Outline items not carried into `SMG1.md`

The distiller dropped or softened these outline lines. They are listed so that no later pass restores them.

| # | Outline line | Verdict | Note |
|---|---|---|---|
| 55 | `O31`, `O239`: "every prior repository attempt on file stops at it" (decoupling) | ERROR | The digest's failed-attempt table (`prior/SMG1.md` lines 55-74) also records failures at other steps: stability ("persistence is not established", line 66), anomaly ("index 16 = 0 with two tastes and 8 with one taste", line 61), symmetry ("keeps no Z4 inside U(1)_eps", line 60), gauging ("a cutoff-scale photon mass", line 69), carrier ("zero and not unitary", line 72). Fix: "the attempts on file that reach a gapped mirror stop at decoupling". |
| 56 | `O142`: `π` content "so it is excluded too" | ERROR | Weak convergence to zero hides it (§2.2). |
| 57 | `O168`: R1(e) with `\|θ\| ≤ t₀Δ₀/4` | ERROR | Strict inequality, as in `O344` and the source. |
| 58 | `O277`: labels of two codewords | ERROR | `u₁+u₃+u₄ = {1467}`, `u₁+u₂+u₃+u₄ = {1458}`; the outline swaps them. |
| 59 | `O304`: the example `Σ_x (−1)^x (i/2)γ_{x,a}γ_{x+1,a}` "gaps flavour `a`" | ERROR | It is gapless on `Z` (§2.3). Fix: `Σ_x (1+(−1)^x)(i/2)γ_{x,a}γ_{x+1,a}`. |
| 60 | `O332`, `O378`, `O407`, `O415`: a tick's intrinsic gap "never available" | INCOMPLETE | One example only in the outline. Lemma F (§2.4) proves the statement for every clustering, cell-invariant stationary state of every cell-covariant NN-a tick. |
| 61 | `O380`: "adding `2πP` to a gate's generator" | ERROR | It breaks `‖X_g‖ < π`. A valid example is in §2.7. |
| 62 | `O371`, `O413`: "Rung 1 closes at a proof", "Rung 1 is done" | ERROR | Under the binding rules a citation is never load-bearing. Proved: rung 1 at `θ = 0`, in the R-GEN reading. Conditional on Fröhlich–Pizzo Theorem 3.5: the open-segment gap at small `θ`. Open: R1-H (native proof, ring, infinite chain) and FLQ (stationarity at `θ ≠ 0`). `SMG1.md` L3 and L100 state this correctly. |
| 63 | `O19`, `O49`, `O51`: line citations | CORRECT (minor) | `VC1_5.md` line 50 is the proof of Theorem 2.1 (statement at line 48); `RCS1.md` Theorem 4 is at line 68, not 66. |
| 64 | `O198-O202`: R3(a) "carry over word for word except the stability step" | CORRECT (in substance) | The atom, the quadratic obstruction and the zero-hop theorem carry over by the same proofs. The cell group, the reflection and the number of hop layers change and must be restated. |

The outline's target theorem (`O113-O148`), rung statements (`O156-O214`), imports and proof assignments were checked against `SMG1.md` sections 1 and 6 and against the sources named there. Apart from items 55-64 and the W2.4 GAP, they are CORRECT as statements of a programme. The choice of trick C (decoupling) as the hardest step is a judgment, not a theorem; after the fix of item 55 it is consistent with the digest.

---

## 2. Notes, proofs and referee closures

### 2.1 Item 7: NN-a names gates, not generators

`SMG1.md` L16: "Write its certified gates as `exp(−iX_g)`, with `X_g` Hermitian and `‖X_g‖<π`." NN-a (`TOE_ASSEMBLY.md` line 235) says: "The factors certify a decomposition of the update." The factors are unitaries. NN-a names no generator. The sentence belongs to R-GEN (Definition 3), with this lemma.

**Lemma G0 (principal generator).** Let `g` be a unitary on a finite-dimensional space. A Hermitian `X` with `g = e^{−iX}` and `‖X‖ < π` exists if and only if `−1 ∉ spec g`. It is then unique.

*Proof.* If `‖X‖ < π`, then `spec X ⊂ (−π, π)`, so `spec g = e^{−i·spec X}` avoids `−1`. Conversely, write `g = Σ_j e^{−iλ_j}Q_j` with distinct `λ_j ∈ (−π, π)` and spectral projections `Q_j`, and put `X = Σ_j λ_jQ_j`. For uniqueness, let `X' = Σ_k μ_kR_k` be another such generator, in spectral form. Then `g = Σ_k e^{−iμ_k}R_k`. The map `μ ↦ e^{−iμ}` is injective on `(−π, π)`, so the `R_k` are the `Q_j` and `μ_k` is the matching `λ_j`. Hence `X' = X`. ∎

So R-GEN is fixed by NN-a's gates alone exactly when no gate has eigenvalue `−1`. A gate with eigenvalue `−1` (a swap, a parity gate) needs extra data. This is the test-4 condition of L112. The rung-1 gates satisfy it, by item 16.

### 2.2 Items 12, 13, 52: W2.4 and the channel at `π`

**The wording.** `O138`: "For every finite family of quasi-local operators, each rescaled by a power of `λ`, the scaling limit of the connected correlations exists and equals the corresponding correlation of a Wick polynomial in the free field of (W2.3)." `O387`, test 2: "the rescaling powers are existential per operator". The wording leaves the quantifier open; the outline's own test fixes it as existential.

**Universal reading: inconsistent.** L23's argument is valid. Take the two fields of W2.3 and raise both powers by one. The two-point function is multiplied by `λ²`. For a test function `f` with `∫ Z S_c f ≠ 0`, the smeared value diverges.

**Existential reading: vacuous.** Take any family `A₁,…,A_n` and put every power equal to `−1`. A connected `n`-point function of bounded operators is a finite sum of products of expectations, so it is bounded by `C_n ∏_i‖A_i‖`. Multiplied by `λ^{−n}`, it tends to zero uniformly, hence as a distribution. Zero is the correlation of the zero Wick polynomial. So every tick meets W2.4 in this reading. If the zero polynomial is excluded instead, a family whose correlations fall faster than every power of `λ` has no admissible power. That is what a gapped mirror is meant to give, so the reading then rejects exactly the theories W2 is meant to accept.

**The channel at `π`.** Let a smeared correlation have the form `∫(−1)^{⌊λt⌋}G(t)dt` with `G` continuous and of compact support. Pair the tick intervals `[k/λ, (k+1)/λ)` for even `k` with their right neighbours. The integral equals `Σ_{k even}∫_{k/λ}^{(k+1)/λ}(G(t) − G(t+1/λ))dt`. Its size is at most the length of the support times the modulus of continuity of `G` at `1/λ`, which tends to zero. So light content at quasi-energy `π` contributes zero to the limits of W2.3 and W2.4. It is invisible, not excluded. `O142` ("so it is excluded too") is an ERROR; L23's last two sentences are right.

**A repaired statement, proposed and not adopted.**

> **(W2.4′)** For quasi-local `A`, real `p` and `λ > 0`, put `A^{λ,p}(x,t) = λ^p α^{⌊λt⌋}(τ_{[λx]}A)` and `Ã^{λ,p}(x,t) = (−1)^{⌊λt⌋}A^{λ,p}(x,t)`. Call `(A, p)` *admissible* if the connected two-point functions of `A^{λ,p}` and of `Ã^{λ,p}` (each against its own adjoint at `(0,0)`) converge as distributions on `(x,t) ≠ (0,0)`. Then (a) for admissible `(A, p)`, the limit for `Ã^{λ,p}` is zero; (b) for admissible `(A₁,p₁),…,(A_n,p_n)`, the connected `n`-point functions of the `A_i^{λ,p_i}` converge on non-coinciding points to the connected correlations of Wick polynomials in the free field of (W2.3) and its derivatives.

Why each part is there. Admissibility removes the `λ²` blow-up of the universal reading: a power above the critical one makes the two-point function diverge. Clause (b) at the critical power removes the vacuity: an extra light field gives a nonzero limit that is not a free-16 correlation. Clause (a) catches light content at `π`: demodulation turns its vanishing weak limit into a nonzero one. A massive operator is admissible at every power, with limit zero, the zero polynomial.

Four tests. (1) C: it states W2's own clause "nothing else is light" and nothing of another part; like R-LIGHT, it should be adopted together with CH1's reading of "light", if at all. (2) P: every quantifier is fixed. (3) C: clause (b) asks for a free limit, which W2.3 already asks of the 16; it settles no gauge, family or breaking question. (4) P: each of admissibility, (a) and (b) answers one named failure above. Nothing here is adopted. The owner's choice is carried as W2-LIGHT.

The tie rule of item 11 is a separate, small fix: for example, "`[λx]` is the point of `2Z³` nearest to `λx`, ties broken toward the lexicographically least point".

### 2.3 Items 18, 20, 22, 25: the atom, the fourteen signs, the dimerised example

**Rebuild of Lemma 2.1 and Theorem 2.2.** The proofs at L41 and L45 were re-derived line by line; the outline's longer versions (`O277`, `O289`) agree. The two steps a reader must supply are short. (i) A Clifford monomial `c_u` with `u ≠ ∅` is traceless on `V = ΛC⁴`: for even `|u|` conjugate by `c_a`, `a ∈ u`, which gives `−c_u`. (ii) `W = −(Σ_{g∈S}g − 1 − g₈)`, because `1` is the only element of degree 0 and `g₈ = g₁g₂` the only one of degree 8. On `V_χ` this is `−16[χ=1] + 1 + χ(g₈)`.

**Sign rule.** For `u, v ⊆ {1,…,8}` and ordered products, `c_uc_v = (−1)^{N(u,v)}c_{u+v}`, where `N(u,v) = #{(a,b) ∈ u×v : a > b}` and `u+v` is the symmetric difference. *Proof*, by induction on `|v|`. For `v = {b}`, move `c_b` left past each `a ∈ u` with `a > b`; each step is one anticommutation; if `b ∈ u`, then `c_bc_b = 1`. For `v = v' ∪ {b}` with `b = max v`, the elements of `u + v'` above `b` are the elements of `u` above `b`, since `v'` has none. So `N(u,v) = N(u,v') + N(u,{b})`. ∎

**The fourteen terms.** With `g₁=−c_{1234}`, `g₂=−c_{5678}`, `g₃=−c_{1256}`, `g₄=−c_{1357}`, the sign rule gives the table below. The last column is Eq. (8) of Fidkowski–Kitaev, arXiv:0904.2197v3, read from the arXiv PDF (text extracted in `/tmp/toe-SMG1ref/`): "W = ĉ1ĉ2ĉ3ĉ4 + ĉ5ĉ6ĉ7ĉ8 + ĉ1ĉ2ĉ5ĉ6 + ĉ3ĉ4ĉ7ĉ8 −ĉ2ĉ3ĉ6ĉ7 −ĉ1ĉ4ĉ5ĉ8 + ĉ1ĉ3ĉ5ĉ7 + ĉ3ĉ4ĉ5ĉ6 + ĉ1ĉ2ĉ7ĉ8 −ĉ2ĉ3ĉ5ĉ8 −ĉ1ĉ4ĉ6ĉ7 + ĉ2ĉ4ĉ6ĉ8 −ĉ1ĉ3ĉ6ĉ8 −ĉ2ĉ4ĉ5ĉ7".

| Element | Product used | `N` | Element as `±c_u` | Sign in `W = −Σg` | FK Eq. (8) |
|---|---|---|---|---|---|
| `g₁`, `g₂`, `g₃`, `g₄` | definition | — | `−c_{1234}`, `−c_{5678}`, `−c_{1256}`, `−c_{1357}` | `+`, `+`, `+`, `+` | `+`, `+`, `+`, `+` |
| `g₁g₃` | `c_{1234}c_{1256}` | 5 | `−c_{3456}` | `+` | `+` |
| `g₁g₄` | `c_{1234}c_{1357}` | 4 | `+c_{2457}` | `−` | `−` |
| `g₂g₃` | `c_{5678}c_{1256}` | 13 | `−c_{1278}` | `+` | `+` |
| `g₂g₄` | `c_{5678}c_{1357}` | 12 | `+c_{1368}` | `−` | `−` |
| `g₃g₄` | `c_{1256}c_{1357}` | 6 | `+c_{2367}` | `−` | `−` |
| `g₁g₂g₃` | `−c_{1…8}c_{1256}` | 18 | `−c_{3478}` | `+` | `+` |
| `g₁g₂g₄` | `−c_{1…8}c_{1357}` | 16 | `−c_{2468}` | `+` | `+` |
| `g₁g₃g₄` | `−c_{1234}c_{2367}` | 3 | `+c_{1467}` | `−` | `−` |
| `g₂g₃g₄` | `−c_{5678}c_{2367}` | 11 | `+c_{2358}` | `−` | `−` |
| `g₁g₂g₃g₄` | `c_{1…8}c_{2367}` | 14 | `+c_{1458}` | `−` | `−` |

All fourteen agree. `[check]` agrees (exact traces against each monomial). FK's Eqs. (9)-(10), "ĉ2j−1 = (aj + a†j)" and "ĉ2j = −i(aj −a†j)", give `a_j = (ĉ_{2j−1} + iĉ_{2j})/2`, the convention of Definition 1. FK's Section II, after Eq. (18), also states the spectrum: "W annihilates 8−, has eigenvalue −14 on the state |ψ⟩∈8+ that is fixed by the so(7), and has eigenvalue 2 on the remaining vector". The GAP of L49 is closed: `W` of L33 equals FK's printed Eq. (8) term by term. The identification is credit only.

**The dimerised example (items 25, 59).** `O304` offers `Q_alt = Σ_x (−1)^x (i/2)γ_{x,a}γ_{x+1,a}` as an `S`-invariant term that "gaps flavour `a`". It does not. Put `s_0 = 1` and `s_{x+1} = (−1)^x s_x`, a sign pattern of period four. The automorphism `γ_{x,a} ↦ s_xγ_{x,a}` maps `Q_alt` to the uniform chain `Σ_x (i/2)γ_{x,a}γ_{x+1,a}`, because `(−1)^x s_xs_{x+1} = 1`. The uniform chain has one-body symbol `−2 sin k`, which vanishes at `k = 0, π`, and the sign change is a unitary on the one-body space. So `Q_alt` is gapless on `Z`. `[check]`: on a ring of 40 sites its smallest one-body energy is 0. A correct example is `Σ_x (1+(−1)^x)(i/2)γ_{x,a}γ_{x+1,a} = Σ_{x even} iγ_{x,a}γ_{x+1,a}`: it pairs each even site with its right neighbour, has one-body energies `±2`, is `S`-invariant, and is not invariant under one-site translation. L57's sentence, with "dimerized" meaning alternating strengths, is true.

### 2.4 Item 34: no intrinsic Floquet gap at a clustering vacuum (Lemma F)

Theorem 4.2 shows the effect for one tick. The general form needs only locality, translation and clustering.

**Setting.** `𝔄` is the quasi-local algebra of the carrier on `Z^d`, with local algebras `𝔄_X` for finite sets `X` of sites and links. `K` is the local gauge group, compact at each site. `𝔅⁺` is the set of gauge-invariant, matter-even elements of `𝔄`, and `𝔅⁺_loc` its local part. `𝔅⁺_loc` is dense in `𝔅⁺`: average a local approximant over the finitely many local gauge groups that act on it (this is the argument of `VC1_5.md` Theorem 2.1, line 50), then take its even part. Elements of `𝔅⁺_loc` with disjoint supports commute, being even.

**Hypotheses.**
(H1) `α` is an automorphism of `𝔄` with `α(𝔅⁺) = 𝔅⁺` and finite propagation: `α(𝔄_X) ⊆ 𝔄_{X_r}` for a fixed `r`, where `X_r` is the `r`-neighbourhood of `X`. An NN-a tick has both properties: its gates are even and it fixes every gauge generator.
(H2) `T` is an infinite group of lattice translations, acting by automorphisms `τ_y` with `τ_y(𝔄_X) = 𝔄_{X+y}`, `τ_y(𝔅⁺) = 𝔅⁺` and `τ_yα = ατ_y`.
(H3) `ω` is a state with `ω∘α = ω` and `ω∘τ_y = ω` for `y ∈ T`, and it clusters along `T` on `𝔅⁺_loc`: `ω(Aτ_y(B)) → ω(A)ω(B)` as `y → ∞` in `T`, for all `A, B ∈ 𝔅⁺_loc`.

Let `(π, Ω)` be the GNS pair of `ω`, `H⁺` the closure of `π(𝔅⁺)Ω`, and `U` the unitary on `H⁺` with `Uπ(A)Ω = π(α(A))Ω`. It is well defined because `ω∘α = ω`, and onto because `α(𝔅⁺) = 𝔅⁺`. `UΩ = Ω`, so `H₁ = H⁺ ⊖ CΩ` reduces `U`.

**Lemma F.** Under (H1)-(H3), if `H₁ ≠ {0}`, then `1 ∈ spec(U|H₁)`.

*Proof.* Step 1. `U|H₁` is unitary on a nonzero space, so its spectrum is nonempty. Pick `z` in it. A normal operator has its spectrum equal to its approximate point spectrum. So for `ε ∈ (0, 1/8)` there is a unit `ξ ∈ H₁` with `‖Uξ − zξ‖ < ε`. Pick `A₀ ∈ 𝔅⁺_loc` with `‖π(A₀)Ω − ξ‖ < ε` and put `A = A₀ − ω(A₀)1`. Then `η := π(A)Ω` is the projection of `π(A₀)Ω` onto `H₁`, so `‖η − ξ‖ < ε`, `ω(A) = 0`, and `‖Uη − zη‖ < 3ε`. Put `B = α(A) ∈ 𝔅⁺_loc`, so `π(B)Ω = Uη`.

Step 2. For `y₁,…,y_n ∈ T` put `A_n = ∏_jτ_{y_j}(A)` and `B_n = ∏_jτ_{y_j}(B)`. Then `π(B_n)Ω = Uπ(A_n)Ω`, since `α` is multiplicative and commutes with each `τ_y`. Choose the `y_j` one at a time, each so far from the earlier ones that the supports of the translates are pairwise disjoint and, for each `D ∈ {A*A, B*B, B*A, A}`, `|ω(P_m(D)τ_{y_{m+1}}(D)) − ω(P_m(D))ω(D)| < δ`, where `P_m(D) = ∏_{j≤m}τ_{y_j}(D)`. These are finitely many conditions, each true for all far `y` by (H3). Disjoint even factors commute, so `A_n*A_n = P_n(A*A)`, `B_n*B_n = P_n(B*B)`, `B_n*A_n = P_n(B*A)`. By induction on `m`, each `ω(P_n(D))` is within `nδ(1+‖A‖+‖B‖)^{2n}` of `ω(D)^n`.

Step 3. Put `a = ω(A*A) = ‖η‖²`. Then `ω(B*B) = ‖Uη‖² = a`, and `w := ω(B*A) = ⟨Uη, η⟩`. Write `Uη = zη + e` with `‖e‖ < 3ε`. Then `zw = a(1+ρ)` with `|ρ| ≤ 3ε/‖η‖ < 4ε`. Hence, with `η_n = π(A_n)Ω`,
`‖Uη_n − z^nη_n‖² = ω(B_n*B_n) − 2Re(z^nω(B_n*A_n)) + ω(A_n*A_n)`,
which is within `4nδ(1+‖A‖+‖B‖)^{2n}` of `2a^n Re(1 − (1+ρ)^n) ≤ 2a^n((1+4ε)^n − 1)`. Also `‖η_n‖²` is within the same error of `a^n ≥ (1−ε)^{2n}`, and `|⟨Ω, η_n⟩| = |ω(A_n)|` is within it of `ω(A)^n = 0`. Let `η'_n` be the projection of `η_n` onto `H₁`. Since `UΩ = Ω`, `‖Uη'_n − z^nη'_n‖ ≤ ‖Uη_n − z^nη_n‖ + 2|⟨Ω,η_n⟩|`. For fixed `n`, letting `ε → 0` and then `δ → 0` makes `‖Uη'_n − z^nη'_n‖/‖η'_n‖` as small as we like. So `z^n` is an approximate eigenvalue of `U|H₁`, hence in its spectrum, for every `n ≥ 1`.

Step 4. Among `z, z², …, z^{N+1}` two, say `z^j` and `z^k` with `j > k`, lie within arc length `2π/N`. Then `|z^{j−k} − 1| ≤ 2π/N` with `1 ≤ j−k ≤ N`. The spectrum is closed, so it contains `1`. ∎

**Corollary F1.** Let `α` be any NN-a tick that commutes with the cell translations, and `ω` any stationary, cell-invariant state that clusters along them on `𝔅⁺_loc` and has `H₁ ≠ {0}`. Then the GNS unitary of the tick on the vacuum-orthogonal part of the invariant sector has `1` in its spectrum. The same holds on the larger sector `closure(π(𝔄^K)Ω) ⊖ CΩ`, which `H₁` reduces. So a spectral gap of a tick around its vacuum eigenvalue never exists at such a state, for any step size and any interaction.

`ω₀` of Theorem 4.1 meets (H3) exactly: for even local `A, B` with disjoint supports, `ω₀(AB) = ω₀(A)ω₀(B)`. With `A = K_x` the lemma reproduces Theorem 4.2 with `z = e^{16iτ}`. Clustering is a hypothesis here. Pure translation-invariant states of quantum spin systems are known to cluster (a Powers-type theorem); that fact is cited as context and not used. Lemma F says nothing about FLQ, which asks whether a stationary state exists near the generator's ground state at `θ ≠ 0`. It does show that the outline's general sentences (item 60) are true for clustering states, and that some reading of "gap" other than the intrinsic one is needed. Which reading is the owner's choice (Q1).

### 2.5 Items 35-39: Lemma 5.1 against Fröhlich–Pizzo Theorem 3.5

Read: arXiv:1812.02457v2 (dated 27 Feb 2019), text extracted from the arXiv PDF in `/tmp/toe-SMG1ref/`. The published version (Commun. Math. Phys. 375 (2020)) was not read; its numbering may differ. Quoted lines, as printed:

- (1.1): "`H(N) := ⊗_{j=1}^N H_j`, where `H_j ≅ C^M`, ∀j = 1, 2, . . . , and where M is an arbitrary, but N-independent finite integer."
- Before (1.2): "Let H be a positive M×M matrix with the properties that 0 is an eigenvalue of H corresponding to an eigenvector Ω ∈ C^M, and `H|_{{CΩ}^⊥} ≥ 1`." (1.2) puts this one `H` in the `i`-th slot.
- (1.4): "`P_Ω H_i P_Ω = 0`, `P^⊥_Ω H_i P^⊥_Ω ≥ P^⊥_Ω`."
- (1.5)-(1.6): `K_N(t) := Σ_i H_i + t Σ_{I_{k;i}⊂I_{N−1;1}, k≤k̄} V_{I_{k;i}}`, where "Ik;i is the 'interval' given by {i, . . . , i + k}" and "VIk;i is a symmetric matrix acting on H(N) with the property that VIk;i acts as the identity on" the factors outside `I_{k;i}`.
- (1.7): "Without loss of generality, we may assume that `‖V_{I_{k;i}}‖ ≤ 1`."
- Theorem 3.5: "Under the assumption that (1.4), (1.6) and (1.7) hold, the Hamiltonian KN defined in (1.5) has the following properties: There exists some t0 > 0 such that, for any t ∈R with |t| < t0, and for all N < ∞, (i) KN ≡KN(t) has a unique ground-state; and (ii) the energy spectrum of KN has a strictly positive gap, ∆N(t) ≥1/2, above the ground-state energy."

**Match.** Lemma 5.1 gives `M = 64` and one on-site matrix `H = (h^{FK} + h⁵ + e)/Δ₀` on `C³² ⊗ C²` for every factor; the dummy link at `x = N` is what makes the last factor equal to the others. `H ≥ 0` has kernel `C(ψ ⊗ |0⟩₅ ⊗ |+⟩)` and `H ≥ 1` on its complement: this is (1.4). `V_{I_{1;x}} = Jb_{(x,x+1)}J*/4` is Hermitian, acts as the identity outside factors `x, x+1`, and has norm 1: this is (1.6) and (1.7) with `k̄ = 1`; the `k = 0` terms are zero. So the printed theorem applies, with `t = 4θ/Δ₀`, and Theorem 5.2 holds for `|θ| < t₀Δ₀/4`, uniformly in `N`.

**Status.** The hypotheses are now checked. The theorem itself is cited, not rebuilt. Under the binding rules a citation is never load-bearing, so Theorem 5.2 stays a conditional result, and the native rebuild with its ring and infinite-chain forms stays open as R1-H. L3's sentence "its precise hypotheses have not been independently checked here" should be replaced (edit E5). The strict threshold of L89 agrees with the source.

### 2.6 Item 45: the form of the allowed mixing terms (Lemma M)

`O182`: "So `H_mix` starts at quartic order: a light bilinear times an `S`-invariant mirror operator." L101 says this does not give every allowed term. Both are right; the complete form is short.

**Lemma M.** On the 1D carrier, let `S` act by `γ_g` on modes 1-4 of every site and `U(1)₅` by `Ad e^{iφN₅}`, `N₅ = Σ_x n_{x,5}`. Let `𝔐` be generated by the mirror Majoranas `γ_{x,a}` (`a ≤ 8`) and `𝔏` by `γ_{x,9}, γ_{x,10}`. (i) Every local operator invariant under `S × U(1)₅` is a finite sum `Σ_i M_iL_iΛ_i`, with `M_i ∈ 𝔐` `S`-invariant, `L_i ∈ 𝔏` `U(1)₅`-invariant and `Λ_i` a link operator. (ii) A non-constant `S`-invariant mirror monomial has degree at least 2, and degree 2 only for a same-flavour pair `γ_{x,a}γ_{y,a}`. (iii) A non-constant `U(1)₅`-invariant light monomial (in `c_{x,5}, c†_{x,5}`) has even degree at least 2. (iv) Hence genuine mixing (`M_i` and `L_i` both non-constant) has degree at least 4, and degree 4 only as a same-flavour mirror pair times a number-conserving light pair.

*Proof.* (i) Each `g_x` is even and lives on modes 1-4, so `γ_g` fixes `𝔏` and the links; `N₅` is even and lives on mode 5, so `Ad e^{iφN₅}` fixes `𝔐` and the links. The averages `E_S = 16^{−1}Σ_gγ_g` and `E_U = (2π)^{−1}∫dφ Ad e^{iφN₅}` therefore commute and act on each factor of a product `mlλ` of monomials separately. An invariant `X` equals `E_SE_U(X) = Σ E_S(m)E_U(l)λ`. (ii) `γ_g` multiplies a mirror monomial by `(−1)^{u·f}`, where `u` is the support of `g` and `f ∈ F₂⁸` counts the factors of each flavour mod 2. Invariance for all `g` means `f ∈ C^⊥ = C`, whose words have weight 0, 4 or 8. Degree 1 or 3 would need a word of weight 1 or 3; degree 2 needs `f = 0`. (iii) Invariance means equal numbers of `c` and `c†`. (iv) follows. ∎

So the allowed terms are pure light terms, pure mirror terms, and mixing terms of degree at least four. Higher mixing occurs: `W_x n_{x,5}` has degree six and is invariant. Local gauge invariance adds link strings and changes no degree. Nothing here gives a Luttinger limit; R1.5-D stays open.

### 2.7 Item 51: two facts about R-GEN

**Decomposition dependence within the bound.** Let `A, B` be Hermitian on one edge triple, with `‖A‖, ‖B‖ < π`. Then `e^{−iA}e^{−iB} = e^{−iB}e^{−iA''}` with `A'' = e^{iB}Ae^{−iB}` and `‖A''‖ = ‖A‖ < π`. Both sides are NN-a decompositions of one update (two layers on one triple). R-GEN gives `A + B` for the first and `B + A''` for the second; they differ whenever `[A, e^{−iB}] ≠ 0`. In the rung-1 model take `A = h_x + h_{x+1} + e_ℓ` and `B = θb_ℓ`: `[H₀, b_ℓ]Ψ = (28τ+τ_E)b_ℓΨ ≠ 0`, so `[A, e^{−iθb_ℓ}] = −iθ[A, b_ℓ] + O(θ²) ≠ 0` for small `θ ≠ 0`. So the reading must name the decomposition, as L112 says; the `2πP` example of `O380` is not needed.

**The conjugated tick (`O381`).** Let `U₀ = L₂L₁`, `V = L₄L₃` and `U' = VU₀V*`, the NN-a tick with layers `L₄, L₃, L₂, L₁, L₃*, L₄*` in that order of writing. The hop generators `θb` and `−θb` cancel, so R-GEN assigns `H₀` to `U'`. *Claim.* On a segment with `N ≥ 2` sites, if `E₁ := 28τ + τ_E ∉ 2πZ`, then `Ψ` is not stationary under `U'` for all small `θ ≠ 0`. *Proof.* Put `β = Σ_ℓ b_ℓΨ`. Each `b_ℓΨ = (i/2)Σ_a (c_aψ)_x ⊗ (c_aψ)_{x+1} ⊗ |−⟩_ℓ` (other factors unchanged) is nonzero, with `H₀`-energy `14τ + 14τ + τ_E = E₁`; different links give orthogonal vectors. So `β ≠ 0` and `H₀β = E₁β`. Also `V*Ψ = Ψ + iθβ + R` with `‖R‖ ≤ C_Nθ²`. Suppose `U'Ψ = cΨ`. Then `U₀V*Ψ = cV*Ψ`. Pair with `Ψ`, using `U₀*Ψ = Ψ`: `⟨Ψ,V*Ψ⟩ = c⟨Ψ,V*Ψ⟩`, and `⟨Ψ,V*Ψ⟩ = 1 + O(θ²) ≠ 0`, so `c = 1`. Pair with `β`, using `U₀*β = e^{iE₁}β`: `e^{−iE₁}⟨β,V*Ψ⟩ = ⟨β,V*Ψ⟩`, and `⟨β,V*Ψ⟩ = iθ‖β‖² + O(θ²) ≠ 0`. So `e^{−iE₁} = 1`, a contradiction. ∎ `[check]` (two sites, modes 1-4, one link, `τ = 0.1`, `τ_E = 0.5`): `|⟨Ψ,U'Ψ⟩| = 0.961` at `θ = 0.1` and `0.9996` at `θ = 0.01`. Meanwhile `U' = e^{−iVH₀V*}` has the stationary ground state `VΨ`. So the R-GEN ground state need not be a state of the tick's dynamics, which is why Definition 4 asks for stationarity separately. The outline's example is correct, with the condition `28τ+τ_E ∉ 2πZ` added.

---

## 3. Required edits to `SMG1.md`

None of these changes a proved theorem. E1-E7 fix errors or close named steps; E8-E15 record the referee closures, which the lead may copy or cite.

1. **E1 (item 7, L16).** Move "Write its certified gates as `exp(−iX_g)` …" from Definition 2 to Definition 3 and mark it as R-GEN data, not NN-a text. Add Lemma G0 (§2.1): such `X_g` exists and is unique if and only if `−1 ∉ spec g`. Add: under NN-a's "pairwise disjoint edge triples", the link layer `L₂` is two NN-a layers.
2. **E2 (item 12, L21).** Replace "under **every** choice of rescaling powers" by the outline's words, "each rescaled by a power of `λ`", and say that the universal reading is inconsistent and the existential reading (the outline's test 2) is vacuous.
3. **E3 (item 13, L23).** Add the vacuity argument and the one-line weak-convergence proof for the `π` channel (§2.2). Record W2.4′ as a proposal, not adopted, with its four tests, or cite this report. Name the open item W2-LIGHT and add it to L7.
4. **E4 (item 11, L20).** Fix a tie rule for `[λx]`, for example toward the lexicographically least nearest point.
5. **E5 (items 1, 35, 37; L3, L81, L85, L89).** In L3, replace "its precise hypotheses have not been independently checked here" by "its hypotheses (1.4), (1.6), (1.7) were checked against arXiv:1812.02457v2 (`SMG1_REFEREE.md` §2.5); the theorem is cited, not rebuilt". In Lemma 5.1, add "with one on-site matrix at every factor; the dummy link makes the last factor equal to the others". In Theorem 5.2, replace "Assume … applies" by "By Theorem 3.5 of arXiv:1812.02457v2, whose hypotheses Lemma 5.1 meets". Keep the conditional status and R1-H.
6. **E6 (item 22, L49).** Replace the GAP by: "Closed at pass 3: the fourteen signs, computed by hand (`SMG1_REFEREE.md` §2.3), agree term by term with Eq. (8) of arXiv:0904.2197v3; its Eqs. (9)-(10) give the convention of Definition 1. Credit only."
7. **E7 (item 31, L71).** Cite "`VC1_5.md` Theorem 2.1 (line 48)" in place of "`VC1_5.md`, section 1".
8. **E8 (item 34, L77).** Add Lemma F and Corollary F1 (§2.4), or cite them, as the scoped general statement: under (H1)-(H3) a tick has no spectral gap at its vacuum eigenvalue. Keep FLQ open. Keep "a generator is the only meaningful notion" out of the theorem; it is Q1.
9. **E9 (item 45, L101).** Replace the GAP sentence by Lemma M (§2.6): the allowed terms are pure light, pure mirror, and mixing terms of degree at least four, of the form (`S`-invariant mirror operator)·(`U(1)₅`-invariant light operator).
10. **E10 (item 51, L112).** Replace "does not demonstrate dependence within its premises" and "its generic nonstationarity was not independently checked here" by the two facts of §2.7: a valid example of decomposition dependence within the bound, and non-stationarity of `Ψ` under the conjugated tick when `28τ+τ_E ∉ 2πZ`.
11. **E11 (item 25, L57).** Give the correct example `Σ_x (1+(−1)^x)(i/2)γ_{x,a}γ_{x+1,a}` and say that the alternating-sign form of `O304` is gapless, so that no later pass copies it.
12. **E12 (item 21, L47).** Replace "was not present at that path in this working folder" by the repository location: branch `docs/consolidate-chirality-doublers`, `docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` line 2341, status "logged".
13. **E13 (item 24, L55).** "generate `Cl₈(C)≅M₁₆(C)`" becomes "generate a nonzero quotient of `Cl₈(C)≅M₁₆(C)`, hence `M₁₆(C)`, because that algebra is simple".
14. **E14 (L112, Q1).** Frame Q1 with its consequences (§5 below).
15. **E15 (L113, Q2).** Frame Q2 as in §5 below: the target text already makes `ν^c` light; W2.1 adds protection of the whole 16 by the exact `G`, which forces `G ⊋ G_SM`.

## 4. Open statements to carry, by name

Each is a statement, not a failed lemma. None was attacked here beyond what the table records; this report is a check of `SMG1.md`, and these items belong to later lanes.

- **R1-H.** A native proof (not a citation) that `H(θ)` has a unique ground state and a gap of at least a fixed fraction of `Δ₀` for `|θ|` below a fixed multiple of `Δ₀`, uniformly on open segments, on even rings, and in infinite volume (for the GNS generator of the unique infinite-volume ground state). With R1-H, Theorem 5.2 becomes unconditional.
- **FLQ.** For small `θ ≠ 0`: a state on `𝔄` that is stationary under the rung-1 tick, pure on `𝔄^K`, cell- and `S`-invariant, and equal to the ground state of `H(θ)` on local observables up to `O(θ)`. Lemma F does not bear on it. The conjugated tick (§2.7) shows that R-GEN alone does not supply it.
- **R0-U5, R1.5-D, R2, R3-H, R3-D, W2.** As stated in `SMG1.md` section 6, with E9's form of the mixing terms for R1.5-D.
- **W2-LIGHT (new).** The owner's choice of a criterion for "nothing else is light" in W2. W2.4 as written fails in both readings (§2.2); W2.4′ is a proposal with four tests `C, P, C, P`.
- **Owner questions Q1 and Q2**, framed as in §5.

## 5. Owner questions Q1 and Q2: framing and four tests

The tests are those of `TOE_ASSEMBLY.md` lines 173-176, quoted at item 50. The owner's guidance ("we can specify if needed") is followed: each question asks for a specification only where the texts leave a meaning open.

**Q1 (R-GEN as the meaning of "gap").** `SMG1.md` L112: "Q1 asks whether the owner accepts R-GEN for this part." The question is framed correctly and adopts nothing. It should state what each answer implies (edit E14).
- *Yes:* rung 1 holds at `θ = 0` (Theorem 4.1), and on open segments for `|θ| < t₀Δ₀/4` given Fröhlich–Pizzo (Theorem 5.2). Stationarity at `θ ≠ 0` stays FLQ. The law must name its gates, because the generator depends on the decomposition (§2.7); a gate with eigenvalue `−1` needs extra data (Lemma G0).
- *No* (the intrinsic reading): by Lemma F, no clustering, cell-invariant stationary state of any cell-covariant NN-a tick has a gap. Rung 1's "gap" then needs some other specification.

Four tests of R-GEN: (1) C. It fixes the meaning of a word in SMG1's own target (`TOE_ASSEMBLY.md` line 718: "with a gap and a symmetric unique ground state"), which is test 1's subject. It passes only as the owner's specification of SMG1's own words, scoped to SMG1 and not used for VC1's vacuum. (2) P, given that the law names its gates (NN-a: "The factors certify a decomposition of the update"). (3) C. It passes while FLQ stays open and no stationarity is inferred from it. (4) C. The generators are not NN-a data; they are fixed by the gates exactly when no gate has eigenvalue `−1`. The draft's `C, P, C, P` becomes `C, P, C, C`, as L112 says.

**Q2 (clause W2.1 and a light, protected `ν^c`).** `SMG1.md` L113: "Q2 asks whether W2.1 and a symmetry-protected `ν^c` are intended." The framing is correct, with one sharpening (edit E15). The owner's sentence already makes `ν^c` light: "whose light sector is one Weyl 16 of Spin(10)" (`TOE_ASSEMBLY.md` line 718), and the 16 contains `ν^c`. What W2.1 adds is protection: no `G`-invariant mass for any light field, which forces `G ⊋ G_SM` (L25). Both live laws provide such a `G`: on `L5-U` the `U(1)_N` charges `u, −3u, 5u` have no pair summing to zero; on `L5-O`, `Sym²(16) = 10 ⊕ 126` has no singlet. If W2.1 is dropped, the rest of W2 is a well-formed existence statement, and a light `ν^c` would be unprotected.

Four tests of W2.1: (1) C, a clause of W2's own target. (2) P, a definite condition. (3) C. It settles by premise that the lightness of the whole 16 is protected by an exact symmetry larger than `G_SM`; that choice is the owner's. (4) P. `G ⊋ G_SM` is exactly what protection needs. This agrees with the outline's test 3 for R-LIGHT (`O388`).

Neither question is decided here.

## 6. Freeze recommendation

**Freeze `SMG1.md` after edits E1-E15, with its open statements named (§4).** Every result that `SMG1.md` marks as proved was re-derived and holds: Lemma 2.1, Theorem 2.2, Theorem 3.1, Theorem 3.2, Theorem 4.1, Theorem 4.2, Lemma 5.1 and Proposition 5.3. Theorem 5.2 holds as a conditional result on Fröhlich–Pizzo Theorem 3.5, whose printed hypotheses Lemma 5.1 meets (§2.5). The three ERRORs are an attribution in a definition (L16), a paraphrase of the outline (L21) and a line citation (L71). The one INCOMPLETE item is a tie rule (L20). Of the five GAPs listed at L5, three are closed here (items 22, 34, 45, with 51), and two stay open by name (W2-LIGHT, FLQ).

On the decisions the lane brief names:
- **Hamming re-proof of Fidkowski–Kitaev.** Correct. Spectrum `−14` (1), `0` (8, odd), `2` (7, even); unique `S`-fixed ground vector; no computer needed. The FK identification GAP was real and is closed (§2.3).
- **`S = Z₂⁴` with translation forbids every quadratic mass.** Correct (Theorem 3.1): eigenspaces of dimension divisible by 16 on every ring; zeros at `k = 0, π` on `Z`. Translation is needed; the outline's example of that need is wrong and has a one-line fix (§2.3).
- **Zero-hop tick.** Correct (Theorem 4.1): NN-a (with `L₂` as two layers), gauge invariant, symmetric, `U = e^{−iH₀}`, unique ground state with gap at least `Δ₀` in finite and infinite volume, pure on `𝔄` and on `𝔄^K`.
- **Eight-Majorana minimum within sign-flip symmetries.** Correct (Theorem 3.2).
- **No intrinsic Floquet gap.** Correct for the tick of Theorem 4.2. The distiller's GAP about the general statements was real; Lemma F now proves them for every clustering, cell-invariant stationary state of every cell-covariant NN-a tick.
- **Reduction to Fröhlich–Pizzo Theorem 3.5.** Correct; hypotheses checked against the printed text; the threshold is strict.
- **W2.4 quantifier GAP.** Real, and wider than L23 says: the universal reading is inconsistent and the existential one vacuous. Repair W2.4′ proposed, not adopted (W2-LIGHT).
- **Outline.** Target theorem, ladder, imports and proof assignments are sound as a programme, apart from items 55-64 and W2.4. The hardest-step judgment (decoupling) stands after the fix of item 55.
- **Q1 and Q2.** Framed correctly as owner questions; both need the sharpenings of §5. R-GEN's tests are `C, P, C, C`; W2.1's are `C, P, C, P`.

No second referee pass is needed if E1-E15 are applied as written. One check is advised before downstream parts cite Lemma F (§2.4), because it is the one new general theorem in this report and VC1, CH1 and MT1 would meet it.

## 7. Prior work used

| Prior result | Path | Use here |
|---|---|---|
| The pass-1 draft of SMG1 (Claude Opus 5.5) | `SMG1_OUTLINE.md` at `494ffe935` | The source each verdict was checked against; its proofs `O277-O346` agree with `SMG1.md` apart from items 55-64. |
| The pass-2 distillation (Codex gpt-6.1-terra) | `SMG1.md` at `a7fa25536` | The text refereed. |
| The prior-work digest | `prior/SMG1.md`, read in full; failed-attempt table lines 55-74 | Item 55. |
| #10078: Cayley form spectrum `-14 (1), 0 (8, odd), +2 (7, even)`, logged | `origin/docs/consolidate-chirality-doublers` (`a1bced899`), `docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` line 2341; the note itself on `origin/claude/toe-cayley-mirror-gap-20261021` (`d2b189516`), lines 4, 34 | Item 21: the precursor exists in the repository at these paths. |
| Gauge averaging, density of local invariant observables, purity on `𝔄^K` equals extremality among gauge-invariant states | `VC1_5.md` Theorem 2.1, line 48 (proof line 50), frozen | Items 9, 31; the setting of Lemma F. |
| Every element of `𝔄^G` is matter-even | `RCS1.md` Theorem 4, line 68, frozen | Item 10. |
| F3a: chirality at 0 equals chirality at `π` for free updates | `CH1.md` line 62, frozen | Item 14. |
| C2-5: ten triple products are not ten CAR modes | `CH1.md` line 126, frozen | Item 43. |
| RC-W | `CG16S.md` line 120, frozen | Item 14. |
| Theorem N and Corollary 2.2: no invertible covariant finite link for infinite images | `GA2_Y2.md` lines 39, 43, frozen | Items 40-41 (finite `S` is outside N's scope). |
| The four smuggle tests; NN-a; the W2 target | `TOE_ASSEMBLY.md` lines 173-176, 235, 718 | Items 7, 16, 50; §5. |
| The FK rebuild map ("Rebuild the Clifford identities, uniqueness, exact first excited energy and antiunitary action") | `LIT_SMG.md` line 202 | §2.3 completes the sign identities of the fourteen terms. |

**Missed by the digest, added here.** `CH1_5UQ.md` (frozen 2026-11-06), status line 9: "Separated local odd fields have zero undressed two-point function at all times; the same excludes Weyl falloff for fields with sufficiently fast norm tails (Theorem 2.2)." It bears on W2.3 for the gauged variants W2[L5-U] and W2[L5-O]: without a dressing prescription, W2.3's limit for local odd fields is zero. So the charged-sector clause of Definition 5 (L19) is necessary, not optional. The digest cites this file only at line 126. Its line 26 also fixes the GNS unitary `Ũπ(A)Ω = π(α(A))Ω` used here and in Theorem 4.2. The search for prior results on the Floquet spectrum of a tick (grep for "Floquet", "GNS unitary", "gap of the tick" in this folder) found no result like Lemma F.

**Literature, credited and not load-bearing for any proof here.** L. Fidkowski and A. Kitaev, arXiv:0904.2197v3 (Phys. Rev. B 81, 134509 (2010)): Eqs. (8)-(11) and the spectrum sentence of Section II, read for the identification in §2.3 only. J. Fröhlich and A. Pizzo, arXiv:1812.02457v2 (Commun. Math. Phys. 375 (2020)): Section 1.1-1.2 and Theorem 3.5, read to check the hypotheses of `SMG1.md`'s own cited step. Powers-type clustering of pure states is mentioned as context in §2.4 and not used.

---

## FINISH

**Proved (pass 3, referee closures; not yet checked by another pass).**
- Lemma G0 (§2.1): a gate has a Hermitian generator of norm below `π` if and only if `−1` is not an eigenvalue, and it is then unique.
- The sign rule and the fourteen-sign table (§2.3): `W` of `SMG1.md` equals Fidkowski–Kitaev's printed Eq. (8) term by term. The FK identification GAP is closed.
- Lemma F and Corollary F1 (§2.4): for every NN-a tick commuting with an infinite group of cell translations, and every stationary, cell-invariant state that clusters along them, the GNS unitary on the vacuum-orthogonal part of the invariant sector has `1` in its spectrum.
- Lemma M (§2.6): every `S × U(1)₅`-invariant operator is a sum of products of `S`-invariant mirror and `U(1)₅`-invariant light operators; genuine mixing starts at degree four.
- §2.7: decomposition dependence of R-GEN within the bound `‖X_g‖ < π`; non-stationarity of `Ψ` under the conjugated tick when `28τ+τ_E ∉ 2πZ` and `θ ≠ 0` is small.
- §2.5: the hypotheses (1.4), (1.6), (1.7) of Fröhlich–Pizzo Theorem 3.5 hold for Lemma 5.1's chain. The theorem stays cited.
- The verdicts of §1: all results that `SMG1.md` marks as proved hold.

**Counterexamples.**
- `O304`: the alternating-sign term `Σ_x (−1)^x (i/2)γ_{x,a}γ_{x+1,a}` is gapless on `Z`, so it does not illustrate the need for translation (§2.3).
- `O380`: adding `2πP` to a gate's generator breaks `‖X_g‖ < π`.
- W2.4 as written: the universal reading contradicts W2.3 (the distiller's argument, confirmed); the existential reading is satisfied by every tick (§2.2).
- `O142`: light content at quasi-energy `π` is not excluded by W2.3-W2.4; it converges weakly to zero (§2.2).
- `O31`, `O239`: "every prior repository attempt on file stops at" decoupling is contradicted by the digest's own failed-attempt table (item 55).

**Open by name.** R1-H; FLQ; R0-U5; R1.5-D; R2; R3-H; R3-D; W2; W2-LIGHT (new: the owner's criterion for "nothing else is light", with W2.4′ proposed). Owner questions Q1 (R-GEN for "gap", tests `C, P, C, C`) and Q2 (clause W2.1, a protected light 16 including `ν^c`, tests `C, P, C, P`). No lemma in this report failed three attacks.

**What changes downstream.**
- **SMG1.** Freeze after edits E1-E15 (§3). Theorem 5.2 keeps its conditional status, with its hypotheses now checked.
- **VC1, CH1, MT1 and any part that speaks of a tick's gap.** Lemma F replaces the outline's one example: at every clustering, cell-invariant stationary state of a cell-covariant NN-a tick, the intrinsic gap is absent. A part needs the generator reading R-GEN or another owner specification. One check of Lemma F is advised before such a part cites it.
- **R1.5 lane.** Start from Lemma M's form of the allowed terms.
- **W2 and CH1-i.** W2.4 needs the owner's choice (W2-LIGHT). For the gauged variants, `CH1_5UQ.md` Theorem 2.2 makes D6's charged-sector clause necessary.
- **`LIT_SMG.md` line 202.** The Clifford-identity item for the Fidkowski–Kitaev block is complete (§2.3, with Theorem 2.2 of `SMG1.md`).
- **Frozen parts and axioms.** None changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. No law, reading or working-set entry is adopted.
